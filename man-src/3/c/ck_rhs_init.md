---
title: "ck_rhs_init(3)"
name: "ck_rhs_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rhs_init/"
description: "ck_rhs_init – initialize a hash set"
---

<h2>NAME</h2>
<p> <code>ck_rhs_init</code> &#8211; initialize a hash set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_rhs.h Ft typedef unsigned long Fn ck_rhs_hash_cb_t const void *key unsigned long seed Ft typedef bool Fn ck_rhs_compare_cb_t const void *c1 const void *c2 Ft bool Fn ck_rhs_init ck_rhs_t *hs unsigned int mode ck_rhs_hash_cb_t *hash_function ck_rhs_compare_cb_t *compare struct ck_malloc *allocator unsigned long capacity unsigned long seed</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_rhs_init function initializes the hash set pointed to by the Fa hs pointer. </p>
<p> The argument Fa mode specifies the type of key-value pairs to be stored in the hash set as well as the expected concurrent access model. The value of Fa mode consists of a bitfield of one of the following:</p>
<dl>
<dt><code>CK_RHS_MODE_OBJECT</code></p>
<dd> The hash set is meant to store pointers to objects. This provides a hint that only CK_MD_VMA_BITS are necessary to encode the key argument. Any unused pointer bits are leveraged for internal optimizations.</p>
<dt><code>CK_RHS_MODE_DIRECT</code></p>
<dd> The hash set is meant to directly store key values and that all bits of the key are used to encode values.</p>
<dt><code>CK_RHS_MODE_READ_MOSTLY</code></p>
<dd> Optimize read operations over put/delete.</dl>
<p> The concurrent access model is specified by:</p>
<dl>
<dt><code>CK_RHS_MODE_SPMC</code></p>
<dd> The hash set should allow for concurrent readers in the presence of a single writer.</p>
<dt><code>CK_RHS_MODE_MPMC</code></p>
<dd> The hash set should allow for concurrent readers in the presence of concurrent writers. This is currently unsupported.</dl>
<p> The developer is free to specify additional workload hints. These hints are one of:</p>
<dl>
</dl>
<p> The argument Fa hash_function is a mandatory pointer to a user-specified hash function. A user-specified hash function takes two arguments. The Fa key argument is a pointer to a key. The Fa seed argument is the initial seed associated with the hash set. This initial seed is specified by the user in ck_rhs_init3. </p>
<p> The Fa compare argument is an optional pointer to a user-specified key comparison function. If NULL is specified in this argument, then pointer equality will be used to determine key equality. A user-specified comparison function takes two arguments representing pointers to the objects being compared for equality. It is expected to return true if the keys are of equal value and false otherwise. </p>
<p> The Fa allocator argument is a pointer to a structure containing Fa malloc and Fa free function pointers which respectively define the memory allocation and destruction functions to be used by the hash set being initialized. </p>
<p> The argument Fa capacity represents the initial number of keys the hash set is expected to contain. This argument is simply a hint and the underlying implementation is free to allocate more or less memory than necessary to contain the number of entries Fa capacity specifies. </p>
<p> The argument Fa seed specifies the initial seed used by the underlying hash function. The user is free to choose a value of their choice.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion Fn ck_rhs_init returns a value of <code>true</code> and otherwise returns a value of <code>false</code> to indicate an error.</p>
<h2>ERRORS</h2>
<dl>
<p> The behavior of Fn ck_rhs_init is undefined if Fa hs is not a pointer to a <code>ck_rhs_t</code> object.</dl>
<h2>SEE ALSO</h2>
<p> ck_rhs_move3, ck_rhs_destroy3, CK_RHS_HASH3, ck_rhs_iterator_init3, ck_rhs_next3, ck_rhs_get3, ck_rhs_put3, ck_rhs_put_unique3, ck_rhs_set3, ck_rhs_fas3, ck_rhs_remove3, ck_rhs_grow3, ck_rhs_rebuild3, ck_rhs_gc3, ck_rhs_count3, ck_rhs_reset3, ck_rhs_reset_size3, ck_rhs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
