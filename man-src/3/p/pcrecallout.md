---
title: "pcrecallout(3)"
name: "pcrecallout"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcrecallout/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
int (*pcre_callout)(pcre_callout_block *);
int (*pcre16_callout)(pcre16_callout_block *);
int (*pcre32_callout)(pcre32_callout_block *);</code></pre>
<h2>Description</h2>
<p>PCRE provides a feature called &quot;callout&quot;, which is a means of temporarily passing control to the caller of PCRE in the middle of pattern matching. The caller of PCRE provides an external function by putting its entry point in the global variable <i>pcre_callout</i> (<i>pcre16_callout</i> for the 16-bit library, <i>pcre32_callout</i> for the 32-bit library). By default, this variable contains NULL, which disables all calling out. Within a regular expression, (?C) indicates the points at which the external function is to be called. Different callout points can be identified by putting a number less than 256 after the letter C. The default value is zero. For example, this pattern has two callout points:<br />
&nbsp;<wbr>&nbsp;(?C1)abc(?C2)def If the PCRE_AUTO_CALLOUT option bit is set when a pattern is compiled, PCRE automatically inserts callouts, all with number 255, before each item in the pattern. For example, if PCRE_AUTO_CALLOUT is used with the pattern<br />
&nbsp;<wbr>&nbsp;A(\d{2}|&#8211;) it is processed as if it were (?C255)A(?C255)((?C255)\d{2}(?C255)|(?C255)-(?C255)-(?C255))(?C255) Notice that there is a callout before and after each parenthesis and alternation bar. If the pattern contains a conditional group whose condition is an assertion, an automatic callout is inserted immediately before the condition. Such a callout may also be inserted explicitly, for example: </p>
<pre><code>(?(?C9)(?=a)ab|de)</code></pre>
<p> This applies only to assertion conditions (because they are themselves independent groups). Automatic callouts can be used for tracking the progress of pattern matching. The <code>pcretest</code> program has a pattern qualifier (/C) that sets automatic callouts; when it is used, the output indicates how the pattern is being matched. This is useful information when you are trying to optimize the performance of a particular pattern.</p>
<h2>Missing Callouts</h2>
<p>You should be aware that, because of optimizations in the way PCRE compiles and matches patterns, callouts sometimes do not happen exactly as you might expect. </p>
<p> At compile time, PCRE &quot;auto-possessifies&quot; repeated items when it knows that what follows cannot be part of the repeat. For example, a+[bc] is compiled as if it were a++[bc]. The <code>pcretest</code> output when this pattern is anchored and then applied with automatic callouts to the string &quot;aaaa&quot; is: </p>
<p>&nbsp;<wbr>&nbsp;&#8212;&gt;aaaa<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+0&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;^<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+1&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a+<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+3&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[bc]<br />
&nbsp;<wbr>&nbsp;No match </p>
<p> This indicates that when matching [bc] fails, there is no backtracking into a+ and therefore the callouts that would be taken for the backtracks do not occur. You can disable the auto-possessify feature by passing PCRE_NO_AUTO_POSSESS to <code>pcre_compile()</code>, or starting the pattern with (*NO_AUTO_POSSESS). If this is done in <code>pcretest</code> (using the /O qualifier), the output changes to this: </p>
<p>&nbsp;<wbr>&nbsp;&#8212;&gt;aaaa<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+0&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;^<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+1&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a+<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+3&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[bc]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+3&nbsp;^&nbsp;<wbr>&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[bc]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+3&nbsp;^&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[bc]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;+3&nbsp;^^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[bc]<br />
&nbsp;<wbr>&nbsp;No match </p>
<p> This time, when matching [bc] fails, the matcher backtracks into a+ and tries again, repeatedly, until a+ itself fails. </p>
<p> Other optimizations that provide fast &quot;no match&quot; results also affect callouts. For example, if the pattern is </p>
<p>&nbsp;<wbr>&nbsp;ab(?C4)cd </p>
<p> PCRE knows that any matching string must contain the letter &quot;d&quot;. If the subject string is &quot;abyz&quot;, the lack of &quot;d&quot; means that matching doesn&#8217;t ever start, and the callout is never reached. However, with &quot;abyd&quot;, though the result is still no match, the callout is obeyed. </p>
<p> If the pattern is studied, PCRE knows the minimum length of a matching string, and will immediately give a &quot;no match&quot; return without actually running a match if the subject is not long enough, or, for unanchored patterns, if it has been scanned far enough. </p>
<p> You can disable these optimizations by passing the PCRE_NO_START_OPTIMIZE option to the matching function, or by starting the pattern with (*NO_START_OPT). This slows down the matching process, but does ensure that callouts such as the example above are obeyed.</p>
<h2>The Callout Interface</h2>
<p>During matching, when PCRE reaches a callout point, the external function defined by <i>pcre_callout</i> or <i>pcre[16|32]_callout</i> is called (if it is set). This applies to both normal and DFA matching. The only argument to the callout function is a pointer to a <code>pcre_callout</code> or <code>pcre[16|32]_callout</code> block. These structures contains the following fields: </p>
<p>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>version</i>;<br />
&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>callout_number</i>;<br />
&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*<i>offset_vector</i>;<br />
&nbsp;<wbr>&nbsp;const char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*<i>subject</i>;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(8-bit version)<br />
&nbsp;<wbr>&nbsp;PCRE_SPTR16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>subject</i>;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(16-bit version)<br />
&nbsp;<wbr>&nbsp;PCRE_SPTR32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>subject</i>;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(32-bit version)<br />
&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>subject_length</i>;<br />
&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>start_match</i>;<br />
&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>current_position</i>;<br />
&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>capture_top</i>;<br />
&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>capture_last</i>;<br />
&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*<i>callout_data</i>;<br />
&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>pattern_position</i>;<br />
&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>next_item_length</i>;<br />
&nbsp;<wbr>&nbsp;const unsigned char&nbsp;*<i>mark</i>;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(8-bit version)<br />
&nbsp;<wbr>&nbsp;const PCRE_UCHAR16&nbsp;<wbr>&nbsp;*<i>mark</i>;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(16-bit version)<br />
&nbsp;<wbr>&nbsp;const PCRE_UCHAR32&nbsp;<wbr>&nbsp;*<i>mark</i>;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(32-bit version) </p>
<p> The <i>version</i> field is an integer containing the version number of the block format. The initial version was 0; the current version is 2. The version number will change again in future if additional fields are added, but the intention is never to remove any of the existing fields. </p>
<p> The <i>callout_number</i> field contains the number of the callout, as compiled into the pattern (that is, the number after ?C for manual callouts, and 255 for automatically generated callouts). </p>
<p> The <i>offset_vector</i> field is a pointer to the vector of offsets that was passed by the caller to the matching function. When <code>pcre_exec()</code> or <code>pcre[16|32]_exec()</code> is used, the contents can be inspected, in order to extract substrings that have been matched so far, in the same way as for extracting substrings after a match has completed. For the DFA matching functions, this field is not useful. </p>
<p> The <i>subject</i> and <i>subject_length</i> fields contain copies of the values that were passed to the matching function. </p>
<p> The <i>start_match</i> field normally contains the offset within the subject at which the current match attempt started. However, if the escape sequence \K has been encountered, this value is changed to reflect the modified starting point. If the pattern is not anchored, the callout function may be called several times from the same point in the pattern for different starting points in the subject. </p>
<p> The <i>current_position</i> field contains the offset within the subject of the current match pointer. </p>
<p> When the <code>pcre_exec()</code> or <code>pcre[16|32]_exec()</code> is used, the <i>capture_top</i> field contains one more than the number of the highest numbered captured substring so far. If no substrings have been captured, the value of <i>capture_top</i> is one. This is always the case when the DFA functions are used, because they do not support captured substrings. </p>
<p> The <i>capture_last</i> field contains the number of the most recently captured substring. However, when a recursion exits, the value reverts to what it was outside the recursion, as do the values of all captured substrings. If no substrings have been captured, the value of <i>capture_last</i> is -1. This is always the case for the DFA matching functions. </p>
<p> The <i>callout_data</i> field contains a value that is passed to a matching function specifically so that it can be passed back in callouts. It is passed in the <i>callout_data</i> field of a <code>pcre_extra</code> or <code>pcre[16|32]_extra</code> data structure. If no such data was passed, the value of <i>callout_data</i> in a callout block is NULL. There is a description of the <code>pcre_extra</code> structure in the <code>pcreapi</code> documentation. </p>
<p> The <i>pattern_position</i> field is present from version 1 of the callout structure. It contains the offset to the next item to be matched in the pattern string. </p>
<p> The <i>next_item_length</i> field is present from version 1 of the callout structure. It contains the length of the next item to be matched in the pattern string. When the callout immediately precedes an alternation bar, a closing parenthesis, or the end of the pattern, the length is zero. When the callout precedes an opening parenthesis, the length is that of the entire subpattern. </p>
<p> The <i>pattern_position</i> and <i>next_item_length</i> fields are intended to help in distinguishing between different automatic callouts, which all have the same callout number. However, they are set for all callouts. </p>
<p> The <i>mark</i> field is present from version 2 of the callout structure. In callouts from <code>pcre_exec()</code> or <code>pcre[16|32]_exec()</code> it contains a pointer to the zero-terminated name of the most recently passed (*MARK), (*PRUNE), or (*THEN) item in the match, or NULL if no such items have been passed. Instances of (*PRUNE) or (*THEN) without a name do not obliterate a previous (*MARK). In callouts from the DFA matching functions this field always contains NULL.</p>
<h2>Return Values</h2>
<p>The external callout function returns an integer to PCRE. If the value is zero, matching proceeds as normal. If the value is greater than zero, matching fails at the current point, but the testing of other matching possibilities goes ahead, just as if a lookahead assertion had failed. If the value is less than zero, the match is abandoned, the matching function returns the negative value. </p>
<p> Negative values should normally be chosen from the set of PCRE_ERROR_xxx values. In particular, PCRE_ERROR_NOMATCH forces a standard &quot;no match&quot; failure. The error number PCRE_ERROR_CALLOUT is reserved for use by callout functions; it will never be used by PCRE itself.</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge CB2 3QH, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 12 November 2013
Copyright (c) 1997-2013 University of Cambridge.</pre>
