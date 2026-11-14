---
title: "ck_cohort_instance(3)"
name: "ck_cohort_instance"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_cohort_instance/"
description: "CK_COHORT_INSTANCE – declare an instance of a cohort type"
---

<p><code>CK_COHORT_INSTANCE</code> &#8211; declare an instance of a cohort type</p>
<h2>Library</h2>
<p>Concurrency Kit (libck, -lck)</p>
<h2>Synopsis</h2>
<p>In ck_cohort.h Fn CK_COHORT_INSTANCE COHORT_NAME cohort_name</p>
<h2>Description</h2>
<p>The user must use this macro to declare instances of cohort types that they have defined. For instance, if they have used the CK_COHORT_PROTOTYPE macro to define a cohort type with name foo, they would create an instance of this type as follows:<br />
 CK_COHORT_INSTANCE(foo) cohort; </p>
<p> This macro should also be used when allocating memory for cohorts. For instance, to allocate a block of 4 cohorts:<br />
 CK_COHORT_INSTANCE(foo) *cohorts = malloc(4 * sizeof(CK_COHORT_INSTANCE(foo)));</p>
<h2>See Also</h2>
<p>ck_cohort3, CK_COHORT_PROTOTYPE3, CK_COHORT_TRYLOCK_PROTOTYPE3, CK_COHORT_INSTANCE3, CK_COHORT_INITIALIZER3, CK_COHORT_LOCK3, CK_COHORT_UNLOCK3, CK_COHORT_LOCKED3, CK_COHORT_TRYLOCK3, </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a></p>
