---
title: "make-redir(1)"
name: "make-redir"
section: "1"
letter: "m"
url: "/docs/linux/man/1-make-redir/"
description: "make-redir – run \"make\" but automatically redirect its results to DESTDIR"
---

<h2>NAME</h2>
<p> make-redir &#8211; run &quot;make&quot; but automatically redirect its results to DESTDIR</p>
<h2>SYNOPSIS</h2>
<p> <code>make-redir</code> [<i>MAKE_ARGUMENT*</i>]&#8230;[<i>install</i>] </p>
<dl>
<dt>
<dd> * DESTDIR=<i>directory</i> and -k/&#8211;keep-going are especially common.</dl>
<h2>DESCRIPTION</h2>
<p> The make-redir program runs &quot;make&quot; in a way that redirects file installations to descend from the $DESTDIR directory, even if the provided makefile doesn&#8217;t natively support $DESTDIR. In most cases, simply replace &quot;make install&quot; with &quot;make-redir DESTDIR=<i>directory</i> install&quot; (adding options as necessary). </p>
<p> The make-redir program attempts to solve a common problem for packagers of software and for users who directly install source code: Inadequate DESTDIR support. Software is typically installed on Unix/Linux from a source code package by typing &quot;make install&quot;. Historically, this script would write directly to privileged directories to perform the installation (e.g., /usr/bin), or at least to a directory that merged all installed files (e.g., $HOME/bin). However, packagers of software using most modern packaging systems (such as .rpm and .deb) instead require that files be written to some intermediate directory, even though they will be run from a different filesystem location. Similarly, users who directly install source code often use programs such as GNU stow, encap, or toast. These programs install each package in its own separate directory, but work best if the installed programs are invoked through a different directory (which merges the contents of multiple packages, simplifying the PATH and supporting plug-ins). Thus, for both many packagers of software and for many users who directly install source code, a program should be installed in one directory, yet actually be run from a different directory. This is easy to do if the installation script supports the &quot;DESTDIR convention&quot;; simply run &quot;make DESTDIR=<i>something</i> install&quot;, which would install the files descending from DESTDIR, even though the files are configured to run without the DESTDIR prefix. Unfortunately, many source packages don&#8217;t support the DESTDIR convention. </p>
<p> The auto-destdir tools &quot;make-redir&quot; and &quot;run-redir&quot; will automatically redirect file reads/writes to follow the DESTDIR convention, without requiring any changes to the build files (e.g., a makefile). Attempts to write to directories that are normally root-privileged (such as /usr/bin) will instead be redirected to descend from a designated destination directory. This destination directory is specified by the environment variable REDIR_DESTDIR or DESTDIR, with REDIR_DESTDIR taking precedence. </p>
<p> You should use make-redir (not run-redir) if you are redirecting &quot;make&quot;, because make-redir performs additional helpful actions. If you pass DESTDIR=something as a parameter, it automatically sets the DESTDIR environment variable. The make-redir command also sets the overrides INSTALL=&quot;install -p&quot; CP=&quot;cp -p&quot; MKDIR=&quot;mkdir&quot; MKDIR_P=&quot;mkdir -p&quot; mkdir_p=&quot;mkdir -p&quot; LN=&quot;ln&quot;, so that makefiles with absolute pathnames of common commands will work correctly and preserve timestamps. (Add overrides on the command line if these are not acceptable.) By default make-redir also sets special SHELL and MAKESHELL values, so that even invocations with a full path name (like /bin/cp) will be redirected if they begin a line in a makefile. </p>
<p> Internally, make-redir runs &quot;make&quot; using run-redir; run-redir does the actual file redirection. Use run-redir if you need to redirect file writes without first running &quot;make&quot;. </p>
<p> The auto-destdir tools are designed to &quot;just work&quot; given the limitations described below (in particular, only &quot;wrapped&quot; commands should read/write files that must be redirected). Filenames will not be redirected twice, so it&#8217;s safe to use run-redir and make-redir even with makefiles that do support DESTDIR. If a write is redirected, all parent directories are first automatically created if they exist in the unredirected filesystem. This means that an attempt to &quot;cp&quot; some file to /usr/bin/xyz will create the directory &quot;$DESTDIR/usr/bin&quot; if /usr/bin already exists, then copy the file to &quot;$DESTDIR/usr/bin/xyz&quot;. If a file is being read, a file written inside $DESTDIR will have precedence over a file that isn&#8217;t; this nicely simulates the overwriting of an old file with a new one. Since make-redir and run-redir set the PATH, they will work even if there are many levels of indirection, and even if they use tools other than make (as long as they end up eventually invoking the usual commands such as cp and install). </p>
<p> If the &quot;make install&quot; works except that it uses a few &quot;unwrapped&quot; commands, consider using the &quot;-k&quot; (&quot;&#8211;keep-going&quot;) option, so that make-redir will keep going instead of failing on an error. Then, re-perform the actions that would have failed. Alternatively, you may be able to perform one or two actions &quot;by hand&quot; first, and then invoke make-redir to do the rest. </p>
<p> The programs make-redir and run-redir can be run as root, but in most cases, you should not run them as root. The installation program itself may require root to run (e.g., to set ownership), even if files are written to DESTDIR. If you just want to record permissions (e.g., chown, chmod), consider also using &quot;fakeroot&quot; to record the intended permissions instead of running as root. When creating an rpm package, the permission-setting is typically irrelevant, since in most cases it is the rpm spec file that will ultimately set the permissions. If the permission-setting is irrelevant, you may want to run make-redir as non-root and pass it the &quot;-k&quot; (&quot;&#8211;keep-going&quot;) option so that make will keep going instead of failing on an error. </p>
<p> A file/directory is not redirected if its full pathname begins as a typical user directory (specifically /home/ or /Users/) or temporary directory (/tmp/, /usr/tmp/, /var/tmp/, or /opt/tmp/). A file/directory is redirected if its full pathname begins with a directory name that is normally privileged: /usr/, /etc/, /boot/, /bin*/, /dev/, /lib*/, /opt/, /sbin*/, /selinux/, /srv/, /sys/, and /var/. If neither case applies, it is not redirected. </p>
<p> You can override some values, though few will need to do so. By default, make-redir invokes &quot;make&quot;; this can be changed by setting the environment variable REALMAKE to whatever &quot;make&quot; program should be invoked instead. By default, make-redir sets a special SHELL value (so it can override commands that give full pathnames); this special value does some processing and then invokes /bin/bash. Set the environment variable REALMAKESHELL to the name of the shell to use after doing this filtering if you do not want it to use /bin/bash. You can disable this filtering entirely by setting the make variables SHELL and MAKESHELL on the command line to the name of the shell program to use (e.g., make-redir SHELL=/bin/sh MAKESHELL=/bin/sh); if make can be called recursively, also set the environment variables with the same name. If you do not want any makefile variable overrides, set the environment variable DESTDIR and use &quot;run-redir make &#8230;&quot; instead. </p>
<h2>EXAMPLES</h2>
<p> The following configures, builds, and then &quot;installs&quot; a program. The &quot;installed&quot; files will descend from /tmp/stuff, e.g., directory /tmp/stuff/usr/bin will contain files that were intended to be installed in /usr/bin: </p>
<dl>
<dt>
<dd>
<pre>
 ./configure --prefix=/usr
 make
 make-redir DESTDIR=/tmp/stuff install
</pre>
</dl>
<p> For example, if &quot;cp myprogram&nbsp;<wbr>/usr/bin&quot; is one of the instructions in the makefile for the &quot;install&quot; target, then (presuming /usr/bin exists) it will actually perform the equivalent of:</p>
<dl>
<dt>
<dd>
<pre>
 /bin/mkdir -p /tmp/stuff/usr/bin
 /bin/cp myprogram /tmp/stuff/usr/bin
</pre>
</dl>
<p> You can use make-redir inside an RPM .spec file. Be sure to &quot;BuildRequires&quot; auto-destdir, and set the DESTDIR to be the RPM build root, as follows in the spec file: </p>
<dl>
<dt>
<dd>
<pre>
 ...
 BuildRequires: auto-destdir
 ...
 %install
 rm -rf &quot;$RPM_BUILD_ROOT&quot;
 make-redir DESTDIR=&quot;$RPM_BUILD_ROOT&quot; install
</pre>
</dl>
<p> Some RPM spec authors may prefer to use %{buildroot} instead of $RPM_BUILD_ROOT. </p>
<h2>IMPLEMENTATION APPROACH</h2>
<p> The auto-destdir tools (including run-redir and make-redir) work by modifying the PATH environment variable and providing a few &quot;wrappers&quot; that override typical installation commands like &quot;cp&quot; and &quot;install&quot;. These commands with wrappers, called &quot;wrapped commands&quot;, use the values of $REDIR_DESTDIR or $DESTDIR (with REDIR_DESTDIR taking precedence), and will redirect reads and writes of files under certain conditions. The &quot;redirection&quot; comes by simply changing the name of the file source or destination, and then calling the &quot;real&quot; program being wrapped. The internal function redir_name takes the original filename, and how it will be used (e.g., for reading or writing), and determines if it should be renamed (and if so, to what). In addition, make-redir redirects all shell commands (using SHELL and a special wrapper for shell commands); any command that begins with the prefix /usr/ or /usr/bin/, followed by a wrapped command&#8217;s name, will have that prefix removed. </p>
<p> This may seem to be an odd implementation approach, but it has many advantages. The &quot;obvious&quot; way to implement redirection is to manipulate LD_PRELOAD and wrap the open() and creat() calls. But as the <a href="/docs/linux/man/1-fakeroot/">fakeroot</a>(1) documentation notes, this approach creates &quot;problems, as demonstrated by the libtricks package. This package wrapped many more functions, and tried to do a lot more than fakeroot. It turned out that a minor upgrade of libc (from one where the stat() function didn&#8217;t use open() to one with a stat() function that did (in some cases) use open()), would cause unexplainable segfaults (that is, the libc6 stat() called the wrapped open(), which would then call the libc6 stat(), etc). Fixing them wasn&#8217;t all that easy, but once fixed, it was just a matter of time before another function started to use open()&#8230;&quot;. LD_PRELOAD-based approaches fail on commands that are statically linked, and the commands usually used for installation (e.g., cp) are often statically linked. Others tools (like fakeroot) also use LD_PRELOAD, so using LD_PRELOAD means that these other tools cannot be used simultaneously. Other &quot;obvious&quot; approaches are to use ptrace(), or redirect file writes using the kernel (e.g. with chroot), but these turn out to have many problems too, as discussed in &lt;<a rel="nofollow" href="http://www.dwheeler.com/essays/automating-destdir.html">http://www.dwheeler.com/essays/automating-destdir.html</a>&gt;. </p>
<p> In contrast, since run-redir and make-redir don&#8217;t manipulate LD_PRELOAD to manipulate open() or creat(), they are immune to deadlocks caused by changes in the C library, work with statically-linked commands, and work with tools like fakeroot. No special privileges are needed to run these programs, nor do they require setuid installation, eliminating many security concerns (compared to a chroot, setuid, or kernel-based approach). No kernel driver is used, nor is ptrace() used, so these tools should be fairly portable to any POSIX-based system with bash. All work happens very quickly, since nearly all commands simply run as usual, and even the wrapped commands merely run a short shell script before running as usual. The implementation is entirely a set of small bash scripts with trivial dependencies, so the auto-destdir tools can be easily included in a package&#8217;s build process without slowing the build process down (even if the build process requires re-installing dependencies on each run). </p>
<p> In practice, this approach is sufficient to automate DESTDIR for typical installation scripts. Typical &quot;make install&quot; programs, even if they are deeply recursive, only use a very few commands to actually write files to their final locations in trusted directories, and usually invoke commands without using the full pathnames of the commands (e.g., &quot;install -p myprog /usr/bin&quot;). As a result, typical installation scripts are easily redirected by this program. </p>
<p> More information about various implementation alternatives, their pros, and their cons, is here: <a rel="nofollow" href="http://www.dwheeler.com/essays/automating-destdir.html">http://www.dwheeler.com/essays/automating-destdir.html</a> </p>
<h2>LIMITATIONS</h2>
<p> Only wrapped programs will be redirected to the new destination directory; any other program will not be redirected. Currently, the &quot;wrapped&quot; commands are (alphabetically): </p>
<dl>
<dt>
<dd> <i>chmod</i>, <i>cp</i>, <i>install</i>, <i>ln</i>, <i>mkdir</i>, <i>mv</i>, and <i>touch</i>.</dl>
<p> If the makefile invokes wrapped programs using absolute pathnames (e.g., calling &quot;/bin/cp&quot; instead of &quot;cp&quot;), then the command will be redirected anyway if it is the absolutely first command at the beginning of a line in a makefile and is invoked directly or via makefile variable expansions like $(CP). Absolute pathnames at the <i>beginning</i> of a line are handled because make-redir sets SHELL to a special shell wrapper that handles this particular case. However, absolute pathnames for wrapped programs are not handled in any other place (doing so would require the shell wrapper to re-implement shell parsing); e.g., program names stored in shell variable expansions will not be intercepted. Thus, makefile lines like &quot;cd X; /usr/bin/install myprogram /usr/bin&quot; will not be redirected. In these cases, you should change absolute pathname invocations like <i>/usr/bin/install</i> to unnamed-path invocations like <i>install</i>. </p>
<p> Capabilities built into the shell are not redirected, including I/O redirection such as &quot;&lt;&quot;, &quot;&gt;&quot;, and &quot;&gt;&gt;&quot;. This means that &quot;cat x &gt; /usr/bin/program&quot; will not be redirected; use &quot;cp x /usr/bin/program&quot; or similar instead. Similarly, &quot;test&quot; and &quot;[&quot; (which are normally shell built-ins) aren&#8217;t redirected. Changing this would require auto-destdir to re-implement a full shell. </p>
<p> The wrappers presume GNU command line options, and will not understand other options even if the underlying tool would. In practice, this is almost always irrelevant; &quot;make install&quot; typically only uses highly-portable commands to copy files and make directories, and does not use unusual options. </p>
<p> The &quot;rm&quot; and &quot;rmdir&quot; commands are not redirected simply because these are unlikely commands during a &quot;make install&quot;. Similarly, there are no &quot;whiteout&quot; files to record when a file is removed from $DESTDIR, because this does not seem useful for &quot;make install&quot;. </p>
<p> In cases where this wrapper is not sufficient, you may need to modify the installation script. If significant modifications to the installation script are required, you may as well add DESTDIR support directly to the installation script. The auto-destdir tools are designed to handle common cases, so that people can focus their time on the cases that need special handling. </p>
<h2>GUIDANCE FOR SOFTWARE CREATORS</h2>
<p> When writing the commands for &quot;make install&quot;:</p>
<dl>
<dt>*</p>
<dd> Only use the wrapped commands to install files and directories in their final positions (e.g., install, cp, ln, and mkdir).</p>
<dt>*</p>
<dd> Don&#8217;t use full pathnames of wrapped commands (e.g., &quot;/usr/bin/install&quot;); use their basename (e.g., &quot;install&quot;).</p>
<dt>*</p>
<dd> Don&#8217;t use redirection (e.g., &quot;&gt;&quot;) to write to files in privileged directories; use redirection to write to a &quot;local&quot; file (typically during the build process), and then use &quot;install&quot; or &quot;cp&quot; to install the result.</dl>
<p> Supporting DESTDIR is still a good idea. </p>
<h2>BUGS</h2>
<p> As noted above, only &quot;wrapped&quot; commands are redirected. Some commands that aren&#8217;t wrapped, and perhaps should be, include: install-info, ldconfig, rm, rmdir, chown, chgrp, and libtool. For permissions-related commands (like chmod, chown, and chgrp), consider also using fakeroot or make&#8217;s &quot;-k&quot; option. </p>
<p> Options with optional arguments cannot accept arguments that begin with &quot;-&quot;, due to limitations of <a href="/docs/linux/man/1-getopt/">getopt</a>(1). </p>
<p> cp&#8217;s &#8211;parents argument is supported, but it won&#8217;t work if the original files are being copied from a redirected location. </p>
<p> When running make-redir, the makefile&#8217;s SHELL value is ignored. If you need to use the SHELL value provided by the makefile, run make-redir and provide &quot;SHELL=&#8230;&quot; with the correct shell value. If you do this, wrapped commands must never be invoked using their full pathname. </p>
<h2>AUTHOR</h2>
<p> David A. Wheeler </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;dwheeler, at, dwheeler dot com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 Institute for Defense Analyses. Released using the MIT license.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-run-redir/">run-redir</a>(1) </p>
<h2>Index</h2>
