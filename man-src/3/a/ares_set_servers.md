---
title: "ares_set_servers(3)"
name: "ares_set_servers"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_set_servers/"
description: "ares_set_servers – Initialize an ares_channel name servers configuration"
---

<h2>NAME</h2>
<p> ares_set_servers &#8211; Initialize an ares_channel name servers configuration</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_set_servers(ares_channel channel, struct ares_addr_node *servers)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-ares_set_servers/">ares_set_servers</a>(3)</code> function initializes name servers configuration for the channel data identified by <i>channel</i>, from a <i>servers</i> pointer to a linked list of ares_addr_node structs holding name servers address data. </p>
<p> The name server linked list pointer argument may be the result of a previous call to <code><a href="/docs/linux/man/3-ares_get_servers/">ares_get_servers</a>(3)</code> or a linked list of ares_addr_node structs setup by other means. </p>
<p> This function replaces any potentially previously configured name servers with the ones given in the linked list. So, in order to configure a channel with more than one name server all the desired ones must be specified in a single list. </p>
<p> <code><a href="/docs/linux/man/3-ares_set_servers/">ares_set_servers</a>(3)</code> does not take ownership of the linked list argument. The caller is responsible for freeing the linked list when no longer needed. </p>
<p> This function is capable of handling IPv4 and IPv6 name server addresses simultaneously, rendering <code><a href="/docs/linux/man/3-ares_init_options/">ares_init_options</a>(3)</code> with optmask <code>ARES_OPT_SERVERS</code> functionally obsolete except for IPv4-only name server usage. </p>
<h2>RETURN VALUES</h2>
<p> <code><a href="/docs/linux/man/3-ares_set_servers/">ares_set_servers</a>(3)</code> may return any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> The name servers configuration was successfuly initialized.</p>
<dt><code>ARES_ENOMEM</code></p>
<dd> The process&#8217;s available memory was exhausted.</p>
<dt><code>ARES_ENODATA</code></p>
<dd> The channel data identified by <i>channel</i> was invalid.</p>
<dt><code>ARES_ENOTINITIALIZED</code></p>
<dd> c-ares library initialization not yet performed.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_set_servers_csv/">ares_set_servers_csv</a></code>(3), <code><a href="/docs/linux/man/3-ares_get_servers/">ares_get_servers</a></code>(3), <code><a href="/docs/linux/man/3-ares_init_options/">ares_init_options</a></code>(3), <code><a href="/docs/linux/man/3-ares_dup/">ares_dup</a>(3)</code></p>
<h2>AVAILABILITY</h2>
<p> <a href="/docs/linux/man/3-ares_set_servers/">ares_set_servers</a>(3) was added in c-ares 1.7.1</p>
<h2>AUTHOR</h2>
<p> Implementation of this function and associated library internals are based on code, comments and feedback provided in November and December of 2008 by Daniel Stenberg, Gregor Jasny, Phil Blundell and Yang Tse, December 2009 by Cedric Bail, February 2010 by Jakub Hrozek. On March 2010 Yang Tse shuffled all the bits and this function popped out.<br />
 Copyright 1998 by the Massachusetts Institute of Technology.<br />
 Copyright (C) 2008-2010 by Daniel Stenberg </p>
<h2>Index</h2>
