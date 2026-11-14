---
title: "antlr3-predict(3)"
name: "antlr3-predict"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-predict/"
description: "ANTLR3_CYCLIC_DFA_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_CYCLIC_DFA_struct &#8211; </p>
<p> Definition of a cyclic dfa structure such that it can be initialized at compile time and have only a single runtime function that can deal with all cyclic dfa structures and show Java how it is done ;-).</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3cyclicdfa.h">antlr3cyclicdfa.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> const <code>ANTLR3_INT32</code> *const <code>accept</code> </p>
<p> const <code>ANTLR3_INT32</code> <code>decisionNumber</code><br />
 <i>Decision number that a particular static structure represents. </i><br />
 const <code>pANTLR3_UCHAR</code> <code>description</code><br />
 <i>What this decision represents. </i><br />
 const <code>ANTLR3_INT32</code> *const <code>eof</code> </p>
<p> const <code>ANTLR3_INT32</code> *const <code>eot</code> </p>
<p> const <code>ANTLR3_INT32</code> *const <code>max</code> </p>
<p> const <code>ANTLR3_INT32</code> *const <code>min</code> </p>
<p> <code>ANTLR3_INT32</code>(* <code>predict</code> )(void *ctx, <code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> is, struct <code>ANTLR3_CYCLIC_DFA_struct</code> *dfa) </p>
<p> const <code>ANTLR3_INT32</code> *const <code>special</code> </p>
<p> <code>ANTLR3_INT32</code>(* <code>specialStateTransition</code> )(void *ctx, <code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> is, struct <code>ANTLR3_CYCLIC_DFA_struct</code> *dfa, <code>ANTLR3_INT32</code> s) </p>
<p> <code>ANTLR3_INT32</code>(* <code>specialTransition</code> )(void *ctx, <code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> is, struct <code>ANTLR3_CYCLIC_DFA_struct</code> *dfa, <code>ANTLR3_INT32</code> s) </p>
<p> const <code>ANTLR3_INT32</code> *const *const <code>transition</code> </p>
<h2>Detailed Description</h2>
<p> Definition of a cyclic dfa structure such that it can be initialized at compile time and have only a single runtime function that can deal with all cyclic dfa structures and show Java how it is done ;-).</p>
<h2>Field Documentation</h2>
<h3>const <code>ANTLR3_INT32</code>* const <code>ANTLR3_CYCLIC_DFA_struct::accept</code></h3>
<p> Referenced by antlr3dfapredict().</p>
<h3>const <code>ANTLR3_INT32</code> <code>ANTLR3_CYCLIC_DFA_struct::decisionNumber</code></h3>
<p> Decision number that a particular static structure represents. </p>
<p> Referenced by noViableAlt().</p>
<h3>const <code>pANTLR3_UCHAR</code> <code>ANTLR3_CYCLIC_DFA_struct::description</code></h3>
<p> What this decision represents. </p>
<p> Referenced by noViableAlt().</p>
<h3>const <code>ANTLR3_INT32</code>* const <code>ANTLR3_CYCLIC_DFA_struct::eof</code></h3>
<p> Referenced by antlr3dfapredict().</p>
<h3>const <code>ANTLR3_INT32</code>* const <code>ANTLR3_CYCLIC_DFA_struct::eot</code></h3>
<p> Referenced by antlr3dfapredict().</p>
<h3>const <code>ANTLR3_INT32</code>* const <code>ANTLR3_CYCLIC_DFA_struct::max</code></h3>
<h3>const <code>ANTLR3_INT32</code>* const <code>ANTLR3_CYCLIC_DFA_struct::min</code></h3>
<p> Referenced by antlr3dfapredict().</p>
<h3><code>ANTLR3_INT32</code>(* <code>ANTLR3_CYCLIC_DFA_struct::predict</code>)(void *ctx, <code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> is, struct <code>ANTLR3_CYCLIC_DFA_struct</code> *dfa)</h3>
<h3>const <code>ANTLR3_INT32</code>* const <code>ANTLR3_CYCLIC_DFA_struct::special</code></h3>
<p> Referenced by antlr3dfapredict().</p>
<h3><code>ANTLR3_INT32</code>(* <code>ANTLR3_CYCLIC_DFA_struct::specialStateTransition</code>)(void *ctx, <code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> is, struct <code>ANTLR3_CYCLIC_DFA_struct</code> *dfa, <code>ANTLR3_INT32</code> s)</h3>
<p> Referenced by antlr3dfapredict().</p>
<h3><code>ANTLR3_INT32</code>(* <code>ANTLR3_CYCLIC_DFA_struct::specialTransition</code>)(void *ctx, <code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> is, struct <code>ANTLR3_CYCLIC_DFA_struct</code> *dfa, <code>ANTLR3_INT32</code> s)</h3>
<h3>const <code>ANTLR3_INT32</code>* const* const <code>ANTLR3_CYCLIC_DFA_struct::transition</code></h3>
<p> Referenced by antlr3dfapredict(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAS">Author</a></p>
<dd></dl>
