---
title: "ipsec(8)"
name: "ipsec"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec/"
description: "ipsec – invoke IPsec utilities"
---

<p>ipsec &#8211; invoke IPsec utilities</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>command</i> [<i>argument</i>&#8230;] <i>ipsec</i> &#8211;help</p>
<dd><i>ipsec</i> &#8211;version</p>
<dd><i>ipsec</i> &#8211;directory</dl>
<h2>Description</h2>
<p><i>ipsec</i></p>
<dd>invokes any of several utilities involved in controlling the IPsec encryption/authentication system, running the specified <i>command</i> with the specified <i>argument</i>s as if it had been invoked directly. This largely eliminates possible name collisions with other software, and also permits some centralized services. </p>
<p> <code>ipsec &#8211;help</code> lists the available commands. Most have their own manual pages, e.g. <code><a href="/docs/linux/man/8-ipsec_auto/">ipsec_auto</a></code>(8) for <i>auto</i>. </p>
<p> <code>ipsec &#8211;version</code> outputs the software version. A version code of the form &#8220;U<i>xxx</i>/K<i>yyy</i>&#8221; indicates that the user-level utilities are version <i>xxx</i> but the kernel portion appears to be version <i>yyy</i> (this form is used only if the two disagree). For the NETKEY/XFRM stack, the kernel version is used, always displaying the U/K split. </p>
<p> <code>ipsec &#8211;directory</code> reports where <code>ipsec</code> thinks the IPsec commands are stored.</p>
<h2>Commands</h2>
<p>To get a list of supported commands, use ipsec &#8211;help. A few of the commonly used commands are described below </p>
<p> <code>ipsec setup start|stop|restart</code> maps to the host init system. Supported init systems are sysv, systemd, upstart and openrc. </p>
<p> <code>ipsec barf</code> dumps the internal system status to stdout for debugging </p>
<p> <code>ipsec auto</code> is used to manually add, remove, up or down connections. For more information see &#8216;man ipsec_auto </p>
<p> <code>ipsec whack</code> is used to communicate direct commands to the pluto daemon using the whack interface. For more information see &#8216;man ipsec_pluto&#8217; </p>
<p> <code>ipsec initnss</code> initialises the NSS database that contains all the X.509 certificate information and private RSA keys </p>
<p> <code>ipsec checknss</code> is ussed to check the NSS database and initialize it when it is not present. </p>
<p> <code>ipsec import</code> is used to import PKCS#12 X.509 files into the NSS database </p>
<p> <code>ipsec checknflog</code> is used to initialise iptables rules for the nflog devices when specified via the nflog= or nflog-all= configuration options. </p>
<p> <code>ipsec stopnflog</code> is used to delete iptables rules for the nflog devices.</p>
<h2>Return Code</h2>
<p>The ipsec command passes the return code of the sub-command back to the caller. The only exception is when <code>ipsec pluto</code> is used without &#8211;nofork, as it will fork into the background and the ipsec command returns success while the pluto daemon may in fact exit with an error code after the fork.</p>
<h2>Files</h2>
<p>/usr/libexec/ipsec usual utilities directory</p>
<h2>See Also</h2>
<p>ipsec.<code><a href="/docs/linux/man/5-conf/">conf</a></code>(5), ipsec.<code><a href="/docs/linux/man/5-secrets/">secrets</a></code>(5), <code><a href="/docs/linux/man/8-ipsec_auto/">ipsec_auto</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_setup/">ipsec_setup</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_showhostkey/">ipsec_showhostkey</a></code>(8)</p>
<h2>Author</h2>
<p><code>Henry Spencer</code></p>
<dl>
<dd></dl>
