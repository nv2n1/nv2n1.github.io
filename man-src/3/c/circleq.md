---
title: "circleq(3)"
name: "circleq"
section: "3"
letter: "c"
url: "/docs/linux/man/3-circleq/"
description: "CIRCLEQ_EMPTY, CIRCLEQ_ENTRY, CIRCLEQ_FIRST, CIRCLEQ_FOREACH, CIRCLEQ_FOREACH_REVERSE, CIRCLEQ_HEAD, CIRCLEQ_HEAD_INITIALIZER, CIRCLEQ_INIT, CIRCLEQ_INSERT_AFTER, CIRCLEQ_INSERT_BEFORE, CIRCLEQ_INS..."
---

<h2 class="name">NAME</h2>
<p> CIRCLEQ_EMPTY, CIRCLEQ_ENTRY, CIRCLEQ_FIRST, CIRCLEQ_FOREACH, CIRCLEQ_FOREACH_REVERSE, CIRCLEQ_HEAD, CIRCLEQ_HEAD_INITIALIZER, CIRCLEQ_INIT, CIRCLEQ_INSERT_AFTER, CIRCLEQ_INSERT_BEFORE, CIRCLEQ_INSERT_HEAD, CIRCLEQ_INSERT_TAIL, CIRCLEQ_LAST, CIRCLEQ_LOOP_NEXT, CIRCLEQ_LOOP_PREV, CIRCLEQ_NEXT, CIRCLEQ_PREV, CIRCLEQ_REMOVE &#8211; implementation of a doubly linked circular queue </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/queue.h&gt;
int CIRCLEQ_EMPTY(CIRCLEQ_HEAD *head);
CIRCLEQ_ENTRY(TYPE);
struct TYPE *CIRCLEQ_FIRST(CIRCLEQ_HEAD *head);
CIRCLEQ_FOREACH(struct TYPE *var, CIRCLEQ_HEAD *head,
                CIRCLEQ_ENTRY NAME);
CIRCLEQ_FOREACH_REVERSE(struct TYPE *var, CIRCLEQ_HEAD *head,
                        CIRCLEQ_ENTRY NAME);
CIRCLEQ_HEAD(HEADNAME, TYPE);
CIRCLEQ_HEAD CIRCLEQ_HEAD_INITIALIZER(CIRCLEQ_HEAD head);
void CIRCLEQ_INIT(CIRCLEQ_HEAD *head);
void CIRCLEQ_INSERT_AFTER(CIRCLEQ_HEAD *head, struct TYPE *listelm,
                          struct TYPE *elm, CIRCLEQ_ENTRY NAME);
void CIRCLEQ_INSERT_BEFORE(CIRCLEQ_HEAD *head, struct TYPE *listelm,
                           struct TYPE *elm, CIRCLEQ_ENTRY NAME);
void CIRCLEQ_INSERT_HEAD(CIRCLEQ_HEAD *head, struct TYPE *elm,
                         CIRCLEQ_ENTRY NAME);
void CIRCLEQ_INSERT_TAIL(CIRCLEQ_HEAD *head, struct TYPE *elm,
                         CIRCLEQ_ENTRY NAME);
struct TYPE *CIRCLEQ_LAST(CIRCLEQ_HEAD *head);
void CIRCLEQ_LOOP_NEXT(CIRCLEQ_HEAD *head, struct TYPE *elm,
                       CIRCLEQ_ENTRY NAME);
void CIRCLEQ_LOOP_PREV(CIRCLEQ_HEAD *head, struct TYPE *elm,
                       CIRCLEQ_ENTRY NAME);
struct TYPE *CIRCLEQ_NEXT(struct TYPE *elm, CIRCLEQ_ENTRY NAME);
struct TYPE *CIRCLEQ_PREV(struct TYPE *elm, CIRCLEQ_ENTRY NAME);
void CIRCLEQ_REMOVE(CIRCLEQ_HEAD *head, struct TYPE *elm,
                    CIRCLEQ_ENTRY NAME);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These macros define and operate on doubly linked circular queues. </p>
<p> In the macro definitions, <i>TYPE</i> is the name of a user-defined structure, that must contain a field of type <i>CIRCLEQ_ENTRY</i>, named <i>NAME</i>. The argument <i>HEADNAME</i> is the name of a user-defined structure that must be declared using the macro <code>CIRCLEQ_HEAD</code>(). </p>
<p> A circular queue is headed by a structure defined by the <code>CIRCLEQ_HEAD</code>() macro. This structure contains a pair of pointers, one to the first element in the circular queue and the other to the last element in the circular queue. The elements are doubly linked so that an arbitrary element can be removed without traversing the circular queue. New elements can be added to the circular queue after an existing element, before an existing element, at the head of the circular queue, or at the end of the circular queue. A <i>CIRCLEQ_HEAD</i> structure is declared as follows: </p>
<p> CIRCLEQ_HEAD(HEADNAME, TYPE) head; </p>
<p> where <i>struct HEADNAME</i> is the structure to be defined, and <i>struct TYPE</i> is the type of the elements to be linked into the circular queue. A pointer to the head of the circular queue can later be declared as: </p>
<p> struct HEADNAME *headp; </p>
<p> (The names <i>head</i> and <i>headp</i> are user selectable.) </p>
<p> The macro <code>CIRCLEQ_HEAD_INITIALIZER</code>() evaluates to an initializer for the circular queue <i>head</i>. </p>
<p> The macro <code>CIRCLEQ_EMPTY</code>() evaluates to true if there are no items on the circular queue. </p>
<p> The macro <code>CIRCLEQ_ENTRY</code>() declares a structure that connects the elements in the circular queue. </p>
<p> The macro <code>CIRCLEQ_FIRST</code>() returns the first item on the circular queue. </p>
<p> The macro <code>CIRCLEQ_FOREACH</code>() traverses the circular queue referenced by <i>head</i> in the forward direction, assigning each element in turn to <i>var</i>. <i>var</i> is set to <i>&amp;head</i> if the loop completes normally, or if there were no elements. </p>
<p> The macro <code>CIRCLEQ_FOREACH_REVERSE</code>() traverses the circular queue referenced by <i>head</i> in the reverse direction, assigning each element in turn to <i>var</i>. </p>
<p> The macro <code>CIRCLEQ_INIT</code>() initializes the circular queue referenced by <i>head</i>. </p>
<p> The macro <code>CIRCLEQ_INSERT_HEAD</code>() inserts the new element <i>elm</i> at the head of the circular queue. </p>
<p> The macro <code>CIRCLEQ_INSERT_TAIL</code>() inserts the new element <i>elm</i> at the end of the circular queue. </p>
<p> The macro <code>CIRCLEQ_INSERT_AFTER</code>() inserts the new element <i>elm</i> after the element <i>listelm</i>. </p>
<p> The macro <code>CIRCLEQ_INSERT_BEFORE</code>() inserts the new element <i>elm</i> before the element <i>listelm</i>. </p>
<p> The macro <code>CIRCLEQ_LAST</code>() returns the last item on the circular queue. </p>
<p> The macro <code>CIRCLEQ_NEXT</code>() returns the next item on the circular queue, or <i>&amp;head</i> if this item is the last one. </p>
<p> The macro <code>CIRCLEQ_PREV</code>() returns the previous item on the circular queue, or <i>&amp;head</i> if this item is the first one. </p>
<p> The macro <code>CIRCLEQ_LOOP_NEXT</code>() returns the next item on the circular queue. If <i>elm</i> is the last element on the circular queue, the first element is returned. </p>
<p> The macro <code>CIRCLEQ_LOOP_PREV</code>() returns the previous item on the circular queue. If <i>elm</i> is the first element on the circular queue, the last element is returned. </p>
<p> The macro <code>CIRCLEQ_REMOVE</code>() removes the element <i>elm</i> from the circular queue.</p>
<h2>RETURN VALUE</h2>
<p> <code>CIRCLEQ_EMPTY</code>() returns nonzero if the queue is empty, and zero if the queue contains at least one entry. </p>
<p> <code>CIRCLEQ_FIRST</code>(), <code>CIRCLEQ_LAST</code>(), <code>CIRCLEQ_NEXT</code>(), and <code>CIRCLEQ_PREV</code>() return a pointer to the first, last, next or previous <i>TYPE</i> structure, respectively. </p>
<p> <code>CIRCLEQ_HEAD_INITIALIZER</code>() returns an initializer that can be assigned to the queue <i>head</i>.</p>
<h2>CONFORMING TO</h2>
<p> Not in POSIX.1, POSIX.1-2001 or POSIX.1-2008. Present on the BSDs (CIRCLEQ macros first appeared in 4.4BSD).</p>
<h2>BUGS</h2>
<p> The macros <code>CIRCLEQ_FOREACH</code>() and <code>CIRCLEQ_FOREACH_REVERSE</code>() don&#8217;t allow <i>var</i> to be removed or freed within the loop, as it would interfere with the traversal. The macros <code>CIRCLEQ_FOREACH_SAFE</code>() and <code>CIRCLEQ_FOREACH_REVERSE_SAFE</code>(), which are present on the BSDs but are not present in glibc, fix this limitation by allowing <i>var</i> to safely be removed from the list and freed from within the loop without interfering with the traversal.</p>
<h2>EXAMPLES</h2>
<p> #include &lt;stddef.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;sys/queue.h&gt; </p>
<p> struct entry {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int data;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CIRCLEQ_ENTRY(entry)&nbsp;entries;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Queue.&nbsp;*/ }; </p>
<p> CIRCLEQ_HEAD(circlehead, entry); </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct entry&nbsp;*n1,&nbsp;*n2,&nbsp;*n3,&nbsp;*np;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct circlehead head;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Queue head.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int i; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CIRCLEQ_INIT(&amp;head);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Initialize the queue.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1&nbsp;=&nbsp;malloc(sizeof(struct entry));&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Insert at the head.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CIRCLEQ_INSERT_HEAD(&amp;head, n1, entries); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1&nbsp;=&nbsp;malloc(sizeof(struct entry));&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Insert at the tail.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CIRCLEQ_INSERT_TAIL(&amp;head, n1, entries); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n2&nbsp;=&nbsp;malloc(sizeof(struct entry));&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Insert after.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CIRCLEQ_INSERT_AFTER(&amp;head, n1, n2, entries); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n3&nbsp;=&nbsp;malloc(sizeof(struct entry));&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Insert before.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CIRCLEQ_INSERT_BEFORE(&amp;head, n2, n3, entries); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CIRCLEQ_REMOVE(&amp;head, n2, entries);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Deletion.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(n2);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Forward traversal.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;i&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CIRCLEQ_FOREACH(np,&nbsp;&amp;head, entries)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;np-&gt;data&nbsp;=&nbsp;i++;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Reverse traversal.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CIRCLEQ_FOREACH_REVERSE(np,&nbsp;&amp;head, entries)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%i
&quot;, np-&gt;data);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Queue deletion.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1&nbsp;=&nbsp;CIRCLEQ_FIRST(&amp;head);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(n1&nbsp;!=&nbsp;(void&nbsp;*)&amp;head)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n2&nbsp;=&nbsp;CIRCLEQ_NEXT(n1, entries);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(n1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1&nbsp;=&nbsp;n2;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CIRCLEQ_INIT(&amp;head); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-insque/">insque</a></code>(3), <code><a href="/docs/linux/man/7-queue/">queue</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
