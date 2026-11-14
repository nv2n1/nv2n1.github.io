---
title: "getdns_dict(3)"
name: "getdns_dict"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_dict/"
description: "getdns_dict, getdns_dict_create, getdns_dict_create_with_extended_memory_functions, getdns_dict_create_with_memory_functions, getdns_dict_destroy — getdns dict create and destroy routines"
---

<h2 class="name">NAME</h2>
<p> <code>getdns_dict, </code> <code>getdns_dict_create, </code> <code>getdns_dict_create_with_extended_memory_functions, </code> <code>getdns_dict_create_with_memory_functions, </code> <code>getdns_dict_destroy </code> &#8212; getdns dict create and destroy routines</p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_dict *<br />
 <code>getdns_dict_create</code> () </p>
<p> getdns_dict *<br />
 <code>getdns_dict_create_with_extended_memory_functions</code></p>
<dl>
<dt>
<dd> (void *userarg,<br />
 void *(*malloc)(void *userarg, size_t sz),<br />
 void *(*realloc)(void *userarg, void *buf, size_t sz),<br />
 void (*free)(void *userarg, void *buf)</dl>
<p> getdns_dict *<br />
 <code>getdns_dict_create_with_memory_functions</code></p>
<dl>
<dt>
<dd> (void *(*malloc)(size_t sz),<br />
 void *(*realloc)(void *buf, size_t sz),<br />
 void (*free)(void *buf)</dl>
<p> void<br />
 <code>getdns_dict_destroy</code> (getdns_dict *this_dict) </p>
<h2>DESCRIPTION</h2>
<p> The getdns_dict type is used to manage name/value pairs in which the names are strings and the data types of the values are heterogeneous and include</p>
<dl>
<dt>
<dd>
 getdns_bindata<br />
 getdns_dict<br />
 getdns_list<br />
 uint32_t</dl>
<p> The destroy function performs a &quot;deep&quot; destroy, freeing storage for all of the members of the dictionary before destroying the dictionary. There are a number of helper functions that provide access to the dictionary object, see their respective man pages. </p>
<p> <i>userarg</i> pass this argument to the user specified memory management functions for operations on lists created using extended memory functions </p>
<p> <i>this_dict</i> the dictionary to destroy </p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion the getdns_dict_create function returns a valid (empty) dictionary structure that should be freed via a call to getdns_dict_destroy. If a parameter in invalid or in the event of some error getdns_dict_create returns NULL. </p>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3), <code><a href="/docs/linux/man/3-getdns_dict_get/">getdns_dict_get</a></code>(3), <code><a href="/docs/linux/man/3-getdns_dict_set/">getdns_dict_set</a></code>(3), <code><a href="/docs/linux/man/3-getdns_list/">getdns_list</a></code>(3), <code><a href="/docs/linux/man/3-getdns_pretty_print_dict/">getdns_pretty_print_dict</a></code>(3). </p>
<h2>Index</h2>
