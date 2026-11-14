---
title: "csv2ods(1)"
name: "csv2ods"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csv2ods/"
description: "csv2ods – Create OpenDocument spreadsheet from comma separated values"
---

<p>csv2ods &#8211; Create OpenDocument spreadsheet from comma separated values</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>csv2ods</code> -i&nbsp;<wbr><i>file.csv</i> -o&nbsp;<wbr><i>file.ods</i></dl>
<h2>Description</h2>
<dd>This program reads a file in CSV format &#8211; table of columns delimited by commas, tabs or any other character. It then creates a spreadsheet. If a value looks like a number the cell is formatted as a number as well.</p>
<h2>Options</h2>
<p> &#8211;version</p>
<dl>
<dt>
<dd> Show program&#8217;s version number and exit</dl>
<p> -h, &#8211;help</p>
<dl>
<dt>
<dd> Show help message and exit</dl>
<p> -i <i>INPUT</i>, &#8211;input=<i>INPUT</i></p>
<dl>
<dt>
<dd> File input in csv.</dl>
<p> -o <i>OUTPUT</i>, &#8211;output=<i>OUTPUT</i></p>
<dl>
<dt>
<dd> File output in ods.</dl>
<p> -d <i>DELIMITER</i>, &#8211;delimiter=<i>DELIMITER</i></p>
<dl>
<dt>
<dd> Specifies a one-character string to use as the field separator. It defaults to &quot;,&quot;.</dl>
<p> -c <i>ENCODING</i>, &#8211;encoding=<i>ENCODING</i></p>
<dl>
<dt>
<dd> Specifies the encoding the file csv. It defaults to utf-8.</dl>
<p> -t <i>TABLENAME</i>, &#8211;table=<i>TABLENAME</i></p>
<dl>
<dt>
<dd> The table name in the output file.</dl>
<p> -s <i>SKIPINITIALSPACE</i>, &#8211;skipinitialspace=<i>SKIPINITIALSPACE</i></p>
<dl>
<dt>
<dd> Specifies how to interpret whitespace which immediately follows a delimiter. It defaults to False, which means that whitespace immediately following a delimiter is part of the following field.</dl>
<p> -l <i>LINETERMINATOR</i>, &#8211;lineterminator=<i>LINETERMINATOR</i></p>
<dl>
<dt>
<dd> Specifies the character sequence which should terminate rows.</dl>
<p> -q <i>QUOTING</i>, &#8211;quoting=<i>QUOTING</i></p>
<dl>
<dt>
<dd> It can take on any of the following module constants: 0 = QUOTE_MINIMAL means only when required, for example, when a field contains either the quotechar or the delimiter. 1 = QUOTE_ALL means that quotes are always placed around fields. 2 = QUOTE_NONNUMERIC means that quotes are always placed around fields which do not parse as integers or floating point numbers. 3 = QUOTE_NONE means that quotes are never placed around fields. It defaults is QUOTE_MINIMAL.</dl>
<p> -e <i>ESCAPECHAR</i>, &#8211;escapechar=<i>ESCAPECHAR</i></p>
<dl>
<dt>
<dd> Specifies a one-character string used to escape the delimiter when quoting is set to QUOTE_NONE.</dl>
<p> -r <i>QUOTECHAR</i>, &#8211;quotechar=<i>QUOTECHAR</i></p>
<dl>
<dt>
<dd> Specifies a one-character string to use as the quoting character. It defaults to &quot;.</dl>
<h2>Example</h2>
<dl>
<dt>
<dd> <font SIZE="-1"> </font></p>
<pre>
csv2ods -i /etc/passwd -o accounts.odt -d:
</pre>
<p> <font SIZE="+1"></dl>
<p> </font></p>
<h2>Author</h2>
<p> <code>Agustin Henze</code> &lt;agustinhenze at gmail.com&gt;</p>
<dl>
<dt>
<dd> Original author of csv-ods.py</dl>
<h2>Index</h2>
