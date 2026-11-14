---
title: "getdns_context_set_dnssec_allowed_skew(3)"
name: "getdns_context_set_dnssec_allowed_skew"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_context_set_dnssec_allowed_skew/"
description: "getdns_context_set_append_name, getdns_context_set_context_update_callback, getdns_context_set_dns_root_servers, getdns_context_set_dns_transport, getdns_context_set_dnssec_trust_anchors, getdns_co..."
---

<h2 class="name">NAME</h2>
<p> <code>getdns_context_set_append_name, </code> <code>getdns_context_set_context_update_callback, </code> <code>getdns_context_set_dns_root_servers, </code> <code>getdns_context_set_dns_transport, </code> <code>getdns_context_set_dnssec_trust_anchors, </code> <code>getdns_context_set_dnssec_allowed_skew,</code> <code>getdns_context_set_follow_redirects, </code> <code>getdns_context_set_limit_outstanding_queries, </code> <code>getdns_context_set_namespaces, </code> <code>getdns_context_set_resolution_type, </code> <code>getdns_context_set_suffix, </code> <code>getdns_context_set_timeout, </code> &#8212; getdns context manipulation routines</p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_return_t<br />
 <code>getdns_context_set_append_name</code> (getdns_context_t context,</p>
<dl>
<dt>
<dd>
 getdns_append_name_t when_to_append)</dl>
<p> getdns_return_t<br />
 <code>getdns_context_set_context_update_callback</code> (getdns_context_t context,</p>
<dl>
<dt>
<dd>
 (*callback)(struct getdns_context *context, uint16_t changed_item))</dl>
<p> getdns_return_t<br />
 <code>getdns_context_set_dns_root_servers</code> (getdns_context_t context,</p>
<dl>
<dt>
<dd>
 getdns_list *root_addresses)</dl>
<p> getdns_return_t<br />
 <code>getdns_context_set_dns_transport</code> (getdns_context_t context,</p>
<dl>
<dt>
<dd>
 uint16_t transport)</dl>
<p> getdns_return_t<br />
 <code>getdns_contet_set_dnssec_allowed_skew</code> (getdns_context *context,</p>
<dl>
<dt>
<dd> uint32_t skew_seconds)</dl>
<p> getdns_return_t<br />
 <code>getdns_contet_set_dnssec_trust_anchors</code> (getdns_context *context,</p>
<dl>
<dt>
<dd> getdns_list *trust_anchors)</dl>
<p> getdns_return_t<br />
 <code>getdns_context_set_follow_redirects</code> (getdns_context_t context,</p>
<dl>
<dt>
<dd>
 getdns_redirects_t followredir)</dl>
<p> getdns_return_t<br />
 <code>getdns_context_set_limit_outstanding_queries</code> (getdns_context_t context,</p>
<dl>
<dt>
<dd>
 uint16_t limit)</dl>
<p> getdns_return_t<br />
 <code>getdns_context_set_namespaces</code> (getdns_context_t context,</p>
<dl>
<dt>
<dd>
 size_t namespace_count,<br />
 uint16_t *namespaces)</dl>
<p> getdns_return_t<br />
 <code>getdns_context_set_resolution_type</code> (getdns_context_t context,</p>
<dl>
<dt>
<dd> uint16_t restype)</dl>
<p> getdns_return_t<br />
 <code>getdns_context_set_suffix</code> (getdns_context *context,</p>
<dl>
<dt>
<dd> getdns_list *suffixes)</dl>
<p> getdns_return_t<br />
 <code>getdns_context_set_timeout</code> (getdns_context_t context,</p>
<dl>
<dt>
<dd> uint16_t timeout)</dl>
<h2>DESCRIPTION</h2>
<p> These functions are used to manipulate a previously allocated and initialized context, see getdns_context (3) for more details on the functions used to allocate, initialized and destroy contexts and for a more detailed discussion of the getdns_context in general. </p>
<p> <code>getdns_context_set_append_name</code> Specifies whether to append a suffix supplied via getdns_context_set_suffix (3) to the query string before the API starts resolving a name. </p>
<p> <code>getdns_context_set_context_update_callback</code> sets a function that will be called if changes to the system files (for example /etc/resolv.conf and /etc/hosts). </p>
<p> <code>getdns_context_set_dns_transport</code> specifies the transport used for DNS lookups, the default is to use UDP and fall back to TCP as needed. </p>
<p> <code>getdns_context_set_dnssec_trust_anchors</code> allows the caller to specify trust anchors as alternatives to the default trust anchors </p>
<p> <code>getdns_context_set_dnssec_allowed_skew</code> set the number of seconds skew allowed in either direction when checking an RRSIGs expiration and inception fields, the default is 0. </p>
<p> <code>getdns_context_set_limit_outstanding_queries</code> specifies the maximum number of outstanding DNS queries, the API will queue queries over this limit until current queries are answers and will then automatically issue the queries on the queue. </p>
<p> <code>getdns_context_set_dns_root_servers</code> provides an alternate set of addresses to use to look up the top level domains. The default (if this function is not called) is the list of IANA root servers (think of this as the root hints). </p>
<p> <code>getdns_context_set_follow_redirects</code> specifies whether or not DNS queries follow redirects (CNAME and DNAME), the default behavior is to follow redirects and return the eventual target. </p>
<p> <code>getdns_context_set_namespaces</code> sets the namespaces to be used by the resolver, the default is DNS and then local files. Future implementations will support netbios, mdns, and nis. </p>
<p> <code>getdns_context_set_resolution_type</code> specifies whether DNS queries are performed with non-recursive lookups or as a stub resolver. </p>
<p> <code>getdns_context_set_suffix</code> Append suffixes to domain names prior to executing the lookup based on getdns_context_set_append_name. </p>
<p> <code>getdns_context_set_timeout</code> specifies the number of milliseconds the API will wait for a response. </p>
<dl>
<dt> <i>context</i></p>
<dd>a previously allocated and initialized getdns_context </p>
<dt> <i>callback</i></p>
<dd>a callback function that will be called when changes are made to the system files (/etc/resolv.conf and /etc/hosts) for contexts created with set_from_os = 1. When this function is called the changed_item parameter indicates which item in the context has changed. </p>
<dt> <i>root_addresses</i></p>
<dd>This is a list of getdns_dict types that each identify a single root server to use to look up top level domains. Each dictionary includes two names, <i>address_type</i> , a bindata containing the string &quot;IPv4&quot; or &quot;IPv6&quot; and <i>address_data</i> a bindata containing the IP address. </p>
<dt> <i>transport</i></p>
<dd>may be one of GETDNS_CONTEXT_UDP_FIRST_AND_FALL_BACK_TO_TCP, GETDNS_CONTEXT_UDP_ONLY, GETDNS_CONTEXT_TCP_ONLY, GETDNS_CONTEXT_TCP_ONLY_KEEP_CONNECTIONS_OPEN. If you need more information on what each of these means reread the mnemonic and take a guess ;) </p>
<dt> <i>followredir</i></p>
<dd>If set to GETDNS_REDIRECTS_FOLLOW (the default) then the eventual target of the redirect is returned. If set to GETDNS_REDIRECTS_DO_NOT_FOLLOW then the CNAME or DNAME is returned and NOT the eventual target. </p>
<dt> <i>limit</i></p>
<dd>the maximum number of concurrent outstanding (unanswered) DNS queries, if exceeded the API will queue queries and issue them as the number of outstanding queries drops. A value of 0 indicates that there is no limit. </p>
<dt> <i>namespaces</i></p>
<dd>The namespaces array contains an ordered list of namespaces that will be queried. Important: this context setting is ignored for the getdns_general and getdns_general_sync functions; it is used for the other functions. The values are GETDNS_CONTEXT_NAMESPACE_DNS, GETDNS_CONTEXT_NAMESPACE_LOCALNAMES, GETDNS_CONTEXT_NAMESPACE_NETBIOS, GETDNS_CONTEXT_NAMESPACE_MDNS, and GETDNS_CONTEXT_NAMESPACE_NIS. When a normal lookup is done, the API does the lookups in the order given and stops when it gets the first result; a different method with the same result would be to run the queries in parallel and return when it gets the first result. Because lookups might be done over different mechanisms because of the different namespaces, there can be information leakage that is similar to that seen with getaddrinfo(). The default is determined by the OS. </p>
<dt> <i>restype</i></p>
<dd>can be set to either GETDNS_CONTEXT_RECURSIVE (the default) or GETDNS_CONTEXT_STUB (requires that forwarders be specified by the caller). </p>
<dt> <i>seconds_skew</i></p>
<dd>the number of seconds skew allowed in either direction when checking an RRSIGs expiration and inception fields. </p>
<dt> <i>suffixes</i></p>
<dd>A list of bindatas that are strings that are to be appended based on getdns_context_set_append_name. The values here follow the rules in section 2.1 of RFC 4343 to allow non-ASCII octets and special characters in labels. </p>
<dt> <i>timeout</i></p>
<dd>the number of milliseconds the API will wait for a response, after which the callback will be invoked (or the synchronous function will return) with a timeout error. </p>
<dt> <i>trust_anchors</i></p>
<dd>list of bindatas that are the DNSSEC trust anchors expressed as RDATA from the DNSKEY resource records, the default are supplied by the IANA root. </p>
<dt> <i>when_to_append</i></p>
<dd>The value is</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GETDNS_APPEND_NAME_ALWAYS,</p>
<dt>&bull;</p>
<dd> GETDNS_APPEND_NAME_ONLY_TO_SINGLE_LABEL_AFTER_FAILURE,</p>
<dt>&bull;</p>
<dd> GETDNS_APPEND_NAME_ONLY_TO_MULTIPLE_LABEL_NAME_AFTER_FAILURE, or</p>
<dt>&bull;</p>
<dd> GETDNS_APPEND_NAME_NEVER.</dl>
</dl>
<dt></dl>
<h2>RETURN VALUES</h2>
<dd>Upon successful completion the functions return <code>GETDNS_RETURN_GOOD</code> , otherwise the following error values are returned: </p>
<p> <code>GETDNS_RETURN_BAD_CONTEXT </code> if the context pointer is invalid </p>
<p> <code>GETDNS_RETURN_CONTEXT_UPDATE_FAIL</code> if there was a problem updating the context </p>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>FILES</h2>
<p> /etc/hosts<br />
 /etc/resolv.conf </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3), <code><a href="/docs/linux/man/3-getdns_address/">getdns_address</a></code>(3), <code><a href="/docs/linux/man/3-getdns_address_sync/">getdns_address_sync</a></code>(3), <code><a href="/docs/linux/man/3-getdns_context/">getdns_context</a></code>(3), <code><a href="/docs/linux/man/3-getdns_general/">getdns_general</a></code>(3), <code><a href="/docs/linux/man/3-getdns_general_sync/">getdns_general_sync</a></code>(3), <code><a href="/docs/linux/man/3-getdns_hostname/">getdns_hostname</a></code>(3), <code><a href="/docs/linux/man/3-getdns_hostname_sync/">getdns_hostname_sync</a></code>(3), <code><a href="/docs/linux/man/3-getdns_service/">getdns_service</a></code>(3), <code><a href="/docs/linux/man/3-getdns_service_sync/">getdns_service_sync</a></code>(3). </p>
<h2>Index</h2>
