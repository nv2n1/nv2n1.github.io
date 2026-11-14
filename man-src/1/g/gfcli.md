---
title: "gfcli(1)"
name: "gfcli"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfcli/"
description: "gfcli – manual page for gfcli (glusterfs-coreutils) 0.2.0"
---

<h2>NAME</h2>
<p> gfcli &#8211; manual page for gfcli (glusterfs-coreutils) 0.2.0</p>
<h2>SYNOPSIS</h2>
<p> <code>gfcli</code> [<i>OPTION</i>]&#8230; [<i>URL</i>]</p>
<h2>DESCRIPTION</h2>
<p> Start a Gluster shell to execute commands on a remote Gluster volume.</p>
<dl>
<dt><code>-o</code>, <code>&#8211;xlator-option</code>=<i>OPTION</i></p>
<dd> specify a translator option for the connection. Multiple options are supported and take the form xlator.key=value.</p>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></p>
<dd> specify a port on which to connect</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> gfcli <a href="glfs://localhost/groot">glfs://localhost/groot</a></p>
<dt>
<dd> Start a shell with a connection to localhost opened.</p>
<dt>
<dd> gfcli -o *replicate*.data-self-heal=on <a href="glfs://localhost/groot">glfs://localhost/groot</a></p>
<dt>
<dd> Start a shell with a connection localhost open, with the translator option data-self-head set to on.</dl>
<h2>AUTHOR</h2>
<p> Written by Craig Cabrey.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2015 Facebook, Inc. License GPLv3: GNU GPL version 3 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl-3.0.en.html">http://www.gnu.org/licenses/gpl-3.0.en.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
