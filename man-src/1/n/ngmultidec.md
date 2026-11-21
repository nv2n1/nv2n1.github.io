---

title: "ngmultidec(1)"
name: "ngmultidec"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ngmultidec/"
description: "ngmultidec – make ngpice sub-circuit for coupled transmission lines"
---

<h2>NAME</h2>
<p> ngmultidec &#8211; make ngpice sub-circuit for coupled transmission lines</p>
<p> <code>ngmultidec</code> [ <i>options</i>&#8230; ]</p>
<p> <i>ngmultidec</i> writes an ngspice input file to standard output which describes a sub-circuit for coupled lines using uncoupled simple lossy lines. </p>
<p> Each generated subcircuit models a 4-conductor transmission line with the following parameters: length <i>l</i>, line capacitance <i>c</i>, line resistance <i>r</i>, line conductance <i>g</i>, inductive_coeff_of_coupling <i>k</i>, inter-line capacitance <i>cm</i>, length <i>l</i>. Derived parameters are: <i>lm</i>, <i>ctot</i>. The values of <i>l</i>, <i>c</i>, the model name, the number of conductors and the length of the line must be specified. </p>
<p> It is important to note that the model is a simplified one &#8211; the following assumptions are made: 1. The self-inductance l, the self-capacitance ctot (note: not c), the series resistance r and the parallel capacitance g are the same for all lines, and 2. Each line is coupled only to the two lines adjacent to it, with the same coupling parameters cm and lm. The first assumption implies that edge effects have to be neglected. The utility of these assumptions is that they make the sL+R and sC+G matrices symmetric, tridiagonal and Toeplitz, with useful consequences (see the paper referenced below). </p>
<p> It may be noted that a symmetric two-conductor line is represented accurately by this model. </p>
<p> Standard C language scientific (exponent) notation may be used for options&#8217; numeric values.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code><i>subcircuit_name</i></dt>
<dd> Set the subcircuit name</dd>
<dt><code>-l</code><i>line_inductance</i></dt>
<dd> Set the line inductance.</dd>
<dt><code>-c</code><i>line_capacitance</i></dt>
<dd> Set the line capacitance.</dd>
<dt><code>-r</code><i>line_resistance</i></dt>
<dd> Set the line resistance.</dd>
<dt><code>-g</code><i>line_conductance</i></dt>
<dd> Set the line conductance.</dd>
<dt><code>-k</code><i>inductive_coefficient_of_coupling</i></dt>
<dd> Set the value of the inductive coefficient of coupling, whose absolute value <i>k</i> must be less than 1.0.</dd>
<dt><code>-x</code><i>line-to-line-capacitance</i></dt>
<dd> Set the line-to-line capacitance.</dd>
<dt><code>-L</code><i>length</i></dt>
<dd> Set the length of the line.</dd>
<dt><code>-n</code><i>number</i></dt>
<dd> Set the number of conductors.</dd>
<dt><code>-u</code></dt>
<dd> Write a usage message to standard error.</dd></dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
</dt><dd> <code>ngmultidec -n4 -l9e9 -c20e-12 -r5.3 -x5e12 -k0.7 -otest -L5.4 &gt; test.cir</code></dd></dl>
<h2>SEE ALSO</h2>
<pre>
<i>Efficient Transient Simulation of Lossy Interconnect</i>,
J.S. Roychowdhury and D.O. Pederson,
Proceedings of the Design Automation Conference,
pp. 740-745.
1991.
<code><a rel="nofollow" href="http://portal.acm.org/citation.cfm?doid=127601.127762">http://portal.acm.org/citation.cfm?doid=127601.127762</a></code>
</pre>
<p> <i><a href="/docs/linux/man/1-ngnutmeg/">ngnutmeg</a></i>(1), <i>ngproc2mod</i>(1), <i><a href="/docs/linux/man/1-ngsconvert/">ngsconvert</a></i>(1), <i><a href="/docs/linux/man/1-ngspice/">ngspice</a></i>(1), <i>nghelp</i>(1). </p>
