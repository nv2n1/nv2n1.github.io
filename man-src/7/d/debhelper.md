---
title: "debhelper(7)"
name: "debhelper"
section: "7"
letter: "d"
url: "/docs/linux/man/7-debhelper/"
description: "debhelper – the debhelper tool suite"
---

<p>debhelper &#8211; the debhelper tool suite</p>
<h2>Synopsis</h2>
<p><code>dh_</code><i>*</i> [<code>-v</code>] [<code>-a</code>] [<code>-i</code>] [<code>&#8211;no-act</code>] [<code>-p</code><i>package</i>] [<code>-N</code><i>package</i>] [<code>-P</code><i>tmpdir</i>]</p>
<h2>Description</h2>
<p>Debhelper is used to help you build a Debian package. The philosophy behind debhelper is to provide a collection of small, simple, and easily understood tools that are used in <i>debian/rules</i> to automate various common aspects of building a package. This means less work for you, the packager. It also, to some degree means that these tools can be changed if Debian policy changes, and packages that use them will require only a rebuild to comply with the new policy. </p>
<p> A typical <i>debian/rules</i> file that uses debhelper will call several debhelper commands in sequence, or use <i><a href="/docs/linux/man/1-dh/">dh</a></i>(1) to automate this process. Examples of rules files that use debhelper are in <i>/usr/share/doc/debhelper/examples/</i> </p>
<p> To create a new Debian package using debhelper, you can just copy one of the sample rules files and edit it by hand. Or you can try the <code>dh-make</code> package, which contains a dh_make command that partially automates the process. For a more gentle introduction, the <code>maint-guide</code> Debian package contains a tutorial about making your first package using debhelper. </p>
<p> Except where tool explicitly denotes otherwise, all of the debhelper tools assumes that they run from root directory of an unpacked source package. This is so they can locate find <i>debian/control</i> and <i>debian/compat</i> when needed.</p>
<h2>Debhelper Commands</h2>
<p>Here is the list of debhelper commands you can use. See their man pages for additional documentation.</p>
<dl>
<dt><i><a href="/docs/linux/man/1-dh_auto_build/">dh_auto_build</a></i>(1)</p>
<dd>automatically builds a package</p>
<dt><i><a href="/docs/linux/man/1-dh_auto_clean/">dh_auto_clean</a></i>(1)</p>
<dd>automatically cleans up after a build</p>
<dt><i><a href="/docs/linux/man/1-dh_auto_configure/">dh_auto_configure</a></i>(1)</p>
<dd>automatically configure a package prior to building</p>
<dt><i><a href="/docs/linux/man/1-dh_auto_install/">dh_auto_install</a></i>(1)</p>
<dd>automatically runs make install or similar</p>
<dt><i><a href="/docs/linux/man/1-dh_auto_test/">dh_auto_test</a></i>(1)</p>
<dd>automatically runs a package&#8217;s test suites</p>
<dt><i><a href="/docs/linux/man/1-dh_bugfiles/">dh_bugfiles</a></i>(1)</p>
<dd>install bug reporting customization files into package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_builddeb/">dh_builddeb</a></i>(1)</p>
<dd>build Debian binary packages</p>
<dt><i><a href="/docs/linux/man/1-dh_clean/">dh_clean</a></i>(1)</p>
<dd>clean up package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_compress/">dh_compress</a></i>(1)</p>
<dd>compress files and fix symlinks in package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_dwz/">dh_dwz</a></i>(1)</p>
<dd>optimize <font SIZE="-1">DWARF</font> debug information in <font SIZE="-1">ELF</font> binaries via dwz</p>
<dt><i><a href="/docs/linux/man/1-dh_fixperms/">dh_fixperms</a></i>(1)</p>
<dd>fix permissions of files in package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_gconf/">dh_gconf</a></i>(1)</p>
<dd>install GConf defaults files and register schemas</p>
<dt><i><a href="/docs/linux/man/1-dh_gencontrol/">dh_gencontrol</a></i>(1)</p>
<dd>generate and install control file</p>
<dt><i><a href="/docs/linux/man/1-dh_icons/">dh_icons</a></i>(1)</p>
<dd>Update caches of Freedesktop icons</p>
<dt><i><a href="/docs/linux/man/1-dh_install/">dh_install</a></i>(1)</p>
<dd>install files into package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_installcatalogs/">dh_installcatalogs</a></i>(1)</p>
<dd>install and register <font SIZE="-1">SGML</font> Catalogs</p>
<dt><i><a href="/docs/linux/man/1-dh_installchangelogs/">dh_installchangelogs</a></i>(1)</p>
<dd>install changelogs into package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_installcron/">dh_installcron</a></i>(1)</p>
<dd>install cron scripts into etc/cron.*</p>
<dt><i><a href="/docs/linux/man/1-dh_installdeb/">dh_installdeb</a></i>(1)</p>
<dd>install files into the <font SIZE="-1">DEBIAN</font> directory</p>
<dt><i><a href="/docs/linux/man/1-dh_installdebconf/">dh_installdebconf</a></i>(1)</p>
<dd>install files used by debconf in package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_installdirs/">dh_installdirs</a></i>(1)</p>
<dd>create subdirectories in package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_installdocs/">dh_installdocs</a></i>(1)</p>
<dd>install documentation into package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_installemacsen/">dh_installemacsen</a></i>(1)</p>
<dd>register an Emacs add on package</p>
<dt><i><a href="/docs/linux/man/1-dh_installexamples/">dh_installexamples</a></i>(1)</p>
<dd>install example files into package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_installgsettings/">dh_installgsettings</a></i>(1)</p>
<dd>install GSettings overrides and set dependencies</p>
<dt><i><a href="/docs/linux/man/1-dh_installifupdown/">dh_installifupdown</a></i>(1)</p>
<dd>install if-up and if-down hooks</p>
<dt><i><a href="/docs/linux/man/1-dh_installinfo/">dh_installinfo</a></i>(1)</p>
<dd>install info files</p>
<dt><i><a href="/docs/linux/man/1-dh_installinit/">dh_installinit</a></i>(1)</p>
<dd>install service init files into package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_installlogcheck/">dh_installlogcheck</a></i>(1)</p>
<dd>install logcheck rulefiles into etc/logcheck/</p>
<dt><i><a href="/docs/linux/man/1-dh_installlogrotate/">dh_installlogrotate</a></i>(1)</p>
<dd>install logrotate config files</p>
<dt><i><a href="/docs/linux/man/1-dh_installman/">dh_installman</a></i>(1)</p>
<dd>install man pages into package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_installmenu/">dh_installmenu</a></i>(1)</p>
<dd>install Debian menu files into package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_installmime/">dh_installmime</a></i>(1)</p>
<dd>install mime files into package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_installmodules/">dh_installmodules</a></i>(1)</p>
<dd>register kernel modules</p>
<dt><i><a href="/docs/linux/man/1-dh_installpam/">dh_installpam</a></i>(1)</p>
<dd>install pam support files</p>
<dt><i><a href="/docs/linux/man/1-dh_installppp/">dh_installppp</a></i>(1)</p>
<dd>install ppp ip-up and ip-down files</p>
<dt><i><a href="/docs/linux/man/1-dh_installsystemd/">dh_installsystemd</a></i>(1)</p>
<dd>install systemd unit files</p>
<dt><i><a href="/docs/linux/man/1-dh_installudev/">dh_installudev</a></i>(1)</p>
<dd>install udev rules files</p>
<dt><i><a href="/docs/linux/man/1-dh_installwm/">dh_installwm</a></i>(1)</p>
<dd>register a window manager</p>
<dt><i><a href="/docs/linux/man/1-dh_installxfonts/">dh_installxfonts</a></i>(1)</p>
<dd>register X fonts</p>
<dt><i><a href="/docs/linux/man/1-dh_link/">dh_link</a></i>(1)</p>
<dd>create symlinks in package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_lintian/">dh_lintian</a></i>(1)</p>
<dd>install lintian override files into package build directories</p>
<dt><i><a href="/docs/linux/man/1-dh_listpackages/">dh_listpackages</a></i>(1)</p>
<dd>list binary packages debhelper will act on</p>
<dt><i><a href="/docs/linux/man/1-dh_makeshlibs/">dh_makeshlibs</a></i>(1)</p>
<dd>automatically create shlibs file and call dpkg-gensymbols</p>
<dt><i><a href="/docs/linux/man/1-dh_md5sums/">dh_md5sums</a></i>(1)</p>
<dd>generate DEBIAN/md5sums file</p>
<dt><i><a href="/docs/linux/man/1-dh_missing/">dh_missing</a></i>(1)</p>
<dd>check for missing files</p>
<dt><i><a href="/docs/linux/man/1-dh_movefiles/">dh_movefiles</a></i>(1)</p>
<dd>move files out of debian/tmp into subpackages</p>
<dt><i><a href="/docs/linux/man/1-dh_perl/">dh_perl</a></i>(1)</p>
<dd>calculates Perl dependencies and cleans up after MakeMaker</p>
<dt><i><a href="/docs/linux/man/1-dh_prep/">dh_prep</a></i>(1)</p>
<dd>perform cleanups in preparation for building a binary package</p>
<dt><i><a href="/docs/linux/man/1-dh_shlibdeps/">dh_shlibdeps</a></i>(1)</p>
<dd>calculate shared library dependencies</p>
<dt><i><a href="/docs/linux/man/1-dh_strip/">dh_strip</a></i>(1)</p>
<dd>strip executables, shared libraries, and some static libraries</p>
<dt><i><a href="/docs/linux/man/1-dh_systemd_enable/">dh_systemd_enable</a></i>(1)</p>
<dd>enable/disable systemd unit files</p>
<dt><i><a href="/docs/linux/man/1-dh_systemd_start/">dh_systemd_start</a></i>(1)</p>
<dd>start/stop/restart systemd unit files</p>
<dt><i><a href="/docs/linux/man/1-dh_testdir/">dh_testdir</a></i>(1)</p>
<dd>test directory before building Debian package</p>
<dt><i><a href="/docs/linux/man/1-dh_testroot/">dh_testroot</a></i>(1)</p>
<dd>ensure that a package is built with necessary level of root permissions</p>
<dt><i><a href="/docs/linux/man/1-dh_ucf/">dh_ucf</a></i>(1)</p>
<dd>register configuration files with ucf</p>
<dt><i><a href="/docs/linux/man/1-dh_update_autotools_config/">dh_update_autotools_config</a></i>(1)</p>
<dd>Update autotools config files</p>
<dt><i><a href="/docs/linux/man/1-dh_usrlocal/">dh_usrlocal</a></i>(1)</p>
<dd>migrate usr/local directories to maintainer scripts</dl>
<h3>Deprecated Commands</h3>
<p>A few debhelper commands are deprecated and should not be used.</p>
<dl>
<dt><i><a href="/docs/linux/man/1-dh_installmanpages/">dh_installmanpages</a></i>(1)</p>
<dd>old-style man page installer (deprecated)</dl>
<h3>Other Commands</h3>
<p>If a program&#8217;s name starts with <code>dh_</code>, and the program is not on the above lists, then it is not part of the debhelper package, but it should still work like the other programs described on this page.</p>
<h2>Debhelper Config Files</h2>
<p>Many debhelper commands make use of files in <i>debian/</i> to control what they do. Besides the common <i>debian/changelog</i> and <i>debian/control</i>, which are in all packages, not just those using debhelper, some additional files can be used to configure the behavior of specific debhelper commands. These files are typically named debian/<i>package</i>.foo (where <i>package</i> of course, is replaced with the package that is being acted on). </p>
<p> For example, <code>dh_installdocs</code> uses files named <i>debian/package.docs</i> to list the documentation files it will install. See the man pages of individual commands for details about the names and formats of the files they use. Generally, these files will list files to act on, one file per line. Some programs in debhelper use pairs of files and destinations or slightly more complicated formats. </p>
<p> Note for the first (or only) binary package listed in <i>debian/control</i>, debhelper will use <i>debian/foo</i> when there&#8217;s no <i>debian/package.foo</i> file. </p>
<p> In some rare cases, you may want to have different versions of these files for different architectures or OSes. If files named debian/<i>package</i>.foo.<i></i><font SIZE="-1"><i>ARCH</i></font><i></i> or debian/<i>package</i>.foo.<i></i><font SIZE="-1"><i>OS</i></font><i></i> exist, where <i></i><font SIZE="-1"><i>ARCH</i></font><i></i> and <i></i><font SIZE="-1"><i>OS</i></font><i></i> are the same as the output of &quot;<code>dpkg-architecture -qDEB_HOST_ARCH</code>&#8220; / &#8221;<code>dpkg-architecture -qDEB_HOST_ARCH_OS</code>&quot;, then they will be used in preference to other, more general files. </p>
<p> Mostly, these config files are used to specify lists of various types of files. Documentation or example files to install, files to move, and so on. When appropriate, in cases like these, you can use standard shell wildcard characters (<code>?</code> and <code>*</code> and <code>[</code><i>..</i><code>]</code> character classes) in the files. You can also put comments in these files; lines beginning with <code>#</code> are ignored. </p>
<p> The syntax of these files is intentionally kept very simple to make them easy to read, understand, and modify. If you prefer power and complexity, you can make the file executable, and write a program that outputs whatever content is appropriate for a given situation. When you do so, the output is not further processed to expand wildcards or strip comments.</p>
<h2>Shared Debhelper Options</h2>
<p>The following command line options are supported by all debhelper programs.</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose mode: show all commands that modify the package build directory.</p>
<dt><code>&#8211;no-act</code></p>
<dd>Do not really do anything. If used with -v, the result is that the command will output what it would have done.</p>
<dt><code>-a</code>, <code>&#8211;arch</code></p>
<dd>Act on architecture dependent packages that should be built for the <font SIZE="-1"><code>DEB_HOST_ARCH</code></font> architecture.</p>
<dt><code>-i</code>, <code>&#8211;indep</code></p>
<dd>Act on all architecture independent packages.</p>
<dt><code>-p</code><i>package</i>, <code>&#8211;package=</code><i>package</i></p>
<dd>Act on the package named <i>package</i>. This option may be specified multiple times to make debhelper operate on a given set of packages.</p>
<dt><code>-s</code>, <code>&#8211;same-arch</code></p>
<dd>Deprecated alias of <code>-a</code>. </p>
<p> This option is removed in compat 12.</p>
<dt><code>-N</code><i>package</i>, <code>&#8211;no-package=</code><i>package</i></p>
<dd>Do not act on the specified package even if an <code>-a</code>, <code>-i</code>, or <code>-p</code> option lists the package as one that should be acted on.</p>
<dt><code>&#8211;remaining-packages</code></p>
<dd>Do not act on the packages which have already been acted on by this debhelper command earlier (i.e. if the command is present in the package debhelper log). For example, if you need to call the command with special options only for a couple of binary packages, pass this option to the last call of the command to process the rest of packages with default settings.</p>
<dt><code>&#8211;ignore=</code><i>file</i></p>
<dd>Ignore the specified file. This can be used if <i>debian/</i> contains a debhelper config file that a debhelper command should not act on. Note that <i>debian/compat</i>, <i>debian/control</i>, and <i>debian/changelog</i> can&#8217;t be ignored, but then, there should never be a reason to ignore those files. </p>
<p> For example, if upstream ships a <i>debian/init</i> that you don&#8217;t want <code>dh_installinit</code> to install, use <code>&#8211;ignore=debian/init</code></p>
<dt><code>-P</code><i>tmpdir</i>, <code>&#8211;tmpdir=</code><i>tmpdir</i></p>
<dd>Use <i>tmpdir</i> for package build directory. The default is debian/<i>package</i></p>
<dt><code>&#8211;mainpackage=</code><i>package</i></p>
<dd>This little-used option changes the package which debhelper considers the &#8220;main package&#8221;, that is, the first one listed in <i>debian/control</i>, and the one for which <i>debian/foo</i> files can be used instead of the usual <i>debian/package.foo</i> files.</p>
<dt><code>-O=</code><i>option</i>|<i>bundle</i></p>
<dd>This is used by <i><a href="/docs/linux/man/1-dh/">dh</a></i>(1) when passing user-specified options to all the commands it runs. If the command supports the specified option or option bundle, it will take effect. If the command does not support the option (or any part of an option bundle), it will be ignored.</dl>
<h2>Common Debhelper Options</h2>
<p>The following command line options are supported by some debhelper programs. See the man page of each program for a complete explanation of what each option does.</p>
<dl>
<dt><code>-n</code></p>
<dd>Do not modify <i>postinst</i>, <i>postrm</i>, etc. scripts.</p>
<dt><code>-X</code><i>item</i>, <code>&#8211;exclude=</code><i>item</i></p>
<dd>Exclude an item from processing. This option may be used multiple times, to exclude more than one thing. The IitemR is typically part of a filename, and any file containing the specified text will be excluded.</p>
<dt><code>-A</code>, <code>&#8211;all</code></p>
<dd>Makes files or other items that are specified on the command line take effect in <font SIZE="-1">ALL</font> packages acted on, not just the first.</dl>
<h2>Build System Options</h2>
<p>The following command line options are supported by all of the <code>dh_auto_</code><i>*</i> debhelper programs. These programs support a variety of build systems, and normally heuristically determine which to use, and how to use them. You can use these command line options to override the default behavior. Typically these are passed to <i><a href="/docs/linux/man/1-dh/">dh</a></i>(1), which then passes them to all the <code>dh_auto_</code><i>*</i> programs.</p>
<dl>
<dt><code>-S</code><i>buildsystem</i>, <code>&#8211;buildsystem=</code><i>buildsystem</i></p>
<dd>Force use of the specified <i>buildsystem</i>, instead of trying to auto-select one which might be applicable for the package.</p>
<dt><code>-D</code><i>directory</i>, <code>&#8211;sourcedirectory=</code><i>directory</i></p>
<dd>Assume that the original package source tree is at the specified <i>directory</i> rather than the top level directory of the Debian source package tree.</p>
<dt><code>-B</code>[<i>directory</i>], <code>&#8211;builddirectory=</code>[<i>directory</i>]</p>
<dd>Enable out of source building and use the specified <i>directory</i> as the build directory. If <i>directory</i> parameter is omitted, a default build directory will be chosen. </p>
<p> If this option is not specified, building will be done in source by default unless the build system requires or prefers out of source tree building. In such a case, the default build directory will be used even if <code>&#8211;builddirectory</code> is not specified. </p>
<p> If the build system prefers out of source tree building but still allows in source building, the latter can be re-enabled by passing a build directory path that is the same as the source directory path.</p>
<dt><code>&#8211;parallel</code>, <code>&#8211;no-parallel</code></p>
<dd>Control whether parallel builds should be used if underlying build system supports them. The number of parallel jobs is controlled by the <font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font> environment variable (&#8220;Debian Policy, section 4.9.1&#8221;) at build time. It might also be subject to a build system specific limit. </p>
<p> If neither option is specified, debhelper currently defaults to <code>&#8211;parallel</code> in compat 10 (or later) and <code>&#8211;no-parallel</code> otherwise. </p>
<p> As an optimization, <code>dh</code> will try to avoid passing these options to subprocesses, if they are unnecessary and the only options passed. Notably this happens when <font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font> does not have a <i>parallel</i> parameter (or its value is 1).</p>
<dt><code>&#8211;max-parallel=</code><i>maximum</i></p>
<dd>This option implies <code>&#8211;parallel</code> and allows further limiting the number of jobs that can be used in a parallel build. If the package build is known to only work with certain levels of concurrency, you can set this to the maximum level that is known to work, or that you wish to support. </p>
<p> Notably, setting the maximum to 1 is effectively the same as using <code>&#8211;no-parallel</code>.</p>
<dt><code>&#8211;list</code>, <code>-l</code></p>
<dd>List all build systems supported by debhelper on this system. The list includes both default and third party build systems (marked as such). Also shows which build system would be automatically selected, or which one is manually specified with the <code>&#8211;buildsystem</code> option.</dl>
<h2>Compatibility Levels</h2>
<p>From time to time, major non-backwards-compatible changes need to be made to debhelper, to keep it clean and well-designed as needs change and its author gains more experience. To prevent such major changes from breaking existing packages, the concept of debhelper compatibility levels was introduced. You must tell debhelper which compatibility level it should use, and it modifies its behavior in various ways. The compatibility level is specified in the <i>debian/compat</i> file and the file must be present. </p>
<p> Tell debhelper what compatibility level to use by writing a number to <i>debian/compat</i>. For example, to use v11 mode: </p>
<pre> % echo 11 &gt; debian/compat</pre>
<p>Your package will also need a versioned build dependency on a version of debhelper equal to (or greater than) the compatibility level your package uses. So for compatibility level 11, ensure debian/control has: </p>
<pre> Build-Depends: debhelper (&gt;= 11)</pre>
<p>Unless otherwise indicated, all debhelper documentation assumes that you are using the most recent compatibility level, and in most cases does not indicate if the behavior is different in an earlier compatibility level, so if you are not using the most recent compatibility level, you&#8217;re advised to read below for notes about what is different in earlier compatibility levels.</p>
<h3>Supported compatibility levels</h3>
<p>These are the available compatibility levels:</p>
<dl>
<dt>v5</p>
<dd>This is the lowest supported compatibility level. </p>
<p> If you are upgrading from an earlier compatibility level, please review <i><a href="/docs/linux/man/7-debhelper-obsolete-compat/">debhelper-obsolete-compat</a></i>(7). </p>
<p> This mode is deprecated.</p>
<dt>v6</p>
<dd>Changes from v5 are:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>Commands that generate maintainer script fragments will order the fragments in reverse order for the <i>prerm</i> and <i>postrm</i> scripts.</p>
<dt>&#8211;</p>
<dd><code>dh_installwm</code> will install a slave manpage link for <i>x-window-manager.1.gz</i>, if it sees the man page in <i>usr/share/man/man1</i> in the package build directory.</p>
<dt>&#8211;</p>
<dd><code>dh_builddeb</code> did not previously delete everything matching <font SIZE="-1"><code>DH_ALWAYS_EXCLUDE</code></font>, if it was set to a list of things to exclude, such as <font SIZE="-1"><code>CVS:</code></font><code>.svn:.git</code>. Now it does.</p>
<dt>&#8211;</p>
<dd><code>dh_installman</code> allows overwriting existing man pages in the package build directory. In previous compatibility levels it silently refuses to do this.</dl>
</dl>
<dl>
<dd>This mode is deprecated.</dl>
<dt>v7</p>
<dd>Changes from v6 are:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd><code>dh_install</code>, will fall back to looking for files in <i>debian/tmp</i> if it doesn&#8217;t find them in the current directory (or wherever you tell it look using <code>&#8211;sourcedir</code>). This allows <code>dh_install</code> to interoperate with <code>dh_auto_install</code>, which installs to <i>debian/tmp</i>, without needing any special parameters.</p>
<dt>&#8211;</p>
<dd><code>dh_clean</code> will read <i>debian/clean</i> and delete files listed there.</p>
<dt>&#8211;</p>
<dd><code>dh_clean</code> will delete toplevel <i>*-stamp</i> files.</p>
<dt>&#8211;</p>
<dd><code>dh_installchangelogs</code> will guess at what file is the upstream changelog if none is specified.</dl>
</dl>
<dl>
<dd>This mode is deprecated.</dl>
<dt>v8</p>
<dd>Changes from v7 are:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>Commands will fail rather than warning when they are passed unknown options.</p>
<dt>&#8211;</p>
<dd><code>dh_makeshlibs</code> will run <code>dpkg-gensymbols</code> on all shared libraries that it generates shlibs files for. So <code>-X</code> can be used to exclude libraries. Also, libraries in unusual locations that <code>dpkg-gensymbols</code> would not have processed before will be passed to it, a behavior change that can cause some packages to fail to build.</p>
<dt>&#8211;</p>
<dd><code>dh</code> requires the sequence to run be specified as the first parameter, and any switches come after it. Ie, use &quot;<code>dh $@ &#8211;foo</code>&#8220;, not &#8221;<code>dh &#8211;foo $@</code>&quot;.</p>
<dt>&#8211;</p>
<dd><code>dh_auto_</code><i>*</i> prefer to use Perl&#8217;s <code>Module::Build</code> in preference to <i>Makefile.PL</i>.</dl>
</dl>
<dl>
<dd>This mode is deprecated.</dl>
<dt>v9</p>
<dd>Changes from v8 are:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>Multiarch support. In particular, <code>dh_auto_configure</code> passes multiarch directories to autoconf in &#8211;libdir and &#8211;libexecdir.</p>
<dt>&#8211;</p>
<dd>dh is aware of the usual dependencies between targets in debian/rules. So, &#8220;dh binary&#8221; will run any build, build-arch, build-indep, install, etc targets that exist in the rules file. There&#8217;s no need to define an explicit binary target with explicit dependencies on the other targets.</p>
<dt>&#8211;</p>
<dd><code>dh_strip</code> compresses debugging symbol files to reduce the installed size of -dbg packages.</p>
<dt>&#8211;</p>
<dd><code>dh_auto_configure</code> does not include the source package name in &#8211;libexecdir when using autoconf.</p>
<dt>&#8211;</p>
<dd><code>dh</code> does not default to enabling &#8211;with=python-support </p>
<p> (Obsolete: As the <code>dh_pysupport</code> tool was removed from Debian stretch. Since debhelper/10.3, <code>dh</code> no longer enables this sequence add-on regardless of compat level)</p>
<dt>&#8211;</p>
<dd>All of the <code>dh_auto_</code><i>*</i> debhelper programs and <code>dh</code> set environment variables listed by <code>dpkg-buildflags</code>, unless they are already set.</p>
<dt>&#8211;</p>
<dd><code>dh_auto_configure</code> passes <code>dpkg-buildflags</code> <font SIZE="-1">CFLAGS, CPPFLAGS,</font> and <font SIZE="-1">LDFLAGS</font> to perl <i>Makefile.PL</i> and <i>Build.PL</i></p>
<dt>&#8211;</p>
<dd><code>dh_strip</code> puts separated debug symbols in a location based on their build-id.</p>
<dt>&#8211;</p>
<dd>Executable debhelper config files are run and their output used as the configuration.</dl>
</dl>
<dl>
<dd></dl>
<dt>v10</p>
<dd>Changes from v9 are:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd><code>dh_installinit</code> will no longer install a file named debian/<i>package</i> as an init script.</p>
<dt>&#8211;</p>
<dd><code>dh_installdocs</code> will error out if it detects links created with &#8211;link-doc between packages of architecture &#8220;all&#8221; and non-&#8220;all&#8221; as it breaks binNMUs.</p>
<dt>&#8211;</p>
<dd><code>dh</code> no longer creates the package build directory when skipping running debhelper commands. This will not affect packages that only build with debhelper commands, but it may expose bugs in commands not included in debhelper.</p>
<dt>&#8211;</p>
<dd><code>dh_installdeb</code> no longer installs a maintainer-provided debian/<i>package</i>.shlibs file. This is now done by <code>dh_makeshlibs</code> instead.</p>
<dt>&#8211;</p>
<dd><code>dh_installwm</code> refuses to create a broken package if no man page can be found (required to register for the x-window-manager alternative).</p>
<dt>&#8211;</p>
<dd>Debhelper will default to <code>&#8211;parallel</code> for all buildsystems that support parallel building. This can be disabled by using either <code>&#8211;no-parallel</code> or passing <code>&#8211;max-parallel</code> with a value of 1.</p>
<dt>&#8211;</p>
<dd>The <code>dh</code> command will not accept any of the deprecated &#8220;manual sequence control&#8221; parameters (<code>&#8211;before</code>, <code>&#8211;after</code>, etc.). Please use override targets instead.</p>
<dt>&#8211;</p>
<dd>The <code>dh</code> command will no longer use log files to track which commands have been run. The <code>dh</code> command <i>still</i> keeps track of whether it already ran the &#8220;build&#8221; sequence and skip it if it did. </p>
<p> The main effects of this are:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>With this, it is now easier to debug the <i>install</i> or/and <i>binary</i> sequences because they can now trivially be re-run (without having to do a full &#8220;clean and rebuild&#8221; cycle)</p>
<dt>&#8211;</p>
<dd>The main caveat is that <code>dh_*</code> now only keeps track of what happened in a single override target. When all the calls to a given <code>dh_cmd</code> command happens in the same override target everything will work as before. </p>
<p> Example of where it can go wrong: </p>
<pre> override_dh_foo:
 dh_foo -pmy-pkg
 override_dh_bar:
 dh_bar
 dh_foo --remaining</pre>
<p>In this case, the call to <code>dh_foo &#8211;remaining</code> will <i>also</i> include <i>my-pkg</i>, since <code>dh_foo -pmy-pkg</code> was run in a separate override target. This issue is not limited to <code>&#8211;remaining</code>, but also includes <code>-a</code>, <code>-i</code>, etc.</dl>
</dl>
<dl>
<dd></dl>
<dt>&#8211;</p>
<dd>The <code>dh_installdeb</code> command now shell-escapes the lines in the <i>maintscript</i> config file. This was the original intent but it did not work properly and packages have begun to rely on the incomplete shell escaping (e.g. quoting file names).</p>
<dt>&#8211;</p>
<dd>The <code>dh_installinit</code> command now defaults to <code>&#8211;restart-after-upgrade</code>. For packages needing the previous behaviour, please use <code>&#8211;no-restart-after-upgrade</code>.</p>
<dt>&#8211;</p>
<dd>The <code>autoreconf</code> sequence is now enabled by default. Please pass <code>&#8211;without autoreconf</code> to <code>dh</code> if this is not desirable for a given package</p>
<dt>&#8211;</p>
<dd>The <code>systemd</code> sequence is now enabled by default. Please pass <code>&#8211;without systemd</code> to <code>dh</code> if this is not desirable for a given package.</dl>
</dl>
<dl>
<dd></dl>
<dt>v11</p>
<dd>This is the recommended mode of operation. </p>
<p> Changes from v10 are:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd><code>dh_installinit</code> no longer installs <i>service</i> or <i>tmpfile</i> files, nor generates maintainer scripts for those files. Please use the new <code>dh_installsystemd</code> helper.</p>
<dt>&#8211;</p>
<dd>The <code>dh_systemd_enable</code> and <code>dh_systemd_start</code> helpers have been replaced by the new <code>dh_installsystemd</code> helper. For the same reason, the <code>systemd</code> sequence for <code>dh</code> has also been removed. If you need to disable the <code>dh_installsystemd</code> helper tool, please use an empty override target. </p>
<p> Please note that the <code>dh_installsystemd</code> tool has a slightly different behaviour in some cases (e.g. when using the <code>&#8211;name</code> parameter).</p>
<dt>&#8211;</p>
<dd><code>dh_installdirs</code> no longer creates debian/<i>package</i> directories unless explicitly requested (or it has to create a subdirectory in it). </p>
<p> The vast majority of all packages will be unaffected by this change.</p>
<dt>&#8211;</p>
<dd>The <code>makefile</code> buildsystem now passes <code>INSTALL=install &#8211;strip-program=true</code> to <i><a href="/docs/linux/man/1-make/">make</a></i>(1). Derivative buildsystems (e.g. <code>configure</code> or <code>cmake</code>) are unaffected by this change.</p>
<dt>&#8211;</p>
<dd>The <code>autoconf</code> buildsystem now passes <code>&#8211;runstatedir=/run</code> to <i>./configure</i>.</p>
<dt>&#8211;</p>
<dd>The <code>cmake</code> buildsystem now passes <code>-DCMAKE_INSTALL_RUNSTATEDIR=/run</code> to <i><a href="/docs/linux/man/1-cmake/">cmake</a></i>(1).</p>
<dt>&#8211;</p>
<dd><code>dh_installman</code> will now prefer detecting the language from the path name rather than the extension.</p>
<dt>&#8211;</p>
<dd><code>dh_auto_install</code> will now only create the destination directory it needs. Previously, it would create the package build directory for all packages. This will not affect packages that only build with debhelper commands, but it may expose bugs in commands not included in debhelper.</p>
<dt>&#8211;</p>
<dd>The helpers <code>dh_installdocs</code>, <code>dh_installexamples</code>, <code>dh_installinfo</code>, and <code>dh_installman</code> now error out if their config has a pattern that does not match anything or reference a path that does not exist. </p>
<p> Known exceptions include building with the <code>nodoc</code> profile, where the above tools will silently permit failed matches where the patterns are used to specify documentation.</p>
<dt>&#8211;</p>
<dd>The helpers <code>dh_installdocs</code>, <code>dh_installexamples</code>, <code>dh_installinfo</code>, and <code>dh_installman</code> now accept the parameter <code>&#8211;sourcedir</code> with same meaning as <code>dh_install</code>. Furthermore, they now also fall back to <i>debian/tmp</i> like <code>dh_install</code>. </p>
<p> Migration note: A bug in debhelper 11 up to 11.1.5 made <code>dh_installinfo</code> incorrectly ignore <code>&#8211;sourcedir</code>.</p>
<dt>&#8211;</p>
<dd>The <code>perl-makemaker</code> and <code>perl-build</code> build systems no longer pass <code>-I.</code> to perl. Packages that still need this behaviour can emulate it by using the <font SIZE="-1"><code>PERL5LIB</code></font> environment variable. E.g. by adding <code>export PERL5LIB=.</code> in their debian/rules file (or similar).</p>
<dt>&#8211;</p>
<dd>The <font SIZE="-1"><code>PERL_USE_UNSAFE_INC</code></font> environment variable is no longer set by <code>dh</code> or any of the <code>dh_auto_*</code> tools. It was added as a temporary work around to avoid a lot of packages failing to build at the same time. </p>
<p> Note this item will eventually become obsolete as upstream intends to drop support for the <font SIZE="-1"><code>PERL_USE_UNSAFE_INC</code></font> environment variable. When perl drops support for it, then this variable will be removed retroactively from existing compat levels as well.</p>
<dt>&#8211;</p>
<dd>The <code>dh_makeshlibs</code> helper will now exit with an error if objdump returns a non-zero exit from analysing a given file.</p>
<dt>&#8211;</p>
<dd>The <code>dh_installdocs</code> and <code>dh_installexamples</code> tools will now attempt to guess the &#8220;main package&#8221; for a given documentation package (e.g. <i>pkg-doc</i> will have <i>pkg</i> as main package if the latter exists). If a main package is found, <i>most</i> of the documentation will be installed into <i>/usr/share/doc/main-pkg</i> by default as recommended by Debian policy §12.3 since version 3.9.7. Notable exceptions include the copyright file and changelog files. </p>
<p> The <code>&#8211;doc-main-package</code> option can be used when the auto-detection is insufficient.</p>
<dt>&#8211;</p>
<dd>The <code>dh_strip</code> and <code>dh_shlibdeps</code> tools no longer uses filename patterns to determine which files to process. Instead, they open the file and look for an <font SIZE="-1">ELF</font> header to determine if a given file is an shared object or an <font SIZE="-1">ELF</font> executable. </p>
<p> This change may cause the tools to process more files than previously.</dl>
</dl>
<dl>
<dd></dl>
<dt>v12</p>
<dd>This compatibility level is still open for development; use with caution. </p>
<p> Changes from v11 are:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>The <code>-s</code> (<code>&#8211;same-arch</code>) option is removed. Please use <code>-a</code> (<code>&#8211;arch</code>) instead.</p>
<dt>&#8211;</p>
<dd>Invoking <code>dh_clean -k</code> now causes an error instead of a deprecation warning.</p>
<dt>&#8211;</p>
<dd>The <code>&#8211;no-restart-on-upgrade</code> option in <code>dh_installinit</code> has been removed. Please use the new name <code>&#8211;no-stop-on-upgrade</code></p>
<dt>&#8211;</p>
<dd>There was a bug in the <code>doit</code> (and similar) functions from Debian::Debhelper::Dh_Lib that made them spawn a shell in one particular circumstance. This bug is now removed and will cause helpers that rely on the bug to fail with a &#8220;command not found&#8221;-error.</p>
<dt>&#8211;</p>
<dd>The <code>&#8211;list-missing</code> and <code>&#8211;fail-missing</code> in <code>dh_install</code> has been removed. Please use <code>dh_missing</code> and its corresponding options, which can also see the files installed by other helpers.</p>
<dt>&#8211;</p>
<dd>The <code>dh_installinit</code> helper no longer installs configuration for the upstart init system. Instead, it will abort the build if it finds an old upstart configuration file. The error is there to remind the package maintainer to ensure the proper removal of the conffiles shipped in previous versions of the package (if any).</p>
<dt>&#8211;</p>
<dd>The <code>dh_installdeb</code> tool will do basic validation of some <i><a href="/docs/linux/man/1-dpkg-maintscript-helper/">dpkg-maintscript-helper</a></i>(1) commands and will error out if the commands appear to be invalid.</p>
<dt>&#8211;</p>
<dd>The <code>dh_missing</code> tool will now default to <code>&#8211;list-missing</code>.</p>
<dt>&#8211;</p>
<dd>The <code>dh_makeshlibs</code> tool will now only pass libraries to <i><a href="/docs/linux/man/1-dpkg-gensymbols/">dpkg-gensymbols</a></i>(1) if the <font SIZE="-1">ELF</font> binary has a <font SIZE="-1">SONAME</font> (containing &#8220;.so&#8221;).</p>
<dt>&#8211;</p>
<dd>The <code>dh_compress</code> tool no longer compresses examples (i.e. anything installed in <i>&lt;/usr/share/doc/package/examples</i>&gt;.)</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h2>Notes</h2>
<h3>Multiple binary package support</h3>
<p>If your source package generates more than one binary package, debhelper programs will default to acting on all binary packages when run. If your source package happens to generate one architecture dependent package, and another architecture independent package, this is not the correct behavior, because you need to generate the architecture dependent packages in the binary-arch <i>debian/rules</i> target, and the architecture independent packages in the binary-indep <i>debian/rules</i> target. To facilitate this, as well as give you more control over which packages are acted on by debhelper programs, all debhelper programs accept the <code>-a</code>, <code>-i</code>, <code>-p</code>, and <code>-s</code> parameters. These parameters are cumulative. If none are given, debhelper programs default to acting on all packages listed in the control file, with the exceptions below. First, any package whose <code>Architecture</code> field in <code>debian/control</code> does not match the <font SIZE="-1"><code>DEB_HOST_ARCH</code></font> architecture will be excluded (&#8220;Debian Policy, section 5.6.8&#8221;). Also, some additional packages may be excluded based on the contents of the <font SIZE="-1"><code>DEB_BUILD_PROFILES</code></font> environment variable and <code>Build-Profiles</code> fields in binary package stanzas in <code>debian/control</code>, according to the draft policy at &lt;<a rel="nofollow" href="https://wiki.debian.org/BuildProfileSpec">https://wiki.debian.org/BuildProfileSpec</a>&gt;. <i>Interaction between package selections and Build-Profiles</i> Build-Profiles affect which packages are included in the package selections mechanisms in debhelper. Generally, the package selections are described from the assumption that all packages are enabled. This section describes how the selections react when a package is disabled due to the active Build-Profiles (or lack of active Build-Profiles).</p>
<dl>
<dt>-a/&#8211;arch, -i/&#8211;indep <font SIZE="-1">OR</font> no selection options (a raw &quot;dh_X&quot; call)</p>
<dd>The package disabled by Build-Profiles is silently excluded from the selection. Note you will receive a warning if <i>all</i> packages related to these selections are disabled. In that case, it generally does not make sense to do the build in the first place.</p>
<dt>-N <i>package</i> / &#8211;no-package <i>package</i></p>
<dd>The option is accepted and effectively does nothing.</p>
<dt>-p <i>package</i> / &#8211;package <i>package</i></p>
<dd>The option is accepted, but debhelper will not act on the package.</dl>
<p> Note that it does not matter whether a package is enabled or disabled by default.</p>
<h3>Automatic generation of Debian install scripts</h3>
<p>Some debhelper commands will automatically generate parts of Debian maintainer scripts. If you want these automatically generated things included in your existing Debian maintainer scripts, then you need to add <code>#DEBHELPER#</code> to your scripts, in the place the code should be added. <code>#DEBHELPER#</code> will be replaced by any auto-generated code when you run <code>dh_installdeb</code>. If a script does not exist at all and debhelper needs to add something to it, then debhelper will create the complete script. All debhelper commands that automatically generate code in this way let it be disabled by the -n parameter (see above). Note that the inserted code will be shell code, so you cannot directly use it in a Perl script. If you would like to embed it into a Perl script, here is one way to do that (note that I made sure that <tt>$1</tt>, <tt>$2</tt>, etc are set with the set command): </p>
<pre><code>my $temp = &quot;set -e
set -- @ARGV
&quot;.&lt;&lt; 'EOF';
#DEBHELPER #
EOF if (system($temp))
{
     my $exit_code = ($? &gt;&gt; 8) &amp; 0xff;
     my $signal = $ ? &amp;0x7f;
     if ($exit_code) {
         die(&quot;The debhelper script failed with error code: ${exit_code}&quot;);
     } else {
         die(&quot;The debhelper script was killed by signal: ${signal}&quot;);
     }
}

Automatic generation of miscellaneous dependencies.

    Some debhelper commands may make the generated package need to depend on
        some other packages.For example,
    if you use dh_installdebconf(1), your package will generally need to depend on debconf.Or if you use dh_installxfonts(1), your package will generally need to depend on a particular version of xutils.Keeping track of these miscellaneous dependencies can be annoying since they are dependent on how debhelper does things, so debhelper offers a way to automate it.</code></pre>
<p> All commands of this type, besides documenting what dependencies may be needed on their man pages, will automatically generate a substvar called <code>${misc:Depends}</code>. If you put that token into your <i>debian/control</i> file, it will be expanded to the dependencies debhelper figures you need. This is entirely independent of the standard <code>${shlibs:Depends}</code> generated by <i><a href="/docs/linux/man/1-dh_makeshlibs/">dh_makeshlibs</a></i>(1), and the <code>${perl:Depends}</code> generated by <i><a href="/docs/linux/man/1-dh_perl/">dh_perl</a></i>(1). You can choose not to use any of these, if debhelper&#8217;s guesses don&#8217;t match reality.</p>
<h3>Package build directories</h3>
<p>By default, all debhelper programs assume that the temporary directory used for assembling the tree of files in a package is debian/<i>package</i>. Sometimes, you might want to use some other temporary directory. This is supported by the <code>-P</code> flag. For example, &quot;<code>dh_installdocs -Pdebian/tmp</code>&quot;, will use <code>debian/tmp</code> as the temporary directory. Note that if you use <code>-P</code>, the debhelper programs can only be acting on a single package at a time. So if you have a package that builds many binary packages, you will need to also use the <code>-p</code> flag to specify which binary package the debhelper program will act on.</p>
<h3>udebs</h3>
<p>Debhelper includes support for udebs. To create a udeb with debhelper, add &quot;<code>Package-Type: udeb</code>&quot; to the package&#8217;s stanza in <i>debian/control</i>. Debhelper will try to create udebs that comply with debian-installer policy, by making the generated package files end in <i>.udeb</i>, not installing any documentation into a udeb, skipping over <i>preinst</i>, <i>postrm</i>, <i>prerm</i>, and <i>config</i> scripts, etc.</p>
<h2>Environment</h2>
<p>The following environment variables can influence the behavior of debhelper. It is important to note that these must be actual environment variables in order to function properly (not simply <i>Makefile</i> variables). To specify them properly in <i>debian/rules</i>, be sure to &quot;<code>export</code>&#8220; them. For example, &#8221;<code>export </code><font SIZE="-1"><code>DH_VERBOSE</code></font>&quot;.</p>
<dl>
<dt><font SIZE="-1"><code>DH_VERBOSE</code></font></p>
<dd>Set to <code>1</code> to enable verbose mode. Debhelper will output every command it runs. Also enables verbose build logs for some build systems like autoconf.</p>
<dt><font SIZE="-1"><code>DH_QUIET</code></font></p>
<dd>Set to <code>1</code> to enable quiet mode. Debhelper will not output commands calling the upstream build system nor will dh print which subcommands are called and depending on the upstream build system might make that more quiet, too. This makes it easier to spot important messages but makes the output quite useless as buildd log. Ignored if <font SIZE="-1">DH_VERBOSE</font> is also set.</p>
<dt><font SIZE="-1"><code>DH_COMPAT</code></font></p>
<dd>Temporarily specifies what compatibility level debhelper should run at, overriding any value in <i>debian/compat</i>.</p>
<dt><font SIZE="-1"><code>DH_NO_ACT</code></font></p>
<dd>Set to <code>1</code> to enable no-act mode.</p>
<dt><font SIZE="-1"><code>DH_OPTIONS</code></font></p>
<dd>Anything in this variable will be prepended to the command line arguments of all debhelper commands. </p>
<p> When using <i><a href="/docs/linux/man/1-dh/">dh</a></i>(1), it can be passed options that will be passed on to each debhelper command, which is generally better than using <font SIZE="-1">DH_OPTIONS.</font></p>
<dt><font SIZE="-1"><code>DH_ALWAYS_EXCLUDE</code></font></p>
<dd>If set, this adds the value the variable is set to to the <code>-X</code> options of all commands that support the <code>-X</code> option. Moreover, <code>dh_builddeb</code> will <code>rm -rf</code> anything that matches the value in your package build tree. </p>
<p> This can be useful if you are doing a build from a <font SIZE="-1">CVS</font> source tree, in which case setting <code>DH_ALWAYS_EXCLUDE=CVS</code> will prevent any <font SIZE="-1">CVS</font> directories from sneaking into the package you build. Or, if a package has a source tarball that (unwisely) includes <font SIZE="-1">CVS</font> directories, you might want to export <code>DH_ALWAYS_EXCLUDE=CVS</code> in <i>debian/rules</i>, to make it take effect wherever your package is built. </p>
<p> Multiple things to exclude can be separated with colons, as in <code>DH_ALWAYS_EXCLUDE=CVS:.svn</code></p>
<dt><font SIZE="-1"><code>DH_EXTRA_ADDONS</code></font></p>
<dd>If set, this adds the specified dh addons to be run in the appropriate places in the sequence of commands. This is equivalent to specifying the addon to run with the &#8211;with flag in the debian/rules file. Any &#8211;without calls specifying an addon in this environment variable will not be run. </p>
<p> This is intended to be used by downstreams or specific local configurations that require a debhelper addon to be run during multiple builds without having to patch a large number of rules file. If at all possible, this should be avoided in favor of a &#8211;with flag in the rules file.</dl>
<h2>See Also</h2>
<dl>
<dt><i>/usr/share/doc/debhelper/examples/</i></p>
<dd>A set of example <i>debian/rules</i> files that use debhelper.</p>
<dt>&lt;<a rel="nofollow" href="http://joeyh.name/code/debhelper/">http://joeyh.name/code/debhelper/</a>&gt;</p>
<dd>Debhelper web site.</dl>
<h2>Author</h2>
<p>Joey Hess &lt;joeyh [at] debian.org&gt;</p>
