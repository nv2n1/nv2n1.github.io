---
title: "perl572delta(1)"
name: "perl572delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl572delta/"
description: "perl572delta – what’s new for perl v5.7.2"
---

<h2 class="name">NAME</h2>
<p> perl572delta &#8211; what&#8217;s new for perl v5.7.2 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.7.1 release and the 5.7.2 release. </p>
<p> (To view the differences between the 5.6.0 release and the 5.7.0 release, see perl570delta. To view the differences between the 5.7.0 release and the 5.7.1 release, see perl571delta.)</p>
<h2>Security Vulnerability Closed</h2>
<p> (This change was already made in 5.7.0 but bears repeating here.) </p>
<p> A security vulnerability affecting all Perl versions prior to 5.6.1 was found in August 2000. The vulnerability does not affect default installations and as far as is known affects only the Linux platform. </p>
<p> You should upgrade your Perl to 5.6.1 as soon as possible. Patches for earlier releases exist but using the patches require full recompilation from the source code anyway, so 5.6.1 is your best choice. </p>
<p> See <a rel="nofollow" href="http://www.cpan.org/src/5.0/sperl-2000-08-05/sperl-2000-08-05.txt">http://www.cpan.org/src/5.0/sperl-2000-08-05/sperl-2000-08-05.txt</a> for more information.</p>
<h2>Incompatible Changes</h2>
<h3>64-bit platforms and malloc</h3>
<p> If your pointers are 64 bits wide, the Perl malloc is no more being used because it simply does not work with 8-byte pointers. Also, usually the system malloc on such platforms are much better optimized for such large memory models than the Perl malloc.</p>
<h3><font SIZE="-1">AIX</font> Dynaloading</h3>
<p> The <font SIZE="-1">AIX</font> dynaloading now uses in <font SIZE="-1">AIX</font> releases 4.3 and newer the native dlopen interface of <font SIZE="-1">AIX</font> instead of the old emulated interface. This change will probably break backward compatibility with compiled modules. The change was made to make Perl more compliant with other applications like modperl which are using the <font SIZE="-1">AIX</font> native interface.</p>
<h3>Socket Extension Dynamic in <font SIZE="-1">VMS</font></h3>
<p> The Socket extension is now dynamically loaded instead of being statically built in. This may or may not be a problem with ancient <font SIZE="-1">TCP/IP</font> stacks of <font SIZE="-1">VMS:</font> we do not know since we weren&#8217;t able to test Perl in such configurations.</p>
<h3>Different Definition of the Unicode Character Classes \p{In&#8230;}</h3>
<p> As suggested by the Unicode consortium, the Unicode character classes now prefer <i>scripts</i> as opposed to <i>blocks</i> (as defined by Unicode); in Perl, when the <tt>&quot;\p{In....}&quot;</tt> and the <tt>&quot;\p{In....}&quot;</tt> regular expression constructs are used. This has changed the definition of some of those character classes. </p>
<p> The difference between scripts and blocks is that scripts are the glyphs used by a language or a group of languages, while the blocks are more artificial groupings of 256 characters based on the Unicode numbering. </p>
<p> In general this change results in more inclusive Unicode character classes, but changes to the other direction also do take place: for example while the script <tt>&quot;Latin&quot;</tt> includes all the Latin characters and their various diacritic-adorned versions, it does not include the various punctuation or digits (since they are not solely <tt>&quot;Latin&quot;</tt>). </p>
<p> Changes in the character class semantics may have happened if a script and a block happen to have the same name, for example <tt>&quot;Hebrew&quot;</tt>. In such cases the script wins and <tt>&quot;\p{InHebrew}&quot;</tt> now means the script definition of Hebrew. The block definition in still available, though, by appending <tt>&quot;Block&quot;</tt> to the name: <tt>&quot;\p{InHebrewBlock}&quot;</tt> means what <tt>&quot;\p{InHebrew}&quot;</tt> meant in perl 5.6.0. For the full list of affected character classes, see &#8220;Blocks&#8221; in perlunicode.</p>
<h3>Deprecations</h3>
<p> The current user-visible implementation of pseudo-hashes (the weird use of the first array element) is deprecated starting from Perl 5.8.0 and will be removed in Perl 5.10.0, and the feature will be implemented differently. Not only is the current interface rather ugly, but the current implementation slows down normal array and hash use quite noticeably. The <tt>&quot;fields&quot;</tt> pragma interface will remain available. </p>
<p> The syntaxes <tt>&quot;@a-&gt;[...]&quot;</tt> and <tt>&quot;@h-&gt;{...}&quot;</tt> have now been deprecated. </p>
<p> The suidperl is also considered to be too much a risk to continue maintaining and the suidperl code is likely to be removed in a future release. </p>
<p> The <tt>&quot;package;&quot;</tt> syntax (<tt>&quot;package&quot;</tt> without an argument has been deprecated. Its semantics were never that clear and its implementation even less so. If you have used that feature to disallow all but fully qualified variables, <tt>&quot;use strict;&quot;</tt> instead. </p>
<p> The chdir(undef) and chdir(&#8221;) behaviors to match <i>chdir()</i> has been deprecated. In future versions, chdir(undef) and chdir(&#8221;) will simply fail.</p>
<h2>Core Enhancements</h2>
<p> In general a lot of fixing has happened in the area of Perl&#8217;s understanding of numbers, both integer and floating point. Since in many systems the standard number parsing functions like <tt>&quot;strtoul()&quot;</tt> and <tt>&quot;atof()&quot;</tt> seem to have bugs, Perl tries to work around their deficiencies. This results hopefully in more accurate numbers.</p>
<dl>
<dt>&bull;</p>
<dd> The rules for allowing underscores (underbars) in numeric constants have been relaxed and simplified: now you can have an underscore <code>between digits</code>.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">GMAGIC</font> (right-hand side magic) could in many cases such as string concatenation be invoked too many times.</p>
<dt>&bull;</p>
<dd> Lexicals I: lexicals outside an eval &quot;&#8220; weren&#8217;t resolved correctly inside a subroutine definition inside the eval &#8221;&#8220; if they were not already referenced in the top level of the eval&#8221;&quot;ed code.</p>
<dt>&bull;</p>
<dd> Lexicals <font SIZE="-1">II:</font> lexicals leaked at file scope into subroutines that were declared before the lexicals.</p>
<dt>&bull;</p>
<dd> Lvalue subroutines can now return <tt>&quot;undef&quot;</tt> in list context.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;op_clear&quot;</tt> and <tt>&quot;op_null&quot;</tt> are now exported.</p>
<dt>&bull;</p>
<dd> A new special regular expression variable has been introduced: <tt>$^N</tt>, which contains the most-recently closed group (submatch).</p>
<dt>&bull;</p>
<dd> utime now supports <tt>&quot;utime undef, undef, @files&quot;</tt> to change the file timestamps to the current time.</p>
<dt>&bull;</p>
<dd> The Perl parser has been stress tested using both random input and Markov chain input.</p>
<dt>&bull;</p>
<dd> <tt>&quot;eval &quot;v200&quot;&quot;</tt> now works.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">VMS</font> now works under PerlIO.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">END</font> blocks are now run even if you exit/die in a <font SIZE="-1">BEGIN</font> block. The execution of <font SIZE="-1">END</font> blocks is now controlled by PL_exit_flags &amp; <font SIZE="-1">PERL_EXIT_DESTRUCT_END</font>. This enables the new behaviour for perl embedders. This will default in 5.10. See perlembed.</dl>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Distributions</h3>
<dl>
<dt>&bull;</p>
<dd> Attribute::Handlers &#8211; Simpler definition of attribute handlers</p>
<dt>&bull;</p>
<dd> ExtUtils::Constant &#8211; generate <font SIZE="-1">XS</font> code to import C header constants</p>
<dt>&bull;</p>
<dd> I18N::Langinfo &#8211; query locale information</p>
<dt>&bull;</p>
<dd> I18N::LangTags &#8211; functions for dealing with RFC3066-style language tags</p>
<dt>&bull;</p>
<dd> libnet &#8211; a collection of perl5 modules related to network programming </p>
<p> Perl installation leaves libnet unconfigured, use <i>libnetcfg</i> to configure.</p>
<dt>&bull;</p>
<dd> List::Util &#8211; selection of general-utility list subroutines</p>
<dt>&bull;</p>
<dd> Locale::Maketext &#8211; framework for localization</p>
<dt>&bull;</p>
<dd> Memoize &#8211; Make your functions faster by trading space for time</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">NEXT</font> &#8211; pseudo-class for method redispatch</p>
<dt>&bull;</p>
<dd> Scalar::Util &#8211; selection of general-utility scalar subroutines</p>
<dt>&bull;</p>
<dd> Test::More &#8211; yet another framework for writing test scripts</p>
<dt>&bull;</p>
<dd> Test::Simple &#8211; Basic utilities for writing tests</p>
<dt>&bull;</p>
<dd> Time::HiRes &#8211; high resolution ualarm, usleep, and gettimeofday</p>
<dt>&bull;</p>
<dd> Time::Piece &#8211; Object Oriented time objects </p>
<p> (Previously known as Time::Object.)</p>
<dt>&bull;</p>
<dd> Time::Seconds &#8211; a simple <font SIZE="-1">API</font> to convert seconds to other date values</p>
<dt>&bull;</p>
<dd> UnicodeCD &#8211; Unicode Character Database</dl>
<h3>Updated And Improved Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> B::Deparse module has been significantly enhanced. It now can deparse almost all of the standard test suite (so that the tests still succeed). There is a make target &#8220;test.deparse&#8221; for trying this out.</p>
<dt>&bull;</p>
<dd> Class::Struct now assigns the array/hash element if the accessor is called with an array/hash element as the <code>sole</code> argument.</p>
<dt>&bull;</p>
<dd> Cwd extension is now (even) faster.</p>
<dt>&bull;</p>
<dd> DB_File extension has been updated to version 1.77.</p>
<dt>&bull;</p>
<dd> Fcntl, Socket, and Sys::Syslog have been rewritten to use the new-style constant dispatch section (see ExtUtils::Constant).</p>
<dt>&bull;</p>
<dd> File::Find is now (again) reentrant. It also has been made more portable.</p>
<dt>&bull;</p>
<dd> File::Glob now supports <tt>&quot;GLOB_LIMIT&quot;</tt> constant to limit the size of the returned list of filenames.</p>
<dt>&bull;</p>
<dd> IO::Socket::INET now supports <tt>&quot;LocalPort&quot;</tt> of zero (usually meaning that the operating system will make one up.)</p>
<dt>&bull;</p>
<dd> The vars pragma now supports declaring fully qualified variables. (Something that <tt>&quot;our()&quot;</tt> does not and will not support.)</dl>
<h2>Utility Changes</h2>
<dl>
<dt>&bull;</p>
<dd> The <i>emacs/e2ctags.pl</i> is now much faster.</p>
<dt>&bull;</p>
<dd> h2ph now supports C trigraphs.</p>
<dt>&bull;</p>
<dd> h2xs uses the new ExtUtils::Constant module which will affect newly created extensions that define constants. Since the new code is more correct (if you have two constants where the first one is a prefix of the second one, the first constant <code>never</code> gets defined), less lossy (it uses integers for integer constant, as opposed to the old code that used floating point numbers even for integer constants), and slightly faster, you might want to consider regenerating your extension code (the new scheme makes regenerating easy). h2xs now also supports C trigraphs.</p>
<dt>&bull;</p>
<dd> libnetcfg has been added to configure the libnet.</p>
<dt>&bull;</p>
<dd> The <i>Pod::Html</i> (and thusly pod2html) now allows specifying a cache directory.</dl>
<h2>New Documentation</h2>
<dl>
<dt>&bull;</p>
<dd> Locale::Maketext::TPJ13 is an article about software localization, originally published in The Perl Journal #13, republished here with kind permission.</p>
<dt>&bull;</p>
<dd> More <font SIZE="-1">README</font>.$PLATFORM files have been converted into pod, which also means that they also be installed as perl$PLATFORM documentation files. The new files are perlapollo, perlbeos, perldgux, perlhurd, perlmint, perlnetware, perlplan9, perlqnx, and perltru64.</p>
<dt>&bull;</p>
<dd> The <i>Todo</i> and <i>Todo-5.6</i> files have been merged into perltodo.</p>
<dt>&bull;</p>
<dd> Use of the <i>gprof</i> tool to profile Perl has been documented in perlhack. There is a make target &#8220;perl.gprof&#8221; for generating a gprofiled Perl executable.</dl>
<h2>Installation and Configuration Improvements</h2>
<h3>New Or Improved Platforms</h3>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">AIX</font> should now work better with gcc, threads, and 64-bitness. Also the long doubles support in <font SIZE="-1">AIX</font> should be better now. See perlaix.</p>
<dt>&bull;</p>
<dd> AtheOS ( <a rel="nofollow" href="http://www.atheos.cx/">http://www.atheos.cx/</a> ) is a new platform.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">DG/UX</font> platform now supports the 5.005-style threads. See perldgux.</p>
<dt>&bull;</p>
<dd> DYNIX/ptx platform (a.k.a. dynixptx) is supported at or near osvers 4.5.2.</p>
<dt>&bull;</p>
<dd> Several Mac <font SIZE="-1">OS</font> (Classic) portability patches have been applied. We hope to get a fully working port by 5.8.0. (The remaining problems relate to the changed <font SIZE="-1">IO</font> model of Perl.) See perlmacos.</p>
<dt>&bull;</p>
<dd> Mac <font SIZE="-1">OS</font> X (or Darwin) should now be able to build Perl even on <font SIZE="-1">HFS+</font> filesystems. (The case-insensitivity confused the Perl build process.)</p>
<dt>&bull;</p>
<dd> NetWare from Novell is now supported. See perlnetware.</p>
<dt>&bull;</p>
<dd> The Amdahl <font SIZE="-1">UTS</font> Unix mainframe platform is now supported.</dl>
<h3>Generic Improvements</h3>
<dl>
<dt>&bull;</p>
<dd> In <font SIZE="-1">AFS</font> installations one can configure the root of the <font SIZE="-1">AFS</font> to be somewhere else than the default <i>/afs</i> by using the Configure parameter <tt>&quot;-Dafsroot=/some/where/else&quot;</tt>.</p>
<dt>&bull;</p>
<dd> The version of Berkeley <font SIZE="-1">DB</font> used when the Perl (and, presumably, the DB_File extension) was built is now available as <tt>@Config{qw(db_version_major db_version_minor db_version_patch)}</tt> from Perl and as <tt>&quot;DB_VERSION_MAJOR_CFG DB_VERSION_MINOR_CFG DB_VERSION_PATCH_CFG&quot;</tt> from C.</p>
<dt>&bull;</p>
<dd> The Thread extension is now not built at all under ithreads (<tt>&quot;Configure -Duseithreads&quot;</tt>) because it wouldn&#8217;t work anyway (the Thread extension requires being Configured with <tt>&quot;-Duse5005threads&quot;</tt>).</p>
<dt>&bull;</p>
<dd> The <tt>&quot;B::Deparse&quot;</tt> compiler backend has been so significantly improved that almost the whole Perl test suite passes after being deparsed. A make target has been added to help in further testing: <tt>&quot;make test.deparse&quot;</tt>.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> The autouse pragma didn&#8217;t work for Multi::Part::Function::Names.</p>
<dt>&bull;</p>
<dd> The behaviour of non-decimal but numeric string constants such as &#8220;0x23&#8221; was platform-dependent: in some platforms that was seen as 35, in some as 0, in some as a floating point number (don&#8217;t ask). This was caused by Perl using the operating system libraries in a situation where the result of the string to number conversion is undefined: now Perl consistently handles such strings as zero in numeric contexts.</p>
<dt>&bull;</p>
<dd> dprofpp -R didn&#8217;t work.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">PERL5OPT</font> with embedded spaces didn&#8217;t work.</p>
<dt>&bull;</p>
<dd> Sys::Syslog ignored the <tt>&quot;LOG_AUTH&quot;</tt> constant.</dl>
<h3>Platform Specific Changes and Fixes</h3>
<dl>
<dt>&bull;</p>
<dd> Some versions of glibc have a broken <i>modfl()</i>. This affects builds with <tt>&quot;-Duselongdouble&quot;</tt>. This version of Perl detects this brokenness and has a workaround for it. The glibc release 2.2.2 is known to have fixed the <i>modfl()</i> bug.</dl>
<h2>New or Changed Diagnostics</h2>
<dl>
<dt>&bull;</p>
<dd> In the regular expression diagnostics the <tt>&quot;&lt;&lt; HERE&quot;</tt> marker introduced in 5.7.0 has been changed to be <tt>&quot;&lt;-- HERE&quot;</tt> since too many people found the <tt>&quot;&lt;&lt;&quot;</tt> to be too similar to here-document starters.</p>
<dt>&bull;</p>
<dd> If you try to &#8220;pack&#8221; in perlfunc a number less than 0 or larger than 255 using the <tt>&quot;C&quot;</tt> format you will get an optional warning. Similarly for the <tt>&quot;c&quot;</tt> format and a number less than -128 or more than 127.</p>
<dt>&bull;</p>
<dd> Certain regex modifiers such as <tt>&quot;(?o)&quot;</tt> make sense only if applied to the entire regex. You will an optional warning if you try to do otherwise.</p>
<dt>&bull;</p>
<dd> Using arrays or hashes as references (e.g. <tt>&quot;%foo-&gt;{bar}&quot;</tt> has been deprecated for a while. Now you will get an optional warning.</dl>
<h2>Source Code Enhancements</h2>
<h3><font SIZE="-1">MAGIC</font> constants</h3>
<p> The <font SIZE="-1">MAGIC</font> constants (e.g. <tt>'P'</tt>) have been macrofied (e.g. <tt>&quot;PERL_MAGIC_TIED&quot;</tt>) for better source code readability and maintainability.</p>
<h3>Better commented code</h3>
<p> <i>perly.c</i>, <i>sv.c</i>, and <i>sv.h</i> have now been extensively commented.</p>
<h3>Regex pre-/post-compilation items matched up</h3>
<p> The regex compiler now maintains a structure that identifies nodes in the compiled bytecode with the corresponding syntactic features of the original regex expression. The information is attached to the new <tt>&quot;offsets&quot;</tt> member of the <tt>&quot;struct regexp&quot;</tt>. See perldebguts for more complete information.</p>
<h3>gcc -Wall</h3>
<p> The C code has been made much more <tt>&quot;gcc -Wall&quot;</tt> clean. Some warning messages still remain, though, so if you are compiling with gcc you will see some warnings about dubious practices. The warnings are being worked on.</p>
<h2>New Tests</h2>
<p> Several new tests have been added, especially for the <i>lib</i> subsection. </p>
<p> The tests are now reported in a different order than in earlier Perls. (This happens because the test scripts from under t/lib have been moved to be closer to the library/extension they are testing.)</p>
<h2>Known Problems</h2>
<p> Note that unlike other sections in this document (which describe changes since 5.7.0) this section is cumulative containing known problems for all the 5.7 releases.</p>
<h3><font SIZE="-1">AIX</font></h3>
<dl>
<dt>&bull;</p>
<dd> In <font SIZE="-1">AIX</font> 4.2 Perl extensions that use C<font SIZE="-2">++</font> functions that use statics may have problems in that the statics are not getting initialized. In newer <font SIZE="-1">AIX</font> releases this has been solved by linking Perl with the libC_r library, but unfortunately in <font SIZE="-1">AIX</font> 4.2 the said library has an obscure bug where the various functions related to time (such as <i>time()</i> and <i>gettimeofday()</i>) return broken values, and therefore in <font SIZE="-1">AIX</font> 4.2 Perl is not linked against the libC_r.</p>
<dt>&bull;</p>
<dd> vac 5.0.0.0 May Produce Buggy Code For Perl </p>
<p> The <font SIZE="-1">AIX</font> C compiler vac version 5.0.0.0 may produce buggy code, resulting in few random tests failing, but when the failing tests are run by hand, they succeed. We suggest upgrading to at least vac version 5.0.1.0, that has been known to compile Perl correctly. &#8220;lslpp -L|grep vac.C&#8221; will tell you the vac version.</dl>
<h3>Amiga Perl Invoking Mystery</h3>
<p> One cannot call Perl using the <tt>&quot;volume:&quot;</tt> syntax, that is, <tt>&quot;perl -v&quot;</tt> works, but for example <tt>&quot;bin:perl -v&quot;</tt> doesn&#8217;t. The exact reason is known but the current suspect is the <i>ixemul</i> library.</p>
<h3>lib/ftmp-security tests warn &#8216;system possibly insecure&#8217;</h3>
<p> Don&#8217;t panic. Read <font SIZE="-1">INSTALL</font> &#8216;make test&#8217; section instead.</p>
<h3>Cygwin intermittent failures of lib/Memoize/t/expire_file 11 and 12</h3>
<p> The subtests 11 and 12 sometimes fail and sometimes work.</p>
<h3>HP-UX lib/io_multihomed Fails When LP64-Configured</h3>
<p> The lib/io_multihomed test may hang in HP-UX if Perl has been configured to be 64-bit. Because other 64-bit platforms do not hang in this test, HP-UX is suspect. All other tests pass in 64-bit HP-UX. The test attempts to create and connect to &#8220;multihomed&#8221; sockets (sockets which have multiple <font SIZE="-1">IP</font> addresses).</p>
<h3>HP-UX lib/posix Subtest 9 Fails When LP64-Configured</h3>
<p> If perl is configured with -Duse64bitall, the successful result of the subtest 10 of lib/posix may arrive before the successful result of the subtest 9, which confuses the test harness so much that it thinks the subtest 9 failed.</p>
<h3>Linux With Sfio Fails op/misc Test 48</h3>
<p> No known fix.</p>
<h3><font SIZE="-1">OS/390</font></h3>
<p> <font SIZE="-1">OS/390</font> has rather many test failures but the situation is actually better than it was in 5.6.0, it&#8217;s just that so many new modules and tests have been added. </p>
<pre><code>
Failed Test Stat Wstat Total Fail Failed List of Failed-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -../ ext / B / Deparse.t 14 1 7.14 % 14../ ext / B / Showlex.t 1 1 100.00 % 1../ ext / Encode / Encode / Tcl.t 610 13 2.13 % 592 594 596 598 600 602 604 - 610../ ext / IO / lib / IO / t / io_unix.t 113 28928 5 3 60.00 % 3 - 5../ ext / POSIX / POSIX.t 29 1 3.45 % 14../ ext / Storable / t / lock.t 255 65280 5 3 60.00 % 3 - 5../ lib / locale.t 129 33024 117 19 16.24 % 99 - 117../ lib / warnings.t 434 1 0.23 % 75../ lib / ExtUtils.t 27 1 3.70 % 25../ lib / Math / BigInt / t / bigintpm.t 1190 1 0.08 % 1145../ lib / Unicode / UCD.t 81 48 59.26 % 1 - 16 49 - 64 66 - 81../ lib / User / pwent.t 9 1 11.11 % 4 op / pat.t 660 6 0.91 % 242 - 243 424 - 425 626 - 627 op / split.t 0 9 ? ? ? ? % ? ? op / taint.t 174 3 1.72 % 156 162 168 op / tr.t 70 3 4.29 % 50 58 - 59 Failed 16 / 422 test scripts, 96.21 % okay.105 / 23251 subtests failed, 99.55 % okay.
</code></pre>
<h3>op/sprintf tests 129 and 130</h3>
<p> The op/sprintf tests 129 and 130 are known to fail on some platforms. Examples include any platform using sfio, and Compaq/Tandem&#8217;s NonStop-UX. The failing platforms do not comply with the <font SIZE="-1">ANSI</font> C Standard, line 19ff on page 134 of <font SIZE="-1">ANSI</font> X3.159 1989 to be exact. (They produce something other than &#8220;1&#8221; and &#8220;-1&#8221; when formatting 0.6 and -0.6 using the printf format &#8220;%.0f&#8221;, most often they produce &#8220;0&#8221; and &#8220;-0&#8221;.)</p>
<h3>Failure of Thread tests</h3>
<p> <code>Note that support for 5.005-style threading remains experimental.</code> </p>
<p> The following tests are known to fail due to fundamental problems in the 5.005 threading implementation. These are not new failures&#8212;Perl 5.005_0x has the same bugs, but didn&#8217;t have these tests. </p>
<pre>
  lib/autouse.t                 4
  t/lib/thr5005.t               19-20
</pre>
<h3><font SIZE="-1">UNICOS</font></h3>
<dl>
<dt>&bull;</p>
<dd> ext/POSIX/sigaction subtests 6 and 13 may fail.</p>
<dt>&bull;</p>
<dd> lib/ExtUtils may spuriously claim that subtest 28 failed, which is interesting since the test only has 27 tests.</p>
<dt>&bull;</p>
<dd> Numerous numerical test failures </p>
<pre>
  op/numconvert                 209,210,217,218
  op/override                   7
  ext/Time/HiRes/HiRes          9
  lib/Math/BigInt/t/bigintpm    1145
  lib/Math/Trig                 25
</pre>
<p> These tests fail because of yet unresolved floating point inaccuracies.</dl>
<h3><font SIZE="-1">UTS</font></h3>
<p> There are a few known test failures, see perluts.</p>
<h3><font SIZE="-1">VMS</font></h3>
<p> Rather many tests are failing in <font SIZE="-1">VMS</font> but that actually more tests succeed in <font SIZE="-1">VMS</font> than they used to, it&#8217;s just that there are many, many more tests than there used to be. </p>
<p> Here are the known failures from some compiler/platform combinations. </p>
<p> <font SIZE="-1">DEC</font> C V5.3-006 on OpenVMS <font SIZE="-1">VAX</font> V6.2 </p>
<p>[-.ext.list.util.t] tainted&#8230;&#8230;&#8230;&#8230;..FAILED on test 3<br />
        [-.ext.posix] sigaction&#8230;&#8230;&#8230;&#8230;&#8230;&#8230; FAILED on test 7<br />
            [-.ext.time.hires] hires&#8230;&#8230;&#8230;&#8230;&#8230;..FAILED on test 14<br />
                [-.lib.file.find] taint&#8230;&#8230;&#8230;&#8230;&#8230;&#8230; FAILED on test 17<br />
                    [-.lib.math.bigint.t] bigintpm&#8230;&#8230;&#8230;..FAILED on test 1183<br />
                        [-.lib.test.simple.t] exit&#8230;&#8230;&#8230;&#8230;&#8230; FAILED on test 1<br />
                            [.lib] vmsish&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;.FAILED on test 13<br />
                                [.op] sprintf&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;.FAILED on test 12 Failed 8 /<br />
    399 tests,<br />
    91.23 % okay.</p>
<p> <font SIZE="-1">DEC</font> C V6.0-001 on OpenVMS Alpha V7.2-1 and Compaq C V6.2-008 on OpenVMS Alpha V7.1 </p>
<p>[-.ext.list.util.t] tainted&#8230;&#8230;&#8230;&#8230;..FAILED on test 3<br />
        [-.lib.file.find] taint&#8230;&#8230;&#8230;&#8230;&#8230;&#8230; FAILED on test 17<br />
            [-.lib.test.simple.t] exit&#8230;&#8230;&#8230;&#8230;&#8230; FAILED on test 1<br />
                [.lib] vmsish&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;.FAILED on test 13 Failed 4 /<br />
    399 tests,<br />
    92.48 % okay.</p>
<p> Compaq C V6.4-005 on OpenVMS Alpha 7.2.1 </p>
<p>[-.ext.b] showlex&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230; FAILED on test 1<br />
        [-.ext.list.util.t] tainted&#8230;&#8230;&#8230;&#8230;..FAILED on test 3<br />
            [-.lib.file.find] taint&#8230;&#8230;&#8230;&#8230;&#8230;&#8230; FAILED on test 17<br />
                [-.lib.test.simple.t] exit&#8230;&#8230;&#8230;&#8230;&#8230; FAILED on test 1<br />
                    [.lib] vmsish&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;.FAILED on test 13<br />
                        [.op] misc&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;.FAILED on test 49 Failed 6 /<br />
    401 tests,<br />
    92.77 % okay.</p>
<h3>Win32</h3>
<p> In multi-CPU boxes there are some problems with the I/O buffering: some output may appear twice.</p>
<h3>Localising a Tied Variable Leaks Memory</h3>
<pre><code>
use Tie::Hash;
tie my % tie_hash = &gt; 'Tie::StdHash';
... local($tie_hash{Foo}) = 1;
#leaks
</code></pre>
<p> Code like the above is known to leak memory every time the <i>local()</i> is executed.</p>
<h3>Self-tying of Arrays and Hashes Is Forbidden</h3>
<p> Self-tying of arrays and hashes is broken in rather deep and hard-to-fix ways. As a stop-gap measure to avoid people from getting frustrated at the mysterious results (core dumps, most often) it is for now forbidden (you will get a fatal error even from an attempt).</p>
<h3>Variable Attributes are not Currently Usable for Tying</h3>
<p> This limitation will hopefully be fixed in future. (Subroutine attributes work fine for tying, see Attribute::Handlers).</p>
<h3>Building Extensions Can Fail Because Of Largefiles</h3>
<p> Some extensions like mod_perl are known to have issues with `largefiles&#8217;, a change brought by Perl 5.6.0 in which file offsets default to 64 bits wide, where supported. Modules may fail to compile at all or compile and work incorrectly. Currently there is no good solution for the problem, but Configure now provides appropriate non-largefile ccflags, ldflags, libswanted, and libs in the <tt>%Config</tt> hash (e.g., <tt>$Config</tt>{ccflags_nolargefiles}) so the extensions that are having problems can try configuring themselves without the largefileness. This is admittedly not a clean solution, and the solution may not even work at all. One potential failure is whether one can (or, if one can, whether it&#8217;s a good idea) link together at all binaries with different ideas about file offsets, all this is platform-dependent.</p>
<h3>The Compiler Suite Is Still Experimental</h3>
<p> The compiler suite is slowly getting better but is nowhere near working order yet.</p>
<h3>The Long Double Support is Still Experimental</h3>
<p> The ability to configure Perl&#8217;s numbers to use &#8220;long doubles&#8221;, floating point numbers of hopefully better accuracy, is still experimental. The implementations of long doubles are not yet widespread and the existing implementations are not quite mature or standardised, therefore trying to support them is a rare and moving target. The gain of more precision may also be offset by slowdown in computations (more bits to move around, and the operations are more likely to be executed by less optimised libraries).</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a> There may also be information at <a rel="nofollow" href="http://www.perl.com/perl/">http://www.perl.com/perl/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information.</p>
<h2>HISTORY</h2>
<p> Written by Jarkko Hietaniemi &lt;<i>jhi [at] iki.fi</i>&gt;, with many contributions from The Perl Porters and Perl Users submitting feedback and patches. </p>
<p> Send omissions or corrections to &lt;<i>perlbug [at] perl.org</i>&gt;. </p>
<h2>Index</h2>
<dt><a href="#lbAK">Core Enhancements</a></p>
<dd>
<dt><a href="#lbAL">Modules and Pragmata</a></p>
<dd>
<dt><a href="#lbAO">Utility Changes</a></p>
<dd>
<dt><a href="#lbAP">New Documentation</a></p>
<dd>
<dt><a href="#lbAQ">Installation and Configuration Improvements</a></p>
<dd>
<dt><a href="#lbAT">Selected Bug Fixes</a></p>
<dd>
<dt><a href="#lbAV">New or Changed Diagnostics</a></p>
<dd>
<dt><a href="#lbAW">Source Code Enhancements</a></p>
<dd>
<dt><a href="#lbBB">New Tests</a></p>
<dd>
<dt><a href="#lbBC">Known Problems</a></p>
<dd>
<dt><a href="#lbBX">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbBY">SEE ALSO</a></p>
<dd>
<dt><a href="#lbBZ">HISTORY</a></p>
<dd></dl>
