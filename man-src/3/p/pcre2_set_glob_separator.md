---
title: "pcre2_set_glob_separator(3)"
name: "pcre2_set_glob_separator"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_set_glob_separator/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_set_glob_separator(pcre2_convert_context *cvcontext,
                             uint32_t separator_char);</code></pre>
<h2>Description</h2>
<p>This function is part of an experimental set of pattern conversion functions. It sets the component separator character that is used when converting globs. The second argument must be one of the characters forward slash, backslash, or dot. The default is backslash when running under Windows, otherwise forward slash. The result of the function is zero for success or PCRE2_ERROR_BADDATA if the second argument is invalid. The pattern conversion functions are described in the <code>pcre2convert</code> documentation. </p>
