---
title: "guestfs-faq(1)"
name: "guestfs-faq"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guestfs-faq/"
description: "guestfs-faq – libguestfs Frequently Asked Questions (FAQ)"
---

<h2 class="name">NAME</h2>
<p> guestfs-faq &#8211; libguestfs Frequently Asked Questions (FAQ) </p>
<h2>ABOUT LIBGUESTFS</h2>
<h3>What is libguestfs?</h3>
<p> libguestfs is a way to create, access and modify disk images. You can look inside disk images, modify the files they contain, create them from scratch, resize them, and much more. It’s especially useful from scripts and programs and from the command line. </p>
<p> libguestfs is a C library (hence &#8220;lib-&#8221;), and a set of tools built on this library, and bindings for many common programming languages. </p>
<p> For more information about what libguestfs can do read the introduction on the home page (<a rel="nofollow" href="http://libguestfs.org">http://libguestfs.org</a>).</p>
<h3>What are the virt tools?</h3>
<p> Virt tools (website: <a rel="nofollow" href="http://virt-tools.org)">http://virt-tools.org)</a> are a whole set of virtualization management tools aimed at system administrators. Some of them come from libguestfs, some from libvirt and many others from other open source projects. So virt tools is a superset of libguestfs. However libguestfs comes with many important tools. See <a rel="nofollow" href="http://libguestfs.org">http://libguestfs.org</a> for a full list.</p>
<h3>Does libguestfs need { libvirt / <font SIZE="-1">KVM /</font> Red Hat / Fedora }?</h3>
<p> No! </p>
<p> libvirt is not a requirement for libguestfs. </p>
<p> libguestfs works with any disk image, including ones created in VMware, <font SIZE="-1">KVM,</font> qemu, VirtualBox, Xen, and many other hypervisors, and ones which you have created from scratch. </p>
<p> Red Hat sponsors (ie. pays for) development of libguestfs and a huge number of other open source projects. But you can run libguestfs and the virt tools on many different Linux distros and Mac <font SIZE="-1">OS X.</font> We try our best to support all Linux distros as first-class citizens. Some virt tools have been ported to Windows.</p>
<h3>How does libguestfs compare to other tools?</h3>
<dl>
<dt><i>vs. kpartx</i></p>
<dd> Libguestfs takes a different approach from kpartx. kpartx needs root, and mounts filesystems on the host kernel (which can be insecure &#8211; see <code><a href="/docs/linux/man/1-guestfs-security/">guestfs-security</a></code>(1)). Libguestfs isolates your host kernel from guests, is more flexible, scriptable, supports <font SIZE="-1">LVM,</font> doesn&#8217;t require root, is isolated from other processes, and cleans up after itself. Libguestfs is more than just file access because you can use it to create images from scratch.</p>
<dt><i>vs. vdfuse</i></p>
<dd> vdfuse is like kpartx but for VirtualBox images. See the kpartx comparison above. You can use libguestfs on the partition files exposed by vdfuse, although it’s not necessary since libguestfs can access VirtualBox images directly.</p>
<dt><i>vs. qemu-nbd</i></p>
<dd> <font SIZE="-1">NBD</font> (Network Block Device) is a protocol for exporting block devices over the network. qemu-nbd is an <font SIZE="-1">NBD</font> server which can handle any disk format supported by qemu (eg. raw, qcow2). You can use libguestfs and qemu-nbd or nbdkit together to access block devices over the network, for example: <tt>&quot;guestfish -a <a href="nbd://remote">nbd://remote</a>&quot;</tt></p>
<dt><i>vs. mounting filesystems in the host</i></p>
<dd> Mounting guest filesystems in the host is insecure and should be avoided completely for untrusted guests. Use libguestfs to provide a layer of protection against filesystem exploits. See also <code><a href="/docs/linux/man/1-guestmount/">guestmount</a></code>(1).</p>
<dt><i>vs. parted</i></p>
<dd> Libguestfs supports <font SIZE="-1">LVM.</font> Libguestfs uses parted and provides most parted features through the libguestfs <font SIZE="-1">API.</font></dl>
<h2>GETTING HELP AND REPORTING BUGS</h2>
<h3>How do I know what version I&#8217;m using?</h3>
<p> The simplest method is: </p>
<pre>
 guestfish --version
</pre>
<p> Libguestfs development happens along an unstable branch and we periodically create a stable branch which we backport stable patches to. To find out more, read &#8220;<font SIZE="-1">LIBGUESTFS VERSION NUMBERS&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3).</p>
<h3>How can I get help?</h3>
<h3>What mailing lists or chat rooms are available?</h3>
<p> If you are a Red Hat customer using Red Hat Enterprise Linux, please contact Red Hat Support: <a rel="nofollow" href="http://redhat.com/support">http://redhat.com/support</a> </p>
<p> There is a mailing list, mainly for development, but users are also welcome to ask questions about libguestfs and the virt tools: <a rel="nofollow" href="https://www.redhat.com/mailman/listinfo/libguestfs">https://www.redhat.com/mailman/listinfo/libguestfs</a> </p>
<p> You can also talk to us on <font SIZE="-1">IRC</font> channel <tt>&quot;#libguestfs&quot;</tt> on FreeNode. We&#8217;re not always around, so please stay in the channel after asking your question and someone will get back to you. </p>
<p> For other virt tools (not ones supplied with libguestfs) there is a general virt tools mailing list: <a rel="nofollow" href="https://www.redhat.com/mailman/listinfo/virt-tools-list">https://www.redhat.com/mailman/listinfo/virt-tools-list</a></p>
<h3>How do I report bugs?</h3>
<p> Please use the following link to enter a bug in Bugzilla: </p>
<p> <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> Include as much detail as you can and a way to reproduce the problem. </p>
<p> Include the full output of <code><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></code>(1).</p>
<h2>COMMON PROBLEMS</h2>
<p> See also &#8220;<font SIZE="-1">LIBGUESTFS GOTCHAS&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) for some &#8220;gotchas&#8221; with using the libguestfs <font SIZE="-1">API.</font></p>
<h3>Could not allocate dynamic translator buffer</h3>
<p> This obscure error is in fact an SELinux failure. You have to enable the following SELinux boolean: </p>
<pre>
 setsebool -P virt_use_execmem=on
</pre>
<p> For more information see <a rel="nofollow" href="https://bugzilla.redhat.com/show_bug.cgi?id=806106.">https://bugzilla.redhat.com/show_bug.cgi?id=806106.</a></p>
<h3>child process died unexpectedly</h3>
<p> [This error message was changed in libguestfs 1.21.18 to something more explanatory.] </p>
<p> This error indicates that qemu failed or the host kernel could not boot. To get further information about the failure, you have to run: </p>
<pre>
 libguestfs-test-tool
</pre>
<p> If, after using this, you still don’t understand the failure, contact us (see previous section).</p>
<h3>libguestfs: error: cannot find any suitable libguestfs supermin, fixed or old-style appliance on <font SIZE="-1">LIBGUESTFS_PATH</font></h3>
<h3>febootstrap-supermin-helper: ext2: parent directory not found</h3>
<h3>supermin-helper: ext2: parent directory not found</h3>
<p> [This issue is fixed permanently in libguestfs ≥ 1.26.] </p>
<p> If you see any of these errors on Debian/Ubuntu, you need to run the following command: </p>
<pre>
 sudo update-guestfs-appliance
</pre>
<h3>Permission denied when running libguestfs as root</h3>
<p> You get a permission denied error when opening a disk image, even though you are running libguestfs as root. </p>
<p> This is caused by libvirt, and so only happens when using the libvirt backend. When run as root, libvirt decides to run the qemu appliance as user <tt>&quot;qemu.qemu&quot;</tt>. Unfortunately this usually means that qemu cannot open disk images, especially if those disk images are owned by root, or are present in directories which require root access. </p>
<p> There is a bug open against libvirt to fix this: <a rel="nofollow" href="https://bugzilla.redhat.com/show_bug.cgi?id=1045069">https://bugzilla.redhat.com/show_bug.cgi?id=1045069</a> </p>
<p> You can work around this by one of the following methods:</p>
<dl>
<dt>&bull;</p>
<dd> Switch to the direct backend: </p>
<pre>
 export LIBGUESTFS_BACKEND=direct
</pre>
<dt>&bull;</p>
<dd> Don’t run libguestfs as root.</p>
<dt>&bull;</p>
<dd> Chmod the disk image and any parent directories so that the qemu user can access them.</p>
<dt>&bull;</p>
<dd> (Nasty) Edit <i>/etc/libvirt/qemu.conf</i> and change the <tt>&quot;user&quot;</tt> setting.</dl>
<h3>execl: /init: Permission denied</h3>
<p> <code>Note:</code> If this error happens when you are using a distro package of libguestfs (eg. from Fedora, Debian, etc) then file a bug against the distro. This is not an error which normal users should ever see if the distro package has been prepared correctly. </p>
<p> This error happens during the supermin boot phase of starting the appliance: </p>
<pre>
 supermin: mounting new root on /root
 supermin: chroot
 execl: /init: Permission denied
 supermin: debug: listing directory /
 [...followed by a lot of debug output...]
</pre>
<p> This is a complicated bug related to <code><a href="/docs/linux/man/1-supermin/">supermin</a></code>(1) appliances. The appliance is constructed by copying files like <i>/bin/bash</i> and many libraries from the host. The file <tt>&quot;hostfiles&quot;</tt> lists the files that should be copied from the host into the appliance. If some files don&#8217;t exist on the host then they are missed out, but if these files are needed in order to (eg) run <i>/bin/bash</i> then you&#8217;ll see the above error. </p>
<p> Diagnosing the problem involves studying the libraries needed by <i>/bin/bash</i>, ie: </p>
<pre>
 ldd /bin/bash
</pre>
<p> comparing that with <tt>&quot;hostfiles&quot;</tt>, with the files actually available in the host filesystem, and with the debug output printed in the error message. Once you&#8217;ve worked out which file is missing, install that file using your package manager and try again. </p>
<p> You should also check that files like <i>/init</i> and <i>/bin/bash</i> (in the appliance) are executable. The debug output shows file modes.</p>
<h2>DOWNLOADING, INSTALLING, COMPILING LIBGUESTFS</h2>
<h3>Where can I get the latest binaries for &#8230;?</h3>
<dl>
<dt>Fedora ≥ 11</p>
<dd> Use: </p>
<pre>
 yum install '*guestf*'
</pre>
<p> For the latest builds, see: <a rel="nofollow" href="http://koji.fedoraproject.org/koji/packageinfo?packageID=8391">http://koji.fedoraproject.org/koji/packageinfo?packageID=8391</a></p>
<dt>Red Hat Enterprise Linux</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1">RHEL 5</font></p>
<dd> The version shipped in official <font SIZE="-1">RHEL 5</font> is very old and should not be used except in conjunction with virt-v2v. Use the up-to-date libguestfs 1.20 package in <font SIZE="-1">EPEL 5:</font> <a rel="nofollow" href="https://fedoraproject.org/wiki/EPEL">https://fedoraproject.org/wiki/EPEL</a></p>
<dt><font SIZE="-1">RHEL 6</font></p>
<dd>
<dt><font SIZE="-1">RHEL 7</font></p>
<dd> It is part of the default install. On <font SIZE="-1">RHEL 6</font> and 7 (only) you have to install <tt>&quot;libguestfs-winsupport&quot;</tt> to get Windows guest support.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Debian and Ubuntu</p>
<dd> For libguestfs &lt; 1.26, after installing libguestfs you need to do: </p>
<pre>
 sudo update-guestfs-appliance
</pre>
<p> (This script has been removed on Debian/Ubuntu with libguestfs ≥ 1.26 and instead the appliance is built on demand.) </p>
<p> On Ubuntu only: </p>
<pre>
 sudo chmod 0644 /boot/vmlinuz*
</pre>
<p> You may need to add yourself to the <tt>&quot;kvm&quot;</tt> group: </p>
<pre>
 sudo usermod -a -G kvm yourlogin
</pre>
<dl>
<dt>
<dd>
<dl>
<dt>Debian Squeeze (6)</p>
<dd> Hilko Bengen has built libguestfs in squeeze backports: <a rel="nofollow" href="http://packages.debian.org/search?keywords=guestfs">http://packages.debian.org/search?keywords=guestfs</a>&amp;searchon=names&amp;section=all&amp;suite=squeeze-backports</p>
<dt>Debian Wheezy and later (7+)</p>
<dd> Hilko Bengen supports libguestfs on Debian. Official Debian packages are available: <a rel="nofollow" href="http://packages.debian.org/search?keywords=libguestfs">http://packages.debian.org/search?keywords=libguestfs</a></p>
<dt>Ubuntu</p>
<dd> We don’t have a full time Ubuntu maintainer, and the packages supplied by Canonical (which are outside our control) are sometimes broken. </p>
<p> Canonical decided to change the permissions on the kernel so that it&#8217;s not readable except by root. This is completely stupid, but they won&#8217;t change it (<a rel="nofollow" href="https://bugs.launchpad.net/ubuntu/+source/linux/+bug/759725">https://bugs.launchpad.net/ubuntu/+source/linux/+bug/759725</a>). So every user should do this: </p>
<pre>
 sudo chmod 0644 /boot/vmlinuz*
</pre>
<dl>
<dt>
<dd>
<dl>
<dt>Ubuntu 12.04</p>
<dd> libguestfs in this version of Ubuntu works, but you need to update febootstrap and seabios to the latest versions. </p>
<p> You need febootstrap ≥ 3.14-2 from: <a rel="nofollow" href="http://packages.ubuntu.com/precise/febootstrap">http://packages.ubuntu.com/precise/febootstrap</a> </p>
<p> After installing or updating febootstrap, rebuild the appliance: </p>
<pre>
 sudo update-guestfs-appliance
</pre>
<p> You need seabios ≥ 0.6.2-0ubuntu2.1 or ≥ 0.6.2-0ubuntu3 from: <a rel="nofollow" href="http://packages.ubuntu.com/precise-updates/seabios">http://packages.ubuntu.com/precise-updates/seabios</a> or <a rel="nofollow" href="http://packages.ubuntu.com/quantal/seabios">http://packages.ubuntu.com/quantal/seabios</a> </p>
<p> Also you need to do (see above): </p>
<pre>
 sudo chmod 0644 /boot/vmlinuz*
</pre>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Gentoo</p>
<dd> Libguestfs was added to Gentoo in 2012-07 by Andreis Vinogradovs (libguestfs) and Maxim Koltsov (mainly hivex). Do: </p>
<pre>
 emerge libguestfs
</pre>
<dt>SuSE</p>
<dd> Libguestfs was added to SuSE in 2012 by Olaf Hering.</p>
<dt>ArchLinux</p>
<dd> Libguestfs was added to the <font SIZE="-1">AUR</font> in 2010.</p>
<dt>Other Linux distro</p>
<dd> Compile from source (next section).</p>
<dt>Other non-Linux distro</p>
<dd> You&#8217;ll have to compile from source, and port it.</dl>
<h3>How can I compile and install libguestfs from source?</h3>
<p> You can compile libguestfs from git or a source tarball. Read the <font SIZE="-1">README</font> file before starting. </p>
<p> Git: <a rel="nofollow" href="https://github.com/libguestfs/libguestfs">https://github.com/libguestfs/libguestfs</a> Source tarballs: <a rel="nofollow" href="http://libguestfs.org/download">http://libguestfs.org/download</a> </p>
<p> Don’t run <tt>&quot;make install&quot;</tt>! Use the <tt>&quot;./run&quot;</tt> script instead (see <font SIZE="-1">README</font>).</p>
<h3>How can I compile and install libguestfs if my distro doesn&#8217;t have new enough qemu/supermin/kernel?</h3>
<p> Libguestfs needs supermin 5. If supermin 5 hasn&#8217;t been ported to your distro, then see the question below. </p>
<p> First compile qemu, supermin and/or the kernel from source. You do <i>not</i> need to <tt>&quot;make install&quot;</tt> them. </p>
<p> In the libguestfs source directory, create two files. <tt>&quot;localconfigure&quot;</tt> should contain: </p>
<pre>
 source localenv
 #export PATH=/tmp/qemu/x86_64-softmmu:$PATH
 ./autogen.sh --prefix /usr &quot;$@&quot;
</pre>
<p> Make <tt>&quot;localconfigure&quot;</tt> executable. </p>
<p> <tt>&quot;localenv&quot;</tt> should contain: </p>
<pre>
 #export SUPERMIN=/tmp/supermin/src/supermin
 #export LIBGUESTFS_HV=/tmp/qemu/x86_64-softmmu/qemu-system-x86_64
 #export SUPERMIN_KERNEL=/tmp/linux/arch/x86/boot/bzImage
 #export SUPERMIN_KERNEL_VERSION=4.XX.0
 #export SUPERMIN_MODULES=/tmp/lib/modules/4.XX.0
</pre>
<p> Uncomment and adjust these lines as required to use the alternate programs you have compiled. </p>
<p> Use <tt>&quot;./localconfigure&quot;</tt> instead of <tt>&quot;./configure&quot;</tt>, but otherwise you compile libguestfs as usual. </p>
<p> Don’t run <tt>&quot;make install&quot;</tt>! Use the <tt>&quot;./run&quot;</tt> script instead (see <font SIZE="-1">README</font>).</p>
<h3>How can I compile and install libguestfs without supermin?</h3>
<p> If supermin 5 supports your distro, but you don’t happen to have a new enough supermin installed, then see the previous question. </p>
<p> If supermin 5 doesn&#8217;t support your distro at all, you will need to use the &#8220;fixed appliance method&#8221; where you use a pre-compiled binary appliance. To build libguestfs without supermin, you need to pass <tt>&quot;--disable-appliance --disable-daemon&quot;</tt> to either <i>./autogen.sh</i> or <i>./configure</i> (depending whether you are building respectively from git or from tarballs). Then, when using libguestfs, you <code>must</code> set the <tt>&quot;LIBGUESTFS_PATH&quot;</tt> environment variable to the directory of a pre-compiled appliance, as also described in &#8220;<font SIZE="-1">FIXED APPLIANCE&#8221;</font> in <code><a href="/docs/linux/man/1-guestfs-internals/">guestfs-internals</a></code>(1). </p>
<p> For pre-compiled appliances, see also: <a rel="nofollow" href="http://libguestfs.org/download/binaries/appliance/.">http://libguestfs.org/download/binaries/appliance/.</a> </p>
<p> Patches to port supermin to more Linux distros are welcome.</p>
<h3>How can I add support for sVirt?</h3>
<p> <code>Note for Fedora/RHEL users:</code> This configuration is the default starting with Fedora 18 and <font SIZE="-1">RHEL 7.</font> If you find any problems, please let us know or file a bug. </p>
<p> SVirt provides a hardened appliance using SELinux, making it very hard for a rogue disk image to &#8220;escape&#8221; from the confinement of libguestfs and damage the host (it&#8217;s fair to say that even in standard libguestfs this would be hard, but sVirt provides an extra layer of protection for the host and more importantly protects virtual machines on the same host from each other). </p>
<p> Currently to enable sVirt you will need libvirt ≥ 0.10.2 (1.0 or later preferred), libguestfs ≥ 1.20, and the SELinux policies from recent Fedora. If you are not running Fedora 18+, you will need to make changes to your SELinux policy &#8211; contact us on the mailing list. </p>
<p> Once you have the requirements, do: </p>
<pre><code>
./ configure-- with - default - backend = libvirt #libguestfs &gt;= 1.22
                                                                             ./
                                                                         configure-- with -
                                                                     default - attach - method = libvirt #libguestfs &lt;= 1.20 make
</code></pre>
<p> Set SELinux to Enforcing mode, and sVirt should be used automatically. </p>
<p> All, or almost all, features of libguestfs should work under sVirt. There is one known shortcoming: <code><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></code>(1) will not use libvirt (hence sVirt), but falls back to direct launch of qemu. So you won&#8217;t currently get the benefit of sVirt protection when using virt-rescue. </p>
<p> You can check if sVirt is being used by enabling libvirtd logging (see <i>/etc/libvirt/libvirtd.log</i>), killing and restarting libvirtd, and checking the log files for &#8220;Setting SELinux context on &#8230;&#8221; messages. </p>
<p> In theory sVirt should support AppArmor, but we have not tried it. It will almost certainly require patching libvirt and writing an AppArmor policy.</p>
<h3>Libguestfs has a really long list of dependencies!</h3>
<p> The base library doesn&#8217;t depend on very much, but there are three causes of the long list of other dependencies:</p>
<dl>
<dt>1.</p>
<dd> Libguestfs has to be able to read and edit many different disk formats. For example, <font SIZE="-1">XFS</font> support requires <font SIZE="-1">XFS</font> tools.</p>
<dt>2.</p>
<dd> There are language bindings for many different languages, all requiring their own development tools. All language bindings (except C) are optional.</p>
<dt>3.</p>
<dd> There are some optional library features which can be disabled.</dl>
<p> Since libguestfs ≥ 1.26 it is possible to split up the appliance dependencies (item 1 in the list above) and thus have (eg) <tt>&quot;libguestfs-xfs&quot;</tt> as a separate subpackage for processing <font SIZE="-1">XFS</font> disk images. We encourage downstream packagers to start splitting the base libguestfs package into smaller subpackages.</p>
<h3>Errors during launch on Fedora ≥ 18, <font SIZE="-1">RHEL</font> ≥ 7</h3>
<p> In Fedora ≥ 18 and <font SIZE="-1">RHEL</font> ≥ 7, libguestfs uses libvirt to manage the appliance. Previously (and upstream) libguestfs runs qemu directly: </p>
<pre>
 ┌──────────────────────────────────┐
 │ libguestfs                       │
 ├────────────────┬─────────────────┤
 │ direct backend │ libvirt backend │
 └────────────────┴─────────────────┘
        ↓                  ↓
    ┌───────┐         ┌──────────┐
    │ qemu  │         │ libvirtd │
    └───────┘         └──────────┘
                           ↓
                       ┌───────┐
                       │ qemu  │
                       └───────┘
 
    upstream          Fedora 18+
    non-Fedora         RHEL 7+
    non-RHEL
</pre>
<p> The libvirt backend is more sophisticated, supporting SELinux/sVirt (see above), hotplugging and more. It is, however, more complex and so less robust. </p>
<p> If you have permissions problems using the libvirt backend, you can switch to the direct backend by setting this environment variable: </p>
<pre>
 export LIBGUESTFS_BACKEND=direct
</pre>
<p> before running any libguestfs program or virt tool.</p>
<h3>How can I switch to a fixed / prebuilt appliance?</h3>
<p> This may improve the stability and performance of libguestfs on Fedora and <font SIZE="-1">RHEL.</font> </p>
<p> Any time after installing libguestfs, run the following commands as root: </p>
<pre>
 mkdir -p /usr/local/lib/guestfs/appliance
 libguestfs-make-fixed-appliance /usr/local/lib/guestfs/appliance
 ls -l /usr/local/lib/guestfs/appliance
</pre>
<p> Now set the following environment variable before using libguestfs or any virt tool: </p>
<pre>
 export LIBGUESTFS_PATH=/usr/local/lib/guestfs/appliance
</pre>
<p> Of course you can change the path to any directory you want. You can share the appliance across machines that have the same architecture (eg. all x86-64), but note that libvirt will prevent you from sharing the appliance across <font SIZE="-1">NFS</font> because of permissions problems (so either switch to the direct backend or don&#8217;t use <font SIZE="-1">NFS</font>).</p>
<h3>How can I speed up libguestfs builds?</h3>
<p> By far the most important thing you can do is to install and properly configure Squid. Note that the default configuration that ships with Squid is rubbish, so configuring it is not optional. </p>
<p> A very good place to start with Squid configuration is here: <a rel="nofollow" href="https://fedoraproject.org/wiki/Extras/MockTricks#Using_Squid_to_Speed_Up_Mock_package_downloads">https://fedoraproject.org/wiki/Extras/MockTricks#Using_Squid_to_Speed_Up_Mock_package_downloads</a> </p>
<p> Make sure Squid is running, and that the environment variables <tt>$http_proxy</tt> and <tt>$ftp_proxy</tt> are pointing to it. </p>
<p> With Squid running and correctly configured, appliance builds should be reduced to a few minutes. </p>
<p> <i>How can I speed up libguestfs builds (Debian)?</i> </p>
<p> Hilko Bengen suggests using &#8220;approx&#8221; which is a Debian archive proxy (<a rel="nofollow" href="http://packages.debian.org/approx">http://packages.debian.org/approx</a>). This tool is documented on Debian in the <code><a href="/docs/linux/man/8-approx/">approx</a></code>(8) manual page.</p>
<h2>SPEED, DISK SPACE USED BY LIBGUESTFS</h2>
<p> <code>Note:</code> Most of the information in this section has moved: <code><a href="/docs/linux/man/1-guestfs-performance/">guestfs-performance</a></code>(1).</p>
<h3>Upload or write seem very slow.</h3>
<p> If the underlying disk is not fully allocated (eg. sparse raw or qcow2) then writes can be slow because the host operating system has to do costly disk allocations while you are writing. The solution is to use a fully allocated format instead, ie. non-sparse raw, or qcow2 with the <tt>&quot;preallocation=metadata&quot;</tt> option.</p>
<h3>Libguestfs uses too much disk space!</h3>
<p> libguestfs caches a large-ish appliance in: </p>
<pre>
 /var/tmp/.guestfs-&lt;UID&gt;
</pre>
<p> If the environment variable <tt>&quot;TMPDIR&quot;</tt> is defined, then <i></i>$TMPDIR<i>/.guestfs-&lt;</i><font SIZE="-1"><i>UID</i></font><i>&gt;</i> is used instead. </p>
<p> It is safe to delete this directory when you are not using libguestfs.</p>
<h3>virt-sparsify seems to make the image grow to the full size of the virtual disk</h3>
<p> If the input to <code><a href="/docs/linux/man/1-virt-sparsify/">virt-sparsify</a></code>(1) is raw, then the output will be raw sparse. Make sure you are measuring the output with a tool which understands sparseness such as <tt>&quot;du -sh&quot;</tt>. It can make a huge difference: </p>
<pre>
 $ ls -lh test1.img
 -rw-rw-r--. 1 rjones rjones 100M Aug  8 08:08 test1.img
 $ du -sh test1.img
 3.6M   test1.img
</pre>
<p> (Compare the apparent size <code>100M</code> vs the actual size <code>3.6M</code>) </p>
<p> If all this confuses you, use a non-sparse output format by specifying the <i>&#8211;convert</i> option, eg: </p>
<pre>
 virt-sparsify --convert qcow2 disk.raw disk.qcow2
</pre>
<h3>Why doesn&#8217;t virt-resize work on the disk image in-place?</h3>
<p> Resizing a disk image is very tricky &#8212; especially making sure that you don&#8217;t lose data or break the bootloader. The current method effectively creates a new disk image and copies the data plus bootloader from the old one. If something goes wrong, you can always go back to the original. </p>
<p> If we were to make virt-resize work in-place then there would have to be limitations: for example, you wouldn&#8217;t be allowed to move existing partitions (because moving data across the same disk is most likely to corrupt data in the event of a power failure or crash), and <font SIZE="-1">LVM</font> would be very difficult to support (because of the almost arbitrary mapping between <font SIZE="-1">LV</font> content and underlying disk blocks). </p>
<p> Another method we have considered is to place a snapshot over the original disk image, so that the original data is untouched and only differences are recorded in the snapshot. You can do this today using <tt>&quot;qemu-img create&quot;</tt> + <tt>&quot;virt-resize&quot;</tt>, but qemu currently isn&#8217;t smart enough to recognize when the same block is written back to the snapshot as already exists in the backing disk, so you will find that this doesn&#8217;t save you any space or time. </p>
<p> In summary, this is a hard problem, and what we have now mostly works so we are reluctant to change it.</p>
<h3>Why doesn&#8217;t virt-sparsify work on the disk image in-place?</h3>
<p> In libguestfs ≥ 1.26, virt-sparsify can now work on disk images in place. Use: </p>
<pre>
 virt-sparsify --in-place disk.img
</pre>
<p> But first you should read &#8220;IN-PLACE <font SIZE="-1">SPARSIFICATION&#8221;</font> in <code><a href="/docs/linux/man/1-virt-sparsify/">virt-sparsify</a></code>(1).</p>
<h2>PROBLEMS OPENING DISK IMAGES</h2>
<h3>Remote libvirt guests cannot be opened.</h3>
<p> Opening remote libvirt guests is not supported at this time. For example this won&#8217;t work: </p>
<pre>
 guestfish -c <a href="qemu://remote/system">qemu://remote/system</a> -d Guest
</pre>
<p> To open remote disks you have to export them somehow, then connect to the export. For example if you decided to use <font SIZE="-1">NBD:</font> </p>
<pre>
 remote$ qemu-nbd -t -p 10809 guest.img
  local$ guestfish -a <a href="nbd://remote:10809">nbd://remote:10809</a> -i
</pre>
<p> Other possibilities include ssh (if qemu is recent enough), <font SIZE="-1">NFS</font> or iSCSI. See &#8220;<font SIZE="-1">REMOTE STORAGE&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3).</p>
<h3>How can I open this strange disk source?</h3>
<p> You have a disk image located inside another system that requires access via a library / <font SIZE="-1">HTTP / REST /</font> proprietary <font SIZE="-1">API,</font> or is compressed or archived in some way. (One example would be remote access to OpenStack glance images without actually downloading them.) </p>
<p> We have a sister project called nbdkit (<a rel="nofollow" href="https://github.com/libguestfs/nbdkit">https://github.com/libguestfs/nbdkit</a>). This project lets you turn any disk source into an <font SIZE="-1">NBD</font> server. Libguestfs can access <font SIZE="-1">NBD</font> servers directly, eg: </p>
<pre>
 guestfish -a <a href="nbd://remote">nbd://remote</a>
</pre>
<p> nbdkit is liberally licensed, so you can link it to or include it in proprietary libraries and code. It also has a simple, stable plugin <font SIZE="-1">API</font> so you can easily write plugins against the <font SIZE="-1">API</font> which will continue to work in future.</p>
<h3>Error opening <font SIZE="-1">VMDK</font> disks: uses a vmdk feature which is not supported by this qemu version: <font SIZE="-1">VMDK</font> version 3</h3>
<p> Qemu (and hence libguestfs) only supports certain <font SIZE="-1">VMDK</font> disk images. Others won&#8217;t work, giving this or similar errors. </p>
<p> Ideally someone would fix qemu to support the latest <font SIZE="-1">VMDK</font> features, but in the meantime you have three options:</p>
<dl>
<dt>1.</p>
<dd> If the guest is hosted on a live, reachable <font SIZE="-1">ESX</font> server, then locate and download the disk image called <i>somename-flat.vmdk</i>. Despite the name, this is a raw disk image, and can be opened by anything. </p>
<p> If you have a recent enough version of qemu and libguestfs, then you may be able to access this disk image remotely using either <font SIZE="-1">HTTPS</font> or ssh. See &#8220;<font SIZE="-1">REMOTE STORAGE&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3).</p>
<dt>2.</p>
<dd> Use VMware’s proprietary vdiskmanager tool to convert the image to raw format.</p>
<dt>3.</p>
<dd> Use nbdkit with the proprietary <font SIZE="-1">VDDK</font> plugin to live export the disk image as an <font SIZE="-1">NBD</font> source. This should allow you to read and write the <font SIZE="-1">VMDK</font> file.</dl>
<h3><font SIZE="-1">UFS</font> disks (as used by <font SIZE="-1">BSD</font>) cannot be opened.</h3>
<p> The <font SIZE="-1">UFS</font> filesystem format has many variants, and these are not self-identifying. The Linux kernel has to be told which variant of <font SIZE="-1">UFS</font> it has to use, which libguestfs cannot know. </p>
<p> You have to pass the right <tt>&quot;ufstype&quot;</tt> mount option when mounting these filesystems. </p>
<p> See <a rel="nofollow" href="https://www.kernel.org/doc/Documentation/filesystems/ufs.txt">https://www.kernel.org/doc/Documentation/filesystems/ufs.txt</a></p>
<h3>Windows ReFS</h3>
<p> Windows ReFS is Microsoft’s ZFS/Btrfs copy. This filesystem has not yet been reverse engineered and implemented in the Linux kernel, and therefore libguestfs doesn&#8217;t support it. At the moment it seems to be very rare &#8220;in the wild&#8221;.</p>
<h3>Non-ASCII characters don’t appear on <font SIZE="-1">VFAT</font> filesystems.</h3>
<p> Typical symptoms of this problem:</p>
<dl>
<dt>&bull;</p>
<dd> You get an error when you create a file where the filename contains non-ASCII characters, particularly non 8-bit characters from Asian languages (Chinese, Japanese, etc). The filesystem is <font SIZE="-1">VFAT.</font></p>
<dt>&bull;</p>
<dd> When you list a directory from a <font SIZE="-1">VFAT</font> filesystem, filenames appear as question marks.</dl>
<p> This is a design flaw of the GNU/Linux system. </p>
<p> <font SIZE="-1">VFAT</font> stores long filenames as <font SIZE="-1">UTF-16</font> characters. When opening or returning filenames, the Linux kernel has to translate these to some form of 8 bit string. <font SIZE="-1">UTF-8</font> would be the obvious choice, except for Linux users who persist in using non-UTF-8 locales (the user’s locale is not known to the kernel because it’s a function of libc). </p>
<p> Therefore you have to tell the kernel what translation you want done when you mount the filesystem. The two methods are the <tt>&quot;iocharset&quot;</tt> parameter (which is not relevant to libguestfs) and the <tt>&quot;utf8&quot;</tt> flag. </p>
<p> So to use a <font SIZE="-1">VFAT</font> filesystem you must add the <tt>&quot;utf8&quot;</tt> flag when mounting. From guestfish, use: </p>
<pre>
 &gt;&lt;fs&gt; mount-options utf8 /dev/sda1 /
</pre>
<p> or on the guestfish command line: </p>
<pre>
 guestfish [...] -m /dev/sda1:/:utf8
</pre>
<p> or from the <font SIZE="-1">API:</font> </p>
<pre>
 guestfs_mount_options (g, &quot;utf8&quot;, &quot;/dev/sda1&quot;, &quot;/&quot;);
</pre>
<p> The kernel will then translate filenames to and from <font SIZE="-1">UTF-8</font> strings. </p>
<p> We considered adding this mount option transparently, but unfortunately there are several problems with doing that:</p>
<dl>
<dt>&bull;</p>
<dd> On some Linux systems, the <tt>&quot;utf8&quot;</tt> mount option doesn&#8217;t work. We don&#8217;t precisely understand what systems or why, but this was reliably reported by one user.</p>
<dt>&bull;</p>
<dd> It would prevent you from using the <tt>&quot;iocharset&quot;</tt> parameter because it is incompatible with <tt>&quot;utf8&quot;</tt>. It is probably not a good idea to use this parameter, but we don&#8217;t want to prevent it.</dl>
<h3>Non-ASCII characters appear as underscore (_) on <font SIZE="-1">ISO9660</font> filesystems.</h3>
<p> The filesystem was not prepared correctly with mkisofs or genisoimage. Make sure the filesystem was created using Joliet and/or Rock Ridge extensions. libguestfs does not require any special mount options to handle the filesystem.</p>
<h3>Cannot open Windows guests which use <font SIZE="-1">NTFS.</font></h3>
<p> You see errors like: </p>
<pre>
 mount: unknown filesystem type 'ntfs'
</pre>
<p> On Red Hat Enterprise Linux or CentOS &lt; 7.2, you have to install the libguestfs-winsupport package. In <font SIZE="-1">RHEL</font> ≥ 7.2, <tt>&quot;libguestfs-winsupport&quot;</tt> is part of the base <font SIZE="-1">RHEL</font> distribution, but see the next question.</p>
<h3>mount: unsupported filesystem type with <font SIZE="-1">NTFS</font> in <font SIZE="-1">RHEL</font> ≥ 7.2</h3>
<p> In <font SIZE="-1">RHEL 7.2</font> we were able to add <tt>&quot;libguestfs-winsupport&quot;</tt> to the base <font SIZE="-1">RHEL</font> distribution, but we had to disable the ability to use it for opening and editing filesystems. It is only supported when used with <code><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></code>(1). If you try to use <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1) or <code><a href="/docs/linux/man/1-guestmount/">guestmount</a></code>(1) or some other programs on an <font SIZE="-1">NTFS</font> filesystem, you will see the error: </p>
<pre>
 mount: unsupported filesystem type
</pre>
<p> This is not a supported configuration, and it will not be made to work in <font SIZE="-1">RHEL.</font> Don&#8217;t bother to open a bug about it, as it will be immediately <tt>&quot;CLOSED -&gt; WONTFIX&quot;</tt>. </p>
<p> You may compile your own libguestfs removing this restriction, but that won&#8217;t be endorsed or supported by Red Hat.</p>
<h3>Cannot open or inspect <font SIZE="-1">RHEL 7</font> guests.</h3>
<h3>Cannot open Linux guests which use <font SIZE="-1">XFS.</font></h3>
<p> <font SIZE="-1">RHEL 7</font> guests, and any other guests that use <font SIZE="-1">XFS,</font> can be opened by libguestfs, but you have to install the <tt>&quot;libguestfs-xfs&quot;</tt> package.</p>
<h2>USING LIBGUESTFS IN YOUR OWN PROGRAMS</h2>
<h3>The <font SIZE="-1">API</font> has hundreds of methods, where do I start?</h3>
<p> We recommend you start by reading the <font SIZE="-1">API</font> overview: &#8220;<font SIZE="-1">API OVERVIEW&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3). </p>
<p> Although the <font SIZE="-1">API</font> overview covers the C <font SIZE="-1">API,</font> it is still worth reading even if you are going to use another programming language, because the <font SIZE="-1">API</font> is the same, just with simple logical changes to the names of the calls: </p>
<pre><code>
C guestfs_ln_sf(g, target, linkname);
Python g.ln_sf(target, linkname);
OCaml g #ln_sf target linkname;
Perl $g-&gt;ln_sf(target, linkname);
Shell(guestfish) ln - sf target linkname
    PHP guestfs_ln_sf($g, $target, $linkname);
</code></pre>
<p> Once you&#8217;re familiar with the <font SIZE="-1">API</font> overview, you should look at this list of starting points for other language bindings: &#8220;<font SIZE="-1">USING LIBGUESTFS WITH OTHER PROGRAMMING LANGUAGES&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3).</p>
<h3>Can I use libguestfs in my proprietary / closed source / commercial program?</h3>
<p> In general, yes. However this is not legal advice &#8211; read the license that comes with libguestfs, and if you have specific questions contact a lawyer. </p>
<p> In the source tree the license is in the file <tt>&quot;COPYING.LIB&quot;</tt> (LGPLv2+ for the library and bindings) and <tt>&quot;COPYING&quot;</tt> (GPLv2+ for the standalone programs).</p>
<h2>DEBUGGING LIBGUESTFS</h2>
<h3>Help, it’s not working!</h3>
<p> If no libguestfs program seems to work at all, run the program below and paste the <code>complete, unedited</code> output into an email to <tt>&quot;libguestfs&quot;</tt> @ <tt>&quot;redhat.com&quot;</tt>: </p>
<pre>
 libguestfs-test-tool
</pre>
<p> If a particular operation fails, supply all the information in this checklist, in an email to <tt>&quot;libguestfs&quot;</tt> @ <tt>&quot;redhat.com&quot;</tt>:</p>
<dl>
<dt>1.</p>
<dd> What are you trying to do?</p>
<dt>2.</p>
<dd> What exact command(s) did you run?</p>
<dt>3.</p>
<dd> What was the precise error or output of these commands?</p>
<dt>4.</p>
<dd> Enable debugging, run the commands again, and capture the <code>complete</code> output. <code>Do not edit the output.</code> </p>
<pre>
 export LIBGUESTFS_DEBUG=1
 export LIBGUESTFS_TRACE=1
</pre>
<dt>5.</p>
<dd> Include the version of libguestfs, the operating system version, and how you installed libguestfs (eg. from source, <tt>&quot;yum install&quot;</tt>, etc.)</dl>
<h3>How do I debug when using any libguestfs program or tool (eg. virt-v2v or virt-df)?</h3>
<p> There are two <tt>&quot;LIBGUESTFS_*&quot;</tt> environment variables you can set in order to get more information from libguestfs.</p>
<dl>
<dt>&quot;LIBGUESTFS_TRACE&quot;</p>
<dd> Set this to 1 and libguestfs will print out each command / <font SIZE="-1">API</font> call in a format which is similar to guestfish commands.</p>
<dt>&quot;LIBGUESTFS_DEBUG&quot;</p>
<dd> Set this to 1 in order to enable massive amounts of debug messages. If you think there is some problem inside the libguestfs appliance, then you should use this option.</dl>
<p> To set these from the shell, do this before running the program: </p>
<pre>
 export LIBGUESTFS_TRACE=1
 export LIBGUESTFS_DEBUG=1
</pre>
<p> For csh/tcsh the equivalent commands would be: </p>
<pre>
 setenv LIBGUESTFS_TRACE 1
 setenv LIBGUESTFS_DEBUG 1
</pre>
<p> For further information, see: &#8220;<font SIZE="-1">ENVIRONMENT VARIABLES&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3).</p>
<h3>How do I debug when using guestfish?</h3>
<p> You can use the same environment variables above. Alternatively use the guestfish options -x (to trace commands) or -v (to get the full debug output), or both. </p>
<p> For further information, see: <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1).</p>
<h3>How do I debug when using the <font SIZE="-1">API</font>?</h3>
<p> Call &#8220;guestfs_set_trace&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) to enable command traces, and/or &#8220;guestfs_set_verbose&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) to enable debug messages. </p>
<p> For best results, call these functions as early as possible, just after creating the guestfs handle if you can, and definitely before calling launch.</p>
<h3>How do I capture debug output and put it into my logging system?</h3>
<p> Use the event <font SIZE="-1">API.</font> For examples, see: &#8220;<font SIZE="-1">SETTING CALLBACKS TO HANDLE EVENTS&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) and the <i>examples/debug-logging.c</i> program in the libguestfs sources.</p>
<h3>Digging deeper into the appliance boot process.</h3>
<p> Enable debugging and then read this documentation on the appliance boot process: <code><a href="/docs/linux/man/1-guestfs-internals/">guestfs-internals</a></code>(1).</p>
<h3>libguestfs hangs or fails during run/launch.</h3>
<p> Enable debugging and look at the full output. If you cannot work out what is going on, file a bug report, including the <i>complete</i> output of <code><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></code>(1).</p>
<h3>Debugging libvirt</h3>
<p> If you are using the libvirt backend, and libvirt is failing, then you can enable debugging by editing <i>/etc/libvirt/libvirtd.conf</i>. </p>
<p> If you are running as non-root, then you have to edit a different file. Create <i>~/.config/libvirt/libvirtd.conf</i> containing: </p>
<pre>
 log_level=1
 log_outputs=&quot;1:file:/tmp/libvirtd.log&quot;
</pre>
<p> Kill any session (non-root) libvirtd that is running, and next time you run the libguestfs command, you should see a large amount of useful debugging information from libvirtd in <i>/tmp/libvirtd.log</i></p>
<h3>Broken kernel, or trying a different kernel.</h3>
<p> You can choose a different kernel for the appliance by setting some supermin environment variables: </p>
<pre>
 export SUPERMIN_KERNEL_VERSION=4.8.0-1.fc25.x86_64
 export SUPERMIN_KERNEL=/boot/vmlinuz-$SUPERMIN_KERNEL_VERSION
 export SUPERMIN_MODULES=/lib/modules/$SUPERMIN_KERNEL_VERSION
 rm -rf /var/tmp/.guestfs-*
 libguestfs-test-tool
</pre>
<h3>Broken qemu, or trying a different qemu.</h3>
<p> You can choose a different qemu by setting the hypervisor environment variable: </p>
<pre>
 export LIBGUESTFS_HV=/path/to/qemu-system-x86_64
 libguestfs-test-tool
</pre>
<h2>DESIGN/INTERNALS OF LIBGUESTFS</h2>
<p> See also <code><a href="/docs/linux/man/1-guestfs-internals/">guestfs-internals</a></code>(1).</p>
<h3>Why don’t you do everything through the <font SIZE="-1">FUSE /</font> filesystem interface?</h3>
<p> We offer a command called <code><a href="/docs/linux/man/1-guestmount/">guestmount</a></code>(1) which lets you mount guest filesystems on the host. This is implemented as a <font SIZE="-1">FUSE</font> module. Why don&#8217;t we just implement the whole of libguestfs using this mechanism, instead of having the large and rather complicated <font SIZE="-1">API</font>? </p>
<p> The reasons are twofold. Firstly, libguestfs offers <font SIZE="-1">API</font> calls for doing things like creating and deleting partitions and logical volumes, which don&#8217;t fit into a filesystem model very easily. Or rather, you could fit them in: for example, creating a partition could be mapped to <tt>&quot;mkdir /fs/hda1&quot;</tt> but then you&#8217;d have to specify some method to choose the size of the partition (maybe <tt>&quot;echo 100M &gt; /fs/hda1/.size&quot;</tt>), and the partition type, start and end sectors etc., but once you&#8217;ve done that the filesystem-based <font SIZE="-1">API</font> starts to look more complicated than the call-based <font SIZE="-1">API</font> we currently have. </p>
<p> The second reason is for efficiency. <font SIZE="-1">FUSE</font> itself is reasonably efficient, but it does make lots of small, independent calls into the <font SIZE="-1">FUSE</font> module. In guestmount these have to be translated into messages to the libguestfs appliance which has a big overhead (in time and round trips). For example, reading a file in 64 <font SIZE="-1">KB</font> chunks is inefficient because each chunk would turn into a single round trip. In the libguestfs <font SIZE="-1">API</font> it is much more efficient to download an entire file or directory through one of the streaming calls like <tt>&quot;guestfs_download&quot;</tt> or <tt>&quot;guestfs_tar_out&quot;</tt>.</p>
<h3>Why don’t you do everything through <font SIZE="-1">GVFS</font>?</h3>
<p> The problems are similar to the problems with <font SIZE="-1">FUSE.</font> </p>
<p> <font SIZE="-1">GVFS</font> is a better abstraction than <font SIZE="-1">POSIX/FUSE.</font> There is an <font SIZE="-1">FTP</font> backend for <font SIZE="-1">GVFS,</font> which is encouraging because <font SIZE="-1">FTP</font> is conceptually similar to the libguestfs <font SIZE="-1">API.</font> However the <font SIZE="-1">GVFS FTP</font> backend makes multiple simultaneous connections in order to keep interactivity, which we can&#8217;t easily do with libguestfs.</p>
<h3>Why can I write to the disk, even though I added it read-only?</h3>
<h3>Why does &#8211;ro appear to have no effect?</h3>
<p> When you add a disk read-only, libguestfs places a writable overlay on top of the underlying disk. Writes go into this overlay, and are discarded when the handle is closed (or <tt>&quot;guestfish&quot;</tt> etc. exits). </p>
<p> There are two reasons for doing it this way: Firstly read-only disks aren&#8217;t possible in many cases (eg. <font SIZE="-1">IDE</font> simply doesn&#8217;t support them, so you couldn&#8217;t have an IDE-emulated read-only disk, although this is not common in real libguestfs installations). </p>
<p> Secondly and more importantly, even if read-only disks were possible, you wouldn&#8217;t want them. Mounting any filesystem that has a journal, even <tt>&quot;mount -o ro&quot;</tt>, causes writes to the filesystem because the journal has to be replayed and metadata updated. If the disk was truly read-only, you wouldn&#8217;t be able to mount a dirty filesystem. </p>
<p> To make it usable, we create the overlay as a place to temporarily store these writes, and then we discard it afterwards. This ensures that the underlying disk is always untouched. </p>
<p> Note also that there is a regression test for this when building libguestfs (in <tt>&quot;tests/qemu&quot;</tt>). This is one reason why it’s important for packagers to run the test suite.</p>
<h3>Does &#8211;ro make all disks read-only?</h3>
<p> <i>No!</i> The <tt>&quot;--ro&quot;</tt> option only affects disks added on the command line, ie. using <tt>&quot;-a&quot;</tt> and <tt>&quot;-d&quot;</tt> options. </p>
<p> In guestfish, if you use the <tt>&quot;add&quot;</tt> command, then disk is added read-write (unless you specify the <tt>&quot;readonly:true&quot;</tt> flag explicitly with the command).</p>
<h3>Can I use guestfish &#8211;ro as a way to backup my virtual machines?</h3>
<p> Usually this is <i>not</i> a good idea. The question is answered in more detail in this mailing list posting: <a rel="nofollow" href="https://www.redhat.com/archives/libguestfs/2010-August/msg00024.html">https://www.redhat.com/archives/libguestfs/2010-August/msg00024.html</a> </p>
<p> See also the next question.</p>
<h3>Why can’t I run fsck on a live filesystem using guestfish &#8211;ro?</h3>
<p> This command will usually <i>not</i> work: </p>
<pre>
 guestfish --ro -a /dev/vg/my_root_fs run : fsck /dev/sda
</pre>
<p> The reason for this is that qemu creates a snapshot over the original filesystem, but it doesn&#8217;t create a strict point-in-time snapshot. Blocks of data on the underlying filesystem are read by qemu at different times as the fsck operation progresses, with host writes in between. The result is that fsck sees massive corruption (imaginary, not real!) and fails. </p>
<p> What you have to do is to create a point-in-time snapshot. If it’s a logical volume, use an <font SIZE="-1">LVM2</font> snapshot. If the filesystem is located inside something like a btrfs/ZFS file, use a btrfs/ZFS snapshot, and then run the fsck on the snapshot. In practice you don&#8217;t need to use libguestfs for this &#8212; just run <i>/sbin/fsck</i> directly. </p>
<p> Creating point-in-time snapshots of host devices and files is outside the scope of libguestfs, although libguestfs can operate on them once they are created.</p>
<h3>What’s the difference between guestfish and virt-rescue?</h3>
<p> A lot of people are confused by the two superficially similar tools we provide: </p>
<pre>
 $ guestfish --ro -a guest.img
 &gt;&lt;fs&gt; run
 &gt;&lt;fs&gt; fsck /dev/sda1
 $ virt-rescue --ro guest.img
 &gt;&lt;rescue&gt; /sbin/fsck /dev/sda1
</pre>
<p> And the related question which then arises is why you can’t type in full shell commands with all the &#8211;options in guestfish (but you can in <code><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></code>(1)). </p>
<p> <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1) is a program providing structured access to the <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) <font SIZE="-1">API.</font> It happens to be a nice interactive shell too, but its primary purpose is structured access from shell scripts. Think of it more like a language binding, like Python and other bindings, but for shell. The key differentiating factor of guestfish (and the libguestfs <font SIZE="-1">API</font> in general) is the ability to automate changes. </p>
<p> <code><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></code>(1) is a free-for-all freeform way to boot the libguestfs appliance and make arbitrary changes to your <font SIZE="-1">VM.</font> It’s not structured, you can&#8217;t automate it, but for making quick ad-hoc fixes to your guests, it can be quite useful. </p>
<p> But, libguestfs also has a &#8220;backdoor&#8221; into the appliance allowing you to send arbitrary shell commands. It’s not as flexible as virt-rescue, because you can&#8217;t interact with the shell commands, but here it is anyway: </p>
<pre>
 &gt;&lt;fs&gt; debug sh &quot;cmd arg1 arg2 ...&quot;
</pre>
<p> Note that you should <code>not</code> rely on this. It could be removed or changed in future. If your program needs some operation, please add it to the libguestfs <font SIZE="-1">API</font> instead.</p>
<h3>What’s the deal with guestfish -i?</h3>
<h3>Why does virt-cat only work on a real <font SIZE="-1">VM</font> image, but virt-df works on any disk image?</h3>
<h3>What does no root device found in this operating system image mean?</h3>
<p> These questions are all related at a fundamental level which may not be immediately obvious. </p>
<p> At the <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) <font SIZE="-1">API</font> level, a &#8220;disk image&#8221; is just a pile of partitions and filesystems. </p>
<p> In contrast, when the virtual machine boots, it mounts those filesystems into a consistent hierarchy such as: </p>
<pre>
 /          (/dev/sda2)
 │
 ├── /boot  (/dev/sda1)
 │
 ├── /home  (/dev/vg_external/Homes)
 │
 ├── /usr   (/dev/vg_os/lv_usr)
 │
 └── /var   (/dev/vg_os/lv_var)
</pre>
<p> (or drive letters on Windows). </p>
<p> The <font SIZE="-1">API</font> first of all sees the disk image at the &#8220;pile of filesystems&#8221; level. But it also has a way to inspect the disk image to see if it contains an operating system, and how the disks are mounted when the operating system boots: &#8220;<font SIZE="-1">INSPECTION&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3). </p>
<p> Users expect some tools (like <code><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></code>(1)) to work with <font SIZE="-1">VM</font> paths: </p>
<pre>
 virt-cat fedora.img /var/log/messages
</pre>
<p> How does virt-cat know that <i>/var</i> is a separate partition? The trick is that virt-cat performs inspection on the disk image, and uses that to translate the path correctly. </p>
<p> Some tools (including <code><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></code>(1), <code><a href="/docs/linux/man/1-virt-edit/">virt-edit</a></code>(1), <code><a href="/docs/linux/man/1-virt-ls/">virt-ls</a></code>(1)) use inspection to map <font SIZE="-1">VM</font> paths. Other tools, such as <code><a href="/docs/linux/man/1-virt-df/">virt-df</a></code>(1) and <code><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></code>(1) operate entirely at the raw &#8220;big pile of filesystems&#8221; level of the libguestfs <font SIZE="-1">API,</font> and don&#8217;t use inspection. </p>
<p> <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1) is in an interesting middle ground. If you use the <i>-a</i> and <i>-m</i> command line options, then you have to tell guestfish exactly how to add disk images and where to mount partitions. This is the raw <font SIZE="-1">API</font> level. </p>
<p> If you use the <i>-i</i> option, libguestfs performs inspection and mounts the filesystems for you. </p>
<p> The error <tt>&quot;no root device found in this operating system image&quot;</tt> is related to this. It means inspection was unable to locate an operating system within the disk image you gave it. You might see this from programs like virt-cat if you try to run them on something which is just a disk image, not a virtual machine disk image.</p>
<h3>What do these debug* and internal-* functions do?</h3>
<p> There are some functions which are used for debugging and internal purposes which are <i>not</i> part of the stable <font SIZE="-1">API.</font> </p>
<p> The <tt>&quot;debug*&quot;</tt> (or <tt>&quot;guestfs_debug*&quot;</tt>) functions, primarily &#8220;guestfs_debug&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) and a handful of others, are used for debugging libguestfs. Although they are not part of the stable <font SIZE="-1">API</font> and thus may change or be removed at any time, some programs may want to call these while waiting for features to be added to libguestfs. </p>
<p> The <tt>&quot;internal-*&quot;</tt> (or <tt>&quot;guestfs_internal_*&quot;</tt>) functions are purely to be used by libguestfs itself. There is no reason for programs to call them, and programs should not try to use them. Using them will often cause bad things to happen, as well as not being part of the documented stable <font SIZE="-1">API.</font></p>
<h2>DEVELOPERS</h2>
<h3>Where do I send patches?</h3>
<p> Please send patches to the libguestfs mailing list <a rel="nofollow" href="https://www.redhat.com/mailman/listinfo/libguestfs.">https://www.redhat.com/mailman/listinfo/libguestfs.</a> You don&#8217;t have to be subscribed, but there will be a delay until your posting is manually approved. </p>
<p> <code>Please don’t use github pull requests &#8211; they will be ignored</code>. The reasons are (a) we want to discuss and dissect patches on the mailing list, and (b) github pull requests turn into merge commits but we prefer to have a linear history.</p>
<h3>How do I propose a feature?</h3>
<p> Large new features that you intend to contribute should be discussed on the mailing list first (<a rel="nofollow" href="https://www.redhat.com/mailman/listinfo/libguestfs">https://www.redhat.com/mailman/listinfo/libguestfs</a>). This avoids disappointment and wasted work if we don&#8217;t think the feature would fit into the libguestfs project. </p>
<p> If you want to suggest a useful feature but don’t want to write the code, you can file a bug (see &#8220;<font SIZE="-1">GETTING HELP AND REPORTING BUGS&#8221;</font>) with <tt>&quot;RFE: &quot;</tt> at the beginning of the Summary line.</p>
<h3>Who can commit to libguestfs git?</h3>
<p> About 5 people have commit access to github. Patches should be posted on the list first and ACKed. The policy for ACKing and pushing patches is outlined here: </p>
<p> <a rel="nofollow" href="https://www.redhat.com/archives/libguestfs/2012-January/msg00023.html">https://www.redhat.com/archives/libguestfs/2012-January/msg00023.html</a></p>
<h3>Can I fork libguestfs?</h3>
<p> Of course you can. Git makes it easy to fork libguestfs. Github makes it even easier. It’s nice if you tell us on the mailing list about forks and the reasons for them.</p>
<h2>MISCELLANEOUS QUESTIONS</h2>
<h3>Can I monitor the live disk activity of a virtual machine using libguestfs?</h3>
<p> A common request is to be able to use libguestfs to monitor the live disk activity of a guest, for example, to get notified every time a guest creates a new file. Libguestfs does <i>not</i> work in the way some people imagine, as you can see from this diagram: </p>
<pre>
            ┌─────────────────────────────────────┐
            │ monitoring program using libguestfs │
            └─────────────────────────────────────┘
                             ↓
 ┌───────────┐    ┌──────────────────────┐
 │ live VM   │    │ libguestfs appliance │
 ├───────────┤    ├──────────────────────┤
 │ kernel (1)│    │ appliance kernel (2) │
 └───────────┘    └──────────────────────┘
      ↓                      ↓ (r/o connection)
      ┌──────────────────────┐
      |      disk image      |
      └──────────────────────┘
</pre>
<p> This scenario is safe (as long as you set the <tt>&quot;readonly&quot;</tt> flag when adding the drive). However the libguestfs appliance kernel (2) does not see all the changes made to the disk image, for two reasons:</p>
<dl>
<dt>i.</p>
<dd> The <font SIZE="-1">VM</font> kernel (1) can cache data in memory, so it doesn&#8217;t appear in the disk image.</p>
<dt>ii.</p>
<dd> The libguestfs appliance kernel (2) doesn&#8217;t expect that the disk image is changing underneath it, so its own cache is not magically updated even when the <font SIZE="-1">VM</font> kernel (1) does update the disk image.</dl>
<p> The only supported solution is to restart the entire libguestfs appliance whenever you want to look at changes in the disk image. At the <font SIZE="-1">API</font> level that corresponds to calling <tt>&quot;guestfs_shutdown&quot;</tt> followed by <tt>&quot;guestfs_launch&quot;</tt>, which is a heavyweight operation (see also <code><a href="/docs/linux/man/3-guestfs-performance/">guestfs-performance</a></code>(3)). </p>
<p> There are some unsupported hacks you can try if relaunching the appliance is really too costly:</p>
<dl>
<dt>&bull;</p>
<dd> Call <tt>&quot;guestfs_drop_caches (g, 3)&quot;</tt>. This causes all cached data help by the libguestfs appliance kernel (2) to be discarded, so it goes back to the disk image. </p>
<p> However this on its own is not sufficient, because qemu also caches some data. You will also need to patch libguestfs to (re-)enable the <tt>&quot;cache=none&quot;</tt> mode. See: <a rel="nofollow" href="https://rwmj.wordpress.com/2013/09/02/new-in-libguestfs-allow-cache-mode-to-be-selected/">https://rwmj.wordpress.com/2013/09/02/new-in-libguestfs-allow-cache-mode-to-be-selected/</a></p>
<dt>&bull;</p>
<dd> Use a tool like virt-bmap instead.</p>
<dt>&bull;</p>
<dd> Run an agent inside the guest.</dl>
<p> Nothing helps if the guest is making more fundamental changes (eg. deleting filesystems). For those kinds of things you must relaunch the appliance. </p>
<p> (Note there is a third problem that you need to use consistent snapshots to really examine live disk images, but that’s a general problem with using libguestfs against any live disk image.)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1), <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2012-2019 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> Lesser General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> See the <font SIZE="-1">GNU</font> Lesser General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA</font></p>
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
<dd> Run <code><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></code>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
</dl>
<h2>Index</h2>
<dt><a href="#lbAH">GETTING HELP AND REPORTING BUGS</a></p>
<dd>
<dt><a href="#lbAM">COMMON PROBLEMS</a></p>
<dd>
<dt><a href="#lbAU">DOWNLOADING, INSTALLING, COMPILING LIBGUESTFS</a></p>
<dd>
<dt><a href="#lbBE">SPEED, DISK SPACE USED BY LIBGUESTFS</a></p>
<dd>
<dt><a href="#lbBK">PROBLEMS OPENING DISK IMAGES</a></p>
<dd>
<dt><a href="#lbBW">USING LIBGUESTFS IN YOUR OWN PROGRAMS</a></p>
<dd>
<dt><a href="#lbBZ">DEBUGGING LIBGUESTFS</a></p>
<dd>
<dt><a href="#lbCK">DESIGN/INTERNALS OF LIBGUESTFS</a></p>
<dd>
<dt><a href="#lbCX">DEVELOPERS</a></p>
<dd>
<dt><a href="#lbDC">MISCELLANEOUS QUESTIONS</a></p>
<dd>
<dt><a href="#lbDE">SEE ALSO</a></p>
<dd>
<dt><a href="#lbDF">AUTHORS</a></p>
<dd>
<dt><a href="#lbDG">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbDH">LICENSE</a></p>
<dd>
<dt><a href="#lbDI">BUGS</a></p>
<dd></dl>
