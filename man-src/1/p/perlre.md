---
title: "perlre(1)"
name: "perlre"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlre/"
---

<h2 class="name">NAME</h2>
 

 perlre - Perl regular expressions 

<h2>DESCRIPTION</h2>

 This page describes the syntax of regular expressions in Perl. 

 If you haven't used regular expressions before, a tutorial introduction is available in perlretut. If you know just a little about them, a quick-start introduction is available in perlrequick. 

 Except for ``The Basics'' section, this page assumes you are familiar with regular expression basics, like what is a ``pattern'', what does it look like, and how it is basically used. For a reference on how they are used, plus various examples of the same, see discussions of <tt>&quot;m//&quot;</tt>, <tt>&quot;s///&quot;</tt>, <tt>&quot;qr//&quot;</tt> and <tt>&quot;??&quot;</tt> in ``Regexp Quote-Like Operators'' in perlop. 

 New in v5.22, <tt>&quot;use re 'strict'&quot;</tt> applies stricter rules than otherwise when compiling regular expression patterns. It can find things that, while legal, may not be what you intended.

<h3>The Basics</h3>

 Regular expressions are strings with the very particular syntax and meaning described in this document and auxiliary documents referred to by this one. The strings are called ``patterns''. Patterns are used to determine if some other string, called the ``target'', has (or doesn't have) the characteristics specified by the pattern. We call this ``matching'' the target string against the pattern. Usually the match is done by having the target be the first operand, and the pattern be the second operand, of one of the two binary operators <tt>&quot;=~&quot;</tt> and <tt>&quot;!~&quot;</tt>, listed in ``Binding Operators'' in perlop; and the pattern will have been converted from an ordinary string by one of the operators in ``Regexp Quote-Like Operators'' in perlop, like so: 

 <pre>
 $foo =~ m/abc/
</pre> 

 This evaluates to true if and only if the string in the variable <tt>$foo</tt> contains somewhere in it, the sequence of characters ``a'', ``b'', then ``c''. (The <tt>&quot;=~ m&quot;</tt>, or match operator, is described in ``m/PATTERN/msixpodualngc'' in perlop.) 

 Patterns that aren't already stored in some variable must be delimitted, at both ends, by delimitter characters. These are often, as in the example above, forward slashes, and the typical way a pattern is written in documentation is with those slashes. In most cases, the delimitter is the same character, fore and aft, but there are a few cases where a character looks like it has a mirror-image mate, where the opening version is the beginning delimiter, and the closing one is the ending delimiter, like 

 <pre>
 $foo =~ m&lt;abc&gt;
</pre> 

 Most times, the pattern is evaluated in double-quotish context, but it is possible to choose delimiters to force single-quotish, like 

 <pre>
 $foo =~ m'abc'
</pre> 

 If the pattern contains its delimiter within it, that delimiter must be escaped. Prefixing it with a backslash (<i>e.g.</i>, <tt>&quot;/foo\/bar/&quot;</tt>) serves this purpose. 

 Any single character in a pattern matches that same character in the target string, unless the character is a <i>metacharacter</i> with a special meaning described in this document. A sequence of non-metacharacters matches the same sequence in the target string, as we saw above with <tt>&quot;m/abc/&quot;</tt>. 

 Only a few characters (all of them being <font SIZE="-1">ASCII</font> punctuation characters) are metacharacters. The most commonly used one is a dot <tt>&quot;.&quot;</tt>, which normally matches almost any character (including a dot itself). 

 You can cause characters that normally function as metacharacters to be interpreted literally by prefixing them with a <tt>&quot;\&quot;</tt>, just like the pattern's delimiter must be escaped if it also occurs within the pattern. Thus, <tt>&quot;\.&quot;</tt> matches just a literal dot, <tt>&quot;.&quot;</tt> instead of its normal meaning. This means that the backslash is also a metacharacter, so <tt>&quot;\\&quot;</tt> matches a single <tt>&quot;\&quot;</tt>. And a sequence that contains an escaped metacharacter matches the same sequence (but without the escape) in the target string. So, the pattern <tt>&quot;/blur\\fl/&quot;</tt> would match any target string that contains the sequence <tt>&quot;blur\fl&quot;</tt>. 

 The metacharacter <tt>&quot;|&quot;</tt> is used to match one thing or another. Thus 

 <pre>
 $foo =~ m/this|that/
</pre> 

 is <font SIZE="-1">TRUE</font> if and only if <tt>$foo</tt> contains either the sequence <tt>&quot;this&quot;</tt> or the sequence <tt>&quot;that&quot;</tt>. Like all metacharacters, prefixing the <tt>&quot;|&quot;</tt> with a backslash makes it match the plain punctuation character; in its case, the <font SIZE="-1">VERTICAL LINE.</font> 

 <pre>
 $foo =~ m/this\|that/
</pre> 

 is <font SIZE="-1">TRUE</font> if and only if <tt>$foo</tt> contains the sequence <tt>&quot;this|that&quot;</tt>. 

 You aren't limited to just a single <tt>&quot;|&quot;</tt>. 

 <pre>
 $foo =~ m/fee|fie|foe|fum/
</pre> 

 is <font SIZE="-1">TRUE</font> if and only if <tt>$foo</tt> contains any of those 4 sequences from the children's story ``Jack and the Beanstalk''. 

 As you can see, the <tt>&quot;|&quot;</tt> binds less tightly than a sequence of ordinary characters. We can override this by using the grouping metacharacters, the parentheses <tt>&quot;(&quot;</tt> and <tt>&quot;)&quot;</tt>. 

 <pre>
 $foo =~ m/th(is|at) thing/
</pre> 

 is <font SIZE="-1">TRUE</font> if and only if <tt>$foo</tt> contains either the sequence <tt>&quot;this thing&quot;</tt> or the sequence <tt>&quot;that thing&quot;</tt>. The portions of the string that match the portions of the pattern enclosed in parentheses are normally made available separately for use later in the pattern, substitution, or program. This is called ``capturing'', and it can get complicated. See ``Capture groups''. 

 The first alternative includes everything from the last pattern delimiter (<tt>&quot;(&quot;</tt>, <tt>&quot;(?:&quot;</tt> (described later), <i>etc</i>. or the beginning of the pattern) up to the first <tt>&quot;|&quot;</tt>, and the last alternative contains everything from the last <tt>&quot;|&quot;</tt> to the next closing pattern delimiter. That's why it's common practice to include alternatives in parentheses: to minimize confusion about where they start and end. 

 Alternatives are tried from left to right, so the first alternative found for which the entire expression matches, is the one that is chosen. This means that alternatives are not necessarily greedy. For example: when matching <tt>&quot;foo|foot&quot;</tt> against <tt>&quot;barefoot&quot;</tt>, only the <tt>&quot;foo&quot;</tt> part will match, as that is the first alternative tried, and it successfully matches the target string. (This might not seem important, but it is important when you are capturing matched text using parentheses.) 

 Besides taking away the special meaning of a metacharacter, a prefixed backslash changes some letter and digit characters away from matching just themselves to instead have special meaning. These are called ``escape sequences'', and all such are described in perlrebackslash. A backslash sequence (of a letter or digit) that doesn't currently have special meaning to Perl will raise a warning if warnings are enabled, as those are reserved for potential future use. 

 One such sequence is <tt>&quot;\b&quot;</tt>, which matches a boundary of some sort. <tt>&quot;\b{wb}&quot;</tt> and a few others give specialized types of boundaries. (They are all described in detail starting at ``\b{}, \b, \B{}, \B'' in perlrebackslash.) Note that these don't match characters, but the zero-width spaces between characters. They are an example of a zero-width assertion. Consider again, 

 <pre>
 $foo =~ m/fee|fie|foe|fum/
</pre> 

 It evaluates to <font SIZE="-1">TRUE</font> if, besides those 4 words, any of the sequences ``feed'', ``field'', ``Defoe'', ``fume'', and many others are in <tt>$foo</tt>. By judicious use of <tt>&quot;\b&quot;</tt> (or better (because it is designed to handle natural language) <tt>&quot;\b{wb}&quot;</tt>), we can make sure that only the Giant's words are matched: 

 <pre><code>
$foo = ~m /\b(fee | fie | foe | fum)\b /
       $foo = ~m /\b{wb}(fee | fie | foe | fum)\b{wb} /
</code></pre> 

 The final example shows that the characters <tt>&quot;{&quot;</tt> and <tt>&quot;}&quot;</tt> are metacharacters. 

 Another use for escape sequences is to specify characters that cannot (or which you prefer not to) be written literally. These are described in detail in ``Character Escapes'' in perlrebackslash, but the next three paragraphs briefly describe some of them. 

 Various control characters can be written in C language style: <tt>&quot;\n&quot;</tt> matches a newline, <tt>&quot;\t&quot;</tt> a tab, <tt>&quot;\r&quot;</tt> a carriage return, <tt>&quot;\f&quot;</tt> a form feed, <i>etc</i>. 

 More generally, <tt>&quot;\</tt>nnn<tt>&quot;</tt>, where <i>nnn</i> is a string of three octal digits, matches the character whose native code point is <i>nnn</i>. You can easily run into trouble if you don't have exactly three digits. So always use three, or since Perl 5.14, you can use <tt>&quot;\o{...}&quot;</tt> to specify any number of octal digits. 

 Similarly, <tt>&quot;\x</tt>nn<tt>&quot;</tt>, where <i>nn</i> are hexadecimal digits, matches the character whose native ordinal is <i>nn</i>. Again, not using exactly two digits is a recipe for disaster, but you can use <tt>&quot;\x{...}&quot;</tt> to specify any number of hex digits. 

 Besides being a metacharacter, the <tt>&quot;.&quot;</tt> is an example of a ``character class'', something that can match any single character of a given set of them. In its case, the set is just about all possible characters. Perl predefines several character classes besides the <tt>&quot;.&quot;</tt>; there is a separate reference page about just these, perlrecharclass. 

 You can define your own custom character classes, by putting into your pattern in the appropriate place(s), a list of all the characters you want in the set. You do this by enclosing the list within <tt>&quot;[]&quot;</tt> bracket characters. These are called ``bracketed character classes'' when we are being precise, but often the word ``bracketed'' is dropped. (Dropping it usually doesn't cause confusion.) This means that the <tt>&quot;[&quot;</tt> character is another metacharacter. It doesn't match anything just by itself; it is used only to tell Perl that what follows it is a bracketed character class. If you want to match a literal left square bracket, you must escape it, like <tt>&quot;\[&quot;</tt>. The matching <tt>&quot;]&quot;</tt> is also a metacharacter; again it doesn't match anything by itself, but just marks the end of your custom class to Perl. It is an example of a ``sometimes metacharacter''. It isn't a metacharacter if there is no corresponding <tt>&quot;[&quot;</tt>, and matches its literal self: 

 <pre>
 print &quot;]&quot; =~ /]/;  # prints 1
</pre> 

 The list of characters within the character class gives the set of characters matched by the class. <tt>&quot;[abc]&quot;</tt> matches a single ``a'' or ``b'' or ``c''. But if the first character after the <tt>&quot;[&quot;</tt> is <tt>&quot;^&quot;</tt>, the class instead matches any character not in the list. Within a list, the <tt>&quot;-&quot;</tt> character specifies a range of characters, so that <tt>&quot;a-z&quot;</tt> represents all characters between ``a'' and ``z'', inclusive. If you want either <tt>&quot;-&quot;</tt> or <tt>&quot;]&quot;</tt> itself to be a member of a class, put it at the start of the list (possibly after a <tt>&quot;^&quot;</tt>), or escape it with a backslash. <tt>&quot;-&quot;</tt> is also taken literally when it is at the end of the list, just before the closing <tt>&quot;]&quot;</tt>. (The following all specify the same class of three characters: <tt>&quot;[-az]&quot;</tt>, <tt>&quot;[az-]&quot;</tt>, and <tt>&quot;[a\-z]&quot;</tt>. All are different from <tt>&quot;[a-z]&quot;</tt>, which specifies a class containing twenty-six characters, even on EBCDIC-based character sets.) 

 There is lots more to bracketed character classes; full details are in ``Bracketed Character Classes'' in perlrecharclass. 

 <i>Metacharacters</i> 

 ``The Basics'' introduced some of the metacharacters. This section gives them all. Most of them have the same meaning as in the <i>egrep</i> command. 

 Only the <tt>&quot;\&quot;</tt> is always a metacharacter. The others are metacharacters just sometimes. The following tables lists all of them, summarizes their use, and gives the contexts where they are metacharacters. Outside those contexts or if prefixed by a <tt>&quot;\&quot;</tt>, they match their corresponding punctuation character. In some cases, their meaning varies depending on various pattern modifiers that alter the default behaviors. See ``Modifiers''. 

 
PURPOSE WHERE
 \ Escape the next character Always, except when escaped by another ^ Match the beginning of the string Not in[](or line, if / m is used) ^ Complement the[] class At the beginning of[].Match any single character except newline Not in[](under / s, includes newline) $ Match the end of the string Not in[], but can(or before newline at the end of the mean interpolate a string; or before any newline if / m is scalar used) | Alternation Not in[]() Grouping Not in[][Start Bracketed Character class Not in[]] End Bracketed Character class Only in[], and not first * Matches the preceding element 0 or more Not in[] times + Matches the preceding element 1 or more Not in[] times ? Matches the preceding element 0 or 1 Not in[] times
{
    Starts a sequence that gives number(s) Not in[] of times the preceding element can be
        matched{when following certain escape sequences
                    starts a modifier to the meaning of the
                        sequence} End sequence started by
    {
        -Indicates a range Only in[] interior
#Beginning of comment, extends to line end Only with / x modifier
 

 Notice that most of the metacharacters lose their special meaning when they occur in a bracketed character class, except <tt>&quot;^&quot;</tt> has a different meaning when it is at the beginning of such a class. And <tt>&quot;-&quot;</tt> and <tt>&quot;]&quot;</tt> are metacharacters only at restricted positions within bracketed character classes; while <tt>&quot;}&quot;</tt> is a metacharacter only when closing a special construct started by <tt>&quot;{&quot;</tt>. 

 In double-quotish context, as is usually the case, you need to be careful about <tt>&quot;$&quot;</tt> and the non-metacharacter <tt>&quot;@&quot;</tt>. Those could interpolate variables, which may or may not be what you intended. 

 These rules were designed for compactness of expression, rather than legibility and maintainability. The ``/x and /xx'' pattern modifiers allow you to insert white space to improve readability. And use of <tt>&quot;re 'strict'&quot;</tt> adds extra checking to catch some typos that might silently compile into something unintended. 

 By default, the <tt>&quot;^&quot;</tt> character is guaranteed to match only the beginning of the string, the <tt>&quot;$&quot;</tt> character only the end (or before the newline at the end), and Perl does certain optimizations with the assumption that the string contains only one line. Embedded newlines will not be matched by <tt>&quot;^&quot;</tt> or <tt>&quot;$&quot;</tt>. You may, however, wish to treat a string as a multi-line buffer, such that the <tt>&quot;^&quot;</tt> will match after any newline within the string (except if the newline is the last character in the string), and <tt>&quot;$&quot;</tt> will match before any newline. At the cost of a little more overhead, you can do this by using the &quot;<tt>&quot;/m&quot;</tt>&quot; modifier on the pattern match operator. (Older programs did this by setting <tt>$*</tt>, but this option was removed in perl 5.10.) 

 To simplify multi-line substitutions, the <tt>&quot;.&quot;</tt> character never matches a newline unless you use the <tt>&quot;/s&quot;</tt> modifier, which in effect tells Perl to pretend the string is a single line---even if it isn't.

<h3>Modifiers</h3>

 <i>Overview</i> 

 The default behavior for matching can be changed, using various modifiers. Modifiers that relate to the interpretation of the pattern are listed just below. Modifiers that alter the way a pattern is used by Perl are detailed in ``Regexp Quote-Like Operators'' in perlop and ``Gory details of parsing quoted constructs'' in perlop.
<dl>
<dt>&quot;m&quot;
<dd> Treat the string being matched against as multiple lines. That is, change <tt>&quot;^&quot;</tt> and <tt>&quot;$&quot;</tt> from matching the start of the string's first line and the end of its last line to matching the start and end of each line within the string.
<dt>&quot;s&quot;
<dd> Treat the string as single line. That is, change <tt>&quot;.&quot;</tt> to match any character whatsoever, even a newline, which normally it would not match. 

 Used together, as <tt>&quot;/ms&quot;</tt>, they let the <tt>&quot;.&quot;</tt> match any character whatsoever, while still allowing <tt>&quot;^&quot;</tt> and <tt>&quot;$&quot;</tt> to match, respectively, just after and just before newlines within the string.
<dt>&quot;i&quot;
<dd> Do case-insensitive pattern matching. For example, ``A'' will match ``a'' under <tt>&quot;/i&quot;</tt>. 

 If locale matching rules are in effect, the case map is taken from the current locale for code points less than 255, and from Unicode rules for larger code points. However, matches that would cross the Unicode rules/non-Unicode rules boundary (ords 255/256) will not succeed, unless the locale is a <font SIZE="-1">UTF-8</font> one. See perllocale. 

 There are a number of Unicode characters that match a sequence of multiple characters under <tt>&quot;/i&quot;</tt>. For example, <tt>&quot;LATIN SMALL LIGATURE FI&quot;</tt> should match the sequence <tt>&quot;fi&quot;</tt>. Perl is not currently able to do this when the multiple characters are in the pattern and are split between groupings, or when one or more are quantified. Thus 

 
"\N{LATIN SMALL LIGATURE FI}" = ~ / fi / i;
#Matches
    "\N{LATIN SMALL LIGATURE FI}" = ~ / [fi][fi] / i;
#Doesn't match! "\N{LATIN SMALL LIGATURE FI}" = ~ / fi * / i;
#Doesn't match!
#The below doesn 't match, and it isn' t clear what $1 and $2 would
#be even if it did !!
    "\N{LATIN SMALL LIGATURE FI}" = ~ / (f)(i) / i;
#Doesn't match!
 

 Perl doesn't match multiple characters in a bracketed character class unless the character that maps to them is explicitly mentioned, and it doesn't match them at all if the character class is inverted, which otherwise could be highly confusing. See ``Bracketed Character Classes'' in perlrecharclass, and ``Negation'' in perlrecharclass.
<dt>&quot;x&quot; and &quot;xx&quot;
<dd> Extend your pattern's legibility by permitting whitespace and comments. Details in ``/x and /xx''
<dt>&quot;p&quot;
<dd> Preserve the string matched such that <tt>&quot;${^PREMATCH}&quot;</tt>, <tt>&quot;${^MATCH}&quot;</tt>, and <tt>&quot;${^POSTMATCH}&quot;</tt> are available for use after matching. 

 In Perl 5.20 and higher this is ignored. Due to a new copy-on-write mechanism, <tt>&quot;${^PREMATCH}&quot;</tt>, <tt>&quot;${^MATCH}&quot;</tt>, and <tt>&quot;${^POSTMATCH}&quot;</tt> will be available after the match regardless of the modifier.
<dt>&quot;a&quot;, &quot;d&quot;, &quot;l&quot;, and &quot;u&quot;
<dd> These modifiers, all new in 5.14, affect which character-set rules (Unicode, <i>etc</i>.) are used, as described below in ``Character set modifiers''.
<dt>&quot;n&quot;
<dd> Prevent the grouping metacharacters <tt>&quot;()&quot;</tt> from capturing. This modifier, new in 5.22, will stop <tt>$1</tt>, <tt>$2</tt>, <i>etc</i>... from being filled in. 

 
"hello" = ~ / (hi | hello) / ;
#$1 is "hello"
       "hello" = ~ / (hi | hello) / n;
#$1 is undef
 

 This is equivalent to putting <tt>&quot;?:&quot;</tt> at the beginning of every capturing group: 

 <pre>
  &quot;hello&quot; =~ /(?:hi|hello)/; # $1 is undef
</pre> 

 <tt>&quot;/n&quot;</tt> can be negated on a per-group basis. Alternatively, named captures may still be used. 

 
"hello" = ~ / (? -n : (hi | hello)) / n;
#$1 is "hello"
       "hello" = ~ / (? &lt;greet&gt; hi | hello) / n;
#$1 is "hello", $ + {greet } is
#"hello"

<dt>Other Modifiers
<dd> There are a number of flags that can be found at the end of regular expression constructs that are <i>not</i> generic regular expression flags, but apply to the operation being performed, like matching or substitution (<tt>&quot;m//&quot;</tt> or <tt>&quot;s///&quot;</tt> respectively). 

 Flags described further in ``Using regular expressions in Perl'' in perlretut are: 

 <pre>
  c  - keep the current position during repeated matching
  g  - globally match the pattern repeatedly in the string
</pre> 

 Substitution-specific modifiers described in ``s/PATTERN/REPLACEMENT/msixpodualngcer'' in perlop are: 

 <pre>
  e  - evaluate the right-hand side as an expression
  ee - evaluate the right side as a string then eval the result
  o  - pretend to optimize your code, but actually introduce bugs
  r  - perform non-destructive substitution and return the new value
</pre></dl>
 

 Regular expression modifiers are usually written in documentation as <i>e.g.</i>, &quot;the <tt>&quot;/x&quot;</tt> modifier&quot;, even though the delimiter in question might not really be a slash. The modifiers <tt>&quot;/imnsxadlup&quot;</tt> may also be embedded within the regular expression itself using the <tt>&quot;(?...)&quot;</tt> construct, see ``Extended Patterns'' below. 

 <i>Details on some modifiers</i> 

 Some of the modifiers require more explanation than given in the ``Overview'' above. 

 <tt>&quot;/x&quot;</tt> and <tt>&quot;/xx&quot;</tt> 

 A single <tt>&quot;/x&quot;</tt> tells the regular expression parser to ignore most whitespace that is neither backslashed nor within a bracketed character class. You can use this to break up your regular expression into more readable parts. Also, the <tt>&quot;#&quot;</tt> character is treated as a metacharacter introducing a comment that runs up to the pattern's closing delimiter, or to the end of the current line if the pattern extends onto the next line. Hence, this is very much like an ordinary Perl code comment. (You can include the closing delimiter within the comment only if you precede it with a backslash, so be careful!) 

 Use of <tt>&quot;/x&quot;</tt> means that if you want real whitespace or <tt>&quot;#&quot;</tt> characters in the pattern (outside a bracketed character class, which is unaffected by <tt>&quot;/x&quot;</tt>), then you'll either have to escape them (using backslashes or <tt>&quot;\Q...\E&quot;</tt>) or encode them using octal, hex, or <tt>&quot;\N{}&quot;</tt> escapes. It is ineffective to try to continue a comment onto the next line by escaping the <tt>&quot;\n&quot;</tt> with a backslash or <tt>&quot;\Q&quot;</tt>. 

 You can use ``(?#text)'' to create a comment that ends earlier than the end of the current line, but <tt>&quot;text&quot;</tt> also can't contain the closing delimiter unless escaped with a backslash. 

 A common pitfall is to forget that <tt>&quot;#&quot;</tt> characters begin a comment under <tt>&quot;/x&quot;</tt> and are not matched literally. Just keep that in mind when trying to puzzle out why a particular <tt>&quot;/x&quot;</tt> pattern isn't working as expected. 

 Starting in Perl v5.26, if the modifier has a second <tt>&quot;x&quot;</tt> within it, it does everything that a single <tt>&quot;/x&quot;</tt> does, but additionally non-backslashed <font SIZE="-1">SPACE</font> and <font SIZE="-1">TAB</font> characters within bracketed character classes are also generally ignored, and hence can be added to make the classes more readable. 

 
    / [d-e g-i 3-7]/xx
    /[ ! @ " # $ % ^ &amp; * () = ? &lt;&gt; ' ]/xx
 

 may be easier to grasp than the squashed equivalents 

 
    /[d-eg-i3-7]/
    /[!@"#$%^&amp;*()=?&lt;&gt;']/
 

 Taken together, these features go a long way towards making Perl's regular expressions more readable. Here's an example: 

 
#Delete(most) C comments.
$program = ~s{
    /\* #Match the opening delimiter..*? #Match a minimal number of characters.
        \* / #Match the closing delimiter.}[] gsx;
 

 Note that anything inside a <tt>&quot;\Q...\E&quot;</tt> stays unaffected by <tt>&quot;/x&quot;</tt>. And note that <tt>&quot;/x&quot;</tt> doesn't affect space interpretation within a single multi-character construct. For example in <tt>&quot;\x{...}&quot;</tt>, regardless of the <tt>&quot;/x&quot;</tt> modifier, there can be no spaces. Same for a quantifier such as <tt>&quot;{3}&quot;</tt> or <tt>&quot;{5,}&quot;</tt>. Similarly, <tt>&quot;(?:...)&quot;</tt> can't have a space between the <tt>&quot;(&quot;</tt>, <tt>&quot;?&quot;</tt>, and <tt>&quot;:&quot;</tt>. Within any delimiters for such a construct, allowed spaces are not affected by <tt>&quot;/x&quot;</tt>, and depend on the construct. For example, <tt>&quot;\x{...}&quot;</tt> can't have spaces because hexadecimal numbers don't have spaces in them. But, Unicode properties can have spaces, so in <tt>&quot;\p{...}&quot;</tt> there can be spaces that follow the Unicode rules, for which see ``Properties accessible through \p{} and \P{}'' in perluniprops. 

 The set of characters that are deemed whitespace are those that Unicode calls ``Pattern White Space'', namely: 

 <pre>
 U+0009 CHARACTER TABULATION
 U+000A LINE FEED
 U+000B LINE TABULATION
 U+000C FORM FEED
 U+000D CARRIAGE RETURN
 U+0020 SPACE
 U+0085 NEXT LINE
 U+200E LEFT-TO-RIGHT MARK
 U+200F RIGHT-TO-LEFT MARK
 U+2028 LINE SEPARATOR
 U+2029 PARAGRAPH SEPARATOR
</pre> 

 Character set modifiers 

 <tt>&quot;/d&quot;</tt>, <tt>&quot;/u&quot;</tt>, <tt>&quot;/a&quot;</tt>, and <tt>&quot;/l&quot;</tt>, available starting in 5.14, are called the character set modifiers; they affect the character set rules used for the regular expression. 

 The <tt>&quot;/d&quot;</tt>, <tt>&quot;/u&quot;</tt>, and <tt>&quot;/l&quot;</tt> modifiers are not likely to be of much use to you, and so you need not worry about them very much. They exist for Perl's internal use, so that complex regular expression data structures can be automatically serialized and later exactly reconstituted, including all their nuances. But, since Perl can't keep a secret, and there may be rare instances where they are useful, they are documented here. 

 The <tt>&quot;/a&quot;</tt> modifier, on the other hand, may be useful. Its purpose is to allow code that is to work mostly on <font SIZE="-1">ASCII</font> data to not have to concern itself with Unicode. 

 Briefly, <tt>&quot;/l&quot;</tt> sets the character set to that of whatever <b>L</b>ocale is in effect at the time of the execution of the pattern match. 

 <tt>&quot;/u&quot;</tt> sets the character set to <b>U</b>nicode. 

 <tt>&quot;/a&quot;</tt> also sets the character set to Unicode, <font SIZE="-1">BUT</font> adds several restrictions for <b>A</b>SCII-safe matching. 

 <tt>&quot;/d&quot;</tt> is the old, problematic, pre-5.14 <b>D</b>efault character set behavior. Its only use is to force that old behavior. 

 At any given time, exactly one of these modifiers is in effect. Their existence allows Perl to keep the originally compiled behavior of a regular expression, regardless of what rules are in effect when it is actually executed. And if it is interpolated into a larger regex, the original's rules continue to apply to it, and don't affect the other parts. 

 The <tt>&quot;/l&quot;</tt> and <tt>&quot;/u&quot;</tt> modifiers are automatically selected for regular expressions compiled within the scope of various pragmas, and we recommend that in general, you use those pragmas instead of specifying these modifiers explicitly. For one thing, the modifiers affect only pattern matching, and do not extend to even any replacement done, whereas using the pragmas gives consistent results for all appropriate operations within their scopes. For example, 

 <pre>
 s/foo/\Ubar/il
</pre> 

 will match ``foo'' using the locale's rules for case-insensitive matching, but the <tt>&quot;/l&quot;</tt> does not affect how the <tt>&quot;\U&quot;</tt> operates. Most likely you want both of them to use locale rules. To do this, instead compile the regular expression within the scope of <tt>&quot;use locale&quot;</tt>. This both implicitly adds the <tt>&quot;/l&quot;</tt>, and applies locale rules to the <tt>&quot;\U&quot;</tt>. The lesson is to <tt>&quot;use locale&quot;</tt>, and not <tt>&quot;/l&quot;</tt> explicitly. 

 Similarly, it would be better to use <tt>&quot;use feature 'unicode_strings'&quot;</tt> instead of, 

 <pre>
 s/foo/\Lbar/iu
</pre> 

 to get Unicode rules, as the <tt>&quot;\L&quot;</tt> in the former (but not necessarily the latter) would also use Unicode rules. 

 More detail on each of the modifiers follows. Most likely you don't need to know this detail for <tt>&quot;/l&quot;</tt>, <tt>&quot;/u&quot;</tt>, and <tt>&quot;/d&quot;</tt>, and can skip ahead to /a. 

 /l 

 means to use the current locale's rules (see perllocale) when pattern matching. For example, <tt>&quot;\w&quot;</tt> will match the ``word'' characters of that locale, and <tt>&quot;/i&quot;</tt> case-insensitive matching will match according to the locale's case folding rules. The locale used will be the one in effect at the time of execution of the pattern match. This may not be the same as the compilation-time locale, and can differ from one match to another if there is an intervening call of the <b>setlocale()</b> function. 

 Prior to v5.20, Perl did not support multi-byte locales. Starting then, <font SIZE="-1">UTF-8</font> locales are supported. No other multi byte locales are ever likely to be supported. However, in all locales, one can have code points above 255 and these will always be treated as Unicode no matter what locale is in effect. 

 Under Unicode rules, there are a few case-insensitive matches that cross the 255/256 boundary. Except for <font SIZE="-1">UTF-8</font> locales in Perls v5.20 and later, these are disallowed under <tt>&quot;/l&quot;</tt>. For example, 0xFF (on <font SIZE="-1">ASCII</font> platforms) does not caselessly match the character at 0x178, <tt>&quot;LATIN CAPITAL LETTER Y WITH DIAERESIS&quot;</tt>, because 0xFF may not be <tt>&quot;LATIN SMALL LETTER Y WITH DIAERESIS&quot;</tt> in the current locale, and Perl has no way of knowing if that character even exists in the locale, much less what code point it is. 

 In a <font SIZE="-1">UTF-8</font> locale in v5.20 and later, the only visible difference between locale and non-locale in regular expressions should be tainting (see perlsec). 

 This modifier may be specified to be the default by <tt>&quot;use locale&quot;</tt>, but see ``Which character set modifier is in effect?''. 

 /u 

 means to use Unicode rules when pattern matching. On <font SIZE="-1">ASCII</font> platforms, this means that the code points between 128 and 255 take on their Latin-1 (<font SIZE="-1">ISO-8859-1</font>) meanings (which are the same as Unicode's). (Otherwise Perl considers their meanings to be undefined.) Thus, under this modifier, the <font SIZE="-1">ASCII</font> platform effectively becomes a Unicode platform; and hence, for example, <tt>&quot;\w&quot;</tt> will match any of the more than 100_000 word characters in Unicode. 

 Unlike most locales, which are specific to a language and country pair, Unicode classifies all the characters that are letters <i>somewhere</i> in the world as <tt>&quot;\w&quot;</tt>. For example, your locale might not think that <tt>&quot;LATIN SMALL LETTER ETH&quot;</tt> is a letter (unless you happen to speak Icelandic), but Unicode does. Similarly, all the characters that are decimal digits somewhere in the world will match <tt>&quot;\d&quot;</tt>; this is hundreds, not 10, possible matches. And some of those digits look like some of the 10 <font SIZE="-1">ASCII</font> digits, but mean a different number, so a human could easily think a number is a different quantity than it really is. For example, <tt>&quot;BENGALI DIGIT FOUR&quot;</tt> (U+09EA) looks very much like an <tt>&quot;ASCII DIGIT EIGHT&quot;</tt> (U+0038), and <tt>&quot;LEPCHA DIGIT SIX&quot;</tt> (U+1C46) looks very much like an <tt>&quot;ASCII DIGIT FIVE&quot;</tt> (U+0035). And, <tt>&quot;\d+&quot;</tt>, may match strings of digits that are a mixture from different writing systems, creating a security issue. A fraudulent website, for example, could display the price of something using U+1C46, and it would appear to the user that something cost 500 units, but it really costs 600. A browser that enforced script runs (``Script Runs'') would prevent that fraudulent display. ``<b>num()</b>'' in Unicode::UCD can also be used to sort this out. Or the <tt>&quot;/a&quot;</tt> modifier can be used to force <tt>&quot;\d&quot;</tt> to match just the <font SIZE="-1">ASCII 0</font> through 9. 

 Also, under this modifier, case-insensitive matching works on the full set of Unicode characters. The <tt>&quot;KELVIN SIGN&quot;</tt>, for example matches the letters ``k'' and ``K''; and <tt>&quot;LATIN SMALL LIGATURE FF&quot;</tt> matches the sequence ``ff'', which, if you're not prepared, might make it look like a hexadecimal constant, presenting another potential security issue. See &lt;<a rel="nofollow" HREF="http://unicode.org/reports/tr36">http://unicode.org/reports/tr36</a>&gt; for a detailed discussion of Unicode security issues. 

 This modifier may be specified to be the default by <tt>&quot;use feature 'unicode_strings&quot;</tt>, <tt>&quot;use locale ':not_characters'&quot;</tt>, or <tt>&quot;use 5.012&quot;</tt> (or higher), but see ``Which character set modifier is in effect?''. 

 /d 

 This modifier means to use the ``Default'' native rules of the platform except when there is cause to use Unicode rules instead, as follows:
<dl>
<dt>1.
<dd> the target string is encoded in <font SIZE="-1">UTF-8</font>; or
<dt>2.
<dd> the pattern is encoded in <font SIZE="-1">UTF-8</font>; or
<dt>3.
<dd> the pattern explicitly mentions a code point that is above 255 (say by <tt>&quot;\x{100}&quot;</tt>); or
<dt>4.
<dd> the pattern uses a Unicode name (<tt>&quot;\N{...}&quot;</tt>); or
<dt>5.
<dd> the pattern uses a Unicode property (<tt>&quot;\p{...}&quot;</tt> or <tt>&quot;\P{...}&quot;</tt>); or
<dt>6.
<dd> the pattern uses a Unicode break (<tt>&quot;\b{...}&quot;</tt> or <tt>&quot;\B{...}&quot;</tt>); or
<dt>7.
<dd> the pattern uses &quot;<tt>&quot;(?[ ])&quot;</tt>&quot;
<dt>8.
<dd> the pattern uses <tt>&quot;(*script_run: ...)&quot;</tt></dl>
 

 Another mnemonic for this modifier is ``Depends'', as the rules actually used depend on various things, and as a result you can get unexpected results. See ``The ''Unicode Bug&quot;&quot; in perlunicode. The Unicode Bug has become rather infamous, leading to yet another (without swearing) name for this modifier, ``Dodgy''. 

 Unless the pattern or string are encoded in <font SIZE="-1">UTF-8,</font> only <font SIZE="-1">ASCII</font> characters can match positively. 

 Here are some examples of how that works on an <font SIZE="-1">ASCII</font> platform: 

 
$str = "\xDF";
#$str is not in UTF - 8 format.$str = ~ / ^\w / ;
#No match, as $str isn't in UTF-8 format. $str.= "\x{0e0b}";
#Now $str is in UTF - 8 format.$str = ~ / ^\w / ;
#Match !$str is now in UTF - 8 format.chop $str;
$str = ~ / ^\w / ;
#Still a match !$str remains in UTF - 8 format.
 

 This modifier is automatically selected by default when none of the others are, so yet another name for it is ``Default''. 

 Because of the unexpected behaviors associated with this modifier, you probably should only explicitly use it to maintain weird backward compatibilities. 

 /a (and /aa) 

 This modifier stands for ASCII-restrict (or ASCII-safe). This modifier may be doubled-up to increase its effect. 

 When it appears singly, it causes the sequences <tt>&quot;\d&quot;</tt>, <tt>&quot;\s&quot;</tt>, <tt>&quot;\w&quot;</tt>, and the Posix character classes to match only in the <font SIZE="-1">ASCII</font> range. They thus revert to their pre-5.6, pre-Unicode meanings. Under <tt>&quot;/a&quot;</tt>, <tt>&quot;\d&quot;</tt> always means precisely the digits <tt>&quot;0&quot;</tt> to <tt>&quot;9&quot;</tt>; <tt>&quot;\s&quot;</tt> means the five characters <tt>&quot;[ \f\n\r\t]&quot;</tt>, and starting in Perl v5.18, the vertical tab; <tt>&quot;\w&quot;</tt> means the 63 characters <tt>&quot;[A-Za-z0-9_]&quot;</tt>; and likewise, all the Posix classes such as <tt>&quot;[[:print:]]&quot;</tt> match only the appropriate ASCII-range characters. 

 This modifier is useful for people who only incidentally use Unicode, and who do not wish to be burdened with its complexities and security concerns. 

 With <tt>&quot;/a&quot;</tt>, one can write <tt>&quot;\d&quot;</tt> with confidence that it will only match <font SIZE="-1">ASCII</font> characters, and should the need arise to match beyond <font SIZE="-1">ASCII,</font> you can instead use <tt>&quot;\p{Digit}&quot;</tt> (or <tt>&quot;\p{Word}&quot;</tt> for <tt>&quot;\w&quot;</tt>). There are similar <tt>&quot;\p{...}&quot;</tt> constructs that can match beyond <font SIZE="-1">ASCII</font> both white space (see ``Whitespace'' in perlrecharclass), and Posix classes (see ``<font SIZE="-1">POSIX</font> Character Classes'' in perlrecharclass). Thus, this modifier doesn't mean you can't use Unicode, it means that to get Unicode matching you must explicitly use a construct (<tt>&quot;\p{}&quot;</tt>, <tt>&quot;\P{}&quot;</tt>) that signals Unicode. 

 As you would expect, this modifier causes, for example, <tt>&quot;\D&quot;</tt> to mean the same thing as <tt>&quot;[^0-9]&quot;</tt>; in fact, all non-ASCII characters match <tt>&quot;\D&quot;</tt>, <tt>&quot;\S&quot;</tt>, and <tt>&quot;\W&quot;</tt>. <tt>&quot;\b&quot;</tt> still means to match at the boundary between <tt>&quot;\w&quot;</tt> and <tt>&quot;\W&quot;</tt>, using the <tt>&quot;/a&quot;</tt> definitions of them (similarly for <tt>&quot;\B&quot;</tt>). 

 Otherwise, <tt>&quot;/a&quot;</tt> behaves like the <tt>&quot;/u&quot;</tt> modifier, in that case-insensitive matching uses Unicode rules; for example, ``k'' will match the Unicode <tt>&quot;\N{KELVIN SIGN}&quot;</tt> under <tt>&quot;/i&quot;</tt> matching, and code points in the Latin1 range, above <font SIZE="-1">ASCII</font> will have Unicode rules when it comes to case-insensitive matching. 

 To forbid ASCII/non-ASCII matches (like ``k'' with <tt>&quot;\N{KELVIN SIGN}&quot;</tt>), specify the <tt>&quot;a&quot;</tt> twice, for example <tt>&quot;/aai&quot;</tt> or <tt>&quot;/aia&quot;</tt>. (The first occurrence of <tt>&quot;a&quot;</tt> restricts the <tt>&quot;\d&quot;</tt>, <i>etc</i>., and the second occurrence adds the <tt>&quot;/i&quot;</tt> restrictions.) But, note that code points outside the <font SIZE="-1">ASCII</font> range will use Unicode rules for <tt>&quot;/i&quot;</tt> matching, so the modifier doesn't really restrict things to just <font SIZE="-1">ASCII</font>; it just forbids the intermixing of <font SIZE="-1">ASCII</font> and non-ASCII. 

 To summarize, this modifier provides protection for applications that don't wish to be exposed to all of Unicode. Specifying it twice gives added protection. 

 This modifier may be specified to be the default by <tt>&quot;use re '/a'&quot;</tt> or <tt>&quot;use re '/aa'&quot;</tt>. If you do so, you may actually have occasion to use the <tt>&quot;/u&quot;</tt> modifier explicitly if there are a few regular expressions where you do want full Unicode rules (but even here, it's best if everything were under feature <tt>&quot;unicode_strings&quot;</tt>, along with the <tt>&quot;use re '/aa'&quot;</tt>). Also see ``Which character set modifier is in effect?''. 

 Which character set modifier is in effect? 

 Which of these modifiers is in effect at any given point in a regular expression depends on a fairly complex set of interactions. These have been designed so that in general you don't have to worry about it, but this section gives the gory details. As explained below in ``Extended Patterns'' it is possible to explicitly specify modifiers that apply only to portions of a regular expression. The innermost always has priority over any outer ones, and one applying to the whole expression has priority over any of the default settings that are described in the remainder of this section. 

 The <tt>&quot;use re '/foo'&quot;</tt> pragma can be used to set default modifiers (including these) for regular expressions compiled within its scope. This pragma has precedence over the other pragmas listed below that also change the defaults. 

 Otherwise, <tt>&quot;use locale&quot;</tt> sets the default modifier to <tt>&quot;/l&quot;</tt>; and <tt>&quot;use feature 'unicode_strings&quot;</tt>, or <tt>&quot;use 5.012&quot;</tt> (or higher) set the default to <tt>&quot;/u&quot;</tt> when not in the same scope as either <tt>&quot;use locale&quot;</tt> or <tt>&quot;use bytes&quot;</tt>. (<tt>&quot;use locale ':not_characters'&quot;</tt> also sets the default to <tt>&quot;/u&quot;</tt>, overriding any plain <tt>&quot;use locale&quot;</tt>.) Unlike the mechanisms mentioned above, these affect operations besides regular expressions pattern matching, and so give more consistent results with other operators, including using <tt>&quot;\U&quot;</tt>, <tt>&quot;\l&quot;</tt>, <i>etc</i>. in substitution replacements. 

 If none of the above apply, for backwards compatibility reasons, the <tt>&quot;/d&quot;</tt> modifier is the one in effect by default. As this can lead to unexpected results, it is best to specify which other rule set should be used. 

 Character set modifier behavior prior to Perl 5.14 

 Prior to 5.14, there were no explicit modifiers, but <tt>&quot;/l&quot;</tt> was implied for regexes compiled within the scope of <tt>&quot;use locale&quot;</tt>, and <tt>&quot;/d&quot;</tt> was implied otherwise. However, interpolating a regex into a larger regex would ignore the original compilation in favor of whatever was in effect at the time of the second compilation. There were a number of inconsistencies (bugs) with the <tt>&quot;/d&quot;</tt> modifier, where Unicode rules would be used when inappropriate, and vice versa. <tt>&quot;\p{}&quot;</tt> did not imply Unicode rules, and neither did all occurrences of <tt>&quot;\N{}&quot;</tt>, until 5.12.

<h3>Regular Expressions</h3>

 <i>Quantifiers</i> 

 Quantifiers are used when a particular portion of a pattern needs to match a certain number (or numbers) of times. If there isn't a quantifier the number of times to match is exactly one. The following standard quantifiers are recognized: 

 
*Match 0 or more times + Match 1 or more times
    ? Match 1 or 0 times{n} Match exactly n times{
                     n,
                 } Match at least n times{n, m} Match at least n but not more than m times
 

 (If a non-escaped curly bracket occurs in a context other than one of the quantifiers listed above, where it does not form part of a backslashed sequence like <tt>&quot;\x{...}&quot;</tt>, it is either a fatal syntax error, or treated as a regular character, generally with a deprecation warning raised. To escape it, you can precede it with a backslash (<tt>&quot;\{&quot;</tt>) or enclose it within square brackets (<tt>&quot;[{]&quot;</tt>). This change will allow for future syntax extensions (like making the lower bound of a quantifier optional), and better error checking of quantifiers). 

 The <tt>&quot;*&quot;</tt> quantifier is equivalent to <tt>&quot;{0,}&quot;</tt>, the <tt>&quot;+&quot;</tt> quantifier to <tt>&quot;{1,}&quot;</tt>, and the <tt>&quot;?&quot;</tt> quantifier to <tt>&quot;{0,1}&quot;</tt>. <i>n</i> and <i>m</i> are limited to non-negative integral values less than a preset limit defined when perl is built. This is usually 32766 on the most common platforms. The actual limit can be seen in the error message generated by code such as this: 

 
    $_ **= $_ , / {$_} / for 2 .. 42;
 

 By default, a quantified subpattern is ``greedy'', that is, it will match as many times as possible (given a particular starting location) while still allowing the rest of the pattern to match. If you want it to match the minimum number of times possible, follow the quantifier with a <tt>&quot;?&quot;</tt>. Note that the meanings don't change, just the ``greediness'': 

 
*? Match 0 or more times, not greedily + ? Match 1 or more times, not greedily ? ? Match 0 or 1 time, not greedily{n} ? Match exactly n times, not greedily(redundant){
                                                                                                                                                   n,
                                                                                                                                               }
? Match at least n times,
    not greedily{n, m} ? Match at least n but not more than m times, not greedily
 

 Normally when a quantified subpattern does not allow the rest of the overall pattern to match, Perl will backtrack. However, this behaviour is sometimes undesirable. Thus Perl provides the ``possessive'' quantifier form as well. 

 
*+Match 0 or more times and give nothing back++ Match 1 or more times and give nothing back
    ? +Match 0 or 1 time and give nothing back{n} + Match exactly n times and give nothing back(redundant){
                                                        n,
                                                    } +
                          Match at least n times and give nothing back{n, m} + Match at least n but not more than m times
                      and give nothing back
 

 For instance, 

 <pre>
   'aaaa' =~ /a++a/
</pre> 

 will never match, as the <tt>&quot;a++&quot;</tt> will gobble up all the <tt>&quot;a&quot;</tt>'s in the string and won't leave any for the remaining part of the pattern. This feature can be extremely useful to give perl hints about where it shouldn't backtrack. For instance, the typical ``match a double-quoted string'' problem can be most efficiently performed when written as: 

 <pre>
   /&quot;(?:[^&quot;\\]++|\\.)*+&quot;/
</pre> 

 as we know that if the final quote does not match, backtracking will not help. See the independent subexpression &quot;<tt>&quot;(?&gt;</tt>pattern<tt>)&quot;</tt>&quot; for more details; possessive quantifiers are just syntactic sugar for that construct. For instance the above example could also be written as follows: 

 <pre>
   /&quot;(?&gt;(?:(?&gt;[^&quot;\\]+)|\\.)*)&quot;/
</pre> 

 Note that the possessive quantifier modifier can not be combined with the non-greedy modifier. This is because it would make no sense. Consider the follow equivalency table: 

 
Illegal Legal-- -- -- -- -- -- -- -- --X ? ? +X{0} X + ? +X{1} X{min, max} ? +X
{
    min
}
 

 <i>Escape sequences</i> 

 Because patterns are processed as double-quoted strings, the following also work: 

 
\t tab(HT, TAB)
 \n newline(LF, NL)
 \r return (CR)
 \f form feed(FF)
 \a alarm(bell)(BEL)
 \e escape(think troff)(ESC)
 \cK control char(example
                   : VT)
 \x{}, \x00 character whose ordinal is the given hexadecimal number
 \N{name} named Unicode character or character sequence
 \N{U + 263D} Unicode character(example
                                      : FIRST QUARTER MOON)
 \o{}, \000 character whose ordinal is the given octal number
 \l lowercase next char(think vi)
 \u uppercase next char(think vi)
 \L lowercase until \E(think vi)
 \U uppercase until \E(think vi)
 \Q quote(disable)
pattern metacharacters until \E
 \E end either case modification or quoted section, think vi
 

 Details are in ``Quote and Quote-like Operators'' in perlop. 

 <i>Character Classes and other Special Escapes</i> 

 In addition, Perl defines the following: 

 
 Sequence   Note    Description
  [...]     [1]  Match a character according to the rules of the
                   bracketed character class defined by the "...".
                   Example: [a-z] matches "a" or "b" or "c" ... or "z"
  [[:...:]] [2]  Match a character according to the rules of the POSIX
                   character class "..." within the outer bracketed
                   character class.  Example: [[:upper:]] matches any
                   uppercase character.
  (?[...])  [8]  Extended bracketed character class
  \w        [3]  Match a "word" character (alphanumeric plus "_", plus
                   other connector punctuation chars plus Unicode
                   marks)
  \W        [3]  Match a non-"word" character
  \s        [3]  Match a whitespace character
  \S        [3]  Match a non-whitespace character
  \d        [3]  Match a decimal digit character
  \D        [3]  Match a non-digit character
  \pP       [3]  Match P, named property.  Use \p
 {
     Prop
 } for longer names
  \PP       [3]  Match non-P
  \X        [4]  Match Unicode "eXtended grapheme cluster"
  \1        [5]  Backreference to a specific capture group or buffer.
                   '1' may actually be any positive integer.
  \g1       [5]  Backreference to a specific or previous group,
  \g{-1}    [5]  The number may be negative indicating a relative
                   previous group and may optionally be wrapped in
                   curly brackets for safer parsing.
  \g{name}  [5]  Named backreference
  \k&lt;name&gt;  [5]  Named backreference
  \K        [6]  Keep the stuff left of the \K, don't include it in $&amp;
  \N        [7]  Any character but \n.  Not affected by /s modifier
  \v        [3]  Vertical whitespace
  \V        [3]  Not vertical whitespace
  \h        [3]  Horizontal whitespace
  \H        [3]  Not horizontal whitespace
  \R        [4]  Linebreak

<dl>
<dt>[1]
<dd> See ``Bracketed Character Classes'' in perlrecharclass for details.
<dt>[2]
<dd> See ``<font SIZE="-1">POSIX</font> Character Classes'' in perlrecharclass for details.
<dt>[3]
<dd> See ``Unicode Character Properties'' in perlunicode for details
<dt>[4]
<dd> See ``Misc'' in perlrebackslash for details.
<dt>[5]
<dd> See ``Capture groups'' below for details.
<dt>[6]
<dd> See ``Extended Patterns'' below for details.
<dt>[7]
<dd> Note that <tt>&quot;\N&quot;</tt> has two meanings. When of the form <tt>&quot;\N{</tt>NAME<tt>}&quot;</tt>, it matches the character or character sequence whose name is <i></i><font SIZE="-1"><i>NAME</i></font><i></i>; and similarly when of the form <tt>&quot;\N{U+</tt>hex<tt>}&quot;</tt>, it matches the character whose Unicode code point is <i>hex</i>. Otherwise it matches any character but <tt>&quot;\n&quot;</tt>.
<dt>[8]
<dd> See ``Extended Bracketed Character Classes'' in perlrecharclass for details.</dl>
 

 <i>Assertions</i> 

 Besides <tt>&quot;^&quot;</tt> and <tt>&quot;$&quot;</tt>, Perl defines the following zero-width assertions: 

 
\b
{
}
Match at Unicode boundary of specified type
 \B
{
}
Match where corresponding \b
{
} doesn't match
 \b     Match a \w\W or \W\w boundary
 \B     Match except at a \w\W or \W\w boundary
 \A     Match only at beginning of string
 \Z     Match only at end of string, or before newline at the end
 \z     Match only at end of string
 \G     Match only at pos() (e.g. at the end-of-match position
        of prior m//g)
 

 A Unicode boundary (<tt>&quot;\b{}&quot;</tt>), available starting in v5.22, is a spot between two characters, or before the first character in the string, or after the final character in the string where certain criteria defined by Unicode are met. See ``\b{}, \b, \B{}, \B'' in perlrebackslash for details. 

 A word boundary (<tt>&quot;\b&quot;</tt>) is a spot between two characters that has a <tt>&quot;\w&quot;</tt> on one side of it and a <tt>&quot;\W&quot;</tt> on the other side of it (in either order), counting the imaginary characters off the beginning and end of the string as matching a <tt>&quot;\W&quot;</tt>. (Within character classes <tt>&quot;\b&quot;</tt> represents backspace rather than a word boundary, just as it normally does in any double-quoted string.) The <tt>&quot;\A&quot;</tt> and <tt>&quot;\Z&quot;</tt> are just like <tt>&quot;^&quot;</tt> and <tt>&quot;$&quot;</tt>, except that they won't match multiple times when the <tt>&quot;/m&quot;</tt> modifier is used, while <tt>&quot;^&quot;</tt> and <tt>&quot;$&quot;</tt> will match at every internal line boundary. To match the actual end of the string and not ignore an optional trailing newline, use <tt>&quot;\z&quot;</tt>. 

 The <tt>&quot;\G&quot;</tt> assertion can be used to chain global matches (using <tt>&quot;m//g&quot;</tt>), as described in ``Regexp Quote-Like Operators'' in perlop. It is also useful when writing <tt>&quot;lex&quot;</tt>-like scanners, when you have several patterns that you want to match against consequent substrings of your string; see the previous reference. The actual location where <tt>&quot;\G&quot;</tt> will match can also be influenced by using <tt>&quot;pos()&quot;</tt> as an lvalue: see ``pos'' in perlfunc. Note that the rule for zero-length matches (see ``Repeated Patterns Matching a Zero-length Substring'') is modified somewhat, in that contents to the left of <tt>&quot;\G&quot;</tt> are not counted when determining the length of the match. Thus the following will not match forever: 

 
my $string = 'ABC';
pos($string) = 1;
while ($string = ~ / (.\G) / g) {
    print $1;
}
 

 It will print 'A' and then terminate, as it considers the match to be zero-width, and thus will not match at the same position twice in a row. 

 It is worth noting that <tt>&quot;\G&quot;</tt> improperly used can result in an infinite loop. Take care when using patterns that include <tt>&quot;\G&quot;</tt> in an alternation. 

 Note also that <tt>&quot;s///&quot;</tt> will refuse to overwrite part of a substitution that has already been replaced; so for example this will stop after the first iteration, rather than iterating its way backwards through the string: 

 
$_ = "123456789";
pos = 6;
    s/.(?=.\G)/X/g;
    print;
#prints 1234X6789, not XXXXX6789
 

 <i>Capture groups</i> 

 The grouping construct <tt>&quot;( ... )&quot;</tt> creates capture groups (also referred to as capture buffers). To refer to the current contents of a group later on, within the same pattern, use <tt>&quot;\g1&quot;</tt> (or <tt>&quot;\g{1}&quot;</tt>) for the first, <tt>&quot;\g2&quot;</tt> (or <tt>&quot;\g{2}&quot;</tt>) for the second, and so on. This is called a <i>backreference</i>. 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; 
&nbsp; 
&nbsp; 
&nbsp;<wbr>&nbsp; There is no limit to the number of captured substrings that you may use. Groups are numbered with the leftmost open parenthesis being number 1, <i>etc</i>. If a group did not match, the associated backreference won't match either. (This can happen if the group is optional, or in a different branch of an alternation.) You can omit the <tt>&quot;g&quot;</tt>, and write <tt>&quot;\1&quot;</tt>, <i>etc</i>, but there are some issues with this form, described below. 

 You can also refer to capture groups relatively, by using a negative number, so that <tt>&quot;\g-1&quot;</tt> and <tt>&quot;\g{-1}&quot;</tt> both refer to the immediately preceding capture group, and <tt>&quot;\g-2&quot;</tt> and <tt>&quot;\g{-2}&quot;</tt> both refer to the group before it. For example: 

 
/
    (Y) #group 1(#group 2(X) #group 3
            \g { -1 } #backref to group 3
            \g{-3} #backref to group 1) / x
 

 would match the same as <tt>&quot;/(Y) ( (X) \g3 \g1 )/x&quot;</tt>. This allows you to interpolate regexes into larger regexes and not have to worry about the capture groups being renumbered. 

 You can dispense with numbers altogether and create named capture groups. The notation is <tt>&quot;(?&lt;</tt>name<tt>&gt;...)&quot;</tt> to declare and <tt>&quot;\g{</tt>name<tt>}&quot;</tt> to reference. (To be compatible with .Net regular expressions, <tt>&quot;\g{</tt>name<tt>}&quot;</tt> may also be written as <tt>&quot;\k{</tt>name<tt>}&quot;</tt>, <tt>&quot;\k&lt;</tt>name<tt>&gt;&quot;</tt> or <tt>&quot;\k'</tt>name<tt>'&quot;</tt>.) <i>name</i> must not begin with a number, nor contain hyphens. When different groups within the same pattern have the same name, any reference to that name assumes the leftmost defined group. Named groups count in absolute and relative numbering, and so can also be referred to by those numbers. (It's possible to do things with named capture groups that would otherwise require <tt>&quot;(??{})&quot;</tt>.) 

 Capture group contents are dynamically scoped and available to you outside the pattern until the end of the enclosing block or until the next successful match, whichever comes first. (See ``Compound Statements'' in perlsyn.) You can refer to them by absolute number (using <tt>&quot;$1&quot;</tt> instead of <tt>&quot;\g1&quot;</tt>, <i>etc</i>); or by name via the <tt>&quot;%+&quot;</tt> hash, using <tt>&quot;$+{</tt>name<tt>}&quot;</tt>. 

 Braces are required in referring to named capture groups, but are optional for absolute or relative numbered ones. Braces are safer when creating a regex by concatenating smaller strings. For example if you have <tt>&quot;qr/$a$b/&quot;</tt>, and <tt>$a</tt> contained <tt>&quot;\g1&quot;</tt>, and <tt>$b</tt> contained <tt>&quot;37&quot;</tt>, you would get <tt>&quot;/\g137/&quot;</tt> which is probably not what you intended. 

 The <tt>&quot;\g&quot;</tt> and <tt>&quot;\k&quot;</tt> notations were introduced in Perl 5.10.0. Prior to that there were no named nor relative numbered capture groups. Absolute numbered groups were referred to using <tt>&quot;\1&quot;</tt>, <tt>&quot;\2&quot;</tt>, <i>etc</i>., and this notation is still accepted (and likely always will be). But it leads to some ambiguities if there are more than 9 capture groups, as <tt>&quot;\10&quot;</tt> could mean either the tenth capture group, or the character whose ordinal in octal is 010 (a backspace in <font SIZE="-1">ASCII</font>). Perl resolves this ambiguity by interpreting <tt>&quot;\10&quot;</tt> as a backreference only if at least 10 left parentheses have opened before it. Likewise <tt>&quot;\11&quot;</tt> is a backreference only if at least 11 left parentheses have opened before it. And so on. <tt>&quot;\1&quot;</tt> through <tt>&quot;\9&quot;</tt> are always interpreted as backreferences. There are several examples below that illustrate these perils. You can avoid the ambiguity by always using <tt>&quot;\g{}&quot;</tt> or <tt>&quot;\g&quot;</tt> if you mean capturing groups; and for octal constants always using <tt>&quot;\o{}&quot;</tt>, or for <tt>&quot;\077&quot;</tt> and below, using 3 digits padded with leading zeros, since a leading zero implies an octal constant. 

 The <tt>&quot;\</tt>digit<tt>&quot;</tt> notation also works in certain circumstances outside the pattern. See ``Warning on \1 Instead of <tt>$1</tt>'' below for details. 

 Examples: 

 
s / ^([^] *)*([^] *) / $2 $1 / ;
#swap first two words / (.)\g1 / #find first doubled char and print "'$1' is the first doubled character\n";
    /(?&lt;char&gt;.)\k&lt;char&gt;/            # ... a different way
         and print "'$+{char}' is the first doubled character\n";
    /(?'char'.)\g1/                 # ... mix and match
         and print "'$1' is the first doubled character\n";
    if (/ Time
        : (..)
        : (..)
        : (..) /) {
#parse out values
            $hours = $1;
        $minutes = $2;
        $seconds = $3;
    }
    / (.)(.)(.)(.)(.)(.)(.)(.)(.)\g10 / # \g10 is a backreference
        / (.)(.)(.)(.)(.)(.)(.)(.)(.)\10 / # \10 is octal
        / ((.)(.)(.)(.)(.)(.)(.)(.)(.))\10 / # \10 is a backreference
        / ((.)(.)(.)(.)(.)(.)(.)(.)(.))\010 / # \010 is octal $a = '(.)\1';
#Creates problems when concatenated.$b = '(.)\g{1}';
#Avoids the problems."aa" = ~ / ${a } / ;
#True
        "aa" = ~ / ${b } / ;
#True
        "aa0" = ~ / $
    {
        a
    }
    0 / ;
#False !"aa0" = ~ / $
    {
        b
    }
    0 / ;
#True
        "aa\x08" = ~ / $
    {
        a
    }
    0 / ;
#True !"aa\x08" = ~ / $
    {
        b
    }
    0 / ;
#False
 

 Several special variables also refer back to portions of the previous match. <tt>$+</tt> returns whatever the last bracket match matched. <tt>$&amp;</tt> returns the entire matched string. (At one point <tt>$0</tt> did also, but now it returns the name of the program.) <tt>&quot;$`&quot;</tt> returns everything before the matched string. <tt>&quot;$'&quot;</tt> returns everything after the matched string. And <tt>$^N</tt> contains whatever was matched by the most-recently closed group (submatch). <tt>$^N</tt> can be used in extended patterns (see below), for example to assign a submatch to a variable. 

 These special variables, like the <tt>&quot;%+&quot;</tt> hash and the numbered match variables (<tt>$1</tt>, <tt>$2</tt>, <tt>$3</tt>, <i>etc</i>.) are dynamically scoped until the end of the enclosing block or until the next successful match, whichever comes first. (See ``Compound Statements'' in perlsyn.) 

 <font SIZE="-1"><b>NOTE</b></font>: Failed matches in Perl do not reset the match variables, which makes it easier to write code that tests for a series of more specific cases and remembers the best match. 

 <font SIZE="-1"><b>WARNING</b></font>: If your code is to run on Perl 5.16 or earlier, beware that once Perl sees that you need one of <tt>$&amp;</tt>, <tt>&quot;$`&quot;</tt>, or <tt>&quot;$'&quot;</tt> anywhere in the program, it has to provide them for every pattern match. This may substantially slow your program. 

 Perl uses the same mechanism to produce <tt>$1</tt>, <tt>$2</tt>, <i>etc</i>, so you also pay a price for each pattern that contains capturing parentheses. (To avoid this cost while retaining the grouping behaviour, use the extended regular expression <tt>&quot;(?: ... )&quot;</tt> instead.) But if you never use <tt>$&amp;</tt>, <tt>&quot;$`&quot;</tt> or <tt>&quot;$'&quot;</tt>, then patterns <i>without</i> capturing parentheses will not be penalized. So avoid <tt>$&amp;</tt>, <tt>&quot;$'&quot;</tt>, and <tt>&quot;$`&quot;</tt> if you can, but if you can't (and some algorithms really appreciate them), once you've used them once, use them at will, because you've already paid the price. 

 Perl 5.16 introduced a slightly more efficient mechanism that notes separately whether each of <tt>&quot;$`&quot;</tt>, <tt>$&amp;</tt>, and <tt>&quot;$'&quot;</tt> have been seen, and thus may only need to copy part of the string. Perl 5.20 introduced a much more efficient copy-on-write mechanism which eliminates any slowdown. 

 As another workaround for this problem, Perl 5.10.0 introduced <tt>&quot;${^PREMATCH}&quot;</tt>, <tt>&quot;${^MATCH}&quot;</tt> and <tt>&quot;${^POSTMATCH}&quot;</tt>, which are equivalent to <tt>&quot;$`&quot;</tt>, <tt>$&amp;</tt> and <tt>&quot;$'&quot;</tt>, <b>except</b> that they are only guaranteed to be defined after a successful match that was executed with the <tt>&quot;/p&quot;</tt> (preserve) modifier. The use of these variables incurs no global performance penalty, unlike their punctuation character equivalents, however at the trade-off that you have to tell perl when you want to use them. As of Perl 5.20, these three variables are equivalent to <tt>&quot;$`&quot;</tt>, <tt>$&amp;</tt> and <tt>&quot;$'&quot;</tt>, and <tt>&quot;/p&quot;</tt> is ignored.

<h3>Quoting metacharacters</h3>

 Backslashed metacharacters in Perl are alphanumeric, such as <tt>&quot;\b&quot;</tt>, <tt>&quot;\w&quot;</tt>, <tt>&quot;\n&quot;</tt>. Unlike some other regular expression languages, there are no backslashed symbols that aren't alphanumeric. So anything that looks like <tt>&quot;\\&quot;</tt>, <tt>&quot;\(&quot;</tt>, <tt>&quot;\)&quot;</tt>, <tt>&quot;\[&quot;</tt>, <tt>&quot;\]&quot;</tt>, <tt>&quot;\{&quot;</tt>, or <tt>&quot;\}&quot;</tt> is always interpreted as a literal character, not a metacharacter. This was once used in a common idiom to disable or quote the special meanings of regular expression metacharacters in a string that you want to use for a pattern. Simply quote all non-``word'' characters: 

 <pre>
    $pattern =~ s/(\W)/\\$1/g;
</pre> 

 (If <tt>&quot;use locale&quot;</tt> is set, then this depends on the current locale.) Today it is more common to use the <tt>&quot;quotemeta()&quot;</tt> function or the <tt>&quot;\Q&quot;</tt> metaquoting escape sequence to disable all metacharacters' special meanings like this: 

 <pre>
    /$unquoted\Q$quoted\E$unquoted/
</pre> 

 Beware that if you put literal backslashes (those not inside interpolated variables) between <tt>&quot;\Q&quot;</tt> and <tt>&quot;\E&quot;</tt>, double-quotish backslash interpolation may lead to confusing results. If you <i>need</i> to use literal backslashes within <tt>&quot;\Q...\E&quot;</tt>, consult ``Gory details of parsing quoted constructs'' in perlop. 

 <tt>&quot;quotemeta()&quot;</tt> and <tt>&quot;\Q&quot;</tt> are fully described in ``quotemeta'' in perlfunc.

<h3>Extended Patterns</h3>

 Perl also defines a consistent extension syntax for features not found in standard tools like <b>awk</b> and <b>lex</b>. The syntax for most of these is a pair of parentheses with a question mark as the first thing within the parentheses. The character after the question mark indicates the extension. 

 A question mark was chosen for this and for the minimal-matching construct because 1) question marks are rare in older regular expressions, and 2) whenever you see one, you should stop and ``question'' exactly what is going on. That's psychology....
<dl>
<dt>&quot;(?#<i>text</i>)&quot;
<dd> A comment. The <i>text</i> is ignored. Note that Perl closes the comment as soon as it sees a <tt>&quot;)&quot;</tt>, so there is no way to put a literal <tt>&quot;)&quot;</tt> in the comment. The pattern's closing delimiter must be escaped by a backslash if it appears in the comment. 

 See ``/x'' for another way to have comments in patterns. 

 Note that a comment can go just about anywhere, except in the middle of an escape sequence. Examples: 

 
 qr/foo(?#comment)bar/'  # Matches 'foobar'
#The pattern below matches 'abcd', 'abccd', or 'abcccd'
 qr/abc(?#comment between literal and its quantifier){1,3}d/
#The pattern below generates a syntax error, because the '\p' must
#be followed immediately by a '{'.
 qr/\p(?#comment between \p and its property name){Any}/
#The pattern below generates a syntax error, because the initial
#'\(' is a literal opening parenthesis, and so there is nothing
#for the closing ')' to match
 qr/\(?#the backslash means this isn't a comment)p{Any}/
#Comments can be used to fold long patterns into multiple lines
 qr/First part of a long regex(?#
   )remaining part/

<dt>&quot;(?adlupimnsx-imnsx)&quot;
<dd>
<dt>&quot;(?^alupimnsx)&quot;
<dd> Zero or more embedded pattern-match modifiers, to be turned on (or turned off if preceded by <tt>&quot;-&quot;</tt>) for the remainder of the pattern or the remainder of the enclosing pattern group (if any). 

 This is particularly useful for dynamically-generated patterns, such as those read in from a configuration file, taken from an argument, or specified in a table somewhere. Consider the case where some patterns want to be case-sensitive and some do not: The case-insensitive ones merely need to include <tt>&quot;(?i)&quot;</tt> at the front of the pattern. For example: 

 
$pattern = "foobar";
if (/ $pattern / i) {
}
#more flexible:
$pattern = "(?i)foobar";
if (/ $pattern /) {
}
 

 These modifiers are restored at the end of the enclosing group. For example, 

 <pre>
    ( (?i) blah ) \s+ \g1
</pre> 

 will match <tt>&quot;blah&quot;</tt> in any case, some spaces, and an exact (<i>including the case</i>!) repetition of the previous word, assuming the <tt>&quot;/x&quot;</tt> modifier, and no <tt>&quot;/i&quot;</tt> modifier outside this group. 

 These modifiers do not carry over into named subpatterns called in the enclosing group. In other words, a pattern such as <tt>&quot;((?i)(?&amp;</tt>NAME<tt>))&quot;</tt> does not change the case-sensitivity of the <i></i><font SIZE="-1"><i>NAME</i></font><i></i> pattern. 

 A modifier is overridden by later occurrences of this construct in the same scope containing the same modifier, so that 

 <pre>
    /((?im)foo(?-m)bar)/
</pre> 

 matches all of <tt>&quot;foobar&quot;</tt> case insensitively, but uses <tt>&quot;/m&quot;</tt> rules for only the <tt>&quot;foo&quot;</tt> portion. The <tt>&quot;a&quot;</tt> flag overrides <tt>&quot;aa&quot;</tt> as well; likewise <tt>&quot;aa&quot;</tt> overrides <tt>&quot;a&quot;</tt>. The same goes for <tt>&quot;x&quot;</tt> and <tt>&quot;xx&quot;</tt>. Hence, in 

 <pre>
    /(?-x)foo/xx
</pre> 

 both <tt>&quot;/x&quot;</tt> and <tt>&quot;/xx&quot;</tt> are turned off during matching <tt>&quot;foo&quot;</tt>. And in 

 <pre>
    /(?x)foo/x
</pre> 

 <tt>&quot;/x&quot;</tt> but <font SIZE="-1">NOT</font> <tt>&quot;/xx&quot;</tt> is turned on for matching <tt>&quot;foo&quot;</tt>. (One might mistakenly think that since the inner <tt>&quot;(?x)&quot;</tt> is already in the scope of <tt>&quot;/x&quot;</tt>, that the result would effectively be the sum of them, yielding <tt>&quot;/xx&quot;</tt>. It doesn't work that way.) Similarly, doing something like <tt>&quot;(?xx-x)foo&quot;</tt> turns off all <tt>&quot;x&quot;</tt> behavior for matching <tt>&quot;foo&quot;</tt>, it is not that you subtract 1 <tt>&quot;x&quot;</tt> from 2 to get 1 <tt>&quot;x&quot;</tt> remaining. 

 Any of these modifiers can be set to apply globally to all regular expressions compiled within the scope of a <tt>&quot;use re&quot;</tt>. See ``'/flags' mode'' in re. 

 Starting in Perl 5.14, a <tt>&quot;^&quot;</tt> (caret or circumflex accent) immediately after the <tt>&quot;?&quot;</tt> is a shorthand equivalent to <tt>&quot;d-imnsx&quot;</tt>. Flags (except <tt>&quot;d&quot;</tt>) may follow the caret to override it. But a minus sign is not legal with it. 

 Note that the <tt>&quot;a&quot;</tt>, <tt>&quot;d&quot;</tt>, <tt>&quot;l&quot;</tt>, <tt>&quot;p&quot;</tt>, and <tt>&quot;u&quot;</tt> modifiers are special in that they can only be enabled, not disabled, and the <tt>&quot;a&quot;</tt>, <tt>&quot;d&quot;</tt>, <tt>&quot;l&quot;</tt>, and <tt>&quot;u&quot;</tt> modifiers are mutually exclusive: specifying one de-specifies the others, and a maximum of one (or two <tt>&quot;a&quot;</tt>'s) may appear in the construct. Thus, for example, <tt>&quot;(?-p)&quot;</tt> will warn when compiled under <tt>&quot;use warnings&quot;</tt>; <tt>&quot;(?-d:...)&quot;</tt> and <tt>&quot;(?dl:...)&quot;</tt> are fatal errors. 

 Note also that the <tt>&quot;p&quot;</tt> modifier is special in that its presence anywhere in a pattern has a global effect. 

 Having zero modifiers makes this a no-op (so why did you specify it, unless it's generated code), and starting in v5.30, warns under <tt>&quot;use re 'strict'&quot;</tt>.
<dt>&quot;(?:<i>pattern</i>)&quot;
<dd>
<dt>&quot;(?adluimnsx-imnsx:<i>pattern</i>)&quot;
<dd>
<dt>&quot;(?^aluimnsx:<i>pattern</i>)&quot;
<dd> This is for clustering, not capturing; it groups subexpressions like <tt>&quot;()&quot;</tt>, but doesn't make backreferences as <tt>&quot;()&quot;</tt> does. So 

 <pre>
    @fields = split(/\b(?:a|b|c)\b/)
</pre> 

 matches the same field delimiters as 

 <pre>
    @fields = split(/\b(a|b|c)\b/)
</pre> 

 but doesn't spit out the delimiters themselves as extra fields (even though that's the behaviour of ``split'' in perlfunc when its pattern contains capturing groups). It's also cheaper not to capture characters if you don't need to. 

 Any letters between <tt>&quot;?&quot;</tt> and <tt>&quot;:&quot;</tt> act as flags modifiers as with <tt>&quot;(?adluimnsx-imnsx)&quot;</tt>. For example, 

 <pre>
    /(?s-i:more.*than).*million/i
</pre> 

 is equivalent to the more verbose 

 <pre>
    /(?:(?s-i)more.*than).*million/i
</pre> 

 Note that any <tt>&quot;()&quot;</tt> constructs enclosed within this one will still capture unless the <tt>&quot;/n&quot;</tt> modifier is in effect. 

 Like the ``(?adlupimnsx-imnsx)'' construct, <tt>&quot;aa&quot;</tt> and <tt>&quot;a&quot;</tt> override each other, as do <tt>&quot;xx&quot;</tt> and <tt>&quot;x&quot;</tt>. They are not additive. So, doing something like <tt>&quot;(?xx-x:foo)&quot;</tt> turns off all <tt>&quot;x&quot;</tt> behavior for matching <tt>&quot;foo&quot;</tt>. 

 Starting in Perl 5.14, a <tt>&quot;^&quot;</tt> (caret or circumflex accent) immediately after the <tt>&quot;?&quot;</tt> is a shorthand equivalent to <tt>&quot;d-imnsx&quot;</tt>. Any positive flags (except <tt>&quot;d&quot;</tt>) may follow the caret, so 

 <pre>
    (?^x:foo)
</pre> 

 is equivalent to 

 <pre>
    (?x-imns:foo)
</pre> 

 The caret tells Perl that this cluster doesn't inherit the flags of any surrounding pattern, but uses the system defaults (<tt>&quot;d-imnsx&quot;</tt>), modified by any flags specified. 

 The caret allows for simpler stringification of compiled regular expressions. These look like 

 <pre>
    (?^:pattern)
</pre> 

 with any non-default flags appearing between the caret and the colon. A test that looks at such stringification thus doesn't need to have the system default flags hard-coded in it, just the caret. If new flags are added to Perl, the meaning of the caret's expansion will change to include the default for those flags, so the test will still work, unchanged. 

 Specifying a negative flag after the caret is an error, as the flag is redundant. 

 Mnemonic for <tt>&quot;(?^...)&quot;</tt>: A fresh beginning since the usual use of a caret is to match at the beginning.
<dt>&quot;(?|<i>pattern</i>)&quot;
<dd> This is the ``branch reset'' pattern, which has the special property that the capture groups are numbered from the same starting point in each alternation branch. It is available starting from perl 5.10.0. 

 Capture groups are numbered from left to right, but inside this construct the numbering is restarted for each branch. 

 The numbering within each branch will be as normal, and any groups following this construct will be numbered as though the construct contained only one branch, that being the one with the most capture groups in it. 

 This construct is useful when you want to capture one of a number of alternative matches. 

 Consider the following pattern. The numbers underneath show in which group the captured content will be stored. 

 
#before-- -- -- -- -- -- -- -branch - reset-- -- -- -- -- -after
    / ( a )  (?| x ( y ) z | (p (q) r) | (t) u (v) ) ( z ) /x
# 1 2 2 3 2 3 4
 

 Be careful when using the branch reset pattern in combination with named captures. Named captures are implemented as being aliases to numbered groups holding the captures, and that interferes with the implementation of the branch reset pattern. If you are using named captures in a branch reset pattern, it's best to use the same names, in the same order, in each of the alternations: 

 <pre>
   /(?|  (?&lt;a&gt; x ) (?&lt;b&gt; y )
      |  (?&lt;a&gt; z ) (?&lt;b&gt; w )) /x
</pre> 

 Not doing so may lead to surprises: 

 
  "12" =~ /(?| (?&lt;a&gt; \d+ ) | (?&lt;b&gt; \D+))/x;
  say $ + {a};
#Prints '12' say $ + {b };
#* Also * prints '12'.
 

 The problem here is that both the group named <tt>&quot;a&quot;</tt> and the group named <tt>&quot;b&quot;</tt> are aliases for the group belonging to <tt>$1</tt>.
<dt>Lookaround Assertions
<dd> Lookaround assertions are zero-width patterns which match a specific pattern without including it in <tt>$&amp;</tt>. Positive assertions match when their subpattern matches, negative assertions match when their subpattern fails. Lookbehind matches text up to the current match position, lookahead matches text following the current match position.
<dl>
<dt>
<dd>
<dl>
<dt>&quot;(?=<i>pattern</i>)&quot;
<dd>
<dt>&quot;(*pla:<i>pattern</i>)&quot;
<dd>
<dt>&quot;(*positive_lookahead:<i>pattern</i>)&quot;
<dd> A zero-width positive lookahead assertion. For example, <tt>&quot;/\w+(?=\t)/&quot;</tt> matches a word followed by a tab, without including the tab in <tt>$&amp;</tt>. 

 The alphabetic forms are experimental; using them yields a warning in the <tt>&quot;experimental::alpha_assertions&quot;</tt> category.
<dt>&quot;(?!<i>pattern</i>)&quot;
<dd>
<dt>&quot;(*nla:<i>pattern</i>)&quot;
<dd>
<dt>&quot;(*negative_lookahead:<i>pattern</i>)&quot;
<dd> A zero-width negative lookahead assertion. For example <tt>&quot;/foo(?!bar)/&quot;</tt> matches any occurrence of ``foo'' that isn't followed by ``bar''. Note however that lookahead and lookbehind are <font SIZE="-1">NOT</font> the same thing. You cannot use this for lookbehind. 

 If you are looking for a ``bar'' that isn't preceded by a ``foo'', <tt>&quot;/(?!foo)bar/&quot;</tt> will not do what you want. That's because the <tt>&quot;(?!foo)&quot;</tt> is just saying that the next thing cannot be ``foo''--and it's not, it's a ``bar'', so ``foobar'' will match. Use lookbehind instead (see below). 

 The alphabetic forms are experimental; using them yields a warning in the <tt>&quot;experimental::alpha_assertions&quot;</tt> category.
<dt>&quot;(?&lt;=<i>pattern</i>)&quot;
<dd>
<dt>&quot;\K&quot;
<dd>
<dt>&quot;(*plb:<i>pattern</i>)&quot;
<dd>
<dt>&quot;(*positive_lookbehind:<i>pattern</i>)&quot;
<dd> A zero-width positive lookbehind assertion. For example, <tt>&quot;/(?&lt;=\t)\w+/&quot;</tt> matches a word that follows a tab, without including the tab in <tt>$&amp;</tt>. 

 Prior to Perl 5.30, it worked only for fixed-width lookbehind, but starting in that release, it can handle variable lengths from 1 to 255 characters as an experimental feature. The feature is enabled automatically if you use a variable length lookbehind assertion, but will raise a warning at pattern compilation time, unless turned off, in the <tt>&quot;experimental::vlb&quot;</tt> category. This is to warn you that the exact behavior is subject to change should feedback from actual use in the field indicate to do so; or even complete removal if the problems found are not practically surmountable. You can achieve close to pre-5.30 behavior by fatalizing warnings in this category. 

 There is a special form of this construct, called <tt>&quot;\K&quot;</tt> (available since Perl 5.10.0), which causes the regex engine to ``keep'' everything it had matched prior to the <tt>&quot;\K&quot;</tt> and not include it in <tt>$&amp;</tt>. This effectively provides non-experimental variable-length lookbehind of any length. 

 And, there is a technique that can be used to handle variable length lookbehinds on earlier releases, and longer than 255 characters. It is described in &lt;<a rel="nofollow" HREF="http://www.drregex.com/2019/02/variable-length-lookbehinds-actually.html">http://www.drregex.com/2019/02/variable-length-lookbehinds-actually.html</a>&gt;. 

 Note that under <tt>&quot;/i&quot;</tt>, a few single characters match two or three other characters. This makes them variable length, and the 255 length applies to the maximum number of characters in the match. For example <tt>&quot;qr/\N{LATIN SMALL LETTER SHARP S}/i&quot;</tt> matches the sequence <tt>&quot;ss&quot;</tt>. Your lookbehind assertion could contain 127 Sharp S characters under <tt>&quot;/i&quot;</tt>, but adding a 128th would generate a compilation error, as that could match 256 <tt>&quot;s&quot;</tt> characters in a row. 

 The use of <tt>&quot;\K&quot;</tt> inside of another lookaround assertion is allowed, but the behaviour is currently not well defined. 

 For various reasons <tt>&quot;\K&quot;</tt> may be significantly more efficient than the equivalent <tt>&quot;(?&lt;=...)&quot;</tt> construct, and it is especially useful in situations where you want to efficiently remove something following something else in a string. For instance 

 <pre>
  s/(foo)bar/$1/g;
</pre> 

 can be rewritten as the much more efficient 

 <pre>
  s/foo\Kbar//g;
</pre> 

 Use of the non-greedy modifier <tt>&quot;?&quot;</tt> may not give you the expected results if it is within a capturing group within the construct. 

 The alphabetic forms (not including <tt>&quot;\K&quot;</tt> are experimental; using them yields a warning in the <tt>&quot;experimental::alpha_assertions&quot;</tt> category.
<dt>&quot;(?&lt;!<i>pattern</i>)&quot;
<dd>
<dt>&quot;(*nlb:<i>pattern</i>)&quot;
<dd>
<dt>&quot;(*negative_lookbehind:<i>pattern</i>)&quot;
<dd> A zero-width negative lookbehind assertion. For example <tt>&quot;/(?&lt;!bar)foo/&quot;</tt> matches any occurrence of ``foo'' that does not follow ``bar''. 

 Prior to Perl 5.30, it worked only for fixed-width lookbehind, but starting in that release, it can handle variable lengths from 1 to 255 characters as an experimental feature. The feature is enabled automatically if you use a variable length lookbehind assertion, but will raise a warning at pattern compilation time, unless turned off, in the <tt>&quot;experimental::vlb&quot;</tt> category. This is to warn you that the exact behavior is subject to change should feedback from actual use in the field indicate to do so; or even complete removal if the problems found are not practically surmountable. You can achieve close to pre-5.30 behavior by fatalizing warnings in this category. 

 There is a technique that can be used to handle variable length lookbehinds on earlier releases, and longer than 255 characters. It is described in &lt;<a rel="nofollow" HREF="http://www.drregex.com/2019/02/variable-length-lookbehinds-actually.html">http://www.drregex.com/2019/02/variable-length-lookbehinds-actually.html</a>&gt;. 

 Note that under <tt>&quot;/i&quot;</tt>, a few single characters match two or three other characters. This makes them variable length, and the 255 length applies to the maximum number of characters in the match. For example <tt>&quot;qr/\N{LATIN SMALL LETTER SHARP S}/i&quot;</tt> matches the sequence <tt>&quot;ss&quot;</tt>. Your lookbehind assertion could contain 127 Sharp S characters under <tt>&quot;/i&quot;</tt>, but adding a 128th would generate a compilation error, as that could match 256 <tt>&quot;s&quot;</tt> characters in a row. 

 Use of the non-greedy modifier <tt>&quot;?&quot;</tt> may not give you the expected results if it is within a capturing group within the construct. 

 The alphabetic forms are experimental; using them yields a warning in the <tt>&quot;experimental::alpha_assertions&quot;</tt> category.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>&quot;(?&lt;<i>NAME</i>&gt;<i>pattern</i>)&quot;
<dd>
<dt>&quot;(?'<i>NAME</i>'<i>pattern</i>)&quot;
<dd> A named capture group. Identical in every respect to normal capturing parentheses <tt>&quot;()&quot;</tt> but for the additional fact that the group can be referred to by name in various regular expression constructs (like <tt>&quot;\g{</tt>NAME<tt>}&quot;</tt>) and can be accessed by name after a successful match via <tt>&quot;%+&quot;</tt> or <tt>&quot;%-&quot;</tt>. See perlvar for more details on the <tt>&quot;%+&quot;</tt> and <tt>&quot;%-&quot;</tt> hashes. 

 If multiple distinct capture groups have the same name, then <tt>$+{</tt>NAME<tt>}</tt> will refer to the leftmost defined group in the match. 

 The forms <tt>&quot;(?'</tt>NAME<tt>'</tt>pattern<tt>)&quot;</tt> and <tt>&quot;(?&lt;</tt>NAME<tt>&gt;</tt>pattern<tt>)&quot;</tt> are equivalent. 

 <font SIZE="-1"><b>NOTE:</b></font> While the notation of this construct is the same as the similar function in .NET regexes, the behavior is not. In Perl the groups are numbered sequentially regardless of being named or not. Thus in the pattern 

 <pre>
  /(x)(?&lt;foo&gt;y)(z)/
</pre> 

 <tt>$+{foo}</tt> will be the same as <tt>$2</tt>, and <tt>$3</tt> will contain 'z' instead of the opposite which is what a .NET regex hacker might expect. 

 Currently <i></i><font SIZE="-1"><i>NAME</i></font><i></i> is restricted to simple identifiers only. In other words, it must match <tt>&quot;/^[_A-Za-z][_A-Za-z0-9]*\z/&quot;</tt> or its Unicode extension (see utf8), though it isn't extended by the locale (see perllocale). 

 <font SIZE="-1"><b>NOTE:</b></font> In order to make things easier for programmers with experience with the Python or <font SIZE="-1">PCRE</font> regex engines, the pattern <tt>&quot;(?P&lt;</tt>NAME<tt>&gt;</tt>pattern<tt>)&quot;</tt> may be used instead of <tt>&quot;(?&lt;</tt>NAME<tt>&gt;</tt>pattern<tt>)&quot;</tt>; however this form does not support the use of single quotes as a delimiter for the name.
<dt>&quot;\k&lt;<i>NAME</i>&gt;&quot;
<dd>
<dt>&quot;\k'<i>NAME</i>'&quot;
<dd> Named backreference. Similar to numeric backreferences, except that the group is designated by name and not number. If multiple groups have the same name then it refers to the leftmost defined group in the current match. 

 It is an error to refer to a name not defined by a <tt>&quot;(?&lt;</tt>NAME<tt>&gt;)&quot;</tt> earlier in the pattern. 

 Both forms are equivalent. 

 <font SIZE="-1"><b>NOTE:</b></font> In order to make things easier for programmers with experience with the Python or <font SIZE="-1">PCRE</font> regex engines, the pattern <tt>&quot;(?P=</tt>NAME<tt>)&quot;</tt> may be used instead of <tt>&quot;\k&lt;</tt>NAME<tt>&gt;&quot;</tt>.
<dt>&quot;(?{ <i>code</i> })&quot;
<dd> <font SIZE="-1"><b>WARNING</b></font>: Using this feature safely requires that you understand its limitations. Code executed that has side effects may not perform identically from version to version due to the effect of future optimisations in the regex engine. For more information on this, see ``Embedded Code Execution Frequency''. 

 This zero-width assertion executes any embedded Perl code. It always succeeds, and its return value is set as <tt>$^R</tt>. 

 In literal patterns, the code is parsed at the same time as the surrounding code. While within the pattern, control is passed temporarily back to the perl parser, until the logically-balancing closing brace is encountered. This is similar to the way that an array index expression in a literal string is handled, for example 

 <pre>
    &quot;abc$array[ 1 + f('[') + g()]def&quot;
</pre> 

 In particular, braces do not need to be balanced: 

 
    s/abc(?{
    f('{'); })/def/
 

 Even in a pattern that is interpolated and compiled at run-time, literal code blocks will be compiled once, at perl compile time; the following prints ``<font SIZE="-1">ABCD'':</font> 

 
print "D";
    my $qr = qr/(?{ BEGIN { print "A" } })/;
    my $foo = "foo";
    /$foo$qr(?{ BEGIN { print "B" } })/;
    BEGIN
    {
        print "C"
    }
 

 In patterns where the text of the code is derived from run-time information rather than appearing literally in a source code /pattern/, the code is compiled at the same time that the pattern is compiled, and for reasons of security, <tt>&quot;use re 'eval'&quot;</tt> must be in scope. This is to stop user-supplied patterns containing code snippets from being executable. 

 In situations where you need to enable this with <tt>&quot;use re 'eval'&quot;</tt>, you should also have taint checking enabled. Better yet, use the carefully constrained evaluation within a Safe compartment. See perlsec for details about both these mechanisms. 

 From the viewpoint of parsing, lexical variable scope and closures, 

 <pre>
    /AAA(?{ BBB })CCC/
</pre> 

 behaves approximately like 

 
/ AAA / &amp;&amp;do {BBB} &amp;&amp; / CCC /
 

 Similarly, 

 <pre>
    qr/AAA(?{ BBB })CCC/
</pre> 

 behaves approximately like 

 
sub
{
    / AAA / &amp;&amp;do {BBB} &amp;&amp; / CCC /
}
 

 In particular: 

 
{
    my $i = 1; $r = qr/(?{ print $i })/
}
my $i = 2;
/ $r / ;
#prints "1"
 

 Inside a <tt>&quot;(?{...})&quot;</tt> block, <tt>$_</tt> refers to the string the regular expression is matching against. You can also use <tt>&quot;pos()&quot;</tt> to know what is the current position of matching within this string. 

 The code block introduces a new scope from the perspective of lexical variable declarations, but <b>not</b> from the perspective of <tt>&quot;local&quot;</tt> and similar localizing behaviours. So later code blocks within the same pattern will still see the values which were localized in earlier blocks. These accumulated localizations are undone either at the end of a successful match, or if the assertion is backtracked (compare ``Backtracking''). For example, 

 
$_ = 'a' x 8;
  m&lt;
     (?{ $cnt = 0 })               # Initialize $cnt.
     (
       a
       (?{
    local $cnt = $cnt + 1;
#Update $cnt,
#backtracking - safe.
       })
     )*
     aaaa
     (?{ $res = $cnt })            # On success copy to
#non - localized location.
   &gt;x;
 

 will initially increment <tt>$cnt</tt> up to 8; then during backtracking, its value will be unwound back to 4, which is the value assigned to <tt>$res</tt>. At the end of the regex execution, <tt>$cnt</tt> will be wound back to its initial value of 0. 

 This assertion may be used as the condition in a 

 <pre>
    (?(condition)yes-pattern|no-pattern)
</pre> 

 switch. If <i>not</i> used in this way, the result of evaluation of <i>code</i> is put into the special variable <tt>$^R</tt>. This happens immediately, so <tt>$^R</tt> can be used from other <tt>&quot;(?{ </tt>code<tt> })&quot;</tt> assertions inside the same regular expression. 

 The assignment to <tt>$^R</tt> above is properly localized, so the old value of <tt>$^R</tt> is restored if the assertion is backtracked; compare ``Backtracking''. 

 Note that the special variable <tt>$^N</tt> is particularly useful with code blocks to capture the results of submatches in variables without having to keep track of the number of nested parentheses. For example: 

 
$_ = "The brown fox jumps over the lazy dog";
  /the (\S+)(?{ $color = $^N }) (\S+)(?{ $animal = $^N })/i;
  print "color = $color, animal = $animal\n";

<dt>&quot;(??{ <i>code</i> })&quot;
<dd> <font SIZE="-1"><b>WARNING</b></font>: Using this feature safely requires that you understand its limitations. Code executed that has side effects may not perform identically from version to version due to the effect of future optimisations in the regex engine. For more information on this, see ``Embedded Code Execution Frequency''. 

 This is a ``postponed'' regular subexpression. It behaves in <i>exactly</i> the same way as a <tt>&quot;(?{ </tt>code<tt> })&quot;</tt> code block as described above, except that its return value, rather than being assigned to <tt>$^R</tt>, is treated as a pattern, compiled if it's a string (or used as-is if its a qr// object), then matched as if it were inserted instead of this construct. 

 During the matching of this sub-pattern, it has its own set of captures which are valid during the sub-match, but are discarded once control returns to the main pattern. For example, the following matches, with the inner pattern capturing ``B'' and matching ``<font SIZE="-1">BB'',</font> while the outer pattern captures ``A''; 

 
my $inner = '(.)\1';
    "ABBA" =~ /^(.)(??{ $inner })\1/;
    print $1;
#prints "A";
 

 Note that this means that there is no way for the inner pattern to refer to a capture group defined outside. (The code block itself can use <tt>$1</tt>, <i>etc</i>., to refer to the enclosing pattern's capture groups.) Thus, although 

 <pre>
    ('a' x 100)=~/(??{'(.)' x 100})/
</pre> 

 <i>will</i> match, it will <i>not</i> set <tt>$1</tt> on exit. 

 The following pattern matches a parenthesized group: 

 
 $re = qr{
            \(
            (?:
               (?&gt; [^()]+ )  # Non-parens without backtracking
             |
               (??{ $re })   # Group with matching parens
            )*
            \)
         }x;
 

 See also <tt>&quot;(?</tt>PARNO<tt>)&quot;</tt> for a different, more efficient way to accomplish the same task. 

 Executing a postponed regular expression too many times without consuming any input string will also result in a fatal error. The depth at which that happens is compiled into perl, so it can be changed with a custom build.
<dt>&quot;(?<i>PARNO</i>)&quot; &quot;(?-<i>PARNO</i>)&quot; &quot;(?+<i>PARNO</i>)&quot; &quot;(?R)&quot; &quot;(?0)&quot;
<dd> Recursive subpattern. Treat the contents of a given capture buffer in the current pattern as an independent subpattern and attempt to match it at the current position in the string. Information about capture state from the caller for things like backreferences is available to the subpattern, but capture buffers set by the subpattern are not visible to the caller. 

 Similar to <tt>&quot;(??{ </tt>code<tt> })&quot;</tt> except that it does not involve executing any code or potentially compiling a returned pattern string; instead it treats the part of the current pattern contained within a specified capture group as an independent pattern that must match at the current position. Also different is the treatment of capture buffers, unlike <tt>&quot;(??{ </tt>code<tt> })&quot;</tt> recursive patterns have access to their caller's match state, so one can use backreferences safely. 

 <i></i><font SIZE="-1"><i>PARNO</i></font><i></i> is a sequence of digits (not starting with 0) whose value reflects the paren-number of the capture group to recurse to. <tt>&quot;(?R)&quot;</tt> recurses to the beginning of the whole pattern. <tt>&quot;(?0)&quot;</tt> is an alternate syntax for <tt>&quot;(?R)&quot;</tt>. If <i></i><font SIZE="-1"><i>PARNO</i></font><i></i> is preceded by a plus or minus sign then it is assumed to be relative, with negative numbers indicating preceding capture groups and positive ones following. Thus <tt>&quot;(?-1)&quot;</tt> refers to the most recently declared group, and <tt>&quot;(?+1)&quot;</tt> indicates the next group to be declared. Note that the counting for relative recursion differs from that of relative backreferences, in that with recursion unclosed groups <b>are</b> included. 

 The following pattern matches a function <tt>&quot;foo()&quot;</tt> which may contain balanced parentheses as the argument. 

 
  $re = qr{ (                   # paren group 1 (full function)
              foo
              (                 # paren group 2 (parens)
                \(
                  (             # paren group 3 (contents of parens)
                  (?:
                   (?&gt; [^()]+ ) # Non-parens without backtracking
                  |
                   (?2)         # Recurse to start of paren group 2
                  )*
                  )
                \)
              )
            )
          }x;
 

 If the pattern was used as follows 

 <pre>
    'foo(bar(baz)+baz(bop))'=~/$re/
        and print &quot;\$1 = $1\n&quot;,
                  &quot;\$2 = $2\n&quot;,
                  &quot;\$3 = $3\n&quot;;
</pre> 

 the output produced should be the following: 

 <pre>
    $1 = foo(bar(baz)+baz(bop))
    $2 = (bar(baz)+baz(bop))
    $3 = bar(baz)+baz(bop)
</pre> 

 If there is no corresponding capture group defined, then it is a fatal error. Recursing deeply without consuming any input string will also result in a fatal error. The depth at which that happens is compiled into perl, so it can be changed with a custom build. 

 The following shows how using negative indexing can make it easier to embed recursive patterns inside of a <tt>&quot;qr//&quot;</tt> construct for later use: 

 
    my $parens = qr/(\((?:[^()]++|(?-1))*+\))/;
    if (/ foo $parens \s + \+ \s + bar $parens / x) {
#do something here...
    }
 

 <b>Note</b> that this pattern does not behave the same way as the equivalent <font SIZE="-1">PCRE</font> or Python construct of the same form. In Perl you can backtrack into a recursed group, in <font SIZE="-1">PCRE</font> and Python the recursed into group is treated as atomic. Also, modifiers are resolved at compile time, so constructs like <tt>&quot;(?i:(?1))&quot;</tt> or <tt>&quot;(?:(?i)(?1))&quot;</tt> do not affect how the sub-pattern will be processed.
<dt>&quot;(?&amp;<i>NAME</i>)&quot;
<dd> Recurse to a named subpattern. Identical to <tt>&quot;(?</tt>PARNO<tt>)&quot;</tt> except that the parenthesis to recurse to is determined by name. If multiple parentheses have the same name, then it recurses to the leftmost. 

 It is an error to refer to a name that is not declared somewhere in the pattern. 

 <font SIZE="-1"><b>NOTE:</b></font> In order to make things easier for programmers with experience with the Python or <font SIZE="-1">PCRE</font> regex engines the pattern <tt>&quot;(?P&gt;</tt>NAME<tt>)&quot;</tt> may be used instead of <tt>&quot;(?&amp;</tt>NAME<tt>)&quot;</tt>.
<dt>&quot;(?(<i>condition</i>)<i>yes-pattern</i>|<i>no-pattern</i>)&quot;
<dd>
<dt>&quot;(?(<i>condition</i>)<i>yes-pattern</i>)&quot;
<dd> Conditional expression. Matches <i>yes-pattern</i> if <i>condition</i> yields a true value, matches <i>no-pattern</i> otherwise. A missing pattern always matches. 

 <tt>&quot;(</tt>condition<tt>)&quot;</tt> should be one of:
<dl>
<dt>
<dd>
<dl>
<dt>an integer in parentheses
<dd> (which is valid if the corresponding pair of parentheses matched);
<dt>a lookahead/lookbehind/evaluate zero-width assertion;
<dd>
<dt>a name in angle brackets or single quotes
<dd> (which is valid if a group with the given name matched);
<dt>the special symbol &quot;(R)&quot;
<dd> (true when evaluated inside of recursion or eval). Additionally the <tt>&quot;R&quot;</tt> may be followed by a number, (which will be true when evaluated when recursing inside of the appropriate group), or by <tt>&quot;&amp;</tt>NAME<tt>&quot;</tt>, in which case it will be true only when evaluated during recursion in the named group.</dl>
</dl>

<dl>
<dt>
<dd> 

 Here's a summary of the possible predicates:
<dl>
<dt>&quot;(1)&quot; &quot;(2)&quot; ...
<dd> Checks if the numbered capturing group has matched something. Full syntax: <tt>&quot;(?(1)then|else)&quot;</tt>
<dt>&quot;(&lt;<i>NAME</i>&gt;)&quot; &quot;('<i>NAME</i>')&quot;
<dd> Checks if a group with the given name has matched something. Full syntax: <tt>&quot;(?(&lt;name&gt;)then|else)&quot;</tt>
<dt>&quot;(?=...)&quot; &quot;(?!...)&quot; &quot;(?&lt;=...)&quot; &quot;(?&lt;!...)&quot;
<dd> Checks whether the pattern matches (or does not match, for the <tt>&quot;!&quot;</tt> variants). Full syntax: <tt>&quot;(?(?=</tt>lookahead<tt>)</tt>then<tt>|</tt>else<tt>)&quot;</tt>
<dt>&quot;(?{ <i>CODE</i> })&quot;
<dd> Treats the return value of the code block as the condition. Full syntax: <tt>&quot;(?(?{ </tt>code<tt> })</tt>then<tt>|</tt>else<tt>)&quot;</tt>
<dt>&quot;(R)&quot;
<dd> Checks if the expression has been evaluated inside of recursion. Full syntax: <tt>&quot;(?(R)</tt>then<tt>|</tt>else<tt>)&quot;</tt>
<dt>&quot;(R1)&quot; &quot;(R2)&quot; ...
<dd> Checks if the expression has been evaluated while executing directly inside of the n-th capture group. This check is the regex equivalent of 

 
if ((caller(0))[3] eq 'subname') {
    ...
}
 

 In other words, it does not check the full recursion stack. 

 Full syntax: <tt>&quot;(?(R1)</tt>then<tt>|</tt>else<tt>)&quot;</tt>
<dt>&quot;(R&amp;<i>NAME</i>)&quot;
<dd> Similar to <tt>&quot;(R1)&quot;</tt>, this predicate checks to see if we're executing directly inside of the leftmost group with a given name (this is the same logic used by <tt>&quot;(?&amp;</tt>NAME<tt>)&quot;</tt> to disambiguate). It does not check the full stack, but only the name of the innermost active recursion. Full syntax: <tt>&quot;(?(R&amp;</tt>name<tt>)</tt>then<tt>|</tt>else<tt>)&quot;</tt>
<dt>&quot;(DEFINE)&quot;
<dd> In this case, the yes-pattern is never directly executed, and no no-pattern is allowed. Similar in spirit to <tt>&quot;(?{0})&quot;</tt> but more efficient. See below for details. Full syntax: <tt>&quot;(?(DEFINE)</tt>definitions<tt>...)&quot;</tt></dl>
</dl>

<dl>
<dt>
<dd> 

 For example: 

 
    m{ ( \( )?
       [^()]+
       (?(1) \) )
     }x
 

 matches a chunk of non-parentheses, possibly included in parentheses themselves. 

 A special form is the <tt>&quot;(DEFINE)&quot;</tt> predicate, which never executes its yes-pattern directly, and does not allow a no-pattern. This allows one to define subpatterns which will be executed only by the recursion mechanism. This way, you can define a set of regular expression rules that can be bundled into any pattern you choose. 

 It is recommended that for this usage you put the <font SIZE="-1">DEFINE</font> block at the end of the pattern, and that you name any subpatterns defined within it. 

 Also, it's worth noting that patterns defined this way probably will not be as efficient, as the optimizer is not very clever about handling them. 

 An example of how this might be used is as follows: 

 <pre>
  /(?&lt;NAME&gt;(?&amp;NAME_PAT))(?&lt;ADDR&gt;(?&amp;ADDRESS_PAT))
   (?(DEFINE)
     (?&lt;NAME_PAT&gt;....)
     (?&lt;ADDRESS_PAT&gt;....)
   )/x
</pre> 

 Note that capture groups matched inside of recursion are not accessible after the recursion returns, so the extra layer of capturing groups is necessary. Thus <tt>$+{NAME_PAT}</tt> would not be defined even though <tt>$+{NAME}</tt> would be. 

 Finally, keep in mind that subpatterns created inside a <font SIZE="-1">DEFINE</font> block count towards the absolute and relative number of captures, so this: 

 <pre>
    my @captures = &quot;a&quot; =~ /(.)                  # First capture
                           (?(DEFINE)
                               (?&lt;EXAMPLE&gt; 1 )  # Second capture
                           )/x;
    say scalar @captures;
</pre> 

 Will output 2, not 1. This is particularly important if you intend to compile the definitions with the <tt>&quot;qr//&quot;</tt> operator, and later interpolate them in another pattern.</dl>

<dt>&quot;(?&gt;<i>pattern</i>)&quot;
<dd>
<dt>&quot;(*atomic:<i>pattern</i>)&quot;
<dd> An ``independent'' subexpression, one which matches the substring that a standalone <i>pattern</i> would match if anchored at the given position, and it matches <i>nothing other than this substring</i>. This construct is useful for optimizations of what would otherwise be ``eternal'' matches, because it will not backtrack (see ``Backtracking''). It may also be useful in places where the ``grab all you can, and do not give anything back'' semantic is desirable. 

 For example: <tt>&quot;^(?&gt;a*)ab&quot;</tt> will never match, since <tt>&quot;(?&gt;a*)&quot;</tt> (anchored at the beginning of string, as above) will match <i>all</i> characters <tt>&quot;a&quot;</tt> at the beginning of string, leaving no <tt>&quot;a&quot;</tt> for <tt>&quot;ab&quot;</tt> to match. In contrast, <tt>&quot;a*ab&quot;</tt> will match the same as <tt>&quot;a+b&quot;</tt>, since the match of the subgroup <tt>&quot;a*&quot;</tt> is influenced by the following group <tt>&quot;ab&quot;</tt> (see ``Backtracking''). In particular, <tt>&quot;a*&quot;</tt> inside <tt>&quot;a*ab&quot;</tt> will match fewer characters than a standalone <tt>&quot;a*&quot;</tt>, since this makes the tail match. 

 <tt>&quot;(?&gt;</tt>pattern<tt>)&quot;</tt> does not disable backtracking altogether once it has matched. It is still possible to backtrack past the construct, but not into it. So <tt>&quot;((?&gt;a*)|(?&gt;b*))ar&quot;</tt> will still match ``bar''. 

 An effect similar to <tt>&quot;(?&gt;</tt>pattern<tt>)&quot;</tt> may be achieved by writing <tt>&quot;(?=(</tt>pattern<tt>))\g{-1}&quot;</tt>. This matches the same substring as a standalone <tt>&quot;a+&quot;</tt>, and the following <tt>&quot;\g{-1}&quot;</tt> eats the matched string; it therefore makes a zero-length assertion into an analogue of <tt>&quot;(?&gt;...)&quot;</tt>. (The difference between these two constructs is that the second one uses a capturing group, thus shifting ordinals of backreferences in the rest of a regular expression.) 

 Consider this pattern: 

 
m{ \(
    (
        [^()] + #x +
        |
            \([^()] * \)) +
       \)} x
 

 That will efficiently match a nonempty group with matching parentheses two levels deep or less. However, if there is no such group, it will take virtually forever on a long string. That's because there are so many different ways to split a long string into several substrings. This is what <tt>&quot;(.+)+&quot;</tt> is doing, and <tt>&quot;(.+)+&quot;</tt> is similar to a subpattern of the above pattern. Consider how the pattern above detects no-match on <tt>&quot;((()aaaaaaaaaaaaaaaaaa&quot;</tt> in several seconds, but that each extra letter doubles this time. This exponential performance will make it appear that your program has hung. However, a tiny change to this pattern 

 
    m{ \(
          (
            (?&gt; [^()]+ )        # change x+ above to (?&gt; x+ )
          |
            \( [^()]* \)
          )+
       \)
     }x
 

 which uses <tt>&quot;(?&gt;...)&quot;</tt> matches exactly when the one above does (verifying this yourself would be a productive exercise), but finishes in a fourth the time when used on a similar string with 1000000 <tt>&quot;a&quot;</tt>s. Be aware, however, that, when this construct is followed by a quantifier, it currently triggers a warning message under the <tt>&quot;use warnings&quot;</tt> pragma or <b>-w</b> switch saying it <tt>&quot;matches null string many times in regex&quot;</tt>. 

 On simple groups, such as the pattern <tt>&quot;(?&gt; [^()]+ )&quot;</tt>, a comparable effect may be achieved by negative lookahead, as in <tt>&quot;[^()]+ (?! [^()] )&quot;</tt>. This was only 4 times slower on a string with 1000000 <tt>&quot;a&quot;</tt>s. 

 The ``grab all you can, and do not give anything back'' semantic is desirable in many situations where on the first sight a simple <tt>&quot;()*&quot;</tt> looks like the correct solution. Suppose we parse text with comments being delimited by <tt>&quot;#&quot;</tt> followed by some optional (horizontal) whitespace. Contrary to its appearance, <tt>&quot;#[ \t]*&quot;</tt> <i>is not</i> the correct subexpression to match the comment delimiter, because it may ``give up'' some whitespace if the remainder of the pattern can be made to match that way. The correct answer is either one of these: 

 
    (?&gt;#[ \t]*)
#[ \t] *(? ![ \t])
 

 For example, to grab non-empty comments into <tt>$1</tt>, one should use either one of these: 

 
    / (?&gt; \# [ \t]* ) (        .+ ) /x;
    /     \#[ \t] * ([^ \t].*) / x;
 

 Which one you pick depends on which of these expressions better reflects the above specification of comments. 

 In some literature this construct is called ``atomic matching'' or ``possessive matching''. 

 Possessive quantifiers are equivalent to putting the item they are applied to inside of one of these constructs. The following equivalences apply: 

 
    Quantifier Form     Bracketing Form
    ---------------     ---------------
    PAT*+               (?&gt;PAT*)
    PAT++               (?&gt;PAT+)
    PAT?+               (?&gt;PAT?)
    PAT{min,max}+       (?&gt;PAT{min,max})
 

 Nested <tt>&quot;(?&gt;...)&quot;</tt> constructs are not no-ops, even if at first glance they might seem to be. This is because the nested <tt>&quot;(?&gt;...)&quot;</tt> can restrict internal backtracking that otherwise might occur. For example, 

 <pre>
 &quot;abc&quot; =~ /(?&gt;a[bc]*c)/
</pre> 

 matches, but 

 <pre>
 &quot;abc&quot; =~ /(?&gt;a(?&gt;[bc]*)c)/
</pre> 

 does not. 

 The alphabetic form (<tt>&quot;(*atomic:...)&quot;</tt>) is experimental; using it yields a warning in the <tt>&quot;experimental::alpha_assertions&quot;</tt> category.
<dt>&quot;(?[ ])&quot;
<dd> See ``Extended Bracketed Character Classes'' in perlrecharclass. 

 Note that this feature is currently experimental; using it yields a warning in the <tt>&quot;experimental::regex_sets&quot;</tt> category.</dl>

<h3>Backtracking</h3>

 <font SIZE="-1">NOTE:</font> This section presents an abstract approximation of regular expression behavior. For a more rigorous (and complicated) view of the rules involved in selecting a match among possible alternatives, see ``Combining <font SIZE="-1">RE</font> Pieces''. 

 A fundamental feature of regular expression matching involves the notion called <i>backtracking</i>, which is currently used (when needed) by all regular non-possessive expression quantifiers, namely <tt>&quot;*&quot;</tt>, <tt>&quot;*?&quot;</tt>, <tt>&quot;+&quot;</tt>, <tt>&quot;+?&quot;</tt>, <tt>&quot;{n,m}&quot;</tt>, and <tt>&quot;{n,m}?&quot;</tt>. Backtracking is often optimized internally, but the general principle outlined here is valid. 

 For a regular expression to match, the <i>entire</i> regular expression must match, not just part of it. So if the beginning of a pattern containing a quantifier succeeds in a way that causes later parts in the pattern to fail, the matching engine backs up and recalculates the beginning part---that's why it's called backtracking. 

 Here is an example of backtracking: Let's say you want to find the word following ``foo'' in the string ``Food is on the foo table.'': 

 
$_ = "Food is on the foo table.";
if (/\b(foo)\s + (\w +) / i) {
    print "$2 follows $1.\n";
}
 

 When the match runs, the first part of the regular expression (<tt>&quot;\b(foo)&quot;</tt>) finds a possible match right at the beginning of the string, and loads up <tt>$1</tt> with ``Foo''. However, as soon as the matching engine sees that there's no whitespace following the ``Foo'' that it had saved in <tt>$1</tt>, it realizes its mistake and starts over again one character after where it had the tentative match. This time it goes all the way until the next occurrence of ``foo''. The complete regular expression matches this time, and you get the expected output of ``table follows foo.'' 

 Sometimes minimal matching can help a lot. Imagine you'd like to match everything between ``foo'' and ``bar''. Initially, you write something like this: 

 
$_ = "The food is under the bar in the barn.";
if (/ foo(.*) bar /) {
    print "got &lt;$1&gt;\n";
}
 

 Which perhaps unexpectedly yields: 

 <pre>
  got &lt;d is under the bar in the &gt;
</pre> 

 That's because <tt>&quot;.*&quot;</tt> was greedy, so you get everything between the <i>first</i> ``foo'' and the <i>last</i> ``bar''. Here it's more effective to use minimal matching to make sure you get the text between a ``foo'' and the first ``bar'' thereafter. 

 <pre>
    if ( /foo(.*?)bar/ ) { print &quot;got &lt;$1&gt;\n&quot; }
  got &lt;d is under the &gt;
</pre> 

 Here's another example. Let's say you'd like to match a number at the end of a string, and you also want to keep the preceding part of the match. So you write this: 

 
$_ = "I have 2 numbers: 53147";
if (/ (.*)(\d *) /) {
#Wrong !print "Beginning is &lt;$1&gt;, number is &lt;$2&gt;.\n";
}
 

 That won't work at all, because <tt>&quot;.*&quot;</tt> was greedy and gobbled up the whole string. As <tt>&quot;\d*&quot;</tt> can match on an empty string the complete regular expression matched successfully. 

 <pre>
    Beginning is &lt;I have 2 numbers: 53147&gt;, number is &lt;&gt;.
</pre> 

 Here are some variants, most of which don't work: 

 
$_ = "I have 2 numbers: 53147";
    @pats = qw{
        (.*)(\d*)
        (.*)(\d+)
        (.*?)(\d*)
        (.*?)(\d+)
        (.*)(\d+)$
        (.*?)(\d+)$
        (.*)\b(\d+)$
        (.*\D)(\d+)$
    };
    for
        $pat(@pats)
        {
            printf "%-12s ", $pat;
            if (/ $pat /) {
                print "&lt;$1&gt; &lt;$2&gt;\n";
            } else {
                print "FAIL\n";
            }
        }
 

 That will print out: 

 <pre>
    (.*)(\d*)    &lt;I have 2 numbers: 53147&gt; &lt;&gt;
    (.*)(\d+)    &lt;I have 2 numbers: 5314&gt; &lt;7&gt;
    (.*?)(\d*)   &lt;&gt; &lt;&gt;
    (.*?)(\d+)   &lt;I have &gt; &lt;2&gt;
    (.*)(\d+)$   &lt;I have 2 numbers: 5314&gt; &lt;7&gt;
    (.*?)(\d+)$  &lt;I have 2 numbers: &gt; &lt;53147&gt;
    (.*)\b(\d+)$ &lt;I have 2 numbers: &gt; &lt;53147&gt;
    (.*\D)(\d+)$ &lt;I have 2 numbers: &gt; &lt;53147&gt;
</pre> 

 As you see, this can be a bit tricky. It's important to realize that a regular expression is merely a set of assertions that gives a definition of success. There may be 0, 1, or several different ways that the definition might succeed against a particular string. And if there are multiple ways it might succeed, you need to understand backtracking to know which variety of success you will achieve. 

 When using lookahead assertions and negations, this can all get even trickier. Imagine you'd like to find a sequence of non-digits not followed by ``123''. You might try to write that as 

 
$_ = "ABC123";
    if ( /^\D*(?!123)/ ) {
#Wrong !print "Yup, no 123 in $_\n";
    }
 

 But that isn't going to match; at least, not the way you're hoping. It claims that there is no 123 in the string. Here's a clearer picture of why that pattern matches, contrary to popular expectations: 

 
$x = 'ABC123';
$y = 'ABC445';
    print "1: got $1\n" if $x =~ /^(ABC)(?!123)/;
    print "2: got $1\n" if $y =~ /^(ABC)(?!123)/;
    print "3: got $1\n" if $x =~ /^(\D*)(?!123)/;
    print "4: got $1\n" if $y =~ /^(\D*)(?!123)/;
 

 This prints 

 <pre>
    2: got ABC
    3: got AB
    4: got ABC
</pre> 

 You might have expected test 3 to fail because it seems to a more general purpose version of test 1. The important difference between them is that test 3 contains a quantifier (<tt>&quot;\D*&quot;</tt>) and so can use backtracking, whereas test 1 will not. What's happening is that you've asked &quot;Is it true that at the start of <tt>$x</tt>, following 0 or more non-digits, you have something that's not 123?&quot; If the pattern matcher had let <tt>&quot;\D*&quot;</tt> expand to ``<font SIZE="-1">ABC'',</font> this would have caused the whole pattern to fail. 

 The search engine will initially match <tt>&quot;\D*&quot;</tt> with ``<font SIZE="-1">ABC''.</font> Then it will try to match <tt>&quot;(?!123)&quot;</tt> with ``123'', which fails. But because a quantifier (<tt>&quot;\D*&quot;</tt>) has been used in the regular expression, the search engine can backtrack and retry the match differently in the hope of matching the complete regular expression. 

 The pattern really, <i>really</i> wants to succeed, so it uses the standard pattern back-off-and-retry and lets <tt>&quot;\D*&quot;</tt> expand to just ``<font SIZE="-1">AB''</font> this time. Now there's indeed something following ``<font SIZE="-1">AB''</font> that is not ``123''. It's ``C123'', which suffices. 

 We can deal with this by using both an assertion and a negation. We'll say that the first part in <tt>$1</tt> must be followed both by a digit and by something that's not ``123''. Remember that the lookaheads are zero-width expressions---they only look, but don't consume any of the string in their match. So rewriting this way produces what you'd expect; that is, case 5 will fail, but case 6 succeeds: 

 
    print "5: got $1\n" if $x =~ /^(\D*)(?=\d)(?!123)/;
    print "6: got $1\n" if $y =~ /^(\D*)(?=\d)(?!123)/;
    6 : got ABC
 

 In other words, the two zero-width assertions next to each other work as though they're ANDed together, just as you'd use any built-in assertions: <tt>&quot;/^$/&quot;</tt> matches only if you're at the beginning of the line <font SIZE="-1">AND</font> the end of the line simultaneously. The deeper underlying truth is that juxtaposition in regular expressions always means <font SIZE="-1">AND,</font> except when you write an explicit <font SIZE="-1">OR</font> using the vertical bar. <tt>&quot;/ab/&quot;</tt> means match ``a'' <font SIZE="-1">AND</font> (then) match ``b'', although the attempted matches are made at different positions because ``a'' is not a zero-width assertion, but a one-width assertion. 

 <font SIZE="-1"><b>WARNING</b></font>: Particularly complicated regular expressions can take exponential time to solve because of the immense number of possible ways they can use backtracking to try for a match. For example, without internal optimizations done by the regular expression engine, this will take a painfully long time to run: 

 
'aaaaaaaaaaaa' = ~ / ((a{0, 5}){0, 5}) *[c] /
 

 And if you used <tt>&quot;*&quot;</tt>'s in the internal groups instead of limiting them to 0 through 5 matches, then it would take forever---or until you ran out of stack space. Moreover, these internal optimizations are not always applicable. For example, if you put <tt>&quot;{0,5}&quot;</tt> instead of <tt>&quot;*&quot;</tt> on the external group, no current optimization is applicable, and the match takes a long time to finish. 

 A powerful tool for optimizing such beasts is what is known as an ``independent group'', which does not backtrack (see &quot;<tt>&quot;(?&gt;pattern)&quot;</tt>&quot;). Note also that zero-length lookahead/lookbehind assertions will not backtrack to make the tail match, since they are in ``logical'' context: only whether they match is considered relevant. For an example where side-effects of lookahead <i>might</i> have influenced the following match, see &quot;<tt>&quot;(?&gt;pattern)&quot;</tt>&quot;.

<h3>Script Runs</h3>

 A script run is basically a sequence of characters, all from the same Unicode script (see ``Scripts'' in perlunicode), such as Latin or Greek. In most places a single word would never be written in multiple scripts, unless it is a spoofing attack. An infamous example, is 

 <pre>
 paypal.com
</pre> 

 Those letters could all be Latin (as in the example just above), or they could be all Cyrillic (except for the dot), or they could be a mixture of the two. In the case of an internet address the <tt>&quot;.com&quot;</tt> would be in Latin, And any Cyrillic ones would cause it to be a mixture, not a script run. Someone clicking on such a link would not be directed to the real Paypal website, but an attacker would craft a look-alike one to attempt to gather sensitive information from the person. 

 Starting in Perl 5.28, it is now easy to detect strings that aren't script runs. Simply enclose just about any pattern like either of these: 

 <pre>
 (*script_run:pattern)
 (*sr:pattern)
</pre> 

 What happens is that after <i>pattern</i> succeeds in matching, it is subjected to the additional criterion that every character in it must be from the same script (see exceptions below). If this isn't true, backtracking occurs until something all in the same script is found that matches, or all possibilities are exhausted. This can cause a lot of backtracking, but generally, only malicious input will result in this, though the slow down could cause a denial of service attack. If your needs permit, it is best to make the pattern atomic to cut down on the amount of backtracking. This is so likely to be what you want, that instead of writing this: 

 <pre>
 (*script_run:(?&gt;pattern))
</pre> 

 you can write either of these: 

 <pre>
 (*atomic_script_run:pattern)
 (*asr:pattern)
</pre> 

 (See &quot;<tt>&quot;(?&gt;</tt>pattern<tt>)&quot;</tt>&quot;.) 

 In Taiwan, Japan, and Korea, it is common for text to have a mixture of characters from their native scripts and base Chinese. Perl follows Unicode's <font SIZE="-1">UTS 39</font> (&lt;<a rel="nofollow" HREF="http://unicode.org/reports/tr39/">http://unicode.org/reports/tr39/</a>&gt;) Unicode Security Mechanisms in allowing such mixtures. For example, the Japanese scripts Katakana and Hiragana are commonly mixed together in practice, along with some Chinese characters, and hence are treated as being in a single script run by Perl. 

 The rules used for matching decimal digits are slightly stricter. Many scripts have their own sets of digits equivalent to the Western <tt>0</tt> through <tt>9</tt> ones. A few, such as Arabic, have more than one set. For a string to be considered a script run, all digits in it must come from the same set of ten, as determined by the first digit encountered. As an example, 

 <pre>
 qr/(*script_run: \d+ \b )/x
</pre> 

 guarantees that the digits matched will all be from the same set of 10. You won't get a look-alike digit from a different script that has a different value than what it appears to be. 

 Unicode has three pseudo scripts that are handled specially. 

 ``Unknown'' is applied to code points whose meaning has yet to be determined. Perl currently will match as a script run, any single character string consisting of one of these code points. But any string longer than one code point containing one of these will not be considered a script run. 

 ``Inherited'' is applied to characters that modify another, such as an accent of some type. These are considered to be in the script of the master character, and so never cause a script run to not match. 

 The other one is ``Common''. This consists of mostly punctuation, emoji, and characters used in mathematics and music, the <font SIZE="-1">ASCII</font> digits <tt>0</tt> through <tt>9</tt>, and full-width forms of these digits. These characters can appear intermixed in text in many of the world's scripts. These also don't cause a script run to not match. But like other scripts, all digits in a run must come from the same set of 10. 

 This construct is non-capturing. You can add parentheses to <i>pattern</i> to capture, if desired. You will have to do this if you plan to use ``(*ACCEPT) (*ACCEPT:arg)'' and not have it bypass the script run checking. 

 This feature is experimental, and the exact syntax and details of operation are subject to change; using it yields a warning in the <tt>&quot;experimental::script_run&quot;</tt> category. 

 The <tt>&quot;Script_Extensions&quot;</tt> property as modified by <font SIZE="-1">UTS 39</font> (&lt;<a rel="nofollow" HREF="http://unicode.org/reports/tr39/">http://unicode.org/reports/tr39/</a>&gt;) is used as the basis for this feature. 

 To summarize,
<dl>
<dt>&bull;
<dd> All length 0 or length 1 sequences are script runs.
<dt>&bull;
<dd> A longer sequence is a script run if and only if <b>all</b> of the following conditions are met: 

 

<dl>
<dt>
<dd>
<dl>
<dt>1.
<dd> No code point in the sequence has the <tt>&quot;Script_Extension&quot;</tt> property of <tt>&quot;Unknown&quot;</tt>. 

 This currently means that all code points in the sequence have been assigned by Unicode to be characters that aren't private use nor surrogate code points.
<dt>2.
<dd> All characters in the sequence come from the Common script and/or the Inherited script and/or a single other script. 

 The script of a character is determined by the <tt>&quot;Script_Extensions&quot;</tt> property as modified by <font SIZE="-1">UTS 39</font> (&lt;<a rel="nofollow" HREF="http://unicode.org/reports/tr39/">http://unicode.org/reports/tr39/</a>&gt;), as described above.
<dt>3.
<dd> All decimal digits in the sequence come from the same block of 10 consecutive digits.</dl>
</dl>

<dl>
<dt>
<dd></dl>
</dl>

<h3>Special Backtracking Control Verbs</h3>

 These special patterns are generally of the form <tt>&quot;(*</tt>VERB<tt>:</tt>arg<tt>)&quot;</tt>. Unless otherwise stated the <i>arg</i> argument is optional; in some cases, it is mandatory. 

 Any pattern containing a special backtracking verb that allows an argument has the special behaviour that when executed it sets the current package's <tt>$REGERROR</tt> and <tt>$REGMARK</tt> variables. When doing so the following rules apply: 

 On failure, the <tt>$REGERROR</tt> variable will be set to the <i>arg</i> value of the verb pattern, if the verb was involved in the failure of the match. If the <i>arg</i> part of the pattern was omitted, then <tt>$REGERROR</tt> will be set to the name of the last <tt>&quot;(*MARK:</tt>NAME<tt>)&quot;</tt> pattern executed, or to <font SIZE="-1">TRUE</font> if there was none. Also, the <tt>$REGMARK</tt> variable will be set to <font SIZE="-1">FALSE.</font> 

 On a successful match, the <tt>$REGERROR</tt> variable will be set to <font SIZE="-1">FALSE,</font> and the <tt>$REGMARK</tt> variable will be set to the name of the last <tt>&quot;(*MARK:</tt>NAME<tt>)&quot;</tt> pattern executed. See the explanation for the <tt>&quot;(*MARK:</tt>NAME<tt>)&quot;</tt> verb below for more details. 

 <font SIZE="-1"><b>NOTE:</b></font> <tt>$REGERROR</tt> and <tt>$REGMARK</tt> are not magic variables like <tt>$1</tt> and most other regex-related variables. They are not local to a scope, nor readonly, but instead are volatile package variables similar to <tt>$AUTOLOAD</tt>. They are set in the package containing the code that <i>executed</i> the regex (rather than the one that compiled it, where those differ). If necessary, you can use <tt>&quot;local&quot;</tt> to localize changes to these variables to a specific scope before executing a regex. 

 If a pattern does not contain a special backtracking verb that allows an argument, then <tt>$REGERROR</tt> and <tt>$REGMARK</tt> are not touched at all.
<dl>
<dt>Verbs
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;(*PRUNE)&quot; &quot;(*PRUNE:<i>NAME</i>)&quot;
<dd> This zero-width pattern prunes the backtracking tree at the current point when backtracked into on failure. Consider the pattern <tt>&quot;/</tt>A<tt> (*PRUNE) </tt>B<tt>/&quot;</tt>, where <i>A</i> and <i>B</i> are complex patterns. Until the <tt>&quot;(*PRUNE)&quot;</tt> verb is reached, <i>A</i> may backtrack as necessary to match. Once it is reached, matching continues in <i>B</i>, which may also backtrack as necessary; however, should B not match, then no further backtracking will take place, and the pattern will fail outright at the current starting position. 

 The following example counts all the possible matching strings in a pattern (without actually matching any of them). 

 
'aaab' = ~ / a + b ? (? {print "$&amp;\n"; $count++ })(*FAIL) / ;
print "Count=$count\n";
 

 which produces: 

 <pre>
    aaab
    aaa
    aa
    a
    aab
    aa
    a
    ab
    a
    Count=9
</pre> 

 If we add a <tt>&quot;(*PRUNE)&quot;</tt> before the count like the following 

 
'aaab' = ~ / a + b ? (*PRUNE)(? {print "$&amp;\n"; $count++ })(*FAIL) / ;
print "Count=$count\n";
 

 we prevent backtracking and find the count of the longest matching string at each matching starting point like so: 

 <pre>
    aaab
    aab
    ab
    Count=3
</pre> 

 Any number of <tt>&quot;(*PRUNE)&quot;</tt> assertions may be used in a pattern. 

 See also <tt>&quot;(?&gt;</tt>pattern<tt>)&quot;</tt> and possessive quantifiers for other ways to control backtracking. In some cases, the use of <tt>&quot;(*PRUNE)&quot;</tt> can be replaced with a <tt>&quot;(?&gt;pattern)&quot;</tt> with no functional difference; however, <tt>&quot;(*PRUNE)&quot;</tt> can be used to handle cases that cannot be expressed using a <tt>&quot;(?&gt;pattern)&quot;</tt> alone.
<dt>&quot;(*SKIP)&quot; &quot;(*SKIP:<i>NAME</i>)&quot;
<dd> This zero-width pattern is similar to <tt>&quot;(*PRUNE)&quot;</tt>, except that on failure it also signifies that whatever text that was matched leading up to the <tt>&quot;(*SKIP)&quot;</tt> pattern being executed cannot be part of <i>any</i> match of this pattern. This effectively means that the regex engine ``skips'' forward to this position on failure and tries to match again, (assuming that there is sufficient room to match). 

 The name of the <tt>&quot;(*SKIP:</tt>NAME<tt>)&quot;</tt> pattern has special significance. If a <tt>&quot;(*MARK:</tt>NAME<tt>)&quot;</tt> was encountered while matching, then it is that position which is used as the ``skip point''. If no <tt>&quot;(*MARK)&quot;</tt> of that name was encountered, then the <tt>&quot;(*SKIP)&quot;</tt> operator has no effect. When used without a name the ``skip point'' is where the match point was when executing the <tt>&quot;(*SKIP)&quot;</tt> pattern. 

 Compare the following to the examples in <tt>&quot;(*PRUNE)&quot;</tt>; note the string is twice as long: 

 
'aaabaaab' = ~ / a + b ? (*SKIP)(? {print "$&amp;\n"; $count++ })(*FAIL) / ;
print "Count=$count\n";
 

 outputs 

 <pre>
    aaab
    aaab
    Count=2
</pre> 

 Once the 'aaab' at the start of the string has matched, and the <tt>&quot;(*SKIP)&quot;</tt> executed, the next starting point will be where the cursor was when the <tt>&quot;(*SKIP)&quot;</tt> was executed.
<dt>&quot;(*MARK:<i>NAME</i>)&quot; &quot;(*:<i>NAME</i>)&quot;
<dd> This zero-width pattern can be used to mark the point reached in a string when a certain part of the pattern has been successfully matched. This mark may be given a name. A later <tt>&quot;(*SKIP)&quot;</tt> pattern will then skip forward to that point if backtracked into on failure. Any number of <tt>&quot;(*MARK)&quot;</tt> patterns are allowed, and the <i></i><font SIZE="-1"><i>NAME</i></font><i></i> portion may be duplicated. 

 In addition to interacting with the <tt>&quot;(*SKIP)&quot;</tt> pattern, <tt>&quot;(*MARK:</tt>NAME<tt>)&quot;</tt> can be used to ``label'' a pattern branch, so that after matching, the program can determine which branches of the pattern were involved in the match. 

 When a match is successful, the <tt>$REGMARK</tt> variable will be set to the name of the most recently executed <tt>&quot;(*MARK:</tt>NAME<tt>)&quot;</tt> that was involved in the match. 

 This can be used to determine which branch of a pattern was matched without using a separate capture group for each branch, which in turn can result in a performance improvement, as perl cannot optimize <tt>&quot;/(?:(x)|(y)|(z))/&quot;</tt> as efficiently as something like <tt>&quot;/(?:x(*MARK:x)|y(*MARK:y)|z(*MARK:z))/&quot;</tt>. 

 When a match has failed, and unless another verb has been involved in failing the match and has provided its own name to use, the <tt>$REGERROR</tt> variable will be set to the name of the most recently executed <tt>&quot;(*MARK:</tt>NAME<tt>)&quot;</tt>. 

 See ``(*SKIP)'' for more details. 

 As a shortcut <tt>&quot;(*MARK:</tt>NAME<tt>)&quot;</tt> can be written <tt>&quot;(*:</tt>NAME<tt>)&quot;</tt>.
<dt>&quot;(*THEN)&quot; &quot;(*THEN:<i>NAME</i>)&quot;
<dd> This is similar to the ``cut group'' operator <tt>&quot;::&quot;</tt> from Perl 6. Like <tt>&quot;(*PRUNE)&quot;</tt>, this verb always matches, and when backtracked into on failure, it causes the regex engine to try the next alternation in the innermost enclosing group (capturing or otherwise) that has alternations. The two branches of a <tt>&quot;(?(</tt>condition<tt>)</tt>yes-pattern<tt>|</tt>no-pattern<tt>)&quot;</tt> do not count as an alternation, as far as <tt>&quot;(*THEN)&quot;</tt> is concerned. 

 Its name comes from the observation that this operation combined with the alternation operator (<tt>&quot;|&quot;</tt>) can be used to create what is essentially a pattern-based if/then/else block: 

 <pre>
  ( COND (*THEN) FOO | COND2 (*THEN) BAR | COND3 (*THEN) BAZ )
</pre> 

 Note that if this operator is used and <font SIZE="-1">NOT</font> inside of an alternation then it acts exactly like the <tt>&quot;(*PRUNE)&quot;</tt> operator. 

 <pre>
  / A (*PRUNE) B /
</pre> 

 is the same as 

 <pre>
  / A (*THEN) B /
</pre> 

 but 

 <pre>
  / ( A (*THEN) B | C ) /
</pre> 

 is not the same as 

 <pre>
  / ( A (*PRUNE) B | C ) /
</pre> 

 as after matching the <i>A</i> but failing on the <i>B</i> the <tt>&quot;(*THEN)&quot;</tt> verb will backtrack and try <i>C</i>; but the <tt>&quot;(*PRUNE)&quot;</tt> verb will simply fail.
<dt>&quot;(*COMMIT)&quot; &quot;(*COMMIT:<i>arg</i>)&quot;
<dd> This is the Perl 6 ``commit pattern'' <tt>&quot;&lt;commit&gt;&quot;</tt> or <tt>&quot;:::&quot;</tt>. It's a zero-width pattern similar to <tt>&quot;(*SKIP)&quot;</tt>, except that when backtracked into on failure it causes the match to fail outright. No further attempts to find a valid match by advancing the start pointer will occur again. For example, 

 
'aaabaaab' = ~ / a + b ? (*COMMIT)(? {print "$&amp;\n"; $count++ })(*FAIL) / ;
print "Count=$count\n";
 

 outputs 

 <pre>
    aaab
    Count=1
</pre> 

 In other words, once the <tt>&quot;(*COMMIT)&quot;</tt> has been entered, and if the pattern does not match, the regex engine will not try any further matching on the rest of the string.
<dt>&quot;(*FAIL)&quot; &quot;(*F)&quot; &quot;(*FAIL:<i>arg</i>)&quot;
<dd> This pattern matches nothing and always fails. It can be used to force the engine to backtrack. It is equivalent to <tt>&quot;(?!)&quot;</tt>, but easier to read. In fact, <tt>&quot;(?!)&quot;</tt> gets optimised into <tt>&quot;(*FAIL)&quot;</tt> internally. You can provide an argument so that if the match fails because of this <tt>&quot;FAIL&quot;</tt> directive the argument can be obtained from <tt>$REGERROR</tt>. 

 It is probably useful only when combined with <tt>&quot;(?{})&quot;</tt> or <tt>&quot;(??{})&quot;</tt>.
<dt>&quot;(*ACCEPT)&quot; &quot;(*ACCEPT:<i>arg</i>)&quot;
<dd> This pattern matches nothing and causes the end of successful matching at the point at which the <tt>&quot;(*ACCEPT)&quot;</tt> pattern was encountered, regardless of whether there is actually more to match in the string. When inside of a nested pattern, such as recursion, or in a subpattern dynamically generated via <tt>&quot;(??{})&quot;</tt>, only the innermost pattern is ended immediately. 

 If the <tt>&quot;(*ACCEPT)&quot;</tt> is inside of capturing groups then the groups are marked as ended at the point at which the <tt>&quot;(*ACCEPT)&quot;</tt> was encountered. For instance: 

 <pre>
  'AB' =~ /(A (A|B(*ACCEPT)|C) D)(E)/x;
</pre> 

 will match, and <tt>$1</tt> will be <tt>&quot;AB&quot;</tt> and <tt>$2</tt> will be <tt>&quot;B&quot;</tt>, <tt>$3</tt> will not be set. If another branch in the inner parentheses was matched, such as in the string '<font SIZE="-1">ACDE</font>', then the <tt>&quot;D&quot;</tt> and <tt>&quot;E&quot;</tt> would have to be matched as well. 

 You can provide an argument, which will be available in the var <tt>$REGMARK</tt> after the match completes.</dl>
</dl>

<dl>
<dt>
<dd></dl>
</dl>

<h3>Warning on \1 Instead of $1</h3>

 Some people get too used to writing things like: 

 <pre>
    $pattern =~ s/(\W)/\\\1/g;
</pre> 

 This is grandfathered (for \1 to \9) for the <font SIZE="-1">RHS</font> of a substitute to avoid shocking the <b>sed</b> addicts, but it's a dirty habit to get into. That's because in PerlThink, the righthand side of an <tt>&quot;s///&quot;</tt> is a double-quoted string. <tt>&quot;\1&quot;</tt> in the usual double-quoted string means a control-A. The customary Unix meaning of <tt>&quot;\1&quot;</tt> is kludged in for <tt>&quot;s///&quot;</tt>. However, if you get into the habit of doing that, you get yourself into trouble if you then add an <tt>&quot;/e&quot;</tt> modifier. 

 <pre>
    s/(\d+)/ \1 + 1 /eg;            # causes warning under -w
</pre> 

 Or if you try to do 

 <pre>
    s/(\d+)/\1000/;
</pre> 

 You can't disambiguate that by saying <tt>&quot;\{1}000&quot;</tt>, whereas you can fix it with <tt>&quot;${1}000&quot;</tt>. The operation of interpolation should not be confused with the operation of matching a backreference. Certainly they mean two different things on the <i>left</i> side of the <tt>&quot;s///&quot;</tt>.

<h3>Repeated Patterns Matching a Zero-length Substring</h3>

 <font SIZE="-1"><b>WARNING</b></font>: Difficult material (and prose) ahead. This section needs a rewrite. 

 Regular expressions provide a terse and powerful programming language. As with most other power tools, power comes together with the ability to wreak havoc. 

 A common abuse of this power stems from the ability to make infinite loops using regular expressions, with something as innocuous as: 

 <pre>
    'foo' =~ m{ ( o? )* }x;
</pre> 

 The <tt>&quot;o?&quot;</tt> matches at the beginning of &quot;<tt>&quot;foo&quot;</tt>&quot;, and since the position in the string is not moved by the match, <tt>&quot;o?&quot;</tt> would match again and again because of the <tt>&quot;*&quot;</tt> quantifier. Another common way to create a similar cycle is with the looping modifier <tt>&quot;/g&quot;</tt>: 

 <pre>
    @matches = ( 'foo' =~ m{ o? }xg );
</pre> 

 or 

 
print "match: &lt;$&amp;&gt;\n" while 'foo' = ~m{o ? } xg;
 

 or the loop implied by <tt>&quot;split()&quot;</tt>. 

 However, long experience has shown that many programming tasks may be significantly simplified by using repeated subexpressions that may match zero-length substrings. Here's a simple example being: 

 <pre>
    @chars = split //, $string;           # // is not magic in split
    ($whitewashed = $string) =~ s/()/ /g; # parens avoid magic s// /
</pre> 

 Thus Perl allows such constructs, by <i>forcefully breaking the infinite loop</i>. The rules for this are different for lower-level loops given by the greedy quantifiers <tt>&quot;*+{}&quot;</tt>, and for higher-level ones like the <tt>&quot;/g&quot;</tt> modifier or <tt>&quot;split()&quot;</tt> operator. 

 The lower-level loops are <i>interrupted</i> (that is, the loop is broken) when Perl detects that a repeated expression matched a zero-length substring. Thus 

 <pre>
   m{ (?: NON_ZERO_LENGTH | ZERO_LENGTH )* }x;
</pre> 

 is made equivalent to 

 <pre>
   m{ (?: NON_ZERO_LENGTH )* (?: ZERO_LENGTH )? }x;
</pre> 

 For example, this program 

 
#!perl - l
   "aaaaab" =~ /
     (?:
        a                 # non-zero
        |                 # or
       (?{print "hello"}) # print hello whenever this
#branch is tried
       (?=(b))            # zero-width assertion
     )*  # any number of times
    /x;
   print $ &amp;;
   print $1;
 

 prints 

 <pre>
   hello
   aaaaa
   b
</pre> 

 Notice that ``hello'' is only printed once, as when Perl sees that the sixth iteration of the outermost <tt>&quot;(?:)*&quot;</tt> matches a zero-length string, it stops the <tt>&quot;*&quot;</tt>. 

 The higher-level loops preserve an additional state between iterations: whether the last match was zero-length. To break the loop, the following match after a zero-length match is prohibited to have a length of zero. This prohibition interacts with backtracking (see ``Backtracking''), and so the <i>second best</i> match is chosen if the <i>best</i> match is of zero length. 

 For example: 

 <pre>
    $_ = 'bar';
    s/\w??/&lt;$&amp;&gt;/g;
</pre> 

 results in <tt>&quot;&lt;&gt;&lt;b&gt;&lt;&gt;&lt;a&gt;&lt;&gt;&lt;r&gt;&lt;&gt;&quot;</tt>. At each position of the string the best match given by non-greedy <tt>&quot;??&quot;</tt> is the zero-length match, and the <i>second best</i> match is what is matched by <tt>&quot;\w&quot;</tt>. Thus zero-length matches alternate with one-character-long matches. 

 Similarly, for repeated <tt>&quot;m/()/g&quot;</tt> the second-best match is the match at the position one notch further in the string. 

 The additional state of being <i>matched with zero-length</i> is associated with the matched string, and is reset by each assignment to <tt>&quot;pos()&quot;</tt>. Zero-length matches at the end of the previous match are ignored during <tt>&quot;split&quot;</tt>.

<h3>Combining <font SIZE="-1">RE</font> Pieces</h3>

 Each of the elementary pieces of regular expressions which were described before (such as <tt>&quot;ab&quot;</tt> or <tt>&quot;\Z&quot;</tt>) could match at most one substring at the given position of the input string. However, in a typical regular expression these elementary pieces are combined into more complicated patterns using combining operators <tt>&quot;ST&quot;</tt>, <tt>&quot;S|T&quot;</tt>, <tt>&quot;S*&quot;</tt> <i>etc</i>. (in these examples <tt>&quot;S&quot;</tt> and <tt>&quot;T&quot;</tt> are regular subexpressions). 

 Such combinations can include alternatives, leading to a problem of choice: if we match a regular expression <tt>&quot;a|ab&quot;</tt> against <tt>&quot;abc&quot;</tt>, will it match substring <tt>&quot;a&quot;</tt> or <tt>&quot;ab&quot;</tt>? One way to describe which substring is actually matched is the concept of backtracking (see ``Backtracking''). However, this description is too low-level and makes you think in terms of a particular implementation. 

 Another description starts with notions of ``better''/``worse''. All the substrings which may be matched by the given regular expression can be sorted from the ``best'' match to the ``worst'' match, and it is the ``best'' match which is chosen. This substitutes the question of ``what is chosen?'' by the question of ``which matches are better, and which are worse?''. 

 Again, for elementary pieces there is no such question, since at most one match at a given position is possible. This section describes the notion of better/worse for combining operators. In the description below <tt>&quot;S&quot;</tt> and <tt>&quot;T&quot;</tt> are regular subexpressions.
<dl>
<dt>&quot;ST&quot;
<dd> Consider two possible matches, <tt>&quot;AB&quot;</tt> and <tt>&quot;A'B'&quot;</tt>, <tt>&quot;A&quot;</tt> and <tt>&quot;A'&quot;</tt> are substrings which can be matched by <tt>&quot;S&quot;</tt>, <tt>&quot;B&quot;</tt> and <tt>&quot;B'&quot;</tt> are substrings which can be matched by <tt>&quot;T&quot;</tt>. 

 If <tt>&quot;A&quot;</tt> is a better match for <tt>&quot;S&quot;</tt> than <tt>&quot;A'&quot;</tt>, <tt>&quot;AB&quot;</tt> is a better match than <tt>&quot;A'B'&quot;</tt>. 

 If <tt>&quot;A&quot;</tt> and <tt>&quot;A'&quot;</tt> coincide: <tt>&quot;AB&quot;</tt> is a better match than <tt>&quot;AB'&quot;</tt> if <tt>&quot;B&quot;</tt> is a better match for <tt>&quot;T&quot;</tt> than <tt>&quot;B'&quot;</tt>.
<dt>&quot;S|T&quot;
<dd> When <tt>&quot;S&quot;</tt> can match, it is a better match than when only <tt>&quot;T&quot;</tt> can match. 

 Ordering of two matches for <tt>&quot;S&quot;</tt> is the same as for <tt>&quot;S&quot;</tt>. Similar for two matches for <tt>&quot;T&quot;</tt>.
<dt>&quot;S{REPEAT_COUNT}&quot;
<dd> Matches as <tt>&quot;SSS...S&quot;</tt> (repeated as many times as necessary).
<dt>&quot;S{min,max}&quot;
<dd> Matches as <tt>&quot;S{max}|S{max-1}|...|S{min+1}|S{min}&quot;</tt>.
<dt>&quot;S{min,max}?&quot;
<dd> Matches as <tt>&quot;S{min}|S{min+1}|...|S{max-1}|S{max}&quot;</tt>.
<dt>&quot;S?&quot;, &quot;S*&quot;, &quot;S+&quot;
<dd> Same as <tt>&quot;S{0,1}&quot;</tt>, <tt>&quot;S{0,BIG_NUMBER}&quot;</tt>, <tt>&quot;S{1,BIG_NUMBER}&quot;</tt> respectively.
<dt>&quot;S??&quot;, &quot;S*?&quot;, &quot;S+?&quot;
<dd> Same as <tt>&quot;S{0,1}?&quot;</tt>, <tt>&quot;S{0,BIG_NUMBER}?&quot;</tt>, <tt>&quot;S{1,BIG_NUMBER}?&quot;</tt> respectively.
<dt>&quot;(?&gt;S)&quot;
<dd> Matches the best match for <tt>&quot;S&quot;</tt> and only that.
<dt>&quot;(?=S)&quot;, &quot;(?&lt;=S)&quot;
<dd> Only the best match for <tt>&quot;S&quot;</tt> is considered. (This is important only if <tt>&quot;S&quot;</tt> has capturing parentheses, and backreferences are used somewhere else in the whole regular expression.)
<dt>&quot;(?!S)&quot;, &quot;(?&lt;!S)&quot;
<dd> For this grouping operator there is no need to describe the ordering, since only whether or not <tt>&quot;S&quot;</tt> can match is important.
<dt>&quot;(??{ <i>EXPR</i> })&quot;, &quot;(?<i>PARNO</i>)&quot;
<dd> The ordering is the same as for the regular expression which is the result of <i></i><font SIZE="-1"><i>EXPR</i></font><i></i>, or the pattern contained by capture group <i></i><font SIZE="-1"><i>PARNO</i></font><i></i>.
<dt>&quot;(?(<i>condition</i>)<i>yes-pattern</i>|<i>no-pattern</i>)&quot;
<dd> Recall that which of <i>yes-pattern</i> or <i>no-pattern</i> actually matches is already determined. The ordering of the matches is the same as for the chosen subexpression.</dl>
 

 The above recipes describe the ordering of matches <i>at a given position</i>. One more rule is needed to understand how a match is determined for the whole regular expression: a match at an earlier position is always better than a match at a later position.

<h3>Creating Custom <font SIZE="-1">RE</font> Engines</h3>

 As of Perl 5.10.0, one can create custom regular expression engines. This is not for the faint of heart, as they have to plug in at the C level. See perlreapi for more details. 

 As an alternative, overloaded constants (see overload) provide a simple way to extend the functionality of the <font SIZE="-1">RE</font> engine, by substituting one pattern for another. 

 Suppose that we want to enable a new <font SIZE="-1">RE</font> escape-sequence <tt>&quot;\Y|&quot;</tt> which matches at a boundary between whitespace characters and non-whitespace characters. Note that <tt>&quot;(?=\S)(?&lt;!\S)|(?!\S)(?&lt;=\S)&quot;</tt> matches exactly at these positions, so we want to have each <tt>&quot;\Y|&quot;</tt> in the place of the more complicated version. We can create a module <tt>&quot;customre&quot;</tt> to do this: 

 
package customre;
use overload;
sub import
{
    shift;
    die "No argument to customre::import allowed" if @_;
    overload::constant 'qr' = &gt; \&amp; convert;
}
    sub invalid { die "/$_[0]/: invalid escape '\\$_[1]'"}
#We must also take care of not escaping the legitimate \\Y |
#sequence, hence the presence of '\\' in the conversion rules.
    my %rules = ( '\\' =&gt; '\\\\',
                  'Y|' =&gt; qr/(?=\S)(?&lt;!\S)|(?!\S)(?&lt;=\S)/ );
    sub convert
    {
        my $re = shift;
        $re = ~s{
                \\ ( \\ | Y.)} {$rules{$1} or invalid($re, $1)} sgex;
        return $re;
    }
 

 Now <tt>&quot;use customre&quot;</tt> enables the new escape in constant regular expressions, <i>i.e.</i>, those without any runtime variable interpolations. As documented in overload, this conversion will work only over literal parts of regular expressions. For <tt>&quot;\Y|$re\Y|&quot;</tt> the variable part of this regular expression needs to be converted explicitly (but only if the special meaning of <tt>&quot;\Y|&quot;</tt> should be enabled inside <tt>$re</tt>): 

 <pre><code>
use customre;
$re = &lt;&gt;;
chomp $re;
$re = customre::convert $re;
/\Y | $re\Y | / ;
</code></pre>

<h3>Embedded Code Execution Frequency</h3>

 The exact rules for how often <tt>&quot;(??{})&quot;</tt> and <tt>&quot;(?{})&quot;</tt> are executed in a pattern are unspecified. In the case of a successful match you can assume that they <font SIZE="-1">DWIM</font> and will be executed in left to right order the appropriate number of times in the accepting path of the pattern as would any other meta-pattern. How non-accepting pathways and match failures affect the number of times a pattern is executed is specifically unspecified and may vary depending on what optimizations can be applied to the pattern and is likely to change from version to version. 

 For instance in 

 <pre>
  &quot;aaabcdeeeee&quot;=~/a(?{print &quot;a&quot;})b(?{print &quot;b&quot;})cde/;
</pre> 

 the exact number of times ``a'' or ``b'' are printed out is unspecified for failure, but you may assume they will be printed at least once during a successful match, additionally you may assume that if ``b'' is printed, it will be preceded by at least one ``a''. 

 In the case of branching constructs like the following: 

 <pre>
  /a(b|(?{ print &quot;a&quot; }))c(?{ print &quot;c&quot; })/;
</pre> 

 you can assume that the input ``ac'' will output ``ac'', and that ``abc'' will output only ``c''. 

 When embedded code is quantified, successful matches will call the code once for each matched iteration of the quantifier. For example: 

 <pre>
  &quot;good&quot; =~ /g(?:o(?{print &quot;o&quot;}))*d/;
</pre> 

 will output ``o'' twice.

<h3>PCRE/Python Support</h3>

 As of Perl 5.10.0, Perl supports several Python/PCRE-specific extensions to the regex syntax. While Perl programmers are encouraged to use the Perl-specific syntax, the following are also accepted:
<dl>
<dt>&quot;(?P&lt;<i>NAME</i>&gt;<i>pattern</i>)&quot;
<dd> Define a named capture group. Equivalent to <tt>&quot;(?&lt;</tt>NAME<tt>&gt;</tt>pattern<tt>)&quot;</tt>.
<dt>&quot;(?P=<i>NAME</i>)&quot;
<dd> Backreference to a named capture group. Equivalent to <tt>&quot;\g{</tt>NAME<tt>}&quot;</tt>.
<dt>&quot;(?P&gt;<i>NAME</i>)&quot;
<dd> Subroutine call to a named capture group. Equivalent to <tt>&quot;(?&amp;</tt>NAME<tt>)&quot;</tt>.</dl>

<h2>BUGS</h2>

 There are a number of issues with regard to case-insensitive matching in Unicode rules. See <tt>&quot;i&quot;</tt> under ``Modifiers'' above. 

 This document varies from difficult to understand to completely and utterly opaque. The wandering prose riddled with jargon is hard to fathom in several places. 

 This document needs a rewrite that separates the tutorial content from the reference content.

<h2>SEE ALSO</h2>

 The syntax of patterns used in Perl pattern matching evolved from those supplied in the Bell Labs Research Unix 8th Edition (Version 8) regex routines. (The code is actually derived (distantly) from Henry Spencer's freely redistributable reimplementation of those V8 routines.) 

 perlrequick. 

 perlretut. 

 ``Regexp Quote-Like Operators'' in perlop. 

 ``Gory details of parsing quoted constructs'' in perlop. 

 perlfaq6. 

 ``pos'' in perlfunc. 

 perllocale. 

 perlebcdic. 

 <i>Mastering Regular Expressions</i> by Jeffrey Friedl, published by O'Reilly and Associates. 

<h2>Index</h2>



<dt><a HREF="#lbAR">BUGS</a>
<dd>
<dt><a HREF="#lbAS">SEE ALSO</a>
<dd></dl>
