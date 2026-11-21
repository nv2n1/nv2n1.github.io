---

title: "perlunicode(1)"
name: "perlunicode"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlunicode/"
description: "perlunicode – Unicode support in Perl"
---

<p> perlunicode &#8211; Unicode support in Perl </p>
<h2>DESCRIPTION</h2>
<p> If you haven&#8217;t already, before reading this document, you should become familiar with both perlunitut and perluniintro. </p>
<p> Unicode aims to <font SIZE="-1"><code>UNI</code></font>-fy the en-<font SIZE="-1"><code>CODE</code></font>-ings of all the world&#8217;s character sets into a single Standard. For quite a few of the various coding standards that existed when Unicode was first created, converting from each to Unicode essentially meant adding a constant to each code point in the original standard, and converting back meant just subtracting that same constant. For <font SIZE="-1">ASCII</font> and <font SIZE="-1">ISO-8859-1,</font> the constant is 0. For <font SIZE="-1">ISO-8859-5,</font> (Cyrillic) the constant is 864; for Hebrew (<font SIZE="-1">ISO-8859-8</font>), it&#8217;s 1488; Thai (<font SIZE="-1">ISO-8859-11</font>), 3424; and so forth. This made it easy to do the conversions, and facilitated the adoption of Unicode. </p>
<p> And it worked; nowadays, those legacy standards are rarely used. Most everyone uses Unicode. </p>
<p> Unicode is a comprehensive standard. It specifies many things outside the scope of Perl, such as how to display sequences of characters. For a full discussion of all aspects of Unicode, see &lt;<a rel="nofollow" href="http://www.unicode.org">http://www.unicode.org</a>&gt;.</p>
<h3>Important Caveats</h3>
<p> Even though some of this section may not be understandable to you on first reading, we think it&#8217;s important enough to highlight some of the gotchas before delving further, so here goes: </p>
<p> Unicode support is an extensive requirement. While Perl does not implement the Unicode standard or the accompanying technical reports from cover to cover, Perl does support many Unicode features. </p>
<p> Also, the use of Unicode may present security issues that aren&#8217;t obvious, see &#8220;Security Implications of Unicode&#8221; below.</p>
<dl>
<dt>Safest if you &quot;use feature &#8216;unicode_strings&#8217;&quot;</dt>
<dd> In order to preserve backward compatibility, Perl does not turn on full internal Unicode support unless the pragma <tt>&quot;use feature 'unicode_strings'&quot;</tt> is specified. (This is automatically selected if you <tt>&quot;use 5.012&quot;</tt> or higher.) Failure to do this can trigger unexpected surprises. See &#8220;The &#8221;Unicode Bug&quot;&quot; below. </dd>
<p> This pragma doesn&#8217;t affect I/O. Nor does it change the internal representation of strings, only their interpretation. There are still several places where Unicode isn&#8217;t fully supported, such as in filenames.</p>
<dt>Input and Output Layers</dt>
<dd> Use the <tt>&quot;:encoding(...)&quot;</tt> layer to read from and write to filehandles using the specified encoding. (See open.)</dd>
<dt>You must convert your non-ASCII, non-UTF-8 Perl scripts to be <font SIZE="-1">UTF-8.</font></dt>
<dd> The encoding module has been deprecated since perl 5.18 and the perl internals it requires have been removed with perl 5.26.</dd>
<dt>&quot;use utf8&quot; still needed to enable <font SIZE="-1">UTF-8</font> in scripts</dt>
<dd> If your Perl script is itself encoded in <font SIZE="-1">UTF-8</font>, the <tt>&quot;use utf8&quot;</tt> pragma must be explicitly included to enable recognition of that (in string or regular expression literals, or in identifier names). <code>This is the only time when an explicit </code>&quot;use utf8&quot;<code> is needed.</code> (See utf8). </dd>
<p> If a Perl script begins with the bytes that form the <font SIZE="-1">UTF-8</font> encoding of the Unicode <font SIZE="-1">BYTE ORDER MARK</font> (<tt>&quot;BOM&quot;</tt>, see &#8220;Unicode Encodings&#8221;), those bytes are completely ignored.</p>
<dt><font SIZE="-1">UTF-16</font> scripts autodetected</dt>
<dd> If a Perl script begins with the Unicode <tt>&quot;BOM&quot;</tt> (<font SIZE="-1">UTF-16LE, UTF16-BE</font>), or if the script looks like non-<tt>&quot;BOM&quot;</tt>-marked <font SIZE="-1">UTF-16</font> of either endianness, Perl will correctly read in the script as the appropriate Unicode encoding.</dd></dl>
<h3>Byte and Character Semantics</h3>
<p> Before Unicode, most encodings used 8 bits (a single byte) to encode each character. Thus a character was a byte, and a byte was a character, and there could be only 256 or fewer possible characters. &#8220;Byte Semantics&#8221; in the title of this section refers to this behavior. There was no need to distinguish between &#8220;Byte&#8221; and &#8220;Character&#8221;. </p>
<p> Then along comes Unicode which has room for over a million characters (and Perl allows for even more). This means that a character may require more than a single byte to represent it, and so the two terms are no longer equivalent. What matter are the characters as whole entities, and not usually the bytes that comprise them. That&#8217;s what the term &#8220;Character Semantics&#8221; in the title of this section refers to. </p>
<p> Perl had to change internally to decouple &#8220;bytes&#8221; from &#8220;characters&#8221;. It is important that you too change your ideas, if you haven&#8217;t already, so that &#8220;byte&#8221; and &#8220;character&#8221; no longer mean the same thing in your mind. </p>
<p> The basic building block of Perl strings has always been a &#8220;character&#8221;. The changes basically come down to that the implementation no longer thinks that a character is always just a single byte. </p>
<p> There are various things to note:</p>
<dl>
<dt>&bull;</dt>
<dd> String handling functions, for the most part, continue to operate in terms of characters. <tt>&quot;length()&quot;</tt>, for example, returns the number of characters in a string, just as before. But that number no longer is necessarily the same as the number of bytes in the string (there may be more bytes than characters). The other such functions include <tt>&quot;chop()&quot;</tt>, <tt>&quot;chomp()&quot;</tt>, <tt>&quot;substr()&quot;</tt>, <tt>&quot;pos()&quot;</tt>, <tt>&quot;index()&quot;</tt>, <tt>&quot;rindex()&quot;</tt>, <tt>&quot;sort()&quot;</tt>, <tt>&quot;sprintf()&quot;</tt>, and <tt>&quot;write()&quot;</tt>. </dd>
<p> The exceptions are:</p>
<dl>
<dl>
<dt>&bull;</dt>
<dd> the bit-oriented <tt>&quot;vec&quot;</tt> </dd>
<dt>&bull;</dt>
<dd> the byte-oriented <tt>&quot;pack&quot;</tt>/<tt>&quot;unpack&quot;</tt> <tt>&quot;C&quot;</tt> format </dd>
<p> However, the <tt>&quot;W&quot;</tt> specifier does operate on whole characters, as does the <tt>&quot;U&quot;</tt> specifier.</p>
<dt>&bull;</dt>
<dd> some operators that interact with the platform&#8217;s operating system </dd>
<p> Operators dealing with filenames are examples.</p>
<dt>&bull;</dt>
<dd> when the functions are called from within the scope of the <tt>&quot;use bytes&quot;</tt> pragma </dd>
<p> Likely, you should use this only for debugging anyway.</dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> Strings&#8212;including hash keys&#8212;and regular expression patterns may contain characters that have ordinal values larger than 255. </dd>
<p> If you use a Unicode editor to edit your program, Unicode characters may occur directly within the literal strings in <font SIZE="-1">UTF-8</font> encoding, or <font SIZE="-1">UTF-16.</font> (The former requires a <tt>&quot;use utf8&quot;</tt>, the latter may require a <tt>&quot;BOM&quot;</tt>.) </p>
<p> &#8220;Creating Unicode&#8221; in perluniintro gives other ways to place non-ASCII characters in your strings.</p>
<dt>&bull;</dt>
<dd> The <tt>&quot;chr()&quot;</tt> and <tt>&quot;ord()&quot;</tt> functions work on whole characters.</dd>
<dt>&bull;</dt>
<dd> Regular expressions match whole characters. For example, <tt>&quot;.&quot;</tt> matches a whole character instead of only a single byte.</dd>
<dt>&bull;</dt>
<dd> The <tt>&quot;tr///&quot;</tt> operator translates whole characters. (Note that the <tt>&quot;tr///CU&quot;</tt> functionality has been removed. For similar functionality to that, see <tt>&quot;pack('U0', ...)&quot;</tt> and <tt>&quot;pack('C0', ...)&quot;</tt>).</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;scalar reverse()&quot;</tt> reverses by character rather than by byte.</dd>
<dt>&bull;</dt>
<dd> The bit string operators, <tt>&quot;&amp; | ^ ~&quot;</tt> and (starting in v5.22) <tt>&quot;&amp;. |. ^. ~.&quot;</tt> can operate on bit strings encoded in <font SIZE="-1">UTF-8,</font> but this can give unexpected results if any of the strings contain code points above 0xFF. Starting in v5.28, it is a fatal error to have such an operand. Otherwise, the operation is performed on a non-UTF-8 copy of the operand. If you&#8217;re not sure about the encoding of a string, downgrade it before using any of these operators; you can use <tt>&quot;utf8::utf8_downgrade()&quot;</tt>.</dd></dl>
<p> The bottom line is that Perl has always practiced &#8220;Character Semantics&#8221;, but with the advent of Unicode, that is now different than &#8220;Byte Semantics&#8221;.</p>
<h3><font SIZE="-1">ASCII</font> Rules versus Unicode Rules</h3>
<p> Before Unicode, when a character was a byte was a character, Perl knew only about the 128 characters defined by <font SIZE="-1">ASCII,</font> code points 0 through 127 (except for under <tt>&quot;use locale&quot;</tt>). That left the code points 128 to 255 as unassigned, and available for whatever use a program might want. The only semantics they have is their ordinal numbers, and that they are members of none of the non-negative character classes. None are considered to match <tt>&quot;\w&quot;</tt> for example, but all match <tt>&quot;\W&quot;</tt>. </p>
<p> Unicode, of course, assigns each of those code points a particular meaning (along with ones above 255). To preserve backward compatibility, Perl only uses the Unicode meanings when there is some indication that Unicode is what is intended; otherwise the non-ASCII code points remain treated as if they are unassigned. </p>
<p> Here are the ways that Perl knows that a string should be treated as Unicode:</p>
<dl>
<dt>&bull;</dt>
<dd> Within the scope of <tt>&quot;use utf8&quot;</tt> </dd>
<p> If the whole program is Unicode (signified by using 8-bit <code>U</code>nicode <code>T</code>ransformation <code>F</code>ormat), then all literal strings within it must be Unicode.</p>
<dt>&bull;</dt>
<dd> Within the scope of <tt>&quot;use feature 'unicode_strings'&quot;</tt> </dd>
<p> This pragma was created so you can explicitly tell Perl that operations executed within its scope are to use Unicode rules. More operations are affected with newer perls. See &#8220;The &#8221;Unicode Bug&quot;&quot;.</p>
<dt>&bull;</dt>
<dd> Within the scope of <tt>&quot;use 5.012&quot;</tt> or higher </dd>
<p> This implicitly turns on <tt>&quot;use feature 'unicode_strings'&quot;</tt>.</p>
<dt>&bull;</dt>
<dd> Within the scope of <tt>&quot;use locale 'not_characters'&quot;</tt>, or <tt>&quot;use locale&quot;</tt> and the current locale is a <font SIZE="-1">UTF-8</font> locale. </dd>
<p> The former is defined to imply Unicode handling; and the latter indicates a Unicode locale, hence a Unicode interpretation of all strings within it.</p>
<dt>&bull;</dt>
<dd> When the string contains a Unicode-only code point </dd>
<p> Perl has never accepted code points above 255 without them being Unicode, so their use implies Unicode for the whole string.</p>
<dt>&bull;</dt>
<dd> When the string contains a Unicode named code point <tt>&quot;\N{...}&quot;</tt> </dd>
<p> The <tt>&quot;\N{...}&quot;</tt> construct explicitly refers to a Unicode code point, even if it is one that is also in <font SIZE="-1">ASCII.</font> Therefore the string containing it must be Unicode.</p>
<dt>&bull;</dt>
<dd> When the string has come from an external source marked as Unicode </dd>
<p> The <tt>&quot;-C&quot;</tt> command line option can specify that certain inputs to the program are Unicode, and the values of this can be read by your Perl code, see &#8220;${^UNICODE}&#8221; in perlvar.</p>
<dt>&bull;</dt>
<dd> When the string has been upgraded to <font SIZE="-1">UTF-8</font> </dd>
<p> The function <tt>&quot;utf8::utf8_upgrade()&quot;</tt> can be explicitly used to permanently (unless a subsequent <tt>&quot;utf8::utf8_downgrade()&quot;</tt> is called) cause a string to be treated as Unicode.</p>
<dt>&bull;</dt>
<dd> There are additional methods for regular expression patterns </dd>
<p> A pattern that is compiled with the <tt>&quot;/u&quot;</tt> or <tt>&quot;/a&quot;</tt> modifiers is treated as Unicode (though there are some restrictions with <tt>&quot;/a&quot;</tt>). Under the <tt>&quot;/d&quot;</tt> and <tt>&quot;/l&quot;</tt> modifiers, there are several other indications for Unicode; see &#8220;Character set modifiers&#8221; in perlre.</dl>
<p> Note that all of the above are overridden within the scope of <tt>&quot;use bytes&quot;</tt>; but you should be using this pragma only for debugging. </p>
<p> Note also that some interactions with the platform&#8217;s operating system never use Unicode rules. </p>
<p> When Unicode rules are in effect:</p>
<dl>
<dt>&bull;</dt>
<dd> Case translation operators use the Unicode case translation tables. </dd>
<p> Note that <tt>&quot;uc()&quot;</tt>, or <tt>&quot;</tt>\U&quot;</code> in interpolated strings, translates to uppercase, while <code>&quot;ucfirst&quot;</code>, or <code>&quot;\u&quot;</code> in interpolated strings, translates to titlecase in languages that make the distinction (which is equivalent to uppercase in languages without the distinction). </p>
<p> There is a <font SIZE="-1">CPAN</font> module, <code>&quot;Unicode::Casing&quot;</code>, which allows you to define your own mappings to be used in <code>&quot;lc()&quot;</code>, <code>&quot;lcfirst()&quot;</code>, <code>&quot;uc()&quot;</code>, <code>&quot;ucfirst()&quot;</code>, and <code>&quot;fc&quot;</code> (or their double-quoted string inlined versions such as <code>&quot;\U&quot;</code>). (Prior to Perl 5.16, this functionality was partially provided in the Perl core, but suffered from a number of insurmountable drawbacks, so the <font SIZE="-1">CPAN</font> module was written instead.) </p>
<dt>&bull;</dt>
<dd> <p> Character classes in regular expressions match based on the character properties specified in the Unicode properties database. </p>
<p> <code>&quot;\w&quot;</code> can be used to match a Japanese ideograph, for instance; and <code>&quot;[[:digit:]]&quot;</code> a Bengali number. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Named Unicode properties, scripts, and block ranges may be used (like bracketed character classes) by using the <code>&quot;\p{}&quot;</code> ``matches property&#8217;&#8216; construct and the <code>&quot;\P{}&quot;</code> negation, ``doesn&#8217;t match property&#8217;&#8216;. </p>
<p> See ``Unicode Character Properties&#8217;&#8216; for more details. </p>
<p> You can define your own character properties and use them in the regular expression with the <code>&quot;\p{}&quot;</code> or <code>&quot;\P{}&quot;</code> construct. See ``User-Defined Character Properties&#8217;&#8216; for more details. </p>
 </dd></dl>
<h3>Extended Grapheme Clusters (Logical characters)</h3>
<p> Consider a character, say <code>&quot;H&quot;</code>. It could appear with various marks around it, such as an acute accent, or a circumflex, or various hooks, circles, arrows, <i>etc.</i>, above, below, to one side or the other, <i>etc</i>. There are many possibilities among the world&#8217;s languages. The number of combinations is astronomical, and if there were a character for each combination, it would soon exhaust Unicode&#8217;s more than a million possible characters. So Unicode took a different approach: there is a character for the base <code>&quot;H&quot;</code>, and a character for each of the possible marks, and these can be variously combined to get a final logical character. So a logical character---what appears to be a single character---can be a sequence of more than one individual characters. The Unicode standard calls these ``extended grapheme clusters&#8217;&#8216; (which is an improved version of the no-longer much used ``grapheme cluster&#8217;&#8216;); Perl furnishes the <code>&quot;\X&quot;</code> regular expression construct to match such sequences in their entirety. </p>
<p> But Unicode&#8217;s intent is to unify the existing character set standards and practices, and several pre-existing standards have single characters that mean the same thing as some of these combinations, like <font SIZE="-1">ISO-8859-1,</font> which has quite a few of them. For example, <code>&quot;LATIN CAPITAL LETTER E WITH ACUTE&quot;</code> was already in this standard when Unicode came along. Unicode therefore added it to its repertoire as that single character. But this character is considered by Unicode to be equivalent to the sequence consisting of the character <code>&quot;LATIN CAPITAL LETTER E&quot;</code> followed by the character <code>&quot;COMBINING ACUTE ACCENT&quot;</code>. </p>
<p> <code>&quot;LATIN CAPITAL LETTER E WITH ACUTE&quot;</code> is called a ``pre-composed&#8217;&#8216; character, and its equivalence with the ``E&#8217;&#8216; and the ``<font SIZE="-1">COMBINING ACCENT&#8217;&#8216;</font> sequence is called canonical equivalence. All pre-composed characters are said to have a decomposition (into the equivalent sequence), and the decomposition type is also called canonical. A string may be comprised as much as possible of precomposed characters, or it may be comprised of entirely decomposed characters. Unicode calls these respectively, ``Normalization Form Composed&#8217;&#8216; (<font SIZE="-1">NFC</font>) and ``Normalization Form Decomposed&#8217;&#8216;. The <code>&quot;Unicode::Normalize&quot;</code> module contains functions that convert between the two. A string may also have both composed characters and decomposed characters; this module can be used to make it all one or the other. </p>
<p> You may be presented with strings in any of these equivalent forms. There is currently nothing in Perl 5 that ignores the differences. So you&#8217;ll have to specially handle it. The usual advice is to convert your inputs to <code>&quot;NFD&quot;</code> before processing further. </p>
<p> For more detailed information, see &lt;<a rel="nofollow" href="http://unicode.org/reports/tr15/">http://unicode.org/reports/tr15/</a>&gt;.  </p>
<h3>Unicode Character Properties</h3>
<p> (The only time that Perl considers a sequence of individual code points as a single logical character is in the <code>&quot;\X&quot;</code> construct, already mentioned above. Therefore ``character&#8217;&#8216; in this discussion means a single Unicode code point.) </p>
<p> Very nearly all Unicode character properties are accessible through regular expressions by using the <code>&quot;\p{}&quot;</code> ``matches property&#8217;&#8216; construct and the <code>&quot;\P{}&quot;</code> ``doesn&#8217;t match property&#8217;&#8216; for its negation. </p>
<p> For instance, <code>&quot;\p{Uppercase}&quot;</code> matches any single character with the Unicode <code>&quot;Uppercase&quot;</code> property, while <code>&quot;\p{L}&quot;</code> matches any character with a <code>&quot;General_Category&quot;</code> of <code>&quot;L&quot;</code> (letter) property (see ``General_Category&#8217;&#8216; below). Brackets are not required for single letter property names, so <code>&quot;\p{L}&quot;</code> is equivalent to <code>&quot;\pL&quot;</code>. </p>
<p> More formally, <code>&quot;\p{Uppercase}&quot;</code> matches any single character whose Unicode <code>&quot;Uppercase&quot;</code> property value is <code>&quot;True&quot;</code>, and <code>&quot;\P{Uppercase}&quot;</code> matches any character whose <code>&quot;Uppercase&quot;</code> property value is <code>&quot;False&quot;</code>, and they could have been written as <code>&quot;\p{Uppercase=True}&quot;</code> and <code>&quot;\p{Uppercase=False}&quot;</code>, respectively. </p>
<p> This formality is needed when properties are not binary; that is, if they can take on more values than just <code>&quot;True&quot;</code> and <code>&quot;False&quot;</code>. For example, the <code>&quot;Bidi_Class&quot;</code> property (see ``Bidirectional Character Types&#8217;&#8216; below), can take on several different values, such as <code>&quot;Left&quot;</code>, <code>&quot;Right&quot;</code>, <code>&quot;Whitespace&quot;</code>, and others. To match these, one needs to specify both the property name (<code>&quot;Bidi_Class&quot;</code>), <font SIZE="-1">AND</font> the value being matched against (<code>&quot;Left&quot;</code>, <code>&quot;Right&quot;</code>, <i>etc.</i>). This is done, as in the examples above, by having the two components separated by an equal sign (or interchangeably, a colon), like <code>&quot;\p{Bidi_Class: Left}&quot;</code>. </p>
<p> All Unicode-defined character properties may be written in these compound forms of <code>&quot;\p{</code>property <code>=</code>value <code>}&quot;</code> or <code>&quot;\p{</code>property <code>:</code>value <code>}&quot;</code>, but Perl provides some additional properties that are written only in the single form, as well as single-form short-cuts for all binary properties and certain others described below, in which you may omit the property name and the equals or colon separator. </p>
<p> Most Unicode character properties have at least two synonyms (or aliases if you prefer): a short one that is easier to type and a longer one that is more descriptive and hence easier to understand. Thus the <code>&quot;L&quot;</code> and <code>&quot;Letter&quot;</code> properties above are equivalent and can be used interchangeably. Likewise, <code>&quot;Upper&quot;</code> is a synonym for <code>&quot;Uppercase&quot;</code>, and we could have written <code>&quot;\p{Uppercase}&quot;</code> equivalently as <code>&quot;\p{Upper}&quot;</code>. Also, there are typically various synonyms for the values the property can be. For binary properties, <code>&quot;True&quot;</code> has 3 synonyms: <code>&quot;T&quot;</code>, <code>&quot;Yes&quot;</code>, and <code>&quot;Y&quot;</code>; and <code>&quot;False&quot;</code> has correspondingly <code>&quot;F&quot;</code>, <code>&quot;No&quot;</code>, and <code>&quot;N&quot;</code>. But be careful. A short form of a value for one property may not mean the same thing as the same short form for another. Thus, for the <code>&quot;General_Category&quot;</code> property, <code>&quot;L&quot;</code> means <code>&quot;Letter&quot;</code>, but for the <code>&quot;Bidi_Class&quot;</code> property, <code>&quot;L&quot;</code> means <code>&quot;Left&quot;</code>. A complete list of properties and synonyms is in perluniprops. </p>
<p> Upper/lower case differences in property names and values are irrelevant; thus <code>&quot;\p{Upper}&quot;</code> means the same thing as <code>&quot;\p{upper}&quot;</code> or even <code>&quot;\p{UpPeR}&quot;</code>. Similarly, you can add or subtract underscores anywhere in the middle of a word, so that these are also equivalent to <code>&quot;\p{U_p_p_e_r}&quot;</code>. And white space is irrelevant adjacent to non-word characters, such as the braces and the equals or colon separators, so <code>&quot;\p{ Upper }&quot;</code> and <code>&quot;\p{ Upper_case : Y }&quot;</code> are equivalent to these as well. In fact, white space and even hyphens can usually be added or deleted anywhere. So even <code>&quot;\p{ Up-per case = Yes}&quot;</code> is equivalent. All this is called ``loose-matching&#8217;&#8216; by Unicode. The few places where stricter matching is used is in the middle of numbers, and in the Perl extension properties that begin or end with an underscore. Stricter matching cares about white space (except adjacent to non-word characters), hyphens, and non-interior underscores. </p>
<p> You can also use negation in both <code>&quot;\p{}&quot;</code> and <code>&quot;\P{}&quot;</code> by introducing a caret (<code>&quot;^&quot;</code>) between the first brace and the property name: <code>&quot;\p{^Tamil}&quot;</code> is equal to <code>&quot;\P{Tamil}&quot;</code>. </p>
<p> Almost all properties are immune to case-insensitive matching. That is, adding a <code>&quot;/i&quot;</code> regular expression modifier does not change what they match. There are two sets that are affected. The first set is <code>&quot;Uppercase_Letter&quot;</code>, <code>&quot;Lowercase_Letter&quot;</code>, and <code>&quot;Titlecase_Letter&quot;</code>, all of which match <code>&quot;Cased_Letter&quot;</code> under <code>&quot;/i&quot;</code> matching. And the second set is <code>&quot;Uppercase&quot;</code>, <code>&quot;Lowercase&quot;</code>, and <code>&quot;Titlecase&quot;</code>, all of which match <code>&quot;Cased&quot;</code> under <code>&quot;/i&quot;</code> matching. This set also includes its subsets <code>&quot;PosixUpper&quot;</code> and <code>&quot;PosixLower&quot;</code> both of which under <code>&quot;/i&quot;</code> match <code>&quot;PosixAlpha&quot;</code>. (The difference between these sets is that some things, such as Roman numerals, come in both upper and lower case so they are <code>&quot;Cased&quot;</code>, but aren&#8217;t considered letters, so they aren&#8217;t <code>&quot;Cased_Letter&quot;</code>&#8216;s.) </p>
<p> See ``Beyond Unicode code points&#8217;&#8216; for special considerations when matching Unicode properties against non-Unicode code points. </p>
<p> <i></i>General_Category <i></i> </p>
<p> Every Unicode character is assigned a general category, which is the ``most usual categorization of a character&#8217;&#8216; (from &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr44">http://www.unicode.org/reports/tr44</a>&gt;). </p>
<p> The compound way of writing these is like <code>&quot;\p{General_Category=Number}&quot;</code> (short: <code>&quot;\p{gc:n}&quot;</code>). But Perl furnishes shortcuts in which everything up through the equal or colon separator is omitted. So you can instead just write <code>&quot;\pN&quot;</code>. </p>
<p> Here are the short and long forms of the values the <code>&quot;General Category&quot;</code> property can have: </p>
<pre><code>    Short Long
    L Letter
    LC, L&amp; Cased_Letter (that is: [\p{Ll}\p{Lu}\p{Lt}])
    Lu Uppercase_Letter
    Ll Lowercase_Letter
    Lt Titlecase_Letter
    Lm Modifier_Letter
    Lo Other_Letter
    M Mark
    Mn Nonspacing_Mark
    Mc Spacing_Mark
    Me Enclosing_Mark
    N Number
    Nd Decimal_Number (also Digit)
    Nl Letter_Number
    No Other_Number
    P Punctuation (also Punct)
    Pc Connector_Punctuation
    Pd Dash_Punctuation
    Ps Open_Punctuation
    Pe Close_Punctuation
    Pi Initial_Punctuation
                (may behave like Ps or Pe depending on usage)
    Pf Final_Punctuation
                (may behave like Ps or Pe depending on usage)
    Po Other_Punctuation
    S Symbol
    Sm Math_Symbol
    Sc Currency_Symbol
    Sk Modifier_Symbol
    So Other_Symbol
    Z Separator
    Zs Space_Separator
    Zl Line_Separator
    Zp Paragraph_Separator
    C Other
    Cc Control (also Cntrl)
    Cf Format
    Cs Surrogate
    Co Private_Use
    Cn Unassigned
</code></pre>
<p> Single-letter properties match all characters in any of the two-letter sub-properties starting with the same letter. <code>&quot;LC&quot;</code> and <code>&quot;L&amp;&quot;</code> are special: both are aliases for the set consisting of everything matched by <code>&quot;Ll&quot;</code>, <code>&quot;Lu&quot;</code>, and <code>&quot;Lt&quot;</code>. </p>
<p> <i></i>Bidirectional Character Types <i></i> </p>
<p> Because scripts differ in their directionality (Hebrew and Arabic are written right to left, for example) Unicode supplies a <code>&quot;Bidi_Class&quot;</code> property. Some of the values this property can have are: </p>
<pre><code>    Value Meaning
    L Left-to-Right
    LRE Left-to-Right Embedding
    LRO Left-to-Right Override
    R Right-to-Left
    AL Arabic Letter
    RLE Right-to-Left Embedding
    RLO Right-to-Left Override
    PDF Pop Directional Format
    EN European Number
    ES European Separator
    ET European Terminator
    AN Arabic Number
    CS Common Separator
    NSM Non-Spacing Mark
    BN Boundary Neutral
    B Paragraph Separator
    S Segment Separator
    WS Whitespace
    ON Other Neutrals
</code></pre>
<p> This property is always written in the compound form. For example, <code>&quot;\p{Bidi_Class:R}&quot;</code> matches characters that are normally written right to left. Unlike the <code>&quot;General_Category&quot;</code> property, this property can have more values added in a future Unicode release. Those listed above comprised the complete set for many Unicode releases, but others were added in Unicode 6.3; you can always find what the current ones are in perluniprops. And &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr9/">http://www.unicode.org/reports/tr9/</a>&gt; describes how to use them. </p>
<p> <i></i>Scripts <i></i> </p>
<p> The world&#8217;s languages are written in many different scripts. This sentence (unless you&#8217;re reading it in translation) is written in Latin, while Russian is written in Cyrillic, and Greek is written in, well, Greek; Japanese mainly in Hiragana or Katakana. There are many more. </p>
<p> The Unicode <code>&quot;Script&quot;</code> and <code>&quot;Script_Extensions&quot;</code> properties give what script a given character is in. The <code>&quot;Script_Extensions&quot;</code> property is an improved version of <code>&quot;Script&quot;</code>, as demonstrated below. Either property can be specified with the compound form like <code>&quot;\p{Script=Hebrew}&quot;</code> (short: <code>&quot;\p{sc=hebr}&quot;</code>), or <code>&quot;\p{Script_Extensions=Javanese}&quot;</code> (short: <code>&quot;\p{scx=java}&quot;</code>). In addition, Perl furnishes shortcuts for all <code>&quot;Script_Extensions&quot;</code> property names. You can omit everything up through the equals (or colon), and simply write <code>&quot;\p{Latin}&quot;</code> or <code>&quot;\P{Cyrillic}&quot;</code>. (This is not true for <code>&quot;Script&quot;</code>, which is required to be written in the compound form. Prior to Perl v5.26, the single form returned the plain old <code>&quot;Script&quot;</code> version, but was changed because <code>&quot;Script_Extensions&quot;</code> gives better results.) </p>
<p> The difference between these two properties involves characters that are used in multiple scripts. For example the digits &#8216;0&#8217; through &#8216;9&#8217; are used in many parts of the world. These are placed in a script named <code>&quot;Common&quot;</code>. Other characters are used in just a few scripts. For example, the <code>&quot;KATAKANA-HIRAGANA DOUBLE HYPHEN&quot;</code> is used in both Japanese scripts, Katakana and Hiragana, but nowhere else. The <code>&quot;Script&quot;</code> property places all characters that are used in multiple scripts in the <code>&quot;Common&quot;</code> script, while the <code>&quot;Script_Extensions&quot;</code> property places those that are used in only a few scripts into each of those scripts; while still using <code>&quot;Common&quot;</code> for those used in many scripts. Thus both these match: </p>
<pre><code> &quot;0&quot; =~ /\p{sc=Common}/ # Matches
 &quot;0&quot; =~ /\p{scx=Common}/ # Matches
</code></pre>
<p> and only the first of these match: </p>
<pre><code> &quot;\N{KATAKANA-HIRAGANA DOUBLE HYPHEN}&quot; =~ /\p{sc=Common} # Matches
 &quot;\N{KATAKANA-HIRAGANA DOUBLE HYPHEN}&quot; =~ /\p{scx=Common} # No match
</code></pre>
<p> And only the last two of these match: </p>
<pre><code> &quot;\N{KATAKANA-HIRAGANA DOUBLE HYPHEN}&quot; =~ /\p{sc=Hiragana} # No match
 &quot;\N{KATAKANA-HIRAGANA DOUBLE HYPHEN}&quot; =~ /\p{sc=Katakana} # No match
 &quot;\N{KATAKANA-HIRAGANA DOUBLE HYPHEN}&quot; =~ /\p{scx=Hiragana} # Matches
 &quot;\N{KATAKANA-HIRAGANA DOUBLE HYPHEN}&quot; =~ /\p{scx=Katakana} # Matches
</code></pre>
<p> <code>&quot;Script_Extensions&quot;</code> is thus an improved <code>&quot;Script&quot;</code>, in which there are fewer characters in the <code>&quot;Common&quot;</code> script, and correspondingly more in other scripts. It is new in Unicode version 6.0, and its data are likely to change significantly in later releases, as things get sorted out. New code should probably be using <code>&quot;Script_Extensions&quot;</code> and not plain <code>&quot;Script&quot;</code>. If you compile perl with a Unicode release that doesn&#8217;t have <code>&quot;Script_Extensions&quot;</code>, the single form Perl extensions will instead refer to the plain <code>&quot;Script&quot;</code> property. If you compile with a version of Unicode that doesn&#8217;t have the <code>&quot;Script&quot;</code> property, these extensions will not be defined at all. </p>
<p> (Actually, besides <code>&quot;Common&quot;</code>, the <code>&quot;Inherited&quot;</code> script, contains characters that are used in multiple scripts. These are modifier characters which inherit the script value of the controlling character. Some of these are used in many scripts, and so go into <code>&quot;Inherited&quot;</code> in both <code>&quot;Script&quot;</code> and <code>&quot;Script_Extensions&quot;</code>. Others are used in just a few scripts, so are in <code>&quot;Inherited&quot;</code> in <code>&quot;Script&quot;</code>, but not in <code>&quot;Script_Extensions&quot;</code>.) </p>
<p> It is worth stressing that there are several different sets of digits in Unicode that are equivalent to 0-9 and are matchable by <code>&quot;\d&quot;</code> in a regular expression. If they are used in a single language only, they are in that language&#8217;s <code>&quot;Script&quot;</code> and <code>&quot;Script_Extensions&quot;</code>. If they are used in more than one script, they will be in <code>&quot;sc=Common&quot;</code>, but only if they are used in many scripts should they be in <code>&quot;scx=Common&quot;</code>. </p>
<p> The explanation above has omitted some detail; refer to UAX#24 ``Unicode Script Property&#8217;&#8216;: &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr24">http://www.unicode.org/reports/tr24</a>&gt;. </p>
<p> A complete list of scripts and their shortcuts is in perluniprops. </p>
<p> <i></i>Use of the &quot;Is&quot; Prefix <i></i> </p>
<p> For backward compatibility (with ancient Perl 5.6), all properties writable without using the compound form mentioned so far may have <code>&quot;Is&quot;</code> or <code>&quot;Is_&quot;</code> prepended to their name, so <code>&quot;\P{Is_Lu}&quot;</code>, for example, is equal to <code>&quot;\P{Lu}&quot;</code>, and <code>&quot;\p{IsScript:Arabic}&quot;</code> is equal to <code>&quot;\p{Arabic}&quot;</code>. </p>
<p> <i></i>Blocks <i></i> </p>
<p> In addition to <code>scripts</code>, Unicode also defines <code>blocks</code> of characters. The difference between scripts and blocks is that the concept of scripts is closer to natural languages, while the concept of blocks is more of an artificial grouping based on groups of Unicode characters with consecutive ordinal values. For example, the <code>&quot;Basic Latin&quot;</code> block is all the characters whose ordinals are between 0 and 127, inclusive; in other words, the <font SIZE="-1">ASCII</font> characters. The <code>&quot;Latin&quot;</code> script contains some letters from this as well as several other blocks, like <code>&quot;Latin-1 Supplement&quot;</code>, <code>&quot;Latin Extended-A&quot;</code>, <i>etc.</i>, but it does not contain all the characters from those blocks. It does not, for example, contain the digits 0-9, because those digits are shared across many scripts, and hence are in the <code>&quot;Common&quot;</code> script. </p>
<p> For more about scripts versus blocks, see UAX#24 ``Unicode Script Property&#8217;&#8216;: &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr24">http://www.unicode.org/reports/tr24</a>&gt; </p>
<p> The <code>&quot;Script_Extensions&quot;</code> or <code>&quot;Script&quot;</code> properties are likely to be the ones you want to use when processing natural language; the <code>&quot;Block&quot;</code> property may occasionally be useful in working with the nuts and bolts of Unicode. </p>
<p> Block names are matched in the compound form, like <code>&quot;\p{Block: Arrows}&quot;</code> or <code>&quot;\p{Blk=Hebrew}&quot;</code>. Unlike most other properties, only a few block names have a Unicode-defined short name. </p>
<p> Perl also defines single form synonyms for the block property in cases where these do not conflict with something else. But don&#8217;t use any of these, because they are unstable. Since these are Perl extensions, they are subordinate to official Unicode property names; Unicode doesn&#8217;t know nor care about Perl&#8217;s extensions. It may happen that a name that currently means the Perl extension will later be changed without warning to mean a different Unicode property in a future version of the perl interpreter that uses a later Unicode release, and your code would no longer work. The extensions are mentioned here for completeness: Take the block name and prefix it with one of: <code>&quot;In&quot;</code> (for example <code>&quot;\p{Blk=Arrows}&quot;</code> can currently be written as <code>&quot;\p{In_Arrows}&quot;</code>); or sometimes <code>&quot;Is&quot;</code> (like <code>&quot;\p{Is_Arrows}&quot;</code>); or sometimes no prefix at all (<code>&quot;\p{Arrows}&quot;</code>). As of this writing (Unicode 9.0) there are no conflicts with using the <code>&quot;In_&quot;</code> prefix, but there are plenty with the other two forms. For example, <code>&quot;\p{Is_Hebrew}&quot;</code> and <code>&quot;\p{Hebrew}&quot;</code> mean <code>&quot;\p{Script_Extensions=Hebrew}&quot;</code> which is <font SIZE="-1">NOT</font> the same thing as <code>&quot;\p{Blk=Hebrew}&quot;</code>. Our advice used to be to use the <code>&quot;In_&quot;</code> prefix as a single form way of specifying a block. But Unicode 8.0 added properties whose names begin with <code>&quot;In&quot;</code>, and it&#8217;s now clear that it&#8217;s only luck that&#8217;s so far prevented a conflict. Using <code>&quot;In&quot;</code> is only marginally less typing than <code>&quot;Blk:&quot;</code>, and the latter&#8217;s meaning is clearer anyway, and guaranteed to never conflict. So don&#8217;t take chances. Use <code>&quot;\p{Blk=foo}&quot;</code> for new code. And be sure that block is what you really really want to do. In most cases scripts are what you want instead. </p>
<p> A complete list of blocks is in perluniprops. </p>
<p> <i></i>Other Properties <i></i> </p>
<p> There are many more properties than the very basic ones described here. A complete list is in perluniprops. </p>
<p> Unicode defines all its properties in the compound form, so all single-form properties are Perl extensions. Most of these are just synonyms for the Unicode ones, but some are genuine extensions, including several that are in the compound form. And quite a few of these are actually recommended by Unicode (in &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr18">http://www.unicode.org/reports/tr18</a>&gt;). </p>
<p> This section gives some details on all extensions that aren&#8217;t just synonyms for compound-form Unicode properties (for those properties, you&#8217;ll have to refer to the Unicode Standard &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr44">http://www.unicode.org/reports/tr44</a>&gt;. </p>
<dl>
<dt>&quot;\p{All}&quot;</dt>
<dd> <p> This matches every possible code point. It is equivalent to <code>&quot;qr/./s&quot;</code>. Unlike all the other non-user-defined <code>&quot;\p{}&quot;</code> property matches, no warning is ever generated if this is property is matched against a non-Unicode code point (see ``Beyond Unicode code points&#8217;&#8216; below). </p>
 </dd>
<dt>&quot;\p{Alnum}&quot;</dt>
<dd> <p> This matches any <code>&quot;\p{Alphabetic}&quot;</code> or <code>&quot;\p{Decimal_Number}&quot;</code> character. </p>
 </dd>
<dt>&quot;\p{Any}&quot;</dt>
<dd> <p> This matches any of the 1_114_112 Unicode code points. It is a synonym for <code>&quot;\p{Unicode}&quot;</code>. </p>
 </dd>
<dt>&quot;\p{ASCII}&quot;</dt>
<dd> <p> This matches any of the 128 characters in the US-ASCII character set, which is a subset of Unicode. </p>
 </dd>
<dt>&quot;\p{Assigned}&quot;</dt>
<dd> <p> This matches any assigned code point; that is, any code point whose general category is not <code>&quot;Unassigned&quot;</code> (or equivalently, not <code>&quot;Cn&quot;</code>). </p>
 </dd>
<dt>&quot;\p{Blank}&quot;</dt>
<dd> <p> This is the same as <code>&quot;\h&quot;</code> and <code>&quot;\p{HorizSpace}&quot;</code>: A character that changes the spacing horizontally. </p>
 </dd>
<dt>&quot;\p{Decomposition_Type: Non_Canonical}&quot; (Short: &quot;\p{Dt=NonCanon}&quot;)</dt>
<dd> <p> Matches a character that has a non-canonical decomposition. </p>
<p> The ``Extended Grapheme Clusters (Logical characters)&#8216;&#8216; section above talked about canonical decompositions. However, many more characters have a different type of decomposition, a ``compatible&#8217;&#8216; or ``non-canonical&#8217;&#8216; decomposition. The sequences that form these decompositions are not considered canonically equivalent to the pre-composed character. An example is the <code>&quot;SUPERSCRIPT ONE&quot;</code>. It is somewhat like a regular digit 1, but not exactly; its decomposition into the digit 1 is called a ``compatible&#8217;&#8216; decomposition, specifically a ``super&#8217;&#8216; decomposition. There are several such compatibility decompositions (see &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr44">http://www.unicode.org/reports/tr44</a>&gt;), including one called ``compat&#8217;&#8216;, which means some miscellaneous type of decomposition that doesn&#8217;t fit into the other decomposition categories that Unicode has chosen. </p>
<p> Note that most Unicode characters don&#8217;t have a decomposition, so their decomposition type is <code>&quot;None&quot;</code>. </p>
<p> For your convenience, Perl has added the <code>&quot;Non_Canonical&quot;</code> decomposition type to mean any of the several compatibility decompositions. </p>
 </dd>
<dt>&quot;\p{Graph}&quot;</dt>
<dd> <p> Matches any character that is graphic. Theoretically, this means a character that on a printer would cause ink to be used. </p>
 </dd>
<dt>&quot;\p{HorizSpace}&quot;</dt>
<dd> <p> This is the same as <code>&quot;\h&quot;</code> and <code>&quot;\p{Blank}&quot;</code>: a character that changes the spacing horizontally. </p>
 </dd>
<dt>&quot;\p{In=*}&quot;</dt>
<dd> <p> This is a synonym for <code>&quot;\p{Present_In=*}&quot;</code> </p>
 </dd>
<dt>&quot;\p{PerlSpace}&quot;</dt>
<dd> <p> This is the same as <code>&quot;\s&quot;</code>, restricted to <font SIZE="-1">ASCII,</font> namely <code>&quot;[ \f\n\r\t]&quot;</code> and starting in Perl v5.18, a vertical tab. </p>
<p> Mnemonic: Perl&#8217;s (original) space </p>
 </dd>
<dt>&quot;\p{PerlWord}&quot;</dt>
<dd> <p> This is the same as <code>&quot;\w&quot;</code>, restricted to <font SIZE="-1">ASCII,</font> namely <code>&quot;[A-Za-z0-9_]&quot;</code> </p>
<p> Mnemonic: Perl&#8217;s (original) word. </p>
 </dd>
<dt>&quot;\p{Posix...}&quot;</dt>
<dd> <p> There are several of these, which are equivalents, using the <code>&quot;\p{}&quot;</code> notation, for Posix classes and are described in ``<font SIZE="-1">POSIX</font> Character Classes&#8217;&#8216; in perlrecharclass. </p>
 </dd>
<dt>&quot;\p{Present_In: *}&quot; (Short: &quot;\p{In=*}&quot;)</dt>
<dd> <p> This property is used when you need to know in what Unicode version(s) a character is. </p>
<p> The ``*&#8216;&#8216; above stands for some Unicode version number, such as <code>1.1</code> or <code>12.0</code>; or the ``*&#8216;&#8216; can also be <code>&quot;Unassigned&quot;</code>. This property will match the code points whose final disposition has been settled as of the Unicode release given by the version number; <code>&quot;\p{Present_In: Unassigned}&quot;</code> will match those code points whose meaning has yet to be assigned. </p>
<p> For example, <code>&quot;U+0041&quot;</code> <code>&quot;LATIN CAPITAL LETTER A&quot;</code> was present in the very first Unicode release available, which is <code>1.1</code>, so this property is true for all valid ``*&#8216;&#8216; versions. On the other hand, <code>&quot;U+1EFF&quot;</code> was not assigned until version 5.1 when it became <code>&quot;LATIN SMALL LETTER Y WITH LOOP&quot;</code>, so the only ``*&#8216;&#8216; that would match it are 5.1, 5.2, and later. </p>
<p> Unicode furnishes the <code>&quot;Age&quot;</code> property from which this is derived. The problem with Age is that a strict interpretation of it (which Perl takes) has it matching the precise release a code point&#8217;s meaning is introduced in. Thus <code>&quot;U+0041&quot;</code> would match only 1.1; and <code>&quot;U+1EFF&quot;</code> only 5.1. This is not usually what you want. </p>
<p> Some non-Perl implementations of the Age property may change its meaning to be the same as the Perl <code>&quot;Present_In&quot;</code> property; just be aware of that. </p>
<p> Another confusion with both these properties is that the definition is not that the code point has been <i>assigned</i>, but that the meaning of the code point has been <i>determined</i>. This is because 66 code points will always be unassigned, and so the <code>&quot;Age&quot;</code> for them is the Unicode version in which the decision to make them so was made. For example, <code>&quot;U+FDD0&quot;</code> is to be permanently unassigned to a character, and the decision to do that was made in version 3.1, so <code>&quot;\p{Age=3.1}&quot;</code> matches this character, as also does <code>&quot;\p{Present_In: 3.1}&quot;</code> and up. </p>
 </dd>
<dt>&quot;\p{Print}&quot;</dt>
<dd> <p> This matches any character that is graphical or blank, except controls. </p>
 </dd>
<dt>&quot;\p{SpacePerl}&quot;</dt>
<dd> <p> This is the same as <code>&quot;\s&quot;</code>, including beyond <font SIZE="-1">ASCII.</font> </p>
<p> Mnemonic: Space, as modified by Perl. (It doesn&#8217;t include the vertical tab until v5.18, which both the Posix standard and Unicode consider white space.) </p>
 </dd>
<dt>&quot;\p{Title}&quot; and &quot;\p{Titlecase}&quot;</dt>
<dd> <p> Under case-sensitive matching, these both match the same code points as <code>&quot;\p{General Category=Titlecase_Letter}&quot;</code> (<code>&quot;\p{gc=lt}&quot;</code>). The difference is that under <code>&quot;/i&quot;</code> caseless matching, these match the same as <code>&quot;\p{Cased}&quot;</code>, whereas <code>&quot;\p{gc=lt}&quot;</code> matches <code>&quot;\p{Cased_Letter&quot;</code>). </p>
 </dd>
<dt>&quot;\p{Unicode}&quot;</dt>
<dd> <p> This matches any of the 1_114_112 Unicode code points. <code>&quot;\p{Any}&quot;</code>. </p>
 </dd>
<dt>&quot;\p{VertSpace}&quot;</dt>
<dd> <p> This is the same as <code>&quot;\v&quot;</code>: A character that changes the spacing vertically. </p>
 </dd>
<dt>&quot;\p{Word}&quot;</dt>
<dd> <p> This is the same as <code>&quot;\w&quot;</code>, including over 100_000 characters beyond <font SIZE="-1">ASCII.</font> </p>
 </dd>
<dt>&quot;\p{XPosix...}&quot;</dt>
<dd> <p> There are several of these, which are the standard Posix classes extended to the full Unicode range. They are described in ``<font SIZE="-1">POSIX</font> Character Classes&#8217;&#8216; in perlrecharclass. </p>
 </dd></dl>
<h3>Wildcards in Property Values</h3>
<p> Starting in Perl 5.30, it is possible to do do something like this: </p>
<pre><code> qr!\p{numeric_value=/\A[0-5]\z/}!
</code></pre>
<p> or, by abbreviating and adding <code>&quot;/x&quot;</code>, </p>
<pre><code> qr! \p{nv= /(?x) \A [0-5] \z / }!
</code></pre>
<p> This matches all code points whose numeric value is one of 0, 1, 2, 3, 4, or 5. This particular example could instead have been written as </p>
<pre><code> qr! \A [ \p{nv=0}\p{nv=1}\p{nv=2}\p{nv=3}\p{nv=4}\p{nv=5} ] \z !xx
</code></pre>
<p> in earlier perls, so in this case this feature just makes things easier and shorter to write. If we hadn&#8217;t included the <code>&quot;\A&quot;</code> and <code>&quot;\z&quot;</code>, these would have matched things like <code>&quot;1/2&quot;</code> because that contains a 1 (as well as a 2). As written, it matches things like subscripts that have these numeric values. If we only wanted the decimal digits with those numeric values, we could say, </p>
<pre><code> qr! (?[ \d &amp; \p{nv=/[0-5]/ ]) }!x
</code></pre>
<p> The <code>&quot;\d&quot;</code> gets rid of needing to anchor the pattern, since it forces the result to only match <code>&quot;[0-9]&quot;</code>, and the <code>&quot;[0-5]&quot;</code> further restricts it. </p>
<p> The text in the above examples enclosed between the <code>&quot;/&quot;</code> characters can be just about any regular expression. It is independent of the main pattern, so doesn&#8217;t share any capturing groups, <i>etc</i>. The delimiters for it must be <font SIZE="-1">ASCII</font> punctuation, but it may <font SIZE="-1">NOT</font> be delimited by <code>&quot;{&quot;</code>, nor <code>&quot;}&quot;</code> nor contain a literal <code>&quot;}&quot;</code>, as that delimits the end of the enclosing <code>&quot;\p{}&quot;</code>. Like any pattern, certain other delimiters are terminated by their mirror images. These are <code>&quot;(&quot;</code>, <code>&quot;&quot;[&quot;</code>&quot;, and <code>&quot;&lt;&quot;</code>. If the delimiter is any of <code>&quot;-&quot;</code>, <code>&quot;_&quot;</code>, <code>&quot;+&quot;</code>, or <code>&quot;\&quot;</code>, or is the same delimiter as is used for the enclosing pattern, it must be be preceded by a backslash escape, both fore and aft. </p>
<p> Beware of using <code>&quot;$&quot;</code> to indicate to match the end of the string. It can too easily be interpreted as being a punctuation variable, like <code>$/</code>. </p>
<p> No modifiers may follow the final delimiter. Instead, use ``(?adlupimnsx-imnsx)&#8216;&#8216; in perlre and/or ``(?adluimnsx-imnsx:pattern)&#8216;&#8216; in perlre to specify modifiers. </p>
<p> This feature is not available when the left-hand side is prefixed by <code>&quot;Is_&quot;</code>, nor for any form that is marked as ``Discouraged&#8217;&#8216; in ``Discouraged&#8217;&#8216; in perluniprops. </p>
<p> Perl wraps your pattern with <code>&quot;(?iaa: ... )&quot;</code>. This is because nothing outside <font SIZE="-1">ASCII</font> can match the Unicode property values available in this release, and they should match caselessly. If your pattern has a syntax error, this wrapping will be shown in the error message, even though you didn&#8217;t specify it yourself. This could be confusing if you don&#8217;t know about this. </p>
<p> This experimental feature has been added to begin to implement &lt;<a rel="nofollow" href="https://www.unicode.org/reports/tr18/#Wildcard_Properties">https://www.unicode.org/reports/tr18/#Wildcard_Properties</a>&gt;. Using it will raise a (default-on) warning in the <code>&quot;experimental::uniprop_wildcards&quot;</code> category. We reserve the right to change its operation as we gain experience. </p>
<p> Your subpattern can be just about anything, but for it to have some utility, it should match when called with either or both of a) the full name of the property value with underscores (and/or spaces in the Block property) and some things uppercase; or b) the property value in all lowercase with spaces and underscores squeezed out. For example, </p>
<pre><code> qr!\p{Blk=/Old I.*/}!
 qr!\p{Blk=/oldi.*/}!
</code></pre>
<p> would match the same things. </p>
<p> A warning is issued if none of the legal values for a property are matched by your pattern. It&#8217;s likely that a future release will raise a warning if your pattern ends up causing every possible code point to match. </p>
<p> Another example that shows that within <code>&quot;\p{...}&quot;</code>, <code>&quot;/x&quot;</code> isn&#8217;t needed to have spaces: </p>
<pre><code> qr!\p{scx= /Hebrew|Greek/ }!
</code></pre>
<p> To be safe, we should have anchored the above example, to prevent matches for something like <code>&quot;Hebrew_Braile&quot;</code>, but there aren&#8217;t any script names like that. </p>
<p> There are certain properties that it doesn&#8217;t currently work with. These are: </p>
<pre><code> Bidi Mirroring Glyph
 Bidi Paired Bracket
 Case Folding
 Decomposition Mapping
 Equivalent Unified Ideograph
 Name
 Name Alias
 Lowercase Mapping
 NFKC Case Fold
 Titlecase Mapping
 Uppercase Mapping
</code></pre>
<p> Nor is the <code>&quot;@</code>unicode_property <code>@&quot;</code> form implemented. </p>
<p> Here&#8217;s a complete example of matching <font SIZE="-1">IPV4</font> internet protocol addresses in any (single) script </p>
<pre><code> no warnings 'experimental::script_run';
 no warnings 'experimental::regex_sets';
 no warnings 'experimental::uniprop_wildcards';
 # Can match a substring, so this intermediate regex needs to have
 # context or anchoring in its final use. Using nt=de yields decimal
 # digits. When specifying a subset of these, we must include \d to
 # prevent things like U+00B2 SUPERSCRIPT TWO from matching
 my $zero_through_255 =
  qr/ \b (*sr: # All from same sript
            (?[ \p{nv=0} &amp; \d ])* # Optional leading zeros
        ( # Then one of:
                                  \d{1,2} # 0 - 99
            | (?[ \p{nv=1} &amp; \d ]) \d{2} # 100 - 199
            | (?[ \p{nv=2} &amp; \d ])
               ( (?[ \p{nv=:[0-4]:} &amp; \d ]) \d # 200 - 249
                | (?[ \p{nv=5} &amp; \d ])
                  (?[ \p{nv=:[0-5]:} &amp; \d ]) # 250 - 255
               )
        )
      )
    \b
  /x;
 my $ipv4 = qr/ \A (*sr: $zero_through_255
                         (?: [.] $zero_through_255 ) {3}
                   )
                \z
            /x;
</code></pre>
<h3>User-Defined Character Properties</h3>
<p> You can define your own binary character properties by defining subroutines whose names begin with <code>&quot;In&quot;</code> or <code>&quot;Is&quot;</code>. (The experimental feature ``(?[ ])&#8216;&#8216; in perlre provides an alternative which allows more complex definitions.) The subroutines can be defined in any package. The user-defined properties can be used in the regular expression <code>&quot;\p{}&quot;</code> and <code>&quot;\P{}&quot;</code> constructs; if you are using a user-defined property from a package other than the one you are in, you must specify its package in the <code>&quot;\p{}&quot;</code> or <code>&quot;\P{}&quot;</code> construct. </p>
<pre><code>    # assuming property Is_Foreign defined in Lang::
    package main; # property package name required
    if ($txt =~ /\p{Lang::IsForeign}+/) { ... }
    package Lang; # property package name not required
    if ($txt =~ /\p{IsForeign}+/) { ... }
</code></pre>
<p> Note that the effect is compile-time and immutable once defined. However, the subroutines are passed a single parameter, which is 0 if case-sensitive matching is in effect and non-zero if caseless matching is in effect. The subroutine may return different values depending on the value of the flag, and one set of values will immutably be in effect for all case-sensitive matches, and the other set for all case-insensitive matches. </p>
<p> Note that if the regular expression is tainted, then Perl will die rather than calling the subroutine when the name of the subroutine is determined by the tainted data. </p>
<p> The subroutines must return a specially-formatted string, with one or more newline-separated lines. Each line must be one of the following: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A single hexadecimal number denoting a code point to include. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Two hexadecimal numbers separated by horizontal whitespace (space or tabular characters) denoting a range of code points to include. The second number must not be smaller than the first. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Something to include, prefixed by <code>&quot;+&quot;</code>: a built-in character property (prefixed by <code>&quot;utf8::&quot;</code>) or a fully qualified (including package name) user-defined character property, to represent all the characters in that property; two hexadecimal code points for a range; or a single hexadecimal code point. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Something to exclude, prefixed by <code>&quot;-&quot;</code>: an existing character property (prefixed by <code>&quot;utf8::&quot;</code>) or a fully qualified (including package name) user-defined character property, to represent all the characters in that property; two hexadecimal code points for a range; or a single hexadecimal code point. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Something to negate, prefixed <code>&quot;!&quot;</code>: an existing character property (prefixed by <code>&quot;utf8::&quot;</code>) or a fully qualified (including package name) user-defined character property, to represent all the characters in that property; two hexadecimal code points for a range; or a single hexadecimal code point. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Something to intersect with, prefixed by <code>&quot;&amp;&quot;</code>: an existing character property (prefixed by <code>&quot;utf8::&quot;</code>) or a fully qualified (including package name) user-defined character property, for all the characters except the characters in the property; two hexadecimal code points for a range; or a single hexadecimal code point. </p>
 </dd></dl>
<p> For example, to define a property that covers both the Japanese syllabaries (hiragana and katakana), you can define </p>
<pre><code>    sub InKana {
        return &lt;&lt;END;
    3040\t309F
    30A0\t30FF
    END
    }
</code></pre>
<p> Imagine that the here-doc end marker is at the beginning of the line. Now you can use <code>&quot;\p{InKana}&quot;</code> and <code>&quot;\P{InKana}&quot;</code>. </p>
<p> You could also have used the existing block property names: </p>
<pre><code>    sub InKana {
        return &lt;&lt;'END';
    +utf8::InHiragana
    +utf8::InKatakana
    END
    }
</code></pre>
<p> Suppose you wanted to match only the allocated characters, not the raw block ranges: in other words, you want to remove the unassigned characters: </p>
<pre><code>    sub InKana {
        return &lt;&lt;'END';
    +utf8::InHiragana
    +utf8::InKatakana
    -utf8::IsCn
    END
    }
</code></pre>
<p> The negation is useful for defining (surprise!) negated classes. </p>
<pre><code>    sub InNotKana {
        return &lt;&lt;'END';
    !utf8::InHiragana
    -utf8::InKatakana
    +utf8::IsCn
    END
    }
</code></pre>
<p> This will match all non-Unicode code points, since every one of them is not in Kana. You can use intersection to exclude these, if desired, as this modified example shows: </p>
<pre><code>    sub InNotKana {
        return &lt;&lt;'END';
    !utf8::InHiragana
    -utf8::InKatakana
    +utf8::IsCn
    &amp;utf8::Any
    END
    }
</code></pre>
<p> <code>&amp;utf8::Any</code> must be the last line in the definition. </p>
<p> Intersection is used generally for getting the common characters matched by two (or more) classes. It&#8217;s important to remember not to use <code>&quot;&amp;&quot;</code> for the first set; that would be intersecting with nothing, resulting in an empty set. (Similarly using <code>&quot;-&quot;</code> for the first set does nothing). </p>
<p> Unlike non-user-defined <code>&quot;\p{}&quot;</code> property matches, no warning is ever generated if these properties are matched against a non-Unicode code point (see ``Beyond Unicode code points&#8217;&#8216; below).  </p>
<h3>User-Defined Case Mappings (for serious hackers only)</h3>
<p> <code>This feature has been removed as of Perl 5.16.</code> The <font SIZE="-1">CPAN</font> module <code>&quot;Unicode::Casing&quot;</code> provides better functionality without the drawbacks that this feature had. If you are using a Perl earlier than 5.16, this feature was most fully documented in the 5.14 version of this pod: &lt;<a rel="nofollow" href="http://perldoc.perl.org/5.14.0/perlunicode.html#User-Defined-Case-Mappings-%28for-serious-hackers-only%29">http://perldoc.perl.org/5.14.0/perlunicode.html#User-Defined-Case-Mappings-%28for-serious-hackers-only%29</a>&gt;  </p>
<h3>Character Encodings for Input and Output</h3>
<p> See Encode.  </p>
<h3>Unicode Regular Expression Support Level</h3>
<p> The following list of Unicode supported features for regular expressions describes all features currently directly supported by core Perl. The references to &quot;Level <i>N</i>&quot; and the section numbers refer to UTS#18 ``Unicode Regular Expressions&#8217;&#8216; &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr18">http://www.unicode.org/reports/tr18</a>&gt;, version 18, October 2016. </p>
<p> <i>Level 1 &#8211; Basic Unicode Support</i> </p>
<pre><code> RL1.1 Hex Notation - Done [1]
 RL1.2 Properties - Done [2]
 RL1.2a Compatibility Properties - Done [3]
 RL1.3 Subtraction and Intersection - Experimental [4]
 RL1.4 Simple Word Boundaries - Done [5]
 RL1.5 Simple Loose Matches - Done [6]
 RL1.6 Line Boundaries - Partial [7]
 RL1.7 Supplementary Code Points - Done [8]
</code></pre>
<dl>
<dt>[1] &quot;\N{U+...}&quot; and &quot;\x{...}&quot;</dt>
<dd>  </dd>
<dt>[2] &quot;\p{...}&quot; &quot;\P{...}&quot;. This requirement is for a minimal list of properties. Perl supports these and all other Unicode character properties, as R2.7 asks (see &quot;Unicode Character Properties&quot; above).</dt>
<dd>  </dd>
<dt>[3] Perl has &quot;\d&quot; &quot;\D&quot; &quot;\s&quot; &quot;\S&quot; &quot;\w&quot; &quot;\W&quot; &quot;\X&quot; &quot;[:<i>prop</i>:]&quot; &quot;[:^<i>prop</i>:]&quot;, plus all the properties specified by &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr18/#Compatibility_Properties">http://www.unicode.org/reports/tr18/#Compatibility_Properties</a>&gt;. These are described above in &quot;Other Properties&quot;</dt>
<dd>  </dd>
<dt>[4]</dt>
<dd> <p> The experimental feature <code>&quot;(?[...])&quot;</code> starting in v5.18 accomplishes this. </p>
<p> See ``(?[ ])&#8216;&#8216; in perlre. If you don&#8217;t want to use an experimental feature, you can use one of the following: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Regular expression lookahead </p>
<p> You can mimic class subtraction using lookahead. For example, what UTS#18 might write as </p>
<pre><code>    [{Block=Greek}-[{UNASSIGNED}]]
</code></pre>
<p> in Perl can be written as: </p>
<pre><code>    (?!\p{Unassigned})\p{Block=Greek}
    (?=\p{Assigned})\p{Block=Greek}
</code></pre>
<p> But in this particular example, you probably really want </p>
<pre><code>    \p{Greek}
</code></pre>
<p> which will match assigned characters known to be part of the Greek script. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CPAN</font> module <code>&quot;Unicode::Regex::Set&quot;</code> </p>
<p> It does implement the full UTS#18 grouping, intersection, union, and removal (subtraction) syntax. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ``User-Defined Character Properties&#8217;&#8216; </p>
<p> <code>&quot;+&quot;</code> for union, <code>&quot;-&quot;</code> for removal (set-difference), <code>&quot;&amp;&quot;</code> for intersection </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>[5] &quot;\b&quot; &quot;\B&quot; meet most, but not all, the details of this requirement, but &quot;\b{wb}&quot; and &quot;\B{wb}&quot; do, as well as the stricter R2.3.</dt>
<dd>  </dd>
<dt>[6]</dt>
<dd> <p> Note that Perl does Full case-folding in matching, not Simple: </p>
<p> For example <code>&quot;U+1F88&quot;</code> is equivalent to <code>&quot;U+1F00 U+03B9&quot;</code>, instead of just <code>&quot;U+1F80&quot;</code>. This difference matters mainly for certain Greek capital letters with certain modifiers: the Full case-folding decomposes the letter, while the Simple case-folding would map it to a single character. </p>
 </dd>
<dt>[7]</dt>
<dd> <p> The reason this is considered to be only partially implemented is that Perl has <code>&quot;qr/\b{lb}/&quot;</code> and <code>&quot;Unicode::LineBreak&quot;</code> that are conformant with UAX#14 ``Unicode Line Breaking Algorithm&#8217;&#8216; &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr14">http://www.unicode.org/reports/tr14</a>&gt;. The regular expression construct provides default behavior, while the heavier-weight module provides customizable line breaking. </p>
<p> But Perl treats <code>&quot;\n&quot;</code> as the start- and end-line delimiter, whereas Unicode specifies more characters that should be so-interpreted. </p>
<p> These are: </p>
<pre><code> VT U+000B (\v in C)
 FF U+000C (\f)
 CR U+000D (\r)
 NEL U+0085
 LS U+2028
 PS U+2029
</code></pre>
<p> <code>&quot;^&quot;</code> and <code>&quot;$&quot;</code> in regular expression patterns are supposed to match all these, but don&#8217;t. These characters also don&#8217;t, but should, affect <code>&quot;&lt;&gt;&quot;</code> <code>$.</code>, and script line numbers. </p>
<p> Also, lines should not be split within <code>&quot;CRLF&quot;</code> (i.e. there is no empty line between <code>&quot;\r&quot;</code> and <code>&quot;\n&quot;</code>). For <code>&quot;CRLF&quot;</code>, try the <code>&quot;:crlf&quot;</code> layer (see PerlIO). </p>
 </dd>
<dt>[8] <font SIZE="-1">UTF-8/UTF-EBDDIC</font> used in Perl allows not only &quot;U+10000&quot; to &quot;U+10FFFF&quot; but also beyond &quot;U+10FFFF&quot;</dt>
<dd>  </dd></dl>
<p> <i>Level 2 &#8211; Extended Unicode Support</i> </p>
<pre><code> RL2.1 Canonical Equivalents - Retracted [9]
                                           by Unicode
 RL2.2 Extended Grapheme Clusters - Partial [10]
 RL2.3 Default Word Boundaries - Done [11]
 RL2.4 Default Case Conversion - Done
 RL2.5 Name Properties - Done
 RL2.6 Wildcards in Property Values - Partial [12]
 RL2.7 Full Properties - Done
</code></pre>
<dl>
<dt>[9] Unicode has rewritten this portion of UTS#18 to say that getting canonical equivalence (see UAX#15 &quot;Unicode Normalization Forms&quot; &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr15">http://www.unicode.org/reports/tr15</a>&gt;) is basically to be done at the programmer level. Use <font SIZE="-1">NFD</font> to write both your regular expressions and text to match them against (you can use Unicode::Normalize).</dt>
<dd>  </dd>
<dt>[10] Perl has &quot;\X&quot; and &quot;\b{gcb}&quot; but we don&#8217;t have a &quot;Grapheme Cluster Mode&quot;.</dt>
<dd>  </dd>
<dt>[11] see UAX#29 &quot;Unicode Text Segmentation&quot; &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr29">http://www.unicode.org/reports/tr29</a>&gt;,</dt>
<dd>  </dd>
<dt>[12] see &quot;Wildcards in Property Values&quot; above.</dt>
<dd>  </dd></dl>
<p> <i>Level 3 &#8211; Tailored Support</i> </p>
<pre><code> RL3.1 Tailored Punctuation - Missing
 RL3.2 Tailored Grapheme Clusters - Missing [13]
 RL3.3 Tailored Word Boundaries - Missing
 RL3.4 Tailored Loose Matches - Retracted by Unicode
 RL3.5 Tailored Ranges - Retracted by Unicode
 RL3.6 Context Matching - Partial [14]
 RL3.7 Incremental Matches - Missing
 RL3.8 Unicode Set Sharing - Retracted by Unicode
 RL3.9 Possible Match Sets - Missing
 RL3.10 Folded Matching - Retracted by Unicode
 RL3.11 Submatchers - Partial [15]
</code></pre>
<dl>
<dt>[13] Perl has Unicode::Collate, but it isn&#8217;t integrated with regular expressions. See UTS#10 &quot;Unicode Collation Algorithms&quot; &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr10">http://www.unicode.org/reports/tr10</a>&gt;.</dt>
<dd>  </dd>
<dt>[14] Perl has &quot;(?&lt;=x)&quot; and &quot;(?=x)&quot;, but this requirement says that it should be possible to specify that matches may occur only in a substring with the lookaheads and lookbehinds able to see beyond that matchable portion.</dt>
<dd>  </dd>
<dt>[15] Perl has user-defined properties (&quot;User-Defined Character Properties&quot;) to look at single code points in ways beyond Unicode, and it might be possible, though probably not very clean, to use code blocks and things like &quot;(?(DEFINE)...)&quot; (see perlre) to do more specialized matching.</dt>
<dd>  </dd></dl>
<h3>Unicode Encodings</h3>
<p> Unicode characters are assigned to <i>code points</i>, which are abstract numbers. To use these numbers, various encodings are needed. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">UTF-8</font> </p>
<p> <font SIZE="-1">UTF-8</font> is a variable-length (1 to 4 bytes), byte-order independent encoding. In most of Perl&#8217;s documentation, including elsewhere in this document, the term ``<font SIZE="-1">UTF-8&#8217;&#8216;</font> means also ``UTF-EBCDIC&#8217;&#8216;. But in this section, ``<font SIZE="-1">UTF-8&#8217;&#8216;</font> refers only to the encoding used on <font SIZE="-1">ASCII</font> platforms. It is a superset of 7-bit US-ASCII, so anything encoded in <font SIZE="-1">ASCII</font> has the identical representation when encoded in <font SIZE="-1">UTF-8.</font> </p>
<p> The following table is from Unicode 3.2. </p>
<pre><code> Code Points 1st Byte 2nd Byte 3rd Byte 4th Byte
   U+0000..U+007F 00..7F
   U+0080..U+07FF * C2..DF 80..BF
   U+0800..U+0FFF E0 * A0..BF 80..BF
   U+1000..U+CFFF E1..EC 80..BF 80..BF
   U+D000..U+D7FF ED 80..9F 80..BF
   U+D800..U+DFFF +++++ utf16 surrogates, not legal utf8 +++++
   U+E000..U+FFFF EE..EF 80..BF 80..BF
  U+10000..U+3FFFF F0 * 90..BF 80..BF 80..BF
  U+40000..U+FFFFF F1..F3 80..BF 80..BF 80..BF
 U+100000..U+10FFFF F4 80..8F 80..BF 80..BF
</code></pre>
<p> Note the gaps marked by ``*&#8216;&#8216; before several of the byte entries above. These are caused by legal <font SIZE="-1">UTF-8</font> avoiding non-shortest encodings: it is technically possible to UTF-8-encode a single code point in different ways, but that is explicitly forbidden, and the shortest possible encoding should always be used (and that is what Perl does). </p>
<p> Another way to look at it is via bits: </p>
<pre><code>                Code Points 1st Byte 2nd Byte 3rd Byte 4th Byte
                   0aaaaaaa 0aaaaaaa
           00000bbbbbaaaaaa 110bbbbb 10aaaaaa
           ccccbbbbbbaaaaaa 1110cccc 10bbbbbb 10aaaaaa
 00000dddccccccbbbbbbaaaaaa 11110ddd 10cccccc 10bbbbbb 10aaaaaa
</code></pre>
<p> As you can see, the continuation bytes all begin with <code>&quot;10&quot;</code>, and the leading bits of the start byte tell how many bytes there are in the encoded character. </p>
<p> The original <font SIZE="-1">UTF-8</font> specification allowed up to 6 bytes, to allow encoding of numbers up to <code>&quot;0x7FFF_FFFF&quot;</code>. Perl continues to allow those, and has extended that up to 13 bytes to encode code points up to what can fit in a 64-bit word. However, Perl will warn if you output any of these as being non-portable; and under strict <font SIZE="-1">UTF-8</font> input protocols, they are forbidden. In addition, it is now illegal to use a code point larger than what a signed integer variable on your system can hold. On 32-bit <font SIZE="-1">ASCII</font> systems, this means <code>&quot;0x7FFF_FFFF&quot;</code> is the legal maximum (much higher on 64-bit systems). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> UTF-EBCDIC </p>
<p> Like <font SIZE="-1">UTF-8,</font> but EBCDIC-safe, in the way that <font SIZE="-1">UTF-8</font> is ASCII-safe. This means that all the basic characters (which includes all those that have <font SIZE="-1">ASCII</font> equivalents (like <code>&quot;A&quot;</code>, <code>&quot;0&quot;</code>, <code>&quot;%&quot;</code>, <i>etc.</i>) are the same in both <font SIZE="-1">EBCDIC</font> and UTF-EBCDIC.) </p>
<p> UTF-EBCDIC is used on <font SIZE="-1">EBCDIC</font> platforms. It generally requires more bytes to represent a given code point than <font SIZE="-1">UTF-8</font> does; the largest Unicode code points take 5 bytes to represent (instead of 4 in <font SIZE="-1">UTF-8</font>), and, extended for 64-bit words, it uses 14 bytes instead of 13 bytes in <font SIZE="-1">UTF-8.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">UTF-16, UTF-16BE, UTF-16LE,</font> Surrogates, and <code>&quot;BOM&quot;</code>&#8216;s (Byte Order Marks) </p>
<p> The followings items are mostly for reference and general Unicode knowledge, Perl doesn&#8217;t use these constructs internally. </p>
<p> Like <font SIZE="-1">UTF-8, UTF-16</font> is a variable-width encoding, but where <font SIZE="-1">UTF-8</font> uses 8-bit code units, <font SIZE="-1">UTF-16</font> uses 16-bit code units. All code points occupy either 2 or 4 bytes in <font SIZE="-1">UTF-16:</font> code points <code>&quot;U+0000..U+FFFF&quot;</code> are stored in a single 16-bit unit, and code points <code>&quot;U+10000..U+10FFFF&quot;</code> in two 16-bit units. The latter case is using <i>surrogates</i>, the first 16-bit unit being the <i>high surrogate</i>, and the second being the <i>low surrogate</i>. </p>
<p> Surrogates are code points set aside to encode the <code>&quot;U+10000..U+10FFFF&quot;</code> range of Unicode code points in pairs of 16-bit units. The <i>high surrogates</i> are the range <code>&quot;U+D800..U+DBFF&quot;</code> and the <i>low surrogates</i> are the range <code>&quot;U+DC00..U+DFFF&quot;</code>. The surrogate encoding is </p>
<pre><code>    $hi = ($uni - 0x10000) / 0x400 + 0xD800;
    $lo = ($uni - 0x10000) % 0x400 + 0xDC00;
</code></pre>
<p> and the decoding is </p>
<pre><code>    $uni = 0x10000 + ($hi - 0xD800) * 0x400 + ($lo - 0xDC00);
</code></pre>
<p> Because of the 16-bitness, <font SIZE="-1">UTF-16</font> is byte-order dependent. <font SIZE="-1">UTF-16</font> itself can be used for in-memory computations, but if storage or transfer is required either <font SIZE="-1">UTF-16BE</font> (big-endian) or <font SIZE="-1">UTF-16LE</font> (little-endian) encodings must be chosen. </p>
<p> This introduces another problem: what if you just know that your data is <font SIZE="-1">UTF-16,</font> but you don&#8217;t know which endianness? Byte Order Marks, or <code>&quot;BOM&quot;</code>&#8216;s, are a solution to this. A special character has been reserved in Unicode to function as a byte order marker: the character with the code point <code>&quot;U+FEFF&quot;</code> is the <code>&quot;BOM&quot;</code>. </p>
<p> The trick is that if you read a <code>&quot;BOM&quot;</code>, you will know the byte order, since if it was written on a big-endian platform, you will read the bytes <code>&quot;0xFE 0xFF&quot;</code>, but if it was written on a little-endian platform, you will read the bytes <code>&quot;0xFF 0xFE&quot;</code>. (And if the originating platform was writing in <font SIZE="-1">ASCII</font> platform <font SIZE="-1">UTF-8,</font> you will read the bytes <code>&quot;0xEF 0xBB 0xBF&quot;</code>.) </p>
<p> The way this trick works is that the character with the code point <code>&quot;U+FFFE&quot;</code> is not supposed to be in input streams, so the sequence of bytes <code>&quot;0xFF 0xFE&quot;</code> is unambiguously &quot;<code>&quot;BOM&quot;</code>, represented in little-endian format&quot; and cannot be <code>&quot;U+FFFE&quot;</code>, represented in big-endian format&quot;. </p>
<p> Surrogates have no meaning in Unicode outside their use in pairs to represent other code points. However, Perl allows them to be represented individually internally, for example by saying <code>&quot;chr(0xD801)&quot;</code>, so that all code points, not just those valid for open interchange, are representable. Unicode does define semantics for them, such as their <code>&quot;General_Category&quot;</code> is <code>&quot;Cs&quot;</code>. But because their use is somewhat dangerous, Perl will warn (using the warning category <code>&quot;surrogate&quot;</code>, which is a sub-category of <code>&quot;utf8&quot;</code>) if an attempt is made to do things like take the lower case of one, or match case-insensitively, or to output them. (But don&#8217;t try this on Perls before 5.14.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">UTF-32, UTF-32BE, UTF-32LE</font> </p>
<p> The <font SIZE="-1">UTF-32</font> family is pretty much like the <font SIZE="-1">UTF-16</font> family, except that the units are 32-bit, and therefore the surrogate scheme is not needed. <font SIZE="-1">UTF-32</font> is a fixed-width encoding. The <code>&quot;BOM&quot;</code> signatures are <code>&quot;0x00 0x00 0xFE 0xFF&quot;</code> for <font SIZE="-1">BE</font> and <code>&quot;0xFF 0xFE 0x00 0x00&quot;</code> for <font SIZE="-1">LE.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">UCS-2, UCS-4</font> </p>
<p> Legacy, fixed-width encodings defined by the <font SIZE="-1">ISO 10646</font> standard. <font SIZE="-1">UCS-2</font> is a 16-bit encoding. Unlike <font SIZE="-1">UTF-16, UCS-2</font> is not extensible beyond <code>&quot;U+FFFF&quot;</code>, because it does not use surrogates. <font SIZE="-1">UCS-4</font> is a 32-bit encoding, functionally identical to <font SIZE="-1">UTF-32</font> (the difference being that <font SIZE="-1">UCS-4</font> forbids neither surrogates nor code points larger than <code>&quot;0x10_FFFF&quot;</code>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">UTF-7</font> </p>
<p> A seven-bit safe (non-eight-bit) encoding, which is useful if the transport or storage is not eight-bit safe. Defined by <font SIZE="-1">RFC 2152.</font> </p>
 </dd></dl>
<h3>Noncharacter code points</h3>
<p> 66 code points are set aside in Unicode as ``noncharacter code points&#8217;&#8216;. These all have the <code>&quot;Unassigned&quot;</code> (<code>&quot;Cn&quot;</code>) <code>&quot;General_Category&quot;</code>, and no character will ever be assigned to any of them. They are the 32 code points between <code>&quot;U+FDD0&quot;</code> and <code>&quot;U+FDEF&quot;</code> inclusive, and the 34 code points: </p>
<pre><code> U+FFFE U+FFFF
 U+1FFFE U+1FFFF
 U+2FFFE U+2FFFF
 ...
 U+EFFFE U+EFFFF
 U+FFFFE U+FFFFF
 U+10FFFE U+10FFFF
</code></pre>
<p> Until Unicode 7.0, the noncharacters were &quot;<code>forbidden</code> for use in open interchange of Unicode text data&quot;, so that code that processed those streams could use these code points as sentinels that could be mixed in with character data, and would always be distinguishable from that data. (Emphasis above and in the next paragraph are added in this document.) </p>
<p> Unicode 7.0 changed the wording so that they are &quot;<code>not recommended</code> for use in open interchange of Unicode text data&quot;. The 7.0 Standard goes on to say: </p>
<dl>
<dd> <p> &quot;If a noncharacter is received in open interchange, an application is not required to interpret it in any way. It is good practice, however, to recognize it as a noncharacter and to take appropriate action, such as replacing it with <code>&quot;U+FFFD&quot;</code> replacement character, to indicate the problem in the text. It is not recommended to simply delete noncharacter code points from such text, because of the potential security issues caused by deleting uninterpreted characters. (See conformance clause C7 in Section 3.2, Conformance Requirements, and Unicode Technical Report #36, ``Unicode Security Considerations&#8217;&#8216; &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr36/#Substituting_for_Ill_Formed_Subsequences">http://www.unicode.org/reports/tr36/#Substituting_for_Ill_Formed_Subsequences</a>&gt;).&quot; </p>
 </dd></dl>
<p> This change was made because it was found that various commercial tools like editors, or for things like source code control, had been written so that they would not handle program files that used these code points, effectively precluding their use almost entirely! And that was never the intent. They&#8217;ve always been meant to be usable within an application, or cooperating set of applications, at will. </p>
<p> If you&#8217;re writing code, such as an editor, that is supposed to be able to handle any Unicode text data, then you shouldn&#8217;t be using these code points yourself, and instead allow them in the input. If you need sentinels, they should instead be something that isn&#8217;t legal Unicode. For <font SIZE="-1">UTF-8</font> data, you can use the bytes 0xC1 and 0xC2 as sentinels, as they never appear in well-formed <font SIZE="-1">UTF-8.</font> (There are equivalents for UTF-EBCDIC). You can also store your Unicode code points in integer variables and use negative values as sentinels. </p>
<p> If you&#8217;re not writing such a tool, then whether you accept noncharacters as input is up to you (though the Standard recommends that you not). If you do strict input stream checking with Perl, these code points continue to be forbidden. This is to maintain backward compatibility (otherwise potential security holes could open up, as an unsuspecting application that was written assuming the noncharacters would be filtered out before getting to it, could now, without warning, start getting them). To do strict checking, you can use the layer <code>&quot;:encoding(&#8216;UTF-8&#8217;)&quot;</code>. </p>
<p> Perl continues to warn (using the warning category <code>&quot;nonchar&quot;</code>, which is a sub-category of <code>&quot;utf8&quot;</code>) if an attempt is made to output noncharacters.  </p>
<h3>Beyond Unicode code points</h3>
<p> The maximum Unicode code point is <code>&quot;U+10FFFF&quot;</code>, and Unicode only defines operations on code points up through that. But Perl works on code points up to the maximum permissible signed number available on the platform. However, Perl will not accept these from input streams unless lax rules are being used, and will warn (using the warning category <code>&quot;non_unicode&quot;</code>, which is a sub-category of <code>&quot;utf8&quot;</code>) if any are output. </p>
<p> Since Unicode rules are not defined on these code points, if a Unicode-defined operation is done on them, Perl uses what we believe are sensible rules, while generally warning, using the <code>&quot;non_unicode&quot;</code> category. For example, <code>&quot;uc(&quot;\x{11_0000}&quot;)&quot;</code> will generate such a warning, returning the input parameter as its result, since Perl defines the uppercase of every non-Unicode code point to be the code point itself. (All the case changing operations, not just uppercasing, work this way.) </p>
<p> The situation with matching Unicode properties in regular expressions, the <code>&quot;\p{}&quot;</code> and <code>&quot;\P{}&quot;</code> constructs, against these code points is not as clear cut, and how these are handled has changed as we&#8217;ve gained experience. </p>
<p> One possibility is to treat any match against these code points as undefined. But since Perl doesn&#8217;t have the concept of a match being undefined, it converts this to failing or <code>&quot;FALSE&quot;</code>. This is almost, but not quite, what Perl did from v5.14 (when use of these code points became generally reliable) through v5.18. The difference is that Perl treated all <code>&quot;\p{}&quot;</code> matches as failing, but all <code>&quot;\P{}&quot;</code> matches as succeeding. </p>
<p> One problem with this is that it leads to unexpected, and confusing results in some cases: </p>
<pre><code> chr(0x110000) =~ \p{ASCII_Hex_Digit=True} # Failed on &lt;= v5.18
 chr(0x110000) =~ \p{ASCII_Hex_Digit=False} # Failed! on &lt;= v5.18
</code></pre>
<p> That is, it treated both matches as undefined, and converted that to false (raising a warning on each). The first case is the expected result, but the second is likely counterintuitive: ``How could both be false when they are complements?&#8216;&#8216; Another problem was that the implementation optimized many Unicode property matches down to already existing simpler, faster operations, which don&#8217;t raise the warning. We chose to not forgo those optimizations, which help the vast majority of matches, just to generate a warning for the unlikely event that an above-Unicode code point is being matched against. </p>
<p> As a result of these problems, starting in v5.20, what Perl does is to treat non-Unicode code points as just typical unassigned Unicode characters, and matches accordingly. (Note: Unicode has atypical unassigned code points. For example, it has noncharacter code points, and ones that, when they do get assigned, are destined to be written Right-to-left, as Arabic and Hebrew are. Perl assumes that no non-Unicode code point has any atypical properties.) </p>
<p> Perl, in most cases, will raise a warning when matching an above-Unicode code point against a Unicode property when the result is <code>&quot;TRUE&quot;</code> for <code>&quot;\p{}&quot;</code>, and <code>&quot;FALSE&quot;</code> for <code>&quot;\P{}&quot;</code>. For example: </p>
<pre><code> chr(0x110000) =~ \p{ASCII_Hex_Digit=True} # Fails, no warning
 chr(0x110000) =~ \p{ASCII_Hex_Digit=False} # Succeeds, with warning
</code></pre>
<p> In both these examples, the character being matched is non-Unicode, so Unicode doesn&#8217;t define how it should match. It clearly isn&#8217;t an <font SIZE="-1">ASCII</font> hex digit, so the first example clearly should fail, and so it does, with no warning. But it is arguable that the second example should have an undefined, hence <code>&quot;FALSE&quot;</code>, result. So a warning is raised for it. </p>
<p> Thus the warning is raised for many fewer cases than in earlier Perls, and only when what the result is could be arguable. It turns out that none of the optimizations made by Perl (or are ever likely to be made) cause the warning to be skipped, so it solves both problems of Perl&#8217;s earlier approach. The most commonly used property that is affected by this change is <code>&quot;\p{Unassigned}&quot;</code> which is a short form for <code>&quot;\p{General_Category=Unassigned}&quot;</code>. Starting in v5.20, all non-Unicode code points are considered <code>&quot;Unassigned&quot;</code>. In earlier releases the matches failed because the result was considered undefined. </p>
<p> The only place where the warning is not raised when it might ought to have been is if optimizations cause the whole pattern match to not even be attempted. For example, Perl may figure out that for a string to match a certain regular expression pattern, the string has to contain the substring <code>&quot;foobar&quot;</code>. Before attempting the match, Perl may look for that substring, and if not found, immediately fail the match without actually trying it; so no warning gets generated even if the string contains an above-Unicode code point. </p>
<p> This behavior is more ``Do what I mean&#8217;&#8216; than in earlier Perls for most applications. But it catches fewer issues for code that needs to be strictly Unicode compliant. Therefore there is an additional mode of operation available to accommodate such code. This mode is enabled if a regular expression pattern is compiled within the lexical scope where the <code>&quot;non_unicode&quot;</code> warning class has been made fatal, say by: </p>
<pre><code> use warnings FATAL =&gt; &quot;non_unicode&quot;
</code></pre>
<p> (see warnings). In this mode of operation, Perl will raise the warning for all matches against a non-Unicode code point (not just the arguable ones), and it skips the optimizations that might cause the warning to not be output. (It currently still won&#8217;t warn if the match isn&#8217;t even attempted, like in the <code>&quot;foobar&quot;</code> example above.) </p>
<p> In summary, Perl now normally treats non-Unicode code points as typical Unicode unassigned code points for regular expression matches, raising a warning only when it is arguable what the result should be. However, if this warning has been made fatal, it isn&#8217;t skipped. </p>
<p> There is one exception to all this. <code>&quot;\p{All}&quot;</code> looks like a Unicode property, but it is a Perl extension that is defined to be true for all possible code points, Unicode or not, so no warning is ever generated when matching this against a non-Unicode code point. (Prior to v5.20, it was an exact synonym for <code>&quot;\p{Any}&quot;</code>, matching code points <code>0</code> through <code>0x10FFFF</code>.)  </p>
<h3>Security Implications of Unicode</h3>
<p> First, read Unicode Security Considerations &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr36">http://www.unicode.org/reports/tr36</a>&gt;. </p>
<p> Also, note the following: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Malformed <font SIZE="-1">UTF-8</font> </p>
<p> <font SIZE="-1">UTF-8</font> is very structured, so many combinations of bytes are invalid. In the past, Perl tried to soldier on and make some sense of invalid combinations, but this can lead to security holes, so now, if the Perl core needs to process an invalid combination, it will either raise a fatal error, or will replace those bytes by the sequence that forms the Unicode <font SIZE="-1">REPLACEMENT CHARACTER,</font> for which purpose Unicode created it. </p>
<p> Every code point can be represented by more than one possible syntactically valid <font SIZE="-1">UTF-8</font> sequence. Early on, both Unicode and Perl considered any of these to be valid, but now, all sequences longer than the shortest possible one are considered to be malformed. </p>
<p> Unicode considers many code points to be illegal, or to be avoided. Perl generally accepts them, once they have passed through any input filters that may try to exclude them. These have been discussed above (see ``Surrogates&#8217;&#8216; under <font SIZE="-1">UTF-16</font> in ``Unicode Encodings&#8217;&#8216;, ``Noncharacter code points&#8217;&#8216;, and ``Beyond Unicode code points&#8217;&#8216;). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regular expression pattern matching may surprise you if you&#8217;re not accustomed to Unicode. Starting in Perl 5.14, several pattern modifiers are available to control this, called the character set modifiers. Details are given in ``Character set modifiers&#8217;&#8216; in perlre. </p>
 </dd></dl>
<p> As discussed elsewhere, Perl has one foot (two hooves?) planted in each of two worlds: the old world of <font SIZE="-1">ASCII</font> and single-byte locales, and the new world of Unicode, upgrading when necessary. If your legacy code does not explicitly use Unicode, no automatic switch-over to Unicode should happen.  </p>
<font SIZE="-1"></font><h3>Unicode in Perl on EBCDIC</h3>
<p> Unicode is supported on <font SIZE="-1">EBCDIC</font> platforms. See perlebcdic. </p>
<p> Unless <font SIZE="-1">ASCII</font> vs. <font SIZE="-1">EBCDIC</font> issues are specifically being discussed, references to <font SIZE="-1">UTF-8</font> encoding in this document and elsewhere should be read as meaning UTF-EBCDIC on <font SIZE="-1">EBCDIC</font> platforms. See ``Unicode and <font SIZE="-1">UTF&#8217;&#8216;</font> in perlebcdic. </p>
<p> Because UTF-EBCDIC is so similar to <font SIZE="-1">UTF-8,</font> the differences are mostly hidden from you; <code>&quot;use utf8&quot;</code> (and <font SIZE="-1">NOT</font> something like <code>&quot;use utfebcdic&quot;</code>) declares the script is in the platform&#8217;s ``native&#8217;&#8216; 8-bit encoding of Unicode. (Similarly for the <code>&quot;:utf8&quot;</code> layer.)  </p>
<h3>Locales</h3>
<p> See ``Unicode and <font SIZE="-1">UTF-8&#8217;&#8216;</font> in perllocale  </p>
<h3>When Unicode Does Not Happen</h3>
<p> There are still many places where Unicode (in some encoding or another) could be given as arguments or received as results, or both in Perl, but it is not, in spite of Perl having extensive ways to input and output in Unicode, and a few other ``entry points&#8217;&#8216; like the <code>@ARGV</code> array (which can sometimes be interpreted as <font SIZE="-1">UTF-8</font>). </p>
<p> The following are such interfaces. Also, see ``The &#8216;&#8216;Unicode Bug&quot;&quot;. For all of these interfaces Perl currently (as of v5.16.0) simply assumes byte strings both as arguments and results, or <font SIZE="-1">UTF-8</font> strings if the (deprecated) <code>&quot;encoding&quot;</code> pragma has been used. </p>
<p> One reason that Perl does not attempt to resolve the role of Unicode in these situations is that the answers are highly dependent on the operating system and the file system(s). For example, whether filenames can be in Unicode and in exactly what kind of encoding, is not exactly a portable concept. Similarly for <code>&quot;qx&quot;</code> and <code>&quot;system&quot;</code>: how well will the ``command-line interface&#8217;&#8216; (and which of them?) handle Unicode? </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;chdir&quot;</code>, <code>&quot;chmod&quot;</code>, <code>&quot;chown&quot;</code>, <code>&quot;chroot&quot;</code>, <code>&quot;exec&quot;</code>, <code>&quot;link&quot;</code>, <code>&quot;lstat&quot;</code>, <code>&quot;mkdir&quot;</code>, <code>&quot;rename&quot;</code>, <code>&quot;rmdir&quot;</code>, <code>&quot;stat&quot;</code>, <code>&quot;symlink&quot;</code>, <code>&quot;truncate&quot;</code>, <code>&quot;unlink&quot;</code>, <code>&quot;utime&quot;</code>, <code>&quot;-X&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>%ENV</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;glob&quot;</code> (aka the <code>&quot;&lt;*&gt;&quot;</code>) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;open&quot;</code>, <code>&quot;opendir&quot;</code>, <code>&quot;sysopen&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;qx&quot;</code> (aka the backtick operator), <code>&quot;system&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;readdir&quot;</code>, <code>&quot;readlink&quot;</code> </p>
 </dd></dl>
<h3>The Unicode Bug</h3>
<p> The term, ``Unicode bug&#8217;&#8216; has been applied to an inconsistency with the code points in the <code>&quot;Latin-1 Supplement&quot;</code> block, that is, between 128 and 255. Without a locale specified, unlike all other characters or code points, these characters can have very different semantics depending on the rules in effect. (Characters whose code points are above 255 force Unicode rules; whereas the rules for <font SIZE="-1">ASCII</font> characters are the same under both <font SIZE="-1">ASCII</font> and Unicode rules.) </p>
<p> Under Unicode rules, these upper-Latin1 characters are interpreted as Unicode code points, which means they have the same semantics as Latin-1 (<font SIZE="-1">ISO-8859-1</font>) and C1 controls. </p>
<p> As explained in ``<font SIZE="-1">ASCII</font> Rules versus Unicode Rules&#8217;&#8216;, under <font SIZE="-1">ASCII</font> rules, they are considered to be unassigned characters. </p>
<p> This can lead to unexpected results. For example, a string&#8217;s semantics can suddenly change if a code point above 255 is appended to it, which changes the rules from <font SIZE="-1">ASCII</font> to Unicode. As an example, consider the following program and its output: </p>
<pre><code> $ perl -le'
     no feature &quot;unicode_strings&quot;;
     $s1 = &quot;\xC2&quot;;
     $s2 = &quot;\x{2660}&quot;;
     for ($s1, $s2, $s1.$s2) {
         print /\w/ || 0;
     }
 '
 0
 0
 1
</code></pre>
<p> If there&#8217;s no <code>&quot;\w&quot;</code> in <code>&quot;s1&quot;</code> nor in <code>&quot;s2&quot;</code>, why does their concatenation have one? </p>
<p> This anomaly stems from Perl&#8217;s attempt to not disturb older programs that didn&#8217;t use Unicode, along with Perl&#8217;s desire to add Unicode support seamlessly. But the result turned out to not be seamless. (By the way, you can choose to be warned when things like this happen. See <code>&quot;encoding::warnings&quot;</code>.) </p>
<p> <code>&quot;use feature &#8216;unicode_strings&#8217;&quot;</code> was added, starting in Perl v5.12, to address this problem. It affects these things: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Changing the case of a scalar, that is, using <code>&quot;uc()&quot;</code>, <code>&quot;ucfirst()&quot;</code>, <code>&quot;lc()&quot;</code>, and <code>&quot;lcfirst()&quot;</code>, or <code>&quot;\L&quot;</code>, <code>&quot;\U&quot;</code>, <code>&quot;\u&quot;</code> and <code>&quot;\l&quot;</code> in double-quotish contexts, such as regular expression substitutions. </p>
<p> Under <code>&quot;unicode_strings&quot;</code> starting in Perl 5.12.0, Unicode rules are generally used. See ``lc&#8217;&#8216; in perlfunc for details on how this works in combination with various other pragmas. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using caseless (<code>&quot;/i&quot;</code>) regular expression matching. </p>
<p> Starting in Perl 5.14.0, regular expressions compiled within the scope of <code>&quot;unicode_strings&quot;</code> use Unicode rules even when executed or compiled into larger regular expressions outside the scope. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Matching any of several properties in regular expressions. </p>
<p> These properties are <code>&quot;\b&quot;</code> (without braces), <code>&quot;\B&quot;</code> (without braces), <code>&quot;\s&quot;</code>, <code>&quot;\S&quot;</code>, <code>&quot;\w&quot;</code>, <code>&quot;\W&quot;</code>, and all the Posix character classes <i>except</i> <code>&quot;[[:ascii:]]&quot;</code>. </p>
<p> Starting in Perl 5.14.0, regular expressions compiled within the scope of <code>&quot;unicode_strings&quot;</code> use Unicode rules even when executed or compiled into larger regular expressions outside the scope. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In <code>&quot;quotemeta&quot;</code> or its inline equivalent <code>&quot;\Q&quot;</code>. </p>
<p> Starting in Perl 5.16.0, consistent quoting rules are used within the scope of <code>&quot;unicode_strings&quot;</code>, as described in ``quotemeta&#8217;&#8216; in perlfunc. Prior to that, or outside its scope, no code points above 127 are quoted in <font SIZE="-1">UTF-8</font> encoded strings, but in byte encoded strings, code points between 128-255 are always quoted. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In the <code>&quot;..&quot;</code> or range operator. </p>
<p> Starting in Perl 5.26.0, the range operator on strings treats their lengths consistently within the scope of <code>&quot;unicode_strings&quot;</code>. Prior to that, or outside its scope, it could produce strings whose length in characters exceeded that of the right-hand side, where the right-hand side took up more bytes than the correct range endpoint. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In <code>&quot;split&quot;</code>&#8216;s special-case whitespace splitting. </p>
<p> Starting in Perl 5.28.0, the <code>&quot;split&quot;</code> function with a pattern specified as a string containing a single space handles whitespace characters consistently within the scope of of <code>&quot;unicode_strings&quot;</code>. Prior to that, or outside its scope, characters that are whitespace according to Unicode rules but not according to <font SIZE="-1">ASCII</font> rules were treated as field contents rather than field separators when they appear in byte-encoded strings. </p>
 </dd></dl>
<p> You can see from the above that the effect of <code>&quot;unicode_strings&quot;</code> increased over several Perl releases. (And Perl&#8217;s support for Unicode continues to improve; it&#8217;s best to use the latest available release in order to get the most complete and accurate results possible.) Note that <code>&quot;unicode_strings&quot;</code> is automatically chosen if you <code>&quot;use 5.012&quot;</code> or higher. </p>
<p> For Perls earlier than those described above, or when a string is passed to a function outside the scope of <code>&quot;unicode_strings&quot;</code>, see the next section.  </p>
<h3>Forcing Unicode in Perl (Or Unforcing Unicode in Perl)</h3>
<p> Sometimes (see ``When Unicode Does Not Happen&#8217;&#8216; or ``The &#8216;&#8216;Unicode Bug&quot;&quot;) there are situations where you simply need to force a byte string into <font SIZE="-1">UTF-8,</font> or vice versa. The standard module Encode can be used for this, or the low-level calls <code>&quot;utf8::upgrade($bytestring)&quot;</code> and <code>&quot;utf8::downgrade($utf8string[, FAIL_OK])&quot;</code>. </p>
<p> Note that <code>&quot;utf8::downgrade()&quot;</code> can fail if the string contains characters that don&#8217;t fit into a byte. </p>
<p> Calling either function on a string that already is in the desired state is a no-op. </p>
<p> ``<font SIZE="-1">ASCII</font> Rules versus Unicode Rules&#8217;&#8216; gives all the ways that a string is made to use Unicode rules.  </p>
<font SIZE="-1"></font><h3>Using Unicode in XS</h3>
<p> See ``Unicode Support&#8217;&#8216; in perlguts for an introduction to Unicode at the <font SIZE="-1">XS</font> level, and ``Unicode Support&#8217;&#8216; in perlapi for the <font SIZE="-1">API</font> details.  </p>
<h3>Hacking Perl to work on earlier Unicode versions (for very serious hackers only)</h3>
<p> Perl by default comes with the latest supported Unicode version built-in, but the goal is to allow you to change to use any earlier one. In Perls v5.20 and v5.22, however, the earliest usable version is Unicode 5.1. Perl v5.18 and v5.24 are able to handle all earlier versions. </p>
<p> Download the files in the desired version of Unicode from the Unicode web site &lt;<a rel="nofollow" href="http://www.unicode.org">http://www.unicode.org</a>&gt;). These should replace the existing files in <i>lib/unicore</i> in the Perl source tree. Follow the instructions in <i></i><font SIZE="-1"><i>README</i></font><i>.perl</i> in that directory to change some of their names, and then build perl (see <font SIZE="-1">INSTALL</font>).  </p>
<h3>Porting code from perl-5.6.X</h3>
<p> Perls starting in 5.8 have a different Unicode model from 5.6. In 5.6 the programmer was required to use the <code>&quot;utf8&quot;</code> pragma to declare that a given scope expected to deal with Unicode data and had to make sure that only Unicode data were reaching that scope. If you have code that is working with 5.6, you will need some of the following adjustments to your code. The examples are written such that the code will continue to work under 5.6, so you should be safe to try them out. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A filehandle that should read or write <font SIZE="-1">UTF-8</font> </p>
<pre><code>  if ($] &gt; 5.008) {
    binmode $fh, &quot;:encoding(UTF-8)&quot;;
  }
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> A scalar that is going to be passed to some extension </p>
<p> Be it <code>&quot;Compress::Zlib&quot;</code>, <code>&quot;Apache::Request&quot;</code> or any extension that has no mention of Unicode in the manpage, you need to make sure that the <font SIZE="-1">UTF8</font> flag is stripped off. Note that at the time of this writing (January 2012) the mentioned modules are not UTF-8-aware. Please check the documentation to verify if this is still true. </p>
<pre><code>  if ($] &gt; 5.008) {
    require Encode;
    $val = Encode::encode(&quot;UTF-8&quot;, $val); # make octets
  }
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> A scalar we got back from an extension </p>
<p> If you believe the scalar comes back as <font SIZE="-1">UTF-8,</font> you will most likely want the <font SIZE="-1">UTF8</font> flag restored: </p>
<pre><code>  if ($] &gt; 5.008) {
    require Encode;
    $val = Encode::decode(&quot;UTF-8&quot;, $val);
  }
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Same thing, if you are really sure it is <font SIZE="-1">UTF-8</font> </p>
<pre><code>  if ($] &gt; 5.008) {
    require Encode;
    Encode::_utf8_on($val);
  }
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> A wrapper for <font SIZE="-1">DBI</font> <code>&quot;fetchrow_array&quot;</code> and <code>&quot;fetchrow_hashref&quot;</code> </p>
<p> When the database contains only <font SIZE="-1">UTF-8,</font> a wrapper function or method is a convenient way to replace all your <code>&quot;fetchrow_array&quot;</code> and <code>&quot;fetchrow_hashref&quot;</code> calls. A wrapper function will also make it easier to adapt to future enhancements in your database driver. Note that at the time of this writing (January 2012), the <font SIZE="-1">DBI</font> has no standardized way to deal with <font SIZE="-1">UTF-8</font> data. Please check the <font SIZE="-1">DBI</font> documentation to verify if that is still true. </p>
<pre><code>  sub fetchrow {
    # $what is one of fetchrow_{array,hashref}
    my($self, $sth, $what) = @_;
    if ($] &lt; 5.008) {
      return $sth-&gt;$what;
    } else {
      require Encode;
      if (wantarray) {
        my @arr = $sth-&gt;$what;
        for (@arr) {
          defined &amp;&amp; /[^\000-\177]/ &amp;&amp; Encode::_utf8_on($_);
        }
        return @arr;
      } else {
        my $ret = $sth-&gt;$what;
        if (ref $ret) {
          for my $k (keys %$ret) {
            defined
            &amp;&amp; /[^\000-\177]/
            &amp;&amp; Encode::_utf8_on($_) for $ret-&gt;{$k};
          }
          return $ret;
        } else {
          defined &amp;&amp; /[^\000-\177]/ &amp;&amp; Encode::_utf8_on($_) for $ret;
          return $ret;
        }
      }
    }
  }
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> A large scalar that you know can only contain <font SIZE="-1">ASCII</font> </p>
<p> Scalars that contain only <font SIZE="-1">ASCII</font> and are marked as <font SIZE="-1">UTF-8</font> are sometimes a drag to your program. If you recognize such a situation, just remove the <font SIZE="-1">UTF8</font> flag: </p>
<pre><code>  utf8::downgrade($val) if $] &gt; 5.008;
</code></pre>
 </dd></dl>
<h2>BUGS</h2>
<p> See also ``The &#8216;&#8216;Unicode Bug&quot;&quot; above.  </p>
<h3>Interaction with Extensions</h3>
<p> When Perl exchanges data with an extension, the extension should be able to understand the <font SIZE="-1">UTF8</font> flag and act accordingly. If the extension doesn&#8217;t recognize that flag, it&#8217;s likely that the extension will return incorrectly-flagged data. </p>
<p> So if you&#8217;re working with Unicode data, consult the documentation of every module you&#8217;re using if there are any issues with Unicode data exchange. If the documentation does not talk about Unicode at all, suspect the worst and probably look at the source to learn how the module is implemented. Modules written completely in Perl shouldn&#8217;t cause problems. Modules that directly or indirectly access code written in other programming languages are at risk. </p>
<p> For affected functions, the simple strategy to avoid data corruption is to always make the encoding of the exchanged data explicit. Choose an encoding that you know the extension can handle. Convert arguments passed to the extensions to that encoding and convert results back from that encoding. Write wrapper functions that do the conversions for you, so you can later change the functions when the extension catches up. </p>
<p> To provide an example, let&#8217;s say the popular <code>&quot;Foo::Bar::escape_html&quot;</code> function doesn&#8217;t deal with Unicode data yet. The wrapper function would convert the argument to raw <font SIZE="-1">UTF-8</font> and convert the result back to Perl&#8217;s internal representation like so: </p>
<pre><code>    sub my_escape_html ($) {
        my($what) = shift;
        return unless defined $what;
        Encode::decode(&quot;UTF-8&quot;, Foo::Bar::escape_html(
                                     Encode::encode(&quot;UTF-8&quot;, $what)));
    }
</code></pre>
<p> Sometimes, when the extension does not convert data but just stores and retrieves it, you will be able to use the otherwise dangerous <code>&quot;Encode::_utf8_on()&quot;</code> function. Let&#8217;s say the popular <code>&quot;Foo::Bar&quot;</code> extension, written in C, provides a <code>&quot;param&quot;</code> method that lets you store and retrieve data according to these prototypes: </p>
<pre><code>    $self-&gt;param($name, $value); # set a scalar
    $value = $self-&gt;param($name); # retrieve a scalar
</code></pre>
<p> If it does not yet provide support for any encoding, one could write a derived class with such a <code>&quot;param&quot;</code> method: </p>
<pre><code>    sub param {
      my($self,$name,$value) = @_;
      utf8::upgrade($name); # make sure it is UTF-8 encoded
      if (defined $value) {
        utf8::upgrade($value); # make sure it is UTF-8 encoded
        return $self-&gt;SUPER::param($name,$value);
      } else {
        my $ret = $self-&gt;SUPER::param($name);
        Encode::_utf8_on($ret); # we know, it is UTF-8 encoded
        return $ret;
      }
    }
</code></pre>
<p> Some extensions provide filters on data entry/exit points, such as <code>&quot;DB_File::filter_store_key&quot;</code> and family. Look out for such filters in the documentation of your extensions; they can make the transition to Unicode data much easier.  </p>
<h3>Speed</h3>
<p> Some functions are slower when working on <font SIZE="-1">UTF-8</font> encoded strings than on byte encoded strings. All functions that need to hop over characters such as <code>&quot;length()&quot;</code>, <code>&quot;substr()&quot;</code> or <code>&quot;index()&quot;</code>, or matching regular expressions can work <code>much</code> faster when the underlying data are byte-encoded. </p>
<p> In Perl 5.8.0 the slowness was often quite spectacular; in Perl 5.8.1 a caching scheme was introduced which improved the situation. In general, operations with <font SIZE="-1">UTF-8</font> encoded strings are still slower. As an example, the Unicode properties (character classes) like <code>&quot;\p{Nd}&quot;</code> are known to be quite a bit slower (5-20 times) than their simpler counterparts like <code>&quot;[0-9]&quot;</code> (then again, there are hundreds of Unicode characters matching <code>&quot;Nd&quot;</code> compared with the 10 <font SIZE="-1">ASCII</font> characters matching <code>&quot;[0-9]&quot;</code>).  </p>
<h2>SEE ALSO</h2>
<p> perlunitut, perluniintro, perluniprops, Encode, open, utf8, bytes, perlretut, ``${^UNICODE}&#8216;&#8216; in perlvar, &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr44">http://www.unicode.org/reports/tr44</a>&gt;). </p>
