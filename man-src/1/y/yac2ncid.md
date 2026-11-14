---
title: "yac2ncid(1)"
name: "yac2ncid"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yac2ncid/"
description: "yac2ncid – YAC server to NCID server gateway"
---

<h2>NAME</h2>
<p> <code>yac2ncid</code> &#8211; YAC server to NCID server gateway</p>
<h2>SYNOPSIS</h2>
<p> <code>yac2ncid</code> [-v]</p>
<h2>DESCRIPTION</h2>
<p> <code>YAC2NCID</code> acts as a YAC client, listens to the CID information from a YAC server and sends it to the NCID server. The server then sends the CID information to the NCID clients. </p>
<p> It is important to understand that to run YAC server with NCID clients you must run YAC2NCID gateway as well as NCID server. </p>
<p> The configuration file for <i>ncid</i> is <i>/etc/ncid/ncid.conf</i>. It may be located in same directory as the script, or in the <i>etc</i> directory, or in NCID default configuration directory. Read the comments in the config file for more details. </p>
<p> <code>YAC2NCID</code> can run on any system, but normally it is run on same box as the NCID server. If it is not run on the same box as the NCID server, you must configure the server IP address in the configuration file. </p>
<p> Configure the YAC server with IP address of the box running <code>YAC2NCID</code>. </p>
<p> <code>YAC2NCID</code> relies on netcat binary (nc). As there are multiple implementations of this binary in existence, the script will try to autodetect the options to use. If script is unable to properly detect the version of nc, set NETCAT_TYPE to CUSTOM in the config file and set custom params to match your version. </p>
<p> There is also a client output module called <i>ncid-yac</i>. It sends the NCID CID information to YAC clients.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Verbose mode.</dl>
<h2>REQUIRED PROGRAMS</h2>
<p> netcat: /usr/bin/nc</p>
<h2>FILES</h2>
<p> /etc/ncid/yac2ncid.conf</p>
<h2>SEE ALSO</h2>
<p> yac2ncid.conf.5, ncidd.8, ncidd.conf.5, ncidd.alias.5, ncidmodules.1 </p>
<h2>Index</h2>
