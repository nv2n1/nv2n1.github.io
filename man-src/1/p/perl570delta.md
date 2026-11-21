---
title: "perl570delta(1)"
name: "perl570delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl570delta/"
description: "perl570delta – what’s new for perl v5.7.0"
---
<h2 class="name">NAME</h2>
<p> perl570delta - what&#8217;s new for perl v5.7.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.6.0 release and the 5.7.0 release.  </p>
<h2>Security Vulnerability Closed</h2>
<p> A potential security vulnerability in the optional suidperl component of Perl has been identified. suidperl is neither built nor installed by default. As of September the 2nd, 2000, the only known vulnerable platform is Linux, most likely all Linux distributions. <font SIZE="-1">CERT</font> and various vendors have been alerted about the vulnerability. </p>
<p> The problem was caused by Perl trying to report a suspected security exploit attempt using an external program, /bin/mail. On Linux platforms the /bin/mail program had an undocumented feature which when combined with suidperl gave access to a root shell, resulting in a serious compromise instead of reporting the exploit attempt. If you don&#8217;t have /bin/mail, or if you have &#8216;safe setuid scripts&#8217;, or if suidperl is not installed, you are safe. </p>
<p> The exploit attempt reporting feature has been completely removed from the Perl 5.7.0 release, so that particular vulnerability isn&#8217;t there anymore. However, further security vulnerabilities are, unfortunately, always possible. The suidperl code is being reviewed and if deemed too risky to continue to be supported, it may be completely removed from future releases. In any case, suidperl should only be used by security experts who know exactly what they are doing and why they are using suidperl instead of some other solution such as sudo ( see <a rel="nofollow" href="http://www.courtesan.com/sudo/">http://www.courtesan.com/sudo/</a> ).  </p>
<h2>Incompatible Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Arrays now always interpolate into double-quoted strings: constructs like ``foo@bar&#8217;&#8216; now always assume <code>@bar</code> is an array, whether or not the compiler has seen use of <code>@bar</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The semantics of bless(<font SIZE="-1">REF</font>, <font SIZE="-1">REF</font>) were unclear and until someone proves it to make some sense, it is forbidden. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A reference to a reference now stringify as ``<font SIZE="-1">REF</font>(0x81485ec)&#8216;&#8216; instead of ``<font SIZE="-1">SCALAR</font>(0x81485ec)&#8216;&#8216; in order to be more consistent with the return value of <i>ref()</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The very dusty examples in the eg/ directory have been removed. Suggestions for new shiny examples welcome but the main issue is that the examples need to be documented, tested and (most importantly) maintained. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The obsolete chat2 library that should never have been allowed to escape the laboratory has been decommissioned. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The unimplemented <font SIZE="-1">POSIX</font> regex features [[.cc.]] and [[=c=]] are still recognised but now cause fatal errors. The previous behaviour of ignoring them by default and warning if requested was unacceptable since it, in a way, falsely promised that the features could be used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The (bogus) escape sequences \8 and \9 now give an optional warning (``Unrecognized escape passed through&#8217;&#8216;). There is no need to \-escape any <code>&quot;\w&quot;</code> character. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> lstat(<font SIZE="-1">FILEHANDLE</font>) now gives a warning because the operation makes no sense. In future releases this may become a fatal error. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The long deprecated uppercase aliases for the string comparison operators (<font SIZE="-1">EQ</font>, <font SIZE="-1">NE</font>, <font SIZE="-1">LT</font>, <font SIZE="-1">LE</font>, <font SIZE="-1">GE</font>, <font SIZE="-1">GT</font>) have now been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The regular expression captured submatches ($1, <code>$2</code>, ...) are now more consistently unset if the match fails, instead of leaving false data lying around in them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The tr///C and tr///U features have been removed and will not return; the interface was a mistake. Sorry about that. For similar functionality, see pack(&#8216;U0&#8217;, ...) and pack(&#8216;C0&#8217;, ...). </p>
 </dd></dl>
<h2>Core Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;perl -d:Module=arg,arg,arg&quot;</code> now works (previously one couldn&#8217;t pass in multiple arguments.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> my __PACKAGE__ <code>$obj</code> now works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;no Module;&quot;</code> now works even if there is no ``sub unimport&#8217;&#8216; in the Module. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The numerical comparison operators return <code>&quot;undef&quot;</code> if either operand is a NaN. Previously the behaviour was unspecified. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pack(&#8216;U0a*&#8216;, ...)&quot;</code> can now be used to force a string to <font SIZE="-1">UTF-8</font>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> prototype(\&amp;) is now available. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> There is now an <font SIZE="-1">UNTIE</font> method. </p>
 </dd></dl>
<h2>Modules and Pragmata</h2>
<h3>New Modules</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> File::Temp allows one to create temporary files and directories in an easy, portable, and secure way. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Storable gives persistence to Perl data structures by allowing the storage and retrieval of Perl data to and from files in a fast and compact binary format. </p>
 </dd></dl>
<h3>Updated And Improved Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The following independently supported modules have been updated to newer versions from <font SIZE="-1">CPAN:</font> <font SIZE="-1">CGI</font>, <font SIZE="-1">CPAN</font>, DB_File, File::Spec, Getopt::Long, the podlators bundle, Pod::LaTeX, Pod::Parser, Term::ANSIColor, Test. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Bug fixes and minor enhancements have been applied to B::Deparse, Data::Dumper, IO::Poll, IO::Socket::INET, Math::BigFloat, Math::Complex, Math::Trig, Net::protoent, the re pragma, SelfLoader, Sys::SysLog, Test::Harness, Text::Wrap, <font SIZE="-1">UNIVERSAL</font>, and the warnings pragma. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <i>attributes::reftype()</i> now works on tied arguments. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> AutoLoader can now be disabled with <code>&quot;no AutoLoader;&quot;</code>, </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The English module can now be used without the infamous performance hit by saying </p>
<pre><code>        use English '-no_performance_hit';
</code></pre>
<p> (Assuming, of course, that one doesn&#8217;t need the troublesome variables <code>&quot;$`&quot;</code>, <code>$&amp;</code>, or <code>&quot;$&#8216;&quot;</code>.) Also, introduced <code>@LAST_MATCH_START</code> and <code>@LAST_MATCH_END</code> English aliases for <code>&quot;@-&quot;</code> and <code>&quot;@+&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Find now has pre- and post-processing callbacks. It also correctly changes directories when chasing symbolic links. Callbacks (naughtily) exiting with ``next;&#8216;&#8216; instead of ``return;&#8216;&#8216; now work. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>File::Glob::glob()</i> renamed to <i>File::Glob::bsd_glob()</i> to avoid prototype mismatch with <i>CORE::glob()</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::Open3 now allows the use of numeric file descriptors. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> use lib now works identically to <code>@INC</code>. Removing directories with &#8216;no lib&#8217; now works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>%INC</code> now localised in a Safe compartment so that use/require work. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Shell module now has an <font SIZE="-1">OO</font> interface. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The Emacs perl mode (emacs/cperl-mode.el) has been updated to version 4.31. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perlbug is now much more robust. It also sends the bug report to perl.org, not perl.com. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The perlcc utility has been rewritten and its user interface (that is, command line) is much more like that of the Unix C compiler, cc. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The xsubpp utility for extension writers now understands <font SIZE="-1">POD</font> documentation embedded in the *.xs files. </p>
 </dd></dl>
<h2>New Documentation</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> perl56delta details the changes between the 5.005 release and the 5.6.0 release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perldebtut is a Perl debugging tutorial. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlebcdic contains considerations for running Perl on <font SIZE="-1">EBCDIC</font> platforms. Note that unfortunately <font SIZE="-1">EBCDIC</font> platforms that used to supported back in Perl 5.005 are still unsupported by Perl 5.7.0; the plan, however, is to bring them back to the fold. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlnewmod tells about writing and submitting a new module. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlposix-bc explains using Perl on the POSIX-BC platform (an <font SIZE="-1">EBCDIC</font> mainframe platform). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlretut is a regular expression tutorial. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlrequick is a regular expressions quick-start guide. Yes, much quicker than perlretut. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlutil explains the command line utilities packaged with the Perl distribution. </p>
 </dd></dl>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <i>map()</i> that changes the size of the list should now work faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>sort()</i> has been changed to use mergesort internally as opposed to the earlier quicksort. For very small lists this may result in slightly slower sorting times, but in general the speedup should be at least 20%. Additional bonuses are that the worst case behaviour of <i>sort()</i> is now better (in computer science terms it now runs in time O(N log N), as opposed to quicksort&#8217;s Theta(N**2) worst-case run time behaviour), and that <i>sort()</i> is now stable (meaning that elements with identical keys will stay ordered as they were before the sort). </p>
 </dd></dl>
<h2>Installation and Configuration Improvements</h2>
<h3>Generic Improvements</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">INSTALL</font> now explains how you can configure Perl to use 64-bit integers even on non-64-bit platforms. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Policy.sh policy change: if you are reusing a Policy.sh file (see <font SIZE="-1">INSTALL</font>) and you use Configure -Dprefix=/foo/bar and in the old Policy <code>$prefix</code> eq <code>$siteprefix</code> and <code>$prefix</code> eq <code>$vendorprefix</code>, all of them will now be changed to the new prefix, /foo/bar. (Previously only <code>$prefix</code> changed.) If you do not like this new behaviour, specify prefix, siteprefix, and vendorprefix explicitly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new optional location for Perl libraries, otherlibdirs, is available. It can be used for example for vendor add-ons without disturbing Perl&#8217;s own library directories. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In many platforms the vendor-supplied &#8216;cc&#8217; is too stripped-down to build Perl (basically, &#8216;cc&#8217; doesn&#8217;t do <font SIZE="-1">ANSI</font> C). If this seems to be the case and &#8216;cc&#8217; does not seem to be the <font SIZE="-1">GNU</font> C compiler &#8216;gcc&#8217;, an automatic attempt is made to find and use &#8216;gcc&#8217; instead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> gcc needs to closely track the operating system release to avoid build problems. If Configure finds that gcc was built for a different operating system release than is running, it now gives a clearly visible warning that there may be trouble ahead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If binary compatibility with the 5.005 release is not wanted, Configure no longer suggests including the 5.005 modules in <code>@INC</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Configure <code>&quot;-S&quot;</code> can now run non-interactively. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> configure.gnu now works with options with whitespace in them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> installperl now outputs everything to <font SIZE="-1">STDERR</font>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$Config</code>{byteorder} is now computed dynamically (this is more robust with ``fat binaries&#8217;&#8216; where an executable image contains binaries for more than one binary platform.) </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Several debugger fixes: exit code now reflects the script exit code, condition <code>&quot;0&quot;</code> now treated correctly, the <code>&quot;d&quot;</code> command now checks line number, the <code>$.</code> no longer gets corrupted, all debugger output now goes correctly to the socket if RemotePort is set. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>*foo{FORMAT}</code> now works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Lexical warnings now propagating correctly between scopes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Line renumbering with eval and <code>&quot;#line&quot;</code> now works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed numerous memory leaks, especially in eval &quot;&quot;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Modulus of unsigned numbers now works (4063328477 % 65535 used to return 27406, instead of 27047). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some ``not a number&#8217;&#8216; warnings introduced in 5.6.0 eliminated to be more compatible with 5.005. Infinity is now recognised as a number. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>our()</i> variables will not cause ``will not stay shared&#8217;&#8216; warnings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> pack ``Z&#8217;&#8216; now correctly terminates the string with ``\0&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix password routines which in some shadow password platforms (e.g. HP-UX) caused <i>getpwent()</i> to return every other entry. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>printf()</i> no longer resets the numeric locale to ``C&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;q(a\\b)&quot;</code> now parses correctly as <code>&#8216;a\\b&#8217;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Printing quads (64-bit integers) with printf/sprintf now works without the q L ll prefixes (assuming you are on a quad-capable platform). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regular expressions on references and overloaded scalars now work. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>scalar()</i> now forces scalar context even when used in void context. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>sort()</i> arguments are now compiled in the right wantarray context (they were accidentally using the context of the <i>sort()</i> itself). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changed the <font SIZE="-1">POSIX</font> character class <code>&quot;[[:space:]]&quot;</code> to include the (very rare) vertical tab character. Added a new POSIX-ish character class <code>&quot;[[:blank:]]&quot;</code> which stands for horizontal whitespace (currently, the space and the tab). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$AUTOLOAD</code>, <i>sort()</i>, <i>lock()</i>, and spawning subprocesses in multiple threads simultaneously are now thread-safe. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Allow read-only string on left hand side of non-modifying tr///. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several Unicode fixes (but still not perfect). </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> BOMs (byte order marks) in the beginning of Perl files (scripts, modules) should now be transparently skipped. <font SIZE="-1">UTF-16</font> (<font SIZE="-1">UCS-2</font>) encoded Perl files should now be read correctly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The character tables have been updated to Unicode 3.0.1. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>chr()</i> for values greater than 127 now create utf8 when under use utf8. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Comparing with utf8 data does not magically upgrade non-utf8 data into utf8. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;IsAlnum&quot;</code>, <code>&quot;IsAlpha&quot;</code>, and <code>&quot;IsWord&quot;</code> now match titlecase. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Concatenation with the <code>&quot;.&quot;</code> operator or via variable interpolation, <code>&quot;eq&quot;</code>, <code>&quot;substr&quot;</code>, <code>&quot;reverse&quot;</code>, <code>&quot;quotemeta&quot;</code>, the <code>&quot;x&quot;</code> operator, substitution with <code>&quot;s///&quot;</code>, single-quoted <font SIZE="-1">UTF-8</font>, should now work---in theory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;tr///&quot;</code> operator now works <i>slightly</i> better but is still rather broken. Note that the <code>&quot;tr///CU&quot;</code> functionality has been removed (but see pack(&#8216;U0&#8217;, ...)). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>vec()</i> now refuses to deal with characters &gt;255. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Zero entries were missing from the Unicode classes like <code>&quot;IsDigit&quot;</code>. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> UNIVERSAL::isa no longer caches methods incorrectly. (This broke the Tk extension with 5.6.0.) </p>
 </dd></dl>
<h3>Platform Specific Changes and Fixes</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">BSDI</font> 4.* </p>
<p> Perl now works on post-4.0 BSD/OSes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> All BSDs </p>
<p> Setting <code>$0</code> now works (as much as possible; see perlvar for details). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Cygwin </p>
<p> Numerous updates; currently synchronised with Cygwin 1.1.4. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">EPOC</font> </p>
<p> <font SIZE="-1">EPOC</font> update after Perl 5.6.0. See <font SIZE="-1">README</font>.epoc. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> FreeBSD 3.* </p>
<p> Perl now works on post-3.0 FreeBSDs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> HP-UX </p>
<p> <font SIZE="-1">README</font>.hpux updated; <code>&quot;Configure -Duse64bitall&quot;</code> now almost works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">IRIX</font> </p>
<p> Numerous compilation flag and hint enhancements; accidental mixing of 32-bit and 64-bit libraries (a doomed attempt) made much harder. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Linux </p>
<p> Long doubles should now work (see <font SIZE="-1">INSTALL</font>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Mac <font SIZE="-1">OS</font> Classic </p>
<p> Compilation of the standard Perl distribution in Mac <font SIZE="-1">OS</font> Classic should now work if you have the Metrowerks development environment and the missing Mac-specific toolkit bits. Contact the macperl mailing list for details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> MPE/iX </p>
<p> MPE/iX update after Perl 5.6.0. See <font SIZE="-1">README</font>.mpeix. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> NetBSD/sparc </p>
<p> Perl now works on NetBSD/sparc. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">OS/2</font> </p>
<p> Now works with usethreads (see <font SIZE="-1">INSTALL</font>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Solaris </p>
<p> 64-bitness using the Sun Workshop compiler now works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tru64 (aka Digital <font SIZE="-1">UNIX</font>, aka <font SIZE="-1">DEC</font> <font SIZE="-1">OSF/1</font>) </p>
<p> The operating system version letter now recorded in <code>$Config</code>{osvers}. Allow compiling with gcc (previously explicitly forbidden). Compiling with gcc still not recommended because buggy code results, even with gcc 2.95.2. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicos </p>
<p> Fixed various alignment problems that lead into core dumps either during build or later; no longer dies on math errors at runtime; now using full quad integers (64 bits), previously was using only 46 bit integers for speed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">VMS</font> </p>
<p> <i>chdir()</i> now works better despite a <font SIZE="-1">CRT</font> bug; now works with <font SIZE="-1">MULTIPLICITY</font> (see <font SIZE="-1">INSTALL</font>); now works with Perl&#8217;s malloc. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Windows </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> <i>accept()</i> no longer leaks memory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Better <i>chdir()</i> return value for a non-existent directory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> New <code>%ENV</code> entries now propagate to subprocesses. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$ENV</code>{<font SIZE="-1">LIB</font>} now used to search for libs under Visual C. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A failed (pseudo)fork now returns undef and sets errno to <font SIZE="-1">EAGAIN</font>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Allow <font SIZE="-1">REG_EXPAND_SZ</font> keys in the registry. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can now <i>send()</i> from all threads, not just the first one. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fake signal handling reenabled, bugs and all. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Less stack reserved per thread so that more threads can run concurrently. (Still 16M per thread.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;File::Spec-&gt;tmpdir()&quot;</code> now prefers C:/temp over /tmp (works better when perl is running as service). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Better <font SIZE="-1">UNC</font> path handling under ithreads. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>wait()</i> and <i>waitpid()</i> now work much better. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> winsock handle leak fixed. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>New or Changed Diagnostics</h2>
<p> All regular expression compilation error messages are now hopefully easier to understand both because the error message now comes before the failed regex and because the point of failure is now clearly marked. </p>
<p> The various ``opened only for&#8217;&#8216;, ``on closed&#8217;&#8216;, ``never opened&#8217;&#8216; warnings drop the <code>&quot;main::&quot;</code> prefix for filehandles in the <code>&quot;main&quot;</code> package, for example <code>&quot;STDIN&quot;</code> instead of &lt;main::STDIN&gt;. </p>
<p> The ``Unrecognized escape&#8217;&#8216; warning has been extended to include <code>&quot;\8&quot;</code>, <code>&quot;\9&quot;</code>, and <code>&quot;\_&quot;</code>. There is no need to escape any of the <code>&quot;\w&quot;</code> characters.  </p>
<h2>Changed Internals</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> perlapi.pod (a companion to perlguts) now attempts to document the internal <font SIZE="-1">API</font>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> You can now build a really minimal perl called microperl. Building microperl does not require even running Configure; <code>&quot;make -f Makefile.micro&quot;</code> should be enough. Beware: microperl makes many assumptions, some of which may be too bold; the resulting executable may crash or otherwise misbehave in wondrous ways. For careful hackers only. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Added <i>rsignal()</i>, <i>whichsig()</i>, <i>do_join()</i> to the publicised <font SIZE="-1">API</font>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Made possible to propagate customised exceptions via <i>croak()</i>ing. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Added <i>is_utf8_char()</i>, <i>is_utf8_string()</i>, <i>bytes_to_utf8()</i>, and <i>utf8_to_bytes()</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Now xsubs can have attributes just like subs. </p>
 </dd></dl>
<h2>Known Problems</h2>
<h3>Unicode Support Still Far From Perfect</h3>
<p> We&#8217;re working on it. Stay tuned.  </p>
<font SIZE="-1"></font><h3>EBCDIC Still A Lost Platform</h3>
<p> The plan is to bring them back.  </p>
<h3>Building Extensions Can Fail Because Of Largefiles</h3>
<p> Certain extensions like mod_perl and BSD::Resource are known to have issues with `largefiles&#8217;, a change brought by Perl 5.6.0 in which file offsets default to 64 bits wide, where supported. Modules may fail to compile at all or compile and work incorrectly. Currently there is no good solution for the problem, but Configure now provides appropriate non-largefile ccflags, ldflags, libswanted, and libs in the <code>%Config</code> hash (e.g., <code>$Config</code>{ccflags_nolargefiles}) so the extensions that are having problems can try configuring themselves without the largefileness. This is admittedly not a clean solution, and the solution may not even work at all. One potential failure is whether one can (or, if one can, whether it&#8217;s a good idea) link together at all binaries with different ideas about file offsets, all this is platform-dependent.  </p>
<h3>ftmp-security tests warn 'system possibly insecure'</h3>
<p> Don&#8217;t panic. Read <font SIZE="-1">INSTALL</font> &#8216;make test&#8217; section instead.  </p>
<h3>Test lib/posix Subtest 9 Fails In LP64-Configured HP-UX</h3>
<p> If perl is configured with -Duse64bitall, the successful result of the subtest 10 of lib/posix may arrive before the successful result of the subtest 9, which confuses the test harness so much that it thinks the subtest 9 failed.  </p>
<h3>Long Doubles Still Don't Work In Solaris</h3>
<p> The experimental long double support is still very much so in Solaris. (Other platforms like Linux and Tru64 are beginning to solidify in this area.)  </p>
<h3>Linux With Sfio Fails op/misc Test 48</h3>
<p> No known fix.  </p>
<h3>Storable tests fail in some platforms</h3>
<p> If any Storable tests fail the use of Storable is not advisable. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Many Storable tests fail on <font SIZE="-1">AIX</font> configured with 64 bit integers. </p>
<p> So far unidentified problems break Storable in <font SIZE="-1">AIX</font> if Perl is configured to use 64 bit integers. <font SIZE="-1">AIX</font> in 32-bit mode works and other 64-bit platforms work with Storable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">DOS</font> <font SIZE="-1">DJGPP</font> may hang when testing Storable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> st-06compat fails in <font SIZE="-1">UNICOS</font> and UNICOS/mk. </p>
<p> This means that you cannot read old (pre-Storable-0.7) Storable images made in other platforms. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> st-store.t and st-retrieve may fail with Compaq C 6.2 on OpenVMS Alpha 7.2. </p>
 </dd></dl>
<h3>Threads Are Still Experimental</h3>
<p> Multithreading is still an experimental feature. Some platforms emit the following message for lib/thr5005 </p>
<pre><code>    #
    # This is a KNOWN FAILURE, and one of the reasons why threading
    # is still an experimental feature. It is here to stop people
    # from deploying threads in production. ;-)
    #
</code></pre>
<p> and another known thread-related warning is </p>
<pre><code>   pragma/overload......Unbalanced saves: 3 more saves than restores
   panic: magic_mutexfree during global destruction.
   ok
   lib/selfloader.......Unbalanced saves: 3 more saves than restores
   panic: magic_mutexfree during global destruction.
   ok
   lib/st-dclone........Unbalanced saves: 3 more saves than restores
   panic: magic_mutexfree during global destruction.
   ok
</code></pre>
<h3>The Compiler Suite Is Still Experimental</h3>
<p> The compiler suite is slowly getting better but is nowhere near working order yet. The backend part that has seen perhaps the most progress is the bytecode compiler.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a> There may also be information at <a rel="nofollow" href="http://www.perl.com/perl/">http://www.perl.com/perl/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information.  </p>
<h2>HISTORY</h2>
<p> Written by Jarkko Hietaniemi &lt;<i>jhi [at] iki.fi</i>&gt;, with many contributions from The Perl Porters and Perl Users submitting feedback and patches. </p>
<p> Send omissions or corrections to &lt;<i>perlbug [at] perl.org</i>&gt;. </p>
