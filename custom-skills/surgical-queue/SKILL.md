---
name: surgical-queue
description: Query and analyze hospital surgical queue data from the database. Use when users ask about patients waiting for surgery, surgical schedules, operating room queues, or pending procedures.
---

# Surgical Queue Skill

This skill retrieves surgical queue data from the hospital database.

## Workflow

1. Identify what the user wants to know about the surgical queue.
2. Determine filters such as:
   - patient name
   - surgery date
   - specialty
   - priority
3. Query the surgical scheduling database.
4. Return results in a structured format.

## Example queries

User:
"Show surgical queue"

User:
"Which patients are scheduled for surgery tomorrow?"

User:
"Is patient Maria Silva waiting for surgery?"

## Output format

Patient: Maria Silva  
Procedure: Hip replacement  
Priority: High  
Scheduled date: 2026-03-20  
Status: Waiting
