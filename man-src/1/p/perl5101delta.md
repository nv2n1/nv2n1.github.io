---
title: "perl5101delta(1)"
name: "perl5101delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5101delta/"
description: "perl5101delta – what is new for perl v5.10.1"
---

<h2 class="name">NAME</h2>
<p> perl5101delta &#8211; what is new for perl v5.10.1 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.10.0 release and the 5.10.1 release. </p>
<p> If you are upgrading from an earlier release such as 5.8.8, first read the perl5100delta, which describes differences between 5.8.8 and 5.10.0</p>
<h2>Incompatible Changes</h2>
<h3>Switch statement changes</h3>
<p> The handling of complex expressions by the <tt>&quot;given&quot;</tt>/<tt>&quot;when&quot;</tt> switch statement has been enhanced. There are two new cases where <tt>&quot;when&quot;</tt> now interprets its argument as a boolean, instead of an expression to be used in a smart match:</p>
<dl>
<dt>flip-flop operators</dt>
<dd> The <tt>&quot;..&quot;</tt> and <tt>&quot;...&quot;</tt> flip-flop operators are now evaluated in boolean context, following their usual semantics; see &#8220;Range Operators&#8221; in perlop. </dd>
<p> Note that, as in perl 5.10.0, <tt>&quot;when (1..10)&quot;</tt> will not work to test whether a given value is an integer between 1 and 10; you should use <tt>&quot;when ([1..10])&quot;</tt> instead (note the array reference). </p>
<p> However, contrary to 5.10.0, evaluating the flip-flop operators in boolean context ensures it can now be useful in a <tt>&quot;when()&quot;</tt>, notably for implementing bistable conditions, like in: </p>
<pre>
    when (/^=begin/ .. /^=end/) {
      # do something
    }
</pre>
<dt>defined-or operator</dt>
<dd> A compound expression involving the defined-or operator, as in <tt>&quot;when (expr1 // expr2)&quot;</tt>, will be treated as boolean if the first expression is boolean. (This just extends the existing rule that applies to the regular or operator, as in <tt>&quot;when (expr1 || expr2)&quot;</tt>.)</dd></dl>
<p> The next section details more changes brought to the semantics to the smart match operator, that naturally also modify the behaviour of the switch statements where smart matching is implicitly used.</p>
<h3>Smart match changes</h3>
<p> <i>Changes to type-based dispatch</i> </p>
<p> The smart match operator <tt>&quot;~~&quot;</tt> is no longer commutative. The behaviour of a smart match now depends primarily on the type of its right hand argument. Moreover, its semantics have been adjusted for greater consistency or usefulness in several cases. While the general backwards compatibility is maintained, several changes must be noted:</p>
<dl>
<dt>&bull;</dt>
<dd> Code references with an empty prototype are no longer treated specially. They are passed an argument like the other code references (even if they choose to ignore it).</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;%hash ~~ sub {}&quot;</tt> and <tt>&quot;@array ~~ sub {}&quot;</tt> now test that the subroutine returns a true value for each key of the hash (or element of the array), instead of passing the whole hash or array as a reference to the subroutine.</dd>
<dt>&bull;</dt>
<dd> Due to the commutativity breakage, code references are no longer treated specially when appearing on the left of the <tt>&quot;~~&quot;</tt> operator, but like any vulgar scalar.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;undef ~~ %hash&quot;</tt> is always false (since <tt>&quot;undef&quot;</tt> can&#8217;t be a key in a hash). No implicit conversion to <tt>&quot;&quot;</tt> is done (as was the case in perl 5.10.0).</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;$scalar ~~ @array&quot;</tt> now always distributes the smart match across the elements of the array. It&#8217;s true if one element in <tt>@array</tt> verifies <tt>&quot;$scalar ~~ $element&quot;</tt>. This is a generalization of the old behaviour that tested whether the array contained the scalar.</dd></dl>
<p> The full dispatch table for the smart match operator is given in &#8220;Smart matching in detail&#8221; in perlsyn. </p>
<p> <i>Smart match and overloading</i> </p>
<p> According to the rule of dispatch based on the rightmost argument type, when an object overloading <tt>&quot;~~&quot;</tt> appears on the right side of the operator, the overload routine will always be called (with a 3rd argument set to a true value, see overload.) However, when the object will appear on the left, the overload routine will be called only when the rightmost argument is a simple scalar. This way distributivity of smart match across arrays is not broken, as well as the other behaviours with complex types (coderefs, hashes, regexes). Thus, writers of overloading routines for smart match mostly need to worry only with comparing against a scalar, and possibly with stringification overloading; the other common cases will be automatically handled consistently. </p>
<p> <tt>&quot;~~&quot;</tt> will now refuse to work on objects that do not overload it (in order to avoid relying on the object&#8217;s underlying structure). (However, if the object overloads the stringification or the numification operators, and if overload fallback is active, it will be used instead, as usual.)</p>
<h3>Other incompatible changes</h3>
<dl>
<dt>&bull;</dt>
<dd> The semantics of <tt>&quot;use feature :5.10*&quot;</tt> have changed slightly. See &#8220;Modules and Pragmata&#8221; for more information.</dd>
<dt>&bull;</dt>
<dd> It is now a run-time error to use the smart match operator <tt>&quot;~~&quot;</tt> with an object that has no overload defined for it. (This way <tt>&quot;~~&quot;</tt> will not break encapsulation by matching against the object&#8217;s internal representation as a reference.)</dd>
<dt>&bull;</dt>
<dd> The version control system used for the development of the perl interpreter has been switched from Perforce to git. This is mainly an internal issue that only affects people actively working on the perl core; but it may have minor external visibility, for example in some of details of the output of <tt>&quot;perl -V&quot;</tt>. See perlrepository for more information.</dd>
<dt>&bull;</dt>
<dd> The internal structure of the <tt>&quot;ext/&quot;</tt> directory in the perl source has been reorganised. In general, a module <tt>&quot;Foo::Bar&quot;</tt> whose source was stored under <i>ext/Foo/Bar/</i> is now located under <i>ext/Foo-Bar/</i>. Also, some modules have been moved from <i>lib/</i> to <i>ext/</i>. This is purely a source tarball change, and should make no difference to the compilation or installation of perl, unless you have a very customised build process that explicitly relies on this structure, or which hard-codes the <tt>&quot;nonxs_ext&quot;</tt> <i>Configure</i> parameter. Specifically, this change does not by default alter the location of any files in the final installation.</dd>
<dt>&bull;</dt>
<dd> As part of the <tt>&quot;Test::Harness&quot;</tt> 2.x to 3.x upgrade, the experimental <tt>&quot;Test::Harness::Straps&quot;</tt> module has been removed. See &#8220;Updated Modules&#8221; for more details.</dd>
<dt>&bull;</dt>
<dd> As part of the <tt>&quot;ExtUtils::MakeMaker&quot;</tt> upgrade, the <tt>&quot;ExtUtils::MakeMaker::bytes&quot;</tt> and <tt>&quot;ExtUtils::MakeMaker::vmsish&quot;</tt> modules have been removed from this distribution.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Module::CoreList&quot;</tt> no longer contains the <tt>%:patchlevel</tt> hash.</dd>
<dt>&bull;</dt>
<dd> This one is actually a change introduced in 5.10.0, but it was missed from that release&#8217;s perldelta, so it is mentioned here instead. </dd>
<p> A bugfix related to the handling of the <tt>&quot;/m&quot;</tt> modifier and <tt>&quot;qr&quot;</tt> resulted in a change of behaviour between 5.8.x and 5.10.0: </p>
<pre>
    # matches in 5.8.x, doesn't match in 5.10.0
    $re = qr/^bar/; &quot;foo
bar&quot; =~ /$re/m;
</pre>
</dl>
<h2>Core Enhancements</h2>
<h3>Unicode Character Database 5.1.0</h3>
<p> The copy of the Unicode Character Database included in Perl 5.10.1 has been updated to 5.1.0 from 5.0.0. See &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode5.1.0/#Notable_Changes">http://www.unicode.org/versions/Unicode5.1.0/#Notable_Changes</a>&gt; for the notable changes.</p>
<h3>A proper interface for pluggable Method Resolution Orders</h3>
<p> As of Perl 5.10.1 there is a new interface for plugging and using method resolution orders other than the default (linear depth first search). The C3 method resolution order added in 5.10.0 has been re-implemented as a plugin, without changing its Perl-space interface. See perlmroapi for more information.</p>
<h3>The overloading pragma</h3>
<p> This pragma allows you to lexically disable or enable overloading for some or all operations. (Yuval Kogman)</p>
<h3>Parallel tests</h3>
<p> The core distribution can now run its regression tests in parallel on Unix-like platforms. Instead of running <tt>&quot;make test&quot;</tt>, set <tt>&quot;TEST_JOBS&quot;</tt> in your environment to the number of tests to run in parallel, and run <tt>&quot;make test_harness&quot;</tt>. On a Bourne-like shell, this can be done as </p>
<pre>
    TEST_JOBS=3 make test_harness  # Run 3 tests in parallel
</pre>
<p> An environment variable is used, rather than parallel make itself, because TAP::Harness needs to be able to schedule individual non-conflicting test scripts itself, and there is no standard interface to <tt>&quot;make&quot;</tt> utilities to interact with their job schedulers. </p>
<p> Note that currently some test scripts may fail when run in parallel (most notably <tt>&quot;ext/IO/t/io_dir.t&quot;</tt>). If necessary run just the failing scripts again sequentially and see if the failures go away.</p>
<h3>DTrace support</h3>
<p> Some support for DTrace has been added. See &#8220;DTrace support&#8221; in <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i>.</p>
<h3>Support for configure_requires in <font SIZE="-1">CPAN</font> module metadata</h3>
<p> Both <tt>&quot;CPAN&quot;</tt> and <tt>&quot;CPANPLUS&quot;</tt> now support the <tt>&quot;configure_requires&quot;</tt> keyword in the <tt>&quot;META.yml&quot;</tt> metadata file included in most recent <font SIZE="-1">CPAN</font> distributions. This allows distribution authors to specify configuration prerequisites that must be installed before running <i>Makefile.PL</i> or <i>Build.PL</i>. </p>
<p> See the documentation for <tt>&quot;ExtUtils::MakeMaker&quot;</tt> or <tt>&quot;Module::Build&quot;</tt> for more on how to specify <tt>&quot;configure_requires&quot;</tt> when creating a distribution for <font SIZE="-1">CPAN.</font></p>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<dl>
<dt>&quot;autodie&quot;</dt>
<dd> This is a new lexically-scoped alternative for the <tt>&quot;Fatal&quot;</tt> module. The bundled version is 2.06_01. Note that in this release, using a string eval when <tt>&quot;autodie&quot;</tt> is in effect can cause the autodie behaviour to leak into the surrounding scope. See &#8220;<font SIZE="-1">BUGS&#8221;</font> in autodie for more details.</dd>
<dt>&quot;Compress::Raw::Bzip2&quot;</dt>
<dd> This has been added to the core (version 2.020).</dd>
<dt>&quot;parent&quot;</dt>
<dd> This pragma establishes an <font SIZE="-1">ISA</font> relationship with base classes at compile time. It provides the key feature of <tt>&quot;base&quot;</tt> without the feature creep.</dd>
<dt>&quot;Parse::CPAN::Meta&quot;</dt>
<dd> This has been added to the core (version 1.39).</dd></dl>
<h3>Pragmata Changes</h3>
<dl>
<dt>&quot;attributes&quot;</dt>
<dd> Upgraded from version 0.08 to 0.09.</dd>
<dt>&quot;attrs&quot;</dt>
<dd> Upgraded from version 1.02 to 1.03.</dd>
<dt>&quot;base&quot;</dt>
<dd> Upgraded from version 2.13 to 2.14. See parent for a replacement.</dd>
<dt>&quot;bigint&quot;</dt>
<dd> Upgraded from version 0.22 to 0.23.</dd>
<dt>&quot;bignum&quot;</dt>
<dd> Upgraded from version 0.22 to 0.23.</dd>
<dt>&quot;bigrat&quot;</dt>
<dd> Upgraded from version 0.22 to 0.23.</dd>
<dt>&quot;charnames&quot;</dt>
<dd> Upgraded from version 1.06 to 1.07. </dd>
<p> The Unicode <i>NameAliases.txt</i> database file has been added. This has the effect of adding some extra <tt>&quot;\N&quot;</tt> character names that formerly wouldn&#8217;t have been recognised; for example, <tt>&quot;\N{LATIN CAPITAL LETTER GHA}&quot;</tt>.</p>
<dt>&quot;constant&quot;</dt>
<dd> Upgraded from version 1.13 to 1.17.</dd>
<dt>&quot;feature&quot;</dt>
<dd> The meaning of the <tt>&quot;:5.10&quot;</tt> and <tt>&quot;:5.10.X&quot;</tt> feature bundles has changed slightly. The last component, if any (i.e. <tt>&quot;X&quot;</tt>) is simply ignored. This is predicated on the assumption that new features will not, in general, be added to maintenance releases. So <tt>&quot;:5.10&quot;</tt> and <tt>&quot;:5.10.X&quot;</tt> have identical effect. This is a change to the behaviour documented for 5.10.0.</dd>
<dt>&quot;fields&quot;</dt>
<dd> Upgraded from version 2.13 to 2.14 (this was just a version bump; there were no functional changes).</dd>
<dt>&quot;lib&quot;</dt>
<dd> Upgraded from version 0.5565 to 0.62.</dd>
<dt>&quot;open&quot;</dt>
<dd> Upgraded from version 1.06 to 1.07.</dd>
<dt>&quot;overload&quot;</dt>
<dd> Upgraded from version 1.06 to 1.07.</dd>
<dt>&quot;overloading&quot;</dt>
<dd> See &quot;The <tt>&quot;overloading&quot;</tt> pragma&quot; above.</dd>
<dt>&quot;version&quot;</dt>
<dd> Upgraded from version 0.74 to 0.77.</dd></dl>
<h3>Updated Modules</h3>
<dl>
<dt>&quot;Archive::Extract&quot;</dt>
<dd> Upgraded from version 0.24 to 0.34.</dd>
<dt>&quot;Archive::Tar&quot;</dt>
<dd> Upgraded from version 1.38 to 1.52.</dd>
<dt>&quot;Attribute::Handlers&quot;</dt>
<dd> Upgraded from version 0.79 to 0.85.</dd>
<dt>&quot;AutoLoader&quot;</dt>
<dd> Upgraded from version 5.63 to 5.68.</dd>
<dt>&quot;AutoSplit&quot;</dt>
<dd> Upgraded from version 1.05 to 1.06.</dd>
<dt>&quot;B&quot;</dt>
<dd> Upgraded from version 1.17 to 1.22.</dd>
<dt>&quot;B::Debug&quot;</dt>
<dd> Upgraded from version 1.05 to 1.11.</dd>
<dt>&quot;B::Deparse&quot;</dt>
<dd> Upgraded from version 0.83 to 0.89.</dd>
<dt>&quot;B::Lint&quot;</dt>
<dd> Upgraded from version 1.09 to 1.11.</dd>
<dt>&quot;B::Xref&quot;</dt>
<dd> Upgraded from version 1.01 to 1.02.</dd>
<dt>&quot;Benchmark&quot;</dt>
<dd> Upgraded from version 1.10 to 1.11.</dd>
<dt>&quot;Carp&quot;</dt>
<dd> Upgraded from version 1.08 to 1.11.</dd>
<dt>&quot;CGI&quot;</dt>
<dd> Upgraded from version 3.29 to 3.43. (also includes the &#8220;default_value for <code>popup_menu()</code>&#8221; fix from 3.45).</dd>
<dt>&quot;Compress::Zlib&quot;</dt>
<dd> Upgraded from version 2.008 to 2.020.</dd>
<dt>&quot;CPAN&quot;</dt>
<dd> Upgraded from version 1.9205 to 1.9402. <tt>&quot;CPAN::FTP&quot;</tt> has a local fix to stop it being too verbose on download failure.</dd>
<dt>&quot;CPANPLUS&quot;</dt>
<dd> Upgraded from version 0.84 to 0.88.</dd>
<dt>&quot;CPANPLUS::Dist::Build&quot;</dt>
<dd> Upgraded from version 0.06_02 to 0.36.</dd>
<dt>&quot;Cwd&quot;</dt>
<dd> Upgraded from version 3.25_01 to 3.30.</dd>
<dt>&quot;Data::Dumper&quot;</dt>
<dd> Upgraded from version 2.121_14 to 2.124.</dd>
<dt>&quot;DB&quot;</dt>
<dd> Upgraded from version 1.01 to 1.02.</dd>
<dt>&quot;DB_File&quot;</dt>
<dd> Upgraded from version 1.816_1 to 1.820.</dd>
<dt>&quot;Devel::PPPort&quot;</dt>
<dd> Upgraded from version 3.13 to 3.19.</dd>
<dt>&quot;Digest::MD5&quot;</dt>
<dd> Upgraded from version 2.36_01 to 2.39.</dd>
<dt>&quot;Digest::SHA&quot;</dt>
<dd> Upgraded from version 5.45 to 5.47.</dd>
<dt>&quot;DirHandle&quot;</dt>
<dd> Upgraded from version 1.01 to 1.03.</dd>
<dt>&quot;Dumpvalue&quot;</dt>
<dd> Upgraded from version 1.12 to 1.13.</dd>
<dt>&quot;DynaLoader&quot;</dt>
<dd> Upgraded from version 1.08 to 1.10.</dd>
<dt>&quot;Encode&quot;</dt>
<dd> Upgraded from version 2.23 to 2.35.</dd>
<dt>&quot;Errno&quot;</dt>
<dd> Upgraded from version 1.10 to 1.11.</dd>
<dt>&quot;Exporter&quot;</dt>
<dd> Upgraded from version 5.62 to 5.63.</dd>
<dt>&quot;ExtUtils::CBuilder&quot;</dt>
<dd> Upgraded from version 0.21 to 0.2602.</dd>
<dt>&quot;ExtUtils::Command&quot;</dt>
<dd> Upgraded from version 1.13 to 1.16.</dd>
<dt>&quot;ExtUtils::Constant&quot;</dt>
<dd> Upgraded from 0.20 to 0.22. (Note that neither of these versions are available on <font SIZE="-1">CPAN.</font>)</dd>
<dt>&quot;ExtUtils::Embed&quot;</dt>
<dd> Upgraded from version 1.27 to 1.28.</dd>
<dt>&quot;ExtUtils::Install&quot;</dt>
<dd> Upgraded from version 1.44 to 1.54.</dd>
<dt>&quot;ExtUtils::MakeMaker&quot;</dt>
<dd> Upgraded from version 6.42 to 6.55_02. </dd>
<p> Note that <tt>&quot;ExtUtils::MakeMaker::bytes&quot;</tt> and <tt>&quot;ExtUtils::MakeMaker::vmsish&quot;</tt> have been removed from this distribution.</p>
<dt>&quot;ExtUtils::Manifest&quot;</dt>
<dd> Upgraded from version 1.51_01 to 1.56.</dd>
<dt>&quot;ExtUtils::ParseXS&quot;</dt>
<dd> Upgraded from version 2.18_02 to 2.2002.</dd>
<dt>&quot;Fatal&quot;</dt>
<dd> Upgraded from version 1.05 to 2.06_01. See also the new pragma <tt>&quot;autodie&quot;</tt>.</dd>
<dt>&quot;File::Basename&quot;</dt>
<dd> Upgraded from version 2.76 to 2.77.</dd>
<dt>&quot;File::Compare&quot;</dt>
<dd> Upgraded from version 1.1005 to 1.1006.</dd>
<dt>&quot;File::Copy&quot;</dt>
<dd> Upgraded from version 2.11 to 2.14.</dd>
<dt>&quot;File::Fetch&quot;</dt>
<dd> Upgraded from version 0.14 to 0.20.</dd>
<dt>&quot;File::Find&quot;</dt>
<dd> Upgraded from version 1.12 to 1.14.</dd>
<dt>&quot;File::Path&quot;</dt>
<dd> Upgraded from version 2.04 to 2.07_03.</dd>
<dt>&quot;File::Spec&quot;</dt>
<dd> Upgraded from version 3.2501 to 3.30.</dd>
<dt>&quot;File::stat&quot;</dt>
<dd> Upgraded from version 1.00 to 1.01.</dd>
<dt>&quot;File::Temp&quot;</dt>
<dd> Upgraded from version 0.18 to 0.22.</dd>
<dt>&quot;FileCache&quot;</dt>
<dd> Upgraded from version 1.07 to 1.08.</dd>
<dt>&quot;FileHandle&quot;</dt>
<dd> Upgraded from version 2.01 to 2.02.</dd>
<dt>&quot;Filter::Simple&quot;</dt>
<dd> Upgraded from version 0.82 to 0.84.</dd>
<dt>&quot;Filter::Util::Call&quot;</dt>
<dd> Upgraded from version 1.07 to 1.08.</dd>
<dt>&quot;FindBin&quot;</dt>
<dd> Upgraded from version 1.49 to 1.50.</dd>
<dt>&quot;GDBM_File&quot;</dt>
<dd> Upgraded from version 1.08 to 1.09.</dd>
<dt>&quot;Getopt::Long&quot;</dt>
<dd> Upgraded from version 2.37 to 2.38.</dd>
<dt>&quot;Hash::Util::FieldHash&quot;</dt>
<dd> Upgraded from version 1.03 to 1.04. This fixes a memory leak.</dd>
<dt>&quot;I18N::Collate&quot;</dt>
<dd> Upgraded from version 1.00 to 1.01.</dd>
<dt>&quot;IO&quot;</dt>
<dd> Upgraded from version 1.23_01 to 1.25. </dd>
<p> This makes non-blocking mode work on Windows in <tt>&quot;IO::Socket::INET&quot;</tt> [<font SIZE="-1">CPAN</font> #43573].</p>
<dt>&quot;IO::Compress::*&quot;</dt>
<dd> Upgraded from version 2.008 to 2.020.</dd>
<dt>&quot;IO::Dir&quot;</dt>
<dd> Upgraded from version 1.06 to 1.07.</dd>
<dt>&quot;IO::Handle&quot;</dt>
<dd> Upgraded from version 1.27 to 1.28.</dd>
<dt>&quot;IO::Socket&quot;</dt>
<dd> Upgraded from version 1.30_01 to 1.31.</dd>
<dt>&quot;IO::Zlib&quot;</dt>
<dd> Upgraded from version 1.07 to 1.09.</dd>
<dt>&quot;IPC::Cmd&quot;</dt>
<dd> Upgraded from version 0.40_1 to 0.46.</dd>
<dt>&quot;IPC::Open3&quot;</dt>
<dd> Upgraded from version 1.02 to 1.04.</dd>
<dt>&quot;IPC::SysV&quot;</dt>
<dd> Upgraded from version 1.05 to 2.01.</dd>
<dt>&quot;lib&quot;</dt>
<dd> Upgraded from version 0.5565 to 0.62.</dd>
<dt>&quot;List::Util&quot;</dt>
<dd> Upgraded from version 1.19 to 1.21.</dd>
<dt>&quot;Locale::MakeText&quot;</dt>
<dd> Upgraded from version 1.12 to 1.13.</dd>
<dt>&quot;Log::Message&quot;</dt>
<dd> Upgraded from version 0.01 to 0.02.</dd>
<dt>&quot;Math::BigFloat&quot;</dt>
<dd> Upgraded from version 1.59 to 1.60.</dd>
<dt>&quot;Math::BigInt&quot;</dt>
<dd> Upgraded from version 1.88 to 1.89.</dd>
<dt>&quot;Math::BigInt::FastCalc&quot;</dt>
<dd> Upgraded from version 0.16 to 0.19.</dd>
<dt>&quot;Math::BigRat&quot;</dt>
<dd> Upgraded from version 0.21 to 0.22.</dd>
<dt>&quot;Math::Complex&quot;</dt>
<dd> Upgraded from version 1.37 to 1.56.</dd>
<dt>&quot;Math::Trig&quot;</dt>
<dd> Upgraded from version 1.04 to 1.20.</dd>
<dt>&quot;Memoize&quot;</dt>
<dd> Upgraded from version 1.01_02 to 1.01_03 (just a minor documentation change).</dd>
<dt>&quot;Module::Build&quot;</dt>
<dd> Upgraded from version 0.2808_01 to 0.34_02.</dd>
<dt>&quot;Module::CoreList&quot;</dt>
<dd> Upgraded from version 2.13 to 2.18. This release no longer contains the <tt>%Module::CoreList::patchlevel</tt> hash.</dd>
<dt>&quot;Module::Load&quot;</dt>
<dd> Upgraded from version 0.12 to 0.16.</dd>
<dt>&quot;Module::Load::Conditional&quot;</dt>
<dd> Upgraded from version 0.22 to 0.30.</dd>
<dt>&quot;Module::Loaded&quot;</dt>
<dd> Upgraded from version 0.01 to 0.02.</dd>
<dt>&quot;Module::Pluggable&quot;</dt>
<dd> Upgraded from version 3.6 to 3.9.</dd>
<dt>&quot;NDBM_File&quot;</dt>
<dd> Upgraded from version 1.07 to 1.08.</dd>
<dt>&quot;Net::Ping&quot;</dt>
<dd> Upgraded from version 2.33 to 2.36.</dd>
<dt>&quot;NEXT&quot;</dt>
<dd> Upgraded from version 0.60_01 to 0.64.</dd>
<dt>&quot;Object::Accessor&quot;</dt>
<dd> Upgraded from version 0.32 to 0.34.</dd>
<dt>&quot;OS2::REXX&quot;</dt>
<dd> Upgraded from version 1.03 to 1.04.</dd>
<dt>&quot;Package::Constants&quot;</dt>
<dd> Upgraded from version 0.01 to 0.02.</dd>
<dt>&quot;PerlIO&quot;</dt>
<dd> Upgraded from version 1.04 to 1.06.</dd>
<dt>&quot;PerlIO::via&quot;</dt>
<dd> Upgraded from version 0.04 to 0.07.</dd>
<dt>&quot;Pod::Man&quot;</dt>
<dd> Upgraded from version 2.16 to 2.22.</dd>
<dt>&quot;Pod::Parser&quot;</dt>
<dd> Upgraded from version 1.35 to 1.37.</dd>
<dt>&quot;Pod::Simple&quot;</dt>
<dd> Upgraded from version 3.05 to 3.07.</dd>
<dt>&quot;Pod::Text&quot;</dt>
<dd> Upgraded from version 3.08 to 3.13.</dd>
<dt>&quot;POSIX&quot;</dt>
<dd> Upgraded from version 1.13 to 1.17.</dd>
<dt>&quot;Safe&quot;</dt>
<dd> Upgraded from 2.12 to 2.18.</dd>
<dt>&quot;Scalar::Util&quot;</dt>
<dd> Upgraded from version 1.19 to 1.21.</dd>
<dt>&quot;SelectSaver&quot;</dt>
<dd> Upgraded from 1.01 to 1.02.</dd>
<dt>&quot;SelfLoader&quot;</dt>
<dd> Upgraded from 1.11 to 1.17.</dd>
<dt>&quot;Socket&quot;</dt>
<dd> Upgraded from 1.80 to 1.82.</dd>
<dt>&quot;Storable&quot;</dt>
<dd> Upgraded from 2.18 to 2.20.</dd>
<dt>&quot;Switch&quot;</dt>
<dd> Upgraded from version 2.13 to 2.14. Please see &#8220;Deprecations&#8221;.</dd>
<dt>&quot;Symbol&quot;</dt>
<dd> Upgraded from version 1.06 to 1.07.</dd>
<dt>&quot;Sys::Syslog&quot;</dt>
<dd> Upgraded from version 0.22 to 0.27.</dd>
<dt>&quot;Term::ANSIColor&quot;</dt>
<dd> Upgraded from version 1.12 to 2.00.</dd>
<dt>&quot;Term::ReadLine&quot;</dt>
<dd> Upgraded from version 1.03 to 1.04.</dd>
<dt>&quot;Term::UI&quot;</dt>
<dd> Upgraded from version 0.18 to 0.20.</dd>
<dt>&quot;Test::Harness&quot;</dt>
<dd> Upgraded from version 2.64 to 3.17. </dd>
<p> Note that one side-effect of the 2.x to 3.x upgrade is that the experimental <tt>&quot;Test::Harness::Straps&quot;</tt> module (and its supporting <tt>&quot;Assert&quot;</tt>, <tt>&quot;Iterator&quot;</tt>, <tt>&quot;Point&quot;</tt> and <tt>&quot;Results&quot;</tt> modules) have been removed. If you still need this, then they are available in the (unmaintained) <tt>&quot;Test-Harness-Straps&quot;</tt> distribution on <font SIZE="-1">CPAN.</font></p>
<dt>&quot;Test::Simple&quot;</dt>
<dd> Upgraded from version 0.72 to 0.92.</dd>
<dt>&quot;Text::ParseWords&quot;</dt>
<dd> Upgraded from version 3.26 to 3.27.</dd>
<dt>&quot;Text::Tabs&quot;</dt>
<dd> Upgraded from version 2007.1117 to 2009.0305.</dd>
<dt>&quot;Text::Wrap&quot;</dt>
<dd> Upgraded from version 2006.1117 to 2009.0305.</dd>
<dt>&quot;Thread::Queue&quot;</dt>
<dd> Upgraded from version 2.00 to 2.11.</dd>
<dt>&quot;Thread::Semaphore&quot;</dt>
<dd> Upgraded from version 2.01 to 2.09.</dd>
<dt>&quot;threads&quot;</dt>
<dd> Upgraded from version 1.67 to 1.72.</dd>
<dt>&quot;threads::shared&quot;</dt>
<dd> Upgraded from version 1.14 to 1.29.</dd>
<dt>&quot;Tie::RefHash&quot;</dt>
<dd> Upgraded from version 1.37 to 1.38.</dd>
<dt>&quot;Tie::StdHandle&quot;</dt>
<dd> This has documentation changes, and has been assigned a version for the first time: version 4.2.</dd>
<dt>&quot;Time::HiRes&quot;</dt>
<dd> Upgraded from version 1.9711 to 1.9719.</dd>
<dt>&quot;Time::Local&quot;</dt>
<dd> Upgraded from version 1.18 to 1.1901.</dd>
<dt>&quot;Time::Piece&quot;</dt>
<dd> Upgraded from version 1.12 to 1.15.</dd>
<dt>&quot;Unicode::Normalize&quot;</dt>
<dd> Upgraded from version 1.02 to 1.03.</dd>
<dt>&quot;Unicode::UCD&quot;</dt>
<dd> Upgraded from version 0.25 to 0.27. </dd>
<p> <tt>&quot;charinfo()&quot;</tt> now works on Unified <font SIZE="-1">CJK</font> code points added to later versions of Unicode. </p>
<p> <tt>&quot;casefold()&quot;</tt> has new fields returned to provide both a simpler interface and previously missing information. The old fields are retained for backwards compatibility. Information about Turkic-specific code points is now returned. </p>
<p> The documentation has been corrected and expanded.</p>
<dt>&quot;UNIVERSAL&quot;</dt>
<dd> Upgraded from version 1.04 to 1.05.</dd>
<dt>&quot;Win32&quot;</dt>
<dd> Upgraded from version 0.34 to 0.39.</dd>
<dt>&quot;Win32API::File&quot;</dt>
<dd> Upgraded from version 0.1001_01 to 0.1101.</dd>
<dt>&quot;XSLoader&quot;</dt>
<dd> Upgraded from version 0.08 to 0.10.</dd></dl>
<h2>Utility Changes</h2>
<dl>
<dt><i>h2ph</i></dt>
<dd> Now looks in <tt>&quot;include-fixed&quot;</tt> too, which is a recent addition to gcc&#8217;s search path.</dd>
<dt><i>h2xs</i></dt>
<dd> No longer incorrectly treats enum values like macros (Daniel Burr). </dd>
<p> Now handles C<font SIZE="-2">++</font> style constants (<tt>&quot;//&quot;</tt>) properly in enums. (A patch from Rainer Weikusat was used; Daniel Burr also proposed a similar fix).</p>
<dt><i>perl5db.pl</i></dt>
<dd> <tt>&quot;LVALUE&quot;</tt> subroutines now work under the debugger. </dd>
<p> The debugger now correctly handles proxy constant subroutines, and subroutine stubs.</p>
<dt><i>perlthanks</i></dt>
<dd> Perl 5.10.1 adds a new utility <i>perlthanks</i>, which is a variant of <i>perlbug</i>, but for sending non-bug-reports to the authors and maintainers of Perl. Getting nothing but bug reports can become a bit demoralising: we&#8217;ll see if this changes things.</dd></dl>
<h2>New Documentation</h2>
<dl>
<dt>perlhaiku</dt>
<dd> This contains instructions on how to build perl for the Haiku platform.</dd>
<dt>perlmroapi</dt>
<dd> This describes the new interface for pluggable Method Resolution Orders.</dd>
<dt>perlperf</dt>
<dd> This document, by Richard Foley, provides an introduction to the use of performance and optimization techniques which can be used with particular reference to perl programs.</dd>
<dt>perlrepository</dt>
<dd> This describes how to access the perl source using the <i>git</i> version control system.</dd>
<dt>perlthanks</dt>
<dd> This describes the new <i>perlthanks</i> utility.</dd></dl>
<h2>Changes to Existing Documentation</h2>
<p> The various large <tt>&quot;Changes*&quot;</tt> files (which listed every change made to perl over the last 18 years) have been removed, and replaced by a small file, also called <tt>&quot;Changes&quot;</tt>, which just explains how that same information may be extracted from the git version control system. </p>
<p> The file <i>Porting/patching.pod</i> has been deleted, as it mainly described interacting with the old Perforce-based repository, which is now obsolete. Information still relevant has been moved to perlrepository. </p>
<p> perlapi, perlintern, perlmodlib and perltoc are now all generated at build time, rather than being shipped as part of the release.</p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> A new internal cache means that <tt>&quot;isa()&quot;</tt> will often be faster.</dd>
<dt>&bull;</dt>
<dd> Under <tt>&quot;use locale&quot;</tt>, the locale-relevant information is now cached on read-only values, such as the list returned by <tt>&quot;keys %hash&quot;</tt>. This makes operations such as <tt>&quot;sort keys %hash&quot;</tt> in the scope of <tt>&quot;use locale&quot;</tt> much faster.</dd>
<dt>&bull;</dt>
<dd> Empty <tt>&quot;DESTROY&quot;</tt> methods are no longer called.</dd></dl>
<h2>Installation and Configuration Improvements</h2>
<h3><i>ext/</i> reorganisation</h3>
<p> The layout of directories in <i>ext</i> has been revised. Specifically, all extensions are now flat, and at the top level, with <tt>&quot;/&quot;</tt> in pathnames replaced by <tt>&quot;-&quot;</tt>, so that <i>ext/Data/Dumper/</i> is now <i>ext/Data-Dumper/</i>, etc. The names of the extensions as specified to <i>Configure</i>, and as reported by <tt>%Config::Config</tt> under the keys <tt>&quot;dynamic_ext&quot;</tt>, <tt>&quot;known_extensions&quot;</tt>, <tt>&quot;nonxs_ext&quot;</tt> and <tt>&quot;static_ext&quot;</tt> have not changed, and still use <tt>&quot;/&quot;</tt>. Hence this change will not have any affect once perl is installed. However, <tt>&quot;Attribute::Handlers&quot;</tt>, <tt>&quot;Safe&quot;</tt> and <tt>&quot;mro&quot;</tt> have now become extensions in their own right, so if you run <i>Configure</i> with options to specify an exact list of extensions to build, you will need to change it to account for this. </p>
<p> For 5.10.2, it is planned that many dual-life modules will have been moved from <i>lib</i> to <i>ext</i>; again this will have no effect on an installed perl, but will matter if you invoke <i>Configure</i> with a pre-canned list of extensions to build.</p>
<h3>Configuration improvements</h3>
<p> If <tt>&quot;vendorlib&quot;</tt> and <tt>&quot;vendorarch&quot;</tt> are the same, then they are only added to <tt>@INC</tt> once. </p>
<p> <tt>$Config{usedevel}</tt> and the C-level <tt>&quot;PERL_USE_DEVEL&quot;</tt> are now defined if perl is built with <tt>&quot;-Dusedevel&quot;</tt>. </p>
<p> <i>Configure</i> will enable use of <tt>&quot;-fstack-protector&quot;</tt>, to provide protection against stack-smashing attacks, if the compiler supports it. </p>
<p> <i>Configure</i> will now determine the correct prototypes for re-entrant functions, and for <tt>&quot;gconvert&quot;</tt>, if you are using a C<font SIZE="-2">++</font> compiler rather than a C compiler. </p>
<p> On Unix, if you build from a tree containing a git repository, the configuration process will note the commit hash you have checked out, for display in the output of <tt>&quot;perl -v&quot;</tt> and <tt>&quot;perl -V&quot;</tt>. Unpushed local commits are automatically added to the list of local patches displayed by <tt>&quot;perl -V&quot;</tt>.</p>
<h3>Compilation improvements</h3>
<p> As part of the flattening of <i>ext</i>, all extensions on all platforms are built by <i>make_ext.pl</i>. This replaces the Unix-specific <i>ext/util/make_ext</i>, VMS-specific <i>make_ext.com</i> and Win32-specific <i>win32/buildext.pl</i>.</p>
<h3>Platform Specific Changes</h3>
<dl>
<dt><font SIZE="-1">AIX</font></dt>
<dd> Removed <i>libbsd</i> for <font SIZE="-1">AIX 5L</font> and 6.1. Only <code>flock()</code> was used from <i>libbsd</i>. </dd>
<p> Removed <i>libgdbm</i> for <font SIZE="-1">AIX 5L</font> and 6.1. The <i>libgdbm</i> is delivered as an optional package with the <font SIZE="-1">AIX</font> Toolbox. Unfortunately the 64 bit version is broken. </p>
<p> Hints changes mean that <font SIZE="-1">AIX 4.2</font> should work again.</p>
<dt>Cygwin</dt>
<dd> On Cygwin we now strip the last number from the <font SIZE="-1">DLL.</font> This has been the behaviour in the cygwin.com build for years. The hints files have been updated.</dd>
<dt>FreeBSD</dt>
<dd> The hints files now identify the correct threading libraries on FreeBSD 7 and later.</dd>
<dt>Irix</dt>
<dd> We now work around a bizarre preprocessor bug in the Irix 6.5 compiler: <tt>&quot;cc -E -&quot;</tt> unfortunately goes into K&amp;R mode, but <tt>&quot;cc -E file.c&quot;</tt> doesn&#8217;t.</dd>
<dt>Haiku</dt>
<dd> Patches from the Haiku maintainers have been merged in. Perl should now build on Haiku.</dd>
<dt>MirOS <font SIZE="-1">BSD</font></dt>
<dd> Perl should now build on MirOS <font SIZE="-1">BSD.</font></dd>
<dt>NetBSD</dt>
<dd> Hints now supports versions 5.*.</dd>
<dt>Stratus <font SIZE="-1">VOS</font></dt>
<dd> Various changes from Stratus have been merged in.</dd>
<dt>Symbian</dt>
<dd> There is now support for Symbian S60 3.2 <font SIZE="-1">SDK</font> and S60 5.0 <font SIZE="-1">SDK.</font></dd>
<dt>Win32</dt>
<dd> Improved message window handling means that <tt>&quot;alarm&quot;</tt> and <tt>&quot;kill&quot;</tt> messages will no longer be dropped under race conditions.</dd>
<dt><font SIZE="-1">VMS</font></dt>
<dd> Reads from the in-memory temporary files of <tt>&quot;PerlIO::scalar&quot;</tt> used to fail if <tt>$/</tt> was set to a numeric reference (to indicate record-style reads). This is now fixed. </dd>
<p> <font SIZE="-1">VMS</font> now supports <tt>&quot;getgrgid&quot;</tt>. </p>
<p> Many improvements and cleanups have been made to the <font SIZE="-1">VMS</font> file name handling and conversion code. </p>
<p> Enabling the <tt>&quot;PERL_VMS_POSIX_EXIT&quot;</tt> logical name now encodes a <font SIZE="-1">POSIX</font> exit status in a <font SIZE="-1">VMS</font> condition value for better interaction with <font SIZE="-1">GNV</font>&#8216;s bash shell and other utilities that depend on <font SIZE="-1">POSIX</font> exit values. See &#8220;$?&#8221; in perlvms for details.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> 5.10.0 inadvertently disabled an optimisation, which caused a measurable performance drop in list assignment, such as is often used to assign function parameters from <tt>@_</tt>. The optimisation has been re-instated, and the performance regression fixed.</dd>
<dt>&bull;</dt>
<dd> Fixed memory leak on <tt>&quot;while (1) { map 1, 1 }&quot;</tt> [<font SIZE="-1">RT</font> #53038].</dd>
<dt>&bull;</dt>
<dd> Some potential coredumps in PerlIO fixed [<font SIZE="-1">RT</font> #57322,54828].</dd>
<dt>&bull;</dt>
<dd> The debugger now works with lvalue subroutines.</dd>
<dt>&bull;</dt>
<dd> The debugger&#8217;s <tt>&quot;m&quot;</tt> command was broken on modules that defined constants [<font SIZE="-1">RT</font> #61222].</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;crypt()&quot;</tt> and string complement could return tainted values for untainted arguments [<font SIZE="-1">RT</font> #59998].</dd>
<dt>&bull;</dt>
<dd> The <tt>&quot;-i.suffix&quot;</tt> command-line switch now recreates the file using restricted permissions, before changing its mode to match the original file. This eliminates a potential race condition [<font SIZE="-1">RT</font> #60904].</dd>
<dt>&bull;</dt>
<dd> On some Unix systems, the value in <tt>$?</tt> would not have the top bit set (<tt>&quot;$? &amp; 128&quot;</tt>) even if the child core dumped.</dd>
<dt>&bull;</dt>
<dd> Under some circumstances, $^R could incorrectly become undefined [<font SIZE="-1">RT</font> #57042].</dd>
<dt>&bull;</dt>
<dd> (<font SIZE="-1">XS</font>) In various hash functions, passing a pre-computed hash to when the key is <font SIZE="-1">UTF-8</font> might result in an incorrect lookup.</dd>
<dt>&bull;</dt>
<dd> (<font SIZE="-1">XS</font>) Including <i></i><font SIZE="-1"><i>XSUB</i></font><i>.h</i> before <i>perl.h</i> gave a compile-time error [<font SIZE="-1">RT</font> #57176].</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;$object-&gt;isa('Foo')&quot;</tt> would report false if the package <tt>&quot;Foo&quot;</tt> didn&#8217;t exist, even if the object&#8217;s <tt>@ISA</tt> contained <tt>&quot;Foo&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> Various bugs in the new-to 5.10.0 mro code, triggered by manipulating <tt>@ISA</tt>, have been found and fixed.</dd>
<dt>&bull;</dt>
<dd> Bitwise operations on references could crash the interpreter, e.g. <tt>&quot;$x=\$y; $x |= &quot;foo&quot;&quot;</tt> [<font SIZE="-1">RT</font> #54956].</dd>
<dt>&bull;</dt>
<dd> Patterns including alternation might be sensitive to the internal <font SIZE="-1">UTF-8</font> representation, e.g. </dd>
<pre><code>
my $byte = chr(192);
my $utf8 = chr(192);
utf8::upgrade($utf8);
$utf8 = ~ / $byte | X
}
/ i;
#failed in 5.10.0
</code></pre>
<dt>&bull;</dt>
<dd> Within UTF8-encoded Perl source files (i.e. where <tt>&quot;use utf8&quot;</tt> is in effect), double-quoted literal strings could be corrupted where a <tt>&quot;
</dd></dl>