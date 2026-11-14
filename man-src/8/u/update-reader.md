---
title: "update-reader(8)"
name: "update-reader"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-reader/"
description: "update-reader.conf – (re)generate /etc/reader.conf"
---

<p>update-reader.conf &#8211; (re)generate /etc/reader.conf</p>
<h2>Synopsis</h2>
<p><code>update-reader.conf</code> [force]</p>
<h2>Description</h2>
<p><code>update-reader.conf</code> is a simple tool to manage <i>/etc/reader.conf</i>. The PCSC daemon (pcscd) uses one configuration file for its configuration. This makes it hard for packages to dynamically add information about their own smart card reader drivers. To fix this <code>update-reader.conf</code> has been introduced. </p>
<p> <code>update-reader.conf</code> attempts to fix this by generating the configuration file from seperate files which are located in <i>/etc/reader.conf.d/</i>. All files in that directory are assembled together to form <i>/etc/reader.conf</i>.</p>
<h2>Files</h2>
<p><code>update-reader.conf</code> will only use files that match the following wildcard: <code>*.conf</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcscd/">pcscd</a></code>(1),<code><a href="/docs/linux/man/5-reader-conf/">reader.conf</a></code>(5)</p>
<h2>Author</h2>
<p>This manual page was written by Ludovic Rousseau &lt;ludovic.rousseau [at] free.fr&gt;.</p>
