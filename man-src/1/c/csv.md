---
title: "csv(1)"
name: "csv"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csv/"
description: "csv – process CSV files from the command line"
---

<h2 class="name">NAME</h2>
<p> csv &#8211; process CSV files from the command line </p>
<h2>SYNOPSIS</h2>
<pre><code>
#On the command line:
  csv 1 2 -1 &lt; report.csv
#Reads the first two fields, as well as the last one, from "report.csv".
#Data is cleaned up and emitted as CSV.
  csv --fields Revenue,Q1,Q2 &lt; report.csv   # or "-f" for short
#First line of the input(from file "report.csv") is considered as
#header line; the fields are emitted in the order "Revenue", "Q1",
# and "Q2".Data is cleaned up and emitted as CSV.
  csv --input report.csv --to_tsv
#Converts the whole report to TSV(tab - separated values).
</code></pre>
<h2>DESCRIPTION</h2>
<p> <font SIZE="-1">CSV </font>(comma-separated value) files are the lowest common denominator of structured data interchange formats. For such a humble file format, it is pretty difficult to get right: embedded quote marks and linebreaks, slipshod delimiters, and no One True Validity Test make <font SIZE="-1">CSV</font> data found in the wild hard to parse correctly. Text::CSV_XS provides flexible and performant access to <font SIZE="-1">CSV</font> files from Perl, but is cumbersome to use in one-liners and the command line. </p>
<p> <code>csv</code> is intended to make commandline processing of <font SIZE="-1">CSV</font> files as easy as plain text is meant to be on Unix. Internally, it holds two Text::CSV objects (for input and for output), which have reasonable defaults but which you can reconfigure to suit your needs. Then you can extract just the fields you want, change the delimiter, clean up the data etc. </p>
<p> In the simplest usage, <code>csv</code> filters stdio and takes a list of integers. These are 1-based column numbers to select from the input <font SIZE="-1">CSV</font> stream. Negative numbers are counted from the line end. Without any column list, <code>csv</code> selects all columns (this is still useful to normalize quoting style etc.).</p>
<h3>Command line options</h3>
<p> The following options are passed to Text::CSV. When preceded by the prefix &#8220;output_&#8221;, the destination is affected. Otherwise these options affect both input and output.</p>
<dl>
<dt><code>&#8211;quote_char</code></p>
<dd>
<dt><code>&#8211;escape_char</code></p>
<dd>
<dt><code>&#8211;sep_char</code></p>
<dd>
<dt><code>&#8211;eol</code></p>
<dd>
<dt><code>&#8211;always_quote</code></p>
<dd>
<dt><code>&#8211;binary</code></p>
<dd>
<dt><code>&#8211;keep_meta_info</code></p>
<dd>
<dt><code>&#8211;allow_loose_quotes</code></p>
<dd>
<dt><code>&#8211;allow_loose_escapes</code></p>
<dd>
<dt><code>&#8211;allow_whitespace</code></p>
<dd>
<dt><code>&#8211;verbatim</code></p>
<dd></dl>
<p> <font SIZE="-1"><code>NOTE</code></font>: <i>binary</i> is set to 1 by default in <code>csv</code>. The other options have their Text::CSV defaults. </p>
<p> The following additional options are available:</p>
<dl>
<dt><code>&#8211;input</code>, <code>-i</code></p>
<dd>
<dt><code>&#8211;output</code>, <code>-o</code></p>
<dd> Filenames for input and output. &#8220;-&#8221; means stdio. Useful to trigger <font SIZE="-1">TSV</font> mode (<tt>&quot;--from_tsv&quot;</tt> and <tt>&quot;--to_tsv&quot;</tt>).</p>
<dt><code>&#8211;columns</code>, <code>-c</code></p>
<dd> Column numbers may be specified using this option.</p>
<dt><code>&#8211;fields</code>, <code>-f</code></p>
<dd> When this option is specified, the first line of the input file is considered as a header line. This option takes a comma-separated list of column-names from the first line. </p>
<p> For convenience, this option also accepts a comma-separated list of column numbers as well. Multiple &#8211;fields options are allowed, and both column names and numbers can be mixed together.</p>
<dt><code>&#8211;from_tsv</code>, <code>&#8211;from-tsv</code></p>
<dd>
<dt><code>&#8211;to_tsv</code>, <code>&#8211;to-tsv</code></p>
<dd> Use tabs instead of commas as the delimiter. When <code>csv</code> has the input or output filenames available, this is inferred when they end with <tt>&quot;.tsv&quot;</tt>. To disable this dwimmery, you may say <tt>&quot;--to_tsv=0&quot;</tt> and <tt>&quot;--from_tsv=0&quot;</tt>.</dl>
<h2>SEE ALSO</h2>
<p> Text::CSV, Text::CSV_XS</p>
<h2>AUTHOR</h2>
<p> Gaal Yahas <tt>&quot;&lt;gaal [at] forum2.org&gt;&quot;</tt></p>
<h2>THANKS</h2>
<p> nothingmuch, gphat, t0m, themoniker, Prakash Kailasa, tsibley, srezic, and ether.</p>
<h2>BUGS</h2>
<p> Please report any bugs or feature requests to <tt>&quot;bug-app-csv at rt.cpan.org&quot;</tt>, or through the web interface at &lt;<a rel="nofollow" href="http://rt.cpan.org/NoAuth/ReportBug.html?Queue=App-CSV">http://rt.cpan.org/NoAuth/ReportBug.html?Queue=App-CSV</a>&gt;. I will be notified, and then you&#8217;ll automatically be notified of progress on your bug as I make changes. </p>
<p> You&#8217;re also invited to work on a patch. The source repo is at </p>
<p> &lt;<a href="git://github.com/gaal/app-csv.git">git://github.com/gaal/app-csv.git</a>&gt; </p>
<p> &lt;<a rel="nofollow" href="http://github.com/gaal/app-csv/tree/master">http://github.com/gaal/app-csv/tree/master</a>&gt;</p>
<h2>COPYRIGHT (The MIT License)</h2>
<p> Copyright 2013 Gaal Yahas. </p>
<p> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &#8220;Software&#8221;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: </p>
<p> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. </p>
<p> <font SIZE="-1">THE SOFTWARE IS PROVIDED &#8220;AS IS&#8221;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</font> </p>
<h2>Index</h2>
