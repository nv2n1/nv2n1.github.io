---
title: "ck_rwcohort_read_lock(3)"
name: "ck_rwcohort_read_lock"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rwcohort_read_lock/"
description: "CK_RWCOHORT_READ_LOCK – acquire read-only permission for cohort-based reader-writer lock"
---

<p><code>CK_RWCOHORT_READ_LOCK</code> &#8211; acquire read-only permission for cohort-based reader-writer lock</p>
<h2>Library</h2>
<p>Concurrency Kit (libck, -lck)</p>
<h2>Synopsis</h2>
<p>In ck_cohort.h Fn CK_RWCOHORT_NEUTRAL_READ_LOCK COHORT_NAME cohort_name LOCK *lock COHORT *cohortvoid *global_context void *local_context Fn CK_RWCOHORT_RP_READ_LOCK COHORT_NAME cohort_name LOCK *lock COHORT *cohortvoid *global_context void *local_context Fn CK_RWCOHORT_WP_READ_LOCK COHORT_NAME cohort_name LOCK *lock COHORT *cohortvoid *global_context void *local_context</p>
<h2>Description</h2>
<p>This call will acquire read-only permission from Fa lock . The call will block until this permission has been acquired. Fa cohort must point to a cohort whose global lock is the same as all other cohorts used with Fa lock . The Fa global_context and Fa local_context arguments will be passed along as the context arguments to any calls to Fa cohort .</p>
<h2>See Also</h2>
<p>ck_cohort3, CK_RWCOHORT_PROTOTYPE3, CK_RWCOHORT_INSTANCE3, CK_RWCOHORT_INITIALIZER3, CK_RWCOHORT_INIT3, CK_RWCOHORT_READ_UNLOCK3, CK_RWCOHORT_WRITE_LOCK3, CK_RWCOHORT_WRITE_UNLOCK3, </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a></p>
