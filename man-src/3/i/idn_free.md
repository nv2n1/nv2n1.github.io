---
title: "idn_free(3)"
name: "idn_free"
section: "3"
letter: "i"
url: "/docs/linux/man/3-idn_free/"
description: "idn_free – API function"
---

<h2>NAME</h2>
<p> idn_free &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;idn.h&gt;</code> </p>
<p> <code>void idn_free(void * </code><i>ptr</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>void * ptr</p>
<dd> memory region to deallocate, or <code>NULL</code>.</dl>
<h2>DESCRIPTION</h2>
<p> Deallocates memory region by calling <code>free()</code>. If <i>ptr</i> is <code>NULL</code> no operation is performed. </p>
<p> Normally applications de-allocate strings allocated by libidn by calling <code>free()</code> directly. Under Windows, different parts of the same application may use different heap memory, and then it is important to deallocate memory allocated within the same module that allocated it. This function makes that possible.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-libidn [at] gnu.org&gt;. GNU Libidn home page: <a rel="nofollow" href="http://www.gnu.org/software/libidn/">http://www.gnu.org/software/libidn/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2013 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>libidn</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>libidn</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info libidn</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
