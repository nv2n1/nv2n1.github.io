---
title: "perl5184delta(1)"
name: "perl5184delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5184delta/"
description: "perl5184delta – what is new for perl v5.18.4"
---

<h2 class="name">NAME</h2>
<p> perl5184delta &#8211; what is new for perl v5.18.4 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.18.4 release and the 5.18.2 release. <code>Please note:</code> This document ignores perl 5.18.3, a broken release which existed for a few hours only. </p>
<p> If you are upgrading from an earlier release such as 5.18.1, first read perl5182delta, which describes differences between 5.18.1 and 5.18.2.</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> Digest::SHA has been upgraded from 5.84_01 to 5.84_02.</p>
<dt>&bull;</p>
<dd> perl5db.pl has been upgraded from version 1.39_10 to 1.39_11. </p>
<p> This fixes a crash in tab completion, where available. [perl #120827] Also, filehandle information is properly reset after a pager is run. [perl #121456]</dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>Win32</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Introduced by perl #113536 &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=113536">https://rt.perl.org/Public/Bug/Display.html?id=113536</a>&gt;, a memory leak on every call to <tt>&quot;system&quot;</tt> and backticks (<tt>&quot; `` &quot;</tt>), on most Win32 Perls starting from 5.18.0 has been fixed. The memory leak only occurred if you enabled pseudo-fork in your build of Win32 Perl, and were running that build on Server 2003 R2 or newer <font SIZE="-1">OS.</font> The leak does not appear on WinXP <font SIZE="-1">SP3.</font> [perl #121676 &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=121676">https://rt.perl.org/Public/Bug/Display.html?id=121676</a>&gt;]</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> The debugger now properly resets filehandles as needed. [perl #121456]</p>
<dt>&bull;</p>
<dd> A segfault in Digest::SHA has been addressed. [perl #121421]</p>
<dt>&bull;</p>
<dd> perl can again be built with <font SIZE="-1">USE_64_BIT_INT,</font> with Visual C 2003, 32 bit. [perl #120925]</p>
<dt>&bull;</p>
<dd> A leading { (brace) in formats is properly parsed again. [perl #119973]</p>
<dt>&bull;</p>
<dd> Copy the values used to perturb hash iteration when cloning an interpreter. This was fairly harmless but caused <tt>&quot;valgrind&quot;</tt> to complain. [perl #121336]</p>
<dt>&bull;</p>
<dd> In Perl v5.18 <tt>&quot;undef *_; goto &amp;sub&quot;</tt> and <tt>&quot;local *_; goto &amp;sub&quot;</tt> started crashing. This has been fixed. [perl #119949]</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.18.4 represents approximately 9 months of development since Perl 5.18.2 and contains approximately 2,000 lines of changes across 53 files from 13 authors. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.18.4: </p>
<p> Daniel Dragan, David Mitchell, Doug Bell, Father Chrysostomos, Hiroo Hayashi, James E Keenan, Karl Williamson, Mark Shelor, Ricardo Signes, Shlomi Fish, Smylers, Steve Hay, Tony Cook. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font></p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
