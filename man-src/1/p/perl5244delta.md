---
title: "perl5244delta(1)"
name: "perl5244delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5244delta/"
---

<h2 class="name">NAME</h2>
 

 perl5244delta - what is new for perl v5.24.4 

<h2>DESCRIPTION</h2>

 This document describes differences between the 5.24.3 release and the 5.24.4 release. 

 If you are upgrading from an earlier release such as 5.24.2, first read perl5243delta, which describes differences between 5.24.2 and 5.24.3.

<h2>Security</h2>

<h3>[<font SIZE="-1">CVE-2018-6797</font>] heap-buffer-overflow (<font SIZE="-1">WRITE</font> of size 1) in S_regatom (regcomp.c)</h3>

 A crafted regular expression could cause a heap buffer write overflow, with control over the bytes written. [perl #132227] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Public/Bug/Display.html?id=132227">https://rt.perl.org/Public/Bug/Display.html?id=132227</a>&gt;

<h3>[<font SIZE="-1">CVE-2018-6798</font>] Heap-buffer-overflow in Perl__byte_dump_string (utf8.c)</h3>

 Matching a crafted locale dependent regular expression could cause a heap buffer read overflow and potentially information disclosure. [perl #132063] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Public/Bug/Display.html?id=132063">https://rt.perl.org/Public/Bug/Display.html?id=132063</a>&gt;

<h3>[<font SIZE="-1">CVE-2018-6913</font>] heap-buffer-overflow in S_pack_rec</h3>

 <tt>&quot;pack()&quot;</tt> could cause a heap buffer write overflow with a large item count. [perl #131844] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Public/Bug/Display.html?id=131844">https://rt.perl.org/Public/Bug/Display.html?id=131844</a>&gt;

<h3>Assertion failure in Perl__core_swash_init (utf8.c)</h3>

 Control characters in a supposed Unicode property name could cause perl to crash. This has been fixed. [perl #132055] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Public/Bug/Display.html?id=132055">https://rt.perl.org/Public/Bug/Display.html?id=132055</a>&gt; [perl #132553] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Public/Bug/Display.html?id=132553">https://rt.perl.org/Public/Bug/Display.html?id=132553</a>&gt; [perl #132658] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Public/Bug/Display.html?id=132658">https://rt.perl.org/Public/Bug/Display.html?id=132658</a>&gt;

<h2>Incompatible Changes</h2>

 There are no changes intentionally incompatible with 5.24.3. If any exist, they are bugs, and we request that you submit a report. See ``Reporting Bugs'' below.

<h2>Modules and Pragmata</h2>

<h3>Updated Modules and Pragmata</h3>

<dl>
<dt>&bull;
<dd> Module::CoreList has been upgraded from version 5.20170922_24 to 5.20180414_24.</dl>

<h2>Selected Bug Fixes</h2>

<dl>
<dt>&bull;
<dd> The <tt>&quot;readpipe()&quot;</tt> built-in function now checks at compile time that it has only one parameter expression, and puts it in scalar context, thus ensuring that it doesn't corrupt the stack at runtime. [perl #4574] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Public/Bug/Display.html?id=4574">https://rt.perl.org/Public/Bug/Display.html?id=4574</a>&gt;</dl>

<h2>Acknowledgements</h2>

 Perl 5.24.4 represents approximately 7 months of development since Perl 5.24.3 and contains approximately 2,400 lines of changes across 49 files from 12 authors. 

 Excluding auto-generated files, documentation and release tools, there were approximately 1,300 lines of changes to 12 .pm, .t, .c and .h files. 

 Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.24.4: 

 Abigail, Chris 'BinGOs' Williams, John <font SIZE="-1">SJ</font> Anderson, Karen Etheridge, Karl Williamson, Renee Baecker, Sawyer X, Steve Hay, Todd Rinaldo, Tony Cook, Yves Orton, Zefram. 

 The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. 

 Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl's core. We're grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. 

 For a more complete list of all of Perl's historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.

<h2>Reporting Bugs</h2>

 If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at &lt;<a rel="nofollow" HREF="https://rt.perl.org/">https://rt.perl.org/</a>&gt; . There may also be information at &lt;<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&gt; , the Perl Home Page. 

 If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. 

 If the bug you are reporting has security implications which make it inappropriate to send to a publicly archived mailing list, then see ``<font SIZE="-1">SECURITY VULNERABILITY CONTACT INFORMATION''</font> in perlsec for details of how to report the issue.

<h2>SEE ALSO</h2>

 The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. 

 The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. 

 The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. 

 The <i>Artistic</i> and <i>Copying</i> files for copyright information. 

<h2>Index</h2>



<dt><a HREF="#lbAI">Incompatible Changes</a>
<dd>
<dt><a HREF="#lbAJ">Modules and Pragmata</a>
<dd>


<dt><a HREF="#lbAL">Selected Bug Fixes</a>
<dd>
<dt><a HREF="#lbAM">Acknowledgements</a>
<dd>
<dt><a HREF="#lbAN">Reporting Bugs</a>
<dd>
<dt><a HREF="#lbAO">SEE ALSO</a>
<dd></dl>
