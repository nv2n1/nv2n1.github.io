---
title: "remctl_open(3)"
name: "remctl_open"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remctl_open/"
---

remctl_open - Connect to a remote remctl server

<h2>Synopsis</h2>

<pre><code>#include &lt;remctl.h&gt;
int remctl_open(struct remctl *r, const char *host,
                unsigned short port,
                const char *principal);
int remctl_open_addrinfo(struct remctl *r, const char *host,
                         const struct addrinfo *ai,
                         const char *principal);
int remctl_open_sockaddr(struct remctl *r, const char *host,
                         const struct sockaddr *addr, int addrlen,
                         const char *principal);
int remctl_open_fd(struct remctl *r, const char *host,
                   int fd, const char *principal);</code></pre>

<h2>Description</h2>

<i>remctl_open()</i> opens a <font SIZE="-1">TCP</font> connection to the given <i>host</i> on the given <i>port</i> and then authenticates using the remctl protocol and the service principal <i>principal</i>. <i>r</i> is a remctl struct created via <i>remctl_new()</i>. <i>host</i> must not be <font SIZE="-1">NULL. </font> If <i>port</i> is 0, the library first attempts to connect to the registered port of 4373 and then tries the legacy port of 4444 if that fails. Future versions of the library will drop this fallback to 4444. If <i>principal</i> is <font SIZE="-1">NULL,</font> a service principal of <tt>&quot;host/</tt>host<tt>&quot;</tt> is used, with the realm determined by domain-realm mapping. 

 <i>remctl_open_addrinfo()</i> operates in the same manner as <i>remctl_open()</i>, but connects to the first usable address in <i>ai</i>, which must be a list of results as returned by <i><a HREF="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></i>(3). The <i>host</i> is used only to form the default service principal, and may be <font SIZE="-1">NULL</font> if <i>principal</i> is not <font SIZE="-1">NULL.</font> 

 <i>remctl_open_sockaddr()</i> is equivalent to <i>remctl_open_addrinfo()</i> with a single addrinfo structure specifying the use of <font SIZE="-1">TCP</font> with socket address <i>addr</i> and length <i>addrlen</i>. 

 <i>remctl_open_fd()</i> operates in the same manner as <i>remctl_open_addrinfo()</i>, but uses an already-established <font SIZE="-1">TCP</font> connection identified by the file descriptor <i>fd</i>. On Windows, <i>fd</i> is of type <tt>&quot;SOCKET&quot;</tt> and must be a valid socket descriptor. 

 If no principal is specified and the default is used, the underlying GSS-API library may canonicalize <i>host</i> via <font SIZE="-1">DNS</font> before determining the service principal, depending on your library configuration. Specifying a principal disables this behavior. 

 The remctl protocol uses Kerberos via GSS-API for authentication. The underlying GSS-API library will use the default ticket cache for authentication, so to successfully use <i>remctl_open()</i>, the caller should already have Kerberos tickets for an appropriate realm stored in its default ticket cache. The environment variable <font SIZE="-1">KRB5CCNAME</font> or the <i><a HREF="/docs/linux/man/3-remctl_set_ccache/">remctl_set_ccache</a></i>(3) function can be used to control which ticket cache is used. 

 To control the timeout for the connect and for subsequent calls, see the <i><a HREF="/docs/linux/man/3-remctl_set_timeout/">remctl_set_timeout</a></i>(3) function. To control the source <font SIZE="-1">IP</font> used by <i>remctl_open()</i>, <i>remctl_open_addrinfo()</i>, and <i>remctl_open_sockaddr()</i>, see the <i><a HREF="/docs/linux/man/3-remctl_set_source_ip/">remctl_set_source_ip</a></i>(3) function.

<h2>Return Value</h2>

<i>remctl_open()</i> returns true on success and false on failure. On failure, the caller should call <i>remctl_error()</i> to retrieve the error message.

<h2>Compatibility</h2>

The <i>remctl_open()</i> interface has been provided by the remctl client library since its initial release in version 2.0. <i>remctl_open_addrinfo()</i>, <i>remctl_open_sockaddr()</i>, and <i>remctl_open_fd()</i> were added in version 3.4. 

 The default port was changed to the IANA-registered port of 4373 in version 2.11. 

 Support for IPv6 was added in version 2.4.

<h2>Caveats</h2>

If the <i>principal</i> argument to <i>remctl_open()</i> is <font SIZE="-1">NULL,</font> most GSS-API libraries will canonicalize the <i>host</i> using <font SIZE="-1">DNS</font> before deriving the principal name from it. This means that when connecting to a remctl server via a <font SIZE="-1">CNAME,</font> <i>remctl_open()</i> will normally authenticate using a principal based on the canonical name of the host instead of the specified <i>host</i> parameter. This behavior may cause problems if two consecutive <font SIZE="-1">DNS</font> lookups of <i>host</i> may return two different results, such as with some DNS-based load-balancing systems. 

 The canonicalization behavior is controlled by the GSS-API library; with the <font SIZE="-1">MIT</font> Kerberos GSS-API library, canonicalization can be disabled by setting <tt>&quot;rdns&quot;</tt> to false in the [libdefaults] section of <i>krb5.conf</i>. It can also be disabled by passing an explicit Kerberos principal name via the <i>principal</i> argument, which will then be used without changes. If canonicalization is desired, the caller may wish to canonicalize <i>host</i> before calling <i>remctl_open()</i> to avoid problems with multiple <font SIZE="-1">DNS</font> calls returning different results. 

 The default behavior, when a port of 0 is given, of trying 4373 and falling back to 4444 will be removed in a future version of this library in favor of using the <tt>&quot;remctl&quot;</tt> service in <i>/etc/services</i> if set and then falling back on only 4373. 4444 was the poorly-chosen original remctl port and should be phased out. 

 Connections established using the alternate-open interfaces <i>remctl_open_fd()</i>, <i>remctl_open_addrinfo()</i>, and <i>remctl_open_sockaddr()</i> do not support the automatic connection-reopening which is used to give the illusion of a single long-lived connection when sending multiple commands to a server which supports only version 1 of the remctl protocol. Therefore, when using these interfaces to open a connection to such a server, it will only be possible to send a single command, after which the connection must be closed and reopened before another command can be sent.

<h2>Notes</h2>

The remctl port number, 4373, was derived by tracing the diagonals of a <font SIZE="-1">QWERTY</font> keyboard up from the letters <tt>&quot;remc&quot;</tt> to the number row.

<h2>Author</h2>

Russ Allbery &lt;eagle [at] eyrie.org&gt;

<h2>Copyright And License</h2>

Copyright 2007, 2008, 2009, 2014 The Board of Trustees of the Leland Stanford Junior University 

 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/3-remctl_new/">remctl_new</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_error/">remctl_error</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_set_ccache/">remctl_set_ccache</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_set_source_ip/">remctl_set_source_ip</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_set_timeout/">remctl_set_timeout</a></i>(3) The current version of the remctl library and complete details of the remctl protocol are available from its web page at &lt;<a rel="nofollow" HREF="http://www.eyrie.org/~eagle/software/remctl/">http://www.eyrie.org/~eagle/software/remctl/</a>&gt;. 
