---
title: "gnutls_server_name_get(3)"
name: "gnutls_server_name_get"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_server_name_get/"
description: "gnutls_server_name_get – API function"
---

<h2>NAME</h2>
<p> gnutls_server_name_get &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_server_name_get(gnutls_session_t </code><i>session</i><code>, void * </code><i>data</i><code>, size_t * </code><i>data_length</i><code>, unsigned int * </code><i>type</i><code>, unsigned int </code><i>indx</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>void * data</p>
<dd> will hold the data</p>
<dt>size_t * data_length</p>
<dd> will hold the data length. Must hold the maximum size of data.</p>
<dt>unsigned int * type</p>
<dd> will hold the server name indicator type</p>
<dt>unsigned int indx</p>
<dd> is the index of the server_name</dl>
<h2>DESCRIPTION</h2>
<p> This function will allow you to get the name indication (if any), a client has sent. The name indication may be any of the enumeration gnutls_server_name_type_t. </p>
<p> If <i>type</i> is GNUTLS_NAME_DNS, then this function is to be used by servers that support virtual hosting, and the data will be a null terminated UTF-8 string. </p>
<p> If <i>data</i> has not enough size to hold the server name GNUTLS_E_SHORT_MEMORY_BUFFER is returned, and <i>data_length</i> will hold the required size. </p>
<p>&nbsp;<wbr><i>index</i>&nbsp;<wbr>is used to retrieve more than one server names&nbsp;<wbr>(if sent by the client). The first server name has an index of 0, the second 1 and so on. If no name with the given index exists GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE is returned.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></p>
<dd> </code></dl>
<h2>Index</h2>
