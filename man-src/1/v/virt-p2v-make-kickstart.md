---
title: "virt-p2v-make-kickstart(1)"
name: "virt-p2v-make-kickstart"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-p2v-make-kickstart/"
description: "virt-p2v-make-kickstart – Build the virt-p2v kickstart"
---

<h2 class="name">NAME</h2>
<p> virt-p2v-make-kickstart &#8211; Build the virt-p2v kickstart </p>
<h2>SYNOPSIS</h2>
<pre><code>
 virt-p2v-make-kickstart [-o p2v.ks] [--proxy=http://...] repo [repo...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1) converts a physical machine to run virtualized on <font SIZE="-1">KVM,</font> managed by libvirt, OpenStack, oVirt, Red Hat Enterprise Virtualisation (<font SIZE="-1">RHEV</font>), or one of the other targets supported by <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1). </p>
<p> Kickstart is a format used by Red Hat-derived distributions (such as Fedora, Red Hat Enterprise Linux, CentOS, Scientific Linux, and others) to describe how to make live CDs, install the distro, make &#8220;Spins&#8221; and so on. It is driven by a kickstart file. </p>
<p> virt-p2v-make-kickstart builds a kickstart file which can be used to build a bootable P2V <font SIZE="-1">ISO,</font> live <font SIZE="-1">CD, USB</font> key, or <font SIZE="-1">PXE</font> image. This tool only builds the kickstart file, but this manual page describes some of the ways you can use the kickstart file.</p>
<h2>BUILDING THE KICKSTART FILE</h2>
<p> Using virt-p2v-make-kickstart is very simple: </p>
<pre>
 virt-p2v-make-kickstart fedora
</pre>
<p> will build a kickstart file for Fedora. The kickstart file will be called <i>p2v.ks</i> and located in the current directory. </p>
<p> The parameters are a list of one or more repositories. Some built-in repositories are available: <tt>&quot;fedora&quot;</tt>, <tt>&quot;rawhide&quot;</tt>, <tt>&quot;koji&quot;</tt> or <tt>&quot;rhel-VERSION&quot;</tt> (eg. <tt>&quot;rhel-7.1&quot;</tt>). You can also use a <font SIZE="-1">URL</font> as a parameter to point to a repository, for example: </p>
<pre>
 virt-p2v-make-kickstart <a rel="nofollow" href="https://dl.fedoraproject.org/pub/fedora/linux/releases/21/Everything/x86_64/os/">https://dl.fedoraproject.org/pub/fedora/linux/releases/21/Everything/x86_64/os/</a>
</pre>
<p> To control the name of the output file, use the <i>-o</i> parameter. To tell kickstart to use a proxy server or web cache to download files, use the <i>&#8211;proxy</i> parameter.</p>
<h2>BUILDING A LIVE CD / ISO</h2>
<p> Once you have the kickstart file, you can use <i><a href="/docs/linux/man/8-livecd-creator/">livecd-creator</a></i>(8) to make a live <font SIZE="-1">CD:</font> </p>
<pre>
 sudo livecd-creator p2v.ks
</pre>
<p> Before running this note that you should probably run <tt>&quot;livecd-creator&quot;</tt> in a disposable virtual machine for these reasons:</p>
<dl>
<dt>&bull;</p>
<dd> You have to disable SELinux when running the tool.</p>
<dt>&bull;</p>
<dd> This tool has to be run as root, and has some nasty failure modes.</p>
<dt>&bull;</p>
<dd> You can only create the exact same Live <font SIZE="-1">CD</font> distro as the host distro. Cross-builds will fail in strange ways (eg. RHBZ#1092327).</dl>
<h2>BUILDING A FEDORA SPIN USING KOJI</h2>
<p> This requires <tt>&quot;spin-livecd&quot;</tt> permissions on Koji, which are not given out usually, even to Fedora packagers. However assuming you have been given these permissions (or have your own Koji instance, I guess), then you can do: </p>
<pre>
 koji spin-livecd [--scratch] virt-p2v 1.XX.YY rawhide x86_64 p2v.ks
</pre>
<dl>
<dt>&bull;</p>
<dd> Add the <tt>&quot;--scratch&quot;</tt> option to do a scratch build (recommended for testing).</p>
<dt>&bull;</p>
<dd> <tt>&quot;1.XX.YY&quot;</tt> should match the libguestfs version</p>
<dt>&bull;</p>
<dd> Instead of <tt>&quot;rawhide&quot;</tt> you can use any Koji target.</dl>
<h2>BUILDING A BOOTABLE USB KEY</h2>
<p> Use the <i><a href="/docs/linux/man/8-livecd-iso-to-disk/">livecd-iso-to-disk</a></i>(8) program to convert the <font SIZE="-1">ISO</font> created above to a <font SIZE="-1">USB</font> key: </p>
<pre>
 sudo livecd-iso-to-disk livecd-p2v.iso /dev/sdX
</pre>
<h2>BUILDING A PXE BOOT IMAGE</h2>
<p> Use the <tt>&quot;livecd-iso-to-pxeboot&quot;</tt> program to convert the <font SIZE="-1">ISO</font> created above to a <font SIZE="-1">PXE</font> boot image. </p>
<pre>
 sudo livecd-iso-to-pxeboot livecd-p2v.iso
</pre>
<p> This creates a <tt>&quot;tftpboot&quot;</tt> subdirectory under the current directory containing the files required to <font SIZE="-1">PXE</font> boot virt-p2v: </p>
<pre>
 $ ls -1R tftpboot/
 tftpboot/:
 initrd0.img
 pxelinux.0
 pxelinux.cfg/
 vmlinuz0
 
 tftpboot/pxelinux.cfg:
 default
</pre>
<h2>32 OR 64 BIT VIRT-P2V?</h2>
<p> Virt-p2v can convert any 32 or 64 bit guest, regardless of whether virt-p2v itself is built as a 32 or 64 bit binary. The only restriction is that 64 bit virt-p2v cannot run on 32 bit hardware. </p>
<p> Old virt-p2v 0.9 was always built as a 32 bit (i686) <font SIZE="-1">ISO. </font> This meant that the <font SIZE="-1">CD</font> could be booted on any 32- or 64-bit i686 or x86-64 hardware, and could convert any guest. The old virt-p2v <font SIZE="-1">ISO</font> shipped by Red Hat was based on Red Hat Enterprise Linux (<font SIZE="-1">RHEL</font>) 6. </p>
<p> Since <font SIZE="-1">RHEL 7</font> dropped support for 32 bit machines, current virt-p2v on <font SIZE="-1">RHEL</font> can only be built for 64 bit. It cannot run on old 32 bit only hardware. </p>
<p> Fedora virt-p2v ISOs are generally built for 32 bit, so like the old <font SIZE="-1">RHEL</font> 6-based virt-p2v 0.9 they can boot on any hardware.</p>
<h2>TESTING VIRT-P2V USING QEMU</h2>
<h3><font SIZE="-1">TESTING THE P2V ISO USING QEMU</font></h3>
<p> You can use qemu to test-boot the P2V <font SIZE="-1">ISO:</font> </p>
<pre>
 qemu-kvm -m 1024 -hda /tmp/guest.img -cdrom /tmp/livecd-p2v.iso -boot d
</pre>
<p> Note that <tt>&quot;-hda&quot;</tt> is the (virtual) system that you want to convert (for test purposes). It could be any guest type supported by <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1), including Windows or Red Hat Enterprise Linux.</p>
<h3><font SIZE="-1">TESTING PXE SUPPORT USING QEMU</font></h3>
<dl>
<dt>&bull;</p>
<dd> Unpack the tftpboot directory into <i>/tmp</i> (so it appears as <i>/tmp/tftpboot</i>).</p>
<dt>&bull;</p>
<dd> Copy <i>pxelinux.0</i> and <i>ldlinux.c32</i> from syslinux (usually from <i>/usr/share/syslinux</i>) into <i>/tmp/tftpboot</i>.</p>
<dt>&bull;</p>
<dd> Adjust the <tt>&quot;APPEND&quot;</tt> line in <i>/tmp/tftpboot/pxelinux.cfg/default</i> if required. See &#8220;<font SIZE="-1">KERNEL COMMAND LINE CONFIGURATION&#8221;</font> in <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1).</p>
<dt>&bull;</p>
<dd> Run qemu like this so that it acts as a <font SIZE="-1">TFTP</font> and <font SIZE="-1">BOOTP</font> server, emulating a netboot: </p>
<pre>
 qemu-kvm \
     -m 4096 -hda /tmp/guest.img \
     -boot n \
     -netdev user,id=unet,tftp=/tmp/tftpboot,bootfile=/pxelinux.0 \
     -device virtio-net-pci,netdev=unet \
     -serial stdio
</pre>
<p> Note that this requires considerably more memory because the <font SIZE="-1">PXE</font> image is loaded into memory. Also that qemu&#8217;s <font SIZE="-1">TFTP</font> server is very slow and the virt-p2v <font SIZE="-1">PXE</font> image is very large, so it can appear to &#8220;hang&#8221; after pxelinux starts up.</dl>
<h2>ADDING EXTRA PACKAGES</h2>
<p> You can install extra packages using the <i>&#8211;install</i> option. This can be useful for making a more fully-featured virt-p2v disk with extra tools for debugging and troubleshooting. Give a list of packages, separated by commas. For example: </p>
<pre>
 virt-p2v-make-kickstart [...] --install tcpdump,traceroute
</pre>
<h2>ADDING AN SSH IDENTITY</h2>
<p> You can inject an <font SIZE="-1">SSH</font> identity (private key) file to the kickstart and hence into the <font SIZE="-1">ISO</font> using the <i>&#8211;inject-ssh-identity</i> option. Note that you <i>cannot</i> inject a key once the <font SIZE="-1">ISO</font> has been built. </p>
<p> First create a key pair. It must have an empty passphrase: </p>
<pre>
 ssh-keygen -t rsa -N '' -f id_rsa
</pre>
<p> This creates a private key (<tt>&quot;id_rsa&quot;</tt>) and a public key (<tt>&quot;id_rsa.pub&quot;</tt>) pair. The public key should be appended to the <tt>&quot;authorized_keys&quot;</tt> file on the virt-v2v conversion server (usually to <tt>&quot;/root/.ssh/authorized_keys&quot;</tt>). </p>
<p> The private key should be added to the kickstart file and then discarded: </p>
<pre>
 virt-p2v-make-kickstart [...] --inject-ssh-identity id_rsa
 rm id_rsa
</pre>
<p> The <font SIZE="-1">ISO</font> can then be built from the kickstart in the usual way (see above), and it will contain the embedded <font SIZE="-1">SSH</font> identity (<i>/var/tmp/id_rsa</i>). </p>
<p> When booting virt-p2v, specify the <font SIZE="-1">URL</font> of the injected file like this: </p>
<pre><code>
 │         User name: [root_____________________________] │
 │                                                        │
 │          Password: [    &lt;leave this field blank&gt;     ] │
 │                                                        │
 │  SSH Identity URL: [file:///var/tmp/id_rsa___________] │
</code></pre>
<p> or if using the kernel command line, add: </p>
<pre>
 p2v.identity=file:///var/tmp/id_rsa
</pre>
<p> For more information, see &#8220;<font SIZE="-1">SSH IDENTITIES&#8221;</font> in <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display help.</p>
<dt><code>&#8211;inject-ssh-identity</code> id_rsa</p>
<dd> Add an <font SIZE="-1">SSH</font> identity (private key) file into the kickstart. See &#8220;<font SIZE="-1">ADDING AN SSH IDENTITY&#8221;</font> above.</p>
<dt><code>&#8211;install</code> pkg,pkg,&#8230;</p>
<dd> Add extra packages to the kickstart <tt>%packages</tt> section. See &#8220;<font SIZE="-1">ADDING EXTRA PACKAGES&#8221;</font> above.</p>
<dt><code>-o</code> <font SIZE="-1">OUTPUT</font></p>
<dd>
<dt><code>&#8211;output</code> <font SIZE="-1">OUTPUT</font></p>
<dd> Write kickstart to <tt>&quot;OUTPUT&quot;</tt>. If not specified, the default is <i>p2v.ks</i> in the current directory.</p>
<dt><code>&#8211;proxy</code> <font SIZE="-1">URL</font></p>
<dd> Tell the kickstart to use a proxy server or web cache for downloads.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose output. Use this if you need to debug problems with the script or if you are filing a bug.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</dl>
<h2>FILES</h2>
<dl>
<dt><i>$libexecdir/virt-p2v</i></p>
<dd> The <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1) binary which is copied into the kickstart file. </p>
<p> The location of the binary can be changed by setting the <tt>&quot;VIRT_P2V_DATA_DIR&quot;</tt> environment variable.</p>
<dt><i>$datadir/virt-p2v/issue</i></p>
<dd>
<dt><i>$datadir/virt-p2v/launch-virt-p2v.in</i></p>
<dd>
<dt><i>$datadir/virt-p2v/p2v.ks.in</i></p>
<dd>
<dt><i>$datadir/virt-p2v/p2v.service</i></p>
<dd> Various data files that are used to make the kickstart. </p>
<p> The location of these files can be changed by setting the <tt>&quot;VIRT_P2V_DATA_DIR&quot;</tt> environment variable.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>&quot;VIRT_P2V_DATA_DIR&quot;</p>
<dd> The directory where virt-p2v-make-kickstart looks for data files and the virt-p2v binary (see &#8220;<font SIZE="-1">FILES&#8221;</font> above). If not set, a compiled-in location is used.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1), <i><a href="/docs/linux/man/1-virt-p2v-make-disk/">virt-p2v-make-disk</a></i>(1), <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1), <i><a href="/docs/linux/man/8-livecd-creator/">livecd-creator</a></i>(8), <i><a href="/docs/linux/man/8-livecd-iso-to-disk/">livecd-iso-to-disk</a></i>(8), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
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
<dt><a href="#lbAN">ADDING EXTRA PACKAGES</a></p>
<dd>
<dt><a href="#lbAO">ADDING AN SSH IDENTITY</a></p>
<dd>
<dt><a href="#lbAP">OPTIONS</a></p>
<dd>
<dt><a href="#lbAQ">FILES</a></p>
<dd>
<dt><a href="#lbAR">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAS">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAT">AUTHORS</a></p>
<dd>
<dt><a href="#lbAU">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAV">LICENSE</a></p>
<dd>
<dt><a href="#lbAW">BUGS</a></p>
<dd></dl>
