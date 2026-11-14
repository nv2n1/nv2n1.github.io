---
title: "perl5181delta(1)"
name: "perl5181delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5181delta/"
---

<h2 class="name">NAME</h2>
 

 perl5181delta - what is new for perl v5.18.1 

<h2>DESCRIPTION</h2>

 This document describes differences between the 5.18.0 release and the 5.18.1 release. 

 If you are upgrading from an earlier release such as 5.16.0, first read perl5180delta, which describes differences between 5.16.0 and 5.18.0.

<h2>Incompatible Changes</h2>

 There are no changes intentionally incompatible with 5.18.0 If any exist, they are bugs, and we request that you submit a report. See ``Reporting Bugs'' below.

<h2>Modules and Pragmata</h2>

<h3>Updated Modules and Pragmata</h3>

<dl>
<dt>&bull;
<dd> B has been upgraded from 1.42 to 1.42_01, fixing bugs related to lexical subroutines.
<dt>&bull;
<dd> Digest::SHA has been upgraded from 5.84 to 5.84_01, fixing a crashing bug. [<font SIZE="-1">RT</font> #118649]
<dt>&bull;
<dd> Module::CoreList has been upgraded from 2.89 to 2.96.</dl>

<h2>Platform Support</h2>

<h3>Platform-Specific Notes</h3>

<dl>
<dt><font SIZE="-1">AIX</font>
<dd> A rarely-encountered configuration bug in the <font SIZE="-1">AIX</font> hints file has been corrected.
<dt>MidnightBSD
<dd> After a patch to the relevant hints file, perl should now build correctly on MidnightBSD 0.4-RELEASE.</dl>

<h2>Selected Bug Fixes</h2>

<dl>
<dt>&bull;
<dd> Starting in v5.18.0, a construct like <tt>&quot;/[#](?{})/x&quot;</tt> would have its <tt>&quot;#&quot;</tt> incorrectly interpreted as a comment. The code block would be skipped, unparsed. This has been corrected.
<dt>&bull;
<dd> A number of memory leaks related to the new, experimental regexp bracketed character class feature have been plugged.
<dt>&bull;
<dd> The <font SIZE="-1">OP</font> allocation code now returns correctly aligned memory in all cases for <tt>&quot;struct pmop&quot;</tt>. Previously it could return memory only aligned to a 4-byte boundary, which is not correct for an ithreads build with 64 bit IVs on some 32 bit platforms. Notably, this caused the build to fail completely on sparc GNU/Linux. [<font SIZE="-1">RT</font> #118055]
<dt>&bull;
<dd> The debugger's <tt>&quot;man&quot;</tt> command been fixed. It was broken in the v5.18.0 release. The <tt>&quot;man&quot;</tt> command is aliased to the names <tt>&quot;doc&quot;</tt> and <tt>&quot;perldoc&quot;</tt> - all now work again.
<dt>&bull;
<dd> <tt>@_</tt> is now correctly visible in the debugger, fixing a regression introduced in v5.18.0's debugger. [<font SIZE="-1">RT</font> #118169]
<dt>&bull;
<dd> Fixed a small number of regexp constructions that could either fail to match or crash perl when the string being matched against was allocated above the 2GB line on 32-bit systems. [<font SIZE="-1">RT</font> #118175]
<dt>&bull;
<dd> Perl v5.16 inadvertently introduced a bug whereby calls to XSUBs that were not visible at compile time were treated as lvalues and could be assigned to, even when the subroutine was not an lvalue sub. This has been fixed. [perl #117947]
<dt>&bull;
<dd> Perl v5.18 inadvertently introduced a bug whereby dual-vars (i.e. variables with both string and numeric values, such as <tt>$!</tt> ) where the truthness of the variable was determined by the numeric value rather than the string value. [<font SIZE="-1">RT</font> #118159]
<dt>&bull;
<dd> Perl v5.18 inadvertently introduced a bug whereby interpolating mixed up- and down-graded <font SIZE="-1">UTF-8</font> strings in a regex could result in malformed <font SIZE="-1">UTF-8</font> in the pattern: specifically if a downgraded character in the range <tt>&quot;\x80..\xff&quot;</tt> followed a <font SIZE="-1">UTF-8</font> string, e.g. 

 <pre><code>
utf8::upgrade(my $u = "\x{e5}");
utf8::downgrade(my $d = "\x{e5}");
/ $u$d /
</code></pre> 

 [perl #118297].
<dt>&bull;
<dd> Lexical constants (<tt>&quot;my sub a() { 42 }&quot;</tt>) no longer crash when inlined.
<dt>&bull;
<dd> Parameter prototypes attached to lexical subroutines are now respected when compiling sub calls without parentheses. Previously, the prototypes were honoured only for calls <i>with</i> parentheses. [<font SIZE="-1">RT</font> #116735]
<dt>&bull;
<dd> Syntax errors in lexical subroutines in combination with calls to the same subroutines no longer cause crashes at compile time.
<dt>&bull;
<dd> The dtrace sub-entry probe now works with lexical subs, instead of crashing [perl #118305].
<dt>&bull;
<dd> Undefining an inlinable lexical subroutine (<tt>&quot;my sub foo() { 42 } undef &amp;foo&quot;</tt>) would result in a crash if warnings were turned on.
<dt>&bull;
<dd> Deep recursion warnings no longer crash lexical subroutines. [<font SIZE="-1">RT</font> #118521]</dl>

<h2>Acknowledgements</h2>

 Perl 5.18.1 represents approximately 2 months of development since Perl 5.18.0 and contains approximately 8,400 lines of changes across 60 files from 12 authors. 

 Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.18.1: 

 Chris 'BinGOs' Williams, Craig A. Berry, Dagfinn Ilmari Mannsåker, David Mitchell, Father Chrysostomos, Karl Williamson, Lukas Mai, Nicholas Clark, Peter Martini, Ricardo Signes, Shlomi Fish, Tony Cook. 

 The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. 

 Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl's core. We're grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. 

 For a more complete list of all of Perl's historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.

<h2>Reporting Bugs</h2>

 If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" HREF="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. 

 If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. 

 If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font>

<h2>SEE ALSO</h2>

 The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. 

 The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. 

 The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. 

 The <i>Artistic</i> and <i>Copying</i> files for copyright information. 

<h2>Index</h2>


