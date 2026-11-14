---
title: "boolstuff(3)"
name: "boolstuff"
section: "3"
letter: "b"
url: "/docs/linux/man/3-boolstuff/"
description: "boolstuff – Disjunctive Normal Form boolean expression C++ library"
---

<h2>NAME</h2>
<p> boolstuff &#8211; Disjunctive Normal Form boolean expression C++ library</p>
<h2>SYNOPSIS</h2>
<p> <code>g++ prog.cpp -lboolstuff</code></p>
<h2>DESCRIPTION</h2>
<p> <code>boolstuff</code> is a C++ library that contains an algorithm to convert a boolean expression binary tree into the Disjunctive Normal Form. The NOT operator is supported. A C API covers most of the library&#8217;s functionality. </p>
<p> The Disjunctive Normal Form is an ORing of ANDed terms. In other words, if the OR is considered an additive operation and the AND a multiplicative operation, then the DNF is a sum of products. </p>
<p> For example, the DNF of the expression <code>a&amp;(b|c)</code> is <code>a&amp;b|a&amp;c</code> </p>
<p> The DNF eliminates parentheses and provides a normalized form of the original expression. This normalized form is easier to execute. </p>
<p> The DNF produced by BoolStuff is devoid of any &quot;useless&quot; terms, which are always false (e.g., <code>x&amp;y&amp;!x</code>), but the terms that form the DNF are not necessarily simplified (e.g., <code>x&amp;y&amp;x</code>). When executing an expression in DNF, it is recommended to obtain the list of terms and then to obtain the set of variables used in each term. In the case of the term <code>x&amp;y&amp;x</code>, the set will only contain <code>x</code> once.</p>
<h2>EXAMPLES</h2>
<p> The library&#8217;s source archive comes with an example program (in the &#8216;examples&#8217; subdirectory) and with two testing programs (in the src/boolstuff subdirectory).</p>
<h2>LICENSE</h2>
<p> This program is free software; you may redistribute it under the terms of the GNU General Public License. This program has absolutely no warranty.</p>
<h2>AUTHOR</h2>
<p> Pierre Sarrazin </p>
<p> See the BoolStuff Home Page:<br />
 <a rel="nofollow" href="http://sarrazip.com/dev/boolstuff.html">http://sarrazip.com/dev/boolstuff.html</a> </p>
<p> Comments are welcome.</p>
<h2>BUGS</h2>
<p> Version 0.1.x is an unstable development version. The programming interface of the library and the command-line options of the accompanying commands are not necessarily fixed. The documentation has not been reviewed for completeness.</p>
<h2>HISTORY</h2>
<p> George Boole (1815-1864) is an English mathematician who helped establish modern symbolic logic and whose algebra of logic, now called Boolean algebra, is basic to the design of digital computer circuits. </p>
<h2>Index</h2>
