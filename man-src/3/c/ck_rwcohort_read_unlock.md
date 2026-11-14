---
title: "ck_rwcohort_read_unlock(3)"
name: "ck_rwcohort_read_unlock"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rwcohort_read_unlock/"
description: "CK_RWCOHORT_READ_UNLOCK – relinquish read-only access to cohort-based reader-writer lock"
---

<p><code>CK_RWCOHORT_READ_UNLOCK</code> &#8211; relinquish read-only access to cohort-based reader-writer lock</p>
<h2>Library</h2>
<p>Concurrency Kit (libck, -lck)</p>
<h2>Synopsis</h2>
<p>In ck_cohort.h Fn CK_RWCOHORT_NEUTRAL_READ_UNLOCK COHORT_NAME cohort_name LOCK *lock COHORT *cohortvoid *global_context void *local_context Fn CK_RWCOHORT_RP_READ_UNLOCK COHORT_NAME cohort_name LOCK *lock COHORT *cohortvoid *global_context void *local_context Fn CK_RWCOHORT_WP_READ_UNLOCK COHORT_NAME cohort_name LOCK *lock COHORT *cohortvoid *global_context void *local_context</p>
<h2>Description</h2>
<p>This call will relinquish read-only permission to Fa lock . Fa cohort must point to a cohort whose global lock is the same as all other cohorts used with Fa lock . The Fa global_context and Fa local_context arguments will be passed along as the context arguments to any calls to Fa cohort .</p>
<h2>See Also</h2>
<p>ck_cohort3, CK_RWCOHORT_PROTOTYPE3, CK_RWCOHORT_INSTANCE3, CK_RWCOHORT_INITIALIZER3, CK_RWCOHORT_INIT3, CK_RWCOHORT_READ_LOCK3, CK_RWCOHORT_WRITE_LOCK3, CK_RWCOHORT_WRITE_UNLOCK3, </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a></p>
