---
title: "getdns_address_sync(3)"
name: "getdns_address_sync"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_address_sync/"
description: "getdns_address, getdns_address_sync — get ip address(es) for a name"
---

<h2>NAME</h2>
<p> <code>getdns_address, </code> <code>getdns_address_sync</code> &#8212; get ip address(es) for a name </p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_return_t<br />
 <code>getdns_address</code> (getdns_context *context,</p>
<dl>
<dt>
<dd> const char *name,<br />
 getdns_dict *extensions,<br />
 void *userarg,<br />
 getdns_transaction_t *transaction_id,<br />
 getdns_callback_t callbackfn)</dl>
<p> getdns_return_t<br />
 <code>getdns_address_sync</code> (getdns_context *context,</p>
<dl>
<dt>
<dd> const char *name,<br />
 getdns_dict *extensions,<br />
 getdns_dict **response)</dl>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/3-getdns_address/">getdns_address</a>(3) and getdns_address_sync functions provide public entry points into the getdns API library to retrieve the address given a host name. They always returns both IPv4 and IPv6 addresses. This function will use all of the namespaces from the context (to better emulate getaddrinfo (3)). </p>
<dl>
<dt> <i>context</i></p>
<dd>A pointer to the previously created DNS context that is to be used with this DNS request. see getdns_context (3) </p>
<dt> <i>name</i></p>
<dd>the host name to resolve to an address (note that an IP address is considered invalid) </p>
<dt> <i>extensions</i></p>
<dd>extensions for this request, NULL if no extensions, see libgetdns (3) for a detailed description of extensions </p>
<dt> <i>userarg</i></p>
<dd>returned to the callback function untouched, can be NULL </p>
<dt> <i>transaction_id</i></p>
<dd>populated by the API and used to identify the callback (for example to getdns_cancel_callback), can be NULL, set to 0 if the function fails </p>
<dt> <i>callbackfn</i></p>
<dd>non-NULL pointer to a callback function defined by the application, typically used to process the response. Only the asynchronous signature accepts a callback function, the synchronous signature does not include a callback. See libgetdns (3) for a more detailed discussion of callback functions. </p>
<dt> <i>response</i></p>
<dd>A getdns_dict type is returned in response and always contains at least three names: replies_full (a list containing the DNS response as binary data), replies_tree (a list containing the parsed DNS response data) and status (an int). The storage associated with this must be freed by a call to getdns_free_sync_request_memory (3). </p>
<dt></dl>
<h2>RETURN VALUES</h2>
<dd>Upon successful completion the functions return <code>GETDNS_RETURN_GOOD</code> , otherwise the following error values are returned: </p>
<p> <code>GETDNS_RETURN_BAD_CONTEXT </code> if the context pointer is invalid or the context has internal deficiencies </p>
<p> <code>GETDNS_RETURN_BAD_DOMAIN_NAME</code> if the domain name passed to the function is invalid </p>
<p> <code>GETDNS_RETURN_EXTENSION_MISFORMAT</code> if the data type specified in one or more of the extensions does not match the specifications </p>
<p> <code>GETDNS_RETURN_GENERIC_ERROR</code> if some problem was encountered in the function not addressed by one of the more specific return codes </p>
<p> <code>GETDNS_RETURN_INVALID PARAMETER </code> if one or more parameters has an invalid value </p>
<p> <code>GETDNS_RETURN_MEMORY_ERROR</code> if unable to allocate the memory required </p>
<p> <code>GETDNS_RETURN_NO_SUCH_EXTENSION</code> if one or more of the strings specified in the extensions are not valid </p>
<p> The values of status included in the response parameter are: </p>
<p> <code>GETDNS_RESPSTATUS_GOOD</code> if at least one response was returned </p>
<p> <code>GETDNS_RESPSTATUS_NO_NAME</code> if queries for the name yielded all negative responses </p>
<p> <code>GETDNS_RESPSTATUS_ALL_TIMEOUT</code> if all queries for the name timed out </p>
<p> <code>GETDNS_RESPSTATUS_NO_SECURE_ANSWERS</code> if only secure replies accepted (per context) and at least one response was received but no DNS responses were secure through DNSSEC </p>
<p> For a more detailed explanation of the response object see <i>libgetdns</i> (3) </p>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>FILES</h2>
<p> /etc/hosts<br />
 /etc/resolv.conf </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3), <code><a href="/docs/linux/man/3-getdns_context/">getdns_context</a></code>(3), <code><a href="/docs/linux/man/3-getdns_free_sync_request_memory/">getdns_free_sync_request_memory</a></code>(3), <code><a href="/docs/linux/man/3-getdns_general/">getdns_general</a></code>(3), <code><a href="/docs/linux/man/3-getdns_general_sync/">getdns_general_sync</a></code>(3), <code><a href="/docs/linux/man/3-getdns_hostname/">getdns_hostname</a></code>(3), <code><a href="/docs/linux/man/3-getdns_hostname_sync/">getdns_hostname_sync</a></code>(3), <code><a href="/docs/linux/man/3-getdns_service/">getdns_service</a></code>(3), <code><a href="/docs/linux/man/3-getdns_service_sync/">getdns_service_sync</a></code>(3) </p>
<h2>Index</h2>
