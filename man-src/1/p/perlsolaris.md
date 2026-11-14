---
title: "perlsolaris(1)"
name: "perlsolaris"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlsolaris/"
description: "perlsolaris – Perl version 5 on Solaris systems"
---

<h2 class="name">NAME</h2>
<p> perlsolaris &#8211; Perl version 5 on Solaris systems </p>
<h2>DESCRIPTION</h2>
<p> This document describes various features of Sun&#8217;s Solaris operating system that will affect how Perl version 5 (hereafter just perl) is compiled and/or runs. Some issues relating to the older SunOS 4.x are also discussed, though they may be out of date. </p>
<p> For the most part, everything should just work. </p>
<p> Starting with Solaris 8, perl5.00503 (or higher) is supplied with the operating system, so you might not even need to build a newer version of perl at all. The Sun-supplied version is installed in /usr/perl5 with <i>/usr/bin/perl</i> pointing to <i>/usr/perl5/bin/perl</i>. Do not disturb that installation unless you really know what you are doing. If you remove the perl supplied with the <font SIZE="-1">OS,</font> you will render some bits of your system inoperable. If you wish to install a newer version of perl, install it under a different prefix from /usr/perl5. Common prefixes to use are /usr/local and /opt/perl. </p>
<p> You may wish to put your version of perl in the <font SIZE="-1">PATH</font> of all users by changing the link <i>/usr/bin/perl</i>. This is probably <font SIZE="-1">OK,</font> as most perl scripts shipped with Solaris use an explicit path. (There are a few exceptions, such as <i>/usr/bin/rpm2cpio</i> and <i>/etc/rcm/scripts/README</i>, but these are also sufficiently generic that the actual version of perl probably doesn&#8217;t matter too much.) </p>
<p> Solaris ships with a range of Solaris-specific modules. If you choose to install your own version of perl you will find the source of many of these modules is available on <font SIZE="-1">CPAN</font> under the Sun::Solaris:: namespace. </p>
<p> Solaris may include two versions of perl, e.g. Solaris 9 includes both 5.005_03 and 5.6.1. This is to provide stability across Solaris releases, in cases where a later perl version has incompatibilities with the version included in the preceding Solaris release. The default perl version will always be the most recent, and in general the old version will only be retained for one Solaris release. Note also that the default perl will <font SIZE="-1">NOT</font> be configured to search for modules in the older version, again due to compatibility/stability concerns. As a consequence if you upgrade Solaris, you will have to rebuild/reinstall any additional <font SIZE="-1">CPAN</font> modules that you installed for the previous Solaris version. See the <font SIZE="-1">CPAN</font> manpage under &#8216;autobundle&#8217; for a quick way of doing this. </p>
<p> As an interim measure, you may either change the #! line of your scripts to specifically refer to the old perl version, e.g. on Solaris 9 use #!/usr/perl5/5.00503/bin/perl to use the perl version that was the default for Solaris 8, or if you have a large number of scripts it may be more convenient to make the old version of perl the default on your system. You can do this by changing the appropriate symlinks under /usr/perl5 as follows (example for Solaris 9): </p>
<pre>
 # cd /usr/perl5
 # rm bin man pod
 # ln -s ./5.00503/bin
 # ln -s ./5.00503/man
 # ln -s ./5.00503/lib/pod
 # rm /usr/bin/perl
 # ln -s ../perl5/5.00503/bin/perl /usr/bin/perl
</pre>
<p> In both cases this should only be considered to be a temporary measure &#8211; you should upgrade to the later version of perl as soon as is practicable. </p>
<p> Note also that the perl command-line utilities (e.g. perldoc) and any that are added by modules that you install will be under /usr/perl5/bin, so that directory should be added to your <font SIZE="-1">PATH.</font></p>
<h3>Solaris Version Numbers.</h3>
<p> For consistency with common usage, perl&#8217;s Configure script performs some minor manipulations on the operating system name and version number as reported by uname. Here&#8217;s a partial translation table: </p>
<pre>
          Sun:                      perl's Configure:
 uname    uname -r   Name           osname     osvers
 SunOS    4.1.3     Solaris 1.1     sunos      4.1.3
 SunOS    5.6       Solaris 2.6     solaris    2.6
 SunOS    5.8       Solaris 8       solaris    2.8
 SunOS    5.9       Solaris 9       solaris    2.9
 SunOS    5.10      Solaris 10      solaris    2.10
</pre>
<p> The complete table can be found in the Sun Managers&#8217; <font SIZE="-1">FAQ</font> &lt;<a href="ftp://ftp.cs.toronto.edu/pub/jdd/sunmanagers/faq">ftp://ftp.cs.toronto.edu/pub/jdd/sunmanagers/faq</a>&gt; under &#8220;9.1) Which Sun models run which versions of SunOS?&#8221;.</p>
<h2>RESOURCES</h2>
<p> There are many, many sources for Solaris information. A few of the important ones for perl:</p>
<dl>
<dt>Solaris <font SIZE="-1">FAQ</font></p>
<dd> The Solaris <font SIZE="-1">FAQ</font> is available at &lt;<a rel="nofollow" href="http://www.science.uva.nl/pub/solaris/solaris2.html">http://www.science.uva.nl/pub/solaris/solaris2.html</a>&gt;. </p>
<p> The Sun Managers&#8217; <font SIZE="-1">FAQ</font> is available at &lt;<a href="ftp://ftp.cs.toronto.edu/pub/jdd/sunmanagers/faq">ftp://ftp.cs.toronto.edu/pub/jdd/sunmanagers/faq</a>&gt;</p>
<dt>Precompiled Binaries</p>
<dd> Precompiled binaries, links to many sites, and much, much more are available at &lt;<a rel="nofollow" href="http://www.sunfreeware.com/">http://www.sunfreeware.com/</a>&gt; and &lt;<a rel="nofollow" href="http://www.blastwave.org/">http://www.blastwave.org/</a>&gt;.</p>
<dt>Solaris Documentation</p>
<dd> All Solaris documentation is available on-line at &lt;<a rel="nofollow" href="http://docs.sun.com/">http://docs.sun.com/</a>&gt;.</dl>
<h2>SETTING UP</h2>
<h3>File Extraction Problems on Solaris.</h3>
<p> Be sure to use a tar program compiled under Solaris (not SunOS 4.x) to extract the perl-5.x.x.tar.gz file. Do not use <font SIZE="-1">GNU</font> tar compiled for SunOS4 on Solaris. (<font SIZE="-1">GNU</font> tar compiled for Solaris should be fine.) When you run SunOS4 binaries on Solaris, the run-time system magically alters pathnames matching m#lib/locale# so that when tar tries to create lib/locale.pm, a file named lib/oldlocale.pm gets created instead. If you found this advice too late and used a SunOS4-compiled tar anyway, you must find the incorrectly renamed file and move it back to lib/locale.pm.</p>
<h3>Compiler and Related Tools on Solaris.</h3>
<p> You must use an <font SIZE="-1">ANSI C</font> compiler to build perl. Perl can be compiled with either Sun&#8217;s add-on C compiler or with gcc. The C compiler that shipped with SunOS4 will not do. </p>
<p> <i>Include /usr/ccs/bin/ in your </i><font SIZE="-1"><i>PATH.</i></font><i></i> </p>
<p> Several tools needed to build perl are located in /usr/ccs/bin/: ar, as, ld, and make. Make sure that /usr/ccs/bin/ is in your <font SIZE="-1">PATH.</font> </p>
<p> On all the released versions of Solaris (8, 9 and 10) you need to make sure the following packages are installed (this info is extracted from the Solaris <font SIZE="-1">FAQ</font>): </p>
<p> for tools (sccs, lex, yacc, make, nm, truss, ld, as): SUNWbtool, SUNWsprot, SUNWtoo </p>
<p> for libraries &amp; headers: SUNWhea, SUNWarc, SUNWlibm, SUNWlibms, SUNWdfbh, SUNWcg6h, SUNWxwinc </p>
<p> Additionally, on Solaris 8 and 9 you also need: </p>
<p> for 64 bit development: SUNWarcx, SUNWbtoox, SUNWdplx, SUNWscpux, SUNWsprox, SUNWtoox, SUNWlmsx, SUNWlmx, SUNWlibCx </p>
<p> And only on Solaris 8 you also need: </p>
<p> for libraries &amp; headers: SUNWolinc </p>
<p> If you are in doubt which package contains a file you are missing, try to find an installation that has that file. Then do a </p>
<pre>
 $ grep /my/missing/file /var/sadm/install/contents
</pre>
<p> This will display a line like this: </p>
<p> /usr/include/sys/errno.h f none 0644 root bin 7471 37605 956241356 SUNWhea </p>
<p> The last item listed (SUNWhea in this example) is the package you need. </p>
<p> <i>Avoid /usr/ucb/cc.</i> </p>
<p> You don&#8217;t need to have /usr/ucb/ in your <font SIZE="-1">PATH</font> to build perl. If you want /usr/ucb/ in your <font SIZE="-1">PATH</font> anyway, make sure that /usr/ucb/ is <font SIZE="-1">NOT</font> in your <font SIZE="-1">PATH</font> before the directory containing the right C compiler. </p>
<p> <i>Sun&#8217;s C Compiler</i> </p>
<p> If you use Sun&#8217;s C compiler, make sure the correct directory (usually /opt/SUNWspro/bin/) is in your <font SIZE="-1">PATH</font> (before /usr/ucb/). </p>
<p> <i></i><font SIZE="-1"><i>GCC</i></font><i></i> </p>
<p> If you use gcc, make sure your installation is recent and complete. perl versions since 5.6.0 build fine with gcc &gt; 2.8.1 on Solaris &gt;= 2.6. </p>
<p> You must Configure perl with </p>
<pre>
 $ sh Configure -Dcc=gcc
</pre>
<p> If you don&#8217;t, you may experience strange build errors. </p>
<p> If you have updated your Solaris version, you may also have to update your gcc. For example, if you are running Solaris 2.6 and your gcc is installed under /usr/local, check in /usr/local/lib/gcc-lib and make sure you have the appropriate directory, sparc-sun-solaris2.6/ or i386-pc-solaris2.6/. If gcc&#8217;s directory is for a different version of Solaris than you are running, then you will need to rebuild gcc for your new version of Solaris. </p>
<p> You can get a precompiled version of gcc from &lt;<a rel="nofollow" href="http://www.sunfreeware.com/">http://www.sunfreeware.com/</a>&gt; or &lt;<a rel="nofollow" href="http://www.blastwave.org/">http://www.blastwave.org/</a>&gt;. Make sure you pick up the package for your Solaris release. </p>
<p> If you wish to use gcc to build add-on modules for use with the perl shipped with Solaris, you should use the Solaris::PerlGcc module which is available from <font SIZE="-1">CPAN.</font> The perl shipped with Solaris is configured and built with the Sun compilers, and the compiler configuration information stored in Config.pm is therefore only relevant to the Sun compilers. The Solaris:PerlGcc module contains a replacement Config.pm that is correct for gcc &#8211; see the module for details. </p>
<p> <i></i><font SIZE="-1"><i>GNU</i></font><i> as and </i><font SIZE="-1"><i>GNU</i></font><i> ld</i> </p>
<p> The following information applies to gcc version 2. Volunteers to update it as appropriately for gcc version 3 would be appreciated. </p>
<p> The versions of as and ld supplied with Solaris work fine for building perl. There is normally no need to install the <font SIZE="-1">GNU</font> versions to compile perl. </p>
<p> If you decide to ignore this advice and use the <font SIZE="-1">GNU</font> versions anyway, then be sure that they are relatively recent. Versions newer than 2.7 are apparently new enough. Older versions may have trouble with dynamic loading. </p>
<p> If you wish to use <font SIZE="-1">GNU</font> ld, then you need to pass it the -Wl,-E flag. The hints/solaris_2.sh file tries to do this automatically by setting the following Configure variables: </p>
<pre>
 ccdlflags=&quot;$ccdlflags -Wl,-E&quot;
 lddlflags=&quot;$lddlflags -Wl,-E -G&quot;
</pre>
<p> However, over the years, changes in gcc, <font SIZE="-1">GNU</font> ld, and Solaris ld have made it difficult to automatically detect which ld ultimately gets called. You may have to manually edit config.sh and add the -Wl,-E flags yourself, or else run Configure interactively and add the flags at the appropriate prompts. </p>
<p> If your gcc is configured to use <font SIZE="-1">GNU</font> as and ld but you want to use the Solaris ones instead to build perl, then you&#8217;ll need to add -B/usr/ccs/bin/ to the gcc command line. One convenient way to do that is with </p>
<pre>
 $ sh Configure -Dcc='gcc -B/usr/ccs/bin/'
</pre>
<p> Note that the trailing slash is required. This will result in some harmless warnings as Configure is run: </p>
<pre>
 gcc: file path prefix `/usr/ccs/bin/' never used
</pre>
<p> These messages may safely be ignored. (Note that for a SunOS4 system, you must use -B/bin/ instead.) </p>
<p> Alternatively, you can use the <font SIZE="-1">GCC_EXEC_PREFIX</font> environment variable to ensure that Sun&#8217;s as and ld are used. Consult your gcc documentation for further information on the -B option and the <font SIZE="-1">GCC_EXEC_PREFIX</font> variable. </p>
<p> <i>Sun and </i><font SIZE="-1"><i>GNU</i></font><i> make</i> </p>
<p> The make under /usr/ccs/bin works fine for building perl. If you have the Sun C compilers, you will also have a parallel version of make (dmake). This works fine to build perl, but can sometimes cause problems when running &#8216;make test&#8217; due to underspecified dependencies between the different test harness files. The same problem can also affect the building of some add-on modules, so in those cases either specify &#8216;-m serial&#8217; on the dmake command line, or use /usr/ccs/bin/make instead. If you wish to use <font SIZE="-1">GNU</font> make, be sure that the set-group-id bit is not set. If it is, then arrange your <font SIZE="-1">PATH</font> so that /usr/ccs/bin/make is before <font SIZE="-1">GNU</font> make or else have the system administrator disable the set-group-id bit on <font SIZE="-1">GNU</font> make. </p>
<p> <i>Avoid libucb.</i> </p>
<p> Solaris provides some BSD-compatibility functions in /usr/ucblib/libucb.a. Perl will not build and run correctly if linked against -lucb since it contains routines that are incompatible with the standard Solaris libc. Normally this is not a problem since the solaris hints file prevents Configure from even looking in /usr/ucblib for libraries, and also explicitly omits -lucb.</p>
<h3>Environment for Compiling perl on Solaris</h3>
<p> <i></i><font SIZE="-1"><i>PATH</i></font><i></i> </p>
<p> Make sure your <font SIZE="-1">PATH</font> includes the compiler (/opt/SUNWspro/bin/ if you&#8217;re using Sun&#8217;s compiler) as well as /usr/ccs/bin/ to pick up the other development tools (such as make, ar, as, and ld). Make sure your path either doesn&#8217;t include /usr/ucb or that it includes it after the compiler and compiler tools and other standard Solaris directories. You definitely don&#8217;t want /usr/ucb/cc. </p>
<p> <i></i><font SIZE="-1"><i>LD_LIBRARY_PATH</i></font><i></i> </p>
<p> If you have the <font SIZE="-1">LD_LIBRARY_PATH</font> environment variable set, be sure that it does <font SIZE="-1">NOT</font> include /lib or /usr/lib. If you will be building extensions that call third-party shared libraries (e.g. Berkeley <font SIZE="-1">DB</font>) then make sure that your <font SIZE="-1">LD_LIBRARY_PATH</font> environment variable includes the directory with that library (e.g. /usr/local/lib). </p>
<p> If you get an error message </p>
<pre>
 dlopen: stub interception failed
</pre>
<p> it is probably because your <font SIZE="-1">LD_LIBRARY_PATH</font> environment variable includes a directory which is a symlink to /usr/lib (such as /lib). The reason this causes a problem is quite subtle. The file libdl.so.1.0 actually *only* contains functions which generate &#8216;stub interception failed&#8217; errors! The runtime linker intercepts links to &#8220;/usr/lib/libdl.so.1.0&#8221; and links in internal implementations of those functions instead. [Thanks to Tim Bunce for this explanation.]</p>
<h2>RUN CONFIGURE.</h2>
<p> See the <font SIZE="-1">INSTALL</font> file for general information regarding Configure. Only Solaris-specific issues are discussed here. Usually, the defaults should be fine.</p>
<h3>64-bit perl on Solaris.</h3>
<p> See the <font SIZE="-1">INSTALL</font> file for general information regarding 64-bit compiles. In general, the defaults should be fine for most people. </p>
<p> By default, perl-5.6.0 (or later) is compiled as a 32-bit application with largefile and long-long support. </p>
<p> <i>General 32-bit vs. 64-bit issues.</i> </p>
<p> Solaris 7 and above will run in either 32 bit or 64 bit mode on <font SIZE="-1">SPARC</font> CPUs, via a reboot. You can build 64 bit apps whilst running 32 bit mode and vice-versa. 32 bit apps will run under Solaris running in either 32 or 64 bit mode. 64 bit apps require Solaris to be running 64 bit mode. </p>
<p> Existing 32 bit apps are properly known as <font SIZE="-1">LP32,</font> i.e. Longs and Pointers are 32 bit. 64-bit apps are more properly known as <font SIZE="-1">LP64.</font> The discriminating feature of a <font SIZE="-1">LP64</font> bit app is its ability to utilise a 64-bit address space. It is perfectly possible to have a <font SIZE="-1">LP32</font> bit app that supports both 64-bit integers (long long) and largefiles (&gt; 2GB), and this is the default for perl-5.6.0. </p>
<p> For a more complete explanation of 64-bit issues, see the &#8220;Solaris 64-bit Developer&#8217;s Guide&#8221; at &lt;<a rel="nofollow" href="http://docs.sun.com/">http://docs.sun.com/</a>&gt; </p>
<p> You can detect the <font SIZE="-1">OS</font> mode using &#8220;isainfo -v&#8221;, e.g. </p>
<pre>
 $ isainfo -v   # Ultra 30 in 64 bit mode
 64-bit sparcv9 applications
 32-bit sparc applications
</pre>
<p> By default, perl will be compiled as a 32-bit application. Unless you want to allocate more than ~ 4GB of memory inside perl, or unless you need more than 255 open file descriptors, you probably don&#8217;t need perl to be a 64-bit app. </p>
<p> <i>Large File Support</i> </p>
<p> For Solaris 2.6 and onwards, there are two different ways for 32-bit applications to manipulate large files (files whose size is &gt; 2GByte). (A 64-bit application automatically has largefile support built in by default.) </p>
<p> First is the &#8220;transitional compilation environment&#8221;, described in <code><a href="/docs/linux/man/5-lfcompile64/">lfcompile64</a></code>(5). According to the man page, </p>
<pre>
 The transitional compilation  environment  exports  all  the
 explicit 64-bit functions (xxx64()) and types in addition to
 all the regular functions (xxx()) and types. Both xxx()  and
 xxx64()  functions  are  available to the program source.  A
 32-bit application must use the xxx64() functions in  order
 to  access  large  files.  See the <a href="//www.systutorials.com/docs/linux/man/5-lf64/">lf64</a>(5) manual page for a
 complete listing of the 64-bit transitional interfaces.
</pre>
<p> The transitional compilation environment is obtained with the following compiler and linker flags: </p>
<pre>
 getconf LFS64_CFLAGS        -D_LARGEFILE64_SOURCE
 getconf LFS64_LDFLAG        # nothing special needed
 getconf LFS64_LIBS          # nothing special needed
</pre>
<p> Second is the &#8220;large file compilation environment&#8221;, described in <code><a href="/docs/linux/man/5-lfcompile/">lfcompile</a></code>(5). According to the man page, </p>
<pre>
 Each interface named xxx() that needs to access 64-bit entities
 to  access  large  files maps to a xxx64() call in the
 resulting binary. All relevant data types are defined to  be
 of correct size (for example, off_t has a typedef definition
 for a 64-bit entity).
 An application compiled in this environment is able  to  use
 the  xxx()  source interfaces to access both large and small
 files, rather than having to explicitly utilize the  transitional
 xxx64()  interface  calls to access large files.
</pre>
<p> Two exceptions are <code>fseek()</code> and <code>ftell()</code>. 32-bit applications should use <a href="//www.systutorials.com/docs/linux/man/3C-fseeko/">fseeko</a>(3C) and <a href="//www.systutorials.com/docs/linux/man/3C-ftello/">ftello</a>(3C). These will get automatically mapped to <code>fseeko64()</code> and <code>ftello64()</code>. </p>
<p> The large file compilation environment is obtained with </p>
<pre>
 getconf LFS_CFLAGS      -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64
 getconf LFS_LDFLAGS     # nothing special needed
 getconf LFS_LIBS        # nothing special needed
</pre>
<p> By default, perl uses the large file compilation environment and relies on Solaris to do the underlying mapping of interfaces. </p>
<p> <i>Building an </i><font SIZE="-1"><i>LP64</i></font><i> perl</i> </p>
<p> To compile a 64-bit application on an UltraSparc with a recent Sun Compiler, you need to use the flag &#8220;-xarch=v9&#8221;. <code><a href="/docs/linux/man/1-getconf/">getconf</a></code>(1) will tell you this, e.g. </p>
<pre>
 $ getconf -a | grep v9
 XBS5_LP64_OFF64_CFLAGS:         -xarch=v9
 XBS5_LP64_OFF64_LDFLAGS:        -xarch=v9
 XBS5_LP64_OFF64_LINTFLAGS:      -xarch=v9
 XBS5_LPBIG_OFFBIG_CFLAGS:       -xarch=v9
 XBS5_LPBIG_OFFBIG_LDFLAGS:      -xarch=v9
 XBS5_LPBIG_OFFBIG_LINTFLAGS:    -xarch=v9
 _XBS5_LP64_OFF64_CFLAGS:        -xarch=v9
 _XBS5_LP64_OFF64_LDFLAGS:       -xarch=v9
 _XBS5_LP64_OFF64_LINTFLAGS:     -xarch=v9
 _XBS5_LPBIG_OFFBIG_CFLAGS:      -xarch=v9
 _XBS5_LPBIG_OFFBIG_LDFLAGS:     -xarch=v9
 _XBS5_LPBIG_OFFBIG_LINTFLAGS:   -xarch=v9
</pre>
<p> This flag is supported in Sun WorkShop Compilers 5.0 and onwards (now marketed under the name Forte) when used on Solaris 7 or later on UltraSparc systems. </p>
<p> If you are using gcc, you would need to use -mcpu=v9 -m64 instead. This option is not yet supported as of gcc 2.95.2; from install/SPECIFIC in that release: </p>
<pre>
 GCC version 2.95 is not able to compile code correctly for sparc64
 targets. Users of the Linux kernel, at least, can use the sparc32
 program to start up a new shell invocation with an environment that
 causes configure to recognize (via uname -a) the system as sparc-*-*
 instead.
</pre>
<p> All this should be handled automatically by the hints file, if requested. </p>
<p> <i>Long Doubles.</i> </p>
<p> As of 5.8.1, long doubles are working if you use the Sun compilers (needed for additional math routines not included in libm).</p>
<h3>Threads in perl on Solaris.</h3>
<p> It is possible to build a threaded version of perl on Solaris. The entire perl thread implementation is still experimental, however, so beware.</p>
<h3>Malloc Issues with perl on Solaris.</h3>
<p> Starting from perl 5.7.1 perl uses the Solaris malloc, since the perl malloc breaks when dealing with more than 2GB of memory, and the Solaris malloc also seems to be faster. </p>
<p> If you for some reason (such as binary backward compatibility) really need to use perl&#8217;s malloc, you can rebuild perl from the sources and Configure the build with </p>
<pre>
 $ sh Configure -Dusemymalloc
</pre>
<p> You should not use perl&#8217;s malloc if you are building with gcc. There are reports of core dumps, especially in the <font SIZE="-1">PDL</font> module. The problem appears to go away under -DDEBUGGING, so it has been difficult to track down. Sun&#8217;s compiler appears to be okay with or without perl&#8217;s malloc. [<font SIZE="-1">XXX</font> further investigation is needed here.]</p>
<h2>MAKE PROBLEMS.</h2>
<dl>
<dt>Dynamic Loading Problems With <font SIZE="-1">GNU</font> as and <font SIZE="-1">GNU</font> ld</p>
<dd> If you have problems with dynamic loading using gcc on SunOS or Solaris, and you are using <font SIZE="-1">GNU</font> as and <font SIZE="-1">GNU</font> ld, see the section &#8220;<font SIZE="-1">GNU</font> as and <font SIZE="-1">GNU</font> ld&#8221; above.</p>
<dt>ld.so.1: ./perl: fatal: relocation error:</p>
<dd> If you get this message on SunOS or Solaris, and you&#8217;re using gcc, it&#8217;s probably the <font SIZE="-1">GNU</font> as or <font SIZE="-1">GNU</font> ld problem in the previous item &#8220;<font SIZE="-1">GNU</font> as and <font SIZE="-1">GNU</font> ld&#8221;.</p>
<dt>dlopen: stub interception failed</p>
<dd> The primary cause of the &#8216;dlopen: stub interception failed&#8217; message is that the <font SIZE="-1">LD_LIBRARY_PATH</font> environment variable includes a directory which is a symlink to /usr/lib (such as /lib). See &#8220;<font SIZE="-1">LD_LIBRARY_PATH&#8221;</font> above.</p>
<dt>#error &quot;No <font SIZE="-1">DATAMODEL_NATIVE</font> specified&quot;</p>
<dd> This is a common error when trying to build perl on Solaris 2.6 with a gcc installation from Solaris 2.5 or 2.5.1. The Solaris header files changed, so you need to update your gcc installation. You can either rerun the fixincludes script from gcc or take the opportunity to update your gcc installation.</p>
<dt>sh: ar: not found</p>
<dd> This is a message from your shell telling you that the command &#8216;ar&#8217; was not found. You need to check your <font SIZE="-1">PATH</font> environment variable to make sure that it includes the directory with the &#8216;ar&#8217; command. This is a common problem on Solaris, where &#8216;ar&#8217; is in the /usr/ccs/bin/ directory.</dl>
<h2>MAKE TEST</h2>
<h3>op/stat.t test 4 in Solaris</h3>
<p> <i>op/stat.t</i> test 4 may fail if you are on a tmpfs of some sort. Building in /tmp sometimes shows this behavior. The test suite detects if you are building in /tmp, but it may not be able to catch all tmpfs situations.</p>
<h3>nss_delete core dump from op/pwent or op/grent</h3>
<p> See &#8220;nss_delete core dump from op/pwent or op/grent&#8221; in perlhpux.</p>
<h2>CROSS-COMPILATION</h2>
<p> Nothing too unusual here. You can easily do this if you have a cross-compiler available; A usual Configure invocation when targetting a Solaris x86 looks something like this: </p>
<pre>
    sh ./Configure -des -Dusecrosscompile \
        -Dcc=i386-pc-solaris2.11-gcc      \
        -Dsysroot=$SYSROOT                \
        -Alddlflags=&quot; -Wl,-z,notext&quot;      \
        -Dtargethost=... # The usual cross-compilation options
</pre>
<p> The lddlflags addition is the only abnormal bit.</p>
<h2>PREBUILT BINARIES OF PERL FOR SOLARIS.</h2>
<p> You can pick up prebuilt binaries for Solaris from &lt;<a rel="nofollow" href="http://www.sunfreeware.com/">http://www.sunfreeware.com/</a>&gt;, &lt;<a rel="nofollow" href="http://www.blastwave.org">http://www.blastwave.org</a>&gt;, ActiveState &lt;<a rel="nofollow" href="http://www.activestate.com/">http://www.activestate.com/</a>&gt;, and &lt;<a rel="nofollow" href="http://www.perl.com/">http://www.perl.com/</a>&gt; under the Binaries list at the top of the page. There are probably other sources as well. Please note that these sites are under the control of their respective owners, not the perl developers.</p>
<h2>RUNTIME ISSUES FOR PERL ON SOLARIS.</h2>
<h3>Limits on Numbers of Open Files on Solaris.</h3>
<p> The <a href="//www.systutorials.com/docs/linux/man/3C-stdio/">stdio</a>(3C) manpage notes that for <font SIZE="-1">LP32</font> applications, only 255 files may be opened using <code>fopen()</code>, and only file descriptors 0 through 255 can be used in a stream. Since perl calls <code>open()</code> and then <a href="//www.systutorials.com/docs/linux/man/3C-fdopen/">fdopen</a>(3C) with the resulting file descriptor, perl is limited to 255 simultaneous open files, even if <code>sysopen()</code> is used. If this proves to be an insurmountable problem, you can compile perl as a <font SIZE="-1">LP64</font> application, see &#8220;Building an <font SIZE="-1">LP64</font> perl&#8221; for details. Note also that the default resource limit for open file descriptors on Solaris is 255, so you will have to modify your ulimit or rctl (Solaris 9 onwards) appropriately.</p>
<h2>SOLARIS-SPECIFIC MODULES.</h2>
<p> See the modules under the Solaris:: and Sun::Solaris namespaces on <font SIZE="-1">CPAN,</font> see &lt;<a rel="nofollow" href="http://www.cpan.org/modules/by-module/Solaris/">http://www.cpan.org/modules/by-module/Solaris/</a>&gt; and &lt;<a rel="nofollow" href="http://www.cpan.org/modules/by-module/Sun/">http://www.cpan.org/modules/by-module/Sun/</a>&gt;.</p>
<h2>SOLARIS-SPECIFIC PROBLEMS WITH MODULES.</h2>
<h3>Proc::ProcessTable on Solaris</h3>
<p> Proc::ProcessTable does not compile on Solaris with perl5.6.0 and higher if you have <font SIZE="-1">LARGEFILES</font> defined. Since largefile support is the default in 5.6.0 and later, you have to take special steps to use this module. </p>
<p> The problem is that various structures visible via procfs use off_t, and if you compile with largefile support these change from 32 bits to 64 bits. Thus what you get back from procfs doesn&#8217;t match up with the structures in perl, resulting in garbage. See <code><a href="/docs/linux/man/4-proc/">proc</a></code>(4) for further discussion. </p>
<p> A fix for Proc::ProcessTable is to edit Makefile to explicitly remove the largefile flags from the ones MakeMaker picks up from Config.pm. This will result in Proc::ProcessTable being built under the correct environment. Everything should then be <font SIZE="-1">OK</font> as long as Proc::ProcessTable doesn&#8217;t try to share off_t&#8217;s with the rest of perl, or if it does they should be explicitly specified as off64_t.</p>
<h3>BSD::Resource on Solaris</h3>
<p> BSD::Resource versions earlier than 1.09 do not compile on Solaris with perl 5.6.0 and higher, for the same reasons as Proc::ProcessTable. BSD::Resource versions starting from 1.09 have a workaround for the problem.</p>
<h3>Net::SSLeay on Solaris</h3>
<p> Net::SSLeay requires a /dev/urandom to be present. This device is available from Solaris 9 onwards. For earlier Solaris versions you can either get the package SUNWski (packaged with several Sun software products, for example the Sun WebServer, which is part of the Solaris Server Intranet Extension, or the Sun Directory Services, part of Solaris for ISPs) or download the ANDIrand package from &lt;<a rel="nofollow" href="http://www.cosy.sbg.ac.at/~andi/">http://www.cosy.sbg.ac.at/~andi/</a>&gt;. If you use SUNWski, make a symbolic link /dev/urandom pointing to /dev/random. For more details, see Document <font SIZE="-1">ID27606</font> entitled &#8220;Differing /dev/random support requirements within Solaris[<font SIZE="-1">TM</font>] Operating Environments&#8221;, available at &lt;<a rel="nofollow" href="http://sunsolve.sun.com">http://sunsolve.sun.com</a>&gt; . </p>
<p> It may be possible to use the Entropy Gathering Daemon (written in Perl!), available from &lt;<a rel="nofollow" href="http://www.lothar.com/tech/crypto/">http://www.lothar.com/tech/crypto/</a>&gt;.</p>
<h2>SunOS 4.x</h2>
<p> In SunOS 4.x you most probably want to use the SunOS ld, /usr/bin/ld, since the more recent versions of <font SIZE="-1">GNU</font> ld (like 2.13) do not seem to work for building Perl anymore. When linking the extensions, the <font SIZE="-1">GNU</font> ld gets very unhappy and spews a lot of errors like this </p>
<pre>
  ... relocation truncated to fit: BASE13 ...
</pre>
<p> and dies. Therefore the SunOS 4.1 hints file explicitly sets the ld to be <i>/usr/bin/ld</i>. </p>
<p> As of Perl 5.8.1 the dynamic loading of libraries (DynaLoader, XSLoader) also seems to have become broken in in SunOS 4.x. Therefore the default is to build Perl statically. </p>
<p> Running the test suite in SunOS 4.1 is a bit tricky since the <i>dist/Tie-File/t/09_gen_rs.t</i> test hangs (subtest #51, <font SIZE="-1">FWIW</font>) for some unknown reason. Just stop the test and kill that particular Perl process. </p>
<p> There are various other failures, that as of SunOS 4.1.4 and gcc 3.2.2 look a lot like gcc bugs. Many of the failures happen in the Encode tests, where for example when the test expects &#8220;0&#8221; you get &#8220;&amp;#48;&#8221; which should after a little squinting look very odd indeed. Another example is earlier in <i>t/run/fresh_perl</i> where <code>chr</code>(0xff) is expected but the test fails because the result is <code>chr</code>(0xff). Exactly. </p>
<p> This is the &#8220;make test&#8221; result from the said combination: </p>
<pre>
  Failed 27 test scripts out of 745, 96.38% okay.
</pre>
<p> Running the <tt>&quot;harness&quot;</tt> is painful because of the many failing Unicode-related tests will output megabytes of failure messages, but if one patiently waits, one gets these results: </p>
<pre><code>
Failed Test Stat Wstat Total Fail Failed List of Failed-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -...
            ../
        ext / Encode / t / at -
    cn.t 4 1024 29 4 13.79 % 14 - 17../ ext / Encode / t / at - tw.t 10 2560 17 10 58.82 % 2 4 6 8 10 12 14 - 17../ ext / Encode / t / enc_data.t 29 7424
    ? ? ? ? %
    ?     ?../ ext / Encode / t / enc_eucjp.t 29 7424
    ? ? ? ? %
    ?     ?../ ext / Encode / t / enc_module.t 29 7424
    ? ? ? ? %
    ?     ?../ ext / Encode / t / encoding.t 29 7424
    ? ? ? ? %
    ?     ?../ ext / Encode / t / grow.t 12 3072 24 12 50.00 % 2 4 6 8 10 12 14 16 18 20 22 24 Failed Test Stat Wstat Total Fail Failed List of Failed-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --../ ext / Encode / t / guess.t 255 65280 29 40 137.93 % 10 - 29../ ext / Encode / t / jperl.t 29 7424 15 30 200.00 % 1 - 15../ ext / Encode / t / mime - header.t 2 512 10 2 20.00 % 2 - 3../ ext / Encode / t / perlio.t 22 5632 38 22 57.89 % 1 - 4 9 - 16 19 - 20 23 - 24 27 - 32../ ext / List / Util / t / shuffle.t 0 139
    ? ? ? ? %
    ?     ?../ ext / PerlIO / t / encoding.t 14 1 7.14 % 11../ ext / PerlIO / t / fallback.t 9 2 22.22 % 3 5../ ext / Socket / t / socketpair.t 0 2 45 70 155.56 % 11 - 45
                                                                                                                                                                            ../
                                                                                                                                                                        lib / CPAN / t / vcmp.t 30 1 3.33 % 25../ lib / Tie / File / t / 09_gen_rs.t 0 15
    ? ? ? ? %
    ?     ?../ lib / Unicode / Collate / t / test.t 199 30 15.08 % 7 26 - 27 71 - 75 81 - 88 95 101 103 - 104 106 108 -
           109 122 124 161 169 - 172../ lib / sort.t 0 139 119 26 21.85 % 107 - 119 op / alarm.t 4 1 25.00 % 4 op / utfhash.t 97 1 1.03 % 31 run / fresh_perl.t 91 1 1.10 % 32 uni / tr_7jis.t
    ? ? ? ? %
    ?     ? uni / tr_eucjp.t 29 7424 6 12 200.00 % 1 - 6 uni / tr_sjis.t 29 7424 6 12 200.00 % 1 - 6 56 tests and 467 subtests skipped.Failed 27 / 811 test scripts,
    96.67 % okay.1383 / 75399 subtests failed,
    98.17 % okay.
</code></pre>
<p> The <code>alarm()</code> test failure is caused by <code>system()</code> apparently blocking <code>alarm()</code>. That is probably a libc bug, and given that SunOS 4.x has been end-of-lifed years ago, don&#8217;t hold your breath for a fix. In addition to that, don&#8217;t try anything too Unicode-y, especially with Encode, and you should be fine in SunOS 4.x.</p>
<h2>AUTHOR</h2>
<p> The original was written by Andy Dougherty <i>doughera [at] lafayette.edu</i> drawing heavily on advice from Alan Burlison, Nick Ing-Simmons, Tim Bunce, and many other Solaris users over the years. </p>
<p> Please report any errors, updates, or suggestions to <i>perlbug [at] perl.org</i>. </p>
<h2>Index</h2>
