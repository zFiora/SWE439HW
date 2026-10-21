# SWE 439 – Homework 1: Code Smell Detection (PMD vs ChatGPT vs DeepSeek)

Compares code-smell detections from a static analysis tool (**PMD 7.28.0**) and two LLMs (**ChatGPT**, proprietary, and **DeepSeek**, open-weight) on **Apache Commons CLI** (Java, 34 files, 2,840 LOC). Smells: Long Method, God Class, Long Parameter List. Each LLM was run 3 times with the same prompt and input.

> Note: the report draft, matching, calculations and explanation scoring were prepared with help from Claude (an AI assistant). This is disclosed in the report's LLM Usage Declaration.

## Files

| File | What it is |
|---|---|
| `SWE439_HW1_Report.docx` | Full report (16 pages): Tasks 1–5, Tables 1 and 2, declaration, appendices |
| `HW1_detection_matrix.xlsx` | All 45 distinct detections by run, Table 1, Table 2, explanation scores, matching rules |
| `commons-cli-scope.txt` | Comment-stripped code (34 files) uploaded to both LLMs |
| `prompt.txt` | Exact prompt used in all 6 runs |
| `pmd_baseline.csv` | The 22 PMD detections |
| `RUN_PROTOCOL.md` | How each run was done |
| `runs/ChatGPT/`, `runs/DeepSeek/` | Answers (`.txt`), PDF exports and screenshots for Runs 1–3 |

## Status

### Done
- [x] ChatGPT ×3 and DeepSeek ×3 runs, with answers, PDFs and DeepSeek screenshots saved
- [x] Repo chosen (Apache Commons CLI, commit `bc23215`) and LOC counted
- [x] 3 smells chosen and PMD run (22 detections)
- [x] Code bundle and prompt prepared
- [x] Detections extracted from the 6 runs and matched against PMD
- [x] Table 1 (overlap) and Table 2 (consistency) calculated and double-checked against the matrix
- [x] 3 disagreement cases analysed
- [x] 11 explanations scored
- [x] Report and workbook written
- [x] Names, IDs, Section 01 and date (21 October 2026) filled in
- [x] DeepSeek settings filled in: Deep thinking off, Smart Search off, no version shown in the web UI (checked from the screenshots of all 3 runs)
- [x] Report rewritten as a team ("we"); review notes removed
- [x] LLM Usage Declaration checked
- [x] Agreed on PMD thresholds (30 statements, 5 parameters) and overloads as separate units
- [x] Deadline confirmed with the instructor
- [x] Formatting fixed: 11pt body text, 9pt tables (nothing smaller), consistent line spacing, no blank pages
- [x] Workbook notes cleaned up and RUN_PROTOCOL.md updated with the settings used

### Left to do (still highlighted in yellow in the report)
- [ ] **ChatGPT model name:** Section 1.1 table. Open each saved chat and hover over the retry/regenerate icon under the answer to see the model.
- [ ] **ChatGPT settings:** confirm web search and memory were really off in all 3 runs (Section 1.1 table; also fix `RUN_PROTOCOL.md` if not)
- [ ] **Figure 3:** screenshot of PMD running on our machine (the `pmd check` command and its output, Appendix C) and paste it into Section 3.6
- [ ] **Figures 4–6:** one screenshot per ChatGPT run showing the model name, pasted into Section 3.6; also save them in `runs/ChatGPT/RunN/screenshot/`
- [ ] Remove the yellow highlighting once each item is filled
- [ ] Quick final review of the report after the screenshots are in
- [ ] Export to PDF if required and submit

Owner for each open item: _write names here_