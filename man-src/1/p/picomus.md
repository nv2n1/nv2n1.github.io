---
title: "picomus(1)"
name: "picomus"
section: "1"
letter: "p"
url: "/docs/linux/man/1-picomus/"
description: "picomus – Minimal Unsatisfiable Core (MUS) generator"
---

<h2>NAME</h2>
<p> picomus &#8211; Minimal Unsatisfiable Core (MUS) generator</p>
<h2>SYNOPSIS</h2>
<p> <code>picomus</code> [<i>OPTION</i>]&#8230; [<i>INPUT</i> [<i>OUTPUT</i>]]</p>
<h2>DESCRIPTION</h2>
<p> PicoMUS is a satisfiability (SAT) solver that generates a minimal unsatisfiable core, using the PicoSAT library. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> print this command line option summary and exit </p>
<dt><code>-v</code></p>
<dd> enable verbose output </p>
</dl>
<p> If no input filename is given, or the input filename is &quot;-&quot;, then standard input is used. If the output filename is &quot;-&quot;, then standard output is used. If no output filename is given, then the MUS is computed but not printed. </p>
<h2>CONFORMING TO</h2>
<p> This program uses DIMACS CNF format as input. The output conforms to the standard SAT solver format used at SAT competitions. </p>
<h2>EXIT STATUS</h2>
<p> The output is a number of lines. Most of these will begin with &quot;c&quot; (comment), and give detailed technical information. The output line beginning with &quot;s&quot; declares whether or not it is satisfiable. The line &quot;s SATISFIABLE&quot; is produced if it is satisfiable (exit status 10), and &quot;s UNSATISFIABLE&quot; is produced if it is not satisfiable (exit status 20). </p>
<h2>AUTHORS</h2>
<p> picomus was written by Armin Biere &lt;biere [at] jku.at&gt; </p>
<p> This man page was written by Jerry James. It is released to the public domain; you may use it in any way you wish. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-picosat/">picosat</a></i>(1), <i><a href="/docs/linux/man/1-minisat2/">minisat2</a></i>(1). </p>
<h2>Index</h2>
