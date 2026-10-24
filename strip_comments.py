#!/usr/bin/env python3
"""Build the LLM input bundle for SWE 439 HW1.

Removes comments and blank lines from every .java file under a source directory
(string literals, char literals and text blocks are preserved), skips
package-info.java (comments only), writes the stripped copies to an output
directory, and concatenates them into one bundle file with a header line
"// ===== FILE: <path relative to the source dir> =====" before each file.
Files are ordered alphabetically by relative path.

Usage:
    python3 strip_comments.py <src/main/java dir> <stripped output dir> <bundle file>

Example (Apache Commons CLI, commit bc23215cff121397c6c473a0633e5a7b77055511):
    python3 strip_comments.py commons-cli/src/main/java stripped_src commons-cli-scope.txt
"""
import os
import sys


def strip(s: str) -> str:
    out = []
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        d = s[i + 1] if i + 1 < n else ''
        if s.startswith('"""', i):                      # text block
            j = s.find('"""', i + 3)
            while j != -1 and s[j - 1] == '\\':
                j = s.find('"""', j + 1)
            out.append(s[i:j + 3])
            i = j + 3
        elif c == '"':                                  # string literal
            j = i + 1
            while s[j] != '"':
                j += 2 if s[j] == '\\' else 1
            out.append(s[i:j + 1])
            i = j + 1
        elif c == "'":                                  # char literal
            j = i + 1
            while s[j] != "'":
                j += 2 if s[j] == '\\' else 1
            out.append(s[i:j + 1])
            i = j + 1
        elif c == '/' and d == '/':                     # line comment
            j = s.find('\n', i)
            i = n if j == -1 else j
        elif c == '/' and d == '*':                     # block / Javadoc comment
            j = s.find('*/', i + 2)
            i = j + 2
            out.append(' ')
        else:
            out.append(c)
            i += 1
    return ''.join(out)


def main() -> None:
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    src, out_dir, bundle_path = sys.argv[1:]
    files = []
    for root, _, names in os.walk(src):
        for f in names:
            if f.endswith('.java') and f != 'package-info.java':
                files.append(os.path.relpath(os.path.join(root, f), src))
    files.sort()
    bundle = []
    for rel in files:
        with open(os.path.join(src, rel), encoding='utf-8') as fh:
            text = strip(fh.read())
        lines = [ln.rstrip() for ln in text.split('\n')]
        text = '\n'.join(ln for ln in lines if ln.strip()) + '\n'
        dest = os.path.join(out_dir, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, 'w', encoding='utf-8') as fh:
            fh.write(text)
        bundle.append(f"// ===== FILE: {rel} =====\n{text}")
    with open(bundle_path, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(bundle))
    print(f"{len(files)} files -> {out_dir} and {bundle_path}")


if __name__ == '__main__':
    main()
