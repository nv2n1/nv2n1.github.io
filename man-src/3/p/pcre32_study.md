---
title: "pcre32_study(3)"
name: "pcre32_study"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre32_study/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;</code></pre>
<pre><code>pcre_extra *pcre_study(const pcre *</code><i>code</i>, int <i>options</i>,
<code> const char **</code><i>errptr</i>);
<code>pcre16_extra *pcre16_study(const pcre16 *</code><i>code</i>, int <i>options</i>,
<code> const char **</code><i>errptr</i>);
<code>pcre32_extra *pcre32_study(const pcre32 *</code><i>code</i>, int <i>options</i>,
<code> const char **</code><i>errptr</i>);</pre>
<h2>Description</h2>
<p>This function studies a compiled pattern, to see if additional information can be extracted that might speed up matching. Its arguments are:<br />
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;A compiled regular expression<br />
&nbsp;<wbr>&nbsp;<i>options</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Options for&nbsp;<code>pcre[16|32]_study()</code><br />
&nbsp;<wbr>&nbsp;<i>errptr</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to put an error message If the function succeeds, it returns a value that can be passed to <code>pcre[16|32]_exec()</code> or <code>pcre[16|32]_dfa_exec()</code> via their <i>extra</i> arguments. If the function returns NULL, either it could not find any additional information, or there was an error. You can tell the difference by looking at the error value. It is NULL in first case. The only option is PCRE_STUDY_JIT_COMPILE. It requests just-in-time compilation if possible. If PCRE has been compiled without JIT support, this option is ignored. See the <code>pcrejit</code> page for further details. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
