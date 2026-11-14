---
title: "livecd-creator(8)"
name: "livecd-creator"
section: "8"
letter: "l"
url: "/docs/linux/man/8-livecd-creator/"
description: "livecd-creator – creates live CD or DVD images."
---

<p>livecd-creator &#8211; creates live CD or DVD images.</p>
<h2>Synopsis</h2>
<p><code>livecd-creator</code> [<font SIZE="-1">OPTIONS</font>]</p>
<h2>Description</h2>
<p><code>livecd-creator</code> creates live <font SIZE="-1">CD</font> or <font SIZE="-1">DVD</font> images(<font SIZE="-1">ISO</font> images) from kickstart files. Kickstart files contain information about packages and configuration settings which are used to build the image.</p>
<h2>Options</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd>Shows the help message and exits.</dl>
<h2>Image Options</h2>
<p>These options define the created image.</p>
<dl>
<dt>-c <font SIZE="-1">KSCFG,</font> &#8211;config=KSCFG</p>
<dd>Path to kickstart configuration file.</p>
<dt>-b <font SIZE="-1">BASE_ON,</font> &#8211;base-on=BASE_ON</p>
<dd>Add packages to an existing live <font SIZE="-1">CD</font> iso9660 image.</p>
<dt>-f <font SIZE="-1">FS_LABEL,</font> &#8211;fslabel=FS_LABEL</p>
<dd>Defines the file system label. The default is based on the configuration name.</p>
<dt>&#8211;compression-type=COMPRESSOR</p>
<dd>Specify a compressor recognized by mksquashfs. xz is the default and works with 2.6.38 and later kernels. gzip works with all kernels. lzo works with 2.6.36 and later kernels. lzma will only work with custom kernels. Set to &#8216;None&#8217; to force reading the compressor used in <font SIZE="-1">BASE_ON.</font> If gzip is used, the -comp option is not passed to mksquashfs to allow the use of older versions of mksquashfs.</p>
<dt>&#8211;releasever=VER</p>
<dd>Set the value to substitute for <tt>$releasever</tt> in kickstart repo urls</dl>
<h2>System Directory Options</h2>
<p>These options define directories used on your system for creating the live image.</p>
<dl>
<dt>-t <font SIZE="-1">TMPDIR,</font> &#8211;tmpdir=TMPDIR</p>
<dd>defines the temporary directory to use. The default directory is /var/tmp.</p>
<dt>&#8211;cache=CACHEDIR</p>
<dd>Defines the cache directory to use (default: private cache).</dl>
<h2>Examples</h2>
<p>Barebones LiveCD </p>
<p> livecd-creator \ &#8211;config=/usr/share/livecd-tools/livecd-fedora-minimal.ks </p>
<p> Fedora Desktop Live <font SIZE="-1">CD</font> </p>
<p> livecd-creator \ &#8211;config=/usr/share/livecd-tools/livecd-fedora-desktop.ks \ &#8211;fslabel=Fedora9-LiveCD-foo</p>
<h2>Repo Extensions</h2>
<p>livecd-creator provides for some extensions to the repo commands similar to what yum supports. The strings <tt>$arch</tt>, <tt>$basearch</tt> and <tt>$releasever</tt> are replaced with the system arch, basearch and release version respectively. When no &#8211;releasever is passed it defaults to the current system&#8217;s version. The allows the use of repo commands such as the following: </p>
<p> repo &#8211;name=fedora &#8211;mirrorlist=<a rel="nofollow" href="http://mirrors.fedoraproject.org/mirrorlist?repo=fedora-$releasever">http://mirrors.fedoraproject.org/mirrorlist?repo=fedora-$releasever</a>&amp;arch=$basearch </p>
<p> Note that in a chroot environment (like koji) the rpmdb is not available, so either don&#8217;t use <tt>$releasever</tt> in that case, or pass &#8211;releasever=VER</p>
<h2>Contributors</h2>
<p>David Zeuthen, Jeremy Katz, Douglas McClendon and a team of many other contributors. See the <font SIZE="-1">AUTHORS</font> file in the source distribution for the complete list of credits.</p>
<h2>Bugs</h2>
<p>Report bugs to the mailing list <tt>&quot;<a rel="nofollow" href="http://www.redhat.com/mailman/listinfo/fedora-livecd-list">http://www.redhat.com/mailman/listinfo/fedora-livecd-list</a>&quot;</tt> or directly to Bugzilla <tt>&quot;<a href="http://bugzilla.redhat.com/bugzilla/">http://bugzilla.redhat.com/bugzilla/</a>&quot;</tt> against the <tt>&quot;Fedora&quot;</tt> product, and the <tt>&quot;livecd-tools&quot;</tt> component.</p>
<h2>Copyright</h2>
<p>Copyright (C) Fedora Project 2008,2009, and various contributors. This is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> General Public License <tt>&quot;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&quot;</tt>. There is <font SIZE="-1">NO WARRANTY,</font> to the extent permitted by law.</p>
<h2>See Also</h2>
<p><tt>&quot;<a href="/docs/linux/man/1-livecd-iso-to-disk/">livecd-iso-to-disk</a>(1)&quot;</tt>, project website <tt>&quot;<a rel="nofollow" href="http://fedoraproject.org/wiki/FedoraLiveCD">http://fedoraproject.org/wiki/FedoraLiveCD</a>&quot;</tt> </p>
