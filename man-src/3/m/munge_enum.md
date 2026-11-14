---
title: "munge_enum(3)"
name: "munge_enum"
section: "3"
letter: "m"
url: "/docs/linux/man/3-munge_enum/"
description: "munge_enum_is_valid, munge_enum_int_to_str, munge_enum_str_to_int – MUNGE enumeration functions"
---

<p>munge_enum_is_valid, munge_enum_int_to_str, munge_enum_str_to_int &#8211; MUNGE enumeration functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;munge.h&gt;</code>
<code>int munge_enum_is_valid (munge_enum_t </code><i>type</i><code>, int </code><i>val</i><code>);</code>
<code>const char * munge_enum_int_to_str (munge_enum_t </code><i>type</i><code>, int </code><i>val</i><code>);</code>
<code>int munge_enum_str_to_int (munge_enum_t </code><i>type</i><code>, const char *</code><i>str</i><code>);</code>
<code>cc `pkg-config --cflags --libs munge` -o foo foo.c</code></pre>
<h2>Description</h2>
<p>The <code>munge_enum_is_valid</code>() function checks if the given value <i>val</i> is a valid MUNGE enumeration of the specified type <i>type</i> in the software configuration as currently compiled. Some enumerations correspond to options that can only be enabled at compile-time. </p>
<p> The <code>munge_enum_int_to_str</code>() function converts the MUNGE enumeration <i>val</i> of the specified type <i>type</i> into a text string. </p>
<p> The <code>munge_enum_str_to_int</code>() function converts the NUL-terminated case-insensitive string <i>str</i> into the corresponding MUNGE enumeration of the specified type <i>type</i>. </p>
<h2>Return Value</h2>
<p>The <code>munge_enum_is_valid</code>() function returns non-zero if the given value <i>val</i> is a valid enumeration. </p>
<p> The <code>munge_enum_int_to_str</code>() function returns a NUL-terminated constant text string, or NULL on error; this string should not be freed or modified by the caller. </p>
<p> The <code>munge_enum_str_to_int</code>() function returns a MUNGE enumeration on success (i.e., &gt;= 0), or -1 on error. </p>
<h2>Enum Types</h2>
<p>The following enumeration types can be specified.</p>
<dl COMPACT>
<dt><code>MUNGE_ENUM_CIPHER</code></p>
<dd>Specify enumerations for the available cipher types.</p>
<dt><code>MUNGE_ENUM_MAC</code></p>
<dd>Specify enumerations for the available MAC types.</p>
<dt><code>MUNGE_ENUM_ZIP</code></p>
<dd>Specify enumerations for the available compression types. </p>
</dl>
<h2>Errors</h2>
<p>Refer to <code><a href="/docs/linux/man/3-munge/">munge</a></code>(3) for a complete list of errors. </p>
<h2>Example</h2>
<p>The following example program illustrates how a list of available cipher types can be queried. </p>
<pre>#include &lt;stdio.h&gt; /* for printf() */
#include &lt;stdlib.h&gt; /* for exit() */
#include &lt;munge.h&gt;
int
main (int argc, char *argv[])
{
 int i;
 const char *p;
 munge_enum_t t = MUNGE_ENUM_CIPHER;
 for (i = 0; (p = munge_enum_int_to_str (t, i)) != NULL; i++) {
 if (munge_enum_is_valid (t, i)) {
 printf (&quot;%2d = %s
&quot;, i, p);
 }
 }
 exit (0);
}</pre>
<h2>Author</h2>
<p>Chris Dunlap &lt;cdunlap [at] llnl.gov&gt; </p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2013 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2002-2007 The Regents of the University of California. </p>
<p> MUNGE is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> Additionally for the MUNGE library (libmunge), you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-munge/">munge</a></code>(1), <code><a href="/docs/linux/man/1-remunge/">remunge</a></code>(1), <code><a href="/docs/linux/man/1-unmunge/">unmunge</a></code>(1), <code><a href="/docs/linux/man/3-munge/">munge</a></code>(3), <code><a href="/docs/linux/man/3-munge_ctx/">munge_ctx</a></code>(3), <code><a href="/docs/linux/man/7-munge/">munge</a></code>(7), <code><a href="/docs/linux/man/8-munged/">munged</a></code>(8). </p>
<p> <code><a rel="nofollow" href="https://munge.googlecode.com/">https://munge.googlecode.com/</a></code></p>
