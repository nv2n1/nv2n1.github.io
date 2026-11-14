---
title: "pcre2_substitute(3)"
name: "pcre2_substitute"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_substitute/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_substitute(const pcre2_code *code, PCRE2_SPTR subject,
                     PCRE2_SIZE length, PCRE2_SIZE startoffset,
                     uint32_t options, pcre2_match_data *match_data,
                     pcre2_match_context *mcontext, PCRE2_SPTR replacement,
                     PCRE2_SIZE rlength, PCRE2_UCHAR *outputbuffer,
                     PCRE2_SIZE *outlengthptr);</code></pre>
<h2>Description</h2>
<p>This function matches a compiled regular expression against a given subject string, using a matching algorithm that is similar to Perl&#8217;s. It then makes a copy of the subject, substituting a replacement string for what was matched. Its arguments are:<br />
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to the compiled pattern<br />
&nbsp;<wbr>&nbsp;<i>subject</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to the subject string<br />
&nbsp;<wbr>&nbsp;<i>length</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Length of the subject string<br />
&nbsp;<wbr>&nbsp;<i>startoffset</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Offset in the subject at which to start matching<br />
&nbsp;<wbr>&nbsp;<i>options</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Option bits<br />
&nbsp;<wbr>&nbsp;<i>match_data</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to a match data block, or is NULL<br />
&nbsp;<wbr>&nbsp;<i>mcontext</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to a match context, or is NULL<br />
&nbsp;<wbr>&nbsp;<i>replacement</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to the replacement string<br />
&nbsp;<wbr>&nbsp;<i>rlength</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Length of the replacement string<br />
&nbsp;<wbr>&nbsp;<i>outputbuffer</i>&nbsp;<wbr>&nbsp;Points to the output buffer<br />
&nbsp;<wbr>&nbsp;<i>outlengthptr</i>&nbsp;<wbr>&nbsp;Points to the length of the output buffer A match data block is needed only if you want to inspect the data from the match that is returned in that block. A match context is needed only if you want to:<br />
&nbsp;<wbr>&nbsp;Set up a callout function<br />
&nbsp;<wbr>&nbsp;Set a matching offset limit<br />
&nbsp;<wbr>&nbsp;Change the backtracking match limit<br />
&nbsp;<wbr>&nbsp;Change the backtracking depth limit<br />
&nbsp;<wbr>&nbsp;Set custom memory management in the match context The <i>length</i>, <i>startoffset</i> and <i>rlength</i> values are code units, not characters, as is the contents of the variable pointed at by <i>outlengthptr</i>, which is updated to the actual length of the new string. The subject and replacement lengths can be given as PCRE2_ZERO_TERMINATED for zero-terminated strings. The options are:  The function returns the number of substitutions, which may be zero if there were no matches. The result can be greater than one only when PCRE2_SUBSTITUTE_GLOBAL is set. In the event of an error, a negative error code is returned. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
