---
title: "perl5140delta(1)"
name: "perl5140delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5140delta/"
description: "perl5140delta – what is new for perl v5.14.0"
---

<h2 class="name">NAME</h2>
<p> perl5140delta &#8211; what is new for perl v5.14.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.12.0 release and the 5.14.0 release. </p>
<p> If you are upgrading from an earlier release such as 5.10.0, first read perl5120delta, which describes differences between 5.10.0 and 5.12.0. </p>
<p> Some of the bug fixes in this release have been backported to subsequent releases of 5.12.x. Those are indicated with the 5.12.x version in parentheses.</p>
<h2>Notice</h2>
<p> As described in perlpolicy, the release of Perl 5.14.0 marks the official end of support for Perl 5.10. Users of Perl 5.10 or earlier should consider upgrading to a more recent release of Perl.</p>
<h2>Core Enhancements</h2>
<h3>Unicode</h3>
<p> <i>Unicode Version 6.0 is now supported (mostly)</i> </p>
<p> Perl comes with the Unicode 6.0 data base updated with Corrigendum #8 &lt;<a rel="nofollow" href="http://www.unicode.org/versions/corrigendum8.html">http://www.unicode.org/versions/corrigendum8.html</a>&gt;, with one exception noted below. See &lt;<a rel="nofollow" href="http://unicode.org/versions/Unicode6.0.0/">http://unicode.org/versions/Unicode6.0.0/</a>&gt; for details on the new release. Perl does not support any Unicode provisional properties, including the new ones for this release. </p>
<p> Unicode 6.0 has chosen to use the name <tt>&quot;BELL&quot;</tt> for the character at U+1F514, which is a symbol that looks like a bell, and is used in Japanese cell phones. This conflicts with the long-standing Perl usage of having <tt>&quot;BELL&quot;</tt> mean the <font SIZE="-1">ASCII</font> <tt>&quot;BEL&quot;</tt> character, U+0007. In Perl 5.14, <tt>&quot;\N{BELL}&quot;</tt> continues to mean U+0007, but its use generates a deprecation warning message unless such warnings are turned off. The new name for U+0007 in Perl is <tt>&quot;ALERT&quot;</tt>, which corresponds nicely with the existing shorthand sequence for it, <tt>&quot;&quot;</tt>. <tt>&quot;\N{BEL}&quot;</tt> means U+0007, with no warning given. The character at U+1F514 has no name in 5.14, but can be referred to by <tt>&quot;\N{U+1F514}&quot;</tt>. In Perl 5.16, <tt>&quot;\N{BELL}&quot;</tt> will refer to U+1F514; all code that uses <tt>&quot;\N{BELL}&quot;</tt> should be converted to use <tt>&quot;\N{ALERT}&quot;</tt>, <tt>&quot;\N{BEL}&quot;</tt>, or <tt>&quot;&quot;</tt> before upgrading. </p>
<p> <i>Full functionality for </i>&quot;use feature &#8216;unicode_strings&#8217;&quot;<i></i> </p>
<p> This release provides full functionality for <tt>&quot;use feature 'unicode_strings'&quot;</tt>. Under its scope, all string operations executed and regular expressions compiled (even if executed outside its scope) have Unicode semantics. See &#8220;the &#8216;unicode_strings&#8217; feature&#8221; in feature. However, see &#8220;Inverted bracketed character classes and multi-character folds&#8221;, below. </p>
<p> This feature avoids most forms of the &#8220;Unicode Bug&#8221; (see &#8220;The &#8221;Unicode Bug&quot;&quot; in perlunicode for details). If there is any possibility that your code will process Unicode strings, you are <i>strongly</i> encouraged to use this subpragma to avoid nasty surprises. </p>
<p> <i></i>&quot;\N{NAME}&quot;<i> and </i>&quot;charnames&quot;<i> enhancements</i></p>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;\N{</tt>NAME<tt>}&quot;</tt> and <tt>&quot;charnames::vianame&quot;</tt> now know about the abbreviated character names listed by Unicode, such as <font SIZE="-1">NBSP, SHY, LRO, ZWJ,</font> etc.; all customary abbreviations for the C0 and C1 control characters (such as <font SIZE="-1">ACK, BEL, CAN,</font> etc.); and a few new variants of some C1 full names that are in common usage.</p>
<dt>&bull;</p>
<dd> Unicode has several <i>named character sequences</i>, in which particular sequences of code points are given names. <tt>&quot;\N{</tt>NAME<tt>}&quot;</tt> now recognizes these.</p>
<dt>&bull;</p>
<dd> <tt>&quot;\N{</tt>NAME<tt>}&quot;</tt>, <tt>&quot;charnames::vianame&quot;</tt>, and <tt>&quot;charnames::viacode&quot;</tt> now know about every character in Unicode. In earlier releases of Perl, they didn&#8217;t know about the Hangul syllables nor several <font SIZE="-1">CJK</font> (Chinese/Japanese/Korean) characters.</p>
<dt>&bull;</p>
<dd> It is now possible to override Perl&#8217;s abbreviations with your own custom aliases.</p>
<dt>&bull;</p>
<dd> You can now create a custom alias of the ordinal of a character, known by <tt>&quot;\N{</tt>NAME<tt>}&quot;</tt>, <tt>&quot;charnames::vianame()&quot;</tt>, and <tt>&quot;charnames::viacode()&quot;</tt>. Previously, aliases had to be to official Unicode character names. This made it impossible to create an alias for unnamed code points, such as those reserved for private use.</p>
<dt>&bull;</p>
<dd> The new function <code>charnames::string_vianame()</code> is a run-time version of <tt>&quot;\N{</tt>NAME<tt>}}&quot;</tt>, returning the string of characters whose Unicode name is its parameter. It can handle Unicode named character sequences, whereas the pre-existing <code>charnames::vianame()</code> cannot, as the latter returns a single code point.</dl>
<p> See charnames for details on all these changes. </p>
<p> <i>New warnings categories for problematic (non-)Unicode code points.</i> </p>
<p> Three new warnings subcategories of &#8220;utf8&#8221; have been added. These allow you to turn off some &#8220;utf8&#8221; warnings, while allowing other warnings to remain on. The three categories are: <tt>&quot;surrogate&quot;</tt> when <font SIZE="-1">UTF-16</font> surrogates are encountered; <tt>&quot;nonchar&quot;</tt> when Unicode non-character code points are encountered; and <tt>&quot;non_unicode&quot;</tt> when code points above the legal Unicode maximum of 0x10FFFF are encountered. </p>
<p> <i>Any unsigned value can be encoded as a character</i> </p>
<p> With this release, Perl is adopting a model that any unsigned value can be treated as a code point and encoded internally (as utf8) without warnings, not just the code points that are legal in Unicode. However, unless utf8 or the corresponding sub-category (see previous item) of lexical warnings have been explicitly turned off, outputting or executing a Unicode-defined operation such as upper-casing on such a code point generates a warning. Attempting to input these using strict rules (such as with the <tt>&quot;:encoding(UTF-8)&quot;</tt> layer) will continue to fail. Prior to this release, handling was inconsistent and in places, incorrect. </p>
<p> Unicode non-characters, some of which previously were erroneously considered illegal in places by Perl, contrary to the Unicode Standard, are now always legal internally. Inputting or outputting them works the same as with the non-legal Unicode code points, because the Unicode Standard says they are (only) illegal for &#8220;open interchange&#8221;. </p>
<p> <i>Unicode database files not installed</i> </p>
<p> The Unicode database files are no longer installed with Perl. This doesn&#8217;t affect any functionality in Perl and saves significant disk space. If you need these files, you can download them from &lt;<a rel="nofollow" href="http://www.unicode.org/Public/zipped/6.0.0/">http://www.unicode.org/Public/zipped/6.0.0/</a>&gt;.</p>
<h3>Regular Expressions</h3>
<p> <i></i>&quot;(?^&#8230;)&quot;<i> construct signifies default modifiers</i> </p>
<p> An <font SIZE="-1">ASCII</font> caret <tt>&quot;^&quot;</tt> immediately following a <tt>&quot;(?&quot;</tt> in a regular expression now means that the subexpression does not inherit surrounding modifiers such as <tt>&quot;/i&quot;</tt>, but reverts to the Perl defaults. Any modifiers following the caret override the defaults. </p>
<p> Stringification of regular expressions now uses this notation. For example, <tt>&quot;qr/hlagh/i&quot;</tt> would previously be stringified as <tt>&quot;(?i-xsm:hlagh)&quot;</tt>, but now it&#8217;s stringified as <tt>&quot;(?^i:hlagh)&quot;</tt>. </p>
<p> The main purpose of this change is to allow tests that rely on the stringification <i>not</i> to have to change whenever new modifiers are added. See &#8220;Extended Patterns&#8221; in perlre. </p>
<p> This change is likely to break code that compares stringified regular expressions with fixed strings containing <tt>&quot;?-xism&quot;</tt>. </p>
<p> <i></i>&quot;/d&quot;<i>, </i>&quot;/l&quot;<i>, </i>&quot;/u&quot;<i>, and </i>&quot;/a&quot;<i> modifiers</i> </p>
<p> Four new regular expression modifiers have been added. These are mutually exclusive: one only can be turned on at a time.</p>
<dl>
<dt>&bull;</p>
<dd> The <tt>&quot;/l&quot;</tt> modifier says to compile the regular expression as if it were in the scope of <tt>&quot;use locale&quot;</tt>, even if it is not.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;/u&quot;</tt> modifier says to compile the regular expression as if it were in the scope of a <tt>&quot;use feature 'unicode_strings'&quot;</tt> pragma.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;/d&quot;</tt> (default) modifier is used to override any <tt>&quot;use locale&quot;</tt> and <tt>&quot;use feature 'unicode_strings'&quot;</tt> pragmas in effect at the time of compiling the regular expression.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;/a&quot;</tt> regular expression modifier restricts <tt>&quot;\s&quot;</tt>, <tt>&quot;\d&quot;</tt> and <tt>&quot;\w&quot;</tt> and the <font SIZE="-1">POSIX</font> (<tt>&quot;[[:posix:]]&quot;</tt>) character classes to the <font SIZE="-1">ASCII</font> range. Their complements and <tt>&quot;&quot;</tt> and <tt>&quot;\B&quot;</tt> are correspondingly affected. Otherwise, <tt>&quot;/a&quot;</tt> behaves like the <tt>&quot;/u&quot;</tt> modifier, in that case-insensitive matching uses Unicode semantics. </p>
<p> If the <tt>&quot;/a&quot;</tt> modifier is repeated, then additionally in case-insensitive matching, no <font SIZE="-1">ASCII</font> character can match a non-ASCII character. For example, </p>
<pre>
    &quot;k&quot;     =~ /\N{KELVIN SIGN}/ai
    &quot;�&quot; =~ /ss/ai
</pre>
<p> match but </p>
<pre>
    &quot;k&quot;    =~ /\N{KELVIN SIGN}/aai
    &quot;�&quot; =~ /ss/aai
</pre>
<p> do not match.</dl>
<p> See &#8220;Modifiers&#8221; in perlre for more detail. </p>
<p> <i>Non-destructive substitution</i> </p>
<p> The substitution (<tt>&quot;s///&quot;</tt>) and transliteration (<tt>&quot;y///&quot;</tt>) operators now support an <tt>&quot;/r&quot;</tt> option that copies the input variable, carries out the substitution on the copy, and returns the result. The original remains unmodified. </p>
<pre>
  my $old = &quot;cat&quot;;
  my $new = $old =~ s/cat/dog/r;
  # $old is &quot;cat&quot; and $new is &quot;dog&quot;
</pre>
<p> This is particularly useful with <tt>&quot;map&quot;</tt>. See perlop for more examples. </p>
<p> <i>Re-entrant regular expression engine</i> </p>
<p> It is now safe to use regular expressions within <tt>&quot;(?{...})&quot;</tt> and <tt>&quot;(??{...})&quot;</tt> code blocks inside regular expressions. </p>
<p> These blocks are still experimental, however, and still have problems with lexical (<tt>&quot;my&quot;</tt>) variables and abnormal exiting. </p>
<p> <i></i>&quot;use re &#8216;/flags&#8217;&quot;<i></i> </p>
<p> The <tt>&quot;re&quot;</tt> pragma now has the ability to turn on regular expression flags till the end of the lexical scope: </p>
<pre>
    use re &quot;/x&quot;;
    &quot;foo&quot; =~ / (.+) /;  # /x implied
</pre>
<p> See &#8220;&#8217;/flags&#8217; mode&#8221; in re for details. </p>
<p> <i>\o{&#8230;} for octals</i> </p>
<p> There is a new octal escape sequence, <tt>&quot;\o&quot;</tt>, in doublequote-like contexts. This construct allows large octal ordinals beyond the current max of 0777 to be represented. It also allows you to specify a character in octal which can safely be concatenated with other regex snippets and which won&#8217;t be confused with being a backreference to a regex capture group. See &#8220;Capture groups&#8221; in perlre. </p>
<p> <i>Add </i>&quot;\p{Titlecase}&quot;<i> as a synonym for </i>&quot;\p{Title}&quot;<i></i> </p>
<p> This synonym is added for symmetry with the Unicode property names <tt>&quot;\p{Uppercase}&quot;</tt> and <tt>&quot;\p{Lowercase}&quot;</tt>. </p>
<p> <i>Regular expression debugging output improvement</i> </p>
<p> Regular expression debugging output (turned on by <tt>&quot;use re 'debug'&quot;</tt>) now uses hexadecimal when escaping non-ASCII characters, instead of octal. </p>
<p> <i>Return value of </i>&quot;delete $+{&#8230;}&quot;<i></i> </p>
<p> Custom regular expression engines can now determine the return value of <tt>&quot;delete&quot;</tt> on an entry of <tt>&quot;%+&quot;</tt> or <tt>&quot;%-&quot;</tt>.</p>
<h3>Syntactical Enhancements</h3>
<p> <i>Array and hash container functions accept references</i> </p>
<p> <code>Warning:</code> This feature is considered experimental, as the exact behaviour may change in a future version of Perl. </p>
<p> All builtin functions that operate directly on array or hash containers now also accept unblessed hard references to arrays or hashes: </p>
<pre><code>
| -- -- -- -- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- -- -- - |
    | Traditional syntax | Terse syntax |
    | -- -- -- -- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- -- -- - |
    | push @$arrayref,
    @stuff | push $arrayref, @stuff | | unshift @$arrayref, @stuff | unshift $arrayref, @stuff | | pop @$arrayref | pop $arrayref | | shift @$arrayref | shift $arrayref | | splice @$arrayref, 0, 2 | splice $arrayref, 0, 2 | | keys % $hashref | keys $hashref | | keys @$arrayref | keys $arrayref | | values % $hashref | values $hashref | | values @$arrayref | values $arrayref | | ($k, $v) = each % $hashref | ($k, $v) = each $hashref | | ($k, $v) = each @$arrayref | ($k, $v) = each $arrayref | | -- -- -- -- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- -- -- - |
</code></pre>
<p> This allows these builtin functions to act on long dereferencing chains or on the return value of subroutines without needing to wrap them in <tt>&quot;@{}&quot;</tt> or <tt>&quot;%{}&quot;</tt>: </p>
<p>push @{$obj-&gt;tags}, $new_tag;<br />
#old way<br />
    push $obj-&gt;tags,<br />
    $new_tag;<br />
#new way for (keys % {$hoh-&gt;{genres} {artists}})<br />
{<br />
    &#8230;<br />
}<br />
#old way for (keys $hoh-&gt;{genres} {artists})<br />
{<br />
    &#8230;<br />
}<br />
#new way</p>
<p> <i>Single term prototype</i> </p>
<p> The <tt>&quot;+&quot;</tt> prototype is a special alternative to <tt>&quot;$&quot;</tt> that acts like <tt>&quot;\[@%]&quot;</tt> when given a literal array or hash variable, but will otherwise force scalar context on the argument. See &#8220;Prototypes&#8221; in perlsub. </p>
<p> <i></i>&quot;package&quot;<i> block syntax</i> </p>
<p> A package declaration can now contain a code block, in which case the declaration is in scope inside that block only. So <tt>&quot;package Foo { ... }&quot;</tt> is precisely equivalent to <tt>&quot;{ package Foo; ... }&quot;</tt>. It also works with a version number in the declaration, as in <tt>&quot;package Foo 1.2 { ... }&quot;</tt>, which is its most attractive feature. See perlfunc. </p>
<p> <i>Statement labels can appear in more places</i> </p>
<p> Statement labels can now occur before any type of statement or declaration, such as <tt>&quot;package&quot;</tt>. </p>
<p> <i>Stacked labels</i> </p>
<p> Multiple statement labels can now appear before a single statement. </p>
<p> <i>Uppercase X/B allowed in hexadecimal/binary literals</i> </p>
<p> Literals may now use either upper case <tt>&quot;0X...&quot;</tt> or <tt>&quot;0B...&quot;</tt> prefixes, in addition to the already supported <tt>&quot;0x...&quot;</tt> and <tt>&quot;0b...&quot;</tt> syntax [perl #76296]. </p>
<p> C, Ruby, Python, and <font SIZE="-1">PHP</font> already support this syntax, and it makes Perl more internally consistent: a round-trip with <tt>&quot;eval sprintf &quot;%#X&quot;, 0x10&quot;</tt> now returns <tt>16</tt>, just like <tt>&quot;eval sprintf &quot;%#x&quot;, 0x10&quot;</tt>. </p>
<p> <i>Overridable tie functions</i> </p>
<p> <tt>&quot;tie&quot;</tt>, <tt>&quot;tied&quot;</tt> and <tt>&quot;untie&quot;</tt> can now be overridden [perl #75902].</p>
<h3>Exception Handling</h3>
<p> To make them more reliable and consistent, several changes have been made to how <tt>&quot;die&quot;</tt>, <tt>&quot;warn&quot;</tt>, and <tt>$@</tt> behave.</p>
<dl>
<dt>&bull;</p>
<dd> When an exception is thrown inside an <tt>&quot;eval&quot;</tt>, the exception is no longer at risk of being clobbered by destructor code running during unwinding. Previously, the exception was written into <tt>$@</tt> early in the throwing process, and would be overwritten if <tt>&quot;eval&quot;</tt> was used internally in the destructor for an object that had to be freed while exiting from the outer <tt>&quot;eval&quot;</tt>. Now the exception is written into <tt>$@</tt> last thing before exiting the outer <tt>&quot;eval&quot;</tt>, so the code running immediately thereafter can rely on the value in <tt>$@</tt> correctly corresponding to that <tt>&quot;eval&quot;</tt>. (<tt>$@</tt> is still also set before exiting the <tt>&quot;eval&quot;</tt>, for the sake of destructors that rely on this.) </p>
<p> Likewise, a <tt>&quot;local $@&quot;</tt> inside an <tt>&quot;eval&quot;</tt> no longer clobbers any exception thrown in its scope. Previously, the restoration of <tt>$@</tt> upon unwinding would overwrite any exception being thrown. Now the exception gets to the <tt>&quot;eval&quot;</tt> anyway. So <tt>&quot;local $@&quot;</tt> is safe before a <tt>&quot;die&quot;</tt>. </p>
<p> Exceptions thrown from object destructors no longer modify the <tt>$@</tt> of the surrounding context. (If the surrounding context was exception unwinding, this used to be another way to clobber the exception being thrown.) Previously such an exception was sometimes emitted as a warning, and then either was string-appended to the surrounding <tt>$@</tt> or completely replaced the surrounding <tt>$@</tt>, depending on whether that exception and the surrounding <tt>$@</tt> were strings or objects. Now, an exception in this situation is always emitted as a warning, leaving the surrounding <tt>$@</tt> untouched. In addition to object destructors, this also affects any function call run by <font SIZE="-1">XS</font> code using the <tt>&quot;G_KEEPERR&quot;</tt> flag.</p>
<dt>&bull;</p>
<dd> Warnings for <tt>&quot;warn&quot;</tt> can now be objects in the same way as exceptions for <tt>&quot;die&quot;</tt>. If an object-based warning gets the default handling of writing to standard error, it is stringified as before with the filename and line number appended. But a <tt>$SIG{__WARN__}</tt> handler now receives an object-based warning as an object, where previously it was passed the result of stringifying the object.</dl>
<h3>Other Enhancements</h3>
<p> <i>Assignment to </i>$0<i> sets the legacy process name with </i>prctl()<i> on Linux</i> </p>
<p> On Linux the legacy process name is now set with <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2), in addition to altering the <font SIZE="-1">POSIX</font> name via <tt>&quot;argv[0]&quot;</tt>, as Perl has done since version 4.000. Now system utilities that read the legacy process name such as <i>ps</i>, <i>top</i>, and <i>killall</i> recognize the name you set when assigning to <tt>$0</tt>. The string you supply is truncated at 16 bytes; this limitation is imposed by Linux. </p>
<p> <i></i>srand()<i> now returns the seed</i> </p>
<p> This allows programs that need to have repeatable results not to have to come up with their own seed-generating mechanism. Instead, they can use <code>srand()</code> and stash the return value for future use. One example is a test program with too many combinations to test comprehensively in the time available for each run. It can test a random subset each time and, should there be a failure, log the seed used for that run so this can later be used to produce the same results. </p>
<p> <i>printf-like functions understand post-1980 size modifiers</i> </p>
<p> Perl&#8217;s printf and sprintf operators, and Perl&#8217;s internal printf replacement function, now understand the C90 size modifiers &#8220;hh&#8221; (<tt>&quot;char&quot;</tt>), &#8220;z&#8221; (<tt>&quot;size_t&quot;</tt>), and &#8220;t&#8221; (<tt>&quot;ptrdiff_t&quot;</tt>). Also, when compiled with a C99 compiler, Perl now understands the size modifier &#8220;j&#8221; (<tt>&quot;intmax_t&quot;</tt>) (but this is not portable). </p>
<p> So, for example, on any modern machine, <tt>&quot;sprintf(&quot;%hhd&quot;, 257)&quot;</tt> returns &#8220;1&#8221;. </p>
<p> <i>New global variable </i>&quot;${^GLOBAL_PHASE}&quot;<i></i> </p>
<p> A new global variable, <tt>&quot;${^GLOBAL_PHASE}&quot;</tt>, has been added to allow introspection of the current phase of the Perl interpreter. It&#8217;s explained in detail in &#8220;${^GLOBAL_PHASE}&#8221; in perlvar and in &#8220;<font SIZE="-1">BEGIN, UNITCHECK, CHECK, INIT</font> and <font SIZE="-1">END&#8221;</font> in perlmod. </p>
<p> <i></i>&quot;-d:-foo&quot;<i> calls </i>&quot;Devel::foo::unimport&quot;<i></i> </p>
<p> The syntax <code>-d:foo</code> was extended in 5.6.1 to make <code>-d:foo=bar</code> equivalent to <code>-MDevel::foo=bar</code>, which expands internally to <tt>&quot;use Devel::foo 'bar'&quot;</tt>. Perl now allows prefixing the module name with <code>&#8211;</code>, with the same semantics as <code>-M</code>; that is:</p>
<dl>
<dt>&quot;-d:-foo&quot;</p>
<dd> Equivalent to <code>-M-Devel::foo</code>: expands to <tt>&quot;no Devel::foo&quot;</tt> and calls <tt>&quot;Devel::foo-&gt;unimport()&quot;</tt> if that method exists.</p>
<dt>&quot;-d:-foo=bar&quot;</p>
<dd> Equivalent to <code>-M-Devel::foo=bar</code>: expands to <tt>&quot;no Devel::foo 'bar'&quot;</tt>, and calls <tt>&quot;Devel::foo-&gt;unimport(&quot;bar&quot;)&quot;</tt> if that method exists.</dl>
<p> This is particularly useful for suppressing the default actions of a <tt>&quot;Devel::*&quot;</tt> module&#8217;s <tt>&quot;import&quot;</tt> method whilst still loading it for debugging. </p>
<p> <i>Filehandle method calls load IO::File on demand</i> </p>
<p> When a method call on a filehandle would die because the method cannot be resolved and IO::File has not been loaded, Perl now loads IO::File via <tt>&quot;require&quot;</tt> and attempts method resolution again: </p>
<p>open my $fh, &#8220;&gt;&#8221;, $file;<br />
$fh-&gt;binmode(&#8220;:raw&#8221;);<br />
#loads IO::File and succeeds</p>
<p> This also works for globs like <tt>&quot;STDOUT&quot;</tt>, <tt>&quot;STDERR&quot;</tt>, and <tt>&quot;STDIN&quot;</tt>: </p>
<p>STDOUT-&gt;autoflush(1);</p>
<p> Because this on-demand load happens only if method resolution fails, the legacy approach of manually loading an IO::File parent class for partial method support still works as expected: </p>
<p>use IO::Handle;<br />
open my $fh, &#8220;&gt;&#8221;, $file;<br />
$fh-&gt;autoflush(1);<br />
#IO::File not loaded</p>
<p> <i>Improved IPv6 support</i> </p>
<p> The <tt>&quot;Socket&quot;</tt> module provides new affordances for IPv6, including implementations of the <tt>&quot;Socket::getaddrinfo()&quot;</tt> and <tt>&quot;Socket::getnameinfo()&quot;</tt> functions, along with related constants and a handful of new functions. See Socket. </p>
<p> <i>DTrace probes now include package name</i> </p>
<p> The <tt>&quot;DTrace&quot;</tt> probes now include an additional argument, <tt>&quot;arg3&quot;</tt>, which contains the package the subroutine being entered or left was compiled in. </p>
<p> For example, using the following DTrace script: </p>
<p>perl$target:: : sub &#8211; entry<br />
{<br />
    printf(&#8220;%s::%s
&#8221;, copyinstr(arg0), copyinstr(arg3));<br />
}</p>
<p> and then running: </p>
<pre>
  $ perl -e 'sub test { }; test'
</pre>
<p> <tt>&quot;DTrace&quot;</tt> will print: </p>
<pre>
  main::test
</pre>
<h3>New C APIs</h3>
<p> See &#8220;Internal Changes&#8221;.</p>
<h2>Security</h2>
<h3>User-defined regular expression properties</h3>
<p> &#8220;User-Defined Character Properties&#8221; in perlunicode documented that you can create custom properties by defining subroutines whose names begin with &#8220;In&#8221; or &#8220;Is&#8221;. However, Perl did not actually enforce that naming restriction, so <tt>&quot;\p{foo::bar}&quot;</tt> could call <code>foo::bar()</code> if it existed. The documented convention is now enforced. </p>
<p> Also, Perl no longer allows tainted regular expressions to invoke a user-defined property. It simply dies instead [perl #82616].</p>
<h2>Incompatible Changes</h2>
<p> Perl 5.14.0 is not binary-compatible with any previous stable release. </p>
<p> In addition to the sections that follow, see &#8220;C <font SIZE="-1">API</font> Changes&#8221;.</p>
<h3>Regular Expressions and String Escapes</h3>
<p> <i>Inverted bracketed character classes and multi-character folds</i> </p>
<p> Some characters match a sequence of two or three characters in <tt>&quot;/i&quot;</tt> regular expression matching under Unicode rules. One example is <tt>&quot;LATIN SMALL LETTER SHARP S&quot;</tt> which matches the sequence <tt>&quot;ss&quot;</tt>. </p>
<p>&#8216;ss&#8217; = ~ /\A[\N{LATIN SMALL LETTER SHARP S}]\z / i #Matches</p>
<p> This, however, can lead to very counter-intuitive results, especially when inverted. Because of this, Perl 5.14 does not use multi-character <tt>&quot;/i&quot;</tt> matching in inverted character classes. </p>
<p>&#8216;ss&#8217; = ~ /\A[^\N{<br />
           LATIN SMALL LETTER SHARP S}] +\z / i #<br />
    ? ? ?</p>
<p> This should match any sequences of characters that aren&#8217;t the <tt>&quot;SHARP S&quot;</tt> nor what <tt>&quot;SHARP S&quot;</tt> matches under <tt>&quot;/i&quot;</tt>. <tt>&quot;s&quot;</tt> isn&#8217;t <tt>&quot;SHARP S&quot;</tt>, but Unicode says that <tt>&quot;ss&quot;</tt> is what <tt>&quot;SHARP S&quot;</tt> matches under <tt>&quot;/i&quot;</tt>. So which one &#8220;wins&#8221;? Do you fail the match because the string has <tt>&quot;ss&quot;</tt> or accept it because it has an <tt>&quot;s&quot;</tt> followed by another <tt>&quot;s&quot;</tt>? </p>
<p> Earlier releases of Perl did allow this multi-character matching, but due to bugs, it mostly did not work. </p>
<p> <i>\400-\777</i> </p>
<p> In certain circumstances, <tt>&quot;\400&quot;</tt>&#8211;<tt>&quot;\777&quot;</tt> in regexes have behaved differently than they behave in all other doublequote-like contexts. Since 5.10.1, Perl has issued a deprecation warning when this happens. Now, these literals behave the same in all doublequote-like contexts, namely to be equivalent to <tt>&quot;
