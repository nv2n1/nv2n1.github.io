---
title: "virt-pki-validate(1)"
name: "virt-pki-validate"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-pki-validate/"
description: "virt-pki-validate – validate libvirt PKI files are configured correctly"
---

<h2 class="name">NAME</h2>
<p> virt-pki-validate &#8211; validate libvirt PKI files are configured correctly </p>
<h2>SYNOPSIS</h2>
<p> <code>virt-pki-validate</code> [<i></i><font SIZE="-1"><i>OPTION</i></font><i></i>]</p>
<h2>DESCRIPTION</h2>
<p> This tool validates that the necessary <font SIZE="-1">PKI</font> files are configured for a secure libvirt server or client using the <font SIZE="-1">TLS</font> encryption protocol. It will report any missing certificate or key files on the host. It should be run as root to ensure it can read all the necessary files</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display command line help usage then exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Display version information then exit.</dl>
<h2>EXIT STATUS</h2>
<p> Upon successful validation, an exit status of 0 will be set. Upon failure a non-zero status will be set.</p>
<h2>AUTHOR</h2>
<p> Richard Jones</p>
<h2>BUGS</h2>
<p> Report any bugs discovered to the libvirt community via the mailing list &lt;<a rel="nofollow" href="http://libvirt.org/contact.html">http://libvirt.org/contact.html</a>&gt; or bug tracker &lt;<a rel="nofollow" href="http://libvirt.org/bugs.html">http://libvirt.org/bugs.html</a>&gt;. Alternatively report bugs to your software distributor / vendor.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2006-2012 by Red Hat, Inc.</p>
<h2>LICENSE</h2>
<p> virt-pki-validate is distributed under the terms of the <font SIZE="-1">GNU GPL</font> v2+. This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE</font></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1), online <font SIZE="-1">PKI</font> setup instructions &lt;<a rel="nofollow" href="http://libvirt.org/remote.html">http://libvirt.org/remote.html</a>&gt; </p>
<h2>Index</h2>
