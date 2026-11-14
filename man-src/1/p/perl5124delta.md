---
title: "perl5124delta(1)"
name: "perl5124delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5124delta/"
description: "perl5124delta – what is new for perl v5.12.4"
---

<h2 class="name">NAME</h2>
<p> perl5124delta &#8211; what is new for perl v5.12.4 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.12.3 release and the 5.12.4 release. </p>
<p> If you are upgrading from an earlier release such as 5.12.2, first read perl5123delta, which describes differences between 5.12.2 and 5.12.3. The major changes made in 5.12.0 are described in perl5120delta.</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.12.3. If any exist, they are bugs and reports are welcome.</p>
<h2>Selected Bug Fixes</h2>
<p> When strict &#8220;refs&#8221; mode is off, <tt>&quot;%{...}&quot;</tt> in rvalue context returns <tt>&quot;undef&quot;</tt> if its argument is undefined. An optimisation introduced in Perl 5.12.0 to make <tt>&quot;keys %{...}&quot;</tt> faster when used as a boolean did not take this into account, causing <tt>&quot;keys %{+undef}&quot;</tt> (and <tt>&quot;keys %$foo&quot;</tt> when <tt>$foo</tt> is undefined) to be an error, which it should be so in strict mode only [perl #81750]. </p>
<p> <tt>&quot;lc&quot;</tt>, <tt>&quot;uc&quot;</tt>, <tt>&quot;lcfirst&quot;</tt>, and <tt>&quot;ucfirst&quot;</tt> no longer return untainted strings when the argument is tainted. This has been broken since perl 5.8.9 [perl #87336]. </p>
<p> Fixed a case where it was possible that a freed buffer may have been read from when parsing a here document.</p>
<h2>Modules and Pragmata</h2>
<p> Module::CoreList has been upgraded from version 2.43 to 2.50.</p>
<h2>Testing</h2>
<p> The <i>cpan/CGI/t/http.t</i> test script has been fixed to work when the environment has HTTPS_* environment variables, such as <font SIZE="-1">HTTPS_PROXY.</font></p>
<h2>Documentation</h2>
<p> Updated the documentation for <code>rand()</code> in perlfunc to note that it is not cryptographically secure.</p>
<h2>Platform Specific Notes</h2>
<dl>
<dt>Linux</p>
<dd> Support Ubuntu 11.04&#8217;s new multi-arch library layout.</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.12.4 represents approximately 5 months of development since Perl 5.12.3 and contains approximately 200 lines of changes across 11 files from 8 authors. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.12.4: </p>
<p> Andy Dougherty, David Golden, David Leadbeater, Father Chrysostomos, Florian Ragwitz, Jesse Vincent, Leon Brocard, Zsbán Ambrus.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font></p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
