---
title: "ck_hs_move(3)"
name: "ck_hs_move"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_hs_move/"
description: "ck_hs_move – move one from hash set to another"
---

<h2>NAME</h2>
<p> <code>ck_hs_move</code> &#8211; move one from hash set to another</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_hs.h Ft bool Fn ck_hs_move ck_hs_t *destination ck_hs_t *source ck_hs_hash_cb_t *hash_cb ck_hs_compare_cb_t *compare_cb struct ck_malloc *m</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_hs_move 3 function will initialize Fa source from Fa destination . The hash function is set to Fa hash_cb , comparison function to Fa compare_cb and the allocator callbacks to Fa m . Further modifications to Fa source will result in undefined behavior. Concurrent ck_hs_get3 and ck_hs_fas3 operations to Fa source are legal until the next write operation to Fa destination . </p>
<p> This operation moves ownership from one hash set object to another and re-assigns callback functions to developer-specified values. This allows for dynamic configuration of allocation callbacks and is necessary for use-cases involving executable code which may be unmapped underneath the hash set.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion Fn ck_hs_move 3 returns true and otherwise returns false to indicate an error.</p>
<h2>SEE ALSO</h2>
<p> ck_hs_init3, ck_hs_destroy3, CK_HS_HASH3, ck_hs_iterator_init3, ck_hs_next3, ck_hs_put3, ck_hs_put_unique3, ck_hs_set3, ck_hs_fas3, ck_hs_remove3, ck_hs_grow3, ck_hs_rebuild3, ck_hs_gc3, ck_hs_count3, ck_hs_reset3, ck_hs_reset_size3, ck_hs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
