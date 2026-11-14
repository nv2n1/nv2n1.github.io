---
title: "list_insert_head(3)"
name: "list_insert_head"
section: "3"
letter: "l"
url: "/docs/linux/man/3-list_insert_head/"
description: "SLIST_EMPTY SLIST_ENTRY SLIST_FIRST SLIST_FOREACH SLIST_HEAD SLIST_HEAD_INITIALIZER SLIST_INIT SLIST_INSERT_AFTER SLIST_INSERT_HEAD SLIST_NEXT SLIST_REMOVE_HEAD SLIST_REMOVE STAILQ_CONCAT STAILQ_EM..."
---

<p><code>SLIST_EMPTY</code> <code>SLIST_ENTRY</code> <code>SLIST_FIRST</code> <code>SLIST_FOREACH</code> <code>SLIST_HEAD</code> <code>SLIST_HEAD_INITIALIZER</code> <code>SLIST_INIT</code> <code>SLIST_INSERT_AFTER</code> <code>SLIST_INSERT_HEAD</code> <code>SLIST_NEXT</code> <code>SLIST_REMOVE_HEAD</code> <code>SLIST_REMOVE</code> <code>STAILQ_CONCAT</code> <code>STAILQ_EMPTY</code> <code>STAILQ_ENTRY</code> <code>STAILQ_FIRST</code> <code>STAILQ_FOREACH</code> <code>STAILQ_HEAD</code> <code>STAILQ_HEAD_INITIALIZER</code> <code>STAILQ_INIT</code> <code>STAILQ_INSERT_AFTER</code> <code>STAILQ_INSERT_HEAD</code> <code>STAILQ_INSERT_TAIL</code> <code>STAILQ_NEXT</code> <code>STAILQ_REMOVE_HEAD</code> <code>STAILQ_REMOVE</code> <code>LIST_EMPTY</code> <code>LIST_ENTRY</code> <code>LIST_FIRST</code> <code>LIST_FOREACH</code> <code>LIST_HEAD</code> <code>LIST_HEAD_INITIALIZER</code> <code>LIST_INIT</code> <code>LIST_INSERT_AFTER</code> <code>LIST_INSERT_BEFORE</code> <code>LIST_INSERT_HEAD</code> <code>LIST_NEXT</code> <code>LIST_REMOVE</code> <code>TAILQ_CONCAT</code> <code>TAILQ_EMPTY</code> <code>TAILQ_ENTRY</code> <code>TAILQ_FIRST</code> <code>TAILQ_FOREACH</code> <code>TAILQ_FOREACH_REVERSE</code> <code>TAILQ_HEAD</code> <code>TAILQ_HEAD_INITIALIZER</code> <code>TAILQ_INIT</code> <code>TAILQ_INSERT_AFTER</code> <code>TAILQ_INSERT_BEFORE</code> <code>TAILQ_INSERT_HEAD</code> <code>TAILQ_INSERT_TAIL</code> <code>TAILQ_LAST</code> <code>TAILQ_NEXT</code> <code>TAILQ_PREV</code> <code>TAILQ_REMOVE</code> <code>TAILQ_SWAP</code> &#8211; implementations of singly-linked lists, singly-linked tail queues, lists and tail queues </p>
<h2>Synopsis</h2>
<p>In sys/queue.h Fn SLIST_EMPTY SLIST_HEAD *head Fn SLIST_ENTRY TYPE Fn SLIST_FIRST SLIST_HEAD *head Fn SLIST_FOREACH TYPE *var SLIST_HEAD *head SLIST_ENTRY NAME Fn SLIST_HEAD HEADNAME TYPE Fn SLIST_HEAD_INITIALIZER SLIST_HEAD head Fn SLIST_INIT SLIST_HEAD *head Fn SLIST_INSERT_AFTER TYPE *listelm TYPE *elm SLIST_ENTRY NAME Fn SLIST_INSERT_HEAD SLIST_HEAD *head TYPE *elm SLIST_ENTRY NAME Fn SLIST_NEXT TYPE *elm SLIST_ENTRY NAME Fn SLIST_REMOVE_HEAD SLIST_HEAD *head SLIST_ENTRY NAME Fn SLIST_REMOVE SLIST_HEAD *head TYPE *elm TYPE SLIST_ENTRY NAME Fn STAILQ_CONCAT STAILQ_HEAD *head1 STAILQ_HEAD *head2 Fn STAILQ_EMPTY STAILQ_HEAD *head Fn STAILQ_ENTRY TYPE Fn STAILQ_FIRST STAILQ_HEAD *head Fn STAILQ_FOREACH TYPE *var STAILQ_HEAD *head STAILQ_ENTRY NAME Fn STAILQ_HEAD HEADNAME TYPE Fn STAILQ_HEAD_INITIALIZER STAILQ_HEAD head Fn STAILQ_INIT STAILQ_HEAD *head Fn STAILQ_INSERT_AFTER STAILQ_HEAD *head TYPE *listelm TYPE *elm STAILQ_ENTRY NAME Fn STAILQ_INSERT_HEAD STAILQ_HEAD *head TYPE *elm STAILQ_ENTRY NAME Fn STAILQ_INSERT_TAIL STAILQ_HEAD *head TYPE *elm STAILQ_ENTRY NAME Fn STAILQ_NEXT TYPE *elm STAILQ_ENTRY NAME Fn STAILQ_REMOVE_HEAD STAILQ_HEAD *head STAILQ_ENTRY NAME Fn STAILQ_REMOVE STAILQ_HEAD *head TYPE *elm TYPE STAILQ_ENTRY NAME Fn LIST_EMPTY LIST_HEAD *head Fn LIST_ENTRY TYPE Fn LIST_FIRST LIST_HEAD *head Fn LIST_FOREACH TYPE *var LIST_HEAD *head LIST_ENTRY NAME Fn LIST_HEAD HEADNAME TYPE Fn LIST_HEAD_INITIALIZER LIST_HEAD head Fn LIST_INIT LIST_HEAD *head Fn LIST_INSERT_AFTER TYPE *listelm TYPE *elm LIST_ENTRY NAME Fn LIST_INSERT_BEFORE TYPE *listelm TYPE *elm LIST_ENTRY NAME Fn LIST_INSERT_HEAD LIST_HEAD *head TYPE *elm LIST_ENTRY NAME Fn LIST_NEXT TYPE *elm LIST_ENTRY NAME Fn LIST_REMOVE TYPE *elm LIST_ENTRY NAME Fn LIST_SWAP LIST_HEAD *head1 LIST_HEAD *head2 TYPE LIST_ENTRY NAME Fn TAILQ_CONCAT TAILQ_HEAD *head1 TAILQ_HEAD *head2 TAILQ_ENTRY NAME Fn TAILQ_EMPTY TAILQ_HEAD *head Fn TAILQ_ENTRY TYPE Fn TAILQ_FIRST TAILQ_HEAD *head Fn TAILQ_FOREACH TYPE *var TAILQ_HEAD *head TAILQ_ENTRY NAME Fn TAILQ_FOREACH_REVERSE TYPE *var TAILQ_HEAD *head HEADNAME TAILQ_ENTRY NAME Fn TAILQ_HEAD HEADNAME TYPE Fn TAILQ_HEAD_INITIALIZER TAILQ_HEAD head Fn TAILQ_INIT TAILQ_HEAD *head Fn TAILQ_INSERT_AFTER TAILQ_HEAD *head TYPE *listelm TYPE *elm TAILQ_ENTRY NAME Fn TAILQ_INSERT_BEFORE TYPE *listelm TYPE *elm TAILQ_ENTRY NAME Fn TAILQ_INSERT_HEAD TAILQ_HEAD *head TYPE *elm TAILQ_ENTRY NAME Fn TAILQ_INSERT_TAIL TAILQ_HEAD *head TYPE *elm TAILQ_ENTRY NAME Fn TAILQ_LAST TAILQ_HEAD *head HEADNAME Fn TAILQ_NEXT TYPE *elm TAILQ_ENTRY NAME Fn TAILQ_PREV TYPE *elm HEADNAME TAILQ_ENTRY NAME Fn TAILQ_REMOVE TAILQ_HEAD *head TYPE *elm TAILQ_ENTRY NAME Fn TAILQ_SWAP TAILQ_HEAD *head1 TAILQ_HEAD *head2 TYPE TAILQ_ENTRY NAME</p>
<h2>Description</h2>
<p>These macros define and operate on four types of data structures: singly-linked lists, singly-linked tail queues, lists, and tail queues. All four structures support the following functionality: </p>
<ol>
<li> Insertion of a new entry at the head of the list.
<li> Insertion of a new entry after any element in the list.
<li> <a href="/docs/linux/man/1-o/">O</a>(1) removal of an entry from the head of the list.
<li> Forward traversal through the list.
<li> Swapping the contents of two lists. </ol>
<p> Singly-linked lists are the simplest of the four data structures and support only the above functionality. Singly-linked lists are ideal for applications with large datasets and few or no removals, or for implementing a LIFO queue. Singly-linked lists add the following functionality: </p>
<ol>
<li> <a href="/docs/linux/man/n-o/">O</a>(n) removal of any entry in the list. </ol>
<p> Singly-linked tail queues add the following functionality: </p>
<ol>
<li> Entries can be added at the end of a list.
<li> <a href="/docs/linux/man/n-o/">O</a>(n) removal of any entry in the list.
<li> They may be concatenated. </ol>
<p> However: </p>
<ol>
<li> All list insertions must specify the head of the list.
<li> Each head entry requires two pointers rather than one.
<li> Code size is about 15% greater and operations run about 20% slower than singly-linked lists. </ol>
<p> Singly-linked tail queues are ideal for applications with large datasets and few or no removals, or for implementing a FIFO queue. </p>
<p> All doubly linked types of data structures (lists and tail queues) additionally allow: </p>
<ol>
<li> Insertion of a new entry before any element in the list.
<li> <a href="/docs/linux/man/1-o/">O</a>(1) removal of any entry in the list. </ol>
<p> However: </p>
<ol>
<li> Each element requires two pointers rather than one.
<li> Code size and execution time of operations (except for removal) is about twice that of the singly-linked data-structures. </ol>
<p> Linked lists are the simplest of the doubly linked data structures. They add the following functionality over the above: </p>
<ol>
<li> They may be traversed backwards. </ol>
<p> However: </p>
<ol>
<li> To traverse backwards, an entry to begin the traversal and the list in which it is contained must be specified. </ol>
<p> Tail queues add the following functionality: </p>
<ol>
<li> Entries can be added at the end of a list.
<li> They may be traversed backwards, from tail to head.
<li> They may be concatenated. </ol>
<p> However: </p>
<ol>
<li> All list insertions and removals must specify the head of the list.
<li> Each head entry requires two pointers rather than one.
<li> Code size is about 15% greater and operations run about 20% slower than singly-linked lists. </ol>
<p> In the macro definitions, Fa TYPE is the name of a user defined structure, that must contain a field of type <code>SLIST_ENTRY</code> <code>STAILQ_ENTRY</code> <code>LIST_ENTRY</code> or <code>TAILQ_ENTRY</code> named Fa NAME . The argument Fa HEADNAME is the name of a user defined structure that must be declared using the macros <code>SLIST_HEAD</code> <code>STAILQ_HEAD</code> <code>LIST_HEAD</code> or <code>TAILQ_HEAD</code> See the examples below for further explanation of how these macros are used.</p>
<h3>Singly-linked lists</h3>
<p>A singly-linked list is headed by a structure defined by the <code>SLIST_HEAD</code> macro. This structure contains a single pointer to the first element on the list. The elements are singly linked for minimum space and pointer manipulation overhead at the expense of <a href="/docs/linux/man/n-o/">O</a>(n) removal for arbitrary elements. New elements can be added to the list after an existing element or at the head of the list. An Fa SLIST_HEAD structure is declared as follows: </p>
<blockquote>
<pre>SLIST_HEAD(HEADNAME, TYPE) head;</pre>
</blockquote>
<p> where Fa HEADNAME is the name of the structure to be defined, and Fa TYPE is the type of the elements to be linked into the list. A pointer to the head of the list can later be declared as: </p>
<blockquote>
<pre>struct HEADNAME *headp;</pre>
</blockquote>
<p> (The names <code>head</code> and <code>headp</code> are user selectable.) </p>
<p> The macro <code>SLIST_HEAD_INITIALIZER</code> evaluates to an initializer for the list Fa head . </p>
<p> The macro <code>SLIST_EMPTY</code> evaluates to true if there are no elements in the list. </p>
<p> The macro <code>SLIST_ENTRY</code> declares a structure that connects the elements in the list. </p>
<p> The macro <code>SLIST_FIRST</code> returns the first element in the list or NULL if the list is empty. </p>
<p> The macro <code>SLIST_FOREACH</code> traverses the list referenced by Fa head in the forward direction, assigning each element in turn to Fa var . </p>
<p> The macro <code>SLIST_INIT</code> initializes the list referenced by Fa head . </p>
<p> The macro <code>SLIST_INSERT_HEAD</code> inserts the new element Fa elm at the head of the list. </p>
<p> The macro <code>SLIST_INSERT_AFTER</code> inserts the new element Fa elm after the element Fa listelm . </p>
<p> The macro <code>SLIST_NEXT</code> returns the next element in the list. </p>
<p> The macro <code>SLIST_REMOVE_HEAD</code> removes the element Fa elm from the head of the list. For optimum efficiency, elements being removed from the head of the list should explicitly use this macro instead of the generic Fa SLIST_REMOVE macro. </p>
<p> The macro <code>SLIST_REMOVE</code> removes the element Fa elm from the list.</p>
<h3>Singly-linked list example</h3>
<pre>SLIST_HEAD(slisthead, entry) head =
 SLIST_HEAD_INITIALIZER(head);
struct slisthead *headp; /* Singly-linked List
 head. */
struct entry {
 ...
 SLIST_ENTRY(entry) entries; /* Singly-linked List. */
 ...
} *n1, *n2, *n3, *np;
SLIST_INIT(&amp;head); /* Initialize the list. */
n1 = malloc(sizeof(struct entry)); /* Insert at the head. */
SLIST_INSERT_HEAD(&amp;head, n1, entries);
n2 = malloc(sizeof(struct entry)); /* Insert after. */
SLIST_INSERT_AFTER(n1, n2, entries);
SLIST_REMOVE(&amp;head, n2, entry, entries);/* Deletion. */
free(n2);
n3 = SLIST_FIRST(&amp;head);
SLIST_REMOVE_HEAD(&amp;head, entries); /* Deletion from the head. */
free(n3);
 /* Forward traversal. */
SLIST_FOREACH(np, &amp;head, entries)
 np-&gt; ...
while (!SLIST_EMPTY(&amp;head)) { /* List Deletion. */
 n1 = SLIST_FIRST(&amp;head);
 SLIST_REMOVE_HEAD(&amp;head, entries);
 free(n1);
}</pre>
<h3>Singly-linked tail queues</h3>
<p>A singly-linked tail queue is headed by a structure defined by the <code>STAILQ_HEAD</code> macro. This structure contains a pair of pointers, one to the first element in the tail queue and the other to the last element in the tail queue. The elements are singly linked for minimum space and pointer manipulation overhead at the expense of <a href="/docs/linux/man/n-o/">O</a>(n) removal for arbitrary elements. New elements can be added to the tail queue after an existing element, at the head of the tail queue, or at the end of the tail queue. A Fa STAILQ_HEAD structure is declared as follows: </p>
<blockquote>
<pre>STAILQ_HEAD(HEADNAME, TYPE) head;</pre>
</blockquote>
<p> where <code>HEADNAME</code> is the name of the structure to be defined, and <code>TYPE</code> is the type of the elements to be linked into the tail queue. A pointer to the head of the tail queue can later be declared as: </p>
<blockquote>
<pre>struct HEADNAME *headp;</pre>
</blockquote>
<p> (The names <code>head</code> and <code>headp</code> are user selectable.) </p>
<p> The macro <code>STAILQ_HEAD_INITIALIZER</code> evaluates to an initializer for the tail queue Fa head . </p>
<p> The macro <code>STAILQ_CONCAT</code> concatenates the tail queue headed by Fa head2 onto the end of the one headed by Fa head1 removing all entries from the former. </p>
<p> The macro <code>STAILQ_EMPTY</code> evaluates to true if there are no items on the tail queue. </p>
<p> The macro <code>STAILQ_ENTRY</code> declares a structure that connects the elements in the tail queue. </p>
<p> The macro <code>STAILQ_FIRST</code> returns the first item on the tail queue or NULL if the tail queue is empty. </p>
<p> The macro <code>STAILQ_FOREACH</code> traverses the tail queue referenced by Fa head in the forward direction, assigning each element in turn to Fa var . </p>
<p> The macro <code>STAILQ_INIT</code> initializes the tail queue referenced by Fa head . </p>
<p> The macro <code>STAILQ_INSERT_HEAD</code> inserts the new element Fa elm at the head of the tail queue. </p>
<p> The macro <code>STAILQ_INSERT_TAIL</code> inserts the new element Fa elm at the end of the tail queue. </p>
<p> The macro <code>STAILQ_INSERT_AFTER</code> inserts the new element Fa elm after the element Fa listelm . </p>
<p> The macro <code>STAILQ_NEXT</code> returns the next item on the tail queue, or NULL this item is the last. </p>
<p> The macro <code>STAILQ_REMOVE_HEAD</code> removes the element at the head of the tail queue. For optimum efficiency, elements being removed from the head of the tail queue should use this macro explicitly rather than the generic Fa STAILQ_REMOVE macro. </p>
<p> The macro <code>STAILQ_REMOVE</code> removes the element Fa elm from the tail queue.</p>
<h3>Singly-linked tail queue example</h3>
<pre>STAILQ_HEAD(stailhead, entry) head =
 STAILQ_HEAD_INITIALIZER(head);
struct stailhead *headp; /* Singly-linked tail queue head. */
struct entry {
 ...
 STAILQ_ENTRY(entry) entries; /* Tail queue. */
 ...
} *n1, *n2, *n3, *np;
STAILQ_INIT(&amp;head); /* Initialize the queue. */
n1 = malloc(sizeof(struct entry)); /* Insert at the head. */
STAILQ_INSERT_HEAD(&amp;head, n1, entries);
n1 = malloc(sizeof(struct entry)); /* Insert at the tail. */
STAILQ_INSERT_TAIL(&amp;head, n1, entries);
n2 = malloc(sizeof(struct entry)); /* Insert after. */
STAILQ_INSERT_AFTER(&amp;head, n1, n2, entries);
 /* Deletion. */
STAILQ_REMOVE(&amp;head, n2, entry, entries);
free(n2);
 /* Deletion from the head. */
n3 = STAILQ_FIRST(&amp;head);
STAILQ_REMOVE_HEAD(&amp;head, entries);
free(n3);
 /* Forward traversal. */
STAILQ_FOREACH(np, &amp;head, entries)
 np-&gt; ...
 /* TailQ Deletion. */
while (!STAILQ_EMPTY(&amp;head)) {
 n1 = STAILQ_FIRST(&amp;head);
 STAILQ_REMOVE_HEAD(&amp;head, entries);
 free(n1);
}
 /* Faster TailQ Deletion. */
n1 = STAILQ_FIRST(&amp;head);
while (n1 != NULL) {
 n2 = STAILQ_NEXT(n1, entries);
 free(n1);
 n1 = n2;
}
STAILQ_INIT(&amp;head);</pre>
<h3>Lists</h3>
<p>A list is headed by a structure defined by the <code>LIST_HEAD</code> macro. This structure contains a single pointer to the first element on the list. The elements are doubly linked so that an arbitrary element can be removed without traversing the list. New elements can be added to the list after an existing element, before an existing element, or at the head of the list. A Fa LIST_HEAD structure is declared as follows: </p>
<blockquote>
<pre>LIST_HEAD(HEADNAME, TYPE) head;</pre>
</blockquote>
<p> where Fa HEADNAME is the name of the structure to be defined, and Fa TYPE is the type of the elements to be linked into the list. A pointer to the head of the list can later be declared as: </p>
<blockquote>
<pre>struct HEADNAME *headp;</pre>
</blockquote>
<p> (The names <code>head</code> and <code>headp</code> are user selectable.) </p>
<p> The macro <code>LIST_HEAD_INITIALIZER</code> evaluates to an initializer for the list Fa head . </p>
<p> The macro <code>LIST_EMPTY</code> evaluates to true if there are no elements in the list. </p>
<p> The macro <code>LIST_ENTRY</code> declares a structure that connects the elements in the list. </p>
<p> The macro <code>LIST_FIRST</code> returns the first element in the list or NULL if the list is empty. </p>
<p> The macro <code>LIST_FOREACH</code> traverses the list referenced by Fa head in the forward direction, assigning each element in turn to Fa var . </p>
<p> The macro <code>LIST_INIT</code> initializes the list referenced by Fa head . </p>
<p> The macro <code>LIST_INSERT_HEAD</code> inserts the new element Fa elm at the head of the list. </p>
<p> The macro <code>LIST_INSERT_AFTER</code> inserts the new element Fa elm after the element Fa listelm . </p>
<p> The macro <code>LIST_INSERT_BEFORE</code> inserts the new element Fa elm before the element Fa listelm . </p>
<p> The macro <code>LIST_NEXT</code> returns the next element in the list, or NULL if this is the last. </p>
<p> The macro <code>LIST_REMOVE</code> removes the element Fa elm from the list.</p>
<h3>List example</h3>
<pre>LIST_HEAD(listhead, entry) head =
 LIST_HEAD_INITIALIZER(head);
struct listhead *headp; /* List head. */
struct entry {
 ...
 LIST_ENTRY(entry) entries; /* List. */
 ...
} *n1, *n2, *n3, *np, *np_temp;
LIST_INIT(&amp;head); /* Initialize the list. */
n1 = malloc(sizeof(struct entry)); /* Insert at the head. */
LIST_INSERT_HEAD(&amp;head, n1, entries);
n2 = malloc(sizeof(struct entry)); /* Insert after. */
LIST_INSERT_AFTER(n1, n2, entries);
n3 = malloc(sizeof(struct entry)); /* Insert before. */
LIST_INSERT_BEFORE(n2, n3, entries);
LIST_REMOVE(n2, entries); /* Deletion. */
free(n2);
 /* Forward traversal. */
LIST_FOREACH(np, &amp;head, entries)
 np-&gt; ...
while (!LIST_EMPTY(&amp;head)) { /* List Deletion. */
 n1 = LIST_FIRST(&amp;head);
 LIST_REMOVE(n1, entries);
 free(n1);
}
n1 = LIST_FIRST(&amp;head); /* Faster List Deletion. */
while (n1 != NULL) {
 n2 = LIST_NEXT(n1, entries);
 free(n1);
 n1 = n2;
}
LIST_INIT(&amp;head);</pre>
<h3>Tail queues</h3>
<p>A tail queue is headed by a structure defined by the <code>TAILQ_HEAD</code> macro. This structure contains a pair of pointers, one to the first element in the tail queue and the other to the last element in the tail queue. The elements are doubly linked so that an arbitrary element can be removed without traversing the tail queue. New elements can be added to the tail queue after an existing element, before an existing element, at the head of the tail queue, or at the end of the tail queue. A Fa TAILQ_HEAD structure is declared as follows: </p>
<blockquote>
<pre>TAILQ_HEAD(HEADNAME, TYPE) head;</pre>
</blockquote>
<p> where <code>HEADNAME</code> is the name of the structure to be defined, and <code>TYPE</code> is the type of the elements to be linked into the tail queue. A pointer to the head of the tail queue can later be declared as: </p>
<blockquote>
<pre>struct HEADNAME *headp;</pre>
</blockquote>
<p> (The names <code>head</code> and <code>headp</code> are user selectable.) </p>
<p> The macro <code>TAILQ_HEAD_INITIALIZER</code> evaluates to an initializer for the tail queue Fa head . </p>
<p> The macro <code>TAILQ_CONCAT</code> concatenates the tail queue headed by Fa head2 onto the end of the one headed by Fa head1 removing all entries from the former. </p>
<p> The macro <code>TAILQ_EMPTY</code> evaluates to true if there are no items on the tail queue. </p>
<p> The macro <code>TAILQ_ENTRY</code> declares a structure that connects the elements in the tail queue. </p>
<p> The macro <code>TAILQ_FIRST</code> returns the first item on the tail queue or NULL if the tail queue is empty. </p>
<p> The macro <code>TAILQ_FOREACH</code> traverses the tail queue referenced by Fa head in the forward direction, assigning each element in turn to Fa var . Fa var is set to <code>NULL</code> if the loop completes normally, or if there were no elements. </p>
<p> The macro <code>TAILQ_FOREACH_REVERSE</code> traverses the tail queue referenced by Fa head in the reverse direction, assigning each element in turn to Fa var . </p>
<p> The macro <code>TAILQ_INIT</code> initializes the tail queue referenced by Fa head . </p>
<p> The macro <code>TAILQ_INSERT_HEAD</code> inserts the new element Fa elm at the head of the tail queue. </p>
<p> The macro <code>TAILQ_INSERT_TAIL</code> inserts the new element Fa elm at the end of the tail queue. </p>
<p> The macro <code>TAILQ_INSERT_AFTER</code> inserts the new element Fa elm after the element Fa listelm . </p>
<p> The macro <code>TAILQ_INSERT_BEFORE</code> inserts the new element Fa elm before the element Fa listelm . </p>
<p> The macro <code>TAILQ_LAST</code> returns the last item on the tail queue. If the tail queue is empty the return value is <code>NULL</code> </p>
<p> The macro <code>TAILQ_NEXT</code> returns the next item on the tail queue, or NULL if this item is the last. </p>
<p> The macro <code>TAILQ_PREV</code> returns the previous item on the tail queue, or NULL if this item is the first. </p>
<p> The macro <code>TAILQ_REMOVE</code> removes the element Fa elm from the tail queue. </p>
<p> The macro <code>TAILQ_SWAP</code> swaps the contents of Fa head1 and Fa head2 .</p>
<h3>Tail queue example</h3>
<pre>TAILQ_HEAD(tailhead, entry) head =
 TAILQ_HEAD_INITIALIZER(head);
struct tailhead *headp; /* Tail queue head. */
struct entry {
 ...
 TAILQ_ENTRY(entry) entries; /* Tail queue. */
 ...
} *n1, *n2, *n3, *np;
TAILQ_INIT(&amp;head); /* Initialize the queue. */
n1 = malloc(sizeof(struct entry)); /* Insert at the head. */
TAILQ_INSERT_HEAD(&amp;head, n1, entries);
n1 = malloc(sizeof(struct entry)); /* Insert at the tail. */
TAILQ_INSERT_TAIL(&amp;head, n1, entries);
n2 = malloc(sizeof(struct entry)); /* Insert after. */
TAILQ_INSERT_AFTER(&amp;head, n1, n2, entries);
n3 = malloc(sizeof(struct entry)); /* Insert before. */
TAILQ_INSERT_BEFORE(n2, n3, entries);
TAILQ_REMOVE(&amp;head, n2, entries); /* Deletion. */
free(n2);
 /* Forward traversal. */
TAILQ_FOREACH(np, &amp;head, entries)
 np-&gt; ...
 /* Reverse traversal. */
TAILQ_FOREACH_REVERSE(np, &amp;head, tailhead, entries)
 np-&gt; ...
 /* TailQ Deletion. */
while (!TAILQ_EMPTY(&amp;head)) {
 n1 = TAILQ_FIRST(&amp;head);
 TAILQ_REMOVE(&amp;head, n1, entries);
 free(n1);
}
 /* Faster TailQ Deletion. */
n1 = TAILQ_FIRST(&amp;head);
while (n1 != NULL) {
 n2 = TAILQ_NEXT(n1, entries);
 free(n1);
 n1 = n2;
}
TAILQ_INIT(&amp;head);
n2 = malloc(sizeof(struct entry)); /* Insert before. */
CIRCLEQ_INSERT_BEFORE(&amp;head, n1, n2, entries);
 /* Forward traversal. */
for (np = head.cqh_first; np != (void *)&amp;head;
 np = np-&gt;entries.cqe_next)
 np-&gt; ...
 /* Reverse traversal. */
for (np = head.cqh_last; np != (void *)&amp;head; np = np-&gt;entries.cqe_prev)
 np-&gt; ...
 /* Delete. */
while (head.cqh_first != (void *)&amp;head)
 CIRCLEQ_REMOVE(&amp;head, head.cqh_first, entries);</pre>
<h2>Conforming To</h2>
<p>Not in POSIX.1, POSIX.1-2001 or POSIX.1-2008. Present on the BSDs. <code>queue</code> functions first appeared in BSD 4.4</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-insque/">insque</a>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.05 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
