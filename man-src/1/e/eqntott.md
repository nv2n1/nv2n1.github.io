---
title: "eqntott(1)"
name: "eqntott"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eqntott/"
description: "eqntott – generate truth table from Boolean equations"
---

<h2>NAME</h2>
<p> eqntott &#8211; generate truth table from Boolean equations</p>
<h2>SYNOPSIS</h2>
<p> <code>eqntott</code> [ <code>-l</code> ] [ <code>-f</code> ] [ <code>-s</code> ] [ <code>-r</code> ] [ <code>-R</code> ] ] [ -.key ] [ cc options ] [ files ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Eqntott</i> generates a truth table suitable for PLA programming from a set of Boolean equations which define the PLA outputs in terms of its inputs. When neither -f nor -s is specified, input and output variables must be mutually exclusive. If the -s option is given, an output variable may be used in an expression defining another output variable: the expression for the first output is substituted for the the name of that output when it is encountered. The -f option allows outputs to be defined in terms of their previous values in a synchronous system (e.g. an FSM): the same name appearing as both an input and an output may be thought of as referring to two distinct variables, or the same variable at two distinct times. (The -f and -s options are mutually exclusive.) </p>
<p> If the -r option is specified, <i>eqntott</i> will attempt to reduce the size of the truth table by merging minterms. The -R option (implies -r) forces <i>eqntott</i> to produce a truth table with no redundant minterms. The truth table generated does not represent a minimal covering of the truth functions, but does preserve some &#8220;don&#8217;t care&#8221; information for some other program to use. </p>
<p> If the -l option is specified, eqntott will output a truth table which includes the name of the pla and its inputs and outputs as specified in PLA(5). </p>
<p> The form that the output takes is controlled by the string <i>key,</i> described below. Input is taken from <i>files</i> (standard input default) and run through the C macro preprocessor of <i><a href="/docs/linux/man/1-cc/">cc</a></i>(1), to permit comments, file inclusion, macros, and conditional processing. The <i>cc options</i> -D, -I, and -U are recognized and passed on to the preprocessor.</p>
<h3>Equation Syntax:</h3>
<p> name = expression;</p>
<dl>
<dt>
</dt><dd> Associates a truth function defined by <i>expression </i> with the output <i>name,</i> both of which are defined below. If an output name is assigned more than one expression, the effect is identical to a single assignment to the output of the logical disjunction of all the original expressions.</dd></dl>
<p> NAME = name ;</p>
<dl>
<dt>
</dt><dd> Defines the name of the pla to be &#8220;name&#8221;. If not specified, the name of the pla is the name of the input file with any postfixes removed.</dd></dl>
<p> INORDER = name [name]&#8230; ;</p>
<dl>
<dt>
</dt><dd> Defines the order in which inputs appear in the truth table. If not specified, the order is that in which the inputs appear in the source.</dd></dl>
<p> OUTORDER = name [name]&#8230; ;</p>
<dl>
<dt>
</dt><dd> Defines the order in which outputs appear in the truth table. If not specified, the order is that in which the outputs appear in the source.</dd></dl>
<h3>Expression Syntax:</h3>
<p> name</p>
<dl>
<dt>
</dt><dd> A name is used to specify an input or output. The name must begin with a letter or underscore; subsequent characters may be letters, digits, underscores, asterisks, periods, square brackets, or angle brackets.</dd></dl>
<p> ZERO (or 0)</p>
<dl>
<dt>
</dt><dd> Builtin input that always has the value zero (false).</dd></dl>
<p> ONE (or 1)</p>
<dl>
<dt>
</dt><dd> Builtin input that always has the value one (true).</dd></dl>
<p> ?</p>
<dl>
<dt>
</dt><dd> Builtin input that always has the value &#8220;don&#8217;t care&#8221;.</dd></dl>
<p> ( expression )</p>
<dl>
<dt>
</dt><dd> Parenthesis may be used to change the order of evaluation.</dd></dl>
<p> ! expression</p>
<dl>
<dt>
</dt><dd> Gives the complement of <i>expression.</i></dd></dl>
<p> expression &amp; expression</p>
<dl>
<dt>
</dt><dd> Gives the logical conjunction of the two expressions. The &amp; operator associates left to right, and has the same precedence as !.</dd></dl>
<p> expression | expression</p>
<dl>
<dt>
</dt><dd> Gives the logical disjunction of the two expressions. The | operator also associates left to right, and has a lower precedence than &amp;.</dd></dl>
<h3>Output Format</h3>
<p> The output format may be controlled to a small extent using the character string <i>key.</i> The string is scanned left to right, and at each character code, a piece of output is generated corresponding to the character encountered. If -.key is not specified, the string &#8220;iopte&#8221; is used, or &#8220;iopfte&#8221; with the -f option. </p>
<dl>
<dt><i>code</i></dt>
<dd> <i>output generated</i> </dd>
<dt><code>e</code></dt>
<dd> <code>.e</code> </dd>
<dt><code>f</code></dt>
<dd> <code>.f</code><i> output-number input-number</i><br />
 (one line for each feedback path, numbers refer to Or- and And-plane truth table column numbers) <i><br />
 </i></dd>
<dt><code>h</code></dt>
<dd> a human readable version of the truth table (q.v.) </dd>
<dt><code>i</code></dt>
<dd> <code>.i</code><i> number-of-inputs</i> </dd>
<dt><code>I</code></dt>
<dd> <code>.I</code><i> input-name</i><br />
 (one line for each input, in order) </dd>
<dt><code>l</code></dt>
<dd> a truth table with the name of the pla, its inputs and its outputs </dd>
<dt><code>p</code></dt>
<dd> <code>.p</code><i> number-of-product-terms</i> </dd>
<dt><code>n</code></dt>
<dd> <code>.n</code><i> number-of-product-terms</i> </dd>
<dt><code>o</code></dt>
<dd> <code>.o</code><i> number-of-outputs</i> </dd>
<dt><code>O</code></dt>
<dd> <code>.O</code><i> output-name</i><br />
 (one line for each output, in order) </dd>
<dt><code>S</code></dt>
<dd> PLA connectivity summary </dd>
<dt><code>t</code></dt>
<dd> PLA personality matrix (q.v.) </dd>
<dt><code>v</code></dt>
<dd> eqntott version information
</dd></dl>
<p> The truth table (personality matrix) consists of a line for each minterm, beginning with that minterm and followed by the values of the various outputs. The minterm is composed of a single character (0, 1, or -) for each input in the conventional fashion. The output values are represented by one of the three characters (0, 1, or x). Some white space is added for readability&#8217;s sake. </p>
<p> In the human readable format, each line of output represents one term in the sum-of-products expression for an output. The line begins with the name of the output, which is enclosed in parentheses for the value &#8220;don&#8217;t care&#8221;. Then follow the names of the inputs in the product; complemented inputs are preceded by a !.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-cc/">cc</a></i>(1).</p>
<h2>DIAGNOSTICS</h2>
<p> Syntax errors are written to the standard error output and should be self-explanatory.</p>
<h2>BUGS</h2>
<p> -l should be the default, but some pla tools can&#8217;t handle the full format. Eqntott likes its options separately; i.e. -f -l works but -fl doesn&#8217;t.</p>
<h2>AUTHOR</h2>
<p> Bob Cmelik.<br />
 -l option added by Jeff Deutsch. </p>
<h2>Index</h2>
