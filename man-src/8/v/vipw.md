---
title: "vipw(8)"
name: "vipw"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vipw/"
description: "vipw, vigr – edit the password, group, shadow-password or shadow-group file"
---

<p>vipw, vigr &#8211; edit the password, group, shadow-password or shadow-group file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>vipw</code> [<i>options</i>]</p>
<dt> <code>vigr</code> [<i>options</i>]</dl>
<h2>Description</h2>
<dd>The <code>vipw</code> and <code>vigr</code> commands edits the files /etc/passwd and /etc/group, respectively. With the <code>-s</code> flag, they will edit the shadow versions of those files, /etc/shadow and /etc/gshadow, respectively. The programs will set the appropriate locks to prevent file corruption. When looking for an editor, the programs will first try the environment variable <code>$VISUAL</code>, then the environment variable <code>$EDITOR</code>, and finally the default editor, <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1).</p>
<h2>Options</h2>
<p>The options which apply to the <code>vipw</code> and <code>vigr</code> commands are: </p>
<p> <code>-g</code>, <code>&#8211;group</code></p>
<dl>
<dd>Edit group database.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-p</code>, <code>&#8211;passwd</code></p>
<dl>
<dd>Edit passwd database.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dd>Quiet mode.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-s</code>, <code>&#8211;shadow</code></p>
<dl>
<dd>Edit shadow or gshadow database.</dl>
<h2>Environment</h2>
<p><code>VISUAL</code></p>
<dl>
<dd>Editor to be used.</dl>
<p> <code>EDITOR</code></p>
<dl>
<dd>Editor to be used if <code>VISUAL</code> is not set.</dl>
<h2>Files</h2>
<p>/etc/group</p>
<dl>
<dd>Group account information.</dl>
<p> /etc/gshadow</p>
<dl>
<dd>Secure group account information.</dl>
<p> /etc/passwd</p>
<dl>
<dd>User account information.</dl>
<p> /etc/shadow</p>
<dl>
<dd>Secure user account information.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-vi/">vi</a></code>(1), <code><a href="/docs/linux/man/5-group/">group</a></code>(5), <code><a href="/docs/linux/man/5-gshadow/">gshadow</a></code>(5) , <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), , <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5). </p>
