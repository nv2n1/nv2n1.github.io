---
title: "stringprep_4i(3)"
name: "stringprep_4i"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stringprep_4i/"
description: "stringprep_4i – API function"
---

<p>stringprep_4i &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stringprep.h&gt;
int stringprep_4i(uint32_t *ucs4, size_t *len, size_t maxucs4len, Stringprep_profile_flags flags, const Stringprep_profile *profile);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>uint32_t * ucs4</p>
<dd>input/output array with string to prepare.</p>
<dt>size_t * len</p>
<dd>on input, length of input array with Unicode code points, on exit, length of output array with Unicode code points.</p>
<dt>size_t maxucs4len</p>
<dd>maximum length of input/output array.</p>
<dt>Stringprep_profile_flags flags</p>
<dd>a <code>Stringprep_profile_flags</code> value, or 0.</p>
<dt>const Stringprep_profile * profile</p>
<dd>pointer to <code>Stringprep_profile</code> to use.</dl>
<h2>Description</h2>
<p>Prepare the input UCS-4 string according to the stringprep profile, and write back the result to the input string. </p>
<p> The input is not required to be zero terminated (<i>ucs4</i>[<i>len</i>] = 0). The output will not be zero terminated unless <i>ucs4</i>[<i>len</i>] = 0. Instead, see <code>stringprep_4zi()</code> if your input is zero terminated or if you want the output to be. </p>
<p> Since the stringprep operation can expand the string, <i>maxucs4len</i> indicate how large the buffer holding the string is. This function will not read or write to code points outside that size. </p>
<p> The <i>flags</i> are one of <code>Stringprep_profile_flags</code> values, or 0. </p>
<p> The <i>profile</i> contain the <code>Stringprep_profile</code> instructions to perform. Your application can define new profiles, possibly re-using the generic stringprep tables that always will be part of the library, or use one of the currently supported profiles.</p>
<h2>Return Value</h2>
<p>Returns <code>STRINGPREP_OK</code> iff successful, or an <code>Stringprep_rc</code> error code.</p>
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
