---
title: "extract_vba(1)"
name: "extract_vba"
section: "1"
letter: "e"
url: "/docs/linux/man/1-extract_vba/"
description: "extract_vba – A utility to extract a VBA project from an Excel 2007+ xlsm file."
---

<h2 class="name">NAME</h2>
<p> extract_vba &#8211; A utility to extract a VBA project from an Excel 2007+ xlsm file. </p>
<h2>DESCRIPTION</h2>
<p> This utility is used to extract the <font SIZE="-1">VBA</font> project binary from an Excel 2007+ xlsm file. The <font SIZE="-1">VBA</font> project can then be added to an Excel::Writer::XLSX file to enable it to have macros. </p>
<p> An <tt>&quot;xlsm&quot;</tt> file is a version of an Excel <tt>&quot;xlsx&quot;</tt> file that contains an additional <font SIZE="-1">VBA</font> project binary file. The <tt>&quot;xlsm&quot;</tt> file format is a collection of mainly <font SIZE="-1">XML</font> files in a <font SIZE="-1">ZIP</font> container. </p>
<p> The extracted <font SIZE="-1">VBA</font> project is an <font SIZE="-1">OLE</font> Compound Document in binary format. It is named <tt>&quot;vbaProject.bin&quot;</tt> and is generally located in the <tt>&quot;xl&quot;</tt> directory of the <tt>&quot;xlsm&quot;</tt> file. </p>
<p> See the <tt>&quot;add_vba_project()&quot;</tt> section of the Excel::Writer::XLSX documentation for more details. </p>
<p> Note: you can also extract the <font SIZE="-1">VBA</font> project from an <tt>&quot;xlsm&quot;</tt> file using the standard Linux <tt>&quot;unzip&quot;</tt> command: </p>
<pre>
    unzip -j macro01.xlsm xl/vbaProject.bin
</pre>
<p> On Windows you can use any suitable Unzip application.</p>
<h2>SYNOPSIS</h2>
<pre>
    $ extract_vba file.xlsm
    Extracted 'vbaProject.bin' successfully
    $ extract_vba -h # For help.
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help or -h</code></p>
<dd> Print the help documentation.</dl>
<h2>AUTHOR</h2>
<p> John McNamara jmcnamara [at] cpan.org</p>
<h2>VERSION</h2>
<p> Version 0.01.</p>
<h2>COPYRIGHT</h2>
<p> (c) <font SIZE="-1">MMXV,</font> John McNamara. </p>
<p> All Rights Reserved. This program is free software. It may be used, redistributed and/or modified under the same terms as Perl itself. </p>
<h2>Index</h2>
