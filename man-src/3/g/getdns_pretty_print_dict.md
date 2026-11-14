---
title: "getdns_pretty_print_dict(3)"
name: "getdns_pretty_print_dict"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_pretty_print_dict/"
description: "getdns_pretty_print_dict — return a string representation of a getdns dict"
---

<h2>NAME</h2>
<p> <code>getdns_pretty_print_dict</code> &#8212; return a string representation of a getdns dict </p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_list *<br />
 <code>getdns_pretty_print_dict</code> (const getdns_dict *this_dict) </p>
<h2>DESCRIPTION</h2>
<p> Helper function that returns a string of nicely formatted data including all of the elements in the dict. </p>
<dl>
<dt> <i>this_dict</i></p>
<dd>the dictionary to render as a string </p>
<dt></dl>
<h2>RETURN VALUES</h2>
<dd>Returns a string that the calling function must free (it is allocated using the system allocator not the user defined allocator). Returns NULL if there is an error. </p>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getdns_dict/">getdns_dict</a></code>(3) <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3) </p>
<h2>Index</h2>
