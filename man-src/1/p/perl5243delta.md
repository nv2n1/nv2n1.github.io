---
title: "perl5243delta(1)"
name: "perl5243delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5243delta/"
description: "perl5243delta – what is new for perl v5.24.3"
---

<h2 class="name">NAME</h2>
<p> perl5243delta &#8211; what is new for perl v5.24.3 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.24.2 release and the 5.24.3 release. </p>
<p> If you are upgrading from an earlier release such as 5.24.1, first read perl5242delta, which describes differences between 5.24.1 and 5.24.2.</p>
<h2>Security</h2>
<h3>[<font SIZE="-1">CVE-2017-12837</font>] Heap buffer overflow in regular expression compiler</h3>
<p> Compiling certain regular expression patterns with the case-insensitive modifier could cause a heap buffer overflow and crash perl. This has now been fixed. [perl #131582] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131582">https://rt.perl.org/Public/Bug/Display.html?id=131582</a>&gt;</p>
<h3>[<font SIZE="-1">CVE-2017-12883</font>] Buffer over-read in regular expression parser</h3>
<p> For certain types of syntax error in a regular expression pattern, the error message could either contain the contents of a random, possibly large, chunk of memory, or could crash perl. This has now been fixed. [perl #131598] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131598">https://rt.perl.org/Public/Bug/Display.html?id=131598</a>&gt;</p>
<h3>[<font SIZE="-1">CVE-2017-12814</font>] $ENV{$key} stack buffer overflow on Windows</h3>
<p> A possible stack buffer overflow in the <tt>%ENV</tt> code on Windows has been fixed by removing the buffer completely since it was superfluous anyway. [perl #131665] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131665">https://rt.perl.org/Public/Bug/Display.html?id=131665</a>&gt;</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.24.2. If any exist, they are bugs, and we request that you submit a report. See &#8220;Reporting Bugs&#8221; below.</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> Module::CoreList has been upgraded from version 5.20170715_24 to 5.20170922_24.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">POSIX</font> has been upgraded from version 1.65 to 1.65_01.</p>
<dt>&bull;</p>
<dd> Time::HiRes has been upgraded from version 1.9733 to 1.9741. </p>
<p> [perl #128427] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128427">https://rt.perl.org/Public/Bug/Display.html?id=128427</a>&gt; [perl #128445] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128445">https://rt.perl.org/Public/Bug/Display.html?id=128445</a>&gt; [perl #128972] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128972">https://rt.perl.org/Public/Bug/Display.html?id=128972</a>&gt; [cpan #120032] &lt;<a rel="nofollow" href="https://rt.cpan.org/Public/Bug/Display.html?id=120032">https://rt.cpan.org/Public/Bug/Display.html?id=120032</a>&gt;</dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</p>
<dd> When building with <font SIZE="-1">GCC 6</font> and link-time optimization (the <code>-flto</code> option to <code>gcc</code>), <i>Configure</i> was treating all probed symbols as present on the system, regardless of whether they actually exist. This has been fixed. [perl #128131] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128131">https://rt.perl.org/Public/Bug/Display.html?id=128131</a>&gt;</p>
<dt>&bull;</p>
<dd> <i>Configure</i> now aborts if both <tt>&quot;-Duselongdouble&quot;</tt> and <tt>&quot;-Dusequadmath&quot;</tt> are requested. [perl #126203] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=126203">https://rt.perl.org/Public/Bug/Display.html?id=126203</a>&gt;</p>
<dt>&bull;</p>
<dd> Fixed a bug in which <i>Configure</i> could append <tt>&quot;-quadmath&quot;</tt> to the archname even if it was already present. [perl #128538] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128538">https://rt.perl.org/Public/Bug/Display.html?id=128538</a>&gt;</p>
<dt>&bull;</p>
<dd> Clang builds with <tt>&quot;-DPERL_GLOBAL_STRUCT&quot;</tt> or <tt>&quot;-DPERL_GLOBAL_STRUCT_PRIVATE&quot;</tt> have been fixed (by disabling Thread Safety Analysis for these configurations).</dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt><font SIZE="-1">VMS</font></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;configure.com&quot;</tt> now recognizes the VSI-branded C compiler.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Windows</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Building <font SIZE="-1">XS</font> modules with <font SIZE="-1">GCC 6</font> in a 64-bit build of Perl failed due to incorrect mapping of <tt>&quot;strtoll&quot;</tt> and <tt>&quot;strtoull&quot;</tt>. This has now been fixed. [perl #131726] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131726">https://rt.perl.org/Public/Bug/Display.html?id=131726</a>&gt; [cpan #121683] &lt;<a rel="nofollow" href="https://rt.cpan.org/Public/Bug/Display.html?id=121683">https://rt.cpan.org/Public/Bug/Display.html?id=121683</a>&gt; [cpan #122353] &lt;<a rel="nofollow" href="https://rt.cpan.org/Public/Bug/Display.html?id=122353">https://rt.cpan.org/Public/Bug/Display.html?id=122353</a>&gt;</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;/@0{0*-&gt;@*/*0&quot;</tt> and similar contortions used to crash, but no longer do, but merely produce a syntax error. [perl #128171] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128171">https://rt.perl.org/Public/Bug/Display.html?id=128171</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;do&quot;</tt> or <tt>&quot;require&quot;</tt> with an argument which is a reference or typeglob which, when stringified, contains a null character, started crashing in Perl 5.20, but has now been fixed. [perl #128182] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128182">https://rt.perl.org/Public/Bug/Display.html?id=128182</a>&gt;</p>
<dt>&bull;</p>
<dd> Expressions containing an <tt>&quot;&amp;&amp;&quot;</tt> or <tt>&quot;||&quot;</tt> operator (or their synonyms <tt>&quot;and&quot;</tt> and <tt>&quot;or&quot;</tt>) were being compiled incorrectly in some cases. If the left-hand side consisted of either a negated bareword constant or a negated <tt>&quot;do {}&quot;</tt> block containing a constant expression, and the right-hand side consisted of a negated non-foldable expression, one of the negations was effectively ignored. The same was true of <tt>&quot;if&quot;</tt> and <tt>&quot;unless&quot;</tt> statement modifiers, though with the left-hand and right-hand sides swapped. This long-standing bug has now been fixed. [perl #127952] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=127952">https://rt.perl.org/Public/Bug/Display.html?id=127952</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;reset&quot;</tt> with an argument no longer crashes when encountering stash entries other than globs. [perl #128106] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128106">https://rt.perl.org/Public/Bug/Display.html?id=128106</a>&gt;</p>
<dt>&bull;</p>
<dd> Assignment of hashes to, and deletion of, typeglobs named <tt>*::::::</tt> no longer causes crashes. [perl #128086] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128086">https://rt.perl.org/Public/Bug/Display.html?id=128086</a>&gt;</p>
<dt>&bull;</p>
<dd> Assignment variants of any bitwise ops under the <tt>&quot;bitwise&quot;</tt> feature would crash if the left-hand side was an array or hash. [perl #128204] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128204">https://rt.perl.org/Public/Bug/Display.html?id=128204</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;socket&quot;</tt> now leaves the error code returned by the system in <tt>$!</tt> on failure. [perl #128316] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128316">https://rt.perl.org/Public/Bug/Display.html?id=128316</a>&gt;</p>
<dt>&bull;</p>
<dd> Parsing bad <font SIZE="-1">POSIX</font> charclasses no longer leaks memory. [perl #128313] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128313">https://rt.perl.org/Public/Bug/Display.html?id=128313</a>&gt;</p>
<dt>&bull;</p>
<dd> Since Perl 5.20, line numbers have been off by one when perl is invoked with the <code>-x</code> switch. This has been fixed. [perl #128508] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128508">https://rt.perl.org/Public/Bug/Display.html?id=128508</a>&gt;</p>
<dt>&bull;</p>
<dd> Some obscure cases of subroutines and file handles being freed at the same time could result in crashes, but have been fixed. The crash was introduced in Perl 5.22. [perl #128597] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128597">https://rt.perl.org/Public/Bug/Display.html?id=128597</a>&gt;</p>
<dt>&bull;</p>
<dd> Some regular expression parsing glitches could lead to assertion failures with regular expressions such as <tt>&quot;/(?&lt;=/&quot;</tt> and <tt>&quot;/(?&lt;!/&quot;</tt>. This has now been fixed. [perl #128170] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128170">https://rt.perl.org/Public/Bug/Display.html?id=128170</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;gethostent&quot;</tt> and similar functions now perform a null check internally, to avoid crashing with the torsocks library. This was a regression from Perl 5.22. [perl #128740] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128740">https://rt.perl.org/Public/Bug/Display.html?id=128740</a>&gt;</p>
<dt>&bull;</p>
<dd> Mentioning the same constant twice in a row (which is a syntax error) no longer fails an assertion under debugging builds. This was a regression from Perl 5.20. [perl #126482] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=126482">https://rt.perl.org/Public/Bug/Display.html?id=126482</a>&gt;</p>
<dt>&bull;</p>
<dd> In Perl 5.24 <tt>&quot;fchown&quot;</tt> was changed not to accept negative one as an argument because in some platforms that is an error. However, in some other platforms that is an acceptable argument. This change has been reverted. [perl #128967] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128967">https://rt.perl.org/Public/Bug/Display.html?id=128967</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;@{x&quot;</tt> followed by a newline where <tt>&quot;x&quot;</tt> represents a control or non-ASCII character no longer produces a garbled syntax error message or a crash. [perl #128951] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128951">https://rt.perl.org/Public/Bug/Display.html?id=128951</a>&gt;</p>
<dt>&bull;</p>
<dd> A regression in Perl 5.24 with <tt>&quot;tr/\N{U+...}/foo/&quot;</tt> when the code point was between 128 and 255 has been fixed. [perl #128734] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128734">https://rt.perl.org/Public/Bug/Display.html?id=128734</a>&gt;.</p>
<dt>&bull;</p>
<dd> Many issues relating to <tt>&quot;printf &quot;%a&quot;&quot;</tt> of hexadecimal floating point were fixed. In addition, the &#8220;subnormals&#8221; (formerly known as &#8220;denormals&#8221;) floating point numbers are now supported both with the plain <font SIZE="-1">IEEE 754</font> floating point numbers (64-bit or 128-bit) and the x86 80-bit &#8220;extended precision&#8221;. Note that subnormal hexadecimal floating point literals will give a warning about &#8220;exponent underflow&#8221;. [perl #128843] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128843">https://rt.perl.org/Public/Bug/Display.html?id=128843</a>&gt; [perl #128888] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128888">https://rt.perl.org/Public/Bug/Display.html?id=128888</a>&gt; [perl #128889] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128889">https://rt.perl.org/Public/Bug/Display.html?id=128889</a>&gt; [perl #128890] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128890">https://rt.perl.org/Public/Bug/Display.html?id=128890</a>&gt; [perl #128893] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128893">https://rt.perl.org/Public/Bug/Display.html?id=128893</a>&gt; [perl #128909] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128909">https://rt.perl.org/Public/Bug/Display.html?id=128909</a>&gt; [perl #128919] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128919">https://rt.perl.org/Public/Bug/Display.html?id=128919</a>&gt;</p>
<dt>&bull;</p>
<dd> The parser could sometimes crash if a bareword came after <tt>&quot;evalbytes&quot;</tt>. [perl #129196] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129196">https://rt.perl.org/Public/Bug/Display.html?id=129196</a>&gt;</p>
<dt>&bull;</p>
<dd> Fixed a place where the regex parser was not setting the syntax error correctly on a syntactically incorrect pattern. [perl #129122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129122">https://rt.perl.org/Public/Bug/Display.html?id=129122</a>&gt;</p>
<dt>&bull;</p>
<dd> A vulnerability in Perl&#8217;s <tt>&quot;sprintf&quot;</tt> implementation has been fixed by avoiding a possible memory wrap. [perl #131260] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131260">https://rt.perl.org/Public/Bug/Display.html?id=131260</a>&gt;</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.24.3 represents approximately 2 months of development since Perl 5.24.2 and contains approximately 3,200 lines of changes across 120 files from 23 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 1,600 lines of changes to 56 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.24.3: </p>
<p> Aaron Crane, Craig A. Berry, Dagfinn Ilmari Mannsåker, Dan Collins, Daniel Dragan, Dave Cross, David Mitchell, Eric Herman, Father Chrysostomos, H.Merijn Brand, Hugo van der Sanden, James E Keenan, Jarkko Hietaniemi, John <font SIZE="-1">SJ</font> Anderson, Karl Williamson, Ken Brown, Lukas Mai, Matthew Horsfall, Stevan Little, Steve Hay, Steven Humphrey, Tony Cook, Yves Orton. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at &lt;<a rel="nofollow" href="https://rt.perl.org/">https://rt.perl.org/</a>&gt; . There may also be information at &lt;<a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a>&gt; , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications which make it inappropriate to send to a publicly archived mailing list, then see &#8220;<font SIZE="-1">SECURITY VULNERABILITY CONTACT INFORMATION&#8221;</font> in perlsec for details of how to report the issue.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Incompatible Changes</a></p>
<dd>
<dt><a href="#lbAI">Modules and Pragmata</a></p>
<dd>
<dt><a href="#lbAK">Configuration and Compilation</a></p>
<dd>
<dt><a href="#lbAL">Platform Support</a></p>
<dd>
<dt><a href="#lbAN">Selected Bug Fixes</a></p>
<dd>
<dt><a href="#lbAO">Acknowledgements</a></p>
<dd>
<dt><a href="#lbAP">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbAQ">SEE ALSO</a></p>
<dd></dl>
