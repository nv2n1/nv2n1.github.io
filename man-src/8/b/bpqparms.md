---
title: "bpqparms(8)"
name: "bpqparms"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bpqparms/"
description: "bpqparms – Configure BPQ ethernet devices."
---

<p>bpqparms &#8211; Configure BPQ ethernet devices.</p>
<h2>Synopsis</h2>
<p><code>bpqparms device [-a ethaddr] [-d ethaddr] [-vV]</code></p>
<h2>Description</h2>
<p><code>Bpqparms</code> allows the setting of the BPQ Ethernet options for a particular device. Each BPQ Ethernet device appears as a device named bpq0&#8230;bpqN which overlays the original Ethernet device, usually eth0&#8230;ethN. This device is an AX.25 device driver and allows AX.25 frames to be transmitted over an Ethernet to another machine using the same protocol. The default for the device is to send and receive BPQ Ethernet packets to the broadcast address. This program replaces the previous lqaxparms -devrq option.</p>
<h2>Options</h2>
<dl>
<dt><code>-a ethaddr</code></p>
<dd>Allows the setting of which ethernet address will be accepted by the BPQ Ethernet device.</p>
<dt><code>-d ethaddr</code></p>
<dd>If specified on its own, will set the destination ethernet address will be used for transmitting and for receiving of BPQ ethernet packets. An address of lqbroadcastrq sets it to the ethernet broadcast address.</p>
<dt><code>-v</code></p>
<dd>Displays the version number.</p>
<dt><code>-V</code></p>
<dd>The original version messages.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4), <code><a href="/docs/linux/man/5-axports/">axports</a></code>(5), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8).</p>
<h2>Author</h2>
<p>Joerg Reuter DL1BKE &lt;jreuter [at] poboxes.com&gt;</p>
