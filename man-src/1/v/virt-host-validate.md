---

title: "virt-host-validate(1)"
name: "virt-host-validate"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-host-validate/"
description: "virt-host-validate – validate host virtualization setup"
---

<p> virt-host-validate &#8211; validate host virtualization setup </p>
<h2>SYNOPSIS</h2>
<p> <code>virt-host-validate</code> [<i></i><i>OPTIONS</i><i></i>&#8230;] [<i>HV-TYPE</i>]</p>
<h2>DESCRIPTION</h2>
<p> This tool validates that the host is configured in a suitable way to run libvirt hypervisor drivers. If invoked without any arguments it will check support for all hypervisor drivers it is aware of. Optionally it can be given a particular hypervisor type (&#8216;qemu&#8217;, &#8216;lxc&#8217; or &#8216;bhyve&#8217;) to restrict the checks to those relevant for that virtualization technology</p>
<h2>OPTIONS</h2>
<dl>
<dt>&quot;-v&quot;, &quot;&#8211;version&quot;</dt>
<dd> Display the command version</dd>
<dt>&quot;-h&quot;, &quot;&#8211;help&quot;</dt>
<dd> Display the command line help</dd>
<dt>&quot;-q&quot;, &quot;&#8211;quiet&quot;</dt>
<dd> Don&#8217;t display details of individual checks being performed. Only display output if a check does not pass.</dd></dl>
<h2>EXIT STATUS</h2>
<p> Upon successful validation, an exit status of 0 will be set. Upon failure a non-zero status will be set.</p>
<h2>AUTHOR</h2>
<p> Daniel P. Berrange</p>
<h2>BUGS</h2>
<p> Report any bugs discovered to the libvirt community via the mailing list &lt;<a rel="nofollow" href="http://libvirt.org/contact.html">http://libvirt.org/contact.html</a>&gt; or bug tracker &lt;<a rel="nofollow" href="http://libvirt.org/bugs.html">http://libvirt.org/bugs.html</a>&gt;. Alternatively report bugs to your software distributor / vendor.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2012 by Red Hat, Inc.</p>
<h2>LICENSE</h2>
<p> virt-host-validate is distributed under the terms of the GNU GPL v2+. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1), <i><a href="/docs/linux/man/1-virt-pki-validate/">virt-pki-validate</a></i>(1), <i><a href="/docs/linux/man/1-virt-xml-validate/">virt-xml-validate</a></i>(1) </p>
