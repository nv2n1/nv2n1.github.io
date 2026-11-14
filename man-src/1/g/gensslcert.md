---
title: "gensslcert(1)"
name: "gensslcert"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gensslcert/"
description: "genSslCert – Generate SSL certificates for Small-Footprint CIM Broker (sfcb)"
---

<p>genSslCert &#8211; Generate SSL certificates for Small-Footprint CIM Broker (sfcb)</p>
<h2>Synopsis</h2>
<p><code>genSslCert</code></p>
<h2>Description</h2>
<p>Script to generate the server.pem and client.pem SSL certificate files to enable the Small-Footprint CIM Broker to handle https requests from CIM clients.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/share/sfcb/genSslCert.sh</i></p>
<dd>The genSslCert script.</p>
<dt><i>/etc/sfcb/server.pem</i></p>
<dd>The server certificate file.</p>
<dt><i>/etc/sfcb/client.pem</i></p>
<dd>The client certificate file.</dl>
<h2>Prerequisites</h2>
<p>Requires OpenSSL package to be installed.</p>
<h2>Author</h2>
<p>Adrian Schuur &lt;schuur [at] de.ibm.com&gt;</p>
<h2>Bugs</h2>
<p>The SBLIM project maintains a mailing list to which you should direct all questions regarding sfcb, sfcc, wbemcli, or any of the SBLIM providers. To subscribe to this mailing list visit</p>
<dl>
<dd><a rel="nofollow" href="http://lists.sourceforge.net/lists/listinfo/sblim-issues">http://lists.sourceforge.net/lists/listinfo/sblim-issues</a></dl>
<p> The SBLIM Project Bug tracking page can be found at</p>
<dl>
<dd><a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=128809">http://sourceforge.net/tracker/?group_id=128809</a>&amp;atid=712784</dl>
<h2>Copyright</h2>
<p>(C) Copyright IBM Corp. 2004, 2005</p>
<h2>Availability</h2>
<p>The Small-Footprint CIM Broker (sfcb) is a part of the SBLIM project. The most recent version is available on the web at</p>
<dl>
<dd><a rel="nofollow" href="http://sblim.sourceforge.net/">http://sblim.sourceforge.net/</a></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sfcbd/">sfcbd</a></code>(1)</p>
