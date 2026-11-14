---
title: "mkhtmlindex(1)"
name: "mkhtmlindex"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkhtmlindex/"
description: "mkhtmlindex – generate index files for HTML man pages"
---

<h2>NAME</h2>
<p> mkhtmlindex &#8211; generate index files for HTML man pages</p>
<h2>SYNOPSIS</h2>
<p> <code>mkhtmlindex</code> <i>htmlmandir</i></p>
<h2>DESCRIPTION</h2>
<p> The <i>mkhtmlindex</i> program generates index files for a directory of HTML-formatted manual pages. It searches for files whose names are of the form &#8220;name.1.html&#8221;, and outputs index files &#8220;manindex1.html&#8221;, &#8220;manindex.2.html&#8221;, and so on, one for each manual volume. Empty index files will be removed. Names and descriptions are found by scanning the first <i>&lt;H2&gt;</i> section of each page.</p>
<h2>OPTIONS</h2>
<p> <i>mkhtmlindex</i> takes only one argument: the directory to process.</p>
<h2>NOTES</h2>
<p> This utility is currently rather specific to X manual pages. In particular, the format of the index files it outputs is not configurable, nor is the HTML formatting it expects of manual pages.</p>
<h2>AUTHOR</h2>
<p> The version of the <i>mkhtmlindex</i> included in this X.Org Foundation release was originally written by David Dawes wrote as a part of XFree86. </p>
<p> Colin Watson wrote this manual page, originally for the Debian Project. </p>
<h2>Index</h2>
