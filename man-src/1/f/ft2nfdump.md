---
title: "ft2nfdump(1)"
name: "ft2nfdump"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ft2nfdump/"
description: "ft2nfdump – flow-tools data converter program"
---

<h2>NAME</h2>
<p> ft2nfdump &#8211; flow-tools data converter program</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ft2nfdump [options]</code></dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>ft2nfdump</code></p>
<dd>is the flow-tools converter program to read, convert and store netflow data, created with the flow-tools package. It works either as a pipe filter or reads flow-tools data format directly from file and exports nfdump data format at stdout. </dd>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r &lt;flow-tools-file&gt;</code></dt>
<dd> Read flow-tools formated netflow data from file <i>flow-tools-file. Default: Read from stdin.</dd>
<dt></i><code>-w &lt;nfdump-file&gt;</code></dt>
<dd> Write nfdump formated file for converted netflow data Default: Write to stdout.</dd>
<dt><code>-j</code></dt>
<dd> Compress flows. Use bz2 compression in output file. Space efficient methode</dd>
<dt><code>-z</code></dt>
<dd> Compress flows. Use fast LZO1X-1 compression in output file. Fastest method</dd>
<dt><code>-c </code><i>num</i></dt>
<dd> Read only <code>num</code> flows from input file.</dd>
<dt><code>-E</code></dt>
<dd> Print raw netflow records to stdout. This option is for debugging purpose only, to see any incoming netflow data. Compatible to option -E in nfcapd.</dd>
<dt><code>-V</code></dt>
<dd> Print ft2nfdump version and exit.</dd>
<dt><code>-h</code></dt>
<dd> Print help text on stdout with all options and exit.</dd></dl>
<h2>RETURN VALUE</h2>
<p> Returns</p>
<dl>
<dt>
</dt><dd>
<p> 0 No error. </p>
<p> 255 Conversion failed.</dd></dl>
<h2>EXAMPLES</h2>
<p> <code>flow-cat ft-v05.2015-05-01.* | ft2nfdump -j -w nfcap.20150501</code> Convert files into nfdump format. </p>
<p> <code>flow-cat ft-v05.2001-05-01.* | ft2nfdump | nfdump -w nfcap.20010501</code> Convert files into nfdump format. </p>
<p> <code>ft2nfdump -r ft-v05.2001-05-01 | nfdump -w nfcap.20010501</code> Convert files into nfdump format. </p>
<h2>NOTES</h2>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-nfcapd/">nfcapd</a>(1), <a href="/docs/linux/man/1-nfdump/">nfdump</a>(1), <a href="/docs/linux/man/1-nfprofile/">nfprofile</a>(1), <a href="/docs/linux/man/1-nfreplay/">nfreplay</a>(1)</p>
<h2>BUGS</h2>
<h2>Index</h2>
</p>