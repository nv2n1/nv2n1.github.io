---
title: "ck_rwcohort_prototype(3)"
name: "ck_rwcohort_prototype"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rwcohort_prototype/"
description: "CK_RWCOHORT_PROTOTYPE – define reader-writer cohort-based lock using the specified cohort type"
---

<p><code>CK_RWCOHORT_PROTOTYPE</code> &#8211; define reader-writer cohort-based lock using the specified cohort type</p>
<h2>Library</h2>
<p>Concurrency Kit (libck, -lck)</p>
<h2>Synopsis</h2>
<p>In ck_rwcohort.h Fn CK_RWCOHORT_NEUTRAL_PROTOTYPE COHORT_NAME cohort_name Fn CK_RWCOHORT_RP_PROTOTYPE COHORT_NAME cohort_name Fn CK_RWCOHORT_WP_PROTOTYPE COHORT_NAME cohort_name</p>
<h2>Description</h2>
<p>The ck_rwcohort.h header file does not define any cohort types. Instead, the user must use the CK_RWCOHORT_PROTOTYPE macro to define any types they want to use. This macro takes a single argument which corresponds to the type of the cohort lock that the reader-writer lock should use. A cohort type must have already been defined with that name using the CK_COHORT_PROTOTYPE3 or CK_COHORT_TRYLOCK_PROTOTYPE3 macros. </p>
<p> Instances of the defined lock type can be declared as: </p>
<p>&nbsp;<wbr>CK_RWCOHORT_INSTANCE(cohort_name)&nbsp;<wbr>lock;</p>
<h2>See Also</h2>
<p>ck_rwcohort3, CK_COHORT_PROTOTYPE3, CK_COHORT_TRYLOCK_PROTOTYPE3, CK_RWCOHORT_INSTANCE3, CK_RWCOHORT_INITIALIZER3, CK_RWCOHORT_INIT3, CK_RWCOHORT_READ_LOCK3, CK_RWCOHORT_READ_UNLOCK3, CK_RWCOHORT_WRITE_LOCK3, CK_RWCOHORT_WRITE_UNLOCK3, </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a></p>
