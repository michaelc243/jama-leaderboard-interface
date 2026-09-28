# NOTE: This project is not complete nor fully functional.

# Jama Zonies PR Leaderboard Manager

A desktop application designed to manage and update a local Power Ranking (PR) leaderboard and sync the standings directly to a Discord channel message via webhooks.

---

## Features

### **PyQt5 Graphical Interface (`main.py`)**:
* Displays up to 20 player positions with point totals.


* Quick **Add** and **Remove** buttons to adjust player point scores dynamically.


* Live status tracking to indicate unsaved changes or file sync states.


* Local JSON storage (`leaderboard_data.json`) to persist player scores.




### **Discord Webhook Synchronization (`main.py`)**:
* Automatically sorts players by point values in descending order.


* Generates a styled Discord embed containing top player standings and rank badges (🥇, 🥈, 🥉).


* Edits an existing Discord webhook message asynchronously using `discord.py` and `aiohttp`.




### **Setup & Configuration (`setup.py`)**:
* Graphical setup dialog for configuring the Discord Webhook URL and target Message ID.


* Input validation to ensure valid Discord webhook URLs and numeric message IDs.


* Saves credentials to `config.json` for seamless integration with the main app.





---

## Prerequisites

* **Python**: Version 3.8 or higher.


* **OS**: Windows (the scripts use `ctypes` for native error message popups).



---

## Installation & Setup

### 1. Install Dependencies

Install the required Python packages:

```bash
pip install PyQt5 discord.py aiohttp

```

### 2. Configure Webhook Settings

Run `setup.py` to enter your Discord webhook details:

```bash
python setup.py

```

1. Enter your **Webhook URL** (must start with `[https://discord.com/api/webhooks/](https://discord.com/api/webhooks/)`).


2. Enter the **Message ID** of the existing Discord message you wish to keep updated.


3. Click **OK** to save configuration into `config.json`.



---

## Usage

Start the leaderboard manager application:

```bash
python main.py

```

### Workflow

1. **Manage Standings**: Input player names into positions 1 through 20 and use the **Add** or **Remove** buttons to increment/decrement point counts.


2. **Sync to Discord**: Click **Sync Now** to save current standings locally to `leaderboard_data.json` and immediately update the specified Discord message via webhook.



---

## File Overview

| File | Language | Description |
| --- | --- | --- |
| `main.py` | Python | PyQt5 desktop GUI for modifying player scores and sending webhook updates to Discord.

 |
| `setup.py` | Python | Configuration dialog GUI for setting up the Discord webhook URL and message ID.

 |
| `leaderboard_data.json` | JSON | Local storage file for saved player names and their corresponding points.

 |
| `config.json` | JSON | Automatically created configuration file containing Discord webhook credentials.

 |
