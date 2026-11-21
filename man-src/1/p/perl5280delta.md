---
title: "perl5280delta(1)"
name: "perl5280delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5280delta/"
description: "perl5280delta – what is new for perl v5.28.0"
---

<h2 class="name">NAME</h2>
<p> perl5280delta &#8211; what is new for perl v5.28.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.26.0 release and the 5.28.0 release. </p>
<p> If you are upgrading from an earlier release such as 5.24.0, first read perl5260delta, which describes differences between 5.24.0 and 5.26.0.</p>
<h2>Core Enhancements</h2>
<h3>Unicode 10.0 is supported</h3>
<p> A list of changes is at &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode10.0.0">http://www.unicode.org/versions/Unicode10.0.0</a>&gt;.</p>
<h3>delete on key/value hash slices</h3>
<p> <tt>&quot;delete&quot;</tt> can now be used on key/value hash slices, returning the keys along with the deleted values. [perl #131328] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131328">https://rt.perl.org/Ticket/Display.html?id=131328</a>&gt;</p>
<h3>Experimentally, there are now alphabetic synonyms for some regular expression assertions</h3>
<p> If you find it difficult to remember how to write certain of the pattern assertions, there are now alphabetic synonyms. </p>
<pre><code>
 CURRENT                NEW SYNONYMS
 ------                 ------------
 (?=...)        (*pla:...) or (*positive_lookahead:...)
 (?!...)        (*nla:...) or (*negative_lookahead:...)
 (?&lt;=...)       (*plb:...) or (*positive_lookbehind:...)
 (?&lt;!...)       (*nlb:...) or (*negative_lookbehind:...)
 (?&gt;...)        (*atomic:...)
</code></pre>
<p> These are considered experimental, so using any of these will raise (unless turned off) a warning in the <tt>&quot;experimental::alpha_assertions&quot;</tt> category.</p>
<h3>Mixed Unicode scripts are now detectable</h3>
<p> A mixture of scripts, such as Cyrillic and Latin, in a string is often the sign of a spoofing attack. A new regular expression construct now allows for easy detection of these. For example, you can say </p>
<pre>
 qr/(*script_run: \d+  )/x
</pre>
<p> And the digits matched will all be from the same set of 10. You won&#8217;t get a look-alike digit from a different script that has a different value than what it appears to be. </p>
<p> Or: </p>
<pre>
 qr/(*sr:  \w+  )/x
</pre>
<p> makes sure that all the characters come from the same script. </p>
<p> You can also combine script runs with <tt>&quot;(?&gt;...)&quot;</tt> (or <tt>&quot;*atomic:...)&quot;</tt>). </p>
<p> Instead of writing: </p>
<pre>
    (*sr:(?&lt;...))
</pre>
<p> you can now run: </p>
<pre>
    (*asr:...)
    # or
    (*atomic_script_run:...)
</pre>
<p> This is considered experimental, so using it will raise (unless turned off) a warning in the <tt>&quot;experimental::script_run&quot;</tt> category. </p>
<p> See &#8220;Script Runs&#8221; in perlre.</p>
<h3>In-place editing with perl -i is now safer</h3>
<p> Previously in-place editing (<tt>&quot;perl -i&quot;</tt>) would delete or rename the input file as soon as you started working on a new file. </p>
<p> Without backups this would result in loss of data if there was an error, such as a full disk, when writing to the output file. </p>
<p> This has changed so that the input file isn&#8217;t replaced until the output file has been completely written and successfully closed. </p>
<p> This works by creating a work file in the same directory, which is renamed over the input file once the output file is complete. </p>
<p> Incompatibilities:</p>
<dl>
<dt>&bull;</dt>
<dd> Since this renaming needs to only happen once, if you create a thread or child process, that renaming will only happen in the original thread or process.</dd>
<dt>&bull;</dt>
<dd> If you change directories while processing a file, and your operating system doesn&#8217;t provide the <tt>&quot;unlinkat()&quot;</tt>, <tt>&quot;renameat()&quot;</tt> and <tt>&quot;fchmodat()&quot;</tt> functions, the final rename step may fail.</dd></dl>
<p> [perl #127663] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=127663">https://rt.perl.org/Public/Bug/Display.html?id=127663</a>&gt;</p>
<h3>Initialisation of aggregate state variables</h3>
<p> A persistent lexical array or hash variable can now be initialized, by an expression such as <tt>&quot;state @a = qw(x y z)&quot;</tt>. Initialization of a list of persistent lexical variables is still not possible.</p>
<h3>Full-size inode numbers</h3>
<p> On platforms where inode numbers are of a type larger than perl&#8217;s native integer numerical types, stat will preserve the full content of large inode numbers by returning them in the form of strings of decimal digits. Exact comparison of inode numbers can thus be achieved by comparing with <tt>&quot;eq&quot;</tt> rather than <tt>&quot;==&quot;</tt>. Comparison with <tt>&quot;==&quot;</tt>, and other numerical operations (which are usually meaningless on inode numbers), work as well as they did before, which is to say they fall back to floating point, and ultimately operate on a fairly useless rounded inode number if the real inode number is too big for the floating point format.</p>
<h3>The sprintf %j format size modifier is now available with pre-C99 compilers</h3>
<p> The actual size used depends on the platform, so remains unportable.</p>
<h3>Close-on-exec flag set atomically</h3>
<p> When opening a file descriptor, perl now generally opens it with its close-on-exec flag already set, on platforms that support doing so. This improves thread safety, because it means that an <tt>&quot;exec&quot;</tt> initiated by one thread can no longer cause a file descriptor in the process of being opened by another thread to be accidentally passed to the executed program. </p>
<p> Additionally, perl now sets the close-on-exec flag more reliably, whether it does so atomically or not. Most file descriptors were getting the flag set, but some were being missed.</p>
<h3>String- and number-specific bitwise ops are no longer experimental</h3>
<p> The new string-specific (<tt>&quot;&amp;. |. ^. ~.&quot;</tt>) and number-specific (<tt>&quot;&amp; | ^ ~&quot;</tt>) bitwise operators introduced in Perl 5.22 that are available within the scope of <tt>&quot;use feature 'bitwise'&quot;</tt> are no longer experimental. Because the number-specific ops are spelled the same way as the existing operators that choose their behaviour based on their operands, these operators must still be enabled via the &#8220;bitwise&#8221; feature, in either of these two ways: </p>
<pre>
    use feature &quot;bitwise&quot;;
    use v5.28; # &quot;bitwise&quot; now included
</pre>
<p> They are also now enabled by the <code>-E</code> command-line switch. </p>
<p> The &#8220;bitwise&#8221; feature no longer emits a warning. Existing code that disables the &#8220;experimental::bitwise&#8221; warning category that the feature previously used will continue to work. </p>
<p> One caveat that module authors ought to be aware of is that the numeric operators now pass a fifth <font SIZE="-1">TRUE</font> argument to overload methods. Any methods that check the number of operands may croak if they do not expect so many. <font SIZE="-1">XS</font> authors in particular should be aware that this: </p>
<pre>
    SV *
    bitop_handler (lobj, robj, swap)
</pre>
<p> may need to be changed to this: </p>
<pre>
    SV *
    bitop_handler (lobj, robj, swap, ...)
</pre>
<h3>Locales are now thread-safe on systems that support them</h3>
<p> These systems include Windows starting with Visual Studio 2005, and in <font SIZE="-1">POSIX 2008</font> systems. </p>
<p> The implication is that you are now free to use locales and change them in a threaded environment. Your changes affect only your thread. See &#8220;Multi-threaded operation&#8221; in perllocale</p>
<h3>New read-only predefined variable ${^SAFE_LOCALES}</h3>
<p> This variable is 1 if the Perl interpreter is operating in an environment where it is safe to use and change locales (see perllocale.) This variable is true when the perl is unthreaded, or compiled in a platform that supports thread-safe locale operation (see previous item).</p>
<h2>Security</h2>
<h3>[<font SIZE="-1">CVE-2017-12837</font>] Heap buffer overflow in regular expression compiler</h3>
<p> Compiling certain regular expression patterns with the case-insensitive modifier could cause a heap buffer overflow and crash perl. This has now been fixed. [perl #131582] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131582">https://rt.perl.org/Public/Bug/Display.html?id=131582</a>&gt;</p>
<h3>[<font SIZE="-1">CVE-2017-12883</font>] Buffer over-read in regular expression parser</h3>
<p> For certain types of syntax error in a regular expression pattern, the error message could either contain the contents of a random, possibly large, chunk of memory, or could crash perl. This has now been fixed. [perl #131598] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131598">https://rt.perl.org/Public/Bug/Display.html?id=131598</a>&gt;</p>
<h3>[<font SIZE="-1">CVE-2017-12814</font>] $ENV{$key} stack buffer overflow on Windows</h3>
<p> A possible stack buffer overflow in the <tt>%ENV</tt> code on Windows has been fixed by removing the buffer completely since it was superfluous anyway. [perl #131665] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131665">https://rt.perl.org/Public/Bug/Display.html?id=131665</a>&gt;</p>
<h3>Default Hash Function Change</h3>
<p> Perl 5.28.0 retires various older hash functions which are not viewed as sufficiently secure for use in Perl. We now support four general purpose hash functions, Siphash (2-4 and 1-3 variants), and Zaphod32, and StadtX hash. In addition we support <font SIZE="-1">SBOX32</font> (a form of tabular hashing) for hashing short strings, in conjunction with any of the other hash functions provided. </p>
<p> By default Perl is configured to support <font SIZE="-1">SBOX</font> hashing of strings up to 24 characters, in conjunction with StadtX hashing on 64 bit builds, and Zaphod32 hashing for 32 bit builds. </p>
<p> You may control these settings with the following options to Configure: </p>
<pre>
    -DPERL_HASH_FUNC_SIPHASH
    -DPERL_HASH_FUNC_SIPHASH13
    -DPERL_HASH_FUNC_STADTX
    -DPERL_HASH_FUNC_ZAPHOD32
</pre>
<p> To disable <font SIZE="-1">SBOX</font> hashing you can use </p>
<pre>
    -DPERL_HASH_USE_SBOX32_ALSO=0
</pre>
<p> And to set the maximum length to use <font SIZE="-1">SBOX32</font> hashing on with: </p>
<pre>
    -DSBOX32_MAX_LEN=16
</pre>
<p> The maximum length allowed is 256. There probably isn&#8217;t much point in setting it higher than the default.</p>
<h2>Incompatible Changes</h2>
<h3>Subroutine attribute and signature order</h3>
<p> The experimental subroutine signatures feature has been changed so that subroutine attributes must now come before the signature rather than after. This is because attributes like <tt>&quot;:lvalue&quot;</tt> can affect the compilation of code within the signature, for example: </p>
<p>sub f : lvalue($a = do { $x = &#8220;abc&#8221;; return substr($x,0,1) })<br />
{<br />
    &#8230;<br />
}</p>
<p> Note that this the second time they have been flipped: </p>
<p>sub f : lvalue($a, $b){&#8230;};<br />
# 5.20;<br />
5.28 onwards<br />
    sub f($a, $b)<br />
    : lvalue{&#8230;};<br />
# 5.22 &#8211; 5.26</p>
<h3>Comma-less variable lists in formats are no longer allowed</h3>
<p> Omitting the commas between variables passed to formats is no longer allowed. This has been deprecated since Perl 5.000.</p>
<h3>The :locked and :unique attributes have been removed</h3>
<p> These have been no-ops and deprecated since Perl 5.12 and 5.10, respectively.</p>
<h3>\N{} with nothing between the braces is now illegal</h3>
<p> This has been deprecated since Perl 5.24.</p>
<h3>Opening the same symbol as both a file and directory handle is no longer allowed</h3>
<p> Using <tt>&quot;open()&quot;</tt> and <tt>&quot;opendir()&quot;</tt> to associate both a filehandle and a dirhandle to the same symbol (glob or scalar) has been deprecated since Perl 5.10.</p>
<h3>Use of bare &lt;&lt; to mean &lt;&lt; is no longer allowed</h3>
<p> Use of a bare terminator has been deprecated since Perl 5.000.</p>
<h3>Setting $/ to a reference to a non-positive integer no longer allowed</h3>
<p> This used to work like setting it to <tt>&quot;undef&quot;</tt>, but has been deprecated since Perl 5.20.</p>
<h3>Unicode code points with values exceeding IV_MAX are now fatal</h3>
<p> This was deprecated since Perl 5.24.</p>
<h3>The B::OP::terse method has been removed</h3>
<p> Use <tt>&quot;B::Concise::b_terse&quot;</tt> instead.</p>
<h3>Use of inherited <font SIZE="-1">AUTOLOAD</font> for non-methods is no longer allowed</h3>
<p> This was deprecated in Perl 5.004.</p>
<h3>Use of strings with code points over 0xFF is not allowed for bitwise string operators</h3>
<p> Code points over <tt>0xFF</tt> do not make sense for bitwise operators and such an operation will now croak, except for a few remaining cases. See perldeprecation. </p>
<p> This was deprecated in Perl 5.24.</p>
<h3>Setting ${^ENCODING} to a defined value is now illegal</h3>
<p> This has been deprecated since Perl 5.22 and a no-op since Perl 5.26.</p>
<h3>Backslash no longer escapes colon in <font SIZE="-1">PATH</font> for the -S switch</h3>
<p> Previously the <tt>&quot;-S&quot;</tt> switch incorrectly treated backslash (&#8220;\&#8221;) as an escape for colon when traversing the <tt>&quot;PATH&quot;</tt> environment variable. [perl #129183] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=129183">https://rt.perl.org/Ticket/Display.html?id=129183</a>&gt;</p>
<h3>the -DH (<font SIZE="-1">DEBUG_H</font>) misfeature has been removed</h3>
<p> On a perl built with debugging support, the <tt>&quot;H&quot;</tt> flag to the <tt>&quot;-D&quot;</tt> debugging option has been removed. This was supposed to dump hash values, but has been broken for many years.</p>
<h3>Yada-yada is now strictly a statement</h3>
<p> By the time of its initial stable release in Perl 5.12, the <tt>&quot;...&quot;</tt> (yada-yada) operator was explicitly intended to serve as a statement, not an expression. However, the original implementation was confused on this point, leading to inconsistent parsing. The operator was accidentally accepted in a few situations where it did not serve as a complete statement, such as </p>
<pre>
    ... . &quot;foo&quot;;
    ... if $a &lt; $b;
</pre>
<p> The parsing has now been made consistent, permitting yada-yada only as a statement. Affected code can use <tt>&quot;do{...}&quot;</tt> to put a yada-yada into an arbitrary expression context.</p>
<h3>Sort algorithm can no longer be specified</h3>
<p> Since Perl 5.8, the sort pragma has had subpragmata <tt>&quot;_mergesort&quot;</tt>, <tt>&quot;_quicksort&quot;</tt>, and <tt>&quot;_qsort&quot;</tt> that can be used to specify which algorithm perl should use to implement the sort builtin. This was always considered a dubious feature that might not last, hence the underscore spellings, and they were documented as not being portable beyond Perl 5.8. These subpragmata have now been deleted, and any attempt to use them is an error. The sort pragma otherwise remains, and the algorithm-neutral <tt>&quot;stable&quot;</tt> subpragma can be used to control sorting behaviour. [perl #119635] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=119635">https://rt.perl.org/Ticket/Display.html?id=119635</a>&gt;</p>
<h3>Over-radix digits in floating point literals</h3>
<p> Octal and binary floating point literals used to permit any hexadecimal digit to appear after the radix point. The digits are now restricted to those appropriate for the radix, as digits before the radix point always were.</p>
<h3>Return type of unpackstring()</h3>
<p> The return types of the C <font SIZE="-1">API</font> functions <tt>&quot;unpackstring()&quot;</tt> and <tt>&quot;unpack_str()&quot;</tt> have changed from <tt>&quot;I32&quot;</tt> to <tt>&quot;SSize_t&quot;</tt>, in order to accommodate datasets of more than two billion items.</p>
<h2>Deprecations</h2>
<h3>Use of vec on strings with code points above 0xFF is deprecated</h3>
<p> Such strings are represented internally in <font SIZE="-1">UTF-8,</font> and <tt>&quot;vec&quot;</tt> is a bit-oriented operation that will likely give unexpected results on those strings.</p>
<h3>Some uses of unescaped { in regexes are no longer fatal</h3>
<p> Perl 5.26.0 fatalized some uses of an unescaped left brace, but an exception was made at the last minute, specifically crafted to be a minimal change to allow <font SIZE="-1">GNU</font> Autoconf to work. That tool is heavily depended upon, and continues to use the deprecated usage. Its use of an unescaped left brace is one where we have no intention of repurposing <tt>&quot;{&quot;</tt> to be something other than itself. </p>
<p> That exception is now generalized to include various other such cases where the <tt>&quot;{&quot;</tt> will not be repurposed. </p>
<p> Note that these uses continue to raise a deprecation message.</p>
<h3>Use of unescaped { immediately after a ( in regular expression patterns is deprecated</h3>
<p> Using unescaped left braces is officially deprecated everywhere, but it is not enforced in contexts where their use does not interfere with expected extensions to the language. A deprecation is added in this release when the brace appears immediately after an opening parenthesis. Before this, even if the brace was part of a legal quantifier, it was not interpreted as such, but as the literal characters, unlike other quantifiers that follow a <tt>&quot;(&quot;</tt> which are considered errors. Now, their use will raise a deprecation message, unless turned off.</p>
<h3>Assignment to $[ will be fatal in Perl 5.30</h3>
<p> Assigning a non-zero value to <tt>$[</tt> has been deprecated since Perl 5.12, but was never given a deadline for removal. This has now been scheduled for Perl 5.30.</p>
<h3><code>hostname()</code> won&#8217;t accept arguments in Perl 5.32</h3>
<p> Passing arguments to <tt>&quot;Sys::Hostname::hostname()&quot;</tt> was already deprecated, but didn&#8217;t have a removal date. This has now been scheduled for Perl 5.32. [perl #124349] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124349">https://rt.perl.org/Ticket/Display.html?id=124349</a>&gt;</p>
<h3>Module removals</h3>
<p> The following modules will be removed from the core distribution in a future release, and will at that time need to be installed from <font SIZE="-1">CPAN.</font> Distributions on <font SIZE="-1">CPAN</font> which require these modules will need to list them as prerequisites. </p>
<p> The core versions of these modules will now issue <tt>&quot;deprecated&quot;</tt>-category warnings to alert you to this fact. To silence these deprecation warnings, install the modules in question from <font SIZE="-1">CPAN.</font> </p>
<p> Note that these are (with rare exceptions) fine modules that you are encouraged to continue to use. Their disinclusion from core primarily hinges on their necessity to bootstrapping a fully functional, CPAN-capable Perl installation, not usually on concerns over their design.</p>
<dl>
<dt>B::Debug</dt>
<dd>
</dd><dt>Locale::Codes and its associated Country, Currency and Language modules</dt>
<dd></dd></dl>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> The start up overhead for creating regular expression patterns with Unicode properties (<tt>&quot;\p{...}&quot;</tt>) has been greatly reduced in most cases.</dd>
<dt>&bull;</dt>
<dd> Many string concatenation expressions are now considerably faster, due to the introduction internally of a <tt>&quot;multiconcat&quot;</tt> opcode which combines multiple concatenations, and optionally a <tt>&quot;=&quot;</tt> or <tt>&quot;.=&quot;</tt>, into a single action. For example, apart from retrieving <tt>$s</tt>, <tt>$a</tt> and <tt>$b</tt>, this whole expression is now handled as a single op: </dd>
<pre>
    $s .= &quot;a=$a b=$b
&quot;
</pre>
<p> As a special case, if the <font SIZE="-1">LHS</font> of an assignment is a lexical variable or <tt>&quot;my $s&quot;</tt>, the op itself handles retrieving the lexical variable, which is faster. </p>
<p> In general, the more the expression includes a mix of constant strings and variable expressions, the longer the expression, and the more it mixes together non-utf8 and utf8 strings, the more marked the performance improvement. For example on a <tt>&quot;x86_64&quot;</tt> system, this code has been benchmarked running four times faster: </p>
<p>my $s;<br />
my $a = &#8220;ab\x{100}cde&quot;; my $b = &quot;fghij&quot;; my $c = &quot;\x{101}klmn&quot;; for my $i (1..10_000_000) { $s = &quot;\x{100}wxyz&quot;; $s .= &quot;foo=$a bar=$b baz=$c&quot;; } </code></pre>
 </p>
<p> In addition, <code>&quot;sprintf&quot;</code> expressions which have a constant format containing only <code>%s</code> and <code>&quot;%%&quot;</code> format elements, and which have a fixed number of arguments, are now also optimised into a <code>&quot;multiconcat&quot;</code> op. </p>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;ref()&quot;</code> builtin is now much faster in boolean context, since it no longer bothers to construct a temporary string like <code>&quot;Foo=ARRAY(0x134af48)&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;keys()&quot;</code> in void and scalar contexts is now more efficient. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The common idiom of comparing the result of <code>index()</code> with -1 is now specifically optimised, e.g. </p>
<pre><code>    if (index(...) != -1) { ... }
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;for()&quot;</code> loops and similar constructs are now more efficient in most cases. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Glob has been modified to remove unnecessary backtracking and recursion, thanks to Russ Cox. See &lt;<a rel="nofollow" href="https://research.swtch.com/glob">https://research.swtch.com/glob</a>&gt; for more details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The XS-level <code>&quot;SvTRUE()&quot;</code> <font SIZE="-1">API</font> function is now more efficient. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various integer-returning ops are now more efficient in scalar/boolean context. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Slightly improved performance when parsing stash names. [perl #129990] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129990">https://rt.perl.org/Public/Bug/Display.html?id=129990</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calls to <code>&quot;require&quot;</code> for an already loaded module are now slightly faster. [perl #132171] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=132171">https://rt.perl.org/Public/Bug/Display.html?id=132171</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The performance of pattern matching <code>&quot;[[:ascii:]]&quot;</code> and <code>&quot;[[:^ascii:]]&quot;</code> has been improved significantly except on <font SIZE="-1">EBCDIC</font> platforms. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various optimizations have been applied to matching regular expression patterns, so under the right circumstances, significant performance gains may be noticed. But in an application with many varied patterns, little overall improvement likely will be seen. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Other optimizations have been applied to <font SIZE="-1">UTF-8</font> handling, but these are not typically a major factor in most applications. </p>
 </dd></dl>
<h2>Modules and Pragmata</h2>
<p> Key highlights in this release across several modules:  </p>
<h3>Removal of use vars</h3>
<p> The usage of <code>&quot;use vars&quot;</code> has been discouraged since the introduction of <code>&quot;our&quot;</code> in Perl 5.6.0. Where possible the usage of this pragma has now been removed from the Perl source code. </p>
<p> This had a slight effect (for the better) on the output of <font SIZE="-1">WARNING_BITS</font> in B::Deparse.  </p>
<h3>Use of DynaLoader changed to XSLoader in many modules</h3>
<p> XSLoader is more modern, and most modules already require perl 5.6 or greater, so no functionality is lost by switching. In some cases, we have also made changes to the local implementation that may not be reflected in the version on <font SIZE="-1">CPAN</font> due to a desire to maintain more backwards compatibility.  </p>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Archive::Tar has been upgraded from version 2.24 to 2.30. </p>
<p> This update also handled <font SIZE="-1">CVE-2018-12015:</font> directory traversal vulnerability. [cpan #125523] &lt;<a rel="nofollow" href="https://rt.cpan.org/Ticket/Display.html?id=125523">https://rt.cpan.org/Ticket/Display.html?id=125523</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> arybase has been upgraded from version 0.12 to 0.15. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Attribute::Handlers has been upgraded from version 0.99 to 1.01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> attributes has been upgraded from version 0.29 to 0.33. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B has been upgraded from version 1.68 to 1.74. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Concise has been upgraded from version 0.999 to 1.003. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Debug has been upgraded from version 1.24 to 1.26. </p>
<p> <font SIZE="-1">NOTE:</font> B::Debug is deprecated and may be removed from a future version of Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Deparse has been upgraded from version 1.40 to 1.48. </p>
<p> It includes many bug fixes, and in particular, it now deparses variable attributes correctly: </p>
<pre><code>    my $x :foo; # used to deparse as
                 # 'attributes'-&gt;import('main', \$x, 'foo'), my $x;
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> base has been upgraded from version 2.25 to 2.27. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> bignum has been upgraded from version 0.47 to 0.49. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> blib has been upgraded from version 1.06 to 1.07. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> bytes has been upgraded from version 1.05 to 1.06. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Carp has been upgraded from version 1.42 to 1.50. </p>
<p> If a package on the call stack contains a constant named <code>&quot;ISA&quot;</code>, Carp no longer throws a ``Not a <font SIZE="-1">GLOB</font> reference&#8217;&#8216; error. </p>
<p> Carp, when generating stack traces, now attempts to work around longstanding bugs resulting from Perl&#8217;s non-reference-counted stack. [perl #52610] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=52610">https://rt.perl.org/Ticket/Display.html?id=52610</a>&gt; </p>
<p> Carp has been modified to avoid assuming that objects cannot be overloaded without the overload module loaded (this can happen with objects created by <font SIZE="-1">XS</font> modules). Previously, infinite recursion would result if an XS-defined overload method itself called Carp. [perl #132828] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132828">https://rt.perl.org/Ticket/Display.html?id=132828</a>&gt; </p>
<p> Carp now avoids using <code>&quot;overload::StrVal&quot;</code>, partly because older versions of overload (included with perl 5.14 and earlier) load Scalar::Util at run time, which will fail if Carp has been invoked after a syntax error. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> charnames has been upgraded from version 1.44 to 1.45. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compress::Raw::Zlib has been upgraded from version 2.074 to 2.076. </p>
<p> This addresses a security vulnerability in older versions of the &#8216;zlib&#8217; library (which is bundled with Compress-Raw-Zlib). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Config::Extensions has been upgraded from version 0.01 to 0.02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Config::Perl::V has been upgraded from version 0.28 to 0.29. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CPAN</font> has been upgraded from version 2.18 to 2.20. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Data::Dumper has been upgraded from version 2.167 to 2.170. </p>
<p> Quoting of glob names now obeys the Useqq option [perl #119831] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=119831">https://rt.perl.org/Ticket/Display.html?id=119831</a>&gt;. </p>
<p> Attempts to set an option to <code>&quot;undef&quot;</code> through a combined getter/setter method are no longer mistaken for getter calls [perl #113090] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=113090">https://rt.perl.org/Ticket/Display.html?id=113090</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::Peek has been upgraded from version 1.26 to 1.27. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::PPPort has been upgraded from version 3.35 to 3.40. </p>
<p> Devel::PPPort has moved from cpan-first to perl-first maintenance </p>
<p> Primary responsibility for the code in Devel::PPPort has moved into core perl. In a practical sense there should be no change except that hopefully it will stay more up to date with changes made to symbols in perl, rather than needing to be updated after the fact. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Digest::SHA has been upgraded from version 5.96 to 6.01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DirHandle has been upgraded from version 1.04 to 1.05. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DynaLoader has been upgraded from version 1.42 to 1.45. </p>
<p> Its documentation now shows the use of <code>&quot;__PACKAGE__&quot;</code> and direct object syntax [perl #132247] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132247">https://rt.perl.org/Ticket/Display.html?id=132247</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Encode has been upgraded from version 2.88 to 2.97. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> encoding has been upgraded from version 2.19 to 2.22. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Errno has been upgraded from version 1.28 to 1.29. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> experimental has been upgraded from version 0.016 to 0.019. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Exporter has been upgraded from version 5.72 to 5.73. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::CBuilder has been upgraded from version 0.280225 to 0.280230. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Constant has been upgraded from version 0.23 to 0.25. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Embed has been upgraded from version 1.34 to 1.35. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Install has been upgraded from version 2.04 to 2.14. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::MakeMaker has been upgraded from version 7.24 to 7.34. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Miniperl has been upgraded from version 1.06 to 1.08. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::ParseXS has been upgraded from version 3.34 to 3.39. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Typemaps has been upgraded from version 3.34 to 3.38. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::XSSymSet has been upgraded from version 1.3 to 1.4. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> feature has been upgraded from version 1.47 to 1.52. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> fields has been upgraded from version 2.23 to 2.24. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Copy has been upgraded from version 2.32 to 2.33. </p>
<p> It will now use the sub-second precision variant of <code>utime()</code> supplied by Time::HiRes where available. [perl #132401] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132401">https://rt.perl.org/Ticket/Display.html?id=132401</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Fetch has been upgraded from version 0.52 to 0.56. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Glob has been upgraded from version 1.28 to 1.31. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Path has been upgraded from version 2.12_01 to 2.15. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Spec and Cwd have been upgraded from version 3.67 to 3.74. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::stat has been upgraded from version 1.07 to 1.08. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> FileCache has been upgraded from version 1.09 to 1.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Filter::Simple has been upgraded from version 0.93 to 0.95. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Filter::Util::Call has been upgraded from version 1.55 to 1.58. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> GDBM_File has been upgraded from version 1.15 to 1.17. </p>
<p> Its documentation now explains that <code>&quot;each&quot;</code> and <code>&quot;delete&quot;</code> don&#8217;t mix in hashes tied to this module [perl #117449] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=117449">https://rt.perl.org/Ticket/Display.html?id=117449</a>&gt;. </p>
<p> It will now retry opening with an acceptable block size if asking gdbm to default the block size failed [perl #119623] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=119623">https://rt.perl.org/Ticket/Display.html?id=119623</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Getopt::Long has been upgraded from version 2.49 to 2.5. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hash::Util::FieldHash has been upgraded from version 1.19 to 1.20. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> I18N::Langinfo has been upgraded from version 0.13 to 0.17. </p>
<p> This module is now available on all platforms, emulating the system <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) on systems that lack it. Some caveats apply, as detailed in its documentation, the most severe being that, except for <font SIZE="-1">MS</font> Windows, the <code>&quot;CODESET&quot;</code> item is not implemented on those systems, always returning <code>&quot;&quot;</code>. </p>
<p> It now sets the <font SIZE="-1">UTF-8</font> flag in its returned scalar if the string contains legal non-ASCII <font SIZE="-1">UTF-8,</font> and the locale is <font SIZE="-1">UTF-8</font> [perl #127288] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127288">https://rt.perl.org/Ticket/Display.html?id=127288</a>&gt;. </p>
<p> This update also fixes a bug in which the underlying locale was ignored for the <code>&quot;RADIXCHAR&quot;</code> (always was returned as a dot) and the <code>&quot;THOUSEP&quot;</code> (always empty). Now the locale-appropriate values are returned. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> I18N::LangTags has been upgraded from version 0.42 to 0.43. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> if has been upgraded from version 0.0606 to 0.0608. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">IO</font> has been upgraded from version 1.38 to 1.39. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO::Socket::IP has been upgraded from version 0.38 to 0.39. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::Cmd has been upgraded from version 0.96 to 1.00. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">JSON::PP</font> has been upgraded from version 2.27400_02 to 2.97001. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;libnet&quot;</code> distribution has been upgraded from version 3.10 to 3.11. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> List::Util has been upgraded from version 1.46_02 to 1.49. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locale::Codes has been upgraded from version 3.42 to 3.56. </p>
<p> <font SIZE="-1"><code>NOTE</code></font>: Locale::Codes scheduled to be removed from core in Perl 5.30. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locale::Maketext has been upgraded from version 1.28 to 1.29. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigInt has been upgraded from version 1.999806 to 1.999811. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigInt::FastCalc has been upgraded from version 0.5005 to 0.5006. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigRat has been upgraded from version 0.2611 to 0.2613. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::CoreList has been upgraded from version 5.20170530 to 5.20180622. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> mro has been upgraded from version 1.20 to 1.22. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Net::Ping has been upgraded from version 2.55 to 2.62. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">NEXT</font> has been upgraded from version 0.67 to 0.67_01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ODBM_File has been upgraded from version 1.14 to 1.15. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Opcode has been upgraded from version 1.39 to 1.43. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> overload has been upgraded from version 1.28 to 1.30. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::encoding has been upgraded from version 0.25 to 0.26. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::scalar has been upgraded from version 0.26 to 0.29. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::via has been upgraded from version 0.16 to 0.17. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Functions has been upgraded from version 1.11 to 1.13. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Html has been upgraded from version 1.2202 to 1.24. </p>
<p> A title for the <font SIZE="-1">HTML</font> document will now be automatically generated by default from a ``<font SIZE="-1">NAME&#8217;&#8216;</font> section in the <font SIZE="-1">POD</font> document, as it used to be before the module was rewritten to use Pod::Simple::XHTML to do the core of its job [perl #110520] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=110520">https://rt.perl.org/Ticket/Display.html?id=110520</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Perldoc has been upgraded from version 3.28 to 3.2801. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;podlators&quot;</code> distribution has been upgraded from version 4.09 to 4.10. </p>
<p> Man page references and function names now follow the Linux man page formatting standards, instead of the Solaris standard. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">POSIX</font> has been upgraded from version 1.76 to 1.84. </p>
<p> Some more cautions were added about using locale-specific functions in threaded applications. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> re has been upgraded from version 0.34 to 0.36. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Scalar::Util has been upgraded from version 1.46_02 to 1.50. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> SelfLoader has been upgraded from version 1.23 to 1.25. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Socket has been upgraded from version 2.020_03 to 2.027. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> sort has been upgraded from version 2.02 to 2.04. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Storable has been upgraded from version 2.62 to 3.08. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Sub::Util has been upgraded from version 1.48 to 1.49. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> subs has been upgraded from version 1.02 to 1.03. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Sys::Hostname has been upgraded from version 1.20 to 1.22. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Term::ReadLine has been upgraded from version 1.16 to 1.17. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test has been upgraded from version 1.30 to 1.31. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test::Harness has been upgraded from version 3.38 to 3.42. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test::Simple has been upgraded from version 1.302073 to 1.302133. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> threads has been upgraded from version 2.15 to 2.22. </p>
<p> The documentation now better describes the problems that arise when returning values from threads, and no longer warns about creating threads in <code>&quot;BEGIN&quot;</code> blocks. [perl #96538] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=96538">https://rt.perl.org/Ticket/Display.html?id=96538</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> threads::shared has been upgraded from version 1.56 to 1.58. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::Array has been upgraded from version 1.06 to 1.07. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::StdHandle has been upgraded from version 4.4 to 4.5. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::gmtime has been upgraded from version 1.03 to 1.04. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::HiRes has been upgraded from version 1.9741 to 1.9759. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::localtime has been upgraded from version 1.02 to 1.03. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::Piece has been upgraded from version 1.31 to 1.3204. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::Collate has been upgraded from version 1.19 to 1.25. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::Normalize has been upgraded from version 1.25 to 1.26. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::UCD has been upgraded from version 0.68 to 0.70. </p>
<p> The function <code>&quot;num&quot;</code> now accepts an optional parameter to help in diagnosing error returns. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> User::grent has been upgraded from version 1.01 to 1.02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> User::pwent has been upgraded from version 1.00 to 1.01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> utf8 has been upgraded from version 1.19 to 1.21. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> vars has been upgraded from version 1.03 to 1.04. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> version has been upgraded from version 0.9917 to 0.9923. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> VMS::DCLsym has been upgraded from version 1.08 to 1.09. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> VMS::Stdio has been upgraded from version 2.41 to 2.44. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> warnings has been upgraded from version 1.37 to 1.42. </p>
<p> It now includes new functions with names ending in <code>&quot;_at_level&quot;</code>, allowing callers to specify the exact call frame. [perl #132468] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132468">https://rt.perl.org/Ticket/Display.html?id=132468</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> XS::Typemap has been upgraded from version 0.15 to 0.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> XSLoader has been upgraded from version 0.27 to 0.30. </p>
<p> Its documentation now shows the use of <code>&quot;__PACKAGE__&quot;</code>, and direct object syntax for example <code>&quot;DynaLoader&quot;</code> usage [perl #132247] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132247">https://rt.perl.org/Ticket/Display.html?id=132247</a>&gt;. </p>
<p> Platforms that use <code>&quot;mod2fname&quot;</code> to edit the names of loadable libraries now look for bootstrap (.bs) files under the correct, non-edited name. </p>
 </dd></dl>
<h3>Removed Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;VMS::stdio&quot;</code> compatibility shim has been removed. </p>
 </dd></dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> We have attempted to update the documentation to reflect the changes listed in this document. If you find any we have missed, send email to perlbug [at] perl.org &lt;mailto:perlbug [at] perl.org&gt;. </p>
<p> Additionally, the following selected changes have been made: </p>
<p> <i>perlapi</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">API</font> functions <code>&quot;perl_parse()&quot;</code>, <code>&quot;perl_run()&quot;</code>, and <code>&quot;perl_destruct()&quot;</code> are now documented comprehensively, where previously the only documentation was a reference to the perlembed tutorial. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The documentation of <code>&quot;newGIVENOP()&quot;</code> has been belatedly updated to account for the removal of lexical <code>$_</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">API</font> functions <code>&quot;newCONSTSUB()&quot;</code> and <code>&quot;newCONSTSUB_flags()&quot;</code> are documented much more comprehensively than before. </p>
 </dd></dl>
<p> <i>perldata</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The section ``Truth and Falsehood&#8217;&#8216; in perlsyn has been moved into perldata. </p>
 </dd></dl>
<p> <i>perldebguts</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The description of the conditions under which <code>&quot;DB::sub()&quot;</code> will be called has been clarified. [perl #131672] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131672">https://rt.perl.org/Ticket/Display.html?id=131672</a>&gt; </p>
 </dd></dl>
<p> <i>perldiag</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> ``Variable length lookbehind not implemented in regex m/%s/&#8216;&#8216; in perldiag </p>
<p> This now gives more ideas as to workarounds to the issue that was introduced in Perl 5.18 (but not documented explicitly in its perldelta) for the fact that some Unicode <code>&quot;/i&quot;</code> rules cause a few sequences such as </p>
<pre><code> (?&lt;!st)
</code></pre>
<p> to be considered variable length, and hence disallowed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ``Use of state <code>$_</code> is experimental&#8217;&#8216; in perldiag </p>
<p> This entry has been removed, as the experimental support of this construct was removed in perl 5.24.0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The diagnostic <code>&quot;Initialization of state variables in list context currently forbidden&quot;</code> has changed to <code>&quot;Initialization of state variables in list currently forbidden&quot;</code>, because list-context initialization of single aggregate state variables is now permitted. </p>
 </dd></dl>
<p> <i>perlembed</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The examples in perlembed have been made more portable in the way they exit, and the example that gets an exit code from the embedded Perl interpreter now gets it from the right place. The examples that pass a constructed argv to Perl now show the mandatory null <code>&quot;argv[argc]&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An example in perlembed used the string value of <code>&quot;ERRSV&quot;</code> as a format string when calling <code>croak()</code>. If that string contains format codes such as <code>%s</code> this could crash the program. </p>
<p> This has been changed to a call to <code>croak_sv()</code>. </p>
<p> An alternative could have been to supply a trivial format string: </p>
<pre><code>  croak(&quot;%s&quot;, SvPV_nolen(ERRSV));
</code></pre>
<p> or as a special case for <code>&quot;ERRSV&quot;</code> simply: </p>
<pre><code>  croak(NULL);
</code></pre>
 </dd></dl>
<p> <i>perlfunc</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> There is now a note that warnings generated by built-in functions are documented in perldiag and warnings. [perl #116080] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=116080">https://rt.perl.org/Ticket/Display.html?id=116080</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The documentation for the <code>&quot;exists&quot;</code> operator no longer says that autovivification behaviour ``may be fixed in a future release&#8217;&#8216;. We&#8217;ve determined that we&#8217;re not going to change the default behaviour. [perl #127712] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127712">https://rt.perl.org/Ticket/Display.html?id=127712</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A couple of small details in the documentation for the <code>&quot;bless&quot;</code> operator have been clarified. [perl #124428] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124428">https://rt.perl.org/Ticket/Display.html?id=124428</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The description of <code>@INC</code> hooks in the documentation for <code>&quot;require&quot;</code> has been corrected to say that filter subroutines receive a useless first argument. [perl #115754] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=115754">https://rt.perl.org/Ticket/Display.html?id=115754</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The documentation of <code>&quot;ref&quot;</code> has been rewritten for clarity. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The documentation of <code>&quot;use&quot;</code> now explains what syntactically qualifies as a version number for its module version checking feature. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The documentation of <code>&quot;warn&quot;</code> has been updated to reflect that since Perl 5.14 it has treated complex exception objects in a manner equivalent to <code>&quot;die&quot;</code>. [perl #121372] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121372">https://rt.perl.org/Ticket/Display.html?id=121372</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The documentation of <code>&quot;die&quot;</code> and <code>&quot;warn&quot;</code> has been revised for clarity. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The documentation of <code>&quot;each&quot;</code> has been improved, with a slightly more explicit description of the sharing of iterator state, and with caveats regarding the fragility of while-each loops. [perl #132644] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132644">https://rt.perl.org/Ticket/Display.html?id=132644</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Clarification to <code>&quot;require&quot;</code> was added to explain the differences between </p>
<pre><code>    require Foo::Bar;
    require &quot;Foo/Bar.pm&quot;;
</code></pre>
 </dd></dl>
<p> <i>perlgit</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The precise rules for identifying <code>&quot;smoke-me&quot;</code> branches are now stated. </p>
 </dd></dl>
<p> <i>perlguts</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The section on reference counting in perlguts has been heavily revised, to describe references in the way a programmer needs to think about them rather than in terms of the physical data structures. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Improve documentation related to <font SIZE="-1">UTF-8</font> multibytes. </p>
 </dd></dl>
<p> <i>perlintern</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The internal functions <code>&quot;newXS_len_flags()&quot;</code> and <code>&quot;newATTRSUB_x()&quot;</code> are now documented. </p>
 </dd></dl>
<p> <i>perlobj</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The documentation about <code>&quot;DESTROY&quot;</code> methods has been corrected, updated, and revised, especially in regard to how they interact with exceptions. [perl #122753] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122753">https://rt.perl.org/Ticket/Display.html?id=122753</a>&gt; </p>
 </dd></dl>
<p> <i>perlop</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The description of the <code>&quot;x&quot;</code> operator in perlop has been clarified. [perl #132460] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132460">https://rt.perl.org/Ticket/Display.html?id=132460</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlop has been updated to note that <code>&quot;qw&quot;</code>&#8216;s whitespace rules differ from that of <code>&quot;split&quot;</code>&#8216;s in that only <font SIZE="-1">ASCII</font> whitespace is used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The general explanation of operator precedence and associativity has been corrected and clarified. [perl #127391] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127391">https://rt.perl.org/Ticket/Display.html?id=127391</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The documentation for the <code>&quot;\&quot;</code> referencing operator now explains the unusual context that it supplies to its operand. [perl #131061] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131061">https://rt.perl.org/Ticket/Display.html?id=131061</a>&gt; </p>
 </dd></dl>
<p> <i>perlrequick</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Clarifications on metacharacters and character classes </p>
 </dd></dl>
<p> <i>perlretut</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Clarify metacharacters. </p>
 </dd></dl>
<p> <i>perlrun</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Clarify the differences between <code>-M</code> and <code>-m</code>. [perl #131518] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131518">https://rt.perl.org/Ticket/Display.html?id=131518</a>&gt; </p>
 </dd></dl>
<p> <i>perlsec</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The documentation about set-id scripts has been updated and revised. [perl #74142] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=74142">https://rt.perl.org/Ticket/Display.html?id=74142</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A section about using <code>&quot;sudo&quot;</code> to run Perl scripts has been added. </p>
 </dd></dl>
<p> <i>perlsyn</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The section ``Truth and Falsehood&#8217;&#8216; in perlsyn has been removed from that document, where it didn&#8217;t belong, and merged into the existing paragraph on the same topic in perldata. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The means to disambiguate between code blocks and hash constructors, already documented in perlref, are now documented in perlsyn too. [perl #130958] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=130958">https://rt.perl.org/Ticket/Display.html?id=130958</a>&gt; </p>
 </dd></dl>
<p> <i>perluniprops</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> perluniprops has been updated to note that <code>&quot;\p{Word}&quot;</code> now includes code points matching the <code>&quot;\p{Join_Control}&quot;</code> property. The change to the property was made in Perl 5.18, but not documented until now. There are currently only two code points that match this property U+200C (<font SIZE="-1">ZERO WIDTH</font> NON-JOINER) and U+200D (<font SIZE="-1">ZERO WIDTH JOINER</font>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> For each binary table or property, the documentation now includes which characters in the range <code>&quot;\x00-\xFF&quot;</code> it matches, as well as a list of the first few ranges of code points matched above that. </p>
 </dd></dl>
<p> <i>perlvar</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The entry for <code>$+</code> in perlvar has been expanded upon to describe handling of multiply-named capturing groups. </p>
 </dd></dl>
<p> <i>perlfunc, perlop, perlsyn</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> In various places, improve the documentation of the special cases in the condition expression of a while loop, such as implicit <code>&quot;defined&quot;</code> and assignment to <code>$_</code>. [perl #132644] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132644">https://rt.perl.org/Ticket/Display.html?id=132644</a>&gt; </p>
 </dd></dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.  </p>
<h3>New Diagnostics</h3>
<p> <i>New Errors</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Can&#8217;t ``goto&#8217;&#8216; into a ``given&#8217;&#8216; block </p>
<p> (F) A ``goto&#8217;&#8216; statement was executed to jump into the middle of a <code>&quot;given&quot;</code> block. You can&#8217;t get there from here. See ``goto&#8217;&#8216; in perlfunc. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can&#8217;t ``goto&#8217;&#8216; into a binary or list expression </p>
<p> Use of <code>&quot;goto&quot;</code> to jump into the parameter of a binary or list operator has been prohibited, to prevent crashes and stack corruption. [perl #130936] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=130936">https://rt.perl.org/Ticket/Display.html?id=130936</a>&gt; </p>
<p> You may only enter the <i>first</i> argument of an operator that takes a fixed number of arguments, since this is a case that will not cause stack corruption. [perl #132854] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132854">https://rt.perl.org/Ticket/Display.html?id=132854</a>&gt; </p>
 </dd></dl>
<p> <i>New Warnings</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Old package separator used in string </p>
<p> (W syntax) You used the old package separator, ``&#8216;&#8216;&#8216;, in a variable named inside a double-quoted string; e.g., <code>&quot;In $name&#8217;s house&quot;</code>. This is equivalent to <code>&quot;In $name::s house&quot;</code>. If you meant the former, put a backslash before the apostrophe (<code>&quot;In $name\&#8216;s house&quot;</code>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ``Locale &#8216;%s&#8217; contains (at least) the following characters which have unexpected meanings: <code>%s</code> The Perl program will use the expected meanings&#8217;&#8216; in perldiag </p>
 </dd></dl>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> A false-positive warning that was issued when using a numerically-quantified sub-pattern in a recursive regex has been silenced. [perl #131868] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131868">https://rt.perl.org/Public/Bug/Display.html?id=131868</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The warning about useless use of a concatenation operator in void context is now generated for expressions with multiple concatenations, such as <code>&quot;$a.$b.$c&quot;</code>, which used to mistakenly not warn. [perl #6997] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=6997">https://rt.perl.org/Ticket/Display.html?id=6997</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Warnings that a variable or subroutine ``masks earlier declaration in same ...&#8216;&#8216;, or that an <code>&quot;our&quot;</code> variable has been redeclared, have been moved to a new warnings category ``shadow&#8217;&#8216;. Previously they were in category ``misc&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The deprecation warning from <code>&quot;Sys::Hostname::hostname()&quot;</code> saying that it doesn&#8217;t accept arguments now states the Perl version in which the warning will be upgraded to an error. [perl #124349] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124349">https://rt.perl.org/Ticket/Display.html?id=124349</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The perldiag entry for the error regarding a set-id script has been expanded to make clear that the error is reporting a specific security vulnerability, and to advise how to fix it. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;Unable to flush stdout&quot;</code> error message was missing a trailing newline. [debian #875361] </p>
 </dd></dl>
<h2>Utility Changes</h2>
<h3>perlbug</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;--help&quot;</code> and <code>&quot;--version&quot;</code> options have been added. </p>
 </dd></dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> C89 requirement </p>
<p> Perl has been documented as requiring a C89 compiler to build since October 1998. A variety of simplifications have now been made to Perl&#8217;s internals to rely on the features specified by the C89 standard. We believe that this internal change hasn&#8217;t altered the set of platforms that Perl builds on, but please report a bug if Perl now has new problems building on your platform. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On <font SIZE="-1">GCC,</font> <code>&quot;-Werror=pointer-arith&quot;</code> is now enabled by default, disallowing arithmetic on void and function pointers. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Where an <font SIZE="-1">HTML</font> version of the documentation is installed, the <font SIZE="-1">HTML</font> documents now use relative links to refer to each other. Links from the index page of perlipc to the individual section documents are now correct. [perl #110056] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=110056">https://rt.perl.org/Ticket/Display.html?id=110056</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>lib/unicore/mktables</i> now correctly canonicalizes the names of the dependencies stored in the files it generates. </p>
<p> <i>regen/mk_invlists.pl</i>, unlike the other <i>regen/*.pl</i> scripts, used <code>$0</code> to name itself in the dependencies stored in the files it generates. It now uses a literal so that the path stored in the generated files doesn&#8217;t depend on how <i>regen/mk_invlists.pl</i> is invoked. </p>
<p> This lack of canonical names could cause test failures in <i>t/porting/regen.t</i>. [perl #132925] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132925">https://rt.perl.org/Ticket/Display.html?id=132925</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> New probes </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><font SIZE="-1">HAS_BUILTIN_ADD_OVERFLOW</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">HAS_BUILTIN_MUL_OVERFLOW</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">HAS_BUILTIN_SUB_OVERFLOW</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">HAS_THREAD_SAFE_NL_LANGINFO_L</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">HAS_LOCALECONV_L</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">HAS_MBRLEN</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">HAS_MBRTOWC</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">HAS_MEMRCHR</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">HAS_NANOSLEEP</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">HAS_STRNLEN</font></dt>
<dd>  </dd>
<dt><font SIZE="-1">HAS_STRTOLD_L</font></dt>
<dd>  </dd>
<dt>I_WCHAR</dt>
<dd>  </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Testing of the XS-APItest directory is now done in parallel, where applicable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now includes a default <i>.travis.yml</i> file for Travis <font SIZE="-1">CI</font> testing on github mirrors. [perl #123981] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123981">https://rt.perl.org/Ticket/Display.html?id=123981</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The watchdog timer count in <i>re/pat_psycho.t</i> can now be overridden. </p>
<p> This test can take a long time to run, so there is a timer to keep this in check (currently, 5 minutes). This commit adds checking the environment variable <code>&quot;PERL_TEST_TIME_OUT_FACTOR&quot;</code>; if set, the time out setting is multiplied by its value. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>harness</i> no longer waits for 30 seconds when running <i>t/io/openpid.t</i>. [perl #121028] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121028">https://rt.perl.org/Ticket/Display.html?id=121028</a>&gt; [perl #132867] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132867">https://rt.perl.org/Ticket/Display.html?id=132867</a>&gt; </p>
 </dd></dl>
<h2>Packaging</h2>
<p> For the past few years we have released perl using three different archive formats: bzip (<code>&quot;.bz2&quot;</code>), <font SIZE="-1">LZMA2</font> (<code>&quot;.xz&quot;</code>) and gzip (<code>&quot;.gz&quot;</code>). Since xz compresses better and decompresses faster, and gzip is more compatible and uses less memory, we have dropped the <code>&quot;.bz2&quot;</code> archive format with this release. (If this poses a problem, do let us know; see ``Reporting Bugs&#8217;&#8216;, below.)  </p>
<h2>Platform Support</h2>
<h3>Discontinued Platforms</h3>
<dl>
<dt>PowerUX / Power <font SIZE="-1">MAX OS</font></dt>
<dd> <p> Compiler hints and other support for these apparently long-defunct platforms has been removed. </p>
 </dd></dl>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>CentOS</dt>
<dd> <p> Compilation on CentOS 5 is now fixed. </p>
 </dd>
<dt>Cygwin</dt>
<dd> <p> A build with the quadmath library can now be done on Cygwin. </p>
 </dd>
<dt>Darwin</dt>
<dd> <p> Perl now correctly uses reentrant functions, like <code>&quot;asctime_r&quot;</code>, on versions of Darwin that have support for them. </p>
 </dd>
<dt>FreeBSD</dt>
<dd> <p> FreeBSD&#8217;s <i>/usr/share/mk/sys.mk</i> specifies <code>&quot;-O2&quot;</code> for architectures other than <font SIZE="-1">ARM</font> and <font SIZE="-1">MIPS.</font> By default, perl is now compiled with the same optimization levels. </p>
 </dd>
<dt><font SIZE="-1">VMS</font></dt>
<dd> <p> Several fix-ups for <i>configure.com</i>, marking function <font SIZE="-1">VMS</font> has (or doesn&#8217;t have). </p>
<p> <font SIZE="-1">CRTL</font> features can now be set by embedders before invoking Perl by using the <code>&quot;decc$feature_set&quot;</code> and <code>&quot;decc$feature_set_value&quot;</code> functions. Previously any attempt to set features after image initialization were ignored. </p>
 </dd>
<dt>Windows</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Support for compiling perl on Windows using Microsoft Visual Studio 2017 (containing Visual C<font SIZE="-2">++</font> 14.1) has been added. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Visual C<font SIZE="-2">++</font> compiler version detection has been improved to work on non-English language systems. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> We now set <code>$Config{libpth}</code> correctly for 64-bit builds using Visual C<font SIZE="-2">++</font> versions earlier than 14.1. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> A new optimisation phase has been added to the compiler, <code>&quot;optimize_optree()&quot;</code>, which does a top-down scan of a complete optree just before the peephole optimiser is run. This phase is not currently hookable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An <code>&quot;OP_MULTICONCAT&quot;</code> op has been added. At <code>&quot;optimize_optree()&quot;</code> time, a chain of <code>&quot;OP_CONCAT&quot;</code> and <code>&quot;OP_CONST&quot;</code> ops, together optionally with an <code>&quot;OP_STRINGIFY&quot;</code> and/or <code>&quot;OP_SASSIGN&quot;</code>, are combined into a single <code>&quot;OP_MULTICONCAT&quot;</code> op. The op is of type <code>&quot;UNOP_AUX&quot;</code>, and the aux array contains the argument count, plus a pointer to a constant string and a set of segment lengths. For example with </p>
<pre><code>    my $x = &quot;foo=$foo, bar=$bar\n&quot;;
</code></pre>
<p> the constant string would be <code>&quot;foo=, bar=\n&quot;</code> and the segment lengths would be (4,6,1). If the string contains characters such as <code>&quot;\x80&quot;</code>, whose representation changes under utf8, two sets of strings plus lengths are precomputed and stored. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Direct access to <code>&quot;PL_keyword_plugin&quot;</code> is not safe in the presence of multithreading. A new <code>&quot;wrap_keyword_plugin&quot;</code> function has been added to allow <font SIZE="-1">XS</font> modules to safely define custom keywords even when loaded from a thread, analogous to <code>&quot;PL_check&quot;</code> / <code>&quot;wrap_op_checker&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;PL_statbuf&quot;</code> interpreter variable has been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The deprecated function <code>&quot;to_utf8_case()&quot;</code>, accessible from <font SIZE="-1">XS</font> code, has been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new function <code>&quot;is_utf8_invariant_string_loc()&quot;</code> has been added that is like <code>&quot;is_utf8_invariant_string()&quot;</code> but takes an extra pointer parameter into which is stored the location of the first variant character, if any are found. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new function, <code>&quot;Perl_langinfo()&quot;</code> has been added. It is an (almost) drop-in replacement for the system <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a>(3)</code>, but works on platforms that lack that; as well as being more thread-safe, and hiding some gotchas with locale handling from the caller. Code that uses this, needn&#8217;t use <code><a href="/docs/linux/man/3-localeconv/">localeconv</a>(3)</code> (and be affected by the gotchas) to find the decimal point, thousands separator, or currency symbol. See ``Perl_langinfo&#8217;&#8216; in perlapi. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new <font SIZE="-1">API</font> function <code>&quot;sv_rvunweaken()&quot;</code> has been added to complement <code>&quot;sv_rvweaken()&quot;</code>. The implementation was taken from ``unweaken&#8217;&#8216; in Scalar::Util. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new flag, <code>&quot;SORTf_UNSTABLE&quot;</code>, has been added. This will allow a future commit to make mergesort unstable when the user specifies ‘no sort stable’, since it has been decided that mergesort should remain stable by default. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">XS</font> modules can now automatically get reentrant versions of system functions on threaded perls. </p>
<p> By adding </p>
<pre><code>    #define PERL_REENTRANT
</code></pre>
<p> near the beginning of an <code>&quot;XS&quot;</code> file, it will be compiled so that whatever reentrant functions perl knows about on that system will automatically and invisibly be used instead of the plain, non-reentrant versions. For example, if you write <code>&quot;getpwnam()&quot;</code> in your code, on a system that has <code>&quot;getpwnam_r()&quot;</code> all calls to the former will be translated invisibly into the latter. This does not happen except on threaded perls, as they aren&#8217;t needed otherwise. Be aware that which functions have reentrant versions varies from system to system. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;PERL_NO_OP_PARENT&quot;</code> build define is no longer supported, which means that perl is now always built with <code>&quot;PERL_OP_PARENT&quot;</code> enabled. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The format and content of the non-utf8 transliteration table attached to the <code>&quot;op_pv&quot;</code> field of <code>&quot;OP_TRANS&quot;</code>/<code>&quot;OP_TRANSR&quot;</code> ops has changed. It&#8217;s now a <code>&quot;struct OPtrans_map&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new compiler <code>&quot;#define&quot;</code>, <code>&quot;dTHX_DEBUGGING&quot;</code>. has been added. This is useful for <font SIZE="-1">XS</font> or C code that only need the thread context because their debugging statements that get compiled only under <code>&quot;-DDEBUGGING&quot;</code> need one. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new <font SIZE="-1">API</font> function ``Perl_setlocale&#8217;&#8216; in perlapi has been added. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ``sync_locale&#8217;&#8216; in perlapi has been revised to return a boolean as to whether the system was using the global locale or not. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new kind of magic scalar, called a ``nonelem&#8217;&#8216; scalar, has been introduced. It is stored in an array to denote a non-existent element, whenever such an element is accessed in a potential lvalue context. It replaces the existing ``defelem&#8217;&#8216; (deferred element) magic wherever this is possible, being significantly more efficient. This means that <code>&quot;some_sub($sparse_array[$nonelem])&quot;</code> no longer has to create a new magic defelem scalar each time, as long as the element is within the array. </p>
<p> It partially fixes the rare bug of deferred elements getting out of synch with their arrays when the array is shifted or unshifted. [perl #132729] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132729">https://rt.perl.org/Ticket/Display.html?id=132729</a>&gt; </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> List assignment (<code>&quot;aassign&quot;</code>) could in some rare cases allocate an entry on the mortals stack and leave the entry uninitialized, leading to possible crashes. [perl #131570] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131570">https://rt.perl.org/Ticket/Display.html?id=131570</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Attempting to apply an attribute to an <code>&quot;our&quot;</code> variable where a function of that name already exists could result in a <font SIZE="-1">NULL</font> pointer being supplied where an <font SIZE="-1">SV</font> was expected, crashing perl. [perl #131597] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131597">https://rt.perl.org/Ticket/Display.html?id=131597</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;split &#8216; &#8216;&quot;</code> now correctly handles the argument being split when in the scope of the <code>&quot;unicode_strings&quot;</code> feature. Previously, when a string using the single-byte internal representation contained characters that are whitespace by Unicode rules but not by <font SIZE="-1">ASCII</font> rules, it treated those characters as part of fields rather than as field separators. [perl #130907] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=130907">https://rt.perl.org/Ticket/Display.html?id=130907</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several built-in functions previously had bugs that could cause them to write to the internal stack without allocating room for the item being written. In rare situations, this could have led to a crash. These bugs have now been fixed, and if any similar bugs are introduced in future, they will be detected automatically in debugging builds. </p>
<p> These internal stack usage checks introduced are also done by the <code>&quot;entersub&quot;</code> operator when calling XSUBs. This means we can report which <font SIZE="-1">XSUB</font> failed to allocate enough stack space. [perl #131975] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131975">https://rt.perl.org/Public/Bug/Display.html?id=131975</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using a symbolic ref with postderef syntax as the key in a hash lookup was yielding an assertion failure on debugging builds. [perl #131627] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131627">https://rt.perl.org/Ticket/Display.html?id=131627</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Array and hash variables whose names begin with a caret now admit indexing inside their curlies when interpolated into strings, as in <code>&quot;${^CAPTURE[0]}&quot;</code> to index <code>&quot;@{^CAPTURE}&quot;</code>. [perl #131664] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131664">https://rt.perl.org/Ticket/Display.html?id=131664</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fetching the name of a glob that was previously <font SIZE="-1">UTF-8</font> but wasn&#8217;t any longer would return that name flagged as <font SIZE="-1">UTF-8.</font> [perl #131263] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131263">https://rt.perl.org/Ticket/Display.html?id=131263</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The perl <code>&quot;sprintf()&quot;</code> function (via the underlying C function <code>&quot;Perl_sv_vcatpvfn_flags()&quot;</code>) has been heavily reworked to fix many minor bugs, including the integer wrapping of large width and precision specifiers and potential buffer overruns. It has also been made faster in many cases. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Exiting from an <code>&quot;eval&quot;</code>, whether normally or via an exception, now always frees temporary values (possibly calling destructors) <i>before</i> setting <code>$@</code>. For example: </p>
<pre><code>    sub DESTROY { eval { die &quot;died in DESTROY&quot;; } }
    eval { bless []; };
    # $@ used to be equal to &quot;died in DESTROY&quot; here; it's now &quot;&quot;.
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a duplicate symbol failure with <code>&quot;-flto -mieee-fp&quot;</code> builds. <i>pp.c</i> defined <code>&quot;_LIB_VERSION&quot;</code> which <code>&quot;-lieee&quot;</code> already defines. [perl #131786] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131786">https://rt.perl.org/Ticket/Display.html?id=131786</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The tokenizer no longer consumes the exponent part of a floating point number if it&#8217;s incomplete. [perl #131725] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131725">https://rt.perl.org/Ticket/Display.html?id=131725</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On non-threaded builds, for <code>&quot;m/$null/&quot;</code> where <code>$null</code> is an empty string is no longer treated as if the <code>&quot;/o&quot;</code> flag was present when the previous matching match operator included the <code>&quot;/o&quot;</code> flag. The rewriting used to implement this behavior could confuse the interpreter. This matches the behaviour of threaded builds. [perl #124368] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=124368">https://rt.perl.org/Ticket/Display.html?id=124368</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Parsing a <code>&quot;sub&quot;</code> definition could cause a use after free if the <code>&quot;sub&quot;</code> keyword was followed by whitespace including newlines (and comments.) [perl #131836] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131836">https://rt.perl.org/Public/Bug/Display.html?id=131836</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The tokenizer now correctly adjusts a parse pointer when skipping whitespace in a <code>&quot;${identifier}&quot;</code> construct. [perl #131949] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131949">https://rt.perl.org/Public/Bug/Display.html?id=131949</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Accesses to <code>&quot;${^LAST_FH}&quot;</code> no longer assert after using any of a variety of I/O operations on a non-glob. [perl #128263] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128263">https://rt.perl.org/Public/Bug/Display.html?id=128263</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The XS-level <code>&quot;Copy()&quot;</code>, <code>&quot;Move()&quot;</code>, <code>&quot;Zero()&quot;</code> macros and their variants now assert if the pointers supplied are <code>&quot;NULL&quot;</code>. <font SIZE="-1">ISO C</font> considers supplying <font SIZE="-1">NULL</font> pointers to the functions these macros are built upon as undefined behaviour even when their count parameters are zero. Based on these assertions and the original bug report three macro calls were made conditional. [perl #131746] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131746">https://rt.perl.org/Public/Bug/Display.html?id=131746</a>&gt; [perl #131892] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131892">https://rt.perl.org/Public/Bug/Display.html?id=131892</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Only the <code>&quot;=&quot;</code> operator is permitted for defining defaults for parameters in subroutine signatures. Previously other assignment operators, e.g. <code>&quot;+=&quot;</code>, were also accidentally permitted. [perl #131777] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131777">https://rt.perl.org/Public/Bug/Display.html?id=131777</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Package names are now always included in <code>&quot;:prototype&quot;</code> warnings [perl #131833] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131833">https://rt.perl.org/Public/Bug/Display.html?id=131833</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;je_old_stack_hwm&quot;</code> field, previously only found in the <code>&quot;jmpenv&quot;</code> structure on debugging builds, has been added to non-debug builds as well. This fixes an issue with some <font SIZE="-1">CPAN</font> modules caused by the size of this structure varying between debugging and non-debugging builds. [perl #131942] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131942">https://rt.perl.org/Public/Bug/Display.html?id=131942</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The arguments to the <code>&quot;ninstr()&quot;</code> macro are now correctly parenthesized. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A <font SIZE="-1">NULL</font> pointer dereference in the <code>&quot;S_regmatch()&quot;</code> function has been fixed. [perl #132017] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=132017">https://rt.perl.org/Public/Bug/Display.html?id=132017</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calling exec <font SIZE="-1">PROGRAM LIST</font> with an empty <code>&quot;LIST&quot;</code> has been fixed. This should call <code>&quot;execvp()&quot;</code> with an empty <code>&quot;argv&quot;</code> array (containing only the terminating <code>&quot;NULL&quot;</code> pointer), but was instead just returning false (and not setting <code>$!</code>). [perl #131730] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131730">https://rt.perl.org/Public/Bug/Display.html?id=131730</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;gv_fetchmeth_sv&quot;</code> C function stopped working properly in Perl 5.22 when fetching a constant with a <font SIZE="-1">UTF-8</font> name if that constant subroutine was stored in the stash as a simple scalar reference, rather than a full typeglob. This has been corrected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Single-letter debugger commands followed by an argument which starts with punctuation (e.g. <code>&quot;p$^V&quot;</code> and <code>&quot;x@ARGV&quot;</code>) now work again. They had been wrongly requiring a space between the command and the argument. [perl #120174] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=120174">https://rt.perl.org/Public/Bug/Display.html?id=120174</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> splice now throws an exception (``Modification of a read-only value attempted&#8217;&#8216;) when modifying a read-only array. Until now it had been silently modifying the array. The new behaviour is consistent with the behaviour of push and unshift. [perl #131000] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=131000">https://rt.perl.org/Public/Bug/Display.html?id=131000</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;stat()&quot;</code>, <code>&quot;lstat()&quot;</code>, and file test operators now fail if given a filename containing a nul character, in the same way that <code>&quot;open()&quot;</code> already fails. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;stat()&quot;</code>, <code>&quot;lstat()&quot;</code>, and file test operators now reliably set <code>$!</code> when failing due to being applied to a closed or otherwise invalid file handle. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File test operators for Unix permission bits that don&#8217;t exist on a particular platform, such as <code>&quot;-k&quot;</code> (sticky bit) on Windows, now check that the file being tested exists before returning the blanket false result, and yield the appropriate errors if the argument doesn&#8217;t refer to a file. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a &#8216;read before buffer&#8217; overrun when parsing a range starting with <code>&quot;\N{}&quot;</code> at the beginning of the character set for the transliteration operator. [perl #132245] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132245">https://rt.perl.org/Ticket/Display.html?id=132245</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a leaked scalar when parsing an empty <code>&quot;\N{}&quot;</code> at compile-time. [perl #132245] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132245">https://rt.perl.org/Ticket/Display.html?id=132245</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calling <code>&quot;do $path&quot;</code> on a directory or block device now yields a meaningful error code in <code>$!</code>. [perl #125774] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125774">https://rt.perl.org/Ticket/Display.html?id=125774</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regexp substitution using an overloaded replacement value that provides a tainted stringification now correctly taints the resulting string. [perl #115266] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=115266">https://rt.perl.org/Ticket/Display.html?id=115266</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Lexical sub declarations in <code>&quot;do&quot;</code> blocks such as <code>&quot;do { my sub lex; 123 }&quot;</code> could corrupt the stack, erasing items already on the stack in the enclosing statement. This has been fixed. [perl #132442] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132442">https://rt.perl.org/Ticket/Display.html?id=132442</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pack&quot;</code> and <code>&quot;unpack&quot;</code> can now handle repeat counts and lengths that exceed two billion. [perl #119367] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=119367">https://rt.perl.org/Ticket/Display.html?id=119367</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Digits past the radix point in octal and binary floating point literals now have the correct weight on platforms where a floating point significand doesn&#8217;t fit into an integer type. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The canonical truth value no longer has a spurious special meaning as a callable subroutine. It used to be a magic placeholder for a missing <code>&quot;import&quot;</code> or <code>&quot;unimport&quot;</code> method, but is now treated like any other string <code>1</code>. [perl #126042] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126042">https://rt.perl.org/Ticket/Display.html?id=126042</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;system&quot;</code> now reduces its arguments to strings in the parent process, so any effects of stringifying them (such as overload methods being called or warnings being emitted) are visible in the way the program expects. [perl #121105] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121105">https://rt.perl.org/Ticket/Display.html?id=121105</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;readpipe()&quot;</code> built-in function now checks at compile time that it has only one parameter expression, and puts it in scalar context, thus ensuring that it doesn&#8217;t corrupt the stack at runtime. [perl #4574] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=4574">https://rt.perl.org/Ticket/Display.html?id=4574</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sort&quot;</code> now performs correct reference counting when aliasing <code>$a</code> and <code>$b</code>, thus avoiding premature destruction and leakage of scalars if they are re-aliased during execution of the sort comparator. [perl #92264] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=92264">https://rt.perl.org/Ticket/Display.html?id=92264</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;reverse&quot;</code> with no operand, reversing <code>$_</code> by default, is no longer in danger of corrupting the stack. [perl #132544] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132544">https://rt.perl.org/Ticket/Display.html?id=132544</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;exec&quot;</code>, <code>&quot;system&quot;</code>, et al are no longer liable to have their argument lists corrupted by reentrant calls and by magic such as tied scalars. [perl #129888] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=129888">https://rt.perl.org/Ticket/Display.html?id=129888</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl&#8217;s own <code>&quot;malloc&quot;</code> no longer gets confused by attempts to allocate more than a gigabyte on a 64-bit platform. [perl #119829] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=119829">https://rt.perl.org/Ticket/Display.html?id=119829</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Stacked file test operators in a sort comparator expression no longer cause a crash. [perl #129347] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=129347">https://rt.perl.org/Ticket/Display.html?id=129347</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An identity <code>&quot;tr///&quot;</code> transformation on a reference is no longer mistaken for that reference for the purposes of deciding whether it can be assigned to. [perl #130578] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=130578">https://rt.perl.org/Ticket/Display.html?id=130578</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Lengthy hexadecimal, octal, or binary floating point literals no longer cause undefined behaviour when parsing digits that are of such low significance that they can&#8217;t affect the floating point value. [perl #131894] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131894">https://rt.perl.org/Ticket/Display.html?id=131894</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;open $$scalarref...&quot;</code> and similar invocations no longer leak the file handle. [perl #115814] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=115814">https://rt.perl.org/Ticket/Display.html?id=115814</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some convoluted kinds of regexp no longer cause an arithmetic overflow when compiled. [perl #131893] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131893">https://rt.perl.org/Ticket/Display.html?id=131893</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The default typemap, by avoiding <code>&quot;newGVgen&quot;</code>, now no longer leaks when XSUBs return file handles (<code>&quot;PerlIO *&quot;</code> or <code>&quot;FILE *&quot;</code>). [perl #115814] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=115814">https://rt.perl.org/Ticket/Display.html?id=115814</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Creating a <code>&quot;BEGIN&quot;</code> block as an <font SIZE="-1">XS</font> subroutine with a prototype no longer crashes because of the early freeing of the subroutine. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;printf&quot;</code> format specifier <code>&quot;%.0f&quot;</code> no longer rounds incorrectly [perl #47602] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=47602">https://rt.perl.org/Ticket/Display.html?id=47602</a>&gt;, and now shows the correct sign for a negative zero. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed an issue where the error <code>&quot;Scalar value @arrayname[0] better written as $arrayname&quot;</code> would give an error <code>&quot;Cannot printf Inf with &#8216;c&#8217;&quot;</code> when arrayname starts with <code>&quot;Inf&quot;</code>. [perl #132645] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132645">https://rt.perl.org/Ticket/Display.html?id=132645</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Perl implementation of <code>&quot;getcwd()&quot;</code> in <code>&quot;Cwd&quot;</code> in the PathTools distribution now behaves the same as <font SIZE="-1">XS</font> implementation on errors: it returns an error, and sets <code>$!</code>. [perl #132648] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132648">https://rt.perl.org/Ticket/Display.html?id=132648</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Vivify array elements when putting them on the stack. Fixes [perl #8910] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=8910">https://rt.perl.org/Ticket/Display.html?id=8910</a>&gt; (reported in April 2002). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed parsing of braced subscript after parens. Fixes [perl #8045] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=8045">https://rt.perl.org/Ticket/Display.html?id=8045</a>&gt; (reported in December 2001). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;tr/non_utf8/long_non_utf8/c&quot;</code> could give the wrong results when the length of the replacement character list was greater than 0x7fff. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;tr/non_utf8/non_utf8/cd&quot;</code> failed to add the implied <code>&quot;\x{100}-\x{7fffffff}&quot;</code> to the search character list. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compilation failures within ``perl-within-perl&#8217;&#8216; constructs, such as with string interpolation and the right part of <code>&quot;s///e&quot;</code>, now cause compilation to abort earlier. </p>
<p> Previously compilation could continue in order to report other errors, but the failed sub-parse could leave partly parsed constructs on the parser shift-reduce stack, confusing the parser, leading to perl crashes. [perl #125351] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125351">https://rt.perl.org/Ticket/Display.html?id=125351</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On threaded perls where the decimal point (radix) character is not a dot, it has been possible for a race to occur between threads when one needs to use the real radix character (such as with <code>&quot;sprintf&quot;</code>). This has now been fixed by use of a mutex on systems without thread-safe locales, and the problem just doesn&#8217;t come up on those with thread-safe locales. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Errors while compiling a regex character class could sometime trigger an assertion failure. [perl #132163] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=132163">https://rt.perl.org/Ticket/Display.html?id=132163</a>&gt; </p>
 </dd></dl>
<h2>Acknowledgements</h2>
<p> Perl 5.28.0 represents approximately 13 months of development since Perl 5.26.0 and contains approximately 730,000 lines of changes across 2,200 files from 77 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 580,000 lines of changes to 1,300 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its fourth decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.28.0: </p>
<p> Aaron Crane, Abigail, Ævar Arnfjörð Bjarmason, Alberto Simões, Alexandr Savca, Andrew Fresh, Andy Dougherty, Andy Lester, Aristotle Pagaltzis, Ask Bjørn Hansen, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, Dagfinn Ilmari Mannsåker, Dan Collins, Daniel Dragan, David Cantrell, David Mitchell, Dmitry Ulanov, Dominic Hargreaves, E. Choroba, Eric Herman, Eugen Konkov, Father Chrysostomos, Gene Sullivan, George Hartzell, Graham Knop, Harald Jörg, H.Merijn Brand, Hugo van der Sanden, Jacques Germishuys, James E Keenan, Jarkko Hietaniemi, Jerry D. Hedden, J. Nick Koston, John Lightsey, John Peacock, John P. Linderman, John <font SIZE="-1">SJ</font> Anderson, Karen Etheridge, Karl Williamson, Ken Brown, Ken Cotterill, Leon Timmermans, Lukas Mai, Marco Fontani, Marc-Philip Werner, Matthew Horsfall, Neil Bowers, Nicholas Clark, Nicolas R., Niko Tyni, Pali, Paul Marquess, Peter John Acklam, Reini Urban, Renee Baecker, Ricardo Signes, Robin Barker, Sawyer X, Scott Lanning, Sergey Aleynikov, Shirakata Kentaro, Shoichi Kaji, Slaven Rezic, Smylers, Steffen Müller, Steve Hay, Sullivan Beck, Thomas Sibley, Todd Rinaldo, Tomasz Konojacki, Tom Hukins, Tom Wyant, Tony Cook, Vitali Peil, Yves Orton, Zefram. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the perl bug database at &lt;<a rel="nofollow" href="https://rt.perl.org/">https://rt.perl.org/</a>&gt; . There may also be information at &lt;<a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a>&gt; , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications which make it inappropriate to send to a publicly archived mailing list, then see ``<font SIZE="-1">SECURITY VULNERABILITY CONTACT INFORMATION&#8217;&#8216;</font> in perlsec for details of how to report the issue.  </p>
<h2>Give Thanks</h2>
<p> If you wish to thank the Perl 5 Porters for the work we had done in Perl 5, you can do so by running the <code>&quot;perlthanks&quot;</code> program: </p>
<pre><code>    perlthanks
</code></pre>
<p> This will send an email to the Perl 5 Porters list with your show of thanks.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
