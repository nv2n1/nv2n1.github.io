---
title: "dnsdist(1)"
name: "dnsdist"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dnsdist/"
description: "dnsdist – tool to balance DNS queries over downstream servers"
---

<h2>NAME</h2>
<p> dnsdist &#8211; tool to balance DNS queries over downstream servers</p>
<h2>SYNOPSIS</h2>
<p> dnsdist [OPTION]&#8230; ADDRESS&#8230;</p>
<h2>DESCRIPTION</h2>
<p> dnsdist receives DNS queries and relays them to one or more downstream servers. It subsequently sends back responses to the original requestor. </p>
<p> dnsdist operates over TCP and UDP, and strives to deliver very high performance over both. </p>
<p> Currently, queries are sent to the downstream server with the least outstanding queries. This effectively implies load balancing, making sure that slower servers get less queries. </p>
<p> If a reply has not come in after a few seconds, it is removed from the queue, but in the short term, timeouts do cause a server to get less traffic. </p>
<p> IPv4 and IPv6 operation can be mixed and matched, in other words, queries coming in over IPv6 could be forwarded to IPv4 and vice versa. </p>
<p> dnsdist is scriptable in Lua, see the dnsdist documentation for more information on this.</p>
<h2>SCOPE</h2>
<p> dnsdist does not &#8216;think&#8217; about DNS, and does not perform any kind of caching, nor is it aware of the quality of the answers it is relaying. </p>
<p> dnsdist assumes that each query leads to exactly one response, which is true for all DNS except for AXFR, which is therefore not supported. </p>
<p> The goal for dnsdist is to remain simple. If more powerful loadbalancing is required, dedicated hardware or software is recommended. Linux Virtual Server for example is often mentioned.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a,&#8211;acl </code>NETMASK</p>
<dd> Add NETMASK to the ACL.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-C,&#8211;config </code>FILE</p>
<dd> Load configuration from FILE.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;check-config</code></p>
<dd> Test the configuration file (which may be set with &#8211;config or -C) for errors. dnsdist will show the errors and exit with a non-zero exit-code when errors are found.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-c,&#8211;client [</code>ADDRESS[:PORT]]</p>
<dd> Operate as a client, connect to dnsdist. This will read the dnsdist configuration for the controlSocket statement and connect to it. When ADDRESS (with optional PORT) is set, dnsdist will connect to that instead.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-k,&#8211;setkey </code>KEY</p>
<dd> When operating as a client(-c, &#8211;client), use KEY as shared secret to connect to dnsdist. This should be the same key that is used on the server (set with setKey()). Note that this will leak the key into your shell&#8217;s history. Only available when dnsdist is compiled with libsodium support.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-d,&#8211;daemon</code></p>
<dd> Operate as a daemon.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-e,&#8211;execute </code>CMD</p>
<dd> Connect to dnsdist and execute CMD.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-h,&#8211;help</code></p>
<dd> Display a helpful message and exit.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-l,&#8211;local </code>ADDRESS</p>
<dd> Bind to ADDRESS, Supply as many addresses (using multiple &#8211;local statements) to listen on as required. Specify IPv4 as 0.0.0.0:53 and IPv6 as [::]:53.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;supervised</code></p>
<dd> Run in foreground, but do not spawn a console. Use this switch to run dnsdist inside a supervisor (use with e.g. systemd and daemontools).</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;disable-syslog</code></p>
<dd> Disable logging to syslog. Use this when running inside a supervisor that handles logging (like systemd). Do not use in combination with &#8211;daemon.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-p,&#8211;pidfile </code>FILE</p>
<dd> Write a pidfile to FILE, works only with &#8211;daemon.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-u,&#8211;uid </code>UID</p>
<dd> Change the process user to UID after binding sockets. UID can be a name or number.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-g,&#8211;gid </code>GID</p>
<dd> Change the process group to GID after binding sockets. GID Can be a name or number.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-V,&#8211;version</code></p>
<dd> Show the dnsdist version and exit.</p>
<dl>
<dt>
<dd></dl>
<dt><code>ADDRESS</code></p>
<dd> Any number of downstream DNS servers, in the same syntax as used with &#8211;local. If the port is not specified, 53 is used.</p>
<dl>
<dt>
<dd></dl>
</dl>
<h2>BUGS</h2>
<p> Right now, the TCP support has some rather arbitrary limits.</p>
<h2>RESOURCES</h2>
<p> Website: <a rel="nofollow" href="http://dnsdist.org">http://dnsdist.org</a></p>
<h2>AUTHORS</h2>
<p> PowerDNS.com BV. </p>
<h2>Index</h2>
