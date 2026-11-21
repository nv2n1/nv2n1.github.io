---

title: "perl5220delta(1)"
name: "perl5220delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5220delta/"
description: "perl5220delta – what is new for perl v5.22.0"
---

<p> This document describes differences between the 5.20.0 release and the 5.22.0 release. </p>
<p> If you are upgrading from an earlier release such as 5.18.0, first read perl5200delta, which describes differences between 5.18.0 and 5.20.0.</p>
<h2>Core Enhancements</h2>
<h3>New bitwise operators</h3>
<p> A new experimental facility has been added that makes the four standard bitwise operators (<tt>&quot;&amp; | ^ ~&quot;</tt>) treat their operands consistently as numbers, and introduces four new dotted operators (<tt>&quot;&amp;. |. ^. ~.&quot;</tt>) that treat their operands consistently as strings. The same applies to the assignment variants (<tt>&quot;&amp;= |= ^= &amp;.= |.= ^.=&quot;</tt>). </p>
<p> To use this, enable the &#8220;bitwise&#8221; feature and disable the &#8220;experimental::bitwise&#8221; warnings category. See &#8220;Bitwise String Operators&#8221; in perlop for details. [perl #123466] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123466">https://rt.perl.org/Ticket/Display.html?id=123466</a>&gt;.</p>
<h3>New double-diamond operator</h3>
<p> <tt>&quot;&lt;&lt;&gt;&gt;&quot;</tt> is like <tt>&quot;&lt;&gt;&quot;</tt> but uses three-argument <tt>&quot;open&quot;</tt> to open each file in <tt>@ARGV</tt>. This means that each element of <tt>@ARGV</tt> will be treated as an actual file name, and <tt>&quot;|foo&quot;</tt> won&#8217;t be treated as a pipe open.</p>
<h3>New  boundaries in regular expressions</h3>
<p> <i></i>&quot;qr/{gcb}/&quot;<i></i> </p>
<p> <tt>&quot;gcb&quot;</tt> stands for Grapheme Cluster Boundary. It is a Unicode property that finds the boundary between sequences of characters that look like a single character to a native speaker of a language. Perl has long had the ability to deal with these through the <tt>&quot;\X&quot;</tt> regular escape sequence. Now, there is an alternative way of handling these. See &#8220;{}, , \B{}, \B&#8221; in perlrebackslash for details. </p>
<p> <i></i>&quot;qr/{wb}/&quot;<i></i> </p>
<p> <tt>&quot;wb&quot;</tt> stands for Word Boundary. It is a Unicode property that finds the boundary between words. This is similar to the plain <tt>&quot;&quot;</tt> (without braces) but is more suitable for natural language processing. It knows, for example, that apostrophes can occur in the middle of words. See &#8220;{}, , \B{}, \B&#8221; in perlrebackslash for details. </p>
<p> <i></i>&quot;qr/{sb}/&quot;<i></i> </p>
<p> <tt>&quot;sb&quot;</tt> stands for Sentence Boundary. It is a Unicode property to aid in parsing natural language sentences. See &#8220;{}, , \B{}, \B&#8221; in perlrebackslash for details.</p>
<h3>Non-Capturing Regular Expression Flag</h3>
<p> Regular expressions now support a <tt>&quot;/n&quot;</tt> flag that disables capturing and filling in <tt>$1</tt>, <tt>$2</tt>, etc inside of groups: </p>
<pre>
  &quot;hello&quot; =~ /(hi|hello)/n; # $1 is not set
</pre>
<p> This is equivalent to putting <tt>&quot;?:&quot;</tt> at the beginning of every capturing group. </p>
<p> See &#8220;n&#8221; in perlre for more information.</p>
<h3>use re &#8216;strict&#8217;</h3>
<p> This applies stricter syntax rules to regular expression patterns compiled within its scope. This will hopefully alert you to typos and other unintentional behavior that backwards-compatibility issues prevent us from reporting in normal regular expression compilations. Because the behavior of this is subject to change in future Perl releases as we gain experience, using this pragma will raise a warning of category <tt>&quot;experimental::re_strict&quot;</tt>. See &#8216;strict&#8217; in re.</p>
<h3>Unicode 7.0 (with correction) is now supported</h3>
<p> For details on what is in this release, see &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode7.0.0/">http://www.unicode.org/versions/Unicode7.0.0/</a>&gt;. The version of Unicode 7.0 that comes with Perl includes a correction dealing with glyph shaping in Arabic (see &lt;<a rel="nofollow" href="http://www.unicode.org/errata/#current_errata">http://www.unicode.org/errata/#current_errata</a>&gt;).</p>
<h3>use locale can restrict which locale categories are affected</h3>
<p> It is now possible to pass a parameter to <tt>&quot;use locale&quot;</tt> to specify a subset of locale categories to be locale-aware, with the remaining ones unaffected. See &#8220;The &#8221;use locale&#8220; pragma&#8221; in perllocale for details.</p>
<h3>Perl now supports <font SIZE="-1">POSIX 2008</font> locale currency additions</h3>
<p> On platforms that are able to handle <font SIZE="-1">POSIX.1-2008,</font> the hash returned by <tt>&quot;POSIX::localeconv()&quot;</tt> includes the international currency fields added by that version of the <font SIZE="-1">POSIX</font> standard. These are <tt>&quot;int_n_cs_precedes&quot;</tt>, <tt>&quot;int_n_sep_by_space&quot;</tt>, <tt>&quot;int_n_sign_posn&quot;</tt>, <tt>&quot;int_p_cs_precedes&quot;</tt>, <tt>&quot;int_p_sep_by_space&quot;</tt>, and <tt>&quot;int_p_sign_posn&quot;</tt>.</p>
<h3>Better heuristics on older platforms for determining locale UTF-8ness</h3>
<p> On platforms that implement neither the C99 standard nor the <font SIZE="-1">POSIX 2001</font> standard, determining if the current locale is <font SIZE="-1">UTF-8</font> or not depends on heuristics. These are improved in this release.</p>
<h3>Aliasing via reference</h3>
<p> Variables and subroutines can now be aliased by assigning to a reference: </p>
<pre>
    \$c = \$d;
    \&amp;x = \&amp;y;
</pre>
<p> Aliasing can also be accomplished by using a backslash before a <tt>&quot;foreach&quot;</tt> iterator variable; this is perhaps the most useful idiom this feature provides: </p>
<pre>
    foreach \%hash (@array_of_hash_refs) { ... }
</pre>
<p> This feature is experimental and must be enabled via <tt>&quot;use feature 'refaliasing'&quot;</tt>. It will warn unless the <tt>&quot;experimental::refaliasing&quot;</tt> warnings category is disabled. </p>
<p> See &#8220;Assigning to References&#8221; in perlref</p>
<h3>prototype with no arguments</h3>
<p> <tt>&quot;prototype()&quot;</tt> with no arguments now infers <tt>$_</tt>. [perl #123514] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123514">https://rt.perl.org/Ticket/Display.html?id=123514</a>&gt;.</p>
<h3>New :const subroutine attribute</h3>
<p> The <tt>&quot;const&quot;</tt> attribute can be applied to an anonymous subroutine. It causes the new sub to be executed immediately whenever one is created (<i>i.e.</i> when the <tt>&quot;sub&quot;</tt> expression is evaluated). Its value is captured and used to create a new constant subroutine that is returned. This feature is experimental. See &#8220;Constant Functions&#8221; in perlsub.</p>
<h3>fileno now works on directory handles</h3>
<p> When the relevant support is available in the operating system, the <tt>&quot;fileno&quot;</tt> builtin now works on directory handles, yielding the underlying file descriptor in the same way as for filehandles. On operating systems without such support, <tt>&quot;fileno&quot;</tt> on a directory handle continues to return the undefined value, as before, but also sets <tt>$!</tt> to indicate that the operation is not supported. </p>
<p> Currently, this uses either a <tt>&quot;dd_fd&quot;</tt> member in the <font SIZE="-1">OS</font> <tt>&quot;DIR&quot;</tt> structure, or a <tt><a href="/docs/linux/man/3-dirfd/">dirfd</a>(3)</tt> function as specified by <font SIZE="-1">POSIX.1-2008.</font></p>
<h3>List form of pipe open implemented for Win32</h3>
<p> The list form of pipe: </p>
<pre>
  open my $fh, &quot;-|&quot;, &quot;program&quot;, @arguments;
</pre>
<p> is now implemented on Win32. It has the same limitations as <tt>&quot;system LIST&quot;</tt> on Win32, since the Win32 <font SIZE="-1">API</font> doesn&#8217;t accept program arguments as a list.</p>
<h3>Assignment to list repetition</h3>
<p> <tt>&quot;(...) x ...&quot;</tt> can now be used within a list that is assigned to, as long as the left-hand side is a valid lvalue. This allows <tt>&quot;(undef,undef,$foo) = that_function()&quot;</tt> to be written as <tt>&quot;((undef)x2, $foo) = that_function()&quot;</tt>.</p>
<h3>Infinity and NaN (not-a-number) handling improved</h3>
<p> Floating point values are able to hold the special values infinity, negative infinity, and NaN (not-a-number). Now we more robustly recognize and propagate the value in computations, and on output normalize them to the strings <tt>&quot;Inf&quot;</tt>, <tt>&quot;-Inf&quot;</tt>, and <tt>&quot;NaN&quot;</tt>. </p>
<p> See also the <font SIZE="-1">POSIX</font> enhancements.</p>
<h3>Floating point parsing has been improved</h3>
<p> Parsing and printing of floating point values has been improved. </p>
<p> As a completely new feature, hexadecimal floating point literals (like <tt>&quot;0x1.23p-4&quot;</tt>) are now supported, and they can be output with <tt>&quot;printf &quot;%a&quot;&quot;</tt>. See &#8220;Scalar value constructors&#8221; in perldata for more details.</p>
<h3>Packing infinity or not-a-number into a character is now fatal</h3>
<p> Before, when trying to pack infinity or not-a-number into a (signed) character, Perl would warn, and assumed you tried to pack <tt>0xFF</tt>; if you gave it as an argument to <tt>&quot;chr&quot;</tt>, <tt>&quot;U+FFFD&quot;</tt> was returned. </p>
<p> But now, all such actions (<tt>&quot;pack&quot;</tt>, <tt>&quot;chr&quot;</tt>, and <tt>&quot;print '%c'&quot;</tt>) result in a fatal error.</p>
<h3>Experimental C Backtrace <font SIZE="-1">API</font></h3>
<p> Perl now supports (via a C level <font SIZE="-1">API</font>) retrieving the C level backtrace (similar to what symbolic debuggers like gdb do). </p>
<p> The backtrace returns the stack trace of the C call frames, with the symbol names (function names), the object names (like &#8220;perl&#8221;), and if it can, also the source code locations (file:line). </p>
<p> The supported platforms are Linux and <font SIZE="-1">OS X</font> (some *BSD might work at least partly, but they have not yet been tested). </p>
<p> The feature needs to be enabled with <tt>&quot;Configure -Dusecbacktrace&quot;</tt>. </p>
<p> See &#8220;C backtrace&#8221; in perlhacktips for more information.</p>
<h2>Security</h2>
<h3>Perl is now compiled with -fstack-protector-strong if available</h3>
<p> Perl has been compiled with the anti-stack-smashing option <tt>&quot;-fstack-protector&quot;</tt> since 5.10.1. Now Perl uses the newer variant called <tt>&quot;-fstack-protector-strong&quot;</tt>, if available.</p>
<h3>The Safe module could allow outside packages to be replaced</h3>
<p> Critical bugfix: outside packages could be replaced. Safe has been patched to 2.38 to address this.</p>
<h3>Perl is now always compiled with -D_FORTIFY_SOURCE=2 if available</h3>
<p> The &#8216;code hardening&#8217; option called <tt>&quot;_FORTIFY_SOURCE&quot;</tt>, available in gcc 4.*, is now always used for compiling Perl, if available. </p>
<p> Note that this isn&#8217;t necessarily a huge step since in many platforms the step had already been taken several years ago: many Linux distributions (like Fedora) have been using this option for Perl, and <font SIZE="-1">OS X</font> has enforced the same for many years.</p>
<h2>Incompatible Changes</h2>
<h3>Subroutine signatures moved before attributes</h3>
<p> The experimental sub signatures feature, as introduced in 5.20, parsed signatures after attributes. In this release, following feedback from users of the experimental feature, the positioning has been moved such that signatures occur after the subroutine name (if any) and before the attribute list (if any).</p>
<h3>&amp; and \&amp; prototypes accepts only subs</h3>
<p> The <tt>&quot;&amp;&quot;</tt> prototype character now accepts only anonymous subs (<tt>&quot;sub {...}&quot;</tt>), things beginning with <tt>&quot;\&amp;&quot;</tt>, or an explicit <tt>&quot;undef&quot;</tt>. Formerly it erroneously also allowed references to arrays, hashes, and lists. [perl #4539] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=4539">https://rt.perl.org/Ticket/Display.html?id=4539</a>&gt;. [perl #123062] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123062">https://rt.perl.org/Ticket/Display.html?id=123062</a>&gt;. [perl #123062] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123475">https://rt.perl.org/Ticket/Display.html?id=123475</a>&gt;. </p>
<p> In addition, the <tt>&quot;\&amp;&quot;</tt> prototype was allowing subroutine calls, whereas now it only allows subroutines: <tt>&amp;foo</tt> is still permitted as an argument, while <tt>&quot;&amp;foo()&quot;</tt> and <tt>&quot;foo()&quot;</tt> no longer are. [perl #77860] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=77860">https://rt.perl.org/Ticket/Display.html?id=77860</a>&gt;.</p>
<h3>use encoding is now lexical</h3>
<p> The encoding pragma&#8217;s effect is now limited to lexical scope. This pragma is deprecated, but in the meantime, it could adversely affect unrelated modules that are included in the same program; this change fixes that.</p>
<h3>List slices returning empty lists</h3>
<p> List slices now return an empty list only if the original list was empty (or if there are no indices). Formerly, a list slice would return an empty list if all indices fell outside the original list; now it returns a list of <tt>&quot;undef&quot;</tt> values in that case. [perl #114498] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=114498">https://rt.perl.org/Ticket/Display.html?id=114498</a>&gt;.</p>
<h3>\N{} with a sequence of multiple spaces is now a fatal error</h3>
<p> E.g. <tt>&quot;\N{TOO  MANY SPACES}&quot;</tt> or <tt>&quot;\N{TRAILING SPACE }&quot;</tt>. This has been deprecated since v5.18.</p>
<h3>use UNIVERSAL &#8216;&#8230;&#8217; is now a fatal error</h3>
<p> Importing functions from <tt>&quot;UNIVERSAL&quot;</tt> has been deprecated since v5.12, and is now a fatal error. <tt>&quot;use UNIVERSAL&quot;</tt> without any arguments is still allowed.</p>
<h3>In double-quotish 
 \cX, <i>X</i> must now be a printable <font SIZE="-1">ASCII</font> character</h3>
<p> In prior releases, failure to do this raised a deprecation warning.  </p>
<h3>Splitting the tokens (? and (* in regular expressions is now a fatal compilation error.</h3>
<p> These had been deprecated since v5.18.  </p>
<h3>qr/foo/x now ignores all Unicode pattern white space</h3>
<p> The <code>&quot;/x&quot;</code> regular expression modifier allows the pattern to contain white space and comments (both of which are ignored) for improved readability. Until now, not all the white space characters that Unicode designates for this purpose were handled. The additional ones now recognized are: </p>
<pre><code>    U+0085 NEXT LINE
    U+200E LEFT-TO-RIGHT MARK
    U+200F RIGHT-TO-LEFT MARK
    U+2028 LINE SEPARATOR
    U+2029 PARAGRAPH SEPARATOR
</code></pre>
<p> The use of these characters with <code>&quot;/x&quot;</code> outside bracketed character classes and when not preceded by a backslash has raised a deprecation warning since v5.18. Now they will be ignored.  </p>
<h3>Comment lines within (?[ ]) are now ended only by a \n</h3>
<p> <code>&quot;(?[ ])&quot;</code> is an experimental feature, introduced in v5.18. It operates as if <code>&quot;/x&quot;</code> is always enabled. But there was a difference: comment lines (following a <code>&quot;#&quot;</code> character) were terminated by anything matching <code>&quot;\R&quot;</code> which includes all vertical whitespace, such as form feeds. For consistency, this is now changed to match what terminates comment lines outside <code>&quot;(?[ ])&quot;</code>, namely a <code>&quot;\n&quot;</code> (even if escaped), which is the same as what terminates a heredoc string and formats.  </p>
<h3>(?[...]) operators now follow standard Perl precedence</h3>
<p> This experimental feature allows set operations in regular expression patterns. Prior to this, the intersection operator had the same precedence as the other binary operators. Now it has higher precedence. This could lead to different outcomes than existing code expects (though the documentation has always noted that this change might happen, recommending fully parenthesizing the expressions). See ``Extended Bracketed Character Classes&#8217;&#8216; in perlrecharclass.  </p>
<h3>Omitting % and @ on hash and array names is no longer permitted</h3>
<p> Really old Perl let you omit the <code>&quot;@&quot;</code> on array names and the <code>&quot;%&quot;</code> on hash names in some spots. This has issued a deprecation warning since Perl 5.000, and is no longer permitted.  </p>
<h3>$! text is now in English outside the scope of use locale</h3>
<p> Previously, the text, unlike almost everything else, always came out based on the current underlying locale of the program. (Also affected on some systems is <code>&quot;$^E&quot;</code>.) For programs that are unprepared to handle locale differences, this can cause garbage text to be displayed. It&#8217;s better to display text that is translatable via some tool than garbage text which is much harder to figure out.  </p>
<font SIZE="-1"></font><h3>$! text will be returned in UTF-8 when appropriate</h3>
<p> The stringification of <code>$!</code> and <code>$^E</code> will have the <font SIZE="-1">UTF-8</font> flag set when the text is actually non-ASCII <font SIZE="-1">UTF-8.</font> This will enable programs that are set up to be locale-aware to properly output messages in the user&#8217;s native language. Code that needs to continue the 5.20 and earlier behavior can do the stringification within the scopes of both <code>&quot;use bytes&quot;</code> and <code>&quot;use locale &quot;:messages&quot;&quot;</code>. Within these two scopes, no other Perl operations will be affected by locale; only <code>$!</code> and <code>$^E</code> stringification. The <code>&quot;bytes&quot;</code> pragma causes the <font SIZE="-1">UTF-8</font> flag to not be set, just as in previous Perl releases. This resolves [perl #112208] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=112208">https://rt.perl.org/Ticket/Display.html?id=112208</a>&gt;.  </p>
<h3>Support for ?PATTERN? without explicit operator has been removed</h3>
<p> The <code>&quot;m?PATTERN?&quot;</code> construct, which allows matching a regex only once, previously had an alternative form that was written directly with a question mark delimiter, omitting the explicit <code>&quot;m&quot;</code> operator. This usage has produced a deprecation warning since 5.14.0. It is now a syntax error, so that the question mark can be available for use in new operators.  </p>
<h3>defined(@array) and defined(%hash) are now fatal errors</h3>
<p> These have been deprecated since v5.6.1 and have raised deprecation warnings since v5.16.  </p>
<h3>Using a hash or an array as a reference are now fatal errors</h3>
<p> For example, <code>&quot;%foo-&gt;{&quot;bar&quot;}&quot;</code> now causes a fatal compilation error. These have been deprecated since before v5.8, and have raised deprecation warnings since then.  </p>
<h3>Changes to the * prototype</h3>
<p> The <code>&quot;*&quot;</code> character in a subroutine&#8217;s prototype used to allow barewords to take precedence over most, but not all, subroutine names. It was never consistent and exhibited buggy behavior. </p>
<p> Now it has been changed, so subroutines always take precedence over barewords, which brings it into conformity with similarly prototyped built-in functions: </p>
<pre><code>    sub splat(*) { ... }
    sub foo { ... }
    splat(foo); # now always splat(foo())
    splat(bar); # still splat('bar') as before
    close(foo); # close(foo())
    close(bar); # close('bar')
</code></pre>
<h2>Deprecations</h2>
<h3>Setting ${^ENCODING} to anything but undef</h3>
<p> This variable allows Perl scripts to be written in an encoding other than <font SIZE="-1">ASCII</font> or <font SIZE="-1">UTF-8.</font> However, it affects all modules globally, leading to wrong answers and segmentation faults. New scripts should be written in <font SIZE="-1">UTF-8</font>; old scripts should be converted to <font SIZE="-1">UTF-8,</font> which is easily done with the piconv utility.  </p>
<h3>Use of non-graphic characters in single-character variable names</h3>
<p> The syntax for single-character variable names is more lenient than for longer variable names, allowing the one-character name to be a punctuation character or even invisible (a non-graphic). Perl v5.20 deprecated the ASCII-range controls as such a name. Now, all non-graphic characters that formerly were allowed are deprecated. The practical effect of this occurs only when not under <code>&quot;use utf8&quot;</code>, and affects just the C1 controls (code points 0x80 through 0xFF), NO-BREAK <font SIZE="-1">SPACE,</font> and <font SIZE="-1">SOFT HYPHEN.</font>  </p>
<h3>Inlining of sub () { $var } with observable side-effects</h3>
<p> In many cases Perl makes <code>&quot;sub () { $var }&quot;</code> into an inlinable constant subroutine, capturing the value of <code>$var</code> at the time the <code>&quot;sub&quot;</code> expression is evaluated. This can break the closure behavior in those cases where <code>$var</code> is subsequently modified, since the subroutine won&#8217;t return the changed value. (Note that this all only applies to anonymous subroutines with an empty prototype (<code>&quot;sub ()&quot;</code>).) </p>
<p> This usage is now deprecated in those cases where the variable could be modified elsewhere. Perl detects those cases and emits a deprecation warning. Such code will likely change in the future and stop producing a constant. </p>
<p> If your variable is only modified in the place where it is declared, then Perl will continue to make the sub inlinable with no warnings. </p>
<pre><code>    sub make_constant {
        my $var = shift;
        return sub () { $var }; # fine
    }
    sub make_constant_deprecated {
        my $var;
        $var = shift;
        return sub () { $var }; # deprecated
    }
    sub make_constant_deprecated2 {
        my $var = shift;
        log_that_value($var); # could modify $var
        return sub () { $var }; # deprecated
    }
</code></pre>
<p> In the second example above, detecting that <code>$var</code> is assigned to only once is too hard to detect. That it happens in a spot other than the <code>&quot;my&quot;</code> declaration is enough for Perl to find it suspicious. </p>
<p> This deprecation warning happens only for a simple variable for the body of the sub. (A <code>&quot;BEGIN&quot;</code> block or <code>&quot;use&quot;</code> statement inside the sub is ignored, because it does not become part of the sub&#8217;s body.) For more complex cases, such as <code>&quot;sub () { do_something() if 0; $var }&quot;</code> the behavior has changed such that inlining does not happen if the variable is modifiable elsewhere. Such cases should be rare.  </p>
<h3>Use of multiple /x regexp modifiers</h3>
<p> It is now deprecated to say something like any of the following: </p>
<pre><code>    qr/foo/xx;
    /(?xax:foo)/;
    use re qw(/amxx);
</code></pre>
<p> That is, now <code>&quot;x&quot;</code> should only occur once in any string of contiguous regular expression pattern modifiers. We do not believe there are any occurrences of this in all of <font SIZE="-1">CPAN.</font> This is in preparation for a future Perl release having <code>&quot;/xx&quot;</code> permit white-space for readability in bracketed character classes (those enclosed in square brackets: <code>&quot;[...]&quot;</code>).  </p>
<h3>Using a NO-BREAK space in a character alias for \N{...} is now deprecated</h3>
<p> This non-graphic character is essentially indistinguishable from a regular space, and so should not be allowed. See ``<font SIZE="-1">CUSTOM ALIASES&#8217;&#8216;</font> in charnames.  </p>
<h3>A literal { should now be escaped in a pattern</h3>
<p> If you want a literal left curly bracket (also called a left brace) in a regular expression pattern, you should now escape it by either preceding it with a backslash (<code>&quot;\{&quot;</code>) or enclosing it within square brackets <code>&quot;[{]&quot;</code>, or by using <code>&quot;\Q&quot;</code>; otherwise a deprecation warning will be raised. This was first announced as forthcoming in the v5.16 release; it will allow future extensions to the language to happen.  </p>
<h3>Making all warnings fatal is discouraged</h3>
<p> The documentation for fatal warnings notes that <code>&quot;use warnings FATAL =&gt; &#8216;all&#8217;&quot;</code> is discouraged, and provides stronger language about the risks of fatal warnings in general.  </p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> If a method or class name is known at compile time, a hash is precomputed to speed up run-time method lookup. Also, compound method names like <code>&quot;SUPER::new&quot;</code> are parsed at compile time, to save having to parse them at run time. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Array and hash lookups (especially nested ones) that use only constants or simple variables as keys, are now considerably faster. See ``Internal Changes&#8217;&#8216; for more details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;(...)x1&quot;</code>, <code>&quot;(&quot;constant&quot;)x0&quot;</code> and <code>&quot;($scalar)x0&quot;</code> are now optimised in list context. If the right-hand argument is a constant 1, the repetition operator disappears. If the right-hand argument is a constant 0, the whole expression is optimised to the empty list, so long as the left-hand argument is a simple scalar or constant. (That is, <code>&quot;(foo())x0&quot;</code> is not subject to this optimisation.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;substr&quot;</code> assignment is now optimised into 4-argument <code>&quot;substr&quot;</code> at the end of a subroutine (or as the argument to <code>&quot;return&quot;</code>). Previously, this optimisation only happened in void context. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In <code>&quot;\L...&quot;</code>, <code>&quot;\Q...&quot;</code>, etc., the extra ``stringify&#8217;&#8216; op is now optimised away, making these just as fast as <code>&quot;lcfirst&quot;</code>, <code>&quot;quotemeta&quot;</code>, etc. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assignment to an empty list is now sometimes faster. In particular, it never calls <code>&quot;FETCH&quot;</code> on tied arguments on the right-hand side, whereas it used to sometimes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> There is a performance improvement of up to 20% when <code>&quot;length&quot;</code> is applied to a non-magical, non-tied string, and either <code>&quot;use bytes&quot;</code> is in scope or the string doesn&#8217;t use <font SIZE="-1">UTF-8</font> internally. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On most perl builds with 64-bit integers, memory usage for non-magical, non-tied scalars containing only a floating point value has been reduced by between 8 and 32 bytes, depending on <font SIZE="-1">OS.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In <code>&quot;@array = split&quot;</code>, the assignment can be optimized away, so that <code>&quot;split&quot;</code> writes directly to the array. This optimisation was happening only for package arrays other than <code>@_</code>, and only sometimes. Now this optimisation happens almost all the time. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;join&quot;</code> is now subject to constant folding. So for example <code>&quot;join &quot;-&quot;, &quot;a&quot;, &quot;b&quot;&quot;</code> is converted at compile-time to <code>&quot;a-b&quot;</code>. Moreover, <code>&quot;join&quot;</code> with a scalar or constant for the separator and a single-item list to join is simplified to a stringification, and the separator doesn&#8217;t even get evaluated. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;qq(@array)&quot;</code> is implemented using two ops: a stringify op and a join op. If the <code>&quot;qq&quot;</code> contains nothing but a single array, the stringification is optimized away. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;our $var&quot;</code> and <code>&quot;our($s,@a,%h)&quot;</code> in void context are no longer evaluated at run time. Even a whole sequence of <code>&quot;our $foo;&quot;</code> statements will simply be skipped over. The same applies to <code>&quot;state&quot;</code> variables. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Many internal functions have been refactored to improve performance and reduce their memory footprints. [perl #121436] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121436">https://rt.perl.org/Ticket/Display.html?id=121436</a>&gt; [perl #121906] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121906">https://rt.perl.org/Ticket/Display.html?id=121906</a>&gt; [perl #121969] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121969">https://rt.perl.org/Ticket/Display.html?id=121969</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-T&quot;</code> and <code>&quot;-B&quot;</code> filetests will return sooner when an empty file is detected. [perl #121489] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121489">https://rt.perl.org/Ticket/Display.html?id=121489</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hash lookups where the key is a constant are faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Subroutines with an empty prototype and a body containing just <code>&quot;undef&quot;</code> are now eligible for inlining. [perl #122728] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122728">https://rt.perl.org/Ticket/Display.html?id=122728</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Subroutines in packages no longer need to be stored in typeglobs: declaring a subroutine will now put a simple sub reference directly in the stash if possible, saving memory. The typeglob still notionally exists, so accessing it will cause the stash entry to be upgraded to a typeglob (<i>i.e.</i> this is just an internal implementation detail). This optimization does not currently apply to XSUBs or exported subroutines, and method calls will undo it, since they cache things in typeglobs. [perl #120441] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=120441">https://rt.perl.org/Ticket/Display.html?id=120441</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The functions <code>&quot;utf8::native_to_unicode()&quot;</code> and <code>&quot;utf8::unicode_to_native()&quot;</code> (see utf8) are now optimized out on <font SIZE="-1">ASCII</font> platforms. There is now not even a minimal performance hit in writing code portable between <font SIZE="-1">ASCII</font> and <font SIZE="-1">EBCDIC</font> platforms. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Win32 Perl uses 8 <font SIZE="-1">KB</font> less of per-process memory than before for every perl process, because some data is now memory mapped from disk and shared between processes from the same perl binary. </p>
 </dd></dl>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<p> Many of the libraries distributed with perl have been upgraded since v5.20.0. For a complete list of changes, run: </p>
<pre><code>  corelist --diff 5.20.0 5.22.0
</code></pre>
<p> You can substitute your favorite version in place of 5.20.0, too. </p>
<p> Some notable changes include: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Archive::Tar has been upgraded to version 2.04. </p>
<p> Tests can now be run in parallel. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> attributes has been upgraded to version 0.27. </p>
<p> The usage of <code>&quot;memEQs&quot;</code> in the <font SIZE="-1">XS</font> has been corrected. [perl #122701] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122701">https://rt.perl.org/Ticket/Display.html?id=122701</a>&gt; </p>
<p> Avoid reading beyond the end of a buffer. [perl #122629] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B has been upgraded to version 1.58. </p>
<p> It provides a new <code>&quot;B::safename&quot;</code> function, based on the existing <code>&quot;B::GV-&gt;SAFENAME&quot;</code>, that converts <code>&quot;\cOPEN&quot;</code> to <code>&quot;^OPEN&quot;</code>. </p>
<p> Nulled COPs are now of class <code>&quot;B::COP&quot;</code>, rather than <code>&quot;B::OP&quot;</code>. </p>
<p> <code>&quot;B::REGEXP&quot;</code> objects now provide a <code>&quot;qr_anoncv&quot;</code> method for accessing the implicit <font SIZE="-1">CV</font> associated with <code>&quot;qr//&quot;</code> things containing code blocks, and a <code>&quot;compflags&quot;</code> method that returns the pertinent flags originating from the <code>&quot;qr//blahblah&quot;</code> op. </p>
<p> <code>&quot;B::PMOP&quot;</code> now provides a <code>&quot;pmregexp&quot;</code> method returning a <code>&quot;B::REGEXP&quot;</code> object. Two new classes, <code>&quot;B::PADNAME&quot;</code> and <code>&quot;B::PADNAMELIST&quot;</code>, have been introduced. </p>
<p> A bug where, after an ithread creation or psuedofork, special/immortal SVs in the child ithread/psuedoprocess did not have the correct class of <code>&quot;B::SPECIAL&quot;</code>, has been fixed. The <code>&quot;id&quot;</code> and <code>&quot;outid&quot;</code> <font SIZE="-1">PADLIST</font> methods have been added. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Concise has been upgraded to version 0.996. </p>
<p> Null ops that are part of the execution chain are now given sequence numbers. </p>
<p> Private flags for nulled ops are now dumped with mnemonics as they would be for the non-nulled counterparts. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Deparse has been upgraded to version 1.35. </p>
<p> It now deparses <code>&quot;+sub : attr { ... }&quot;</code> correctly at the start of a statement. Without the initial <code>&quot;+&quot;</code>, <code>&quot;sub&quot;</code> would be a statement label. </p>
<p> <code>&quot;BEGIN&quot;</code> blocks are now emitted in the right place most of the time, but the change unfortunately introduced a regression, in that <code>&quot;BEGIN&quot;</code> blocks occurring just before the end of the enclosing block may appear below it instead. </p>
<p> <code>&quot;B::Deparse&quot;</code> no longer puts erroneous <code>&quot;local&quot;</code> here and there, such as for <code>&quot;LIST = tr/a//d&quot;</code>. [perl #119815] </p>
<p> Adjacent <code>&quot;use&quot;</code> statements are no longer accidentally nested if one contains a <code>&quot;do&quot;</code> block. [perl #115066] </p>
<p> Parenthesised arrays in lists passed to <code>&quot;\&quot;</code> are now correctly deparsed with parentheses (<i>e.g.</i>, <code>&quot;\(@a, (@b), @c)&quot;</code> now retains the parentheses around <code>@b</code>), thus preserving the flattening behavior of referenced parenthesised arrays. Formerly, it only worked for one array: <code>&quot;\(@a)&quot;</code>. </p>
<p> <code>&quot;local our&quot;</code> is now deparsed correctly, with the <code>&quot;our&quot;</code> included. </p>
<p> <code>&quot;for($foo; !$bar; $baz) {...}&quot;</code> was deparsed without the <code>&quot;!&quot;</code> (or <code>&quot;not&quot;</code>). This has been fixed. </p>
<p> Core keywords that conflict with lexical subroutines are now deparsed with the <code>&quot;CORE::&quot;</code> prefix. </p>
<p> <code>&quot;foreach state $x (...) {...}&quot;</code> now deparses correctly with <code>&quot;state&quot;</code> and not <code>&quot;my&quot;</code>. </p>
<p> <code>&quot;our @array = split(...)&quot;</code> now deparses correctly with <code>&quot;our&quot;</code> in those cases where the assignment is optimized away. </p>
<p> It now deparses <code>&quot;our(</code>LIST <code>)&quot;</code> and typed lexical (<code>&quot;my Dog $spot&quot;</code>) correctly. </p>
<p> Deparse <code>$#_</code> as that instead of as <code>$#{_}</code>. [perl #123947] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123947">https://rt.perl.org/Ticket/Display.html?id=123947</a>&gt; </p>
<p> <font SIZE="-1">BEGIN</font> blocks at the end of the enclosing scope are now deparsed in the right place. [perl #77452] </p>
<p> <font SIZE="-1">BEGIN</font> blocks were sometimes deparsed as __ANON__, but are now always called <font SIZE="-1">BEGIN.</font> </p>
<p> Lexical subroutines are now fully deparsed. [perl #116553] </p>
<p> <code>&quot;Anything =~ y///r&quot;</code> with <code>&quot;/r&quot;</code> no longer omits the left-hand operand. </p>
<p> The op trees that make up regexp code blocks are now deparsed for real. Formerly, the original string that made up the regular expression was used. That caused problems with <code>&quot;qr/(?{&lt;&lt;heredoc})/&quot;</code> and multiline code blocks, which were deparsed incorrectly. [perl #123217] [perl #115256] </p>
<p> <code>$;</code> at the end of a statement no longer loses its semicolon. [perl #123357] </p>
<p> Some cases of subroutine declarations stored in the stash in shorthand form were being omitted. </p>
<p> Non-ASCII characters are now consistently escaped in strings, instead of some of the time. (There are still outstanding problems with regular expressions and identifiers that have not been fixed.) </p>
<p> When prototype sub calls are deparsed with <code>&quot;&amp;&quot;</code> (<i>e.g.</i>, under the <code>-P</code> option), <code>&quot;scalar&quot;</code> is now added where appropriate, to force the scalar context implied by the prototype. </p>
<p> <code>&quot;require(foo())&quot;</code>, <code>&quot;do(foo())&quot;</code>, <code>&quot;goto(foo())&quot;</code> and similar constructs with loop controls are now deparsed correctly. The outer parentheses are not optional. </p>
<p> Whitespace is no longer escaped in regular expressions, because it was getting erroneously escaped within <code>&quot;(?x:...)&quot;</code> sections. </p>
<p> <code>&quot;sub foo { foo() }&quot;</code> is now deparsed with those mandatory parentheses. </p>
<p> <code>&quot;/@array/&quot;</code> is now deparsed as a regular expression, and not just <code>@array</code>. </p>
<p> <code>&quot;/@{-}/&quot;</code>, <code>&quot;/@{+}/&quot;</code> and <code>$#{1}</code> are now deparsed with the braces, which are mandatory in these cases. </p>
<p> In deparsing feature bundles, <code>&quot;B::Deparse&quot;</code> was emitting <code>&quot;no feature;&quot;</code> first instead of <code>&quot;no feature &#8216;:all&#8217;;&quot;</code>. This has been fixed. </p>
<p> <code>&quot;chdir FH&quot;</code> is now deparsed without quotation marks. </p>
<p> <code>&quot;\my @a&quot;</code> is now deparsed without parentheses. (Parenthese would flatten the array.) </p>
<p> <code>&quot;system&quot;</code> and <code>&quot;exec&quot;</code> followed by a block are now deparsed correctly. Formerly there was an erroneous <code>&quot;do&quot;</code> before the block. </p>
<p> <code>&quot;use constant QR =&gt; qr/.../flags&quot;</code> followed by <code>&quot;&quot;&quot; =~ QR&quot;</code> is no longer without the flags. </p>
<p> Deparsing <code>&quot;BEGIN { undef &amp;foo }&quot;</code> with the <code>-w</code> switch enabled started to emit &#8216;uninitialized&#8217; warnings in Perl 5.14. This has been fixed. </p>
<p> Deparsing calls to subs with a <code>&quot;(;+)&quot;</code> prototype resulted in an infinite loop. The <code>&quot;(;$&quot;</code>) <code>&quot;(_)&quot;</code> and <code>&quot;(;_)&quot;</code> prototypes were given the wrong precedence, causing <code>&quot;foo($a&lt;$b)&quot;</code> to be deparsed without the parentheses. </p>
<p> Deparse now provides a defined state sub in inner subs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Op_private has been added. </p>
<p> B::Op_private provides detailed information about the flags used in the <code>&quot;op_private&quot;</code> field of perl opcodes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> bigint, bignum, bigrat have been upgraded to version 0.39. </p>
<p> Document in <font SIZE="-1">CAVEATS</font> that using strings as numbers won&#8217;t always invoke the big number overloading, and how to invoke it. [rt.perl.org #123064] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Carp has been upgraded to version 1.36. </p>
<p> <code>&quot;Carp::Heavy&quot;</code> now ignores version mismatches with Carp if Carp is newer than 1.12, since <code>&quot;Carp::Heavy&quot;</code>&#8216;s guts were merged into Carp at that point. [perl #121574] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121574">https://rt.perl.org/Ticket/Display.html?id=121574</a>&gt; </p>
<p> Carp now handles non-ASCII platforms better. </p>
<p> Off-by-one error fix for Perl &lt; 5.14. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> constant has been upgraded to version 1.33. </p>
<p> It now accepts fully-qualified constant names, allowing constants to be defined in packages other than the caller. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CPAN</font> has been upgraded to version 2.11. </p>
<p> Add support for <code>&quot;Cwd::getdcwd()&quot;</code> and introduce workaround for a misbehavior seen on Strawberry Perl 5.20.1. </p>
<p> Fix <code>&quot;chdir()&quot;</code> after building dependencies bug. </p>
<p> Introduce experimental support for plugins/hooks. </p>
<p> Integrate the <code>&quot;App::Cpan&quot;</code> sources. </p>
<p> Do not check recursion on optional dependencies. </p>
<p> Sanity check <i></i><font SIZE="-1"><i>META</i></font><i>.yml</i> to contain a hash. [cpan #95271] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=95271">https://rt.cpan.org/Ticket/Display.html?id=95271</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> CPAN::Meta::Requirements has been upgraded to version 2.132. </p>
<p> Works around limitations in <code>&quot;version::vpp&quot;</code> detecting v-string magic and adds support for forthcoming ExtUtils::MakeMaker bootstrap <i>version.pm</i> for Perls older than 5.10.0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Data::Dumper has been upgraded to version 2.158. </p>
<p> Fixes <font SIZE="-1">CVE-2014-4330</font> by adding a configuration variable/option to limit recursion when dumping deep data structures. </p>
<p> Changes to resolve Coverity issues. <font SIZE="-1">XS</font> dumps incorrectly stored the name of code references stored in a <font SIZE="-1">GLOB.</font> [perl #122070] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122070">https://rt.perl.org/Ticket/Display.html?id=122070</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DynaLoader has been upgraded to version 1.32. </p>
<p> Remove <code>&quot;dl_nonlazy&quot;</code> global if unused in Dynaloader. [perl #122926] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Encode has been upgraded to version 2.72. </p>
<p> <code>&quot;piconv&quot;</code> now has better error handling when the encoding name is nonexistent, and a build breakage when upgrading Encode in perl-5.8.2 and earlier has been fixed. </p>
<p> Building in C<font SIZE="-2">++</font> mode on Windows now works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Errno has been upgraded to version 1.23. </p>
<p> Add <code>&quot;-P&quot;</code> to the preprocessor command-line on <font SIZE="-1">GCC 5.</font> <font SIZE="-1">GCC</font> added extra line directives, breaking parsing of error code definitions. [rt.perl.org #123784] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> experimental has been upgraded to version 0.013. </p>
<p> Hardcodes features for Perls older than 5.15.7. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::CBuilder has been upgraded to version 0.280221. </p>
<p> Fixes a regression on Android. [perl #122675] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122675">https://rt.perl.org/Ticket/Display.html?id=122675</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Manifest has been upgraded to version 1.70. </p>
<p> Fixes a bug with <code>&quot;maniread()&quot;</code>&#8216;s handling of quoted filenames and improves <code>&quot;manifind()&quot;</code> to follow symlinks. [perl #122415] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122415">https://rt.perl.org/Ticket/Display.html?id=122415</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::ParseXS has been upgraded to version 3.28. </p>
<p> Only declare <code>&quot;file&quot;</code> unused if we actually define it. Improve generated <code>&quot;RETVAL&quot;</code> code generation to avoid repeated references to <code>ST(0)</code>. [perl #123278] Broaden and document the <code>&quot;/OBJ$/&quot;</code> to <code>&quot;/REF$/&quot;</code> typemap optimization for the <code>&quot;DESTROY&quot;</code> method. [perl #123418] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fcntl has been upgraded to version 1.13. </p>
<p> Add support for the Linux pipe buffer size <code>&quot;fcntl()&quot;</code> commands. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Find has been upgraded to version 1.29. </p>
<p> <code>&quot;find()&quot;</code> and <code>&quot;finddepth()&quot;</code> will now warn if passed inappropriate or misspelled options. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Glob has been upgraded to version 1.24. </p>
<p> Avoid <code>&quot;SvIV()&quot;</code> expanding to call <code>&quot;get_sv()&quot;</code> three times in a few places. [perl #123606] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> HTTP::Tiny has been upgraded to version 0.054. </p>
<p> <code>&quot;keep_alive&quot;</code> is now fork-safe and thread-safe. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">IO</font> has been upgraded to version 1.35. </p>
<p> The <font SIZE="-1">XS</font> implementation has been fixed for the sake of older Perls. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO::Socket has been upgraded to version 1.38. </p>
<p> Document the limitations of the <code>&quot;connected()&quot;</code> method. [perl #123096] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO::Socket::IP has been upgraded to version 0.37. </p>
<p> A better fix for subclassing <code>&quot;connect()&quot;</code>. [cpan #95983] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=95983">https://rt.cpan.org/Ticket/Display.html?id=95983</a>&gt; [cpan #97050] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=97050">https://rt.cpan.org/Ticket/Display.html?id=97050</a>&gt; </p>
<p> Implements Timeout for <code>&quot;connect()&quot;</code>. [cpan #92075] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=92075">https://rt.cpan.org/Ticket/Display.html?id=92075</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The libnet collection of modules has been upgraded to version 3.05. </p>
<p> Support for IPv6 and <font SIZE="-1">SSL</font> to <code>&quot;Net::FTP&quot;</code>, <code>&quot;Net::NNTP&quot;</code>, <code>&quot;Net::POP3&quot;</code> and <code>&quot;Net::SMTP&quot;</code>. Improvements in <code>&quot;Net::SMTP&quot;</code> authentication. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locale::Codes has been upgraded to version 3.34. </p>
<p> Fixed a bug in the scripts used to extract data from spreadsheets that prevented the <font SIZE="-1">SHP</font> currency code from being found. [cpan #94229] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=94229">https://rt.cpan.org/Ticket/Display.html?id=94229</a>&gt; </p>
<p> New codes have been added. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigInt has been upgraded to version 1.9997. </p>
<p> Synchronize <font SIZE="-1">POD</font> changes from the <font SIZE="-1">CPAN</font> release. <code>&quot;Math::BigFloat-&gt;blog(x)&quot;</code> would sometimes return <code>&quot;blog(2*x)&quot;</code> when the accuracy was greater than 70 digits. The result of <code>&quot;Math::BigFloat-&gt;bdiv()&quot;</code> in list context now satisfies <code>&quot;x = quotient * divisor + remainder&quot;</code>. </p>
<p> Correct handling of subclasses. [cpan #96254] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=96254">https://rt.cpan.org/Ticket/Display.html?id=96254</a>&gt; [cpan #96329] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=96329">https://rt.cpan.org/Ticket/Display.html?id=96329</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Metadata has been upgraded to version 1.000026. </p>
<p> Support installations on older perls with an ExtUtils::MakeMaker earlier than 6.63_03 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> overload has been upgraded to version 1.26. </p>
<p> A redundant <code>&quot;ref $sub&quot;</code> check has been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The PathTools module collection has been upgraded to version 3.56. </p>
<p> A warning from the <code>gcc</code> compiler is now avoided when building the <font SIZE="-1">XS.</font> </p>
<p> Don&#8217;t turn leading <code>&quot;//&quot;</code> into <code>&quot;/&quot;</code> on Cygwin. [perl #122635] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perl5db.pl has been upgraded to version 1.49. </p>
<p> The debugger would cause an assertion failure. [perl #124127] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124127">https://rt.perl.org/Ticket/Display.html?id=124127</a>&gt; </p>
<p> <code>&quot;fork()&quot;</code> in the debugger under <code>&quot;tmux&quot;</code> will now create a new window for the forked process. [perl #121333] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121333">https://rt.perl.org/Ticket/Display.html?id=121333</a>&gt; </p>
<p> The debugger now saves the current working directory on startup and restores it when you restart your program with <code>&quot;R&quot;</code> or <code>&quot;rerun&quot;</code>. [perl #121509] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121509">https://rt.perl.org/Ticket/Display.html?id=121509</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::scalar has been upgraded to version 0.22. </p>
<p> Reading from a position well past the end of the scalar now correctly returns end of file. [perl #123443] </p>
<p> Seeking to a negative position still fails, but no longer leaves the file position set to a negation location. </p>
<p> <code>&quot;eof()&quot;</code> on a <code>&quot;PerlIO::scalar&quot;</code> handle now properly returns true when the file position is past the 2GB mark on 32-bit systems. </p>
<p> Attempting to write at file positions impossible for the platform now fail early rather than wrapping at 4GB. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Perldoc has been upgraded to version 3.25. </p>
<p> Filehandles opened for reading or writing now have <code>&quot;:encoding(UTF-8)&quot;</code> set. [cpan #98019] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=98019">https://rt.cpan.org/Ticket/Display.html?id=98019</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">POSIX</font> has been upgraded to version 1.53. </p>
<p> The C99 math functions and constants (for example <code>&quot;acosh&quot;</code>, <code>&quot;isinf&quot;</code>, <code>&quot;isnan&quot;</code>, <code>&quot;round&quot;</code>, <code>&quot;trunc&quot;</code>; <code>&quot;M_E&quot;</code>, <code>&quot;M_SQRT2&quot;</code>, <code>&quot;M_PI&quot;</code>) have been added. </p>
<p> <code>&quot;POSIX::tmpnam()&quot;</code> now produces a deprecation warning. [perl #122005] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Safe has been upgraded to version 2.39. </p>
<p> <code>&quot;reval&quot;</code> was not propagating void context properly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Scalar-List-Utils has been upgraded to version 1.41. </p>
<p> A new module, Sub::Util, has been added, containing functions related to <font SIZE="-1">CODE</font> refs, including <code>&quot;subname&quot;</code> (inspired by <code>&quot;Sub::Identity&quot;</code>) and <code>&quot;set_subname&quot;</code> (copied and renamed from <code>&quot;Sub::Name&quot;</code>). The use of <code>&quot;GetMagic&quot;</code> in <code>&quot;List::Util::reduce()&quot;</code> has also been fixed. [cpan #63211] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=63211">https://rt.cpan.org/Ticket/Display.html?id=63211</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> SDBM_File has been upgraded to version 1.13. </p>
<p> Simplified the build process. [perl #123413] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::Piece has been upgraded to version 1.29. </p>
<p> When pretty printing negative <code>&quot;Time::Seconds&quot;</code>, the ``minus&#8217;&#8216; is no longer lost. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::Collate has been upgraded to version 1.12. </p>
<p> Version 0.67&#8217;s improved discontiguous contractions is invalidated by default and is supported as a parameter <code>&quot;long_contraction&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::Normalize has been upgraded to version 1.18. </p>
<p> The <font SIZE="-1">XSUB</font> implementation has been removed in favor of pure Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::UCD has been upgraded to version 0.61. </p>
<p> A new function <code>property_values()</code> has been added to return a given property&#8217;s possible values. </p>
<p> A new function <code>charprop()</code> has been added to return the value of a given property for a given code point. </p>
<p> A new function <code>charprops_all()</code> has been added to return the values of all Unicode properties for a given code point. </p>
<p> A bug has been fixed so that <code>propaliases()</code> returns the correct short and long names for the Perl extensions where it was incorrect. </p>
<p> A bug has been fixed so that <code>prop_value_aliases()</code> returns <code>&quot;undef&quot;</code> instead of a wrong result for properties that are Perl extensions. </p>
<p> This module now works on <font SIZE="-1">EBCDIC</font> platforms. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> utf8 has been upgraded to version 1.17 </p>
<p> A mismatch between the documentation and the code in <code>&quot;utf8::downgrade()&quot;</code> was fixed in favor of the documentation. The optional second argument is now correctly treated as a perl boolean (true/false semantics) and not as an integer. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> version has been upgraded to version 0.9909. </p>
<p> Numerous changes. See the <i>Changes</i> file in the <font SIZE="-1">CPAN</font> distribution for details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Win32 has been upgraded to version 0.51. </p>
<p> <code>&quot;GetOSName()&quot;</code> now supports Windows 8.1, and building in C<font SIZE="-2">++</font> mode now works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Win32API::File has been upgraded to version 0.1202 </p>
<p> Building in C<font SIZE="-2">++</font> mode now works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> XSLoader has been upgraded to version 0.20. </p>
<p> Allow XSLoader to load modules from a different namespace. [perl #122455] </p>
 </dd></dl>
<h3>Removed Modules and Pragmata</h3>
<p> The following modules (and associated modules) have been removed from the core perl distribution: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CGI</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Build </p>
 </dd></dl>
<h2>Documentation</h2>
<h3>New Documentation</h3>
<p> <i>perlunicook</i> </p>
<p> This document, by Tom Christiansen, provides examples of handling Unicode in Perl.  </p>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlaix</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A note on long doubles has been added. </p>
 </dd></dl>
<p> <i>perlapi</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Note that <code>&quot;SvSetSV&quot;</code> doesn&#8217;t do set magic. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sv_usepvn_flags&quot;</code> &#8211; fix documentation to mention the use of <code>&quot;Newx&quot;</code> instead of <code>&quot;malloc&quot;</code>. </p>
<p> [perl #121869] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121869">https://rt.perl.org/Ticket/Display.html?id=121869</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Clarify where <code>&quot;NUL&quot;</code> may be embedded or is required to terminate a string. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some documentation that was previously missing due to formatting errors is now included. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Entries are now organized into groups rather than by the file where they are found. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Alphabetical sorting of entries is now done consistently (automatically by the <font SIZE="-1">POD</font> generator) to make entries easier to find when scanning. </p>
 </dd></dl>
<p> <i>perldata</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The syntax of single-character variable names has been brought up-to-date and more fully explained. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hexadecimal floating point numbers are described, as are infinity and NaN. </p>
 </dd></dl>
<p> <i>perlebcdic</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> This document has been significantly updated in the light of recent improvements to <font SIZE="-1">EBCDIC</font> support. </p>
 </dd></dl>
<p> <i>perlfilter</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Added a <font SIZE="-1">LIMITATIONS</font> section. </p>
 </dd></dl>
<p> <i>perlfunc</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Mention that <code>&quot;study()&quot;</code> is currently a no-op. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calling <code>&quot;delete&quot;</code> or <code>&quot;exists&quot;</code> on array values is now described as ``strongly discouraged&#8217;&#8216; rather than ``deprecated&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Improve documentation of <code>&quot;our&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-l&quot;</code> now notes that it will return false if symlinks aren&#8217;t supported by the file system. [perl #121523] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121523">https://rt.perl.org/Ticket/Display.html?id=121523</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Note that <code>&quot;exec LIST&quot;</code> and <code>&quot;system LIST&quot;</code> may fall back to the shell on Win32. Only the indirect-object syntax <code>&quot;exec PROGRAM LIST&quot;</code> and <code>&quot;system PROGRAM LIST&quot;</code> will reliably avoid using the shell. </p>
<p> This has also been noted in perlport. </p>
<p> [perl #122046] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122046">https://rt.perl.org/Ticket/Display.html?id=122046</a>&gt; </p>
 </dd></dl>
<p> <i>perlguts</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">OOK</font> example has been updated to account for <font SIZE="-1">COW</font> changes and a change in the storage of the offset. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Details on C level symbols and libperl.t added. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Information on Unicode handling has been added </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Information on <font SIZE="-1">EBCDIC</font> handling has been added </p>
 </dd></dl>
<p> <i>perlhack</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A note has been added about running on platforms with non-ASCII character sets </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A note has been added about performance testing </p>
 </dd></dl>
<p> <i>perlhacktips</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Documentation has been added illustrating the perils of assuming that there is no change to the contents of static memory pointed to by the return values of Perl&#8217;s wrappers for C library functions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Replacements for <code>&quot;tmpfile&quot;</code>, <code>&quot;atoi&quot;</code>, <code>&quot;strtol&quot;</code>, and <code>&quot;strtoul&quot;</code> are now recommended. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Updated documentation for the <code>&quot;test.valgrind&quot;</code> <code>&quot;make&quot;</code> target. [perl #121431] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121431">https://rt.perl.org/Ticket/Display.html?id=121431</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Information is given about writing test files portably to non-ASCII platforms. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A note has been added about how to get a C language stack backtrace. </p>
 </dd></dl>
<p> <i>perlhpux</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Note that the message ``Redeclaration of &#8216;&#8216;sendpath`` with a different storage class specifier&#8217;&#8216; is harmless. </p>
 </dd></dl>
<p> <i>perllocale</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Updated for the enhancements in v5.22, along with some clarifications. </p>
 </dd></dl>
<p> <i>perlmodstyle</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Instead of pointing to the module list, we are now pointing to PrePAN &lt;<a rel="nofollow" href="http://prepan.org/">http://prepan.org/</a>&gt;. </p>
 </dd></dl>
<p> <i>perlop</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Updated for the enhancements in v5.22, along with some clarifications. </p>
 </dd></dl>
<p> <i>perlpodspec</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The specification of the pod language is changing so that the default encoding of pods that aren&#8217;t in <font SIZE="-1">UTF-8</font> (unless otherwise indicated) is <font SIZE="-1">CP1252</font> instead of <font SIZE="-1">ISO 8859-1</font> (Latin1). </p>
 </dd></dl>
<p> <i>perlpolicy</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> We now have a code of conduct for the <i>p5p</i> mailing list, as documented in ``<font SIZE="-1">STANDARDS OF CONDUCT&#8217;&#8216;</font> in perlpolicy. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The conditions for marking an experimental feature as non-experimental are now set out. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Clarification has been made as to what sorts of changes are permissible in maintenance releases. </p>
 </dd></dl>
<p> <i>perlport</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Out-of-date VMS-specific information has been fixed and/or simplified. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Notes about <font SIZE="-1">EBCDIC</font> have been added. </p>
 </dd></dl>
<p> <i>perlre</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The description of the <code>&quot;/x&quot;</code> modifier has been clarified to note that comments cannot be continued onto the next line by escaping them; and there is now a list of all the characters that are considered whitespace by this modifier. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The new <code>&quot;/n&quot;</code> modifier is described. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A note has been added on how to make bracketed character class ranges portable to non-ASCII machines. </p>
 </dd></dl>
<p> <i>perlrebackslash</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Added documentation of <code>&quot;\b{sb}&quot;</code>, <code>&quot;\b{wb}&quot;</code>, <code>&quot;\b{gcb}&quot;</code>, and <code>&quot;\b{g}&quot;</code>. </p>
 </dd></dl>
<p> <i>perlrecharclass</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Clarifications have been added to ``Character Ranges&#8217;&#8216; in perlrecharclass to the effect <code>&quot;[A-Z]&quot;</code>, <code>&quot;[a-z]&quot;</code>, <code>&quot;[0-9]&quot;</code> and any subranges thereof in regular expression bracketed character classes are guaranteed to match exactly what a naive English speaker would expect them to match, even on platforms (such as <font SIZE="-1">EBCDIC</font>) where perl has to do extra work to accomplish this. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The documentation of Bracketed Character Classes has been expanded to cover the improvements in <code>&quot;qr/[\N{named sequence}]/&quot;</code> (see under ``Selected Bug Fixes&#8217;&#8216;). </p>
 </dd></dl>
<p> <i>perlref</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A new section has been added Assigning to References </p>
 </dd></dl>
<p> <i>perlsec</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Comments added on algorithmic complexity and tied hashes. </p>
 </dd></dl>
<p> <i>perlsyn</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> An ambiguity in the documentation of the <code>&quot;...&quot;</code> statement has been corrected. [perl #122661] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122661">https://rt.perl.org/Ticket/Display.html?id=122661</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The empty conditional in <code>&quot;for&quot;</code> and <code>&quot;while&quot;</code> is now documented in perlsyn. </p>
 </dd></dl>
<p> <i>perlunicode</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> This has had extensive revisions to bring it up-to-date with current Unicode support and to make it more readable. Notable is that Unicode 7.0 changed what it should do with non-characters. Perl retains the old way of handling for reasons of backward compatibility. See ``Noncharacter code points&#8217;&#8216; in perlunicode. </p>
 </dd></dl>
<p> <i>perluniintro</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Advice for how to make sure your strings and regular expression patterns are interpreted as Unicode has been updated. </p>
 </dd></dl>
<p> <i>perlvar</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>$]</code> is no longer listed as being deprecated. Instead, discussion has been added on the advantages and disadvantages of using it versus <code>$^V</code>. <code>$OLD_PERL_VERSION</code> was re-added to the documentation as the long form of <code>$]</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;${^ENCODING}&quot;</code> is now marked as deprecated. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The entry for <code>&quot;%^H&quot;</code> has been clarified to indicate it can only handle simple values. </p>
 </dd></dl>
<p> <i>perlvms</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Out-of-date and/or incorrect material has been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Updated documentation on environment and shell interaction in <font SIZE="-1">VMS.</font> </p>
 </dd></dl>
<p> <i>perlxs</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Added a discussion of locale issues in <font SIZE="-1">XS</font> code. </p>
 </dd></dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.  </p>
<h3>New Diagnostics</h3>
<p> <i>New Errors</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Bad symbol for scalar </p>
<p> (P) An internal request asked to add a scalar entry to something that wasn&#8217;t a symbol table entry. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can&#8217;t use a hash as a reference </p>
<p> (F) You tried to use a hash as a reference, as in <code>&quot;%foo-&gt;{&quot;bar&quot;}&quot;</code> or <code>&quot;%$ref-&gt;{&quot;hello&quot;}&quot;</code>. Versions of perl &lt;= 5.6.1 used to allow this syntax, but shouldn&#8217;t have. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can&#8217;t use an array as a reference </p>
<p> (F) You tried to use an array as a reference, as in <code>&quot;@foo-&gt;[23]&quot;</code> or <code>&quot;@$ref-&gt;[99]&quot;</code>. Versions of perl &lt;= 5.6.1 used to allow this syntax, but shouldn&#8217;t have. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can&#8217;t use &#8216;defined(@array)&#8216; (Maybe you should just omit the <code>defined()</code>?) </p>
<p> (F) <code>&quot;defined()&quot;</code> is not useful on arrays because it checks for an undefined <i>scalar</i> value. If you want to see if the array is empty, just use <code>&quot;if (@array) { # not empty }&quot;</code> for example. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can&#8217;t use &#8216;defined(%hash)&#8216; (Maybe you should just omit the <code>defined()</code>?) </p>
<p> (F) <code>&quot;defined()&quot;</code> is not usually right on hashes. </p>
<p> Although <code>&quot;defined %hash&quot;</code> is false on a plain not-yet-used hash, it becomes true in several non-obvious circumstances, including iterators, weak references, stash names, even remaining true after <code>&quot;undef %hash&quot;</code>. These things make <code>&quot;defined %hash&quot;</code> fairly useless in practice, so it now generates a fatal error. </p>
<p> If a check for non-empty is what you wanted then just put it in boolean context (see ``Scalar values&#8217;&#8216; in perldata): </p>
<pre><code>    if (%hash) {
       # not empty
    }
</code></pre>
<p> If you had <code>&quot;defined %Foo::Bar::QUUX&quot;</code> to check whether such a package variable exists then that&#8217;s never really been reliable, and isn&#8217;t a good way to enquire about the features of a package, or whether it&#8217;s loaded, etc. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Cannot chr <code>%f</code> </p>
<p> (F) You passed an invalid number (like an infinity or not-a-number) to <code>&quot;chr&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Cannot compress <code>%f</code> in pack </p>
<p> (F) You tried converting an infinity or not-a-number to an unsigned character, which makes no sense. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Cannot pack <code>%f</code> with &#8216;%c&#8217; </p>
<p> (F) You tried converting an infinity or not-a-number to a character, which makes no sense. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Cannot print <code>%f</code> with &#8216;%c&#8217; </p>
<p> (F) You tried printing an infinity or not-a-number as a character (<code>%c</code>), which makes no sense. Maybe you meant <code>&#8216;%s&#8217;</code>, or just stringifying it? </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> charnames alias definitions may not contain a sequence of multiple spaces </p>
<p> (F) You defined a character name which had multiple space characters in a row. Change them to single spaces. Usually these names are defined in the <code>&quot;:alias&quot;</code> import argument to <code>&quot;use charnames&quot;</code>, but they could be defined by a translator installed into <code>$^H{charnames}</code>. See ``<font SIZE="-1">CUSTOM ALIASES&#8217;&#8216;</font> in charnames. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> charnames alias definitions may not contain trailing white-space </p>
<p> (F) You defined a character name which ended in a space character. Remove the trailing space(s). Usually these names are defined in the <code>&quot;:alias&quot;</code> import argument to <code>&quot;use charnames&quot;</code>, but they could be defined by a translator installed into <code>$^H{charnames}</code>. See ``<font SIZE="-1">CUSTOM ALIASES&#8217;&#8216;</font> in charnames. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> :const is not permitted on named subroutines </p>
<p> (F) The <code>&quot;const&quot;</code> attribute causes an anonymous subroutine to be run and its value captured at the time that it is cloned. Named subroutines are not cloned like this, so the attribute does not make sense on them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hexadecimal float: internal error </p>
<p> (F) Something went horribly bad in hexadecimal float handling. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hexadecimal float: unsupported long double format </p>
<p> (F) You have configured Perl to use long doubles but the internals of the long double format are unknown, therefore the hexadecimal float output is impossible. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Illegal suidscript </p>
<p> (F) The script run under suidperl was somehow illegal. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In &#8216;(?...)&#8216;, the &#8216;(&#8216; and &#8216;?&#8216; must be adjacent in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
<p> (F) The two-character sequence <code>&quot;(?&quot;</code> in this context in a regular expression pattern should be an indivisible token, with nothing intervening between the <code>&quot;(&quot;</code> and the <code>&quot;?&quot;</code>, but you separated them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In &#8216;(*VERB...)&#8216;, the &#8216;(&#8216; and &#8216;*&#8216; must be adjacent in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
<p> (F) The two-character sequence <code>&quot;(*&quot;</code> in this context in a regular expression pattern should be an indivisible token, with nothing intervening between the <code>&quot;(&quot;</code> and the <code>&quot;*&quot;</code>, but you separated them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Invalid quantifier in {,} in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
<p> (F) The pattern looks like a {min,max} quantifier, but the min or max could not be parsed as a valid number: either it has leading zeroes, or it represents too big a number to cope with. The &lt;-- <font SIZE="-1">HERE</font> shows where in the regular expression the problem was discovered. See perlre. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> &#8216;%s&#8217; is an unknown bound type in regex </p>
<p> (F) You used <code>&quot;\b{...}&quot;</code> or <code>&quot;\B{...}&quot;</code> and the <code>&quot;...&quot;</code> is not known to Perl. The current valid ones are given in ``\b{}, \b, \B{}, \B&#8217;&#8216; in perlrebackslash. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Missing or undefined argument to require </p>
<p> (F) You tried to call <code>&quot;require&quot;</code> with no argument or with an undefined value as an argument. <code>&quot;require&quot;</code> expects either a package name or a file-specification as an argument. See ``require&#8217;&#8216; in perlfunc. </p>
<p> Formerly, <code>&quot;require&quot;</code> with no argument or <code>&quot;undef&quot;</code> warned about a Null filename. </p>
 </dd></dl>
<p> <i>New Warnings</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> \C is deprecated in regex </p>
<p> (D deprecated) The <code>&quot;/\C/&quot;</code> character class was deprecated in v5.20, and now emits a warning. It is intended that it will become an error in v5.24. This character class matches a single byte even if it appears within a multi-byte character, breaks encapsulation, and can corrupt <font SIZE="-1">UTF-8</font> strings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ``%s&#8217;&#8216; is more clearly written simply as ``%s&#8217;&#8216; in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
<p> (W regexp) (only under <code>&quot;use re &#8216;strict&#8217;&quot;</code> or within <code>&quot;(?[...])&quot;</code>) </p>
<p> You specified a character that has the given plainer way of writing it, and which is also portable to platforms running with different character sets. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Argument ``%s&#8217;&#8216; treated as 0 in increment (++) </p>
<p> (W numeric) The indicated string was fed as an argument to the <code>&quot;++&quot;</code> operator which expects either a number or a string matching <code>&quot;/^[a-zA-Z]*[0-9]*\z/&quot;</code>. See ``Auto-increment and Auto-decrement&#8217;&#8216; in perlop for details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Both or neither range ends should be Unicode in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
<p> (W regexp) (only under <code>&quot;use re &#8216;strict&#8217;&quot;</code> or within <code>&quot;(?[...])&quot;</code>) </p>
<p> In a bracketed character class in a regular expression pattern, you had a range which has exactly one end of it specified using <code>&quot;\N{}&quot;</code>, and the other end is specified using a non-portable mechanism. Perl treats the range as a Unicode range, that is, all the characters in it are considered to be the Unicode characters, and which may be different code points on some platforms Perl runs on. For example, <code>&quot;[\N{U+06}-\x08]&quot;</code> is treated as if you had instead said <code>&quot;[\N{U+06}-\N{U+08}]&quot;</code>, that is it matches the characters whose code points in Unicode are 6, 7, and 8. But that <code>&quot;\x08&quot;</code> might indicate that you meant something different, so the warning gets raised. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can&#8217;t do %s(``%s&#8217;&#8216;) on non-UTF-8 locale; resolved to ``%s&#8217;&#8216;. </p>
<p> (W locale) You are 1) running under &quot;<code>&quot;use locale&quot;</code>&quot;; 2) the current locale is not a <font SIZE="-1">UTF-8</font> one; 3) you tried to do the designated case-change operation on the specified Unicode character; and 4) the result of this operation would mix Unicode and locale rules, which likely conflict. </p>
<p> The warnings category <code>&quot;locale&quot;</code> is new. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> :const is experimental </p>
<p> (S experimental::const_attr) The <code>&quot;const&quot;</code> attribute is experimental. If you want to use the feature, disable the warning with <code>&quot;no warnings &#8216;experimental::const_attr&#8217;&quot;</code>, but know that in doing so you are taking the risk that your code may break in a future Perl version. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> gmtime(%f) failed </p>
<p> (W overflow) You called <code>&quot;gmtime&quot;</code> with a number that it could not handle: too large, too small, or NaN. The returned value is <code>&quot;undef&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hexadecimal float: exponent overflow </p>
<p> (W overflow) The hexadecimal floating point has larger exponent than the floating point supports. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hexadecimal float: exponent underflow </p>
<p> (W overflow) The hexadecimal floating point has smaller exponent than the floating point supports. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hexadecimal float: mantissa overflow </p>
<p> (W overflow) The hexadecimal floating point literal had more bits in the mantissa (the part between the <code>&quot;0x&quot;</code> and the exponent, also known as the fraction or the significand) than the floating point supports. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hexadecimal float: precision loss </p>
<p> (W overflow) The hexadecimal floating point had internally more digits than could be output. This can be caused by unsupported long double formats, or by 64-bit integers not being available (needed to retrieve the digits under some configurations). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locale &#8216;%s&#8217; may not work well.%s </p>
<p> (W locale) You are using the named locale, which is a non-UTF-8 one, and which perl has determined is not fully compatible with what it can handle. The second <code>%s</code> gives a reason. </p>
<p> The warnings category <code>&quot;locale&quot;</code> is new. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> localtime(%f) failed </p>
<p> (W overflow) You called <code>&quot;localtime&quot;</code> with a number that it could not handle: too large, too small, or NaN. The returned value is <code>&quot;undef&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Negative repeat count does nothing </p>
<p> (W numeric) You tried to execute the <code>&quot;x&quot;</code> repetition operator fewer than 0 times, which doesn&#8217;t make sense. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> NO-BREAK <font SIZE="-1">SPACE</font> in a charnames alias definition is deprecated </p>
<p> (D deprecated) You defined a character name which contained a no-break space character. Change it to a regular space. Usually these names are defined in the <code>&quot;:alias&quot;</code> import argument to <code>&quot;use charnames&quot;</code>, but they could be defined by a translator installed into <code>$^H{charnames}</code>. See ``<font SIZE="-1">CUSTOM ALIASES&#8217;&#8216;</font> in charnames. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Non-finite repeat count does nothing </p>
<p> (W numeric) You tried to execute the <code>&quot;x&quot;</code> repetition operator <code>&quot;Inf&quot;</code> (or <code>&quot;-Inf&quot;</code>) or NaN times, which doesn&#8217;t make sense. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO layer &#8216;:win32&#8217; is experimental </p>
<p> (S experimental::win32_perlio) The <code>&quot;:win32&quot;</code> PerlIO layer is experimental. If you want to take the risk of using this layer, simply disable this warning: </p>
<pre><code>    no warnings &quot;experimental::win32_perlio&quot;;
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Ranges of <font SIZE="-1">ASCII</font> printables should be some subset of ``0-9&#8217;&#8216;, ``A-Z&#8217;&#8216;, or ``a-z&#8217;&#8216; in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
<p> (W regexp) (only under <code>&quot;use re &#8216;strict&#8217;&quot;</code> or within <code>&quot;(?[...])&quot;</code>) </p>
<p> Stricter rules help to find typos and other errors. Perhaps you didn&#8217;t even intend a range here, if the <code>&quot;-&quot;</code> was meant to be some other character, or should have been escaped (like <code>&quot;\-&quot;</code>). If you did intend a range, the one that was used is not portable between <font SIZE="-1">ASCII</font> and <font SIZE="-1">EBCDIC</font> platforms, and doesn&#8217;t have an obvious meaning to a casual reader. </p>
<pre><code> [3-7] # OK; Obvious and portable
 [d-g] # OK; Obvious and portable
 [A-Y] # OK; Obvious and portable
 [A-z] # WRONG; Not portable; not clear what is meant
 [a-Z] # WRONG; Not portable; not clear what is meant
 [%-.] # WRONG; Not portable; not clear what is meant
 [\x41-Z] # WRONG; Not portable; not obvious to non-geek
</code></pre>
<p> (You can force portability by specifying a Unicode range, which means that the endpoints are specified by <code>&quot;\N{...}&quot;</code>, but the meaning may still not be obvious.) The stricter rules require that ranges that start or stop with an <font SIZE="-1">ASCII</font> character that is not a control have all their endpoints be a literal character, and not some escape sequence (like <code>&quot;\x41&quot;</code>), and the ranges must be all digits, or all uppercase letters, or all lowercase letters. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Ranges of digits should be from the same group in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
<p> (W regexp) (only under <code>&quot;use re &#8216;strict&#8217;&quot;</code> or within <code>&quot;(?[...])&quot;</code>) </p>
<p> Stricter rules help to find typos and other errors. You included a range, and at least one of the end points is a decimal digit. Under the stricter rules, when this happens, both end points should be digits in the same group of 10 consecutive digits. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Redundant argument in <code>%s</code> </p>
<p> (W redundant) You called a function with more arguments than were needed, as indicated by information within other arguments you supplied (<i>e.g</i>. a printf format). Currently only emitted when a printf-type format required fewer arguments than were supplied, but might be used in the future for <i>e.g.</i> ``pack&#8217;&#8216; in perlfunc. </p>
<p> The warnings category <code>&quot;redundant&quot;</code> is new. See also [perl #121025] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121025">https://rt.perl.org/Ticket/Display.html?id=121025</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Replacement list is longer than search list </p>
<p> This is not a new diagnostic, but in earlier releases was accidentally not displayed if the transliteration contained wide characters. This is now fixed, so that you may see this diagnostic in places where you previously didn&#8217;t (but should have). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of \b{} for non-UTF-8 locale is wrong. Assuming a <font SIZE="-1">UTF-8</font> locale </p>
<p> (W locale) You are matching a regular expression using locale rules, and a Unicode boundary is being matched, but the locale is not a Unicode one. This doesn&#8217;t make sense. Perl will continue, assuming a Unicode (<font SIZE="-1">UTF-8</font>) locale, but the results could well be wrong except if the locale happens to be <font SIZE="-1">ISO-8859-1</font> (Latin1) where this message is spurious and can be ignored. </p>
<p> The warnings category <code>&quot;locale&quot;</code> is new. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using /u for &#8216;%s&#8217; instead of /%s in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
<p> (W regexp) You used a Unicode boundary (<code>&quot;\b{...}&quot;</code> or <code>&quot;\B{...}&quot;</code>) in a portion of a regular expression where the character set modifiers <code>&quot;/a&quot;</code> or <code>&quot;/aa&quot;</code> are in effect. These two modifiers indicate an <font SIZE="-1">ASCII</font> interpretation, and this doesn&#8217;t make sense for a Unicode definition. The generated regular expression will compile so that the boundary uses all of Unicode. No other portion of the regular expression is affected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The bitwise feature is experimental </p>
<p> (S experimental::bitwise) This warning is emitted if you use bitwise operators (<code>&quot;&amp; | ^ ~ &amp;. |. ^. ~.&quot;</code>) with the ``bitwise&#8217;&#8216; feature enabled. Simply suppress the warning if you want to use the feature, but know that in doing so you are taking the risk of using an experimental feature which may change or be removed in a future Perl version: </p>
<pre><code>    no warnings &quot;experimental::bitwise&quot;;
    use feature &quot;bitwise&quot;;
    $x |.= $y;
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unescaped left brace in regex is deprecated, passed through in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
<p> (D deprecated, regexp) You used a literal <code>&quot;{&quot;</code> character in a regular expression pattern. You should change to use <code>&quot;\{&quot;</code> instead, because a future version of Perl (tentatively v5.26) will consider this to be a syntax error. If the pattern delimiters are also braces, any matching right brace (<code>&quot;}&quot;</code>) should also be escaped to avoid confusing the parser, for example, </p>
<pre><code>    qr{abc\{def\}ghi}
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of literal non-graphic characters in variable names is deprecated </p>
<p> (D deprecated) Using literal non-graphic (including control) characters in the source to refer to the <i>^FOO</i> variables, like <code>$^X</code> and <code>&quot;${^GLOBAL_PHASE}&quot;</code> is now deprecated. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Useless use of attribute ``const&#8217;&#8216; </p>
<p> (W misc) The <code>&quot;const&quot;</code> attribute has no effect except on anonymous closure prototypes. You applied it to a subroutine via attributes.pm. This is only useful inside an attribute handler for an anonymous subroutine. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Useless use of /d modifier in transliteration operator </p>
<p> This is not a new diagnostic, but in earlier releases was accidentally not displayed if the transliteration contained wide characters. This is now fixed, so that you may see this diagnostic in places where you previously didn&#8217;t (but should have). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ``use re &#8216;strict&#8217;&#8216;&#8216; is experimental </p>
<p> (S experimental::re_strict) The things that are different when a regular expression pattern is compiled under <code>&#8216;strict&#8217;</code> are subject to change in future Perl releases in incompatible ways; there are also proposals to change how to enable strict checking instead of using this subpragma. This means that a pattern that compiles today may not in a future Perl release. This warning is to alert you to that risk. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Warning: unable to close filehandle properly: <code>%s</code> </p>
<p> Warning: unable to close filehandle <code>%s</code> properly: <code>%s</code> </p>
<p> (S io) Previously, perl silently ignored any errors when doing an implicit close of a filehandle, <i>i.e.</i> where the reference count of the filehandle reached zero and the user&#8217;s code hadn&#8217;t already called <code>&quot;close()&quot;</code>; <i>e.g.</i> </p>
<pre><code>    {
        open my $fh, '&gt;', $file or die &quot;open: '$file': $!\n&quot;;
        print $fh, $data or die;
    } # implicit close here
</code></pre>
<p> In a situation such as disk full, due to buffering, the error may only be detected during the final close, so not checking the result of the close is dangerous. </p>
<p> So perl now warns in such situations. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Wide character (U+%X) in <code>%s</code> </p>
<p> (W locale) While in a single-byte locale (<i>i.e.</i>, a non-UTF-8 one), a multi-byte character was encountered. Perl considers this character to be the specified Unicode code point. Combining non-UTF-8 locales and Unicode is dangerous. Almost certainly some characters will have two different representations. For example, in the <font SIZE="-1">ISO 8859-7</font> (Greek) locale, the code point 0xC3 represents a Capital Gamma. But so also does 0x393. This will make string comparisons unreliable. </p>
<p> You likely need to figure out how this multi-byte character got mixed up with your single-byte locale (or perhaps you thought you had a <font SIZE="-1">UTF-8</font> locale, but Perl disagrees). </p>
<p> The warnings category <code>&quot;locale&quot;</code> is new. </p>
 </dd></dl>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> &lt;&gt; should be quotes </p>
<p> This warning has been changed to &lt;&gt; at require-statement should be quotes to make the issue more identifiable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Argument ``%s&#8217;&#8216; isn&#8217;t numeric%s </p>
<p> The perldiag entry for this warning has added this clarifying note: </p>
<pre><code> Note that for the Inf and NaN (infinity and not-a-number) the
 definition of &quot;numeric&quot; is somewhat unusual: the strings themselves
 (like &quot;Inf&quot;) are considered numeric, and anything following them is
 considered non-numeric.
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Global symbol ``%s&#8217;&#8216; requires explicit package name </p>
<p> This message has had &#8216;(did you forget to declare ``my <code>%s</code>&#8216;&#8216;?)&#8216; appended to it, to make it more helpful to new Perl programmers. [perl #121638] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121638">https://rt.perl.org/Ticket/Display.html?id=121638</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> &#8216;``my&#8217;&#8216; variable &amp;foo::bar can&#8217;t be in a package&#8217; has been reworded to say &#8216;subroutine&#8217; instead of &#8216;variable&#8217;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> \N{} in character class restricted to one character in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
<p> This message has had <i>character class</i> changed to <i>inverted character class or as a range end-point is</i> to reflect improvements in <code>&quot;qr/[\N{named sequence}]/&quot;</code> (see under ``Selected Bug Fixes&#8217;&#8216;). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> panic: frexp </p>
<p> This message has had &#8216;: <code>%f</code>&#8216; appended to it, to show what the offending floating point number is. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Possible precedence problem on bitwise </i>%c <i> operator</i> reworded as Possible precedence problem on bitwise <code>%s</code> operator. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unsuccessful <code>%s</code> on filename containing newline </p>
<p> This warning is now only produced when the newline is at the end of the filename. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> &quot;Variable <code>%s</code> will not stay shared`` has been changed to say &#8216;&#8216;Subroutine&quot; when it is actually a lexical sub that will not stay shared. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Variable length lookbehind not implemented in regex m/%s/ </p>
<p> The perldiag entry for this warning has had information about Unicode behavior added. </p>
 </dd></dl>
<h3>Diagnostic Removals</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> ``Ambiguous use of -foo resolved as -&amp;<code>foo()</code>&#8216;&#8216; </p>
<p> There is actually no ambiguity here, and this impedes the use of negated constants; <i>e.g.</i>, <code>&quot;-Inf&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ``Constant is not a <font SIZE="-1">FOO</font> reference&#8217;&#8216; </p>
<p> Compile-time checking of constant dereferencing (<i>e.g.</i>, <code>&quot;my_constant-&gt;()&quot;</code>) has been removed, since it was not taking overloading into account. [perl #69456] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=69456">https://rt.perl.org/Ticket/Display.html?id=69456</a>&gt; [perl #122607] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122607">https://rt.perl.org/Ticket/Display.html?id=122607</a>&gt; </p>
 </dd></dl>
<h2>Utility Changes</h2>
<i></i><i></i><i></i><h3>find2perl , s2p and a2p removal</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The <i>x2p/</i> directory has been removed from the Perl core. </p>
<p> This removes find2perl, s2p and a2p. They have all been released to <font SIZE="-1">CPAN</font> as separate distributions (<code>&quot;App::find2perl&quot;</code>, <code>&quot;App::s2p&quot;</code>, <code>&quot;App::a2p&quot;</code>). </p>
 </dd></dl>
<h3>h2ph</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <i>h2ph</i> now handles hexadecimal constants in the compiler&#8217;s predefined macro definitions, as visible in <code>$Config{cppsymbols}</code>. [perl #123784] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123784">https://rt.perl.org/Ticket/Display.html?id=123784</a>&gt;. </p>
 </dd></dl>
<h3>encguess</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> No longer depends on non-core modules. </p>
 </dd></dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <i>Configure</i> now checks for <code>&quot;lrintl()&quot;</code>, <code>&quot;lroundl()&quot;</code>, <code>&quot;llrintl()&quot;</code>, and <code>&quot;llroundl()&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Configure</i> with <code>&quot;-Dmksymlinks&quot;</code> should now be faster. [perl #122002] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122002">https://rt.perl.org/Ticket/Display.html?id=122002</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;pthreads&quot;</code> and <code>&quot;cl&quot;</code> libraries will be linked by default if present. This allows <font SIZE="-1">XS</font> modules that require threading to work on non-threaded perls. Note that you must still pass <code>&quot;-Dusethreads&quot;</code> if you want a threaded perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> To get more precision and range for floating point numbers one can now use the <font SIZE="-1">GCC</font> quadmath library which implements the quadruple precision floating point numbers on x86 and <font SIZE="-1">IA-64</font> platforms. See <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> for details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> MurmurHash64A and MurmurHash64B can now be configured as the internal hash function. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;make test.valgrind&quot;</code> now supports parallel testing. </p>
<p> For example: </p>
<pre><code>    TEST_JOBS=9 make test.valgrind
</code></pre>
<p> See ``valgrind&#8217;&#8216; in perlhacktips for more information. </p>
<p> [perl #121431] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121431">https://rt.perl.org/Ticket/Display.html?id=121431</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">MAD</font> (Misc Attribute Decoration) build option has been removed </p>
<p> This was an unmaintained attempt at preserving the Perl parse tree more faithfully so that automatic conversion of Perl 5 to Perl 6 would have been easier. </p>
<p> This build-time configuration option had been unmaintained for years, and had probably seriously diverged on both Perl 5 and Perl 6 sides. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new compilation flag, <code>&quot;-DPERL_OP_PARENT&quot;</code> is available. For details, see the discussion below at ``Internal Changes&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pathtools no longer tries to load <font SIZE="-1">XS</font> on miniperl. This speeds up building perl slightly. </p>
 </dd></dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <i>t/porting/re_context.t</i> has been added to test that utf8 and its dependencies only use the subset of the <code>&quot;$1..$n&quot;</code> capture vars that <code>&quot;Perl_save_re_context()&quot;</code> is hard-coded to localize, because that function has no efficient way of determining at runtime what vars to localize. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tests for performance issues have been added in the file <i>t/perf/taint.t</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some regular expression tests are written in such a way that they will run very slowly if certain optimizations break. These tests have been moved into new files, <i>t/re/speed.t</i> and <i>t/re/speed_thr.t</i>, and are run with a <code>&quot;watchdog()&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;test.pl&quot;</code> now allows <code>&quot;plan skip_all =&gt; $reason&quot;</code>, to make it more compatible with <code>&quot;Test::More&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new test script, <i>op/infnan.t</i>, has been added to test if infinity and NaN are working correctly. See ``Infinity and NaN (not-a-number) handling improved&#8217;&#8216;. </p>
 </dd></dl>
<h2>Platform Support</h2>
<h3>Regained Platforms</h3>
<dl>
<dt><font SIZE="-1">IRIX</font> and Tru64 platforms are working again.</dt>
<dd> <p> Some <code>&quot;make test&quot;</code> failures remain: [perl #123977] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123977">https://rt.perl.org/Ticket/Display.html?id=123977</a>&gt; and [perl #125298] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125298">https://rt.perl.org/Ticket/Display.html?id=125298</a>&gt; for <font SIZE="-1">IRIX</font>; [perl #124212] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124212">https://rt.perl.org/Ticket/Display.html?id=124212</a>&gt;, [cpan #99605] &lt;<a rel="nofollow" href="https://rt.cpan.org/Public/Bug/Display.html?id=99605">https://rt.cpan.org/Public/Bug/Display.html?id=99605</a>&gt;, and [cpan #104836] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=104836">https://rt.cpan.org/Ticket/Display.html?id=104836</a>&gt; for Tru64. </p>
 </dd>
<dt>z/OS running <font SIZE="-1">EBCDIC</font> Code Page 1047</dt>
<dd> <p> Core perl now works on this <font SIZE="-1">EBCDIC</font> platform. Earlier perls also worked, but, even though support wasn&#8217;t officially withdrawn, recent perls would not compile and run well. Perl 5.20 would work, but had many bugs which have now been fixed. Many <font SIZE="-1">CPAN</font> modules that ship with Perl still fail tests, including <code>&quot;Pod::Simple&quot;</code>. However the version of <code>&quot;Pod::Simple&quot;</code> currently on <font SIZE="-1">CPAN</font> should work; it was fixed too late to include in Perl 5.22. Work is under way to fix many of the still-broken <font SIZE="-1">CPAN</font> modules, which likely will be installed on <font SIZE="-1">CPAN</font> when completed, so that you may not have to wait until Perl 5.24 to get a working version. </p>
 </dd></dl>
<h3>Discontinued Platforms</h3>
<dl>
<dt>NeXTSTEP/OPENSTEP</dt>
<dd> <p> NeXTSTEP was a proprietary operating system bundled with NeXT&#8217;s workstations in the early to mid 90s; <font SIZE="-1">OPENSTEP</font> was an <font SIZE="-1">API</font> specification that provided a NeXTSTEP-like environment on a non-NeXTSTEP system. Both are now long dead, so support for building Perl on them has been removed. </p>
 </dd></dl>
<h3>Platform-Specific Notes</h3>
<dl>
<dt><font SIZE="-1">EBCDIC</font></dt>
<dd> <p> Special handling is required of the perl interpreter on <font SIZE="-1">EBCDIC</font> platforms to get <code>&quot;qr/[i-j]/&quot;</code> to match only <code>&quot;i&quot;</code> and <code>&quot;j&quot;</code>, since there are 7 characters between the code points for <code>&quot;i&quot;</code> and <code>&quot;j&quot;</code>. This special handling had only been invoked when both ends of the range are literals. Now it is also invoked if any of the <code>&quot;\N{...}&quot;</code> forms for specifying a character by name or Unicode code point is used instead of a literal. See ``Character Ranges&#8217;&#8216; in perlrecharclass. </p>
 </dd>
<dt>HP-UX</dt>
<dd> <p> The archname now distinguishes use64bitint from use64bitall. </p>
 </dd>
<dt>Android</dt>
<dd> <p> Build support has been improved for cross-compiling in general and for Android in particular. </p>
 </dd>
<dt><font SIZE="-1">VMS</font></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> When spawning a subprocess without waiting, the return value is now the correct <font SIZE="-1">PID.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix a prototype so linking doesn&#8217;t fail under the <font SIZE="-1">VMS C<font SIZE="-2">++</font></font> compiler. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;finite&quot;</code>, <code>&quot;finitel&quot;</code>, and <code>&quot;isfinite&quot;</code> detection has been added to <code>&quot;configure.com&quot;</code>, environment handling has had some minor changes, and a fix for legacy feature checking status. </p>
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
<dd> <p> <i>miniperl.exe</i> is now built with <code>&quot;-fno-strict-aliasing&quot;</code>, allowing 64-bit builds to complete on <font SIZE="-1">GCC 4.8.</font> [perl #123976] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123976">https://rt.perl.org/Ticket/Display.html?id=123976</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;nmake minitest&quot;</code> now works on Win32. Due to dependency issues you need to build <code>&quot;nmake test-prep&quot;</code> first, and a small number of the tests fail. [perl #123394] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123394">https://rt.perl.org/Ticket/Display.html?id=123394</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl can now be built in C<font SIZE="-2">++</font> mode on Windows by setting the makefile macro <code>&quot;USE_CPLUSPLUS&quot;</code> to the value ``define&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The list form of piped open has been implemented for Win32. Note: unlike <code>&quot;system LIST&quot;</code> this does not fall back to the shell. [perl #121159] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121159">https://rt.perl.org/Ticket/Display.html?id=121159</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> New <code>&quot;DebugSymbols&quot;</code> and <code>&quot;DebugFull&quot;</code> configuration options added to Windows makefiles. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Previously, compiling <font SIZE="-1">XS</font> modules (including <font SIZE="-1">CPAN</font> ones) using Visual C<font SIZE="-2">++</font> for Win64 resulted in around a dozen warnings per file from <i>hv_func.h</i>. These warnings have been silenced. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Support for building without PerlIO has been removed from the Windows makefiles. Non-PerlIO builds were all but deprecated in Perl 5.18.0 and are already not supported by <i>Configure</i> on <font SIZE="-1">POSIX</font> systems. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Between 2 and 6 milliseconds and seven I/O calls have been saved per attempt to open a perl module for each path in <code>@INC</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Intel C builds are now always built with C99 mode on. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>%I64d</code> is now being used instead of <code>%lld</code> for MinGW. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In the experimental <code>&quot;:win32&quot;</code> layer, a crash in <code>&quot;open&quot;</code> was fixed. Also opening <i>/dev/null</i> (which works under Win32 Perl&#8217;s default <code>&quot;:unix&quot;</code> layer) was implemented for <code>&quot;:win32&quot;</code>. [perl #122224] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122224">https://rt.perl.org/Ticket/Display.html?id=122224</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new makefile option, <code>&quot;USE_LONG_DOUBLE&quot;</code>, has been added to the Windows dmake makefile for gcc builds only. Set this to ``define&#8217;&#8216; if you want perl to use long doubles to give more accuracy and range for floating point numbers. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>OpenBSD</dt>
<dd> <p> On OpenBSD, Perl will now default to using the system <code>&quot;malloc&quot;</code> due to the security features it provides. Perl&#8217;s own malloc wrapper has been in use since v5.14 due to performance reasons, but the OpenBSD project believes the tradeoff is worth it and would prefer that users who need the speed specifically ask for it. </p>
<p> [perl #122000] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122000">https://rt.perl.org/Ticket/Display.html?id=122000</a>&gt;. </p>
 </dd>
<dt>Solaris</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> We now look for the Sun Studio compiler in both <i>/opt/solstudio*</i> and <i>/opt/solarisstudio*</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Builds on Solaris 10 with <code>&quot;-Dusedtrace&quot;</code> would fail early since make didn&#8217;t follow implied dependencies to build <code>&quot;perldtrace.h&quot;</code>. Added an explicit dependency to <code>&quot;depend&quot;</code>. [perl #120120] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=120120">https://rt.perl.org/Ticket/Display.html?id=120120</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> C99 options have been cleaned up; hints look for <code>&quot;solstudio&quot;</code> as well as <code>&quot;SUNWspro&quot;</code>; and support for native <code>&quot;setenv&quot;</code> has been added. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Experimental support has been added to allow ops in the optree to locate their parent, if any. This is enabled by the non-default build option <code>&quot;-DPERL_OP_PARENT&quot;</code>. It is envisaged that this will eventually become enabled by default, so <font SIZE="-1">XS</font> code which directly accesses the <code>&quot;op_sibling&quot;</code> field of ops should be updated to be future-proofed. </p>
<p> On <code>&quot;PERL_OP_PARENT&quot;</code> builds, the <code>&quot;op_sibling&quot;</code> field has been renamed <code>&quot;op_sibparent&quot;</code> and a new flag, <code>&quot;op_moresib&quot;</code>, added. On the last op in a sibling chain, <code>&quot;op_moresib&quot;</code> is false and <code>&quot;op_sibparent&quot;</code> points to the parent (if any) rather than being <code>&quot;NULL&quot;</code>. </p>
<p> To make existing code work transparently whether using <code>&quot;PERL_OP_PARENT&quot;</code> or not, a number of new macros and functions have been added that should be used, rather than directly manipulating <code>&quot;op_sibling&quot;</code>. </p>
<p> For the case of just reading <code>&quot;op_sibling&quot;</code> to determine the next sibling, two new macros have been added. A simple scan through a sibling chain like this: </p>
<pre><code>    for (; kid-&gt;op_sibling; kid = kid-&gt;op_sibling) { ... }
</code></pre>
<p> should now be written as: </p>
<pre><code>    for (; OpHAS_SIBLING(kid); kid = OpSIBLING(kid)) { ... }
</code></pre>
<p> For altering optrees, a general-purpose function <code>&quot;op_sibling_splice()&quot;</code> has been added, which allows for manipulation of a chain of sibling ops. By analogy with the Perl function <code>&quot;splice()&quot;</code>, it allows you to cut out zero or more ops from a sibling chain and replace them with zero or more new ops. It transparently handles all the updating of sibling, parent, op_last pointers etc. </p>
<p> If you need to manipulate ops at a lower level, then three new macros, <code>&quot;OpMORESIB_set&quot;</code>, <code>&quot;OpLASTSIB_set&quot;</code> and <code>&quot;OpMAYBESIB_set&quot;</code> are intended to be a low-level portable way to set <code>&quot;op_sibling&quot;</code> / <code>&quot;op_sibparent&quot;</code> while also updating <code>&quot;op_moresib&quot;</code>. The first sets the sibling pointer to a new sibling, the second makes the op the last sibling, and the third conditionally does the first or second action. Note that unlike <code>&quot;op_sibling_splice()&quot;</code> these macros won&#8217;t maintain consistency in the parent at the same time (<i>e.g.</i> by updating <code>&quot;op_first&quot;</code> and <code>&quot;op_last&quot;</code> where appropriate). </p>
<p> A C-level <code>&quot;Perl_op_parent()&quot;</code> function and a Perl-level <code>&quot;B::OP::parent()&quot;</code> method have been added. The C function only exists under <code>&quot;PERL_OP_PARENT&quot;</code> builds (using it is build-time error on vanilla perls). <code>&quot;B::OP::parent()&quot;</code> exists always, but on a vanilla build it always returns <code>&quot;NULL&quot;</code>. Under <code>&quot;PERL_OP_PARENT&quot;</code>, they return the parent of the current op, if any. The variable <code>$B::OP::does_parent</code> allows you to determine whether <code>&quot;B&quot;</code> supports retrieving an op&#8217;s parent. </p>
<p> <code>&quot;PERL_OP_PARENT&quot;</code> was introduced in 5.21.2, but the interface was changed considerably in 5.21.11. If you updated your code before the 5.21.11 changes, it may require further revision. The main changes after 5.21.2 were: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;OP_SIBLING&quot;</code> and <code>&quot;OP_HAS_SIBLING&quot;</code> macros have been renamed <code>&quot;OpSIBLING&quot;</code> and <code>&quot;OpHAS_SIBLING&quot;</code> for consistency with other op-manipulating macros. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;op_lastsib&quot;</code> field has been renamed <code>&quot;op_moresib&quot;</code>, and its meaning inverted. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The macro <code>&quot;OpSIBLING_set&quot;</code> has been removed, and has been superseded by <code>&quot;OpMORESIB_set&quot;</code> <i>et al</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;op_sibling_splice()&quot;</code> function now accepts a null <code>&quot;parent&quot;</code> argument where the splicing doesn&#8217;t affect the first or last ops in the sibling chain </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Macros have been created to allow <font SIZE="-1">XS</font> code to better manipulate the <font SIZE="-1">POSIX</font> locale category <code>&quot;LC_NUMERIC&quot;</code>. See ``Locale-related functions and macros&#8217;&#8216; in perlapi. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The previous <code>&quot;atoi&quot;</code> <i>et al</i> replacement function, <code>&quot;grok_atou&quot;</code>, has now been superseded by <code>&quot;grok_atoUV&quot;</code>. See perlclib for details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new function, <code>&quot;Perl_sv_get_backrefs()&quot;</code>, has been added which allows you retrieve the weak references, if any, which point at an <font SIZE="-1">SV.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;screaminstr()&quot;</code> function has been removed. Although marked as public <font SIZE="-1">API,</font> it was undocumented and had no usage in <font SIZE="-1">CPAN</font> modules. Calling it has been fatal since 5.17.0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;newDEFSVOP()&quot;</code>, <code>&quot;block_start()&quot;</code>, <code>&quot;block_end()&quot;</code> and <code>&quot;intro_my()&quot;</code> functions have been added to the <font SIZE="-1">API.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The internal <code>&quot;convert&quot;</code> function in <i>op.c</i> has been renamed <code>&quot;op_convert_list&quot;</code> and added to the <font SIZE="-1">API.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;sv_magic()&quot;</code> function no longer forbids ``ext&#8217;&#8216; magic on read-only values. After all, perl can&#8217;t know whether the custom magic will modify the <font SIZE="-1">SV</font> or not. [perl #123103] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123103">https://rt.perl.org/Ticket/Display.html?id=123103</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Accessing ``CvPADLIST&#8217;&#8216; in perlapi on an <font SIZE="-1">XSUB</font> is now forbidden. </p>
<p> The <code>&quot;CvPADLIST&quot;</code> field has been reused for a different internal purpose for XSUBs. So in particular, you can no longer rely on it being <font SIZE="-1">NULL</font> as a test of whether a <font SIZE="-1">CV</font> is an <font SIZE="-1">XSUB.</font> Use <code>&quot;CvISXSUB()&quot;</code> instead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> SVs of type <code>&quot;SVt_NV&quot;</code> are now sometimes bodiless when the build configuration and platform allow it: specifically, when <code>&quot;sizeof(NV) &lt;= sizeof(IV)&quot;</code>. ``Bodiless&#8217;&#8216; means that the <font SIZE="-1">NV</font> value is stored directly in the head of an <font SIZE="-1">SV,</font> without requiring a separate body to be allocated. This trick has already been used for IVs since 5.9.2 (though in the case of IVs, it is always used, regardless of platform and build configuration). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>$DB::single</code>, <code>$DB::signal</code> and <code>$DB::trace</code> variables now have set- and get-magic that stores their values as IVs, and those IVs are used when testing their values in <code>&quot;pp_dbstate()&quot;</code>. This prevents perl from recursing infinitely if an overloaded object is assigned to any of those variables. [perl #122445] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122445">https://rt.perl.org/Ticket/Display.html?id=122445</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Perl_tmps_grow()&quot;</code>, which is marked as public <font SIZE="-1">API</font> but is undocumented, has been removed from the public <font SIZE="-1">API.</font> This change does not affect <font SIZE="-1">XS</font> code that uses the <code>&quot;EXTEND_MORTAL&quot;</code> macro to pre-extend the mortal stack. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl&#8217;s internals no longer sets or uses the <code>&quot;SVs_PADMY&quot;</code> flag. <code>&quot;SvPADMY()&quot;</code> now returns a true value for anything not marked <code>&quot;PADTMP&quot;</code> and <code>&quot;SVs_PADMY&quot;</code> is now defined as 0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The macros <code>&quot;SETsv&quot;</code> and <code>&quot;SETsvUN&quot;</code> have been removed. They were no longer used in the core since commit 6f1401dc2a five years ago, and have not been found present on <font SIZE="-1">CPAN.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;SvFAKE&quot;</code> bit (unused on HVs) got informally reserved by David Mitchell for future work on vtables. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;sv_catpvn_flags()&quot;</code> function accepts <code>&quot;SV_CATBYTES&quot;</code> and <code>&quot;SV_CATUTF8&quot;</code> flags, which specify whether the appended string is bytes or <font SIZE="-1">UTF-8,</font> respectively. (These flags have in fact been present since 5.16.0, but were formerly not regarded as part of the <font SIZE="-1">API.</font>) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new opcode class, <code>&quot;METHOP&quot;</code>, has been introduced. It holds information used at runtime to improve the performance of class/object method calls. </p>
<p> <code>&quot;OP_METHOD&quot;</code> and <code>&quot;OP_METHOD_NAMED&quot;</code> have changed from being <code>&quot;UNOP/SVOP&quot;</code> to being <code>&quot;METHOP&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;cv_name()&quot;</code> is a new <font SIZE="-1">API</font> function that can be passed a <font SIZE="-1">CV</font> or <font SIZE="-1">GV.</font> It returns an <font SIZE="-1">SV</font> containing the name of the subroutine, for use in diagnostics. </p>
<p> [perl #116735] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=116735">https://rt.perl.org/Ticket/Display.html?id=116735</a>&gt; [perl #120441] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=120441">https://rt.perl.org/Ticket/Display.html?id=120441</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;cv_set_call_checker_flags()&quot;</code> is a new <font SIZE="-1">API</font> function that works like <code>&quot;cv_set_call_checker()&quot;</code>, except that it allows the caller to specify whether the call checker requires a full <font SIZE="-1">GV</font> for reporting the subroutine&#8217;s name, or whether it could be passed a <font SIZE="-1">CV</font> instead. Whatever value is passed will be acceptable to <code>&quot;cv_name()&quot;</code>. <code>&quot;cv_set_call_checker()&quot;</code> guarantees there will be a <font SIZE="-1">GV,</font> but it may have to create one on the fly, which is inefficient. [perl #116735] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=116735">https://rt.perl.org/Ticket/Display.html?id=116735</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;CvGV&quot;</code> (which is not part of the <font SIZE="-1">API</font>) is now a more complex macro, which may call a function and reify a <font SIZE="-1">GV.</font> For those cases where it has been used as a boolean, <code>&quot;CvHASGV&quot;</code> has been added, which will return true for CVs that notionally have GVs, but without reifying the <font SIZE="-1">GV.</font> <code>&quot;CvGV&quot;</code> also returns a <font SIZE="-1">GV</font> now for lexical subs. [perl #120441] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=120441">https://rt.perl.org/Ticket/Display.html?id=120441</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ``sync_locale&#8217;&#8216; in perlapi function has been added to the public <font SIZE="-1">API.</font> Changing the program&#8217;s locale should be avoided by <font SIZE="-1">XS</font> code. Nevertheless, certain non-Perl libraries called from <font SIZE="-1">XS</font> need to do so, such as <code>&quot;Gtk&quot;</code>. When this happens, Perl needs to be told that the locale has changed. Use this function to do so, before returning to Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The defines and labels for the flags in the <code>&quot;op_private&quot;</code> field of OPs are now auto-generated from data in <i>regen/op_private</i>. The noticeable effect of this is that some of the flag output of <code>&quot;Concise&quot;</code> might differ slightly, and the flag output of <code>&quot;perl -Dx&quot;</code> may differ considerably (they both use the same set of labels now). Also, debugging builds now have a new assertion in <code>&quot;op_free()&quot;</code> to ensure that the op doesn&#8217;t have any unrecognized flags set in <code>&quot;op_private&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The deprecated variable <code>&quot;PL_sv_objcount&quot;</code> has been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now tries to keep the locale category <code>&quot;LC_NUMERIC&quot;</code> set to ``C&#8217;&#8216; except around operations that need it to be set to the program&#8217;s underlying locale. This protects the many <font SIZE="-1">XS</font> modules that cannot cope with the decimal radix character not being a dot. Prior to this release, Perl initialized this category to ``C&#8217;&#8216;, but a call to <code>&quot;POSIX::setlocale()&quot;</code> would change it. Now such a call will change the underlying locale of the <code>&quot;LC_NUMERIC&quot;</code> category for the program, but the locale exposed to <font SIZE="-1">XS</font> code will remain ``C&#8217;&#8216;. There are new macros to manipulate the <font SIZE="-1">LC_NUMERIC</font> locale, including <code>&quot;STORE_LC_NUMERIC_SET_TO_NEEDED&quot;</code> and <code>&quot;STORE_LC_NUMERIC_FORCE_TO_UNDERLYING&quot;</code>. See ``Locale-related functions and macros&#8217;&#8216; in perlapi. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new macro <code>&quot;isUTF8_CHAR&quot;</code> has been written which efficiently determines if the string given by its parameters begins with a well-formed <font SIZE="-1">UTF-8</font> encoded character. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The following private <font SIZE="-1">API</font> functions had their context parameter removed: <code>&quot;Perl_cast_ulong&quot;</code>, <code>&quot;Perl_cast_i32&quot;</code>, <code>&quot;Perl_cast_iv&quot;</code>, <code>&quot;Perl_cast_uv&quot;</code>, <code>&quot;Perl_cv_const_sv&quot;</code>, <code>&quot;Perl_mg_find&quot;</code>, <code>&quot;Perl_mg_findext&quot;</code>, <code>&quot;Perl_mg_magical&quot;</code>, <code>&quot;Perl_mini_mktime&quot;</code>, <code>&quot;Perl_my_dirfd&quot;</code>, <code>&quot;Perl_sv_backoff&quot;</code>, <code>&quot;Perl_utf8_hop&quot;</code>. </p>
<p> Note that the prefix-less versions of those functions that are part of the public <font SIZE="-1">API,</font> such as <code>&quot;cast_i32()&quot;</code>, remain unaffected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;PADNAME&quot;</code> and <code>&quot;PADNAMELIST&quot;</code> types are now separate types, and no longer simply aliases for <font SIZE="-1">SV</font> and <font SIZE="-1">AV.</font> [perl #123223] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123223">https://rt.perl.org/Ticket/Display.html?id=123223</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pad names are now always <font SIZE="-1">UTF-8.</font> The <code>&quot;PadnameUTF8&quot;</code> macro always returns true. Previously, this was effectively the case already, but any support for two different internal representations of pad names has now been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new op class, <code>&quot;UNOP_AUX&quot;</code>, has been added. This is a subclass of <code>&quot;UNOP&quot;</code> with an <code>&quot;op_aux&quot;</code> field added, which points to an array of unions of <font SIZE="-1">UV,</font> SV* etc. It is intended for where an op needs to store more data than a simple <code>&quot;op_sv&quot;</code> or whatever. Currently the only op of this type is <code>&quot;OP_MULTIDEREF&quot;</code> (see next item). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new op has been added, <code>&quot;OP_MULTIDEREF&quot;</code>, which performs one or more nested array and hash lookups where the key is a constant or simple variable. For example the expression <code>$a[0]{$k}[$i]</code>, which previously involved ten <code>&quot;rv2Xv&quot;</code>, <code>&quot;Xelem&quot;</code>, <code>&quot;gvsv&quot;</code> and <code>&quot;const&quot;</code> ops is now performed by a single <code>&quot;multideref&quot;</code> op. It can also handle <code>&quot;local&quot;</code>, <code>&quot;exists&quot;</code> and <code>&quot;delete&quot;</code>. A non-simple index expression, such as <code>&quot;[$i+1]&quot;</code> is still done using <code>&quot;aelem&quot;</code>/<code>&quot;helem&quot;</code>, and single-level array lookup with a small constant index is still done using <code>&quot;aelemfast&quot;</code>. </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;close&quot;</code> now sets <code>$!</code> </p>
<p> When an I/O error occurs, the fact that there has been an error is recorded in the handle. <code>&quot;close&quot;</code> returns false for such a handle. Previously, the value of <code>$!</code> would be untouched by <code>&quot;close&quot;</code>, so the common convention of writing <code>&quot;close $fh or die $!&quot;</code> did not work reliably. Now the handle records the value of <code>$!</code>, too, and <code>&quot;close&quot;</code> restores it. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;no re&quot;</code> now can turn off everything that <code>&quot;use re&quot;</code> enables </p>
<p> Previously, running <code>&quot;no re&quot;</code> would turn off only a few things. Now it can turn off all the enabled things. For example, the only way to stop debugging, once enabled, was to exit the enclosing block; that is now fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pack(&quot;D&quot;, $x)&quot;</code> and <code>&quot;pack(&quot;F&quot;, $x)&quot;</code> now zero the padding on x86 long double builds. Under some build options on <font SIZE="-1">GCC 4.8</font> and later, they used to either overwrite the zero-initialized padding, or bypass the initialized buffer entirely. This caused <i>op/pack.t</i> to fail. [perl #123971] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123971">https://rt.perl.org/Ticket/Display.html?id=123971</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Extending an array cloned from a parent thread could result in ``Modification of a read-only value attempted&#8217;&#8216; errors when attempting to modify the new elements. [perl #124127] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124127">https://rt.perl.org/Ticket/Display.html?id=124127</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An assertion failure and subsequent crash with <code>&quot;*x=&lt;y&gt;&quot;</code> has been fixed. [perl #123790] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123790">https://rt.perl.org/Ticket/Display.html?id=123790</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A possible crashing/looping bug related to compiling lexical subs has been fixed. [perl #124099] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124099">https://rt.perl.org/Ticket/Display.html?id=124099</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">UTF-8</font> now works correctly in function names, in unquoted HERE-document terminators, and in variable names used as array indexes. [perl #124113] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124113">https://rt.perl.org/Ticket/Display.html?id=124113</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Repeated global pattern matches in scalar context on large tainted strings were exponentially slow depending on the current match position in the string. [perl #123202] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123202">https://rt.perl.org/Ticket/Display.html?id=123202</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various crashes due to the parser getting confused by syntax errors have been fixed. [perl #123801] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123801">https://rt.perl.org/Ticket/Display.html?id=123801</a>&gt; [perl #123802] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123802">https://rt.perl.org/Ticket/Display.html?id=123802</a>&gt; [perl #123955] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123955">https://rt.perl.org/Ticket/Display.html?id=123955</a>&gt; [perl #123995] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123995">https://rt.perl.org/Ticket/Display.html?id=123995</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;split&quot;</code> in the scope of lexical <code>$_</code> has been fixed not to fail assertions. [perl #123763] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123763">https://rt.perl.org/Ticket/Display.html?id=123763</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;my $x : attr&quot;</code> syntax inside various list operators no longer fails assertions. [perl #123817] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123817">https://rt.perl.org/Ticket/Display.html?id=123817</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An <code>&quot;@&quot;</code> sign in quotes followed by a non-ASCII digit (which is not a valid identifier) would cause the parser to crash, instead of simply trying the <code>&quot;@&quot;</code> as literal. This has been fixed. [perl #123963] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123963">https://rt.perl.org/Ticket/Display.html?id=123963</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;*bar::=*foo::=*glob_with_hash&quot;</code> has been crashing since Perl 5.14, but no longer does. [perl #123847] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123847">https://rt.perl.org/Ticket/Display.html?id=123847</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;foreach&quot;</code> in scalar context was not pushing an item on to the stack, resulting in bugs. (<code>&quot;print 4, scalar do { foreach(@x){} } + 1&quot;</code> would print 5.) It has been fixed to return <code>&quot;undef&quot;</code>. [perl #124004] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124004">https://rt.perl.org/Ticket/Display.html?id=124004</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several cases of data used to store environment variable contents in core C code being potentially overwritten before being used have been fixed. [perl #123748] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123748">https://rt.perl.org/Ticket/Display.html?id=123748</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some patterns starting with <code>&quot;/.*..../&quot;</code> matched against long strings have been slow since v5.8, and some of the form <code>&quot;/.*..../i&quot;</code> have been slow since v5.18. They are now all fast again. [perl #123743] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123743">https://rt.perl.org/Ticket/Display.html?id=123743</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The original visible value of <code>$/</code> is now preserved when it is set to an invalid value. Previously if you set <code>$/</code> to a reference to an array, for example, perl would produce a runtime error and not set <code>&quot;PL_rs&quot;</code>, but Perl code that checked <code>$/</code> would see the array reference. [perl #123218] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123218">https://rt.perl.org/Ticket/Display.html?id=123218</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In a regular expression pattern, a <font SIZE="-1">POSIX</font> class, like <code>&quot;[:ascii:]&quot;</code>, must be inside a bracketed character class, like <code>&quot;qr/[[:ascii:]]/&quot;</code>. A warning is issued when something looking like a <font SIZE="-1">POSIX</font> class is not inside a bracketed class. That warning wasn&#8217;t getting generated when the <font SIZE="-1">POSIX</font> class was negated: <code>&quot;[:^ascii:]&quot;</code>. This is now fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl 5.14.0 introduced a bug whereby <code>&quot;eval { LABEL: }&quot;</code> would crash. This has been fixed. [perl #123652] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123652">https://rt.perl.org/Ticket/Display.html?id=123652</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various crashes due to the parser getting confused by syntax errors have been fixed. [perl #123617] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123617">https://rt.perl.org/Ticket/Display.html?id=123617</a>&gt;. [perl #123737] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123737">https://rt.perl.org/Ticket/Display.html?id=123737</a>&gt;. [perl #123753] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123753">https://rt.perl.org/Ticket/Display.html?id=123753</a>&gt;. [perl #123677] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123677">https://rt.perl.org/Ticket/Display.html?id=123677</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Code like <code>&quot;/$a[/&quot;</code> used to read the next line of input and treat it as though it came immediately after the opening bracket. Some invalid code consequently would parse and run, but some code caused crashes, so this is now disallowed. [perl #123712] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123712">https://rt.perl.org/Ticket/Display.html?id=123712</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix argument underflow for <code>&quot;pack&quot;</code>. [perl #123874] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123874">https://rt.perl.org/Ticket/Display.html?id=123874</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix handling of non-strict <code>&quot;\x{}&quot;</code>. Now <code>&quot;\x{}&quot;</code> is equivalent to <code>&quot;\x{0}&quot;</code> instead of faulting. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;stat -t&quot;</code> is now no longer treated as stackable, just like <code>&quot;-t stat&quot;</code>. [perl #123816] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123816">https://rt.perl.org/Ticket/Display.html?id=123816</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The following no longer causes a <font SIZE="-1">SEGV:</font> <code>&quot;qr{x+(y(?0))*}&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed infinite loop in parsing backrefs in regexp patterns. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several minor bug fixes in behavior of Infinity and NaN, including warnings when stringifying Infinity-like or NaN-like strings. For example, ``NaNcy&#8217;&#8216; doesn&#8217;t numify to NaN anymore. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A bug in regular expression patterns that could lead to segfaults and other crashes has been fixed. This occurred only in patterns compiled with <code>&quot;/i&quot;</code> while taking into account the current <font SIZE="-1">POSIX</font> locale (which usually means they have to be compiled within the scope of <code>&quot;use locale&quot;</code>), and there must be a string of at least 128 consecutive bytes to match. [perl #123539] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123539">https://rt.perl.org/Ticket/Display.html?id=123539</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;s///g&quot;</code> now works on very long strings (where there are more than 2 billion iterations) instead of dying with &#8216;Substitution loop&#8217;. [perl #103260] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=103260">https://rt.perl.org/Ticket/Display.html?id=103260</a>&gt;. [perl #123071] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123071">https://rt.perl.org/Ticket/Display.html?id=123071</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;gmtime&quot;</code> no longer crashes with not-a-number values. [perl #123495] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123495">https://rt.perl.org/Ticket/Display.html?id=123495</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;\()&quot;</code> (a reference to an empty list), and <code>&quot;y///&quot;</code> with lexical <code>$_</code> in scope, could both do a bad write past the end of the stack. They have both been fixed to extend the stack first. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;prototype()&quot;</code> with no arguments used to read the previous item on the stack, so <code>&quot;print &quot;foo&quot;, prototype()&quot;</code> would print foo&#8217;s prototype. It has been fixed to infer <code>$_</code> instead. [perl #123514] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123514">https://rt.perl.org/Ticket/Display.html?id=123514</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some cases of lexical state subs declared inside predeclared subs could crash, for example when evalling a string including the name of an outer variable, but no longer do. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some cases of nested lexical state subs inside anonymous subs could cause &#8216;Bizarre copy&#8217; errors or possibly even crashes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When trying to emit warnings, perl&#8217;s default debugger (<i>perl5db.pl</i>) was sometimes giving &#8216;Undefined subroutine &amp;DB::db_warn called&#8217; instead. This bug, which started to occur in Perl 5.18, has been fixed. [perl #123553] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123553">https://rt.perl.org/Ticket/Display.html?id=123553</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Certain syntax errors in substitutions, such as <code>&quot;s/${&lt;&gt;{})//&quot;</code>, would crash, and had done so since Perl 5.10. (In some cases the crash did not start happening till 5.16.) The crash has, of course, been fixed. [perl #123542] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123542">https://rt.perl.org/Ticket/Display.html?id=123542</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix a couple of string grow size calculation overflows; in particular, a repeat expression like <code>&quot;33 x ~3&quot;</code> could cause a large buffer overflow since the new output buffer size was not correctly handled by <code>&quot;SvGROW()&quot;</code>. An expression like this now properly produces a memory wrap panic. [perl #123554] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123554">https://rt.perl.org/Ticket/Display.html?id=123554</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;formline(&quot;@...&quot;, &quot;a&quot;);&quot;</code> would crash. The <code>&quot;FF_CHECKNL&quot;</code> case in <code>&quot;pp_formline()&quot;</code> didn&#8217;t set the pointer used to mark the chop position, which led to the <code>&quot;FF_MORE&quot;</code> case crashing with a segmentation fault. This has been fixed. [perl #123538] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123538">https://rt.perl.org/Ticket/Display.html?id=123538</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A possible buffer overrun and crash when parsing a literal pattern during regular expression compilation has been fixed. [perl #123604] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123604">https://rt.perl.org/Ticket/Display.html?id=123604</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;fchmod()&quot;</code> and <code>&quot;futimes()&quot;</code> now set <code>$!</code> when they fail due to being passed a closed file handle. [perl #122703] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122703">https://rt.perl.org/Ticket/Display.html?id=122703</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;op_free()&quot;</code> and <code>&quot;scalarvoid()&quot;</code> no longer crash due to a stack overflow when freeing a deeply recursive op tree. [perl #108276] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=108276">https://rt.perl.org/Ticket/Display.html?id=108276</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In Perl 5.20.0, <code>$^N</code> accidentally had the internal <font SIZE="-1">UTF-8</font> flag turned off if accessed from a code block within a regular expression, effectively UTF-8-encoding the value. This has been fixed. [perl #123135] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123135">https://rt.perl.org/Ticket/Display.html?id=123135</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A failed <code>&quot;semctl&quot;</code> call no longer overwrites existing items on the stack, which means that <code>&quot;(semctl(-1,0,0,0))[0]&quot;</code> no longer gives an ``uninitialized&#8217;&#8216; warning. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;else{foo()}&quot;</code> with no space before <code>&quot;foo&quot;</code> is now better at assigning the right line number to that statement. [perl #122695] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122695">https://rt.perl.org/Ticket/Display.html?id=122695</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Sometimes the assignment in <code>&quot;@array = split&quot;</code> gets optimised so that <code>&quot;split&quot;</code> itself writes directly to the array. This caused a bug, preventing this assignment from being used in lvalue context. So <code>&quot;(@a=split//,&quot;foo&quot;)=bar()&quot;</code> was an error. (This bug probably goes back to Perl 3, when the optimisation was added.) It has now been fixed. [perl #123057] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123057">https://rt.perl.org/Ticket/Display.html?id=123057</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When an argument list fails the checks specified by a subroutine signature (which is still an experimental feature), the resulting error messages now give the file and line number of the caller, not of the called subroutine. [perl #121374] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121374">https://rt.perl.org/Ticket/Display.html?id=121374</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The flip-flop operators (<code>&quot;..&quot;</code> and <code>&quot;...&quot;</code> in scalar context) used to maintain a separate state for each recursion level (the number of times the enclosing sub was called recursively), contrary to the documentation. Now each closure has one internal state for each flip-flop. [perl #122829] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122829">https://rt.perl.org/Ticket/Display.html?id=122829</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The flip-flop operator (<code>&quot;..&quot;</code> in scalar context) would return the same scalar each time, unless the containing subroutine was called recursively. Now it always returns a new scalar. [perl #122829] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122829">https://rt.perl.org/Ticket/Display.html?id=122829</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;use&quot;</code>, <code>&quot;no&quot;</code>, statement labels, special blocks (<code>&quot;BEGIN&quot;</code>) and pod are now permitted as the first thing in a <code>&quot;map&quot;</code> or <code>&quot;grep&quot;</code> block, the block after <code>&quot;print&quot;</code> or <code>&quot;say&quot;</code> (or other functions) returning a handle, and within <code>&quot;${...}&quot;</code>, <code>&quot;@{...}&quot;</code>, etc. [perl #122782] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122782">https://rt.perl.org/Ticket/Display.html?id=122782</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The repetition operator <code>&quot;x&quot;</code> now propagates lvalue context to its left-hand argument when used in contexts like <code>&quot;foreach&quot;</code>. That allows <code>&quot;for(($#that_array)x2) { ... }&quot;</code> to work as expected if the loop modifies <code>$_</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;(...) x ...&quot;</code> in scalar context used to corrupt the stack if one operand was an object with ``x&#8217;&#8216; overloading, causing erratic behavior. [perl #121827] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121827">https://rt.perl.org/Ticket/Display.html?id=121827</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assignment to a lexical scalar is often optimised away; for example in <code>&quot;my $x; $x = $y + $z&quot;</code>, the assign operator is optimised away and the add operator writes its result directly to <code>$x</code>. Various bugs related to this optimisation have been fixed. Certain operators on the right-hand side would sometimes fail to assign the value at all or assign the wrong value, or would call <font SIZE="-1">STORE</font> twice or not at all on tied variables. The operators affected were <code>&quot;$foo++&quot;</code>, <code>&quot;$foo--&quot;</code>, and <code>&quot;-$foo&quot;</code> under <code>&quot;use integer&quot;</code>, <code>&quot;chomp&quot;</code>, <code>&quot;chr&quot;</code> and <code>&quot;setpgrp&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> List assignments were sometimes buggy if the same scalar ended up on both sides of the assignment due to use of <code>&quot;tied&quot;</code>, <code>&quot;values&quot;</code> or <code>&quot;each&quot;</code>. The result would be the wrong value getting assigned. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;setpgrp($nonzero)&quot;</code> (with one argument) was accidentally changed in 5.16 to mean <code>setpgrp(0)</code>. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;__SUB__&quot;</code> could return the wrong value or even corrupt memory under the debugger (the <code>&quot;-d&quot;</code> switch) and in subs containing <code>&quot;eval $string&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When <code>&quot;sub () { $var }&quot;</code> becomes inlinable, it now returns a different scalar each time, just as a non-inlinable sub would, though Perl still optimises the copy away in cases where it would make no observable difference. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;my sub f () { $var }&quot;</code> and <code>&quot;sub () : attr { $var }&quot;</code> are no longer eligible for inlining. The former would crash; the latter would just throw the attributes away. An exception is made for the little-known <code>&quot;:method&quot;</code> attribute, which does nothing much. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Inlining of subs with an empty prototype is now more consistent than before. Previously, a sub with multiple statements, of which all but the last were optimised away, would be inlinable only if it were an anonymous sub containing a string <code>&quot;eval&quot;</code> or <code>&quot;state&quot;</code> declaration or closing over an outer lexical variable (or any anonymous sub under the debugger). Now any sub that gets folded to a single constant after statements have been optimised away is eligible for inlining. This applies to things like <code>&quot;sub () { jabber() if DEBUG; 42 }&quot;</code>. </p>
<p> Some subroutines with an explicit <code>&quot;return&quot;</code> were being made inlinable, contrary to the documentation, Now <code>&quot;return&quot;</code> always prevents inlining. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On some systems, such as <font SIZE="-1">VMS,</font> <code>&quot;crypt&quot;</code> can return a non-ASCII string. If a scalar assigned to had contained a <font SIZE="-1">UTF-8</font> string previously, then <code>&quot;crypt&quot;</code> would not turn off the <font SIZE="-1">UTF-8</font> flag, thus corrupting the return value. This would happen with <code>&quot;$lexical = crypt ...&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;crypt&quot;</code> no longer calls <code>&quot;FETCH&quot;</code> twice on a tied first argument. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An unterminated here-doc on the last line of a quote-like operator (<code>&quot;qq[${ &lt;&lt;END }]&quot;</code>, <code>&quot;/(?{ &lt;&lt;END })/&quot;</code>) no longer causes a double free. It started doing so in 5.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;index()&quot;</code> and <code>&quot;rindex()&quot;</code> no longer crash when used on strings over 2GB in size. [perl #121562] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121562">https://rt.perl.org/Ticket/Display.html?id=121562</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A small, previously intentional, memory leak in <code>&quot;PERL_SYS_INIT&quot;</code>/<code>&quot;PERL_SYS_INIT3&quot;</code> on Win32 builds was fixed. This might affect embedders who repeatedly create and destroy perl engines within the same process. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;POSIX::localeconv()&quot;</code> now returns the data for the program&#8217;s underlying locale even when called from outside the scope of <code>&quot;use locale&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;POSIX::localeconv()&quot;</code> now works properly on platforms which don&#8217;t have <code>&quot;LC_NUMERIC&quot;</code> and/or <code>&quot;LC_MONETARY&quot;</code>, or for which Perl has been compiled to disregard either or both of these locale categories. In such circumstances, there are now no entries for the corresponding values in the hash returned by <code>&quot;localeconv()&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;POSIX::localeconv()&quot;</code> now marks appropriately the values it returns as <font SIZE="-1">UTF-8</font> or not. Previously they were always returned as bytes, even if they were supposed to be encoded as <font SIZE="-1">UTF-8.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On Microsoft Windows, within the scope of <code>&quot;use locale&quot;</code>, the following <font SIZE="-1">POSIX</font> character classes gave results for many locales that did not conform to the <font SIZE="-1">POSIX</font> standard: <code>&quot;[[:alnum:]]&quot;</code>, <code>&quot;[[:alpha:]]&quot;</code>, <code>&quot;[[:blank:]]&quot;</code>, <code>&quot;[[:digit:]]&quot;</code>, <code>&quot;[[:graph:]]&quot;</code>, <code>&quot;[[:lower:]]&quot;</code>, <code>&quot;[[:print:]]&quot;</code>, <code>&quot;[[:punct:]]&quot;</code>, <code>&quot;[[:upper:]]&quot;</code>, <code>&quot;[[:word:]]&quot;</code>, and <code>&quot;[[:xdigit:]]&quot;</code>. This was because the underlying Microsoft implementation does not follow the standard. Perl now takes special precautions to correct for this. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Many issues have been detected by Coverity &lt;<a rel="nofollow" href="http://www.coverity.com/">http://www.coverity.com/</a>&gt; and fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;system()&quot;</code> and friends should now work properly on more Android builds. </p>
<p> Due to an oversight, the value specified through <code>&quot;-Dtargetsh&quot;</code> to <i>Configure</i> would end up being ignored by some of the build process. This caused perls cross-compiled for Android to end up with defective versions of <code>&quot;system()&quot;</code>, <code>&quot;exec()&quot;</code> and backticks: the commands would end up looking for <code>&quot;/bin/sh&quot;</code> instead of <code>&quot;/system/bin/sh&quot;</code>, and so would fail for the vast majority of devices, leaving <code>$!</code> as <code>&quot;ENOENT&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;qr(...\(...\)...)&quot;</code>, <code>&quot;qr[...\[...\]...]&quot;</code>, and <code>&quot;qr{...\{...\}...}&quot;</code> now work. Previously it was impossible to escape these three left-characters with a backslash within a regular expression pattern where otherwise they would be considered metacharacters, and the pattern opening delimiter was the character, and the closing delimiter was its mirror character. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;s///e&quot;</code> on tainted <font SIZE="-1">UTF-8</font> strings corrupted <code>&quot;pos()&quot;</code>. This bug, introduced in 5.20, is now fixed. [perl #122148] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122148">https://rt.perl.org/Ticket/Display.html?id=122148</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A non-word boundary in a regular expression (<code>&quot;\B&quot;</code>) did not always match the end of the string; in particular <code>&quot;q{} =~ /\B/&quot;</code> did not match. This bug, introduced in perl 5.14, is now fixed. [perl #122090] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122090">https://rt.perl.org/Ticket/Display.html?id=122090</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;&quot; P&quot; =~ /(?=.*P)P/&quot;</code> should match, but did not. This is now fixed. [perl #122171] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122171">https://rt.perl.org/Ticket/Display.html?id=122171</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Failing to compile <code>&quot;use Foo&quot;</code> in an <code>&quot;eval&quot;</code> could leave a spurious <code>&quot;BEGIN&quot;</code> subroutine definition, which would produce a ``Subroutine <font SIZE="-1">BEGIN</font> redefined&#8217;&#8216; warning on the next use of <code>&quot;use&quot;</code>, or other <code>&quot;BEGIN&quot;</code> block. [perl #122107] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122107">https://rt.perl.org/Ticket/Display.html?id=122107</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;method { BLOCK } ARGS&quot;</code> syntax now correctly parses the arguments if they begin with an opening brace. [perl #46947] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=46947">https://rt.perl.org/Ticket/Display.html?id=46947</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> External libraries and Perl may have different ideas of what the locale is. This is problematic when parsing version strings if the locale&#8217;s numeric separator has been changed. Version parsing has been patched to ensure it handles the locales correctly. [perl #121930] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121930">https://rt.perl.org/Ticket/Display.html?id=121930</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A bug has been fixed where zero-length assertions and code blocks inside of a regex could cause <code>&quot;pos&quot;</code> to see an incorrect value. [perl #122460] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122460">https://rt.perl.org/Ticket/Display.html?id=122460</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Dereferencing of constants now works correctly for typeglob constants. Previously the glob was stringified and its name looked up. Now the glob itself is used. [perl #69456] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=69456">https://rt.perl.org/Ticket/Display.html?id=69456</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When parsing a sigil (<code>&quot;$&quot;</code> <code>&quot;@&quot;</code> <code>&quot;%&quot;</code> <code>&quot;&amp;)&quot;</code> followed by braces, the parser no longer tries to guess whether it is a block or a hash constructor (causing a syntax error when it guesses the latter), since it can only be a block. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;undef $reference&quot;</code> now frees the referent immediately, instead of hanging on to it until the next statement. [perl #122556] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122556">https://rt.perl.org/Ticket/Display.html?id=122556</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various cases where the name of a sub is used (autoload, overloading, error messages) used to crash for lexical subs, but have been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Bareword lookup now tries to avoid vivifying packages if it turns out the bareword is not going to be a subroutine name. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compilation of anonymous constants (<i>e.g.</i>, <code>&quot;sub () { 3 }&quot;</code>) no longer deletes any subroutine named <code>&quot;__ANON__&quot;</code> in the current package. Not only was <code>&quot;*__ANON__{CODE}&quot;</code> cleared, but there was a memory leak, too. This bug goes back to Perl 5.8.0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Stub declarations like <code>&quot;sub f;&quot;</code> and <code>&quot;sub f ();&quot;</code> no longer wipe out constants of the same name declared by <code>&quot;use constant&quot;</code>. This bug was introduced in Perl 5.10.0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;qr/[\N{named sequence}]/&quot;</code> now works properly in many instances. </p>
<p> Some names known to <code>&quot;\N{...}&quot;</code> refer to a sequence of multiple characters, instead of the usual single character. Bracketed character classes generally only match single characters, but now special handling has been added so that they can match named sequences, but not if the class is inverted or the sequence is specified as the beginning or end of a range. In these cases, the only behavior change from before is a slight rewording of the fatal error message given when this class is part of a <code>&quot;?[...])&quot;</code> construct. When the <code>&quot;[...]&quot;</code> stands alone, the same non-fatal warning as before is raised, and only the first character in the sequence is used, again just as before. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tainted constants evaluated at compile time no longer cause unrelated statements to become tainted. [perl #122669] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122669">https://rt.perl.org/Ticket/Display.html?id=122669</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;open $$fh, ...&quot;</code>, which vivifies a handle with a name like <code>&quot;main::_GEN_0&quot;</code>, was not giving the handle the right reference count, so a double free could happen. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When deciding that a bareword was a method name, the parser would get confused if an <code>&quot;our&quot;</code> sub with the same name existed, and look up the method in the package of the <code>&quot;our&quot;</code> sub, instead of the package of the invocant. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The parser no longer gets confused by <code>&quot;\U=&quot;</code> within a double-quoted string. It used to produce a syntax error, but now compiles it correctly. [perl #80368] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=80368">https://rt.perl.org/Ticket/Display.html?id=80368</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> It has always been the intention for the <code>&quot;-B&quot;</code> and <code>&quot;-T&quot;</code> file test operators to treat <font SIZE="-1">UTF-8</font> encoded files as text. (perlfunc has been updated to say this.) Previously, it was possible for some files to be considered <font SIZE="-1">UTF-8</font> that actually weren&#8217;t valid <font SIZE="-1">UTF-8.</font> This is now fixed. The operators now work on <font SIZE="-1">EBCDIC</font> platforms as well. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under some conditions warning messages raised during regular expression pattern compilation were being output more than once. This has now been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl 5.20.0 introduced a regression in which a <font SIZE="-1">UTF-8</font> encoded regular expression pattern that contains a single <font SIZE="-1">ASCII</font> lowercase letter did not match its uppercase counterpart. That has been fixed in both 5.20.1 and 5.22.0. [perl #122655] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122655">https://rt.perl.org/Ticket/Display.html?id=122655</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Constant folding could incorrectly suppress warnings if lexical warnings (<code>&quot;use warnings&quot;</code> or <code>&quot;no warnings&quot;</code>) were not in effect and <code>$^W</code> were false at compile time and true at run time. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Loading Unicode tables during a regular expression match could cause assertion failures under debugging builds if the previous match used the very same regular expression. [perl #122747] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122747">https://rt.perl.org/Ticket/Display.html?id=122747</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Thread cloning used to work incorrectly for lexical subs, possibly causing crashes or double frees on exit. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Since Perl 5.14.0, deleting <code>$SomePackage::{__ANON__}</code> and then undefining an anonymous subroutine could corrupt things internally, resulting in Devel::Peek crashing or B.pm giving nonsensical data. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;(caller $n)[3]&quot;</code> now reports names of lexical subs, instead of treating them as <code>&quot;(unknown)&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sort subname LIST&quot;</code> now supports using a lexical sub as the comparison routine. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Aliasing (<i>e.g.</i>, via <code>&quot;*x = *y&quot;</code>) could confuse list assignments that mention the two names for the same variable on either side, causing wrong values to be assigned. [perl #15667] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=15667">https://rt.perl.org/Ticket/Display.html?id=15667</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Long here-doc terminators could cause a bad read on short lines of input. This has been fixed. It is doubtful that any crash could have occurred. This bug goes back to when here-docs were introduced in Perl 3.000 twenty-five years ago. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An optimization in <code>&quot;split&quot;</code> to treat <code>&quot;split /^/&quot;</code> like <code>&quot;split /^/m&quot;</code> had the unfortunate side-effect of also treating <code>&quot;split /\A/&quot;</code> like <code>&quot;split /^/m&quot;</code>, which it should not. This has been fixed. (Note, however, that <code>&quot;split /^x/&quot;</code> does not behave like <code>&quot;split /^x/m&quot;</code>, which is also considered to be a bug and will be fixed in a future version.) [perl #122761] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122761">https://rt.perl.org/Ticket/Display.html?id=122761</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The little-known <code>&quot;my Class $var&quot;</code> syntax (see fields and attributes) could get confused in the scope of <code>&quot;use utf8&quot;</code> if <code>&quot;Class&quot;</code> were a constant whose value contained Latin-1 characters. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locking and unlocking values via Hash::Util or <code>&quot;Internals::SvREADONLY&quot;</code> no longer has any effect on values that were read-only to begin with. Previously, unlocking such values could result in crashes, hangs or other erratic behavior. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some unterminated <code>&quot;(?(...)...)&quot;</code> constructs in regular expressions would either crash or give erroneous error messages. <code>&quot;/(?(1)/&quot;</code> is one such example. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pack &quot;w&quot;, $tied&quot;</code> no longer calls <font SIZE="-1">FETCH</font> twice. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> List assignments like <code>&quot;($x, $z) = (1, $y)&quot;</code> now work correctly if <code>$x</code> and <code>$y</code> have been aliased by <code>&quot;foreach&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some patterns including code blocks with syntax errors, such as <code>&quot;/ (?{(^{})/&quot;</code>, would hang or fail assertions on debugging builds. Now they produce errors. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An assertion failure when parsing <code>&quot;sort&quot;</code> with debugging enabled has been fixed. [perl #122771] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122771">https://rt.perl.org/Ticket/Display.html?id=122771</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;*a = *b; @a = split //, $b[1]&quot;</code> could do a bad read and produce junk results. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In <code>&quot;() = @array = split&quot;</code>, the <code>&quot;() =&quot;</code> at the beginning no longer confuses the optimizer into assuming a limit of 1. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fatal warnings no longer prevent the output of syntax errors. [perl #122966] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122966">https://rt.perl.org/Ticket/Display.html?id=122966</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a NaN double-to-long-double conversion error on <font SIZE="-1">VMS.</font> For quiet NaNs (and only on Itanium, not Alpha) negative infinity instead of NaN was produced. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed the issue that caused <code>&quot;make distclean&quot;</code> to incorrectly leave some files behind. [perl #122820] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122820">https://rt.perl.org/Ticket/Display.html?id=122820</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">AIX</font> now sets the length in <code>&quot;getsockopt&quot;</code> correctly. [perl #120835] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=120835">https://rt.perl.org/Ticket/Display.html?id=120835</a>&gt;. [cpan #91183] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=91183">https://rt.cpan.org/Ticket/Display.html?id=91183</a>&gt;. [cpan #85570] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=85570">https://rt.cpan.org/Ticket/Display.html?id=85570</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The optimization phase of a regexp compilation could run ``forever&#8217;&#8216; and exhaust all memory under certain circumstances; now fixed. [perl #122283] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122283">https://rt.perl.org/Ticket/Display.html?id=122283</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The test script <i>t/op/crypt.t</i> now uses the <font SIZE="-1">SHA-256</font> algorithm if the default one is disabled, rather than giving failures. [perl #121591] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121591">https://rt.perl.org/Ticket/Display.html?id=121591</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed an off-by-one error when setting the size of a shared array. [perl #122950] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122950">https://rt.perl.org/Ticket/Display.html?id=122950</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a bug that could cause perl to enter an infinite loop during compilation. In particular, a <code><a href="/docs/linux/man/1-while/">while</a>(1)</code> within a sublist, <i>e.g.</i> </p>
<pre><code>    sub foo { () = ($a, my $b, ($c, do {while(1) {} })) }
</code></pre>
<p> The bug was introduced in 5.20.0 [perl #122995] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122995">https://rt.perl.org/Ticket/Display.html?id=122995</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On Win32, if a variable was <code>&quot;local&quot;</code>-ized in a pseudo-process that later forked, restoring the original value in the child pseudo-process caused memory corruption and a crash in the child pseudo-process (and therefore the <font SIZE="-1">OS</font> process). [perl #40565] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=40565">https://rt.perl.org/Ticket/Display.html?id=40565</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calling <code>&quot;write&quot;</code> on a format with a <code>&quot;^**&quot;</code> field could produce a panic in <code>&quot;sv_chop()&quot;</code> if there were insufficient arguments or if the variable used to fill the field was empty. [perl #123245] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123245">https://rt.perl.org/Ticket/Display.html?id=123245</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Non-ASCII lexical sub names now appear without trailing junk when they appear in error messages. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;\@&quot;</code> subroutine prototype no longer flattens parenthesized arrays (taking a reference to each element), but takes a reference to the array itself. [perl #47363] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=47363">https://rt.perl.org/Ticket/Display.html?id=47363</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A block containing nothing except a C-style <code>&quot;for&quot;</code> loop could corrupt the stack, causing lists outside the block to lose elements or have elements overwritten. This could happen with <code>&quot;map { for(...){...} } ...&quot;</code> and with lists containing <code>&quot;do { for(...){...} }&quot;</code>. [perl #123286] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123286">https://rt.perl.org/Ticket/Display.html?id=123286</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;scalar()&quot;</code> now propagates lvalue context, so that <code>&quot;for(scalar($#foo)) { ... }&quot;</code> can modify <code>$#foo</code> through <code>$_</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;qr/@array(?{block})/&quot;</code> no longer dies with ``Bizarre copy of <font SIZE="-1">ARRAY&#8217;&#8216;.</font> [perl #123344] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123344">https://rt.perl.org/Ticket/Display.html?id=123344</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;eval &#8216;$variable&#8217;&quot;</code> in nested named subroutines would sometimes look up a global variable even with a lexical variable in scope. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In perl 5.20.0, <code>&quot;sort CORE::fake&quot;</code> where &#8216;fake&#8217; is anything other than a keyword, started chopping off the last 6 characters and treating the result as a sort sub name. The previous behavior of treating <code>&quot;CORE::fake&quot;</code> as a sort sub name has been restored. [perl #123410] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123410">https://rt.perl.org/Ticket/Display.html?id=123410</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Outside of <code>&quot;use utf8&quot;</code>, a single-character Latin-1 lexical variable is disallowed. The error message for it, &quot;Can&#8217;t use global <code>$foo</code>...&quot;, was giving garbage instead of the variable name. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;readline&quot;</code> on a nonexistent handle was causing <code>&quot;${^LAST_FH}&quot;</code> to produce a reference to an undefined scalar (or fail an assertion). Now <code>&quot;${^LAST_FH}&quot;</code> ends up undefined. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;(...) x ...&quot;</code> in void context now applies scalar context to the left-hand argument, instead of the context the current sub was called in. [perl #123020] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123020">https://rt.perl.org/Ticket/Display.html?id=123020</a>&gt;. </p>
 </dd></dl>
<h2>Known Problems</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pack&quot;</code>-ing a NaN on a perl compiled with Visual C 6 does not behave properly, leading to a test failure in <i>t/op/infnan.t</i>. [perl 125203] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125203">https://rt.perl.org/Ticket/Display.html?id=125203</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A goal is for Perl to be able to be recompiled to work reasonably well on any Unicode version. In Perl 5.22, though, the earliest such version is Unicode 5.1 (current is 7.0). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">EBCDIC</font> platforms </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;cmp&quot;</code> (and hence <code>&quot;sort&quot;</code>) operators do not necessarily give the correct results when both operands are UTF-EBCDIC encoded strings and there is a mixture of <font SIZE="-1">ASCII</font> and/or control characters, along with other characters. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Ranges containing <code>&quot;\N{...}&quot;</code> in the <code>&quot;tr///&quot;</code> (and <code>&quot;y///&quot;</code>) transliteration operators are treated differently than the equivalent ranges in regular expression patterns. They should, but don&#8217;t, cause the values in the ranges to all be treated as Unicode code points, and not native ones. (``Version 8 Regular Expressions&#8217;&#8216; in perlre gives details as to how it should work.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Encode and encoding are mostly broken. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Many <font SIZE="-1">CPAN</font> modules that are shipped with core show failing tests. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pack&quot;</code>/<code>&quot;unpack&quot;</code> with <code>&quot;U0&quot;</code> format may not work properly. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> The following modules are known to have test failures with this version of Perl. In many cases, patches have been submitted, so there will hopefully be new releases soon: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> B::Generate version 1.50 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Utils version 0.25 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Coro version 6.42 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Dancer version 1.3130 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Data::Alias version 1.18 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Data::Dump::Streamer version 2.38 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Data::Util version 0.63 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::Spy version 0.07 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> invoker version 0.34 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Lexical::Var version 0.009 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> LWP::ConsoleLogger version 0.000018 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Mason version 2.22 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> NgxQueue version 0.02 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Padre version 1.00 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Parse::Keyword 0.08 </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>Obituary</h2>
<p> Brian McCauley died on May 8, 2015. He was a frequent poster to Usenet, Perl Monks, and other Perl forums, and made several <font SIZE="-1">CPAN</font> contributions under the nick <font SIZE="-1">NOBULL,</font> including to the Perl <font SIZE="-1">FAQ.</font> He attended almost every YAPC::Europe, and indeed, helped organise YAPC::Europe 2006 and the <font SIZE="-1">QA</font> Hackathon 2009. His wit and his delight in intricate systems were particularly apparent in his love of board games; many Perl mongers will have fond memories of playing Fluxx and other games with Brian. He will be missed.  </p>
<h2>Acknowledgements</h2>
<p> Perl 5.22.0 represents approximately 12 months of development since Perl 5.20.0 and contains approximately 590,000 lines of changes across 2,400 files from 94 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 370,000 lines of changes to 1,500 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.22.0: </p>
<p> Aaron Crane, Abhijit Menon-Sen, Abigail, Alberto Simões, Alex Solovey, Alex Vandiver, Alexandr Ciornii, Alexandre (Midnite) Jousset, Andreas König, Andreas Voegele, Andrew Fresh, Andy Dougherty, Anthony Heading, Aristotle Pagaltzis, brian d foy, Brian Fraser, Chad Granum, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, Dagfinn Ilmari Mannsåker, Daniel Dragan, Darin McBride, Dave Rolsky, David Golden, David Mitchell, David Wheeler, Dmitri Tikhonov, Doug Bell, E. Choroba, Ed J, Eric Herman, Father Chrysostomos, George Greer, Glenn D. Golden, Graham Knop, H.Merijn Brand, Herbert Breunung, Hugo van der Sanden, James E Keenan, James McCoy, James Raspass, Jan Dubois, Jarkko Hietaniemi, Jasmine Ngan, Jerry D. Hedden, Jim Cromie, John Goodyear, kafka, Karen Etheridge, Karl Williamson, Kent Fredric, kmx, Lajos Veres, Leon Timmermans, Lukas Mai, Mathieu Arnold, Matthew Horsfall, Max Maischein, Michael Bunk, Nicholas Clark, Niels Thykier, Niko Tyni, Norman Koch, Olivier Mengué, Peter John Acklam, Peter Martini, Petr Písař, Philippe Bruhat (BooK), Pierre Bogossian, Rafael Garcia-Suarez, Randy Stauner, Reini Urban, Ricardo Signes, Rob Hoelz, Rostislav Skudnov, Sawyer X, Shirakata Kentaro, Shlomi Fish, Sisyphus, Slaven Rezic, Smylers, Steffen Müller, Steve Hay, Sullivan Beck, syber, Tadeusz Sośnierz, Thomas Sibley, Todd Rinaldo, Tony Cook, Vincent Pit, Vladimir Marek, Yaroslav Kuzmin, Yves Orton, Ævar Arnfjörð Bjarmason. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at &lt;<a rel="nofollow" href="https://rt.perl.org/">https://rt.perl.org/</a>&gt;. There may also be information at &lt;<a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a>&gt;, the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
