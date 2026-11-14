---
title: "avahi-browse(1)"
name: "avahi-browse"
section: "1"
letter: "a"
url: "/docs/linux/man/1-avahi-browse/"
description: "avahi-browse – Browse for mDNS/DNS-SD services using the Avahi daemon"
---

<h2 class="name">NAME</h2>
<p> avahi-browse &#8211; Browse for mDNS/DNS-SD services using the Avahi daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>avahi-browse [</code><i>options</i><code>] </code><i>service-type</i><code> </p>
<p> avahi-browse [</code><i>options</i><code>] &#8211;all </p>
<p> avahi-browse [</code><i>options</i><code>] &#8211;browse-domains </p>
<p> avahi-browse [</code><i>options</i><code>] &#8211;dump-db </p>
<p> avahi-browse-domains [</code><i>options</i><code>] </code></p>
<h2>DESCRIPTION</h2>
<p> Browse for mDNS/DNS-SD network services and browsing domains using the Avahi daemon.</p>
<h2>OPTIONS</h2>
<p> Specify a DNS-SD service type (e.g. _http._tcp) to browse for on the command line, or <code>-a</code> to browse for all available service types. Items that appear on the network are prefixed with &quot;+&quot;, items that disappear are prefixed with &quot;-&quot;. If <code>&#8211;resolve</code> is passed items that are resolved are prefixed with &quot;=&quot;.</p>
<dl>
<dt><code>-a | &#8211;all</code></p>
<dd> Browse for all service types registered on the LAN, not just the one specified on the command line.</p>
<dt><code>-D | &#8211;browse-domains</code></p>
<dd> Browse for browsing domains instead for services. avahi-browse-domains is equivalent to avahi-browse &#8211;browse-domains</p>
<dt><code>-d | &#8211;domain=</code> <i>DOMAIN</i></p>
<dd> Browse in the specified domain. If omitted avahi-browse will browse in the default browsing domain (usually: local)</p>
<dt><code>-v | &#8211;verbose</code></p>
<dd> Enable verbose mode.</p>
<dt><code>-t | &#8211;terminate</code></p>
<dd> Terminate after dumping a more or less complete list.</p>
<dt><code>-c | &#8211;cache</code></p>
<dd> Terminate after dumping all entries available in the cache.</p>
<dt><code>-l | &#8211;ignore-local</code></p>
<dd> Ignore local services, show only remote services.</p>
<dt><code>-r | &#8211;resolve</code></p>
<dd> Automatically resolve services found.</p>
<dt><code>-f | &#8211;no-fail</code></p>
<dd> Don&#8217;t fail if the daemon is not found running. Instead, wait until it appears. If it disconnects, try to reconnect.</p>
<dt><code>-p | &#8211;parsable</code></p>
<dd> Make output easily parsable for usage in scripts. If enabled fields are separated by semicolons (;), service names are escaped. It is recommended to combine this with <code>&#8211;no-db-lookup</code>.</p>
<dt><code>-k | &#8211;no-db-lookup</code></p>
<dd> Don&#8217;t lookup services types in service type database.</p>
<dt><code>-b | &#8211;dump-db</code></p>
<dd> Dump the service type database (may be combined with -k)</p>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help.</p>
<dt><code>-V | &#8211;version</code></p>
<dd> Show version information.</dl>
<h2>AUTHORS</h2>
<p> The Avahi Developers &lt;avahi (at) lists (dot) freedesktop (dot) org&gt;; Avahi is available from <code><a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avahi-publish/">avahi-publish</a>(1)</code>, <code><a href="/docs/linux/man/1-avahi-resolve/">avahi-resolve</a>(1)</code>, <code><a href="/docs/linux/man/8-avahi-daemon/">avahi-daemon</a>(8)</code></p>
<h2>COMMENTS</h2>
<p> This man page was written using <code><a href="/docs/linux/man/1-xml2man/">xml2man</a>(1)</code> by Oliver Kurth. </p>
<h2>Index</h2>
