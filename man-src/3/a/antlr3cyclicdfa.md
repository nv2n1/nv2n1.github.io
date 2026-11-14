---
title: "antlr3cyclicdfa(3)"
name: "antlr3cyclicdfa"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3cyclicdfa/"
description: "include/antlr3cyclicdfa.h –"
---

<h2 class="name">NAME</h2>
<p> include/antlr3cyclicdfa.h &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3baserecognizer.h">antlr3baserecognizer.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3intstream.h">antlr3intstream.h</a>&gt; </p>
<h3>Data Structures</h3>
<p> struct <code>ANTLR3_CYCLIC_DFA_struct</code><br />
 <i>Definition of a cyclic dfa structure such that it can be initialized at compile time and have only a single runtime function that can deal with all cyclic dfa structures and show Java how it is done ;-). </i></p>
<h3>Typedefs</h3>
<p> typedef struct <code>ANTLR3_CYCLIC_DFA_struct</code> <code>ANTLR3_CYCLIC_DFA</code><br />
 <i>Definition of a cyclic dfa structure such that it can be initialized at compile time and have only a single runtime function that can deal with all cyclic dfa structures and show Java how it is done ;-). </i><br />
 typedef <code>ANTLR3_INT32</code>(* <code>CDFA_SPECIAL_FUNC</code> )(void *, <code>pANTLR3_BASE_RECOGNIZER</code>, <code>pANTLR3_INT_STREAM</code>, struct <code>ANTLR3_CYCLIC_DFA_struct</code> *, <code>ANTLR3_INT32</code>) </p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_CYCLIC_DFA_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_CYCLIC_DFA</code>&quot; </p>
<p> Definition of a cyclic dfa structure such that it can be initialized at compile time and have only a single runtime function that can deal with all cyclic dfa structures and show Java how it is done ;-).</p>
<h3>typedef <code>ANTLR3_INT32</code>(* <code>CDFA_SPECIAL_FUNC</code>)(void *, <code>pANTLR3_BASE_RECOGNIZER</code>, <code>pANTLR3_INT_STREAM</code>, struct <code>ANTLR3_CYCLIC_DFA_struct</code> *, <code>ANTLR3_INT32</code>)</h3>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
