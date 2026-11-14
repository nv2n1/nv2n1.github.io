---
title: "virtfs-proxy-helper(1)"
name: "virtfs-proxy-helper"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virtfs-proxy-helper/"
description: "virtfs-proxy-helper – QEMU 9p virtfs proxy filesystem helper"
---

<h2 class="name">NAME</h2>
<p> virtfs-proxy-helper &#8211; QEMU 9p virtfs proxy filesystem helper </p>
<h2>SYNOPSIS</h2>
<p> <code>virtfs-proxy-helper</code> <i>options</i></p>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd> Pass-through security model in <font SIZE="-1">QEMU</font> 9p server needs root privilege to do few file operations (like chown, chmod to any mode/uid:gid). There are two issues in pass-through security model </p>
<p> 1) <font SIZE="-1">TOCTTOU</font> vulnerability: Following symbolic links in the server could provide access to files beyond 9p export path. </p>
<p> 2) Running <font SIZE="-1">QEMU</font> with root privilege could be a security issue. </p>
<p> To overcome above issues, following approach is used: A new filesystem type &#8216;proxy&#8217; is introduced. Proxy <font SIZE="-1">FS</font> uses chroot + socket combination for securing the vulnerability known with following symbolic links. Intention of adding a new filesystem type is to allow qemu to run in non-root mode, but doing privileged operations using socket <font SIZE="-1">IO.</font> </p>
<p> Proxy helper(a stand alone binary part of qemu) is invoked with root privileges. Proxy helper chroots into 9p export path and creates a socket pair or a named socket based on the command line parameter. <font SIZE="-1">QEMU</font> and proxy helper communicate using this socket. <font SIZE="-1">QEMU</font> proxy fs driver sends filesystem request to proxy helper and receives the response from it. </p>
<p> The proxy helper is designed so that it can drop root privileges except for the capabilities needed for doing filesystem operations.</dl>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-h</code></p>
<dd> Display help and exit</p>
<dt><code>-p|&#8211;path path</code></p>
<dd> Path to export for proxy filesystem driver</p>
<dt><code>-f|&#8211;fd socket-id</code></p>
<dd> Use given file descriptor as socket descriptor for communicating with qemu proxy fs drier. Usually a helper like libvirt will create socketpair and pass one of the fds as parameter to -f|&#8211;fd</p>
<dt><code>-s|&#8211;socket socket-file</code></p>
<dd> Creates named socket file for communicating with qemu proxy fs driver</p>
<dt><code>-u|&#8211;uid uid -g|&#8211;gid gid</code></p>
<dd> uid:gid combination to give access to named socket file</p>
<dt><code>-n|&#8211;nodaemon</code></p>
<dd> Run as a normal program. By default program will run in daemon mode</dl>
<h2>AUTHOR</h2>
<p> M. Mohan Kumar </p>
<h2>Index</h2>
