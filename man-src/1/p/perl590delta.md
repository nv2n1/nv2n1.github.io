---
title: "perl590delta(1)"
name: "perl590delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl590delta/"
description: "perl590delta – what is new for perl v5.9.0"
---

<h2 class="name">NAME</h2>
<p> perl590delta &#8211; what is new for perl v5.9.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.8.0 release and the 5.9.0 release.</p>
<h2>Incompatible Changes</h2>
<h3>Hash Randomisation</h3>
<p> Mainly due to security reasons, the &#8220;random ordering&#8221; of hashes has been made even more random. Previously while the order of hash elements from <i>keys()</i>, <i>values()</i>, and <i>each()</i> was essentially random, it was still repeatable. Now, however, the order varies between different runs of Perl. </p>
<p> <code>Perl has never guaranteed any ordering of the hash keys</code>, and the ordering has already changed several times during the lifetime of Perl 5. Also, the ordering of hash keys has always been, and continues to be, affected by the insertion order. </p>
<p> The added randomness may affect applications. </p>
<p> One possible scenario is when output of an application has included hash data. For example, if you have used the Data::Dumper module to dump data into different files, and then compared the files to see whether the data has changed, now you will have false positives since the order in which hashes are dumped will vary. In general the cure is to sort the keys (or the values); in particular for Data::Dumper to use the <tt>&quot;Sortkeys&quot;</tt> option. If some particular order is really important, use tied hashes: for example the Tie::IxHash module which by default preserves the order in which the hash elements were added. </p>
<p> More subtle problem is reliance on the order of &#8220;global destruction&#8221;. That is what happens at the end of execution: Perl destroys all data structures, including user data. If your destructors (the <font SIZE="-1">DESTROY</font> subroutines) have assumed any particular ordering to the global destruction, there might be problems ahead. For example, in a destructor of one object you cannot assume that objects of any other class are still available, unless you hold a reference to them. If the environment variable <font SIZE="-1">PERL_DESTRUCT_LEVEL</font> is set to a non-zero value, or if Perl is exiting a spawned thread, it will also destruct the ordinary references and the symbol tables that are no longer in use. You can&#8217;t call a class method or an ordinary function on a class that has been collected that way. </p>
<p> The hash randomisation is certain to reveal hidden assumptions about some particular ordering of hash elements, and outright bugs: it revealed a few bugs in the Perl core and core modules. </p>
<p> To disable the hash randomisation in runtime, set the environment variable <font SIZE="-1">PERL_HASH_SEED</font> to 0 (zero) before running Perl (for more information see &#8220;<font SIZE="-1">PERL_HASH_SEED</font>&#8221; in perlrun), or to disable the feature completely in compile time, compile with <tt>&quot;-DNO_HASH_SEED&quot;</tt> (see <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i>). </p>
<p> See &#8220;Algorithmic Complexity Attacks&#8221; in perlsec for the original rationale behind this change.</p>
<h3><font SIZE="-1">UTF-8</font> On Filehandles No Longer Activated By Locale</h3>
<p> In Perl 5.8.0 all filehandles, including the standard filehandles, were implicitly set to be in Unicode <font SIZE="-1">UTF-8</font> if the locale settings indicated the use of <font SIZE="-1">UTF-8</font>. This feature caused too many problems, so the feature was turned off and redesigned: see &#8220;Core Enhancements&#8221;.</p>
<h3>Single-number v-strings are no longer v-strings before =&gt;</h3>
<p> The version strings or v-strings (see &#8220;Version Strings&#8221; in perldata) feature introduced in Perl 5.6.0 has been a source of some confusion&#8212; especially when the user did not want to use it, but Perl thought it knew better. Especially troublesome has been the feature that before a &#8220;=&gt;&#8221; a version string (a &#8220;v&#8221; followed by digits) has been interpreted as a v-string instead of a string literal. In other words: </p>
<pre>
        %h = ( v65 =&gt; 42 );
</pre>
<p> has meant since Perl 5.6.0 </p>
<pre>
        %h = ( 'A' =&gt; 42 );
</pre>
<p> (at least in platforms of <font SIZE="-1">ASCII</font> progeny) Perl 5.8.1 restored the more natural interpretation </p>
<pre>
        %h = ( 'v65' =&gt; 42 );
</pre>
<p> The multi-number v-strings like v65.66 and 65.66.67 still continue to be v-strings in Perl 5.8.</p>
<h3>(Win32) The -C Switch Has Been Repurposed</h3>
<p> The -C switch has changed in an incompatible way. The old semantics of this switch only made sense in Win32 and only in the &#8220;use utf8&#8221; universe in 5.6.x releases, and do not make sense for the Unicode implementation in 5.8.0. Since this switch could not have been used by anyone, it has been repurposed. The behavior that this switch enabled in 5.6.x releases may be supported in a transparent, data-dependent fashion in a future release. </p>
<p> For the new life of this switch, see &#8220;<font SIZE="-1">UTF-8</font> no longer default under <font SIZE="-1">UTF-8</font> locales&#8221;, and &#8220;-C&#8221; in perlrun.</p>
<h3>(Win32) The /d Switch Of cmd.exe</h3>
<p> Since version 5.8.1, perl uses the /d switch when running the cmd.exe shell internally for <i>system()</i>, backticks, and when opening pipes to external programs. The extra switch disables the execution of AutoRun commands from the registry, which is generally considered undesirable when running external programs. If you wish to retain compatibility with the older behavior, set <font SIZE="-1">PERL5SHELL</font> in your environment to <tt>&quot;cmd /x/c&quot;</tt>.</p>
<h3>The $* variable has been removed</h3>
<p> <tt>$*</tt>, which was deprecated in favor of the <tt>&quot;/s&quot;</tt> and <tt>&quot;/m&quot;</tt> regexp modifiers, has been removed.</p>
<h2>Core Enhancements</h2>
<h3>Assertions</h3>
<p> Perl 5.9.0 has experimental support for assertions. Note that the user interface is not fully stabilized yet, and it may change until the 5.10.0 release. A new command-line switch, <code>-A</code>, is used to activate assertions, which are declared with the <tt>&quot;assertions&quot;</tt> pragma. See assertions.</p>
<h3>Defined-or operators</h3>
<p> A new operator <tt>&quot;//&quot;</tt> (defined-or) has been implemented. The following statement: </p>
<pre>
    $a // $b
</pre>
<p> is merely equivalent to </p>
<pre>
   defined $a ? $a : $b
</pre>
<p> and </p>
<pre>
   $c //= $d;
</pre>
<p> can be used instead of </p>
<pre>
   $c = $d unless defined $c;
</pre>
<p> This operator has the same precedence and associativity as <tt>&quot;||&quot;</tt>. It has a low-precedence counterpart, <tt>&quot;err&quot;</tt>, which has the same precedence and associativity as <tt>&quot;or&quot;</tt>. Special care has been taken to ensure that those operators Do What You Mean while not breaking old code, but some edge cases involving the empty regular expression may now parse differently. See perlop for details.</p>
<h3><font SIZE="-1">UTF-8</font> no longer default under <font SIZE="-1">UTF-8</font> locales</h3>
<p> In Perl 5.8.0 many Unicode features were introduced. One of them was found to be of more nuisance than benefit: the automagic (and silent) &#8220;UTF-8-ification&#8221; of filehandles, including the standard filehandles, if the user&#8217;s locale settings indicated use of <font SIZE="-1">UTF-8</font>. </p>
<p> For example, if you had <tt>&quot;en_US.UTF-8&quot;</tt> as your locale, your <font SIZE="-1">STDIN</font> and <font SIZE="-1">STDOUT</font> were automatically &#8220;<font SIZE="-1">UTF-8</font>&#8221;, in other words an implicit binmode(&#8230;, &#8220;:utf8&#8221;) was made. This meant that trying to print, say, <i>chr</i>(0xff), ended up printing the bytes 0xc3 0xbf. Hardly what you had in mind unless you were aware of this feature of Perl 5.8.0. The problem is that the vast majority of people weren&#8217;t: for example in RedHat releases 8 and 9 the <code>default</code> locale setting is <font SIZE="-1">UTF-8</font>, so all RedHat users got <font SIZE="-1">UTF-8</font> filehandles, whether they wanted it or not. The pain was intensified by the Unicode implementation of Perl 5.8.0 (still) having nasty bugs, especially related to the use of s/// and tr///. (Bugs that have been fixed in 5.8.1) </p>
<p> Therefore a decision was made to backtrack the feature and change it from implicit silent default to explicit conscious option. The new Perl command line option <tt>&quot;-C&quot;</tt> and its counterpart environment variable <font SIZE="-1">PERL_UNICODE</font> can now be used to control how Perl and Unicode interact at interfaces like I/O and for example the command line arguments. See &#8220;-C&#8221; in perlrun and &#8220;<font SIZE="-1">PERL_UNICODE</font>&#8221; in perlrun for more information.</p>
<h3>Unsafe signals again available</h3>
<p> In Perl 5.8.0 the so-called &#8220;safe signals&#8221; were introduced. This means that Perl no longer handles signals immediately but instead &#8220;between opcodes&#8221;, when it is safe to do so. The earlier immediate handling easily could corrupt the internal state of Perl, resulting in mysterious crashes. </p>
<p> However, the new safer model has its problems too. Because now an opcode, a basic unit of Perl execution, is never interrupted but instead let to run to completion, certain operations that can take a long time now really do take a long time. For example, certain network operations have their own blocking and timeout mechanisms, and being able to interrupt them immediately would be nice. </p>
<p> Therefore perl 5.8.1 introduced a &#8220;backdoor&#8221; to restore the pre-5.8.0 (pre-5.7.3, really) signal behaviour. Just set the environment variable <font SIZE="-1">PERL_SIGNALS</font> to <tt>&quot;unsafe&quot;</tt>, and the old immediate (and unsafe) signal handling behaviour returns. See &#8220;<font SIZE="-1">PERL_SIGNALS</font>&#8221; in perlrun and &#8220;Deferred Signals (Safe Signals)&#8221; in perlipc. </p>
<p> In completely unrelated news, you can now use safe signals with POSIX::SigAction. See &#8220;POSIX::SigAction&#8221; in <font SIZE="-1">POSIX</font>.</p>
<h3>Tied Arrays with Negative Array Indices</h3>
<p> Formerly, the indices passed to <tt>&quot;FETCH&quot;</tt>, <tt>&quot;STORE&quot;</tt>, <tt>&quot;EXISTS&quot;</tt>, and <tt>&quot;DELETE&quot;</tt> methods in tied array class were always non-negative. If the actual argument was negative, Perl would call <font SIZE="-1">FETCHSIZE</font> implicitly and add the result to the index before passing the result to the tied array method. This behaviour is now optional. If the tied array class contains a package variable named <tt>$NEGATIVE_INDICES</tt> which is set to a true value, negative values will be passed to <tt>&quot;FETCH&quot;</tt>, <tt>&quot;STORE&quot;</tt>, <tt>&quot;EXISTS&quot;</tt>, and <tt>&quot;DELETE&quot;</tt> unchanged.</p>
<h3>local ${$x}</h3>
<p> The syntaxes </p>
<pre><code>
local ${$x} local @{$x} local %
{
    $x
}
</code></pre>
<p> now do localise variables, given that the <tt>$x</tt> is a valid variable name.</p>
<h3>Unicode Character Database 4.0.0</h3>
<p> The copy of the Unicode Character Database included in Perl 5.8 has been updated to 4.0.0 from 3.2.0. This means for example that the Unicode character properties are as in Unicode 4.0.0.</p>
<h3>Miscellaneous Enhancements</h3>
<p> <tt>&quot;unpack()&quot;</tt> now defaults to unpacking the <tt>$_</tt>. </p>
<p> <tt>&quot;map&quot;</tt> in void context is no longer expensive. <tt>&quot;map&quot;</tt> is now context aware, and will not construct a list if called in void context. </p>
<p> If a socket gets closed by the server while printing to it, the client now gets a <font SIZE="-1">SIGPIPE</font>. While this new feature was not planned, it fell naturally out of PerlIO changes, and is to be considered an accidental feature. </p>
<p> PerlIO::get_layers(<font SIZE="-1">FH</font>) returns the names of the PerlIO layers active on a filehandle. </p>
<p> PerlIO::via layers can now have an optional <font SIZE="-1">UTF8</font> method to indicate whether the layer wants to &#8220;auto-:utf8&#8221; the stream. </p>
<p> <i>utf8::is_utf8()</i> has been added as a quick way to test whether a scalar is encoded internally in <font SIZE="-1">UTF-8</font> (Unicode).</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules And Pragmata</h3>
<p> The following modules and pragmata have been updated since Perl 5.8.0:</p>
<dl>
<dt>base</p>
<dd>
<dt>B::Bytecode</p>
<dd> In much better shape than it used to be. Still far from perfect, but maybe worth a try.</p>
<dt>B::Concise</p>
<dd>
<dt>B::Deparse</p>
<dd>
<dt>Benchmark</p>
<dd> An optional feature, <tt>&quot;:hireswallclock&quot;</tt>, now allows for high resolution wall clock times (uses Time::HiRes).</p>
<dt>ByteLoader</p>
<dd> See B::Bytecode.</p>
<dt>bytes</p>
<dd> Now has bytes::substr.</p>
<dt><font SIZE="-1">CGI</font></p>
<dd>
<dt>charnames</p>
<dd> One can now have custom character name aliases.</p>
<dt><font SIZE="-1">CPAN</font></p>
<dd> There is now a simple command line frontend to the <font SIZE="-1">CPAN</font>.pm module called <i>cpan</i>.</p>
<dt>Data::Dumper</p>
<dd> A new option, Pair, allows choosing the separator between hash keys and values.</p>
<dt>DB_File</p>
<dd>
<dt>Devel::PPPort</p>
<dd>
<dt>Digest::MD5</p>
<dd>
<dt>Encode</p>
<dd> Significant updates on the encoding pragma functionality (tr/// and the <font SIZE="-1">DATA</font> filehandle, formats). </p>
<p> If a filehandle has been marked as to have an encoding, unmappable characters are detected already during input, not later (when the corrupted data is being used). </p>
<p> The <font SIZE="-1">ISO</font> 8859-6 conversion table has been corrected (the 0x30..0x39 erroneously mapped to U+0660..U+0669, instead of U+0030..U+0039). The <font SIZE="-1">GSM</font> 03.38 conversion did not handle escape sequences correctly. The <font SIZE="-1">UTF-7</font> encoding has been added (making Encode feature-complete with Unicode::String).</p>
<dt>fields</p>
<dd>
<dt>libnet</p>
<dd>
<dt>Math::BigInt</p>
<dd> A lot of bugs have been fixed since v1.60, the version included in Perl v5.8.0. Especially noteworthy are the bug in Calc that caused div and mod to fail for some large values, and the fixes to the handling of bad inputs. </p>
<p> Some new features were added, e.g. the <i>broot()</i> method, you can now pass parameters to <i>config()</i> to change some settings at runtime, and it is now possible to trap the creation of NaN and infinity. </p>
<p> As usual, some optimizations took place and made the math overall a tad faster. In some cases, quite a lot faster, actually. Especially alternative libraries like Math::BigInt::GMP benefit from this. In addition, a lot of the quite clunky routines like <i>fsqrt()</i> and <i>flog()</i> are now much much faster.</p>
<dt>MIME::Base64</p>
<dd>
<dt><font SIZE="-1">NEXT</font></p>
<dd> Diamond inheritance now works.</p>
<dt>Net::Ping</p>
<dd>
<dt>PerlIO::scalar</p>
<dd> Reading from non-string scalars (like the special variables, see perlvar) now works.</p>
<dt>podlators</p>
<dd>
<dt>Pod::LaTeX</p>
<dd>
<dt>PodParsers</p>
<dd>
<dt>Pod::Perldoc</p>
<dd> Complete rewrite. As a side-effect, no longer refuses to startup when run by root.</p>
<dt>Scalar::Util</p>
<dd> New utilities: refaddr, isvstring, looks_like_number, set_prototype.</p>
<dt>Storable</p>
<dd> Can now store code references (via B::Deparse, so not foolproof).</p>
<dt>strict</p>
<dd> Earlier versions of the strict pragma did not check the parameters implicitly passed to its &#8220;import&#8221; (use) and &#8220;unimport&#8221; (no) routine. This caused the false idiom such as: </p>
<p>use strict qw(@ISA);<br />
@ISA = qw(Foo);</p>
<p> This however (probably) raised the false expectation that the strict refs, vars and subs were being enforced (and that <tt>@ISA</tt> was somehow &#8220;declared&#8221;). But the strict refs, vars, and subs are <code>not</code> enforced when using this false idiom. </p>
<p> Starting from Perl 5.8.1, the above <code>will</code> cause an error to be raised. This may cause programs which used to execute seemingly correctly without warnings and errors to fail when run under 5.8.1. This happens because </p>
<pre>
        use strict qw(@ISA);
</pre>
<p> will now fail with the error: </p>
<pre>
        Unknown 'strict' tag(s) '@ISA'
</pre>
<p> The remedy to this problem is to replace this code with the correct idiom: </p>
<pre><code>
use strict;
use vars qw(@ISA);
@ISA = qw(Foo);
</code></pre>
<dt>Term::ANSIcolor</p>
<dd>
<dt>Test::Harness</p>
<dd> Now much more picky about extra or missing output from test scripts.</p>
<dt>Test::More</p>
<dd>
<dt>Test::Simple</p>
<dd>
<dt>Text::Balanced</p>
<dd>
<dt>Time::HiRes</p>
<dd> Use of <i>nanosleep()</i>, if available, allows mixing subsecond sleeps with alarms.</p>
<dt>threads</p>
<dd> Several fixes, for example for <i>join()</i> problems and memory leaks. In some platforms (like Linux) that use glibc the minimum memory footprint of one ithread has been reduced by several hundred kilobytes.</p>
<dt>threads::shared</p>
<dd> Many memory leaks have been fixed.</p>
<dt>Unicode::Collate</p>
<dd>
<dt>Unicode::Normalize</p>
<dd>
<dt>Win32::GetFolderPath</p>
<dd>
<dt>Win32::GetOSVersion</p>
<dd> Now returns extra information.</dl>
<h2>Utility Changes</h2>
<p> The <tt>&quot;h2xs&quot;</tt> utility now produces a more modern layout: <i>Foo-Bar/lib/Foo/Bar.pm</i> instead of <i>Foo/Bar/Bar.pm</i>. Also, the boilerplate test is now called <i>t/Foo-Bar.t</i> instead of <i>t/1.t</i>. </p>
<p> The Perl debugger (<i>lib/perl5db.pl</i>) has now been extensively documented and bugs found while documenting have been fixed. </p>
<p> <tt>&quot;perldoc&quot;</tt> has been rewritten from scratch to be more robust and feature rich. </p>
<p> <tt>&quot;perlcc -B&quot;</tt> works now at least somewhat better, while <tt>&quot;perlcc -c&quot;</tt> is rather more broken. (The Perl compiler suite as a whole continues to be experimental.)</p>
<h2>New Documentation</h2>
<p> perl573delta has been added to list the differences between the (now quite obsolete) development releases 5.7.2 and 5.7.3. </p>
<p> perl58delta and perl581delta have been added: these are the perldeltas of 5.8.0 and 5.8.1, detailing the differences respectively between 5.6.0 and 5.8.0, and between 5.8.0 and 5.8.1. </p>
<p> perlartistic has been added: it is the Artistic License in pod format, making it easier for modules to refer to it. </p>
<p> perlcheat has been added: it is a Perl cheat sheet. </p>
<p> perlgpl has been added: it is the <font SIZE="-1">GNU</font> General Public License in pod format, making it easier for modules to refer to it. </p>
<p> perlmacosx has been added to tell about the installation and use of Perl in Mac <font SIZE="-1">OS</font> X. </p>
<p> perlos400 has been added to tell about the installation and use of Perl in <font SIZE="-1">OS/400</font> <font SIZE="-1">PASE</font>. </p>
<p> perlreref has been added: it is a regular expressions quick reference.</p>
<h2>Installation and Configuration Improvements</h2>
<p> The Unix standard Perl location, <i>/usr/bin/perl</i>, is no longer overwritten by default if it exists. This change was very prudent because so many Unix vendors already provide a <i>/usr/bin/perl</i>, but simultaneously many system utilities may depend on that exact version of Perl, so better not to overwrite it. </p>
<p> One can now specify installation directories for site and vendor man and <font SIZE="-1">HTML</font> pages, and site and vendor scripts. See <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i>. </p>
<p> One can now specify a destination directory for Perl installation by specifying the <font SIZE="-1">DESTDIR</font> variable for <tt>&quot;make install&quot;</tt>. (This feature is slightly different from the previous <tt>&quot;Configure -Dinstallprefix=...&quot;</tt>.) See <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i>. </p>
<p> gcc versions 3.x introduced a new warning that caused a lot of noise during Perl compilation: <tt>&quot;gcc -Ialreadyknowndirectory (warning: changing search order)&quot;</tt>. This warning has now been avoided by Configure weeding out such directories before the compilation. </p>
<p> One can now build subsets of Perl core modules by using the Configure flags <tt>&quot;-Dnoextensions=...&quot;</tt> and <tt>&quot;-Donlyextensions=...&quot;</tt>, see <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i>.</p>
<h3>Platform-specific enhancements</h3>
<p> In Cygwin Perl can now be built with threads (<tt>&quot;Configure -Duseithreads&quot;</tt>). This works with both Cygwin 1.3.22 and Cygwin 1.5.3. </p>
<p> In newer FreeBSD releases Perl 5.8.0 compilation failed because of trying to use <i>malloc.h</i>, which in FreeBSD is just a dummy file, and a fatal error to even try to use. Now <i>malloc.h</i> is not used. </p>
<p> Perl is now known to build also in Hitachi HI-UXMPP. </p>
<p> Perl is now known to build again in LynxOS. </p>
<p> Mac <font SIZE="-1">OS</font> X now installs with Perl version number embedded in installation directory names for easier upgrading of user-compiled Perl, and the installation directories in general are more standard. In other words, the default installation no longer breaks the Apple-provided Perl. On the other hand, with <tt>&quot;Configure -Dprefix=/usr&quot;</tt> you can now really replace the Apple-supplied Perl (<code>please be careful</code>). </p>
<p> Mac <font SIZE="-1">OS</font> X now builds Perl statically by default. This change was done mainly for faster startup times. The Apple-provided Perl is still dynamically linked and shared, and you can enable the sharedness for your own Perl builds by <tt>&quot;Configure -Duseshrplib&quot;</tt>. </p>
<p> Perl has been ported to <font SIZE="-1">IBM</font>&#8216;s <font SIZE="-1">OS/400</font> <font SIZE="-1">PASE</font> environment. The best way to build a Perl for <font SIZE="-1">PASE</font> is to use an <font SIZE="-1">AIX</font> host as a cross-compilation environment. See <font SIZE="-1">README</font>.os400. </p>
<p> Yet another cross-compilation option has been added: now Perl builds on OpenZaurus, an Linux distribution based on Mandrake + Embedix for the Sharp Zaurus <font SIZE="-1">PDA</font>. See the Cross/README file. </p>
<p> Tru64 when using gcc 3 drops the optimisation for <i>toke.c</i> to <tt>&quot;-O2&quot;</tt> because of gigantic memory use with the default <tt>&quot;-O3&quot;</tt>. </p>
<p> Tru64 can now build Perl with the newer Berkeley DBs. </p>
<p> Building Perl on WinCE has been much enhanced, see <i></i><font SIZE="-1"><i>README</i></font><i>.ce</i> and <i></i><font SIZE="-1"><i>README</i></font><i>.perlce</i>.</p>
<h2>Selected Bug Fixes</h2>
<h3>Closures, eval and lexicals</h3>
<p> There have been many fixes in the area of anonymous subs, lexicals and closures. Although this means that Perl is now more &#8220;correct&#8221;, it is possible that some existing code will break that happens to rely on the faulty behaviour. In practice this is unlikely unless your code contains a very complex nesting of anonymous subs, evals and lexicals.</p>
<h3>Generic fixes</h3>
<p> If an input filehandle is marked <tt>&quot;:utf8&quot;</tt> and Perl sees illegal <font SIZE="-1">UTF-8</font> coming in when doing <tt>&quot;&lt;FH&gt;&quot;</tt>, if warnings are enabled a warning is immediately given &#8211; instead of being silent about it and Perl being unhappy about the broken data later. (The <tt>&quot;:encoding(utf8)&quot;</tt> layer also works the same way.) </p>
<p> binmode(<font SIZE="-1">SOCKET</font>, &#8220;:utf8&#8221;) only worked on the input side, not on the output side of the socket. Now it works both ways. </p>
<p> For threaded Perls certain system database functions like <i>getpwent()</i> and <i>getgrent()</i> now grow their result buffer dynamically, instead of failing. This means that at sites with lots of users and groups the functions no longer fail by returning only partial results. </p>
<p> Perl 5.8.0 had accidentally broken the capability for users to define their own uppercase&lt;-&gt;lowercase Unicode mappings (as advertised by the Camel). This feature has been fixed and is also documented better. </p>
<p> In 5.8.0 this </p>
<pre>
        $some_unicode .= &lt;FH&gt;;
</pre>
<p> didn&#8217;t work correctly but instead corrupted the data. This has now been fixed. </p>
<p> Tied methods like <font SIZE="-1">FETCH</font> etc. may now safely access tied values, i.e. resulting in a recursive call to <font SIZE="-1">FETCH</font> etc. Remember to break the recursion, though. </p>
<p> At startup Perl blocks the <font SIZE="-1">SIGFPE</font> signal away since there isn&#8217;t much Perl can do about it. Previously this blocking was in effect also for programs executed from within Perl. Now Perl restores the original <font SIZE="-1">SIGFPE</font> handling routine, whatever it was, before running external programs. </p>
<p> Linenumbers in Perl scripts may now be greater than 65536, or 2**16. (Perl scripts have always been able to be larger than that, it&#8217;s just that the linenumber for reported errors and warnings have &#8220;wrapped around&#8221;.) While scripts that large usually indicate a need to rethink your code a bit, such Perl scripts do exist, for example as results from generated code. Now linenumbers can go all the way to 4294967296, or 2**32.</p>
<h3>Platform-specific fixes</h3>
<p> Linux</p>
<dl>
<dt>&bull;</p>
<dd> Setting <tt>$0</tt> works again (with certain limitations that Perl cannot do much about: see &#8220;$0&#8221; in perlvar)</dl>
<p> HP-UX</p>
<dl>
<dt>&bull;</p>
<dd> Setting <tt>$0</tt> now works.</dl>
<p> <font SIZE="-1">VMS</font></p>
<dl>
<dt>&bull;</p>
<dd> Configuration now tests for the presence of <tt>&quot;poll()&quot;</tt>, and IO::Poll now uses the vendor-supplied function if detected.</p>
<dt>&bull;</p>
<dd> A rare access violation at Perl start-up could occur if the Perl image was installed with privileges or if there was an identifier with the subsystem attribute set in the process&#8217;s rightslist. Either of these circumstances triggered tainting code that contained a pointer bug. The faulty pointer arithmetic has been fixed.</p>
<dt>&bull;</p>
<dd> The length limit on values (not keys) in the <tt>%ENV</tt> hash has been raised from 255 bytes to 32640 bytes (except when the <font SIZE="-1">PERL_ENV_TABLES</font> setting overrides the default use of logical names for <tt>%ENV</tt>). If it is necessary to access these long values from outside Perl, be aware that they are implemented using search list logical names that store the value in pieces, each 255-byte piece (up to 128 of them) being an element in the search list. When doing a lookup in <tt>%ENV</tt> from within Perl, the elements are combined into a single value. The existing VMS-specific ability to access individual elements of a search list logical name via the <tt>$ENV</tt>{&#8216;foo;N&#8217;} syntax (where N is the search list index) is unimpaired.</p>
<dt>&bull;</p>
<dd> The piping implementation now uses local rather than global <font SIZE="-1">DCL</font> symbols for inter-process communication.</p>
<dt>&bull;</p>
<dd> File::Find could become confused when navigating to a relative directory whose name collided with a logical name. This problem has been corrected by adding directory syntax to relative path names, thus preventing logical name translation.</dl>
<p> Win32</p>
<dl>
<dt>&bull;</p>
<dd> A memory leak in the <i>fork()</i> emulation has been fixed.</p>
<dt>&bull;</p>
<dd> The return value of the <i>ioctl()</i> built-in function was accidentally broken in 5.8.0. This has been corrected.</p>
<dt>&bull;</p>
<dd> The internal message loop executed by perl during blocking operations sometimes interfered with messages that were external to Perl. This often resulted in blocking operations terminating prematurely or returning incorrect results, when Perl was executing under environments that could generate Windows messages. This has been corrected.</p>
<dt>&bull;</p>
<dd> Pipes and sockets are now automatically in binary mode.</p>
<dt>&bull;</p>
<dd> The four-argument form of <i>select()</i> did not preserve $! (errno) properly when there were errors in the underlying call. This is now fixed.</p>
<dt>&bull;</p>
<dd> The &#8220;<font SIZE="-1">CR</font> <font SIZE="-1">CR</font> <font SIZE="-1">LF</font>&#8221; problem of has been fixed, binmode(<font SIZE="-1">FH</font>, &#8220;:crlf&#8221;) is now effectively a no-op.</dl>
<h2>New or Changed Diagnostics</h2>
<p> All the warnings related to <i>pack()</i> and <i>unpack()</i> were made more informative and consistent.</p>
<h3>Changed A thread exited while %d threads were running</h3>
<p> The old version </p>
<pre>
    A thread exited while %d other threads were still running
</pre>
<p> was misleading because the &#8220;other&#8221; included also the thread giving the warning.</p>
<h3>Removed Attempt to clear a restricted hash</h3>
<p> It is not illegal to clear a restricted hash, so the warning was removed.</p>
<h3>New Illegal declaration of anonymous subroutine</h3>
<p> You must specify the block of code for <tt>&quot;sub&quot;</tt>.</p>
<h3>Changed Invalid range %s in transliteration operator</h3>
<p> The old version </p>
<pre>
    Invalid [] range &quot;%s&quot; in transliteration operator
</pre>
<p> was simply wrong because there are no &#8220;[] ranges&#8221; in tr///.</p>
<h3>New Missing control char name in 
