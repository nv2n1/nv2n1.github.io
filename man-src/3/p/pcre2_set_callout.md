---
title: "pcre2_set_callout(3)"
name: "pcre2_set_callout"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_set_callout/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_set_callout(pcre2_match_context *mcontext,
                      int (*callout_function)(pcre2_callout_block *),
                      void *callout_data);</code></pre>
<h2>Description</h2>
<p>This function sets the callout fields in a match context (the first argument). The second argument specifies a callout function, and the third argument is an opaque data item that is passed to it. The result of this function is always zero. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
