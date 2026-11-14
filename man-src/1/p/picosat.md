---
title: "picosat(1)"
name: "picosat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-picosat/"
description: "picosat – Satisfiability (SAT) solver with proof and core support"
---

<h2>NAME</h2>
<p> picosat &#8211; Satisfiability (SAT) solver with proof and core support</p>
<h2>SYNOPSIS</h2>
<p> <code>picosat</code> [<i>OPTION</i>]&#8230; [<i>FILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> PicoSAT is a satisfiability (SAT) solver for boolean variables in boolean expressions. A SAT solver can determine if it is possible to find assignments to boolean variables that would make a given set of expressions true. If it&#8217;s satisfiable, it can also show a set of assignments that make the expression true. Many problems can be broken down into a large SAT problem (perhaps with thousands of variables), so SAT solvers have a variety of uses. </p>
<p> The <code>picosat</code> binary is built with options that provide for the greatest speed. A second binary, <code>picosat.trace</code>, is built with proof and core capabilities, which incur some overhead. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> print this command line option summary and exit </p>
<dt><code>&#8211;version</code></p>
<dd> print version and exit </p>
<dt><code>&#8211;config</code></p>
<dd> print build configuration and exit </p>
<dt><code>-v</code></p>
<dd> enable verbose output </p>
<dt><code>-f</code></p>
<dd> ignore invalid header </p>
<dt><code>-n</code></p>
<dd> do not print satisfying assignment </p>
<dt><code>-p</code></p>
<dd> print formula in DIMACS format and exit </p>
<dt><code>-a</code><i> &lt;lit&gt;</i></p>
<dd> start with an assumption </p>
<dt><code>-l</code><i> &lt;limit&gt;</i></p>
<dd> set decision limit (no limit per default) </p>
<dt><code>-i</code><i> &lt;0|1&gt;</i></p>
<dd> force FALSE respectively TRUE as default phase </p>
<dt><code>-s</code><i> &lt;seed&gt;</i></p>
<dd> set random number generator seed (default 0) </p>
<dt><code>-o</code><i> &lt;output&gt;</i></p>
<dd> set output file (&lt;stdout&gt; per default) </p>
<dt><code>-t</code><i> &lt;trace&gt;</i></p>
<dd> generate compact proof trace file (use picosat.trace; see above) </p>
<dt><code>-T</code><i> &lt;trace&gt;</i></p>
<dd> generate extended proof trace file (use picosat.trace; see above) </p>
<dt><code>-r</code><i> &lt;trace&gt;</i></p>
<dd> generate reverse unit propagation proof file (use picosat.trace; see above) </p>
<dt><code>-c</code><i> &lt;core&gt;</i></p>
<dd> generate clausal core file in DIMACS format (use picosat.trace; see above) </p>
<dt><code>-V</code><i> &lt;core&gt;</i></p>
<dd> generate file listing core variables </p>
<dt><code>-U</code><i> &lt;core&gt;</i></p>
<dd> generate file listing used variables </p>
</dl>
<p> If no input filename is given, standard input is used. </p>
<h2>CONFORMING TO</h2>
<p> This program uses DIMACS CNF format as input. </p>
<p> Like many SAT solvers, this program requires that its input be in conjunctive normal form (CNF or cnf) in DIMACS CNF format. CNF is built from these building blocks:</p>
<dl>
<dt>*</p>
<dd> <i>R term :</i> A term is either a boolean variable (e.g., x4) or a negated boolean variable (NOT x4, written here as -x4).</p>
<dt>*</p>
<dd> <i>R clause :</i> A clause is a set of one or more terms, connected with OR (written here as |); boolean variables may not repeat inside a clause.</p>
<dt>*</p>
<dd> <i>R expression :</i> An expression is a set of one or more clauses, each connected by AND (written here as &amp;). </p>
</dl>
<p> Any boolean expression can be converted into CNF. </p>
<p> DIMACS CNF format is a simple text format for CNF. Every line beginning &quot;c&quot; is a comment. The first non-comment line must be of the form: </p>
<p>&nbsp;<wbr>p cnf NUMBER_OF_VARIABLES NUMBER_OF_CLAUSES </p>
<p> Each of the non-comment lines afterwards defines a clause. Each of these lines is a space-separated list of variables; a positive value means that corresponding variable (so 4 means x4), and a negative value means the negation of that variable (so -5 means -x5). Each line must end in a space and the number 0. </p>
<h2>EXIT STATUS</h2>
<p> The output is a number of lines. Most of these will begin with &quot;c&quot; (comment), and give detailed technical information. The output line beginning with &quot;s&quot; declares whether or not it is satisfiable. The line &quot;s SATISFIABLE&quot; is produced if it is satisfiable (exit status 10), and &quot;s UNSATISFIABLE&quot; is produced if it is not satisfiable (exit status 20). </p>
<p> If it is satisfiable, the output line beginning with &quot;v&quot; declares a set of variable settings that satisfy all formulas. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>v 1 -2 -3 -4 5 0 </p>
<p> Shows that there is a solution with variable 1 true, variables 2, 3, and 4 false, and variable 5 true. </p>
<h2>EXAMPLE</h2>
<p> An example of CNF is: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>(x1 | -x5 | x4)&nbsp;<wbr>&amp;<br />
&nbsp;<wbr>&nbsp;<wbr>(-x1 | x5 | x3 | x4)&nbsp;<wbr>&amp;<br />
&nbsp;<wbr>&nbsp;<wbr>(-x3 | x4). </p>
<p> The DIMACS CNF format for the above set of expressions could be: </p>
<p>&nbsp;<wbr>c Here is a comment.<br />
&nbsp;<wbr>p cnf 5 3<br />
&nbsp;<wbr>1 -5 4 0<br />
&nbsp;<wbr>-1 5 3 4 0<br />
&nbsp;<wbr>-3 -4 0 </p>
<p> The &quot;p cnf&quot; line above means that this is SAT problem in CNF format with 5 variables and 3 clauses. The first line after it is the first clause, meaning x1 | -x5 | x4. </p>
<p> CNFs with conflicting requirements are not satisfiable. For example, the following DIMACS CNF formatted data is not satisfiable, because it requires that variable 1 always be true and also always be false: </p>
<p>&nbsp;<wbr>c This is not satisfiable.<br />
&nbsp;<wbr>p cnf 2 2<br />
&nbsp;<wbr>-1 0<br />
&nbsp;<wbr>1 0 </p>
<h2>AUTHORS</h2>
<p> picosat was written by Armin Biere &lt;biere [at] jku.at&gt; </p>
<p> This man page was written by David A. Wheeler. It is released to the public domain; you may use it in any way you wish. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-picomus/">picomus</a></i>(1), <i><a href="/docs/linux/man/1-minisat2/">minisat2</a></i>(1). </p>
<h2>Index</h2>
