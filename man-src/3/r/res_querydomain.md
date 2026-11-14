---
title: "res_querydomain(3)"
name: "res_querydomain"
section: "3"
letter: "r"
url: "/docs/linux/man/3-res_querydomain/"
description: "res_ninit, res_nclose, res_nquery, res_nsearch, res_nquerydomain, res_nmkquery, res_nsend, res_init, res_query, res_search, res_querydomain, res_mkquery, res_send, dn_comp, dn_expand – resolver rou..."
---

<p>res_ninit, res_nclose, res_nquery, res_nsearch, res_nquerydomain, res_nmkquery, res_nsend, res_init, res_query, res_search, res_querydomain, res_mkquery, res_send, dn_comp, dn_expand &#8211; resolver routines</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;arpa/nameser.h&gt;
#include &lt;netinet/in.h&gt;
#include &lt;resolv.h&gt;

struct __res_state;
typedef struct __res_state *res_state;

int res_ninit(res_state statep);

void res_nclose(res_state statep);

int res_nquery(res_state statep,
               const char *dname, int class, int type,
               unsigned char *answer, int anslen);

int res_nsearch(res_state statep,
                const char *dname, int class, int type,
                unsigned char *answer, int anslen);

int res_nquerydomain(res_state statep,
                     const char *name, const char *domain,
                     int class, int type, unsigned char *answer,
                     int anslen);

int res_nmkquery(res_state statep,
                 int op, const char *dname, int class,
                 int type, const unsigned char *data, int datalen,
                 const unsigned char *newrr,
                 unsigned char *buf, int buflen);

int res_nsend(res_state statep,
              const unsigned char *msg, int msglen,
              unsigned char *answer, int anslen);

int dn_comp(const char *exp_dn, unsigned char *comp_dn,
            int length, unsigned char **dnptrs,
            unsigned char **lastdnptr);

int dn_expand(const unsigned char *msg,
              const unsigned char *eomorig,
              const unsigned char *comp_dn, char *exp_dn,
              int length);

Deprecated

    extern struct __res_state _res;

int res_init(void);

int res_query(const char *dname, int class, int type,
              unsigned char *answer, int anslen);

int res_search(const char *dname, int class, int type,
               unsigned char *answer, int anslen);

int res_querydomain(const char *name, const char *domain,
                    int class, int type, unsigned char *answer,
                    int anslen);

int res_mkquery(int op, const char *dname, int class,
                int type, const unsigned char *data, int datalen,
                const unsigned char *newrr,
                unsigned char *buf, int buflen);

int res_send(const unsigned char *msg, int msglen,
             unsigned char *answer, int anslen);</code></pre>
<p> Link with <i>-lresolv</i>.</p>
<h2>Description</h2>
<p><code>Note:</code> This page is incomplete (various resolver functions provided by glibc are not described) and likely out of date. </p>
<p> The functions described below make queries to and interpret the responses from Internet domain name servers. </p>
<p> The API consists of a set of more modern, reentrant functions and an older set of nonreentrant functions that have been superseded. The traditional resolver interfaces such as <code>res_init</code>() and <code>res_query</code>() use some static (global) state stored in the <i>_res</i> structure, rendering these functions non-thread-safe. BIND 8.2 introduced a set of new interfaces <code>res_ninit</code>(), <code>res_nquery</code>(), and so on, which take a <i>res_state</i> as their first argument, so you can use a per-thread resolver state. </p>
<p> The <code>res_ninit</code>() and <code>res_init</code>() functions read the configuration files (see <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5)) to get the default domain name and name server address(es). If no server is given, the local host is tried. If no domain is given, that associated with the local host is used. It can be overridden with the environment variable <code>LOCALDOMAIN</code>. <code>res_ninit</code>() or <code>res_init</code>() is normally executed by the first call to one of the other functions. Every call to <code>res_ninit</code>() requires a corresponding call to <code>res_nclose</code>() to free memory allocated by <code>res_ninit</code>() and subsequent calls to <code>res_nquery</code>(). </p>
<p> The <code>res_nquery</code>() and <code>res_query</code>() functions query the name server for the fully qualified domain name <i>name</i> of specified <i>type</i> and <i>class</i>. The reply is left in the buffer <i>answer</i> of length <i>anslen</i> supplied by the caller. </p>
<p> The <code>res_nsearch</code>() and <code>res_search</code>() functions make a query and waits for the response like <code>res_nquery</code>() and <code>res_query</code>(), but in addition they implement the default and search rules controlled by <code>RES_DEFNAMES</code> and <code>RES_DNSRCH</code> (see description of <i>_res</i> options below). </p>
<p> The <code>res_nquerydomain</code>() and <code>res_querydomain</code>() functions make a query using <code>res_nquery</code>()/<code>res_query</code>() on the concatenation of <i>name</i> and <i>domain</i>. </p>
<p> The following functions are lower-level routines used by <code>res_nquery</code>()/<code>res_query</code>(). </p>
<p> The <code>res_nmkquery</code>() and <code>res_mkquery</code>() functions construct a query message in <i>buf</i> of length <i>buflen</i> for the domain name <i>dname</i>. The query type <i>op</i> is one of the following (typically <code>QUERY</code>):</p>
<dl>
<dt><code>QUERY</code></p>
<dd>Standard query.</p>
<dt><code>IQUERY</code></p>
<dd>Inverse query. This option was removed in glibc 2.26, since it has not been supported by DNS servers for a very long time.</p>
<dt><code>NS_NOTIFY_OP</code></p>
<dd>Notify secondary of SOA (Start of Authority) change.</dl>
<p> <i>newrr</i> is currently unused. </p>
<p> The <code>res_nsend</code>() and <code>res_send</code>() function send a preformatted query given in <i>msg</i> of length <i>msglen</i> and returns the answer in <i>answer</i> which is of length <i>anslen</i>. They will call <code>res_ninit</code>()/<code>res_init</code>() if it has not already been called. </p>
<p> The <code>dn_comp</code>() function compresses the domain name <i>exp_dn</i> and stores it in the buffer <i>comp_dn</i> of length <i>length</i>. The compression uses an array of pointers <i>dnptrs</i> to previously compressed names in the current message. The first pointer points to the beginning of the message and the list ends with NULL. The limit of the array is specified by <i>lastdnptr</i>. If <i>dnptr</i> is NULL, domain names are not compressed. If <i>lastdnptr</i> is NULL, the list of labels is not updated. </p>
<p> The <code>dn_expand</code>() function expands the compressed domain name <i>comp_dn</i> to a full domain name, which is placed in the buffer <i>exp_dn</i> of size <i>length</i>. The compressed name is contained in a query or reply message, and <i>msg</i> points to the beginning of the message. </p>
<p> The resolver routines use configuration and state information contained in a <i>__res_state</i> structure (either passed as the <i>statep</i> argument, or in the global variable <i>_res</i>, in the case of the older nonreentrant functions). The only field of this structure that is normally manipulated by the user is the <i>options</i> field. This field can contain the bitwise &quot;OR&quot; of the following options:</p>
<dl>
<dt><code>RES_INIT</code></p>
<dd>True if <code>res_ninit</code>() or <code>res_init</code>() has been called.</p>
<dt><code>RES_DEBUG</code></p>
<dd>Print debugging messages. This option is available only if glibc was built with debugging enabled, which is not the default.</p>
<dt><code>RES_AAONLY</code> (unimplemented; deprecated in glibc 2.25)</p>
<dd>Accept authoritative answers only. <code>res_send</code>() continues until it finds an authoritative answer or returns an error. This option was present but unimplemented in glibc until version 2.24; since glibc 2.25, it is deprecated, and its usage produces a warning.</p>
<dt><code>RES_USEVC</code></p>
<dd>Use TCP connections for queries rather than UDP datagrams.</p>
<dt><code>RES_PRIMARY</code> (unimplemented; deprecated in glibc 2.25)</p>
<dd>Query primary domain name server only. This option was present but unimplemented in glibc until version 2.24; since glibc 2.25, it is deprecated, and its usage produces a warning.</p>
<dt><code>RES_IGNTC</code></p>
<dd>Ignore truncation errors. Don&#8217;t retry with TCP.</p>
<dt><code>RES_RECURSE</code></p>
<dd>Set the recursion desired bit in queries. Recursion is carried out by the domain name server, not by <code>res_send</code>(). [Enabled by default].</p>
<dt><code>RES_DEFNAMES</code></p>
<dd>If set, <code>res_search</code>() will append the default domain name to single component names&#8212;that is, those that do not contain a dot. [Enabled by default].</p>
<dt><code>RES_STAYOPEN</code></p>
<dd>Used with <code>RES_USEVC</code> to keep the TCP connection open between queries.</p>
<dt><code>RES_DNSRCH</code></p>
<dd>If set, <code>res_search</code>() will search for hostnames in the current domain and in parent domains. This option is used by <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3). [Enabled by default].</p>
<dt><code>RES_INSECURE1</code></p>
<dd>Accept a response from a wrong server. This can be used to detect potential security hazards, but you need to compile glibc with debugging enabled and use <code>RES_DEBUG</code> option (for debug purpose only).</p>
<dt><code>RES_INSECURE2</code></p>
<dd>Accept a response which contains a wrong query. This can be used to detect potential security hazards, but you need to compile glibc with debugging enabled and use <code>RES_DEBUG</code> option (for debug purpose only).</p>
<dt><code>RES_NOALIASES</code></p>
<dd>Disable usage of <code>HOSTALIASES</code> environment variable.</p>
<dt><code>RES_USE_INET6</code></p>
<dd>Try an AAAA query before an A query inside the <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3) function, and map IPv4 responses in IPv6 &quot;tunneled form&quot; if no AAAA records are found but an A record set exists. Since glibc 2.25, this option is deprecated, and its usage produces a warning; applications should use <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3), rather than <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3).</p>
<dt><code>RES_ROTATE</code></p>
<dd>Causes round-robin selection of name servers from among those listed. This has the effect of spreading the query load among all listed servers, rather than having all clients try the first listed server first every time.</p>
<dt><code>RES_NOCHECKNAME</code> (unimplemented; deprecated in glibc 2.25)</p>
<dd>Disable the modern BIND checking of incoming hostnames and mail names for invalid characters such as underscore (_), non-ASCII, or control characters. This option was present in glibc until version 2.24; since glibc 2.25, it is deprecated, and its usage produces a warning.</p>
<dt><code>RES_KEEPTSIG</code> (unimplemented; deprecated in glibc 2.25)</p>
<dd>Do not strip TSIG records. This option was present but unimplemented in glibc until version 2.24; since glibc 2.25, it is deprecated, and its usage produces a warning.</p>
<dt><code>RES_BLAST</code> (unimplemented; deprecated in glibc 2.25)</p>
<dd>Send each query simultaneously and recursively to all servers. This option was present but unimplemented in glibc until version 2.24; since glibc 2.25, it is deprecated, and its usage produces a warning.</p>
<dt><code>RES_USEBSTRING</code> (glibc 2.3.4 to 2.24)</p>
<dd>Make reverse IPv6 lookups using the bit-label format described in RFC 2673; if this option is not set (which is the default), then nibble format is used. This option was removed in glibc 2.25, since it relied on a backward-incompatible DNS extension that was never deployed on the Internet.</p>
<dt><code>RES_NOIP6DOTINT</code> (glibc 2.24 and earlier)</p>
<dd>Use <i>ip6.arpa</i> zone in IPv6 reverse lookup instead of <i>ip6.int</i>, which is deprecated since glibc 2.3.4. This option is present in glibc up to and including version 2.24, where it is enabled by default. In glibc 2.25, this option was removed.</p>
<dt><code>RES_USE_EDNS0</code> (since glibc 2.6)</p>
<dd>Enables support for the DNS extensions (EDNS0) described in RFC 2671.</p>
<dt><code>RES_SNGLKUP</code> (since glibc 2.10)</p>
<dd>By default, glibc performs IPv4 and IPv6 lookups in parallel since version 2.9. Some appliance DNS servers cannot handle these queries properly and make the requests time out. This option disables the behavior and makes glibc perform the IPv6 and IPv4 requests sequentially (at the cost of some slowdown of the resolving process).</p>
<dt><code>RES_SNGLKUPREOP</code></p>
<dd>When <code>RES_SNGLKUP</code> option is enabled, opens a new socket for the each request.</p>
<dt><code>RES_USE_DNSSEC</code></p>
<dd>Use DNSSEC with OK bit in OPT record. This option implies <code>RES_USE_EDNS0</code>.</p>
<dt><code>RES_NOTLDQUERY</code></p>
<dd>Do not look up unqualified name as a top-level domain (TLD).</p>
<dt><code>RES_DEFAULT</code></p>
<dd>Default option which implies: <code>RES_RECURSE</code>, <code>RES_DEFNAMES</code>, <code>RES_DNSRCH</code>, and <code>RES_NOIP6DOTINT</code>.</dl>
<h2>Return Value</h2>
<p>The <code>res_ninit</code>() and <code>res_init</code>() functions return 0 on success, or -1 if an error occurs. </p>
<p> The <code>res_nquery</code>(), <code>res_query</code>(), <code>res_nsearch</code>(), <code>res_search</code>(), <code>res_nquerydomain</code>(), <code>res_querydomain</code>(), <code>res_nmkquery</code>(), <code>res_mkquery</code>(), <code>res_nsend</code>(), and <code>res_send</code>() functions return the length of the response, or -1 if an error occurs. </p>
<p> The <code>dn_comp</code>() and <code>dn_expand</code>() functions return the length of the compressed name, or -1 if an error occurs. </p>
<p> In the case of an error return from <code>res_nquery</code>(), <code>res_query</code>(), <code>res_nsearch</code>(), <code>res_search</code>(), <code>res_nquerydomain</code>(), or <code>res_querydomain</code>(), the global variable <i>h_errno</i> (see <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3)) can be consulted to determine the cause of the error.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/resolv.conf</i></p>
<dd>resolver configuration file</p>
<dt><i>/etc/host.conf</i></p>
<dd>resolver configuration file</dl>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>res_ninit</code>(), <code>res_nclose</code>(), <code>res_nquery</code>(),<br />
 <code>res_nsearch</code>(), <code>res_nquerydomain</code>(), <code>res_nsend</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>res_nmkquery</code>(), <code>dn_comp</code>(),<br />
 <code>dn_expand</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>4.3BSD.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3), <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5), <code><a href="/docs/linux/man/5-resolver/">resolver</a></code>(5), <code><a href="/docs/linux/man/7-hostname/">hostname</a></code>(7), <code><a href="/docs/linux/man/8-named/">named</a></code>(8) </p>
<p> The GNU C library source file <i>resolv/README</i>.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
