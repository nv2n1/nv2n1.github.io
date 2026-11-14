---
title: "nfnl_osf(8)"
name: "nfnl_osf"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nfnl_osf/"
description: "nfnl_osf – OS fingerprint loader utility"
---

<p>nfnl_osf &#8211; OS fingerprint loader utility</p>
<h2>Synopsis</h2>
<p><code>nfnl_osf</code> <code>-f</code><i> fingerprints</i> [ <code>-d</code> ] </p>
<h2>Description</h2>
<p>The <code>nfnl_osf</code> utility allows to load a set of operating system signatures into the kernel for later matching against using iptables&#8217; <code>osf</code> match. </p>
<h2>Options</h2>
<dl>
<dt><code>-f</code><i> fingerprints</i></p>
<dd>Read signatures from file <i>fingerprints</i>. </p>
<dt><code>-d</code></p>
<dd>Instead of adding the signatures from <i>fingerprints</i> into the kernel, remove them. </p>
</dl>
<h2>Exit Status</h2>
<p>Exit status is 0 if command succeeded, otherwise a negative return code indicates the type of error which happened: </p>
<dl>
<dt><code>-1</code></p>
<dd>Illegal arguments passed, fingerprints file not readable or failure in netlink communication. </p>
<dt><code>-ENOENT</code></p>
<dd>Fingerprints file not specified. </p>
<dt><code>-EINVAL</code></p>
<dd>Netlink handle initialization failed or fingerprints file format invalid. </p>
</dl>
<h2>Files</h2>
<p>An up to date set of operating system signatures can be downloaded from <a rel="nofollow" href="http://www.openbsd.org/cgi-bin/cvsweb/src/etc/pf.os">http://www.openbsd.org/cgi-bin/cvsweb/src/etc/pf.os</a> .</p>
<h2>See Also</h2>
<p>The description of <code>osf</code> match in <code><a href="/docs/linux/man/8-iptables-extensions/">iptables-extensions</a></code>(8) contains further information about the topic as well as example <code>nfnl_osf</code> invocations. </p>
