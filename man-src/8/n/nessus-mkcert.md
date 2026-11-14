---
title: "nessus-mkcert(8)"
name: "nessus-mkcert"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nessus-mkcert/"
description: "nessus-mkcert – Creates a server certificate"
---

<p>nessus-mkcert &#8211; Creates a server certificate </p>
<h2>Synopsis</h2>
<p><code>nessus-mkcert</code> [ -q ] </p>
<h2>Description</h2>
<p>The <code>Nessus Security Scanner</code> protects the communication between the client and the server by using SSL. SSL requires the server to present a certificate to the client, and the client can optionally present a certificate to the server. This script <code>nessus-mkcert</code> creates a certificate authority (if none exists already) and generates the server certificate. </p>
<h2>Options</h2>
<p><i>-q</i> quickly generates a new certificate, without asking any question</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nessusd/">nessusd</a></code>(8),&nbsp;<wbr><code><a href="/docs/linux/man/1-nessus-mkcert-client/">nessus-mkcert-client</a></code>(1),&nbsp;<wbr><code><a href="/docs/linux/man/1-openssl/">openssl</a>(1)</code> </p>
<h2>More Information About The Nessus Project</h2>
<p>The canonical places where you will find more information about the Nessus project are:</p>
<dl>
<dd><a rel="nofollow" href="http://www.nessus.org/">http://www.nessus.org/</a> (Official site)<br />
 <a rel="nofollow" href="http://cvs.nessus.org/">http://cvs.nessus.org/</a> (Developers site)</dl>
<h2>Author</h2>
<p><code>nessus-mkcert</code> was written by Michel Arboi &lt;arboi [at] alussinan.org&gt; and Renaud Deraison &lt;deraison [at] cvs.nessus.org&gt;</p>
