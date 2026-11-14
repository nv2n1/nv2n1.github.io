---
title: "ck_cohort(3)"
name: "ck_cohort"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_cohort/"
description: "ck_cohort – generalized interface for lock cohorts"
---

<h2>NAME</h2>
<p> <code>ck_cohort</code> &#8211; generalized interface for lock cohorts</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_cohort.h Fn CK_COHORT_PROTOTYPE COHORT_NAME cohort_name LOCK_FXN global_lock_method LOCK_FXN global_unlock_method LOCK_FXN local_lock_method LOCK_FXN local_unlock_method Fn CK_COHORT_TRYLOCK_PROTOTYPE COHORT_NAME cohort_name LOCK_FXN global_lock_method LOCK_FXN global_unlock_method BOOL_LOCK_FXN global_locked_method BOOL_LOCK_FXN global_trylock_method LOCK_FXN local_lock_method LOCK_FXN local_unlock_method BOOL_LOCK_FXN local_locked_method BOOL_LOCK_FXN local_trylock_method Fn CK_COHORT_INSTANCE COHORT_NAME cohort_name Fn CK_COHORT_INIT COHORT_NAME cohort_name ck_cohort *cohort void *global_lock void *local_lock unsigned int pass_limit Fn CK_COHORT_LOCK COHORT_NAME cohort_name ck_cohort *cohort void *global_context void *local_context Fn CK_COHORT_UNLOCK COHORT_NAME cohort_name ck_cohort *cohort void *global_context void *local_context </p>
<p> Where LOCK_FXN refers to a method with the signature<br />
 void(void *lock, void *context)<br />
 BOOL_LOCK_FXN refers to a method with the signature<br />
 bool(void *lock, void *context) </p>
<p> The Fa context argument in each signature is used to pass along any additional information that the lock might need for its lock, unlock and trylock methods. The values for this argument are provided to each call to CK_COHORT_LOCK3, CK_COHORT_UNLOCK3, CK_COHORT_LOCKED3, and CK_COHORT_TRYLOCK3</p>
<h2>DESCRIPTION</h2>
<p> ck_cohort.h provides an interface for defining lock cohorts with arbitrary lock types. Cohorts are a mechanism for coordinating threads on NUMA architectures in order to reduce the frequency with which a lock is passed between threads on different clusters. </p>
<p> Before using a cohort, the user must define a cohort type using either the Fn CK_COHORT_PROTOTYPE or the Fn CK_COHORT_TRYLOCK_PROTOTYPE macros. These macros allow the user to specify the lock methods that they would like the cohort to use. See the CK_COHORT_PROTOTYPE3 and CK_COHORT_TRYLOCK_PROTOTYPE3 man pages for more details. </p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_cohort.h&gt;
#include &lt;ck_pr.h&gt;
#include &lt;ck_spinlock.h&gt;
#include &lt;pthread.h&gt;
#include &lt;stdlib.h&gt;
/*
 * Create cohort methods with signatures that match
 * the required signature
 */
static void
ck_spinlock_lock_with_context(ck_spinlock_t *lock, void *context)
{
    (void)context;
    ck_spinlock_lock(lock);
    return;
}
static void
ck_spinlock_unlock_with_context(ck_spinlock_t *lock, void *context)
{
    (void)context;
    ck_spinlock_unlock(lock);
    return;
}
static bool
ck_spinlock_locked_with_context(ck_spinlock_t *lock, void *context)
{
    (void)context;
    return ck_spinlock_locked(lock);
}
/*
 * define a cohort type named "test_cohort" that will use
 * the above methods for both its global and local locks
 */
CK_COHORT_PROTOTYPE(test_cohort,
                    ck_spinlock_lock_with_context, ck_spinlock_unlock_with_context, ck_spinlock_locked_with_context,
                    ck_spinlock_lock_with_context, ck_spinlock_unlock_with_context, ck_spinlock_locked_with_context)
static ck_spinlock_t global_lock = CK_SPINLOCK_INITIALIZER;
static unsigned int ready;
static void *
function(void *context)
{
    CK_COHORT_INSTANCE(test_cohort) *cohort = context;
    while (ready == 0)
        ;
    while (ready &gt; 0) {
        /*
         * acquire the cohort lock before performing critical section.
         * note that we pass NULL for both the global and local context
         * arguments because neither the lock nor unlock functions
         * will use them.
         */
        CK_COHORT_LOCK(test_cohort, cohort, NULL, NULL);
        /* perform critical section */
        /* relinquish cohort lock */
        CK_COHORT_UNLOCK(test_cohort, cohort, NULL, NULL);
    }
    return NULL;
}
int main(void)
{
    unsigned int nthr = 4;
    unsigned int n_cohorts = 2;
    unsigned int i;
    /* allocate 2 cohorts of the defined type */
    CK_COHORT_INSTANCE(test_cohort) *cohorts =
        calloc(n_cohorts, sizeof(CK_COHORT_INSTANCE(test_cohort)));
    /* create local locks to use with each cohort */
    ck_spinlock_t *local_locks =
        calloc(n_cohorts, sizeof(ck_spinlock_t));
    pthread_t *threads =
        calloc(nthr, sizeof(pthread_t));
    /* initialize each of the cohorts before using them */
    for (i = 0; i &lt; n_cohorts; ++i) {
        CK_COHORT_INIT(test_cohort, cohorts + i, &amp;global_lock, local_locks + i,
                       CK_COHORT_DEFAULT_LOCAL_PASS_LIMIT);
    }
    /* start each thread and assign cohorts equally */
    for (i = 0; i &lt; nthr; ++i) {
        pthread_create(threads + i, NULL, function, cohorts + (i % n_cohorts));
    }
    ck_pr_store_uint(&amp;ready, 1);
    sleep(10);
    ck_pr_store_uint(&amp;ready, 0);
    for (i = 0; i &lt; nthr; ++i) {
        pthread_join(threads[i], NULL);
    }
    return 0;
}
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> CK_COHORT_PROTOTYPE3, CK_COHORT_TRYLOCK_PROTOTYPE3, CK_COHORT_INSTANCE3, CK_COHORT_INITIALIZER3, CK_COHORT_INIT3, CK_COHORT_LOCK3, CK_COHORT_UNLOCK3, CK_COHORT_LOCKED3, CK_COHORT_TRYLOCK3, </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
