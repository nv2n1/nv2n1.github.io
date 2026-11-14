---
title: "stringprep_check_version(3)"
name: "stringprep_check_version"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stringprep_check_version/"
description: "stringprep_check_version – API function"
---

<p>stringprep_check_version &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stringprep.h&gt;
const char *stringprep_check_version(const char *req_version);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>const char * req_version</p>
<dd>Required version number, or NULL.</dl>
<h2>Description</h2>
<p>Check that the version of the library is at minimum the requested one and return the version string; return NULL if the condition is not satisfied. If a NULL is passed to this function, no check is done, but the version string is simply returned. </p>
<p> See <code>STRINGPREP_VERSION</code> for a suitable <i>req_version</i> string.</p>
<h2>Return Value</h2>
<p>Version string of run-time library, or NULL if the run-time library does not meet the required version number.</p>
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
