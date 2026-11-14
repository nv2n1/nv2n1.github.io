---
title: "macof(8)"
name: "macof"
section: "8"
letter: "m"
url: "/docs/linux/man/8-macof/"
description: "macof – flood a switched LAN with random MAC addresses"
---

<p>macof &#8211; flood a switched LAN with random MAC addresses</p>
<h2>Synopsis</h2>
<p><code>macof</code> [<code>-i </code><i>interface</i>] [<code>-s </code><i>src</i>] [<code>-d </code><i>dst</i>] [<code>-e </code><i>tha</i>] [<code>-x </code><i>sport</i>] [<code>-y </code><i>dport</i>] [<code>-n </code><i>times</i>]</p>
<h2>Description</h2>
<p><code>macof</code> floods the local network with random MAC addresses (causing some switches to fail open in repeating mode, facilitating sniffing). A straight C port of the original Perl Net::RawIP macof program by Ian Vitek &lt;ian.vitek [at] infosec.se&gt;.</p>
<h2>Options</h2>
<dl>
<dt><code>-i </code><i>interface</i></p>
<dd>Specify the interface to send on.</p>
<dt><code>-s </code><i>src</i></p>
<dd>Specify source IP address.</p>
<dt><code>-d </code><i>dst</i></p>
<dd>Specify destination IP address.</p>
<dt><code>-e </code><i>tha</i></p>
<dd>Specify target hardware address.</p>
<dt><code>-x </code><i>sport</i></p>
<dd>Specify TCP source port.</p>
<dt><code>-y </code><i>dport</i></p>
<dd>Specify TCP destination port.</p>
<dt><code>-n </code><i>times</i></p>
<dd>Specify the number of packets to send.</dl>
<p> Values for any options left unspecified will be generated randomly.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dsniff/">dsniff</a>(8)</p>
<h2>Author</h2>
<pre>Dug Song &lt;dugsong [at] monkey.org&gt;</pre>
