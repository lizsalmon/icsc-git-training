# Git In Practice – Level 3 Exercise

## Getting Started

1. I would recommend that you turn off your email notifications for failed workflows before starting this!
    - Go to your icon, Settings, Notifications, scroll down to actions and deselect email from the "Notify me" drop down.
    - You'll thank me later :) 

1. **Clone this repository** to your local machine.

2. Create a new branch using your name:

```bash
git switch -c <your-name>
```

> ⚠️ Please **do create your own branch**. Accidentally pushing to `main` is fixable, but it’s still annoying to clean up.

---

## The Challenge

Your task is to **find a specific commit from another branch and cherry-pick it into your branch** so that the workflow verification checks pass.

Below is an example of what a failing workflow might look like:

<img width="1212" height="124" alt="image" src="https://github.com/user-attachments/assets/767fb04f-4e83-43a6-9abc-91bc8156be99" />

> The red cross shown above.

To complete the challenge you need to:

1. **Locate the required commit** on the branch that is passing.
2. **Cherry-pick that commit** into your branch.
3. **Push your branch to the remote repository**.

```bash
git push origin <your-name>
```

> Please **do not push to `main`**.

---

## Important Note

The `main` branch **changes every 5 minutes**… 👀
(The workflow validation checks that you have the most up to date version of main.)
