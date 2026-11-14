---
title: "pcre16_jit_exec(3)"
name: "pcre16_jit_exec"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre16_jit_exec/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
int pcre_jit_exec(const pcre *code, const pcre_extra *extra,
                  const char *subject, int length, int startoffset,
                  int options, int *ovector, int ovecsize,
                  pcre_jit_stack *jstack);

int pcre16_jit_exec(const pcre16 *code, const pcre16_extra *extra,
                    PCRE_SPTR16 subject, int length, int startoffset,
                    int options, int *ovector, int ovecsize,
                    pcre_jit_stack *jstack);

int pcre32_jit_exec(const pcre32 *code, const pcre32_extra *extra,
                    PCRE_SPTR32 subject, int length, int startoffset,
                    int options, int *ovector, int ovecsize,
                    pcre_jit_stack *jstack);</code></pre>
<h2>Description</h2>
<p>This function matches a compiled regular expression that has been successfully studied with one of the JIT options against a given subject string, using a matching algorithm that is similar to Perl&#8217;s. It is a &quot;fast path&quot; interface to JIT, and it bypasses some of the sanity checks that <code>pcre_exec()</code> applies. It returns offsets to captured substrings. Its arguments are:<br />
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to the compiled pattern<br />
&nbsp;<wbr>&nbsp;<i>extra</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to an associated&nbsp;<code>pcre[16|32]_extra</code>&nbsp;structure,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;or is NULL<br />
&nbsp;<wbr>&nbsp;<i>subject</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to the subject string<br />
&nbsp;<wbr>&nbsp;<i>length</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Length of the subject string, in bytes<br />
&nbsp;<wbr>&nbsp;<i>startoffset</i>&nbsp;<wbr>&nbsp;Offset in bytes in the subject at which to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start matching<br />
&nbsp;<wbr>&nbsp;<i>options</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Option bits<br />
&nbsp;<wbr>&nbsp;<i>ovector</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to a vector of ints for result offsets<br />
&nbsp;<wbr>&nbsp;<i>ovecsize</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Number of elements in the vector&nbsp;(a multiple of 3)<br />
&nbsp;<wbr>&nbsp;<i>jstack</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pointer to a JIT stack The allowed options are:<br />
&nbsp;<wbr>&nbsp;PCRE_NOTBOL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Subject string is not the beginning of a line<br />
&nbsp;<wbr>&nbsp;PCRE_NOTEOL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Subject string is not the end of a line<br />
&nbsp;<wbr>&nbsp;PCRE_NOTEMPTY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;An empty string is not a valid match<br />
&nbsp;<wbr>&nbsp;PCRE_NOTEMPTY_ATSTART&nbsp;<wbr>&nbsp;An empty string at the start of the subject<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;is not a valid match<br />
&nbsp;<wbr>&nbsp;PCRE_NO_UTF16_CHECK&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Do not check the subject for UTF-16<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;validity&nbsp;(only relevant if PCRE_UTF16<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;was set at compile time)<br />
&nbsp;<wbr>&nbsp;PCRE_NO_UTF32_CHECK&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Do not check the subject for UTF-32<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;validity&nbsp;(only relevant if PCRE_UTF32<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;was set at compile time)<br />
&nbsp;<wbr>&nbsp;PCRE_NO_UTF8_CHECK&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Do not check the subject for UTF-8<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;validity&nbsp;(only relevant if PCRE_UTF8<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;was set at compile time)<br />
&nbsp;<wbr>&nbsp;PCRE_PARTIAL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;)&nbsp;Return PCRE_ERROR_PARTIAL for a partial<br />
&nbsp;<wbr>&nbsp;PCRE_PARTIAL_SOFT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;)&nbsp;<wbr>&nbsp;<wbr>&nbsp;match if no full matches are found<br />
&nbsp;<wbr>&nbsp;PCRE_PARTIAL_HARD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Return PCRE_ERROR_PARTIAL for a partial match<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if that is found before a full match However, the PCRE_NO_UTF[8|16|32]_CHECK options have no effect, as this check is never applied. For details of partial matching, see the <code>pcrepartial</code> page. A <code>pcre_extra</code> structure contains the following fields:<br />
&nbsp;<wbr>&nbsp;<i>flags</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bits indicating which fields are set<br />
&nbsp;<wbr>&nbsp;<i>study_data</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Opaque data from&nbsp;<code>pcre[16|32]_study()</code><br />
&nbsp;<wbr>&nbsp;<i>match_limit</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Limit on internal resource use<br />
&nbsp;<wbr>&nbsp;<i>match_limit_recursion</i>&nbsp;<wbr>&nbsp;Limit on internal recursion depth<br />
&nbsp;<wbr>&nbsp;<i>callout_data</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Opaque data passed back to callouts<br />
&nbsp;<wbr>&nbsp;<i>tables</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to character tables or is NULL<br />
&nbsp;<wbr>&nbsp;<i>mark</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;For passing back a&nbsp;*MARK pointer<br />
&nbsp;<wbr>&nbsp;<i>executable_jit</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Opaque data from JIT compilation The flag bits are PCRE_EXTRA_STUDY_DATA, PCRE_EXTRA_MATCH_LIMIT, PCRE_EXTRA_MATCH_LIMIT_RECURSION, PCRE_EXTRA_CALLOUT_DATA, PCRE_EXTRA_TABLES, PCRE_EXTRA_MARK and PCRE_EXTRA_EXECUTABLE_JIT. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the JIT API in the <code>pcrejit</code> page. </p>
