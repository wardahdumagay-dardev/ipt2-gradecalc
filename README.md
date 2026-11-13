# ipt2-gradecalc

A small grade calculator for IT 316 – Integrative Programming and Technologies 2.
It computes a final grade (30% prelim, 30% midterm, 40% finals) and a PASSED/FAILED remark.

<!-- Activity 3: paste your CI status badge on the next line -->


## Team

<<<<<<< HEAD
Team description: We are the student developers to build a fast, accurate and accessible grade calculation tool.
=======
Team description: A collaborative development team building a user-friendly grade calculator application for our Integrative Programming and Technologies 2 (IPT2) course.
>>>>>>> 5ecc289436ba48b5ac5d13c284b36bc467e4569e

| Role      | Name | GitHub username |
|-----------|------|-----------------|
| Partner A |      |                 |
| Partner B |      |                 |

## How to run the tests

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate      macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -v --cov=grades --cov-report=term-missing
```
