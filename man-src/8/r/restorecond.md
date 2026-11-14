---
title: "restorecond(8)"
name: "restorecond"
section: "8"
letter: "r"
url: "/docs/linux/man/8-restorecond/"
description: "restorecond – daemon that watches for file creation and then sets the default SELinux file context"
---

<p>restorecond &#8211; daemon that watches for file creation and then sets the default SELinux file context </p>
<h2>Synopsis</h2>
<p><code>restorecond [-d] [-h] [-f restorecond_file ] [-u] [-v]</code> </p>
<h2>Description</h2>
<p>This manual page describes the <code>restorecond</code> program. This daemon uses inotify to watch files listed in the /etc/selinux/restorecond.conf, when they are created, this daemon will make sure they have the correct file context associated with the policy. </p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Turns on debugging mode. Application will stay in the foreground and lots of debugs messages start printing.</p>
<dt><code>-h</code></p>
<dd>Print usage statement.</p>
<dt><code>-f restorecond_file</code></p>
<dd>Use alternative restorecond.conf file.</p>
<dt><code>-u</code></p>
<dd>Turns on user mode. Runs restorecond in the user session and reads /etc/selinux/restorecond_user.conf. Uses dbus to make sure only one restorecond is running per user session.</p>
<dt><code>-v</code></p>
<dd>Turns on verbose debugging. (Report missing files) </p>
</dl>
<h2>Author</h2>
<p>This man page and program was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.</p>
<h2>Files</h2>
<p>/etc/selinux/restorecond.conf /etc/selinux/restorecond_user.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-restorecon/">restorecon</a></code>(8), </p>
