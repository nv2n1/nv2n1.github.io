---
title: "tree(3)"
name: "tree"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tree/"
description: "SPLAY_PROTOTYPE SPLAY_GENERATE SPLAY_ENTRY SPLAY_HEAD SPLAY_INITIALIZER SPLAY_ROOT SPLAY_EMPTY SPLAY_NEXT SPLAY_MIN SPLAY_MAX SPLAY_FIND SPLAY_LEFT SPLAY_RIGHT SPLAY_FOREACH SPLAY_INIT SPLAY_INSERT..."
---

<h2 class="name">NAME</h2>
<p> <code>SPLAY_PROTOTYPE</code> <code>SPLAY_GENERATE</code> <code>SPLAY_ENTRY</code> <code>SPLAY_HEAD</code> <code>SPLAY_INITIALIZER</code> <code>SPLAY_ROOT</code> <code>SPLAY_EMPTY</code> <code>SPLAY_NEXT</code> <code>SPLAY_MIN</code> <code>SPLAY_MAX</code> <code>SPLAY_FIND</code> <code>SPLAY_LEFT</code> <code>SPLAY_RIGHT</code> <code>SPLAY_FOREACH</code> <code>SPLAY_INIT</code> <code>SPLAY_INSERT</code> <code>SPLAY_REMOVE</code> <code>RB_PROTOTYPE</code> <code>RB_PROTOTYPE_STATIC</code> <code>RB_GENERATE</code> <code>RB_GENERATE_STATIC</code> <code>RB_ENTRY</code> <code>RB_HEAD</code> <code>RB_INITIALIZER</code> <code>RB_ROOT</code> <code>RB_EMPTY</code> <code>RB_NEXT</code> <code>RB_PREV</code> <code>RB_MIN</code> <code>RB_MAX</code> <code>RB_FIND</code> <code>RB_NFIND</code> <code>RB_LEFT</code> <code>RB_RIGHT</code> <code>RB_PARENT</code> <code>RB_FOREACH</code> <code>RB_FOREACH_REVERSE</code> <code>RB_INIT</code> <code>RB_INSERT</code> <code>RB_REMOVE</code> &#8211; implementations of splay and red-black trees </p>
<h2>SYNOPSIS</h2>
<p> In bsd/sys/tree.h Fn SPLAY_PROTOTYPE NAME TYPE FIELD CMP Fn SPLAY_GENERATE NAME TYPE FIELD CMP Fn SPLAY_ENTRY TYPE Fn SPLAY_HEAD HEADNAME TYPE Ft struct TYPE * Fn SPLAY_INITIALIZER SPLAY_HEAD *head Fn SPLAY_ROOT SPLAY_HEAD *head Ft bool Fn SPLAY_EMPTY SPLAY_HEAD *head Ft struct TYPE * Fn SPLAY_NEXT NAME SPLAY_HEAD *head struct TYPE *elm Ft struct TYPE * Fn SPLAY_MIN NAME SPLAY_HEAD *head Ft struct TYPE * Fn SPLAY_MAX NAME SPLAY_HEAD *head Ft struct TYPE * Fn SPLAY_FIND NAME SPLAY_HEAD *head struct TYPE *elm Ft struct TYPE * Fn SPLAY_LEFT struct TYPE *elm SPLAY_ENTRY NAME Ft struct TYPE * Fn SPLAY_RIGHT struct TYPE *elm SPLAY_ENTRY NAME Fn SPLAY_FOREACH VARNAME NAME SPLAY_HEAD *head Ft void Fn SPLAY_INIT SPLAY_HEAD *head Ft struct TYPE * Fn SPLAY_INSERT NAME SPLAY_HEAD *head struct TYPE *elm Ft struct TYPE * Fn SPLAY_REMOVE NAME SPLAY_HEAD *head struct TYPE *elm Fn RB_PROTOTYPE NAME TYPE FIELD CMP Fn RB_PROTOTYPE_STATIC NAME TYPE FIELD CMP Fn RB_GENERATE NAME TYPE FIELD CMP Fn RB_GENERATE_STATIC NAME TYPE FIELD CMP Fn RB_ENTRY TYPE Fn RB_HEAD HEADNAME TYPE Fn RB_INITIALIZER RB_HEAD *head Ft struct TYPE * Fn RB_ROOT RB_HEAD *head Ft bool Fn RB_EMPTY RB_HEAD *head Ft struct TYPE * Fn RB_NEXT NAME RB_HEAD *head struct TYPE *elm Ft struct TYPE * Fn RB_PREV NAME RB_HEAD *head struct TYPE *elm Ft struct TYPE * Fn RB_MIN NAME RB_HEAD *head Ft struct TYPE * Fn RB_MAX NAME RB_HEAD *head Ft struct TYPE * Fn RB_FIND NAME RB_HEAD *head struct TYPE *elm Ft struct TYPE * Fn RB_NFIND NAME RB_HEAD *head struct TYPE *elm Ft struct TYPE * Fn RB_LEFT struct TYPE *elm RB_ENTRY NAME Ft struct TYPE * Fn RB_RIGHT struct TYPE *elm RB_ENTRY NAME Ft struct TYPE * Fn RB_PARENT struct TYPE *elm RB_ENTRY NAME Fn RB_FOREACH VARNAME NAME RB_HEAD *head Fn RB_FOREACH_REVERSE VARNAME NAME RB_HEAD *head Ft void Fn RB_INIT RB_HEAD *head Ft struct TYPE * Fn RB_INSERT NAME RB_HEAD *head struct TYPE *elm Ft struct TYPE * Fn RB_REMOVE NAME RB_HEAD *head struct TYPE *elm</p>
<h2>DESCRIPTION</h2>
<p> These macros define data structures for different types of trees: splay trees and red-black trees. </p>
<p> In the macro definitions, Fa TYPE is the name tag of a user defined structure that must contain a field of type Vt SPLAY_ENTRY , or Vt RB_ENTRY , named Fa ENTRYNAME . The argument Fa HEADNAME is the name tag of a user defined structure that must be declared using the macros Fn SPLAY_HEAD , or Fn RB_HEAD . The argument Fa NAME has to be a unique name prefix for every tree that is defined. </p>
<p> The function prototypes are declared with Fn SPLAY_PROTOTYPE , Fn RB_PROTOTYPE , or Fn RB_PROTOTYPE_STATIC . The function bodies are generated with Fn SPLAY_GENERATE , Fn RB_GENERATE , or Fn RB_GENERATE_STATIC . See the examples below for further explanation of how these macros are used.</p>
<h2>SPLAY TREES</h2>
<p> A splay tree is a self-organizing data structure. Every operation on the tree causes a splay to happen. The splay moves the requested node to the root of the tree and partly rebalances it. </p>
<p> This has the benefit that request locality causes faster lookups as the requested nodes move to the top of the tree. On the other hand, every lookup causes memory writes. </p>
<p> The Balance Theorem bounds the total access time for <i>m</i> operations and <i>n</i> inserts on an initially empty tree as Fn O m + nlg n . The amortized cost for a sequence of <i>m</i> accesses to a splay tree is Fn O lg n . </p>
<p> A splay tree is headed by a structure defined by the Fn SPLAY_HEAD macro. A structure is declared as follows: </p>
<blockquote><p> Fn SPLAY_HEAD HEADNAME TYPE <i>head</i> </p></blockquote>
<p> where Fa HEADNAME is the name of the structure to be defined, and struct Fa TYPE is the type of the elements to be inserted into the tree. </p>
<p> The Fn SPLAY_ENTRY macro declares a structure that allows elements to be connected in the tree. </p>
<p> In order to use the functions that manipulate the tree structure, their prototypes need to be declared with the Fn SPLAY_PROTOTYPE macro, where Fa NAME is a unique identifier for this particular tree. The Fa TYPE argument is the type of the structure that is being managed by the tree. The Fa FIELD argument is the name of the element defined by Fn SPLAY_ENTRY . </p>
<p> The function bodies are generated with the Fn SPLAY_GENERATE macro. It takes the same arguments as the Fn SPLAY_PROTOTYPE macro, but should be used only once. </p>
<p> Finally, the Fa CMP argument is the name of a function used to compare tree nodes with each other. The function takes two arguments of type Vt struct TYPE * . If the first argument is smaller than the second, the function returns a value smaller than zero. If they are equal, the function returns zero. Otherwise, it should return a value greater than zero. The compare function defines the order of the tree elements. </p>
<p> The Fn SPLAY_INIT macro initializes the tree referenced by Fa head . </p>
<p> The splay tree can also be initialized statically by using the Fn SPLAY_INITIALIZER macro like this: </p>
<blockquote><p> Fn SPLAY_HEAD HEADNAME TYPE <i>head</i> = Fn SPLAY_INITIALIZER &amp;head ; </p></blockquote>
<p> The Fn SPLAY_INSERT macro inserts the new element Fa elm into the tree. </p>
<p> The Fn SPLAY_REMOVE macro removes the element Fa elm from the tree pointed by Fa head . </p>
<p> The Fn SPLAY_FIND macro can be used to find a particular element in the tree. </p>
<blockquote>
<pre><code>
struct TYPE find, *res;
find.key = 30;
res = SPLAY_FIND(NAME, head, &amp;find);
</code></pre>
</blockquote>
<p> The Fn SPLAY_ROOT , Fn SPLAY_MIN , Fn SPLAY_MAX , and Fn SPLAY_NEXT macros can be used to traverse the tree: </p>
<blockquote><p>
for (np = SPLAY_MIN(NAME, &amp;head); np != NULL; np = SPLAY_NEXT(NAME, &amp;head, np))
 </p></blockquote>
<p> Or, for simplicity, one can use the Fn SPLAY_FOREACH macro: </p>
<blockquote><p> Fn SPLAY_FOREACH np NAME head </p></blockquote>
<p> The Fn SPLAY_EMPTY macro should be used to check whether a splay tree is empty.</p>
<h2>RED-BLACK TREES</h2>
<p> A red-black tree is a binary search tree with the node color as an extra attribute. It fulfills a set of conditions: </p>
<ol>
<li> Every search path from the root to a leaf consists of the same number of black nodes.
<li> Each red node (except for the root) has a black parent.
<li> Each leaf node is black. </ol>
<p> Every operation on a red-black tree is bounded as Fn O lg n . The maximum height of a red-black tree is Fn 2lg n + 1 . </p>
<p> A red-black tree is headed by a structure defined by the Fn RB_HEAD macro. A structure is declared as follows: </p>
<blockquote><p> Fn RB_HEAD HEADNAME TYPE <i>head</i> </p></blockquote>
<p> where Fa HEADNAME is the name of the structure to be defined, and struct Fa TYPE is the type of the elements to be inserted into the tree. </p>
<p> The Fn RB_ENTRY macro declares a structure that allows elements to be connected in the tree. </p>
<p> In order to use the functions that manipulate the tree structure, their prototypes need to be declared with the Fn RB_PROTOTYPE or Fn RB_PROTOTYPE_STATIC macro, where Fa NAME is a unique identifier for this particular tree. The Fa TYPE argument is the type of the structure that is being managed by the tree. The Fa FIELD argument is the name of the element defined by Fn RB_ENTRY . </p>
<p> The function bodies are generated with the Fn RB_GENERATE or Fn RB_GENERATE_STATIC macro. These macros take the same arguments as the Fn RB_PROTOTYPE and Fn RB_PROTOTYPE_STATIC macros, but should be used only once. </p>
<p> Finally, the Fa CMP argument is the name of a function used to compare tree nodes with each other. The function takes two arguments of type Vt struct TYPE * . If the first argument is smaller than the second, the function returns a value smaller than zero. If they are equal, the function returns zero. Otherwise, it should return a value greater than zero. The compare function defines the order of the tree elements. </p>
<p> The Fn RB_INIT macro initializes the tree referenced by Fa head . </p>
<p> The red-black tree can also be initialized statically by using the Fn RB_INITIALIZER macro like this: </p>
<blockquote><p> Fn RB_HEAD HEADNAME TYPE <i>head</i> = Fn RB_INITIALIZER &amp;head ; </p></blockquote>
<p> The Fn RB_INSERT macro inserts the new element Fa elm into the tree. </p>
<p> The Fn RB_REMOVE macro removes the element Fa elm from the tree pointed by Fa head . </p>
<p> The Fn RB_FIND and Fn RB_NFIND macros can be used to find a particular element in the tree. </p>
<blockquote><p>
struct TYPE find, *res;<br />
find.key = 30;<br />
res = RB_FIND(NAME, head, &amp;find);
 </p></blockquote>
<p> The Fn RB_ROOT , Fn RB_MIN , Fn RB_MAX , Fn RB_NEXT , and Fn RB_PREV macros can be used to traverse the tree: </p>
<blockquote><p><tt>&quot;for (np = RB_MIN(NAME, &amp;head); np != NULL; np = RB_NEXT(NAME, &amp;head, np))&quot;</tt></p></blockquote>
<p> Or, for simplicity, one can use the Fn RB_FOREACH or Fn RB_FOREACH_REVERSE macro: </p>
<blockquote><p> Fn RB_FOREACH np NAME head </p></blockquote>
<p> The Fn RB_EMPTY macro should be used to check whether a red-black tree is empty.</p>
<h2>NOTES</h2>
<p> Trying to free a tree in the following way is a common error: </p>
<blockquote><p>
SPLAY_FOREACH(var, NAME, head)<br />
{<br />
    SPLAY_REMOVE(NAME, head, var);<br />
    free(var);<br />
}<br />
free(head);
 </p></blockquote>
<p> Since <i>var</i> is freed, the Fn FOREACH macro refers to a pointer that may have been reallocated already. Proper code needs a second variable. </p>
<blockquote>
<pre><code>
for (var = SPLAY_MIN(NAME, head); var != NULL; var = nxt) {
    nxt = SPLAY_NEXT(NAME, head, var);
    SPLAY_REMOVE(NAME, head, var);
    free(var);
}
</code></pre>
</blockquote>
<p> Both Fn RB_INSERT and Fn SPLAY_INSERT return <code>NULL</code> if the element was inserted in the tree successfully, otherwise they return a pointer to the element with the colliding key. </p>
<p> Accordingly, Fn RB_REMOVE and Fn SPLAY_REMOVE return the pointer to the removed element otherwise they return <code>NULL</code> to indicate an error.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-queue/">queue</a>(3)</p>
<h2>AUTHORS</h2>
<p> The author of the tree macros is An Niels Provos . </p>
<h2>Index</h2>
