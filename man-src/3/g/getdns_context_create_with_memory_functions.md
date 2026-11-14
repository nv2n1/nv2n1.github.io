---
title: "getdns_context_create_with_memory_functions(3)"
name: "getdns_context_create_with_memory_functions"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_context_create_with_memory_functions/"
---

<h2 class="name">NAME</h2>
 

 <b>getdns_context, </b> <b>getdns_context_create, </b> <b>getdns_context_create_with_memory_functions, </b> <b>getdns_context_create_with_extended_memory_functions, </b> <b>getdns_context_destroy, </b> <b>getdns_context_get_api_information </b> -- getdns context create and destroy routines

<h2>LIBRARY</h2>

 DNS Resolver library (libgetdns, -lgetdns) 

<h2>SYNOPSIS</h2>

 #include &lt;getdns.h&gt; 

 getdns_return_t 
 <b>getdns_context_create</b> (getdns_context ** context,
<dl>
<dt>
<dd> 
 int set_from_os)</dl>
 

 getdns_return_t 
 <b>getdns_context_create_with_memory_functions</b> (getdns_context ** context,
<dl>
<dt>
<dd> 
 int set_from_os, 
 void *(*malloc) (size_t), 
 void *(*realloc) (void *, size_t), 
 void (*free) (void *))</dl>
 

 getdns_return_t 
 <b>getdns_context_create_with_extended_memory_functions</b> (getdns_context **context,
<dl>
<dt>
<dd> 
 int set_from_os, 
 void *userarg, 
 void *(*malloc) (void *userarg, size_t), 
 void *(*realloc) (void *userarg, void *, size_t), 
 void (*free) (void *userarg, void *))</dl>
 

 void 
 <b>getdns_context_destroy</b> (getdns_context *context) 

 getdns_dict * 
 <b>getdns_context_get_api_information</b> (getdns_context *context) 

<h2>DESCRIPTION</h2>

 

 

 Calls to getdns functions require a DNS context, which is a group of API settings that affect how DNS calls are made. For most applications, a default context is sufficient. 

 

 To create a new DNS context, use the function:
<dl>
<dt>
<dd> 
 getdns_return_t <b>getdns_context_create</b> (getdns_context_t *context, bool set_from_os)</dl>
 

 

 The call to getdns_context_create immediately returns a context that can be used with other API calls; that context contains the API's default values. Most applications will want set_from_os set to true. 

 

 To clean up the context, including cleaning up all outstanding transactions that were called using this context, use the function:
<dl>
<dt>
<dd> 
 void <b>getdns_context_destroy</b> (getdns_context_t context)</dl>
 

 

 When getdns_context_destroy() returns, the application knows that all outstanding transactions associated with this context will have been called; callbacks that had not been called before getdns_context_destroy() was called will be called with a callback_type of GETDNS_CALLBACK_CANCEL. getdns_context_destroy() returns after all of the needed cleanup is done and callbacks are made. 

<dl>
<dt> <i>context</i>
<dd>Used to return the pointer to an opaque structure. The caller passes the address of a pointer (decl: getdns_context *context; passed as &amp;context) which will be populated as a result of returning from the function. The result is a newly allocated and initialized context (if there are no errors). In the getdns_destroy_context function this is the context whose associated memory will be released. 

<dt> <i>set_from_os</i>
<dd>If set_from_os is 0 then the caller must provide forwarding name servers if running in stub mode. If set_from_os is 1 then the system files are used to initialize the context. /etc/resolv.conf is used to populate forwarders when running as a stub resolver (only &quot;nameserver&quot; lines are recognized). If set_from_os is 1 /etc/hosts entries are preferred before resorting to a DNS query. Errors in the system files will not prevent the context form being constructed. 

<dt> <i>userarg</i>
<dd>In the extended use case this argument is passed unchanged to each of the memory management functions each time they are called. 

<dt> <i>malloc</i>
<dd>The function that will be used for creating response dicts (and the members within the response dicts). By default the system malloc is used. 

<dt> <i>realloc</i>
<dd>The function that will be used for creating response dicts (and the members within the response dicts). By default the system realloc is used. 

<dt> <i>free</i>
<dd>The function that will be used for releasing storage for response dicts (and the members within the response dicts). By default the system free is used. 

 

</dl>

<h2>DESCRIPTION (LONG)</h2>

 

 

 Many calls in the DNS API require a DNS context. A DNS context contains the information that the API needs in order to process DNS calls, such as the locations of upstream DNS servers, DNSSEC trust anchors, and so on. The internal structure of the DNS context is opaque, and might be different on each OS. When a context is passed to any function, it must be an allocated context; the context must not be NULL. 

 

 A typical application using this API doesn't need to know anything about contexts. Basically, the application creates a default context, uses it in the functions that require a context, and then deallocates it when done. Context manipulation is available for more DNS-aware programs, but is unlikely to be of interest to applications that just want the results of lookups for A, AAAA, SRV, and PTR records. 

 

 It is expected that contexts in implementations of the API will not necessarily be thread-safe, but they will not be thread-hostile. A context should not be used by multiple threads: create a new context for use on a different thread. It is just fine for an application to have many contexts, and some DNS-heavy applications will certainly want to have many even if the application uses a single thread. 

 

 When the context is used in the API for the first time and set_from_os is 1, the API starts replacing some of the values with values from the OS, such as those that would be found in <a HREF="/docs/linux/man/3-res_query/">res_query</a>(3), /etc/resolv.conf, and so on, then proceeds with the new function. Some advanced users will not want the API to change the values to the OS's defaults; if set_from_os is 0, the API will not do any updates to the initial values based on changes in the OS. For example, this might be useful if the API is acting as a stub resolver that is using a specific upstream recursive resolver chosen by the application, not the one that might come back from DHCP. 

<dl>
<dt></dl>

<h2>RETURN VALUES</h2>

 

<dd>Upon successful completion each of these functions return <b>GETDNS_RETURN_GOOD</b> , otherwise the following error values are returned: 

 

 <b>GETDNS_RETURN_GENERIC_ERROR</b> memory allocation failed or some other untoward thing happened while initializing the context 

 

 <b>GETDNS_RETURN_BAD_CONTEXT </b> if the context pointer is invalid (getdns_context_destroy) 

 

 The getdns_dict returned by getdns_context_get_api_information must be destroyed by the called and includes the following name/value pairs: 

<dl>
<dt>version_string
<dd> a bindata containing a printable string of the version of the DNS API implemented by this library 

<dt>implementation_string
<dd> a bindata containing a printable string set by the implementation 

<dt>resolution_type
<dd> an int equal to GETDNS_RESOLUTION_RECURSING or GETDNS_RESOLUTION_STUB 

<dt>all_context
<dd> a getdns_dict with names for all the types of context, feed it to getdns_pretty_print_dict (3) for something easily readable 

</dl>

<h2>EXAMPLES</h2>

 

 TBD 

<h2>FILES</h2>

 
 /etc/hosts 
 /etc/resolv.conf 

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/3-libgetdns/">libgetdns</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_address/">getdns_address</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_address_sync/">getdns_address_sync</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_context_set/">getdns_context_set</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_context_set_context_update_callback/">getdns_context_set_context_update_callback</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_general/">getdns_general</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_general_sync/">getdns_general_sync</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_hostname/">getdns_hostname</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_hostname_sync/">getdns_hostname_sync</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_service/">getdns_service</a></b>(3), <b><a HREF="/docs/linux/man/3-getdns_service_sync/">getdns_service_sync</a></b>(3). 

 

<h2>Index</h2>


