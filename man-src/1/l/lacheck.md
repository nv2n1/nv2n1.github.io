---
title: "lacheck(1)"
name: "lacheck"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lacheck/"
description: "lacheck – A consistency checker for LaTeX documents."
---

<h2 class="name">NAME</h2>
<p> lacheck &#8211; A consistency checker for LaTeX documents. </p>
<h2>SYNOPSIS</h2>
<p> <code>lacheck </code> <i>filename</i> [ <i>.tex</i> ]</p>
<h2>DESCRIPTION</h2>
<p> LaCheck is a general purpose consistency checker for LaTeX documents. It reads a LaTeX document and displays warning messages, if it finds bad sequences. It should be noted, that the badness is <i>very</i> subjective. LaCheck is designed to help find common mistakes in LaTeX documents, especially those made by beginners. </p>
<p> The things checked are: </p>
<p> Mismatched groups (braces), environments and math mode delimiters. When a mismatch is found, line numbers for <i>both </i> start and end of the mismatch is given. The error messages comes in pairs, one for the end match and one for the beginning, marked with `&lt;-&#8216; and `-&gt;&#8217; respectively. </p>
<p> Bad spacing including missing a `\ &#8216; after an abbreviation, missing an `\@&#8217; before a punctuation mark in a paragraph that is ended by an capital letter, double spaces like ` ~&#8217;, bad usage of ellipsis (like using &#8230; instead of \ldots, or using \ldots where 
