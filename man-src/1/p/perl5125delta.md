---
title: "perl5125delta(1)"
name: "perl5125delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5125delta/"
description: "perl5125delta – what is new for perl v5.12.5"
---
<h2 class="name">NAME</h2>
<p> perl5125delta - what is new for perl v5.12.5 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.12.4 release and the 5.12.5 release. </p>
<p> If you are upgrading from an earlier release such as 5.12.3, first read perl5124delta, which describes differences between 5.12.3 and 5.12.4.  </p>
<h2>Security</h2>
<font SIZE="-1"></font><h3>Encode decode_xs n-byte heap-overflow ( CVE-2011-2939 )</h3>
<p> A bug in <code>&quot;Encode&quot;</code> could, on certain inputs, cause the heap to overflow. This problem has been corrected. Bug reported by Robert Zacek.  </p>
<font SIZE="-1"></font><font SIZE="-1"></font><h3>File::Glob::bsd_glob() memory error with GLOB_ALTDIRFUNC ( CVE-2011-2728 ).</h3>
<p> Calling <code>&quot;File::Glob::bsd_glob&quot;</code> with the unsupported flag <font SIZE="-1">GLOB_ALTDIRFUNC</font> would cause an access violation / segfault. A Perl program that accepts a flags value from an external source could expose itself to denial of service or arbitrary code execution attacks. There are no known exploits in the wild. The problem has been corrected by explicitly disabling all unsupported flags and setting unused function pointers to null. Bug reported by Clément Lecigne.  </p>
<font SIZE="-1"></font><h3>Heap buffer overrun in 'x' string repeat operator ( CVE-2012-5195 )</h3>
<p> Poorly written perl code that allows an attacker to specify the count to perl&#8217;s &#8216;x&#8217; string repeat operator can already cause a memory exhaustion denial-of-service attack. A flaw in versions of perl before 5.15.5 can escalate that into a heap buffer overrun; coupled with versions of glibc before 2.16, it possibly allows the execution of arbitrary code. </p>
<p> This problem has been fixed.  </p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.12.4. If any exist, they are bugs and reports are welcome.  </p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules</h3>
<p> <i>B::Concise</i> </p>
<p> B::Concise no longer produces mangled output with the <code>-tree</code> option [perl #80632]. </p>
<p> <i>charnames</i> </p>
<p> A regression introduced in Perl 5.8.8 has been fixed, that caused <code>charnames::viacode(0)</code> to return <code>&quot;undef&quot;</code> instead of the string ``<font SIZE="-1">NULL&#8217;&#8216;</font> [perl #72624]. </p>
<p> <i>Encode has been upgraded from version 2.39 to version 2.39_01.</i> </p>
<p> See ``Security&#8217;&#8216;. </p>
<p> <i>File::Glob has been upgraded from version 1.07 to version 1.07_01.</i> </p>
<p> See ``Security&#8217;&#8216;. </p>
<p> <i>Unicode::UCD</i> </p>
<p> The documentation for the <code>&quot;upper&quot;</code> function now actually says ``upper&#8217;&#8216;, not ``lower&#8217;&#8216;. </p>
<p> <i>Module::CoreList</i> </p>
<p> Module::CoreList has been updated to version 2.50_02 to add data for this release.  </p>
<h2>Changes to Existing Documentation</h2>
<h3>perlebcdic</h3>
<p> The perlebcdic document contains a helpful table to use in <code>&quot;tr///&quot;</code> to convert between <font SIZE="-1">EBCDIC</font> and Latin1/ASCII. Unfortunately, the table was the inverse of the one it describes. This has been corrected.  </p>
<h3>perlunicode</h3>
<p> The section on User-Defined Case Mappings had some bad markup and unclear sentences, making parts of it unreadable. This has been rectified.  </p>
<h3>perluniprops</h3>
<p> This document has been corrected to take non-ASCII platforms into account.  </p>
<h2>Installation and Configuration Improvements</h2>
<h3>Platform Specific Changes</h3>
<dl>
<dt>Mac <font SIZE="-1">OS X</font></dt>
<dd> <p> There have been configuration and test fixes to make Perl build cleanly on Lion and Mountain Lion. </p>
 </dd>
<dt>NetBSD</dt>
<dd> <p> The NetBSD hints file was corrected to be compatible with NetBSD 6.* </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;chop&quot;</code> now correctly handles characters above ``\x{7fffffff}&#8216;&#8216; [perl #73246]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;($&lt;,$&gt;) = (...)&quot;</code> stopped working properly in 5.12.0. It is supposed to make a single <code>&quot;setreuid()&quot;</code> call, rather than calling <code>&quot;setruid()&quot;</code> and <code>&quot;seteuid()&quot;</code> separately. Consequently it did not work properly. This has been fixed [perl #75212]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a regression of <code>kill()</code> when a match variable is used for the process <font SIZE="-1">ID</font> to kill [perl #75812]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;UNIVERSAL::VERSION&quot;</code> no longer leaks memory. It started leaking in Perl 5.10.0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The C-level <code>&quot;my_strftime&quot;</code> functions no longer leaks memory. This fixes a memory leak in <code>&quot;POSIX::strftime&quot;</code> [perl #73520]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;caller&quot;</code> no longer leaks memory when called from the <font SIZE="-1">DB</font> package if <code>@DB::args</code> was assigned to after the first call to <code>&quot;caller&quot;</code>. Carp was triggering this bug [perl #97010]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Passing to <code>&quot;index&quot;</code> an offset beyond the end of the string when the string is encoded internally in <font SIZE="-1">UTF8</font> no longer causes panics [perl #75898]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Syntax errors in <code>&quot;(?{...})&quot;</code> blocks in regular expressions no longer cause panic messages [perl #2353]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl 5.10.0 introduced some faulty logic that made ``U*&#8216;&#8216; in the middle of a pack template equivalent to ``U0&#8217;&#8216; if the input string was empty. This has been fixed [perl #90160]. </p>
 </dd></dl>
<h2>Errata</h2>
<code></code><h3>split() and @_</h3>
<p> <code>split()</code> no longer modifies <code>@_</code> when called in scalar or void context. In void context it now produces a ``Useless use of split&#8217;&#8216; warning. This is actually a change introduced in perl 5.12.0, but it was missed from that release&#8217;s perl5120delta.  </p>
<h2>Acknowledgements</h2>
<p> Perl 5.12.5 represents approximately 17 months of development since Perl 5.12.4 and contains approximately 1,900 lines of changes across 64 files from 18 authors. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.12.5: </p>
<p> Andy Dougherty, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, David Mitchell, Dominic Hargreaves, Father Chrysostomos, Florian Ragwitz, George Greer, Goro Fuji, Jesse Vincent, Karl Williamson, Leon Brocard, Nicholas Clark, Rafael Garcia-Suarez, Reini Urban, Ricardo Signes, Steve Hay, Tony Cook. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
