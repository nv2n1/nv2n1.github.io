---

title: "perl5300delta(1)"
name: "perl5300delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5300delta/"
description: "perldelta – what is new for perl v5.30.0"
---

<p> perldelta &#8211; what is new for perl v5.30.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.28.0 release and the 5.30.0 release. </p>
<p> If you are upgrading from an earlier release such as 5.26.0, first read perl5280delta, which describes differences between 5.26.0 and 5.28.0.</p>
<h2>Notice</h2>
<p> sv_utf8_(downgrade|decode) are no longer marked as experimental. [perl #133788] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133788">https://rt.perl.org/Ticket/Display.html?id=133788</a>&gt;.</p>
<h2>Core Enhancements</h2>
<h3>Limited variable length lookbehind in regular expression pattern matching is now experimentally supported</h3>
<p> Using a lookbehind assertion (like <tt>&quot;(?&lt;=foo?)&quot;</tt> or <tt>&quot;(?&lt;!ba{1,9}r)&quot;</tt> previously would generate an error and refuse to compile. Now it compiles (if the maximum lookbehind is at most 255 characters), but raises a warning in the new <tt>&quot;experimental::vlb&quot;</tt> warnings category. This is to caution you that the precise behavior is subject to change based on feedback from use in the field. </p>
<p> See &#8220;(?&lt;=pattern)&#8221; in perlre and &#8220;(?&lt;!pattern)&#8221; in perlre.</p>
<h3>The upper limit n specifiable in a regular expression quantifier of the form {m,n} has been doubled to 65534</h3>
<p> The meaning of an unbounded upper quantifier <tt>&quot;{m,}&quot;</tt> remains unchanged. It matches 2**31 &#8211; 1 times on most platforms, and more on ones where a C language short variable is more than 4 bytes long.</p>
<h3>Unicode 12.1 is supported</h3>
<p> Because of a change in Unicode release cycles, Perl jumps from Unicode 10.0 in Perl 5.28 to Unicode 12.1 in Perl 5.30. </p>
<p> For details on the Unicode changes, see &lt;<a rel="nofollow" href="https://www.unicode.org/versions/Unicode11.0.0/">https://www.unicode.org/versions/Unicode11.0.0/</a>&gt; for 11.0; &lt;<a rel="nofollow" href="https://www.unicode.org/versions/Unicode12.0.0/">https://www.unicode.org/versions/Unicode12.0.0/</a>&gt; for 12.0; and &lt;<a rel="nofollow" href="https://www.unicode.org/versions/Unicode12.1.0/">https://www.unicode.org/versions/Unicode12.1.0/</a>&gt; for 12.1. (Unicode 12.1 differs from 12.0 only in the addition of a single character, that for the new Japanese era name.) </p>
<p> The Word_Break property, as in past Perl releases, remains tailored to behave more in line with expectations of Perl users. This means that sequential runs of horizontal white space characters are not broken apart, but kept as a single run. Unicode 11 changed from past versions to be more in line with Perl, but it left several white space characters as causing breaks: TAB, NO BREAK SPACE, and FIGURE SPACE (U+2007). We have decided to continue to use the previous Perl tailoring with regards to these.</p>
<h3>Wildcards in Unicode property value specifications are now partially supported</h3>
<p> You can now do something like this in a regular expression pattern </p>
<pre><code>
qr ! \p
{nv= /(?x) \A [0-5] \z /
}
!
</code></pre>
<p> which matches all Unicode code points whose numeric value is between 0 and 5 inclusive. So, it could match the Thai or Bengali digits whose numeric values are 0, 1, 2, 3, 4, or 5. </p>
<p> This marks another step in implementing the regular expression features the Unicode Consortium suggests. </p>
<p> Most properties are supported, with the remainder planned for 5.32. Details are in &#8220;Wildcards in Property Values&#8221; in perlunicode.</p>
<h3>qr&#8217;\N{name}&#8217; is now supported</h3>
<p> Previously it was an error to evaluate a named character <tt>&quot;\N{...}&quot;</tt> within a single quoted regular expression pattern (whose evaluation is deferred from the normal place). This restriction is now removed.</p>
<h3>Turkic UTF-8 locales are now seamlessly supported</h3>
<p> Turkic languages have different casing rules than other languages for the characters <tt>&quot;i&quot;</tt> and <tt>&quot;I&quot;</tt>. The uppercase of <tt>&quot;i&quot;</tt> is LATIN CAPITAL LETTER I WITH DOT ABOVE (U+0130); and the lowercase of <tt>&quot;I&quot;</tt> is LATIN SMALL LETTER DOTLESS I (U+0131). Unicode furnishes alternate casing rules for use with Turkic languages. Previously, Perl ignored these, but now, it uses them when it detects that it is operating under a Turkic UTF-8 locale.</p>
<h3>It is now possible to compile perl to always use thread-safe locale operations.</h3>
<p> Previously, these calls were only used when the perl was compiled to be multi-threaded. To always enable them, add </p>
<pre>
 -Accflags='-DUSE_THREAD_SAFE_LOCALE'
</pre>
<p> to your <i>Configure</i> flags.</p>
<h3>Eliminate opASSIGN macro usage from core</h3>
<p> This macro is still defined but no longer used in core</p>
<h3>-Drv now means something on -DDEBUGGING builds</h3>
<p> Now, adding the verbose flag (<tt>&quot;-Dv&quot;</tt>) to the <tt>&quot;-Dr&quot;</tt> flag turns on all possible regular expression debugging.</p>
<h2>Incompatible Changes</h2>
<h3>Assigning non-zero to $[ is fatal</h3>
<p> Setting <tt>$[</tt> to a non-zero value has been deprecated since Perl 5.12 and now throws a fatal error. See &quot;Assigning non-zero to <tt>$[</tt> is fatal&quot; in perldeprecation.</p>
<h3>Delimiters must now be graphemes</h3>
<p> See &#8220;Use of unassigned code point or non-standalone grapheme for a delimiter.&#8221; in perldeprecation</p>
<h3>Some formerly deprecated uses of an unescaped left brace { in regular expression patterns are now illegal</h3>
<p> But to avoid breaking code unnecessarily, most instances that issued a deprecation warning, remain legal and now have a non-deprecation warning raised. See &#8220;Unescaped left braces in regular expressions&#8221; in perldeprecation.</p>
<h3>Previously deprecated <code>sysread()</code>/<code>syswrite()</code> on :utf8 handles is now fatal</h3>
<p> Calling <code>sysread()</code>, <code>syswrite()</code>, <code>send()</code> or <code>recv()</code> on a <tt>&quot;:utf8&quot;</tt> handle, whether applied explicitly or implicitly, is now fatal. This was deprecated in perl 5.24. </p>
<p> There were two problems with calling these functions on <tt>&quot;:utf8&quot;</tt> handles:</p>
<dl>
<dt>&bull;</dt>
<dd> All four functions only paid attention to the <tt>&quot;:utf8&quot;</tt> flag. Other layers were completely ignored, so a handle with <tt>&quot;:encoding(UTF-16LE)&quot;</tt> layer would be treated as UTF-8. Other layers, such as compression are completely ignored with or without the <tt>&quot;:utf8&quot;</tt> flag.</dd>
<dt>&bull;</dt>
<dd> <code>sysread()</code> and <code>recv()</code> would read from the handle, skipping any validation by the layers, and do no validation of their own. This could lead to invalidly encoded perl scalars.</dd></dl>
<p> [perl #125760] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125760">https://rt.perl.org/Ticket/Display.html?id=125760</a>&gt;.</p>
<h3><code>my()</code> in false conditional prohibited</h3>
<p> Declarations such as <tt>&quot;my $x if 0&quot;</tt> are no longer permitted. </p>
<p> [perl #133543] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133543">https://rt.perl.org/Ticket/Display.html?id=133543</a>&gt;.</p>
<h3>Fatalize $* and $#</h3>
<p> These special variables, long deprecated, now throw exceptions when used. </p>
<p> [perl #133583] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133583">https://rt.perl.org/Ticket/Display.html?id=133583</a>&gt;.</p>
<h3>Fatalize unqualified use of <code>dump()</code></h3>
<p> The <tt>&quot;dump()&quot;</tt> function, long discouraged, may no longer be used unless it is fully qualified, <i>i.e.</i>, <tt>&quot;CORE::dump()&quot;</tt>. </p>
<p> [perl #133584] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133584">https://rt.perl.org/Ticket/Display.html?id=133584</a>&gt;.</p>
<h3>Remove <code>File::Glob::glob()</code></h3>
<p> The <tt>&quot;File::Glob::glob()&quot;</tt> function, long deprecated, has been removed and now throws an exception which advises use of <tt>&quot;File::Glob::bsd_glob()&quot;</tt> instead. </p>
<p> [perl #133586] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133586">https://rt.perl.org/Ticket/Display.html?id=133586</a>&gt;.</p>
<h3>pack() no longer can return malformed UTF-8</h3>
<p> It croaks if it would otherwise return a UTF-8 string that contains malformed UTF-8. This protects against potential security threats. This is considered a bug fix as well. [perl #131642] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131642">https://rt.perl.org/Ticket/Display.html?id=131642</a>&gt;.</p>
<h3>Any set of digits in the Common script are legal in a script run of another script</h3>
<p> There are several sets of digits in the Common script. <tt>&quot;[0-9]&quot;</tt> is the most familiar. But there are also <tt>&quot;[</tt>\x{FF10}-\x{FF19}]&quot;</code> (FULLWIDTH DIGIT ZERO &#8211; FULLWIDTH DIGIT NINE), and several sets for use in mathematical notation, such as the MATHEMATICAL DOUBLE-STRUCK DIGITs. Any of these sets should be able to appear in script runs of, say, Greek. But the design of 5.30 overlooked all but the ASCII digits <code>&quot;[0-9]&quot;</code>, so the design was flawed. This has been fixed, so is both a bug fix and an incompatibility. [perl #133547] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133547">https://rt.perl.org/Ticket/Display.html?id=133547</a>&gt;. </p>
<p> All digits in a run still have to come from the same set of ten digits.  </p>
<h3>JSON::PP enables allow_nonref by default</h3>
<p> As JSON::XS 4.0 changed its policy and enabled allow_nonref by default, JSON::PP also enabled allow_nonref by default.  </p>
<h2>Deprecations</h2>
<h3>In XS code, use of various macros dealing with UTF-8.</h3>
<p> This deprecation was scheduled to become fatal in 5.30, but has been delayed to 5.32 due to problems that showed up with some CPAN modules. For details of what&#8217;s affected, see perldeprecation.  </p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Translating from UTF-8 into the code point it represents now is done via a deterministic finite automaton, speeding it up. As a typical example, <code>&quot;ord(&quot;\x7fff&quot;)&quot;</code> now requires 12% fewer instructions than before. The performance of checking that a sequence of bytes is valid UTF-8 is similarly improved, again by using a DFA. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Eliminate recursion from <code>finalize_op()</code>. [perl #108276] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=108276">https://rt.perl.org/Ticket/Display.html?id=108276</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A handful of small optimizations related to character folding and character classes in regular expressions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Optimization of <code>&quot;IV&quot;</code> to <code>&quot;UV&quot;</code> conversions. [perl #133677] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133677">https://rt.perl.org/Ticket/Display.html?id=133677</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Speed up of the integer stringification algorithm by processing two digits at a time instead of one. [perl #133691] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133691">https://rt.perl.org/Ticket/Display.html?id=133691</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Improvements based on LGTM analysis and recommendation. (&lt;<a rel="nofollow" href="https://lgtm.com/projects/g/Perl/perl5/alerts/?mode=tree">https://lgtm.com/projects/g/Perl/perl5/alerts/?mode=tree</a>&gt;). [perl #133686] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133686">https://rt.perl.org/Ticket/Display.html?id=133686</a>&gt;. [perl #133699] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133699">https://rt.perl.org/Ticket/Display.html?id=133699</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Code optimizations in <i>regcomp.c</i>, <i>regcomp.h</i>, <i>regexec.c</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regular expression pattern matching of things like <code>&quot;qr/[^</code>a <code>]/&quot;</code> is significantly sped up, where <i>a</i> is any ASCII character. Other classes can get this speed up, but which ones is complicated and depends on the underlying bit patterns of those characters, so differs between ASCII and EBCDIC platforms, but all case pairs, like <code>&quot;qr/[Gg]/&quot;</code> are included, as is <code>&quot;[^01]&quot;</code>. </p>
 </dd></dl>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Archive::Tar has been upgraded from version 2.30 to 2.32. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B has been upgraded from version 1.74 to 1.76. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Concise has been upgraded from version 1.003 to 1.004. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Deparse has been upgraded from version 1.48 to 1.49. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> bignum has been upgraded from version 0.49 to 0.51. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> bytes has been upgraded from version 1.06 to 1.07. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Carp has been upgraded from version 1.38 to 1.50 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compress::Raw::Bzip2 has been upgraded from version 2.074 to 2.084. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compress::Raw::Zlib has been upgraded from version 2.076 to 2.084. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Config::Extensions has been upgraded from version 0.02 to 0.03. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Config::Perl::V. has been upgraded from version 0.29 to 0.32. This was due to a new configuration variable that has influence on binary compatibility: <code>&quot;USE_THREAD_SAFE_LOCALE&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> CPAN has been upgraded from version 2.20 to 2.22. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Data::Dumper has been upgraded from version 2.170 to 2.174 </p>
<p> Data::Dumper now avoids leaking when <code>&quot;croak&quot;</code>ing. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DB_File has been upgraded from version 1.840 to 1.843. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> deprecate has been upgraded from version 0.03 to 0.04. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::Peek has been upgraded from version 1.27 to 1.28. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::PPPort has been upgraded from version 3.40 to 3.52. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Digest::SHA has been upgraded from version 6.01 to 6.02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Encode has been upgraded from version 2.97 to 3.01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Errno has been upgraded from version 1.29 to 1.30. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> experimental has been upgraded from version 0.019 to 0.020. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::CBuilder has been upgraded from version 0.280230 to 0.280231. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Manifest has been upgraded from version 1.70 to 1.72. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Miniperl has been upgraded from version 1.08 to 1.09. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::ParseXS has been upgraded from version 3.39 to 3.40. <code>&quot;OUTLIST&quot;</code> parameters are no longer incorrectly included in the automatically generated function prototype. [perl #133654] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133654">https://rt.perl.org/Ticket/Display.html?id=133654</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> feature has been upgraded from version 1.52 to 1.54. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Copy has been upgraded from version 2.33 to 2.34. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Find has been upgraded from version 1.34 to 1.36. </p>
<p> <code>$File::Find::dont_use_nlink</code> now defaults to 1 on all platforms. [perl #133673] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133673">https://rt.perl.org/Ticket/Display.html?id=133673</a>&gt;. </p>
<p> Variables <code>$Is_Win32</code> and <code>$Is_VMS</code> are being initialized. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Glob has been upgraded from version 1.31 to 1.32. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Path has been upgraded from version 2.15 to 2.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Spec has been upgraded from version 3.74 to 3.78. </p>
<p> Silence Cwd warning on Android builds if <code>&quot;targetsh&quot;</code> is not defined. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Temp has been upgraded from version 0.2304 to 0.2309. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Filter::Util::Call has been upgraded from version 1.58 to 1.59. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> GDBM_File has been upgraded from version 1.17 to 1.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> HTTP::Tiny has been upgraded from version 0.070 to 0.076. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> I18N::Langinfo has been upgraded from version 0.17 to 0.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO has been upgraded from version 1.39 to 1.40. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO-Compress has been upgraded from version 2.074 to 2.084. </p>
<p> Adds support for <code>&quot;IO::Uncompress::Zstd&quot;</code> and <code>&quot;IO::Uncompress::UnLzip&quot;</code>. </p>
<p> The <code>&quot;BinModeIn&quot;</code> and <code>&quot;BinModeOut&quot;</code> options are now no-ops. ALL files will be read/written in binmode. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::Cmd has been upgraded from version 1.00 to 1.02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> JSON::PP has been upgraded from version 2.97001 to 4.02. </p>
<p> JSON::PP as JSON::XS 4.0 enables <code>&quot;allow_nonref&quot;</code> by default. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> lib has been upgraded from version 0.64 to 0.65. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locale::Codes has been upgraded from version 3.56 to 3.57. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigInt has been upgraded from version 1.999811 to 1.999816. </p>
<p> <code>&quot;bnok()&quot;</code> now supports the full Kronenburg extension. [cpan #95628] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=95628">https://rt.cpan.org/Ticket/Display.html?id=95628</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigInt::FastCalc has been upgraded from version 0.5006 to 0.5008. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigRat has been upgraded from version 0.2613 to 0.2614. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::CoreList has been upgraded from version 5.20180622 to 5.20190520. </p>
<p> Changes to B::Op_private and Config </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Load has been upgraded from version 0.32 to 0.34. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Metadata has been upgraded from version 1.000033 to 1.000036. </p>
<p> Properly clean up temporary directories after testing. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> NDBM_File has been upgraded from version 1.14 to 1.15. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Net::Ping has been upgraded from version 2.62 to 2.71. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ODBM_File has been upgraded from version 1.15 to 1.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PathTools has been upgraded from version 3.74 to 3.78. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> parent has been upgraded from version 0.236 to 0.237. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perl5db.pl has been upgraded from version 1.54 to 1.55. </p>
<p> Debugging threaded code no longer deadlocks in <code>&quot;DB::sub&quot;</code> nor <code>&quot;DB::lsub&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlfaq has been upgraded from version 5.021011 to 5.20190126. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::encoding has been upgraded from version 0.26 to 0.27. </p>
<p> Warnings enabled by setting the <code>&quot;WARN_ON_ERR&quot;</code> flag in <code>$PerlIO::encoding::fallback</code> are now only produced if warnings are enabled with <code>&quot;use warnings &quot;utf8&quot;;&quot;</code> or setting <code>$^W</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::scalar has been upgraded from version 0.29 to 0.30. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> podlators has been upgraded from version 4.10 to 4.11. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> POSIX has been upgraded from version 1.84 to 1.88. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> re has been upgraded from version 0.36 to 0.37. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> SDBM_File has been upgraded from version 1.14 to 1.15. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> sigtrap has been upgraded from version 1.08 to 1.09. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Storable has been upgraded from version 3.08 to 3.15. </p>
<p> Storable no longer probes for recursion limits at build time. [perl #133708] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133708">https://rt.perl.org/Ticket/Display.html?id=133708</a>&gt; and others. </p>
<p> Metasploit exploit code was included to test for CVE-2015-1992 detection, this caused anti-virus detections on at least one AV suite. The exploit code has been removed and replaced with a simple functional test. [perl #133706] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133706">https://rt.perl.org/Ticket/Display.html?id=133706</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test::Simple has been upgraded from version 1.302133 to 1.302162. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Thread::Queue has been upgraded from version 3.12 to 3.13. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> threads::shared has been upgraded from version 1.58 to 1.60. </p>
<p> Added support for extra tracing of locking, this requires a <code>&quot;-DDEBUGGING&quot;</code> and extra compilation flags. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::HiRes has been upgraded from version 1.9759 to 1.9760. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::Local has been upgraded from version 1.25 to 1.28. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::Piece has been upgraded from version 1.3204 to 1.33. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::Collate has been upgraded from version 1.25 to 1.27. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::UCD has been upgraded from version 0.70 to 0.72. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> User::grent has been upgraded from version 1.02 to 1.03. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> utf8 has been upgraded from version 1.21 to 1.22. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> vars has been upgraded from version 1.04 to 1.05. </p>
<p> <code>&quot;vars.pm&quot;</code> no longer disables non-vars strict when checking if strict vars is enabled. [perl #130674] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=130674">https://rt.perl.org/Ticket/Display.html?id=130674</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> version has been upgraded from version 0.9923 to 0.9924. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> warnings has been upgraded from version 1.42 to 1.44. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> XS::APItest has been upgraded from version 0.98 to 1.00. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> XS::Typemap has been upgraded from version 0.16 to 0.17. </p>
 </dd></dl>
<h3>Removed Modules and Pragmata</h3>
<p> The following modules will be removed from the core distribution in a future release, and will at that time need to be installed from CPAN. Distributions on CPAN which require these modules will need to list them as prerequisites. </p>
<p> The core versions of these modules will now issue <code>&quot;deprecated&quot;</code>-category warnings to alert you to this fact. To silence these deprecation warnings, install the modules in question from CPAN. </p>
<p> Note that these are (with rare exceptions) fine modules that you are encouraged to continue to use. Their disinclusion from core primarily hinges on their necessity to bootstrapping a fully functional, CPAN-capable Perl installation, not usually on concerns over their design. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> B::Debug is no longer distributed with the core distribution. It continues to be available on CPAN as <code>&quot;B::Debug &lt;<a rel="nofollow" href="https://metacpan.org/pod/B::Debug">https://metacpan.org/pod/B::Debug</a>&gt;&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locale::Codes has been removed at the request of its author. It continues to be available on CPAN as <code>&quot;Locale::Codes &lt;<a rel="nofollow" href="https://metacpan.org/pod/Locale::Codes">https://metacpan.org/pod/Locale::Codes</a>&gt;&quot;</code> [perl #133458] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133458">https://rt.perl.org/Ticket/Display.html?id=133458</a>&gt;. </p>
 </dd></dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> We have attempted to update the documentation to reflect the changes listed in this document. If you find any we have missed, send email to perlbug [at] perl.org &lt;mailto:perlbug [at] perl.org&gt;. </p>
<p> <i>perlapi</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;AvFILL()&quot;</code> was wrongly listed as deprecated. This has been corrected. [perl #133278] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133278">https://rt.perl.org/Ticket/Display.html?id=133278</a>&gt; </p>
 </dd></dl>
<p> <i>perlop</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> We no longer have null (empty line) here doc terminators, so perlop should not refer to them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The behaviour of <code>&quot;tr&quot;</code> when the delimiter is an apostrophe has been clarified. In particular, hyphens aren&#8217;t special, and <code>&quot;\x{}&quot;</code> isn&#8217;t interpolated. [perl #130679] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=130679">https://rt.perl.org/Ticket/Display.html?id=130679</a>&gt; </p>
 </dd></dl>
<p> <i>perlreapi, perlvar</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Improve docs for lastparen, lastcloseparen. </p>
 </dd></dl>
<p> <i>perlfunc</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The entry for ``-X&#8217;&#8216; in perlfunc has been clarified to indicate that symbolic links are followed for most tests. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Clarification of behaviour of <code>&quot;reset EXPR&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Try to clarify that <code>&quot;ref(qr/xx/)&quot;</code> returns <code>&quot;Regexp&quot;</code> rather than <code>&quot;REGEXP&quot;</code> and why. [perl #133751] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133751">https://rt.perl.org/Ticket/Display.html?id=133751</a>&gt;. </p>
 </dd></dl>
<p> <i>perlreref</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Clarification of the syntax of /(?(cond)yes)/. </p>
 </dd></dl>
<p> <i>perllocale</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> There are actually two slightly different types of UTF-8 locales: one for Turkic languages and one for everything else. Starting in Perl v5.30, Perl seamlessly handles both types. </p>
 </dd></dl>
<p> <i>perlrecharclass</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Added a note for the ::xdigit:: character class. </p>
 </dd></dl>
<p> <i>perlvar</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> More specific documentation of paragraph mode. [perl #133722] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133722">https://rt.perl.org/Ticket/Display.html?id=133722</a>&gt;. </p>
 </dd></dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.  </p>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> As noted under ``Incompatible Changes&#8217;&#8216; above, the deprecation warning ``Unescaped left brace in regex is deprecated here (and will be fatal in Perl 5.30), passed through in regex; marked by &lt;-- HERE in m/%s/&#8216;&#8216; has been changed to the non-deprecation warning ``Unescaped left brace in regex is passed through in regex; marked by &lt;-- HERE in m/%s/&#8216;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Specifying <code>&quot;\o{}&quot;</code> without anything between the braces now yields the fatal error message ``Empty \o{}&#8216;&#8216;. Previously it was ``Number with no digits&#8217;&#8216;. This means the same wording is used for this kind of error as with similar constructs such as <code>&quot;\p{}&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Within the scope of the experimental feature <code>&quot;use re &#8216;strict&#8217;&quot;</code>, specifying <code>&quot;\x{}&quot;</code> without anything between the braces now yields the fatal error message ``Empty \x{}&#8216;&#8216;. Previously it was ``Number with no digits&#8217;&#8216;. This means the same wording is used for this kind of error as with similar constructs such as <code>&quot;\p{}&quot;</code>. It is legal, though not wise to have an empty <code>&quot;\x&quot;</code> outside of <code>&quot;re &#8216;strict&#8217;&quot;</code>; it silently generates a NUL character. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Type of arg <code>%d</code> to <code>%s</code> must be <code>%s</code> (not <code>%s</code>) </p>
<p> Attempts to push, pop, etc on a hash or glob now produce this message rather than complaining that they no longer work on scalars. [perl #130367] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=130367">https://rt.perl.org/Ticket/Display.html?id=130367</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Prototype not terminated </p>
<p> The file and line number is now reported for this error. [perl #133524] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133524">https://rt.perl.org/Ticket/Display.html?id=133524</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under <code>&quot;-Dr&quot;</code> (or <code>&quot;use re &#8216;Debug&#8217;&quot;</code>) the compiled regex engine program is displayed. It used to use two different spellings for <i>infinity</i>, <code>&quot;INFINITY&quot;</code>, and <code>&quot;INFTY&quot;</code>. It now uses the latter exclusively, as that spelling has been around the longest. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<h3>xsubpp</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The generated prototype (with <code>&quot;PROTOTYPES: ENABLE&quot;</code>) would include <code>&quot;OUTLIST&quot;</code> parameters, but these aren&#8217;t arguments to the perl function. This has been rectified. [perl #133654] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133654">https://rt.perl.org/Ticket/Display.html?id=133654</a>&gt;. </p>
 </dd></dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Normally the thread-safe locale functions are used only on threaded builds. It is now possible to force their use on unthreaded builds on systems that have them available, by including the <code>&quot;-Accflags=&#8216;-DUSE_THREAD_SAFE_LOCALE&#8217;&quot;</code> option to <i>Configure</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Improve detection of memrchr, strlcat, and strlcpy </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Improve Configure detection of <code>memmem()</code>. [perl #133760] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133760">https://rt.perl.org/Ticket/Display.html?id=133760</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Multiple improvements and fixes for -DPERL_GLOBAL_STRUCT build option. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix -DPERL_GLOBAL_STRUCT_PRIVATE build option. </p>
 </dd></dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <i>t/lib/croak/op</i> [perl #130367] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=130367">https://rt.perl.org/Ticket/Display.html?id=130367</a>&gt;. </p>
<p> separate error for <code>&quot;push&quot;</code>, etc. on hash/glob. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/svleak.t</i> [perl #133660] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133660">https://rt.perl.org/Ticket/Display.html?id=133660</a>&gt;. </p>
<p> Add test for <code>&quot;goto &amp;sub&quot;</code> in overload leaking. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Split <i>t/re/fold_grind.t</i> into multiple test files. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix intermittent tests which failed due to race conditions which surface during parallel testing. [perl #133740] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133740">https://rt.perl.org/Ticket/Display.html?id=133740</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Thoroughly test paragraph mode, using a new test file, <i>t/io/paragraph_mode.t</i>. [perl #133722] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133722">https://rt.perl.org/Ticket/Display.html?id=133722</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some tests in <i>t/io/eintr.t</i> caused the process to hang on pre-16 Darwin. These tests are skipped for those version of Darwin. </p>
 </dd></dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>HP-UX 11.11</dt>
<dd> <p> An obscure problem in <code>&quot;pack()&quot;</code> when compiling with HP C-ANSI-C has been fixed by disabling optimizations in <i>pp_pack.c</i>. </p>
 </dd>
<dt>Mac OS X</dt>
<dd> <p> Perl&#8217;s build and testing process on Mac OS X for <code>&quot;-Duseshrplib&quot;</code> builds is now compatible with Mac OS X System Integrity Protection (SIP). </p>
<p> SIP prevents binaries in <i>/bin</i> (and a few other places) being passed the <code>&quot;DYLD_LIBRARY_PATH&quot;</code> environment variable. For our purposes this prevents <code>&quot;DYLD_LIBRARY_PATH&quot;</code> from being passed to the shell, which prevents that variable being passed to the testing or build process, so running <code>&quot;perl&quot;</code> couldn&#8217;t find <i>libperl.dylib</i>. </p>
<p> To work around that, the initial build of the <i>perl</i> executable expects to find <i>libperl.dylib</i> in the build directory, and the library path is then adjusted during installation to point to the installed library. </p>
<p> [perl #126706] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126706">https://rt.perl.org/Ticket/Display.html?id=126706</a>&gt;. </p>
 </dd>
<dt>Minix3</dt>
<dd> <p> Some support for Minix3 has been re-added. </p>
 </dd>
<dt>Cygwin</dt>
<dd> <p> Cygwin doesn&#8217;t make <code>&quot;cuserid&quot;</code> visible. </p>
 </dd>
<dt>Win32 Mingw</dt>
<dd> <p> C99 math functions are now available. </p>
 </dd>
<dt>Windows</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;USE_CPLUSPLUS&quot;</code> build option which has long been available in <i>win32/Makefile</i> (for <code>nmake</code>) and <i>win32/makefile.mk</i> (for <code>dmake</code>) is now also available in <i>win32/GNUmakefile</i> (for <code>gmake</code>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>nmake</code> makefile no longer defaults to Visual C++ 6.0 (a very old version which is unlikely to be widely used today). As a result, it is now a requirement to specify the <code>&quot;CCTYPE&quot;</code> since there is no obvious choice of which modern version to default to instead. Failure to specify <code>&quot;CCTYPE&quot;</code> will result in an error being output and the build will stop. </p>
<p> (The <code>dmake</code> and <code>gmake</code> makefiles will automatically detect which compiler is being used, so do not require <code>&quot;CCTYPE&quot;</code> to be set. This feature has not yet been added to the <code>nmake</code> makefile.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sleep()&quot;</code> with warnings enabled for a <code>&quot;USE_IMP_SYS&quot;</code> build no longer warns about the sleep timeout being too large. [perl #133376] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133376">https://rt.perl.org/Ticket/Display.html?id=133376</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Support for compiling perl on Windows using Microsoft Visual Studio 2019 (containing Visual C++ 14.2) has been added. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>socket()</code> now sets <code>$!</code> if the protocol, address family and socket type combination is not found. [perl #133853] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133853">https://rt.perl.org/Ticket/Display.html?id=133853</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Windows Server 2003 SP1 Platform SDK build, with its early x64 compiler and tools, was accidentally broken in Perl 5.27.9. This has now been fixed. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The sizing pass has been eliminated from the regular expression compiler. An extra pass may instead be needed in some cases to count the number of parenthetical capture groups. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new function &quot;<code>&quot;my_strtod&quot;</code>&quot; in perlapi or its synonym, <code>Strtod()</code>, is now available with the same signature as the libc <code>strtod()</code>. It provides <code>strotod()</code> equivalent behavior on all platforms, using the best available precision, depending on platform capabilities and <i>Configure</i> options, while handling locale-related issues, such as if the radix character should be a dot or comma. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Added <code>&quot;newSVsv_nomg()&quot;</code> to copy a SV without processing get magic on the source. [perl #132964] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132964">https://rt.perl.org/Ticket/Display.html?id=132964</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> It is now forbidden to malloc more than <code>&quot;PTRDIFF_T_MAX&quot;</code> bytes. Much code (including C optimizers) assumes that all data structures will not be larger than this, so this catches such attempts before overflow happens. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Two new regnodes have been introduced <code>&quot;EXACT_ONLY8&quot;</code>, and <code>&quot;EXACTFU_ONLY8&quot;</code>. They&#8217;re equivalent to <code>&quot;EXACT&quot;</code> and <code>&quot;EXACTFU&quot;</code>, except that they contain a code point which requires UTF-8 to represent/match. Hence, if the target string isn&#8217;t UTF-8, we know it can&#8217;t possibly match, without needing to try. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;print_bytes_for_locale()&quot;</code> is now defined if <code>&quot;DEBUGGING&quot;</code>, Prior, it didn&#8217;t get defined unless <code>&quot;LC_COLLATE&quot;</code> was defined on the platform. </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Compilation under <code>&quot;-DPERL_MEM_LOG&quot;</code> and <code>&quot;-DNO_LOCALE&quot;</code> have been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl 5.28 introduced an <code>&quot;index()&quot;</code> optimization when comparing to -1 (or indirectly, e.g. &gt;= 0). When this optimization was triggered inside a <code>&quot;when&quot;</code> clause it caused a warning (``Argument <code>%s</code> isn&#8217;t numeric in smart match&#8217;&#8216;). This has now been fixed. [perl #133368] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133368">https://rt.perl.org/Ticket/Display.html?id=133368</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The new in-place editing code no longer leaks directory handles. [perl #133314] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133314">https://rt.perl.org/Ticket/Display.html?id=133314</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Warnings produced from constant folding operations on overloaded values no longer produce spurious ``Use of uninitialized value&#8217;&#8216; warnings. [perl #132683] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132683">https://rt.perl.org/Ticket/Display.html?id=132683</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix for ``mutator not seen in (lex = ...) .= ...&#8216;&#8216; [perl #133441] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133441">https://rt.perl.org/Ticket/Display.html?id=133441</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pack &quot;u&quot;, &quot;invalid uuencoding&quot;&quot;</code> now properly NUL terminates the zero-length SV produced. [perl #132655] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132655">https://rt.perl.org/Ticket/Display.html?id=132655</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Improve the debugging output for <code>calloc()</code> calls with <code>&quot;-Dm&quot;</code>. [perl #133439] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133439">https://rt.perl.org/Ticket/Display.html?id=133439</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regexp script runs were failing to permit ASCII digits in some cases. [perl #133547] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133547">https://rt.perl.org/Ticket/Display.html?id=133547</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On Unix-like systems supporting a platform-specific technique for determining <code>$^X</code>, Perl failed to fall back to the generic technique when the platform-specific one fails (for example, a Linux system with /proc not mounted). This was a regression in Perl 5.28.0. [perl #133573] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133573">https://rt.perl.org/Ticket/Display.html?id=133573</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> SDBM_File is now more robust with corrupt database files. The improvements do not make SDBM files suitable as an interchange format. [perl #132147] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132147">https://rt.perl.org/Ticket/Display.html?id=132147</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;binmode($fh);&quot;</code> or <code>&quot;binmode($fh, &#8216;:raw&#8217;);&quot;</code> now properly removes the <code>&quot;:utf8&quot;</code> flag from the default <code>&quot;:crlf&quot;</code> I/O layer on Win32. [perl #133604] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133604">https://rt.perl.org/Ticket/Display.html?id=133604</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The experimental reference aliasing feature was misinterpreting array and hash slice assignment as being localised, e.g. </p>
<pre><code>    \(@a[3,5,7]) = \(....);
</code></pre>
<p> was being interpreted as: </p>
<pre><code>    local \(@a[3,5,7]) = \(....);
</code></pre>
<p> [perl #133538] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133538">https://rt.perl.org/Ticket/Display.html?id=133538</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sort SUBNAME&quot;</code> within an <code>&quot;eval EXPR&quot;</code> when <code>&quot;EXPR&quot;</code> was UTF-8 upgraded could panic if the <code>&quot;SUBNAME&quot;</code> was non-ASCII. [perl #134061] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=134061">https://rt.perl.org/Ticket/Display.html?id=134061</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Correctly handle <code>realloc()</code> modifying <code>&quot;errno&quot;</code> on success so that the modification isn&#8217;t visible to the perl user, since <code>realloc()</code> is called implicitly by the interpreter. This modification is permitted by the C standard, but has only been observed on FreeBSD 13.0-CURRENT. [perl #133958] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133958">https://rt.perl.org/Ticket/Display.html?id=133958</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now exposes POSIX <code>&quot;getcwd&quot;</code> as <code>&quot;Internals::getcwd()&quot;</code> if available. This is intended for use by <code>&quot;Cwd.pm&quot;</code> during bootstrapping and may be removed or changed without notice. This fixes some bootstrapping issues while building perl in a directory where some ancestor directory isn&#8217;t readable. [perl #133951] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133951">https://rt.perl.org/Ticket/Display.html?id=133951</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pack()&quot;</code> no longer can return malformed UTF-8. It croaks if it would otherwise return a UTF-8 string that contains malformed UTF-8. This protects against potential security threats. [perl #131642] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131642">https://rt.perl.org/Ticket/Display.html?id=131642</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> See ``Any set of digits in the Common script are legal in a script run of another script&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regular expression matching no longer leaves stale UTF-8 length magic when updating <code>$^R</code>. This could result in <code>&quot;length($^R)&quot;</code> returning an incorrect value. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Reduce recursion on ops [perl #108276] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=108276">https://rt.perl.org/Ticket/Display.html?id=108276</a>&gt;. </p>
<p> This can prevent stack overflow when processing extremely deep op trees. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Avoid leak in multiconcat with overloading. [perl #133789] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133789">https://rt.perl.org/Ticket/Display.html?id=133789</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The handling of user-defined <code>&quot;\p{}&quot;</code> properties (see ``User-Defined Character Properties&#8217;&#8216; in perlunicode) has been rewritten to be in C (instead of Perl). This speeds things up, but in the process several inconsistencies and bug fixes are made. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>1.</dt>
<dd> <p> A few error messages have minor wording changes. This is essentially because the new way is integrated into the regex error handling mechanism that marks the position in the input at which the error occurred. That was not possible previously. The messages now also contain additional back-trace-like information in case the error occurs deep in nested calls. </p>
 </dd>
<dt>2.</dt>
<dd> <p> A user-defined property is implemented as a perl subroutine with certain highly constrained naming conventions. It was documented previously that the sub would be in the current package if the package was unspecified. This turned out not to be true in all cases, but now it is. </p>
 </dd>
<dt>3.</dt>
<dd> <p> All recursive calls are treated as infinite recursion. Previously they would cause the interpreter to panic. Now, they cause the regex pattern to fail to compile. </p>
 </dd>
<dt>4.</dt>
<dd> <p> Similarly, any other error likely would lead to a panic; now to just the pattern failing to compile. </p>
 </dd>
<dt>5.</dt>
<dd> <p> The old mechanism did not detect illegal ranges in the definition of the property. Now, the range max must not be smaller than the range min. Otherwise, the pattern fails to compile. </p>
 </dd>
<dt>6.</dt>
<dd> <p> The intention was to have each sub called only once during the lifetime of the program, so that a property&#8217;s definition is immutable. This was relaxed so that it could be called once for all /i compilations, and potentially a second time for non-/i (the sub is passed a parameter indicating which). However, in practice there were instances when this was broken, and multiple calls were possible. Those have been fixed. Now (besides the /i,non-/i cases) the only way a sub can be called multiple times is if some component of it has not been defined yet. For example, suppose we have sub <code>IsA()</code> whose definition is known at compile time, and it in turn calls <code>isB()</code> whose definition is not yet known. <code>isA()</code> will be called each time a pattern it appears in is compiled. If <code>isA()</code> also calls <code>isC()</code> and that definition is known, <code>isC()</code> will be called just once. </p>
 </dd>
<dt>7.</dt>
<dd> <p> There were some races and very long hangs should one thread be compiling the same property as another simultaneously. These have now been fixed. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Fixed a failure to match properly. </p>
<p> An EXACTFish regnode has a finite length it can hold for the string being matched. If that length is exceeded, a second node is used for the next segment of the string, for as many regnodes as are needed. Care has to be taken where to break the string, in order to deal multi-character folds in Unicode correctly. If we want to break a string at a place which could potentially be in the middle of a multi-character fold, we back off one (or more) characters, leaving a shorter EXACTFish regnode. This backing off mechanism contained an off-by-one error. [perl #133756] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133756">https://rt.perl.org/Ticket/Display.html?id=133756</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A bare <code>&quot;eof&quot;</code> call with no previous file handle now returns true. [perl #133721] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133721">https://rt.perl.org/Ticket/Display.html?id=133721</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Failing to compile a format now aborts compilation. Like other errors in sub-parses this could leave the parser in a strange state, possibly crashing perl if compilation continued. [perl #132158] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132158">https://rt.perl.org/Ticket/Display.html?id=132158</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If an in-place edit is still in progress during global destruction and the process exit code (as stored in <code>$?</code>) is zero, perl will now treat the in-place edit as successful, replacing the input file with any output produced. </p>
<p> This allows code like: </p>
<pre><code>  perl -i -ne 'print &quot;Foo&quot;; last'
</code></pre>
<p> to replace the input file, while code like: </p>
<pre><code>  perl -i -ne 'print &quot;Foo&quot;; die'
</code></pre>
<p> will not. Partly resolves [perl #133659] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133659">https://rt.perl.org/Ticket/Display.html?id=133659</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A regression in 5.28 caused the following code to fail </p>
<pre><code> close(STDIN); open(CHILD, &quot;|wc -l&quot;)'
</code></pre>
<p> because the child&#8217;s stdin would be closed on exec. This has now been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed an issue where compiling a regexp containing both compile-time and run-time code blocks could lead to trying to compile something which is invalid syntax. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed build failures with <code>&quot;-DNO_LOCALE_NUMERIC&quot;</code> and <code>&quot;-DNO_LOCALE_COLLATE&quot;</code>. [perl #133696] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133696">https://rt.perl.org/Ticket/Display.html?id=133696</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Prevent the tests in <i>ext/B/t/strict.t</i> from being skipped. [perl #133713] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=133713">https://rt.perl.org/Ticket/Display.html?id=133713</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;/di&quot;</code> nodes ending or beginning in <i>s</i> are now <code>&quot;EXACTF&quot;</code>. We do not want two <code>&quot;EXACTFU&quot;</code> to be joined together during optimization, and to form a <code>&quot;ss&quot;</code>, <code>&quot;sS&quot;</code>, <code>&quot;Ss&quot;</code> or <code>&quot;SS&quot;</code> sequence; they are the only multi-character sequences which may match differently under <code>&quot;/ui&quot;</code> and <code>&quot;/di&quot;</code>. </p>
 </dd></dl>
<h2>Acknowledgements</h2>
<p> Perl 5.30.0 represents approximately 11 months of development since Perl 5.28.0 and contains approximately 620,000 lines of changes across 1,300 files from 58 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 510,000 lines of changes to 750 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its fourth decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.30.0: </p>
<p> Aaron Crane, Abigail, Alberto Simões, Alexandr Savca, Andreas König, Andy Dougherty, Aristotle Pagaltzis, Brian Greenfield, Chad Granum, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, Dagfinn Ilmari Mannsåker, Dan Book, Dan Dedrick, Daniel Dragan, Dan Kogai, David Cantrell, David Mitchell, Dominic Hargreaves, E. Choroba, Ed J, Eugen Konkov, François Perrad, Graham Knop, Hauke D, H.Merijn Brand, Hugo van der Sanden, Jakub Wilk, James Clarke, James E Keenan, Jerry D. Hedden, Jim Cromie, John SJ Anderson, Karen Etheridge, Karl Williamson, Leon Timmermans, Matthias Bethke, Nicholas Clark, Nicolas R., Niko Tyni, Pali, Petr Písař, Phil Pearl (Lobbes), Richard Leach, Ryan Voots, Sawyer X, Shlomi Fish, Sisyphus, Slaven Rezic, Steve Hay, Sullivan Beck, Tina Müller, Tomasz Konojacki, Tom Wyant, Tony Cook, Unicode Consortium, Yves Orton, Zak B. Elep. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of most of the (very much appreciated) contributors who reported issues to the Perl bug tracker. Noteworthy in this release were the large number of bug fixes made possible by Sergey Aleynikov&#8217;s high quality perlbug reports for issues he discovered by fuzzing with AFL. </p>
<p> Many of the changes included in this version originated in the CPAN modules included in Perl&#8217;s core. We&#8217;re grateful to the entire CPAN community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><i>AUTHORS</i><i></i> file in the Perl source distribution.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the perl bug database at &lt;<a rel="nofollow" href="https://rt.perl.org/">https://rt.perl.org/</a>&gt;. There may also be information at &lt;<a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a>&gt;, the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications which make it inappropriate to send to a publicly archived mailing list, then see ``SECURITY VULNERABILITY CONTACT INFORMATION&#8217;&#8216; in perlsec for details of how to report the issue.  </p>
<h2>Give Thanks</h2>
<p> If you wish to thank the Perl 5 Porters for the work we had done in Perl 5, you can do so by running the <code>&quot;perlthanks&quot;</code> program: </p>
<pre><code>    perlthanks
</code></pre>
<p> This will send an email to the Perl 5 Porters list with your show of thanks.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><i>INSTALL</i><i></i> file for how to build Perl. </p>
<p> The <i></i><i>README</i><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
