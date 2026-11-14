---
title: "qblist-h(3)"
name: "qblist-h"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qblist-h/"
description: "qblist.h –"
---

<p>qblist.h &#8211; </p>
<p> This is a kernel style list implementation.</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;stdint.h&gt;

#include &lt;qb/qbdefs.h&gt;</code></pre>
<h3>Data Structures</h3>
<pre><code>struct qb_list_head



Macros
#define QB_LIST_DECLARE(name) struct qb_list_head name = {&amp;(name), &amp;(name)}


Declare and initialize a list head.

#define QB_INIT_LIST_HEAD(ptr)

#define qb_list_entry(ptr, type, member) ((type *)((char *)(ptr) - (char *)(&amp;((type *)0)-&gt;member)))


Get the struct for this entry.

#define qb_list_first_entry(ptr, type, member) qb_list_entry((ptr)-&gt;next, type, member)


Get the first element from a list.

#define qb_list_for_each(pos, head) for (pos = (head)-&gt;next; pos != (head); pos = pos-&gt;next)


Iterate over a list.

#define qb_list_for_each_reverse(pos, head) for (pos = (head)-&gt;prev; pos != (head); pos = pos-&gt;prev)


Iterate over a list backwards.

#define qb_list_for_each_safe(pos, n, head)


Iterate over a list safe against removal of list entry.

#define qb_list_for_each_entry(pos, head, member)


Iterate over list of given type.

#define qb_list_for_each_entry_reverse(pos, head, member)


Iterate backwards over list of given type.

#define qb_list_for_each_entry_safe(pos, n, head, member)


Iterate over list of given type safe against removal of list entry.

#define qb_list_for_each_entry_safe_reverse(pos, n, head, member)


Iterate backwards over list safe against removal.

#define qb_list_for_each_entry_from(pos, head, member)


Iterate over list of given type from the current point.



Functions</code></pre>
<p> static void <code>qb_list_init</code> (struct <code>qb_list_head</code> *head)<br />
 <i>Initialize the list entry. </i><br />
 static void <code>qb_list_add</code> (struct <code>qb_list_head</code> *element, struct <code>qb_list_head</code> *head)<br />
 <i>Add this element to the list. </i><br />
 static void <code>qb_list_add_tail</code> (struct <code>qb_list_head</code> *element, struct <code>qb_list_head</code> *head)<br />
 <i>Add to the list (but at the end of the list). </i><br />
 static void <code>qb_list_del</code> (struct <code>qb_list_head</code> *_remove)<br />
 <i>Delete an entry from the list. </i><br />
 static void <code>qb_list_replace</code> (struct <code>qb_list_head</code> *old, struct <code>qb_list_head</code> *new)<br />
 <i>Replace old entry by new one. </i><br />
 static int <code>qb_list_is_last</code> (const struct <code>qb_list_head</code> *list, const struct <code>qb_list_head</code> *head)<br />
 <i>Tests whether list is the last entry in list head. </i><br />
 static int32_t <code>qb_list_empty</code> (const struct <code>qb_list_head</code> *head)<br />
 <i>A quick test to see if the list is empty (pointing to it&#8217;s self). </i><br />
 static void <code>qb_list_splice</code> (struct <code>qb_list_head</code> *list, struct <code>qb_list_head</code> *head)<br />
 <i>Join two lists. </i><br />
 static void <code>qb_list_splice_tail</code> (struct <code>qb_list_head</code> *list, struct <code>qb_list_head</code> *head)<br />
 <i>Join two lists, each list being a queue. </i><br />
 static int32_t <code>qb_list_length</code> (struct <code>qb_list_head</code> *head)<br />
 <i>Count the number of items in the list. </i></p>
<h2>Detailed Description</h2>
<p>This is a kernel style list implementation. </p>
<p> <code>Author:</code></p>
<dl>
<dd>Steven Dake sdake [at] redhat.com</dl>
<h2>Macro Definition Documentation</h2>
<h3>#define QB_INIT_LIST_HEAD(ptr)</h3>
<p><code>Value:</code> </p>
<pre>do { (ptr)-&gt;next = (ptr); (ptr)-&gt;prev = (ptr); } while (0)</pre>
<h3>#define QB_LIST_DECLARE(name) struct <code>qb_list_head</code> name = { &amp;(name), &amp;(name) }</h3>
<p>Declare and initialize a list head.</p>
<h3>#define qb_list_entry(ptr, type, member) ((type *)((char *)(ptr)-(char*)(&amp;((type *)0)-&gt;member)))</h3>
<p>Get the struct for this entry. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr,:</i> the &amp;struct list_head pointer.<br />
 <i>type,:</i> the type of the struct this is embedded in.<br />
 <i>member,:</i> the name of the list_struct within the struct.</dl>
<h3>#define qb_list_first_entry(ptr, type, member) <code>qb_list_entry</code>((ptr)-&gt;next, type, member)</h3>
<p>Get the first element from a list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr,:</i> the &amp;struct list_head pointer.<br />
 <i>type,:</i> the type of the struct this is embedded in.<br />
 <i>member,:</i> the name of the list_struct within the struct.</dl>
<h3>#define qb_list_for_each(pos, head) for (pos = (head)-&gt;next; pos != (head); pos = pos-&gt;next)</h3>
<p>Iterate over a list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>pos,:</i> the &amp;struct list_head to use as a loop counter.<br />
 <i>head,:</i> the head for your list.</dl>
<p> Referenced by qb_list_length().</p>
<h3>#define qb_list_for_each_entry(pos, head, member)</h3>
<p><code>Value:</code> </p>
<pre>for (pos = qb_list_entry((head)-&gt;next, typeof(*pos), member); &amp;pos-&gt;member != (head); pos = qb_list_entry(pos-&gt;member.next, typeof(*pos), member))</pre>
<p>Iterate over list of given type. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>pos,:</i> the type * to use as a loop counter.<br />
 <i>head,:</i> the head for your list.<br />
 <i>member,:</i> the name of the list_struct within the struct.</dl>
<h3>#define qb_list_for_each_entry_from(pos, head, member)</h3>
<p><code>Value:</code> </p>
<pre>for (; &amp;pos-&gt;member != (head); pos = qb_list_entry(pos-&gt;member.next, typeof(*pos), member))</pre>
<p>Iterate over list of given type from the current point. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>pos,:</i> the type * to use as a loop cursor.<br />
 <i>head,:</i> the head for your list.<br />
 <i>member,:</i> the name of the list_struct within the struct.</dl>
<h3>#define qb_list_for_each_entry_reverse(pos, head, member)</h3>
<p><code>Value:</code> </p>
<pre>for (pos = qb_list_entry((head)-&gt;prev, typeof(*pos), member); &amp;pos-&gt;member != (head); pos = qb_list_entry(pos-&gt;member.prev, typeof(*pos), member))</pre>
<p>Iterate backwards over list of given type. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>pos,:</i> the type to use as a loop counter.<br />
 <i>head,:</i> the head for your list.<br />
 <i>member,:</i> the name of the list_struct within the struct.</dl>
<h3>#define qb_list_for_each_entry_safe(pos, n, head, member)</h3>
<p><code>Value:</code> </p>
<pre>for (pos = qb_list_entry((head)-&gt;next, typeof(*pos), member), n = qb_list_entry(pos-&gt;member.next, typeof(*pos), member); &amp;pos-&gt;member != (head); pos = n, n = qb_list_entry(n-&gt;member.next, typeof(*n), member))</pre>
<p>Iterate over list of given type safe against removal of list entry. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>pos,:</i> the type * to use as a loop cursor.<br />
 <i>n,:</i> another type * to use as temporary storage<br />
 <i>head,:</i> the head for your list.<br />
 <i>member,:</i> the name of the list_struct within the struct.</dl>
<h3>#define qb_list_for_each_entry_safe_reverse(pos, n, head, member)</h3>
<p><code>Value:</code> </p>
<pre>for (pos = qb_list_entry((head)-&gt;prev, typeof(*pos), member), n = qb_list_entry(pos-&gt;member.prev, typeof(*pos), member); &amp;pos-&gt;member != (head); pos = n, n = qb_list_entry(n-&gt;member.prev, typeof(*n), member))</pre>
<p>Iterate backwards over list safe against removal. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>pos,:</i> the type * to use as a loop cursor.<br />
 <i>n,:</i> another type * to use as temporary storage<br />
 <i>head,:</i> the head for your list.<br />
 <i>member,:</i> the name of the list_struct within the struct.</dl>
<h3>#define qb_list_for_each_reverse(pos, head) for (pos = (head)-&gt;prev; pos != (head); pos = pos-&gt;prev)</h3>
<p>Iterate over a list backwards. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>pos,:</i> the &amp;struct list_head to use as a loop counter.<br />
 <i>head,:</i> the head for your list.</dl>
<h3>#define qb_list_for_each_safe(pos, n, head)</h3>
<p><code>Value:</code> </p>
<pre>for (pos = (head)-&gt;next, n = pos-&gt;next; pos != (head); pos = n, n = pos-&gt;next)</pre>
<p>Iterate over a list safe against removal of list entry. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>pos,:</i> the &amp;struct list_head to use as a loop counter.<br />
 <i>n,:</i> another &amp;struct list_head to use as temporary storage<br />
 <i>head,:</i> the head for your list.</dl>
<h2>Function Documentation</h2>
<h3>static void qb_list_add (struct <code>qb_list_head</code> *element, struct <code>qb_list_head</code> *head) [inline], [static]</h3>
<p>Add this element to the list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>element</i> the new element to insert.<br />
 <i>head</i> pointer to the list head</dl>
<p> References qb_list_head::next, and qb_list_head::prev.</p>
<h3>static void qb_list_add_tail (struct <code>qb_list_head</code> *element, struct <code>qb_list_head</code> *head) [inline], [static]</h3>
<p>Add to the list (but at the end of the list). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>element</i> pointer to the element to add<br />
 <i>head</i> pointer to the list head</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_list_add()</code></dl>
<p> References qb_list_head::next, and qb_list_head::prev.</p>
<h3>static void qb_list_del (struct <code>qb_list_head</code> *_remove) [inline], [static]</h3>
<p>Delete an entry from the list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>_remove</i> the list item to remove</dl>
<p> References qb_list_head::next, and qb_list_head::prev.</p>
<h3>static int32_t qb_list_empty (const struct <code>qb_list_head</code> *head) [inline], [static]</h3>
<p>A quick test to see if the list is empty (pointing to it&#8217;s self). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>head</i> pointer to the list head</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>boolean true/false</dl>
<p> References qb_list_head::next. </p>
<p> Referenced by qb_list_splice(), and qb_list_splice_tail().</p>
<h3>static void qb_list_init (struct <code>qb_list_head</code> *head) [inline], [static]</h3>
<p>Initialize the list entry. Points next and prev pointers to head. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>head</i> pointer to the list head</dl>
<p> References qb_list_head::next, and qb_list_head::prev.</p>
<h3>static int qb_list_is_last (const struct <code>qb_list_head</code> *list, const struct <code>qb_list_head</code> *head) [inline], [static]</h3>
<p>Tests whether list is the last entry in list head. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>list,:</i> the entry to test<br />
 <i>head,:</i> the head of the list</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>boolean true/false</dl>
<p> References qb_list_head::next.</p>
<h3>static int32_t qb_list_length (struct <code>qb_list_head</code> *head) [inline], [static]</h3>
<p>Count the number of items in the list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>head,:</i> the head for your list.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>length of the list.</dl>
<p> References qb_list_for_each.</p>
<h3>static void qb_list_replace (struct <code>qb_list_head</code> *old, struct <code>qb_list_head</code> *new) [inline], [static]</h3>
<p>Replace old entry by new one. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>old,:</i> the element to be replaced<br />
 <i>new,:</i> the new element to insert</dl>
<p> References qb_list_head::next, and qb_list_head::prev.</p>
<h3>static void qb_list_splice (struct <code>qb_list_head</code> *list, struct <code>qb_list_head</code> *head) [inline], [static]</h3>
<p>Join two lists. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>list</i> the new list to add.<br />
 <i>head</i> the place to add it in the first list.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>The &#8216;list&#8217; is reinitialised</dl>
<p> References qb_list_head::next, qb_list_head::prev, and qb_list_empty().</p>
<h3>static void qb_list_splice_tail (struct <code>qb_list_head</code> *list, struct <code>qb_list_head</code> *head) [inline], [static]</h3>
<p>Join two lists, each list being a queue. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>list,:</i> the new list to add.<br />
 <i>head,:</i> the place to add it in the first list.</dl>
<p> References qb_list_head::next, qb_list_head::prev, and qb_list_empty().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libqb from the source code.</p>
