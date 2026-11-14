---
title: "globus_callback_signal(3)"
name: "globus_callback_signal"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_callback_signal/"
description: "Globus Callback Signal Handling –"
---

<h2 class="name">NAME</h2>
<p> Globus Callback Signal Handling &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_SIGNAL_INTERRUPT</code> </p>
<h3>Functions</h3>
<p> <code>globus_result_t</code> <code>globus_callback_space_register_signal_handler</code> (int signum, <code>globus_bool_t</code> persist, <code>globus_callback_func_t</code> callback_func, void *callback_user_arg, <code>globus_callback_space_t</code> space)<br />
 <i>Fire a callback when the specified signal is received. </i><br />
 <code>globus_result_t</code> <code>globus_callback_unregister_signal_handler</code> (int signum, <code>globus_callback_func_t</code> unregister_callback, void *unreg_arg)<br />
 <i>Unregister a signal handling callback. </i><br />
 void <code>globus_callback_add_wakeup_handler</code> (void(*wakeup)(void *), void *user_arg)<br />
 <i>Register a wakeup handler with callback library. </i></p>
<h2>Detailed Description</h2>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_SIGNAL_INTERRUPT</h3>
<p> Use this to trap interrupts (SIGINT on unix). In the future, this will also map to handle ctrl-C on win32.</p>
<h2>Function Documentation</h2>
<h3>void globus_callback_add_wakeup_handler (void(*)(void *)wakeup, void *user_arg)</h3>
<p> Register a wakeup handler with callback library. This is really only needed in non-threaded builds, but for cross builds should be used everywhere that a callback may sleep for an extended period of time. </p>
<p> An example use is for an io poller that sleeps indefinitely on select(). If the callback library receives a signal that it needs to deliver asap, it will call the wakeup handler(s), These wakeup handlers must run as though they were called from a signal handler (don&#8217;t use any thread utilities). The io poll example will likely write a single byte to a pipe that select() is monitoring. </p>
<p> This handler will not be unregistered until the callback library is deactivated (via common). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>wakeup</i> function to call when callback library needs you to return asap from any blocked callbacks.<br />
 <i>user_arg</i> user data that will be passed along in the wakeup handler</dl>
<h3><code>globus_result_t</code> globus_callback_space_register_signal_handler (intsignum, <code>globus_bool_t</code>persist, <code>globus_callback_func_t</code>callback_func, void *callback_user_arg, <code>globus_callback_space_t</code>space)</h3>
<p> Fire a callback when the specified signal is received. Note that there is a tiny delay between the time this call returns and the signal is actually handled by this library. It is likely that, if the signal was received the instant the call returned, it will be lost (this is normally not an issue, since you would call this in your startup code anyway) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>signum</i> The signal to receive. The following signals are not allowed: SIGKILL, SIGSEGV, SIGABRT, SIGBUS, SIGFPE, SIGILL, SIGIOT, SIGPIPE, SIGEMT, SIGSYS, SIGTRAP, SIGSTOP, SIGCONT, and SIGWAITING<br />
 <i>persist</i> If GLOBUS_TRUE, keep this callback registered for multiple signals. If GLOBUS_FALSE, the signal handler will automatically be unregistered once the signal has been received.<br />
 <i>callback_func</i> the user func to call when a signal is received<br />
 <i>callback_user_arg</i> user arg that will be passed to callback<br />
 <i>space</i> the space to deliver callbacks to.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_SPACE</p>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_ARGUMENT</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS otherwise</dl>
</dl>
<h3><code>globus_result_t</code> globus_callback_unregister_signal_handler (intsignum, <code>globus_callback_func_t</code>unregister_callback, void *unreg_arg)</h3>
<p> Unregister a signal handling callback. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>signum</i> The signal to unregister.<br />
 <i>unregister_callback</i> the function to call when the callback has been canceled and there are no running instances of it (may be NULL). This will be delivered to the same space used in the register call.<br />
 <i>unreg_arg</i> user arg that will be passed to callback</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_ARGUMENT if this signal was registered with persist == false, then there is a race between a signal actually being caught and therefor automatically unregistered and the attempt to manually unregister it. If that race occurs, you will receive this error just as you would for any signal not registered.</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS otherwise</dl>
</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
