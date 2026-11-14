---
title: "ares_getnameinfo(3)"
name: "ares_getnameinfo"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_getnameinfo/"
description: "ares_getnameinfo – Address-to-nodename translation in protocol-independent manner"
---

<h2>NAME</h2>
<p> ares_getnameinfo &#8211; Address-to-nodename translation in protocol-independent manner</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
typedef void (*ares_nameinfo_callback)(void *arg, int status,
void ares_getnameinfo(ares_channel channel, const struct sockaddr *sa,
ares_socklen_t salen, int flags, ares_nameinfo_callback callback,
void *arg)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_getnameinfo</code> function is defined for protocol-independent address translation. The function is a combination of <i><a href="/docs/linux/man/3-ares_gethostbyaddr/">ares_gethostbyaddr</a>(3)</i> and <i><a href="/docs/linux/man/3-getservbyport/">getservbyport</a>(3)</i>. The function will translate the address either by executing a host query on the name service channel identified by <i>channel</i> or it will attempt to resolve it locally if possible. The parameters <i>sa</i> and <i>len</i> give the address as a sockaddr structure, and <i>flags</i> gives the options that the function will use. Valid flags are listed below:</p>
<dl>
<dt><code>ARES_NI_NOFQDN</code></p>
<dd> Only the nodename portion of the FQDN is returned for local hosts.</p>
<dt><code>ARES_NI_NUMERICHOST</code></p>
<dd> The numeric form of the hostname is returned rather than the name.</p>
<dt><code>ARES_NI_NAMEREQD</code></p>
<dd> An error is returned if the hostname cannot be found in the DNS.</p>
<dt><code>ARES_NI_NUMERICSERV</code></p>
<dd> The numeric form of the service is returned rather than the name.</p>
<dt><code>ARES_NI_TCP</code></p>
<dd> The service name is to be looked up for the TCP protocol.</p>
<dt><code>ARES_NI_UDP</code></p>
<dd> The service name is to be looked up for the UDP protocol.</p>
<dt><code>ARES_NI_SCTP</code></p>
<dd> The service name is to be looked up for the SCTP protocol.</p>
<dt><code>ARES_NI_DCCP</code></p>
<dd> The service name is to be looked up for the DCCP protocol.</p>
<dt><code>ARES_NI_NUMERICSCOPE</code></p>
<dd> The numeric form of the scope ID is returned rather than the name.</p>
<dt><code>ARES_NI_LOOKUPHOST</code></p>
<dd> A hostname lookup is being requested.</p>
<dt><code>ARES_NI_LOOKUPSERVICE</code></p>
<dd> A service name lookup is being requested.</dl>
<p> When the query is complete or has failed, the ares library will invoke <i>callback</i>. Completion or failure of the query may happen immediately, or may happen during a later call to <i><a href="/docs/linux/man/3-ares_process/">ares_process</a>(3)</i>, <i><a href="/docs/linux/man/3-ares_destroy/">ares_destroy</a>(3)</i> or <i><a href="/docs/linux/man/3-ares_cancel/">ares_cancel</a>(3)</i>. </p>
<p> The callback argument <i>arg</i> is copied from the <code>ares_getnameinfo</code> argument <i>arg</i>. The callback argument <i>status</i> indicates whether the query succeeded and, if not, how it failed. It may have any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> The host lookup completed successfully.</p>
<dt><code>ARES_ENOTIMP</code></p>
<dd> The ares library does not know how to look up addresses of type <i>family</i>.</p>
<dt><code>ARES_ENOTFOUND</code></p>
<dd> The address <i>addr</i> was not found.</p>
<dt><code>ARES_ENOMEM</code></p>
<dd> Memory was exhausted.</p>
<dt><code>ARES_ECANCELLED</code></p>
<dd> The query was cancelled.</p>
<dt><code>ARES_EDESTRUCTION</code></p>
<dd> The name service channel <i>channel</i> is being destroyed; the query will not be completed.</p>
<dt><code>ARES_EBADFLAGS</code></p>
<dd> The <i>flags</i> parameter contains an illegal value.</dl>
<p> The callback argument <i>timeouts</i> reports how many times a query timed out during the execution of the given request. </p>
<p> On successful completion of the query, the callback argument <i>node</i> contains a string representing the hostname (assuming <code>ARES_NI_LOOKUPHOST</code> was specified). Additionally, <i>service</i> contains a string representing the service name (assuming <code>ARES_NI_LOOKUPSERVICE</code> was specified). If the query did not complete successfully, or one of the values was not requested, <i>node</i> or <i>service</i> will be <code>NULL</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_process/">ares_process</a></code>(3), <code><a href="/docs/linux/man/3-ares_getaddrinfo/">ares_getaddrinfo</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Dominick Meglio<br />
 Copyright 2005 by Dominick Meglio. </p>
<h2>Index</h2>
