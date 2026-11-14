---
title: "ck_spinlock(3)"
name: "ck_spinlock"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_spinlock/"
description: "ck_spinlock_init ck_spinlock_lock ck_spinlock_unlock ck_spinlock_locked ck_spinlock_trylock ck_spinlock_anderson_init ck_spinlock_anderson_locked ck_spinlock_anderson_lock ck_spinlock_anderson_unlo..."
---

<h2>NAME</h2>
<p> <code>ck_spinlock_init</code> <code>ck_spinlock_lock</code> <code>ck_spinlock_unlock</code> <code>ck_spinlock_locked</code> <code>ck_spinlock_trylock</code> <code>ck_spinlock_anderson_init</code> <code>ck_spinlock_anderson_locked</code> <code>ck_spinlock_anderson_lock</code> <code>ck_spinlock_anderson_unlock</code> <code>ck_spinlock_cas_init</code> <code>ck_spinlock_cas_locked</code> <code>ck_spinlock_cas_lock</code> <code>ck_spinlock_cas_lock_eb</code> <code>ck_spinlock_cas_trylock</code> <code>ck_spinlock_cas_unlock</code> <code>ck_spinlock_clh_init</code> <code>ck_spinlock_clh_locked</code> <code>ck_spinlock_clh_lock</code> <code>ck_spinlock_clh_unlock</code> <code>ck_spinlock_dec_init</code> <code>ck_spinlock_dec_locked</code> <code>ck_spinlock_dec_lock</code> <code>ck_spinlock_dec_lock_eb</code> <code>ck_spinlock_dec_trylock</code> <code>ck_spinlock_dec_unlock</code> <code>ck_spinlock_fas_init</code> <code>ck_spinlock_fas_lock</code> <code>ck_spinlock_fas_lock_eb</code> <code>ck_spinlock_fas_locked</code> <code>ck_spinlock_fas_trylock</code> <code>ck_spinlock_fas_unlock</code> <code>ck_spinlock_hclh_init</code> <code>ck_spinlock_hclh_locked</code> <code>ck_spinlock_hclh_lock</code> <code>ck_spinlock_hclh_unlock</code> <code>ck_spinlock_mcs_init</code> <code>ck_spinlock_mcs_locked</code> <code>ck_spinlock_mcs_lock</code> <code>ck_spinlock_mcs_trylock</code> <code>ck_spinlock_mcs_unlock</code> <code>ck_spinlock_ticket_init</code> <code>ck_spinlock_ticket_locked</code> <code>ck_spinlock_ticket_lock</code> <code>ck_spinlock_ticket_lock_pb</code> <code>ck_spinlock_ticket_trylock</code> <code>ck_spinlock_ticket_unlock</code> &#8211; spinlock implementations</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_spinlock.h </p>
<p> <code>ck_spinlock_t spinlock = CK_SPINLOCK_INITIALIZER;</code> Ft void Fn ck_spinlock_init ck_spinlock_t *lock Ft void Fn ck_spinlock_lock ck_spinlock_t *lock Ft void Fn ck_spinlock_unlock ck_spinlock_t *lock Ft bool Fn ck_spinlock_locked ck_spinlock_t *lock Ft bool Fn ck_spinlock_trylock ck_spinlock_t *lock Ft void Fn ck_spinlock_anderson_init ck_spinlock_anderson_t *lock ck_spinlock_anderson_thread_t *slots unsigned int count Ft bool Fn ck_spinlock_anderson_locked ck_spinlock_anderson_t *lock Ft void Fn ck_spinlock_anderson_lock ck_spinlock_anderson_t *lock ck_spinlock_anderson_thread_t **slot Ft void Fn ck_spinlock_anderson_unlock ck_spinlock_anderson_t *lock ck_spinlock_anderson_thread_t *slot </p>
<p> <code>ck_spinlock_cas_t spinlock = CK_SPINLOCK_CAS_INITIALIZER;</code> Ft void Fn ck_spinlock_cas_init ck_spinlock_cas_t *lock Ft bool Fn ck_spinlock_cas_locked ck_spinlock_cas_t *lock Ft void Fn ck_spinlock_cas_lock ck_spinlock_cas_t *lock Ft void Fn ck_spinlock_cas_lock_eb ck_spinlock_cas_t *lock Ft bool Fn ck_spinlock_cas_trylock ck_spinlock_cas_t *lock Ft void Fn ck_spinlock_cas_unlock ck_spinlock_cas_t *lock Ft void Fn ck_spinlock_clh_init ck_spinlock_clh_t **lock ck_spinlock_clh_t *unowned Ft bool Fn ck_spinlock_clh_locked ck_spinlock_clh_t **lock Ft void Fn ck_spinlock_clh_lock ck_spinlock_clh_t **lock ck_spinlock_clh_t *node Ft void Fn ck_spinlock_clh_unlock ck_spinlock_clh_t **node </p>
<p> <code>ck_spinlock_dec_t spinlock = CK_SPINLOCK_DEC_INITIALIZER;</code> Ft void Fn ck_spinlock_dec_init ck_spinlock_dec_t *lock Ft bool Fn ck_spinlock_dec_locked ck_spinlock_dec_t *lock Ft void Fn ck_spinlock_dec_lock ck_spinlock_dec_t *lock Ft void Fn ck_spinlock_dec_lock_eb ck_spinlock_dec_t *lock Ft bool Fn ck_spinlock_dec_trylock ck_spinlock_dec_t *lock Ft void Fn ck_spinlock_dec_unlock ck_spinlock_dec_t *lock </p>
<p> <code>ck_spinlock_fas_t spinlock = CK_SPINLOCK_FAS_INITIALIZER;</code> Ft void Fn ck_spinlock_fas_init ck_spinlock_fas_t *lock Ft void Fn ck_spinlock_fas_lock ck_spinlock_fas_t *lock Ft void Fn ck_spinlock_fas_lock_eb ck_spinlock_fas_t *lock Ft bool Fn ck_spinlock_fas_locked ck_spinlock_fas_t *lock Ft bool Fn ck_spinlock_fas_trylock ck_spinlock_fas_t *lock Ft void Fn ck_spinlock_fas_unlock ck_spinlock_fas_t *lock </p>
<p> Ft void Fn ck_spinlock_hclh_init ck_spinlock_hclh_t **lock ck_spinlock_hclh_t *unowned Ft bool Fn ck_spinlock_hclh_locked ck_spinlock_hclh_t **lock Ft void Fn ck_spinlock_hclh_lock ck_spinlock_hclh_t **lock ck_spinlock_hclh_t *node Ft void Fn ck_spinlock_hclh_unlock ck_spinlock_hclh_t **node </p>
<p> <code>ck_spinlock_mcs_t spinlock = CK_SPINLOCK_MCS_INITIALIZER;</code> Ft void Fn ck_spinlock_mcs_init ck_spinlock_mcs_t **lock Ft bool Fn ck_spinlock_mcs_locked ck_spinlock_mcs_t **lock Ft void Fn ck_spinlock_mcs_lock ck_spinlock_mcs_t **lock ck_spinlock_mcs_t *node Ft bool Fn ck_spinlock_mcs_trylock ck_spinlock_mcs_t **lock ck_spinlock_mcs_t *node Ft void Fn ck_spinlock_mcs_unlock ck_spinlock_mcs_t **lock ck_spinlock_mcs_t *node </p>
<p> <code>ck_spinlock_ticket_t spinlock = CK_SPINLOCK_TICKET_INITIALIZER;</code> Ft void Fn ck_spinlock_ticket_init ck_spinlock_ticket_t *lock Ft bool Fn ck_spinlock_ticket_locked ck_spinlock_ticket_t *lock Ft void Fn ck_spinlock_ticket_lock ck_spinlock_ticket_t *lock Ft void Fn ck_spinlock_ticket_lock_pb ck_spinlock_ticket_t *lock unsigned int period Ft bool Fn ck_spinlock_ticket_trylock ck_spinlock_ticket_t *lock Ft void Fn ck_spinlock_ticket_unlock ck_spinlock_ticket_t *lock</p>
<h2>DESCRIPTION</h2>
<p> A family of busy-wait spinlock implementations. The ck_spinlock_t implementation is simply a wrapper around the fetch-and-swap (ck_spinlock_fas_t) implementation. The table below provides a summary of the current implementations. </p>
<pre><code>
| Namespace | Algorithm | Type | Restrictions | Fair |
    '----------------------|-----------------------------|---------------|-------------------------|--------' ck_spinlock_anderson Anderson Array Fixed number of threads Yes
            ck_spinlock_cas Compare -
        and-Swap Centralized None No
               ck_spinlock_clh Craig,
    Landin and Hagersten Queue Lifetime requirements Yes
            ck_spinlock_dec
            Decrement(Linux kernel) Centralized UINT_MAX concurrency No
        ck_spinlock_fas Fetch
        - and-store Centralized None No ck_spinlock_hclh Hierarchical CLH Queue Lifetime requirements Yes *ck_spinlock_mcs Mellor - Crummey and Scott Queue None Yes ck_spinlock_ticket Ticket Centralized None Yes
</code></pre>
<p> * Hierarchical CLH only offers weak fairness for threads accross cluster nodes. </p>
<p> If contention is low and there is no hard requirement for starvation-freedom then a centralized greedy (unfair) spinlock is recommended. If contention is high and there is no requirement for starvation-freedom then a centralized greedy spinlock is recommended to be used with an exponential backoff mechanism. If contention is generally low and there is a hard requirement for starvation-freedom then the ticket lock is recommended. If contention is high and there is a hard requirement for starvation-freedom then the Craig and Landin and Hagersten queue spinlock is recommended unless stack allocation is necessary or NUMA factor is high, in which case the Mellor-Crummey and Scott spinlock is recommended. If you cannot afford <a href="/docs/linux/man/n-o/">O</a>(n) space-usage from array or queue spinlocks but still require fairness under high contention then the ticket lock with proportional back-off is recommended. If NUMA factor is high but prefer a greedy lock, then please see ck_cohort3.</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_spinlock.h&gt;
#include &lt;stdbool.h&gt;
/*
 * Alternatively, the mutex may be initialized at run-time with
 * ck_spinlock_init(&amp;mutex).
 */
ck_spinlock_t mutex = CK_SPINLOCK_INITIALIZER;
void example(void)
{
    ck_spinlock_lock(&amp;mutex);
    /*
     * Critical section.
     */
    ck_spinlock_unlock(&amp;mutex);
    ck_spinlock_lock_eb(&amp;mutex);
    /*
     * Critical section.
     */
    ck_spinlock_unlock(&amp;mutex);
    if (ck_spinlock_trylock(&amp;mutex) == true) {
        /*
         * Critical section.
         */
        ck_spinlock_unlock(&amp;mutex);
    }
}
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> ck_cohort3, ck_elide3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
