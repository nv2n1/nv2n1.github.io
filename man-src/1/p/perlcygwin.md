---
title: "perlcygwin(1)"
name: "perlcygwin"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlcygwin/"
description: "perlcygwin – Perl for Cygwin"
---

<h2 class="name">NAME</h2>
<p> perlcygwin &#8211; Perl for Cygwin </p>
<h2>SYNOPSIS</h2>
<p> This document will help you configure, make, test and install Perl on Cygwin. This document also describes features of Cygwin that will affect how Perl behaves at runtime. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> There are pre-built Perl packages available for Cygwin and a version of Perl is provided in the normal Cygwin install. If you do not need to customize the configuration, consider using one of those packages.</p>
<h2>PREREQUISITES FOR COMPILING PERL ON CYGWIN</h2>
<h3>Cygwin = GNU+Cygnus+Windows (Don&#8217;t leave <font SIZE="-1">UNIX</font> without it)</h3>
<p> The Cygwin tools are ports of the popular <font SIZE="-1">GNU</font> development tools for Win32 platforms. They run thanks to the Cygwin library which provides the <font SIZE="-1">UNIX</font> system calls and environment these programs expect. More information about this project can be found at: </p>
<p> &lt;<a rel="nofollow" href="http://www.cygwin.com/">http://www.cygwin.com/</a>&gt; </p>
<p> A recent net or commercial release of Cygwin is required. </p>
<p> At the time this document was last updated, Cygwin 1.7.16 was current.</p>
<h3>Cygwin Configuration</h3>
<p> While building Perl some changes may be necessary to your Cygwin setup so that Perl builds cleanly. These changes are <code>not</code> required for normal Perl usage. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> The binaries that are built will run on all Win32 versions. They do not depend on your host system (WinXP/Win2K/Win7) or your Cygwin configuration (binary/text mounts, cvgserver). The only dependencies come from hard-coded pathnames like <i>/usr/local</i>. However, your host system and Cygwin configuration will affect Perl&#8217;s runtime behavior (see &#8220;<font SIZE="-1">TEST&#8221;</font>).</p>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;PATH&quot;</tt> </p>
<p> Set the <tt>&quot;PATH&quot;</tt> environment variable so that Configure finds the Cygwin versions of programs. Any not-needed Windows directories should be removed or moved to the end of your <tt>&quot;PATH&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <i>nroff</i> </p>
<p> If you do not have <i>nroff</i> (which is part of the <i>groff</i> package), Configure will <code>not</code> prompt you to install <i>man</i> pages.</dl>
<h2>CONFIGURE PERL ON CYGWIN</h2>
<p> The default options gathered by Configure with the assistance of <i>hints/cygwin.sh</i> will build a Perl that supports dynamic loading (which requires a shared <i>cygperl5_16.dll</i>). </p>
<p> This will run Configure and keep a record: </p>
<pre>
  ./Configure 2&gt;&amp;1 | tee log.configure
</pre>
<p> If you are willing to accept all the defaults run Configure with <code>-de</code>. However, several useful customizations are available.</p>
<h3>Stripping Perl Binaries on Cygwin</h3>
<p> It is possible to strip the EXEs and DLLs created by the build process. The resulting binaries will be significantly smaller. If you want the binaries to be stripped, you can either add a <code>-s</code> option when Configure prompts you, </p>
<pre><code>
Any additional ld flags(NOT including libraries) ? [none] - s
                                                       Any special flags to pass to g++ to create a dynamically loaded
                                                       library
    ? [none] - s
          Any special flags to pass to gcc to use dynamic linking
    ? [none] - s
</code></pre>
<p> or you can edit <i>hints/cygwin.sh</i> and uncomment the relevant variables near the end of the file.</p>
<h3>Optional Libraries for Perl on Cygwin</h3>
<p> Several Perl functions and modules depend on the existence of some optional libraries. Configure will find them if they are installed in one of the directories listed as being used for library searches. Pre-built packages for most of these are available from the Cygwin installer.</p>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;-lcrypt&quot;</tt> </p>
<p> The crypt package distributed with Cygwin is a Linux compatible 56-bit <font SIZE="-1">DES</font> crypt port by Corinna Vinschen. </p>
<p> Alternatively, the crypt libraries in <font SIZE="-1">GNU</font> libc have been ported to Cygwin. </p>
<p> As of libcrypt 1.3 (March 2016), you will need to install the libcrypt-devel package for Configure to detect <code>crypt()</code>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;-lgdbm_compat&quot;</tt> (<tt>&quot;use GDBM_File&quot;</tt>) </p>
<p> <font SIZE="-1">GDBM</font> is available for Cygwin. </p>
<p> <font SIZE="-1">NOTE:</font> The <font SIZE="-1">GDBM</font> library only works on <font SIZE="-1">NTFS</font> partitions.</p>
<dt>&bull;</p>
<dd> <tt>&quot;-ldb&quot;</tt> (<tt>&quot;use DB_File&quot;</tt>) </p>
<p> BerkeleyDB is available for Cygwin. </p>
<p> <font SIZE="-1">NOTE:</font> The BerkeleyDB library only completely works on <font SIZE="-1">NTFS</font> partitions.</p>
<dt>&bull;</p>
<dd> <tt>&quot;cygserver&quot;</tt> (<tt>&quot;use IPC::SysV&quot;</tt>) </p>
<p> A port of SysV <font SIZE="-1">IPC</font> is available for Cygwin. </p>
<p> <font SIZE="-1">NOTE:</font> This has <code>not</code> been extensively tested. In particular, <tt>&quot;d_semctl_semun&quot;</tt> is undefined because it fails a Configure test and on Win9x the <i>shm*()</i> functions seem to hang. It also creates a compile time dependency because <i>perl.h</i> includes <i>&lt;sys/ipc.h</i>&gt; and <i>&lt;sys/sem.h</i>&gt; (which will be required in the future when compiling <font SIZE="-1">CPAN</font> modules). <font SIZE="-1">CURRENTLY NOT SUPPORTED</font>!</p>
<dt>&bull;</p>
<dd> <tt>&quot;-lutil&quot;</tt> </p>
<p> Included with the standard Cygwin netrelease is the inetutils package which includes libutil.a.</dl>
<h3>Configure-time Options for Perl on Cygwin</h3>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> document describes several Configure-time options. Some of these will work with Cygwin, others are not yet possible. Also, some of these are experimental. You can either select an option when Configure prompts you or you can define (undefine) symbols on the command line.</p>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;-Uusedl&quot;</tt> </p>
<p> Undefining this symbol forces Perl to be compiled statically.</p>
<dt>&bull;</p>
<dd> <tt>&quot;-Dusemymalloc&quot;</tt> </p>
<p> By default Perl does not use the <tt>&quot;malloc()&quot;</tt> included with the Perl source, because it was slower and not entirely thread-safe. If you want to force Perl to build with the old -Dusemymalloc define this.</p>
<dt>&bull;</p>
<dd> <tt>&quot;-Uuseperlio&quot;</tt> </p>
<p> Undefining this symbol disables the PerlIO abstraction. PerlIO is now the default; it is not recommended to disable PerlIO.</p>
<dt>&bull;</p>
<dd> <tt>&quot;-Dusemultiplicity&quot;</tt> </p>
<p> Multiplicity is required when embedding Perl in a C program and using more than one interpreter instance. This is only required when you build a not-threaded perl with <tt>&quot;-Uuseithreads&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;-Uuse64bitint&quot;</tt> </p>
<p> By default Perl uses 64 bit integers. If you want to use smaller 32 bit integers, define this symbol.</p>
<dt>&bull;</p>
<dd> <tt>&quot;-Duselongdouble&quot;</tt> </p>
<p> <i>gcc</i> supports long doubles (12 bytes). However, several additional long double math functions are necessary to use them within Perl (<i>{atan2, cos, exp, floor, fmod, frexp, isnan, log, modf, pow, sin, sqrt}l, strtold</i>). These are <code>not</code> yet available with newlib, the Cygwin libc.</p>
<dt>&bull;</p>
<dd> <tt>&quot;-Uuseithreads&quot;</tt> </p>
<p> Define this symbol if you want not-threaded faster perl.</p>
<dt>&bull;</p>
<dd> <tt>&quot;-Duselargefiles&quot;</tt> </p>
<p> Cygwin uses 64-bit integers for internal size and position calculations, this will be correctly detected and defined by Configure.</p>
<dt>&bull;</p>
<dd> <tt>&quot;-Dmksymlinks&quot;</tt> </p>
<p> Use this to build perl outside of the source tree. Details can be found in the <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> document. This is the recommended way to build perl from sources.</dl>
<h3>Suspicious Warnings on Cygwin</h3>
<p> You may see some messages during Configure that seem suspicious.</p>
<dl>
<dt>&bull;</p>
<dd> Win9x and <tt>&quot;d_eofnblk&quot;</tt> </p>
<p> Win9x does not correctly report <tt>&quot;EOF&quot;</tt> with a non-blocking read on a closed pipe. You will see the following messages: </p>
<pre>
 But it also returns -1 to signal EOF, so be careful!
 WARNING: you can't distinguish between EOF and no data!
 *** WHOA THERE!!! ***
     The recommended value for $d_eofnblk on this machine was
     &quot;define&quot;!
     Keep the recommended value? [y]
</pre>
<p> At least for consistency with WinNT, you should keep the recommended value.</p>
<dt>&bull;</p>
<dd> Compiler/Preprocessor defines </p>
<p> The following error occurs because of the Cygwin <tt>&quot;#define&quot;</tt> of <tt>&quot;_LONG_DOUBLE&quot;</tt>: </p>
<pre>
  Guessing which symbols your C compiler and preprocessor define...
  try.c:&lt;line#&gt;: missing binary operator
</pre>
<p> This failure does not seem to cause any problems. With older gcc versions, &#8220;parse error&#8221; is reported instead of &#8220;missing binary operator&#8221;.</dl>
<h2>MAKE ON CYGWIN</h2>
<p> Simply run <i>make</i> and wait: </p>
<pre>
  make 2&gt;&amp;1 | tee log.make
</pre>
<h2>TEST ON CYGWIN</h2>
<p> There are two steps to running the test suite: </p>
<pre>
  make test 2&gt;&amp;1 | tee log.make-test
  cd t; ./perl harness 2&gt;&amp;1 | tee ../log.harness
</pre>
<p> The same tests are run both times, but more information is provided when running as <tt>&quot;./perl harness&quot;</tt>. </p>
<p> Test results vary depending on your host system and your Cygwin configuration. If a test can pass in some Cygwin setup, it is always attempted and explainable test failures are documented. It is possible for Perl to pass all the tests, but it is more likely that some tests will fail for one of the reasons listed below.</p>
<h3>File Permissions on Cygwin</h3>
<p> <font SIZE="-1">UNIX</font> file permissions are based on sets of mode bits for {read,write,execute} for each {user,group,other}. By default Cygwin only tracks the Win32 read-only attribute represented as the <font SIZE="-1">UNIX</font> file user write bit (files are always readable, files are executable if they have a <i>.{com,bat,exe}</i> extension or begin with <tt>&quot;#!&quot;</tt>, directories are always readable and executable). On WinNT with the <i>ntea</i> <tt>&quot;CYGWIN&quot;</tt> setting, the additional mode bits are stored as extended file attributes. On WinNT with the default <i>ntsec</i> <tt>&quot;CYGWIN&quot;</tt> setting, permissions use the standard WinNT security descriptors and access control lists. Without one of these options, these tests will fail (listing not updated yet): </p>
<p>Failed Test List of failed&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;io / fs.t 5, 7, 9 &#8211; 10 lib / anydbm.t 2 lib / db &#8211; btree.t 20 lib / db &#8211; hash.t 16 lib / db &#8211; recno.t 18 lib / gdbm.t 2 lib / ndbm.t 2 lib / odbm.t 2 lib / sdbm.t 2 op / stat.t 9, 20(.tmp not an executable extension)</p>
<h3>NDBM_File and ODBM_File do not work on <font SIZE="-1">FAT</font> filesystems</h3>
<p> Do not use NDBM_File or ODBM_File on <font SIZE="-1">FAT</font> filesystem. They can be built on a <font SIZE="-1">FAT</font> filesystem, but many tests will fail: </p>
<pre>
 ../ext/NDBM_File/ndbm.t       13  3328    71   59  83.10%  1-2 4 16-71
 ../ext/ODBM_File/odbm.t      255 65280    ??   ??       %  ??
 ../lib/AnyDBM_File.t           2   512    12    2  16.67%  1 4
 ../lib/Memoize/t/errors.t      0   139    11    5  45.45%  7-11
 ../lib/Memoize/t/tie_ndbm.t   13  3328     4    4 100.00%  1-4
 run/fresh_perl.t                          97    1   1.03%  91
</pre>
<p> If you intend to run only on <font SIZE="-1">FAT</font> (or if using AnyDBM_File on <font SIZE="-1">FAT</font>), run Configure with the -Ui_ndbm and -Ui_dbm options to prevent NDBM_File and ODBM_File being built. </p>
<p> With <font SIZE="-1">NTFS</font> (and no CYGWIN=nontsec), there should be no problems even if perl was built on <font SIZE="-1">FAT.</font></p>
<h3>fork() failures in io_* tests</h3>
<p> A <tt>&quot;fork()&quot;</tt> failure may result in the following tests failing: </p>
<pre>
  ext/IO/lib/IO/t/io_multihomed.t
  ext/IO/lib/IO/t/io_sock.t
  ext/IO/lib/IO/t/io_unix.t
</pre>
<p> See comment on fork in &#8220;Miscellaneous&#8221; below.</p>
<h2>Specific features of the Cygwin port</h2>
<h3>Script Portability on Cygwin</h3>
<p> Cygwin does an outstanding job of providing UNIX-like semantics on top of Win32 systems. However, in addition to the items noted above, there are some differences that you should know about. This is a very brief guide to portability, more information can be found in the Cygwin documentation.</p>
<dl>
<dt>&bull;</p>
<dd> Pathnames </p>
<p> Cygwin pathnames are separated by forward (<i>/</i>) slashes, Universal Naming Codes (<i>//UNC</i>) are also supported Since cygwin-1.7 non-POSIX pathnames are discouraged. Names may contain all printable characters. </p>
<p> File names are case insensitive, but case preserving. A pathname that contains a backslash or drive letter is a Win32 pathname, and not subject to the translations applied to <font SIZE="-1">POSIX</font> style pathnames, but cygwin will warn you, so better convert them to <font SIZE="-1">POSIX.</font> </p>
<p> For conversion we have <tt>&quot;Cygwin::win_to_posix_path()&quot;</tt> and <tt>&quot;Cygwin::posix_to_win_path()&quot;</tt>. </p>
<p> Since cygwin-1.7 pathnames are <font SIZE="-1">UTF-8</font> encoded.</p>
<dt>&bull;</p>
<dd> Text/Binary </p>
<p> Since cygwin-1.7 textmounts are deprecated and strongly discouraged. </p>
<p> When a file is opened it is in either text or binary mode. In text mode a file is subject to CR/LF/Ctrl-Z translations. With Cygwin, the default mode for an <tt>&quot;open()&quot;</tt> is determined by the mode of the mount that underlies the file. See &#8220;Cygwin::is_binmount&#8221;(). Perl provides a <tt>&quot;binmode()&quot;</tt> function to set binary mode on files that otherwise would be treated as text. <tt>&quot;sysopen()&quot;</tt> with the <tt>&quot;O_TEXT&quot;</tt> flag sets text mode on files that otherwise would be treated as binary: </p>
<pre>
    sysopen(FOO, &quot;bar&quot;, O_WRONLY|O_CREAT|O_TEXT)
</pre>
<p> <tt>&quot;lseek()&quot;</tt>, <tt>&quot;tell()&quot;</tt> and <tt>&quot;sysseek()&quot;</tt> only work with files opened in binary mode. </p>
<p> The text/binary issue is covered at length in the Cygwin documentation.</p>
<dt>&bull;</p>
<dd> PerlIO </p>
<p> PerlIO overrides the default Cygwin Text/Binary behaviour. A file will always be treated as binary, regardless of the mode of the mount it lives on, just like it is in <font SIZE="-1">UNIX.</font> So <font SIZE="-1">CR/LF</font> translation needs to be requested in either the <tt>&quot;open()&quot;</tt> call like this: </p>
<pre>
  open(FH, &quot;&gt;:crlf&quot;, &quot;out.txt&quot;);
</pre>
<p> which will do conversion from <font SIZE="-1">LF</font> to <font SIZE="-1">CR/LF</font> on the output, or in the environment settings (add this to your .bashrc): </p>
<pre>
  export PERLIO=crlf
</pre>
<p> which will pull in the crlf PerlIO layer which does <font SIZE="-1">LF</font> -&gt; <font SIZE="-1">CRLF</font> conversion on every output generated by perl.</p>
<dt>&bull;</p>
<dd> <i>.exe</i> </p>
<p> The Cygwin <tt>&quot;stat()&quot;</tt>, <tt>&quot;lstat()&quot;</tt> and <tt>&quot;readlink()&quot;</tt> functions make the <i>.exe</i> extension transparent by looking for <i>foo.exe</i> when you ask for <i>foo</i> (unless a <i>foo</i> also exists). Cygwin does not require a <i>.exe</i> extension, but <i>gcc</i> adds it automatically when building a program. However, when accessing an executable as a normal file (e.g., <i>cp</i> in a makefile) the <i>.exe</i> is not transparent. The <i>install</i> program included with Cygwin automatically appends a <i>.exe</i> when necessary.</p>
<dt>&bull;</p>
<dd> Cygwin vs. Windows process ids </p>
<p> Cygwin processes have their own pid, which is different from the underlying windows pid. Most posix compliant Proc functions expect the cygwin pid, but several Win32::Process functions expect the winpid. E.g. <tt>$$</tt> is the cygwin pid of <i>/usr/bin/perl</i>, which is not the winpid. Use <tt>&quot;Cygwin::pid_to_winpid()&quot;</tt> and <tt>&quot;Cygwin::winpid_to_pid()&quot;</tt> to translate between them.</p>
<dt>&bull;</p>
<dd> Cygwin vs. Windows errors </p>
<p> Under Cygwin, $^E is the same as $!. When using Win32 <font SIZE="-1">API</font> Functions, use <tt>&quot;Win32::GetLastError()&quot;</tt> to get the last Windows error.</p>
<dt>&bull;</p>
<dd> rebase errors on fork or system </p>
<p> Using <tt>&quot;fork()&quot;</tt> or <tt>&quot;system()&quot;</tt> out to another perl after loading multiple dlls may result on a <font SIZE="-1">DLL</font> baseaddress conflict. The internal cygwin error looks like like the following: </p>
<pre>
 0 [main] perl 8916 child_info_fork::abort: data segment start:
 parent (0xC1A000) != child(0xA6A000)
</pre>
<p> or: </p>
<p> 183 [main] perl 3588 C:
