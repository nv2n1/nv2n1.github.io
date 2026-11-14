---
title: "apport-unpack(1)"
name: "apport-unpack"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apport-unpack/"
description: "apport-unpack – extract the fields of a problem report to separate files"
---

<h2 class="name">NAME</h2>
<p> apport-unpack &#8211; extract the fields of a problem report to separate files</p>
<h2>SYNOPSIS</h2>
<p> <code>apport-unpack</code> <i>report target-directory</i> </p>
<h2>DESCRIPTION</h2>
<p> A problem report, as produced by <code>apport</code> is a single file with a set of key/value pairs in the RFC822 syntax. This tool disassembles a report such that the value of each entry is written into a separate file, with the key as file name. This is particularly useful for large binary data like the core dump. </p>
<p> <i>report </i> is either a path to an existing apport crash report, or &#8216;-&#8216; to read from stdin. </p>
<p> The <i>target-directory</i> must either be nonexisting or empty. </p>
<h2>AUTHOR</h2>
<p> <code>apport</code> and the accompanying tools are developed by Martin Pitt &lt;martin.pitt [at] ubuntu.com&gt;. </p>
<h2>Index</h2>
