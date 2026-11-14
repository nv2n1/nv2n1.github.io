---
title: "booldnf(1)"
name: "booldnf"
section: "1"
letter: "b"
url: "/docs/linux/man/1-booldnf/"
description: "booldnf – converts a boolean expression to the DNF"
---

<h2>NAME</h2>
<p> booldnf &#8211; converts a boolean expression to the DNF</p>
<h2>SYNOPSIS</h2>
<p> <code>echo &#8216;a&amp;(!b|c&amp;!d)&#8217; | booldnf &gt; result.txt</code></p>
<h2>DESCRIPTION</h2>
<p> <code>booldnf</code> is a program that reads boolean expressions from its standard input and rewrites them in <code>Disjunctive Normal Form</code> on its standard output. It uses the BoolStuff library. </p>
<p> The Disjunctive Normal Form is an ORing of ANDed terms. In other words, if the OR is considered an additive operation and the AND a multiplicative operation, then the DNF is a sum of products. </p>
<p> Each expression must be on its own text line. Variable names must be composed only of ASCII letters and digits. </p>
<p> The AND operator is <code>&amp;</code>, the OR operator is <code>|</code>, and the NOT operator is <code>!</code>. Parentheses are allowed. </p>
<p> The command flushes its output buffer after each result or error message, to make sure that it can be used with bidirectional pipes. Results and error messages always take exactly one text line.</p>
<h2>EXAMPLES</h2>
<p> The command</p>
<dl>
<dt>
<dd> <code>echo &#8216;a&amp;(!b|c&amp;!d)&#8217; | booldnf</code></dl>
<p> should display</p>
<dl>
<dt>
<dd> <code>a&amp;c&amp;!d|a&amp;!b</code></dl>
<h2>LICENSE</h2>
<p> This program is free software; you may redistribute it under the terms of the GNU General Public License. This program has absolutely no warranty.</p>
<h2>AUTHOR</h2>
<p> See the <a href="/docs/linux/man/3-boolstuff/">boolstuff</a>(3) manual page.</p>
<h2>BUGS</h2>
<p> See the <a href="/docs/linux/man/3-boolstuff/">boolstuff</a>(3) manual page. </p>
<h2>Index</h2>
