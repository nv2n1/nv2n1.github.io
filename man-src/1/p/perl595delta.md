---
title: "perl595delta(1)"
name: "perl595delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl595delta/"
description: "perl595delta – what is new for perl v5.9.5"
---

<h2 class="name">NAME</h2>
<p> perl595delta &#8211; what is new for perl v5.9.5 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.9.4 and the 5.9.5 development releases. See perl590delta, perl591delta, perl592delta, perl593delta and perl594delta for the differences between 5.8.0 and 5.9.4.</p>
<h2>Incompatible Changes</h2>
<h3>Tainting and printf</h3>
<p> When perl is run under taint mode, <tt>&quot;printf()&quot;</tt> and <tt>&quot;sprintf()&quot;</tt> will now reject any tainted format argument. (Rafael Garcia-Suarez)</p>
<h3>undef and signal handlers</h3>
<p> Undefining or deleting a signal handler via <tt>&quot;undef $SIG{FOO}&quot;</tt> is now equivalent to setting it to <tt>'DEFAULT'</tt>. (Rafael)</p>
<h3>strictures and array/hash dereferencing in <i>defined()</i></h3>
<p> <tt>&quot;defined @$foo&quot;</tt> and <tt>&quot;defined %$bar&quot;</tt> are now subject to <tt>&quot;strict 'refs'&quot;</tt> (that is, <tt>$foo</tt> and <tt>$bar</tt> shall be proper references there.) (Nicholas Clark) </p>
<p> (However, <tt>&quot;defined(@foo)&quot;</tt> and <tt>&quot;defined(%bar)&quot;</tt> are discouraged constructs anyway.)</p>
<h3>(?p{}) has been removed</h3>
<p> The regular expression construct <tt>&quot;(?p{})&quot;</tt>, which was deprecated in perl 5.8, has been removed. Use <tt>&quot;(??{})&quot;</tt> instead. (Rafael)</p>
<h3>Pseudo-hashes have been removed</h3>
<p> Support for pseudo-hashes has been removed from Perl 5.9. (The <tt>&quot;fields&quot;</tt> pragma remains here, but uses an alternate implementation.)</p>
<h3>Removal of the bytecode compiler and of perlcc</h3>
<p> <tt>&quot;perlcc&quot;</tt>, the byteloader and the supporting modules (B::C, B::CC, B::Bytecode, etc.) are no longer distributed with the perl sources. Those experimental tools have never worked reliably, and, due to the lack of volunteers to keep them in line with the perl interpreter developments, it was decided to remove them instead of shipping a broken version of those. The last version of those modules can be found with perl 5.9.4. </p>
<p> However the B compiler framework stays supported in the perl core, as with the more useful modules it has permitted (among others, B::Deparse and B::Concise).</p>
<h3>Removal of the <font SIZE="-1">JPL</font></h3>
<p> The <font SIZE="-1">JPL</font> (Java-Perl Linguo) has been removed from the perl sources tarball.</p>
<h3>Recursive inheritance detected earlier</h3>
<p> Perl will now immediately throw an exception if you modify any package&#8217;s <tt>@ISA</tt> in such a way that it would cause recursive inheritance. </p>
<p> Previously, the exception would not occur until Perl attempted to make use of the recursive inheritance while resolving a method or doing a <tt>&quot;$foo-&gt;isa($bar)&quot;</tt> lookup.</p>
<h2>Core Enhancements</h2>
<h3>Regular expressions</h3>
<dl>
<dt>Recursive Patterns</p>
<dd> It is now possible to write recursive patterns without using the <tt>&quot;(??{})&quot;</tt> construct. This new way is more efficient, and in many cases easier to read. </p>
<p> Each capturing parenthesis can now be treated as an independent pattern that can be entered by using the <tt>&quot;(?PARNO)&quot;</tt> syntax (<tt>&quot;PARNO&quot;</tt> standing for &#8220;parenthesis number&#8221;). For example, the following pattern will match nested balanced angle brackets: </p>
<pre>
    /
     ^                      # start of line
     (                      # start capture buffer 1
        &lt;                   #   match an opening angle bracket
        (?:                 #   match one of:
            (?&gt;             #     don't backtrack over the inside of this group
                [^&lt;&gt;]+      #       one or more non angle brackets
            )               #     end non backtracking group
        |                   #     ... or ...
            (?1)            #     recurse to bracket 1 and try it again
        )*                  #   0 or more times.
        &gt;                   #   match a closing angle bracket
     )                      # end capture buffer one
     $                      # end of line
    /x
</pre>
<p> Note, users experienced with <font SIZE="-1">PCRE</font> will find that the Perl implementation of this feature differs from the <font SIZE="-1">PCRE</font> one in that it is possible to backtrack into a recursed pattern, whereas in <font SIZE="-1">PCRE</font> the recursion is atomic or &#8220;possessive&#8221; in nature. (Yves Orton)</p>
<dt>Named Capture Buffers</p>
<dd> It is now possible to name capturing parenthesis in a pattern and refer to the captured contents by name. The naming syntax is <tt>&quot;(?&lt;NAME&gt;....)&quot;</tt>. It&#8217;s possible to backreference to a named buffer with the <tt>&quot;\k&lt;NAME&gt;&quot;</tt> syntax. In code, the new magical hashes <tt>&quot;%+&quot;</tt> and <tt>&quot;%-&quot;</tt> can be used to access the contents of the capture buffers. </p>
<p> Thus, to replace all doubled chars, one could write </p>
<pre>
    s/(?&lt;letter&gt;.)\k&lt;letter&gt;/$+{letter}/g
</pre>
<p> Only buffers with defined contents will be &#8220;visible&#8221; in the <tt>&quot;%+&quot;</tt> hash, so it&#8217;s possible to do something like </p>
<pre><code>
foreach
    my $name(keys % +)
    {
        print "content of buffer '$name' is $+{$name}
";
    }
</code></pre>
<p> The <tt>&quot;%-&quot;</tt> hash is a bit more complete, since it will contain array refs holding values from all capture buffers similarly named, if there should be many of them. </p>
<p> <tt>&quot;%+&quot;</tt> and <tt>&quot;%-&quot;</tt> are implemented as tied hashes through the new module <tt>&quot;Tie::Hash::NamedCapture&quot;</tt>. </p>
<p> Users exposed to the .NET regex engine will find that the perl implementation differs in that the numerical ordering of the buffers is sequential, and not &#8220;unnamed first, then named&#8221;. Thus in the pattern </p>
<pre>
   /(A)(?&lt;B&gt;B)(C)(?&lt;D&gt;D)/
</pre>
<p> <tt>$1</tt> will be &#8216;A&#8217;, <tt>$2</tt> will be &#8216;B&#8217;, <tt>$3</tt> will be &#8216;C&#8217; and <tt>$4</tt> will be &#8216;D&#8217; and not <tt>$1</tt> is &#8216;A&#8217;, <tt>$2</tt> is &#8216;C&#8217; and <tt>$3</tt> is &#8216;B&#8217; and <tt>$4</tt> is &#8216;D&#8217; that a .NET programmer would expect. This is considered a feature. :-) (Yves Orton)</p>
<dt>Possessive Quantifiers</p>
<dd> Perl now supports the &#8220;possessive quantifier&#8221; syntax of the &#8220;atomic match&#8221; pattern. Basically a possessive quantifier matches as much as it can and never gives any back. Thus it can be used to control backtracking. The syntax is similar to non-greedy matching, except instead of using a &#8216;?&#8217; as the modifier the &#8216;+&#8217; is used. Thus <tt>&quot;?+&quot;</tt>, <tt>&quot;*+&quot;</tt>, <tt>&quot;++&quot;</tt>, <tt>&quot;{min,max}+&quot;</tt> are now legal quantifiers. (Yves Orton)</p>
<dt>Backtracking control verbs</p>
<dd> The regex engine now supports a number of special-purpose backtrack control verbs: (*THEN), (*PRUNE), (*MARK), (*SKIP), (*COMMIT), (*FAIL) and (*ACCEPT). See perlre for their descriptions. (Yves Orton)</p>
<dt>Relative backreferences</p>
<dd> A new syntax <tt>&quot;\g{N}&quot;</tt> or <tt>&quot;\gN&quot;</tt> where &#8220;N&#8221; is a decimal integer allows a safer form of back-reference notation as well as allowing relative backreferences. This should make it easier to generate and embed patterns that contain backreferences. See &#8220;Capture buffers&#8221; in perlre. (Yves Orton)</p>
<dt>&quot;\K&quot; escape</p>
<dd> The functionality of Jeff Pinyan&#8217;s module Regexp::Keep has been added to the core. You can now use in regular expressions the special escape <tt>&quot;\K&quot;</tt> as a way to do something like floating length positive lookbehind. It is also useful in substitutions like: </p>
<pre>
  s/(foo)bar/$1/g
</pre>
<p> that can now be converted to </p>
<pre>
  s/foo\Kbar//g
</pre>
<p> which is much more efficient. (Yves Orton)</p>
<dt>Vertical and horizontal whitespace, and linebreak</p>
<dd> Regular expressions now recognize the <tt>&quot;&quot;</tt> and <tt>&quot;\h&quot;</tt> escapes, that match vertical and horizontal whitespace, respectively. <tt>&quot;\V&quot;</tt> and <tt>&quot;\H&quot;</tt> logically match their complements. </p>
<p> <tt>&quot;\R&quot;</tt> matches a generic linebreak, that is, vertical whitespace, plus the multi-character sequence <tt>&quot;
&quot;</tt>.</dl>
<h3>The _ prototype</h3>
<p> A new prototype character has been added. <tt>&quot;_&quot;</tt> is equivalent to <tt>&quot;$&quot;</tt> (it denotes a scalar), but defaults to <tt>$_</tt> if the corresponding argument isn&#8217;t supplied. Due to the optional nature of the argument, you can only use it at the end of a prototype, or before a semicolon. </p>
<p> This has a small incompatible consequence: the <i>prototype()</i> function has been adjusted to return <tt>&quot;_&quot;</tt> for some built-ins in appropriate cases (for example, <tt>&quot;prototype('CORE::rmdir')&quot;</tt>). (Rafael)</p>
<h3><font SIZE="-1">UNITCHECK</font> blocks</h3>
<p> <tt>&quot;UNITCHECK&quot;</tt>, a new special code block has been introduced, in addition to <tt>&quot;BEGIN&quot;</tt>, <tt>&quot;CHECK&quot;</tt>, <tt>&quot;INIT&quot;</tt> and <tt>&quot;END&quot;</tt>. </p>
<p> <tt>&quot;CHECK&quot;</tt> and <tt>&quot;INIT&quot;</tt> blocks, while useful for some specialized purposes, are always executed at the transition between the compilation and the execution of the main program, and thus are useless whenever code is loaded at runtime. On the other hand, <tt>&quot;UNITCHECK&quot;</tt> blocks are executed just after the unit which defined them has been compiled. See perlmod for more information. (Alex Gough)</p>
<h3><i>readpipe()</i> is now overridable</h3>
<p> The built-in function <i>readpipe()</i> is now overridable. Overriding it permits also to override its operator counterpart, <tt>&quot;qx//&quot;</tt> (a.k.a. <tt>&quot;``&quot;</tt>). Moreover, it now defaults to <tt>$_</tt> if no argument is provided. (Rafael)</p>
<h3>default argument for <i>readline()</i></h3>
<p> <i>readline()</i> now defaults to <tt>*ARGV</tt> if no argument is provided. (Rafael)</p>
<h3><font SIZE="-1">UCD</font> 5.0.0</h3>
<p> The copy of the Unicode Character Database included in Perl 5.9 has been updated to version 5.0.0.</p>
<h3>Smart match</h3>
<p> The smart match operator (<tt>&quot;~~&quot;</tt>) is now available by default (you don&#8217;t need to enable it with <tt>&quot;use feature&quot;</tt> any longer). (Michael G Schwern)</p>
<h3>Implicit loading of feature</h3>
<p> The <tt>&quot;feature&quot;</tt> pragma is now implicitly loaded when you require a minimal perl version (with the <tt>&quot;use VERSION&quot;</tt> construct) greater than, or equal to, 5.9.5.</p>
<h2>Modules and Pragmas</h2>
<h3>New Pragma, mro</h3>
<p> A new pragma, <tt>&quot;mro&quot;</tt> (for Method Resolution Order) has been added. It permits to switch, on a per-class basis, the algorithm that perl uses to find inherited methods in case of a multiple inheritance hierarchy. The default <font SIZE="-1">MRO</font> hasn&#8217;t changed (<font SIZE="-1">DFS</font>, for Depth First Search). Another <font SIZE="-1">MRO</font> is available: the C3 algorithm. See mro for more information. (Brandon Black) </p>
<p> Note that, due to changes in the implementation of class hierarchy search, code that used to undef the <tt>*ISA</tt> glob will most probably break. Anyway, undef&#8217;ing <tt>*ISA</tt> had the side-effect of removing the magic on the <tt>@ISA</tt> array and should not have been done in the first place.</p>
<h3>bignum, bigint, bigrat</h3>
<p> The three numeric pragmas <tt>&quot;bignum&quot;</tt>, <tt>&quot;bigint&quot;</tt> and <tt>&quot;bigrat&quot;</tt> are now lexically scoped. (Tels)</p>
<h3>Math::BigInt/Math::BigFloat</h3>
<p> Many bugs have been fixed; noteworthy are comparisons with NaN, which no longer warn about undef values. </p>
<p> The following things are new:</p>
<dl>
<dt><i>config()</i></p>
<dd> The <i>config()</i> method now also supports the calling-style <tt>&quot;config('lib')&quot;</tt> in addition to <tt>&quot;config()-&gt;{'lib'}&quot;</tt>.</p>
<dt><i>import()</i></p>
<dd> Upon import, using <tt>&quot;lib =&gt; 'Foo'&quot;</tt> now warns if the low-level library cannot be found. To suppress the warning, you can use <tt>&quot;try =&gt; 'Foo'&quot;</tt> instead. To convert the warning into a die, use <tt>&quot;only =&gt; 'Foo'&quot;</tt> instead.</p>
<dt>roundmode common</p>
<dd> A rounding mode of <tt>&quot;common&quot;</tt> is now supported.</dl>
<p> Also, support for the following methods has been added:</p>
<dl>
<dt><i>bpi()</i>, <i>bcos()</i>, <i>bsin()</i>, <i>batan()</i>, <i>batan2()</i></p>
<dd>
<dt><i>bmuladd()</i></p>
<dd>
<dt><i>bexp()</i>, <i>bnok()</i></p>
<dd>
<dt><i>from_hex()</i>, <i>from_oct()</i>, and <i>from_bin()</i></p>
<dd>
<dt><i>as_oct()</i></p>
<dd></dl>
<p> In addition, the default math-backend (Calc (Perl) and FastCalc (<font SIZE="-1">XS</font>)) now support storing numbers in parts with 9 digits instead of 7 on Perls with either 64bit integer or long double support. This means math operations scale better and are thus faster for really big numbers.</p>
<h3>New Core Modules</h3>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;Locale::Maketext::Simple&quot;</tt>, needed by <font SIZE="-1">CPANPLUS</font>, is a simple wrapper around <tt>&quot;Locale::Maketext::Lexicon&quot;</tt>. Note that <tt>&quot;Locale::Maketext::Lexicon&quot;</tt> isn&#8217;t included in the perl core; the behaviour of <tt>&quot;Locale::Maketext::Simple&quot;</tt> gracefully degrades when the later isn&#8217;t present.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Params::Check&quot;</tt> implements a generic input parsing/checking mechanism. It is used by <font SIZE="-1">CPANPLUS</font>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Term::UI&quot;</tt> simplifies the task to ask questions at a terminal prompt.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Object::Accessor&quot;</tt> provides an interface to create per-object accessors.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Module::Pluggable&quot;</tt> is a simple framework to create modules that accept pluggable sub-modules.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Module::Load::Conditional&quot;</tt> provides simple ways to query and possibly load installed modules.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Time::Piece&quot;</tt> provides an object oriented interface to time functions, overriding the built-ins <i>localtime()</i> and <i>gmtime()</i>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;IPC::Cmd&quot;</tt> helps to find and run external commands, possibly interactively.</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::Fetch&quot;</tt> provide a simple generic file fetching mechanism.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Log::Message&quot;</tt> and <tt>&quot;Log::Message::Simple&quot;</tt> are used by the log facility of <tt>&quot;CPANPLUS&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Archive::Extract&quot;</tt> is a generic archive extraction mechanism for <i>.tar</i> (plain, gziped or bzipped) or <i>.zip</i> files.</p>
<dt>&bull;</p>
<dd> <tt>&quot;CPANPLUS&quot;</tt> provides an <font SIZE="-1">API</font> and a command-line tool to access the <font SIZE="-1">CPAN</font> mirrors.</dl>
<h3>Module changes</h3>
<dl>
<dt>&quot;assertions&quot;</p>
<dd> The <tt>&quot;assertions&quot;</tt> pragma, its submodules <tt>&quot;assertions::activate&quot;</tt> and <tt>&quot;assertions::compat&quot;</tt> and the <code>-A</code> command-line switch have been removed. The interface was not judged mature enough for inclusion in a stable release.</p>
<dt>&quot;base&quot;</p>
<dd> The <tt>&quot;base&quot;</tt> pragma now warns if a class tries to inherit from itself. (Curtis &#8220;Ovid&#8221; Poe)</p>
<dt>&quot;strict&quot; and &quot;warnings&quot;</p>
<dd> <tt>&quot;strict&quot;</tt> and <tt>&quot;warnings&quot;</tt> will now complain loudly if they are loaded via incorrect casing (as in <tt>&quot;use Strict;&quot;</tt>). (Johan Vromans)</p>
<dt>&quot;warnings&quot;</p>
<dd> The <tt>&quot;warnings&quot;</tt> pragma doesn&#8217;t load <tt>&quot;Carp&quot;</tt> anymore. That means that code that used <tt>&quot;Carp&quot;</tt> routines without having loaded it at compile time might need to be adjusted; typically, the following (faulty) code won&#8217;t work anymore, and will require parentheses to be added after the function name: </p>
<pre>
    use warnings;
    require Carp;
    Carp::confess &quot;argh&quot;;
</pre>
<dt>&quot;less&quot;</p>
<dd> <tt>&quot;less&quot;</tt> now does something useful (or at least it tries to). In fact, it has been turned into a lexical pragma. So, in your modules, you can now test whether your users have requested to use less <font SIZE="-1">CPU</font>, or less memory, less magic, or maybe even less fat. See less for more. (Joshua ben Jore)</p>
<dt>&quot;Attribute::Handlers&quot;</p>
<dd> <tt>&quot;Attribute::Handlers&quot;</tt> can now report the caller&#8217;s file and line number. (David Feldman)</p>
<dt>&quot;B::Lint&quot;</p>
<dd> <tt>&quot;B::Lint&quot;</tt> is now based on <tt>&quot;Module::Pluggable&quot;</tt>, and so can be extended with plugins. (Joshua ben Jore)</p>
<dt>&quot;B&quot;</p>
<dd> It&#8217;s now possible to access the lexical pragma hints (<tt>&quot;%^H&quot;</tt>) by using the method <i>B::COP::hints_hash()</i>. It returns a <tt>&quot;B::RHE&quot;</tt> object, which in turn can be used to get a hash reference via the method <i>B::RHE::HASH()</i>. (Joshua ben Jore)</p>
<dt>&quot;Thread&quot;</p>
<dd> As the old 5005thread threading model has been removed, in favor of the ithreads scheme, the <tt>&quot;Thread&quot;</tt> module is now a compatibility wrapper, to be used in old code only. It has been removed from the default list of dynamic extensions.</dl>
<h2>Utility Changes</h2>
<h3>cpanp</h3>
<p> <tt>&quot;cpanp&quot;</tt>, the <font SIZE="-1">CPANPLUS</font> shell, has been added. (<tt>&quot;cpanp-run-perl&quot;</tt>, an helper for <font SIZE="-1">CPANPLUS</font> operation, has been added too, but isn&#8217;t intended for direct use).</p>
<h3>cpan2dist</h3>
<p> <tt>&quot;cpan2dist&quot;</tt> is a new utility, that comes with <font SIZE="-1">CPANPLUS</font>. It&#8217;s a tool to create distributions (or packages) from <font SIZE="-1">CPAN</font> modules.</p>
<h3>pod2html</h3>
<p> The output of <tt>&quot;pod2html&quot;</tt> has been enhanced to be more customizable via <font SIZE="-1">CSS</font>. Some formatting problems were also corrected. (Jari Aalto)</p>
<h2>Documentation</h2>
<h3>New manpage, perlunifaq</h3>
<p> A new manual page, perlunifaq (the Perl Unicode <font SIZE="-1">FAQ</font>), has been added (Juerd Waalboer).</p>
<h2>Installation and Configuration Improvements</h2>
<h3>C<font SIZE="-2">++</font> compatibility</h3>
<p> Efforts have been made to make perl and the core <font SIZE="-1">XS</font> modules compilable with various C<font SIZE="-2">++</font> compilers (although the situation is not perfect with some of the compilers on some of the platforms tested.)</p>
<h3>Visual C<font SIZE="-2">++</font></h3>
<p> Perl now can be compiled with Microsoft Visual C<font SIZE="-2">++</font> 2005.</p>
<h3>Static build on Win32</h3>
<p> It&#8217;s now possible to build a <tt>&quot;perl-static.exe&quot;</tt> that doesn&#8217;t depend on <tt>&quot;perl59.dll&quot;</tt> on Win32. See the Win32 makefiles for details. (Vadim Konovalov)</p>
<h3>win32 builds</h3>
<p> All win32 builds (MS-Win, WinCE) have been merged and cleaned up.</p>
<h3>d_pseudofork and d_printf_format_null</h3>
<p> A new configuration variable, available as <tt>$Config{d_pseudofork}</tt> in the Config module, has been added, to distinguish real <i>fork()</i> support from fake pseudofork used on Windows platforms. </p>
<p> A new configuration variable, <tt>&quot;d_printf_format_null&quot;</tt>, has been added, to see if printf-like formats are allowed to be <font SIZE="-1">NULL</font>.</p>
<h3>Help</h3>
<p> <tt>&quot;Configure -h&quot;</tt> has been extended with the most used option. </p>
<p> Much less &#8216;Whoa there&#8217; messages.</p>
<h3>64bit systems</h3>
<p> Better detection of 64bit(only) systems, and setting all the (library) paths accordingly.</p>
<h3>Ports</h3>
<p> Perl has been reported to work on MidnightBSD. </p>
<p> Support for Cray <font SIZE="-1">XT4</font> Catamount/Qk has been added. </p>
<p> Vendor patches have been merged for RedHat and GenToo.</p>
<h2>Selected Bug Fixes</h2>
<p> PerlIO::scalar will now prevent writing to read-only scalars. Moreover, <i>seek()</i> is now supported with PerlIO::scalar-based filehandles, the underlying string being zero-filled as needed. (Rafael, Jarkko Hietaniemi) </p>
<p> <i>study()</i> never worked for <font SIZE="-1">UTF-8</font> strings, but could lead to false results. It&#8217;s now a no-op on <font SIZE="-1">UTF-8</font> data. (Yves Orton) </p>
<p> The signals <font SIZE="-1">SIGILL</font>, <font SIZE="-1">SIGBUS</font> and <font SIZE="-1">SIGSEGV</font> are now always delivered in an &#8220;unsafe&#8221; manner (contrary to other signals, that are deferred until the perl interpreter reaches a reasonably stable state; see &#8220;Deferred Signals (Safe Signals)&#8221; in perlipc). (Rafael) </p>
<p> When a module or a file is loaded through an <tt>@INC</tt>-hook, and when this hook has set a filename entry in <tt>%INC</tt>, __FILE__ is now set for this module accordingly to the contents of that <tt>%INC</tt> entry. (Rafael) </p>
<p> The <tt>&quot;-w&quot;</tt> and <tt>&quot;-t&quot;</tt> switches can now be used together without messing up what categories of warnings are activated or not. (Rafael) </p>
<p> Duping a filehandle which has the <tt>&quot;:utf8&quot;</tt> PerlIO layer set will now properly carry that layer on the duped filehandle. (Rafael) </p>
<p> Localizing an hash element whose key was given as a variable didn&#8217;t work correctly if the variable was changed while the <i>local()</i> was in effect (as in <tt>&quot;local $h{$x}; ++$x&quot;</tt>). (Bo Lindbergh)</p>
<h2>New or Changed Diagnostics</h2>
<h3>Deprecations</h3>
<p> Two deprecation warnings have been added: (Rafael) </p>
<pre>
    Opening dirhandle %s also as a file
    Opening filehandle %s also as a directory
</pre>
<h2>Changed Internals</h2>
<p> The anonymous hash and array constructors now take 1 op in the optree instead of 3, now that pp_anonhash and pp_anonlist return a reference to an hash/array when the op is flagged with OPf_SPECIAL (Nicholas Clark).</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/rt3/">http://rt.perl.org/rt3/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Core Enhancements</a></p>
<dd>
<dt><a href="#lbAV">Modules and Pragmas</a></p>
<dd>
<dt><a href="#lbBB">Utility Changes</a></p>
<dd>
<dt><a href="#lbBF">Documentation</a></p>
<dd>
<dt><a href="#lbBH">Installation and Configuration Improvements</a></p>
<dd>
<dt><a href="#lbBQ">Selected Bug Fixes</a></p>
<dd>
<dt><a href="#lbBR">New or Changed Diagnostics</a></p>
<dd>
<dt><a href="#lbBT">Changed Internals</a></p>
<dd>
<dt><a href="#lbBU">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbBV">SEE ALSO</a></p>
<dd></dl>
