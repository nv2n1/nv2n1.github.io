---
title: "sybilsim(8)"
name: "sybilsim"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sybilsim/"
description: "sybilsim — Cjdns packet switch"
---

<p><code>sybilsim</code> &#8212; Cjdns packet switch</p>
<h2>Synopsis</h2>
<p><code>/usr/libexec/cjdns/sybilsim &lt; config.json</code></p>
<h2>Description</h2>
<p>Sybilsim reads a list of nodes and peers from stdin and simulates the corresponding mesh without any actual networking using the same code as cjdroute. This is useful for testing and optimizing cjdroute. Every node must have a valid cjdns private key. The <a href="/docs/linux/man/1-makekeys/">makekeys</a>(1) utility can be useful for scripts that generate the config.</p>
<h2>Usage</h2>
<p>Example config:</p>
<dl>
<dd>
<pre>{
 &quot;nodes&quot;: {
&quot;alice&quot;: {
 &quot;privateKey&quot;:
 &quot;5e2295679394e5e1db67c238abbc10292ad9b127904394c52cc5fff39383e920&quot;,
 &quot;peers&quot;: []
},
&quot;bob&quot;: {
 &quot;privateKey&quot;:
 &quot;6569bf3f0d168faa6dfb2912f8ee5ee9b938319e97618fdf06caed73b1aad1cc&quot;,
 &quot;peers&quot;: [ &quot;alice&quot; ]
}
 }
}</pre>
<dd></dl>
<p> Example use:</p>
<dl>
<dd>
<pre>makekeys | head -20 &gt;keys.txt
node /usr/libexec/cjdns/tools/lib/makesim.js keys.txt |
/usr/libexec/cjdns/sybilsim</pre>
<dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-makekeys/">makekeys</a>(1), <a href="/docs/linux/man/1-cjdroute/">cjdroute</a>(1) <a href="/docs/linux/man/8-sybilsim/">sybilsim</a>(8) &#8212; Cjdns packet switch =============================================</p>
<h2>Synopsis</h2>
<p><code>/usr/libexec/cjdns/sybilsim &lt; config.json</code></p>
<h2>Description</h2>
<p>Sybilsim reads a list of nodes and peers from stdin and simulates the corresponding mesh without any actual networking using the same code as cjdroute. This is useful for testing and optimizing cjdroute. Every node must have a valid cjdns private key. The <a href="/docs/linux/man/1-makekeys/">makekeys</a>(1) utility can be useful for scripts that generate the config.</p>
<h2>Usage</h2>
<p>Example config:</p>
<dl>
<dd>
<pre>{
 &quot;nodes&quot;: {
&quot;alice&quot;: {
 &quot;privateKey&quot;:
 &quot;5e2295679394e5e1db67c238abbc10292ad9b127904394c52cc5fff39383e920&quot;,
 &quot;peers&quot;: []
},
&quot;bob&quot;: {
 &quot;privateKey&quot;:
 &quot;6569bf3f0d168faa6dfb2912f8ee5ee9b938319e97618fdf06caed73b1aad1cc&quot;,
 &quot;peers&quot;: [ &quot;alice&quot; ]
}
 }
}</pre>
<dd></dl>
<p> Example use:</p>
<dl>
<dd>
<pre>makekeys | head -20 &gt;keys.txt
node /usr/libexec/cjdns/tools/lib/makesim.js keys.txt |
/usr/libexec/cjdns/sybilsim</pre>
<dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-makekeys/">makekeys</a>(1), <a href="/docs/linux/man/1-cjdroute/">cjdroute</a>(1) </p>
