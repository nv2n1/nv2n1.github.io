---
title: "quotagrpadmins(5)"
name: "quotagrpadmins"
section: "5"
letter: "q"
url: "/docs/linux/man/5-quotagrpadmins/"
description: "quotagrpadmins – users responsible for group disk usage"
---

<p>quotagrpadmins &#8211; users responsible for group disk usage</p>
<h2>Synopsis</h2>
<p><code>/etc/quotagrpadmins</code></p>
<h2>Description</h2>
<p>The <code>quotagrpadmins</code> file lists administrators of user groups who will receive a warning if <code>warnquota &#8211;group</code> command finds a group exceeding its disk usage limits. </p>
<p> Each line consists of a group name followed by a colon and an user name. White space characters surrounding the names are allowed. Empty lines or lines starting with a hash sign or a semicolon are ignored.</p>
<h2>Example</h2>
<p># comment</p>
<dl>
<dd>users: root</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/quotagrpadmins</code></p>
<dd>list of group administrators</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-warnquota/">warnquota</a></code>(8). </p>
