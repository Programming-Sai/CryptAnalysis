# CryptAnalysis

## Project Overview

An exploration of cryptographic concepts, including modular exponentiation, RSA algorithm analysis, and brute-force password cracking techniques. This repository contains Python implementations, performance evaluations, and visualizations as part of the **MATH 359 project for the 2024/25 academic year.**

- Modular exponentiation algorithms.
- Performance evaluation of the RSA algorithm and its complexity.
- Brute-force password cracking techniques for different scenarios.

Our goal is to implement these concepts using Python, analyze their performance, and present the findings in a well-documented and collaborative manner.

[Go here to see the Presentation](https://programming-sai.github.io/CryptAnalysis/)

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Features](#features)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Contributors](#contributors)

---

## Getting Started

### Prerequisites

To run the code in this repository, ensure you have the following installed:

- Python 3.8 or higher
- Jupyter Notebook
- Required libraries (listed in `requirements.txt`)

### Installation

1. **Fork the Repository**

   - Go to the [CryptAnalysis repository](https://github.com/Programming-Sai/CryptAnalysis) on GitHub.
   - In the top-right corner, click the **Fork** button to create your own copy of the repository.
   - After forking, you’ll be directed to your own forked repository.

2. **Clone Your Forked Repository**

   - Clone the repository to your local machine by using your forked version’s URL:

   ```bash
   git clone https://github.com/<your-username>/CryptAnalysis.git
   ```

   Replace `<your-username>` with your GitHub username.

3. **Navigate to the Project Directory**

   ```bash
   cd CryptAnalysis
   ```

4. **Create a Virtual Environment**

   ```bash
   python -m venv .crypt-venv
   ```

5. **Activate the Virtual Environment**

   ```bash
   .\.crypt-venv\Scripts\activate  # Windows

   # OR

   source .crypt-venv/bin/activate  # MacOS/Linux
   ```

6. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

### Working with the Repository

1. **Create a Branch for Your Work**  
   After cloning your forked repository, **create a new branch** to work on your task (e.g., implementing modular exponentiation or brute force password cracking).

   ```bash
   git checkout -b my-feature-branch
   ```

   Example:

   ```bash
   git checkout -b modular-exp-work
   ```

> [!TIP]  
> _For naming your branches, please make sure that the section you chose would be part of them name of your branch. For example, your can name your branch `mod-exp` (if you are doing the Modular exponentiation work) `rsa-prob` (for the RSA one) or `pswd-cracking` (for the password and bruteforcing.)._

2. **Make Changes**  
   Modify the appropriate files as per the assigned task. For example, you’ll be working inside `notebooks/Modular_Exponentiation_Problems/` if working on modular exponentiation.

3. **Stage and Commit Your Changes**  
   After making changes, **stage** and **commit** them to your branch:

   ```bash
   git add .
   git commit -m "Implemented modular exponentiation function"
   ```

4. **Push Your Branch to Your Fork**  
   Push your branch to your **forked repository** on GitHub:

   ```bash
   git push origin my-feature-branch
   ```

5. **Create a Pull Request (PR)**
   - Go to your forked repository on GitHub.
   - You should see a banner asking if you want to **Create a Pull Request** for the branch you just pushed.
   - Click on **"Compare & pull request"**.
   - Add a **title** and **description** for your PR (e.g., "Implemented modular exponentiation function").
   - Make sure the **base repository** is `Programming-Sai/CryptAnalysis` and the **base branch** is `main`.
   - Click **"Create Pull Request"** to submit your PR for review.

---

### Reviewing and Making Changes

- If changes are requested after the pull request review, make the necessary edits locally.
- **Commit** and **push** the changes to your branch. Your pull request will automatically update.

```bash
git add .
git commit -m "Updated implementation as per review"
git push origin my-feature-branch
```

---

### Summary Workflow:

1. **Fork** the repository.
2. **Clone** your forked repo.
3. **Create a branch** for your work.
4. **Make changes**, **stage**, and **commit**.
5. **Push** the branch to your fork.
6. **Submit a pull request** to the main repository.

> [!IMPORTANT]  
> _At the bottom of the page, update this readme with your name and ID (Please for this README, make changes to only your details. leave everything else as is!!)._

---

## Features

- **Modular Exponentiation Algorithm**: Python function implementation with performance comparison.
- **RSA Decryption Complexity**: Analyzing brute-force decryption time for varying key sizes.
- **Password Cracking**: Brute-force attack simulations for numeric and alphanumeric PINs.
- **Visualization**: Graphs for performance comparisons and password cracking times.

---

## Usage

1. Open the Jupyter Notebook in the project folder:
   ```bash
   jupyter notebook CryptAnalysis.ipynb
   ```
2. Run the cells to view the implementation, results, and visualizations.
3. Edit or contribute by creating new branches for your work.

---

## Project Structure

```
CryptAnalysis/
│── data/                                # Store input/output files if needed
│── result/                              # Store final results
│── logs/                                # Store timing and performance logs
│── figures/                             # Store generated graphs and plots
│── scripts/                             # Reusable Python scripts for calculations
│── presentation/                        # Final slides and summary notebook
│── notebooks/                           # Jupyter Notebooks for team members
│   ├── Modular_Exponentiation_Problems/ # Modular exponentiation work
│   ├── Password_And_BruteForcing/       # Brute-force password attack work
│   └── RSA_Problems/                    # RSA decryption work
│── .gitignore                           # Ignore unnecessary files in version control
│── README.md                            # Overview and instructions
└── requirements.txt                     # Dependencies (if any)

```

---

## Contributors

This project is a group effort by the following team members:

_Add your name, ID and selected selection here_

- **[Menah Lartey Isaiah Nii Lartey] - [11222100]**: Modular Exponentiation Algorithm

- **[⁠Tattah Abel Mawunyo] - [11335775]**: RSA Algorithm Analysis

- **[Anti Bright Gyeadu] - [11340436]**: Brute-Force Password Cracking

- **[Ebenezer Ofori Acquah] - [11154989]**: RSA Algorithm Analysis

- **[Addo Reuben Nii Addotey] - [11019527]**: Modular Exponentiation Algorithm

- **[Angela Acquah] - [11033579]**: Modular Exponentiation Algorithm

- **[Abormegah Elisah Yaw] - [10823700]**:

    <br>
    <br>

> [!NOTE]  
> _If you're a team member, ensure you’ve been added as a collaborator. Reach out if you need access._

---
