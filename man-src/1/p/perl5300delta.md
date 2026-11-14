---
title: "perl5300delta(1)"
name: "perl5300delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5300delta/"
description: "perldelta – what is new for perl v5.30.0"
---

<h2 class="name">NAME</h2>
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
<p> The Word_Break property, as in past Perl releases, remains tailored to behave more in line with expectations of Perl users. This means that sequential runs of horizontal white space characters are not broken apart, but kept as a single run. Unicode 11 changed from past versions to be more in line with Perl, but it left several white space characters as causing breaks: <font SIZE="-1">TAB, NO BREAK SPACE,</font> and <font SIZE="-1">FIGURE SPACE</font> (U+2007). We have decided to continue to use the previous Perl tailoring with regards to these.</p>
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
<h3>Turkic <font SIZE="-1">UTF-8</font> locales are now seamlessly supported</h3>
<p> Turkic languages have different casing rules than other languages for the characters <tt>&quot;i&quot;</tt> and <tt>&quot;I&quot;</tt>. The uppercase of <tt>&quot;i&quot;</tt> is <font SIZE="-1">LATIN CAPITAL LETTER I WITH DOT ABOVE</font> (U+0130); and the lowercase of <tt>&quot;I&quot;</tt> is <font SIZE="-1">LATIN SMALL LETTER DOTLESS I</font> (U+0131). Unicode furnishes alternate casing rules for use with Turkic languages. Previously, Perl ignored these, but now, it uses them when it detects that it is operating under a Turkic <font SIZE="-1">UTF-8</font> locale.</p>
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
<dt>&bull;</p>
<dd> All four functions only paid attention to the <tt>&quot;:utf8&quot;</tt> flag. Other layers were completely ignored, so a handle with <tt>&quot;:encoding(UTF-16LE)&quot;</tt> layer would be treated as <font SIZE="-1">UTF-8.</font> Other layers, such as compression are completely ignored with or without the <tt>&quot;:utf8&quot;</tt> flag.</p>
<dt>&bull;</p>
<dd> <code>sysread()</code> and <code>recv()</code> would read from the handle, skipping any validation by the layers, and do no validation of their own. This could lead to invalidly encoded perl scalars.</dl>
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
<h3>pack() no longer can return malformed <font SIZE="-1">UTF-8</font></h3>
<p> It croaks if it would otherwise return a <font SIZE="-1">UTF-8</font> string that contains malformed <font SIZE="-1">UTF-8.</font> This protects against potential security threats. This is considered a bug fix as well. [perl #131642] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131642">https://rt.perl.org/Ticket/Display.html?id=131642</a>&gt;.</p>
<h3>Any set of digits in the Common script are legal in a script run of another script</h3>
<p> There are several sets of digits in the Common script. <tt>&quot;[0-9]&quot;</tt> is the most familiar. But there are also <tt>&quot;[
