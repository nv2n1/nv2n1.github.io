---
title: "perlvms(1)"
name: "perlvms"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlvms/"
description: "perlvms – VMS-specific documentation for Perl"
---

<h2 class="name">NAME</h2>
<p> perlvms &#8211; VMS-specific documentation for Perl </p>
<h2>DESCRIPTION</h2>
<p> Gathered below are notes describing details of Perl 5&#8217;s behavior on <font SIZE="-1">VMS.</font> They are a supplement to the regular Perl 5 documentation, so we have focussed on the ways in which Perl 5 functions differently under <font SIZE="-1">VMS</font> than it does under Unix, and on the interactions between Perl and the rest of the operating system. We haven&#8217;t tried to duplicate complete descriptions of Perl features from the main Perl documentation, which can be found in the <i>[.pod]</i> subdirectory of the Perl distribution. </p>
<p> We hope these notes will save you from confusion and lost sleep when writing Perl scripts on <font SIZE="-1">VMS.</font> If you find we&#8217;ve missed something you think should appear here, please don&#8217;t hesitate to drop a line to vmsperl [at] perl.org.</p>
<h2>Installation</h2>
<p> Directions for building and installing Perl 5 can be found in the file <i></i><font SIZE="-1"><i>README</i></font><i>.vms</i> in the main source directory of the Perl distribution.</p>
<h2>Organization of Perl Images</h2>
<h3>Core Images</h3>
<p> During the build process, three Perl images are produced. <i>Miniperl.Exe</i> is an executable image which contains all of the basic functionality of Perl, but cannot take advantage of Perl <font SIZE="-1">XS</font> extensions and has a hard-wired list of library locations for loading pure-Perl modules. It is used extensively to build and test Perl and various extensions, but is not installed. </p>
<p> Most of the complete Perl resides in the shareable image <i>PerlShr.Exe</i>, which provides a core to which the Perl executable image and all Perl extensions are linked. It is generally located via the logical name <i></i><font SIZE="-1"><i>PERLSHR</i></font><i></i>. While it&#8217;s possible to put the image in <i></i><font SIZE="-1"><i>SYS$SHARE</i></font><i></i> to make it loadable, that&#8217;s not recommended. And while you may wish to <font SIZE="-1">INSTALL</font> the image for performance reasons, you should not install it with privileges; if you do, the result will not be what you expect as image privileges are disabled during Perl start-up. </p>
<p> Finally, <i>Perl.Exe</i> is an executable image containing the main entry point for Perl, as well as some initialization code. It should be placed in a public directory, and made world executable. In order to run Perl with command line arguments, you should define a foreign command to invoke this image.</p>
<h3>Perl Extensions</h3>
<p> Perl extensions are packages which provide both <font SIZE="-1">XS</font> and Perl code to add new functionality to perl. (<font SIZE="-1">XS</font> is a meta-language which simplifies writing C code which interacts with Perl, see perlxs for more details.) The Perl code for an extension is treated like any other library module &#8211; it&#8217;s made available in your script through the appropriate <tt>&quot;use&quot;</tt> or <tt>&quot;require&quot;</tt> statement, and usually defines a Perl package containing the extension. </p>
<p> The portion of the extension provided by the <font SIZE="-1">XS</font> code may be connected to the rest of Perl in either of two ways. In the <code>static</code> configuration, the object code for the extension is linked directly into <i>PerlShr.Exe</i>, and is initialized whenever Perl is invoked. In the <code>dynamic</code> configuration, the extension&#8217;s machine code is placed into a separate shareable image, which is mapped by Perl&#8217;s DynaLoader when the extension is <tt>&quot;use&quot;</tt>d or <tt>&quot;require&quot;</tt>d in your script. This allows you to maintain the extension as a separate entity, at the cost of keeping track of the additional shareable image. Most extensions can be set up as either static or dynamic. </p>
<p> The source code for an extension usually resides in its own directory. At least three files are generally provided: <i>Extshortname</i><i>.xs</i> (where <i>Extshortname</i> is the portion of the extension&#8217;s name following the last <tt>&quot;::&quot;</tt>), containing the <font SIZE="-1">XS</font> code, <i>Extshortname</i><i>.pm</i>, the Perl library module for the extension, and <i>Makefile.PL</i>, a Perl script which uses the <tt>&quot;MakeMaker&quot;</tt> library modules supplied with Perl to generate a <i>Descrip.MMS</i> file for the extension.</p>
<h3>Installing static extensions</h3>
<p> Since static extensions are incorporated directly into <i>PerlShr.Exe</i>, you&#8217;ll have to rebuild Perl to incorporate a new extension. You should edit the main <i>Descrip.MMS</i> or <i>Makefile</i> you use to build Perl, adding the extension&#8217;s name to the <tt>&quot;ext&quot;</tt> macro, and the extension&#8217;s object file to the <tt>&quot;extobj&quot;</tt> macro. You&#8217;ll also need to build the extension&#8217;s object file, either by adding dependencies to the main <i>Descrip.MMS</i>, or using a separate <i>Descrip.MMS</i> for the extension. Then, rebuild <i>PerlShr.Exe</i> to incorporate the new code. </p>
<p> Finally, you&#8217;ll need to copy the extension&#8217;s Perl library module to the <i>[.</i><i>Extname</i><i>]</i> subdirectory under one of the directories in <tt>@INC</tt>, where <i>Extname</i> is the name of the extension, with all <tt>&quot;::&quot;</tt> replaced by <tt>&quot;.&quot;</tt> (e.g. the library module for extension Foo::Bar would be copied to a <i>[.Foo.Bar]</i> subdirectory).</p>
<h3>Installing dynamic extensions</h3>
<p> In general, the distributed kit for a Perl extension includes a file named Makefile.PL, which is a Perl program which is used to create a <i>Descrip.MMS</i> file which can be used to build and install the files required by the extension. The kit should be unpacked into a directory tree <code>not</code> under the main Perl source directory, and the procedure for building the extension is simply </p>
<pre>
    $ perl Makefile.PL  ! Create Descrip.MMS
    $ mmk               ! Build necessary files
    $ mmk test          ! Run test code, if supplied
    $ mmk install       ! Install into public Perl tree
</pre>
<p> <font SIZE="-1">VMS</font> support for this process in the current release of Perl is sufficient to handle most extensions. (See the MakeMaker documentation for more details on installation options for extensions.)</p>
<dl>
<dt>&bull;</p>
<dd> the <i>[.Lib.Auto.</i><i>Arch</i><i></i>$PVers<i></i><i>Extname</i><i>]</i> subdirectory of one of the directories in <tt>@INC</tt> (where <i>PVers</i> is the version of Perl you&#8217;re using, as supplied in <tt>$]</tt>, with &#8216;.&#8217; converted to &#8216;_&#8217;), or</p>
<dt>&bull;</p>
<dd> one of the directories in <tt>@INC</tt>, or</p>
<dt>&bull;</p>
<dd> a directory which the extensions Perl library module passes to the DynaLoader when asking it to map the shareable image, or</p>
<dt>&bull;</p>
<dd> <i>Sys$Share</i> or <i>Sys$Library</i>.</dl>
<p> If the shareable image isn&#8217;t in any of these places, you&#8217;ll need to define a logical name <i>Extshortname</i>, where <i>Extshortname</i> is the portion of the extension&#8217;s name after the last <tt>&quot;::&quot;</tt>, which translates to the full file specification of the shareable image.</p>
<h2>File specifications</h2>
<h3>Syntax</h3>
<p> We have tried to make Perl aware of both VMS-style and Unix-style file specifications wherever possible. You may use either style, or both, on the command line and in scripts, but you may not combine the two styles within a single file specification. <font SIZE="-1">VMS</font> Perl interprets Unix pathnames in much the same way as the <font SIZE="-1">CRTL</font> (<i>e.g.</i> the first component of an absolute path is read as the device name for the <font SIZE="-1">VMS</font> file specification). There are a set of functions provided in the <tt>&quot;VMS::Filespec&quot;</tt> package for explicit interconversion between <font SIZE="-1">VMS</font> and Unix syntax; its documentation provides more details. </p>
<p> We&#8217;ve tried to minimize the dependence of Perl library modules on Unix syntax, but you may find that some of these, as well as some scripts written for Unix systems, will require that you use Unix syntax, since they will assume that &#8216;/&#8217; is the directory separator, <i>etc.</i> If you find instances of this in the Perl distribution itself, please let us know, so we can try to work around them. </p>
<p> Also when working on Perl programs on <font SIZE="-1">VMS,</font> if you need a syntax in a specific operating system format, then you need either to check the appropriate <font SIZE="-1">DECC$</font> feature logical, or call a conversion routine to force it to that format. </p>
<p> The feature logical name <font SIZE="-1">DECC$FILENAME_UNIX_REPORT</font> modifies traditional Perl behavior in the conversion of file specifications from Unix to <font SIZE="-1">VMS</font> format in order to follow the extended character handling rules now expected by the <font SIZE="-1">CRTL.</font> Specifically, when this feature is in effect, the <tt>&quot;./.../&quot;</tt> in a Unix path is now translated to <tt>&quot;[.^.^.^.]&quot;</tt> instead of the traditional <font SIZE="-1">VMS</font> <tt>&quot;[...]&quot;</tt>. To be compatible with what MakeMaker expects, if a <font SIZE="-1">VMS</font> path cannot be translated to a Unix path, it is passed through unchanged, so <tt>&quot;unixify(&quot;[...]&quot;)&quot;</tt> will return <tt>&quot;[...]&quot;</tt>. </p>
<p> There are several ambiguous cases where a conversion routine cannot determine whether an input filename is in Unix format or in <font SIZE="-1">VMS</font> format, since now both <font SIZE="-1">VMS</font> and Unix file specifications may have characters in them that could be mistaken for syntax delimiters of the other type. So some pathnames simply cannot be used in a mode that allows either type of pathname to be present. Perl will tend to assume that an ambiguous filename is in Unix format. </p>
<p> Allowing &#8220;.&#8221; as a version delimiter is simply incompatible with determining whether a pathname is in <font SIZE="-1">VMS</font> format or in Unix format with extended file syntax. There is no way to know whether &#8220;perl-5.8.6&#8221; is a Unix &#8220;perl-5.8.6&#8221; or a <font SIZE="-1">VMS</font> &#8220;perl-5.8;6&#8221; when passing it to <code>unixify()</code> or <code>vmsify()</code>. </p>
<p> The <font SIZE="-1">DECC$FILENAME_UNIX_REPORT</font> logical name controls how Perl interprets filenames to the extent that Perl uses the <font SIZE="-1">CRTL</font> internally for many purposes, and attempts to follow <font SIZE="-1">CRTL</font> conventions for reporting filenames. The <font SIZE="-1">DECC$FILENAME_UNIX_ONLY</font> feature differs in that it expects all filenames passed to the C run-time to be already in Unix format. This feature is not yet supported in Perl since Perl uses traditional OpenVMS file specifications internally and in the test harness, and it is not yet clear whether this mode will be useful or useable. The feature logical name <font SIZE="-1">DECC$POSIX_COMPLIANT_PATHNAMES</font> is new with the <font SIZE="-1">RMS</font> Symbolic Link <font SIZE="-1">SDK</font> and included with OpenVMS v8.3, but is not yet supported in Perl.</p>
<h3>Filename Case</h3>
<p> Perl enables <font SIZE="-1">DECC$EFS_CASE_PRESERVE</font> and <font SIZE="-1">DECC$ARGV_PARSE_STYLE</font> by default. Note that the latter only takes effect when extended parse is set in the process in which Perl is running. When these features are explicitly disabled in the environment or the <font SIZE="-1">CRTL</font> does not support them, Perl follows the traditional <font SIZE="-1">CRTL</font> behavior of downcasing command-line arguments and returning file specifications in lower case only. </p>
<p> <i>N. B.</i> It is very easy to get tripped up using a mixture of other programs, external utilities, and Perl scripts that are in varying states of being able to handle case preservation. For example, a file created by an older version of an archive utility or a build utility such as <font SIZE="-1">MMK</font> or <font SIZE="-1">MMS</font> may generate a filename in all upper case even on an <font SIZE="-1">ODS-5</font> volume. If this filename is later retrieved by a Perl script or module in a case preserving environment, that upper case name may not match the mixed-case or lower-case expectations of the Perl code. Your best bet is to follow an all-or-nothing approach to case preservation: either don&#8217;t use it at all, or make sure your entire toolchain and application environment support and use it. </p>
<p> OpenVMS Alpha v7.3-1 and later and all version of OpenVMS I64 support case sensitivity as a process setting (see <tt>&quot;SET PROCESS /CASE_LOOKUP=SENSITIVE&quot;</tt>). Perl does not currently support case sensitivity on <font SIZE="-1">VMS,</font> but it may in the future, so Perl programs should use the <tt>&quot;File::Spec-&gt;case_tolerant&quot;</tt> method to determine the state, and not the <tt>$^O</tt> variable.</p>
<h3>Symbolic Links</h3>
<p> When built on an <font SIZE="-1">ODS-5</font> volume with symbolic links enabled, Perl by default supports symbolic links when the requisite support is available in the filesystem and <font SIZE="-1">CRTL</font> (generally 64-bit OpenVMS v8.3 and later). There are a number of limitations and caveats to be aware of when working with symbolic links on <font SIZE="-1">VMS.</font> Most notably, the target of a valid symbolic link must be expressed as a Unix-style path and it must exist on a volume visible from your <font SIZE="-1">POSIX</font> root (see the <tt>&quot;SHOW ROOT&quot;</tt> command in <font SIZE="-1">DCL</font> help). For further details on symbolic link capabilities and requirements, see chapter 12 of the <font SIZE="-1">CRTL</font> manual that ships with OpenVMS v8.3 or later.</p>
<h3>Wildcard expansion</h3>
<p> File specifications containing wildcards are allowed both on the command line and within Perl globs (e.g. <tt>&quot;&lt;*.c&gt;&quot;</tt>). If the wildcard filespec uses <font SIZE="-1">VMS</font> syntax, the resultant filespecs will follow <font SIZE="-1">VMS</font> syntax; if a Unix-style filespec is passed in, Unix-style filespecs will be returned. Similar to the behavior of wildcard globbing for a Unix shell, one can escape command line wildcards with double quotation marks <tt>&quot;&quot;&quot;</tt> around a perl program command line argument. However, owing to the stripping of <tt>&quot;&quot;&quot;</tt> characters carried out by the C handling of argv you will need to escape a construct such as this one (in a directory containing the files <i></i><font SIZE="-1"><i>PERL.C</i></font><i></i>, <i></i><font SIZE="-1"><i>PERL.EXE</i></font><i></i>, <i></i><font SIZE="-1"><i>PERL.H</i></font><i></i>, and <i></i><font SIZE="-1"><i>PERL.OBJ</i></font><i></i>): </p>
<pre>
    $ perl -e &quot;print join(' ',@ARGV)&quot; perl.*
    perl.c perl.exe perl.h perl.obj
</pre>
<p> in the following triple quoted manner: </p>
<pre>
    $ perl -e &quot;print join(' ',@ARGV)&quot; &quot;&quot;&quot;perl.*&quot;&quot;&quot;
    perl.*
</pre>
<p> In both the case of unquoted command line arguments or in calls to <tt>&quot;glob()&quot;</tt> <font SIZE="-1">VMS</font> wildcard expansion is performed. (csh-style wildcard expansion is available if you use <tt>&quot;File::Glob::glob&quot;</tt>.) If the wildcard filespec contains a device or directory specification, then the resultant filespecs will also contain a device and directory; otherwise, device and directory information are removed. VMS-style resultant filespecs will contain a full device and directory, while Unix-style resultant filespecs will contain only as much of a directory path as was present in the input filespec. For example, if your default directory is Perl_Root:[000000], the expansion of <tt>&quot;[.t]*.*&quot;</tt> will yield filespecs like &#8220;perl_root:[t]base.dir&#8221;, while the expansion of <tt>&quot;t/*/*&quot;</tt> will yield filespecs like &#8220;t/base.dir&#8221;. (This is done to match the behavior of glob expansion performed by Unix shells.) </p>
<p> Similarly, the resultant filespec will contain the file version only if one was present in the input filespec.</p>
<h3>Pipes</h3>
<p> Input and output pipes to Perl filehandles are supported; the &#8220;file name&#8221; is passed to lib$<code>spawn()</code> for asynchronous execution. You should be careful to close any pipes you have opened in a Perl script, lest you leave any &#8220;orphaned&#8221; subprocesses around when Perl exits. </p>
<p> You may also use backticks to invoke a <font SIZE="-1">DCL</font> subprocess, whose output is used as the return value of the expression. The string between the backticks is handled as if it were the argument to the <tt>&quot;system&quot;</tt> operator (see below). In this case, Perl will wait for the subprocess to complete before continuing. </p>
<p> The mailbox (<font SIZE="-1">MBX</font>) that perl can create to communicate with a pipe defaults to a buffer size of 8192 on 64-bit systems, 512 on <font SIZE="-1">VAX.</font> The default buffer size is adjustable via the logical name <font SIZE="-1">PERL_MBX_SIZE</font> provided that the value falls between 128 and the <font SIZE="-1">SYSGEN</font> parameter <font SIZE="-1">MAXBUF</font> inclusive. For example, to set the mailbox size to 32767 use <tt>&quot;$ENV{'PERL_MBX_SIZE'} = 32767;&quot;</tt> and then open and use pipe constructs. An alternative would be to issue the command: </p>
<pre>
    $ Define PERL_MBX_SIZE 32767
</pre>
<p> before running your wide record pipe program. A larger value may improve performance at the expense of the <font SIZE="-1">BYTLM UAF</font> quota.</p>
<h2>PERL5LIB and PERLLIB</h2>
<p> The <font SIZE="-1">PERL5LIB</font> and <font SIZE="-1">PERLLIB</font> environment elements work as documented in perl, except that the element separator is, by default, &#8216;|&#8217; instead of &#8216;:&#8217;. However, when running under a Unix shell as determined by the logical name <tt>&quot;GNV$UNIX_SHELL&quot;</tt>, the separator will be &#8216;:&#8217; as on Unix systems. The directory specifications may use either <font SIZE="-1">VMS</font> or Unix syntax.</p>
<h2>The Perl Forked Debugger</h2>
<p> The Perl forked debugger places the debugger commands and output in a separate X-11 terminal window so that commands and output from multiple processes are not mixed together. </p>
<p> Perl on <font SIZE="-1">VMS</font> supports an emulation of the forked debugger when Perl is run on a <font SIZE="-1">VMS</font> system that has X11 support installed. </p>
<p> To use the forked debugger, you need to have the default display set to an X-11 Server and some environment variables set that Unix expects. </p>
<p> The forked debugger requires the environment variable <tt>&quot;TERM&quot;</tt> to be <tt>&quot;xterm&quot;</tt>, and the environment variable <tt>&quot;DISPLAY&quot;</tt> to exist. <tt>&quot;xterm&quot;</tt> must be in lower case. </p>
<pre>
  $define TERM &quot;xterm&quot;
  $define DISPLAY &quot;hostname:0.0&quot;
</pre>
<p> Currently the value of <tt>&quot;DISPLAY&quot;</tt> is ignored. It is recommended that it be set to be the hostname of the display, the server and screen in Unix notation. In the future the value of <font SIZE="-1">DISPLAY</font> may be honored by Perl instead of using the default display. </p>
<p> It may be helpful to always use the forked debugger so that script I/O is separated from debugger I/O. You can force the debugger to be forked by assigning a value to the logical name &lt;<font SIZE="-1">PERLDB_PIDS</font>&gt; that is not a process identification number. </p>
<pre>
  $define PERLDB_PIDS XXXX
</pre>
<h2>PERL_VMS_EXCEPTION_DEBUG</h2>
<p> The <font SIZE="-1">PERL_VMS_EXCEPTION_DEBUG</font> being defined as &#8220;<font SIZE="-1">ENABLE&#8221;</font> will cause the <font SIZE="-1">VMS</font> debugger to be invoked if a fatal exception that is not otherwise handled is raised. The purpose of this is to allow debugging of internal Perl problems that would cause such a condition. </p>
<p> This allows the programmer to look at the execution stack and variables to find out the cause of the exception. As the debugger is being invoked as the Perl interpreter is about to do a fatal exit, continuing the execution in debug mode is usually not practical. </p>
<p> Starting Perl in the <font SIZE="-1">VMS</font> debugger may change the program execution profile in a way that such problems are not reproduced. </p>
<p> The <tt>&quot;kill&quot;</tt> function can be used to test this functionality from within a program. </p>
<p> In typical <font SIZE="-1">VMS</font> style, only the first letter of the value of this logical name is actually checked in a case insensitive mode, and it is considered enabled if it is the value &#8220;T&#8221;,&#8220;1&#8221; or &#8220;E&#8221;. </p>
<p> This logical name must be defined before Perl is started.</p>
<h2>Command line</h2>
<h3>I/O redirection and backgrounding</h3>
<p> Perl for <font SIZE="-1">VMS</font> supports redirection of input and output on the command line, using a subset of Bourne shell syntax:</p>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;&lt;file&quot;</tt> reads stdin from <tt>&quot;file&quot;</tt>,</p>
<dt>&bull;</p>
<dd> <tt>&quot;&gt;file&quot;</tt> writes stdout to <tt>&quot;file&quot;</tt>,</p>
<dt>&bull;</p>
<dd> <tt>&quot;&gt;&gt;file&quot;</tt> appends stdout to <tt>&quot;file&quot;</tt>,</p>
<dt>&bull;</p>
<dd> <tt>&quot;2&gt;file&quot;</tt> writes stderr to <tt>&quot;file&quot;</tt>,</p>
<dt>&bull;</p>
<dd> <tt>&quot;2&gt;&gt;file&quot;</tt> appends stderr to <tt>&quot;file&quot;</tt>, and</p>
<dt>&bull;</p>
<dd> <tt>&quot;2&gt;&amp;1&quot;</tt> redirects stderr to stdout.</dl>
<p> In addition, output may be piped to a subprocess, using the character &#8216;|&#8217;. Anything after this character on the command line is passed to a subprocess for execution; the subprocess takes the output of Perl as its input. </p>
<p> Finally, if the command line ends with &#8216;&amp;&#8217;, the entire command is run in the background as an asynchronous subprocess.</p>
<h3>Command line switches</h3>
<p> The following command line switches behave differently under <font SIZE="-1">VMS</font> than described in perlrun. Note also that in order to pass uppercase switches to Perl, you need to enclose them in double-quotes on the command line, since the <font SIZE="-1">CRTL</font> downcases all unquoted strings. </p>
<p> On newer 64 bit versions of OpenVMS, a process setting now controls if the quoting is needed to preserve the case of command line arguments.</p>
<dl>
<dt>-i</p>
<dd> If the <tt>&quot;-i&quot;</tt> switch is present but no extension for a backup copy is given, then inplace editing creates a new version of a file; the existing copy is not deleted. (Note that if an extension is given, an existing file is renamed to the backup file, as is the case under other operating systems, so it does not remain as a previous version under the original filename.)</p>
<dt>-S</p>
<dd> If the <tt>&quot;-S&quot;</tt> or <tt>&quot;-&quot;S&quot;&quot;</tt> switch is present <i>and</i> the script name does not contain a directory, then Perl translates the logical name <font SIZE="-1">DCL$PATH</font> as a searchlist, using each translation as a directory in which to look for the script. In addition, if no file type is specified, Perl looks in each directory for a file matching the name specified, with a blank type, a type of <i>.pl</i>, and a type of <i>.com</i>, in that order.</p>
<dt>-u</p>
<dd> The <tt>&quot;-u&quot;</tt> switch causes the <font SIZE="-1">VMS</font> debugger to be invoked after the Perl program is compiled, but before it has run. It does not create a core dump file.</dl>
<h2>Perl functions</h2>
<p> As of the time this document was last revised, the following Perl functions were implemented in the <font SIZE="-1">VMS</font> port of Perl (functions marked with * are discussed in more detail below): </p>
<pre>
    file tests*, abs, alarm, atan, backticks*, binmode*, bless,
    caller, chdir, chmod, chown, chomp, chop, chr,
    close, closedir, cos, crypt*, defined, delete, die, do, dump*, 
    each, endgrent, endpwent, eof, eval, exec*, exists, exit, exp, 
    fileno, flock  getc, getgrent*, getgrgid*, getgrnam, getlogin,
    getppid, getpwent*, getpwnam*, getpwuid*, glob, gmtime*, goto,
    grep, hex, ioctl, import, index, int, join, keys, kill*,
    last, lc, lcfirst, lchown*, length, link*, local, localtime, log,
    lstat, m//, map, mkdir, my, next, no, oct, open, opendir, ord,
    pack, pipe, pop, pos, print, printf, push, q//, qq//, qw//,
    qx//*, quotemeta, rand, read, readdir, readlink*, redo, ref,
    rename, require, reset, return, reverse, rewinddir, rindex,
    rmdir, s///, scalar, seek, seekdir, select(internal),
    select (system call)*, setgrent, setpwent, shift, sin, sleep,
    socketpair, sort, splice, split, sprintf, sqrt, srand, stat,
    study, substr, symlink*, sysread, system*, syswrite, tell,
    telldir, tie, time, times*, tr///, uc, ucfirst, umask,
    undef, unlink*, unpack, untie, unshift, use, utime*,
    values, vec, wait, waitpid*, wantarray, warn, write, y///
</pre>
<p> The following functions were not implemented in the <font SIZE="-1">VMS</font> port, and calling them produces a fatal error (usually) or undefined behavior (rarely, we hope): </p>
<pre>
    chroot, dbmclose, dbmopen, fork*, getpgrp, getpriority,  
    msgctl, msgget, msgsend, msgrcv, semctl,
    semget, semop, setpgrp, setpriority, shmctl, shmget,
    shmread, shmwrite, syscall
</pre>
<p> The following functions are available on Perls compiled with Dec C 5.2 or greater and running <font SIZE="-1">VMS 7.0</font> or greater: </p>
<pre>
    truncate
</pre>
<p> The following functions are available on Perls built on <font SIZE="-1">VMS 7.2</font> or greater: </p>
<pre>
    fcntl (without locking)
</pre>
<p> The following functions may or may not be implemented, depending on what type of socket support you&#8217;ve built into your copy of Perl: </p>
<pre>
    accept, bind, connect, getpeername,
    gethostbyname, getnetbyname, getprotobyname,
    getservbyname, gethostbyaddr, getnetbyaddr,
    getprotobynumber, getservbyport, gethostent,
    getnetent, getprotoent, getservent, sethostent,
    setnetent, setprotoent, setservent, endhostent,
    endnetent, endprotoent, endservent, getsockname,
    getsockopt, listen, recv, select(system call)*,
    send, setsockopt, shutdown, socket
</pre>
<p> The following function is available on Perls built on 64 bit OpenVMS v8.2 with hard links enabled on an <font SIZE="-1">ODS-5</font> formatted build disk. <font SIZE="-1">CRTL</font> support is in principle available as of OpenVMS v7.3-1, and better configuration support could detect this. </p>
<pre>
    link
</pre>
<p> The following functions are available on Perls built on 64 bit OpenVMS v8.2 and later. <font SIZE="-1">CRTL</font> support is in principle available as of OpenVMS v7.3-2, and better configuration support could detect this. </p>
<pre>
   getgrgid, getgrnam, getpwnam, getpwuid,
   setgrent, ttyname
</pre>
<p> The following functions are available on Perls built on 64 bit OpenVMS v8.2 and later. </p>
<pre>
   statvfs, socketpair
</pre>
<dl>
<dt>File tests</p>
<dd> The tests <tt>&quot;-b&quot;</tt>, <tt>&quot;-B&quot;</tt>, <tt>&quot;-c&quot;</tt>, <tt>&quot;-C&quot;</tt>, <tt>&quot;-d&quot;</tt>, <tt>&quot;-e&quot;</tt>, <tt>&quot;-f&quot;</tt>, <tt>&quot;-o&quot;</tt>, <tt>&quot;-M&quot;</tt>, <tt>&quot;-s&quot;</tt>, <tt>&quot;-S&quot;</tt>, <tt>&quot;-t&quot;</tt>, <tt>&quot;-T&quot;</tt>, and <tt>&quot;-z&quot;</tt> work as advertised. The return values for <tt>&quot;-r&quot;</tt>, <tt>&quot;-w&quot;</tt>, and <tt>&quot;-x&quot;</tt> tell you whether you can actually access the file; this may not reflect the UIC-based file protections. Since real and effective <font SIZE="-1">UIC</font> don&#8217;t differ under <font SIZE="-1">VMS,</font> <tt>&quot;-O&quot;</tt>, <tt>&quot;-R&quot;</tt>, <tt>&quot;-W&quot;</tt>, and <tt>&quot;-X&quot;</tt> are equivalent to <tt>&quot;-o&quot;</tt>, <tt>&quot;-r&quot;</tt>, <tt>&quot;-w&quot;</tt>, and <tt>&quot;-x&quot;</tt>. Similarly, several other tests, including <tt>&quot;-A&quot;</tt>, <tt>&quot;-g&quot;</tt>, <tt>&quot;-k&quot;</tt>, <tt>&quot;-l&quot;</tt>, <tt>&quot;-p&quot;</tt>, and <tt>&quot;-u&quot;</tt>, aren&#8217;t particularly meaningful under <font SIZE="-1">VMS,</font> and the values returned by these tests reflect whatever your <font SIZE="-1">CRTL</font> <tt>&quot;stat()&quot;</tt> routine does to the equivalent bits in the st_mode field. Finally, <tt>&quot;-d&quot;</tt> returns true if passed a device specification without an explicit directory (e.g. <tt>&quot;DUA1:&quot;</tt>), as well as if passed a directory. </p>
<p> There are <font SIZE="-1">DECC</font> feature logical names <font SIZE="-1">AND ODS-5</font> volume attributes that also control what values are returned for the date fields. </p>
<p> Note: Some sites have reported problems when using the file-access tests (<tt>&quot;-r&quot;</tt>, <tt>&quot;-w&quot;</tt>, and <tt>&quot;-x&quot;</tt>) on files accessed via <font SIZE="-1">DEC</font>&#8216;s <font SIZE="-1">DFS.</font> Specifically, since <font SIZE="-1">DFS</font> does not currently provide access to the extended file header of files on remote volumes, attempts to examine the <font SIZE="-1">ACL</font> fail, and the file tests will return false, with <tt>$!</tt> indicating that the file does not exist. You can use <tt>&quot;stat&quot;</tt> on these files, since that checks UIC-based protection only, and then manually check the appropriate bits, as defined by your C compiler&#8217;s <i>stat.h</i>, in the mode value it returns, if you need an approximation of the file&#8217;s protections.</p>
<dt>backticks</p>
<dd> Backticks create a subprocess, and pass the enclosed string to it for execution as a <font SIZE="-1">DCL</font> command. Since the subprocess is created directly via <tt>&quot;lib$spawn()&quot;</tt>, any valid <font SIZE="-1">DCL</font> command string may be specified.</p>
<dt>binmode <font SIZE="-1">FILEHANDLE</font></p>
<dd> The <tt>&quot;binmode&quot;</tt> operator will attempt to insure that no translation of carriage control occurs on input from or output to this filehandle. Since this involves reopening the file and then restoring its file position indicator, if this function returns <font SIZE="-1">FALSE,</font> the underlying filehandle may no longer point to an open file, or may point to a different position in the file than before <tt>&quot;binmode&quot;</tt> was called. </p>
<p> Note that <tt>&quot;binmode&quot;</tt> is generally not necessary when using normal filehandles; it is provided so that you can control I/O to existing record-structured files when necessary. You can also use the <tt>&quot;vmsfopen&quot;</tt> function in the VMS::Stdio extension to gain finer control of I/O to files and devices with different record structures.</p>
<dt>crypt <font SIZE="-1">PLAINTEXT, USER</font></p>
<dd> The <tt>&quot;crypt&quot;</tt> operator uses the <tt>&quot;sys$hash_password&quot;</tt> system service to generate the hashed representation of <font SIZE="-1">PLAINTEXT.</font> If <font SIZE="-1">USER</font> is a valid username, the algorithm and salt values are taken from that user&#8217;s <font SIZE="-1">UAF</font> record. If it is not, then the preferred algorithm and a salt of 0 are used. The quadword encrypted value is returned as an 8-character string. </p>
<p> The value returned by <tt>&quot;crypt&quot;</tt> may be compared against the encrypted password from the <font SIZE="-1">UAF</font> returned by the <tt>&quot;getpw*&quot;</tt> functions, in order to authenticate users. If you&#8217;re going to do this, remember that the encrypted password in the <font SIZE="-1">UAF</font> was generated using uppercase username and password strings; you&#8217;ll have to upcase the arguments to <tt>&quot;crypt&quot;</tt> to insure that you&#8217;ll get the proper value: </p>
<pre><code>
sub validate_passwd
{
    my($user, $passwd) = @_;
    my($pwdhash);
    if (!($pwdhash = (getpwnam($user))[1]) ||
        $pwdhash ne crypt("
