---
title: "avahi-publish(1)"
name: "avahi-publish"
section: "1"
letter: "a"
url: "/docs/linux/man/1-avahi-publish/"
description: "avahi-publish-service – Register an mDNS/DNS-SD service or host name or address mapping using the Avahi daemon"
---

<h2 class="name">NAME</h2>
<p> avahi-publish-service &#8211; Register an mDNS/DNS-SD service or host name or address mapping using the Avahi daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>avahi-publish -s [</code><i>options</i><code>] </code><i>name</i><i>service-type</i><i>port</i><code> [</code><i>TXT data</i><code> &#8230;] </p>
<p> avahi-publish-service [</code><i>options</i><code>] </code><i>name</i><i>service-type</i><i>port</i><code> [</code><i>TXT data</i><code> &#8230;] </p>
<p> avahi-publish -a [</code><i>options</i><code>] </code><i>host name</i><i>address</i><code> </p>
<p> avahi-publish-address [</code><i>options</i><code>] </code><i>host name</i><i>address</i></p>
<h2>DESCRIPTION</h2>
<p> Register an mDNS/DNS-SD service or host name/address mapping using the Avahi daemon.</p>
<h2>OPTIONS</h2>
<p> When calling in service registration mode, specify a DNS-SD service name (e.g. &quot;Lennart&#8217;s Files&quot;), a service type (e.g. _http._tcp) and an IP port number for the service, optionally followed by any number of TXT record strings on the command line. When calling in address/host name registration mode specify a fully qualified host name and an address (IPv4 or IPv6).</p>
<dl>
<dt><code>-s | &#8211;service</code></p>
<dd> Register a service. avahi-publish-service is equivalent to avahi-publish -s.</p>
<dt><code>-a | &#8211;address</code></p>
<dd> Register an address/host name mapping. avahi-publish-address is equivalent to avahi-publish -a.</p>
<dt><code>-v | &#8211;verbose</code></p>
<dd> Enable verbose mode.</p>
<dt><code>-H | &#8211;host=</code> <i>HOSTNAME</i></p>
<dd> Specify a host name for this service, in case it doesn&#8217;t reside on the local host. This host name needs to be fully qualified and resolvable using mDNS or unicast DNS.</p>
<dt><code>-d | &#8211;domain=</code> <i>DOMAIN</i></p>
<dd> Publish the service in the specified domain. If omitted the Avahi daemon will publish it in its default domain (usually .local).</p>
<dt><code>&#8211;subtype=</code> <i>SUBTYPE</i></p>
<dd> Register the service with an additional subtype in addition to the main type. DNS-SD subtypes have the form _anon._sub._<a href="ftp://ftp._tcp">ftp._tcp</a>, where _anon is the identifier of the subtype and _<a href="ftp://ftp._tcp">ftp._tcp</a> is the main type. You may pass this option multiple times to register the service with multiple subtypes.</p>
<dt><code>-f | &#8211;no-fail</code></p>
<dd> Don&#8217;t fail if the daemon is not found running. Instead, wait until it appears. If it disconnects, try to reconnect.</p>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help</p>
<dt><code>-V | &#8211;version</code></p>
<dd> Show version information.</dl>
<h2>AUTHORS</h2>
<p> The Avahi Developers &lt;avahi (at) lists (dot) freedesktop (dot) org&gt;; Avahi is available from <code><a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avahi-resolve/">avahi-resolve</a>(1)</code>, <code><a href="/docs/linux/man/1-avahi-browse/">avahi-browse</a>(1)</code>, <code><a href="/docs/linux/man/8-avahi-daemon/">avahi-daemon</a>(8)</code></p>
<h2>COMMENTS</h2>
<p> This man page was written using <code><a href="/docs/linux/man/1-xml2man/">xml2man</a>(1)</code> by Oliver Kurth. </p>
<h2>Index</h2>
