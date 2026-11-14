---
title: "sort-dctrl(1)"
name: "sort-dctrl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sort-dctrl/"
description: "sort-dctrl – sort Debian control files"
---

<h2 class="name">NAME</h2>
<p> sort-dctrl &#8211; sort Debian control files </p>
<h2>SYNOPSIS</h2>
<p> <code>sort-dctrl</code> [options] [ <i>file</i> &#8230; ] </p>
<p> <code>sort-dctrl</code> &#8211;copying | &#8211;help | &#8211;version | -ChV</p>
<h2>DESCRIPTION</h2>
<p> The <code>sort-dctrl</code> program sorts Debian control files according to specified criteria. </p>
<p> A Debian control (dctrl) file is a semistructured single-table database stored in a machine-parseable text file. Such a database consists of a set of records; each record is a mapping from field names to field content. Textually, records are separated by empty lines, while each field is encoded as one or more nonempty lines inside a record. A field starts with its name, followed by a colon, followed by the field content. The colon must reside on the first line of the field, and the first line must start with no whitespace. Subsequent lines, in contrast, always start with linear whitespace (one or more space or tab characters). </p>
<p> The <code>sort-dctrl</code> program recognizes two field types: string fields and version fields. Version fields act also as numeric fields. String fields are compared according to strict lexicographical octet-by-octet comparison, after ignoring any initial whitespace after the colon. Version fields are parsed and compared as Debian version numbers. When comparing version numbers, if a field content does not in fact conform to the version number syntax, it compares less than any field content that does conform, and equal to any other nonconforming field content. The <code>sort-dctrl</code> program assumes all fields are string fields unless told otherwise. </p>
<p> You can specify arbitrary number of keys for sorting, using the <code>-k</code> option. The keys are interpreted in a descending order of priority: the first key specified is primary, the second key specified is secondary, and so on. If two records compare equal under the primary key, then they are compared under the secondary key, and so on. If no keys are specified, a default key is assumed (the &quot;Package&quot; field with no modifiers).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-k </code><i>keyspec</i>, <code>&#8211;key-spec=</code><i>keyspec</p>
<dd> Specify one or more keys for sorting. You may specify this option any number of times. The keyspec</i> argument consists of a comma-separated list of key specifications. Each key specification consists of the name of the field that serves as the key, optionally followed by a colon and key modifiers. The following key modifiers are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>r</code></p>
<dd> Invert the comparison for this key, reversing the sorting order.</p>
<dt><code>v</code></p>
<dd> Treat this field as a version number field.</p>
<dt><code>n</code></p>
<dd> Treat this field as numeric, which currently is synonymous with <code>v</code>.</dl>
</dl>
<dt><code>-q</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</p>
<dd> Output nothing to the standard output stream. Instead, exit immediately after finding the first match.</p>
<dt>-l </code><i>level</i>, <code>&#8211;errorlevel=</code><i>level</p>
<dd> Set log level to level</i>. <i>level</i> is one of <code>fatal</code>, <code>important</code>, <code>informational</code> and <code>debug</code>, but the last may not be available, depending on the compile-time options. These categories are given here in order; every message that is emitted when <code>fatal</code> is in effect, will be emitted in the <code>important</code> error level, and so on. The default is <code>important</code>.</p>
<dt><code>-V</code>, <code>&#8211;version</p>
<dd> Print out version information.</p>
<dt>-C</code>, <code>&#8211;copying</p>
<dd> Print out the copyright license. This produces much output; be sure to redirect or pipe it somewhere (such as your favourite pager).</p>
<dt>-h</code>, <code>&#8211;help</p>
<dd> Print out a help summary.</dl>
<p> </code></p>
<h2>EXAMPLES</h2>
<p> Here are some sample invocations of the program:</p>
<dl>
<dt>sort-dctrl /var/lib/dpkg/available</p>
<dd> Output the <code>dpkg</code> <i>available</i> file sorted by the package name.</p>
<dt>sort-dctrl -k Version:v /var/lib/dpkg/available</p>
<dd> Output the <code>dpkg</code> <i>available</i> file sorted in ascending order of version numbers.</p>
<dt>sort-dctrl -k Version:vr /var/lib/dpkg/available</p>
<dd> Output the <code>dpkg</code> <i>available</i> file sorted in descending order of version numbers.</p>
<dt>sort-dctrl -k Package,Version:v /var/lib/dpkg/available</p>
<dd> Output the <code>dpkg</code> <i>available</i> file sorted primarily in ascending order of package names and secondarily in descending order of version numbers.</p>
<dt>sort-dctrl -k Installed-Size:n,Size:nr /var/lib/dpkg/available</p>
<dd> Output the <code>dpkg</code> <i>available</i> file sorted primarily in ascending order of installation sizes and secondarily in descending order of package sizes.</dl>
<h2>AUTHOR</h2>
<p> The program and this manual page were written by Antti-Juhani Kaijanaho &lt;ajk [at] debian.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> Debian Policy Manual. Published as the Debian package <code>debian-policy</code>. Also available in the Debian website. </p>
<p> <code><a href="/docs/linux/man/1-grep-dctrl/">grep-dctrl</a></code>(1) </p>
<h2>Index</h2>
