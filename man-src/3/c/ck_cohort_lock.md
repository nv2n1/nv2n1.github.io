---
title: "ck_cohort_lock(3)"
name: "ck_cohort_lock"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_cohort_lock/"
description: "CK_COHORT_LOCK – acquire cohort lock"
---

<p><code>CK_COHORT_LOCK</code> &#8211; acquire cohort lock</p>
<h2>Library</h2>
<p>Concurrency Kit (libck, -lck)</p>
<h2>Synopsis</h2>
<p>In ck_cohort.h Fn CK_COHORT_LOCK COHORT_NAME cohort_name COHORT *cohort void *global_context void *local_context</p>
<h2>Description</h2>
<p>This call attempts to acquire both the local and global (if necessary) locks from Fa cohort . The call will block until both locks have been acquired. Fa global_context will be passed as the second argument to the function that was provided as the Fa global_lock_method argument to CK_COHORT_PROTOTYPE if that method is called, and Fa local_context will be passed to the function specified by Fa local_lock_method</p>
<h2>See Also</h2>
<p>ck_cohort3, CK_COHORT_PROTOTYPE3, CK_COHORT_TRYLOCK_PROTOTYPE3, CK_COHORT_INSTANCE3, CK_COHORT_INITIALIZER3, CK_COHORT_INIT3, CK_COHORT_UNLOCK3, CK_COHORT_LOCKED3, CK_COHORT_TRYLOCK3, </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a></p>
