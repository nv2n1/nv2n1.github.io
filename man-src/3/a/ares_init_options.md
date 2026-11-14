---
title: "ares_init_options(3)"
name: "ares_init_options"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_init_options/"
description: "ares_init, ares_init_options – Initialize a resolver channel"
---

<h2>NAME</h2>
<p> ares_init, ares_init_options &#8211; Initialize a resolver channel</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_init(ares_channel *channelptr) int ares_init_options(ares_channel *channelptr,
                                                              struct ares_options *options, int optmask)
        cc file.c
    - lcares
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_init</code> function initializes a communications channel for name service lookups. If it returns successfully, <code>ares_init</code> will set the variable pointed to by <i>channelptr</i> to a handle used to identify the name service channel. The caller should invoke <code><a href="/docs/linux/man/3-ares_destroy/">ares_destroy</a></code>(3) on the handle when the channel is no longer needed. </p>
<p> The <code>ares_init_options</code> function also initializes a name service channel, with additional options useful for applications requiring more control over name service configuration. The <i>optmask</i> parameter specifies which fields in the structure pointed to by <i>options</i> are set, as follows:</p>
<dl>
<dt><code>ARES_OPT_FLAGS</code></p>
<dd> <code>int </code><i>flags</i>;<br />
 Flags controlling the behavior of the resolver. See below for a description of possible flag values.</p>
<dt><code>ARES_OPT_TIMEOUT</code></p>
<dd> <code>int </code><i>timeout</i>;<br />
 The number of seconds each name server is given to respond to a query on the first try. (After the first try, the timeout algorithm becomes more complicated, but scales linearly with the value of <i>timeout</i>.) The default is five seconds. This option is being deprecated by <i>ARES_OPT_TIMEOUTMS</i> starting in c-ares 1.5.2.</p>
<dt><code>ARES_OPT_TIMEOUTMS</code></p>
<dd> <code>int </code><i>timeout</i>;<br />
 The number of milliseconds each name server is given to respond to a query on the first try. (After the first try, the timeout algorithm becomes more complicated, but scales linearly with the value of <i>timeout</i>.) The default is five seconds. Note that this option is specified with the same struct field as the former <i>ARES_OPT_TIMEOUT</i>, it is but the option bits that tell c-ares how to interpret the number. This option was added in c-ares 1.5.2.</p>
<dt><code>ARES_OPT_TRIES</code></p>
<dd> <code>int </code><i>tries</i>;<br />
 The number of tries the resolver will try contacting each name server before giving up. The default is four tries.</p>
<dt><code>ARES_OPT_NDOTS</code></p>
<dd> <code>int </code><i>ndots</i>;<br />
 The number of dots which must be present in a domain name for it to be queried for &quot;as is&quot; prior to querying for it with the default domain extensions appended. The default value is 1 unless set otherwise by resolv.conf or the RES_OPTIONS environment variable.</p>
<dt><code>ARES_OPT_PORT</code></p>
<dd> <code>unsigned short </code><i>port</i>;<br />
 The port to use for queries (both TCP and UDP), in network byte order. The default value is 53 (in network byte order), the standard name service port.</p>
<dt><code>ARES_OPT_SERVERS</code></p>
<dd> <code>struct in_addr *</code><i>servers</i>;<br />
 <code>int </code><i>nservers</i>;<br />
 The list of IPv4 servers to contact, instead of the servers specified in resolv.conf or the local named. In order to allow specification of either IPv4 or IPv6 name servers, the <code><a href="/docs/linux/man/3-ares_set_servers/">ares_set_servers</a>(3)</code> function must be used instead.</p>
<dt><code>ARES_OPT_DOMAINS</code></p>
<dd> <code>char **</code><i>domains</i>;<br />
 <code>int </code><i>ndomains</i>;<br />
 The domains to search, instead of the domains specified in resolv.conf or the domain derived from the kernel hostname variable.</p>
<dt><code>ARES_OPT_LOOKUPS</code></p>
<dd> <code>char *</code><i>lookups</i>;<br />
 The lookups to perform for host queries. <i>lookups</i> should be set to a string of the characters &quot;b&quot; or &quot;f&quot;, where &quot;b&quot; indicates a DNS lookup and &quot;f&quot; indicates a lookup in the hosts file.</p>
<dt><code>ARES_OPT_SOCK_STATE_CB</code></p>
<dd> <code>void (*</code><i>sock_state_cb</i>)(void *data, int s, int read, int write);<br />
 <code>void *</code><i>sock_state_cb_data</i>;<br />
 A callback function to be invoked when a socket changes state. <i>s</i> will be passed the socket whose state has changed; <i>read</i> will be set to true if the socket should listen for read events, and <i>write</i> will be set to true if the socket should listen for write events. The value of <i>sock_state_cb_data</i> will be passed as the <i>data</i> argument.</dl>
<p> The <i>flags</i> field should be the bitwise or of some subset of the following values:</p>
<dl>
<dt><code>ARES_FLAG_USEVC</code></p>
<dd> Always use TCP queries (the &quot;virtual circuit&quot;) instead of UDP queries. Normally, TCP is only used if a UDP query yields a truncated result.</p>
<dt><code>ARES_FLAG_PRIMARY</code></p>
<dd> Only query the first server in the list of servers to query.</p>
<dt><code>ARES_FLAG_IGNTC</code></p>
<dd> If a truncated response to a UDP query is received, do not fall back to TCP; simply continue on with the truncated response.</p>
<dt><code>ARES_FLAG_NORECURSE</code></p>
<dd> Do not set the &quot;recursion desired&quot; bit on outgoing queries, so that the name server being contacted will not try to fetch the answer from other servers if it doesn&#8217;t know the answer locally. Be aware that ares will not do the recursion for you. Recursion must be handled by the application calling ares if <i>ARES_FLAG_NORECURSE</i> is set.</p>
<dt><code>ARES_FLAG_STAYOPEN</code></p>
<dd> Do not close communications sockets when the number of active queries drops to zero.</p>
<dt><code>ARES_FLAG_NOSEARCH</code></p>
<dd> Do not use the default search domains; only query hostnames as-is or as aliases.</p>
<dt><code>ARES_FLAG_NOALIASES</code></p>
<dd> Do not honor the HOSTALIASES environment variable, which normally specifies a file of hostname translations.</p>
<dt><code>ARES_FLAG_NOCHECKRESP</code></p>
<dd> Do not discard responses with the SERVFAIL, NOTIMP, or REFUSED response code or responses whose questions don&#8217;t match the questions in the request. Primarily useful for writing clients which might be used to test or debug name servers.</dl>
<h2>RETURN VALUES</h2>
<p> <i>ares_init</i> or <i>ares_init_options</i> can return any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> Initialization succeeded.</p>
<dt><code>ARES_EFILE</code></p>
<dd> A configuration file could not be read.</p>
<dt><code>ARES_ENOMEM</code></p>
<dd> The process&#8217;s available memory was exhausted.</p>
<dt><code>ARES_ENOTINITIALIZED</code></p>
<dd> c-ares library initialization not yet performed.</dl>
<h2>NOTES</h2>
<p> When initializing from <code>/etc/resolv.conf,</code> <code><a href="/docs/linux/man/3-ares_init/">ares_init</a></code>(3) reads the <i>domain</i> and <i>search</i> directives to allow lookups of short names relative to the domains specified. The <i>domain</i> and <i>search</i> directives override one another. If more that one instance of either <i>domain</i> or <i>search</i> directives is specified, the last occurence wins. For more information, please see the <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5) manual page.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_destroy/">ares_destroy</a>(3),</code> <code><a href="/docs/linux/man/3-ares_dup/">ares_dup</a>(3),</code> <code><a href="/docs/linux/man/3-ares_library_init/">ares_library_init</a>(3),</code> <code><a href="/docs/linux/man/3-ares_set_servers/">ares_set_servers</a>(3)</code></p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 1998 by the Massachusetts Institute of Technology.<br />
 Copyright (C) 2004-2010 by Daniel Stenberg. </p>
<h2>Index</h2>
