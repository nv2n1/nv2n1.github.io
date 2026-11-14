---
title: "globus_libc_contact_string_to_ints(3)"
name: "globus_libc_contact_string_to_ints"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_libc_contact_string_to_ints/"
description: "globus_libc.h –"
---

<h2 class="name">NAME</h2>
<p> globus_libc.h &#8211; </p>
<p> Thread-safe libc macros, function prototypes.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_common_include.h&#8217;<br />
 #include &#8216;globus_thread.h&#8217; </p>
<h3>Functions</h3>
<p> char * <code>globus_libc_join</code> (const char **array, int count) </p>
<p> <code>globus_result_t</code> <code>globus_libc_contact_string_to_ints</code> (const char *contact_string, int *host, int *count, unsigned short *port) </p>
<h2>Detailed Description</h2>
<p> Thread-safe libc macros, function prototypes. </p>
<h2>Function Documentation</h2>
<h3><code>globus_result_t</code> globus_libc_contact_string_to_ints (const char *contact_string, int *host, int *count, unsigned short *port)</h3>
<p> convert a numeric contact string to an array of ints </p>
<p> (port is optional and may be NULL. 0 will be passed back if no port is found) host needs to have room for at least 16 ints count will be passed back. 4 for ipv4, 16 for ipv6</p>
<h3>char* globus_libc_join (const char **array, intcount)</h3>
<p> create a new string from all of the strings in array </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>array</i> an array of strings to concatenate (null entries are skipped)<br />
 <i>count</i> length of array</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
