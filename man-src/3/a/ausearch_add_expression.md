---
title: "ausearch_add_expression(3)"
name: "ausearch_add_expression"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ausearch_add_expression/"
description: "ausearch_add_expression – build up search expression"
---

<h2>NAME</h2>
<p> ausearch_add_expression &#8211; build up search expression</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> <code>int ausearch_add_expression(auparse_state_t *</code><i>au</i><code>, const char *</code><i>expression</i><code>, char **</code><i>error</i><code>, ausearch_rule_t </code><i>how</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ausearch_add_item</code> adds an expression to the current audit search expression. The search conditions can then be used to scan logs, files, or buffers for something of interest. The <i>expression</i> parameter contains an expression, as specified in <code><a href="/docs/linux/man/5-ausearch-expression/">ausearch-expression</a></code>(5). </p>
<p> The <i>how</i> parameter determines how this search expression will affect the existing search expression, if one is already defined. The possible values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>AUSEARCH_RULE_CLEAR</i></p>
<dd> Clear the current search expression, if any, and use only this search expression.</p>
<dt><i>AUSEARCH_RULE_OR</i></p>
<dd> If a search expression <i>E</i> is already configured, replace it by <code>(</code><i>E</i><code> || </code><i>this_search_expression</i><code>)</code>.</p>
<dt><i>AUSEARCH_RULE_AND</i></p>
<dd> If a search expression <i>E</i> is already configured, replace it by <code>(</code><i>E</i><code> &amp;&amp; </code><i>this_search_expression</i><code>)</code>.</dl>
</dl>
<h2>RETURN VALUE</h2>
<p> If successful, <code>ausearch_add_expression</code> returns 0. Otherwise, it returns -1, sets <code>errno</code> and it may set <code>*</code><i>error</i> to an error message; the caller must free the error message using <code><a href="/docs/linux/man/3-free/">free</a></code>(3). If an error message is not available or can not be allocated, <code>*</code><i>error</i> is set to <code>NULL</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ausearch_add_item/">ausearch_add_item</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_add_interpreted_item/">ausearch_add_interpreted_item</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_add_timestamp_item/">ausearch_add_timestamp_item</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_add_regex/">ausearch_add_regex</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_set_stop/">ausearch_set_stop</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_clear/">ausearch_clear</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_next_event/">ausearch_next_event</a></code>(3), <code><a href="/docs/linux/man/5-ausearch-expression/">ausearch-expression</a></code>(5). </p>
<h2>AUTHOR</h2>
<p> Miloslav Trmac </p>
<h2>Index</h2>
