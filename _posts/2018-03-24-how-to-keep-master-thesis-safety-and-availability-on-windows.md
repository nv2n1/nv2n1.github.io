---
title: "Backing Up Your Thesis With Git and Remote Storage on Windows"
date: 2018-03-24 11:49:09 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-keep-master-thesis-safety-and-availability-on-windows/
---

Writing a master thesis means protecting years of work. You need to handle three core concerns: preventing data loss from hardware failure or malware, ensuring 24/7 access to your work, and keeping it private until publication.

The solution is version control with remote backup. Git provides local history and recovery, while a private remote repository ensures your thesis survives disk failures. This approach gives you both safety and redundancy without relying on a single storage device.

## What You’ll Need

- **Git for Windows** — the Git version control system with Windows integration
- **A code hosting platform** — GitHub (free private repos), GitLab (free private repos), or Gitea (self-hosted)
- **A text editor** — VS Code, Notepad++, or any editor you prefer
- **The command line** — Git Bash or PowerShell

GitHub and GitLab both offer unlimited free private repositories now, making them practical choices. Bitbucket still works, but these alternatives are more widely used.

## Setting Up Your Thesis Repository

First, install Git for Windows from <a href="https://git-scm.com/" rel="nofollow noopener" target="_blank">https://git-scm.com/</a>. This gives you Git Bash, a Unix-like shell on Windows.

Create a new folder for your thesis work:

``` powershell
mkdir thesis
cd thesis
git init
```

Configure Git with your name and email:

``` bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Working With Your Files

Use any text editor you’re comfortable with. VS Code handles UTF-8 and Chinese text well. If you prefer Notepad++, ensure you set encoding to UTF-8 without BOM in the Encoding menu.

Create or add your thesis files to the repository. After each writing session, stage and commit your changes:

``` bash
git add .
git commit -m "Add introduction section"
```

Git keeps a complete history. You can view past versions or restore deleted sections using `git log` and `git show`.

## Remote Backup for Safety

Set up a private repository on GitHub, GitLab, or another platform. Then connect your local repository to it:

``` bash
git remote add origin https://github.com/your-username/thesis.git
git branch -M main
git push -u origin main
```

Now push your work regularly:

``` bash
git push
```

If your computer fails, clone your thesis from the remote:

``` bash
git clone https://github.com/your-username/thesis.git
```

## Practical Workflows

**Daily routine:** Edit files, commit changes, push to remote.

``` bash
# After editing
git status
git add chapter1.md
git commit -m "Revise methodology section"
git push
```

**Recovering a deleted section:** Use the log to find the commit where it existed.

``` bash
git log --oneline
git show commit-hash:path/to/file.md
```

**Working on multiple machines:** Clone on your second computer and pull updates.

``` bash
git pull
# Work, then commit and push
git push
```

## Additional Safeguards

Create a `.gitignore` file to exclude temporary files:

    .DS_Store
    *.tmp
    ~$*

Consider storing a backup on an external USB drive:

``` bash
git clone --mirror . F:\thesis-backup.git
```

Add a second remote for extra redundancy:

``` bash
git remote add backup https://gitlab.com/your-username/thesis.git
git push backup main
```

## Why This Works

Git provides version control and local recovery from accidental deletions or corruption. A private remote repository protects against hardware failure and gives you access from any device. You maintain full privacy until you’re ready to publish. The entire history of your work stays available, allowing you to audit changes and recover anything.

This setup scales with your thesis — whether you’re writing plain text, Markdown, or LaTeX files, Git handles them all efficiently.
