---
title: "stailq(3)"
name: "stailq"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stailq/"
description: "STAILQ_CONCAT, STAILQ_EMPTY, STAILQ_ENTRY, STAILQ_FIRST, STAILQ_FOREACH, STAILQ_HEAD, STAILQ_HEAD_INITIALIZER, STAILQ_INIT, STAILQ_INSERT_AFTER, STAILQ_INSERT_HEAD, STAILQ_INSERT_TAIL, STAILQ_NEXT,..."
---

<p>STAILQ_CONCAT, STAILQ_EMPTY, STAILQ_ENTRY, STAILQ_FIRST, STAILQ_FOREACH, STAILQ_HEAD, STAILQ_HEAD_INITIALIZER, STAILQ_INIT, STAILQ_INSERT_AFTER, STAILQ_INSERT_HEAD, STAILQ_INSERT_TAIL, STAILQ_NEXT, STAILQ_REMOVE, STAILQ_REMOVE_HEAD, &#8211; implementation of a singly linked tail queue</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/queue.h&gt;

void STAILQ_CONCAT(STAILQ_HEAD *head1, STAILQ_HEAD *head2);

int STAILQ_EMPTY(STAILQ_HEAD *head);

STAILQ_ENTRY(TYPE);

struct TYPE *STAILQ_FIRST(STAILQ_HEAD *head);

STAILQ_FOREACH(struct TYPE *var, STAILQ_HEAD *head, STAILQ_ENTRY NAME);

STAILQ_HEAD(HEADNAME, TYPE);

STAILQ_HEAD STAILQ_HEAD_INITIALIZER(STAILQ_HEAD head);

void STAILQ_INIT(STAILQ_HEAD *head);

void STAILQ_INSERT_AFTER(STAILQ_HEAD *head, struct TYPE *listelm,
                         struct TYPE *elm, STAILQ_ENTRY NAME);

void STAILQ_INSERT_HEAD(STAILQ_HEAD *head, struct TYPE *elm,
                        STAILQ_ENTRY NAME);

void STAILQ_INSERT_TAIL(STAILQ_HEAD *head, struct TYPE *elm,
                        STAILQ_ENTRY NAME);

struct TYPE *STAILQ_NEXT(struct TYPE *elm, STAILQ_ENTRY NAME);

void STAILQ_REMOVE(STAILQ_HEAD *head, struct TYPE *elm, TYPE,
                   STAILQ_ENTRY NAME);

void STAILQ_REMOVE_HEAD(STAILQ_HEAD *head, STAILQ_ENTRY NAME);</code></pre>
<h2>Description</h2>
<p>These macros define and operate on singly linked tail queues. In the macro definitions, <i>TYPE</i> is the name of a user-defined structure, that must contain a field of type <i>STAILQ_ENTRY</i>, named <i>NAME</i>. The argument <i>HEADNAME</i> is the name of a user-defined structure that must be declared using the macro <code>STAILQ_HEAD</code>(). A singly linked tail queue is headed by a structure defined by the <code>STAILQ_HEAD</code>() macro. This structure contains a pair of pointers, one to the first element in the tail queue and the other to the last element in the tail queue. The elements are singly linked for minimum space and pointer manipulation overhead at the expense of <a href="/docs/linux/man/n-o/">O</a>(n) removal for arbitrary elements. New elements can be added to the tail queue after an existing element, at the head of the tail queue, or at the end of the tail queue. A <i>STAILQ_HEAD</i> structure is declared as follows: STAILQ_HEAD(HEADNAME, TYPE) head; where <i>struct HEADNAME</i> is the structure to be defined, and <i>struct TYPE</i> is the type of the elements to be linked into the tail queue. A pointer to the head of the tail queue can later be declared as: struct HEADNAME *headp; (The names <i>head</i> and <i>headp</i> are user selectable.) The macro <code>STAILQ_HEAD_INITIALIZER</code>() evaluates to an initializer for the tail queue <i>head</i>. The macro <code>STAILQ_CONCAT</code>() concatenates the tail queue headed by <i>head2</i> onto the end of the one headed by <i>head1</i> removing all entries from the former. The macro <code>STAILQ_EMPTY</code>() evaluates to true if there are no items on the tail queue. The macro <code>STAILQ_ENTRY</code>() declares a structure that connects the elements in the tail queue. The macro <code>STAILQ_FIRST</code>() returns the first item on the tail queue or NULL if the tail queue is empty. The macro <code>STAILQ_FOREACH</code>() traverses the tail queue referenced by <i>head</i> in the forward direction, assigning each element in turn to <i>var</i>. The macro <code>STAILQ_INIT</code>() initializes the tail queue referenced by <i>head</i>. The macro <code>STAILQ_INSERT_HEAD</code>() inserts the new element <i>elm</i> at the head of the tail queue. The macro <code>STAILQ_INSERT_TAIL</code>() inserts the new element <i>elm</i> at the end of the tail queue. The macro <code>STAILQ_INSERT_AFTER</code>() inserts the new element <i>elm</i> after the element <i>listelm</i>. The macro <code>STAILQ_NEXT</code>() returns the next item on the tail queue, or NULL this item is the last. The macro <code>STAILQ_REMOVE_HEAD</code>() removes the element at the head of the tail queue. For optimum efficiency, elements being removed from the head of the tail queue should use this macro explicitly rather than the generic <code>STAILQ_REMOVE</code>() macro. The macro <code>STAILQ_REMOVE</code>() removes the element <i>elm</i> from the tail queue.</p>
<h2>Return Value</h2>
<p><code>STAILQ_EMPTY</code>() returns nonzero if the queue is empty, and zero if the queue contains at least one entry. </p>
<p> <code>STAILQ_FIRST</code>(), and <code>STAILQ_NEXT</code>() return a pointer to the first or next <i>TYPE</i> structure, respectively. </p>
<p> <code>STAILQ_HEAD_INITIALIZER</code>() returns an initializer that can be assigned to the queue <i>head</i>.</p>
<h2>Conforming To</h2>
<p>Not in POSIX.1, POSIX.1-2001 or POSIX.1-2008. Present on the BSDs (STAILQ macros first appeared in 4.4BSD).</p>
<h2>Bugs</h2>
<p>The macro <code>STAILQ_FOREACH</code>() doesn&#8217;t allow <i>var</i> to be removed or freed within the loop, as it would interfere with the traversal. The macro <code>STAILQ_FOREACH_SAFE</code>(), which is present on the BSDs but is not present in glibc, fixes this limitation by allowing <i>var</i> to safely be removed from the list and freed from within the loop without interfering with the traversal.</p>
<h2>Examples</h2>
<p>#include &lt;stddef.h&gt;<br />
#include &lt;stdio.h&gt;<br />
#include &lt;stdlib.h&gt;<br />
#include &lt;sys/queue.h&gt;<br />
struct entry {<br />
    int data;<br />
    STAILQ_ENTRY(entry)<br />
    entries; /* Singly linked tail queue. */<br />
}; STAILQ_HEAD(stailhead, entry); int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct entry&nbsp;*n1,&nbsp;*n2,&nbsp;*n3,&nbsp;*np;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct stailhead head;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Singly linked tail queue<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;head.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;STAILQ_INIT(&amp;head);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Initialize the queue.&nbsp;*/ </p>
<pre><code>n1 = malloc(sizeof(struct entry)); /* Insert at the head. */
STAILQ_INSERT_HEAD(&amp;head, n1, entries);
n1 = malloc(sizeof(struct entry)); /* Insert at the tail. */
STAILQ_INSERT_TAIL(&amp;head, n1, entries);
n2 = malloc(sizeof(struct entry)); /* Insert after. */
STAILQ_INSERT_AFTER(&amp;head, n1, n2, entries);
STAILQ_REMOVE(&amp;head, n2, entry, entries); /* Deletion. */
free(n2);
n3 = STAILQ_FIRST(&amp;head);
STAILQ_REMOVE_HEAD(&amp;head, entries); /* Deletion from the head. */
free(n3);
n1 = STAILQ_FIRST(&amp;head);
n1-&gt;data = 0;
for (int i = 1; i &lt; 5; i++) {
    n1 = malloc(sizeof(struct entry));
    STAILQ_INSERT_HEAD(&amp;head, n1, entries);
    n1-&gt;data = i;
}
/* Forward traversal. */
STAILQ_FOREACH(np, &amp;head, entries)
printf(&quot;%i
&quot;, np-&gt;data);
/* TailQ Deletion. */
n1 = STAILQ_FIRST(&amp;head);
while (n1 != NULL) {
    n2 = STAILQ_NEXT(n1, entries);
    free(n1);
    n1 = n2;
}
STAILQ_INIT(&amp;head);
exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-insque/">insque</a></code>(3), <code><a href="/docs/linux/man/7-queue/">queue</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
