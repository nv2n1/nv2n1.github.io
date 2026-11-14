---
title: "perl591delta(1)"
name: "perl591delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl591delta/"
description: "perl591delta – what is new for perl v5.9.1"
---

<h2 class="name">NAME</h2>
<p> perl591delta &#8211; what is new for perl v5.9.1 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.9.0 and the 5.9.1 development releases. See perl590delta for the differences between 5.8.0 and 5.9.0.</p>
<h2>Incompatible Changes</h2>
<h3><i>substr()</i> lvalues are no longer fixed-length</h3>
<p> The lvalues returned by the three argument form of <i>substr()</i> used to be a &#8220;fixed length window&#8221; on the original string. In some cases this could cause surprising action at distance or other undefined behaviour. Now the length of the window adjusts itself to the length of the string assigned to it.</p>
<h3>The :unique attribute is only meaningful for globals</h3>
<p> Now applying <tt>&quot;:unique&quot;</tt> to lexical variables and to subroutines will result in a compilation error.</p>
<h2>Core Enhancements</h2>
<h3>Lexical $_</h3>
<p> The default variable <tt>$_</tt> can now be lexicalized, by declaring it like any other lexical variable, with a simple </p>
<pre>
    my $_;
</pre>
<p> The operations that default on <tt>$_</tt> will use the lexically-scoped version of <tt>$_</tt> when it exists, instead of the global <tt>$_</tt>. </p>
<p> In a <tt>&quot;map&quot;</tt> or a <tt>&quot;grep&quot;</tt> block, if <tt>$_</tt> was previously my&#8217;ed, then the <tt>$_</tt> inside the block is lexical as well (and scoped to the block). </p>
<p> In a scope where <tt>$_</tt> has been lexicalized, you can still have access to the global version of <tt>$_</tt> by using <tt>$::_</tt>, or, more simply, by overriding the lexical declaration with <tt>&quot;our $_&quot;</tt>.</p>
<h3>Tied hashes in scalar context</h3>
<p> As of perl 5.8.2/5.9.0, tied hashes did not return anything useful in scalar context, for example when used as boolean tests: </p>
<pre>
        if (%tied_hash) { ... }
</pre>
<p> The old nonsensical behaviour was always to return false, regardless of whether the hash is empty or has elements. </p>
<p> There is now an interface for the implementors of tied hashes to implement the behaviour of a hash in scalar context, via the <font SIZE="-1">SCALAR</font> method (see perltie). Without a <font SIZE="-1">SCALAR</font> method, perl will try to guess whether the hash is empty, by testing if it&#8217;s inside an iteration (in this case it can&#8217;t be empty) or by calling <font SIZE="-1">FIRSTKEY</font>.</p>
<h3>Formats</h3>
<p> Formats were improved in several ways. A new field, <tt>&quot;^*&quot;</tt>, can be used for variable-width, one-line-at-a-time text. Null characters are now handled correctly in picture lines. Using <tt>&quot;@#&quot;</tt> and <tt>&quot;~~&quot;</tt> together will now produce a compile-time error, as those format fields are incompatible. perlform has been improved, and miscellaneous bugs fixed.</p>
<h3>Stacked filetest operators</h3>
<p> As a new form of syntactic sugar, it&#8217;s now possible to stack up filetest operators. You can now write <tt>&quot;-f -w -x $file&quot;</tt> in a row to mean <tt>&quot;-x $file &amp;&amp; -w _ &amp;&amp; -f _&quot;</tt>. See &#8220;-X&#8221; in perlfunc.</p>
<h2>Modules and Pragmata</h2>
<dl>
<dt>Benchmark</p>
<dd> In <tt>&quot;Benchmark&quot;</tt>, <i>cmpthese()</i> and <i>timestr()</i> now use the time statistics of children instead of parent when the selected style is &#8216;nop&#8217;.</p>
<dt>Carp</p>
<dd> The error messages produced by <tt>&quot;Carp&quot;</tt> now include spaces between the arguments in function argument lists: this makes long error messages appear more nicely in browsers and other tools.</p>
<dt>Exporter</p>
<dd> <tt>&quot;Exporter&quot;</tt> will now recognize grouping tags (such as <tt>&quot;:name&quot;</tt>) anywhere in the import list, not only at the beginning.</p>
<dt>FindBin</p>
<dd> A function <tt>&quot;again&quot;</tt> is provided to resolve problems where modules in different directories wish to use FindBin.</p>
<dt>List::Util</p>
<dd> You can now weaken references to read only values.</p>
<dt>threads::shared</p>
<dd> <tt>&quot;cond_wait&quot;</tt> has a new two argument form. <tt>&quot;cond_timedwait&quot;</tt> has been added.</dl>
<h2>Utility Changes</h2>
<p> <tt>&quot;find2perl&quot;</tt> now assumes <tt>&quot;-print&quot;</tt> as a default action. Previously, it needed to be specified explicitly. </p>
<p> A new utility, <tt>&quot;prove&quot;</tt>, makes it easy to run an individual regression test at the command line. <tt>&quot;prove&quot;</tt> is part of Test::Harness, which users of earlier Perl versions can install from <font SIZE="-1">CPAN</font>. </p>
<p> The perl debugger now supports a <tt>&quot;save&quot;</tt> command, to save the current history to a file, and an <tt>&quot;i&quot;</tt> command, which prints the inheritance tree of its argument (if the <tt>&quot;Class::ISA&quot;</tt> module is installed.)</p>
<h2>Documentation</h2>
<p> The documentation has been revised in places to produce more standard manpages. </p>
<p> The long-existing feature of <tt>&quot;/(?{...})/&quot;</tt> regexps setting <tt>$_</tt> and <i>pos()</i> is now documented.</p>
<h2>Performance Enhancements</h2>
<p> Sorting arrays in place (<tt>&quot;@a = sort @a&quot;</tt>) is now optimized to avoid making a temporary copy of the array. </p>
<p> The operations involving case mapping on <font SIZE="-1">UTF-8</font> strings (<i>uc()</i>, <i>lc()</i>, <tt>&quot;//i&quot;</tt>, etc.) have been greatly speeded up. </p>
<p> Access to elements of lexical arrays via a numeric constant between 0 and 255 is now faster. (This used to be only the case for global arrays.)</p>
<h2>Selected Bug Fixes</h2>
<h3><font SIZE="-1">UTF-8</font> bugs</h3>
<p> Using <i>substr()</i> on a <font SIZE="-1">UTF-8</font> string could cause subsequent accesses on that string to return garbage. This was due to incorrect <font SIZE="-1">UTF-8</font> offsets being cached, and is now fixed. </p>
<p> <i>join()</i> could return garbage when the same <i>join()</i> statement was used to process 8 bit data having earlier processed <font SIZE="-1">UTF-8</font> data, due to the flags on that statement&#8217;s temporary workspace not being reset correctly. This is now fixed. </p>
<p> Using Unicode keys with tied hashes should now work correctly. </p>
<p> <i>chop()</i> and <i>chomp()</i> used to mangle <font SIZE="-1">UTF-8</font> strings. This has been fixed. </p>
<p> <i>sprintf()</i> used to misbehave when the format string was in <font SIZE="-1">UTF-8</font>. This is now fixed.</p>
<h3>Threading bugs</h3>
<p> Hashes with the <tt>&quot;:unique&quot;</tt> attribute weren&#8217;t made read-only in new threads. They are now.</p>
<h3>More bugs</h3>
<p> <tt>&quot;$a .. $b&quot;</tt> will now work as expected when either <tt>$a</tt> or <tt>$b</tt> is <tt>&quot;undef&quot;</tt>. </p>
<p> Reading $^E now preserves $!. Previously, the C code implementing $^E did not preserve <tt>&quot;errno&quot;</tt>, so reading $^E could cause <tt>&quot;errno&quot;</tt> and therefore <tt>$!</tt> to change unexpectedly. </p>
<p> <tt>&quot;strict&quot;</tt> wasn&#8217;t in effect in regexp-eval blocks (<tt>&quot;/(?{...})/&quot;</tt>).</p>
<h2>New or Changed Diagnostics</h2>
<p> A new deprecation warning, <i>Deprecated use of my() in false conditional</i>, has been added, to warn against the use of the dubious and deprecated construct </p>
<pre>
    my $x if 0;
</pre>
<p> See perldiag. </p>
<p> The fatal error <i></i><font SIZE="-1"><i>DESTROY</i></font><i> created new reference to dead object</i> is now documented in perldiag. </p>
<p> A new error, <i></i>%ENV<i> is aliased to </i>%s<i></i>, is produced when taint checks are enabled and when <tt>*ENV</tt> has been aliased (and thus doesn&#8217;t reflect the program&#8217;s environment anymore.)</p>
<h2>Changed Internals</h2>
<p> These news matter to you only if you either write <font SIZE="-1">XS</font> code or like to know about or hack Perl internals (using Devel::Peek or any of the <tt>&quot;B::&quot;</tt> modules counts), or like to run Perl with the <tt>&quot;-D&quot;</tt> option.</p>
<h3>Reordering of SVt_* constants</h3>
<p> The relative ordering of constants that define the various types of <tt>&quot;SV&quot;</tt> have changed; in particular, <tt>&quot;SVt_PVGV&quot;</tt> has been moved before <tt>&quot;SVt_PVLV&quot;</tt>, <tt>&quot;SVt_PVAV&quot;</tt>, <tt>&quot;SVt_PVHV&quot;</tt> and <tt>&quot;SVt_PVCV&quot;</tt>. This is unlikely to make any difference unless you have code that explicitly makes assumptions about that ordering. (The inheritance hierarchy of <tt>&quot;B::*&quot;</tt> objects has been changed to reflect this.)</p>
<h3>Removal of <font SIZE="-1">CPP</font> symbols</h3>
<p> The C preprocessor symbols <tt>&quot;PERL_PM_APIVERSION&quot;</tt> and <tt>&quot;PERL_XS_APIVERSION&quot;</tt>, which were supposed to give the version number of the oldest perl binary-compatible (resp. source-compatible) with the present one, were not used, and sometimes had misleading values. They have been removed.</p>
<h3>Less space is used by ops</h3>
<p> The <tt>&quot;BASEOP&quot;</tt> structure now uses less space. The <tt>&quot;op_seq&quot;</tt> field has been removed and replaced by two one-bit fields, <tt>&quot;op_opt&quot;</tt> and <tt>&quot;op_static&quot;</tt>. <tt>&quot;opt_type&quot;</tt> is now 9 bits long. (Consequently, the <tt>&quot;B::OP&quot;</tt> class doesn&#8217;t provide an <tt>&quot;seq&quot;</tt> method anymore.)</p>
<h3>New parser</h3>
<p> perl&#8217;s parser is now generated by bison (it used to be generated by byacc.) As a result, it seems to be a bit more robust.</p>
<h2>Configuration and Building</h2>
<p> <tt>&quot;Configure&quot;</tt> now invokes callbacks regardless of the value of the variable they are called for. Previously callbacks were only invoked in the <tt>&quot;case $variable $define)&quot;</tt> branch. This change should only affect platform maintainers writing configuration hints files. </p>
<p> The portability and cleanliness of the Win32 makefiles has been improved.</p>
<h2>Known Problems</h2>
<p> There are still a couple of problems in the implementation of the lexical <tt>$_</tt>: it doesn&#8217;t work inside <tt>&quot;/(?{...})/&quot;</tt> blocks and with regard to the <i>reverse()</i> built-in used without arguments. (See the <font SIZE="-1">TODO</font> tests in <i>t/op/mydef.t</i>.)</p>
<h3>Platform Specific Problems</h3>
<p> The test <i>ext/IPC/SysV/t/ipcsysv.t</i> may fail on OpenBSD. This hasn&#8217;t been diagnosed yet. </p>
<p> On some configurations on <font SIZE="-1">AIX</font> 5, one test in <i>lib/Time/Local.t</i> fails. When configured with long doubles, perl may fail tests 224-236 in <i>t/op/pow.t</i> on the same platform. </p>
<p> For threaded builds, <i>ext/threads/shared/t/wait.t</i> has been reported to fail some tests on HP-UX 10.20.</p>
<h2>To-do for perl 5.10.0</h2>
<p> This is a non-exhaustive, non-ordered, non-contractual and non-definitive list of things to do (or nice to have) for perl 5.10.0 : </p>
<p> Clean up and finish support for assertions. See assertions. </p>
<p> Reimplement the mechanism of lexical pragmas to be more extensible. Fix current pragmas that don&#8217;t work well (or at all) with lexical scopes or in run-time eval(<font SIZE="-1">STRING</font>) (<tt>&quot;sort&quot;</tt>, <tt>&quot;re&quot;</tt>, <tt>&quot;encoding&quot;</tt> for example). <font SIZE="-1">MJD</font> has a preliminary patch that implements this. </p>
<p> Fix (or rewrite) the implementation of the <tt>&quot;/(?{...})/&quot;</tt> closures. </p>
<p> Conversions from byte strings to <font SIZE="-1">UTF-8</font> currently map high bit characters to Unicode without translation (or, depending on how you look at it, by implicitly assuming that the byte strings are in Latin-1). As perl assumes the C locale by default, upgrading a string to <font SIZE="-1">UTF-8</font> may change the meaning of its contents regarding character classes, case mapping, etc. This should probably emit a warning (at least). </p>
<p> Introduce a new special block, <font SIZE="-1">UNITCHECK</font>, which is run at the end of a compilation unit (module, file, eval(<font SIZE="-1">STRING</font>) block). This will correspond to the Perl 6 <font SIZE="-1">CHECK</font>. Perl 5&#8217;s <font SIZE="-1">CHECK</font> cannot be changed or removed because the O.pm/B.pm backend framework depends on it. </p>
<p> Study the possibility of adding a new prototype character, <tt>&quot;_&quot;</tt>, meaning &#8220;this argument defaults to <tt>$_</tt>&#8221;. </p>
<p> Make the peephole optimizer optional. </p>
<p> Allow lexical aliases (maybe via the syntax <tt>&quot;my \$alias = \$foo&quot;</tt>. </p>
<p> Fix the bugs revealed by running the test suite with the <tt>&quot;-t&quot;</tt> switch (via <tt>&quot;make test.taintwarn&quot;</tt>). </p>
<p> Make threads more robust. </p>
<p> Make <tt>&quot;no 6&quot;</tt> and <tt>&quot;no v6&quot;</tt> work (opposite of <tt>&quot;use 5.005&quot;</tt>, etc.). </p>
<p> A test suite for the B module would be nice. </p>
<p> A ponie.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
<dt><a href="#lbAG">Core Enhancements</a></p>
<dd>
<dt><a href="#lbAL">Modules and Pragmata</a></p>
<dd>
<dt><a href="#lbAM">Utility Changes</a></p>
<dd>
<dt><a href="#lbAN">Documentation</a></p>
<dd>
<dt><a href="#lbAO">Performance Enhancements</a></p>
<dd>
<dt><a href="#lbAP">Selected Bug Fixes</a></p>
<dd>
<dt><a href="#lbAT">New or Changed Diagnostics</a></p>
<dd>
<dt><a href="#lbAU">Changed Internals</a></p>
<dd>
<dt><a href="#lbAZ">Configuration and Building</a></p>
<dd>
<dt><a href="#lbBA">Known Problems</a></p>
<dd>
<dt><a href="#lbBC">To-do for perl 5.10.0</a></p>
<dd>
<dt><a href="#lbBD">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbBE">SEE ALSO</a></p>
<dd></dl>
