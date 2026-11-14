---
title: "sponge(1)"
name: "sponge"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sponge/"
description: "sponge – soak up standard input and write to a file"
---

<h2 class="name">NAME</h2>
<p> sponge &#8211; soak up standard input and write to a file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>sed &#8216;&#8230;&#8217; file | grep &#8216;&#8230;&#8217; | sponge [-a] file</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>sponge</code></p>
<dd>reads standard input and writes it out to the specified file. Unlike a shell redirect, <code>sponge</code> soaks up all its input before writing the output file. This allows constructing pipelines that read from and write to the same file. </p>
<p> <code>sponge</code> preserves the permissions of the output file if it already exists. </p>
<p> When possible, <code>sponge</code> creates or updates the output file atomically by renaming a temp file into place. (This cannot be done if TMPDIR is not in the same filesystem.) </p>
<p> If the output file is a special file or symlink, the data will be written to it, non-atomically. </p>
<p> If no file is specified, <code>sponge</code> outputs to stdout.</p>
<h2>OPTIONS</h2>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> Replace the file with a new file that contains the file&#8217;s original content, with the standard input appended to it. This is done atomically when possible.</dl>
<h2>AUTHOR</h2>
<p> Colin Watson and Tollef Fog Heen </p>
<h2>Index</h2>
