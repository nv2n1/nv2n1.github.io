---
title: "ausearch_add_item(3)"
name: "ausearch_add_item"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ausearch_add_item/"
description: "ausearch_add_item – build up search rule"
---

<h2>NAME</h2>
<p> ausearch_add_item &#8211; build up search rule</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int ausearch_add_item(auparse_state_t *au, const char *field, const char *op, const char *value, ausearch_rule_t how); </p>
<h2>DESCRIPTION</h2>
<p> ausearch_add_item adds one search condition to the current audit search expression. The search conditions can then be used to scan logs, files, or buffers for something of interest. The field value is the field name that the value will be checked for. The op variable describes what kind of check is to be done. Legal op values are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><i>exists</i></p>
<dd>
&nbsp;<wbr>just check that a field name exists</p>
<dt><i>=</i></p>
<dd>
&nbsp;<wbr>locate the field name and check that the value associated with it is equal to the value given in this rule.</p>
<dt><i>!=</i></p>
<dd>
&nbsp;<wbr>locate the field name and check that the value associated with it is NOT equal to the value given in this rule.</dl>
</dl>
<p> The value parameter is compared to the uninterpreted field value. If you are trying to match against a field who&#8217;s type is AUPARSE_TYPE_ESCAPED, you will want to use the ausearch_add_interpreted_item() function instead. </p>
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
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ausearch_add_expression/">ausearch_add_expression</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_add_interpreted_item/">ausearch_add_interpreted_item</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_add_timestamp_item/">ausearch_add_timestamp_item</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_add_regex/">ausearch_add_regex</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_set_stop/">ausearch_set_stop</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_clear/">ausearch_clear</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_next_event/">ausearch_next_event</a></code>(3), <code><a href="/docs/linux/man/5-ausearch-expression/">ausearch-expression</a></code>(5). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
