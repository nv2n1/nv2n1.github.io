---

title: "perl5200delta(1)"
name: "perl5200delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5200delta/"
description: "perl5200delta – what is new for perl v5.20.0"
---

<p> perl5200delta &#8211; what is new for perl v5.20.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.18.0 release and the 5.20.0 release. </p>
<p> If you are upgrading from an earlier release such as 5.16.0, first read perl5180delta, which describes differences between 5.16.0 and 5.18.0.</p>
<h2>Core Enhancements</h2>
<h3>Experimental Subroutine signatures</h3>
<p> Declarative syntax to unwrap argument list into lexical variables. <tt>&quot;sub foo ($a,$b) {...}&quot;</tt> checks the number of arguments and puts the arguments into lexical variables. Signatures are not equivalent to the existing idiom of <tt>&quot;sub foo { my($a,$b) = @_; ... }&quot;</tt>. Signatures are only available by enabling a non-default feature, and generate warnings about being experimental. The syntactic clash with prototypes is managed by disabling the short prototype syntax when signatures are enabled. </p>
<p> See &#8220;Signatures&#8221; in perlsub for details.</p>
<h3>subs now take a prototype attribute</h3>
<p> When declaring or defining a <tt>&quot;sub&quot;</tt>, the prototype can now be specified inside of a <tt>&quot;prototype&quot;</tt> attribute instead of in parens following the name. </p>
<p> For example, <tt>&quot;sub foo($$){}&quot;</tt> could be rewritten as <tt>&quot;sub foo : prototype($$){}&quot;</tt>.</p>
<h3>More consistent prototype parsing</h3>
<p> Multiple semicolons in subroutine prototypes have long been tolerated and treated as a single semicolon. There was one case where this did not happen. A subroutine whose prototype begins with &#8220;*&#8221; or &#8220;;*&#8221; can affect whether a bareword is considered a method name or sub call. This now applies also to &#8220;;;;*&#8221;. </p>
<p> Whitespace has long been allowed inside subroutine prototypes, so <tt>&quot;sub( $ $ )&quot;</tt> is equivalent to <tt>&quot;sub($$)&quot;</tt>, but until now it was stripped when the subroutine was parsed. Hence, whitespace was <i>not</i> allowed in prototypes set by <tt>&quot;Scalar::Util::set_prototype&quot;</tt>. Now it is permitted, and the parser no longer strips whitespace. This means <tt>&quot;prototype &amp;mysub&quot;</tt> returns the original prototype, whitespace and all.</p>
<h3>rand now uses a consistent random number generator</h3>
<p> Previously perl would use a platform specific random number generator, varying between the libc <code>rand()</code>, <code>random()</code> or <code>drand48()</code>. </p>
<p> This meant that the quality of perl&#8217;s random numbers would vary from platform to platform, from the 15 bits of <code>rand()</code> on Windows to 48-bits on <font SIZE="-1">POSIX</font> platforms such as Linux with <code>drand48()</code>. </p>
<p> Perl now uses its own internal <code>drand48()</code> implementation on all platforms. This does not make perl&#8217;s <tt>&quot;rand&quot;</tt> cryptographically secure. [perl #115928]</p>
<h3>New slice syntax</h3>
<p> The new <tt>%hash{...}</tt> and <tt>%array[...]</tt> syntax returns a list of key/value (or index/value) pairs. See &#8220;Key/Value Hash Slices&#8221; in perldata.</p>
<h3>Experimental Postfix Dereferencing</h3>
<p> When the <tt>&quot;postderef&quot;</tt> feature is in effect, the following syntactical equivalencies are set up: </p>
<pre><code>
$sref-&gt;$ *;
#same as ${$sref } #interpolates $aref-&gt;@ *;
#same as @{$aref } #interpolates $href-&gt;% *;
#same as % {$href } $cref-&gt;&amp;*;
#same as &amp;{$cref } $gref-&gt;**;
#same as *{$gref } $aref-&gt;$ #*;
#same as $ #{$aref } $gref-&gt;*{$slot };
#same as *{$gref } {$slot } $aref-&gt;@[...];
#same as @$aref[...] #interpolates $href-&gt;@{... };
#same as @$href{... } #interpolates $aref-&gt;% [...];
#same as % $aref[...] $href-&gt;% {... };
#same as % $href
{
    ...
}
</code></pre>
<p> Those marked as interpolating only interpolate if the associated <tt>&quot;postderef_qq&quot;</tt> feature is also enabled. This feature is <code>experimental</code> and will trigger <tt>&quot;experimental::postderef&quot;</tt>-category warnings when used, unless they are suppressed. </p>
<p> For more information, consult the Postfix Dereference Syntax section of perlref.</p>
<h3>Unicode 6.3 now supported</h3>
<p> Perl now supports and is shipped with Unicode 6.3 (though Perl may be recompiled with any previous Unicode release as well). A detailed list of Unicode 6.3 changes is at &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode6.3.0/">http://www.unicode.org/versions/Unicode6.3.0/</a>&gt;.</p>
<h3>New \p{Unicode} regular expression pattern property</h3>
<p> This is a synonym for <tt>&quot;\p{Any}&quot;</tt> and matches the set of Unicode-defined code points 0 &#8211; 0x10FFFF.</p>
<h3>Better 64-bit support</h3>
<p> On 64-bit platforms, the internal array functions now use 64-bit offsets, allowing Perl arrays to hold more than 2**31 elements, if you have the memory available. </p>
<p> The regular expression engine now supports strings longer than 2**31 characters. [perl #112790, #116907] </p>
<p> The functions PerlIO_get_bufsiz, PerlIO_get_cnt, PerlIO_set_cnt and PerlIO_set_ptrcnt now have SSize_t, rather than int, return values and parameters.</p>
<h3>use locale now works on <font SIZE="-1">UTF-8</font> locales</h3>
<p> Until this release, only single-byte locales, such as the <font SIZE="-1">ISO 8859</font> series were supported. Now, the increasingly common multi-byte <font SIZE="-1">UTF-8</font> locales are also supported. A <font SIZE="-1">UTF-8</font> locale is one in which the character set is Unicode and the encoding is <font SIZE="-1">UTF-8.</font> The <font SIZE="-1">POSIX</font> <tt>&quot;LC_CTYPE&quot;</tt> category operations (case changing (like <tt>&quot;lc()&quot;</tt>, <tt>&quot;</tt>\U&quot;</code>), and character classification (<code>&quot;\w&quot;</code>, <code>&quot;\D&quot;</code>, <code>&quot;qr/[[:punct:]]/&quot;</code>)) under such a locale work just as if not under locale, but instead as if under <code>&quot;use feature &#8216;unicode_strings&#8217;&quot;</code>, except taint rules are followed. Sorting remains by code point order in this release. [perl #56820].  </p>
<h3>use locale now compiles on systems without locale ability</h3>
<p> Previously doing this caused the program to not compile. Within its scope the program behaves as if in the ``C&#8217;&#8216; locale. Thus programs written for platforms that support locales can run on locale-less platforms without change. Attempts to change the locale away from the ``C&#8217;&#8216; locale will, of course, fail.  </p>
<h3>More locale initialization fallback options</h3>
<p> If there was an error with locales during Perl start-up, it immediately gave up and tried to use the <code>&quot;C&quot;</code> locale. Now it first tries using other locales given by the environment variables, as detailed in ``<font SIZE="-1">ENVIRONMENT&#8217;&#8216;</font> in perllocale. For example, if <code>&quot;LC_ALL&quot;</code> and <code>&quot;LANG&quot;</code> are both set, and using the <code>&quot;LC_ALL&quot;</code> locale fails, Perl will now try the <code>&quot;LANG&quot;</code> locale, and only if that fails, will it fall back to <code>&quot;C&quot;</code>. On Windows machines, Perl will try, ahead of using <code>&quot;C&quot;</code>, the system default locale if all the locales given by environment variables fail.  </p>
<h3>-DL runtime option now added for tracing locale setting</h3>
<p> This is designed for Perl core developers to aid in field debugging bugs regarding locales.  </p>
<code></code><code></code><code></code><code></code><h3>-F now implies -a and -a implies -n</h3>
<p> Previously <code>-F</code> without <code>-a</code> was a no-op, and <code>-a</code> without <code>-n</code> or <code>-p</code> was a no-op, with this change, if you supply <code>-F</code> then both <code>-a</code> and <code>-n</code> are implied and if you supply <code>-a</code> then <code>-n</code> is implied. </p>
<p> You can still use <code>-p</code> for its extra behaviour. [perl #116190]  </p>
<h3>$a and $b warnings exemption</h3>
<p> The special variables <code>$a</code> and <code>$b</code>, used in <code>&quot;sort&quot;</code>, are now exempt from ``used once&#8217;&#8216; warnings, even where <code>&quot;sort&quot;</code> is not used. This makes it easier for <font SIZE="-1">CPAN</font> modules to provide functions using <code>$a</code> and <code>$b</code> for similar purposes. [perl #120462]  </p>
<h2>Security</h2>
<code></code><h3>Avoid possible read of free() d memory during parsing</h3>
<p> It was possible that <code>free()</code>d memory could be read during parsing in the unusual circumstance of the Perl program ending with a heredoc and the last line of the file on disk having no terminating newline character. This has now been fixed.  </p>
<h2>Incompatible Changes</h2>
<h3>do can no longer be used to call subroutines</h3>
<p> The <code>&quot;do SUBROUTINE(LIST)&quot;</code> form has resulted in a deprecation warning since Perl v5.0.0, and is now a syntax error.  </p>
<h3>Quote-like escape changes</h3>
<p> The character after <code>&quot;\c&quot;</code> in a double-quoted string (``...&#8216;&#8216; or qq(...)) or regular expression must now be a printable character and may not be <code>&quot;{&quot;</code>. </p>
<p> A literal <code>&quot;{&quot;</code> after <code>&quot;\B&quot;</code> or <code>&quot;\b&quot;</code> is now fatal. </p>
<p> These were deprecated in perl v5.14.0.  </p>
<h3>Tainting happens under more circumstances; now conforms to documentation</h3>
<p> This affects regular expression matching and changing the case of a string (<code>&quot;lc&quot;</code>, <code>&quot;\U&quot;</code>, <i>etc</i>.) within the scope of <code>&quot;use locale&quot;</code>. The result is now tainted based on the operation, no matter what the contents of the string were, as the documentation (perlsec, ``<font SIZE="-1">SECURITY&#8217;&#8216;</font> in perllocale) indicates it should. Previously, for the case change operation, if the string contained no characters whose case change could be affected by the locale, the result would not be tainted. For example, the result of <code>&quot;uc()&quot;</code> on an empty string or one containing only above-Latin1 code points is now tainted, and wasn&#8217;t before. This leads to more consistent tainting results. Regular expression patterns taint their non-binary results (like <code>$&amp;</code>, <code>$2</code>) if and only if the pattern contains elements whose matching depends on the current (potentially tainted) locale. Like the case changing functions, the actual contents of the string being matched now do not matter, whereas formerly it did. For example, if the pattern contains a <code>&quot;\w&quot;</code>, the results will be tainted even if the match did not have to use that portion of the pattern to succeed or fail, because what a <code>&quot;\w&quot;</code> matches depends on locale. However, for example, a <code>&quot;.&quot;</code> in a pattern will not enable tainting, because the dot matches any single character, and what the current locale is doesn&#8217;t change in any way what matches and what doesn&#8217;t.  </p>
<h3>\p{}, \P{} matching has changed for non-Unicode code points.</h3>
<p> <code>&quot;\p{}&quot;</code> and <code>&quot;\P{}&quot;</code> are defined by Unicode only on Unicode-defined code points (<code>&quot;U+0000&quot;</code> through <code>&quot;U+10FFFF&quot;</code>). Their behavior on matching these legal Unicode code points is unchanged, but there are changes for code points <code>0x110000</code> and above. Previously, Perl treated the result of matching <code>&quot;\p{}&quot;</code> and <code>&quot;\P{}&quot;</code> against these as <code>&quot;undef&quot;</code>, which translates into ``false&#8217;&#8216;. For <code>&quot;\P{}&quot;</code>, this was then complemented into ``true&#8217;&#8216;. A warning was supposed to be raised when this happened. However, various optimizations could prevent the warning, and the results were often counter-intuitive, with both a match and its seeming complement being false. Now all non-Unicode code points are treated as typical unassigned Unicode code points. This generally is more Do-What-I-Mean. A warning is raised only if the results are arguably different from a strict Unicode approach, and from what Perl used to do. Code that needs to be strictly Unicode compliant can make this warning fatal, and then Perl always raises the warning. </p>
<p> Details are in ``Beyond Unicode code points&#8217;&#8216; in perlunicode.  </p>
<h3>\p{All} has been expanded to match all possible code points</h3>
<p> The Perl-defined regular expression pattern element <code>&quot;\p{All}&quot;</code>, unused on <font SIZE="-1">CPAN,</font> used to match just the Unicode code points; now it matches all possible code points; that is, it is equivalent to <code>&quot;qr/./s&quot;</code>. Thus <code>&quot;\p{All}&quot;</code> is no longer synonymous with <code>&quot;\p{Any}&quot;</code>, which continues to match just the Unicode code points, as Unicode says it should.  </p>
<h3>Data::Dumper's output may change</h3>
<p> Depending on the data structures dumped and the settings set for Data::Dumper, the dumped output may have changed from previous versions. </p>
<p> If you have tests that depend on the exact output of Data::Dumper, they may fail. </p>
<p> To avoid this problem in your code, test against the data structure from evaluating the dumped structure, instead of the dump itself.  </p>
<h3>Locale decimal point character no longer leaks outside of use locale scope</h3>
<p> This is actually a bug fix, but some code has come to rely on the bug being present, so this change is listed here. The current locale that the program is running under is not supposed to be visible to Perl code except within the scope of a <code>&quot;use locale&quot;</code>. However, until now under certain circumstances, the character used for a decimal point (often a comma) leaked outside the scope. If your code is affected by this change, simply add a <code>&quot;use locale&quot;</code>.  </p>
<i></i><code></code><h3>Assignments of Windows sockets error codes to $! now prefer errno.h values over WSAGetLastError() values</h3>
<p> In previous versions of Perl, Windows sockets error codes as returned by <code>WSAGetLastError()</code> were assigned to $!, and some constants such as <font SIZE="-1">ECONNABORTED,</font> not in <i>errno.h</i> in <font SIZE="-1">VC++</font> (or the various Windows ports of gcc) were defined to corresponding WSAE* values to allow $! to be tested against the E* constants exported by Errno and <font SIZE="-1">POSIX</font>. </p>
<p> This worked well until <font SIZE="-1">VC++ 2010</font> and later, which introduced new E* constants with values &gt; 100 into <i>errno.h</i>, including some being (re)defined by perl to WSAE* values. That caused problems when linking <font SIZE="-1">XS</font> code against other libraries which used the original definitions of <i>errno.h</i> constants. </p>
<p> To avoid this incompatibility, perl now maps WSAE* error codes to E* values where possible, and assigns those values to $!. The E* constants exported by Errno and <font SIZE="-1">POSIX</font> are updated to match so that testing $! against them, wherever previously possible, will continue to work as expected, and all E* constants found in <i>errno.h</i> are now exported from those modules with their original <i>errno.h</i> values. </p>
<p> In order to avoid breakage in existing Perl code which assigns WSAE* values to $!, perl now intercepts the assignment and performs the same mapping to E* values as it uses internally when assigning to $! itself. </p>
<p> However, one backwards-incompatibility remains: existing Perl code which compares $! against the numeric values of the WSAE* error codes that were previously assigned to $! will now be broken in those cases where a corresponding E* value has been assigned instead. This is only an issue for those E* values &lt; 100, which were always exported from Errno and <font SIZE="-1">POSIX</font> with their original <i>errno.h</i> values, and therefore could not be used for WSAE* error code tests (e.g. <font SIZE="-1">WSAEINVAL</font> is 10022, but the corresponding <font SIZE="-1">EINVAL</font> is 22). (E* values &gt; 100, if present, were redefined to WSAE* values anyway, so compatibility can be achieved by using the E* constants, which will work both before and after this change, albeit using different numeric values under the hood.)  </p>
<h3>Functions PerlIO_vsprintf and PerlIO_sprintf have been removed</h3>
<p> These two functions, undocumented, unused in <font SIZE="-1">CPAN,</font> and problematic, have been removed.  </p>
<h2>Deprecations</h2>
<h3>The /\C/ character class</h3>
<p> The <code>&quot;/\C/&quot;</code> regular expression character class is deprecated. From perl 5.22 onwards it will generate a warning, and from perl 5.24 onwards it will be a regular expression compiler error. If you need to examine the individual bytes that make up a UTF8-encoded character, then use <code>&quot;utf8::encode()&quot;</code> on the string (or a copy) first.  </p>
<h3>Literal control characters in variable names</h3>
<p> This deprecation affects things like $\cT, where \cT is a literal control (such as a <code>&quot;NAK&quot;</code> or <code>&quot;NEGATIVE ACKNOWLEDGE&quot;</code> character) in the source code. Surprisingly, it appears that originally this was intended as the canonical way of accessing variables like $^T, with the caret form only being added as an alternative. </p>
<p> The literal control form is being deprecated for two main reasons. It has what are likely unfixable bugs, such as $\cI not working as an alias for $^I, and their usage not being portable to non-ASCII platforms: While $^T will work everywhere, \cT is whitespace in <font SIZE="-1">EBCDIC.</font> [perl #119123]  </p>
<h3>References to non-integers and non-positive integers in $/</h3>
<p> Setting <code>$/</code> to a reference to zero or a reference to a negative integer is now deprecated, and will behave <code>exactly</code> as though it was set to <code>&quot;undef&quot;</code>. If you want slurp behavior set <code>$/</code> to <code>&quot;undef&quot;</code> explicitly. </p>
<p> Setting <code>$/</code> to a reference to a non integer is now forbidden and will throw an error. Perl has never documented what would happen in this context and while it used to behave the same as setting <code>$/</code> to the address of the references in future it may behave differently, so we have forbidden this usage.  </p>
<font SIZE="-1"></font><h3>Character matching routines in POSIX</h3>
<p> Use of any of these functions in the <code>&quot;POSIX&quot;</code> module is now deprecated: <code>&quot;isalnum&quot;</code>, <code>&quot;isalpha&quot;</code>, <code>&quot;iscntrl&quot;</code>, <code>&quot;isdigit&quot;</code>, <code>&quot;isgraph&quot;</code>, <code>&quot;islower&quot;</code>, <code>&quot;isprint&quot;</code>, <code>&quot;ispunct&quot;</code>, <code>&quot;isspace&quot;</code>, <code>&quot;isupper&quot;</code>, and <code>&quot;isxdigit&quot;</code>. The functions are buggy and don&#8217;t work on <font SIZE="-1">UTF-8</font> encoded strings. See their entries in <font SIZE="-1">POSIX</font> for more information. </p>
<p> A warning is raised on the first call to any of them from each place in the code that they are called. (Hence a repeated statement in a loop will raise just the one warning.)  </p>
<i></i><h3>Interpreter-based threads are now discouraged</h3>
<p> The ``interpreter-based threads&#8217;&#8216; provided by Perl are not the fast, lightweight system for multitasking that one might expect or hope for. Threads are implemented in a way that make them easy to misuse. Few people know how to use them correctly or will be able to provide help. </p>
<p> The use of interpreter-based threads in perl is officially discouraged.  </p>
<h3>Module removals</h3>
<p> The following modules will be removed from the core distribution in a future release, and will at that time need to be installed from <font SIZE="-1">CPAN.</font> Distributions on <font SIZE="-1">CPAN</font> which require these modules will need to list them as prerequisites. </p>
<p> The core versions of these modules will now issue <code>&quot;deprecated&quot;</code>-category warnings to alert you to this fact. To silence these deprecation warnings, install the modules in question from <font SIZE="-1">CPAN.</font> </p>
<p> Note that the planned removal of these modules from core does not reflect a judgement about the quality of the code and should not be taken as a suggestion that their use be halted. Their disinclusion from core primarily hinges on their necessity to bootstrapping a fully functional, CPAN-capable Perl installation, not on concerns over their design. </p>
<dl>
<dt><font SIZE="-1">CGI</font> and its associated <font SIZE="-1">CGI::</font> packages</dt>
<dd>  </dd>
<dt>inc::latest</dt>
<dd>  </dd>
<dt>Package::Constants</dt>
<dd>  </dd>
<dt>Module::Build and its associated Module::Build:: packages</dt>
<dd>  </dd></dl>
<h3>Utility removals</h3>
<p> The following utilities will be removed from the core distribution in a future release, and will at that time need to be installed from <font SIZE="-1">CPAN.</font> </p>
<dl>
<dt>find2perl</dt>
<dd>  </dd>
<dt>s2p</dt>
<dd>  </dd>
<dt>a2p</dt>
<dd>  </dd></dl>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Perl has a new copy-on-write mechanism that avoids the need to copy the internal string buffer when assigning from one scalar to another. This makes copying large strings appear much faster. Modifying one of the two (or more) strings after an assignment will force a copy internally. This makes it unnecessary to pass strings by reference for efficiency. </p>
<p> This feature was already available in 5.18.0, but wasn&#8217;t enabled by default. It is the default now, and so you no longer need build perl with the <i>Configure</i> argument: </p>
<pre><code>    -Accflags=-DPERL_NEW_COPY_ON_WRITE
</code></pre>
<p> It can be disabled (for now) in a perl build with: </p>
<pre><code>    -Accflags=-DPERL_NO_COW
</code></pre>
<p> On some operating systems Perl can be compiled in such a way that any attempt to modify string buffers shared by multiple SVs will crash. This way <font SIZE="-1">XS</font> authors can test that their modules handle copy-on-write scalars correctly. See ``Copy on Write&#8217;&#8216; in perlguts for detail. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl has an optimizer for regular expression patterns. It analyzes the pattern to find things such as the minimum length a string has to be to match, etc. It now better handles code points that are above the Latin1 range. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Executing a regex that contains the <code>&quot;^&quot;</code> anchor (or its variant under the <code>&quot;/m&quot;</code> flag) has been made much faster in several situations. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Precomputed hash values are now used in more places during method lookup. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Constant hash key lookups (<code>$hash{key}</code> as opposed to <code>$hash{$key}</code>) have long had the internal hash value computed at compile time, to speed up lookup. This optimisation has only now been applied to hash slices as well. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Combined <code>&quot;and&quot;</code> and <code>&quot;or&quot;</code> operators in void context, like those generated for <code>&quot;unless ($a &amp;&amp; $b)&quot;</code> and <code>&quot;if ($a || b)&quot;</code> now short circuit directly to the end of the statement. [perl #120128] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In certain situations, when <code>&quot;return&quot;</code> is the last statement in a subroutine&#8217;s main scope, it will be optimized out. This means code like: </p>
<pre><code>  sub baz { return $cat; }
</code></pre>
<p> will now behave like: </p>
<pre><code>  sub baz { $cat; }
</code></pre>
<p> which is notably faster. </p>
<p> [perl #120765] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Code like: </p>
<pre><code>  my $x; # or @x, %x
  my $y;
</code></pre>
<p> is now optimized to: </p>
<pre><code>  my ($x, $y);
</code></pre>
<p> In combination with the padrange optimization introduced in v5.18.0, this means longer uninitialized my variable statements are also optimized, so: </p>
<pre><code>  my $x; my @y; my %z;
</code></pre>
<p> becomes: </p>
<pre><code>  my ($x, @y, %z);
</code></pre>
<p> [perl #121077] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The creation of certain sorts of lists, including array and hash slices, is now faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The optimisation for arrays indexed with a small constant integer is now applied for integers in the range -128..127, rather than 0..255. This should speed up Perl code using expressions like <code>$x[-1]</code>, at the expense of (presumably much rarer) code using expressions like <code>$x[200]</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The first iteration over a large hash (using <code>&quot;keys&quot;</code> or <code>&quot;each&quot;</code>) is now faster. This is achieved by preallocating the hash&#8217;s internal iterator state, rather than lazily creating it when the hash is first iterated. (For small hashes, the iterator is still created only when first needed. The assumption is that small hashes are more likely to be used as objects, and therefore never allocated. For large hashes, that&#8217;s less likely to be true, and the cost of allocating the iterator is swamped by the cost of allocating space for the hash itself.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When doing a global regex match on a string that came from the <code>&quot;readline&quot;</code> or <code>&quot;&lt;&gt;&quot;</code> operator, the data is no longer copied unnecessarily. [perl #121259] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Dereferencing (as in <code>&quot;$obj-&gt;[0]&quot;</code> or <code>&quot;$obj-&gt;{k}&quot;</code>) is now faster when <code>$obj</code> is an instance of a class that has overloaded methods, but doesn&#8217;t overload any of the dereferencing methods <code>&quot;@{}&quot;</code>, <code>&quot;%{}&quot;</code>, and so on. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl&#8217;s optimiser no longer skips optimising code that follows certain <code>&quot;eval {}&quot;</code> expressions (including those with an apparent infinite loop). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The implementation now does a better job of avoiding meaningless work at runtime. Internal effect-free ``null&#8217;&#8216; operations (created as a side-effect of parsing Perl programs) are normally deleted during compilation. That deletion is now applied in some situations that weren&#8217;t previously handled. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now does less disk I/O when dealing with Unicode properties that cover up to three ranges of consecutive code points. </p>
 </dd></dl>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> experimental 0.007 has been added to the Perl core. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO::Socket::IP 0.29 has been added to the Perl core. </p>
 </dd></dl>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Archive::Tar has been upgraded from version 1.90 to 1.96. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> arybase has been upgraded from version 0.06 to 0.07. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Attribute::Handlers has been upgraded from version 0.94 to 0.96. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> attributes has been upgraded from version 0.21 to 0.22. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> autodie has been upgraded from version 2.13 to 2.23. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> AutoLoader has been upgraded from version 5.73 to 5.74. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> autouse has been upgraded from version 1.07 to 1.08. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B has been upgraded from version 1.42 to 1.48. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Concise has been upgraded from version 0.95 to 0.992. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Debug has been upgraded from version 1.18 to 1.19. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Deparse has been upgraded from version 1.20 to 1.26. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> base has been upgraded from version 2.18 to 2.22. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Benchmark has been upgraded from version 1.15 to 1.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> bignum has been upgraded from version 0.33 to 0.37. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Carp has been upgraded from version 1.29 to 1.3301. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CGI</font> has been upgraded from version 3.63 to 3.65. <font SIZE="-1">NOTE:</font> <font SIZE="-1">CGI</font> is deprecated and may be removed from a future version of Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> charnames has been upgraded from version 1.36 to 1.40. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Class::Struct has been upgraded from version 0.64 to 0.65. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compress::Raw::Bzip2 has been upgraded from version 2.060 to 2.064. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compress::Raw::Zlib has been upgraded from version 2.060 to 2.065. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Config::Perl::V has been upgraded from version 0.17 to 0.20. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> constant has been upgraded from version 1.27 to 1.31. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CPAN</font> has been upgraded from version 2.00 to 2.05. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> CPAN::Meta has been upgraded from version 2.120921 to 2.140640. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> CPAN::Meta::Requirements has been upgraded from version 2.122 to 2.125. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> CPAN::Meta::YAML has been upgraded from version 0.008 to 0.012. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Data::Dumper has been upgraded from version 2.145 to 2.151. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">DB</font> has been upgraded from version 1.04 to 1.07. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DB_File has been upgraded from version 1.827 to 1.831. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DBM_Filter has been upgraded from version 0.05 to 0.06. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> deprecate has been upgraded from version 0.02 to 0.03. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::Peek has been upgraded from version 1.11 to 1.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::PPPort has been upgraded from version 3.20 to 3.21. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> diagnostics has been upgraded from version 1.31 to 1.34. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Digest::MD5 has been upgraded from version 2.52 to 2.53. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Digest::SHA has been upgraded from version 5.84 to 5.88. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DynaLoader has been upgraded from version 1.18 to 1.25. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Encode has been upgraded from version 2.49 to 2.60. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> encoding has been upgraded from version 2.6_01 to 2.12. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> English has been upgraded from version 1.06 to 1.09. </p>
<p> <code>$OLD_PERL_VERSION</code> was added as an alias of <code>$]</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Errno has been upgraded from version 1.18 to 1.20_03. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Exporter has been upgraded from version 5.68 to 5.70. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::CBuilder has been upgraded from version 0.280210 to 0.280216. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Command has been upgraded from version 1.17 to 1.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Embed has been upgraded from version 1.30 to 1.32. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Install has been upgraded from version 1.59 to 1.67. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::MakeMaker has been upgraded from version 6.66 to 6.98. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Miniperl has been upgraded from version to 1.01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::ParseXS has been upgraded from version 3.18 to 3.24. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Typemaps has been upgraded from version 3.19 to 3.24. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::XSSymSet has been upgraded from version 1.2 to 1.3. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> feature has been upgraded from version 1.32 to 1.36. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> fields has been upgraded from version 2.16 to 2.17. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Basename has been upgraded from version 2.84 to 2.85. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Copy has been upgraded from version 2.26 to 2.29. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::DosGlob has been upgraded from version 1.10 to 1.12. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Fetch has been upgraded from version 0.38 to 0.48. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Find has been upgraded from version 1.23 to 1.27. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Glob has been upgraded from version 1.20 to 1.23. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Spec has been upgraded from version 3.40 to 3.47. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Temp has been upgraded from version 0.23 to 0.2304. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> FileCache has been upgraded from version 1.08 to 1.09. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Filter::Simple has been upgraded from version 0.89 to 0.91. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Filter::Util::Call has been upgraded from version 1.45 to 1.49. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Getopt::Long has been upgraded from version 2.39 to 2.42. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Getopt::Std has been upgraded from version 1.07 to 1.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hash::Util::FieldHash has been upgraded from version 1.10 to 1.15. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> HTTP::Tiny has been upgraded from version 0.025 to 0.043. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> I18N::Langinfo has been upgraded from version 0.10 to 0.11. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> I18N::LangTags has been upgraded from version 0.39 to 0.40. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> if has been upgraded from version 0.0602 to 0.0603. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> inc::latest has been upgraded from version 0.4003 to 0.4205. <font SIZE="-1">NOTE:</font> inc::latest is deprecated and may be removed from a future version of Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> integer has been upgraded from version 1.00 to 1.01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">IO</font> has been upgraded from version 1.28 to 1.31. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO::Compress::Gzip and friends have been upgraded from version 2.060 to 2.064. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::Cmd has been upgraded from version 0.80 to 0.92. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::Open3 has been upgraded from version 1.13 to 1.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::SysV has been upgraded from version 2.03 to 2.04. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">JSON::PP</font> has been upgraded from version 2.27202 to 2.27203. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> List::Util has been upgraded from version 1.27 to 1.38. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> locale has been upgraded from version 1.02 to 1.03. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locale::Codes has been upgraded from version 3.25 to 3.30. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locale::Maketext has been upgraded from version 1.23 to 1.25. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigInt has been upgraded from version 1.9991 to 1.9993. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigInt::FastCalc has been upgraded from version 0.30 to 0.31. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigRat has been upgraded from version 0.2604 to 0.2606. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> MIME::Base64 has been upgraded from version 3.13 to 3.14. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Build has been upgraded from version 0.4003 to 0.4205. <font SIZE="-1">NOTE:</font> Module::Build is deprecated and may be removed from a future version of Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::CoreList has been upgraded from version 2.89 to 3.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Load has been upgraded from version 0.24 to 0.32. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Load::Conditional has been upgraded from version 0.54 to 0.62. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Metadata has been upgraded from version 1.000011 to 1.000019. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> mro has been upgraded from version 1.11 to 1.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Net::Ping has been upgraded from version 2.41 to 2.43. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Opcode has been upgraded from version 1.25 to 1.27. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Package::Constants has been upgraded from version 0.02 to 0.04. <font SIZE="-1">NOTE:</font> Package::Constants is deprecated and may be removed from a future version of Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Params::Check has been upgraded from version 0.36 to 0.38. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> parent has been upgraded from version 0.225 to 0.228. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Parse::CPAN::Meta has been upgraded from version 1.4404 to 1.4414. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl::OSType has been upgraded from version 1.003 to 1.007. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlfaq has been upgraded from version 5.0150042 to 5.0150044. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO has been upgraded from version 1.07 to 1.09. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::encoding has been upgraded from version 0.16 to 0.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::scalar has been upgraded from version 0.16 to 0.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::via has been upgraded from version 0.12 to 0.14. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Escapes has been upgraded from version 1.04 to 1.06. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Functions has been upgraded from version 1.06 to 1.08. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Html has been upgraded from version 1.18 to 1.21. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Parser has been upgraded from version 1.60 to 1.62. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Perldoc has been upgraded from version 3.19 to 3.23. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Usage has been upgraded from version 1.61 to 1.63. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">POSIX</font> has been upgraded from version 1.32 to 1.38_03. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> re has been upgraded from version 0.23 to 0.26. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Safe has been upgraded from version 2.35 to 2.37. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Scalar::Util has been upgraded from version 1.27 to 1.38. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> SDBM_File has been upgraded from version 1.09 to 1.11. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Socket has been upgraded from version 2.009 to 2.013. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Storable has been upgraded from version 2.41 to 2.49. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> strict has been upgraded from version 1.07 to 1.08. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> subs has been upgraded from version 1.01 to 1.02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Sys::Hostname has been upgraded from version 1.17 to 1.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Sys::Syslog has been upgraded from version 0.32 to 0.33. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Term::Cap has been upgraded from version 1.13 to 1.15. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Term::ReadLine has been upgraded from version 1.12 to 1.14. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test::Harness has been upgraded from version 3.26 to 3.30. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test::Simple has been upgraded from version 0.98 to 1.001002. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Text::ParseWords has been upgraded from version 3.28 to 3.29. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Text::Tabs has been upgraded from version 2012.0818 to 2013.0523. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Text::Wrap has been upgraded from version 2012.0818 to 2013.0523. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Thread has been upgraded from version 3.02 to 3.04. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Thread::Queue has been upgraded from version 3.02 to 3.05. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> threads has been upgraded from version 1.86 to 1.93. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> threads::shared has been upgraded from version 1.43 to 1.46. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::Array has been upgraded from version 1.05 to 1.06. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::File has been upgraded from version 0.99 to 1.00. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::Hash has been upgraded from version 1.04 to 1.05. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::Scalar has been upgraded from version 1.02 to 1.03. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::StdHandle has been upgraded from version 4.3 to 4.4. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::HiRes has been upgraded from version 1.9725 to 1.9726. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::Piece has been upgraded from version 1.20_01 to 1.27. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::Collate has been upgraded from version 0.97 to 1.04. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::Normalize has been upgraded from version 1.16 to 1.17. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::UCD has been upgraded from version 0.51 to 0.57. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> utf8 has been upgraded from version 1.10 to 1.13. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> version has been upgraded from version 0.9902 to 0.9908. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> vmsish has been upgraded from version 1.03 to 1.04. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> warnings has been upgraded from version 1.18 to 1.23. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Win32 has been upgraded from version 0.47 to 0.49. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> XS::Typemap has been upgraded from version 0.10 to 0.13. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> XSLoader has been upgraded from version 0.16 to 0.17. </p>
 </dd></dl>
<h2>Documentation</h2>
<h3>New Documentation</h3>
<p> <i>perlrepository</i> </p>
<p> This document was removed (actually, renamed perlgit and given a major overhaul) in Perl v5.14, causing Perl documentation websites to show the now out of date version in Perl v5.12 as the latest version. It has now been restored in stub form, directing readers to current information.  </p>
<h3>Changes to Existing Documentation</h3>
<p> <i>perldata</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> New sections have been added to document the new index/value array slice and key/value hash slice syntax. </p>
 </dd></dl>
<p> <i>perldebguts</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;DB::goto&quot;</code> and <code>&quot;DB::lsub&quot;</code> debugger subroutines are now documented. [perl #77680] </p>
 </dd></dl>
<p> <i>perlexperiment</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;\s&quot;</code> matching <code>&quot;\cK&quot;</code> is marked experimental. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ithreads were accepted in v5.8.0 (but are discouraged as of v5.20.0). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Long doubles are not considered experimental. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Code in regular expressions, regular expression backtracking verbs, and lvalue subroutines are no longer listed as experimental. (This also affects perlre and perlsub.) </p>
 </dd></dl>
<p> <i>perlfunc</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;chop&quot;</code> and <code>&quot;chomp&quot;</code> now note that they can reset the hash iterator. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;exec&quot;</code>&#8216;s handling of arguments is now more clearly documented. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;eval EXPR&quot;</code> now has caveats about expanding floating point numbers in some locales. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;goto EXPR&quot;</code> is now documented to handle an expression that evalutes to a code reference as if it was <code>&quot;goto &amp;$coderef&quot;</code>. This behavior is at least ten years old. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Since Perl v5.10, it has been possible for subroutines in <code>@INC</code> to return a reference to a scalar holding initial source code to prepend to the file. This is now documented. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The documentation of <code>&quot;ref&quot;</code> has been updated to recommend the use of <code>&quot;blessed&quot;</code>, <code>&quot;isa&quot;</code> and <code>&quot;reftype&quot;</code> when dealing with references to blessed objects. </p>
 </dd></dl>
<p> <i>perlguts</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Numerous minor changes have been made to reflect changes made to the perl internals in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> New sections on Read-Only Values and Copy on Write have been added. </p>
 </dd></dl>
<p> <i>perlhack</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The Super Quick Patch Guide section has been updated. </p>
 </dd></dl>
<p> <i>perlhacktips</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The documentation has been updated to include some more examples of <code>&quot;gdb&quot;</code> usage. </p>
 </dd></dl>
<p> <i>perllexwarn</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The perllexwarn documentation used to describe the hierarchy of warning categories understood by the warnings pragma. That description has now been moved to the warnings documentation itself, leaving perllexwarn as a stub that points to it. This change consolidates all documentation for lexical warnings in a single place. </p>
 </dd></dl>
<p> <i>perllocale</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The documentation now mentions <i></i>fc()<i></i> and <code>&quot;\F&quot;</code>, and includes many clarifications and corrections in general. </p>
 </dd></dl>
<p> <i>perlop</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The language design of Perl has always called for monomorphic operators. This is now mentioned explicitly. </p>
 </dd></dl>
<p> <i>perlopentut</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;open&quot;</code> tutorial has been completely rewritten by Tom Christiansen, and now focuses on covering only the basics, rather than providing a comprehensive reference to all things openable. This rewrite came as the result of a vigorous discussion on perl5-porters kicked off by a set of improvements written by Alexander Hartmaier to the existing perlopentut. A &quot;more than you ever wanted to know about <code>&quot;open&quot;</code>&quot; document may follow in subsequent versions of perl. </p>
 </dd></dl>
<p> <i>perlre</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The fact that the regexp engine makes no effort to call (?{}) and (??{}) constructs any specified number of times (although it will basically <font SIZE="-1">DWIM</font> in case of a successful match) has been documented. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;/r&quot;</code> modifier (for non-destructive substitution) is now documented. [perl #119151] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The documentation for <code>&quot;/x&quot;</code> and <code>&quot;(?# comment)&quot;</code> has been expanded and clarified. </p>
 </dd></dl>
<p> <i>perlreguts</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The documentation has been updated in the light of recent changes to <i>regcomp.c</i>. </p>
 </dd></dl>
<p> <i>perlsub</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The need to predeclare recursive functions with prototypes in order for the prototype to be honoured in the recursive call is now documented. [perl #2726] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A list of subroutine names used by the perl implementation is now included. [perl #77680] </p>
 </dd></dl>
<p> <i>perltrap</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> There is now a JavaScript section. </p>
 </dd></dl>
<p> <i>perlunicode</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The documentation has been updated to reflect <code>&quot;Bidi_Class&quot;</code> changes in Unicode 6.3. </p>
 </dd></dl>
<p> <i>perlvar</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A new section explaining the performance issues of $`, $&amp; and $&#8216;, including workarounds and changes in different versions of Perl, has been added. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Three English variable names which have long been documented but do not actually exist have been removed from the documentation. These were <code>$OLD_PERL_VERSION</code>, <code>$OFMT</code>, and <code>$ARRAY_BASE</code>. </p>
<p> (Actually, <code>&quot;OLD_PERL_VERSION&quot;</code> <i>does</i> exist, starting with this revision, but remained undocumented until perl 5.22.0.) </p>
 </dd></dl>
<p> <i>perlxs</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Several problems in the <code>&quot;MY_CXT&quot;</code> example have been fixed. </p>
 </dd></dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.  </p>
<h3>New Diagnostics</h3>
<p> <i>New Errors</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> delete argument is index/value array slice, use array slice </p>
<p> (F) You used index/value array slice syntax (<code>%array[...]</code>) as the argument to <code>&quot;delete&quot;</code>. You probably meant <code>@array[...]</code> with an @ symbol instead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> delete argument is key/value hash slice, use hash slice </p>
<p> (F) You used key/value hash slice syntax (<code>%hash{...}</code>) as the argument to <code>&quot;delete&quot;</code>. You probably meant <code>@hash{...}</code> with an @ symbol instead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Magical list constants are not supported </p>
<p> (F) You assigned a magical array to a stash element, and then tried to use the subroutine from the same slot. You are asking Perl to do something it cannot do, details subject to change between Perl versions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Added Setting $/ to a <code>%s</code> reference is forbidden </p>
 </dd></dl>
<p> <i>New Warnings</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>%s</code> on reference is experimental: </p>
<p> The ``auto-deref&#8217;&#8216; feature is experimental. </p>
<p> Starting in v5.14.0, it was possible to use push, pop, keys, and other built-in functions not only on aggregate types, but on references to them. The feature was not deployed to its original intended specification, and now may become redundant to postfix dereferencing. It has always been categorized as an experimental feature, and in v5.20.0 is carries a warning as such. </p>
<p> Warnings will now be issued at compile time when these operations are detected. </p>
<pre><code>  no if $] &gt;= 5.01908, warnings =&gt; &quot;experimental::autoderef&quot;;
</code></pre>
<p> Consider, though, replacing the use of these features, as they may change behavior again before becoming stable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A sequence of multiple spaces in a charnames alias definition is deprecated </p>
<p> Trailing white-space in a charnames alias definition is deprecated </p>
<p> These two deprecation warnings involving <code>&quot;\N{...}&quot;</code> were incorrectly implemented. They did not warn by default (now they do) and could not be made fatal via <code>&quot;use warnings FATAL =&gt; &#8216;deprecated&#8217;&quot;</code> (now they can). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Attribute prototype(%s) discards earlier prototype attribute in same sub </p>
<p> (W misc) A sub was declared as <code>&quot;sub foo : prototype(A) : prototype(B) {}&quot;</code>, for example. Since each sub can only have one prototype, the earlier declaration(s) are discarded while the last one is applied. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Invalid \0 character in <code>%s</code> for <code>%s:</code> <code>%s</code>\0%s </p>
<p> (W syscalls) Embedded \0 characters in pathnames or other system call arguments produce a warning as of 5.20. The parts after the \0 were formerly ignored by system calls. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Matched non-Unicode code point 0x%X against Unicode property; may not be portable. </p>
<p> This replaces the message ``Code point 0x%X is not Unicode, all \p{} matches fail; all \P{} matches succeed&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Missing &#8216;]&#8216; in prototype for <code>%s</code> : <code>%s</code> </p>
<p> (W illegalproto) A grouping was started with <code>&quot;[&quot;</code> but never closed with <code>&quot;]&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Possible precedence issue with control flow operator </p>
<p> (W syntax) There is a possible problem with the mixing of a control flow operator (e.g. <code>&quot;return&quot;</code>) and a low-precedence operator like <code>&quot;or&quot;</code>. Consider: </p>
<pre><code>    sub { return $a or $b; }
</code></pre>
<p> This is parsed as: </p>
<pre><code>    sub { (return $a) or $b; }
</code></pre>
<p> Which is effectively just: </p>
<pre><code>    sub { return $a; }
</code></pre>
<p> Either use parentheses or the high-precedence variant of the operator. </p>
<p> Note this may be also triggered for constructs like: </p>
<pre><code>    sub { 1 if die; }
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Postfix dereference is experimental </p>
<p> (S experimental::postderef) This warning is emitted if you use the experimental postfix dereference syntax. Simply suppress the warning if you want to use the feature, but know that in doing so you are taking the risk of using an experimental feature which may change or be removed in a future Perl version: </p>
<pre><code>    no warnings &quot;experimental::postderef&quot;;
    use feature &quot;postderef&quot;, &quot;postderef_qq&quot;;
    $ref-&gt;$*;
    $aref-&gt;@*;
    $aref-&gt;@[@indices];
    ... etc ...
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Prototype &#8216;%s&#8217; overridden by attribute &#8216;prototype(%s)&#8216; in <code>%s</code> </p>
<p> (W prototype) A prototype was declared in both the parentheses after the sub name and via the prototype attribute. The prototype in parentheses is useless, since it will be replaced by the prototype from the attribute before it&#8217;s ever used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Scalar value @%s[%s] better written as $%s[%s] </p>
<p> (W syntax) In scalar context, you&#8217;ve used an array index/value slice (indicated by %) to select a single element of an array. Generally it&#8217;s better to ask for a scalar value (indicated by $). The difference is that <code>$foo[&amp;bar]</code> always behaves like a scalar, both in the value it returns and when evaluating its argument, while <code>%foo[&amp;bar]</code> provides a list context to its subscript, which can do weird things if you&#8217;re expecting only one subscript. When called in list context, it also returns the index (what <code>&amp;bar</code> returns) in addition to the value. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Scalar value @%s{%s} better written as $%s{%s} </p>
<p> (W syntax) In scalar context, you&#8217;ve used a hash key/value slice (indicated by %) to select a single element of a hash. Generally it&#8217;s better to ask for a scalar value (indicated by $). The difference is that <code>$foo{&amp;bar}</code> always behaves like a scalar, both in the value it returns and when evaluating its argument, while <code>@foo{&amp;bar}</code> and provides a list context to its subscript, which can do weird things if you&#8217;re expecting only one subscript. When called in list context, it also returns the key in addition to the value. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Setting $/ to a reference to <code>%s</code> as a form of slurp is deprecated, treating as undef </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unexpected exit <code>%u</code> </p>
<p> (S) <code>exit()</code> was called or the script otherwise finished gracefully when <code>&quot;PERL_EXIT_WARN&quot;</code> was set in <code>&quot;PL_exit_flags&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unexpected exit failure <code>%d</code> </p>
<p> (S) An uncaught <code>die()</code> was called when <code>&quot;PERL_EXIT_WARN&quot;</code> was set in <code>&quot;PL_exit_flags&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of literal control characters in variable names is deprecated </p>
<p> (D deprecated) Using literal control characters in the source to refer to the ^FOO variables, like $^X and ${^GLOBAL_PHASE} is now deprecated. This only affects code like $\cT, where \cT is a control (like a <code>&quot;SOH&quot;</code>) in the source code: ${``\cT&#8217;&#8216;} and $^T remain valid. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Useless use of greediness modifier </p>
<p> This fixes [Perl #42957]. </p>
 </dd></dl>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Warnings and errors from the regexp engine are now <font SIZE="-1">UTF-8</font> clean. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ``Unknown switch condition&#8217;&#8216; error message has some slight changes. This error triggers when there is an unknown condition in a <code>&quot;(?(foo))&quot;</code> conditional. The error message used to read: </p>
<pre><code>    Unknown switch condition (?(%s in regex;
</code></pre>
<p> But what <code>%s</code> could be was mostly up to luck. For <code>&quot;(?(foobar))&quot;</code>, you might have seen ``fo&#8217;&#8216; or ``f&#8217;&#8216;. For Unicode characters, you would generally get a corrupted string. The message has been changed to read: </p>
<pre><code>    Unknown switch condition (?(...)) in regex;
</code></pre>
<p> Additionally, the <code>&#8216;&lt;-- HERE&#8217;</code> marker in the error will now point to the correct spot in the regex. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ``%s &#8216;&#8216;\x%X`` does not map to Unicode&#8217;&#8216; warning is now correctly listed as a severe warning rather than as a fatal error. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under rare circumstances, one could get a ``Can&#8217;t coerce readonly <font SIZE="-1">REF</font> to string&#8217;&#8216; instead of the customary ``Modification of a read-only value&#8217;&#8216;. This alternate error message has been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ``Ambiguous use of * resolved as operator *&#8216;&#8216;: This and similar warnings about ``%&#8216;&#8216; and ``&amp;&#8216;&#8216; used to occur in some circumstances where there was no operator of the type cited, so the warning was completely wrong. This has been fixed [perl #117535, #76910]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Warnings about malformed subroutine prototypes are now more consistent in how the prototypes are rendered. Some of these warnings would truncate prototypes containing nulls. In other cases one warning would suppress another. The warning about illegal characters in prototypes no longer says ``after &#8216;_&#8216;&#8216;&#8216; if the bad character came before the underscore. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl folding rules are not up-to-date for 0x%X; please use the perlbug utility to report; in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
<p> This message is now only in the regexp category, and not in the deprecated category. It is still a default (i.e., severe) warning [perl #89648]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> %%s[%s] in scalar context better written as $%s[%s] </p>
<p> This warning now occurs for any <code>%array[$index]</code> or <code>%hash{key}</code> known to be in scalar context at compile time. Previously it was worded ``Scalar value %%s[%s] better written as $%s[%s]&#8216;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Switch condition not recognized in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/: </p>
<p> The description for this diagnostic has been extended to cover all cases where the warning may occur. Issues with the positioning of the arrow indicator have also been resolved. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The error messages for <code>&quot;my($a?$b$c)&quot;</code> and <code>&quot;my(do{})&quot;</code> now mention ``conditional expression&#8217;&#8216; and ``do block&#8217;&#8216;, respectively, instead of reading &#8216;Can&#8217;t declare null operation in ``my&#8217;&#8216;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When <code>&quot;use re &quot;debug&quot;&quot;</code> executes a regex containing a backreference, the debugging output now shows what string is being matched. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The now fatal error message <code>&quot;Character following &quot;\c&quot; must be ASCII&quot;</code> has been reworded as <code>&quot;Character following &quot;\c&quot; must be printable ASCII&quot;</code> to emphasize that in <code>&quot;\c</code>X <code>&quot;</code>, <i>X</i> must be a <i>printable (non-control)</i> <font SIZE="-1">ASCII</font> character. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<p> <i>a2p</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A possible crash from an off-by-one error when trying to access before the beginning of a buffer has been fixed. [perl #120244] </p>
 </dd></dl>
<p> <i>bisect.pl</i> </p>
<p> The git bisection tool <i>Porting/bisect.pl</i> has had many enhancements. </p>
<p> It is provided as part of the source distribution but not installed because it is not self-contained as it relies on being run from within a git checkout. Note also that it makes no attempt to fix tests, correct runtime bugs or make something useful to install &#8211; its purpose is to make minimal changes to get any historical revision of interest to build and run as close as possible to ``as-was&#8217;&#8216;, and thereby make <code>&quot;git bisect&quot;</code> easy to use. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Can optionally run the test case with a timeout. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can now run in-place in a clean git checkout. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can run the test case under <code>&quot;valgrind&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can apply user supplied patches and fixes to the source checkout before building. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Now has fixups to enable building several more historical ranges of bleadperl, which can be useful for pinpointing the origins of bugs or behaviour changes. </p>
 </dd></dl>
<p> <i>find2perl</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> find2perl now handles <code>&quot;?&quot;</code> wildcards correctly. [perl #113054] </p>
 </dd></dl>
<p> <i>perlbug</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <i>perlbug</i> now has a <code>&quot;-p&quot;</code> option for attaching patches with a bug report. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlbug has been modified to supply the report template with <font SIZE="-1">CRLF</font> line endings on Windows. [perl #121277 &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=121277">https://rt.perl.org/Public/Bug/Display.html?id=121277</a>&gt;] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlbug now makes as few assumptions as possible about the encoding of the report. This will likely change in the future to assume <font SIZE="-1">UTF-8</font> by default but allow a user override. </p>
 </dd></dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The <i>Makefile.PL</i> for SDBM_File now generates a better <i>Makefile</i>, which avoids a race condition during parallel makes, which could cause the build to fail. This is the last known parallel make problem (on *nix platforms), and therefore we believe that a parallel make should now always be error free. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>installperl</i> and <i>installman</i>&#8216;s option handling has been refactored to use Getopt::Long. Both are used by the <i>Makefile</i> <code>&quot;install&quot;</code> targets, and are not installed, so these changes are only likely to affect custom installation scripts. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Single letter options now also have long names. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Invalid options are now rejected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Command line arguments that are not options are now rejected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Each now has a <code>&quot;--help&quot;</code> option to display the usage message. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> The behaviour for all valid documented invocations is unchanged. </p>
 </dd></dl>
<dt>&bull;</dt>
<dd> <p> Where possible, the build now avoids recursive invocations of <i>make</i> when building pure-Perl extensions, without removing any parallelism from the build. Currently around 80 extensions can be processed directly by the <i>make_ext.pl</i> tool, meaning that 80 invocations of <i>make</i> and 160 invocations of <i>miniperl</i> are no longer made. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The build system now works correctly when compiling under <font SIZE="-1">GCC</font> or Clang with link-time optimization enabled (the <code>&quot;-flto&quot;</code> option). [perl #113022] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Distinct library basenames with <code>&quot;d_libname_unique&quot;</code>. </p>
<p> When compiling perl with this option, the library files for <font SIZE="-1">XS</font> modules are named something ``unique&#8217;&#8216; --- for example, Hash/Util/Util.so becomes Hash/Util/PL_Hash__Util.so. This behavior is similar to what currently happens on <font SIZE="-1">VMS,</font> and serves as groundwork for the Android port. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sysroot&quot;</code> option to indicate the logical root directory under gcc and clang. </p>
<p> When building with this option set, both Configure and the compilers search for all headers and libraries under this new sysroot, instead of /. </p>
<p> This is a huge time saver if cross-compiling, but can also help on native builds if your toolchain&#8217;s files have non-standard locations. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The cross-compilation model has been renovated. There&#8217;s several new options, and some backwards-incompatible changes: </p>
<p> We now build binaries for miniperl and generate_uudmap to be used on the host, rather than running every miniperl call on the target; this means that, short of &#8216;make test&#8217;, we no longer need access to the target system once Configure is done. You can provide already-built binaries through the <code>&quot;hostperl&quot;</code> and <code>&quot;hostgenerate&quot;</code> options to Configure. </p>
<p> Additionally, if targeting an <font SIZE="-1">EBCDIC</font> platform from an <font SIZE="-1">ASCII</font> host, or viceversa, you&#8217;ll need to run Configure with <code>&quot;-Uhostgenerate&quot;</code>, to indicate that generate_uudmap should be run on the target. </p>
<p> Finally, there&#8217;s also a way of having Configure end early, right after building the host binaries, by cross-compiling without specifying a <code>&quot;targethost&quot;</code>. </p>
<p> The incompatible changes include no longer using xconfig.h, xlib, or Cross.pm, so canned config files and Makefiles will have to be updated. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Related to the above, there is now a way of specifying the location of sh (or equivalent) on the target system: <code>&quot;targetsh&quot;</code>. </p>
<p> For example, Android has its sh in /system/bin/sh, so if cross-compiling from a more normal Unixy system with sh in /bin/sh, ``targetsh&#8217;&#8216; would end up as /system/bin/sh, and ``sh&#8217;&#8216; as /bin/sh. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> By default, <code>gcc</code> 4.9 does some optimizations that break perl. The <code>-fwrapv</code> option disables those optimizations (and probably others), so for <code>gcc</code> 4.3 and later (since the there might be similar problems lurking on older versions too, but <code>-fwrapv</code> was broken before 4.3, and the optimizations probably won&#8217;t go away), <i>Configure</i> now adds <code>-fwrapv</code> unless the user requests <code>-fno-wrapv</code>, which disables <code>-fwrapv</code>, or <code>-fsanitize=undefined</code>, which turns the overflows <code>-fwrapv</code> ignores into runtime errors. [perl #121505 &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=121505">https://rt.perl.org/Public/Bug/Display.html?id=121505</a>&gt;] </p>
 </dd></dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;test.valgrind&quot;</code> make target now allows tests to be run in parallel. This target allows Perl&#8217;s test suite to be run under Valgrind, which detects certain sorts of C programming errors, though at significant cost in running time. On suitable hardware, allowing parallel execution claws back a lot of that additional cost. [perl #121431] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various tests in <i>t/porting/</i> are no longer skipped when the perl <i>.git</i> directory is outside the perl tree and pointed to by <code>$GIT_DIR</code>. [perl #120505] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The test suite no longer fails when the user&#8217;s interactive shell maintains a <code>$PWD</code> environment variable, but the <i>/bin/sh</i> used for running tests doesn&#8217;t. </p>
 </dd></dl>
<h2>Platform Support</h2>
<h3>New Platforms</h3>
<dl>
<dt>Android</dt>
<dd> <p> Perl can now be built for Android, either natively or through cross-compilation, for all three currently available architectures (<font SIZE="-1">ARM, MIPS,</font> and x86), on a wide range of versions. </p>
 </dd>
<dt>Bitrig</dt>
<dd> <p> Compile support has been added for Bitrig, a fork of OpenBSD. </p>
 </dd>
<dt>FreeMiNT</dt>
<dd> <p> Support has been added for FreeMiNT, a free open-source <font SIZE="-1">OS</font> for the Atari <font SIZE="-1">ST</font> system and its successors, based on the original MiNT that was officially adopted by Atari. </p>
 </dd>
<dt>Synology</dt>
<dd> <p> Synology ships its <font SIZE="-1">NAS</font> boxes with a lean Linux distribution (<font SIZE="-1">DSM</font>) on relative cheap <font SIZE="-1">CPU</font>&#8216;s (like the Marvell Kirkwood mv6282 &#8211; ARMv5tel or Freescale QorIQ P1022 ppc &#8211; e500v2) not meant for workstations or development. These boxes should build now. The basic problems are the non-standard location for tools. </p>
 </dd></dl>
<h3>Discontinued Platforms</h3>
<dl>
<dt>&quot;sfio&quot;</dt>
<dd> <p> Code related to supporting the <code>&quot;sfio&quot;</code> I/O system has been removed. </p>
<p> Perl 5.004 added support to use the native <font SIZE="-1">API</font> of <code>&quot;sfio&quot;</code>, <font SIZE="-1">AT&amp;T</font>&#8216;s Safe/Fast I/O library. This code still built with v5.8.0, albeit with many regression tests failing, but was inadvertently broken before the v5.8.1 release, meaning that it has not worked on any version of Perl released since then. In over a decade we have received no bug reports about this, hence it is clear that no-one is using this functionality on any version of Perl that is still supported to any degree. </p>
 </dd>
<dt><font SIZE="-1">AT&amp;T</font> 3b1</dt>
<dd> <p> Configure support for the 3b1, also known as the <font SIZE="-1">AT&amp;T</font> Unix <font SIZE="-1">PC</font> (and the similar <font SIZE="-1">AT&amp;T 7300</font>), has been removed. </p>
 </dd>
<dt><font SIZE="-1">DG/UX</font></dt>
<dd> <p> <font SIZE="-1">DG/UX</font> was a Unix sold by Data General. The last release was in April 2001. It only runs on Data General&#8217;s own hardware. </p>
 </dd>
<dt><font SIZE="-1">EBCDIC</font></dt>
<dd> <p> In the absence of a regular source of smoke reports, code intended to support native <font SIZE="-1">EBCDIC</font> platforms will be removed from perl before 5.22.0. </p>
 </dd></dl>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>Cygwin</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>recv()</code> on a connected handle would populate the returned sender address with whatever happened to be in the working buffer. <code>recv()</code> now uses a workaround similar to the Win32 <code>recv()</code> wrapper and returns an empty string when <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2) doesn&#8217;t modify the supplied address length. [perl #118843] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a build error in cygwin.c on Cygwin 1.7.28. </p>
<p> Tests now handle the errors that occur when <code>&quot;cygserver&quot;</code> isn&#8217;t running. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>GNU/Hurd</dt>
<dd> <p> The <font SIZE="-1">BSD</font> compatibility library <code>&quot;libbsd&quot;</code> is no longer required for builds. </p>
 </dd>
<dt>Linux</dt>
<dd> <p> The hints file now looks for <code>&quot;libgdbm_compat&quot;</code> only if <code>&quot;libgdbm&quot;</code> itself is also wanted. The former is never useful without the latter, and in some circumstances, including it could actually prevent building. </p>
 </dd>
<dt>Mac <font SIZE="-1">OS</font></dt>
<dd> <p> The build system now honors an <code>&quot;ld&quot;</code> setting supplied by the user running <i>Configure</i>. </p>
 </dd>
<dt>MidnightBSD</dt>
<dd> <p> <code>&quot;objformat&quot;</code> was removed from version 0.4-RELEASE of MidnightBSD and had been deprecated on earlier versions. This caused the build environment to be erroneously configured for <code>&quot;a.out&quot;</code> rather than <code>&quot;elf&quot;</code>. This has been now been corrected. </p>
 </dd>
<dt>Mixed-endian platforms</dt>
<dd> <p> The code supporting <code>&quot;pack&quot;</code> and <code>&quot;unpack&quot;</code> operations on mixed endian platforms has been removed. We believe that Perl has long been unable to build on mixed endian architectures (such as PDP-11s), so we don&#8217;t think that this change will affect any platforms which were able to build v5.18.0. </p>
 </dd>
<dt><font SIZE="-1">VMS</font></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;PERL_ENV_TABLES&quot;</code> feature to control the population of <code>%ENV</code> at perl start-up was broken in Perl 5.16.0 but has now been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Skip access checks on remotes in <code>opendir()</code>. [perl #121002] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A check for glob metacharacters in a path returned by the <code>&quot;glob()&quot;</code> operator has been replaced with a check for <font SIZE="-1">VMS</font> wildcard characters. This saves a significant number of unnecessary <code>&quot;lstat()&quot;</code> calls such that some simple glob operations become 60-80% faster. </p>
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
<dd> <p> <code>&quot;rename&quot;</code> and <code>&quot;link&quot;</code> on Win32 now set $! to <font SIZE="-1">ENOSPC</font> and <font SIZE="-1">EDQUOT</font> when appropriate. [perl #119857] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">BUILD_STATIC</font> and <font SIZE="-1">ALL_STATIC</font> makefile options for linking some or (nearly) all extensions statically (into perl520.dll, and into a separate perl-static.exe too) were broken for MinGW builds. This has now been fixed. </p>
<p> The <font SIZE="-1">ALL_STATIC</font> option has also been improved to include the Encode and Win32 extensions (for both <font SIZE="-1">VC++</font> and MinGW builds). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Support for building with Visual C<font SIZE="-2">++</font> 2013 has been added. There are currently two possible test failures (see ``Testing Perl on Windows&#8217;&#8216; in perlwin32) which will hopefully be resolved soon. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Experimental support for building with Intel C<font SIZE="-2">++</font> Compiler has been added. The nmake makefile (win32/Makefile) and the dmake makefile (win32/makefile.mk) can be used. A ``nmake test&#8217;&#8216; will not pass at this time due to <i>cpan/CGI/t/url.t</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Killing a process tree with ``kill&#8217;&#8216; in perlfunc and a negative signal, was broken starting in 5.18.0. In this bug, <code>&quot;kill&quot;</code> always returned 0 for a negative signal even for valid PIDs, and no processes were terminated. This has been fixed [perl #121230]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The time taken to build perl on Windows has been reduced quite significantly (time savings in the region of 30-40% are typically seen) by reducing the number of, usually failing, I/O calls for each <code>&quot;require()&quot;</code> (for <code>miniperl.exe</code> only). [perl #121119 &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=121119">https://rt.perl.org/Public/Bug/Display.html?id=121119</a>&gt;] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> About 15 minutes of idle sleeping was removed from running <code>&quot;make test&quot;</code> due to a bug in which the timeout monitor used for tests could not be cancelled once the test completes, and the full timeout period elapsed before running the next test file. [perl #121395 &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=121395">https://rt.perl.org/Public/Bug/Display.html?id=121395</a>&gt;] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On a perl built without pseudo-fork (pseudo-fork builds were not affected by this bug), killing a process tree with <code>&quot;kill()&quot;</code> and a negative signal resulted in <code>&quot;kill()&quot;</code> inverting the returned value. For example, if <code>&quot;kill()&quot;</code> killed 1 process tree <font SIZE="-1">PID</font> then it returned 0 instead of 1, and if <code>&quot;kill()&quot;</code> was passed 2 invalid PIDs then it returned 2 instead of 0. This has probably been the case since the process tree kill feature was implemented on Win32. It has now been corrected to follow the documented behaviour. [perl #121230 &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=121230">https://rt.perl.org/Public/Bug/Display.html?id=121230</a>&gt;] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When building a 64-bit perl, an uninitialized memory read in <code>miniperl.exe</code>, used during the build process, could lead to a 4GB <code>wperl.exe</code> being created. This has now been fixed. (Note that <code>perl.exe</code> itself was unaffected, but obviously <code>wperl.exe</code> would have been completely broken.) [perl #121471 &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=121471">https://rt.perl.org/Public/Bug/Display.html?id=121471</a>&gt;] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl can now be built with <code>gcc</code> version 4.8.1 from &lt;<a rel="nofollow" href="http://www.mingw.org">http://www.mingw.org</a>&gt;. This was previously broken due to an incorrect definition of <code>DllMain()</code> in one of perl&#8217;s source files. Earlier <code>gcc</code> versions were also affected when using version 4 of the w32api package. Versions of <code>gcc</code> available from &lt;<a rel="nofollow" href="http://mingw-w64.sourceforge.net/">http://mingw-w64.sourceforge.net/</a>&gt; were not affected. [perl #121643 &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=121643">https://rt.perl.org/Public/Bug/Display.html?id=121643</a>&gt;] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The test harness now has no failures when perl is built on a <font SIZE="-1">FAT</font> drive with the Windows <font SIZE="-1">OS</font> on an <font SIZE="-1">NTFS</font> drive. [perl #21442 &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=21442">https://rt.perl.org/Public/Bug/Display.html?id=21442</a>&gt;] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When cloning the context stack in <code>fork()</code> emulation, <code>Perl_cx_dup()</code> would crash accessing parameter information for context stack entries that included no parameters, as with <code>&quot;&amp;foo;&quot;</code>. [perl #121721 &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=121721">https://rt.perl.org/Public/Bug/Display.html?id=121721</a>&gt;] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Introduced by perl #113536 &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=113536">https://rt.perl.org/Public/Bug/Display.html?id=113536</a>&gt;, a memory leak on every call to <code>&quot;system&quot;</code> and backticks (<code>&quot; `` &quot;</code>), on most Win32 Perls starting from 5.18.0 has been fixed. The memory leak only occurred if you enabled pseudo-fork in your build of Win32 Perl, and were running that build on Server 2003 R2 or newer <font SIZE="-1">OS.</font> The leak does not appear on WinXP <font SIZE="-1">SP3.</font> [perl #121676 &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=121676">https://rt.perl.org/Public/Bug/Display.html?id=121676</a>&gt;] </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>WinCE</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> The building of <font SIZE="-1">XS</font> modules has largely been restored. Several still cannot (yet) be built but it is now possible to build Perl on WinCE with only a couple of further patches (to Socket and ExtUtils::MakeMaker), hopefully to be incorporated soon. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl can now be built in one shot with no user intervention on WinCE by running <code>&quot;nmake -f Makefile.ce all&quot;</code>. </p>
<p> Support for building with <font SIZE="-1">EVC</font> (Embedded Visual C<font SIZE="-2">++</font>) 4 has been restored. Perl can also be built using Smart Devices for Visual C<font SIZE="-2">++</font> 2005 or 2008. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The internal representation has changed for the match variables <code>$1</code>, <code>$2</code> etc., $`, $&amp;, $&#8216;, ${^PREMATCH}, ${^MATCH} and ${^POSTMATCH}. It uses slightly less memory, avoids string comparisons and numeric conversions during lookup, and uses 23 fewer lines of C. This change should not affect any external code. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Arrays now use <font SIZE="-1">NULL</font> internally to represent unused slots, instead of &amp;PL_sv_undef. &amp;PL_sv_undef is no longer treated as a special value, so av_store(av, 0, &amp;PL_sv_undef) will cause element 0 of that array to hold a read-only undefined scalar. <code>&quot;$array[0] = anything&quot;</code> will croak and <code>&quot;\$array[0]&quot;</code> will compare equal to <code>&quot;\undef&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">SV</font> returned by <code>HeSVKEY_force()</code> now correctly reflects the UTF8ness of the underlying hash key when that key is not stored as a <font SIZE="-1">SV.</font> [perl #79074] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Certain rarely used functions and macros available to <font SIZE="-1">XS</font> code are now deprecated. These are: <code>&quot;utf8_to_uvuni_buf&quot;</code> (use <code>&quot;utf8_to_uvchr_buf&quot;</code> instead), <code>&quot;valid_utf8_to_uvuni&quot;</code> (use <code>&quot;utf8_to_uvchr_buf&quot;</code> instead), <code>&quot;NATIVE_TO_NEED&quot;</code> (this did not work properly anyway), and <code>&quot;ASCII_TO_NEED&quot;</code> (this did not work properly anyway). </p>
<p> Starting in this release, almost never does application code need to distinguish between the platform&#8217;s character set and Latin1, on which the lowest 256 characters of Unicode are based. New code should not use <code>&quot;utf8n_to_uvuni&quot;</code> (use <code>&quot;utf8_to_uvchr_buf&quot;</code> instead), nor <code>&quot;uvuni_to_utf8&quot;</code> (use <code>&quot;uvchr_to_utf8&quot;</code> instead), </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Makefile shortcut targets for many rarely (or never) used testing and profiling targets have been removed, or merged into the only other Makefile target that uses them. Specifically, these targets are gone, along with documentation that referenced them or explained how to use them: </p>
<pre><code>    check.third check.utf16 check.utf8 coretest minitest.prep
    minitest.utf16 perl.config.dashg perl.config.dashpg
    perl.config.gcov perl.gcov perl.gprof perl.gprof.config
    perl.pixie perl.pixie.atom perl.pixie.config perl.pixie.irix
    perl.third perl.third.config perl.valgrind.config purecovperl
    pureperl quantperl test.deparse test.taintwarn test.third
    test.torture test.utf16 test.utf8 test_notty.deparse
    test_notty.third test_notty.valgrind test_prep.third
    test_prep.valgrind torturetest ucheck ucheck.third ucheck.utf16
    ucheck.valgrind utest utest.third utest.utf16 utest.valgrind
</code></pre>
<p> It&#8217;s still possible to run the relevant commands by ``hand&#8217;&#8216; &#8211; no underlying functionality has been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> It is now possible to keep Perl from initializing locale handling. For the most part, Perl doesn&#8217;t pay attention to locale. (See perllocale.) Nonetheless, until now, on startup, it has always initialized locale handling to the system default, just in case the program being executed ends up using locales. (This is one of the first things a locale-aware program should do, long before Perl knows if it will actually be needed or not.) This works well except when Perl is embedded in another application which wants a locale that isn&#8217;t the system default. Now, if the environment variable <code>&quot;PERL_SKIP_LOCALE_INIT&quot;</code> is set at the time Perl is started, this initialization step is skipped. Prior to this, on Windows platforms, the only workaround for this deficiency was to use a hacked-up copy of internal Perl code. Applications that need to use older Perls can discover if the embedded Perl they are using needs the workaround by testing that the C preprocessor symbol <code>&quot;HAS_SKIP_LOCALE_INIT&quot;</code> is not defined. [<font SIZE="-1">RT</font> #38193] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;BmRARE&quot;</code> and <code>&quot;BmPREVIOUS&quot;</code> have been removed. They were not used anywhere and are not part of the <font SIZE="-1">API.</font> For <font SIZE="-1">XS</font> modules, they are now #defined as 0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sv_force_normal&quot;</code>, which usually croaks on read-only values, used to allow read-only values to be modified at compile time. This has been changed to croak on read-only values regardless. This change uncovered several core bugs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl&#8217;s new copy-on-write mechanism (which is now enabled by default), allows any <code>&quot;SvPOK&quot;</code> scalar to be automatically upgraded to a copy-on-write scalar when copied. A reference count on the string buffer is stored in the string buffer itself. </p>
<p> For example: </p>
<pre><code>    $ perl -MDevel::Peek -e'$a=&quot;abc&quot;; $b = $a; Dump $a; Dump $b'
    SV = PV(0x260cd80) at 0x2620ad8
      REFCNT = 1
      FLAGS = (POK,IsCOW,pPOK)
      PV = 0x2619bc0 &quot;abc&quot;\0
      CUR = 3
      LEN = 16
      COW_REFCNT = 1
    SV = PV(0x260ce30) at 0x2620b20
      REFCNT = 1
      FLAGS = (POK,IsCOW,pPOK)
      PV = 0x2619bc0 &quot;abc&quot;\0
      CUR = 3
      LEN = 16
      COW_REFCNT = 1
</code></pre>
<p> Note that both scalars share the same <font SIZE="-1">PV</font> buffer and have a <font SIZE="-1">COW_REFCNT</font> greater than zero. </p>
<p> This means that <font SIZE="-1">XS</font> code which wishes to modify the <code>&quot;SvPVX()&quot;</code> buffer of an <font SIZE="-1">SV</font> should call <code>&quot;SvPV_force()&quot;</code> or similar first, to ensure a valid (and unshared) buffer, and to call <code>&quot;SvSETMAGIC()&quot;</code> afterwards. This in fact has always been the case (for example hash keys were already copy-on-write); this change just spreads the <font SIZE="-1">COW</font> behaviour to a wider variety of SVs. </p>
<p> One important difference is that before 5.18.0, shared hash-key scalars used to have the <code>&quot;SvREADONLY&quot;</code> flag set; this is no longer the case. </p>
<p> This new behaviour can still be disabled by running <i>Configure</i> with <code>-Accflags=-DPERL_NO_COW</code>. This option will probably be removed in Perl 5.22. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PL_sawampersand&quot;</code> is now a constant. The switch this variable provided (to enable/disable the pre-match copy depending on whether <code>$&amp;</code> had been seen) has been removed and replaced with copy-on-write, eliminating a few bugs. </p>
<p> The previous behaviour can still be enabled by running <i>Configure</i> with <code>-Accflags=-DPERL_SAWAMPERSAND</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The functions <code>&quot;my_swap&quot;</code>, <code>&quot;my_htonl&quot;</code> and <code>&quot;my_ntohl&quot;</code> have been removed. It is unclear why these functions were ever marked as <i>A</i>, part of the <font SIZE="-1">API. XS</font> code can&#8217;t call them directly, as it can&#8217;t rely on them being compiled. Unsurprisingly, no code on <font SIZE="-1">CPAN</font> references them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The signature of the <code>&quot;Perl_re_intuit_start()&quot;</code> regex function has changed; the function pointer <code>&quot;intuit&quot;</code> in the regex engine plugin structure has also changed accordingly. A new parameter, <code>&quot;strbeg&quot;</code> has been added; this has the same meaning as the same-named parameter in <code>&quot;Perl_regexec_flags&quot;</code>. Previously intuit would try to guess the start of the string from the passed <font SIZE="-1">SV</font> (if any), and would sometimes get it wrong (e.g. with an overloaded <font SIZE="-1">SV</font>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The signature of the <code>&quot;Perl_regexec_flags()&quot;</code> regex function has changed; the function pointer <code>&quot;exec&quot;</code> in the regex engine plugin structure has also changed to match. The <code>&quot;minend&quot;</code> parameter now has type <code>&quot;SSize_t&quot;</code> to better support 64-bit systems. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">XS</font> code may use various macros to change the case of a character or code point (for example <code>&quot;toLOWER_utf8()&quot;</code>). Only a couple of these were documented until now; and now they should be used in preference to calling the underlying functions. See ``Character case changing&#8217;&#8216; in perlapi. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The code dealt rather inconsistently with uids and gids. Some places assumed that they could be safely stored in UVs, others in IVs, others in ints. Four new macros are introduced: <code>SvUID()</code>, <code>sv_setuid()</code>, <code>SvGID()</code>, and <code>sv_setgid()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sv_pos_b2u_flags&quot;</code> has been added to the <font SIZE="-1">API.</font> It is similar to <code>&quot;sv_pos_b2u&quot;</code>, but supports long strings on 64-bit platforms. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PL_exit_flags&quot;</code> can now be used by perl embedders or other <font SIZE="-1">XS</font> code to have perl <code>&quot;warn&quot;</code> or <code>&quot;abort&quot;</code> on an attempted exit. [perl #52000] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compiling with <code>&quot;-Accflags=-PERL_BOOL_AS_CHAR&quot;</code> now allows C99 and C<font SIZE="-2">++</font> compilers to emulate the aliasing of <code>&quot;bool&quot;</code> to <code>&quot;char&quot;</code> that perl does for C89 compilers. [perl #120314] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;sv&quot;</code> argument in ``sv_2pv_flags&#8217;&#8216; in perlapi, ``sv_2iv_flags&#8217;&#8216; in perlapi, ``sv_2uv_flags&#8217;&#8216; in perlapi, and ``sv_2nv_flags&#8217;&#8216; in perlapi and their older wrappers sv_2pv, sv_2iv, sv_2uv, sv_2nv, is now non-NULL. Passing <font SIZE="-1">NULL</font> now will crash. When the non-NULL marker was introduced en masse in 5.9.3 the functions were marked non-NULL, but since the creation of the <font SIZE="-1">SV API</font> in 5.0 alpha 2, if <font SIZE="-1">NULL</font> was passed, the functions returned 0 or false-type values. The code that supports <code>&quot;sv&quot;</code> argument being non-NULL dates to 5.0 alpha 2 directly, and indirectly to Perl 1.0 (pre 5.0 api). The lack of documentation that the functions accepted a <font SIZE="-1">NULL</font> <code>&quot;sv&quot;</code> was corrected in 5.11.0 and between 5.11.0 and 5.19.5 the functions were marked <font SIZE="-1">NULLOK.</font> As an optimization the <font SIZE="-1">NULLOK</font> code has now been removed, and the functions became non-NULL marked again, because core getter-type macros never pass <font SIZE="-1">NULL</font> to these functions and would crash before ever passing <font SIZE="-1">NULL.</font> </p>
<p> The only way a <font SIZE="-1">NULL</font> <code>&quot;sv&quot;</code> can be passed to sv_2*v* functions is if <font SIZE="-1">XS</font> code directly calls sv_2*v*. This is unlikely as <font SIZE="-1">XS</font> code uses Sv*V* macros to get the underlying value out of the <font SIZE="-1">SV.</font> One possible situation which leads to a <font SIZE="-1">NULL</font> <code>&quot;sv&quot;</code> being passed to sv_2*v* functions, is if <font SIZE="-1">XS</font> code defines its own getter type Sv*V* macros, which check for <font SIZE="-1">NULL</font> <code>before</code> dereferencing and checking the <font SIZE="-1">SV</font>&#8216;s flags through public <font SIZE="-1">API</font> Sv*OK* macros or directly using private <font SIZE="-1">API</font> <code>&quot;SvFLAGS&quot;</code>, and if <code>&quot;sv&quot;</code> is <font SIZE="-1">NULL,</font> then calling the sv_2*v functions with a <font SIZE="-1">NULL</font> litteral or passing the <code>&quot;sv&quot;</code> containing a <font SIZE="-1">NULL</font> value. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> newATTRSUB is now a macro </p>
<p> The public <font SIZE="-1">API</font> newATTRSUB was previously a macro to the private function Perl_newATTRSUB. Function Perl_newATTRSUB has been removed. newATTRSUB is now macro to a different internal function. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes in warnings raised by <code>&quot;utf8n_to_uvchr()&quot;</code> </p>
<p> This bottom level function decodes the first character of a <font SIZE="-1">UTF-8</font> string into a code point. It is accessible to <code>&quot;XS&quot;</code> level code, but it&#8217;s discouraged from using it directly. There are higher level functions that call this that should be used instead, such as ``utf8_to_uvchr_buf&#8217;&#8216; in perlapi. For completeness though, this documents some changes to it. Now, tests for malformations are done before any tests for other potential issues. One of those issues involves code points so large that they have never appeared in any official standard (the current standard has scaled back the highest acceptable code point from earlier versions). It is possible (though not done in <font SIZE="-1">CPAN</font>) to warn and/or forbid these code points, while accepting smaller code points that are still above the legal Unicode maximum. The warning message for this now includes the code point if representable on the machine. Previously it always displayed raw bytes, which is what it still does for non-representable code points. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regexp engine changes that affect the pluggable regex engine interface </p>
<p> Many flags that used to be exposed via regexp.h and used to populate the extflags member of struct regexp have been removed. These fields were technically private to Perl&#8217;s own regexp engine and should not have been exposed there in the first place. </p>
<p> The affected flags are: </p>
<pre><code>    RXf_NOSCAN
    RXf_CANY_SEEN
    RXf_GPOS_SEEN
    RXf_GPOS_FLOAT
    RXf_ANCH_BOL
    RXf_ANCH_MBOL
    RXf_ANCH_SBOL
    RXf_ANCH_GPOS
</code></pre>
<p> As well as the follow flag masks: </p>
<pre><code>    RXf_ANCH_SINGLE
    RXf_ANCH
</code></pre>
<p> All have been renamed to PREGf_ equivalents and moved to regcomp.h. </p>
<p> The behavior previously achieved by setting one or more of the RXf_ANCH_ flags (via the RXf_ANCH mask) have now been replaced by a *single* flag bit in extflags: </p>
<pre><code>    RXf_IS_ANCHORED
</code></pre>
<p> pluggable regex engines which previously used to set these flags should now set this flag <font SIZE="-1">ALONE.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Perl core now consistently uses <code>&quot;av_tindex()&quot;</code> (``the top index of an array&#8217;&#8216;) as a more clearly-named synonym for <code>&quot;av_len()&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The obscure interpreter variable <code>&quot;PL_timesbuf&quot;</code> is expected to be removed early in the 5.21.x development series, so that Perl 5.22.0 will not provide it to <font SIZE="-1">XS</font> authors. While the variable still exists in 5.20.0, we hope that this advance warning of the deprecation will help anyone who is using that variable. </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<h3>Regular Expressions</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Fixed a small number of regexp constructions that could either fail to match or crash perl when the string being matched against was allocated above the 2GB line on 32-bit systems. [<font SIZE="-1">RT</font> #118175] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various memory leaks involving the parsing of the <code>&quot;(?[...])&quot;</code> regular expression construct have been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;(?[...])&quot;</code> now allows interpolation of precompiled patterns consisting of <code>&quot;(?[...])&quot;</code> with bracketed character classes inside (<code>&quot;$pat = qr/(?[ [a] ])/; /(?[ $pat ])/&quot;</code>). Formerly, the brackets would confuse the regular expression parser. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ``Quantifier unexpected on zero-length expression&#8217;&#8216; warning message could appear twice starting in Perl v5.10 for a regular expression also containing alternations (e.g., ``a|b&#8217;&#8216;) triggering the trie optimisation. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl v5.18 inadvertently introduced a bug whereby interpolating mixed up- and down-graded <font SIZE="-1">UTF-8</font> strings in a regex could result in malformed <font SIZE="-1">UTF-8</font> in the pattern: specifically if a downgraded character in the range <code>&quot;\x80..\xff&quot;</code> followed a <font SIZE="-1">UTF-8</font> string, e.g. </p>
<pre><code>    utf8::upgrade( my $u = &quot;\x{e5}&quot;);
    utf8::downgrade(my $d = &quot;\x{e5}&quot;);
    /$u$d/
</code></pre>
<p> [<font SIZE="-1">RT</font> #118297] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In regular expressions containing multiple code blocks, the values of <code>$1</code>, <code>$2</code>, etc., set by nested regular expression calls would leak from one block to the next. Now these variables always refer to the outer regular expression at the start of an embedded block [perl #117917]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;/$qr/p&quot;</code> was broken in Perl 5.18.0; the <code>&quot;/p&quot;</code> flag was ignored. This has been fixed. [perl #118213] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Starting in Perl 5.18.0, a construct like <code>&quot;/[#](?{})/x&quot;</code> would have its <code>&quot;#&quot;</code> incorrectly interpreted as a comment. The code block would be skipped, unparsed. This has been corrected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Starting in Perl 5.001, a regular expression like <code>&quot;/[#$a]/x&quot;</code> or <code>&quot;/[#]$a/x&quot;</code> would have its <code>&quot;#&quot;</code> incorrectly interpreted as a comment, so the variable would not interpolate. This has been corrected. [perl #45667] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl 5.18.0 inadvertently made dereferenced regular expressions (<code>&quot;${ qr// }&quot;</code>) false as booleans. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The use of <code>&quot;\G&quot;</code> in regular expressions, where it&#8217;s not at the start of the pattern, is now slightly less buggy (although it is still somewhat problematic). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Where a regular expression included code blocks (<code>&quot;/(?{...})/&quot;</code>), and where the use of constant overloading triggered a re-compilation of the code block, the second compilation didn&#8217;t see its outer lexical scope. This was a regression in Perl 5.18.0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The string position set by <code>&quot;pos&quot;</code> could shift if the string changed representation internally to or from utf8. This could happen, e.g., with references to objects with string overloading. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Taking references to the return values of two <code>&quot;pos&quot;</code> calls with the same argument, and then assigning a reference to one and <code>&quot;undef&quot;</code> to the other, could result in assertion failures or memory leaks. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Elements of @- and @+ now update correctly when they refer to non-existent captures. Previously, a referenced element (<code>&quot;$ref = \$-[1]&quot;</code>) could refer to the wrong match after subsequent matches. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The code that parses regex backrefs (or ambiguous backref/octals) such as \123 did a simple <code>atoi()</code>, which could wrap round to negative values on long digit strings and cause segmentation faults. This has now been fixed. [perl #119505] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assigning another typeglob to <code>&quot;*^R&quot;</code> no longer makes the regular expression engine crash. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;\N&quot;</code> regular expression escape, when used without the curly braces (to mean <code>&quot;[^\n]&quot;</code>), was ignoring a following <code>&quot;*&quot;</code> if followed by whitespace under /x. It had been this way since <code>&quot;\N&quot;</code> to mean <code>&quot;[^\n]&quot;</code> was introduced in 5.12.0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;s///&quot;</code>, <code>&quot;tr///&quot;</code> and <code>&quot;y///&quot;</code> now work when a wide character is used as the delimiter. [perl #120463] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some cases of unterminated (?...) sequences in regular expressions (e.g., <code>&quot;/(?&lt;/&quot;</code>) have been fixed to produce the proper error message instead of ``panic: memory wrap&#8217;&#8216;. Other cases (e.g., <code>&quot;/(?(/&quot;</code>) have yet to be fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When a reference to a reference to an overloaded object was returned from a regular expression <code>&quot;(??{...})&quot;</code> code block, an incorrect implicit dereference could take place if the inner reference had been returned by a code block previously. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A tied variable returned from <code>&quot;(??{...})&quot;</code> sees the inner values of match variables (i.e., the <code>$1</code> etc. from any matches inside the block) in its <font SIZE="-1">FETCH</font> method. This was not the case if a reference to an overloaded object was the last thing assigned to the tied variable. Instead, the match variables referred to the outer pattern during the <font SIZE="-1">FETCH</font> call. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix unexpected tainting via regexp using locale. Previously, under certain conditions, the use of character classes could cause tainting when it shouldn&#8217;t. Some character classes are locale-dependent, but before this patch, sometimes tainting was happening even for character classes that don&#8217;t depend on the locale. [perl #120675] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under certain conditions, Perl would throw an error if in a lookbehind assertion in a regexp, the assertion referred to a named subpattern, complaining the lookbehind was variable when it wasn&#8217;t. This has been fixed. [perl #120600], [perl #120618]. The current fix may be improved on in the future. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$^R</code> wasn&#8217;t available outside of the regular expression that initialized it. [perl #121070] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A large set of fixes and refactoring for <code>re_intuit_start()</code> was merged, the highlights are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Fixed a panic when compiling the regular expression <code>&quot;/\x{100}[xy]\x{100}{2}/&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a performance regression when performing a global pattern match against a <font SIZE="-1">UTF-8</font> string. [perl #120692] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed another performance issue where matching a regular expression like <code>&quot;/ab.{1,2}x/&quot;</code> against a long <font SIZE="-1">UTF-8</font> string would unnecessarily calculate byte offsets for a large portion of the string. [perl #120692] </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Fixed an alignment error when compiling regular expressions when built with <font SIZE="-1">GCC</font> on HP-UX 64-bit. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On 64-bit platforms <code>&quot;pos&quot;</code> can now be set to a value higher than 2**31-1. [perl #72766] </p>
 </dd></dl>
<h3>Perl 5 Debugger and -d</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The debugger&#8217;s <code>&quot;man&quot;</code> command been fixed. It was broken in the v5.18.0 release. The <code>&quot;man&quot;</code> command is aliased to the names <code>&quot;doc&quot;</code> and <code>&quot;perldoc&quot;</code> &#8211; all now work again. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>@_</code> is now correctly visible in the debugger, fixing a regression introduced in v5.18.0&#8217;s debugger. [<font SIZE="-1">RT</font> #118169] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under copy-on-write builds (the default as of 5.20.0) <code>&quot;${&#8216;_&lt;-e&#8217;}[0]&quot;</code> no longer gets mangled. This is the first line of input saved for the debugger&#8217;s use for one-liners [perl #118627]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On non-threaded builds, setting <code>&quot;${&quot;_&lt;filename&quot;}&quot;</code> to a reference or typeglob no longer causes <code>&quot;__FILE__&quot;</code> and some error messages to produce a corrupt string, and no longer prevents <code>&quot;#line&quot;</code> directives in string evals from providing the source lines to the debugger. Threaded builds were unaffected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Starting with Perl 5.12, line numbers were off by one if the <code>-d</code> switch was used on the #! line. Now they are correct. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;*DB::DB = sub {} if 0&quot;</code> no longer stops Perl&#8217;s debugging mode from finding <code>&quot;DB::DB&quot;</code> subs declared thereafter. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;%{&#8216;_&lt;...&#8216;}&quot;</code> hashes now set breakpoints on the corresponding <code>&quot;@{&#8216;_&lt;...&#8216;}&quot;</code> rather than whichever array <code>@DB::dbline</code> is aliased to. [perl #119799] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Call set-magic when setting <code>$DB::sub</code>. [perl #121255] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The debugger&#8217;s ``n&#8217;&#8216; command now respects lvalue subroutines and steps over them [perl #118839]. </p>
 </dd></dl>
<h3>Lexical Subroutines</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Lexical constants (<code>&quot;my sub a() { 42 }&quot;</code>) no longer crash when inlined. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Parameter prototypes attached to lexical subroutines are now respected when compiling sub calls without parentheses. Previously, the prototypes were honoured only for calls <i>with</i> parentheses. [<font SIZE="-1">RT</font> #116735] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Syntax errors in lexical subroutines in combination with calls to the same subroutines no longer cause crashes at compile time. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Deep recursion warnings no longer crash lexical subroutines. [<font SIZE="-1">RT</font> #118521] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The dtrace sub-entry probe now works with lexical subs, instead of crashing [perl #118305]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Undefining an inlinable lexical subroutine (<code>&quot;my sub foo() { 42 } undef &amp;foo&quot;</code>) would result in a crash if warnings were turned on. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An undefined lexical sub used as an inherited method no longer crashes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The presence of a lexical sub named ``<font SIZE="-1">CORE&#8217;&#8216;</font> no longer stops the <font SIZE="-1">CORE::</font> prefix from working. </p>
 </dd></dl>
<h3>Everything Else</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">OP</font> allocation code now returns correctly aligned memory in all cases for <code>&quot;struct pmop&quot;</code>. Previously it could return memory only aligned to a 4-byte boundary, which is not correct for an ithreads build with 64 bit IVs on some 32 bit platforms. Notably, this caused the build to fail completely on sparc GNU/Linux. [<font SIZE="-1">RT</font> #118055] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Evaluating large hashes in scalar context is now much faster, as the number of used chains in the hash is now cached for larger hashes. Smaller hashes continue not to store it and calculate it when needed, as this saves one <font SIZE="-1">IV.</font> That would be 1 <font SIZE="-1">IV</font> overhead for every object built from a hash. [<font SIZE="-1">RT</font> #114576] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl v5.16 inadvertently introduced a bug whereby calls to XSUBs that were not visible at compile time were treated as lvalues and could be assigned to, even when the subroutine was not an lvalue sub. This has been fixed. [<font SIZE="-1">RT</font> #117947] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In Perl v5.18.0 dualvars that had an empty string for the string part but a non-zero number for the number part starting being treated as true. In previous versions they were treated as false, the string representation taking precedeence. The old behaviour has been restored. [<font SIZE="-1">RT</font> #118159] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Since Perl v5.12, inlining of constants that override built-in keywords of the same name had countermanded <code>&quot;use subs&quot;</code>, causing subsequent mentions of the constant to use the built-in keyword instead. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The warning produced by <code>&quot;-l $handle&quot;</code> now applies to <font SIZE="-1">IO</font> refs and globs, not just to glob refs. That warning is also now UTF8-clean. [<font SIZE="-1">RT</font> #117595] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;delete local $ENV{nonexistent_env_var}&quot;</code> no longer leaks memory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sort&quot;</code> and <code>&quot;require&quot;</code> followed by a keyword prefixed with <code>&quot;CORE::&quot;</code> now treat it as a keyword, and not as a subroutine or module name. [<font SIZE="-1">RT</font> #24482] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Through certain conundrums, it is possible to cause the current package to be freed. Certain operators (<code>&quot;bless&quot;</code>, <code>&quot;reset&quot;</code>, <code>&quot;open&quot;</code>, <code>&quot;eval&quot;</code>) could not cope and would crash. They have been made more resilient. [<font SIZE="-1">RT</font> #117941] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Aliasing filehandles through glob-to-glob assignment would not update internal method caches properly if a package of the same name as the filehandle existed, resulting in filehandle method calls going to the package instead. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;./Configure -de -Dusevendorprefix&quot;</code> didn&#8217;t default. [<font SIZE="-1">RT</font> #64126] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;Statement unlikely to be reached&quot;</code> warning was listed in perldiag as an <code>&quot;exec&quot;</code>-category warning, but was enabled and disabled by the <code>&quot;syntax&quot;</code> category. On the other hand, the <code>&quot;exec&quot;</code> category controlled its fatal-ness. It is now entirely handled by the <code>&quot;exec&quot;</code> category. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ``Replacement list is longer that search list&#8217;&#8216; warning for <code>&quot;tr///&quot;</code> and <code>&quot;y///&quot;</code> no longer occurs in the presence of the <code>&quot;/c&quot;</code> flag. [<font SIZE="-1">RT</font> #118047] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Stringification of NVs are not cached so that the lexical locale controls stringification of the decimal point. [perl #108378] [perl #115800] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> There have been several fixes related to Perl&#8217;s handling of locales. perl #38193 was described above in ``Internal Changes&#8217;&#8216;. Also fixed is #118197, where the radix (decimal point) character had to be an <font SIZE="-1">ASCII</font> character (which doesn&#8217;t work for some non-Western languages); and #115808, in which <code>&quot;POSIX::setlocale()&quot;</code> on failure returned an <code>&quot;undef&quot;</code> which didn&#8217;t warn about not being defined even if those warnings were enabled. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compiling a <code>&quot;split&quot;</code> operator whose third argument is a named constant evaluating to 0 no longer causes the constant&#8217;s value to change. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A named constant used as the second argument to <code>&quot;index&quot;</code> no longer gets coerced to a string if it is a reference, regular expression, dualvar, etc. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A named constant evaluating to the undefined value used as the second argument to <code>&quot;index&quot;</code> no longer produces ``uninitialized&#8217;&#8216; warnings at compile time. It will still produce them at run time. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When a scalar was returned from a subroutine in <code>@INC</code>, the referenced scalar was magically converted into an <font SIZE="-1">IO</font> thingy, possibly resulting in ``Bizarre copy&#8217;&#8216; errors if that scalar continued to be used elsewhere. Now Perl uses an internal copy of the scalar instead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Certain uses of the <code>&quot;sort&quot;</code> operator are optimised to modify an array in place, such as <code>&quot;@a = sort @a&quot;</code>. During the sorting, the array is made read-only. If a sort block should happen to die, then the array remained read-only even outside the <code>&quot;sort&quot;</code>. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$a</code> and <code>$b</code> inside a sort block are aliased to the actual arguments to <code>&quot;sort&quot;</code>, so they can be modified through those two variables. This did not always work, e.g., for lvalue subs and <code>$#ary</code>, and probably many other operators. It works now. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The arguments to <code>&quot;sort&quot;</code> are now all in list context. If the <code>&quot;sort&quot;</code> itself were called in void or scalar context, then <i>some</i>, but not all, of the arguments used to be in void or scalar context. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Subroutine prototypes with Unicode characters above U+00FF were getting mangled during closure cloning. This would happen with subroutines closing over lexical variables declared outside, and with lexical subs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;UNIVERSAL::can&quot;</code> now treats its first argument the same way that method calls do: Typeglobs and glob references with non-empty <font SIZE="-1">IO</font> slots are treated as handles, and strings are treated as filehandles, rather than packages, if a handle with that name exists [perl #113932]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Method calls on typeglobs (e.g., <code>&quot;*ARGV-&gt;getline&quot;</code>) used to stringify the typeglob and then look it up again. Combined with changes in Perl 5.18.0, this allowed <code>&quot;*foo-&gt;bar&quot;</code> to call methods on the ``foo&#8217;&#8216; package (like <code>&quot;foo-&gt;bar&quot;</code>). In some cases it could cause the method to be called on the wrong handle. Now a typeglob argument is treated as a handle (just like <code>&quot;(\*foo)-&gt;bar&quot;</code>), or, if its <font SIZE="-1">IO</font> slot is empty, an error is raised. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assigning a vstring to a tied variable or to a subroutine argument aliased to a nonexistent hash or array element now works, without flattening the vstring into a regular string. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pos&quot;</code>, <code>&quot;tie&quot;</code>, <code>&quot;tied&quot;</code> and <code>&quot;untie&quot;</code> did not work properly on subroutine arguments aliased to nonexistent hash and array elements [perl #77814, #27010]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;=&gt;&quot;</code> fat arrow operator can now quote built-in keywords even if it occurs on the next line, making it consistent with how it treats other barewords. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Autovivifying a subroutine stub via <code>&quot;\&amp;$glob&quot;</code> started causing crashes in Perl 5.18.0 if the <code>$glob</code> was merely a copy of a real glob, i.e., a scalar that had had a glob assigned to it. This has been fixed. [perl #119051] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl used to leak an implementation detail when it came to referencing the return values of certain operators. <code>&quot;for ($a+$b) { warn \$_; warn \$_ }&quot;</code> used to display two different memory addresses, because the <code>&quot;\&quot;</code> operator was copying the variable. Under threaded builds, it would also happen for constants (<code>&quot;<a href="/docs/linux/man/1-for/">for</a>(1) { ... }&quot;</code>). This has been fixed. [perl #21979, #78194, #89188, #109746, #114838, #115388] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The range operator <code>&quot;..&quot;</code> was returning the same modifiable scalars with each call, unless it was the only thing in a <code>&quot;foreach&quot;</code> loop header. This meant that changes to values within the list returned would be visible the next time the operator was executed. [perl #3105] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Constant folding and subroutine inlining no longer cause operations that would normally return new modifiable scalars to return read-only values instead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Closures of the form <code>&quot;sub () { $some_variable }&quot;</code> are no longer inlined, causing changes to the variable to be ignored by callers of the subroutine. [perl #79908] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Return values of certain operators such as <code>&quot;ref&quot;</code> would sometimes be shared between recursive calls to the same subroutine, causing the inner call to modify the value returned by <code>&quot;ref&quot;</code> in the outer call. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;__PACKAGE__&quot;</code> and constants returning a package name or hash key are now consistently read-only. In various previous Perl releases, they have become mutable under certain circumstances. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Enabling ``used once&#8217;&#8216; warnings no longer causes crashes on stash circularities created at compile time (<code>&quot;*Foo::Bar::Foo:: = *Foo::&quot;</code>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Undef constants used in hash keys (<code>&quot;use constant u =&gt; undef; $h{+u}&quot;</code>) no longer produce ``uninitialized&#8217;&#8216; warnings at compile time. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Modifying a substitution target inside the substitution replacement no longer causes crashes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The first statement inside a string eval used to use the wrong pragma setting sometimes during constant folding. <code>&quot;eval &#8216;uc chr 0xe0&#8217;&quot;</code> would randomly choose between Unicode, byte, and locale semantics. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The handling of return values of <code>@INC</code> filters (subroutines returned by subroutines in <code>@INC</code>) has been fixed in various ways. Previously tied variables were mishandled, and setting <code>$_</code> to a reference or typeglob could result in crashes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;SvPVbyte&quot;</code> <font SIZE="-1">XS</font> function has been fixed to work with tied scalars returning something other than a string. It used to return utf8 in those cases where <code>&quot;SvPV&quot;</code> would. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl 5.18.0 inadvertently made <code>&quot;--&quot;</code> and <code>&quot;++&quot;</code> crash on dereferenced regular expressions, and stopped <code>&quot;++&quot;</code> from flattening vstrings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;bless&quot;</code> no longer dies with ``Can&#8217;t bless non-reference value&#8217;&#8216; if its first argument is a tied reference. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;reset&quot;</code> with an argument no longer skips copy-on-write scalars, regular expressions, typeglob copies, and vstrings. Also, when encountering those or read-only values, it no longer skips any array or hash with the same name. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;reset&quot;</code> with an argument now skips scalars aliased to typeglobs (<code>&quot;for $z (*foo) { reset &quot;z&quot; }&quot;</code>). Previously it would corrupt memory or crash. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;ucfirst&quot;</code> and <code>&quot;lcfirst&quot;</code> were not respecting the bytes pragma. This was a regression from Perl 5.12. [perl #117355] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes to <code>&quot;UNIVERSAL::DESTROY&quot;</code> now update <font SIZE="-1">DESTROY</font> caches in all classes, instead of causing classes that have already had objects destroyed to continue using the old sub. This was a regression in Perl 5.18. [perl #114864] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> All known false-positive occurrences of the deprecation warning ``Useless use of &#8216;\&#8216;; doesn&#8217;t escape metacharacter &#8216;%c&#8217;&#8216;&#8216;, added in Perl 5.18.0, have been removed. [perl #119101] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The value of $^E is now saved across signal handlers on Windows. [perl #85104] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A lexical filehandle (as in <code>&quot;open my $fh...&quot;</code>) is usually given a name based on the current package and the name of the variable, e.g. ``main::$fh&#8217;&#8216;. Under recursion, the filehandle was losing the ``$fh&#8217;&#8216; part of the name. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Uninitialized values returned by XSUBs are no longer exempt from uninitialized warnings. [perl #118693] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;elsif (&quot;&quot;)&quot;</code> no longer erroneously produces a warning about void context. [perl #118753] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Passing <code>&quot;undef&quot;</code> to a subroutine now causes <code>@_</code> to contain the same read-only undefined scalar that <code>&quot;undef&quot;</code> returns. Furthermore, <code>&quot;exists $_[0]&quot;</code> will now return true if <code>&quot;undef&quot;</code> was the first argument. [perl #7508, #109726] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Passing a non-existent array element to a subroutine does not usually autovivify it unless the subroutine modifies its argument. This did not work correctly with negative indices and with non-existent elements within the array. The element would be vivified immediately. The delayed vivification has been extended to work with those. [perl #118691] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assigning references or globs to the scalar returned by $#foo after the <code>@foo</code> array has been freed no longer causes assertion failures on debugging builds and memory leaks on regular builds. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On 64-bit platforms, large ranges like 1..1000000000000 no longer crash, but eat up all your memory instead. [perl #119161] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;__DATA__&quot;</code> now puts the <code>&quot;DATA&quot;</code> handle in the right package, even if the current package has been renamed through glob assignment. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When <code>&quot;die&quot;</code>, <code>&quot;last&quot;</code>, <code>&quot;next&quot;</code>, <code>&quot;redo&quot;</code>, <code>&quot;goto&quot;</code> and <code>&quot;exit&quot;</code> unwind the scope, it is possible for <code>&quot;DESTROY&quot;</code> recursively to call a subroutine or format that is currently being exited. It that case, sometimes the lexical variables inside the sub would start out having values from the outer call, instead of being undefined as they should. This has been fixed. [perl #119311] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ${^MPEN} is no longer treated as a synonym for ${^MATCH}. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now tries a little harder to return the correct line number in <code>&quot;(caller)[2]&quot;</code>. [perl #115768] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Line numbers inside multiline quote-like operators are now reported correctly. [perl #3643] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;#line&quot;</code> directives inside code embedded in quote-like operators are now respected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Line numbers are now correct inside the second here-doc when two here-doc markers occur on the same line. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An optimization in Perl 5.18 made incorrect assumptions causing a bad interaction with the Devel::CallParser <font SIZE="-1">CPAN</font> module. If the module was loaded then lexical variables declared in separate statements following a <code>&quot;my(...)&quot;</code> list might fail to be cleared on scope exit. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&amp;xsub</code> and <code>&quot;goto &amp;xsub&quot;</code> calls now allow the called subroutine to autovivify elements of <code>@_</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&amp;xsub</code> and <code>&quot;goto &amp;xsub&quot;</code> no longer crash if *_ has been undefined and has no <font SIZE="-1">ARRAY</font> entry (i.e. <code>@_</code> does not exist). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&amp;xsub</code> and <code>&quot;goto &amp;xsub&quot;</code> now work with tied <code>@_</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Overlong identifiers no longer cause a buffer overflow (and a crash). They started doing so in Perl 5.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The warning ``Scalar value <code>@hash</code>{foo} better written as <code>$hash</code>{foo}&#8216;&#8216; now produces far fewer false positives. In particular, <code>@hash{+function_returning_a_list}</code> and <code>@hash{ qw &quot;foo bar baz&quot; }</code> no longer warn. The same applies to array slices. [perl #28380, #114024] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;$! = EINVAL; waitpid(0, WNOHANG);&quot;</code> no longer goes into an internal infinite loop. [perl #85228] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A possible segmentation fault in filehandle duplication has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A subroutine in <code>@INC</code> can return a reference to a scalar containing the initial contents of the file. However, that scalar was freed prematurely if not referenced elsewhere, giving random results. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;last&quot;</code> no longer returns values that the same statement has accumulated so far, fixing amongst other things the long-standing bug that <code>&quot;push @a, last&quot;</code> would try to return the <code>@a</code>, copying it like a scalar in the process and resulting in the error, ``Bizarre copy of <font SIZE="-1">ARRAY</font> in last.&#8216;&#8216; [perl #3112] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In some cases, closing file handles opened to pipe to or from a process, which had been duplicated into a standard handle, would call perl&#8217;s internal waitpid wrapper with a pid of zero. With the fix for [perl #85228] this zero pid was passed to <code>&quot;waitpid&quot;</code>, possibly blocking the process. This wait for process zero no longer occurs. [perl #119893] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;select&quot;</code> used to ignore magic on the fourth (timeout) argument, leading to effects such as <code>&quot;select&quot;</code> blocking indefinitely rather than the expected sleep time. This has now been fixed. [perl #120102] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The class name in <code>&quot;for my class $foo&quot;</code> is now parsed correctly. In the case of the second character of the class name being followed by a digit (e.g. &#8216;a1b&#8217;) this used to give the error ``Missing $ on loop variable&#8217;&#8216;. [perl #120112] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl 5.18.0 accidentally disallowed <code>&quot;-bareword&quot;</code> under <code>&quot;use strict&quot;</code> and <code>&quot;use integer&quot;</code>. This has been fixed. [perl #120288] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-a&quot;</code> at the start of a line (or a hyphen with any single letter that is not a filetest operator) no longer produces an erroneous &#8216;Use of ``-a&#8217;&#8216; without parentheses is ambiguous&#8217; warning. [perl #120288] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Lvalue context is now properly propagated into bare blocks and <code>&quot;if&quot;</code> and <code>&quot;else&quot;</code> blocks in lvalue subroutines. Previously, arrays and hashes would sometimes incorrectly be flattened when returned in lvalue list context, or ``Bizarre copy&#8217;&#8216; errors could occur. [perl #119797] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Lvalue context is now propagated to the branches of <code>&quot;||&quot;</code> and <code>&quot;&amp;&amp;&quot;</code> (and their alphabetic equivalents, <code>&quot;or&quot;</code> and <code>&quot;and&quot;</code>). This means <code>&quot;foreach (pos $x || pos $y) {...}&quot;</code> now allows <code>&quot;pos&quot;</code> to be modified through <code>$_</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;stat&quot;</code> and <code>&quot;readline&quot;</code> remember the last handle used; the former for the special <code>&quot;_&quot;</code> filehandle, the latter for <code>&quot;${^LAST_FH}&quot;</code>. <code>&quot;eval &quot;*foo if 0&quot;&quot;</code> where *foo was the last handle passed to <code>&quot;stat&quot;</code> or <code>&quot;readline&quot;</code> could cause that handle to be forgotten if the handle were not opened yet. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various cases of <code>&quot;delete $::{a}&quot;</code>, <code>&quot;delete $::{ENV}&quot;</code> etc. causing a crash have been fixed. [perl #54044] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Setting <code>$!</code> to <font SIZE="-1">EACCESS</font> before calling <code>&quot;require&quot;</code> could affect <code>&quot;require&quot;</code>&#8216;s behaviour. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ``Can&#8217;t use \1 to mean <code>$1</code> in expression&#8217;&#8216; warning message now only occurs on the right-hand (replacement) part of a substitution. Formerly it could happen in code embedded in the left-hand side, or in any other quote-like operator. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Blessing into a reference (<code>&quot;bless $thisref, $thatref&quot;</code>) has long been disallowed, but magical scalars for the second like <code>$/</code> and those tied were exempt. They no longer are. [perl #119809] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Blessing into a reference was accidentally allowed in 5.18 if the class argument were a blessed reference with stale method caches (i.e., whose class had had subs defined since the last method call). They are disallowed once more, as in 5.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;$x-&gt;{key}&quot;</code> where <code>$x</code> was declared as <code>&quot;my Class $x&quot;</code> no longer crashes if a Class::FIELDS subroutine stub has been declared. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>@$obj{&#8216;key&#8217;}</code> and <code>&quot;${$obj}{key}&quot;</code> used to be exempt from compile-time field checking (``No such class field&#8217;&#8216;; see fields) but no longer are. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A nonexistent array element with a large index passed to a subroutine that ties the array and then tries to access the element no longer results in a crash. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Declaring a subroutine stub named <font SIZE="-1">NEGATIVE_INDICES</font> no longer makes negative array indices crash when the current package is a tied array class. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Declaring a <code>&quot;require&quot;</code>, <code>&quot;glob&quot;</code>, or <code>&quot;do&quot;</code> subroutine stub in the <font SIZE="-1">CORE::GLOBAL::</font> package no longer makes compilation of calls to the corresponding functions crash. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Aliasing <font SIZE="-1">CORE::GLOBAL::</font> functions to constants stopped working in Perl 5.10 but has now been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When <code>&quot;`...`&quot;</code> or <code>&quot;qx/.../&quot;</code> calls a <code>&quot;readpipe&quot;</code> override, double-quotish interpolation now happens, as is the case when there is no override. Previously, the presence of an override would make these quote-like operators act like <code>&quot;q{}&quot;</code>, suppressing interpolation. [perl #115330] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;&lt;&lt;&lt;`...`&quot;</code> here-docs (with backticks as the delimiters) now call <code>&quot;readpipe&quot;</code> overrides. [perl #119827] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;&amp;CORE::exit()&quot;</code> and <code>&quot;&amp;CORE::die()&quot;</code> now respect vmsish hints. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Undefining a glob that triggers a <font SIZE="-1">DESTROY</font> method that undefines the same glob is now safe. It used to produce ``Attempt to free unreferenced glob pointer&#8217;&#8216; warnings and leak memory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If subroutine redefinition (<code>&quot;eval &#8216;sub foo{}&#8216;&quot;</code> or <code>&quot;newXS&quot;</code> for <font SIZE="-1">XS</font> code) triggers a <font SIZE="-1">DESTROY</font> method on the sub that is being redefined, and that method assigns a subroutine to the same slot (<code>&quot;*foo = sub {}&quot;</code>), <code>$_[0]</code> is no longer left pointing to a freed scalar. Now <font SIZE="-1">DESTROY</font> is delayed until the new subroutine has been installed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On Windows, perl no longer calls <code>CloseHandle()</code> on a socket handle. This makes debugging easier on Windows by removing certain irrelevant bad handle exceptions. It also fixes a race condition that made socket functions randomly fail in a Perl process with multiple <font SIZE="-1">OS</font> threads, and possible test failures in <i>dist/IO/t/cachepropagate-tcp.t</i>. [perl #120091/118059] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Formats involving <font SIZE="-1">UTF-8</font> encoded strings, or strange vars like ties, overloads, or stringified refs (and in recent perls, pure <font SIZE="-1">NOK</font> vars) would generally do the wrong thing in formats when the var is treated as a string and repeatedly chopped, as in <code>&quot;^&lt;&lt;&lt;~~&quot;</code> and similar. This has now been resolved. [perl #33832/45325/113868/119847/119849/119851] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;semctl(..., SETVAL, ...)&quot;</code> would set the semaphore to the top 32-bits of the supplied integer instead of the bottom 32-bits on 64-bit big-endian systems. [perl #120635] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;readdir()&quot;</code> now only sets <code>$!</code> on error. <code>$!</code> is no longer set to <code>&quot;EBADF&quot;</code> when then terminating <code>&quot;undef&quot;</code> is read from the directory unless the system call sets <code>$!</code>. [perl #118651] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&amp;CORE::glob</code> no longer causes an intermittent crash due to perl&#8217;s stack getting corrupted. [perl #119993] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;open&quot;</code> with layers that load modules (e.g., ``&lt;:encoding(utf8)&#8216;&#8216;) no longer runs the risk of crashing due to stack corruption. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl 5.18 broke autoloading via <code>&quot;-&gt;SUPER::foo&quot;</code> method calls by looking up <font SIZE="-1">AUTOLOAD</font> from the current package rather than the current package&#8217;s superclass. This has been fixed. [perl #120694] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A longstanding bug causing <code>&quot;do {} until CONSTANT&quot;</code>, where the constant holds a true value, to read unallocated memory has been resolved. This would usually happen after a syntax error. In past versions of Perl it has crashed intermittently. [perl #72406] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix HP-UX <code>$!</code> failure. HP-UX <code>strerror()</code> returns an empty string for an unknown error code. This caused an assertion to fail under <font SIZE="-1">DEBUGGING</font> builds. Now instead, the returned string for <code>&quot;$!&quot;</code> contains text indicating the code is for an unknown error. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Individually-tied elements of <code>@INC</code> (as in <code>&quot;tie $INC[0]...&quot;</code>) are now handled correctly. Formerly, whether a sub returned by such a tied element would be treated as a sub depended on whether a <font SIZE="-1">FETCH</font> had occurred previously. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;getc&quot;</code> on a byte-sized handle after the same <code>&quot;getc&quot;</code> operator had been used on a utf8 handle used to treat the bytes as utf8, resulting in erratic behavior (e.g., malformed <font SIZE="-1">UTF-8</font> warnings). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An initial <code>&quot;{&quot;</code> at the beginning of a format argument line was always interpreted as the beginning of a block prior to v5.18. In Perl v5.18, it started being treated as an ambiguous token. The parser would guess whether it was supposed to be an anonymous hash constructor or a block based on the contents. Now the previous behavious has been restored. [perl #119973] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In Perl v5.18 <code>&quot;undef *_; goto &amp;sub&quot;</code> and <code>&quot;local *_; goto &amp;sub&quot;</code> started crashing. This has been fixed. [perl #119949] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Backticks (<code>&quot; `` &quot;</code> or <code>&quot; qx// &quot;</code>) combined with multiple threads on Win32 could result in output sent to stdout on one thread being captured by backticks of an external command in another thread. </p>
<p> This could occur for pseudo-forked processes too, as Win32&#8217;s pseudo-fork is implemented in terms of threads. [perl #77672] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;open $fh, &quot;&gt;+&quot;, undef&quot;</code> no longer leaks memory when <font SIZE="-1">TMPDIR</font> is set but points to a directory a temporary file cannot be created in. [perl #120951] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot; for ( $h{k} || &#8216;&#8216; ) &quot;</code> no longer auto-vivifies <code>$h{k}</code>. [perl #120374] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On Windows machines, Perl now emulates the <font SIZE="-1">POSIX</font> use of the environment for locale initialization. Previously, the environment was ignored. See ``<font SIZE="-1">ENVIRONMENT&#8217;&#8216;</font> in perllocale. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a crash when destroying a self-referencing <font SIZE="-1">GLOB.</font> [perl #121242] </p>
 </dd></dl>
<h2>Known Problems</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> IO::Socket is known to fail tests on <font SIZE="-1">AIX 5.3.</font> There is a patch &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=120835">https://rt.perl.org/Ticket/Display.html?id=120835</a>&gt; in the request tracker, #120835, which may be applied to future releases. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The following modules are known to have test failures with this version of Perl. Patches have been submitted, so there will hopefully be new releases soon: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Data::Structure::Util version 0.15 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> HTML::StripScripts version 1.05 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> List::Gather version 0.08. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>Obituary</h2>
<p> Diana Rosa, 27, of Rio de Janeiro, went to her long rest on May 10, 2014, along with the plush camel she kept hanging on her computer screen all the time. She was a passionate Perl hacker who loved the language and its community, and who never missed a Rio.pm event. She was a true artist, an enthusiast about writing code, singing arias and graffiting walls. We&#8217;ll never forget you. </p>
<p> Greg McCarroll died on August 28, 2013. </p>
<p> Greg was well known for many good reasons. He was one of the organisers of the first YAPC::Europe, which concluded with an unscheduled auction where he frantically tried to raise extra money to avoid the conference making a loss. It was Greg who mistakenly arrived for a london.pm meeting a week late; some years later he was the one who sold the choice of official meeting date at a YAPC::Europe auction, and eventually as glorious leader of london.pm he got to inherit the irreverent confusion that he had created. </p>
<p> Always helpful, friendly and cheerfully optimistic, you will be missed, but never forgotten.  </p>
<h2>Acknowledgements</h2>
<p> Perl 5.20.0 represents approximately 12 months of development since Perl 5.18.0 and contains approximately 470,000 lines of changes across 2,900 files from 124 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 280,000 lines of changes to 1,800 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.20.0: </p>
<p> Aaron Crane, Abhijit Menon-Sen, Abigail, Abir Viqar, Alan Haggai Alavi, Alan Hourihane, Alexander Voronov, Alexandr Ciornii, Andy Dougherty, Anno Siegel, Aristotle Pagaltzis, Arthur Axel &#8216;fREW&#8217; Schmidt, Brad Gilbert, Brendan Byrd, Brian Childs, Brian Fraser, Brian Gottreu, Chris &#8216;BinGOs&#8217; Williams, Christian Millour, Colin Kuskie, Craig A. Berry, Dabrien &#8216;Dabe&#8217; Murphy, Dagfinn Ilmari Mannsåker, Daniel Dragan, Darin McBride, David Golden, David Leadbeater, David Mitchell, David Nicol, David Steinbrunner, Dennis Kaarsemaker, Dominic Hargreaves, Ed Avis, Eric Brine, Evan Zacks, Father Chrysostomos, Florian Ragwitz, François Perrad, Gavin Shelley, Gideon Israel Dsouza, Gisle Aas, Graham Knop, H.Merijn Brand, Hauke D, Heiko Eissfeldt, Hiroo Hayashi, Hojung Youn, James E Keenan, Jarkko Hietaniemi, Jerry D. Hedden, Jess Robinson, Jesse Luehrs, Johan Vromans, John Gardiner Myers, John Goodyear, John P. Linderman, John Peacock, kafka, Kang-min Liu, Karen Etheridge, Karl Williamson, Keedi Kim, Kent Fredric, kevin dawson, Kevin Falcone, Kevin Ryde, Leon Timmermans, Lukas Mai, Marc Simpson, Marcel Grünauer, Marco Peereboom, Marcus Holland-Moritz, Mark Jason Dominus, Martin McGrath, Matthew Horsfall, Max Maischein, Mike Doherty, Moritz Lenz, Nathan Glenn, Nathan Trapuzzano, Neil Bowers, Neil Williams, Nicholas Clark, Niels Thykier, Niko Tyni, Olivier Mengué, Owain G. Ainsworth, Paul Green, Paul Johnson, Peter John Acklam, Peter Martini, Peter Rabbitson, Petr Písař, Philip Boulain, Philip Guenther, Piotr Roszatycki, Rafael Garcia-Suarez, Reini Urban, Reuben Thomas, Ricardo Signes, Ruslan Zakirov, Sergey Alekseev, Shirakata Kentaro, Shlomi Fish, Slaven Rezic, Smylers, Steffen Müller, Steve Hay, Sullivan Beck, Thomas Sibley, Tobias Leich, Toby Inkster, Tokuhiro Matsuno, Tom Christiansen, Tom Hukins, Tony Cook, Victor Efimov, Viktor Turskyi, Vladimir Timofeev, <font SIZE="-1">YAMASHINA</font> Hio, Yves Orton, Zefram, Zsbán Ambrus, Ævar Arnfjörð Bjarmason. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
