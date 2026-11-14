---
title: "stailq_insert_head(3)"
name: "stailq_insert_head"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stailq_insert_head/"
description: "STAILQ_CONCAT, STAILQ_EMPTY, STAILQ_ENTRY, STAILQ_FIRST, STAILQ_FOREACH, STAILQ_HEAD, STAILQ_HEAD_INITIALIZER, STAILQ_INIT, STAILQ_INSERT_AFTER, STAILQ_INSERT_HEAD, STAILQ_INSERT_TAIL, STAILQ_NEXT,..."
---

<p>STAILQ_CONCAT, STAILQ_EMPTY, STAILQ_ENTRY, STAILQ_FIRST, STAILQ_FOREACH, STAILQ_HEAD, STAILQ_HEAD_INITIALIZER, STAILQ_INIT, STAILQ_INSERT_AFTER, STAILQ_INSERT_HEAD, STAILQ_INSERT_TAIL, STAILQ_NEXT, STAILQ_REMOVE, STAILQ_REMOVE_HEAD, &#8211; implementation of a singly linked tail queue </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/queue.h&gt;</code>
<code>void STAILQ_CONCAT(STAILQ_HEAD *</code><i>head1</i><code>, STAILQ_HEAD *</code><i>head2</i><code>);</code>
<code>int STAILQ_EMPTY(STAILQ_HEAD *</code><i>head</i><code>);</code>
<code>STAILQ_ENTRY(TYPE);</code>
<code>struct TYPE *STAILQ_FIRST(STAILQ_HEAD *</code><i>head</i><code>);</code>
<code>STAILQ_FOREACH(struct TYPE *</code><i>var</i><code>, STAILQ_HEAD *</code><i>head</i><code>, STAILQ_ENTRY </code><i>NAME</i><code>);</code>
<code>STAILQ_HEAD(HEADNAME, TYPE);</code>
<code>STAILQ_HEAD STAILQ_HEAD_INITIALIZER(STAILQ_HEAD </code><i>head</i><code>);</code>
<code>void STAILQ_INIT(STAILQ_HEAD *</code><i>head</i><code>);</code>
<code>void STAILQ_INSERT_AFTER(STAILQ_HEAD *</code><i>head</i><code>, struct TYPE *</code><i>listelm</i><code>,</code>
<code> struct TYPE *</code><i>elm</i><code>, STAILQ_ENTRY </code><i>NAME</i><code>);</code>
<code>void STAILQ_INSERT_HEAD(STAILQ_HEAD *</code><i>head</i><code>, struct TYPE *</code><i>elm</i><code>,</code>
<code> STAILQ_ENTRY </code><i>NAME</i><code>);</code>
<code>void STAILQ_INSERT_TAIL(STAILQ_HEAD *</code><i>head</i><code>, struct TYPE *</code><i>elm</i><code>,</code>
<code> STAILQ_ENTRY </code><i>NAME</i><code>);</code>
<code>struct TYPE *STAILQ_NEXT(struct TYPE *</code><i>elm</i><code>, STAILQ_ENTRY </code><i>NAME</i><code>);</code>
<code>void STAILQ_REMOVE(STAILQ_HEAD *</code><i>head</i><code>, struct TYPE *</code><i>elm</i><code>, TYPE,</code>
<code> STAILQ_ENTRY </code><i>NAME</i><code>);</code>
<code>void STAILQ_REMOVE_HEAD(STAILQ_HEAD *</code><i>head</i><code>, STAILQ_ENTRY </code><i>NAME</i><code>);</code></pre>
<h2>Description</h2>
<p>These macros define and operate on singly linked tail queues. </p>
<p> In the macro definitions, <i>TYPE</i> is the name of a user-defined structure, that must contain a field of type <i>STAILQ_ENTRY</i>, named <i>NAME</i>. The argument <i>HEADNAME</i> is the name of a user-defined structure that must be declared using the macro <code>STAILQ_HEAD</code>(). </p>
<p> A singly linked tail queue is headed by a structure defined by the <code>STAILQ_HEAD</code>() macro. This structure contains a pair of pointers, one to the first element in the tail queue and the other to the last element in the tail queue. The elements are singly linked for minimum space and pointer manipulation overhead at the expense of <a href="/docs/linux/man/n-o/">O</a>(n) removal for arbitrary elements. New elements can be added to the tail queue after an existing element, at the head of the tail queue, or at the end of the tail queue. A <i>STAILQ_HEAD</i> structure is declared as follows: </p>
<p> STAILQ_HEAD(HEADNAME, TYPE) head; </p>
<p> where <i>struct HEADNAME</i> is the structure to be defined, and <i>struct TYPE</i> is the type of the elements to be linked into the tail queue. A pointer to the head of the tail queue can later be declared as: </p>
<p> struct HEADNAME *headp; </p>
<p> (The names <i>head</i> and <i>headp</i> are user selectable.) </p>
<p> The macro <code>STAILQ_HEAD_INITIALIZER</code>() evaluates to an initializer for the tail queue <i>head</i>. </p>
<p> The macro <code>STAILQ_CONCAT</code>() concatenates the tail queue headed by <i>head2</i> onto the end of the one headed by <i>head1</i> removing all entries from the former. </p>
<p> The macro <code>STAILQ_EMPTY</code>() evaluates to true if there are no items on the tail queue. </p>
<p> The macro <code>STAILQ_ENTRY</code>() declares a structure that connects the elements in the tail queue. </p>
<p> The macro <code>STAILQ_FIRST</code>() returns the first item on the tail queue or NULL if the tail queue is empty. </p>
<p> The macro <code>STAILQ_FOREACH</code>() traverses the tail queue referenced by <i>head</i> in the forward direction, assigning each element in turn to <i>var</i>. </p>
<p> The macro <code>STAILQ_INIT</code>() initializes the tail queue referenced by <i>head</i>. </p>
<p> The macro <code>STAILQ_INSERT_HEAD</code>() inserts the new element <i>elm</i> at the head of the tail queue. </p>
<p> The macro <code>STAILQ_INSERT_TAIL</code>() inserts the new element <i>elm</i> at the end of the tail queue. </p>
<p> The macro <code>STAILQ_INSERT_AFTER</code>() inserts the new element <i>elm</i> after the element <i>listelm</i>. </p>
<p> The macro <code>STAILQ_NEXT</code>() returns the next item on the tail queue, or NULL this item is the last. </p>
<p> The macro <code>STAILQ_REMOVE_HEAD</code>() removes the element at the head of the tail queue. For optimum efficiency, elements being removed from the head of the tail queue should use this macro explicitly rather than the generic <code>STAILQ_REMOVE</code>() macro. </p>
<p> The macro <code>STAILQ_REMOVE</code>() removes the element <i>elm</i> from the tail queue.</p>
<h2>Return Value</h2>
<p><code>STAILQ_EMPTY</code>() returns nonzero if the queue is empty, and zero if the queue contains at least one entry. </p>
<p> <code>STAILQ_FIRST</code>(), and <code>STAILQ_NEXT</code>() return a pointer to the first or next <i>TYPE</i> structure, respectively. </p>
<p> <code>STAILQ_HEAD_INITIALIZER</code>() returns an initializer that can be assigned to the queue <i>head</i>.</p>
<h2>Conforming To</h2>
<p>Not in POSIX.1, POSIX.1-2001 or POSIX.1-2008. Present on the BSDs (STAILQ macros first appeared in 4.4BSD).</p>
<h2>Bugs</h2>
<p>The macro <code>STAILQ_FOREACH</code>() doesn&#8217;t allow <i>var</i> to be removed or freed within the loop, as it would interfere with the traversal. The macro <code>STAILQ_FOREACH_SAFE</code>(), which is present on the BSDs but is not present in glibc, fixes this limitation by allowing <i>var</i> to safely be removed from the list and freed from within the loop without interfering with the traversal.</p>
<h2>Examples</h2>
<p>#include &lt;stddef.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;sys/queue.h&gt; </p>
<p> struct entry {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int data;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;STAILQ_ENTRY(entry)&nbsp;entries;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Singly linked tail queue.&nbsp;*/ }; </p>
<p> STAILQ_HEAD(stailhead, entry); </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct entry&nbsp;*n1,&nbsp;*n2,&nbsp;*n3,&nbsp;*np;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct stailhead head;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Singly linked tail queue<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;head.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;STAILQ_INIT(&amp;head);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Initialize the queue.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1&nbsp;=&nbsp;malloc(sizeof(struct entry));&nbsp;<wbr>&nbsp;/*&nbsp;Insert at the head.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;STAILQ_INSERT_HEAD(&amp;head, n1, entries); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1&nbsp;=&nbsp;malloc(sizeof(struct entry));&nbsp;<wbr>&nbsp;/*&nbsp;Insert at the tail.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;STAILQ_INSERT_TAIL(&amp;head, n1, entries); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n2&nbsp;=&nbsp;malloc(sizeof(struct entry));&nbsp;<wbr>&nbsp;/*&nbsp;Insert after.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;STAILQ_INSERT_AFTER(&amp;head, n1, n2, entries); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;STAILQ_REMOVE(&amp;head, n2, entry, entries);/*&nbsp;Deletion.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(n2); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n3&nbsp;=&nbsp;STAILQ_FIRST(&amp;head);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;STAILQ_REMOVE_HEAD(&amp;head, entries);&nbsp;/*&nbsp;Deletion from the head.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(n3); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1&nbsp;=&nbsp;STAILQ_FIRST(&amp;head);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1-&gt;data&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int i&nbsp;=&nbsp;1;&nbsp;i&nbsp;&lt;&nbsp;5;&nbsp;i++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1&nbsp;=&nbsp;malloc(sizeof(struct entry));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;STAILQ_INSERT_HEAD(&amp;head, n1, entries);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1-&gt;data&nbsp;=&nbsp;i;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Forward traversal.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;STAILQ_FOREACH(np,&nbsp;&amp;head, entries)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%i
&quot;, np-&gt;data);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;TailQ Deletion.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1&nbsp;=&nbsp;STAILQ_FIRST(&amp;head);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(n1&nbsp;!=&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n2&nbsp;=&nbsp;STAILQ_NEXT(n1, entries);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(n1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1&nbsp;=&nbsp;n2;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;STAILQ_INIT(&amp;head); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-insque/">insque</a></code>(3), <code><a href="/docs/linux/man/7-queue/">queue</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
