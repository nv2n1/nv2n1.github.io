---
title: "pamslice(1)"
name: "pamslice"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamslice/"
description: "pamslice – extract one line of values out of a Netpbm image"
---

<h2 class="name">NAME</h2>
<p> pamslice &#8211; extract one line of values out of a Netpbm image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamslice</code> {<code>-row=</code><i>rownumber</i> | <code>-column=</code><i>columnnumber</i>} [<code>-plane=</code><i>planenumber</i>] [<i>imagefile</i>] </p>
<h2>OPTION USAGE</h2>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamslice</code> extracts one line of tuples (pixels) out of a Netpbm image and prints their values in a table. A line means a row or column. It shows you a one-dimensional cross section of a two-dimensional image. (With the <code>-plane</code> option, it can be thought of as a one-dimensional cross-section of a three-dimensional image). </p>
<p> The table has one line per tuple, consisting of blank-separated ASCII decimal numbers. The first number is the column number if you specified a row slice or the row number if you specified a column slice. The rest of the numbers are the sample values in plane number order. For a PBM or PGM input, there is only one plane. For a PPM input, Plane 0 is red, Plane 1 is green, and Plane 2 is blue. See the specifications of the image formats for details on exactly what these numbers mean. </p>
<p> If you want to see all the pixels in a PPM, PGM, or PBM image in ASCII decimal, <code>pnmtopnm -plain</code> is a good way to do that. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-row=</code><i>rownumber</i></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>This indicates that the slice is to be horizontal &#8212; i.e. one row of the<br />
&nbsp;<wbr>&nbsp;<wbr>image &#8212; and indicates which row.&nbsp;<wbr>&nbsp;<wbr>Rows are numbered from the top<br />
&nbsp;<wbr>&nbsp;<wbr>starting with 0. </p>
<p> You cannot specify both <code>-row</code> and <code>-column</code>. </p>
<dt><code>-column=</code><i>colnumber</i></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>This indicates that the slice is to be vertical &#8212; i.e. one column of the<br />
&nbsp;<wbr>&nbsp;<wbr>image &#8212; and indicates which column.&nbsp;<wbr>&nbsp;<wbr>Columns are numbered from the left<br />
&nbsp;<wbr>&nbsp;<wbr>starting with 0. </p>
<p> You cannot specify both <code>-row</code> and <code>-column</code>. </p>
<dt><code>-plane=</code><i>planenumber</i></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>This specifies that you are interested in only one plane of the image<br />
&nbsp;<wbr>&nbsp;<wbr>and which one.&nbsp;<wbr>&nbsp;<wbr>Planes are numbered from 0 and have meanings that vary<br />
&nbsp;<wbr>&nbsp;<wbr>on the type of image.&nbsp;<wbr>&nbsp;<wbr>In a PPM image, Plane 0 is red, Plane 1 is<br />
&nbsp;<wbr>&nbsp;<wbr>green, and Plane 2 is blue. </p>
<p> If you don&#8217;t specify <code>-plane</code>, you get all the planes &#8212; each<br />
&nbsp;<wbr>&nbsp;<wbr>line of output has multiple numbers in addition to the sequence number.<br />
&nbsp;<wbr>&nbsp;<wbr>If you do specify&nbsp;<wbr><code>-plane</code>, each line of output contains one<br />
&nbsp;<wbr>&nbsp;<wbr>number in addition to the sequence number. </p>
<dt><code>-xmgr</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>This option causes&nbsp;<wbr><code>pamslice</code>&nbsp;<wbr>to format the output as input for a<br />
&nbsp;<wbr>&nbsp;<wbr><code>xmgr</code>&nbsp;<wbr>so you can plot it.&nbsp;<wbr>&nbsp;<wbr>The only difference this option makes<br />
&nbsp;<wbr>&nbsp;<wbr>is that it adds header information to the beginning of the output. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamcut/">pamcut</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pnmtopnm/">pnmtopnm</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pnmtoplainpnm/">pnmtoplainpnm</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamslice</code> replaced <code>pgmslice</code> in Netpbm 10.3 (June 2002). It was backward compatible, but worked on Netpbm images other than PGM and PBM and added the <code>-plane</code> and <code>-xmgr</code> options. </p>
<h2>AUTHOR</h2>
<p> Jos Dingjan &lt;<i>jos [at] tuatha.org</i>&gt; wrote <code>pgmslice</code> after being unable to find the source code to Marco Beijersbergen&#8217;s program with the same name. Bryan Henderson converted it to <code>pamslice</code>. </p>
<h2>Index</h2>
