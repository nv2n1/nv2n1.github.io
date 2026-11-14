---
title: "getdns_dict_set_list(3)"
name: "getdns_dict_set_list"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_dict_set_list/"
description: "getdns_dict_set, getdns_dict_set_bindata, getdns_dict_set_dict, getdns_dict_set_int, getdns_dict_set_list, — set a value by name in a getdns dict"
---

<h2>NAME</h2>
<p> <code>getdns_dict_set, </code> <code>getdns_dict_set_bindata, </code> <code>getdns_dict_set_dict, </code> <code>getdns_dict_set_int, </code> <code>getdns_dict_set_list, </code> &#8212; set a value by name in a getdns dict </p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_return_t<br />
 <code>getdns_dict_set_bindata</code> (getdns_dict *this_dict,</p>
<dl>
<dt>
<dd> char *name,<br />
 getdns_bindata *child_bindata)</dl>
<p> getdns_return_t<br />
 <code>getdns_dict_set_dict</code> (getdns_dict *this_dict,</p>
<dl>
<dt>
<dd> char *name,<br />
 getdns_dict *child_dict)</dl>
<p> getdns_return_t<br />
 <code>getdns_dict_set_int</code> (getdns_dict *this_dict,</p>
<dl>
<dt>
<dd> char *name,<br />
 uint32_t child_uint32_t)</dl>
<p> getdns_return_t<br />
 <code>getdns_dict_set_list</code> (getdns_dict *this_dict,</p>
<dl>
<dt>
<dd> char *name,<br />
 getdns_list *child_list)</dl>
<h2>DESCRIPTION</h2>
<p> The getdns_dict type is used to manage name/value pairs in which the names are strings and the data types of the values are heterogeneous and include</p>
<dl>
<dt>
<dd>
 getdns_bindata<br />
 getdns_dict<br />
 getdns_list<br />
 uint32_t</dl>
<p> <i>this_dict</i> the dictionary in which to add/update the name/value pair </p>
<p> <i>name</i> the name whose associated value is to be set. If the name exists in the dictionary the value associated with that name is replaced, if the name does not exist in the dictionary a new item is added to the dictionary. </p>
<p> <i>child_bindata</i> <i>child_dict</i> <i>child_list</i> <i>child_uint32</i> value to assign the name </p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion the functions return <code>GETDNS_RETURN_GOOD</code> , otherwise the following error values are returned: </p>
<p> <code>GETDNS_RETURN_GENERIC_ERROR</code> if this_dict is not a valid dictionary </p>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3), <code><a href="/docs/linux/man/3-getdns_address/">getdns_address</a></code>(3), <code><a href="/docs/linux/man/3-getdns_dict/">getdns_dict</a></code>(3), <code><a href="/docs/linux/man/3-getdns_dict_get/">getdns_dict_get</a></code>(3), <code><a href="/docs/linux/man/3-getdns_general/">getdns_general</a></code>(3), <code><a href="/docs/linux/man/3-getdns_hostname/">getdns_hostname</a></code>(3), <code><a href="/docs/linux/man/3-getdns_service/">getdns_service</a></code>(3) </p>
<h2>Index</h2>
