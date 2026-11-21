---

title: "perl5143delta(1)"
name: "perl5143delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5143delta/"
description: "perl5143delta – what is new for perl v5.14.3"
---

<p> perl5143delta - what is new for perl v5.14.3 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.14.2 release and the 5.14.3 release. </p>
<p> If you are upgrading from an earlier release such as 5.12.0, first read perl5140delta, which describes differences between 5.12.0 and 5.14.0.  </p>
<h2>Core Enhancements</h2>
<p> No changes since 5.14.0.  </p>
<h2>Security</h2>
<font SIZE="-1"></font><h3>Digest unsafe use of eval ( CVE-2011-3597 )</h3>
<p> The <code>&quot;Digest-&gt;new()&quot;</code> function did not properly sanitize input before using it in an <code>eval()</code> call, which could lead to the injection of arbitrary Perl code. </p>
<p> In order to exploit this flaw, the attacker would need to be able to set the algorithm name used, or be able to execute arbitrary Perl code already. </p>
<p> This problem has been fixed.  </p>
<font SIZE="-1"></font><h3>Heap buffer overrun in 'x' string repeat operator ( CVE-2012-5195 )</h3>
<p> Poorly written perl code that allows an attacker to specify the count to perl&#8217;s &#8216;x&#8217; string repeat operator can already cause a memory exhaustion denial-of-service attack. A flaw in versions of perl before 5.15.5 can escalate that into a heap buffer overrun; coupled with versions of glibc before 2.16, it possibly allows the execution of arbitrary code. </p>
<p> This problem has been fixed.  </p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.14.0. If any exist, they are bugs and reports are welcome.  </p>
<h2>Deprecations</h2>
<p> There have been no deprecations since 5.14.0.  </p>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<p> None  </p>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> PerlIO::scalar was updated to fix a bug in which opening a filehandle to a glob copy caused assertion failures (under debugging) or hangs or other erratic behaviour without debugging. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ODBM_File and NDBM_File were updated to allow building on GNU/Hurd. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::Open3 has been updated to fix a regression introduced in perl 5.12, which broke <code>&quot;IPC::Open3::open3($in, $out, $err, &#8216;-&#8216;)&quot;</code>. [perl #95748] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Digest has been upgraded from version 1.16 to 1.16_01. </p>
<p> See ``Security&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::CoreList has been updated to version 2.49_04 to add data for this release. </p>
 </dd></dl>
<h3>Removed Modules and Pragmata</h3>
<p> None  </p>
<h2>Documentation</h2>
<h3>New Documentation</h3>
<p> None  </p>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlcheat</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> perlcheat was updated to 5.14. </p>
 </dd></dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> h2ph was updated to search correctly gcc include directories on platforms such as Debian with multi-architecture support. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In Configure, the test for procselfexe was refactored into a loop. </p>
 </dd></dl>
<h2>Platform Support</h2>
<h3>New Platforms</h3>
<p> None  </p>
<h3>Discontinued Platforms</h3>
<p> None  </p>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>FreeBSD</dt>
<dd> <p> The FreeBSD hints file was corrected to be compatible with FreeBSD 10.0. </p>
 </dd>
<dt>Solaris and NetBSD</dt>
<dd> <p> Configure was updated for ``procselfexe&#8217;&#8216; support on Solaris and NetBSD. </p>
 </dd>
<dt>HP-UX</dt>
<dd> <p> <font SIZE="-1">README</font>.hpux was updated to note the existence of a broken header in HP-UX 11.00. </p>
 </dd>
<dt>Linux</dt>
<dd> <p> libutil is no longer used when compiling on Linux platforms, which avoids warnings being emitted. </p>
<p> The system gcc (rather than any other gcc which might be in the compiling user&#8217;s path) is now used when searching for libraries such as <code>&quot;-lm&quot;</code>. </p>
 </dd>
<dt>Mac <font SIZE="-1">OS X</font></dt>
<dd> <p> The locale tests were updated to reflect the behaviour of locales in Mountain Lion. </p>
 </dd>
<dt>GNU/Hurd</dt>
<dd> <p> Various build and test fixes were included for GNU/Hurd. </p>
<p> <font SIZE="-1">LFS</font> support was enabled in GNU/Hurd. </p>
 </dd>
<dt>NetBSD</dt>
<dd> <p> The NetBSD hints file was corrected to be compatible with NetBSD 6.* </p>
 </dd></dl>
<h2>Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> A regression has been fixed that was introduced in 5.14, in <code>&quot;/i&quot;</code> regular expression matching, in which a match improperly fails if the pattern is in <font SIZE="-1">UTF-8,</font> the target string is not, and a Latin-1 character precedes a character in the string that should match the pattern. [perl #101710] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In case-insensitive regular expression pattern matching, no longer on <font SIZE="-1">UTF-8</font> encoded strings does the scan for the start of match only look at the first possible position. This caused matches such as <code>&quot;&quot;f\x{FB00}&quot; =~ /ff/i&quot;</code> to fail. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The sitecustomize support was made relocatableinc aware, so that -Dusesitecustomize and -Duserelocatableinc may be used together. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The smartmatch operator (<code>&quot;~~&quot;</code>) was changed so that the right-hand side takes precedence during <code>&quot;Any ~~ Object&quot;</code> operations. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A bug has been fixed in the tainting support, in which an <code>&quot;index()&quot;</code> operation on a tainted constant would cause all other constants to become tainted. [perl #64804] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A regression has been fixed that was introduced in perl 5.12, whereby tainting errors were not correctly propagated through <code>&quot;die()&quot;</code>. [perl #111654] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A regression has been fixed that was introduced in perl 5.14, in which <code>&quot;/[[:lower:]]/i&quot;</code> and <code>&quot;/[[:upper:]]/i&quot;</code> no longer matched the opposite case. [perl #101970] </p>
 </dd></dl>
<h2>Acknowledgements</h2>
<p> Perl 5.14.3 represents approximately 12 months of development since Perl 5.14.2 and contains approximately 2,300 lines of changes across 64 files from 22 authors. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.14.3: </p>
<p> Abigail, Andy Dougherty, Carl Hayter, Chris &#8216;BinGOs&#8217; Williams, Dave Rolsky, David Mitchell, Dominic Hargreaves, Father Chrysostomos, Florian Ragwitz, H.Merijn Brand, Jilles Tjoelker, Karl Williamson, Leon Timmermans, Michael G Schwern, Nicholas Clark, Niko Tyni, Pino Toscano, Ricardo Signes, Salvador Fandiño, Samuel Thibault, Steve Hay, Tony Cook. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
