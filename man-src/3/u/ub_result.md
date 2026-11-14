---
title: "ub_result(3)"
name: "ub_result"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ub_result/"
description: "libunbound, unbound.h, ub_ctx, ub_result, ub_callback_t, ub_ctx_create, ub_ctx_delete, ub_ctx_set_option, ub_ctx_get_option, ub_ctx_config, ub_ctx_set_fwd, ub_ctx_resolvconf, ub_ctx_hosts, ub_ctx_a..."
---

<p><code>libunbound,</code> <code>unbound.h,</code> <code>ub_ctx,</code> <code>ub_result,</code> <code>ub_callback_t,</code> <code>ub_ctx_create,</code> <code>ub_ctx_delete,</code> <code>ub_ctx_set_option,</code> <code>ub_ctx_get_option,</code> <code>ub_ctx_config,</code> <code>ub_ctx_set_fwd,</code> <code>ub_ctx_resolvconf,</code> <code>ub_ctx_hosts,</code> <code>ub_ctx_add_ta,</code> <code>ub_ctx_add_ta_file,</code> <code>ub_ctx_trustedkeys,</code> <code>ub_ctx_debugout,</code> <code>ub_ctx_debuglevel,</code> <code>ub_ctx_async,</code> <code>ub_poll,</code> <code>ub_wait,</code> <code>ub_fd,</code> <code>ub_process,</code> <code>ub_resolve,</code> <code>ub_resolve_async,</code> <code>ub_cancel,</code> <code>ub_resolve_free,</code> <code>ub_strerror,</code> <code>ub_ctx_print_local_zones,</code> <code>ub_ctx_zone_add,</code> <code>ub_ctx_zone_remove,</code> <code>ub_ctx_data_add,</code> <code>ub_ctx_data_remove</code> &#8211; Unbound DNS validating resolver 1.4.20 functions.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;unbound.h&gt;
struct ub_ctx *
ub_ctx_create(void);
void ub_ctx_delete(struct ub_ctx *ctx);
int ub_ctx_set_option(struct ub_ctx *ctx, char *opt, char *val);
int ub_ctx_get_option(struct ub_ctx *ctx, char *opt, char **val);
int ub_ctx_config(struct ub_ctx *ctx, char *fname);
int ub_ctx_set_fwd(struct ub_ctx *ctx, char *addr);
int ub_ctx_resolvconf(struct ub_ctx *ctx, char *fname);
int ub_ctx_hosts(struct ub_ctx *ctx, char *fname);
int ub_ctx_add_ta(struct ub_ctx *ctx, char *ta);
int ub_ctx_add_ta_file(struct ub_ctx *ctx, char *fname);
int ub_ctx_trustedkeys(struct ub_ctx *ctx, char *fname);
int ub_ctx_debugout(struct ub_ctx *ctx, FILE *out);
int ub_ctx_debuglevel(struct ub_ctx *ctx, int d);
int ub_ctx_async(struct ub_ctx *ctx, int dothread);
int ub_poll(struct ub_ctx *ctx);
int ub_wait(struct ub_ctx *ctx);
int ub_fd(struct ub_ctx *ctx);
int ub_process(struct ub_ctx *ctx);
int ub_resolve(struct ub_ctx *ctx, char *name,

               int rrtype, int rrclass, struct ub_result **result);
int ub_resolve_async(struct ub_ctx *ctx, char *name,

                     int rrtype, int rrclass, void *mydata,

                     ub_callback_t callback, int *async_id);
int ub_cancel(struct ub_ctx *ctx, int async_id);
void ub_resolve_free(struct ub_result *result);
const char *
ub_strerror(int err);
int ub_ctx_print_local_zones(struct ub_ctx *ctx);
int ub_ctx_zone_add(struct ub_ctx *ctx, char *zone_name, char *zone_type);
int ub_ctx_zone_remove(struct ub_ctx *ctx, char *zone_name);
int ub_ctx_data_add(struct ub_ctx *ctx, char *data);
int ub_ctx_data_remove(struct ub_ctx *ctx, char *data);</code></pre>
<h2>Description</h2>
<p><code>Unbound </code> is an implementation of a DNS resolver, that does caching and DNSSEC validation. This is the library API, for using the -lunbound library. The server daemon is described in <i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8). The library can be used to convert hostnames to ip addresses, and back, and obtain other information from the DNS. The library performs public-key validation of results with DNSSEC. </p>
<p> The library uses a variable of type <i>struct ub_ctx</i> to keep context between calls. The user must maintain it, creating it with <code>ub_ctx_create</code> and deleting it with <code>ub_ctx_delete</code>. It can be created and deleted at any time. Creating it anew removes any previous configuration (such as trusted keys) and clears any cached results. </p>
<p> The functions are thread-safe, and a context an be used in a threaded (as well as in a non-threaded) environment. Also resolution (and validation) can be performed blocking and non-blocking (also called asynchronous). The async method returns from the call immediately, so that processing can go on, while the results become available later. </p>
<p> The functions are discussed in turn below.</p>
<h2>Functions</h2>
<dl>
<dt><code>ub_ctx_create</code></p>
<dd>Create a new context, initialised with defaults. The information from /etc/resolv.conf and /etc/hosts is not utilised by default. Use <code>ub_ctx_resolvconf</code> and <code>ub_ctx_hosts</code> to read them.</p>
<dt><code>ub_ctx_delete</code></p>
<dd>Delete validation context and free associated resources. Outstanding async queries are killed and callbacks are not called for them.</p>
<dt><code>ub_ctx_set_option</code></p>
<dd>A power-user interface that lets you specify one of the options from the config file format, see <i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5). Not all options are relevant. For some specific options, such as adding trust anchors, special routines exist. Pass the option name with the trailing &#8216;:&#8217;.</p>
<dt><code>ub_ctx_get_option</code></p>
<dd>A power-user interface that gets an option value. Some options cannot be gotten, and others return a newline separated list. Pass the option name without trailing &#8216;:&#8217;. The returned value must be <a href="/docs/linux/man/2-free/">free</a>(2)d by the caller.</p>
<dt><code>ub_ctx_config</code></p>
<dd>A power-user interface that lets you specify an unbound config file, see <i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5), which is read for configuration. Not all options are relevant. For some specific options, such as adding trust anchors, special routines exist.</p>
<dt><code>ub_ctx_set_fwd</code></p>
<dd>Set machine to forward DNS queries to, the caching resolver to use. IP4 or IP6 address. Forwards all DNS requests to that machine, which is expected to run a recursive resolver. If the proxy is not DNSSEC capable, validation may fail. Can be called several times, in that case the addresses are used as backup servers. At this time it is only possible to set configuration before the first resolve is done.</p>
<dt><code>ub_ctx_resolvconf</code></p>
<dd>By default the root servers are queried and full resolver mode is used, but you can use this call to read the list of nameservers to use from the filename given. Usually &quot;/etc/resolv.conf&quot;. Uses those nameservers as caching proxies. If they do not support DNSSEC, validation may fail. Only nameservers are picked up, the searchdomain, ndots and other settings from <i><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></i>(5) are ignored. If fname NULL is passed, &quot;/etc/resolv.conf&quot; is used (if on Windows, the system-wide configured nameserver is picked instead). At this time it is only possible to set configuration before the first resolve is done.</p>
<dt><code>ub_ctx_hosts</code></p>
<dd>Read list of hosts from the filename given. Usually &quot;/etc/hosts&quot;. When queried for, these addresses are not marked DNSSEC secure. If fname NULL is passed, &quot;/etc/hosts&quot; is used (if on Windows, etc/hosts from WINDIR is picked instead). At this time it is only possible to set configuration before the first resolve is done.</p>
<dt><code>ub_ctx_add_ta</code></p>
<dd>Add a trust anchor to the given context. At this time it is only possible to add trusted keys before the first resolve is done. The format is a string, similar to the zone-file format, [domainname] [type] [rdata contents]. Both DS and DNSKEY records are accepted.</p>
<dt><code>ub_ctx_add_ta_file</code></p>
<dd>Add trust anchors to the given context. Pass name of a file with DS and DNSKEY records in zone file format. At this time it is only possible to add trusted keys before the first resolve is done.</p>
<dt><code>ub_ctx_trustedkeys</code></p>
<dd>Add trust anchors to the given context. Pass the name of a bind-style config file with trusted-keys{}. At this time it is only possible to add trusted keys before the first resolve is done.</p>
<dt><code>ub_ctx_debugout</code></p>
<dd>Set debug and error log output to the given stream. Pass NULL to disable output. Default is stderr. File-names or using syslog can be enabled using config options, this routine is for using your own stream.</p>
<dt><code>ub_ctx_debuglevel</code></p>
<dd>Set debug verbosity for the context. Output is directed to stderr. Higher debug level gives more output.</p>
<dt><code>ub_ctx_async</code></p>
<dd>Set a context behaviour for asynchronous action. if set to true, enables threading and a call to <code>ub_resolve_async </code> creates a thread to handle work in the background. If false, a process is forked to handle work in the background. Changes to this setting after <code>ub_resolve_async </code> calls have been made have no effect (delete and re-create the context to change).</p>
<dt><code>ub_poll</code></p>
<dd>Poll a context to see if it has any new results. Do not poll in a loop, instead extract the fd below to poll for readiness, and then check, or wait using the wait routine. Returns 0 if nothing to read, or nonzero if a result is available. If nonzero, call <code>ub_process </code> to do callbacks.</p>
<dt><code>ub_wait</code></p>
<dd>Wait for a context to finish with results. Calls <code>ub_process </code> after the wait for you. After the wait, there are no more outstanding asynchronous queries.</p>
<dt><code>ub_fd</code></p>
<dd>Get file descriptor. Wait for it to become readable, at this point answers are returned from the asynchronous validating resolver. Then call the <code>ub_process</code> to continue processing.</p>
<dt><code>ub_process</code></p>
<dd>Call this routine to continue processing results from the validating resolver (when the fd becomes readable). Will perform necessary callbacks.</p>
<dt><code>ub_resolve</code></p>
<dd>Perform resolution and validation of the target name. The name is a domain name in a zero terminated text string. The rrtype and rrclass are DNS type and class codes. The result structure is newly allocated with the resulting data.</p>
<dt><code>ub_resolve_async</code></p>
<dd>Perform asynchronous resolution and validation of the target name. Arguments mean the same as for <code>ub_resolve</code> except no data is returned immediately, instead a callback is called later. The callback receives a copy of the mydata pointer, that you can use to pass information to the callback. The callback type is a function pointer to a function declared as</p>
<dd>void my_callback_function(void* my_arg, int err, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>struct ub_result*&nbsp;<wbr>result);</p>
<dd>The async_id is returned so you can (at your option) decide to track it and cancel the request if needed. If you pass a NULL pointer the async_id is not returned.</p>
<dt><code>ub_cancel</code></p>
<dd>Cancel an async query in progress. This may return an error if the query does not exist, or the query is already being delivered, in that case you may still get a callback for the query.</p>
<dt><code>ub_resolve_free</code></p>
<dd>Free struct ub_result contents after use.</p>
<dt><code>ub_strerror</code></p>
<dd>Convert error value from one of the unbound library functions to a human readable string.</p>
<dt><code>ub_ctx_print_local_zones</code></p>
<dd>Debug printout the local authority information to debug output.</p>
<dt><code>ub_ctx_zone_add</code></p>
<dd>Add new zone to local authority info, like local-zone <i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5) statement.</p>
<dt><code>ub_ctx_zone_remove</code></p>
<dd>Delete zone from local authority info.</p>
<dt><code>ub_ctx_data_add</code></p>
<dd>Add resource record data to local authority info, like local-data <i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5) statement.</p>
<dt><code>ub_ctx_data_remove</code></p>
<dd>Delete local authority data from the name given.</dl>
<h2>Result Data Structure</h2>
<p>The result of the DNS resolution and validation is returned as <i>struct ub_result</i>. The result structure contains the following entries. </p>
<pre> struct ub_result {
 char* qname; /* text string, original question */
 int qtype; /* type code asked for */
 int qclass; /* class code asked for */
 char** data; /* array of rdata items, NULL terminated*/
 int* len; /* array with lengths of rdata items */
 char* canonname; /* canonical name of result */
 int rcode; /* additional error code in case of no data */
 void* answer_packet; /* full network format answer packet */
 int answer_len; /* length of packet in octets */
 int havedata; /* true if there is data */
 int nxdomain; /* true if nodata because name does not exist */
 int secure; /* true if result is secure */
 int bogus; /* true if a security failure happened */
 char* why_bogus; /* string with error if bogus */
 int ttl; /* number of seconds the result is valid */
 };</pre>
<p>If both secure and bogus are false, security was not enabled for the domain of the query.</p>
<h2>Return Values</h2>
<p>Many routines return an error code. The value 0 (zero) denotes no error happened. Other values can be passed to <code>ub_strerror</code> to obtain a readable error string. <code>ub_strerror</code> returns a zero terminated string. <code>ub_ctx_create</code> returns NULL on an error (a malloc failure). <code>ub_poll</code> returns true if some information may be available, false otherwise. <code>ub_fd</code> returns a file descriptor or -1 on error.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5), <i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8).</p>
<h2>Authors</h2>
<p><code>Unbound</code> developers are mentioned in the CREDITS file in the distribution.</p>
