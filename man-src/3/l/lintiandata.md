---
title: "lintiandata(3)"
name: "lintiandata"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiandata/"
description: "Lintian::Data – Lintian interface to query lists of keywords"
---

<p>Lintian::Data &#8211; Lintian interface to query lists of keywords </p>
<h2>Synopsis</h2>
<pre> my $keyword;
 my $list = Lintian::Data-&gt;new('type');
 if ($list-&gt;known($keyword)) {
 # do something ...
 }
 my $hash = Lintian::Data-&gt;new('another-type', qr{\s++});
 if ($hash-&gt;value($keyword) &gt; 1) {
 # do something ...
 }
 if ($list-&gt;value($keyword) &gt; 1) {
 # do something ...
 }
 my @keywords = $list-&gt;all;
 if ($list-&gt;matches_any($keyword)) {
 # do something ...
 }</pre>
<h2>Description</h2>
<p>Lintian::Data provides a way of loading a list of keywords or key/value pairs from a file in the Lintian root and then querying that list. The lists are stored in the <i>data</i> directory of the Lintian root and consist of one keyword or key/value pair per line. Blank lines and lines beginning with <tt>&quot;#&quot;</tt> are ignored. Leading and trailing whitespace is stripped. </p>
<p> If requested, the lines are split into key/value pairs with a given separator regular expression. Otherwise, keywords are taken verbatim as they are listed in the file and may include spaces. </p>
<p> This module allows lists such as menu sections, doc-base sections, obsolete packages, package fields, and so forth to be stored in simple, easily editable files. </p>
<p> <font SIZE="-1">NB:</font> By default Lintian::Data is lazy and defers loading of the data file until it is actually needed.</p>
<h3>Interface for the <font SIZE="-1">CODE</font> argument</h3>
<p>This section describes the interface between for the <font SIZE="-1">CODE</font> argument for the class method new. </p>
<p> The sub will be called once for each key/pair with three arguments, <font SIZE="-1">KEY, VALUE</font> and <font SIZE="-1">CURVALUE.</font> The first two are the key/value pair parsed from the data file and <font SIZE="-1">CURVALUE</font> is current value associated with the key. <font SIZE="-1">CURVALUE</font> will be <tt>&quot;undef&quot;</tt> the first time the sub is called with that <font SIZE="-1">KEY</font> argument. </p>
<p> The sub can then modify <font SIZE="-1">VALUE</font> in some way and return the new value for that <font SIZE="-1">KEY.</font> If <font SIZE="-1">CURVALUE</font> is not <tt>&quot;undef&quot;</tt>, the sub may return <tt>&quot;undef&quot;</tt> to indicate that the current value should still be used. It is not permissible for the sub to return <tt>&quot;undef&quot;</tt> if <font SIZE="-1">CURVALUE</font> is <tt>&quot;undef&quot;</tt>. </p>
<p> Where Perl semantics allow it, the sub can modify <font SIZE="-1">CURVALUE</font> and the changes will be reflected in the result. As an example, if <font SIZE="-1">CURVALUE</font> is a hashref, new keys can be inserted etc.</p>
<h2>Class Methods</h2>
<dl COMPACT>
<dt>new(<font SIZE="-1">TYPE</font> [,SEPARATOR[, <font SIZE="-1">CODE</font>]])</p>
<dd>Creates a new Lintian::Data object for the given <font SIZE="-1">TYPE.</font> <font SIZE="-1">TYPE</font> is a partial path relative to the <i>data</i> directory and should correspond to a file in that directory. The contents of that file will be loaded into memory and returned as part of the newly created object. On error, <code>new()</code> throws an exception. </p>
<p> If <font SIZE="-1">SEPARATOR</font> is given, it will be used as a regular expression for splitting the lines into key/value pairs. </p>
<p> If <font SIZE="-1">CODE</font> is also given, it is assumed to be a sub that will pre-process the key/value pairs. See the &#8220;Interface for the <font SIZE="-1">CODE</font> argument&#8221; above. </p>
<p> A given file will only be loaded once. If <code>new()</code> is called again with the same <font SIZE="-1">TYPE</font> argument, the data previously loaded will be reused, avoiding multiple file reads.</p>
<dt>set_vendor(<font SIZE="-1">PROFILE</font>)</p>
<dd>Specifies vendor profile. It must be set before the first data file is loaded.</dl>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt><code>all()</code></p>
<dd>Returns all keywords listed in the data file as a list in original order. In a scalar context, returns the number of keywords.</p>
<dt>matches_any(KEYWORD[, <font SIZE="-1">MODIFIERS</font>])</p>
<dd>Returns true if <font SIZE="-1">KEYWORD</font> matches any regular expression listed in the data file. The optional <font SIZE="-1">MODIFIERS</font> serve as modifiers on all regexes.</p>
<dt>known(<font SIZE="-1">KEYWORD</font>)</p>
<dd>Returns true if <font SIZE="-1">KEYWORD</font> was listed in the data file represented by this Lintian::Data instance and false otherwise.</p>
<dt>value(<font SIZE="-1">KEYWORD</font>)</p>
<dd>Returns the value attached to <font SIZE="-1">KEYWORD</font> if it was listed in the data file represented by this Lintian::Data instance and the undefined value otherwise. If <font SIZE="-1">SEPARATOR</font> was not given, the value will &#8216;1&#8217;.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>no data type specified</p>
<dd><code>new()</code> was called without a <font SIZE="-1">TYPE</font> argument.</p>
<dt>unknown data type %s</p>
<dd>The <font SIZE="-1">TYPE</font> argument to <code>new()</code> did not correspond to a file in the <i>data</i> directory of the Lintian root.</p>
<dt>undefined value for %s (type: %s)</p>
<dd>The <font SIZE="-1">CODE</font> argument return undef for the <font SIZE="-1">KEY</font> and no previous value for that <font SIZE="-1">KEY</font> was available.</dl>
<h2>Files</h2>
<dl COMPACT>
<dt>LINTIAN_INCLUDE_DIR/data</p>
<dd>The files loaded by this module must be located in this directory. Relative paths containing a <tt>&quot;/&quot;</tt> are permitted, so files may be organized in subdirectories in this directory. </p>
<p> Note that lintian supports multiple LINTIAN_INCLUDE_DIRs.</dl>
<h2>Author</h2>
<p>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1), &lt;<a rel="nofollow" href="https://lintian.debian.org/manual/section-2.6.html">https://lintian.debian.org/manual/section-2.6.html</a>&gt;</p>
