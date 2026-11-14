---
title: "nsd-notify(8)"
name: "nsd-notify"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsd-notify/"
description: "nsd-notify – program to send NOTIFY’s to remote nameservers."
---

<p><code>nsd-notify </code> &#8211; program to send NOTIFY&#8217;s to remote nameservers.</p>
<h2>Synopsis</h2>
<p><code>nsd-notify</code> [<code>-4</code>] [<code>-6</code>] [<code>-h</code>] [<code>-a</code> <i>address[@port]</i>] [<code>-p</code> <i>port</i>] [<code>-y</code> <i>key:secret[:algorithm]</i>] <code>-z</code> <i>zone servers</i></p>
<h2>Description</h2>
<p><code>Nsd-notify </code> is simple program to send NOTIFY&#8217;s to remoter nameservers. <code>NSD </code> is a complete implementation of an authoritative DNS nameserver.</p>
<h2>Options</h2>
<dl>
<dt><code>-4</code></p>
<dd>Only send to IPv4 addresses.</p>
<dt><code>-6</code></p>
<dd>Only send to IPv6 addresses.</p>
<dt><code>-h</code></p>
<dd>Print help information and exit.</p>
<dt><code>-a</code><i> address[@port]</i></p>
<dd>Specify the source address (and port) to send from.</p>
<dt><code>-p</code><i> port</i></p>
<dd>Specify the port to send to.</p>
<dt><code>-y</code><i> key:secret[:algorithm]</i></p>
<dd>Specify a TSIG key and base64 encoded secret to sign the notification with. If the TSIG algorithm is not defined, MD5 is used.</p>
<dt><code>z</code><i> zone</i></p>
<dd>Specify the zone to notify about.</p>
<dt><i>servers</i></p>
<dd>List of nameservers to send to.</dl>
<h2>Examples</h2>
<p>To run this program the standard way type: </p>
<p> <code># nsd-notify -z foobar.cz 1.2.3.4</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-nsd/">nsd</a>(8), <a href="/docs/linux/man/8-nsdc/">nsdc</a>(8), <a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a>(5), <a href="/docs/linux/man/8-nsd-checkconf/">nsd-checkconf</a>(8), <a href="/docs/linux/man/8-nsd-patch/">nsd-patch</a>(8), <a href="/docs/linux/man/8-nsd-xfer/">nsd-xfer</a>(8), <a href="/docs/linux/man/8-zonec/">zonec</a>(8)</p>
<h2>Authors</h2>
<p><code>NSD</code> was written by NLnet Labs and RIPE NCC joint team. Please see CREDITS file in the distribution for further details.</p>
