---
title: "iv_work_item_init(3)"
name: "iv_work_item_init"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_work_item_init/"
description: "IV_WORK_POOL_INIT, iv_work_pool_create, iv_work_pool_put, IV_WORK_ITEM_INIT, iv_work_pool_submit_work – ivykis worker thread management"
---

<p>IV_WORK_POOL_INIT, iv_work_pool_create, iv_work_pool_put, IV_WORK_ITEM_INIT, iv_work_pool_submit_work &#8211; ivykis worker thread management</p>
<h2>Synopsis</h2>
<p><code>#include &lt;iv_work.h&gt;</code> </p>
<pre>struct iv_work_pool {
 int max_threads;
 void *cookie;
 void (*thread_start)(void *cookie);
 void (*thread_stop)(void *cookie);
};
struct iv_work_item {
 void *cookie;
 void (*work)(void *cookie);
 void (*completion)(void *cookie);
};</pre>
<p><code>void IV_WORK_POOL_INIT(struct iv_work_pool *</code><i>this</i><code>);</code><br />
 <code>int iv_work_pool_create(struct iv_work_pool *</code><i>this</i><code>);</code><br />
 <code>int iv_work_pool_put(struct iv_work_pool *</code><i>this</i><code>);</code><br />
 <code>void IV_WORK_ITEM_INIT(struct iv_work_item *</code><i>work</i><code>);</code><br />
 <code>int iv_work_pool_submit_work(struct iv_work_pool *</code><i>this</i><code>, struct iv_work_item *</code><i>work</i><code>);</code> </p>
<h2>Description</h2>
<p>Calling <code>iv_work_pool_create</code> on a <code>struct iv_work_pool</code> object previously initialised by <code>IV_WORK_POOL_INIT</code> creates a pool of worker threads that can be used to offload CPU intensive tasks to, so as to prevent negatively influencing event handling latency in the calling thread, and to enable the use of multiple host CPUs for CPU intensive tasks. </p>
<p> <code>iv_work</code> dynamically adjusts the number of threads in the pool to the amount of work there is to do. The <code>-&gt;max_threads</code> member of <code>struct iv_work_pool</code> specifies the maximum number of threads that will be created in this pool. </p>
<p> Calling <code>iv_work_pool_submit_work</code> on a <code>struct iv_work_item</code> object previously initialised by <code>IV_WORK_ITEM_INIT</code> submits a work item to a pool. The <code>-&gt;work</code> member of <code>struct iv_work_item</code> specifies the function that will be called in one of the worker threads in the pool specified by <code>-&gt;this,</code> with <code>-&gt;cookie</code> as its sole argument. When the work function has completed, <code>iv_work</code> will call the <code>-&gt;completion</code> callback to indicate this, also with <code>-&gt;cookie</code> as its sole argument, in the thread that <code>iv_work_pool_create</code> was called in for this pool object. </p>
<p> As a special case, calling <code>iv_work_pool_submit_work</code> with a <code>NULL</code> work pool pointer will cause the work item to be processed in the local thread, from an <code><a href="/docs/linux/man/3-iv_task/">iv_task</a></code>(3) callback. </p>
<p> If the <code>-&gt;thread_start</code> function pointer specified in <code>struct iv_work_pool</code> is not NULL, it will be called upon creation of a new worker thread, in the context of the created worker thread, with <code>-&gt;cookie</code> as its sole argument. Calls to <code>-&gt;thread_start</code> are not explicitly serialised, which should be kept in mind when manipulating state shared between threads from within that callback function. </p>
<p> Similarly, if <code>iv_work</code> decides to terminate a worker thread, for example due to inactivity, <code>-&gt;thread_stop</code> will be called in the context of the terminating thread, with <code>-&gt;cookie</code> as its sole argument. Calls to <code>-&gt;thread_stop</code> are also not explicitly serialised. </p>
<p> <code>iv_work_pool_submit_work</code> can only be called from the thread that <code>iv_work_pool_create</code> for this pool object was called in. </p>
<p> There is no way to cancel submitted work items. </p>
<p> There is no guaranteed order, FIFO or otherwise, between different work items submitted to the same worker thread pool. </p>
<p> When the user has no more work items to submit to the pool, its reference to the pool can be dropped by calling <code>iv_work_pool_put.</code> </p>
<p> If there are still pending or running work items assigned to this pool when <code>iv_work_pool_put</code> is called, those work items will not be canceled, but will be allowed to run to completion, and their <code>-&gt;completion</code> callbacks will be called as usual. A similar thing holds for the <code>-&gt;thread_start</code> and <code>-&gt;thread_stop</code> callbacks &#8212; they can also still be called after <code>iv_work_pool_put</code> returns. Even so, the memory corresponding to the <code>struct iv_work_pool</code> can immediately be freed or reused by the user upon return of the <code>iv_work_pool_put</code> call. </p>
<p> Internally, <code>iv_work</code> uses <code><a href="/docs/linux/man/3-iv_thread/">iv_thread</a></code>(3) for its thread management. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_thread/">iv_thread</a></code>(3)</p>
