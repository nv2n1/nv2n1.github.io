---
title: "ipsec__stackmanager(8)"
name: "ipsec__stackmanager"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec__stackmanager/"
description: "ipsec__stackmanager – internal script to bring up kernel components for Libreswan"
---

<p>ipsec__stackmanager &#8211; internal script to bring up kernel components for Libreswan</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>_stackmanager start</i>&nbsp;<wbr>[&#8211;netkey]</p>
<dt> <code>ipsec</code> <i>_stackmanager stop</i></dl>
<h2>Description</h2>
<p><i>ipsec _stackmanager</i></p>
<dd>is called from within the init sub-system (systemd, upstart, sysv initscripts) to bring up the Libreswan kernel component as configured via the <i>protostack=</i> option in the <i>ipsec.conf</i> configuration file. </p>
<p> This involves loading and optionally unloading of the required kernel modules. Because the Linux kernel cannot autodetect most crypto related drivers on-demand, _stackmanager handles loading the hardware random number (RNG) device drivers, OpenBSD/FreeBSD Cryptographic Framework (OCF) drivers, CryptoAPI drivers, and the modules for the specific stack (Linux NETKEY/XFM or KLIPS/MAST). Probing for OCF supported hardware is not supported &#8211; those modules must be loaded by the system before the start of the Libreswan sub system. </p>
<p> When the &#8211;netkey option is given to the start command, the netkey stack is loaded regardless of the existence or contents of the ipsec.conf file. This is used for docker tests where the host system, which might not have libreswan installed, needs to run _stackmanager from the source tree to load the modules on the host so the modules are available inside the containers.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_tncfg/">ipsec_tncfg</a></code>(8), <code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5), <code><a href="/docs/linux/man/8-ipsec_addconn/">ipsec_addconn</a></code>(8), <code><a href="/docs/linux/man/8-pluto/">pluto</a></code>(8)</p>
<h2>History</h2>
<p>This script was introduced in Libreswan. On the older Openswan systems, this functionality was split over various script files such as ipsec _startnetkey, ipsec _startklips, ipsec _realsetup and ipsec setup. Man page written for the Libreswan project &lt;m[blue]<code><a rel="nofollow" href="http://www.libreswan.org/">http://www.libreswan.org/</a></code>m[]&gt; by Paul Wouters.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
