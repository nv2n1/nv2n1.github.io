---
title: "ares_search(3)"
name: "ares_search"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_search/"
description: "ares_search – Initiate a DNS query with domain search"
---

<h2>NAME</h2>
<p> ares_search &#8211; Initiate a DNS query with domain search</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
typedef void (*ares_callback)(void *arg, int status,
void ares_search(ares_channel channel, const char *name,
int dnsclass, int type, ares_callback callback,
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_search</code> function initiates a series of single-question DNS queries on the name service channel identified by <i>channel</i>, using the channel&#8217;s search domains as well as a host alias file given by the HOSTALIAS environment variable. The parameter <i>name</i> gives the alias name or the base of the query name as a NUL-terminated C string of period-separated labels; if it ends with a period, the channel&#8217;s search domains will not be used. Periods and backslashes within a label must be escaped with a backslash. The parameters <i>dnsclass</i> and <i>type</i> give the class and type of the query using the values defined in <code>&lt;arpa/nameser.h&gt;</code>. When the query sequence is complete or has failed, the ares library will invoke <i>callback</i>. Completion or failure of the query sequence may happen immediately, or may happen during a later call to <code><a href="/docs/linux/man/3-ares_process/">ares_process</a></code>(3) or <code><a href="/docs/linux/man/3-ares_destroy/">ares_destroy</a></code>(3). </p>
<p> The callback argument <i>arg</i> is copied from the <code>ares_search</code> argument <i>arg</i>. The callback argument <i>status</i> indicates whether the query sequence ended with a successful query and, if not, how the query sequence failed. It may have any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> A query completed successfully.</p>
<dt><code>ARES_ENODATA</code></p>
<dd> No query completed successfully; when the query was tried without a search domain appended, a response was returned with no answers.</p>
<dt><code>ARES_EFORMERR</code></p>
<dd> A query completed but the server claimed that the query was malformatted.</p>
<dt><code>ARES_ESERVFAIL</code></p>
<dd> No query completed successfully; when the query was tried without a search domain appended, the server claimed to have experienced a failure. (This code can only occur if the <code>ARES_FLAG_NOCHECKRESP</code> flag was specified at channel initialization time; otherwise, such responses are ignored at the <code><a href="/docs/linux/man/3-ares_send/">ares_send</a></code>(3) level.)</p>
<dt><code>ARES_ENOTFOUND</code></p>
<dd> No query completed successfully; when the query was tried without a search domain appended, the server reported that the queried-for domain name was not found.</p>
<dt><code>ARES_ENOTIMP</code></p>
<dd> A query completed but the server does not implement the operation requested by the query. (This code can only occur if the <code>ARES_FLAG_NOCHECKRESP</code> flag was specified at channel initialization time; otherwise, such responses are ignored at the <code><a href="/docs/linux/man/3-ares_send/">ares_send</a></code>(3) level.)</p>
<dt><code>ARES_EREFUSED</code></p>
<dd> A query completed but the server refused the query. (This code can only occur returned if the <code>ARES_FLAG_NOCHECKRESP</code> flag was specified at channel initialization time; otherwise, such responses are ignored at the <code><a href="/docs/linux/man/3-ares_send/">ares_send</a></code>(3) level.)</p>
<dt><code>ARES_TIMEOUT</code></p>
<dd> No name servers responded to a query within the timeout period.</p>
<dt><code>ARES_ECONNREFUSED</code></p>
<dd> No name servers could be contacted.</p>
<dt><code>ARES_ENOMEM</code></p>
<dd> Memory was exhausted.</p>
<dt><code>ARES_ECANCELLED</code></p>
<dd> The query was cancelled.</p>
<dt><code>ARES_EDESTRUCTION</code></p>
<dd> The name service channel <i>channel</i> is being destroyed; the query will not be completed.</dl>
<p> The callback argument <i>timeouts</i> reports how many times a query timed out during the execution of the given request. </p>
<p> If a query completed successfully, the callback argument <i>abuf</i> points to a result buffer of length <i>alen</i>. If the query did not complete successfully, <i>abuf</i> will usually be NULL and <i>alen</i> will usually be 0, but in some cases an unsuccessful query result may be placed in <i>abuf</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_process/">ares_process</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
