---
title: "perl5203delta(1)"
name: "perl5203delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5203delta/"
description: "perl5203delta – what is new for perl v5.20.3"
---

<h2 class="name">NAME</h2>
<p> perl5203delta &#8211; what is new for perl v5.20.3 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.20.2 release and the 5.20.3 release. </p>
<p> If you are upgrading from an earlier release such as 5.20.1, first read perl5202delta, which describes differences between 5.20.1 and 5.20.2.</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.20.2. If any exist, they are bugs, and we request that you submit a report. See &#8220;Reporting Bugs&#8221; below.</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> Errno has been upgraded from version 1.20_05 to 1.20_06. </p>
<p> Add <code>-P</code> to the pre-processor command-line on <font SIZE="-1">GCC 5.</font> <font SIZE="-1">GCC</font> added extra line directives, breaking parsing of error code definitions. [perl #123784] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123784">https://rt.perl.org/Ticket/Display.html?id=123784</a>&gt;</p>
<dt>&bull;</p>
<dd> Module::CoreList has been upgraded from version 5.20150214 to 5.20150822. </p>
<p> Updated to cover the latest releases of Perl.</p>
<dt>&bull;</p>
<dd> perl5db.pl has been upgraded from 1.44 to 1.44_01. </p>
<p> The debugger would cause an assertion failure. [perl #124127] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124127">https://rt.perl.org/Ticket/Display.html?id=124127</a>&gt;</dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlfunc</i></p>
<dl>
<dt>&bull;</p>
<dd> Mention that <tt>&quot;study()&quot;</tt> is currently a no-op.</dl>
<p> <i>perlguts</i></p>
<dl>
<dt>&bull;</p>
<dd> The <font SIZE="-1">OOK</font> example has been updated to account for <font SIZE="-1">COW</font> changes and a change in the storage of the offset.</dl>
<p> <i>perlhacktips</i></p>
<dl>
<dt>&bull;</p>
<dd> Documentation has been added illustrating the perils of assuming the contents of static memory pointed to by the return values of Perl wrappers for C library functions doesn&#8217;t change.</dl>
<p> <i>perlpodspec</i></p>
<dl>
<dt>&bull;</p>
<dd> The specification of the <font SIZE="-1">POD</font> language is changing so that the default encoding of PODs that aren&#8217;t in <font SIZE="-1">UTF-8</font> (unless otherwise indicated) is <font SIZE="-1">CP1252</font> instead of <font SIZE="-1">ISO-8859-1</font> (Latin1).</dl>
<h2>Utility Changes</h2>
<h3>h2ph</h3>
<dl>
<dt>&bull;</p>
<dd> <code>h2ph</code> now handles hexadecimal constants in the compiler&#8217;s predefined macro definitions, as visible in <tt>$Config{cppsymbols}</tt>. [perl #123784] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123784">https://rt.perl.org/Ticket/Display.html?id=123784</a>&gt;</dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</p>
<dd> <i>t/perf/taint.t</i> has been added to see if optimisations with taint issues are keeping things fast.</p>
<dt>&bull;</p>
<dd> <i>t/porting/re_context.t</i> has been added to test that utf8 and its dependencies only use the subset of the <tt>&quot;$1..$n&quot;</tt> capture vars that <code>Perl_save_re_context()</code> is hard-coded to localize, because that function has no efficient way of determining at runtime what vars to localize.</dl>
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
<dd> Previously, when compiling with a 64-bit Visual C<font SIZE="-2">++</font>, every Perl <font SIZE="-1">XS</font> module (including <font SIZE="-1">CPAN</font> ones) and Perl aware C file would unconditionally have around a dozen warnings from <i>hv_func.h</i>. These warnings have been silenced. <font SIZE="-1">GCC</font> (all bitness) and 32-bit Visual C<font SIZE="-2">++</font> were not affected.</p>
<dt>&bull;</p>
<dd> <code>miniperl.exe</code> is now built with <code>-fno-strict-aliasing</code>, allowing 64-bit builds to complete with <font SIZE="-1">GCC 4.8.</font> [perl #123976] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123976">https://rt.perl.org/Ticket/Display.html?id=123976</a>&gt;</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> Repeated global pattern matches in scalar context on large tainted strings were exponentially slow depending on the current match position in the string. [perl #123202] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123202">https://rt.perl.org/Ticket/Display.html?id=123202</a>&gt;</p>
<dt>&bull;</p>
<dd> The original visible value of <tt>$/</tt> is now preserved when it is set to an invalid value. Previously if you set <tt>$/</tt> to a reference to an array, for example, perl would produce a runtime error and not set PL_rs, but Perl code that checked <tt>$/</tt> would see the array reference. [perl #123218] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123218">https://rt.perl.org/Ticket/Display.html?id=123218</a>&gt;</p>
<dt>&bull;</p>
<dd> Perl 5.14.0 introduced a bug whereby <tt>&quot;eval { LABEL: }&quot;</tt> would crash. This has been fixed. [perl #123652] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123652">https://rt.perl.org/Ticket/Display.html?id=123652</a>&gt;</p>
<dt>&bull;</p>
<dd> Extending an array cloned from a parent thread could result in &#8220;Modification of a read-only value attempted&#8221; errors when attempting to modify the new elements. [perl #124127] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124127">https://rt.perl.org/Ticket/Display.html?id=124127</a>&gt;</p>
<dt>&bull;</p>
<dd> Several cases of data used to store environment variable contents in core C code being potentially overwritten before being used have been fixed. [perl #123748] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123748">https://rt.perl.org/Ticket/Display.html?id=123748</a>&gt;</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">UTF-8</font> variable names used in array indexes, unquoted <font SIZE="-1">UTF-8</font> HERE-document terminators and <font SIZE="-1">UTF-8</font> function names all now work correctly. [perl #124113] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124113">https://rt.perl.org/Ticket/Display.html?id=124113</a>&gt;</p>
<dt>&bull;</p>
<dd> A subtle bug introduced in Perl 5.20.2 involving <font SIZE="-1">UTF-8</font> in regular expressions and sometimes causing a crash has been fixed. A new test script has been added to test this fix; see under &#8220;Testing&#8221;. [perl #124109] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124109">https://rt.perl.org/Ticket/Display.html?id=124109</a>&gt;</p>
<dt>&bull;</p>
<dd> Some patterns starting with <tt>&quot;/.*..../&quot;</tt> matched against long strings have been slow since Perl 5.8, and some of the form <tt>&quot;/.*..../i&quot;</tt> have been slow since Perl 5.18. They are now all fast again. [perl #123743] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123743">https://rt.perl.org/Ticket/Display.html?id=123743</a>&gt;</p>
<dt>&bull;</p>
<dd> Warning fatality is now ignored when rewinding the stack. This prevents infinite recursion when the now fatal error also causes rewinding of the stack. [perl #123398] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123398">https://rt.perl.org/Ticket/Display.html?id=123398</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;setpgrp($nonzero)&quot;</tt> (with one argument) was accidentally changed in Perl 5.16 to mean <tt>setpgrp(0)</tt>. This has been fixed.</p>
<dt>&bull;</p>
<dd> A crash with <tt>&quot;%::=(); J-&gt;${\&quot;::&quot;}&quot;</tt> has been fixed. [perl #125541] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125541">https://rt.perl.org/Ticket/Display.html?id=125541</a>&gt;</p>
<dt>&bull;</p>
<dd> Regular expression possessive quantifier Perl 5.20 regression now fixed. <tt>&quot;qr/&quot;</tt><i></i><font SIZE="-1"><i>PAT</i></font><i></i><tt>&quot;{&quot;</tt><i>min</i>,<i>max</i><tt>&quot;}+&quot;</tt><tt>&quot;/&quot;</tt> is supposed to behave identically to <tt>&quot;qr/(?&gt;&quot;</tt><i></i><font SIZE="-1"><i>PAT</i></font><i></i><tt>&quot;{&quot;</tt><i>min</i>,<i>max</i><tt>&quot;})/&quot;</tt>. Since Perl 5.20, this didn&#8217;t work if <i>min</i> and <i>max</i> were equal. [perl #125825] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125825">https://rt.perl.org/Ticket/Display.html?id=125825</a>&gt;</p>
<dt>&bull;</p>
<dd> Code like <tt>&quot;/$a[/&quot;</tt> used to read the next line of input and treat it as though it came immediately after the opening bracket. Some invalid code consequently would parse and run, but some code caused crashes, so this is now disallowed. [perl #123712] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123712">https://rt.perl.org/Ticket/Display.html?id=123712</a>&gt;</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.20.3 represents approximately 7 months of development since Perl 5.20.2 and contains approximately 3,200 lines of changes across 99 files from 26 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 1,500 lines of changes to 43 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.20.3: </p>
<p> Alex Vandiver, Andy Dougherty, Aristotle Pagaltzis, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, Dagfinn Ilmari Mannsåker, Daniel Dragan, David Mitchell, Father Chrysostomos, H.Merijn Brand, James E Keenan, James McCoy, Jarkko Hietaniemi, Karen Etheridge, Karl Williamson, kmx, Lajos Veres, Lukas Mai, Matthew Horsfall, Petr Písař, Randy Stauner, Ricardo Signes, Sawyer X, Steve Hay, Tony Cook, Yves Orton. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="https://rt.perl.org/">https://rt.perl.org/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font></p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
