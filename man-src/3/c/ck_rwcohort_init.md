---
title: "ck_rwcohort_init(3)"
name: "ck_rwcohort_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rwcohort_init/"
description: "CK_RWCOHORT_INIT – initialize instance of a cohort-based reader-writer lock type"
---

<p><code>CK_RWCOHORT_INIT</code> &#8211; initialize instance of a cohort-based reader-writer lock type</p>
<h2>Library</h2>
<p>Concurrency Kit (libck, -lck)</p>
<h2>Synopsis</h2>
<p>In ck_rwcohort.h Fn CK_RWCOHORT_NEUTRAL_INIT COHORT_NAME cohort_name LOCK *lock Fn CK_RWCOHORT_RP_INIT COHORT_NAME cohort_name LOCK *lock unsigned int wait_limit Fn CK_RWCOHORT_WP_INIT COHORT_NAME cohort_name LOCK *lock unsigned int wait_limit</p>
<h2>Description</h2>
<p>This macro initializes the lock instance pointed to by the Fa lock argument. Until a lock instance is initialized using the CK_RWCOHORT_INIT macro, any operations involving it will have undefined behavior. Note that the Fa wait_limit argument should only be used with reader-preference or writer-preference locks. For neutral locks, this argument should be excluded. If you are unsure of a value to use for the Fa wait_limit argument, you should use CK_RWCOHORT_STRATEGY_DEFAULT_LOCAL_WAIT_LIMIT.</p>
<h2>See Also</h2>
<p>ck_rwcohort3, CK_RWCOHORT_PROTOTYPE3, CK_RWCOHORT_TRYLOCK_PROTOTYPE3, CK_RWCOHORT_INSTANCE3, CK_RWCOHORT_INITIALIZER3, CK_RWCOHORT_LOCK3, CK_RWCOHORT_UNLOCK3, CK_RWCOHORT_LOCKED3, CK_RWCOHORT_TRYLOCK3, </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a></p>
