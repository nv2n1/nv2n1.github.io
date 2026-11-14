---
title: "mona(1)"
name: "mona"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mona/"
description: "mona – a decision procedure for the logics WS1S and WS2S"
---

<h2>NAME</h2>
<p> mona &#8211; a decision procedure for the logics WS1S and WS2S</p>
<h2>SYNOPSIS</h2>
<p> <code>mona </code> [ <i>options</i> ] <i>mona-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>MONA </code> is a tool that translates formulas in the logics WS1S or WS2S into finite-state automata represented by BDDs. The formulas may express search patterns, temporal properties of reactive systems, parse tree constraints, etc. MONA also analyses the automaton resulting from the compilation, and determines whether the formula is valid and, if the formula is not valid, generates a counter-example. </p>
<p> The MONA project is a research project at the BRICS Research Center at University of Aarhus, Denmark. </p>
<p> Full documentation, GPL source code, and related research papers are available from the MONA project home page at <code><a rel="nofollow" href="http://www.brics.dk/mona">http://www.brics.dk/mona</a></code></p>
<h2>OPTIONS</h2>
<dl>
<dt>-w</p>
<dd> Output whole automaton. Default is to only output its size.</p>
<dt>-n</p>
<dd> Don&#8217;t analyze automaton. Default is to analyze for validity and unsatisfiability and to generate a satisfying example and counter-example.</p>
<dt>-t</p>
<dd> Print elapsed time for each phase. If -s is also used, the time for each automaton operation is also printed.</p>
<dt>-s</p>
<dd> Print statistics. Prints information for each automaton operation and a summary.</p>
<dt>-i</p>
<dd> Print intermediate automata (implies -s).</p>
<dt>-d</p>
<dd> Dump AST, symboltable, and code DAG. Useful for debugging.</p>
<dt>-q</p>
<dd> Quiet, don&#8217;t print progress.</p>
<dt>-e</p>
<dd> Enable separate compilation. (See the MONALIB environment variable below.)</p>
<dt>-oN</p>
<dd> Code optimization level N (0=none, 1=safe, 2=heuristic) (default 1).</p>
<dt>-r</p>
<dd> Disable BDD index reordering, use order of declaration as index ordering. Default is to reorder BDD indices heuristically.</p>
<dt>-f</p>
<dd> Force normal tree-mode output style. Only applicable for WSRT mode.</p>
<dt>-m</p>
<dd> Alternative M2L-Str emulation (v1.3 style).</p>
<dt>-h</p>
<dd> Enable inherited acceptance analysis.</p>
<dt>-u</p>
<dd> Unrestrict output automata. Create conventional automata by converting &quot;don&#8217;t-care&quot; states to &quot;reject&quot; states and minimizes.</p>
<dt>-gw</p>
<dd> Output whole automaton in Graphviz format (implies -n -q). (Graphviz is available at <a rel="nofollow" href="http://www.research.att.com/sw/tools/graphviz/)">http://www.research.att.com/sw/tools/graphviz/)</a></p>
<dt>-gs</p>
<dd> Output satisfying example tree in Graphviz format (implies -q).</p>
<dt>-gc</p>
<dd> Output counter-example tree in Graphviz format (implies -q).</p>
<dt>-gd</p>
<dd> Dump code DAG in Graphviz format (implies -n -q).</p>
<dt>-xw</p>
<dd> Output whole automaton in external format (implies -n -q). &quot;External format&quot; is the format used by dfalib and gtalib, see the source package.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>MONALIB</p>
<dd> Defines the directory used for separate-compilation automata (default is current directory).</dl>
<h2>BUGS</h2>
<p> Please send bug reports to &lt;mona [at] brics.dk&gt;</p>
<h2>AUTHORS</h2>
<p> Anders Moeller &lt;amoeller [at] brics.dk&gt;, Nils Klarlund, Jacob Elgaard, Theis Rauhe, and Morten Biehl. </p>
<h2>Index</h2>
