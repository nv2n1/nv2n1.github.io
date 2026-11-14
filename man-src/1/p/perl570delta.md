---
title: "perl570delta(1)"
name: "perl570delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl570delta/"
description: "perl570delta – what’s new for perl v5.7.0"
---

<h2 class="name">NAME</h2>
<p> perl570delta &#8211; what&#8217;s new for perl v5.7.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.6.0 release and the 5.7.0 release.</p>
<h2>Security Vulnerability Closed</h2>
<p> A potential security vulnerability in the optional suidperl component of Perl has been identified. suidperl is neither built nor installed by default. As of September the 2nd, 2000, the only known vulnerable platform is Linux, most likely all Linux distributions. <font SIZE="-1">CERT</font> and various vendors have been alerted about the vulnerability. </p>
<p> The problem was caused by Perl trying to report a suspected security exploit attempt using an external program, /bin/mail. On Linux platforms the /bin/mail program had an undocumented feature which when combined with suidperl gave access to a root shell, resulting in a serious compromise instead of reporting the exploit attempt. If you don&#8217;t have /bin/mail, or if you have &#8216;safe setuid scripts&#8217;, or if suidperl is not installed, you are safe. </p>
<p> The exploit attempt reporting feature has been completely removed from the Perl 5.7.0 release, so that particular vulnerability isn&#8217;t there anymore. However, further security vulnerabilities are, unfortunately, always possible. The suidperl code is being reviewed and if deemed too risky to continue to be supported, it may be completely removed from future releases. In any case, suidperl should only be used by security experts who know exactly what they are doing and why they are using suidperl instead of some other solution such as sudo ( see <a rel="nofollow" href="http://www.courtesan.com/sudo/">http://www.courtesan.com/sudo/</a> ).</p>
<h2>Incompatible Changes</h2>
<dl>
<dt>&bull;</p>
<dd> Arrays now always interpolate into double-quoted strings: constructs like &#8220;foo@bar&#8221; now always assume <tt>@bar</tt> is an array, whether or not the compiler has seen use of <tt>@bar</tt>.</p>
<dt>&bull;</p>
<dd> The semantics of bless(<font SIZE="-1">REF</font>, <font SIZE="-1">REF</font>) were unclear and until someone proves it to make some sense, it is forbidden.</p>
<dt>&bull;</p>
<dd> A reference to a reference now stringify as &#8220;<font SIZE="-1">REF</font>(0x81485ec)&#8221; instead of &#8220;<font SIZE="-1">SCALAR</font>(0x81485ec)&#8221; in order to be more consistent with the return value of <i>ref()</i>.</p>
<dt>&bull;</p>
<dd> The very dusty examples in the eg/ directory have been removed. Suggestions for new shiny examples welcome but the main issue is that the examples need to be documented, tested and (most importantly) maintained.</p>
<dt>&bull;</p>
<dd> The obsolete chat2 library that should never have been allowed to escape the laboratory has been decommissioned.</p>
<dt>&bull;</p>
<dd> The unimplemented <font SIZE="-1">POSIX</font> regex features [[.cc.]] and [[=c=]] are still recognised but now cause fatal errors. The previous behaviour of ignoring them by default and warning if requested was unacceptable since it, in a way, falsely promised that the features could be used.</p>
<dt>&bull;</p>
<dd> The (bogus) escape sequences \8 and \9 now give an optional warning (&#8220;Unrecognized escape passed through&#8221;). There is no need to \-escape any <tt>&quot;\w&quot;</tt> character.</p>
<dt>&bull;</p>
<dd> lstat(<font SIZE="-1">FILEHANDLE</font>) now gives a warning because the operation makes no sense. In future releases this may become a fatal error.</p>
<dt>&bull;</p>
<dd> The long deprecated uppercase aliases for the string comparison operators (<font SIZE="-1">EQ</font>, <font SIZE="-1">NE</font>, <font SIZE="-1">LT</font>, <font SIZE="-1">LE</font>, <font SIZE="-1">GE</font>, <font SIZE="-1">GT</font>) have now been removed.</p>
<dt>&bull;</p>
<dd> The regular expression captured submatches ($1, <tt>$2</tt>, &#8230;) are now more consistently unset if the match fails, instead of leaving false data lying around in them.</p>
<dt>&bull;</p>
<dd> The tr///C and tr///U features have been removed and will not return; the interface was a mistake. Sorry about that. For similar functionality, see pack(&#8216;U0&#8217;, &#8230;) and pack(&#8216;C0&#8217;, &#8230;).</dl>
<h2>Core Enhancements</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;perl -d:Module=arg,arg,arg&quot;</tt> now works (previously one couldn&#8217;t pass in multiple arguments.)</p>
<dt>&bull;</p>
<dd> my __PACKAGE__ <tt>$obj</tt> now works.</p>
<dt>&bull;</p>
<dd> <tt>&quot;no Module;&quot;</tt> now works even if there is no &#8220;sub unimport&#8221; in the Module.</p>
<dt>&bull;</p>
<dd> The numerical comparison operators return <tt>&quot;undef&quot;</tt> if either operand is a NaN. Previously the behaviour was unspecified.</p>
<dt>&bull;</p>
<dd> <tt>&quot;pack('U0a*', ...)&quot;</tt> can now be used to force a string to <font SIZE="-1">UTF-8</font>.</p>
<dt>&bull;</p>
<dd> prototype(\&amp;) is now available.</p>
<dt>&bull;</p>
<dd> There is now an <font SIZE="-1">UNTIE</font> method.</dl>
<h2>Modules and Pragmata</h2>
<h3>New Modules</h3>
<dl>
<dt>&bull;</p>
<dd> File::Temp allows one to create temporary files and directories in an easy, portable, and secure way.</p>
<dt>&bull;</p>
<dd> Storable gives persistence to Perl data structures by allowing the storage and retrieval of Perl data to and from files in a fast and compact binary format.</dl>
<h3>Updated And Improved Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> The following independently supported modules have been updated to newer versions from <font SIZE="-1">CPAN:</font> <font SIZE="-1">CGI</font>, <font SIZE="-1">CPAN</font>, DB_File, File::Spec, Getopt::Long, the podlators bundle, Pod::LaTeX, Pod::Parser, Term::ANSIColor, Test.</p>
<dt>&bull;</p>
<dd> Bug fixes and minor enhancements have been applied to B::Deparse, Data::Dumper, IO::Poll, IO::Socket::INET, Math::BigFloat, Math::Complex, Math::Trig, Net::protoent, the re pragma, SelfLoader, Sys::SysLog, Test::Harness, Text::Wrap, <font SIZE="-1">UNIVERSAL</font>, and the warnings pragma.</p>
<dt>&bull;</p>
<dd> The <i>attributes::reftype()</i> now works on tied arguments.</p>
<dt>&bull;</p>
<dd> AutoLoader can now be disabled with <tt>&quot;no AutoLoader;&quot;</tt>,</p>
<dt>&bull;</p>
<dd> The English module can now be used without the infamous performance hit by saying </p>
<pre>
        use English '-no_performance_hit';
</pre>
<p> (Assuming, of course, that one doesn&#8217;t need the troublesome variables <tt>&quot;$`&quot;</tt>, <tt>$&amp;</tt>, or <tt>&quot;$'&quot;</tt>.) Also, introduced <tt>@LAST_MATCH_START</tt> and <tt>@LAST_MATCH_END</tt> English aliases for <tt>&quot;@-&quot;</tt> and <tt>&quot;@+&quot;</tt>.</p>
<dt>&bull;</p>
<dd> File::Find now has pre- and post-processing callbacks. It also correctly changes directories when chasing symbolic links. Callbacks (naughtily) exiting with &#8220;next;&#8221; instead of &#8220;return;&#8221; now work.</p>
<dt>&bull;</p>
<dd> <i>File::Glob::glob()</i> renamed to <i>File::Glob::bsd_glob()</i> to avoid prototype mismatch with <i>CORE::glob()</i>.</p>
<dt>&bull;</p>
<dd> IPC::Open3 now allows the use of numeric file descriptors.</p>
<dt>&bull;</p>
<dd> use lib now works identically to <tt>@INC</tt>. Removing directories with &#8216;no lib&#8217; now works.</p>
<dt>&bull;</p>
<dd> <tt>%INC</tt> now localised in a Safe compartment so that use/require work.</p>
<dt>&bull;</p>
<dd> The Shell module now has an <font SIZE="-1">OO</font> interface.</dl>
<h2>Utility Changes</h2>
<dl>
<dt>&bull;</p>
<dd> The Emacs perl mode (emacs/cperl-mode.el) has been updated to version 4.31.</p>
<dt>&bull;</p>
<dd> Perlbug is now much more robust. It also sends the bug report to perl.org, not perl.com.</p>
<dt>&bull;</p>
<dd> The perlcc utility has been rewritten and its user interface (that is, command line) is much more like that of the Unix C compiler, cc.</p>
<dt>&bull;</p>
<dd> The xsubpp utility for extension writers now understands <font SIZE="-1">POD</font> documentation embedded in the *.xs files.</dl>
<h2>New Documentation</h2>
<dl>
<dt>&bull;</p>
<dd> perl56delta details the changes between the 5.005 release and the 5.6.0 release.</p>
<dt>&bull;</p>
<dd> perldebtut is a Perl debugging tutorial.</p>
<dt>&bull;</p>
<dd> perlebcdic contains considerations for running Perl on <font SIZE="-1">EBCDIC</font> platforms. Note that unfortunately <font SIZE="-1">EBCDIC</font> platforms that used to supported back in Perl 5.005 are still unsupported by Perl 5.7.0; the plan, however, is to bring them back to the fold.</p>
<dt>&bull;</p>
<dd> perlnewmod tells about writing and submitting a new module.</p>
<dt>&bull;</p>
<dd> perlposix-bc explains using Perl on the POSIX-BC platform (an <font SIZE="-1">EBCDIC</font> mainframe platform).</p>
<dt>&bull;</p>
<dd> perlretut is a regular expression tutorial.</p>
<dt>&bull;</p>
<dd> perlrequick is a regular expressions quick-start guide. Yes, much quicker than perlretut.</p>
<dt>&bull;</p>
<dd> perlutil explains the command line utilities packaged with the Perl distribution.</dl>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</p>
<dd> <i>map()</i> that changes the size of the list should now work faster.</p>
<dt>&bull;</p>
<dd> <i>sort()</i> has been changed to use mergesort internally as opposed to the earlier quicksort. For very small lists this may result in slightly slower sorting times, but in general the speedup should be at least 20%. Additional bonuses are that the worst case behaviour of <i>sort()</i> is now better (in computer science terms it now runs in time O(N log N), as opposed to quicksort&#8217;s Theta(N**2) worst-case run time behaviour), and that <i>sort()</i> is now stable (meaning that elements with identical keys will stay ordered as they were before the sort).</dl>
<h2>Installation and Configuration Improvements</h2>
<h3>Generic Improvements</h3>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">INSTALL</font> now explains how you can configure Perl to use 64-bit integers even on non-64-bit platforms.</p>
<dt>&bull;</p>
<dd> Policy.sh policy change: if you are reusing a Policy.sh file (see <font SIZE="-1">INSTALL</font>) and you use Configure -Dprefix=/foo/bar and in the old Policy <tt>$prefix</tt> eq <tt>$siteprefix</tt> and <tt>$prefix</tt> eq <tt>$vendorprefix</tt>, all of them will now be changed to the new prefix, /foo/bar. (Previously only <tt>$prefix</tt> changed.) If you do not like this new behaviour, specify prefix, siteprefix, and vendorprefix explicitly.</p>
<dt>&bull;</p>
<dd> A new optional location for Perl libraries, otherlibdirs, is available. It can be used for example for vendor add-ons without disturbing Perl&#8217;s own library directories.</p>
<dt>&bull;</p>
<dd> In many platforms the vendor-supplied &#8216;cc&#8217; is too stripped-down to build Perl (basically, &#8216;cc&#8217; doesn&#8217;t do <font SIZE="-1">ANSI</font> C). If this seems to be the case and &#8216;cc&#8217; does not seem to be the <font SIZE="-1">GNU</font> C compiler &#8216;gcc&#8217;, an automatic attempt is made to find and use &#8216;gcc&#8217; instead.</p>
<dt>&bull;</p>
<dd> gcc needs to closely track the operating system release to avoid build problems. If Configure finds that gcc was built for a different operating system release than is running, it now gives a clearly visible warning that there may be trouble ahead.</p>
<dt>&bull;</p>
<dd> If binary compatibility with the 5.005 release is not wanted, Configure no longer suggests including the 5.005 modules in <tt>@INC</tt>.</p>
<dt>&bull;</p>
<dd> Configure <tt>&quot;-S&quot;</tt> can now run non-interactively.</p>
<dt>&bull;</p>
<dd> configure.gnu now works with options with whitespace in them.</p>
<dt>&bull;</p>
<dd> installperl now outputs everything to <font SIZE="-1">STDERR</font>.</p>
<dt>&bull;</p>
<dd> <tt>$Config</tt>{byteorder} is now computed dynamically (this is more robust with &#8220;fat binaries&#8221; where an executable image contains binaries for more than one binary platform.)</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> Several debugger fixes: exit code now reflects the script exit code, condition <tt>&quot;0&quot;</tt> now treated correctly, the <tt>&quot;d&quot;</tt> command now checks line number, the <tt>$.</tt> no longer gets corrupted, all debugger output now goes correctly to the socket if RemotePort is set.</p>
<dt>&bull;</p>
<dd> <tt>*foo{FORMAT}</tt> now works.</p>
<dt>&bull;</p>
<dd> Lexical warnings now propagating correctly between scopes.</p>
<dt>&bull;</p>
<dd> Line renumbering with eval and <tt>&quot;#line&quot;</tt> now works.</p>
<dt>&bull;</p>
<dd> Fixed numerous memory leaks, especially in eval &quot;&quot;.</p>
<dt>&bull;</p>
<dd> Modulus of unsigned numbers now works (4063328477 % 65535 used to return 27406, instead of 27047).</p>
<dt>&bull;</p>
<dd> Some &#8220;not a number&#8221; warnings introduced in 5.6.0 eliminated to be more compatible with 5.005. Infinity is now recognised as a number.</p>
<dt>&bull;</p>
<dd> <i>our()</i> variables will not cause &#8220;will not stay shared&#8221; warnings.</p>
<dt>&bull;</p>
<dd> pack &#8220;Z&#8221; now correctly terminates the string with &#8220;
