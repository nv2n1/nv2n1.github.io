---
title: "globus_callback-h(3)"
name: "globus_callback-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_callback-h/"
description: "globus_callback.h –"
---

<p>globus_callback.h &#8211; </p>
<p> Globus Callback API.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common_include.h&#8217;<br />
 #include &#8216;globus_module.h&#8217;<br />
 #include &#8216;globus_time.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_CALLBACK_MODULE</code><br />
 <i>Module descriptor. </i><br />
 #define <code>GLOBUS_POLL_MODULE</code><br />
 <i>Module descriptor. </i><br />
 #define <code>GLOBUS_CALLBACK_GLOBAL_SPACE</code><br />
 <i>Global callback space. </i><br />
 #define <code>GLOBUS_SIGNAL_INTERRUPT</code> </p>
<p> <code>Convenience Macros</code> </p>
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
<h3>Typedefs</h3>
<p>typedef int <code>globus_callback_handle_t</code><br />
 <i>Periodic callback handle. </i><br />
 typedef int <code>globus_callback_space_t</code><br />
 <i>Callback space handle. </i><br />
 typedef struct<br />
 globus_l_callback_space_attr_s * <code>globus_callback_space_attr_t</code>&quot;<br />
 <i>Callback space attribute. </i> </p>
<p> <code>Callback Prototypes</code> </p>
<p> typedef void(* <code>globus_callback_func_t</code> )(void *user_arg)<br />
 <i>Globus callback prototype. </i></p>
<h3>Enumerations</h3>
<p>enum <code>globus_callback_error_type_t</code> { <code>GLOBUS_CALLBACK_ERROR_INVALID_CALLBACK_HANDLE</code> = 1024, <code>GLOBUS_CALLBACK_ERROR_INVALID_SPACE</code>, <code>GLOBUS_CALLBACK_ERROR_MEMORY_ALLOC</code>, <code>GLOBUS_CALLBACK_ERROR_INVALID_ARGUMENT</code>, <code>GLOBUS_CALLBACK_ERROR_ALREADY_CANCELED</code>, <code>GLOBUS_CALLBACK_ERROR_NO_ACTIVE_CALLBACK</code> }<br />
 <i>Error types. </i><br />
 enum <code>globus_callback_space_behavior_t</code> { <code>GLOBUS_CALLBACK_SPACE_BEHAVIOR_SINGLE</code>, <code>GLOBUS_CALLBACK_SPACE_BEHAVIOR_SERIALIZED</code>, <code>GLOBUS_CALLBACK_SPACE_BEHAVIOR_THREADED</code> }<br />
 <i>Callback space behaviors describe how a space behaves. </i></p>
<h3>Functions</h3>
<p><code>globus_result_t</code> <code>globus_callback_space_init</code> (<code>globus_callback_space_t</code> *space, <code>globus_callback_space_attr_t</code> attr)<br />
 <i>Initialize a user space. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_reference</code> (<code>globus_callback_space_t</code> space)<br />
 <i>Take a reference to a space. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_destroy</code> (<code>globus_callback_space_t</code> space)<br />
 <i>Destroy a reference to a user space. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_attr_init</code> (<code>globus_callback_space_attr_t</code> *attr)<br />
 <i>Initialize a space attr. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_attr_destroy</code> (<code>globus_callback_space_attr_t</code> attr)<br />
 <i>Destroy a space attr. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_attr_set_behavior</code> (<code>globus_callback_space_attr_t</code> attr, <code>globus_callback_space_behavior_t</code> behavior)<br />
 <i>Set the behavior of a space. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_attr_get_behavior</code> (<code>globus_callback_space_attr_t</code> attr, <code>globus_callback_space_behavior_t</code> *behavior)<br />
 <i>Get the behavior associated with an attr. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_get</code> (<code>globus_callback_space_t</code> *space)<br />
 <i>Retrieve the space of a currently running callback. </i><br />
 int <code>globus_callback_space_get_depth</code> (<code>globus_callback_space_t</code> space)<br />
 <i>Retrieve the current nesting level of a space. </i><br />
 <code>globus_bool_t</code> <code>globus_callback_space_is_single</code> (<code>globus_callback_space_t</code> space)<br />
 <i>See if the specified space is a single threaded behavior space. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_register_signal_handler</code> (int signum, <code>globus_bool_t</code> persist, <code>globus_callback_func_t</code> callback_func, void *callback_user_arg, <code>globus_callback_space_t</code> space)<br />
 <i>Fire a callback when the specified signal is received. </i><br />
 <code>globus_result_t</code> <code>globus_callback_unregister_signal_handler</code> (int signum, <code>globus_callback_func_t</code> unregister_callback, void *unreg_arg)<br />
 <i>Unregister a signal handling callback. </i><br />
 void <code>globus_callback_add_wakeup_handler</code> (void(*wakeup)(void *), void *user_arg)<br />
 <i>Register a wakeup handler with callback library. </i> </p>
<p> <code>Oneshot Callbacks</code> </p>
<p> <code>globus_result_t</code> <code>globus_callback_space_register_oneshot</code> (<code>globus_callback_handle_t</code> *callback_handle, const globus_reltime_t *delay_time, <code>globus_callback_func_t</code> callback_func, void *callback_user_arg, <code>globus_callback_space_t</code> space)<br />
 <i>Register a oneshot some delay from now. </i> </p>
<p> <code>Periodic Callbacks</code> </p>
<p> <code>globus_result_t</code> <code>globus_callback_space_register_periodic</code> (<code>globus_callback_handle_t</code> *callback_handle, const globus_reltime_t *delay_time, const globus_reltime_t *period, <code>globus_callback_func_t</code> callback_func, void *callback_user_arg, <code>globus_callback_space_t</code> space)<br />
 <i>Register a periodic callback. </i><br />
 <code>globus_result_t</code> <code>globus_callback_unregister</code> (<code>globus_callback_handle_t</code> callback_handle, <code>globus_callback_func_t</code> unregister_callback, void *unreg_arg, <code>globus_bool_t</code> *active)<br />
 <i>Unregister a callback. </i><br />
 <code>globus_result_t</code> <code>globus_callback_adjust_oneshot</code> (<code>globus_callback_handle_t</code> callback_handle, const globus_reltime_t *new_delay)<br />
 <i>Adjust the delay of a oneshot callback. </i><br />
 <code>globus_result_t</code> <code>globus_callback_adjust_period</code> (<code>globus_callback_handle_t</code> callback_handle, const globus_reltime_t *new_period)<br />
 <i>Adjust the period of a periodic callback. </i> </p>
<p> <code>Callback Polling</code> </p>
<p> void <code>globus_callback_space_poll</code> (const globus_abstime_t *timestop, <code>globus_callback_space_t</code> space)<br />
 <i>Poll for ready callbacks. </i><br />
 void <code>globus_callback_signal_poll</code> ()<br />
 <i>Signal the poll. </i> </p>
<p> <code>Miscellaneous</code> </p>
<p> <code>globus_bool_t</code> <code>globus_callback_get_timeout</code> (globus_reltime_t *time_left)<br />
 <i>Get the amount of time left in a callback. </i><br />
 <code>globus_bool_t</code> <code>globus_callback_has_time_expired</code> ()<br />
 <i>See if there is remaining time in a callback. </i><br />
 <code>globus_bool_t</code> <code>globus_callback_was_restarted</code> ()<br />
 <i>See if a callback has been restarted. </i></p>
<h2>Detailed Description</h2>
<p>Globus Callback API. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_common from the source code.</p>
