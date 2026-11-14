---
title: "perl5130delta(1)"
name: "perl5130delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5130delta/"
description: "perl5130delta – what is new for perl v5.13.0"
---

<h2 class="name">NAME</h2>
<p> perl5130delta &#8211; what is new for perl v5.13.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.12.0 release and the 5.13.0 release. </p>
<p> If you are upgrading from an earlier release such as 5.10.0, first read perl5120delta, which describes differences between 5.10.0 and 5.12.0.</p>
<h2>Core Enhancements</h2>
<h3>safe signals optimization</h3>
<p> Signal dispatch has been moved from the runloop into control ops. This should give a few percent speed increase, and eliminates almost all of the speed penalty caused by the introduction of &#8220;safe signals&#8221; in 5.8.0. Signals should still be dispatched within the same statement as they were previously &#8211; if this is not the case, or it is possible to create uninterruptible loops, this is a bug, and reports are encouraged of how to recreate such issues.</p>
<h3>Assignment to $0 sets the legacy process name with prctl() on Linux</h3>
<p> On Linux the legacy process name will be set with <i><a href="/docs/linux/man/2-prctl/">prctl</a></i>(2), in addition to altering the <font SIZE="-1">POSIX</font> name via <tt>&quot;argv[0]&quot;</tt> as perl has done since version 4.000. Now system utilities that read the legacy process name such as ps, top and killall will recognize the name you set when assigning to <tt>$0</tt>. The string you supply will be cut off at 16 bytes, this is a limitation imposed by Linux.</p>
<h3>Optimization of shift; and pop; calls without arguments</h3>
<p> Additional two OPs are not added anymore into op tree for shift and pop calls without argument (when it works on <tt>@_</tt>). Makes <tt>&quot;shift;&quot;</tt> 5% faster over <tt>&quot;shift @_;&quot;</tt> on not threaded perl and 25% faster on threaded.</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules</h3>
<dl>
<dt><font SIZE="-1">CGI</font></p>
<dd> Updated to version 3.49.</p>
<dt>Data::Dumper</p>
<dd> Updated to version 2.126.</p>
<dt>MIME::Base64</p>
<dd> Updated to 3.09.</p>
<dt>threads</p>
<dd> Updated to version 1.77</p>
<dt>threads-shared</p>
<dd> Updated to version 1.33</dl>
<h2>Installation and Configuration Improvements</h2>
<h3>Platform Specific Changes</h3>
<dl>
<dt><font SIZE="-1">AIX</font></p>
<dd> Allow building on <font SIZE="-1">AIX</font> 4.2.</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.13.0 represents eight days of development since Perl 5.12.0 and contains 3,766 lines of changes across 151 files from 29 authors and committers. </p>
<p> Thank you to the following for contributing to this release: </p>
<p> var Arnfjo.rd<i>&#8211;</i> Bjarmason, Alex Vandiver, Chris Williams, chromatic, Craig A. Berry, David Golden, David Mitchell, Eric Brine, Father Chrysostomos, Florian Ragwitz, Frank Wiegand, Gisle Aas, H.Merijn Brand, Hugo van der Sanden, Jesse Vincent, Josh ben Jore, Karl Williamson, Leon Brocard, Michael G Schwern, Michael G. Schwern, Nga Tang Chan, Nicholas Clark, Niko Tyni, Rafael Garcia-Suarez, Ricardo Signes, Robin Barker, Slaven Rezic, Steffen Mueller, Zefram.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN</font>.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
