---
title: "udns(3)"
name: "udns"
section: "3"
letter: "u"
url: "/docs/linux/man/3-udns/"
description: "udns – stub DNS resolver library"
---

<p>udns &#8211; stub DNS resolver library</p>
<h2>Synopsys</h2>
<pre>#include &lt;udns.h&gt;
struct <code>dns_ctx</code>;
struct <code>dns_query</code>;
extern struct dns_ctx <code>dns_defctx</code>;
struct dns_ctx *<i>ctx</i>;
typedef void <code>dns_query_fn</code>(<i>ctx</i>, void *<i>result</i>, void *<i>data</i>);
typedef int
<code>dns_parse_fn</code>(const unsigned char *<i>qnd</i>,
 const unsigned char *<i>pkt</i>,
 const unsigned char *<i>cur</i>,
 const unsigned char *<i>end</i>,
 void **<i>resultp</i>);
<code>cc</code> ... -l<code>udns</code></pre>
<h2>Description</h2>
<p>The DNS library, <code>udns</code>, implements thread-safe stub DNS resolver functionality, which may be used both traditional, syncronous way and asyncronously, with application-supplied event loop. While DNS works with both TCP and UDP, performing UDP query first and if the result does not fit in UDP buffer (512 bytes max for original DNS protocol), retrying the query over TCP, the library uses UDP only, but uses EDNS0 (RFC2671) extensions which allows larger UDP buffers. The library uses single UDP socket to perform all operations even when asking multiple nameservers. This way, it is very simple to use the library in asyncronous event-loop applications: an application should add only single socket to the set of filedescriptors it monitors for I/O. The library uses two main objects, <i>resolver context</i> of type <code>struct dns_ctx</code>, and <i>query structure</i> of type <code>struct dns_query</code>, both are opaque for an application. Resolver context holds global information about the resolver, such as list of nameservers to use, list of active requests and the like. Query objects holds information about a single DNS query in progress and are allocated/processed/freed by the library. Pointer to query structure may be treated as an identifier of an in-progress query and may be used to cancel the asyncronous query or to wait for it to complete. Asyncronous interface works as follows. An application initializes resolver context, submits any number of queries for it using one of supplied <code>dns_submit_</code><i>XXX</i>() routines (each return the query identifier as pointer to query structure), waits for input on the UDP socket used by the library, and gives some control to the library by calling <code>dns_ioevent</code>() and <code>dns_timeouts</code>() routines when appropriate. The library performs all necessary processing and executes application supplied callback routine when a query completes (either successefully or not), giving it the result if any, pointer to the resolver context (from which completion status may be obtained), and the data pointer supplied by an application when the query has been submitted. When submitting a query, an application requests how to handle the reply &#8212; to either return raw DNS reply packet for its own low-level processing, or it may provide an address of <i>parsing routine</i> of type <code>dns_parse_fn</code> to perform conversion of on-wire format into easy to use data structure (the library provides parsing routines for several commonly used resource record types, as well as type-safe higher-level inteface that requests parsing automatically). The I/O monitoring and timeout handling may be either traditional select() or poll() based, or any callback-driven technique may be used. Additionally, the library provides traditional syncronous interface, which may be intermixed with asyncronous calls (during syncronous query processing, other asyncronous queries for the same resolver context continued to be processed as usual). An application uses one of numerous <code>dns_resolve_</code><i>XXX</i>() routines provided by the library to perform a query. As with asyncronous interface, an application may either request to return raw DNS packet or type-specific data structure by providing the parsing routine to handle the reply. Every routine from <code>dns_resolve_</code><i>XXX</i>() series return pointer to result or NULL in case of any error. Query completion status (or length of the raw DNS packet) is available from the resolver context using <code>dns_status</code>() routine, the same way as for the asyncronous interface. Internally, library uses on-wire format of domain names, referred to as <i>DN format</i> in this manual page. This is a series of domain <i>labels</i> whith preceeding length byte, terminated by zero-length label wich is integral part of the DN format. There are several routines provided to convert from traditional asciiz string to DN and back. Higher-level type-specific query interface hides the DN format from an application. </p>
<h2>Common Definitions</h2>
<p>Every DNS Resource Record (RR) has a <i>type</i> and a <i>class</i>. The library defines several integer constants, <code>DNS_C_</code><i>XXX</i> and <code>DNS_T_</code><i>XXX</i>, to use as symbolic names for RR classes and types, such as <code>DNS_C_IN</code> for Internet class, <code>DNS_T_A</code> for IPv4 address record type and so on. See udns.h header file for complete list of all such constants. </p>
<p> The following constants are defined in udns.h header file:</p>
<dl>
<dt><code>DNS_MAXDN</code> (255 bytes)</p>
<dd>Maximum length of the domain name in internal (on-wire) DN format.</p>
<dt><code>DNS_MAXLABEL</code> (63 bytes)</p>
<dd>Maximum length of a single label in DN format.</p>
<dt><code>DNS_MAXNAME</code> (1024 bytes)</p>
<dd>Maximum length of asciiz format of a domain name.</p>
<dt><code>DNS_HSIZE</code> (12 bytes)</p>
<dd>Size of header in DNS packet.</p>
<dt><code>DNS_PORT</code> (53)</p>
<dd>Default port to use when contacting a DNS server.</p>
<dt><code>DNS_MAXSERV</code> (6 servers)</p>
<dd>Maximum number of DNS servers to use.</p>
<dt><code>DNS_MAXPACKET</code> (512 bytes)</p>
<dd>Maximum length of DNS UDP packet as specified by original DNS protocol</p>
<dt><code>DNS_EDNS0PACKET</code> (4096 bytes)</p>
<dd>Default length of DNS UDP packet (with EDNS0 extensions) the library uses. Note that recursive nameservers usually resides near the client asking them to resolve names, e.g. on the same LAN segment or even on the same host, so UDP packet fragmentation isn&#8217;t a problem in most cases. Note also that the size of actual packets will be as many bytes as actual reply size requires, which is smaller than this value in almost all cases. </p>
</dl>
<p> Additionally, several constants are defined to simplify work with raw DNS packets, such as DNS response codes (<code>DNS_R_</code><i>XXX</i>), DNS header layout (<code>DNS_H_</code><i>XXX</i>) and others. Again, see udns.h for complete list. Library error codes (<code>DNS_E_</code><i>XXX</i>) are described later in this manual page.</p>
<h2>Resolver Context</h2>
<p>Resolver context, of type <code>struct dns_ctx</code>, is an object which is opaque to an application. Several routines provided by the library to initialize, copy and free resolver contexts. Most other high-level routines in this library expects a pointer to resolver context, <i>ctx</i>, as the first argument. There is a default resolver context available, named <code>dns_defctx</code>. When the context pointer <i>ctx</i> passed to a routine is NULL, <code>dns_defctx</code> is used. Several resolver contexts may be active at the same time, for example, when an application is multi-threaded and each thread uses resolver. </p>
<p> In order to use the library, an application should initialize and open one or more resolver context objects. These are two separate actions, performed by <code>dns_init</code>() (or <code>dns_reset</code>()), and <code>dns_open</code>(). Between the two calls, an application is free to pefrorm additional initialisation, such as setting custom nameservers, options or domain search lists. Optionally, in case no additional custom initialisation is required, <code>dns_init</code>() may open the context if <i>do_open</i> argument (see below) is non-zero. </p>
<p> When initializing resolver context, the library uses information from system file /etc/resolv.conf (see <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5)), consults environment variables <code>$LOCALDOMAIN</code>, <code>$NSCACHEIP</code>, <code>$NAMESERVERS</code> and <code>$RES_OPTIONS</code>, and local host name to obtain list of local nameservers, domain name search list and various resolver options. </p>
<p> The following routines to initialize resolver context are available: </p>
<pre>void <code>dns_reset</code>(<i>ctx</i>)
int <code>dns_init</code>(<i>ctx</i>, int <i>do_open</i>)</pre>
<dl>
<dd><code>dns_reset</code>() resets a given resolver context to default values, preparing it to be opened by <code>dns_open</code>(). It is ok to call this routine against opened and active context &#8211; all active queries will be dropped, sockets will be closed and so on. This routine does not initialize any parameters from system configuration files, use <code>dns_init</code>() for this. There&#8217;s no error return &#8211; operation always succeeds. <code>dns_init</code>() does everything <code>dns_reset</code>() does, plus initializes various parameters of the context according to system configuration and process environment variables. If <i>do_open</i> is non-zero, <code>dns_init</code>() calls <i>dns_open</i>(), so that the whole library initialisation is performed in a single step.</dl>
<pre>struct dns_ctx *<code>dns_new</code>(struct dns_ctx *<i>copy</i>)
void <code>dns_free</code>(<i>ctx</i>)</pre>
<dl>
<dd><code>dns_new</code>() allocates new resolver context and copies all parameters for a given resolver context <i>copy</i>, or default context if <i>copy</i> is NULL, and returns pointer to the newly allocated context. The context being copied should be initialized. <code>dns_new</code>() may fail if there&#8217;s no memory available to make a copy of <i>copy</i>, in which case the routine will return NULL pointer. <code>dns_free</code>() is used to close assotiated socket and free resolver context resources and cancelling (abandoming) all active queries assotiated with it. It&#8217;s an error to free <code>dns_defctx</code>, only dynamically allocated contexts returned by <code>dns_new</code>() are allowed to be freed by <code>dns_free</code>().</dl>
<pre>int <code>dns_add_serv</code>(<i>ctx</i>, const char *<i>servaddr</i>)
int <code>dns_add_serv_s</code>(<i>ctx</i>, const struct sockaddr *<i>sa</i>)
int <code>dns_add_srch</code>(<i>ctx</i>, const char *<i>srch</i>)</pre>
<dl>
<dd>Add an element to list of nameservers (<code>dns_add_serv</code>(), as asciiz-string <i>servaddr</i> with an IP address of the nameserver, and <code>dns_add_serv_s</code>(), as initialized socket address <i>sa</i>), or search list (<code>dns_add_srch</code>(), as a pointer to domain name) for the given context <i>ctx</i>. If the last argument is a NULL pointer, the corresponding list (search or nameserver) is reset instead. Upon successeful completion, each routine returns new number of elements in the list in question. On error, negative value is returned and global variable <code>errno</code> is set appropriately. It is an error to call any of this functions if the context is opened (after <code>dns_open</code>() or <code>dns_init</code>() with non-zero argument).</dl>
<pre>int <code>dns_set_opts</code>(<i>ctx</i>, const char *<i>opts</i>)</pre>
<dl>
<dd>set resolver context options from <i>opts</i> string, in the same way as processing <code>options</code> statement in resolv.conf and <code>$RES_OPTIONS</code> environment variable. Return number of unrecognized/invalid options found (all recognized and valid options gets processed).</dl>
<pre>void <code>dns_set_opt</code>(<i>ctx</i>, int <i>opt</i>, <i>val</i>)</pre>
<dl>
<dd><code>TODO</code> The <i>flags</i> argument is a bitmask with the following bits defined:</p>
<dl>
<dt><code>DNS_NOSRCH</code></p>
<dd>do not perform domain name search in search list.</p>
<dt><code>DNS_NORD</code></p>
<dd>do not request recursion when performing queries (i.e. don&#8217;t set RD flag in querues).</p>
<dt><code>DNS_AAONLY</code></p>
<dd>request authoritative answers only (i.e. set AA flag in queries).</dl>
</dl>
<pre>int <code>dns_open</code>(<i>ctx</i>)
int <code>dns_sock</code>(const <i>ctx</i>)
void <code>dns_close</code>(<i>ctx</i>)</pre>
<dl>
<dd><code>dns_open</code>() opens the UDP socket used for queries if not already open, and return assotiated filedescriptor (or negative value in case of error). Before any query can be submitted, the context should be opened using this routine. And before opening, the context should be initialized. <code>dns_sock</code>() return the UDP socket if open, or -1 if not. <code>dns_close</code>() closes the UDP socket if it was open, and drops all active queries if any.</dl>
<pre>int <code>dns_active</code>(const <i>ctx</i>)</pre>
<dl>
<dd>return number of active queries queued for the given context <i>ctx</i>, or zero if none.</dl>
<pre>int <code>dns_status</code>(const <i>ctx</i>)</pre>
<dl>
<dd>return status code from last operation. When using syncronous interface, this is the query completion status of the last query. With asyncronous interface, from within the callback routine, this is the query completion status of the query for which the callback is being called. When query submission fails, this is the error code indicating failure reason. All error codes are negative and are represented by <code>DNS_E_</code><i>XXX</i> constants described below.</dl>
<pre>void <code>dns_ioevent</code>(<i>ctx</i>, time_t <i>now</i>)</pre>
<dl>
<dd>this routine may be called by an application to process I/O events on the UDP socket used by the library, as returned by <code>dns_sock</code>(). The routine tries to receive incoming UDP datagram from the socket and process it. The socket is set up to be non-blocking, so it is safe to call the routine even if there&#8217;s no data to read. The routine will process as many datagrams as are queued for the socket, so it is safe to use it with either level-triggered or edge-triggered I/O monitoring model. The <i>now</i> argument is either a current time as returned by <code>time</code>(), or 0, in which case the routine will obtain current time by it&#8217;s own.</dl>
<pre>int <code>dns_timeouts</code>(<i>ctx</i>, int <i>maxwait</i>, time_t <i>now</i>)</pre>
<dl>
<dd>process any pending timeouts and return number of secounds from current time (<i>now</i> if it is not 0) to the time when the library wants the application to pass it control to process more queued requests. In case when there are no requests pending, this time is -1. The routine will not request a time larger than <i>maxwait</i> secounds if it is greather or equal to zero. If <i>now</i> is 0, the routine will obtain current time by it&#8217;s own; when it is not 0, it should contain current time as returned by <code>time</code>().</dl>
<pre>typedef void <code>dns_utm_fn</code>(<i>ctx</i>, int <i>timeout</i>, void *<i>data</i>)
void <code>dns_set_tmcbck</code>(<i>ctx</i>, dns_utm_fn *<i>utmfn</i>, void *<i>data</i>)</pre>
<dl>
<dd>An application may use custom callback-based I/O multiplexing mechanism. Usually such a mechanism have concept of a <i>timer</i>, and an ability to register a timer event in a form of a callback routine which will be executed after certain amount of time. In order to use such an event mechanism, udns provides an ability to register and de-register timer events necessary for internal processing using whatever event mechanism an application uses. For this to work, it is possible to assotiate a pointer to a routine that will perform necessary work for (de)registering timer events with a given resolver context, and udns will call that routine at appropriate times. Prototype of such a routine is shown by <code>dns_utm_fn</code> typedef above. Libudns assotiates single timer with resolver context. User-supplied <i>utmfn</i> routine will be called by the library with the following arguments:</p>
<dl>
<dt><i>ctx</i> == NULL</p>
<dd>delete user timer, at context free time or when an application changes user timer request routine using <code>dns_set_tmcbck</code>();</p>
<dt><i>ctx</i> != NULL, <i>timeout</i> &lt; 0</p>
<dd>don&#8217;t fire timer anymore, when there are no active requests;</p>
<dt><i>ctx</i> != NULL, <i>timeout</i> == 0</p>
<dd>fire timer at the next possibility, but not immediately;</p>
<dt><i>ctx</i> != NULL, <i>timeout</i> &gt; 0</p>
<dd>fire timer after <i>timeout</i> seconds after now.</dl>
<p> The <i>data</i> argument passed to the routine will be the same as passed to <code>dns_set_tmcbck</code>(). </p>
<p> When a timer expires, an application should call <code>dns_timeouts</code>() routine (see below). Non-callback timer usage is provided too.</dl>
<p> <code>XXXX TODO: some more resolver context routines, like dns_set_dbgfn() etc.</code></p>
<h2>Query Interface</h2>
<p>There are two ways to perform DNS queries: traditional syncronous way, when udns performs all the necessary processing and return control to the application only when the query completes, and asyncronous way, when an application submits one or more queries to the library using given resolver context, and waits for completion by monitoring filedescriptor used by library and calling library routines to process input on that filedescriptor. Asyncronous mode works with callback routines: an application supplies an address of a routine to execute when the query completes, and a data pointer, which is passed to the callback routine. </p>
<p> Queries are submitted to the library in a form of <code>struct dns_query</code>. To perform asyncronous query, an application calls one of the <code>dns_submit_</code><i>XXX</i>() rounines, and provides necessary information for a callback, together with all the query parameters. When the query completes, library will call application-supplied callback routine, giving it the resolver context (wich holds query completion status), dynamically allocated result (which will be either raw DNS packet or, if applicatin requested parsing the result by specifying non-NULL parse routine, ready-to-use type-specific structure), and a data pointer provided by an application when it submitted the query. It is the application who&#8217;s responsible for freeing the result memory. </p>
<p> Generic query callback routine looks like this: </p>
<pre>typedef void
<code>dns_query_fn</code>(<i>ctx</i>, void *<i>result</i>, void *<i>data</i>)</pre>
<p>Type-specific query interface expects similar form of callback routine with the only difference in type of <code>result</code> argument, which will be pointer to specific data structure (decoded reply) instead of this void pointer to raw DNS packet data. </p>
<p> Result parsing routine looks like this: </p>
<pre>typedef int
<code>dns_parse_fn</code>(const unsigned char *<i>qdn</i>,
 const unsigned char *<i>pkt</i>,
 const unsigned char *<i>cur</i>,
 const unsigned char *<i>end</i>,
 void **<i>resultp</i>);</pre>
<p>When called by the library, the arguments are as follows: <i>pkt</i> points to the start of the packet received; <i>end</i> points past the end of the packet received; <i>cur</i> points past the query DN in the query section of the packet; <i>qdn</i> points to the original query DN. The routine should allocate a single buffer to hold the result, parse the reply filling in the buffer, and return the buffer using <i>resultp</i> argument. It returns 0 in case of error, or udns error code (<code>DNS_E_</code><i>XXX</i> constants) in case of error. Note that by the time when the parse routine is called by the library, packet is already verified to be a reply to the original query, by matching query DN, query class and query type. </p>
<p> Type-specific query inteface supplies necessary parsing routines automatically. </p>
<p> In case of error, query completion status as returned by <code>dns_status</code>(<i>ctx</i>), will contain one of the following values:</p>
<dl>
<dt>positive value</p>
<dd>length of raw DNS packet if parsing is not requested.</p>
<dt>0</p>
<dd>the query was successeful and the <i>reply</i> points to type-specific data structure.</p>
<dt><code>DNS_E_TEMPFAIL</code></p>
<dd>temporary error, the resolver nameserver was not able to process our query or timed out.</p>
<dt><code>DNS_E_PROTOCOL</code></p>
<dd>protocol error, a nameserver returned malformed reply.</p>
<dt><code>DNS_E_NXDOMAIN</code></p>
<dd>the domain name does not exist.</p>
<dt><code>DNS_E_NODATA</code></p>
<dd>there is no data of requested type found.</p>
<dt><code>DNS_E_NOMEM</code></p>
<dd>out of memory while processing request.</p>
<dt><code>DNS_E_BADQUERY</code></p>
<dd>some aspect of the query (most common is the domain name in question) is invalid, and the library can&#8217;t even start a query. </p>
</dl>
<p> Library provides two series of routines which uses similar interface &#8212; one for asyncronous queries and another for syncronous queries. There are two general low-level routines in each series to submit (asyncronous interface) and resolve (syncronous interface) queries, as well as several type-specific routines with more easy-to-use interfaces. To submit an asyncronous query, use one of <code>dns_submit_</code><i>XXX</i>() routine, each of which accepts query parameters, pointers to callback routine and to callback data, and optional current time hint. Note type-specific <code>dns_submit_</code><i>XXX</i>() routines expects specific type of the callback routine as well, which accepts reply as a pointer to corresponding structure, not a void pointer). Every <code>dns_submit_</code><i>XXX</i>() routine return pointer to internal query structure of type struct dns_query, used as an identifier for the given query. </p>
<p> To resolve a query syncronously, use one of <code>dns_resolve_</code><i>XXX</i>() routines, which accepts the same query parameters (but not the callback pointers) as corresponding <code>dns_submit_</code><i>XXX</i>(), and return the query result, which is the same as passed to the callback routine in case of asyncronous interface. </p>
<p> In either case, the result memory (if the query completed successefully) is dynamically allocated and should be freed by an application. If the query failed for any reason, the result will be NULL, and error status will be available from <code>dns_status</code>(<i>ctx</i>) routine as shown above. </p>
<pre>struct dns_query *
<code>dns_submit_dn</code>(<i>ctx</i>,
 const unsigned char *<i>dn</i>, <i>qcls</i>, <i>qtyp</i>, <i>flags</i>,
 <i>parse</i>, <i>cbck</i>, <i>data</i>)
struct dns_query *
<code>dns_submit_p</code>(<i>ctx</i>,
 const char *<i>name</i>, <i>qcls</i>, <i>qtyp</i>, <i>flags</i>,
 <i>parse</i>, <i>cbck</i>, <i>data</i>)
 enum dns_class <i>qcls</i>;
 enum dns_type <i>qtyp</i>;
 int <i>flags</i>;
 dns_parse_fn *<i>parse</i>;
 dns_query_fn *<i>cbck</i>;
 void *<i>data</i>;</pre>
<dl>
<dd>submit a query for processing for the given resolver context <i>ctx</i>. Two routines differs only in 3rd argument, which is domain name in DN format (<i>dn</i>) or asciiz string (<i>name</i>). The query will be performed for the given domain name, with type <i>qtyp</i> in class <i>qcls</i>, using option bits in <i>flags</i>, using RR parsing routine pointed by <i>parse</i> if not-NULL, and upon completion, <i>cbck</i> function will be called with the <i>data</i> argument. In case of successeful query submission, the routine return pointer to internal query structure which may be treated as an identifier of the query as used by the library, and may be used as an argument for <code>dns_cancel</code>() routine. In case of error, NULL will be returned, and context error status (available using <i>dns_status</i>() routine) will be set to corresponding error code, which in this case may be DNS_E_BADQUERY if the <i>name</i> of <i>dn</i> is invalid, DNS_E_NOMEM if there&#8217;s no memory available to allocate query structure, or DNS_E_TEMPFAIL if an internal error occured.</dl>
<pre>void *<code>dns_resolve_dn</code>(<i>ctx</i>,
 const unsigned char *<i>dn</i>, <i>qcls</i>, <i>qtyp</i>, <i>flags</i>, <i>parse</i>);
void *<code>dns_resolve_p</code>(<i>ctx</i>,
 const char *<i>name</i>, <i>qcls</i>, <i>qtyp</i>, <i>flags</i>, <i>parse</i>)
 enum dns_class <i>qcls</i>;
 enum dns_type <i>qtyp</i>;
 int <i>flags</i>;
 dns_parse_fn *<i>parse</i>; </pre>
<dl>
<dd>syncronous interface. The routines perform all the steps necessary to resolve the given query and return the result. If there&#8217;s no positive result for any reason, all the routines return NULL, and set context error status (available using <code>dns_status</code>() routine) to indicate the error code. If the query was successeful, context status code will contain either the length of the raw DNS reply packet if <i>parse</i> argument was NULL (in which case the return value is pointer to the reply DNS packet), or 0 (in which case the return value is the result of <i>parse</i> routine). If the query successeful (return value is not NULL), the memory returned was dynamically allocated by the library and should be free()d by application after use.</dl>
<pre>void *<code>dns_resolve</code>(<i>ctx</i>, struct dns_query *<i>q</i>)</pre>
<dl>
<dd>wait for the given query <i>q</i>, as returned by one of <code>dns_submit_</code><i>XXX</i>() routines, for completion, and return the result. The callback routine will not be called for this query. After completion, the query identifier <i>q</i> is not valid. Both <code>dns_resolve_dn</code>() and <code>dns_resolve_p</code>() are just wrappers around corresponding submit routines and this <code>dns_resolve</code>() routine.</dl>
<pre>void <code>dns_cancel</code>(<i>ctx</i>, struct dns_query *<i>q</i>)</pre>
<dl>
<dd>cancel an active query <i>q</i>, without calling a callback routine. After completion, the query identifier <i>q</i> is not valid.</dl>
<h2>Type-Specific Queries</h2>
<p>In addition to the generic low-level query interface, the library provides a set of routines to perform specific queries in a type-safe manner, as well as parsers for several well-known resource record types. The library implements high-level interface for A, AAAA, PTR, MX and TXT records and DNSBL and RHSBL functionality. These routines returns specific types as result of a query, instead of raw DNS packets. The following types and routines are available. </p>
<pre>struct <code>dns_rr_null</code> {
 char *<code>dnsn_qname</code>; /* original query name */
 char *<code>dnsn_cname</code>; /* canonical name */
 unsigned <code>dnsn_ttl</code>; /* Time-To-Live (TTL) value */
 int <code>dnsn_nrr</code>; /* number of records in the set */
};</pre>
<p>NULL RR set, used as a base for all other RR type structures. Every RR structure as used by the library have four standard fields as in struct&nbsp;<wbr><code>dns_rr_null</code>.</p>
<h3>IN A Queries</h3>
<pre>struct <code>dns_rr_a4</code> { /* IN A RRset */
 char *<code>dnsa4_qname</code>; /* original query name */
 char *<code>dnsa4_cname</code>; /* canonical name */
 unsigned <code>dnsa4_ttl</code>; /* Time-To-Live (TTL) value */
 int <code>dnsa4_nrr</code>; /* number of addresses in the set */
 struct in_addr <code>dnsa4_addr</code>[]; /* array of addresses */
};
typedef void
 <code>dns_query_a4_fn</code>(<i>ctx</i>, struct dns_rr_a4 *<i>result</i>, <i>data</i>)
dns_parse_fn <code>dns_parse_a4;
struct dns_query *
dns_submit_a4(</code><i>ctx</i>, const char *<i>name</i>, int <i>flags</i>,
 dns_query_a4_fn *<i>cbck</i>, <i>data</i>);
struct dns_rr_a4 *
<code>dns_resolve_a4(</code><i>ctx</i>, const char *<i>name</i>, int <i>flags</i>);</pre>
<p>The <code>dns_rr_a4</code> structure holds a result of an <code>IN A</code> query, which is an array of IPv4 addresses. Callback routine for IN A queries expected to be of type <code>dns_query_a4_fn</code>, which expects pointer to <code>dns_rr_a4</code> structure as query result instead of raw DNS packet. The <code>dns_parse_a4</code>() is used to convert raw DNS reply packet into <code>dns_rr_a4</code> structure (it is used internally and may be used directly too with generic query interface). Routines <code>dns_submit_a4</code>() and <code>dns_resolve_a4</code>() are used to perform A IN queries in a type-safe manner. The <i>name</i> parameter is the domain name in question, and <i>flags</i> is query flags bitmask, with one bit, DNS_NOSRCH, of practical interest (if the <i>name</i> is absolute, that is, it ends up with a dot, DNS_NOSRCH flag will be set automatically).</p>
<h3>IN AAAA Queries</h3>
<pre>struct <code>dns_rr_a6</code> { /* IN AAAA RRset */
 char *<code>dnsa6_qname</code>; /* original query name */
 char *<code>dnsa6_cname</code>; /* canonical name */
 unsigned <code>dnsa6_ttl</code>; /* Time-To-Live (TTL) value */
 int <code>dnsa6_nrr</code>; /* number of addresses in the set */
 struct in6_addr <code>dnsa6_addr</code>[]; /* array of addresses */
};
typedef void
 <code>dns_query_a6_fn</code>(<i>ctx</i>, struct dns_rr_a6 *<i>result</i>, <i>data</i>)
dns_parse_fn <code>dns_parse_a6;
struct dns_query *
dns_submit_a6(</code><i>ctx</i>, const char *<i>name</i>, int <i>flags</i>,
 dns_query_a6_fn *<i>cbck</i>, <i>data</i>);
struct dns_rr_a6 *
<code>dns_resolve_a6(</code><i>ctx</i>, const char *<i>name</i>, int <i>flags</i>);</pre>
<p>The <code>dns_rr_a6</code> structure holds a result of an <code>IN AAAA</code> query, which is an array of IPv6 addresses. Callback routine for IN AAAA queries expected to be of type <code>dns_query_a6_fn</code>, which expects pointer to <code>dns_rr_a6</code> structure as query result instead of raw DNS packet. The <code>dns_parse_a6</code>() is used to convert raw DNS reply packet into <code>dns_rr_a6</code> structure (it is used internally and may be used directly too with generic query interface). Routines <code>dns_submit_a6</code>() and <code>dns_resolve_a6</code>() are used to perform AAAA IN queries in a type-safe manner. The <i>name</i> parameter is the domain name in question, and <i>flags</i> is query flags bitmask, with one bit, DNS_NOSRCH, of practical interest (if the <i>name</i> is absolute, that is, it ends up with a dot, DNS_NOSRCH flag will be set automatically).</p>
<h3>IN PTR Queries</h3>
<pre>struct <code>dns_rr_ptr</code> { /* IN PTR RRset */
 char *<code>dnsptr_qname</code>; /* original query name */
 char *<code>dnsptr_cname</code>; /* canonical name */
 unsigned <code>dnsptr_ttl</code>; /* Time-To-Live (TTL) value */
 int <code>dnsptr_nrr</code>; /* number of domain name pointers */
 char *<code>dnsptr_ptr</code>[]; /* array of domain name pointers */
};
typedef void
 <code>dns_query_ptr_fn</code>(<i>ctx</i>, struct dns_rr_ptr *<i>result</i>, <i>data</i>)
dns_parse_fn <code>dns_parse_ptr;
struct dns_query *
dns_submit_a4ptr(</code><i>ctx</i>, const struct in_addr *<code>addr</code>,
 dns_query_ptr_fn *<i>cbck</i>, <i>data</i>);
struct dns_rr_ptr *
<code>dns_resolve_a4ptr(</code><i>ctx</i>, const struct in_addr *<code>addr</code>);
struct dns_query *
<code>dns_submit_a6ptr(</code><i>ctx</i>, const struct in6_addr *<code>addr</code>,
 dns_query_ptr_fn *<i>cbck</i>, <i>data</i>);
struct dns_rr_ptr *
<code>dns_resolve_a6ptr(</code><i>ctx</i>, const struct in6_addr *<code>addr</code>);</pre>
<p>The <code>dns_rr_ptr</code> structure holds a result of an IN PTR query, which is an array of domain name pointers for a given IPv4 or IPv6 address. Callback routine for IN PTR queries expected to be of type <code>dns_query_ptr_fn</code>, which expects pointer to <code>dns_rr_ptr</code> structure as query result instead of raw DNS packet. The <code>dns_parse_ptr</code>() is used to convert raw DNS reply packet into <code>dns_rr_ptr</code> structure (it is used internally and may be used directly too with generic query interface). Routines <code>dns_submit_a4ptr</code>() and <code>dns_resolve_a4ptr</code>() are used to perform IN PTR queries for IPv4 addresses in a type-safe manner. Routines <code>dns_submit_a6ptr</code>() and <code>dns_resolve_a6ptr</code>() are used to perform IN PTR queries for IPv6 addresses.</p>
<h3>IN MX Queries</h3>
<pre>struct <code>dns_mx</code> { /* single MX record */
 int <code>priority</code>; /* priority value of this MX */
 char *<code>name</code>; /* domain name of this MX */
};
struct <code>dns_rr_mx</code> { /* IN MX RRset */
 char *<code>dnsmx_qname</code>; /* original query name */
 char *<code>dnsmx_cname</code>; /* canonical name */
 unsigned <code>dnsmx_ttl</code>; /* Time-To-Live (TTL) value */
 int <code>dnsmx_nrr</code>; /* number of mail exchangers in the set */
 struct dns_mx <code>dnsmx_mx</code>[]; /* array of mail exchangers */
};
typedef void
 <code>dns_query_mx_fn</code>(<i>ctx</i>, struct dns_rr_mx *<i>result</i>, <i>data</i>)
dns_parse_fn <code>dns_parse_mx;
struct dns_query *
dns_submit_mx(</code><i>ctx</i>, const char *<i>name</i>, int <i>flags</i>,
 dns_query_mx_fn *<i>cbck</i>, <i>data</i>);
struct dns_rr_mx *
<code>dns_resolve_mx(</code><i>ctx</i>, const char *<i>name</i>, int <i>flags</i>);</pre>
<p>The <code>dns_rr_mx</code> structure holds a result of an IN MX query, which is an array of mail exchangers for a given domain. Callback routine for IN MX queries expected to be of type <code>dns_query_mx_fn</code>, which expects pointer to <code>dns_rr_mx</code> structure as query result instead of raw DNS packet. The <code>dns_parse_mx</code>() is used to convert raw DNS reply packet into <code>dns_rr_mx</code> structure (it is used internally and may be used directly too with generic query interface). Routines <code>dns_submit_mx</code>() and <code>dns_resolve_mx</code>() are used to perform IN MX queries in a type-safe manner. The <i>name</i> parameter is the domain name in question, and <i>flags</i> is query flags bitmask, with one bit, DNS_NOSRCH, of practical interest (if the <i>name</i> is absolute, that is, it ends up with a dot, DNS_NOSRCH flag will be set automatically).</p>
<h3>TXT Queries</h3>
<pre>struct <code>dns_txt</code> { /* single TXT record */
 int <code>len</code>; /* length of the text */
 unsigned char *<code>txt</code>; /* pointer to the text */
};
struct <code>dns_rr_txt</code> { /* TXT RRset */
 char *<code>dnstxt_qname</code>; /* original query name */
 char *<code>dnstxt_cname</code>; /* canonical name */
 unsigned <code>dnstxt_ttl</code>; /* Time-To-Live (TTL) value */
 int <code>dnstxt_nrr</code>; /* number of text records in the set */
 struct dns_txt <code>dnstxt_txt</code>[]; /* array of TXT records */
};
typedef void
 <code>dns_query_txt_fn</code>(<i>ctx</i>, struct dns_rr_txt *<i>result</i>, <i>data</i>)
dns_parse_fn <code>dns_parse_txt;
struct dns_query *
dns_submit_txt(</code><i>ctx</i>, const char *<i>name</i>, enum dns_class <i>qcls</i>,
 int <i>flags</i>, dns_query_txt_fn *<i>cbck</i>, <i>data</i>);
struct dns_rr_txt *
<code>dns_resolve_txt(</code><i>ctx</i>, const char *<i>name</i>,
 enum dns_class <i>qcls</i>, int <i>flags</i>);</pre>
<p>The <code>dns_rr_txt</code> structure holds a result of a TXT query, which is an array of text records for a given domain name. Callback routine for TXT queries expected to be of type <code>dns_query_txt_fn</code>, which expects pointer to <code>dns_rr_txt</code> structure as query result instead of raw DNS packet. The <code>dns_parse_txt</code>() is used to convert raw DNS reply packet into <code>dns_rr_txt</code> structure (it is used internally and may be used directly too with generic query interface). Routines <code>dns_submit_txt</code>() and <code>dns_resolve_txt</code>() are used to perform IN MX queries in a type-safe manner. The <i>name</i> parameter is the domain name in question, and <i>flags</i> is query flags bitmask, with one bit, DNS_NOSRCH, of practical interest (if the <i>name</i> is absolute, that is, it ends up with a dot, DNS_NOSRCH flag will be set automatically). Note that each TXT string is represented by <code>struct dns_txt</code>, while zero-terminated (and the len field of the structure does not include the terminator), may contain embedded null characters &#8212; content of TXT records is not interpreted by the library in any way.</p>
<h3>SRV Queries</h3>
<pre>struct <code>dns_srv</code> { /* single SRV record */
 int <code>priority</code>; /* priority of the record */
 int <code>weight</code>; /* weight of the record */
 int <code>port</code>; /* the port number to connect to */
 char *<code>name</code>; /* target host name */
};
struct <code>dns_rr_srv</code> { /* SRV RRset */
 char *<code>dnssrv_qname</code>; /* original query name */
 char *<code>dnssrv_cname</code>; /* canonical name */
 unsigned <code>dnssrv_ttl</code>; /* Time-To-Live (TTL) value */
 int <code>dnssrv_nrr</code>; /* number of text records in the set */
 struct dns_srv <code>dnssrv_srv</code>[]; /* array of SRV records */
};
typedef void
 <code>dns_query_srv_fn</code>(<i>ctx</i>, struct dns_rr_srv *<i>result</i>, <i>data</i>)
dns_parse_fn <code>dns_parse_srv;
struct dns_query *
dns_submit_srv(</code><i>ctx</i>, const char *<i>name</i>, const char *<i>service</i>, const char *<i>protocol</i>,
 int <i>flags</i>, dns_query_txt_fn *<i>cbck</i>, <i>data</i>);
struct dns_rr_srv *
<code>dns_resolve_srv(</code><i>ctx</i>, const char *<i>name</i>, const char *<i>service</i>, const char *<i>protocol</i>,
 int <i>flags</i>);</pre>
<p>The <code>dns_rr_srv</code> structure holds a result of an IN SRV (rfc2782) query, which is an array of servers (together with port numbers) which are performing operations for a given <i>service</i> using given <i>protocol</i> on a target domain <i>name</i>. Callback routine for IN SRV queries expected to be of type <code>dns_query_srv_fn</code>, which expects pointer to <code>dns_rr_srv</code> structure as query result instead of raw DNS packet. The <code>dns_parse_srv</code>() is used to convert raw DNS reply packet into <code>dns_rr_srv</code> structure (it is used internally and may be used directly too with generic query interface). Routines <code>dns_submit_srv</code>() and <code>dns_resolve_srv</code>() are used to perform IN SRV queries in a type-safe manner. The <i>name</i> parameter is the domain name in question, <i>service</i> and protocl specifies the service and the protocol in question (the library will construct query DN according to rfc2782 rules) and may be NULL (in this case the library assumes <i>name</i> parameter holds the complete SRV query), and <i>flags</i> is query flags bitmask, with one bit, DNS_NOSRCH, of practical interest (if the <i>name</i> is absolute, that is, it ends up with a dot, DNS_NOSRCH flag will be set automatically).</p>
<h3>NAPTR Queries</h3>
<pre>struct <code>dns_naptr</code> { /* single NAPTR record */
 int <code>order</code>; /* record order */
 int <code>preference</code>; /* preference of this record */
 char *<code>flags</code>; /* application-specific flags */
 char *<code>service</code>; /* service parameter */
 char *<code>regexp</code>; /* substitutional regular expression */
 char *<code>replacement</code>; /* replacement string */
};
struct <code>dns_rr_naptr</code> { /* NAPTR RRset */
 char *<code>dnsnaptr_qname</code>; /* original query name */
 char *<code>dnsnaptr_cname</code>; /* canonical name */
 unsigned <code>dnsnaptr_ttl</code>; /* Time-To-Live (TTL) value */
 int <code>dnsnaptr_nrr</code>; /* number of text records in the set */
 struct dns_naptr <code>dnsnaptr_naptr</code>[]; /* array of NAPTR records */
};
typedef void
 <code>dns_query_naptr_fn</code>(<i>ctx</i>, struct dns_rr_naptr *<i>result</i>, <i>data</i>)
dns_parse_fn <code>dns_parse_naptr;
struct dns_query *
dns_submit_naptr(</code><i>ctx</i>, const char *<i>name</i>, int <i>flags</i>,
 dns_query_txt_fn *<i>cbck</i>, <i>data</i>);
struct dns_rr_naptr *
<code>dns_resolve_naptr(</code><i>ctx</i>, const char *<i>name</i>, int <i>flags</i>);</pre>
<p>The <code>dns_rr_naptr</code> structure holds a result of an IN NAPTR (rfc3403) query. Callback routine for IN NAPTR queries expected to be of type <code>dns_query_naptr_fn</code>, expects pointer to <code>dns_rr_naptr</code> structure as query result instead of raw DNS packet. The <code>dns_parse_naptr</code>() is used to convert raw DNS reply packet into <code>dns_rr_naptr</code> structure (it is used internally and may be used directly too with generic query interface). Routines <code>dns_submit_naptr</code>() and <code>dns_resolve_naptr</code>() are used to perform IN NAPTR queries in a type-safe manner. The <i>name</i> parameter is the domain name in question, and <i>flags</i> is query flags bitmask, with one bit, DNS_NOSRCH, of practical interest (if the <i>name</i> is absolute, that is, it ends up with a dot, DNS_NOSRCH flag will be set automatically).</p>
<h3>DNSBL Interface</h3>
<p>A DNS-based blocklists, or a DNSBLs, are in wide use nowadays, especially to protect mailservers from spammers. The library provides DNSBL interface, a set of routines to perform queries against DNSBLs. Routines accepts an IP address (IPv4 and IPv6 are both supported) and a base DNSBL zone as query parameters, and returns either <code>dns_rr_a4</code> or <code>dns_rr_txt</code> structure. Note that IPv6 interface return IPv4 RRset. </p>
<pre>struct dns_query *
<code>dns_submit_a4dnsbl</code>(<i>ctx</i>,
 const struct in_addr *<i>addr</i>, const char *<i>dnsbl</i>,
 dns_query_a4_fn *<i>cbck</i>, void *<i>data</i>);
struct dns_query *
<code>dns_submit_a4dnsbl_txt</code>(<i>ctx</i>,
 const struct in_addr *<i>addr</i>, const char *<i>dnsbl</i>,
 dns_query_txt_fn *<i>cbck</i>, void *<i>data</i>);
struct dns_query *
<code>dns_submit_a6dnsbl</code>(<i>ctx</i>,
 const struct in6_addr *<i>addr</i>, const char *<i>dnsbl</i>,
 dns_query_a4_fn *<i>cbck</i>, void *<i>data</i>);
struct dns_query *
<code>dns_submit_a6dnsbl_txt</code>(<i>ctx</i>,
 const struct in6_addr *<i>addr</i>, const char *<i>dnsbl</i>,
 dns_query_txt_fn *<i>cbck</i>, void *<i>data</i>);
struct dns_rr_a4 *<code>dns_resolve_a4dnsbl</code>(<i>ctx</i>,
 const struct in_addr *<i>addr</i>, const char *<i>dnsbl</i>)
struct dns_rr_txt *<code>dns_resolve_a4dnsbl_txt</code>(<i>ctx</i>,
 const struct in_addr *<i>addr</i>, const char *<i>dnsbl</i>)
struct dns_rr_a4 *<code>dns_resolve_a6dnsbl</code>(<i>ctx</i>,
 const struct in6_addr *<i>addr</i>, const char *<i>dnsbl</i>)
struct dns_rr_txt *<code>dns_resolve_a6dnsbl_txt</code>(<i>ctx</i>,
 const struct in6_addr *<i>addr</i>, const char *<i>dnsbl</i>)</pre>
<p>Perform (submit or resolve) a DNSBL query for the given <i>dnsbl</i> domain and an IP <i>addr</i> in question, requesting either A or TXT records.</p>
<h3>RHSBL Interface</h3>
<p>RHSBL is similar to DNSBL, but instead of an IP address, the parameter is a domain name. </p>
<pre>struct dns_query *
<code>dns_submit_rhsbl</code>(<i>ctx</i>, const char *<i>name</i>, const char *<i>rhsbl</i>,
 dns_query_a4_fn *<i>cbck</i>, void *<i>data</i>);
struct dns_query *
<code>dns_submit_rhsbl_txt</code>(<i>ctx</i>, const char *<i>name</i>, const char *<i>rhsbl</i>,
 dns_query_txt_fn *<i>cbck</i>, void *<i>data</i>);
struct dns_rr_a4 *
<code>dns_resolve_rhsbl</code>(<i>ctx</i>, const char *<i>name</i>, const char *<i>rhsbl</i>);
struct dns_rr_txt *
<code>dns_resolve_rhsbl_txt</code>(<i>ctx</i>, const char *<i>name</i>, const char *<i>rhsbl</i>);</pre>
<p>Perform (submit or resolve) a RHSBL query for the given <i>rhsbl</i> domain and <i>name</i> in question, requesting either A or TXT records.</p>
<h2>Low-Level Interface</h2>
<h3>Domain Names (DNs)</h3>
<p>A DN is a series of domain name labels each starts with length byte, followed by empty label (label with zero length). The following routines to work with DNs are provided. </p>
<pre>unsigned <code>dns_dnlen</code>(const unsigned char *<i>dn</i>)</pre>
<dl>
<dd>return length of the domain name <i>dn</i>, including the terminating label.</dl>
<pre>unsigned <code>dns_dnlabels</code>(const unsigned char *<i>dn</i>)</pre>
<dl>
<dd>return number of non-zero labels in domain name <i>dn</i>.</dl>
<pre>unsigned <code>dns_dnequal</code>(<i>dn1</i>, <i>dn2</i>)
 const unsigned char *<i>dn1</i>, *<i>dn2</i>;</pre>
<dl>
<dd>test whenever the two domain names, <i>dn1</i> and <i>dn2</i>, are equal (case-insensitive). Return domain name length if equal or 0 if not.</dl>
<pre>unsigned <code>dns_dntodn</code>(<i>sdn</i>, <i>ddn</i>, <i>dnsiz</i>)
 const unsigned char *<i>sdn</i>;
 unsigned char *<i>ddn</i>;
 unsigned <i>dnsiz</i>;</pre>
<dl>
<dd>copies the source domain name <i>sdn</i> to destination buffer <i>ddn</i> of size <i>dnsiz</i>. Return domain name length or 0 if <i>ddn</i> is too small.</dl>
<pre>int <code>dns_ptodn</code>(<i>name</i>, <i>namelen</i>, <i>dn</i>, <i>dnsiz</i>, <i>isabs</i>)
int <code>dns_sptodn</code>(<i>name</i>, <i>dn</i>, <i>dnsiz</i>)
 const char *<i>name</i>; unsigned <i>namelen</i>;
 unsigned char *<i>dn</i>; unsigned <i>dnsiz</i>;
 int *<i>isabs</i>;</pre>
<dl>
<dd>convert asciiz name <i>name</i> of length <i>namelen</i> to DN format, placing result into buffer <i>dn</i> of size <i>dnsiz</i>. Return length of the DN if successeful, 0 if the <i>dn</i> buffer supplied is too small, or negative value if <i>name</i> is invalid. If <i>isabs</i> is non-NULL and conversion was successeful, *<i>isabs</i> will be set to either 1 or 0 depending whenever <i>name</i> was absolute (i.e. ending with a dot) or not. Name length, <i>namelength</i>, may be zero, in which case strlen(<i>name</i>) will be used. Second form, <code>dns_sptodn</code>(), is a simplified form of <code>dns_ptodn</code>(), equivalent to </p>
<pre><code>dns_ptodn</code>(<i>name</i>, 0, <i>dn</i>, <i>dnlen</i>, 0).</pre>
</dl>
<pre>extern const unsigned char <code>dns_inaddr_arpa_dn</code>[]
int <code>dns_a4todn</code>(const struct in_addr *<i>addr</i>, const unsigned char *<i>tdn</i>,
 unsigned char *<i>dn</i>, unsigned <i>dnsiz</i>)
int <code>dns_a4ptodn</code>(const struct in_addr *<i>addr</i>, const char *<i>tname</i>,
 unsigned char *<i>dn</i>, unsigned <i>dnsiz</i>)
extern const unsigned char <code>dns_ip6_arpa_dn</code>[]
int <code>dns_a6todn</code>(const struct in6_addr *<i>addr</i>, const unsigned char *<i>tdn</i>,
 unsigned char *<i>dn</i>, unsigned <i>dnsiz</i>)
int <code>dns_a6ptodn</code>(const struct in6_addr *<i>addr</i>, const char *<i>tname</i>,
 unsigned char *<i>dn</i>, unsigned <i>dnsiz</i>)</pre>
<dl>
<dd>several variants of routines to convert IPv4 and IPv6 address <i>addr</i> into reverseDNS-like domain name in DN format, storing result in <i>dn</i> of size <i>dnsiz</i>. <i>tdn</i> (or <i>tname</i>) is the base zone name, like in-addr.arpa for IPv4 or in6.arpa for IPv6. If <i>tdn</i> (or <i>tname</i>) is NULL, <code>dns_inaddr_arpa_dn</code> (or <code>dns_ip6_arpa_dn</code>) will be used. The routines may be used to construct a DN for a DNSBL lookup for example. All routines return length of the resulting DN on success, -1 if resulting DN is invalid, or 0 if the <i>dn</i> buffer (<i>dnsiz</i>) is too small. To hold standard rDNS DN, a buffer of size <code>DNS_A4RSIZE</code> (30 bytes) for IPv4 address, or <code>DNS_A6RSIZE</code> (74 bytes) for IPv6 address, is sufficient.</dl>
<pre>int <code>dns_dntop</code>(<i>dn</i>, <i>name</i>, <i>namesiz</i>)
 const unsigned char *<i>dn</i>;
 const char *<i>name</i>; unsigned <i>namesiz</i>;</pre>
<dl>
<dd>convert domain name <i>dn</i> in DN format to asciiz string, placing result into <i>name</i> buffer of size <i>namesiz</i>. Maximum length of asciiz representation of domain name is <code>DNS_MAXNAME</code> (1024) bytes. Root domain is represented as empty string. Return length of the resulting name (including terminating character, i.e. strlen(name)+1) on success, 0 if the <i>name</i> buffer is too small, or negative value if <i>dn</i> is invalid (last case should never happen since all routines in this library which produce domain names ensure the DNs generated are valid).</dl>
<pre>const char *<code>dns_dntosp</code>(const unsigned char *<i>dn</i>)</pre>
<dl>
<dd>convert domain name <i>dn</i> in DN format to asciiz string using static buffer. Return the resulting asciiz string on success or NULL on failure. Note since this routine uses static buffer, it is not thread-safe.</dl>
<pre>unsigned <code>dns_dntop_size</code>(const unsigned char *<i>dn</i>)</pre>
<dl>
<dd>return the buffer size needed to convert the <i>dn</i> domain name in DN format to asciiz string, for <code>dns_dntop</code>(). The routine return either the size of buffer required, including the trailing zero byte, or 0 if <i>dn</i> is invalid.</dl>
<h3>Working with DNS Packets</h3>
<p>The following routines are provided to encode and decode DNS on-wire packets. This is low-level interface. </p>
<p> DNS response codes (returned by <code>dns_rcode</code>() routine) are defined as constants prefixed with <code>DNS_R_</code>. See udns.h header file for the complete list. In particular, constants <code>DNS_R_NOERROR</code> (0), <code>DNS_R_SERVFAIL</code>, <code>DNS_R_NXDOMAIN</code> may be of interest to an application. </p>
<pre>unsigned <code>dns_get16</code>(const unsigned char *<i>p</i>)
unsigned <code>dns_get32</code>(const unsigned char *<i>p</i>)</pre>
<dl>
<dd>helper routines, convert 16-bit or 32-bit integer in on-wire format pointed to by <i>p</i> to unsigned.</dl>
<pre>unsigned char *<code>dns_put16</code>(unsigned char *<i>d</i>, unsigned <i>n</i>)
unsigned char *<code>dns_put32</code>(unsigned char *<i>d</i>, unsigned <i>n</i>)</pre>
<dl>
<dd>helper routine, convert unsigned 16-bit or 32-bit integer <i>n</i> to on-wire format to buffer pointed to by <i>d</i>, return <i>d</i>+2 or <i>d</i>+4.</dl>
<pre><code>DNS_HSIZE</code> (12)</pre>
<dl>
<dd>defines size of DNS header. Data section in the DNS packet immediately follows the header. In the header, there are query identifier (id), various flags and codes, and number of resource records in various data sections. See udns.h header file for complete list of DNS header definitions.</dl>
<pre>unsigned <code>dns_qid</code>(const unsigned char *<i>pkt</i>)
int <code>dns_rd</code>(const unsigned char *<i>pkt</i>)
int <code>dns_tc</code>(const unsigned char *<i>pkt</i>)
int <code>dns_aa</code>(const unsigned char *<i>pkt</i>)
int <code>dns_qr</code>(const unsigned char *<i>pkt</i>)
int <code>dns_ra</code>(const unsigned char *<i>pkt</i>)
unsigned <code>dns_opcode</code>(const unsigned char *<i>pkt</i>)
unsigned <code>dns_rcode</code>(const unsigned char *<i>pkt</i>)
unsigned <code>dns_numqd</code>(const unsigned char *<i>pkt</i>)
unsigned <code>dns_numan</code>(const unsigned char *<i>pkt</i>)
unsigned <code>dns_numns</code>(const unsigned char *<i>pkt</i>)
unsigned <code>dns_numar</code>(const unsigned char *<i>pkt</i>)
const unsigned char *<code>dns_payload</code>(const unsigned char *<i>pkt</i>)</pre>
<dl>
<dd>return various parts from the DNS packet header <i>pkt</i>: query identifier (qid), recursion desired (rd) flag, truncation occured (tc) flag, authoritative answer (aa) flag, query response (qr) flag, recursion available (ra) flag, operation code (opcode), result code (rcode), number of entries in question section (numqd), number of answers (numan), number of authority records (numns), number of additional records (numar), and the pointer to the packet data (payload).</dl>
<pre>int <code>dns_getdn</code>(<i>pkt</i>, <i>curp</i>, <i>pkte</i>, <i>dn</i>, <i>dnsiz</i>)
const unsigned char *<code>dns_skipdn</code>(<i>cur</i>, <i>pkte</i>)
 const unsigned char *<i>pkt</i>, *<i>pkte</i>, **<i>curp</i>, *<i>cur</i>;
 unsigned char *<i>dn</i>; unsigned <i>dnsiz</i>;</pre>
<dl>
<dd><code>dns_getdn</code>() extract DN from DNS packet <i>pkt</i> which ends before <i>pkte</i> starting at position *<i>curp</i> into buffer pointed to by <i>dn</i> of size <i>dnsiz</i>. Upon successeful completion, *<i>curp</i> will point to the next byte in the packet after the extracted domain name. It return positive number (length of the DN if <i>dn</i>) upon successeful completion, negative value on error (when the packet contains invalid data), or zero if the <i>dnsiz</i> is too small (maximum length of a domain name is <code>DNS_MAXDN</code>). <code>dns_skipdn</code>() return pointer to the next byte in DNS packet which ends up before <i>pkte</i> after a domain name which starts at the <i>cur</i> byte, or NULL if the packet is invalid. <code>dns_skipdn</code>() is more or less equivalent to what <code>dns_getdn</code>() does, except it does not actually extract the domain name in question, and uses simpler interface.</dl>
<pre>struct <code>dns_rr</code> {
 unsigned char <code>dnsrr_dn</code>[DNS_MAXDN]; /* the RR DN name */
 enum dns_class <code>dnsrr_cls</code>; /* class of the RR */
 enum dns_type <code>dnsrr_typ</code>; /* type of the RR */
 unsigned <code>dnsrr_ttl</code>; /* TTL value */
 unsigned <code>dnsrr_dsz</code>; /* size of data in bytes */
 const unsigned char *<code>dnsrr_dptr</code>; /* pointer to the first data byte */
 const unsigned char *<code>dnsrr_dend</code>; /* next byte after RR */
};</pre>
<dl>
<dd>The <code>dns_rr</code> structure is used to hold information about single DNS Resource Record (RR) in an easy to use form.</dl>
<pre>struct <code>dns_parse</code> {
 const unsigned char *<code>dnsp_pkt</code>; /* pointer to the packet being parsed */
 const unsigned char *<code>dnsp_end</code>; /* end of the packet pointer */
 const unsigned char *<code>dnsp_cur</code>; /* current packet positionn */
 const unsigned char *<code>dnsp_ans</code>; /* pointer to the answer section */
 int <code>dnsp_rrl</code>; /* number of RRs left */
 int <code>dnsp_nrr</code>; /* number of relevant RRs seen so far */
 unsigned <code>dnsp_ttl</code>; /* TTL value so far */
 const unsigned char *<code>dnsp_qdn</code>; /* the domain of interest or NULL */
 enum dns_class <code>dnsp_qcls</code>; /* class of interest or 0 for any */
 enum dns_type <code>dnsp_qtyp</code>; /* type of interest or 0 for any */
 unsigned char <code>dnsp_dnbuf</code>[DNS_MAXDN]; /* domain name buffer */
};</pre>
<dl>
<dd>The <code>dns_parse</code> structure is used to parse DNS reply packet. It holds information about the packet being parsed (dnsp_pkt, dnsp_end and dnsp_cur fields), number of RRs in the current section left to do, and the information about specific RR which we&#8217;re looking for (dnsp_qdn, dnsp_qcls and dnsp_qtyp fields).</dl>
<pre>int <code>dns_initparse</code>(struct dns_parse *<i>p</i>,
 const unsigned char *<i>qdn</i>,
 const unsigned char *<i>pkt</i>,
 const unsigned char *<i>cur</i>,
 const unsigned char *<i>end</i>)</pre>
<dl>
<dd>initializes the RR parsing structure <i>p</i>. Arguments <i>pkt</i>, <i>cur</i> and <i>end</i> should describe the received packet: <i>pkt</i> is the start of the packet, <i>end</i> points to the next byte after the end of the packet, and <i>cur</i> points past the query DN in query section (to query class+type information). And <i>qdn</i> points to the query DN. This is the arguments passed to <code>dns_parse_fn</code>() routine. <code>dns_initparse</code>() initializes <code>dnsp_pkt</code>, <code>dnsp_end</code> and <code>dnsp_qdn</code> fields to the corresponding arguments, extracts and initializes <code>dnsp_qcls</code> and <code>dnsp_qtyp</code> fields to the values found at <i>cur</i> pointer, initializes <code>dnsp_cur</code> and <code>dnsp_ans</code> fields to be <i>cur</i>+4 (to the start of answer section), and initializes <code>dnsp_rrl</code> field to be number of entries in answer section. <code>dnsp_ttl</code> will be set to max TTL value, 0xffffffff, and <code>dnsp_nrr</code> to 0.</dl>
<pre>int <code>dns_nextrr</code>(struct dns_parse *<i>p</i>, struct dns_rr *<i>rr</i>);</pre>
<dl>
<dd>searches for next RR in the packet based on the criteria provided in the <i>p</i> structure, filling in the <i>rr</i> structure and advancing <i>p</i>-&gt;<code>dnsp_cur</code> to the next RR in the packet. RR selection is based on dnsp_qdn, dnsp_qcls and dnsp_qtyp fields in the dns_parse structure. Any (or all) of the 3 fields may be 0, which means any actual value from the packet is acceptable. In case the field isn&#8217;t 0 (or NULL for dnsp_qdn), only RRs with corresponding characteristics are acceptable. Additionally, when dnsp_qdn is non-NULL, <code>dns_nextrr</code>() performs automatic CNAME expansion. Routine will return positive value on success, 0 in case it reached the end of current section in the packet (<i>p</i>-&gt;<code>dnsp_rrl</code> is zero), or negative value if next RR can not be decoded (packet format is invalid). The routine updates <i>p</i>-&gt;<code>dnsp_qdn</code> automatically when this field is non-NULL and it encounters appropriate CNAME RRs (saving CNAME target in <i>p</i>-&gt;<code>dnsp_dnbuf</code>), so after end of the process, <i>p</i>-&gt;<code>dnsp_qdn</code> will point to canonical name of the domain in question. The routine updates <i>p</i>-&gt;<code>dnsp_ttl</code> value to be the minimum TTL of all RRs found.</dl>
<pre>void <code>dns_rewind</code>(struct dns_parse *<i>p</i>, const unsigned char *<i>qdn</i>)</pre>
<dl>
<dd>this routine &quot;rewinds&quot; the packet parse state structure to be at the same state as after a call to <code>dns_initparse</code>(), i.e. reposition the parse structure <i>p</i> to the start of answer section and initialize <i>p</i>-&gt;<code>dnsp_rrl</code> to the number of entries in answer section.</dl>
<pre>int <code>dns_stdrr_size</code>(const struct dns_parse *<i>p</i>);</pre>
<dl>
<dd>return size to hold standard RRset structure information, as shown in <code>dns_rr_null</code> structure (for the query and canonical names). Used to calculate amount of memory to allocate for common part of type-specific RR structures in parsing routines.</dl>
<pre>void *<code>dns_stdrr_finish</code>(struct dns_rr_null *<i>ret</i>, char *<i>cp</i>,
 const struct dns_parse *<i>p</i>);</pre>
<dl>
<dd>initializes standard RRset fields in <i>ret</i> structure using buffer pointed to by <i>cp</i>, which should have at least as many bytes as <code>dns_stdrr_size</code>(<i>p</i>) returned. Used to finalize common part of type-specific RR structures in parsing routines.</dl>
<p> See library source for usage examples of all the above low-level routines, especially source of the parsing routines.</p>
<h3>Auxilary Routines</h3>
<pre>int <code>dns_pton</code>(int <i>af</i>, const char *<i>src</i>, void *<i>dst</i>);</pre>
<dl>
<dd>privides functionality similar to standard <code>inet_pton</code>() routine, to convert printable representation of an IP address of family <i>af</i> (either <code>AF_INET</code> or <code>AF_INET6</code>) pointed to by <i>src</i> into binary form suitable for socket addresses and transmission over network, in buffer pointed to by <i>dst</i>. The destination buffer should be of size 4 for <code>AF_INET</code> family or 16 for <code>AF_INET6</code>. The return value is positive on success, 0 if <i>src</i> is not a valid text representation of an address of family <i>af</i>, or negative if the given address family is not supported.</dl>
<pre>const char *<code>dns_ntop</code>(int <i>af</i>, const void *<i>src</i>,
 char *<i>dst</i>, int <i>dstsize</i>)</pre>
<dl>
<dd>privides functionality similar to standard <code>inet_ntop</code>() routine, to convert binary representation of an IP address of family <i>af</i> (either <code>AF_INET</code> or <code>AF_INET6</code>) pointed to by <i>src</i> (either 4 or 16 bytes) into printable form in buffer in buffer pointed to by <i>dst</i> of size <i>dstsize</i>. The destination buffer should be at least of size 16 bytes for <code>AF_INET</code> family or 46 bytes for <code>AF_INET6</code>. The return value is either <i>dst</i>, or NULL pointer if <i>dstsize</i> is too small to hold this address or if the given address family is not supported.</dl>
<h2>Author</h2>
<p>The <code>udns</code> library has been written by Michael Tokarev, mjt+udns [at] tls.msk.ru.</p>
<h2>Version</h2>
<p>This manual page corresponds to udns version 0.4, released Jan-2014.</p>
