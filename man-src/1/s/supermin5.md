---
title: "supermin5(1)"
name: "supermin5"
section: "1"
letter: "s"
url: "/docs/linux/man/1-supermin5/"
description: "supermin – Tool for creating and building supermin appliances"
---

<h2 class="name">NAME</h2>
<p> supermin &#8211; Tool for creating and building supermin appliances </p>
<h2>SYNOPSIS</h2>
<pre><code>
supermin-- prepare - o OUTPUTDIR PACKAGE[PACKAGE...] supermin-- build - o OUTPUTDIR - f chroot | ext2 INPUT[INPUT...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Supermin is a tool for building supermin appliances. These are tiny appliances (similar to virtual machines), usually around 100KB in size, which get fully instantiated on-the-fly in a fraction of a second when you need to boot one of them. </p>
<p> This program used to be called febootstrap. This manual page documents supermin 5.x which is a complete rewrite and quite different from febootstrap 2.x. If you are looking for the febootstrap 2.x tools, then this is not the right place.</p>
<h3><font SIZE="-1">BASIC OPERATION</font></h3>
<p> The supermin tool can be used in two modes, <code>preparing</code> a tiny supermin appliance, which is done on a build system. And <code>building</code>, which takes the supermin appliance and constructs a full, bootable appliance, which is done on the end user&#8217;s system. </p>
<p> Supermin does not need to be run as root, and generally <i>should not</i> be run as root. It does not affect the host system or the packages installed on the host system. </p>
<p> <i></i><font SIZE="-1"><i>PREPARE MODE</i></font><i></i> </p>
<p> <i>&#8211;prepare</i> creates the tiny supermin appliance in the given output directory. You give it a list of packages that you want installed, and supermin will automatically find the dependencies. The list of packages has to be installed on the host machine. </p>
<p> For example: </p>
<pre>
 supermin --prepare bash coreutils -o supermin.d
</pre>
<p> creates a supermin appliance containing the packages <tt>&quot;bash&quot;</tt> and <tt>&quot;coreutils&quot;</tt>. Specifically, it creates some files in directory <i>supermin.d</i>. This directory <i>is</i> the supermin appliance. (See &#8220;<font SIZE="-1">SUPERMIN APPLIANCES&#8221;</font> below). </p>
<p> It is intended that the <i>&#8211;prepare</i> step is done on a central build machine, and the supermin appliance is distributed to end users (which is easy because supermin appliances are so small). </p>
<p> <i></i><font SIZE="-1"><i>BUILD MODE</i></font><i></i> </p>
<p> <i>&#8211;build</i> (previously a separate program called <tt>&quot;supermin-helper&quot;</tt>) builds the full appliance from the supermin appliance: </p>
<pre>
 supermin --build --format ext2 supermin.d -o appliance.d
</pre>
<p> This will create files called <i>appliance.d/kernel</i>, <i>appliance.d/root</i> etc, which is the full sized bootable appliance. </p>
<p> It is intended that the <i>&#8211;build</i> step is done on the end user&#8217;s machine at the last second before the appliance is needed. The packages in the supermin appliance (those specified when the supermin appliance was prepared) must be installed on the end user&#8217;s machine. </p>
<p> Build and cache </p>
<p> Typically you want to rebuild the appliance on the end user machine only on demand. Supermin has some extra options to make this easy: </p>
<pre><code>
supermin-- build-- if - newer-- lock / run / user /`id - u`/ supermin.lock-- format ext2 supermin.d - o appliance.d
</code></pre>
<p> If multiple programs run this command in parallel, the instances will wait on the lock file. The full appliance only gets rebuilt if it doesn&#8217;t exist or if it is older than the input files and host package database. </p>
<p> Note that the lock file <code>must not</code> be stored inside the <i>-o</i> directory. </p>
<p> <i></i><font SIZE="-1"><i>PACKAGES</i></font><i></i> </p>
<p> By &#8220;package&#8221; we mean the <font SIZE="-1">RPM,</font> Debian, (etc.) package, eg. <tt>&quot;coreutils&quot;</tt>, <tt>&quot;perl&quot;</tt>. </p>
<p> In all cases supermin can only build a supermin appliance which is identical in distro, version and architecture to the host. It does <i>not</i> do cross-builds.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display brief command line usage, and exit.</p>
<dt><code>&#8211;build</code></p>
<dd> Build the full appliance from the supermin appliance. This used to be a separate program called <tt>&quot;supermin-helper&quot;</tt>.</p>
<dt><code>&#8211;copy-kernel</code></p>
<dd> (<i>&#8211;build</i> mode only) </p>
<p> Copy the kernel (and device tree, if created) instead of symlinking to the kernel in <i>/boot</i>. </p>
<p> This is fractionally slower, but is necessary if you want to change the permissions or SELinux label on the kernel or device tree.</p>
<dt><code>&#8211;dtb</code> <font SIZE="-1">WILDCARD</font></p>
<dd> (<i>&#8211;build</i> mode only) </p>
<p> If specified, search for a device tree which is compatible with the selected kernel and the name of which matches the given wildcard. You can use a wildcard such as <tt>&quot;vexpress-*a9*.dtb&quot;</tt> which would match <i>vexpress-v2p-ca9.dtb</i>. </p>
<p> Notes:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> You may need to quote the wildcard to prevent it from being expanded by your shell.</p>
<dt>&bull;</p>
<dd> If no <i>&#8211;dtb</i> option is given, no device tree will be looked for.</p>
<dt>&bull;</p>
<dd> You only need a device tree on architectures such as <font SIZE="-1">ARM</font> and PowerPC which use them. On other architectures, don&#8217;t use this option.</p>
<dt>&bull;</p>
<dd> If you use this option and no compatible device tree can be found, supermin will exit with an error.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-f</code> <font SIZE="-1">FORMAT</font></p>
<dd>
<dt><code>&#8211;format</code> <font SIZE="-1">FORMAT</font></p>
<dd> (<i>&#8211;build</i> mode only) </p>
<p> Select the output format for the full appliance. </p>
<p> There is no default. When using <i>&#8211;build</i> you must specify the <i>&#8211;format</i> option. </p>
<p> Possible formats are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>chroot</p>
<dd> A directory tree in the host filesystem. </p>
<p> The filesystem tree is written to <i></i><font SIZE="-1"><i>OUTPUTDIR</i></font><i></i> (ie. the <i>-o</i> option). </p>
<p> This is called a <tt>&quot;chroot&quot;</tt> because you could literally <i><a href="/docs/linux/man/1-chroot/">chroot</a></i>(1) into this directory afterwards, although it&#8217;s a better idea to use a container technology (<font SIZE="-1">LXC,</font> etc.). </p>
<p> No kernel, initrd or dtb is generated in this mode because it is assumed that you will be running the appliance using the host kernel.</p>
<dt>ext2</p>
<dd> An ext2 filesystem disk image. </p>
<p> The output kernel is written to <i>OUTPUTDIR/kernel</i>, the device tree (if using) to <i>OUTPUTDIR/dtb</i>, a small initramfs which can mount the appliance to <i>OUTPUTDIR/initrd</i>, and the ext2 filesystem image to <i>OUTPUTDIR/root</i>. (Where <i></i><font SIZE="-1"><i>OUTPUTDIR</i></font><i></i> is specified by the <i>-o</i> option). </p>
<p> The filesystem (<i>OUTPUTDIR/root</i>) has a default size of 4 <font SIZE="-1">GB </font>(see also the <i>&#8211;size</i> option).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;host-cpu</code> <font SIZE="-1">CPU</font></p>
<dd> (<i>&#8211;build</i> mode only) </p>
<p> Specify the host <font SIZE="-1">CPU </font>(eg. <tt>&quot;i686&quot;</tt>, <tt>&quot;x86_64&quot;</tt>). This is used as a substring match when searching for compatible kernels. If not specified, it defaults to the host <font SIZE="-1">CPU</font> that supermin was compiled on.</p>
<dt><code>&#8211;if-newer</code></p>
<dd> (<i>&#8211;build</i> mode only) </p>
<p> The output directory is checked and it is <i>not</i> rebuilt unless it needs to be. </p>
<p> This is done by consulting the dates of the host package database (<i>/var/lib/rpm</i> etc), the input supermin files, and the output directory. The operation is only carried out if either the host package database or the input supermin files are newer than the output directory. </p>
<p> See also <i>&#8211;lock</i> below.</p>
<dt><code>&quot;&#8211;include-packagelist</code></p>
<dd> (<i>&#8211;build</i> mode only) </p>
<p> Add a <i>/packagelist</i> file inside the generated chroot or ext2 filesystem, containing a sorted list of all the packages used to build the appliance. </p>
<p> Mostly useful for debugging, as it makes it easier to find out e.g. which version of a package was copied in the appliance.</p>
<dt><code>&#8211;list-drivers</code></p>
<dd> List the package manager drivers compiled into supermin, and whether the corresponding package manager is detected on the current system.</p>
<dt><code>&#8211;lock</code> <font SIZE="-1">LOCKFILE</font></p>
<dd> (<i>&#8211;build</i> mode only) </p>
<p> If multiple parallel runs of supermin need to build a full appliance, then you can use the <i>&#8211;lock</i> option to ensure they do not stomp on each other. </p>
<p> The lock file is used to provide mutual exclusion so only one instance of supermin will run at a time. </p>
<p> Note that the lock file <code>must not</code> be stored inside the output directory.</p>
<dt><code>-o</code> <font SIZE="-1">OUTPUTDIR</font></p>
<dd> Select the output directory. </p>
<p> When using <i>&#8211;prepare</i>, this is the directory where the supermin appliance will be written. When using <i>&#8211;build</i>, this is the directory where the full appliance, kernel etc will be written. </p>
<p> <code>Any previous contents of the output directory are deleted</code>, and a new output directory is created. </p>
<p> The output directory is created (nearly) atomically by constructing a temporary directory called something like <i></i><font SIZE="-1"><i>OUTPUTDIR</i></font><i>.abc543</i>, then renaming the old output directory (if present) and deleting it, and then renaming the temporary directory to <i></i><font SIZE="-1"><i>OUTPUTDIR</i></font><i></i>. By combining this option with <i>&#8211;lock</i> you can ensure that multiple parallel runs of supermin do not conflict with each other.</p>
<dt><code>&#8211;packager-config</code> <font SIZE="-1">CONFIGFILE</font></p>
<dd> (<i>&#8211;prepare</i> mode only) </p>
<p> Set the configuration file for the package manager. This allows you to specify alternate software repositories. </p>
<p> For ArchLinux, this sets the pacman configuration file (default <i>/etc/pacman.conf</i>). See <i><a href="/docs/linux/man/5-pacman-conf/">pacman.conf</a></i>(5). </p>
<p> For Yum/RPM distributions, this sets the yum configuration file (default <i>/etc/yum.conf</i>). See <i><a href="/docs/linux/man/5-yum-conf/">yum.conf</a></i>(5).</p>
<dt><code>&#8211;prepare</code></p>
<dd> Prepare the supermin appliance.</p>
<dt><code>&#8211;use-installed</code></p>
<dd> (<i>&#8211;prepare</i> mode only) </p>
<p> If packages are already installed, use the contents (from the local filesystem) instead of downloading them. </p>
<p> Note that this can cause malformed appliances if local files have been changed from what was originally in the package. This is particularly a problem for configuration files. </p>
<p> However this option is useful in some controlled situations: for example when using supermin inside a freshly installed chroot, or if you have no network access during the build.</p>
<dt><code>&#8211;size</code> <font SIZE="-1">SIZE</font></p>
<dd> (<i>&#8211;build</i> mode only) </p>
<p> Select the size of the output ext2 filesystem, where the size can be specified using common names such as <tt>&quot;32G&quot;</tt> (32 gigabytes) etc. </p>
<p> If the size is not specified, a default size of 4 <font SIZE="-1">GB</font> is used. </p>
<p> To specify size in bytes, the number must be followed by the lowercase letter <i>b</i>, eg: <tt>&quot;--size 10737418240b&quot;</tt>.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose messages. </p>
<p> You can give this option multiple times to enable even more messages:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>-v</i></p>
<dd> Debugging of overall stages.</p>
<dt><i>-v -v</i></p>
<dd> Detailed information within each stage.</p>
<dt><i>-v -v -v</i></p>
<dd> Massive amounts of debugging (far too much for normal use, but good if you are trying to diagnose a bug in supermin).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Print the package name and version number, and exit.</dl>
<h2>SUPERMIN APPLIANCES</h2>
<p> Supermin appliances consist of just enough information to be able to build an appliance containing the same operating system (Linux version, distro, release etc) as the host <font SIZE="-1">OS. </font> Since the host and appliance share many common files such as <i>/bin/bash</i> and <i>/lib/libc.so</i> there is no reason to ship these files in the appliance. They can simply be read from the host on demand when the appliance is launched. Therefore to save space we just store the names of the packages we want from the host, and copy those in (plus dependencies) at build time. </p>
<p> There are some files which cannot just be copied from the host in this way. These include configuration files which the host admin might have edited. So along with the list of host files, we also store a skeleton base image which contains these files and the outline directory structure. </p>
<p> Therefore the supermin appliance normally consists of at least two control files (<i>packages</i> and <i>base.tar.gz</i>).</p>
<dl>
<dt><i>packages</i></p>
<dd> The list of packages to be copied from the host. Dependencies are resolved automatically. </p>
<p> The file is plain text, one package name per line.</p>
<dt><i>base.tar</i></p>
<dd>
<dt><i>base.tar.gz</i></p>
<dd> This tar file (which may be compressed) contains the skeleton filesystem. Mostly it contains directories and a few configuration files. </p>
<p> All paths in the tar file should be relative to the root directory of the appliance.</p>
<dt><i>hostfiles</i></p>
<dd> Any other files that are to be copied from the host. This is a plain text file with one pathname per line. </p>
<p> Paths can contain wildcards, which are expanded when the appliance is created, eg: </p>
<pre>
 /etc/yum.repos.d/*.repo
</pre>
<p> would copy all of the <i>*.repo</i> files into the appliance. </p>
<p> Each pathname in the file should start with a <tt>&quot;/&quot;</tt> character. </p>
<p> Supermin itself does not create hostfiles (although before version 5, this was the main mechanism used to create the full appliance). However you may drop one or more of these files into the supermin appliance directory if you want to copy random unpackaged files into the full appliance.</p>
<dt><i>excludefiles</i></p>
<dd> A list of filenames, directory names, or wildcards prefixed by <tt>&quot;-&quot;</tt> which are excluded from the final appliance. </p>
<p> This is rather brutal since it just removes things, potentially breaking packages. However it can be used as a convenient way to minimize the size of the final appliance. </p>
<p> Supermin itself does not create excludefiles. However you may drop one of more of these files into the supermin appliance directory to stop packaged files from being copied into the full appliance.</dl>
<p> Note that the names above are just suggestions. You can use any names you want, as supermin detects the contents of each file when it reconstructs the appliance. You can also have multiple of each type of file.</p>
<h3><font SIZE="-1">RECONSTRUCTING THE APPLIANCE</font></h3>
<p> The separate mode <tt>&quot;supermin --build&quot;</tt> is used to reconstruct an appliance from the supermin appliance files. </p>
<p> This program in fact iterates recursively over the files and directories passed to it. A common layout could look like this: </p>
<pre>
 supermin.d/
 supermin.d/base.tar.gz
 supermin.d/extra.tar.gz
 supermin.d/packages
 supermin.d/zz-hostfiles
</pre>
<p> In this way extra files can be added to the appliance just by creating another tar file (<i>extra.tar.gz</i> in the example above) and dropping it into the directory, and additional host files can be added (<i>zz-hostfiles</i> in the example above). When the appliance is constructed, the extra files will appear in the appliance.</p>
<h3><font SIZE="-1">MINIMIZING THE SUPERMIN APPLIANCE</font></h3>
<p> You may want to &#8220;minimize&#8221; the supermin appliance in order to save time and space when it is instantiated. Typically you might want to remove documentation, info files, man pages and locales. </p>
<p> You can do this by creating an excludefiles that lists files, directories or wildcards that you don&#8217;t want to include. They are skipped when the full appliance is built. </p>
<pre>
 -/boot/*
 -/lib/modules/*
 -/usr/share/doc/*
 -/usr/share/info/*
 -/usr/share/man/*
</pre>
<p> Be careful what you remove because files may be necessary for correct operation of the appliance.</p>
<h3><font SIZE="-1">KERNEL AND KERNEL MODULES</font></h3>
<p> Usually the kernel and kernel modules are <i>not</i> included in the supermin appliance. </p>
<p> When the full appliance is built, the kernel modules from the host are copied in, and it is booted using the host kernel. </p>
<p> <i></i><font SIZE="-1"><i>USING A CUSTOM KERNEL AND KERNEL MODULES</i></font><i></i> </p>
<p> Supermin is able to choose the best host kernel available to boot the appliance. However you can override this by setting environment variables (see &#8220;<font SIZE="-1">ENVIRONMENT VARIABLES&#8221;</font> below). </p>
<p> If you build a custom kernel (eg. by compiling Linux from source), then you should do something like this: </p>
<pre>
 mkdir /tmp/kmods
 make bzImage
 make modules
 make modules_install INSTALL_MOD_PATH=/tmp/kmods
 
 export SUPERMIN_KERNEL=/path/to/linux.git/arch/x86/boot/bzImage
 export SUPERMIN_MODULES=/tmp/kmods/lib/modules/3.xx.yy
 
 supermin --build -f ext2 [etc]
</pre>
<h3><font SIZE="-1">ENFORCING AVAILABILITY OF PACKAGES</font></h3>
<p> Supermin builds the appliance by copying in the packages listed in <i>packages</i>. For this to work those packages must be available. We usually enforce this by adding requirements (eg. <font SIZE="-1">RPM </font><tt>&quot;Requires:&quot;</tt> lines) on the package that uses the supermin appliance, so that package cannot be installed without pulling in the dependent packages and thus making sure the packages are installed for supermin to use.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><font SIZE="-1">SUPERMIN_KERNEL</font></p>
<dd> If this environment variable is set, then automatic selection of the kernel is bypassed and this kernel is used. </p>
<p> The environment variable should point to a kernel file, eg. <i>/boot/vmlinuz-3.0.x86_64</i></p>
<dt><font SIZE="-1">SUPERMIN_MODULES</font></p>
<dd> This specifies the kernel modules directory to use. </p>
<p> The environment variable should point to a module directory, eg. <i>/lib/modules/3.0.x86_64/</i></p>
<dt><font SIZE="-1">SUPERMIN_DTB</font></p>
<dd> Force the given device tree file to be used.</p>
<dt><font SIZE="-1">SUPERMIN_KERNEL_VERSION</font></p>
<dd> On non-x86 architectures, you may need to set this environment variable if supermin cannot determine the kernel version of <tt>&quot;SUPERMIN_KERNEL&quot;</tt> just by looking at the file.</dl>
<h2>SEE ALSO</h2>
<p> &lt;<a rel="nofollow" href="http://people.redhat.com/~rjones/supermin/">http://people.redhat.com/~rjones/supermin/</a>&gt;, <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), &lt;<a rel="nofollow" href="http://libguestfs.org/">http://libguestfs.org/</a>&gt;.</p>
<h2>AUTHORS</h2>
<dl>
<dt>&bull;</p>
<dd> Richard W.M. Jones &lt;<a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a>&gt;</p>
<dt>&bull;</p>
<dd> Matthew Booth</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2014 Red Hat Inc. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font> </p>
<h2>Index</h2>
<dt><a href="#lbAF">OPTIONS</a></p>
<dd>
<dt><a href="#lbAG">SUPERMIN APPLIANCES</a></p>
<dd>
<dt><a href="#lbAL">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAM">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAN">AUTHORS</a></p>
<dd>
<dt><a href="#lbAO">COPYRIGHT</a></p>
<dd></dl>
