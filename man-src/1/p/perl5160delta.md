---
title: "perl5160delta(1)"
name: "perl5160delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5160delta/"
description: "perl5160delta – what is new for perl v5.16.0"
---

<h2 class="name">NAME</h2>
<p> perl5160delta &#8211; what is new for perl v5.16.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.14.0 release and the 5.16.0 release. </p>
<p> If you are upgrading from an earlier release such as 5.12.0, first read perl5140delta, which describes differences between 5.12.0 and 5.14.0. </p>
<p> Some bug fixes in this release have been backported to later releases of 5.14.x. Those are indicated with the 5.14.x version in parentheses.</p>
<h2>Notice</h2>
<p> With the release of Perl 5.16.0, the 5.12.x series of releases is now out of its support period. There may be future 5.12.x releases, but only in the event of a critical security issue. Users of Perl 5.12 or earlier should consider upgrading to a more recent release of Perl. </p>
<p> This policy is described in greater detail in perlpolicy.</p>
<h2>Core Enhancements</h2>
<h3>use VERSION</h3>
<p> As of this release, version declarations like <tt>&quot;use v5.16&quot;</tt> now disable all features before enabling the new feature bundle. This means that the following holds true: </p>
<pre>
    use 5.016;
    # only 5.16 features enabled here
    use 5.014;
    # only 5.14 features enabled here (not 5.16)
</pre>
<p> <tt>&quot;use v5.12&quot;</tt> and higher continue to enable strict, but explicit <tt>&quot;use strict&quot;</tt> and <tt>&quot;no strict&quot;</tt> now override the version declaration, even when they come first: </p>
<pre>
    no strict;
    use 5.012;
    # no strict here
</pre>
<p> There is a new &#8220;:default&#8221; feature bundle that represents the set of features enabled before any version declaration or <tt>&quot;use feature&quot;</tt> has been seen. Version declarations below 5.10 now enable the &#8220;:default&#8221; feature set. This does not actually change the behavior of <tt>&quot;use v5.8&quot;</tt>, because features added to the &#8220;:default&#8221; set are those that were traditionally enabled by default, before they could be turned off. </p>
<p> <tt>&quot;no feature&quot;</tt> now resets to the default feature set. To disable all features (which is likely to be a pretty special-purpose request, since it presumably won&#8217;t match any named set of semantics) you can now write <tt>&quot;no feature ':all'&quot;</tt>. </p>
<p> <tt>$[</tt> is now disabled under <tt>&quot;use v5.16&quot;</tt>. It is part of the default feature set and can be turned on or off explicitly with <tt>&quot;use feature 'array_base'&quot;</tt>.</p>
<h3>__SUB__</h3>
<p> The new <tt>&quot;__SUB__&quot;</tt> token, available under the <tt>&quot;current_sub&quot;</tt> feature (see feature) or <tt>&quot;use v5.16&quot;</tt>, returns a reference to the current subroutine, making it easier to write recursive closures.</p>
<h3>New and Improved Built-ins</h3>
<p> <i>More consistent </i>&quot;eval&quot;<i></i> </p>
<p> The <tt>&quot;eval&quot;</tt> operator sometimes treats a string argument as a sequence of characters and sometimes as a sequence of bytes, depending on the internal encoding. The internal encoding is not supposed to make any difference, but there is code that relies on this inconsistency. </p>
<p> The new <tt>&quot;unicode_eval&quot;</tt> and <tt>&quot;evalbytes&quot;</tt> features (enabled under <tt>&quot;use 5.16.0&quot;</tt>) resolve this. The <tt>&quot;unicode_eval&quot;</tt> feature causes <tt>&quot;eval $string&quot;</tt> to treat the string always as Unicode. The <tt>&quot;evalbytes&quot;</tt> features provides a function, itself called <tt>&quot;evalbytes&quot;</tt>, which evaluates its argument always as a string of bytes. </p>
<p> These features also fix oddities with source filters leaking to outer dynamic scopes. </p>
<p> See feature for more detail. </p>
<p> <i></i>&quot;substr&quot;<i> lvalue revamp</i> </p>
<p> When <tt>&quot;substr&quot;</tt> is called in lvalue or potential lvalue context with two or three arguments, a special lvalue scalar is returned that modifies the original string (the first argument) when assigned to. </p>
<p> Previously, the offsets (the second and third arguments) passed to <tt>&quot;substr&quot;</tt> would be converted immediately to match the string, negative offsets being translated to positive and offsets beyond the end of the string being truncated. </p>
<p> Now, the offsets are recorded without modification in the special lvalue scalar that is returned, and the original string is not even looked at by <tt>&quot;substr&quot;</tt> itself, but only when the returned lvalue is read or modified. </p>
<p> These changes result in an incompatible change: </p>
<p> If the original string changes length after the call to <tt>&quot;substr&quot;</tt> but before assignment to its return value, negative offsets will remember their position from the end of the string, affecting code like this: </p>
<pre><code>
my $string = "string";
my $lvalue = \substr $string, -4, 2;
print $$lvalue, "
";
#prints "ri" $string = "bailing twine";
print $$lvalue, "
";
#prints "wi";
used to print "il"
</code></pre>
<p> The same thing happens with an omitted third argument. The returned lvalue will always extend to the end of the string, even if the string becomes longer. </p>
<p> Since this change also allowed many bugs to be fixed (see &quot;The <tt>&quot;substr&quot;</tt> operator&quot;), and since the behavior of negative offsets has never been specified, the change was deemed acceptable. </p>
<p> <i>Return value of </i>&quot;tied&quot;<i></i> </p>
<p> The value returned by <tt>&quot;tied&quot;</tt> on a tied variable is now the actual scalar that holds the object to which the variable is tied. This lets ties be weakened with <tt>&quot;Scalar::Util::weaken(tied $tied_variable)&quot;</tt>.</p>
<h3>Unicode Support</h3>
<p> <i>Supports (almost) Unicode 6.1</i> </p>
<p> Besides the addition of whole new scripts, and new characters in existing scripts, this new version of Unicode, as always, makes some changes to existing characters. One change that may trip up some applications is that the General Category of two characters in the Latin-1 range, <font SIZE="-1">PILCROW SIGN</font> and <font SIZE="-1">SECTION SIGN,</font> has been changed from Other_Symbol to Other_Punctuation. The same change has been made for a character in each of Tibetan, Ethiopic, and Aegean. The code points U+3248..U+324F (<font SIZE="-1">CIRCLED NUMBER TEN ON BLACK SQUARE</font> through <font SIZE="-1">CIRCLED NUMBER EIGHTY ON BLACK SQUARE</font>) have had their General Category changed from Other_Symbol to Other_Numeric. The Line Break property has changes for Hebrew and Japanese; and because of other changes in 6.1, the Perl regular expression construct <tt>&quot;\X&quot;</tt> now works differently for some characters in Thai and Lao. </p>
<p> New aliases (synonyms) have been defined for many property values; these, along with the previously existing ones, are all cross-indexed in perluniprops. </p>
<p> The return value of <tt>&quot;charnames::viacode()&quot;</tt> is affected by other changes: </p>
<pre>
 Code point      Old Name             New Name
   U+000A    LINE FEED (LF)        LINE FEED
   U+000C    FORM FEED (FF)        FORM FEED
   U+000D    CARRIAGE RETURN (CR)  CARRIAGE RETURN
   U+0085    NEXT LINE (NEL)       NEXT LINE
   U+008E    SINGLE-SHIFT 2        SINGLE-SHIFT-2
   U+008F    SINGLE-SHIFT 3        SINGLE-SHIFT-3
   U+0091    PRIVATE USE 1         PRIVATE USE-1
   U+0092    PRIVATE USE 2         PRIVATE USE-2
   U+2118    SCRIPT CAPITAL P      WEIERSTRASS ELLIPTIC FUNCTION
</pre>
<p> Perl will accept any of these names as input, but <tt>&quot;charnames::viacode()&quot;</tt> now returns the new name of each pair. The change for U+2118 is considered by Unicode to be a correction, that is the original name was a mistake (but again, it will remain forever valid to use it to refer to U+2118). But most of these changes are the fallout of the mistake Unicode 6.0 made in naming a character used in Japanese cell phones to be &#8220;<font SIZE="-1">BELL&#8221;,</font> which conflicts with the longstanding industry use of (and Unicode&#8217;s recommendation to use) that name to mean the <font SIZE="-1">ASCII</font> control character at U+0007. Therefore, that name has been deprecated in Perl since v5.14, and any use of it will raise a warning message (unless turned off). The name &#8220;<font SIZE="-1">ALERT&#8221;</font> is now the preferred name for this code point, with &#8220;<font SIZE="-1">BEL&#8221;</font> an acceptable short form. The name for the new cell phone character, at code point U+1F514, remains undefined in this version of Perl (hence we don&#8217;t implement quite all of Unicode 6.1), but starting in v5.18, <font SIZE="-1">BELL</font> will mean this character, and not U+0007. </p>
<p> Unicode has taken steps to make sure that this sort of mistake does not happen again. The Standard now includes all generally accepted names and abbreviations for control characters, whereas previously it didn&#8217;t (though there were recommended names for most of them, which Perl used). This means that most of those recommended names are now officially in the Standard. Unicode did not recommend names for the four code points listed above between U+008E and U+008F, and in standardizing them Unicode subtly changed the names that Perl had previously given them, by replacing the final blank in each name by a hyphen. Unicode also officially accepts names that Perl had deprecated, such as <font SIZE="-1">FILE SEPARATOR.</font> Now the only deprecated name is <font SIZE="-1">BELL.</font> Finally, Perl now uses the new official names instead of the old (now considered obsolete) names for the first four code points in the list above (the ones which have the parentheses in them). </p>
<p> Now that the names have been placed in the Unicode standard, these kinds of changes should not happen again, though corrections, such as to U+2118, are still possible. </p>
<p> Unicode also added some name abbreviations, which Perl now accepts: <font SIZE="-1">SP</font> for <font SIZE="-1">SPACE</font>; <font SIZE="-1">TAB</font> for <font SIZE="-1">CHARACTER TABULATION</font>; <font SIZE="-1">NEW LINE, END OF LINE, NL,</font> and <font SIZE="-1">EOL</font> for <font SIZE="-1">LINE FEED</font>; LOCKING-SHIFT <font SIZE="-1">ONE</font> for <font SIZE="-1">SHIFT OUT</font>; LOCKING-SHIFT <font SIZE="-1">ZERO</font> for <font SIZE="-1">SHIFT IN</font>; and <font SIZE="-1">ZWNBSP</font> for <font SIZE="-1">ZERO WIDTH</font> NO-BREAK <font SIZE="-1">SPACE.</font> </p>
<p> More details on this version of Unicode are provided in &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode6.1.0/">http://www.unicode.org/versions/Unicode6.1.0/</a>&gt;. </p>
<p> <i></i>&quot;use charnames&quot;<i> is no longer needed for </i>&quot;\N{name}&quot;<i></i> </p>
<p> When <tt>&quot;\N{</tt>name<tt>}&quot;</tt> is encountered, the <tt>&quot;charnames&quot;</tt> module is now automatically loaded when needed as if the <tt>&quot;:full&quot;</tt> and <tt>&quot;:short&quot;</tt> options had been specified. See charnames for more information. </p>
<p> <i></i>&quot;\N{&#8230;}&quot;<i> can now have Unicode loose name matching</i> </p>
<p> This is described in the <tt>&quot;charnames&quot;</tt> item in &#8220;Updated Modules and Pragmata&#8221; below. </p>
<p> <i>Unicode Symbol Names</i> </p>
<p> Perl now has proper support for Unicode in symbol names. It used to be that <tt>&quot;*{$foo}&quot;</tt> would ignore the internal <font SIZE="-1">UTF8</font> flag and use the bytes of the underlying representation to look up the symbol. That meant that <tt>&quot;*{&quot;
