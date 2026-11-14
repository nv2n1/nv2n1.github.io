---
title: "stdatomic_thread_fence(3)"
name: "stdatomic_thread_fence"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_thread_fence/"
---

std::atomic_thread_fence - std::atomic_thread_fence

<h2>Synopsis</h2>

Defined in header &lt;atomic&gt; 
extern &quot;C&quot; void atomic_thread_fence( std::memory_order order ) noexcept; <i>(since C++11)</i> 
Establishes memory_synchronization_ordering of non-atomic and relaxed atomic accesses, as instructed by order, without an associated atomic operation. 
Fence-atomic synchronization 
A release fence F in thread A synchronizes-with atomic acquire_operation Y in thread B, if 
* there exists an atomic store X (with any memory order) 
* Y reads the value written by X (or the value would be written by release_sequence_headed_by_X if X were a release operation) 
* F is sequenced-before X in thread A 
In this case, all non-atomic and relaxed atomic stores that are sequenced-before F in thread A will happen-before all non-atomic and relaxed atomic loads from the same locations made in thread B after Y. 
Atomic-fence synchronization 
An atomic release_operation X in thread A synchronizes-with an acquire fence F in thread B, if 
* there exists an atomic read Y (with any memory order) 
* Y reads the value written by X (or by the release_sequence_headed_by_X) 
* Y is sequenced-before F in thread B 
In this case, all non-atomic and relaxed atomic stores that are sequenced-before X in thread A will happen-before all non-atomic and relaxed atomic loads from the same locations made in thread B after F. 
Fence-fence synchronization 
A release fence FA in thread A synchronizes-with an acquire fence FB in thread B, if 
* There exists an atomic object M, 
* There exists an atomic write X (with any memory order) that modifies M in thread A 
* FA is sequenced-before X in thread A 
* There exists an atomic read Y (with any memory order) in thread B 
* Y reads the value written by X (or the value would be written by release_sequence_headed_by_X if X were a release operation) 
* Y is sequenced-before FB in thread B 
In this case, all non-atomic and relaxed atomic stores that are sequenced-before FA in thread A will happen-before all non-atomic and relaxed atomic loads from the same locations made in thread B after FB 

<h2>Parameters</h2>

order - the memory ordering executed by this fence

<h2>Return value</h2>

<i>(none)</i> 

<h2>Notes</h2>

atomic_thread_fence imposes stronger synchronization constraints than an atomic store operation with the same std::memory_order. While an atomic store-release operation prevents all preceding writes from moving past the store-release, an atomic_thread_fence with memory_order_release ordering prevents all preceding writes from moving past all subsequent stores. 
Fence-fence synchronization can be used to add synchronization to a sequence of several relaxed atomic operations, for example <pre><code>// Global

std::string computation(int);

void print(std::string);
std::atomic&lt;int&gt; arr[3] = {-1, -1, -1};

std::string data[1000] // non-atomic data
    // Thread A, compute 3 values

    void
    ThreadA(int v0, int v1, int v2)

{

    // assert( 0 &lt;= v0, v1, v2 &lt; 1000 );

    data[v0] = computation(v0);

    data[v1] = computation(v1);

    data[v2] = computation(v2);

    std::atomic_thread_fence(std::memory_order_release);

    std::atomic_store_explicit(&amp;arr[0], v0, std::memory_order_relaxed);

    std::atomic_store_explicit(&amp;arr[1], v1, std::memory_order_relaxed);

    std::atomic_store_explicit(&amp;arr[2], v2, std::memory_order_relaxed);
}
// Thread B, prints between 0 and 3 values already computed.

void ThreadB()

{

    int v0 = std::atomic_load_explicit(&amp;arr[0], std::memory_order_relaxed);

    int v1 = std::atomic_load_explicit(&amp;arr[1], std::memory_order_relaxed);

    int v2 = std::atomic_load_explicit(&amp;arr[2], std::memory_order_relaxed);

    std::atomic_thread_fence(std::memory_order_acquire);

    // v0, v1, v2 might turn out to be -1, some or all of them.

    // otherwise it is safe to read the non-atomic data because of the fences:

    if (v0 != -1) {
        print(data[v0]);
    }

    if (v1 != -1) {
        print(data[v1]);
    }

    if (v2 != -1) {
        print(data[v2]);
    }
}
</code></pre>

<h2>Examples</h2>

Scan an array of mailboxes, and process only the ones intended for us, without unnecessary synchronization. This example uses atomic-fence synchronization. 
 // Run this code <pre><code>const int num_mailboxes = 32;

std::atomic&lt;int&gt; mailbox_receiver[num_mailboxes];

std::string mailbox_data[num_mailboxes];
// The writer threads update non-atomic shared data

// and then update mailbox_receiver[i] as follows

mailbox_data[i] = ...;

std::atomic_store_explicit(&amp;mailbox_receiver[i], receiver_id, std::memory_order_release);
// Reader thread needs to check all mailbox[i], but only needs to sync with one

for (int i = 0; i &lt; num_mailboxes; ++i) {
    if (std::atomic_load_explicit(&amp;mailbox_receiver[i], std::memory_order_relaxed) == my_id) {
        std::atomic_thread_fence(std::memory_order_acquire); // synchronize with just one writer
        do_work(mailbox_data[i]);                            // guaranteed to observe everything done in the writer thread before
                                                             // the atomic_store_explicit()
    }
}
</code></pre>

<h2>See also</h2>

memory_order defines memory ordering constraints for the given atomic operation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
<i>(C++11)</i> 
atomic_signal_fence fence between a thread and a signal handler executed in the same thread 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
