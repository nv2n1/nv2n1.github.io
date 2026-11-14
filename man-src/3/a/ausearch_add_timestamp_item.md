---
title: "ausearch_add_timestamp_item(3)"
name: "ausearch_add_timestamp_item"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ausearch_add_timestamp_item/"
description: "ausearch_add_timestamp_item – build up search rule"
---

<h2>NAME</h2>
<p> ausearch_add_timestamp_item &#8211; build up search rule</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int ausearch_add_timestamp_item(auparse_state_t *au, const char *op, time_t sec, unsigned milli, ausearch_rule_t how) </p>
<h2>DESCRIPTION</h2>
<p> ausearch_add_timestamp_item adds an event time condition to the current audit search expression. The search conditions can then be used to scan logs, files, or buffers for something of interest. The op parameter specifies the desired comparison. Legal op values are <i>&lt;</i>, <i>&lt;=</i>, <i>&gt;=</i>, <i>&gt;</i> and <i>=</i>. The left operand of the comparison operator is the timestamp of the examined event, the right operand is specified by the sec and milli parameters. </p>
<p> The how value determines how this search condition will affect the existing search expression if one is already defined. The possible values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>AUSEARCH_RULE_CLEAR</i></p>
<dd> Clear the current search expression, if any, and use only this search condition.</p>
<dt><i>AUSEARCH_RULE_OR</i></p>
<dd> If a search expression <i>E</i> is already configured, replace it by <code>(</code><i>E</i><code> || </code><i>this_search_condition</i><code>)</code>.</p>
<dt><i>AUSEARCH_RULE_AND</i></p>
<dd> If a search expression <i>E</i> is already configured, replace it by <code>(</code><i>E</i><code> &amp;&amp; </code><i>this_search_condition</i><code>)</code>.</dl>
</dl>
<h2>RETURN VALUE</h2>
<p> Returns -1 if an error occurs; otherwise, 0 for success. </p>
<h2>APPLICATION USAGE</h2>
<p> Use <code><a href="/docs/linux/man/3-ausearch_add_item/">ausearch_add_item</a></code>(3) and <code><a href="/docs/linux/man/3-ausearch_add_interpreted_item/">ausearch_add_interpreted_item</a></code>(3) to add conditions that check audit record fields. Use <code><a href="/docs/linux/man/3-ausearch_add_expression/">ausearch_add_expression</a></code>(3) to add complex search expressions using a single function call. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ausearch_add_expression/">ausearch_add_expression</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_add_item/">ausearch_add_item</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_add_interpreted_item/">ausearch_add_interpreted_item</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_add_regex/">ausearch_add_regex</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_set_stop/">ausearch_set_stop</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_clear/">ausearch_clear</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_next_event/">ausearch_next_event</a></code>(3), <code><a href="/docs/linux/man/5-ausearch-expression/">ausearch-expression</a></code>(5). </p>
<h2>AUTHOR</h2>
<p> Miloslav Trmac </p>
<h2>Index</h2>
