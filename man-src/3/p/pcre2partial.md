---
title: "pcre2partial(3)"
name: "pcre2partial"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2partial/"
description: "PCRE2 – Perl-compatible regular expressions"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions</p>
<h2>Partial Matching In Pcre2</h2>
<p>In normal use of PCRE2, if there is a match up to the end of a subject string, but more characters are needed to match the entire pattern, PCRE2_ERROR_NOMATCH is returned, just like any other failing match. There are circumstances where it might be helpful to distinguish this &quot;partial match&quot; case. </p>
<p> One example is an application where the subject string is very long, and not all available at once. The requirement here is to be able to do the matching segment by segment, but special action is needed when a matched substring spans the boundary between two segments. </p>
<p> Another example is checking a user input string as it is typed, to ensure that it conforms to a required format. Invalid characters can be immediately diagnosed and rejected, giving instant feedback. </p>
<p> Partial matching is a PCRE2-specific feature; it is not Perl-compatible. It is requested by setting one of the PCRE2_PARTIAL_HARD or PCRE2_PARTIAL_SOFT options when calling a matching function. The difference between the two options is whether or not a partial match is preferred to an alternative complete match, though the details differ between the two types of matching function. If both options are set, PCRE2_PARTIAL_HARD takes precedence. </p>
<p> If you want to use partial matching with just-in-time optimized code, as well as setting a partial match option for the matching function, you must also call <code>pcre2_jit_compile()</code> with one or both of these options: </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_JIT_PARTIAL_HARD<br />
&nbsp;<wbr>&nbsp;PCRE2_JIT_PARTIAL_SOFT </p>
<p> PCRE2_JIT_COMPLETE should also be set if you are going to run non-partial matches on the same pattern. Separate code is compiled for each mode. If the appropriate JIT mode has not been compiled, interpretive matching code is used. </p>
<p> Setting a partial matching option disables two of PCRE2&#8217;s standard optimization hints. PCRE2 remembers the last literal code unit in a pattern, and abandons matching immediately if it is not present in the subject string. This optimization cannot be used for a subject string that might match only partially. PCRE2 also remembers a minimum length of a matching string, and does not bother to run the matching function on shorter strings. This optimization is also disabled for partial matching.</p>
<h2>Requirements For A Partial Match</h2>
<p>A possible partial match occurs during matching when the end of the subject string is reached successfully, but either more characters are needed to complete the match, or the addition of more characters might change what is matched. </p>
<p> Example 1: if the pattern is /abc/ and the subject is &quot;ab&quot;, more characters are definitely needed to complete a match. In this case both hard and soft matching options yield a partial match. </p>
<p> Example 2: if the pattern is /ab+/ and the subject is &quot;ab&quot;, a complete match can be found, but the addition of more characters might change what is matched. In this case, only PCRE2_PARTIAL_HARD returns a partial match; PCRE2_PARTIAL_SOFT returns the complete match. </p>
<p> On reaching the end of the subject, when PCRE2_PARTIAL_HARD is set, if the next pattern item is \z, \Z, , \B, or $ there is always a partial match. Otherwise, for both options, the next pattern item must be one that inspects a character, and at least one of the following must be true: </p>
<p> (1) At least one character has already been inspected. An inspected character need not form part of the final matched string; lookbehind assertions and the \K escape sequence provide ways of inspecting characters before the start of a matched string. </p>
<p> (2) The pattern contains one or more lookbehind assertions. This condition exists in case there is a lookbehind that inspects characters before the start of the match. </p>
<p> (3) There is a special case when the whole pattern can match an empty string. When the starting point is at the end of the subject, the empty string match is a possibility, and if PCRE2_PARTIAL_SOFT is set and neither of the above conditions is true, it is returned. However, because adding more characters might result in a non-empty match, PCRE2_PARTIAL_HARD returns a partial match, which in this case means &quot;there is going to be a match at this point, but until some more characters are added, we do not know if it will be an empty string or something longer&quot;.</p>
<h2>PARTIAL MATCHING USING pcre2_match()</h2>
<p>When a partial matching option is set, the result of calling <code>pcre2_match()</code> can be one of the following:</p>
<dl>
<dt><code>A successful match</code></p>
<dd>A complete match has been found, starting and ending within this subject.</p>
<dt><code>PCRE2_ERROR_NOMATCH</code></p>
<dd>No match can start anywhere in this subject.</p>
<dt><code>PCRE2_ERROR_PARTIAL</code></p>
<dd>Adding more characters may result in a complete match that uses one or more characters from the end of this subject.</dl>
<p> When a partial match is returned, the first two elements in the ovector point to the portion of the subject that was matched, but the values in the rest of the ovector are undefined. The appearance of \K in the pattern has no effect for a partial match. Consider this pattern: </p>
<p>&nbsp;<wbr>&nbsp;/abc\K123/ </p>
<p> If it is matched against &quot;456abc123xyz&quot; the result is a complete match, and the ovector defines the matched string as &quot;123&quot;, because \K resets the &quot;start of match&quot; point. However, if a partial match is requested and the subject string is &quot;456abc12&quot;, a partial match is found for the string &quot;abc12&quot;, because all these characters are needed for a subsequent re-match with additional characters. </p>
<p> If there is more than one partial match, the first one that was found provides the data that is returned. Consider this pattern: </p>
<p>&nbsp;<wbr>&nbsp;/123\w+X|dogY/ </p>
<p> If this is matched against the subject string &quot;abc123dog&quot;, both alternatives fail to match, but the end of the subject is reached during matching, so PCRE2_ERROR_PARTIAL is returned. The offsets are set to 3 and 9, identifying &quot;123dog&quot; as the first partial match. (In this example, there are two partial matches, because &quot;dog&quot; on its own partially matches the second alternative.)</p>
<h3>How a partial match is processed by pcre2_match()</h3>
<p>What happens when a partial match is identified depends on which of the two partial matching options is set. </p>
<p> If PCRE2_PARTIAL_HARD is set, PCRE2_ERROR_PARTIAL is returned as soon as a partial match is found, without continuing to search for possible complete matches. This option is &quot;hard&quot; because it prefers an earlier partial match over a later complete match. For this reason, the assumption is made that the end of the supplied subject string is not the true end of the available data, which is why \z, \Z, , \B, and $ always give a partial match. </p>
<p> If PCRE2_PARTIAL_SOFT is set, the partial match is remembered, but matching continues as normal, and other alternatives in the pattern are tried. If no complete match can be found, PCRE2_ERROR_PARTIAL is returned instead of PCRE2_ERROR_NOMATCH. This option is &quot;soft&quot; because it prefers a complete match over a partial match. All the various matching items in a pattern behave as if the subject string is potentially complete; \z, \Z, and $ match at the end of the subject, as normal, and for  and \B the end of the subject is treated as a non-alphanumeric. </p>
<p> The difference between the two partial matching options can be illustrated by a pattern such as: </p>
<p>&nbsp;<wbr>&nbsp;/dog(sbody)?/ </p>
<p> This matches either &quot;dog&quot; or &quot;dogsbody&quot;, greedily (that is, it prefers the longer string if possible). If it is matched against the string &quot;dog&quot; with PCRE2_PARTIAL_SOFT, it yields a complete match for &quot;dog&quot;. However, if PCRE2_PARTIAL_HARD is set, the result is PCRE2_ERROR_PARTIAL. On the other hand, if the pattern is made ungreedy the result is different: </p>
<p>&nbsp;<wbr>&nbsp;/dog(sbody)??/ </p>
<p> In this case the result is always a complete match because that is found first, and matching never continues after finding a complete match. It might be easier to follow this explanation by thinking of the two patterns like this: </p>
<p>&nbsp;<wbr>&nbsp;/dog(sbody)?/&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;is the same as&nbsp;<wbr>&nbsp;/dogsbody|dog/<br />
&nbsp;<wbr>&nbsp;/dog(sbody)??/&nbsp;<wbr>&nbsp;<wbr>&nbsp;is the same as&nbsp;<wbr>&nbsp;/dog|dogsbody/ </p>
<p> The second pattern will never match &quot;dogsbody&quot;, because it will always find the shorter match first.</p>
<h3>Example of partial matching using pcre2test</h3>
<p>The <code>pcre2test</code> data modifiers <code>partial_hard</code> (or <code>ph</code>) and <code>partial_soft</code> (or <code>ps</code>) set PCRE2_PARTIAL_HARD and PCRE2_PARTIAL_SOFT, respectively, when calling <code>pcre2_match()</code>. Here is a run of <code>pcre2test</code> using a pattern that matches the whole subject in the form of a date: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;re&gt;&nbsp;/^\d?\d(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\d\d$/<br />
&nbsp;<wbr>&nbsp;data&gt;&nbsp;25dec3\=ph<br />
&nbsp;<wbr>&nbsp;Partial match: 23dec3<br />
&nbsp;<wbr>&nbsp;data&gt;&nbsp;3ju\=ph<br />
&nbsp;<wbr>&nbsp;Partial match: 3ju<br />
&nbsp;<wbr>&nbsp;data&gt;&nbsp;3juj\=ph<br />
&nbsp;<wbr>&nbsp;No match </p>
<p> This example gives the same results for both hard and soft partial matching options. Here is an example where there is a difference: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;re&gt;&nbsp;/^\d?\d(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\d\d$/<br />
&nbsp;<wbr>&nbsp;data&gt;&nbsp;25jun04\=ps<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;0: 25jun04<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;1: jun<br />
&nbsp;<wbr>&nbsp;data&gt;&nbsp;25jun04\=ph<br />
&nbsp;<wbr>&nbsp;Partial match: 25jun04 </p>
<p> With PCRE2_PARTIAL_SOFT, the subject is matched completely. For PCRE2_PARTIAL_HARD, however, the subject is assumed not to be complete, so there is only a partial match.</p>
<h2>MULTI-SEGMENT MATCHING WITH pcre2_match()</h2>
<p>PCRE was not originally designed with multi-segment matching in mind. However, over time, features (including partial matching) that make multi-segment matching possible have been added. A very long string can be searched segment by segment by calling <code>pcre2_match()</code> repeatedly, with the aim of achieving the same results that would happen if the entire string was available for searching all the time. Normally, the strings that are being sought are much shorter than each individual segment, and are in the middle of very long strings, so the pattern is normally not anchored. </p>
<p> Special logic must be implemented to handle a matched substring that spans a segment boundary. PCRE2_PARTIAL_HARD should be used, because it returns a partial match at the end of a segment whenever there is the possibility of changing the match by adding more characters. The PCRE2_NOTBOL option should also be set for all but the first segment. </p>
<p> When a partial match occurs, the next segment must be added to the current subject and the match re-run, using the <i>startoffset</i> argument of <code>pcre2_match()</code> to begin at the point where the partial match started. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;re&gt;&nbsp;/\d?\d(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\d\d/<br />
&nbsp;<wbr>&nbsp;data&gt;&nbsp;&#8230;the date is 23ja\=ph<br />
&nbsp;<wbr>&nbsp;Partial match: 23ja<br />
&nbsp;<wbr>&nbsp;data&gt;&nbsp;&#8230;the date is 23jan19 and on that day&#8230;\=offset=15<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;0: 23jan19<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;1: jan </p>
<p> Note the use of the <code>offset</code> modifier to start the new match where the partial match was found. In this example, the next segment was added to the one in which the partial match was found. This is the most straightforward approach, typically using a memory buffer that is twice the size of each segment. After a partial match, the first half of the buffer is discarded, the second half is moved to the start of the buffer, and a new segment is added before repeating the match as in the example above. After a no match, the entire buffer can be discarded. </p>
<p> If there are memory constraints, you may want to discard text that precedes a partial match before adding the next segment. Unfortunately, this is not at present straightforward. In cases such as the above, where the pattern does not contain any lookbehinds, it is sufficient to retain only the partially matched substring. However, if the pattern contains a lookbehind assertion, characters that precede the start of the partial match may have been inspected during the matching process. When <code>pcre2test</code> displays a partial match, it indicates these characters with &#8216;&lt;&#8216; if the <code>allusedtext</code> modifier is set: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;re&gt;&nbsp;&quot;(?&lt;=123)abc&quot;<br />
&nbsp;<wbr>&nbsp;data&gt;&nbsp;xx123ab\=ph,allusedtext<br />
&nbsp;<wbr>&nbsp;Partial match: 123ab<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&lt;&lt; </p>
<p> However, the allusedtext modifier is not available for JIT matching, because JIT matching does not record the first (or last) consulted characters. For this reason, this information is not available via the API. It is therefore not possible in general to obtain the exact number of characters that must be retained in order to get the right match result. If you cannot retain the entire segment, you must find some heuristic way of choosing. </p>
<p> If you know the approximate length of the matching substrings, you can use that to decide how much text to retain. The only lookbehind information that is currently available via the API is the length of the longest individual lookbehind in a pattern, but this can be misleading if there are nested lookbehinds. The value returned by calling <code>pcre2_pattern_info()</code> with the PCRE2_INFO_MAXLOOKBEHIND option is the maximum number of characters (not code units) that any individual lookbehind moves back when it is processed. A pattern such as &quot;(?&lt;=(?&lt;!b)a)&quot; has a maximum lookbehind value of one, but inspects two characters before its starting point. </p>
<p> In a non-UTF or a 32-bit case, moving back is just a subtraction, but in UTF-8 or UTF-16 you have to count characters while moving back through the code units.</p>
<h2>PARTIAL MATCHING USING pcre2_dfa_match()</h2>
<p>The DFA function moves along the subject string character by character, without backtracking, searching for all possible matches simultaneously. If the end of the subject is reached before the end of the pattern, there is the possibility of a partial match. </p>
<p> When PCRE2_PARTIAL_SOFT is set, PCRE2_ERROR_PARTIAL is returned only if there have been no complete matches. Otherwise, the complete matches are returned. If PCRE2_PARTIAL_HARD is set, a partial match takes precedence over any complete matches. The portion of the string that was matched when the longest partial match was found is set as the first matching string. </p>
<p> Because the DFA function always searches for all possible matches, and there is no difference between greedy and ungreedy repetition, its behaviour is different from the <code>pcre2_match()</code>. Consider the string &quot;dog&quot; matched against this ungreedy pattern: </p>
<p>&nbsp;<wbr>&nbsp;/dog(sbody)??/ </p>
<p> Whereas the standard function stops as soon as it finds the complete match for &quot;dog&quot;, the DFA function also finds the partial match for &quot;dogsbody&quot;, and so returns that when PCRE2_PARTIAL_HARD is set.</p>
<h2>MULTI-SEGMENT MATCHING WITH pcre2_dfa_match()</h2>
<p>When a partial match has been found using the DFA matching function, it is possible to continue the match by providing additional subject data and calling the function again with the same compiled regular expression, this time setting the PCRE2_DFA_RESTART option. You must pass the same working space as before, because this is where details of the previous partial match are stored. You can set the PCRE2_PARTIAL_SOFT or PCRE2_PARTIAL_HARD options with PCRE2_DFA_RESTART to continue partial matching over multiple segments. Here is an example using <code>pcre2test</code>: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;re&gt;&nbsp;/^\d?\d(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\d\d$/<br />
&nbsp;<wbr>&nbsp;data&gt;&nbsp;23ja\=dfa,ps<br />
&nbsp;<wbr>&nbsp;Partial match: 23ja<br />
&nbsp;<wbr>&nbsp;data&gt;&nbsp;n05\=dfa,dfa_restart<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;0: n05 </p>
<p> The first call has &quot;23ja&quot; as the subject, and requests partial matching; the second call has &quot;n05&quot; as the subject for the continued (restarted) match. Notice that when the match is complete, only the last part is shown; PCRE2 does not retain the previously partially-matched string. It is up to the calling program to do that if it needs to. This means that, for an unanchored pattern, if a continued match fails, it is not possible to try again at a new starting point. All this facility is capable of doing is continuing with the previous match attempt. For example, consider this pattern: </p>
<p>&nbsp;<wbr>&nbsp;1234|3789 </p>
<p> If the first part of the subject is &quot;ABC123&quot;, a partial match of the first alternative is found at offset 3. There is no partial match for the second alternative, because such a match does not start at the same point in the subject string. Attempting to continue with the string &quot;7890&quot; does not yield a match because only those alternatives that match at one point in the subject are remembered. Depending on the application, this may or may not be what you want. </p>
<p> If you do want to allow for starting again at the next character, one way of doing it is to retain some or all of the segment and try a new complete match, as described for <code>pcre2_match()</code> above. Another possibility is to work with two buffers. If a partial match at offset <i>n</i> in the first buffer is followed by &quot;no match&quot; when PCRE2_DFA_RESTART is used on the second buffer, you can then try a new match starting at offset <i>n+1</i> in the first buffer.</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 04 September 2019
Copyright (c) 1997-2019 University of Cambridge.</pre>
