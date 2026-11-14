---
title: "arpspoof(8)"
name: "arpspoof"
section: "8"
letter: "a"
url: "/docs/linux/man/8-arpspoof/"
description: "arpspoof – intercept packets on a switched LAN"
---

<p>arpspoof &#8211; intercept packets on a switched LAN</p>
<h2>Synopsis</h2>
<p><code>arpspoof</code> [<code>-i </code><i>interface</i>] [<code>-c </code><i>own|host|both</i>] [<code>-t </code><i>target</i>] [<code>-r</code>] <i>host</i></p>
<h2>Description</h2>
<p><code>arpspoof</code> redirects packets from a target host (or all hosts) on the LAN intended for another host on the LAN by forging ARP replies. This is an extremely effective way of sniffing traffic on a switch. </p>
<p> Kernel IP forwarding (or a userland program which accomplishes the same, e.g. <a href="/docs/linux/man/8-fragrouter/">fragrouter</a>(8)) must be turned on ahead of time.</p>
<h2>Options</h2>
<dl>
<dt><code>-i </code><i>interface</i></p>
<dd>Specify the interface to use.</p>
<dt><code>-c </code><i>own|host|both</i></p>
<dd>Specify which hardware address t use when restoring the arp configuration; while cleaning up, packets can be send with the own address as well as with the address of the host. Sending packets with a fake hw address can disrupt connectivity with certain switch/ap/bridge configurations, however it works more reliably than using the own address, which is the default way arpspoof cleans up afterwards.</p>
<dt><code>-t </code><i>target</i></p>
<dd>Specify a particular host to ARP poison (if not specified, all hosts on the LAN). Repeat to specify multiple hosts.</p>
<dt><code>-r</code></p>
<dd>Poison both hosts (host and target) to capture traffic in both directions. (only valid in conjuntion with -t)</p>
<dt><i>host</i></p>
<dd>Specify the host you wish to intercept packets for (usually the local gateway).</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dsniff/">dsniff</a>(8), <a href="/docs/linux/man/8-fragrouter/">fragrouter</a>(8)</p>
<h2>Author</h2>
<pre>Dug Song &lt;dugsong [at] monkey.org&gt;</pre>
