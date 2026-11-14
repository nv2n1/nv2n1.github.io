---
title: "tbl-dctrl(1)"
name: "tbl-dctrl"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tbl-dctrl/"
description: "tbl-dctrl – generate tabular representations of data in dctrl format"
---

<h2 class="name">NAME</h2>
<p> tbl-dctrl &#8211; generate tabular representations of data in dctrl format </p>
<h2>SYNOPSIS</h2>
<p> <code>tbl-dctrl</code> [ <i>options</i> ] [ <code>-c</code> <i>column-specification</i> &#8230; ] [ <i>filename</i> ] &#8230; </p>
<p> <code>tbl-dctrl</code> <code>&#8211;version</code> </p>
<p> <code>tbl-dctrl</code> <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> <code>tbl-dctrl</code> creates tabular representations of data given to it in Debian control file format. </p>
<p> By default, <code>tbl-dctrl</code> reads the whole database, looking for the longest entry in each requested column; it then outputs a table, with borders and column titles, where each column is just wide enough to fit the longest entry. Most of this behaviour can be customized as described below. </p>
<p> A column is requested by specifying the <code>-c</code> (<code>&#8211;column</code>) switch with a column specification. The simplest kind of a column specification consists solely of the name of a field. In such a case, <code>tbl-dctrl</code> will include in the output a column whose title is the literal column specification and whose data is drawn from fields with that name. If no <code>-c</code> options are given, <code>tbl-dctrl</code> will use all fields in the input in the order in which they first appear. </p>
<p> There are two optional additions one can make to a column specification. Prefixing the field name with some text followed by an equality sign (for example, <code>-c &#8216;Package name=Package&#8217;</code>) modifies the column in such a way that the text before the equality sign is used as the column title, while the text after the equality sign is used as the name of the field from which data is drawn. One can also append a colon followed by a positive whole number to the field name. In such a case, the number after the colon specifies the width of the column. These two additions can be used separately or together. If there are more than one colon, the last one is significant. If there are more than one equals sign, the first one is significant. Other colons and equals signs are used simply as data. Note that the whole column specification must be given to <code>tbl-dctrl</code> as one argument, so if it contains spaces, it must be quoted for the shell. </p>
<p> If all requested columns have a specified width, <code>tbl-dctrl</code> will produce output immediately, not waiting for the whole input to be read in.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d </code><i>delimiter</i>, <code>&#8211;delimiter=</code><i>delimiter</p>
<dd> Instead of drawing nice borders to the table, use the specified delimiter</i> string to delimit columns in a row.</p>
<dt><code>-H</code>, <code>&#8211;no-heading</p>
<dd> Do not print a table heading (column titles).</p>
<dt>-l </code><i>level</i>, <code>&#8211;errorlevel=</code><i>level</p>
<dd> Set log level to level</i>. <i>level</i> is one of <code>fatal</code>, <code>important</code>, <code>informational</code> and <code>debug</code>, but the last may not be available, depending on the compile-time options. These categories are given here in order; every message that is emitted when <code>fatal</code> is in effect, will be emitted in the <code>important</code> error level, and so on. The default is <code>important</code>.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print out version information.</p>
<dt><code>-C</code>, <code>&#8211;copying</code></p>
<dd> Print out the copyright license. This produces much output; be sure to redirect or pipe it somewhere (such as your favourite pager).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print out a help summary.</dl>
<h2>OPERANDS</h2>
<p> <code>tbl-dctrl</code> will read its input from the files named on the command line, in the specified order. A file called <code>&#8211;</code> represents the program&#8217;s standard input stream. If no files are named, the program behaves as if <code>&#8211;</code> alone had been named, that is, input is read from the standard input stream.</p>
<h2>STDIN</h2>
<p> The standard input stream may be used as input as specified above in the <code>OPERANDS</code> section.</p>
<h2>INPUT FILES</h2>
<p> All input to <code>tbl-dctrl</code> is in the format of a Debian control file. </p>
<p> A Debian control (dctrl) file is a semistructured single-table database stored in a machine-parseable text file. Such a database consists of a set of records; each record is a mapping from field names to field content. Textually, records are separated by empty lines, while each field is encoded as one or more nonempty lines inside a record. A field starts with its name, followed by a colon, followed by the field content. The colon must reside on the first line of the field, and the first line must start with no whitespace. Subsequent lines, in contrast, always start with linear whitespace (one or more space or tab characters). </p>
<p> When input is read from multiple files, a record separator is implicit between two adjacent files.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The standard locale environment, specifically its character set setting, affects the interpretation of input and output as character streams.</p>
<h2>ASYNCHRONOUS EVENTS</h2>
<p> Standard UNIX signals have their usual meaning.</p>
<h2>STDOUT</h2>
<p> All output is sent to the standard output stream. The output is a tabular representation of the input database restricted to the specified fields. Logically, the output is a table; when the <code>-d</code> option is used, this table is represented simply by separating columns in each row by the specified <i>delimiter</i>; when the option is not used, a frame is drawn around the table. The order of the columns is the same as the order of the column specifications on the command line.</p>
<h2>OUTPUT FILES</h2>
<p> There are no output files.</p>
<h2>EXIT STATUS</h2>
<p> This utility exits with <code>0</code> when successful. It uses a nonzero exit code inconsistently when an error is noticed (this is a bug).</p>
<h2>CONSEQUENCES OF ERRORS</h2>
<p> In case of errors in the input, the output will be partially or completely garbage. In case of errors in invocation, the program will refuse to function.</p>
<h2>EXAMPLES</h2>
<p> The following command line pipe outputs a table of all packages, with their maintainer data, sorted by the maintainer data, that have no content: </p>
<pre>
% grep-available -FInstalled-Size --eq 0 | sort-dctrl -kMaintainer - \
  | tbl-dctrl -cPackage -cMaintainer
</pre>
<h2>AUTHOR</h2>
<p> The <code>tbl-dctrl</code> program and this manual page were written by Antti-Juhani Kaijanaho.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-apt-cache/">apt-cache</a></code>(1), <code><a href="/docs/linux/man/1-ara/">ara</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-awk/">dpkg-awk</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-query/">dpkg-query</a></code>(1), <code><a href="/docs/linux/man/1-grep-dctrl/">grep-dctrl</a></code>(1), <code><a href="/docs/linux/man/1-sort-dctrl/">sort-dctrl</a></code>(1), <code><a href="/docs/linux/man/8-dpkg/">dpkg</a></code>(8) </p>
<h2>Index</h2>
