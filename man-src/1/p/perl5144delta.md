---
title: "perl5144delta(1)"
name: "perl5144delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5144delta/"
description: "perl5144delta – what is new for perl v5.14.4"
---

<h2 class="name">NAME</h2>
<p> perl5144delta &#8211; what is new for perl v5.14.4 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.14.3 release and the 5.14.4 release. </p>
<p> If you are upgrading from an earlier release such as 5.12.0, first read perl5140delta, which describes differences between 5.12.0 and 5.14.0.</p>
<h2>Core Enhancements</h2>
<p> No changes since 5.14.0.</p>
<h2>Security</h2>
<p> This release contains one major, and medium, and a number of minor security fixes. The latter are included mainly to allow the test suite to pass cleanly with the clang compiler&#8217;s address sanitizer facility.</p>
<h3><font SIZE="-1">CVE-2013-1667:</font> memory exhaustion with arbitrary hash keys</h3>
<p> With a carefully crafted set of hash keys (for example arguments on a <font SIZE="-1">URL</font>), it is possible to cause a hash to consume a large amount of memory and <font SIZE="-1">CPU,</font> and thus possibly to achieve a Denial-of-Service. </p>
<p> This problem has been fixed.</p>
<h3>memory leak in Encode</h3>
<p> The <font SIZE="-1">UTF-8</font> encoding implementation in Encode.xs had a memory leak which has been fixed.</p>
<h3>[perl #111594] Socket::unpack_sockaddr_un heap-buffer-overflow</h3>
<p> A read buffer overflow could occur when copying <tt>&quot;sockaddr&quot;</tt> buffers. Fairly harmless. </p>
<p> This problem has been fixed.</p>
<h3>[perl #111586] SDBM_File: fix off-by-one access to global .dir</h3>
<p> An extra byte was being copied for some string literals. Fairly harmless. </p>
<p> This problem has been fixed.</p>
<h3>off-by-two error in List::Util</h3>
<p> A string literal was being used that included two bytes beyond the end of the string. Fairly harmless. </p>
<p> This problem has been fixed.</p>
<h3>[perl #115994] fix segv in regcomp.<code>c:S_join_exact()</code></h3>
<p> Under debugging builds, while marking optimised-out regex nodes as type <tt>&quot;OPTIMIZED&quot;</tt>, it could treat blocks of exact text as if they were nodes, and thus <font SIZE="-1">SEGV.</font> Fairly harmless. </p>
<p> This problem has been fixed.</p>
<h3>[perl #115992] PL_eval_start use-after-free</h3>
<p> The statement <tt>&quot;local $[;&quot;</tt>, when preceded by an <tt>&quot;eval&quot;</tt>, and when not part of an assignment, could crash. Fairly harmless. </p>
<p> This problem has been fixed.</p>
<h3>wrap-around with <font SIZE="-1">IO</font> on long strings</h3>
<p> Reading or writing strings greater than 2**31 bytes in size could segfault due to integer wraparound. </p>
<p> This problem has been fixed.</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.14.0. If any exist, they are bugs and reports are welcome.</p>
<h2>Deprecations</h2>
<p> There have been no deprecations since 5.14.0.</p>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<p> None</p>
<h3>Updated Modules and Pragmata</h3>
<p> The following modules have just the minor code fixes as listed above in &#8220;Security&#8221; (version numbers have not changed):</p>
<dl>
<dt>Socket</p>
<dd>
<dt>SDBM_File</p>
<dd>
<dt>List::Util</p>
<dd></dl>
<p> Encode has been upgraded from version 2.42_01 to version 2.42_02. </p>
<p> Module::CoreList has been updated to version 2.49_06 to add data for this release.</p>
<h3>Removed Modules and Pragmata</h3>
<p> None.</p>
<h2>Documentation</h2>
<h3>New Documentation</h3>
<p> None.</p>
<h3>Changes to Existing Documentation</h3>
<p> None.</p>
<h2>Diagnostics</h2>
<p> No new or changed diagnostics.</p>
<h2>Utility Changes</h2>
<p> None</p>
<h2>Configuration and Compilation</h2>
<p> No changes.</p>
<h2>Platform Support</h2>
<h3>New Platforms</h3>
<p> None.</p>
<h3>Discontinued Platforms</h3>
<p> None.</p>
<h3>Platform-Specific Notes</h3>
<dl>
<dt><font SIZE="-1">VMS</font></p>
<dd> 5.14.3 failed to compile on <font SIZE="-1">VMS</font> due to incomplete application of a patch series that allowed <tt>&quot;userelocatableinc&quot;</tt> and <tt>&quot;usesitecustomize&quot;</tt> to be used simultaneously. Other platforms were not affected and the problem has now been corrected.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> In Perl 5.14.0, <tt>&quot;$tainted ~~ @array&quot;</tt> stopped working properly. Sometimes it would erroneously fail (when <tt>$tainted</tt> contained a string that occurs in the array <i>after</i> the first element) or erroneously succeed (when <tt>&quot;undef&quot;</tt> occurred after the first element) [perl #93590].</dl>
<h2>Known Problems</h2>
<p> None.</p>
<h2>Acknowledgements</h2>
<p> Perl 5.14.4 represents approximately 5 months of development since Perl 5.14.3 and contains approximately 1,700 lines of changes across 49 files from 12 authors. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.14.4: </p>
<p> Andy Dougherty, Chris &#8216;BinGOs&#8217; Williams, Christian Hansen, Craig A. Berry, Dave Rolsky, David Mitchell, Dominic Hargreaves, Father Chrysostomos, Florian Ragwitz, Reini Urban, Ricardo Signes, Yves Orton. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font></p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
<dt><a href="#lbAN">Incompatible Changes</a></p>
<dd>
<dt><a href="#lbAO">Deprecations</a></p>
<dd>
<dt><a href="#lbAP">Modules and Pragmata</a></p>
<dd>
<dt><a href="#lbAT">Documentation</a></p>
<dd>
<dt><a href="#lbAW">Diagnostics</a></p>
<dd>
<dt><a href="#lbAX">Utility Changes</a></p>
<dd>
<dt><a href="#lbAY">Configuration and Compilation</a></p>
<dd>
<dt><a href="#lbAZ">Platform Support</a></p>
<dd>
<dt><a href="#lbBD">Selected Bug Fixes</a></p>
<dd>
<dt><a href="#lbBE">Known Problems</a></p>
<dd>
<dt><a href="#lbBF">Acknowledgements</a></p>
<dd>
<dt><a href="#lbBG">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbBH">SEE ALSO</a></p>
<dd></dl>
