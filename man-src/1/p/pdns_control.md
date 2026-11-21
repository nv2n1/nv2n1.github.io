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
<dt><code>&#8211;help</code></dt>
<dd>
 Show summary of options.</dd>
<dt><code>&#8211;chroot=&#8230;</code></dt>
<dd>
 Where PowerDNS is chrooted</dd>
<dt><code>&#8211;config-dir=&#8230;</code></dt>
<dd>
 Location of configuration directory (pdns.conf)</dd>
<dt><code>&#8211;config-name=&#8230;</code></dt>
<dd>
 Name of this virtual configuration &#8211; will rename the binary image</dd>
<dt><code>&#8211;remote-address=&#8230;</code></dt>
<dd>
 Remote address to query</dd>
<dt><code>&#8211;remote-port=&#8230;</code></dt>
<dd>
 Remote port to query</dd>
<dt><code>&#8211;secret=&#8230;</code></dt>
<dd>
 Secret needed to connect to remote PowerDNS</dd>
<dt><code>&#8211;socket-dir=&#8230;</code></dt>
<dd> Where the controlsocket will live</dd></dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>ccounts</code></dt>
<dd> Show the content of the cache</dd>
<dt><code>notify </code><i>&lt;domain&gt;</i></dt>
<dd> Adds a domain to the notification list, causing PDNS to send out notifications to the nameservers of a domain. Can be used if a slave missed previous notifications or is generally hard of hearing.</dd>
<dt><code>notify-host </code><i>&lt;domain&gt;</i> <i>&lt;host&gt;</i></dt>
<dd> Same as above but with operator specified IP address as destination, to be used if you know better than PowerDNS.</dd>
<dt><code>cycle</code></dt>
<dd> Restart the nameserver so it reloads its configuration.</dd>
<dt><code>ping</code></dt>
<dd> Check if the server is alive.</dd>
<dt><code>purge </code><i>[&lt;record&gt;]</i></dt>
<dd> Purge entries from the packet cache. If the record name ends with a dollar ($) all entries that end with that name are removed. If no record is specified the entire cache is purged.</dd>
<dt><code>rediscover</code></dt>
<dd> Instructs backends that new domains may have appeared in the database, or, in the case of the Bind backend, in named.conf.</dd>
<dt><code>retrieve </code><i>&lt;domain&gt;</i></dt>
<dd> Retrieve a slave domain from its master. Done nearly immediately.</dd>
<dt><code>set </code><i>&lt;variable&gt; &lt;value&gt;</i></dt>
<dd> Set the configuration parameter <i>&lt;variable&gt;</i> to <i>&lt;value&gt;</i>. Currently only the <i>query-logging</i> can be set.</dd>
<dt><code>show </code><i>&lt;variable&gt;</i></dt>
<dd> Show a single statistic, as present in the output of the list command.</dd>
<dt><code>quit</code></dt>
<dd> Tell a running <code>pdns_server</code> to quit.</dd>
<dt><code>status</code></dt>
<dd> Show usage statistics.</dd>
<dt><code>uptime</code></dt>
<dd> Show the uptime of the running server.</dd>
<dt><code>version</code></dt>
<dd> Print the version of the running pdns daemon.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>&lt;socket&gt;</i></dt>
<dd> Control socket used to communicate with <code>pdns_server</code>.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>pdns_server</code>(8) </p>
