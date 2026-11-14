---
title: "globus_callback_signal_poll(3)"
name: "globus_callback_signal_poll"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_callback_signal_poll/"
description: "Globus Callback API –"
---

<h2 class="name">NAME</h2>
<p> Globus Callback API &#8211; </p>
<h3>Convenience Macros</h3>
<p> #define <code>globus_callback_poll</code>(a)<br />
 <i>Poll the global callback space. </i><br />
 #define <code>globus_poll_blocking</code>()<br />
 <i>Blocking poll of the global callback space. </i><br />
 #define <code>globus_poll_nonblocking</code>()<br />
 <i>Nonblocking poll of the global callback space. </i><br />
 #define <code>globus_poll</code>()<br />
 <i>Nonblocking poll of the global callback space. </i><br />
 #define <code>globus_signal_poll</code>()<br />
 <i>Wake up callback polling thread. </i><br />
 #define <code>globus_callback_register_oneshot</code>(callback_handle,delay_time,callback_func,callback_user_arg)<br />
 <i>Register a oneshot function in the global callback space. </i><br />
 #define <code>globus_callback_register_periodic</code>(callback_handle,delay_time,period,callback_func,callback_user_arg)<br />
 <i>Register a periodic function in the global callback space. </i><br />
 #define <code>globus_callback_register_signal_handler</code>(signum,persist,callback_func,callback_user_arg)<br />
 <i>Register a signal handler in the global callback space. </i></p>
<h3>Callback Prototypes</h3>
<p> typedef void(* <code>globus_callback_func_t</code> )(void *user_arg)<br />
 <i>Globus callback prototype. </i></p>
<h3>Oneshot Callbacks</h3>
<p> <code>globus_result_t</code> <code>globus_callback_space_register_oneshot</code> (<code>globus_callback_handle_t</code> *callback_handle, const globus_reltime_t *delay_time, <code>globus_callback_func_t</code> callback_func, void *callback_user_arg, <code>globus_callback_space_t</code> space)<br />
 <i>Register a oneshot some delay from now. </i></p>
<h3>Periodic Callbacks</h3>
<p> <code>globus_result_t</code> <code>globus_callback_space_register_periodic</code> (<code>globus_callback_handle_t</code> *callback_handle, const globus_reltime_t *delay_time, const globus_reltime_t *period, <code>globus_callback_func_t</code> callback_func, void *callback_user_arg, <code>globus_callback_space_t</code> space)<br />
 <i>Register a periodic callback. </i><br />
 <code>globus_result_t</code> <code>globus_callback_unregister</code> (<code>globus_callback_handle_t</code> callback_handle, <code>globus_callback_func_t</code> unregister_callback, void *unreg_arg, <code>globus_bool_t</code> *active)<br />
 <i>Unregister a callback. </i><br />
 <code>globus_result_t</code> <code>globus_callback_adjust_oneshot</code> (<code>globus_callback_handle_t</code> callback_handle, const globus_reltime_t *new_delay)<br />
 <i>Adjust the delay of a oneshot callback. </i><br />
 <code>globus_result_t</code> <code>globus_callback_adjust_period</code> (<code>globus_callback_handle_t</code> callback_handle, const globus_reltime_t *new_period)<br />
 <i>Adjust the period of a periodic callback. </i></p>
<h3>Callback Polling</h3>
<p> void <code>globus_callback_space_poll</code> (const globus_abstime_t *timestop, <code>globus_callback_space_t</code> space)<br />
 <i>Poll for ready callbacks. </i><br />
 void <code>globus_callback_signal_poll</code> ()<br />
 <i>Signal the poll. </i></p>
<h3>Miscellaneous</h3>
<p> <code>globus_bool_t</code> <code>globus_callback_get_timeout</code> (globus_reltime_t *time_left)<br />
 <i>Get the amount of time left in a callback. </i><br />
 <code>globus_bool_t</code> <code>globus_callback_has_time_expired</code> ()<br />
 <i>See if there is remaining time in a callback. </i><br />
 <code>globus_bool_t</code> <code>globus_callback_was_restarted</code> ()<br />
 <i>See if a callback has been restarted. </i></p>
<h2>Detailed Description</h2>
<h2>Macro Definition Documentation</h2>
<h3>#define globus_callback_poll(a)</h3>
<p> Poll the global callback space. Specifies the global space for <code>globus_callback_space_poll()</code>. argument is the timeout </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_poll()</code></dl>
<h3>#define globus_callback_register_oneshot(callback_handle, delay_time, callback_func, callback_user_arg)</h3>
<p> Register a oneshot function in the global callback space. Specifies the global space for <code>globus_callback_space_register_oneshot()</code> all other arguments are the same as specified there. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_register_oneshot()</code></dl>
<h3>#define globus_callback_register_periodic(callback_handle, delay_time, period, callback_func, callback_user_arg)</h3>
<p> Register a periodic function in the global callback space. Specifies the global space for <code>globus_callback_space_register_periodic()</code> all other arguments are the same as specified there. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_register_periodic()</code></dl>
<h3>#define globus_callback_register_signal_handler(signum, persist, callback_func, callback_user_arg)</h3>
<p> Register a signal handler in the global callback space. Specifies the global space for <code>globus_callback_space_register_signal_handler()</code> all other arguments are the same as specified there. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_register_signal_handler()</code></dl>
<h3>#define globus_poll()</h3>
<p> Nonblocking poll of the global callback space. Specifies that <code>globus_callback_space_poll()</code> should poll on the global space with an immediate timeout </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_poll()</code></dl>
<h3>#define globus_poll_blocking()</h3>
<p> Blocking poll of the global callback space. Specifies that <code>globus_callback_space_poll()</code> should poll on the global space with an infinite timeout </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_poll()</code></dl>
<h3>#define globus_poll_nonblocking()</h3>
<p> Nonblocking poll of the global callback space. Specifies that <code>globus_callback_space_poll()</code> should poll on the global space with an immediate timeout </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_poll()</code></dl>
<h3>#define globus_signal_poll()</h3>
<p> Wake up callback polling thread. Counterpart to <code>globus_poll()</code>. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_signal_poll()</code></dl>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_callback_func_t)(void *user_arg)</h3>
<p> Globus callback prototype. This is the signature of the function registered with the globus_callback_register_* calls. </p>
<p> If this is a periodic callback, it is guaranteed that the call canNOT be reentered unless globus_thread_blocking_space_will_block() is called (explicitly, or implicitly via <code>globus_cond_wait()</code>). Also, if <code>globus_callback_unregister()</code> is called to cancel this periodic from within this callback, it is guaranteed that the callback will NOT be requeued again </p>
<p> If the function will block at all, the user should call <code>globus_callback_get_timeout()</code> to see how long this function can safely block or call globus_thread_blocking_space_will_block() </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>user_arg</i> The user argument registered with this callback</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> void</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_register_oneshot()</code> </p>
<p> <code>globus_callback_space_register_periodic()</code> </p>
<p> globus_thread_blocking_space_will_block() </p>
<p> <code>globus_callback_get_timeout()</code></dl>
<h2>Function Documentation</h2>
<h3><code>globus_result_t</code> globus_callback_adjust_oneshot (<code>globus_callback_handle_t</code>callback_handle, const globus_reltime_t *new_delay)</h3>
<p> Adjust the delay of a oneshot callback. This function allows a user to adjust the delay of a previously registered callback. It is safe to call this within or outside of the callback that is being modified. </p>
<p> Note if the oneshot has already been fired, this function will still return GLOBUS_SUCCESS, but won&#8217;t affect anything. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_handle</i> the handle received from a <code>globus_callback_space_register_oneshot()</code> call<br />
 <i>new_delay</i> The new delay from now. If NULL, then callback will be fired as soon as possible.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_CALLBACK_HANDLE</p>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_ALREADY_CANCELED</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_register_periodic()</code></dl>
<h3><code>globus_result_t</code> globus_callback_adjust_period (<code>globus_callback_handle_t</code>callback_handle, const globus_reltime_t *new_period)</h3>
<p> Adjust the period of a periodic callback. This function allows a user to adjust the period of a previously registered callback. It is safe to call this within or outside of the callback that is being modified. </p>
<p> This func also allows a user to effectively &#8216;suspend&#8217; a periodic callback until another time by passing a period of NULL. The callback can later be resumed by passing in a new period. </p>
<p> Note that the callback will not be fired sooner than &#8216;new_period&#8217; from now. A &#8216;suspended&#8217; callback must still be unregistered to free its resources. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_handle</i> the handle received from a <code>globus_callback_space_register_periodic()</code> call<br />
 <i>new_period</i> The new period. If NULL or globus_i_reltime_infinity, then callback will be &#8216;suspended&#8217; as soon as the last running instance of it returns.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_CALLBACK_HANDLE</p>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_ALREADY_CANCELED</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_register_periodic()</code></dl>
<h3><code>globus_bool_t</code> globus_callback_get_timeout (globus_reltime_t *time_left)</h3>
<p> Get the amount of time left in a callback. This function retrieves the remaining time a callback is allowed to run. If a callback has already timed out, time_left will be set to zero and GLOBUS_TRUE returned. This function is intended to be called within a callback&#8217;s stack, but is harmless to call anywhere (will return GLOBUS_FALSE and an infinite time_left) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>time_left</i> storage for the remaining time.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_FALSE if time remaining</p>
<dt>&bull;</p>
<dd> GLOBUS_TRUE if already timed out</dl>
</dl>
<h3><code>globus_bool_t</code> globus_callback_has_time_expired ()</h3>
<p> See if there is remaining time in a callback. This function returns GLOBUS_TRUE if the running time of a callback has already expired. This function is intended to be called within a callback&#8217;s stack, but is harmless to call anywhere (will return GLOBUS_FALSE) </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_FALSE if time remaining</p>
<dt>&bull;</p>
<dd> GLOBUS_TRUE if already timed out</dl>
</dl>
<h3>void globus_callback_signal_poll ()</h3>
<p> Signal the poll. This function signals <code>globus_callback_space_poll()</code> that something has changed and it should return to its caller as soon as possible. </p>
<p> In general, you never need to call this function directly. It is called (when necessary) by <code>globus_cond_signal()</code> or globus_cond_broadcast. The only case in which a user may wish to call this explicitly is if the application has no aspirations of ever being built threaded. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> void</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_poll()</code></dl>
<h3>void globus_callback_space_poll (const globus_abstime_t *timestop, <code>globus_callback_space_t</code>space)</h3>
<p> Poll for ready callbacks. This function is used to poll for registered callbacks. </p>
<p> For non-threaded builds, callbacks are not/can not be delivered unless this is called. Any call to this can cause callbacks registered with the &#8216;global&#8217; space to be fired. Whereas callbacks registered with a user&#8217;s space will only be delivered when this is called with that space. </p>
<p> For threaded builds, this only needs to be called to poll user spaces with behavior == GLOBUS_CALLBACK_SPACE_BEHAVIOR_SINGLE. The &#8216;global&#8217; space and other user spaces are constantly polled in a separate thread. (If it is called in a threaded build for these spaces, it will just yield its thread) </p>
<p> In general, you never need to call this function directly. It is called (when necessary) by <code>globus_cond_wait()</code>. The only case in which a user may wish to call this explicitly is if the application has no aspirations of ever being built threaded. </p>
<p> This function (when not yielding) will block up to timestop or until <code>globus_callback_signal_poll()</code> is called by one of the fired callbacks. It will always try and kick out ready callbacks, regardless of the timestop. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>timestop</i> The time to block until. If this is NULL or less than the cuurent time, an attempt to fire only ready callbacks is made (no blocking).<br />
 <i>space</i> The callback space to poll. Note: regardless of what space is passed here, the &#8216;global&#8217; space is also always polled.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> void</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>Globus Callback Spaces</code> </p>
<p> <code>globus_condattr_setspace()</code></dl>
<h3><code>globus_result_t</code> globus_callback_space_register_oneshot (<code>globus_callback_handle_t</code> *callback_handle, const globus_reltime_t *delay_time, <code>globus_callback_func_t</code>callback_func, void *callback_user_arg, <code>globus_callback_space_t</code>space)</h3>
<p> Register a oneshot some delay from now. This function registers the callback_func to start some delay_time from now. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_handle</i> Storage for a handle. This may be NULL. If it is NOT NULL, you must unregister the callback to reclaim resources.<br />
 <i>delay_time</i> The relative time from now to fire this callback. If NULL, will fire as soon as possible<br />
 <i>callback_func</i> the user func to call<br />
 <i>callback_user_arg</i> user arg that will be passed to callback<br />
 <i>space</i> The space with which to register this callback</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_ARGUMENT</p>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_MEMORY_ALLOC</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_func_t</code> </p>
<p> <code>Globus Callback Spaces</code></dl>
<h3><code>globus_result_t</code> globus_callback_space_register_periodic (<code>globus_callback_handle_t</code> *callback_handle, const globus_reltime_t *delay_time, const globus_reltime_t *period, <code>globus_callback_func_t</code>callback_func, void *callback_user_arg, <code>globus_callback_space_t</code>space)</h3>
<p> Register a periodic callback. This function registers a periodic callback_func to start some delay_time and run every period from then. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_handle</i> Storage for a handle. This may be NULL. If it is NOT NULL, you must cancel the periodic to reclaim resources.<br />
 <i>delay_time</i> The relative time from now to fire this callback. If NULL, will fire the first callback as soon as possible<br />
 <i>period</i> The relative period of this callback<br />
 <i>callback_func</i> the user func to call<br />
 <i>callback_user_arg</i> user arg that will be passed to callback<br />
 <i>space</i> The space with which to register this callback</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_ARGUMENT</p>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_MEMORY_ALLOC</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_unregister()</code> </p>
<p> <code>globus_callback_func_t</code> </p>
<p> <code>globus_callback_spaces</code></dl>
<h3><code>globus_result_t</code> globus_callback_unregister (<code>globus_callback_handle_t</code>callback_handle, <code>globus_callback_func_t</code>unregister_callback, void *unreg_arg, <code>globus_bool_t</code> *active)</h3>
<p> Unregister a callback. This function will cancel a callback and free the resources associcated with the callback handle. If the callback was able to be canceled immediately (or if it has already run), GLOBUS_SUCCESS is returned and it is guaranteed that there are no running instances of the callback. </p>
<p> If the callback is currently running (or unstoppably about to be run), then the callback is prevented from being requeued, but, the &#8216;official&#8217; cancel is deferred until the last running instance of the callback returns. If you need to know when the callback is guaranteed to have been canceled, pass an unregister callback. </p>
<p> If you would like to know if you unregistered a callback before it ran, pass storage for a boolean &#8216;active&#8217;. This will be GLOBUS_TRUE if callback was running. GLOBUS_FALSE otherwise. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_handle</i> the handle received from a globus_callback_space_register_*() call<br />
 <i>unregister_callback</i> the function to call when the callback has been canceled and there are no running instances of it. This will be delivered to the same space used in the register call.<br />
 <i>unreg_arg</i> user arg that will be passed to the unregister callback<br />
 <i>active</i> storage for an indication of whether the callback was running when this call was made</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_CALLBACK_HANDLE</p>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_ALREADY_CANCELED</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_register_periodic()</code> </p>
<p> <code>globus_callback_func_t</code></dl>
<h3><code>globus_bool_t</code> globus_callback_was_restarted ()</h3>
<p> See if a callback has been restarted. If the callback is a oneshot, this merely means the callback called globus_thread_blocking_space_will_block (or <code>globus_cond_wait()</code> at some point. </p>
<p> For a periodic, it signifies the same and also that the periodic has been requeued. This means that the callback function may be reentered if the period is short enough (on a threaded build) </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_FALSE if not restarted</p>
<dt>&bull;</p>
<dd> GLOBUS_TRUE if restarted</dl>
</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBF">Author</a></p>
<dd></dl>
