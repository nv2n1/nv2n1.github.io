---

title: "xls2csv(1)"
name: "xls2csv"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xls2csv/"
description: "xls2csv – reads MS-Excel file and puts its content as comma-separated data on standard output"
---

<p> xls2csv - reads MS-Excel file and puts its content as comma-separated data on standard output  </p>
<h2>SYNOPSIS</h2>
<p> <code>xls2csv </code>[<code>-xlV</code>] [<code>-f</code> <i> format </i>] [<code>-b</code> <i> string </i>] [<code>-s</code> <i> charset </i>] [<code>-d</code> <i> charset </i>] [-q <i> number </i>] [<code>-c</code> <i> char</i>] <i>files</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>xls2csv </code> reads MS-Excel spreadsheet and dumps its content as comma-separated values to stdout. Numbers are printed without delimiters, strings are enclosed in the double quotes. Double-quotes inside string are doubled.  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-x</code></dt>
<dd> <p> print unknown Unicode chars as \xNNNN, rather than as question marks </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> list known charsets and exit successfully </p>
 </dd>
<dt><code>-c</code><i>char</i></dt>
<dd> <p> cell separator char. By default - comma. </p>
 </dd>
<dt><code>-b</code><i>string</i></dt>
<dd> <p> sheet break string. This string (by default - formfeed) would be output at the end of each workbook page. This string is printed after page starting at start of line, but no linefeed would be automatically added at the end of string. Include newline at the ent of sheet separator if you want it to appear on separate line by itself </p>
 </dd>
<dt><code>-g</code><i>number</i></dt>
<dd> <p> number of decimal digits in the numbers. By default maximal double precision (system-dependent macro DBL_DIG) is used. </p>
 </dd>
<dt><code>-q</code><i>number</i></dt>
<dd> <p> set quote mode. In quote mode 0 cell contents is never quoted. In quote mode 1 only strings which contain spaces, double quotes or commas are quoted. In quote mode 2 (default) all cells with type string are quoted. In quote mode 3 all cells are quoted. </p>
 </dd>
<dt><code>-d</code><i>charset`</i></dt>
<dd> <p> - specifies destination charset name. Charset file has format described in CHARACTER SETS section of <code><a href="/docs/linux/man/1-catdoc/">catdoc</a></code>(1) manual page. By default, current locale charset would be used if langinfo support was enabled at the compile time. </p>
 </dd>
<dt><code>-s</code><i>charset</i></dt>
<dd> <p> - specifies source charset. Typically, Excel files have CODE PAGE record, which denotes input charset, but for some reason you may wish to override it. </p>
 </dd>
<dt><code>-f</code><i>format</i></dt>
<dd> <p> - specifies date/time format to use for output of all Excel date and time values. If this option is not specified, format, specified in the spreadsheet is used. On POSIX system any format, allowed by <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) can be used as value of this option. Under MS-DOS <code>xls2csv</code> implements limited set of <code>strftime </code> formats, namely <code>m</code>, <code>d</code>, <code>y</code>, <code>Y</code>, <code>b</code>, <code>l</code>, <code>p</code>, <code>H</code>, <code>M</code>, <code>S</code>. </p>
 </dd>
<dt><code>-V</code></dt>
<dd> <p> outputs version number </p>
 </dd></dl>
<h2>FILES</h2>
<p> ${HOME}/.catdocrc, catdoc charset files and substitution map files (see <code><a href="/docs/linux/man/1-catdoc/">catdoc</a></code>(1) manual page for details, </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1), <code><a href="/docs/linux/man/1-catdoc/">catdoc</a></code>(1), <code><a href="/docs/linux/man/1-strings/">strings</a></code>(1), <code>utf</code>(4), <code>unicode</code>(4) </p>
<h2>AUTHOR</h2>
<p> V.B.Wagner &lt;vitus [at] 45.free.net&gt;, based on biffview by David Rysdam </p>
