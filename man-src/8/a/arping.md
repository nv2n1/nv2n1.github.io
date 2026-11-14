---
title: "arping(8)"
name: "arping"
section: "8"
letter: "a"
url: "/docs/linux/man/8-arping/"
description: "arping – send ARP REQUEST to a neighbour host"
---

<p>arping &#8211; send ARP REQUEST to a neighbour host</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>arping</code> [<code>-AbDfhqUV</code>] [<code>-c&nbsp;</code><i>count</i>] [<code>-w&nbsp;</code><i>deadline</i>] [<code>-i&nbsp;</code><i>interval</i>] [<code>-s&nbsp;</code><i>source</i>] [<code>-I&nbsp;</code><i>interface</i>] {destination}</dl>
<h2>Description</h2>
<dd>Ping <i>destination</i> on device <i>interface</i> by ARP packets, using source address <i>source</i>.</p>
<h2>Options</h2>
<p><code>-A</code></p>
<dl>
<dd>The same as <code>-U</code>, but ARP REPLY packets used instead of ARP REQUEST.</dl>
<p> <code>-b</code></p>
<dl>
<dd>Send only MAC level broadcasts. Normally <code>arping</code> starts from sending broadcast, and switch to unicast after reply received.</dl>
<p> <code>-c </code><i>count</i></p>
<dl>
<dd>Stop after sending <i>count</i> ARP REQUEST packets. With <i>deadline</i> option, instead wait for <i>count</i> ARP REPLY packets, or until the timeout expires.</dl>
<p> <code>-D</code></p>
<dl>
<dd>Duplicate address detection mode (DAD). See RFC2131, 4.4.1. Returns 0, if DAD succeeded i.e. no replies are received.</dl>
<p> <code>-f</code></p>
<dl>
<dd>Finish after the first reply confirming that target is alive.</dl>
<p> <code>-I </code><i>interface</i></p>
<dl>
<dd>Name of network device where to send ARP REQUEST packets.</dl>
<p> <code>-h</code></p>
<dl>
<dd>Print help page and exit.</dl>
<p> <code>-q</code></p>
<dl>
<dd>Quiet output. Nothing is displayed.</dl>
<p> <code>-s </code><i>source</i></p>
<dl>
<dd>IP source address to use in ARP packets. If this option is absent, source address is: </p>
<dl>
<dd>&bull; In DAD mode (with option <code>-D</code>) set to 0.0.0.0.</dl>
<dl>
<dd>&bull; In Unsolicited ARP mode (with options <code>-U</code> or <code>-A</code>) set to <i>destination</i>.</dl>
<dl>
<dd>&bull; Otherwise, it is calculated from routing tables.</dl>
</dl>
<p> <code>-U</code></p>
<dl>
<dd>Unsolicited ARP mode to update neighbours&#8217; ARP caches. No replies are expected.</dl>
<p> <code>-V</code></p>
<dl>
<dd>Print version of the program and exit.</dl>
<p> <code>-w </code><i>deadline</i></p>
<dl>
<dd>Specify a timeout, in seconds, before <code>arping</code> exits regardless of how many packets have been sent or received. In this case <code>arping</code> does not stop after <i>count</i> packet are sent, it waits either for <i>deadline</i> expire or until <i>count</i> probes are answered.</dl>
<p> <code>-i </code><i>interval</i></p>
<dl>
<dd>Specify an interval, in seconds, between packets.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ping/">ping</a></code>(8), <code><a href="/docs/linux/man/8-clockdiff/">clockdiff</a></code>(8), <code><a href="/docs/linux/man/8-tracepath/">tracepath</a></code>(8).</p>
<h2>Author</h2>
<p><code>arping</code> was written by Alexey Kuznetsov &lt;kuznet [at] ms2.inr.ac.ru&gt;.</p>
<h2>Security</h2>
<p><code>arping</code> requires CAP_NET_RAW capability to be executed. It is not recommended to be used as set-uid root, because it allows user to modify ARP caches of neighbour hosts.</p>
<h2>Availability</h2>
<p><code>arping</code> is part of <i>iputils</i> package.</p>
