---
title: "ares_free_data(3)"
name: "ares_free_data"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_free_data/"
description: "ares_free_data – Free data allocated by several c-ares functions"
---

<h2>NAME</h2>
<p> ares_free_data &#8211; Free data allocated by several c-ares functions</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
void ares_free_data(void *dataptr)
        cc file.c
    - lcares
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-ares_free_data/">ares_free_data</a>(3)</code> function frees one or more data structures allocated and returned by several c-ares functions. Specifically the data returned by the following list of functions must be deallocated using this function.</p>
<dl>
<dt><code><a href="/docs/linux/man/3-ares_get_servers/">ares_get_servers</a>(3)</code></p>
<dd> When used to free the data returned by <a href="/docs/linux/man/3-ares_get_servers/">ares_get_servers</a>(3) this will free the whole linked list of ares_addr_node structures returned by <a href="/docs/linux/man/3-ares_get_servers/">ares_get_servers</a>(3).</p>
<dt><code><a href="/docs/linux/man/3-ares_parse_srv_reply/">ares_parse_srv_reply</a>(3)</code></p>
<dd> When used to free the data returned by <a href="/docs/linux/man/3-ares_parse_srv_reply/">ares_parse_srv_reply</a>(3) this will free the whole linked list of ares_srv_reply structures returned by <a href="/docs/linux/man/3-ares_parse_srv_reply/">ares_parse_srv_reply</a>(3), along with any additional storage associated with those structures.</p>
<dt><code><a href="/docs/linux/man/3-ares_parse_mx_reply/">ares_parse_mx_reply</a>(3)</code></p>
<dd> When used to free the data returned by <a href="/docs/linux/man/3-ares_parse_mx_reply/">ares_parse_mx_reply</a>(3) this will free the whole linked list of ares_mx_reply structures returned by <a href="/docs/linux/man/3-ares_parse_mx_reply/">ares_parse_mx_reply</a>(3), along with any additional storage associated with those structures.</p>
<dt><code><a href="/docs/linux/man/3-ares_parse_txt_reply/">ares_parse_txt_reply</a>(3)</code></p>
<dd> When used to free the data returned by <a href="/docs/linux/man/3-ares_parse_txt_reply/">ares_parse_txt_reply</a>(3) this will free the whole linked list of ares_txt_reply structures returned by <a href="/docs/linux/man/3-ares_parse_txt_reply/">ares_parse_txt_reply</a>(3), along with any additional storage associated with those structures.</p>
<dt><code><a href="/docs/linux/man/3-ares_parse_soa_reply/">ares_parse_soa_reply</a>(3)</code></p>
<dd> When used to free the data returned by <a href="/docs/linux/man/3-ares_parse_soa_reply/">ares_parse_soa_reply</a>(3) this will free the ares_soa_reply structure, along with any additional storage associated with those structure.</dl>
<h2>RETURN VALUE</h2>
<p> The ares_free_data() function does not return a value.</p>
<h2>AVAILABILITY</h2>
<p> This function was first introduced in c-ares version 1.7.0.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_get_servers/">ares_get_servers</a>(3),</code> <code><a href="/docs/linux/man/3-ares_parse_srv_reply/">ares_parse_srv_reply</a>(3),</code> <code><a href="/docs/linux/man/3-ares_parse_mx_reply/">ares_parse_mx_reply</a>(3),</code> <code><a href="/docs/linux/man/3-ares_parse_txt_reply/">ares_parse_txt_reply</a>(3),</code> <code><a href="/docs/linux/man/3-ares_parse_soa_reply/">ares_parse_soa_reply</a>(3)</code></p>
<h2>AUTHOR</h2>
<p> Yang Tse </p>
<p> Copyright 1998 by the Massachusetts Institute of Technology.<br />
 Copyright (C) 2004-2010 by Daniel Stenberg. </p>
<h2>Index</h2>
