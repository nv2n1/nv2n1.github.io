---
title: "supermin(8)"
name: "supermin"
section: "8"
letter: "s"
url: "/docs/linux/man/8-supermin/"
description: "supermin – Tool for creating supermin appliances"
---

<p>supermin &#8211; Tool for creating supermin appliances</p>
<h2>Synopsis</h2>
<pre> supermin [-o OUTPUTDIR] --names LIST OF PKGS ...
 supermin [-o OUTPUTDIR] PKG FILE NAMES ...</pre>
<h2>Description</h2>
<p>Supermin is a tool for building supermin appliances. These are tiny appliances (similar to virtual machines), usually around 100KB in size, which get fully instantiated on-the-fly in a fraction of a second when you need to boot one of them. </p>
<p> Originally &#8220;fe&#8221; in &#8220;febootstrap&#8221; stood for &#8220;Fedora&#8221;, but this tool is now distro-independent and can build supermin appliances for several popular Linux distros, and adding support for others is reasonably easy. For this reason, starting with version 4, we have renamed the tool &#8220;supermin&#8221;. </p>
<p> Note that this manual page documents supermin 4.x which is a complete rewrite and quite different from febootstrap 2.x. If you are looking for the febootstrap 2.x tools, then this is not the right place.</p>
<h3><font SIZE="-1">BASIC OPERATION</font></h3>
<p>There are two modes for using supermin. With the <i>&#8211;names</i> parameter, supermin takes a list of package names and creates a supermin appliance containing those packages and all dependencies that those packages require. In this mode supermin usually needs network access because it may need to consult package repositories in order to work out dependencies and download packages. </p>
<p> Without <i>&#8211;names</i>, supermin takes a list of packages (ie. filenames of locally available packages). This package set must be complete and consistent with no dependencies outside the set of packages you provide. In this mode supermin does not require any network access. It works by looking at the package files themselves. </p>
<p> By &#8220;package&#8221; we mean the <font SIZE="-1">RPM, DEB, </font>(etc.) package. A package name might be the fully qualified name (eg. <tt>&quot;coreutils-8.5-7.fc14.x86_64&quot;</tt>) or some abbreviation (eg. <tt>&quot;coreutils&quot;</tt>). The precise format of the name and what abbreviations are allowed depends on the package manager. </p>
<p> The supermin appliance that supermin writes consists of two files called <tt>&quot;hostfiles&quot;</tt> and <tt>&quot;base.img&quot;</tt> (see &#8220;<font SIZE="-1">SUPERMIN APPLIANCES&#8221;</font> below). By default these are written to the current directory. If you specify the <i>-o </i><font SIZE="-1"><i>OUTPUTDIR</i></font><i></i> option then these files are written to the named directory instead (traditionally this directory is named <tt>&quot;supermin.d&quot;</tt> but you can call it whatever you want). </p>
<p> In all cases supermin can only build a supermin appliance which is identical in distro, version and architecture to the host. It does <i>not</i> do cross-builds.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Display brief command line usage, and exit.</p>
<dt><code>&#8211;exclude </code><font SIZE="-1"><code>REGEXP</code></font></p>
<dd>After doing dependency resolution, exclude packages which match the regular expression. </p>
<p> This option is only used with <i>&#8211;names</i>, and it can be given multiple times on the command line.</p>
<dt><code>&#8211;names</code></p>
<dd>Provide a list of package names, instead of providing packages directly. In this mode supermin may require network access. See &#8220;<font SIZE="-1">BASIC OPERATION&#8221;</font> above.</p>
<dt><code>&#8211;no-warnings</code></p>
<dd>Don&#8217;t print warnings about packaging problems.</p>
<dt><code>-o outputdir</code></p>
<dd>Select the output directory where the two supermin appliance files are written (<tt>&quot;hostfiles&quot;</tt> and <tt>&quot;base.img&quot;</tt>). The default directory is the current directory. Note that if this files exist already in the output directory then they will be overwritten.</p>
<dt><code>&#8211;packager-config </code><font SIZE="-1"><code>CONFIGFILE</code></font></p>
<dd>Set the configuration file for the package manager. This allows you to specify alternate software repositories. </p>
<p> For ArchLinux, this sets the pacman configuration file (default <tt>&quot;/etc/pacman.conf&quot;</tt>). See <i><a href="/docs/linux/man/5-pacman-conf/">pacman.conf</a></i>(5). </p>
<p> For Yum/RPM distributions, this sets the yum configuration file (default <tt>&quot;/etc/yum.conf&quot;</tt>). See <i><a href="/docs/linux/man/5-yum-conf/">yum.conf</a></i>(5).</p>
<dt><code>&#8211;save-temps</code></p>
<dd>Don&#8217;t remove temporary files and directories on exit. This is useful for debugging.</p>
<dt><code>&#8211;use-installed</code></p>
<dd>If packages are already installed, use the contents (from the local filesystem) instead of downloading them. </p>
<p> Note that this can cause malformed appliances if local files have been changed from what was originally in the package. This is particularly a problem for configuration files. </p>
<p> However this option is useful in some controlled situations: for example when using supermin inside a freshly installed chroot.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd>Enable verbose messages.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>Print the package name and version number, and exit.</p>
<dt><code>&#8211;yum-config </code><font SIZE="-1"><code>CONFIGFILE</code></font></p>
<dd>This is a deprecated alias for <i>&#8211;packager-config </i><font SIZE="-1"><i>CONFIGFILE</i></font><i></i>.</dl>
<h2>Supermin Appliances</h2>
<p>Supermin appliances consist of just enough information to be able to build an appliance containing the same operating system (Linux version, distro, release etc) as the host <font SIZE="-1">OS. </font> Since the host and appliance share many common files such as <tt>&quot;/bin/bash&quot;</tt> and <tt>&quot;/lib/libc.so&quot;</tt> there is no reason to ship these files in the appliance. They can simply be read from the host on demand when the appliance is launched. Therefore to save space we just store the names of the host files that we want. </p>
<p> There are some files which cannot just be copied from the host in this way. These include configuration files which the host admin might have edited. So along with the list of host files, we also store a skeleton base image which contains these files and the outline directory structure. </p>
<p> Therefore the supermin appliance normally consists of at least two control files:</p>
<dl>
<dt><code>hostfiles</code></p>
<dd>The list of files that are to be copied from the host. This is a plain text file with one pathname per line. Directories are included in this file. </p>
<p> Paths can contain wildcards, which are expanded when the appliance is created, eg: </p>
<pre> /etc/yum.repos.d/*.repo</pre>
<p>would copy all of the <tt>&quot;*.repo&quot;</tt> files into the appliance. </p>
<p> Each pathname in the file should start with a <tt>&quot;/&quot;</tt> character. (In older versions of febootstrap, paths started with <tt>&quot;./&quot;</tt> and were relative to the root directory, but you should not do that in new files).</p>
<dt><code>base.img</code></p>
<dd>This uncompressed cpio file contains the skeleton filesystem. Mostly it contains directories and a few configuration files. </p>
<p> All paths in the cpio file should be relative to the root directory of the appliance. </p>
<p> Note that unlike <tt>&quot;hostfiles&quot;</tt>, paths and directories in the base image don&#8217;t need to have any relationship to the host filesystem.</p>
<dt><code>base.img.gz</code></p>
<dd>Since supermin ≥ 4.1.4, any cpio image files may be gzip-compressed to save disk space. <tt>&quot;hostfiles&quot;</tt> cannot be compressed. The supermin program won&#8217;t create these files. You need to compress the output yourself, eg by doing: </p>
<pre> gzip -9 supermin.d/*.img</pre>
</dl>
<h3><font SIZE="-1">RECONSTRUCTING THE APPLIANCE</font></h3>
<p>The separate tool <i><a href="/docs/linux/man/8-supermin-helper/">supermin-helper</a></i>(8) is used to reconstruct an appliance from the hostfiles and base image files. </p>
<p> This program in fact iterates recursively over the files and directories passed to it. A common layout is: </p>
<pre> supermin.d/
 supermin.d/base.img
 supermin.d/extra.img
 supermin.d/hostfiles</pre>
<p>and then invoking supermin-helper with just the <tt>&quot;supermin.d&quot;</tt> directory path as an argument. </p>
<p> In this way extra files can be added to the appliance just by creating another cpio file (<tt>&quot;extra.img&quot;</tt> in the example above) and dropping it into the directory. When the appliance is constructed, the extra files will appear in the appliance. </p>
<p> <i></i><font SIZE="-1"><i>DIRECTORIES BEFORE FILES</i></font><i></i> </p>
<p> In order for supermin-helper to run quickly, it does not know how to create directories automatically. Inside hostfiles and the cpio files, directories must be specified before any files that they contain. For example: </p>
<pre> /usr
 /usr/sbin
 /usr/sbin/serviced</pre>
<p>It is fine to list the same directory name multiple times. </p>
<p> <i></i><font SIZE="-1"><i>LEXICOGRAPHICAL ORDER</i></font><i></i> </p>
<p> supermin-helper visits the supermin control files in lexicographical order. Thus in the example above, in the order <tt>&quot;base.img&quot;</tt> -&gt; <tt>&quot;extra.img&quot;</tt> -&gt; <tt>&quot;hostfiles&quot;</tt>. </p>
<p> This has an important effect: files contained in later cpio files overwrite earlier files, and directories do not need to be specified if they have already been created in earlier control files. </p>
<p> <i></i><font SIZE="-1"><i>EXAMPLE OF CREATING EXTRA CPIO FILE</i></font><i></i> </p>
<p> You can create a file like <tt>&quot;extra.img&quot;</tt> very easily using a shell snippet similar to this one: </p>
<pre> cd $tmpdir
 mkdir -p usr/sbin
 cp /path/to/serviced usr/sbin/
 echo -e &quot;usr
usr/sbin
usr/sbin/serviced&quot; |
 cpio --quiet -o -H newc &gt; extra.img
 rm -rf usr</pre>
<p>Notice how we instruct cpio to create intermediate directories.</p>
<h3><font SIZE="-1">MINIMIZING THE SUPERMIN APPLIANCE</font></h3>
<p>You may want to &#8220;minimize&#8221; the supermin appliance in order to save time and space when it is instantiated. Typically you might want to remove documentation, info files, man pages and locales. We used to provide a separate tool called <tt>&quot;febootstrap-minimize&quot;</tt> for this purpose, but it is no longer provided. Instead you can post-process <tt>&quot;hostfiles&quot;</tt> yourself to remove any files or directories that you don&#8217;t want (by removing lines from the file). Be careful what you remove because files may be necessary for correct operation of the appliance. </p>
<p> For example: </p>
<pre> &lt; supermin.d/hostfiles \
 grep -v '^/usr/share/man/' |
 grep -v '^/usr/share/doc/' |
 grep -v '^/usr/share/info/' &gt; supermin.d/hostfiles-t
 mv supermin.d/hostfiles-t supermin.d/hostfiles</pre>
<h3><font SIZE="-1">KERNEL AND KERNEL MODULES</font></h3>
<p>Usually the kernel and kernel modules are <i>not</i> included in the supermin appliance. When the appliance is instantiated, the kernel modules from the host kernel are copied in, and it is booted using the host kernel. </p>
<p> supermin-helper is able to choose the best host kernel available to boot the appliance. Users can override this by setting environment variables (see <i><a href="/docs/linux/man/8-supermin-helper/">supermin-helper</a></i>(8)).</p>
<h3><font SIZE="-1">BOOTING AND CACHING THE SUPERMIN APPLIANCE</font></h3>
<p>For fastest boot times you should cache the output of supermin-helper. See the libguestfs source file <tt>&quot;src/appliance.c&quot;</tt> for an example of how this is done.</p>
<h3><font SIZE="-1">ENFORCING AVAILABILITY OF HOSTFILES</font></h3>
<p>supermin-helper builds the appliance by copying in host files as listed in <tt>&quot;hostfiles&quot;</tt>. For this to work those host files must be available. We usually enforce this by adding requirements (eg. <font SIZE="-1">RPM </font><tt>&quot;Requires:&quot;</tt> lines) on the package that uses the supermin appliance, so that package cannot be installed without pulling in the dependent packages and thus making sure the host files are available.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-supermin-helper/">supermin-helper</a></i>(8), &lt;<a rel="nofollow" href="http://people.redhat.com/~rjones/supermin/">http://people.redhat.com/~rjones/supermin/</a>&gt;, <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), &lt;<a rel="nofollow" href="http://libguestfs.org/">http://libguestfs.org/</a>&gt;.</p>
<h2>Authors</h2>
<dl>
<dt>&bull;</p>
<dd>Richard W.M. Jones &lt;<a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a>&gt;</p>
<dt>&bull;</p>
<dd>Matthew Booth mbooth [at] redhat.com</dl>
<h2>Copyright</h2>
<p>Copyright (C) 2009-2011 Red Hat Inc. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font></p>
