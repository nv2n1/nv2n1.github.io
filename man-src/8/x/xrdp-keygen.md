---
title: "xrdp-keygen(8)"
name: "xrdp-keygen"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xrdp-keygen/"
description: "xrdp-keygen – xrdp RSA key generation utility"
---

<p>xrdp-keygen &#8211; xrdp RSA key generation utility </p>
<h2>Synopsis</h2>
<p><code>xrdp-keygen xrdp</code> &lt; <i>outfile</i> | <code>auto</code> &gt;<br />
 <code>xrdp-keygen test</code> </p>
<h2>Description</h2>
<p><code>xrdp-keygen</code> generates the file <i>/etc/xrdp/rsakeys.ini</i> which contains the RSA key pair used to perform authentication to remote clients. The public key is self-signed. </p>
<h2>Options</h2>
<p>This program takes one of the following options:</p>
<dl>
<dt><code>xrdp</code> <i>outfile</i></p>
<dd>Generate a new key pair. The key data is stored in the file named <i>outfile</i>.<br />
 If <code>auto</code> is used as <i>outfile</i>, the default file <i>/etc/xrdp/rsakeys.ini</i> gets created if it does not yet exists.</p>
<dt><code>test</code></p>
<dd>Generate a test key pair and print information to standard output. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/xrdp/rsakeys.ini</i></p>
<dd>RSA public and private key pair used to identify this XRDP server. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8), <code><a href="/docs/linux/man/8-xrdp-sesman/">xrdp-sesman</a></code>(8). </p>
<h2>Author</h2>
<p>This manual page was originally written by Vincent Bernat &lt;bernat [at] luffy.cx&gt;.</p>
