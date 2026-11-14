---
title: "twalk_r(3)"
name: "twalk_r"
section: "3"
letter: "t"
url: "/docs/linux/man/3-twalk_r/"
description: "tsearch, tfind, tdelete, twalk, tdestroy – manage a binary search tree"
---

<p>tsearch, tfind, tdelete, twalk, tdestroy &#8211; manage a binary search tree</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;search.h&gt;

typedef enum { preorder,
               postorder,
               endorder,
               leaf } VISIT;

void *tsearch(const void *key, void **rootp,
              int (*compar)(const void *, const void *));

void *tfind(const void *key, void *const *rootp,
            int (*compar)(const void *, const void *));

void *tdelete(const void *key, void **rootp,
              int (*compar)(const void *, const void *));

void twalk(const void *root,
           void (*action)(const void *nodep, VISIT which,
                          int depth));

#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;search.h&gt;

void twalk_r(const void *root,
             void (*action)(const void *nodep, VISIT which,
                            void *closure),
             void *closure);

void tdestroy(void *root, void (*free_node)(void *nodep));</code></pre>
<h2>Description</h2>
<p><code>tsearch</code>(), <code>tfind</code>(), <code>twalk</code>(), and <code>tdelete</code>() manage a binary search tree. They are generalized from Knuth (6.2.2) Algorithm T. The first field in each node of the tree is a pointer to the corresponding data item. (The calling program must store the actual data.) <i>compar</i> points to a comparison routine, which takes pointers to two items. It should return an integer which is negative, zero, or positive, depending on whether the first item is less than, equal to, or greater than the second. </p>
<p> <code>tsearch</code>() searches the tree for an item. <i>key</i> points to the item to be searched for. <i>rootp</i> points to a variable which points to the root of the tree. If the tree is empty, then the variable that <i>rootp</i> points to should be set to NULL. If the item is found in the tree, then <code>tsearch</code>() returns a pointer to the corresponding tree node. (In other words, <code>tsearch</code>() returns a pointer to a pointer to the data item.) If the item is not found, then <code>tsearch</code>() adds it, and returns a pointer to the corresponding tree node. </p>
<p> <code>tfind</code>() is like <code>tsearch</code>(), except that if the item is not found, then <code>tfind</code>() returns NULL. </p>
<p> <code>tdelete</code>() deletes an item from the tree. Its arguments are the same as for <code>tsearch</code>(). </p>
<p> <code>twalk</code>() performs depth-first, left-to-right traversal of a binary tree. <i>root</i> points to the starting node for the traversal. If that node is not the root, then only part of the tree will be visited. <code>twalk</code>() calls the user function <i>action</i> each time a node is visited (that is, three times for an internal node, and once for a leaf). <i>action</i>, in turn, takes three arguments. The first argument is a pointer to the node being visited. The structure of the node is unspecified, but it is possible to cast the pointer to a pointer-to-pointer-to-element in order to access the element stored within the node. The application must not modify the structure pointed to by this argument. The second argument is an integer which takes one of the values <code>preorder</code>, <code>postorder</code>, or <code>endorder</code> depending on whether this is the first, second, or third visit to the internal node, or the value <code>leaf</code> if this is the single visit to a leaf node. (These symbols are defined in <i>&lt;search.h&gt;</i>.) The third argument is the depth of the node; the root node has depth zero. </p>
<p> (More commonly, <code>preorder</code>, <code>postorder</code>, and <code>endorder</code> are known as <code>preorder</code>, <code>inorder</code>, and <code>postorder</code>: before visiting the children, after the first and before the second, and after visiting the children. Thus, the choice of name <code>postorder</code> is rather confusing.) </p>
<p> <code>twalk_r</code>() is similar to <code>twalk</code>(), but instead of the <i>depth</i> argument, the <i>closure</i> argument pointer is passed to each invocation of the action callback, unchanged. This pointer can be used to pass information to and from the callback function in a thread-safe fashion, without resorting to global variables. </p>
<p> <code>tdestroy</code>() removes the whole tree pointed to by <i>root</i>, freeing all resources allocated by the <code>tsearch</code>() function. For the data in each tree node the function <i>free_node</i> is called. The pointer to the data is passed as the argument to the function. If no such work is necessary, <i>free_node</i> must point to a function doing nothing.</p>
<h2>Return Value</h2>
<p><code>tsearch</code>() returns a pointer to a matching node in the tree, or to the newly added node, or NULL if there was insufficient memory to add the item. <code>tfind</code>() returns a pointer to the node, or NULL if no match is found. If there are multiple items that match the key, the item whose node is returned is unspecified. </p>
<p> <code>tdelete</code>() returns a pointer to the parent of the node deleted, or NULL if the item was not found. If the deleted node was the root node, <code>tdelete</code>() returns a dangling pointer that must not be accessed. </p>
<p> <code>tsearch</code>(), <code>tfind</code>(), and <code>tdelete</code>() also return NULL if <i>rootp</i> was NULL on entry.</p>
<h2>Versions</h2>
<p><code>twalk_r</code>() is available in glibc since version 2.30.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>tsearch</code>(), <code>tfind</code>(),<br />
 <code>tdelete</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:rootp
</td>
</tr>
<tr VALIGN=top>
<td> <code>twalk</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:root
</td>
</tr>
<tr VALIGN=top>
<td> <code>twalk_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:root
</td>
</tr>
<tr VALIGN=top>
<td> <code>tdestroy</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, SVr4. The functions <code>tdestroy</code>() and <code>twalk_r</code>() are GNU extensions.</p>
<h2>Notes</h2>
<p><code>twalk</code>() takes a pointer to the root, while the other functions take a pointer to a variable which points to the root. </p>
<p> <code>tdelete</code>() frees the memory required for the node in the tree. The user is responsible for freeing the memory for the corresponding data. </p>
<p> The example program depends on the fact that <code>twalk</code>() makes no further reference to a node after calling the user function with argument &quot;endorder&quot; or &quot;leaf&quot;. This works with the GNU library implementation, but is not in the System V documentation.</p>
<h2>Examples</h2>
<p>The following program inserts twelve random numbers into a binary tree, where duplicate numbers are collapsed, then prints the numbers in order. </p>
<pre><code>#define _GNU_SOURCE /* Expose declaration of tdestroy() */
#include &lt;search.h&gt;
#include &lt;stddef.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;time.h&gt;
static void *root = NULL;
static void *
xmalloc(size_t n)
{
    void *p;
    p = malloc(n);
    if (p)
        return p;
    fprintf(stderr, &quot;insufficient memory
&quot;);
    exit(EXIT_FAILURE);
}
static int
compare(const void *pa, const void *pb)
{
    if (*(int *)pa &lt; *(int *)pb)
        return -1;
    if (*(int *)pa &gt; *(int *)pb)
        return 1;
    return 0;
}
static void
action(const void *nodep, VISIT which, int depth)
{
    int *datap;
    switch (which) {
    case preorder:
        break;
    case postorder:
        datap = *(int **)nodep;
        printf(&quot;%6d
&quot;, *datap);
        break;
    case endorder:
        break;
    case leaf:
        datap = *(int **)nodep;
        printf(&quot;%6d
&quot;, *datap);
        break;
    }
}
int main(void)
{
    int **val;
    srand(time(NULL));
    for (int i = 0; i &lt; 12; i++) {
        int *ptr = xmalloc(sizeof(*ptr));
        *ptr = rand() &amp; 0xff;
        val = tsearch(ptr, &amp;root, compare);
        if (val == NULL)
            exit(EXIT_FAILURE);
        else if (*val != ptr)
            free(ptr);
    }
    twalk(root, action);
    tdestroy(root, free);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-bsearch/">bsearch</a></code>(3), <code><a href="/docs/linux/man/3-hsearch/">hsearch</a></code>(3), <code><a href="/docs/linux/man/3-lsearch/">lsearch</a></code>(3), <code><a href="/docs/linux/man/3-qsort/">qsort</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
