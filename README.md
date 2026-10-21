# SWE 439 – Homework 1: Code Smell Detection (PMD vs ChatGPT vs DeepSeek)

Compares code-smell detections from a static analysis tool (**PMD 7.28.0**) and two LLMs (**ChatGPT**, proprietary, and **DeepSeek**, open-weight) on **Apache Commons CLI** (Java, 34 files, 2,840 LOC). Smells: Long Method, God Class, Long Parameter List. Each LLM was run 3 times with the same prompt and input.

> Note: the report draft, matching, calculations and explanation scoring were prepared with help from Claude (an AI assistant). This must be disclosed in the report's LLM Usage Declaration.

## Files

| File | What it is |
|---|---|
| `SWE439_HW1_Report.docx` | Full report draft (15 pages): Tasks 1–5, Tables 1 and 2, declaration, appendices |
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
- [x] Table 1 (overlap) and Table 2 (consistency) calculated
- [x] 3 disagreement cases analysed
- [x] 11 explanations scored (draft)
- [x] Report and workbook drafted

### Left to do
- [ ] Fill the yellow placeholders in the report: names, IDs, section, date, ChatGPT model name, DeepSeek version and settings (Deep thinking / Smart Search on or off)
- [ ] Take the missing screenshots: one ChatGPT screenshot per run showing the model name, and a screenshot of PMD running on our machine (commands in Appendix C of the report)
- [ ] Update and check the LLM Usage Declaration so it matches what each of us did
- [ ] Everyone reads the whole report and checks numbers and wording, especially Sections 3.5 and 4
- [ ] Agree on two choices that change the percentages: PMD thresholds (30 statements, 5 parameters) and treating overloaded methods as separate units
- [ ] Confirm the deadline with the instructor (handout says Oct 17, which has passed)
- [ ] Export to PDF if required and submit

Owner for each open item: _write names here_
