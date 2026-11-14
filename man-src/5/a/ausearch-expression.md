---
title: "ausearch-expression(5)"
name: "ausearch-expression"
section: "5"
letter: "a"
url: "/docs/linux/man/5-ausearch-expression/"
description: "ausearch-expression – audit search expression format"
---

<p>ausearch-expression &#8211; audit search expression format </p>
<h2>Overview</h2>
<p>This man page describes the format of &quot;ausearch expressions&quot;. Parsing and evaluation of these expressions is provided by libauparse and is common to applications that use this library.</p>
<h2>Lexical Structure</h2>
<p>White space (ASCII space, tab and new-line characters) between tokens is ignored. The following tokens are recognized: </p>
<dl>
<dt>Punctuation</p>
<dd><code>( ) \</code> </p>
<dt>Logical operators</p>
<dd><code>! &amp;&amp; ||</code> </p>
<dt>Comparison operators</p>
<dd><code>&lt; &lt;= == &gt; &gt;= !== i= i!= r= r!=</code> </p>
<dt>Unquoted strings</p>
<dd>Any non-empty sequence of ASCII letters, digits, and the <code>_</code> symbol. </p>
<dt>Quoted strings</p>
<dd>A sequence of characters surrounded by the <code>&quot;</code> quotes. The <code>\</code> character starts an escape sequence. The only defined escape sequences are <code>\</code> and <code>\&quot;</code>. The semantics of other escape sequences is undefined. </p>
<dt>Regexps</p>
<dd>A sequence of characters surrounded by the <code>/</code> characters. The <code>\</code> character starts an escape sequence. The only defined escape sequences are <code>\</code> and <code>\/</code>. The semantics of other escape sequences is undefined. </p>
</dl>
<p> Anywhere an unquoted string is valid, a quoted string is valid as well, and vice versa. In particular, field names may be specified using quoted strings, and field values may be specified using unquoted strings.</p>
<h2>Expression Syntax</h2>
<p>The primary expression has one of the following forms:</p>
<dl>
<dd><i>field comparison-operator value</i> </p>
<p> <code>egexp</code> <i>string-or-regexp</i></dl>
<p> <i>field</i> is either a string, which specifies the first field with that name within the current audit record, or the <code>\</code> escape character followed by a string, which specifies a virtual field with the specified name (virtual fields are defined in a later section). </p>
<p> <i>field</i> is a string. <i>operator</i> specifies the comparison to perform </p>
<dl>
<dt><code>r= r!=</code></p>
<dd>Get the &quot;raw&quot; string of <i>field</i>, and compare it to <i>value</i>. For fields in audit records, the &quot;raw&quot; string is the exact string stored in the audit record (with all escaping and unprintable character encoding left alone); applications can read the &quot;raw&quot; string using <code><a href="/docs/linux/man/3-auparse_get_field_str/">auparse_get_field_str</a></code>(3). Each virtual field may define a &quot;raw&quot; string. If <i>field</i> is not present or does not define a &quot;raw&quot; string, the result of the comparison is <code>false</code> (regardless of the operator). </p>
<dt><code>i= i!=</code></p>
<dd>Get the &quot;interpreted&quot; string of <i>field</i>, and compare it to <i>value</i>. For fields in audit records, the &quot;interpreted&quot; string is an &quot;user-readable&quot; interpretation of the field value; applications can read the &quot;interpreted&quot; string using <code><a href="/docs/linux/man/3-auparse_interpret_field/">auparse_interpret_field</a></code>(3). Each virtual field may define an &quot;interpreted&quot; string. If <i>field</i> is not present or does not define an &quot;interpreted&quot; string, the result of the comparison is <code>false</code> (regardless of the operator). </p>
<dt><code>&lt; &lt;= == &gt; &gt;= !==</code></p>
<dd>Evaluate the &quot;value&quot; of <i>field</i>, and compare it to <i>value</i>. A &quot;value&quot; may be defined for any field or virtual field, but no &quot;value&quot; is currently defined for any audit record field. The rules of parsing <i>value</i> for comparing it with the &quot;value&quot; of <i>field</i> are specific for each <i>field</i>. If <i>field</i> is not present, the result of the comparison is <code>false</code> (regardless of the operator). If <i>field</i> does not define a &quot;value&quot;, an error is reported when parsing the expression.</dl>
<p> In the special case of <code>egexp</code> <i>regexp-or-string</i>, the current audit record is taken as a string (without interpreting field values), and matched against <i>regexp-or-string</i>. <i>regexp-or-string</i> is an extended regular expression, using a string or regexp token (in other words, delimited by <code>&quot;</code> or <code>/</code>). </p>
<p> If <i>E1</i> and <i>E2</i> are valid expressions, then <code>!</code> <i>E1</i>, <i>E1</i> <code>&amp;&amp;</code> <i>E2</i>, and <i>E1</i> <code>||</code> <i>E2</i> are valid expressions as well, with the usual C semantics and evaluation priorities. Note that <code>!</code> <i>field op value</i> is interpreted as <code>!(</code><i>field op value</i><code>)</code>, not as <code>(!</code><i>field</i><code>)</code><i> op value</i>.</p>
<h2>Virtual Fields</h2>
<p>The following virtual fields are defined: </p>
<dl>
<dt><code>	imestamp</code></p>
<dd>The value is the timestamp of the current event. <i>value</i> must have the <code>ts:</code><i>seconds</i>.<i>milli</i> format, where <i>seconds</i> and <i>milli</i> are decimal numbers specifying the seconds and milliseconds part of the timestamp, respectively. </p>
<dt><code>ecord_type</code></p>
<dd>The value is the type of the current record. <i>value</i> is either the record type name, or a decimal number specifying the type. </p>
</dl>
<h2>Semantics</h2>
<p>The expression as a whole applies to a single record. The expression is <code>true</code> for a specified event if it is <code>true</code> for any record associated with the event.</p>
<h2>Examples</h2>
<p>As a demonstration of the semantics of handling missing fields, the following expression is <code>true</code> if <i>field</i> is present:</p>
<dl>
<dd><code>(</code><i>field</i><code> r= &quot;&quot;) || (</code><i>field</i><code> r!= &quot;&quot;)</code></dl>
<p> and the same expression surrounded by <code>!(</code> and <code>)</code> is <code>true</code> if <i>field</i> is not present. </p>
<h2>Future Directions</h2>
<p>New escape sequences for quoted strings may be defined. </p>
<p> For currently defined virtual fields that do not define a &quot;raw&quot; or &quot;interpreted&quot; string, the definition may be added. Therefore, don&#8217;t rely on the fact that comparing the &quot;raw&quot; or &quot;interpreted&quot; string of the field with any value is <code>false</code>. </p>
<p> New formats of value constants for the <code>	imestamp</code> virtual field may be added.</p>
<h2>Author</h2>
<p>Miloslav Trmac</p>
