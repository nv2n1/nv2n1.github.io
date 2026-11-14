---
title: "slist_init(3)"
name: "slist_init"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slist_init/"
description: "SLIST_EMPTY, SLIST_ENTRY, SLIST_FIRST, SLIST_FOREACH, SLIST_HEAD, SLIST_HEAD_INITIALIZER, SLIST_INIT, SLIST_INSERT_AFTER, SLIST_INSERT_HEAD, SLIST_NEXT, SLIST_REMOVE, SLIST_REMOVE_HEAD – implementa..."
---

<p>SLIST_EMPTY, SLIST_ENTRY, SLIST_FIRST, SLIST_FOREACH, SLIST_HEAD, SLIST_HEAD_INITIALIZER, SLIST_INIT, SLIST_INSERT_AFTER, SLIST_INSERT_HEAD, SLIST_NEXT, SLIST_REMOVE, SLIST_REMOVE_HEAD &#8211; implementation of a singly linked list </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/queue.h&gt;</code>
<code>int SLIST_EMPTY(SLIST_HEAD *</code><i>head</i><code>);</code>
<code>SLIST_ENTRY(TYPE);</code>
<code>struct TYPE *SLIST_FIRST(SLIST_HEAD *</code><i>head</i><code>);</code>
<code>SLIST_FOREACH(struct TYPE *</code><i>var</i><code>, SLIST_HEAD *</code><i>head</i><code>, SLIST_ENTRY </code><i>NAME</i><code>);</code>
<code>SLIST_HEAD(HEADNAME, TYPE);</code>
<code>SLIST_HEAD SLIST_HEAD_INITIALIZER(SLIST_HEAD </code><i>head</i><code>);</code>
<code>void SLIST_INIT(SLIST_HEAD *</code><i>head</i><code>);</code>
<code>void SLIST_INSERT_AFTER(struct TYPE *</code><i>listelm</i><code>, struct TYPE *</code><i>elm</i><code>,</code>
<code> SLIST_ENTRY </code><i>NAME</i><code>);</code>
<code>void SLIST_INSERT_HEAD(SLIST_HEAD *</code><i>head</i><code>, struct TYPE *</code><i>elm</i><code>,</code>
<code> SLIST_ENTRY </code><i>NAME</i><code>);</code>
<code>struct TYPE *SLIST_NEXT(struct TYPE *</code><i>elm</i><code>, SLIST_ENTRY </code><i>NAME</i><code>);</code>
<code>void SLIST_REMOVE(SLIST_HEAD *</code><i>head</i><code>, struct TYPE *</code><i>elm</i><code>, SLIST_ENTRY </code><i>NAME</i><code>);</code>
<code>void SLIST_REMOVE_HEAD(SLIST_HEAD *</code><i>head</i><code>, SLIST_ENTRY </code><i>NAME</i><code>);</code></pre>
<h2>Description</h2>
<p>These macros define and operate on doubly linked lists. </p>
<p> In the macro definitions, <i>TYPE</i> is the name of a user-defined structure, that must contain a field of type <i>SLIST_ENTRY</i>, named <i>NAME</i>. The argument <i>HEADNAME</i> is the name of a user-defined structure that must be declared using the macro <code>SLIST_HEAD</code>(). </p>
<p> A singly linked list is headed by a structure defined by the <code>SLIST_HEAD</code>() macro. This structure contains a single pointer to the first element on the list. The elements are singly linked for minimum space and pointer manipulation overhead at the expense of <a href="/docs/linux/man/n-o/">O</a>(n) removal for arbitrary elements. New elements can be added to the list after an existing element or at the head of the list. An <i>SLIST_HEAD</i> structure is declared as follows: </p>
<p> SLIST_HEAD(HEADNAME, TYPE) head; </p>
<p> where <i>struct HEADNAME</i> is the structure to be defined, and <i>struct TYPE</i> is the type of the elements to be linked into the list. A pointer to the head of the list can later be declared as: </p>
<p> struct HEADNAME *headp; </p>
<p> (The names <i>head</i> and <i>headp</i> are user selectable.) </p>
<p> The macro <code>SLIST_HEAD_INITIALIZER</code>() evaluates to an initializer for the list <i>head</i>. </p>
<p> The macro <code>SLIST_EMPTY</code>() evaluates to true if there are no elements in the list. </p>
<p> The macro <code>SLIST_ENTRY</code>() declares a structure that connects the elements in the list. </p>
<p> The macro <code>SLIST_FIRST</code>() returns the first element in the list or NULL if the list is empty. </p>
<p> The macro <code>SLIST_FOREACH</code>() traverses the list referenced by <i>head</i> in the forward direction, assigning each element in turn to <i>var</i>. </p>
<p> The macro <code>SLIST_INIT</code>() initializes the list referenced by <i>head</i>. </p>
<p> The macro <code>SLIST_INSERT_HEAD</code>() inserts the new element <i>elm</i> at the head of the list. </p>
<p> The macro <code>SLIST_INSERT_AFTER</code>() inserts the new element <i>elm</i> after the element <i>listelm</i>. </p>
<p> The macro <code>SLIST_NEXT</code>() returns the next element in the list. </p>
<p> The macro <code>SLIST_REMOVE_HEAD</code>() removes the element <i>elm</i> from the head of the list. For optimum efficiency, elements being removed from the head of the list should explicitly use this macro instead of the generic <i>SLIST_REMOVE</i> macro. </p>
<p> The macro <code>SLIST_REMOVE</code>() removes the element <i>elm</i> from the list.</p>
<h2>Return Value</h2>
<p><code>SLIST_EMPTY</code>() returns nonzero if the list is empty, and zero if the list contains at least one entry. </p>
<p> <code>SLIST_FIRST</code>(), and <code>SLIST_NEXT</code>() return a pointer to the first or next <i>TYPE</i> structure, respectively. </p>
<p> <code>SLIST_HEAD_INITIALIZER</code>() returns an initializer that can be assigned to the list <i>head</i>.</p>
<h2>Conforming To</h2>
<p>Not in POSIX.1, POSIX.1-2001 or POSIX.1-2008. Present on the BSDs (SLIST macros first appeared in 4.4BSD).</p>
<h2>Bugs</h2>
<p>The macro <code>SLIST_FOREACH</code>() doesn&#8217;t allow <i>var</i> to be removed or freed within the loop, as it would interfere with the traversal. The macro <code>SLIST_FOREACH_SAFE</code>(), which is present on the BSDs but is not present in glibc, fixes this limitation by allowing <i>var</i> to safely be removed from the list and freed from within the loop without interfering with the traversal.</p>
<h2>Examples</h2>
<p>#include &lt;stddef.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;sys/queue.h&gt; </p>
<p> struct entry {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int data;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SLIST_ENTRY(entry)&nbsp;entries;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Singly linked List.&nbsp;*/ }; </p>
<p> SLIST_HEAD(slisthead, entry); </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct entry&nbsp;*n1,&nbsp;*n2,&nbsp;*n3,&nbsp;*np;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct slisthead head;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Singly linked List<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;head.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SLIST_INIT(&amp;head);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Initialize the queue.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1&nbsp;=&nbsp;malloc(sizeof(struct entry));&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Insert at the head.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SLIST_INSERT_HEAD(&amp;head, n1, entries); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n2&nbsp;=&nbsp;malloc(sizeof(struct entry));&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Insert after.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SLIST_INSERT_AFTER(n1, n2, entries); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SLIST_REMOVE(&amp;head, n2, entry, entries);/*&nbsp;Deletion.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(n2); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n3&nbsp;=&nbsp;SLIST_FIRST(&amp;head);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SLIST_REMOVE_HEAD(&amp;head, entries);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Deletion from the head.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(n3); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int i&nbsp;=&nbsp;0;&nbsp;i&nbsp;&lt;&nbsp;5;&nbsp;i++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1&nbsp;=&nbsp;malloc(sizeof(struct entry));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SLIST_INSERT_HEAD(&amp;head, n1, entries);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1-&gt;data&nbsp;=&nbsp;i;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Forward traversal.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SLIST_FOREACH(np,&nbsp;&amp;head, entries)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%i
&quot;, np-&gt;data); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(!SLIST_EMPTY(&amp;head))&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;List Deletion.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n1&nbsp;=&nbsp;SLIST_FIRST(&amp;head);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SLIST_REMOVE_HEAD(&amp;head, entries);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(n1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SLIST_INIT(&amp;head); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-insque/">insque</a></code>(3), <code><a href="/docs/linux/man/7-queue/">queue</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
