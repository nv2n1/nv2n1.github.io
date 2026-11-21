---

title: "perl5140delta(1)"
name: "perl5140delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5140delta/"
description: "perl5140delta – what is new for perl v5.14.0"
---

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
<dt>&bull;</dt>
<dd> <tt>&quot;\N{</tt>NAME<tt>}&quot;</tt> and <tt>&quot;charnames::vianame&quot;</tt> now know about the abbreviated character names listed by Unicode, such as <font SIZE="-1">NBSP, SHY, LRO, ZWJ,</font> etc.; all customary abbreviations for the C0 and C1 control characters (such as <font SIZE="-1">ACK, BEL, CAN,</font> etc.); and a few new variants of some C1 full names that are in common usage.</dd>
<dt>&bull;</dt>
<dd> Unicode has several <i>named character sequences</i>, in which particular sequences of code points are given names. <tt>&quot;\N{</tt>NAME<tt>}&quot;</tt> now recognizes these.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;\N{</tt>NAME<tt>}&quot;</tt>, <tt>&quot;charnames::vianame&quot;</tt>, and <tt>&quot;charnames::viacode&quot;</tt> now know about every character in Unicode. In earlier releases of Perl, they didn&#8217;t know about the Hangul syllables nor several <font SIZE="-1">CJK</font> (Chinese/Japanese/Korean) characters.</dd>
<dt>&bull;</dt>
<dd> It is now possible to override Perl&#8217;s abbreviations with your own custom aliases.</dd>
<dt>&bull;</dt>
<dd> You can now create a custom alias of the ordinal of a character, known by <tt>&quot;\N{</tt>NAME<tt>}&quot;</tt>, <tt>&quot;charnames::vianame()&quot;</tt>, and <tt>&quot;charnames::viacode()&quot;</tt>. Previously, aliases had to be to official Unicode character names. This made it impossible to create an alias for unnamed code points, such as those reserved for private use.</dd>
<dt>&bull;</dt>
<dd> The new function <code>charnames::string_vianame()</code> is a run-time version of <tt>&quot;\N{</tt>NAME<tt>}}&quot;</tt>, returning the string of characters whose Unicode name is its parameter. It can handle Unicode named character sequences, whereas the pre-existing <code>charnames::vianame()</code> cannot, as the latter returns a single code point.</dd></dl>
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
<dt>&bull;</dt>
<dd> The <tt>&quot;/l&quot;</tt> modifier says to compile the regular expression as if it were in the scope of <tt>&quot;use locale&quot;</tt>, even if it is not.</dd>
<dt>&bull;</dt>
<dd> The <tt>&quot;/u&quot;</tt> modifier says to compile the regular expression as if it were in the scope of a <tt>&quot;use feature 'unicode_strings'&quot;</tt> pragma.</dd>
<dt>&bull;</dt>
<dd> The <tt>&quot;/d&quot;</tt> (default) modifier is used to override any <tt>&quot;use locale&quot;</tt> and <tt>&quot;use feature 'unicode_strings'&quot;</tt> pragmas in effect at the time of compiling the regular expression.</dd>
<dt>&bull;</dt>
<dd> The <tt>&quot;/a&quot;</tt> regular expression modifier restricts <tt>&quot;\s&quot;</tt>, <tt>&quot;\d&quot;</tt> and <tt>&quot;\w&quot;</tt> and the <font SIZE="-1">POSIX</font> (<tt>&quot;[[:posix:]]&quot;</tt>) character classes to the <font SIZE="-1">ASCII</font> range. Their complements and <tt>&quot;&quot;</tt> and <tt>&quot;\B&quot;</tt> are correspondingly affected. Otherwise, <tt>&quot;/a&quot;</tt> behaves like the <tt>&quot;/u&quot;</tt> modifier, in that case-insensitive matching uses Unicode semantics. </dd>
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
<dt>&bull;</dt>
<dd> When an exception is thrown inside an <tt>&quot;eval&quot;</tt>, the exception is no longer at risk of being clobbered by destructor code running during unwinding. Previously, the exception was written into <tt>$@</tt> early in the throwing process, and would be overwritten if <tt>&quot;eval&quot;</tt> was used internally in the destructor for an object that had to be freed while exiting from the outer <tt>&quot;eval&quot;</tt>. Now the exception is written into <tt>$@</tt> last thing before exiting the outer <tt>&quot;eval&quot;</tt>, so the code running immediately thereafter can rely on the value in <tt>$@</tt> correctly corresponding to that <tt>&quot;eval&quot;</tt>. (<tt>$@</tt> is still also set before exiting the <tt>&quot;eval&quot;</tt>, for the sake of destructors that rely on this.) </dd>
<p> Likewise, a <tt>&quot;local $@&quot;</tt> inside an <tt>&quot;eval&quot;</tt> no longer clobbers any exception thrown in its scope. Previously, the restoration of <tt>$@</tt> upon unwinding would overwrite any exception being thrown. Now the exception gets to the <tt>&quot;eval&quot;</tt> anyway. So <tt>&quot;local $@&quot;</tt> is safe before a <tt>&quot;die&quot;</tt>. </p>
<p> Exceptions thrown from object destructors no longer modify the <tt>$@</tt> of the surrounding context. (If the surrounding context was exception unwinding, this used to be another way to clobber the exception being thrown.) Previously such an exception was sometimes emitted as a warning, and then either was string-appended to the surrounding <tt>$@</tt> or completely replaced the surrounding <tt>$@</tt>, depending on whether that exception and the surrounding <tt>$@</tt> were strings or objects. Now, an exception in this situation is always emitted as a warning, leaving the surrounding <tt>$@</tt> untouched. In addition to object destructors, this also affects any function call run by <font SIZE="-1">XS</font> code using the <tt>&quot;G_KEEPERR&quot;</tt> flag.</p>
<dt>&bull;</dt>
<dd> Warnings for <tt>&quot;warn&quot;</tt> can now be objects in the same way as exceptions for <tt>&quot;die&quot;</tt>. If an object-based warning gets the default handling of writing to standard error, it is stringified as before with the filename and line number appended. But a <tt>$SIG{__WARN__}</tt> handler now receives an object-based warning as an object, where previously it was passed the result of stringifying the object.</dd></dl>
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
<dt>&quot;-d:-foo&quot;</dt>
<dd> Equivalent to <code>-M-Devel::foo</code>: expands to <tt>&quot;no Devel::foo&quot;</tt> and calls <tt>&quot;Devel::foo-&gt;unimport()&quot;</tt> if that method exists.</dd>
<dt>&quot;-d:-foo=bar&quot;</dt>
<dd> Equivalent to <code>-M-Devel::foo=bar</code>: expands to <tt>&quot;no Devel::foo 'bar'&quot;</tt>, and calls <tt>&quot;Devel::foo-&gt;unimport(&quot;bar&quot;)&quot;</tt> if that method exists.</dd></dl>
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
<p> In certain circumstances, <tt>&quot;\400&quot;</tt>&#8211;<tt>&quot;\777&quot;</tt> in regexes have behaved differently than they behave in all other doublequote-like contexts. Since 5.10.1, Perl has issued a deprecation warning when this happens. Now, these literals behave the same in all doublequote-like contexts, namely to be equivalent to <tt>&quot;</tt>\x{100}&quot;</code>-<code>&quot;\x{1FF}&quot;</code>, with no deprecation warning. </p>
<p> Use of <code>&quot;\400&quot;</code>-<code>&quot;\777&quot;</code> in the command-line option <code>-0</code> retain their conventional meaning. They slurp whole input files; previously, this was documented only for <code>-0777</code>. </p>
<p> Because of various ambiguities, you should use the new <code>&quot;\o{...}&quot;</code> construct to represent characters in octal instead. </p>
<p> <i>Most </i>&quot;\p{}&quot;<i> properties are now immune to case-insensitive matching</i> </p>
<p> For most Unicode properties, it doesn&#8217;t make sense to have them match differently under <code>&quot;/i&quot;</code> case-insensitive matching. Doing so can lead to unexpected results and potential security holes. For example </p>
<pre><code> m/\p{ASCII_Hex_Digit}+/i
</code></pre>
<p> could previously match non-ASCII characters because of the Unicode matching rules (although there were several bugs with this). Now matching under <code>&quot;/i&quot;</code> gives the same results as non-<code>&quot;/i&quot;</code> matching except for those few properties where people have come to expect differences, namely the ones where casing is an integral part of their meaning, such as <code>&quot;m/\p{Uppercase}/i&quot;</code> and <code>&quot;m/\p{Lowercase}/i&quot;</code>, both of which match the same code points as matched by <code>&quot;m/\p{Cased}/i&quot;</code>. Details are in ``Unicode Properties&#8217;&#8216; in perlrecharclass. </p>
<p> User-defined property handlers that need to match differently under <code>&quot;/i&quot;</code> must be changed to read the new boolean parameter passed to them, which is non-zero if case-insensitive matching is in effect and 0 otherwise. See ``User-Defined Character Properties&#8217;&#8216; in perlunicode. </p>
<p> <i>\p{} implies Unicode semantics</i> </p>
<p> Specifying a Unicode property in the pattern indicates that the pattern is meant for matching according to Unicode rules, the way <code>&quot;\N{</code>NAME <code>}&quot;</code> does. </p>
<p> <i>Regular expressions retain their localeness when interpolated</i> </p>
<p> Regular expressions compiled under <code>&quot;use locale&quot;</code> now retain this when interpolated into a new regular expression compiled outside a <code>&quot;use locale&quot;</code>, and vice-versa. </p>
<p> Previously, one regular expression interpolated into another inherited the localeness of the surrounding regex, losing whatever state it originally had. This is considered a bug fix, but may trip up code that has come to rely on the incorrect behaviour. </p>
<p> <i>Stringification of regexes has changed</i> </p>
<p> Default regular expression modifiers are now notated using <code>&quot;(?^...)&quot;</code>. Code relying on the old stringification will fail. This is so that when new modifiers are added, such code won&#8217;t have to keep changing each time this happens, because the stringification will automatically incorporate the new modifiers. </p>
<p> Code that needs to work properly with both old- and new-style regexes can avoid the whole issue by using (for perls since 5.9.5; see re): </p>
<pre><code> use re qw(regexp_pattern);
 my ($pat, $mods) = regexp_pattern($re_ref);
</code></pre>
<p> If the actual stringification is important or older Perls need to be supported, you can use something like the following: </p>
<pre><code>    # Accept both old and new-style stringification
    my $modifiers = (qr/foobar/ =~ /\Q(?^/) ? &quot;^&quot; : &quot;-xism&quot;;
</code></pre>
<p> And then use <code>$modifiers</code> instead of <code>&quot;-xism&quot;</code>. </p>
<p> <i>Run-time code blocks in regular expressions inherit pragmata</i> </p>
<p> Code blocks in regular expressions (<code>&quot;(?{...})&quot;</code> and <code>&quot;(??{...})&quot;</code>) previously did not inherit pragmata (strict, warnings, etc.) if the regular expression was compiled at run time as happens in cases like these two: </p>
<pre><code>  use re &quot;eval&quot;;
  $foo =~ $bar; # when $bar contains (?{...})
  $foo =~ /$bar(?{ $finished = 1 })/;
</code></pre>
<p> This bug has now been fixed, but code that relied on the buggy behaviour may need to be fixed to account for the correct behaviour.  </p>
<h3>Stashes and Package Variables</h3>
<p> <i>Localised tied hashes and arrays are no longed tied</i> </p>
<p> In the following: </p>
<pre><code>    tie @a, ...;
    {
            local @a;
            # here, @a is a now a new, untied array
    }
    # here, @a refers again to the old, tied array
</code></pre>
<p> Earlier versions of Perl incorrectly tied the new local array. This has now been fixed. This fix could however potentially cause a change in behaviour of some code. </p>
<p> <i>Stashes are now always defined</i> </p>
<p> <code>&quot;defined %Foo::&quot;</code> now always returns true, even when no symbols have yet been defined in that package. </p>
<p> This is a side-effect of removing a special-case kludge in the tokeniser, added for 5.10.0, to hide side-effects of changes to the internal storage of hashes. The fix drastically reduces hashes&#8217; memory overhead. </p>
<p> Calling defined on a stash has been deprecated since 5.6.0, warned on lexicals since 5.6.0, and warned for stashes and other package variables since 5.12.0. <code>&quot;defined %hash&quot;</code> has always exposed an implementation detail: emptying a hash by deleting all entries from it does not make <code>&quot;defined %hash&quot;</code> false. Hence <code>&quot;defined %hash&quot;</code> is not valid code to determine whether an arbitrary hash is empty. Instead, use the behaviour of an empty <code>%hash</code> always returning false in scalar context. </p>
<p> <i>Clearing stashes</i> </p>
<p> Stash list assignment <code>&quot;%foo:: = ()&quot;</code> used to make the stash temporarily anonymous while it was being emptied. Consequently, any of its subroutines referenced elsewhere would become anonymous, showing up as ``(unknown)&#8216;&#8216; in <code>&quot;caller&quot;</code>. They now retain their package names such that <code>&quot;caller&quot;</code> returns the original sub name if there is still a reference to its typeglob and ``foo::__ANON__&#8216;&#8216; otherwise [perl #79208]. </p>
<p> <i>Dereferencing typeglobs</i> </p>
<p> If you assign a typeglob to a scalar variable: </p>
<pre><code>    $glob = *foo;
</code></pre>
<p> the glob that is copied to <code>$glob</code> is marked with a special flag indicating that the glob is just a copy. This allows subsequent assignments to <code>$glob</code> to overwrite the glob. The original glob, however, is immutable. </p>
<p> Some Perl operators did not distinguish between these two types of globs. This would result in strange behaviour in edge cases: <code>&quot;untie $scalar&quot;</code> would not untie the scalar if the last thing assigned to it was a glob (because it treated it as <code>&quot;untie *$scalar&quot;</code>, which unties a handle). Assignment to a glob slot (such as <code>&quot;*$glob = \@some_array&quot;</code>) would simply assign <code>&quot;\@some_array&quot;</code> to <code>$glob</code>. </p>
<p> To fix this, the <code>&quot;*{}&quot;</code> operator (including its <code>*foo</code> and <code>*$foo</code> forms) has been modified to make a new immutable glob if its operand is a glob copy. This allows operators that make a distinction between globs and scalars to be modified to treat only immutable globs as globs. (<code>&quot;tie&quot;</code>, <code>&quot;tied&quot;</code> and <code>&quot;untie&quot;</code> have been left as they are for compatibility&#8217;s sake, but will warn. See ``Deprecations&#8217;&#8216;.) </p>
<p> This causes an incompatible change in code that assigns a glob to the return value of <code>&quot;*{}&quot;</code> when that operator was passed a glob copy. Take the following code, for instance: </p>
<pre><code>    $glob = *foo;
    *$glob = *bar;
</code></pre>
<p> The <code>*$glob</code> on the second line returns a new immutable glob. That new glob is made an alias to <code>*bar</code>. Then it is discarded. So the second assignment has no effect. </p>
<p> See &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77810">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77810</a>&gt; for more detail. </p>
<p> <i>Magic variables outside the main package</i> </p>
<p> In previous versions of Perl, magic variables like <code>$!</code>, <code>%SIG</code>, etc. would ``leak&#8217;&#8216; into other packages. So <code>%foo::SIG</code> could be used to access signals, <code>&quot;${&quot;foo::!&quot;}&quot;</code> (with strict mode off) to access C&#8217;s <code>&quot;errno&quot;</code>, etc. </p>
<p> This was a bug, or an ``unintentional&#8217;&#8216; feature, which caused various ill effects, such as signal handlers being wiped when modules were loaded, etc. </p>
<p> This has been fixed (or the feature has been removed, depending on how you see it). </p>
<p> <i>local($_) strips all magic from </i>$_<i></i> </p>
<p> <code>local()</code> on scalar variables gives them a new value but keeps all their magic intact. This has proven problematic for the default scalar variable <code>$_</code>, where perlsub recommends that any subroutine that assigns to <code>$_</code> should first localize it. This would throw an exception if <code>$_</code> is aliased to a read-only variable, and could in general have various unintentional side-effects. </p>
<p> Therefore, as an exception to the general rule, local($_) will not only assign a new value to <code>$_</code>, but also remove all existing magic from it as well. </p>
<p> <i>Parsing of package and variable names</i> </p>
<p> Parsing the names of packages and package variables has changed: multiple adjacent pairs of colons, as in <code>&quot;foo::::bar&quot;</code>, are now all treated as package separators. </p>
<p> Regardless of this change, the exact parsing of package separators has never been guaranteed and is subject to change in future Perl versions.  </p>
<h3>Changes to Syntax or to Perl Operators</h3>
<p> <i></i>&quot;given&quot;<i> return values</i> </p>
<p> <code>&quot;given&quot;</code> blocks now return the last evaluated expression, or an empty list if the block was exited by <code>&quot;break&quot;</code>. Thus you can now write: </p>
<pre><code>    my $type = do {
     given ($num) {
      break when undef;
      &quot;integer&quot; when /^[+-]?[0-9]+$/;
      &quot;float&quot; when /^[+-]?[0-9]+(?:\.[0-9]+)?$/;
      &quot;unknown&quot;;
     }
    };
</code></pre>
<p> See ``Return value&#8217;&#8216; in perlsyn for details. </p>
<p> <i>Change in parsing of certain prototypes</i> </p>
<p> Functions declared with the following prototypes now behave correctly as unary functions: </p>
<pre><code>  *
  \$ \% \@ \* \&amp;
  \[...]
  ;$ ;*
  ;\$ ;\% etc.
  ;\[...]
</code></pre>
<p> Due to this bug fix [perl #75904], functions using the <code>&quot;(*)&quot;</code>, <code>&quot;(;$)&quot;</code> and <code>&quot;(;*)&quot;</code> prototypes are parsed with higher precedence than before. So in the following example: </p>
<pre><code>  sub foo(;$);
  foo $a &lt; $b;
</code></pre>
<p> the second line is now parsed correctly as <code>&quot;foo($a) &lt; $b&quot;</code>, rather than <code>&quot;foo($a &lt; $b)&quot;</code>. This happens when one of these operators is used in an unparenthesised argument: </p>
<pre><code>  &lt; &gt; &lt;= &gt;= lt gt le ge
  == != &lt;=&gt; eq ne cmp ~~
  &amp;
  | ^
  &amp;&amp;
  || //
  .. ...
  ?:
  = += -= *= etc.
  , =&gt;
</code></pre>
<p> <i>Smart-matching against array slices</i> </p>
<p> Previously, the following code resulted in a successful match: </p>
<pre><code>    my @a = qw(a y0 z);
    my @b = qw(a x0 z);
    @a[0 .. $#b] ~~ @b;
</code></pre>
<p> This odd behaviour has now been fixed [perl #77468]. </p>
<p> <i>Negation treats strings differently from before</i> </p>
<p> The unary negation operator, <code>&quot;-&quot;</code>, now treats strings that look like numbers as numbers [perl #57706]. </p>
<p> <i>Negative zero</i> </p>
<p> Negative zero (-0.0), when converted to a string, now becomes ``0&#8217;&#8216; on all platforms. It used to become ``-0&#8217;&#8216; on some, but ``0&#8217;&#8216; on others. </p>
<p> If you still need to determine whether a zero is negative, use <code>&quot;sprintf(&quot;%g&quot;, $zero) =~ /^-/&quot;</code> or the Data::Float module on <font SIZE="-1">CPAN.</font> </p>
<p> <i></i>&quot;:=&quot;<i> is now a syntax error</i> </p>
<p> Previously <code>&quot;my $pi := 4&quot;</code> was exactly equivalent to <code>&quot;my $pi : = 4&quot;</code>, with the <code>&quot;:&quot;</code> being treated as the start of an attribute list, ending before the <code>&quot;=&quot;</code>. The use of <code>&quot;:=&quot;</code> to mean <code>&quot;: =&quot;</code> was deprecated in 5.12.0, and is now a syntax error. This allows future use of <code>&quot;:=&quot;</code> as a new token. </p>
<p> Outside the core&#8217;s tests for it, we find no Perl 5 code on <font SIZE="-1">CPAN</font> using this construction, so we believe that this change will have little impact on real-world codebases. </p>
<p> If it is absolutely necessary to have empty attribute lists (for example, because of a code generator), simply avoid the error by adding a space before the <code>&quot;=&quot;</code>. </p>
<p> <i>Change in the parsing of identifiers</i> </p>
<p> Characters outside the Unicode ``XIDStart&#8217;&#8216; set are no longer allowed at the beginning of an identifier. This means that certain accents and marks that normally follow an alphabetic character may no longer be the first character of an identifier.  </p>
<h3>Threads and Processes</h3>
<p> <i>Directory handles not copied to threads</i> </p>
<p> On systems other than Windows that do not have a <code>&quot;fchdir&quot;</code> function, newly-created threads no longer inherit directory handles from their parent threads. Such programs would usually have crashed anyway [perl #75154]. </p>
<p> <i></i>&quot;close&quot;<i> on shared pipes</i> </p>
<p> To avoid deadlocks, the <code>&quot;close&quot;</code> function no longer waits for the child process to exit if the underlying file descriptor is still in use by another thread. It returns true in such cases. </p>
<p> <i></i>fork()<i> emulation will not wait for signalled children</i> </p>
<p> On Windows parent processes would not terminate until all forked children had terminated first. However, <code>&quot;kill(&quot;KILL&quot;, ...)&quot;</code> is inherently unstable on pseudo-processes, and <code>&quot;kill(&quot;TERM&quot;, ...)&quot;</code> might not get delivered if the child is blocked in a system call. </p>
<p> To avoid the deadlock and still provide a safe mechanism to terminate the hosting process, Perl now no longer waits for children that have been sent a <font SIZE="-1">SIGTERM</font> signal. It is up to the parent process to <code>waitpid()</code> for these children if child-cleanup processing must be allowed to finish. However, it is also then the responsibility of the parent to avoid the deadlock by making sure the child process can&#8217;t be blocked on I/O. </p>
<p> See perlfork for more information about the <code>fork()</code> emulation on Windows.  </p>
<h3>Configuration</h3>
<p> <i>Naming fixes in Policy_sh.SH may invalidate Policy.sh</i> </p>
<p> Several long-standing typos and naming confusions in <i>Policy_sh.SH</i> have been fixed, standardizing on the variable names used in <i>config.sh</i>. </p>
<p> This will change the behaviour of <i>Policy.sh</i> if you happen to have been accidentally relying on its incorrect behaviour. </p>
<p> <i>Perl source code is read in text mode on Windows</i> </p>
<p> Perl scripts used to be read in binary mode on Windows for the benefit of the ByteLoader module (which is no longer part of core Perl). This had the side-effect of breaking various operations on the <code>&quot;DATA&quot;</code> filehandle, including <code>seek()</code>/<code>tell()</code>, and even simply reading from <code>&quot;DATA&quot;</code> after filehandles have been flushed by a call to <code>system()</code>, backticks, <code>fork()</code> etc. </p>
<p> The default build options for Windows have been changed to read Perl source code on Windows in text mode now. ByteLoader will (hopefully) be updated on <font SIZE="-1">CPAN</font> to automatically handle this situation [perl #28106].  </p>
<h2>Deprecations</h2>
<p> See also ``Deprecated C APIs&#8217;&#8216;.  </p>
<h3>Omitting a space between a regular expression and subsequent word</h3>
<p> Omitting the space between a regular expression operator or its modifiers and the following word is deprecated. For example, <code>&quot;m/foo/sand $bar&quot;</code> is for now still parsed as <code>&quot;m/foo/s and $bar&quot;</code>, but will now issue a warning.  </p>
<h3>\cX</h3>
<p> The backslash-c construct was designed as a way of specifying non-printable characters, but there were no restrictions (on <font SIZE="-1">ASCII</font> platforms) on what the character following the <code>&quot;c&quot;</code> could be. Now, a deprecation warning is raised if that character isn&#8217;t an <font SIZE="-1">ASCII</font> character. Also, a deprecation warning is raised for <code>&quot;\c{&quot;</code> (which is the same as simply saying <code>&quot;;&quot;</code>).  </p>
<h3>\b{ and \B{</h3>
<p> In regular expressions, a literal <code>&quot;{&quot;</code> immediately following a <code>&quot;\b&quot;</code> (not in a bracketed character class) or a <code>&quot;\B{&quot;</code> is now deprecated to allow for its future use by Perl itself.  </p>
<h3>Perl 4-era .pl libraries</h3>
<p> Perl bundles a handful of library files that predate Perl 5. This bundling is now deprecated for most of these files, which are now available from <font SIZE="-1">CPAN.</font> The affected files now warn when run, if they were installed as part of the core. </p>
<p> This is a mandatory warning, not obeying <code>-X</code> or lexical warning bits. The warning is modelled on that supplied by <i>deprecate.pm</i> for deprecated-in-core <i>.pm</i> libraries. It points to the specific <font SIZE="-1">CPAN</font> distribution that contains the <i>.pl</i> libraries. The <font SIZE="-1">CPAN</font> versions, of course, do not generate the warning.  </p>
<h3>List assignment to $[</h3>
<p> Assignment to <code>$[</code> was deprecated and started to give warnings in Perl version 5.12.0. This version of Perl (5.14) now also emits a warning when assigning to <code>$[</code> in list context. This fixes an oversight in 5.12.0.  </p>
<h3>Use of qw(...) as parentheses</h3>
<p> Historically the parser fooled itself into thinking that <code>&quot;qw(...)&quot;</code> literals were always enclosed in parentheses, and as a result you could sometimes omit parentheses around them: </p>
<pre><code>    for $x qw(a b c) { ... }
</code></pre>
<p> The parser no longer lies to itself in this way. Wrap the list literal in parentheses like this: </p>
<pre><code>    for $x (qw(a b c)) { ... }
</code></pre>
<p> This is being deprecated because the parentheses in <code>&quot;for $i (1,2,3) { ... }&quot;</code> are not part of expression syntax. They are part of the statement syntax, with the <code>&quot;for&quot;</code> statement wanting literal parentheses. The synthetic parentheses that a <code>&quot;qw&quot;</code> expression acquired were only intended to be treated as part of expression syntax. </p>
<p> Note that this does not change the behaviour of cases like: </p>
<pre><code>    use POSIX qw(setlocale localeconv);
    our @EXPORT = qw(foo bar baz);
</code></pre>
<p> where parentheses were never required around the expression.  </p>
<h3>\N{BELL}</h3>
<p> This is because Unicode is using that name for a different character. See ``Unicode Version 6.0 is now supported (mostly)&#8216;&#8216; for more explanation.  </p>
<h3>?PATTERN?</h3>
<p> <code>&quot;?PATTERN?&quot;</code> (without the initial <code>&quot;m&quot;</code>) has been deprecated and now produces a warning. This is to allow future use of <code>&quot;?&quot;</code> in new operators. The match-once functionality is still available as <code>&quot;m?PATTERN?&quot;</code>.  </p>
<h3>Tie functions on scalars holding typeglobs</h3>
<p> Calling a tie function (<code>&quot;tie&quot;</code>, <code>&quot;tied&quot;</code>, <code>&quot;untie&quot;</code>) with a scalar argument acts on a filehandle if the scalar happens to hold a typeglob. </p>
<p> This is a long-standing bug that will be removed in Perl 5.16, as there is currently no way to tie the scalar itself when it holds a typeglob, and no way to untie a scalar that has had a typeglob assigned to it. </p>
<p> Now there is a deprecation warning whenever a tie function is used on a handle without an explicit <code>&quot;*&quot;</code>.  </p>
<h3>User-defined case-mapping</h3>
<p> This feature is being deprecated due to its many issues, as documented in ``User-Defined Case Mappings (for serious hackers only)&#8216;&#8216; in perlunicode. This feature will be removed in Perl 5.16. Instead use the <font SIZE="-1">CPAN</font> module Unicode::Casing, which provides improved functionality.  </p>
<h3>Deprecated modules</h3>
<p> The following module will be removed from the core distribution in a future release, and should be installed from <font SIZE="-1">CPAN</font> instead. Distributions on <font SIZE="-1">CPAN</font> that require this should add it to their prerequisites. The core version of these module now issues a deprecation warning. </p>
<p> If you ship a packaged version of Perl, either alone or as part of a larger system, then you should carefully consider the repercussions of core module deprecations. You may want to consider shipping your default build of Perl with a package for the deprecated module that installs into <code>&quot;vendor&quot;</code> or <code>&quot;site&quot;</code> Perl library directories. This will inhibit the deprecation warnings. </p>
<p> Alternatively, you may want to consider patching <i>lib/deprecate.pm</i> to provide deprecation warnings specific to your packaging system or distribution of Perl, consistent with how your packaging system or distribution manages a staged transition from a release where the installation of a single package provides the given functionality, to a later release where the system administrator needs to know to install multiple packages to get that same functionality. </p>
<p> You can silence these deprecation warnings by installing the module in question from <font SIZE="-1">CPAN.</font> To install the latest version of it by role rather than by name, just install <code>&quot;Task::Deprecations::5_14&quot;</code>. </p>
<dl>
<dt>Devel::DProf</dt>
<dd> <p> We strongly recommend that you install and use Devel::NYTProf instead of Devel::DProf, as Devel::NYTProf offers significantly improved profiling and reporting. </p>
 </dd></dl>
<h2>Performance Enhancements</h2>
<h3>Safe signals optimisation</h3>
<p> Signal dispatch has been moved from the runloop into control ops. This should give a few percent speed increase, and eliminates nearly all the speed penalty caused by the introduction of ``safe signals&#8217;&#8216; in 5.8.0. Signals should still be dispatched within the same statement as they were previously. If this does <i>not</i> happen, or if you find it possible to create uninterruptible loops, this is a bug, and reports are encouraged of how to recreate such issues.  </p>
<code></code><code></code><h3>Optimisation of shift() and pop() calls without arguments</h3>
<p> Two fewer OPs are used for <code>shift()</code> and <code>pop()</code> calls with no argument (with implicit <code>@_</code>). This change makes <code>shift()</code> 5% faster than <code>&quot;shift @_&quot;</code> on non-threaded perls, and 25% faster on threaded ones.  </p>
<h3>Optimisation of regexp engine string comparison work</h3>
<p> The <code>&quot;foldEQ_utf8&quot;</code> <font SIZE="-1">API</font> function for case-insensitive comparison of strings (which is used heavily by the regexp engine) was substantially refactored and optimised --- and its documentation much improved as a free bonus.  </p>
<h3>Regular expression compilation speed-up</h3>
<p> Compiling regular expressions has been made faster when upgrading the regex to utf8 is necessary but this isn&#8217;t known when the compilation begins.  </p>
<h3>String appending is 100 times faster</h3>
<p> When doing a lot of string appending, perls built to use the system&#8217;s <code>&quot;malloc&quot;</code> could end up allocating a lot more memory than needed in a inefficient way. </p>
<p> <code>&quot;sv_grow&quot;</code>, the function used to allocate more memory if necessary when appending to a string, has been taught to round up the memory it requests to a certain geometric progression, making it much faster on certain platforms and configurations. On Win32, it&#8217;s now about 100 times faster.  </p>
<h3>Eliminate PL_* accessor functions under ithreads</h3>
<p> When <code>&quot;MULTIPLICITY&quot;</code> was first developed, and interpreter state moved into an interpreter struct, thread- and interpreter-local <code>&quot;PL_*&quot;</code> variables were defined as macros that called accessor functions (returning the address of the value) outside the Perl core. The intent was to allow members within the interpreter struct to change size without breaking binary compatibility, so that bug fixes could be merged to a maintenance branch that necessitated such a size change. This mechanism was redundant and penalised well-behaved code. It has been removed.  </p>
<h3>Freeing weak references</h3>
<p> When there are many weak references to an object, freeing that object can under some circumstances take O(<i>N*N</i>) time to free, where <i>N</i> is the number of references. The circumstances in which this can happen have been reduced [perl #75254]  </p>
<h3>Lexical array and hash assignments</h3>
<p> An earlier optimisation to speed up <code>&quot;my @array = ...&quot;</code> and <code>&quot;my %hash = ...&quot;</code> assignments caused a bug and was disabled in Perl 5.12.0. </p>
<p> Now we have found another way to speed up these assignments [perl #82110].  </p>
<h3>@_ uses less memory</h3>
<p> Previously, <code>@_</code> was allocated for every subroutine at compile time with enough space for four entries. Now this allocation is done on demand when the subroutine is called [perl #72416].  </p>
<font SIZE="-1"></font><font SIZE="-1"></font><h3>Size optimisations to SV and HV structures</h3>
<p> <code>&quot;xhv_fill&quot;</code> has been eliminated from <code>&quot;struct xpvhv&quot;</code>, saving 1 <font SIZE="-1">IV</font> per hash and on some systems will cause <code>&quot;struct xpvhv&quot;</code> to become cache-aligned. To avoid this memory saving causing a slowdown elsewhere, boolean use of <code>&quot;HvFILL&quot;</code> now calls <code>&quot;HvTOTALKEYS&quot;</code> instead (which is equivalent), so while the fill data when actually required are now calculated on demand, cases when this needs to be done should be rare. </p>
<p> The order of structure elements in <font SIZE="-1">SV</font> bodies has changed. Effectively, the <font SIZE="-1">NV</font> slot has swapped location with <font SIZE="-1">STASH</font> and <font SIZE="-1">MAGIC.</font> As all access to <font SIZE="-1">SV</font> members is via macros, this should be completely transparent. This change allows the space saving for PVHVs documented above, and may reduce the memory allocation needed for PVIVs on some architectures. </p>
<p> <code>&quot;XPV&quot;</code>, <code>&quot;XPVIV&quot;</code>, and <code>&quot;XPVNV&quot;</code> now allocate only the parts of the <code>&quot;SV&quot;</code> body they actually use, saving some space. </p>
<p> Scalars containing regular expressions now allocate only the part of the <code>&quot;SV&quot;</code> body they actually use, saving some space.  </p>
<h3>Memory consumption improvements to Exporter</h3>
<p> The <code>@EXPORT_FAIL</code> <font SIZE="-1">AV</font> is no longer created unless needed, hence neither is the typeglob backing it. This saves about 200 bytes for every package that uses Exporter but doesn&#8217;t use this functionality.  </p>
<h3>Memory savings for weak references</h3>
<p> For weak references, the common case of just a single weak reference per referent has been optimised to reduce the storage required. In this case it saves the equivalent of one small Perl array per referent.  </p>
<h3>%+ and %- use less memory</h3>
<p> The bulk of the <code>&quot;Tie::Hash::NamedCapture&quot;</code> module used to be in the Perl core. It has now been moved to an <font SIZE="-1">XS</font> module to reduce overhead for programs that do not use <code>&quot;%+&quot;</code> or <code>&quot;%-&quot;</code>.  </p>
<h3>Multiple small improvements to threads</h3>
<p> The internal structures of threading now make fewer <font SIZE="-1">API</font> calls and fewer allocations, resulting in noticeably smaller object code. Additionally, many thread context checks have been deferred so they&#8217;re done only as needed (although this is only possible for non-debugging builds).  </p>
<h3>Adjacent pairs of nextstate opcodes are now optimized away</h3>
<p> Previously, in code such as </p>
<pre><code>    use constant DEBUG =&gt; 0;
    sub GAK {
        warn if DEBUG;
        print &quot;stuff\n&quot;;
    }
</code></pre>
<p> the ops for <code>&quot;warn if DEBUG&quot;</code> would be folded to a <code>&quot;null&quot;</code> op (<code>&quot;ex-const&quot;</code>), but the <code>&quot;nextstate&quot;</code> op would remain, resulting in a runtime op dispatch of <code>&quot;nextstate&quot;</code>, <code>&quot;nextstate&quot;</code>, etc. </p>
<p> The execution of a sequence of <code>&quot;nextstate&quot;</code> ops is indistinguishable from just the last <code>&quot;nextstate&quot;</code> op so the peephole optimizer now eliminates the first of a pair of <code>&quot;nextstate&quot;</code> ops except when the first carries a label, since labels must not be eliminated by the optimizer, and label usage isn&#8217;t conclusively known at compile time.  </p>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> CPAN::Meta::YAML 0.003 has been added as a dual-life module. It supports a subset of <font SIZE="-1">YAML</font> sufficient for reading and writing <i></i><font SIZE="-1"><i>META</i></font><i>.yml</i> and <i></i><font SIZE="-1"><i>MYMETA</i></font><i>.yml</i> files included with <font SIZE="-1">CPAN</font> distributions or generated by the module installation toolchain. It should not be used for any other general <font SIZE="-1">YAML</font> parsing or generation task. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> CPAN::Meta version 2.110440 has been added as a dual-life module. It provides a standard library to read, interpret and write <font SIZE="-1">CPAN</font> distribution metadata files (like <i></i><font SIZE="-1"><i>META</i></font><i>.json</i> and <i></i><font SIZE="-1"><i>META</i></font><i>.yml</i>) that describe a distribution, its contents, and the requirements for building it and installing it. The latest <font SIZE="-1">CPAN</font> distribution metadata specification is included as CPAN::Meta::Spec and notes on changes in the specification over time are given in CPAN::Meta::History. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> HTTP::Tiny 0.012 has been added as a dual-life module. It is a very small, simple <font SIZE="-1">HTTP/1.1</font> client designed for simple <font SIZE="-1">GET</font> requests and file mirroring. It has been added so that <i></i><font SIZE="-1"><i>CPAN</i></font><i>.pm</i> and <font SIZE="-1">CPANPLUS</font> can ``bootstrap&#8217;&#8216; <font SIZE="-1">HTTP</font> access to <font SIZE="-1">CPAN</font> using pure Perl without relying on external binaries like <code><a href="/docs/linux/man/1-curl/">curl</a></code>(1) or <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">JSON::PP</font> 2.27105 has been added as a dual-life module to allow <font SIZE="-1">CPAN</font> clients to read <i></i><font SIZE="-1"><i>META</i></font><i>.json</i> files in <font SIZE="-1">CPAN</font> distributions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Metadata 1.000004 has been added as a dual-life module. It gathers package and <font SIZE="-1">POD</font> information from Perl module files. It is a standalone module based on Module::Build::ModuleInfo for use by other module installation toolchain components. Module::Build::ModuleInfo has been deprecated in favor of this module instead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl::OSType 1.002 has been added as a dual-life module. It maps Perl operating system names (like ``dragonfly&#8217;&#8216; or ``MSWin32&#8217;&#8216;) to more generic types with standardized names (like ``Unix&#8217;&#8216; or ``Windows&#8217;&#8216;). It has been refactored out of Module::Build and ExtUtils::CBuilder and consolidates such mappings into a single location for easier maintenance. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The following modules were added by the Unicode::Collate upgrade. See below for details. </p>
<p> Unicode::Collate::CJK::Big5 </p>
<p> Unicode::Collate::CJK::GB2312 </p>
<p> Unicode::Collate::CJK::JISX0208 </p>
<p> Unicode::Collate::CJK::Korean </p>
<p> Unicode::Collate::CJK::Pinyin </p>
<p> Unicode::Collate::CJK::Stroke </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Version::Requirements version 0.101020 has been added as a dual-life module. It provides a standard library to model and manipulates module prerequisites and version constraints defined in CPAN::Meta::Spec. </p>
 </dd></dl>
<h3>Updated Modules and Pragma</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> attributes has been upgraded from version 0.12 to 0.14. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Archive::Extract has been upgraded from version 0.38 to 0.48. </p>
<p> Updates since 0.38 include: a safe print method that guards Archive::Extract from changes to <code>&quot;$\&quot;</code>; a fix to the tests when run in core Perl; support for <font SIZE="-1">TZ</font> files; a modification for the lzma logic to favour IO::Uncompress::Unlzma; and a fix for an issue with NetBSD-current and its new <code><a href="/docs/linux/man/1-unzip/">unzip</a></code>(1) executable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Archive::Tar has been upgraded from version 1.54 to 1.76. </p>
<p> Important changes since 1.54 include the following: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Compatibility with busybox implementations of <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A fix so that <code>write()</code> and <code>create_archive()</code> close only filehandles they themselves opened. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A bug was fixed regarding the exit code of extract_archive. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code><a href="/docs/linux/man/1-ptar/">ptar</a></code>(1) utility has a new option to allow safe creation of tarballs without world-writable files on Windows, allowing those archives to be uploaded to <font SIZE="-1">CPAN.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new <code><a href="/docs/linux/man/1-ptargrep/">ptargrep</a></code>(1) utility for using regular expressions against the contents of files in a tar archive. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> pax extended headers are now skipped. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Attribute::Handlers has been upgraded from version 0.87 to 0.89. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> autodie has been upgraded from version 2.06_01 to 2.1001. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> AutoLoader has been upgraded from version 5.70 to 5.71. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The B module has been upgraded from version 1.23 to 1.29. </p>
<p> It no longer crashes when taking apart a <code>&quot;y///&quot;</code> containing characters outside the octet range or compiled in a <code>&quot;use utf8&quot;</code> scope. </p>
<p> The size of the shared object has been reduced by about 40%, with no reduction in functionality. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Concise has been upgraded from version 0.78 to 0.83. </p>
<p> B::Concise marks <code>rv2sv()</code>, <code>rv2av()</code>, and <code>rv2hv()</code> ops with the new <code>&quot;OPpDEREF&quot;</code> flag as ``DREFed&#8217;&#8216;. </p>
<p> It no longer produces mangled output with the <code>-tree</code> option [perl #80632]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Debug has been upgraded from version 1.12 to 1.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Deparse has been upgraded from version 0.96 to 1.03. </p>
<p> The deparsing of a <code>&quot;nextstate&quot;</code> op has changed when it has both a change of package relative to the previous nextstate, or a change of <code>&quot;%^H&quot;</code> or other state and a label. The label was previously emitted first, but is now emitted last (5.12.1). </p>
<p> The <code>&quot;no 5.13.2&quot;</code> or similar form is now correctly handled by B::Deparse (5.12.3). </p>
<p> B::Deparse now properly handles the code that applies a conditional pattern match against implicit <code>$_</code> as it was fixed in [perl #20444]. </p>
<p> Deparsing of <code>&quot;our&quot;</code> followed by a variable with funny characters (as permitted under the <code>&quot;use utf8&quot;</code> pragma) has also been fixed [perl #33752]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Lint has been upgraded from version 1.11_01 to 1.13. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> base has been upgraded from version 2.15 to 2.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Benchmark has been upgraded from version 1.11 to 1.12. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> bignum has been upgraded from version 0.23 to 0.27. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Carp has been upgraded from version 1.15 to 1.20. </p>
<p> Carp now detects incomplete <code>caller()</code> overrides and avoids using bogus <code>@DB::args</code>. To provide backtraces, Carp relies on particular behaviour of the <code>caller()</code> builtin. Carp now detects if other code has overridden this with an incomplete implementation, and modifies its backtrace accordingly. Previously incomplete overrides would cause incorrect values in backtraces (best case), or obscure fatal errors (worst case). </p>
<p> This fixes certain cases of ``Bizarre copy of <font SIZE="-1">ARRAY&#8217;&#8216;</font> caused by modules overriding <code>caller()</code> incorrectly (5.12.2). </p>
<p> It now also avoids using regular expressions that cause Perl to load its Unicode tables, so as to avoid the ``<font SIZE="-1">BEGIN</font> not safe after errors&#8217;&#8216; error that ensue if there has been a syntax error [perl #82854]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CGI</font> has been upgraded from version 3.48 to 3.52. </p>
<p> This provides the following security fixes: the <font SIZE="-1">MIME</font> boundary in <code>multipart_init()</code> is now random and the handling of newlines embedded in header values has been improved. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compress::Raw::Bzip2 has been upgraded from version 2.024 to 2.033. </p>
<p> It has been updated to use <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1) 1.0.6. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compress::Raw::Zlib has been upgraded from version 2.024 to 2.033. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> constant has been upgraded from version 1.20 to 1.21. </p>
<p> Unicode constants work once more. They have been broken since Perl 5.10.0 [<font SIZE="-1">CPAN RT</font> #67525]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CPAN</font> has been upgraded from version 1.94_56 to 1.9600. </p>
<p> Major highlights: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> much less configuration dialog hassle </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> support for <i></i><font SIZE="-1"><i>META/MYMETA</i></font><i>.json</i> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> support for local::lib </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> support for HTTP::Tiny to reduce the dependency on <font SIZE="-1">FTP</font> sites </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> automatic mirror selection </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> iron out all known bugs in configure_requires </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> support for distributions compressed with <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> allow <i>Foo/Bar.pm</i> on the command line to mean <code>&quot;Foo::Bar&quot;</code> </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CPANPLUS</font> has been upgraded from version 0.90 to 0.9103. </p>
<p> A change to <i>cpanp-run-perl</i> resolves <font SIZE="-1">RT</font> #55964 &lt;<a rel="nofollow" href="http://rt.cpan.org/Public/Bug/Display.html?id=55964">http://rt.cpan.org/Public/Bug/Display.html?id=55964</a>&gt; and <font SIZE="-1">RT</font> #57106 &lt;<a rel="nofollow" href="http://rt.cpan.org/Public/Bug/Display.html?id=57106">http://rt.cpan.org/Public/Bug/Display.html?id=57106</a>&gt;, both of which related to failures to install distributions that use <code>&quot;Module::Install::DSL&quot;</code> (5.12.2). </p>
<p> A dependency on Config was not recognised as a core module dependency. This has been fixed. </p>
<p> <font SIZE="-1">CPANPLUS</font> now includes support for <i></i><font SIZE="-1"><i>META</i></font><i>.json</i> and <i></i><font SIZE="-1"><i>MYMETA</i></font><i>.json</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> CPANPLUS::Dist::Build has been upgraded from version 0.46 to 0.54. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Data::Dumper has been upgraded from version 2.125 to 2.130_02. </p>
<p> The indentation used to be off when <code>$Data::Dumper::Terse</code> was set. This has been fixed [perl #73604]. </p>
<p> This upgrade also fixes a crash when using custom sort functions that might cause the stack to change [perl #74170]. </p>
<p> Dumpxs no longer crashes with globs returned by <code>*$io_ref</code> [perl #72332]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DB_File has been upgraded from version 1.820 to 1.821. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DBM_Filter has been upgraded from version 0.03 to 0.04. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::DProf has been upgraded from version 20080331.00 to 20110228.00. </p>
<p> Merely loading Devel::DProf now no longer triggers profiling to start. Both <code>&quot;use Devel::DProf&quot;</code> and <code>&quot;perl -d:DProf ...&quot;</code> behave as before and start the profiler. </p>
<p> <font SIZE="-1"><code>NOTE</code></font>: Devel::DProf is deprecated and will be removed from a future version of Perl. We strongly recommend that you install and use Devel::NYTProf instead, as it offers significantly improved profiling and reporting. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::Peek has been upgraded from version 1.04 to 1.07. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::SelfStubber has been upgraded from version 1.03 to 1.05. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> diagnostics has been upgraded from version 1.19 to 1.22. </p>
<p> It now renders pod links slightly better, and has been taught to find descriptions for messages that share their descriptions with other messages. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Digest::MD5 has been upgraded from version 2.39 to 2.51. </p>
<p> It is now safe to use this module in combination with threads. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Digest::SHA has been upgraded from version 5.47 to 5.61. </p>
<p> <code>&quot;shasum&quot;</code> now more closely mimics <code><a href="/docs/linux/man/1-sha1sum/">sha1sum</a></code>(1)/<code><a href="/docs/linux/man/1-md5sum/">md5sum</a></code>(1). </p>
<p> <code>&quot;addfile&quot;</code> accepts all <font SIZE="-1">POSIX</font> filenames. </p>
<p> New <font SIZE="-1">SHA-512/224</font> and <font SIZE="-1">SHA-512/256</font> transforms (ref. <font SIZE="-1">NIST</font> Draft <font SIZE="-1">FIPS 180-4</font> [February 2011]) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DirHandle has been upgraded from version 1.03 to 1.04. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Dumpvalue has been upgraded from version 1.13 to 1.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DynaLoader has been upgraded from version 1.10 to 1.13. </p>
<p> It fixes a buffer overflow when passed a very long file name. </p>
<p> It no longer inherits from AutoLoader; hence it no longer produces weird error messages for unsuccessful method calls on classes that inherit from DynaLoader [perl #84358]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Encode has been upgraded from version 2.39 to 2.42. </p>
<p> Now, all 66 Unicode non-characters are treated the same way U+FFFF has always been treated: in cases when it was disallowed, all 66 are disallowed, and in cases where it warned, all 66 warn. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Env has been upgraded from version 1.01 to 1.02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Errno has been upgraded from version 1.11 to 1.13. </p>
<p> The implementation of Errno has been refactored to use about 55% less memory. </p>
<p> On some platforms with unusual header files, like Win32 <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1) using <code>&quot;mingw64&quot;</code> headers, some constants that weren&#8217;t actually error numbers have been exposed by Errno. This has been fixed [perl #77416]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Exporter has been upgraded from version 5.64_01 to 5.64_03. </p>
<p> Exporter no longer overrides <code>$SIG{__WARN__}</code> [perl #74472] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::CBuilder has been upgraded from version 0.27 to 0.280203. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Command has been upgraded from version 1.16 to 1.17. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Constant has been upgraded from 0.22 to 0.23. </p>
<p> The <font SIZE="-1">AUTOLOAD</font> helper code generated by <code>&quot;ExtUtils::Constant::ProxySubs&quot;</code> can now <code>croak()</code> for missing constants, or generate a complete <code>&quot;AUTOLOAD&quot;</code> subroutine in <font SIZE="-1">XS,</font> allowing simplification of many modules that use it (Fcntl, File::Glob, GDBM_File, I18N::Langinfo, <font SIZE="-1">POSIX</font>, Socket). </p>
<p> ExtUtils::Constant::ProxySubs can now optionally push the names of all constants onto the package&#8217;s <code>@EXPORT_OK</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Install has been upgraded from version 1.55 to 1.56. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::MakeMaker has been upgraded from version 6.56 to 6.57_05. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Manifest has been upgraded from version 1.57 to 1.58. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::ParseXS has been upgraded from version 2.21 to 2.2210. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fcntl has been upgraded from version 1.06 to 1.11. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Basename has been upgraded from version 2.78 to 2.82. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::CheckTree has been upgraded from version 4.4 to 4.41. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Copy has been upgraded from version 2.17 to 2.21. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::DosGlob has been upgraded from version 1.01 to 1.04. </p>
<p> It allows patterns containing literal parentheses: they no longer need to be escaped. On Windows, it no longer adds an extra <i>./</i> to file names returned when the pattern is a relative glob with a drive specification, like <i>C:*.pl</i> [perl #71712]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Fetch has been upgraded from version 0.24 to 0.32. </p>
<p> HTTP::Lite is now supported for the ``http&#8217;&#8216; scheme. </p>
<p> The <code><a href="/docs/linux/man/1-fetch/">fetch</a></code>(1) utility is supported on FreeBSD, NetBSD, and Dragonfly <font SIZE="-1">BSD</font> for the <code>&quot;http&quot;</code> and <code>&quot;ftp&quot;</code> schemes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Find has been upgraded from version 1.15 to 1.19. </p>
<p> It improves handling of backslashes on Windows, so that paths like <i>C:\dir\/file</i> are no longer generated [perl #71710]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Glob has been upgraded from version 1.07 to 1.12. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Spec has been upgraded from version 3.31 to 3.33. </p>
<p> Several portability fixes were made in File::Spec::VMS: a colon is now recognized as a delimiter in native filespecs; caret-escaped delimiters are recognized for better handling of extended filespecs; <code>catpath()</code> returns an empty directory rather than the current directory if the input directory name is empty; and <code>abs2rel()</code> properly handles Unix-style input (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::stat has been upgraded from 1.02 to 1.05. </p>
<p> The <code>&quot;-x&quot;</code> and <code>&quot;-X&quot;</code> file test operators now work correctly when run by the superuser. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Filter::Simple has been upgraded from version 0.84 to 0.86. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> GDBM_File has been upgraded from 1.10 to 1.14. </p>
<p> This fixes a memory leak when <font SIZE="-1">DBM</font> filters are used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hash::Util has been upgraded from 0.07 to 0.11. </p>
<p> Hash::Util no longer emits spurious ``uninitialized&#8217;&#8216; warnings when recursively locking hashes that have undefined values [perl #74280]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hash::Util::FieldHash has been upgraded from version 1.04 to 1.09. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> I18N::Collate has been upgraded from version 1.01 to 1.02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> I18N::Langinfo has been upgraded from version 0.03 to 0.08. </p>
<p> <code>langinfo()</code> now defaults to using <code>$_</code> if there is no argument given, just as the documentation has always claimed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> I18N::LangTags has been upgraded from version 0.35 to 0.35_01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> if has been upgraded from version 0.05 to 0.0601. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">IO</font> has been upgraded from version 1.25_02 to 1.25_04. </p>
<p> This version of <font SIZE="-1">IO</font> includes a new IO::Select, which now allows IO::Handle objects (and objects in derived classes) to be removed from an IO::Select set even if the underlying file descriptor is closed or invalid. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::Cmd has been upgraded from version 0.54 to 0.70. </p>
<p> Resolves an issue with splitting Win32 command lines. An argument consisting of the single character ``0&#8217;&#8216; used to be omitted (<font SIZE="-1">CPAN RT</font> #62961). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::Open3 has been upgraded from 1.05 to 1.09. </p>
<p> <code>open3()</code> now produces an error if the <code>&quot;exec&quot;</code> call fails, allowing this condition to be distinguished from a child process that exited with a non-zero status [perl #72016]. </p>
<p> The internal <code>xclose()</code> routine now knows how to handle file descriptors as documented, so duplicating <code>&quot;STDIN&quot;</code> in a child process using its file descriptor now works [perl #76474]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::SysV has been upgraded from version 2.01 to 2.03. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> lib has been upgraded from version 0.62 to 0.63. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locale::Maketext has been upgraded from version 1.14 to 1.19. </p>
<p> Locale::Maketext now supports external caches. </p>
<p> This upgrade also fixes an infinite loop in <code>&quot;Locale::Maketext::Guts::_compile()&quot;</code> when working with tainted values (<font SIZE="-1">CPAN RT</font> #40727). </p>
<p> <code>&quot;-&gt;maketext&quot;</code> calls now back up and restore <code>$@</code> so error messages are not suppressed (<font SIZE="-1">CPAN RT</font> #34182). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Log::Message has been upgraded from version 0.02 to 0.04. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Log::Message::Simple has been upgraded from version 0.06 to 0.08. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigInt has been upgraded from version 1.89_01 to 1.994. </p>
<p> This fixes, among other things, incorrect results when computing binomial coefficients [perl #77640]. </p>
<p> It also prevents <code>&quot;sqrt($int)&quot;</code> from crashing under <code>&quot;use bigrat&quot;</code>. [perl #73534]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigInt::FastCalc has been upgraded from version 0.19 to 0.28. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigRat has been upgraded from version 0.24 to 0.26_02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Memoize has been upgraded from version 1.01_03 to 1.02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> MIME::Base64 has been upgraded from 3.08 to 3.13. </p>
<p> Includes new functions to calculate the length of encoded and decoded base64 strings. </p>
<p> Now provides <code>encode_base64url()</code> and <code>decode_base64url()</code> functions to process the base64 scheme for ``<font SIZE="-1">URL</font> applications&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Build has been upgraded from version 0.3603 to 0.3800. </p>
<p> A notable change is the deprecation of several modules. Module::Build::Version has been deprecated and Module::Build now relies on the version pragma directly. Module::Build::ModuleInfo has been deprecated in favor of a standalone copy called Module::Metadata. Module::Build::YAML has been deprecated in favor of CPAN::Meta::YAML. </p>
<p> Module::Build now also generates <i></i><font SIZE="-1"><i>META</i></font><i>.json</i> and <i></i><font SIZE="-1"><i>MYMETA</i></font><i>.json</i> files in accordance with version 2 of the <font SIZE="-1">CPAN</font> distribution metadata specification, CPAN::Meta::Spec. The older format <i></i><font SIZE="-1"><i>META</i></font><i>.yml</i> and <i></i><font SIZE="-1"><i>MYMETA</i></font><i>.yml</i> files are still generated. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::CoreList has been upgraded from version 2.29 to 2.47. </p>
<p> Besides listing the updated core modules of this release, it also stops listing the <code>&quot;Filespec&quot;</code> module. That module never existed in core. The scripts generating Module::CoreList confused it with VMS::Filespec, which actually is a core module as of Perl 5.8.7. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Load has been upgraded from version 0.16 to 0.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Load::Conditional has been upgraded from version 0.34 to 0.44. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The mro pragma has been upgraded from version 1.02 to 1.07. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> NDBM_File has been upgraded from version 1.08 to 1.12. </p>
<p> This fixes a memory leak when <font SIZE="-1">DBM</font> filters are used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Net::Ping has been upgraded from version 2.36 to 2.38. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">NEXT</font> has been upgraded from version 0.64 to 0.65. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Object::Accessor has been upgraded from version 0.36 to 0.38. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ODBM_File has been upgraded from version 1.07 to 1.10. </p>
<p> This fixes a memory leak when <font SIZE="-1">DBM</font> filters are used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Opcode has been upgraded from version 1.15 to 1.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The overload pragma has been upgraded from 1.10 to 1.13. </p>
<p> <code>&quot;overload::Method&quot;</code> can now handle subroutines that are themselves blessed into overloaded classes [perl #71998]. </p>
<p> The documentation has greatly improved. See ``Documentation&#8217;&#8216; below. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Params::Check has been upgraded from version 0.26 to 0.28. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The parent pragma has been upgraded from version 0.223 to 0.225. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Parse::CPAN::Meta has been upgraded from version 1.40 to 1.4401. </p>
<p> The latest Parse::CPAN::Meta can now read <font SIZE="-1">YAML</font> and <font SIZE="-1">JSON</font> files using CPAN::Meta::YAML and <font SIZE="-1">JSON::PP</font>, which are now part of the Perl core. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::encoding has been upgraded from version 0.12 to 0.14. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::scalar has been upgraded from 0.07 to 0.11. </p>
<p> A <code>read()</code> after a <code>seek()</code> beyond the end of the string no longer thinks it has data to read [perl #78716]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::via has been upgraded from version 0.09 to 0.11. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Html has been upgraded from version 1.09 to 1.11. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::LaTeX has been upgraded from version 0.58 to 0.59. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Perldoc has been upgraded from version 3.15_02 to 3.15_03. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Simple has been upgraded from version 3.13 to 3.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">POSIX</font> has been upgraded from 1.19 to 1.24. </p>
<p> It now includes constants for <font SIZE="-1">POSIX</font> signal constants. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The re pragma has been upgraded from version 0.11 to 0.18. </p>
<p> The <code>&quot;use re &#8216;/flags&#8217;&quot;</code> subpragma is new. </p>
<p> The <code>regmust()</code> function used to crash when called on a regular expression belonging to a pluggable engine. Now it croaks instead. </p>
<p> <code>regmust()</code> no longer leaks memory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Safe has been upgraded from version 2.25 to 2.29. </p>
<p> Coderefs returned by <code>reval()</code> and <code>rdo()</code> are now wrapped via <code>wrap_code_refs()</code> (5.12.1). </p>
<p> This fixes a possible infinite loop when looking for coderefs. </p>
<p> It adds several <code>&quot;version::vxs::*&quot;</code> routines to the default share. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> SDBM_File has been upgraded from version 1.06 to 1.09. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> SelfLoader has been upgraded from 1.17 to 1.18. </p>
<p> It now works in taint mode [perl #72062]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The sigtrap pragma has been upgraded from version 1.04 to 1.05. </p>
<p> It no longer tries to modify read-only arguments when generating a backtrace [perl #72340]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Socket has been upgraded from version 1.87 to 1.94. </p>
<p> See ``Improved IPv6 support&#8217;&#8216; above. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Storable has been upgraded from version 2.22 to 2.27. </p>
<p> Includes performance improvement for overloaded classes. </p>
<p> This adds support for serialising code references that contain <font SIZE="-1">UTF-8</font> strings correctly. The Storable minor version number changed as a result, meaning that Storable users who set <code>$Storable::accept_future_minor</code> to a <code>&quot;FALSE&quot;</code> value will see errors (see ``<font SIZE="-1">FORWARD COMPATIBILITY&#8217;&#8216;</font> in Storable for more details). </p>
<p> Freezing no longer gets confused if the Perl stack gets reallocated during freezing [perl #80074]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Sys::Hostname has been upgraded from version 1.11 to 1.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Term::ANSIColor has been upgraded from version 2.02 to 3.00. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Term::UI has been upgraded from version 0.20 to 0.26. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test::Harness has been upgraded from version 3.17 to 3.23. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test::Simple has been upgraded from version 0.94 to 0.98. </p>
<p> Among many other things, subtests without a <code>&quot;plan&quot;</code> or <code>&quot;no_plan&quot;</code> now have an implicit <code>done_testing()</code> added to them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Thread::Semaphore has been upgraded from version 2.09 to 2.12. </p>
<p> It provides two new methods that give more control over the decrementing of semaphores: <code>&quot;down_nb&quot;</code> and <code>&quot;down_force&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Thread::Queue has been upgraded from version 2.11 to 2.12. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The threads pragma has been upgraded from version 1.75 to 1.83. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The threads::shared pragma has been upgraded from version 1.32 to 1.37. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::Hash has been upgraded from version 1.03 to 1.04. </p>
<p> Calling <code>&quot;Tie::Hash-&gt;TIEHASH()&quot;</code> used to loop forever. Now it <code>&quot;croak&quot;</code>s. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::Hash::NamedCapture has been upgraded from version 0.06 to 0.08. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::RefHash has been upgraded from version 1.38 to 1.39. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::HiRes has been upgraded from version 1.9719 to 1.9721_01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::Local has been upgraded from version 1.1901_01 to 1.2000. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::Piece has been upgraded from version 1.15_01 to 1.20_01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::Collate has been upgraded from version 0.52_01 to 0.73. </p>
<p> Unicode::Collate has been updated to use Unicode 6.0.0. </p>
<p> Unicode::Collate::Locale now supports a plethora of new locales: <i>ar, be, bg, de__phonebook, hu, hy, kk, mk, nso, om, tn, vi, hr, ig, ja, ko, ru, sq, se, sr, to, uk, zh, zh__big5han, zh__gb2312han, zh__pinyin</i>, and <i>zh__stroke</i>. </p>
<p> The following modules have been added: </p>
<p> Unicode::Collate::CJK::Big5 for <code>&quot;zh__big5han&quot;</code> which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s big5han ordering. </p>
<p> Unicode::Collate::CJK::GB2312 for <code>&quot;zh__gb2312han&quot;</code> which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s gb2312han ordering. </p>
<p> Unicode::Collate::CJK::JISX0208 which makes tailoring of 6355 kanji (<font SIZE="-1">CJK</font> Unified Ideographs) in the <font SIZE="-1">JIS X 0208</font> order. </p>
<p> Unicode::Collate::CJK::Korean which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s Korean ordering. </p>
<p> Unicode::Collate::CJK::Pinyin for <code>&quot;zh__pinyin&quot;</code> which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s pinyin ordering. </p>
<p> Unicode::Collate::CJK::Stroke for <code>&quot;zh__stroke&quot;</code> which makes tailoring of <font SIZE="-1">CJK</font> Unified Ideographs in the order of <font SIZE="-1">CLDR</font>&#8216;s stroke ordering. </p>
<p> This also sees the switch from using the pure-Perl version of this module to the <font SIZE="-1">XS</font> version. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::Normalize has been upgraded from version 1.03 to 1.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::UCD has been upgraded from version 0.27 to 0.32. </p>
<p> A new function, <code>Unicode::UCD::num()</code>, has been added. This function returns the numeric value of the string passed it or <code>&quot;undef&quot;</code> if the string in its entirety has no ``safe&#8217;&#8216; numeric value. (For more detail, and for the definition of ``safe&#8217;&#8216;, see ``<code>num()</code>&#8216;&#8216; in Unicode::UCD.) </p>
<p> This upgrade also includes several bug fixes: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>charinfo()</code></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> It is now updated to Unicode Version 6.0.0 with <i>Corrigendum #8</i>, excepting that, just as with Perl 5.14, the code point at U+1F514 has no name. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hangul syllable code points have the correct names, and their decompositions are always output without requiring Lingua::KO::Hangul::Util to be installed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CJK</font> (Chinese-Japanese-Korean) code points U+2A700 to U+2B734 and U+2B740 to U+2B81D are now properly handled. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Numeric values are now output for those <font SIZE="-1">CJK</font> code points that have them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Names output for code points with multiple aliases are now the corrected ones. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt><code>charscript()</code></dt>
<dd> <p> This now correctly returns ``Unknown&#8217;&#8216; instead of <code>&quot;undef&quot;</code> for the script of a code point that hasn&#8217;t been assigned another one. </p>
 </dd>
<dt><code>charblock()</code></dt>
<dd> <p> This now correctly returns ``No_Block&#8217;&#8216; instead of <code>&quot;undef&quot;</code> for the block of a code point that hasn&#8217;t been assigned to another one. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> The version pragma has been upgraded from 0.82 to 0.88. </p>
<p> Because of a bug, now fixed, the <code>is_strict()</code> and <code>is_lax()</code> functions did not work when exported (5.12.1). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The warnings pragma has been upgraded from version 1.09 to 1.12. </p>
<p> Calling <code>&quot;use warnings&quot;</code> without arguments is now significantly more efficient. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The warnings::register pragma has been upgraded from version 1.01 to 1.02. </p>
<p> It is now possible to register warning categories other than the names of packages using warnings::register. See <code><a href="/docs/linux/man/1-perllexwarn/">perllexwarn</a></code>(1) for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> XSLoader has been upgraded from version 0.10 to 0.13. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> VMS::DCLsym has been upgraded from version 1.03 to 1.05. </p>
<p> Two bugs have been fixed [perl #84086]: </p>
<p> The symbol table name was lost when tying a hash, due to a thinko in <code>&quot;TIEHASH&quot;</code>. The result was that all tied hashes interacted with the local symbol table. </p>
<p> Unless a symbol table name had been explicitly specified in the call to the constructor, querying the special key <code>&quot;:LOCAL&quot;</code> failed to identify objects connected to the local symbol table. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Win32 module has been upgraded from version 0.39 to 0.44. </p>
<p> This release has several new functions: <code>Win32::GetSystemMetrics()</code>, <code>Win32::GetProductInfo()</code>, <code>Win32::GetOSDisplayName()</code>. </p>
<p> The names returned by <code>Win32::GetOSName()</code> and <code>Win32::GetOSDisplayName()</code> have been corrected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> XS::Typemap has been upgraded from version 0.03 to 0.05. </p>
 </dd></dl>
<h3>Removed Modules and Pragmata</h3>
<p> As promised in Perl 5.12.0&#8217;s release notes, the following modules have been removed from the core distribution, and if needed should be installed from <font SIZE="-1">CPAN</font> instead. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Class::ISA has been removed from the Perl core. Prior version was 0.36. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Plainer has been removed from the Perl core. Prior version was 1.02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Switch has been removed from the Perl core. Prior version was 2.16. </p>
 </dd></dl>
<p> The removal of Shell has been deferred until after 5.14, as the implementation of Shell shipped with 5.12.0 did not correctly issue the warning that it was to be removed from core.  </p>
<h2>Documentation</h2>
<h3>New Documentation</h3>
<p> <i>perlgpl</i> </p>
<p> perlgpl has been updated to contain <font SIZE="-1">GPL</font> version 1, as is included in the <i></i><font SIZE="-1"><i>README</i></font><i></i> distributed with Perl (5.12.1). </p>
<p> <i>Perl 5.12.x delta files</i> </p>
<p> The perldelta files for Perl 5.12.1 to 5.12.3 have been added from the maintenance branch: perl5121delta, perl5122delta, perl5123delta. </p>
<p> <i>perlpodstyle</i> </p>
<p> New style guide for <font SIZE="-1">POD</font> documentation, split mostly from the <font SIZE="-1">NOTES</font> section of the <code><a href="/docs/linux/man/1-pod2man/">pod2man</a></code>(1) manpage. </p>
<p> <i>perlsource, perlinterp, perlhacktut, and perlhacktips</i> </p>
<p> See ``perlhack and perlrepository revamp&#8217;&#8216;, below.  </p>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlmodlib is now complete</i> </p>
<p> The perlmodlib manpage that came with Perl 5.12.0 was missing several modules due to a bug in the script that generates the list. This has been fixed [perl #74332] (5.12.1). </p>
<p> <i>Replace incorrect tr/// table in perlebcdic</i> </p>
<p> perlebcdic contains a helpful table to use in <code>&quot;tr///&quot;</code> to convert between <font SIZE="-1">EBCDIC</font> and Latin1/ASCII. The table was the inverse of the one it describes, though the code that used the table worked correctly for the specific example given. </p>
<p> The table has been corrected and the sample code changed to correspond. </p>
<p> The table has also been changed to hex from octal, and the recipes in the pod have been altered to print out leading zeros to make all values the same length. </p>
<p> <i>Tricks for user-defined casing</i> </p>
<p> perlunicode now contains an explanation of how to override, mangle and otherwise tweak the way Perl handles upper-, lower- and other-case conversions on Unicode data, and how to provide scoped changes to alter one&#8217;s own code&#8217;s behaviour without stomping on anybody else&#8217;s. </p>
<p> <i></i><font SIZE="-1"><i>INSTALL</i></font><i> explicitly states that Perl requires a C89 compiler</i> </p>
<p> This was already true, but it&#8217;s now Officially Stated For The Record (5.12.2). </p>
<p> <i>Explanation of </i>&quot;\xHH&quot;<i> and </i>&quot;\oOOO&quot;<i> escapes</i> </p>
<p> perlop has been updated with more detailed explanation of these two character escapes. </p>
<p> <i></i>-0<font SIZE="-1">NNN</font><i> switch</i> </p>
<p> In perlrun, the behaviour of the <code>-0NNN</code> switch for <code>-0400</code> or higher has been clarified (5.12.2). </p>
<p> <i>Maintenance policy</i> </p>
<p> perlpolicy now contains the policy on what patches are acceptable for maintenance branches (5.12.1). </p>
<p> <i>Deprecation policy</i> </p>
<p> perlpolicy now contains the policy on compatibility and deprecation along with definitions of terms like ``deprecation&#8217;&#8216; (5.12.2). </p>
<p> <i>New descriptions in perldiag</i> </p>
<p> The following existing diagnostics are now documented: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Ambiguous use of <code>%c</code> resolved as operator <code>%c</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Ambiguous use of <code>%c</code>{%s} resolved to <code>%c</code>%s </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Ambiguous use of <code>%c</code>{%s[...]} resolved to <code>%c</code>%s[...] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Ambiguous use of <code>%c</code>{%s{...}} resolved to <code>%c</code>%s{...} </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Ambiguous use of -%s resolved as -&amp;%s() </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Invalid strict version format (%s) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Invalid version format (%s) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Invalid version object </p>
 </dd></dl>
<p> <i>perlbook</i> </p>
<p> perlbook has been expanded to cover many more popular books. </p>
<p> <i></i>&quot;SvTRUE&quot;<i> macro</i> </p>
<p> The documentation for the <code>&quot;SvTRUE&quot;</code> macro in perlapi was simply wrong in stating that get-magic is not processed. It has been corrected. </p>
<p> <i>op manipulation functions</i> </p>
<p> Several <font SIZE="-1">API</font> functions that process optrees have been newly documented. </p>
<p> <i>perlvar revamp</i> </p>
<p> perlvar reorders the variables and groups them by topic. Each variable introduced after Perl 5.000 notes the first version in which it is available. perlvar also has a new section for deprecated variables to note when they were removed. </p>
<p> <i>Array and hash slices in scalar context</i> </p>
<p> These are now documented in perldata. </p>
<p> <i></i>&quot;use locale&quot;<i> and formats</i> </p>
<p> perlform and perllocale have been corrected to state that <code>&quot;use locale&quot;</code> affects formats. </p>
<p> <i>overload</i> </p>
<p> overload&#8217;s documentation has practically undergone a rewrite. It is now much more straightforward and clear. </p>
<p> <i>perlhack and perlrepository revamp</i> </p>
<p> The perlhack document is now much shorter, and focuses on the Perl 5 development process and submitting patches to Perl. The technical content has been moved to several new documents, perlsource, perlinterp, perlhacktut, and perlhacktips. This technical content has been only lightly edited. </p>
<p> The perlrepository document has been renamed to perlgit. This new document is just a how-to on using git with the Perl source code. Any other content that used to be in perlrepository has been moved to perlhack. </p>
<p> <i>Time::Piece examples</i> </p>
<p> Examples in perlfaq4 have been updated to show the use of Time::Piece.  </p>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.  </p>
<h3>New Diagnostics</h3>
<p> <i>New Errors</i> </p>
<dl>
<dt>Closure prototype called</dt>
<dd> <p> This error occurs when a subroutine reference passed to an attribute handler is called, if the subroutine is a closure [perl #68560]. </p>
 </dd>
<dt>Insecure user-defined property %s</dt>
<dd> <p> Perl detected tainted data when trying to compile a regular expression that contains a call to a user-defined character property function, meaning <code>&quot;\p{IsFoo}&quot;</code> or <code>&quot;\p{InFoo}&quot;</code>. See ``User-Defined Character Properties&#8217;&#8216; in perlunicode and perlsec. </p>
 </dd>
<dt>panic: gp_free failed to free glob pointer &#8211; something is repeatedly re-creating entries</dt>
<dd> <p> This new error is triggered if a destructor called on an object in a typeglob that is being freed creates a new typeglob entry containing an object with a destructor that creates a new entry containing an object etc. </p>
 </dd>
<dt>Parsing code internal error (%s)</dt>
<dd> <p> This new fatal error is produced when parsing code supplied by an extension violates the parser&#8217;s <font SIZE="-1">API</font> in a detectable way. </p>
 </dd>
<dt>refcnt: fd %d%s</dt>
<dd> <p> This new error only occurs if an internal consistency check fails when a pipe is about to be closed. </p>
 </dd>
<dt>Regexp modifier &quot;/%c&quot; may not appear twice</dt>
<dd> <p> The regular expression pattern has one of the mutually exclusive modifiers repeated. </p>
 </dd>
<dt>Regexp modifiers &quot;/%c&quot; and &quot;/%c&quot; are mutually exclusive</dt>
<dd> <p> The regular expression pattern has more than one of the mutually exclusive modifiers. </p>
 </dd>
<dt>Using !~ with %s doesn&#8217;t make sense</dt>
<dd> <p> This error occurs when <code>&quot;!~&quot;</code> is used with <code>&quot;s///r&quot;</code> or <code>&quot;y///r&quot;</code>. </p>
 </dd></dl>
<p> <i>New Warnings</i> </p>
<dl>
<dt>&quot;\b{&quot; is deprecated; use &quot;\b\{&quot; instead</dt>
<dd>  </dd>
<dt>&quot;\B{&quot; is deprecated; use &quot;\B\{&quot; instead</dt>
<dd> <p> Use of an unescaped ``{&#8216;&#8216; immediately following a <code>&quot;\b&quot;</code> or <code>&quot;\B&quot;</code> is now deprecated in order to reserve its use for Perl itself in a future release. </p>
 </dd>
<dt>Operation &quot;%s&quot; returns its argument for ...</dt>
<dd> <p> Performing an operation requiring Unicode semantics (such as case-folding) on a Unicode surrogate or a non-Unicode character now triggers this warning. </p>
 </dd>
<dt>Use of qw(...) as parentheses is deprecated</dt>
<dd> <p> See ``Use of qw(...) as parentheses&#8217;&#8216;, above, for details. </p>
 </dd></dl>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The ``Variable <code>$foo</code> is not imported&#8217;&#8216; warning that precedes a <code>&quot;strict &#8216;vars&#8217;&quot;</code> error has now been assigned the ``misc&#8217;&#8216; category, so that <code>&quot;no warnings&quot;</code> will suppress it [perl #73712]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>warn()</code> and <code>die()</code> now produce ``Wide character&#8217;&#8216; warnings when fed a character outside the byte range if <code>&quot;STDERR&quot;</code> is a byte-sized handle. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ``Layer does not match this perl&#8217;&#8216; error message has been replaced with these more helpful messages [perl #73754]: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> PerlIO layer function table size (%d) does not match size expected by this perl (%d) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO layer instance size (%d) does not match size expected by this perl (%d) </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> The ``Found = in conditional&#8217;&#8216; warning that is emitted when a constant is assigned to a variable in a condition is now withheld if the constant is actually a subroutine or one generated by <code>&quot;use constant&quot;</code>, since the value of the constant may not be known at the time the program is written [perl #77762]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Previously, if none of the <code>gethostbyaddr()</code>, <code>gethostbyname()</code> and <code>gethostent()</code> functions were implemented on a given platform, they would all die with the message ``Unsupported socket function &#8216;gethostent&#8217; called&#8217;&#8216;, with analogous messages for getnet*() and getserv*(). This has been corrected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The warning message about unrecognized regular expression escapes passed through has been changed to include any literal ``{&#8216;&#8216; following the two-character escape. For example, ``\q{&#8216;&#8216; is now emitted instead of ``\q&#8217;&#8216;. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<p> <i></i><a href="/docs/linux/man/1-perlbug/">perlbug</a><i>(1)</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> perlbug now looks in the <font SIZE="-1">EMAIL</font> environment variable for a return address if the REPLY-TO and <font SIZE="-1">REPLYTO</font> variables are empty. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlbug did not previously generate a ``From:&#8216;&#8216; header, potentially resulting in dropped mail; it now includes that header. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The user&#8217;s address is now used as the Return-Path. </p>
<p> Many systems these days don&#8217;t have a valid Internet domain name, and perlbug [at] perl.org does not accept email with a return-path that does not resolve. So the user&#8217;s address is now passed to sendmail so it&#8217;s less likely to get stuck in a mail queue somewhere [perl #82996]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlbug now always gives the reporter a chance to change the email address it guesses for them (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlbug should no longer warn about uninitialized values when using the <code>-d</code> and <code>-v</code> options (5.12.2). </p>
 </dd></dl>
<p> <i>perl5db.pl</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The remote terminal works after forking and spawns new sessions, one per forked process. </p>
 </dd></dl>
<p> <i>ptargrep</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> ptargrep is a new utility to apply pattern matching to the contents of files in a tar archive. It comes with <code>&quot;Archive::Tar&quot;</code>. </p>
 </dd></dl>
<h2>Configuration and Compilation</h2>
<p> See also ``Naming fixes in Policy_sh.SH may invalidate Policy.sh&#8217;&#8216;, above. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CCINCDIR</font> and <font SIZE="-1">CCLIBDIR</font> for the mingw64 cross-compiler are now correctly under <i>$(</i><font SIZE="-1"><i>CCHOME</i></font><i>)\mingw\include</i> and <i>\lib</i> rather than immediately below <i>$(</i><font SIZE="-1"><i>CCHOME</i></font><i>)</i>. </p>
<p> This means the ``incpath&#8217;&#8216;, ``libpth&#8217;&#8216;, ``ldflags&#8217;&#8216;, ``lddlflags&#8217;&#8216; and ``ldflags_nolargefiles&#8217;&#8216; values in <i>Config.pm</i> and <i>Config_heavy.pl</i> are now set correctly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;make test.valgrind&quot;</code> has been adjusted to account for <i>cpan/dist/ext</i> separation. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On compilers that support it, <code>-Wwrite-strings</code> is now added to cflags by default. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Encode module can now (once again) be included in a static Perl build. The special-case handling for this situation got broken in Perl 5.11.0, and has now been repaired. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The previous default size of a PerlIO buffer (4096 bytes) has been increased to the larger of 8192 bytes and your local <font SIZE="-1">BUFSIZ.</font> Benchmarks show that doubling this decade-old default increases read and write performance by around 25% to 50% when using the default layers of perlio on top of unix. To choose a non-default size, such as to get back the old value or to obtain an even larger value, configure with: </p>
<pre><code>     ./Configure -Accflags=-DPERLIOBUF_DEFAULT_BUFSIZ=N
</code></pre>
<p> where N is the desired size in bytes; it should probably be a multiple of your page size. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An ``incompatible operand types&#8217;&#8216; error in ternary expressions when building with <code>&quot;clang&quot;</code> has been fixed (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now skips setuid File::Copy tests on partitions it detects mounted as <code>&quot;nosuid&quot;</code> (5.12.2). </p>
 </dd></dl>
<h2>Platform Support</h2>
<h3>New Platforms</h3>
<dl>
<dt><font SIZE="-1">AIX</font></dt>
<dd> <p> Perl now builds on <font SIZE="-1">AIX 4.2</font> (5.12.1). </p>
 </dd></dl>
<h3>Discontinued Platforms</h3>
<dl>
<dt>Apollo DomainOS</dt>
<dd> <p> The last vestiges of support for this platform have been excised from the Perl distribution. It was officially discontinued in version 5.12.0. It had not worked for years before that. </p>
 </dd>
<dt>MacOS Classic</dt>
<dd> <p> The last vestiges of support for this platform have been excised from the Perl distribution. It was officially discontinued in an earlier version. </p>
 </dd></dl>
<h3>Platform-Specific Notes</h3>
<p> <i></i><font SIZE="-1"><i>AIX</i></font><i></i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <i></i><font SIZE="-1"><i>README</i></font><i>.aix</i> has been updated with information about the <font SIZE="-1">XL C/C<font SIZE="-2">++</font> V11</font> compiler suite (5.12.2). </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>ARM</i></font><i></i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;d_u32align&quot;</code> configuration probe on <font SIZE="-1">ARM</font> has been fixed (5.12.2). </p>
 </dd></dl>
<p> <i>Cygwin</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> MakeMaker has been updated to build manpages on cygwin. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Improved rebase behaviour </p>
<p> If a <font SIZE="-1">DLL</font> is updated on cygwin the old imagebase address is reused. This solves most rebase errors, especially when updating on core <font SIZE="-1">DLL</font>&#8216;s. See &lt;<a rel="nofollow" href="http://www.tishler.net/jason/software/rebase/rebase-2.4.2.README">http://www.tishler.net/jason/software/rebase/rebase-2.4.2.README</a>&gt; for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Support for the standard cygwin dll prefix (needed for FFIs) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Updated build hints file </p>
 </dd></dl>
<p> <i>FreeBSD 7</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> FreeBSD 7 no longer contains <i>/usr/bin/objformat</i>. At build time, Perl now skips the <i>objformat</i> check for versions 7 and higher and assumes <font SIZE="-1">ELF</font> (5.12.1). </p>
 </dd></dl>
<p> <i>HP-UX</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Perl now allows <code>-Duse64bitint</code> without promoting to <code>&quot;use64bitall&quot;</code> on HP-UX (5.12.1). </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>IRIX</i></font><i></i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Conversion of strings to floating-point numbers is now more accurate on <font SIZE="-1">IRIX</font> systems [perl #32380]. </p>
 </dd></dl>
<p> <i>Mac </i><font SIZE="-1"><i>OS X</i></font><i></i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Early versions of Mac <font SIZE="-1">OS X</font> (Darwin) had buggy implementations of the <code>setregid()</code>, <code>setreuid()</code>, setrgid(,) and <code>setruid()</code> functions, so Perl would pretend they did not exist. </p>
<p> These functions are now recognised on Mac <font SIZE="-1">OS 10.5</font> (Leopard; Darwin 9) and higher, as they have been fixed [perl #72990]. </p>
 </dd></dl>
<p> <i>MirBSD</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Previously if you built Perl with a shared <i>libperl.so</i> on MirBSD (the default config), it would work up to the installation; however, once installed, it would be unable to find <i>libperl</i>. Path handling is now treated as in the other <font SIZE="-1">BSD</font> dialects. </p>
 </dd></dl>
<p> <i>NetBSD</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The NetBSD hints file has been changed to make the system malloc the default. </p>
 </dd></dl>
<p> <i>OpenBSD</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> OpenBSD &gt; 3.7 has a new malloc implementation which is <i>mmap</i>-based, and as such can release memory back to the <font SIZE="-1">OS</font>; however, Perl&#8217;s use of this malloc causes a substantial slowdown, so we now default to using Perl&#8217;s malloc instead [perl #75742]. </p>
 </dd></dl>
<p> <i>OpenVOS</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Perl now builds again with OpenVOS (formerly known as Stratus <font SIZE="-1">VOS</font>) [perl #78132] (5.12.3). </p>
 </dd></dl>
<p> <i>Solaris</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> DTrace is now supported on Solaris. There used to be build failures, but these have been fixed [perl #73630] (5.12.3). </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>VMS</i></font><i></i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Extension building on older (pre 7.3-2) <font SIZE="-1">VMS</font> systems was broken because configure.com hit the <font SIZE="-1">DCL</font> symbol length limit of 1K. We now work within this limit when assembling the list of extensions in the core build (5.12.1). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> We fixed configuring and building Perl with <code>-Uuseperlio</code> (5.12.1). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PerlIOUnix_open&quot;</code> now honours the default permissions on <font SIZE="-1">VMS.</font> </p>
<p> When <code>&quot;perlio&quot;</code> became the default and <code>&quot;unix&quot;</code> became the default bottom layer, the most common path for creating files from Perl became <code>&quot;PerlIOUnix_open&quot;</code>, which has always explicitly used <code>0666</code> as the permission mask. This prevents inheriting permissions from <font SIZE="-1">RMS</font> defaults and ACLs, so to avoid that problem, we now pass <code>0777</code> to <code>open()</code>. In the <font SIZE="-1">VMS CRTL,</font> <code>0777</code> has a special meaning over and above intersecting with the current umask; specifically, it allows Unix syscalls to preserve native default permissions (5.12.3). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The shortening of symbols longer than 31 characters in the core C sources and in extensions is now by default done by the C compiler rather than by xsubpp (which could only do so for generated symbols in <font SIZE="-1">XS</font> code). You can reenable xsubpp&#8217;s symbol shortening by configuring with -Uuseshortenedsymbols, but you&#8217;ll have some work to do to get the core sources to compile. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Record-oriented files (record format variable or variable with fixed control) opened for write by the <code>&quot;perlio&quot;</code> layer will now be line-buffered to prevent the introduction of spurious line breaks whenever the perlio buffer fills up. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>git_version.h</i> is now installed on <font SIZE="-1">VMS.</font> This was an oversight in v5.12.0 which caused some extensions to fail to build (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several memory leaks in <code>stat()</code> have been fixed (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A memory leak in <code>Perl_rename()</code> due to a double allocation has been fixed (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A memory leak in <code>vms_fid_to_name()</code> (used by <code>realpath()</code> and <code>realname()</code>&gt; has been fixed (5.12.2). </p>
 </dd></dl>
<p> <i>Windows</i> </p>
<p> See also ``<code>fork()</code> emulation will not wait for signalled children&#8217;&#8216; and ``Perl source code is read in text mode on Windows&#8217;&#8216;, above. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Fixed build process for <font SIZE="-1">SDK2003SP1</font> compilers. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compilation with Visual Studio 2010 is now supported. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When using old 32-bit compilers, the define <code>&quot;_USE_32BIT_TIME_T&quot;</code> is now set in <code>$Config{ccflags}</code>. This improves portability when compiling <font SIZE="-1">XS</font> extensions using new compilers, but for a Perl compiled with old 32-bit compilers. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$Config{gccversion}</code> is now set correctly when Perl is built using the mingw64 compiler from &lt;<a rel="nofollow" href="http://mingw64.org">http://mingw64.org</a>&gt; [perl #73754]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When building Perl with the mingw64 x64 cross-compiler <code>&quot;incpath&quot;</code>, <code>&quot;libpth&quot;</code>, <code>&quot;ldflags&quot;</code>, <code>&quot;lddlflags&quot;</code> and <code>&quot;ldflags_nolargefiles&quot;</code> values in <i>Config.pm</i> and <i>Config_heavy.pl</i> were not previously being set correctly because, with that compiler, the include and lib directories are not immediately below <code>&quot;$(CCHOME)&quot;</code> (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The build process proceeds more smoothly with mingw and dmake when <i>C:\MSYS\bin</i> is in the <font SIZE="-1">PATH,</font> due to a <code>&quot;Cwd&quot;</code> fix. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Support for building with Visual C<font SIZE="-2">++</font> 2010 is now underway, but is not yet complete. See <i></i><font SIZE="-1"><i>README</i></font><i>.win32</i> or perlwin32 for more details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The option to use an externally-supplied <code>crypt()</code>, or to build with no <code>crypt()</code> at all, has been removed. Perl supplies its own <code>crypt()</code> implementation for Windows, and the political situation that required this part of the distribution to sometimes be omitted is long gone. </p>
 </dd></dl>
<h2>Internal Changes</h2>
<h3>New APIs</h3>
<p> <i></i><font SIZE="-1"><i>CLONE_PARAMS</i></font><i> structure added to ease correct thread creation</i> </p>
<p> Modules that create threads should now create <code>&quot;CLONE_PARAMS&quot;</code> structures by calling the new function <code>Perl_clone_params_new()</code>, and free them with <code>Perl_clone_params_del()</code>. This will ensure compatibility with any future changes to the internals of the <code>&quot;CLONE_PARAMS&quot;</code> structure layout, and that it is correctly allocated and initialised. </p>
<p> <i>New parsing functions</i> </p>
<p> Several functions have been added for parsing Perl statements and expressions. These functions are meant to be used by <font SIZE="-1">XS</font> code invoked during Perl parsing, in a recursive-descent manner, to allow modules to augment the standard Perl syntax. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>parse_stmtseq()</code> parses a sequence of statements, up to closing brace or <font SIZE="-1">EOF.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>parse_fullstmt()</code> parses a complete Perl statement, including optional label. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>parse_barestmt()</code> parses a statement without a label. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>parse_block()</code> parses a code block. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>parse_label()</code> parses a statement label, separate from statements. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;parse_fullexpr()&quot;</code>, <code>&quot;parse_listexpr()&quot;</code>, <code>&quot;parse_termexpr()&quot;</code>, and <code>&quot;parse_arithexpr()&quot;</code> parse expressions at various precedence levels. </p>
 </dd></dl>
<p> <i>Hints hash </i><font SIZE="-1"><i>API</i></font><i></i> </p>
<p> A new C <font SIZE="-1">API</font> for introspecting the hinthash <code>&quot;%^H&quot;</code> at runtime has been added. See <code>&quot;cop_hints_2hv&quot;</code>, <code>&quot;cop_hints_fetchpvn&quot;</code>, <code>&quot;cop_hints_fetchpvs&quot;</code>, <code>&quot;cop_hints_fetchsv&quot;</code>, and <code>&quot;hv_copy_hints_hv&quot;</code> in perlapi for details. </p>
<p> A new, experimental <font SIZE="-1">API</font> has been added for accessing the internal structure that Perl uses for <code>&quot;%^H&quot;</code>. See the functions beginning with <code>&quot;cophh_&quot;</code> in perlapi. </p>
<p> <i>C interface to </i>caller()<i></i> </p>
<p> The <code>&quot;caller_cx&quot;</code> function has been added as an XSUB-writer&#8217;s equivalent of <code>caller()</code>. See perlapi for details. </p>
<p> <i>Custom per-subroutine check hooks</i> </p>
<p> <font SIZE="-1">XS</font> code in an extension module can now annotate a subroutine (whether implemented in <font SIZE="-1">XS</font> or in Perl) so that nominated <font SIZE="-1">XS</font> code will be called at compile time (specifically as part of op checking) to change the op tree of that subroutine. The compile-time check function (supplied by the extension module) can implement argument processing that can&#8217;t be expressed as a prototype, generate customised compile-time warnings, perform constant folding for a pure function, inline a subroutine consisting of sufficiently simple ops, replace the whole call with a custom op, and so on. This was previously all possible by hooking the <code>&quot;entersub&quot;</code> op checker, but the new mechanism makes it easy to tie the hook to a specific subroutine. See ``cv_set_call_checker&#8217;&#8216; in perlapi. </p>
<p> To help in writing custom check hooks, several subtasks within standard <code>&quot;entersub&quot;</code> op checking have been separated out and exposed in the <font SIZE="-1">API.</font> </p>
<p> <i>Improved support for custom OPs</i> </p>
<p> Custom ops can now be registered with the new <code>&quot;custom_op_register&quot;</code> C function and the <code>&quot;XOP&quot;</code> structure. This will make it easier to add new properties of custom ops in the future. Two new properties have been added already, <code>&quot;xop_class&quot;</code> and <code>&quot;xop_peep&quot;</code>. </p>
<p> <code>&quot;xop_class&quot;</code> is one of the OA_*OP constants. It allows B and other introspection mechanisms to work with custom ops that aren&#8217;t BASEOPs. <code>&quot;xop_peep&quot;</code> is a pointer to a function that will be called for ops of this type from <code>&quot;Perl_rpeep&quot;</code>. </p>
<p> See ``Custom Operators&#8217;&#8216; in perlguts and ``Custom Operators&#8217;&#8216; in perlapi for more detail. </p>
<p> The old <code>&quot;PL_custom_op_names&quot;</code>/<code>&quot;PL_custom_op_descs&quot;</code> interface is still supported but discouraged. </p>
<p> <i>Scope hooks</i> </p>
<p> It is now possible for <font SIZE="-1">XS</font> code to hook into Perl&#8217;s lexical scope mechanism at compile time, using the new <code>&quot;Perl_blockhook_register&quot;</code> function. See ``Compile-time scope hooks&#8217;&#8216; in perlguts. </p>
<p> <i>The recursive part of the peephole optimizer is now hookable</i> </p>
<p> In addition to <code>&quot;PL_peepp&quot;</code>, for hooking into the toplevel peephole optimizer, a <code>&quot;PL_rpeepp&quot;</code> is now available to hook into the optimizer recursing into side-chains of the optree. </p>
<p> <i>New non-magical variants of existing functions</i> </p>
<p> The following functions/macros have been added to the <font SIZE="-1">API.</font> The <code>*_nomg</code> macros are equivalent to their non-<code>&quot;_nomg&quot;</code> variants, except that they ignore get-magic. Those ending in <code>&quot;_flags&quot;</code> allow one to specify whether get-magic is processed. </p>
<pre><code>  sv_2bool_flags
  SvTRUE_nomg
  sv_2nv_flags
  SvNV_nomg
  sv_cmp_flags
  sv_cmp_locale_flags
  sv_eq_flags
  sv_collxfrm_flags
</code></pre>
<p> In some of these cases, the non-<code>&quot;_flags&quot;</code> functions have been replaced with wrappers around the new functions. </p>
<p> <i>pv/pvs/sv versions of existing functions</i> </p>
<p> Many functions ending with pvn now have equivalent <code>&quot;pv/pvs/sv&quot;</code> versions. </p>
<p> <i>List op-building functions</i> </p>
<p> List op-building functions have been added to the <font SIZE="-1">API.</font> See op_append_elem, op_append_list, and op_prepend_elem in perlapi. </p>
<p> <i></i>&quot;LINKLIST&quot;<i></i> </p>
<p> The <font SIZE="-1">LINKLIST</font> macro, part of op building that constructs the execution-order op chain, has been added to the <font SIZE="-1">API.</font> </p>
<p> <i>Localisation functions</i> </p>
<p> The <code>&quot;save_freeop&quot;</code>, <code>&quot;save_op&quot;</code>, <code>&quot;save_pushi32ptr&quot;</code> and <code>&quot;save_pushptrptr&quot;</code> functions have been added to the <font SIZE="-1">API.</font> </p>
<p> <i>Stash names</i> </p>
<p> A stash can now have a list of effective names in addition to its usual name. The first effective name can be accessed via the <code>&quot;HvENAME&quot;</code> macro, which is now the recommended name to use in <font SIZE="-1">MRO</font> linearisations (<code>&quot;HvNAME&quot;</code> being a fallback if there is no <code>&quot;HvENAME&quot;</code>). </p>
<p> These names are added and deleted via <code>&quot;hv_ename_add&quot;</code> and <code>&quot;hv_ename_delete&quot;</code>. These two functions are <i>not</i> part of the <font SIZE="-1">API.</font> </p>
<p> <i>New functions for finding and removing magic</i> </p>
<p> The <code>&quot;mg_findext()&quot;</code> and <code>&quot;sv_unmagicext()&quot;</code> functions have been added to the <font SIZE="-1">API.</font> They allow extension authors to find and remove magic attached to scalars based on both the magic type and the magic virtual table, similar to how <code>sv_magicext()</code> attaches magic of a certain type and with a given virtual table to a scalar. This eliminates the need for extensions to walk the list of <code>&quot;MAGIC&quot;</code> pointers of an <code>&quot;SV&quot;</code> to find the magic that belongs to them. </p>
<p> <i></i>&quot;find_rundefsv&quot;<i></i> </p>
<p> This function returns the <font SIZE="-1">SV</font> representing <code>$_</code>, whether it&#8217;s lexical or dynamic. </p>
<p> <i></i>&quot;Perl_croak_no_modify&quot;<i></i> </p>
<p> <code>Perl_croak_no_modify()</code> is short-hand for <code>&quot;Perl_croak(&quot;%s&quot;, PL_no_modify)&quot;</code>. </p>
<p> <i></i>&quot;PERL_STATIC_INLINE&quot;<i> define</i> </p>
<p> The <code>&quot;PERL_STATIC_INLINE&quot;</code> define has been added to provide the best-guess incantation to use for static inline functions, if the C compiler supports C99-style static inline. If it doesn&#8217;t, it&#8217;ll give a plain <code>&quot;static&quot;</code>. </p>
<p> <code>&quot;HAS_STATIC_INLINE&quot;</code> can be used to check if the compiler actually supports inline functions. </p>
<p> <i>New </i>&quot;pv_escape&quot;<i> option for hexadecimal escapes</i> </p>
<p> A new option, <code>&quot;PERL_PV_ESCAPE_NONASCII&quot;</code>, has been added to <code>&quot;pv_escape&quot;</code> to dump all characters above <font SIZE="-1">ASCII</font> in hexadecimal. Before, one could get all characters as hexadecimal or the Latin1 non-ASCII as octal. </p>
<p> <i></i>&quot;lex_start&quot;<i></i> </p>
<p> <code>&quot;lex_start&quot;</code> has been added to the <font SIZE="-1">API,</font> but is considered experimental. </p>
<p> <i></i>op_scope()<i> and </i>op_lvalue()<i></i> </p>
<p> The <code>op_scope()</code> and <code>op_lvalue()</code> functions have been added to the <font SIZE="-1">API,</font> but are considered experimental.  </p>
<font SIZE="-1"></font><h3>C API Changes</h3>
<p> <i></i>&quot;PERL_POLLUTE&quot;<i> has been removed</i> </p>
<p> The option to define <code>&quot;PERL_POLLUTE&quot;</code> to expose older 5.005 symbols for backwards compatibility has been removed. Its use was always discouraged, and MakeMaker contains a more specific escape hatch: </p>
<pre><code>    perl Makefile.PL POLLUTE=1
</code></pre>
<p> This can be used for modules that have not been upgraded to 5.6 naming conventions (and really should be completely obsolete by now). </p>
<p> <i>Check </i><font SIZE="-1"><i>API</i></font><i> compatibility when loading </i><font SIZE="-1"><i>XS</i></font><i> modules</i> </p>
<p> When Perl&#8217;s <font SIZE="-1">API</font> changes in incompatible ways (which usually happens between major releases), <font SIZE="-1">XS</font> modules compiled for previous versions of Perl will no longer work. They need to be recompiled against the new Perl. </p>
<p> The <code>&quot;XS_APIVERSION_BOOTCHECK&quot;</code> macro has been added to ensure that modules are recompiled and to prevent users from accidentally loading modules compiled for old perls into newer perls. That macro, which is called when loading every newly compiled extension, compares the <font SIZE="-1">API</font> version of the running perl with the version a module has been compiled for and raises an exception if they don&#8217;t match. </p>
<p> <i>Perl_fetch_cop_label</i> </p>
<p> The first argument of the C <font SIZE="-1">API</font> function <code>&quot;Perl_fetch_cop_label&quot;</code> has changed from <code>&quot;struct refcounted_he *&quot;</code> to <code>&quot;COP *&quot;</code>, to insulate the user from implementation details. </p>
<p> This <font SIZE="-1">API</font> function was marked as ``may change&#8217;&#8216;, and likely isn&#8217;t in use outside the core. (Neither an unpacked <font SIZE="-1">CPAN</font> nor Google&#8217;s codesearch finds any other references to it.) </p>
<p> <i></i>GvCV()<i> and </i>GvGP()<i> are no longer lvalues</i> </p>
<p> The new <code>GvCV_set()</code> and <code>GvGP_set()</code> macros are now provided to replace assignment to those two macros. </p>
<p> This allows a future commit to eliminate some backref magic between <font SIZE="-1">GV</font> and CVs, which will require complete control over assignment to the <code>&quot;gp_cv&quot;</code> slot. </p>
<p> <i></i>CvGV()<i> is no longer an lvalue</i> </p>
<p> Under some circumstances, the <code>CvGV()</code> field of a <font SIZE="-1">CV</font> is now reference-counted. To ensure consistent behaviour, direct assignment to it, for example <code>&quot;CvGV(cv) = gv&quot;</code> is now a compile-time error. A new macro, <code>&quot;CvGV_set(cv,gv)&quot;</code> has been introduced to run this operation safely. Note that modification of this field is not part of the public <font SIZE="-1">API,</font> regardless of this new macro (and despite its being listed in this section). </p>
<p> <i></i>CvSTASH()<i> is no longer an lvalue</i> </p>
<p> The <code>CvSTASH()</code> macro can now only be used as an rvalue. <code>CvSTASH_set()</code> has been added to replace assignment to <code>CvSTASH()</code>. This is to ensure that backreferences are handled properly. These macros are not part of the <font SIZE="-1">API.</font> </p>
<p> <i>Calling conventions for </i>&quot;newFOROP&quot;<i> and </i>&quot;newWHILEOP&quot;<i></i> </p>
<p> The way the parser handles labels has been cleaned up and refactored. As a result, the <code>newFOROP()</code> constructor function no longer takes a parameter stating what label is to go in the state op. </p>
<p> The <code>newWHILEOP()</code> and <code>newFOROP()</code> functions no longer accept a line number as a parameter. </p>
<p> <i>Flags passed to </i>&quot;uvuni_to_utf8_flags&quot;<i> and </i>&quot;utf8n_to_uvuni&quot;<i></i> </p>
<p> Some of the flags parameters to <code>uvuni_to_utf8_flags()</code> and <code>utf8n_to_uvuni()</code> have changed. This is a result of Perl&#8217;s now allowing internal storage and manipulation of code points that are problematic in some situations. Hence, the default actions for these functions has been complemented to allow these code points. The new flags are documented in perlapi. Code that requires the problematic code points to be rejected needs to change to use the new flags. Some flag names are retained for backward source compatibility, though they do nothing, as they are now the default. However the flags <code>&quot;UNICODE_ALLOW_FDD0&quot;</code>, <code>&quot;UNICODE_ALLOW_FFFF&quot;</code>, <code>&quot;UNICODE_ILLEGAL&quot;</code>, and <code>&quot;UNICODE_IS_ILLEGAL&quot;</code> have been removed, as they stem from a fundamentally broken model of how the Unicode non-character code points should be handled, which is now described in ``Non-character code points&#8217;&#8216; in perlunicode. See also the Unicode section under ``Selected Bug Fixes&#8217;&#8216;.  </p>
<h3>Deprecated C APIs</h3>
<dl>
<dt>&quot;Perl_ptr_table_clear&quot;</dt>
<dd> <p> <code>&quot;Perl_ptr_table_clear&quot;</code> is no longer part of Perl&#8217;s public <font SIZE="-1">API.</font> Calling it now generates a deprecation warning, and it will be removed in a future release. </p>
 </dd>
<dt>&quot;sv_compile_2op&quot;</dt>
<dd> <p> The <code>sv_compile_2op()</code> <font SIZE="-1">API</font> function is now deprecated. Searches suggest that nothing on <font SIZE="-1">CPAN</font> is using it, so this should have zero impact. </p>
<p> It attempted to provide an <font SIZE="-1">API</font> to compile code down to an optree, but failed to bind correctly to lexicals in the enclosing scope. It&#8217;s not possible to fix this problem within the constraints of its parameters and return value. </p>
 </dd>
<dt>&quot;find_rundefsvoffset&quot;</dt>
<dd> <p> The <code>&quot;find_rundefsvoffset&quot;</code> function has been deprecated. It appeared that its design was insufficient for reliably getting the lexical <code>$_</code> at run-time. </p>
<p> Use the new <code>&quot;find_rundefsv&quot;</code> function or the <code>&quot;UNDERBAR&quot;</code> macro instead. They directly return the right <font SIZE="-1">SV</font> representing <code>$_</code>, whether it&#8217;s lexical or dynamic. </p>
 </dd>
<dt>&quot;CALL_FPTR&quot; and &quot;CPERLscope&quot;</dt>
<dd> <p> Those are left from an old implementation of <code>&quot;MULTIPLICITY&quot;</code> using C<font SIZE="-2">++</font> objects, which was removed in Perl 5.8. Nowadays these macros do exactly nothing, so they shouldn&#8217;t be used anymore. </p>
<p> For compatibility, they are still defined for external <code>&quot;XS&quot;</code> code. Only extensions defining <code>&quot;PERL_CORE&quot;</code> must be updated now. </p>
 </dd></dl>
<h3>Other Internal Changes</h3>
<p> <i>Stack unwinding</i> </p>
<p> The protocol for unwinding the C stack at the last stage of a <code>&quot;die&quot;</code> has changed how it identifies the target stack frame. This now uses a separate variable <code>&quot;PL_restartjmpenv&quot;</code>, where previously it relied on the <code>&quot;blk_eval.cur_top_env&quot;</code> pointer in the <code>&quot;eval&quot;</code> context frame that has nominally just been discarded. This change means that code running during various stages of Perl-level unwinding no longer needs to take care to avoid destroying the ghost frame. </p>
<p> <i>Scope stack entries</i> </p>
<p> The format of entries on the scope stack has been changed, resulting in a reduction of memory usage of about 10%. In particular, the memory used by the scope stack to record each active lexical variable has been halved. </p>
<p> <i>Memory allocation for pointer tables</i> </p>
<p> Memory allocation for pointer tables has been changed. Previously <code>&quot;Perl_ptr_table_store&quot;</code> allocated memory from the same arena system as <code>&quot;SV&quot;</code> bodies and <code>&quot;HE&quot;</code>s, with freed memory remaining bound to those arenas until interpreter exit. Now it allocates memory from arenas private to the specific pointer table, and that memory is returned to the system when <code>&quot;Perl_ptr_table_free&quot;</code> is called. Additionally, allocation and release are both less <font SIZE="-1">CPU</font> intensive. </p>
<p> <i></i>&quot;UNDERBAR&quot;<i></i> </p>
<p> The <code>&quot;UNDERBAR&quot;</code> macro now calls <code>&quot;find_rundefsv&quot;</code>. <code>&quot;dUNDERBAR&quot;</code> is now a noop but should still be used to ensure past and future compatibility. </p>
<p> <i>String comparison routines renamed</i> </p>
<p> The <code>&quot;ibcmp_*&quot;</code> functions have been renamed and are now called <code>&quot;foldEQ&quot;</code>, <code>&quot;foldEQ_locale&quot;</code>, and <code>&quot;foldEQ_utf8&quot;</code>. The old names are still available as macros. </p>
<p> <i></i>&quot;chop&quot;<i> and </i>&quot;chomp&quot;<i> implementations merged</i> </p>
<p> The opcode bodies for <code>&quot;chop&quot;</code> and <code>&quot;chomp&quot;</code> and for <code>&quot;schop&quot;</code> and <code>&quot;schomp&quot;</code> have been merged. The implementation functions <code>Perl_do_chop()</code> and <code>Perl_do_chomp()</code>, never part of the public <font SIZE="-1">API,</font> have been merged and moved to a static function in <i>pp.c</i>. This shrinks the Perl binary slightly, and should not affect any code outside the core (unless it is relying on the order of side-effects when <code>&quot;chomp&quot;</code> is passed a <i>list</i> of values).  </p>
<h2>Selected Bug Fixes</h2>
<h3>I/O</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Perl no longer produces this warning: </p>
<pre><code>    $ perl -we 'open(my $f, &quot;&gt;&quot;, \my $x); binmode($f, &quot;scalar&quot;)'
    Use of uninitialized value in binmode at -e line 1.
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Opening a glob reference via <code>&quot;open($fh, &quot;&gt;&quot;, \*glob)&quot;</code> no longer causes the glob to be corrupted when the filehandle is printed to. This would cause Perl to crash whenever the glob&#8217;s contents were accessed [perl #77492]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO no longer crashes when called recursively, such as from a signal handler. Now it just leaks memory [perl #75556]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Most I/O functions were not warning for unopened handles unless the ``closed&#8217;&#8216; and ``unopened&#8217;&#8216; warnings categories were both enabled. Now only <code>&quot;use warnings &#8216;unopened&#8217;&quot;</code> is necessary to trigger these warnings, as had always been the intention. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> There have been several fixes to PerlIO layers: </p>
<p> When <code>&quot;binmode(FH, &quot;:crlf&quot;)&quot;</code> pushes the <code>&quot;:crlf&quot;</code> layer on top of the stack, it no longer enables crlf layers lower in the stack so as to avoid unexpected results [perl #38456]. </p>
<p> Opening a file in <code>&quot;:raw&quot;</code> mode now does what it advertises to do (first open the file, then <code>&quot;binmode&quot;</code> it), instead of simply leaving off the top layer [perl #80764]. </p>
<p> The three layers <code>&quot;:pop&quot;</code>, <code>&quot;:utf8&quot;</code>, and <code>&quot;:bytes&quot;</code> didn&#8217;t allow stacking when opening a file. For example this: </p>
<pre><code>    open(FH, &quot;&gt;:pop:perlio&quot;, &quot;some.file&quot;) or die $!;
</code></pre>
<p> would throw an ``Invalid argument&#8217;&#8216; error. This has been fixed in this release [perl #82484]. </p>
 </dd></dl>
<h3>Regular Expression Bug Fixes</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The regular expression engine no longer loops when matching <code>&quot;&quot;\N{LATIN SMALL LIGATURE FF}&quot; =~ /f+/i&quot;</code> and similar expressions [perl #72998] (5.12.1). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The trie runtime code should no longer allocate massive amounts of memory, fixing #74484. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Syntax errors in <code>&quot;(?{...})&quot;</code> blocks no longer cause panic messages [perl #2353]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A pattern like <code>&quot;(?:(o){2})?&quot;</code> no longer causes a ``panic&#8217;&#8216; error [perl #39233]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A fatal error in regular expressions containing <code>&quot;(.*?)&quot;</code> when processing <font SIZE="-1">UTF-8</font> data has been fixed [perl #75680] (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An erroneous regular expression engine optimisation that caused regex verbs like <code>*COMMIT</code> sometimes to be ignored has been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The regular expression bracketed character class <code>&quot;[\8\9]&quot;</code> was effectively the same as <code>&quot;[89\000]&quot;</code>, incorrectly matching a <font SIZE="-1">NULL</font> character. It also gave incorrect warnings that the <code>8</code> and <code>9</code> were ignored. Now <code>&quot;[\8\9]&quot;</code> is the same as <code>&quot;[89]&quot;</code> and gives legitimate warnings that <code>&quot;\8&quot;</code> and <code>&quot;\9&quot;</code> are unrecognized escape sequences, passed-through. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A regular expression match in the right-hand side of a global substitution (<code>&quot;s///g&quot;</code>) that is in the same scope will no longer cause match variables to have the wrong values on subsequent iterations. This can happen when an array or hash subscript is interpolated in the right-hand side, as in <code>&quot;s|(.)|@a{ print($1), /./ }|g&quot;</code> [perl #19078]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several cases in which characters in the Latin-1 non-ASCII range (0x80 to 0xFF) used not to match themselves, or used to match both a character class and its complement, have been fixed. For instance, U+00E2 could match both <code>&quot;\w&quot;</code> and <code>&quot;\W&quot;</code> [perl #78464] [perl #18281] [perl #60156]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Matching a Unicode character against an alternation containing characters that happened to match continuation bytes in the former&#8217;s <font SIZE="-1">UTF8</font> representation (like <code>&quot;qq{\x{30ab}} =~ /\xab|\xa9/&quot;</code>) would cause erroneous warnings [perl #70998]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The trie optimisation was not taking empty groups into account, preventing ``foo&#8217;&#8216; from matching <code>&quot;/\A(?:(?:)foo|bar|zot)\z/&quot;</code> [perl #78356]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A pattern containing a <code>&quot;+&quot;</code> inside a lookahead would sometimes cause an incorrect match failure in a global match (for example, <code>&quot;/(?=(\S+))/g&quot;</code>) [perl #68564]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A regular expression optimisation would sometimes cause a match with a <code>&quot;{n,m}&quot;</code> quantifier to fail when it should have matched [perl #79152]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Case-insensitive matching in regular expressions compiled under <code>&quot;use locale&quot;</code> now works much more sanely when the pattern or target string is internally encoded in <font SIZE="-1">UTF8.</font> Previously, under these conditions the localeness was completely lost. Now, code points above 255 are treated as Unicode, but code points between 0 and 255 are treated using the current locale rules, regardless of whether the pattern or the string is encoded in <font SIZE="-1">UTF8.</font> The few case-insensitive matches that cross the 255/256 boundary are not allowed. For example, 0xFF does not caselessly match the character at 0x178, <font SIZE="-1">LATIN CAPITAL LETTER Y WITH DIAERESIS,</font> because 0xFF may not be <font SIZE="-1">LATIN SMALL LETTER Y</font> in the current locale, and Perl has no way of knowing if that character even exists in the locale, much less what code point it is. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;(?|...)&quot;</code> regular expression construct no longer crashes if the final branch has more sets of capturing parentheses than any other branch. This was fixed in Perl 5.10.1 for the case of a single branch, but that fix did not take multiple branches into account [perl #84746]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A bug has been fixed in the implementation of <code>&quot;{...}&quot;</code> quantifiers in regular expressions that prevented the code block in <code>&quot;/((\w+)(?{ print $2 })){2}/&quot;</code> from seeing the <code>$2</code> sometimes [perl #84294]. </p>
 </dd></dl>
<h3>Syntax/Parsing Bugs</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;when (scalar) {...}&quot;</code> no longer crashes, but produces a syntax error [perl #74114] (5.12.1). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A label right before a string eval (<code>&quot;foo: eval $string&quot;</code>) no longer causes the label to be associated also with the first statement inside the eval [perl #74290] (5.12.1). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;no 5.13.2&quot;</code> form of <code>&quot;no&quot;</code> no longer tries to turn on features or pragmata (like strict) [perl #70075] (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;BEGIN {require 5.12.0}&quot;</code> now behaves as documented, rather than behaving identically to <code>&quot;use 5.12.0&quot;</code>. Previously, <code>&quot;require&quot;</code> in a <code>&quot;BEGIN&quot;</code> block was erroneously executing the <code>&quot;use feature &#8216;:5.12.0&#8217;&quot;</code> and <code>&quot;use strict&quot;</code> behaviour, which only <code>&quot;use&quot;</code> was documented to provide [perl #69050]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A regression introduced in Perl 5.12.0, making <code>&quot;my $x = 3; $x = length(undef)&quot;</code> result in <code>$x</code> set to <code>3</code> has been fixed. <code>$x</code> will now be <code>&quot;undef&quot;</code> [perl #85508] (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When strict ``refs&#8217;&#8216; mode is off, <code>&quot;%{...}&quot;</code> in rvalue context returns <code>&quot;undef&quot;</code> if its argument is undefined. An optimisation introduced in Perl 5.12.0 to make <code>&quot;keys %{...}&quot;</code> faster when used as a boolean did not take this into account, causing <code>&quot;keys %{+undef}&quot;</code> (and <code>&quot;keys %$foo&quot;</code> when <code>$foo</code> is undefined) to be an error, which it should be so in strict mode only [perl #81750]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Constant-folding used to cause </p>
<pre><code>  $text =~ ( 1 ? /phoo/ : /bear/)
</code></pre>
<p> to turn into </p>
<pre><code>  $text =~ /phoo/
</code></pre>
<p> at compile time. Now it correctly matches against <code>$_</code> [perl #20444]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Parsing Perl code (either with string <code>&quot;eval&quot;</code> or by loading modules) from within a <code>&quot;UNITCHECK&quot;</code> block no longer causes the interpreter to crash [perl #70614]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> String <code>&quot;eval&quot;</code>s no longer fail after 2 billion scopes have been compiled [perl #83364]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The parser no longer hangs when encountering certain Unicode characters, such as U+387 [perl #74022]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Defining a constant with the same name as one of Perl&#8217;s special blocks (like <code>&quot;INIT&quot;</code>) stopped working in 5.12.0, but has now been fixed [perl #78634]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A reference to a literal value used as a hash key (<code>$hash{\&quot;foo&quot;}</code>) used to be stringified, even if the hash was tied [perl #79178]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A closure containing an <code>&quot;if&quot;</code> statement followed by a constant or variable is no longer treated as a constant [perl #63540]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;state&quot;</code> can now be used with attributes. It used to mean the same thing as <code>&quot;my&quot;</code> if any attributes were present [perl #68658]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Expressions like <code>&quot;@$a &gt; 3&quot;</code> no longer cause <code>$a</code> to be mentioned in the ``Use of uninitialized value in numeric gt&#8217;&#8216; warning when <code>$a</code> is undefined (since it is not part of the <code>&quot;&gt;&quot;</code> expression, but the operand of the <code>&quot;@&quot;</code>) [perl #72090]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Accessing an element of a package array with a hard-coded number (as opposed to an arbitrary expression) would crash if the array did not exist. Usually the array would be autovivified during compilation, but typeglob manipulation could remove it, as in these two cases which used to crash: </p>
<pre><code>  *d = *a; print $d[0];
  undef *d; print $d[0];
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>-C</code> command-line option, when used on the shebang line, can now be followed by other options [perl #72434]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;B&quot;</code> module was returning <code>&quot;B::OP&quot;</code>s instead of <code>&quot;B::LOGOP&quot;</code>s for <code>&quot;entertry&quot;</code> [perl #80622]. This was due to a bug in the Perl core, not in <code>&quot;B&quot;</code> itself. </p>
 </dd></dl>
<h3>Stashes, Globs and Method Lookup</h3>
<p> Perl 5.10.0 introduced a new internal mechanism for caching MROs (method resolution orders, or lists of parent classes; aka ``isa&#8217;&#8216; caches) to make method lookup faster (so <code>@ISA</code> arrays would not have to be searched repeatedly). Unfortunately, this brought with it quite a few bugs. Almost all of these have been fixed now, along with a few MRO-related bugs that existed before 5.10.0: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The following used to have erratic effects on method resolution, because the ``isa&#8217;&#8216; caches were not reset or otherwise ended up listing the wrong classes. These have been fixed. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>Aliasing packages by assigning to globs [perl #77358]</dt>
<dd>  </dd>
<dt>Deleting packages by deleting their containing stash elements</dt>
<dd>  </dd>
<dt>Undefining the glob containing a package (&quot;undef *Foo::&quot;)</dt>
<dd>  </dd>
<dt>Undefining an <font SIZE="-1">ISA</font> glob (&quot;undef *Foo::ISA&quot;)</dt>
<dd>  </dd>
<dt>Deleting an <font SIZE="-1">ISA</font> stash element (&quot;delete $Foo::{ISA}&quot;)</dt>
<dd>  </dd>
<dt>Sharing @ISA arrays between classes (via &quot;*Foo::ISA = \@Bar::ISA&quot; or &quot;*Foo::ISA = *Bar::ISA&quot;) [perl #77238]</dt>
<dd>  </dd></dl>
</dl>
<dl>
<dd> <p> <code>&quot;undef *Foo::ISA&quot;</code> would even stop a new <code>@Foo::ISA</code> array from updating caches. </p>
 </dd></dl>
<dt>&bull;</dt>
<dd> <p> Typeglob assignments would crash if the glob&#8217;s stash no longer existed, so long as the glob assigned to were named <code>&quot;ISA&quot;</code> or the glob on either side of the assignment contained a subroutine. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PL_isarev&quot;</code>, which is accessible to Perl via <code>&quot;mro::get_isarev&quot;</code> is now updated properly when packages are deleted or removed from the <code>@ISA</code> of other classes. This allows many packages to be created and deleted without causing a memory leak [perl #75176]. </p>
 </dd></dl>
<p> In addition, various other bugs related to typeglobs and stashes have been fixed: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Some work has been done on the internal pointers that link between symbol tables (stashes), typeglobs, and subroutines. This has the effect that various edge cases related to deleting stashes or stash entries (for example, &lt;%FOO:: = ()&gt;), and complex typeglob or code-reference aliasing, will no longer crash the interpreter. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assigning a reference to a glob copy now assigns to a glob slot instead of overwriting the glob with a scalar [perl #1804] [perl #77508]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A bug when replacing the glob of a loop variable within the loop has been fixed [perl #21469]. This means the following code will no longer crash: </p>
<pre><code>    for $x (...) {
        *x = *y;
    }
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assigning a glob to a <font SIZE="-1">PVLV</font> used to convert it to a plain string. Now it works correctly, and a <font SIZE="-1">PVLV</font> can hold a glob. This would happen when a nonexistent hash or array element was passed to a subroutine: </p>
<pre><code>  sub { $_[0] = *foo }-&gt;($hash{key});
  # $_[0] would have been the string &quot;*main::foo&quot;
</code></pre>
<p> It also happened when a glob was assigned to, or returned from, an element of a tied array or hash [perl #36051]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When trying to report <code>&quot;Use of uninitialized value $Foo::BAR&quot;</code>, crashes could occur if the glob holding the global variable in question had been detached from its original stash by, for example, <code>&quot;delete $::{&quot;Foo::&quot;}&quot;</code>. This has been fixed by disabling the reporting of variable names in those cases. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> During the restoration of a localised typeglob on scope exit, any destructors called as a result would be able to see the typeglob in an inconsistent state, containing freed entries, which could result in a crash. This would affect code like this: </p>
<pre><code>  local *@;
  eval { die bless [] }; # puts an object in $@
  sub DESTROY {
    local $@; # boom
  }
</code></pre>
<p> Now the glob entries are cleared before any destructors are called. This also means that destructors can vivify entries in the glob. So Perl tries again and, if the entries are re-created too many times, dies with a ``panic: gp_free ...&#8216;&#8216; error message. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If a typeglob is freed while a subroutine attached to it is still referenced elsewhere, the subroutine is renamed to <code>&quot;__ANON__&quot;</code> in the same package, unless the package has been undefined, in which case the <code>&quot;__ANON__&quot;</code> package is used. This could cause packages to be sometimes autovivified, such as if the package had been deleted. Now this no longer occurs. The <code>&quot;__ANON__&quot;</code> package is also now used when the original package is no longer attached to the symbol table. This avoids memory leaks in some cases [perl #87664]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Subroutines and package variables inside a package whose name ends with <code>&quot;::&quot;</code> can now be accessed with a fully qualified name. </p>
 </dd></dl>
<h3>Unicode</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> What has become known as ``the Unicode Bug&#8217;&#8216; is almost completely resolved in this release. Under <code>&quot;use feature &#8216;unicode_strings&#8217;&quot;</code> (which is automatically selected by <code>&quot;use 5.012&quot;</code> and above), the internal storage format of a string no longer affects the external semantics. [perl #58182]. </p>
<p> There are two known exceptions: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>1.</dt>
<dd> <p> The now-deprecated, user-defined case-changing functions require utf8-encoded strings to operate. The <font SIZE="-1">CPAN</font> module Unicode::Casing has been written to replace this feature without its drawbacks, and the feature is scheduled to be removed in 5.16. </p>
 </dd>
<dt>2.</dt>
<dd> <p> <code>quotemeta()</code> (and its in-line equivalent <code>&quot;\Q&quot;</code>) can also give different results depending on whether a string is encoded in <font SIZE="-1">UTF-8.</font> See ``The &#8216;&#8216;Unicode Bug&quot;&quot; in perlunicode. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Handling of Unicode non-character code points has changed. Previously they were mostly considered illegal, except that in some place only one of the 66 of them was known. The Unicode Standard considers them all legal, but forbids their ``open interchange&#8217;&#8216;. This is part of the change to allow internal use of any code point (see ``Core Enhancements&#8217;&#8216;). Together, these changes resolve [perl #38722], [perl #51918], [perl #51936], and [perl #63446]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Case-insensitive <code>&quot;/i&quot;</code> regular expression matching of Unicode characters that match multiple characters now works much more as intended. For example </p>
<pre><code> &quot;\N{LATIN SMALL LIGATURE FFI}&quot; =~ /ffi/ui
</code></pre>
<p> and </p>
<pre><code> &quot;ffi&quot; =~ /\N{LATIN SMALL LIGATURE FFI}/ui
</code></pre>
<p> are both true. Previously, there were many bugs with this feature. What hasn&#8217;t been fixed are the places where the pattern contains the multiple characters, but the characters are split up by other things, such as in </p>
<pre><code> &quot;\N{LATIN SMALL LIGATURE FFI}&quot; =~ /(f)(f)i/ui
</code></pre>
<p> or </p>
<pre><code> &quot;\N{LATIN SMALL LIGATURE FFI}&quot; =~ /ffi*/ui
</code></pre>
<p> or </p>
<pre><code> &quot;\N{LATIN SMALL LIGATURE FFI}&quot; =~ /[a-f][f-m][g-z]/ui
</code></pre>
<p> None of these match. </p>
<p> Also, this matching doesn&#8217;t fully conform to the current Unicode Standard, which asks that the matching be made upon the <font SIZE="-1">NFD</font> (Normalization Form Decomposed) of the text. However, as of this writing (April 2010), the Unicode Standard is currently in flux about what they will recommend doing with regard in such scenarios. It may be that they will throw out the whole concept of multi-character matches. [perl #71736]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Naming a deprecated character in <code>&quot;\N{</code>NAME <code>}&quot;</code> no longer leaks memory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> We fixed a bug that could cause <code>&quot;\N{</code>NAME <code>}&quot;</code> constructs followed by a single <code>&quot;.&quot;</code> to be parsed incorrectly [perl #74978] (5.12.1). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;chop&quot;</code> now correctly handles characters above <code>&quot;\x{7fffffff}&quot;</code> [perl #73246]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Passing to <code>&quot;index&quot;</code> an offset beyond the end of the string when the string is encoded internally in <font SIZE="-1">UTF8</font> no longer causes panics [perl #75898]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>warn()</code> and <code>die()</code> now respect utf8-encoded scalars [perl #45549]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Sometimes the <font SIZE="-1">UTF8</font> length cache would not be reset on a value returned by substr, causing <code>&quot;length(substr($uni_string, ...))&quot;</code> to give wrong answers. With <code>&quot;${^UTF8CACHE}&quot;</code> set to -1, it would also produce a ``panic&#8217;&#8216; error message [perl #77692]. </p>
 </dd></dl>
<h3>Ties, Overloading and Other Magic</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Overloading now works properly in conjunction with tied variables. What formerly happened was that most ops checked their arguments for overloading <i>before</i> checking for magic, so for example an overloaded object returned by a tied array access would usually be treated as not overloaded [<font SIZE="-1">RT</font> #57012]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various instances of magic (like tie methods) being called on tied variables too many or too few times have been fixed: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;$tied-&gt;()&quot;</code> did not always call <font SIZE="-1">FETCH</font> [perl #8438]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Filetest operators and <code>&quot;y///&quot;</code> and <code>&quot;tr///&quot;</code> were calling <font SIZE="-1">FETCH</font> too many times. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;=&quot;</code> operator used to ignore magic on its right-hand side if the scalar happened to hold a typeglob (if a typeglob was the last thing returned from or assigned to a tied scalar) [perl #77498]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Dereference operators used to ignore magic if the argument was a reference already (such as from a previous <font SIZE="-1">FETCH</font>) [perl #72144]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;splice&quot;</code> now calls set-magic (so changes made by <code>&quot;splice @ISA&quot;</code> are respected by method calls) [perl #78400]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In-memory files created by <code>&quot;open($fh, &quot;&gt;&quot;, \$buffer)&quot;</code> were not calling <font SIZE="-1">FETCH/STORE</font> at all [perl #43789] (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>utf8::is_utf8()</code> now respects get-magic (like <code>$1</code>) (5.12.1). </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Non-commutative binary operators used to swap their operands if the same tied scalar was used for both operands and returned a different value for each <font SIZE="-1">FETCH.</font> For instance, if <code>$t</code> returned 2 the first time and 3 the second, then <code>&quot;$t/$t&quot;</code> would evaluate to 1.5. This has been fixed [perl #87708]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> String <code>&quot;eval&quot;</code> now detects taintedness of overloaded or tied arguments [perl #75716]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> String <code>&quot;eval&quot;</code> and regular expression matches against objects with string overloading no longer cause memory corruption or crashes [perl #77084]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> readline now honors <code>&quot;&lt;&gt;&quot;</code> overloading on tied arguments. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;&lt;expr&gt;&quot;</code> always respects overloading now if the expression is overloaded. </p>
<p> Because ``&lt;&gt; as glob&#8217;&#8216; was parsed differently from ``&lt;&gt; as filehandle&#8217;&#8216; from 5.6 onwards, something like <code>&quot;&lt;$foo[0]&gt;&quot;</code> did not handle overloading, even if <code>$foo[0]</code> was an overloaded object. This was contrary to the documentation for overload, and meant that <code>&quot;&lt;&gt;&quot;</code> could not be used as a general overloaded iterator operator. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The fallback behaviour of overloading on binary operators was asymmetric [perl #71286]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Magic applied to variables in the main package no longer affects other packages. See ``Magic variables outside the main package&#8217;&#8216; above [perl #76138]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Sometimes magic (ties, taintedness, etc.) attached to variables could cause an object to last longer than it should, or cause a crash if a tied variable were freed from within a tie method. These have been fixed [perl #81230]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">DESTROY</font> methods of objects implementing ties are no longer able to crash by accessing the tied variable through a weak reference [perl #86328]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a regression of <code>kill()</code> when a match variable is used for the process <font SIZE="-1">ID</font> to kill [perl #75812]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$AUTOLOAD</code> used to remain tainted forever if it ever became tainted. Now it is correctly untainted if an autoloaded method is called and the method name was not tainted. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sprintf&quot;</code> now dies when passed a tainted scalar for the format. It did already die for arbitrary expressions, but not for simple scalars [perl #82250]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;lc&quot;</code>, <code>&quot;uc&quot;</code>, <code>&quot;lcfirst&quot;</code>, and <code>&quot;ucfirst&quot;</code> no longer return untainted strings when the argument is tainted. This has been broken since perl 5.8.9 [perl #87336]. </p>
 </dd></dl>
<h3>The Debugger</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The Perl debugger now also works in taint mode [perl #76872]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Subroutine redefinition works once more in the debugger [perl #48332]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When <code>-d</code> is used on the shebang (<code>&quot;#!&quot;</code>) line, the debugger now has access to the lines of the main program. In the past, this sometimes worked and sometimes did not, depending on the order in which things happened to be arranged in memory [perl #71806]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A possible memory leak when using <code>caller()</code> to set <code>@DB::args</code> has been fixed (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl no longer stomps on <code>$DB::single</code>, <code>$DB::trace</code>, and <code>$DB::signal</code> if these variables already have values when <code>$^P</code> is assigned to [perl #72422]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;#line&quot;</code> directives in string evals were not properly updating the arrays of lines of code (<code>&quot;@{&quot;_&lt; ...&quot;}&quot;</code>) that the debugger (or any debugging or profiling module) uses. In threaded builds, they were not being updated at all. In non-threaded builds, the line number was ignored, so any change to the existing line number would cause the lines to be misnumbered [perl #79442]. </p>
 </dd></dl>
<h3>Threads</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Perl no longer accidentally clones lexicals in scope within active stack frames in the parent when creating a child thread [perl #73086]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several memory leaks in cloning and freeing threaded Perl interpreters have been fixed [perl #77352]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Creating a new thread when directory handles were open used to cause a crash, because the handles were not cloned, but simply passed to the new thread, resulting in a double free. </p>
<p> Now directory handles are cloned properly on Windows and on systems that have a <code>&quot;fchdir&quot;</code> function. On other systems, new threads simply do not inherit directory handles from their parent threads [perl #75154]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The typeglob <code>&quot;*,&quot;</code>, which holds the scalar variable <code>$,</code> (output field separator), had the wrong reference count in child threads. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> [perl #78494] When pipes are shared between threads, the <code>&quot;close&quot;</code> function (and any implicit close, such as on thread exit) no longer blocks. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now does a timely cleanup of SVs that are cloned into a new thread but then discovered to be orphaned (that is, their owners are <i>not</i> cloned). This eliminates several ``scalars leaked&#8217;&#8216; warnings when joining threads. </p>
 </dd></dl>
<h3>Scoping and Subroutines</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Lvalue subroutines are again able to return copy-on-write scalars. This had been broken since version 5.10.0 [perl #75656] (5.12.3). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;require&quot;</code> no longer causes <code>&quot;caller&quot;</code> to return the wrong file name for the scope that called <code>&quot;require&quot;</code> and other scopes higher up that had the same file name [perl #68712]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sort&quot;</code> with a <code>&quot;($$)&quot;</code>-prototyped comparison routine used to cause the value of <code>@_</code> to leak out of the sort. Taking a reference to <code>@_</code> within the sorting routine could cause a crash [perl #72334]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Match variables (like <code>$1</code>) no longer persist between calls to a sort subroutine [perl #76026]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Iterating with <code>&quot;foreach&quot;</code> over an array returned by an lvalue sub now works [perl #23790]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$@</code> is now localised during calls to <code>&quot;binmode&quot;</code> to prevent action at a distance [perl #78844]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calling a closure prototype (what is passed to an attribute handler for a closure) now results in a ``Closure prototype called&#8217;&#8216; error message instead of a crash [perl #68560]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Mentioning a read-only lexical variable from the enclosing scope in a string <code>&quot;eval&quot;</code> no longer causes the variable to become writable [perl #19135]. </p>
 </dd></dl>
<h3>Signals</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Within signal handlers, <code>$!</code> is now implicitly localized. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CHLD</font> signals are no longer unblocked after a signal handler is called if they were blocked before by <code>&quot;POSIX::sigprocmask&quot;</code> [perl #82040]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A signal handler called within a signal handler could cause leaks or double-frees. Now fixed [perl #76248]. </p>
 </dd></dl>
<h3>Miscellaneous Memory Leaks</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Several memory leaks when loading <font SIZE="-1">XS</font> modules were fixed (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>substr()</code>, <code>pos()</code>, <code>keys()</code>, and <code>vec()</code> could, when used in combination with lvalues, result in leaking the scalar value they operate on, and cause its destruction to happen too late. This has now been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The postincrement and postdecrement operators, <code>&quot;++&quot;</code> and <code>&quot;--&quot;</code>, used to cause leaks when used on references. This has now been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Nested <code>&quot;map&quot;</code> and <code>&quot;grep&quot;</code> blocks no longer leak memory when processing large lists [perl #48004]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;use </code>VERSION <code>&quot;</code> and <code>&quot;no </code>VERSION <code>&quot;</code> no longer leak memory [perl #78436] [perl #69050]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;.=&quot;</code> followed by <code>&quot;&lt;&gt;&quot;</code> or <code>&quot;readline&quot;</code> would leak memory if <code>$/</code> contained characters beyond the octet range and the scalar assigned to happened to be encoded as <font SIZE="-1">UTF8</font> internally [perl #72246]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;eval &#8216;BEGIN{die}&#8216;&quot;</code> no longer leaks memory on non-threaded builds. </p>
 </dd></dl>
<h3>Memory Corruption and Crashes</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>glob()</code> no longer crashes when <code>%File::Glob::</code> is empty and <code>&quot;CORE::GLOBAL::glob&quot;</code> isn&#8217;t present [perl #75464] (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>readline()</code> has been fixed when interrupted by signals so it no longer returns the ``same thing&#8217;&#8216; as before or random memory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When assigning a list with duplicated keys to a hash, the assignment used to return garbage and/or freed values: </p>
<pre><code>    @a = %h = (list with some duplicate keys);
</code></pre>
<p> This has now been fixed [perl #31865]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The mechanism for freeing objects in globs used to leave dangling pointers to freed SVs, meaning Perl users could see corrupted state during destruction. </p>
<p> Perl now frees only the affected slots of the <font SIZE="-1">GV,</font> rather than freeing the <font SIZE="-1">GV</font> itself. This makes sure that there are no dangling refs or corrupted state during destruction. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The interpreter no longer crashes when freeing deeply-nested arrays of arrays. Hashes have not been fixed yet [perl #44225]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Concatenating long strings under <code>&quot;use encoding&quot;</code> no longer causes Perl to crash [perl #78674]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calling <code>&quot;-&gt;import&quot;</code> on a class lacking an import method could corrupt the stack, resulting in strange behaviour. For instance, </p>
<pre><code>  push @a, &quot;foo&quot;, $b = bar-&gt;import;
</code></pre>
<p> would assign ``foo&#8217;&#8216; to <code>$b</code> [perl #63790]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;recv&quot;</code> function could crash when called with the <font SIZE="-1">MSG_TRUNC</font> flag [perl #75082]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;formline&quot;</code> no longer crashes when passed a tainted format picture. It also taints <code>$^A</code> now if its arguments are tainted [perl #79138]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A bug in how we process filetest operations could cause a segfault. Filetests don&#8217;t always expect an op on the stack, so we now use TOPs only if we&#8217;re sure that we&#8217;re not <code>&quot;stat&quot;</code>ing the <code>&quot;_&quot;</code> filehandle. This is indicated by <code>&quot;OPf_KIDS&quot;</code> (as checked in ck_ftst) [perl #74542] (5.12.1). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>unpack()</code> now handles scalar context correctly for <code>%32H</code> and <code>%32u</code>, fixing a potential crash. <code>split()</code> would crash because the third item on the stack wasn&#8217;t the regular expression it expected. <code>&quot;unpack(&quot;%2H&quot;, ...)&quot;</code> would return both the unpacked result and the checksum on the stack, as would <code>&quot;unpack(&quot;%2u&quot;, ...)&quot;</code> [perl #73814] (5.12.2). </p>
 </dd></dl>
<h3>Fixes to Various Perl Operators</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;&amp;&quot;</code>, <code>&quot;|&quot;</code>, and <code>&quot;^&quot;</code> bitwise operators no longer coerce read-only arguments [perl #20661]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Stringifying a scalar containing ``-0.0&#8217;&#8216; no longer has the effect of turning false into true [perl #45133]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some numeric operators were converting integers to floating point, resulting in loss of precision on 64-bit platforms [perl #77456]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>sprintf()</code> was ignoring locales when called with constant arguments [perl #78632]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Combining the vector (<code>%v</code>) flag and dynamic precision would cause <code>&quot;sprintf&quot;</code> to confuse the order of its arguments, making it treat the string as the precision and vice-versa [perl #83194]. </p>
 </dd></dl>
<font SIZE="-1"></font><h3>Bugs Relating to the C API</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The C-level <code>&quot;lex_stuff_pvn&quot;</code> function would sometimes cause a spurious syntax error on the last line of the file if it lacked a final semicolon [perl #74006] (5.12.1). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;eval_sv&quot;</code> and <code>&quot;eval_pv&quot;</code> C functions now set <code>$@</code> correctly when there is a syntax error and no <code>&quot;G_KEEPERR&quot;</code> flag, and never set it if the <code>&quot;G_KEEPERR&quot;</code> flag is present [perl #3719]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">XS</font> multicall <font SIZE="-1">API</font> no longer causes subroutines to lose reference counts if called via the multicall interface from within those very subroutines. This affects modules like List::Util. Calling one of its functions with an active subroutine as the first argument could cause a crash [perl #78070]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;SvPVbyte&quot;</code> function available to <font SIZE="-1">XS</font> modules now calls magic before downgrading the <font SIZE="-1">SV,</font> to avoid warnings about wide characters [perl #72398]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ref types in the typemap for <font SIZE="-1">XS</font> bindings now support magical variables [perl #72684]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sv_catsv_flags&quot;</code> no longer calls <code>&quot;mg_get&quot;</code> on its second argument (the source string) if the flags passed to it do not include <font SIZE="-1">SV_GMAGIC.</font> So it now matches the documentation. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;my_strftime&quot;</code> no longer leaks memory. This fixes a memory leak in <code>&quot;POSIX::strftime&quot;</code> [perl #73520]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i></i><font SIZE="-1"><i>XSUB</i></font><i>.h</i> now correctly redefines fgets under <font SIZE="-1">PERL_IMPLICIT_SYS</font> [perl #55049] (5.12.1). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">XS</font> code using <code>fputc()</code> or <code>fputs()</code> on Windows could cause an error due to their arguments being swapped [perl #72704] (5.12.1). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A possible segfault in the <code>&quot;T_PTROBJ&quot;</code> default typemap has been fixed (5.12.2). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A bug that could cause ``Unknown error&#8217;&#8216; messages when <code>&quot;call_sv(code, G_EVAL)&quot;</code> is called from an <font SIZE="-1">XS</font> destructor has been fixed (5.12.2). </p>
 </dd></dl>
<h2>Known Problems</h2>
<p> This is a list of significant unresolved issues which are regressions from earlier versions of Perl or which affect widely-used <font SIZE="-1">CPAN</font> modules. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;List::Util::first&quot;</code> misbehaves in the presence of a lexical <code>$_</code> (typically introduced by <code>&quot;my $_&quot;</code> or implicitly by <code>&quot;given&quot;</code>). The variable that gets set for each iteration is the package variable <code>$_</code>, not the lexical <code>$_</code>. </p>
<p> A similar issue may occur in other modules that provide functions which take a block as their first argument, like </p>
<pre><code>    foo { ... $_ ...} list
</code></pre>
<p> See also: &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=67694">http://rt.perl.org/rt3/Public/Bug/Display.html?id=67694</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>readline()</code> returns an empty string instead of a cached previous value when it is interrupted by a signal </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The changes in prototype handling break Switch. A patch has been sent upstream and will hopefully appear on <font SIZE="-1">CPAN</font> soon. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The upgrade to <i>ExtUtils-MakeMaker-6.57_05</i> has caused some tests in the <i>Module-Install</i> distribution on <font SIZE="-1">CPAN</font> to fail. (Specifically, <i>02_mymeta.t</i> tests 5 and 21; <i>18_all_from.t</i> tests 6 and 15; <i>19_authors.t</i> tests 5, 13, 21, and 29; and <i>20_authors_with_special_characters.t</i> tests 6, 15, and 23 in version 1.00 of that distribution now fail.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On <font SIZE="-1">VMS,</font> <code>&quot;Time::HiRes&quot;</code> tests will fail due to a bug in the <font SIZE="-1">CRTL</font>&#8216;s implementation of <code>&quot;setitimer&quot;</code>: previous timer values would be cleared if a timer expired but not if the timer was reset before expiring. <font SIZE="-1">HP</font> OpenVMS Engineering have corrected the problem and will release a patch in due course (Quix case # <font SIZE="-1">QXCM1001115136</font>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On <font SIZE="-1">VMS,</font> there were a handful of <code>&quot;Module::Build&quot;</code> test failures we didn&#8217;t get to before the release; please watch <font SIZE="-1">CPAN</font> for updates. </p>
 </dd></dl>
<h2>Errata</h2>
<code></code><code></code><code></code><h3>keys() , values() , and each() work on arrays</h3>
<p> You can now use the <code>keys()</code>, <code>values()</code>, and <code>each()</code> builtins on arrays; previously you could use them only on hashes. See perlfunc for details. This is actually a change introduced in perl 5.12.0, but it was missed from that release&#8217;s perl5120delta.  </p>
<code></code><h3>split() and @_</h3>
<p> <code>split()</code> no longer modifies <code>@_</code> when called in scalar or void context. In void context it now produces a ``Useless use of split&#8217;&#8216; warning. This was also a perl 5.12.0 change that missed the perldelta.  </p>
<h2>Obituary</h2>
<p> Randy Kobes, creator of <a rel="nofollow" href="http://kobesearch.cpan.org/">http://kobesearch.cpan.org/</a> and contributor/maintainer to several core Perl toolchain modules, passed away on September 18, 2010 after a battle with lung cancer. The community was richer for his involvement. He will be missed.  </p>
<h2>Acknowledgements</h2>
<p> Perl 5.14.0 represents one year of development since Perl 5.12.0 and contains nearly 550,000 lines of changes across nearly 3,000 files from 150 authors and committers. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.14.0: </p>
<p> Aaron Crane, Abhijit Menon-Sen, Abigail, Ævar Arnfjörð Bjarmason, Alastair Douglas, Alexander Alekseev, Alexander Hartmaier, Alexandr Ciornii, Alex Davies, Alex Vandiver, Ali Polatel, Allen Smith, Andreas König, Andrew Rodland, Andy Armstrong, Andy Dougherty, Aristotle Pagaltzis, Arkturuz, Arvan, A. Sinan Unur, Ben Morrow, Bo Lindbergh, Boris Ratner, Brad Gilbert, Bram, brian d foy, Brian Phillips, Casey West, Charles Bailey, Chas. Owens, Chip Salzenberg, Chris &#8216;BinGOs&#8217; Williams, chromatic, Craig A. Berry, Curtis Jewell, Dagfinn Ilmari Mannsåker, Dan Dascalescu, Dave Rolsky, David Caldwell, David Cantrell, David Golden, David Leadbeater, David Mitchell, David Wheeler, Eric Brine, Father Chrysostomos, Fingle Nark, Florian Ragwitz, Frank Wiegand, Franz Fasching, Gene Sullivan, George Greer, Gerard Goossen, Gisle Aas, Goro Fuji, Grant McLean, gregor herrmann, H.Merijn Brand, Hongwen Qiu, Hugo van der Sanden, Ian Goodacre, James E Keenan, James Mastros, Jan Dubois, Jay Hannah, Jerry D. Hedden, Jesse Vincent, Jim Cromie, Jirka Hruška, John Peacock, Joshua ben Jore, Joshua Pritikin, Karl Williamson, Kevin Ryde, kmx, Lars Dɪᴇᴄᴋᴏᴡ 迪拉斯, Larwan Berke, Leon Brocard, Leon Timmermans, Lubomir Rintel, Lukas Mai, Maik Hentsche, Marty Pauley, Marvin Humphrey, Matt Johnson, Matt S Trout, Max Maischein, Michael Breen, Michael Fig, Michael G Schwern, Michael Parker, Michael Stevens, Michael Witten, Mike Kelly, Moritz Lenz, Nicholas Clark, Nick Cleaton, Nick Johnston, Nicolas Kaiser, Niko Tyni, Noirin Shirley, Nuno Carvalho, Paul Evans, Paul Green, Paul Johnson, Paul Marquess, Peter J. Holzer, Peter John Acklam, Peter Martini, Philippe Bruhat (BooK), Piotr Fusik, Rafael Garcia-Suarez, Rainer Tammer, Reini Urban, Renee Baecker, Ricardo Signes, Richard Möhn, Richard Soderberg, Rob Hoelz, Robin Barker, Ruslan Zakirov, Salvador Fandiño, Salvador Ortiz Garcia, Shlomi Fish, Sinan Unur, Sisyphus, Slaven Rezic, Steffen Müller, Steve Hay, Steven Schubiger, Steve Peters, Sullivan Beck, Tatsuhiko Miyagawa, Tim Bunce, Todd Rinaldo, Tom Christiansen, Tom Hukins, Tony Cook, Tye McQueen, Vadim Konovalov, Vernon Lyon, Vincent Pit, Walt Mankowski, Wolfram Humann, Yves Orton, Zefram, and Zsbán Ambrus. </p>
<p> This is woefully incomplete as it&#8217;s automatically generated from version control history. In particular, it doesn&#8217;t include the names of the (very much appreciated) contributors who reported issues in previous versions of Perl that helped make Perl 5.14.0 better. For a more complete list of all of Perl&#8217;s historical contributors, please see the <code>&quot;AUTHORS&quot;</code> file in the Perl 5.14.0 distribution. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the Perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who are able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please use this address for security issues in the Perl core <i>only</i>, not for modules independently distributed on <font SIZE="-1">CPAN.</font>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
