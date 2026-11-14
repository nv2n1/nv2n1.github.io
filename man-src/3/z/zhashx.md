---
title: "zhashx(3)"
name: "zhashx"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhashx/"
description: "zhashx – extended generic hash container"
---

<p>zhashx &#8211; extended generic hash container</p>
<h2>Synopsis</h2>
<pre><code>// Destroy an item
typedef void(zhashx_destructor_fn)(
    void **item);

// Duplicate an item
typedef void *(zhashx_duplicator_fn)(const void *item);

// Compare two items, for sorting
typedef int(zhashx_comparator_fn)(
    const void *item1, const void *item2);

// compare two items, for sorting
typedef void(zhashx_free_fn)(
    void *data);

// compare two items, for sorting
typedef size_t(zhashx_hash_fn)(
    const void *key);

// DEPRECATED as clumsy -- use zhashx_first/_next instead
typedef int(zhashx_foreach_fn)(
    const char *key, void *item, void *argument);

//  Create a new, empty hash container
CZMQ_EXPORT zhashx_t *
zhashx_new();

//  Destroy a hash container and all items in it
CZMQ_EXPORT void
zhashx_destroy(zhashx_t **self_p);

//  Insert item into hash table with specified key and item.
//  If key is already present returns -1 and leaves existing item unchanged
//  Returns 0 on success.
CZMQ_EXPORT int
zhashx_insert(zhashx_t *self, const void *key, void *item);

//  Update or insert item into hash table with specified key and item. If the
//  key is already present, destroys old item and inserts new one. If you set
//  a container item destructor, this is called on the old value. If the key
//  was not already present, inserts a new item. Sets the hash cursor to the
//  new item.
CZMQ_EXPORT void
zhashx_update(zhashx_t *self, const void *key, void *item);

//  Remove an item specified by key from the hash table. If there was no such
//  item, this function does nothing.
CZMQ_EXPORT void
zhashx_delete(zhashx_t *self, const void *key);

//  Delete all items from the hash table. If the key destructor is
//  set, calls it on every key. If the item destructor is set, calls
//  it on every item.
CZMQ_EXPORT void
zhashx_purge(zhashx_t *self);

//  Return the item at the specified key, or null
CZMQ_EXPORT void *
zhashx_lookup(zhashx_t *self, const void *key);

//  Reindexes an item from an old key to a new key. If there was no such
//  item, does nothing. Returns 0 if successful, else -1.
CZMQ_EXPORT int
zhashx_rename(zhashx_t *self, const void *old_key, const void *new_key);

//  Set a free function for the specified hash table item. When the item is
//  destroyed, the free function, if any, is called on that item.
//  Use this when hash items are dynamically allocated, to ensure that
//  you don't have memory leaks. You can pass 'free' or NULL as a free_fn.
//  Returns the item, or NULL if there is no such item.
CZMQ_EXPORT void *
zhashx_freefn(zhashx_t *self, const void *key, zhashx_free_fn free_fn);

//  Return the number of keys/items in the hash table
CZMQ_EXPORT size_t
zhashx_size(zhashx_t *self);

//  Return a zlistx_t containing the keys for the items in the
//  table. Uses the key_duplicator to duplicate all keys and sets the
//  key_destructor as destructor for the list.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zlistx_t *
zhashx_keys(zhashx_t *self);

//  Return a zlistx_t containing the values for the items in the
//  table. Uses the duplicator to duplicate all items and sets the
//  destructor as destructor for the list.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zlistx_t *
zhashx_values(zhashx_t *self);

//  Simple iterator; returns first item in hash table, in no given order,
//  or NULL if the table is empty. This method is simpler to use than the
//  foreach() method, which is deprecated. To access the key for this item
//  use zhashx_cursor(). NOTE: do NOT modify the table while iterating.
CZMQ_EXPORT void *
zhashx_first(zhashx_t *self);

//  Simple iterator; returns next item in hash table, in no given order,
//  or NULL if the last item was already returned. Use this together with
//  zhashx_first() to process all items in a hash table. If you need the
//  items in sorted order, use zhashx_keys() and then zlistx_sort(). To
//  access the key for this item use zhashx_cursor(). NOTE: do NOT modify
//  the table while iterating.
CZMQ_EXPORT void *
zhashx_next(zhashx_t *self);

//  After a successful first/next method, returns the key for the item that
//  was returned. This is a constant string that you may not modify or
//  deallocate, and which lasts as long as the item in the hash. After an
//  unsuccessful first/next, returns NULL.
CZMQ_EXPORT const void *
zhashx_cursor(zhashx_t *self);

//  Add a comment to hash table before saving to disk. You can add as many
//  comment lines as you like. These comment lines are discarded when loading
//  the file. If you use a null format, all comments are deleted.
CZMQ_EXPORT void
zhashx_comment(zhashx_t *self, const char *format, ...) CHECK_PRINTF(2);

//  Save hash table to a text file in name=value format. Hash values must be
//  printable strings; keys may not contain '=' character. Returns 0 if OK,
//  else -1 if a file error occurred.
CZMQ_EXPORT int
zhashx_save(zhashx_t *self, const char *filename);

//  Load hash table from a text file in name=value format; hash table must
//  already exist. Hash values must printable strings; keys may not contain
//  '=' character. Returns 0 if OK, else -1 if a file was not readable.
CZMQ_EXPORT int
zhashx_load(zhashx_t *self, const char *filename);

//  When a hash table was loaded from a file by zhashx_load, this method will
//  reload the file if it has been modified since, and is &quot;stable&quot;, i.e. not
//  still changing. Returns 0 if OK, -1 if there was an error reloading the
//  file.
CZMQ_EXPORT int
zhashx_refresh(zhashx_t *self);

//  Serialize hash table to a binary frame that can be sent in a message.
//  The packed format is compatible with the 'dictionary' type defined in
//  http://rfc.zeromq.org/spec:35/FILEMQ, and implemented by zproto:
//
//     ; A list of name/value pairs
//     dictionary      = dict-count *( dict-name dict-value )
//     dict-count      = number-4
//     dict-value      = longstr
//     dict-name       = string
//
//     ; Strings are always length + text contents
//     longstr         = number-4 *VCHAR
//     string          = number-1 *VCHAR
//
//     ; Numbers are unsigned integers in network byte order
//     number-1        = 1OCTET
//     number-4        = 4OCTET
//
//  Comments are not included in the packed data. Item values MUST be
//  strings.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zframe_t *
zhashx_pack(zhashx_t *self);

//  Unpack binary frame into a new hash table. Packed data must follow format
//  defined by zhashx_pack. Hash table is set to autofree. An empty frame
//  unpacks to an empty hash table.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zhashx_t *
zhashx_unpack(zframe_t *frame);

//  Make a copy of the list; items are duplicated if you set a duplicator
//  for the list, otherwise not. Copying a null reference returns a null
//  reference. Note that this method's behavior changed slightly for CZMQ
//  v3.x, as it does not set nor respect autofree. It does however let you
//  duplicate any hash table safely. The old behavior is in zhashx_dup_v2.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zhashx_t *
zhashx_dup(zhashx_t *self);

//  Set a user-defined deallocator for hash items; by default items are not
//  freed when the hash is destroyed.
CZMQ_EXPORT void
zhashx_set_destructor(zhashx_t *self, zhashx_destructor_fn destructor);

//  Set a user-defined duplicator for hash items; by default items are not
//  copied when the hash is duplicated.
CZMQ_EXPORT void
zhashx_set_duplicator(zhashx_t *self, zhashx_duplicator_fn duplicator);

//  Set a user-defined deallocator for keys; by default keys are freed
//  when the hash is destroyed using free().
CZMQ_EXPORT void
zhashx_set_key_destructor(zhashx_t *self, zhashx_destructor_fn destructor);

//  Set a user-defined duplicator for keys; by default keys are duplicated
//  using strdup.
CZMQ_EXPORT void
zhashx_set_key_duplicator(zhashx_t *self, zhashx_duplicator_fn duplicator);

//  Set a user-defined comparator for keys; by default keys are
//  compared using strcmp.
CZMQ_EXPORT void
zhashx_set_key_comparator(zhashx_t *self, zhashx_comparator_fn comparator);

//  Set a user-defined comparator for keys; by default keys are
//  compared using strcmp.
CZMQ_EXPORT void
zhashx_set_key_hasher(zhashx_t *self, zhashx_hash_fn hasher);

//  Make copy of hash table; if supplied table is null, returns null.
//  Does not copy items themselves. Rebuilds new table so may be slow on
//  very large tables. NOTE: only works with item values that are strings
//  since there's no other way to know how to duplicate the item value.
CZMQ_EXPORT zhashx_t *
zhashx_dup_v2(zhashx_t *self);

//  DEPRECATED as clumsy -- use set_destructor instead
//  Set hash for automatic value destruction
CZMQ_EXPORT void
zhashx_autofree(zhashx_t *self);

//  DEPRECATED as clumsy -- use zhashx_first/_next instead
//  Apply function to each item in the hash table. Items are iterated in no
//  defined order. Stops if callback function returns non-zero and returns
//  final return code from callback function (zero = success).
//  Callback function for zhashx_foreach method
CZMQ_EXPORT int
zhashx_foreach(zhashx_t *self, zhashx_foreach_fn callback, void *argument);

//  Self test of this class
CZMQ_EXPORT void
zhashx_test(int verbose);</code></pre>
<h2>Description</h2>
<p>zhashx is an extended hash table container with more functionality than zhash, its simpler cousin. </p>
<p> The hash table always has a size that is prime and roughly doubles its size when 75% full. In case of hash collisions items are chained in a linked list. The hash table size is increased slightly (up to 5 times before roughly doubling the size) when an overly long chain (between 1 and 63 items depending on table size) is detected.</p>
<h2>Example</h2>
<p><code>From zhashx_test method</code>. </p>
<pre><code>zhashx_t *hash = zhashx_new();
assert(hash);
assert(zhashx_size(hash) == 0);
assert(zhashx_first(hash) == NULL);
assert(zhashx_cursor(hash) == NULL);

//  Insert some items
int rc;
rc = zhashx_insert(hash, &quot;DEADBEEF&quot;, &quot;dead beef&quot;);
char *item = (char *)zhashx_first(hash);
assert(streq((char *)zhashx_cursor(hash), &quot;DEADBEEF&quot;));
assert(streq(item, &quot;dead beef&quot;));
assert(rc == 0);
rc = zhashx_insert(hash, &quot;ABADCAFE&quot;, &quot;a bad cafe&quot;);
assert(rc == 0);
rc = zhashx_insert(hash, &quot;C0DEDBAD&quot;, &quot;coded bad&quot;);
assert(rc == 0);
rc = zhashx_insert(hash, &quot;DEADF00D&quot;, &quot;dead food&quot;);
assert(rc == 0);
assert(zhashx_size(hash) == 4);

//  Look for existing items
item = (char *)zhashx_lookup(hash, &quot;DEADBEEF&quot;);
assert(streq(item, &quot;dead beef&quot;));
item = (char *)zhashx_lookup(hash, &quot;ABADCAFE&quot;);
assert(streq(item, &quot;a bad cafe&quot;));
item = (char *)zhashx_lookup(hash, &quot;C0DEDBAD&quot;);
assert(streq(item, &quot;coded bad&quot;));
item = (char *)zhashx_lookup(hash, &quot;DEADF00D&quot;);
assert(streq(item, &quot;dead food&quot;));

//  Look for non-existent items
item = (char *)zhashx_lookup(hash, &quot;foo&quot;);
assert(item == NULL);

//  Try to insert duplicate items
rc = zhashx_insert(hash, &quot;DEADBEEF&quot;, &quot;foo&quot;);
assert(rc == -1);
item = (char *)zhashx_lookup(hash, &quot;DEADBEEF&quot;);
assert(streq(item, &quot;dead beef&quot;));

//  Some rename tests

//  Valid rename, key is now LIVEBEEF
rc = zhashx_rename(hash, &quot;DEADBEEF&quot;, &quot;LIVEBEEF&quot;);
assert(rc == 0);
item = (char *)zhashx_lookup(hash, &quot;LIVEBEEF&quot;);
assert(streq(item, &quot;dead beef&quot;));

//  Trying to rename an unknown item to a non-existent key
rc = zhashx_rename(hash, &quot;WHATBEEF&quot;, &quot;NONESUCH&quot;);
assert(rc == -1);

//  Trying to rename an unknown item to an existing key
rc = zhashx_rename(hash, &quot;WHATBEEF&quot;, &quot;LIVEBEEF&quot;);
assert(rc == -1);
item = (char *)zhashx_lookup(hash, &quot;LIVEBEEF&quot;);
assert(streq(item, &quot;dead beef&quot;));

//  Trying to rename an existing item to another existing item
rc = zhashx_rename(hash, &quot;LIVEBEEF&quot;, &quot;ABADCAFE&quot;);
assert(rc == -1);
item = (char *)zhashx_lookup(hash, &quot;LIVEBEEF&quot;);
assert(streq(item, &quot;dead beef&quot;));
item = (char *)zhashx_lookup(hash, &quot;ABADCAFE&quot;);
assert(streq(item, &quot;a bad cafe&quot;));

//  Test keys method
zlistx_t *keys = zhashx_keys(hash);
assert(zlistx_size(keys) == 4);
zlistx_destroy(&amp;keys);

zlistx_t *values = zhashx_values(hash);
assert(zlistx_size(values) == 4);
zlistx_destroy(&amp;values);

//  Test dup method
zhashx_t *copy = zhashx_dup(hash);
assert(zhashx_size(copy) == 4);
item = (char *)zhashx_lookup(copy, &quot;LIVEBEEF&quot;);
assert(item);
assert(streq(item, &quot;dead beef&quot;));
zhashx_destroy(&amp;copy);

//  Test pack/unpack methods
zframe_t *frame = zhashx_pack(hash);
copy = zhashx_unpack(frame);
zframe_destroy(&amp;frame);
assert(zhashx_size(copy) == 4);
item = (char *)zhashx_lookup(copy, &quot;LIVEBEEF&quot;);
assert(item);
assert(streq(item, &quot;dead beef&quot;));
zhashx_destroy(&amp;copy);

//  Test save and load
zhashx_comment(hash, &quot;This is a test file&quot;);
zhashx_comment(hash, &quot;Created by %s&quot;, &quot;czmq_selftest&quot;);
zhashx_save(hash, &quot;.cache&quot;);
copy = zhashx_new();
assert(copy);
zhashx_load(copy, &quot;.cache&quot;);
item = (char *)zhashx_lookup(copy, &quot;LIVEBEEF&quot;);
assert(item);
assert(streq(item, &quot;dead beef&quot;));
zhashx_destroy(&amp;copy);
zsys_file_delete(&quot;.cache&quot;);

//  Delete a item
zhashx_delete(hash, &quot;LIVEBEEF&quot;);
item = (char *)zhashx_lookup(hash, &quot;LIVEBEEF&quot;);
assert(item == NULL);
assert(zhashx_size(hash) == 3);

//  Check that the queue is robust against random usage
struct {
    char name[100];
    bool exists;
} testset[200];
memset(testset, 0, sizeof(testset));
int testmax = 200, testnbr, iteration;

srandom((unsigned)time(NULL));
for (iteration = 0; iteration &lt; 25000; iteration++) {
    testnbr = randof(testmax);
    if (testset[testnbr].exists) {
        item = (char *)zhashx_lookup(hash, testset[testnbr].name);
        assert(item);
        zhashx_delete(hash, testset[testnbr].name);
        testset[testnbr].exists = false;
    } else {
        sprintf(testset[testnbr].name, &quot;%x-%x&quot;, rand(), rand());
        if (zhashx_insert(hash, testset[testnbr].name, &quot;&quot;) == 0)
            testset[testnbr].exists = true;
    }
}
//  Test 10K lookups
for (iteration = 0; iteration &lt; 10000; iteration++)
    item = (char *)zhashx_lookup(hash, &quot;DEADBEEFABADCAFE&quot;);

//  Destructor should be safe to call twice
zhashx_destroy(&amp;hash);
zhashx_destroy(&amp;hash);
assert(hash == NULL);

//  Test autofree; automatically copies and frees string values
hash = zhashx_new();
assert(hash);
zhashx_autofree(hash);
char value[255];
strcpy(value, &quot;This is a string&quot;);
rc = zhashx_insert(hash, &quot;key1&quot;, value);
assert(rc == 0);
strcpy(value, &quot;Ring a ding ding&quot;);
rc = zhashx_insert(hash, &quot;key2&quot;, value);
assert(rc == 0);
assert(streq((char *)zhashx_lookup(hash, &quot;key1&quot;), &quot;This is a string&quot;));
assert(streq((char *)zhashx_lookup(hash, &quot;key2&quot;), &quot;Ring a ding ding&quot;));
zhashx_destroy(&amp;hash);
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
