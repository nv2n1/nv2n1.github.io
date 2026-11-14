---
title: "perl5262delta(1)"
name: "perl5262delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5262delta/"
description: "perl5262delta – what is new for perl v5.26.2"
---

<h2 class="name">NAME</h2>
<p> perl5262delta &#8211; what is new for perl v5.26.2 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.26.1 release and the 5.26.2 release. </p>
<p> If you are upgrading from an earlier release such as 5.26.0, first read perl5261delta, which describes differences between 5.26.0 and 5.26.1.</p>
<h2>Security</h2>
<h3>[<font SIZE="-1">CVE-2018-6797</font>] heap-buffer-overflow (<font SIZE="-1">WRITE</font> of size 1) in S_regatom (regcomp.c)</h3>
<p> A crafted regular expression could cause a heap buffer write overflow, with control over the bytes written. [perl #132227] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=132227">https://rt.perl.org/Public/Bug/Display.html?id=132227</a>&gt;</p>
<h3>[<font SIZE="-1">CVE-2018-6798</font>] Heap-buffer-overflow in Perl__byte_dump_string (utf8.c)</h3>
<p> Matching a crafted locale dependent regular expression could cause a heap buffer read overflow and potentially information disclosure. [perl #132063] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=132063">https://rt.perl.org/Public/Bug/Display.html?id=132063</a>&gt;</p>
<h3>[<font SIZE="-1">CVE-2018-6913</font>] heap-buffer-overflow in S_pack_rec</h3>
<p> <tt>&quot;pack()&quot;</tt> could cause a heap buffer write overflow with a large item count. [perl #131844] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131844">https://rt.perl.org/Public/Bug/Display.html?id=131844</a>&gt;</p>
<h3>Assertion failure in Perl__core_swash_init (utf8.c)</h3>
<p> Control characters in a supposed Unicode property name could cause perl to crash. This has been fixed. [perl #132055] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=132055">https://rt.perl.org/Public/Bug/Display.html?id=132055</a>&gt; [perl #132553] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=132553">https://rt.perl.org/Public/Bug/Display.html?id=132553</a>&gt; [perl #132658] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=132658">https://rt.perl.org/Public/Bug/Display.html?id=132658</a>&gt;</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.26.1. If any exist, they are bugs, and we request that you submit a report. See &#8220;Reporting Bugs&#8221; below.</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> Module::CoreList has been upgraded from version 5.20170922_26 to 5.20180414_26.</p>
<dt>&bull;</p>
<dd> PerlIO::via has been upgraded from version 0.16 to 0.17.</p>
<dt>&bull;</p>
<dd> Term::ReadLine has been upgraded from version 1.16 to 1.17.</p>
<dt>&bull;</p>
<dd> Unicode::UCD has been upgraded from version 0.68 to 0.69.</dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perluniprops</i></p>
<dl>
<dt>&bull;</p>
<dd> This has been updated to note that <tt>&quot;\p{Word}&quot;</tt> now includes code points matching the <tt>&quot;\p{Join_Control}&quot;</tt> property. The change to the property was made in Perl 5.18, but not documented until now. There are currently only two code points that match this property: U+200C (<font SIZE="-1">ZERO WIDTH</font> NON-JOINER) and U+200D (<font SIZE="-1">ZERO WIDTH JOINER</font>).</dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>Windows</p>
<dd> Visual C<font SIZE="-2">++</font> compiler version detection has been improved to work on non-English language systems. [perl #132421] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=132421">https://rt.perl.org/Public/Bug/Display.html?id=132421</a>&gt; </p>
<p> We now set <tt>$Config{libpth}</tt> correctly for 64-bit builds using Visual C<font SIZE="-2">++</font> versions earlier than 14.1. [perl #132484] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=132484">https://rt.perl.org/Public/Bug/Display.html?id=132484</a>&gt;</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> The <tt>&quot;readpipe()&quot;</tt> built-in function now checks at compile time that it has only one parameter expression, and puts it in scalar context, thus ensuring that it doesn&#8217;t corrupt the stack at runtime. [perl #4574] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=4574">https://rt.perl.org/Public/Bug/Display.html?id=4574</a>&gt;</p>
<dt>&bull;</p>
<dd> Fixed a use after free bug in <tt>&quot;pp_list&quot;</tt> introduced in Perl 5.27.1. [perl #131954] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131954">https://rt.perl.org/Public/Bug/Display.html?id=131954</a>&gt;</p>
<dt>&bull;</p>
<dd> Parsing a <tt>&quot;sub&quot;</tt> definition could cause a use after free if the <tt>&quot;sub&quot;</tt> keyword was followed by whitespace including newlines (and comments). [perl #131836] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131836">https://rt.perl.org/Public/Bug/Display.html?id=131836</a>&gt;</p>
<dt>&bull;</p>
<dd> The tokenizer now correctly adjusts a parse pointer when skipping whitespace in an <tt>&quot; ${identifier} &quot;</tt> construct. [perl #131949] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131949">https://rt.perl.org/Public/Bug/Display.html?id=131949</a>&gt;</p>
<dt>&bull;</p>
<dd> Accesses to <tt>&quot;${^LAST_FH}&quot;</tt> no longer assert after using any of a variety of I/O operations on a non-glob. [perl #128263] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128263">https://rt.perl.org/Public/Bug/Display.html?id=128263</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;sort&quot;</tt> now performs correct reference counting when aliasing <tt>$a</tt> and <tt>$b</tt>, thus avoiding premature destruction and leakage of scalars if they are re-aliased during execution of the sort comparator. [perl #92264] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=92264">https://rt.perl.org/Public/Bug/Display.html?id=92264</a>&gt;</p>
<dt>&bull;</p>
<dd> Some convoluted kinds of regexp no longer cause an arithmetic overflow when compiled. [perl #131893] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131893">https://rt.perl.org/Public/Bug/Display.html?id=131893</a>&gt;</p>
<dt>&bull;</p>
<dd> Fixed a duplicate symbol failure with <code>-flto -mieee-fp</code> builds. <i>pp.c</i> defined <tt>&quot;_LIB_VERSION&quot;</tt> which <code>-lieee</code> already defines. [perl #131786] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131786">https://rt.perl.org/Public/Bug/Display.html?id=131786</a>&gt;</p>
<dt>&bull;</p>
<dd> A <font SIZE="-1">NULL</font> pointer dereference in the <tt>&quot;S_regmatch()&quot;</tt> function has been fixed. [perl #132017] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=132017">https://rt.perl.org/Public/Bug/Display.html?id=132017</a>&gt;</p>
<dt>&bull;</p>
<dd> Failures while compiling code within other constructs, such as with string interpolation and the right part of <tt>&quot;s///e&quot;</tt> now cause compilation to abort earlier. </p>
<p> Previously compilation could continue in order to report other errors, but the failed sub-parse could leave partly parsed constructs on the parser shift-reduce stack, confusing the parser, leading to perl crashes. [perl #125351] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=125351">https://rt.perl.org/Public/Bug/Display.html?id=125351</a>&gt;</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.26.2 represents approximately 7 months of development since Perl 5.26.1 and contains approximately 3,300 lines of changes across 82 files from 17 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 1,800 lines of changes to 36 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.26.2: </p>
<p> Aaron Crane, Abigail, Chris &#8216;BinGOs&#8217; Williams, H.Merijn Brand, James E Keenan, Jarkko Hietaniemi, John <font SIZE="-1">SJ</font> Anderson, Karen Etheridge, Karl Williamson, Lukas Mai, Renee Baecker, Sawyer X, Steve Hay, Todd Rinaldo, Tony Cook, Yves Orton, Zefram. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the perl bug database at &lt;<a rel="nofollow" href="https://rt.perl.org/">https://rt.perl.org/</a>&gt; . There may also be information at &lt;<a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a>&gt; , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications which make it inappropriate to send to a publicly archived mailing list, then see &#8220;<font SIZE="-1">SECURITY VULNERABILITY CONTACT INFORMATION&#8221;</font> in perlsec for details of how to report the issue.</p>
<h2>Give Thanks</h2>
<p> If you wish to thank the Perl 5 Porters for the work we had done in Perl 5, you can do so by running the <tt>&quot;perlthanks&quot;</tt> program: </p>
<pre>
    perlthanks
</pre>
<p> This will send an email to the Perl 5 Porters list with your show of thanks.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Incompatible Changes</a></p>
<dd>
<dt><a href="#lbAJ">Modules and Pragmata</a></p>
<dd>
<dt><a href="#lbAL">Documentation</a></p>
<dd>
<dt><a href="#lbAN">Platform Support</a></p>
<dd>
<dt><a href="#lbAP">Selected Bug Fixes</a></p>
<dd>
<dt><a href="#lbAQ">Acknowledgements</a></p>
<dd>
<dt><a href="#lbAR">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbAS">Give Thanks</a></p>
<dd>
<dt><a href="#lbAT">SEE ALSO</a></p>
<dd></dl>
