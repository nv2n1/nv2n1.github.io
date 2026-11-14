---
title: "febootstrap(8)"
name: "febootstrap"
section: "8"
letter: "f"
url: "/docs/linux/man/8-febootstrap/"
description: "febootstrap – Bootstrap a basic Fedora system (like Debian debootstrap)"
---

<p>febootstrap &#8211; Bootstrap a basic Fedora system (like Debian debootstrap)</p>
<h2>Synopsis</h2>
<pre> febootstrap [--options] REPO TARGET [MIRROR]</pre>
<h2>Examples</h2>
<pre> febootstrap fedora-10 /tmp/f10
 febootstrap rawhide /tmp/rawhide
 febootstrap rawhide /tmp/rawhide <a rel="nofollow" href="http://mymirror/rawhide/x86_64/os">http://mymirror/rawhide/x86_64/os</a>
 febootstrap --groupinstall=&quot;Mail Server&quot; fedora-10 /tmp/mailserver</pre>
<h2>Description</h2>
<p>febootstrap creates a Fedora root filesystem, based on the Fedora version specified by <i></i><font SIZE="-1"><i>REPO</i></font><i></i> under the directory specified by <i></i><font SIZE="-1"><i>TARGET</i></font><i></i>. Optionally <i></i><font SIZE="-1"><i>MIRROR</i></font><i></i> can point to a local mirror (otherwise the public Fedora mirrors are used). <i></i><font SIZE="-1"><i>REPO</i></font><i></i> names are <tt>&quot;fedora-</tt>VERSION<tt>&quot;</tt> (eg. <tt>&quot;fedora-10&quot;</tt>) or <tt>&quot;rawhide&quot;</tt>. </p>
<p> febootstrap does <i>not</i> need to be run as root. If for some reason you do run it as root, then it works slightly differently and may have side effects such as stopping or starting system daemons. </p>
<p> For more advanced needs, take a look at <i><a href="/docs/linux/man/1-mock/">mock</a></i>(1), <tt>&quot;livecd-creator&quot;</tt> and <i>thincrust.net</i>&#8216;s <tt>&quot;appliance-creator&quot;</tt>. </p>
<p> The normal output is a root directory located at <i></i><font SIZE="-1"><i>TARGET</i></font><i></i> and a fakeroot logfile at <tt>&quot;</tt>TARGET<tt>/fakeroot.log&quot;</tt>.</p>
<h2>Options</h2>
<dl>
<dt><code>-i package</code></p>
<dd>
<dt><code>&#8211;install=package</code></p>
<dd>
<dt><code>-g group</code></p>
<dd>
<dt><code>&#8211;groupinstall=group</code></p>
<dd>Specify the package or group to install. To list multiple packages or groups, you must give multiple <tt>&quot;-i&quot;</tt> or <tt>&quot;-g&quot;</tt> options. Group names can contain spaces, so use quotes where necessary. </p>
<p> These are passed directly to <tt>&quot;yum install&quot;</tt> or <tt>&quot;yum groupinstall&quot;</tt> commands, and thus any dependencies are also resolved by yum. You can also use shell globs and filenames here, as with ordinary yum. </p>
<p> If no packages or groups are given, then we install the <tt>&quot;Core&quot;</tt> group which is a small working Fedora installation (but by no means minimal). Use <tt>&quot;yum groupinfo Core&quot;</tt> to list the packages currently in the <tt>&quot;Core&quot;</tt> group.</p>
<dt><code>&#8211;no-clean</code></p>
<dd>Normally febootstrap will clean up the yum repository (<tt>&quot;/var/cache/yum&quot;</tt> inside the image). This contains the downloaded RPMs and metadata. However if you give the <tt>&quot;--no-clean&quot;</tt> option, then the yum repository is left. This is useful if you want to run further yum commands inside the filesystem by hand.</p>
<dt><code>-p proxyurl</code></p>
<dd>
<dt><code>&#8211;proxy=proxyurl</code></p>
<dd><font SIZE="-1">URL</font> to the proxy server that yum should use.</p>
<dt><code>-u source</code></p>
<dd>
<dt><code>&#8211;updates=source</code></p>
<dd>Pull in updates from an additional updates repository. The possible sources are:</p>
<dl>
<dd>
<dl>
<dt>-u <a rel="nofollow" href="http://...">http://&#8230;</a> (a <font SIZE="-1">URL</font>)</p>
<dd>Get updates from the specific <font SIZE="-1">URL</font>.</p>
<dt>-u updates-released-fN (an updates repository name)</p>
<dd>Get updates from the public mirrors of the named repository (eg. <tt>&quot;updates-released-f10&quot;</tt>). See <font SIZE="-1">REPOSITORIES</font> below.</p>
<dt>-u none (default)</p>
<dd>Don&#8217;t add an updates repository. This is the default.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h2>Repositories</h2>
<p>You can list available repositories by visiting this <font SIZE="-1">URL:</font> </p>
<p> &lt;<a rel="nofollow" href="http://mirrors.fedoraproject.org/mirrorlist?repo=help">http://mirrors.fedoraproject.org/mirrorlist?repo=help</a>&amp;arch=i386&gt; </p>
<p> (If necessary replace <tt>&quot;i386&quot;</tt> with your architecture, but it seems unlikely that this list will change based on architecture).</p>
<h2>Running Extra Commands In The Root Filesystem</h2>
<p>If you want to run further commands inside the root filesystem, for example additional <tt>&quot;yum&quot;</tt> installs, then use <tt>&quot;febootstrap-run&quot;</tt>. See the <i><a href="/docs/linux/man/8-febootstrap-run/">febootstrap-run</a></i>(8) manual page for more details. </p>
<p> You have to be careful about modifying files in the root filesystem directly (without using <tt>&quot;febootstrap-run&quot;</tt>). It&#8217;s easy to confuse fakeroot and end up with the wrong permissions on files (see <font SIZE="-1">FAKEROOT</font> <font SIZE="-1">LOGFILE</font> below). </p>
<p> <tt>&quot;febootstrap-run&quot;</tt> runs the command inside the root filesystem, which means it won&#8217;t normally have access to files outside the root. You can use <tt>&quot;FAKECHROOT_EXCLUDE_PATH&quot;</tt> environment variable (see <i><a href="/docs/linux/man/1-fakechroot/">fakechroot</a></i>(1)) or copy files into the root first.</p>
<h3><font SIZE="-1">FAKEROOT</font> <font SIZE="-1">LOGFILE</font></h3>
<p>When febootstrap is run as non-root (the normal case) we use fakeroot so that yum thinks it is running as root. Fakeroot keeps track of &#8220;real&#8221; file permissions in a log file which is saved into the target directory as <tt>&quot;</tt>TARGET<tt>/fakeroot.log&quot;</tt>. </p>
<p> This logfile is indexed by inode number, which makes certain operations safe and other operations unsafe. Files should be replaced only by doing: </p>
<pre> echo updated-content &gt; old-file</pre>
<p>(since that preserves the original inode). </p>
<p> Deleting files and then creating new ones (even with a different name) is usually unsafe, because the new files might reuse inodes claimed by the old files, and so appear with peculiar permissions (eg. unreadable, or as a symbolic link). </p>
<p> Deleting files is also usually unsafe, although the reasons are more subtle. If you just use <tt>&quot;rm&quot;</tt> then the inode number is not deleted from <tt>&quot;fakeroot.log&quot;</tt> which means it can be reused by another file later on. </p>
<p> In most cases it&#8217;s usually safest to use <tt>&quot;febootstrap-run&quot;</tt>. </p>
<p> You can use the fakeroot logfile in a number of ways:</p>
<dl>
<dt>*</p>
<dd>Use <i><a href="/docs/linux/man/8-febootstrap-run/">febootstrap-run</a></i>(8) to run a command with the faked file permissions.</p>
<dt>*</p>
<dd>Use <i><a href="/docs/linux/man/8-febootstrap-install/">febootstrap-install</a></i>(8) to install a file with permissions in the root filesystem.</p>
<dt>*</p>
<dd>Generate an initramfs (compressed cpio) file containing the correct permissions using the tool <tt>&quot;febootstrap-to-initramfs&quot;</tt>.</p>
<dt>*</p>
<dd>Generate a supermin appliance using the tool <tt>&quot;febootstrap-to-supermin&quot;</tt>.</p>
<dt>*</p>
<dd>Apply the permissions to the target directory using the forthcoming tool <tt>&quot;febootstrap-fix-root&quot;</tt> (requires root).</dl>
<h2>Running Febootstrap As Root</h2>
<p>There is some rudimentary support for running <tt>&quot;febootstrap&quot;</tt> as root. However it is not well-tested and generally not recommended.</p>
<h2>Comparison To Debootstrap</h2>
<p>febootstrap cannot do cross-architecture installs (<tt>&quot;debootstrap --foreign&quot;</tt>). The reason is that <tt>%pre</tt> and <tt>%post</tt> scripts cannot run. It may be possible to defer running of scriptlets (which is basically how debootstrap works), and patches to do this are welcomed. </p>
<p> febootstrap cannot do 32-on-64 bit installs. The reason is that fakeroot and fakechroot do not load the correct preload library. This is really a bug in fakeroot/fakechroot, which we think would be easy to fix. (debootstrap deals with this case the same as for <tt>&quot;--foreign&quot;</tt> installs &#8211; see previous point).</p>
<h2>Other Restrictions And Bugs</h2>
<p>The following programs are not run during <tt>%post</tt> scriptlets (because they are all statically linked, and fakechroot cannot run statically linked programs).</p>
<dl>
<dt>/sbin/ldconfig (from many packages)</p>
<dd>
<dt>/usr/sbin/glibc_post_upgrade (from glibc)</p>
<dd>
<dt>/usr/sbin/build-locale-archive (from glibc-common)</p>
<dd>
<dt>/usr/sbin/libgcc_post_upgrade (from libgcc)</p>
<dd></dl>
<p> If you wish, you can run them the first time you boot into the new machine. </p>
<p> febootstrap recreates the repository anew each time, and this causes yum to download all the RPMs every time. This is very wasteful, and we should provide a way to cache the repository.</p>
<h2>Home Page</h2>
<p>&lt;<a rel="nofollow" href="http://et.redhat.com/~rjones/febootstrap">http://et.redhat.com/~rjones/febootstrap</a>&gt;</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-febootstrap-to-initramfs/">febootstrap-to-initramfs</a></i>(8), <i><a href="/docs/linux/man/8-febootstrap-minimize/">febootstrap-minimize</a></i>(8), <i><a href="/docs/linux/man/8-febootstrap-run/">febootstrap-run</a></i>(8), <i><a href="/docs/linux/man/8-febootstrap-install/">febootstrap-install</a></i>(8), <i><a href="/docs/linux/man/8-febootstrap-to-supermin/">febootstrap-to-supermin</a></i>(8), <i><a href="/docs/linux/man/1-fakeroot/">fakeroot</a></i>(1), <i><a href="/docs/linux/man/1-fakechroot/">fakechroot</a></i>(1), <i><a href="/docs/linux/man/8-yum/">yum</a></i>(8), <i><a href="/docs/linux/man/8-rpm/">rpm</a></i>(8).</p>
<h2>Alternatives</h2>
<p><i><a href="/docs/linux/man/1-mock/">mock</a></i>(1), &lt;<a rel="nofollow" href="http://fedoraproject.org/wiki/FedoraLiveCD/LiveCDHowTo">http://fedoraproject.org/wiki/FedoraLiveCD/LiveCDHowTo</a>&gt;, &lt;<a rel="nofollow" href="http://thincrust.net/">http://thincrust.net/</a>&gt;, <i><a href="/docs/linux/man/8-debootstrap/">debootstrap</a></i>(8), <tt>&quot;ubuntu-vm-builder&quot;</tt>.</p>
<h2>Authors</h2>
<p>Richard W.M. Jones &lt;rjones @ redhat . com&gt;</p>
<h2>Copyright</h2>
<p>(C) Copyright 2009 Red Hat Inc., &lt;<a rel="nofollow" href="http://et.redhat.com/~rjones/febootstrap">http://et.redhat.com/~rjones/febootstrap</a>&gt;. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA</font> 02139, <font SIZE="-1">USA</font>.</p>
