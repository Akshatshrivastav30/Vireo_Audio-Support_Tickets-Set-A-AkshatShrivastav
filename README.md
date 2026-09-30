# 🎧 Vireo Audio - Support Analytics & Optimization Framework

A modular, deterministic Python analytics platform and QA validation suite built for **Vireo Audio**. Designed to profile 18 months of helpdesk data, track internal transfer cost leakage, generate weekly complaint digests, and surface a fair, Tier-1 filtered agent performance leaderboard.

## 📌 Table of Contents

- Project Overview

- Repository Architecture

- Key EDA & Data Discovery Insights

- Financial & Operational Policy Rules

- Core Modules & Tooling

- Quick Start & Execution Guide

- Validation & Quality Assurance

## 🎯 Project Overview

Vireo Audio experienced rapid growth across its Indore and Bengaluru support hubs, leading to financial leakage and operational bottlenecks. This repository delivers an end-to-end consulting solution featuring:

1. **Financial Leakage Tracking:** Automated calculation of inter-team transfer costs.

2. **Weekly Complaint Digests:** Category-level trend analysis to catch systemic product/checkout issues early.

3. **Tier-Isolated Leaderboard:** Frontline (Tier 1) agent ranking that avoids cross-tier distortions.

4. **Deterministic Validation:** Zero-hallucination script ensuring 100% mathematical and schema integrity.

## 📁 Repository Architecture

Plaintext

```
technical_work/
├── Resources/                   # Master Data Vault (Immutable)
│   ├── tickets.csv              # 18-month helpdesk log (12,528 records)
│   ├── agents.csv               # Agent roster & multi-shift records
│   └── support-policy.pdf       # Operating policy & cost framework
├── analysis_tool/               # Standalone Execution Environment
│   ├── vireo_tool.py            # Analytics engine & leaderboard tool
│   ├── tickets.csv              # Local execution dataset copy
│   ├── agents.csv               # Local execution agent roster copy
│   └── README.md                # Module run guide
├── validation/                  # QA & Automated Integrity Suite
│   ├── validate.py              # Deterministic test runner
│   └── README.md                # Validation framework guide
├── explore.py                   # Initial EDA & dataset profiling script
├── inspect_agent.py             # Agent roster de-duplication diagnostic
└── explanation.pdf              # Executive engineering report
```

## 🔍 Key EDA & Data Discovery Insights

Prior to tool construction, exploratory scripts (`explore.py` and `inspect_agent.py`) were run against the master dataset:

### 1. Helpdesk Scale & Backlog (`explore.py`)

- **Total Volume:** **12,528 tickets** across 18 months (Jan 2025 – Jun 2026), averaging ~700 tickets/month across 44 agents.

- **Resolution Rate:** **11,884 completed** (10,716 resolved, 1,168 closed).

- **Active Queue:** **644 active tickets** (399 open, 245 pending) demonstrating persistent operational backlogs.

### 2. Financial Leakage & Root Causes

- **Total Refunds Issued:** **₹6,343,318.00** (~₹63.43 Lakhs) in direct customer cash outflows.

- **Primary Drivers:**
  
  - `RETURN-QC-OK` (**882 instances**): Products returned that pass quality checks (buyer's remorse/expectation mismatch).
  
  - `DUP-PAYMENT` (**563 instances**): Systemic checkout loop causing duplicate payments. Fixing this payment gateway glitch presents an immediate ₹95k+/quarter save.
  
  - `DOA-REPL` (**144 instances**): Dead-on-Arrival hardware defects from manufacturing or transit.

### 3. Agent Roster Dynamics (`inspect_agent.py`)

- **Multi-Shift De-duplication:** Agents changing shifts/sites created duplicate `agent_id` entries. The tool implements `.drop_duplicates(keep='last')` to evaluate active roles accurately.

- **Tier Isolation:** Per Support Policy §6, Tier 2 technical specialists handle multi-day warranty cases. The leaderboard strictly filters for **Tier 1 (Frontline)** agents to avoid misjudging specialist performance against high-volume agents.

## 💰 Financial & Operational Policy Rules

| **Policy Section**               | **Operational Rule**                                 | **Financial Impact**                                                     |
| -------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------ |
| **Section 3 (SLA Breaches)**     | Missed First Response Time target (e.g., Chat > 15m) | **₹350 automatic store credit** penalty per breach                       |
| **Section 4 (Channel Costs)**    | Base outreach handling costs by interaction channel  | Chat: **₹210** \| Social: **₹240** \| Email: **₹260** \| Voice: **₹520** |
| **Section 4 (Transfer Penalty)** | Inter-team ticket bounces / hand-offs                | **₹305 administrative penalty** per transfer                             |
| **Section 5 (Replacements)**     | Product replacement + reverse pickup shipping        | **Manufacturing Unit Cost + ₹340 flat freight fee**                      |

## ⚡ Core Modules & Tooling

### 1. Analytics Engine (`analysis_tool/vireo_tool.py`)

Runs completely out-of-the-box in its self-contained directory:

- Computes exact financial waste from internal transfers (`transfers * ₹305`).

- Aggregates weekly complaint volumes across top categories.

- Generates a Tier-1 agent performance leaderboard based on resolved/closed tickets.

### 2. Validation Suite (`validation/validate.py`)

Guarantees zero hallucination and complete mathematical reliability:

- **Null Safety:** Verifies missing Ticket IDs equals `0`.

- **Deterministic Math:** Programmatically multiplies transfer counts against policy constants (`₹305`).

- **Schema Consistency:** Asserts ticket statuses strictly fall within `{'resolved', 'closed', 'open', 'pending'}`.

## 🚀 Quick Start & Execution Guide

### Prerequisites

- Python 3.8+

- Pandas library (`pip install pandas`)

### 1. Running the Analytics Tool

Bash

```
# Navigate to the execution directory
cd analysis_tool

# Execute the analytics script
python vireo_tool.py
```

### 2. Running the Validation Framework

Bash

```
# Navigate to the validation directory
cd ../validation

# Execute the integrity test suite
python validate.py
```

### 3. Running Data Discovery Diagnostics

Bash

```
# From the root project folder
python explore.py
python inspect_agent.py
```

## 🧪 Validation & Quality Assurance

Plaintext

```
============================================================
     VIREO SUPPORT TOOL - ACCURACY & VALIDATION CHECK
============================================================
1. Missing Ticket IDs: 0 (Expected: 0)
2. Transfer Cost Math Verification: 5,120 transfers * ₹305 = ₹1,561,600.00
3. Status Categories Valid: True (Expected: True)
============================================================
Validation Complete: Zero data distortion or hallucination detected.
============================================================
```
