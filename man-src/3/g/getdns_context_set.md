---

title: "getdns_context_set(3)"
name: "getdns_context_set"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_context_set/"
---

<b>getdns_context_set_append_name, </b> <b>getdns_context_set_context_update_callback, </b> <b>getdns_context_set_dns_root_servers, </b> <b>getdns_context_set_dns_transport, </b> <b>getdns_context_set_dnssec_trust_anchors, </b> <b>getdns_context_set_dnssec_allowed_skew,</b> <b>getdns_context_set_follow_redirects, </b> <b>getdns_context_set_limit_outstanding_queries, </b> <b>getdns_context_set_namespaces, </b> <b>getdns_context_set_resolution_type, </b> <b>getdns_context_set_suffix, </b> <b>getdns_context_set_timeout, </b> -- getdns context manipulation routines

<h2>LIBRARY</h2>

 DNS Resolver library (libgetdns, -lgetdns) 

<h2>SYNOPSIS</h2>

 #include &lt;getdns.h&gt; 

 getdns_return_t 
 <b>getdns_context_set_append_name</b> (getdns_context_t context,
<dl>
<dt>
</dt><dd> 
 getdns_append_name_t when_to_append)</dd></dl>
 

 getdns_return_t 
 <b>getdns_context_set_context_update_callback</b> (getdns_context_t context,
<dl>
<dt>
</dt><dd> 
 (*callback)(struct getdns_context *context, uint16_t changed_item))</dd></dl>
 

 getdns_return_t 
 <b>getdns_context_set_dns_root_servers</b> (getdns_context_t context,
<dl>
<dt>
</dt><dd> 
 getdns_list *root_addresses)</dd></dl>
 

 getdns_return_t 
 <b>getdns_context_set_dns_transport</b> (getdns_context_t context,
<dl>
<dt>
</dt><dd> 
 uint16_t transport)</dd></dl>
 

 getdns_return_t 
 <b>getdns_contet_set_dnssec_allowed_skew</b> (getdns_context *context,
<dl>
<dt>
</dt><dd> uint32_t skew_seconds)</dd></dl>
 

 getdns_return_t 
 <b>getdns_contet_set_dnssec_trust_anchors</b> (getdns_context *context,
<dl>
<dt>
</dt><dd> getdns_list *trust_anchors)</dd></dl>
 

 getdns_return_t 
 <b>getdns_context_set_follow_redirects</b> (getdns_context_t context,
<dl>
<dt>
</dt><dd> 
 getdns_redirects_t followredir)</dd></dl>
 

 getdns_return_t 
 <b>getdns_context_set_limit_outstanding_queries</b> (getdns_context_t context,
<dl>
<dt>
</dt><dd> 
 uint16_t limit)</dd></dl>
 

 getdns_return_t 
 <b>getdns_context_set_namespaces</b> (getdns_context_t context,
<dl>
<dt>
</dt><dd> 
 size_t namespace_count, 
 uint16_t *namespaces)</dd></dl>
 

 getdns_return_t 
 <b>getdns_context_set_resolution_type</b> (getdns_context_t context,
<dl>
<dt>
</dt><dd> uint16_t restype)</dd></dl>
 

 getdns_return_t 
 <b>getdns_context_set_suffix</b> (getdns_context *context,
<dl>
<dt>
</dt><dd> getdns_list *suffixes)</dd></dl>
 

 getdns_return_t 
 <b>getdns_context_set_timeout</b> (getdns_context_t context,
<dl>
<dt>
</dt><dd> uint16_t timeout)</dd></dl>
 

<h2>DESCRIPTION</h2>

 

 

 These functions are used to manipulate a previously allocated and initialized context, see getdns_context (3) for more details on the functions used to allocate, initialized and destroy contexts and for a more detailed discussion of the getdns_context in general. 

 

 <b>getdns_context_set_append_name</b> Specifies whether to append a suffix supplied via getdns_context_set_suffix (3) to the query string before the API starts resolving a name. 

 

 <b>getdns_context_set_context_update_callback</b> sets a function that will be called if changes to the system files (for example /etc/resolv.conf and /etc/hosts). 

 

 <b>getdns_context_set_dns_transport</b> specifies the transport used for DNS lookups, the default is to use UDP and fall back to TCP as needed. 

 

 <b>getdns_context_set_dnssec_trust_anchors</b> allows the caller to specify trust anchors as alternatives to the default trust anchors 

 

 <b>getdns_context_set_dnssec_allowed_skew</b> set the number of seconds skew allowed in either direction when checking an RRSIGs expiration and inception fields, the default is 0. 

 

 <b>getdns_context_set_limit_outstanding_queries</b> specifies the maximum number of outstanding DNS queries, the API will queue queries over this limit until current queries are answers and will then automatically issue the queries on the queue. 

 

 <b>getdns_context_set_dns_root_servers</b> provides an alternate set of addresses to use to look up the top level domains. The default (if this function is not called) is the list of IANA root servers (think of this as the root hints). 

 

 <b>getdns_context_set_follow_redirects</b> specifies whether or not DNS queries follow redirects (CNAME and DNAME), the default behavior is to follow redirects and return the eventual target. 

 

 <b>getdns_context_set_namespaces</b> sets the namespaces to be used by the resolver, the default is DNS and then local files. Future implementations will support netbios, mdns, and nis. 

 

 <b>getdns_context_set_resolution_type</b> specifies whether DNS queries are performed with non-recursive lookups or as a stub resolver. 

 

 <b>getdns_context_set_suffix</b> Append suffixes to domain names prior to executing the lookup based on getdns_context_set_append_name. 

 

 <b>getdns_context_set_timeout</b> specifies the number of milliseconds the API will wait for a response. 

<dl>
<dt> <i>context</i>
</dt><dd>a previously allocated and initialized getdns_context 
</dd><dt> <i>callback</i>
</dt><dd>a callback function that will be called when changes are made to the system files (/etc/resolv.conf and /etc/hosts) for contexts created with set_from_os = 1. When this function is called the changed_item parameter indicates which item in the context has changed. 
</dd><dt> <i>root_addresses</i>
</dt><dd>This is a list of getdns_dict types that each identify a single root server to use to look up top level domains. Each dictionary includes two names, <i>address_type</i> , a bindata containing the string &quot;IPv4&quot; or &quot;IPv6&quot; and <i>address_data</i> a bindata containing the IP address. 
</dd><dt> <i>transport</i>
</dt><dd>may be one of GETDNS_CONTEXT_UDP_FIRST_AND_FALL_BACK_TO_TCP, GETDNS_CONTEXT_UDP_ONLY, GETDNS_CONTEXT_TCP_ONLY, GETDNS_CONTEXT_TCP_ONLY_KEEP_CONNECTIONS_OPEN. If you need more information on what each of these means reread the mnemonic and take a guess ;) 
</dd><dt> <i>followredir</i>
</dt><dd>If set to GETDNS_REDIRECTS_FOLLOW (the default) then the eventual target of the redirect is returned. If set to GETDNS_REDIRECTS_DO_NOT_FOLLOW then the CNAME or DNAME is returned and NOT the eventual target. 
</dd><dt> <i>limit</i>
</dt><dd>the maximum number of concurrent outstanding (unanswered) DNS queries, if exceeded the API will queue queries and issue them as the number of outstanding queries drops. A value of 0 indicates that there is no limit. 
</dd><dt> <i>namespaces</i>
</dt><dd>The namespaces array contains an ordered list of namespaces that will be queried. Important: this context setting is ignored for the getdns_general and getdns_general_sync functions; it is used for the other functions. The values are GETDNS_CONTEXT_NAMESPACE_DNS, GETDNS_CONTEXT_NAMESPACE_LOCALNAMES, GETDNS_CONTEXT_NAMESPACE_NETBIOS, GETDNS_CONTEXT_NAMESPACE_MDNS, and GETDNS_CONTEXT_NAMESPACE_NIS. When a normal lookup is done, the API does the lookups in the order given and stops when it gets the first result; a different method with the same result would be to run the queries in parallel and return when it gets the first result. Because lookups might be done over different mechanisms because of the different namespaces, there can be information leakage that is similar to that seen with getaddrinfo(). The default is determined by the OS. 
</dd><dt> <i>restype</i>
</dt><dd>can be set to either GETDNS_CONTEXT_RECURSIVE (the default) or GETDNS_CONTEXT_STUB (requires that forwarders be specified by the caller). 
</dd><dt> <i>seconds_skew</i>
</dt><dd>the number of seconds skew allowed in either direction when checking an RRSIGs expiration and inception fields. 
</dd><dt> <i>suffixes</i>
</dt><dd>A list of bindatas that are strings that are to be appended based on getdns_context_set_append_name. The values here follow the rules in section 2.1 of RFC 4343 to allow non-ASCII octets and special characters in labels. 
</dd><dt> <i>timeout</i>
</dt><dd>the number of milliseconds the API will wait for a response, after which the callback will be invoked (or the synchronous function will return) with a timeout error. 
</dd><dt> <i>trust_anchors</i>
</dt><dd>list of bindatas that are the DNSSEC trust anchors expressed as RDATA from the DNSKEY resource records, the default are supplied by the IANA root. 
</dd><dt> <i>when_to_append</i>
</dt><dd>The value is
</dd><dl>
<dl>
<dt>&bull;
</dt><dd> GETDNS_APPEND_NAME_ALWAYS,
</dd><dt>&bull;
</dt><dd> GETDNS_APPEND_NAME_ONLY_TO_SINGLE_LABEL_AFTER_FAILURE,
</dd><dt>&bull;
</dt><dd> GETDNS_APPEND_NAME_ONLY_TO_MULTIPLE_LABEL_NAME_AFTER_FAILURE, or
</dd><dt>&bull;
</dt><dd> GETDNS_APPEND_NAME_NEVER.</dd></dl>
</dl>
 

<dt></dt></dl>

<h2>RETURN VALUES</h2>

 

<dd>Upon successful completion the functions return <b>GETDNS_RETURN_GOOD</b> , otherwise the following error values are returned: 

 

 <b>GETDNS_RETURN_BAD_CONTEXT </b> if the context pointer is invalid 

 <b>GETDNS_RETURN_CONTEXT_UPDATE_FAIL</b> if there was a problem updating the context 

<h2>EXAMPLES</h2>

 

 TBD 

<h2>FILES</h2>

 
 /etc/hosts 
 /etc/resolv.conf 

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/3-libgetdns/">libgetdns</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_address/">getdns_address</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_address_sync/">getdns_address_sync</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_context/">getdns_context</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_general/">getdns_general</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_general_sync/">getdns_general_sync</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_hostname/">getdns_hostname</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_hostname_sync/">getdns_hostname_sync</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_service/">getdns_service</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_service_sync/">getdns_service_sync</a></b>(3).
