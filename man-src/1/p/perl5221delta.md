---

title: "perl5221delta(1)"
name: "perl5221delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5221delta/"
description: "perl5221delta – what is new for perl v5.22.1"
---

<p> perl5221delta - what is new for perl v5.22.1 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.22.0 release and the 5.22.1 release. </p>
<p> If you are upgrading from an earlier release such as 5.20.0, first read perl5220delta, which describes differences between 5.20.0 and 5.22.0.  </p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.20.0 other than the following single exception, which we deemed to be a sensible change to make in order to get the new <code>&quot;\b{wb}&quot;</code> and (in particular) <code>&quot;\b{sb}&quot;</code> features sane before people decided they&#8217;re worthless because of bugs in their Perl 5.22.0 implementation and avoided them in the future. If any others exist, they are bugs, and we request that you submit a report. See ``Reporting Bugs&#8217;&#8216; below.  </p>
<h3>Bounds Checking Constructs</h3>
<p> Several bugs, including a segmentation fault, have been fixed with the bounds checking constructs (introduced in Perl 5.22) <code>&quot;\b{gcb}&quot;</code>, <code>&quot;\b{sb}&quot;</code>, <code>&quot;\b{wb}&quot;</code>, <code>&quot;\B{gcb}&quot;</code>, <code>&quot;\B{sb}&quot;</code>, and <code>&quot;\B{wb}&quot;</code>. All the <code>&quot;\B{}&quot;</code> ones now match an empty string; none of the <code>&quot;\b{}&quot;</code> ones do. [perl #126319] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126319">https://rt.perl.org/Ticket/Display.html?id=126319</a>&gt;  </p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Module::CoreList has been upgraded from version 5.20150520 to 5.20151213. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::scalar has been upgraded from version 0.22 to 0.23. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">POSIX</font> has been upgraded from version 1.53 to 1.53_01. </p>
<p> If <code>&quot;POSIX::strerror&quot;</code> was passed <code>$!</code> as its argument then it accidentally cleared <code>$!</code>. This has been fixed. [perl #126229] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126229">https://rt.perl.org/Ticket/Display.html?id=126229</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Storable has been upgraded from version 2.53 to 2.53_01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> warnings has been upgraded from version 1.32 to 1.34. </p>
<p> The <code>&quot;warnings::enabled&quot;</code> example now actually uses <code>&quot;warnings::enabled&quot;</code>. [perl #126051] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126051">https://rt.perl.org/Ticket/Display.html?id=126051</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Win32 has been upgraded from version 0.51 to 0.52. </p>
<p> This has been updated for Windows 8.1, 10 and 2012 R2 Server. </p>
 </dd></dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perltie</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The usage of <code>&quot;FIRSTKEY&quot;</code> and <code>&quot;NEXTKEY&quot;</code> has been clarified. </p>
 </dd></dl>
<p> <i>perlvar</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The specific true value of <code>$!{E...}</code> is now documented, noting that it is subject to change and not guaranteed. </p>
 </dd></dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.  </p>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;printf&quot;</code> and <code>&quot;sprintf&quot;</code> builtins are now more careful about the warnings they emit: argument reordering now disables the ``redundant argument&#8217;&#8216; warning in all cases. [perl #125469] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125469">https://rt.perl.org/Ticket/Display.html?id=125469</a>&gt; </p>
 </dd></dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Using the <code>&quot;NO_HASH_SEED&quot;</code> define in combination with the default hash algorithm <code>&quot;PERL_HASH_FUNC_ONE_AT_A_TIME_HARD&quot;</code> resulted in a fatal error while compiling the interpreter, since Perl 5.17.10. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Configuring with ccflags containing quotes (e.g. <code>&quot;-Accflags=&#8216;-DAPPLLIB_EXP=\&quot;/usr/libperl\&quot;&#8216;&quot;</code>) was broken in Perl 5.22.0 but has now been fixed again. [perl #125314] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125314">https://rt.perl.org/Ticket/Display.html?id=125314</a>&gt; </p>
 </dd></dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt><font SIZE="-1">IRIX</font></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Under some circumstances <font SIZE="-1">IRIX</font> stdio <code>fgetc()</code> and <code>fread()</code> set the errno to <code>&quot;ENOENT&quot;</code>, which made no sense according to either <font SIZE="-1">IRIX</font> or <font SIZE="-1">POSIX</font> docs. Errno is now cleared in such cases. [perl #123977] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123977">https://rt.perl.org/Ticket/Display.html?id=123977</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Problems when multiplying long doubles by infinity have been fixed. [perl #126396] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126396">https://rt.perl.org/Ticket/Display.html?id=126396</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> All tests pass now on <font SIZE="-1">IRIX</font> with the default build configuration. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;qr/(?[ () ])/&quot;</code> no longer segfaults, giving a syntax error message instead. [perl #125805] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125805">https://rt.perl.org/Ticket/Display.html?id=125805</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regular expression possessive quantifier Perl 5.20 regression now fixed. <code>&quot;qr/&quot;</code><i></i><font SIZE="-1"><i>PAT</i></font><i></i><code>&quot;{&quot;</code><i>min</i>,<i>max</i><code>&quot;}+&quot;</code><code>&quot;/&quot;</code> is supposed to behave identically to <code>&quot;qr/(?&gt;&quot;</code><i></i><font SIZE="-1"><i>PAT</i></font><i></i><code>&quot;{&quot;</code><i>min</i>,<i>max</i><code>&quot;})/&quot;</code>. Since Perl 5.20, this didn&#8217;t work if <i>min</i> and <i>max</i> were equal. [perl #125825] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125825">https://rt.perl.org/Ticket/Display.html?id=125825</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Certain syntax errors in ``Extended Bracketed Character Classes&#8217;&#8216; in perlrecharclass caused panics instead of the proper error message. This has now been fixed. [perl #126481] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126481">https://rt.perl.org/Ticket/Display.html?id=126481</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;BEGIN &lt;&gt;&quot;</code> no longer segfaults and properly produces an error message. [perl #125341] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125341">https://rt.perl.org/Ticket/Display.html?id=125341</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A regression from Perl 5.20 has been fixed, in which some syntax errors in <code>&quot;(?[...])&quot;</code> constructs within regular expression patterns could cause a segfault instead of a proper error message. [perl #126180] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126180">https://rt.perl.org/Ticket/Display.html?id=126180</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Another problem with <code>&quot;(?[...])&quot;</code> constructs has been fixed wherein things like <code>&quot;\c]&quot;</code> could cause panics. [perl #126181] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126181">https://rt.perl.org/Ticket/Display.html?id=126181</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In Perl 5.22.0, the logic changed when parsing a numeric parameter to the -C option, such that the successfully parsed number was not saved as the option value if it parsed to the end of the argument. [perl #125381] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125381">https://rt.perl.org/Ticket/Display.html?id=125381</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Warning fatality is now ignored when rewinding the stack. This prevents infinite recursion when the now fatal error also causes rewinding of the stack. [perl #123398] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123398">https://rt.perl.org/Ticket/Display.html?id=123398</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A crash with <code>&quot;%::=(); J-&gt;${\&quot;::&quot;}&quot;</code> has been fixed. [perl #125541] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125541">https://rt.perl.org/Ticket/Display.html?id=125541</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Nested quantifiers such as <code>&quot;/.{1}??/&quot;</code> should cause perl to throw a fatal error, but were being silently accepted since Perl 5.20.0. This has been fixed. [perl #126253] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126253">https://rt.perl.org/Ticket/Display.html?id=126253</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regular expression sequences such as <code>&quot;/(?i/&quot;</code> (and similarly with other recognized flags or combination of flags) should cause perl to throw a fatal error, but were being silently accepted since Perl 5.18.0. This has been fixed. [perl #126178] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126178">https://rt.perl.org/Ticket/Display.html?id=126178</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A bug in hexadecimal floating point literal support meant that high-order bits could be lost in cases where mantissa overflow was caused by too many trailing zeros in the fractional part. This has been fixed. [perl #126582] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126582">https://rt.perl.org/Ticket/Display.html?id=126582</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Another hexadecimal floating point bug, causing low-order bits to be lost in cases where the last hexadecimal digit of the mantissa has bits straddling the limit of the number of bits allowed for the mantissa, has also been fixed. [perl #126586] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126586">https://rt.perl.org/Ticket/Display.html?id=126586</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Further hexadecimal floating point bugs have been fixed: In some circumstances, the <code>%a</code> format specifier could variously lose the sign of the negative zero, fail to display zeros after the radix point with the requested precision, or even lose the radix point after the leftmost hexadecimal digit completely. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A crash caused by incomplete expressions within <code>&quot;/(?[ ])/&quot;</code> (e.g. <code>&quot;/(?[[0]+()+])/&quot;</code>) has been fixed. [perl #126615] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126615">https://rt.perl.org/Ticket/Display.html?id=126615</a>&gt; </p>
 </dd></dl>
<h2>Acknowledgements</h2>
<p> Perl 5.22.1 represents approximately 6 months of development since Perl 5.22.0 and contains approximately 19,000 lines of changes across 130 files from 27 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 1,700 lines of changes to 44 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.22.1: </p>
<p> Aaron Crane, Abigail, Andy Broad, Aristotle Pagaltzis, Chase Whitener, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, Daniel Dragan, David Mitchell, Father Chrysostomos, Herbert Breunung, Hugo van der Sanden, James E Keenan, Jan Dubois, Jarkko Hietaniemi, Karen Etheridge, Karl Williamson, Lukas Mai, Matthew Horsfall, Peter Martini, Rafael Garcia-Suarez, Ricardo Signes, Shlomi Fish, Sisyphus, Steve Hay, Tony Cook, Victor Adam. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="https://rt.perl.org/">https://rt.perl.org/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
