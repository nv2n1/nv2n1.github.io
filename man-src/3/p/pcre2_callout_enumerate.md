---
title: "pcre2_callout_enumerate(3)"
name: "pcre2_callout_enumerate"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_callout_enumerate/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_callout_enumerate(const pcre2_code *code,
                            int (*callback)(pcre2_callout_enumerate_block *, void *),
                            void *callout_data);</code></pre>
<h2>Description</h2>
<p>This function scans a compiled regular expression and calls the <i>callback()</i> function for each callout within the pattern. The yield of the function is zero for success and non-zero otherwise. The arguments are:<br />
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to the compiled pattern<br />
&nbsp;<wbr>&nbsp;<i>callback</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The callback function<br />
&nbsp;<wbr>&nbsp;<i>callout_data</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;User data that is passed to the callback The <i>callback()</i> function is passed a pointer to a data block containing the following fields (not necessarily in this order):<br />
&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>version</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Block version number<br />
&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>callout_number</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Number for numbered callouts<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE&nbsp;<i>pattern_position</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Offset to next item in pattern<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE&nbsp;<i>next_item_length</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Length of next item in pattern<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE&nbsp;<i>callout_string_offset</i>&nbsp;<wbr>&nbsp;Offset to string within pattern<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE&nbsp;<i>callout_string_length</i>&nbsp;<wbr>&nbsp;Length of callout string<br />
&nbsp;<wbr>&nbsp;PCRE2_SPTR&nbsp;<i>callout_string</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to callout string or is NULL The second argument passed to the <code>callback()</code> function is the callout data that was passed to <code>pcre2_callout_enumerate()</code>. The <code>callback()</code> function must return zero for success. Any other value causes the pattern scan to stop, with the value being passed back as the result of <code>pcre2_callout_enumerate()</code>. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
