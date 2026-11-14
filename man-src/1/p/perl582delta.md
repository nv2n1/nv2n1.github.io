---
title: "perl582delta(1)"
name: "perl582delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl582delta/"
description: "perl582delta – what is new for perl v5.8.2"
---

<h2 class="name">NAME</h2>
<p> perl582delta &#8211; what is new for perl v5.8.2 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.8.1 release and the 5.8.2 release. </p>
<p> If you are upgrading from an earlier release such as 5.6.1, first read the perl58delta, which describes differences between 5.6.0 and 5.8.0, and the perl581delta, which describes differences between 5.8.0 and 5.8.1.</p>
<h2>Incompatible Changes</h2>
<p> For threaded builds for modules calling certain re-entrant system calls, binary compatibility was accidentally lost between 5.8.0 and 5.8.1. Binary compatibility with 5.8.0 has been restored in 5.8.2, which necessitates breaking compatibility with 5.8.1. We see this as the lesser of two evils. </p>
<p> This will only affect people who have a threaded perl 5.8.1, and compiled modules which use these calls, and now attempt to run the compiled modules with 5.8.2. The fix is to re-compile and re-install the modules using 5.8.2.</p>
<h2>Core Enhancements</h2>
<h3>Hash Randomisation</h3>
<p> The hash randomisation introduced with 5.8.1 has been amended. It transpired that although the implementation introduced in 5.8.1 was source compatible with 5.8.0, it was not binary compatible in certain cases. 5.8.2 contains an improved implementation which is both source and binary compatible with both 5.8.0 and 5.8.1, and remains robust against the form of attack which prompted the change for 5.8.1. </p>
<p> We are grateful to the Debian project for their input in this area. See &#8220;Algorithmic Complexity Attacks&#8221; in perlsec for the original rationale behind this change.</p>
<h3>Threading</h3>
<p> Several memory leaks associated with variables shared between threads have been fixed.</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules And Pragmata</h3>
<p> The following modules and pragmata have been updated since Perl 5.8.1:</p>
<dl>
<dt>Devel::PPPort</p>
<dd>
<dt>Digest::MD5</p>
<dd>
<dt>I18N::LangTags</p>
<dd>
<dt>libnet</p>
<dd>
<dt>MIME::Base64</p>
<dd>
<dt>Pod::Perldoc</p>
<dd>
<dt>strict</p>
<dd> Documentation improved</p>
<dt>Tie::Hash</p>
<dd> Documentation improved</p>
<dt>Time::HiRes</p>
<dd>
<dt>Unicode::Collate</p>
<dd>
<dt>Unicode::Normalize</p>
<dd>
<dt><font SIZE="-1">UNIVERSAL</font></p>
<dd> Documentation improved</dl>
<h2>Selected Bug Fixes</h2>
<p> Some syntax errors involving unrecognized filetest operators are now handled correctly by the parser.</p>
<h2>Changed Internals</h2>
<p> Interpreter initialization is more complete when -DMULTIPLICITY is off. This should resolve problems with initializing and destroying the Perl interpreter more than once in a single process.</p>
<h2>Platform Specific Problems</h2>
<p> Dynamic linker flags have been tweaked for Solaris and <font SIZE="-1">OS X,</font> which should solve problems seen while building some <font SIZE="-1">XS</font> modules. </p>
<p> Bugs in <font SIZE="-1">OS/2</font> sockets and tmpfile have been fixed. </p>
<p> In <font SIZE="-1">OS X</font> <tt>&quot;setreuid&quot;</tt> and friends are troublesome &#8211; perl will now work around their problems as best possible.</p>
<h2>Future Directions</h2>
<p> Starting with 5.8.3 we intend to make more frequent maintenance releases, with a smaller number of changes in each. The intent is to propagate bug fixes out to stable releases more rapidly and make upgrading stable releases less of an upheaval. This should give end users more flexibility in their choice of upgrade timing, and allow them easier assessment of the impact of upgrades. The current plan is for code freezes as follows</p>
<dl>
<dt>&bull;</p>
<dd> 5.8.3 23:59:59 <font SIZE="-1">GMT,</font> Wednesday December 31st 2003</p>
<dt>&bull;</p>
<dd> 5.8.4 23:59:59 <font SIZE="-1">GMT,</font> Wednesday March 31st 2004</p>
<dt>&bull;</p>
<dd> 5.8.5 23:59:59 <font SIZE="-1">GMT,</font> Wednesday June 30th 2004</dl>
<p> with the release following soon after, when testing is complete. </p>
<p> See &#8220;Future Directions&#8221; in perl581delta for more soothsaying.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org/.">http://bugs.perl.org/.</a> There may also be information at <a rel="nofollow" href="http://www.perl.com/,">http://www.perl.com/,</a> the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. You can browse and search the Perl 5 bugs at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a></p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
