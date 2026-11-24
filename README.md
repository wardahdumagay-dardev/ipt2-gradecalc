# ipt2-gradecalc

[![CI](https://github.com/wardahdumagay-dardev/ipt2-gradecalc/actions/workflows/ci.yml/badge.svg)](https://github.com/wardahdumagay-dardev/ipt2-gradecalc/actions/workflows/ci.yml)

A small grade calculator for IT 316 – Integrative Programming and Technologies 2.
It computes a final grade (30% prelim, 30% midterm, 40% finals) and a PASSED/FAILED remark.

<!-- Activity 3: paste your CI status badge on the next line -->


## Team

g
Team description: A collaborative development team building a user-friendly grade calculator application for our Integrative Programming and Technologies 2 (IPT2) course.

| Role      | Name | GitHub username |
|-----------|------|-----------------|
| Partner A |   Wardah Dumagay   |         wardahdumagay-dardev        |
| Partner B |  Lady leyn Ladaga    |     ladyleyn            |

## How to run the tests

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate      macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -v --cov=grades --cov-report=term-missing
```
