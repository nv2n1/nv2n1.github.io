---
title: "perl5123delta(1)"
name: "perl5123delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5123delta/"
description: "perl5123delta – what is new for perl v5.12.3"
---

<h2 class="name">NAME</h2>
<p> perl5123delta &#8211; what is new for perl v5.12.3 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.12.2 release and the 5.12.3 release. </p>
<p> If you are upgrading from an earlier release such as 5.12.1, first read perl5122delta, which describes differences between 5.12.1 and 5.12.2. The major changes made in 5.12.0 are described in perl5120delta.</p>
<h2>Incompatible Changes</h2>
<pre>
    There are no changes intentionally incompatible with 5.12.2. If any
    exist, they are bugs and reports are welcome.
</pre>
<h2>Core Enhancements</h2>
<h3>keys, values work on arrays</h3>
<p> You can now use the <tt>&quot;keys&quot;</tt>, <tt>&quot;values&quot;</tt>, <tt>&quot;each&quot;</tt> builtin functions on arrays (previously you could only use them on hashes). See perlfunc for details. This is actually a change introduced in perl 5.12.0, but it was missed from that release&#8217;s perldelta.</p>
<h2>Bug Fixes</h2>
<p> &#8220;no <font SIZE="-1">VERSION&#8221;</font> will now correctly deparse with B::Deparse, as will certain constant expressions. </p>
<p> Module::Build should be more reliably pass its tests under cygwin. </p>
<p> Lvalue subroutines are again able to return copy-on-write scalars. This had been broken since version 5.10.0.</p>
<h2>Platform Specific Notes</h2>
<dl>
<dt>Solaris</p>
<dd> A separate DTrace is now build for miniperl, which means that perl can be compiled with -Dusedtrace on Solaris again.</p>
<dt><font SIZE="-1">VMS</font></p>
<dd> A number of regressions on <font SIZE="-1">VMS</font> have been fixed. In addition to minor cleanup of questionable expressions in <i>vms.c</i>, file permissions should no longer be garbled by the PerlIO layer, and spurious record boundaries should no longer be introduced by the PerlIO layer during output. </p>
<p> For more details and discussion on the latter, see: </p>
<pre>
    <a rel="nofollow" href="http://www.nntp.perl.org/group/perl.vmsperl/2010/11/msg15419.html">http://www.nntp.perl.org/group/perl.vmsperl/2010/11/msg15419.html</a>
</pre>
<dt><font SIZE="-1">VOS</font></p>
<dd> A few very small changes were made to the build process on <font SIZE="-1">VOS</font> to better support the platform. Longer-than-32-character filenames are now supported on OpenVOS, and build properly without IPv6 support.</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.12.3 represents approximately four months of development since Perl 5.12.2 and contains approximately 2500 lines of changes across 54 files from 16 authors. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.12.3: </p>
<p> Craig A. Berry, David Golden, David Leadbeater, Father Chrysostomos, Florian Ragwitz, Jesse Vincent, Karl Williamson, Nick Johnston, Nicolas Kaiser, Paul Green, Rafael Garcia-Suarez, Rainer Tammer, Ricardo Signes, Steffen Mueller, Zsbán Ambrus, Ævar Arnfjörð Bjarmason</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font></p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
