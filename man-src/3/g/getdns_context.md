---
title: "getdns_context(3)"
name: "getdns_context"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_context/"
description: "getdns_context, getdns_context_create, getdns_context_create_with_memory_functions, getdns_context_create_with_extended_memory_functions, getdns_context_destroy, getdns_context_get_api_information ..."
---

<h2 class="name">NAME</h2>
<p> <code>getdns_context, </code> <code>getdns_context_create, </code> <code>getdns_context_create_with_memory_functions, </code> <code>getdns_context_create_with_extended_memory_functions, </code> <code>getdns_context_destroy, </code> <code>getdns_context_get_api_information </code> &#8212; getdns context create and destroy routines</p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_return_t<br />
 <code>getdns_context_create</code> (getdns_context ** context,</p>
<dl>
<dt>
<dd>
 int set_from_os)</dl>
<p> getdns_return_t<br />
 <code>getdns_context_create_with_memory_functions</code> (getdns_context ** context,</p>
<dl>
<dt>
<dd>
 int set_from_os,<br />
 void *(*malloc) (size_t),<br />
 void *(*realloc) (void *, size_t),<br />
 void (*free) (void *))</dl>
<p> getdns_return_t<br />
 <code>getdns_context_create_with_extended_memory_functions</code> (getdns_context **context,</p>
<dl>
<dt>
<dd>
 int set_from_os,<br />
 void *userarg,<br />
 void *(*malloc) (void *userarg, size_t),<br />
 void *(*realloc) (void *userarg, void *, size_t),<br />
 void (*free) (void *userarg, void *))</dl>
<p> void<br />
 <code>getdns_context_destroy</code> (getdns_context *context) </p>
<p> getdns_dict *<br />
 <code>getdns_context_get_api_information</code> (getdns_context *context) </p>
<h2>DESCRIPTION</h2>
<p> Calls to getdns functions require a DNS context, which is a group of API settings that affect how DNS calls are made. For most applications, a default context is sufficient. </p>
<p> To create a new DNS context, use the function:</p>
<dl>
<dt>
<dd>
 getdns_return_t <code>getdns_context_create</code> (getdns_context_t *context, bool set_from_os)</dl>
<p> The call to getdns_context_create immediately returns a context that can be used with other API calls; that context contains the API&#8217;s default values. Most applications will want set_from_os set to true. </p>
<p> To clean up the context, including cleaning up all outstanding transactions that were called using this context, use the function:</p>
<dl>
<dt>
<dd>
 void <code>getdns_context_destroy</code> (getdns_context_t context)</dl>
<p> When getdns_context_destroy() returns, the application knows that all outstanding transactions associated with this context will have been called; callbacks that had not been called before getdns_context_destroy() was called will be called with a callback_type of GETDNS_CALLBACK_CANCEL. getdns_context_destroy() returns after all of the needed cleanup is done and callbacks are made. </p>
<dl>
<dt> <i>context</i></p>
<dd>Used to return the pointer to an opaque structure. The caller passes the address of a pointer (decl: getdns_context *context; passed as &amp;context) which will be populated as a result of returning from the function. The result is a newly allocated and initialized context (if there are no errors). In the getdns_destroy_context function this is the context whose associated memory will be released. </p>
<dt> <i>set_from_os</i></p>
<dd>If set_from_os is 0 then the caller must provide forwarding name servers if running in stub mode. If set_from_os is 1 then the system files are used to initialize the context. /etc/resolv.conf is used to populate forwarders when running as a stub resolver (only &quot;nameserver&quot; lines are recognized). If set_from_os is 1 /etc/hosts entries are preferred before resorting to a DNS query. Errors in the system files will not prevent the context form being constructed. </p>
<dt> <i>userarg</i></p>
<dd>In the extended use case this argument is passed unchanged to each of the memory management functions each time they are called. </p>
<dt> <i>malloc</i></p>
<dd>The function that will be used for creating response dicts (and the members within the response dicts). By default the system malloc is used. </p>
<dt> <i>realloc</i></p>
<dd>The function that will be used for creating response dicts (and the members within the response dicts). By default the system realloc is used. </p>
<dt> <i>free</i></p>
<dd>The function that will be used for releasing storage for response dicts (and the members within the response dicts). By default the system free is used. </p>
</dl>
<h2>DESCRIPTION (LONG)</h2>
<p> Many calls in the DNS API require a DNS context. A DNS context contains the information that the API needs in order to process DNS calls, such as the locations of upstream DNS servers, DNSSEC trust anchors, and so on. The internal structure of the DNS context is opaque, and might be different on each OS. When a context is passed to any function, it must be an allocated context; the context must not be NULL. </p>
<p> A typical application using this API doesn&#8217;t need to know anything about contexts. Basically, the application creates a default context, uses it in the functions that require a context, and then deallocates it when done. Context manipulation is available for more DNS-aware programs, but is unlikely to be of interest to applications that just want the results of lookups for A, AAAA, SRV, and PTR records. </p>
<p> It is expected that contexts in implementations of the API will not necessarily be thread-safe, but they will not be thread-hostile. A context should not be used by multiple threads: create a new context for use on a different thread. It is just fine for an application to have many contexts, and some DNS-heavy applications will certainly want to have many even if the application uses a single thread. </p>
<p> When the context is used in the API for the first time and set_from_os is 1, the API starts replacing some of the values with values from the OS, such as those that would be found in <a href="/docs/linux/man/3-res_query/">res_query</a>(3), /etc/resolv.conf, and so on, then proceeds with the new function. Some advanced users will not want the API to change the values to the OS&#8217;s defaults; if set_from_os is 0, the API will not do any updates to the initial values based on changes in the OS. For example, this might be useful if the API is acting as a stub resolver that is using a specific upstream recursive resolver chosen by the application, not the one that might come back from DHCP. </p>
<dl>
<dt></dl>
<h2>RETURN VALUES</h2>
<dd>Upon successful completion each of these functions return <code>GETDNS_RETURN_GOOD</code> , otherwise the following error values are returned: </p>
<p> <code>GETDNS_RETURN_GENERIC_ERROR</code> memory allocation failed or some other untoward thing happened while initializing the context </p>
<p> <code>GETDNS_RETURN_BAD_CONTEXT </code> if the context pointer is invalid (getdns_context_destroy) </p>
<p> The getdns_dict returned by getdns_context_get_api_information must be destroyed by the called and includes the following name/value pairs: </p>
<dl>
<dt>version_string</p>
<dd> a bindata containing a printable string of the version of the DNS API implemented by this library </p>
<dt>implementation_string</p>
<dd> a bindata containing a printable string set by the implementation </p>
<dt>resolution_type</p>
<dd> an int equal to GETDNS_RESOLUTION_RECURSING or GETDNS_RESOLUTION_STUB </p>
<dt>all_context</p>
<dd> a getdns_dict with names for all the types of context, feed it to getdns_pretty_print_dict (3) for something easily readable </p>
</dl>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>FILES</h2>
<p> /etc/hosts<br />
 /etc/resolv.conf </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3), <code><a href="/docs/linux/man/3-getdns_address/">getdns_address</a></code>(3), <code><a href="/docs/linux/man/3-getdns_address_sync/">getdns_address_sync</a></code>(3), <code><a href="/docs/linux/man/3-getdns_context_set/">getdns_context_set</a></code>(3), <code><a href="/docs/linux/man/3-getdns_context_set_context_update_callback/">getdns_context_set_context_update_callback</a></code>(3), <code><a href="/docs/linux/man/3-getdns_general/">getdns_general</a></code>(3), <code><a href="/docs/linux/man/3-getdns_general_sync/">getdns_general_sync</a></code>(3), <code><a href="/docs/linux/man/3-getdns_hostname/">getdns_hostname</a></code>(3), <code><a href="/docs/linux/man/3-getdns_hostname_sync/">getdns_hostname_sync</a></code>(3), <code><a href="/docs/linux/man/3-getdns_service/">getdns_service</a></code>(3), <code><a href="/docs/linux/man/3-getdns_service_sync/">getdns_service_sync</a></code>(3). </p>
<h2>Index</h2>
