---
title: "genpng(1)"
name: "genpng"
section: "1"
letter: "g"
url: "/docs/linux/man/1-genpng/"
description: "genpng – Generate an overview image from a source file"
---

<h2>NAME</h2>
<p> genpng &#8211; Generate an overview image from a source file</p>
<h2>SYNOPSIS</h2>
<p> <code>genpng</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>-v</code>|<code>&#8211;version</code>]</p>
<dl>
<dt>
<dd>
 [<code>-t</code>|<code>&#8211;tab-size</code> <i>tabsize</i>] [<code>-w</code>|<code>&#8211;width</code> <i>width</i>]<br />
 [<code>-o</code>|<code>&#8211;output-filename</code> <i>output-filename</i>]<br />
 <i>source-file</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>genpng</code> creates an overview image for a given source code file of either plain text or .gcov file format. </p>
<p> Note that the <i>GD.pm</i> Perl module has to be installed for this script to work (it may be obtained from <i><a rel="nofollow" href="http://www.cpan.org">http://www.cpan.org</a></i>). </p>
<p> Note also that <code>genpng</code> is called from within <code>genhtml</code> so that there is usually no need to call it directly. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code><br />
 <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text, then exit.</dl>
<p> <code>-v</code><br />
 <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version number, then exit.</dl>
<p> <code>-t </code><i>tab-size</i><br />
 <code>&#8211;tab-size </code><i>tab-size</i></p>
<dl>
<dt>
<dd> Use <i>tab-size</i> spaces in place of tab. </p>
<p> All occurrences of tabulator signs in the source code file will be replaced by the number of spaces defined by <i>tab-size</i> (default is 4).</dl>
<p> <code>-w </code><i>width</i><br />
 <code>&#8211;width </code><i>width</i></p>
<dl>
<dt>
<dd> Set width of output image to <i>width</i> pixel. </p>
<p> The resulting image will be exactly <i>width</i> pixel wide (default is 80). </p>
<p> Note that source code lines which are longer than <i>width</i> will be truncated.</dl>
<p> <code>-o </code><i>filename</i><br />
 <code>&#8211;output-filename </code><i>filename</i></p>
<dl>
<dt>
<dd> Write image to <i>filename</i>. </p>
<p> Specify a name for the resulting image file (default is <i>source-file</i>.png).</dl>
<h2>AUTHOR</h2>
<p> Peter Oberparleiter &lt;Peter.Oberparleiter [at] de.ibm.com&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lcov/">lcov</a></code>(1), <code><a href="/docs/linux/man/1-genhtml/">genhtml</a></code>(1), <code><a href="/docs/linux/man/1-geninfo/">geninfo</a></code>(1), <code><a href="/docs/linux/man/1-gendesc/">gendesc</a></code>(1), <code><a href="/docs/linux/man/1-gcov/">gcov</a></code>(1) </p>
<h2>Index</h2>
