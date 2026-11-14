---
title: "perl5161delta(1)"
name: "perl5161delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5161delta/"
---

<h2 class="name">NAME</h2>
 

 perl5161delta - what is new for perl v5.16.1 

<h2>DESCRIPTION</h2>

 This document describes differences between the 5.16.0 release and the 5.16.1 release. 

 If you are upgrading from an earlier release such as 5.14.0, first read perl5160delta, which describes differences between 5.14.0 and 5.16.0.

<h2>Security</h2>

<h3>an off-by-two error in Scalar-List-Util has been fixed</h3>

 The bugfix was in Scalar-List-Util 1.23_04, and perl 5.16.1 includes Scalar-List-Util 1.25.

<h2>Incompatible Changes</h2>

 There are no changes intentionally incompatible with 5.16.0 If any exist, they are bugs, and we request that you submit a report. See ``Reporting Bugs'' below.

<h2>Modules and Pragmata</h2>

<h3>Updated Modules and Pragmata</h3>

<dl>
<dt>&bull;
<dd> Scalar::Util and List::Util have been upgraded from version 1.23 to version 1.25.
<dt>&bull;
<dd> B::Deparse has been updated from version 1.14 to 1.14_01. An ``uninitialized'' warning emitted by B::Deparse has been squashed [perl #113464].</dl>

<h2>Configuration and Compilation</h2>

<dl>
<dt>&bull;
<dd> Building perl with some Windows compilers used to fail due to a problem with miniperl's <tt>&quot;glob&quot;</tt> operator (which uses the <tt>&quot;perlglob&quot;</tt> program) deleting the <font SIZE="-1">PATH</font> environment variable [perl #113798].</dl>

<h2>Platform Support</h2>

<h3>Platform-Specific Notes</h3>

<dl>
<dt><font SIZE="-1">VMS</font>
<dd> All C header files from the top-level directory of the distribution are now installed on <font SIZE="-1">VMS,</font> providing consistency with a long-standing practice on other platforms. Previously only a subset were installed, which broke non-core extension builds for extensions that depended on the missing include files.</dl>

<h2>Selected Bug Fixes</h2>

<dl>
<dt>&bull;
<dd> A regression introduced in Perl v5.16.0 involving <tt>&quot;tr/</tt>SEARCHLIST<tt>/</tt>REPLACEMENTLIST<tt>/&quot;</tt> has been fixed. Only the first instance is supposed to be meaningful if a character appears more than once in <tt>&quot;</tt>SEARCHLIST<tt>&quot;</tt>. Under some circumstances, the final instance was overriding all earlier ones. [perl #113584]
<dt>&bull;
<dd> <tt>&quot;B::COP::stashlen&quot;</tt> has been added. This provides access to an internal field added in perl 5.16 under threaded builds. It was broken at the last minute before 5.16 was released [perl #113034].
<dt>&bull;
<dd> The re pragma will no longer clobber <tt>$_</tt>. [perl #113750]
<dt>&bull;
<dd> Unicode 6.1 published an incorrect alias for one of the Canonical_Combining_Class property's values (which range between 0 and 254). The alias <tt>&quot;CCC133&quot;</tt> should have been <tt>&quot;CCC132&quot;</tt>. Perl now overrides the data file furnished by Unicode to give the correct value.
<dt>&bull;
<dd> Duplicating scalar filehandles works again. [perl #113764]
<dt>&bull;
<dd> Under threaded perls, a runtime code block in a regular expression could corrupt the package name stored in the op tree, resulting in bad reads in <tt>&quot;caller&quot;</tt>, and possibly crashes [perl #113060].
<dt>&bull;
<dd> For efficiency's sake, many operators and built-in functions return the same scalar each time. Lvalue subroutines and subroutines in the <font SIZE="-1">CORE::</font> namespace were allowing this implementation detail to leak through. <tt>&quot;print &amp;CORE::uc(&quot;a&quot;), &amp;CORE::uc(&quot;b&quot;)&quot;</tt> used to print ``<font SIZE="-1">BB''.</font> The same thing would happen with an lvalue subroutine returning the return value of <tt>&quot;uc&quot;</tt>. Now the value is copied in such cases [perl #113044].
<dt>&bull;
<dd> <tt>&quot;__SUB__&quot;</tt> now works in special blocks (<tt>&quot;BEGIN&quot;</tt>, <tt>&quot;END&quot;</tt>, etc.).
<dt>&bull;
<dd> Formats that reference lexical variables from outside no longer result in crashes.</dl>

<h2>Known Problems</h2>

 There are no new known problems, but consult ``Known Problems'' in perl5160delta to see those identified in the 5.16.0 release.

<h2>Acknowledgements</h2>

 Perl 5.16.1 represents approximately 2 months of development since Perl 5.16.0 and contains approximately 14,000 lines of changes across 96 files from 8 authors. 

 Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.16.1: 

 Chris 'BinGOs' Williams, Craig A. Berry, Father Chrysostomos, Karl Williamson, Paul Johnson, Reini Urban, Ricardo Signes, Tony Cook. 

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


