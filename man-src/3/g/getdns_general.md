---

title: "getdns_general(3)"
name: "getdns_general"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_general/"
description: "getdns_general, getdns_general_sync — do a getdns DNS lookup"
---

<h2>NAME</h2>
<p> <code>getdns_general, </code> <code>getdns_general_sync</code> &#8212; do a getdns DNS lookup </p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_return_t<br />
 <code>getdns_general</code> (getdns_context *context,</p>
<dl>
<dt>
</dt><dd> const char *name,<br />
 uint16_t request_type<br />
 getdns_dict *extensions,<br />
 void *userarg,<br />
 getdns_transaction_t *transaction_id,<br />
 getdns_callback_t callbackfn)</dd></dl>
<p> getdns_return_t<br />
 <code>getdns_general_sync</code> (getdns_context *context,</p>
<dl>
<dt>
</dt><dd> const char *name,<br />
 uint16_t request_type<br />
 getdns_dict *extensions,<br />
 getdns_dict **response)</dd></dl>
<p> The <a href="/docs/linux/man/3-getdns_general/">getdns_general</a>(3) and getdns_general_sync functions provide public entry points into the getdns API library to retrieve any valid responses to a query from the DNS (note that other namespaces in the context are not used). Most typical use cases for applications are probably satisifed via calls to <a href="/docs/linux/man/3-getdns_address/">getdns_address</a>(3) which would replace <a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a>(3). </p>
<dl>
<dt> <i>context</i></dt>
<dd>A pointer to the previsouly created DNS context that is to be used with this DNS request. see getdns_context (3) </dd>
<dt> <i>name</i></dt>
<dd>The ASCII-based domain name looked up as a string. This can also be an IPv4 or IPv6 address for request types that take addresses instead of domain names, such as PTR. The values here follow the rules in section 2.1 of RFC 4343 to allow non-ASCII octets and special characters in labels. </dd>
<dt> <i>request_type</i></dt>
<dd>Specifies the RRtype for the query; the RRtype numbers are listed in the IANA registry. For example, to get the NS records, request_type would be 2. The API also has defined macros for most of the RRtypes by name; the definition names all start with &quot;GETDNS_RRTYPE_&quot;. For example, to get the NS records, you can also set the request_type to GETDNS_RRTYPE_NS. </dd>
<dt> <i>extensions</i></dt>
<dd>extensions for this request, NULL if no extensions, see libgetnds (3) for a detailed description of extensions </dd>
<dt> <i>userarg</i></dt>
<dd>returned to the callback function untouched, can be NULL </dd>
<dt> <i>transaction_id</i></dt>
<dd>populated by the API and used to identify the callback (for example to getdns_cancel_callback), can be NULL, set to 0 if the function fails </dd>
<dt> <i>callbackfn</i></dt>
<dd>non-NULL pointer to a callback function defined by the application, typically used to process the response. Only the asynchronous signature accepts a callback function, the synchronous signature does not include a callback. See libgetdns (3) for a more detailed discussion of callback functions. </dd>
<dt> <i>response</i></dt>
<dd>A getdns_dict type is returned in response and always contains at least three names: replies_full (a list containing the DNS response as binary data), replies_tree (a list containing the parsed DNS response data) and status (an int). The storage associated with this must be freed by a call to getdns_free_sync_request_memory (3). </dd>
<dt></dt></dl>
<h2>RETURN VALUES</h2>
<dd>Upon successful completion the functions return <code>GETDNS_RETURN_GOOD</code> , otherwise the following error values are returned: </dd>
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
<dl>
<dt><code>A</code></dt>
<dd> Host address</dd>
<dt><code>AAAA</code></dt>
<dd> IPv6 address</dd>
<dt><code>CAA</code></dt>
<dd> Certificate Authority Authorization</dd>
<dt><code>CNAME</code></dt>
<dd> Canonical name for an alias</dd>
<dt><code>DLV</code></dt>
<dd> DNSSEC lookaside validation</dd>
<dt><code>DNAME</code></dt>
<dd> DNAME</dd>
<dt><code>DS</code></dt>
<dd> Delegation signer</dd>
<dt><code>HINFO</code></dt>
<dd> Host information</dd>
<dt><code>KEY</code></dt>
<dd> Security key</dd>
<dt><code>MINFO</code></dt>
<dd> Mailbox or mail list information</dd>
<dt><code>MX</code></dt>
<dd> Mail exchange</dd>
<dt><code>NS</code></dt>
<dd> Authoritative name server</dd>
<dt><code>NSEC</code></dt>
<dd> Next secure record</dd>
<dt><code>NSEC3</code></dt>
<dd> Next secure record (hashed)</dd>
<dt><code>NSEC3PARAM</code></dt>
<dd> NSEC3PARAM</dd>
<dt><code>PTR</code></dt>
<dd> Domain name pointer</dd>
<dt><code>RRSIG</code></dt>
<dd> Signature for a record set</dd>
<dt><code>SIG</code></dt>
<dd> Security signature</dd>
<dt><code>SOA</code></dt>
<dd> Marks the start of a zone of authority</dd>
<dt><code>SRV</code></dt>
<dd> Server selection</dd>
<dt><code>TA</code></dt>
<dd> DNSSEC trust authorities</dd>
<dt><code>TKEY</code></dt>
<dd> Transaction key</dd>
<dt><code>TLSA</code></dt>
<dd> TLSA</dd>
<dt><code>TSIG</code></dt>
<dd> Transaction signature</dd>
<dt><code>TXT</code></dt>
<dd> Text strings</dd></dl>
</dl>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>FILES</h2>
<p> /etc/hosts<br />
 /etc/resolv.conf </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3), <code><a href="/docs/linux/man/3-getdns_address/">getdns_address</a></code>(3), <code><a href="/docs/linux/man/3-getdns_context/">getdns_context</a></code>(3), <code>getdns_free_sync_request_memory</code>(3), <code><a href="/docs/linux/man/3-getdns_hostname/">getdns_hostname</a></code>(3), <code><a href="/docs/linux/man/3-getdns_service/">getdns_service</a></code>(3), </p>
