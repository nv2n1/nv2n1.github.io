---
title: "ck_elide(3)"
name: "ck_elide"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_elide/"
description: "CK_ELIDE_PROTOTYPE CK_ELIDE_LOCK_ADAPTIVE CK_ELIDE_UNLOCK_ADAPTIVE CK_ELIDE_LOCK CK_ELIDE_UNLOCK CK_ELIDE_TRYLOCK_PROTOTYPE CK_ELIDE_TRYLOCK – lock elision wrappers"
---

<h2>NAME</h2>
<p> <code>CK_ELIDE_PROTOTYPE</code> <code>CK_ELIDE_LOCK_ADAPTIVE</code> <code>CK_ELIDE_UNLOCK_ADAPTIVE</code> <code>CK_ELIDE_LOCK</code> <code>CK_ELIDE_UNLOCK</code> <code>CK_ELIDE_TRYLOCK_PROTOTYPE</code> <code>CK_ELIDE_TRYLOCK</code> &#8211; lock elision wrappers</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_elide.h </p>
<p> <code>ck_elide_stat_t stat = CK_ELIDE_STAT_INITIALIZER;</code> </p>
<p> Ft void Fn ck_elide_stat_init ck_elide_stat_t * </p>
<p> <code>struct ck_elide_config config = CK_ELIDE_CONFIG_DEFAULT_INITIALIZER;</code> </p>
<pre><code>
struct ck_elide_config {
    unsigned short skip_busy;
    short retry_busy;
    unsigned short skip_other;
    short retry_other;
    unsigned short skip_conflict;
    short retry_conflict;
};
</code></pre>
<p> Fn CK_ELIDE_PROTOTYPE NAME TYPE LOCK_PREDICATE LOCK_FUNCTION UNLOCK_PREDICATE UNLOCK_FUNCTION Fn CK_ELIDE_LOCK_ADAPTIVE NAME ck_elide_stat_t * struct ck_elide_config * TYPE * Fn CK_ELIDE_UNLOCK_ADAPTIVE NAME ck_elide_stat_t * TYPE * Fn CK_ELIDE_LOCK NAME TYPE * Fn CK_ELIDE_UNLOCK NAME TYPE * Fn CK_ELIDE_TRYLOCK_PROTOTYPE NAME TYPE LOCK_PREDICATE TRYLOCK_FUNCTION</p>
<h2>DESCRIPTION</h2>
<p> These macros implement lock elision wrappers for a user-specified single-argument lock interface. The wrappers will attempt to elide lock acquisition, allowing concurrent execution of critical sections that do not issue conflicting memory operations. If any threads have successfully elided a lock acquisition, conflicting memory operations will roll-back any side-effects of the critical section and force every thread to retry the lock acquisition regularly. </p>
<p> Fn CK_ELIDE_LOCK , Fn CK_ELIDE_UNLOCK , Fn CK_ELIDE_LOCK_ADAPTIVE , and Fn CK_ELIDE_UNLOCK_ADAPTIVE macros require a previous Fn CK_ELIDE_PROTOTYPE with the same Fa NAME . Elision is attempted if the Fa LOCK_PREDICATE function returns false. If Fa LOCK_PREDICATE returns true then elision is aborted and Fa LOCK_FUNCTION is executed instead. If any threads are in an elided critical section, Fa LOCK_FUNCTION must force them to rollback through a conflicting memory operation. The Fa UNLOCK_PREDICATE function must return true if the lock is acquired by the caller, meaning that the lock was not successfully elided. If Fa UNLOCK_PREDICATE returns true, then the Fa UNLOCK_FUNCTION is executed. If RTM is unsupported (no CK_F_PR_RTM macro) then Fn CK_ELIDE_LOCK and Fn CK_ELIDE_LOCK_ADAPTIVE will immediately call Fn LOCK_FUNCTION . Fn CK_ELIDE_UNLOCK and Fn CK_ELIDE_UNLOCK_ADAPTIVE will immediately call Fn UNLOCK_FUNCTION . </p>
<p> Fn CK_ELIDE_TRYLOCK requires a previous Fn CK_ELIDE_TRYLOCK_PROTOTYPE with the same name. Elision is attempted if the Fa LOCK_PREDICATE function returns false. If Fa LOCK_PREDICATE returns true or if elision fails then the operation is aborted. If RTM is unsupported (no CK_F_PR_RTM macro) then Fn CK_ELIDE_TRYLOCK will immediately call Fn TRYLOCK_FUNCTION . </p>
<p> Fn CK_ELIDE_LOCK_ADAPTIVE and Fn CK_ELIDE_UNLOCK_ADAPTIVE will adapt the elision behavior associated with lock operations according to the run-time behavior of the program. This behavior is defined by the ck_elide_config structure pointer passed to Fn CK_ELIDE_LOCK_ADAPTIVE . A thread-local ck_elide_stat structure must be passed to both Fn CK_ELIDE_LOCK_ADAPTIVE and Fn CK_ELIDE_UNLOCK_ADAPTIVE . This structure is expected to be unique for different workloads, may not be re-used in recursive acquisitions and must match the lifetime of the lock it is associated with. It is safe to mix adaptive calls with best-effort calls. </p>
<p> Both ck_spinlock.h and ck_rwlock.h define ck_elide wrappers under the ck_spinlock and ck_rwlock namespace, respectively.</p>
<h2>EXAMPLES</h2>
<p> This example utilizes built-in lock elision facilities in ck_rwlock and ck_spinlock. </p>
<blockquote><p>
#include &lt;ck_rwlock.h&gt;<br />
#include &lt;ck_spinlock.h&gt;<br />
static ck_rwlock_t rw = CK_RWLOCK_INITIALIZER;<br />
static struct ck_elide_config rw_config =<br />
    CK_ELIDE_CONFIG_DEFAULT_INITIALIZER;<br />
static __thread ck_elide_stat_t rw_stat =<br />
    CK_ELIDE_STAT_INITIALIZER;<br />
static ck_spinlock_t spinlock = CK_SPINLOCK_INITIALIZER;<br />
static struct ck_elide_config spinlock_config =<br />
    CK_ELIDE_CONFIG_DEFAULT_INITIALIZER;<br />
static __thread ck_elide_stat_t spinlock_stat =<br />
    CK_ELIDE_STAT_INITIALIZER;<br />
void function(void)<br />
{<br />
    /* Lock-unlock write-side lock in weak best-effort manner. */<br />
    CK_ELIDE_LOCK(ck_rwlock_write, &amp;rw);<br />
    CK_ELIDE_UNLOCK(ck_rwlock_write, &amp;rw);<br />
    /* Attempt to acquire the write-side lock. */<br />
    if (CK_ELIDE_TRYLOCK(ck_rwlock_write, &amp;rw) == true)<br />
        CK_ELIDE_UNLOCK(ck_rwlock_write, &amp;rw);<br />
    /* Lock-unlock read-side lock in weak best-effort manner. */<br />
    CK_ELIDE_LOCK(ck_rwlock_read, &amp;rw);<br />
    CK_ELIDE_UNLOCK(ck_rwlock_read, &amp;rw);<br />
    /* Attempt to acquire the read-side lock. */<br />
    if (CK_ELIDE_TRYLOCK(ck_rwlock_read, &amp;rw) == true)<br />
        CK_ELIDE_UNLOCK(ck_rwlock_read, &amp;rw);<br />
    /* Lock-unlock write-side lock in an adaptive manner. */<br />
    CK_ELIDE_LOCK_ADAPTIVE(ck_rwlock_write, &amp;rw_stat,<br />
                           &amp;rw_config, &amp;rw);<br />
    CK_ELIDE_UNLOCK_ADAPTIVE(ck_rwlock_write, &amp;rw_stat,<br />
                             &amp;rw_config, &amp;rw);<br />
    /* Lock-unlock read-side lock in an adaptive manner. */<br />
    CK_ELIDE_LOCK_ADAPTIVE(ck_rwlock_read, &amp;rw_stat,<br />
                           &amp;rw_config, &amp;rw);<br />
    CK_ELIDE_UNLOCK_ADAPTIVE(ck_rwlock_read, &amp;rw_stat,<br />
                             &amp;rw_config, &amp;rw);<br />
    /* Lock-unlock spinlock in weak best-effort manner. */<br />
    CK_ELIDE_LOCK(ck_spinlock, &amp;spinlock);<br />
    CK_ELIDE_UNLOCK(ck_spinlock, &amp;spinlock);<br />
    /* Attempt to acquire the lock. */<br />
    if (CK_ELIDE_TRYLOCK(ck_spinlock, &amp;lock) == true)<br />
        CK_ELIDE_UNLOCK(ck_spinlock, &amp;spinlock);<br />
    /* Lock-unlock spinlock in an adaptive manner. */<br />
    CK_ELIDE_LOCK_ADAPTIVE(ck_spinlock, &amp;spinlock_stat,<br />
                           &amp;spinlock_config, &amp;spinlock);<br />
    CK_ELIDE_UNLOCK_ADAPTIVE(ck_spinlock, &amp;spinlock_stat,<br />
                             &amp;spinlock_config, &amp;spinlock);<br />
}
 </p></blockquote>
<p> In this example, user-defined locking functions are provided an elision implementation. </p>
<blockquote>
<pre><code>
/* Assume lock_t has been previously defined. */
#include &lt;ck_elide.h&gt;
/*
 * This function returns true if the lock is unavailable at the time
 * it was called or false if the lock is available.
 */
bool is_locked(lock_t *);
/*
 * This function acquires the supplied lock.
 */
void lock(lock_t *);
/*
 * This function releases the lock.
 */
void unlock(lock_t *);
CK_ELIDE_PROTOTYPE(my_lock, lock_t, is_locked, lock, is_locked, unlock)
static lock_t lock;
void function(void)
{
    CK_ELIDE_LOCK(my_lock, &amp;lock);
    CK_ELIDE_UNLOCK(my_lock, &amp;lock);
}
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> ck_rwlock3, ck_spinlock3 </p>
<p> Ravi Rajwar and James R. Goodman. 2001. Speculative lock elision: enabling highly concurrent multithreaded execution. In Proceedings of the 34th annual ACM/IEEE international symposium on Microarchitecture (MICRO 34). IEEE Computer Society, Washington, DC, USA, 294-305. </p>
<p> Additional information available at <a rel="nofollow" href="http://en.wikipedia.org/wiki/Transactional_Synchronization_Extensions">http://en.wikipedia.org/wiki/Transactional_Synchronization_Extensions</a> and <a href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
