---
title: "tcl_regexprange(3)"
name: "tcl_regexprange"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_regexprange/"
description: "Tcl_RegExpMatch, Tcl_RegExpCompile, Tcl_RegExpExec, Tcl_RegExpRange, Tcl_GetRegExpFromObj, Tcl_RegExpMatchObj, Tcl_RegExpExecObj, Tcl_RegExpGetInfo – Pattern matching with regular expressions"
---

<p>Tcl_RegExpMatch, Tcl_RegExpCompile, Tcl_RegExpExec, Tcl_RegExpRange, Tcl_GetRegExpFromObj, Tcl_RegExpMatchObj, Tcl_RegExpExecObj, Tcl_RegExpGetInfo &#8211; Pattern matching with regular expressions </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_RegExpMatchObj</code>(<i>interp</i>, <i>textObj</i>, <i>patObj</i>)
int
<code>Tcl_RegExpMatch</code>(<i>interp</i>, <i>text</i>, <i>pattern</i>)
Tcl_RegExp
<code>Tcl_RegExpCompile</code>(<i>interp</i>, <i>pattern</i>)
int
<code>Tcl_RegExpExec</code>(<i>interp</i>, <i>regexp</i>, <i>text</i>, <i>start</i>)
void
<code>Tcl_RegExpRange</code>(<i>regexp</i>, <i>index</i>, <i>startPtr</i>, <i>endPtr</i>)
Tcl_RegExp
<code>Tcl_GetRegExpFromObj</code>(<i>interp</i>, <i>patObj</i>, <i>cflags</i>)
int
<code>Tcl_RegExpExecObj</code>(<i>interp</i>, <i>regexp</i>, <i>textObj</i>, <i>offset</i>, <i>nmatches</i>, <i>eflags</i>)
void
<code>Tcl_RegExpGetInfo</code>(<i>regexp</i>, <i>infoPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Tcl interpreter to use for error reporting. The interpreter may be NULL if no error reporting is desired.</p>
<dd>Tcl_Obj <i>*textObj</i> (in/out) Refers to the object from which to get the text to search. The internal representation of the object may be converted to a form that can be efficiently searched.</p>
<dd>Tcl_Obj <i>*patObj</i> (in/out) Refers to the object from which to get a regular expression. The compiled regular expression is cached in the object.</p>
<dd>char <i>*text</i> (in) Text to search for a match with a regular expression.</p>
<dd>const char <i>*pattern</i> (in) String in the form of a regular expression pattern.</p>
<dd>Tcl_RegExp <i>regexp</i> (in) Compiled regular expression. Must have been returned previously by <code>Tcl_GetRegExpFromObj</code> or <code>Tcl_RegExpCompile</code>.</p>
<dd>char <i>*start</i> (in) If <i>text</i> is just a portion of some other string, this argument identifies the beginning of the larger string. If it is not the same as <i>text</i>, then no &#8220;<code>^</code>&#8221; matches will be allowed.</p>
<dd>int <i>index</i> (in) Specifies which range is desired: 0 means the range of the entire match, 1 or greater means the range that matched a parenthesized sub-expression.</p>
<dd>const char <i>**startPtr</i> (out) The address of the first character in the range is stored here, or NULL if there is no such range.</p>
<dd>const char <i>**endPtr</i> (out) The address of the character just after the last one in the range is stored here, or NULL if there is no such range.</p>
<dd>int <i>cflags</i> (in) OR-ed combination of the compilation flags <code>TCL_REG_ADVANCED</code>, <code>TCL_REG_EXTENDED</code>, <code>TCL_REG_BASIC</code>, <code>TCL_REG_EXPANDED</code>, <code>TCL_REG_QUOTE</code>, <code>TCL_REG_NOCASE</code>, <code>TCL_REG_NEWLINE</code>, <code>TCL_REG_NLSTOP</code>, <code>TCL_REG_NLANCH</code>, <code>TCL_REG_NOSUB</code>, and <code>TCL_REG_CANMATCH</code>. See below for more information.</p>
<dd>int <i>offset</i> (in) The character offset into the text where matching should begin. The value of the offset has no impact on <code>^</code> matches. This behavior is controlled by <i>eflags</i>.</p>
<dd>int <i>nmatches</i> (in) The number of matching subexpressions that should be remembered for later use. If this value is 0, then no subexpression match information will be computed. If the value is -1, then all of the matching subexpressions will be remembered. Any other value will be taken as the maximum number of subexpressions to remember.</p>
<dd>int <i>eflags</i> (in) OR-ed combination of the execution flags <code>TCL_REG_NOTBOL</code> and <code>TCL_REG_NOTEOL</code>. See below for more information.</p>
<dd>Tcl_RegExpInfo <i>*infoPtr</i> (out) The address of the location where information about a previous match should be stored by <code>Tcl_RegExpGetInfo</code>.
</dl>
<h2>Description</h2>
<p><code>Tcl_RegExpMatch</code> determines whether its <i>pattern</i> argument matches <i>regexp</i>, where <i>regexp</i> is interpreted as a regular expression using the rules in the <code>re_syntax</code> reference page. If there is a match then <code>Tcl_RegExpMatch</code> returns 1. If there is no match then <code>Tcl_RegExpMatch</code> returns 0. If an error occurs in the matching process (e.g. <i>pattern</i> is not a valid regular expression) then <code>Tcl_RegExpMatch</code> returns -1 and leaves an error message in the interpreter result. <code>Tcl_RegExpMatchObj</code> is similar to <code>Tcl_RegExpMatch</code> except it operates on the Tcl objects <i>textObj</i> and <i>patObj</i> instead of UTF strings. <code>Tcl_RegExpMatchObj</code> is generally more efficient than <code>Tcl_RegExpMatch</code>, so it is the preferred interface. </p>
<p> <code>Tcl_RegExpCompile</code>, <code>Tcl_RegExpExec</code>, and <code>Tcl_RegExpRange</code> provide lower-level access to the regular expression pattern matcher. <code>Tcl_RegExpCompile</code> compiles a regular expression string into the internal form used for efficient pattern matching. The return value is a token for this compiled form, which can be used in subsequent calls to <code>Tcl_RegExpExec</code> or <code>Tcl_RegExpRange</code>. If an error occurs while compiling the regular expression then <code>Tcl_RegExpCompile</code> returns NULL and leaves an error message in the interpreter result. Note: the return value from <code>Tcl_RegExpCompile</code> is only valid up to the next call to <code>Tcl_RegExpCompile</code>; it is not safe to retain these values for long periods of time. </p>
<p> <code>Tcl_RegExpExec</code> executes the regular expression pattern matcher. It returns 1 if <i>text</i> contains a range of characters that match <i>regexp</i>, 0 if no match is found, and -1 if an error occurs. In the case of an error, <code>Tcl_RegExpExec</code> leaves an error message in the interpreter result. When searching a string for multiple matches of a pattern, it is important to distinguish between the start of the original string and the start of the current search. For example, when searching for the second occurrence of a match, the <i>text</i> argument might point to the character just after the first match; however, it is important for the pattern matcher to know that this is not the start of the entire string, so that it does not allow &#8220;<code>^</code>&#8221; atoms in the pattern to match. The <i>start</i> argument provides this information by pointing to the start of the overall string containing <i>text</i>. <i>Start</i> will be less than or equal to <i>text</i>; if it is less than <i>text</i> then no <code>^</code> matches will be allowed. </p>
<p> <code>Tcl_RegExpRange</code> may be invoked after <code>Tcl_RegExpExec</code> returns; it provides detailed information about what ranges of the string matched what parts of the pattern. <code>Tcl_RegExpRange</code> returns a pair of pointers in <i>*startPtr</i> and <i>*endPtr</i> that identify a range of characters in the source string for the most recent call to <code>Tcl_RegExpExec</code>. <i>Index</i> indicates which of several ranges is desired: if <i>index</i> is 0, information is returned about the overall range of characters that matched the entire pattern; otherwise, information is returned about the range of characters that matched the <i>index</i>&#8216;th parenthesized subexpression within the pattern. If there is no range corresponding to <i>index</i> then NULL is stored in <i>*startPtr</i> and <i>*endPtr</i>. </p>
<p> <code>Tcl_GetRegExpFromObj</code>, <code>Tcl_RegExpExecObj</code>, and <code>Tcl_RegExpGetInfo</code> are object interfaces that provide the most direct control of Henry Spencer&#8217;s regular expression library. For users that need to modify compilation and execution options directly, it is recommended that you use these interfaces instead of calling the internal regexp functions. These interfaces handle the details of UTF to Unicode translations as well as providing improved performance through caching in the pattern and string objects. </p>
<p> <code>Tcl_GetRegExpFromObj</code> attempts to return a compiled regular expression from the <i>patObj</i>. If the object does not already contain a compiled regular expression it will attempt to create one from the string in the object and assign it to the internal representation of the <i>patObj</i>. The return value of this function is of type <code>Tcl_RegExp</code>. The return value is a token for this compiled form, which can be used in subsequent calls to <code>Tcl_RegExpExecObj</code> or <code>Tcl_RegExpGetInfo</code>. If an error occurs while compiling the regular expression then <code>Tcl_GetRegExpFromObj</code> returns NULL and leaves an error message in the interpreter result. The regular expression token can be used as long as the internal representation of <i>patObj</i> refers to the compiled form. The <i>cflags</i> argument is a bit-wise OR of zero or more of the following flags that control the compilation of <i>patObj</i>:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>TCL_REG_ADVANCED</code></p>
<dd>Compile advanced regular expressions (&#8220;ARE&#8221;s). This mode corresponds to the normal regular expression syntax accepted by the Tcl <code>regexp</code> and <code>regsub</code> commands.</p>
<dt><code>TCL_REG_EXTENDED</code></p>
<dd>Compile extended regular expressions (&#8220;ERE&#8221;s). This mode corresponds to the regular expression syntax recognized by Tcl 8.0 and earlier versions.</p>
<dt><code>TCL_REG_BASIC</code></p>
<dd>Compile basic regular expressions (&#8220;BRE&#8221;s). This mode corresponds to the regular expression syntax recognized by common Unix utilities like <code>sed</code> and <code>grep</code>. This is the default if no flags are specified.</p>
<dt><code>TCL_REG_EXPANDED</code></p>
<dd>Compile the regular expression (basic, extended, or advanced) using an expanded syntax that allows comments and whitespace. This mode causes non-backslashed non-bracket-expression white space and #-to-end-of-line comments to be ignored.</p>
<dt><code>TCL_REG_QUOTE</code></p>
<dd>Compile a literal string, with all characters treated as ordinary characters.</p>
<dt><code>TCL_REG_NOCASE</code></p>
<dd>Compile for matching that ignores upper/lower case distinctions.</p>
<dt><code>TCL_REG_NEWLINE</code></p>
<dd>Compile for newline-sensitive matching. By default, newline is a completely ordinary character with no special meaning in either regular expressions or strings. With this flag, &#8220;[^&#8221; bracket expressions and &#8220;.&#8221; never match newline, &#8220;^&#8221; matches an empty string after any newline in addition to its normal function, and &#8220;$&#8221; matches an empty string before any newline in addition to its normal function. <code>REG_NEWLINE</code> is the bit-wise OR of <code>REG_NLSTOP</code> and <code>REG_NLANCH</code>.</p>
<dt><code>TCL_REG_NLSTOP</code></p>
<dd>Compile for partial newline-sensitive matching, with the behavior of &#8220;[^&#8221; bracket expressions and &#8220;.&#8221; affected, but not the behavior of &#8220;^&#8221; and &#8220;$&#8221;. In this mode, &#8220;[^&#8221; bracket expressions and &#8220;.&#8221; never match newline.</p>
<dt><code>TCL_REG_NLANCH</code></p>
<dd>Compile for inverse partial newline-sensitive matching, with the behavior of &#8220;^&#8221; and &#8220;$&#8221; (the &#8220;anchors&#8221;) affected, but not the behavior of &#8220;[^&#8221; bracket expressions and &#8220;.&#8221;. In this mode &#8220;^&#8221; matches an empty string after any newline in addition to its normal function, and &#8220;$&#8221; matches an empty string before any newline in addition to its normal function.</p>
<dt><code>TCL_REG_NOSUB</code></p>
<dd>Compile for matching that reports only success or failure, not what was matched. This reduces compile overhead and may improve performance. Subsequent calls to <code>Tcl_RegExpGetInfo</code> or <code>Tcl_RegExpRange</code> will not report any match information.</p>
<dt><code>TCL_REG_CANMATCH</code></p>
<dd>Compile for matching that reports the potential to complete a partial match given more text (see below).</dl>
</dl>
<p> Only one of <code>TCL_REG_EXTENDED</code>, <code>TCL_REG_ADVANCED</code>, <code>TCL_REG_BASIC</code>, and <code>TCL_REG_QUOTE</code> may be specified. </p>
<p> <code>Tcl_RegExpExecObj</code> executes the regular expression pattern matcher. It returns 1 if <i>objPtr</i> contains a range of characters that match <i>regexp</i>, 0 if no match is found, and -1 if an error occurs. In the case of an error, <code>Tcl_RegExpExecObj</code> leaves an error message in the interpreter result. The <i>nmatches</i> value indicates to the matcher how many subexpressions are of interest. If <i>nmatches</i> is 0, then no subexpression match information is recorded, which may allow the matcher to make various optimizations. If the value is -1, then all of the subexpressions in the pattern are remembered. If the value is a positive integer, then only that number of subexpressions will be remembered. Matching begins at the specified Unicode character index given by <i>offset</i>. Unlike <code>Tcl_RegExpExec</code>, the behavior of anchors is not affected by the offset value. Instead the behavior of the anchors is explicitly controlled by the <i>eflags</i> argument, which is a bit-wise OR of zero or more of the following flags:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>TCL_REG_NOTBOL</code></p>
<dd>The starting character will not be treated as the beginning of a line or the beginning of the string, so &#8220;^&#8221; will not match there. Note that this flag has no effect on how &#8220;<code>\A</code>&#8221; matches.</p>
<dt><code>TCL_REG_NOTEOL</code></p>
<dd>The last character in the string will not be treated as the end of a line or the end of the string, so &#8220;$&#8221; will not match there. Note that this flag has no effect on how &#8220;<code>\Z</code>&#8221; matches.</dl>
</dl>
<p> <code>Tcl_RegExpGetInfo</code> retrieves information about the last match performed with a given regular expression <i>regexp</i>. The <i>infoPtr</i> argument contains a pointer to a structure that is defined as follows: </p>
<dl COMPACT>
<dd>
<pre>typedef struct Tcl_RegExpInfo {
 int <i>nsubs</i>;
 Tcl_RegExpIndices *<i>matches</i>;
 long <i>extendStart</i>;
} Tcl_RegExpInfo;</pre>
</dl>
<p> The <i>nsubs</i> field contains a count of the number of parenthesized subexpressions within the regular expression. If the <code>TCL_REG_NOSUB</code> was used, then this value will be zero. The <i>matches</i> field points to an array of <i>nsubs</i>+1 values that indicate the bounds of each subexpression matched. The first element in the array refers to the range matched by the entire regular expression, and subsequent elements refer to the parenthesized subexpressions in the order that they appear in the pattern. Each element is a structure that is defined as follows: </p>
<dl COMPACT>
<dd>
<pre>typedef struct Tcl_RegExpIndices {
 long <i>start</i>;
 long <i>end</i>;
} Tcl_RegExpIndices;</pre>
</dl>
<p> The <i>start</i> and <i>end</i> values are Unicode character indices relative to the offset location within <i>objPtr</i> where matching began. The <i>start</i> index identifies the first character of the matched subexpression. The <i>end</i> index identifies the first character after the matched subexpression. If the subexpression matched the empty string, then <i>start</i> and <i>end</i> will be equal. If the subexpression did not participate in the match, then <i>start</i> and <i>end</i> will be set to -1. </p>
<p> The <i>extendStart</i> field in <code>Tcl_RegExpInfo</code> is only set if the <code>TCL_REG_CANMATCH</code> flag was used. It indicates the first character in the string where a match could occur. If a match was found, this will be the same as the beginning of the current match. If no match was found, then it indicates the earliest point at which a match might occur if additional text is appended to the string. If it is no match is possible even with further text, this field will be set to -1.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/n-re_syntax/">re_syntax</a>(n)</p>
<h2>Keywords</h2>
<p>match, pattern, regular expression, string, subexpression, Tcl_RegExpIndices, Tcl_RegExpInfo</p>
