#!/usr/bin/env bash
# Reproduces the tool side of SWE 439 HW1 (LOC, input bundle, PMD results).
# Requirements: git, python3, pygount (pip install pygount), JDK 17+ (java, javac),
# and PMD 7.28.0 unpacked somewhere (https://github.com/pmd/pmd/releases/tag/pmd_releases%2F7.28.0).
# Usage:  PMD_HOME=/path/to/pmd-bin-7.28.0 ./reproduce.sh
# Run it from the folder that contains strip_comments.py and pmd-ruleset.xml.
# Everything it creates (clone, stripped sources, bundle, classes) goes into ./repro_out/
# so your submission folder is not changed. Delete repro_out/ afterwards if you like.
set -euo pipefail
: "${PMD_HOME:?Set PMD_HOME to the unpacked pmd-bin-7.28.0 folder}"
HERE="$(pwd)"
mkdir -p repro_out && cd repro_out
COMMIT=bc23215cff121397c6c473a0633e5a7b77055511

# 1. Get the exact source version
[ -d commons-cli ] || git clone https://github.com/apache/commons-cli.git
git -C commons-cli checkout "$COMMIT"

# 2. Lines of code (SLOC = non-blank, non-comment). Expected: 36 files, 2,842 code lines
pygount --format=summary --suffix=java commons-cli/src/main/java

# 3. Strip comments and build the bundle uploaded to the LLMs (expected: 34 files)
python3 "$HERE/strip_comments.py" commons-cli/src/main/java stripped_src commons-cli-scope.txt
sha256sum commons-cli-scope.txt        # should start with 8e3ad4c1bb341411
if [ -f "$HERE/commons-cli-scope.txt" ]; then
  cmp commons-cli-scope.txt "$HERE/commons-cli-scope.txt" && echo "OK: identical to the submitted commons-cli-scope.txt"
fi

# 4. Check the stripped code still compiles
mkdir -p classes && javac -nowarn -d classes $(find stripped_src -name '*.java')

# 5. Run PMD on the stripped code with the HW ruleset (expected: 22 detections)
"$PMD_HOME/bin/pmd" check -d stripped_src -R "$HERE/pmd-ruleset.xml" -f text --no-cache
