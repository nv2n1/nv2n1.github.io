---
title: "ares_get_servers(3)"
name: "ares_get_servers"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_get_servers/"
description: "ares_get_servers – Retrieve name servers from an initialized ares_channel"
---

<h2>NAME</h2>
<p> ares_get_servers &#8211; Retrieve name servers from an initialized ares_channel</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_get_servers(ares_channel channel, struct ares_addr_node **servers)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-ares_get_servers/">ares_get_servers</a>(3)</code> function retrieves name servers configuration from the channel data identified by <i>channel</i>, as a linked list of ares_addr_node structs storing a pointer to the first node at the address specified by <i>servers</i>. </p>
<p> Function caller may traverse the returned name server linked list, or may use it directly as suitable input for the <code><a href="/docs/linux/man/3-ares_set_servers/">ares_set_servers</a>(3)</code> function, but shall not shrink or extend the list on its own. </p>
<p> Each node of the name server linked list is stored in memory dynamically allocated and managed by c-ares. It is the caller&#8217;s responsibility to free the resulting linked list, using <code><a href="/docs/linux/man/3-ares_free_data/">ares_free_data</a>(3)</code> , once the caller does not need it any longer. </p>
<p> This function is capable of handling IPv4 and IPv6 name server addresses simultaneously, rendering <code><a href="/docs/linux/man/3-ares_save_options/">ares_save_options</a>(3)</code> with optmask <code>ARES_OPT_SERVERS</code> functionally obsolete except for IPv4-only name server usage. </p>
<h2>RETURN VALUES</h2>
<p> <code><a href="/docs/linux/man/3-ares_get_servers/">ares_get_servers</a>(3)</code> may return any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> The name servers configuration was successfuly retrieved</p>
<dt><code>ARES_ENOMEM</code></p>
<dd> The memory was exhausted</p>
<dt><code>ARES_ENODATA</code></p>
<dd> The channel data identified by <i>channel</i> was invalid.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_set_servers/">ares_set_servers</a></code>(3), <code><a href="/docs/linux/man/3-ares_init_options/">ares_init_options</a></code>(3), <code><a href="/docs/linux/man/3-ares_save_options/">ares_save_options</a>(3)</code></p>
<h2>AVAILABILITY</h2>
<p> <a href="/docs/linux/man/3-ares_get_servers/">ares_get_servers</a>(3) was added in c-ares 1.7.1</p>
<h2>AUTHOR</h2>
<p> Implementation of this function and associated library internals are based on code, comments and feedback provided in November and December of 2008 by Daniel Stenberg, Gregor Jasny, Phil Blundell and Yang Tse, December 2009 by Cedric Bail, February 2010 by Jakub Hrozek. On March 2010 Yang Tse shuffled all the bits and this function popped out.<br />
 Copyright 1998 by the Massachusetts Institute of Technology.<br />
 Copyright (C) 2008-2010 by Daniel Stenberg </p>
<h2>Index</h2>
