---

title: "pcre2_substitute(3)"
name: "pcre2_substitute"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_substitute/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API) </p>

<p> <code>#include &lt;pcre2.h&gt;</code> </p>
<pre><code>
 int pcre2_substitute(const pcre2_code *  code , PCRE2_SPTR subject ,
   PCRE2_SIZE  length , PCRE2_SIZE startoffset ,
   uint32_t  options , pcre2_match_data * match_data ,
   pcre2_match_context *  mcontext , PCRE2_SPTR replacement ,
   PCRE2_SIZE  rlength , PCRE2_UCHAR * outputbuffer ,
   PCRE2_SIZE *  outlengthptr );
</code></pre>
<h2>DESCRIPTION</h2>
<p>This function matches a compiled regular expression against a given subject string, using a matching algorithm that is similar to Perl&#8217;s. It then makes a copy of the subject, substituting a replacement string for what was matched. Its arguments are: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to the compiled pattern <br />
&nbsp;<wbr>&nbsp;<i>subject</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to the subject string <br />
&nbsp;<wbr>&nbsp;<i>length</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Length of the subject string <br />
&nbsp;<wbr>&nbsp;<i>startoffset</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Offset in the subject at which to start matching <br />
&nbsp;<wbr>&nbsp;<i>options</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Option bits <br />
&nbsp;<wbr>&nbsp;<i>match_data</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to a match data block, or is NULL <br />
&nbsp;<wbr>&nbsp;<i>mcontext</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to a match context, or is NULL <br />
&nbsp;<wbr>&nbsp;<i>replacement</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to the replacement string <br />
&nbsp;<wbr>&nbsp;<i>rlength</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Length of the replacement string <br />
&nbsp;<wbr>&nbsp;<i>outputbuffer</i>&nbsp;<wbr>&nbsp;Points to the output buffer <br />
&nbsp;<wbr>&nbsp;<i>outlengthptr</i>&nbsp;<wbr>&nbsp;Points to the length of the output buffer </p>
<p>A match data block is needed only if you want to inspect the data from the match that is returned in that block. A match context is needed only if you want to: </p>
<p> <br />
&nbsp;<wbr>&nbsp;Set up a callout function <br />
&nbsp;<wbr>&nbsp;Set a matching offset limit <br />
&nbsp;<wbr>&nbsp;Change the backtracking match limit <br />
&nbsp;<wbr>&nbsp;Change the backtracking depth limit <br />
&nbsp;<wbr>&nbsp;Set custom memory management in the match context </p>
<p>The <i>length</i>, <i>startoffset</i> and <i>rlength</i> values are code units, not characters, as is the contents of the variable pointed at by <i>outlengthptr</i>, which is updated to the actual length of the new string. The subject and replacement lengths can be given as PCRE2_ZERO_TERMINATED for zero-terminated strings. The options are: </p>
<p> <br />
&nbsp;<wbr>&nbsp;PCRE2_ANCHORED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Match only at the first position <br />
&nbsp;<wbr>&nbsp;PCRE2_ENDANCHORED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pattern can match only at end of subject <br />
&nbsp;<wbr>&nbsp;PCRE2_NOTBOL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Subject is not the beginning of a line <br />
&nbsp;<wbr>&nbsp;PCRE2_NOTEOL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Subject is not the end of a line <br />
&nbsp;<wbr>&nbsp;PCRE2_NOTEMPTY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;An empty string is not a valid match <br />
&nbsp;<wbr>&nbsp;PCRE2_NOTEMPTY_ATSTART&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;An empty string at the start of the <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;subject is not a valid match <br />
&nbsp;<wbr>&nbsp;PCRE2_NO_JIT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Do not use JIT matching <br />
&nbsp;<wbr>&nbsp;PCRE2_NO_UTF_CHECK&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Do not check the subject or replacement <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for UTF validity&nbsp;(only relevant if <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE2_UTF was set at compile time) <br />
&nbsp;<wbr>&nbsp;PCRE2_SUBSTITUTE_EXTENDED&nbsp;<wbr>&nbsp;Do extended replacement processing <br />
&nbsp;<wbr>&nbsp;PCRE2_SUBSTITUTE_GLOBAL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Replace all occurrences in the subject <br />
&nbsp;<wbr>&nbsp;PCRE2_SUBSTITUTE_OVERFLOW_LENGTH&nbsp;<wbr>&nbsp;If overflow, compute needed length <br />
&nbsp;<wbr>&nbsp;PCRE2_SUBSTITUTE_UNKNOWN_UNSET&nbsp;<wbr>&nbsp;Treat unknown group as unset <br />
&nbsp;<wbr>&nbsp;PCRE2_SUBSTITUTE_UNSET_EMPTY&nbsp;<wbr>&nbsp;Simple unset insert&nbsp;=&nbsp;empty string </p>
<p>The function returns the number of substitutions, which may be zero if there were no matches. The result can be greater than one only when PCRE2_SUBSTITUTE_GLOBAL is set. In the event of an error, a negative error code is returned. </p>
<p>There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
