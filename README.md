# Git In Practice – Level 3 Exercise

## Getting Started

1. I recommend turning off email notifications for failed workflows before starting.

   - Click your **GitHub avatar → Settings → Notifications**
   - Scroll down to **Actions**
   - Change **Notify me** to remove email notifications.

   You’ll thank me later :)

---

## Fork and Clone the Repository

1. **Fork this repository** to your own GitHub account.

   Click **Fork** in the top-right corner of the repository page.

2. **Clone your fork** to your local machine.

```
git clone <your-fork-url>
cd icsc-git-training
```

3. Add the original repository as an **upstream remote** so you can keep up with updates.

```
git remote add upstream https://github.com/lizsalmon/icsc-git-training.git
```
---

## Create Your Branch

Create a new branch using your name:

```
git switch -c <your-name>
```

Example:

```
git switch -c alice
```

You will work on this branch throughout the exercise.

---

## The Challenge

Your task is to **find a specific commit from another branch and cherry-pick it into your branch so that the workflow verification checks pass.**

Below is an example of what a failing workflow looks like:

<img width="1219" height="124" alt="image" src="https://github.com/user-attachments/assets/52717da3-f94f-4e84-bf8a-4e83430be077" />

To complete the challenge you need to:

1. **Locate the required commit** on the branch that is passing.
2. **Cherry-pick that commit** into your branch.
3. **Push your branch to your fork**.
4. **Create a pull request** from your fork into the original repository.

Push your branch:

```
git push origin <your-name>
```

---

## Creating the Pull Request

After pushing:

1. Go to your **fork on GitHub**.
2. Click **Compare & Pull Request**.
3. Ensure the PR targets the **original repository's `main` branch**.

Example:

```
your-username:your-name → upstream-repo:main
```

---

## Keeping Your Branch Up to Date

The `main` branch **changes every 5 minutes**.

Before your PR can pass the workflow checks, your branch must be **up to date with `main`**.

Fetch the latest changes from the upstream repository:

```
git fetch upstream
```

Update your branch:

```
git rebase upstream/main
```

Then push the updated branch to your fork:

```
git push --force-with-lease
```

---

## Important Notes

- **Do not work directly on `main`.**
- **Always work in your own branch.**
- Your branch must be **up to date with `main` and pass the workflow checks** before it can be merged.
