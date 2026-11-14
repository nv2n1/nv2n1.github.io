---
title: "filesnarf(8)"
name: "filesnarf"
section: "8"
letter: "f"
url: "/docs/linux/man/8-filesnarf/"
description: "filesnarf – sniff files from NFS traffic"
---

<p>filesnarf &#8211; sniff files from NFS traffic</p>
<h2>Synopsis</h2>
<p><code>filesnarf</code> [<code>-i </code><i>interface</i> | <code>-p </code><i>pcapfile</i>] [[<code>-v</code>] <i>pattern [expression</i>]]</p>
<h2>Description</h2>
<p><code>filesnarf</code> saves files sniffed from NFS traffic in the current working directory.</p>
<h2>Options</h2>
<dl>
<dt><code>-i </code><i>interface</i></p>
<dd>Specify the interface to listen on.</p>
<dt><code>-p </code><i>pcapfile</i></p>
<dd>Process packets from the specified PCAP capture file instead of the network.</p>
<dt><code>-v</code></p>
<dd>&quot;Versus&quot; mode. Invert the sense of matching, to select non-matching files.</p>
<dt><i>pattern</i></p>
<dd>Specify regular expression for filename matching.</p>
<dt><i>expression</i></p>
<dd>Specify a <a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8) filter expression to select traffic to sniff.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dsniff/">dsniff</a>(8), <a href="/docs/linux/man/8-nfsd/">nfsd</a>(8)</p>
<h2>Author</h2>
<pre>Dug Song &lt;dugsong [at] monkey.org&gt;</pre>
