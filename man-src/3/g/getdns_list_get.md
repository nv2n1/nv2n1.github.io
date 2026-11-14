---
title: "getdns_list_get(3)"
name: "getdns_list_get"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_list_get/"
description: "getdns_list_get, getdns_list_get_bindata, getdns_list_get_data_type, getdns_list_get_dict, getdns_list_get_length, getdns_list_get_list, getdns_list_get_int — get a value by index from a getdns list"
---

<h2>NAME</h2>
<p> <code>getdns_list_get, </code> <code>getdns_list_get_bindata, </code> <code>getdns_list_get_data_type, </code> <code>getdns_list_get_dict, </code> <code>getdns_list_get_length,</code> <code>getdns_list_get_list, </code> <code>getdns_list_get_int</code> &#8212; get a value by index from a getdns list </p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_return_t<br />
 <code>getdns_list_get_bindata</code> (getdns_list *this_list,</p>
<dl>
<dt>
<dd> size_t index,<br />
 getdns_bindata **answer)</dl>
<p> getdns_return_t<br />
 <code>getdns_list_get_data_type</code> (getdns_list *this_list,</p>
<dl>
<dt>
<dd> size_t index,<br />
 getdns_data_type *answer)</dl>
<p> getdns_return_t<br />
 <code>getdns_list_get_dict</code> (getdns_list *this_list,</p>
<dl>
<dt>
<dd> size_t index,<br />
 getdns_dict **answer)</dl>
<p> getdns_return_t<br />
 <code>getdns_list_get_length</code> (getdns_list *this_list,</p>
<dl>
<dt>
<dd> size_t *answer)</dl>
<p> getdns_return_t<br />
 <code>getdns_list_get_list</code> (getdns_list *this_list,</p>
<dl>
<dt>
<dd> size_t index,<br />
 getdns_list **answer)</dl>
<p> getdns_return_t<br />
 <code>getdns_list_get_int</code> (getdns_list *this_list,</p>
<dl>
<dt>
<dd> size_t index,<br />
 uint32_t *answer)</dl>
<h2>DESCRIPTION</h2>
<p> The getdns_list type is used to manage heterogeneous lists in which the objects are each one of the data types:</p>
<dl>
<dt>
<dd>
 getdns_bindata<br />
 getdns_dict<br />
 getdns_list<br />
 uint32_t</dl>
<p> <i>this_list</i> the list from which to retrieve the object </p>
<p> <i>index</i> the numeric index (0 based) of the item in the list you would like copied to answer </p>
<p> <i>answer</i> a copy of the object in the list is placed in answer, the caller is responsible for freeing the storage associated with that object by calling the appropriate destroy function. </p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion the functions return <code>GETDNS_RETURN_GOOD</code> , otherwise the following error values are returned: </p>
<p> <code>GETDNS_RETURN_GENERIC_ERROR</code> if this_list is not a valid list </p>
<p> <code>GETDNS_RETURN_NO_SUCH_LIST_ITEM</code> if index is out of range </p>
<p> <code>GETDNS_RETURN_WRONG_TYPE_REQUESTED</code> if the requested data type doesn&#8217;t match the contents of the indexed argument </p>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3), <code><a href="/docs/linux/man/3-getdns_address/">getdns_address</a></code>(3), <code><a href="/docs/linux/man/3-getdns_dict/">getdns_dict</a></code>(3), <code><a href="/docs/linux/man/3-getdns_general/">getdns_general</a></code>(3), <code><a href="/docs/linux/man/3-getdns_hostname/">getdns_hostname</a></code>(3), <code><a href="/docs/linux/man/3-getdns_service/">getdns_service</a></code>(3), </p>
<h2>Index</h2>
