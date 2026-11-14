---
title: "ck_cohort_trylock_prototype(3)"
name: "ck_cohort_trylock_prototype"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_cohort_trylock_prototype/"
description: "CK_COHORT_TRYLOCK_PROTOTYPE – define cohort type with specified lock types"
---

<p><code>CK_COHORT_TRYLOCK_PROTOTYPE</code> &#8211; define cohort type with specified lock types</p>
<h2>Library</h2>
<p>Concurrency Kit (libck, -lck)</p>
<h2>Synopsis</h2>
<p>In ck_cohort.h Fn CK_COHORT_TRYLOCK_PROTOTYPE COHORT_NAME cohort_name LOCK_FXN global_lock_method LOCK_FXN global_unlock_method BOOL_LOCK_FXN global_locked_method BOOL_LOCK_FXN global_trylock_method LOCK_FXN local_lock_method LOCK_FXN local_unlock_method BOOL_LOCK_FXN local_locked_method BOOL_LOCK_FXN local_trylock_method</p>
<h2>Description</h2>
<p>The ck_cohort.h header file does not define any cohort types. Instead, the user must use the CK_COHORT_PROTOTYPE or CK_COHORT_TRYLOCK_PROTOTYPE macros to define any types they want to use. They must use CK_COHORT_TRYLOCK_PROTOTYPE if they want their cohort type to have support for trylock operations. The CK_COHORT_TRYLOCK_PROTOTYPE macro takes the following arguments: </p>
<p> Fa cohort_name : An identifier used for this cohort type. This will have to be passed to each of the other CK_COHORT macros.<br />
 Fa global_lock_method : The method that should be called to acquire the global lock<br />
 Fa global_unlock_method : The method that should be called to relinquish the global lock<br />
 Fa global_locked_method : This method should return true iff the global lock is acquired by a thread.<br />
 Fa global_trylock_method : The method that should be called to try to acquire the global lock. It should not block and return true iff the lock was successfully acquired.<br />
 Fa local_lock_method : The method that should be called to acquire the local lock<br />
 Fa local_unlock_method : The method that should be called to relinquish the local lock<br />
 Fa global_locked_method : This method should return true iff the global lock is acquired by a thread.<br />
 Fa local_trylock_method : The method that should be called to try to acquire the local lock. It should not block and return true iff the lock was successfully acquired. </p>
<p> Instances of the defined cohort type can be declared as: </p>
<p>&nbsp;<wbr>CK_COHORT_INSTANCE(cohort_name)&nbsp;<wbr>cohort;</p>
<h2>See Also</h2>
<p>ck_cohort3, CK_COHORT_PROTOTYPE3, CK_COHORT_INSTANCE3, CK_COHORT_INITIALIZER3, CK_COHORT_INIT3, CK_COHORT_LOCK3, CK_COHORT_UNLOCK3, CK_COHORT_LOCKED3, CK_COHORT_TRYLOCK3, </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a></p>
