---
title: "precedence(7)"
name: "precedence"
section: "7"
letter: "p"
url: "/docs/linux/man/7-precedence/"
description: "operator – C operator precedence and order of evaluation"
---

<p>operator &#8211; C operator precedence and order of evaluation</p>
<h2>Description</h2>
<p>This manual page lists C operators and their precedence in evaluation. </p>
<table>
<tr VALIGN=top>
<td><code>Operator</code></td>
<td><code>Associativity</code></td>
<td><code>Notes</code>
</td>
</tr>
<tr VALIGN=top>
<td>() [] -&gt; . ++ &#8212;</td>
<td>left to right</td>
<td>[1]
</td>
</tr>
<tr VALIGN=top>
<td>! ~ ++ &#8212; + &#8211; (type) * &amp; sizeof</td>
<td>right to left</td>
<td>[2]
</td>
</tr>
<tr VALIGN=top>
<td>* / %</td>
<td>left to right</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>+ &#8211;</td>
<td>left to right</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&lt;&lt; &gt;&gt;</td>
<td>left to right</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&lt; &lt;= &gt; &gt;=</td>
<td>left to right</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>== !=</td>
<td>left to right</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&amp;</td>
<td>left to right</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>ha</td>
<td>left to right</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>|</td>
<td>left to right</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&amp;&amp;</td>
<td>left to right</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>||</td>
<td>left to right</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>?:</td>
<td>right to left</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>= += -= *= /= %= &lt;&lt;= &gt;&gt;= &amp;= ha= |=</td>
<td>right to left</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>,</td>
<td>left to right</td>
<td>
</td>
</tr>
</table>
<p> The following notes provide further information to the above table: </p>
<dl>
<dt>[1]</p>
<dd>The ++ and &#8212; operators at this precedence level are the postfix flavors of the operators.</p>
<dt>[2]</p>
<dd>The ++ and &#8212; operators at this precedence level are the prefix flavors of the operators.</dl>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
