---
title: "ck_tflock(3)"
name: "ck_tflock"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_tflock/"
description: "ck_tflock_ticket_init ck_tflock_ticket_write_lock ck_tflock_ticket_write_unlock ck_tflock_ticket_read_lock ck_tflock_ticket_read_unlock – centralized task-fair reader-writer locks"
---

<h2>NAME</h2>
<p> <code>ck_tflock_ticket_init</code> <code>ck_tflock_ticket_write_lock</code> <code>ck_tflock_ticket_write_unlock</code> <code>ck_tflock_ticket_read_lock</code> <code>ck_tflock_ticket_read_unlock</code> &#8211; centralized task-fair reader-writer locks</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_tflock.h </p>
<p> <code>ck_tflock_ticket_t lock = CK_TFLOCK_TICKET_INITIALIZER;</code> </p>
<p> Ft void Fn ck_tflock_ticket_init ck_tflock_ticket_t *lock Ft void Fn ck_tflock_ticket_write_lock ck_tflock_ticket_t *lock Ft void Fn ck_tflock_ticket_write_unlock ck_tflock_ticket_t *lock Ft void Fn ck_tflock_ticket_read_lock ck_tflock_ticket_t *lock Ft void Fn ck_tflock_ticket_read_unlock ck_tflock_ticket_t *lock</p>
<h2>DESCRIPTION</h2>
<p> This is a centralized task-fair reader-writer lock. It requires little space overhead and has a low latency fast path.</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_tflock.h&gt;
static ck_tflock_ticket_t lock = CK_TFLOCK_INITIALIZER;
static void
reader(void)
{
    for (;;) {
        ck_tflock_ticket_read_lock(&amp;lock);
        /* Read-side critical section. */
        ck_tflock_ticket_read_unlock(&amp;lock);
    }
    return;
}
static void
writer(void)
{
    for (;;) {
        ck_tflock_ticket_write_lock(&amp;lock);
        /* Write-side critical section. */
        ck_tflock_ticket_write_unlock(&amp;lock);
    }
    return;
}
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> ck_brlock3, ck_rwlock3, ck_pflock3, ck_swlock3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
