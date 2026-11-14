---
title: "htcopy(1)"
name: "htcopy"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htcopy/"
description: "htcopy – HTTP client with LCGDM extensions"
---

<h2 class="name">NAME</h2>
<p> htcopy &#8211; HTTP client with LCGDM extensions</p>
<h2>SYNOPSIS</h2>
<p> <code>htcopy</code> [options] <i>[source] [destination]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>htcopy</code> is a HTTP client that implements some extensions of the protocol used by the HTTP/DAV front-end of LCGDM. The command is designed to work without user interaction. </p>
<p> It allows to copy from local to remote, from remote to local, and it can also trigger third party copies. </p>
<p> It supports multiple streams for uploads and downloads, improving the performance of the transfer. </p>
<h2>SOURCE / DESTINATION</h2>
<p> Both the source and/or the destination can be a local path or a HTTP URL. Depending on the combination, it will do an upload, a download, or trigger a third-party copy. Local copies are not supported. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h/&#8211;help</p>
<dd> Shows the command help. </p>
<dt>-v/&#8211;verbose</p>
<dd> Enable the verbose mode. It can be specified more than once (-vvv) to increase the verbosity. </p>
<dt>-l/&#8211;log &lt;log file&gt;</p>
<dd> Specified into which file the extended output (as HTTP headers) must be printed. </p>
<dt>-n/&#8211;stream-number &lt;number of streams&gt;</p>
<dd> Number of streams to use. </p>
<dt>-b, &#8211;buffer-size &lt;buffer size&gt;</p>
<dd> Internal buffer size. </p>
<dt>-E/&#8211;user-cert &lt;user certificate&gt;</p>
<dd> The path to the user certificate in PEM format. </p>
<dt>&#8211;user-key &lt;user private key&gt;</p>
<dd> The user private key in PEM format, if the user certificate doesn&#8217;t include it. </p>
<dt>&#8211;key-pass &lt;private key password&gt;</p>
<dd> Allows to pass the private key password as an argument. </p>
<dt>&#8211;ca-path &lt;CA path&gt;</p>
<dd> Use the certificate directory to verify the remote certificate. </p>
<dt>&#8211;ca-bundle &lt;CA file&gt;</p>
<dd> Use the certificate file to verify the remote certificate. </p>
<dt>&#8211;insecure</p>
<dd> Do no check the peer certificate. </p>
</dl>
<h2>Index</h2>
