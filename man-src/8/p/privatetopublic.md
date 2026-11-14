---
title: "privatetopublic(8)"
name: "privatetopublic"
section: "8"
letter: "p"
url: "/docs/linux/man/8-privatetopublic/"
description: "privatetopublic — convert cjdns private keys to public keys and IP6"
---

<p><code>privatetopublic</code> &#8212; convert cjdns private keys to public keys and IP6</p>
<h2>Synopsis</h2>
<p><code>/usr/libexec/cjdns/privatetopublic</code></p>
<h2>Description</h2>
<p>As private keys are very sensitive, /usr/libexec/cjdns/privatetopublic reads them from stdin. If your shell, terminal, or other program keeps history, please avoid <code>echo &#8216;key&#8217; | /usr/libexec/cjdns/privatetopublic</code>, or similar constructs. A heredoc is suitable for use in scripts, and will avoid unwanted revealing of the key in process lists, like so:</p>
<dl>
<dd>
<pre>/usr/libexec/cjdns/privatetopublic &lt;&lt;EOF
key
EOF</pre>
<dd></dl>
<p> Key should be in hex form, maximum 64 characters. Extra characters will be silently ignored.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-publictoip6/">publictoip6</a>(1) <a href="/docs/linux/man/8-privatetopublic/">privatetopublic</a>(8) &#8212; convert cjdns private keys to public keys and IP6 =============================================</p>
<h2>Synopsis</h2>
<p><code>/usr/libexec/cjdns/privatetopublic</code></p>
<h2>Description</h2>
<p>As private keys are very sensitive, /usr/libexec/cjdns/privatetopublic reads them from stdin. If your shell, terminal, or other program keeps history, please avoid <code>echo &#8216;key&#8217; | /usr/libexec/cjdns/privatetopublic</code>, or similar constructs. A heredoc is suitable for use in scripts, and will avoid unwanted revealing of the key in process lists, like so:</p>
<dl>
<dd>
<pre>/usr/libexec/cjdns/privatetopublic &lt;&lt;EOF
key
EOF</pre>
<dd></dl>
<p> Key should be in hex form, maximum 64 characters. Extra characters will be silently ignored.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-publictoip6/">publictoip6</a>(1) </p>
