---
title: "ares_query(3)"
name: "ares_query"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_query/"
description: "ares_query – Initiate a single-question DNS query"
---

<h2>NAME</h2>
<p> ares_query &#8211; Initiate a single-question DNS query</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
typedef void (*ares_callback)(void *arg, int status,
void ares_query(ares_channel channel, const char *name,
int dnsclass, int type, ares_callback callback,
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_query</code> function initiates a single-question DNS query on the name service channel identified by <i>channel</i>. The parameter <i>name</i> gives the query name as a NUL-terminated C string of period-separated labels optionally ending with a period; periods and backslashes within a label must be escaped with a backslash. The parameters <i>dnsclass</i> and <i>type</i> give the class and type of the query using the values defined in <code>&lt;arpa/nameser.h&gt;</code>. When the query is complete or has failed, the ares library will invoke <i>callback</i>. Completion or failure of the query may happen immediately, or may happen during a later call to <code><a href="/docs/linux/man/3-ares_process/">ares_process</a></code>(3) or <code><a href="/docs/linux/man/3-ares_destroy/">ares_destroy</a></code>(3). </p>
<p> The callback argument <i>arg</i> is copied from the <code>ares_query</code> argument <i>arg</i>. The callback argument <i>status</i> indicates whether the query succeeded and, if not, how it failed. It may have any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> The query completed successfully.</p>
<dt><code>ARES_ENODATA</code></p>
<dd> The query completed but contains no answers.</p>
<dt><code>ARES_EFORMERR</code></p>
<dd> The query completed but the server claims that the query was malformatted.</p>
<dt><code>ARES_ESERVFAIL</code></p>
<dd> The query completed but the server claims to have experienced a failure. (This code can only occur if the <code>ARES_FLAG_NOCHECKRESP</code> flag was specified at channel initialization time; otherwise, such responses are ignored at the <code><a href="/docs/linux/man/3-ares_send/">ares_send</a></code>(3) level.)</p>
<dt><code>ARES_ENOTFOUND</code></p>
<dd> The query completed but the queried-for domain name was not found.</p>
<dt><code>ARES_ENOTIMP</code></p>
<dd> The query completed but the server does not implement the operation requested by the query. (This code can only occur if the <code>ARES_FLAG_NOCHECKRESP</code> flag was specified at channel initialization time; otherwise, such responses are ignored at the <code><a href="/docs/linux/man/3-ares_send/">ares_send</a></code>(3) level.)</p>
<dt><code>ARES_EREFUSED</code></p>
<dd> The query completed but the server refused the query. (This code can only occur if the <code>ARES_FLAG_NOCHECKRESP</code> flag was specified at channel initialization time; otherwise, such responses are ignored at the <code><a href="/docs/linux/man/3-ares_send/">ares_send</a></code>(3) level.)</p>
<dt><code>ARES_EBADNAME</code></p>
<dd> The query name <i>name</i> could not be encoded as a domain name, either because it contained a zero-length label or because it contained a label of more than 63 characters.</p>
<dt><code>ARES_ETIMEOUT</code></p>
<dd> No name servers responded within the timeout period.</p>
<dt><code>ARES_ECONNREFUSED</code></p>
<dd> No name servers could be contacted.</p>
<dt><code>ARES_ENOMEM</code></p>
<dd> Memory was exhausted.</p>
<dt><code>ARES_ECANCELLED</code></p>
<dd> The query was cancelled.</p>
<dt><code>ARES_EDESTRUCTION</code></p>
<dd> The name service channel <i>channel</i> is being destroyed; the query will not be completed.</dl>
<p> The callback argument <i>timeouts</i> reports how many times a query timed out during the execution of the given request. </p>
<p> If the query completed (even if there was something wrong with it, as indicated by some of the above error codes), the callback argument <i>abuf</i> points to a result buffer of length <i>alen</i>. If the query did not complete, <i>abuf</i> will be NULL and <i>alen</i> will be 0.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_process/">ares_process</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
