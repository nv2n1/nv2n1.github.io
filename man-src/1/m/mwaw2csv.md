---
title: "mwaw2csv(1)"
name: "mwaw2csv"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mwaw2csv/"
description: "mwaw2csv – convert Mac spreadsheet into CSV"
---

<h2>NAME</h2>
<p> mwaw2csv &#8211; convert Mac spreadsheet into CSV</p>
<h2>SYNOPSIS</h2>
<p> <code>mwaw2csv</code> [<i>OPTION</i>] <i>&lt;Mac Spreadsheet Document&gt;</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>:</p>
<dd> Shows this help message</p>
<dt><code>-dc</code>:</p>
<dd> Sets the decimal commas to character c: default .</p>
<dt><code>-fc</code>:</p>
<dd> Sets the field separator to character c: default ,</p>
<dt><code>-tc</code>:</p>
<dd> Sets the text separator to character c: default &quot;</p>
<dt><code>-F</code>:</p>
<dd> Sets to output the formula which exists in the file</p>
<dt><code>-Dformat</code>:</p>
<dd> Sets the date format: default &quot;%m/%d/%y&quot;</p>
<dt><code>-Tformat</code>:</p>
<dd> Sets the time format: default &quot;%H:%M:%S&quot;</p>
<dt> <code>-o</code> file.csv: Defines the ouput file</p>
<dt><code>-v</code>:</p>
<dd>
<dd>Output mwaw2csv version</dl>
<h3>Example:</h3>
<dl>
<dt>
<dd> mwaw2cvs <code>-d</code>, <code>-D</code>&quot;%d/%m/%y&quot; file : Converts a file using french locale</dl>
<h3>Note:</h3>
<dl>
<dt>
<dd> If <code>-F</code> is present, the formula are generated which english names </p>
</dl>
<h2>Index</h2>
