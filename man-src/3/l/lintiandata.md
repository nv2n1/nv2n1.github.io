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
<p> NB: By default Lintian::Data is lazy and defers loading of the data file until it is actually needed.</p>
<h3>Interface for the CODE argument</h3>
<p>This section describes the interface between for the CODE argument for the class method new. </p>
<p> The sub will be called once for each key/pair with three arguments, KEY, VALUE and CURVALUE. The first two are the key/value pair parsed from the data file and CURVALUE is current value associated with the key. CURVALUE will be <tt>&quot;undef&quot;</tt> the first time the sub is called with that KEY argument. </p>
<p> The sub can then modify VALUE in some way and return the new value for that KEY. If CURVALUE is not <tt>&quot;undef&quot;</tt>, the sub may return <tt>&quot;undef&quot;</tt> to indicate that the current value should still be used. It is not permissible for the sub to return <tt>&quot;undef&quot;</tt> if CURVALUE is <tt>&quot;undef&quot;</tt>. </p>
<p> Where Perl semantics allow it, the sub can modify CURVALUE and the changes will be reflected in the result. As an example, if CURVALUE is a hashref, new keys can be inserted etc.</p>
<h2>Class Methods</h2>
<dl COMPACT>
<dt>new(TYPE [,SEPARATOR[, CODE]])</dt>
<dd>Creates a new Lintian::Data object for the given TYPE. TYPE is a partial path relative to the <i>data</i> directory and should correspond to a file in that directory. The contents of that file will be loaded into memory and returned as part of the newly created object. On error, <code>new()</code> throws an exception. </dd>
<p> If SEPARATOR is given, it will be used as a regular expression for splitting the lines into key/value pairs. </p>
<p> If CODE is also given, it is assumed to be a sub that will pre-process the key/value pairs. See the &#8220;Interface for the CODE argument&#8221; above. </p>
<p> A given file will only be loaded once. If <code>new()</code> is called again with the same TYPE argument, the data previously loaded will be reused, avoiding multiple file reads.</p>
<dt>set_vendor(PROFILE)</dt>
<dd>Specifies vendor profile. It must be set before the first data file is loaded.</dd></dl>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt><code>all()</code></dt>
<dd>Returns all keywords listed in the data file as a list in original order. In a scalar context, returns the number of keywords.</dd>
<dt>matches_any(KEYWORD[, MODIFIERS])</dt>
<dd>Returns true if KEYWORD matches any regular expression listed in the data file. The optional MODIFIERS serve as modifiers on all regexes.</dd>
<dt>known(KEYWORD)</dt>
<dd>Returns true if KEYWORD was listed in the data file represented by this Lintian::Data instance and false otherwise.</dd>
<dt>value(KEYWORD)</dt>
<dd>Returns the value attached to KEYWORD if it was listed in the data file represented by this Lintian::Data instance and the undefined value otherwise. If SEPARATOR was not given, the value will &#8216;1&#8217;.</dd></dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>no data type specified</dt>
<dd><code>new()</code> was called without a TYPE argument.</dd>
<dt>unknown data type %s</dt>
<dd>The TYPE argument to <code>new()</code> did not correspond to a file in the <i>data</i> directory of the Lintian root.</dd>
<dt>undefined value for %s (type: %s)</dt>
<dd>The CODE argument return undef for the KEY and no previous value for that KEY was available.</dd></dl>
<h2>Files</h2>
<dl COMPACT>
<dt>LINTIAN_INCLUDE_DIR/data</dt>
<dd>The files loaded by this module must be located in this directory. Relative paths containing a <tt>&quot;/&quot;</tt> are permitted, so files may be organized in subdirectories in this directory. </dd>
<p> Note that lintian supports multiple LINTIAN_INCLUDE_DIRs.</dl>
<h2>Author</h2>
<p>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1), &lt;<a rel="nofollow" href="https://lintian.debian.org/manual/section-2.6.html">https://lintian.debian.org/manual/section-2.6.html</a>&gt;</p>
</p>