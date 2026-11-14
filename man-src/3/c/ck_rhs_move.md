---
title: "ck_rhs_move(3)"
name: "ck_rhs_move"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rhs_move/"
description: "ck_rhs_move – move one from hash set to another"
---

<h2>NAME</h2>
<p> <code>ck_rhs_move</code> &#8211; move one from hash set to another</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_rhs.h Ft bool Fn ck_rhs_move ck_rhs_t *destination ck_rhs_t *source ck_rhs_hash_cb_t *hash_cb ck_rhs_compare_cb_t *compare_cb struct ck_malloc *m</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_rhs_move 3 function will initialize Fa source from Fa destination . The hash function is set to Fa hash_cb , comparison function to Fa compare_cb and the allocator callbacks to Fa m . Further modifications to Fa source will result in undefined behavior. Concurrent ck_rhs_get3 and ck_rhs_fas3 operations to Fa source are legal until the next write operation to Fa destination . </p>
<p> This operation moves ownership from one hash set object to another and re-assigns callback functions to developer-specified values. This allows for dynamic configuration of allocation callbacks and is necessary for use-cases involving executable code which may be unmapped underneath the hash set.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion Fn ck_rhs_move 3 returns true and otherwise returns false to indicate an error.</p>
<h2>SEE ALSO</h2>
<p> ck_rhs_init3, ck_rhs_destroy3, CK_RHS_HASH3, ck_rhs_iterator_init3, ck_rhs_next3, ck_rhs_put3, ck_rhs_put_unique3, ck_rhs_set3, ck_rhs_fas3, ck_rhs_remove3, ck_rhs_grow3, ck_rhs_rebuild3, ck_rhs_gc3, ck_rhs_count3, ck_rhs_reset3, ck_rhs_reset_size3, ck_rhs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
