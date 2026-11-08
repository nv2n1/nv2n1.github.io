---
title: "Show Git Blame in Eclipse Editor"
date: 2020-10-31 11:26:09 +0000
layout: post
canonical: https://www.systutorials.com/configure-eclipse-to-show-git-revision-information-in-editor/
---

Eclipse’s EGit plugin includes Git blame functionality built-in, allowing you to view revision details directly in the editor. This feature shows commit information, author, and date for each line without leaving your editor.

First, ensure you have EGit installed. If you’re on a recent Eclipse version (2024 or later), EGit comes bundled. If not, install it from the Eclipse Marketplace by going to **Help** → **Eclipse Marketplace** and searching for “EGit”.

To enable revision information display, right-click the left margin of the editor (the line number gutter) and select **Show Revision Information**. A colored overlay will appear showing commit details for each line.

## Viewing Revision Details

Once enabled, hover your mouse over any line number in the left gutter. A tooltip will display:

- Commit hash
- Author name
- Commit date
- Commit message (first line)

This is equivalent to running `git blame filename.ext` from the command line, but integrated directly into your editor workflow.

## Configuring Display Options

Eclipse provides several customization options for the revision information display. Access these settings via **Window** → **Preferences** → **Team** → **Git** → **Revision Information**.

Key configuration options include:

**Color coding:**

- **By author**: Lines are colored based on who committed them, making it easy to identify code ownership
- **By date**: Lines are colored by age, with newer commits in one color scheme and older ones in another, helping identify recently modified code

**Information display:**

- **Show author**: Displays the committer’s name
- **Show commit ID**: Shows the abbreviated commit hash (useful for referencing in commit messages or tickets)
- **Show date**: Shows the commit date

You can enable any combination of these options. A typical setup includes author and date for quick context about why a line exists.

## Combining with Other Git Features

Eclipse’s revision information pairs well with other Git integration features:

- **Highlight Changed Lines**: Configure Eclipse to highlight lines modified since the last commit (Window → Preferences → Team → Git → Change Set). This shows uncommitted changes at a glance.
- **Git History View**: Right-click a file and select **Team** → **Show in History** to see the full commit log for that file.
- **Blame View**: For deeper analysis, use **Team** → **Show Git Blame** to open a dedicated blame view showing the entire file with revision details in a separate pane.

## Keyboard Shortcuts

Once the revision information is displayed, use these shortcuts for faster navigation:

- **Ctrl+Shift+O** (Windows/Linux) or **Cmd+Shift+O** (macOS): Open Git History for the current file
- Right-click a commit hash in the tooltip and select **Open Commit** to view the full changeset

## Performance Considerations

For large repositories or files with hundreds of commits, revision information display may briefly slow down editor responsiveness. If you experience lag:

- Disable revision information on files you’re not actively investigating
- Ensure your local Git repository is optimized by running `git gc` periodically
- Consider shallow cloning very large repositories to reduce blame lookup time

## When to Use Git Blame Features

Git revision information is most valuable when:

- Investigating bug origins (find when a problematic line was introduced)
- Understanding code context (why was this approach chosen?)
- Code review (verifying changes during peer review)
- Tracking down issues for follow-up commits (using the commit ID from the tooltip)

Combine this with `git log -p <commit>` from the terminal to see the full context of why a change was made, not just who made it.
