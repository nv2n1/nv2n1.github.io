---

title: "perl587delta(1)"
name: "perl587delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl587delta/"
description: "perl587delta – what is new for perl v5.8.7"
---

<p> perl587delta - what is new for perl v5.8.7 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.8.6 release and the 5.8.7 release.  </p>
<h2>Incompatible Changes</h2>
<p> There are no changes incompatible with 5.8.6.  </p>
<h2>Core Enhancements</h2>
<h3>Unicode Character Database 4.1.0</h3>
<p> The copy of the Unicode Character Database included in Perl 5.8 has been updated to 4.1.0 from 4.0.1. See &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode4.1.0/#NotableChanges">http://www.unicode.org/versions/Unicode4.1.0/#NotableChanges</a>&gt; for the notable changes.  </p>
<h3>suidperl less insecure</h3>
<p> A pair of exploits in <code>&quot;suidperl&quot;</code> involving debugging code have been closed. </p>
<p> For new projects the core perl team strongly recommends that you use dedicated, single purpose security tools such as <code>&quot;sudo&quot;</code> in preference to <code>&quot;suidperl&quot;</code>.  </p>
<h3>Optional site customization script</h3>
<p> The perl interpreter can be built to allow the use of a site customization script. By default this is not enabled, to be consistent with previous perl releases. To use this, add <code>&quot;-Dusesitecustomize&quot;</code> to the command line flags when running the <code>&quot;Configure&quot;</code> script. See also ``-f&#8217;&#8216; in perlrun.  </p>
<h3>Config.pm is now much smaller.</h3>
<p> <code>&quot;Config.pm&quot;</code> is now about 3K rather than 32K, with the infrequently used code and <code>%Config</code> values loaded on demand. This is transparent to the programmer, but means that most code will save parsing and loading 29K of script (for example, code that uses <code>&quot;File::Find&quot;</code>).  </p>
<h2>Modules and Pragmata</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> B upgraded to version 1.09 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> base upgraded to version 2.07 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> bignum upgraded to version 0.17 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> bytes upgraded to version 1.02 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Carp upgraded to version 1.04 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> CGI upgraded to version 3.10 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Class::ISA upgraded to version 0.33 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Data::Dumper upgraded to version 2.121_02 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DB_File upgraded to version 1.811 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::PPPort upgraded to version 3.06 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Digest upgraded to version 1.10 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Encode upgraded to version 2.10 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> FileCache upgraded to version 1.05 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Path upgraded to version 1.07 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Temp upgraded to version 0.16 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO::File upgraded to version 1.11 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO::Socket upgraded to version 1.28 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigInt upgraded to version 1.77 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigRat upgraded to version 0.15 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> overload upgraded to version 1.03 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PathTools upgraded to version 3.05 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::HTML upgraded to version 1.0503 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Perldoc upgraded to version 3.14 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::LaTeX upgraded to version 0.58 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Parser upgraded to version 1.30 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Symbol upgraded to version 1.06 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Term::ANSIColor upgraded to version 1.09 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test::Harness upgraded to version 2.48 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test::Simple upgraded to version 0.54 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Text::Wrap upgraded to version 2001.09293, to fix a bug when <code>wrap()</code> was called with a non-space separator. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> threads::shared upgraded to version 0.93 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::HiRes upgraded to version 1.66 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::Local upgraded to version 1.11 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::Normalize upgraded to version 0.32 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> utf8 upgraded to version 1.05 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Win32 upgraded to version 0.24, which provides Win32::GetFileVersion </p>
 </dd></dl>
<h2>Utility Changes</h2>
<h3>find2perl enhancements</h3>
<p> <code>&quot;find2perl&quot;</code> has new options <code>&quot;-iname&quot;</code>, <code>&quot;-path&quot;</code> and <code>&quot;-ipath&quot;</code>.  </p>
<h2>Performance Enhancements</h2>
<p> The internal pointer mapping hash used during ithreads cloning now uses an arena for memory allocation. In tests this reduced ithreads cloning time by about 10%.  </p>
<h2>Installation and Configuration Improvements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The Win32 ``dmake&#8217;&#8216; makefile.mk has been updated to make it compatible with the latest versions of dmake. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PERL_MALLOC&quot;</code>, <code>&quot;DEBUG_MSTATS&quot;</code>, <code>&quot;PERL_HASH_SEED_EXPLICIT&quot;</code> and <code>&quot;NO_HASH_SEED&quot;</code> should now work in Win32 makefiles. </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>socket()</code> function on Win32 has been fixed so that it is able to use transport providers which specify a protocol of 0 (meaning any protocol is allowed) once more. (This was broken in 5.8.6, and typically caused the use of ICMP sockets to fail.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Another obscure bug involving <code>&quot;substr&quot;</code> and UTF-8 caused by bad internal offset caching has been identified and fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A bug involving the loading of UTF-8 tables by the regexp engine has been fixed - code such as <code>&quot;&quot;\x{100}&quot; =~ /[[:print:]]/&quot;</code> will no longer give corrupt results. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Case conversion operations such as <code>&quot;uc&quot;</code> on a long Unicode string could exhaust memory. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;index&quot;</code>/<code>&quot;rindex&quot;</code> were buggy for some combinations of Unicode and non-Unicode data. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;read&quot;</code> (and presumably <code>&quot;sysread&quot;</code>) would expose the UTF-8 internals when reading from a byte oriented file handle into a UTF-8 scalar. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several <code>&quot;pack&quot;</code>/<code>&quot;unpack&quot;</code> bug fixes: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Checksums with <code>&quot;b&quot;</code> or <code>&quot;B&quot;</code> formats were broken. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;unpack&quot;</code> checksums could overflow with the <code>&quot;C&quot;</code> format. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;U0&quot;</code> and <code>&quot;C0&quot;</code> are now scoped to <code>&quot;()&quot;</code> <code>&quot;pack&quot;</code> sub-templates. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Counted length prefixes now don&#8217;t change <code>&quot;C0&quot;</code>/<code>&quot;U0&quot;</code> mode. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pack&quot;</code> <code>&quot;Z0&quot;</code> used to destroy the preceding character. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;P&quot;</code>/<code>&quot;p&quot;</code> <code>&quot;pack&quot;</code> formats used to only recognise literal <code>&quot;undef&quot;</code> </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Using closures with ithreads could cause perl to crash. This was due to failure to correctly lock internal OP structures, and has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The return value of <code>&quot;close&quot;</code> now correctly reflects any file errors that occur while flushing the handle&#8217;s data, instead of just giving failure if the actual underlying file close operation failed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;not() || 1&quot;</code> used to segfault. <code>&quot;not()&quot;</code> now behaves like <code>not(0)</code>, which was the pre 5.6.0 behaviour. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;h2ph&quot;</code> has various enhancements to cope with constructs in header files that used to result in incorrect or invalid output. </p>
 </dd></dl>
<h2>New or Changed Diagnostics</h2>
<p> There is a new taint error, ``%ENV is aliased to <code>%s</code>&#8216;&#8216;. This error is thrown when taint checks are enabled and when <code>*ENV</code> has been aliased, so that <code>%ENV</code> has no env-magic anymore and hence the environment cannot be verified as taint-free. </p>
<p> The internals of <code>&quot;pack&quot;</code> and <code>&quot;unpack&quot;</code> have been updated. All legitimate templates should work as before, but there may be some changes in the error reported for complex failure cases. Any behaviour changes for non-error cases are bugs, and should be reported.  </p>
<h2>Changed Internals</h2>
<p> There has been a fair amount of refactoring of the <code>&quot;C&quot;</code> source code, partly to make it tidier and more maintainable. The resulting object code and the <code>&quot;perl&quot;</code> binary may well be smaller than 5.8.6, and hopefully faster in some cases, but apart from this there should be no user-detectable changes. </p>
<p> <code>&quot;${^UTF8LOCALE}&quot;</code> has been added to give perl space access to <code>&quot;PL_utf8locale&quot;</code>. </p>
<p> The size of the arenas used to allocate SV heads and most SV bodies can now be changed at compile time. The old size was 1008 bytes, the new default size is 4080 bytes.  </p>
<h2>Known Problems</h2>
<p> Unicode strings returned from overloaded operators can be buggy. This is a long standing bug reported since 5.8.6 was released, but we do not yet have a suitable fix for it.  </p>
<h2>Platform Specific Problems</h2>
<p> On UNICOS, lib/Math/BigInt/t/bigintc.t hangs burning CPU. ext/B/t/bytecode.t and ext/Socket/t/socketpair.t both fail tests. These are unlikely to be resolved, as our valiant UNICOS porter&#8217;s last Cray is being decommissioned.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org.">http://bugs.perl.org.</a> There may also be information at <a rel="nofollow" href="http://www.perl.org,">http://www.perl.org,</a> the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. You can browse and search the Perl 5 bugs at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><i>INSTALL</i><i></i> file for how to build Perl. </p>
<p> The <i></i><i>README</i><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
