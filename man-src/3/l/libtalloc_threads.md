---
title: "libtalloc_threads(3)"
name: "libtalloc_threads"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libtalloc_threads/"
description: "libtalloc_threads – Chapter 8: Using threads with talloc"
---

<h2 class="name">NAME</h2>
<p> libtalloc_threads &#8211; Chapter 8: Using threads with talloc</p>
<h2>and thread safety</h2>
<p> The talloc library is not internally thread-safe, in that accesses to variables on a talloc context are not controlled by mutexes or other thread-safe primitives. </p>
<p> However, so long as <code>talloc_disable_null_tracking()</code> is called from the main thread to disable global variable access within talloc, then each thread can safely use its own top level talloc context allocated off the NULL context. </p>
<p> For example: </p>
<pre><code>
static void *thread_fn(void *arg)
{
    const char *ctx_name = (const char *)arg;
    /*
     * Create a new top level talloc hierarchy in
     * this thread.
     */
    void *top_ctx = talloc_named_const(NULL, 0, "top");
    if (top_ctx == NULL) {
        return NULL;
    }
    sub_ctx = talloc_named_const(top_ctx, 100, ctx_name);
    if (sub_ctx == NULL) {
        return NULL;
    }
    /*
     * Do more processing/talloc calls on top_ctx
     * and its children.
     */
    ...... talloc_free(top_ctx);
    return value;
}
</code></pre>
<p> is a perfectly safe use of talloc within a thread. </p>
<p> The problem comes when one thread wishes to move some memory allocated on its local top level talloc context to another thread. Care must be taken to add data access exclusion to prevent memory corruption. One method would be to lock a mutex before any talloc call on each thread, but this would push the burden of total talloc thread-safety on the poor user of the library. </p>
<p> A much easier way to transfer talloced memory between threads is by the use of an intermediate, mutex locked, intermediate variable. </p>
<p> An example of this is below &#8211; taken from test code inside the talloc testsuite. </p>
<p> The main thread creates 1000 sub-threads, and then accepts the transfer of some thread-talloc&#8217;ed memory onto its top level context from each thread in turn. </p>
<p> A pthread mutex and condition variable are used to synchronize the transfer via the intermediate_ptr variable. </p>
<pre><code>
/* Required sync variables. */
static pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t condvar = PTHREAD_COND_INITIALIZER;
/* Intermediate talloc pointer for transfer. */
static void *intermediate_ptr;
/* Subthread. */
static void *thread_fn(void *arg)
{
    int ret;
    const char *ctx_name = (const char *)arg;
    void *sub_ctx = NULL;
    /*
     * Do stuff that creates a new talloc hierarchy in
     * this thread.
     */
    void *top_ctx = talloc_named_const(NULL, 0, "top");
    if (top_ctx == NULL) {
        return NULL;
    }
    sub_ctx = talloc_named_const(top_ctx, 100, ctx_name);
    if (sub_ctx == NULL) {
        return NULL;
    }
    /*
     * Now transfer a pointer from our hierarchy
     * onto the intermediate ptr.
     */
    ret = pthread_mutex_lock(&amp;mtx);
    if (ret != 0) {
        talloc_free(top_ctx);
        return NULL;
    }
    /* Wait for intermediate_ptr to be free. */
    while (intermediate_ptr != NULL) {
        ret = pthread_cond_wait(&amp;condvar, &amp;mtx);
        if (ret != 0) {
            talloc_free(top_ctx);
            return NULL;
        }
    }
    /* and move our memory onto it from our toplevel hierarchy. */
    intermediate_ptr = talloc_move(NULL, &amp;sub_ctx);
    /* Tell the main thread it's ready for pickup. */
    pthread_cond_broadcast(&amp;condvar);
    pthread_mutex_unlock(&amp;mtx);
    talloc_free(top_ctx);
    return NULL;
}
/* Main thread. */
#define NUM_THREADS 1000
static bool test_pthread_talloc_passing(void)
{
    int i;
    int ret;
    char str_array[NUM_THREADS][20];
    pthread_t thread_id;
    void *mem_ctx;
    /*
     * Important ! Null tracking breaks threaded talloc.
     * It *must* be turned off.
     */
    talloc_disable_null_tracking();
    /* Main thread toplevel context. */
    mem_ctx = talloc_named_const(NULL, 0, "toplevel");
    if (mem_ctx == NULL) {
        return false;
    }
    /*
     * Spin off NUM_THREADS threads.
     * They will use their own toplevel contexts.
     */
    for (i = 0; i &lt; NUM_THREADS; i++) {
        (void)snprintf(str_array[i],
                       20,
                       "thread:%d",
                       i);
        if (str_array[i] == NULL) {
            return false;
        }
        ret = pthread_create(&amp;thread_id,
                             NULL,
                             thread_fn,
                             str_array[i]);
        if (ret != 0) {
            return false;
        }
    }
    /* Now wait for NUM_THREADS transfers of the talloc'ed memory. */
    for (i = 0; i &lt; NUM_THREADS; i++) {
        ret = pthread_mutex_lock(&amp;mtx);
        if (ret != 0) {
            talloc_free(mem_ctx);
            return false;
        }
        /* Wait for intermediate_ptr to have our data. */
        while (intermediate_ptr == NULL) {
            ret = pthread_cond_wait(&amp;condvar, &amp;mtx);
            if (ret != 0) {
                talloc_free(mem_ctx);
                return false;
            }
        }
        /* and move it onto our toplevel hierarchy. */
        (void)talloc_move(mem_ctx, &amp;intermediate_ptr);
        /* Tell the sub-threads we're ready for another. */
        pthread_cond_broadcast(&amp;condvar);
        pthread_mutex_unlock(&amp;mtx);
    }
    /* Dump the hierarchy. */
    talloc_report(mem_ctx, stdout);
    talloc_free(mem_ctx);
    return true;
}
</code></pre>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
