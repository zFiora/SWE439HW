# SWE 439 – Homework 1: Code Smell Detection (PMD vs ChatGPT vs DeepSeek)

KFUPM · SWE 439 Software Quality Engineering (Term 261) · Section 01

| Team member | Student ID |
|---|---|
| Haidar AlDahan | 202256620 |
| Muhannad AlMelaifi | 202253960 |
| Amjad AlSadiq | 202269000 |
| Mahdi Al Hassan | 202271080 |

This project compares code-smell detections from a static analysis tool (**PMD 7.28.0**) and two LLMs (**ChatGPT, GPT-6.1 Sol**, proprietary, and **DeepSeek-V3**, open-weight) on **Apache Commons CLI** (Java, 34 files, 2,840 LOC). The smells are Long Method, God Class and Long Parameter List. Each LLM was run three times with the same prompt and input.

AI assistance used in preparing the analysis and the report is disclosed in the report's LLM Usage Declaration.

## Files

| File | What it is |
|---|---|
| `SWE439_HW1_Report.docx` | Final report: Tasks 1–5, Tables 1 and 2, LLM Usage Declaration, appendices |
| `HW1_detection_matrix.xlsx` | All 45 distinct detections by run, Table 1, Table 2, explanation scores and matching rules |
| `commons-cli-scope.txt` | Comment-stripped source code (34 files) given to PMD and uploaded to both LLMs |
| `prompt.txt` | Exact prompt used in all six LLM runs |
| `pmd_baseline.csv` | The 22 PMD detections with PMD's messages |
| `RUN_PROTOCOL.md` | How each LLM run was carried out |
| `runs/ChatGPT/`, `runs/DeepSeek/` | Answers (`.txt`), PDF exports and screenshots for Runs 1–3 |

## Key results

| | Overlap with PMD (Run 1) | Three-run consistency |
|---|---|---|
| ChatGPT | 20.0% – 55.6% | 12.5% – 100% |
| DeepSeek | 33.3% – 66.7% | 21.4% – 62.5% |

Full results, by smell, are in Tables 1 and 2 of the report.

## Reproducing the PMD baseline

The ruleset, commands and expected output are in Appendix C of the report. The run reports 22 violations, listed in `pmd_baseline.csv` and Appendix A.