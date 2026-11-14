---
title: "perl593delta(1)"
name: "perl593delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl593delta/"
description: "perl593delta – what is new for perl v5.9.3"
---

<h2 class="name">NAME</h2>
<p> perl593delta &#8211; what is new for perl v5.9.3 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.9.2 and the 5.9.3 development releases. See perl590delta, perl591delta and perl592delta for the differences between 5.8.0 and 5.9.2.</p>
<h2>Incompatible Changes</h2>
<h3>Parsing of -f _</h3>
<p> The identifier <tt>&quot;_&quot;</tt> is now forced to be a bareword after a filetest operator. This solves a number of misparsing issues when a global <tt>&quot;_&quot;</tt> subroutine is defined.</p>
<h3>mkdir()</h3>
<p> <tt>&quot;mkdir()&quot;</tt> without arguments now defaults to <tt>$_</tt>.</p>
<h3>Magic goto and eval</h3>
<p> The construct <tt>&quot;eval { goto &amp;foo }&quot;</tt> is now disallowed. (Note that the similar construct, but with <tt>&quot;eval(&quot;&quot;)&quot;</tt> instead, was already forbidden.)</p>
<h3>$# has been removed</h3>
<p> The deprecated <tt>$#</tt> variable (output format for numbers) has been removed. A new warning, <tt>&quot;$# is no longer supported&quot;</tt>, has been added.</p>
<h3>:unique</h3>
<p> The <tt>&quot;:unique&quot;</tt> attribute has been made a no-op, since its current implementation was fundamentally flawed and not threadsafe.</p>
<h3>Scoping of the sort pragma</h3>
<p> The <tt>&quot;sort&quot;</tt> pragma is now lexically scoped. Its effect used to be global.</p>
<h2>Core Enhancements</h2>
<h3>The feature pragma</h3>
<p> The <tt>&quot;feature&quot;</tt> pragma is used to enable new syntax that would break Perl&#8217;s backwards-compatibility with older releases of the language. It&#8217;s a lexical pragma, like <tt>&quot;strict&quot;</tt> or <tt>&quot;warnings&quot;</tt>. </p>
<p> Currently the following new features are available: <tt>&quot;switch&quot;</tt> (adds a switch statement), <tt>&quot;~~&quot;</tt> (adds a Perl 6-like smart match operator), <tt>&quot;say&quot;</tt> (adds a <tt>&quot;say&quot;</tt> built-in function), and <tt>&quot;err&quot;</tt> (adds an <tt>&quot;err&quot;</tt> keyword). Those features are described below. </p>
<p> Note that <tt>&quot;err&quot;</tt> low-precedence defined-or operator used to be enabled by default (although as a weak keyword, meaning that any function would override it). It&#8217;s now only recognized when explicitly turned on (and is then a regular keyword). </p>
<p> Those features, and the <tt>&quot;feature&quot;</tt> pragma itself, have been contributed by Robin Houston.</p>
<h3>Switch and Smart Match operator</h3>
<p> Perl 5 now has a switch statement. It&#8217;s available when <tt>&quot;use feature 'switch'&quot;</tt> is in effect. This feature introduces three new keywords, <tt>&quot;given&quot;</tt>, <tt>&quot;when&quot;</tt>, and <tt>&quot;default&quot;</tt>: </p>
<pre><code>
given($foo)
{
    when(/ ^abc /)
    {
        $abc = 1;
    }
    when(/ ^def /)
    {
        $def = 1;
    }
    when(/ ^xyz /)
    {
        $xyz = 1;
    }
    default
    {
        $nothing = 1;
    }
}
</code></pre>
<p> A more complete description of how Perl matches the switch variable against the <tt>&quot;when&quot;</tt> conditions is given in &#8220;Switch statements&#8221; in perlsyn. </p>
<p> This kind of match is called <i>smart match</i>, and it&#8217;s also possible to use it outside of switch statements, via the new <tt>&quot;~~&quot;</tt> operator (enabled via the <tt>&quot;use feature '~~'&quot;</tt> directive). See &#8220;Smart matching in detail&#8221; in perlsyn.</p>
<h3>say()</h3>
<p> <i>say()</i> is a new built-in, only available when <tt>&quot;use feature 'say'&quot;</tt> is in effect, that is similar to <i>print()</i>, but that implicitly appends a newline to the printed string. See &#8220;say&#8221; in perlfunc.</p>
<h3>CLONE_SKIP()</h3>
<p> Perl has now support for the <tt>&quot;CLONE_SKIP&quot;</tt> special subroutine. Like <tt>&quot;CLONE&quot;</tt>, <tt>&quot;CLONE_SKIP&quot;</tt> is called once per package; however, it is called just before cloning starts, and in the context of the parent thread. If it returns a true value, then no objects of that class will be cloned. See perlmod for details. (Contributed by Dave Mitchell.)</p>
<h3>${^CHILD_ERROR_NATIVE}</h3>
<p> A new internal variable, <tt>&quot;${^CHILD_ERROR_NATIVE}&quot;</tt>, gives the native status returned by the last pipe close, backtick command, successful call to <i>wait()</i> or <i>waitpid()</i>, or from the <i>system()</i> operator. See perlrun for details. (Contributed by Gisle Aas.)</p>
<h3>Assertions</h3>
<p> The support for assertions, introduced in perl 5.9.0, has been improved. The syntax for the <tt>&quot;-A&quot;</tt> command-line switch has changed; it now accepts an optional module name, defaulting to <tt>&quot;assertions::activate&quot;</tt>. See assertions and perlrun. (Contributed by Salvador Fandin~o Garcia.)</p>
<h3>Unicode Character Database 4.1.0</h3>
<p> The copy of the Unicode Character Database included in Perl 5.9 has been updated to 4.1.0.</p>
<h3>no VERSION</h3>
<p> You can now use <tt>&quot;no&quot;</tt> followed by a version number to specify that you want to use a version of perl older than the specified one.</p>
<h3>Recursive sort subs</h3>
<p> You can now use recursive subroutines with <i>sort()</i>, thanks to Robin Houston.</p>
<h3>Effect of pragmas in eval</h3>
<p> The compile-time value of the <tt>&quot;%^H&quot;</tt> hint variable can now propagate into eval(&quot;&quot;)uated code. This makes it more useful to implement lexical pragmas. </p>
<p> As a side-effect of this, the overloaded-ness of constants now propagates into eval(&quot;&quot;).</p>
<h3>New <code>-E</code> command-line switch</h3>
<p> <code>-E</code> is equivalent to <code>-e</code>, but it implicitly enables all optional features (like <tt>&quot;use feature &quot;:5.10&quot;&quot;</tt>).</p>
<h3>chdir, chmod and chown on filehandles</h3>
<p> <tt>&quot;chdir&quot;</tt>, <tt>&quot;chmod&quot;</tt> and <tt>&quot;chown&quot;</tt> can now work on filehandles as well as filenames, if the system supports respectively <tt>&quot;fchdir&quot;</tt>, <tt>&quot;fchmod&quot;</tt> and <tt>&quot;fchown&quot;</tt>, thanks to a patch provided by Gisle Aas.</p>
<h3><font SIZE="-1">OS</font> groups</h3>
<p> <tt>$(</tt> and <tt>$)</tt> now return groups in the order where the <font SIZE="-1">OS</font> returns them, thanks to Gisle Aas. This wasn&#8217;t previously the case.</p>
<h2>Modules and Pragmata</h2>
<h3>New Core Modules</h3>
<dl>
<dt>&bull;</p>
<dd> A new pragma, <tt>&quot;feature&quot;</tt>, has been added; see above in &#8220;Core Enhancements&#8221;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;assertions::compat&quot;</tt>, also available on <font SIZE="-1">CPAN</font>, allows the use of assertions on perl versions prior to 5.9.0 (that is the first one to natively support them).</p>
<dt>&bull;</p>
<dd> <tt>&quot;Math::BigInt::FastCalc&quot;</tt> is an XS-enabled, and thus faster, version of <tt>&quot;Math::BigInt::Calc&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Compress::Zlib&quot;</tt> is an interface to the zlib compression library. It comes with a bundled version of zlib, so having a working zlib is not a prerequisite to install it. It&#8217;s used by <tt>&quot;Archive::Tar&quot;</tt> (see below).</p>
<dt>&bull;</p>
<dd> <tt>&quot;IO::Zlib&quot;</tt> is an <tt>&quot;IO::&quot;</tt>-style interface to <tt>&quot;Compress::Zlib&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Archive::Tar&quot;</tt> is a module to manipulate <tt>&quot;tar&quot;</tt> archives.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Digest::SHA&quot;</tt> is a module used to calculate many types of <font SIZE="-1">SHA</font> digests, has been included for <font SIZE="-1">SHA</font> support in the <font SIZE="-1">CPAN</font> module.</p>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::CBuilder&quot;</tt> and <tt>&quot;ExtUtils::ParseXS&quot;</tt> have been added.</dl>
<h2>Utility Changes</h2>
<h3>ptar</h3>
<p> <tt>&quot;ptar&quot;</tt> is a pure perl implementation of <tt>&quot;tar&quot;</tt>, that comes with <tt>&quot;Archive::Tar&quot;</tt>.</p>
<h3>ptardiff</h3>
<p> <tt>&quot;ptardiff&quot;</tt> is a small script used to generate a diff between the contents of a tar archive and a directory tree. Like <tt>&quot;ptar&quot;</tt>, it comes with <tt>&quot;Archive::Tar&quot;</tt>.</p>
<h3>shasum</h3>
<p> This command-line utility, used to print or to check <font SIZE="-1">SHA</font> digests, comes with the new <tt>&quot;Digest::SHA&quot;</tt> module.</p>
<h3>h2xs enhancements</h3>
<p> <tt>&quot;h2xs&quot;</tt> implements a new option <tt>&quot;--use-xsloader&quot;</tt> to force use of <tt>&quot;XSLoader&quot;</tt> even in backwards compatible modules. </p>
<p> The handling of authors&#8217; names that had apostrophes has been fixed. </p>
<p> Any enums with negative values are now skipped.</p>
<h3>perlivp enhancements</h3>
<p> <tt>&quot;perlivp&quot;</tt> no longer checks for <i>*.ph</i> files by default. Use the new <tt>&quot;-a&quot;</tt> option to run <i>all</i> tests.</p>
<h2>Documentation</h2>
<h3>Perl Glossary</h3>
<p> The perlglossary manpage is a glossary of terms used in the Perl documentation, technical and otherwise, kindly provided by O&#8217;Reilly Media, Inc. </p>
<p> perltodo now lists a rough roadmap to Perl 5.10.</p>
<h2>Performance Enhancements</h2>
<h3>XS-assisted <font SIZE="-1">SWASHGET</font></h3>
<p> Some pure-perl code that perl was using to retrieve Unicode properties and transliteration mappings has been reimplemented in <font SIZE="-1">XS</font>.</p>
<h3>Constant subroutines</h3>
<p> The interpreter internals now support a far more memory efficient form of inlineable constants. Storing a reference to a constant value in a symbol table is equivalent to a full typeglob referencing a constant subroutine, but using about 400 bytes less memory. This proxy constant subroutine is automatically upgraded to a real typeglob with subroutine if necessary. The approach taken is analogous to the existing space optimisation for subroutine stub declarations, which are stored as plain scalars in place of the full typeglob. </p>
<p> Several of the core modules have been converted to use this feature for their system dependent constants &#8211; as a result <tt>&quot;use POSIX;&quot;</tt> now takes about 200K less memory.</p>
<h3>PERL_DONT_CREATE_GVSV</h3>
<p> The new compilation flag <tt>&quot;PERL_DONT_CREATE_GVSV&quot;</tt>, introduced as an option in perl 5.8.8, is turned on by default in perl 5.9.3. It prevents perl from creating an empty scalar with every new typeglob. See perl589delta for details.</p>
<h3>Weak references are cheaper</h3>
<p> Weak reference creation is now <i><a href="/docs/linux/man/1-o/">O</a>(1)</i> rather than <i><a href="/docs/linux/man/n-o/">O</a>(n)</i>, courtesy of Nicholas Clark. Weak reference deletion remains <i><a href="/docs/linux/man/n-o/">O</a>(n)</i>, but if deletion only happens at program exit, it may be skipped completely.</p>
<h3><i>sort()</i> enhancements</h3>
<p> Salvador Fandin~o provided improvements to reduce the memory usage of <tt>&quot;sort&quot;</tt> and to speed up some cases.</p>
<h2>Installation and Configuration Improvements</h2>
<h3>Compilation improvements</h3>
<p> Parallel makes should work properly now, although there may still be problems if <tt>&quot;make test&quot;</tt> is instructed to run in parallel. </p>
<p> Building with Borland&#8217;s compilers on Win32 should work more smoothly. In particular Steve Hay has worked to side step many warnings emitted by their compilers and at least one C compiler internal error. </p>
<p> Perl extensions on Windows now can be statically built into the Perl <font SIZE="-1">DLL</font>, thanks to a work by Vadim Konovalov.</p>
<h3>New Or Improved Platforms</h3>
<p> Perl is being ported to Symbian <font SIZE="-1">OS</font>. See perlsymbian for more information. </p>
<p> The <font SIZE="-1">VMS</font> port has been improved. See perlvms. </p>
<p> <i>DynaLoader::dl_unload_file()</i> now works on Windows. </p>
<p> Portability of Perl on various recent compilers on Windows has been improved (Borland C<font SIZE="-2">++</font>, Visual C<font SIZE="-2">++</font> 7.0).</p>
<h3>New probes</h3>
<p> <tt>&quot;Configure&quot;</tt> will now detect <tt>&quot;clearenv&quot;</tt> and <tt>&quot;unsetenv&quot;</tt>, thanks to a patch from Alan Burlison. It will also probe for <tt>&quot;futimes&quot;</tt> (and use it internally if available), and whether <tt>&quot;sprintf&quot;</tt> correctly returns the length of the formatted string.</p>
<h3>Module auxiliary files</h3>
<p> <font SIZE="-1">README</font> files and changelogs for <font SIZE="-1">CPAN</font> modules bundled with perl are no longer installed.</p>
<h2>Selected Bug Fixes</h2>
<h3>defined $$x</h3>
<p> <tt>&quot;use strict &quot;refs&quot;&quot;</tt> was ignoring taking a hard reference in an argument to <i>defined()</i>, as in : </p>
<p>use strict &#8220;refs&#8221;;<br />
my $x = &#8220;foo&#8221;;<br />
if (defined $$x) {<br />
    &#8230;<br />
}</p>
<p> This now correctly produces the run-time error <tt>&quot;Can't use string as a SCALAR ref while &quot;strict refs&quot; in use&quot;</tt>. (However, <tt>&quot;defined @$foo&quot;</tt> and <tt>&quot;defined %$foo&quot;</tt> are still allowed. Those constructs are discouraged anyway.)</p>
<h3>Calling <i>CORE::require()</i></h3>
<p> <i>CORE::require()</i> and <i>CORE::do()</i> were always parsed as <i>require()</i> and <i>do()</i> when they were overridden. This is now fixed.</p>
<h3>Subscripts of slices</h3>
<p> You can now use a non-arrowed form for chained subscripts after a list slice, like in: </p>
<p>({foo = &gt; &#8220;bar&#8221;})[0]<br />
{<br />
    foo<br />
}</p>
<p> This used to be a syntax error; a <tt>&quot;-&gt;&quot;</tt> was required.</p>
<h3>Remove over-optimisation</h3>
<p> Perl 5.9.2 introduced a change so that assignments of <tt>&quot;undef&quot;</tt> to a scalar, or of an empty list to an array or a hash, were optimised out. As this could cause problems when <tt>&quot;goto&quot;</tt> jumps were involved, this change was backed out.</p>
<h3><i>sprintf()</i> fixes</h3>
<p> Using the <i>sprintf()</i> function with some formats could lead to a buffer overflow in some specific cases. This has been fixed, along with several other bugs, notably in bounds checking. </p>
<p> In related fixes, it was possible for badly written code that did not follow the documentation of <tt>&quot;Sys::Syslog&quot;</tt> to have formatting vulnerabilities. <tt>&quot;Sys::Syslog&quot;</tt> has been changed to protect people from poor quality third party code.</p>
<h3>no warnings &#8216;category&#8217; works correctly with -w</h3>
<p> Previously when running with warnings enabled globally via <tt>&quot;-w&quot;</tt>, selective disabling of specific warning categories would actually turn off all warnings. This is now fixed; now <tt>&quot;no warnings 'io';&quot;</tt> will only turn off warnings in the <tt>&quot;io&quot;</tt> class. Previously it would erroneously turn off all warnings.</p>
<h3>Smaller fixes</h3>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;FindBin&quot;</tt> now works better with directories where access rights are more restrictive than usual.</p>
<dt>&bull;</p>
<dd> Several memory leaks in ithreads were closed. Also, ithreads were made less memory-intensive.</p>
<dt>&bull;</p>
<dd> Trailing spaces are now trimmed from <tt>$!</tt> and <tt>$^E</tt>.</p>
<dt>&bull;</p>
<dd> Operations that require perl to read a process&#8217;s list of groups, such as reads of <tt>$(</tt> and <tt>$)</tt>, now dynamically allocate memory rather than using a fixed sized array. The fixed size array could cause C stack exhaustion on systems configured to use large numbers of groups.</p>
<dt>&bull;</p>
<dd> <tt>&quot;PerlIO::scalar&quot;</tt> now works better with non-default <tt>$/</tt> settings.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;x&quot;</tt> repetition operator is now able to operate on <tt>&quot;qw//&quot;</tt> lists. This used to raise a syntax error.</p>
<dt>&bull;</p>
<dd> The debugger now traces correctly execution in eval(&quot;&quot;)uated code that contains #line directives.</p>
<dt>&bull;</p>
<dd> The value of the <tt>&quot;open&quot;</tt> pragma is no longer ignored for three-argument opens.</p>
<dt>&bull;</p>
<dd> Perl will now use the C library calls <tt>&quot;unsetenv&quot;</tt> and <tt>&quot;clearenv&quot;</tt> if present to delete keys from <tt>%ENV</tt> and delete <tt>%ENV</tt> entirely, thanks to a patch from Alan Burlison.</dl>
<h3>More Unicode Fixes</h3>
<dl>
<dt>&bull;</p>
<dd> <i>chr()</i> on a negative value now gives <tt>&quot;
