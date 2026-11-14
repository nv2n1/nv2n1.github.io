---
title: "perl5115delta(1)"
name: "perl5115delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5115delta/"
description: "perl5115delta – what is new for perl v5.11.5"
---

<h2 class="name">NAME</h2>
<p> perl5115delta &#8211; what is new for perl v5.11.5 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.11.4 release and the 5.11.5 release. </p>
<p> If you are upgrading from an earlier release such as 5.11.3, first read perl5114delta, which describes differences between 5.11.3 and 5.11.4.</p>
<h2>Core Enhancements</h2>
<h3>32-bit limit on substr arguments removed</h3>
<p> The 32-bit limit on <tt>&quot;substr&quot;</tt> arguments has now been removed. The full range of the system&#8217;s signed and unsigned integers is now available for the <tt>&quot;pos&quot;</tt> and <tt>&quot;len&quot;</tt> arguments.</p>
<h2>Modules and Pragmata</h2>
<h3>Pragmata Changes</h3>
<dl>
<dt>&quot;version&quot;</p>
<dd> Upgraded from version 0.81 to 0.82. </p>
<p> The <tt>&quot;is_lax&quot;</tt> and <tt>&quot;is_strict&quot;</tt> functions can now be optionally exported to the caller&#8217;s namespace and are also now documented. </p>
<p> Undefined version objects are now uninitialized with zero rather than <tt>&quot;undef&quot;</tt>.</dl>
<h3>Updated Modules</h3>
<dl>
<dt>&quot;B::Debug&quot;</p>
<dd> Upgraded from version 1.11 to 1.12.</p>
<dt>&quot;CPAN&quot;</p>
<dd> Upgraded from version 1.94_53 to 1.94_56. </p>
<p> This resolves <font SIZE="-1">RT</font> #72362, in which <font SIZE="-1">CPAN</font> was ignoring <tt>&quot;configure_requires&quot;</tt>, and <font SIZE="-1">RT</font> #72348, in which the command <tt>&quot;o conf init&quot;</tt> in the <font SIZE="-1">CPAN</font> shell could cause an exception to be thrown. </p>
<p> This module is also now built in a less specialized way, which resolves a problem that caused <tt>&quot;make&quot;</tt> after <tt>&quot;make clean&quot;</tt> to fail, fixing <font SIZE="-1">RT</font> #72218.</p>
<dt>&quot;CPANPLUS::Dist::Build&quot;</p>
<dd> Upgraded from version 0.44 to 0.46. </p>
<p> This makes the prereq resolving fall back to <i>_build/</i> querying if the <tt>&quot;prereq_data&quot;</tt> action fails.</p>
<dt>&quot;Pod::Perldoc&quot;</p>
<dd> Upgraded from version 3.15_01 to 3.15_02.</p>
<dt>&quot;Pod::Plainer&quot;</p>
<dd> Upgraded from version 1.01 to 1.02.</p>
<dt>&quot;Safe&quot;</p>
<dd> Upgraded from version 2.21 to 2.22. </p>
<p> This resolves <font SIZE="-1">RT</font> #72700, in which an exception thrown from a closure was getting lost.</p>
<dt>&quot;Socket&quot;</p>
<dd> Upgraded from version 1.85 to 1.86. </p>
<p> This makes the new Socket implementation of <tt>&quot;inet_pton&quot;</tt> consistent with the existing Socket6 implementation of <tt>&quot;inet_pton&quot;</tt>, fixing <font SIZE="-1">RT</font> #72884.</p>
<dt>&quot;podlators&quot;</p>
<dd> Upgraded from version 2.2.2 to 2.3.1.</dl>
<h2>Changes to Existing Documentation</h2>
<p> The syntax <tt>&quot;unless (EXPR) BLOCK else BLOCK&quot;</tt> is now documented as valid, as is the syntax <tt>&quot;unless (EXPR) BLOCK elsif (EXPR) BLOCK ... else BLOCK&quot;</tt>, although actually using the latter may not be the best idea for the readability of your source code.</p>
<h2>Installation and Configuration Improvements</h2>
<h3>Configuration improvements</h3>
<p> Support for SystemTap&#8217;s <tt>&quot;dtrace&quot;</tt> compatibility layer has been added and an issue with linking <tt>&quot;miniperl&quot;</tt> has been fixed in the process. </p>
<p> <tt>&quot;less -R&quot;</tt> is now used instead of <tt>&quot;less&quot;</tt> for <tt>&quot;groff&quot;</tt>&#8216;s new usage of <font SIZE="-1">ANSI</font> escape codes by setting <tt>$Config{less}</tt> (and thereby <tt>$Config{pager}</tt>, which fixes <font SIZE="-1">RT</font> #72156. </p>
<p> <font SIZE="-1">USE_PERL_ATOF</font> is now reported in the compile-time options listed by the <tt>&quot;-V&quot;</tt> switch.</p>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> Arbitrary whitespace is now allowed between <tt>&quot;NAME&quot;</tt> and <tt>&quot;VERSION&quot;</tt> in <tt>&quot;package NAME VERSION;&quot;</tt> statements. (Fixes <font SIZE="-1">RT</font> #72432)</p>
<dt>&bull;</p>
<dd> A panic caused by trying to load <tt>&quot;charnames&quot;</tt> when the parser is already in error (e.g. by a missing <tt>&quot;my&quot;</tt> under <tt>&quot;use strict;&quot;</tt>) is now averted. This was a regression since Perl 5.10.0. (Fixes <font SIZE="-1">RT</font> #72590)</p>
<dt>&bull;</p>
<dd> Reading <tt>$!</tt> no longer causes a <font SIZE="-1">SEGV</font> for out of range <tt>&quot;errno&quot;</tt> values. (Fixes <font SIZE="-1">RT</font> #72850)</p>
<dt>&bull;</p>
<dd> A possible <font SIZE="-1">SEGV</font> in <tt>&quot;/\N{...}/&quot;</tt> has been fixed. This was a regression since Perl 5.10.</p>
<dt>&bull;</p>
<dd> A possible <font SIZE="-1">SEGV</font> when freeing a scalar that was upgraded to an <tt>&quot;SVt_REGEXP&quot;</tt> type from a simple(r) scalar has been fixed.</p>
<dt>&bull;</p>
<dd> A type conversion bug in <tt>&quot;gmtime64&quot;</tt> that caused it to break around <tt>&quot;2**48&quot;</tt> has been fixed.</p>
<dt>&bull;</p>
<dd> Interpolating a regex that makes use of the <tt>&quot;charnames&quot;</tt> pragma will no longer cause a run-time error. (Fixes <font SIZE="-1">RT</font> #56444)</p>
<dt>&bull;</p>
<dd> Array references assigned to <tt>*Foo::ISA</tt> now have the necessary magic added to them to catch any further updates to the new <tt>@ISA</tt>. (Fixes <font SIZE="-1">RT</font> #72866)</p>
<dt>&bull;</p>
<dd> Filehandles are now always blessed into <tt>&quot;IO::File&quot;</tt>, which, together with some suitable manipulation of <tt>@IO::File::ISA</tt>, fixes a breakage introduced in Perl 5.11.3 by a change that always blessed filehandles into <tt>&quot;IO::Handle&quot;</tt> rather than checking for <tt>&quot;FileHandle&quot;</tt> first.</p>
<dt>&bull;</p>
<dd> A change in the behaviour of <tt>&quot;warnings::enabled&quot;</tt> and <tt>&quot;warnings::warnif&quot;</tt> in Perl 5.10.0 that wasn&#8217;t documented at the time is now documented in perl5100delta. (Fixes <font SIZE="-1">RT</font> #62522)</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">RT</font> #71504 is now fixed by simply skipping the tests that failed on OpenBSD with ithreads and perlio.</dl>
<h2>New or Changed Diagnostics</h2>
<dl>
<dt>&bull;</p>
<dd> The fatal error <tt>&quot;Malformed UTF-8 returned by \N&quot;</tt> is now produced if the <tt>&quot;charnames&quot;</tt> handler returns malformed <font SIZE="-1">UTF-8</font>.</p>
<dt>&bull;</p>
<dd> If an unresolved named character or sequence was encountered when compiling a regex pattern then the fatal error <tt>&quot;\N{NAME} must be resolved by the lexer&quot;</tt> is now produced. This can happen, for example, when using a single-quotish context like <tt>&quot;$re = '\N{SPACE}'; $re;&quot;</tt>. See perldiag for more examples of how the lexer can get bypassed.</p>
<dt>&bull;</p>
<dd> The fatal error <tt>&quot;Invalid hexadecimal number in \N{U+...}&quot;</tt> will be produced if the character constant represented by <tt>&quot;...&quot;</tt> is not a valid hexadecimal number.</p>
<dt>&bull;</p>
<dd> The new meaning of <tt>&quot;\N&quot;</tt> as <tt>&quot;[^
]&quot;</tt> is not valid in a bracketed character class, just like <tt>&quot;.&quot;</tt> in a character class loses its special meaning, and will cause the fatal error <tt>&quot;\N in a character class must be a named character: \N{...}&quot;</tt>.</p>
<dt>&bull;</p>
<dd> The rules on what is legal for the <tt>&quot;...&quot;</tt> in <tt>&quot;\N{...}&quot;</tt> have been tightened up so that unless the <tt>&quot;...&quot;</tt> begins with an alphabetic character and continues with a combination of alphanumerics, dashes, spaces, parentheses or colons then the warning <tt>&quot;Deprecated character(s) in \N{...} starting at '%s'&quot;</tt> is now issued.</p>
<dt>&bull;</p>
<dd> The warning <tt>&quot;Using just the first characters returned by \N{}&quot;</tt> will be issued if the <tt>&quot;charnames&quot;</tt> handler returns a sequence of characters which exceeds the limit of the number of characters that can be used. The message will indicate which characters were used and which were discarded.</p>
<dt>&bull;</p>
<dd> Currently, all but the first of the several characters that the <tt>&quot;charnames&quot;</tt> handler may return are discarded when used in a regular expression pattern bracketed character class. If this happens then the warning <tt>&quot;Using just the first character returned by \N{} in character class&quot;</tt> will be issued.</p>
<dt>&bull;</p>
<dd> The warning <tt>&quot;Missing right brace on \N{} or unescaped left brace after \N. Assuming the latter&quot;</tt> will be issued if Perl encounters a <tt>&quot;\N{&quot;</tt> but doesn&#8217;t find a matching <tt>&quot;}&quot;</tt>. In this case Perl doesn&#8217;t know if it was mistakenly omitted, or if &#8220;match non-newline&#8221; followed by &quot;match a <tt>&quot;{&quot;</tt>&quot; was desired. It assumes the latter because that is actually a valid interpretation as written, unlike the other case. If you meant the former, you need to add the matching right brace. If you did mean the latter, you can silence this warning by writing instead <tt>&quot;\N\{&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;gmtime&quot;</tt> and <tt>&quot;localtime&quot;</tt> called with numbers smaller than they can reliably handle will now issue the warnings <tt>&quot;gmtime(%.0f) too small&quot;</tt> and <tt>&quot;localtime(%.0f) too small&quot;</tt>.</dl>
<h2>New Tests</h2>
<dl>
<dt><i>t/op/filehandle.t</i></p>
<dd> Tests some suitably portable filetest operators to check that they work as expected, particularly in the light of some internal changes made in how filehandles are blessed.</p>
<dt><i>t/op/time_loop.t</i></p>
<dd> Tests that times greater than <tt>&quot;2**63&quot;</tt>, which can now be handed to <tt>&quot;gmtime&quot;</tt> and <tt>&quot;localtime&quot;</tt>, do not cause an internal overflow or an excessively long loop.</dl>
<h2>Known Problems</h2>
<p> Perl 5.11.5 is a development release leading up to Perl 5.12.0. Some notable known problems found in 5.11.5 are listed as dependencies of <font SIZE="-1">RT</font> #69710, the Perl 5 version 12 meta-ticket.</p>
<h2>Acknowledgements</h2>
<p> Perl 5.11.5 represents approximately one month of development since Perl 5.11.4 and contains 9618 lines of changes across 151 files from 33 authors and committers: </p>
<p> var Arnfjo.rd<i>&#8211;</i> Bjarmason, Abigail, brian d foy, Chris Williams, David Golden, David Mitchell, Eric Brine, Frank Wiegand, Gisle Aas, H.Merijn Brand, Jan Dubois, Jesse Vincent, Jim Cromie, John Peacock, Josh ben Jore, Karl Williamson, Marcus Holland-Moritz, Michael G Schwern, Nicholas Clark, Offer Kaye, Philippe Bruhat (BooK), Rafael Garcia-Suarez, Reini Urban, Ricardo Signes, Robin Barker, Slaven Rezic, Steffen Mueller, Steve Hay, Steve Peters, Tim Bunce, Todd Rinaldo, Tony Cook and Vincent Pit. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analyzed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN</font>.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
