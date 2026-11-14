---
title: "h5diff(1)"
name: "h5diff"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5diff/"
description: "h5diff – Compares two HDF5 files and reports the differences."
---

<h2>NAME</h2>
<p> h5diff &#8211; Compares two HDF5 files and reports the differences.</p>
<h2>SYNOPSIS</h2>
<p> h5diff file1 file2 [OPTIONS] [object1 [object2 ] ]</p>
<h2>DESCRIPTION</h2>
<p> h5diff is a command line tool that compares two HDF5 files, file1 and file2, and reports the differences between them. </p>
<p> Optionally, h5diff will compare two objects within these files. If only one object, object1, is specified, h5diff will compare object1 in file1 with object1 in file2. In two objects, object1 and object2, are specified, h5diff will compare object1 in file1 with object2 in file2. These objects must be HDF5 datasets. </p>
<p> object1 and object2 must be expressed as absolute paths from the respective file&#8217;s root group. </p>
<p> Additional information, with several sample cases, can be found in the document H5diff Examples.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>file1 file2</code></p>
<dd> The HDF5 files to be compared.</p>
<dt><code>-h</code></p>
<dd> Print all differences.</p>
<dt><code>-r</code></p>
<dd> Print only the names of objects that differ; do not print the differences. These objects may be HDF5 datasets, groups, or named datatypes.</p>
<dt><code>-n count</code></p>
<dd> Print difference up to count differences, then stop. count must be a positive integer.</p>
<dt><code>-d delta</code></p>
<dd> Print only differences that are greater than the limit delta. delta must be a positive number. The comparison criterion is whether the absolute value of the difference of two corresponding values is greater than delta (e.g., |a-b| &gt; delta, where a is a value in file1 and b is a value in file2).</p>
<dt><code>-p relative</code></p>
<dd> Print only differences that are greater than a relative error. relative must be a positive number. The comparison criterion is whether the absolute value of the difference 1 and the ratio of two corresponding values is greater than relative (e.g., |1-(b/a)| &gt; relative where a is a value in file1 and b is a value in file2).</p>
<dt><code>object1 object2</code></p>
<dd> Specific object(s) within the files to be compared.</dl>
<h2>EXAMPLES</h2>
<p> The following h5diff call compares the object /a/b in file1 with the object /a/c in file2:<br />
&nbsp;<wbr>h5diff file1 file2&nbsp;<wbr>/a/b&nbsp;<wbr>/a/c&nbsp;<wbr> </p>
<p> This h5diff call compares the object /a/b in file1 with the same object in file2:<br />
&nbsp;<wbr>h5diff file1 file2&nbsp;<wbr>/a/b&nbsp;<wbr> </p>
<p> And this h5diff call compares all objects in both files:<br />
&nbsp;<wbr>h5diff file1 file2</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-h5dump/">h5dump</a></i>(1), <i><a href="/docs/linux/man/1-h5ls/">h5ls</a></i>(1), <i><a href="/docs/linux/man/1-h5repart/">h5repart</a></i>(1), <i><a href="/docs/linux/man/1-h5import/">h5import</a></i>(1), <i><a href="/docs/linux/man/1-gif2h5/">gif2h5</a></i>(1), <i><a href="/docs/linux/man/1-h52gif/">h52gif</a></i>(1), <i><a href="/docs/linux/man/1-h5perf/">h5perf</a></i>(1) </p>
<h2>Index</h2>
