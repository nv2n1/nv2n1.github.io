---
title: "lwres_gethostent_r(3)"
name: "lwres_gethostent_r"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres_gethostent_r/"
description: "lwres_gethostbyname, lwres_gethostbyname2, lwres_gethostbyaddr, lwres_gethostent, lwres_sethostent, lwres_endhostent, lwres_gethostbyname_r, lwres_gethostbyaddr_r, lwres_gethostent_r, lwres_sethost..."
---

<h2 class="name">NAME</h2>
<p> lwres_gethostbyname, lwres_gethostbyname2, lwres_gethostbyaddr, lwres_gethostent, lwres_sethostent, lwres_endhostent, lwres_gethostbyname_r, lwres_gethostbyaddr_r, lwres_gethostent_r, lwres_sethostent_r, lwres_endhostent_r &#8211; lightweight resolver get network host entry </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/netdb.h&gt;
</code></pre>
<dl>
<dt> <code>struct hostent * lwres_gethostbyname(const char&nbsp;<wbr>*</code><i>name</i><code>);</code></p>
<dt> <code>struct hostent * lwres_gethostbyname2(const char&nbsp;<wbr>*</code><i>name</i><code>, int&nbsp;<wbr></code><i>af</i><code>);</code></p>
<dt> <code>struct hostent * lwres_gethostbyaddr(const char&nbsp;<wbr>*</code><i>addr</i><code>, int&nbsp;<wbr></code><i>len</i><code>, int&nbsp;<wbr></code><i>type</i><code>);</code></p>
<dt> <code>struct hostent * lwres_gethostent(void);</code></p>
<dt> <code>void lwres_sethostent(int&nbsp;<wbr></code><i>stayopen</i><code>);</code></p>
<dt> <code>void lwres_endhostent(void);</code></p>
<dt> <code>struct hostent * lwres_gethostbyname_r(const char&nbsp;<wbr>*</code><i>name</i><code>, struct hostent&nbsp;<wbr>*</code><i>resbuf</i><code>, char&nbsp;<wbr>*</code><i>buf</i><code>, int&nbsp;<wbr></code><i>buflen</i><code>, int&nbsp;<wbr>*</code><i>error</i><code>);</code></p>
<dt> <code>struct hostent * lwres_gethostbyaddr_r(const char&nbsp;<wbr>*</code><i>addr</i><code>, int&nbsp;<wbr></code><i>len</i><code>, int&nbsp;<wbr></code><i>type</i><code>, struct hostent&nbsp;<wbr>*</code><i>resbuf</i><code>, char&nbsp;<wbr>*</code><i>buf</i><code>, int&nbsp;<wbr></code><i>buflen</i><code>, int&nbsp;<wbr>*</code><i>error</i><code>);</code></p>
<dt> <code>struct hostent * lwres_gethostent_r(struct hostent&nbsp;<wbr>*</code><i>resbuf</i><code>, char&nbsp;<wbr>*</code><i>buf</i><code>, int&nbsp;<wbr></code><i>buflen</i><code>, int&nbsp;<wbr>*</code><i>error</i><code>);</code></p>
<dt> <code>void lwres_sethostent_r(int&nbsp;<wbr></code><i>stayopen</i><code>);</code></p>
<dt> <code>void lwres_endhostent_r(void);</code></dl>
<h2>DESCRIPTION</h2>
<dd>These functions provide hostname-to-address and address-to-hostname lookups by means of the lightweight resolver. They are similar to the standard <code><a href="/docs/linux/man/3-gethostent/">gethostent</a></code>(3) functions provided by most operating systems. They use a <code>struct hostent</code> which is usually defined in <i>&lt;namedb.h&gt;</i>. </p>
<dl>
<dt>
<dd>
<pre><code>
struct hostent {
    char *h_name;       /* official name of host */
    char **h_aliases;   /* alias list */
    int h_addrtype;     /* host address type */
    int h_length;       /* length of address */
    char **h_addr_list; /* list of addresses from name server */
};
#define h_addr h_addr_list[0] /* address, for backward compatibility */
</code></pre>
</dl>
<p> The members of this structure are: </p>
<p> <code>h_name</code></p>
<dl>
<dt>
<dd> The official (canonical) name of the host.</dl>
<p> <code>h_aliases</code></p>
<dl>
<dt>
<dd> A NULL-terminated array of alternate names (nicknames) for the host.</dl>
<p> <code>h_addrtype</code></p>
<dl>
<dt>
<dd> The type of address being returned &#8212; <code>PF_INET</code> or <code>PF_INET6</code>.</dl>
<p> <code>h_length</code></p>
<dl>
<dt>
<dd> The length of the address in bytes.</dl>
<p> <code>h_addr_list</code></p>
<dl>
<dt>
<dd> A <code>NULL</code> terminated array of network addresses for the host. Host addresses are returned in network byte order.</dl>
<p> For backward compatibility with very old software, <code>h_addr</code> is the first address in <code>h_addr_list.</code> </p>
<p> <code>lwres_gethostent()</code>, <code>lwres_sethostent()</code>, <code>lwres_endhostent()</code>, <code>lwres_gethostent_r()</code>, <code>lwres_sethostent_r()</code> and <code>lwres_endhostent_r()</code> provide iteration over the known host entries on systems that provide such functionality through facilities like <i>/etc/hosts</i> or NIS. The lightweight resolver does not currently implement these functions; it only provides them as stub functions that always return failure. </p>
<p> <code>lwres_gethostbyname()</code> and <code>lwres_gethostbyname2()</code> look up the hostname <i>name</i>. <code>lwres_gethostbyname()</code> always looks for an IPv4 address while <code>lwres_gethostbyname2()</code> looks for an address of protocol family <i>af</i>: either <code>PF_INET</code> or <code>PF_INET6</code> &#8212; IPv4 or IPV6 addresses respectively. Successful calls of the functions return a <code>struct hostent</code>for the name that was looked up. <code>NULL</code> is returned if the lookups by <code>lwres_gethostbyname()</code> or <code>lwres_gethostbyname2()</code> fail. </p>
<p> Reverse lookups of addresses are performed by <code>lwres_gethostbyaddr()</code>. <i>addr</i> is an address of length <i>len</i> bytes and protocol family <i>type</i> &#8212; <code>PF_INET</code> or <code>PF_INET6</code>. <code>lwres_gethostbyname_r()</code> is a thread-safe function for forward lookups. If an error occurs, an error code is returned in <i>*error</i>. <i>resbuf</i> is a pointer to a <code>struct hostent</code> which is initialised by a successful call to <code>lwres_gethostbyname_r()</code>. <i>buf</i> is a buffer of length <i>len</i> bytes which is used to store the <code>h_name</code>, <code>h_aliases</code>, and <code>h_addr_list</code> elements of the <code>struct hostent</code> returned in <i>resbuf</i>. Successful calls to <code>lwres_gethostbyname_r()</code> return <i>resbuf</i>, which is a pointer to the <code>struct hostent</code> it created. </p>
<p> <code>lwres_gethostbyaddr_r()</code> is a thread-safe function that performs a reverse lookup of address <i>addr</i> which is <i>len</i> bytes long and is of protocol family <i>type</i> &#8212; <code>PF_INET</code> or <code>PF_INET6</code>. If an error occurs, the error code is returned in <i>*error</i>. The other function parameters are identical to those in <code>lwres_gethostbyname_r()</code>. <i>resbuf</i> is a pointer to a <code>struct hostent</code> which is initialised by a successful call to <code>lwres_gethostbyaddr_r()</code>. <i>buf</i> is a buffer of length <i>len</i> bytes which is used to store the <code>h_name</code>, <code>h_aliases</code>, and <code>h_addr_list</code> elements of the <code>struct hostent</code> returned in <i>resbuf</i>. Successful calls to <code>lwres_gethostbyaddr_r()</code> return <i>resbuf</i>, which is a pointer to the <code>struct hostent()</code> it created.</p>
<h2>RETURN VALUES</h2>
<p> The functions <code>lwres_gethostbyname()</code>, <code>lwres_gethostbyname2()</code>, <code>lwres_gethostbyaddr()</code>, and <code>lwres_gethostent()</code> return NULL to indicate an error. In this case the global variable <code>lwres_h_errno</code> will contain one of the following error codes defined in <i>&lt;lwres/netdb.h&gt;</i>: </p>
<p> <code>HOST_NOT_FOUND</code></p>
<dl>
<dt>
<dd> The host or address was not found.</dl>
<p> <code>TRY_AGAIN</code></p>
<dl>
<dt>
<dd> A recoverable error occurred, e.g., a timeout. Retrying the lookup may succeed.</dl>
<p> <code>NO_RECOVERY</code></p>
<dl>
<dt>
<dd> A non-recoverable error occurred.</dl>
<p> <code>NO_DATA</code></p>
<dl>
<dt>
<dd> The name exists, but has no address information associated with it (or vice versa in the case of a reverse lookup). The code NO_ADDRESS is accepted as a synonym for NO_DATA for backwards compatibility.</dl>
<p> <code><a href="/docs/linux/man/3-lwres_hstrerror/">lwres_hstrerror</a></code>(3) translates these error codes to suitable error messages. </p>
<p> <code>lwres_gethostent()</code> and <code>lwres_gethostent_r()</code> always return <code>NULL</code>. </p>
<p> Successful calls to <code>lwres_gethostbyname_r()</code> and <code>lwres_gethostbyaddr_r()</code> return <i>resbuf</i>, a pointer to the <code>struct hostent</code> that was initialised by these functions. They return <code>NULL</code> if the lookups fail or if <i>buf</i> was too small to hold the list of addresses and names referenced by the <code>h_name</code>, <code>h_aliases</code>, and <code>h_addr_list</code> elements of the <code>struct hostent</code>. If <i>buf</i> was too small, both <code>lwres_gethostbyname_r()</code> and <code>lwres_gethostbyaddr_r()</code> set the global variable <code>errno</code> to <code>ERANGE</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gethostent/">gethostent</a></code>(3), <code><a href="/docs/linux/man/3-lwres_getipnode/">lwres_getipnode</a></code>(3), <code><a href="/docs/linux/man/3-lwres_hstrerror/">lwres_hstrerror</a></code>(3)</p>
<h2>BUGS</h2>
<p> <code>lwres_gethostbyname()</code>, <code>lwres_gethostbyname2()</code>, <code>lwres_gethostbyaddr()</code> and <code>lwres_endhostent()</code> are not thread safe; they return pointers to static data and provide error codes through a global variable. Thread-safe versions for name and address lookup are provided by <code>lwres_gethostbyname_r()</code>, and <code>lwres_gethostbyaddr_r()</code> respectively. </p>
<p> The resolver daemon does not currently support any non-DNS name services such as <i>/etc/hosts</i> or <code>NIS</code>, consequently the above functions don&#8217;t, either.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2001 Internet Software Consortium. </p>
<h2>Index</h2>
