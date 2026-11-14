---
title: "fakechroot(1)"
name: "fakechroot"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fakechroot/"
description: "fakechroot – gives a fake chroot environment"
---

<h2 class="name">NAME</h2>
<p> fakechroot &#8211; gives a fake chroot environment </p>
<h2>SYNOPSIS</h2>
<p> <code>fakechroot</code> [<code>-s</code>|<code>&#8211;use-system-libs</code>] [<code>-l</code>|<code>&#8211;lib</code>&nbsp;<wbr><i>library</i>] [<code>&#8212;</code>] [<i>command</i>]</p>
<h2>DESCRIPTION</h2>
<p> fakechroot runs a command in an environment were is additional possibility to use <i><a href="/docs/linux/man/8-chroot/">chroot</a></i>(8) command without root privileges. This is useful for allowing users to create own chrooted environment with possibility to install another packages without need for root privileges. </p>
<p> fakechroot replaces more library functions (<i><a href="/docs/linux/man/2-chroot/">chroot</a></i>(2), <i><a href="/docs/linux/man/2-open/">open</a></i>(2), etc.) by ones that simulate the effect the real library functions would have had, had the user really been in chroot. These wrapper functions are in a shared library <i>/usr/lib/fakechroot/libfakechroot.so</i> which is loaded through the <font SIZE="-1"><code>LD_PRELOAD</code></font> mechanism of the dynamic loader. (See <i><a href="/docs/linux/man/8-ld-so/">ld.so</a></i>(8)) </p>
<p> In fake chroot you can install Debian bootstrap with `debootstrap &#8211;variant=fakechroot&#8217; command. In this environment you can use i.e. <i><a href="/docs/linux/man/8-apt-get/">apt-get</a></i>(8) command to install another packages from common user&#8217;s account. </p>
<p> In the current version, the fakechroot does not provide the <i><a href="/docs/linux/man/1-fakeroot/">fakeroot</a></i>(1) functionality! You might to call fakechroot with fakeroot command, if you want to emulate root environment, i.e.: </p>
<pre>
 $ fakeroot fakechroot /usr/sbin/chroot /tmp/debian /bin/sh
 # id
 uid=0(root) gid=0(root) groups=0(root)
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code> <i>library</i>|<code>&#8211;lib</code> <i>library</i></p>
<dd> Specify an alternative wrapper library.</p>
<dt><code>-s</code>|<code>&#8211;use-system-libs</code></p>
<dd> Use system libraries before chroot&#8217;s libraries. This might be a workaround if system dynamic linker (<i>/lib/ld-linux.so.2</i> for Linux) can not load <i>libc.so</i> from fake chroot. </p>
<p> Try this setting if you noticed following errors: </p>
<pre>
 $ fakechroot /usr/sbin/chroot /tmp/sarge /bin/true
 /bin/true: relocation error: /srv/sarge/lib/tls/libc.so.6: symbol _dl
 _starting_up, version GLIBC_PRIVATE not defined in file ld-linux.so.2
  with link time reference
 $ fakechroot /usr/sbin/chroot /tmp/centos4 /bin/true
 Segmentation fault
</pre>
<dt>[<code>&#8212;</code>] <i>command</i></p>
<dd> Any command you want to be ran as fakechroot. Use &#8216;<code>&#8212;</code>&#8216; if in the command you have other options that may confuse fakechroot&#8217;s option parsing.</p>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-v</code></p>
<dd> Display version.</dl>
<h2>EXAMPLES</h2>
<p> An example session with fakechroot: </p>
<pre>
 $ export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin
 :/bin:/usr/bin/X11
 $ fakeroot -s fakechroot.save fakechroot debootstrap --variant=fakech
 root lenny /tmp/lenny
 $ fakeroot -i fakechroot.save fakechroot chroot /tmp/lenny /bin/bash
 # cd /
 # sh /usr/share/doc/fakechroot/examples/savemode.sh
 # echo deb <a rel="nofollow" href="http://ftp.debian.org/debian">http://ftp.debian.org/debian</a> lenny main contrib non-free &gt;
 /etc/apt/sources.list
 # echo deb-src <a rel="nofollow" href="http://ftp.debian.org/debian">http://ftp.debian.org/debian</a> lenny main contrib non-fr
 ee &gt;&gt; /etc/apt/sources.list
 # apt-get update
 # apt-get install adduser whiptail build-essential devscripts
 # adduser --uid 1001 user
 # cd /tmp
 # apt-get source hello
 # cd hello-*
 # debuild --preserve-env -b
 # exit
</pre>
<h2>SECURITY ASPECTS</h2>
<p> fakechroot is a regular, non-setuid program. It does not enhance a user&#8217;s privileges, or decrease the system&#8217;s security.</p>
<h2>FILES</h2>
<dl>
<dt><i>/usr/lib/fakechroot/libfakechroot.so</i></p>
<dd> The shared library containing the wrapper functions.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>FAKECHROOT</code></font></p>
<dd> The value is true for fake chroot environment.</p>
<dt><font SIZE="-1"><code>FAKECHROOT_VERSION</code></font></p>
<dd> The version of current fakechroot library.</p>
<dt><font SIZE="-1"><code>FAKECHROOT_BASE</code></font></p>
<dd> The root directory for fake chroot environment.</p>
<dt><font SIZE="-1"><code>FAKECHROOT_EXCLUDE_PATH</code></font></p>
<dd> The list of directories which are excluded from being chrooted. The elements of list are separated with colon.</p>
<dt><font SIZE="-1"><code>FAKECHROOT_CMD_SUBST</code></font></p>
<dd> A list of command substitutions. If a program tries to execute one of the commands given (path relative to the chroot) then the substitute command runs instead (path to substitute command is not chrooted). </p>
<p> For example: </p>
<pre>
 FAKECHROOT_CMD_SUBST=/sbin/ldconfig=/tmp/ldconfig-wrapper
</pre>
<p> will substitute <tt>&quot;/tmp/ldconfig-wrapper&quot;</tt> for <tt>&quot;/sbin/ldconfig&quot;</tt>. </p>
<p> Give as many substitute commands as you want, separated by <tt>&quot;:&quot;</tt> (colon) characters.</p>
<dt><font SIZE="-1"><code>LD_LIBRARY_PATH</code></font>, <font SIZE="-1"><code>LD_PRELOAD</code></font></p>
<dd> Fakechroot is implemented by wrapping system calls. This is accomplished by setting LD_LIBRARY_PATH=/usr/lib/fakechroot and LD_PRELOAD=libfakechroot.so. That library is loaded before the system&#8217;s C library, and so most of the library functions are intercepted by it. If you need to set either <font SIZE="-1"><code>LD_LIBRARY_PATH</code></font> or <font SIZE="-1"><code>LD_PRELOAD</code></font> from within a fakechroot environment, it should be set relative to the given paths, as in LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/foo/bar/</dl>
<h2>LIMITATIONS</h2>
<dl>
<dt>o</p>
<dd> <i>/lib/ld-linux.so.2</i> is always loaded from real environment. This path is hardcoded by linker for all binaries.</p>
<dt>o</p>
<dd> Every command executed within fakechroot needs to be linked to the same version of the C library as fakechroot itself. If the libraries in chroot are not compatible, try to use <code>&#8211;use-system-libs</code> option.</p>
<dt>o</p>
<dd> You can provide symlinks to the outside. The symlink have to be created before chroot is called. It can be useful for accessing the real <i>/proc</i> and <i>/dev</i> directory. You can also set the <font SIZE="-1"><code>FAKECHROOT_EXCLUDE_PATH</code></font> environment variable: </p>
<pre>
 $ export FAKECHROOT_EXCLUDE_PATH=/tmp:/proc:/dev:/var/run
</pre>
<dt>o</p>
<dd> Statically linked binaries doesn&#8217;t work, especially <i><a href="/docs/linux/man/8-ldconfig/">ldconfig</a></i>(8), so you have to wrap this command with dummy version and i.e. set the dpkg diversion, see: <i><a href="/docs/linux/man/8-dpkg-divert/">dpkg-divert</a></i>(8).</p>
<dt>o</p>
<dd> <i><a href="/docs/linux/man/1-ldd/">ldd</a></i>(1) also doesn&#8217;t work. You have to use <tt>&quot;alias ldd='LD_TRACE_LOADED_OBJECTS=1'&quot;</tt> or to use a wrapper instead. The example wrapper is available at <i>scripts/</i> directory in fakechroot&#8217;s source package and it is located at <i>/usr/share/doc/fakechroot/examples</i> directory.</p>
<dt>o</p>
<dd> The full screen applications hangs up if <i>/dev/tty</i> file is not a real device. Link <i>/dev/tty</i> file or whole <i>/dev</i> directory to the real one or remove it from fake chroot environment.</p>
<dt>o</p>
<dd> <i>lckpwdf()</i> and <i>ulckpwdf()</i> are ignored so <i><a href="/docs/linux/man/1-passwd/">passwd</a></i>(1) command should work</p>
<dt>o</p>
<dd> Your real uid should exist in <i>/etc/passwd</i>. Create it with adduser &#8211;uid <i>realuid</i> <i>realuser</i>.</p>
<dt>o</p>
<dd> <i><a href="/docs/linux/man/1-debuild/">debuild</a></i>(1) cleans environment. Use &#8211;preserve-env option to prevent this behaviour.</dl>
<h2>COPYING</h2>
<p> fakechroot is distributed under the <font SIZE="-1">GNU</font> Lesser General Public License (<font SIZE="-1">LGPL</font> 2.1 or greater).</p>
<h2>AUTHORS</h2>
<p> Copyright (c) 2003-2008 Piotr Roszatycki &lt;dexter [at] debian.org&gt; </p>
<p> Copyright (c) 2006-2007 Lionel Tricon &lt;lionel.tricon [at] free.fr&gt; </p>
<p> Copyright (c) 2007 Mark Eichin &lt;eichin [at] metacarta.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-fakeroot/">fakeroot</a></i>(1), <i><a href="/docs/linux/man/1-dpkg-buildpackage/">dpkg-buildpackage</a></i>(1), <i><a href="/docs/linux/man/1-debuild/">debuild</a></i>(1), <i><a href="/docs/linux/man/8-debootstrap/">debootstrap</a></i>(8), <a rel="nofollow" href="http://fakechroot.alioth.debian.org/">http://fakechroot.alioth.debian.org/</a> </p>
<h2>Index</h2>
