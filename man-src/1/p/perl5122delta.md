---
title: "perl5122delta(1)"
name: "perl5122delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5122delta/"
description: "perl5122delta – what is new for perl v5.12.2"
---

<h2 class="name">NAME</h2>
<p> perl5122delta &#8211; what is new for perl v5.12.2 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.12.1 release and the 5.12.2 release. </p>
<p> If you are upgrading from an earlier major version, such as 5.10.1, first read perl5120delta, which describes differences between 5.10.1 and 5.12.0, as well as perl5121delta, which describes earlier changes in the 5.12 stable release series.</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.12.1. If any exist, they are bugs and reports are welcome.</p>
<h2>Core Enhancements</h2>
<p> Other than the bug fixes listed below, there should be no user-visible changes to the core language in this release.</p>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<p> This release does not introduce any new modules or pragmata.</p>
<h3>Pragmata Changes</h3>
<p> In the previous release, <tt>&quot;no </tt>VERSION<tt>;&quot;</tt> statements triggered a bug which could cause feature bundles to be loaded and strict mode to be enabled unintentionally.</p>
<h3>Updated Modules</h3>
<dl>
<dt>&quot;Carp&quot;</p>
<dd> Upgraded from version 1.16 to 1.17. </p>
<p> Carp now detects incomplete <code>caller()</code> overrides and avoids using bogus <tt>@DB::args</tt>. To provide backtraces, Carp relies on particular behaviour of the caller built-in. Carp now detects if other code has overridden this with an incomplete implementation, and modifies its backtrace accordingly. Previously incomplete overrides would cause incorrect values in backtraces (best case), or obscure fatal errors (worst case) </p>
<p> This fixes certain cases of <tt>&quot;Bizarre copy of ARRAY&quot;</tt> caused by modules overriding <tt>&quot;caller()&quot;</tt> incorrectly.</p>
<dt>&quot;CPANPLUS&quot;</p>
<dd> A patch to <i>cpanp-run-perl</i> has been backported from <font SIZE="-1">CPANPLUS</font> <tt>0.9004</tt>. This resolves <font SIZE="-1">RT</font> #55964 &lt;<a rel="nofollow" href="http://rt.cpan.org/Public/Bug/Display.html?id=55964">http://rt.cpan.org/Public/Bug/Display.html?id=55964</a>&gt; and <font SIZE="-1">RT</font> #57106 &lt;<a rel="nofollow" href="http://rt.cpan.org/Public/Bug/Display.html?id=57106">http://rt.cpan.org/Public/Bug/Display.html?id=57106</a>&gt;, both of which related to failures to install distributions that use <tt>&quot;Module::Install::DSL&quot;</tt>.</p>
<dt>&quot;File::Glob&quot;</p>
<dd> A regression which caused a failure to find <tt>&quot;CORE::GLOBAL::glob&quot;</tt> after loading <tt>&quot;File::Glob&quot;</tt> to crash has been fixed. Now, it correctly falls back to external globbing via <tt>&quot;pp_glob&quot;</tt>.</p>
<dt>&quot;File::Copy&quot;</p>
<dd> <tt>&quot;File::Copy::copy(FILE, DIR)&quot;</tt> is now documented.</p>
<dt>&quot;File::Spec&quot;</p>
<dd> Upgraded from version 3.31 to 3.31_01. </p>
<p> Several portability fixes were made in <tt>&quot;File::Spec::VMS&quot;</tt>: a colon is now recognized as a delimiter in native filespecs; caret-escaped delimiters are recognized for better handling of extended filespecs; <tt>&quot;catpath()&quot;</tt> returns an empty directory rather than the current directory if the input directory name is empty; <tt>&quot;abs2rel()&quot;</tt> properly handles Unix-style input.</dl>
<h2>Utility Changes</h2>
<dl>
<dt>&bull;</p>
<dd> <i>perlbug</i> now always gives the reporter a chance to change the email address it guesses for them.</p>
<dt>&bull;</p>
<dd> <i>perlbug</i> should no longer warn about uninitialized values when using the <tt>&quot;-d&quot;</tt> and <tt>&quot;-v&quot;</tt> options.</dl>
<h2>Changes to Existing Documentation</h2>
<dl>
<dt>&bull;</p>
<dd> The existing policy on backward-compatibility and deprecation has been added to perlpolicy, along with definitions of terms like <i>deprecation</i>.</p>
<dt>&bull;</p>
<dd> &#8220;srand&#8221; in perlfunc&#8217;s usage has been clarified.</p>
<dt>&bull;</p>
<dd> The entry for &#8220;die&#8221; in perlfunc was reorganized to emphasize its role in the exception mechanism.</p>
<dt>&bull;</p>
<dd> Perl&#8217;s <font SIZE="-1">INSTALL</font> file has been clarified to explicitly state that Perl requires a C89 compliant <font SIZE="-1">ANSI C</font> Compiler.</p>
<dt>&bull;</p>
<dd> IO::Socket&#8217;s <tt>&quot;getsockopt()&quot;</tt> and <tt>&quot;setsockopt()&quot;</tt> have been documented.</p>
<dt>&bull;</p>
<dd> <i></i>alarm()<i></i>&#8216;s inability to interrupt blocking <font SIZE="-1">IO</font> on Windows has been documented.</p>
<dt>&bull;</p>
<dd> Math::TrulyRandom hasn&#8217;t been updated since 1996 and has been removed as a recommended solution for random number generation.</p>
<dt>&bull;</p>
<dd> perlrun has been updated to clarify the behaviour of octal flags to <i>perl</i>.</p>
<dt>&bull;</p>
<dd> To ease user confusion, <tt>$#</tt> and <tt>$*</tt>, two special variables that were removed in earlier versions of Perl have been documented.</p>
<dt>&bull;</p>
<dd> The version of perlfaq shipped with the Perl core has been updated from the official <font SIZE="-1">FAQ</font> version, which is now maintained in the <tt>&quot;briandfoy/perlfaq&quot;</tt> branch of the Perl repository at &lt;<a href="git://perl5.git.perl.org/perl.git">git://perl5.git.perl.org/perl.git</a>&gt;.</dl>
<h2>Installation and Configuration Improvements</h2>
<h3>Configuration improvements</h3>
<dl>
<dt>&bull;</p>
<dd> The <tt>&quot;d_u32align&quot;</tt> configuration probe on <font SIZE="-1">ARM</font> has been fixed.</dl>
<h3>Compilation improvements</h3>
<dl>
<dt>&bull;</p>
<dd> An &quot;<tt>&quot;incompatible operand types&quot;</tt>&quot; error in ternary expressions when building with <tt>&quot;clang&quot;</tt> has been fixed.</p>
<dt>&bull;</p>
<dd> Perl now skips setuid <tt>&quot;File::Copy&quot;</tt> tests on partitions it detects to be mounted as <tt>&quot;nosuid&quot;</tt>.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> A possible segfault in the <tt>&quot;T_PRTOBJ&quot;</tt> default typemap has been fixed.</p>
<dt>&bull;</p>
<dd> A possible memory leak when using <code>caller()</code> to set <tt>@DB::args</tt> has been fixed.</p>
<dt>&bull;</p>
<dd> Several memory leaks when loading <font SIZE="-1">XS</font> modules were fixed.</p>
<dt>&bull;</p>
<dd> <tt>&quot;unpack()&quot;</tt> now handles scalar context correctly for <tt>%32H</tt> and <tt>%32u</tt>, fixing a potential crash. <tt>&quot;split()&quot;</tt> would crash because the third item on the stack wasn&#8217;t the regular expression it expected. <tt>&quot;unpack(&quot;%2H&quot;, ...)&quot;</tt> would return both the unpacked result and the checksum on the stack, as would <tt>&quot;unpack(&quot;%2u&quot;, ...)&quot;</tt>. [perl #73814] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Ticket/Display.html?id=73814">http://rt.perl.org/rt3/Ticket/Display.html?id=73814</a>&gt;</p>
<dt>&bull;</p>
<dd> Perl now avoids using memory after calling <tt>&quot;free()&quot;</tt> in <i>pp_require</i> when there are CODEREFs in <tt>@INC</tt>.</p>
<dt>&bull;</p>
<dd> A bug that could cause &quot;<tt>&quot;Unknown error&quot;</tt>&#8220; messages when &#8221;<tt>&quot;call_sv(code, G_EVAL)&quot;</tt>&quot; is called from an <font SIZE="-1">XS</font> destructor has been fixed.</p>
<dt>&bull;</p>
<dd> The implementation of the <tt>&quot;open $fh, '&gt;' \$buffer&quot;</tt> feature now supports get/set magic and thus tied buffers correctly.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;pp_getc&quot;</tt>, <tt>&quot;pp_tell&quot;</tt>, and <tt>&quot;pp_eof&quot;</tt> opcodes now make room on the stack for their return values in cases where no argument was passed in.</p>
<dt>&bull;</p>
<dd> When matching unicode strings under some conditions inappropriate backtracking would result in a <tt>&quot;Malformed UTF-8 character (fatal)&quot;</tt> error. This should no longer occur. See [perl #75680] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=75680">http://rt.perl.org/rt3/Public/Bug/Display.html?id=75680</a>&gt;</dl>
<h2>Platform Specific Notes</h2>
<h3><font SIZE="-1">AIX</font></h3>
<dl>
<dt>&bull;</p>
<dd> <i></i><font SIZE="-1"><i>README</i></font><i>.aix</i> has been updated with information about the <font SIZE="-1">XL C/C<font SIZE="-2">++</font> V11</font> compiler suite.</dl>
<h3>Windows</h3>
<dl>
<dt>&bull;</p>
<dd> When building Perl with the mingw64 x64 cross-compiler <tt>&quot;incpath&quot;</tt>, <tt>&quot;libpth&quot;</tt>, <tt>&quot;ldflags&quot;</tt>, <tt>&quot;lddlflags&quot;</tt> and <tt>&quot;ldflags_nolargefiles&quot;</tt> values in <i>Config.pm</i> and <i>Config_heavy.pl</i> were not previously being set correctly because, with that compiler, the include and lib directories are not immediately below <tt>&quot;$(CCHOME)&quot;</tt>.</dl>
<h3><font SIZE="-1">VMS</font></h3>
<dl>
<dt>&bull;</p>
<dd> <i>git_version.h</i> is now installed on <font SIZE="-1">VMS.</font> This was an oversight in v5.12.0 which caused some extensions to fail to build.</p>
<dt>&bull;</p>
<dd> Several memory leaks in <code>stat()</code> have been fixed.</p>
<dt>&bull;</p>
<dd> A memory leak in <tt>&quot;Perl_rename()&quot;</tt> due to a double allocation has been fixed.</p>
<dt>&bull;</p>
<dd> A memory leak in <tt>&quot;vms_fid_to_name()&quot;</tt> (used by <tt>&quot;realpath()&quot;</tt> and <tt>&quot;realname()&quot;</tt>) has been fixed.</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.12.2 represents approximately three months of development since Perl 5.12.1 and contains approximately 2,000 lines of changes across 100 files from 36 authors. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.12.2: </p>
<p> Abigail, Ævar Arnfjörð Bjarmason, Ben Morrow, brian d foy, Brian Phillips, Chas. Owens, Chris &#8216;BinGOs&#8217; Williams, Chris Williams, Craig A. Berry, Curtis Jewell, Dan Dascalescu, David Golden, David Mitchell, Father Chrysostomos, Florian Ragwitz, George Greer, H.Merijn Brand, Jan Dubois, Jesse Vincent, Jim Cromie, Karl Williamson, Lars Dɪᴇᴄᴋᴏᴡ 迪拉斯, Leon Brocard, Maik Hentsche, Matt S Trout, Nicholas Clark, Rafael Garcia-Suarez, Rainer Tammer, Ricardo Signes, Salvador Ortiz Garcia, Sisyphus, Slaven Rezic, Steffen Mueller, Tony Cook, Vincent Pit and Yves Orton.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font></p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
<dt><a href="#lbAT">Acknowledgements</a></p>
<dd>
<dt><a href="#lbAU">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbAV">SEE ALSO</a></p>
<dd></dl>
