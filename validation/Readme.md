# Vireo Support Tool - Validation Framework

This folder houses the automated validation and data integrity framework designed for the Vireo Audio support analytics project. It ensures that all operational metrics, financial calculations, and data schemas maintain 100% mathematical accuracy with zero hallucination risk.

## Directory Structure & Data Source
Rather than duplicating datasets, this validation module references the master data source directly from the centralized repository:
- `validate.py`: The automated test script.
- **Data Source:** Pulls pristine records directly from `../Resources/tickets.csv`.

## How to Run Validation on a Clean Machine
1. Open your terminal and navigate into the `validation` folder.
2. Ensure you have the `pandas` library installed:
   ```bash
   pip install pandas
Execute the validation script:

Bash
python validate.py
Core Validation Pillars
Zero Hallucination / Deterministic Math:

Mechanism: Financial waste metrics (such as inter-team transfer costs) are calculated using exact programmatic multiplication (total_transfers * ₹305 based on Support Policy §4).

Benefit: Eliminates LLM estimation drift and rounding errors, ensuring complete mathematical reproducibility.

Defensive Error Handling & Schema Integrity:

Mechanism: Numeric fields such as transfers pass through defensive data coercion (pd.to_numeric(..., errors='coerce').fillna(0)).

Benefit: Prevents runtime crashes and handles missing strings or corrupted log cells gracefully by defaulting them safely to zero.

Status State Validation:

Mechanism: Validates that all ticket status categories map strictly within expected operational boundaries (resolved, closed, open, pending).

Benefit: Guarantees that downstream reporting and leaderboards are not distorted by legacy or malformed state classifications.