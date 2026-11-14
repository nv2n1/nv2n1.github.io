---
title: "zhash(3)"
name: "zhash"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhash/"
description: "zhash – simple generic hash container"
---

<p>zhash &#8211; simple generic hash container</p>
<h2>Synopsis</h2>
<pre><code>// Callback function for zhash_freefn method
typedef void(zhash_free_fn)(
    void *data);

// DEPRECATED as clumsy -- use zhash_first/_next instead
typedef int(zhash_foreach_fn)(
    const char *key, void *item, void *argument);

//  Create a new, empty hash container
CZMQ_EXPORT zhash_t *
zhash_new();

//  Destroy a hash container and all items in it
CZMQ_EXPORT void
zhash_destroy(zhash_t **self_p);

//  Insert item into hash table with specified key and item.
//  If key is already present returns -1 and leaves existing item unchanged
//  Returns 0 on success.
CZMQ_EXPORT int
zhash_insert(zhash_t *self, const char *key, void *item);

//  Update item into hash table with specified key and item.
//  If key is already present, destroys old item and inserts new one.
//  Use free_fn method to ensure deallocator is properly called on item.
CZMQ_EXPORT void
zhash_update(zhash_t *self, const char *key, void *item);

//  Remove an item specified by key from the hash table. If there was no such
//  item, this function does nothing.
CZMQ_EXPORT void
zhash_delete(zhash_t *self, const char *key);

//  Return the item at the specified key, or null
CZMQ_EXPORT void *
zhash_lookup(zhash_t *self, const char *key);

//  Reindexes an item from an old key to a new key. If there was no such
//  item, does nothing. Returns 0 if successful, else -1.
CZMQ_EXPORT int
zhash_rename(zhash_t *self, const char *old_key, const char *new_key);

//  Set a free function for the specified hash table item. When the item is
//  destroyed, the free function, if any, is called on that item.
//  Use this when hash items are dynamically allocated, to ensure that
//  you don't have memory leaks. You can pass 'free' or NULL as a free_fn.
//  Returns the item, or NULL if there is no such item.
CZMQ_EXPORT void *
zhash_freefn(zhash_t *self, const char *key, zhash_free_fn free_fn);

//  Return the number of keys/items in the hash table
CZMQ_EXPORT size_t
zhash_size(zhash_t *self);

//  Make copy of hash table; if supplied table is null, returns null.
//  Does not copy items themselves. Rebuilds new table so may be slow on
//  very large tables. NOTE: only works with item values that are strings
//  since there's no other way to know how to duplicate the item value.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zhash_t *
zhash_dup(zhash_t *self);

//  Return keys for items in table
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zlist_t *
zhash_keys(zhash_t *self);

//  Simple iterator; returns first item in hash table, in no given order,
//  or NULL if the table is empty. This method is simpler to use than the
//  foreach() method, which is deprecated. To access the key for this item
//  use zhash_cursor(). NOTE: do NOT modify the table while iterating.
CZMQ_EXPORT void *
zhash_first(zhash_t *self);

//  Simple iterator; returns next item in hash table, in no given order,
//  or NULL if the last item was already returned. Use this together with
//  zhash_first() to process all items in a hash table. If you need the
//  items in sorted order, use zhash_keys() and then zlist_sort(). To
//  access the key for this item use zhash_cursor(). NOTE: do NOT modify
//  the table while iterating.
CZMQ_EXPORT void *
zhash_next(zhash_t *self);

//  After a successful first/next method, returns the key for the item that
//  was returned. This is a constant string that you may not modify or
//  deallocate, and which lasts as long as the item in the hash. After an
//  unsuccessful first/next, returns NULL.
CZMQ_EXPORT const char *
zhash_cursor(zhash_t *self);

//  Add a comment to hash table before saving to disk. You can add as many
//  comment lines as you like. These comment lines are discarded when loading
//  the file. If you use a null format, all comments are deleted.
CZMQ_EXPORT void
zhash_comment(zhash_t *self, const char *format, ...) CHECK_PRINTF(2);

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
zhash_pack(zhash_t *self);

//  Unpack binary frame into a new hash table. Packed data must follow format
//  defined by zhash_pack. Hash table is set to autofree. An empty frame
//  unpacks to an empty hash table.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zhash_t *
zhash_unpack(zframe_t *frame);

//  Save hash table to a text file in name=value format. Hash values must be
//  printable strings; keys may not contain '=' character. Returns 0 if OK,
//  else -1 if a file error occurred.
CZMQ_EXPORT int
zhash_save(zhash_t *self, const char *filename);

//  Load hash table from a text file in name=value format; hash table must
//  already exist. Hash values must printable strings; keys may not contain
//  '=' character. Returns 0 if OK, else -1 if a file was not readable.
CZMQ_EXPORT int
zhash_load(zhash_t *self, const char *filename);

//  When a hash table was loaded from a file by zhash_load, this method will
//  reload the file if it has been modified since, and is &quot;stable&quot;, i.e. not
//  still changing. Returns 0 if OK, -1 if there was an error reloading the
//  file.
CZMQ_EXPORT int
zhash_refresh(zhash_t *self);

//  Set hash for automatic value destruction
CZMQ_EXPORT void
zhash_autofree(zhash_t *self);

//  DEPRECATED as clumsy -- use zhash_first/_next instead
//  Apply function to each item in the hash table. Items are iterated in no
//  defined order. Stops if callback function returns non-zero and returns
//  final return code from callback function (zero = success).
//  Callback function for zhash_foreach method
CZMQ_EXPORT int
zhash_foreach(zhash_t *self, zhash_foreach_fn callback, void *argument);

//  Self test of this class
CZMQ_EXPORT void
zhash_test(int verbose);</code></pre>
<h2>Description</h2>
<p>zhash is an expandable hash table container. This is a simple container. For heavy-duty applications we recommend using zhashx. </p>
<p> Note that it&#8217;s relatively slow (50K insertions/deletes per second), so don&#8217;t do inserts/updates on the critical path for message I/O. It can do 2.5M lookups per second for 16-char keys. Timed on a 1.6GHz CPU.</p>
<h2>Example</h2>
<p><code>From zhash_test method</code>. </p>
<pre><code>zhash_t *hash = zhash_new();
assert(hash);
assert(zhash_size(hash) == 0);
assert(zhash_first(hash) == NULL);
assert(zhash_cursor(hash) == NULL);

//  Insert some items
int rc;
rc = zhash_insert(hash, &quot;DEADBEEF&quot;, &quot;dead beef&quot;);
char *item = (char *)zhash_first(hash);
assert(streq(zhash_cursor(hash), &quot;DEADBEEF&quot;));
assert(streq(item, &quot;dead beef&quot;));
assert(rc == 0);
rc = zhash_insert(hash, &quot;ABADCAFE&quot;, &quot;a bad cafe&quot;);
assert(rc == 0);
rc = zhash_insert(hash, &quot;C0DEDBAD&quot;, &quot;coded bad&quot;);
assert(rc == 0);
rc = zhash_insert(hash, &quot;DEADF00D&quot;, &quot;dead food&quot;);
assert(rc == 0);
assert(zhash_size(hash) == 4);

//  Look for existing items
item = (char *)zhash_lookup(hash, &quot;DEADBEEF&quot;);
assert(streq(item, &quot;dead beef&quot;));
item = (char *)zhash_lookup(hash, &quot;ABADCAFE&quot;);
assert(streq(item, &quot;a bad cafe&quot;));
item = (char *)zhash_lookup(hash, &quot;C0DEDBAD&quot;);
assert(streq(item, &quot;coded bad&quot;));
item = (char *)zhash_lookup(hash, &quot;DEADF00D&quot;);
assert(streq(item, &quot;dead food&quot;));

//  Look for non-existent items
item = (char *)zhash_lookup(hash, &quot;foo&quot;);
assert(item == NULL);

//  Try to insert duplicate items
rc = zhash_insert(hash, &quot;DEADBEEF&quot;, &quot;foo&quot;);
assert(rc == -1);
item = (char *)zhash_lookup(hash, &quot;DEADBEEF&quot;);
assert(streq(item, &quot;dead beef&quot;));

//  Some rename tests

//  Valid rename, key is now LIVEBEEF
rc = zhash_rename(hash, &quot;DEADBEEF&quot;, &quot;LIVEBEEF&quot;);
assert(rc == 0);
item = (char *)zhash_lookup(hash, &quot;LIVEBEEF&quot;);
assert(streq(item, &quot;dead beef&quot;));

//  Trying to rename an unknown item to a non-existent key
rc = zhash_rename(hash, &quot;WHATBEEF&quot;, &quot;NONESUCH&quot;);
assert(rc == -1);

//  Trying to rename an unknown item to an existing key
rc = zhash_rename(hash, &quot;WHATBEEF&quot;, &quot;LIVEBEEF&quot;);
assert(rc == -1);
item = (char *)zhash_lookup(hash, &quot;LIVEBEEF&quot;);
assert(streq(item, &quot;dead beef&quot;));

//  Trying to rename an existing item to another existing item
rc = zhash_rename(hash, &quot;LIVEBEEF&quot;, &quot;ABADCAFE&quot;);
assert(rc == -1);
item = (char *)zhash_lookup(hash, &quot;LIVEBEEF&quot;);
assert(streq(item, &quot;dead beef&quot;));
item = (char *)zhash_lookup(hash, &quot;ABADCAFE&quot;);
assert(streq(item, &quot;a bad cafe&quot;));

//  Test keys method
zlist_t *keys = zhash_keys(hash);
assert(zlist_size(keys) == 4);
zlist_destroy(&amp;keys);

//  Test dup method
zhash_t *copy = zhash_dup(hash);
assert(zhash_size(copy) == 4);
item = (char *)zhash_lookup(copy, &quot;LIVEBEEF&quot;);
assert(item);
assert(streq(item, &quot;dead beef&quot;));
zhash_destroy(&amp;copy);

//  Test pack/unpack methods
zframe_t *frame = zhash_pack(hash);
copy = zhash_unpack(frame);
zframe_destroy(&amp;frame);
assert(zhash_size(copy) == 4);
item = (char *)zhash_lookup(copy, &quot;LIVEBEEF&quot;);
assert(item);
assert(streq(item, &quot;dead beef&quot;));
zhash_destroy(&amp;copy);

//  Test save and load
zhash_comment(hash, &quot;This is a test file&quot;);
zhash_comment(hash, &quot;Created by %s&quot;, &quot;czmq_selftest&quot;);
zhash_save(hash, &quot;.cache&quot;);
copy = zhash_new();
assert(copy);
zhash_load(copy, &quot;.cache&quot;);
item = (char *)zhash_lookup(copy, &quot;LIVEBEEF&quot;);
assert(item);
assert(streq(item, &quot;dead beef&quot;));
zhash_destroy(&amp;copy);
zsys_file_delete(&quot;.cache&quot;);

//  Delete a item
zhash_delete(hash, &quot;LIVEBEEF&quot;);
item = (char *)zhash_lookup(hash, &quot;LIVEBEEF&quot;);
assert(item == NULL);
assert(zhash_size(hash) == 3);

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
        item = (char *)zhash_lookup(hash, testset[testnbr].name);
        assert(item);
        zhash_delete(hash, testset[testnbr].name);
        testset[testnbr].exists = false;
    } else {
        sprintf(testset[testnbr].name, &quot;%x-%x&quot;, rand(), rand());
        if (zhash_insert(hash, testset[testnbr].name, &quot;&quot;) == 0)
            testset[testnbr].exists = true;
    }
}
//  Test 10K lookups
for (iteration = 0; iteration &lt; 10000; iteration++)
    item = (char *)zhash_lookup(hash, &quot;DEADBEEFABADCAFE&quot;);

//  Destructor should be safe to call twice
zhash_destroy(&amp;hash);
zhash_destroy(&amp;hash);
assert(hash == NULL);

// Test autofree; automatically copies and frees string values
hash = zhash_new();
assert(hash);
zhash_autofree(hash);
char value[255];
strcpy(value, &quot;This is a string&quot;);
rc = zhash_insert(hash, &quot;key1&quot;, value);
assert(rc == 0);
strcpy(value, &quot;Inserting with the same key will fail&quot;);
rc = zhash_insert(hash, &quot;key1&quot;, value);
assert(rc == -1);
strcpy(value, &quot;Ring a ding ding&quot;);
rc = zhash_insert(hash, &quot;key2&quot;, value);
assert(rc == 0);
assert(streq((char *)zhash_lookup(hash, &quot;key1&quot;), &quot;This is a string&quot;));
assert(streq((char *)zhash_lookup(hash, &quot;key2&quot;), &quot;Ring a ding ding&quot;));
zhash_destroy(&amp;hash);
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
