---
title: "pcre_table(5)"
name: "pcre_table"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pcre_table/"
description: "pcre_table – format of Postfix PCRE tables"
---

<p>pcre_table &#8211; format of Postfix PCRE tables</p>
<h2>Synopsis</h2>
<pre><code>postmap -q &quot;</code><i>string</i><code>&quot; pcre:/etc/postfix/</code><i>filename</i>
<code>postmap -q - pcre:/etc/postfix/</code><i>filename</i> &lt;<i>inputfile</i></pre>
<h2>Description</h2>
<p>The Postfix mail system uses optional tables for address rewriting, mail routing, or access control. These tables are usually in <code>dbm</code> or <code>db</code> format. </p>
<p> Alternatively, lookup tables can be specified in Perl Compatible Regular Expression form. In this case, each input is compared against a list of patterns. When a match is found, the corresponding result is returned and the search is terminated. </p>
<p> To find out what types of lookup tables your Postfix system supports use the &quot;<code>postconf -m</code>&quot; command. </p>
<p> To test lookup tables, use the &quot;<code>postmap -q</code>&quot; command as described in the SYNOPSIS above.</p>
<h2>Compatibility</h2>
<p>With Postfix version 2.2 and earlier specify &quot;<code>postmap -fq</code>&quot; to query a table that contains case sensitive patterns. Patterns are case insensitive by default.</p>
<h2>Table Format</h2>
<p>The general form of a PCRE table is:</p>
<dl>
<dt><code>/</code><i>pattern</i><code>/</code><i>flags result</i></p>
<dd>When <i>pattern</i> matches the input string, use the corresponding <i>result</i> value.</p>
<dt><code>!/</code><i>pattern</i><code>/</code><i>flags result</i></p>
<dd>When <i>pattern</i> does <code>not</code> match the input string, use the corresponding <i>result</i> value.</p>
<dt><code>if /</code><i>pattern</i><code>/</code><i>flags</i></p>
<dd>
<dt><code>endif</code></p>
<dd>Match the input string against the patterns between <code>if</code> and <code>endif</code>, if and only if that same input string also matches <i>pattern</i>. The <code>if</code>..<code>endif</code> can nest. </p>
<p> Note: do not prepend whitespace to patterns inside <code>if</code>..<code>endif</code>. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<dt><code>if !/</code><i>pattern</i><code>/</code><i>flags</i></p>
<dd>
<dt><code>endif</code></p>
<dd>Match the input string against the patterns between <code>if</code> and <code>endif</code>, if and only if that same input string does <code>not</code> match <i>pattern</i>. The <code>if</code>..<code>endif</code> can nest. </p>
<p> Note: do not prepend whitespace to patterns inside <code>if</code>..<code>endif</code>. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<dt>blank lines and comments</p>
<dd>Empty lines and whitespace-only lines are ignored, as are lines whose first non-whitespace character is a `#&#8217;.</p>
<dt>multi-line text</p>
<dd>A logical line starts with non-whitespace text. A line that starts with whitespace continues a logical line.</dl>
<p> Each pattern is a perl-like regular expression. The expression delimiter can be any non-alphanumerical character, except whitespace or characters that have special meaning (traditionally the forward slash is used). The regular expression can contain whitespace. </p>
<p> By default, matching is case-insensitive, and newlines are not treated as special characters. The behavior is controlled by flags, which are toggled by appending one or more of the following characters after the pattern:</p>
<dl>
<dt><code>i</code> (default: on)</p>
<dd>Toggles the case sensitivity flag. By default, matching is case insensitive.</p>
<dt><code>m</code> (default: off)</p>
<dd>Toggles the PCRE_MULTILINE flag. When this flag is on, the <code>^</code> and <code>$</code> metacharacters match immediately after and immediately before a newline character, respectively, in addition to matching at the start and end of the subject string.</p>
<dt><code>s</code> (default: on)</p>
<dd>Toggles the PCRE_DOTALL flag. When this flag is on, the <code>.</code> metacharacter matches the newline character. With Postfix versions prior to 2.0, the flag is off by default, which is inconvenient for multi-line message header matching.</p>
<dt><code>x</code> (default: off)</p>
<dd>Toggles the pcre extended flag. When this flag is on, whitespace characters in the pattern (other than in a character class) are ignored. To include a whitespace character as part of the pattern, escape it with backslash. </p>
<p> Note: do not use <code>#</code><i>comment</i> after patterns.</p>
<dt><code>A</code> (default: off)</p>
<dd>Toggles the PCRE_ANCHORED flag. When this flag is on, the pattern is forced to be &quot;anchored&quot;, that is, it is constrained to match only at the start of the string which is being searched (the &quot;subject string&quot;). This effect can also be achieved by appropriate constructs in the pattern itself.</p>
<dt><code>E</code> (default: off)</p>
<dd>Toggles the PCRE_DOLLAR_ENDONLY flag. When this flag is on, a <code>$</code> metacharacter in the pattern matches only at the end of the subject string. Without this flag, a dollar also matches immediately before the final character if it is a newline character (but not before any other newline characters). This flag is ignored if PCRE_MULTILINE flag is set.</p>
<dt><code>U</code> (default: off)</p>
<dd>Toggles the ungreedy matching flag. When this flag is on, the pattern matching engine inverts the &quot;greediness&quot; of the quantifiers so that they are not greedy by default, but become greedy if followed by &quot;?&quot;. This flag can also set by a (?U) modifier within the pattern.</p>
<dt><code>X</code> (default: off)</p>
<dd>Toggles the PCRE_EXTRA flag. When this flag is on, any backslash in a pattern that is followed by a letter that has no special meaning causes an error, thus reserving these combinations for future expansion.</dl>
<h2>Search Order</h2>
<p>Patterns are applied in the order as specified in the table, until a pattern is found that matches the input string. </p>
<p> Each pattern is applied to the entire input string. Depending on the application, that string is an entire client hostname, an entire client IP address, or an entire mail address. Thus, no parent domain or parent network search is done, and <i>user [at] domain</i> mail addresses are not broken up into their <i>user</i> and <i>domain</i> constituent parts, nor is <i>user+foo</i> broken up into <i>user</i> and <i>foo</i>.</p>
<h2>Text Substitution</h2>
<p>Substitution of substrings from the matched expression into the result string is possible using the conventional perl syntax ($1, $2, etc.); specify $$ to produce a $ character as output. The macros in the result string may need to be written as ${n} or $(n) if they aren&#8217;t followed by whitespace. </p>
<p> Note: since negated patterns (those preceded by <code>!</code>) return a result when the expression does not match, substitutions are not available for negated patterns.</p>
<h2>Example Smtpd Access Map</h2>
<pre># Protect your outgoing majordomo exploders
/^(?!owner-)(.*)-outgoing@(.*)/ 550 Use ${1}@${2} instead
# Bounce friend [at] whatever, except when whatever is our domain (you would
# be better just bouncing all friend@ mail - this is just an example).
/^(friend@(?!my\.domain$).*)$/ 550 Stick this in your pipe $1
# A multi-line entry. The text is sent as one line.
#
/^noddy@my\.domain$/
&nbsp;<wbr>550 This user is a funny one. You really don't want to send mail to
&nbsp;<wbr>them as it only makes their head spin.</pre>
<h2>Example Header Filter Map</h2>
<pre>/^Subject: make money fast/ REJECT
/^To: friend [at] public\.com/ REJECT</pre>
<h2>Example Body Filter Map</h2>
<pre># First skip over base 64 encoded text to save CPU cycles.
# Requires PCRE version 3.
~^[[:alnum:]+/]{60,}$~ OK
# Put your own body patterns here.</pre>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-regexp_table/">regexp_table</a>(5), format of POSIX regular expression tables</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>DATABASE_README, Postfix lookup table overview</pre>
<h2>Author(S)</h2>
<pre>The PCRE table lookup code was originally written by:
Andrew McNamara
andrewm [at] connect.com.au
connect.com.au Pty. Ltd.
Level 3, 213 Miller St
North Sydney, NSW, Australia
Adopted and adapted by:
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
