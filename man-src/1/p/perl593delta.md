---

title: "perl593delta(1)"
name: "perl593delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl593delta/"
description: "perl593delta – what is new for perl v5.9.3"
---

<p> perl593delta - what is new for perl v5.9.3 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.9.2 and the 5.9.3 development releases. See perl590delta, perl591delta and perl592delta for the differences between 5.8.0 and 5.9.2.  </p>
<h2>Incompatible Changes</h2>
<h3>Parsing of -f _</h3>
<p> The identifier <code>&quot;_&quot;</code> is now forced to be a bareword after a filetest operator. This solves a number of misparsing issues when a global <code>&quot;_&quot;</code> subroutine is defined.  </p>
<h3>mkdir()</h3>
<p> <code>&quot;mkdir()&quot;</code> without arguments now defaults to <code>$_</code>.  </p>
<h3>Magic goto and eval</h3>
<p> The construct <code>&quot;eval { goto &amp;foo }&quot;</code> is now disallowed. (Note that the similar construct, but with <code>&quot;eval(&quot;&quot;)&quot;</code> instead, was already forbidden.)  </p>
<h3>$# has been removed</h3>
<p> The deprecated <code>$#</code> variable (output format for numbers) has been removed. A new warning, <code>&quot;$# is no longer supported&quot;</code>, has been added.  </p>
<h3>:unique</h3>
<p> The <code>&quot;:unique&quot;</code> attribute has been made a no-op, since its current implementation was fundamentally flawed and not threadsafe.  </p>
<h3>Scoping of the sort pragma</h3>
<p> The <code>&quot;sort&quot;</code> pragma is now lexically scoped. Its effect used to be global.  </p>
<h2>Core Enhancements</h2>
<h3>The feature pragma</h3>
<p> The <code>&quot;feature&quot;</code> pragma is used to enable new syntax that would break Perl&#8217;s backwards-compatibility with older releases of the language. It&#8217;s a lexical pragma, like <code>&quot;strict&quot;</code> or <code>&quot;warnings&quot;</code>. </p>
<p> Currently the following new features are available: <code>&quot;switch&quot;</code> (adds a switch statement), <code>&quot;~~&quot;</code> (adds a Perl 6-like smart match operator), <code>&quot;say&quot;</code> (adds a <code>&quot;say&quot;</code> built-in function), and <code>&quot;err&quot;</code> (adds an <code>&quot;err&quot;</code> keyword). Those features are described below. </p>
<p> Note that <code>&quot;err&quot;</code> low-precedence defined-or operator used to be enabled by default (although as a weak keyword, meaning that any function would override it). It&#8217;s now only recognized when explicitly turned on (and is then a regular keyword). </p>
<p> Those features, and the <code>&quot;feature&quot;</code> pragma itself, have been contributed by Robin Houston.  </p>
<h3>Switch and Smart Match operator</h3>
<p> Perl 5 now has a switch statement. It&#8217;s available when <code>&quot;use feature &#8216;switch&#8217;&quot;</code> is in effect. This feature introduces three new keywords, <code>&quot;given&quot;</code>, <code>&quot;when&quot;</code>, and <code>&quot;default&quot;</code>: </p>
<pre><code>    given ($foo) {
        when (/^abc/) { $abc = 1; }
        when (/^def/) { $def = 1; }
        when (/^xyz/) { $xyz = 1; }
        default { $nothing = 1; }
    }
</code></pre>
<p> A more complete description of how Perl matches the switch variable against the <code>&quot;when&quot;</code> conditions is given in ``Switch statements&#8217;&#8216; in perlsyn. </p>
<p> This kind of match is called <i>smart match</i>, and it&#8217;s also possible to use it outside of switch statements, via the new <code>&quot;~~&quot;</code> operator (enabled via the <code>&quot;use feature &#8216;~~&#8216;&quot;</code> directive). See ``Smart matching in detail&#8217;&#8216; in perlsyn.  </p>
<h3>say()</h3>
<p> <i>say()</i> is a new built-in, only available when <code>&quot;use feature &#8216;say&#8217;&quot;</code> is in effect, that is similar to <i>print()</i>, but that implicitly appends a newline to the printed string. See ``say&#8217;&#8216; in perlfunc.  </p>
<h3>CLONE_SKIP()</h3>
<p> Perl has now support for the <code>&quot;CLONE_SKIP&quot;</code> special subroutine. Like <code>&quot;CLONE&quot;</code>, <code>&quot;CLONE_SKIP&quot;</code> is called once per package; however, it is called just before cloning starts, and in the context of the parent thread. If it returns a true value, then no objects of that class will be cloned. See perlmod for details. (Contributed by Dave Mitchell.)  </p>
<h3>${^CHILD_ERROR_NATIVE}</h3>
<p> A new internal variable, <code>&quot;${^CHILD_ERROR_NATIVE}&quot;</code>, gives the native status returned by the last pipe close, backtick command, successful call to <i>wait()</i> or <i>waitpid()</i>, or from the <i>system()</i> operator. See perlrun for details. (Contributed by Gisle Aas.)  </p>
<h3>Assertions</h3>
<p> The support for assertions, introduced in perl 5.9.0, has been improved. The syntax for the <code>&quot;-A&quot;</code> command-line switch has changed; it now accepts an optional module name, defaulting to <code>&quot;assertions::activate&quot;</code>. See assertions and perlrun. (Contributed by Salvador Fandin~o Garcia.)  </p>
<h3>Unicode Character Database 4.1.0</h3>
<p> The copy of the Unicode Character Database included in Perl 5.9 has been updated to 4.1.0.  </p>
<h3>no VERSION</h3>
<p> You can now use <code>&quot;no&quot;</code> followed by a version number to specify that you want to use a version of perl older than the specified one.  </p>
<h3>Recursive sort subs</h3>
<p> You can now use recursive subroutines with <i>sort()</i>, thanks to Robin Houston.  </p>
<h3>Effect of pragmas in eval</h3>
<p> The compile-time value of the <code>&quot;%^H&quot;</code> hint variable can now propagate into eval(&quot;&quot;)uated code. This makes it more useful to implement lexical pragmas. </p>
<p> As a side-effect of this, the overloaded-ness of constants now propagates into eval(&quot;&quot;).  </p>
<code></code><h3>New -E command-line switch</h3>
<p> <code>-E</code> is equivalent to <code>-e</code>, but it implicitly enables all optional features (like <code>&quot;use feature &quot;:5.10&quot;&quot;</code>).  </p>
<h3>chdir, chmod and chown on filehandles</h3>
<p> <code>&quot;chdir&quot;</code>, <code>&quot;chmod&quot;</code> and <code>&quot;chown&quot;</code> can now work on filehandles as well as filenames, if the system supports respectively <code>&quot;fchdir&quot;</code>, <code>&quot;fchmod&quot;</code> and <code>&quot;fchown&quot;</code>, thanks to a patch provided by Gisle Aas.  </p>
<font SIZE="-1"></font><h3>OS groups</h3>
<p> <code>$(</code> and <code>$)</code> now return groups in the order where the <font SIZE="-1">OS</font> returns them, thanks to Gisle Aas. This wasn&#8217;t previously the case.  </p>
<h2>Modules and Pragmata</h2>
<h3>New Core Modules</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> A new pragma, <code>&quot;feature&quot;</code>, has been added; see above in ``Core Enhancements&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;assertions::compat&quot;</code>, also available on <font SIZE="-1">CPAN</font>, allows the use of assertions on perl versions prior to 5.9.0 (that is the first one to natively support them). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Math::BigInt::FastCalc&quot;</code> is an XS-enabled, and thus faster, version of <code>&quot;Math::BigInt::Calc&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Compress::Zlib&quot;</code> is an interface to the zlib compression library. It comes with a bundled version of zlib, so having a working zlib is not a prerequisite to install it. It&#8217;s used by <code>&quot;Archive::Tar&quot;</code> (see below). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;IO::Zlib&quot;</code> is an <code>&quot;IO::&quot;</code>-style interface to <code>&quot;Compress::Zlib&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Archive::Tar&quot;</code> is a module to manipulate <code>&quot;tar&quot;</code> archives. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Digest::SHA&quot;</code> is a module used to calculate many types of <font SIZE="-1">SHA</font> digests, has been included for <font SIZE="-1">SHA</font> support in the <font SIZE="-1">CPAN</font> module. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;ExtUtils::CBuilder&quot;</code> and <code>&quot;ExtUtils::ParseXS&quot;</code> have been added. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<h3>ptar</h3>
<p> <code>&quot;ptar&quot;</code> is a pure perl implementation of <code>&quot;tar&quot;</code>, that comes with <code>&quot;Archive::Tar&quot;</code>.  </p>
<h3>ptardiff</h3>
<p> <code>&quot;ptardiff&quot;</code> is a small script used to generate a diff between the contents of a tar archive and a directory tree. Like <code>&quot;ptar&quot;</code>, it comes with <code>&quot;Archive::Tar&quot;</code>.  </p>
<h3>shasum</h3>
<p> This command-line utility, used to print or to check <font SIZE="-1">SHA</font> digests, comes with the new <code>&quot;Digest::SHA&quot;</code> module.  </p>
<h3>h2xs enhancements</h3>
<p> <code>&quot;h2xs&quot;</code> implements a new option <code>&quot;--use-xsloader&quot;</code> to force use of <code>&quot;XSLoader&quot;</code> even in backwards compatible modules. </p>
<p> The handling of authors&#8217; names that had apostrophes has been fixed. </p>
<p> Any enums with negative values are now skipped.  </p>
<h3>perlivp enhancements</h3>
<p> <code>&quot;perlivp&quot;</code> no longer checks for <i>*.ph</i> files by default. Use the new <code>&quot;-a&quot;</code> option to run <i>all</i> tests.  </p>
<h2>Documentation</h2>
<h3>Perl Glossary</h3>
<p> The perlglossary manpage is a glossary of terms used in the Perl documentation, technical and otherwise, kindly provided by O&#8217;Reilly Media, Inc. </p>
<p> perltodo now lists a rough roadmap to Perl 5.10.  </p>
<h2>Performance Enhancements</h2>
<font SIZE="-1"></font><h3>XS-assisted SWASHGET</h3>
<p> Some pure-perl code that perl was using to retrieve Unicode properties and transliteration mappings has been reimplemented in <font SIZE="-1">XS</font>.  </p>
<h3>Constant subroutines</h3>
<p> The interpreter internals now support a far more memory efficient form of inlineable constants. Storing a reference to a constant value in a symbol table is equivalent to a full typeglob referencing a constant subroutine, but using about 400 bytes less memory. This proxy constant subroutine is automatically upgraded to a real typeglob with subroutine if necessary. The approach taken is analogous to the existing space optimisation for subroutine stub declarations, which are stored as plain scalars in place of the full typeglob. </p>
<p> Several of the core modules have been converted to use this feature for their system dependent constants - as a result <code>&quot;use POSIX;&quot;</code> now takes about 200K less memory.  </p>
<h3>PERL_DONT_CREATE_GVSV</h3>
<p> The new compilation flag <code>&quot;PERL_DONT_CREATE_GVSV&quot;</code>, introduced as an option in perl 5.8.8, is turned on by default in perl 5.9.3. It prevents perl from creating an empty scalar with every new typeglob. See perl589delta for details.  </p>
<h3>Weak references are cheaper</h3>
<p> Weak reference creation is now <i>O(1)</i> rather than <i>O(n)</i>, courtesy of Nicholas Clark. Weak reference deletion remains <i>O(n)</i>, but if deletion only happens at program exit, it may be skipped completely.  </p>
<i></i><h3>sort() enhancements</h3>
<p> Salvador Fandin~o provided improvements to reduce the memory usage of <code>&quot;sort&quot;</code> and to speed up some cases.  </p>
<h2>Installation and Configuration Improvements</h2>
<h3>Compilation improvements</h3>
<p> Parallel makes should work properly now, although there may still be problems if <code>&quot;make test&quot;</code> is instructed to run in parallel. </p>
<p> Building with Borland&#8217;s compilers on Win32 should work more smoothly. In particular Steve Hay has worked to side step many warnings emitted by their compilers and at least one C compiler internal error. </p>
<p> Perl extensions on Windows now can be statically built into the Perl <font SIZE="-1">DLL</font>, thanks to a work by Vadim Konovalov.  </p>
<h3>New Or Improved Platforms</h3>
<p> Perl is being ported to Symbian <font SIZE="-1">OS</font>. See perlsymbian for more information. </p>
<p> The <font SIZE="-1">VMS</font> port has been improved. See perlvms. </p>
<p> <i>DynaLoader::dl_unload_file()</i> now works on Windows. </p>
<p> Portability of Perl on various recent compilers on Windows has been improved (Borland C<font SIZE="-2">++</font>, Visual C<font SIZE="-2">++</font> 7.0).  </p>
<h3>New probes</h3>
<p> <code>&quot;Configure&quot;</code> will now detect <code>&quot;clearenv&quot;</code> and <code>&quot;unsetenv&quot;</code>, thanks to a patch from Alan Burlison. It will also probe for <code>&quot;futimes&quot;</code> (and use it internally if available), and whether <code>&quot;sprintf&quot;</code> correctly returns the length of the formatted string.  </p>
<h3>Module auxiliary files</h3>
<p> <font SIZE="-1">README</font> files and changelogs for <font SIZE="-1">CPAN</font> modules bundled with perl are no longer installed.  </p>
<h2>Selected Bug Fixes</h2>
<h3>defined $$x</h3>
<p> <code>&quot;use strict &quot;refs&quot;&quot;</code> was ignoring taking a hard reference in an argument to <i>defined()</i>, as in : </p>
<pre><code>    use strict &quot;refs&quot;;
    my $x = &quot;foo&quot;;
    if (defined $$x) {...}
</code></pre>
<p> This now correctly produces the run-time error <code>&quot;Can&#8217;t use string as a SCALAR ref while &quot;strict refs&quot; in use&quot;</code>. (However, <code>&quot;defined @$foo&quot;</code> and <code>&quot;defined %$foo&quot;</code> are still allowed. Those constructs are discouraged anyway.)  </p>
<i></i><h3>Calling CORE::require()</h3>
<p> <i>CORE::require()</i> and <i>CORE::do()</i> were always parsed as <i>require()</i> and <i>do()</i> when they were overridden. This is now fixed.  </p>
<h3>Subscripts of slices</h3>
<p> You can now use a non-arrowed form for chained subscripts after a list slice, like in: </p>
<pre><code>    ({foo =&gt; &quot;bar&quot;})[0]{foo}
</code></pre>
<p> This used to be a syntax error; a <code>&quot;-&gt;&quot;</code> was required.  </p>
<h3>Remove over-optimisation</h3>
<p> Perl 5.9.2 introduced a change so that assignments of <code>&quot;undef&quot;</code> to a scalar, or of an empty list to an array or a hash, were optimised out. As this could cause problems when <code>&quot;goto&quot;</code> jumps were involved, this change was backed out.  </p>
<i></i><h3>sprintf() fixes</h3>
<p> Using the <i>sprintf()</i> function with some formats could lead to a buffer overflow in some specific cases. This has been fixed, along with several other bugs, notably in bounds checking. </p>
<p> In related fixes, it was possible for badly written code that did not follow the documentation of <code>&quot;Sys::Syslog&quot;</code> to have formatting vulnerabilities. <code>&quot;Sys::Syslog&quot;</code> has been changed to protect people from poor quality third party code.  </p>
<h3>no warnings 'category' works correctly with -w</h3>
<p> Previously when running with warnings enabled globally via <code>&quot;-w&quot;</code>, selective disabling of specific warning categories would actually turn off all warnings. This is now fixed; now <code>&quot;no warnings &#8216;io&#8217;;&quot;</code> will only turn off warnings in the <code>&quot;io&quot;</code> class. Previously it would erroneously turn off all warnings.  </p>
<h3>Smaller fixes</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;FindBin&quot;</code> now works better with directories where access rights are more restrictive than usual. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several memory leaks in ithreads were closed. Also, ithreads were made less memory-intensive. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Trailing spaces are now trimmed from <code>$!</code> and <code>$^E</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Operations that require perl to read a process&#8217;s list of groups, such as reads of <code>$(</code> and <code>$)</code>, now dynamically allocate memory rather than using a fixed sized array. The fixed size array could cause C stack exhaustion on systems configured to use large numbers of groups. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PerlIO::scalar&quot;</code> now works better with non-default <code>$/</code> settings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;x&quot;</code> repetition operator is now able to operate on <code>&quot;qw//&quot;</code> lists. This used to raise a syntax error. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The debugger now traces correctly execution in eval(&quot;&quot;)uated code that contains #line directives. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The value of the <code>&quot;open&quot;</code> pragma is no longer ignored for three-argument opens. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl will now use the C library calls <code>&quot;unsetenv&quot;</code> and <code>&quot;clearenv&quot;</code> if present to delete keys from <code>%ENV</code> and delete <code>%ENV</code> entirely, thanks to a patch from Alan Burlison. </p>
 </dd></dl>
<h3>More Unicode Fixes</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <i>chr()</i> on a negative value now gives <code>&quot;\x{FFFD}&quot;</code>, the Unicode replacement character, unless when the <code>&quot;bytes&quot;</code> pragma is in effect, where the low eight bytes of the value are used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some case insensitive matches between <font SIZE="-1">UTF-8</font> encoded data and 8 bit regexps, and vice versa, could give malformed character warnings. These have been fixed by Dave Mitchell and Yves Orton. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;lcfirst&quot;</code> and <code>&quot;ucfirst&quot;</code> could corrupt the string for certain cases where the length <font SIZE="-1">UTF-8</font> encoding of the string in lower case, upper case or title case differed. This was fixed by Nicholas Clark. </p>
 </dd></dl>
<h2>New or Changed Diagnostics</h2>
<h3>Attempt to set length of freed array</h3>
<p> This is a new warning, produced in situations like the following one: </p>
<pre><code>    $r = do {my @a; \$#a};
    $$r = 503;
</code></pre>
<h3>Non-string passed as bitmask</h3>
<p> This is a new warning, produced when number has been passed as a argument to <i>select()</i>, instead of a bitmask. </p>
<pre><code>    # Wrong, will now warn
    $rin = fileno(STDIN);
    ($nfound,$timeleft) = select($rout=$rin, undef, undef, $timeout);
    # Should be
    $rin = '';
    vec($rin,fileno(STDIN),1) = 1;
    ($nfound,$timeleft) = select($rout=$rin, undef, undef, $timeout);
</code></pre>
<h3>Search pattern not terminated or ternary operator parsed as search pattern</h3>
<p> This syntax error indicates that the lexer couldn&#8217;t find the final delimiter of a <code>&quot;?PATTERN?&quot;</code> construct. Mentioning the ternary operator in this error message makes syntax diagnostic easier.  </p>
<h3>%s variable %s masks earlier declaration</h3>
<p> This warning is now emitted in more consistent cases; in short, when one of the declarations involved is a <code>&quot;my&quot;</code> variable: </p>
<pre><code>    my $x; my $x; # warns
    my $x; our $x; # warns
    our $x; my $x; # warns
</code></pre>
<p> On the other hand, the following: </p>
<pre><code>    our $x; our $x;
</code></pre>
<p> now gives a <code>&quot;&quot;our&quot; variable %s redeclared&quot;</code> warning.  </p>
<i></i><i></i><h3>readdir() / closedir() /etc. attempted on invalid dirhandle</h3>
<p> These new warnings are now emitted when a dirhandle is used but is either closed or not really a dirhandle.  </p>
<h2>Changed Internals</h2>
<p> In general, the source code of perl has been refactored, tied up, and optimized in many places. Also, memory management and allocation has been improved in a couple of points. </p>
<p> Andy Lester supplied many improvements to determine which function parameters and local variables could actually be declared <code>&quot;const&quot;</code> to the C compiler. Steve Peters provided new <code>*_set</code> macros and reworked the core to use these rather than assigning to macros in <font SIZE="-1">LVALUE</font> context. </p>
<p> Dave Mitchell improved the lexer debugging output under <code>&quot;-DT&quot;</code>. </p>
<p> A new file, <i>mathoms.c</i>, has been added. It contains functions that are no longer used in the perl core, but that remain available for binary or source compatibility reasons. However, those functions will not be compiled in if you add <code>&quot;-DNO_MATHOMS&quot;</code> in the compiler flags. </p>
<p> The <code>&quot;AvFLAGS&quot;</code> macro has been removed. </p>
<p> The <code>&quot;av_*()&quot;</code> functions, used to manipulate arrays, no longer accept null <code>&quot;AV*&quot;</code> parameters.  </p>
<h3>B:: modules inheritance changed</h3>
<p> The inheritance hierarchy of <code>&quot;B::&quot;</code> modules has changed; <code>&quot;B::NV&quot;</code> now inherits from <code>&quot;B::SV&quot;</code> (it used to inherit from <code>&quot;B::IV&quot;</code>).  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
