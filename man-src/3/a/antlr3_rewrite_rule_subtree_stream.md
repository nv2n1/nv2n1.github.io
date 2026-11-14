---
title: "antlr3_rewrite_rule_subtree_stream(3)"
name: "antlr3_rewrite_rule_subtree_stream"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_rewrite_rule_subtree_stream/"
description: "include/antlr3rewritestreams.h –"
---

<p>include/antlr3rewritestreams.h &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3commontreeadaptor.h">antlr3commontreeadaptor.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3baserecognizer.h">antlr3baserecognizer.h</a>&gt; </p>
<h3>Data Structures</h3>
<p>struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code><br />
 <i>A generic list of elements tracked in an alternative to be used in a -&gt; rewrite rule. </i></p>
<h3>Typedefs</h3>
<p>typedef struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM</code><br />
 <i>A generic list of elements tracked in an alternative to be used in a -&gt; rewrite rule. </i><br />
 typedef struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> <code>ANTLR3_REWRITE_RULE_NODE_STREAM</code><br />
 <i>This is an implementation of a node stream, which is basically an element stream that deals with tree nodes only. </i><br />
 typedef struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> <code>ANTLR3_REWRITE_RULE_SUBTREE_STREAM</code><br />
 <i>This is an implementation of a subtree stream which is a set of trees modelled as an element stream. </i><br />
 typedef struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> <code>ANTLR3_REWRITE_RULE_TOKEN_STREAM</code><br />
 <i>This is an implementation of a token stream, which is basically an element stream that deals with tokens only. </i></p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM</code>&quot; </p>
<p> A generic list of elements tracked in an alternative to be used in a -&gt; rewrite rule. In the C implementation, all tree oriented streams return a pointer to the same type: pANTLR3_BASE_TREE. Anything that has subclassed from this still passes this type, within which there is a super pointer, which points to it&#8217;s own data and methods. Hence we do not need to implement this as the equivalent of an abstract class, but just fill in the appropriate interface as usual with this model. </p>
<p> Once you start <code>next()</code>ing, do not try to add more elements. It will break the cursor tracking I believe. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>pANTLR3_REWRITE_RULE_NODE_STREAM</code> </p>
<p> <code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> </p>
<p> <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code></dl>
<p> TODO: add mechanism to detect/puke on modification after reading from stream</p>
<h3>typedef struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> <code>ANTLR3_REWRITE_RULE_NODE_STREAM</code></h3>
<p>This is an implementation of a node stream, which is basically an element stream that deals with tree nodes only.</p>
<h3>typedef struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> <code>ANTLR3_REWRITE_RULE_SUBTREE_STREAM</code></h3>
<p>This is an implementation of a subtree stream which is a set of trees modelled as an element stream.</p>
<h3>typedef struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> <code>ANTLR3_REWRITE_RULE_TOKEN_STREAM</code></h3>
<p>This is an implementation of a token stream, which is basically an element stream that deals with tokens only.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
