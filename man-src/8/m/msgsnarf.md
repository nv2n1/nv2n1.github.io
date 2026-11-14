---
title: "msgsnarf(8)"
name: "msgsnarf"
section: "8"
letter: "m"
url: "/docs/linux/man/8-msgsnarf/"
description: "msgsnarf – sniff chat messages"
---

<p>msgsnarf &#8211; sniff chat messages</p>
<h2>Synopsis</h2>
<p><code>msgsnarf</code> [<code>-i </code><i>interface</i> | <code>-p </code><i>pcapfile</i>] [[<code>-v</code>] <i>pattern [expression</i>]]</p>
<h2>Description</h2>
<p><code>msgsnarf</code> records selected messages from AOL Instant Messenger, ICQ 2000, IRC, MSN Messenger, or Yahoo Messenger chat sessions.</p>
<h2>Options</h2>
<dl>
<dt><code>-i </code><i>interface</i></p>
<dd>Specify the interface to listen on.</p>
<dt><code>-p </code><i>pcapfile</i></p>
<dd>Process packets from the specified PCAP capture file instead of the network.</p>
<dt><code>-v</code></p>
<dd>&quot;Versus&quot; mode. Invert the sense of matching, to select non-matching messages.</p>
<dt><i>pattern</i></p>
<dd>Specify regular expression for message matching.</p>
<dt><i>expression</i></p>
<dd>Specify a <a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8) filter expression to select traffic to sniff.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dsniff/">dsniff</a>(8)</p>
<h2>Author</h2>
<pre>Dug Song &lt;dugsong [at] monkey.org&gt;</pre>
