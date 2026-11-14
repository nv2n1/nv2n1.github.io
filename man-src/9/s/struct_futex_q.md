---
title: "struct_futex_q(9)"
name: "struct_futex_q"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_futex_q/"
description: "struct_futex_q – The hashed futex queue entry, one per waiting task"
---

<p>struct_futex_q &#8211; The hashed futex queue entry, one per waiting task</p>
<h2>Synopsis</h2>
<pre><code>struct futex_q {
    struct plist_node list;
    struct task_struct *task;
    spinlock_t *lock_ptr;
    union futex_key key;
    struct futex_pi_state *pi_state;
    struct rt_mutex_waiter *rt_waiter;
    union futex_key *requeue_pi_key;
    u32 bitset;
};</code></pre>
<h2>Members</h2>
<p>list</p>
<dl>
<dd>priority-sorted list of tasks waiting on this futex</dl>
<p> task</p>
<dl>
<dd>the task waiting on the futex</dl>
<p> lock_ptr</p>
<dl>
<dd>the hash bucket lock</dl>
<p> key</p>
<dl>
<dd>the key the futex is hashed on</dl>
<p> pi_state</p>
<dl>
<dd>optional priority inheritance state</dl>
<p> rt_waiter</p>
<dl>
<dd>rt_waiter storage for use with requeue_pi</dl>
<p> requeue_pi_key</p>
<dl>
<dd>the requeue_pi target futex key</dl>
<p> bitset</p>
<dl>
<dd>bitset for the optional bitmasked wakeup</dl>
<h2>Description</h2>
<p>We use this hashed waitqueue, instead of a normal wait_queue_t, so we can wake only the relevant ones (hashed queues may be shared). </p>
<p> A futex_q has a woken state, just like tasks have TASK_RUNNING. It is considered woken when plist_node_empty(q-&gt;list) || q-&gt;lock_ptr == 0. The order of wakeup is always to make the first condition true, then the second. </p>
<p> PI futexes are typically woken before they are removed from the hash list via the rt_mutex code. See <code>unqueue_me_pi</code>.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
