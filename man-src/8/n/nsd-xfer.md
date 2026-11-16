---
title: "nsd-xfer(8)"
name: "nsd-xfer"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsd-xfer/"
description: "nsd-xfer – AXFR client to transfer zones from a name server"
---

<p><code>nsd-xfer</code> &#8211; AXFR client to transfer zones from a name server</p>
<h2>Synopsis</h2>
<p><code>nsd-xfer</code> [<code>-4</code>] [<code>-6</code>] [<code>-a</code> <i>address[@port]</i>] [<code>-p</code> <i>port</i>] [<code>-s</code> <i>serial</i>] [<code>-T</code> <i>tsiginfo</i>] [<code>-v</code>] <code>-z</code> <i>zone</i> <code>-f</code> <i>file</i> <i>servers</i></p>
<h2>Description</h2>
<p><code>Nsd-xfer </code> is program to transfer zones from a name server using AXFR. <code>NSD </code> is a complete implementation of an authoritative DNS nameserver.</p>
<h2>Options</h2>
<dl>
<dt><code>-4</code></dt>
<dd>Only send to IPv4 addresses.</dd>
<dt><code>-6</code></dt>
<dd>Only send to IPv6 addresses.</dd>
<dt><code>-a</code><i> address[@port]</i></dt>
<dd>Specify the source address (and port) to send from.</dd>
<dt><code>-f</code><i> file</i></dt>
<dd>The file to store the zone in.</dd>
<dt><code>-p</code><i> port</i></dt>
<dd>Specify the port to send to.</dd>
<dt><code>-s</code><i> serial</i></dt>
<dd>Specify the serial of the current zone. The zone is only transferred if the master server has a zone with a greater serial number.</dd>
<dt><code>-T</code><i> tsiginfo</i></dt>
<dd>Use TSIG to verify the zone transfer. The <i>tsiginfo</i> file must contain the TSIG key information. The file is removed upon successful reading of the key.</dd>
<dt><code>-v</code></dt>
<dd>Be more verbose.</dd>
<dt><code>-z</code><i> zone</i></dt>
<dd>Specify the zone to receive.</dd>
<dt><i>servers</i></dt>
<dd>List of nameservers to try.</dd></dl>
<h2>Examples</h2>
<p>To run this program the standard way type: </p>
<p> # nsd-xfer -z foobar.cz -f foobar.cz.zone 1.2.3.4</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-nsd/">nsd</a>(8), <a href="/docs/linux/man/8-nsdc/">nsdc</a>(8), <a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a>(5), <a href="/docs/linux/man/8-nsd-checkconf/">nsd-checkconf</a>(8), <a href="/docs/linux/man/8-nsd-notify/">nsd-notify</a>(8), <a href="/docs/linux/man/8-nsd-patch/">nsd-patch</a>(8), <a href="/docs/linux/man/8-zonec/">zonec</a>(8)</p>
<h2>Authors</h2>
<p><code>NSD</code> was written by NLnet Labs and RIPE NCC joint team. Please see CREDITS file in the distribution for further details.</p>
