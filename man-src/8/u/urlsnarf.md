---
title: "urlsnarf(8)"
name: "urlsnarf"
section: "8"
letter: "u"
url: "/docs/linux/man/8-urlsnarf/"
description: "urlsnarf – sniff HTTP requests in Common Log Format"
---

<p>urlsnarf &#8211; sniff HTTP requests in Common Log Format</p>
<h2>Synopsis</h2>
<p><code>urlsnarf</code> [<code>-n</code>] [<code>-i </code><i>interface</i> | <code>-p </code><i>pcapfile</i>] [[<code>-v</code>] <i>pattern [expression</i>]]</p>
<h2>Description</h2>
<p><code>urlsnarf</code> outputs all requested URLs sniffed from HTTP traffic in CLF (Common Log Format, used by almost all web servers), suitable for offline post-processing with your favorite web log analysis tool (analog, wwwstat, etc.).</p>
<h2>Options</h2>
<dl>
<dt><code>-n</code></p>
<dd>Do not resolve IP addresses to hostnames.</p>
<dt><code>-i </code><i>interface</i></p>
<dd>Specify the interface to listen on.</p>
<dt><code>-p </code><i>pcapfile</i></p>
<dd>Process packets from the specified PCAP capture file instead of the network.</p>
<dt><code>-v</code></p>
<dd>&quot;Versus&quot; mode. Invert the sense of matching, to select non-matching URLs. Specify the interface to listen on.</p>
<dt><i>pattern</i></p>
<dd>Specify regular expression for URL matching.</p>
<dt><i>expression</i></p>
<dd>Specify a <a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8) filter expression to select traffic to sniff.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dsniff/">dsniff</a>(8)</p>
<h2>Author</h2>
<pre>Dug Song &lt;dugsong [at] monkey.org&gt;</pre>
