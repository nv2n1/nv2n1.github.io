---
title: "Reducing Whitespace in LaTeX Documents"
date: 2018-03-24 08:13:54 +0000
layout: post
canonical: https://www.systutorials.com/squeezing-space-in-latex-systutorials-qa/
---

When you’re fighting page limits — conference submissions, journal requirements, or just fitting content on a poster — reducing LaTeX’s default spacing is essential. Here are the practical approaches, from gentle to aggressive.

## Basic Spacing Adjustments

Start with the most impactful changes. These target the whitespace around floats (figures, tables) and captions:

``` latex
\setlength{\textfloatsep}{1pt}      % Space between text and floats
\setlength{\abovecaptionskip}{1pt}  % Space above captions
\setlength{\belowcaptionskip}{1pt}  % Space below captions
```

These alone can recover significant space without making the document look cramped.

## Comprehensive Space-Saving Configuration

For more aggressive reduction, use this preamble setup. It targets lists, bibliography spacing, section headings, and margins:

``` latex
% Reduce list spacing
\usepackage{enumitem}
\setlist{nosep}  % Removes all vertical spacing in lists

% Tighter section headings
\usepackage[compact]{titlesec}
\titlespacing*{\section}{0pt}{1ex}{0.5ex}
\titlespacing*{\subsection}{0pt}{0.75ex}{0.25ex}

% Float and caption spacing
\setlength{\textfloatsep}{2pt}
\setlength{\abovecaptionskip}{2pt}
\setlength{\belowcaptionskip}{2pt}
\setlength{\floatsep}{2pt}
\setlength{\dblfloatsep}{2pt}
\setlength{\dbltextfloatsep}{2pt}

% List margins
\setlength{\leftmargini}{8pt}
\setlength{\leftmarginii}{8pt}
\setlength{\itemsep}{0pt}
\setlength{\parsep}{0pt}

% Column separation
\setlength{\columnsep}{9pt}

% Paragraph spacing
\setlength{\parskip}{0pt}
\setlength{\parindent}{12pt}

% Smaller bibliography
\usepackage{natbib}
\renewcommand{\bibfont}{\small}
\setlength{\bibsep}{0pt}
```

## Font and Line Spacing Techniques

Switching fonts can reduce overall document size. `times` or `newtxtext` are denser than Computer Modern:

``` latex
\usepackage{newtxtext}  % More compact than CM
\usepackage[nodisplayskip]{setspace}
\setstretch{0.95}  % Slightly reduced line spacing
```

Avoid setting line spacing below 0.9 unless your reviewers won’t notice — it damages readability.

## Additional Space Savers

**Reduce figure/table sizes carefully:**

``` latex
\includegraphics[width=0.95\columnwidth]{figure.pdf}
```

**Tighten equation spacing:**

``` latex
\setlength{\abovedisplayskip}{2pt}
\setlength{\belowdisplayskip}{2pt}
```

\**Use \`\vspace*{-2mm}\` selectively\*\* before section headings or floats where vertical gaps feel excessive, but don’t overuse it.

**Bibliography optimization:**

- Use `\bibpunct{[}{]}{,}{n}{}{;}` to compress citation formatting
- Set `\bibsep=0pt` to remove space between bibliography entries
- Consider splitting long author lists with `et al.`

## Reality Check

Most journals and conferences have explicit formatting guidelines. Check before aggressively squeezing space — some enforce minimum margins or line spacing that will override your settings. If you’re 1–2 pages over, targeted spacing reduction works. If you’re 5+ pages over, you likely need to cut content instead.

The Cambridge University guide linked in older versions of this article is no longer maintained, but the principles remain: every \setlength change compounds. Test incrementally and preserve document readability.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
