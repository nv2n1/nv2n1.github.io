---
title: "antlr3-newtree(3)"
name: "antlr3-newtree"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-newtree/"
description: "ANTLR3_ARBORETUM_struct –"
---

<p>ANTLR3_ARBORETUM_struct &#8211; </p>
<p> ANTLR3 Tree factory interface to create lots of trees efficiently rather than creating and freeing lots of little bits of memory.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3commontree.h">antlr3commontree.h</a>&gt;</p>
<h3>Data Fields</h3>
<p>void(* <code>close</code> )(struct <code>ANTLR3_ARBORETUM_struct</code> *factory)<br />
 <i>Pointer to a function the destroys the factory. </i><br />
 <code>pANTLR3_BASE_TREE</code>(* <code>newFromToken</code> )(struct <code>ANTLR3_ARBORETUM_struct</code> *factory, <code>pANTLR3_COMMON_TOKEN</code> token) </p>
<p> <code>pANTLR3_BASE_TREE</code>(* <code>newFromTree</code> )(struct <code>ANTLR3_ARBORETUM_struct</code> *factory, <code>pANTLR3_COMMON_TREE</code> tree) </p>
<p> <code>pANTLR3_BASE_TREE</code>(* <code>newTree</code> )(struct <code>ANTLR3_ARBORETUM_struct</code> *factory)<br />
 <i>Pointer to a function that returns a new tree. </i><br />
 <code>ANTLR3_UINT32</code> <code>nextTree</code><br />
 <i>The next token to throw out from the pool, will cause a new pool allocation if this exceeds the available tokenCount. </i><br />
 <code>pANTLR3_STACK</code> <code>nilStack</code><br />
 <i>A resuse stack for reclaiming Nil nodes that were used in rewrites and are now dead. </i><br />
 <code>pANTLR3_COMMON_TREE</code> * <code>pools</code><br />
 <i>Pointers to the array of tokens that this factory has produced so far. </i><br />
 <code>ANTLR3_INT32</code> <code>thisPool</code><br />
 <i>Current pool tokens we are allocating from. </i><br />
 <code>ANTLR3_COMMON_TREE</code> <code>unTruc</code><br />
 <i>Trick to initialize tokens and their API quickly, we set up this token when the factory is created, then just copy the memory it uses into the new token. </i><br />
 <code>pANTLR3_VECTOR_FACTORY</code> <code>vFactory</code><br />
 <i>Pointer to a vector factory that is used to create child list vectors for any child nodes that need them. </i></p>
<h2>Detailed Description</h2>
<p>ANTLR3 Tree factory interface to create lots of trees efficiently rather than creating and freeing lots of little bits of memory.</p>
<h2>Field Documentation</h2>
<h3>void(* <code>ANTLR3_ARBORETUM_struct::close</code>)(struct <code>ANTLR3_ARBORETUM_struct</code> *factory)</h3>
<p>Pointer to a function the destroys the factory. </p>
<p> Referenced by antlr3ArboretumNew(), and ctaFree().</p>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_ARBORETUM_struct::newFromToken</code>)(struct <code>ANTLR3_ARBORETUM_struct</code> *factory, <code>pANTLR3_COMMON_TOKEN</code> token)</h3>
<p>Referenced by antlr3ArboretumNew().</p>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_ARBORETUM_struct::newFromTree</code>)(struct <code>ANTLR3_ARBORETUM_struct</code> *factory, <code>pANTLR3_COMMON_TREE</code> tree)</h3>
<p>Referenced by antlr3ArboretumNew(), and dupNode().</p>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_ARBORETUM_struct::newTree</code>)(struct <code>ANTLR3_ARBORETUM_struct</code> *factory)</h3>
<p>Pointer to a function that returns a new tree. </p>
<p> Referenced by antlr3ArboretumNew(), newFromToken(), and newFromTree().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_ARBORETUM_struct::nextTree</code></h3>
<p>The next token to throw out from the pool, will cause a new pool allocation if this exceeds the available tokenCount. </p>
<p> Referenced by newPool(), and newPoolTree().</p>
<h3><code>pANTLR3_STACK</code> <code>ANTLR3_ARBORETUM_struct::nilStack</code></h3>
<p>A resuse stack for reclaiming Nil nodes that were used in rewrites and are now dead. The <code>nilNode()</code> method will eat one of these before creating a new node. </p>
<p> Referenced by antlr3ArboretumNew(), factoryClose(), newPoolTree(), and reuse().</p>
<h3><code>pANTLR3_COMMON_TREE</code>* <code>ANTLR3_ARBORETUM_struct::pools</code></h3>
<p>Pointers to the array of tokens that this factory has produced so far. </p>
<p> Referenced by antlr3ArboretumNew(), factoryClose(), newPool(), and newPoolTree().</p>
<h3><code>ANTLR3_INT32</code> <code>ANTLR3_ARBORETUM_struct::thisPool</code></h3>
<p>Current pool tokens we are allocating from. </p>
<p> Referenced by antlr3ArboretumNew(), factoryClose(), newPool(), and newPoolTree().</p>
<h3><code>ANTLR3_COMMON_TREE</code> <code>ANTLR3_ARBORETUM_struct::unTruc</code></h3>
<p>Trick to initialize tokens and their API quickly, we set up this token when the factory is created, then just copy the memory it uses into the new token. </p>
<p> Referenced by antlr3ArboretumNew(), and newPoolTree().</p>
<h3><code>pANTLR3_VECTOR_FACTORY</code> <code>ANTLR3_ARBORETUM_struct::vFactory</code></h3>
<p>Pointer to a vector factory that is used to create child list vectors for any child nodes that need them. This means that we auto track the vectors and auto free them when we close the factory. It also means that all rewriting trees can use the same tree factory and the same vector factory and we do not dup any nodes unless we must do so explicitly because of context such as an empty rewrite stream and -&gt;IMAGINARY[ID] so on. This makes memory tracking much simpler and tempts no errors. </p>
<p> Referenced by antlr3ArboretumNew(), and factoryClose(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
