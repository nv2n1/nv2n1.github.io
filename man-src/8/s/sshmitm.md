---
title: "sshmitm(8)"
name: "sshmitm"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sshmitm/"
description: "sshmitm – SSH monkey-in-the-middle"
---

<p>sshmitm &#8211; SSH monkey-in-the-middle</p>
<h2>Synopsis</h2>
<p><code>sshmitm</code> [<code>-d</code>] [<code>-I</code>] [<code>-p </code><i>port</i>] host [<i>port</i>]</p>
<h2>Description</h2>
<p><code>sshmitm</code> proxies and sniffs SSH traffic redirected by <a href="/docs/linux/man/8-dnsspoof/">dnsspoof</a>(8), capturing SSH password logins, and optionally hijacking interactive sessions. Only SSH protocol version 1 is (or ever will be) supported &#8211; this program is far too evil already.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></dt>
<dd>Enable verbose debugging output.</dd>
<dt><code>-I</code></dt>
<dd>Monitor / hijack an interactive session.</dd>
<dt><code>-p </code><i>port</i></dt>
<dd>Specify the local port to listen on.</dd>
<dt><i>host</i></dt>
<dd>Specify the remote host to relay connections to.</dd>
<dt><i>port</i></dt>
<dd>Specify the remote port to relay connections to.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dsniff/">dsniff</a>(8), <a href="/docs/linux/man/8-dnsspoof/">dnsspoof</a>(8)</p>
<h2>Author</h2>
<pre>Dug Song &lt;dugsong [at] monkey.org&gt;</pre>
