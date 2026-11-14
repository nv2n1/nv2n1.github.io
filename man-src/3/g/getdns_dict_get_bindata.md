---
title: "getdns_dict_get_bindata(3)"
name: "getdns_dict_get_bindata"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_dict_get_bindata/"
description: "getdns_dict_get, getdns_dict_get_bindata, getdns_dict_get_data_type, getdns_dict_get_dict, getdns_dict_get_int, getdns_dict_get_list, getdns_dict_get_names — get value by name from a getdns dict"
---

<h2>NAME</h2>
<p> <code>getdns_dict_get, </code> <code>getdns_dict_get_bindata, </code> <code>getdns_dict_get_data_type, </code> <code>getdns_dict_get_dict, </code> <code>getdns_dict_get_int, </code> <code>getdns_dict_get_list, </code> <code>getdns_dict_get_names</code> &#8212; get value by name from a getdns dict </p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_return_t<br />
 <code>getdns_dict_get_bindata</code> (getdns_dict *this_dict,</p>
<dl>
<dt>
<dd> char *name,<br />
 getdns_bindata **answer)</dl>
<p> getdns_return_t<br />
 <code>getdns_dict_get_data_type</code> (getdns_dict *this_dict,</p>
<dl>
<dt>
<dd> char *name,<br />
 getdns_data_type *answer)</dl>
<p> getdns_return_t<br />
 <code>getdns_dict_get_dict</code> (getdns_dict *this_dict,</p>
<dl>
<dt>
<dd> char *name,<br />
 getdns_dict **answer)</dl>
<p> getdns_return_t<br />
 <code>getdns_dict_get_int</code> (getdns_dict *this_dict,</p>
<dl>
<dt>
<dd> char *name,<br />
 uint32_t *answer)</dl>
<p> getdns_return_t<br />
 <code>getdns_dict_get_list</code> (getdns_dict *this_dict,</p>
<dl>
<dt>
<dd> char *name,<br />
 getdns_list **answer)</dl>
<p> getdns_return_t<br />
 <code>getdns_dict_get_names</code> (getdns_dict *this_dict,</p>
<dl>
<dt>
<dd> getdns_list **answer)</dl>
<h2>DESCRIPTION</h2>
<p> The getdns_dict type is used to manage name/value pairs in which the names are strings and the data types of the values are heterogeneous and include</p>
<dl>
<dt>
<dd>
 getdns_bindata<br />
 getdns_dict<br />
 getdns_list<br />
 uint32_t</dl>
<p> <i>this_dict</i> the dictionary from which to retrieve the list of names </p>
<p> <i>name</i> the name whose associated value is to be returned in answer </p>
<p> <i>answer</i> the list of all names in the dictionary, note that the caller must free storage allocated to the list via a call to <code><a href="/docs/linux/man/3-getdns_list_destroy/">getdns_list_destroy</a>(3)</code> </p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion the functions return <code>GETDNS_RETURN_GOOD</code> , otherwise the following error values are returned: </p>
<p> <code>GETDNS_RETURN_GENERIC_ERROR</code> if this_dict is not a valid dictionary </p>
<p> <code>GETDNS_RETURN_NO_SUCH_DICT_NAME</code> if the name argument doesn&#8217;t exist in the dictionary </p>
<p> <code>GETDNS_RETURN_WRONG_TYPE_REQUESTED</code> if the requested data type doesn&#8217;t match the contents of the indexed argument or name </p>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3), <code><a href="/docs/linux/man/3-getdns_address/">getdns_address</a></code>(3), <code><a href="/docs/linux/man/3-getdns_dict/">getdns_dict</a></code>(3), <code><a href="/docs/linux/man/3-getdns_dict_set/">getdns_dict_set</a></code>(3), <code><a href="/docs/linux/man/3-getdns_general/">getdns_general</a></code>(3), <code><a href="/docs/linux/man/3-getdns_hostname/">getdns_hostname</a></code>(3), <code><a href="/docs/linux/man/3-getdns_list/">getdns_list</a></code>(3), <code><a href="/docs/linux/man/3-getdns_service/">getdns_service</a></code>(3), </p>
<h2>Index</h2>
