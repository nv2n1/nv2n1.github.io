---
title: "perl5111delta(1)"
name: "perl5111delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5111delta/"
description: "perl5111delta – what is new for perl v5.11.1"
---

<h2 class="name">NAME</h2>
<p> perl5111delta &#8211; what is new for perl v5.11.1 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.11.0 release and the 5.11.1 release.</p>
<h2>Incompatible Changes</h2>
<dl>
<dt>&bull;</p>
<dd> The boolkeys op moved to the group of hash ops. This breaks binary compatibility.</p>
<dt>&bull;</p>
<dd> <tt>&quot;\s&quot;</tt> <tt>&quot;\w&quot;</tt> and <tt>&quot;\d&quot;</tt> once again have the semantics they had in Perl 5.8.x.</dl>
<h2>Core Enhancements</h2>
<h3>Add package NAME VERSION syntax</h3>
<p> This new syntax allows a module author to set the <tt>$VERSION</tt> of a namespace when the namespace is declared with &#8216;package&#8217;. It eliminates the need for <tt>&quot;our $VERSION = ...&quot;</tt> and similar constructs. E.g. </p>
<pre>
      package Foo::Bar 1.23;
      # $Foo::Bar::VERSION == 1.23
</pre>
<p> There are several advantages to this:</p>
<dl>
<dt>&bull;</p>
<dd> <tt>$VERSION</tt> is parsed in <i>exactly</i> the same way as <tt>&quot;use NAME VERSION&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>$VERSION</tt> is set at compile time</p>
<dt>&bull;</p>
<dd> Eliminates <tt>&quot;$VERSION = ...&quot;</tt> and <tt>&quot;eval $VERSION&quot;</tt> clutter</p>
<dt>&bull;</p>
<dd> As it requires <font SIZE="-1">VERSION</font> to be a numeric literal or v-string literal, it can be statically parsed by toolchain modules without <tt>&quot;eval&quot;</tt> the way <font SIZE="-1">MM-</font>&gt;parse_version does for <tt>&quot;$VERSION = ...&quot;</tt></p>
<dt>&bull;</p>
<dd> Alpha versions with underscores do not need to be quoted; static parsing will preserve the underscore, but during compilation, Perl will remove underscores as it does for all numeric literals </p>
<p> It does not break old code with only <tt>&quot;package NAME&quot;</tt>, but code that uses <tt>&quot;package NAME VERSION&quot;</tt> will need to be restricted to perl 5.11.X or newer This is analogous to the change to <tt>&quot;open&quot;</tt> from two-args to three-args. Users requiring the latest Perl will benefit, and perhaps N years from now it will become standard practice when Perl 5.12 is targeted the way that 5.6 is today.</dl>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules</h3>
<dl>
<dt>&bull;</p>
<dd> Upgrade to Test-Simple 0.94</p>
<dt>&bull;</p>
<dd> Upgrade to Storable 2.21</p>
<dt>&bull;</p>
<dd> Upgrade to Pod-Simple 3.08</p>
<dt>&bull;</p>
<dd> Upgrade to Parse-CPAN-Meta 1.40</p>
<dt>&bull;</p>
<dd> Upgrade to ExtUtils-Manifest 1.57</p>
<dt>&bull;</p>
<dd> Upgrade to ExtUtils-CBuilder 0.260301</p>
<dt>&bull;</p>
<dd> Upgrade to <font SIZE="-1">CGI</font>.pm-3.48</p>
<dt>&bull;</p>
<dd> Upgrade <font SIZE="-1">CPANPLUS</font> to <font SIZE="-1">CPAN</font> version 0.89_02</p>
<dt>&bull;</p>
<dd> Upgrade to threads::shared 1.32</p>
<dt>&bull;</p>
<dd> Upgrade ExtUtils::ParseXS to 2.21</p>
<dt>&bull;</p>
<dd> Upgrade File::Path to 2.08 (and add taint.t test)</p>
<dt>&bull;</p>
<dd> Upgrade Module::CoreList to 2.20</p>
<dt>&bull;</p>
<dd> Updated Object::Accessor to0.36</dl>
<h2>New Documentation</h2>
<dl>
<dt>&bull;</p>
<dd> perlpolicy extends the &#8220;Social contract about contributed modules&#8221; into the beginnings of a document on Perl porting policies.</dl>
<h2>Changes to Existing Documentation</h2>
<dl>
<dt>Documentation for $1 in perlvar.pod clarified</p>
<dd></dl>
<h2>Performance Enhancements</h2>
<dl>
<dt>&quot;if (%foo)&quot; has been optimized to be faster than &quot;if (keys %foo)&quot;</p>
<dd></dl>
<h2>Platform Specific Notes</h2>
<dl>
<dt>Darwin (Mac <font SIZE="-1">OS</font> X)</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Skip testing the be_BY.CP1131 locale on Darwin 10 (Mac <font SIZE="-1">OS</font> X 10.6), as it&#8217;s still buggy.</p>
<dt>&bull;</p>
<dd> Correct infelicities in the regexp used to identify buggy locales on Darwin 8 and 9 (Mac <font SIZE="-1">OS</font> X 10.4 and 10.5, respectively).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>DragonFly <font SIZE="-1">BSD</font></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Fix thread library selection [perl #69686]</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Win32</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Initial support for mingw64 is now available</p>
<dt>&bull;</p>
<dd> Various bits of Perl&#8217;s build infrastructure are no longer converted to win32 line endings at release time. If this hurts you, please speak up.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> Perl now properly returns a syntax error instead of segfaulting if <tt>&quot;each&quot;</tt>, <tt>&quot;keys&quot;</tt> or <tt>&quot;values&quot;</tt> is used without an argument</p>
<dt>&bull;</p>
<dd> <tt>&quot;tell()&quot;</tt> now fails properly if called without an argument and when no previous file was read </p>
<p> <tt>&quot;tell()&quot;</tt> now returns <tt>&quot;-1&quot;</tt>, and sets errno to <tt>&quot;EBADF&quot;</tt>, thus restoring the 5.8.x behaviour</p>
<dt>&bull;</p>
<dd> overload no longer implicitly unsets fallback on repeated &#8216;use overload&#8217; lines</p>
<dt>&bull;</p>
<dd> <i>POSIX::strftime()</i> can now handle Unicode characters in the format string.</p>
<dt>&bull;</p>
<dd> The Windows <i>select()</i> implementation now supports all empty <tt>&quot;fd_set&quot;</tt>s more correctly.</dl>
<h2>New or Changed Diagnostics</h2>
<dl>
<dt>&bull;</p>
<dd> The &#8216;syntax&#8217; category was removed from 5 warnings that should only be in &#8216;deprecated&#8217;.</p>
<dt>&bull;</p>
<dd> Three fatal pack/unpack error messages have been normalized to &#8220;panic: <tt>%s</tt>&#8221;</p>
<dt>&bull;</p>
<dd> &#8220;Unicode character is illegal&#8221; has been rephrased to be more accurate </p>
<p> It now reads <tt>&quot;Unicode non-character is illegal in interchange&quot;</tt> and the perldiag documentation has been expanded a bit.</p>
<dt>&bull;</p>
<dd> Perl now defaults to issuing a warning if a deprecated language feature is used. </p>
<p> To disable this feature in a given lexical scope, you should use <tt>&quot;no warnings 'deprecated';&quot;</tt> For information about which language features are deprecated and explanations of various deprecation warnings, please see perldiag</dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</p>
<dd> Significant cleanups to core tests to ensure that language and interpreter features are not used before they&#8217;re tested.</p>
<dt>&bull;</p>
<dd> <tt>&quot;make test_porting&quot;</tt> now runs a number of important pre-commit checks which might be of use to anyone working on the Perl core.</p>
<dt>&bull;</p>
<dd> <i>t/porting/podcheck.t</i> automatically checks the well-formedness of <font SIZE="-1">POD</font> found in all .pl, .pm and .pod files in the <i></i><font SIZE="-1"><i>MANIFEST</i></font><i></i>, other than in dual-lifed modules which are primarily maintained outside the Perl core.</p>
<dt>&bull;</p>
<dd> <i>t/porting/manifest.t</i> now tests that all files listed in <font SIZE="-1">MANIFEST</font> are present.</dl>
<h2>Known Problems</h2>
<dl>
<dt>Untriaged test crashes on Windows 2000</p>
<dd> Several porters have reported mysterious crashes when Perl&#8217;s entire test suite is run after a build on certain Windows 2000 systems. When run by hand, the individual tests reportedly work fine.</p>
<dt>Known test failures on <font SIZE="-1">VMS</font></p>
<dd> Perl 5.11.1 fails a small set of core and <font SIZE="-1">CPAN</font> tests as of this release. With luck, that&#8217;ll be sorted out for 5.11.2</dl>
<h2>Errata for 5.11.0</h2>
<dl>
<dt>The Perl 5.11.0 release notes incorrectly described &#8216;delete local&#8217;</p>
<dd></dl>
<h2>Acknowledgements</h2>
<p> Perl 5.11.1 represents approximately 3 weeks development since Perl 5.11.0 contains 22,000 lines of changes across 396 files from 26 authors and committers: </p>
<p> Abigail, Alex Vandiver, brian d foy, Chris Williams, Craig A. Berry, David Fifield, David Golden, demerphq, Eric Brine, Geoffrey T. Dairiki, George Greer, H.Merijn Brand, Jan Dubois, Jerry D. Hedden, Jesse Vincent, Josh ben Jore, Max Maischein, Nicholas Clark, Rafael Garcia-Suarez, Simon Schubert, Sisyphus, Smylers, Steve Hay, Steve Peters, Vincent Pit and Yves Orton. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN</font>.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
