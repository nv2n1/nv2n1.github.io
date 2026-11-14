---
title: "pfbtops(1)"
name: "pfbtops"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pfbtops/"
description: "pfbtops – translate Printer Font Binary files to PostScript ASCII"
---

<h2 class="name">NAME</h2>
<p> pfbtops &#8211; translate Printer Font Binary files to PostScript ASCII </p>
<h2>SYNOPSIS</h2>
<p> [<i>pfb-file</i>] <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <i>pfbtops</i> translates a PostScript font in Printer Font Binary (PFB) format to ASCII, splitting overlong lines in text packets into smaller chunks. If <i>pfb-file</i> is omitted, the PFB file will be read from the standard input. The ASCII format PostScript font will be written on the standard output. PostScript fonts for MS-DOS are normally supplied in PFB format. </p>
<p> The resulting ASCII format PostScript font can be used with groff, if it is first listed in <i>/usr/:share/:groff/:1.22.4/:font/:devps/:download</i> and <i>/usr/:share/:groff/:1.22.4/:font/:devpdf/:download</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display a usage message and exit.</p>
<dt><code>-v</code></p>
<dd> <code>&#8211;version</code> Display version information and exit.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-grops/">grops</a></i>(1), <i><a href="/docs/linux/man/1-gropdf/">gropdf</a></i>(1) </p>
<h2>Index</h2>
