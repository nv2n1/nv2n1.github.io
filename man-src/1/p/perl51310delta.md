---
title: "perl51310delta(1)"
name: "perl51310delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl51310delta/"
description: "perl51310delta – what is new for perl v5.13.10"
---

<h2 class="name">NAME</h2>
<p> perl51310delta &#8211; what is new for perl v5.13.10 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.13.9 release and the 5.13.10 release. </p>
<p> If you are upgrading from an earlier release such as 5.13.8, first read perl5139delta, which describes differences between 5.13.8 and 5.13.9.</p>
<h2>Core Enhancements</h2>
<h3>The new regular expression modifiers available in suffix form</h3>
<p> Various releases of the 5.13.x series have added new regular expression modifiers, <tt>&quot;/a&quot;</tt>, <tt>&quot;/d&quot;</tt>, <tt>&quot;/l&quot;</tt>, and <tt>&quot;/u&quot;</tt>. They were only available in infix form (e.g., <tt>&quot;(?a:...)&quot;</tt>) until this release; now they are usable in suffix form. This change was made too late to change all the affected documentation, so there are a number of places that erroneously say these must be used in infix form. </p>
<p> However, there is an ambiguity with the construct, <tt>&quot;s/foo/bar/le...&quot;</tt>. Due to backward compatibility constraints, in Perl 5.14 only, it will be resolved as <tt>&quot;s/foo/bar/ le...&quot;</tt>, that is, as meaning to take the result of the substitution, and see if it is stringwise less-than-or-equal-to what follows. In Perl 5.16 and later, it will instead be resolved as meaning to do the pattern match using the rules of the current locale, and evaluate the rhs as an expression when doing the substitution. In 5.14, if you want the latter interpretation, you can write &#8220;el&#8221; instead.</p>
<h3>Add \p{Titlecase} as a synonym for \p{Title}</h3>
<p> This synonym is added for symmetry with the Unicode property names <tt>&quot;\p{Uppercase}&quot;</tt> and <tt>&quot;\p{Lowercase}&quot;</tt>.</p>
<h3>New regular expression modifier option /aa</h3>
<p> Doubling the <tt>&quot;/a&quot;</tt> regular expression modifier increases its effect, so that in case-insensitive matching, no <font SIZE="-1">ASCII</font> character will match a non-ASCII character. For example, normally, </p>
<pre>
    'k' =~ /\N{KELVIN SIGN}/i
</pre>
<p> will match; it won&#8217;t under <tt>&quot;/aa&quot;</tt>.</p>
<h3>New warnings categories for problematic (non-)Unicode code points.</h3>
<p> Three new warnings subcategories of &lt;utf8&gt; have been added. These allow you to turn off warnings for their covered events, while allowing the other <font SIZE="-1">UTF-8</font> warnings to remain on. The three categories are: <tt>&quot;surrogate&quot;</tt> when <font SIZE="-1">UTF-16</font> surrogates are encountered; <tt>&quot;nonchar&quot;</tt> when Unicode non-character code points are encountered; and <tt>&quot;non_unicode&quot;</tt> when code points that are above the legal Unicode maximum of 0x10FFFF are encountered.</p>
<h2>Incompatible Changes</h2>
<h3>Most \p{} properties are now immune from case-insensitive matching</h3>
<p> For most Unicode properties, it doesn&#8217;t make sense to have them match differently under <tt>&quot;/i&quot;</tt> case-insensitive matching than not. And doing so leads to unexpected results and potential security holes. For example </p>
<pre>
 m/\p{ASCII_Hex_Digit}+/i
</pre>
<p> could previously match non-ASCII characters because of the Unicode matching rules. There were a number of bugs in this feature until an earlier release in the 5.13 series. Now this release reverts, and removes the feature completely except for the few properties where people have come to expect it, namely the ones where casing is an integral part of their functionality, such as <tt>&quot;m/\p{Uppercase}/i&quot;</tt> and <tt>&quot;m/\p{Lowercase}/i&quot;</tt>, both of which match the exact same code points, namely those matched by <tt>&quot;m/\p{Cased}/i&quot;</tt>. Details are in &#8220;Unicode Properties&#8221; in perlrecharclass. </p>
<p> User-defined property handlers that need to match differently under <tt>&quot;/i&quot;</tt> must change to read the new boolean parameter passed it which is non-zero if case-insensitive matching is in effect; 0 if not. See &#8220;User-Defined Character Properties&#8221; in perluniprops.</p>
<h3>regex: \p{} in pattern implies Unicode semantics</h3>
<p> Now, a Unicode property match specified in the pattern will indicate that the pattern is meant for matching according to Unicode rules (e40e74f)</p>
<h3>add <i>GvCV_set()</i> and <i>GvGP_set()</i> macros and change <i>GvGP()</i></h3>
<p> This allows a future commit to eliminate some backref magic between <font SIZE="-1">GV</font> and CVs, which will require complete control over assignment to the gp_cv slot. </p>
<p> If you&#8217;ve been using <i>GvGP()</i> in lvalue context this change will break your code, you should use <i>GvGP_set()</i> instead. (c43ae56)</p>
<h3>_swash_inversion_hash is no longer exported as part of the <font SIZE="-1">API</font></h3>
<p> This function shouldn&#8217;t be called from <font SIZE="-1">XS</font> code. (4c2e113)</p>
<h3>Unreferenced objects in global destruction</h3>
<p> The fix for [perl #36347], which made sure that destructors were called on unreferenced objects, broke the tests for three <font SIZE="-1">CPAN</font> modules, which apparently rely on the bug. </p>
<p> To provide more time for fixing them (as this is such a minor bug), we have reverted the fix until after perl 5.14.0. </p>
<p> This resolves [perl #82542] and other related tickets.</p>
<h3>close on shared pipes</h3>
<p> The <tt>&quot;close&quot;</tt> function no longer waits for the child process to exit if the underlying file descriptor is still in use by another thread, to avoid deadlocks. It returns true in such cases.</p>
<h2>Deprecations</h2>
<dl>
<dt>Deprecated Modules</p>
<dd> The following modules will be removed from the core distribution in a future release, and should be installed from <font SIZE="-1">CPAN</font> instead. Distributions on <font SIZE="-1">CPAN</font> which require these should add them to their prerequisites. The core versions of these modules warnings will issue a deprecation warning. </p>
<p> If you ship a packaged version of Perl, either alone or as part of a larger system, then you should carefully consider the repercussions of core module deprecations. You may want to consider shipping your default build of Perl with packages for some or all deprecated modules which install into <tt>&quot;vendor&quot;</tt> or <tt>&quot;site&quot;</tt> perl library directories. This will inhibit the deprecation warnings. </p>
<p> Alternatively, you may want to consider patching <i>lib/deprecate.pm</i> to provide deprecation warnings specific to your packaging system or distribution of Perl, consistent with how your packaging system or distribution manages a staged transition from a release where the installation of a single package provides the given functionality, to a later release where the system administrator needs to know to install multiple packages to get that same functionality. </p>
<p> You can silence these deprecation warnings by installing the modules in question from <font SIZE="-1">CPAN</font>. To install the latest version of all of them, just install <tt>&quot;Task::Deprecations::5_14&quot;</tt>.</p>
<dl>
<dt>
<dd>
<dl>
<dt>Devel::DProf</p>
<dd> We strongly recommend that you install and used Devel::NYTProf in preference, as it offers significantly improved profiling and reporting.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>User-defined case-mapping</h3>
<p> This feature is being deprecated due to its many issues, as documented in &#8220;User-Defined Case Mappings (for serious hackers only)&#8221; in perlunicode. It is planned to remove this feature in Perl 5.16. A <font SIZE="-1">CPAN</font> module providing improved functionality is being prepared for release by the time 5.14 is.</p>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;CPAN::Meta&quot;</tt> version 2.110440 has been added as a dual-life module. It provides a standard library to read, interpret and write <font SIZE="-1">CPAN</font> distribution metadata files (e.g. <font SIZE="-1">META</font>.json and <font SIZE="-1">META</font>.yml) which describes a distribution, its contents, and the requirements for building it and installing it. The latest <font SIZE="-1">CPAN</font> distribution metadata specification is included as <tt>&quot;CPAN::Meta::Spec&quot;</tt> and notes on changes in the specification over time are given in <tt>&quot;CPAN::Meta::History&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Version::Requirements&quot;</tt> version 0.101020 has been added as a dual-life module. It provides a standard library to model and manipulates module prerequisites and version constraints as defined in the CPAN::Meta::Spec.</dl>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;B&quot;</tt> has been upgraded from version 1.27 to 1.28.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Carp&quot;</tt> has been upgraded from version 1.19 to 1.20. </p>
<p> [perl #82854] It now avoids using regular expressions that cause perl to load its Unicode tables, in order to avoid the &#8216;<font SIZE="-1">BEGIN</font> not safe after errors&#8217; error that will ensue if there has been a syntax error.</p>
<dt>&bull;</p>
<dd> <tt>&quot;CGI&quot;</tt> has been upgraded from version 3.51 to 3.52</p>
<dt>&bull;</p>
<dd> <tt>&quot;CPAN&quot;</tt> has been upgraded from version 1.94_64 to 1.94_65 </p>
<p> Includes support for <font SIZE="-1">META</font>.json and <font SIZE="-1">MYMETA</font>.json.</p>
<dt>&bull;</p>
<dd> <tt>&quot;CPANPLUS&quot;</tt> has been upgraded from version 0.9011 to 0.9101 </p>
<p> Includes support for <font SIZE="-1">META</font>.json and <font SIZE="-1">MYMETA</font>.json and a change to using Digest::SHA for <font SIZE="-1">CPAN</font> checksums.</p>
<dt>&bull;</p>
<dd> <tt>&quot;deprecate&quot;</tt> has been upgraded from version 0.01 to 0.02.</p>
<dt>&bull;</p>
<dd> <tt>&quot;diagnostics&quot;</tt> has been upgraded from version 1.21 to 1.22. </p>
<p> It now renders pod links slightly better, and has been taught to find descriptions for messages that share their descriptions with other messages.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Devel::DProf&quot;</tt> has been upgraded from version 20080331.00 to 20110217.00. </p>
<p> Merely loading <tt>&quot;Devel::DProf&quot;</tt> now no longer triggers profiling to start. <tt>&quot;use Devel::DProf&quot;</tt> and <tt>&quot;perl -d:DProf ...&quot;</tt> still behave as before and start the profiler. </p>
<p> <font SIZE="-1">NOTE:</font> <tt>&quot;Devel::DProf&quot;</tt> is deprecated and will be removed from a future version of Perl. We strongly recommend that you install and use Devel::NYTProf instead, as it offers significantly improved profiling and reporting.</p>
<dt>&bull;</p>
<dd> <tt>&quot;DynaLoader&quot;</tt> has been upgraded from version 1.12 to 1.13. </p>
<p> [perl #84358] It no longer inherits from AutoLoader; hence it no longer produces weird error messages for unsuccessful method calls on classes that inherit from DynaLoader.</p>
<dt>&bull;</p>
<dd> <tt>&quot;IO::Select&quot;</tt> has been upgraded from version 1.17 to 1.18. </p>
<p> It now allows IO::Handle objects (and objects in derived classes) to be removed from an IO::Select set even if the underlying file descriptor is closed or invalid.</p>
<dt>&bull;</p>
<dd> <tt>&quot;IPC::Cmd&quot;</tt> has been upgraded from version 0.68 to 0.70</p>
<dt>&bull;</p>
<dd> <tt>&quot;HTTP::Tiny&quot;</tt> has been upgraded from version 0.009 to 0.010</p>
<dt>&bull;</p>
<dd> <tt>&quot;Math::BigInt&quot;</tt> has been upgraded from version 1.99_04 to 1.992.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Module::Build&quot;</tt> has been upgraded from version 0.3607 to 0.37_05. </p>
<p> A notable change is the deprecation of several modules. Module::Build::Version has been deprecated and Module::Build now relies directly upon version. Module::Build::ModuleInfo has been deprecated in favor of a standalone copy of it called Module::Metadata. Module::Build::YAML has been deprecated in favor of CPAN::Meta::YAML. </p>
<p> Module::Build now also generates <font SIZE="-1">META</font>.json and <font SIZE="-1">MYMETA</font>.json files in accordance with version 2 of the <font SIZE="-1">CPAN</font> distribution metadata specification, CPAN::Meta::Spec. The older format <font SIZE="-1">META</font>.yml and <font SIZE="-1">MYMETA</font>.yml files are still generated, as well.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Module::Load::Conditional&quot;</tt> has been upgraded from version 0.40 to 0.44</p>
<dt>&bull;</p>
<dd> <tt>&quot;Module::Metadata&quot;</tt> has been upgraded from version 1.000003 to 1.000004.</p>
<dt>&bull;</p>
<dd> <tt>&quot;overload&quot;</tt> has been upgraded from version 1.12 to 1.13. </p>
<p> The documentation has greatly improved. See &#8220;Documentation&#8221; below.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Parse::CPAN::Meta&quot;</tt> has been upgraded from version 1.40 to 1.4401. </p>
<p> The latest Parse::CPAN::Meta can now read <font SIZE="-1">YAML</font> or <font SIZE="-1">JSON</font> files using CPAN::Meta::YAML and <font SIZE="-1">JSON::PP</font>, which are now part of the Perl core.</p>
<dt>&bull;</p>
<dd> <tt>&quot;re&quot;</tt> has been upgraded from version 0.16 to 0.17. </p>
<p> It now supports the double-a flag: <tt>&quot;use re '/aa';&quot;</tt> </p>
<p> The <tt>&quot;regmust&quot;</tt> function used to crash when called on a regular expression belonging to a pluggable engine. Now it has been disabled for those. </p>
<p> <tt>&quot;regmust&quot;</tt> no longer leaks memory.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Term::UI&quot;</tt> has been upgraded from version 0.24 to 0.26</p>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::Collate&quot;</tt> has been upgraded from version 0.68 to 0.72 </p>
<p> This also sees the switch from using the pure-perl version of this module to the <font SIZE="-1">XS</font> version.`</p>
<dt>&bull;</p>
<dd> <tt>&quot;VMS::DCLsym&quot;</tt> has been upgraded from version 1.04 to 1.05. </p>
<p> Two bugs have been fixed [perl #84086]: </p>
<p> The symbol table name was lost when tying a hash, due to a thinko in <tt>&quot;TIEHASH&quot;</tt>. The result was that all tied hashes interacted with the local symbol table. </p>
<p> Unless a symbol table name had been explicitly specified in the call to the constructor, querying the special key &#8216;:LOCAL&#8217; failed to identify objects connected to the local symbol table.</p>
<dt>&bull;</p>
<dd> Added new function <tt>&quot;Unicode::UCD::num()&quot;</tt>. This function will return the numeric value of the string passed it; <tt>&quot;undef&quot;</tt> if the string in its entirety has no safe numeric value. </p>
<p> To be safe, a string must be a single character which has a numeric value, or consist entirely of characters that match \d, coming from the same Unicode block of digits. Thus, a mix of Bengali and Western digits would be considered unsafe, as well as a mix of half- and full-width digits, but strings consisting entirely of Devanagari digits or of &#8220;Mathematical Bold&#8221; digits would would be safe.</p>
<dt>&bull;</p>
<dd> <tt>&quot;CPAN&quot;</tt> has been upgraded from version 1.94_63 to 1.94_64.</dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>overload</i></p>
<dl>
<dt>&bull;</p>
<dd> overload&#8217;s documentation has practically undergone a rewrite. It is now much more straightforward and clear.</dl>
<p> <i>perlhack and perlrepository</i></p>
<dl>
<dt>&bull;</p>
<dd> The perlhack and perlrepository documents have been heavily edited and split up into several new documents. </p>
<p> The perlhack document is now much shorter, and focuses on the Perl 5 development process and submitting patches to Perl. The technical content has been moved to several new documents, perlsource, perlinterp, perlhacktut, and perlhacktips. This technical content has only been lightly edited. </p>
<p> The perlrepository document has been renamed to perlgit. This new document is just a how-to on using git with the Perl source code. Any other content that used to be in perlrepository has been moved to perlhack.</dl>
<p> <i>perlfunc</i></p>
<dl>
<dt>&bull;</p>
<dd> The documentation for the <tt>&quot;map&quot;</tt> function now contains more examples, see <code>perldoc -f map</code> (f947627)</dl>
<p> <i>perlfaq4</i></p>
<dl>
<dt>&bull;</p>
<dd> Examples in perlfaq4 have been updated to show the use of Time::Piece. (9243591)</dl>
<p> <i>Miscellaneous</i></p>
<dl>
<dt>&bull;</p>
<dd> Many <font SIZE="-1">POD</font> related <font SIZE="-1">RT</font> bugs and other issues which are too numerous to enumerate have been solved by Michael Stevens.</dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.</p>
<h3>New Diagnostics</h3>
<dl>
<dt>&quot;{&quot; is deprecated; use &quot;\{&quot; instead</p>
<dd>
<dt>&quot;\B{&quot; is deprecated; use &quot;\B\{&quot; instead</p>
<dd> Use of an unescaped &#8220;{&#8221; immediately following a <tt>&quot;&quot;</tt> or <tt>&quot;\B&quot;</tt> is now deprecated so as to reserve its use for Perl itself in a future release.</p>
<dt>regcomp: Add warning if \p is used under locale. (fb2e24c)</p>
<dd> <tt>&quot;\p&quot;</tt> implies Unicode matching rules, which are likely going to be different than the locale&#8217;s.</p>
<dt>panic: gp_free failed to free glob pointer &#8211; something is repeatedly re-creating entries</p>
<dd> This new error is triggered if a destructor called on an object in a typeglob that is being freed creates a new typeglob entry containing an object with a destructor that creates a new entry containing an object&#8230;.</p>
<dt>refcnt: fd %d%s</p>
<dd> This new error only occurs if a internal consistency check fails when a pipe is about to be closed.</dl>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</p>
<dd> The warning message about regex unrecognized escapes passed through is changed to include any literal &#8216;{&#8216; following the 2-char escape. e.g., &#8220;\q{&#8221; will include the { in the message as part of the escape (216bfc0).</p>
<dt>&bull;</p>
<dd> <tt>&quot;binmode $fh, ':scalar'&quot;</tt> no longer warns (8250589) </p>
<p> Perl will now no longer produce this warning: </p>
<pre>
    $ perl -we 'open my $f, &quot;&gt;&quot;, \my $x; binmode $f, &quot;scalar&quot;'
    Use of uninitialized value in binmode at -e line 1.
</pre>
</dl>
<h2>Utility Changes</h2>
<p> <i>perlbug</i></p>
<dl>
<dt>&bull;</p>
<dd> [perl #82996] Use the user&#8217;s from address as return-path in perlbug </p>
<p> Many systems these days don&#8217;t have a valid Internet domain name and perlbug [at] perl.org does not accept email with a return-path that does not resolve. Therefore pass the user&#8217;s address to sendmail so it&#8217;s less likely to get stuck in a mail queue somewhere. (019cfd2)</dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</p>
<dd> make reg_eval_scope.t TODOs consistently fail (daaf7ac) </p>
<p> Some of the <font SIZE="-1">TODO</font> tests in reg_eval_scope.t spuriously passed under non-threaded builds. Make the tests harder so they always fail. </p>
<p> Since one of the key bugs in (?{..}) is the trashing of the parent pad, add some extra lexical vars to the parent scope and check they&#8217;re still there at the end.</p>
<dt>&bull;</p>
<dd> Stop EU::CBuilder&#8217;s tests from failing in parallel (cbf59d5) </p>
<p> It used to use the same paths for temporary files in all tests. This blew up randomly when the tests were run in parallel.</dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</p>
<dd> <i>porting/FindExt.t</i> now skips all tests on a static (-Uusedl) build of perl.</p>
<dt>&bull;</p>
<dd> <i>porting/FindExt.t</i> now passes on non-Win32 platforms when some extensions are built statically.</dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>Windows</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The <tt>&quot;test-prep&quot;</tt> build target now depends on <i>pod/perltoc.pod</i> to allow the <i>t/porting/buildtoc.t</i> test to run successfully.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>MirBSD</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> [perl #82988] Skip hanging taint.t test on MirBSD 10 (1fb83d0) </p>
<p> Skip a hanging test under MirBSD that was already being skipped under OpenBSD.</p>
<dt>&bull;</p>
<dd> Previously if you build perl with a shared libperl.so on MirBSD (the default config), it will work up to the installation; however, once installed, it will be unable to find libperl. Treat path handling like in the other <font SIZE="-1">BSD</font> dialects.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</p>
<dd> Fix harmless invalid read in <i>Perl_re_compile()</i> (f6d9469) </p>
<p> [perl #2460] described a case where electric fence reported an invalid read. This could be reproduced under valgrind with blead and -e&#8217;/x/&#8217;, but only on a non-debugging build. </p>
<p> This was because it was checking for certain pairs of nodes (e.g. <font SIZE="-1">BOL</font> + <font SIZE="-1">END</font>) and wasn&#8217;t allowing for <font SIZE="-1">EXACT</font> nodes, which have the string at the next node position when using a naive <font SIZE="-1">NEXTOPER</font>(first). In the non-debugging build, the nodes aren&#8217;t initialised to zero, and a 1-char <font SIZE="-1">EXACT</font> node isn&#8217;t long enough to spill into the type field of the &#8220;next node&#8221;. </p>
<p> Fix this by only using <font SIZE="-1">NEXTOPER</font>(first) when we know the first node is kosher.</p>
<dt>&bull;</p>
<dd> Break out the generated function <i>Perl_keywords()</i> into <i>keywords.c</i>, a new file. (26ea9e1) </p>
<p> As it and <i>Perl_yylex()</i> both need <font SIZE="-1">FEATURE_IS_ENABLED</font>, <i>feature_is_enabled()</i> is no longer static, and the two macro definitions move from toke.c to perl.h </p>
<p> Previously, one had to cut and paste the output of perl_keywords.pl into the middle of toke.c, and it was not clear that it was generated code.</p>
<dt>&bull;</p>
<dd> A lot of tests have been ported from Test to Test::More, e.g. in 3842ad6.</p>
<dt>&bull;</p>
<dd> Increase default PerlIO buffer size. (b83080d) </p>
<p> The previous default size of a PerlIO buffer (4096 bytes) has been increased to the larger of 8192 bytes and your local <font SIZE="-1">BUFSIZ</font>. Benchmarks show that doubling this decade-old default increases read and write performance in the neighborhood of 25% to 50% when using the default layers of perlio on top of unix. To choose a non-default size, such as to get back the old value or to obtain and even larger value, configure with: </p>
<pre>
     ./Configure -Accflags=-DPERLIOBUF_DEFAULT_BUFSIZ=N
</pre>
<p> where N is the desired size in bytes; it should probably be a multiple of your page size.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> A Unicode <tt>&quot;\p{}&quot;</tt> property match in a regular expression pattern will now force Unicode rules for the rest of the regular expression</p>
<dt>&bull;</p>
<dd> [perl #38456] binmode <font SIZE="-1">FH</font>, &#8220;:crlf&#8221; only modifies top crlf layer (7826b36) </p>
<p> When pushed on top of the stack, crlf will no longer enable crlf layers lower in the stack. This will prevent unexpected results.</p>
<dt>&bull;</p>
<dd> Fix &#8216;raw&#8217; layer for <font SIZE="-1">RT</font> #80764 (ecfd064) </p>
<p> Made a &#8216;:raw&#8217; open do what it advertises to do (first open the file, then binmode it), instead of leaving off the top layer.</p>
<dt>&bull;</p>
<dd> Use PerlIOBase_open for pop, utf8 and bytes layers (c0888ac) </p>
<p> Three of Perl&#8217;s builtin PerlIO layers (<tt>&quot;:pop&quot;</tt>, <tt>&quot;:utf8&quot;</tt> and <tt>&quot;:bytes&quot;</tt>) didn&#8217;t allow stacking when opening a file. For example this: </p>
<pre>
    open FH, '&gt;:pop:perlio', 'some.file' or die $!;
</pre>
<p> Would throw an error: &#8220;Invalid argument&#8221;. This has been fixed in this release.</p>
<dt>&bull;</p>
<dd> An issue present since 5.13.1, where s/A/B/ with A utf8 and B non-utf8, could cause corruption or segfaults has been fixed. (c95ca9b)</p>
<dt>&bull;</p>
<dd> String evals will no longer fail after 2 billion scopes have been compiled (d1bfb64, 2df5bdd, 0d311cd and 6012dc8)</p>
<dt>&bull;</p>
<dd> [perl #81750] When strict &#8216;refs&#8217; mode is off, <tt>&quot;%{...}&quot;</tt> in rvalue context returns <tt>&quot;undef&quot;</tt> if its argument is undefined. An optimisation introduced in perl 5.12.0 to make <tt>&quot;keys %{...}&quot;</tt> faster when used as a boolean did not take this into account, causing <tt>&quot;keys %{+undef}&quot;</tt> (and <tt>&quot;keys %$foo&quot;</tt> when <tt>$foo</tt> is undefined) to be an error, which it should only be in strict mode.</p>
<dt>&bull;</p>
<dd> [perl #83194] Combining the vector (%v) flag and dynamic precision would cause sprintf to confuse the order of its arguments, making it treat the string as the precision and vice versa.</p>
<dt>&bull;</p>
<dd> [perl #77692] Sometimes the <font SIZE="-1">UTF8</font> length cache would not be reset on a value returned by substr, causing <tt>&quot;length(substr($uni_string,...))&quot;</tt> to give wrong answers. With <tt>&quot;${^UTF8CACHE}&quot;</tt> set to -1, it would produce a &#8216;panic&#8217; error message, too.</p>
<dt>&bull;</p>
<dd> During the restoration of a localised typeglob on scope exit, any destructors called as a result would be able to see the typeglob in an inconsistent state, containing freed entries, which could result in a crash. This would affect code like this: </p>
<pre><code>
local *@;
eval{die bless[]};
#puts an object in $ @sub DESTROY
{
    local $ @;
#boom
}
</code></pre>
<p> Now the glob entries are cleared before any destructors are called. This also means that destructors can vivify entries in the glob. So perl tries again and, if the entries are re-created too many times, dies with a &#8216;panic: gp_free&#8230;&#8217; error message.</p>
<dt>&bull;</p>
<dd> [perl #78494] When pipes are shared between threads, the <tt>&quot;close&quot;</tt> function (and any implicit close, such as on thread exit) no longer blocks.</p>
<dt>&bull;</p>
<dd> Several contexts no longer allow a Unicode character to begin a word that should never begin words, for an example an accent that must follow another character previously could precede all other characters.</p>
<dt>&bull;</p>
<dd> Case insensitive matching in regular expressions compiled under <tt>&quot;use locale&quot;</tt> now works much more sanely when the pattern and/or target string are encoded in <font SIZE="-1">UTF-8</font>. Previously, under these conditions the localeness was completely lost. Now, code points above 255 are treated as Unicode, but code points between 0 and 255 are treated using the current locale rules, regardless of whether the pattern or string are encoded in <font SIZE="-1">UTF-8</font>. The few case insensitive matches that cross the 255/256 boundary are not allowed. For example, 0xFF does not caselessly match the character at 0x178, <font SIZE="-1">LATIN</font> <font SIZE="-1">CAPITAL</font> <font SIZE="-1">LETTER</font> Y <font SIZE="-1">WITH</font> <font SIZE="-1">DIAERESIS</font>, because 0xFF may not be <font SIZE="-1">LATIN</font> <font SIZE="-1">SMALL</font> <font SIZE="-1">LETTER</font> Y in the current locale, and Perl has no way of knowing if that character even exists in the locale, much less what code point it is.</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.13.10 represents approximately one month of development since Perl 5.13.9 and contains approximately 63000 lines of changes across 609 files from 38 authors and committers: </p>
<p> Abigail, Alexander Hartmaier, brian d foy, Charles Bailey, Chip Salzenberg, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, Curtis Jewell, Dave Rolsky, David Golden, David Leadbeater, David Mitchell, David Wheeler, Father Chrysostomos, Florian Ragwitz, Franz Fasching, George Greer, H.Merijn Brand, Hongwen Qiu, Hugo van der Sanden, Jay Hannah, Jesse Vincent, Karl Williamson, Larwan Berke, Leon Timmermans, Michael Breen, Michael Stevens, Nicholas Clark, Noirin Shirley, Paul Evans, Peter John Acklam, Ricardo Signes, Robin Barker, Steven Schubiger, Tom Christiansen, Tony Cook, Zsban Ambrus and var Arnfjo.rd<i>&#8211;</i> Bjarmason</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN</font>.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
<dt><a href="#lbAP">Deprecations</a></p>
<dd>
<dt><a href="#lbAR">Modules and Pragmata</a></p>
<dd>
<dt><a href="#lbAU">Documentation</a></p>
<dd>
<dt><a href="#lbAW">Diagnostics</a></p>
<dd>
<dt><a href="#lbAZ">Utility Changes</a></p>
<dd>
<dt><a href="#lbBA">Configuration and Compilation</a></p>
<dd>
<dt><a href="#lbBB">Testing</a></p>
<dd>
<dt><a href="#lbBC">Platform Support</a></p>
<dd>
<dt><a href="#lbBE">Internal Changes</a></p>
<dd>
<dt><a href="#lbBF">Selected Bug Fixes</a></p>
<dd>
<dt><a href="#lbBG">Acknowledgements</a></p>
<dd>
<dt><a href="#lbBH">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbBI">SEE ALSO</a></p>
<dd></dl>
