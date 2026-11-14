---
title: "perl5281delta(1)"
name: "perl5281delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5281delta/"
---

<h2 class="name">NAME</h2>
 

 perl5281delta - what is new for perl v5.28.1 

<h2>DESCRIPTION</h2>

 This document describes differences between the 5.28.0 release and the 5.28.1 release. 

 If you are upgrading from an earlier release such as 5.26.0, first read perl5280delta, which describes differences between 5.26.0 and 5.28.0.

<h2>Security</h2>

<h3>[<font SIZE="-1">CVE-2018-18311</font>] Integer overflow leading to buffer overflow and segmentation fault</h3>

 Integer arithmetic in <tt>&quot;Perl_my_setenv()&quot;</tt> could wrap when the combined length of the environment variable name and value exceeded around 0x7fffffff. This could lead to writing beyond the end of an allocated buffer with attacker supplied data. 

 [perl #133204] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=133204">https://rt.perl.org/Ticket/Display.html?id=133204</a>&gt;

<h3>[<font SIZE="-1">CVE-2018-18312</font>] Heap-buffer-overflow write in S_regatom (regcomp.c)</h3>

 A crafted regular expression could cause heap-buffer-overflow write during compilation, potentially allowing arbitrary code execution. 

 [perl #133423] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=133423">https://rt.perl.org/Ticket/Display.html?id=133423</a>&gt;

<h2>Incompatible Changes</h2>

 There are no changes intentionally incompatible with 5.28.0. If any exist, they are bugs, and we request that you submit a report. See ``Reporting Bugs'' below.

<h2>Modules and Pragmata</h2>

<h3>Updated Modules and Pragmata</h3>

<dl>
<dt>&bull;
<dd> Module::CoreList has been upgraded from version 5.20180622 to 5.20181129_28.</dl>

<h2>Selected Bug Fixes</h2>

<dl>
<dt>&bull;
<dd> Perl 5.28 introduced an <tt>&quot;index()&quot;</tt> optimization when comparing to -1 (or indirectly, e.g. &gt;= 0). When this optimization was triggered inside a <tt>&quot;when&quot;</tt> clause it caused a warning (``Argument <tt>%s</tt> isn't numeric in smart match''). This has now been fixed. [perl #133368] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=133368">https://rt.perl.org/Ticket/Display.html?id=133368</a>&gt;
<dt>&bull;
<dd> Matching of decimal digits in script runs, introduced in Perl 5.28, had a bug that led to <tt>&quot;1\N{THAI DIGIT FIVE}&quot;</tt> matching <tt>&quot;/^(*sr:\d+)$/&quot;</tt> when it should not. This has now been fixed.
<dt>&bull;
<dd> The new in-place editing code no longer leaks directory handles. [perl #133314] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=133314">https://rt.perl.org/Ticket/Display.html?id=133314</a>&gt;</dl>

<h2>Acknowledgements</h2>

 Perl 5.28.1 represents approximately 5 months of development since Perl 5.28.0 and contains approximately 6,100 lines of changes across 44 files from 12 authors. 

 Excluding auto-generated files, documentation and release tools, there were approximately 700 lines of changes to 12 .pm, .t, .c and .h files. 

 Perl continues to flourish into its fourth decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.28.1: 

 Aaron Crane, Abigail, Chris 'BinGOs' Williams, Dagfinn Ilmari Mannsåker, David Mitchell, James E Keenan, John <font SIZE="-1">SJ</font> Anderson, Karen Etheridge, Karl Williamson, Sawyer X, Steve Hay, Tony Cook. 

 The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. 

 Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl's core. We're grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. 

 For a more complete list of all of Perl's historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.

<h2>Reporting Bugs</h2>

 If you find what you think is a bug, you might check the perl bug database at &lt;<a rel="nofollow" HREF="https://rt.perl.org/">https://rt.perl.org/</a>&gt; . There may also be information at &lt;<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&gt; , the Perl Home Page. 

 If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. 

 If the bug you are reporting has security implications which make it inappropriate to send to a publicly archived mailing list, then see ``<font SIZE="-1">SECURITY VULNERABILITY CONTACT INFORMATION''</font> in perlsec for details of how to report the issue.

<h2>Give Thanks</h2>

 If you wish to thank the Perl 5 Porters for the work we had done in Perl 5, you can do so by running the <tt>&quot;perlthanks&quot;</tt> program: 

 <pre>
    perlthanks
</pre> 

 This will send an email to the Perl 5 Porters list with your show of thanks.

<h2>SEE ALSO</h2>

 The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. 

 The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. 

 The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. 

 The <i>Artistic</i> and <i>Copying</i> files for copyright information. 

<h2>Index</h2>



<dt><a HREF="#lbAG">Incompatible Changes</a>
<dd>
<dt><a HREF="#lbAH">Modules and Pragmata</a>
<dd>


<dt><a HREF="#lbAJ">Selected Bug Fixes</a>
<dd>
<dt><a HREF="#lbAK">Acknowledgements</a>
<dd>
<dt><a HREF="#lbAL">Reporting Bugs</a>
<dd>
<dt><a HREF="#lbAM">Give Thanks</a>
<dd>
<dt><a HREF="#lbAN">SEE ALSO</a>
<dd></dl>
