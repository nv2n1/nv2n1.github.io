---

title: "perlvms(1)"
name: "perlvms"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlvms/"
description: "perlvms – VMS-specific documentation for Perl"
---

<p> perlvms - VMS-specific documentation for Perl </p>
<h2>DESCRIPTION</h2>
<p> Gathered below are notes describing details of Perl 5&#8217;s behavior on <font SIZE="-1">VMS.</font> They are a supplement to the regular Perl 5 documentation, so we have focussed on the ways in which Perl 5 functions differently under <font SIZE="-1">VMS</font> than it does under Unix, and on the interactions between Perl and the rest of the operating system. We haven&#8217;t tried to duplicate complete descriptions of Perl features from the main Perl documentation, which can be found in the <i>[.pod]</i> subdirectory of the Perl distribution. </p>
<p> We hope these notes will save you from confusion and lost sleep when writing Perl scripts on <font SIZE="-1">VMS.</font> If you find we&#8217;ve missed something you think should appear here, please don&#8217;t hesitate to drop a line to vmsperl [at] perl.org.  </p>
<h2>Installation</h2>
<p> Directions for building and installing Perl 5 can be found in the file <i></i><font SIZE="-1"><i>README</i></font><i>.vms</i> in the main source directory of the Perl distribution.  </p>
<h2>Organization of Perl Images</h2>
<h3>Core Images</h3>
<p> During the build process, three Perl images are produced. <i>Miniperl.Exe</i> is an executable image which contains all of the basic functionality of Perl, but cannot take advantage of Perl <font SIZE="-1">XS</font> extensions and has a hard-wired list of library locations for loading pure-Perl modules. It is used extensively to build and test Perl and various extensions, but is not installed. </p>
<p> Most of the complete Perl resides in the shareable image <i>PerlShr.Exe</i>, which provides a core to which the Perl executable image and all Perl extensions are linked. It is generally located via the logical name <i></i><font SIZE="-1"><i>PERLSHR</i></font><i></i>. While it&#8217;s possible to put the image in <i></i><font SIZE="-1"><i>SYS$SHARE</i></font><i></i> to make it loadable, that&#8217;s not recommended. And while you may wish to <font SIZE="-1">INSTALL</font> the image for performance reasons, you should not install it with privileges; if you do, the result will not be what you expect as image privileges are disabled during Perl start-up. </p>
<p> Finally, <i>Perl.Exe</i> is an executable image containing the main entry point for Perl, as well as some initialization code. It should be placed in a public directory, and made world executable. In order to run Perl with command line arguments, you should define a foreign command to invoke this image.  </p>
<h3>Perl Extensions</h3>
<p> Perl extensions are packages which provide both <font SIZE="-1">XS</font> and Perl code to add new functionality to perl. (<font SIZE="-1">XS</font> is a meta-language which simplifies writing C code which interacts with Perl, see perlxs for more details.) The Perl code for an extension is treated like any other library module - it&#8217;s made available in your script through the appropriate <code>&quot;use&quot;</code> or <code>&quot;require&quot;</code> statement, and usually defines a Perl package containing the extension. </p>
<p> The portion of the extension provided by the <font SIZE="-1">XS</font> code may be connected to the rest of Perl in either of two ways. In the <code>static</code> configuration, the object code for the extension is linked directly into <i>PerlShr.Exe</i>, and is initialized whenever Perl is invoked. In the <code>dynamic</code> configuration, the extension&#8217;s machine code is placed into a separate shareable image, which is mapped by Perl&#8217;s DynaLoader when the extension is <code>&quot;use&quot;</code>d or <code>&quot;require&quot;</code>d in your script. This allows you to maintain the extension as a separate entity, at the cost of keeping track of the additional shareable image. Most extensions can be set up as either static or dynamic. </p>
<p> The source code for an extension usually resides in its own directory. At least three files are generally provided: <i>Extshortname</i><i>.xs</i> (where <i>Extshortname</i> is the portion of the extension&#8217;s name following the last <code>&quot;::&quot;</code>), containing the <font SIZE="-1">XS</font> code, <i>Extshortname</i><i>.pm</i>, the Perl library module for the extension, and <i>Makefile.PL</i>, a Perl script which uses the <code>&quot;MakeMaker&quot;</code> library modules supplied with Perl to generate a <i>Descrip.MMS</i> file for the extension.  </p>
<h3>Installing static extensions</h3>
<p> Since static extensions are incorporated directly into <i>PerlShr.Exe</i>, you&#8217;ll have to rebuild Perl to incorporate a new extension. You should edit the main <i>Descrip.MMS</i> or <i>Makefile</i> you use to build Perl, adding the extension&#8217;s name to the <code>&quot;ext&quot;</code> macro, and the extension&#8217;s object file to the <code>&quot;extobj&quot;</code> macro. You&#8217;ll also need to build the extension&#8217;s object file, either by adding dependencies to the main <i>Descrip.MMS</i>, or using a separate <i>Descrip.MMS</i> for the extension. Then, rebuild <i>PerlShr.Exe</i> to incorporate the new code. </p>
<p> Finally, you&#8217;ll need to copy the extension&#8217;s Perl library module to the <i>[.</i><i>Extname</i><i>]</i> subdirectory under one of the directories in <code>@INC</code>, where <i>Extname</i> is the name of the extension, with all <code>&quot;::&quot;</code> replaced by <code>&quot;.&quot;</code> (e.g. the library module for extension Foo::Bar would be copied to a <i>[.Foo.Bar]</i> subdirectory).  </p>
<h3>Installing dynamic extensions</h3>
<p> In general, the distributed kit for a Perl extension includes a file named Makefile.PL, which is a Perl program which is used to create a <i>Descrip.MMS</i> file which can be used to build and install the files required by the extension. The kit should be unpacked into a directory tree <code>not</code> under the main Perl source directory, and the procedure for building the extension is simply </p>
<pre><code>    $ perl Makefile.PL ! Create Descrip.MMS
    $ mmk ! Build necessary files
    $ mmk test ! Run test code, if supplied
    $ mmk install ! Install into public Perl tree
</code></pre>
<p> <font SIZE="-1">VMS</font> support for this process in the current release of Perl is sufficient to handle most extensions. (See the MakeMaker documentation for more details on installation options for extensions.) </p>
<dl>
<dt>&bull;</dt>
<dd> <p> the <i>[.Lib.Auto.</i><i>Arch</i><i></i>$PVers <i></i><i>Extname</i><i>]</i> subdirectory of one of the directories in <code>@INC</code> (where <i>PVers</i> is the version of Perl you&#8217;re using, as supplied in <code>$]</code>, with &#8216;.&#8216; converted to &#8216;_&#8216;), or </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> one of the directories in <code>@INC</code>, or </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> a directory which the extensions Perl library module passes to the DynaLoader when asking it to map the shareable image, or </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Sys$Share</i> or <i>Sys$Library</i>. </p>
 </dd></dl>
<p> If the shareable image isn&#8217;t in any of these places, you&#8217;ll need to define a logical name <i>Extshortname</i>, where <i>Extshortname</i> is the portion of the extension&#8217;s name after the last <code>&quot;::&quot;</code>, which translates to the full file specification of the shareable image.  </p>
<h2>File specifications</h2>
<h3>Syntax</h3>
<p> We have tried to make Perl aware of both VMS-style and Unix-style file specifications wherever possible. You may use either style, or both, on the command line and in scripts, but you may not combine the two styles within a single file specification. <font SIZE="-1">VMS</font> Perl interprets Unix pathnames in much the same way as the <font SIZE="-1">CRTL</font> (<i>e.g.</i> the first component of an absolute path is read as the device name for the <font SIZE="-1">VMS</font> file specification). There are a set of functions provided in the <code>&quot;VMS::Filespec&quot;</code> package for explicit interconversion between <font SIZE="-1">VMS</font> and Unix syntax; its documentation provides more details. </p>
<p> We&#8217;ve tried to minimize the dependence of Perl library modules on Unix syntax, but you may find that some of these, as well as some scripts written for Unix systems, will require that you use Unix syntax, since they will assume that &#8216;/&#8216; is the directory separator, <i>etc.</i> If you find instances of this in the Perl distribution itself, please let us know, so we can try to work around them. </p>
<p> Also when working on Perl programs on <font SIZE="-1">VMS,</font> if you need a syntax in a specific operating system format, then you need either to check the appropriate <font SIZE="-1">DECC$</font> feature logical, or call a conversion routine to force it to that format. </p>
<p> The feature logical name <font SIZE="-1">DECC$FILENAME_UNIX_REPORT</font> modifies traditional Perl behavior in the conversion of file specifications from Unix to <font SIZE="-1">VMS</font> format in order to follow the extended character handling rules now expected by the <font SIZE="-1">CRTL.</font> Specifically, when this feature is in effect, the <code>&quot;./.../&quot;</code> in a Unix path is now translated to <code>&quot;[.^.^.^.]&quot;</code> instead of the traditional <font SIZE="-1">VMS</font> <code>&quot;[...]&quot;</code>. To be compatible with what MakeMaker expects, if a <font SIZE="-1">VMS</font> path cannot be translated to a Unix path, it is passed through unchanged, so <code>&quot;unixify(&quot;[...]&quot;)&quot;</code> will return <code>&quot;[...]&quot;</code>. </p>
<p> There are several ambiguous cases where a conversion routine cannot determine whether an input filename is in Unix format or in <font SIZE="-1">VMS</font> format, since now both <font SIZE="-1">VMS</font> and Unix file specifications may have characters in them that could be mistaken for syntax delimiters of the other type. So some pathnames simply cannot be used in a mode that allows either type of pathname to be present. Perl will tend to assume that an ambiguous filename is in Unix format. </p>
<p> Allowing ``.&#8216;&#8216; as a version delimiter is simply incompatible with determining whether a pathname is in <font SIZE="-1">VMS</font> format or in Unix format with extended file syntax. There is no way to know whether ``perl-5.8.6&#8217;&#8216; is a Unix ``perl-5.8.6&#8217;&#8216; or a <font SIZE="-1">VMS</font> ``perl-5.8;6&#8217;&#8216; when passing it to <code>unixify()</code> or <code>vmsify()</code>. </p>
<p> The <font SIZE="-1">DECC$FILENAME_UNIX_REPORT</font> logical name controls how Perl interprets filenames to the extent that Perl uses the <font SIZE="-1">CRTL</font> internally for many purposes, and attempts to follow <font SIZE="-1">CRTL</font> conventions for reporting filenames. The <font SIZE="-1">DECC$FILENAME_UNIX_ONLY</font> feature differs in that it expects all filenames passed to the C run-time to be already in Unix format. This feature is not yet supported in Perl since Perl uses traditional OpenVMS file specifications internally and in the test harness, and it is not yet clear whether this mode will be useful or useable. The feature logical name <font SIZE="-1">DECC$POSIX_COMPLIANT_PATHNAMES</font> is new with the <font SIZE="-1">RMS</font> Symbolic Link <font SIZE="-1">SDK</font> and included with OpenVMS v8.3, but is not yet supported in Perl.  </p>
<h3>Filename Case</h3>
<p> Perl enables <font SIZE="-1">DECC$EFS_CASE_PRESERVE</font> and <font SIZE="-1">DECC$ARGV_PARSE_STYLE</font> by default. Note that the latter only takes effect when extended parse is set in the process in which Perl is running. When these features are explicitly disabled in the environment or the <font SIZE="-1">CRTL</font> does not support them, Perl follows the traditional <font SIZE="-1">CRTL</font> behavior of downcasing command-line arguments and returning file specifications in lower case only. </p>
<p> <i>N. B.</i> It is very easy to get tripped up using a mixture of other programs, external utilities, and Perl scripts that are in varying states of being able to handle case preservation. For example, a file created by an older version of an archive utility or a build utility such as <font SIZE="-1">MMK</font> or <font SIZE="-1">MMS</font> may generate a filename in all upper case even on an <font SIZE="-1">ODS-5</font> volume. If this filename is later retrieved by a Perl script or module in a case preserving environment, that upper case name may not match the mixed-case or lower-case expectations of the Perl code. Your best bet is to follow an all-or-nothing approach to case preservation: either don&#8217;t use it at all, or make sure your entire toolchain and application environment support and use it. </p>
<p> OpenVMS Alpha v7.3-1 and later and all version of OpenVMS I64 support case sensitivity as a process setting (see <code>&quot;SET PROCESS /CASE_LOOKUP=SENSITIVE&quot;</code>). Perl does not currently support case sensitivity on <font SIZE="-1">VMS,</font> but it may in the future, so Perl programs should use the <code>&quot;File::Spec-&gt;case_tolerant&quot;</code> method to determine the state, and not the <code>$^O</code> variable.  </p>
<h3>Symbolic Links</h3>
<p> When built on an <font SIZE="-1">ODS-5</font> volume with symbolic links enabled, Perl by default supports symbolic links when the requisite support is available in the filesystem and <font SIZE="-1">CRTL</font> (generally 64-bit OpenVMS v8.3 and later). There are a number of limitations and caveats to be aware of when working with symbolic links on <font SIZE="-1">VMS.</font> Most notably, the target of a valid symbolic link must be expressed as a Unix-style path and it must exist on a volume visible from your <font SIZE="-1">POSIX</font> root (see the <code>&quot;SHOW ROOT&quot;</code> command in <font SIZE="-1">DCL</font> help). For further details on symbolic link capabilities and requirements, see chapter 12 of the <font SIZE="-1">CRTL</font> manual that ships with OpenVMS v8.3 or later.  </p>
<h3>Wildcard expansion</h3>
<p> File specifications containing wildcards are allowed both on the command line and within Perl globs (e.g. <code>&quot;&lt;*.c&gt;&quot;</code>). If the wildcard filespec uses <font SIZE="-1">VMS</font> syntax, the resultant filespecs will follow <font SIZE="-1">VMS</font> syntax; if a Unix-style filespec is passed in, Unix-style filespecs will be returned. Similar to the behavior of wildcard globbing for a Unix shell, one can escape command line wildcards with double quotation marks <code>&quot;&quot;&quot;</code> around a perl program command line argument. However, owing to the stripping of <code>&quot;&quot;&quot;</code> characters carried out by the C handling of argv you will need to escape a construct such as this one (in a directory containing the files <i></i><font SIZE="-1"><i>PERL.C</i></font><i></i>, <i></i><font SIZE="-1"><i>PERL.EXE</i></font><i></i>, <i></i><font SIZE="-1"><i>PERL.H</i></font><i></i>, and <i></i><font SIZE="-1"><i>PERL.OBJ</i></font><i></i>): </p>
<pre><code>    $ perl -e &quot;print join(' ',@ARGV)&quot; perl.*
    perl.c perl.exe perl.h perl.obj
</code></pre>
<p> in the following triple quoted manner: </p>
<pre><code>    $ perl -e &quot;print join(' ',@ARGV)&quot; &quot;&quot;&quot;perl.*&quot;&quot;&quot;
    perl.*
</code></pre>
<p> In both the case of unquoted command line arguments or in calls to <code>&quot;glob()&quot;</code> <font SIZE="-1">VMS</font> wildcard expansion is performed. (csh-style wildcard expansion is available if you use <code>&quot;File::Glob::glob&quot;</code>.) If the wildcard filespec contains a device or directory specification, then the resultant filespecs will also contain a device and directory; otherwise, device and directory information are removed. VMS-style resultant filespecs will contain a full device and directory, while Unix-style resultant filespecs will contain only as much of a directory path as was present in the input filespec. For example, if your default directory is Perl_Root:[000000], the expansion of <code>&quot;[.t]*.*&quot;</code> will yield filespecs like ``perl_root:[t]base.dir&#8217;&#8216;, while the expansion of <code>&quot;t/*/*&quot;</code> will yield filespecs like ``t/base.dir&#8217;&#8216;. (This is done to match the behavior of glob expansion performed by Unix shells.) </p>
<p> Similarly, the resultant filespec will contain the file version only if one was present in the input filespec.  </p>
<h3>Pipes</h3>
<p> Input and output pipes to Perl filehandles are supported; the ``file name&#8217;&#8216; is passed to lib$<code>spawn()</code> for asynchronous execution. You should be careful to close any pipes you have opened in a Perl script, lest you leave any ``orphaned&#8217;&#8216; subprocesses around when Perl exits. </p>
<p> You may also use backticks to invoke a <font SIZE="-1">DCL</font> subprocess, whose output is used as the return value of the expression. The string between the backticks is handled as if it were the argument to the <code>&quot;system&quot;</code> operator (see below). In this case, Perl will wait for the subprocess to complete before continuing. </p>
<p> The mailbox (<font SIZE="-1">MBX</font>) that perl can create to communicate with a pipe defaults to a buffer size of 8192 on 64-bit systems, 512 on <font SIZE="-1">VAX.</font> The default buffer size is adjustable via the logical name <font SIZE="-1">PERL_MBX_SIZE</font> provided that the value falls between 128 and the <font SIZE="-1">SYSGEN</font> parameter <font SIZE="-1">MAXBUF</font> inclusive. For example, to set the mailbox size to 32767 use <code>&quot;$ENV{&#8216;PERL_MBX_SIZE&#8217;} = 32767;&quot;</code> and then open and use pipe constructs. An alternative would be to issue the command: </p>
<pre><code>    $ Define PERL_MBX_SIZE 32767
</code></pre>
<p> before running your wide record pipe program. A larger value may improve performance at the expense of the <font SIZE="-1">BYTLM UAF</font> quota.  </p>
<h2>PERL5LIB and PERLLIB</h2>
<p> The <font SIZE="-1">PERL5LIB</font> and <font SIZE="-1">PERLLIB</font> environment elements work as documented in perl, except that the element separator is, by default, &#8216;|&#8216; instead of &#8216;:&#8216;. However, when running under a Unix shell as determined by the logical name <code>&quot;GNV$UNIX_SHELL&quot;</code>, the separator will be &#8216;:&#8216; as on Unix systems. The directory specifications may use either <font SIZE="-1">VMS</font> or Unix syntax.  </p>
<h2>The Perl Forked Debugger</h2>
<p> The Perl forked debugger places the debugger commands and output in a separate X-11 terminal window so that commands and output from multiple processes are not mixed together. </p>
<p> Perl on <font SIZE="-1">VMS</font> supports an emulation of the forked debugger when Perl is run on a <font SIZE="-1">VMS</font> system that has X11 support installed. </p>
<p> To use the forked debugger, you need to have the default display set to an X-11 Server and some environment variables set that Unix expects. </p>
<p> The forked debugger requires the environment variable <code>&quot;TERM&quot;</code> to be <code>&quot;xterm&quot;</code>, and the environment variable <code>&quot;DISPLAY&quot;</code> to exist. <code>&quot;xterm&quot;</code> must be in lower case. </p>
<pre><code>  $define TERM &quot;xterm&quot;
  $define DISPLAY &quot;hostname:0.0&quot;
</code></pre>
<p> Currently the value of <code>&quot;DISPLAY&quot;</code> is ignored. It is recommended that it be set to be the hostname of the display, the server and screen in Unix notation. In the future the value of <font SIZE="-1">DISPLAY</font> may be honored by Perl instead of using the default display. </p>
<p> It may be helpful to always use the forked debugger so that script I/O is separated from debugger I/O. You can force the debugger to be forked by assigning a value to the logical name &lt;<font SIZE="-1">PERLDB_PIDS</font>&gt; that is not a process identification number. </p>
<pre><code>  $define PERLDB_PIDS XXXX
</code></pre>
<h2>PERL_VMS_EXCEPTION_DEBUG</h2>
<p> The <font SIZE="-1">PERL_VMS_EXCEPTION_DEBUG</font> being defined as ``<font SIZE="-1">ENABLE&#8217;&#8216;</font> will cause the <font SIZE="-1">VMS</font> debugger to be invoked if a fatal exception that is not otherwise handled is raised. The purpose of this is to allow debugging of internal Perl problems that would cause such a condition. </p>
<p> This allows the programmer to look at the execution stack and variables to find out the cause of the exception. As the debugger is being invoked as the Perl interpreter is about to do a fatal exit, continuing the execution in debug mode is usually not practical. </p>
<p> Starting Perl in the <font SIZE="-1">VMS</font> debugger may change the program execution profile in a way that such problems are not reproduced. </p>
<p> The <code>&quot;kill&quot;</code> function can be used to test this functionality from within a program. </p>
<p> In typical <font SIZE="-1">VMS</font> style, only the first letter of the value of this logical name is actually checked in a case insensitive mode, and it is considered enabled if it is the value ``T&#8217;&#8216;,``1&#8217;&#8216; or ``E&#8217;&#8216;. </p>
<p> This logical name must be defined before Perl is started.  </p>
<h2>Command line</h2>
<h3>I/O redirection and backgrounding</h3>
<p> Perl for <font SIZE="-1">VMS</font> supports redirection of input and output on the command line, using a subset of Bourne shell syntax: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;&lt;file&quot;</code> reads stdin from <code>&quot;file&quot;</code>, </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;&gt;file&quot;</code> writes stdout to <code>&quot;file&quot;</code>, </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;&gt;&gt;file&quot;</code> appends stdout to <code>&quot;file&quot;</code>, </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;2&gt;file&quot;</code> writes stderr to <code>&quot;file&quot;</code>, </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;2&gt;&gt;file&quot;</code> appends stderr to <code>&quot;file&quot;</code>, and </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;2&gt;&amp;1&quot;</code> redirects stderr to stdout. </p>
 </dd></dl>
<p> In addition, output may be piped to a subprocess, using the character &#8216;|&#8216;. Anything after this character on the command line is passed to a subprocess for execution; the subprocess takes the output of Perl as its input. </p>
<p> Finally, if the command line ends with &#8216;&amp;&#8216;, the entire command is run in the background as an asynchronous subprocess.  </p>
<h3>Command line switches</h3>
<p> The following command line switches behave differently under <font SIZE="-1">VMS</font> than described in perlrun. Note also that in order to pass uppercase switches to Perl, you need to enclose them in double-quotes on the command line, since the <font SIZE="-1">CRTL</font> downcases all unquoted strings. </p>
<p> On newer 64 bit versions of OpenVMS, a process setting now controls if the quoting is needed to preserve the case of command line arguments. </p>
<dl>
<dt>-i</dt>
<dd> <p> If the <code>&quot;-i&quot;</code> switch is present but no extension for a backup copy is given, then inplace editing creates a new version of a file; the existing copy is not deleted. (Note that if an extension is given, an existing file is renamed to the backup file, as is the case under other operating systems, so it does not remain as a previous version under the original filename.) </p>
 </dd>
<dt>-S</dt>
<dd> <p> If the <code>&quot;-S&quot;</code> or <code>&quot;-&quot;S&quot;&quot;</code> switch is present <i>and</i> the script name does not contain a directory, then Perl translates the logical name <font SIZE="-1">DCL$PATH</font> as a searchlist, using each translation as a directory in which to look for the script. In addition, if no file type is specified, Perl looks in each directory for a file matching the name specified, with a blank type, a type of <i>.pl</i>, and a type of <i>.com</i>, in that order. </p>
 </dd>
<dt>-u</dt>
<dd> <p> The <code>&quot;-u&quot;</code> switch causes the <font SIZE="-1">VMS</font> debugger to be invoked after the Perl program is compiled, but before it has run. It does not create a core dump file. </p>
 </dd></dl>
<h2>Perl functions</h2>
<p> As of the time this document was last revised, the following Perl functions were implemented in the <font SIZE="-1">VMS</font> port of Perl (functions marked with * are discussed in more detail below): </p>
<pre><code>    file tests*, abs, alarm, atan, backticks*, binmode*, bless,
    caller, chdir, chmod, chown, chomp, chop, chr,
    close, closedir, cos, crypt*, defined, delete, die, do, dump*,
    each, endgrent, endpwent, eof, eval, exec*, exists, exit, exp,
    fileno, flock getc, getgrent*, getgrgid*, getgrnam, getlogin,
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
</code></pre>
<p> The following functions were not implemented in the <font SIZE="-1">VMS</font> port, and calling them produces a fatal error (usually) or undefined behavior (rarely, we hope): </p>
<pre><code>    chroot, dbmclose, dbmopen, fork*, getpgrp, getpriority,
    msgctl, msgget, msgsend, msgrcv, semctl,
    semget, semop, setpgrp, setpriority, shmctl, shmget,
    shmread, shmwrite, syscall
</code></pre>
<p> The following functions are available on Perls compiled with Dec C 5.2 or greater and running <font SIZE="-1">VMS 7.0</font> or greater: </p>
<pre><code>    truncate
</code></pre>
<p> The following functions are available on Perls built on <font SIZE="-1">VMS 7.2</font> or greater: </p>
<pre><code>    fcntl (without locking)
</code></pre>
<p> The following functions may or may not be implemented, depending on what type of socket support you&#8217;ve built into your copy of Perl: </p>
<pre><code>    accept, bind, connect, getpeername,
    gethostbyname, getnetbyname, getprotobyname,
    getservbyname, gethostbyaddr, getnetbyaddr,
    getprotobynumber, getservbyport, gethostent,
    getnetent, getprotoent, getservent, sethostent,
    setnetent, setprotoent, setservent, endhostent,
    endnetent, endprotoent, endservent, getsockname,
    getsockopt, listen, recv, select(system call)*,
    send, setsockopt, shutdown, socket
</code></pre>
<p> The following function is available on Perls built on 64 bit OpenVMS v8.2 with hard links enabled on an <font SIZE="-1">ODS-5</font> formatted build disk. <font SIZE="-1">CRTL</font> support is in principle available as of OpenVMS v7.3-1, and better configuration support could detect this. </p>
<pre><code>    link
</code></pre>
<p> The following functions are available on Perls built on 64 bit OpenVMS v8.2 and later. <font SIZE="-1">CRTL</font> support is in principle available as of OpenVMS v7.3-2, and better configuration support could detect this. </p>
<pre><code>   getgrgid, getgrnam, getpwnam, getpwuid,
   setgrent, ttyname
</code></pre>
<p> The following functions are available on Perls built on 64 bit OpenVMS v8.2 and later. </p>
<pre><code>   statvfs, socketpair
</code></pre>
<dl>
<dt>File tests</dt>
<dd> <p> The tests <code>&quot;-b&quot;</code>, <code>&quot;-B&quot;</code>, <code>&quot;-c&quot;</code>, <code>&quot;-C&quot;</code>, <code>&quot;-d&quot;</code>, <code>&quot;-e&quot;</code>, <code>&quot;-f&quot;</code>, <code>&quot;-o&quot;</code>, <code>&quot;-M&quot;</code>, <code>&quot;-s&quot;</code>, <code>&quot;-S&quot;</code>, <code>&quot;-t&quot;</code>, <code>&quot;-T&quot;</code>, and <code>&quot;-z&quot;</code> work as advertised. The return values for <code>&quot;-r&quot;</code>, <code>&quot;-w&quot;</code>, and <code>&quot;-x&quot;</code> tell you whether you can actually access the file; this may not reflect the UIC-based file protections. Since real and effective <font SIZE="-1">UIC</font> don&#8217;t differ under <font SIZE="-1">VMS,</font> <code>&quot;-O&quot;</code>, <code>&quot;-R&quot;</code>, <code>&quot;-W&quot;</code>, and <code>&quot;-X&quot;</code> are equivalent to <code>&quot;-o&quot;</code>, <code>&quot;-r&quot;</code>, <code>&quot;-w&quot;</code>, and <code>&quot;-x&quot;</code>. Similarly, several other tests, including <code>&quot;-A&quot;</code>, <code>&quot;-g&quot;</code>, <code>&quot;-k&quot;</code>, <code>&quot;-l&quot;</code>, <code>&quot;-p&quot;</code>, and <code>&quot;-u&quot;</code>, aren&#8217;t particularly meaningful under <font SIZE="-1">VMS,</font> and the values returned by these tests reflect whatever your <font SIZE="-1">CRTL</font> <code>&quot;stat()&quot;</code> routine does to the equivalent bits in the st_mode field. Finally, <code>&quot;-d&quot;</code> returns true if passed a device specification without an explicit directory (e.g. <code>&quot;DUA1:&quot;</code>), as well as if passed a directory. </p>
<p> There are <font SIZE="-1">DECC</font> feature logical names <font SIZE="-1">AND ODS-5</font> volume attributes that also control what values are returned for the date fields. </p>
<p> Note: Some sites have reported problems when using the file-access tests (<code>&quot;-r&quot;</code>, <code>&quot;-w&quot;</code>, and <code>&quot;-x&quot;</code>) on files accessed via <font SIZE="-1">DEC</font>&#8216;s <font SIZE="-1">DFS.</font> Specifically, since <font SIZE="-1">DFS</font> does not currently provide access to the extended file header of files on remote volumes, attempts to examine the <font SIZE="-1">ACL</font> fail, and the file tests will return false, with <code>$!</code> indicating that the file does not exist. You can use <code>&quot;stat&quot;</code> on these files, since that checks UIC-based protection only, and then manually check the appropriate bits, as defined by your C compiler&#8217;s <i>stat.h</i>, in the mode value it returns, if you need an approximation of the file&#8217;s protections. </p>
 </dd>
<dt>backticks</dt>
<dd> <p> Backticks create a subprocess, and pass the enclosed string to it for execution as a <font SIZE="-1">DCL</font> command. Since the subprocess is created directly via <code>&quot;lib$spawn()&quot;</code>, any valid <font SIZE="-1">DCL</font> command string may be specified. </p>
 </dd>
<dt>binmode <font SIZE="-1">FILEHANDLE</font></dt>
<dd> <p> The <code>&quot;binmode&quot;</code> operator will attempt to insure that no translation of carriage control occurs on input from or output to this filehandle. Since this involves reopening the file and then restoring its file position indicator, if this function returns <font SIZE="-1">FALSE,</font> the underlying filehandle may no longer point to an open file, or may point to a different position in the file than before <code>&quot;binmode&quot;</code> was called. </p>
<p> Note that <code>&quot;binmode&quot;</code> is generally not necessary when using normal filehandles; it is provided so that you can control I/O to existing record-structured files when necessary. You can also use the <code>&quot;vmsfopen&quot;</code> function in the VMS::Stdio extension to gain finer control of I/O to files and devices with different record structures. </p>
 </dd>
<dt>crypt <font SIZE="-1">PLAINTEXT, USER</font></dt>
<dd> <p> The <code>&quot;crypt&quot;</code> operator uses the <code>&quot;sys$hash_password&quot;</code> system service to generate the hashed representation of <font SIZE="-1">PLAINTEXT.</font> If <font SIZE="-1">USER</font> is a valid username, the algorithm and salt values are taken from that user&#8217;s <font SIZE="-1">UAF</font> record. If it is not, then the preferred algorithm and a salt of 0 are used. The quadword encrypted value is returned as an 8-character string. </p>
<p> The value returned by <code>&quot;crypt&quot;</code> may be compared against the encrypted password from the <font SIZE="-1">UAF</font> returned by the <code>&quot;getpw*&quot;</code> functions, in order to authenticate users. If you&#8217;re going to do this, remember that the encrypted password in the <font SIZE="-1">UAF</font> was generated using uppercase username and password strings; you&#8217;ll have to upcase the arguments to <code>&quot;crypt&quot;</code> to insure that you&#8217;ll get the proper value: </p>
<pre><code>    sub validate_passwd {
        my($user,$passwd) = @_;
        my($pwdhash);
        if ( !($pwdhash = (getpwnam($user))[1]) ||
               $pwdhash ne crypt(&quot;\U$passwd&quot;,&quot;\U$name&quot;) ) {
            intruder_alert($name);
        }
        return 1;
    }
</code></pre>
 </dd>
<dt>die</dt>
<dd> <p> <code>&quot;die&quot;</code> will force the native <font SIZE="-1">VMS</font> exit status to be an <font SIZE="-1">SS$_ABORT</font> code if neither of the $! or $? status values are ones that would cause the native status to be interpreted as being what <font SIZE="-1">VMS</font> classifies as <font SIZE="-1">SEVERE_ERROR</font> severity for <font SIZE="-1">DCL</font> error handling. </p>
<p> When <code>&quot;PERL_VMS_POSIX_EXIT&quot;</code> is active (see ``$?&#8216;&#8216; below), the native <font SIZE="-1">VMS</font> exit status value will have either one of the <code>$!</code> or <code>$?</code> or <code>$^E</code> or the Unix value 255 encoded into it in a way that the effective original value can be decoded by other programs written in C, including Perl and the <font SIZE="-1">GNV</font> package. As per the normal non-VMS behavior of <code>&quot;die&quot;</code> if either <code>$!</code> or <code>$?</code> are non-zero, one of those values will be encoded into a native <font SIZE="-1">VMS</font> status value. If both of the Unix status values are 0, and the <code>$^E</code> value is set one of <font SIZE="-1">ERROR</font> or <font SIZE="-1">SEVERE_ERROR</font> severity, then the <code>$^E</code> value will be used as the exit code as is. If none of the above apply, the Unix value of 255 will be encoded into a native <font SIZE="-1">VMS</font> exit status value. </p>
<p> Please note a significant difference in the behavior of <code>&quot;die&quot;</code> in the <code>&quot;PERL_VMS_POSIX_EXIT&quot;</code> mode is that it does not force a <font SIZE="-1">VMS SEVERE_ERROR</font> status on exit. The Unix exit values of 2 through 255 will be encoded in <font SIZE="-1">VMS</font> status values with severity levels of <font SIZE="-1">SUCCESS.</font> The Unix exit value of 1 will be encoded in a <font SIZE="-1">VMS</font> status value with a severity level of <font SIZE="-1">ERROR.</font> This is to be compatible with how the <font SIZE="-1">VMS C</font> library encodes these values. </p>
<p> The minimum severity level set by <code>&quot;die&quot;</code> in <code>&quot;PERL_VMS_POSIX_EXIT&quot;</code> mode may be changed to be <font SIZE="-1">ERROR</font> or higher in the future depending on the results of testing and further review. </p>
<p> See ``$?&#8216;&#8216; for a description of the encoding of the Unix value to produce a native <font SIZE="-1">VMS</font> status containing it. </p>
 </dd>
<dt>dump</dt>
<dd> <p> Rather than causing Perl to abort and dump core, the <code>&quot;dump&quot;</code> operator invokes the <font SIZE="-1">VMS</font> debugger. If you continue to execute the Perl program under the debugger, control will be transferred to the label specified as the argument to <code>&quot;dump&quot;</code>, or, if no label was specified, back to the beginning of the program. All other state of the program (<i>e.g.</i> values of variables, open file handles) are not affected by calling <code>&quot;dump&quot;</code>. </p>
 </dd>
<dt>exec <font SIZE="-1">LIST</font></dt>
<dd> <p> A call to <code>&quot;exec&quot;</code> will cause Perl to exit, and to invoke the command given as an argument to <code>&quot;exec&quot;</code> via <code>&quot;lib$do_command&quot;</code>. If the argument begins with &#8216;@&#8216; or &#8216;$&#8216; (other than as part of a filespec), then it is executed as a <font SIZE="-1">DCL</font> command. Otherwise, the first token on the command line is treated as the filespec of an image to run, and an attempt is made to invoke it (using <i>.Exe</i> and the process defaults to expand the filespec) and pass the rest of <code>&quot;exec&quot;</code>&#8216;s argument to it as parameters. If the token has no file type, and matches a file with null type, then an attempt is made to determine whether the file is an executable image which should be invoked using <code>&quot;MCR&quot;</code> or a text file which should be passed to <font SIZE="-1">DCL</font> as a command procedure. </p>
 </dd>
<dt>fork</dt>
<dd> <p> While in principle the <code>&quot;fork&quot;</code> operator could be implemented via (and with the same rather severe limitations as) the <font SIZE="-1">CRTL</font> <code>&quot;vfork()&quot;</code> routine, and while some internal support to do just that is in place, the implementation has never been completed, making <code>&quot;fork&quot;</code> currently unavailable. A true kernel <code>&quot;fork()&quot;</code> is expected in a future version of <font SIZE="-1">VMS,</font> and the pseudo-fork based on interpreter threads may be available in a future version of Perl on <font SIZE="-1">VMS</font> (see perlfork). In the meantime, use <code>&quot;system&quot;</code>, backticks, or piped filehandles to create subprocesses. </p>
 </dd>
<dt>getpwent</dt>
<dd>  </dd>
<dt>getpwnam</dt>
<dd>  </dd>
<dt>getpwuid</dt>
<dd> <p> These operators obtain the information described in perlfunc, if you have the privileges necessary to retrieve the named user&#8217;s <font SIZE="-1">UAF</font> information via <code>&quot;sys$getuai&quot;</code>. If not, then only the <code>$name</code>, <code>$uid</code>, and <code>$gid</code> items are returned. The <code>$dir</code> item contains the login directory in <font SIZE="-1">VMS</font> syntax, while the <code>$comment</code> item contains the login directory in Unix syntax. The <code>$gcos</code> item contains the owner field from the <font SIZE="-1">UAF</font> record. The <code>$quota</code> item is not used. </p>
 </dd>
<dt>gmtime</dt>
<dd> <p> The <code>&quot;gmtime&quot;</code> operator will function properly if you have a working <font SIZE="-1">CRTL</font> <code>&quot;gmtime()&quot;</code> routine, or if the logical name <font SIZE="-1">SYS$TIMEZONE_DIFFERENTIAL</font> is defined as the number of seconds which must be added to <font SIZE="-1">UTC</font> to yield local time. (This logical name is defined automatically if you are running a version of <font SIZE="-1">VMS</font> with built-in <font SIZE="-1">UTC</font> support.) If neither of these cases is true, a warning message is printed, and <code>&quot;undef&quot;</code> is returned. </p>
 </dd>
<dt>kill</dt>
<dd> <p> In most cases, <code>&quot;kill&quot;</code> is implemented via the undocumented system service <code>$SIGPRC</code>, which has the same calling sequence as <code>$FORCEX</code>, but throws an exception in the target process rather than forcing it to call <code>$EXIT</code>. Generally speaking, <code>&quot;kill&quot;</code> follows the behavior of the <font SIZE="-1">CRTL</font>&#8216;s <code>&quot;kill()&quot;</code> function, but unlike that function can be called from within a signal handler. Also, unlike the <code>&quot;kill&quot;</code> in some versions of the <font SIZE="-1">CRTL,</font> Perl&#8217;s <code>&quot;kill&quot;</code> checks the validity of the signal passed in and returns an error rather than attempting to send an unrecognized signal. </p>
<p> Also, negative signal values don&#8217;t do anything special under <font SIZE="-1">VMS</font>; they&#8217;re just converted to the corresponding positive value. </p>
 </dd>
<dt>qx//</dt>
<dd> <p> See the entry on <code>&quot;backticks&quot;</code> above. </p>
 </dd>
<dt>select (system call)</dt>
<dd> <p> If Perl was not built with socket support, the system call version of <code>&quot;select&quot;</code> is not available at all. If socket support is present, then the system call version of <code>&quot;select&quot;</code> functions only for file descriptors attached to sockets. It will not provide information about regular files or pipes, since the <font SIZE="-1">CRTL</font> <code>&quot;select()&quot;</code> routine does not provide this functionality. </p>
 </dd>
<dt>stat <font SIZE="-1">EXPR</font></dt>
<dd> <p> Since <font SIZE="-1">VMS</font> keeps track of files according to a different scheme than Unix, it&#8217;s not really possible to represent the file&#8217;s <font SIZE="-1">ID</font> in the <code>&quot;st_dev&quot;</code> and <code>&quot;st_ino&quot;</code> fields of a <code>&quot;struct stat&quot;</code>. Perl tries its best, though, and the values it uses are pretty unlikely to be the same for two different files. We can&#8217;t guarantee this, though, so caveat scriptor. </p>
 </dd>
<dt>system <font SIZE="-1">LIST</font></dt>
<dd> <p> The <code>&quot;system&quot;</code> operator creates a subprocess, and passes its arguments to the subprocess for execution as a <font SIZE="-1">DCL</font> command. Since the subprocess is created directly via <code>&quot;lib$spawn()&quot;</code>, any valid <font SIZE="-1">DCL</font> command string may be specified. If the string begins with &#8216;@&#8216;, it is treated as a <font SIZE="-1">DCL</font> command unconditionally. Otherwise, if the first token contains a character used as a delimiter in file specification (e.g. <code>&quot;:&quot;</code> or <code>&quot;]&quot;</code>), an attempt is made to expand it using a default type of <i>.Exe</i> and the process defaults, and if successful, the resulting file is invoked via <code>&quot;MCR&quot;</code>. This allows you to invoke an image directly simply by passing the file specification to <code>&quot;system&quot;</code>, a common Unixish idiom. If the token has no file type, and matches a file with null type, then an attempt is made to determine whether the file is an executable image which should be invoked using <code>&quot;MCR&quot;</code> or a text file which should be passed to <font SIZE="-1">DCL</font> as a command procedure. </p>
<p> If <font SIZE="-1">LIST</font> consists of the empty string, <code>&quot;system&quot;</code> spawns an interactive <font SIZE="-1">DCL</font> subprocess, in the same fashion as typing <font SIZE="-1"><code>SPAWN</code></font> at the <font SIZE="-1">DCL</font> prompt. </p>
<p> Perl waits for the subprocess to complete before continuing execution in the current process. As described in perlfunc, the return value of <code>&quot;system&quot;</code> is a fake ``status&#8217;&#8216; which follows <font SIZE="-1">POSIX</font> semantics unless the pragma <code>&quot;use vmsish &#8216;status&#8217;&quot;</code> is in effect; see the description of <code>$?</code> in this document for more detail. </p>
 </dd>
<dt>time</dt>
<dd> <p> The value returned by <code>&quot;time&quot;</code> is the offset in seconds from 01-JAN-1970 00:00:00 (just like the <font SIZE="-1">CRTL</font>&#8216;s <code>times()</code> routine), in order to make life easier for code coming in from the POSIX/Unix world. </p>
 </dd>
<dt>times</dt>
<dd> <p> The array returned by the <code>&quot;times&quot;</code> operator is divided up according to the same rules the <font SIZE="-1">CRTL</font> <code>&quot;times()&quot;</code> routine. Therefore, the ``system time&#8217;&#8216; elements will always be 0, since there is no difference between ``user time&#8217;&#8216; and ``system&#8217;&#8216; time under <font SIZE="-1">VMS,</font> and the time accumulated by a subprocess may or may not appear separately in the ``child time&#8217;&#8216; field, depending on whether <code>&quot;times()&quot;</code> keeps track of subprocesses separately. Note especially that the <font SIZE="-1">VAXCRTL</font> (at least) keeps track only of subprocesses spawned using <code>&quot;fork()&quot;</code> and <code>&quot;exec()&quot;</code>; it will not accumulate the times of subprocesses spawned via pipes, <code>&quot;system()&quot;</code>, or backticks. </p>
 </dd>
<dt>unlink <font SIZE="-1">LIST</font></dt>
<dd> <p> <code>&quot;unlink&quot;</code> will delete the highest version of a file only; in order to delete all versions, you need to say </p>
<pre><code>    1 while unlink LIST;
</code></pre>
<p> You may need to make this change to scripts written for a Unix system which expect that after a call to <code>&quot;unlink&quot;</code>, no files with the names passed to <code>&quot;unlink&quot;</code> will exist. (Note: This can be changed at compile time; if you <code>&quot;use Config&quot;</code> and <code>$Config{&#8216;d_unlink_all_versions&#8217;}</code> is <code>&quot;define&quot;</code>, then <code>&quot;unlink&quot;</code> will delete all versions of a file on the first call.) </p>
<p> <code>&quot;unlink&quot;</code> will delete a file if at all possible, even if it requires changing file protection (though it won&#8217;t try to change the protection of the parent directory). You can tell whether you&#8217;ve got explicit delete access to a file by using the <code>&quot;VMS::Filespec::candelete&quot;</code> operator. For instance, in order to delete only files to which you have delete access, you could say something like </p>
<pre><code>    sub safe_unlink {
        my($file,$num);
        foreach $file (@_) {
            next unless VMS::Filespec::candelete($file);
            $num += unlink $file;
        }
        $num;
    }
</code></pre>
<p> (or you could just use <code>&quot;VMS::Stdio::remove&quot;</code>, if you&#8217;ve installed the VMS::Stdio extension distributed with Perl). If <code>&quot;unlink&quot;</code> has to change the file protection to delete the file, and you interrupt it in midstream, the file may be left intact, but with a changed <font SIZE="-1">ACL</font> allowing you delete access. </p>
<p> This behavior of <code>&quot;unlink&quot;</code> is to be compatible with <font SIZE="-1">POSIX</font> behavior and not traditional <font SIZE="-1">VMS</font> behavior. </p>
 </dd>
<dt>utime <font SIZE="-1">LIST</font></dt>
<dd> <p> This operator changes only the modification time of the file (<font SIZE="-1">VMS</font> revision date) on <font SIZE="-1">ODS-2</font> volumes and <font SIZE="-1">ODS-5</font> volumes without access dates enabled. On <font SIZE="-1">ODS-5</font> volumes with access dates enabled, the true access time is modified. </p>
 </dd>
<dt>waitpid <font SIZE="-1">PID,FLAGS</font></dt>
<dd> <p> If <font SIZE="-1">PID</font> is a subprocess started by a piped <code>&quot;open()&quot;</code> (see open), <code>&quot;waitpid&quot;</code> will wait for that subprocess, and return its final status value in <code>$?</code>. If <font SIZE="-1">PID</font> is a subprocess created in some other way (e.g. SPAWNed before Perl was invoked), <code>&quot;waitpid&quot;</code> will simply check once per second whether the process has completed, and return when it has. (If <font SIZE="-1">PID</font> specifies a process that isn&#8217;t a subprocess of the current process, and you invoked Perl with the <code>&quot;-w&quot;</code> switch, a warning will be issued.) </p>
<p> Returns <font SIZE="-1">PID</font> on success, -1 on error. The <font SIZE="-1">FLAGS</font> argument is ignored in all cases. </p>
 </dd></dl>
<h2>Perl variables</h2>
<p> The following VMS-specific information applies to the indicated ``special&#8217;&#8216; Perl variables, in addition to the general information in perlvar. Where there is a conflict, this information takes precedence. </p>
<dl>
<dt>%ENV</dt>
<dd> <p> The operation of the <code>%ENV</code> array depends on the translation of the logical name <i></i><font SIZE="-1"><i>PERL_ENV_TABLES</i></font><i></i>. If defined, it should be a search list, each element of which specifies a location for <code>%ENV</code> elements. If you tell Perl to read or set the element <code>&quot;$ENV{&quot;</code><i>name</i><code>&quot;}&quot;</code>, then Perl uses the translations of <i></i><font SIZE="-1"><i>PERL_ENV_TABLES</i></font><i></i> as follows: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><font SIZE="-1">CRTL_ENV</font></dt>
<dd> <p> This string tells Perl to consult the <font SIZE="-1">CRTL</font>&#8216;s internal <code>&quot;environ&quot;</code> array of key-value pairs, using <i>name</i> as the key. In most cases, this contains only a few keys, but if Perl was invoked via the C <code>&quot;exec[lv]e()&quot;</code> function, as is the case for some embedded Perl applications or when running under a shell such as <font SIZE="-1">GNV</font> bash, the <code>&quot;environ&quot;</code> array may have been populated by the calling program. </p>
 </dd>
<dt>CLISYM_[<font SIZE="-1">LOCAL</font>]</dt>
<dd> <p> A string beginning with <code>&quot;CLISYM_&quot;</code>tells Perl to consult the <font SIZE="-1">CLI</font>&#8216;s symbol tables, using <i>name</i> as the name of the symbol. When reading an element of <code>%ENV</code>, the local symbol table is scanned first, followed by the global symbol table.. The characters following <code>&quot;CLISYM_&quot;</code> are significant when an element of <code>%ENV</code> is set or deleted: if the complete string is <code>&quot;CLISYM_LOCAL&quot;</code>, the change is made in the local symbol table; otherwise the global symbol table is changed. </p>
 </dd>
<dt>Any other string</dt>
<dd> <p> If an element of <i></i><font SIZE="-1"><i>PERL_ENV_TABLES</i></font><i></i> translates to any other string, that string is used as the name of a logical name table, which is consulted using <i>name</i> as the logical name. The normal search order of access modes is used. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> <i></i><font SIZE="-1"><i>PERL_ENV_TABLES</i></font><i></i> is translated once when Perl starts up; any changes you make while Perl is running do not affect the behavior of <code>%ENV</code>. If <i></i><font SIZE="-1"><i>PERL_ENV_TABLES</i></font><i></i> is not defined, then Perl defaults to consulting first the logical name tables specified by <i></i><font SIZE="-1"><i>LNM$FILE_DEV</i></font><i></i>, and then the <font SIZE="-1">CRTL</font> <code>&quot;environ&quot;</code> array. This default order is reversed when the logical name <i></i><font SIZE="-1"><i>GNV$UNIX_SHELL</i></font><i></i> is defined, such as when running under <font SIZE="-1">GNV</font> bash. </p>
<p> For operations on <code>%ENV</code> entries based on logical names or <font SIZE="-1">DCL</font> symbols, the key string is treated as if it were entirely uppercase, regardless of the case actually specified in the Perl expression. Entries in <code>%ENV</code> based on the <font SIZE="-1">CRTL</font>&#8216;s environ array preserve the case of the key string when stored, and lookups are case sensitive. </p>
<p> When an element of <code>%ENV</code> is read, the locations to which <i></i><font SIZE="-1"><i>PERL_ENV_TABLES</i></font><i></i> points are checked in order, and the value obtained from the first successful lookup is returned. If the name of the <code>%ENV</code> element contains a semi-colon, it and any characters after it are removed. These are ignored when the <font SIZE="-1">CRTL</font> <code>&quot;environ&quot;</code> array or a <font SIZE="-1">CLI</font> symbol table is consulted. However, the name is looked up in a logical name table, the suffix after the semi-colon is treated as the translation index to be used for the lookup. This lets you look up successive values for search list logical names. For instance, if you say </p>
<pre><code>   $ Define STORY once,upon,a,time,there,was
   $ perl -e &quot;for ($i = 0; $i &lt;= 6; $i++) &quot; -
   _$ -e &quot;{ print $ENV{'story;'.$i},' '}&quot;
</code></pre>
<p> Perl will print <code>&quot;ONCE UPON A TIME THERE WAS&quot;</code>, assuming, of course, that <i></i><font SIZE="-1"><i>PERL_ENV_TABLES</i></font><i></i> is set up so that the logical name <code>&quot;story&quot;</code> is found, rather than a <font SIZE="-1">CLI</font> symbol or <font SIZE="-1">CRTL</font> <code>&quot;environ&quot;</code> element with the same name. </p>
<p> When an element of <code>%ENV</code> is set to a defined string, the corresponding definition is made in the location to which the first translation of <i></i><font SIZE="-1"><i>PERL_ENV_TABLES</i></font><i></i> points. If this causes a logical name to be created, it is defined in supervisor mode. (The same is done if an existing logical name was defined in executive or kernel mode; an existing user or supervisor mode logical name is reset to the new value.) If the value is an empty string, the logical name&#8217;s translation is defined as a single <code>&quot;NUL&quot;</code> (<font SIZE="-1">ASCII</font> <code>&quot;\0&quot;</code>) character, since a logical name cannot translate to a zero-length string. (This restriction does not apply to <font SIZE="-1">CLI</font> symbols or <font SIZE="-1">CRTL</font> <code>&quot;environ&quot;</code> values; they are set to the empty string.) </p>
<p> When an element of <code>%ENV</code> is set to <code>&quot;undef&quot;</code>, the element is looked up as if it were being read, and if it is found, it is deleted. (An item ``deleted&#8217;&#8216; from the <font SIZE="-1">CRTL</font> <code>&quot;environ&quot;</code> array is set to the empty string.) Using <code>&quot;delete&quot;</code> to remove an element from <code>%ENV</code> has a similar effect, but after the element is deleted, another attempt is made to look up the element, so an inner-mode logical name or a name in another location will replace the logical name just deleted. In either case, only the first value found searching <font SIZE="-1">PERL_ENV_TABLES</font> is altered. It is not possible at present to define a search list logical name via <code>%ENV</code>. </p>
<p> The element <code>$ENV{DEFAULT}</code> is special: when read, it returns Perl&#8217;s current default device and directory, and when set, it resets them, regardless of the definition of <i></i><font SIZE="-1"><i>PERL_ENV_TABLES</i></font><i></i>. It cannot be cleared or deleted; attempts to do so are silently ignored. </p>
<p> Note that if you want to pass on any elements of the C-local environ array to a subprocess which isn&#8217;t started by fork/exec, or isn&#8217;t running a C program, you can ``promote&#8217;&#8216; them to logical names in the current process, which will then be inherited by all subprocesses, by saying </p>
<pre><code>    foreach my $key (qw[C-local keys you want promoted]) {
        my $temp = $ENV{$key}; # read from C-local array
        $ENV{$key} = $temp; # and define as logical name
    }
</code></pre>
<p> (You can&#8217;t just say <code>$ENV{$key} = $ENV{$key}</code>, since the Perl optimizer is smart enough to elide the expression.) </p>
<p> Don&#8217;t try to clear <code>%ENV</code> by saying <code>&quot;%ENV = ();&quot;</code>, it will throw a fatal error. This is equivalent to doing the following from <font SIZE="-1">DCL:</font> </p>
<pre><code>    DELETE/LOGICAL *
</code></pre>
<p> You can imagine how bad things would be if, for example, the <font SIZE="-1">SYS$MANAGER</font> or <font SIZE="-1">SYS$SYSTEM</font> logical names were deleted. </p>
<p> At present, the first time you iterate over <code>%ENV</code> using <code>&quot;keys&quot;</code>, or <code>&quot;values&quot;</code>, you will incur a time penalty as all logical names are read, in order to fully populate <code>%ENV</code>. Subsequent iterations will not reread logical names, so they won&#8217;t be as slow, but they also won&#8217;t reflect any changes to logical name tables caused by other programs. </p>
<p> You do need to be careful with the logical names representing process-permanent files, such as <code>&quot;SYS$INPUT&quot;</code> and <code>&quot;SYS$OUTPUT&quot;</code>. The translations for these logical names are prepended with a two-byte binary value (0x1B 0x00) that needs to be stripped off if you want to use it. (In previous versions of Perl it wasn&#8217;t possible to get the values of these logical names, as the null byte acted as an end-of-string marker) </p>
 </dd></dl>
<dt>$!</dt>
<dd> <p> The string value of <code>$!</code> is that returned by the <font SIZE="-1">CRTL</font>&#8216;s <code>strerror()</code> function, so it will include the <font SIZE="-1">VMS</font> message for VMS-specific errors. The numeric value of <code>$!</code> is the value of <code>&quot;errno&quot;</code>, except if errno is <font SIZE="-1">EVMSERR,</font> in which case <code>$!</code> contains the value of vaxc$errno. Setting <code>$!</code> always sets errno to the value specified. If this value is <font SIZE="-1">EVMSERR,</font> it also sets vaxc$errno to 4 (NONAME-F-NOMSG), so that the string value of <code>$!</code> won&#8217;t reflect the <font SIZE="-1">VMS</font> error message from before <code>$!</code> was set. </p>
 </dd>
<dt>$^E</dt>
<dd> <p> This variable provides direct access to <font SIZE="-1">VMS</font> status values in vaxc$errno, which are often more specific than the generic Unix-style error messages in <code>$!</code>. Its numeric value is the value of vaxc$errno, and its string value is the corresponding <font SIZE="-1">VMS</font> message string, as retrieved by sys$<code>getmsg()</code>. Setting <code>$^E</code> sets vaxc$errno to the value specified. </p>
<p> While Perl attempts to keep the vaxc$errno value to be current, if errno is not <font SIZE="-1">EVMSERR,</font> it may not be from the current operation. </p>
 </dd>
<dt>$?</dt>
<dd> <p> The ``status value&#8217;&#8216; returned in <code>$?</code> is synthesized from the actual exit status of the subprocess in a way that approximates <font SIZE="-1">POSIX</font> <code>wait</code>(5) semantics, in order to allow Perl programs to portably test for successful completion of subprocesses. The low order 8 bits of <code>$?</code> are always 0 under <font SIZE="-1">VMS,</font> since the termination status of a process may or may not have been generated by an exception. </p>
<p> The next 8 bits contain the termination status of the program. </p>
<p> If the child process follows the convention of C programs compiled with the _POSIX_EXIT macro set, the status value will contain the actual value of 0 to 255 returned by that program on a normal exit. </p>
<p> With the _POSIX_EXIT macro set, the Unix exit value of zero is represented as a <font SIZE="-1">VMS</font> native status of 1, and the Unix values from 2 to 255 are encoded by the equation: </p>
<pre><code>   VMS_status = 0x35a000 + (unix_value * 8) + 1.
</code></pre>
<p> And in the special case of Unix value 1 the encoding is: </p>
<pre><code>   VMS_status = 0x35a000 + 8 + 2 + 0x10000000.
</code></pre>
<p> For other termination statuses, the severity portion of the subprocess&#8217;s exit status is used: if the severity was success or informational, these bits are all 0; if the severity was warning, they contain a value of 1; if the severity was error or fatal error, they contain the actual severity bits, which turns out to be a value of 2 for error and 4 for severe_error. Fatal is another term for the severe_error status. </p>
<p> As a result, <code>$?</code> will always be zero if the subprocess&#8217;s exit status indicated successful completion, and non-zero if a warning or error occurred or a program compliant with encoding _POSIX_EXIT values was run and set a status. </p>
<p> How can you tell the difference between a non-zero status that is the result of a <font SIZE="-1">VMS</font> native error status or an encoded Unix status? You can not unless you look at the ${^CHILD_ERROR_NATIVE} value. The ${^CHILD_ERROR_NATIVE} value returns the actual <font SIZE="-1">VMS</font> status value and check the severity bits. If the severity bits are equal to 1, then if the numeric value for <code>$?</code> is between 2 and 255 or 0, then <code>$?</code> accurately reflects a value passed back from a Unix application. If <code>$?</code> is 1, and the severity bits indicate a <font SIZE="-1">VMS</font> error (2), then <code>$?</code> is from a Unix application exit value. </p>
<p> In practice, Perl scripts that call programs that return _POSIX_EXIT type status values will be expecting those values, and programs that call traditional <font SIZE="-1">VMS</font> programs will either be expecting the previous behavior or just checking for a non-zero status. </p>
<p> And success is always the value 0 in all behaviors. </p>
<p> When the actual <font SIZE="-1">VMS</font> termination status of the child is an error, internally the <code>$!</code> value will be set to the closest Unix errno value to that error so that Perl scripts that test for error messages will see the expected Unix style error message instead of a <font SIZE="-1">VMS</font> message. </p>
<p> Conversely, when setting <code>$?</code> in an <font SIZE="-1">END</font> block, an attempt is made to convert the <font SIZE="-1">POSIX</font> value into a native status intelligible to the operating system upon exiting Perl. What this boils down to is that setting <code>$?</code> to zero results in the generic success value <font SIZE="-1">SS$_NORMAL,</font> and setting <code>$?</code> to a non-zero value results in the generic failure status <font SIZE="-1">SS$_ABORT.</font> See also ``exit&#8217;&#8216; in perlport. </p>
<p> With the <code>&quot;PERL_VMS_POSIX_EXIT&quot;</code> logical name defined as ``<font SIZE="-1">ENABLE&#8217;&#8216;,</font> setting <code>$?</code> will cause the new value to be encoded into <code>$^E</code> so that either the original parent or child exit status values <br />
&nbsp;0 to 255 can be automatically recovered by C programs expecting _POSIX_EXIT behavior. If both a parent and a child exit value are non-zero, then it will be assumed that this is actually a <font SIZE="-1">VMS</font> native status value to be passed through. The special value of 0xFFFF is almost a <font SIZE="-1">NOOP</font> as it will cause the current native <font SIZE="-1">VMS</font> status in the C library to become the current native Perl <font SIZE="-1">VMS</font> status, and is handled this way as it is known to not be a valid native <font SIZE="-1">VMS</font> status value. It is recommend that only values in the range of normal Unix parent or child status numbers, 0 to 255 are used. </p>
<p> The pragma <code>&quot;use vmsish &#8216;status&#8217;&quot;</code> makes <code>$?</code> reflect the actual <font SIZE="-1">VMS</font> exit status instead of the default emulation of <font SIZE="-1">POSIX</font> status described above. This pragma also disables the conversion of non-zero values to <font SIZE="-1">SS$_ABORT</font> when setting <code>$?</code> in an <font SIZE="-1">END</font> block (but zero will still be converted to <font SIZE="-1">SS$_NORMAL</font>). </p>
<p> Do not use the pragma <code>&quot;use vmsish &#8216;status&#8217;&quot;</code> with <code>&quot;PERL_VMS_POSIX_EXIT&quot;</code> enabled, as they are at times requesting conflicting actions and the consequence of ignoring this advice will be undefined to allow future improvements in the <font SIZE="-1">POSIX</font> exit handling. </p>
<p> In general, with <code>&quot;PERL_VMS_POSIX_EXIT&quot;</code> enabled, more detailed information will be available in the exit status for <font SIZE="-1">DCL</font> scripts or other native <font SIZE="-1">VMS</font> tools, and will give the expected information for Posix programs. It has not been made the default in order to preserve backward compatibility. </p>
<p> N.B. Setting <code>&quot;DECC$FILENAME_UNIX_REPORT&quot;</code> implicitly enables <code>&quot;PERL_VMS_POSIX_EXIT&quot;</code>. </p>
 </dd>
<dt>$|</dt>
<dd> <p> Setting <code>$|</code> for an I/O stream causes data to be flushed all the way to disk on each write (<i>i.e.</i> not just to the underlying <font SIZE="-1">RMS</font> buffers for a file). In other words, it&#8217;s equivalent to calling <code>fflush()</code> and <code>fsync()</code> from C. </p>
 </dd></dl>
<h2>Standard modules with VMS-specific differences</h2>
<h3>SDBM_File</h3>
<p> SDBM_File works properly on <font SIZE="-1">VMS.</font> It has, however, one minor difference. The database directory file created has a <i>.sdbm_dir</i> extension rather than a <i>.dir</i> extension. <i>.dir</i> files are <font SIZE="-1">VMS</font> filesystem directory files, and using them for other purposes could cause unacceptable problems.  </p>
<h2>Revision date</h2>
<p> Please see the git repository for revision history.  </p>
<h2>AUTHOR</h2>
<p> Charles Bailey bailey [at] cor.newman.upenn.edu Craig Berry craigberry [at] mac.com Dan Sugalski dan [at] sidhe.org John Malmberg wb8tyw [at] qsl.net </p>
