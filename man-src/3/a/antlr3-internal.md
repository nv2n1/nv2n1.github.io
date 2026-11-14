---
title: "antlr3-internal(3)"
name: "antlr3-internal"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-internal/"
description: "ANTLR3_VECTOR_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_VECTOR_struct &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;</p>
<h3>Public Member Functions</h3>
<p> <code>void</code> (ANTLR3_CDECL *free)(struct <code>ANTLR3_VECTOR_struct</code> *vector) </p>
<h3>Data Fields</h3>
<p> <code>ANTLR3_UINT32</code>(* <code>add</code> )(struct <code>ANTLR3_VECTOR_struct</code> *vector, void *element, void(ANTLR3_CDECL *freeptr)(void *)) </p>
<p> void(* <code>clear</code> )(struct <code>ANTLR3_VECTOR_struct</code> *vector) </p>
<p> <code>ANTLR3_UINT32</code> <code>count</code><br />
 <i>Number of entries currently in the list;. </i><br />
 void(* <code>del</code> )(struct <code>ANTLR3_VECTOR_struct</code> *vector, <code>ANTLR3_UINT32</code> entry) </p>
<p> <code>pANTLR3_VECTOR_ELEMENT</code> <code>elements</code><br />
 <i>Array of pointers to vector elements. </i><br />
 <code>ANTLR3_UINT32</code> <code>elementsSize</code><br />
 <i>Total number of entries in elements at any point in time. </i><br />
 <code>ANTLR3_BOOLEAN</code> <code>factoryMade</code><br />
 <i>Indicates if the structure was made by a factory, in which case only the factory can free the memory for the actual vector, though the vector free function is called and will recurse through its entries calling any free pointers for each entry. </i><br />
 void *(* <code>get</code> )(struct <code>ANTLR3_VECTOR_struct</code> *vector, <code>ANTLR3_UINT32</code> entry) </p>
<p> <code>ANTLR3_VECTOR_ELEMENT</code> <code>internal</code> [ANTLR3_VECTOR_INTERNAL_SIZE]<br />
 <i>Many times, a vector holds just a few nodes in an AST and it is too much overhead to malloc the space for elements so at the expense of a few bytes of memory, we hold the first few elements internally. </i><br />
 void *(* <code>remove</code> )(struct <code>ANTLR3_VECTOR_struct</code> *vector, <code>ANTLR3_UINT32</code> entry) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>set</code> )(struct <code>ANTLR3_VECTOR_struct</code> *vector, <code>ANTLR3_UINT32</code> entry, void *element, void(ANTLR3_CDECL *freeptr)(void *), <code>ANTLR3_BOOLEAN</code> freeExisting) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>size</code> )(struct <code>ANTLR3_VECTOR_struct</code> *vector) </p>
<p> <code>ANTLR3_BOOLEAN</code>(* <code>swap</code> )(struct <code>ANTLR3_VECTOR_struct</code> *, <code>ANTLR3_UINT32</code> entry1, <code>ANTLR3_UINT32</code> entry2) </p>
<h2>Member Function Documentation</h2>
<h3>ANTLR3_VECTOR_struct::void (ANTLR3_CDECL * free)</h3>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_VECTOR_struct::add</code>)(struct <code>ANTLR3_VECTOR_struct</code> *vector, void *element, void(ANTLR3_CDECL *freeptr)(void *))</h3>
<p> Referenced by add(), addChild(), antlr3AsciiMark(), antlr3SetVectorApi(), antlr3StackPush(), fillBuffer(), freeNodeRS(), freeRS(), and replaceChildren().</p>
<h3>void(* <code>ANTLR3_VECTOR_struct::clear</code>)(struct <code>ANTLR3_VECTOR_struct</code> *vector)</h3>
<p> Referenced by antlr3SetVectorApi(), freeNodeRS(), freeRS(), returnVector(), and reuse().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_VECTOR_struct::count</code></h3>
<p> Number of entries currently in the list;. </p>
<p> Referenced by add(), antlr3AsciiMark(), antlr3RewriteRuleElementStreamNewAE(), antlr3SetVectorApi(), antlr3StackPop(), antlr3StackSize(), antlr3VectorAdd(), antlr3VectorClear(), antlr3VectorDel(), antlr3VectorFree(), antlr3VectorSet(), antlr3VectorSize(), antrl3VectorRemove(), freeNodeRS(), mismatchIsMissingToken(), size(), and sortVector().</p>
<h3>void(* <code>ANTLR3_VECTOR_struct::del</code>)(struct <code>ANTLR3_VECTOR_struct</code> *vector, <code>ANTLR3_UINT32</code> entry)</h3>
<p> Referenced by antlr3SetVectorApi(), antlr3StackPop(), and destroy().</p>
<h3><code>pANTLR3_VECTOR_ELEMENT</code> <code>ANTLR3_VECTOR_struct::elements</code></h3>
<p> Array of pointers to vector elements. </p>
<p> Referenced by antlr3SetVectorApi(), antlr3VectorAdd(), antlr3VectorClear(), antlr3VectorDel(), antlr3VectorFree(), antlr3VectorGet(), antlr3VectorResize(), antlr3VectorSet(), antlr3VectorSwap(), antrl3VectorRemove(), closeVectorFactory(), destroy(), freeNodeRS(), LB(), newVector(), replaceChildren(), and tokLT().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_VECTOR_struct::elementsSize</code></h3>
<p> Total number of entries in elements at any point in time. </p>
<p> Referenced by antlr3SetVectorApi(), antlr3VectorAdd(), antlr3VectorFree(), antlr3VectorResize(), antlr3VectorSet(), antlr3VectorSwap(), and closeVectorFactory().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_VECTOR_struct::factoryMade</code></h3>
<p> Indicates if the structure was made by a factory, in which case only the factory can free the memory for the actual vector, though the vector free function is called and will recurse through its entries calling any free pointers for each entry. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAEV(), antlr3SetVectorApi(), antlr3VectorFactoryNew(), antlr3VectorFree(), closeVectorFactory(), freeNodeRS(), freeRS(), and newVector().</p>
<h3>void*(* <code>ANTLR3_VECTOR_struct::get</code>)(struct <code>ANTLR3_VECTOR_struct</code> *vector, <code>ANTLR3_UINT32</code> entry)</h3>
<p> Referenced by _next(), addChild(), antlr3AsciiMark(), antlr3AsciiRewind(), antlr3SetVectorApi(), antlr3StackGet(), antlr3StackPop(), dupTree(), get(), getChild(), getFirstChildWithType(), LB(), replaceChildren(), and toStringTree().</p>
<h3><code>ANTLR3_VECTOR_ELEMENT</code> <code>ANTLR3_VECTOR_struct::internal</code>[ANTLR3_VECTOR_INTERNAL_SIZE]</h3>
<p> Many times, a vector holds just a few nodes in an AST and it is too much overhead to malloc the space for elements so at the expense of a few bytes of memory, we hold the first few elements internally. It means we must copy them when we grow beyond this initial size, but that is less overhead than the malloc/free callas we would otherwise require. </p>
<p> Referenced by antlr3SetVectorApi(), antlr3VectorResize(), and newVector().</p>
<h3>void*(* <code>ANTLR3_VECTOR_struct::remove</code>)(struct <code>ANTLR3_VECTOR_struct</code> *vector, <code>ANTLR3_UINT32</code> entry)</h3>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE(), antlr3SetVectorApi(), deleteChild(), and replaceChildren().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_VECTOR_struct::set</code>)(struct <code>ANTLR3_VECTOR_struct</code> *vector, <code>ANTLR3_UINT32</code> entry, void *element, void(ANTLR3_CDECL *freeptr)(void *), <code>ANTLR3_BOOLEAN</code> freeExisting)</h3>
<p> Referenced by antlr3SetVectorApi(), newRaw16(), newRaw8(), replaceChildren(), and setChild().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_VECTOR_struct::size</code>)(struct <code>ANTLR3_VECTOR_struct</code> *vector)</h3>
<p> Referenced by addChild(), antlr3SetVectorApi(), consume(), dupTree(), getChild(), getChildCount(), getFirstChildWithType(), hasNext(), replaceChildren(), and toStringTree().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_VECTOR_struct::swap</code>)(struct <code>ANTLR3_VECTOR_struct</code> *, <code>ANTLR3_UINT32</code> entry1, <code>ANTLR3_UINT32</code> entry2)</h3>
<p> Referenced by antlr3SetVectorApi(), and sortVector(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAV">Author</a></p>
<dd></dl>
