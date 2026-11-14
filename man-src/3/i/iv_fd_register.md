---
title: "iv_fd_register(3)"
name: "iv_fd_register"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_fd_register/"
description: "iv_fd_register, iv_fd_register_try, iv_fd_unregister, iv_fd_registered, iv_fd_set_handler_in, iv_fd_set_handler_err, iv_fd_set_handler_out – deal with ivykis file descriptors"
---

<h2>NAME</h2>
<p> iv_fd_register, iv_fd_register_try, iv_fd_unregister, iv_fd_registered, iv_fd_set_handler_in, iv_fd_set_handler_err, iv_fd_set_handler_out &#8211; deal with ivykis file descriptors</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;iv.h&gt;</code> </p>
<pre><code>
struct iv_fd {
    int fd;
    void *cookie;
    void (*handler_in)(void *);
    void (*handler_out)(void *);
    void (*handler_err)(void *);
};
</code></pre>
<p> <code>void IV_FD_INIT(struct iv_fd *</code><i>fd</i><code>);</code><br />
 <code>void iv_fd_register(struct iv_fd *</code><i>fd</i><code>);</code><br />
 <code>int iv_fd_register_try(struct iv_fd *</code><i>fd</i><code>);</code><br />
 <code>void iv_fd_unregister(struct iv_fd *</code><i>fd</i><code>);</code><br />
 <code>int iv_fd_registered(struct iv_fd *</code><i>fd</i><code>);</code><br />
 <code>void iv_fd_set_handler_in(struct iv_fd *</code><i>fd</i><code>, void (*</code><i>handler</i><code>)(void *));</code><br />
 <code>void iv_fd_set_handler_out(struct iv_fd *</code><i>fd</i><code>, void (*</code><i>handler</i><code>)(void *));</code><br />
 <code>void iv_fd_set_handler_err(struct iv_fd *</code><i>fd</i><code>, void (*</code><i>handler</i><code>)(void *));</code> </p>
<h2>DESCRIPTION</h2>
<p> The functions <code>iv_fd_register</code> and <code>iv_fd_unregister</code> register, respectively unregister, a file descriptor with the current thread&#8217;s ivykis event loop. Calling <code>iv_fd_registered</code> on a file descriptor returns true if that file descriptor is currently registered with ivykis. </p>
<p> When a file descriptor that is registered with ivykis becomes ready for input or output, or an error condition occurs on that file descriptor, and a callback function for that event has been specified, that callback function will be called in the thread that the file descriptor was registered in. </p>
<p> And conversely, when a file descriptor that is already ready for input or output or already has an error condition set is registered with ivykis, and the corresponding callback function pointer is not NULL, the callback function will be called in the next iteration of the current thread&#8217;s ivykis event loop. </p>
<p> Before a file descriptor is registered, it must have been initialised by calling <code>IV_FD_INIT</code> on it, and must have had its <code>-&gt;fd</code> member field set to a valid OS file descriptor. The <code>-&gt;handler_in, -&gt;handler_out</code> and <code>-&gt;handler_err</code> member fields point to callback functions that are to be called when the specified file descriptor becomes ready for input or output or an error condition occurs. If any handler function is set to <code>NULL,</code> it indicates that the application is not interested in being notified of the corresponding event. </p>
<p> An application is not allowed to change the <code>-&gt;fd</code> member while a file descriptor is registered. </p>
<p> <code>iv_fd_set_handler_in</code> changes the callback function to be called when descriptor <code>fd</code> becomes ready for input. An application is not allowed to directly change the <code>-&gt;handler_in</code> member after the file descriptor has been registered, this function has to be used instead. Conversely, it is not allowed to use this function before the file descriptor has been registered. </p>
<p> <code>iv_fd_set_handler_out</code> is analogous to <code>iv_fd_set_handler_in,</code> only it deals with the callback function for output readiness <code>(-&gt;handler_out).</code> </p>
<p> <code>iv_fd_set_handler_err</code> is analogous to <code>iv_fd_set_handler_in</code> and <code>iv_fd_set_handler_out,</code> only it deals with the callback function for error conditions <code>(-&gt;handler_err).</code> </p>
<p> When a handler function was NULL, and was set to a non-NULL value by calling <code>iv_fd_set_handler_in, iv_fd_set_handler_out</code> or <code>iv_fd_set_handler_err,</code> and the file descriptor was already ready for input or output, or already had an error condition set, an event is generated, and the specified callback function will be called in the next iteration of the current thread&#8217;s event loop. The application does not need to poll the file descriptor to see if a condition was already raised. </p>
<p> Callback functions are passed a <code>cookie</code> value as their first and sole argument. If the application wishes to use this facility for transferring data to the callback function, it should set the <code>-&gt;cookie</code> member of a file descriptor to a value of type <code>void *.</code> This value can be modified directly by the application at any time without calling a helper function. </p>
<p> When a file descriptor is registered with ivykis, it is transparently set to nonblocking mode, and configured to be closed on <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3). </p>
<p> An application is allowed to unregister a file descriptor from within any callback function, including callback functions triggered by that file descriptor itself, and even to free the memory corresponding to that file descriptor from any callback function, but a <code>struct iv_fd</code> can only be unregistered in the thread that it was registered from. </p>
<p> It is allowed to register the same underlying OS file descriptor in multiple threads, but a given <code>struct iv_fd</code> can only be registered in one thread at a time. </p>
<p> <code>iv_fd_register</code> does not return errors to the caller, and in case of an error while registering the file descriptor, for example if it isn&#8217;t open or is unpollable, <code><a href="/docs/linux/man/3-abort/">abort</a></code>(3) will be invoked. If it is not known whether registering the file descriptor with the kernel will be successful or not, use <code>iv_fd_register_try</code> instead, which is a variant on <code>iv_fd_register</code> which returns a nonzero value in case of a registration error. Since <code>iv_fd_register_try</code> disables various internal optimisations, it is recommended to use <code>iv_fd_register</code> whenever possible. </p>
<p> See <code><a href="/docs/linux/man/3-iv_examples/">iv_examples</a></code>(3) for programming examples.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_examples/">iv_examples</a></code>(3) </p>
<h2>Index</h2>
