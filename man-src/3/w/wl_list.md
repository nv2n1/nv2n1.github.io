---
title: "wl_list(3)"
name: "wl_list"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wl_list/"
---

wl_list - 

 doubly-linked list

<h2>Synopsis</h2>

<pre><code>

#include &lt;wayland-util.h&gt;

Public Attributes
struct wl_list * prev



struct wl_list * next</code></pre>

<h2>Detailed Description</h2>

doubly-linked list 

 The list head is of 'struct wl_list' type, and must be initialized using wl_list_init(). All entries in the list must be of the same type. The item type must have a 'struct wl_list' member. This member will be initialized by wl_list_insert(). There is no need to call wl_list_init() on the individual item. To query if the list is empty in <a HREF="/docs/linux/man/1-o/">O</a>(1), use wl_list_empty(). 

 Let's call the list reference 'struct wl_list foo_list', the item type as 'item_t', and the item member as 'struct wl_list link'. 

 The following code will initialize a list: 

 <pre> struct wl_list foo_list;
 struct item_t {
 int foo;
 struct wl_list link;
 };
 struct item_t item1, item2, item3;
 wl_list_init(&amp;foo_list);
 wl_list_insert(&amp;foo_list, &amp;item1.link); Pushes item1 at the head
 wl_list_insert(&amp;foo_list, &amp;item2.link); Pushes item2 at the head
 wl_list_insert(&amp;item2.link, &amp;item3.link); Pushes item3 after item2</pre>The list now looks like [item2, item3, item1] 

 Will iterate the list in ascending order: 

 <pre> item_t *item;
 wl_list_for_each(item, foo_list, link) {
 Do_something_with_item(item);</pre>&nbsp;<wbr>

<h2>Author</h2>

Generated automatically by Doxygen for Wayland from the source code.
