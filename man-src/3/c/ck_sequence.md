---
title: "ck_sequence(3)"
name: "ck_sequence"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_sequence/"
description: "ck_sequence_init ck_sequence_read_begin ck_sequence_read_retry ck_sequence_write_begin ck_sequence_write_end – sequence locks"
---

<h2>NAME</h2>
<p> <code>ck_sequence_init</code> <code>ck_sequence_read_begin</code> <code>ck_sequence_read_retry</code> <code>ck_sequence_write_begin</code> <code>ck_sequence_write_end</code> &#8211; sequence locks</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_sequence.h </p>
<p> <code>ck_sequence_t seqlock = CK_SEQUENCE_INITIALIZER;</code> </p>
<p> Ft void Fn ck_sequence_init ck_sequence_t *sq Ft unsigned int Fn ck_sequence_read_begin const ck_sequence_t *sq Ft bool Fn ck_sequence_read_retry const ck_sequence_t *sq unsigned int version Ft void Fn ck_sequence_write_begin ck_sequence_t *sq Ft void Fn ck_sequence_write_end ck_sequence_t *sq</p>
<h2>DESCRIPTION</h2>
<p> It is recommended to use ck_sequence when a small amount of data that cannot be accessed atomically has to be synchronized with readers in a fashion that does not block any writer. Readers are able to execute their read-side critical sections without any atomic operations. A ck_sequence_t must be initialized before use. It may be initialized using either a static initializer (CK_SEQUENCE_INITIALIZER) or using Fn ck_sequence_init . Before readers attempt to read data that may be concurrently modified they must first save the return value of Fn ck_sequence_read_begin . While or after a reader has completed copying the data associated with a ck_sequence_t it must pass the earlier return value of Fn ck_sequence_read_begin to Fn ck_sequence_read_retry. If Fn ck_sequence_read_retry returns true then the copy of data may be inconsistent and the read process must be retried. Writers must rely on their own synchronization primitives. Once a writer has entered its respective critical section, it must call Fn ck_sequence_write_begin to signal intent to update the data protected by the ck_sequence_t. Before the writer leaves its critical section it must execute Fn ck_sequence_write_end to indicate that the updates have left respective objects in a consistent state.</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_sequence.h&gt;
#include &lt;stdlib.h&gt;
static struct example {
    int a;
    int b;
    int c;
} global;
static ck_sequence_t seqlock = CK_SEQUENCE_INITIALIZER;
void reader(void)
{
    struct example copy;
    unsigned int version;
    /*
     * Attempt a read of the data structure. If the structure
     * has been modified between ck_sequence_read_begin and
     * ck_sequence_read_retry then attempt another read since
     * the data may be in an inconsistent state.
     */
    do {
        version = ck_sequence_read_begin(&amp;seqlock);
        copy = global;
    } while (ck_sequence_read_retry(&amp;seqlock, version));
    /*
     * The previous may also be expressed using CK_SEQUENCE_READ.
     * Generally recommend to only use ck_sequence_read_retry
     * if you would like to detect a conflicting write at some
     * higher granularity.
     */
    CK_SEQUENCE_READ(&amp;seqlock, &amp;version)
    {
        copy = global;
    }
    return;
}
void writer(void)
{
    for (;;) {
        ck_sequence_write_begin(&amp;seqlock);
        global.a = rand();
        global.b = global.a + global.b;
        global.c = global.b + global.c;
        ck_sequence_write_end(&amp;seqlock);
    }
    return;
}
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> ck_brlock3, ck_bytelock3, ck_rwlock3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
