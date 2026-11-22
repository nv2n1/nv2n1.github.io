---

title: "virt-p2v-make-kickstart(1)"
name: "virt-p2v-make-kickstart"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-p2v-make-kickstart/"
description: "virt-p2v-make-kickstart – Build the virt-p2v kickstart"
---

<p> virt-p2v-make-kickstart &#8211; Build the virt-p2v kickstart </p>
<h2>SYNOPSIS</h2>
<pre><code>
 virt-p2v-make-kickstart [-o p2v.ks] [--proxy=http://...] repo [repo...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1) converts a physical machine to run virtualized on KVM, managed by libvirt, OpenStack, oVirt, Red Hat Enterprise Virtualisation (RHEV), or one of the other targets supported by <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1). </p>
<p> Kickstart is a format used by Red Hat-derived distributions (such as Fedora, Red Hat Enterprise Linux, CentOS, Scientific Linux, and others) to describe how to make live CDs, install the distro, make &#8220;Spins&#8221; and so on. It is driven by a kickstart file. </p>
<p> virt-p2v-make-kickstart builds a kickstart file which can be used to build a bootable P2V ISO, live CD, USB key, or PXE image. This tool only builds the kickstart file, but this manual page describes some of the ways you can use the kickstart file.</p>
<h2>BUILDING THE KICKSTART FILE</h2>
<p> Using virt-p2v-make-kickstart is very simple: </p>
<pre>
 virt-p2v-make-kickstart fedora
</pre>
<p> will build a kickstart file for Fedora. The kickstart file will be called <i>p2v.ks</i> and located in the current directory. </p>
<p> The parameters are a list of one or more repositories. Some built-in repositories are available: <tt>&quot;fedora&quot;</tt>, <tt>&quot;rawhide&quot;</tt>, <tt>&quot;koji&quot;</tt> or <tt>&quot;rhel-VERSION&quot;</tt> (eg. <tt>&quot;rhel-7.1&quot;</tt>). You can also use a URL as a parameter to point to a repository, for example: </p>
<pre>
 virt-p2v-make-kickstart <a rel="nofollow" href="https://dl.fedoraproject.org/pub/fedora/linux/releases/21/Everything/x86_64/os/">https://dl.fedoraproject.org/pub/fedora/linux/releases/21/Everything/x86_64/os/</a>
</pre>
<p> To control the name of the output file, use the <i>-o</i> parameter. To tell kickstart to use a proxy server or web cache to download files, use the <i>&#8211;proxy</i> parameter.</p>
<h2>BUILDING A LIVE CD / ISO</h2>
<p> Once you have the kickstart file, you can use <i><a href="/docs/linux/man/8-livecd-creator/">livecd-creator</a></i>(8) to make a live CD: </p>
<pre>
 sudo livecd-creator p2v.ks
</pre>
<p> Before running this note that you should probably run <tt>&quot;livecd-creator&quot;</tt> in a disposable virtual machine for these reasons:</p>
<dl>
<dt>&bull;</dt>
<dd> You have to disable SELinux when running the tool.</dd>
<dt>&bull;</dt>
<dd> This tool has to be run as root, and has some nasty failure modes.</dd>
<dt>&bull;</dt>
<dd> You can only create the exact same Live CD distro as the host distro. Cross-builds will fail in strange ways (eg. RHBZ#1092327).</dd></dl>
<h2>BUILDING A FEDORA SPIN USING KOJI</h2>
<p> This requires <tt>&quot;spin-livecd&quot;</tt> permissions on Koji, which are not given out usually, even to Fedora packagers. However assuming you have been given these permissions (or have your own Koji instance, I guess), then you can do: </p>
<pre>
 koji spin-livecd [--scratch] virt-p2v 1.XX.YY rawhide x86_64 p2v.ks
</pre>
<dl>
<dt>&bull;</dt>
<dd> Add the <tt>&quot;--scratch&quot;</tt> option to do a scratch build (recommended for testing).</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;1.XX.YY&quot;</tt> should match the libguestfs version</dd>
<dt>&bull;</dt>
<dd> Instead of <tt>&quot;rawhide&quot;</tt> you can use any Koji target.</dd></dl>
<h2>BUILDING A BOOTABLE USB KEY</h2>
<p> Use the <i><a href="/docs/linux/man/8-livecd-iso-to-disk/">livecd-iso-to-disk</a></i>(8) program to convert the ISO created above to a USB key: </p>
<pre>
 sudo livecd-iso-to-disk livecd-p2v.iso /dev/sdX
</pre>
<h2>BUILDING A PXE BOOT IMAGE</h2>
<p> Use the <tt>&quot;livecd-iso-to-pxeboot&quot;</tt> program to convert the ISO created above to a PXE boot image. </p>
<pre>
 sudo livecd-iso-to-pxeboot livecd-p2v.iso
</pre>
<p> This creates a <tt>&quot;tftpboot&quot;</tt> subdirectory under the current directory containing the files required to PXE boot virt-p2v: </p>
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
<p> Old virt-p2v 0.9 was always built as a 32 bit (i686) ISO.  This meant that the CD could be booted on any 32- or 64-bit i686 or x86-64 hardware, and could convert any guest. The old virt-p2v ISO shipped by Red Hat was based on Red Hat Enterprise Linux (RHEL) 6. </p>
<p> Since RHEL 7 dropped support for 32 bit machines, current virt-p2v on RHEL can only be built for 64 bit. It cannot run on old 32 bit only hardware. </p>
<p> Fedora virt-p2v ISOs are generally built for 32 bit, so like the old RHEL 6-based virt-p2v 0.9 they can boot on any hardware.</p>
<h2>TESTING VIRT-P2V USING QEMU</h2>
<h3>TESTING THE P2V ISO USING QEMU</h3>
<p> You can use qemu to test-boot the P2V ISO: </p>
<pre>
 qemu-kvm -m 1024 -hda /tmp/guest.img -cdrom /tmp/livecd-p2v.iso -boot d
</pre>
<p> Note that <tt>&quot;-hda&quot;</tt> is the (virtual) system that you want to convert (for test purposes). It could be any guest type supported by <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1), including Windows or Red Hat Enterprise Linux.</p>
<h3>TESTING PXE SUPPORT USING QEMU</h3>
<dl>
<dt>&bull;</dt>
<dd> Unpack the tftpboot directory into <i>/tmp</i> (so it appears as <i>/tmp/tftpboot</i>).</dd>
<dt>&bull;</dt>
<dd> Copy <i>pxelinux.0</i> and <i>ldlinux.c32</i> from syslinux (usually from <i>/usr/share/syslinux</i>) into <i>/tmp/tftpboot</i>.</dd>
<dt>&bull;</dt>
<dd> Adjust the <tt>&quot;APPEND&quot;</tt> line in <i>/tmp/tftpboot/pxelinux.cfg/default</i> if required. See &#8220;KERNEL COMMAND LINE CONFIGURATION&#8221; in <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1).</dd>
<dt>&bull;</dt>
<dd> Run qemu like this so that it acts as a TFTP and BOOTP server, emulating a netboot: </dd>
<pre>
 qemu-kvm \
     -m 4096 -hda /tmp/guest.img \
     -boot n \
     -netdev user,id=unet,tftp=/tmp/tftpboot,bootfile=/pxelinux.0 \
     -device virtio-net-pci,netdev=unet \
     -serial stdio
</pre>
<p> Note that this requires considerably more memory because the PXE image is loaded into memory. Also that qemu&#8217;s TFTP server is very slow and the virt-p2v PXE image is very large, so it can appear to &#8220;hang&#8221; after pxelinux starts up.</dl>
<h2>ADDING EXTRA PACKAGES</h2>
<p> You can install extra packages using the <i>&#8211;install</i> option. This can be useful for making a more fully-featured virt-p2v disk with extra tools for debugging and troubleshooting. Give a list of packages, separated by commas. For example: </p>
<pre>
 virt-p2v-make-kickstart [...] --install tcpdump,traceroute
</pre>
<h2>ADDING AN SSH IDENTITY</h2>
<p> You can inject an SSH identity (private key) file to the kickstart and hence into the ISO using the <i>&#8211;inject-ssh-identity</i> option. Note that you <i>cannot</i> inject a key once the ISO has been built. </p>
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
<p> The ISO can then be built from the kickstart in the usual way (see above), and it will contain the embedded SSH identity (<i>/var/tmp/id_rsa</i>). </p>
<p> When booting virt-p2v, specify the URL of the injected file like this: </p>
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
<p> For more information, see &#8220;SSH IDENTITIES&#8221; in <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Display help.</dd>
<dt><code>&#8211;inject-ssh-identity</code> id_rsa</dt>
<dd> Add an SSH identity (private key) file into the kickstart. See &#8220;ADDING AN SSH IDENTITY&#8221; above.</dd>
<dt><code>&#8211;install</code> pkg,pkg,&#8230;</dt>
<dd> Add extra packages to the kickstart <tt>%packages</tt> section. See &#8220;ADDING EXTRA PACKAGES&#8221; above.</dd>
<dt><code>-o</code> OUTPUT</dt>
<dd>
</dd><dt><code>&#8211;output</code> OUTPUT</dt>
<dd> Write kickstart to <tt>&quot;OUTPUT&quot;</tt>. If not specified, the default is <i>p2v.ks</i> in the current directory.</dd>
<dt><code>&#8211;proxy</code> URL</dt>
<dd> Tell the kickstart to use a proxy server or web cache for downloads.</dd>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>&#8211;verbose</code></dt>
<dd> Enable verbose output. Use this if you need to debug problems with the script or if you are filing a bug.</dd>
<dt><code>-V</code></dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd> Display version number and exit.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>$libexecdir/virt-p2v</i></dt>
<dd> The <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1) binary which is copied into the kickstart file. </dd>
<p> The location of the binary can be changed by setting the <tt>&quot;VIRT_P2V_DATA_DIR&quot;</tt> environment variable.</p>
<dt><i>$datadir/virt-p2v/issue</i></dt>
<dd>
</dd><dt><i>$datadir/virt-p2v/launch-virt-p2v.in</i></dt>
<dd>
</dd><dt><i>$datadir/virt-p2v/p2v.ks.in</i></dt>
<dd>
</dd><dt><i>$datadir/virt-p2v/p2v.service</i></dt>
<dd> Various data files that are used to make the kickstart. </dd>
<p> The location of these files can be changed by setting the <tt>&quot;VIRT_P2V_DATA_DIR&quot;</tt> environment variable.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>&quot;VIRT_P2V_DATA_DIR&quot;</dt>
<dd> The directory where virt-p2v-make-kickstart looks for data files and the virt-p2v binary (see &#8220;FILES&#8221; above). If not set, a compiled-in location is used.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1), <i><a href="/docs/linux/man/1-virt-p2v-make-disk/">virt-p2v-make-disk</a></i>(1), <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1), <i><a href="/docs/linux/man/8-livecd-creator/">livecd-creator</a></i>(8), <i><a href="/docs/linux/man/8-livecd-iso-to-disk/">livecd-iso-to-disk</a></i>(8), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2016 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.</p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</dt>
<dd> The version of libguestfs.</dd>
<dt>&bull;</dt>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</dd>
<dt>&bull;</dt>
<dd> Describe the bug accurately and give a way to reproduce it.</dd>
<dt>&bull;</dt>
<dd> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </dd>
</dl>
