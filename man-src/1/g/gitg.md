---
title: "gitg(1)"
name: "gitg"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gitg/"
description: "gitg – Git repository viewer"
---

<h2>NAME</h2>
<p> gitg &#8211; Git repository viewer </p>
<h2>SYNOPSIS</h2>
<p> <code>gitg</code> [options]&nbsp;<wbr>[repository]&nbsp;<wbr>[&lt;refspec&gt;]</p>
<h2>DESCRIPTION</h2>
<p> <code>gitg</code> is a graphical user interface for git. It aims at being a small, fast and convenient tool to visualize the history of git repositories. Besides visualization, gitg also provides several utilities to manage your repository and commit your work.</p>
<h2>OPTIONS</h2>
<p> <code>-c,&#8211;commit</code> Open <code>gitg </code> in commit view </p>
<p> <code>-?,&#8211;help</code> Show the help message </p>
<p> <code>[repository]</code> Load the repository at <code>repository</code> in <code>gitg. </code> If unspecified, <code>gitg </code> will try to open the repository at the current working directory </p>
<p> <code>[&lt;refspec&gt;]</code> Populate the history view of <code>gitg</code> using the specified <code>&lt;refspec&gt;</code> which has the same format as used with <code>git log</code> (Example: <code>gitg</code> &#8211;left-right HEAD..FETCH_HEAD) </p>
<h2>AUTHORS</h2>
<p> Jesse van den Kieboom &lt;jesse [at] icecrew.nl&gt; </p>
<h2>Index</h2>
