---
title: "mailsnarf(8)"
name: "mailsnarf"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mailsnarf/"
description: "mailsnarf – sniff mail messages in Berkeley mbox format"
---

<p>mailsnarf &#8211; sniff mail messages in Berkeley mbox format</p>
<h2>Synopsis</h2>
<p><code>mailsnarf</code> [<code>-i </code><i>interface</i> | <code>-p </code><i>pcapfile</i>] [[<code>-v</code>] <i>pattern [expression</i>]]</p>
<h2>Description</h2>
<p><code>mailsnarf</code> outputs e-mail messages sniffed from SMTP and POP traffic in Berkeley mbox format, suitable for offline browsing with your favorite mail reader (<a href="/docs/linux/man/1-mail/">mail</a>(1), pine(1), etc.).</p>
<h2>Options</h2>
<dl>
<dt><code>-i </code><i>interface</i></dt>
<dd>Specify the interface to listen on.</dd>
<dt><code>-p </code><i>pcapfile</i></dt>
<dd>Process packets from the specified PCAP capture file instead of the network.</dd>
<dt><code>-v</code></dt>
<dd>&quot;Versus&quot; mode. Invert the sense of matching, to select non-matching messages.</dd>
<dt><i>pattern</i></dt>
<dd>Specify regular expression for message header/body matching.</dd>
<dt><i>expression</i></dt>
<dd>Specify a <a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8) filter expression to select traffic to sniff.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dsniff/">dsniff</a>(8), <a href="/docs/linux/man/1-mail/">mail</a>(1), pine(1)</p>
<h2>Author</h2>
<pre>Dug Song &lt;dugsong [at] monkey.org&gt;</pre>
