---

title: "perl581delta(1)"
name: "perl581delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl581delta/"
description: "perl581delta – what is new for perl v5.8.1"
---

<p> perl581delta - what is new for perl v5.8.1 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.8.0 release and the 5.8.1 release. </p>
<p> If you are upgrading from an earlier release such as 5.6.1, first read the perl58delta, which describes differences between 5.6.0 and 5.8.0. </p>
<p> In case you are wondering about 5.6.1, it was bug-fix-wise rather identical to the development release 5.7.1. Confused? This timeline hopefully helps a bit: it lists the new major releases, their maintenance releases, and the development releases. </p>
<pre><code>          New Maintenance Development
          5.6.0 2000-Mar-22
                               5.7.0 2000-Sep-02
                  5.6.1 2001-Apr-08
                               5.7.1 2001-Apr-09
                               5.7.2 2001-Jul-13
                               5.7.3 2002-Mar-05
          5.8.0 2002-Jul-18
                  5.8.1 2003-Sep-25
</code></pre>
<h2>Incompatible Changes</h2>
<h3>Hash Randomisation</h3>
<p> Mainly due to security reasons, the ``random ordering&#8217;&#8216; of hashes has been made even more random. Previously while the order of hash elements from <code>keys()</code>, <code>values()</code>, and <code>each()</code> was essentially random, it was still repeatable. Now, however, the order varies between different runs of Perl. </p>
<p> <code>Perl has never guaranteed any ordering of the hash keys</code>, and the ordering has already changed several times during the lifetime of Perl 5. Also, the ordering of hash keys has always been, and continues to be, affected by the insertion order. </p>
<p> The added randomness may affect applications. </p>
<p> One possible scenario is when output of an application has included hash data. For example, if you have used the Data::Dumper module to dump data into different files, and then compared the files to see whether the data has changed, now you will have false positives since the order in which hashes are dumped will vary. In general the cure is to sort the keys (or the values); in particular for Data::Dumper to use the <code>&quot;Sortkeys&quot;</code> option. If some particular order is really important, use tied hashes: for example the Tie::IxHash module which by default preserves the order in which the hash elements were added. </p>
<p> More subtle problem is reliance on the order of ``global destruction&#8217;&#8216;. That is what happens at the end of execution: Perl destroys all data structures, including user data. If your destructors (the DESTROY subroutines) have assumed any particular ordering to the global destruction, there might be problems ahead. For example, in a destructor of one object you cannot assume that objects of any other class are still available, unless you hold a reference to them. If the environment variable PERL_DESTRUCT_LEVEL is set to a non-zero value, or if Perl is exiting a spawned thread, it will also destruct the ordinary references and the symbol tables that are no longer in use. You can&#8217;t call a class method or an ordinary function on a class that has been collected that way. </p>
<p> The hash randomisation is certain to reveal hidden assumptions about some particular ordering of hash elements, and outright bugs: it revealed a few bugs in the Perl core and core modules. </p>
<p> To disable the hash randomisation in runtime, set the environment variable PERL_HASH_SEED to 0 (zero) before running Perl (for more information see ``PERL_HASH_SEED&#8217;&#8216; in perlrun), or to disable the feature completely in compile time, compile with <code>&quot;-DNO_HASH_SEED&quot;</code> (see <i></i><i>INSTALL</i><i></i>). </p>
<p> See ``Algorithmic Complexity Attacks&#8217;&#8216; in perlsec for the original rationale behind this change.  </p>
<h3>UTF-8 On Filehandles No Longer Activated By Locale</h3>
<p> In Perl 5.8.0 all filehandles, including the standard filehandles, were implicitly set to be in Unicode UTF-8 if the locale settings indicated the use of UTF-8. This feature caused too many problems, so the feature was turned off and redesigned: see ``Core Enhancements&#8217;&#8216;.  </p>
<h3>Single-number v-strings are no longer v-strings before =&gt;</h3>
<p> The version strings or v-strings (see ``Version Strings&#8217;&#8216; in perldata) feature introduced in Perl 5.6.0 has been a source of some confusion--- especially when the user did not want to use it, but Perl thought it knew better. Especially troublesome has been the feature that before a ``=&gt;&#8216;&#8216; a version string (a ``v&#8217;&#8216; followed by digits) has been interpreted as a v-string instead of a string literal. In other words: </p>
<pre><code>        %h = ( v65 =&gt; 42 );
</code></pre>
<p> has meant since Perl 5.6.0 </p>
<pre><code>        %h = ( 'A' =&gt; 42 );
</code></pre>
<p> (at least in platforms of ASCII progeny) Perl 5.8.1 restores the more natural interpretation </p>
<pre><code>        %h = ( 'v65' =&gt; 42 );
</code></pre>
<p> The multi-number v-strings like v65.66 and 65.66.67 still continue to be v-strings in Perl 5.8.  </p>
<h3>(Win32) The -C Switch Has Been Repurposed</h3>
<p> The -C switch has changed in an incompatible way. The old semantics of this switch only made sense in Win32 and only in the ``use utf8&#8217;&#8216; universe in 5.6.x releases, and do not make sense for the Unicode implementation in 5.8.0. Since this switch could not have been used by anyone, it has been repurposed. The behavior that this switch enabled in 5.6.x releases may be supported in a transparent, data-dependent fashion in a future release. </p>
<p> For the new life of this switch, see ``UTF-8 no longer default under UTF-8 locales&#8217;&#8216;, and ``-C&#8217;&#8216; in perlrun.  </p>
<h3>(Win32) The /d Switch Of cmd.exe</h3>
<p> Perl 5.8.1 uses the /d switch when running the cmd.exe shell internally for <code>system()</code>, backticks, and when opening pipes to external programs. The extra switch disables the execution of AutoRun commands from the registry, which is generally considered undesirable when running external programs. If you wish to retain compatibility with the older behavior, set PERL5SHELL in your environment to <code>&quot;cmd /x/c&quot;</code>.  </p>
<h2>Core Enhancements</h2>
<h3>UTF-8 no longer default under UTF-8 locales</h3>
<p> In Perl 5.8.0 many Unicode features were introduced. One of them was found to be of more nuisance than benefit: the automagic (and silent) ``UTF-8-ification&#8217;&#8216; of filehandles, including the standard filehandles, if the user&#8217;s locale settings indicated use of UTF-8. </p>
<p> For example, if you had <code>&quot;en_US.UTF-8&quot;</code> as your locale, your STDIN and STDOUT were automatically ``UTF-8&#8217;&#8216;, in other words an implicit binmode(..., ``:utf8&#8217;&#8216;) was made. This meant that trying to print, say, <code>chr</code>(0xff), ended up printing the bytes 0xc3 0xbf. Hardly what you had in mind unless you were aware of this feature of Perl 5.8.0. The problem is that the vast majority of people weren&#8217;t: for example in RedHat releases 8 and 9 the <code>default</code> locale setting is UTF-8, so all RedHat users got UTF-8 filehandles, whether they wanted it or not. The pain was intensified by the Unicode implementation of Perl 5.8.0 (still) having nasty bugs, especially related to the use of s/// and tr///. (Bugs that have been fixed in 5.8.1) </p>
<p> Therefore a decision was made to backtrack the feature and change it from implicit silent default to explicit conscious option. The new Perl command line option <code>&quot;-C&quot;</code> and its counterpart environment variable PERL_UNICODE can now be used to control how Perl and Unicode interact at interfaces like I/O and for example the command line arguments. See ``-C&#8217;&#8216; in perlrun and ``PERL_UNICODE&#8217;&#8216; in perlrun for more information.  </p>
<h3>Unsafe signals again available</h3>
<p> In Perl 5.8.0 the so-called ``safe signals&#8217;&#8216; were introduced. This means that Perl no longer handles signals immediately but instead ``between opcodes&#8217;&#8216;, when it is safe to do so. The earlier immediate handling easily could corrupt the internal state of Perl, resulting in mysterious crashes. </p>
<p> However, the new safer model has its problems too. Because now an opcode, a basic unit of Perl execution, is never interrupted but instead let to run to completion, certain operations that can take a long time now really do take a long time. For example, certain network operations have their own blocking and timeout mechanisms, and being able to interrupt them immediately would be nice. </p>
<p> Therefore perl 5.8.1 introduces a ``backdoor&#8217;&#8216; to restore the pre-5.8.0 (pre-5.7.3, really) signal behaviour. Just set the environment variable PERL_SIGNALS to <code>&quot;unsafe&quot;</code>, and the old immediate (and unsafe) signal handling behaviour returns. See ``PERL_SIGNALS&#8217;&#8216; in perlrun and ``Deferred Signals (Safe Signals)&#8216;&#8216; in perlipc. </p>
<p> In completely unrelated news, you can now use safe signals with POSIX::SigAction. See ``POSIX::SigAction&#8217;&#8216; in POSIX.  </p>
<h3>Tied Arrays with Negative Array Indices</h3>
<p> Formerly, the indices passed to <code>&quot;FETCH&quot;</code>, <code>&quot;STORE&quot;</code>, <code>&quot;EXISTS&quot;</code>, and <code>&quot;DELETE&quot;</code> methods in tied array class were always non-negative. If the actual argument was negative, Perl would call FETCHSIZE implicitly and add the result to the index before passing the result to the tied array method. This behaviour is now optional. If the tied array class contains a package variable named <code>$NEGATIVE_INDICES</code> which is set to a true value, negative values will be passed to <code>&quot;FETCH&quot;</code>, <code>&quot;STORE&quot;</code>, <code>&quot;EXISTS&quot;</code>, and <code>&quot;DELETE&quot;</code> unchanged.  </p>
<h3>local ${$x}</h3>
<p> The syntaxes </p>
<pre><code>        local ${$x}
        local @{$x}
        local %{$x}
</code></pre>
<p> now do localise variables, given that the <code>$x</code> is a valid variable name.  </p>
<h3>Unicode Character Database 4.0.0</h3>
<p> The copy of the Unicode Character Database included in Perl 5.8 has been updated to 4.0.0 from 3.2.0. This means for example that the Unicode character properties are as in Unicode 4.0.0.  </p>
<h3>Deprecation Warnings</h3>
<p> There is one new feature deprecation. Perl 5.8.0 forgot to add some deprecation warnings, these warnings have now been added. Finally, a reminder of an impending feature removal. </p>
<p> <i>(Reminder) Pseudo-hashes are deprecated (really)</i> </p>
<p> Pseudo-hashes were deprecated in Perl 5.8.0 and will be removed in Perl 5.10.0, see perl58delta for details. Each attempt to access pseudo-hashes will trigger the warning <code>&quot;Pseudo-hashes are deprecated&quot;</code>. If you really want to continue using pseudo-hashes but not to see the deprecation warnings, use: </p>
<pre><code>    no warnings 'deprecated';
</code></pre>
<p> Or you can continue to use the fields pragma, but please don&#8217;t expect the data structures to be pseudohashes any more. </p>
<p> <i>(Reminder) 5.005-style threads are deprecated (really)</i> </p>
<p> 5.005-style threads (activated by <code>&quot;use Thread;&quot;</code>) were deprecated in Perl 5.8.0 and will be removed after Perl 5.8, see perl58delta for details. Each 5.005-style thread creation will trigger the warning <code>&quot;5.005 threads are deprecated&quot;</code>. If you really want to continue using the 5.005 threads but not to see the deprecation warnings, use: </p>
<pre><code>    no warnings 'deprecated';
</code></pre>
<p> <i>(Reminder) The $* variable is deprecated (really)</i> </p>
<p> The <code>$*</code> variable controlling multi-line matching has been deprecated and will be removed after 5.8. The variable has been deprecated for a long time, and a deprecation warning <code>&quot;Use of $* is deprecated&quot;</code> is given, now the variable will just finally be removed. The functionality has been supplanted by the <code>&quot;/s&quot;</code> and <code>&quot;/m&quot;</code> modifiers on pattern matching. If you really want to continue using the <code>$*</code>-variable but not to see the deprecation warnings, use: </p>
<pre><code>    no warnings 'deprecated';
</code></pre>
<h3>Miscellaneous Enhancements</h3>
<p> <code>&quot;map&quot;</code> in void context is no longer expensive. <code>&quot;map&quot;</code> is now context aware, and will not construct a list if called in void context. </p>
<p> If a socket gets closed by the server while printing to it, the client now gets a SIGPIPE. While this new feature was not planned, it fell naturally out of PerlIO changes, and is to be considered an accidental feature. </p>
<p> PerlIO::get_layers(FH) returns the names of the PerlIO layers active on a filehandle. </p>
<p> PerlIO::via layers can now have an optional UTF8 method to indicate whether the layer wants to ``auto-:utf8&#8217;&#8216; the stream. </p>
<p> <code>utf8::is_utf8()</code> has been added as a quick way to test whether a scalar is encoded internally in UTF-8 (Unicode).  </p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules And Pragmata</h3>
<p> The following modules and pragmata have been updated since Perl 5.8.0: </p>
<dl>
<dt>base</dt>
<dd>  </dd>
<dt>B::Bytecode</dt>
<dd> <p> In much better shape than it used to be. Still far from perfect, but maybe worth a try. </p>
 </dd>
<dt>B::Concise</dt>
<dd>  </dd>
<dt>B::Deparse</dt>
<dd>  </dd>
<dt>Benchmark</dt>
<dd> <p> An optional feature, <code>&quot;:hireswallclock&quot;</code>, now allows for high resolution wall clock times (uses Time::HiRes). </p>
 </dd>
<dt>ByteLoader</dt>
<dd> <p> See B::Bytecode. </p>
 </dd>
<dt>bytes</dt>
<dd> <p> Now has bytes::substr. </p>
 </dd>
<dt>CGI</dt>
<dd>  </dd>
<dt>charnames</dt>
<dd> <p> One can now have custom character name aliases. </p>
 </dd>
<dt>CPAN</dt>
<dd> <p> There is now a simple command line frontend to the CPAN.pm module called <i>cpan</i>. </p>
 </dd>
<dt>Data::Dumper</dt>
<dd> <p> A new option, Pair, allows choosing the separator between hash keys and values. </p>
 </dd>
<dt>DB_File</dt>
<dd>  </dd>
<dt>Devel::PPPort</dt>
<dd>  </dd>
<dt>Digest::MD5</dt>
<dd>  </dd>
<dt>Encode</dt>
<dd> <p> Significant updates on the encoding pragma functionality (tr/// and the DATA filehandle, formats). </p>
<p> If a filehandle has been marked as to have an encoding, unmappable characters are detected already during input, not later (when the corrupted data is being used). </p>
<p> The ISO 8859-6 conversion table has been corrected (the 0x30..0x39 erroneously mapped to U+0660..U+0669, instead of U+0030..U+0039). The GSM 03.38 conversion did not handle escape sequences correctly. The UTF-7 encoding has been added (making Encode feature-complete with Unicode::String). </p>
 </dd>
<dt>fields</dt>
<dd>  </dd>
<dt>libnet</dt>
<dd>  </dd>
<dt>Math::BigInt</dt>
<dd> <p> A lot of bugs have been fixed since v1.60, the version included in Perl v5.8.0. Especially noteworthy are the bug in Calc that caused div and mod to fail for some large values, and the fixes to the handling of bad inputs. </p>
<p> Some new features were added, e.g. the <code>broot()</code> method, you can now pass parameters to <code>config()</code> to change some settings at runtime, and it is now possible to trap the creation of NaN and infinity. </p>
<p> As usual, some optimizations took place and made the math overall a tad faster. In some cases, quite a lot faster, actually. Especially alternative libraries like Math::BigInt::GMP benefit from this. In addition, a lot of the quite clunky routines like <code>fsqrt()</code> and <code>flog()</code> are now much much faster. </p>
 </dd>
<dt>MIME::Base64</dt>
<dd>  </dd>
<dt>NEXT</dt>
<dd> <p> Diamond inheritance now works. </p>
 </dd>
<dt>Net::Ping</dt>
<dd>  </dd>
<dt>PerlIO::scalar</dt>
<dd> <p> Reading from non-string scalars (like the special variables, see perlvar) now works. </p>
 </dd>
<dt>podlators</dt>
<dd>  </dd>
<dt>Pod::LaTeX</dt>
<dd>  </dd>
<dt>PodParsers</dt>
<dd>  </dd>
<dt>Pod::Perldoc</dt>
<dd> <p> Complete rewrite. As a side-effect, no longer refuses to startup when run by root. </p>
 </dd>
<dt>Scalar::Util</dt>
<dd> <p> New utilities: refaddr, isvstring, looks_like_number, set_prototype. </p>
 </dd>
<dt>Storable</dt>
<dd> <p> Can now store code references (via B::Deparse, so not foolproof). </p>
 </dd>
<dt>strict</dt>
<dd> <p> Earlier versions of the strict pragma did not check the parameters implicitly passed to its ``import&#8217;&#8216; (use) and ``unimport&#8217;&#8216; (no) routine. This caused the false idiom such as: </p>
<pre><code>        use strict qw(@ISA);
        @ISA = qw(Foo);
</code></pre>
<p> This however (probably) raised the false expectation that the strict refs, vars and subs were being enforced (and that <code>@ISA</code> was somehow ``declared&#8217;&#8216;). But the strict refs, vars, and subs are <code>not</code> enforced when using this false idiom. </p>
<p> Starting from Perl 5.8.1, the above <code>will</code> cause an error to be raised. This may cause programs which used to execute seemingly correctly without warnings and errors to fail when run under 5.8.1. This happens because </p>
<pre><code>        use strict qw(@ISA);
</code></pre>
<p> will now fail with the error: </p>
<pre><code>        Unknown 'strict' tag(s) '@ISA'
</code></pre>
<p> The remedy to this problem is to replace this code with the correct idiom: </p>
<pre><code>        use strict;
        use vars qw(@ISA);
        @ISA = qw(Foo);
</code></pre>
 </dd>
<dt>Term::ANSIcolor</dt>
<dd>  </dd>
<dt>Test::Harness</dt>
<dd> <p> Now much more picky about extra or missing output from test scripts. </p>
 </dd>
<dt>Test::More</dt>
<dd>  </dd>
<dt>Test::Simple</dt>
<dd>  </dd>
<dt>Text::Balanced</dt>
<dd>  </dd>
<dt>Time::HiRes</dt>
<dd> <p> Use of <code>nanosleep()</code>, if available, allows mixing subsecond sleeps with alarms. </p>
 </dd>
<dt>threads</dt>
<dd> <p> Several fixes, for example for <code>join()</code> problems and memory leaks. In some platforms (like Linux) that use glibc the minimum memory footprint of one ithread has been reduced by several hundred kilobytes. </p>
 </dd>
<dt>threads::shared</dt>
<dd> <p> Many memory leaks have been fixed. </p>
 </dd>
<dt>Unicode::Collate</dt>
<dd>  </dd>
<dt>Unicode::Normalize</dt>
<dd>  </dd>
<dt>Win32::GetFolderPath</dt>
<dd>  </dd>
<dt>Win32::GetOSVersion</dt>
<dd> <p> Now returns extra information. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<p> The <code>&quot;h2xs&quot;</code> utility now produces a more modern layout: <i>Foo-Bar/lib/Foo/Bar.pm</i> instead of <i>Foo/Bar/Bar.pm</i>. Also, the boilerplate test is now called <i>t/Foo-Bar.t</i> instead of <i>t/1.t</i>. </p>
<p> The Perl debugger (<i>lib/perl5db.pl</i>) has now been extensively documented and bugs found while documenting have been fixed. </p>
<p> <code>&quot;perldoc&quot;</code> has been rewritten from scratch to be more robust and feature rich. </p>
<p> <code>&quot;perlcc -B&quot;</code> works now at least somewhat better, while <code>&quot;perlcc -c&quot;</code> is rather more broken. (The Perl compiler suite as a whole continues to be experimental.)  </p>
<h2>New Documentation</h2>
<p> perl573delta has been added to list the differences between the (now quite obsolete) development releases 5.7.2 and 5.7.3. </p>
<p> perl58delta has been added: it is the perldelta of 5.8.0, detailing the differences between 5.6.0 and 5.8.0. </p>
<p> perlartistic has been added: it is the Artistic License in pod format, making it easier for modules to refer to it. </p>
<p> perlcheat has been added: it is a Perl cheat sheet. </p>
<p> perlgpl has been added: it is the GNU General Public License in pod format, making it easier for modules to refer to it. </p>
<p> perlmacosx has been added to tell about the installation and use of Perl in Mac OS X. </p>
<p> perlos400 has been added to tell about the installation and use of Perl in OS/400 PASE. </p>
<p> perlreref has been added: it is a regular expressions quick reference.  </p>
<h2>Installation and Configuration Improvements</h2>
<p> The Unix standard Perl location, <i>/usr/bin/perl</i>, is no longer overwritten by default if it exists. This change was very prudent because so many Unix vendors already provide a <i>/usr/bin/perl</i>, but simultaneously many system utilities may depend on that exact version of Perl, so better not to overwrite it. </p>
<p> One can now specify installation directories for site and vendor man and HTML pages, and site and vendor scripts. See <i></i><i>INSTALL</i><i></i>. </p>
<p> One can now specify a destination directory for Perl installation by specifying the DESTDIR variable for <code>&quot;make install&quot;</code>. (This feature is slightly different from the previous <code>&quot;Configure -Dinstallprefix=...&quot;</code>.) See <i></i><i>INSTALL</i><i></i>. </p>
<p> gcc versions 3.x introduced a new warning that caused a lot of noise during Perl compilation: <code>&quot;gcc -Ialreadyknowndirectory (warning: changing search order)&quot;</code>. This warning has now been avoided by Configure weeding out such directories before the compilation. </p>
<p> One can now build subsets of Perl core modules by using the Configure flags <code>&quot;-Dnoextensions=...&quot;</code> and <code>&quot;-Donlyextensions=...&quot;</code>, see <i></i><i>INSTALL</i><i></i>.  </p>
<h3>Platform-specific enhancements</h3>
<p> In Cygwin Perl can now be built with threads (<code>&quot;Configure -Duseithreads&quot;</code>). This works with both Cygwin 1.3.22 and Cygwin 1.5.3. </p>
<p> In newer FreeBSD releases Perl 5.8.0 compilation failed because of trying to use <i>malloc.h</i>, which in FreeBSD is just a dummy file, and a fatal error to even try to use. Now <i>malloc.h</i> is not used. </p>
<p> Perl is now known to build also in Hitachi HI-UXMPP. </p>
<p> Perl is now known to build again in LynxOS. </p>
<p> Mac OS X now installs with Perl version number embedded in installation directory names for easier upgrading of user-compiled Perl, and the installation directories in general are more standard. In other words, the default installation no longer breaks the Apple-provided Perl. On the other hand, with <code>&quot;Configure -Dprefix=/usr&quot;</code> you can now really replace the Apple-supplied Perl (<code>please be careful</code>). </p>
<p> Mac OS X now builds Perl statically by default. This change was done mainly for faster startup times. The Apple-provided Perl is still dynamically linked and shared, and you can enable the sharedness for your own Perl builds by <code>&quot;Configure -Duseshrplib&quot;</code>. </p>
<p> Perl has been ported to IBM&#8216;s OS/400 PASE environment. The best way to build a Perl for PASE is to use an AIX host as a cross-compilation environment. See README.os400. </p>
<p> Yet another cross-compilation option has been added: now Perl builds on OpenZaurus, a Linux distribution based on Mandrake + Embedix for the Sharp Zaurus PDA. See the Cross/README file. </p>
<p> Tru64 when using gcc 3 drops the optimisation for <i>toke.c</i> to <code>&quot;-O2&quot;</code> because of gigantic memory use with the default <code>&quot;-O3&quot;</code>. </p>
<p> Tru64 can now build Perl with the newer Berkeley DBs. </p>
<p> Building Perl on WinCE has been much enhanced, see <i></i><i>README</i><i>.ce</i> and <i></i><i>README</i><i>.perlce</i>.  </p>
<h2>Selected Bug Fixes</h2>
<h3>Closures, eval and lexicals</h3>
<p> There have been many fixes in the area of anonymous subs, lexicals and closures. Although this means that Perl is now more ``correct&#8217;&#8216;, it is possible that some existing code will break that happens to rely on the faulty behaviour. In practice this is unlikely unless your code contains a very complex nesting of anonymous subs, evals and lexicals.  </p>
<h3>Generic fixes</h3>
<p> If an input filehandle is marked <code>&quot;:utf8&quot;</code> and Perl sees illegal UTF-8 coming in when doing <code>&quot;&lt;FH&gt;&quot;</code>, if warnings are enabled a warning is immediately given - instead of being silent about it and Perl being unhappy about the broken data later. (The <code>&quot;:encoding(utf8)&quot;</code> layer also works the same way.) </p>
<p> binmode(SOCKET, ``:utf8&#8217;&#8216;) only worked on the input side, not on the output side of the socket. Now it works both ways. </p>
<p> For threaded Perls certain system database functions like <code>getpwent()</code> and <code>getgrent()</code> now grow their result buffer dynamically, instead of failing. This means that at sites with lots of users and groups the functions no longer fail by returning only partial results. </p>
<p> Perl 5.8.0 had accidentally broken the capability for users to define their own uppercase&lt;-&gt;lowercase Unicode mappings (as advertised by the Camel). This feature has been fixed and is also documented better. </p>
<p> In 5.8.0 this </p>
<pre><code>        $some_unicode .= &lt;FH&gt;;
</code></pre>
<p> didn&#8217;t work correctly but instead corrupted the data. This has now been fixed. </p>
<p> Tied methods like FETCH etc. may now safely access tied values, i.e. resulting in a recursive call to FETCH etc. Remember to break the recursion, though. </p>
<p> At startup Perl blocks the SIGFPE signal away since there isn&#8217;t much Perl can do about it. Previously this blocking was in effect also for programs executed from within Perl. Now Perl restores the original SIGFPE handling routine, whatever it was, before running external programs. </p>
<p> Linenumbers in Perl scripts may now be greater than 65536, or 2**16. (Perl scripts have always been able to be larger than that, it&#8217;s just that the linenumber for reported errors and warnings have ``wrapped around&#8217;&#8216;.) While scripts that large usually indicate a need to rethink your code a bit, such Perl scripts do exist, for example as results from generated code. Now linenumbers can go all the way to 4294967296, or 2**32.  </p>
<h3>Platform-specific fixes</h3>
<p> Linux </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Setting <code>$0</code> works again (with certain limitations that Perl cannot do much about: see ``$0&#8217;&#8216; in perlvar) </p>
 </dd></dl>
<p> HP-UX </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Setting <code>$0</code> now works. </p>
 </dd></dl>
<p> VMS </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Configuration now tests for the presence of <code>&quot;poll()&quot;</code>, and IO::Poll now uses the vendor-supplied function if detected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A rare access violation at Perl start-up could occur if the Perl image was installed with privileges or if there was an identifier with the subsystem attribute set in the process&#8217;s rightslist. Either of these circumstances triggered tainting code that contained a pointer bug. The faulty pointer arithmetic has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The length limit on values (not keys) in the <code>%ENV</code> hash has been raised from 255 bytes to 32640 bytes (except when the PERL_ENV_TABLES setting overrides the default use of logical names for <code>%ENV</code>). If it is necessary to access these long values from outside Perl, be aware that they are implemented using search list logical names that store the value in pieces, each 255-byte piece (up to 128 of them) being an element in the search list. When doing a lookup in <code>%ENV</code> from within Perl, the elements are combined into a single value. The existing VMS-specific ability to access individual elements of a search list logical name via the <code>$ENV</code>{&#8216;foo;N&#8217;} syntax (where N is the search list index) is unimpaired. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The piping implementation now uses local rather than global DCL symbols for inter-process communication. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Find could become confused when navigating to a relative directory whose name collided with a logical name. This problem has been corrected by adding directory syntax to relative path names, thus preventing logical name translation. </p>
 </dd></dl>
<p> Win32 </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A memory leak in the <code>fork()</code> emulation has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The return value of the <code>ioctl()</code> built-in function was accidentally broken in 5.8.0. This has been corrected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The internal message loop executed by perl during blocking operations sometimes interfered with messages that were external to Perl. This often resulted in blocking operations terminating prematurely or returning incorrect results, when Perl was executing under environments that could generate Windows messages. This has been corrected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pipes and sockets are now automatically in binary mode. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The four-argument form of <code>select()</code> did not preserve $! (errno) properly when there were errors in the underlying call. This is now fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ``CR CR LF&#8217;&#8216; problem of has been fixed, binmode(FH, ``:crlf&#8217;&#8216;) is now effectively a no-op. </p>
 </dd></dl>
<h2>New or Changed Diagnostics</h2>
<p> All the warnings related to <code>pack()</code> and <code>unpack()</code> were made more informative and consistent.  </p>
<h3>Changed A thread exited while %d threads were running</h3>
<p> The old version </p>
<pre><code>    A thread exited while %d other threads were still running
</code></pre>
<p> was misleading because the ``other&#8217;&#8216; included also the thread giving the warning.  </p>
<h3>Removed Attempt to clear a restricted hash</h3>
<p> It is not illegal to clear a restricted hash, so the warning was removed.  </p>
<h3>New Illegal declaration of anonymous subroutine</h3>
<p> You must specify the block of code for <code>&quot;sub&quot;</code>.  </p>
<h3>Changed Invalid range %s in transliteration operator</h3>
<p> The old version </p>
<pre><code>    Invalid [] range &quot;%s&quot; in transliteration operator
</code></pre>
<p> was simply wrong because there are no ``[] ranges&#8217;&#8216; in tr///.  </p>
<h3>New Missing control char name in \c</h3>
<p> Self-explanatory.  </p>
<h3>New Newline in left-justified string for %s</h3>
<p> The padding spaces would appear after the newline, which is probably not what you had in mind.  </p>
<h3>New Possible precedence problem on bitwise %c operator</h3>
<p> If you think this </p>
<pre><code>    $x &amp; $y == 0
</code></pre>
<p> tests whether the bitwise AND of <code>$x</code> and <code>$y</code> is zero, you will like this warning.  </p>
<h3>New Pseudo-hashes are deprecated</h3>
<p> This warning should have been already in 5.8.0, since they are.  </p>
<code></code><h3>New read() on %s filehandle %s</h3>
<p> You cannot <code>read()</code> (or <code>sysread()</code>) from a closed or unopened filehandle.  </p>
<h3>New 5.005 threads are deprecated</h3>
<p> This warning should have been already in 5.8.0, since they are.  </p>
<h3>New Tied variable freed while still in use</h3>
<p> Something pulled the plug on a live tied variable, Perl plays safe by bailing out.  </p>
<h3>New To%s: illegal mapping '%s'</h3>
<p> An illegal user-defined Unicode casemapping was specified.  </p>
<h3>New Use of freed value in iteration</h3>
<p> Something modified the values being iterated over. This is not good.  </p>
<h2>Changed Internals</h2>
<p> These news matter to you only if you either write XS code or like to know about or hack Perl internals (using Devel::Peek or any of the <code>&quot;B::&quot;</code> modules counts), or like to run Perl with the <code>&quot;-D&quot;</code> option. </p>
<p> The embedding examples of perlembed have been reviewed to be up to date and consistent: for example, the correct use of <code>PERL_SYS_INIT3</code><code>()</code> and <code>PERL_SYS_TERM</code><code>()</code>. </p>
<p> Extensive reworking of the pad code (the code responsible for lexical variables) has been conducted by Dave Mitchell. </p>
<p> Extensive work on the v-strings by John Peacock. </p>
<p> UTF-8 length and position cache: to speed up the handling of Unicode (UTF-8) scalars, a cache was introduced. Potential problems exist if an extension bypasses the official APIs and directly modifies the PV of an SV: the UTF-8 cache does not get cleared as it should. </p>
<p> APIs obsoleted in Perl 5.8.0, like sv_2pv, sv_catpvn, sv_catsv, sv_setsv, are again available. </p>
<p> Certain Perl core C APIs like cxinc and regatom are no longer available at all to code outside the Perl core of the Perl core extensions. This is intentional. They never should have been available with the shorter names, and if you application depends on them, you should (be ashamed and) contact perl5-porters to discuss what are the proper APIs. </p>
<p> Certain Perl core C APIs like <code>&quot;Perl_list&quot;</code> are no longer available without their <code>&quot;Perl_&quot;</code> prefix. If your XS module stops working because some functions cannot be found, in many cases a simple fix is to add the <code>&quot;Perl_&quot;</code> prefix to the function and the thread context <code>&quot;aTHX_&quot;</code> as the first argument of the function call. This is also how it should always have been done: letting the Perl_-less forms to leak from the core was an accident. For cleaner embedding you can also force this for all APIs by defining at compile time the cpp define PERL_NO_SHORT_NAMES. </p>
<p> <code>Perl_save_bool()</code> has been added. </p>
<p> Regexp objects (those created with <code>&quot;qr&quot;</code>) now have S-magic rather than R-magic. This fixed regexps of the form /...(??{...;$x})/ to no longer ignore changes made to <code>$x</code>. The S-magic avoids dropping the caching optimization and making (??{...}) constructs obscenely slow (and consequently useless). See also ``Magic Variables&#8217;&#8216; in perlguts. Regexp::Copy was affected by this change. </p>
<p> The Perl internal debugging macros <code>DEBUG</code><code>()</code> and <code>DEB</code><code>()</code> have been renamed to <code>PERL_DEBUG</code><code>()</code> and <code>PERL_DEB</code><code>()</code> to avoid namespace conflicts. </p>
<p> <code>&quot;-DL&quot;</code> removed (the leaktest had been broken and unsupported for years, use alternative debugging mallocs or tools like valgrind and Purify). </p>
<p> Verbose modifier <code>&quot;v&quot;</code> added for <code>&quot;-DXv&quot;</code> and <code>&quot;-Dsv&quot;</code>, see perlrun.  </p>
<h2>New Tests</h2>
<p> In Perl 5.8.0 there were about 69000 separate tests in about 700 test files, in Perl 5.8.1 there are about 77000 separate tests in about 780 test files. The exact numbers depend on the Perl configuration and on the operating system platform.  </p>
<h2>Known Problems</h2>
<p> The hash randomisation mentioned in ``Incompatible Changes&#8217;&#8216; is definitely problematic: it will wake dormant bugs and shake out bad assumptions. </p>
<p> If you want to use mod_perl 2.x with Perl 5.8.1, you will need mod_perl-1.99_10 or higher. Earlier versions of mod_perl 2.x do not work with the randomised hashes. (mod_perl 1.x works fine.) You will also need Apache::Test 1.04 or higher. </p>
<p> Many of the rarer platforms that worked 100% or pretty close to it with perl 5.8.0 have been left a little bit untended since their maintainers have been otherwise busy lately, and therefore there will be more failures on those platforms. Such platforms include Mac OS Classic, IBM z/OS (and other EBCDIC platforms), and NetWare. The most common Perl platforms (Unix and Unix-like, Microsoft platforms, and VMS) have large enough testing and expert population that they are doing well.  </p>
<h3>Tied hashes in scalar context</h3>
<p> Tied hashes do not currently return anything useful in scalar context, for example when used as boolean tests: </p>
<pre><code>        if (%tied_hash) { ... }
</code></pre>
<p> The current nonsensical behaviour is always to return false, regardless of whether the hash is empty or has elements. </p>
<p> The root cause is that there is no interface for the implementors of tied hashes to implement the behaviour of a hash in scalar context.  </p>
<h3>Net::Ping 450_service and 510_ping_udp failures</h3>
<p> The subtests 9 and 18 of lib/Net/Ping/t/450_service.t, and the subtest 2 of lib/Net/Ping/t/510_ping_udp.t might fail if you have an unusual networking setup. For example in the latter case the test is trying to send a UDP ping to the IP address 127.0.0.1.  </p>
<h3>B::C</h3>
<p> The C-generating compiler backend B::C (the frontend being <code>&quot;perlcc -c&quot;</code>) is even more broken than it used to be because of the extensive lexical variable changes. (The good news is that B::Bytecode and ByteLoader are better than they used to be.)  </p>
<h2>Platform Specific Problems</h2>
<h3>EBCDIC Platforms</h3>
<p> IBM z/OS and other EBCDIC platforms continue to be problematic regarding Unicode support. Many Unicode tests are skipped when they really should be fixed.  </p>
<h3>Cygwin 1.5 problems</h3>
<p> In Cygwin 1.5 the <i>io/tell</i> and <i>op/sysio</i> tests have failures for some yet unknown reason. In 1.5.5 the threads tests stress_cv, stress_re, and stress_string are failing unless the environment variable PERLIO is set to ``perlio&#8217;&#8216; (which makes also the io/tell failure go away). </p>
<p> Perl 5.8.1 does build and work well with Cygwin 1.3: with (uname -a) <code>&quot;CYGWIN_NT-5.0 ... 1.3.22(0.78/3/2) 2003-03-18 09:20 i686 ...&quot;</code> a 100% ``make test&#8217;&#8216; was achieved with <code>&quot;Configure -des -Duseithreads&quot;</code>.  </p>
<h3>HP-UX: HP cc warnings about sendfile and sendpath</h3>
<p> With certain HP C compiler releases (e.g. B.11.11.02) you will get many warnings like this (lines wrapped for easier reading): </p>
<pre><code>  cc: &quot;/usr/include/sys/socket.h&quot;, line 504: warning 562:
    Redeclaration of &quot;sendfile&quot; with a different storage class specifier:
      &quot;sendfile&quot; will have internal linkage.
  cc: &quot;/usr/include/sys/socket.h&quot;, line 505: warning 562:
    Redeclaration of &quot;sendpath&quot; with a different storage class specifier:
      &quot;sendpath&quot; will have internal linkage.
</code></pre>
<p> The warnings show up both during the build of Perl and during certain lib/ExtUtils tests that invoke the C compiler. The warning, however, is not serious and can be ignored.  </p>
<h3>IRIX: t/uni/tr_7jis.t falsely failing</h3>
<p> The test t/uni/tr_7jis.t is known to report failure under &#8216;make test&#8217; or the test harness with certain releases of IRIX (at least IRIX 6.5 and MIPSpro Compilers Version 7.3.1.1m), but if run manually the test fully passes.  </p>
<h3>Mac OS X: no usemymalloc</h3>
<p> The Perl malloc (<code>&quot;-Dusemymalloc&quot;</code>) does not work at all in Mac OS X. This is not that serious, though, since the native malloc works just fine.  </p>
<h3>Tru64: No threaded builds with GNU cc (gcc)</h3>
<p> In the latest Tru64 releases (e.g. v5.1B or later) gcc cannot be used to compile a threaded Perl (-Duseithreads) because the system <code>&quot;&lt;pthread.h&gt;&quot;</code> file doesn&#8217;t know about gcc.  </p>
<h3>Win32: sysopen, sysread, syswrite</h3>
<p> As of the 5.8.0 release, <code>sysopen()</code>/<code>sysread()</code>/<code>syswrite()</code> do not behave like they used to in 5.6.1 and earlier with respect to ``text&#8217;&#8216; mode. These built-ins now always operate in ``binary&#8217;&#8216; mode (even if <code>sysopen()</code> was passed the O_TEXT flag, or if <code>binmode()</code> was used on the file handle). Note that this issue should only make a difference for disk files, as sockets and pipes have always been in ``binary&#8217;&#8216; mode in the Windows port. As this behavior is currently considered a bug, compatible behavior may be re-introduced in a future release. Until then, the use of <code>sysopen()</code>, <code>sysread()</code> and <code>syswrite()</code> is not supported for ``text&#8217;&#8216; mode operations.  </p>
<h2>Future Directions</h2>
<p> The following things <code>might</code> happen in future. The first publicly available releases having these characteristics will be the developer releases Perl 5.9.x, culminating in the Perl 5.10.0 release. These are our best guesses at the moment: we reserve the right to rethink. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> PerlIO will become The Default. Currently (in Perl 5.8.x) the stdio library is still used if Perl thinks it can use certain tricks to make stdio go <code>really</code> fast. For future releases our goal is to make PerlIO go even faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new feature called <i>assertions</i> will be available. This means that one can have code called assertions sprinkled in the code: usually they are optimised away, but they can be enabled with the <code>&quot;-A&quot;</code> option. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new operator <code>&quot;//&quot;</code> (defined-or) will be available. This means that one will be able to say </p>
<pre><code>    $a // $b
</code></pre>
<p> instead of </p>
<pre><code>   defined $a ? $a : $b
</code></pre>
<p> and </p>
<pre><code>   $c //= $d;
</code></pre>
<p> instead of </p>
<pre><code>   $c = $d unless defined $c;
</code></pre>
<p> The operator will have the same precedence and associativity as <code>&quot;||&quot;</code>. A source code patch against the Perl 5.8.1 sources will be available in CPAN as <i>authors/id/H/HM/HMBRAND/dor-5.8.1.diff</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;unpack()&quot;</code> will default to unpacking the <code>$_</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various Copy-On-Write techniques will be investigated in hopes of speeding up Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> CPANPLUS, Inline, and Module::Build will become core modules. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ability to write true lexically scoped pragmas will be introduced. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Work will continue on the bytecompiler and byteloader. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> v-strings as they currently exist are scheduled to be deprecated. The v-less form (1.2.3) will become a ``version object&#8217;&#8216; when used with <code>&quot;use&quot;</code>, <code>&quot;require&quot;</code>, and <code>$VERSION</code>. $^V will also be a ``version object&#8217;&#8216; so the printf(``%vd&#8217;&#8216;,...) construct will no longer be needed. The v-ful version (v1.2.3) will become obsolete. The equivalence of strings and v-strings (e.g. that currently 5.8.0 is equal to ``\5\8\0&#8217;&#8216;) will go away. <code>There may be no deprecation warning for v-strings</code>, though: it is quite hard to detect when v-strings are being used safely, and when they are not. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> 5.005 Threads Will Be Removed </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>$*</code> Variable Will Be Removed (it was deprecated a long time ago) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pseudohashes Will Be Removed </p>
 </dd></dl>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.com/">http://www.perl.com/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. You can browse and search the Perl 5 bugs at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><i>INSTALL</i><i></i> file for how to build Perl. </p>
<p> The <i></i><i>README</i><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
