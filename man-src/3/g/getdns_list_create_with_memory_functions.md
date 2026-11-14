---
title: "getdns_list_create_with_memory_functions(3)"
name: "getdns_list_create_with_memory_functions"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_list_create_with_memory_functions/"
description: "getdns_list, getdns_list_create, getdns_list_create_with_extended_memory_functions, getdns_list_create_with_memory_functions, getdns_list_destroy — getdns list create and destroy routines"
---

<h2 class="name">NAME</h2>
<p> <code>getdns_list, </code> <code>getdns_list_create, </code> <code>getdns_list_create_with_extended_memory_functions, </code> <code>getdns_list_create_with_memory_functions, </code> <code>getdns_list_destroy </code> &#8212; getdns list create and destroy routines</p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_list *<br />
 <code>getdns_list_create</code> () </p>
<p> getdns_list *<br />
 <code>getdns_list_create_with_extended_memory_functions</code></p>
<dl>
<dt>
<dd> (void *userarg,<br />
 void *(*malloc)(void *userarg, size_t sz),<br />
 void *(*realloc)(void *userarg, void *buf, size_t sz),<br />
 void (*free)(void *userarg, void *buf)</dl>
<p> getdns_list *<br />
 <code>getdns_list_create_with_memory_functions</code></p>
<dl>
<dt>
<dd> (void *userarg,<br />
 void *(*malloc)(size_t sz),<br />
 void *(*realloc)(void *buf, size_t sz),<br />
 void (*free)(void *buf)</dl>
<p> void<br />
 <code>getdns_list_destroy</code> (getdns_list *this_dict) </p>
<h2>DESCRIPTION</h2>
<p> The getdns_list type is used to manage heterogeneous indexed lists name/value pairs in which the data types of the values include</p>
<dl>
<dt>
<dd>
 getdns_bindata<br />
 getdns_dict<br />
 getdns_list<br />
 uint32_t</dl>
<p> The destroy function performs a &quot;deep&quot; destroy, freeing storage for all of the members of the list before destroying the list. There are a number of helper functions that provide access to the list object, see their respective man pages. </p>
<p> <i>userarg</i> pass this argument to the user specified memory management functions for operations on lists created using extended memory functions </p>
<p> <i>this_list</i> the list to destroy </p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion the getdns_list_create function returns a valid (empty) list structure that should be freed via a call to getdns_list_destroy. If a parameter in invalid or in the event of some error getdns_list_create returns NULL. </p>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3), <code><a href="/docs/linux/man/3-getdns_dict/">getdns_dict</a></code>(3), <code><a href="/docs/linux/man/3-getdns_list_get/">getdns_list_get</a></code>(3), <code><a href="/docs/linux/man/3-getdns_list_set/">getdns_list_set</a></code>(3) </p>
<h2>Index</h2>
