---
title: "webmitm(8)"
name: "webmitm"
section: "8"
letter: "w"
url: "/docs/linux/man/8-webmitm/"
description: "webmitm – HTTP / HTTPS monkey-in-the-middle"
---

<p>webmitm &#8211; HTTP / HTTPS monkey-in-the-middle</p>
<h2>Synopsis</h2>
<p><code>webmitm</code> [<code>-d</code>] [<code>host</code>]</p>
<h2>Description</h2>
<p><code>webmitm</code> transparently proxies and sniffs HTTP / HTTPS traffic redirected by <a href="/docs/linux/man/8-dnsspoof/">dnsspoof</a>(8), capturing most &quot;secure&quot; SSL-encrypted webmail logins and form submissions.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Enable debugging mode. May be specified multiple times to greater effect.</p>
<dt><code>host</code></p>
<dd>Specify a host to proxy to. If none given, only requests containing an HTTP/1.1 Host: header or absolute URI will be relayed transparently.</dl>
<h2>Files</h2>
<dl>
<dt><i>webmitm.crt</i></p>
<dd>SSL certificate</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dsniff/">dsniff</a>(8), <a href="/docs/linux/man/8-dnsspoof/">dnsspoof</a>(8)</p>
<h2>Author</h2>
<pre>Dug Song &lt;dugsong [at] monkey.org&gt;</pre>
