---
title: "ck_ht_init(3)"
name: "ck_ht_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_init/"
description: "ck_ht_init – initialize a hash table"
---

<h2>NAME</h2>
<p> <code>ck_ht_init</code> &#8211; initialize a hash table</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft typedef void Fn ck_ht_hash_cb_t ck_ht_hash_t *h const void *key size_t key_length uint64_t seed Ft bool Fn ck_ht_init ck_ht_t *ht enum ck_ht_mode mode ck_ht_hash_cb_t *hash_function struct ck_malloc *allocator uint64_t capacity uint64_t seed</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_init function initializes the hash table pointed to by the Fa ht pointer. </p>
<p> The argument Fa mode specifies the type of key-value pairs to be stored in the hash table. The value of Fa mode may be one of:</p>
<dl>
<dt><code>CK_HT_MODE_BYTESTRING</code></p>
<dd> The hash table is meant to store key-value pointers where key is a region of memory that is up to 65536 bytes long. This pointer will be dereferenced during hash table operations for key comparison. Entries of this hash table are expected to be interacted with using the ck_ht_entry_empty3, ck_ht_entry_key3, ck_ht_entry_key_length3, ck_ht_entry_value3, and ck_ht_entry_set3 functions. Attempting a hash table operation with a key of value NULL or (void *)UINTPTR_MAX will result in undefined behavior.</p>
<dt><code>CK_HT_MODE_DIRECT</code></p>
<dd> The hash table is meant to store key-value pointers where the key is of fixed width field compatible with the <code>uintptr_t</code> type. The key will be directly compared with other keys for equality. Entries of this hash table are expected to be interacted with using the ck_ht_entry_empty3, ck_ht_entry_key_direct3, ck_ht_entry_value_direct3 and ck_ht_entry_set_direct3 functions. Attempting a hash table operation with a key of value of 0 or UINTPTR_MAX will result in undefined behavior.</dl>
<p> In addition to this, the user may bitwise OR the mode flag with CK_HT_WORKLOAD_DELETE to indicate that the hash table will have to handle a delete heavy workload, in which case stronger bounds on latency can be provided at the cost of approximately 13% higher memory usage. The argument Fa hash_function is a pointer to a user-specified hash function. It is optional, if <code>NULL</code> is specified, then the default hash function implementation will be used ( ck_ht_hash3). A user-specified hash function takes four arguments. The Fa h argument is a pointer to a hash value object. The hash function is expected to update the Fa value object of type Fa uint64_t contained with-in the object pointed to by Fa h . The Fa key argument is a pointer to a key, the Fa key_length argument is the length of the key and the Fa seed argument is the initial seed associated with the hash table. This initial seed is specified by the user in ck_ht_init3. </p>
<p> The Fa allocator argument is a pointer to a structure containing Fa malloc and Fa free function pointers which respectively define the memory allocation and destruction functions to be used by the hash table being initialized. </p>
<p> The argument Fa capacity represents the initial number of key-value pairs the hash table is expected to contain. This argument is simply a hint and the underlying implementation is free to allocate more or less memory than necessary to contain the number of entries Fa capacity specifies. </p>
<p> The argument Fa seed specifies the initial seed used by the underlying hash function. The user is free to choose a value of their choice. </p>
<p> The hash table is safe to access by multiple readers in the presence of one concurrent writer. Behavior is undefined in the presence of concurrent writers.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion Fn ck_ht_init returns a value of <code>true</code> and otherwise returns a value of <code>false</code> to indicate an error.</p>
<h2>ERRORS</h2>
<dl>
<p> The behavior of Fn ck_ht_init is undefined if Fa ht is not a pointer to a <code>ck_ht_t</code> object.</dl>
<h2>SEE ALSO</h2>
<p> ck_ht_stat3, ck_ht_destroy3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_get_spmc3, ck_ht_grow_spmc3, ck_ht_remove_spmc3, ck_ht_reset_spmc3, ck_ht_reset_size_spmc3, ck_ht_count3, ck_ht_entry_empty3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key3, ck_ht_entry_key_length3, ck_ht_entry_value3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value_direct3, ck_ht_iterator_init3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
