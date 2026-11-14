---
title: "perl5240delta(1)"
name: "perl5240delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5240delta/"
description: "perl5240delta – what is new for perl v5.24.0"
---

<h2 class="name">NAME</h2>
<p> perl5240delta &#8211; what is new for perl v5.24.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes the differences between the 5.22.0 release and the 5.24.0 release.</p>
<h2>Core Enhancements</h2>
<h3>Postfix dereferencing is no longer experimental</h3>
<p> Using the <tt>&quot;postderef&quot;</tt> and <tt>&quot;postderef_qq&quot;</tt> features no longer emits a warning. Existing code that disables the <tt>&quot;experimental::postderef&quot;</tt> warning category that they previously used will continue to work. The <tt>&quot;postderef&quot;</tt> feature has no effect; all Perl code can use postfix dereferencing, regardless of what feature declarations are in scope. The <tt>5.24</tt> feature bundle now includes the <tt>&quot;postderef_qq&quot;</tt> feature.</p>
<h3>Unicode 8.0 is now supported</h3>
<p> For details on what is in this release, see &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode8.0.0/">http://www.unicode.org/versions/Unicode8.0.0/</a>&gt;.</p>
<h3>perl will now croak when closing an in-place output file fails</h3>
<p> Until now, failure to close the output file for an in-place edit was not detected, meaning that the input file could be clobbered without the edit being successfully completed. Now, when the output file cannot be closed successfully, an exception is raised.</p>
<h3>New {lb} boundary in regular expressions</h3>
<p> <tt>&quot;lb&quot;</tt> stands for Line Break. It is a Unicode property that determines where a line of text is suitable to break (typically so that it can be output without overflowing the available horizontal space). This capability has long been furnished by the Unicode::LineBreak module, but now a light-weight, non-customizable version that is suitable for many purposes is in core Perl.</p>
<h3>qr/(?[ ])/ now works in <font SIZE="-1">UTF-8</font> locales</h3>
<p> Extended Bracketed Character Classes now will successfully compile when <tt>&quot;use locale&quot;</tt> is in effect. The compiled pattern will use standard Unicode rules. If the runtime locale is not a <font SIZE="-1">UTF-8</font> one, a warning is raised and standard Unicode rules are used anyway. No tainting is done since the outcome does not actually depend on the locale.</p>
<h3>Integer shift (&lt;&lt; and &gt;&gt;) now more explicitly defined</h3>
<p> Negative shifts are reverse shifts: left shift becomes right shift, and right shift becomes left shift. </p>
<p> Shifting by the number of bits in a native integer (or more) is zero, except when the &#8220;overshift&#8221; is right shifting a negative value under <tt>&quot;use integer&quot;</tt>, in which case the result is -1 (arithmetic shift). </p>
<p> Until now negative shifting and overshifting have been undefined because they have relied on whatever the C implementation happens to do. For example, for the overshift a common C behavior is &#8220;modulo shift&#8221;: </p>
<pre><code>
1 &gt;&gt; 64 == 1 &gt;&gt; (64 % 64) == 1 &gt;&gt; 0 == 1 #Common C behavior.
#And the same for &lt;&lt;, while Perl now produces 0 for both.
</code></pre>
<p> Now these behaviors are well-defined under Perl, regardless of what the underlying C implementation does. Note, however, that you are still constrained by the native integer width: you need to know how far left you can go. You can use for example: </p>
<p>use Config;<br />
my $wordbits = $Config{uvsize} * 8;<br />
#Or $Config{uvsize } &lt;&lt; 3.</p>
<p> If you need a more bits on the left shift, you can use for example the <tt>&quot;bigint&quot;</tt> pragma, or the <tt>&quot;Bit::Vector&quot;</tt> module from <font SIZE="-1">CPAN.</font></p>
<h3>printf and sprintf now allow reordered precision arguments</h3>
<p> That is, <tt>&quot;sprintf '|%.*2$d|', 2, 3&quot;</tt> now returns <tt>&quot;|002|&quot;</tt>. This extends the existing reordering mechanism (which allows reordering for arguments that are used as format fields, widths, and vector separators).</p>
<h3>More fields provided to sigaction callback with SA_SIGINFO</h3>
<p> When passing the <tt>&quot;SA_SIGINFO&quot;</tt> flag to sigaction, the <tt>&quot;errno&quot;</tt>, <tt>&quot;status&quot;</tt>, <tt>&quot;uid&quot;</tt>, <tt>&quot;pid&quot;</tt>, <tt>&quot;addr&quot;</tt> and <tt>&quot;band&quot;</tt> fields are now included in the hash passed to the handler, if supported by the platform.</p>
<h3>Hashbang redirection to Perl 6</h3>
<p> Previously perl would redirect to another interpreter if it found a hashbang path unless the path contains &#8220;perl&#8221; (see perlrun). To improve compatibility with Perl 6 this behavior has been extended to also redirect if &#8220;perl&#8221; is followed by &#8220;6&#8221;.</p>
<h2>Security</h2>
<h3>Set proper umask before calling <a href="/docs/linux/man/3-mkstemp/">mkstemp</a>(3)</h3>
<p> In 5.22 perl started setting umask to 0600 before calling <tt><a href="/docs/linux/man/3-mkstemp/">mkstemp</a>(3)</tt> and restoring it afterwards. This wrongfully tells <tt><a href="/docs/linux/man/2-open/">open</a>(2)</tt> to strip the owner read and write bits from the given mode before applying it, rather than the intended negation of leaving only those bits in place. </p>
<p> Systems that use mode 0666 in <tt><a href="/docs/linux/man/3-mkstemp/">mkstemp</a>(3)</tt> (like old versions of glibc) create a file with permissions 0066, leaving world read and write permissions regardless of current umask. </p>
<p> This has been fixed by using umask 0177 instead. [perl #127322]</p>
<h3>Fix out of boundary access in Win32 path handling</h3>
<p> This is <font SIZE="-1">CVE-2015-8608.</font> For more information see [perl #126755] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126755">https://rt.perl.org/Ticket/Display.html?id=126755</a>&gt;</p>
<h3>Fix loss of taint in canonpath</h3>
<p> This is <font SIZE="-1">CVE-2015-8607.</font> For more information see [perl #126862] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126862">https://rt.perl.org/Ticket/Display.html?id=126862</a>&gt;</p>
<h3>Avoid accessing uninitialized memory in win32 crypt()</h3>
<p> Added validation that will detect both a short salt and invalid characters in the salt. [perl #126922] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126922">https://rt.perl.org/Ticket/Display.html?id=126922</a>&gt;</p>
<h3>Remove duplicate environment variables from environ</h3>
<p> Previously, if an environment variable appeared more than once in <tt>&quot;environ[]&quot;</tt>, <tt>%ENV</tt> would contain the last entry for that name, while a typical <tt>&quot;getenv()&quot;</tt> would return the first entry. We now make sure <tt>%ENV</tt> contains the same as what <tt>&quot;getenv&quot;</tt> returns. </p>
<p> Second, we remove duplicates from <tt>&quot;environ[]&quot;</tt>, so if a setting with that name is set in <tt>%ENV</tt>, we won&#8217;t pass an unsafe value to a child process. </p>
<p> [<font SIZE="-1">CVE-2016-2381</font>]</p>
<h2>Incompatible Changes</h2>
<h3>The autoderef feature has been removed</h3>
<p> The experimental <tt>&quot;autoderef&quot;</tt> feature (which allowed calling <tt>&quot;push&quot;</tt>, <tt>&quot;pop&quot;</tt>, <tt>&quot;shift&quot;</tt>, <tt>&quot;unshift&quot;</tt>, <tt>&quot;splice&quot;</tt>, <tt>&quot;keys&quot;</tt>, <tt>&quot;values&quot;</tt>, and <tt>&quot;each&quot;</tt> on a scalar argument) has been deemed unsuccessful. It has now been removed; trying to use the feature (or to disable the <tt>&quot;experimental::autoderef&quot;</tt> warning it previously triggered) now yields an exception.</p>
<h3>Lexical $_ has been removed</h3>
<p> <tt>&quot;my $_&quot;</tt> was introduced in Perl 5.10, and subsequently caused much confusion with no obvious solution. In Perl 5.18.0, it was made experimental on the theory that it would either be removed or redesigned in a less confusing (but backward-incompatible) way. Over the following years, no alternatives were proposed. The feature has now been removed and will fail to compile.</p>
<h3>qr/{wb}/ is now tailored to Perl expectations</h3>
<p> This is now more suited to be a drop-in replacement for plain <tt>&quot;&quot;</tt>, but giving better results for parsing natural language. Previously it strictly followed the current Unicode rules which calls for it to match between each white space character. Now it doesn&#8217;t generally match within spans of white space, behaving like <tt>&quot;&quot;</tt> does. See &#8220;{wb}&#8221; in perlrebackslash</p>
<h3>Regular expression compilation errors</h3>
<p> Some regular expression patterns that had runtime errors now don&#8217;t compile at all. </p>
<p> Almost all Unicode properties using the <tt>&quot;\p{}&quot;</tt> and <tt>&quot;\P{}&quot;</tt> regular expression pattern constructs are now checked for validity at pattern compilation time, and invalid ones will cause the program to not compile. In earlier releases, this check was often deferred until run time. Whenever an error check is moved from run- to compile time, erroneous code is caught 100% of the time, whereas before it would only get caught if and when the offending portion actually gets executed, which for unreachable code might be never.</p>
<h3>qr/\N{}/ now disallowed under use re strict</h3>
<p> An empty <tt>&quot;\N{}&quot;</tt> makes no sense, but for backwards compatibility is accepted as doing nothing, though a deprecation warning is raised by default. But now this is a fatal error under the experimental feature &#8220;&#8217;strict&#8217; mode&#8221; in re.</p>
<h3>Nested declarations are now disallowed</h3>
<p> A <tt>&quot;my&quot;</tt>, <tt>&quot;our&quot;</tt>, or <tt>&quot;state&quot;</tt> declaration is no longer allowed inside of another <tt>&quot;my&quot;</tt>, <tt>&quot;our&quot;</tt>, or <tt>&quot;state&quot;</tt> declaration. </p>
<p> For example, these are now fatal: </p>
<p>my($x, my($y));<br />
our(my $x);</p>
<p> [perl #125587] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125587">https://rt.perl.org/Ticket/Display.html?id=125587</a>&gt; </p>
<p> [perl #121058] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121058">https://rt.perl.org/Ticket/Display.html?id=121058</a>&gt;</p>
<h3>The /\C/ character class has been removed.</h3>
<p> This regular expression character class was deprecated in v5.20.0 and has produced a deprecation warning since v5.22.0. It is now a compile-time error. If you need to examine the individual bytes that make up a UTF8-encoded character, then use <tt>&quot;utf8::encode()&quot;</tt> on the string (or a copy) first.</p>
<h3>chdir(&#8221;) no longer chdirs home</h3>
<p> Using <tt>&quot;chdir('')&quot;</tt> or <tt>&quot;chdir(undef)&quot;</tt> to chdir home has been deprecated since perl v5.8, and will now fail. Use <tt>&quot;chdir()&quot;</tt> instead.</p>
<h3><font SIZE="-1">ASCII</font> characters in variable names must now be all visible</h3>
<p> It was legal until now on <font SIZE="-1">ASCII</font> platforms for variable names to contain non-graphical <font SIZE="-1">ASCII</font> control characters (ordinals 0 through 31, and 127, which are the C0 controls and <tt>&quot;DELETE&quot;</tt>). This usage has been deprecated since v5.20, and as of now causes a syntax error. The variables these names referred to are special, reserved by Perl for whatever use it may choose, now, or in the future. Each such variable has an alternative way of spelling it. Instead of the single non-graphic control character, a two character sequence beginning with a caret is used, like <tt>$^]</tt> and <tt>&quot;${^GLOBAL_PHASE}&quot;</tt>. Details are at perlvar. It remains legal, though unwise and deprecated (raising a deprecation warning), to use certain non-graphic non-ASCII characters in variables names when not under <tt>&quot;use utf8&quot;</tt>. No code should do this, as all such variables are reserved by Perl, and Perl doesn&#8217;t currently define any of them (but could at any time, without notice).</p>
<h3>An off by one issue in $Carp::MaxArgNums has been fixed</h3>
<p> <tt>$Carp::MaxArgNums</tt> is supposed to be the number of arguments to display. Prior to this version, it was instead showing <tt>$Carp::MaxArgNums</tt> + 1 arguments, contrary to the documentation.</p>
<h3>Only blanks and tabs are now allowed within [&#8230;] within (?[&#8230;]).</h3>
<p> The experimental Extended Bracketed Character Classes can contain regular bracketed character classes within them. These differ from regular ones in that white space is generally ignored, unless escaped by preceding it with a backslash. The white space that is ignored is now limited to just tab <tt>&quot;	&quot;</tt> and <font SIZE="-1">SPACE</font> characters. Previously, it was any white space. See &#8220;Extended Bracketed Character Classes&#8221; in perlrecharclass.</p>
<h2>Deprecations</h2>
<h3>Using code points above the platform&#8217;s IV_MAX is now deprecated</h3>
<p> Unicode defines code points in the range <tt>&quot;0..0x10FFFF&quot;</tt>. Some standards at one time defined them up to 2**31 &#8211; 1, but Perl has allowed them to be as high as anything that will fit in a word on the platform being used. However, use of those above the platform&#8217;s <tt>&quot;IV_MAX&quot;</tt> is broken in some constructs, notably <tt>&quot;tr///&quot;</tt>, regular expression patterns involving quantifiers, and in some arithmetic and comparison operations, such as being the upper limit of a loop. Now the use of such code points raises a deprecation warning, unless that warning category is turned off. <tt>&quot;IV_MAX&quot;</tt> is typically 2**31 -1 on 32-bit platforms, and 2**63-1 on 64-bit ones.</p>
<h3>Doing bitwise operations on strings containing code points above 0xFF is deprecated</h3>
<p> The string bitwise operators treat their operands as strings of bytes, and values beyond 0xFF are nonsensical in this context. To operate on encoded bytes, first encode the strings. To operate on code points&#8217; numeric values, use <tt>&quot;split&quot;</tt> and <tt>&quot;map ord&quot;</tt>. In the future, this warning will be replaced by an exception.</p>
<h3>sysread(), syswrite(), recv() and send() are deprecated on :utf8 handles</h3>
<p> The <tt>&quot;sysread()&quot;</tt>, <tt>&quot;recv()&quot;</tt>, <tt>&quot;syswrite()&quot;</tt> and <tt>&quot;send()&quot;</tt> operators are deprecated on handles that have the <tt>&quot;:utf8&quot;</tt> layer, either explicitly, or implicitly, eg., with the <tt>&quot;:encoding(UTF-16LE)&quot;</tt> layer. </p>
<p> Both <tt>&quot;sysread()&quot;</tt> and <tt>&quot;recv()&quot;</tt> currently use only the <tt>&quot;:utf8&quot;</tt> flag for the stream, ignoring the actual layers. Since <tt>&quot;sysread()&quot;</tt> and <tt>&quot;recv()&quot;</tt> do no <font SIZE="-1">UTF-8</font> validation they can end up creating invalidly encoded scalars. </p>
<p> Similarly, <tt>&quot;syswrite()&quot;</tt> and <tt>&quot;send()&quot;</tt> use only the <tt>&quot;:utf8&quot;</tt> flag, otherwise ignoring any layers. If the flag is set, both write the value <font SIZE="-1">UTF-8</font> encoded, even if the layer is some different encoding, such as the example above. </p>
<p> Ideally, all of these operators would completely ignore the <tt>&quot;:utf8&quot;</tt> state, working only with bytes, but this would result in silently breaking existing code. To avoid this a future version of perl will throw an exception when any of <tt>&quot;sysread()&quot;</tt>, <tt>&quot;recv()&quot;</tt>, <tt>&quot;syswrite()&quot;</tt> or <tt>&quot;send()&quot;</tt> are called on handle with the <tt>&quot;:utf8&quot;</tt> layer.</p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</p>
<dd> The overhead of scope entry and exit has been considerably reduced, so for example subroutine calls, loops and basic blocks are all faster now. This empty function call now takes about a third less time to execute: </p>
<p>sub f<br />
{<br />
}<br />
f();</p>
<dt>&bull;</p>
<dd> Many languages, such as Chinese, are caseless. Perl now knows about most common ones, and skips much of the work when a program tries to change case in them (like <tt>&quot;ucfirst()&quot;</tt>) or match caselessly (<tt>&quot;qr//i&quot;</tt>). This will speed up a program, such as a web server, that can operate on multiple languages, while it is operating on a caseless one.</p>
<dt>&bull;</p>
<dd> <tt>&quot;/fixed-substr/&quot;</tt> has been made much faster. </p>
<p> On platforms with a libc <tt>&quot;memchr()&quot;</tt> implementation which makes good use of underlying hardware support, patterns which include fixed substrings will now often be much faster; for example with glibc on a recent x86_64 <font SIZE="-1">CPU,</font> this: </p>
<pre>
    $s = &quot;a&quot; x 1000 . &quot;wxyz&quot;;
    $s =~ /wxyz/ for 1..30000
</pre>
<p> is now about 7 times faster. On systems with slow <tt>&quot;memchr()&quot;</tt>, e.g. 32-bit <font SIZE="-1">ARM</font> Raspberry Pi, there will be a small or little speedup. Conversely, some pathological cases, such as <tt>&quot;&quot;ab&quot; x 1000 =~ /aa/&quot;</tt> will be slower now; up to 3 times slower on the rPi, 1.5x slower on x86_64.</p>
<dt>&bull;</p>
<dd> Faster addition, subtraction and multiplication. </p>
<p> Since 5.8.0, arithmetic became slower due to the need to support 64-bit integers. To deal with 64-bit integers, a lot more corner cases need to be checked, which adds time. We now detect common cases where there is no need to check for those corner cases, and special-case them.</p>
<dt>&bull;</p>
<dd> Preincrement, predecrement, postincrement, and postdecrement have been made faster by internally splitting the functions which handled multiple cases into different functions.</p>
<dt>&bull;</p>
<dd> Creating Perl debugger data structures (see &#8220;Debugger Internals&#8221; in perldebguts) for XSUBs and const subs has been removed. This removed one glob/scalar combo for each unique <tt>&quot;.c&quot;</tt> file that XSUBs and const subs came from. On startup (<tt>&quot;perl -e&quot;0&quot;&quot;</tt>) about half a dozen glob/scalar debugger combos were created. Loading <font SIZE="-1">XS</font> modules created more glob/scalar combos. These things were being created regardless of whether the perl debugger was being used, and despite the fact that it can&#8217;t debug C code anyway</p>
<dt>&bull;</p>
<dd> On Win32, <tt>&quot;stat&quot;</tt>ing or <tt>&quot;-X&quot;</tt>ing a path, if the file or directory does not exist, is now 3.5x faster than before.</p>
<dt>&bull;</p>
<dd> Single arguments in list assign are now slightly faster: </p>
<pre><code>
($x) = (...);
(...) = ($x);
</code></pre>
<dt>&bull;</p>
<dd> Less peak memory is now used when compiling regular expression patterns.</dl>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> arybase has been upgraded from version 0.10 to 0.11.</p>
<dt>&bull;</p>
<dd> Attribute::Handlers has been upgraded from version 0.97 to 0.99.</p>
<dt>&bull;</p>
<dd> autodie has been upgraded from version 2.26 to 2.29.</p>
<dt>&bull;</p>
<dd> autouse has been upgraded from version 1.08 to 1.11.</p>
<dt>&bull;</p>
<dd> B has been upgraded from version 1.58 to 1.62.</p>
<dt>&bull;</p>
<dd> B::Deparse has been upgraded from version 1.35 to 1.37.</p>
<dt>&bull;</p>
<dd> base has been upgraded from version 2.22 to 2.23.</p>
<dt>&bull;</p>
<dd> Benchmark has been upgraded from version 1.2 to 1.22.</p>
<dt>&bull;</p>
<dd> bignum has been upgraded from version 0.39 to 0.42.</p>
<dt>&bull;</p>
<dd> bytes has been upgraded from version 1.04 to 1.05.</p>
<dt>&bull;</p>
<dd> Carp has been upgraded from version 1.36 to 1.40.</p>
<dt>&bull;</p>
<dd> Compress::Raw::Bzip2 has been upgraded from version 2.068 to 2.069.</p>
<dt>&bull;</p>
<dd> Compress::Raw::Zlib has been upgraded from version 2.068 to 2.069.</p>
<dt>&bull;</p>
<dd> Config::Perl::V has been upgraded from version 0.24 to 0.25.</p>
<dt>&bull;</p>
<dd> CPAN::Meta has been upgraded from version 2.150001 to 2.150005.</p>
<dt>&bull;</p>
<dd> CPAN::Meta::Requirements has been upgraded from version 2.132 to 2.140.</p>
<dt>&bull;</p>
<dd> CPAN::Meta::YAML has been upgraded from version 0.012 to 0.018.</p>
<dt>&bull;</p>
<dd> Data::Dumper has been upgraded from version 2.158 to 2.160.</p>
<dt>&bull;</p>
<dd> Devel::Peek has been upgraded from version 1.22 to 1.23.</p>
<dt>&bull;</p>
<dd> Devel::PPPort has been upgraded from version 3.31 to 3.32.</p>
<dt>&bull;</p>
<dd> Dumpvalue has been upgraded from version 1.17 to 1.18.</p>
<dt>&bull;</p>
<dd> DynaLoader has been upgraded from version 1.32 to 1.38.</p>
<dt>&bull;</p>
<dd> Encode has been upgraded from version 2.72 to 2.80.</p>
<dt>&bull;</p>
<dd> encoding has been upgraded from version 2.14 to 2.17.</p>
<dt>&bull;</p>
<dd> encoding::warnings has been upgraded from version 0.11 to 0.12.</p>
<dt>&bull;</p>
<dd> English has been upgraded from version 1.09 to 1.10.</p>
<dt>&bull;</p>
<dd> Errno has been upgraded from version 1.23 to 1.25.</p>
<dt>&bull;</p>
<dd> experimental has been upgraded from version 0.013 to 0.016.</p>
<dt>&bull;</p>
<dd> ExtUtils::CBuilder has been upgraded from version 0.280221 to 0.280225.</p>
<dt>&bull;</p>
<dd> ExtUtils::Embed has been upgraded from version 1.32 to 1.33.</p>
<dt>&bull;</p>
<dd> ExtUtils::MakeMaker has been upgraded from version 7.04_01 to 7.10_01.</p>
<dt>&bull;</p>
<dd> ExtUtils::ParseXS has been upgraded from version 3.28 to 3.31.</p>
<dt>&bull;</p>
<dd> ExtUtils::Typemaps has been upgraded from version 3.28 to 3.31.</p>
<dt>&bull;</p>
<dd> feature has been upgraded from version 1.40 to 1.42.</p>
<dt>&bull;</p>
<dd> fields has been upgraded from version 2.17 to 2.23.</p>
<dt>&bull;</p>
<dd> File::Find has been upgraded from version 1.29 to 1.34.</p>
<dt>&bull;</p>
<dd> File::Glob has been upgraded from version 1.24 to 1.26.</p>
<dt>&bull;</p>
<dd> File::Path has been upgraded from version 2.09 to 2.12_01.</p>
<dt>&bull;</p>
<dd> File::Spec has been upgraded from version 3.56 to 3.63.</p>
<dt>&bull;</p>
<dd> Filter::Util::Call has been upgraded from version 1.54 to 1.55.</p>
<dt>&bull;</p>
<dd> Getopt::Long has been upgraded from version 2.45 to 2.48.</p>
<dt>&bull;</p>
<dd> Hash::Util has been upgraded from version 0.18 to 0.19.</p>
<dt>&bull;</p>
<dd> Hash::Util::FieldHash has been upgraded from version 1.15 to 1.19.</p>
<dt>&bull;</p>
<dd> HTTP::Tiny has been upgraded from version 0.054 to 0.056.</p>
<dt>&bull;</p>
<dd> I18N::Langinfo has been upgraded from version 0.12 to 0.13.</p>
<dt>&bull;</p>
<dd> if has been upgraded from version 0.0604 to 0.0606.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">IO</font> has been upgraded from version 1.35 to 1.36.</p>
<dt>&bull;</p>
<dd> IO-Compress has been upgraded from version 2.068 to 2.069.</p>
<dt>&bull;</p>
<dd> IPC::Open3 has been upgraded from version 1.18 to 1.20.</p>
<dt>&bull;</p>
<dd> IPC::SysV has been upgraded from version 2.04 to 2.06_01.</p>
<dt>&bull;</p>
<dd> List::Util has been upgraded from version 1.41 to 1.42_02.</p>
<dt>&bull;</p>
<dd> locale has been upgraded from version 1.06 to 1.08.</p>
<dt>&bull;</p>
<dd> Locale::Codes has been upgraded from version 3.34 to 3.37.</p>
<dt>&bull;</p>
<dd> Math::BigInt has been upgraded from version 1.9997 to 1.999715.</p>
<dt>&bull;</p>
<dd> Math::BigInt::FastCalc has been upgraded from version 0.31 to 0.40.</p>
<dt>&bull;</p>
<dd> Math::BigRat has been upgraded from version 0.2608 to 0.260802.</p>
<dt>&bull;</p>
<dd> Module::CoreList has been upgraded from version 5.20150520 to 5.20160320.</p>
<dt>&bull;</p>
<dd> Module::Metadata has been upgraded from version 1.000026 to 1.000031.</p>
<dt>&bull;</p>
<dd> mro has been upgraded from version 1.17 to 1.18.</p>
<dt>&bull;</p>
<dd> ODBM_File has been upgraded from version 1.12 to 1.14.</p>
<dt>&bull;</p>
<dd> Opcode has been upgraded from version 1.32 to 1.34.</p>
<dt>&bull;</p>
<dd> parent has been upgraded from version 0.232 to 0.234.</p>
<dt>&bull;</p>
<dd> Parse::CPAN::Meta has been upgraded from version 1.4414 to 1.4417.</p>
<dt>&bull;</p>
<dd> Perl::OSType has been upgraded from version 1.008 to 1.009.</p>
<dt>&bull;</p>
<dd> perlfaq has been upgraded from version 5.021009 to 5.021010.</p>
<dt>&bull;</p>
<dd> PerlIO::encoding has been upgraded from version 0.21 to 0.24.</p>
<dt>&bull;</p>
<dd> PerlIO::mmap has been upgraded from version 0.014 to 0.016.</p>
<dt>&bull;</p>
<dd> PerlIO::scalar has been upgraded from version 0.22 to 0.24.</p>
<dt>&bull;</p>
<dd> PerlIO::via has been upgraded from version 0.15 to 0.16.</p>
<dt>&bull;</p>
<dd> Pod::Functions has been upgraded from version 1.09 to 1.10.</p>
<dt>&bull;</p>
<dd> Pod::Perldoc has been upgraded from version 3.25 to 3.25_02.</p>
<dt>&bull;</p>
<dd> Pod::Simple has been upgraded from version 3.29 to 3.32.</p>
<dt>&bull;</p>
<dd> Pod::Usage has been upgraded from version 1.64 to 1.68.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">POSIX</font> has been upgraded from version 1.53 to 1.65.</p>
<dt>&bull;</p>
<dd> Scalar::Util has been upgraded from version 1.41 to 1.42_02.</p>
<dt>&bull;</p>
<dd> SDBM_File has been upgraded from version 1.13 to 1.14.</p>
<dt>&bull;</p>
<dd> SelfLoader has been upgraded from version 1.22 to 1.23.</p>
<dt>&bull;</p>
<dd> Socket has been upgraded from version 2.018 to 2.020_03.</p>
<dt>&bull;</p>
<dd> Storable has been upgraded from version 2.53 to 2.56.</p>
<dt>&bull;</p>
<dd> strict has been upgraded from version 1.09 to 1.11.</p>
<dt>&bull;</p>
<dd> Term::ANSIColor has been upgraded from version 4.03 to 4.04.</p>
<dt>&bull;</p>
<dd> Term::Cap has been upgraded from version 1.15 to 1.17.</p>
<dt>&bull;</p>
<dd> Test has been upgraded from version 1.26 to 1.28.</p>
<dt>&bull;</p>
<dd> Test::Harness has been upgraded from version 3.35 to 3.36.</p>
<dt>&bull;</p>
<dd> Thread::Queue has been upgraded from version 3.05 to 3.08.</p>
<dt>&bull;</p>
<dd> threads has been upgraded from version 2.01 to 2.06.</p>
<dt>&bull;</p>
<dd> threads::shared has been upgraded from version 1.48 to 1.50.</p>
<dt>&bull;</p>
<dd> Tie::File has been upgraded from version 1.01 to 1.02.</p>
<dt>&bull;</p>
<dd> Tie::Scalar has been upgraded from version 1.03 to 1.04.</p>
<dt>&bull;</p>
<dd> Time::HiRes has been upgraded from version 1.9726 to 1.9732.</p>
<dt>&bull;</p>
<dd> Time::Piece has been upgraded from version 1.29 to 1.31.</p>
<dt>&bull;</p>
<dd> Unicode::Collate has been upgraded from version 1.12 to 1.14.</p>
<dt>&bull;</p>
<dd> Unicode::Normalize has been upgraded from version 1.18 to 1.25.</p>
<dt>&bull;</p>
<dd> Unicode::UCD has been upgraded from version 0.61 to 0.64.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">UNIVERSAL</font> has been upgraded from version 1.12 to 1.13.</p>
<dt>&bull;</p>
<dd> utf8 has been upgraded from version 1.17 to 1.19.</p>
<dt>&bull;</p>
<dd> version has been upgraded from version 0.9909 to 0.9916.</p>
<dt>&bull;</p>
<dd> warnings has been upgraded from version 1.32 to 1.36.</p>
<dt>&bull;</p>
<dd> Win32 has been upgraded from version 0.51 to 0.52.</p>
<dt>&bull;</p>
<dd> Win32API::File has been upgraded from version 0.1202 to 0.1203.</p>
<dt>&bull;</p>
<dd> XS::Typemap has been upgraded from version 0.13 to 0.14.</p>
<dt>&bull;</p>
<dd> XSLoader has been upgraded from version 0.20 to 0.21.</dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlapi</i></p>
<dl>
<dt>&bull;</p>
<dd> The process of using undocumented globals has been documented, namely, that one should send email to perl5-porters [at] perl.org &lt;mailto:perl5-porters [at] perl.org&gt; first to get the go-ahead for documenting and using an undocumented function or global variable.</dl>
<p> <i>perlcall</i></p>
<dl>
<dt>&bull;</p>
<dd> A number of cleanups have been made to perlcall, including:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> use <tt>&quot;EXTEND(SP, n)&quot;</tt> and <tt>&quot;PUSHs()&quot;</tt> instead of <tt>&quot;XPUSHs()&quot;</tt> where applicable and update prose to match</p>
<dt>&bull;</p>
<dd> add POPu, POPul and POPpbytex to the &#8220;complete list of <font SIZE="-1">POP</font> macros&#8221; and clarify the documentation for some of the existing entries, and a note about side-effects</p>
<dt>&bull;</p>
<dd> add <font SIZE="-1">API</font> documentation for POPu and POPul</p>
<dt>&bull;</p>
<dd> use <font SIZE="-1">ERRSV</font> more efficiently</p>
<dt>&bull;</p>
<dd> approaches to thread-safety storage of SVs.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> <i>perlfunc</i></p>
<dl>
<dt>&bull;</p>
<dd> The documentation of <tt>&quot;hex&quot;</tt> has been revised to clarify valid inputs.</p>
<dt>&bull;</p>
<dd> Better explain meaning of negative PIDs in <tt>&quot;waitpid&quot;</tt>. [perl #127080] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127080">https://rt.perl.org/Ticket/Display.html?id=127080</a>&gt;</p>
<dt>&bull;</p>
<dd> General cleanup: there&#8217;s more consistency now (in <font SIZE="-1">POD</font> usage, grammar, code examples), better practices in code examples (use of <tt>&quot;my&quot;</tt>, removal of bareword filehandles, dropped usage of <tt>&quot;&amp;&quot;</tt> when calling subroutines, &#8230;), etc.</dl>
<p> <i>perlguts</i></p>
<dl>
<dt>&bull;</p>
<dd> A new section has been added, &#8220;Dynamic Scope and the Context Stack&#8221; in perlguts, which explains how the perl context stack works.</dl>
<p> <i>perllocale</i></p>
<dl>
<dt>&bull;</p>
<dd> A stronger caution about using locales in threaded applications is given. Locales are not thread-safe, and you can get wrong results or even segfaults if you use them there.</dl>
<p> <i>perlmodlib</i></p>
<dl>
<dt>&bull;</p>
<dd> We now recommend contacting the module-authors list or <font SIZE="-1">PAUSE</font> in seeking guidance on the naming of modules.</dl>
<p> <i>perlop</i></p>
<dl>
<dt>&bull;</p>
<dd> The documentation of <tt>&quot;qx//&quot;</tt> now describes how <tt>$?</tt> is affected.</dl>
<p> <i>perlpolicy</i></p>
<dl>
<dt>&bull;</p>
<dd> This note has been added to perlpolicy: </p>
<pre>
 While civility is required, kindness is encouraged; if you have any
 doubt about whether you are being civil, simply ask yourself, &quot;Am I
 being kind?&quot; and aspire to that.
</pre>
</dl>
<p> <i>perlreftut</i></p>
<dl>
<dt>&bull;</p>
<dd> Fix some examples to be strict clean.</dl>
<p> <i>perlrebackslash</i></p>
<dl>
<dt>&bull;</p>
<dd> Clarify that in languages like Japanese and Thai, dictionary lookup is required to determine word boundaries.</dl>
<p> <i>perlsub</i></p>
<dl>
<dt>&bull;</p>
<dd> Updated to note that anonymous subroutines can have signatures.</dl>
<p> <i>perlsyn</i></p>
<dl>
<dt>&bull;</p>
<dd> Fixed a broken example where <tt>&quot;=&quot;</tt> was used instead of <tt>&quot;==&quot;</tt> in conditional in do/while example.</dl>
<p> <i>perltie</i></p>
<dl>
<dt>&bull;</p>
<dd> The usage of <tt>&quot;FIRSTKEY&quot;</tt> and <tt>&quot;NEXTKEY&quot;</tt> has been clarified.</dl>
<p> <i>perlunicode</i></p>
<dl>
<dt>&bull;</p>
<dd> Discourage use of &#8216;In&#8217; as a prefix signifying the Unicode Block property.</dl>
<p> <i>perlvar</i></p>
<dl>
<dt>&bull;</p>
<dd> The documentation of <tt>$@</tt> was reworded to clarify that it is not just for syntax errors in <tt>&quot;eval&quot;</tt>. [perl #124034] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124034">https://rt.perl.org/Ticket/Display.html?id=124034</a>&gt;</p>
<dt>&bull;</p>
<dd> The specific true value of <tt>$!{E...}</tt> is now documented, noting that it is subject to change and not guaranteed.</p>
<dt>&bull;</p>
<dd> Use of <tt>$OLD_PERL_VERSION</tt> is now discouraged.</dl>
<p> <i>perlxs</i></p>
<dl>
<dt>&bull;</p>
<dd> The documentation of <tt>&quot;PROTOTYPES&quot;</tt> has been corrected; they are <i>disabled</i> by default, not <i>enabled</i>.</dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.</p>
<h3>New Diagnostics</h3>
<p> <i>New Errors</i></p>
<dl>
<dt>&bull;</p>
<dd> <tt>%s</tt> must not be a named sequence in transliteration operator</p>
<dt>&bull;</p>
<dd> Can&#8217;t find Unicode property definition &#8220;%s&#8221; in regex;</p>
<dt>&bull;</p>
<dd> Can&#8217;t redeclare &#8220;%s&#8221; in &#8220;%s&#8221;</p>
<dt>&bull;</p>
<dd> Character following \p must be &#8216;{&#8216; or a single-character Unicode property name in regex;</p>
<dt>&bull;</p>
<dd> Empty \%c in regex; marked by &lt;&#8211; <font SIZE="-1">HERE</font> in m/%s/</p>
<dt>&bull;</p>
<dd> Illegal user-defined property name</p>
<dt>&bull;</p>
<dd> Invalid number &#8216;%s&#8217; for -C option.</p>
<dt>&bull;</p>
<dd> Sequence (?&#8230; not terminated in regex; marked by &lt;&#8211; <font SIZE="-1">HERE</font> in m/%s/</p>
<dt>&bull;</p>
<dd> Sequence (?P&lt;&#8230; not terminated in regex; marked by &lt;&#8211; <font SIZE="-1">HERE</font> in m/%s/</p>
<dt>&bull;</p>
<dd> Sequence (?P&gt;&#8230; not terminated in regex; marked by &lt;&#8211; <font SIZE="-1">HERE</font> in m/%s/</dl>
<p> <i>New Warnings</i></p>
<dl>
<dt>&bull;</p>
<dd> Assuming <font SIZE="-1">NOT</font> a <font SIZE="-1">POSIX</font> class since <tt>%s</tt> in regex; marked by &lt;&#8211; <font SIZE="-1">HERE</font> in m/%s/</p>
<dt>&bull;</p>
<dd> %s() is deprecated on :utf8 handles</dl>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</p>
<dd> Accessing the <tt>&quot;IO&quot;</tt> part of a glob as <tt>&quot;FILEHANDLE&quot;</tt> instead of <tt>&quot;IO&quot;</tt> is no longer deprecated. It is discouraged to encourage uniformity (so that, for example, one can grep more easily) but it will not be removed. [perl #127060] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127060">https://rt.perl.org/Ticket/Display.html?id=127060</a>&gt;</p>
<dt>&bull;</p>
<dd> The diagnostic <tt>&quot;Hexadecimal float: internal error&quot;</tt> has been changed to <tt>&quot;Hexadecimal float: internal error (%s)&quot;</tt> to include more information.</p>
<dt>&bull;</p>
<dd> Can&#8217;t modify non-lvalue subroutine call of &amp;%s </p>
<p> This error now reports the name of the non-lvalue subroutine you attempted to use as an lvalue.</p>
<dt>&bull;</p>
<dd> When running out of memory during an attempt the increase the stack size, previously, perl would die using the cryptic message <tt>&quot;panic: av_extend_guts() negative count (-9223372036854775681)&quot;</tt>. This has been fixed to show the prettier message: Out of memory during stack extend</dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;Configure&quot;</tt> now acts as if the <tt>&quot;-O&quot;</tt> option is always passed, allowing command line options to override saved configuration. This should eliminate confusion when command line options are ignored for no obvious reason. <tt>&quot;-O&quot;</tt> is now permitted, but ignored.</p>
<dt>&bull;</p>
<dd> Bison 3.0 is now supported.</p>
<dt>&bull;</p>
<dd> <i>Configure</i> no longer probes for <i>libnm</i> by default. Originally this was the &#8220;New Math&#8221; library, but the name has been re-used by the <font SIZE="-1">GNOME</font> NetworkManager. [perl #127131] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127131">https://rt.perl.org/Ticket/Display.html?id=127131</a>&gt;</p>
<dt>&bull;</p>
<dd> Added <i>Configure</i> probes for <tt>&quot;newlocale&quot;</tt>, <tt>&quot;freelocale&quot;</tt>, and <tt>&quot;uselocale&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;PPPort.so/PPPort.dll&quot;</tt> no longer get installed, as they are not used by <tt>&quot;PPPort.pm&quot;</tt>, only by its test files.</p>
<dt>&bull;</p>
<dd> It is now possible to specify which compilation date to show on <tt>&quot;perl -V&quot;</tt> output, by setting the macro <tt>&quot;PERL_BUILD_DATE&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Using the <tt>&quot;NO_HASH_SEED&quot;</tt> define in combination with the default hash algorithm <tt>&quot;PERL_HASH_FUNC_ONE_AT_A_TIME_HARD&quot;</tt> resulted in a fatal error while compiling the interpreter, since Perl 5.17.10. This has been fixed.</p>
<dt>&bull;</p>
<dd> <i>Configure</i> should handle spaces in paths a little better.</p>
<dt>&bull;</p>
<dd> No longer generate <font SIZE="-1">EBCDIC</font> POSIX-BC tables. We don&#8217;t believe anyone is using Perl and POSIX-BC at this time, and by not generating these tables it saves time during development, and makes the resulting tar ball smaller.</p>
<dt>&bull;</p>
<dd> The <font SIZE="-1">GNU</font> Make makefile for Win32 now supports parallel builds. [perl #126632]</p>
<dt>&bull;</p>
<dd> You can now build perl with <font SIZE="-1">MSVC++</font> on Win32 using <font SIZE="-1">GNU</font> Make. [perl #126632]</p>
<dt>&bull;</p>
<dd> The Win32 miniperl now has a real <tt>&quot;getcwd&quot;</tt> which increases build performance resulting in <tt>&quot;getcwd()&quot;</tt> being 605x faster in Win32 miniperl.</p>
<dt>&bull;</p>
<dd> Configure now takes <tt>&quot;-Dusequadmath&quot;</tt> into account when calculating the <tt>&quot;alignbytes&quot;</tt> configuration variable. Previously the mis-calculated <tt>&quot;alignbytes&quot;</tt> could cause alignment errors on debugging builds. [perl #127894]</dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</p>
<dd> A new test (<i>t/op/aassign.t</i>) has been added to test the list assignment operator <tt>&quot;OP_AASSIGN&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Parallel building has been added to the dmake <tt>&quot;makefile.mk&quot;</tt> makefile. All Win32 compilers are supported.</dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>AmigaOS</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The AmigaOS port has been reintegrated into the main tree, based off of Perl 5.22.1.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Cygwin</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Tests are more robust against unusual cygdrive prefixes. [perl #126834] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126834">https://rt.perl.org/Ticket/Display.html?id=126834</a>&gt;</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><font SIZE="-1">EBCDIC</font></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>UTF-EBCDIC extended</p>
<dd> UTF-EBCDIC is like <font SIZE="-1">UTF-8,</font> but for <font SIZE="-1">EBCDIC</font> platforms. It now has been extended so that it can represent code points up to 2 ** 64 &#8211; 1 on platforms with 64-bit words. This brings it into parity with <font SIZE="-1">UTF-8.</font> This enhancement requires an incompatible change to the representation of code points in the range 2 ** 30 to 2 ** 31 -1 (the latter was the previous maximum representable code point). This means that a file that contains one of these code points, written out with previous versions of perl cannot be read in, without conversion, by a perl containing this change. We do not believe any such files are in existence, but if you do have one, submit a ticket at perlbug [at] perl.org &lt;mailto:perlbug [at] perl.org&gt;, and we will write a conversion script for you.</p>
<dt><font SIZE="-1">EBCDIC</font> &quot;cmp()&quot; and &quot;sort()&quot; fixed for UTF-EBCDIC strings</p>
<dd> Comparing two strings that were both encoded in <font SIZE="-1">UTF-8</font> (or more precisely, UTF-EBCDIC) did not work properly until now. Since <tt>&quot;sort()&quot;</tt> uses <tt>&quot;cmp()&quot;</tt>, this fixes that as well.</p>
<dt><font SIZE="-1">EBCDIC</font> &quot;tr///&quot; and &quot;y///&quot; fixed for &quot;\N{}&quot;, and &quot;use utf8&quot; ranges</p>
<dd> Perl v5.22 introduced the concept of portable ranges to regular expression patterns. A portable range matches the same set of characters no matter what platform is being run on. This concept is now extended to <tt>&quot;tr///&quot;</tt>. See <tt>&quot;tr///&quot;</tt>. </p>
<p> There were also some problems with these operations under <tt>&quot;use utf8&quot;</tt>, which are now fixed</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>FreeBSD</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Use the <tt>&quot;fdclose()&quot;</tt> function from FreeBSD if it is available. [perl #126847] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126847">https://rt.perl.org/Ticket/Display.html?id=126847</a>&gt;</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><font SIZE="-1">IRIX</font></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Under some circumstances <font SIZE="-1">IRIX</font> stdio <tt>&quot;fgetc()&quot;</tt> and <tt>&quot;fread()&quot;</tt> set the errno to <tt>&quot;ENOENT&quot;</tt>, which made no sense according to either <font SIZE="-1">IRIX</font> or <font SIZE="-1">POSIX</font> docs. Errno is now cleared in such cases. [perl #123977] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123977">https://rt.perl.org/Ticket/Display.html?id=123977</a>&gt;</p>
<dt>&bull;</p>
<dd> Problems when multiplying long doubles by infinity have been fixed. [perl #126396] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126396">https://rt.perl.org/Ticket/Display.html?id=126396</a>&gt;</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>MacOS X</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Until now <font SIZE="-1">OS X</font> builds of perl have specified a link target of 10.3 (Panther, 2003) but have not specified a compiler target. From now on, builds of perl on <font SIZE="-1">OS X 10.6</font> or later (Snow Leopard, 2008) by default capture the current <font SIZE="-1">OS X</font> version and specify that as the explicit build target in both compiler and linker flags, thus preserving binary compatibility for extensions built later regardless of changes in <font SIZE="-1">OS X, SDK,</font> or compiler and linker versions. To override the default value used in the build and preserved in the flags, specify <tt>&quot;export MACOSX_DEPLOYMENT_TARGET=10.N&quot;</tt> before configuring and building perl, where 10.N is the version of <font SIZE="-1">OS X</font> you wish to target. In <font SIZE="-1">OS X 10.5</font> or earlier there is no change to the behavior present when those systems were current; the link target is still <font SIZE="-1">OS X 10.3</font> and there is no explicit compiler target.</p>
<dt>&bull;</p>
<dd> Builds with both -DDEBUGGING and threading enabled would fail with a &#8220;panic: free from wrong pool&#8221; error when built or tested from Terminal on <font SIZE="-1">OS X.</font> This was caused by perl&#8217;s internal management of the environment conflicting with an atfork handler using the libc <tt>&quot;setenv()&quot;</tt> function to update the environment. </p>
<p> Perl now uses <tt>&quot;setenv()&quot;</tt>/<tt>&quot;unsetenv()&quot;</tt> to update the environment on <font SIZE="-1">OS X.</font> [perl #126240] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126240">https://rt.perl.org/Ticket/Display.html?id=126240</a>&gt;</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Solaris</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> All Solaris variants now build a shared libperl </p>
<p> Solaris and variants like OpenIndiana now always build with the shared Perl library (Configure -Duseshrplib). This was required for the OpenIndiana builds, but this has also been the setting for Oracle/Sun Perl builds for several years.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Tru64</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Workaround where Tru64 balks when prototypes are listed as <tt>&quot;PERL_STATIC_INLINE&quot;</tt>, but where the test is build with <tt>&quot;-DPERL_NO_INLINE_FUNCTIONS&quot;</tt>.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><font SIZE="-1">VMS</font></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> On <font SIZE="-1">VMS,</font> the math function prototypes in <tt>&quot;math.h&quot;</tt> are now visible under C<font SIZE="-2">++</font>. Now building the <font SIZE="-1">POSIX</font> extension with C<font SIZE="-2">++</font> will no longer crash.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">VMS</font> has had <tt>&quot;setenv&quot;</tt>/<tt>&quot;unsetenv&quot;</tt> since v7.0 (released in 1996), <tt>&quot;Perl_vmssetenv&quot;</tt> now always uses <tt>&quot;setenv&quot;</tt>/<tt>&quot;unsetenv&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Perl now implements its own <tt>&quot;killpg&quot;</tt> by scanning for processes in the specified process group, which may not mean exactly the same thing as a Unix process group, but allows us to send a signal to a parent (or master) process and all of its sub-processes. At the perl level, this means we can now send a negative pid like so: </p>
<pre>
    kill SIGKILL, -$pid;
</pre>
<p> to signal all processes in the same group as <tt>$pid</tt>.</p>
<dt>&bull;</p>
<dd> For those <tt>%ENV</tt> elements based on the <font SIZE="-1">CRTL</font> environ array, we&#8217;ve always preserved case when setting them but did look-ups only after upcasing the key first, which made lower- or mixed-case entries go missing. This problem has been corrected by making <tt>%ENV</tt> elements derived from the environ array case-sensitive on look-up as well as case-preserving on store.</p>
<dt>&bull;</p>
<dd> Environment look-ups for <tt>&quot;PERL5LIB&quot;</tt> and <tt>&quot;PERLLIB&quot;</tt> previously only considered logical names, but now consider all sources of <tt>%ENV</tt> as determined by <tt>&quot;PERL_ENV_TABLES&quot;</tt> and as documented in &#8220;%ENV&#8221; in perlvms.</p>
<dt>&bull;</p>
<dd> The minimum supported version of <font SIZE="-1">VMS</font> is now v7.3-2, released in 2003. As a side effect of this change, <font SIZE="-1">VAX</font> is no longer supported as the terminal release of OpenVMS <font SIZE="-1">VAX</font> was v7.3 in 2001.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Win32</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> A new build option <tt>&quot;USE_NO_REGISTRY&quot;</tt> has been added to the makefiles. This option is off by default, meaning the default is to do Windows registry lookups. This option stops Perl from looking inside the registry for anything. For what values are looked up in the registry see perlwin32. Internally, in C, the name of this option is <tt>&quot;WIN32_NO_REGISTRY&quot;</tt>.</p>
<dt>&bull;</p>
<dd> The behavior of Perl using <tt>&quot;HKEY_CURRENT_USER\Software\Perl&quot;</tt> and <tt>&quot;HKEY_LOCAL_MACHINE\Software\Perl&quot;</tt> to lookup certain values, including <tt>%ENV</tt> vars starting with <tt>&quot;PERL&quot;</tt> has changed. Previously, the 2 keys were checked for entries at all times through the perl process&#8217;s life time even if they did not exist. For performance reasons, now, if the root key (i.e. <tt>&quot;HKEY_CURRENT_USER\Software\Perl&quot;</tt> or <tt>&quot;HKEY_LOCAL_MACHINE\Software\Perl&quot;</tt>) does not exist at process start time, it will not be checked again for <tt>%ENV</tt> override entries for the remainder of the perl process&#8217;s life. This more closely matches Unix behavior in that the environment is copied or inherited on startup and changing the variable in the parent process or another process or editing <i>.bashrc</i> will not change the environmental variable in other existing, running, processes.</p>
<dt>&bull;</p>
<dd> One glob fetch was removed for each <tt>&quot;-X&quot;</tt> or <tt>&quot;stat&quot;</tt> call whether done from Perl code or internally from Perl&#8217;s C code. The glob being looked up was <tt>&quot;${^WIN32_SLOPPY_STAT}&quot;</tt> which is a special variable. This makes <tt>&quot;-X&quot;</tt> and <tt>&quot;stat&quot;</tt> slightly faster.</p>
<dt>&bull;</p>
<dd> During miniperl&#8217;s process startup, during the build process, 4 to 8 <font SIZE="-1">IO</font> calls related to the process starting <i>.pl</i> and the <i>buildcustomize.pl</i> file were removed from the code opening and executing the first 1 or 2 <i>.pl</i> files.</p>
<dt>&bull;</p>
<dd> Builds using Microsoft Visual C<font SIZE="-2">++</font> 2003 and earlier no longer produce an &#8220;<font SIZE="-1">INTERNAL COMPILER ERROR&#8221;</font> message. [perl #126045]</p>
<dt>&bull;</p>
<dd> Visual C<font SIZE="-2">++</font> 2013 builds will now execute on <font SIZE="-1">XP</font> and higher. Previously they would only execute on Vista and higher.</p>
<dt>&bull;</p>
<dd> You can now build perl with <font SIZE="-1">GNU</font> Make and <font SIZE="-1">GCC.</font> [perl #123440]</p>
<dt>&bull;</p>
<dd> <tt>&quot;truncate($filename, $size)&quot;</tt> now works for files over 4GB in size. [perl #125347]</p>
<dt>&bull;</p>
<dd> Parallel building has been added to the dmake <tt>&quot;makefile.mk&quot;</tt> makefile. All Win32 compilers are supported.</p>
<dt>&bull;</p>
<dd> Building a 64-bit perl with a 64-bit <font SIZE="-1">GCC</font> but a 32-bit gmake would result in an invalid <tt>$Config{archname}</tt> for the resulting perl. [perl #127584]</p>
<dt>&bull;</p>
<dd> Errors set by Winsock functions are now put directly into <tt>$^E</tt>, and the relevant <tt>&quot;WSAE*&quot;</tt> error codes are now exported from the Errno and <font SIZE="-1">POSIX</font> modules for testing this against. </p>
<p> The previous behavior of putting the errors (converted to POSIX-style <tt>&quot;E*&quot;</tt> error codes since Perl 5.20.0) into <tt>$!</tt> was buggy due to the non-equivalence of like-named Winsock and <font SIZE="-1">POSIX</font> error constants, a relationship between which has unfortunately been established in one way or another since Perl 5.8.0. </p>
<p> The new behavior provides a much more robust solution for checking Winsock errors in portable software without accidentally matching <font SIZE="-1">POSIX</font> tests that were intended for other OSes and may have different meanings for Winsock. </p>
<p> The old behavior is currently retained, warts and all, for backwards compatibility, but users are encouraged to change any code that tests <tt>$!</tt> against <tt>&quot;E*&quot;</tt> constants for Winsock errors to instead test <tt>$^E</tt> against <tt>&quot;WSAE*&quot;</tt> constants. After a suitable deprecation period, the old behavior may be removed, leaving <tt>$!</tt> unchanged after Winsock function calls, to avoid any possible confusion over which error variable to check.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>ppc64el</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>floating point</p>
<dd> The floating point format of ppc64el (Debian naming for little-endian PowerPC) is now detected correctly.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</p>
<dd> The implementation of perl&#8217;s context stack system, and its internal <font SIZE="-1">API,</font> have been heavily reworked. Note that no significant changes have been made to any external APIs, but <font SIZE="-1">XS</font> code which relies on such internal details may need to be fixed. The main changes are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The <tt>&quot;PUSHBLOCK()&quot;</tt>, <tt>&quot;POPSUB()&quot;</tt> etc. macros have been replaced with static inline functions such as <tt>&quot;cx_pushblock()&quot;</tt>, <tt>&quot;cx_popsub()&quot;</tt> etc. These use function args rather than implicitly relying on local vars such as <tt>&quot;gimme&quot;</tt> and <tt>&quot;newsp&quot;</tt> being available. Also their functionality has changed: in particular, <tt>&quot;cx_popblock()&quot;</tt> no longer decrements <tt>&quot;cxstack_ix&quot;</tt>. The ordering of the steps in the <tt>&quot;pp_leave*&quot;</tt> functions involving <tt>&quot;cx_popblock()&quot;</tt>, <tt>&quot;cx_popsub()&quot;</tt> etc. has changed. See the new documentation, &#8220;Dynamic Scope and the Context Stack&#8221; in perlguts, for details on how to use them.</p>
<dt>&bull;</p>
<dd> Various macros, which now consistently have a <font SIZE="-1">CX_</font> prefix, have been added: </p>
<pre>
  CX_CUR(), CX_LEAVE_SCOPE(), CX_POP()
</pre>
<p> or renamed: </p>
<pre>
  CX_POP_SAVEARRAY(), CX_DEBUG(), CX_PUSHSUBST(), CX_POPSUBST()
</pre>
<dt>&bull;</p>
<dd> <tt>&quot;cx_pushblock()&quot;</tt> now saves <tt>&quot;PL_savestack_ix&quot;</tt> and <tt>&quot;PL_tmps_floor&quot;</tt>, so <tt>&quot;pp_enter*&quot;</tt> and <tt>&quot;pp_leave*&quot;</tt> no longer do </p>
<pre>
  ENTER; SAVETMPS; ....; LEAVE
</pre>
<dt>&bull;</p>
<dd> <tt>&quot;cx_popblock()&quot;</tt> now also restores <tt>&quot;PL_curpm&quot;</tt>.</p>
<dt>&bull;</p>
<dd> In <tt>&quot;dounwind()&quot;</tt> for every context type, the current savestack frame is now processed before each context is popped; formerly this was only done for sub-like context frames. This action has been removed from <tt>&quot;cx_popsub()&quot;</tt> and placed into its own macro, <tt>&quot;CX_LEAVE_SCOPE(cx)&quot;</tt>, which must be called before <tt>&quot;cx_popsub()&quot;</tt> etc. </p>
<p> <tt>&quot;dounwind()&quot;</tt> now also does a <tt>&quot;cx_popblock()&quot;</tt> on the last popped frame (formerly it only did the <tt>&quot;cx_popsub()&quot;</tt> etc. actions on each frame).</p>
<dt>&bull;</p>
<dd> The temps stack is now freed on scope exit; previously, temps created during the last statement of a block wouldn&#8217;t be freed until the next <tt>&quot;nextstate&quot;</tt> following the block (apart from an existing hack that did this for recursive subs in scalar context); and in something like <tt>&quot;f(g())&quot;</tt>, the temps created by the last statement in <tt>&quot;g()&quot;</tt> would formerly not be freed until the statement following the return from <tt>&quot;f()&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Most values that were saved on the savestack on scope entry are now saved in suitable new fields in the context struct, and saved and restored directly by <tt>&quot;cx_pushfoo()&quot;</tt> and <tt>&quot;cx_popfoo()&quot;</tt>, which is much faster.</p>
<dt>&bull;</p>
<dd> Various context struct fields have been added, removed or modified.</p>
<dt>&bull;</p>
<dd> The handling of <tt>@_</tt> in <tt>&quot;cx_pushsub()&quot;</tt> and <tt>&quot;cx_popsub()&quot;</tt> has been considerably tidied up, including removing the <tt>&quot;argarray&quot;</tt> field from the context struct, and extracting out some common (but rarely used) code into a separate function, <tt>&quot;clear_defarray()&quot;</tt>. Also, useful subsets of <tt>&quot;cx_popsub()&quot;</tt> which had been unrolled in places like <tt>&quot;pp_goto&quot;</tt> have been gathered into the new functions <tt>&quot;cx_popsub_args()&quot;</tt> and <tt>&quot;cx_popsub_common()&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;pp_leavesub&quot;</tt> and <tt>&quot;pp_leavesublv&quot;</tt> now use the same function as the rest of the <tt>&quot;pp_leave*&quot;</tt>&#8216;s to process return args.</p>
<dt>&bull;</p>
<dd> <tt>&quot;CXp_FOR_PAD&quot;</tt> and <tt>&quot;CXp_FOR_GV&quot;</tt> flags have been added, and <tt>&quot;CXt_LOOP_FOR&quot;</tt> has been split into <tt>&quot;CXt_LOOP_LIST&quot;</tt>, <tt>&quot;CXt_LOOP_ARY&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Some variables formerly declared by <tt>&quot;dMULTICALL&quot;</tt> (but not documented) have been removed.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> The obscure <tt>&quot;PL_timesbuf&quot;</tt> variable, effectively a vestige of Perl 1, has been removed. It was documented as deprecated in Perl 5.20, with a statement that it would be removed early in the 5.21.x series; that has now finally happened. [perl #121351] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121351">https://rt.perl.org/Ticket/Display.html?id=121351</a>&gt;</p>
<dt>&bull;</p>
<dd> An unwarranted assertion in <tt>&quot;Perl_newATTRSUB_x()&quot;</tt> has been removed. If a stub subroutine definition with a prototype has been seen, then any subsequent stub (or definition) of the same subroutine with an attribute was causing an assertion failure because of a null pointer. [perl #126845] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126845">https://rt.perl.org/Ticket/Display.html?id=126845</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;::&quot;</tt> has been replaced by <tt>&quot;__&quot;</tt> in <tt>&quot;ExtUtils::ParseXS&quot;</tt>, like it&#8217;s done for parameters/return values. This is more consistent, and simplifies writing <font SIZE="-1">XS</font> code wrapping C<font SIZE="-2">++</font> classes into a nested Perl namespace (it requires only a typedef for <tt>&quot;Foo__Bar&quot;</tt> rather than two, one for <tt>&quot;Foo_Bar&quot;</tt> and the other for <tt>&quot;Foo::Bar&quot;</tt>).</p>
<dt>&bull;</p>
<dd> The <tt>&quot;to_utf8_case()&quot;</tt> function is now deprecated. Instead use <tt>&quot;toUPPER_utf8&quot;</tt>, <tt>&quot;toTITLE_utf8&quot;</tt>, <tt>&quot;toLOWER_utf8&quot;</tt>, and <tt>&quot;toFOLD_utf8&quot;</tt>. (See &lt;<a rel="nofollow" href="http://nntp.perl.org/group/perl.perl5.porters/233287">http://nntp.perl.org/group/perl.perl5.porters/233287</a>&gt;.)</p>
<dt>&bull;</p>
<dd> Perl core code and the threads extension have been annotated so that, if Perl is configured to use threads, then during compile-time clang (3.6 or later) will warn about suspicious uses of mutexes. See &lt;<a rel="nofollow" href="http://clang.llvm.org/docs/ThreadSafetyAnalysis.html">http://clang.llvm.org/docs/ThreadSafetyAnalysis.html</a>&gt; for more information.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;signbit()&quot;</tt> emulation has been enhanced. This will help older and/or more exotic platforms or configurations.</p>
<dt>&bull;</p>
<dd> Most EBCDIC-specific code in the core has been unified with non-EBCDIC code, to avoid repetition and make maintenance easier.</p>
<dt>&bull;</p>
<dd> MSWin32 code for <tt>$^X</tt> has been moved out of the <i>win32</i> directory to <i>caretx.c</i>, where other operating systems set that variable.</p>
<dt>&bull;</p>
<dd> <tt>&quot;sv_ref()&quot;</tt> is now part of the <font SIZE="-1">API.</font></p>
<dt>&bull;</p>
<dd> &#8220;sv_backoff&#8221; in perlapi had its return type changed from <tt>&quot;int&quot;</tt> to <tt>&quot;void&quot;</tt>. It previously has always returned <tt>0</tt> since Perl 5.000 stable but that was undocumented. Although <tt>&quot;sv_backoff&quot;</tt> is marked as public <font SIZE="-1">API, XS</font> code is not expected to be impacted since the proper <font SIZE="-1">API</font> call would be through public <font SIZE="-1">API</font> <tt>&quot;sv_setsv(sv, &amp;PL_sv_undef)&quot;</tt>, or quasi-public <tt>&quot;SvOOK_off&quot;</tt>, or non-public <tt>&quot;SvOK_off&quot;</tt> calls, and the return value of <tt>&quot;sv_backoff&quot;</tt> was previously a meaningless constant that can be rewritten as <tt>&quot;(sv_backoff(sv),0)&quot;</tt>.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;EXTEND&quot;</tt> and <tt>&quot;MEXTEND&quot;</tt> macros have been improved to avoid various issues with integer truncation and wrapping. In particular, some casts formerly used within the macros have been removed. This means for example that passing an unsigned <tt>&quot;nitems&quot;</tt> argument is likely to raise a compiler warning now (it&#8217;s always been documented to require a signed value; formerly int, lately SSize_t).</p>
<dt>&bull;</p>
<dd> <tt>&quot;PL_sawalias&quot;</tt> and <tt>&quot;GPf_ALIASED_SV&quot;</tt> have been removed.</p>
<dt>&bull;</p>
<dd> <tt>&quot;GvASSIGN_GENERATION&quot;</tt> and <tt>&quot;GvASSIGN_GENERATION_set&quot;</tt> have been removed.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> It now works properly to specify a user-defined property, such as </p>
<pre>
 qr/\p{mypkg1::IsMyProperty}/i
</pre>
<p> with <tt>&quot;/i&quot;</tt> caseless matching, an explicit package name, and <i>IsMyProperty</i> not defined at the time of the pattern compilation.</p>
<dt>&bull;</p>
<dd> Perl&#8217;s <tt>&quot;memcpy()&quot;</tt>, <tt>&quot;memmove()&quot;</tt>, <tt>&quot;memset()&quot;</tt> and <tt>&quot;memcmp()&quot;</tt> fallbacks are now more compatible with the originals. [perl #127619]</p>
<dt>&bull;</p>
<dd> Fixed the issue where a <tt>&quot;s///r&quot;</tt>) with <code>-DPERL_NO_COW</code> attempts to modify the source <font SIZE="-1">SV,</font> resulting in the program dying. [perl #127635]</p>
<dt>&bull;</p>
<dd> Fixed an EBCDIC-platform-only case where a pattern could fail to match. This occurred when matching characters from the set of C1 controls when the target matched string was in <font SIZE="-1">UTF-8.</font></p>
<dt>&bull;</p>
<dd> Narrow the filename check in <i>strict.pm</i> and <i>warnings.pm</i>. Previously, it assumed that if the filename (without the <i>.pmc?</i> extension) differed from the package name, if was a misspelled use statement (i.e. <tt>&quot;use Strict&quot;</tt> instead of <tt>&quot;use strict&quot;</tt>). We now check whether there&#8217;s really a miscapitalization happening, and not some other issue.</p>
<dt>&bull;</p>
<dd> Turn an assertion into a more user friendly failure when parsing regexes. [perl #127599]</p>
<dt>&bull;</p>
<dd> Correctly raise an error when trying to compile patterns with unterminated character classes while there are trailing backslashes. [perl #126141].</p>
<dt>&bull;</p>
<dd> Line numbers larger than 2**31-1 but less than 2**32 are no longer returned by <tt>&quot;caller()&quot;</tt> as negative numbers. [perl #126991]</p>
<dt>&bull;</p>
<dd> <tt>&quot;unless ( </tt>assignment<tt> )&quot;</tt> now properly warns when syntax warnings are enabled. [perl #127122]</p>
<dt>&bull;</p>
<dd> Setting an <tt>&quot;ISA&quot;</tt> glob to an array reference now properly adds <tt>&quot;isaelem&quot;</tt> magic to any existing elements. Previously modifying such an element would not update the <font SIZE="-1">ISA</font> cache, so method calls would call the wrong function. Perl would also crash if the <tt>&quot;ISA&quot;</tt> glob was destroyed, since new code added in 5.23.7 would try to release the <tt>&quot;isaelem&quot;</tt> magic from the elements. [perl #127351]</p>
<dt>&bull;</p>
<dd> If a here-doc was found while parsing another operator, the parser had already read end of file, and the here-doc was not terminated, perl could produce an assertion or a segmentation fault. This now reliably complains about the unterminated here-doc. [perl #125540]</p>
<dt>&bull;</p>
<dd> <tt>&quot;untie()&quot;</tt> would sometimes return the last value returned by the <tt>&quot;UNTIE()&quot;</tt> handler as well as it&#8217;s normal value, messing up the stack. [perl #126621]</p>
<dt>&bull;</p>
<dd> Fixed an operator precedence problem when <tt>&quot; castflags &amp; 2&quot;</tt> is true. [perl #127474]</p>
<dt>&bull;</p>
<dd> Caching of <font SIZE="-1">DESTROY</font> methods could result in a non-pointer or a non-STASH stored in the <tt>&quot;SvSTASH()&quot;</tt> slot of a stash, breaking the B <tt>&quot;STASH()&quot;</tt> method. The <font SIZE="-1">DESTROY</font> method is now cached in the <font SIZE="-1">MRO</font> metadata for the stash. [perl #126410]</p>
<dt>&bull;</p>
<dd> The <font SIZE="-1">AUTOLOAD</font> method is now called when searching for a <font SIZE="-1">DESTROY</font> method, and correctly sets <tt>$AUTOLOAD</tt> too. [perl #124387] [perl #127494]</p>
<dt>&bull;</p>
<dd> Avoid parsing beyond the end of the buffer when processing a <tt>&quot;#line&quot;</tt> directive with no filename. [perl #127334]</p>
<dt>&bull;</p>
<dd> Perl now raises a warning when a regular expression pattern looks like it was supposed to contain a <font SIZE="-1">POSIX</font> class, like <tt>&quot;qr/[[:alpha:]]/&quot;</tt>, but there was some slight defect in its specification which causes it to instead be treated as a regular bracketed character class. An example would be missing the second colon in the above like this: <tt>&quot;qr/[[:alpha]]/&quot;</tt>. This compiles to match a sequence of two characters. The second is <tt>&quot;]&quot;</tt>, and the first is any of: <tt>&quot;[&quot;</tt>, <tt>&quot;:&quot;</tt>, <tt>&quot;a&quot;</tt>, <tt>&quot;h&quot;</tt>, <tt>&quot;l&quot;</tt>, or <tt>&quot;p&quot;</tt>. This is unlikely to be the intended meaning, and now a warning is raised. No warning is raised unless the specification is very close to one of the 14 legal <font SIZE="-1">POSIX</font> classes. (See &#8220;<font SIZE="-1">POSIX</font> Character Classes&#8221; in perlrecharclass.) [perl #8904]</p>
<dt>&bull;</p>
<dd> Certain regex patterns involving a complemented <font SIZE="-1">POSIX</font> class in an inverted bracketed character class, and matching something else optionally would improperly fail to match. An example of one that could fail is <tt>&quot;qr/_?[^\Wbar]
