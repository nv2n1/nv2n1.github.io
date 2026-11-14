---
title: "ck_cohort_trylock(3)"
name: "ck_cohort_trylock"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_cohort_trylock/"
description: "CK_COHORT_TRYLOCK – try to acquire cohort lock"
---

<p><code>CK_COHORT_TRYLOCK</code> &#8211; try to acquire cohort lock</p>
<h2>Library</h2>
<p>Concurrency Kit (libck, -lck)</p>
<h2>Synopsis</h2>
<p>In ck_cohort.h Fn CK_COHORT_TRYLOCK COHORT_NAME cohort_name COHORT *cohort void *global_trylock_context void *local_trylock_context void *lock_unlock_context</p>
<h2>Description</h2>
<p>This call attempts to acquire both the local and global (if necessary) locks from Fa cohort . It can only be used with cohort types that were defined using the CK_COHORT_TRYLOCK_PROTOTYPE3 macro. The call will not block and will return a bool that will evaluate to true iff the cohort was successfully acquired. Fa global_trylock_context will be passed as the second argument to the function that was provided as the Fa global_trylock_method argument to CK_COHORT_TRYLOCK_PROTOTYPE if that method is called, and Fa local_trylock_context will be passed to the function specified by Fa local_trylock_method . If the global lock acquisition fails, then the cohort will immediately release its local lock as well, and Fa local_unlock_context will be passed to the function specified by Fa local_unlock_method when this call is made.</p>
<h2>See Also</h2>
<p>ck_cohort3, CK_COHORT_PROTOTYPE3, CK_COHORT_TRYLOCK_PROTOTYPE3, CK_COHORT_INSTANCE3, CK_COHORT_INITIALIZER3, CK_COHORT_INIT3, CK_COHORT_LOCK3, CK_COHORT_UNLOCK3, CK_COHORT_LOCKED3, </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a></p>
