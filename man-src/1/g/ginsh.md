---
title: "ginsh(1)"
name: "ginsh"
section: "1"
letter: "g"
url: "/docs/linux/man/1-ginsh/"
description: "ginsh – GiNaC Interactive Shell"
---

<h2>NAME</h2>
<p> ginsh &#8211; GiNaC Interactive Shell</p>
<h2>SYNPOSIS</h2>
<p> <code>ginsh</code> [<i>file&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ginsh</code> is an interactive frontend for the GiNaC symbolic computation framework. It is intended as a tool for testing and experimenting with GiNaC&#8217;s features, not as a replacement for traditional interactive computer algebra systems. Although it can do many things these traditional systems can do, ginsh provides no programming constructs like loops or conditional expressions. If you need this functionality you are advised to write your program in C++, using the &quot;native&quot; GiNaC class framework.</p>
<h2>USAGE</h2>
<h3>INPUT FORMAT</h3>
<p> After startup, ginsh displays a prompt (&quot;&gt; &quot;) signifying that it is ready to accept your input. Acceptable input are numeric or symbolic expressions consisting of numbers (e.g. <code>42</code>, <code>2/3</code> or <code>0.17</code>), symbols (e.g. <code>x</code> or <code>result</code>), mathematical operators like <code>+</code> and <code>*</code>, and functions (e.g. <code>sin</code> or <code>normal</code>). Every input expression must be terminated with either a semicolon (<code>;</code>) or a colon (<code>:</code>). If terminated with a semicolon, ginsh will evaluate the expression and print the result to stdout. If terminated with a colon, ginsh will only evaluate the expression but not print the result. It is possible to enter multiple expressions on one line. Whitespace (spaces, tabs, newlines) can be applied freely between tokens. To quit ginsh, enter <code>quit</code> or <code>exit</code>, or type an EOF (Ctrl-D) at the prompt.</p>
<h3>COMMENTS</h3>
<p> Anything following a double slash (<code>//</code>) up to the end of the line, and all lines starting with a hash mark (<code>#</code>) are treated as a comment and ignored.</p>
<h3>NUMBERS</h3>
<p> ginsh accepts numbers in the usual decimal notations. This includes arbitrary precision integers and rationals as well as floating point numbers in standard or scientific notation (e.g. <code>1.2E6</code>). The general rule is that if a number contains a decimal point (<code>.</code>), it is an (inexact) floating point number; otherwise it is an (exact) integer or rational. Integers can be specified in binary, octal, hexadecimal or arbitrary (2-36) base by prefixing them with <code>#b</code>, <code>#o</code>, <code>#x</code>, or <code>#</code><i>n</i><code>R</code> , respectively.</p>
<h3>SYMBOLS</h3>
<p> Symbols are made up of a string of alphanumeric characters and the underscore (<code>_</code>), with the first character being non-numeric. E.g. <code>a</code> and <code>mu_1</code> are acceptable symbol names, while <code>2pi</code> is not. It is possible to use symbols with the same names as functions (e.g. <code>sin</code>); ginsh is able to distinguish between the two. </p>
<p> Symbols can be assigned values by entering</p>
<dl>
<dt>
<dd> <i>symbol</i><code> = </code><i>expression</i><code>;</code></dl>
<p> To unassign the value of an assigned symbol, type</p>
<dl>
<dt>
<dd> <code>unassign(&#8216;</code><i>symbol</i><code>&#8216;);</code></dl>
<p> Assigned symbols are automatically evaluated (= replaced by their assigned value) when they are used. To refer to the unevaluated symbol, put single quotes (<code>&#8216;</code>) around the name, as demonstrated for the &quot;unassign&quot; command above. </p>
<p> Symbols are considered to be in the complex domain by default, i.e. they are treated as if they stand in for complex numbers. This behavior can be changed by using the keywords <code>real_symbols</code> and <code>complex_symbols</code> and affects all newly created symbols. </p>
<p> The following symbols are pre-defined constants that cannot be assigned a value by the user:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Pi</code></p>
<dd> Archimedes&#8217; Constant</p>
<dt><code>Catalan</code></p>
<dd> Catalan&#8217;s Constant</p>
<dt><code>Euler</code></p>
<dd> Euler-Mascheroni Constant</p>
<dt><code>I</code></p>
<dd> sqrt(-1)</p>
<dt><code>FAIL</code></p>
<dd> an object of the GiNaC &quot;fail&quot; class</dl>
</dl>
<p> There is also the special</p>
<dl>
<dt>
<dd> <code>Digits</code></dl>
<p> symbol that controls the numeric precision of calculations with inexact numbers. Assigning an integer value to digits will change the precision to the given number of decimal places.</p>
<h3>WILDCARDS</h3>
<p> The has(), find(), match() and subs() functions accept wildcards as placeholders for expressions. These have the syntax</p>
<dl>
<dt>
<dd> <code>$</code><i>number</i></dl>
<p> for example $0, $1 etc.</p>
<h3>LAST PRINTED EXPRESSIONS</h3>
<p> ginsh provides the three special symbols</p>
<dl>
<dt>
<dd> %, %% and %%%</dl>
<p> that refer to the last, second last, and third last printed expression, respectively. These are handy if you want to use the results of previous computations in a new expression.</p>
<h3>OPERATORS</h3>
<p> ginsh provides the following operators, listed in falling order of precedence:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>!</code></p>
<dd> postfix factorial</p>
<dt><code>^</code></p>
<dd> powering</p>
<dt><code>+</code></p>
<dd> unary plus</p>
<dt><code>&#8211;</code></p>
<dd> unary minus</p>
<dt><code>*</code></p>
<dd> multiplication</p>
<dt><code>/</code></p>
<dd> division</p>
<dt><code>+</code></p>
<dd> addition</p>
<dt><code>&#8211;</code></p>
<dd> subtraction</p>
<dt><code>&lt;</code></p>
<dd> less than</p>
<dt><code>&gt;</code></p>
<dd> greater than</p>
<dt><code>&lt;=</code></p>
<dd> less or equal</p>
<dt><code>&gt;=</code></p>
<dd> greater or equal</p>
<dt><code>==</code></p>
<dd> equal</p>
<dt><code>!=</code></p>
<dd> not equal</p>
<dt><code>=</code></p>
<dd> symbol assignment</dl>
</dl>
<p> All binary operators are left-associative, with the exception of <code>^</code> and <code>=</code> which are right-associative. The result of the assignment operator (<code>=</code>) is its right-hand side, so it&#8217;s possible to assign multiple symbols in one expression (e.g. <code>a = b = c = 2;</code>).</p>
<h3>LISTS</h3>
<p> Lists are used by the <code>subs</code> and <code>lsolve</code> functions. A list consists of an opening curly brace (<code>{</code>), a (possibly empty) comma-separated sequence of expressions, and a closing curly brace (<code>}</code>).</p>
<h3>MATRICES</h3>
<p> A matrix consists of an opening square bracket (<code>[</code>), a non-empty comma-separated sequence of matrix rows, and a closing square bracket (<code>]</code>). Each matrix row consists of an opening square bracket (<code>[</code>), a non-empty comma-separated sequence of expressions, and a closing square bracket (<code>]</code>). If the rows of a matrix are not of the same length, the width of the matrix becomes that of the longest row and shorter rows are filled up at the end with elements of value zero.</p>
<h3>FUNCTIONS</h3>
<p> A function call in ginsh has the form</p>
<dl>
<dt>
<dd> <i>name</i><code>(</code><i>arguments</i><code>)</code></dl>
<p> where <i>arguments</i> is a comma-separated sequence of expressions. ginsh provides a couple of built-in functions and also &quot;imports&quot; all symbolic functions defined by GiNaC and additional libraries. There is no way to define your own functions other than linking ginsh against a library that defines symbolic GiNaC functions. </p>
<p> ginsh provides Tab-completion on function names: if you type the first part of a function name, hitting Tab will complete the name if possible. If the part you typed is not unique, hitting Tab again will display a list of matching functions. Hitting Tab twice at the prompt will display the list of all available functions. </p>
<p> A list of the built-in functions follows. They nearly all work as the respective GiNaC methods of the same name, so I will not describe them in detail here. Please refer to the GiNaC documentation. </p>
<dl>
<dt>
<dd> <code>charpoly(</code><i>matrix</i><code>, </code><i>symbol</i><code>)</code> &#8211; characteristic polynomial of a matrix<br />
 <code>coeff(</code><i>expression</i><code>, </code><i>object</i><code>, </code><i>number</i><code>)</code> &#8211; extracts coefficient of object^number from a polynomial<br />
 <code>collect(</code><i>expression</i><code>, </code><i>object-or-list</i><code>)</code> &#8211; collects coefficients of like powers (result in recursive form)<br />
 <code>collect_distributed(</code><i>expression</i><code>, </code><i>list</i><code>)</code> &#8211; collects coefficients of like powers (result in distributed form)<br />
 <code>collect_common_factors(</code><i>expression</i><code>)</code> &#8211; collects common factors from the terms of sums<br />
 <code>conjugate(</code><i>expression</i><code>)</code> &#8211; complex conjugation<br />
 <code>content(</code><i>expression</i><code>, </code><i>symbol</i><code>)</code> &#8211; content part of a polynomial<br />
 <code>decomp_rational(</code><i>expression</i><code>, </code><i>symbol</i><code>)</code> &#8211; decompose rational function into polynomial and proper rational function<br />
 <code>degree(</code><i>expression</i><code>, </code><i>object</i><code>)</code> &#8211; degree of a polynomial<br />
 <code>denom(</code><i>expression</i><code>)</code> &#8211; denominator of a rational function<br />
 <code>determinant(</code><i>matrix</i><code>)</code> &#8211; determinant of a matrix<br />
 <code>diag(</code><i>expression&#8230;</i><code>)</code> &#8211; constructs diagonal matrix<br />
 <code>diff(</code><i>expression</i><code>, </code><i>symbol [</i><code>, </code><i>number]</i><code>)</code> &#8211; partial differentiation<br />
 <code>divide(</code><i>expression</i><code>, </code><i>expression</i><code>)</code> &#8211; exact polynomial division<br />
 <code>eval(</code><i>expression [</i><code>, </code><i>level]</i><code>)</code> &#8211; evaluates an expression, replacing symbols by their assigned value<br />
 <code>evalf(</code><i>expression [</i><code>, </code><i>level]</i><code>)</code> &#8211; evaluates an expression to a floating point number<br />
 <code>evalm(</code><i>expression</i><code>)</code> &#8211; evaluates sums, products and integer powers of matrices<br />
 <code>expand(</code><i>expression</i><code>)</code> &#8211; expands an expression<br />
 <code>factor(</code><i>expression</i><code>)</code> &#8211; factorizes an expression (univariate)<br />
 <code>find(</code><i>expression</i><code>, </code><i>pattern</i><code>)</code> &#8211; returns a list of all occurrences of a pattern in an expression<br />
 <code>fsolve(</code><i>expression</i><code>, </code><i>symbol</i><code>, </code><i>number</i><code>, </code><i>number</i><code>)</code> &#8211; numerically find root of a real-valued function within an interval<br />
 <code>gcd(</code><i>expression</i><code>, </code><i>expression</i><code>)</code> &#8211; greatest common divisor<br />
 <code>has(</code><i>expression</i><code>, </code><i>pattern</i><code>)</code> &#8211; returns &quot;1&quot; if the first expression contains the pattern as a subexpression, &quot;0&quot; otherwise<br />
 <code>integer_content(</code><i>expression</i><code>)</code> &#8211; integer content of a polynomial<br />
 <code>inverse(</code><i>matrix</i><code>)</code> &#8211; inverse of a matrix<br />
 <code>is(</code><i>relation</i><code>)</code> &#8211; returns &quot;1&quot; if the relation is true, &quot;0&quot; otherwise (false or undecided)<br />
 <code>lcm(</code><i>expression</i><code>, </code><i>expression</i><code>)</code> &#8211; least common multiple<br />
 <code>lcoeff(</code><i>expression</i><code>, </code><i>object</i><code>)</code> &#8211; leading coefficient of a polynomial<br />
 <code>ldegree(</code><i>expression</i><code>, </code><i>object</i><code>)</code> &#8211; low degree of a polynomial<br />
 <code>lsolve(</code><i>equation-list</i><code>, </code><i>symbol-list</i><code>)</code> &#8211; solve system of linear equations<br />
 <code>map(</code><i>expression</i><code>, </code><i>pattern</i><code>)</code> &#8211; apply function to each operand; the function to be applied is specified as a pattern with the &quot;$0&quot; wildcard standing for the operands<br />
 <code>match(</code><i>expression</i><code>, </code><i>pattern</i><code>)</code> &#8211; check whether expression matches a pattern; returns a list of wildcard substitutions or &quot;FAIL&quot; if there is no match<br />
 <code>nops(</code><i>expression</i><code>)</code> &#8211; number of operands in expression<br />
 <code>normal(</code><i>expression [</i><code>, </code><i>level]</i><code>)</code> &#8211; rational function normalization<br />
 <code>numer(</code><i>expression</i><code>)</code> &#8211; numerator of a rational function<br />
 <code>numer_denom(</code><i>expression</i><code>)</code> &#8211; numerator and denumerator of a rational function as a list<br />
 <code>op(</code><i>expression</i><code>, </code><i>number</i><code>)</code> &#8211; extract operand from expression<br />
 <code>power(</code><i>expr1</i><code>, </code><i>expr2</i><code>)</code> &#8211; exponentiation (equivalent to writing expr1^expr2)<br />
 <code>prem(</code><i>expression</i><code>, </code><i>expression</i><code>, </code><i>symbol</i><code>)</code> &#8211; pseudo-remainder of polynomials<br />
 <code>primpart(</code><i>expression</i><code>, </code><i>symbol</i><code>)</code> &#8211; primitive part of a polynomial<br />
 <code>quo(</code><i>expression</i><code>, </code><i>expression</i><code>, </code><i>symbol</i><code>)</code> &#8211; quotient of polynomials<br />
 <code>rank(</code><i>matrix</i><code>)</code> &#8211; rank of a matrix<br />
 <code>rem(</code><i>expression</i><code>, </code><i>expression</i><code>, </code><i>symbol</i><code>)</code> &#8211; remainder of polynomials<br />
 <code>resultant(</code><i>expression</i><code>, </code><i>expression</i><code>, </code><i>symbol</i><code>)</code> &#8211; resultant of two polynomials with respect to symbol s<br />
 <code>series(</code><i>expression</i><code>, </code><i>relation-or-symbol</i><code>, </code><i>order</i><code>)</code> &#8211; series expansion<br />
 <code>sprem(</code><i>expression</i><code>, </code><i>expression</i><code>, </code><i>symbol</i><code>)</code> &#8211; sparse pseudo-remainder of polynomials<br />
 <code>sqrfree(</code><i>expression [</i><code>, </code><i>symbol-list]</i><code>)</code> &#8211; square-free factorization of a polynomial<br />
 <code>sqrt(</code><i>expression</i><code>)</code> &#8211; square root<br />
 <code>subs(</code><i>expression</i><code>, </code><i>relation-or-list</i><code>)</code><br />
 <code>subs(</code><i>expression</i><code>, </code><i>look-for-list</i><code>, </code><i>replace-by-list</i><code>)</code> &#8211; substitute subexpressions (you may use wildcards)<br />
 <code>tcoeff(</code><i>expression</i><code>, </code><i>object</i><code>)</code> &#8211; trailing coefficient of a polynomial<br />
 <code>time(</code><i>expression</i><code>)</code> &#8211; returns the time in seconds needed to evaluate the given expression<br />
 <code>trace(</code><i>matrix</i><code>)</code> &#8211; trace of a matrix<br />
 <code>transpose(</code><i>matrix</i><code>)</code> &#8211; transpose of a matrix<br />
 <code>unassign(</code><i>&#8216;symbol&#8217;</i><code>)</code> &#8211; unassign an assigned symbol (mind the quotes, please!)<br />
 <code>unit(</code><i>expression</i><code>, </code><i>symbol</i><code>)</code> &#8211; unit part of a polynomial
</dl>
<h3>SPECIAL COMMANDS</h3>
<p> To exit ginsh, enter</p>
<dl>
<dt>
<dd> <code>quit</code></dl>
<p> or</p>
<dl>
<dt>
<dd> <code>exit</code></dl>
<p> ginsh can display a (short) help for a given topic (mostly about functions and operators) by entering</p>
<dl>
<dt>
<dd> <code>?</code><i>topic</i></dl>
<p> Typing</p>
<dl>
<dt>
<dd> <code>??</code></dl>
<p> will display a list of available help topics. </p>
<p> The command</p>
<dl>
<dt>
<dd> <code>print(</code><i>expression</i><code>);</code></dl>
<p> will print a dump of GiNaC&#8217;s internal representation for the given <i>expression</i>. This is useful for debugging and for learning about GiNaC internals. </p>
<p> The command</p>
<dl>
<dt>
<dd> <code>print_latex(</code><i>expression</i><code>);</code></dl>
<p> prints a LaTeX representation of the given <i>expression</i>. </p>
<p> The command</p>
<dl>
<dt>
<dd> <code>print_csrc(</code><i>expression</i><code>);</code></dl>
<p> prints the given <i>expression</i> in a way that can be used in a C or C++ program. </p>
<p> The command</p>
<dl>
<dt>
<dd> <code>iprint(</code><i>expression</i><code>);</code></dl>
<p> prints the given <i>expression</i> (which must evaluate to an integer) in decimal, octal, and hexadecimal representations. </p>
<p> Finally, the shell escape</p>
<dl>
<dt>
<dd> <code>!</code> [<i>command </i>[<i>arguments</i>]]</dl>
<p> passes the given <i>command</i> and optionally <i>arguments</i> to the shell for execution. With this method, you can execute shell commands from within ginsh without having to quit.</p>
<h2>EXAMPLES</h2>
<pre><code>
&gt; a = x ^ 2 - x - 2;
- 2 - x + x ^ 2 &gt; b = (x + 1) ^ 2;
(x + 1) ^ 2 &gt; s = a / b;
(x + 1) ^ (-2) * (-2 - x + x ^ 2) &gt; diff(s, x);
(2 * x - 1) * (x + 1) ^ (-2) - 2 * (x + 1) ^ (-3) * (-x + x ^ 2 - 2) &gt; normal(s);
(x - 2) * (x + 1) ^ (-1) &gt; x = 3 ^ 50;
717897987691852588770249 &gt; s;
717897987691852588770247 / 717897987691852588770250 &gt; Digits = 40;
40 &gt; evalf(s);
0.999999999999999999999995821133292704384960990679 &gt; unassign('x');
x &gt; s;
(x + 1) ^ (-2) * (-x + x ^ 2 - 2) &gt; series(sin(x), x == 0, 6);
1 * x + (-1 / 6) * x ^ 3 + 1 / 120 * x ^ 5 + Order(x ^ 6) &gt; lsolve({3 * x + 5 * y == 7}, {x, y});
{x == -5 / 3 * y + 7 / 3, y == y} &gt; lsolve({3 * x + 5 * y == 7, -2 * x + 10 * y == -5}, {x, y});
{x == 19 / 8, y == -1 / 40} &gt; M = [[a, b], [c, d]];
[ [ -x + x ^ 2 - 2, (x + 1) ^ 2 ], [ c, d ] ] &gt; determinant(M);
- 2 * d - 2 * x *c - x ^ 2 * c - x *d + x ^ 2 * d - c &gt; collect(%, x);
(-d - 2 * c) * x + (d - c) * x ^ 2 - 2 * d - c
                                     &gt; solve quantum field theory;
parse error at quantum &gt; quit
</code></pre>
<h2>DIAGNOSTICS</h2>
<dl>
<dt>parse error at <i>foo</i></p>
<dd> You entered something which ginsh was unable to parse. Please check the syntax of your input and try again.</p>
<dt>argument <i>num</i> to <i>function</i> must be a <i>type</i></p>
<dd> The argument number <i>num</i> to the given <i>function</i> must be of a certain type (e.g. a symbol, or a list). The first argument has number 0, the second argument number 1, etc.</dl>
<h2>AUTHOR</h2>
<dl>
<dt>The GiNaC Group:</p>
<dd>
 Christian Bauer &lt;Christian.Bauer [at] uni-mainz.de&gt;<br />
 Alexander Frink &lt;Alexander.Frink [at] uni-mainz.de&gt;<br />
 Richard Kreckel &lt;Richard.Kreckel [at] uni-mainz.de&gt;<br />
 Jens Vollinga &lt;vollinga [at] thep.physik.uni-mainz.de&gt;</dl>
<h2>SEE ALSO</h2>
<p> GiNaC Tutorial &#8211; An open framework for symbolic computation within the C++ programming language </p>
<p> CLN &#8211; A Class Library for Numbers, Bruno Haible</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1999-2009 Johannes Gutenberg Universit:at Mainz, Germany </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
