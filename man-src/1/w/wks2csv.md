---

title: "wks2csv(1)"
name: "wks2csv"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wks2csv/"
description: "wks2csv – convert Works spreadsheet into CSV"
---

<p> wks2csv &#8211; convert Works spreadsheet into CSV</p>
<h2>SYNOPSIS</h2>
<p> <code>wks2csv</code> [<i>OPTION</i>] <i>&lt;Works Spreadsheet Document&gt;</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>:</dt>
<dd> Shows this help message</dd>
<dt><code>-dc</code>:</dt>
<dd> Sets the decimal commas to character c: default .</dd>
<dt><code>-fc</code>:</dt>
<dd> Sets the field separator to character c: default ,</dd>
<dt><code>-tc</code>:</dt>
<dd> Sets the text separator to character c: default &quot;</dd>
<dt><code>-F</code>:</dt>
<dd> Sets to output the formula which exists in the file</dd>
<dt><code>-Dformat</code>:</dt>
<dd> Sets the date format: default &quot;%m/%d/%y&quot;</dd>
<dt><code>-Tformat</code>:</dt>
<dd> Sets the time format: default &quot;%H:%M:%S&quot;</dd>
<dt> <code>-o</code> file.csv: Defines the ouput file</dt>
<dt><code>-v</code>:</dt>
<dd>
</dd><dd>Output wks2csv version</dd></dl>
<h3>Example:</h3>
<dl>
<dt>
</dt><dd> wks2cvs <code>-d</code>, <code>-D</code>&quot;%d/%m/%y&quot; file : Converts a file using french locale</dd></dl>
<h3>Note:</h3>
<dl>
<dt>
</dt><dd> If <code>-F</code> is present, the formula are generated which english names </dd>
</dl>
