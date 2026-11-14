---
title: "zlistx(3)"
name: "zlistx"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlistx/"
description: "zlistx – extended generic list container"
---

<p>zlistx &#8211; extended generic list container</p>
<h2>Synopsis</h2>
<pre><code>//  Create a new, empty list.
CZMQ_EXPORT zlistx_t *
zlistx_new(void);

//  Destroy a list. If an item destructor was specified, all items in the
//  list are automatically destroyed as well.
CZMQ_EXPORT void
zlistx_destroy(zlistx_t **self_p);

//  Add an item to the head of the list. Calls the item duplicator, if any,
//  on the item. Resets cursor to list head. Returns an item handle on
//  success, NULL if memory was exhausted.
CZMQ_EXPORT void *
zlistx_add_start(zlistx_t *self, void *item);

//  Add an item to the tail of the list. Calls the item duplicator, if any,
//  on the item. Resets cursor to list head. Returns an item handle on
//  success, NULL if memory was exhausted.
CZMQ_EXPORT void *
zlistx_add_end(zlistx_t *self, void *item);

//  Return the number of items in the list
CZMQ_EXPORT size_t
zlistx_size(zlistx_t *self);

//  Return the item at the head of list. If the list is empty, returns NULL.
//  Leaves cursor pointing at the head item, or NULL if the list is empty.
CZMQ_EXPORT void *
zlistx_first(zlistx_t *self);

//  Return the next item. At the end of the list (or in an empty list),
//  returns NULL. Use repeated zlistx_next () calls to work through the list
//  from zlistx_first (). First time, acts as zlistx_first().
CZMQ_EXPORT void *
zlistx_next(zlistx_t *self);

//  Return the previous item. At the start of the list (or in an empty list),
//  returns NULL. Use repeated zlistx_prev () calls to work through the list
//  backwards from zlistx_last (). First time, acts as zlistx_last().
CZMQ_EXPORT void *
zlistx_prev(zlistx_t *self);

//  Return the item at the tail of list. If the list is empty, returns NULL.
//  Leaves cursor pointing at the tail item, or NULL if the list is empty.
CZMQ_EXPORT void *
zlistx_last(zlistx_t *self);

//  Returns the value of the item at the cursor, or NULL if the cursor is
//  not pointing to an item.
CZMQ_EXPORT void *
zlistx_item(zlistx_t *self);

//  Returns the handle of the item at the cursor, or NULL if the cursor is
//  not pointing to an item.
CZMQ_EXPORT void *
zlistx_cursor(zlistx_t *self);

//  Returns the item associated with the given list handle, or NULL if passed
//  in handle is NULL. Asserts that the passed in handle points to a list element.
CZMQ_EXPORT void *
zlistx_handle_item(void *handle);

//  Find an item in the list, searching from the start. Uses the item
//  comparator, if any, else compares item values directly. Returns the
//  item handle found, or NULL. Sets the cursor to the found item, if any.
CZMQ_EXPORT void *
zlistx_find(zlistx_t *self, void *item);

//  Detach an item from the list, using its handle. The item is not modified,
//  and the caller is responsible for destroying it if necessary. If handle is
//  null, detaches the first item on the list. Returns item that was detached,
//  or null if none was. If cursor was at item, moves cursor to previous item,
//  so you can detach items while iterating forwards through a list.
CZMQ_EXPORT void *
zlistx_detach(zlistx_t *self, void *handle);

//  Detach item at the cursor, if any, from the list. The item is not modified,
//  and the caller is responsible for destroying it as necessary. Returns item
//  that was detached, or null if none was. Moves cursor to previous item, so
//  you can detach items while iterating forwards through a list.
CZMQ_EXPORT void *
zlistx_detach_cur(zlistx_t *self);

//  Delete an item, using its handle. Calls the item destructor is any is
//  set. If handle is null, deletes the first item on the list. Returns 0
//  if an item was deleted, -1 if not. If cursor was at item, moves cursor
//  to previous item, so you can delete items while iterating forwards
//  through a list.
CZMQ_EXPORT int
zlistx_delete(zlistx_t *self, void *handle);

//  Move an item to the start of the list, via its handle.
CZMQ_EXPORT void
zlistx_move_start(zlistx_t *self, void *handle);

//  Move an item to the end of the list, via its handle.
CZMQ_EXPORT void
zlistx_move_end(zlistx_t *self, void *handle);

//  Remove all items from the list, and destroy them if the item destructor
//  is set.
CZMQ_EXPORT void
zlistx_purge(zlistx_t *self);

//  Sort the list. If an item comparator was set, calls that to compare
//  items, otherwise compares on item value. The sort is not stable, so may
//  reorder equal items.
CZMQ_EXPORT void
zlistx_sort(zlistx_t *self);

//  Create a new node and insert it into a sorted list. Calls the item
//  duplicator, if any, on the item. If low_value is true, starts searching
//  from the start of the list, otherwise searches from the end. Use the item
//  comparator, if any, to find where to place the new node. Returns a handle
//  to the new node, or NULL if memory was exhausted. Resets the cursor to the
//  list head.
CZMQ_EXPORT void *
zlistx_insert(zlistx_t *self, void *item, bool low_value);

//  Move an item, specified by handle, into position in a sorted list. Uses
//  the item comparator, if any, to determine the new location. If low_value
//  is true, starts searching from the start of the list, otherwise searches
//  from the end.
CZMQ_EXPORT void
zlistx_reorder(zlistx_t *self, void *handle, bool low_value);

//  Make a copy of the list; items are duplicated if you set a duplicator
//  for the list, otherwise not. Copying a null reference returns a null
//  reference.
CZMQ_EXPORT zlistx_t *
zlistx_dup(zlistx_t *self);

//  Set a user-defined deallocator for list items; by default items are not
//  freed when the list is destroyed.
CZMQ_EXPORT void
zlistx_set_destructor(zlistx_t *self, czmq_destructor destructor);

//  Set a user-defined duplicator for list items; by default items are not
//  copied when the list is duplicated.
CZMQ_EXPORT void
zlistx_set_duplicator(zlistx_t *self, czmq_duplicator duplicator);

//  Set a user-defined comparator for zlistx_find and zlistx_sort; the method
//  must return -1, 0, or 1 depending on whether item1 is less than, equal to,
//  or greater than, item2.
CZMQ_EXPORT void
zlistx_set_comparator(zlistx_t *self, czmq_comparator comparator);

//  Runs selftest of class
CZMQ_EXPORT void
zlistx_test(int verbose);</code></pre>
<h2>Description</h2>
<p>Provides a generic doubly-linked list container. This container provides hooks for duplicator, comparator, and destructor functions. These tie into CZMQ and standard C semantics, so e.g. for string items you can use strdup, strcmp, and zstr_free. To store custom objects, define your own duplicator and comparator, and use the standard object destructor. </p>
<p> This is a reworking of the simpler zlist container. It is faster to insert and delete items anywhere in the list, and to keep ordered lists.</p>
<h2>Example</h2>
<p><code>From zlistx_test method</code>. </p>
<pre><code>zlistx_t *list = zlistx_new();
assert(list);
assert(zlistx_size(list) == 0);

//  Test operations on an empty list
assert(zlistx_first(list) == NULL);
assert(zlistx_last(list) == NULL);
assert(zlistx_next(list) == NULL);
assert(zlistx_prev(list) == NULL);
assert(zlistx_find(list, &quot;hello&quot;) == NULL);
assert(zlistx_delete(list, NULL) == -1);
assert(zlistx_detach(list, NULL) == NULL);
assert(zlistx_delete(list, NULL) == -1);
assert(zlistx_detach(list, NULL) == NULL);
zlistx_purge(list);
zlistx_sort(list);

//  Use item handlers
zlistx_set_destructor(list, (czmq_destructor *)zstr_free);
zlistx_set_duplicator(list, (czmq_duplicator *)strdup);
zlistx_set_comparator(list, (czmq_comparator *)strcmp);

//  Try simple insert/sort/delete/next
assert(zlistx_next(list) == NULL);
zlistx_add_end(list, &quot;world&quot;);
assert(streq((char *)zlistx_next(list), &quot;world&quot;));
zlistx_add_end(list, &quot;hello&quot;);
assert(streq((char *)zlistx_prev(list), &quot;hello&quot;));
zlistx_sort(list);
assert(zlistx_size(list) == 2);
void *handle = zlistx_find(list, &quot;hello&quot;);
char *item1 = (char *)zlistx_item(list);
char *item2 = (char *)zlistx_handle_item(handle);
assert(item1 == item2);
assert(streq(item1, &quot;hello&quot;));
zlistx_delete(list, handle);
assert(zlistx_size(list) == 1);
char *string = (char *)zlistx_detach(list, NULL);
assert(streq(string, &quot;world&quot;));
free(string);
assert(zlistx_size(list) == 0);

//  Check next/back work
//  Now populate the list with items
zlistx_add_start(list, &quot;five&quot;);
zlistx_add_end(list, &quot;six&quot;);
zlistx_add_start(list, &quot;four&quot;);
zlistx_add_end(list, &quot;seven&quot;);
zlistx_add_start(list, &quot;three&quot;);
zlistx_add_end(list, &quot;eight&quot;);
zlistx_add_start(list, &quot;two&quot;);
zlistx_add_end(list, &quot;nine&quot;);
zlistx_add_start(list, &quot;one&quot;);
zlistx_add_end(list, &quot;ten&quot;);

//  Test our navigation skills
assert(zlistx_size(list) == 10);
assert(streq((char *)zlistx_last(list), &quot;ten&quot;));
assert(streq((char *)zlistx_prev(list), &quot;nine&quot;));
assert(streq((char *)zlistx_prev(list), &quot;eight&quot;));
assert(streq((char *)zlistx_prev(list), &quot;seven&quot;));
assert(streq((char *)zlistx_prev(list), &quot;six&quot;));
assert(streq((char *)zlistx_prev(list), &quot;five&quot;));
assert(streq((char *)zlistx_first(list), &quot;one&quot;));
assert(streq((char *)zlistx_next(list), &quot;two&quot;));
assert(streq((char *)zlistx_next(list), &quot;three&quot;));
assert(streq((char *)zlistx_next(list), &quot;four&quot;));

//  Sort by alphabetical order
zlistx_sort(list);
assert(streq((char *)zlistx_first(list), &quot;eight&quot;));
assert(streq((char *)zlistx_last(list), &quot;two&quot;));

//  Moving items around
handle = zlistx_find(list, &quot;six&quot;);
zlistx_move_start(list, handle);
assert(streq((char *)zlistx_first(list), &quot;six&quot;));
zlistx_move_end(list, handle);
assert(streq((char *)zlistx_last(list), &quot;six&quot;));
zlistx_sort(list);
assert(streq((char *)zlistx_last(list), &quot;two&quot;));

//  Copying a list
zlistx_t *copy = zlistx_dup(list);
assert(copy);
assert(zlistx_size(copy) == 10);
assert(streq((char *)zlistx_first(copy), &quot;eight&quot;));
assert(streq((char *)zlistx_last(copy), &quot;two&quot;));
zlistx_destroy(&amp;copy);

//  Delete items while iterating
string = (char *)zlistx_first(list);
assert(streq(string, &quot;eight&quot;));
string = (char *)zlistx_next(list);
assert(streq(string, &quot;five&quot;));
zlistx_delete(list, zlistx_cursor(list));
string = (char *)zlistx_next(list);
assert(streq(string, &quot;four&quot;));

zlistx_purge(list);
zlistx_destroy(&amp;list);
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
