---
title: "stringprep_strerror(3)"
name: "stringprep_strerror"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stringprep_strerror/"
description: "stringprep_strerror – API function"
---

<p>stringprep_strerror &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stringprep.h&gt;
const char *stringprep_strerror(Stringprep_rc rc);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>Stringprep_rc rc</p>
<dd>a <code>Stringprep_rc</code> return code.</dl>
<h2>Description</h2>
<p>Convert a return code integer to a text string. This string can be used to output a diagnostic message to the user.</p>
<h2>Stringprep_Ok</h2>
<p>Successful operation. This value is guaranteed to always be zero, the remaining ones are only guaranteed to hold non-zero values, for logical comparison purposes.</p>
<h2>Stringprep_Contains_Unassigned</h2>
<p>String contain unassigned Unicode code points, which is forbidden by the profile.</p>
<h2>Stringprep_Contains_Prohibited</h2>
<p>String contain code points prohibited by the profile.</p>
<h2>Stringprep_Bidi_Both_L_And_Ral</h2>
<p>String contain code points with conflicting bidirection category.</p>
<h2>Stringprep_Bidi_Leadtrail_Not_Ral</h2>
<p>Leading and trailing character in string not of proper bidirectional category.</p>
<h2>Stringprep_Bidi_Contains_Prohibited</h2>
<p>Contains prohibited code points detected by bidirectional code.</p>
<h2>Stringprep_Too_Small_Buffer</h2>
<p>Buffer handed to function was too small. This usually indicate a problem in the calling application.</p>
<h2>Stringprep_Profile_Error</h2>
<p>The stringprep profile was inconsistent. This usually indicate an internal error in the library.</p>
<h2>Stringprep_Flag_Error</h2>
<p>The supplied flag conflicted with profile. This usually indicate a problem in the calling application.</p>
<h2>Stringprep_Unknown_Profile</h2>
<p>The supplied profile name was not known to the library.</p>
<h2>Stringprep_Nfkc_Failed</h2>
<p>The Unicode NFKC operation failed. This usually indicate an internal error in the library.</p>
<h2>Stringprep_Malloc_Error</h2>
<p>The <code>malloc()</code> was out of memory. This is usually a fatal error.</p>
<h2>Return Value</h2>
<p>Returns a pointer to a statically allocated string containing a description of the error with the return code <i>rc</i>.</p>
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
