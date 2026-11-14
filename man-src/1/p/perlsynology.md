---
title: "perlsynology(1)"
name: "perlsynology"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlsynology/"
description: "perlsynology – Perl 5 on Synology DSM systems"
---

<h2 class="name">NAME</h2>
<p> perlsynology &#8211; Perl 5 on Synology DSM systems </p>
<h2>DESCRIPTION</h2>
<p> Synology manufactures a vast number of Network Attached Storage (<font SIZE="-1">NAS</font>) devices that are very popular in large organisations as well as small businesses and homes. </p>
<p> The <font SIZE="-1">NAS</font> systems are equipped with Synology Disk Storage Manager (<font SIZE="-1">DSM</font>), which is a trimmed-down Linux system enhanced with several tools for managing the <font SIZE="-1">NAS.</font> There are several flavours of hardware: Marvell Armada (ARMv5tel, ARMv7l), Intel Atom (i686, x86_64), Freescale QorIQ (<font SIZE="-1">PPC</font>), and more. For a full list see the Synology <font SIZE="-1">FAQ</font> &lt;<a rel="nofollow" href="http://forum.synology.com/wiki/index.php/What_kind_of_CPU_does_my_NAS_have">http://forum.synology.com/wiki/index.php/What_kind_of_CPU_does_my_NAS_have</a>&gt;. </p>
<p> Since it is based on Linux, the <font SIZE="-1">NAS</font> can run many popular Linux software packages, including Perl. In fact, Synology provides a ready-to-install package for Perl, depending on the version of <font SIZE="-1">DSM</font> the installed perl ranges from 5.8.6 on <font SIZE="-1">DSM-4.3</font> to 5.24.0 on <font SIZE="-1">DSM-6.1.</font> </p>
<p> There is an active user community that provides many software packages for the Synology <font SIZE="-1">DSM</font> systems; at the time of writing this document they provide Perl version 5.24.1. </p>
<p> This document describes various features of Synology <font SIZE="-1">DSM</font> operating system that will affect how Perl 5 (hereafter just Perl) is configured, compiled and/or runs. It has been compiled and verified by Johan Vromans for the Synology <font SIZE="-1">DS413</font> (QorIQ), with feedback from H.Merijn Brand (<font SIZE="-1">DS213,</font> ARMv5tel and <font SIZE="-1">RS815,</font> Intel Atom x64).</p>
<h3>Setting up the build environment</h3>
<p> <i></i><font SIZE="-1"><i>DSM 5</i></font><i></i> </p>
<p> As <font SIZE="-1">DSM</font> is a trimmed-down Linux system, it lacks many of the tools and libraries commonly found on Linux. The basic tools like sh, cp, rm, etc. are implemented using BusyBox &lt;<a rel="nofollow" href="http://en.wikipedia.org/wiki/BusyBox">http://en.wikipedia.org/wiki/BusyBox</a>&gt;.</p>
<dl>
<dt>&bull;</p>
<dd> Using your favourite browser open the <font SIZE="-1">DSM</font> management page and start the Package Center.</p>
<dt>&bull;</p>
<dd> If you want to smoke test Perl, install <tt>&quot;Perl&quot;</tt>.</p>
<dt>&bull;</p>
<dd> In Settings, add the following Package Sources: </p>
<pre>
  <a rel="nofollow" href="http://www.cphub.net">http://www.cphub.net</a>
  <a rel="nofollow" href="http://packages.quadrat4.de">http://packages.quadrat4.de</a>
</pre>
<dt>&bull;</p>
<dd> Still in Settings, in Channel Update, select Beta Channel.</p>
<dt>&bull;</p>
<dd> Press Refresh. In the left panel the item &#8220;Community&#8221; will appear. Click it. Select &#8220;Bootstrap Installer Beta&#8221; and install it.</p>
<dt>&bull;</p>
<dd> Likewise, install &#8220;iPKGui Beta&#8221;. </p>
<p> The application window should now show an icon for iPKGui.</p>
<dt>&bull;</p>
<dd> Start iPKGui. Install the packages <tt>&quot;make&quot;</tt>, <tt>&quot;gcc&quot;</tt> and <tt>&quot;coreutils&quot;</tt>. </p>
<p> If you want to smoke test Perl, install <tt>&quot;patch&quot;</tt>.</dl>
<p> The next step is to add some symlinks to system libraries. For example, the development software expect a library <tt>&quot;libm.so&quot;</tt> that normally is a symlink to <tt>&quot;libm.so.6&quot;</tt>. Synology only provides the latter and not the symlink. </p>
<p> Here the actual architecture of the Synology system matters. You have to find out where the gcc libraries have been installed. Look in /opt for a directory similar to arm-none-linux-gnueab or powerpc-linux-gnuspe. In the instructions below I&#8217;ll use powerpc-linux-gnuspe as an example.</p>
<dl>
<dt>&bull;</p>
<dd> On the <font SIZE="-1">DSM</font> management page start the Control Panel.</p>
<dt>&bull;</p>
<dd> Click Terminal, and enable <font SIZE="-1">SSH</font> service.</p>
<dt>&bull;</p>
<dd> Close Terminal and the Control Panel.</p>
<dt>&bull;</p>
<dd> Open a shell on the Synology using ssh and become root.</p>
<dt>&bull;</p>
<dd> Execute the following commands: </p>
<pre>
  cd /lib
  ln -s libm.so.6 libm.so
  ln -s libcrypt.so.1 libcrypt.so
  ln -s libdl.so.2 libdl.so
  cd /opt/powerpc-linux-gnuspe/lib  (or
                                    /opt/arm-none-linux-gnueabi/lib)
  ln -s /lib/libdl.so.2 libdl.so
</pre>
</dl>
<p> <font SIZE="-1"><code>WARNING:</code></font> When you perform a system software upgrade, these links will disappear and need to be re-established. </p>
<p> <i></i><font SIZE="-1"><i>DSM 6</i></font><i></i> </p>
<p> Using iPkg has been deprecated on <font SIZE="-1">DSM 6,</font> but an alternative is available for <font SIZE="-1">DSM 6:</font> entware/opkg. For instructions on how to use that, please read Install Entware-ng on Synology <font SIZE="-1">NAS</font> &lt;<a rel="nofollow" href="https://github.com/Entware-ng/Entware-ng/wiki/Install-on-Synology-NAS">https://github.com/Entware-ng/Entware-ng/wiki/Install-on-Synology-NAS</a>&gt; </p>
<p> That sadly does not (yet) work on QorIQ. At the moment of writing, the supported architectures are armv5, armv7, mipsel, wl500g, x86_32, and x86_64. Check here &lt;<a rel="nofollow" href="http://pkg.entware.net/binaries/">http://pkg.entware.net/binaries/</a>&gt; for supported platforms. </p>
<p> Entware-ng comes with a precompiled 5.24.1 (June 2017) that allowes building shared <font SIZE="-1">XS</font> code. Note that this installation does <code>not</code> use a site_perl folder. The available <tt>&quot;cpan&quot;</tt> works. If all required development packages are installed too, also for <font SIZE="-1">XS.</font></p>
<h3>Compiling Perl 5</h3>
<p> When the build environment has been set up, building and testing Perl is straightforward. The only thing you need to do is download the sources as usual, and add a file Policy.sh as follows: </p>
<pre><code>
#Administrivia.
perladmin = "your.email [at] goes.here"
#Install Perl in a tree in / opt / perl instead of / opt / bin.
    prefix = / opt / perl
#Select the compiler.Note that there is no 'cc' alias or link.
                         cc = gcc
#Build flags.
                 ccflags = "-DDEBUGGING"
#Library and include paths.
    libpth = "/lib" locincpth = "/opt/include" loclibpth = "/lib"
</code></pre>
<p> You may want to create the destination directory and give it the right permissions before installing, thus eliminating the need to build Perl as a super user. </p>
<p> In the directory where you unpacked the sources, issue the familiar commands: </p>
<pre>
  ./Configure -des
  make
  make test
  make install
</pre>
<h3>Known problems</h3>
<p> <i>Configure</i> </p>
<p> No known problems yet </p>
<p> <i>Build</i></p>
<dl>
<dt>Error message &quot;No error definitions found&quot;.</p>
<dd> This error is generated when it is not possible to find the local definitions for error codes, due to the uncommon structure of the Synology file system. </p>
<p> This error was fixed in the Perl development git for version 5.19, commit 7a8f1212e5482613c8a5b0402528e3105b26ff24.</dl>
<p> <i>Failing tests</i></p>
<dl>
<dt><i>ext/DynaLoader/t/DynaLoader.t</i></p>
<dd> One subtest fails due to the uncommon structure of the Synology file system. The file <i>/lib/glibc.so</i> is missing. </p>
<p> <font SIZE="-1"><code>WARNING:</code></font> Do not symlink <i>/lib/glibc.so.6</i> to <i>/lib/glibc.so</i> or some system components will start to fail.</dl>
<h3>Smoke testing Perl 5</h3>
<p> If building completes successfully, you can set up smoke testing as described in the Test::Smoke documentation. </p>
<p> For smoke testing you need a running Perl. You can either install the Synology supplied package for Perl 5.8.6, or build and install your own, much more recent version. </p>
<p> Note that I could not run successful smokes when initiated by the Synology Task Scheduler. I resorted to initiating the smokes via a cron job run on another system, using ssh: </p>
<pre>
  ssh nas1 wrk/Test-Smoke/smoke/smokecurrent.sh
</pre>
<p> <i>Local patches</i> </p>
<p> When local patches are applied with smoke testing, the test driver will automatically request regeneration of certain tables after the patches are applied. The Synology supplied Perl 5.8.6 (at least on the <font SIZE="-1">DS413</font>) <code>is </code><font SIZE="-1"><code>NOT</code></font><code> capable</code> of generating these tables. It will generate opcodes with bogus values, causing the build to fail. </p>
<p> You can prevent regeneration by adding the setting </p>
<pre>
  'flags' =&gt; 0,
</pre>
<p> to the smoke config, or by adding another patch that inserts </p>
<pre><code>
  exit 0 if $] == 5.008006;
</code></pre>
<p> in the beginning of the <tt>&quot;regen.pl&quot;</tt> program.</p>
<h3>Adding libraries</h3>
<p> The above procedure describes a basic environment and hence results in a basic Perl. If you want to add additional libraries to Perl, you may need some extra settings. </p>
<p> For example, the basic Perl does not have any of the <font SIZE="-1">DB</font> libraries (db, dbm, ndbm, gdsm). You can add these using iPKGui, however, you need to set environment variable <font SIZE="-1">LD_LIBRARY_PATH</font> to the appropriate value: </p>
<pre>
  LD_LIBRARY_PATH=/lib:/opt/lib
  export LD_LIBRARY_PATH
</pre>
<p> This setting needs to be in effect while Perl is built, but also when the programs are run.</p>
<h2>REVISION</h2>
<p> June 2017, for Synology <font SIZE="-1">DSM 5.1.5022</font> and <font SIZE="-1">DSM 6.1-15101-4.</font></p>
<h2>AUTHOR</h2>
<p> Johan Vromans &lt;jvromans [at] squirrel.nl&gt; H. Merijn Brand &lt;h.m.brand [at] xs4all.nl&gt; </p>
<h2>Index</h2>
