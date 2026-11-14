---
title: "getdns_general_sync(3)"
name: "getdns_general_sync"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_general_sync/"
description: "getdns_general, getdns_general_sync — do a getdns DNS lookup"
---

<h2>NAME</h2>
<p> <code>getdns_general, </code> <code>getdns_general_sync</code> &#8212; do a getdns DNS lookup </p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_return_t<br />
 <code>getdns_general</code> (getdns_context *context,</p>
<dl>
<dt>
<dd> const char *name,<br />
 uint16_t request_type<br />
 getdns_dict *extensions,<br />
 void *userarg,<br />
 getdns_transaction_t *transaction_id,<br />
 getdns_callback_t callbackfn)</dl>
<p> getdns_return_t<br />
 <code>getdns_general_sync</code> (getdns_context *context,</p>
<dl>
<dt>
<dd> const char *name,<br />
 uint16_t request_type<br />
 getdns_dict *extensions,<br />
 getdns_dict **response)</dl>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/3-getdns_general/">getdns_general</a>(3) and getdns_general_sync functions provide public entry points into the getdns API library to retrieve any valid responses to a query from the DNS (note that other namespaces in the context are not used). Most typical use cases for applications are probably satisifed via calls to <a href="/docs/linux/man/3-getdns_address/">getdns_address</a>(3) which would replace <a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a>(3). </p>
<dl>
<dt> <i>context</i></p>
<dd>A pointer to the previsouly created DNS context that is to be used with this DNS request. see getdns_context (3) </p>
<dt> <i>name</i></p>
<dd>The ASCII-based domain name looked up as a string. This can also be an IPv4 or IPv6 address for request types that take addresses instead of domain names, such as PTR. The values here follow the rules in section 2.1 of RFC 4343 to allow non-ASCII octets and special characters in labels. </p>
<dt> <i>request_type</i></p>
<dd>Specifies the RRtype for the query; the RRtype numbers are listed in the IANA registry. For example, to get the NS records, request_type would be 2. The API also has defined macros for most of the RRtypes by name; the definition names all start with &quot;GETDNS_RRTYPE_&quot;. For example, to get the NS records, you can also set the request_type to GETDNS_RRTYPE_NS. </p>
<dt> <i>extensions</i></p>
<dd>extensions for this request, NULL if no extensions, see libgetnds (3) for a detailed description of extensions </p>
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
<h2>REQUEST TYPES</h2>
<p> This is a list of the most common request types, a full list of request types in more detail is available at <a rel="nofollow" href="http://www.iana.org/assignments/dns-parameters/dns-parameters.xml">http://www.iana.org/assignments/dns-parameters/dns-parameters.xml</a> </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>A</code></p>
<dd> Host address</p>
<dt><code>AAAA</code></p>
<dd> IPv6 address</p>
<dt><code>CAA</code></p>
<dd> Certificate Authority Authorization</p>
<dt><code>CNAME</code></p>
<dd> Canonical name for an alias</p>
<dt><code>DLV</code></p>
<dd> DNSSEC lookaside validation</p>
<dt><code>DNAME</code></p>
<dd> DNAME</p>
<dt><code>DS</code></p>
<dd> Delegation signer</p>
<dt><code>HINFO</code></p>
<dd> Host information</p>
<dt><code>KEY</code></p>
<dd> Security key</p>
<dt><code>MINFO</code></p>
<dd> Mailbox or mail list information</p>
<dt><code>MX</code></p>
<dd> Mail exchange</p>
<dt><code>NS</code></p>
<dd> Authoritative name server</p>
<dt><code>NSEC</code></p>
<dd> Next secure record</p>
<dt><code>NSEC3</code></p>
<dd> Next secure record (hashed)</p>
<dt><code>NSEC3PARAM</code></p>
<dd> NSEC3PARAM</p>
<dt><code>PTR</code></p>
<dd> Domain name pointer</p>
<dt><code>RRSIG</code></p>
<dd> Signature for a record set</p>
<dt><code>SIG</code></p>
<dd> Security signature</p>
<dt><code>SOA</code></p>
<dd> Marks the start of a zone of authority</p>
<dt><code>SRV</code></p>
<dd> Server selection</p>
<dt><code>TA</code></p>
<dd> DNSSEC trust authorities</p>
<dt><code>TKEY</code></p>
<dd> Transaction key</p>
<dt><code>TLSA</code></p>
<dd> TLSA</p>
<dt><code>TSIG</code></p>
<dd> Transaction signature</p>
<dt><code>TXT</code></p>
<dd> Text strings</dl>
</dl>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>FILES</h2>
<p> /etc/hosts<br />
 /etc/resolv.conf </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3), <code><a href="/docs/linux/man/3-getdns_address/">getdns_address</a></code>(3), <code><a href="/docs/linux/man/3-getdns_context/">getdns_context</a></code>(3), <code><a href="/docs/linux/man/3-getdns_free_sync_request_memory/">getdns_free_sync_request_memory</a></code>(3), <code><a href="/docs/linux/man/3-getdns_hostname/">getdns_hostname</a></code>(3), <code><a href="/docs/linux/man/3-getdns_service/">getdns_service</a></code>(3), </p>
<h2>Index</h2>
