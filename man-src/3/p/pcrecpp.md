---
title: "pcrecpp(3)"
name: "pcrecpp"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcrecpp/"
description: "PCRE – Perl-compatible regular expressions."
---

<p>PCRE &#8211; Perl-compatible regular expressions.</p>
<h2>Synopsis Of C++ Wrapper</h2>
<p><code>#include &lt;pcrecpp.h&gt;</code></p>
<h2>Description</h2>
<p>The C++ wrapper for PCRE was provided by Google Inc. Some additional functionality was added by Giuseppe Maxia. This brief man page was constructed from the notes in the <i>pcrecpp.h</i> file, which should be consulted for further details. Note that the C++ wrapper supports only the original 8-bit PCRE library. There is no 16-bit or 32-bit support at present.</p>
<h2>Matching Interface</h2>
<p>The &quot;FullMatch&quot; operation checks that supplied text matches a supplied pattern exactly. If pointer arguments are supplied, it copies matched sub-strings that match sub-patterns into them. </p>
<p>&nbsp;<wbr>&nbsp;Example: successful match<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::RE re(&quot;h.*o&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;re.FullMatch(&quot;hello&quot;); </p>
<p>&nbsp;<wbr>&nbsp;Example: unsuccessful match&nbsp;(requires full match):<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::RE re(&quot;e&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;!re.FullMatch(&quot;hello&quot;); </p>
<p>&nbsp;<wbr>&nbsp;Example: creating a temporary RE object:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::RE(&quot;h.*o&quot;).FullMatch(&quot;hello&quot;); </p>
<p> You can pass in a &quot;const char*&quot; or a &quot;string&quot; for &quot;text&quot;. The examples below tend to use a const char*. You can, as in the different examples above, store the RE object explicitly in a variable or use a temporary RE object. The examples below use one mode or the other arbitrarily. Either could correctly be used for any of these examples. </p>
<p> You must supply extra pointer arguments to extract matched subpieces. </p>
<p>&nbsp;<wbr>&nbsp;Example: extracts&nbsp;&quot;ruby&quot;&nbsp;into&nbsp;&quot;s&quot;&nbsp;and 1234 into&nbsp;&quot;i&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int i;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;string s;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::RE re(&quot;(\w+):(\d+)&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;re.FullMatch(&quot;ruby:1234&quot;,&nbsp;&amp;s,&nbsp;&amp;i); </p>
<p>&nbsp;<wbr>&nbsp;Example: does not try to extract any extra sub-patterns<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;re.FullMatch(&quot;ruby:1234&quot;,&nbsp;&amp;s); </p>
<p>&nbsp;<wbr>&nbsp;Example: does not try to extract into NULL<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;re.FullMatch(&quot;ruby:1234&quot;, NULL,&nbsp;&amp;i); </p>
<p>&nbsp;<wbr>&nbsp;Example: integer overflow causes failure<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;!re.FullMatch(&quot;ruby:1234567891234&quot;, NULL,&nbsp;&amp;i); </p>
<p>&nbsp;<wbr>&nbsp;Example: fails because there aren&#8217;t enough sub-patterns:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;!pcrecpp::RE(&quot;\w+:\d+&quot;).FullMatch(&quot;ruby:1234&quot;,&nbsp;&amp;s); </p>
<p>&nbsp;<wbr>&nbsp;Example: fails because string cannot be stored in integer<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;!pcrecpp::RE(&quot;(.*)&quot;).FullMatch(&quot;ruby&quot;,&nbsp;&amp;i); </p>
<p> The provided pointer arguments can be pointers to any scalar numeric type, or one of: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;string&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(matched piece is copied to string)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;StringPiece&nbsp;<wbr>&nbsp;<wbr>&nbsp;(StringPiece is mutated to point to matched piece)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;T&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(where&nbsp;&quot;bool T::ParseFrom(const char*, int)&quot;&nbsp;exists)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;NULL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(the corresponding matched sub-pattern is not copied) </p>
<p> The function returns true iff all of the following conditions are satisfied: </p>
<p>&nbsp;<wbr>&nbsp;a.&nbsp;&quot;text&quot;&nbsp;matches&nbsp;&quot;pattern&quot;&nbsp;exactly; </p>
<p>&nbsp;<wbr>&nbsp;b. The number of matched sub-patterns is&nbsp;&gt;=&nbsp;number of supplied<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pointers; </p>
<p>&nbsp;<wbr>&nbsp;c. The&nbsp;&quot;i&quot;th argument has a suitable type for holding the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;string captured as the&nbsp;&quot;i&quot;th sub-pattern. If you pass in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;*&nbsp;NULL for the&nbsp;&quot;i&quot;th argument, or a non-void&nbsp;*&nbsp;NULL<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;of the correct type, or pass fewer arguments than the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;number of sub-patterns,&nbsp;&quot;i&quot;th captured sub-pattern is<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ignored. </p>
<p> CAVEAT: An optional sub-pattern that does not exist in the matched string is assigned the empty string. Therefore, the following will return false (because the empty string is not a valid number): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int number;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::RE::FullMatch(&quot;abc&quot;,&nbsp;&quot;[a-z]+(\d+)?&quot;,&nbsp;&amp;number); </p>
<p> The matching interface supports at most 16 arguments per call. If you need more, consider using the more general interface <code>pcrecpp::RE::DoMatch</code>. See <code>pcrecpp.h</code> for the signature for <code>DoMatch</code>. </p>
<p> NOTE: Do not use <code>no_arg</code>, which is used internally to mark the end of a list of optional arguments, as a placeholder for missing arguments, as this can lead to segfaults.</p>
<h2>Quoting Metacharacters</h2>
<p>You can use the &quot;QuoteMeta&quot; operation to insert backslashes before all potentially meaningful characters in a string. The returned string, used as a regular expression, will exactly match the original string. </p>
<p>&nbsp;<wbr>&nbsp;Example:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;string quoted&nbsp;=&nbsp;RE::QuoteMeta(unquoted); </p>
<p> Note that it&#8217;s legal to escape a character even if it has no special meaning in a regular expression &#8212; so this function does that. (This also makes it identical to the perl function of the same name; see &quot;perldoc -f quotemeta&quot;.) For example, &quot;1.5-2.0?&quot; becomes &quot;1\.5\-2\.0\?&quot;.</p>
<h2>Partial Matches</h2>
<p>You can use the &quot;PartialMatch&quot; operation when you want the pattern to match any substring of the text. </p>
<p>&nbsp;<wbr>&nbsp;Example: simple search for a string:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::RE(&quot;ell&quot;).PartialMatch(&quot;hello&quot;); </p>
<p>&nbsp;<wbr>&nbsp;Example: find first number in a string:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int number;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::RE re(&quot;(\d+)&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;re.PartialMatch(&quot;x*100&nbsp;+&nbsp;20&quot;,&nbsp;&amp;number);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assert(number&nbsp;==&nbsp;100);</p>
<h2>Utf-8 And The Matching Interface</h2>
<p>By default, pattern and text are plain text, one byte per character. The UTF8 flag, passed to the constructor, causes both pattern and string to be treated as UTF-8 text, still a byte stream but potentially multiple bytes per character. In practice, the text is likelier to be UTF-8 than the pattern, but the match returned may depend on the UTF8 flag, so always use it when matching UTF8 text. For example, &quot;.&quot; will match one byte normally but with UTF8 set may match up to three bytes of a multi-byte character. </p>
<p>&nbsp;<wbr>&nbsp;Example:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::RE_Options options;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;options.set_utf8();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::RE re(utf8_pattern, options);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;re.FullMatch(utf8_string); </p>
<p>&nbsp;<wbr>&nbsp;Example: using the convenience function UTF8():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::RE re(utf8_pattern, pcrecpp::UTF8());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;re.FullMatch(utf8_string); </p>
<p> NOTE: The UTF8 flag is ignored if pcre was not configured with the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;enable-utf8 flag.</p>
<h2>Passing Modifiers To The Regular Expression Engine</h2>
<p>PCRE defines some modifiers to change the behavior of the regular expression engine. The C++ wrapper defines an auxiliary class, RE_Options, as a vehicle to pass such modifiers to a RE class. Currently, the following modifiers are supported: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;modifier&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;description&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Perl corresponding </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_CASELESS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case insensitive match&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/i<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_MULTILINE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;multiple lines match&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/m<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_DOTALL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dot matches newlines&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/s<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_DOLLAR_ENDONLY&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;matches only at end&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;N/A<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_EXTRA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strict escape parsing&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;N/A<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_EXTENDED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ignore white spaces&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/x<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_UTF8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handles UTF8 chars&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;built-in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_UNGREEDY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reverses&nbsp;*&nbsp;and&nbsp;*?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;N/A<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_NO_AUTO_CAPTURE&nbsp;<wbr>&nbsp;disables capturing parens&nbsp;<wbr>&nbsp;<wbr>&nbsp;N/A&nbsp;(*) </p>
<p> (*) Both Perl and PCRE allow non capturing parentheses by means of the &quot;?:&quot; modifier within the pattern itself. e.g. (?:ab|cd) does not capture, while (ab|cd) does. </p>
<p> For a full account on how each modifier works, please check the PCRE API reference page. </p>
<p> For each modifier, there are two member functions whose name is made out of the modifier in lowercase, without the &quot;PCRE_&quot; prefix. For instance, PCRE_CASELESS is handled by </p>
<p>&nbsp;<wbr>&nbsp;bool caseless() </p>
<p> which returns true if the modifier is set, and </p>
<p>&nbsp;<wbr>&nbsp;RE_Options&nbsp;&amp;&nbsp;set_caseless(bool) </p>
<p> which sets or unsets the modifier. Moreover, PCRE_EXTRA_MATCH_LIMIT can be accessed through the <code>set_match_limit()</code> and <code>match_limit()</code> member functions. Setting <i>match_limit</i> to a non-zero value will limit the execution of pcre to keep it from doing bad things like blowing the stack or taking an eternity to return a result. A value of 5000 is good enough to stop stack blowup in a 2MB thread stack. Setting <i>match_limit</i> to zero disables match limiting. Alternatively, you can call <code>match_limit_recursion()</code> which uses PCRE_EXTRA_MATCH_LIMIT_RECURSION to limit how much PCRE recurses. <code>match_limit()</code> limits the number of matches PCRE does; <code>match_limit_recursion()</code> limits the depth of internal recursion, and therefore the amount of stack that is used. </p>
<p> Normally, to pass one or more modifiers to a RE class, you declare a <i>RE_Options</i> object, set the appropriate options, and pass this object to a RE constructor. Example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;RE_Options opt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;opt.set_caseless(true);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(RE(&quot;HELLO&quot;, opt).PartialMatch(&quot;hello world&quot;))&nbsp;&#8230; </p>
<p> RE_options has two constructors. The default constructor takes no arguments and creates a set of flags that are off by default. The optional parameter <i>option_flags</i> is to facilitate transfer of legacy code from C programs. This lets you do </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;RE(pattern,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;RE_Options(PCRE_CASELESS|PCRE_MULTILINE)).PartialMatch(str); </p>
<p> However, new code is better off doing </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;RE(pattern,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;RE_Options().set_caseless(true).set_multiline(true))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.PartialMatch(str); </p>
<p> If you are going to pass one of the most used modifiers, there are some convenience functions that return a RE_Options class with the appropriate modifier already set: <code>CASELESS()</code>, <code>UTF8()</code>, <code>MULTILINE()</code>, <code>DOTALL</code>(), and <code>EXTENDED()</code>. </p>
<p> If you need to set several options at once, and you don&#8217;t want to go through the pains of declaring a RE_Options object and setting several options, there is a parallel method that give you such ability on the fly. You can concatenate several <code>set_xxxxx()</code> member functions, since each of them returns a reference to its class object. For example, to pass PCRE_CASELESS, PCRE_EXTENDED, and PCRE_MULTILINE to a RE with one statement, you may write: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;RE(&quot;&nbsp;^&nbsp;xyz&nbsp;\s+&nbsp;.*&nbsp;blah$&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;RE_Options()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.set_caseless(true)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.set_extended(true)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.set_multiline(true)).PartialMatch(sometext);</p>
<h2>Scanning Text Incrementally</h2>
<p>The &quot;Consume&quot; operation may be useful if you want to repeatedly match regular expressions at the front of a string and skip over them as they match. This requires use of the &quot;StringPiece&quot; type, which represents a sub-range of a real string. Like RE, StringPiece is defined in the pcrecpp namespace. </p>
<p>&nbsp;<wbr>&nbsp;Example: read lines of the form&nbsp;&quot;var&nbsp;=&nbsp;value&quot;&nbsp;from a string.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;string contents&nbsp;=&nbsp;&#8230;;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;//&nbsp;Fill string somehow<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::StringPiece input(contents);&nbsp;<wbr>&nbsp;//&nbsp;Wrap in a StringPiece </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;string var;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int value;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::RE re(&quot;(\w+)&nbsp;=&nbsp;(\d+)
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(re.Consume(&amp;input,&nbsp;&amp;var,&nbsp;&amp;value))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> Each successful call to &quot;Consume&quot; will set &quot;var/value&quot;, and also advance &quot;input&quot; so it points past the matched text. </p>
<p> The &quot;FindAndConsume&quot; operation is similar to &quot;Consume&quot; but does not anchor your match at the beginning of the string. For example, you could extract all words from a string by repeatedly calling </p>
<p>&nbsp;<wbr>&nbsp;pcrecpp::RE(&quot;(\w+)&quot;).FindAndConsume(&amp;input,&nbsp;&amp;word)</p>
<h2>Parsing Hex/Octal/C-Radix Numbers</h2>
<p>By default, if you pass a pointer to a numeric value, the corresponding text is interpreted as a base-10 number. You can instead wrap the pointer with a call to one of the operators Hex(), Octal(), or CRadix() to interpret the text in another base. The CRadix operator interprets C-style &quot;0&quot; (base-8) and &quot;0x&quot; (base-16) prefixes, but defaults to base-10. </p>
<p>&nbsp;<wbr>&nbsp;Example:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int a, b, c, d;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::RE re(&quot;(.*)&nbsp;(.*)&nbsp;(.*)&nbsp;(.*)&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;re.FullMatch(&quot;100 40 0100 0x40&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::Octal(&amp;a), pcrecpp::Hex(&amp;b),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcrecpp::CRadix(&amp;c), pcrecpp::CRadix(&amp;d)); </p>
<p> will leave 64 in a, b, c, and d.</p>
<h2>Replacing Parts Of Strings</h2>
<p>You can replace the first match of &quot;pattern&quot; in &quot;str&quot; with &quot;rewrite&quot;. Within &quot;rewrite&quot;, backslash-escaped digits (\1 to \9) can be used to insert text matching corresponding parenthesized group from the pattern. 
