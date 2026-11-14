---
title: "modules(5)"
name: "modules"
section: "5"
letter: "m"
url: "/docs/linux/man/5-modules/"
description: "/etc/modules – kernel modules to load at boot time"
---

<p>/etc/modules &#8211; kernel modules to load at boot time</p>
<h2>Description</h2>
<p>The <code>/etc/modules</code> file contains the names of kernel modules that are to be loaded at boot time, one per line. Options can only be specified using <code>modprobe.d</code> configuration files. Lines beginning with a &#8216;#&#8217; are ignored.</p>
<h2>Example</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;/etc/modules: kernel modules to load at boot time.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;This file contains the names of kernel modules that<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;should be loaded at boot time, one per line. Lines<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;beginning with&nbsp;&quot;#&quot;&nbsp;are ignored. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;w83781d </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3c509<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nf_nat_ftp</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-depmod/">depmod</a></code>(8) <code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8) <code><a href="/docs/linux/man/5-modprobe-d/">modprobe.d</a></code>(5) </p>
