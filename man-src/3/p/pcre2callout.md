---
title: "pcre2callout(3)"
name: "pcre2callout"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2callout/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int (*pcre2_callout)(pcre2_callout_block *, void *);

int pcre2_callout_enumerate(const pcre2_code *code,
                            int (*callback)(pcre2_callout_enumerate_block *, void *),
                            void *user_data);</code></pre>
<h2>Description</h2>
<p>PCRE2 provides a feature called &quot;callout&quot;, which is a means of temporarily passing control to the caller of PCRE2 in the middle of pattern matching. The caller of PCRE2 provides an external function by putting its entry point in a match context (see <code>pcre2_set_callout()</code> in the <code>pcre2api</code> documentation). When using the <code>pcre2_substitute()</code> function, an additional callout feature is available. This does a callout after each change to the subject string and is described in the <code>pcre2api</code> documentation; the rest of this document is concerned with callouts during pattern matching. Within a regular expression, (?C&lt;arg&gt;) indicates a point at which the external function is to be called. Different callout points can be identified by putting a number less than 256 after the letter C. The default value is zero. Alternatively, the argument may be a delimited string. The starting delimiter must be one of ` &#8216; &quot; ^ % # $ { and the ending delimiter is the same as the start, except for {, where the ending delimiter is }. If the ending delimiter is needed within the string, it must be doubled. For example, this pattern has two callout points:<br />
&nbsp;<wbr>&nbsp;(?C1)abc(?C&quot;some&nbsp;&quot;&quot;arbitrary&quot;&quot;&nbsp;text&quot;)def If the PCRE2_AUTO_CALLOUT option bit is set when a pattern is compiled, PCRE2 automatically inserts callouts, all with number 255, before each item in the pattern except for immediately before or after an explicit callout. For example, if PCRE2_AUTO_CALLOUT is used with the pattern<br />
&nbsp;<wbr>&nbsp;A(?C3)B it is processed as if it were<br />
&nbsp;<wbr>&nbsp;(?C255)A(?C3)B(?C255) Here is a more complicated example:<br />
&nbsp;<wbr>&nbsp;A(\d{2}|&#8211;) With PCRE2_AUTO_CALLOUT, this pattern is processed as if it were<br />
&nbsp;<wbr>&nbsp;(?C255)A(?C255)((?C255)\d{2}(?C255)|(?C255)-(?C255)-(?C255))(?C255) Notice that there is a callout before and after each parenthesis and alternation bar. If the pattern contains a conditional group whose condition is an assertion, an automatic callout is inserted immediately before the condition. Such a callout may also be inserted explicitly, for example: </p>
<pre><code>(?(?C9)(?=a)ab|de)  (?(?C%text%)(?!=d)ab|de)</code></pre>
<p> This applies only to assertion conditions (because they are themselves independent groups). Callouts can be useful for tracking the progress of pattern matching. The <code>pcre2test</code> program has a pattern qualifier (/auto_callout) that sets automatic callouts. When any callouts are present, the output from <code>pcre2test</code> indicates how the pattern is being matched. This is useful information when you are trying to optimize the performance of a particular pattern.</p>
<h2>Missing Callouts</h2>
<p>You should be aware that, because of optimizations in the way PCRE2 compiles and matches patterns, callouts sometimes do not happen exactly as you might expect.</p>
<h3>Auto-possessification</h3>
<p>At compile time, PCRE2 &quot;auto-possessifies&quot; repeated items when it knows that what follows cannot be part of the repeat. For example, a+[bc] is compiled as if it were a++[bc]. The <code>pcre2test</code> output when this pattern is compiled with PCRE2_ANCHORED and PCRE2_AUTO_CALLOUT and then applied to the string &quot;aaaa&quot; is: </p>
<p>&nbsp;<wbr>&nbsp;&#8212;&gt;aaaa<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+0&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a+<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+2&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[bc]<br />
&nbsp;<wbr>&nbsp;No match </p>
<p> This indicates that when matching [bc] fails, there is no backtracking into a+ (because it is being treated as a++) and therefore the callouts that would be taken for the backtracks do not occur. You can disable the auto-possessify feature by passing PCRE2_NO_AUTO_POSSESS to <code>pcre2_compile()</code>, or starting the pattern with (*NO_AUTO_POSSESS). In this case, the output changes to this: </p>
<p>&nbsp;<wbr>&nbsp;&#8212;&gt;aaaa<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+0&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a+<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+2&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[bc]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+2&nbsp;^&nbsp;<wbr>&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[bc]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+2&nbsp;^&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[bc]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+2&nbsp;^^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[bc]<br />
&nbsp;<wbr>&nbsp;No match </p>
<p> This time, when matching [bc] fails, the matcher backtracks into a+ and tries again, repeatedly, until a+ itself fails.</p>
<h3>Automatic .* anchoring</h3>
<p>By default, an optimization is applied when .* is the first significant item in a pattern. If PCRE2_DOTALL is set, so that the dot can match any character, the pattern is automatically anchored. If PCRE2_DOTALL is not set, a match can start only after an internal newline or at the beginning of the subject, and <code>pcre2_compile()</code> remembers this. If a pattern has more than one top-level branch, automatic anchoring occurs if all branches are anchorable. </p>
<p> This optimization is disabled, however, if .* is in an atomic group or if there is a backreference to the capture group in which it appears. It is also disabled if the pattern contains (*PRUNE) or (*SKIP). However, the presence of callouts does not affect it. </p>
<p> For example, if the pattern .*\d is compiled with PCRE2_AUTO_CALLOUT and applied to the string &quot;aa&quot;, the <code>pcre2test</code> output is: </p>
<p>&nbsp;<wbr>&nbsp;&#8212;&gt;aa<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+0&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+2&nbsp;^&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\d<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+2&nbsp;^^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\d<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+2&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\d<br />
&nbsp;<wbr>&nbsp;No match </p>
<p> This shows that all match attempts start at the beginning of the subject. In other words, the pattern is anchored. You can disable this optimization by passing PCRE2_NO_DOTSTAR_ANCHOR to <code>pcre2_compile()</code>, or starting the pattern with (*NO_DOTSTAR_ANCHOR). In this case, the output changes to: </p>
<p>&nbsp;<wbr>&nbsp;&#8212;&gt;aa<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+0&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+2&nbsp;^&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\d<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+2&nbsp;^^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\d<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+2&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\d<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+0&nbsp;<wbr>&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+2&nbsp;<wbr>&nbsp;^^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\d<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+2&nbsp;<wbr>&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\d<br />
&nbsp;<wbr>&nbsp;No match </p>
<p> This shows more match attempts, starting at the second subject character. Another optimization, described in the next section, means that there is no subsequent attempt to match with an empty subject.</p>
<h3>Other optimizations</h3>
<p>Other optimizations that provide fast &quot;no match&quot; results also affect callouts. For example, if the pattern is </p>
<p>&nbsp;<wbr>&nbsp;ab(?C4)cd </p>
<p> PCRE2 knows that any matching string must contain the letter &quot;d&quot;. If the subject string is &quot;abyz&quot;, the lack of &quot;d&quot; means that matching doesn&#8217;t ever start, and the callout is never reached. However, with &quot;abyd&quot;, though the result is still no match, the callout is obeyed. </p>
<p> For most patterns PCRE2 also knows the minimum length of a matching string, and will immediately give a &quot;no match&quot; return without actually running a match if the subject is not long enough, or, for unanchored patterns, if it has been scanned far enough. </p>
<p> You can disable these optimizations by passing the PCRE2_NO_START_OPTIMIZE option to <code>pcre2_compile()</code>, or by starting the pattern with (*NO_START_OPT). This slows down the matching process, but does ensure that callouts such as the example above are obeyed.</p>
<h2>The Callout Interface</h2>
<p>During matching, when PCRE2 reaches a callout point, if an external function is provided in the match context, it is called. This applies to both normal, DFA, and JIT matching. The first argument to the callout function is a pointer to a <code>pcre2_callout</code> block. The second argument is the void * callout data that was supplied when the callout was set up by calling <code>pcre2_set_callout()</code> (see the <code>pcre2api</code> documentation). The callout block structure contains the following fields, not necessarily in this order: </p>
<p>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>version</i>;<br />
&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>callout_number</i>;<br />
&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>capture_top</i>;<br />
&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>capture_last</i>;<br />
&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>callout_flags</i>;<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;*<i>offset_vector</i>;<br />
&nbsp;<wbr>&nbsp;PCRE2_SPTR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>mark</i>;<br />
&nbsp;<wbr>&nbsp;PCRE2_SPTR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>subject</i>;<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>subject_length</i>;<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>start_match</i>;<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>current_position</i>;<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>pattern_position</i>;<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>next_item_length</i>;<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>callout_string_offset</i>;<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>callout_string_length</i>;<br />
&nbsp;<wbr>&nbsp;PCRE2_SPTR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>callout_string</i>; </p>
<p> The <i>version</i> field contains the version number of the block format. The current version is 2; the three callout string fields were added for version 1, and the <i>callout_flags</i> field for version 2. If you are writing an application that might use an earlier release of PCRE2, you should check the version number before accessing any of these fields. The version number will increase in future if more fields are added, but the intention is never to remove any of the existing fields.</p>
<h3>Fields for numerical callouts</h3>
<p>For a numerical callout, <i>callout_string</i> is NULL, and <i>callout_number</i> contains the number of the callout, in the range 0-255. This is the number that follows (?C for callouts that part of the pattern; it is 255 for automatically generated callouts.</p>
<h3>Fields for string callouts</h3>
<p>For callouts with string arguments, <i>callout_number</i> is always zero, and <i>callout_string</i> points to the string that is contained within the compiled pattern. Its length is given by <i>callout_string_length</i>. Duplicated ending delimiters that were present in the original pattern string have been turned into single characters, but there is no other processing of the callout string argument. An additional code unit containing binary zero is present after the string, but is not included in the length. The delimiter that was used to start the string is also stored within the pattern, immediately before the string itself. You can access this delimiter as <i>callout_string</i>[-1] if you need it. </p>
<p> The <i>callout_string_offset</i> field is the code unit offset to the start of the callout argument string within the original pattern string. This is provided for the benefit of applications such as script languages that might need to report errors in the callout string within the pattern.</p>
<h3>Fields for all callouts</h3>
<p>The remaining fields in the callout block are the same for both kinds of callout. </p>
<p> The <i>offset_vector</i> field is a pointer to a vector of capturing offsets (the &quot;ovector&quot;). You may read the elements in this vector, but you must not change any of them. </p>
<p> For calls to <code>pcre2_match()</code>, the <i>offset_vector</i> field is not (since release 10.30) a pointer to the actual ovector that was passed to the matching function in the match data block. Instead it points to an internal ovector of a size large enough to hold all possible captured substrings in the pattern. Note that whenever a recursion or subroutine call within a pattern completes, the capturing state is reset to what it was before. </p>
<p> The <i>capture_last</i> field contains the number of the most recently captured substring, and the <i>capture_top</i> field contains one more than the number of the highest numbered captured substring so far. If no substrings have yet been captured, the value of <i>capture_last</i> is 0 and the value of <i>capture_top</i> is 1. The values of these fields do not always differ by one; for example, when the callout in the pattern ((a)(b))(?C2) is taken, <i>capture_last</i> is 1 but <i>capture_top</i> is 4. </p>
<p> The contents of ovector[2] to ovector[&lt;capture_top&gt;*2-1] can be inspected in order to extract substrings that have been matched so far, in the same way as extracting substrings after a match has completed. The values in ovector[0] and ovector[1] are always PCRE2_UNSET because the match is by definition not complete. Substrings that have not been captured but whose numbers are less than <i>capture_top</i> also have both of their ovector slots set to PCRE2_UNSET. </p>
<p> For DFA matching, the <i>offset_vector</i> field points to the ovector that was passed to the matching function in the match data block for callouts at the top level, but to an internal ovector during the processing of pattern recursions, lookarounds, and atomic groups. However, these ovectors hold no useful information because <code>pcre2_dfa_match()</code> does not support substring capturing. The value of <i>capture_top</i> is always 1 and the value of <i>capture_last</i> is always 0 for DFA matching. </p>
<p> The <i>subject</i> and <i>subject_length</i> fields contain copies of the values that were passed to the matching function. </p>
<p> The <i>start_match</i> field normally contains the offset within the subject at which the current match attempt started. However, if the escape sequence \K has been encountered, this value is changed to reflect the modified starting point. If the pattern is not anchored, the callout function may be called several times from the same point in the pattern for different starting points in the subject. </p>
<p> The <i>current_position</i> field contains the offset within the subject of the current match pointer. </p>
<p> The <i>pattern_position</i> field contains the offset in the pattern string to the next item to be matched. </p>
<p> The <i>next_item_length</i> field contains the length of the next item to be processed in the pattern string. When the callout is at the end of the pattern, the length is zero. When the callout precedes an opening parenthesis, the length includes meta characters that follow the parenthesis. For example, in a callout before an assertion such as (?=ab) the length is 3. For an an alternation bar or a closing parenthesis, the length is one, unless a closing parenthesis is followed by a quantifier, in which case its length is included. (This changed in release 10.23. In earlier releases, before an opening parenthesis the length was that of the entire group, and before an alternation bar or a closing parenthesis the length was zero.) </p>
<p> The <i>pattern_position</i> and <i>next_item_length</i> fields are intended to help in distinguishing between different automatic callouts, which all have the same callout number. However, they are set for all callouts, and are used by <code>pcre2test</code> to show the next item to be matched when displaying callout information. </p>
<p> In callouts from <code>pcre2_match()</code> the <i>mark</i> field contains a pointer to the zero-terminated name of the most recently passed (*MARK), (*PRUNE), or (*THEN) item in the match, or NULL if no such items have been passed. Instances of (*PRUNE) or (*THEN) without a name do not obliterate a previous (*MARK). In callouts from the DFA matching function this field always contains NULL. </p>
<p> The <i>callout_flags</i> field is always zero in callouts from <code>pcre2_dfa_match()</code> or when JIT is being used. When <code>pcre2_match()</code> without JIT is used, the following bits may be set: </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CALLOUT_STARTMATCH </p>
<p> This is set for the first callout after the start of matching for each new starting position in the subject. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CALLOUT_BACKTRACK </p>
<p> This is set if there has been a matching backtrack since the previous callout, or since the start of matching if this is the first callout from a <code>pcre2_match()</code> run. </p>
<p> Both bits are set when a backtrack has caused a &quot;bumpalong&quot; to a new starting position in the subject. Output from <code>pcre2test</code> does not indicate the presence of these bits unless the <code>callout_extra</code> modifier is set. </p>
<p> The information in the <code>callout_flags</code> field is provided so that applications can track and tell their users how matching with backtracking is done. This can be useful when trying to optimize patterns, or just to understand how PCRE2 works. There is no support in <code>pcre2_dfa_match()</code> because there is no backtracking in DFA matching, and there is no support in JIT because JIT is all about maximimizing matching performance. In both these cases the <code>callout_flags</code> field is always zero.</p>
<h2>Return Values From Callouts</h2>
<p>The external callout function returns an integer to PCRE2. If the value is zero, matching proceeds as normal. If the value is greater than zero, matching fails at the current point, but the testing of other matching possibilities goes ahead, just as if a lookahead assertion had failed. If the value is less than zero, the match is abandoned, and the matching function returns the negative value. </p>
<p> Negative values should normally be chosen from the set of PCRE2_ERROR_xxx values. In particular, PCRE2_ERROR_NOMATCH forces a standard &quot;no match&quot; failure. The error number PCRE2_ERROR_CALLOUT is reserved for use by callout functions; it will never be used by PCRE2 itself.</p>
<h2>Callout Enumeration</h2>
<pre><code>int pcre2_callout_enumerate(const pcre2_code *</code><i>code</i>,
<code> int (*</code><i>callback</i>)(pcre2_callout_enumerate_block *, void *),
<code> void *</code><i>user_data</i>);</pre>
<p>A script language that supports the use of string arguments in callouts might like to scan all the callouts in a pattern before running the match. This can be done by calling <code>pcre2_callout_enumerate()</code>. The first argument is a pointer to a compiled pattern, the second points to a callback function, and the third is arbitrary user data. The callback function is called for every callout in the pattern in the order in which they appear. Its first argument is a pointer to a callout enumeration block, and its second argument is the <i>user_data</i> value that was passed to <code>pcre2_callout_enumerate()</code>. The data block contains the following fields: </p>
<p>&nbsp;<wbr>&nbsp;<i>version</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Block version number<br />
&nbsp;<wbr>&nbsp;<i>pattern_position</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Offset to next item in pattern<br />
&nbsp;<wbr>&nbsp;<i>next_item_length</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Length of next item in pattern<br />
&nbsp;<wbr>&nbsp;<i>callout_number</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Number for numbered callouts<br />
&nbsp;<wbr>&nbsp;<i>callout_string_offset</i>&nbsp;<wbr>&nbsp;Offset to string within pattern<br />
&nbsp;<wbr>&nbsp;<i>callout_string_length</i>&nbsp;<wbr>&nbsp;Length of callout string<br />
&nbsp;<wbr>&nbsp;<i>callout_string</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to callout string or is NULL </p>
<p> The version number is currently 0. It will increase if new fields are ever added to the block. The remaining fields are the same as their namesakes in the <code>pcre2_callout</code> block that is used for callouts during matching, as described above. </p>
<p> Note that the value of <i>pattern_position</i> is unique for each callout. However, if a callout occurs inside a group that is quantified with a non-zero minimum or a fixed maximum, the group is replicated inside the compiled pattern. For example, a pattern such as /(a){2}/ is compiled as if it were /(a)(a)/. This means that the callout will be enumerated more than once, but with the same value for <i>pattern_position</i> in each case. </p>
<p> The callback function should normally return zero. If it returns a non-zero value, scanning the pattern stops, and that value is returned from <code>pcre2_callout_enumerate()</code>.</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 03 February 2019
Copyright (c) 1997-2019 University of Cambridge.</pre>
