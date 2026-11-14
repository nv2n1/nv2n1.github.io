---
title: "seunshare(8)"
name: "seunshare"
section: "8"
letter: "s"
url: "/docs/linux/man/8-seunshare/"
description: "seunshare – Run cmd with alternate homedir, tmpdir and/or SELinux context"
---

<p>seunshare &#8211; Run cmd with alternate homedir, tmpdir and/or SELinux context</p>
<h2>Synopsis</h2>
<p><code>seunshare</code> [ -v ] [ -C ] [ -k ] [ -t tmpdir ] [ -h homedir ] [ -Z context ] &#8212; executable [args]</p>
<h2>Description</h2>
<p>Run the <i>executable</i> within the specified context, using the alternate home directory and /tmp directory. The seunshare command unshares from the default namespace, then mounts the specified homedir and tmpdir over the default homedir and /tmp. Finally it tells the kernel to execute the application under the specified SELinux context. </p>
<dl>
<dt><code>-h homedir</code></p>
<dd>Alternate homedir to be used by the application. Homedir must be owned by the user.</p>
<dt><code>-t tmpdir</p>
<dd>Use alternate tempory directory to mount on /tmp. tmpdir must be owned by the user.</p>
<dt>-C &#8211;capabilities</code></p>
<dd>Allow apps executed within the namespace to use capabilities. Default is no capabilities.</p>
<dt><code>-k &#8211;kill</code></p>
<dd>Kill all processes with matching MCS level.</p>
<dt><code>-Z context</p>
<dd>Use alternate SELinux context while running the executable.</p>
<dt>-v</code></p>
<dd>Verbose output</dl>
<h2>See Also</h2>
<dl>
<dt><a href="/docs/linux/man/1-runcon/">runcon</a>(1), <a href="/docs/linux/man/8-sandbox/">sandbox</a>(8), <a href="/docs/linux/man/8-selinux/">selinux</a>(8)</p>
<dd></dl>
<h2>Author</h2>
<p>This manual page was written by <i>Dan Walsh &lt;dwalsh [at] redhat.com&gt;</i> and <i>Thomas Liu &lt;tliu [at] fedoraproject.org&gt;</i></p>
