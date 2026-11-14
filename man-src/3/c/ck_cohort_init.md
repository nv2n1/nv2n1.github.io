---
title: "ck_cohort_init(3)"
name: "ck_cohort_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_cohort_init/"
description: "CK_COHORT_INIT – initialize instance of a cohort type"
---

<p><code>CK_COHORT_INIT</code> &#8211; initialize instance of a cohort type</p>
<h2>Library</h2>
<p>Concurrency Kit (libck, -lck)</p>
<h2>Synopsis</h2>
<p>In ck_cohort.h Fn CK_COHORT_INIT COHORT_NAME cohort_name COHORT *cohort void *global_lock void *local_lock unsigned int pass_limit</p>
<h2>Description</h2>
<p>Until a cohort instance is initialized using the CK_COHORT_INIT macro, any operations involving it will have undefined behavior. After this macro has been called, the cohort pointed to by the Fa cohort argument will use the lock pointed to by Fa global_lock as its global lock and the lock pointed to by Fa local_lock as its local lock. </p>
<p> The cohort will relinquish its global lock after Fa pass_limit consecutive acquisitions of its local lock, even if there are other threads waiting. If you are unsure of a value to use for the Fa pass_limit argument, you should use CK_COHORT_DEFAULT_LOCAL_PASS_LIMIT.</p>
<h2>See Also</h2>
<p>ck_cohort3, CK_COHORT_PROTOTYPE3, CK_COHORT_TRYLOCK_PROTOTYPE3, CK_COHORT_INSTANCE3, CK_COHORT_INITIALIZER3, CK_COHORT_LOCK3, CK_COHORT_UNLOCK3, CK_COHORT_LOCKED3, CK_COHORT_TRYLOCK3, </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a></p>
