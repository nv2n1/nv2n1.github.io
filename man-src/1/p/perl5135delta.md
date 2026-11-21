---

title: "perl5135delta(1)"
name: "perl5135delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5135delta/"
description: "perl5135delta – what is new for perl v5.13.5"
---

<p> perl5135delta - what is new for perl v5.13.5 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.13.4 release and the 5.13.5 release. </p>
<p> If you are upgrading from an earlier release such as 5.13.3, first read perl5134delta, which describes differences between 5.13.3 and 5.13.4.  </p>
<h2>Core Enhancements</h2>
<h3>Adjacent pairs of nextstate opcodes are now optimized away</h3>
<p> Previously, in code such as </p>
<pre><code>    use constant DEBUG =&gt; 0;
    sub GAK {
        warn if DEBUG;
        print &quot;stuff\n&quot;;
    }
</code></pre>
<p> the ops for <code>&quot;warn if DEBUG;&quot;</code> would be folded to a <code>&quot;null&quot;</code> op (<code>&quot;ex-const&quot;</code>), but the <code>&quot;nextstate&quot;</code> op would remain, resulting in a runtime op dispatch of <code>&quot;nextstate&quot;</code>, <code>&quot;nextstate&quot;</code>, ... </p>
<p> The execution of a sequence of <code>&quot;nextstate&quot;</code> ops is indistinguishable from just the last <code>&quot;nextstate&quot;</code> op so the peephole optimizer now eliminates the first of a pair of <code>&quot;nextstate&quot;</code> ops, except where the first carries a label, since labels must not be eliminated by the optimizer and label usage isn&#8217;t conclusively known at compile time.  </p>
<font SIZE="-1"></font><h3>API function to parse statements</h3>
<p> The <code>&quot;parse_fullstmt&quot;</code> function has been added to allow parsing of a single complete Perl statement. See perlapi for details.  </p>
<font SIZE="-1"></font><h3>API functions for accessing the runtime hinthash</h3>
<p> A new C <font SIZE="-1">API</font> for introspecting the hinthash <code>&quot;%^H&quot;</code> at runtime has been added. See <code>&quot;cop_hints_2hv&quot;</code>, <code>&quot;cop_hints_fetchpvn&quot;</code>, <code>&quot;cop_hints_fetchpvs&quot;</code>, <code>&quot;cop_hints_fetchsv&quot;</code>, and <code>&quot;hv_copy_hints_hv&quot;</code> in perlapi for details.  </p>
<h3>C interface to caller()</h3>
<p> The <code>&quot;caller_cx&quot;</code> function has been added as an XSUB-writer&#8217;s equivalent of <code>&quot;caller()&quot;</code>. See perlapi for details.  </p>
<h2>Incompatible Changes</h2>
<h3>Magic variables outside the main package</h3>
<p> In previous versions of Perl, magic variables like <code>$!</code>, <code>%SIG</code>, etc. would &#8216;leak&#8217; into other packages. So <code>%foo::SIG</code> could be used to access signals, <code>&quot;${&quot;foo::!&quot;}&quot;</code> (with strict mode off) to access C&#8217;s <code>&quot;errno&quot;</code>, etc. </p>
<p> This was a bug, or an &#8216;unintentional&#8217; feature, which caused various ill effects, such as signal handlers being wiped when modules were loaded, etc. </p>
<p> This has been fixed (or the feature has been removed, depending on how you see it).  </p>
<h3>Smart-matching against array slices</h3>
<p> Previously, the following code resulted in a successful match: </p>
<pre><code>    my @a = qw(a y0 z);
    my @b = qw(a x0 z);
    @a[0 .. $#b] ~~ @b;
</code></pre>
<p> This odd behaviour has now been fixed [perl #77468] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=77468">http://rt.perl.org/rt3//Public/Bug/Display.html?id=77468</a>&gt;.  </p>
<font SIZE="-1"></font><h3>C API changes</h3>
<p> The first argument of the C <font SIZE="-1">API</font> function <code>&quot;Perl_fetch_cop_label&quot;</code> has changed from <code>&quot;struct refcounted he *&quot;</code> to <code>&quot;COP *&quot;</code>, to better insulate the user from implementation details. </p>
<p> This <font SIZE="-1">API</font> function was marked as ``may change&#8217;&#8216;, and likely isn&#8217;t in use outside the core. (Neither an unpacked <font SIZE="-1">CPAN</font>, nor Google&#8217;s codesearch, finds any other references to it.)  </p>
<h2>Deprecations</h2>
<h3>Use of qw(...) as parentheses</h3>
<p> Historically the parser fooled itself into thinking that <code>&quot;qw(...)&quot;</code> literals were always enclosed in parentheses, and as a result you could sometimes omit parentheses around them: </p>
<pre><code>    for $x qw(a b c) { ... }
</code></pre>
<p> The parser no longer lies to itself in this way. Wrap the list literal in parentheses, like: </p>
<pre><code>    for $x (qw(a b c)) { ... }
</code></pre>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Scalars containing regular expressions now only allocate the part of the <code>&quot;SV&quot;</code> body they actually use, saving some space. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compiling regular expressions has been made faster for the case where upgrading the regex to utf8 is necessary but that isn&#8217;t known when the compilation begins. </p>
 </dd></dl>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&quot;bignum&quot;</dt>
<dd> <p> Upgraded from version 0.23 to 0.25. </p>
 </dd>
<dt>&quot;blib&quot;</dt>
<dd> <p> Upgraded from version 1.05 to 1.06. </p>
 </dd>
<dt>&quot;open&quot;</dt>
<dd> <p> Upgraded from version 1.07 to 1.08. </p>
 </dd>
<dt>&quot;threads-shared&quot;</dt>
<dd> <p> Upgraded from version 1.33_02 to 1.33_03. </p>
 </dd>
<dt>&quot;warnings&quot; and &quot;warnings::register&quot;</dt>
<dd> <p> Upgraded from version 1.10 to 1.11 and from version 1.01 to 1.02 respectively. </p>
<p> It is now possible to register warning categories other than the names of packages using <code>&quot;warnings::register&quot;</code>. See perllexwarn for more information. </p>
 </dd>
<dt>&quot;B::Debug&quot;</dt>
<dd> <p> Upgraded from version 1.12 to 1.16. </p>
 </dd>
<dt>&quot;CPANPLUS::Dist::Build&quot;</dt>
<dd> <p> Upgraded from version 0.46 to 0.48. </p>
 </dd>
<dt>&quot;Data::Dumper&quot;</dt>
<dd> <p> Upgraded from version 2.126 to 2.128. </p>
<p> This fixes a crash when using custom sort functions that might cause the stack to change. </p>
 </dd>
<dt>&quot;Encode&quot;</dt>
<dd> <p> Upgraded from version 2.39 to 2.40. </p>
 </dd>
<dt>&quot;Errno&quot;</dt>
<dd> <p> Upgraded from version 1.12 to 1.13. </p>
<p> On some platforms with unusual header files, like Win32/gcc using mingw64 headers, some constants which weren&#8217;t actually error numbers have been exposed by <code>&quot;Errno&quot;</code>. This has been fixed [perl #77416] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=77416">http://rt.perl.org/rt3//Public/Bug/Display.html?id=77416</a>&gt;. </p>
 </dd>
<dt>&quot;ExtUtils::MakeMaker&quot;</dt>
<dd> <p> Upgraded from version 6.5601 to 6.57_05. </p>
 </dd>
<dt>&quot;Filter::Simple&quot;</dt>
<dd> <p> Upgraded from version 0.84 to 0.85. </p>
 </dd>
<dt>&quot;Hash::Util&quot;</dt>
<dd> <p> Upgraded from version 0.08 to 0.09. </p>
 </dd>
<dt>&quot;Math::BigInt&quot;</dt>
<dd> <p> Upgraded from version 1.89_01 to 1.95. </p>
<p> This fixes, among other things, incorrect results when computing binomial coefficients [perl #77640] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77640">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77640</a>&gt;. </p>
 </dd>
<dt>&quot;Math::BigInt::FastCalc&quot;</dt>
<dd> <p> Upgraded from version 0.19 to 0.22. </p>
 </dd>
<dt>&quot;Math::BigRat&quot;</dt>
<dd> <p> Upgraded from version 0.24 to 0.26. </p>
 </dd>
<dt>&quot;Module::CoreList&quot;</dt>
<dd> <p> Upgraded from version 2.37 to 2.38. </p>
 </dd>
<dt>&quot;PerlIO::scalar&quot;</dt>
<dd> <p> Upgraded from version 0.08 to 0.09. </p>
 </dd>
<dt>&quot;POSIX&quot;</dt>
<dd> <p> Upgraded from version 1.19 to 1.20. </p>
<p> It now includes constants for <font SIZE="-1">POSIX</font> signal constants. </p>
 </dd>
<dt>&quot;Safe&quot;</dt>
<dd> <p> Upgraded from version 2.27 to 2.28. </p>
<p> This fixes a possible infinite loop when looking for coderefs. </p>
 </dd>
<dt>&quot;Test::Simple&quot;</dt>
<dd> <p> Upgraded from version 0.96 to 0.97_01. </p>
 </dd>
<dt>&quot;Tie::Hash&quot;</dt>
<dd> <p> Upgraded from version 1.03 to 1.04. </p>
<p> Calling <code>&quot;Tie::Hash-&gt;TIEHASH()&quot;</code> used to loop forever. Now it <code>&quot;croak&quot;</code>s. </p>
 </dd>
<dt>&quot;Unicode::Collate&quot;</dt>
<dd> <p> Upgraded from version 0.56 to 0.59. </p>
 </dd>
<dt>&quot;XSLoader&quot;</dt>
<dd> <p> Upgraded from version 0.10 to 0.11. </p>
 </dd></dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlapi</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Many of the optree construction functions are now documented. </p>
 </dd></dl>
<p> <i>perlbook</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Expanded to cover many more popular books. </p>
 </dd></dl>
<p> <i>perlfaq</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> perlfaq, perlfaq2, perlfaq4, perlfaq5, perlfaq6, perlfaq8, and perlfaq9 have seen various updates and modernizations. </p>
 </dd></dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.  </p>
<h3>New Diagnostics</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Parsing code internal error (%s) </p>
<p> New fatal error produced when parsing code supplied by an extension violated the parser&#8217;s <font SIZE="-1">API</font> in a detectable way. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of qw(...) as parentheses is deprecated </p>
<p> See ``Use of qw(...) as parentheses&#8217;&#8216; for details. </p>
 </dd></dl>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;warn&quot;</code> and <code>&quot;die&quot;</code> now produce &#8216;Wide character&#8217; warnings when fed a character outside the byte range if <font SIZE="-1">STDERR</font> is a byte-sized handle. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<p> <i>h2ph</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The use of a deprecated <code>&quot;goto&quot;</code> construct has been removed [perl #74404] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=74404">http://rt.perl.org/rt3/Public/Bug/Display.html?id=74404</a>&gt;. </p>
 </dd></dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The new <i>t/lib/universal.t</i> script tests the Internal::* functions and other things in <i>universal.c</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A rare race condition in <i>t/op/while_readdir.t</i> has been fixed, stopping it from failing randomly when running tests in parallel. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The new <i>t/op/leaky-magic.t</i> script tests that magic applied to variables in the main packages does not affect other packages. </p>
 </dd></dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt><font SIZE="-1">VMS</font></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Make <code>&quot;PerlIOUnix_open&quot;</code> honour default permissions on <font SIZE="-1">VMS</font>. </p>
<p> When <code>&quot;perlio&quot;</code> became the default and <code>&quot;unixio&quot;</code> became the default bottom layer, the most common path for creating files from Perl became <code>&quot;PerlIOUnix_open&quot;</code>, which has always explicitly used <code>0666</code> as the permission mask. </p>
<p> To avoid this, <code>0777</code> is now passed as the permissions to <code>&quot;open()&quot;</code>. In the <font SIZE="-1">VMS</font> <font SIZE="-1">CRTL</font>, <code>0777</code> has a special meaning over and above intersecting with the current umask; specifically, it allows Unix syscalls to preserve native default permissions. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;CALL_FPTR&quot;</code> and <code>&quot;CPERLscope&quot;</code> have been deprecated. </p>
<p> Those are left from an old implementation of <code>&quot;MULTIPLICITY&quot;</code> using C<font SIZE="-2">++</font> objects, which was removed in Perl 5.8. Nowadays these macros do exactly nothing, so they shouldn&#8217;t be used anymore. </p>
<p> For compatibility, they are still defined for external <code>&quot;XS&quot;</code> code. Only extensions defining <code>&quot;PERL_CORE&quot;</code> must be updated now. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;lex_stuff_pvs()&quot;</code> has been added as a convenience macro wrapping <code>&quot;lex_stuff_pvn()&quot;</code> for literal strings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The recursive part of the peephole optimizer is now hookable. </p>
<p> In addition to <code>&quot;PL_peepp&quot;</code>, for hooking into the toplevel peephole optimizer, a <code>&quot;PL_rpeepp&quot;</code> is now available to hook into the optimizer recursing into side-chains of the optree. </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> A regression introduced in Perl 5.12.0, making <code>&quot;my $x = 3; $x = length(undef)&quot;</code> result in <code>$x</code> set to <code>3</code> has been fixed. <code>$x</code> will now be <code>&quot;undef&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A fatal error in regular expressions when processing <font SIZE="-1">UTF-8</font> data has been fixed [perl #75680] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=75680">http://rt.perl.org/rt3/Public/Bug/Display.html?id=75680</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An erroneous regular expression engine optimization that caused regex verbs like <code>*COMMIT</code> to sometimes be ignored has been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Perl debugger now also works in taint mode [perl #76872] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=76872">http://rt.perl.org/rt3/Public/Bug/Display.html?id=76872</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several memory leaks in cloning and freeing threaded Perl interpreters have been fixed [perl #77352] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77352">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77352</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A possible string corruption when doing regular expression matches on overloaded objects has been fixed [perl #77084] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77084">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77084</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Magic applied to variables in the main package no longer affects other packages. See ``Magic variables outside the main package&#8217;&#8216; above [perl #76138] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=76138">http://rt.perl.org/rt3/Public/Bug/Display.html?id=76138</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Opening a glob reference via <code>&quot;open $fh, &quot;&gt;&quot;, \*glob&quot;</code> will no longer cause the glob to be corrupted when the filehandle is printed to. This would cause perl to crash whenever the glob&#8217;s contents were accessed [perl #77492] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77492">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77492</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The postincrement and postdecrement operators, <code>&quot;++&quot;</code> and <code>&quot;--&quot;</code>, used to cause leaks when being used on references. This has now been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A bug when replacing the glob of a loop variable within the loop has been fixed [perl #21469] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=21469">http://rt.perl.org/rt3/Public/Bug/Display.html?id=21469</a>&gt;. This means the following code will no longer crash: </p>
<pre><code>    for $x (...) {
        *x = *y;
    }
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl would segfault if the undocumented <code>&quot;Internals&quot;</code> functions that used reference prototypes were called with the <code>&quot;&amp;foo()&quot;</code> syntax, e.g. <code>&quot;&amp;Internals::SvREADONLY(undef)&quot;</code> [perl #77776] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77776">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77776</a>&gt;. </p>
<p> These functions now call <code>&quot;SvROK&quot;</code> on their arguments before dereferencing them with <code>&quot;SvRV&quot;</code>, and we test for this case in <i>t/lib/universal.t</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When assigning a list with duplicated keys to a hash, the assignment used to return garbage and/or freed values: </p>
<pre><code>    @a = %h = (list with some duplicate keys);
</code></pre>
<p> This has now been fixed [perl #31865] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=31865">http://rt.perl.org/rt3/Public/Bug/Display.html?id=31865</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An earlier release of the 5.13 series of Perl changed the semantics of opening a reference to a copy of a glob: </p>
<pre><code>    my $var = *STDOUT;
    open my $fh, '&gt;', \$var;
</code></pre>
<p> This was a mistake, and the previous behaviour from Perl 5.10 and 5.12, which is to treat \$var as a scalar reference, has now been restored. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The regular expression bracketed character class <code>&quot;[\8\9]&quot;</code> was effectively the same as <code>&quot;[89\000]&quot;</code>, incorrectly matching a <font SIZE="-1">NULL</font> character. It also gave incorrect warnings that the <code>8</code> and <code>9</code> were ignored. Now <code>&quot;[\8\9]&quot;</code> is the same as <code>&quot;[89]&quot;</code> and gives legitimate warnings that <code>&quot;\8&quot;</code> and <code>&quot;\9&quot;</code> are unrecognized escape sequences, passed-through. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;warn()&quot;</code> and <code>&quot;die()&quot;</code> now respect utf8-encoded scalars [perl #45549] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=45549">http://rt.perl.org/rt3/Public/Bug/Display.html?id=45549</a>&gt;. </p>
 </dd></dl>
<h2>Known Problems</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The upgrade to Encode-2.40 has caused some tests in the libwww-perl distribution on <font SIZE="-1">CPAN</font> to fail. (Specifically, <i>base/message-charset.t</i> tests 33-36 in version 5.836 of that distribution now fail.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The upgrade to ExtUtils-MakeMaker-6.57_05 has caused some tests in the Module-Install distribution on <font SIZE="-1">CPAN</font> to fail. (Specifically, <i>02_mymeta.t</i> tests 5 and 21, <i>18_all_from.t</i> tests 6 and 15, <i>19_authors.t</i> tests 5, 13, 21 and 29, and <i>20_authors_with_special_characters.t</i> tests 6, 15 and 23 in version 1.00 of that distribution now fail.) </p>
 </dd></dl>
<h2>Acknowledgements</h2>
<p> Perl 5.13.5 represents approximately one month of development since Perl 5.13.4 and contains 74558 lines of changes across 549 files from 45 authors and committers: </p>
<p> Abigail, Alexander Alekseev, Aristotle Pagaltzis, Ben Morrow, Bram, brian d foy, Chas. Owens, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, Curtis Jewell, Dagfinn Ilmari Mannsa&#176;ker, David Golden, David Leadbeater, David Mitchell, Eric Brine, Father Chrysostomos, Florian Ragwitz, Gisle Aas, Jan Dubois, Jerry D. Hedden, Jesse Vincent, Jim Cromie, Jirka HruXka, Karl Williamson, Michael G. Schwern, Nicholas Clark, Paul Johnson, Philippe Bruhat (BooK), Piotr Fusik, Rafael Garcia-Suarez, Rainer Tammer, Reini Urban, Ricardo Signes, Rob Hoelz, Robin Barker, Steffen Mueller, Steve Hay, Steve Peters, Todd Rinaldo, Tony Cook, Vincent Pit, Yves Orton, Zefram, Zsban Ambrus, var Arnfjo.rd <i>-</i> Bjarmason. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN</font>.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
