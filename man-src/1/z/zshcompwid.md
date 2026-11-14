---
title: "zshcompwid(1)"
name: "zshcompwid"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshcompwid/"
description: "zshcompwid – zsh completion widgets"
---

<h2 class="name">NAME</h2>
<p> zshcompwid &#8211; zsh completion widgets </p>
<h2>DESCRIPTION</h2>
<p> The shell&#8217;s programmable completion mechanism can be manipulated in two ways; here the low-level features supporting the newer, function-based mechanism are defined. A complete set of shell functions based on these features is described in <i><a href="/docs/linux/man/1-zshcompsys/">zshcompsys</a></i>(1), and users with no interest in adding to that system (or, potentially, writing their own &#8212; see dictionary entry for `hubris&#8217;) should skip the current section. The older system based on the <code>compctl</code> builtin command is described in <i><a href="/docs/linux/man/1-zshcompctl/">zshcompctl</a></i>(1). </p>
<p> Completion widgets are defined by the <code>-C</code> option to the <code>zle</code> builtin command provided by the <code>zsh/zle</code> module (see <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1)). For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>zle -C complete expand-or-complete completer</code>
</pre>
</dl>
<p> defines a widget named `<code>complete</code>&#8216;. The second argument is the name of any of the builtin widgets that handle completions: <code>complete-word</code>, <code>expand-or-complete</code>, <code>expand-or-complete-prefix</code>, <code>menu-complete</code>, <code>menu-expand-or-complete</code>, <code>reverse-menu-complete</code>, <code>list-choices</code>, or <code>delete-char-or-list</code>. Note that this will still work even if the widget in question has been re-bound. </p>
<p> When this newly defined widget is bound to a key using the <code>bindkey</code> builtin command defined in the <code>zsh/zle</code> module (see <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1)), typing that key will call the shell function `<code>completer</code>&#8216;. This function is responsible for generating the possible matches using the builtins described below. As with other ZLE widgets, the function is called with its standard input closed. </p>
<p> Once the function returns, the completion code takes over control again and treats the matches in the same manner as the specified builtin widget, in this case <code>expand-or-complete</code>. </p>
<h2>COMPLETION SPECIAL PARAMETERS</h2>
<p> The parameters <code>ZLE_REMOVE_SUFFIX_CHARS</code> and <code>ZLE_SPACE_SUFFIX_CHARS</code> are used by the completion mechanism, but are not special. See <i>Parameters Used By The Shell</i> in <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1). </p>
<p> Inside completion widgets, and any functions called from them, some parameters have special meaning; outside these functions they are not special to the shell in any way. These parameters are used to pass information between the completion code and the completion widget. Some of the builtin commands and the condition codes use or change the current values of these parameters. Any existing values will be hidden during execution of completion widgets; except for <code>compstate</code>, the parameters are reset on each function exit (including nested function calls from within the completion widget) to the values they had when the function was entered. </p>
<dl>
<dt>
<dd> <code>CURRENT</code> This is the number of the current word, i.e. the word the cursor is currently on in the <code>words</code> array. Note that this value is only correct if the <code>ksharrays</code> option is not set.</p>
<dt><code>IPREFIX</code></p>
<dd> Initially this will be set to the empty string. This parameter functions like <code>PREFIX</code>; it contains a string which precedes the one in <code>PREFIX</code> and is not considered part of the list of matches. Typically, a string is transferred from the beginning of <code>PREFIX</code> to the end of <code>IPREFIX</code>, for example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
IPREFIX = ${PREFIX % %\= *} =
    PREFIX = $
{
    PREFIX # *=
}
</code></pre>
</dl>
<p> causes the part of the prefix up to and including the first equal sign not to be treated as part of a matched string. This can be done automatically by the <code>compset</code> builtin, see below.</dl>
<dt><code>ISUFFIX</code></p>
<dd> As <code>IPREFIX</code>, but for a suffix that should not be considered part of the matches; note that the <code>ISUFFIX</code> string follows the <code>SUFFIX</code> string.</p>
<dt><code>PREFIX</code></p>
<dd> Initially this will be set to the part of the current word from the beginning of the word up to the position of the cursor; it may be altered to give a common prefix for all matches.</p>
<dt><code>QIPREFIX</code></p>
<dd> This parameter is read-only and contains the quoted string up to the word being completed. E.g. when completing `<code>&quot;foo</code>&#8216;, this parameter contains the double quote. If the <code>-q</code> option of <code>compset</code> is used (see below), and the original string was `<code>&quot;foo bar</code>&#8216; with the cursor on the `<code>bar</code>&#8216;, this parameter contains `<code>&quot;foo </code>&#8216;.</p>
<dt><code>QISUFFIX</code></p>
<dd> Like <code>QIPREFIX</code>, but containing the suffix.</p>
<dt><code>SUFFIX</code></p>
<dd> Initially this will be set to the part of the current word from the cursor position to the end; it may be altered to give a common suffix for all matches. It is most useful when the option <code>COMPLETE_IN_WORD</code> is set, as otherwise the whole word on the command line is treated as a prefix.</p>
<dt><code>compstate</code></p>
<dd> This is an associative array with various keys and values that the completion code uses to exchange information with the completion widget. The keys are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>all_quotes</code> The <code>-q</code> option of the <code>compset</code> builtin command (see below) allows a quoted string to be broken into separate words; if the cursor is on one of those words, that word will be completed, possibly invoking `<code>compset -q</code>&#8216; recursively. With this key it is possible to test the types of quoted strings which are currently broken into parts in this fashion. Its value contains one character for each quoting level. The characters are a single quote or a double quote for strings quoted with these characters, a dollars sign for strings quoted with <code>$&#8217;</code><i>&#8230;</i><code>&#8216;</code> and a backslash for strings not starting with a quote character. The first character in the value always corresponds to the innermost quoting level.</p>
<dt><code>context</code></p>
<dd> This will be set by the completion code to the overall context in which completion is attempted. Possible values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>array_value</code> when completing inside the value of an array parameter assignment; in this case the <code>words</code> array contains the words inside the parentheses.</p>
<dt><code>brace_parameter</code></p>
<dd> when completing the name of a parameter in a parameter expansion beginning with <code>${</code>. This context will also be set when completing parameter flags following <code>${(</code>; the full command line argument is presented and the handler must test the value to be completed to ascertain that this is the case.</p>
<dt><code>assign_parameter</code></p>
<dd> when completing the name of a parameter in a parameter assignment.</p>
<dt><code>command</code></p>
<dd> when completing for a normal command (either in command position or for an argument of the command).</p>
<dt><code>condition</code></p>
<dd> when completing inside a `<code>[[</code>&#8230;<code>]]</code>&#8216; conditional expression; in this case the <code>words</code> array contains only the words inside the conditional expression.</p>
<dt><code>math</code></p>
<dd> when completing in a mathematical environment such as a `<code>((</code>&#8230;<code>))</code>&#8216; construct.</p>
<dt><code>parameter</code></p>
<dd> when completing the name of a parameter in a parameter expansion beginning with <code>$</code> but not <code>${</code>.</p>
<dt><code>redirect</code></p>
<dd> when completing after a redirection operator.</p>
<dt><code>subscript</code></p>
<dd> when completing inside a parameter subscript.</p>
<dt><code>value</code></p>
<dd> when completing the value of a parameter assignment.</dl>
</dl>
<dt><code>exact</code></p>
<dd> Controls the behaviour when the <code>REC_EXACT</code> option is set. It will be set to <code>accept</code> if an exact match would be accepted, and will be unset otherwise.</p>
<dl>
<dt>
<dd>
<p> If it was set when at least one match equal to the string on the line was generated, the match is accepted.</dl>
<dt><code>exact_string</code></p>
<dd> The string of an exact match if one was found, otherwise unset.</p>
<dt><code>ignored</code></p>
<dd> The number of words that were ignored because they matched one of the patterns given with the <code>-F</code> option to the <code>compadd</code> builtin command.</p>
<dt><code>insert</code></p>
<dd> This controls the manner in which a match is inserted into the command line. On entry to the widget function, if it is unset the command line is not to be changed; if set to <code>unambiguous</code>, any prefix common to all matches is to be inserted; if set to <code>automenu-unambiguous</code>, the common prefix is to be inserted and the next invocation of the completion code may start menu completion (due to the <code>AUTO_MENU</code> option being set); if set to <code>menu</code> or <code>automenu</code> menu completion will be started for the matches currently generated (in the latter case this will happen because the <code>AUTO_MENU</code> is set). The value may also contain the string `<code>tab</code>&#8216; when the completion code would normally not really do completion, but only insert the TAB character.</p>
<dl>
<dt>
<dd>
<p> On exit it may be set to any of the values above (where setting it to the empty string is the same as unsetting it), or to a number, in which case the match whose number is given will be inserted into the command line. Negative numbers count backward from the last match (with `<code>-1</code>&#8216; selecting the last match) and out-of-range values are wrapped around, so that a value of zero selects the last match and a value one more than the maximum selects the first. Unless the value of this key ends in a space, the match is inserted as in a menu completion, i.e. without automatically appending a space. </p>
<p> Both <code>menu</code> and <code>automenu</code> may also specify the number of the match to insert, given after a colon. For example, `<code>menu:2</code>&#8216; says to start menu completion, beginning with the second match. </p>
<p> Note that a value containing the substring `<code>tab</code>&#8216; makes the matches generated be ignored and only the TAB be inserted. </p>
<p> Finally, it may also be set to <code>all</code>, which makes all matches generated be inserted into the line.</dl>
<dt><code>insert_positions</code></p>
<dd> When the completion system inserts an unambiguous string into the line, there may be multiple places where characters are missing or where the character inserted differs from at least one match. The value of this key contains a colon separated list of all these positions, as indexes into the command line.</p>
<dt><code>last_prompt</code></p>
<dd> If this is set to a non-empty string for every match added, the completion code will move the cursor back to the previous prompt after the list of completions has been displayed. Initially this is set or unset according to the <code>ALWAYS_LAST_PROMPT</code> option.</p>
<dt><code>list</code></p>
<dd> This controls whether or how the list of matches will be displayed. If it is unset or empty they will never be listed; if its value begins with <code>list</code>, they will always be listed; if it begins with <code>autolist</code> or <code>ambiguous</code>, they will be listed when the <code>AUTO_LIST</code> or <code>LIST_AMBIGUOUS</code> options respectively would normally cause them to be.</p>
<dl>
<dt>
<dd>
<p> If the substring <code>force</code> appears in the value, this makes the list be shown even if there is only one match. Normally, the list would be shown only if there are at least two matches. </p>
<p> The value contains the substring <code>packed</code> if the <code>LIST_PACKED</code> option is set. If this substring is given for all matches added to a group, this group will show the <code>LIST_PACKED</code> behavior. The same is done for the <code>LIST_ROWS_FIRST</code> option with the substring <code>rows</code>. </p>
<p> Finally, if the value contains the string <code>explanations</code>, only the explanation strings, if any, will be listed and if it contains <code>messages</code>, only the messages (added with the <code>-x</code> option of <code>compadd</code>) will be listed. If it contains both <code>explanations</code> and <code>messages</code> both kinds of explanation strings will be listed. It will be set appropriately on entry to a completion widget and may be changed there.</dl>
<dt><code>list_lines</code></p>
<dd> This gives the number of lines that are needed to display the full list of completions. Note that to calculate the total number of lines to display you need to add the number of lines needed for the command line to this value, this is available as the value of the <code>BUFFERLINES</code> special parameter.</p>
<dt><code>list_max</code></p>
<dd> Initially this is set to the value of the <code>LISTMAX</code> parameter. It may be set to any other value; when the widget exits this value will be used in the same way as the value of <code>LISTMAX</code>.</p>
<dt><code>nmatches</code></p>
<dd> The number of matches generated and accepted by the completion code so far.</p>
<dt><code>old_insert</code></p>
<dd> On entry to the widget this will be set to the number of the match of an old list of completions that is currently inserted into the command line. If no match has been inserted, this is unset.</p>
<dl>
<dt>
<dd>
<p> As with <code>old_list</code>, the value of this key will only be used if it is the string <code>keep</code>. If it was set to this value by the widget and there was an old match inserted into the command line, this match will be kept and if the value of the <code>insert</code> key specifies that another match should be inserted, this will be inserted after the old one.</dl>
<dt><code>old_list</code></p>
<dd> This is set to <code>yes</code> if there is still a valid list of completions from a previous completion at the time the widget is invoked. This will usually be the case if and only if the previous editing operation was a completion widget or one of the builtin completion functions. If there is a valid list and it is also currently shown on the screen, the value of this key is <code>shown</code>.</p>
<dl>
<dt>
<dd>
<p> After the widget has exited the value of this key is only used if it was set to <code>keep</code>. In this case the completion code will continue to use this old list. If the widget generated new matches, they will not be used.</dl>
<dt><code>parameter</code></p>
<dd> The name of the parameter when completing in a subscript or in the value of a parameter assignment.</p>
<dt><code>pattern_insert</code></p>
<dd> Normally this is set to <code>menu</code>, which specifies that menu completion will be used whenever a set of matches was generated using pattern matching. If it is set to any other non-empty string by the user and menu completion is not selected by other option settings, the code will instead insert any common prefix for the generated matches as with normal completion.</p>
<dt><code>pattern_match</code></p>
<dd> Locally controls the behaviour given by the <code>GLOB_COMPLETE</code> option. Initially it is set to `<code>*</code>&#8216; if and only if the option is set. The completion widget may set it to this value, to an empty string (which has the same effect as unsetting it), or to any other non-empty string. If it is non-empty, unquoted metacharacters on the command line will be treated as patterns; if it is `<code>*</code>&#8216;, then additionally a wildcard `<code>*</code>&#8216; is assumed at the cursor position; if it is empty or unset, metacharacters will be treated literally.</p>
<dl>
<dt>
<dd>
<p> Note that the matcher specifications given to the <code>compadd</code> builtin command are not used if this is set to a non-empty string.</dl>
<dt><code>quote</code></p>
<dd> When completing inside quotes, this contains the quotation character (i.e. either a single quote, a double quote, or a backtick). Otherwise it is unset.</p>
<dt><code>quoting</code></p>
<dd> When completing inside single quotes, this is set to the string <code>single</code>; inside double quotes, the string <code>double</code>; inside backticks, the string <code>backtick</code>. Otherwise it is unset.</p>
<dt><code>redirect</code></p>
<dd> The redirection operator when completing in a redirection position, i.e. one of <code>&lt;</code>, <code>&gt;</code>, etc.</p>
<dt><code>restore</code></p>
<dd> This is set to <code>auto</code> before a function is entered, which forces the special parameters mentioned above (<code>words</code>, <code>CURRENT</code>, <code>PREFIX</code>, <code>IPREFIX</code>, <code>SUFFIX</code>, and <code>ISUFFIX</code>) to be restored to their previous values when the function exits. If a function unsets it or sets it to any other string, they will not be restored.</p>
<dt><code>to_end</code></p>
<dd> Specifies the occasions on which the cursor is moved to the end of a string when a match is inserted. On entry to a widget function, it may be <code>single</code> if this will happen when a single unambiguous match was inserted or <code>match</code> if it will happen any time a match is inserted (for example, by menu completion; this is likely to be the effect of the <code>ALWAYS_TO_END</code> option).</p>
<dl>
<dt>
<dd>
<p> On exit, it may be set to <code>single</code> as above. It may also be set to <code>always</code>, or to the empty string or unset; in those cases the cursor will be moved to the end of the string always or never respectively. Any other string is treated as <code>match</code>.</dl>
<dt><code>unambiguous</code></p>
<dd> This key is read-only and will always be set to the common (unambiguous) prefix the completion code has generated for all matches added so far.</p>
<dt><code>unambiguous_cursor</code></p>
<dd> This gives the position the cursor would be placed at if the common prefix in the <code>unambiguous</code> key were inserted, relative to the value of that key. The cursor would be placed before the character whose index is given by this key.</p>
<dt><code>unambiguous_positions</code></p>
<dd> This contains all positions where characters in the unambiguous string are missing or where the character inserted differs from at least one of the matches. The positions are given as indexes into the string given by the value of the <code>unambiguous</code> key.</p>
<dt><code>vared</code></p>
<dd> If completion is called while editing a line using the <code>vared</code> builtin, the value of this key is set to the name of the parameter given as an argument to <code>vared</code>. This key is only set while a <code>vared</code> command is active.</dl>
</dl>
<dt><code>words</code></p>
<dd> This array contains the words present on the command line currently being edited.</dl>
<h2>COMPLETION BUILTIN COMMANDS</h2>
<dl>
<dt>
<dd> <code>compadd </code>[ <code>-akqQfenUl12C</code> ] [ <code>-F</code> <i>array</i> ]</p>
<dt>
<dd> [<code>-P</code> <i>prefix</i> ] [ <code>-S</code> <i>suffix</i> ]</p>
<dt>
<dd> [<code>-p</code> <i>hidden-prefix</i> ] [ <code>-s</code> <i>hidden-suffix</i> ]</p>
<dt>
<dd> [<code>-i</code> <i>ignored-prefix</i> ] [ <code>-I</code> <i>ignored-suffix</i> ]</p>
<dt>
<dd> [<code>-W</code> <i>file-prefix</i> ] [ <code>-d</code> <i>array</i> ]</p>
<dt>
<dd> [<code>-J</code> <i>group-name</i> ] [ <code>-X</code> <i>explanation</i> ] [ <code>-x</code> <i>message</i> ]</p>
<dt>
<dd> [<code>-V</code> <i>group-name</i> ] [ <code>-o</code> [ <i>order</i> ] ]</p>
<dt>
<dd> [<code>-r</code> <i>remove-chars</i> ] [ <code>-R</code> <i>remove-func</i> ]</p>
<dt>
<dd> [<code>-D</code> <i>array</i> ] [ <code>-O</code> <i>array</i> ] [ <code>-A</code> <i>array</i> ]</p>
<dt>
<dd> [<code>-E</code> <i>number</i> ]</p>
<dt>
<dd> [<code>-M</code> <i>match-spec</i> ] [ <code>&#8211;</code><code>&#8211;</code> ] [ <i>words</i> &#8230; ]</p>
<dl>
<dt>
<dd>
<p> This builtin command can be used to add matches directly and control all the information the completion code stores with each possible match. The return status is zero if at least one match was added and non-zero if no matches were added. </p>
<p> The completion code breaks the string to complete into seven fields in the order: </p>
<dl>
<dt>
<dd>
<pre>
<i>&lt;ipre&gt;&lt;apre&gt;&lt;hpre&gt;&lt;word&gt;&lt;hsuf&gt;&lt;asuf&gt;&lt;isuf&gt;</i>
</pre>
</dl>
<p> The first field is an ignored prefix taken from the command line, the contents of the <code>IPREFIX</code> parameter plus the string given with the <code>-i</code> option. With the <code>-U</code> option, only the string from the <code>-i</code> option is used. The field <i>&lt;apre&gt;</i> is an optional prefix string given with the <code>-P</code> option. The <i>&lt;hpre&gt;</i> field is a string that is considered part of the match but that should not be shown when listing completions, given with the <code>-p</code> option; for example, functions that do filename generation might specify a common path prefix this way. <i>&lt;word&gt;</i> is the part of the match that should appear in the list of completions, i.e. one of the <i>words</i> given at the end of the <code>compadd</code> command line. The suffixes <i>&lt;hsuf&gt;</i>, <i>&lt;asuf&gt;</i> and <i>&lt;isuf&gt;</i> correspond to the prefixes <i>&lt;hpre&gt;</i>, <i>&lt;apre&gt;</i> and <i>&lt;ipre&gt;</i> and are given by the options <code>-s</code>, <code>-S</code> and <code>-I</code>, respectively. </p>
<p> The supported flags are: </p>
<dl>
<dt>
<dd> <code>-P</code> <i>prefix</i> This gives a string to be inserted before the given <i>words</i>. The string given is not considered as part of the match and any shell metacharacters in it will not be quoted when the string is inserted.</p>
<dt><code>-S</code> <i>suffix</i></p>
<dd> Like <code>-P</code>, but gives a string to be inserted after the match.</p>
<dt><code>-p</code> <i>hidden-prefix</i></p>
<dd> This gives a string that should be inserted into the command line before the match but that should not appear in the list of matches. Unless the <code>-U</code> option is given, this string must be matched as part of the string on the command line.</p>
<dt><code>-s</code> <i>hidden-suffix</i></p>
<dd> Like `<code>-p</code>&#8216;, but gives a string to insert after the match.</p>
<dt><code>-i</code> <i>ignored-prefix</i></p>
<dd> This gives a string to insert into the command line just before any string given with the `<code>-P</code>&#8216; option. Without `<code>-P</code>&#8216; the string is inserted before the string given with `<code>-p</code>&#8216; or directly before the match.</p>
<dt><code>-I</code> <i>ignored-suffix</i></p>
<dd> Like <code>-i</code>, but gives an ignored suffix.</p>
<dt><code>-a</code></p>
<dd> With this flag the <i>words</i> are taken as names of arrays and the possible matches are their values. If only some elements of the arrays are needed, the <i>words</i> may also contain subscripts, as in `<code>foo[2,-1]</code>&#8216;.</p>
<dt><code>-k</code></p>
<dd> With this flag the <i>words</i> are taken as names of associative arrays and the possible matches are their keys. As for <code>-a</code>, the <i>words</i> may also contain subscripts, as in `<code>foo[(R)*bar*]</code>&#8216;.</p>
<dt><code>-d</code> <i>array</i></p>
<dd> This adds per-match display strings. The <i>array</i> should contain one element per <i>word</i> given. The completion code will then display the first element instead of the first <i>word</i>, and so on. The <i>array</i> may be given as the name of an array parameter or directly as a space-separated list of words in parentheses.</p>
<dl>
<dt>
<dd>
<p> If there are fewer display strings than <i>words</i>, the leftover <i>words</i> will be displayed unchanged and if there are more display strings than <i>words</i>, the leftover display strings will be silently ignored.</dl>
<dt><code>-l</code></p>
<dd> This option only has an effect if used together with the <code>-d</code> option. If it is given, the display strings are listed one per line, not arrayed in columns.</p>
<dt><code>-o</code> [ <i>order</i> ]</p>
<dd> This controls the order in which matches are sorted. <i>order</i> is a comma-separated list comprising the following possible values. These values can be abbreviated to their initial two or three characters. Note that the order forms part of the group name space so matches with different orderings will not be in the same group.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>match</code> If given, the order of the output is determined by the match strings; otherwise it is determined by the display strings (i.e. the strings given by the <code>-d</code> option). This is the default if `<code>-o</code>&#8216; is specified but the <i>order</i> argument is omitted.</p>
<dt><code>nosort</code></p>
<dd> This specifies that the matches are pre-sorted and their order should be preserved. This value only makes sense alone and cannot be combined with any others.</p>
<dt><code>numeric</code></p>
<dd> If the matches include numbers, sort them numerically rather than lexicographically.</p>
<dt><code>reverse</code></p>
<dd> Arrange the matches backwards by reversing the sort ordering.</dl>
</dl>
<dt><code>-J</code> <i>group-name</i></p>
<dd> Gives the name of the group of matches the words should be stored in.</p>
<dt><code>-V</code> <i>group-name</i></p>
<dd> Like <code>-J</code> but naming an unsorted group. This option is identical to the combination of <code>-J</code> and <code>-o nosort</code>.</p>
<dt><code>-1</code></p>
<dd> If given together with the <code>-V</code> option, makes only consecutive duplicates in the group be removed. If combined with the <code>-J</code> option, this has no visible effect. Note that groups with and without this flag are in different name spaces.</p>
<dt><code>-2</code></p>
<dd> If given together with the <code>-J</code> or <code>-V</code> option, makes all duplicates be kept. Again, groups with and without this flag are in different name spaces.</p>
<dt><code>-X</code> <i>explanation</i></p>
<dd> The <i>explanation</i> string will be printed with the list of matches, above the group currently selected.</p>
<dl>
<dt>
<dd>
<p> Within the <i>explanation</i>, the following sequences may be used to specify output attributes as described in the section EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1): `<code>%B</code>&#8216;, `<code>%S</code>&#8216;, `<code>%U</code>&#8216;, `<code>%F</code>&#8216;, `<code>%K</code>&#8216; and their lower case counterparts, as well as `<code>%{</code>&#8230;<code>%}</code>&#8216;. `<code>%F</code>&#8216;, `<code>%K</code>&#8216; and `<code>%{</code>&#8230;<code>%}</code>&#8216; take arguments in the same form as prompt expansion. (Note that the sequence `<code>%G</code>&#8216; is not available; an argument to `<code>%{</code>&#8216; should be used instead.) The sequence `<code>%%</code>&#8216; produces a literal `<code>%</code>&#8216;. </p>
<p> These sequences are most often employed by users when customising the <code>format</code> style (see <i><a href="/docs/linux/man/1-zshcompsys/">zshcompsys</a></i>(1)), but they must also be taken into account when writing completion functions, as passing descriptions with unescaped `<code>%</code>&#8216; characters to utility functions such as <code>_arguments</code> and <code>_message</code> may produce unexpected results. If arbitrary text is to be passed in a description, it can be escaped using e.g. <code>${my_str//\%/%%}</code>.</dl>
<dt><code>-x</code> <i>message</i></p>
<dd> Like <code>-X</code>, but the <i>message</i> will be printed even if there are no matches in the group.</p>
<dt><code>-q</code></p>
<dd> The suffix given with <code>-S</code> will be automatically removed if the next character typed is a blank or does not insert anything, or if the suffix consists of only one character and the next character typed is the same character.</p>
<dt><code>-r</code> <i>remove-chars</i></p>
<dd> This is a more versatile form of the <code>-q</code> option. The suffix given with <code>-S</code> or the slash automatically added after completing directories will be automatically removed if the next character typed inserts one of the characters given in the <i>remove-chars</i>. This string is parsed as a characters class and understands the backslash sequences used by the <code>print</code> command. For example, `<code>-r &quot;a-z	&quot;</code>&#8216; removes the suffix if the next character typed inserts a lower case character or a TAB, and `<code>-r &quot;^0-9&quot;</code>&#8216; removes the suffix if the next character typed inserts anything but a digit. One extra backslash sequence is understood in this string: `<code>\-</code>&#8216; stands for all characters that insert nothing. Thus `<code>-S &quot;=&quot; -q</code>&#8216; is the same as `<code>-S &quot;=&quot; -r &quot;= 	
\-&quot;</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> This option may also be used without the <code>-S</code> option; then any automatically added space will be removed when one of the characters in the list is typed.</dl>
<dt><code>-R</code> <i>remove-func</i></p>
<dd> This is another form of the <code>-r</code> option. When a suffix has been inserted and the completion accepted, the function <i>remove-func</i> will be called after the next character typed. It is passed the length of the suffix as an argument and can use the special parameters available in ordinary (non-completion) zle widgets (see <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1)) to analyse and modify the command line.</p>
<dt><code>-f</code></p>
<dd> If this flag is given, all of the matches built from <i>words</i> are marked as being the names of files. They are not required to be actual filenames, but if they are, and the option <code>LIST_TYPES</code> is set, the characters describing the types of the files in the completion lists will be shown. This also forces a slash to be added when the name of a directory is completed.</p>
<dt><code>-e</code></p>
<dd> This flag can be used to tell the completion code that the matches added are parameter names for a parameter expansion. This will make the <code>AUTO_PARAM_SLASH</code> and <code>AUTO_PARAM_KEYS</code> options be used for the matches.</p>
<dt><code>-W</code> <i>file-prefix</i></p>
<dd> This string is a pathname that will be prepended to each of the matches formed by the given <i>words</i> together with any prefix specified by the <code>-p</code> option to form a complete filename for testing. Hence it is only useful if combined with the <code>-f</code> flag, as the tests will not otherwise be performed.</p>
<dt><code>-F</code> <i>array</i></p>
<dd> Specifies an array containing patterns. Words matching one of these patterns are ignored, i.e. not considered to be possible matches.</p>
<dl>
<dt>
<dd>
<p> The <i>array</i> may be the name of an array parameter or a list of literal patterns enclosed in parentheses and quoted, as in `<code>-F &quot;(*?.o *?.h)&quot;</code>&#8216;. If the name of an array is given, the elements of the array are taken as the patterns.</dl>
<dt><code>-Q</code></p>
<dd> This flag instructs the completion code not to quote any metacharacters in the words when inserting them into the command line.</p>
<dt><code>-M</code> <i>match-spec</i></p>
<dd> This gives local match specifications as described below in the section `Completion Matching Control&#8217;. This option may be given more than once. In this case all <i>match-spec</i>s given are concatenated with spaces between them to form the specification string to use. Note that they will only be used if the <code>-U</code> option is not given.</p>
<dt><code>-n</code></p>
<dd> Specifies that the words added are to be used as possible matches, but are not to appear in the completion listing.</p>
<dt><code>-U</code></p>
<dd> If this flag is given, all words given will be accepted and no matching will be done by the completion code. Normally this is used in functions that do the matching themselves.</p>
<dt><code>-O</code> <i>array</i></p>
<dd> If this option is given, the <i>words</i> are <i>not</i> added to the set of possible completions. Instead, matching is done as usual and all of the <i>words</i> given as arguments that match the string on the command line will be stored in the array parameter whose name is given as <i>array</i>.</p>
<dt><code>-A</code> <i>array</i></p>
<dd> As the <code>-O</code> option, except that instead of those of the <i>words</i> which match being stored in <i>array</i>, the strings generated internally by the completion code are stored. For example, with a matching specification of `<code>-M &quot;L:|no=&quot;</code>&#8216;, the string `<code>nof</code>&#8216; on the command line and the string `<code>foo</code>&#8216; as one of the <i>words</i>, this option stores the string `<code>nofoo</code>&#8216; in the array, whereas the <code>-O</code> option stores the `<code>foo</code>&#8216; originally given.</p>
<dt><code>-D</code> <i>array</i></p>
<dd> As with <code>-O</code>, the <i>words</i> are not added to the set of possible completions. Instead, the completion code tests whether each <i>word</i> in turn matches what is on the line. If the <i>n</i>th <i>word</i> does not match, the <i>n</i>th element of the <i>array</i> is removed. Elements for which the corresponding <i>word</i> is matched are retained.</p>
<dt><code>-C</code></p>
<dd> This option adds a special match which expands to all other matches when inserted into the line, even those that are added after this option is used. Together with the <code>-d</code> option it is possible to specify a string that should be displayed in the list for this special match. If no string is given, it will be shown as a string containing the strings that would be inserted for the other matches, truncated to the width of the screen.</p>
<dt><code>-E</code> <i>number</i></p>
<dd> This option adds <i>number</i> empty matches after the <i>words</i> have been added. An empty match takes up space in completion listings but will never be inserted in the line and can&#8217;t be selected with menu completion or menu selection. This makes empty matches only useful to format completion lists and to make explanatory string be shown in completion lists (since empty matches can be given display strings with the <code>-d</code> option). And because all but one empty string would otherwise be removed, this option implies the <code>-V</code> and <code>-2</code> options (even if an explicit <code>-J</code> option is given). This can be important to note as it affects the name space into which matches are added.</p>
<dt>
<dd> <code>&#8211;</code></p>
<dt>
<dd> <code>&#8211;</code><code>&#8211;</code> This flag ends the list of flags and options. All arguments after it will be taken as the words to use as matches even if they begin with hyphens.</dl>
<p> Except for the <code>-M</code> flag, if any of these flags is given more than once, the first one (and its argument) will be used.</dl>
<dt>
<dd> <code>compset -p</code> <i>number</i></p>
<dt>
<dd> <code>compset -P</code> [ <i>number</i> ] <i>pattern</i></p>
<dt>
<dd> <code>compset -s</code> <i>number</i></p>
<dt>
<dd> <code>compset -S</code> [ <i>number</i> ] <i>pattern</i></p>
<dt>
<dd> <code>compset -n</code> <i>begin</i> [ <i>end</i> ]</p>
<dt>
<dd> <code>compset -N</code> <i>beg-pat</i> [ <i>end-pat</i> ]</p>
<dt>
<dd> <code>compset -q</code> This command simplifies modification of the special parameters, while its return status allows tests on them to be carried out.</p>
<dl>
<dt>
<dd>
<p> The options are: </p>
<dl>
<dt>
<dd> <code>-p</code> <i>number</i> If the value of the <code>PREFIX</code> parameter is at least <i>number</i> characters long, the first <i>number</i> characters are removed from it and appended to the contents of the <code>IPREFIX</code> parameter.</p>
<dt><code>-P</code> [ <i>number</i> ] <i>pattern</i></p>
<dd> If the value of the <code>PREFIX</code> parameter begins with anything that matches the <i>pattern</i>, the matched portion is removed from <code>PREFIX</code> and appended to <code>IPREFIX</code>.</p>
<dl>
<dt>
<dd>
<p> Without the optional <i>number</i>, the longest match is taken, but if <i>number</i> is given, anything up to the <i>number</i>th match is moved. If the <i>number</i> is negative, the <i>number</i>th longest match is moved. For example, if <code>PREFIX</code> contains the string `<code>a=b=c</code>&#8216;, then <code>compset -P &#8216;*\=&#8217;</code> will move the string `<code>a=b=</code>&#8216; into the <code>IPREFIX</code> parameter, but <code>compset -P 1 &#8216;*\=&#8217;</code> will move only the string `<code>a=</code>&#8216;.</dl>
<dt><code>-s</code> <i>number</i></p>
<dd> As <code>-p</code>, but transfer the last <i>number</i> characters from the value of <code>SUFFIX</code> to the front of the value of <code>ISUFFIX</code>.</p>
<dt><code>-S</code> [ <i>number</i> ] <i>pattern</i></p>
<dd> As <code>-P</code>, but match the last portion of <code>SUFFIX</code> and transfer the matched portion to the front of the value of <code>ISUFFIX</code>.</p>
<dt><code>-n</code> <i>begin</i> [ <i>end</i> ]</p>
<dd> If the current word position as specified by the parameter <code>CURRENT</code> is greater than or equal to <i>begin</i>, anything up to the <i>begin</i>th word is removed from the <code>words</code> array and the value of the parameter <code>CURRENT</code> is decremented by <i>begin</i>.</p>
<dl>
<dt>
<dd>
<p> If the optional <i>end</i> is given, the modification is done only if the current word position is also less than or equal to <i>end</i>. In this case, the words from position <i>end</i> onwards are also removed from the <code>words</code> array. </p>
<p> Both <i>begin</i> and <i>end</i> may be negative to count backwards from the last element of the <code>words</code> array.</dl>
<dt><code>-N</code> <i>beg-pat</i> [ <i>end-pat</i> ]</p>
<dd> If one of the elements of the <code>words</code> array before the one at the index given by the value of the parameter <code>CURRENT</code> matches the pattern <i>beg-pat</i>, all elements up to and including the matching one are removed from the <code>words</code> array and the value of <code>CURRENT</code> is changed to point to the same word in the changed array.</p>
<dl>
<dt>
<dd>
<p> If the optional pattern <i>end-pat</i> is also given, and there is an element in the <code>words</code> array matching this pattern, the parameters are modified only if the index of this word is higher than the one given by the <code>CURRENT</code> parameter (so that the matching word has to be after the cursor). In this case, the words starting with the one matching <code>end-pat</code> are also removed from the <code>words</code> array. If <code>words</code> contains no word matching <i>end-pat</i>, the testing and modification is performed as if it were not given.</dl>
<dt><code>-q</code></p>
<dd> The word currently being completed is split on spaces into separate words, respecting the usual shell quoting conventions. The resulting words are stored in the <code>words</code> array, and <code>CURRENT</code>, <code>PREFIX</code>, <code>SUFFIX</code>, <code>QIPREFIX</code>, and <code>QISUFFIX</code> are modified to reflect the word part that is completed.</dl>
<p> In all the above cases the return status is zero if the test succeeded and the parameters were modified and non-zero otherwise. This allows one to use this builtin in tests such as: </p>
<dl>
<dt>
<dd>
<pre>
<code>if compset -P '*\='; then ...</code>
</pre>
</dl>
<p> This forces anything up to and including the last equal sign to be ignored by the completion code.</dl>
<dt><code>compcall</code> [ <code>-TD</code> ]</p>
<dd> This allows the use of completions defined with the <code>compctl</code> builtin from within completion widgets. The list of matches will be generated as if one of the non-widget completion functions (<code>complete-word</code>, etc.) had been called, except that only <code>compctl</code>s given for specific commands are used. To force the code to try completions defined with the <code>-T</code> option of <code>compctl</code> and/or the default completion (whether defined by <code>compctl -D</code> or the builtin default) in the appropriate places, the <code>-T</code> and/or <code>-D</code> flags can be passed to <code>compcall</code>.</p>
<dl>
<dt>
<dd>
<p> The return status can be used to test if a matching <code>compctl</code> definition was found. It is non-zero if a <code>compctl</code> was found and zero otherwise. </p>
<p> Note that this builtin is defined by the <code>zsh/compctl</code> module.</dl>
</dl>
<h2>COMPLETION CONDITION CODES</h2>
<p> The following additional condition codes for use within the <code>[[</code> <i>&#8230;</i> <code>]]</code> construct are available in completion widgets. These work on the special parameters. All of these tests can also be performed by the <code>compset</code> builtin, but in the case of the condition codes the contents of the special parameters are not modified. </p>
<dl>
<dt>
<dd> <code>-prefix</code> [ <i>number</i> ] <i>pattern</i> true if the test for the <code>-P</code> option of <code>compset</code> would succeed.</p>
<dt><code>-suffix</code> [ <i>number</i> ] <i>pattern</i></p>
<dd> true if the test for the <code>-S</code> option of <code>compset</code> would succeed.</p>
<dt><code>-after</code> <i>beg-pat</i></p>
<dd> true if the test of the <code>-N</code> option with only the <i>beg-pat</i> given would succeed.</p>
<dt><code>-between</code> <i>beg-pat end-pat</i></p>
<dd> true if the test for the <code>-N</code> option with both patterns would succeed.</dl>
<h2>COMPLETION MATCHING CONTROL</h2>
<p> It is possible by use of the <code>-M</code> option of the <code>compadd</code> builtin command to specify how the characters in the string to be completed (referred to here as the command line) map onto the characters in the list of matches produced by the completion code (referred to here as the trial completions). Note that this is not used if the command line contains a glob pattern and the <code>GLOB_COMPLETE</code> option is set or the <code>pattern_match</code> of the <code>compstate</code> special association is set to a non-empty string. </p>
<p> The <i>match-spec</i> given as the argument to the <code>-M</code> option (see `Completion Builtin Commands&#8217; above) consists of one or more matching descriptions separated by whitespace. Each description consists of a letter followed by a colon and then the patterns describing which character sequences on the line match which character sequences in the trial completion. Any sequence of characters not handled in this fashion must match exactly, as usual. </p>
<p> The forms of <i>match-spec</i> understood are as follows. In each case, the form with an upper case initial character retains the string already typed on the command line as the final result of completion, while with a lower case initial character the string on the command line is changed into the corresponding part of the trial completion. </p>
<dl>
<dt>
<dd> <code>m:</code><i>lpat</i><code>=</code><i>tpat</i></p>
<dt>
<dd> <code>M:</code><i>lpat</i><code>=</code><i>tpat</i> Here, <i>lpat</i> is a pattern that matches on the command line, corresponding to <i>tpat</i> which matches in the trial completion.</p>
<dt>
<dd> <code>l:</code><i>lanchor</i><code>|</code><i>lpat</i><code>=</code><i>tpat</i></p>
<dt>
<dd> <code>L:</code><i>lanchor</i><code>|</code><i>lpat</i><code>=</code><i>tpat</i></p>
<dt>
<dd> <code>l:</code><i>lanchor</i><code>||</code><i>ranchor</i><code>=</code><i>tpat</i></p>
<dt>
<dd> <code>L:</code><i>lanchor</i><code>||</code><i>ranchor</i><code>=</code><i>tpat</i></p>
<dt>
<dd> <code>b:</code><i>lpat</i><code>=</code><i>tpat</i></p>
<dt>
<dd> <code>B:</code><i>lpat</i><code>=</code><i>tpat</i> These letters are for patterns that are anchored by another pattern on the left side. Matching for <i>lpat</i> and <i>tpat</i> is as for <code>m</code> and <code>M</code>, but the pattern <i>lpat</i> matched on the command line must be preceded by the pattern <i>lanchor</i>. The <i>lanchor</i> can be blank to anchor the match to the start of the command line string; otherwise the anchor can occur anywhere, but must match in both the command line and trial completion strings.</p>
<dl>
<dt>
<dd>
<p> If no <i>lpat</i> is given but a <i>ranchor</i> is, this matches the gap between substrings matched by <i>lanchor</i> and <i>ranchor</i>. Unlike <i>lanchor</i>, the <i>ranchor</i> only needs to match the trial completion string. </p>
<p> The <code>b</code> and <code>B</code> forms are similar to <code>l</code> and <code>L</code> with an empty anchor, but need to match only the beginning of the word on the command line or trial completion, respectively.</dl>
<dt>
<dd> <code>r:</code><i>lpat</i><code>|</code><i>ranchor</i><code>=</code><i>tpat</i></p>
<dt>
<dd> <code>R:</code><i>lpat</i><code>|</code><i>ranchor</i><code>=</code><i>tpat</i></p>
<dt>
<dd> <code>r:</code><i>lanchor</i><code>||</code><i>ranchor</i><code>=</code><i>tpat</i></p>
<dt>
<dd> <code>R:</code><i>lanchor</i><code>||</code><i>ranchor</i><code>=</code><i>tpat</i></p>
<dt>
<dd> <code>e:</code><i>lpat</i><code>=</code><i>tpat</i></p>
<dt>
<dd> <code>E:</code><i>lpat</i><code>=</code><i>tpat</i> As <code>l</code>, <code>L</code>, <code>b</code> and <code>B</code>, with the difference that the command line and trial completion patterns are anchored on the right side. Here an empty <i>ranchor</i> and the <code>e</code> and <code>E</code> forms force the match to the end of the command line or trial completion string.</p>
<dt><code>x:</code></p>
<dd> This form is used to mark the end of matching specifications: subsequent specifications are ignored. In a single standalone list of specifications this has no use but where matching specifications are accumulated, such as from nested function calls, it can allow one function to override another.</dl>
<p> Each <i>lpat</i>, <i>tpat</i> or <i>anchor</i> is either an empty string or consists of a sequence of literal characters (which may be quoted with a backslash), question marks, character classes, and correspondence classes; ordinary shell patterns are not used. Literal characters match only themselves, question marks match any character, and character classes are formed as for globbing and match any character in the given set. </p>
<p> Correspondence classes are defined like character classes, but with two differences: they are delimited by a pair of braces, and negated classes are not allowed, so the characters <code>!</code> and <code>^</code> have no special meaning directly after the opening brace. They indicate that a range of characters on the line match a range of characters in the trial completion, but (unlike ordinary character classes) paired according to the corresponding position in the sequence. For example, to make any ASCII lower case letter on the line match the corresponding upper case letter in the trial completion, you can use `<code>m:{a-z}={A-Z}</code>&#8216; (however, see below for the recommended form for this). More than one pair of classes can occur, in which case the first class before the <code>=</code> corresponds to the first after it, and so on. If one side has more such classes than the other side, the superfluous classes behave like normal character classes. In anchor patterns correspondence classes also behave like normal character classes. </p>
<p> The standard `<code>[:</code><i>name</i><code>:]</code>&#8216; forms described for standard shell patterns (see the section FILENAME GENERATION in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1)) may appear in correspondence classes as well as normal character classes. The only special behaviour in correspondence classes is if the form on the left and the form on the right are each one of <code>[:upper:]</code>, <code>[:lower:]</code>. In these cases the character in the word and the character on the line must be the same up to a difference in case. Hence to make any lower case character on the line match the corresponding upper case character in the trial completion you can use `<code>m:{[:lower:]}={[:upper:]}</code>&#8216;. Although the matching system does not yet handle multibyte characters, this is likely to be a future extension, at which point this syntax will handle arbitrary alphabets; hence this form, rather than the use of explicit ranges, is the recommended form. In other cases `<code>[:</code><i>name</i><code>:]</code>&#8216; forms are allowed. If the two forms on the left and right are the same, the characters must match exactly. In remaining cases, the corresponding tests are applied to both characters, but they are not otherwise constrained; any matching character in one set goes with any matching character in the other set: this is equivalent to the behaviour of ordinary character classes. </p>
<p> The pattern <i>tpat</i> may also be one or two stars, `<code>*</code>&#8216; or `<code>**</code>&#8216;. This means that the pattern on the command line can match any number of characters in the trial completion. In this case the pattern must be anchored (on either side); in the case of a single star, the <i>anchor</i> then determines how much of the trial completion is to be included &#8212; only the characters up to the next appearance of the anchor will be matched. With two stars, substrings matched by the anchor can be matched, too. </p>
<p> Examples: </p>
<p> The keys of the <code>options</code> association defined by the <code>parameter</code> module are the option names in all-lower-case form, without underscores, and without the optional <code>no</code> at the beginning even though the builtins <code>setopt</code> and <code>unsetopt</code> understand option names with upper case letters, underscores, and the optional <code>no</code>. The following alters the matching rules so that the prefix <code>no</code> and any underscore are ignored when trying to match the trial completions generated and upper case letters on the line match the corresponding lower case letters in the words: </p>
<dl>
<dt>
<dd>
compadd &#8211; M &#8216;L:|[nN][oO]= M:_= M:{[:upper:]}={[:lower:]}&#8217; &#8211; \<br />
  $<br />
{<br />
    (k) options<br />
}
</dl>
<p> The first part says that the pattern `<code>[nN][oO]</code>&#8216; at the beginning (the empty anchor before the pipe symbol) of the string on the line matches the empty string in the list of words generated by completion, so it will be ignored if present. The second part does the same for an underscore anywhere in the command line string, and the third part uses correspondence classes so that any upper case letter on the line matches the corresponding lower case letter in the word. The use of the upper case forms of the specification characters (<code>L</code> and <code>M</code>) guarantees that what has already been typed on the command line (in particular the prefix <code>no</code>) will not be deleted. </p>
<p> Note that the use of <code>L</code> in the first part means that it matches only when at the beginning of both the command line string and the trial completion. I.e., the string `<code>_NO_f</code>&#8216; would not be completed to `<code>_NO_foo</code>&#8216;, nor would `<code>NONO_f</code>&#8216; be completed to `<code>NONO_foo</code>&#8216; because of the leading underscore or the second `<code>NO</code>&#8216; on the line which makes the pattern fail even though they are otherwise ignored. To fix this, one would use `<code>B:[nN][oO]=</code>&#8216; instead of the first part. As described above, this matches at the beginning of the trial completion, independent of other characters or substrings at the beginning of the command line word which are ignored by the same or other <i>match-spec</i>s. </p>
<p> The second example makes completion case insensitive. This is just the same as in the option example, except here we wish to retain the characters in the list of completions: </p>
<dl>
<dt>
<dd>
compadd &#8211; M &#8216;m:{[:lower:]}={[:upper:]}&#8217; &#8230;
</dl>
<p> This makes lower case letters match their upper case counterparts. To make upper case letters match the lower case forms as well: </p>
<dl>
<dt>
<dd>
compadd &#8211; M &#8216;m:{[:lower:][:upper:]}={[:upper:][:lower:]}&#8217; &#8230;
</dl>
<p> A nice example for the use of <code>*</code> patterns is partial word completion. Sometimes you would like to make strings like `<code>c.s.u</code>&#8216; complete to strings like `<code>comp.source.unix</code>&#8216;, i.e. the word on the command line consists of multiple parts, separated by a dot in this example, where each part should be completed separately &#8212; note, however, that the case where each part of the word, i.e. `<code>comp</code>&#8216;, `<code>source</code>&#8216; and `<code>unix</code>&#8216; in this example, is to be completed from separate sets of matches is a different problem to be solved by the implementation of the completion widget. The example can be handled by: </p>
<dl>
<dt>
<dd>
<pre>
<code>compadd -M 'r:|.=* r:|=*' \ 
  - comp.sources.unix comp.sources.misc ...</code>
</pre>
</dl>
<p> The first specification says that <i>lpat</i> is the empty string, while <i>anchor</i> is a dot; <i>tpat</i> is <code>*</code>, so this can match anything except for the `<code>.</code>&#8216; from the anchor in the trial completion word. So in `<code>c.s.u</code>&#8216;, the matcher sees `<code>c</code>&#8216;, followed by the empty string, followed by the anchor `<code>.</code>&#8216;, and likewise for the second dot, and replaces the empty strings before the anchors, giving `<code>c</code>[<code>omp</code>]<code>.s</code>[<code>ources</code>]<code>.u</code>[<code>nix</code>]&#8217;, where the last part of the completion is just as normal. </p>
<p> With the pattern shown above, the string `<code>c.u</code>&#8216; could not be completed to `<code>comp.sources.unix</code>&#8216; because the single star means that no dot (matched by the anchor) can be skipped. By using two stars as in `<code>r:|.=**</code>&#8216;, however, `<code>c.u</code>&#8216; could be completed to `<code>comp.sources.unix</code>&#8216;. This also shows that in some cases, especially if the anchor is a real pattern, like a character class, the form with two stars may result in more matches than one would like. </p>
<p> The second specification is needed to make this work when the cursor is in the middle of the string on the command line and the option <code>COMPLETE_IN_WORD</code> is set. In this case the completion code would normally try to match trial completions that end with the string as typed so far, i.e. it will only insert new characters at the cursor position rather than at the end. However in our example we would like the code to recognise matches which contain extra characters after the string on the line (the `<code>nix</code>&#8216; in the example). Hence we say that the empty string at the end of the string on the line matches any characters at the end of the trial completion. </p>
<p> More generally, the specification </p>
<dl>
<dt>
<dd>
<pre>
<code>compadd -M 'r:|[.,_-]=* r:|=*' ... </code>
</pre>
</dl>
<p> allows one to complete words with abbreviations before any of the characters in the square brackets. For example, to complete <code>veryverylongfile.c</code> rather than <code>veryverylongheader.h</code> with the above in effect, you can just type <code>very.c</code> before attempting completion. </p>
<p> The specifications with both a left and a right anchor are useful to complete partial words whose parts are not separated by some special character. For example, in some places strings have to be completed that are formed `<code>LikeThis</code>&#8216; (i.e. the separate parts are determined by a leading upper case letter) or maybe one has to complete strings with trailing numbers. Here one could use the simple form with only one anchor as in: </p>
<dl>
<dt>
<dd>
compadd &#8211; M &#8216;r:|[[:upper:]0-9]=* r:|=*&#8217; LikeTHIS FooHoo 5foo123 5bar234
</dl>
<p> But with this, the string `<code>H</code>&#8216; would neither complete to `<code>FooHoo</code>&#8216; nor to `<code>LikeTHIS</code>&#8216; because in each case there is an upper case letter before the `<code>H</code>&#8216; and that is matched by the anchor. Likewise, a `<code>2</code>&#8216; would not be completed. In both cases this could be changed by using `<code>r:|[[:upper:]0-9]=**</code>&#8216;, but then `<code>H</code>&#8216; completes to both `<code>LikeTHIS</code>&#8216; and `<code>FooHoo</code>&#8216; and a `<code>2</code>&#8216; matches the other strings because characters can be inserted before every upper case letter and digit. To avoid this one would use: </p>
<dl>
<dt>
<dd>
<pre><code>
compadd - M 'r:[^[:upper:]0-9]||[[:upper:]0-9]=** r:|=*' \ 
    LikeTHIS FooHoo foo123 bar234
</code></pre>
</dl>
<p> By using these two anchors, a `<code>H</code>&#8216; matches only upper case `<code>H</code>&#8216;s that are immediately preceded by something matching the left anchor `<code>[^[:upper:]0-9]</code>&#8216;. The effect is, of course, that `<code>H</code>&#8216; matches only the string `<code>FooHoo</code>&#8216;, a `<code>2</code>&#8216; matches only `<code>bar234</code>&#8216; and so on. </p>
<p> When using the completion system (see <i><a href="/docs/linux/man/1-zshcompsys/">zshcompsys</a></i>(1)), users can define match specifications that are to be used for specific contexts by using the <code>matcher</code> and <code>matcher-list</code> styles. The values for the latter will be used everywhere. </p>
<h2>COMPLETION WIDGET EXAMPLE</h2>
<p> The first step is to define the widget: </p>
<dl>
<dt>
<dd>
<pre>
<code>zle -C complete complete-word complete-files</code>
</pre>
</dl>
<p> Then the widget can be bound to a key using the <code>bindkey</code> builtin command: </p>
<dl>
<dt>
<dd>
<pre>
<code>bindkey '^X	' complete</code>
</pre>
</dl>
<p> After that the shell function <code>complete-files</code> will be invoked after typing control-X and TAB. The function should then generate the matches, e.g.: </p>
<dl>
<dt>
<dd>
<pre>
<code>complete-files () { compadd - * }</code>
</pre>
</dl>
<p> This function will complete files in the current directory matching the current word. </p>
<h2>Index</h2>
