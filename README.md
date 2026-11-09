# Exploring Empathy and Informal Language in AI Customer Service Chatbots

This repository contains study materials, chatbot prompts, de-identified results data, and illustrative chat screenshots for the project **“Exploring Empathy and Informal Language in AI Customer Service Chatbots.”**

The study examines how two communication features—**brief, situation-specific empathy** and **informal language**—affect user experience in AI customer service interactions.

## Study Overview

The study used a within-subjects design with four chatbot conditions:

| Condition | Description |
|---|---|
| **Baseline** | Neutral, concise, professional customer service language. |
| **Empathy** | Professional language with one brief, situation-specific acknowledgment of a relevant customer concern. |
| **Informal Language** | Casual, conversational text-chat language without deliberate emotional validation. |
| **Empathy + Informal Language** | Casual language paired with one brief, informal acknowledgment of a relevant customer concern. |

Participants completed four customer service roleplay trials involving delayed delivery, billing discrepancies, defective products, and account-access problems. After each interaction, participants completed a user-experience survey.

## Repository Structure

```text
.
├── chatExamples/
│   ├── baseline.png
│   ├── empathy.png
│   ├── empathyInformalLanguage.png
│   └── informalLanguage.png
├── procedure/
│   ├── procedure.pdf
│   ├── randomize.py
│   ├── scenarios.txt
│   └── survey.pdf
├── prompts/
│   ├── baseline.txt
│   ├── empathy.txt
│   ├── empathyInformalLanguage.txt
│   └── informalLanguage.txt
├── README.md
└── results.xlsx
```

## Materials

### Chatbot Prompts

The `prompts/` directory contains the full system-prompt instructions for each condition:

- `baseline.txt` — neutral professional customer service chatbot
- `empathy.txt` — chatbot using brief, situation-specific empathy
- `informalLanguage.txt` — chatbot using casual, conversational language
- `empathyInformalLanguage.txt` — chatbot combining empathy and informal language

These prompts were created for a **simulated customer service roleplay study**. They instruct chatbots to generate fictional but plausible account details, policies, and resolutions when necessary to continue a scenario.

> **Important:** The prompts should not be deployed unchanged in a real customer service system. A production chatbot should use verified organizational policies and authorized customer data, avoid fabricating information or outcomes, communicate uncertainty clearly, and escalate cases to human support when it cannot provide a verified answer.

### Study Procedure

The `procedure/` directory contains the study protocol and participant-facing materials:

- `procedure.pdf` — study procedure, including consent, instructions, trial flow, and debriefing
- `scenarios.txt` — the four customer service roleplay scenarios
- `survey.pdf` — questionnaire containing demographic questions, user-experience survey after each chatbot interaction, and final open-ended feedback
- `randomize.py` — script used to randomize chatbot and scenario presentation order

### Example Conversations

The `chatExamples/` directory contains illustrative screenshots of interactions with each chatbot condition from the user study:

- `baseline.png`
- `empathy.png`
- `informalLanguage.png`
- `empathyInformalLanguage.png`

These screenshots are examples intended to demonstrate the communication style of each condition. They are not intended to represent average chatbot performance or the complete set of study interactions.

### Results Data

`results.xlsx` contains the de-identified study results used to calculate the reported user-experience scores.

The study evaluated four dimensions:

1. **Intent Fulfillment**
2. **Emotional Appropriateness**
3. **Coherence and Context Retention**
4. **User Satisfaction and Engagement**

Overall user-experience scores were calculated by averaging the four dimension scores for each chatbot condition.

## Study Design

The study used a within-subjects $2 \times 2$ design:

| | Professional / Neutral Language | Informal Language |
|---|---|---|
| **No brief empathy** | Baseline | Informal Language |
| **Brief empathy** | Empathy | Empathy + Informal Language |

Each participant interacted with all four chatbot conditions and completed each customer service scenario once. Chatbot--scenario pairings and trial order were randomized.

## Implementation Context

The chatbot agents were implemented in **PromptLab**, a University of North Carolina at Chapel Hill web-based platform for creating and interacting with AI agents, using the **ChatGPT-5.6 Luna** model. All agents shared the same core customer service, problem-solving, roleplay, escalation, and role-boundary instructions. The experimental conditions differed in instructions governing empathy and informal language.

## Privacy and Ethical Considerations

This repository does not include participant names, contact information, consent forms, raw identifiable chat logs, or other direct identifiers.

The study used simulated roleplay scenarios rather than real customer accounts or company systems. Any public use of the included materials should preserve participant privacy and should not treat the fictional roleplay details as real customer service policies or records.

## Citation

If you use or adapt these materials, please cite:

```text
Jean Cheng. 2026. Exploring Empathy and Informal Language in AI customer Service Chatbots.
```