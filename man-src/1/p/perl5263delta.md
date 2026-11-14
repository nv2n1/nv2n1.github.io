---
title: "perl5263delta(1)"
name: "perl5263delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5263delta/"
---

<h2 class="name">NAME</h2>
 

 perl5263delta - what is new for perl v5.26.3 

<h2>DESCRIPTION</h2>

 This document describes differences between the 5.26.2 release and the 5.26.3 release. 

 If you are upgrading from an earlier release such as 5.26.1, first read perl5262delta, which describes differences between 5.26.1 and 5.26.2.

<h2>Security</h2>

<h3>[<font SIZE="-1">CVE-2018-12015</font>] Directory traversal in module Archive::Tar</h3>

 By default, Archive::Tar doesn't allow extracting files outside the current working directory. However, this secure extraction mode could be bypassed by putting a symlink and a regular file with the same name into the tar file. 

 [perl #133250] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=133250">https://rt.perl.org/Ticket/Display.html?id=133250</a>&gt; [cpan #125523] &lt;<a rel="nofollow" HREF="https://rt.cpan.org/Ticket/Display.html?id=125523">https://rt.cpan.org/Ticket/Display.html?id=125523</a>&gt;

<h3>[<font SIZE="-1">CVE-2018-18311</font>] Integer overflow leading to buffer overflow and segmentation fault</h3>

 Integer arithmetic in <tt>&quot;Perl_my_setenv()&quot;</tt> could wrap when the combined length of the environment variable name and value exceeded around 0x7fffffff. This could lead to writing beyond the end of an allocated buffer with attacker supplied data. 

 [perl #133204] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=133204">https://rt.perl.org/Ticket/Display.html?id=133204</a>&gt;

<h3>[<font SIZE="-1">CVE-2018-18312</font>] Heap-buffer-overflow write in S_regatom (regcomp.c)</h3>

 A crafted regular expression could cause heap-buffer-overflow write during compilation, potentially allowing arbitrary code execution. 

 [perl #133423] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=133423">https://rt.perl.org/Ticket/Display.html?id=133423</a>&gt;

<h3>[<font SIZE="-1">CVE-2018-18313</font>] Heap-buffer-overflow read in S_grok_bslash_N (regcomp.c)</h3>

 A crafted regular expression could cause heap-buffer-overflow read during compilation, potentially leading to sensitive information being leaked. 

 [perl #133192] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=133192">https://rt.perl.org/Ticket/Display.html?id=133192</a>&gt;

<h3>[<font SIZE="-1">CVE-2018-18314</font>] Heap-buffer-overflow write in S_regatom (regcomp.c)</h3>

 A crafted regular expression could cause heap-buffer-overflow write during compilation, potentially allowing arbitrary code execution. 

 [perl #131649] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=131649">https://rt.perl.org/Ticket/Display.html?id=131649</a>&gt;

<h2>Incompatible Changes</h2>

 There are no changes intentionally incompatible with 5.26.2. If any exist, they are bugs, and we request that you submit a report. See ``Reporting Bugs'' below.

<h2>Modules and Pragmata</h2>

<h3>Updated Modules and Pragmata</h3>

<dl>
<dt>&bull;
<dd> Archive::Tar has been upgraded from version 2.24 to 2.24_01.
<dt>&bull;
<dd> Module::CoreList has been upgraded from version 5.20180414_26 to 5.20181129_26.</dl>

<h2>Diagnostics</h2>

 The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.

<h3>New Diagnostics</h3>

 <i>New Errors</i>
<dl>
<dt>&bull;
<dd> Unexpected ']' with no following ')' in (?[... in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ 

 (F) While parsing an extended character class a ']' character was encountered at a point in the definition where the only legal use of ']' is to close the character class definition as part of a '])', you may have forgotten the close paren, or otherwise confused the parser.
<dt>&bull;
<dd> Expecting close paren for nested extended charclass in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ 

 (F) While parsing a nested extended character class like: 

 <pre><code>
    (?[ ... (?flags:(?[ ... ])) ... ])
                             ^
</code></pre> 

 we expected to see a close paren ')' (marked by ^) but did not.
<dt>&bull;
<dd> Expecting close paren for wrapper for nested extended charclass in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ 

 (F) While parsing a nested extended character class like: 

 <pre><code>
    (?[ ... (?flags:(?[ ... ])) ... ])
                              ^
</code></pre> 

 we expected to see a close paren ')' (marked by ^) but did not.</dl>

<h3>Changes to Existing Diagnostics</h3>

<dl>
<dt>&bull;
<dd> Syntax error in (?[...]) in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ 

 This fatal error message has been slightly expanded (from ``Syntax error in (?[...]) in regex m/%s/'') for greater clarity.</dl>

<h2>Acknowledgements</h2>

 Perl 5.26.3 represents approximately 8 months of development since Perl 5.26.2 and contains approximately 4,500 lines of changes across 51 files from 15 authors. 

 Excluding auto-generated files, documentation and release tools, there were approximately 770 lines of changes to 10 .pm, .t, .c and .h files. 

 Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.26.3: 

 Aaron Crane, Abigail, Chris 'BinGOs' Williams, Dagfinn Ilmari Mannsåker, David Mitchell, H.Merijn Brand, James E Keenan, John <font SIZE="-1">SJ</font> Anderson, Karen Etheridge, Karl Williamson, Sawyer X, Steve Hay, Todd Rinaldo, Tony Cook, Yves Orton. 

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



<dt><a HREF="#lbAJ">Incompatible Changes</a>
<dd>
<dt><a HREF="#lbAK">Modules and Pragmata</a>
<dd>


<dt><a HREF="#lbAM">Diagnostics</a>
<dd>


<dt><a HREF="#lbAP">Acknowledgements</a>
<dd>
<dt><a HREF="#lbAQ">Reporting Bugs</a>
<dd>
<dt><a HREF="#lbAR">Give Thanks</a>
<dd>
<dt><a HREF="#lbAS">SEE ALSO</a>
<dd></dl>
