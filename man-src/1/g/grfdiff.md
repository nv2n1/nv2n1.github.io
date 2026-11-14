---
title: "grfdiff(1)"
name: "grfdiff"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grfdiff/"
description: "GRFDiff – A tool to create a binary GRF diff from to GRFs."
---

<h2>NAME</h2>
<p> <code>GRFDiff</code> &#8211; A tool to create a binary GRF diff from to GRFs.</p>
<h2>SYNOPSIS</h2>
<p> <code>grfdiff</code> [-<code>hnxyv</code> ] [-<code>l </code><i>numbers</i> ] [-<code>o </code><i>GRF-File</i> ] <i>Original-GRF-file</i> <i>New-GRF-file</i> </p>
<p> Compare the two GRF files and produce a GRD file containing only the sprites from the second file that are different from the first file. </p>
<p> GRFDiff makes a .GRD file with the same basename as the new GRF file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display the help message.</p>
<dt><code>-l </code><i>numbers</i></p>
<dd> Save the sprites with these numbers in the .GRD instead of finding the modified sprites. With this option, the first GRF file can be omitted. </p>
<p> Format of the numbers: &lt;from1&gt;[-&lt;to1&gt;][,&lt;from2&gt;[-&lt;to2&gt;]]&#8230; e.g. 1-5,8,20-31 (must be increasing numbers).</p>
<dt><code>-n</code></p>
<dd> Only show a list of modified sprites, don&#8217;t make a .GRF file.</p>
<dt><code>-x</code></p>
<dd> Make a self-extracting (.EXE) file instead of a .GRD.</p>
<dt><code>-y</code></p>
<dd> Answer &#8216;y&#8217; to all questions.</p>
<dt><code>-v</code></p>
<dd> Display the version.</dl>
<p> You can specify several sets of GRF files along with their &#8211;<code>l</code> options by separating them with a double-dash `&#8211;&#8216;. The result will be written to a single .GRD file. Only &#8211;<code>l</code> is valid after the first set.</p>
<h2>SEE ALSO</h2>
<p> The documentation in /usr/share/doc/grfcodec/</p>
<h2>AUTHOR</h2>
<p> GRFDiff was written by Josef Drexler. </p>
<p> This manual page was written by Remko Bijker.</p>
<h2>COPYRIGHT</h2>
<p> GRFDiff is Copyright (C) 2003 by Josef Drexler &lt;jdrexler [at] uwo.ca&gt; </p>
<h2>Index</h2>
