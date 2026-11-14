---
title: "chartex(1)"
name: "chartex"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chartex/"
description: "chartex – A utility to extract charts from an Excel file for insertion into a Spreadsheet::WriteExcel file."
---

<h2 class="name">NAME</h2>
<p> chartex &#8211; A utility to extract charts from an Excel file for insertion into a Spreadsheet::WriteExcel file. </p>
<h2>DESCRIPTION</h2>
<p> This program is used for extracting one or more charts from an Excel file in binary format. The charts can then be included in a <tt>&quot;Spreadsheet::WriteExcel&quot;</tt> file. </p>
<p> See the <tt>&quot;add_chart_ext()&quot;</tt> section of the Spreadsheet::WriteExcel documentation for more details.</p>
<h2>SYNOPSIS</h2>
<p> chartex [&#8211;chartname &#8211;help &#8211;man] file.xls </p>
<pre>
    Options:
        --chartname -c  The root name for the extracted charts,
                        defaults to &quot;chart&quot;.
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;chartname or -c</code></p>
<dd> This sets the root name for the extracted charts, defaults to &#8220;chart&#8221;. For example: </p>
<pre>
    $ chartex file.xls
    Extracting &quot;Chart1&quot; to chart01.bin
    $ chartex -c mychart file.xls
    Extracting &quot;Chart1&quot; to mychart01.bin
</pre>
<dt><code>&#8211;help or -h</code></p>
<dd> Print a brief help message and exits.</p>
<dt><code>&#8211;man or -m</code></p>
<dd> Prints the manual page and exits.</dl>
<h2>AUTHOR</h2>
<p> John McNamara jmcnamara [at] cpan.org</p>
<h2>VERSION</h2>
<p> Version 0.02.</p>
<h2>COPYRIGHT</h2>
<p> X <font SIZE="-1">MMV,</font> John McNamara. </p>
<p> All Rights Reserved. This program is free software. It may be used, redistributed and/or modified under the same terms as Perl itself. </p>
<h2>Index</h2>
