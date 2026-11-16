---
title: "pptpsetup(8)"
name: "pptpsetup"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pptpsetup/"
---

pptpsetup - Point-to-Point Tunneling Protocol setup

<h2>Synopsis</h2>

<pre> pptpsetup --create &lt;TUNNEL&gt; --server &lt;SERVER&gt; [--domain &lt;DOMAIN&gt;]
 --username &lt;USERNAME&gt; [--password &lt;PASSWORD&gt;]
 [--encrypt] [--start]
 pptpsetup --delete &lt;TUNNEL&gt;</pre>

<h2>Description</h2>

<font SIZE="-1">PPTP</font> Client is a Linux, FreeBSD, NetBSD and OpenBSD client for the proprietary Microsoft Point-to-Point Tunneling Protocol, <font SIZE="-1">PPTP.</font> 

 This script configures <font SIZE="-1">PPTP</font> Client on Linux.

<h2>Options</h2>

<dl><dt>--create <font SIZE="-1">TUNNEL</font>
</dt><dd>create a tunnel named <font SIZE="-1">TUNNEL</font>
</dd><dt>--delete <font SIZE="-1">TUNNEL</font>
</dt><dd>delete the file /etc/ppp/peers/TUNNEL and any lines from /etc/ppp/chap-secrets that contains ``<font SIZE="-1">TUNNEL''</font> as a single word
</dd><dt>--server <font SIZE="-1">SERVER</font>
</dt><dd>the <font SIZE="-1">IP</font> address or host name of the server
</dd><dt>--domain <font SIZE="-1">DOMAIN</font>
</dt><dd>the authentication domain name (optional)
</dd><dt>--username <font SIZE="-1">USERNAME</font>
</dt><dd>the username you are to use
</dd><dt>--password <font SIZE="-1">PASSWORD</font>
</dt><dd>the password you are to use. If you don't specify a password, pptpsetup will ask for one.
</dd><dt>--encrypt
</dt><dd>whether encryption is required
</dd><dt>--start
</dt><dd>whether the connection should be started after configuration.</dd></dl>

<h2>Author</h2>

Nelson Ferraz &lt;nferraz at gmail.com&gt;, based on James Cameron's <font SIZE="-1">PPTP</font> Client Debian <font SIZE="-1">HOWTO.</font>

<h2>See Also</h2>

<dl><dt><font SIZE="-1">PPTP</font> Client Debian <font SIZE="-1">HOWTO</font>
</dt><dd><a rel="nofollow" HREF="http://pptpclient.sourceforge.net/howto-debian.phtml">http://pptpclient.sourceforge.net/howto-debian.phtml</a>
</dd><dt><font SIZE="-1">PPTP</font> Client Diagnosis <font SIZE="-1">HOWTO</font>
</dt><dd><a rel="nofollow" HREF="http://pptpclient.sourceforge.net/howto-diagnosis.phtml">http://pptpclient.sourceforge.net/howto-diagnosis.phtml</a></dd></dl>

<h2>Copyright</h2>

pptpsetup - Point-to-Point Tunneling Protocol setup 

 Copyright (C) 2006 Nelson Ferraz 

 This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, <font SIZE="-1">MA</font> 02110-1301 <font SIZE="-1">USA</font>
