---
title: "tailq(3)"
name: "tailq"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tailq/"
description: "TAILQ_CONCAT, TAILQ_EMPTY, TAILQ_ENTRY, TAILQ_FIRST, TAILQ_FOREACH, TAILQ_FOREACH_REVERSE, TAILQ_HEAD, TAILQ_HEAD_INITIALIZER, TAILQ_INIT, TAILQ_INSERT_AFTER, TAILQ_INSERT_BEFORE, TAILQ_INSERT_HEAD..."
---

<p>TAILQ_CONCAT, TAILQ_EMPTY, TAILQ_ENTRY, TAILQ_FIRST, TAILQ_FOREACH, TAILQ_FOREACH_REVERSE, TAILQ_HEAD, TAILQ_HEAD_INITIALIZER, TAILQ_INIT, TAILQ_INSERT_AFTER, TAILQ_INSERT_BEFORE, TAILQ_INSERT_HEAD, TAILQ_INSERT_TAIL, TAILQ_LAST, TAILQ_NEXT, TAILQ_PREV, TAILQ_REMOVE &#8211; implementation of a doubly linked tail queue</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/queue.h&gt;

void TAILQ_CONCAT(TAILQ_HEAD *head1, TAILQ_HEAD *head2,
                  TAILQ_ENTRY NAME);

int TAILQ_EMPTY(TAILQ_HEAD *head);

TAILQ_ENTRY(TYPE);

struct TYPE *TAILQ_FIRST(TAILQ_HEAD *head);

TAILQ_FOREACH(struct TYPE *var, TAILQ_HEAD *head, TAILQ_ENTRY NAME);

TAILQ_FOREACH_REVERSE(struct TYPE *var, TAILQ_HEAD *head, HEADNAME,
                      TAILQ_ENTRY NAME);

TAILQ_HEAD(HEADNAME, TYPE);

TAILQ_HEAD TAILQ_HEAD_INITIALIZER(TAILQ_HEAD head);

void TAILQ_INIT(TAILQ_HEAD *head);

void TAILQ_INSERT_AFTER(TAILQ_HEAD *head, struct TYPE *listelm,
                        struct TYPE *elm, TAILQ_ENTRY NAME);

void TAILQ_INSERT_BEFORE(struct TYPE *listelm, struct TYPE *elm,
                         TAILQ_ENTRY NAME);

void TAILQ_INSERT_HEAD(TAILQ_HEAD *head, struct TYPE *elm,
                       TAILQ_ENTRY NAME);

void TAILQ_INSERT_TAIL(TAILQ_HEAD *head, struct TYPE *elm,
                       TAILQ_ENTRY NAME);

struct TYPE *TAILQ_LAST(TAILQ_HEAD *head, HEADNAME);

struct TYPE *TAILQ_NEXT(struct TYPE *elm, TAILQ_ENTRY NAME);

struct TYPE *TAILQ_PREV(struct TYPE *elm, HEADNAME, TAILQ_ENTRY NAME);

void TAILQ_REMOVE(TAILQ_HEAD *head, struct TYPE *elm, TAILQ_ENTRY NAME);</code></pre>
<h2>Description</h2>
<p>These macros define and operate on doubly linked tail queues. In the macro definitions, <i>TYPE</i> is the name of a user defined structure, that must contain a field of type <i>TAILQ_ENTRY</i>, named <i>NAME</i>. The argument <i>HEADNAME</i> is the name of a user defined structure that must be declared using the macro <code>TAILQ_HEAD</code>(). A tail queue is headed by a structure defined by the <code>TAILQ_HEAD</code>() macro. This structure contains a pair of pointers, one to the first element in the tail queue and the other to the last element in the tail queue. The elements are doubly linked so that an arbitrary element can be removed without traversing the tail queue. New elements can be added to the tail queue after an existing element, before an existing element, at the head of the tail queue, or at the end of the tail queue. A <i>TAILQ_HEAD</i> structure is declared as follows: TAILQ_HEAD(HEADNAME, TYPE) head; where <i>struct HEADNAME</i> is the structure to be defined, and <i>struct TYPE</i> is the type of the elements to be linked into the tail queue. A pointer to the head of the tail queue can later be declared as: struct HEADNAME *headp; (The names <i>head</i> and <i>headp</i> are user selectable.) The macro <code>TAILQ_HEAD_INITIALIZER</code>() evaluates to an initializer for the tail queue <i>head</i>. The macro <code>TAILQ_CONCAT</code>() concatenates the tail queue headed by <i>head2</i> onto the end of the one headed by <i>head1</i> removing all entries from the former. The macro <code>TAILQ_EMPTY</code>() evaluates to true if there are no items on the tail queue. The macro <code>TAILQ_ENTRY</code>() declares a structure that connects the elements in the tail queue. The macro <code>TAILQ_FIRST</code>() returns the first item on the tail queue or NULL if the tail queue is empty. The macro <code>TAILQ_FOREACH</code>() traverses the tail queue referenced by <i>head</i> in the forward direction, assigning each element in turn to <i>var</i>. <i>var</i> is set to NULL if the loop completes normally, or if there were no elements. The macro <code>TAILQ_FOREACH_REVERSE</code>() traverses the tail queue referenced by <i>head</i> in the reverse direction, assigning each element in turn to <i>var</i>. The macro <code>TAILQ_INIT</code>() initializes the tail queue referenced by <i>head</i>. The macro <code>TAILQ_INSERT_HEAD</code>() inserts the new element <i>elm</i> at the head of the tail queue. The macro <code>TAILQ_INSERT_TAIL</code>() inserts the new element <i>elm</i> at the end of the tail queue. The macro <code>TAILQ_INSERT_AFTER</code>() inserts the new element <i>elm</i> after the element <i>listelm</i>. The macro <code>TAILQ_INSERT_BEFORE</code>() inserts the new element <i>elm</i> before the element <i>listelm</i>. The macro <code>TAILQ_LAST</code>() returns the last item on the tail queue. If the tail queue is empty the return value is NULL. The macro <code>TAILQ_NEXT</code>() returns the next item on the tail queue, or NULL if this item is the last. The macro <code>TAILQ_PREV</code>() returns the previous item on the tail queue, or NULL if this item is the first. The macro <code>TAILQ_REMOVE</code>() removes the element <i>elm</i> from the tail queue.</p>
<h2>Return Value</h2>
<p><code>TAILQ_EMPTY</code>() returns nonzero if the queue is empty, and zero if the queue contains at least one entry. </p>
<p> <code>TAILQ_FIRST</code>(), <code>TAILQ_LAST</code>(), <code>TAILQ_NEXT</code>(), and <code>TAILQ_PREV</code>() return a pointer to the first, last, next or previous <i>TYPE</i> structure, respectively. </p>
<p> <code>TAILQ_HEAD_INITIALIZER</code>() returns an initializer that can be assigned to the queue <i>head</i>.</p>
<h2>Conforming To</h2>
<p>Not in POSIX.1, POSIX.1-2001 or POSIX.1-2008. Present on the BSDs. (TAILQ functions first appeared in 4.4BSD).</p>
<h2>Bugs</h2>
<p>The macros <code>TAILQ_FOREACH</code>() and <code>TAILQ_FOREACH_REVERSE</code>() don&#8217;t allow <i>var</i> to be removed or freed within the loop, as it would interfere with the traversal. The macros <code>TAILQ_FOREACH_SAFE</code>() and <code>TAILQ_FOREACH_REVERSE_SAFE</code>(), which are present on the BSDs but are not present in glibc, fix this limitation by allowing <i>var</i> to safely be removed from the list and freed from within the loop without interfering with the traversal.</p>
<h2>Examples</h2>
<p>#include &lt;stddef.h&gt;<br />
#include &lt;stdio.h&gt;<br />
#include &lt;stdlib.h&gt;<br />
#include &lt;sys/queue.h&gt;<br />
struct entry {<br />
    int data;<br />
    TAILQ_ENTRY(entry)<br />
    entries; /* Tail queue. */<br />
}; TAILQ_HEAD(tailhead, entry); </p>
<pre><code>int main(void)
{
    struct entry *n1, *n2, *n3, *np;
    struct tailhead head; /* Tail queue head. */
    int i;
    TAILQ_INIT(&amp;head);                 /* Initialize the queue. */
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
    i = 0;
    TAILQ_FOREACH(np, &amp;head, entries)
    np-&gt;data = i++;
    /* Reverse traversal. */
    TAILQ_FOREACH_REVERSE(np, &amp;head, tailhead, entries)
    printf(&quot;%i
&quot;, np-&gt;data);
    /* TailQ Deletion. */
    n1 = TAILQ_FIRST(&amp;head);
    while (n1 != NULL) {
        n2 = TAILQ_NEXT(n1, entries);
        free(n1);
        n1 = n2;
    }
    TAILQ_INIT(&amp;head);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-insque/">insque</a></code>(3), <code><a href="/docs/linux/man/7-queue/">queue</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
