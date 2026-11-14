---
title: "perl5261delta(1)"
name: "perl5261delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5261delta/"
description: "perl5261delta – what is new for perl v5.26.1"
---

<h2 class="name">NAME</h2>
<p> perl5261delta &#8211; what is new for perl v5.26.1 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.26.0 release and the 5.26.1 release. </p>
<p> If you are upgrading from an earlier release such as 5.24.0, first read perl5260delta, which describes differences between 5.24.0 and 5.26.0.</p>
<h2>Security</h2>
<h3>[<font SIZE="-1">CVE-2017-12837</font>] Heap buffer overflow in regular expression compiler</h3>
<p> Compiling certain regular expression patterns with the case-insensitive modifier could cause a heap buffer overflow and crash perl. This has now been fixed. [perl #131582] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131582">https://rt.perl.org/Public/Bug/Display.html?id=131582</a>&gt;</p>
<h3>[<font SIZE="-1">CVE-2017-12883</font>] Buffer over-read in regular expression parser</h3>
<p> For certain types of syntax error in a regular expression pattern, the error message could either contain the contents of a random, possibly large, chunk of memory, or could crash perl. This has now been fixed. [perl #131598] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131598">https://rt.perl.org/Public/Bug/Display.html?id=131598</a>&gt;</p>
<h3>[<font SIZE="-1">CVE-2017-12814</font>] $ENV{$key} stack buffer overflow on Windows</h3>
<p> A possible stack buffer overflow in the <tt>%ENV</tt> code on Windows has been fixed by removing the buffer completely since it was superfluous anyway. [perl #131665] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131665">https://rt.perl.org/Public/Bug/Display.html?id=131665</a>&gt;</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.26.0. If any exist, they are bugs, and we request that you submit a report. See &#8220;Reporting Bugs&#8221; below.</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> base has been upgraded from version 2.25 to 2.26. </p>
<p> The effects of dotless <tt>@INC</tt> on this module have been limited by the introduction of a more refined and accurate solution for removing <tt>'.'</tt> from <tt>@INC</tt> while reducing the false positives.</p>
<dt>&bull;</p>
<dd> charnames has been upgraded from version 1.44 to 1.45.</p>
<dt>&bull;</p>
<dd> Module::CoreList has been upgraded from version 5.20170530 to 5.20170922_26.</dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>FreeBSD</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Building with <code>g++</code> on FreeBSD-11.0 has been fixed. [perl #131337] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131337">https://rt.perl.org/Public/Bug/Display.html?id=131337</a>&gt;</dl>
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
<dd> Support for compiling perl on Windows using Microsoft Visual Studio 2017 (containing Visual C<font SIZE="-2">++</font> 14.1) has been added.</p>
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
<dd> Several built-in functions previously had bugs that could cause them to write to the internal stack without allocating room for the item being written. In rare situations, this could have led to a crash. These bugs have now been fixed, and if any similar bugs are introduced in future, they will be detected automatically in debugging builds. [perl #131732] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131732">https://rt.perl.org/Public/Bug/Display.html?id=131732</a>&gt;</p>
<dt>&bull;</p>
<dd> Using a symbolic ref with postderef syntax as the key in a hash lookup was yielding an assertion failure on debugging builds. [perl #131627] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131627">https://rt.perl.org/Public/Bug/Display.html?id=131627</a>&gt;</p>
<dt>&bull;</p>
<dd> List assignment (<tt>&quot;aassign&quot;</tt>) could in some rare cases allocate an entry on the mortal stack and leave the entry uninitialized. [perl #131570] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131570">https://rt.perl.org/Public/Bug/Display.html?id=131570</a>&gt;</p>
<dt>&bull;</p>
<dd> Attempting to apply an attribute to an <tt>&quot;our&quot;</tt> variable where a function of that name already exists could result in a <font SIZE="-1">NULL</font> pointer being supplied where an <font SIZE="-1">SV</font> was expected, crashing perl. [perl #131597] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131597">https://rt.perl.org/Public/Bug/Display.html?id=131597</a>&gt;</p>
<dt>&bull;</p>
<dd> The code that vivifies a typeglob out of a code ref made some false assumptions that could lead to a crash in cases such as <tt>$::{&quot;A&quot;} = sub {}; \&amp;{&quot;A&quot;}</tt>. This has now been fixed. [perl #131085] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131085">https://rt.perl.org/Public/Bug/Display.html?id=131085</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;my_atof2&quot;</tt> no longer reads beyond the terminating <font SIZE="-1">NUL,</font> which previously occurred if the decimal point is immediately before the <font SIZE="-1">NUL.</font> [perl #131526] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131526">https://rt.perl.org/Public/Bug/Display.html?id=131526</a>&gt;</p>
<dt>&bull;</p>
<dd> Occasional &#8220;Malformed <font SIZE="-1">UTF-8</font> character&#8221; crashes in <tt>&quot;s//&quot;</tt> on utf8 strings have been fixed. [perl #131575] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131575">https://rt.perl.org/Public/Bug/Display.html?id=131575</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;perldoc -f s&quot;</tt> now finds <tt>&quot;s///&quot;</tt>. [perl #131371] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131371">https://rt.perl.org/Public/Bug/Display.html?id=131371</a>&gt;</p>
<dt>&bull;</p>
<dd> Some erroneous warnings after utf8 conversion have been fixed. [perl #131190] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131190">https://rt.perl.org/Public/Bug/Display.html?id=131190</a>&gt;</p>
<dt>&bull;</p>
<dd> The <tt>&quot;jmpenv&quot;</tt> frame to catch Perl exceptions is set up lazily, and this used to be a bit too lazy. The catcher is now set up earlier, preventing some possible crashes. [perl #105930] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=105930">https://rt.perl.org/Public/Bug/Display.html?id=105930</a>&gt;</p>
<dt>&bull;</p>
<dd> Spurious &#8220;Assuming <font SIZE="-1">NOT</font> a <font SIZE="-1">POSIX</font> class&#8221; warnings have been removed. [perl #131522] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131522">https://rt.perl.org/Public/Bug/Display.html?id=131522</a>&gt;</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.26.1 represents approximately 4 months of development since Perl 5.26.0 and contains approximately 8,900 lines of changes across 85 files from 23 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 990 lines of changes to 38 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.26.1: </p>
<p> Aaron Crane, Andy Dougherty, Aristotle Pagaltzis, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, Dagfinn Ilmari Mannsåker, David Mitchell, E. Choroba, Eric Herman, Father Chrysostomos, Jacques Germishuys, James E Keenan, John <font SIZE="-1">SJ</font> Anderson, Karl Williamson, Ken Brown, Lukas Mai, Matthew Horsfall, Ricardo Signes, Sawyer X, Steve Hay, Tony Cook, Yves Orton, Zefram. </p>
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
<dt><a href="#lbAH">Incompatible Changes</a></p>
<dd>
<dt><a href="#lbAI">Modules and Pragmata</a></p>
<dd>
<dt><a href="#lbAK">Platform Support</a></p>
<dd>
<dt><a href="#lbAM">Selected Bug Fixes</a></p>
<dd>
<dt><a href="#lbAN">Acknowledgements</a></p>
<dd>
<dt><a href="#lbAO">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbAP">Give Thanks</a></p>
<dd>
<dt><a href="#lbAQ">SEE ALSO</a></p>
<dd></dl>
