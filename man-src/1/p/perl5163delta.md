---
title: "perl5163delta(1)"
name: "perl5163delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5163delta/"
---

<h2 class="name">NAME</h2>
 

 perl5163delta - what is new for perl v5.16.3 

<h2>DESCRIPTION</h2>

 This document describes differences between the 5.16.2 release and the 5.16.3 release. 

 If you are upgrading from an earlier release such as 5.16.1, first read perl5162delta, which describes differences between 5.16.1 and 5.16.2.

<h2>Core Enhancements</h2>

 No changes since 5.16.0.

<h2>Security</h2>

 This release contains one major and a number of minor security fixes. These latter are included mainly to allow the test suite to pass cleanly with the clang compiler's address sanitizer facility.

<h3><font SIZE="-1">CVE-2013-1667:</font> memory exhaustion with arbitrary hash keys</h3>

 With a carefully crafted set of hash keys (for example arguments on a <font SIZE="-1">URL</font>), it is possible to cause a hash to consume a large amount of memory and <font SIZE="-1">CPU,</font> and thus possibly to achieve a Denial-of-Service. 

 This problem has been fixed.

<h3>wrap-around with <font SIZE="-1">IO</font> on long strings</h3>

 Reading or writing strings greater than 2**31 bytes in size could segfault due to integer wraparound. 

 This problem has been fixed.

<h3>memory leak in Encode</h3>

 The <font SIZE="-1">UTF-8</font> encoding implementation in Encode.xs had a memory leak which has been fixed.

<h2>Incompatible Changes</h2>

 There are no changes intentionally incompatible with 5.16.0. If any exist, they are bugs and reports are welcome.

<h2>Deprecations</h2>

 There have been no deprecations since 5.16.0.

<h2>Modules and Pragmata</h2>

<h3>Updated Modules and Pragmata</h3>

<dl>
<dt>&bull;
<dd> Encode has been upgraded from version 2.44 to version 2.44_01.
<dt>&bull;
<dd> Module::CoreList has been upgraded from version 2.76 to version 2.76_02.
<dt>&bull;
<dd> XS::APItest has been upgraded from version 0.38 to version 0.39.</dl>

<h2>Known Problems</h2>

 None.

<h2>Acknowledgements</h2>

 Perl 5.16.3 represents approximately 4 months of development since Perl 5.16.2 and contains approximately 870 lines of changes across 39 files from 7 authors. 

 Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.16.3: 

 Andy Dougherty, Chris 'BinGOs' Williams, Dave Rolsky, David Mitchell, Michael Schroeder, Ricardo Signes, Yves Orton. 

 The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. 

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



<dt><a HREF="#lbAI">Incompatible Changes</a>
<dd>
<dt><a HREF="#lbAJ">Deprecations</a>
<dd>
<dt><a HREF="#lbAK">Modules and Pragmata</a>
<dd>


<dt><a HREF="#lbAM">Known Problems</a>
<dd>
<dt><a HREF="#lbAN">Acknowledgements</a>
<dd>
<dt><a HREF="#lbAO">Reporting Bugs</a>
<dd>
<dt><a HREF="#lbAP">SEE ALSO</a>
<dd></dl>
