---
title: "ck_rwcohort(3)"
name: "ck_rwcohort"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rwcohort/"
description: "ck_rwcohort – generalized interface for reader-writer locks using cohort locks"
---

<h2>NAME</h2>
<p> <code>ck_rwcohort</code> &#8211; generalized interface for reader-writer locks using cohort locks</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_rwcohort.h In each of the following macros, &quot;STRATEGY&quot; should be replaced with either &quot;NEUTRAL&quot;, &quot;RP&quot;, or &quot;WP&quot; depending on which locking strategy the user prefers. RP and WP represent reader preference and writer preference, respectively, while NEUTRAL represents a strategy neutral to reads vs. writes. Fn CK_RWCOHORT_STRATEGY_PROTOTYPE COHORT_NAME cohort_name Fn CK_RWCOHORT_STRATEGY_NAME COHORT_NAME cohort_name Fn CK_RWCOHORT_STRATEGY_INSTANCE COHORT_NAME cohort_name Fn CK_RWCOHORT_STRATEGY_INIT COHORT_NAME cohort_name RWCOHORT lock unsigned int wait_limit Note: the wait_limit argument should be omitted for locks using the neutral strategy Fn CK_RWCOHORT_STRATEGY_READ_LOCK COHORT_NAME cohort_name RWCOHORT lock COHORT cohort void *global_context void *local_context Fn CK_RWCOHORT_STRATEGY_READ_UNLOCK COHORT_NAME cohort_name RWCOHORT lock COHORT cohort void *global_context void *local_context Fn CK_RWCOHORT_STRATEGY_WRITE_LOCK COHORT_NAME cohort_name RWCOHORT lock COHORT cohort void *global_context void *local_context Fn CK_RWCOHORT_STRATEGY_WRITE_UNLOCK COHORT_NAME cohort_name RWCOHORT lock COHORT cohort void *global_context void *local_context </p>
<p> Arguments of type RWCOHORT must be pointers to structs defined using the CK_RWCOHORT_STRATEGY_PROTOTYPE3 macro with the same strategy and cohort name as the current call. </p>
<p> Arguments of type COHORT must be pointers to structs defined using the CK_COHORT_PROTOTYPE3 macro.</p>
<h2>DESCRIPTION</h2>
<p> ck_rwcohort.h provides an interface for defining reader-writer locks that use cohort locks internally to increase performance on NUMA architectures. See ck_cohort3 for more information about cohort locks. </p>
<p> Before using a reader-writer cohort lock, the user must define a cohort type using either the CK_COHORT_PROTOTYPE3 or the CK_COHORT_TRYLOCK_PROTOTYPE3 macros, and define a reader-writer lock type using the CK_RWCOHORT_PROTOTYPE3 macro. </p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_cohort.h&gt;
#include &lt;ck_pr.h&gt;
#include &lt;ck_rwcohort.h&gt;
#include &lt;ck_spinlock.h&gt;
#include &lt;pthread.h&gt;
#include &lt;stdlib.h&gt;
/* Create cohort methods with signatures that match the required signature */
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
/* define a reader-writer type using the same cohort type */
CK_RWCOHORT_WP_PROTOTYPE(test_cohort)
static ck_spinlock_t global_lock = CK_SPINLOCK_INITIALIZER;
static CK_COHORT_INSTANCE(test_cohort) * cohorts;
static CK_RWCOHORT_WP_INSTANCE(test_cohort) rw_cohort = CK_RWCOHORT_WP_INITIALIZER;
static unsigned int ready;
static void *
function(void *context)
{
    CK_COHORT_INSTANCE(test_cohort) *cohort = context;
    while (ck_pr_load_uint(&amp;ready) == 0)
        ;
    while (ck_pr_load_uint(&amp;ready) &gt; 0) {
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
