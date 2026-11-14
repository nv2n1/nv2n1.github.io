---
title: "xwrapper-config(5)"
name: "xwrapper-config"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xwrapper-config/"
description: "Xorg.wrap – Xorg X server binary wrapper"
---

<p>Xorg.wrap &#8211; Xorg X server binary wrapper</p>
<h2>Description</h2>
<p>The Xorg X server may need root rights to function properly. To start the Xorg X server with these rights your system is using a suid root wrapper installed as /usr/lib/xorg/Xorg.wrap which will execute the real X server which is installed as /usr/lib/xorg/Xorg. By default Xorg.wrap will autodetect if root rights are necessary, and if not it will drop its elevated rights before starting the real X server. By default Xorg.wrap will only allow executing the real X server from login sessions on a physical console. </p>
<h2>Config File</h2>
<p>Xorg.wrap&#8217;s default behavior can be overridden from the <i>/etc/X11/Xwrapper.config</i> config file. Lines starting with a <code>#</code> in Xwrapper.config are considered comments and will be ignored. Any other non empty lines must take the form of <code>key</code> = <i>value</i>.</p>
<dl>
<dt><code>allowed_users</code> = <i>rootonly</i>|<i>console</i>|<i>anybody</i></p>
<dd>Specify which users may start the X server through the wrapper. Use <i>rootonly</i> to only allow root, use <i>console</i> to only allow users logged into a physical console, and use <i>anybody</i> to allow anybody. The default is <i>console</i>.</p>
<dt><code>needs_root_rights</code> = <i>yes</i>|<i>no</i>|<i>auto</i></p>
<dd>Configure if the wrapper should drop its elevated (root) rights before starting the X server. Use <i>yes</i> to force execution as root, <i>no</i> to force execution with all suid rights dropped, and <i>auto</i> to let the wrapper auto-detect. The default is <i>auto</i>.</dl>
<p> When auto-detecting the wrapper will drop rights if kms graphics are available and not drop them if no kms graphics are detected. If a system has multiple graphics cards and some are not kms capable auto-detection may fail, in this case manual configuration should be used.</p>
<h2>See Also</h2>
<p>Xorg X server information: <i><a href="/docs/linux/man/1-xorg/">Xorg</a></i>(1) </p>
