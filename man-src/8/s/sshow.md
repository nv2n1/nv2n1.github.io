---
title: "sshow(8)"
name: "sshow"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sshow/"
description: "sshow – SSH traffic analysis tool"
---

<p>sshow &#8211; SSH traffic analysis tool</p>
<h2>Synopsis</h2>
<p><code>sshow</code> [<code>-d</code>] [<code>-i </code><i>interface</i> | <code>-p </code><i>pcapfile</i>] [<i>expression</i>]</p>
<h2>Description</h2>
<p><code>sshow</code> analyzes encrypted SSH-1 and SSH-2 traffic, identifying authentication attempts, the lengths of passwords entered in interactive sessions, and command line lengths. </p>
<p> The following advisory describes the attacks implemented by <code>sshow</code> in detail: </p>
<dl>
<dd><i><a rel="nofollow" href="http://www.openwall.com/advisories/OW-003-ssh-traffic-analysis.txt">http://www.openwall.com/advisories/OW-003-ssh-traffic-analysis.txt</a></i></dl>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Enable verbose debugging output.</p>
<dt><code>-i </code><i>interface</i></p>
<dd>Specify the interface to listen on.</p>
<dt><code>-p </code><i>pcapfile</i></p>
<dd>Process packets from the specified PCAP capture file instead of the network.</p>
<dt><i>expression</i></p>
<dd>Specify a <a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8) filter expression to select traffic to sniff.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dsniff/">dsniff</a>(8), <a href="/docs/linux/man/8-sshmitm/">sshmitm</a>(8)</p>
<h2>Authors</h2>
<pre>Solar Designer &lt;solar [at] openwall.com&gt;
Dug Song &lt;dugsong [at] monkey.org&gt;</pre>
