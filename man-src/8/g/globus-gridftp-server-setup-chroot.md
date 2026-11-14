---
title: "globus-gridftp-server-setup-chroot(8)"
name: "globus-gridftp-server-setup-chroot"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-gridftp-server-setup-chroot/"
description: "globus-gridftp-server-setup-chroot – Set up a chroot for the Globus GridFTP server"
---

<p>globus-gridftp-server-setup-chroot &#8211; Set up a chroot for the Globus GridFTP server</p>
<h2>Synopsis</h2>
<p>globus-gridftp-server-setup-chroot [-h] [-c CERT-DIR] -r NEW-CHROOT</p>
<h2>Description</h2>
<p>The <code>globus-gridftp-server-setup-chroot</code> program creates a chroot directory tree that can be used for the <code><a href="/docs/linux/man/8-globus-gridftp-server/">globus-gridftp-server</a></code>(8). This chroot contains a copy of essential POSIX devices in dev; hosts, group, passwd, and grid-security configuration files in etc; and a temporary file directory in tmp. </p>
<p> The <i>-c CERT-DIR</i> option copies certificate files from a different directory than the default [/etc/grid-security/certificates].</p>
<h2>Options</h2>
<p><code>-h</code></p>
<dl>
<dd>Print short usage and exit</dl>
<p> <code>-r NEW-CHROOT</code></p>
<dl>
<dd>Specify the new chroot directory to create.</dl>
<p> <code>-c CERT-DIR</code></p>
<dl>
<dd>Specify the trusted certificate dir source.</dl>
<h2>Exit Status</h2>
<p>0</p>
<dl>
<dd>Successful program execution.</dl>
<p> 1</p>
<dl>
<dd>Error</dl>
<h2>Author</h2>
<p>Copyright &#169; 1999-2015 University of Chicago</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-globus-gridftp-server/">globus-gridftp-server</a></code>(8) </p>
