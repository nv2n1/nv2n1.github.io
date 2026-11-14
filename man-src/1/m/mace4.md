---
title: "mace4(1)"
name: "mace4"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mace4/"
description: "mace4 – searches for finite countermodels of first-order statements"
---

<h2>NAME</h2>
<p> mace4 &#8211; searches for finite countermodels of first-order statements</p>
<h2>SYNOPSIS</h2>
<p> <code>mace4</code> [<i>options</i>] &lt; <i>input-file</i> &gt; <i>output-file</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>mace4</code> command. </p>
<p> The program <code>mace4</code> searches for finite structures satisfying first-order and equational statements, the same kind of statement that <code><a href="/docs/linux/man/1-prover9/">prover9</a></code>(1) accepts. If the statement is the denial of some conjecture, any structures found by <code>mace4</code> are counterexamples to the conjecture. <code>mace4</code> can be a valuable complement to <code><a href="/docs/linux/man/1-prover9/">prover9</a></code>(1), looking for counterexamples before (or at the same time as) using <code><a href="/docs/linux/man/1-prover9/">prover9</a></code>(1) to search for a proof. It can also be used to help debug input clauses and formulas for <code><a href="/docs/linux/man/1-prover9/">prover9</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. Options override the equivalent settings given in the input file. To set or clear a flag, you must give 1 or 0 as the value.</p>
<dl>
<dt><code>-help</code></p>
<dd> This tells <code>mace4</code> to print a summary of these command-line options.</p>
<dt><code>-n </code><i>n</i></p>
<dd> This gives the starting domain size for the search. The default value is 2. If you also give an <code>-N</code> option, <code>mace4</code> will iterate domain sizes up through the <code>-N</code> value, using an increment given by the <code>-I</code> value. Otherwise, <code>mace4</code> will search only for the <code>-n</code> value.</p>
<dt><code>-N </code><i>n</i></p>
<dd> This gives the ending domain size for the search. The default is 10.</p>
<dt><code>-i </code><i>n</i></p>
<dd> This gives the domain size increment for the search. The default is 1.</p>
<dt><code>-q </code><i>n</i></p>
<dd> This flag overrides the parameter iterate. It says to try the sizes that are prime numbers, from <code>-n</code> up through <code>-N</code>.</p>
<dt><code>-m </code><i>n</i></p>
<dd> Stop searching when the <i>n</i>th structure has been found. The default is 1.</p>
<dt><code>-t </code><i>n</i></p>
<dd> Stop searching after <i>n</i> seconds.</p>
<dt><code>-s </code><i>n</i></p>
<dd> Allow at most <i>n</i> seconds for each domain size. The parameter can be used (together with <code>-t</code>) to give an overall time limit.</p>
<dt><code>-b </code><i>n</i></p>
<dd> Stop searching when (about) <i>n</i> megabytes of memory have been used.</p>
<dt><code>-V </code><i>n</i></p>
<dd> A rule is needed for distinguishing variables from constants in clauses and formulas with free variables. If this flag is clear, variables start with (lower case) `u&#8217; through `z&#8217;. If this flag is set, variables in clauses start with (upper case) `A&#8217; through `Z&#8217; or `_&#8217;.</p>
<dt><code>-P </code><i>n</i></p>
<dd> If this flag is set, all structures that are found are printed in `standard&#8217; form, which means they are suitable as input to other LADR programs such as <code><a href="/docs/linux/man/1-isofilter/">isofilter</a></code>(1) and <code><a href="/docs/linux/man/1-interpformat/">interpformat</a></code>(1).</p>
<dt><code>-p </code><i>n</i></p>
<dd> If this flag is set, and if <code>-P</code> is clear, all structures that are found are printed in a tabular form.</p>
<dt><code>-R </code><i>n</i></p>
<dd> If this flag is set, a ring structure is is applied to the search. The operations {+,-,*} are assumed to be the ring of integers (mod domain_size). This method puts a tight constraint on the search, allowing much larger structures to be investigated.</p>
<dt><code>-v </code><i>n</i></p>
<dd> If this flag is set, the output file receives information about the search, including the initial partial model (the part of the model that can be determined before backtracking starts) and timing and other statistics for each domain size. (It does not give a trace of the backtracking, so it does not consume a lot of file space.)</p>
<dt><code>-T </code><i>n</i></p>
<dd> If the trace flag is set, detailed information about the search, including a trace of all assignments and backtracking, is printed to the standard output. This flag causes a lot of output, so it should be used only on small searches.</dl>
<p> There also exist a number of advanced options, which are used for experimentation with search methods. They can be ignored by nearly all users. For descriptions of these options, see the original <code>mace4</code> manual.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-prover9/">prover9</a></code>(1).<br />
 Full documentation for <code>mace4</code> is found in the <code>prover9</code> manual, available on Debian systems in the <i>prover9-doc</i> package at <i>/usr/share/doc/prover9-doc/manual/index.html</i>.<br />
 The original <code>mace4</code> manual, which can be downloaded at <a rel="nofollow" href="http://www.cs.unm.edu/~mccune/prover9/mace4.pdf">http://www.cs.unm.edu/~mccune/prover9/mace4.pdf</a></p>
<h2>AUTHOR</h2>
<p> <code>mace4</code> was written by William McCune &lt;mccune [at] cs.unm.edu&gt; </p>
<p> This manual page was written by Peter Collingbourne &lt;pcc03 [at] doc.ic.ac.uk&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
