---
title: "make-ssl-cert(8)"
name: "make-ssl-cert"
section: "8"
letter: "m"
url: "/docs/linux/man/8-make-ssl-cert/"
description: "make-ssl-cert – Debconf wrapper for openssl"
---

<p>make-ssl-cert &#8211; Debconf wrapper for openssl</p>
<h2>Synopsis</h2>
<p><code>make-ssl-cert</code> [<i>,OPTION/</i>]&#8230; <i>template</i> <i>output-certificate</i><br />
 <code>make-ssl-cert [</code><i>,OPTION/</i>]&#8230; generate-default-snakeoil</p>
<h2>Description</h2>
<p>make-ssl-cert is a simple debconf to openssl wrapper to create self-signed certificates. It requires a source template (Ex: /usr/share/ssl-cert/ssleay.cnf) and it will place the new generated certificate in the specified output file.<br />
 Invoked with &quot;generate-default-snakeoil&quot;, it will generate /etc/ssl/certs/ssl-cert-snakeoil.pem and /etc/ssl/private/ssl-cert-snakeoil.key.</p>
<h2>Options</h2>
<p>A summary of options are included below.</p>
<dl>
<dt><code>&#8211;force-overwrite</code></p>
<dd>Always create a new certificate, even if the file already exists. For backwards compatibility with 1.0.x, this option can be given as last argument, too.</p>
<dt><code>&#8211;no-overwrite</code></p>
<dd>Never overwrite an existing file, even if the old certificate&#8217;s key length is too small or if it uses an obsoltete signature algorithm.</p>
<dt><code>&#8211;expiration-days </code><i>N</i></p>
<dd>Make the new certificate expire in <i>N</i> days. Default is 3650.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-openssl/">openssl</a></i>(1)</p>
<h2>Author</h2>
<p>The program author is Thom May &lt;thom [at] debian.org&gt;, manual page was written for completeness by Fabio M. Di Nitto &lt;fabbione [at] fabbione.net&gt;, for the Debian GNU/Linux system (but may be used by others).</p>
