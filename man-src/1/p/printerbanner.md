---
title: "printerbanner(1)"
name: "printerbanner"
section: "1"
letter: "p"
url: "/docs/linux/man/1-printerbanner/"
description: "printerbanner – print large banner on printer"
---

<h2 class="name">NAME</h2>
<p> <code>printerbanner</code> &#8211; print large banner on printer </p>
<h2>SYNOPSIS</h2>
<p> [-<code>d</code> ] [-<code>t</code> ] [-<code>w </code><i>width</i> ] <i>message &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Banner</code> prints a large, high quality banner on the standard output. If the message is omitted, it prompts for and reads one line of its standard input. </p>
<p> The output should be printed on paper of the appropriate width, with no breaks between the pages. </p>
<p> The following options are available:</p>
<dl>
<dt><code>-d</code></p>
<dd> Enable debug.</p>
<dt><code>-t</code></p>
<dd> Enable trace.</p>
<dt><code>-w </code><i>width</i></p>
<dd> Change the output from a width of 132 to <i>width</i> suitable for a narrow terminal.</dl>
<h2>AUTHORS</h2>
<p> An Mark Horton</p>
<h2>BUGS</h2>
<p> Several <code>ASCII</code> characters are not defined, notably &lt;, &gt;, [, ], \, ^, _, {, }, |, and ~. The same holds for all non <code>ASCII</code> characters. Also, the characters &quot;, &#8216;, and &amp; are funny looking (but in a useful way.) </p>
<p> The &#8211;<code>w</code> option is implemented by skipping some rows and columns. The smaller it gets, the grainier the output. Sometimes it runs letters together. </p>
<p> Messages are limited to 1024 characters in length. </p>
<p> This program is called just banner on FreeBSD. </p>
<h2>Index</h2>
