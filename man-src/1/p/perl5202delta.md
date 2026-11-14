---
title: "perl5202delta(1)"
name: "perl5202delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5202delta/"
description: "perl5202delta – what is new for perl v5.20.2"
---

<h2 class="name">NAME</h2>
<p> perl5202delta &#8211; what is new for perl v5.20.2 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.20.1 release and the 5.20.2 release. </p>
<p> If you are upgrading from an earlier release such as 5.20.0, first read perl5201delta, which describes differences between 5.20.0 and 5.20.1.</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.20.1. If any exist, they are bugs, and we request that you submit a report. See &#8220;Reporting Bugs&#8221; below.</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> attributes has been upgraded from version 0.22 to 0.23. </p>
<p> The usage of <tt>&quot;memEQs&quot;</tt> in the <font SIZE="-1">XS</font> has been corrected. [perl #122701] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122701">https://rt.perl.org/Ticket/Display.html?id=122701</a>&gt;</p>
<dt>&bull;</p>
<dd> Data::Dumper has been upgraded from version 2.151 to 2.151_01. </p>
<p> Fixes <font SIZE="-1">CVE-2014-4330</font> by adding a configuration variable/option to limit recursion when dumping deep data structures.</p>
<dt>&bull;</p>
<dd> Errno has been upgraded from version 1.20_03 to 1.20_05. </p>
<p> Warnings when building the <font SIZE="-1">XS</font> on Windows with the Visual C<font SIZE="-2">++</font> compiler are now avoided.</p>
<dt>&bull;</p>
<dd> feature has been upgraded from version 1.36 to 1.36_01. </p>
<p> The <tt>&quot;postderef&quot;</tt> feature has now been documented. This feature was actually added in Perl 5.20.0 but was accidentally omitted from the feature documentation until now.</p>
<dt>&bull;</p>
<dd> IO::Socket has been upgraded from version 1.37 to 1.38. </p>
<p> Document the limitations of the <code>connected()</code> method. [perl #123096] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123096">https://rt.perl.org/Ticket/Display.html?id=123096</a>&gt;</p>
<dt>&bull;</p>
<dd> Module::CoreList has been upgraded from version 5.020001 to 5.20150214. </p>
<p> The list of Perl versions covered has been updated.</p>
<dt>&bull;</p>
<dd> PathTools has been upgraded from version 3.48 to 3.48_01. </p>
<p> A warning from the <code>gcc</code> compiler is now avoided when building the <font SIZE="-1">XS.</font></p>
<dt>&bull;</p>
<dd> PerlIO::scalar has been upgraded from version 0.18 to 0.18_01. </p>
<p> Reading from a position well past the end of the scalar now correctly returns end of file. [perl #123443] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123443">https://rt.perl.org/Ticket/Display.html?id=123443</a>&gt; </p>
<p> Seeking to a negative position still fails, but no longer leaves the file position set to a negation location. </p>
<p> <tt>&quot;eof()&quot;</tt> on a <tt>&quot;PerlIO::scalar&quot;</tt> handle now properly returns true when the file position is past the 2GB mark on 32-bit systems.</p>
<dt>&bull;</p>
<dd> Storable has been upgraded from version 2.49 to 2.49_01. </p>
<p> Minor grammatical change to the documentation only.</p>
<dt>&bull;</p>
<dd> VMS::DCLsym has been upgraded from version 1.05 to 1.05_01. </p>
<p> Minor formatting change to the documentation only.</p>
<dt>&bull;</p>
<dd> VMS::Stdio has been upgraded from version 2.4 to 2.41. </p>
<p> Minor formatting change to the documentation only.</dl>
<h2>Documentation</h2>
<h3>New Documentation</h3>
<p> <i>perlunicook</i> </p>
<p> This document, by Tom Christiansen, provides examples of handling Unicode in Perl.</p>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlexperiment</i></p>
<dl>
<dt>&bull;</p>
<dd> Added reference to subroutine signatures. This feature was actually added in Perl 5.20.0 but was accidentally omitted from the experimental feature documentation until now.</dl>
<p> <i>perlpolicy</i></p>
<dl>
<dt>&bull;</p>
<dd> The process whereby features may graduate from experimental status has now been formally documented.</dl>
<p> <i>perlsyn</i></p>
<dl>
<dt>&bull;</p>
<dd> An ambiguity in the documentation of the ellipsis statement has been corrected. [perl #122661] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122661">https://rt.perl.org/Ticket/Display.html?id=122661</a>&gt;</dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.</p>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</p>
<dd> Bad symbol for scalar is now documented. This error is not new, but was not previously documented here.</p>
<dt>&bull;</p>
<dd> Missing right brace on \N{} is now documented. This error is not new, but was not previously documented here.</dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</p>
<dd> The test script <i>re/rt122747.t</i> has been added to verify that perl #122747 &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122747">https://rt.perl.org/Ticket/Display.html?id=122747</a>&gt; remains fixed.</dl>
<h2>Platform Support</h2>
<h3>Regained Platforms</h3>
<p> <font SIZE="-1">IRIX</font> and Tru64 platforms are working again. (Some <tt>&quot;make test&quot;</tt> failures remain.)</p>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">AIX</font> now sets the length in <tt>&quot;getsockopt&quot;</tt> correctly. [perl #120835] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=120835">https://rt.perl.org/Ticket/Display.html?id=120835</a>&gt;, [cpan #91183] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=91183">https://rt.cpan.org/Ticket/Display.html?id=91183</a>&gt;, [cpan #85570] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=85570">https://rt.cpan.org/Ticket/Display.html?id=85570</a>&gt;</p>
<dt>&bull;</p>
<dd> In Perl 5.20.0, <tt>$^N</tt> accidentally had the internal <font SIZE="-1">UTF8</font> flag turned off if accessed from a code block within a regular expression, effectively UTF8-encoding the value. This has been fixed. [perl #123135] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123135">https://rt.perl.org/Ticket/Display.html?id=123135</a>&gt;</p>
<dt>&bull;</p>
<dd> Various cases where the name of a sub is used (autoload, overloading, error messages) used to crash for lexical subs, but have been fixed.</p>
<dt>&bull;</p>
<dd> An assertion failure when parsing <tt>&quot;sort&quot;</tt> with debugging enabled has been fixed. [perl #122771] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122771">https://rt.perl.org/Ticket/Display.html?id=122771</a>&gt;</p>
<dt>&bull;</p>
<dd> Loading <font SIZE="-1">UTF8</font> tables during a regular expression match could cause assertion failures under debugging builds if the previous match used the very same regular expression. [perl #122747] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122747">https://rt.perl.org/Ticket/Display.html?id=122747</a>&gt;</p>
<dt>&bull;</p>
<dd> Due to a mistake in the string-copying logic, copying the value of a state variable could instead steal the value and undefine the variable. This bug, introduced in Perl 5.20, would happen mostly for long strings (1250 chars or more), but could happen for any strings under builds with copy-on-write disabled. [perl #123029] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123029">https://rt.perl.org/Ticket/Display.html?id=123029</a>&gt;</p>
<dt>&bull;</p>
<dd> Fixed a bug that could cause perl to execute an infinite loop during compilation. [perl #122995] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122995">https://rt.perl.org/Ticket/Display.html?id=122995</a>&gt;</p>
<dt>&bull;</p>
<dd> On Win32, restoring in a child pseudo-process a variable that was <tt>&quot;local()&quot;</tt>ed in a parent pseudo-process before the <tt>&quot;fork&quot;</tt> happened caused memory corruption and a crash in the child pseudo-process (and therefore <font SIZE="-1">OS</font> process). [perl #40565] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=40565">https://rt.perl.org/Ticket/Display.html?id=40565</a>&gt;</p>
<dt>&bull;</p>
<dd> Tainted constants evaluated at compile time no longer cause unrelated statements to become tainted. [perl #122669] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122669">https://rt.perl.org/Ticket/Display.html?id=122669</a>&gt;</p>
<dt>&bull;</p>
<dd> Calling <tt>&quot;write&quot;</tt> on a format with a <tt>&quot;^**&quot;</tt> field could produce a panic in <code>sv_chop()</code> if there were insufficient arguments or if the variable used to fill the field was empty. [perl #123245] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123245">https://rt.perl.org/Ticket/Display.html?id=123245</a>&gt;</p>
<dt>&bull;</p>
<dd> In Perl 5.20.0, <tt>&quot;sort CORE::fake&quot;</tt> where &#8216;fake&#8217; is anything other than a keyword started chopping of the last 6 characters and treating the result as a sort sub name. The previous behaviour of treating &#8220;CORE::fake&#8221; as a sort sub name has been restored. [perl #123410] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123410">https://rt.perl.org/Ticket/Display.html?id=123410</a>&gt;</p>
<dt>&bull;</p>
<dd> A bug in regular expression patterns that could lead to segfaults and other crashes has been fixed. This occurred only in patterns compiled with <tt>&quot;/i&quot;</tt>, while taking into account the current <font SIZE="-1">POSIX</font> locale (this usually means they have to be compiled within the scope of <tt>&quot;use locale&quot;</tt>), and there must be a string of at least 128 consecutive bytes to match. [perl #123539] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123539">https://rt.perl.org/Ticket/Display.html?id=123539</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;qr/@array(?{block})/&quot;</tt> no longer dies with &#8220;Bizarre copy of <font SIZE="-1">ARRAY&#8221;.</font> [perl #123344] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123344">https://rt.perl.org/Ticket/Display.html?id=123344</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;gmtime&quot;</tt> no longer crashes with not-a-number values. [perl #123495] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123495">https://rt.perl.org/Ticket/Display.html?id=123495</a>&gt;</p>
<dt>&bull;</p>
<dd> Certain syntax errors in substitutions, such as <tt>&quot;s/${&lt;&gt;{})//&quot;</tt>, would crash, and had done so since Perl 5.10. (In some cases the crash did not start happening until Perl 5.16.) The crash has, of course, been fixed. [perl #123542] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123542">https://rt.perl.org/Ticket/Display.html?id=123542</a>&gt;</p>
<dt>&bull;</p>
<dd> A memory leak in some regular expressions, introduced in Perl 5.20.1, has been fixed. [perl #123198] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123198">https://rt.perl.org/Ticket/Display.html?id=123198</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;formline(&quot;@...&quot;, &quot;a&quot;);&quot;</tt> would crash. The <tt>&quot;FF_CHECKNL&quot;</tt> case in <code>pp_formline()</code> didn&#8217;t set the pointer used to mark the chop position, which led to the <tt>&quot;FF_MORE&quot;</tt> case crashing with a segmentation fault. This has been fixed. [perl #123538] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123538">https://rt.perl.org/Ticket/Display.html?id=123538</a>&gt; [perl #123622] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123622">https://rt.perl.org/Ticket/Display.html?id=123622</a>&gt;</p>
<dt>&bull;</p>
<dd> A possible buffer overrun and crash when parsing a literal pattern during regular expression compilation has been fixed. [perl #123604] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123604">https://rt.perl.org/Ticket/Display.html?id=123604</a>&gt;</dl>
<h2>Known Problems</h2>
<dl>
<dt>&bull;</p>
<dd> It is a known bug that lexical subroutines cannot be used as the <tt>&quot;SUBNAME&quot;</tt> argument to <tt>&quot;sort&quot;</tt>. This will be fixed in a future version of Perl.</dl>
<h2>Errata From Previous Releases</h2>
<dl>
<dt>&bull;</p>
<dd> A regression has been fixed that was introduced in Perl 5.20.0 (fixed in Perl 5.20.1 as well as here) in which a <font SIZE="-1">UTF-8</font> encoded regular expression pattern that contains a single <font SIZE="-1">ASCII</font> lowercase letter does not match its uppercase counterpart. [perl #122655] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122655">https://rt.perl.org/Ticket/Display.html?id=122655</a>&gt;</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.20.2 represents approximately 5 months of development since Perl 5.20.1 and contains approximately 6,300 lines of changes across 170 files from 34 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 1,900 lines of changes to 80 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.20.2: </p>
<p> Aaron Crane, Abigail, Andreas Voegele, Andy Dougherty, Anthony Heading, Aristotle Pagaltzis, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, Daniel Dragan, Doug Bell, Ed J, Father Chrysostomos, Glenn D. Golden, H.Merijn Brand, Hugo van der Sanden, James E Keenan, Jarkko Hietaniemi, Jim Cromie, Karen Etheridge, Karl Williamson, kmx, Matthew Horsfall, Max Maischein, Peter Martini, Rafael Garcia-Suarez, Ricardo Signes, Shlomi Fish, Slaven Rezic, Steffen Müller, Steve Hay, Tadeusz Sośnierz, Tony Cook, Yves Orton, Ævar Arnfjörð Bjarmason. </p>
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
