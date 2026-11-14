---
title: "pdns_control(1)"
name: "pdns_control"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdns_control/"
description: "pdns_control – Control the PowerDNS nameserver"
---

<h2>NAME</h2>
<p> pdns_control &#8211; Control the PowerDNS nameserver</p>
<h2>SYNOPSIS</h2>
<p> <code>pdns_control </code><i>[options]</i> command</p>
<h2>DESCRIPTION</h2>
<p> <code>pdns_control</code> is used to send commands to a running PowerDNS nameserver.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd>
 Show summary of options.</p>
<dt><code>&#8211;chroot=&#8230;</code></p>
<dd>
 Where PowerDNS is chrooted</p>
<dt><code>&#8211;config-dir=&#8230;</code></p>
<dd>
 Location of configuration directory (pdns.conf)</p>
<dt><code>&#8211;config-name=&#8230;</code></p>
<dd>
 Name of this virtual configuration &#8211; will rename the binary image</p>
<dt><code>&#8211;remote-address=&#8230;</code></p>
<dd>
 Remote address to query</p>
<dt><code>&#8211;remote-port=&#8230;</code></p>
<dd>
 Remote port to query</p>
<dt><code>&#8211;secret=&#8230;</code></p>
<dd>
 Secret needed to connect to remote PowerDNS</p>
<dt><code>&#8211;socket-dir=&#8230;</code></p>
<dd> Where the controlsocket will live</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>ccounts</code></p>
<dd> Show the content of the cache</p>
<dt><code>notify </code><i>&lt;domain&gt;</i></p>
<dd> Adds a domain to the notification list, causing PDNS to send out notifications to the nameservers of a domain. Can be used if a slave missed previous notifications or is generally hard of hearing.</p>
<dt><code>notify-host </code><i>&lt;domain&gt;</i> <i>&lt;host&gt;</i></p>
<dd> Same as above but with operator specified IP address as destination, to be used if you know better than PowerDNS.</p>
<dt><code>cycle</code></p>
<dd> Restart the nameserver so it reloads its configuration.</p>
<dt><code>ping</code></p>
<dd> Check if the server is alive.</p>
<dt><code>purge </code><i>[&lt;record&gt;]</i></p>
<dd> Purge entries from the packet cache. If the record name ends with a dollar ($) all entries that end with that name are removed. If no record is specified the entire cache is purged.</p>
<dt><code>rediscover</code></p>
<dd> Instructs backends that new domains may have appeared in the database, or, in the case of the Bind backend, in named.conf.</p>
<dt><code>retrieve </code><i>&lt;domain&gt;</i></p>
<dd> Retrieve a slave domain from its master. Done nearly immediately.</p>
<dt><code>set </code><i>&lt;variable&gt; &lt;value&gt;</i></p>
<dd> Set the configuration parameter <i>&lt;variable&gt;</i> to <i>&lt;value&gt;</i>. Currently only the <i>query-logging</i> can be set.</p>
<dt><code>show </code><i>&lt;variable&gt;</i></p>
<dd> Show a single statistic, as present in the output of the list command.</p>
<dt><code>quit</code></p>
<dd> Tell a running <code>pdns_server</code> to quit.</p>
<dt><code>status</code></p>
<dd> Show usage statistics.</p>
<dt><code>uptime</code></p>
<dd> Show the uptime of the running server.</p>
<dt><code>version</code></p>
<dd> Print the version of the running pdns daemon.</dl>
<h2>FILES</h2>
<dl>
<dt><i>&lt;socket&gt;</i></p>
<dd> Control socket used to communicate with <code>pdns_server</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-pdns_server/">pdns_server</a></code>(8) </p>
<h2>Index</h2>
