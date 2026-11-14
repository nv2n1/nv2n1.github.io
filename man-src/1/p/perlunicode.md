---
title: "perlunicode(1)"
name: "perlunicode"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlunicode/"
description: "perlunicode – Unicode support in Perl"
---

<h2 class="name">NAME</h2>
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
<dt>Safest if you &quot;use feature &#8216;unicode_strings&#8217;&quot;</p>
<dd> In order to preserve backward compatibility, Perl does not turn on full internal Unicode support unless the pragma <tt>&quot;use feature 'unicode_strings'&quot;</tt> is specified. (This is automatically selected if you <tt>&quot;use 5.012&quot;</tt> or higher.) Failure to do this can trigger unexpected surprises. See &#8220;The &#8221;Unicode Bug&quot;&quot; below. </p>
<p> This pragma doesn&#8217;t affect I/O. Nor does it change the internal representation of strings, only their interpretation. There are still several places where Unicode isn&#8217;t fully supported, such as in filenames.</p>
<dt>Input and Output Layers</p>
<dd> Use the <tt>&quot;:encoding(...)&quot;</tt> layer to read from and write to filehandles using the specified encoding. (See open.)</p>
<dt>You must convert your non-ASCII, non-UTF-8 Perl scripts to be <font SIZE="-1">UTF-8.</font></p>
<dd> The encoding module has been deprecated since perl 5.18 and the perl internals it requires have been removed with perl 5.26.</p>
<dt>&quot;use utf8&quot; still needed to enable <font SIZE="-1">UTF-8</font> in scripts</p>
<dd> If your Perl script is itself encoded in <font SIZE="-1">UTF-8</font>, the <tt>&quot;use utf8&quot;</tt> pragma must be explicitly included to enable recognition of that (in string or regular expression literals, or in identifier names). <code>This is the only time when an explicit </code>&quot;use utf8&quot;<code> is needed.</code> (See utf8). </p>
<p> If a Perl script begins with the bytes that form the <font SIZE="-1">UTF-8</font> encoding of the Unicode <font SIZE="-1">BYTE ORDER MARK</font> (<tt>&quot;BOM&quot;</tt>, see &#8220;Unicode Encodings&#8221;), those bytes are completely ignored.</p>
<dt><font SIZE="-1">UTF-16</font> scripts autodetected</p>
<dd> If a Perl script begins with the Unicode <tt>&quot;BOM&quot;</tt> (<font SIZE="-1">UTF-16LE, UTF16-BE</font>), or if the script looks like non-<tt>&quot;BOM&quot;</tt>-marked <font SIZE="-1">UTF-16</font> of either endianness, Perl will correctly read in the script as the appropriate Unicode encoding.</dl>
<h3>Byte and Character Semantics</h3>
<p> Before Unicode, most encodings used 8 bits (a single byte) to encode each character. Thus a character was a byte, and a byte was a character, and there could be only 256 or fewer possible characters. &#8220;Byte Semantics&#8221; in the title of this section refers to this behavior. There was no need to distinguish between &#8220;Byte&#8221; and &#8220;Character&#8221;. </p>
<p> Then along comes Unicode which has room for over a million characters (and Perl allows for even more). This means that a character may require more than a single byte to represent it, and so the two terms are no longer equivalent. What matter are the characters as whole entities, and not usually the bytes that comprise them. That&#8217;s what the term &#8220;Character Semantics&#8221; in the title of this section refers to. </p>
<p> Perl had to change internally to decouple &#8220;bytes&#8221; from &#8220;characters&#8221;. It is important that you too change your ideas, if you haven&#8217;t already, so that &#8220;byte&#8221; and &#8220;character&#8221; no longer mean the same thing in your mind. </p>
<p> The basic building block of Perl strings has always been a &#8220;character&#8221;. The changes basically come down to that the implementation no longer thinks that a character is always just a single byte. </p>
<p> There are various things to note:</p>
<dl>
<dt>&bull;</p>
<dd> String handling functions, for the most part, continue to operate in terms of characters. <tt>&quot;length()&quot;</tt>, for example, returns the number of characters in a string, just as before. But that number no longer is necessarily the same as the number of bytes in the string (there may be more bytes than characters). The other such functions include <tt>&quot;chop()&quot;</tt>, <tt>&quot;chomp()&quot;</tt>, <tt>&quot;substr()&quot;</tt>, <tt>&quot;pos()&quot;</tt>, <tt>&quot;index()&quot;</tt>, <tt>&quot;rindex()&quot;</tt>, <tt>&quot;sort()&quot;</tt>, <tt>&quot;sprintf()&quot;</tt>, and <tt>&quot;write()&quot;</tt>. </p>
<p> The exceptions are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> the bit-oriented <tt>&quot;vec&quot;</tt> </p>
<dt>&bull;</p>
<dd> the byte-oriented <tt>&quot;pack&quot;</tt>/<tt>&quot;unpack&quot;</tt> <tt>&quot;C&quot;</tt> format </p>
<p> However, the <tt>&quot;W&quot;</tt> specifier does operate on whole characters, as does the <tt>&quot;U&quot;</tt> specifier.</p>
<dt>&bull;</p>
<dd> some operators that interact with the platform&#8217;s operating system </p>
<p> Operators dealing with filenames are examples.</p>
<dt>&bull;</p>
<dd> when the functions are called from within the scope of the <tt>&quot;use bytes&quot;</tt> pragma </p>
<p> Likely, you should use this only for debugging anyway.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> Strings&#8212;including hash keys&#8212;and regular expression patterns may contain characters that have ordinal values larger than 255. </p>
<p> If you use a Unicode editor to edit your program, Unicode characters may occur directly within the literal strings in <font SIZE="-1">UTF-8</font> encoding, or <font SIZE="-1">UTF-16.</font> (The former requires a <tt>&quot;use utf8&quot;</tt>, the latter may require a <tt>&quot;BOM&quot;</tt>.) </p>
<p> &#8220;Creating Unicode&#8221; in perluniintro gives other ways to place non-ASCII characters in your strings.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;chr()&quot;</tt> and <tt>&quot;ord()&quot;</tt> functions work on whole characters.</p>
<dt>&bull;</p>
<dd> Regular expressions match whole characters. For example, <tt>&quot;.&quot;</tt> matches a whole character instead of only a single byte.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;tr///&quot;</tt> operator translates whole characters. (Note that the <tt>&quot;tr///CU&quot;</tt> functionality has been removed. For similar functionality to that, see <tt>&quot;pack('U0', ...)&quot;</tt> and <tt>&quot;pack('C0', ...)&quot;</tt>).</p>
<dt>&bull;</p>
<dd> <tt>&quot;scalar reverse()&quot;</tt> reverses by character rather than by byte.</p>
<dt>&bull;</p>
<dd> The bit string operators, <tt>&quot;&amp; | ^ ~&quot;</tt> and (starting in v5.22) <tt>&quot;&amp;. |. ^. ~.&quot;</tt> can operate on bit strings encoded in <font SIZE="-1">UTF-8,</font> but this can give unexpected results if any of the strings contain code points above 0xFF. Starting in v5.28, it is a fatal error to have such an operand. Otherwise, the operation is performed on a non-UTF-8 copy of the operand. If you&#8217;re not sure about the encoding of a string, downgrade it before using any of these operators; you can use <tt>&quot;utf8::utf8_downgrade()&quot;</tt>.</dl>
<p> The bottom line is that Perl has always practiced &#8220;Character Semantics&#8221;, but with the advent of Unicode, that is now different than &#8220;Byte Semantics&#8221;.</p>
<h3><font SIZE="-1">ASCII</font> Rules versus Unicode Rules</h3>
<p> Before Unicode, when a character was a byte was a character, Perl knew only about the 128 characters defined by <font SIZE="-1">ASCII,</font> code points 0 through 127 (except for under <tt>&quot;use locale&quot;</tt>). That left the code points 128 to 255 as unassigned, and available for whatever use a program might want. The only semantics they have is their ordinal numbers, and that they are members of none of the non-negative character classes. None are considered to match <tt>&quot;\w&quot;</tt> for example, but all match <tt>&quot;\W&quot;</tt>. </p>
<p> Unicode, of course, assigns each of those code points a particular meaning (along with ones above 255). To preserve backward compatibility, Perl only uses the Unicode meanings when there is some indication that Unicode is what is intended; otherwise the non-ASCII code points remain treated as if they are unassigned. </p>
<p> Here are the ways that Perl knows that a string should be treated as Unicode:</p>
<dl>
<dt>&bull;</p>
<dd> Within the scope of <tt>&quot;use utf8&quot;</tt> </p>
<p> If the whole program is Unicode (signified by using 8-bit <code>U</code>nicode <code>T</code>ransformation <code>F</code>ormat), then all literal strings within it must be Unicode.</p>
<dt>&bull;</p>
<dd> Within the scope of <tt>&quot;use feature 'unicode_strings'&quot;</tt> </p>
<p> This pragma was created so you can explicitly tell Perl that operations executed within its scope are to use Unicode rules. More operations are affected with newer perls. See &#8220;The &#8221;Unicode Bug&quot;&quot;.</p>
<dt>&bull;</p>
<dd> Within the scope of <tt>&quot;use 5.012&quot;</tt> or higher </p>
<p> This implicitly turns on <tt>&quot;use feature 'unicode_strings'&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Within the scope of <tt>&quot;use locale 'not_characters'&quot;</tt>, or <tt>&quot;use locale&quot;</tt> and the current locale is a <font SIZE="-1">UTF-8</font> locale. </p>
<p> The former is defined to imply Unicode handling; and the latter indicates a Unicode locale, hence a Unicode interpretation of all strings within it.</p>
<dt>&bull;</p>
<dd> When the string contains a Unicode-only code point </p>
<p> Perl has never accepted code points above 255 without them being Unicode, so their use implies Unicode for the whole string.</p>
<dt>&bull;</p>
<dd> When the string contains a Unicode named code point <tt>&quot;\N{...}&quot;</tt> </p>
<p> The <tt>&quot;\N{...}&quot;</tt> construct explicitly refers to a Unicode code point, even if it is one that is also in <font SIZE="-1">ASCII.</font> Therefore the string containing it must be Unicode.</p>
<dt>&bull;</p>
<dd> When the string has come from an external source marked as Unicode </p>
<p> The <tt>&quot;-C&quot;</tt> command line option can specify that certain inputs to the program are Unicode, and the values of this can be read by your Perl code, see &#8220;${^UNICODE}&#8221; in perlvar.</p>
<dt>&bull;</p>
<dd> When the string has been upgraded to <font SIZE="-1">UTF-8</font> </p>
<p> The function <tt>&quot;utf8::utf8_upgrade()&quot;</tt> can be explicitly used to permanently (unless a subsequent <tt>&quot;utf8::utf8_downgrade()&quot;</tt> is called) cause a string to be treated as Unicode.</p>
<dt>&bull;</p>
<dd> There are additional methods for regular expression patterns </p>
<p> A pattern that is compiled with the <tt>&quot;/u&quot;</tt> or <tt>&quot;/a&quot;</tt> modifiers is treated as Unicode (though there are some restrictions with <tt>&quot;/a&quot;</tt>). Under the <tt>&quot;/d&quot;</tt> and <tt>&quot;/l&quot;</tt> modifiers, there are several other indications for Unicode; see &#8220;Character set modifiers&#8221; in perlre.</dl>
<p> Note that all of the above are overridden within the scope of <tt>&quot;use bytes&quot;</tt>; but you should be using this pragma only for debugging. </p>
<p> Note also that some interactions with the platform&#8217;s operating system never use Unicode rules. </p>
<p> When Unicode rules are in effect:</p>
<dl>
<dt>&bull;</p>
<dd> Case translation operators use the Unicode case translation tables. </p>
<p> Note that <tt>&quot;uc()&quot;</tt>, or <tt>&quot;
