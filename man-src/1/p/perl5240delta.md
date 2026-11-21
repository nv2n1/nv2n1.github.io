---

title: "perl5240delta(1)"
name: "perl5240delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5240delta/"
description: "perl5240delta – what is new for perl v5.24.0"
---

<p> This document describes the differences between the 5.22.0 release and the 5.24.0 release.  </p>
<h2>Core Enhancements</h2>
<h3>Postfix dereferencing is no longer experimental</h3>
<p> Using the <code>&quot;postderef&quot;</code> and <code>&quot;postderef_qq&quot;</code> features no longer emits a warning. Existing code that disables the <code>&quot;experimental::postderef&quot;</code> warning category that they previously used will continue to work. The <code>&quot;postderef&quot;</code> feature has no effect; all Perl code can use postfix dereferencing, regardless of what feature declarations are in scope. The <code>5.24</code> feature bundle now includes the <code>&quot;postderef_qq&quot;</code> feature.  </p>
<h3>Unicode 8.0 is now supported</h3>
<p> For details on what is in this release, see &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode8.0.0/">http://www.unicode.org/versions/Unicode8.0.0/</a>&gt;.  </p>
<h3>perl will now croak when closing an in-place output file fails</h3>
<p> Until now, failure to close the output file for an in-place edit was not detected, meaning that the input file could be clobbered without the edit being successfully completed. Now, when the output file cannot be closed successfully, an exception is raised.  </p>
<h3>New \b{lb} boundary in regular expressions</h3>
<p> <code>&quot;lb&quot;</code> stands for Line Break. It is a Unicode property that determines where a line of text is suitable to break (typically so that it can be output without overflowing the available horizontal space). This capability has long been furnished by the Unicode::LineBreak module, but now a light-weight, non-customizable version that is suitable for many purposes is in core Perl.  </p>
<font SIZE="-1"></font><h3>qr/(?[ ])/ now works in UTF-8 locales</h3>
<p> Extended Bracketed Character Classes now will successfully compile when <code>&quot;use locale&quot;</code> is in effect. The compiled pattern will use standard Unicode rules. If the runtime locale is not a <font SIZE="-1">UTF-8</font> one, a warning is raised and standard Unicode rules are used anyway. No tainting is done since the outcome does not actually depend on the locale.  </p>
<h3>Integer shift (&lt;&lt; and &gt;&gt;) now more explicitly defined</h3>
<p> Negative shifts are reverse shifts: left shift becomes right shift, and right shift becomes left shift. </p>
<p> Shifting by the number of bits in a native integer (or more) is zero, except when the ``overshift&#8217;&#8216; is right shifting a negative value under <code>&quot;use integer&quot;</code>, in which case the result is -1 (arithmetic shift). </p>
<p> Until now negative shifting and overshifting have been undefined because they have relied on whatever the C implementation happens to do. For example, for the overshift a common C behavior is ``modulo shift&#8217;&#8216;: </p>
<pre><code>  1 &gt;&gt; 64 == 1 &gt;&gt; (64 % 64) == 1 &gt;&gt; 0 == 1 # Common C behavior.
  # And the same for &lt;&lt;, while Perl now produces 0 for both.
</code></pre>
<p> Now these behaviors are well-defined under Perl, regardless of what the underlying C implementation does. Note, however, that you are still constrained by the native integer width: you need to know how far left you can go. You can use for example: </p>
<pre><code>  use Config;
  my $wordbits = $Config{uvsize} * 8; # Or $Config{uvsize} &lt;&lt; 3.
</code></pre>
<p> If you need a more bits on the left shift, you can use for example the <code>&quot;bigint&quot;</code> pragma, or the <code>&quot;Bit::Vector&quot;</code> module from <font SIZE="-1">CPAN.</font>  </p>
<h3>printf and sprintf now allow reordered precision arguments</h3>
<p> That is, <code>&quot;sprintf &#8216;|%.*2$d|&#8216;, 2, 3&quot;</code> now returns <code>&quot;|002|&quot;</code>. This extends the existing reordering mechanism (which allows reordering for arguments that are used as format fields, widths, and vector separators).  </p>
<h3>More fields provided to sigaction callback with SA_SIGINFO</h3>
<p> When passing the <code>&quot;SA_SIGINFO&quot;</code> flag to sigaction, the <code>&quot;errno&quot;</code>, <code>&quot;status&quot;</code>, <code>&quot;uid&quot;</code>, <code>&quot;pid&quot;</code>, <code>&quot;addr&quot;</code> and <code>&quot;band&quot;</code> fields are now included in the hash passed to the handler, if supported by the platform.  </p>
<h3>Hashbang redirection to Perl 6</h3>
<p> Previously perl would redirect to another interpreter if it found a hashbang path unless the path contains ``perl&#8217;&#8216; (see perlrun). To improve compatibility with Perl 6 this behavior has been extended to also redirect if ``perl&#8217;&#8216; is followed by ``6&#8217;&#8216;.  </p>
<h2>Security</h2>
<a href="/docs/linux/man/3-mkstemp/"></a><h3>Set proper umask before calling mkstemp (3)</h3>
<p> In 5.22 perl started setting umask to 0600 before calling <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a>(3)</code> and restoring it afterwards. This wrongfully tells <code><a href="/docs/linux/man/2-open/">open</a>(2)</code> to strip the owner read and write bits from the given mode before applying it, rather than the intended negation of leaving only those bits in place. </p>
<p> Systems that use mode 0666 in <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a>(3)</code> (like old versions of glibc) create a file with permissions 0066, leaving world read and write permissions regardless of current umask. </p>
<p> This has been fixed by using umask 0177 instead. [perl #127322]  </p>
<h3>Fix out of boundary access in Win32 path handling</h3>
<p> This is <font SIZE="-1">CVE-2015-8608.</font> For more information see [perl #126755] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126755">https://rt.perl.org/Ticket/Display.html?id=126755</a>&gt;  </p>
<h3>Fix loss of taint in canonpath</h3>
<p> This is <font SIZE="-1">CVE-2015-8607.</font> For more information see [perl #126862] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126862">https://rt.perl.org/Ticket/Display.html?id=126862</a>&gt;  </p>
<h3>Avoid accessing uninitialized memory in win32 crypt()</h3>
<p> Added validation that will detect both a short salt and invalid characters in the salt. [perl #126922] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126922">https://rt.perl.org/Ticket/Display.html?id=126922</a>&gt;  </p>
<h3>Remove duplicate environment variables from environ</h3>
<p> Previously, if an environment variable appeared more than once in <code>&quot;environ[]&quot;</code>, <code>%ENV</code> would contain the last entry for that name, while a typical <code>&quot;getenv()&quot;</code> would return the first entry. We now make sure <code>%ENV</code> contains the same as what <code>&quot;getenv&quot;</code> returns. </p>
<p> Second, we remove duplicates from <code>&quot;environ[]&quot;</code>, so if a setting with that name is set in <code>%ENV</code>, we won&#8217;t pass an unsafe value to a child process. </p>
<p> [<font SIZE="-1">CVE-2016-2381</font>]  </p>
<h2>Incompatible Changes</h2>
<h3>The autoderef feature has been removed</h3>
<p> The experimental <code>&quot;autoderef&quot;</code> feature (which allowed calling <code>&quot;push&quot;</code>, <code>&quot;pop&quot;</code>, <code>&quot;shift&quot;</code>, <code>&quot;unshift&quot;</code>, <code>&quot;splice&quot;</code>, <code>&quot;keys&quot;</code>, <code>&quot;values&quot;</code>, and <code>&quot;each&quot;</code> on a scalar argument) has been deemed unsuccessful. It has now been removed; trying to use the feature (or to disable the <code>&quot;experimental::autoderef&quot;</code> warning it previously triggered) now yields an exception.  </p>
<h3>Lexical $_ has been removed</h3>
<p> <code>&quot;my $_&quot;</code> was introduced in Perl 5.10, and subsequently caused much confusion with no obvious solution. In Perl 5.18.0, it was made experimental on the theory that it would either be removed or redesigned in a less confusing (but backward-incompatible) way. Over the following years, no alternatives were proposed. The feature has now been removed and will fail to compile.  </p>
<h3>qr/\b{wb}/ is now tailored to Perl expectations</h3>
<p> This is now more suited to be a drop-in replacement for plain <code>&quot;\b&quot;</code>, but giving better results for parsing natural language. Previously it strictly followed the current Unicode rules which calls for it to match between each white space character. Now it doesn&#8217;t generally match within spans of white space, behaving like <code>&quot;\b&quot;</code> does. See ``\b{wb}&#8216;&#8216; in perlrebackslash  </p>
<h3>Regular expression compilation errors</h3>
<p> Some regular expression patterns that had runtime errors now don&#8217;t compile at all. </p>
<p> Almost all Unicode properties using the <code>&quot;\p{}&quot;</code> and <code>&quot;\P{}&quot;</code> regular expression pattern constructs are now checked for validity at pattern compilation time, and invalid ones will cause the program to not compile. In earlier releases, this check was often deferred until run time. Whenever an error check is moved from run- to compile time, erroneous code is caught 100% of the time, whereas before it would only get caught if and when the offending portion actually gets executed, which for unreachable code might be never.  </p>
<h3>qr/\N{}/ now disallowed under use re strict</h3>
<p> An empty <code>&quot;\N{}&quot;</code> makes no sense, but for backwards compatibility is accepted as doing nothing, though a deprecation warning is raised by default. But now this is a fatal error under the experimental feature ``&#8216;strict&#8217; mode&#8217;&#8216; in re.  </p>
<h3>Nested declarations are now disallowed</h3>
<p> A <code>&quot;my&quot;</code>, <code>&quot;our&quot;</code>, or <code>&quot;state&quot;</code> declaration is no longer allowed inside of another <code>&quot;my&quot;</code>, <code>&quot;our&quot;</code>, or <code>&quot;state&quot;</code> declaration. </p>
<p> For example, these are now fatal: </p>
<pre><code>   my ($x, my($y));
   our (my $x);
</code></pre>
<p> [perl #125587] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125587">https://rt.perl.org/Ticket/Display.html?id=125587</a>&gt; </p>
<p> [perl #121058] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121058">https://rt.perl.org/Ticket/Display.html?id=121058</a>&gt;  </p>
<h3>The /\C/ character class has been removed.</h3>
<p> This regular expression character class was deprecated in v5.20.0 and has produced a deprecation warning since v5.22.0. It is now a compile-time error. If you need to examine the individual bytes that make up a UTF8-encoded character, then use <code>&quot;utf8::encode()&quot;</code> on the string (or a copy) first.  </p>
<h3>chdir('') no longer chdirs home</h3>
<p> Using <code>&quot;chdir(&#8216;&#8216;)&quot;</code> or <code>&quot;chdir(undef)&quot;</code> to chdir home has been deprecated since perl v5.8, and will now fail. Use <code>&quot;chdir()&quot;</code> instead.  </p>
<font SIZE="-1"></font><h3>ASCII characters in variable names must now be all visible</h3>
<p> It was legal until now on <font SIZE="-1">ASCII</font> platforms for variable names to contain non-graphical <font SIZE="-1">ASCII</font> control characters (ordinals 0 through 31, and 127, which are the C0 controls and <code>&quot;DELETE&quot;</code>). This usage has been deprecated since v5.20, and as of now causes a syntax error. The variables these names referred to are special, reserved by Perl for whatever use it may choose, now, or in the future. Each such variable has an alternative way of spelling it. Instead of the single non-graphic control character, a two character sequence beginning with a caret is used, like <code>$^]</code> and <code>&quot;${^GLOBAL_PHASE}&quot;</code>. Details are at perlvar. It remains legal, though unwise and deprecated (raising a deprecation warning), to use certain non-graphic non-ASCII characters in variables names when not under <code>&quot;use utf8&quot;</code>. No code should do this, as all such variables are reserved by Perl, and Perl doesn&#8217;t currently define any of them (but could at any time, without notice).  </p>
<h3>An off by one issue in $Carp::MaxArgNums has been fixed</h3>
<p> <code>$Carp::MaxArgNums</code> is supposed to be the number of arguments to display. Prior to this version, it was instead showing <code>$Carp::MaxArgNums</code> + 1 arguments, contrary to the documentation.  </p>
<h3>Only blanks and tabs are now allowed within [...] within (?[...]).</h3>
<p> The experimental Extended Bracketed Character Classes can contain regular bracketed character classes within them. These differ from regular ones in that white space is generally ignored, unless escaped by preceding it with a backslash. The white space that is ignored is now limited to just tab <code>&quot;\t&quot;</code> and <font SIZE="-1">SPACE</font> characters. Previously, it was any white space. See ``Extended Bracketed Character Classes&#8217;&#8216; in perlrecharclass.  </p>
<h2>Deprecations</h2>
<h3>Using code points above the platform's IV_MAX is now deprecated</h3>
<p> Unicode defines code points in the range <code>&quot;0..0x10FFFF&quot;</code>. Some standards at one time defined them up to 2**31 - 1, but Perl has allowed them to be as high as anything that will fit in a word on the platform being used. However, use of those above the platform&#8217;s <code>&quot;IV_MAX&quot;</code> is broken in some constructs, notably <code>&quot;tr///&quot;</code>, regular expression patterns involving quantifiers, and in some arithmetic and comparison operations, such as being the upper limit of a loop. Now the use of such code points raises a deprecation warning, unless that warning category is turned off. <code>&quot;IV_MAX&quot;</code> is typically 2**31 -1 on 32-bit platforms, and 2**63-1 on 64-bit ones.  </p>
<h3>Doing bitwise operations on strings containing code points above 0xFF is deprecated</h3>
<p> The string bitwise operators treat their operands as strings of bytes, and values beyond 0xFF are nonsensical in this context. To operate on encoded bytes, first encode the strings. To operate on code points&#8217; numeric values, use <code>&quot;split&quot;</code> and <code>&quot;map ord&quot;</code>. In the future, this warning will be replaced by an exception.  </p>
<h3>sysread(), syswrite(), recv() and send() are deprecated on :utf8 handles</h3>
<p> The <code>&quot;sysread()&quot;</code>, <code>&quot;recv()&quot;</code>, <code>&quot;syswrite()&quot;</code> and <code>&quot;send()&quot;</code> operators are deprecated on handles that have the <code>&quot;:utf8&quot;</code> layer, either explicitly, or implicitly, eg., with the <code>&quot;:encoding(UTF-16LE)&quot;</code> layer. </p>
<p> Both <code>&quot;sysread()&quot;</code> and <code>&quot;recv()&quot;</code> currently use only the <code>&quot;:utf8&quot;</code> flag for the stream, ignoring the actual layers. Since <code>&quot;sysread()&quot;</code> and <code>&quot;recv()&quot;</code> do no <font SIZE="-1">UTF-8</font> validation they can end up creating invalidly encoded scalars. </p>
<p> Similarly, <code>&quot;syswrite()&quot;</code> and <code>&quot;send()&quot;</code> use only the <code>&quot;:utf8&quot;</code> flag, otherwise ignoring any layers. If the flag is set, both write the value <font SIZE="-1">UTF-8</font> encoded, even if the layer is some different encoding, such as the example above. </p>
<p> Ideally, all of these operators would completely ignore the <code>&quot;:utf8&quot;</code> state, working only with bytes, but this would result in silently breaking existing code. To avoid this a future version of perl will throw an exception when any of <code>&quot;sysread()&quot;</code>, <code>&quot;recv()&quot;</code>, <code>&quot;syswrite()&quot;</code> or <code>&quot;send()&quot;</code> are called on handle with the <code>&quot;:utf8&quot;</code> layer.  </p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The overhead of scope entry and exit has been considerably reduced, so for example subroutine calls, loops and basic blocks are all faster now. This empty function call now takes about a third less time to execute: </p>
<pre><code>    sub f{} f();
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Many languages, such as Chinese, are caseless. Perl now knows about most common ones, and skips much of the work when a program tries to change case in them (like <code>&quot;ucfirst()&quot;</code>) or match caselessly (<code>&quot;qr//i&quot;</code>). This will speed up a program, such as a web server, that can operate on multiple languages, while it is operating on a caseless one. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;/fixed-substr/&quot;</code> has been made much faster. </p>
<p> On platforms with a libc <code>&quot;memchr()&quot;</code> implementation which makes good use of underlying hardware support, patterns which include fixed substrings will now often be much faster; for example with glibc on a recent x86_64 <font SIZE="-1">CPU,</font> this: </p>
<pre><code>    $s = &quot;a&quot; x 1000 . &quot;wxyz&quot;;
    $s =~ /wxyz/ for 1..30000
</code></pre>
<p> is now about 7 times faster. On systems with slow <code>&quot;memchr()&quot;</code>, e.g. 32-bit <font SIZE="-1">ARM</font> Raspberry Pi, there will be a small or little speedup. Conversely, some pathological cases, such as <code>&quot;&quot;ab&quot; x 1000 =~ /aa/&quot;</code> will be slower now; up to 3 times slower on the rPi, 1.5x slower on x86_64. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Faster addition, subtraction and multiplication. </p>
<p> Since 5.8.0, arithmetic became slower due to the need to support 64-bit integers. To deal with 64-bit integers, a lot more corner cases need to be checked, which adds time. We now detect common cases where there is no need to check for those corner cases, and special-case them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Preincrement, predecrement, postincrement, and postdecrement have been made faster by internally splitting the functions which handled multiple cases into different functions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Creating Perl debugger data structures (see ``Debugger Internals&#8217;&#8216; in perldebguts) for XSUBs and const subs has been removed. This removed one glob/scalar combo for each unique <code>&quot;.c&quot;</code> file that XSUBs and const subs came from. On startup (<code>&quot;perl -e&quot;0&quot;&quot;</code>) about half a dozen glob/scalar debugger combos were created. Loading <font SIZE="-1">XS</font> modules created more glob/scalar combos. These things were being created regardless of whether the perl debugger was being used, and despite the fact that it can&#8217;t debug C code anyway </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On Win32, <code>&quot;stat&quot;</code>ing or <code>&quot;-X&quot;</code>ing a path, if the file or directory does not exist, is now 3.5x faster than before. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Single arguments in list assign are now slightly faster: </p>
<pre><code>  ($x) = (...);
  (...) = ($x);
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Less peak memory is now used when compiling regular expression patterns. </p>
 </dd></dl>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> arybase has been upgraded from version 0.10 to 0.11. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Attribute::Handlers has been upgraded from version 0.97 to 0.99. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> autodie has been upgraded from version 2.26 to 2.29. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> autouse has been upgraded from version 1.08 to 1.11. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B has been upgraded from version 1.58 to 1.62. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Deparse has been upgraded from version 1.35 to 1.37. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> base has been upgraded from version 2.22 to 2.23. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Benchmark has been upgraded from version 1.2 to 1.22. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> bignum has been upgraded from version 0.39 to 0.42. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> bytes has been upgraded from version 1.04 to 1.05. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Carp has been upgraded from version 1.36 to 1.40. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compress::Raw::Bzip2 has been upgraded from version 2.068 to 2.069. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compress::Raw::Zlib has been upgraded from version 2.068 to 2.069. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Config::Perl::V has been upgraded from version 0.24 to 0.25. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> CPAN::Meta has been upgraded from version 2.150001 to 2.150005. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> CPAN::Meta::Requirements has been upgraded from version 2.132 to 2.140. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> CPAN::Meta::YAML has been upgraded from version 0.012 to 0.018. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Data::Dumper has been upgraded from version 2.158 to 2.160. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::Peek has been upgraded from version 1.22 to 1.23. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::PPPort has been upgraded from version 3.31 to 3.32. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Dumpvalue has been upgraded from version 1.17 to 1.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DynaLoader has been upgraded from version 1.32 to 1.38. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Encode has been upgraded from version 2.72 to 2.80. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> encoding has been upgraded from version 2.14 to 2.17. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> encoding::warnings has been upgraded from version 0.11 to 0.12. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> English has been upgraded from version 1.09 to 1.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Errno has been upgraded from version 1.23 to 1.25. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> experimental has been upgraded from version 0.013 to 0.016. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::CBuilder has been upgraded from version 0.280221 to 0.280225. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Embed has been upgraded from version 1.32 to 1.33. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::MakeMaker has been upgraded from version 7.04_01 to 7.10_01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::ParseXS has been upgraded from version 3.28 to 3.31. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Typemaps has been upgraded from version 3.28 to 3.31. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> feature has been upgraded from version 1.40 to 1.42. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> fields has been upgraded from version 2.17 to 2.23. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Find has been upgraded from version 1.29 to 1.34. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Glob has been upgraded from version 1.24 to 1.26. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Path has been upgraded from version 2.09 to 2.12_01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Spec has been upgraded from version 3.56 to 3.63. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Filter::Util::Call has been upgraded from version 1.54 to 1.55. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Getopt::Long has been upgraded from version 2.45 to 2.48. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hash::Util has been upgraded from version 0.18 to 0.19. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hash::Util::FieldHash has been upgraded from version 1.15 to 1.19. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> HTTP::Tiny has been upgraded from version 0.054 to 0.056. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> I18N::Langinfo has been upgraded from version 0.12 to 0.13. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> if has been upgraded from version 0.0604 to 0.0606. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">IO</font> has been upgraded from version 1.35 to 1.36. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO-Compress has been upgraded from version 2.068 to 2.069. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::Open3 has been upgraded from version 1.18 to 1.20. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::SysV has been upgraded from version 2.04 to 2.06_01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> List::Util has been upgraded from version 1.41 to 1.42_02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> locale has been upgraded from version 1.06 to 1.08. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locale::Codes has been upgraded from version 3.34 to 3.37. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigInt has been upgraded from version 1.9997 to 1.999715. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigInt::FastCalc has been upgraded from version 0.31 to 0.40. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigRat has been upgraded from version 0.2608 to 0.260802. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::CoreList has been upgraded from version 5.20150520 to 5.20160320. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Metadata has been upgraded from version 1.000026 to 1.000031. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> mro has been upgraded from version 1.17 to 1.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ODBM_File has been upgraded from version 1.12 to 1.14. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Opcode has been upgraded from version 1.32 to 1.34. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> parent has been upgraded from version 0.232 to 0.234. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Parse::CPAN::Meta has been upgraded from version 1.4414 to 1.4417. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl::OSType has been upgraded from version 1.008 to 1.009. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlfaq has been upgraded from version 5.021009 to 5.021010. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::encoding has been upgraded from version 0.21 to 0.24. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::mmap has been upgraded from version 0.014 to 0.016. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::scalar has been upgraded from version 0.22 to 0.24. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::via has been upgraded from version 0.15 to 0.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Functions has been upgraded from version 1.09 to 1.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Perldoc has been upgraded from version 3.25 to 3.25_02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Simple has been upgraded from version 3.29 to 3.32. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Usage has been upgraded from version 1.64 to 1.68. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">POSIX</font> has been upgraded from version 1.53 to 1.65. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Scalar::Util has been upgraded from version 1.41 to 1.42_02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> SDBM_File has been upgraded from version 1.13 to 1.14. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> SelfLoader has been upgraded from version 1.22 to 1.23. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Socket has been upgraded from version 2.018 to 2.020_03. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Storable has been upgraded from version 2.53 to 2.56. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> strict has been upgraded from version 1.09 to 1.11. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Term::ANSIColor has been upgraded from version 4.03 to 4.04. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Term::Cap has been upgraded from version 1.15 to 1.17. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test has been upgraded from version 1.26 to 1.28. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test::Harness has been upgraded from version 3.35 to 3.36. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Thread::Queue has been upgraded from version 3.05 to 3.08. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> threads has been upgraded from version 2.01 to 2.06. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> threads::shared has been upgraded from version 1.48 to 1.50. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::File has been upgraded from version 1.01 to 1.02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::Scalar has been upgraded from version 1.03 to 1.04. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::HiRes has been upgraded from version 1.9726 to 1.9732. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::Piece has been upgraded from version 1.29 to 1.31. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::Collate has been upgraded from version 1.12 to 1.14. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::Normalize has been upgraded from version 1.18 to 1.25. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::UCD has been upgraded from version 0.61 to 0.64. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">UNIVERSAL</font> has been upgraded from version 1.12 to 1.13. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> utf8 has been upgraded from version 1.17 to 1.19. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> version has been upgraded from version 0.9909 to 0.9916. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> warnings has been upgraded from version 1.32 to 1.36. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Win32 has been upgraded from version 0.51 to 0.52. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Win32API::File has been upgraded from version 0.1202 to 0.1203. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> XS::Typemap has been upgraded from version 0.13 to 0.14. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> XSLoader has been upgraded from version 0.20 to 0.21. </p>
 </dd></dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlapi</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The process of using undocumented globals has been documented, namely, that one should send email to perl5-porters [at] perl.org &lt;mailto:perl5-porters [at] perl.org&gt; first to get the go-ahead for documenting and using an undocumented function or global variable. </p>
 </dd></dl>
<p> <i>perlcall</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A number of cleanups have been made to perlcall, including: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> use <code>&quot;EXTEND(SP, n)&quot;</code> and <code>&quot;PUSHs()&quot;</code> instead of <code>&quot;XPUSHs()&quot;</code> where applicable and update prose to match </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> add POPu, POPul and POPpbytex to the ``complete list of <font SIZE="-1">POP</font> macros&#8217;&#8216; and clarify the documentation for some of the existing entries, and a note about side-effects </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> add <font SIZE="-1">API</font> documentation for POPu and POPul </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> use <font SIZE="-1">ERRSV</font> more efficiently </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> approaches to thread-safety storage of SVs. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<p> <i>perlfunc</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The documentation of <code>&quot;hex&quot;</code> has been revised to clarify valid inputs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Better explain meaning of negative PIDs in <code>&quot;waitpid&quot;</code>. [perl #127080] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127080">https://rt.perl.org/Ticket/Display.html?id=127080</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> General cleanup: there&#8217;s more consistency now (in <font SIZE="-1">POD</font> usage, grammar, code examples), better practices in code examples (use of <code>&quot;my&quot;</code>, removal of bareword filehandles, dropped usage of <code>&quot;&amp;&quot;</code> when calling subroutines, ...), etc. </p>
 </dd></dl>
<p> <i>perlguts</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A new section has been added, ``Dynamic Scope and the Context Stack&#8217;&#8216; in perlguts, which explains how the perl context stack works. </p>
 </dd></dl>
<p> <i>perllocale</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A stronger caution about using locales in threaded applications is given. Locales are not thread-safe, and you can get wrong results or even segfaults if you use them there. </p>
 </dd></dl>
<p> <i>perlmodlib</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> We now recommend contacting the module-authors list or <font SIZE="-1">PAUSE</font> in seeking guidance on the naming of modules. </p>
 </dd></dl>
<p> <i>perlop</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The documentation of <code>&quot;qx//&quot;</code> now describes how <code>$?</code> is affected. </p>
 </dd></dl>
<p> <i>perlpolicy</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> This note has been added to perlpolicy: </p>
<pre><code> While civility is required, kindness is encouraged; if you have any
 doubt about whether you are being civil, simply ask yourself, &quot;Am I
 being kind?&quot; and aspire to that.
</code></pre>
 </dd></dl>
<p> <i>perlreftut</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Fix some examples to be strict clean. </p>
 </dd></dl>
<p> <i>perlrebackslash</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Clarify that in languages like Japanese and Thai, dictionary lookup is required to determine word boundaries. </p>
 </dd></dl>
<p> <i>perlsub</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Updated to note that anonymous subroutines can have signatures. </p>
 </dd></dl>
<p> <i>perlsyn</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Fixed a broken example where <code>&quot;=&quot;</code> was used instead of <code>&quot;==&quot;</code> in conditional in do/while example. </p>
 </dd></dl>
<p> <i>perltie</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The usage of <code>&quot;FIRSTKEY&quot;</code> and <code>&quot;NEXTKEY&quot;</code> has been clarified. </p>
 </dd></dl>
<p> <i>perlunicode</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Discourage use of &#8216;In&#8217; as a prefix signifying the Unicode Block property. </p>
 </dd></dl>
<p> <i>perlvar</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The documentation of <code>$@</code> was reworded to clarify that it is not just for syntax errors in <code>&quot;eval&quot;</code>. [perl #124034] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124034">https://rt.perl.org/Ticket/Display.html?id=124034</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The specific true value of <code>$!{E...}</code> is now documented, noting that it is subject to change and not guaranteed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of <code>$OLD_PERL_VERSION</code> is now discouraged. </p>
 </dd></dl>
<p> <i>perlxs</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The documentation of <code>&quot;PROTOTYPES&quot;</code> has been corrected; they are <i>disabled</i> by default, not <i>enabled</i>. </p>
 </dd></dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.  </p>
<h3>New Diagnostics</h3>
<p> <i>New Errors</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>%s</code> must not be a named sequence in transliteration operator </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can&#8217;t find Unicode property definition ``%s&#8217;&#8216; in regex; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can&#8217;t redeclare ``%s&#8217;&#8216; in ``%s&#8217;&#8216; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Character following \p must be &#8216;{&#8216; or a single-character Unicode property name in regex; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Empty \%c in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Illegal user-defined property name </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Invalid number &#8216;%s&#8217; for -C option. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Sequence (?... not terminated in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Sequence (?P&lt;... not terminated in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Sequence (?P&gt;... not terminated in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
 </dd></dl>
<p> <i>New Warnings</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Assuming <font SIZE="-1">NOT</font> a <font SIZE="-1">POSIX</font> class since <code>%s</code> in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> %s() is deprecated on :utf8 handles </p>
 </dd></dl>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Accessing the <code>&quot;IO&quot;</code> part of a glob as <code>&quot;FILEHANDLE&quot;</code> instead of <code>&quot;IO&quot;</code> is no longer deprecated. It is discouraged to encourage uniformity (so that, for example, one can grep more easily) but it will not be removed. [perl #127060] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127060">https://rt.perl.org/Ticket/Display.html?id=127060</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The diagnostic <code>&quot;Hexadecimal float: internal error&quot;</code> has been changed to <code>&quot;Hexadecimal float: internal error (%s)&quot;</code> to include more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can&#8217;t modify non-lvalue subroutine call of &amp;%s </p>
<p> This error now reports the name of the non-lvalue subroutine you attempted to use as an lvalue. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When running out of memory during an attempt the increase the stack size, previously, perl would die using the cryptic message <code>&quot;panic: av_extend_guts() negative count (-9223372036854775681)&quot;</code>. This has been fixed to show the prettier message: Out of memory during stack extend </p>
 </dd></dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Configure&quot;</code> now acts as if the <code>&quot;-O&quot;</code> option is always passed, allowing command line options to override saved configuration. This should eliminate confusion when command line options are ignored for no obvious reason. <code>&quot;-O&quot;</code> is now permitted, but ignored. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Bison 3.0 is now supported. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Configure</i> no longer probes for <i>libnm</i> by default. Originally this was the ``New Math&#8217;&#8216; library, but the name has been re-used by the <font SIZE="-1">GNOME</font> NetworkManager. [perl #127131] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127131">https://rt.perl.org/Ticket/Display.html?id=127131</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Added <i>Configure</i> probes for <code>&quot;newlocale&quot;</code>, <code>&quot;freelocale&quot;</code>, and <code>&quot;uselocale&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PPPort.so/PPPort.dll&quot;</code> no longer get installed, as they are not used by <code>&quot;PPPort.pm&quot;</code>, only by its test files. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> It is now possible to specify which compilation date to show on <code>&quot;perl -V&quot;</code> output, by setting the macro <code>&quot;PERL_BUILD_DATE&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using the <code>&quot;NO_HASH_SEED&quot;</code> define in combination with the default hash algorithm <code>&quot;PERL_HASH_FUNC_ONE_AT_A_TIME_HARD&quot;</code> resulted in a fatal error while compiling the interpreter, since Perl 5.17.10. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Configure</i> should handle spaces in paths a little better. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> No longer generate <font SIZE="-1">EBCDIC</font> POSIX-BC tables. We don&#8217;t believe anyone is using Perl and POSIX-BC at this time, and by not generating these tables it saves time during development, and makes the resulting tar ball smaller. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">GNU</font> Make makefile for Win32 now supports parallel builds. [perl #126632] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> You can now build perl with <font SIZE="-1">MSVC++</font> on Win32 using <font SIZE="-1">GNU</font> Make. [perl #126632] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Win32 miniperl now has a real <code>&quot;getcwd&quot;</code> which increases build performance resulting in <code>&quot;getcwd()&quot;</code> being 605x faster in Win32 miniperl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Configure now takes <code>&quot;-Dusequadmath&quot;</code> into account when calculating the <code>&quot;alignbytes&quot;</code> configuration variable. Previously the mis-calculated <code>&quot;alignbytes&quot;</code> could cause alignment errors on debugging builds. [perl #127894] </p>
 </dd></dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> A new test (<i>t/op/aassign.t</i>) has been added to test the list assignment operator <code>&quot;OP_AASSIGN&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Parallel building has been added to the dmake <code>&quot;makefile.mk&quot;</code> makefile. All Win32 compilers are supported. </p>
 </dd></dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>AmigaOS</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> The AmigaOS port has been reintegrated into the main tree, based off of Perl 5.22.1. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>Cygwin</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Tests are more robust against unusual cygdrive prefixes. [perl #126834] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126834">https://rt.perl.org/Ticket/Display.html?id=126834</a>&gt; </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt><font SIZE="-1">EBCDIC</font></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>UTF-EBCDIC extended</dt>
<dd> <p> UTF-EBCDIC is like <font SIZE="-1">UTF-8,</font> but for <font SIZE="-1">EBCDIC</font> platforms. It now has been extended so that it can represent code points up to 2 ** 64 - 1 on platforms with 64-bit words. This brings it into parity with <font SIZE="-1">UTF-8.</font> This enhancement requires an incompatible change to the representation of code points in the range 2 ** 30 to 2 ** 31 -1 (the latter was the previous maximum representable code point). This means that a file that contains one of these code points, written out with previous versions of perl cannot be read in, without conversion, by a perl containing this change. We do not believe any such files are in existence, but if you do have one, submit a ticket at perlbug [at] perl.org &lt;mailto:perlbug [at] perl.org&gt;, and we will write a conversion script for you. </p>
 </dd>
<dt><font SIZE="-1">EBCDIC</font> &quot;cmp()&quot; and &quot;sort()&quot; fixed for UTF-EBCDIC strings</dt>
<dd> <p> Comparing two strings that were both encoded in <font SIZE="-1">UTF-8</font> (or more precisely, UTF-EBCDIC) did not work properly until now. Since <code>&quot;sort()&quot;</code> uses <code>&quot;cmp()&quot;</code>, this fixes that as well. </p>
 </dd>
<dt><font SIZE="-1">EBCDIC</font> &quot;tr///&quot; and &quot;y///&quot; fixed for &quot;\N{}&quot;, and &quot;use utf8&quot; ranges</dt>
<dd> <p> Perl v5.22 introduced the concept of portable ranges to regular expression patterns. A portable range matches the same set of characters no matter what platform is being run on. This concept is now extended to <code>&quot;tr///&quot;</code>. See <code>&quot;tr///&quot;</code>. </p>
<p> There were also some problems with these operations under <code>&quot;use utf8&quot;</code>, which are now fixed </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>FreeBSD</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Use the <code>&quot;fdclose()&quot;</code> function from FreeBSD if it is available. [perl #126847] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126847">https://rt.perl.org/Ticket/Display.html?id=126847</a>&gt; </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt><font SIZE="-1">IRIX</font></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Under some circumstances <font SIZE="-1">IRIX</font> stdio <code>&quot;fgetc()&quot;</code> and <code>&quot;fread()&quot;</code> set the errno to <code>&quot;ENOENT&quot;</code>, which made no sense according to either <font SIZE="-1">IRIX</font> or <font SIZE="-1">POSIX</font> docs. Errno is now cleared in such cases. [perl #123977] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123977">https://rt.perl.org/Ticket/Display.html?id=123977</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Problems when multiplying long doubles by infinity have been fixed. [perl #126396] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126396">https://rt.perl.org/Ticket/Display.html?id=126396</a>&gt; </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>MacOS X</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Until now <font SIZE="-1">OS X</font> builds of perl have specified a link target of 10.3 (Panther, 2003) but have not specified a compiler target. From now on, builds of perl on <font SIZE="-1">OS X 10.6</font> or later (Snow Leopard, 2008) by default capture the current <font SIZE="-1">OS X</font> version and specify that as the explicit build target in both compiler and linker flags, thus preserving binary compatibility for extensions built later regardless of changes in <font SIZE="-1">OS X, SDK,</font> or compiler and linker versions. To override the default value used in the build and preserved in the flags, specify <code>&quot;export MACOSX_DEPLOYMENT_TARGET=10.N&quot;</code> before configuring and building perl, where 10.N is the version of <font SIZE="-1">OS X</font> you wish to target. In <font SIZE="-1">OS X 10.5</font> or earlier there is no change to the behavior present when those systems were current; the link target is still <font SIZE="-1">OS X 10.3</font> and there is no explicit compiler target. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Builds with both -DDEBUGGING and threading enabled would fail with a ``panic: free from wrong pool&#8217;&#8216; error when built or tested from Terminal on <font SIZE="-1">OS X.</font> This was caused by perl&#8217;s internal management of the environment conflicting with an atfork handler using the libc <code>&quot;setenv()&quot;</code> function to update the environment. </p>
<p> Perl now uses <code>&quot;setenv()&quot;</code>/<code>&quot;unsetenv()&quot;</code> to update the environment on <font SIZE="-1">OS X.</font> [perl #126240] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126240">https://rt.perl.org/Ticket/Display.html?id=126240</a>&gt; </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>Solaris</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> All Solaris variants now build a shared libperl </p>
<p> Solaris and variants like OpenIndiana now always build with the shared Perl library (Configure -Duseshrplib). This was required for the OpenIndiana builds, but this has also been the setting for Oracle/Sun Perl builds for several years. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>Tru64</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Workaround where Tru64 balks when prototypes are listed as <code>&quot;PERL_STATIC_INLINE&quot;</code>, but where the test is build with <code>&quot;-DPERL_NO_INLINE_FUNCTIONS&quot;</code>. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt><font SIZE="-1">VMS</font></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> On <font SIZE="-1">VMS,</font> the math function prototypes in <code>&quot;math.h&quot;</code> are now visible under C<font SIZE="-2">++</font>. Now building the <font SIZE="-1">POSIX</font> extension with C<font SIZE="-2">++</font> will no longer crash. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">VMS</font> has had <code>&quot;setenv&quot;</code>/<code>&quot;unsetenv&quot;</code> since v7.0 (released in 1996), <code>&quot;Perl_vmssetenv&quot;</code> now always uses <code>&quot;setenv&quot;</code>/<code>&quot;unsetenv&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now implements its own <code>&quot;killpg&quot;</code> by scanning for processes in the specified process group, which may not mean exactly the same thing as a Unix process group, but allows us to send a signal to a parent (or master) process and all of its sub-processes. At the perl level, this means we can now send a negative pid like so: </p>
<pre><code>    kill SIGKILL, -$pid;
</code></pre>
<p> to signal all processes in the same group as <code>$pid</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> For those <code>%ENV</code> elements based on the <font SIZE="-1">CRTL</font> environ array, we&#8217;ve always preserved case when setting them but did look-ups only after upcasing the key first, which made lower- or mixed-case entries go missing. This problem has been corrected by making <code>%ENV</code> elements derived from the environ array case-sensitive on look-up as well as case-preserving on store. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Environment look-ups for <code>&quot;PERL5LIB&quot;</code> and <code>&quot;PERLLIB&quot;</code> previously only considered logical names, but now consider all sources of <code>%ENV</code> as determined by <code>&quot;PERL_ENV_TABLES&quot;</code> and as documented in ``%ENV&#8217;&#8216; in perlvms. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The minimum supported version of <font SIZE="-1">VMS</font> is now v7.3-2, released in 2003. As a side effect of this change, <font SIZE="-1">VAX</font> is no longer supported as the terminal release of OpenVMS <font SIZE="-1">VAX</font> was v7.3 in 2001. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>Win32</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> A new build option <code>&quot;USE_NO_REGISTRY&quot;</code> has been added to the makefiles. This option is off by default, meaning the default is to do Windows registry lookups. This option stops Perl from looking inside the registry for anything. For what values are looked up in the registry see perlwin32. Internally, in C, the name of this option is <code>&quot;WIN32_NO_REGISTRY&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The behavior of Perl using <code>&quot;HKEY_CURRENT_USER\Software\Perl&quot;</code> and <code>&quot;HKEY_LOCAL_MACHINE\Software\Perl&quot;</code> to lookup certain values, including <code>%ENV</code> vars starting with <code>&quot;PERL&quot;</code> has changed. Previously, the 2 keys were checked for entries at all times through the perl process&#8217;s life time even if they did not exist. For performance reasons, now, if the root key (i.e. <code>&quot;HKEY_CURRENT_USER\Software\Perl&quot;</code> or <code>&quot;HKEY_LOCAL_MACHINE\Software\Perl&quot;</code>) does not exist at process start time, it will not be checked again for <code>%ENV</code> override entries for the remainder of the perl process&#8217;s life. This more closely matches Unix behavior in that the environment is copied or inherited on startup and changing the variable in the parent process or another process or editing <i>.bashrc</i> will not change the environmental variable in other existing, running, processes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> One glob fetch was removed for each <code>&quot;-X&quot;</code> or <code>&quot;stat&quot;</code> call whether done from Perl code or internally from Perl&#8217;s C code. The glob being looked up was <code>&quot;${^WIN32_SLOPPY_STAT}&quot;</code> which is a special variable. This makes <code>&quot;-X&quot;</code> and <code>&quot;stat&quot;</code> slightly faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> During miniperl&#8217;s process startup, during the build process, 4 to 8 <font SIZE="-1">IO</font> calls related to the process starting <i>.pl</i> and the <i>buildcustomize.pl</i> file were removed from the code opening and executing the first 1 or 2 <i>.pl</i> files. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Builds using Microsoft Visual C<font SIZE="-2">++</font> 2003 and earlier no longer produce an ``<font SIZE="-1">INTERNAL COMPILER ERROR&#8217;&#8216;</font> message. [perl #126045] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Visual C<font SIZE="-2">++</font> 2013 builds will now execute on <font SIZE="-1">XP</font> and higher. Previously they would only execute on Vista and higher. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> You can now build perl with <font SIZE="-1">GNU</font> Make and <font SIZE="-1">GCC.</font> [perl #123440] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;truncate($filename, $size)&quot;</code> now works for files over 4GB in size. [perl #125347] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Parallel building has been added to the dmake <code>&quot;makefile.mk&quot;</code> makefile. All Win32 compilers are supported. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Building a 64-bit perl with a 64-bit <font SIZE="-1">GCC</font> but a 32-bit gmake would result in an invalid <code>$Config{archname}</code> for the resulting perl. [perl #127584] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Errors set by Winsock functions are now put directly into <code>$^E</code>, and the relevant <code>&quot;WSAE*&quot;</code> error codes are now exported from the Errno and <font SIZE="-1">POSIX</font> modules for testing this against. </p>
<p> The previous behavior of putting the errors (converted to POSIX-style <code>&quot;E*&quot;</code> error codes since Perl 5.20.0) into <code>$!</code> was buggy due to the non-equivalence of like-named Winsock and <font SIZE="-1">POSIX</font> error constants, a relationship between which has unfortunately been established in one way or another since Perl 5.8.0. </p>
<p> The new behavior provides a much more robust solution for checking Winsock errors in portable software without accidentally matching <font SIZE="-1">POSIX</font> tests that were intended for other OSes and may have different meanings for Winsock. </p>
<p> The old behavior is currently retained, warts and all, for backwards compatibility, but users are encouraged to change any code that tests <code>$!</code> against <code>&quot;E*&quot;</code> constants for Winsock errors to instead test <code>$^E</code> against <code>&quot;WSAE*&quot;</code> constants. After a suitable deprecation period, the old behavior may be removed, leaving <code>$!</code> unchanged after Winsock function calls, to avoid any possible confusion over which error variable to check. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>ppc64el</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>floating point</dt>
<dd> <p> The floating point format of ppc64el (Debian naming for little-endian PowerPC) is now detected correctly. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The implementation of perl&#8217;s context stack system, and its internal <font SIZE="-1">API,</font> have been heavily reworked. Note that no significant changes have been made to any external APIs, but <font SIZE="-1">XS</font> code which relies on such internal details may need to be fixed. The main changes are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;PUSHBLOCK()&quot;</code>, <code>&quot;POPSUB()&quot;</code> etc. macros have been replaced with static inline functions such as <code>&quot;cx_pushblock()&quot;</code>, <code>&quot;cx_popsub()&quot;</code> etc. These use function args rather than implicitly relying on local vars such as <code>&quot;gimme&quot;</code> and <code>&quot;newsp&quot;</code> being available. Also their functionality has changed: in particular, <code>&quot;cx_popblock()&quot;</code> no longer decrements <code>&quot;cxstack_ix&quot;</code>. The ordering of the steps in the <code>&quot;pp_leave*&quot;</code> functions involving <code>&quot;cx_popblock()&quot;</code>, <code>&quot;cx_popsub()&quot;</code> etc. has changed. See the new documentation, ``Dynamic Scope and the Context Stack&#8217;&#8216; in perlguts, for details on how to use them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various macros, which now consistently have a <font SIZE="-1">CX_</font> prefix, have been added: </p>
<pre><code>  CX_CUR(), CX_LEAVE_SCOPE(), CX_POP()
</code></pre>
<p> or renamed: </p>
<pre><code>  CX_POP_SAVEARRAY(), CX_DEBUG(), CX_PUSHSUBST(), CX_POPSUBST()
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;cx_pushblock()&quot;</code> now saves <code>&quot;PL_savestack_ix&quot;</code> and <code>&quot;PL_tmps_floor&quot;</code>, so <code>&quot;pp_enter*&quot;</code> and <code>&quot;pp_leave*&quot;</code> no longer do </p>
<pre><code>  ENTER; SAVETMPS; ....; LEAVE
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;cx_popblock()&quot;</code> now also restores <code>&quot;PL_curpm&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In <code>&quot;dounwind()&quot;</code> for every context type, the current savestack frame is now processed before each context is popped; formerly this was only done for sub-like context frames. This action has been removed from <code>&quot;cx_popsub()&quot;</code> and placed into its own macro, <code>&quot;CX_LEAVE_SCOPE(cx)&quot;</code>, which must be called before <code>&quot;cx_popsub()&quot;</code> etc. </p>
<p> <code>&quot;dounwind()&quot;</code> now also does a <code>&quot;cx_popblock()&quot;</code> on the last popped frame (formerly it only did the <code>&quot;cx_popsub()&quot;</code> etc. actions on each frame). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The temps stack is now freed on scope exit; previously, temps created during the last statement of a block wouldn&#8217;t be freed until the next <code>&quot;nextstate&quot;</code> following the block (apart from an existing hack that did this for recursive subs in scalar context); and in something like <code>&quot;f(g())&quot;</code>, the temps created by the last statement in <code>&quot;g()&quot;</code> would formerly not be freed until the statement following the return from <code>&quot;f()&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Most values that were saved on the savestack on scope entry are now saved in suitable new fields in the context struct, and saved and restored directly by <code>&quot;cx_pushfoo()&quot;</code> and <code>&quot;cx_popfoo()&quot;</code>, which is much faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various context struct fields have been added, removed or modified. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The handling of <code>@_</code> in <code>&quot;cx_pushsub()&quot;</code> and <code>&quot;cx_popsub()&quot;</code> has been considerably tidied up, including removing the <code>&quot;argarray&quot;</code> field from the context struct, and extracting out some common (but rarely used) code into a separate function, <code>&quot;clear_defarray()&quot;</code>. Also, useful subsets of <code>&quot;cx_popsub()&quot;</code> which had been unrolled in places like <code>&quot;pp_goto&quot;</code> have been gathered into the new functions <code>&quot;cx_popsub_args()&quot;</code> and <code>&quot;cx_popsub_common()&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pp_leavesub&quot;</code> and <code>&quot;pp_leavesublv&quot;</code> now use the same function as the rest of the <code>&quot;pp_leave*&quot;</code>&#8216;s to process return args. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;CXp_FOR_PAD&quot;</code> and <code>&quot;CXp_FOR_GV&quot;</code> flags have been added, and <code>&quot;CXt_LOOP_FOR&quot;</code> has been split into <code>&quot;CXt_LOOP_LIST&quot;</code>, <code>&quot;CXt_LOOP_ARY&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some variables formerly declared by <code>&quot;dMULTICALL&quot;</code> (but not documented) have been removed. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> The obscure <code>&quot;PL_timesbuf&quot;</code> variable, effectively a vestige of Perl 1, has been removed. It was documented as deprecated in Perl 5.20, with a statement that it would be removed early in the 5.21.x series; that has now finally happened. [perl #121351] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121351">https://rt.perl.org/Ticket/Display.html?id=121351</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An unwarranted assertion in <code>&quot;Perl_newATTRSUB_x()&quot;</code> has been removed. If a stub subroutine definition with a prototype has been seen, then any subsequent stub (or definition) of the same subroutine with an attribute was causing an assertion failure because of a null pointer. [perl #126845] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126845">https://rt.perl.org/Ticket/Display.html?id=126845</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;::&quot;</code> has been replaced by <code>&quot;__&quot;</code> in <code>&quot;ExtUtils::ParseXS&quot;</code>, like it&#8217;s done for parameters/return values. This is more consistent, and simplifies writing <font SIZE="-1">XS</font> code wrapping C<font SIZE="-2">++</font> classes into a nested Perl namespace (it requires only a typedef for <code>&quot;Foo__Bar&quot;</code> rather than two, one for <code>&quot;Foo_Bar&quot;</code> and the other for <code>&quot;Foo::Bar&quot;</code>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;to_utf8_case()&quot;</code> function is now deprecated. Instead use <code>&quot;toUPPER_utf8&quot;</code>, <code>&quot;toTITLE_utf8&quot;</code>, <code>&quot;toLOWER_utf8&quot;</code>, and <code>&quot;toFOLD_utf8&quot;</code>. (See &lt;<a rel="nofollow" href="http://nntp.perl.org/group/perl.perl5.porters/233287">http://nntp.perl.org/group/perl.perl5.porters/233287</a>&gt;.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl core code and the threads extension have been annotated so that, if Perl is configured to use threads, then during compile-time clang (3.6 or later) will warn about suspicious uses of mutexes. See &lt;<a rel="nofollow" href="http://clang.llvm.org/docs/ThreadSafetyAnalysis.html">http://clang.llvm.org/docs/ThreadSafetyAnalysis.html</a>&gt; for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;signbit()&quot;</code> emulation has been enhanced. This will help older and/or more exotic platforms or configurations. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Most EBCDIC-specific code in the core has been unified with non-EBCDIC code, to avoid repetition and make maintenance easier. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> MSWin32 code for <code>$^X</code> has been moved out of the <i>win32</i> directory to <i>caretx.c</i>, where other operating systems set that variable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sv_ref()&quot;</code> is now part of the <font SIZE="-1">API.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ``sv_backoff&#8217;&#8216; in perlapi had its return type changed from <code>&quot;int&quot;</code> to <code>&quot;void&quot;</code>. It previously has always returned <code>0</code> since Perl 5.000 stable but that was undocumented. Although <code>&quot;sv_backoff&quot;</code> is marked as public <font SIZE="-1">API, XS</font> code is not expected to be impacted since the proper <font SIZE="-1">API</font> call would be through public <font SIZE="-1">API</font> <code>&quot;sv_setsv(sv, &amp;PL_sv_undef)&quot;</code>, or quasi-public <code>&quot;SvOOK_off&quot;</code>, or non-public <code>&quot;SvOK_off&quot;</code> calls, and the return value of <code>&quot;sv_backoff&quot;</code> was previously a meaningless constant that can be rewritten as <code>&quot;(sv_backoff(sv),0)&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;EXTEND&quot;</code> and <code>&quot;MEXTEND&quot;</code> macros have been improved to avoid various issues with integer truncation and wrapping. In particular, some casts formerly used within the macros have been removed. This means for example that passing an unsigned <code>&quot;nitems&quot;</code> argument is likely to raise a compiler warning now (it&#8217;s always been documented to require a signed value; formerly int, lately SSize_t). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PL_sawalias&quot;</code> and <code>&quot;GPf_ALIASED_SV&quot;</code> have been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;GvASSIGN_GENERATION&quot;</code> and <code>&quot;GvASSIGN_GENERATION_set&quot;</code> have been removed. </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> It now works properly to specify a user-defined property, such as </p>
<pre><code> qr/\p{mypkg1::IsMyProperty}/i
</code></pre>
<p> with <code>&quot;/i&quot;</code> caseless matching, an explicit package name, and <i>IsMyProperty</i> not defined at the time of the pattern compilation. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl&#8217;s <code>&quot;memcpy()&quot;</code>, <code>&quot;memmove()&quot;</code>, <code>&quot;memset()&quot;</code> and <code>&quot;memcmp()&quot;</code> fallbacks are now more compatible with the originals. [perl #127619] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed the issue where a <code>&quot;s///r&quot;</code>) with <code>-DPERL_NO_COW</code> attempts to modify the source <font SIZE="-1">SV,</font> resulting in the program dying. [perl #127635] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed an EBCDIC-platform-only case where a pattern could fail to match. This occurred when matching characters from the set of C1 controls when the target matched string was in <font SIZE="-1">UTF-8.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Narrow the filename check in <i>strict.pm</i> and <i>warnings.pm</i>. Previously, it assumed that if the filename (without the <i>.pmc?</i> extension) differed from the package name, if was a misspelled use statement (i.e. <code>&quot;use Strict&quot;</code> instead of <code>&quot;use strict&quot;</code>). We now check whether there&#8217;s really a miscapitalization happening, and not some other issue. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Turn an assertion into a more user friendly failure when parsing regexes. [perl #127599] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Correctly raise an error when trying to compile patterns with unterminated character classes while there are trailing backslashes. [perl #126141]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Line numbers larger than 2**31-1 but less than 2**32 are no longer returned by <code>&quot;caller()&quot;</code> as negative numbers. [perl #126991] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;unless ( </code>assignment <code> )&quot;</code> now properly warns when syntax warnings are enabled. [perl #127122] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Setting an <code>&quot;ISA&quot;</code> glob to an array reference now properly adds <code>&quot;isaelem&quot;</code> magic to any existing elements. Previously modifying such an element would not update the <font SIZE="-1">ISA</font> cache, so method calls would call the wrong function. Perl would also crash if the <code>&quot;ISA&quot;</code> glob was destroyed, since new code added in 5.23.7 would try to release the <code>&quot;isaelem&quot;</code> magic from the elements. [perl #127351] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If a here-doc was found while parsing another operator, the parser had already read end of file, and the here-doc was not terminated, perl could produce an assertion or a segmentation fault. This now reliably complains about the unterminated here-doc. [perl #125540] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;untie()&quot;</code> would sometimes return the last value returned by the <code>&quot;UNTIE()&quot;</code> handler as well as it&#8217;s normal value, messing up the stack. [perl #126621] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed an operator precedence problem when <code>&quot; castflags &amp; 2&quot;</code> is true. [perl #127474] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Caching of <font SIZE="-1">DESTROY</font> methods could result in a non-pointer or a non-STASH stored in the <code>&quot;SvSTASH()&quot;</code> slot of a stash, breaking the B <code>&quot;STASH()&quot;</code> method. The <font SIZE="-1">DESTROY</font> method is now cached in the <font SIZE="-1">MRO</font> metadata for the stash. [perl #126410] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">AUTOLOAD</font> method is now called when searching for a <font SIZE="-1">DESTROY</font> method, and correctly sets <code>$AUTOLOAD</code> too. [perl #124387] [perl #127494] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Avoid parsing beyond the end of the buffer when processing a <code>&quot;#line&quot;</code> directive with no filename. [perl #127334] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now raises a warning when a regular expression pattern looks like it was supposed to contain a <font SIZE="-1">POSIX</font> class, like <code>&quot;qr/[[:alpha:]]/&quot;</code>, but there was some slight defect in its specification which causes it to instead be treated as a regular bracketed character class. An example would be missing the second colon in the above like this: <code>&quot;qr/[[:alpha]]/&quot;</code>. This compiles to match a sequence of two characters. The second is <code>&quot;]&quot;</code>, and the first is any of: <code>&quot;[&quot;</code>, <code>&quot;:&quot;</code>, <code>&quot;a&quot;</code>, <code>&quot;h&quot;</code>, <code>&quot;l&quot;</code>, or <code>&quot;p&quot;</code>. This is unlikely to be the intended meaning, and now a warning is raised. No warning is raised unless the specification is very close to one of the 14 legal <font SIZE="-1">POSIX</font> classes. (See ``<font SIZE="-1">POSIX</font> Character Classes&#8217;&#8216; in perlrecharclass.) [perl #8904] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Certain regex patterns involving a complemented <font SIZE="-1">POSIX</font> class in an inverted bracketed character class, and matching something else optionally would improperly fail to match. An example of one that could fail is <code>&quot;qr/_?[^\Wbar]\x{100}/&quot;</code>. This has been fixed. [perl #127537] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl 5.22 added support to the C99 hexadecimal floating point notation, but sometimes misparses hex floats. This has been fixed. [perl #127183] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A regression that allowed undeclared barewords in hash keys to work despite strictures has been fixed. [perl #126981] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126981">https://rt.perl.org/Ticket/Display.html?id=126981</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calls to the placeholder <code>&amp;PL_sv_yes</code> used internally when an <code>&quot;import()&quot;</code> or <code>&quot;unimport()&quot;</code> method isn&#8217;t found now correctly handle scalar context. [perl #126042] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126042">https://rt.perl.org/Ticket/Display.html?id=126042</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Report more context when we see an array where we expect to see an operator and avoid an assertion failure. [perl #123737] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123737">https://rt.perl.org/Ticket/Display.html?id=123737</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Modifying an array that was previously a package <code>@ISA</code> no longer causes assertion failures or crashes. [perl #123788] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123788">https://rt.perl.org/Ticket/Display.html?id=123788</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Retain binary compatibility across plain and <font SIZE="-1">DEBUGGING</font> perl builds. [perl #127212] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127212">https://rt.perl.org/Ticket/Display.html?id=127212</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Avoid leaking memory when setting <code>$ENV{foo}</code> on darwin. [perl #126240] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126240">https://rt.perl.org/Ticket/Display.html?id=126240</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;/...\G/&quot;</code> no longer crashes on utf8 strings. When <code>&quot;\G&quot;</code> is a fixed number of characters from the start of the regex, perl needs to count back that many characters from the current <code>&quot;pos()&quot;</code> position and start matching from there. However, it was counting back bytes rather than characters, which could lead to panics on utf8 strings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In some cases operators that return integers would return negative integers as large positive integers. [perl #126635] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126635">https://rt.perl.org/Ticket/Display.html?id=126635</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;pipe()&quot;</code> operator would assert for <font SIZE="-1">DEBUGGING</font> builds instead of producing the correct error message. The condition asserted on is detected and reported on correctly without the assertions, so the assertions were removed. [perl #126480] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126480">https://rt.perl.org/Ticket/Display.html?id=126480</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In some cases, failing to parse a here-doc would attempt to use freed memory. This was caused by a pointer not being restored correctly. [perl #126443] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126443">https://rt.perl.org/Ticket/Display.html?id=126443</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;@x = sort { *a = 0; $a &lt;=&gt; $b } 0 .. 1&quot;</code> no longer frees the <font SIZE="-1">GP</font> for *a before restoring its <font SIZE="-1">SV</font> slot. [perl #124097] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124097">https://rt.perl.org/Ticket/Display.html?id=124097</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Multiple problems with the new hexadecimal floating point printf format <code>%a</code> were fixed: [perl #126582] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126582">https://rt.perl.org/Ticket/Display.html?id=126582</a>&gt;, [perl #126586] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126586">https://rt.perl.org/Ticket/Display.html?id=126586</a>&gt;, [perl #126822] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126822">https://rt.perl.org/Ticket/Display.html?id=126822</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calling <code>&quot;mg_set()&quot;</code> in <code>&quot;leave_scope()&quot;</code> no longer leaks. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A regression from Perl v5.20 was fixed in which debugging output of regular expression compilation was wrong. (The pattern was correctly compiled, but what got displayed for it was wrong.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;\b{sb}&quot;</code> works much better. In Perl v5.22.0, this new construct didn&#8217;t seem to give the expected results, yet passed all the tests in the extensive suite furnished by Unicode. It turns out that it was because these were short input strings, and the failures had to do with longer inputs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Certain syntax errors in ``Extended Bracketed Character Classes&#8217;&#8216; in perlrecharclass caused panics instead of the proper error message. This has now been fixed. [perl #126481] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl 5.20 added a message when a quantifier in a regular expression was useless, but then caused the parser to skip it; this caused the surplus quantifier to be silently ignored, instead of throwing an error. This is now fixed. [perl #126253] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The switch to building non-XS modules last in win32/makefile.mk (introduced by design as part of the changes to enable parallel building) caused the build of <font SIZE="-1">POSIX</font> to break due to problems with the version module. This is now fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Improved parsing of hex float constants. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed an issue with <code>&quot;pack&quot;</code> where <code>&quot;pack &quot;H&quot;&quot;</code> (and <code>&quot;pack &quot;h&quot;&quot;</code>) could read past the source when given a non-utf8 source, and a utf8 target. [perl #126325] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed several cases where perl would abort due to a segmentation fault, or a C-level assert. [perl #126615], [perl #126602], [perl #126193]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> There were places in regular expression patterns where comments (<code>&quot;(?#...)&quot;</code>) weren&#8217;t allowed, but should have been. This is now fixed. [perl #116639] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=116639">https://rt.perl.org/Ticket/Display.html?id=116639</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some regressions from Perl 5.20 have been fixed, in which some syntax errors in <code>&quot;(?[...])&quot;</code> constructs within regular expression patterns could cause a segfault instead of a proper error message. [perl #126180] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126180">https://rt.perl.org/Ticket/Display.html?id=126180</a>&gt; [perl #126404] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126404">https://rt.perl.org/Ticket/Display.html?id=126404</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Another problem with <code>&quot;(?[...])&quot;</code> constructs has been fixed wherein things like <code>&quot;\c]&quot;</code> could cause panics. [perl #126181] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126181">https://rt.perl.org/Ticket/Display.html?id=126181</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some problems with attempting to extend the perl stack to around 2G or 4G entries have been fixed. This was particularly an issue on 32-bit perls built to use 64-bit integers, and was easily noticeable with the list repetition operator, e.g. </p>
<pre><code>    @a = (1) x $big_number
</code></pre>
<p> Formerly perl may have crashed, depending on the exact value of <code>$big_number</code>; now it will typically raise an exception. [perl #125937] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125937">https://rt.perl.org/Ticket/Display.html?id=125937</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In a regex conditional expression <code>&quot;(?(condition)yes-pattern|no-pattern)&quot;</code>, if the condition is <code>&quot;(?!)&quot;</code> then perl failed the match outright instead of matching the no-pattern. This has been fixed. [perl #126222] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126222">https://rt.perl.org/Ticket/Display.html?id=126222</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The special backtracking control verbs <code>&quot;(*VERB:ARG)&quot;</code> now all allow an optional argument and set <code>&quot;REGERROR&quot;</code>/<code>&quot;REGMARK&quot;</code> appropriately as well. [perl #126186] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126186">https://rt.perl.org/Ticket/Display.html?id=126186</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several bugs, including a segmentation fault, have been fixed with the boundary checking constructs (introduced in Perl 5.22) <code>&quot;\b{gcb}&quot;</code>, <code>&quot;\b{sb}&quot;</code>, <code>&quot;\b{wb}&quot;</code>, <code>&quot;\B{gcb}&quot;</code>, <code>&quot;\B{sb}&quot;</code>, and <code>&quot;\B{wb}&quot;</code>. All the <code>&quot;\B{}&quot;</code> ones now match an empty string; none of the <code>&quot;\b{}&quot;</code> ones do. [perl #126319] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126319">https://rt.perl.org/Ticket/Display.html?id=126319</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Duplicating a closed file handle for write no longer creates a filename of the form <i></i><font SIZE="-1"><i>GLOB</i></font><i>(0xXXXXXXXX)</i>. [perl #125115] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Warning fatality is now ignored when rewinding the stack. This prevents infinite recursion when the now fatal error also causes rewinding of the stack. [perl #123398] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In perl v5.22.0, the logic changed when parsing a numeric parameter to the -C option, such that the successfully parsed number was not saved as the option value if it parsed to the end of the argument. [perl #125381] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The PadlistNAMES macro is an lvalue again. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Zero -DPERL_TRACE_OPS memory for sub-threads. </p>
<p> <code>&quot;perl_clone_using()&quot;</code> was missing Zero init of PL_op_exec_cnt[]. This caused sub-threads in threaded -DPERL_TRACE_OPS builds to spew exceedingly large op-counts at destruct. These counts would print <code>%x</code> as ``<font SIZE="-1">ABABABAB&#8217;&#8216;,</font> clearly a mem-poison value. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A leak in the <font SIZE="-1">XS</font> typemap caused one scalar to be leaked each time a <code>&quot;FILE *&quot;</code> or a <code>&quot;PerlIO *&quot;</code> was <code>&quot;OUTPUT:&quot;</code>ed or imported to Perl, since perl 5.000. These particular typemap entries are thought to be extremely rarely used by <font SIZE="-1">XS</font> modules. [perl #124181] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;alarm()&quot;</code> and <code>&quot;sleep()&quot;</code> will now warn if the argument is a negative number and return undef. Previously they would pass the negative value to the underlying C function which may have set up a timer with a surprising value. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl can again be compiled with any Unicode version. This used to (mostly) work, but was lost in v5.18 through v5.20. The property <code>&quot;Name_Alias&quot;</code> did not exist prior to Unicode 5.0. Unicode::UCD incorrectly said it did. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Very large code-points (beyond Unicode) in regular expressions no longer cause a buffer overflow in some cases when converted to <font SIZE="-1">UTF-8.</font> [perl #125826] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125826">https://rt.perl.org/Ticket/Display.html?id=125826</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The integer overflow check for the range operator (...) in list context now correctly handles the case where the size of the range is larger than the address space. This could happen on 32-bits with -Duse64bitint. [perl #125781] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125781">https://rt.perl.org/Ticket/Display.html?id=125781</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A crash with <code>&quot;%::=(); J-&gt;${\&quot;::&quot;}&quot;</code> has been fixed. [perl #125541] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125541">https://rt.perl.org/Ticket/Display.html?id=125541</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;qr/(?[ () ])/&quot;</code> no longer segfaults, giving a syntax error message instead. [perl #125805] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regular expression possessive quantifier v5.20 regression now fixed. <code>&quot;qr/&quot;</code><i></i><font SIZE="-1"><i>PAT</i></font><i></i><code>&quot;{&quot;</code><i>min</i>,<i>max</i><code>&quot;}+&quot;</code><code>&quot;/&quot;</code> is supposed to behave identically to <code>&quot;qr/(?&gt;&quot;</code><i></i><font SIZE="-1"><i>PAT</i></font><i></i><code>&quot;{&quot;</code><i>min</i>,<i>max</i><code>&quot;})/&quot;</code>. Since v5.20, this didn&#8217;t work if <i>min</i> and <i>max</i> were equal. [perl #125825] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;BEGIN &lt;&gt;&quot;</code> no longer segfaults and properly produces an error message. [perl #125341] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In <code>&quot;tr///&quot;</code> an illegal backwards range like <code>&quot;tr/\x{101}-\x{100}//&quot;</code> was not always detected, giving incorrect results. This is now fixed. </p>
 </dd></dl>
<h2>Acknowledgements</h2>
<p> Perl 5.24.0 represents approximately 11 months of development since Perl 5.24.0 and contains approximately 360,000 lines of changes across 1,800 files from 75 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 250,000 lines of changes to 1,200 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.24.0: </p>
<p> Aaron Crane, Aaron Priven, Abigail, Achim Gratz, Alexander D&#8217;Archangel, Alex Vandiver, Andreas König, Andy Broad, Andy Dougherty, Aristotle Pagaltzis, Chase Whitener, Chas. Owens, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, Dagfinn Ilmari Mannsåker, Dan Collins, Daniel Dragan, David Golden, David Mitchell, Doug Bell, Dr.Ruud, Ed Avis, Ed J, Father Chrysostomos, Herbert Breunung, H.Merijn Brand, Hugo van der Sanden, Ivan Pozdeev, James E Keenan, Jan Dubois, Jarkko Hietaniemi, Jerry D. Hedden, Jim Cromie, John Peacock, John <font SIZE="-1">SJ</font> Anderson, Karen Etheridge, Karl Williamson, kmx, Leon Timmermans, Ludovic E. R. Tolhurst-Cleaver, Lukas Mai, Martijn Lievaart, Matthew Horsfall, Mattia Barbon, Max Maischein, Mohammed El-Afifi, Nicholas Clark, Nicolas R., Niko Tyni, Peter John Acklam, Peter Martini, Peter Rabbitson, Pip Cet, Rafael Garcia-Suarez, Reini Urban, Ricardo Signes, Sawyer X, Shlomi Fish, Sisyphus, Stanislaw Pusep, Steffen Müller, Stevan Little, Steve Hay, Sullivan Beck, Thomas Sibley, Todd Rinaldo, Tom Hukins, Tony Cook, Unicode Consortium, Victor Adam, Vincent Pit, Vladimir Timofeev, Yves Orton, Zachary Storer, Zefram. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="https://rt.perl.org/">https://rt.perl.org/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications which make it inappropriate to send to a publicly archived mailing list, then see ``<font SIZE="-1">SECURITY VULNERABILITY CONTACT INFORMATION&#8217;&#8216;</font> in perlsec for details of how to report the issue.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
