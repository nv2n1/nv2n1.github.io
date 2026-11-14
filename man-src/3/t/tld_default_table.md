---
title: "tld_default_table(3)"
name: "tld_default_table"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tld_default_table/"
description: "tld_default_table – API function"
---

<p>tld_default_table &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tld.h&gt;
const Tld_table *tld_default_table(const char *tld, const Tld_table **overrides);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>const char * tld</p>
<dd>TLD name (e.g. &quot;com&quot;) as zero terminated ASCII byte string.</p>
<dt>const Tld_table ** overrides</p>
<dd>Additional zero terminated array of <code>Tld_table</code> info-structures for TLDs, or <code>NULL</code> to only use library deault tables.</dl>
<h2>Description</h2>
<p>Get the TLD table for a named TLD, using the internal defaults, possibly overrided by the (optional) supplied tables.</p>
<h2>Return Value</h2>
<p>Return structure corresponding to TLD <i>tld_str</i>, first looking through <i>overrides</i> then thru built-in list, or <code>NULL</code> if no such structure found.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-libidn [at] gnu.org&gt;. GNU Libidn home page: <a rel="nofollow" href="http://www.gnu.org/software/libidn/">http://www.gnu.org/software/libidn/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2002-2013 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>See Also</h2>
<p>The full documentation for <code>libidn</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>libidn</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info libidn</code></dl>
<p> should give you access to the complete manual. </p>
