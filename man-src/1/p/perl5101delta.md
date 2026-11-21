---
title: "perl5101delta(1)"
name: "perl5101delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5101delta/"
description: "perl5101delta – what is new for perl v5.10.1"
---
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.10.0 release and the 5.10.1 release. </p>
<p> If you are upgrading from an earlier release such as 5.8.8, first read the perl5100delta, which describes differences between 5.8.8 and 5.10.0  </p>
<h2>Incompatible Changes</h2>
<h3>Switch statement changes</h3>
<p> The handling of complex expressions by the <code>&quot;given&quot;</code>/<code>&quot;when&quot;</code> switch statement has been enhanced. There are two new cases where <code>&quot;when&quot;</code> now interprets its argument as a boolean, instead of an expression to be used in a smart match: </p>
<dl>
<dt>flip-flop operators</dt>
<dd> <p> The <code>&quot;..&quot;</code> and <code>&quot;...&quot;</code> flip-flop operators are now evaluated in boolean context, following their usual semantics; see ``Range Operators&#8217;&#8216; in perlop. </p>
<p> Note that, as in perl 5.10.0, <code>&quot;when (1..10)&quot;</code> will not work to test whether a given value is an integer between 1 and 10; you should use <code>&quot;when ([1..10])&quot;</code> instead (note the array reference). </p>
<p> However, contrary to 5.10.0, evaluating the flip-flop operators in boolean context ensures it can now be useful in a <code>&quot;when()&quot;</code>, notably for implementing bistable conditions, like in: </p>
<pre><code>    when (/^=begin/ .. /^=end/) {
      # do something
    }
</code></pre>
 </dd>
<dt>defined-or operator</dt>
<dd> <p> A compound expression involving the defined-or operator, as in <code>&quot;when (expr1 // expr2)&quot;</code>, will be treated as boolean if the first expression is boolean. (This just extends the existing rule that applies to the regular or operator, as in <code>&quot;when (expr1 || expr2)&quot;</code>.) </p>
 </dd></dl>
<p> The next section details more changes brought to the semantics to the smart match operator, that naturally also modify the behaviour of the switch statements where smart matching is implicitly used.  </p>
<h3>Smart match changes</h3>
<p> <i>Changes to type-based dispatch</i> </p>
<p> The smart match operator <code>&quot;~~&quot;</code> is no longer commutative. The behaviour of a smart match now depends primarily on the type of its right hand argument. Moreover, its semantics have been adjusted for greater consistency or usefulness in several cases. While the general backwards compatibility is maintained, several changes must be noted: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Code references with an empty prototype are no longer treated specially. They are passed an argument like the other code references (even if they choose to ignore it). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;%hash ~~ sub {}&quot;</code> and <code>&quot;@array ~~ sub {}&quot;</code> now test that the subroutine returns a true value for each key of the hash (or element of the array), instead of passing the whole hash or array as a reference to the subroutine. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Due to the commutativity breakage, code references are no longer treated specially when appearing on the left of the <code>&quot;~~&quot;</code> operator, but like any vulgar scalar. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;undef ~~ %hash&quot;</code> is always false (since <code>&quot;undef&quot;</code> can&#8217;t be a key in a hash). No implicit conversion to <code>&quot;&quot;</code> is done (as was the case in perl 5.10.0). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;$scalar ~~ @array&quot;</code> now always distributes the smart match across the elements of the array. It&#8217;s true if one element in <code>@array</code> verifies <code>&quot;$scalar ~~ $element&quot;</code>. This is a generalization of the old behaviour that tested whether the array contained the scalar. </p>
 </dd></dl>
<p> The full dispatch table for the smart match operator is given in ``Smart matching in detail&#8217;&#8216; in perlsyn. </p>
<p> <i>Smart match and overloading</i> </p>
<p> According to the rule of dispatch based on the rightmost argument type, when an object overloading <code>&quot;~~&quot;</code> appears on the right side of the operator, the overload routine will always be called (with a 3rd argument set to a true value, see overload.) However, when the object will appear on the left, the overload routine will be called only when the rightmost argument is a simple scalar. This way distributivity of smart match across arrays is not broken, as well as the other behaviours with complex types (coderefs, hashes, regexes). Thus, writers of overloading routines for smart match mostly need to worry only with comparing against a scalar, and possibly with stringification overloading; the other common cases will be automatically handled consistently. </p>
<p> <code>&quot;~~&quot;</code> will now refuse to work on objects that do not overload it (in order to avoid relying on the object&#8217;s underlying structure). (However, if the object overloads the stringification or the numification operators, and if overload fallback is active, it will be used instead, as usual.)  </p>
<h3>Other incompatible changes</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The semantics of <code>&quot;use feature :5.10*&quot;</code> have changed slightly. See ``Modules and Pragmata&#8217;&#8216; for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> It is now a run-time error to use the smart match operator <code>&quot;~~&quot;</code> with an object that has no overload defined for it. (This way <code>&quot;~~&quot;</code> will not break encapsulation by matching against the object&#8217;s internal representation as a reference.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The version control system used for the development of the perl interpreter has been switched from Perforce to git. This is mainly an internal issue that only affects people actively working on the perl core; but it may have minor external visibility, for example in some of details of the output of <code>&quot;perl -V&quot;</code>. See perlrepository for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The internal structure of the <code>&quot;ext/&quot;</code> directory in the perl source has been reorganised. In general, a module <code>&quot;Foo::Bar&quot;</code> whose source was stored under <i>ext/Foo/Bar/</i> is now located under <i>ext/Foo-Bar/</i>. Also, some modules have been moved from <i>lib/</i> to <i>ext/</i>. This is purely a source tarball change, and should make no difference to the compilation or installation of perl, unless you have a very customised build process that explicitly relies on this structure, or which hard-codes the <code>&quot;nonxs_ext&quot;</code> <i>Configure</i> parameter. Specifically, this change does not by default alter the location of any files in the final installation. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> As part of the <code>&quot;Test::Harness&quot;</code> 2.x to 3.x upgrade, the experimental <code>&quot;Test::Harness::Straps&quot;</code> module has been removed. See ``Updated Modules&#8217;&#8216; for more details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> As part of the <code>&quot;ExtUtils::MakeMaker&quot;</code> upgrade, the <code>&quot;ExtUtils::MakeMaker::bytes&quot;</code> and <code>&quot;ExtUtils::MakeMaker::vmsish&quot;</code> modules have been removed from this distribution. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Module::CoreList&quot;</code> no longer contains the <code>%:patchlevel</code> hash. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> This one is actually a change introduced in 5.10.0, but it was missed from that release&#8217;s perldelta, so it is mentioned here instead. </p>
<p> A bugfix related to the handling of the <code>&quot;/m&quot;</code> modifier and <code>&quot;qr&quot;</code> resulted in a change of behaviour between 5.8.x and 5.10.0: </p>
<pre><code>    # matches in 5.8.x, doesn't match in 5.10.0
    $re = qr/^bar/; &quot;foo\nbar&quot; =~ /$re/m;
</code></pre>
 </dd></dl>
<h2>Core Enhancements</h2>
<h3>Unicode Character Database 5.1.0</h3>
<p> The copy of the Unicode Character Database included in Perl 5.10.1 has been updated to 5.1.0 from 5.0.0. See &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode5.1.0/#Notable_Changes">http://www.unicode.org/versions/Unicode5.1.0/#Notable_Changes</a>&gt; for the notable changes.  </p>
<h3>A proper interface for pluggable Method Resolution Orders</h3>
<p> As of Perl 5.10.1 there is a new interface for plugging and using method resolution orders other than the default (linear depth first search). The C3 method resolution order added in 5.10.0 has been re-implemented as a plugin, without changing its Perl-space interface. See perlmroapi for more information.  </p>
<h3>The overloading pragma</h3>
<p> This pragma allows you to lexically disable or enable overloading for some or all operations. (Yuval Kogman)  </p>
<h3>Parallel tests</h3>
<p> The core distribution can now run its regression tests in parallel on Unix-like platforms. Instead of running <code>&quot;make test&quot;</code>, set <code>&quot;TEST_JOBS&quot;</code> in your environment to the number of tests to run in parallel, and run <code>&quot;make test_harness&quot;</code>. On a Bourne-like shell, this can be done as </p>
<pre><code>    TEST_JOBS=3 make test_harness # Run 3 tests in parallel
</code></pre>
<p> An environment variable is used, rather than parallel make itself, because TAP::Harness needs to be able to schedule individual non-conflicting test scripts itself, and there is no standard interface to <code>&quot;make&quot;</code> utilities to interact with their job schedulers. </p>
<p> Note that currently some test scripts may fail when run in parallel (most notably <code>&quot;ext/IO/t/io_dir.t&quot;</code>). If necessary run just the failing scripts again sequentially and see if the failures go away.  </p>
<h3>DTrace support</h3>
<p> Some support for DTrace has been added. See ``DTrace support&#8217;&#8216; in <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i>.  </p>
<font SIZE="-1"></font><h3>Support for configure_requires in CPAN module metadata</h3>
<p> Both <code>&quot;CPAN&quot;</code> and <code>&quot;CPANPLUS&quot;</code> now support the <code>&quot;configure_requires&quot;</code> keyword in the <code>&quot;META.yml&quot;</code> metadata file included in most recent <font SIZE="-1">CPAN</font> distributions. This allows distribution authors to specify configuration prerequisites that must be installed before running <i>Makefile.PL</i> or <i>Build.PL</i>. </p>
<p> See the documentation for <code>&quot;ExtUtils::MakeMaker&quot;</code> or <code>&quot;Module::Build&quot;</code> for more on how to specify <code>&quot;configure_requires&quot;</code> when creating a distribution for <font SIZE="-1">CPAN.</font>  </p>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<dl>
<dt>&quot;autodie&quot;</dt>
<dd> <p> This is a new lexically-scoped alternative for the <code>&quot;Fatal&quot;</code> module. The bundled version is 2.06_01. Note that in this release, using a string eval when <code>&quot;autodie&quot;</code> is in effect can cause the autodie behaviour to leak into the surrounding scope. See ``<font SIZE="-1">BUGS&#8217;&#8216;</font> in autodie for more details. </p>
 </dd>
<dt>&quot;Compress::Raw::Bzip2&quot;</dt>
<dd> <p> This has been added to the core (version 2.020). </p>
 </dd>
<dt>&quot;parent&quot;</dt>
<dd> <p> This pragma establishes an <font SIZE="-1">ISA</font> relationship with base classes at compile time. It provides the key feature of <code>&quot;base&quot;</code> without the feature creep. </p>
 </dd>
<dt>&quot;Parse::CPAN::Meta&quot;</dt>
<dd> <p> This has been added to the core (version 1.39). </p>
 </dd></dl>
<h3>Pragmata Changes</h3>
<dl>
<dt>&quot;attributes&quot;</dt>
<dd> <p> Upgraded from version 0.08 to 0.09. </p>
 </dd>
<dt>&quot;attrs&quot;</dt>
<dd> <p> Upgraded from version 1.02 to 1.03. </p>
 </dd>
<dt>&quot;base&quot;</dt>
<dd> <p> Upgraded from version 2.13 to 2.14. See parent for a replacement. </p>
 </dd>
<dt>&quot;bigint&quot;</dt>
<dd> <p> Upgraded from version 0.22 to 0.23. </p>
 </dd>
<dt>&quot;bignum&quot;</dt>
<dd> <p> Upgraded from version 0.22 to 0.23. </p>
 </dd>
<dt>&quot;bigrat&quot;</dt>
<dd> <p> Upgraded from version 0.22 to 0.23. </p>
 </dd>
<dt>&quot;charnames&quot;</dt>
<dd> <p> Upgraded from version 1.06 to 1.07. </p>
<p> The Unicode <i>NameAliases.txt</i> database file has been added. This has the effect of adding some extra <code>&quot;\N&quot;</code> character names that formerly wouldn&#8217;t have been recognised; for example, <code>&quot;\N{LATIN CAPITAL LETTER GHA}&quot;</code>. </p>
 </dd>
<dt>&quot;constant&quot;</dt>
<dd> <p> Upgraded from version 1.13 to 1.17. </p>
 </dd>
<dt>&quot;feature&quot;</dt>
<dd> <p> The meaning of the <code>&quot;:5.10&quot;</code> and <code>&quot;:5.10.X&quot;</code> feature bundles has changed slightly. The last component, if any (i.e. <code>&quot;X&quot;</code>) is simply ignored. This is predicated on the assumption that new features will not, in general, be added to maintenance releases. So <code>&quot;:5.10&quot;</code> and <code>&quot;:5.10.X&quot;</code> have identical effect. This is a change to the behaviour documented for 5.10.0. </p>
 </dd>
<dt>&quot;fields&quot;</dt>
<dd> <p> Upgraded from version 2.13 to 2.14 (this was just a version bump; there were no functional changes). </p>
 </dd>
<dt>&quot;lib&quot;</dt>
<dd> <p> Upgraded from version 0.5565 to 0.62. </p>
 </dd>
<dt>&quot;open&quot;</dt>
<dd> <p> Upgraded from version 1.06 to 1.07. </p>
 </dd>
<dt>&quot;overload&quot;</dt>
<dd> <p> Upgraded from version 1.06 to 1.07. </p>
 </dd>
<dt>&quot;overloading&quot;</dt>
<dd> <p> See &quot;The <code>&quot;overloading&quot;</code> pragma&quot; above. </p>
 </dd>
<dt>&quot;version&quot;</dt>
<dd> <p> Upgraded from version 0.74 to 0.77. </p>
 </dd></dl>
<h3>Updated Modules</h3>
<dl>
<dt>&quot;Archive::Extract&quot;</dt>
<dd> <p> Upgraded from version 0.24 to 0.34. </p>
 </dd>
<dt>&quot;Archive::Tar&quot;</dt>
<dd> <p> Upgraded from version 1.38 to 1.52. </p>
 </dd>
<dt>&quot;Attribute::Handlers&quot;</dt>
<dd> <p> Upgraded from version 0.79 to 0.85. </p>
 </dd>
<dt>&quot;AutoLoader&quot;</dt>
<dd> <p> Upgraded from version 5.63 to 5.68. </p>
 </dd>
<dt>&quot;AutoSplit&quot;</dt>
<dd> <p> Upgraded from version 1.05 to 1.06. </p>
 </dd>
<dt>&quot;B&quot;</dt>
<dd> <p> Upgraded from version 1.17 to 1.22. </p>
 </dd>
<dt>&quot;B::Debug&quot;</dt>
<dd> <p> Upgraded from version 1.05 to 1.11. </p>
 </dd>
<dt>&quot;B::Deparse&quot;</dt>
<dd> <p> Upgraded from version 0.83 to 0.89. </p>
 </dd>
<dt>&quot;B::Lint&quot;</dt>
<dd> <p> Upgraded from version 1.09 to 1.11. </p>
 </dd>
<dt>&quot;B::Xref&quot;</dt>
<dd> <p> Upgraded from version 1.01 to 1.02. </p>
 </dd>
<dt>&quot;Benchmark&quot;</dt>
<dd> <p> Upgraded from version 1.10 to 1.11. </p>
 </dd>
<dt>&quot;Carp&quot;</dt>
<dd> <p> Upgraded from version 1.08 to 1.11. </p>
 </dd>
<dt>&quot;CGI&quot;</dt>
<dd> <p> Upgraded from version 3.29 to 3.43. (also includes the ``default_value for <code>popup_menu()</code>&#8216;&#8216; fix from 3.45). </p>
 </dd>
<dt>&quot;Compress::Zlib&quot;</dt>
<dd> <p> Upgraded from version 2.008 to 2.020. </p>
 </dd>
<dt>&quot;CPAN&quot;</dt>
<dd> <p> Upgraded from version 1.9205 to 1.9402. <code>&quot;CPAN::FTP&quot;</code> has a local fix to stop it being too verbose on download failure. </p>
 </dd>
<dt>&quot;CPANPLUS&quot;</dt>
<dd> <p> Upgraded from version 0.84 to 0.88. </p>
 </dd>
<dt>&quot;CPANPLUS::Dist::Build&quot;</dt>
<dd> <p> Upgraded from version 0.06_02 to 0.36. </p>
 </dd>
<dt>&quot;Cwd&quot;</dt>
<dd> <p> Upgraded from version 3.25_01 to 3.30. </p>
 </dd>
<dt>&quot;Data::Dumper&quot;</dt>
<dd> <p> Upgraded from version 2.121_14 to 2.124. </p>
 </dd>
<dt>&quot;DB&quot;</dt>
<dd> <p> Upgraded from version 1.01 to 1.02. </p>
 </dd>
<dt>&quot;DB_File&quot;</dt>
<dd> <p> Upgraded from version 1.816_1 to 1.820. </p>
 </dd>
<dt>&quot;Devel::PPPort&quot;</dt>
<dd> <p> Upgraded from version 3.13 to 3.19. </p>
 </dd>
<dt>&quot;Digest::MD5&quot;</dt>
<dd> <p> Upgraded from version 2.36_01 to 2.39. </p>
 </dd>
<dt>&quot;Digest::SHA&quot;</dt>
<dd> <p> Upgraded from version 5.45 to 5.47. </p>
 </dd>
<dt>&quot;DirHandle&quot;</dt>
<dd> <p> Upgraded from version 1.01 to 1.03. </p>
 </dd>
<dt>&quot;Dumpvalue&quot;</dt>
<dd> <p> Upgraded from version 1.12 to 1.13. </p>
 </dd>
<dt>&quot;DynaLoader&quot;</dt>
<dd> <p> Upgraded from version 1.08 to 1.10. </p>
 </dd>
<dt>&quot;Encode&quot;</dt>
<dd> <p> Upgraded from version 2.23 to 2.35. </p>
 </dd>
<dt>&quot;Errno&quot;</dt>
<dd> <p> Upgraded from version 1.10 to 1.11. </p>
 </dd>
<dt>&quot;Exporter&quot;</dt>
<dd> <p> Upgraded from version 5.62 to 5.63. </p>
 </dd>
<dt>&quot;ExtUtils::CBuilder&quot;</dt>
<dd> <p> Upgraded from version 0.21 to 0.2602. </p>
 </dd>
<dt>&quot;ExtUtils::Command&quot;</dt>
<dd> <p> Upgraded from version 1.13 to 1.16. </p>
 </dd>
<dt>&quot;ExtUtils::Constant&quot;</dt>
<dd> <p> Upgraded from 0.20 to 0.22. (Note that neither of these versions are available on <font SIZE="-1">CPAN.</font>) </p>
 </dd>
<dt>&quot;ExtUtils::Embed&quot;</dt>
<dd> <p> Upgraded from version 1.27 to 1.28. </p>
 </dd>
<dt>&quot;ExtUtils::Install&quot;</dt>
<dd> <p> Upgraded from version 1.44 to 1.54. </p>
 </dd>
<dt>&quot;ExtUtils::MakeMaker&quot;</dt>
<dd> <p> Upgraded from version 6.42 to 6.55_02. </p>
<p> Note that <code>&quot;ExtUtils::MakeMaker::bytes&quot;</code> and <code>&quot;ExtUtils::MakeMaker::vmsish&quot;</code> have been removed from this distribution. </p>
 </dd>
<dt>&quot;ExtUtils::Manifest&quot;</dt>
<dd> <p> Upgraded from version 1.51_01 to 1.56. </p>
 </dd>
<dt>&quot;ExtUtils::ParseXS&quot;</dt>
<dd> <p> Upgraded from version 2.18_02 to 2.2002. </p>
 </dd>
<dt>&quot;Fatal&quot;</dt>
<dd> <p> Upgraded from version 1.05 to 2.06_01. See also the new pragma <code>&quot;autodie&quot;</code>. </p>
 </dd>
<dt>&quot;File::Basename&quot;</dt>
<dd> <p> Upgraded from version 2.76 to 2.77. </p>
 </dd>
<dt>&quot;File::Compare&quot;</dt>
<dd> <p> Upgraded from version 1.1005 to 1.1006. </p>
 </dd>
<dt>&quot;File::Copy&quot;</dt>
<dd> <p> Upgraded from version 2.11 to 2.14. </p>
 </dd>
<dt>&quot;File::Fetch&quot;</dt>
<dd> <p> Upgraded from version 0.14 to 0.20. </p>
 </dd>
<dt>&quot;File::Find&quot;</dt>
<dd> <p> Upgraded from version 1.12 to 1.14. </p>
 </dd>
<dt>&quot;File::Path&quot;</dt>
<dd> <p> Upgraded from version 2.04 to 2.07_03. </p>
 </dd>
<dt>&quot;File::Spec&quot;</dt>
<dd> <p> Upgraded from version 3.2501 to 3.30. </p>
 </dd>
<dt>&quot;File::stat&quot;</dt>
<dd> <p> Upgraded from version 1.00 to 1.01. </p>
 </dd>
<dt>&quot;File::Temp&quot;</dt>
<dd> <p> Upgraded from version 0.18 to 0.22. </p>
 </dd>
<dt>&quot;FileCache&quot;</dt>
<dd> <p> Upgraded from version 1.07 to 1.08. </p>
 </dd>
<dt>&quot;FileHandle&quot;</dt>
<dd> <p> Upgraded from version 2.01 to 2.02. </p>
 </dd>
<dt>&quot;Filter::Simple&quot;</dt>
<dd> <p> Upgraded from version 0.82 to 0.84. </p>
 </dd>
<dt>&quot;Filter::Util::Call&quot;</dt>
<dd> <p> Upgraded from version 1.07 to 1.08. </p>
 </dd>
<dt>&quot;FindBin&quot;</dt>
<dd> <p> Upgraded from version 1.49 to 1.50. </p>
 </dd>
<dt>&quot;GDBM_File&quot;</dt>
<dd> <p> Upgraded from version 1.08 to 1.09. </p>
 </dd>
<dt>&quot;Getopt::Long&quot;</dt>
<dd> <p> Upgraded from version 2.37 to 2.38. </p>
 </dd>
<dt>&quot;Hash::Util::FieldHash&quot;</dt>
<dd> <p> Upgraded from version 1.03 to 1.04. This fixes a memory leak. </p>
 </dd>
<dt>&quot;I18N::Collate&quot;</dt>
<dd> <p> Upgraded from version 1.00 to 1.01. </p>
 </dd>
<dt>&quot;IO&quot;</dt>
<dd> <p> Upgraded from version 1.23_01 to 1.25. </p>
<p> This makes non-blocking mode work on Windows in <code>&quot;IO::Socket::INET&quot;</code> [<font SIZE="-1">CPAN</font> #43573]. </p>
 </dd>
<dt>&quot;IO::Compress::*&quot;</dt>
<dd> <p> Upgraded from version 2.008 to 2.020. </p>
 </dd>
<dt>&quot;IO::Dir&quot;</dt>
<dd> <p> Upgraded from version 1.06 to 1.07. </p>
 </dd>
<dt>&quot;IO::Handle&quot;</dt>
<dd> <p> Upgraded from version 1.27 to 1.28. </p>
 </dd>
<dt>&quot;IO::Socket&quot;</dt>
<dd> <p> Upgraded from version 1.30_01 to 1.31. </p>
 </dd>
<dt>&quot;IO::Zlib&quot;</dt>
<dd> <p> Upgraded from version 1.07 to 1.09. </p>
 </dd>
<dt>&quot;IPC::Cmd&quot;</dt>
<dd> <p> Upgraded from version 0.40_1 to 0.46. </p>
 </dd>
<dt>&quot;IPC::Open3&quot;</dt>
<dd> <p> Upgraded from version 1.02 to 1.04. </p>
 </dd>
<dt>&quot;IPC::SysV&quot;</dt>
<dd> <p> Upgraded from version 1.05 to 2.01. </p>
 </dd>
<dt>&quot;lib&quot;</dt>
<dd> <p> Upgraded from version 0.5565 to 0.62. </p>
 </dd>
<dt>&quot;List::Util&quot;</dt>
<dd> <p> Upgraded from version 1.19 to 1.21. </p>
 </dd>
<dt>&quot;Locale::MakeText&quot;</dt>
<dd> <p> Upgraded from version 1.12 to 1.13. </p>
 </dd>
<dt>&quot;Log::Message&quot;</dt>
<dd> <p> Upgraded from version 0.01 to 0.02. </p>
 </dd>
<dt>&quot;Math::BigFloat&quot;</dt>
<dd> <p> Upgraded from version 1.59 to 1.60. </p>
 </dd>
<dt>&quot;Math::BigInt&quot;</dt>
<dd> <p> Upgraded from version 1.88 to 1.89. </p>
 </dd>
<dt>&quot;Math::BigInt::FastCalc&quot;</dt>
<dd> <p> Upgraded from version 0.16 to 0.19. </p>
 </dd>
<dt>&quot;Math::BigRat&quot;</dt>
<dd> <p> Upgraded from version 0.21 to 0.22. </p>
 </dd>
<dt>&quot;Math::Complex&quot;</dt>
<dd> <p> Upgraded from version 1.37 to 1.56. </p>
 </dd>
<dt>&quot;Math::Trig&quot;</dt>
<dd> <p> Upgraded from version 1.04 to 1.20. </p>
 </dd>
<dt>&quot;Memoize&quot;</dt>
<dd> <p> Upgraded from version 1.01_02 to 1.01_03 (just a minor documentation change). </p>
 </dd>
<dt>&quot;Module::Build&quot;</dt>
<dd> <p> Upgraded from version 0.2808_01 to 0.34_02. </p>
 </dd>
<dt>&quot;Module::CoreList&quot;</dt>
<dd> <p> Upgraded from version 2.13 to 2.18. This release no longer contains the <code>%Module::CoreList::patchlevel</code> hash. </p>
 </dd>
<dt>&quot;Module::Load&quot;</dt>
<dd> <p> Upgraded from version 0.12 to 0.16. </p>
 </dd>
<dt>&quot;Module::Load::Conditional&quot;</dt>
<dd> <p> Upgraded from version 0.22 to 0.30. </p>
 </dd>
<dt>&quot;Module::Loaded&quot;</dt>
<dd> <p> Upgraded from version 0.01 to 0.02. </p>
 </dd>
<dt>&quot;Module::Pluggable&quot;</dt>
<dd> <p> Upgraded from version 3.6 to 3.9. </p>
 </dd>
<dt>&quot;NDBM_File&quot;</dt>
<dd> <p> Upgraded from version 1.07 to 1.08. </p>
 </dd>
<dt>&quot;Net::Ping&quot;</dt>
<dd> <p> Upgraded from version 2.33 to 2.36. </p>
 </dd>
<dt>&quot;NEXT&quot;</dt>
<dd> <p> Upgraded from version 0.60_01 to 0.64. </p>
 </dd>
<dt>&quot;Object::Accessor&quot;</dt>
<dd> <p> Upgraded from version 0.32 to 0.34. </p>
 </dd>
<dt>&quot;OS2::REXX&quot;</dt>
<dd> <p> Upgraded from version 1.03 to 1.04. </p>
 </dd>
<dt>&quot;Package::Constants&quot;</dt>
<dd> <p> Upgraded from version 0.01 to 0.02. </p>
 </dd>
<dt>&quot;PerlIO&quot;</dt>
<dd> <p> Upgraded from version 1.04 to 1.06. </p>
 </dd>
<dt>&quot;PerlIO::via&quot;</dt>
<dd> <p> Upgraded from version 0.04 to 0.07. </p>
 </dd>
<dt>&quot;Pod::Man&quot;</dt>
<dd> <p> Upgraded from version 2.16 to 2.22. </p>
 </dd>
<dt>&quot;Pod::Parser&quot;</dt>
<dd> <p> Upgraded from version 1.35 to 1.37. </p>
 </dd>
<dt>&quot;Pod::Simple&quot;</dt>
<dd> <p> Upgraded from version 3.05 to 3.07. </p>
 </dd>
<dt>&quot;Pod::Text&quot;</dt>
<dd> <p> Upgraded from version 3.08 to 3.13. </p>
 </dd>
<dt>&quot;POSIX&quot;</dt>
<dd> <p> Upgraded from version 1.13 to 1.17. </p>
 </dd>
<dt>&quot;Safe&quot;</dt>
<dd> <p> Upgraded from 2.12 to 2.18. </p>
 </dd>
<dt>&quot;Scalar::Util&quot;</dt>
<dd> <p> Upgraded from version 1.19 to 1.21. </p>
 </dd>
<dt>&quot;SelectSaver&quot;</dt>
<dd> <p> Upgraded from 1.01 to 1.02. </p>
 </dd>
<dt>&quot;SelfLoader&quot;</dt>
<dd> <p> Upgraded from 1.11 to 1.17. </p>
 </dd>
<dt>&quot;Socket&quot;</dt>
<dd> <p> Upgraded from 1.80 to 1.82. </p>
 </dd>
<dt>&quot;Storable&quot;</dt>
<dd> <p> Upgraded from 2.18 to 2.20. </p>
 </dd>
<dt>&quot;Switch&quot;</dt>
<dd> <p> Upgraded from version 2.13 to 2.14. Please see ``Deprecations&#8217;&#8216;. </p>
 </dd>
<dt>&quot;Symbol&quot;</dt>
<dd> <p> Upgraded from version 1.06 to 1.07. </p>
 </dd>
<dt>&quot;Sys::Syslog&quot;</dt>
<dd> <p> Upgraded from version 0.22 to 0.27. </p>
 </dd>
<dt>&quot;Term::ANSIColor&quot;</dt>
<dd> <p> Upgraded from version 1.12 to 2.00. </p>
 </dd>
<dt>&quot;Term::ReadLine&quot;</dt>
<dd> <p> Upgraded from version 1.03 to 1.04. </p>
 </dd>
<dt>&quot;Term::UI&quot;</dt>
<dd> <p> Upgraded from version 0.18 to 0.20. </p>
 </dd>
<dt>&quot;Test::Harness&quot;</dt>
<dd> <p> Upgraded from version 2.64 to 3.17. </p>
<p> Note that one side-effect of the 2.x to 3.x upgrade is that the experimental <code>&quot;Test::Harness::Straps&quot;</code> module (and its supporting <code>&quot;Assert&quot;</code>, <code>&quot;Iterator&quot;</code>, <code>&quot;Point&quot;</code> and <code>&quot;Results&quot;</code> modules) have been removed. If you still need this, then they are available in the (unmaintained) <code>&quot;Test-Harness-Straps&quot;</code> distribution on <font SIZE="-1">CPAN.</font> </p>
 </dd>
<dt>&quot;Test::Simple&quot;</dt>
<dd> <p> Upgraded from version 0.72 to 0.92. </p>
 </dd>
<dt>&quot;Text::ParseWords&quot;</dt>
<dd> <p> Upgraded from version 3.26 to 3.27. </p>
 </dd>
<dt>&quot;Text::Tabs&quot;</dt>
<dd> <p> Upgraded from version 2007.1117 to 2009.0305. </p>
 </dd>
<dt>&quot;Text::Wrap&quot;</dt>
<dd> <p> Upgraded from version 2006.1117 to 2009.0305. </p>
 </dd>
<dt>&quot;Thread::Queue&quot;</dt>
<dd> <p> Upgraded from version 2.00 to 2.11. </p>
 </dd>
<dt>&quot;Thread::Semaphore&quot;</dt>
<dd> <p> Upgraded from version 2.01 to 2.09. </p>
 </dd>
<dt>&quot;threads&quot;</dt>
<dd> <p> Upgraded from version 1.67 to 1.72. </p>
 </dd>
<dt>&quot;threads::shared&quot;</dt>
<dd> <p> Upgraded from version 1.14 to 1.29. </p>
 </dd>
<dt>&quot;Tie::RefHash&quot;</dt>
<dd> <p> Upgraded from version 1.37 to 1.38. </p>
 </dd>
<dt>&quot;Tie::StdHandle&quot;</dt>
<dd> <p> This has documentation changes, and has been assigned a version for the first time: version 4.2. </p>
 </dd>
<dt>&quot;Time::HiRes&quot;</dt>
<dd> <p> Upgraded from version 1.9711 to 1.9719. </p>
 </dd>
<dt>&quot;Time::Local&quot;</dt>
<dd> <p> Upgraded from version 1.18 to 1.1901. </p>
 </dd>
<dt>&quot;Time::Piece&quot;</dt>
<dd> <p> Upgraded from version 1.12 to 1.15. </p>
 </dd>
<dt>&quot;Unicode::Normalize&quot;</dt>
<dd> <p> Upgraded from version 1.02 to 1.03. </p>
 </dd>
<dt>&quot;Unicode::UCD&quot;</dt>
<dd> <p> Upgraded from version 0.25 to 0.27. </p>
<p> <code>&quot;charinfo()&quot;</code> now works on Unified <font SIZE="-1">CJK</font> code points added to later versions of Unicode. </p>
<p> <code>&quot;casefold()&quot;</code> has new fields returned to provide both a simpler interface and previously missing information. The old fields are retained for backwards compatibility. Information about Turkic-specific code points is now returned. </p>
<p> The documentation has been corrected and expanded. </p>
 </dd>
<dt>&quot;UNIVERSAL&quot;</dt>
<dd> <p> Upgraded from version 1.04 to 1.05. </p>
 </dd>
<dt>&quot;Win32&quot;</dt>
<dd> <p> Upgraded from version 0.34 to 0.39. </p>
 </dd>
<dt>&quot;Win32API::File&quot;</dt>
<dd> <p> Upgraded from version 0.1001_01 to 0.1101. </p>
 </dd>
<dt>&quot;XSLoader&quot;</dt>
<dd> <p> Upgraded from version 0.08 to 0.10. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<dl>
<dt><i>h2ph</i></dt>
<dd> <p> Now looks in <code>&quot;include-fixed&quot;</code> too, which is a recent addition to gcc&#8217;s search path. </p>
 </dd>
<dt><i>h2xs</i></dt>
<dd> <p> No longer incorrectly treats enum values like macros (Daniel Burr). </p>
<p> Now handles C<font SIZE="-2">++</font> style constants (<code>&quot;//&quot;</code>) properly in enums. (A patch from Rainer Weikusat was used; Daniel Burr also proposed a similar fix). </p>
 </dd>
<dt><i>perl5db.pl</i></dt>
<dd> <p> <code>&quot;LVALUE&quot;</code> subroutines now work under the debugger. </p>
<p> The debugger now correctly handles proxy constant subroutines, and subroutine stubs. </p>
 </dd>
<dt><i>perlthanks</i></dt>
<dd> <p> Perl 5.10.1 adds a new utility <i>perlthanks</i>, which is a variant of <i>perlbug</i>, but for sending non-bug-reports to the authors and maintainers of Perl. Getting nothing but bug reports can become a bit demoralising: we&#8217;ll see if this changes things. </p>
 </dd></dl>
<h2>New Documentation</h2>
<dl>
<dt>perlhaiku</dt>
<dd> <p> This contains instructions on how to build perl for the Haiku platform. </p>
 </dd>
<dt>perlmroapi</dt>
<dd> <p> This describes the new interface for pluggable Method Resolution Orders. </p>
 </dd>
<dt>perlperf</dt>
<dd> <p> This document, by Richard Foley, provides an introduction to the use of performance and optimization techniques which can be used with particular reference to perl programs. </p>
 </dd>
<dt>perlrepository</dt>
<dd> <p> This describes how to access the perl source using the <i>git</i> version control system. </p>
 </dd>
<dt>perlthanks</dt>
<dd> <p> This describes the new <i>perlthanks</i> utility. </p>
 </dd></dl>
<h2>Changes to Existing Documentation</h2>
<p> The various large <code>&quot;Changes*&quot;</code> files (which listed every change made to perl over the last 18 years) have been removed, and replaced by a small file, also called <code>&quot;Changes&quot;</code>, which just explains how that same information may be extracted from the git version control system. </p>
<p> The file <i>Porting/patching.pod</i> has been deleted, as it mainly described interacting with the old Perforce-based repository, which is now obsolete. Information still relevant has been moved to perlrepository. </p>
<p> perlapi, perlintern, perlmodlib and perltoc are now all generated at build time, rather than being shipped as part of the release.  </p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> A new internal cache means that <code>&quot;isa()&quot;</code> will often be faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under <code>&quot;use locale&quot;</code>, the locale-relevant information is now cached on read-only values, such as the list returned by <code>&quot;keys %hash&quot;</code>. This makes operations such as <code>&quot;sort keys %hash&quot;</code> in the scope of <code>&quot;use locale&quot;</code> much faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Empty <code>&quot;DESTROY&quot;</code> methods are no longer called. </p>
 </dd></dl>
<h2>Installation and Configuration Improvements</h2>
<i></i><h3>ext/ reorganisation</h3>
<p> The layout of directories in <i>ext</i> has been revised. Specifically, all extensions are now flat, and at the top level, with <code>&quot;/&quot;</code> in pathnames replaced by <code>&quot;-&quot;</code>, so that <i>ext/Data/Dumper/</i> is now <i>ext/Data-Dumper/</i>, etc. The names of the extensions as specified to <i>Configure</i>, and as reported by <code>%Config::Config</code> under the keys <code>&quot;dynamic_ext&quot;</code>, <code>&quot;known_extensions&quot;</code>, <code>&quot;nonxs_ext&quot;</code> and <code>&quot;static_ext&quot;</code> have not changed, and still use <code>&quot;/&quot;</code>. Hence this change will not have any affect once perl is installed. However, <code>&quot;Attribute::Handlers&quot;</code>, <code>&quot;Safe&quot;</code> and <code>&quot;mro&quot;</code> have now become extensions in their own right, so if you run <i>Configure</i> with options to specify an exact list of extensions to build, you will need to change it to account for this. </p>
<p> For 5.10.2, it is planned that many dual-life modules will have been moved from <i>lib</i> to <i>ext</i>; again this will have no effect on an installed perl, but will matter if you invoke <i>Configure</i> with a pre-canned list of extensions to build.  </p>
<h3>Configuration improvements</h3>
<p> If <code>&quot;vendorlib&quot;</code> and <code>&quot;vendorarch&quot;</code> are the same, then they are only added to <code>@INC</code> once. </p>
<p> <code>$Config{usedevel}</code> and the C-level <code>&quot;PERL_USE_DEVEL&quot;</code> are now defined if perl is built with <code>&quot;-Dusedevel&quot;</code>. </p>
<p> <i>Configure</i> will enable use of <code>&quot;-fstack-protector&quot;</code>, to provide protection against stack-smashing attacks, if the compiler supports it. </p>
<p> <i>Configure</i> will now determine the correct prototypes for re-entrant functions, and for <code>&quot;gconvert&quot;</code>, if you are using a C<font SIZE="-2">++</font> compiler rather than a C compiler. </p>
<p> On Unix, if you build from a tree containing a git repository, the configuration process will note the commit hash you have checked out, for display in the output of <code>&quot;perl -v&quot;</code> and <code>&quot;perl -V&quot;</code>. Unpushed local commits are automatically added to the list of local patches displayed by <code>&quot;perl -V&quot;</code>.  </p>
<h3>Compilation improvements</h3>
<p> As part of the flattening of <i>ext</i>, all extensions on all platforms are built by <i>make_ext.pl</i>. This replaces the Unix-specific <i>ext/util/make_ext</i>, VMS-specific <i>make_ext.com</i> and Win32-specific <i>win32/buildext.pl</i>.  </p>
<h3>Platform Specific Changes</h3>
<dl>
<dt><font SIZE="-1">AIX</font></dt>
<dd> <p> Removed <i>libbsd</i> for <font SIZE="-1">AIX 5L</font> and 6.1. Only <code>flock()</code> was used from <i>libbsd</i>. </p>
<p> Removed <i>libgdbm</i> for <font SIZE="-1">AIX 5L</font> and 6.1. The <i>libgdbm</i> is delivered as an optional package with the <font SIZE="-1">AIX</font> Toolbox. Unfortunately the 64 bit version is broken. </p>
<p> Hints changes mean that <font SIZE="-1">AIX 4.2</font> should work again. </p>
 </dd>
<dt>Cygwin</dt>
<dd> <p> On Cygwin we now strip the last number from the <font SIZE="-1">DLL.</font> This has been the behaviour in the cygwin.com build for years. The hints files have been updated. </p>
 </dd>
<dt>FreeBSD</dt>
<dd> <p> The hints files now identify the correct threading libraries on FreeBSD 7 and later. </p>
 </dd>
<dt>Irix</dt>
<dd> <p> We now work around a bizarre preprocessor bug in the Irix 6.5 compiler: <code>&quot;cc -E -&quot;</code> unfortunately goes into K&amp;R mode, but <code>&quot;cc -E file.c&quot;</code> doesn&#8217;t. </p>
 </dd>
<dt>Haiku</dt>
<dd> <p> Patches from the Haiku maintainers have been merged in. Perl should now build on Haiku. </p>
 </dd>
<dt>MirOS <font SIZE="-1">BSD</font></dt>
<dd> <p> Perl should now build on MirOS <font SIZE="-1">BSD.</font> </p>
 </dd>
<dt>NetBSD</dt>
<dd> <p> Hints now supports versions 5.*. </p>
 </dd>
<dt>Stratus <font SIZE="-1">VOS</font></dt>
<dd> <p> Various changes from Stratus have been merged in. </p>
 </dd>
<dt>Symbian</dt>
<dd> <p> There is now support for Symbian S60 3.2 <font SIZE="-1">SDK</font> and S60 5.0 <font SIZE="-1">SDK.</font> </p>
 </dd>
<dt>Win32</dt>
<dd> <p> Improved message window handling means that <code>&quot;alarm&quot;</code> and <code>&quot;kill&quot;</code> messages will no longer be dropped under race conditions. </p>
 </dd>
<dt><font SIZE="-1">VMS</font></dt>
<dd> <p> Reads from the in-memory temporary files of <code>&quot;PerlIO::scalar&quot;</code> used to fail if <code>$/</code> was set to a numeric reference (to indicate record-style reads). This is now fixed. </p>
<p> <font SIZE="-1">VMS</font> now supports <code>&quot;getgrgid&quot;</code>. </p>
<p> Many improvements and cleanups have been made to the <font SIZE="-1">VMS</font> file name handling and conversion code. </p>
<p> Enabling the <code>&quot;PERL_VMS_POSIX_EXIT&quot;</code> logical name now encodes a <font SIZE="-1">POSIX</font> exit status in a <font SIZE="-1">VMS</font> condition value for better interaction with <font SIZE="-1">GNV</font>&#8216;s bash shell and other utilities that depend on <font SIZE="-1">POSIX</font> exit values. See ``$?&#8216;&#8216; in perlvms for details. </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> 5.10.0 inadvertently disabled an optimisation, which caused a measurable performance drop in list assignment, such as is often used to assign function parameters from <code>@_</code>. The optimisation has been re-instated, and the performance regression fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed memory leak on <code>&quot;while (1) { map 1, 1 }&quot;</code> [<font SIZE="-1">RT</font> #53038]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some potential coredumps in PerlIO fixed [<font SIZE="-1">RT</font> #57322,54828]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The debugger now works with lvalue subroutines. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The debugger&#8217;s <code>&quot;m&quot;</code> command was broken on modules that defined constants [<font SIZE="-1">RT</font> #61222]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;crypt()&quot;</code> and string complement could return tainted values for untainted arguments [<font SIZE="-1">RT</font> #59998]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;-i.suffix&quot;</code> command-line switch now recreates the file using restricted permissions, before changing its mode to match the original file. This eliminates a potential race condition [<font SIZE="-1">RT</font> #60904]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On some Unix systems, the value in <code>$?</code> would not have the top bit set (<code>&quot;$? &amp; 128&quot;</code>) even if the child core dumped. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under some circumstances, $^R could incorrectly become undefined [<font SIZE="-1">RT</font> #57042]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> (<font SIZE="-1">XS</font>) In various hash functions, passing a pre-computed hash to when the key is <font SIZE="-1">UTF-8</font> might result in an incorrect lookup. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> (<font SIZE="-1">XS</font>) Including <i></i><font SIZE="-1"><i>XSUB</i></font><i>.h</i> before <i>perl.h</i> gave a compile-time error [<font SIZE="-1">RT</font> #57176]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;$object-&gt;isa(&#8216;Foo&#8217;)&quot;</code> would report false if the package <code>&quot;Foo&quot;</code> didn&#8217;t exist, even if the object&#8217;s <code>@ISA</code> contained <code>&quot;Foo&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various bugs in the new-to 5.10.0 mro code, triggered by manipulating <code>@ISA</code>, have been found and fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Bitwise operations on references could crash the interpreter, e.g. <code>&quot;$x=\$y; $x |= &quot;foo&quot;&quot;</code> [<font SIZE="-1">RT</font> #54956]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Patterns including alternation might be sensitive to the internal <font SIZE="-1">UTF-8</font> representation, e.g. </p>
<pre><code>    my $byte = chr(192);
    my $utf8 = chr(192); utf8::upgrade($utf8);
    $utf8 =~ /$byte|X}/i; # failed in 5.10.0
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Within UTF8-encoded Perl source files (i.e. where <code>&quot;use utf8&quot;</code> is in effect), double-quoted literal strings could be corrupted where a <code>&quot;\xNN&quot;</code>, <code>&quot;\0NNN&quot;</code> or <code>&quot;\N{}&quot;</code> is followed by a literal character with ordinal value greater than 255 [<font SIZE="-1">RT</font> #59908]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;B::Deparse&quot;</code> failed to correctly deparse various constructs: <code>&quot;readpipe STRING&quot;</code> [<font SIZE="-1">RT</font> #62428], <code>&quot;CORE::require(STRING)&quot;</code> [<font SIZE="-1">RT</font> #62488], <code>&quot;sub foo(_)&quot;</code> [<font SIZE="-1">RT</font> #62484]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using <code>&quot;setpgrp()&quot;</code> with no arguments could corrupt the perl stack. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The block form of <code>&quot;eval&quot;</code> is now specifically trappable by <code>&quot;Safe&quot;</code> and <code>&quot;ops&quot;</code>. Previously it was erroneously treated like string <code>&quot;eval&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In 5.10.0, the two characters <code>&quot;[~&quot;</code> were sometimes parsed as the smart match operator (<code>&quot;~~&quot;</code>) [<font SIZE="-1">RT</font> #63854]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In 5.10.0, the <code>&quot;*&quot;</code> quantifier in patterns was sometimes treated as <code>&quot;{0,32767}&quot;</code> [<font SIZE="-1">RT</font> #60034, #60464]. For example, this match would fail: </p>
<pre><code>    (&quot;ab&quot; x 32768) =~ /^(ab)*$/
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;shmget&quot;</code> was limited to a 32 bit segment size on a 64 bit <font SIZE="-1">OS</font> [<font SIZE="-1">RT</font> #63924]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using <code>&quot;next&quot;</code> or <code>&quot;last&quot;</code> to exit a <code>&quot;given&quot;</code> block no longer produces a spurious warning like the following: </p>
<pre><code>    Exiting given via last at foo.pl line 123
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> On Windows, <code>&#8216;.\foo&#8217;</code> and <code>&#8216;..\foo&#8217;</code> were treated differently than <code>&#8216;./foo&#8217;</code> and <code>&#8216;../foo&#8217;</code> by <code>&quot;do&quot;</code> and <code>&quot;require&quot;</code> [<font SIZE="-1">RT</font> #63492]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assigning a format to a glob could corrupt the format; e.g.: </p>
<pre><code>     *bar=*foo{FORMAT}; # foo format now bad
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Attempting to coerce a typeglob to a string or number could cause an assertion failure. The correct error message is now generated, <code>&quot;Can&#8217;t coerce GLOB to </code>$type <code>&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under <code>&quot;use filetest &#8216;access&#8217;&quot;</code>, <code>&quot;-x&quot;</code> was using the wrong access mode. This has been fixed [<font SIZE="-1">RT</font> #49003]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;length&quot;</code> on a tied scalar that returned a Unicode value would not be correct the first time. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using an array <code>&quot;tie&quot;</code> inside in array <code>&quot;tie&quot;</code> could <font SIZE="-1">SEGV.</font> This has been fixed. [<font SIZE="-1">RT</font> #51636] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A race condition inside <code>&quot;PerlIOStdio_close()&quot;</code> has been identified and fixed. This used to cause various threading issues, including SEGVs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In <code>&quot;unpack&quot;</code>, the use of <code>&quot;()&quot;</code> groups in scalar context was internally placing a list on the interpreter&#8217;s stack, which manifested in various ways, including SEGVs. This is now fixed [<font SIZE="-1">RT</font> #50256]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Magic was called twice in <code>&quot;substr&quot;</code>, <code>&quot;\&amp;$x&quot;</code>, <code>&quot;tie $x, $m&quot;</code> and <code>&quot;chop&quot;</code>. These have all been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A 5.10.0 optimisation to clear the temporary stack within the implicit loop of <code>&quot;s///ge&quot;</code> has been reverted, as it turned out to be the cause of obscure bugs in seemingly unrelated parts of the interpreter [commit ef0d4e17921ee3de]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The line numbers for warnings inside <code>&quot;elsif&quot;</code> are now correct. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;..&quot;</code> operator now works correctly with ranges whose ends are at or close to the values of the smallest and largest integers. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;binmode STDIN, &#8216;:raw&#8217;&quot;</code> could lead to segmentation faults on some platforms. This has been fixed [<font SIZE="-1">RT</font> #54828]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An off-by-one error meant that <code>&quot;index $str, ...&quot;</code> was effectively being executed as <code>&quot;index &quot;$str\0&quot;, ...&quot;</code>. This has been fixed [<font SIZE="-1">RT</font> #53746]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various leaks associated with named captures in regexes have been fixed [<font SIZE="-1">RT</font> #57024]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A weak reference to a hash would leak. This was affecting <code>&quot;DBI&quot;</code> [<font SIZE="-1">RT</font> #56908]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using (?|) in a regex could cause a segfault [<font SIZE="-1">RT</font> #59734]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of a <font SIZE="-1">UTF-8</font> <code>&quot;tr//&quot;</code> within a closure could cause a segfault [<font SIZE="-1">RT</font> #61520]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calling <code>&quot;sv_chop()&quot;</code> or otherwise upgrading an <font SIZE="-1">SV</font> could result in an unaligned 64-bit access on the <font SIZE="-1">SPARC</font> architecture [<font SIZE="-1">RT</font> #60574]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In the 5.10.0 release, <code>&quot;inc_version_list&quot;</code> would incorrectly list <code>&quot;5.10.*&quot;</code> after <code>&quot;5.8.*&quot;</code>; this affected the <code>@INC</code> search order [<font SIZE="-1">RT</font> #67628]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In 5.10.0, <code>&quot;pack &quot;a*&quot;, $tainted_value&quot;</code> returned a non-tainted value [<font SIZE="-1">RT</font> #52552]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In 5.10.0, <code>&quot;printf&quot;</code> and <code>&quot;sprintf&quot;</code> could produce the fatal error <code>&quot;panic: utf8_mg_pos_cache_update&quot;</code> when printing <font SIZE="-1">UTF-8</font> strings [<font SIZE="-1">RT</font> #62666]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In the 5.10.0 release, a dynamically created <code>&quot;AUTOLOAD&quot;</code> method might be missed (method cache issue) [<font SIZE="-1">RT</font> #60220,60232]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In the 5.10.0 release, a combination of <code>&quot;use feature&quot;</code> and <code>&quot;//ee&quot;</code> could cause a memory leak [<font SIZE="-1">RT</font> #63110]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-C&quot;</code> on the shebang (<code>&quot;#!&quot;</code>) line is once more permitted if it is also specified on the command line. <code>&quot;-C&quot;</code> on the shebang line used to be a silent no-op <i>if</i> it was not also on the command line, so perl 5.10.0 disallowed it, which broke some scripts. Now perl checks whether it is also on the command line and only dies if it is not [<font SIZE="-1">RT</font> #67880]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In 5.10.0, certain types of re-entrant regular expression could crash, or cause the following assertion failure [<font SIZE="-1">RT</font> #60508]: </p>
<pre><code>    Assertion rx-&gt;sublen &gt;= (s - rx-&gt;subbeg) + i failed
</code></pre>
 </dd></dl>
<h2>New or Changed Diagnostics</h2>
<dl>
<dt>&quot;panic: sv_chop %s&quot;</dt>
<dd> <p> This new fatal error occurs when the C routine <code>&quot;Perl_sv_chop()&quot;</code> was passed a position that is not within the scalar&#8217;s string buffer. This could be caused by buggy <font SIZE="-1">XS</font> code, and at this point recovery is not possible. </p>
 </dd>
<dt>&quot;Can&#8217;t locate package %s for the parents of %s&quot;</dt>
<dd> <p> This warning has been removed. In general, it only got produced in conjunction with other warnings, and removing it allowed an <font SIZE="-1">ISA</font> lookup optimisation to be added. </p>
 </dd>
<dt>&quot;v-string in use/require is non-portable&quot;</dt>
<dd> <p> This warning has been removed. </p>
 </dd>
<dt>&quot;Deep recursion on subroutine &quot;%s&quot;&quot;</dt>
<dd> <p> It is now possible to change the depth threshold for this warning from the default of 100, by recompiling the <i>perl</i> binary, setting the C pre-processor macro <code>&quot;PERL_SUB_DEPTH_WARN&quot;</code> to the desired value. </p>
 </dd></dl>
<h2>Changed Internals</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The J.R.R. Tolkien quotes at the head of C source file have been checked and proper citations added, thanks to a patch from Tom Christiansen. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;vcroak()&quot;</code> now accepts a null first argument. In addition, a full audit was made of the ``not <font SIZE="-1">NULL&#8217;&#8216;</font> compiler annotations, and those for several other internal functions were corrected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> New macros <code>&quot;dSAVEDERRNO&quot;</code>, <code>&quot;dSAVE_ERRNO&quot;</code>, <code>&quot;SAVE_ERRNO&quot;</code>, <code>&quot;RESTORE_ERRNO&quot;</code> have been added to formalise the temporary saving of the <code>&quot;errno&quot;</code> variable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The function <code>&quot;Perl_sv_insert_flags&quot;</code> has been added to augment <code>&quot;Perl_sv_insert&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The function <code>&quot;Perl_newSV_type(type)&quot;</code> has been added, equivalent to <code>&quot;Perl_newSV()&quot;</code> followed by <code>&quot;Perl_sv_upgrade(type)&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The function <code>&quot;Perl_newSVpvn_flags()&quot;</code> has been added, equivalent to <code>&quot;Perl_newSVpvn()&quot;</code> and then performing the action relevant to the flag. </p>
<p> Two flag bits are currently supported. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&quot;SVf_UTF8&quot;</dt>
<dd> <p> This will call <code>&quot;SvUTF8_on()&quot;</code> for you. (Note that this does not convert an sequence of <font SIZE="-1">ISO 8859-1</font> characters to <font SIZE="-1">UTF-8</font>). A wrapper, <code>&quot;newSVpvn_utf8()&quot;</code> is available for this. </p>
 </dd>
<dt>&quot;SVs_TEMP&quot;</dt>
<dd> <p> Call <code>&quot;sv_2mortal()&quot;</code> on the new <font SIZE="-1">SV.</font> </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> There is also a wrapper that takes constant strings, <code>&quot;newSVpvs_flags()&quot;</code>. </p>
 </dd></dl>
<dt>&bull;</dt>
<dd> <p> The function <code>&quot;Perl_croak_xs_usage&quot;</code> has been added as a wrapper to <code>&quot;Perl_croak&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The functions <code>&quot;PerlIO_find_layer&quot;</code> and <code>&quot;PerlIO_list_alloc&quot;</code> are now exported. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PL_na&quot;</code> has been exterminated from the core code, replaced by local <font SIZE="-1">STRLEN</font> temporaries, or <code>&quot;*_nolen()&quot;</code> calls. Either approach is faster than <code>&quot;PL_na&quot;</code>, which is a pointer deference into the interpreter structure under ithreads, and a global variable otherwise. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Perl_mg_free()&quot;</code> used to leave freed memory accessible via <code>SvMAGIC()</code> on the scalar. It now updates the linked list to remove each piece of magic as it is freed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under ithreads, the regex in <code>&quot;PL_reg_curpm&quot;</code> is now reference counted. This eliminates a lot of hackish workarounds to cope with it not being reference counted. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Perl_mg_magical()&quot;</code> would sometimes incorrectly turn on <code>&quot;SvRMAGICAL()&quot;</code>. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <i>public</i> <font SIZE="-1">IV</font> and <font SIZE="-1">NV</font> flags are now not set if the string value has trailing ``garbage&#8217;&#8216;. This behaviour is consistent with not setting the public <font SIZE="-1">IV</font> or <font SIZE="-1">NV</font> flags if the value is out of range for the type. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">SV</font> allocation tracing has been added to the diagnostics enabled by <code>&quot;-Dm&quot;</code>. The tracing can alternatively output via the <code>&quot;PERL_MEM_LOG&quot;</code> mechanism, if that was enabled when the <i>perl</i> binary was compiled. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Uses of <code>&quot;Nullav&quot;</code>, <code>&quot;Nullcv&quot;</code>, <code>&quot;Nullhv&quot;</code>, <code>&quot;Nullop&quot;</code>, <code>&quot;Nullsv&quot;</code> etc have been replaced by <code>&quot;NULL&quot;</code> in the core code, and non-dual-life modules, as <code>&quot;NULL&quot;</code> is clearer to those unfamiliar with the core code. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A macro <code>MUTABLE_PTR(p)</code> has been added, which on (non-pedantic) gcc will not cast away <code>&quot;const&quot;</code>, returning a <code>&quot;void *&quot;</code>. Macros <code>&quot;MUTABLE_SV(av)&quot;</code>, <code>&quot;MUTABLE_SV(cv)&quot;</code> etc build on this, casting to <code>&quot;AV *&quot;</code> etc without casting away <code>&quot;const&quot;</code>. This allows proper compile-time auditing of <code>&quot;const&quot;</code> correctness in the core, and helped picked up some errors (now fixed). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Macros <code>&quot;mPUSHs()&quot;</code> and <code>&quot;mXPUSHs()&quot;</code> have been added, for pushing SVs on the stack and mortalizing them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of the private structure <code>&quot;mro_meta&quot;</code> has changed slightly. Nothing outside the core should be accessing this directly anyway. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new tool, <code>&quot;Porting/expand-macro.pl&quot;</code> has been added, that allows you to view how a C preprocessor macro would be expanded when compiled. This is handy when trying to decode the macro hell that is the perl guts. </p>
 </dd></dl>
<h2>New Tests</h2>
<p> Many modules updated from <font SIZE="-1">CPAN</font> incorporate new tests. </p>
<p> Several tests that have the potential to hang forever if they fail now incorporate a ``watchdog&#8217;&#8216; functionality that will kill them after a timeout, which helps ensure that <code>&quot;make test&quot;</code> and <code>&quot;make test_harness&quot;</code> run to completion automatically. (Jerry Hedden). </p>
<p> Some core-specific tests have been added: </p>
<dl>
<dt>t/comp/retainedlines.t</dt>
<dd> <p> Check that the debugger can retain source lines from <code>&quot;eval&quot;</code>. </p>
 </dd>
<dt>t/io/perlio_fail.t</dt>
<dd> <p> Check that bad layers fail. </p>
 </dd>
<dt>t/io/perlio_leaks.t</dt>
<dd> <p> Check that PerlIO layers are not leaking. </p>
 </dd>
<dt>t/io/perlio_open.t</dt>
<dd> <p> Check that certain special forms of open work. </p>
 </dd>
<dt>t/io/perlio.t</dt>
<dd> <p> General PerlIO tests. </p>
 </dd>
<dt>t/io/pvbm.t</dt>
<dd> <p> Check that there is no unexpected interaction between the internal types <code>&quot;PVBM&quot;</code> and <code>&quot;PVGV&quot;</code>. </p>
 </dd>
<dt>t/mro/package_aliases.t</dt>
<dd> <p> Check that mro works properly in the presence of aliased packages. </p>
 </dd>
<dt>t/op/dbm.t</dt>
<dd> <p> Tests for <code>&quot;dbmopen&quot;</code> and <code>&quot;dbmclose&quot;</code>. </p>
 </dd>
<dt>t/op/index_thr.t</dt>
<dd> <p> Tests for the interaction of <code>&quot;index&quot;</code> and threads. </p>
 </dd>
<dt>t/op/pat_thr.t</dt>
<dd> <p> Tests for the interaction of esoteric patterns and threads. </p>
 </dd>
<dt>t/op/qr_gc.t</dt>
<dd> <p> Test that <code>&quot;qr&quot;</code> doesn&#8217;t leak. </p>
 </dd>
<dt>t/op/reg_email_thr.t</dt>
<dd> <p> Tests for the interaction of regex recursion and threads. </p>
 </dd>
<dt>t/op/regexp_qr_embed_thr.t</dt>
<dd> <p> Tests for the interaction of patterns with embedded <code>&quot;qr//&quot;</code> and threads. </p>
 </dd>
<dt>t/op/regexp_unicode_prop.t</dt>
<dd> <p> Tests for Unicode properties in regular expressions. </p>
 </dd>
<dt>t/op/regexp_unicode_prop_thr.t</dt>
<dd> <p> Tests for the interaction of Unicode properties and threads. </p>
 </dd>
<dt>t/op/reg_nc_tie.t</dt>
<dd> <p> Test the tied methods of <code>&quot;Tie::Hash::NamedCapture&quot;</code>. </p>
 </dd>
<dt>t/op/reg_posixcc.t</dt>
<dd> <p> Check that <font SIZE="-1">POSIX</font> character classes behave consistently. </p>
 </dd>
<dt>t/op/re.t</dt>
<dd> <p> Check that exportable <code>&quot;re&quot;</code> functions in <i>universal.c</i> work. </p>
 </dd>
<dt>t/op/setpgrpstack.t</dt>
<dd> <p> Check that <code>&quot;setpgrp&quot;</code> works. </p>
 </dd>
<dt>t/op/substr_thr.t</dt>
<dd> <p> Tests for the interaction of <code>&quot;substr&quot;</code> and threads. </p>
 </dd>
<dt>t/op/upgrade.t</dt>
<dd> <p> Check that upgrading and assigning scalars works. </p>
 </dd>
<dt>t/uni/lex_utf8.t</dt>
<dd> <p> Check that Unicode in the lexer works. </p>
 </dd>
<dt>t/uni/tie.t</dt>
<dd> <p> Check that Unicode and <code>&quot;tie&quot;</code> work. </p>
 </dd></dl>
<h2>Known Problems</h2>
<p> This is a list of some significant unfixed bugs, which are regressions from either 5.10.0 or 5.8.x. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;List::Util::first&quot;</code> misbehaves in the presence of a lexical <code>$_</code> (typically introduced by <code>&quot;my $_&quot;</code> or implicitly by <code>&quot;given&quot;</code>). The variable which gets set for each iteration is the package variable <code>$_</code>, not the lexical <code>$_</code> [<font SIZE="-1">RT</font> #67694]. </p>
<p> A similar issue may occur in other modules that provide functions which take a block as their first argument, like </p>
<pre><code>    foo { ... $_ ...} list
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;charnames&quot;</code> pragma may generate a run-time error when a regex is interpolated [<font SIZE="-1">RT</font> #56444]: </p>
<pre><code>    use charnames ':full';
    my $r1 = qr/\N{THAI CHARACTER SARA I}/;
    &quot;foo&quot; =~ $r1; # okay
    &quot;foo&quot; =~ /$r1+/; # runtime error
</code></pre>
<p> A workaround is to generate the character outside of the regex: </p>
<pre><code>    my $a = &quot;\N{THAI CHARACTER SARA I}&quot;;
    my $r1 = qr/$a/;
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some regexes may run much more slowly when run in a child thread compared with the thread the pattern was compiled into [<font SIZE="-1">RT</font> #55600]. </p>
 </dd></dl>
<h2>Deprecations</h2>
<p> The following items are now deprecated. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Switch&quot;</code> is buggy and should be avoided. From perl 5.11.0 onwards, it is intended that any use of the core version of this module will emit a warning, and that the module will eventually be removed from the core (probably in perl 5.14.0). See ``Switch statements&#8217;&#8216; in perlsyn for its replacement. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;suidperl&quot;</code> will be removed in 5.12.0. This provides a mechanism to emulate setuid permission bits on systems that don&#8217;t support it properly. </p>
 </dd></dl>
<h2>Acknowledgements</h2>
<p> Some of the work in this release was funded by a <font SIZE="-1">TPF</font> grant. </p>
<p> Nicholas Clark officially retired from maintenance pumpking duty at the end of 2008; however in reality he has put much effort in since then to help get 5.10.1 into a fit state to be released, including writing a considerable chunk of this perldelta. </p>
<p> Steffen Mueller and David Golden in particular helped getting <font SIZE="-1">CPAN</font> modules polished and synchronised with their in-core equivalents. </p>
<p> Craig Berry was tireless in getting maint to run under <font SIZE="-1">VMS,</font> no matter how many times we broke it for him. </p>
<p> The other core committers contributed most of the changes, and applied most of the patches sent in by the hundreds of contributors listed in <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i>. </p>
<p> (Sorry to all the people I haven&#8217;t mentioned by name). </p>
<p> Finally, thanks to Larry Wall, without whom none of this would be necessary.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
