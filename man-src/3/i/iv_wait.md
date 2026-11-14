---
title: "iv_wait(3)"
name: "iv_wait"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_wait/"
description: "IV_WAIT_INTEREST_INIT, iv_wait_interest_register, iv_wait_interest_register_spawn, iv_wait_interest_unregister, iv_wait_interest_kill – ivykis wait4(2) wrapper"
---

<h2>NAME</h2>
<p> IV_WAIT_INTEREST_INIT, iv_wait_interest_register, iv_wait_interest_register_spawn, iv_wait_interest_unregister, iv_wait_interest_kill &#8211; ivykis <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2) wrapper</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;iv_wait.h&gt;</code> </p>
<pre><code>
struct iv_wait_interest {
    pid_t pid;
    void *cookie;
    void (*handler)(void *cookie, int status,
                    struct rusage *rusage);
};
</code></pre>
<p> <code>void IV_WAIT_INTEREST_INIT(struct iv_wait_interest *</code><i>this</i><code>);</code><br />
 <code>int iv_wait_interest_register(struct iv_wait_interest *</code><i>this</i><code>);</code><br />
 <code>int iv_wait_interest_register_spawn(struct iv_wait_interest *</code><i>this</i><code>, void (*</code><i>fn</i><code>)(void *), void *</code><i>cookie</i><code>);</code><br />
 <code>void iv_wait_interest_unregister(struct iv_wait_interest *</code><i>this</i><code>);</code><br />
 <code>int iv_wait_interest_kill(struct iv_wait_interest *</code><i>this</i><code>, int </code><i>sig</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>iv_wait</code> is an <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3) wrapper around <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2), integrating process state change notification with the ivykis event loop. </p>
<p> An ivykis application desiring process state change notifications registers a <code>struct iv_wait_interest</code> object by calling <code>iv_wait_interest_register,</code> after having initialised it with <code>IV_WAIT_INTEREST_INIT</code> and subsequently having filled in the <code>-&gt;pid,</code> <code>-&gt;cookie</code> and <code>-&gt;handler</code> members. </p>
<p> Alternatively, an ivykis application can use <code>iv_wait_interest_register_spawn</code> to atomically fork off a child process and register a <code>struct iv_wait_interest</code> for it. In this context, &#8216;atomically&#8217; means that the call to <code>iv_wait_interest_register_spawn</code> will be serialised with respect to invocations of <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2), which closes the race where process state change notifications can occur and be delivered between forking off the child process and registering a <code>struct iv_wait_interest</code> for the child&#8217;s pid. The child process will run the function given by the <code>iv_wait_interest_register_spawn</code> argument <code>fn,</code> with argument <code>cookie</code> as its argument. </p>
<p> Once a process state change occurs (as indicated by delivery of a SIGCHLD signal to the current process), <code>iv_wait</code> calls <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2) to return information about the process state change, looks up the returned process ID in the set of registered <code>struct iv_wait_interest</code> objects, and if there is a registered interest with a matching <code>-&gt;pid</code> field, arranges for that object&#8217;s callback function to be called in the thread that the object was registered in. </p>
<p> Process state change notifications will continue to be delivered to the object&#8217;s callback function until <code>iv_wait_interest_unregister</code> is called on the object or until a WIFEXITED or WIFSIGNALED status for this pid is returned by <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2). </p>
<p> Delivery of a WIFEXITED or WIFSIGNALED status does not automatically unregister the object, this always needs to be done explicitly. </p>
<p> Unregistering a <code>struct iv_wait_interest</code> object can only be done from the thread that that object was registered in, but within that thread, can safely be done from (and its underlying memory allocation can safely be freed from) its own callback function. </p>
<p> Registering multiple <code>struct iv_wait_interest</code> objects for the same process ID will produce undefined behavior. </p>
<p> To send a signal to a child process, use <code>iv_wait_interest_kill.</code> This function will internally serialise with invocations of <code><a href="/docs/linux/man/2-wait4/">wait4</a>(2),</code> to avoid the race between sending a signal to a process and collecting a termination notification for that process (which makes its pid available for reuse). </p>
<p> Internally, <code>iv_wait</code> is implemented using <code><a href="/docs/linux/man/3-iv_signal/">iv_signal</a></code>(3) and <code><a href="/docs/linux/man/3-iv_event/">iv_event</a></code>(3). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_signal/">iv_signal</a></code>(3), <code><a href="/docs/linux/man/3-iv_event/">iv_event</a></code>(3), <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2) </p>
<h2>Index</h2>
