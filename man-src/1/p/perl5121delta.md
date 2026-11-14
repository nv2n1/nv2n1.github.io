---
title: "perl5121delta(1)"
name: "perl5121delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5121delta/"
description: "perl5121delta – what is new for perl v5.12.1"
---

<h2 class="name">NAME</h2>
<p> perl5121delta &#8211; what is new for perl v5.12.1 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.12.0 release and the 5.12.1 release. </p>
<p> If you are upgrading from an earlier release such as 5.10.1, first read perl5120delta, which describes differences between 5.10.1 and 5.12.0.</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.12.0. If any incompatibilities with 5.12.0 exist, they are bugs. Please report them.</p>
<h2>Core Enhancements</h2>
<p> Other than the bug fixes listed below, there should be no user-visible changes to the core language in this release.</p>
<h2>Modules and Pragmata</h2>
<h3>Pragmata Changes</h3>
<dl>
<dt>&bull;</p>
<dd> We fixed exporting of <tt>&quot;is_strict&quot;</tt> and <tt>&quot;is_lax&quot;</tt> from version. </p>
<p> These were being exported with a wrapper that treated them as method calls, which caused them to fail. They are just functions, are documented as such, and should never be subclassed, so this patch just exports them directly as functions without the wrapper.</dl>
<h3>Updated Modules</h3>
<dl>
<dt>&bull;</p>
<dd> We upgraded <font SIZE="-1">CGI</font>.pm to version 3.49 to incorporate fixes for regressions introduced in the release we shipped with Perl 5.12.0.</p>
<dt>&bull;</p>
<dd> We upgraded Pod::Simple to version 3.14 to get an improvement to \C\&lt;\&lt; \&gt;\&gt; parsing.</p>
<dt>&bull;</p>
<dd> We made a small fix to the <font SIZE="-1">CPANPLUS</font> test suite to fix an occasional spurious test failure.</p>
<dt>&bull;</p>
<dd> We upgraded Safe to version 2.27 to wrap coderefs returned by <tt>&quot;reval()&quot;</tt> and <tt>&quot;rdo()&quot;</tt>.</dl>
<h2>Changes to Existing Documentation</h2>
<dl>
<dt>&bull;</p>
<dd> We added the new maintenance release policy to perlpolicy.pod</p>
<dt>&bull;</p>
<dd> We&#8217;ve clarified the multiple-angle-bracket construct in the spec for <font SIZE="-1">POD</font> in perlpodspec</p>
<dt>&bull;</p>
<dd> We added a missing explanation for a warning about <tt>&quot;:=&quot;</tt> to perldiag.pod</p>
<dt>&bull;</p>
<dd> We removed a false claim in perlunitut that all text strings are Unicode strings in Perl.</p>
<dt>&bull;</p>
<dd> We updated the Github mirror link in perlrepository to mirrors/perl, not github/perl</p>
<dt>&bull;</p>
<dd> We fixed a minor error in perl5114delta.pod.</p>
<dt>&bull;</p>
<dd> We replaced a mention of the now-obsolete Switch.pm with <i>given</i>/<i>when</i>.</p>
<dt>&bull;</p>
<dd> We improved documentation about <i></i>$sitelibexp<i>/sitecustomize.pl</i> in perlrun.</p>
<dt>&bull;</p>
<dd> We corrected perlmodlib.pod which had unintentionally omitted a number of modules.</p>
<dt>&bull;</p>
<dd> We updated the documentation for &#8216;require&#8217; in perlfunc.pod relating to putting Perl code in <tt>@INC</tt>.</p>
<dt>&bull;</p>
<dd> We reinstated some erroneously-removed documentation about quotemeta in perlfunc.</p>
<dt>&bull;</p>
<dd> We fixed an <i>a2p</i> example in perlutil.pod.</p>
<dt>&bull;</p>
<dd> We filled in a blank in perlport.pod with the release date of Perl 5.12.</p>
<dt>&bull;</p>
<dd> We fixed broken links in a number of perldelta files.</p>
<dt>&bull;</p>
<dd> The documentation for Carp.pm incorrectly stated that the <tt>$Carp::Verbose</tt> variable makes cluck generate stack backtraces.</p>
<dt>&bull;</p>
<dd> We fixed a number of typos in Pod::Functions</p>
<dt>&bull;</p>
<dd> We improved documentation of case-changing functions in perlfunc.pod</p>
<dt>&bull;</p>
<dd> We corrected perlgpl.pod to contain the correct version of the <font SIZE="-1">GNU</font> General Public License.</dl>
<h2>Testing</h2>
<h3>Testing Improvements</h3>
<dl>
<dt>&bull;</p>
<dd> <i>t/op/sselect.t</i> is now less prone to clock jitter during timing checks on Windows. </p>
<p> <code>sleep()</code> time on Win32 may be rounded down to multiple of the clock tick interval.</p>
<dt>&bull;</p>
<dd> <i>lib/blib.t</i> and <i>lib/locale.t</i>: Fixes for test failures on Darwin/PPC</p>
<dt>&bull;</p>
<dd> <i>perl5db.t</i>: Fix for test failures when <tt>&quot;Term::ReadLine::Gnu&quot;</tt> is installed.</dl>
<h2>Installation and Configuration Improvements</h2>
<h3>Configuration improvements</h3>
<dl>
<dt>&bull;</p>
<dd> We updated <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> with notes about how to deal with broken <i>dbm.h</i> on OpenSUSE (and possibly other platforms)</dl>
<h2>Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> A bug in how we process filetest operations could cause a segfault. Filetests don&#8217;t always expect an op on the stack, so we now use TOPs only if we&#8217;re sure that we&#8217;re not stat&#8217;ing the _ filehandle. This is indicated by OPf_KIDS (as checked in ck_ftst). </p>
<p> See also: &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=74542">http://rt.perl.org/rt3/Public/Bug/Display.html?id=74542</a>&gt;</p>
<dt>&bull;</p>
<dd> When deparsing a nextstate op that has both a change of package (relative to the previous nextstate) and a label, the package declaration is now emitted first, because it is syntactically impermissible for a label to prefix a package declaration.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">XSUB</font>.h now correctly redefines fgets under <font SIZE="-1">PERL_IMPLICIT_SYS</font> </p>
<p> See also: &lt;<a rel="nofollow" href="http://rt.cpan.org/Public/Bug/Display.html?id=55049">http://rt.cpan.org/Public/Bug/Display.html?id=55049</a>&gt;</p>
<dt>&bull;</p>
<dd> utf8::is_utf8 now respects <font SIZE="-1">GMAGIC</font> (e.g. <tt>$1</tt>)</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">XS</font> code using <tt>&quot;fputc()&quot;</tt> or <tt>&quot;fputs()&quot;</tt>: on Windows could cause an error due to their arguments being swapped. </p>
<p> See also: &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=72704">http://rt.perl.org/rt3/Public/Bug/Display.html?id=72704</a>&gt;</p>
<dt>&bull;</p>
<dd> We fixed a small bug in <code>lex_stuff_pvn()</code> that caused spurious syntax errors in an obscure situation. It happened when stuffing was performed on the last line of a file and the line ended with a statement that lacked a terminating semicolon. </p>
<p> See also: &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=74006">http://rt.perl.org/rt3/Public/Bug/Display.html?id=74006</a>&gt;</p>
<dt>&bull;</p>
<dd> We fixed a bug that could cause \N{} constructs followed by a single . to be parsed incorrectly. </p>
<p> See also: &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=74978">http://rt.perl.org/rt3/Public/Bug/Display.html?id=74978</a>&gt;</p>
<dt>&bull;</p>
<dd> We fixed a bug that caused when(scalar) without an argument not to be treated as a syntax error. </p>
<p> See also: &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=74114">http://rt.perl.org/rt3/Public/Bug/Display.html?id=74114</a>&gt;</p>
<dt>&bull;</p>
<dd> We fixed a regression in the handling of labels immediately before string evals that was introduced in Perl 5.12.0. </p>
<p> See also: &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=74290">http://rt.perl.org/rt3/Public/Bug/Display.html?id=74290</a>&gt;</p>
<dt>&bull;</p>
<dd> We fixed a regression in case-insensitive matching of folded characters in regular expressions introduced in Perl 5.10.1. </p>
<p> See also: &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=72998">http://rt.perl.org/rt3/Public/Bug/Display.html?id=72998</a>&gt;</dl>
<h2>Platform Specific Notes</h2>
<h3>HP-UX</h3>
<dl>
<dt>&bull;</p>
<dd> Perl now allows -Duse64bitint without promoting to use64bitall on HP-UX</dl>
<h3><font SIZE="-1">AIX</font></h3>
<dl>
<dt>&bull;</p>
<dd> Perl now builds on <font SIZE="-1">AIX 4.2</font> </p>
<p> The changes required work around <font SIZE="-1">AIX 4</font>.2s&#8217; lack of support for IPv6, and limited support for <font SIZE="-1">POSIX</font> <tt>&quot;sigaction()&quot;</tt>.</dl>
<h3>FreeBSD 7</h3>
<dl>
<dt>&bull;</p>
<dd> FreeBSD 7 no longer contains <i>/usr/bin/objformat</i>. At build time, Perl now skips the <i>objformat</i> check for versions 7 and higher and assumes <font SIZE="-1">ELF.</font></dl>
<h3><font SIZE="-1">VMS</font></h3>
<dl>
<dt>&bull;</p>
<dd> It&#8217;s now possible to build extensions on older (pre 7.3-2) <font SIZE="-1">VMS</font> systems. </p>
<p> <font SIZE="-1">DCL</font> symbol length was limited to 1K up until about seven years or so ago, but there was no particularly deep reason to prevent those older systems from configuring and building Perl.</p>
<dt>&bull;</p>
<dd> We fixed the previously-broken <tt>&quot;-Uuseperlio&quot;</tt> build on <font SIZE="-1">VMS.</font> </p>
<p> We were checking a variable that doesn&#8217;t exist in the non-default case of disabling perlio. Now we only look at it when it exists.</p>
<dt>&bull;</p>
<dd> We fixed the -Uuseperlio command-line option in configure.com. </p>
<p> Formerly it only worked if you went through all the questions interactively and explicitly answered no.</dl>
<h2>Known Problems</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;List::Util::first&quot;</tt> misbehaves in the presence of a lexical <tt>$_</tt> (typically introduced by <tt>&quot;my $_&quot;</tt> or implicitly by <tt>&quot;given&quot;</tt>). The variable which gets set for each iteration is the package variable <tt>$_</tt>, not the lexical <tt>$_</tt>. </p>
<p> A similar issue may occur in other modules that provide functions which take a block as their first argument, like </p>
<pre>
    foo { ... $_ ...} list
</pre>
<p> See also: &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=67694">http://rt.perl.org/rt3/Public/Bug/Display.html?id=67694</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;Module::Load::Conditional&quot;</tt> and <tt>&quot;version&quot;</tt> have an unfortunate interaction which can cause <tt>&quot;CPANPLUS&quot;</tt> to crash when it encounters an unparseable version string. Upgrading to <tt>&quot;CPANPLUS&quot;</tt> 0.9004 or <tt>&quot;Module::Load::Conditional&quot;</tt> 0.38 from <font SIZE="-1">CPAN</font> will resolve this issue.</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.12.1 represents approximately four weeks of development since Perl 5.12.0 and contains approximately 4,000 lines of changes across 142 files from 28 authors. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.12.1: </p>
<p> Ævar Arnfjörð Bjarmason, Chris Williams, chromatic, Craig A. Berry, David Golden, Father Chrysostomos, Florian Ragwitz, Frank Wiegand, Gene Sullivan, Goro Fuji, H.Merijn Brand, James E Keenan, Jan Dubois, Jesse Vincent, Josh ben Jore, Karl Williamson, Leon Brocard, Michael Schwern, Nga Tang Chan, Nicholas Clark, Niko Tyni, Philippe Bruhat, Rafael Garcia-Suarez, Ricardo Signes, Steffen Mueller, Todd Rinaldo, Vincent Pit and Zefram.</p>
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
<dt><a href="#lbAT">Known Problems</a></p>
<dd>
<dt><a href="#lbAU">Acknowledgements</a></p>
<dd>
<dt><a href="#lbAV">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbAW">SEE ALSO</a></p>
<dd></dl>
