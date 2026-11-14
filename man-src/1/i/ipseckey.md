---
title: "ipseckey(1)"
name: "ipseckey"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipseckey/"
description: "ipseckey – Generate IPSECKEY records on libreswan IPsec servers"
---

<h2 class="name">NAME</h2>
<p> ipseckey &#8211; Generate IPSECKEY records on libreswan IPsec servers </p>
<h2>SYNTAX</h2>
<p> ipseckey</p>
<h2>DESCRIPTION</h2>
<p> ipseckey generates RFC-4025 IPSECKEY DNS records based on the public key of the IPsec server. Supported IPsec software is libreswan and some versions of openswan (depending on its implementation of showhostkey). The record is displayed will have the label of the hostname. This can be manually changed. </p>
<p> (TODO: allow specifying &#8211;hostname and allow &#8211;reverse for creating in-addr.arpa. entries)</p>
<h2>OPTIONS</h2>
<p> <code>-h / &#8211;help</code></p>
<dl>
<dt>
<dd> Output help information and exit.</dl>
<p> <code>-v / &#8211;version</code></p>
<dl>
<dt>
<dd> Output version information and exit.</dl>
<h2>FILES</h2>
<p> The NSS IPsec database in /etc/ipsec.d/*.db or for older openswan without NSS /etc/ipsec.secrets</p>
<h2>REQUIREMENTS</h2>
<p> ipseckey MUST be run on the IPsec gateway itself because unlike TLS, IPsec servers do not present their public RSA key any client. Currently, only libreswan IPsec is supported (m[blue]<code><a rel="nofollow" href="https://libreswan.org">https://libreswan.org</a></code>m[]) although some versions of openswan might work as well. Root access is needed because the public key is pulled from /etc/ipsec.secrets which can contain secrets and is therefor only readable by root (even though with libreswan, ipsec.secrets does not contain the any private RSA keys)</p>
<h2>BUGS</h2>
<p> Some other IPsec software is not yet supported</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-ipsec_showhostkey/">ipsec_showhostkey</a></code>(8) and RFC-4025</p>
<h2>AUTHORS</h2>
<p> Paul Wouters &lt;pwouters [at] redhat.com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2015 Paul Wouters </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. See &lt;m[blue]<code><a rel="nofollow" href="http://www.fsf.org/copyleft/gpl.txt">http://www.fsf.org/copyleft/gpl.txt</a></code>m[]&gt;. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License (file COPYING in the distribution) for more details. </p>
<h2>Index</h2>
