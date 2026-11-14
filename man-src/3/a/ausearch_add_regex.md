---
title: "ausearch_add_regex(3)"
name: "ausearch_add_regex"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ausearch_add_regex/"
description: "ausearch_add_regex – use regular expression search rule"
---

<h2>NAME</h2>
<p> ausearch_add_regex &#8211; use regular expression search rule</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int ausearch_add_regex(auparse_state_t *au, const char *expr); </p>
<h2>DESCRIPTION</h2>
<p> ausearch_add_regex adds one search condition based on a regular expression to the current audit search expression. The search conditions can then be used to scan logs, files, or buffers for something of interest. The regular expression follows the posix extended regular expression conventions, and is matched against the full record (without interpreting field values). </p>
<p> If an existing search expression <i>E</i> is already defined, this function replaces it by <code>(</code><i>E</i><code> &amp;&amp; </code><i>this_regexp</i><code>)</code>. </p>
<h2>RETURN VALUE</h2>
<p> Returns -1 if an error occurs; otherwise, 0 for success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ausearch_add_expression/">ausearch_add_expression</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_add_item/">ausearch_add_item</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_clear/">ausearch_clear</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_next_event/">ausearch_next_event</a></code>(3), <code><a href="/docs/linux/man/3-regcomp/">regcomp</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
