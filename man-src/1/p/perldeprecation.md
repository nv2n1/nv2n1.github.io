---
title: "perldeprecation(1)"
name: "perldeprecation"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldeprecation/"
description: "perldeprecation – list Perl deprecations"
---

<h2 class="name">NAME</h2>
<p> perldeprecation &#8211; list Perl deprecations </p>
<h2>DESCRIPTION</h2>
<p> The purpose of this document is to document what has been deprecated in Perl, and by which version the deprecated feature will disappear, or, for already removed features, when it was removed. </p>
<p> This document will try to discuss what alternatives for the deprecated features are available. </p>
<p> The deprecated features will be grouped by the version of Perl in which they will be removed.</p>
<h3>Perl 5.32</h3>
<p> <i>Constants from lexical variables potentially modified elsewhere</i> </p>
<p> You wrote something like </p>
<pre>
    my $var;
    $sub = sub () { $var };
</pre>
<p> but <tt>$var</tt> is referenced elsewhere and could be modified after the <tt>&quot;sub&quot;</tt> expression is evaluated. Either it is explicitly modified elsewhere (<tt>&quot;$var = 3&quot;</tt>) or it is passed to a subroutine or to an operator like <tt>&quot;printf&quot;</tt> or <tt>&quot;map&quot;</tt>, which may or may not modify the variable. </p>
<p> Traditionally, Perl has captured the value of the variable at that point and turned the subroutine into a constant eligible for inlining. In those cases where the variable can be modified elsewhere, this breaks the behavior of closures, in which the subroutine captures the variable itself, rather than its value, so future changes to the variable are reflected in the subroutine&#8217;s return value. </p>
<p> If you intended for the subroutine to be eligible for inlining, then make sure the variable is not referenced elsewhere, possibly by copying it: </p>
<pre>
    my $var2 = $var;
    $sub = sub () { $var2 };
</pre>
<p> If you do want this subroutine to be a closure that reflects future changes to the variable that it closes over, add an explicit <tt>&quot;return&quot;</tt>: </p>
<pre><code>
my $var;
$sub = sub(){return $var};
</code></pre>
<p> This usage has been deprecated, and will no longer be allowed in Perl 5.32. </p>
<p> <i>Use of strings with code points over 0xFF as arguments to </i>&quot;vec&quot;<i></i> </p>
<p> <tt>&quot;vec&quot;</tt> views its string argument as a sequence of bits. A string containing a code point over 0xFF is nonsensical. This usage is deprecated in Perl 5.28, and will be removed in Perl 5.32. </p>
<p> <i>Use of code points over 0xFF in string bitwise operators</i> </p>
<p> The string bitwise operators, <tt>&quot;&amp;&quot;</tt>, <tt>&quot;|&quot;</tt>, <tt>&quot;^&quot;</tt>, and <tt>&quot;~&quot;</tt>, treat their operands as strings of bytes. As such, values above 0xFF are nonsensical. Some instances of these have been deprecated since Perl 5.24, and were made fatal in 5.28, but it turns out that in cases where the wide characters did not affect the end result, no deprecation notice was raised, and so remain legal. Now, all occurrences either are fatal or raise a deprecation warning, so that the remaining legal occurrences will be fatal in 5.32. </p>
<p> An example of this is </p>
<pre>
 &quot;&quot; &amp; &quot;\x{100}&quot;
</code></pre>
<p> The wide character is not used in the <code>&quot;&amp;&quot;</code> operation because the left operand is shorter. This now warns anyway. </p>
<p> <i></i>hostname()<i> doesn&#8217;t accept any arguments</i> </p>
<p> The function <code>&quot;hostname()&quot;</code> in the Sys::Hostname module has always been documented to be called with no arguments. Historically it has not enforced this, and has actually accepted and ignored any arguments. As a result, some users have got the mistaken impression that an argument does something useful. To avoid these bugs, the function is being made strict. Passing arguments was deprecated in Perl 5.28, and will become fatal in Perl 5.32. </p>
<p> <i>Unescaped left braces in regular expressions</i> </p>
<p> The simple rule to remember, if you want to match a literal <code>&quot;{&quot;</code> character (U+007B <code>&quot;LEFT CURLY BRACKET&quot;</code>) in a regular expression pattern, is to escape each literal instance of it in some way. Generally easiest is to precede it with a backslash, like <code>&quot;\{&quot;</code> or enclose it in square brackets (<code>&quot;[{]&quot;</code>). If the pattern delimiters are also braces, any matching right brace (<code>&quot;}&quot;</code>) should also be escaped to avoid confusing the parser, for example, </p>
<pre><code> qr{abc\{def\}ghi}
</code></pre>
<p> Forcing literal <code>&quot;{&quot;</code> characters to be escaped will enable the Perl language to be extended in various ways in future releases. To avoid needlessly breaking existing code, the restriction is is not enforced in contexts where there are unlikely to ever be extensions that could conflict with the use there of <code>&quot;{&quot;</code> as a literal. A non-deprecation warning that the left brace is being taken literally is raised in contexts where there could be confusion about it. </p>
<p> Literal uses of <code>&quot;{&quot;</code> were deprecated in Perl 5.20, and some uses of it started to give deprecation warnings since. These cases were made fatal in Perl 5.26. Due to an oversight, not all cases of a use of a literal <code>&quot;{&quot;</code> got a deprecation warning. Some cases started warning in Perl 5.26, and were made fatal in Perl 5.30. Other cases started in Perl 5.28, and will be made fatal in 5.32. </p>
<p> <i>In </i><font SIZE="-1"><i>XS</i></font><i> code, use of various macros dealing with </i><font SIZE="-1"><i>UTF-8.</i></font><i></i> </p>
<p> These macros will require an extra parameter in Perl 5.32: <code>&quot;isALPHANUMERIC_utf8&quot;</code>, <code>&quot;isASCII_utf8&quot;</code>, <code>&quot;isBLANK_utf8&quot;</code>, <code>&quot;isCNTRL_utf8&quot;</code>, <code>&quot;isDIGIT_utf8&quot;</code>, <code>&quot;isIDFIRST_utf8&quot;</code>, <code>&quot;isPSXSPC_utf8&quot;</code>, <code>&quot;isSPACE_utf8&quot;</code>, <code>&quot;isVERTWS_utf8&quot;</code>, <code>&quot;isWORDCHAR_utf8&quot;</code>, <code>&quot;isXDIGIT_utf8&quot;</code>, <code>&quot;isALPHANUMERIC_LC_utf8&quot;</code>, <code>&quot;isALPHA_LC_utf8&quot;</code>, <code>&quot;isASCII_LC_utf8&quot;</code>, <code>&quot;isBLANK_LC_utf8&quot;</code>, <code>&quot;isCNTRL_LC_utf8&quot;</code>, <code>&quot;isDIGIT_LC_utf8&quot;</code>, <code>&quot;isGRAPH_LC_utf8&quot;</code>, <code>&quot;isIDCONT_LC_utf8&quot;</code>, <code>&quot;isIDFIRST_LC_utf8&quot;</code>, <code>&quot;isLOWER_LC_utf8&quot;</code>, <code>&quot;isPRINT_LC_utf8&quot;</code>, <code>&quot;isPSXSPC_LC_utf8&quot;</code>, <code>&quot;isPUNCT_LC_utf8&quot;</code>, <code>&quot;isSPACE_LC_utf8&quot;</code>, <code>&quot;isUPPER_LC_utf8&quot;</code>, <code>&quot;isWORDCHAR_LC_utf8&quot;</code>, <code>&quot;isXDIGIT_LC_utf8&quot;</code>, <code>&quot;toFOLD_utf8&quot;</code>, <code>&quot;toLOWER_utf8&quot;</code>, <code>&quot;toTITLE_utf8&quot;</code>, and <code>&quot;toUPPER_utf8&quot;</code>. </p>
<p> There is now a macro that corresponds to each one of these, simply by appending <code>&quot;_safe&quot;</code> to the name. It takes the extra parameter. For example, <code>&quot;isDIGIT_utf8_safe&quot;</code> corresponds to <code>&quot;isDIGIT_utf8&quot;</code>, but takes the extra parameter, and its use doesn&#8217;t generate a deprecation warning. All are documented in ``Character case changing&#8217;&#8216; in perlapi and ``Character classification&#8217;&#8216; in perlapi. </p>
<p> You can change to use these versions at any time, or, if you can live with the deprecation messages, wait until 5.32 and add the parameter to the existing calls, without changing the names. </p>
<p> This change was originally scheduled for 5.30, but was delayed.  </p>
<h3>Perl 5.30</h3>
<p> <i></i>$*<i> is no longer supported</i> </p>
<p> Before Perl 5.10, setting <code>$*</code> to a true value globally enabled multi-line matching within a string. This relique from the past lost its special meaning in 5.10. Use of this variable will be a fatal error in Perl 5.30, freeing the variable up for a future special meaning. </p>
<p> To enable multiline matching one should use the <code>&quot;/m&quot;</code> regexp modifier (possibly in combination with <code>&quot;/s&quot;</code>). This can be set on a per match bases, or can be enabled per lexical scope (including a whole file) with <code>&quot;use re &#8216;/m&#8217;&quot;</code>. </p>
<p> <i></i>$#<i> is no longer supported</i> </p>
<p> This variable used to have a special meaning --- it could be used to control how numbers were formatted when printed. This seldom used functionality was removed in Perl 5.10. In order to free up the variable for a future special meaning, its use will be a fatal error in Perl 5.30. </p>
<p> To specify how numbers are formatted when printed, one is advised to use <code>&quot;printf&quot;</code> or <code>&quot;sprintf&quot;</code> instead. </p>
<p> <i>Assigning non-zero to </i>$[<i> is fatal</i> </p>
<p> This variable (and the corresponding <code>&quot;array_base&quot;</code> feature and arybase module) allowed changing the base for array and string indexing operations. </p>
<p> Setting this to a non-zero value has been deprecated since Perl 5.12 and throws a fatal error as of Perl 5.30. </p>
<p> <i></i>&quot;File::Glob::glob()&quot;<i> will disappear</i> </p>
<p> <code>&quot;File::Glob&quot;</code> has a function called <code>&quot;glob&quot;</code>, which just calls <code>&quot;bsd_glob&quot;</code>. However, its prototype is different from the prototype of <code>&quot;CORE::glob&quot;</code>, and hence, <code>&quot;File::Glob::glob&quot;</code> should not be used. </p>
<p> <code>&quot;File::Glob::glob()&quot;</code> was deprecated in Perl 5.8. A deprecation message was issued from Perl 5.26 onwards, and the function will disappear in Perl 5.30. </p>
<p> Code using <code>&quot;File::Glob::glob()&quot;</code> should call <code>&quot;File::Glob::bsd_glob()&quot;</code> instead. </p>
<p> <i>Unescaped left braces in regular expressions (for 5.30)</i> </p>
<p> See ``Unescaped left braces in regular expressions&#8217;&#8216; above. </p>
<p> <i>Unqualified </i>&quot;dump()&quot;<i></i> </p>
<p> Use of <code>&quot;dump()&quot;</code> instead of <code>&quot;CORE::dump()&quot;</code> was deprecated in Perl 5.8, and an unqualified <code>&quot;dump()&quot;</code> will no longer be available in Perl 5.30. </p>
<p> See ``dump&#8217;&#8216; in perlfunc. </p>
<p> <i>Using </i>my()<i> in false conditional.</i> </p>
<p> There has been a long-standing bug in Perl that causes a lexical variable not to be cleared at scope exit when its declaration includes a false conditional. Some people have exploited this bug to achieve a kind of static variable. Since we intend to fix this bug, we don&#8217;t want people relying on this behavior. </p>
<p> Instead, it&#8217;s recommended one uses <code>&quot;state&quot;</code> variables to achieve the same effect: </p>
<pre><code>    use 5.10.0;
    sub count {state $counter; return ++ $counter}
    say count (); # Prints 1
    say count (); # Prints 2
</code></pre>
<p> <code>&quot;state&quot;</code> variables were introduced in Perl 5.10. </p>
<p> Alternatively, you can achieve a similar static effect by declaring the variable in a separate block outside the function, eg </p>
<pre><code>    sub f { my $x if 0; return $x++ }
</code></pre>
<p> becomes </p>
<pre><code>    { my $x; sub f { return $x++ } }
</code></pre>
<p> The use of <code>&quot;my()&quot;</code> in a false conditional has been deprecated in Perl 5.10, and it will become a fatal error in Perl 5.30. </p>
<p> <i>Reading/writing bytes from/to :utf8 handles.</i> </p>
<p> The <code>sysread()</code>, <code>recv()</code>, <code>syswrite()</code> and <code>send()</code> operators are deprecated on handles that have the <code>&quot;:utf8&quot;</code> layer, either explicitly, or implicitly, eg., with the <code>&quot;:encoding(UTF-16LE)&quot;</code> layer. </p>
<p> Both <code>sysread()</code> and <code>recv()</code> currently use only the <code>&quot;:utf8&quot;</code> flag for the stream, ignoring the actual layers. Since <code>sysread()</code> and <code>recv()</code> do no <font SIZE="-1">UTF-8</font> validation they can end up creating invalidly encoded scalars. </p>
<p> Similarly, <code>syswrite()</code> and <code>send()</code> use only the <code>&quot;:utf8&quot;</code> flag, otherwise ignoring any layers. If the flag is set, both write the value <font SIZE="-1">UTF-8</font> encoded, even if the layer is some different encoding, such as the example above. </p>
<p> Ideally, all of these operators would completely ignore the <code>&quot;:utf8&quot;</code> state, working only with bytes, but this would result in silently breaking existing code. To avoid this a future version of perl will throw an exception when any of <code>sysread()</code>, <code>recv()</code>, <code>syswrite()</code> or <code>send()</code> are called on handle with the <code>&quot;:utf8&quot;</code> layer. </p>
<p> In Perl 5.30, it will no longer be possible to use <code>sysread()</code>, <code>recv()</code>, <code>syswrite()</code> or <code>send()</code> to read or send bytes from/to :utf8 handles. </p>
<p> <i>Use of unassigned code point or non-standalone grapheme for a delimiter.</i> </p>
<p> A grapheme is what appears to a native-speaker of a language to be a character. In Unicode (and hence Perl) a grapheme may actually be several adjacent characters that together form a complete grapheme. For example, there can be a base character, like ``R&#8217;&#8216; and an accent, like a circumflex ``^&#8216;&#8216;, that appear to be a single character when displayed, with the circumflex hovering over the ``R&#8217;&#8216;. </p>
<p> As of Perl 5.30, use of delimiters which are non-standalone graphemes is fatal, in order to move the language to be able to accept multi-character graphemes as delimiters. </p>
<p> Also, as of Perl 5.30, delimiters which are unassigned code points but that may someday become assigned are prohibited. Otherwise, code that works today would fail to compile if the currently unassigned delimiter ends up being something that isn&#8217;t a stand-alone grapheme. Because Unicode is never going to assign non-character code points, nor code points that are above the legal Unicode maximum, those can be delimiters.  </p>
<h3>Perl 5.28</h3>
<p> <i>Attributes </i>&quot;:locked&quot;<i> and </i>&quot;:unique&quot;<i></i> </p>
<p> The attributes <code>&quot;:locked&quot;</code> (on code references) and <code>&quot;:unique&quot;</code> (on array, hash and scalar references) have had no effect since Perl 5.005 and Perl 5.8.8 respectively. Their use has been deprecated since. </p>
<p> As of Perl 5.28, these attributes are syntax errors. Since the attributes do not do anything, removing them from your code fixes the syntax error; and removing them will not influence the behaviour of your code. </p>
<p> <i>Bare here-document terminators</i> </p>
<p> Perl has allowed you to use a bare here-document terminator to have the here-document end at the first empty line. This practise was deprecated in Perl 5.000; as of Perl 5.28, using a bare here-document terminator throws a fatal error. </p>
<p> You are encouraged to use the explicitly quoted form if you wish to use an empty line as the terminator of the here-document: </p>
<pre><code>  print &lt;&lt;&quot;&quot;;
    Print this line.
  # Previous blank line ends the here-document.
</code></pre>
<p> <i>Setting $/ to a reference to a non-positive integer</i> </p>
<p> You assigned a reference to a scalar to <code>$/</code> where the referenced item is not a positive integer. In older perls this <code>appeared</code> to work the same as setting it to <code>&quot;undef&quot;</code> but was in fact internally different, less efficient and with very bad luck could have resulted in your file being split by a stringified form of the reference. </p>
<p> In Perl 5.20.0 this was changed so that it would be <code>exactly</code> the same as setting <code>$/</code> to undef, with the exception that this warning would be thrown. </p>
<p> As of Perl 5.28, setting <code>$/</code> to a reference of a non-positive integer throws a fatal error. </p>
<p> You are recommended to change your code to set <code>$/</code> to <code>&quot;undef&quot;</code> explicitly if you wish to slurp the file. </p>
<p> <i>Limit on the value of Unicode code points.</i> </p>
<p> Unicode only allows code points up to 0x10FFFF, but Perl allows much larger ones. Up till Perl 5.28, it was allowed to use code points exceeding the maximum value of an integer (<code>&quot;IV_MAX&quot;</code>). However, that did break the perl interpreter in some constructs, including causing it to hang in a few cases. The known problem areas were in <code>&quot;tr///&quot;</code>, regular expression pattern matching using quantifiers, as quote delimiters in <code>&quot;q</code>X <code>...</code>X <code>&quot;</code> (where <i>X</i> is the <code>&quot;chr()&quot;</code> of a large code point), and as the upper limits in loops. </p>
<p> The use of out of range code points was deprecated in Perl 5.24; as of Perl 5.28 using a code point exceeding <code>&quot;IV_MAX&quot;</code> throws a fatal error. </p>
<p> If your code is to run on various platforms, keep in mind that the upper limit depends on the platform. It is much larger on 64-bit word sizes than 32-bit ones. For 32-bit integers, <code>&quot;IV_MAX&quot;</code> equals <code>0x7FFFFFFF</code>, for 64-bit integers, <code>&quot;IV_MAX&quot;</code> equals <code>0x7FFFFFFFFFFFFFFF</code>. </p>
<p> <i>Use of comma-less variable list in formats.</i> </p>
<p> It was allowed to use a list of variables in a format, without separating them with commas. This usage has been deprecated for a long time, and as of Perl 5.28, this throws a fatal error. </p>
<p> <i>Use of </i>&quot;\N{}&quot;<i></i> </p>
<p> Use of <code>&quot;\N{}&quot;</code> with nothing between the braces was deprecated in Perl 5.24, and throws a fatal error as of Perl 5.28. </p>
<p> Since such a construct is equivalent to using an empty string, you are recommended to remove such <code>&quot;\N{}&quot;</code> constructs. </p>
<p> <i>Using the same symbol to open a filehandle and a dirhandle</i> </p>
<p> It used to be legal to use <code>&quot;open()&quot;</code> to associate both a filehandle and a dirhandle to the same symbol (glob or scalar). This idiom is likely to be confusing, and it was deprecated in Perl 5.10. </p>
<p> Using the same symbol to <code>&quot;open()&quot;</code> a filehandle and a dirhandle throws a fatal error as of Perl 5.28. </p>
<p> You should be using two different symbols instead. </p>
<p> <i>${^ENCODING} is no longer supported.</i> </p>
<p> The special variable <code>&quot;${^ENCODING}&quot;</code> was used to implement the <code>&quot;encoding&quot;</code> pragma. Setting this variable to anything other than <code>&quot;undef&quot;</code> was deprecated in Perl 5.22. Full deprecation of the variable happened in Perl 5.25.3. </p>
<p> Setting this variable to anything other than an undefined value throws a fatal error as of Perl 5.28. </p>
<p> <i></i>&quot;B::OP::terse&quot;<i></i> </p>
<p> This method, which just calls <code>&quot;B::Concise::b_terse&quot;</code>, has been deprecated, and disappeared in Perl 5.28. Please use <code>&quot;B::Concise&quot;</code> instead. </p>
<p> <i>Use of inherited </i><font SIZE="-1"><i>AUTOLOAD</i></font><i> for non-method </i>%s::<i>%s() is no longer allowed</i> </p>
<p> As an (ahem) accidental feature, <code>&quot;AUTOLOAD&quot;</code> subroutines were looked up as methods (using the <code>@ISA</code> hierarchy) even when the subroutines to be autoloaded were called as plain functions (e.g. <code>&quot;Foo::bar()&quot;</code>), not as methods (e.g. <code>&quot;Foo-&gt;bar()&quot;</code> or <code>&quot;$obj-&gt;bar()&quot;</code>). </p>
<p> This bug was deprecated in Perl 5.004, has been rectified in Perl 5.28 by using method lookup only for methods&#8217; <code>&quot;AUTOLOAD&quot;</code>s. </p>
<p> The simple rule is: Inheritance will not work when autoloading non-methods. The simple fix for old code is: In any module that used to depend on inheriting <code>&quot;AUTOLOAD&quot;</code> for non-methods from a base class named <code>&quot;BaseClass&quot;</code>, execute <code>&quot;*AUTOLOAD = \&amp;BaseClass::AUTOLOAD&quot;</code> during startup. </p>
<p> In code that currently says <code>&quot;use AutoLoader; @ISA = qw(AutoLoader);&quot;</code> you should remove AutoLoader from <code>@ISA</code> and change <code>&quot;use AutoLoader;&quot;</code> to <code>&quot;use AutoLoader &#8216;AUTOLOAD&#8217;;&quot;</code>. </p>
<p> <i>Use of code points over 0xFF in string bitwise operators</i> </p>
<p> The string bitwise operators, <code>&quot;&amp;&quot;</code>, <code>&quot;|&quot;</code>, <code>&quot;^&quot;</code>, and <code>&quot;~&quot;</code>, treat their operands as strings of bytes. As such, values above 0xFF are nonsensical. Using such code points with these operators was deprecated in Perl 5.24, and is fatal as of Perl 5.28. </p>
<p> <i>In </i><font SIZE="-1"><i>XS</i></font><i> code, use of </i>&quot;to_utf8_case()&quot;<i></i> </p>
<p> This function has been removed as of Perl 5.28; instead convert to call the appropriate one of: <code>&quot;toFOLD_utf8_safe&quot;</code>. <code>&quot;toLOWER_utf8_safe&quot;</code>, <code>&quot;toTITLE_utf8_safe&quot;</code>, or <code>&quot;toUPPER_utf8_safe&quot;</code>.  </p>
<h3>Perl 5.26</h3>
<p> <i></i>&quot;--libpods&quot;<i> in </i>&quot;Pod::Html&quot;<i></i> </p>
<p> Since Perl 5.18, the option <code>&quot;--libpods&quot;</code> has been deprecated, and using this option did not do anything other than producing a warning. </p>
<p> The <code>&quot;--libpods&quot;</code> option is no longer recognized as of Perl 5.26. </p>
<p> <i>The utilities </i>&quot;c2ph&quot;<i> and </i>&quot;pstruct&quot;<i></i> </p>
<p> These old, perl3-era utilities have been deprecated in favour of <code>&quot;h2xs&quot;</code> for a long time. As of Perl 5.26, they have been removed. </p>
<p> <i>Trapping </i>&quot;$SIG {__DIE__}&quot;<i> other than during program exit.</i> </p>
<p> The <code>$SIG{__DIE__}</code> hook is called even inside an <code>&quot;eval()&quot;</code>. It was never intended to happen this way, but an implementation glitch made this possible. This used to be deprecated, as it allowed strange action at a distance like rewriting a pending exception in <code>$@</code>. Plans to rectify this have been scrapped, as users found that rewriting a pending exception is actually a useful feature, and not a bug. </p>
<p> Perl never issued a deprecation warning for this; the deprecation was by documentation policy only. But this deprecation has been lifted as of Perl 5.26. </p>
<p> <i>Malformed </i><font SIZE="-1"><i>UTF-8</i></font><i> string in ``%s&#8217;&#8216;</i> </p>
<p> This message indicates a bug either in the Perl core or in <font SIZE="-1">XS</font> code. Such code was trying to find out if a character, allegedly stored internally encoded as <font SIZE="-1">UTF-8,</font> was of a given type, such as being punctuation or a digit. But the character was not encoded in legal <font SIZE="-1">UTF-8.</font> The <code>%s</code> is replaced by a string that can be used by knowledgeable people to determine what the type being checked against was. </p>
<p> Passing malformed strings was deprecated in Perl 5.18, and became fatal in Perl 5.26.  </p>
<h3>Perl 5.24</h3>
<p> <i>Use of </i>*glob{FILEHANDLE}<i></i> </p>
<p> The use of <code>*glob{FILEHANDLE}</code> was deprecated in Perl 5.8. The intention was to use <code>*glob{IO}</code> instead, for which <code>*glob{FILEHANDLE}</code> is an alias. </p>
<p> However, this feature was undeprecated in Perl 5.24. </p>
<p> <i>Calling POSIX::%s() is deprecated</i> </p>
<p> The following functions in the <code>&quot;POSIX&quot;</code> module are no longer available: <code>&quot;isalnum&quot;</code>, <code>&quot;isalpha&quot;</code>, <code>&quot;iscntrl&quot;</code>, <code>&quot;isdigit&quot;</code>, <code>&quot;isgraph&quot;</code>, <code>&quot;islower&quot;</code>, <code>&quot;isprint&quot;</code>, <code>&quot;ispunct&quot;</code>, <code>&quot;isspace&quot;</code>, <code>&quot;isupper&quot;</code>, and <code>&quot;isxdigit&quot;</code>. The functions are buggy and don&#8217;t work on <font SIZE="-1">UTF-8</font> encoded strings. See their entries in <font SIZE="-1">POSIX</font> for more information. </p>
<p> The functions were deprecated in Perl 5.20, and removed in Perl 5.24.  </p>
<h3>Perl 5.16</h3>
<p> <i>Use of </i>%s <i> on a handle without * is deprecated</i> </p>
<p> It used to be possible to use <code>&quot;tie&quot;</code>, <code>&quot;tied&quot;</code> or <code>&quot;untie&quot;</code> on a scalar while the scalar holds a typeglob. This caused its filehandle to be tied. It left no way to tie the scalar itself when it held a typeglob, and no way to untie a scalar that had had a typeglob assigned to it. </p>
<p> This was deprecated in Perl 5.14, and the bug was fixed in Perl 5.16. </p>
<p> So now <code>&quot;tie $scalar&quot;</code> will always tie the scalar, not the handle it holds. To tie the handle, use <code>&quot;tie *$scalar&quot;</code> (with an explicit asterisk). The same applies to <code>&quot;tied *$scalar&quot;</code> and <code>&quot;untie *$scalar&quot;</code>.  </p>
<h2>SEE ALSO</h2>
<p> warnings, diagnostics. </p>
