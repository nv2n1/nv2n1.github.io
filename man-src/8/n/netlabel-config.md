---
title: "netlabel-config(8)"
name: "netlabel-config"
section: "8"
letter: "n"
url: "/docs/linux/man/8-netlabel-config/"
description: "netlabel-config – NetLabel configuration utility"
---

<p>netlabel-config &#8211; NetLabel configuration utility</p>
<h2>Synopsis</h2>
<p><code>netlabelctl</code> reset| load</p>
<h2>Description</h2>
<p>The NetLabel configuration utility, netlabel-config, is a script designed to make it easier for system administratiors to create, manage, and use complex NetLabel configurations. The netlabel-config script uses the <a href="/docs/linux/man/8-netlabelctl/">netlabelctl</a>(8) tool and /etc/netlabel.rules configuration file to load a saved NetLabel configuration into the kernel and reset the kernel&#8217;s NetLabel configuration to the default state when needed.</p>
<dl>
<dt><code>reset</code></p>
<dd>Removes any NetLabel configuration loaded into the kernel and resets the kernel&#8217;s NetLabel state to the default.</p>
<dt><code>load</code></p>
<dd>Loads the NetLabel configuration specified by /etc/netlabel.rules into the kernel.</dl>
<h2>Exit Status</h2>
<p>Returns zero on success, errno values on failure.</p>
<h2>Notes</h2>
<p>The NetLabel subsystem is supported on Linux Kernels version 2.6.19 and later. The static, or fallback, labels are only supported on Linux Kernels version 2.6.25 and later. The domain mapping address selectors are only supported on Linux Kernels 2.6.28 and later. </p>
<p> The NetLabel project site, with more information including the source code repository, can be found at <a rel="nofollow" href="http://netlabel.sf.net.">http://netlabel.sf.net.</a> This program is currently under development, please report any bugs at the project site or directly to the author.</p>
<h2>Author</h2>
<p>Paul Moore &lt;paul [at] paul-moore.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-netlabelctl/">netlabelctl</a></code>(8) </p>
