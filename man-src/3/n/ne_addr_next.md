---
title: "ne_addr_next(3)"
name: "ne_addr_next"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_addr_next/"
description: "ne_addr_resolve, ne_addr_result, ne_addr_first, ne_addr_next, ne_addr_error, ne_addr_destroy – functions to resolve hostnames to addresses"
---

<p>ne_addr_resolve, ne_addr_result, ne_addr_first, ne_addr_next, ne_addr_error, ne_addr_destroy &#8211; functions to resolve hostnames to addresses</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_socket.h&gt;

ne_sock_addr *ne_addr_resolve(const char *hostname, int flags);

int ne_addr_result(const ne_sock_addr *addr);

const ne_inet_addr *ne_addr_first(ne_sock_addr *addr);

const ne_inet_addr *ne_addr_next(ne_sock_addr *addr);

char *ne_addr_error(const ne_sock_addr *addr, char *buffer, size_t bufsiz);

void ne_addr_destroy(ne_sock_addr *addr);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_addr_resolve</code> function resolves the given <i>hostname</i>, returning an <code>ne_sock_addr</code> object representing the address (or addresses) associated with the hostname. The <i>flags</i> parameter is currently unused, and must be passed as 0. </p>
<p> The <i>hostname</i> passed to <code>ne_addr_resolve</code> can be a DNS hostname (e.g. &quot;<a rel="nofollow" href="http://www.example.com">www.example.com</a>&quot;) or an IPv4 dotted quad (e.g. &quot;192.0.34.72&quot;); or, on systems which support IPv6, an IPv6 hex address, which may be enclosed in brackets, e.g. &quot;[::1]&quot;. </p>
<p> To determine whether the hostname was successfully resolved, the <code>ne_addr_result</code> function is used, which returns non-zero if an error occurred. If an error did occur, the <code>ne_addr_error</code> function can be used, which will copy the error string into a given <i>buffer</i> (of size <i>bufsiz</i>). </p>
<p> The functions <code>ne_addr_first</code> and <code>ne_addr_next</code> are used to retrieve the Internet addresses associated with an address object which has been successfully resolved. <code>ne_addr_first</code> returns the first address; <code>ne_addr_next</code> returns the next address after the most recent call to <code>ne_addr_next</code> or <code>ne_addr_first</code>, or NULL if there are no more addresses. The <code>ne_inet_addr</code> pointer returned by these functions can be passed to <code>ne_sock_connect</code> to connect a socket. </p>
<p> After the address object has been used, it should be destroyed using <code>ne_addr_destroy</code>.</p>
<h2>Return Value</h2>
<p><code>ne_addr_resolve</code> returns a pointer to an address object, and never NULL. <code>ne_addr_error</code> returns the <i>buffer</i> parameter .</p>
<h2>Examples</h2>
<p>The code below prints out the set of addresses associated with the hostname <a rel="nofollow" href="http://www.google.com">www.google.com</a>. </p>
<pre><code>ne_sock_addr *addr;
char buf[256];

addr = ne_addr_resolve(&quot;www.google.com&quot;, 0);
if (ne_addr_result(addr)) {
    printf(&quot;Could not resolve www.google.com: %s
&quot;,
           ne_addr_error(addr, buf, sizeof buf));
} else {
    const ne_inet_addr *ia;
    printf(&quot;www.google.com:&quot;);
    for (ia = ne_addr_first(addr); ia != NULL; ia = ne_addr_next(addr)) {
        printf(&quot; %s&quot;, ne_iaddr_print(ia, buf, sizeof buf));
    }
    putchar('
');
}
ne_addr_destroy(addr);</code></pre>
<h2>See Also</h2>
<p>ne_iaddr_print</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
