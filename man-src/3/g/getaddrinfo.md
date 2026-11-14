---
title: "getaddrinfo(3)"
name: "getaddrinfo"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getaddrinfo/"
description: "getaddrinfo, freeaddrinfo, gai_strerror – network address and service translation"
---

<p>getaddrinfo, freeaddrinfo, gai_strerror &#8211; network address and service translation</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netdb.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt;

int getaddrinfo(const char *node, const char *service,
                const struct addrinfo *hints,
                struct addrinfo **res);

void freeaddrinfo(struct addrinfo *res);

const char *gai_strerror(int errcode);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>getaddrinfo</code>(), <code>freeaddrinfo</code>(), <code>gai_strerror</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.22:&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.21 and earlier:&nbsp;_POSIX_C_SOURCE</p>
<h2>Description</h2>
<p>Given <i>node</i> and <i>service</i>, which identify an Internet host and a service, <code>getaddrinfo</code>() returns one or more <i>addrinfo</i> structures, each of which contains an Internet address that can be specified in a call to <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) or <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2). The <code>getaddrinfo</code>() function combines the functionality provided by the <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3) and <code><a href="/docs/linux/man/3-getservbyname/">getservbyname</a></code>(3) functions into a single interface, but unlike the latter functions, <code>getaddrinfo</code>() is reentrant and allows programs to eliminate IPv4-versus-IPv6 dependencies. The <i>addrinfo</i> structure used by <code>getaddrinfo</code>() contains the following fields: struct addrinfo {<br />
    int ai_flags;<br />
    int ai_family;<br />
    int ai_socktype;<br />
    int ai_protocol;<br />
    socklen_t ai_addrlen;<br />
    struct sockaddr *ai_addr;<br />
    char *ai_canonname;<br />
    struct addrinfo *ai_next;<br />
}; The <i>hints</i> argument points to an <i>addrinfo</i> structure that specifies criteria for selecting the socket address structures returned in the list pointed to by <i>res</i>. If <i>hints</i> is not NULL it points to an <i>addrinfo</i> structure whose <i>ai_family</i>, <i>ai_socktype</i>, and <i>ai_protocol</i> specify criteria that limit the set of socket addresses returned by <code>getaddrinfo</code>(), as follows:</p>
<dl>
<dt><i>ai_family</i></p>
<dd>This field specifies the desired address family for the returned addresses. Valid values for this field include <code>AF_INET</code> and <code>AF_INET6</code>. The value <code>AF_UNSPEC</code> indicates that <code>getaddrinfo</code>() should return socket addresses for any address family (either IPv4 or IPv6, for example) that can be used with <i>node</i> and <i>service</i>.</p>
<dt><i>ai_socktype</i></p>
<dd>This field specifies the preferred socket type, for example <code>SOCK_STREAM</code> or <code>SOCK_DGRAM</code>. Specifying 0 in this field indicates that socket addresses of any type can be returned by <code>getaddrinfo</code>().</p>
<dt><i>ai_protocol</i></p>
<dd>This field specifies the protocol for the returned socket addresses. Specifying 0 in this field indicates that socket addresses with any protocol can be returned by <code>getaddrinfo</code>().</p>
<dt><i>ai_flags</i></p>
<dd>This field specifies additional options, described below. Multiple flags are specified by bitwise OR-ing them together.</dl>
<p> All the other fields in the structure pointed to by <i>hints</i> must contain either 0 or a null pointer, as appropriate. Specifying <i>hints</i> as NULL is equivalent to setting <i>ai_socktype</i> and <i>ai_protocol</i> to 0; <i>ai_family</i> to <code>AF_UNSPEC</code>; and <i>ai_flags</i> to <code>(AI_V4MAPPED | AI_ADDRCONFIG)</code>. (POSIX specifies different defaults for <i>ai_flags</i>; see NOTES.) <i>node</i> specifies either a numerical network address (for IPv4, numbers-and-dots notation as supported by <code><a href="/docs/linux/man/3-inet_aton/">inet_aton</a></code>(3); for IPv6, hexadecimal string format as supported by <code><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></code>(3)), or a network hostname, whose network addresses are looked up and resolved. If <i>hints.ai_flags</i> contains the <code>AI_NUMERICHOST</code> flag, then <i>node</i> must be a numerical network address. The <code>AI_NUMERICHOST</code> flag suppresses any potentially lengthy network host address lookups. If the <code>AI_PASSIVE</code> flag is specified in <i>hints.ai_flags</i>, and <i>node</i> is NULL, then the returned socket addresses will be suitable for <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2)ing a socket that will <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2) connections. The returned socket address will contain the &quot;wildcard address&quot; (<code>INADDR_ANY</code> for IPv4 addresses, <code>IN6ADDR_ANY_INIT</code> for IPv6 address). The wildcard address is used by applications (typically servers) that intend to accept connections on any of the host&#8217;s network addresses. If <i>node</i> is not NULL, then the <code>AI_PASSIVE</code> flag is ignored. If the <code>AI_PASSIVE</code> flag is not set in <i>hints.ai_flags</i>, then the returned socket addresses will be suitable for use with <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2), or <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2). If <i>node</i> is NULL, then the network address will be set to the loopback interface address (<code>INADDR_LOOPBACK</code> for IPv4 addresses, <code>IN6ADDR_LOOPBACK_INIT</code> for IPv6 address); this is used by applications that intend to communicate with peers running on the same host. <i>service</i> sets the port in each returned address structure. If this argument is a service name (see <code><a href="/docs/linux/man/5-services/">services</a></code>(5)), it is translated to the corresponding port number. This argument can also be specified as a decimal number, which is simply converted to binary. If <i>service</i> is NULL, then the port number of the returned socket addresses will be left uninitialized. If <code>AI_NUMERICSERV</code> is specified in <i>hints.ai_flags</i> and <i>service</i> is not NULL, then <i>service</i> must point to a string containing a numeric port number. This flag is used to inhibit the invocation of a name resolution service in cases where it is known not to be required. Either <i>node</i> or <i>service</i>, but not both, may be NULL. The <code>getaddrinfo</code>() function allocates and initializes a linked list of <i>addrinfo</i> structures, one for each network address that matches <i>node</i> and <i>service</i>, subject to any restrictions imposed by <i>hints</i>, and returns a pointer to the start of the list in <i>res</i>. The items in the linked list are linked by the <i>ai_next</i> field. There are several reasons why the linked list may have more than one <i>addrinfo</i> structure, including: the network host is multihomed, accessible over multiple protocols (e.g., both <code>AF_INET</code> and <code>AF_INET6</code>); or the same service is available from multiple socket types (one <code>SOCK_STREAM</code> address and another <code>SOCK_DGRAM</code> address, for example). Normally, the application should try using the addresses in the order in which they are returned. The sorting function used within <code>getaddrinfo</code>() is defined in RFC 3484; the order can be tweaked for a particular system by editing <i>/etc/gai.conf</i> (available since glibc 2.5). If <i>hints.ai_flags</i> includes the <code>AI_CANONNAME</code> flag, then the <i>ai_canonname</i> field of the first of the <i>addrinfo</i> structures in the returned list is set to point to the official name of the host. The remaining fields of each returned <i>addrinfo</i> structure are initialized as follows:</p>
<dl>
<dt>*</p>
<dd>The <i>ai_family</i>, <i>ai_socktype</i>, and <i>ai_protocol</i> fields return the socket creation parameters (i.e., these fields have the same meaning as the corresponding arguments of <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2)). For example, <i>ai_family</i> might return <code>AF_INET</code> or <code>AF_INET6</code>; <i>ai_socktype</i> might return <code>SOCK_DGRAM</code> or <code>SOCK_STREAM</code>; and <i>ai_protocol</i> returns the protocol for the socket.</p>
<dt>*</p>
<dd>A pointer to the socket address is placed in the <i>ai_addr</i> field, and the length of the socket address, in bytes, is placed in the <i>ai_addrlen</i> field.</dl>
<p> If <i>hints.ai_flags</i> includes the <code>AI_ADDRCONFIG</code> flag, then IPv4 addresses are returned in the list pointed to by <i>res</i> only if the local system has at least one IPv4 address configured, and IPv6 addresses are returned only if the local system has at least one IPv6 address configured. The loopback address is not considered for this case as valid as a configured address. This flag is useful on, for example, IPv4-only systems, to ensure that <code>getaddrinfo</code>() does not return IPv6 socket addresses that would always fail in <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) or <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2). If <i>hints.ai_flags</i> specifies the <code>AI_V4MAPPED</code> flag, and <i>hints.ai_family</i> was specified as <code>AF_INET6</code>, and no matching IPv6 addresses could be found, then return IPv4-mapped IPv6 addresses in the list pointed to by <i>res</i>. If both <code>AI_V4MAPPED</code> and <code>AI_ALL</code> are specified in <i>hints.ai_flags</i>, then return both IPv6 and IPv4-mapped IPv6 addresses in the list pointed to by <i>res</i>. <code>AI_ALL</code> is ignored if <code>AI_V4MAPPED</code> is not also specified. The <code>freeaddrinfo</code>() function frees the memory that was allocated for the dynamically allocated linked list <i>res</i>.</p>
<h3>Extensions to getaddrinfo() for Internationalized Domain Names</h3>
<p>Starting with glibc 2.3.4, <code>getaddrinfo</code>() has been extended to selectively allow the incoming and outgoing hostnames to be transparently converted to and from the Internationalized Domain Name (IDN) format (see RFC 3490, <i>Internationalizing Domain Names in Applications (IDNA)</i>). Four new flags are defined:</p>
<dl>
<dt><code>AI_IDN</code></p>
<dd>If this flag is specified, then the node name given in <i>node</i> is converted to IDN format if necessary. The source encoding is that of the current locale.</p>
<dd>If the input name contains non-ASCII characters, then the IDN encoding is used. Those parts of the node name (delimited by dots) that contain non-ASCII characters are encoded using ASCII Compatible Encoding (ACE) before being passed to the name resolution functions.</p>
<dt><code>AI_CANONIDN</code></p>
<dd>After a successful name lookup, and if the <code>AI_CANONNAME</code> flag was specified, <code>getaddrinfo</code>() will return the canonical name of the node corresponding to the <i>addrinfo</i> structure value passed back. The return value is an exact copy of the value returned by the name resolution function.</p>
<dd>If the name is encoded using ACE, then it will contain the <i>xn--</i> prefix for one or more components of the name. To convert these components into a readable form the <code>AI_CANONIDN</code> flag can be passed in addition to <code>AI_CANONNAME</code>. The resulting string is encoded using the current locale&#8217;s encoding.</p>
<dt><code>AI_IDN_ALLOW_UNASSIGNED</code>, <code>AI_IDN_USE_STD3_ASCII_RULES</code></p>
<dd>Setting these flags will enable the IDNA_ALLOW_UNASSIGNED (allow unassigned Unicode code points) and IDNA_USE_STD3_ASCII_RULES (check output to make sure it is a STD3 conforming hostname) flags respectively to be used in the IDNA handling.</dl>
<h2>Return Value</h2>
<p><code>getaddrinfo</code>() returns 0 if it succeeds, or one of the following nonzero error codes:</p>
<dl>
<dt><code>EAI_ADDRFAMILY</code></p>
<dd>The specified network host does not have any network addresses in the requested address family.</p>
<dt><code>EAI_AGAIN</code></p>
<dd>The name server returned a temporary failure indication. Try again later.</p>
<dt><code>EAI_BADFLAGS</code></p>
<dd><i>hints.ai_flags</i> contains invalid flags; or, <i>hints.ai_flags</i> included <code>AI_CANONNAME</code> and <i>name</i> was NULL.</p>
<dt><code>EAI_FAIL</code></p>
<dd>The name server returned a permanent failure indication.</p>
<dt><code>EAI_FAMILY</code></p>
<dd>The requested address family is not supported.</p>
<dt><code>EAI_MEMORY</code></p>
<dd>Out of memory.</p>
<dt><code>EAI_NODATA</code></p>
<dd>The specified network host exists, but does not have any network addresses defined.</p>
<dt><code>EAI_NONAME</code></p>
<dd>The <i>node</i> or <i>service</i> is not known; or both <i>node</i> and <i>service</i> are NULL; or <code>AI_NUMERICSERV</code> was specified in <i>hints.ai_flags</i> and <i>service</i> was not a numeric port-number string.</p>
<dt><code>EAI_SERVICE</code></p>
<dd>The requested service is not available for the requested socket type. It may be available through another socket type. For example, this error could occur if <i>service</i> was &quot;shell&quot; (a service available only on stream sockets), and either <i>hints.ai_protocol</i> was <code>IPPROTO_UDP</code>, or <i>hints.ai_socktype</i> was <code>SOCK_DGRAM</code>; or the error could occur if <i>service</i> was not NULL, and <i>hints.ai_socktype</i> was <code>SOCK_RAW</code> (a socket type that does not support the concept of services).</p>
<dt><code>EAI_SOCKTYPE</code></p>
<dd>The requested socket type is not supported. This could occur, for example, if <i>hints.ai_socktype</i> and <i>hints.ai_protocol</i> are inconsistent (e.g., <code>SOCK_DGRAM</code> and <code>IPPROTO_TCP</code>, respectively).</p>
<dt><code>EAI_SYSTEM</code></p>
<dd>Other system error, check <i>errno</i> for details.</dl>
<p> The <code>gai_strerror</code>() function translates these error codes to a human readable string, suitable for error reporting.</p>
<h2>Files</h2>
<p><i>/etc/gai.conf</i></p>
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
<td> <code>getaddrinfo</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>freeaddrinfo</code>(), <code>gai_strerror</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008. The <code>getaddrinfo</code>() function is documented in RFC 2553.</p>
<h2>Notes</h2>
<p><code>getaddrinfo</code>() supports the <i>address</i><code>%</code><i>scope-id</i> notation for specifying the IPv6 scope-ID. </p>
<p> <code>AI_ADDRCONFIG</code>, <code>AI_ALL</code>, and <code>AI_V4MAPPED</code> are available since glibc 2.3.3. <code>AI_NUMERICSERV</code> is available since glibc 2.3.4. </p>
<p> According to POSIX.1, specifying <i>hints</i> as NULL should cause <i>ai_flags</i> to be assumed as 0. The GNU C library instead assumes a value of <code>(AI_V4MAPPED | AI_ADDRCONFIG)</code> for this case, since this value is considered an improvement on the specification.</p>
<h2>Examples</h2>
<p>The following programs demonstrate the use of <code>getaddrinfo</code>(), <code>gai_strerror</code>(), <code>freeaddrinfo</code>(), and <code><a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a></code>(3). The programs are an echo server and client for UDP datagrams.</p>
<h3>Server program</h3>
<p>#include &lt;sys/types.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;string.h&gt; #include &lt;sys/socket.h&gt; #include &lt;netdb.h&gt; </p>
<pre><code>#define BUF_SIZE 500
int main(int argc, char *argv[])
{
    struct addrinfo hints;
    struct addrinfo *result, *rp;
    int sfd, s;
    struct sockaddr_storage peer_addr;
    socklen_t peer_addr_len;
    ssize_t nread;
    char buf[BUF_SIZE];
    if (argc != 2) {
        fprintf(stderr, &quot;Usage: %s port
&quot;, argv[0]);
        exit(EXIT_FAILURE);
    }
    memset(&amp;hints, 0, sizeof(hints));
    hints.ai_family = AF_UNSPEC;    /* Allow IPv4 or IPv6 */
    hints.ai_socktype = SOCK_DGRAM; /* Datagram socket */
    hints.ai_flags = AI_PASSIVE;    /* For wildcard IP address */
    hints.ai_protocol = 0;          /* Any protocol */
    hints.ai_canonname = NULL;
    hints.ai_addr = NULL;
    hints.ai_next = NULL;
    s = getaddrinfo(NULL, argv[1], &amp;hints, &amp;result);
    if (s != 0) {
        fprintf(stderr, &quot;getaddrinfo: %s
&quot;, gai_strerror(s));
        exit(EXIT_FAILURE);
    }
    /* getaddrinfo() returns a list of address structures.
           Try each address until we successfully bind(2).
           If socket(2) (or bind(2)) fails, we (close the socket
           and) try the next address. */
    for (rp = result; rp != NULL; rp = rp-&gt;ai_next) {
        sfd = socket(rp-&gt;ai_family, rp-&gt;ai_socktype,
                     rp-&gt;ai_protocol);
        if (sfd == -1)
            continue;
        if (bind(sfd, rp-&gt;ai_addr, rp-&gt;ai_addrlen) == 0)
            break; /* Success */
        close(sfd);
    }
    freeaddrinfo(result); /* No longer needed */
    if (rp == NULL) {     /* No address succeeded */
        fprintf(stderr, &quot;Could not bind
&quot;);
        exit(EXIT_FAILURE);
    }
    /* Read datagrams and echo them back to sender */
    for (;;) {
        peer_addr_len = sizeof(peer_addr);
        nread = recvfrom(sfd, buf, BUF_SIZE, 0,
                         (struct sockaddr *)&amp;peer_addr, &amp;peer_addr_len);
        if (nread == -1)
            continue; /* Ignore failed request */
        char host[NI_MAXHOST], service[NI_MAXSERV];
        s = getnameinfo((struct sockaddr *)&amp;peer_addr,
                        peer_addr_len, host, NI_MAXHOST,
                        service, NI_MAXSERV, NI_NUMERICSERV);
        if (s == 0)
            printf(&quot;Received %zd bytes from %s:%s
&quot;,
                   nread, host, service);
        else
            fprintf(stderr, &quot;getnameinfo: %s
&quot;, gai_strerror(s));
        if (sendto(sfd, buf, nread, 0,
                   (struct sockaddr *)&amp;peer_addr,
                   peer_addr_len) != nread)
            fprintf(stderr, &quot;Error sending response
&quot;);
    }
}

Client program

#include &lt;netdb.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt;
#define BUF_SIZE 500
    int
    main(int argc, char *argv[])
{
    struct addrinfo hints;
    struct addrinfo *result, *rp;
    int sfd, s;
    size_t len;
    ssize_t nread;
    char buf[BUF_SIZE];
    if (argc &lt; 3) {
        fprintf(stderr, &quot;Usage: %s host port msg...
&quot;, argv[0]);
        exit(EXIT_FAILURE);
    }
    /* Obtain address(es) matching host/port */
    memset(&amp;hints, 0, sizeof(hints));
    hints.ai_family = AF_UNSPEC;    /* Allow IPv4 or IPv6 */
    hints.ai_socktype = SOCK_DGRAM; /* Datagram socket */
    hints.ai_flags = 0;
    hints.ai_protocol = 0; /* Any protocol */
    s = getaddrinfo(argv[1], argv[2], &amp;hints, &amp;result);
    if (s != 0) {
        fprintf(stderr, &quot;getaddrinfo: %s
&quot;, gai_strerror(s));
        exit(EXIT_FAILURE);
    }
    /* getaddrinfo() returns a list of address structures.
           Try each address until we successfully connect(2).
           If socket(2) (or connect(2)) fails, we (close the socket
           and) try the next address. */
    for (rp = result; rp != NULL; rp = rp-&gt;ai_next) {
        sfd = socket(rp-&gt;ai_family, rp-&gt;ai_socktype,
                     rp-&gt;ai_protocol);
        if (sfd == -1)
            continue;
        if (connect(sfd, rp-&gt;ai_addr, rp-&gt;ai_addrlen) != -1)
            break; /* Success */
        close(sfd);
    }
    freeaddrinfo(result); /* No longer needed */
    if (rp == NULL) {     /* No address succeeded */
        fprintf(stderr, &quot;Could not connect
&quot;);
        exit(EXIT_FAILURE);
    }
    /* Send remaining command-line arguments as separate
           datagrams, and read responses from server */
    for (int j = 3; j &lt; argc; j++) {
        len = strlen(argv[j]) + 1;
        /* +1 for terminating null byte */
        if (len &gt; BUF_SIZE) {
            fprintf(stderr,
                    &quot;Ignoring long message in argument %d
&quot;, j);
            continue;
        }
        if (write(sfd, argv[j], len) != len) {
            fprintf(stderr, &quot;partial/failed write
&quot;);
            exit(EXIT_FAILURE);
        }
        nread = read(sfd, buf, BUF_SIZE);
        if (nread == -1) {
            perror(&quot;read&quot;);
            exit(EXIT_FAILURE);
        }
        printf(&quot;Received %zd bytes: %s
&quot;, nread, buf);
    }
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getaddrinfo_a/">getaddrinfo_a</a></code>(3), <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3), <code><a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a></code>(3), <code><a href="/docs/linux/man/3-inet/">inet</a></code>(3), <code><a href="/docs/linux/man/5-gai-conf/">gai.conf</a></code>(5), <code><a href="/docs/linux/man/7-hostname/">hostname</a></code>(7), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
