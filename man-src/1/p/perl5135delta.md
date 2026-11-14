---
title: "perl5135delta(1)"
name: "perl5135delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5135delta/"
description: "perl5135delta – what is new for perl v5.13.5"
---

<h2 class="name">NAME</h2>
<p> perl5135delta &#8211; what is new for perl v5.13.5 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.13.4 release and the 5.13.5 release. </p>
<p> If you are upgrading from an earlier release such as 5.13.3, first read perl5134delta, which describes differences between 5.13.3 and 5.13.4.</p>
<h2>Core Enhancements</h2>
<h3>Adjacent pairs of nextstate opcodes are now optimized away</h3>
<p> Previously, in code such as </p>
<pre><code>
use constant DEBUG = &gt; 0;
sub GAK
{
    warn if DEBUG;
    print "stuff
";
}
</code></pre>
<p> the ops for <tt>&quot;warn if DEBUG;&quot;</tt> would be folded to a <tt>&quot;null&quot;</tt> op (<tt>&quot;ex-const&quot;</tt>), but the <tt>&quot;nextstate&quot;</tt> op would remain, resulting in a runtime op dispatch of <tt>&quot;nextstate&quot;</tt>, <tt>&quot;nextstate&quot;</tt>, &#8230; </p>
<p> The execution of a sequence of <tt>&quot;nextstate&quot;</tt> ops is indistinguishable from just the last <tt>&quot;nextstate&quot;</tt> op so the peephole optimizer now eliminates the first of a pair of <tt>&quot;nextstate&quot;</tt> ops, except where the first carries a label, since labels must not be eliminated by the optimizer and label usage isn&#8217;t conclusively known at compile time.</p>
<h3><font SIZE="-1">API</font> function to parse statements</h3>
<p> The <tt>&quot;parse_fullstmt&quot;</tt> function has been added to allow parsing of a single complete Perl statement. See perlapi for details.</p>
<h3><font SIZE="-1">API</font> functions for accessing the runtime hinthash</h3>
<p> A new C <font SIZE="-1">API</font> for introspecting the hinthash <tt>&quot;%^H&quot;</tt> at runtime has been added. See <tt>&quot;cop_hints_2hv&quot;</tt>, <tt>&quot;cop_hints_fetchpvn&quot;</tt>, <tt>&quot;cop_hints_fetchpvs&quot;</tt>, <tt>&quot;cop_hints_fetchsv&quot;</tt>, and <tt>&quot;hv_copy_hints_hv&quot;</tt> in perlapi for details.</p>
<h3>C interface to caller()</h3>
<p> The <tt>&quot;caller_cx&quot;</tt> function has been added as an XSUB-writer&#8217;s equivalent of <tt>&quot;caller()&quot;</tt>. See perlapi for details.</p>
<h2>Incompatible Changes</h2>
<h3>Magic variables outside the main package</h3>
<p> In previous versions of Perl, magic variables like <tt>$!</tt>, <tt>%SIG</tt>, etc. would &#8216;leak&#8217; into other packages. So <tt>%foo::SIG</tt> could be used to access signals, <tt>&quot;${&quot;foo::!&quot;}&quot;</tt> (with strict mode off) to access C&#8217;s <tt>&quot;errno&quot;</tt>, etc. </p>
<p> This was a bug, or an &#8216;unintentional&#8217; feature, which caused various ill effects, such as signal handlers being wiped when modules were loaded, etc. </p>
<p> This has been fixed (or the feature has been removed, depending on how you see it).</p>
<h3>Smart-matching against array slices</h3>
<p> Previously, the following code resulted in a successful match: </p>
<p>my @a = qw(a y0 z);<br />
my @b = qw(a x0 z);<br />
@a[0..$ #b] ~~@b;</p>
<p> This odd behaviour has now been fixed [perl #77468] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=77468">http://rt.perl.org/rt3//Public/Bug/Display.html?id=77468</a>&gt;.</p>
<h3>C <font SIZE="-1">API</font> changes</h3>
<p> The first argument of the C <font SIZE="-1">API</font> function <tt>&quot;Perl_fetch_cop_label&quot;</tt> has changed from <tt>&quot;struct refcounted he *&quot;</tt> to <tt>&quot;COP *&quot;</tt>, to better insulate the user from implementation details. </p>
<p> This <font SIZE="-1">API</font> function was marked as &#8220;may change&#8221;, and likely isn&#8217;t in use outside the core. (Neither an unpacked <font SIZE="-1">CPAN</font>, nor Google&#8217;s codesearch, finds any other references to it.)</p>
<h2>Deprecations</h2>
<h3>Use of qw(&#8230;) as parentheses</h3>
<p> Historically the parser fooled itself into thinking that <tt>&quot;qw(...)&quot;</tt> literals were always enclosed in parentheses, and as a result you could sometimes omit parentheses around them: </p>
<pre>
    for $x qw(a b c) { ... }
</pre>
<p> The parser no longer lies to itself in this way. Wrap the list literal in parentheses, like: </p>
<pre>
    for $x (qw(a b c)) { ... }
</pre>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</p>
<dd> Scalars containing regular expressions now only allocate the part of the <tt>&quot;SV&quot;</tt> body they actually use, saving some space.</p>
<dt>&bull;</p>
<dd> Compiling regular expressions has been made faster for the case where upgrading the regex to utf8 is necessary but that isn&#8217;t known when the compilation begins.</dl>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&quot;bignum&quot;</p>
<dd> Upgraded from version 0.23 to 0.25.</p>
<dt>&quot;blib&quot;</p>
<dd> Upgraded from version 1.05 to 1.06.</p>
<dt>&quot;open&quot;</p>
<dd> Upgraded from version 1.07 to 1.08.</p>
<dt>&quot;threads-shared&quot;</p>
<dd> Upgraded from version 1.33_02 to 1.33_03.</p>
<dt>&quot;warnings&quot; and &quot;warnings::register&quot;</p>
<dd> Upgraded from version 1.10 to 1.11 and from version 1.01 to 1.02 respectively. </p>
<p> It is now possible to register warning categories other than the names of packages using <tt>&quot;warnings::register&quot;</tt>. See perllexwarn for more information.</p>
<dt>&quot;B::Debug&quot;</p>
<dd> Upgraded from version 1.12 to 1.16.</p>
<dt>&quot;CPANPLUS::Dist::Build&quot;</p>
<dd> Upgraded from version 0.46 to 0.48.</p>
<dt>&quot;Data::Dumper&quot;</p>
<dd> Upgraded from version 2.126 to 2.128. </p>
<p> This fixes a crash when using custom sort functions that might cause the stack to change.</p>
<dt>&quot;Encode&quot;</p>
<dd> Upgraded from version 2.39 to 2.40.</p>
<dt>&quot;Errno&quot;</p>
<dd> Upgraded from version 1.12 to 1.13. </p>
<p> On some platforms with unusual header files, like Win32/gcc using mingw64 headers, some constants which weren&#8217;t actually error numbers have been exposed by <tt>&quot;Errno&quot;</tt>. This has been fixed [perl #77416] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=77416">http://rt.perl.org/rt3//Public/Bug/Display.html?id=77416</a>&gt;.</p>
<dt>&quot;ExtUtils::MakeMaker&quot;</p>
<dd> Upgraded from version 6.5601 to 6.57_05.</p>
<dt>&quot;Filter::Simple&quot;</p>
<dd> Upgraded from version 0.84 to 0.85.</p>
<dt>&quot;Hash::Util&quot;</p>
<dd> Upgraded from version 0.08 to 0.09.</p>
<dt>&quot;Math::BigInt&quot;</p>
<dd> Upgraded from version 1.89_01 to 1.95. </p>
<p> This fixes, among other things, incorrect results when computing binomial coefficients [perl #77640] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77640">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77640</a>&gt;.</p>
<dt>&quot;Math::BigInt::FastCalc&quot;</p>
<dd> Upgraded from version 0.19 to 0.22.</p>
<dt>&quot;Math::BigRat&quot;</p>
<dd> Upgraded from version 0.24 to 0.26.</p>
<dt>&quot;Module::CoreList&quot;</p>
<dd> Upgraded from version 2.37 to 2.38.</p>
<dt>&quot;PerlIO::scalar&quot;</p>
<dd> Upgraded from version 0.08 to 0.09.</p>
<dt>&quot;POSIX&quot;</p>
<dd> Upgraded from version 1.19 to 1.20. </p>
<p> It now includes constants for <font SIZE="-1">POSIX</font> signal constants.</p>
<dt>&quot;Safe&quot;</p>
<dd> Upgraded from version 2.27 to 2.28. </p>
<p> This fixes a possible infinite loop when looking for coderefs.</p>
<dt>&quot;Test::Simple&quot;</p>
<dd> Upgraded from version 0.96 to 0.97_01.</p>
<dt>&quot;Tie::Hash&quot;</p>
<dd> Upgraded from version 1.03 to 1.04. </p>
<p> Calling <tt>&quot;Tie::Hash-&gt;TIEHASH()&quot;</tt> used to loop forever. Now it <tt>&quot;croak&quot;</tt>s.</p>
<dt>&quot;Unicode::Collate&quot;</p>
<dd> Upgraded from version 0.56 to 0.59.</p>
<dt>&quot;XSLoader&quot;</p>
<dd> Upgraded from version 0.10 to 0.11.</dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlapi</i></p>
<dl>
<dt>&bull;</p>
<dd> Many of the optree construction functions are now documented.</dl>
<p> <i>perlbook</i></p>
<dl>
<dt>&bull;</p>
<dd> Expanded to cover many more popular books.</dl>
<p> <i>perlfaq</i></p>
<dl>
<dt>&bull;</p>
<dd> perlfaq, perlfaq2, perlfaq4, perlfaq5, perlfaq6, perlfaq8, and perlfaq9 have seen various updates and modernizations.</dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.</p>
<h3>New Diagnostics</h3>
<dl>
<dt>&bull;</p>
<dd> Parsing code internal error (%s) </p>
<p> New fatal error produced when parsing code supplied by an extension violated the parser&#8217;s <font SIZE="-1">API</font> in a detectable way.</p>
<dt>&bull;</p>
<dd> Use of qw(&#8230;) as parentheses is deprecated </p>
<p> See &#8220;Use of qw(&#8230;) as parentheses&#8221; for details.</dl>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;warn&quot;</tt> and <tt>&quot;die&quot;</tt> now produce &#8216;Wide character&#8217; warnings when fed a character outside the byte range if <font SIZE="-1">STDERR</font> is a byte-sized handle.</dl>
<h2>Utility Changes</h2>
<p> <i>h2ph</i></p>
<dl>
<dt>&bull;</p>
<dd> The use of a deprecated <tt>&quot;goto&quot;</tt> construct has been removed [perl #74404] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=74404">http://rt.perl.org/rt3/Public/Bug/Display.html?id=74404</a>&gt;.</dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</p>
<dd> The new <i>t/lib/universal.t</i> script tests the Internal::* functions and other things in <i>universal.c</i>.</p>
<dt>&bull;</p>
<dd> A rare race condition in <i>t/op/while_readdir.t</i> has been fixed, stopping it from failing randomly when running tests in parallel.</p>
<dt>&bull;</p>
<dd> The new <i>t/op/leaky-magic.t</i> script tests that magic applied to variables in the main packages does not affect other packages.</dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt><font SIZE="-1">VMS</font></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Make <tt>&quot;PerlIOUnix_open&quot;</tt> honour default permissions on <font SIZE="-1">VMS</font>. </p>
<p> When <tt>&quot;perlio&quot;</tt> became the default and <tt>&quot;unixio&quot;</tt> became the default bottom layer, the most common path for creating files from Perl became <tt>&quot;PerlIOUnix_open&quot;</tt>, which has always explicitly used <tt>0666</tt> as the permission mask. </p>
<p> To avoid this, <tt>0777</tt> is now passed as the permissions to <tt>&quot;open()&quot;</tt>. In the <font SIZE="-1">VMS</font> <font SIZE="-1">CRTL</font>, <tt>0777</tt> has a special meaning over and above intersecting with the current umask; specifically, it allows Unix syscalls to preserve native default permissions.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;CALL_FPTR&quot;</tt> and <tt>&quot;CPERLscope&quot;</tt> have been deprecated. </p>
<p> Those are left from an old implementation of <tt>&quot;MULTIPLICITY&quot;</tt> using C<font SIZE="-2">++</font> objects, which was removed in Perl 5.8. Nowadays these macros do exactly nothing, so they shouldn&#8217;t be used anymore. </p>
<p> For compatibility, they are still defined for external <tt>&quot;XS&quot;</tt> code. Only extensions defining <tt>&quot;PERL_CORE&quot;</tt> must be updated now.</p>
<dt>&bull;</p>
<dd> <tt>&quot;lex_stuff_pvs()&quot;</tt> has been added as a convenience macro wrapping <tt>&quot;lex_stuff_pvn()&quot;</tt> for literal strings.</p>
<dt>&bull;</p>
<dd> The recursive part of the peephole optimizer is now hookable. </p>
<p> In addition to <tt>&quot;PL_peepp&quot;</tt>, for hooking into the toplevel peephole optimizer, a <tt>&quot;PL_rpeepp&quot;</tt> is now available to hook into the optimizer recursing into side-chains of the optree.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> A regression introduced in Perl 5.12.0, making <tt>&quot;my $x = 3; $x = length(undef)&quot;</tt> result in <tt>$x</tt> set to <tt>3</tt> has been fixed. <tt>$x</tt> will now be <tt>&quot;undef&quot;</tt>.</p>
<dt>&bull;</p>
<dd> A fatal error in regular expressions when processing <font SIZE="-1">UTF-8</font> data has been fixed [perl #75680] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=75680">http://rt.perl.org/rt3/Public/Bug/Display.html?id=75680</a>&gt;.</p>
<dt>&bull;</p>
<dd> An erroneous regular expression engine optimization that caused regex verbs like <tt>*COMMIT</tt> to sometimes be ignored has been removed.</p>
<dt>&bull;</p>
<dd> The Perl debugger now also works in taint mode [perl #76872] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=76872">http://rt.perl.org/rt3/Public/Bug/Display.html?id=76872</a>&gt;.</p>
<dt>&bull;</p>
<dd> Several memory leaks in cloning and freeing threaded Perl interpreters have been fixed [perl #77352] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77352">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77352</a>&gt;.</p>
<dt>&bull;</p>
<dd> A possible string corruption when doing regular expression matches on overloaded objects has been fixed [perl #77084] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77084">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77084</a>&gt;.</p>
<dt>&bull;</p>
<dd> Magic applied to variables in the main package no longer affects other packages. See &#8220;Magic variables outside the main package&#8221; above [perl #76138] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=76138">http://rt.perl.org/rt3/Public/Bug/Display.html?id=76138</a>&gt;.</p>
<dt>&bull;</p>
<dd> Opening a glob reference via <tt>&quot;open $fh, &quot;&gt;&quot;, \*glob&quot;</tt> will no longer cause the glob to be corrupted when the filehandle is printed to. This would cause perl to crash whenever the glob&#8217;s contents were accessed [perl #77492] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77492">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77492</a>&gt;.</p>
<dt>&bull;</p>
<dd> The postincrement and postdecrement operators, <tt>&quot;++&quot;</tt> and <tt>&quot;--&quot;</tt>, used to cause leaks when being used on references. This has now been fixed.</p>
<dt>&bull;</p>
<dd> A bug when replacing the glob of a loop variable within the loop has been fixed [perl #21469] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=21469">http://rt.perl.org/rt3/Public/Bug/Display.html?id=21469</a>&gt;. This means the following code will no longer crash: </p>
<pre><code>
    for
        $x(...)
        {
            *x = *y;
        }
</code></pre>
<dt>&bull;</p>
<dd> Perl would segfault if the undocumented <tt>&quot;Internals&quot;</tt> functions that used reference prototypes were called with the <tt>&quot;&amp;foo()&quot;</tt> syntax, e.g. <tt>&quot;&amp;Internals::SvREADONLY(undef)&quot;</tt> [perl #77776] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77776">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77776</a>&gt;. </p>
<p> These functions now call <tt>&quot;SvROK&quot;</tt> on their arguments before dereferencing them with <tt>&quot;SvRV&quot;</tt>, and we test for this case in <i>t/lib/universal.t</i>.</p>
<dt>&bull;</p>
<dd> When assigning a list with duplicated keys to a hash, the assignment used to return garbage and/or freed values: </p>
<pre>
    @a = %h = (list with some duplicate keys);
</pre>
<p> This has now been fixed [perl #31865] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=31865">http://rt.perl.org/rt3/Public/Bug/Display.html?id=31865</a>&gt;.</p>
<dt>&bull;</p>
<dd> An earlier release of the 5.13 series of Perl changed the semantics of opening a reference to a copy of a glob: </p>
<pre>
    my $var = *STDOUT;
    open my $fh, '&gt;', \$var;
</pre>
<p> This was a mistake, and the previous behaviour from Perl 5.10 and 5.12, which is to treat \$var as a scalar reference, has now been restored.</p>
<dt>&bull;</p>
<dd> The regular expression bracketed character class <tt>&quot;[\8\9]&quot;</tt> was effectively the same as <tt>&quot;[89
