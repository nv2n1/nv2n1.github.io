---
title: "pcre2_dfa_match(3)"
name: "pcre2_dfa_match"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_dfa_match/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_dfa_match(const pcre2_code *code, PCRE2_SPTR subject,
                    PCRE2_SIZE length, PCRE2_SIZE startoffset,
                    uint32_t options, pcre2_match_data *match_data,
                    pcre2_match_context *mcontext,
                    int *workspace, PCRE2_SIZE wscount);</code></pre>
<h2>Description</h2>
<p>This function matches a compiled regular expression against a given subject string, using an alternative matching algorithm that scans the subject string just once (except when processing lookaround assertions). This function is <i>not</i> Perl-compatible (the Perl-compatible matching function is <code>pcre2_match()</code>). The arguments for this function are:<br />
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to the compiled pattern<br />
&nbsp;<wbr>&nbsp;<i>subject</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to the subject string<br />
&nbsp;<wbr>&nbsp;<i>length</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Length of the subject string<br />
&nbsp;<wbr>&nbsp;<i>startoffset</i>&nbsp;<wbr>&nbsp;Offset in the subject at which to start matching<br />
&nbsp;<wbr>&nbsp;<i>options</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Option bits<br />
&nbsp;<wbr>&nbsp;<i>match_data</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to a match data block, for results<br />
&nbsp;<wbr>&nbsp;<i>mcontext</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to a match context, or is NULL<br />
&nbsp;<wbr>&nbsp;<i>workspace</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to a vector of ints used as working space<br />
&nbsp;<wbr>&nbsp;<i>wscount</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Number of elements in the vector For <code>pcre2_dfa_match()</code>, a match context is needed only if you want to set up a callout function or specify the heap limit or the match or the recursion depth limits. The <i>length</i> and <i>startoffset</i> values are code units, not characters. The options are:<br />
&nbsp;<wbr>&nbsp;PCRE2_ANCHORED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Match only at the first position<br />
&nbsp;<wbr>&nbsp;PCRE2_COPY_MATCHED_SUBJECT<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;On success, make a private subject copy<br />
&nbsp;<wbr>&nbsp;PCRE2_ENDANCHORED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pattern can match only at end of subject<br />
&nbsp;<wbr>&nbsp;PCRE2_NOTBOL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Subject is not the beginning of a line<br />
&nbsp;<wbr>&nbsp;PCRE2_NOTEOL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Subject is not the end of a line<br />
&nbsp;<wbr>&nbsp;PCRE2_NOTEMPTY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;An empty string is not a valid match<br />
&nbsp;<wbr>&nbsp;PCRE2_NOTEMPTY_ATSTART&nbsp;<wbr>&nbsp;An empty string at the start of the subject<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;is not a valid match<br />
&nbsp;<wbr>&nbsp;PCRE2_NO_UTF_CHECK&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Do not check the subject for UTF<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;validity&nbsp;(only relevant if PCRE2_UTF<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;was set at compile time)<br />
&nbsp;<wbr>&nbsp;PCRE2_PARTIAL_HARD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Return PCRE2_ERROR_PARTIAL for a partial<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match even if there is a full match<br />
&nbsp;<wbr>&nbsp;PCRE2_PARTIAL_SOFT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Return PCRE2_ERROR_PARTIAL for a partial<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match if no full matches are found<br />
&nbsp;<wbr>&nbsp;PCRE2_DFA_RESTART&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Restart after a partial match<br />
&nbsp;<wbr>&nbsp;PCRE2_DFA_SHORTEST&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Return only the shortest match There are restrictions on what may appear in a pattern when using this matching function. Details are given in the <code>pcre2matching</code> documentation. For details of partial matching, see the <code>pcre2partial</code> page. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
