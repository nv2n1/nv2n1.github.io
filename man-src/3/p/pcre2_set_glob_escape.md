---
title: "pcre2_set_glob_escape(3)"
name: "pcre2_set_glob_escape"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_set_glob_escape/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_set_glob_escape(pcre2_convert_context *cvcontext,
                          uint32_t escape_char);</code></pre>
<h2>Description</h2>
<p>This function is part of an experimental set of pattern conversion functions. It sets the escape character that is used when converting globs. The second argument must either be zero (meaning there is no escape character) or a punctuation character whose code point is less than 256. The default is grave accent if running under Windows, otherwise backslash. The result of the function is zero for success or PCRE2_ERROR_BADDATA if the second argument is invalid. The pattern conversion functions are described in the <code>pcre2convert</code> documentation. </p>
