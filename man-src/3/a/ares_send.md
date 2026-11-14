---
title: "ares_send(3)"
name: "ares_send"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_send/"
description: "ares_send – Initiate a DNS query"
---

<h2>NAME</h2>
<p> ares_send &#8211; Initiate a DNS query</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
typedef void (*ares_callback)(void *arg, int status,
void ares_send(ares_channel channel, const unsigned char *qbuf,
int qlen, ares_callback callback, void *arg)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_send</code> function initiates a DNS query on the name service channel identified by <i>channel</i>. The parameters <i>qbuf</i> and <i>qlen</i> give the DNS query, which should already have been formatted according to the DNS protocol. When the query is complete or has failed, the ares library will invoke <i>callback</i>. Completion or failure of the query may happen immediately, or may happen during a later call to <code><a href="/docs/linux/man/3-ares_process/">ares_process</a></code>(3) or <code><a href="/docs/linux/man/3-ares_destroy/">ares_destroy</a></code>(3). </p>
<p> The callback argument <i>arg</i> is copied from the <code>ares_send</code> argument <i>arg</i>. The callback argument <i>status</i> indicates whether the query succeeded and, if not, how it failed. It may have any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> The query completed.</p>
<dt><code>ARES_EBADQUERY</code></p>
<dd> The query buffer was poorly formed (was not long enough for a DNS header or was too long for TCP transmission).</p>
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
<p> If the query completed, the callback argument <i>abuf</i> points to a result buffer of length <i>alen</i>. If the query did not complete, <i>abuf</i> will be NULL and <i>alen</i> will be 0. </p>
<p> Unless the flag <code>ARES_FLAG_NOCHECKRESP</code> was set at channel initialization time, <code>ares_send</code> will normally ignore responses whose questions do not match the questions in <i>qbuf</i>, as well as responses with reply codes of <code>SERVFAIL</code>, <code>NOTIMP</code>, and <code>REFUSED</code>. Unlike other query functions in the ares library, however, <code>ares_send</code> does not inspect the header of the reply packet to determine the error status, so a callback status of <code>ARES_SUCCESS</code> does not reflect as much about the response as for other query functions.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_process/">ares_process</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
