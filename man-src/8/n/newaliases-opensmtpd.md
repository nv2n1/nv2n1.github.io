---
title: "newaliases-opensmtpd(8)"
name: "newaliases-opensmtpd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-newaliases-opensmtpd/"
description: "newaliases – rebuild the database for the mail aliases file"
---

<p><code>newaliases</code> &#8211; rebuild the database for the mail aliases file</p>
<h2>Synopsis</h2>
<p><code>newaliases</code> [<code>-f</code> <i>file</i>]</p>
<h2>Description</h2>
<p><code>newaliases</code> rebuilds the random access database for the mail aliases file, the location of which is defined in <code><a href="/docs/linux/man/5-smtpd-conf/">smtpd.conf</a></code>(5), and which by default is <i>/etc/opensmtpd/aliases</i>. If using database (db) files this utility must be run every time the <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) file is changed. </p>
<p> The options are as follows:</p>
<dl>
<dd>
<dl>
<dt><code>-f</code> <i>file</i></p>
<dd>Use <i>file</i> as the configuration file, instead of the default <i>/etc/opensmtpd/smtpd.conf</i>.</dl>
</dl>
<p> Note: this utility is provided for sendmail compatibility. The preferred way of rebuilding the database is with <code><a href="/docs/linux/man/8-makemap/">makemap</a></code>(8):</p>
<dl>
<dd>
<pre># makemap -t aliases /etc/opensmtpd/aliases
</dl></pre>
<h2>Files</h2>
<dl>
<dd>
<dl>
<dt><code>/etc/opensmtpd/aliases</code></p>
<dd>List of local user mail aliases.</p>
<dt><code>/etc/opensmtpd/virtual</code></p>
<dd>List of virtual host aliases.</dl>
</dl>
<h2>Exit Status</h2>
<p>The <code>newaliases</code> utility exits 0 on success, and &gt;0 if an error occurs. newaliases</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-smtpd-conf/">smtpd.conf</a></code>(5), <code><a href="/docs/linux/man/8-makemap/">makemap</a></code>(8)</p>
<h2>History</h2>
<p>The <code>newaliases</code> command first appeared in OpenBSD 4.6 as a replacement for the equivalent command shipped with sendmail.</p>
