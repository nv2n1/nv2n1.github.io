---
title: "perl5110delta(1)"
name: "perl5110delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5110delta/"
description: "perl5110delta – what is new for perl v5.11.0"
---

<h2 class="name">NAME</h2>
<p> perl5110delta &#8211; what is new for perl v5.11.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.10.0 release and the 5.11.0 development release.</p>
<h2>Incompatible Changes</h2>
<h3>Unicode interpretation of \w, \d, \s, and the <font SIZE="-1">POSIX</font> character classes redefined.</h3>
<p> Previous versions of Perl tried to map <font SIZE="-1">POSIX</font> style character class definitions onto Unicode property names so that patterns would &#8220;dwim&#8221; when matches were made against latin-1 or unicode strings. This proved to be a mistake, breaking character class negation, causing forward compatibility problems (as Unicode keeps updating their property definitions and adding new characters), and other problems. </p>
<p> Therefore we have now defined a new set of artificial &#8220;unicode&#8221; property names which will be used to do unicode matching of patterns using <font SIZE="-1">POSIX</font> style character classes and perl short-form escape character classes like \w and \d. </p>
<p> The key change here is that \d will no longer match every digit in the unicode standard (there are thousands) nor will \w match every word character in the standard, instead they will match precisely their <font SIZE="-1">POSIX</font> or Perl definition. </p>
<p> Those needing to match based on Unicode properties can continue to do so by using the \p{} syntax to match whichever property they like, including the new artificial definitions. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> This is a backwards incompatible no-warning change in behaviour. If you are upgrading and you process large volumes of text look for <font SIZE="-1">POSIX</font> and Perl style character classes and change them to the relevant property name (by removing the word &#8216;Posix&#8217; from the current name). </p>
<p> The following table maps the <font SIZE="-1">POSIX</font> character class names, the escapes and the old and new Unicode property mappings: </p>
<pre><code>
    POSIX  Esc  Class               New-Property  ! Old-Property
    ----------------------------------------------+-------------
    alnum       [0-9A-Za-z]         IsPosixAlnum  ! IsAlnum
    alpha       [A-Za-z]            IsPosixAlpha  ! IsAlpha
    ascii       [</code>\000-\177] IsASCII = IsASCII
    blank [\011 ] IsPosixBlank !
    cntrl [\0-\37\177] IsPosixCntrl ! IsCntrl
    digit \d [0-9] IsPosixDigit ! IsDigit
    graph [!-~] IsPosixGraph ! IsGraph
    lower [a-z] IsPosixLower ! IsLower
    print [ -~] IsPosixPrint ! IsPrint
    punct [!-/:-@[-`{-~] IsPosixPunct ! IsPunct
    space [\11-\15 ] IsPosixSpace ! IsSpace
            \s [\11\12\14\15 ] IsPerlSpace ! IsSpacePerl
    upper [A-Z] IsPosixUpper ! IsUpper
    word \w [0-9A-Z_a-z] IsPerlWord ! IsWord
    xdigit [0-9A-Fa-f] IsXDigit = IsXDigit
</code></pre>
<p> If you wish to build perl with the old mapping you may do so by setting </p>
<pre><code>        #define PERL_LEGACY_UNICODE_CHARCLASS_MAPPINGS 1
</code></pre>
<p> in regcomp.h, and then setting </p>
<pre><code>        PERL_TEST_LEGACY_POSIX_CC
</code></pre>
<p> to true your environment when testing.  </p>
<h3>@INC reorganization</h3>
<p> In <code>@INC</code>, <font SIZE="-1">ARCHLIB</font> and <font SIZE="-1">PRIVLIB</font> now occur after after the current version&#8217;s site_perl and vendor_perl.  </p>
<h3>Switch statement changes</h3>
<p> The handling of complex expressions by the <code>&quot;given&quot;</code>/<code>&quot;when&quot;</code> switch statement has been enhanced. These enhancements are also available in 5.10.1 and subsequent 5.10 releases. There are two new cases where <code>&quot;when&quot;</code> now interprets its argument as a boolean, instead of an expression to be used in a smart match: </p>
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
<p> The next section details more changes brought to the semantics to the smart match operator, that naturally also modify the behaviour of the switch statements where smart matching is implicitly used. These changers were also made for the 5.10.1 release, and will remain in subsequent 5.10 releases.  </p>
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
<h3>Labels can't be keywords</h3>
<p> Labels used as targets for the <code>&quot;goto&quot;</code>, <code>&quot;last&quot;</code>, <code>&quot;next&quot;</code> or <code>&quot;redo&quot;</code> statements cannot be keywords anymore. This restriction will prevent potential confusion between the <code>&quot;goto LABEL&quot;</code> and <code>&quot;goto EXPR&quot;</code> syntaxes: for example, a statement like <code>&quot;goto print&quot;</code> would jump to a label whose name would be the return value of <code>&quot;print()&quot;</code>, (usually 1), instead of a label named <code>&quot;print&quot;</code>. Moreover, the other control flow statements would just ignore any keyword passed to them as a label name. Since such labels cannot be defined anymore, this kind of error will be avoided.  </p>
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
<dd> <p> The internal structure of the <code>&quot;ext/&quot;</code> directory in the perl source has been reorganised. In general, a module <code>&quot;Foo::Bar&quot;</code> whose source was stored under <i>ext/Foo/Bar/</i> is now located under <i>ext/Foo-Bar/</i>. Also, nearly all dual-life modules have been moved from <i>lib/</i> to <i>ext/</i>. This is purely a source tarball change, and should make no difference to the compilation or installation of perl, unless you have a very customised build process that explicitly relies on this structure, or which hard-codes the <code>&quot;nonxs_ext&quot;</code> <i>Configure</i> parameter. Specifically, this change does not by default alter the location of any files in the final installation. </p>
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
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;length undef&quot;</code> now returns undef. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unsupported private C <font SIZE="-1">API</font> functions are now declared ``static&#8217;&#8216; to prevent leakage to Perl&#8217;s public <font SIZE="-1">API</font>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> To support the bootstrapping process, <i>miniperl</i> no longer builds with <font SIZE="-1">UTF-8</font> support in the regexp engine. </p>
<p> This allows a build to complete with <font SIZE="-1">PERL_UNICODE</font> set and a <font SIZE="-1">UTF-8</font> locale. Without this there&#8217;s a bootstrapping problem, as miniperl can&#8217;t load the <font SIZE="-1">UTF-8</font> components of the regexp engine, because they&#8217;re not yet built. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>miniperl</i>&#8216;s <code>@INC</code> is now restricted to just -I..., the split of <code>$ENV</code>{<font SIZE="-1">PERL5LIB</font>}, and ``.&#8216;&#8216; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A space or a newline is now required after a <code>&quot;#line XXX&quot;</code> directive. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tied filehandles now have an additional method <font SIZE="-1">EOF</font> which provides the <font SIZE="-1">EOF</font> type </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> To better match all other flow control statements, <code>&quot;foreach&quot;</code> may no longer be used as an attribute. </p>
 </dd></dl>
<h2>Core Enhancements</h2>
<h3>Unicode Character Database 5.1.0</h3>
<p> The copy of the Unicode Character Database included in Perl 5.11.0 has been updated to 5.1.0 from 5.0.0. See &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode5.1.0/#Notable_Changes">http://www.unicode.org/versions/Unicode5.1.0/#Notable_Changes</a>&gt; for the notable changes.  </p>
<h3>A proper interface for pluggable Method Resolution Orders</h3>
<p> As of Perl 5.11.0 there is a new interface for plugging and using method resolution orders other than the default (linear depth first search). The C3 method resolution order added in 5.10.0 has been re-implemented as a plugin, without changing its Perl-space interface. See perlmroapi for more information.  </p>
<h3>The overloading pragma</h3>
<p> This pragma allows you to lexically disable or enable overloading for some or all operations. (Yuval Kogman)  </p>
<h3>\N regex escape</h3>
<p> A new regex escape has been added, <code>&quot;\N&quot;</code>. It will match any character that is not a newline, independently from the presence or absence of the single line match modifier <code>&quot;/s&quot;</code>. (If <code>&quot;\N&quot;</code> is followed by an opening brace and by a letter, perl will still assume that a Unicode character name is coming, so compatibility is preserved.) (Rafael Garcia-Suarez)  </p>
<h3>Implicit strictures</h3>
<p> Using the <code>&quot;use VERSION&quot;</code> syntax with a version number greater or equal to 5.11.0 will also lexically enable strictures just like <code>&quot;use strict&quot;</code> would do (in addition to enabling features.) So, the following: </p>
<pre><code>    use 5.11.0;
</code></pre>
<p> will now imply: </p>
<pre><code>    use strict;
    use feature ':5.11';
</code></pre>
<h3>Parallel tests</h3>
<p> The core distribution can now run its regression tests in parallel on Unix-like platforms. Instead of running <code>&quot;make test&quot;</code>, set <code>&quot;TEST_JOBS&quot;</code> in your environment to the number of tests to run in parallel, and run <code>&quot;make test_harness&quot;</code>. On a Bourne-like shell, this can be done as </p>
<pre><code>    TEST_JOBS=3 make test_harness # Run 3 tests in parallel
</code></pre>
<p> An environment variable is used, rather than parallel make itself, because TAP::Harness needs to be able to schedule individual non-conflicting test scripts itself, and there is no standard interface to <code>&quot;make&quot;</code> utilities to interact with their job schedulers. </p>
<p> Note that currently some test scripts may fail when run in parallel (most notably <code>&quot;ext/IO/t/io_dir.t&quot;</code>). If necessary run just the failing scripts again sequentially and see if the failures go away.  </p>
<h3>The ... operator</h3>
<p> A new operator, <code>&quot;...&quot;</code>, nicknamed the Yada Yada operator, has been added. It is intended to mark placeholder code, that is not yet implemented. See ``Yada Yada Operator&#8217;&#8216; in perlop. (chromatic)  </p>
<h3>DTrace support</h3>
<p> Some support for DTrace has been added. See ``DTrace support&#8217;&#8216; in <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i>.  </p>
<font SIZE="-1"></font><h3>Support for configure_requires in CPAN module metadata</h3>
<p> Both <code>&quot;CPAN&quot;</code> and <code>&quot;CPANPLUS&quot;</code> now support the <code>&quot;configure_requires&quot;</code> keyword in the <i></i><font SIZE="-1"><i>META</i></font><i>.yml</i> metadata file included in most recent <font SIZE="-1">CPAN</font> distributions. This allows distribution authors to specify configuration prerequisites that must be installed before running <i>Makefile.PL</i> or <i>Build.PL</i>. </p>
<p> See the documentation for <code>&quot;ExtUtils::MakeMaker&quot;</code> or <code>&quot;Module::Build&quot;</code> for more on how to specify <code>&quot;configure_requires&quot;</code> when creating a distribution for <font SIZE="-1">CPAN</font>.  </p>
<h3>each is now more flexible</h3>
<p> The <code>&quot;each&quot;</code> function can now operate on arrays.  </p>
<h3>Y2038 compliance</h3>
<p> Perl&#8217;s core time-related functions are now Y2038 compliant. (With 29 years to spare!)  </p>
<h3>$, flexibility</h3>
<p> The variable <code>$,</code> may now be tied.  </p>
<h3>// in where clauses</h3>
<p> // now behaves like || in when clauses  </p>
<h3>Enabling warnings from your shell environment</h3>
<p> You can now set <code>&quot;-W&quot;</code> from the <code>&quot;PERL5OPT&quot;</code> environment variable  </p>
<h3>delete local</h3>
<p> <code>&quot;delete local&quot;</code> now allows you to locally delete a hash entry.  </p>
<h3>New support for Abstract namespace sockets</h3>
<p> Abstract namespace sockets are Linux-specific socket type that live in <font SIZE="-1">AF_UNIX</font> family, slightly abusing it to be able to use arbitrary character arrays as addresses: They start with nul byte and are not terminated by nul byte, but with the length passed to the <i>socket()</i> system call.  </p>
<h2>Modules and Pragmata</h2>
<h3>Dual-lifed modules moved</h3>
<p> Dual-lifed modules maintained primarily in the Perl core now live in dist/. Dual-lifed modules maintained primarily on <font SIZE="-1">CPAN</font> now live in cpan/ </p>
<p> In previous releases of Perl, it was customary to enumerate all module changes in this section of the <code>&quot;perldelta&quot;</code> file. From 5.11.0 forward only notable updates (such as new or deprecated modules ) will be listed in this section. For a complete reference to the versions of modules shipped in a given release of perl, please see Module::CoreList.  </p>
<h3>New Modules and Pragmata</h3>
<dl>
<dt>&quot;autodie&quot;</dt>
<dd> <p> This is a new lexically-scoped alternative for the <code>&quot;Fatal&quot;</code> module. The bundled version is 2.06_01. Note that in this release, using a string eval when <code>&quot;autodie&quot;</code> is in effect can cause the autodie behaviour to leak into the surrounding scope. See ``<font SIZE="-1">BUGS</font>&#8216;&#8216; in autodie for more details. </p>
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
<dt>&quot;overloading&quot;</dt>
<dd> <p> See &quot;The <code>&quot;overloading&quot;</code> pragma&quot; above. </p>
 </dd>
<dt>&quot;attrs&quot;</dt>
<dd> <p> The <code>&quot;attrs&quot;</code> pragma has been removed. It had been marked as deprecated since 5.6.0. </p>
 </dd>
<dt>&quot;charnames&quot;</dt>
<dd> <p> The Unicode <i>NameAliases.txt</i> database file has been added. This has the effect of adding some extra <code>&quot;\N&quot;</code> character names that formerly wouldn&#8217;t have been recognised; for example, <code>&quot;\N{LATIN CAPITAL LETTER GHA}&quot;</code>. </p>
 </dd>
<dt>&quot;feature&quot;</dt>
<dd> <p> The meaning of the <code>&quot;:5.10&quot;</code> and <code>&quot;:5.10.X&quot;</code> feature bundles has changed slightly. The last component, if any (i.e. <code>&quot;X&quot;</code>) is simply ignored. This is predicated on the assumption that new features will not, in general, be added to maintenance releases. So <code>&quot;:5.10&quot;</code> and <code>&quot;:5.10.X&quot;</code> have identical effect. This is a change to the behaviour documented for 5.10.0. </p>
 </dd>
<dt>&quot;mro&quot;</dt>
<dd> <p> Upgraded from version 1.00 to 1.01. Performance for single inheritance is 40% faster &#8211; see ``Performance Enhancements&#8217;&#8216; below. </p>
<p> <code>&quot;mro&quot;</code> is now implemented as an <font SIZE="-1">XS</font> extension. The documented interface has not changed. Code relying on the implementation detail that some <code>&quot;mro::&quot;</code> methods happened to be available at all times gets to ``keep both pieces&#8217;&#8216;. </p>
 </dd></dl>
<h3>Updated Modules</h3>
<dl>
<dt>&quot;ExtUtils::MakeMaker&quot;</dt>
<dd> <p> Upgraded from version 6.42 to 6.55_02. </p>
<p> Note that <code>&quot;ExtUtils::MakeMaker::bytes&quot;</code> and <code>&quot;ExtUtils::MakeMaker::vmsish&quot;</code> have been removed from this distribution. </p>
 </dd>
<dt>&quot;Test::Harness&quot;</dt>
<dd> <p> Upgraded from version 2.64 to 3.17. </p>
<p> Note that one side-effect of the 2.x to 3.x upgrade is that the experimental <code>&quot;Test::Harness::Straps&quot;</code> module (and its supporting <code>&quot;Assert&quot;</code>, <code>&quot;Iterator&quot;</code>, <code>&quot;Point&quot;</code> and <code>&quot;Results&quot;</code> modules) have been removed. If you still need this, then they are available in the (unmaintained) <code>&quot;Test-Harness-Straps&quot;</code> distribution on <font SIZE="-1">CPAN</font>. </p>
 </dd>
<dt>&quot;UNIVERSAL&quot;</dt>
<dd> <p> Upgraded from version 1.04 to 1.05. </p>
<p> <code>&quot;UNIVERSAL-&gt;import()&quot;</code> is now deprecated. </p>
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
<dt><i>perlbug</i></dt>
<dd> <p> <i>perlbug</i> now uses <code>%Module::CoreList::bug_tracker</code> to print out upstream bug tracker URLs. </p>
<p> Where the user names a module that their bug report is about, and we know the <font SIZE="-1">URL</font> for its upstream bug tracker, provide a message to the user explaining that the core copies the <font SIZE="-1">CPAN</font> version directly, and provide the <font SIZE="-1">URL</font> for reporting the bug directly to upstream. </p>
 </dd>
<dt><i>perlthanks</i></dt>
<dd> <p> Perl 5.11.0 added a new utility <i>perlthanks</i>, which is a variant of <i>perlbug</i>, but for sending non-bug-reports to the authors and maintainers of Perl. Getting nothing but bug reports can become a bit demoralising: we&#8217;ll see if this changes things. </p>
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
 </dd></dl>
<h2>Changes to Existing Documentation</h2>
<p> The various large <i>Changes*</i> files (which listed every change made to perl over the last 18 years) have been removed, and replaced by a small file, also called <i>Changes</i>, which just explains how that same information may be extracted from the git version control system. </p>
<p> The file <i>Porting/patching.pod</i> has been deleted, as it mainly described interacting with the old Perforce-based repository, which is now obsolete. Information still relevant has been moved to perlrepository. </p>
<p> perlapi, perlintern, perlmodlib and perltoc are now all generated at build time, rather than being shipped as part of the release. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Documented -X overloading. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Documented that <code>&quot;when()&quot;</code> treats specially most of the filetest operators </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Documented when as a syntax modifier </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Eliminated ``Old Perl threads tutorial&#8217;&#8216;, which describes 5005 threads. </p>
<p> <i>pod/perlthrtut.pod</i> is the same material reworked for ithreads. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Correct previous documentation: v-strings are not deprecated </p>
<p> With version objects, we need them to use <font SIZE="-1">MODULE</font> <font SIZE="-1">VERSION</font> syntax. This patch removes the deprecation note. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Added security contact information to perlsec </p>
 </dd></dl>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> A new internal cache means that <code>&quot;isa()&quot;</code> will often be faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The implementation of <code>&quot;C3&quot;</code> Method Resolution Order has been optimised &#8211; linearisation for classes with single inheritance is 40% faster. Performance for multiple inheritance is unchanged. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under <code>&quot;use locale&quot;</code>, the locale-relevant information is now cached on read-only values, such as the list returned by <code>&quot;keys %hash&quot;</code>. This makes operations such as <code>&quot;sort keys %hash&quot;</code> in the scope of <code>&quot;use locale&quot;</code> much faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Empty <code>&quot;DESTROY&quot;</code> methods are no longer called. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Faster <code>&quot;Perl_sv_utf8_upgrade()&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Speed up <code>&quot;keys&quot;</code> on empty hash </p>
 </dd></dl>
<h2>Installation and Configuration Improvements</h2>
<i></i><h3>ext/ reorganisation</h3>
<p> The layout of directories in <i>ext</i> has been revised. Specifically, all extensions are now flat, and at the top level, with <code>&quot;/&quot;</code> in pathnames replaced by <code>&quot;-&quot;</code>, so that <i>ext/Data/Dumper/</i> is now <i>ext/Data-Dumper/</i>, etc. The names of the extensions as specified to <i>Configure</i>, and as reported by <code>%Config::Config</code> under the keys <code>&quot;dynamic_ext&quot;</code>, <code>&quot;known_extensions&quot;</code>, <code>&quot;nonxs_ext&quot;</code> and <code>&quot;static_ext&quot;</code> have not changed, and still use <code>&quot;/&quot;</code>. Hence this change will not have any affect once perl is installed. <code>&quot;Safe&quot;</code> has been split out from being part of <code>&quot;Opcode&quot;</code>, and <code>&quot;mro&quot;</code> is now an extension in its own right. </p>
<p> Nearly all dual-life modules have been moved from <i>lib</i> to <i>ext</i>, and will now appear as known <code>&quot;nonxs_ext&quot;</code>. This will made no difference to the structure of an installed perl, nor will the modules installed differ, unless you run <i>Configure</i> with options to specify an exact list of extensions to build. In this case, you will rapidly become aware that you need to add to your list, because various modules needed to complete the build, such as <code>&quot;ExtUtils::ParseXS&quot;</code>, have now become extensions, and without them the build will fail well before it attempts to run the regression tests.  </p>
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
<dd> <p> Removed <i>libbsd</i> for <font SIZE="-1">AIX</font> 5L and 6.1. Only <code>&quot;flock()&quot;</code> was used from <i>libbsd</i>. </p>
<p> Removed <i>libgdbm</i> for <font SIZE="-1">AIX</font> 5L and 6.1. The <i>libgdbm</i> is delivered as an optional package with the <font SIZE="-1">AIX</font> Toolbox. Unfortunately the 64 bit version is broken. </p>
<p> Hints changes mean that <font SIZE="-1">AIX</font> 4.2 should work again. </p>
 </dd>
<dt>Cygwin</dt>
<dd> <p> On Cygwin we now strip the last number from the <font SIZE="-1">DLL</font>. This has been the behaviour in the cygwin.com build for years. The hints files have been updated. </p>
 </dd>
<dt>DomainOS</dt>
<dd> <p> Support for Apollo DomainOS was removed in Perl 5.11.0 </p>
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
<dt>MachTen</dt>
<dd> <p> Support for Tenon Intersystems MachTen Unix layer for MacOS Classic was removed in Perl 5.11.0 </p>
 </dd>
<dt>MiNT</dt>
<dd> <p> Support for Atari MiNT was removed in Perl 5.11.0. </p>
 </dd>
<dt>MirOS <font SIZE="-1">BSD</font></dt>
<dd> <p> Perl should now build on MirOS <font SIZE="-1">BSD</font>. </p>
 </dd>
<dt>NetBSD</dt>
<dd> <p> Hints now supports versions 5.*. </p>
 </dd>
<dt>Stratus <font SIZE="-1">VOS</font></dt>
<dd> <p> Various changes from Stratus have been merged in. </p>
 </dd>
<dt>Symbian</dt>
<dd> <p> There is now support for Symbian S60 3.2 <font SIZE="-1">SDK</font> and S60 5.0 <font SIZE="-1">SDK</font>. </p>
 </dd>
<dt>Win32</dt>
<dd> <p> Improved message window handling means that <code>&quot;alarm&quot;</code> and <code>&quot;kill&quot;</code> messages will no longer be dropped under race conditions. </p>
 </dd>
<dt><font SIZE="-1">VMS</font></dt>
<dd> <p> Reads from the in-memory temporary files of <code>&quot;PerlIO::scalar&quot;</code> used to fail if <code>$/</code> was set to a numeric reference (to indicate record-style reads). This is now fixed. </p>
<p> <font SIZE="-1">VMS</font> now supports <code>&quot;getgrgid&quot;</code>. </p>
<p> Many improvements and cleanups have been made to the <font SIZE="-1">VMS</font> file name handling and conversion code. </p>
<p> Enabling the <code>&quot;PERL_VMS_POSIX_EXIT&quot;</code> logical name now encodes a <font SIZE="-1">POSIX</font> exit status in a <font SIZE="-1">VMS</font> condition value for better interaction with <font SIZE="-1">GNV</font>&#8216;s bash shell and other utilities that depend on <font SIZE="-1">POSIX</font> exit values. See ``$?&#8216;&#8216; in perlvms for details. </p>
<p> <code>&quot;File::Copy&quot;</code> now detects Unix compatibility mode on <font SIZE="-1">VMS</font>. </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-I&quot;</code> on shebang line now adds directories in front of <code>@INC</code> as documented, and as does <code>&quot;-I&quot;</code> when specified on the command-line. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;kill&quot;</code> is now fatal when called on non-numeric process identifiers. Previously, an &#8216;undef&#8217; process identifier would be interpreted as a request to kill process ``0&#8217;&#8216;, which would terminate the current process group on <font SIZE="-1">POSIX</font> systems. Since process identifiers are always integers, killing a non-numeric process is now fatal. </p>
 </dd>
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
<dd> <p> <code>&quot;crypt&quot;</code> and string complement could return tainted values for untainted arguments [<font SIZE="-1">RT</font> #59998]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;-i&quot;</code><i>.suffix</i> command-line switch now recreates the file using restricted permissions, before changing its mode to match the original file. This eliminates a potential race condition [<font SIZE="-1">RT</font> #60904]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On some Unix systems, the value in <code>$?</code> would not have the top bit set (<code>&quot;$? &amp; 128&quot;</code>) even if the child core dumped. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under some circumstances, <code>$^R</code> could incorrectly become undefined [<font SIZE="-1">RT</font> #57042]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In the <font SIZE="-1">XS</font> <font SIZE="-1">API</font>, various hash functions, when passed a pre-computed hash where the key is <font SIZE="-1">UTF-8</font>, might result in an incorrect lookup. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">XS</font> code including <i></i><font SIZE="-1"><i>XSUB</i></font><i>.h</i> before <i>perl.h</i> gave a compile-time error [<font SIZE="-1">RT</font> #57176]. </p>
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
<dd> <p> Using <code>&quot;setpgrp&quot;</code> with no arguments could corrupt the perl stack. </p>
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
<dd> <p> Using an array <code>&quot;tie&quot;</code> inside in array <code>&quot;tie&quot;</code> could <font SIZE="-1">SEGV</font>. This has been fixed. [<font SIZE="-1">RT</font> #51636] </p>
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
<dd> <p> Calling <code>&quot;Perl_sv_chop()&quot;</code> or otherwise upgrading an <font SIZE="-1">SV</font> could result in an unaligned 64-bit access on the <font SIZE="-1">SPARC</font> architecture [<font SIZE="-1">RT</font> #60574]. </p>
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
 </dd>
<dt>&bull;</dt>
<dd> <p> Previously missing files from Unicode 5.1 Character Database are now included. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;TMPDIR&quot;</code> is now honored when opening an anonymous temporary file </p>
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
<dd> <p> <font SIZE="-1">TODO:</font> <code>&quot;SVt_RV&quot;</code> is gone. RVs are now stored in IVs </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">TODO:</font> REGEXPs are first class </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">TODO:</font> <font SIZE="-1">OOK</font> is reworked, such that an OOKed scalar is <font SIZE="-1">PV</font> not <font SIZE="-1">PVIV</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The J.R.R. Tolkien quotes at the head of C source file have been checked and proper citations added, thanks to a patch from Tom Christiansen. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Perl_vcroak()&quot;</code> now accepts a null first argument. In addition, a full audit was made of the ``not <font SIZE="-1">NULL</font>&#8216;&#8216; compiler annotations, and those for several other internal functions were corrected. </p>
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
<dd> <p> This will call <code>&quot;SvUTF8_on()&quot;</code> for you. (Note that this does not convert an sequence of <font SIZE="-1">ISO</font> 8859-1 characters to <font SIZE="-1">UTF-8</font>). A wrapper, <code>&quot;newSVpvn_utf8()&quot;</code> is available for this. </p>
 </dd>
<dt>&quot;SVs_TEMP&quot;</dt>
<dd> <p> Call <code>&quot;Perl_sv_2mortal()&quot;</code> on the new <font SIZE="-1">SV</font>. </p>
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
<dd> <p> <code>&quot;Perl_mg_free()&quot;</code> used to leave freed memory accessible via <code>&quot;SvMAGIC()&quot;</code> on the scalar. It now updates the linked list to remove each piece of magic as it is freed. </p>
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
<dd> <p> Smartmatch resolution tracing has been added as a new diagnostic. Use <code>&quot;-DM&quot;</code> to enable it. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new debugging flag <code>&quot;-DB&quot;</code> now dumps subroutine definitions, leaving <code>&quot;-Dx&quot;</code> for its original purpose of dumping syntax trees. </p>
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
<dd> <p> A new tool, <i>Porting/expand-macro.pl</i> has been added, that allows you to view how a C preprocessor macro would be expanded when compiled. This is handy when trying to decode the macro hell that is the perl guts. </p>
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
<dd> <p> The following modules will be removed from the core distribution in a future release, and should be installed from <font SIZE="-1">CPAN</font> instead. Distributions on <font SIZE="-1">CPAN</font> which require these should add them to their prerequisites. The core versions of these modules warnings will issue a deprecation warning. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Class::ISA&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Pod::Plainer&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Shell&quot;</code> </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> Currently support to install from <font SIZE="-1">CPAN</font> without a <i>force</i> is <code>&quot;TODO&quot;</code> in <font SIZE="-1">CPAN</font> and <font SIZE="-1">CPANPLUS</font>. This will be addressed before 5.12.0 ships. </p>
 </dd></dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;suidperl&quot;</code> has been removed. It used to provide a mechanism to emulate setuid permission bits on systems that don&#8217;t support it properly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Deprecate assignment to $[ </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Remove attrs, which has been deprecated since 1999/10/02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Deprecate use of the attribute :locked on subroutines. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Deprecate using ``locked&#8217;&#8216; with the attributes pragma. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Deprecate using ``unique&#8217;&#8216; with the attributes pragma. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> warn if ++ or --- are unable to change the value because it&#8217;s beyond the limit of representation </p>
<p> This uses a new warnings category: ``imprecision&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Make lc/uc/lcfirst/ucfirst warn when passed undef. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Show constant in ``Useless use of a constant in void context&#8217;&#8216; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Make the new warning report undef constants as undef </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Add a new warning, ``Prototype after &#8216;%s&#8217;&#8216;&#8216; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tweak the ``Illegal character in prototype&#8217;&#8216; warning so it&#8217;s more precise when reporting illegal characters after _ </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unintended interpolation of $\ in regex </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Make overflow warnings in gmtime/localtime only occur when warnings are on </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Improve mro merging error messages. </p>
<p> They are now very similar to those produced by Algorithm::C3. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Amelioration of the error message ``Unrecognized character <code>%s</code> in column <code>%d</code>&#8216;&#8216; </p>
<p> Changes the error message to ``Unrecognized character <code>%s</code>; marked by &lt;-- <font SIZE="-1">HERE</font> after <code>%s</code>&lt;-- <font SIZE="-1">HERE</font> near column <code>%d</code>&#8216;&#8216;. This should make it a little simpler to spot and correct the suspicious character. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Explicitly point to $. when it causes an uninitialized warning for ranges in scalar context </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Deprecated numerous Perl 4-era libraries: </p>
<p> <i>termcap.pl</i>, <i>tainted.pl</i>, <i>stat.pl</i>, <i>shellwords.pl</i>, <i>pwd.pl</i>, <i>open3.pl</i>, <i>open2.pl</i>, <i>newgetopt.pl</i>, <i>look.pl</i>, <i>find.pl</i>, <i>finddepth.pl</i>, <i>importenv.pl</i>, <i>hostname.pl</i>, <i>getopts.pl</i>, <i>getopt.pl</i>, <i>getcwd.pl</i>, <i>flush.pl</i>, <i>fastcwd.pl</i>, <i>exceptions.pl</i>, <i>ctime.pl</i>, <i>complete.pl</i>, <i>cacheout.pl</i>, <i>bigrat.pl</i>, <i>bigint.pl</i>, <i>bigfloat.pl</i>, <i>assert.pl</i>, <i>abbrev.pl</i>, <i>dotsh.pl</i>, and <i>timelocal.pl</i> are all now deprecated. Using them will incur a warning. </p>
 </dd></dl>
<h2>Acknowledgements</h2>
<p> Some of the work in this release was funded by a <font SIZE="-1">TPF</font> grant funded by Dijkmat <font SIZE="-1">BV</font>, The Netherlands. </p>
<p> Steffen Mueller and David Golden in particular helped getting <font SIZE="-1">CPAN</font> modules polished and synchronised with their in-core equivalents. </p>
<p> Craig Berry was tireless in getting maint to run under <font SIZE="-1">VMS</font>, no matter how many times we broke it for him. </p>
<p> The other core committers contributed most of the changes, and applied most of the patches sent in by the hundreds of contributors listed in <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i>. </p>
<p> Much of the work of categorizing changes in this perldelta file was contributed by the following porters using changelogger.bestpractical.com: </p>
<p> Nicholas Clark, leon, shawn, alexm, rjbs, rafl, Pedro Melo, brunorc, anonymous, X, Tom Hukins, anonymous, Jesse, dagolden, Moritz Onken, Mark Fowler, chorny, anonymous, tmtm </p>
<p> Finally, thanks to Larry Wall, without whom none of this would be necessary.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN</font>.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
