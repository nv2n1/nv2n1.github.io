---
title: "webspy(8)"
name: "webspy"
section: "8"
letter: "w"
url: "/docs/linux/man/8-webspy/"
description: "webspy – display sniffed URLs in Netscape in real-time"
---

<p>webspy &#8211; display sniffed URLs in Netscape in real-time</p>
<h2>Synopsis</h2>
<p><code>webspy</code> [<code>-i </code><i>interface</i> | <code>-p </code><i>pcapfile</i>] <i>host</i></p>
<h2>Description</h2>
<p><code>webspy</code> sends URLs sniffed from a client to your local Netscape browser for display, updated in real-time (as the target surfs, your browser surfs along with them, automagically). Netscape must be running on your local X display ahead of time.</p>
<h2>Options</h2>
<dl>
<dt><code>-i </code><i>interface</i></p>
<dd>Specify the interface to listen on.</p>
<dt><code>-p </code><i>pcapfile</i></p>
<dd>Process packets from the specified PCAP capture file instead of the network.</p>
<dt><i>host</i></p>
<dd>Specify the web client to spy on.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dsniff/">dsniff</a>(8)</p>
<h2>Author</h2>
<pre>Dug Song &lt;dugsong [at] monkey.org&gt;</pre>
