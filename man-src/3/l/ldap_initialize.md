---
title: "ldap_initialize(3)"
name: "ldap_initialize"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_initialize/"
description: "ldap_init, ldap_initialize, ldap_open – Initialize the LDAP library and open a connection to an LDAP server"
---

<h2 class="name">NAME</h2>
<p> ldap_init, ldap_initialize, ldap_open &#8211; Initialize the LDAP library and open a connection to an LDAP server </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
LDAP *ldap_open(host, port)
char *host;
int port;
LDAP *ldap_init(host, port)
char *host;
int port;
int ldap_initialize(ldp, uri)
LDAP **ldp;
char *uri;
int ldap_set_urllist_proc(ld, proc, params)
LDAP *ld;
LDAP_URLLIST_PROC *proc;
void *params;
int(LDAP_URLLIST_PROC)(ld, urllist, url, params);
LDAP *ld;
LDAPURLDesc **urllist;
LDAPURLDesc **url;
void *params;
#include &lt;ldap_pvt.h&gt;
int ldap_init_fd(fd, proto, uri, ldp)
ber_socket_t fd;
int proto;
char *uri;
LDAP **ldp;
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ldap_open()</code> opens a connection to an LDAP server and allocates an LDAP structure which is used to identify the connection and to maintain per-connection information. <code>ldap_init()</code> allocates an LDAP structure but does not open an initial connection. <code>ldap_initialize()</code> allocates an LDAP structure but does not open an initial connection. <code>ldap_init_fd()</code> allocates an LDAP structure using an existing connection on the provided socket. One of these routines must be called before any operations are attempted. </p>
<p> <code>ldap_open()</code> takes <i>host</i>, the hostname on which the LDAP server is running, and <i>port</i>, the port number to which to connect. If the default IANA-assigned port of 389 is desired, LDAP_PORT should be specified for <i>port</i>. The <i>host</i> parameter may contain a blank-separated list of hosts to try to connect to, and each host may optionally by of the form <i>host:port</i>. If present, the <i>:port</i> overrides the <i>port</i> parameter to <code>ldap_open()</code>. Upon successfully making a connection to an LDAP server, <code>ldap_open()</code> returns a pointer to an opaque LDAP structure, which should be passed to subsequent calls to <code>ldap_bind()</code>, <code>ldap_search()</code>, etc. Certain fields in the LDAP structure can be set to indicate size limit, time limit, and how aliases are handled during operations; read and write access to those fields must occur by calling <code><a href="/docs/linux/man/3-ldap_get_option/">ldap_get_option</a></code>(3) and <code><a href="/docs/linux/man/3-ldap_set_option/">ldap_set_option</a></code>(3) respectively, whenever possible. </p>
<p> <code>ldap_init()</code> acts just like <code>ldap_open()</code>, but does not open a connection to the LDAP server. The actual connection open will occur when the first operation is attempted. </p>
<p> <code>ldap_initialize()</code> acts like <code>ldap_init()</code>, but it returns an integer indicating either success or the failure reason, and it allows to specify details for the connection in the schema portion of the URI. The <i>uri</i> parameter may be a comma- or whitespace-separated list of URIs containing only the <i>schema</i>, the <i>host</i>, and the <i>port</i> fields. Apart from <code>ldap</code>, other (non-standard) recognized values of the <i>schema</i> field are <code>ldaps</code> (LDAP over TLS), <code>ldapi</code> (LDAP over IPC), and <code>cldap</code> (connectionless LDAP). If other fields are present, the behavior is undefined. </p>
<p> At this time, <code>ldap_open()</code> and <code>ldap_init()</code> are deprecated in favor of <code>ldap_initialize()</code>, essentially because the latter allows to specify a schema in the URI and it explicitly returns an error code. </p>
<p> <code>ldap_init_fd()</code> allows an LDAP structure to be initialized using an already-opened connection. The <i>proto</i> parameter should be one of LDAP_PROTO_TCP, LDAP_PROTO_UDP, or LDAP_PROTO_IPC for a connection using TCP, UDP, or IPC, respectively. The value LDAP_PROTO_EXT may also be specified if user-supplied sockbuf handlers are going to be used. Note that support for UDP is not implemented unless libldap was built with LDAP_CONNECTIONLESS defined. The <i>uri</i> parameter may optionally be provided for informational purposes. </p>
<p> <code>ldap_set_urllist_proc()</code> allows to set a function <i>proc</i> of type <i>LDAP_URLLIST_PROC</i> that is called when a successful connection can be established. This function receives the list of URIs parsed from the <i>uri</i> string originally passed to <code>ldap_initialize()</code>, and the one that successfully connected. The function may manipulate the URI list; the typical use consists in moving the successful URI to the head of the list, so that subsequent attempts to connect to one of the URIs using the same LDAP handle will try it first. If <i>ld</i> is null, <i>proc</i> is set as a global parameter that is inherited by all handlers within the process that are created after the call to <code>ldap_set_urllist_proc()</code>. By default, no <i>LDAP_URLLIST_PROC</i> is set. In a multithreaded environment, <code>ldap_set_urllist_proc()</code> must be called before any concurrent operation using the LDAP handle is started. </p>
<p> Note: the first call into the LDAP library also initializes the global options for the library. As such the first call should be single-threaded or otherwise protected to insure that only one call is active. It is recommended that <code>ldap_get_option</code>() or <code>ldap_set_option</code>() be used in the program&#8217;s main thread before any additional threads are created. See <code><a href="/docs/linux/man/3-ldap_get_option/">ldap_get_option</a></code>(3). </p>
<h2>ERRORS</h2>
<p> If an error occurs, <code>ldap_open()</code> and <code>ldap_init()</code> will return NULL and <i>errno</i> should be set appropriately. <code>ldap_initialize()</code> and <code>ldap_init_fd()</code> will directly return the LDAP code associated to the error (or <i>LDAP_SUCCESS</i> in case of success); <i>errno</i> should be set as well whenever appropriate. <code>ldap_set_urllist_proc()</code> returns LDAP_OPT_ERROR on error, and LDAP_OPT_SUCCESS on success.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_bind/">ldap_bind</a></code>(3), <code><a href="/docs/linux/man/3-ldap_get_option/">ldap_get_option</a></code>(3), <code><a href="/docs/linux/man/3-ldap_set_option/">ldap_set_option</a></code>(3), <code><a href="/docs/linux/man/3-lber-sockbuf/">lber-sockbuf</a></code>(3), <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
