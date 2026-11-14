---
title: "ck_cohort_unlock(3)"
name: "ck_cohort_unlock"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_cohort_unlock/"
description: "CK_COHORT_UNLOCK – release cohort lock"
---

<p><code>CK_COHORT_UNLOCK</code> &#8211; release cohort lock</p>
<h2>Library</h2>
<p>Concurrency Kit (libck, -lck)</p>
<h2>Synopsis</h2>
<p>In ck_cohort.h Fn CK_COHORT_UNLOCK COHORT_NAME cohort_name COHORT *cohort void *global_context void *local_context</p>
<h2>Description</h2>
<p>This call instructs Fa cohort to relinquish its local lock and potentially its global lock as well. Fa global_context will be passed as the second argument to the function that was provided as the Fa global_lock_method argument to CK_COHORT_PROTOTYPE if that method is called, and Fa local_context will be passed to the function specified by Fa local_lock_method</p>
<h2>See Also</h2>
<p>ck_cohort3, CK_COHORT_PROTOTYPE3, CK_COHORT_TRYLOCK_PROTOTYPE3, CK_COHORT_INSTANCE3, CK_COHORT_INITIALIZER3, CK_COHORT_INIT3, CK_COHORT_LOCK3, CK_COHORT_LOCKED3, CK_COHORT_TRYLOCK3, </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a></p>
