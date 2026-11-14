---
title: "ares_gethostbyaddr(3)"
name: "ares_gethostbyaddr"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_gethostbyaddr/"
description: "ares_gethostbyaddr – Initiate a host query by address"
---

<h2>NAME</h2>
<p> ares_gethostbyaddr &#8211; Initiate a host query by address</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
typedef void (*ares_host_callback)(void *arg, int status,
void ares_gethostbyaddr(ares_channel channel, const void *addr,
int addrlen, int family, ares_host_callback callback,
void *arg)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_gethostbyaddr</code> function initiates a host query by address on the name service channel identified by <i>channel</i>. The parameters <i>addr</i> and <i>addrlen</i> give the address as a series of bytes, and <i>family</i> gives the type of address. When the query is complete or has failed, the ares library will invoke <i>callback</i>. Completion or failure of the query may happen immediately, or may happen during a later call to <i><a href="/docs/linux/man/3-ares_process/">ares_process</a>(3)</i>, <i><a href="/docs/linux/man/3-ares_destroy/">ares_destroy</a>(3)</i> or <i><a href="/docs/linux/man/3-ares_cancel/">ares_cancel</a>(3)</i>. </p>
<p> The callback argument <i>arg</i> is copied from the <code>ares_gethostbyaddr</code> argument <i>arg</i>. The callback argument <i>status</i> indicates whether the query succeeded and, if not, how it failed. It may have any of the following values:</p>
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
<dd> The name service channel <i>channel</i> is being destroyed; the query will not be completed.</dl>
<p> The callback argument <i>timeouts</i> reports how many times a query timed out during the execution of the given request. </p>
<p> On successful completion of the query, the callback argument <i>hostent</i> points to a <code>struct hostent</code> containing the name of the host returned by the query. The callback need not and should not attempt to free the memory pointed to by <i>hostent</i>; the ares library will free it when the callback returns. If the query did not complete successfully, <i>hostent</i> will be <code>NULL</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_process/">ares_process</a></code>(3), <code><a href="/docs/linux/man/3-ares_gethostbyname/">ares_gethostbyname</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
