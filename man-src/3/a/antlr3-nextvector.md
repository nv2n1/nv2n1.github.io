---
title: "antlr3-nextvector(3)"
name: "antlr3-nextvector"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-nextvector/"
description: "ANTLR3_VECTOR_FACTORY_struct –"
---

<p>ANTLR3_VECTOR_FACTORY_struct &#8211; </p>
<p> Structure that tracks vectors in a vector and auto deletes the vectors in the vector factory when closed.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;</p>
<h3>Data Fields</h3>
<p>void(* <code>close</code> )(struct <code>ANTLR3_VECTOR_FACTORY_struct</code> *factory)<br />
 <i>Function to close the vector factory. </i><br />
 <code>pANTLR3_STACK</code> <code>freeStack</code><br />
 <i>Consumers from the factory can release a factory produced vector back to the factory so that it may be reused (and thus conserve memory) by another caller. </i><br />
 <code>pANTLR3_VECTOR</code>(* <code>newVector</code> )(struct <code>ANTLR3_VECTOR_FACTORY_struct</code> *factory)<br />
 <i>Function to supply a new vector. </i><br />
 <code>ANTLR3_UINT32</code> <code>nextVector</code><br />
 <i>The next vector available in the pool. </i><br />
 <code>pANTLR3_VECTOR</code> * <code>pools</code><br />
 <i>List of all vector pools allocated so far. </i><br />
 void(* <code>returnVector</code> )(struct <code>ANTLR3_VECTOR_FACTORY_struct</code> *factory, <code>pANTLR3_VECTOR</code> vector)<br />
 <i>Function to return a vector to the factory for reuse. </i><br />
 <code>ANTLR3_INT32</code> <code>thisPool</code><br />
 <i>Count of the vector pools allocated so far (current active pool). </i><br />
 <code>ANTLR3_VECTOR</code> <code>unTruc</code><br />
 <i>Trick to quickly initialize a new vector via memcpy and not a function call. </i></p>
<h2>Detailed Description</h2>
<p>Structure that tracks vectors in a vector and auto deletes the vectors in the vector factory when closed.</p>
<h2>Field Documentation</h2>
<h3>void(* <code>ANTLR3_VECTOR_FACTORY_struct::close</code>)(struct <code>ANTLR3_VECTOR_FACTORY_struct</code> *factory)</h3>
<p>Function to close the vector factory. </p>
<p> Referenced by antlr3VectorFactoryNew(), and factoryClose().</p>
<h3><code>pANTLR3_STACK</code> <code>ANTLR3_VECTOR_FACTORY_struct::freeStack</code></h3>
<p>Consumers from the factory can release a factory produced vector back to the factory so that it may be reused (and thus conserve memory) by another caller. The available vectors are stored here. Note that the only vectors avaible in the free chain are produced by this factory, so they need not be explicitly freed when the factory is closed. </p>
<p> Referenced by antlr3VectorFactoryNew(), closeVectorFactory(), newVector(), and returnVector().</p>
<h3><code>pANTLR3_VECTOR</code>(* <code>ANTLR3_VECTOR_FACTORY_struct::newVector</code>)(struct <code>ANTLR3_VECTOR_FACTORY_struct</code> *factory)</h3>
<p>Function to supply a new vector. </p>
<p> Referenced by add(), and antlr3VectorFactoryNew().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_VECTOR_FACTORY_struct::nextVector</code></h3>
<p>The next vector available in the pool. </p>
<p> Referenced by closeVectorFactory(), newPool(), and newVector().</p>
<h3><code>pANTLR3_VECTOR</code>* <code>ANTLR3_VECTOR_FACTORY_struct::pools</code></h3>
<p>List of all vector pools allocated so far. </p>
<p> Referenced by antlr3VectorFactoryNew(), closeVectorFactory(), newPool(), and newVector().</p>
<h3>void(* <code>ANTLR3_VECTOR_FACTORY_struct::returnVector</code>)(struct <code>ANTLR3_VECTOR_FACTORY_struct</code> *factory, <code>pANTLR3_VECTOR</code> vector)</h3>
<p>Function to return a vector to the factory for reuse. </p>
<p> Referenced by antlr3VectorFactoryNew(), freeNodeRS(), and freeRS().</p>
<h3><code>ANTLR3_INT32</code> <code>ANTLR3_VECTOR_FACTORY_struct::thisPool</code></h3>
<p>Count of the vector pools allocated so far (current active pool). </p>
<p> Referenced by antlr3VectorFactoryNew(), closeVectorFactory(), newPool(), and newVector().</p>
<h3><code>ANTLR3_VECTOR</code> <code>ANTLR3_VECTOR_FACTORY_struct::unTruc</code></h3>
<p>Trick to quickly initialize a new vector via memcpy and not a function call. </p>
<p> Referenced by antlr3VectorFactoryNew(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
