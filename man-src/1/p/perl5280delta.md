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
<dt>&bull;</p>
<dd> Since this renaming needs to only happen once, if you create a thread or child process, that renaming will only happen in the original thread or process.</p>
<dt>&bull;</p>
<dd> If you change directories while processing a file, and your operating system doesn&#8217;t provide the <tt>&quot;unlinkat()&quot;</tt>, <tt>&quot;renameat()&quot;</tt> and <tt>&quot;fchmodat()&quot;</tt> functions, the final rename step may fail.</dl>
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
<dt>B::Debug</p>
<dd>
<dt>Locale::Codes and its associated Country, Currency and Language modules</p>
<dd></dl>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</p>
<dd> The start up overhead for creating regular expression patterns with Unicode properties (<tt>&quot;\p{...}&quot;</tt>) has been greatly reduced in most cases.</p>
<dt>&bull;</p>
<dd> Many string concatenation expressions are now considerably faster, due to the introduction internally of a <tt>&quot;multiconcat&quot;</tt> opcode which combines multiple concatenations, and optionally a <tt>&quot;=&quot;</tt> or <tt>&quot;.=&quot;</tt>, into a single action. For example, apart from retrieving <tt>$s</tt>, <tt>$a</tt> and <tt>$b</tt>, this whole expression is now handled as a single op: </p>
<pre>
    $s .= &quot;a=$a b=$b
&quot;
</pre>
<p> As a special case, if the <font SIZE="-1">LHS</font> of an assignment is a lexical variable or <tt>&quot;my $s&quot;</tt>, the op itself handles retrieving the lexical variable, which is faster. </p>
<p> In general, the more the expression includes a mix of constant strings and variable expressions, the longer the expression, and the more it mixes together non-utf8 and utf8 strings, the more marked the performance improvement. For example on a <tt>&quot;x86_64&quot;</tt> system, this code has been benchmarked running four times faster: </p>
<p>my $s;<br />
my $a = &#8220;ab
