---
title: "sys-unconfig(8)"
name: "sys-unconfig"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sys-unconfig/"
description: "sys-unconfig – shell script to reconfigure the system upon next boot"
---

<p>sys-unconfig &#8211; shell script to reconfigure the system upon next boot</p>
<h2>Synopsis</h2>
<p><code>sys-unconfig</code></p>
<h2>Description</h2>
<p><code>sys-unconfig</code> provides a simple method of reconfiguring a system in a new environment. Upon executing sys-unconfig will poweroff your system, and run firstboot at next boot. </p>
<h2>Files</h2>
<dl>
<dt><i>/.unconfigured</i></p>
<dd>The presence of this file will trigger firsboot. </p>
</dl>
<h2>Notes</h2>
<p>This utility should not be used for creating cloud or virtual machine images. For that use please see <code>virt-sysprep</code>. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a>(1)</code> </p>
<h2>Authors</h2>
<pre>H.J. Lu &lt;hjl [at] valinux.com&gt;</pre>
