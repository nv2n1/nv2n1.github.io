---
title: "antlr3_stack_struct(3)"
name: "antlr3_stack_struct"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_stack_struct/"
description: "ANTLR3_STACK_struct –"
---

<p>ANTLR3_STACK_struct &#8211; </p>
<p> Structure that represents a Stack collection.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;</p>
<h3>Data Fields</h3>
<p>void(* <code>free</code> )(struct <code>ANTLR3_STACK_struct</code> *stack) </p>
<p> void *(* <code>get</code> )(struct <code>ANTLR3_STACK_struct</code> *stack, <code>ANTLR3_INTKEY</code> key) </p>
<p> void *(* <code>peek</code> )(struct <code>ANTLR3_STACK_struct</code> *stack) </p>
<p> void *(* <code>pop</code> )(struct <code>ANTLR3_STACK_struct</code> *stack) </p>
<p> <code>ANTLR3_BOOLEAN</code>(* <code>push</code> )(struct <code>ANTLR3_STACK_struct</code> *stack, void *element, void(ANTLR3_CDECL *freeptr)(void *)) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>size</code> )(struct <code>ANTLR3_STACK_struct</code> *stack) </p>
<p> void * <code>top</code><br />
 <i>Used for quick access to the top of the stack. </i><br />
 <code>pANTLR3_VECTOR</code> <code>vector</code><br />
 <i>List that supports the stack structure. </i></p>
<h2>Detailed Description</h2>
<p>Structure that represents a Stack collection.</p>
<h2>Field Documentation</h2>
<h3>void(* <code>ANTLR3_STACK_struct::free</code>)(struct <code>ANTLR3_STACK_struct</code> *stack)</h3>
<p>Referenced by antlr3CommonTreeNodeStreamFree(), antlr3StackNew(), closeVectorFactory(), factoryClose(), freeLexer(), freeParser(), and reset().</p>
<h3>void*(* <code>ANTLR3_STACK_struct::get</code>)(struct <code>ANTLR3_STACK_struct</code> *stack, <code>ANTLR3_INTKEY</code> key)</h3>
<p>Referenced by antlr3StackNew(), and combineFollows().</p>
<h3>void*(* <code>ANTLR3_STACK_struct::peek</code>)(struct <code>ANTLR3_STACK_struct</code> *stack)</h3>
<p>Referenced by antlr3StackNew(), newPoolTree(), and newVector().</p>
<h3>void*(* <code>ANTLR3_STACK_struct::pop</code>)(struct <code>ANTLR3_STACK_struct</code> *stack)</h3>
<p>Referenced by antlr3StackNew(), newPoolTree(), newVector(), and popCharStream().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_STACK_struct::push</code>)(struct <code>ANTLR3_STACK_struct</code> *stack, void *element, void(ANTLR3_CDECL *freeptr)(void *))</h3>
<p>Referenced by antlr3StackNew(), pushCharStream(), returnVector(), and reuse().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_STACK_struct::size</code>)(struct <code>ANTLR3_STACK_struct</code> *stack)</h3>
<p>Referenced by antlr3StackNew(), combineFollows(), nextToken(), and popCharStream().</p>
<h3>void* <code>ANTLR3_STACK_struct::top</code></h3>
<p>Used for quick access to the top of the stack. </p>
<p> Referenced by antlr3StackFree(), antlr3StackNew(), antlr3StackPeek(), antlr3StackPop(), antlr3StackPush(), and popCharStream().</p>
<h3><code>pANTLR3_VECTOR</code> <code>ANTLR3_STACK_struct::vector</code></h3>
<p>List that supports the stack structure. </p>
<p> Referenced by antlr3StackFree(), antlr3StackGet(), antlr3StackNew(), antlr3StackPop(), antlr3StackPush(), antlr3StackSize(), and mismatchIsMissingToken(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
