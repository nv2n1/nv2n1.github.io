---
title: "perl5142delta(1)"
name: "perl5142delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5142delta/"
---

<h2 class="name">NAME</h2>
 

 perl5142delta - what is new for perl v5.14.2 

<h2>DESCRIPTION</h2>

 This document describes differences between the 5.14.1 release and the 5.14.2 release. 

 If you are upgrading from an earlier release such as 5.14.0, first read perl5141delta, which describes differences between 5.14.0 and 5.14.1.

<h2>Core Enhancements</h2>

 No changes since 5.14.0.

<h2>Security</h2>

<h3>File::Glob::bsd_glob() memory error with <font SIZE="-1">GLOB_ALTDIRFUNC</font> (<font SIZE="-1">CVE-2011-2728</font>).</h3>

 Calling <tt>&quot;File::Glob::bsd_glob&quot;</tt> with the unsupported flag <font SIZE="-1">GLOB_ALTDIRFUNC</font> would cause an access violation / segfault. A Perl program that accepts a flags value from an external source could expose itself to denial of service or arbitrary code execution attacks. There are no known exploits in the wild. The problem has been corrected by explicitly disabling all unsupported flags and setting unused function pointers to null. Bug reported by Clément Lecigne.

<h3>Encode decode_xs n-byte heap-overflow (<font SIZE="-1">CVE-2011-2939</font>)</h3>

 A bug in <tt>&quot;Encode&quot;</tt> could, on certain inputs, cause the heap to overflow. This problem has been corrected. Bug reported by Robert Zacek.

<h2>Incompatible Changes</h2>

 There are no changes intentionally incompatible with 5.14.0. If any exist, they are bugs and reports are welcome.

<h2>Deprecations</h2>

 There have been no deprecations since 5.14.0.

<h2>Modules and Pragmata</h2>

<h3>New Modules and Pragmata</h3>

 None

<h3>Updated Modules and Pragmata</h3>

<dl>
<dt>&bull;
<dd> <font SIZE="-1">CPAN</font> has been upgraded from version 1.9600 to version 1.9600_01. 

 CPAN::Distribution has been upgraded from version 1.9602 to 1.9602_01. 

 Backported bugfixes from <font SIZE="-1">CPAN</font> version 1.9800. Ensures proper detection of <tt>&quot;configure_requires&quot;</tt> prerequisites from <font SIZE="-1">CPAN</font> Meta files in the case where <tt>&quot;dynamic_config&quot;</tt> is true. [rt.cpan.org #68835] 

 Also ensures that <tt>&quot;configure_requires&quot;</tt> is only checked in <font SIZE="-1">META</font> files, not <font SIZE="-1">MYMETA</font> files, so protect against <font SIZE="-1">MYMETA</font> generation that drops <tt>&quot;configure_requires&quot;</tt>.
<dt>&bull;
<dd> Encode has been upgraded from version 2.42 to 2.42_01. 

 See ``Security''.
<dt>&bull;
<dd> File::Glob has been upgraded from version 1.12 to version 1.13. 

 See ``Security''.
<dt>&bull;
<dd> PerlIO::scalar has been upgraded from version 0.11 to 0.11_01. 

 It fixes a problem with <tt>&quot;open my $fh, &quot;&gt;&quot;, \$scalar&quot;</tt> not working if <tt>$scalar</tt> is a copy-on-write scalar.</dl>

<h3>Removed Modules and Pragmata</h3>

 None

<h2>Platform Support</h2>

<h3>New Platforms</h3>

 None

<h3>Discontinued Platforms</h3>

 None

<h3>Platform-Specific Notes</h3>

<dl>
<dt>HP-UX <font SIZE="-1">PA-RISC/64</font> now supports gcc-4.x
<dd> A fix to correct the socketsize now makes the test suite pass on HP-UX PA-RISC for 64bitall builds.
<dt>Building on <font SIZE="-1">OS X 10.7</font> Lion and Xcode 4 works again
<dd> The build system has been updated to work with the build tools under Mac <font SIZE="-1">OS X 10.7.</font></dl>

<h2>Bug Fixes</h2>

<dl>
<dt>&bull;
<dd> In <tt>@INC</tt> filters (subroutines returned by subroutines in <tt>@INC</tt>), <tt>$_</tt> used to misbehave: If returned from a subroutine, it would not be copied, but the variable itself would be returned; and freeing <tt>$_</tt> (e.g., with <tt>&quot;undef *_&quot;</tt>) would cause perl to crash. This has been fixed [perl #91880].
<dt>&bull;
<dd> Perl 5.10.0 introduced some faulty logic that made ``U*'' in the middle of a pack template equivalent to ``U0'' if the input string was empty. This has been fixed [perl #90160].
<dt>&bull;
<dd> <tt>&quot;caller&quot;</tt> no longer leaks memory when called from the <font SIZE="-1">DB</font> package if <tt>@DB::args</tt> was assigned to after the first call to <tt>&quot;caller&quot;</tt>. Carp was triggering this bug [perl #97010].
<dt>&bull;
<dd> <tt>&quot;utf8::decode&quot;</tt> had a nasty bug that would modify copy-on-write scalars' string buffers in place (i.e., skipping the copy). This could result in hashes having two elements with the same key [perl #91834].
<dt>&bull;
<dd> Localising a tied variable used to make it read-only if it contained a copy-on-write string.
<dt>&bull;
<dd> Elements of restricted hashes (see the fields pragma) containing copy-on-write values couldn't be deleted, nor could such hashes be cleared (<tt>&quot;%hash = ()&quot;</tt>).
<dt>&bull;
<dd> Locking a hash element that is a glob copy no longer causes subsequent assignment to it to corrupt the glob.
<dt>&bull;
<dd> A panic involving the combination of the regular expression modifiers <tt>&quot;/aa&quot;</tt> introduced in 5.14.0 and the <tt>&quot;\b&quot;</tt> escape sequence has been fixed [perl #95964].</dl>

<h2>Known Problems</h2>

 This is a list of some significant unfixed bugs, which are regressions from 5.12.0.
<dl>
<dt>&bull;
<dd> <tt>&quot;PERL_GLOBAL_STRUCT&quot;</tt> is broken. 

 Since perl 5.14.0, building with <tt>&quot;-DPERL_GLOBAL_STRUCT&quot;</tt> hasn't been possible. This means that perl currently doesn't work on any platforms that require it to be built this way, including Symbian. 

 While <tt>&quot;PERL_GLOBAL_STRUCT&quot;</tt> now works again on recent development versions of perl, it actually working on Symbian again hasn't been verified. 

 We'd be very interested in hearing from anyone working with Perl on Symbian.</dl>

<h2>Acknowledgements</h2>

 Perl 5.14.2 represents approximately three months of development since Perl 5.14.1 and contains approximately 1200 lines of changes across 61 files from 9 authors. 

 Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.14.2: 

 Craig A. Berry, David Golden, Father Chrysostomos, Florian Ragwitz, H.Merijn Brand, Karl Williamson, Nicholas Clark, Pau Amma and Ricardo Signes.

<h2>Reporting Bugs</h2>

 If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" HREF="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. 

 If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. 

 If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font>

<h2>SEE ALSO</h2>

 The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. 

 The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. 

 The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. 

 The <i>Artistic</i> and <i>Copying</i> files for copyright information. 

<h2>Index</h2>



<dt><a HREF="#lbAH">Incompatible Changes</a>
<dd>
<dt><a HREF="#lbAI">Deprecations</a>
<dd>
<dt><a HREF="#lbAJ">Modules and Pragmata</a>
<dd>


<dt><a HREF="#lbAN">Platform Support</a>
<dd>


<dt><a HREF="#lbAR">Bug Fixes</a>
<dd>
<dt><a HREF="#lbAS">Known Problems</a>
<dd>
<dt><a HREF="#lbAT">Acknowledgements</a>
<dd>
<dt><a HREF="#lbAU">Reporting Bugs</a>
<dd>
<dt><a HREF="#lbAV">SEE ALSO</a>
<dd></dl>
