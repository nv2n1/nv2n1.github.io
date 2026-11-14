---
title: "h5repack(1)"
name: "h5repack"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5repack/"
description: "h5repack – Copy an HDF5 file to a new file with or without compression/chunking"
---

<h2>NAME</h2>
<p> h5repack &#8211; Copy an HDF5 file to a new file with or without compression/chunking</p>
<h2>SYNOPSIS</h2>
<p> <code>h5repack</code> <code>-i</code> <i>file1</i> <code>-o</code> <i>file2 </i> [<code>-h</code>] [<code>-v</code>] [<code>-f</code> <i>&#8216;filter&#8217;</i>] [<code>-l</code> <i>&#8216;layout&#8217;</i>] [<code>-m</code> <i>number</i>] [<code>-e</code> <i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>h5repack</code> is a command line tool that applies HDF5 filters to a input file <i>file1</i>, saving the output in a new file, <i>file2</i>. </p>
<p> <i>&#8216;filter&#8217;</i> is a string with the format <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;list of objects&gt; : &lt;name of filter&gt; = &lt;filter parameters&gt;.</p>
<p> <i>&lt;list of objects&gt;</i> is a comma separated list of object names meaning apply compression only to those objects. If no object names are specified, the filter is applied to all objects. </p>
<p> <i>&lt;name of filter&gt;</i> can be:<br />
&nbsp;<wbr>GZIP, to apply the HDF5 GZIP filter&nbsp;<wbr>(GZIP compression)<br />
&nbsp;<wbr>SZIP, to apply the HDF5 SZIP filter&nbsp;<wbr>(SZIP compression)<br />
&nbsp;<wbr>SHUF, to apply the HDF5 shuffle filter<br />
&nbsp;<wbr>FLET, to apply the HDF5 checksum filter<br />
&nbsp;<wbr>NONE, to remove the filter </p>
<p> <i>&lt;filter parameters&gt;</i> contains the optional compression information:<br />
&nbsp;<wbr>SHUF&nbsp;<wbr>(no parameter)&nbsp;<wbr><br />
&nbsp;<wbr>FLET&nbsp;<wbr>(no parameter)&nbsp;<wbr><br />
&nbsp;<wbr>GZIP=&lt;deflation level&gt;&nbsp;<wbr>from 1-9&nbsp;<wbr><br />
&nbsp;<wbr>SZIP=&lt;pixels per block,coding&gt;&nbsp;<wbr>(pixels per block is a even number in&nbsp;<wbr> 2-32 and coding method is &#8216;EC&#8217; or &#8216;NN&#8217;) </p>
<p> <i>&#8216;layout&#8217; is a string with the format</i><br />
&nbsp;<wbr>&lt;list of objects&gt;&nbsp;<wbr>:&nbsp;<wbr>&lt;layout type&gt;&nbsp;<wbr> </p>
<p> <i>&lt;list of objects&gt;</i> is a comma separated list of object names, meaning that layout information is supplied for those objects. If no object names are specified, the layout is applied to all objects. </p>
<p> <i>&lt;layout type&gt; </i> can be:<br />
&nbsp;<wbr>CHUNK, to apply chunking layout&nbsp;<wbr><br />
&nbsp;<wbr>COMPA, to apply compact layout&nbsp;<wbr><br />
&nbsp;<wbr>CONTI, to apply continuous layout&nbsp;<wbr> </p>
<p> <i>&lt;layout parameters&gt;</i> is present for the chunk case only it is the chunk size of each dimension: <i>&lt;dim_1 x dim_2 x &#8230; dim_n&gt;</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><i>file1</i>,<i>file2</i></p>
<dd> The input and output HDF5 files</p>
<dt><code>-h</code></p>
<dd> Print a help message</p>
<dt><code>-f</code> <i>filter</i></p>
<dd> Filter type</p>
<dt><code>-l</code> <i>layout</i></p>
<dd> Layout type</p>
<dt><code>-v</code></p>
<dd> Verbose mode. Print output (list of objects in the file, filters and layout applied).</p>
<dt><code>-e</code> <i>file</i></p>
<dd> File with the <code>-f</code> and <code>-l </code> options (only filter and layout flags)</p>
<dt><code>-d</code> <i>delta</i></p>
<dd> Print only differences that are greater than the limit <i>delta</i>. <i>delta </i> must be a positive number. The comparison criterion is whether the absolute value of the difference of two corresponding values is greater than <i>delta</i> (e.g., |<i>a</i>&#8211;<i>b</i>| &gt; <i>delta</i>, where <i>a</i> is a value in <i>file1</i> and <i>b</i> is a value in <i>file2</i>).</p>
<dt><code>-m</code> <i>number</i></p>
<dd> Do not apply the filter to objects which size in bytes is smaller than number. If no size is specified a minimum of 1024 bytes is assumed.</dl>
<h2>EXAMPLES</h2>
<p> Apply GZIP compression to all objects in <i>file1</i> and save the output in <i>file2</i>: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>h5repack -i file1 -o file2 -f GZIP=1 -v</p>
<p> Apply SZIP compression only to object <i>&#8216;dset1&#8217;</i>: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>h5repack -i file1 -o file2 -f dset1:SZIP=8,NN -v</p>
<p> Apply a chunked layout to objects <i>&#8216;dset1&#8217;</i> and <i>&#8216;dset2&#8217;</i>: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>h5repack -i file1 -o file2 -l dset1,dset2:CHUNK=20&#215;10 -v</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-h5dump/">h5dump</a></i>(1), <i><a href="/docs/linux/man/1-h5ls/">h5ls</a></i>(1), <i><a href="/docs/linux/man/1-h5diff/">h5diff</a></i>(1), <i><a href="/docs/linux/man/1-h5import/">h5import</a></i>(1), <i><a href="/docs/linux/man/1-gif2h5/">gif2h5</a></i>(1), <i><a href="/docs/linux/man/1-h52gif/">h52gif</a></i>(1), <i><a href="/docs/linux/man/1-h5perf/">h5perf</a></i>(1), <i><a href="/docs/linux/man/1-h5repart/">h5repart</a></i>(1). </p>
<h2>Index</h2>
