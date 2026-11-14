---
title: "getdns_list_set_int(3)"
name: "getdns_list_set_int"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_list_set_int/"
description: "getdns_list_set, getdns_list_set_bindata, getdns_list_set_dict, getdns_list_set_int, getdns_list_set_list, — set a value by index from a getdns list"
---

<h2>NAME</h2>
<p> <code>getdns_list_set, </code> <code>getdns_list_set_bindata, </code> <code>getdns_list_set_dict, </code> <code>getdns_list_set_int, </code> <code>getdns_list_set_list, </code> &#8212; set a value by index from a getdns list </p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_return_t<br />
 <code>getdns_list_set_bindata</code> (getdns_list *this_list,</p>
<dl>
<dt>
<dd> size_t index,<br />
 getdns_bindata *child_bindata)</dl>
<p> getdns_return_t<br />
 <code>getdns_list_set_dict</code> (getdns_list *this_list,</p>
<dl>
<dt>
<dd> size_t index,<br />
 getdns_dict *child_dict)</dl>
<p> getdns_return_t<br />
 <code>getdns_list_set_int</code> (getdns_list *this_list,</p>
<dl>
<dt>
<dd> size_t index,<br />
 uint32_t child_uint32_t)</dl>
<p> getdns_return_t<br />
 <code>getdns_list_set_list</code> (getdns_list *this_list,</p>
<dl>
<dt>
<dd> size_t index,<br />
 getdns_list *child_list)</dl>
<h2>DESCRIPTION</h2>
<p> The getdns_list type is used to manage a heterogeneous indexed list of values that include:</p>
<dl>
<dt>
<dd>
 getdns_bindata<br />
 getdns_dict<br />
 getdns_list<br />
 uint32_t</dl>
<p> <i>this_list</i> the list in which to add/update the indexed item </p>
<p> <i>index</i> the index whose associated value is to be set. If the index exists in the list the value associated with that index is replaced, if the index does not exist in the list a new item is added to the list at the specified index. </p>
<p> <i>child_bindata</i> <i>child_dict</i> <i>child_list</i> <i>child_uint32</i> value to assign the indexed element </p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion the functions return <code>GETDNS_RETURN_GOOD</code> , otherwise the following error values are returned: </p>
<p> <code>GETDNS_RETURN_NO_SUCH_LIST_ITEM</code> if the index is out of range </p>
<p> <code>GETDNS_RETURN_GENERIC_ERROR</code> if this_list is not a valid list </p>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3), <code><a href="/docs/linux/man/3-getdns_address/">getdns_address</a></code>(3), <code><a href="/docs/linux/man/3-getdns_list/">getdns_list</a></code>(3), <code><a href="/docs/linux/man/3-getdns_list_get/">getdns_list_get</a></code>(3), <code><a href="/docs/linux/man/3-getdns_general/">getdns_general</a></code>(3), <code><a href="/docs/linux/man/3-getdns_hostname/">getdns_hostname</a></code>(3), <code><a href="/docs/linux/man/3-getdns_service/">getdns_service</a></code>(3), </p>
<h2>Index</h2>
