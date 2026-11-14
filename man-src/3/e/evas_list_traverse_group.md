---
title: "evas_list_traverse_group(3)"
name: "evas_list_traverse_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_list_traverse_group/"
description: "Linked List Traverse Functions – Functions that you can use to traverse a linked list."
---

<p>Linked List Traverse Functions &#8211; Functions that you can use to traverse a linked list. </p>
<h3>Functions</h3>
<p>EAPI <code>Evas_List</code> * <code>evas_list_last</code> (const <code>Evas_List</code> *list)<br />
 <i>Get the last list node in the list. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_next</code> (const <code>Evas_List</code> *list)<br />
 <i>Get the next list node after the specified list node. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_prev</code> (const <code>Evas_List</code> *list)<br />
 <i>Get the previous list node before the specified list node. </i></p>
<h2>Detailed Description</h2>
<p>Functions that you can use to traverse a linked list.</p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Evas_List</code>* evas_list_last (const <code>Evas_List</code> * list)</h3>
<p>Get the last list node in the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to get the last list node from</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The last list node in the list list</dl>
<p> This function will return the last list node in the list (or NULL if the list is empty). </p>
<p> NB: This is a order-1 operation (it takes the same short time regardless of the length of the list). </p>
<p> Example: </p>
<pre> extern Evas_List *list;
 Evas_List *last, *l;
 last = evas_list_last(list);
 printf('The list in reverse:);
 for (l = last; l; l = l-&gt;prev)
 {
 printf('%p, l-&gt;data);
 }</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::accounting.</p>
<h3>EAPI <code>Evas_List</code>* evas_list_next (const <code>Evas_List</code> * list)</h3>
<p>Get the next list node after the specified list node. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list node to get the next list node from</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The next list node, or NULL if no next list node exists</dl>
<p> This function returns the next list node after the current one. It is equivalent to list-&gt;next. </p>
<p> Example: </p>
<pre> extern Evas_List *list;
 Evas_List *l;
 printf('The list:);
 for (l = list; l; l = <a href="//www.systutorials.com/docs/linux/man/l-evas_list_next/">evas_list_next</a>(l))
 {
 printf('%p, l-&gt;data);
 }</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::next. </p>
<p> Referenced by evas_list_sort().</p>
<h3>EAPI <code>Evas_List</code>* evas_list_prev (const <code>Evas_List</code> * list)</h3>
<p>Get the previous list node before the specified list node. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list node to get the previous list node from</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The previous list node, or NULL if no previous list node exists</dl>
<p> This function returns the previous list node before the current one. It is equivalent to list-&gt;prev. </p>
<p> Example: </p>
<pre> extern Evas_List *list;
 Evas_List *last, *l;
 last = evas_list_last(list);
 printf('The list in reverse:);
 for (l = last; l; l = <a href="//www.systutorials.com/docs/linux/man/l-evas_list_prev/">evas_list_prev</a>(l))
 {
 printf('%p, l-&gt;data);
 }</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::prev. </p>
<p> Referenced by evas_list_sort().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
