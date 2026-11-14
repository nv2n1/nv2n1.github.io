---
title: "h5ls(1)"
name: "h5ls"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5ls/"
description: "h5ls – Prints information about a file or dataset."
---

<h2>NAME</h2>
<p> h5ls &#8211; Prints information about a file or dataset.</p>
<h2>SYNOPSIS</h2>
<p> h5ls [OPTIONS] file [OBJECTS&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> h5ls prints selected information about file objects in the specified format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> or <code>-? </code> or <code>&#8211;help</code> Print a usage message and exit.</p>
<dt><code>-a </code></p>
<dd> or <code>&#8211;address</code> Print addresses for raw data.</p>
<dt><code>-d </code></p>
<dd> or <code>&#8211;data</code> Print the values of datasets.</p>
<dt><code>-e </code></p>
<dd> or <code>&#8211;errors</code> Show all HDF5 error reporting.</p>
<dt><code>-f </code></p>
<dd> or <code>&#8211;full</code> Print full path names instead of base names.</p>
<dt><code>-g </code></p>
<dd> or <code>&#8211;group</code> Show information about a group, not its contents.</p>
<dt><code>-l </code></p>
<dd> or <code>&#8211;label</code> Label members of compound datasets.</p>
<dt><code>-r </code></p>
<dd> or <code>&#8211;recursive</code> List all groups recursively, avoiding cycles.</p>
<dt><code>-s </code></p>
<dd> or <code>&#8211;string</code> Print 1-bytes integer datasets as ASCII.</p>
<dt><code>-S </code></p>
<dd> or <code>&#8211;simple</code> Use a machine-readable output format.</p>
<dt><code>-wN </code></p>
<dd> or <code>&#8211;width=N</code> Set the number of columns of output.</p>
<dt><code>-v </code></p>
<dd> or <code>&#8211;verbose</code> Generate more verbose output.</p>
<dt><code>-V </code></p>
<dd> or <code>&#8211;version</code> Print version number and exit.</p>
<dt><code>-x </code></p>
<dd> or <code>&#8211;hexdump</code> Show raw data in hexadecimal format.</p>
<dt><code>file</code></p>
<dd> The file name may include a <a href="//www.systutorials.com/docs/linux/man/3C-printf/">printf</a>(3C) integer format such as %%05d to open a file family.</p>
<dt><code>objects</code></p>
<dd> Each object consists of an HDF5 file name optionally followed by a slash and an object name within the file (if no object is specified within the file then the contents of the root group are displayed). The file name may include a <a href="//www.systutorials.com/docs/linux/man/3C-printf/">printf</a>(3C) integer format such as &quot;%05d&quot; to open a file family.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-h5dump/">h5dump</a></i>(1), <i><a href="/docs/linux/man/1-h5diff/">h5diff</a></i>(1), <i><a href="/docs/linux/man/1-h5repart/">h5repart</a></i>(1), <i><a href="/docs/linux/man/1-h5import/">h5import</a></i>(1), <i><a href="/docs/linux/man/1-gif2h5/">gif2h5</a></i>(1), <i><a href="/docs/linux/man/1-h52gif/">h52gif</a></i>(1), <i><a href="/docs/linux/man/1-h5perf/">h5perf</a></i>(1) </p>
<h2>Index</h2>
