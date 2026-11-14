---
title: "join-dctrl(1)"
name: "join-dctrl"
section: "1"
letter: "j"
url: "/docs/linux/man/1-join-dctrl/"
description: "join-dctrl – perform relational join on data in dctrl format"
---

<h2 class="name">NAME</h2>
<p> join-dctrl &#8211; perform relational join on data in dctrl format </p>
<h2>SYNOPSIS</h2>
<p> <code>join-dctrl</code> [ <i>options</i> ] <i>filename</i> <i>filename</i> </p>
<p> <code>join-dctrl</code> <code>&#8211;version</code> </p>
<p> <code>join-dctrl</code> <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> <code>join-dctrl</code> performs a relational join operation on data given to it in Debian control file format. </p>
<p> A <i>join field</i> must be specified using either the switches <code>-1</code> and <code>-2</code> or the switch <code>-j</code>. Conceptually, the program creates all ordered pairs of records that can be formed by having a record from the first file as the first member of the pair and having a record from the second file as the second member of the pair; and then it deletes all such pairs where the join fields are not equal. Effectively, each of the input files is treated as a relational database table. </p>
<p> Every input file must be in ascending order on its join field; this allows the program to work fast. The <code><a href="/docs/linux/man/1-sort-dctrl/">sort-dctrl</a></code>(1) program can be used to make it so.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1 </code><i>field</i>, <code>&#8211;1st-join-field=</code><i>field</p>
<dd> Specify the join field</i> of the first input file.</p>
<dt><code>-2 </code><i>field</i>, <code>&#8211;2nd-join-field=</code><i>field</p>
<dd> Specify the join field</i> of the second input file.</p>
<dt><code>-j </code><i>field</i>, <code>&#8211;join-field=</code><i>field</p>
<dd> Specify a common join field</i> for all files.</p>
<dt><code>-a </code><i>fileno</i>, <code>&#8211;unpairable-from=</code><i>fileno</p>
<dd> Specify that unmatched paragraphs from the first (if </i><code>1</code> is given) or the second (if <code>2</code> is given) file are printed.</p>
<dt><code>-o </code><i>fieldspec</i>, <code>&#8211;output-fields=</code><i>fieldspec</p>
<dd> Specify which fields are included in the output. Fields are separated by commas (more than one </i><code>-o</code> option can be used, too). Each field is specified in the format <i>fileno</i><code>.</code><i>field</i> in which <i>fileno</i> is the ordinal number of the input file from which the field is drawn (either <code>1</code> or <code>2</code>), and <i>field</i> gives the name of the field to use. As a special case, simple <code>0</code> can be used instead of <i>fileno</i><code>.</code><i>field</i> to refer to the common value of the join fields.</p>
<dt>
<dd> The name of the field (not including the file number) is used in the output as the name of the field. However, a different name for output purposes can be specified by suffixing the field specification by a colon and the preferred visible name.</p>
<dt>
<dd> For example, the option <code>-o 0,1.Version:Old-Version,2.Version</code> specifies that the first field in any output record should be the join field, the second field should be <code>Old-Version</code> drawing its data from the <code>Version</code> field of the first input file, and the third field should be <code>Version</code> drawing its data from the field with the same name in the second input file, and these are the only fields in an output record.</p>
<dt>
<dd> If no <code>-o</code> option is given, all fields of all the records being joined are included in the output.</p>
<dt><code>-l </code><i>level</i>, <code>&#8211;errorlevel=</code><i>level</p>
<dd> Set log level to level</i>. <i>level</i> is one of <code>fatal</code>, <code>important</code>, <code>informational</code> and <code>debug</code>, but the last may not be available, depending on the compile-time options. These categories are given here in order; every message that is emitted when <code>fatal</code> is in effect, will be emitted in the <code>important</code> error level, and so on. The default is <code>important</code>.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print out version information.</p>
<dt><code>-C</code>, <code>&#8211;copying</code></p>
<dd> Print out the copyright license. This produces much output; be sure to redirect or pipe it somewhere (such as your favourite pager).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print out a help summary.</dl>
<h2>OPERANDS</h2>
<p> <code>join-dctrl</code> will treat each file named on the command line as a relational database table. A file called <code>&#8211;</code> represents the program&#8217;s standard input stream. Currently, exactly two files must be named.</p>
<h2>STDIN</h2>
<p> The standard input stream may be used as input as specified above in the <code>OPERANDS</code> section.</p>
<h2>INPUT FILES</h2>
<p> All input to <code>join-dctrl</code> is in the format of a Debian control file. </p>
<p> A Debian control (dctrl) file is a semistructured single-table database stored in a machine-parseable text file. Such a database consists of a set of records; each record is a mapping from field names to field content. Textually, records are separated by empty lines, while each field is encoded as one or more nonempty lines inside a record. A field starts with its name, followed by a colon, followed by the field content. The colon must reside on the first line of the field, and the first line must start with no whitespace. Subsequent lines, in contrast, always start with linear whitespace (one or more space or tab characters). </p>
<p> Each input file must be in the ascending order of its join field.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The standard locale environment, specifically its character set setting, affects the interpretation of input and output as character streams.</p>
<h2>ASYNCHRONOUS EVENTS</h2>
<p> Standard UNIX signals have their usual meaning.</p>
<h2>STDOUT</h2>
<p> All output is sent to the standard output stream. The output is in the format of a Debian control file, described above in the <code>INPUT FILES</code> section. The output will be in the ascending order of the join field, if that field is included in the output.</p>
<h2>OUTPUT FILES</h2>
<p> There are no output files.</p>
<h2>EXIT STATUS</h2>
<p> This utility exits with <code>0</code> when successful. It uses a nonzero exit code inconsistently when an error is noticed (this is a bug).</p>
<h2>CONSEQUENCES OF ERRORS</h2>
<p> In case of errors in the input, the output will be partially or completely garbage. In case of errors in invocation, the program will refuse to function.</p>
<h2>EXAMPLES</h2>
<p> Suppose that a file containing data about binary packages for the AMD64 architecture contained in the Debian squeeze (6.0) release, section <code>main</code>, is in the current directory and named <i>Packages</i>. Suppose that we are currently on a Debian system. Suppose further that the current directory does not contain files named <i>stat</i> and <i>pkg</i>. The following commands gives, for each package currently installed and available in Debian squeeze (6.0), its currently installed version (as Old-Version) and the version in squeeze (as New-Version): </p>
<pre>
$ sort-dctrl -kPackage /var/lib/dpkg/status &gt; stat
$ sort-dctrl -kPackage Packages &gt; pkg
$ join-dctrl -j Package \
  -o 0,1.Version:Old-Version,2.Version:New-Version \
  stat pkg
</pre>
<h2>AUTHOR</h2>
<p> The <code>join-dctrl</code> program and this manual page were written by Antti-Juhani Kaijanaho.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-grep-dctrl/">grep-dctrl</a></code>(1), <code><a href="/docs/linux/man/1-sort-dctrl/">sort-dctrl</a></code>(1), <code><a href="/docs/linux/man/1-tbl-dctrl/">tbl-dctrl</a></code>(1) </p>
<h2>Index</h2>
