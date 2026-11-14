---
title: "ck_swlock(3)"
name: "ck_swlock"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_swlock/"
description: "ck_swlock_init ck_swlock_write_latch ck_swlock_write_unlatch ck_swlock_write_lock ck_swlock_write_unlock ck_swlock_write_trylock ck_swlock_write_downgrade ck_swlock_locked_writer ck_swlock_read_loc..."
---

<h2>NAME</h2>
<p> <code>ck_swlock_init</code> <code>ck_swlock_write_latch</code> <code>ck_swlock_write_unlatch</code> <code>ck_swlock_write_lock</code> <code>ck_swlock_write_unlock</code> <code>ck_swlock_write_trylock</code> <code>ck_swlock_write_downgrade</code> <code>ck_swlock_locked_writer</code> <code>ck_swlock_read_lock</code> <code>ck_swlock_read_trylock</code> <code>ck_swlock_read_unlock</code> <code>ck_swlock_locked_reader</code> &#8211; centralized copy-safe write-biased single-writer read-write locks</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_swlock.h </p>
<p> <code>ck_swlock_t lock = CK_SWLOCK_INITIALIZER;</code> </p>
<p> Ft void Fn ck_swlock_init ck_swlock_t *lock Ft void Fn ck_swlock_write_lock ck_swlock_t *lock Ft void Fn ck_swlock_write_unlock ck_swlock_t *lock Ft void Fn ck_swlatch_write_latch ck_swlatch_t *latch Ft void Fn ck_swlatch_write_unlatch ck_swlatch_t *latch Ft bool Fn ck_swlock_write_trylock ck_swlock_t *lock Ft bool Fn ck_swlock_write_downgrade ck_swlock_t *lock Ft bool Fn ck_swlock_locked_writer ck_swlock_t *lock Ft void Fn ck_swlock_read_lock ck_swlock_t *lock Ft bool Fn ck_swlock_read_trylock ck_swlock_t *lock Ft void Fn ck_swlock_read_unlock ck_swlock_t *lock Ft bool Fn ck_swlock_locked_reader ck_swlock_t *lock</p>
<h2>DESCRIPTION</h2>
<p> This is a centralized write-biased single-writer reader-writer lock. It requires half the space that ck_rwlock does and has a low latency fast path. The lock supports latch and unlatch operations that allow it to be used in a copy-safe manner (reader-bits may be over-written safely).</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_swlock.h&gt;
static ck_swlock_t lock = CK_SWLOCK_INITIALIZER;
static void
reader(void)
{
    for (;;) {
        ck_swlock_read_lock(&amp;lock);
        /* Read-side critical section. */
        ck_swlock_read_unlock(&amp;lock);
        if (ck_swlock_read_trylock(&amp;lock) == true) {
            /* Read-side critical section. */
            ck_swlock_read_unlock(&amp;lock);
        }
    }
    return;
}
static void
writer(void)
{
    ck_swlock_t contrived;
    for (;;) {
        ck_swlock_write_lock(&amp;lock);
        /* Write-side critical section. */
        ck_swlock_write_unlock(&amp;lock);
        if (ck_swlock_write_trylock(&amp;lock) == true) {
            /* Write-side critical section. */
            ck_swlock_write_unlock(&amp;lock);
        }
        ck_swlock_write_latch(&amp;lock);
        /* Write-side critical section. */
        /* This is safe to do with-in a latch. */
        contrived = lock;
        lock = contrived;
        ck_swlock_write_unlatch(&amp;lock);
    }
    return;
}
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> ck_brlock3, ck_elide3, ck_pflock3, ck_rwlock3, ck_tflock3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
