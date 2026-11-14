---
title: "ck_rwlock(3)"
name: "ck_rwlock"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rwlock/"
description: "ck_rwlock_init ck_rwlock_write_lock ck_rwlock_write_unlock ck_rwlock_write_trylock ck_rwlock_write_downgrade ck_rwlock_locked_writer ck_rwlock_read_lock ck_rwlock_read_trylock ck_rwlock_read_unlock..."
---

<h2>NAME</h2>
<p> <code>ck_rwlock_init</code> <code>ck_rwlock_write_lock</code> <code>ck_rwlock_write_unlock</code> <code>ck_rwlock_write_trylock</code> <code>ck_rwlock_write_downgrade</code> <code>ck_rwlock_locked_writer</code> <code>ck_rwlock_read_lock</code> <code>ck_rwlock_read_trylock</code> <code>ck_rwlock_read_unlock</code> <code>ck_rwlock_locked_reader</code> <code>ck_rwlock_recursive_write_lock</code> <code>ck_rwlock_recursive_write_trylock</code> <code>ck_rwlock_recurisve_write_unlock</code> <code>ck_rwlock_recursive_read_lock</code> <code>ck_rwlock_recursive_read_trylock</code> <code>ck_rwlock_recursive_read_unlock</code> &#8211; centralized write-biased reader-writer locks</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_rwlock.h </p>
<p> <code>ck_rwlock_t lock = CK_RWLOCK_INITIALIZER;</code> </p>
<p> Ft void Fn ck_rwlock_init ck_rwlock_t *lock Ft void Fn ck_rwlock_write_lock ck_rwlock_t *lock Ft void Fn ck_rwlock_write_unlock ck_rwlock_t *lock Ft bool Fn ck_rwlock_write_trylock ck_rwlock_t *lock Ft bool Fn ck_rwlock_write_downgrade ck_rwlock_t *lock Ft bool Fn ck_rwlock_locked_writer ck_rwlock_t *lock Ft void Fn ck_rwlock_read_lock ck_rwlock_t *lock Ft bool Fn ck_rwlock_read_trylock ck_rwlock_t *lock Ft void Fn ck_rwlock_read_unlock ck_rwlock_t *lock Ft bool Fn ck_rwlock_locked_reader ck_rwlock_t *lock </p>
<p> <code>ck_rwlock_recursive_t lock = CK_RWLOCK_RECURSIVE_INITIALIZER;</code> </p>
<p> Ft void Fn ck_rwlock_recursive_write_lock ck_rwlock_recursive_t *lock unsigned int tid Ft bool Fn ck_rwlock_recursive_write_trylock ck_rwlock_recursive_t *lock unsigned int tid Ft void Fn ck_rwlock_recurisve_write_unlock ck_rwlock_recursive_t *lock Ft void Fn ck_rwlock_recursive_read_lock ck_rwlock_recursive_t *lock Ft bool Fn ck_rwlock_recursive_read_trylock ck_rwlock_recursive_t *lock Ft void Fn ck_rwlock_recursive_read_unlock ck_rwlock_recursive_t *lock</p>
<h2>DESCRIPTION</h2>
<p> This is a centralized write-biased reader-writer lock. It requires very little space overhead and has a low latency fast path. Write-side recursion requires usage of ck_rwlock_recursive. Read-side recursion is disallowed. The Fn ck_rwlock_write_downgrade function degrades the caller&#8217;s write-side acquisition to a read-side acquisition without forfeit of current critical section.</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_rwlock.h&gt;
static ck_rwlock_t lock = CK_RWLOCK_INITIALIZER;
static void
reader(void)
{
    for (;;) {
        ck_rwlock_read_lock(&amp;lock);
        /* Read-side critical section. */
        ck_rwlock_read_unlock(&amp;lock);
        if (ck_rwlock_read_trylock(&amp;lock) == true) {
            /* Read-side critical section. */
            ck_rwlock_read_unlock(&amp;lock);
        }
    }
    return;
}
static void
writer(void)
{
    for (;;) {
        ck_rwlock_write_lock(&amp;lock);
        /* Write-side critical section. */
        ck_rwlock_write_unlock(&amp;lock);
        if (ck_rwlock_write_trylock(&amp;lock, 1) == true) {
            /* Write-side critical section. */
            ck_rwlock_write_unlock(&amp;lock);
        }
    }
    return;
}
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> ck_brlock3, ck_elide3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
