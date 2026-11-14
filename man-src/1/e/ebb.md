---
title: "ebb(1)"
name: "ebb"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ebb/"
description: "extractbb, ebb – extract bounding box information from graphics files"
---

<h2>NAME</h2>
<p> extractbb, ebb &#8211; extract bounding box information from graphics files </p>
<h2>SYNOPSIS</h2>
<p> <code>extractbb</code> [<code>-v</code>|<code>-q</code>] [<code>-O</code>] [<code>-m</code>|<code>-x</code>] <i>file</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> For each <font SIZE="-1">JPEG</font>, <font SIZE="-1">PNG</font>, or <font SIZE="-1">PDF</font> file given on the command line, <code>extractbb</code> extracts the bounding box information and writes it into a file with extension <code>.xbb</code>, together with some header information. These files can then be used by <code>dvipdfmx</code> or other programs. For <font SIZE="-1">PDF</font> files, the number of pages and the <font SIZE="-1">PDF</font> version number are reported as well. The input filename extension may be in upper or lower case. </p>
<p> If called as <code>ebb</code>, the output is written in the &#8220;bb&#8221; format (and with extension <code>.bb</code>) as used by <code>dvipdfm</code>. <code>Xbb</code> may be defined as a synomym for <code>extractbb</code> on your system. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Be verbose.</p>
<dt><code>-q</code></p>
<dd> Be quiet.</p>
<dt><code>-O</code></p>
<dd> Write output to standard output.</p>
<dt><code>-m</code></p>
<dd> Write output in dvipdfm&#8217;s &#8220;bb&#8221; format.</p>
<dt><code>-x</code></p>
<dd> Write output in dvipdfmx&#8217;s &#8220;xbb&#8221; format (default), which is the same as that used by pdfTeX.</dl>
<h2>OUTPUT FORMATS</h2>
<p> Here are more details about the bb and xbb formats: </p>
<p> The original ebb (from dvipdfm) ignored density information in bitmap images, and generated bounding boxes with 100px = 72bp = 1in. Unfortunately, screenshots (especially) tend to look bad with this approach. </p>
<p> So, extractbb (from dvipdfmx) uses density information if present. Otherwise, it generates bounding box with 100px = 100bp. This is what pdfTeX does.</p>
<h2>BUGS</h2>
<p> There is currently no way to specify which bounding box is taken for <font SIZE="-1">PDF</font> files. It will always be the first one from the following list: ArtBox, TrimBox, BleedBox, MediaBox. (Often only MediaBox is defined.) Moreover, the reported bounding box always refers to the first page in a <font SIZE="-1">PDF</font> file. </p>
<h2>AUTHOR</h2>
<p> <code>extractbb</code> was written by the DVIPDFMx project team &lt;dvipdfmx [at] ktug.or.kr&gt;, based on the program <code>ebb</code> by Mark A. Wicks. </p>
<p> This manual page was also written by the DVIPDFMx project team, based on a manual page Frank K&uuml;ster &lt;frank [at] kuesterei.ch&gt; wrote for the Debian GNU/Linux system. It may be used, modified, and/or redistributed by others without contacting the authors. </p>
<h2>Index</h2>
