---
title: "ceph-post-file(8)"
name: "ceph-post-file"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ceph-post-file/"
description: "ceph-post-file – post files for ceph developers"
---

<p>ceph-post-file &#8211; post files for ceph developers</p>
<h2>Synopsis</h2>
<pre><code>ceph-post-file</code> [-d <i>description] [-u *user</i>] <i>file or dir</i> ...</pre>
<h2>Description</h2>
<p><code>ceph-post-file</code> will upload files or directories to ceph.com for later analysis by Ceph developers. </p>
<p> Each invocation uploads files or directories to a separate directory with a unique tag. That tag can be passed to a developer or referenced in a bug report (<i><a rel="nofollow" href="http://tracker.ceph.com/">http://tracker.ceph.com/</a></i>). Once the upload completes, the directory is marked non-readable and non-writeable to prevent access or modification by other users.</p>
<h2>Warning</h2>
<p>Basic measures are taken to make posted data be visible only to developers with access to ceph.com infrastructure. However, users should think twice and/or take appropriate precautions before posting potentially sensitive data (for example, logs or data directories that contain Ceph secrets).</p>
<h2>Options</h2>
<dl>
<dt><code>-d *description*, &#8211;description *description*</code></p>
<dd>Add a short description for the upload. This is a good opportunity to reference a bug number. There is no default value.</p>
<dt><code>-u *user*</code></p>
<dd>Set the user metadata for the upload. This defaults to <i>whoami`@`hostname -f</i>.</dl>
<h2>Examples</h2>
<p>To upload a single log: </p>
<pre>ceph-post-file /var/log/ceph/ceph-mon.`hostname`.log</pre>
<p>To upload several directories: </p>
<pre>ceph-post-file -d 'mon data directories' /var/log/ceph/mon/*</pre>
<h2>Availability</h2>
<p><code>ceph-post-file</code> is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to the Ceph documentation at <i><a rel="nofollow" href="http://ceph.com/docs">http://ceph.com/docs</a></i> for more information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ceph/">ceph</a></code>(8), <code><a href="/docs/linux/man/8-ceph-debugpack/">ceph-debugpack</a></code>(8),</p>
<h2>Copyright</h2>
<p>2010-2014, Inktank Storage, Inc. and contributors. Licensed under Creative Commons BY-SA</p>
