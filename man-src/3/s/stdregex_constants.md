---
title: "stdregex_constants(3)"
name: "stdregex_constants"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_constants/"
description: "std::regex_constants –"
---

<p>std::regex_constants &#8211;</p>
<h2>Synopsis</h2>
<h3>5.1 Regular Expression Syntax Options</h3>
<p>enum <code>__syntax_option</code> { <code>_S_icase</code>, <code>_S_nosubs</code>, <code>_S_optimize</code>, <code>_S_collate</code>, <code>_S_ECMAScript</code>, <code>_S_basic</code>, <code>_S_extended</code>, <code>_S_awk</code>, <code>_S_grep</code>, <code>_S_egrep</code>, <code>_S_syntax_last</code> } </p>
<p> typedef unsigned int <code>syntax_option_type</code> </p>
<p> constexpr <code>syntax_option_type</code> <code>icase</code> </p>
<p> constexpr <code>syntax_option_type</code> <code>nosubs</code> </p>
<p> constexpr <code>syntax_option_type</code> <code>optimize</code> </p>
<p> constexpr <code>syntax_option_type</code> <code>collate</code> </p>
<p> constexpr <code>syntax_option_type</code> <code>ECMAScript</code> </p>
<p> constexpr <code>syntax_option_type</code> <code>basic</code> </p>
<p> constexpr <code>syntax_option_type</code> <code>extended</code> </p>
<p> constexpr <code>syntax_option_type</code> <code>awk</code> </p>
<p> constexpr <code>syntax_option_type</code> <code>grep</code> </p>
<p> constexpr <code>syntax_option_type</code> <code>egrep</code></p>
<h3>5.2 Matching Rules</h3>
<p>Matching a regular expression against a sequence of characters [first, last) proceeds according to the rules of the grammar specified for the regular expression object, modified according to the effects listed below for any bitmask elements set.<br />
 enum <code>__match_flag</code> { <code>_S_not_bol</code>, <code>_S_not_eol</code>, <code>_S_not_bow</code>, <code>_S_not_eow</code>, <code>_S_any</code>, <code>_S_not_null</code>, <code>_S_continuous</code>, <code>_S_prev_avail</code>, <code>_S_sed</code>, <code>_S_no_copy</code>, <code>_S_first_only</code>, <code>_S_match_flag_last</code> } </p>
<p> typedef std::bitset<br />
 &lt; _S_match_flag_last &gt; <code>match_flag_type</code>&quot; </p>
<p> constexpr <code>match_flag_type</code> <code>match_default</code> </p>
<p> constexpr <code>match_flag_type</code> <code>match_not_bol</code> </p>
<p> constexpr <code>match_flag_type</code> <code>match_not_eol</code> </p>
<p> constexpr <code>match_flag_type</code> <code>match_not_bow</code> </p>
<p> constexpr <code>match_flag_type</code> <code>match_not_eow</code> </p>
<p> constexpr <code>match_flag_type</code> <code>match_any</code> </p>
<p> constexpr <code>match_flag_type</code> <code>match_not_null</code> </p>
<p> constexpr <code>match_flag_type</code> <code>match_continuous</code> </p>
<p> constexpr <code>match_flag_type</code> <code>match_prev_avail</code> </p>
<p> constexpr <code>match_flag_type</code> <code>format_default</code> </p>
<p> constexpr <code>match_flag_type</code> <code>format_sed</code> </p>
<p> constexpr <code>match_flag_type</code> <code>format_no_copy</code> </p>
<p> constexpr <code>match_flag_type</code> <code>format_first_only</code></p>
<h3>5.3 Error Types</h3>
<p>enum <code>error_type</code> { <code>_S_error_collate</code>, <code>_S_error_ctype</code>, <code>_S_error_escape</code>, <code>_S_error_backref</code>, <code>_S_error_brack</code>, <code>_S_error_paren</code>, <code>_S_error_brace</code>, <code>_S_error_badbrace</code>, <code>_S_error_range</code>, <code>_S_error_space</code>, <code>_S_error_badrepeat</code>, <code>_S_error_complexity</code>, <code>_S_error_stack</code>, <code>_S_error_last</code> } </p>
<p> constexpr <code>error_type</code> <code>error_collate</code> (_S_error_collate) </p>
<p> constexpr <code>error_type</code> <code>error_ctype</code> (_S_error_ctype) </p>
<p> constexpr <code>error_type</code> <code>error_escape</code> (_S_error_escape) </p>
<p> constexpr <code>error_type</code> <code>error_backref</code> (_S_error_backref) </p>
<p> constexpr <code>error_type</code> <code>error_brack</code> (_S_error_brack) </p>
<p> constexpr <code>error_type</code> <code>error_paren</code> (_S_error_paren) </p>
<p> constexpr <code>error_type</code> <code>error_brace</code> (_S_error_brace) </p>
<p> constexpr <code>error_type</code> <code>error_badbrace</code> (_S_error_badbrace) </p>
<p> constexpr <code>error_type</code> <code>error_range</code> (_S_error_range) </p>
<p> constexpr <code>error_type</code> <code>error_space</code> (_S_error_space) </p>
<p> constexpr <code>error_type</code> <code>error_badrepeat</code> (_S_error_badrepeat) </p>
<p> constexpr <code>error_type</code> <code>error_complexity</code> (_S_error_complexity) </p>
<p> constexpr <code>error_type</code> <code>error_stack</code> (_S_error_stack)</p>
<h2>Detailed Description</h2>
<p>ISO C++-0x entities sub namespace for regex.</p>
<h2>Typedef Documentation</h2>
<h3>typedef std::bitset&lt;_S_match_flag_last&gt; <code>std::regex_constants::match_flag_type</code></h3>
<p>This is a bitmask type indicating regex matching rules. The match_flag_type is implementation defined but it is valid to perform bitwise operations on these values and expect the right thing to happen. </p>
<p> Definition at line 198 of file regex_constants.h.</p>
<h3>typedef unsigned int <code>std::regex_constants::syntax_option_type</code></h3>
<p>This is a bitmask type indicating how to interpret the regex. The syntax_option_type is implementation defined but it is valid to perform bitwise operations on these values and expect the right thing to happen. </p>
<p> A valid value of type syntax_option_type shall have exactly one of the elements ECMAScript, basic, extended, awk, grep, egrep set. </p>
<p> Definition at line 80 of file regex_constants.h.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>std::regex_constants::__match_flag</code></h3>
<p>This is a bitmask type indicating regex matching rules. The match_flag_type is implementation defined but it is valid to perform bitwise operations on these values and expect the right thing to happen. </p>
<p> Definition at line 175 of file regex_constants.h.</p>
<h3>enum <code>std::regex_constants::__syntax_option</code></h3>
<p>This is a bitmask type indicating how to interpret the regex. The syntax_option_type is implementation defined but it is valid to perform bitwise operations on these values and expect the right thing to happen. </p>
<p> A valid value of type syntax_option_type shall have exactly one of the elements ECMAScript, basic, extended, awk, grep, egrep set. </p>
<p> Definition at line 54 of file regex_constants.h.</p>
<h3>enum <code>std::regex_constants::error_type</code></h3>
<p>The expression contained an invalid collating element name. </p>
<p> Definition at line 49 of file regex_error.h.</p>
<h2>Function Documentation</h2>
<h3>constexpr <code>error_type</code> std::regex_constants::error_backref (_S_error_backref)</h3>
<p>The expression contained an invalid back reference.</p>
<h3>constexpr <code>error_type</code> std::regex_constants::error_badbrace (_S_error_badbrace)</h3>
<p>The expression contained an invalid range in a {} expression.</p>
<h3>constexpr <code>error_type</code> std::regex_constants::error_badrepeat (_S_error_badrepeat)</h3>
<p>One of <i>*?+{</i> was not preceded by a valid regular expression.</p>
<h3>constexpr <code>error_type</code> std::regex_constants::error_brace (_S_error_brace)</h3>
<p>The expression contained mismatched { and }</p>
<h3>constexpr <code>error_type</code> std::regex_constants::error_brack (_S_error_brack)</h3>
<p>The expression contained mismatched [ and ].</p>
<h3>constexpr <code>error_type</code> std::regex_constants::error_collate (_S_error_collate)</h3>
<p>The expression contained an invalid collating element name.</p>
<h3>constexpr <code>error_type</code> std::regex_constants::error_complexity (_S_error_complexity)</h3>
<p>The complexity of an attempted match against a regular expression exceeded a pre-set level.</p>
<h3>constexpr <code>error_type</code> std::regex_constants::error_ctype (_S_error_ctype)</h3>
<p>The expression contained an invalid character class name.</p>
<h3>constexpr <code>error_type</code> std::regex_constants::error_escape (_S_error_escape)</h3>
<p>The expression contained an invalid escaped character, or a trailing escape.</p>
<h3>constexpr <code>error_type</code> std::regex_constants::error_paren (_S_error_paren)</h3>
<p>The expression contained mismatched ( and ).</p>
<h3>constexpr <code>error_type</code> std::regex_constants::error_range (_S_error_range)</h3>
<p>The expression contained an invalid character range, such as [b-a] in most encodings.</p>
<h3>constexpr <code>error_type</code> std::regex_constants::error_space (_S_error_space)</h3>
<p>There was insufficient memory to convert the expression into a finite state machine.</p>
<h3>constexpr <code>error_type</code> std::regex_constants::error_stack (_S_error_stack)</h3>
<p>There was insufficient memory to determine whether the regular expression could match the specified character sequence.</p>
<h2>Variable Documentation</h2>
<h3>constexpr <code>syntax_option_type</code> std::regex_constants::awk</h3>
<p>Specifies that the grammar recognized by the regular expression engine is that used by POSIX utility awk in IEEE Std 1003.1-2001. This option is identical to syntax_option_type extended, except that C-style escape sequences are supported. These sequences are: \, , , , 
, , 	 , , \&#8217;, &#8216;, and \ddd (where ddd is one, two, or three octal digits). </p>
<p> Definition at line 144 of file regex_constants.h.</p>
<h3>constexpr <code>syntax_option_type</code> std::regex_constants::basic</h3>
<p>Specifies that the grammar recognized by the regular expression engine is that used by POSIX basic regular expressions in IEEE Std 1003.1-2001, Portable Operating System Interface (POSIX), Base Definitions and Headers, Section 9, Regular Expressions [IEEE, Information Technology &#8212; Portable Operating System Interface (POSIX), IEEE Standard 1003.1-2001]. </p>
<p> Definition at line 126 of file regex_constants.h.</p>
<h3>constexpr <code>syntax_option_type</code> std::regex_constants::collate</h3>
<p>Specifies that character ranges of the form [a-b] should be locale sensitive. </p>
<p> Definition at line 107 of file regex_constants.h.</p>
<h3>constexpr <code>syntax_option_type</code> std::regex_constants::ECMAScript</h3>
<p>Specifies that the grammar recognized by the regular expression engine is that used by ECMAScript in ECMA-262 [Ecma International, ECMAScript Language Specification, Standard Ecma-262, third edition, 1999], as modified in section [28.13]. This grammar is similar to that defined in the PERL scripting language but extended with elements found in the POSIX regular expression grammar. </p>
<p> Definition at line 117 of file regex_constants.h.</p>
<h3>constexpr <code>syntax_option_type</code> std::regex_constants::egrep</h3>
<p>Specifies that the grammar recognized by the regular expression engine is that used by POSIX utility grep when given the -E option in IEEE Std 1003.1-2001. This option is identical to syntax_option_type extended, except that newlines are treated as whitespace. </p>
<p> Definition at line 160 of file regex_constants.h.</p>
<h3>constexpr <code>syntax_option_type</code> std::regex_constants::extended</h3>
<p>Specifies that the grammar recognized by the regular expression engine is that used by POSIX extended regular expressions in IEEE Std 1003.1-2001, Portable Operating System Interface (POSIX), Base Definitions and Headers, Section 9, Regular Expressions. </p>
<p> Definition at line 134 of file regex_constants.h.</p>
<h3>constexpr <code>match_flag_type</code> std::regex_constants::format_default</h3>
<p>When a regular expression match is to be replaced by a new string, the new string is constructed using the rules used by the ECMAScript replace function in ECMA- 262 [Ecma International, ECMAScript Language Specification, Standard Ecma-262, third edition, 1999], part 15.5.4.11 String.prototype.replace. In addition, during search and replace operations all non-overlapping occurrences of the regular expression are located and replaced, and sections of the input that did not match the expression are copied unchanged to the output string. </p>
<p> Format strings (from ECMA-262 [15.5.4.11]): </p>
<dl>
<dt>&bull;</p>
<dd>$$ The dollar-sign itself ($)</p>
<dt>&bull;</p>
<dd>$&amp; The matched substring.</p>
<dt>&bull;</p>
<dd>$` The portion of <i>string</i> that precedes the matched substring. This would be match_results::prefix().</p>
<dt>&bull;</p>
<dd>$&#8217; The portion of <i>string</i> that follows the matched substring. This would be match_results::suffix().</p>
<dt>&bull;</p>
<dd>$n The nth capture, where n is in [1,9] and $n is not followed by a decimal digit. If n &lt;= match_results::size() and the nth capture is undefined, use the empty string instead. If n &gt; match_results::size(), the result is implementation-defined.</p>
<dt>&bull;</p>
<dd>$nn The nnth capture, where nn is a two-digit decimal number on [01, 99]. If nn &lt;= match_results::size() and the nth capture is undefined, use the empty string instead. If nn &gt; match_results::size(), the result is implementation-defined.</dl>
<p> Definition at line 280 of file regex_constants.h.</p>
<h3>constexpr <code>match_flag_type</code> std::regex_constants::format_first_only</h3>
<p>When specified during a search and replace operation, only the first occurrence of the regular expression shall be replaced. </p>
<p> Definition at line 301 of file regex_constants.h.</p>
<h3>constexpr <code>match_flag_type</code> std::regex_constants::format_no_copy</h3>
<p>During a search and replace operation, sections of the character container sequence being searched that do not match the regular expression shall not be copied to the output string. </p>
<p> Definition at line 295 of file regex_constants.h.</p>
<h3>constexpr <code>match_flag_type</code> std::regex_constants::format_sed</h3>
<p>When a regular expression match is to be replaced by a new string, the new string is constructed using the rules used by the POSIX sed utility in IEEE Std 1003.1- 2001 [IEEE, Information Technology &#8212; Portable Operating System Interface (POSIX), IEEE Standard 1003.1-2001]. </p>
<p> Definition at line 288 of file regex_constants.h.</p>
<h3>constexpr <code>syntax_option_type</code> std::regex_constants::grep</h3>
<p>Specifies that the grammar recognized by the regular expression engine is that used by POSIX utility grep in IEEE Std 1003.1-2001. This option is identical to syntax_option_type basic, except that newlines are treated as whitespace. </p>
<p> Definition at line 152 of file regex_constants.h.</p>
<h3>constexpr <code>syntax_option_type</code> std::regex_constants::icase</h3>
<p>Specifies that the matching of regular expressions against a character sequence shall be performed without regard to case. </p>
<p> Definition at line 86 of file regex_constants.h.</p>
<h3>constexpr <code>match_flag_type</code> std::regex_constants::match_any</h3>
<p>If more than one match is possible then any match is an acceptable result. </p>
<p> Definition at line 235 of file regex_constants.h.</p>
<h3>constexpr <code>match_flag_type</code> std::regex_constants::match_continuous</h3>
<p>The expression only matches a sub-sequence that begins at first . </p>
<p> Definition at line 245 of file regex_constants.h.</p>
<h3>constexpr <code>match_flag_type</code> std::regex_constants::match_default</h3>
<p>The default matching rules. </p>
<p> Definition at line 203 of file regex_constants.h.</p>
<h3>constexpr <code>match_flag_type</code> std::regex_constants::match_not_bol</h3>
<p>The first character in the sequence [first, last) is treated as though it is not at the beginning of a line, so the character (^) in the regular expression shall not match [first, first). </p>
<p> Definition at line 210 of file regex_constants.h.</p>
<h3>constexpr <code>match_flag_type</code> std::regex_constants::match_not_bow</h3>
<p>The expression  is not matched against the sub-sequence [first,first). </p>
<p> Definition at line 223 of file regex_constants.h.</p>
<h3>constexpr <code>match_flag_type</code> std::regex_constants::match_not_eol</h3>
<p>The last character in the sequence [first, last) is treated as though it is not at the end of a line, so the character ($) in the regular expression shall not match [last, last). </p>
<p> Definition at line 217 of file regex_constants.h.</p>
<h3>constexpr <code>match_flag_type</code> std::regex_constants::match_not_eow</h3>
<p>The expression  should not be matched against the sub-sequence [last,last). </p>
<p> Definition at line 229 of file regex_constants.h.</p>
<h3>constexpr <code>match_flag_type</code> std::regex_constants::match_not_null</h3>
<p>The expression does not match an empty sequence. </p>
<p> Definition at line 240 of file regex_constants.h.</p>
<h3>constexpr <code>match_flag_type</code> std::regex_constants::match_prev_avail</h3>
<p>&#8211;first is a valid iterator position. When this flag is set then the flags match_not_bol and match_not_bow are ignored by the regular expression algorithms 28.11 and iterators 28.12. </p>
<p> Definition at line 252 of file regex_constants.h.</p>
<h3>constexpr <code>syntax_option_type</code> std::regex_constants::nosubs</h3>
<p>Specifies that when a regular expression is matched against a character container sequence, no sub-expression matches are to be stored in the supplied match_results structure. </p>
<p> Definition at line 93 of file regex_constants.h.</p>
<h3>constexpr <code>syntax_option_type</code> std::regex_constants::optimize</h3>
<p>Specifies that the regular expression engine should pay more attention to the speed with which regular expressions are matched, and less to the speed with which regular expression objects are constructed. Otherwise it has no detectable effect on the program output. </p>
<p> Definition at line 101 of file regex_constants.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
