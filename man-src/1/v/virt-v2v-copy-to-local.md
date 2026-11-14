---
title: "virt-v2v-copy-to-local(1)"
name: "virt-v2v-copy-to-local"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-v2v-copy-to-local/"
description: "virt-v2v-copy-to-local – Copy a remote guest to the local machine"
---

<h2 class="name">NAME</h2>
<p> virt-v2v-copy-to-local &#8211; Copy a remote guest to the local machine </p>
<h2>SYNOPSIS</h2>
<pre>
 virt-v2v-copy-to-local -ic LIBVIRT_URI GUEST
 virt-v2v-copy-to-local -ic xen+<a href="ssh://root@xen.example.com">ssh://root@xen.example.com</a> xen_guest
 virt-v2v-copy-to-local -ic <a href="esx://root@esxi.example.com">esx://root@esxi.example.com</a> vmware_guest
</pre>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;virt-v2v-copy-to-local&quot;</tt> copies a guest from a remote hypervisor to the local machine, in preparation for conversion by <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1). Note this tool alone <code>does not</code> do the virt-v2v conversion.</p>
<h3>When to use this tool</h3>
<p> This tool is not usually necessary, but there are a few special cases (see list below) where you might need it. </p>
<p> If your case does not fit one of these special cases, then ignore this tool and read <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1) instead. The virt-v2v-copy-to-local process is slower than using virt-v2v directly, because it has to copy unused parts of the guest disk.</p>
<dl>
<dt>&bull;</p>
<dd> You have a Xen guest using host block devices. Virt-v2v cannot convert such guests directly. </p>
<p> See &#8220;<font SIZE="-1">XEN OR SSH CONVERSIONS FROM BLOCK DEVICES&#8221;</font> in <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1).</p>
<dt>&bull;</p>
<dd> You have VMware ESXi hypervisors, and are not using VMware vCenter to manage them. Virt-v2v cannot directly access ESXi hypervisor, so you either have to export the guest as an <font SIZE="-1">OVA </font>(eg. using VMware&#8217;s <tt>&quot;ovftool&quot;</tt>); or you can use this tool to copy the guest to a local file on the conversion server, from where virt-v2v will be able to access it. </p>
<p> See &#8220;<font SIZE="-1">INPUT FROM VMWARE</font> ESXi <font SIZE="-1">HYPERVISOR&#8221;</font> in <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1).</dl>
<h3>How this tool works</h3>
<p> This tool uses libvirt to get the libvirt <font SIZE="-1">XML </font>(metadata) of the remote guest, essentially equivalent to running <tt>&quot;virsh dumpxml guest&quot;</tt>. </p>
<p> It then uses the <font SIZE="-1">XML</font> to locate the remote guest disks, which are copied over using a hypervisor-specific method. It uses ssh for remote Xen hypervisors, and <font SIZE="-1">HTTPS </font>(curl) for remote ESXi hypervisors. </p>
<p> It then modifies the libvirt <font SIZE="-1">XML</font> so that it points at the local copies of the guest disks. </p>
<p> The libvirt <font SIZE="-1">XML</font> is output to a file called <i>guest.xml</i> (where <i>guest</i> is the name of the guest). The disk(s) are output to file(s) called <i>guest-disk1</i>, <i>guest-disk2</i> and so on. </p>
<p> After copying the guest locally, you can convert it using: </p>
<pre>
 virt-v2v -i libvirtxml guest.xml [-o options ...]
</pre>
<p> Virt-v2v finds the local copies of the disks by looking in the <font SIZE="-1">XML.</font></p>
<h2>EXAMPLES</h2>
<h3>Copy and convert from Xen hypervisor that uses host block devices</h3>
<p> For full instructions, see &#8220;<font SIZE="-1">XEN OR SSH CONVERSIONS FROM BLOCK DEVICES&#8221;</font> in <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1). </p>
<pre>
 virt-v2v-copy-to-local -ic xen+<a href="ssh://root@xen.example.com">ssh://root@xen.example.com</a> xen_guest
 virt-v2v -i libvirtxml xen_guest.xml -o local -os /var/tmp
 rm xen_guest.xml xen_guest-disk*
</pre>
<h3>Copy and convert from ESXi hypervisor</h3>
<p> For full instructions, see &#8220;<font SIZE="-1">INPUT FROM VMWARE</font> ESXi <font SIZE="-1">HYPERVISOR&#8221;</font> in <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1). </p>
<pre>
 virt-v2v-copy-to-local -ic <a href="esx://root@esxi.example.com?no_verify=1">esx://root@esxi.example.com?no_verify=1</a> vmware_guest
 virt-v2v -i libvirtxml vmware_guest.xml -o local -os /var/tmp
 rm vmware_guest.xml vmware_guest-disk*
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display help.</p>
<dt><code>-ic</code> libvirtURI</p>
<dd> Specify a libvirt connection <font SIZE="-1">URI</font></p>
<dt><code>&#8211;password-file</code> file</p>
<dd> Instead of asking for password(s) interactively, pass the password through a file. Note the file should contain the whole password, <code>without any trailing newline</code>, and for security the file should have mode <tt>0600</tt> so that others cannot read it. </p>
<p> Currently this option does not have any effect on xen+ssh transfers, but that is a bug.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> This disables progress bars and other unnecessary output.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose messages for debugging.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1), <i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/,">http://libguestfs.org/,</a> <a rel="nofollow" href="https://libvirt.org/uri.html,">https://libvirt.org/uri.html,</a> <a rel="nofollow" href="https://libvirt.org/remote.html,">https://libvirt.org/remote.html,</a> <a rel="nofollow" href="https://libvirt.org/drvesx.html.">https://libvirt.org/drvesx.html.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2016 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font></p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</p>
<dd> The version of libguestfs.</p>
<dt>&bull;</p>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</p>
<dt>&bull;</p>
<dd> Describe the bug accurately and give a way to reproduce it.</p>
<dt>&bull;</p>
<dd> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
</dl>
<h2>Index</h2>
