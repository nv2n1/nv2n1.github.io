---
title: "ck_brlock(3)"
name: "ck_brlock"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_brlock/"
description: "ck_brlock_init ck_brlock_write_lock ck_brlock_write_unlock ck_brlock_write_trylock ck_brlock_read_register ck_brlock_read_unregister ck_brlock_read_lock ck_brlock_read_trylock ck_brlock_read_unlock..."
---

<h2>NAME</h2>
<p> <code>ck_brlock_init</code> <code>ck_brlock_write_lock</code> <code>ck_brlock_write_unlock</code> <code>ck_brlock_write_trylock</code> <code>ck_brlock_read_register</code> <code>ck_brlock_read_unregister</code> <code>ck_brlock_read_lock</code> <code>ck_brlock_read_trylock</code> <code>ck_brlock_read_unlock</code> &#8211; big-reader locks</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_brlock.h </p>
<p> <code>ck_brlock_t brlock = CK_BRLOCK_INITIALIZER;</code> </p>
<p> <code>ck_brlock_reader_t reader = CK_BRLOCK_READER_INITIALIZER;</code> </p>
<p> Ft void Fn ck_brlock_init ck_brlock_t *br Ft void Fn ck_brlock_write_lock ck_brlock_t *br Ft void Fn ck_brlock_write_unlock ck_brlock_t *br Ft bool Fn ck_brlock_write_trylock ck_brlock_t *br unsigned int factor Ft void Fn ck_brlock_read_register ck_brlock_t *br ck_brlock_reader_t *reader Ft void Fn ck_brlock_read_unregister ck_brlock_t *br ck_brlock_reader_t *reader Ft void Fn ck_brlock_read_lock ck_brlock_t *br ck_brlock_reader_t *reader Ft bool Fn ck_brlock_read_trylock ck_brlock_t *br ck_brlock_reader_t *reader unsigned int factor Ft void Fn ck_brlock_read_unlock ck_brlock_reader_t *reader</p>
<h2>DESCRIPTION</h2>
<p> Big reader locks are distributed reader-writer locks with low latency constant time reader acquisition (with respect to number of concurrent readers). On the other hand, writer acquisitions are a relatively expensive <a href="/docs/linux/man/n-o/">O</a>(n) operation. This is a write-biased lock.</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
static ck_brlock_t lock = CK_BRLOCK_INITIALIZER;
static __thread ck_brlock_reader_t reader;
static void
reader(void)
{
    /* Add our thread as a lock participant. */
    ck_brlock_read_register(&amp;lock, &amp;reader);
    for (;;) {
        ck_brlock_read_lock(&amp;lock, &amp;reader);
        /* Read-side critical section. */
        ck_brlock_read_unlock(&amp;reader);
        if (ck_brlock_read_trylock(&amp;lock, &amp;reader, 1) == true) {
            /* Read-side critical section. */
            ck_brlock_read_unlock(&amp;reader);
        }
    }
    return;
}
static void
writer(void)
{
    for (;;) {
        ck_brlock_write_lock(&amp;lock);
        /* Write-side critical section. */
        ck_brlock_write_unlock(&amp;lock);
        if (ck_brlock_write_trylock(&amp;lock, 1) == true) {
            /* Write-side critical section. */
            ck_brlock_write_unlock(&amp;lock);
        }
    }
    return;
}
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> ck_bytelock3, ck_rwlock3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
