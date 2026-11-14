---
title: "ck_rwcohort_instance(3)"
name: "ck_rwcohort_instance"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rwcohort_instance/"
description: "CK_RWCOHORT_INSTANCE – declare an instance of a cohort-based reader-writer lock type"
---

<p><code>CK_RWCOHORT_INSTANCE</code> &#8211; declare an instance of a cohort-based reader-writer lock type</p>
<h2>Library</h2>
<p>Concurrency Kit (libck, -lck)</p>
<h2>Synopsis</h2>
<p>In ck_cohort.h Fn CK_RWCOHORT_NEUTRAL_INSTANCE COHORT_NAME cohort_name Fn CK_RWCOHORT_RP_INSTANCE COHORT_NAME cohort_name Fn CK_RWCOHORT_WP_INSTANCE COHORT_NAME cohort_name</p>
<h2>Description</h2>
<p>The user must use this macro to declare instances of lock types that they have defined using the CK_RWCOHORT_PROTOTYPE3 macro. The cohort_name must be the same as the one used in the prototype macro. For instance, if CK_RWCOHORT_PROTOTYPE was called with the name &quot;foo&quot;, the CK_RWCOHORT_INSTANCE macro should be called as<br />
 CK_RWCOHORT_INSTANCE(foo) cohort; </p>
<p> This macro should also be used when allocating memory for cohorts. For instance, to allocate a block of 4 cohorts:<br />
 CK_RWCOHORT_WP_INSTANCE(foo) *cohorts = malloc(4 * sizeof(CK_RWCOHORT_WP_INSTANCE(foo)));</p>
<h2>See Also</h2>
<p>ck_rwcohort3, CK_RWCOHORT_PROTOTYPE3, CK_RWCOHORT_TRYLOCK_PROTOTYPE3, CK_RWCOHORT_INSTANCE3, CK_RWCOHORT_INITIALIZER3, CK_RWCOHORT_LOCK3, CK_RWCOHORT_UNLOCK3, CK_RWCOHORT_LOCKED3, CK_RWCOHORT_TRYLOCK3, </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a></p>
