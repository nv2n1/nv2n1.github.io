---
title: "zlist(3)"
name: "zlist"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlist/"
description: "zlist – simple generic list container"
---

<p>zlist &#8211; simple generic list container</p>
<h2>Synopsis</h2>
<pre><code>// Comparison function e.g. for sorting and removing.
typedef int(zlist_compare_fn)(
    void *item1, void *item2);

// Callback function for zlist_freefn method
typedef void(zlist_free_fn)(
    void *data);

//  Create a new list container
CZMQ_EXPORT zlist_t *
zlist_new();

//  Destroy a list container
CZMQ_EXPORT void
zlist_destroy(zlist_t **self_p);

//  Return the item at the head of list. If the list is empty, returns NULL.
//  Leaves cursor pointing at the head item, or NULL if the list is empty.
CZMQ_EXPORT void *
zlist_first(zlist_t *self);

//  Return the next item. If the list is empty, returns NULL. To move to
//  the start of the list call zlist_first (). Advances the cursor.
CZMQ_EXPORT void *
zlist_next(zlist_t *self);

//  Return the item at the tail of list. If the list is empty, returns NULL.
//  Leaves cursor pointing at the tail item, or NULL if the list is empty.
CZMQ_EXPORT void *
zlist_last(zlist_t *self);

//  Return first item in the list, or null, leaves the cursor
CZMQ_EXPORT void *
zlist_head(zlist_t *self);

//  Return last item in the list, or null, leaves the cursor
CZMQ_EXPORT void *
zlist_tail(zlist_t *self);

//  Return the current item of list. If the list is empty, returns NULL.
//  Leaves cursor pointing at the current item, or NULL if the list is empty.
CZMQ_EXPORT void *
zlist_item(zlist_t *self);

//  Append an item to the end of the list, return 0 if OK or -1 if this
//  failed for some reason (out of memory). Note that if a duplicator has
//  been set, this method will also duplicate the item.
CZMQ_EXPORT int
zlist_append(zlist_t *self, void *item);

//  Push an item to the start of the list, return 0 if OK or -1 if this
//  failed for some reason (out of memory). Note that if a duplicator has
//  been set, this method will also duplicate the item.
CZMQ_EXPORT int
zlist_push(zlist_t *self, void *item);

//  Pop the item off the start of the list, if any
CZMQ_EXPORT void *
zlist_pop(zlist_t *self);

//  Checks if an item already is present. Uses compare method to determine if
//  items are equal. If the compare method is NULL the check will only compare
//  pointers. Returns true if item is present else false.
CZMQ_EXPORT bool
zlist_exists(zlist_t *self, void *item);

//  Remove the specified item from the list if present
CZMQ_EXPORT void
zlist_remove(zlist_t *self, void *item);

//  Make a copy of list. If the list has autofree set, the copied list will
//  duplicate all items, which must be strings. Otherwise, the list will hold
//  pointers back to the items in the original list. If list is null, returns
//  NULL.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zlist_t *
zlist_dup(zlist_t *self);

//  Purge all items from list
CZMQ_EXPORT void
zlist_purge(zlist_t *self);

//  Return number of items in the list
CZMQ_EXPORT size_t
zlist_size(zlist_t *self);

//  Sort the list by ascending key value using a straight ASCII comparison.
//  The sort is not stable, so may reorder items with the same keys.
CZMQ_EXPORT void
zlist_sort(zlist_t *self, zlist_compare_fn compare);

//  Set list for automatic item destruction; item values MUST be strings.
//  By default a list item refers to a value held elsewhere. When you set
//  this, each time you append or push a list item, zlist will take a copy
//  of the string value. Then, when you destroy the list, it will free all
//  item values automatically. If you use any other technique to allocate
//  list values, you must free them explicitly before destroying the list.
//  The usual technique is to pop list items and destroy them, until the
//  list is empty.
CZMQ_EXPORT void
zlist_autofree(zlist_t *self);

//  Sets a compare function for this list. The function compares two items.
//  It returns an integer less than, equal to, or greater than zero if the
//  first item is found, respectively, to be less than, to match, or be
//  greater than the second item.
//  This function is used for sorting, removal and exists checking.
CZMQ_EXPORT void
zlist_comparefn(zlist_t *self, zlist_compare_fn fn);

//  Set a free function for the specified list item. When the item is
//  destroyed, the free function, if any, is called on that item.
//  Use this when list items are dynamically allocated, to ensure that
//  you don't have memory leaks. You can pass 'free' or NULL as a free_fn.
//  Returns the item, or NULL if there is no such item.
CZMQ_EXPORT void *
zlist_freefn(zlist_t *self, void *item, zlist_free_fn fn, bool at_tail);

//  Self test of this class
CZMQ_EXPORT void
zlist_test(int verbose);</code></pre>
<h2>Description</h2>
<p>Provides a generic container implementing a fast singly-linked list. You can use this to construct multi-dimensional lists, and other structures together with other generic containers like zhash. This is a simple class. For demanding applications we recommend using zlistx. </p>
<p> To iterate through a list, use zlist_first to get the first item, then loop while not null, and do zlist_next at the end of each iteration.</p>
<h2>Example</h2>
<p><code>From zlist_test method</code>. </p>
<pre><code>zlist_t *list = zlist_new();
assert(list);
assert(zlist_size(list) == 0);

//  Three items we'll use as test data
//  List items are void *, not particularly strings
char *cheese = &quot;boursin&quot;;
char *bread = &quot;baguette&quot;;
char *wine = &quot;bordeaux&quot;;

zlist_append(list, cheese);
assert(zlist_size(list) == 1);
assert(zlist_exists(list, cheese));
assert(!zlist_exists(list, bread));
assert(!zlist_exists(list, wine));
zlist_append(list, bread);
assert(zlist_size(list) == 2);
assert(zlist_exists(list, cheese));
assert(zlist_exists(list, bread));
assert(!zlist_exists(list, wine));
zlist_append(list, wine);
assert(zlist_size(list) == 3);
assert(zlist_exists(list, cheese));
assert(zlist_exists(list, bread));
assert(zlist_exists(list, wine));

assert(zlist_head(list) == cheese);
assert(zlist_next(list) == cheese);

assert(zlist_first(list) == cheese);
assert(zlist_tail(list) == wine);
assert(zlist_next(list) == bread);

assert(zlist_first(list) == cheese);
assert(zlist_next(list) == bread);
assert(zlist_next(list) == wine);
assert(zlist_next(list) == NULL);
//  After we reach end of list, next wraps around
assert(zlist_next(list) == cheese);
assert(zlist_size(list) == 3);

zlist_remove(list, wine);
assert(zlist_size(list) == 2);

assert(zlist_first(list) == cheese);
zlist_remove(list, cheese);
assert(zlist_size(list) == 1);
assert(zlist_first(list) == bread);

zlist_remove(list, bread);
assert(zlist_size(list) == 0);

zlist_append(list, cheese);
zlist_append(list, bread);
assert(zlist_last(list) == bread);
zlist_remove(list, bread);
assert(zlist_last(list) == cheese);
zlist_remove(list, cheese);
assert(zlist_last(list) == NULL);

zlist_push(list, cheese);
assert(zlist_size(list) == 1);
assert(zlist_first(list) == cheese);

zlist_push(list, bread);
assert(zlist_size(list) == 2);
assert(zlist_first(list) == bread);
assert(zlist_item(list) == bread);

zlist_append(list, wine);
assert(zlist_size(list) == 3);
assert(zlist_first(list) == bread);

zlist_t *sub_list = zlist_dup(list);
assert(sub_list);
assert(zlist_size(sub_list) == 3);

zlist_sort(list, s_compare);
char *item;
item = (char *)zlist_pop(list);
assert(item == bread);
item = (char *)zlist_pop(list);
assert(item == wine);
item = (char *)zlist_pop(list);
assert(item == cheese);
assert(zlist_size(list) == 0);

assert(zlist_size(sub_list) == 3);
zlist_push(list, sub_list);
zlist_t *sub_list_2 = zlist_dup(sub_list);
zlist_append(list, sub_list_2);
assert(zlist_freefn(list, sub_list, &amp;s_zlist_free, false) == sub_list);
assert(zlist_freefn(list, sub_list_2, &amp;s_zlist_free, true) == sub_list_2);
zlist_destroy(&amp;list);

//  Test autofree functionality
list = zlist_new();
assert(list);
zlist_autofree(list);
//  Set equals function otherwise equals will not work as autofree copies strings
zlist_comparefn(list, s_compare);
zlist_push(list, bread);
zlist_append(list, cheese);
assert(zlist_size(list) == 2);
zlist_append(list, wine);
assert(zlist_exists(list, wine));
zlist_remove(list, wine);
assert(!zlist_exists(list, wine));
assert(streq((const char *)zlist_first(list), bread));
item = (char *)zlist_pop(list);
assert(streq(item, bread));
free(item);
item = (char *)zlist_pop(list);
assert(streq(item, cheese));
free(item);

zlist_destroy(&amp;list);
assert(list == NULL);
</code></pre>
<h2>Authors</h2>
<p>The czmq manual was written by the authors in the AUTHORS file.</p>
<h2>Resources</h2>
<p>Main web site: m[blue]m[] </p>
<p> Report bugs to the email &lt;m[blue]<code>zeromq-dev [at] lists.zeromq.org</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>Copyright</h2>
<p>Copyright (c) 1991-2012 iMatix Corporation &#8212; <a rel="nofollow" href="http://www.imatix.com">http://www.imatix.com</a> Copyright other contributors as noted in the AUTHORS file. This file is part of CZMQ, the high-level C binding for 0MQ: <a href="http://czmq.zeromq.org">http://czmq.zeromq.org</a> This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a> LICENSE included with the czmq distribution.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>zeromq-dev [at] lists.zeromq.org</p>
<dl>
<dd>mailto:zeromq-dev [at] lists.zeromq.org</dl>
