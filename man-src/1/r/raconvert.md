---
title: "raconvert(1)"
name: "raconvert"
section: "1"
letter: "r"
url: "/docs/linux/man/1-raconvert/"
description: "raconvert – convert comma-separated ASCII argus(8) data, to binary argus(8) data."
---

<h2>NAME</h2>
<p> <code>raconvert</code> &#8211; convert comma-separated ASCII <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data, to binary <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data.</p>
<h2>SYNOPSIS</h2>
<p> <code>raconvert</code> <code>-r</code> <i>input</i> <code>-w</code> <i>output</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Raconvert</code> reads comman separated ASCII <code>argus</code> data from a file or stdin, and converts the ASCII representation to binary format. In order for <code>raconver</code> to process the delimited data correctly, the file should be created by <code>ra.1</code> like programs, using the &quot;-c &lt;char&gt;&quot; option to specify a field separator. Column delimiters can be any non-ambiguous character, and are automatically discovered from the files title string. </p>
<p> Because <code>raconvert.1</code> expects the first valid string in the file to be a <code>ra.1</code> column title line, the <code>ra.1</code> program must use the equivalent of the &quot;-L 0&quot; option. </p>
<p> The file can present its column oriented data in any order, and <code>raconvert</code> will accomodate. Duplicate columns on the same line are allowed, but the final value in the resulting argus record with be the last value encountered. </p>
<p> <code>raconvert.1</code> can read gzip and bzip2 compressed files, based on the file extension. </p>
<h2>USES</h2>
<p> <code>Raconvert</code> is predominately used for reading ASCII represented archive data. Argus data is routinely converted to ASCII for inspection and archiving, due to the good compressibility offered by gzip and others. Argus data is also converted from binary to ASCII and back to binary, as a routine process to enforce content policies. The conversion, with ASCII inspection ensures that specific data of interest isn&#8217;t leaked. </p>
<h2>INVOCATION</h2>
<pre>
<code>ra</code> -L0 c , -r argusfile &gt; argus.ascii.csv 
<code>raconvert</code> -r argus.ascii.csv -w argusfile
</pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a>(1),</code> <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5),</code> <code><a href="/docs/linux/man/8-argus/">argus</a>(8),</code></p>
<h2>FILES</h2>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>BUGS</h2>
<h2>Index</h2>
