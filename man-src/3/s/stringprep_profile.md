---
title: "stringprep_profile(3)"
name: "stringprep_profile"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stringprep_profile/"
description: "stringprep_profile – API function"
---

<p>stringprep_profile &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stringprep.h&gt;
int stringprep_profile(const char *in, char **out, const char *profile, Stringprep_profile_flags flags);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>const char * in</p>
<dd>input array with UTF-8 string to prepare.</p>
<dt>char ** out</p>
<dd>output variable with pointer to newly allocate string.</p>
<dt>const char * profile</p>
<dd>name of stringprep profile to use.</p>
<dt>Stringprep_profile_flags flags</p>
<dd>a <code>Stringprep_profile_flags</code> value, or 0.</dl>
<h2>Description</h2>
<p>Prepare the input zero terminated UTF-8 string according to the stringprep profile, and return the result in a newly allocated variable. </p>
<p> Note that you must convert strings entered in the systems locale into UTF-8 before using this function, see <code>stringprep_locale_to_utf8()</code>. </p>
<p> The output <i>out</i> variable must be deallocated by the caller. </p>
<p> The <i>flags</i> are one of <code>Stringprep_profile_flags</code> values, or 0. </p>
<p> The <i>profile</i> specifies the name of the stringprep profile to use. It must be one of the internally supported stringprep profiles.</p>
<h2>Return Value</h2>
<p>Returns <code>STRINGPREP_OK</code> iff successful, or an error code.</p>
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
