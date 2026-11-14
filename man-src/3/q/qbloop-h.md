---
title: "qbloop-h(3)"
name: "qbloop-h"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qbloop-h/"
description: "qbloop.h –"
---

<p>qbloop.h &#8211; </p>
<p> Main loop manages timers, jobs and polling sockets.</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;signal.h&gt;

#include &lt;stdint.h&gt;</code></pre>
<h3>Typedefs</h3>
<p>typedef struct qb_loop <code>qb_loop_t</code><br />
 <i>An opaque data type representing the main loop. </i><br />
 typedef uint64_t <code>qb_loop_timer_handle</code> </p>
<p> typedef void * <code>qb_loop_signal_handle</code> </p>
<p> typedef int32_t(* <code>qb_loop_poll_dispatch_fn</code> )(int32_t fd, int32_t revents, void *data) </p>
<p> typedef void(* <code>qb_loop_job_dispatch_fn</code> )(void *data) </p>
<p> typedef void(* <code>qb_loop_timer_dispatch_fn</code> )(void *data) </p>
<p> typedef int32_t(* <code>qb_loop_signal_dispatch_fn</code> )(int32_t rsignal, void *data) </p>
<p> typedef void(* <code>qb_loop_poll_low_fds_event_fn</code> )(int32_t not_enough, int32_t fds_available)</p>
<h3>Enumerations</h3>
<pre><code>enum qb_loop_priority { QB_LOOP_LOW = 0, QB_LOOP_MED = 1, QB_LOOP_HIGH = 2 }


Priorites for jobs, timers &amp; poll.



Functions</code></pre>
<p> <code>qb_loop_t</code> * <code>qb_loop_create</code> (void)<br />
 <i>Create a new main loop. </i><br />
 void <code>qb_loop_destroy</code> (struct qb_loop *l) </p>
<p> void <code>qb_loop_stop</code> (<code>qb_loop_t</code> *l)<br />
 <i>Stop the main loop. </i><br />
 void <code>qb_loop_run</code> (<code>qb_loop_t</code> *l)<br />
 <i>Run the main loop. </i><br />
 int32_t <code>qb_loop_job_add</code> (<code>qb_loop_t</code> *l, enum <code>qb_loop_priority</code> p, void *data, <code>qb_loop_job_dispatch_fn</code> dispatch_fn)<br />
 <i>Add a job to the mainloop. </i><br />
 int32_t <code>qb_loop_job_del</code> (struct qb_loop *l, enum <code>qb_loop_priority</code> p, void *data, <code>qb_loop_job_dispatch_fn</code> dispatch_fn)<br />
 <i>Delete a job from the mainloop. </i><br />
 int32_t <code>qb_loop_timer_add</code> (<code>qb_loop_t</code> *l, enum <code>qb_loop_priority</code> p, uint64_t nsec_duration, void *data, <code>qb_loop_timer_dispatch_fn</code> dispatch_fn, <code>qb_loop_timer_handle</code> *timer_handle_out)<br />
 <i>Add a timer to the mainloop. </i><br />
 int32_t <code>qb_loop_timer_del</code> (<code>qb_loop_t</code> *l, <code>qb_loop_timer_handle</code> th)<br />
 <i>Delete a timer that is still outstanding. </i><br />
 int32_t <code>qb_loop_timer_is_running</code> (<code>qb_loop_t</code> *l, <code>qb_loop_timer_handle</code> th)<br />
 <i>Check to see if a timer that is still outstanding. </i><br />
 uint64_t <code>qb_loop_timer_expire_time_get</code> (struct qb_loop *l, <code>qb_loop_timer_handle</code> th)<br />
 <i>Get the time remaining before it expires. </i><br />
 int32_t <code>qb_loop_poll_low_fds_event_set</code> (<code>qb_loop_t</code> *l, <code>qb_loop_poll_low_fds_event_fn</code> fn)<br />
 <i>Set a callback to receive events on file descriptors getting low. </i><br />
 int32_t <code>qb_loop_poll_add</code> (<code>qb_loop_t</code> *l, enum <code>qb_loop_priority</code> p, int32_t fd, int32_t events, void *data, <code>qb_loop_poll_dispatch_fn</code> dispatch_fn)<br />
 <i>Add a poll job to the mainloop. </i><br />
 int32_t <code>qb_loop_poll_mod</code> (<code>qb_loop_t</code> *l, enum <code>qb_loop_priority</code> p, int32_t fd, int32_t events, void *data, <code>qb_loop_poll_dispatch_fn</code> dispatch_fn)<br />
 <i>Modify a poll job. </i><br />
 int32_t <code>qb_loop_poll_del</code> (<code>qb_loop_t</code> *l, int32_t fd)<br />
 <i>Delete a poll job. </i><br />
 int32_t <code>qb_loop_signal_add</code> (<code>qb_loop_t</code> *l, enum <code>qb_loop_priority</code> p, int32_t sig, void *data, <code>qb_loop_signal_dispatch_fn</code> dispatch_fn, <code>qb_loop_signal_handle</code> *handle)<br />
 <i>Add a signal job. </i><br />
 int32_t <code>qb_loop_signal_mod</code> (<code>qb_loop_t</code> *l, enum <code>qb_loop_priority</code> p, int32_t sig, void *data, <code>qb_loop_signal_dispatch_fn</code> dispatch_fn, <code>qb_loop_signal_handle</code> handle)<br />
 <i>Modify the signal job. </i><br />
 int32_t <code>qb_loop_signal_del</code> (<code>qb_loop_t</code> *l, <code>qb_loop_signal_handle</code> handle)<br />
 <i>Delete the signal job. </i></p>
<h2>Detailed Description</h2>
<p>Main loop manages timers, jobs and polling sockets.</p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* qb_loop_job_dispatch_fn)(void *data)</h3>
<h3>typedef int32_t(* qb_loop_poll_dispatch_fn)(int32_t fd, int32_t revents, void *data)</h3>
<h3>typedef void(* qb_loop_poll_low_fds_event_fn)(int32_t not_enough, int32_t fds_available)</h3>
<h3>typedef int32_t(* qb_loop_signal_dispatch_fn)(int32_t rsignal, void *data)</h3>
<h3>typedef void* <code>qb_loop_signal_handle</code></h3>
<h3>typedef struct qb_loop <code>qb_loop_t</code></h3>
<p>An opaque data type representing the main loop.</p>
<h3>typedef void(* qb_loop_timer_dispatch_fn)(void *data)</h3>
<h3>typedef uint64_t <code>qb_loop_timer_handle</code></h3>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>qb_loop_priority</code></h3>
<p>Priorites for jobs, timers &amp; poll. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>QB_LOOP_LOW </i></p>
<dd>
<dt><i>QB_LOOP_MED </i></p>
<dd>
<dt><i>QB_LOOP_HIGH </i></p>
<dd></dl>
<h2>Function Documentation</h2>
<h3><code>qb_loop_t</code>* qb_loop_create (void)</h3>
<p>Create a new main loop. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>loop instance.</dl>
<h3>void qb_loop_destroy (struct qb_loop *l)</h3>
<h3>int32_t qb_loop_job_add (<code>qb_loop_t</code> *l, enum <code>qb_loop_priority</code>p, void *data, <code>qb_loop_job_dispatch_fn</code>dispatch_fn)</h3>
<p>Add a job to the mainloop. This is run in the next cycle of the loop. </p>
<p> <code>Note:</code></p>
<dl>
<dd>it is a one-shot job.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance<br />
 <i>p</i> the priority<br />
 <i>data</i> user data passed into the dispatch function<br />
 <i>dispatch_fn</i> callback function</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>status (0 == ok, -errno == failure)</dl>
<h3>int32_t qb_loop_job_del (struct qb_loop *l, enum <code>qb_loop_priority</code>p, void *data, <code>qb_loop_job_dispatch_fn</code>dispatch_fn)</h3>
<p>Delete a job from the mainloop. This will try to delete the job if it hasn&#8217;t run yet. </p>
<p> <code>Note:</code></p>
<dl>
<dd>this will remove the first job that matches the paramaters (priority, data, dispatch_fn).</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance<br />
 <i>p</i> the priority<br />
 <i>data</i> user data passed into the dispatch function<br />
 <i>dispatch_fn</i> callback function</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>status (0 == ok, -errno == failure)</dl>
<h3>int32_t qb_loop_poll_add (<code>qb_loop_t</code> *l, enum <code>qb_loop_priority</code>p, int32_tfd, int32_tevents, void *data, <code>qb_loop_poll_dispatch_fn</code>dispatch_fn)</h3>
<p>Add a poll job to the mainloop. </p>
<p> <code>Note:</code></p>
<dl>
<dd>it is a re-occuring job.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance<br />
 <i>p</i> the priority<br />
 <i>fd</i> file descriptor.<br />
 <i>events</i> (POLLIN|POLLOUT) etc &#8230;.<br />
 <i>data</i> user data passed into the dispatch function<br />
 <i>dispatch_fn</i> callback function</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>status (0 == ok, -errno == failure)</dl>
<h3>int32_t qb_loop_poll_del (<code>qb_loop_t</code> *l, int32_tfd)</h3>
<p>Delete a poll job. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance<br />
 <i>fd</i> file descriptor.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>status (0 == ok, -errno == failure)</dl>
<h3>int32_t qb_loop_poll_low_fds_event_set (<code>qb_loop_t</code> *l, <code>qb_loop_poll_low_fds_event_fn</code>fn)</h3>
<p>Set a callback to receive events on file descriptors getting low. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance<br />
 <i>fn</i> callback function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>status (0 == ok, -errno == failure)</dl>
<h3>int32_t qb_loop_poll_mod (<code>qb_loop_t</code> *l, enum <code>qb_loop_priority</code>p, int32_tfd, int32_tevents, void *data, <code>qb_loop_poll_dispatch_fn</code>dispatch_fn)</h3>
<p>Modify a poll job. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance<br />
 <i>p</i> the priority<br />
 <i>fd</i> file descriptor.<br />
 <i>events</i> (POLLIN|POLLOUT) etc &#8230;.<br />
 <i>data</i> user data passed into the dispatch function<br />
 <i>dispatch_fn</i> callback function</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>status (0 == ok, -errno == failure)</dl>
<h3>void qb_loop_run (<code>qb_loop_t</code> *l)</h3>
<p>Run the main loop. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance</dl>
<h3>int32_t qb_loop_signal_add (<code>qb_loop_t</code> *l, enum <code>qb_loop_priority</code>p, int32_tsig, void *data, <code>qb_loop_signal_dispatch_fn</code>dispatch_fn, <code>qb_loop_signal_handle</code> *handle)</h3>
<p>Add a signal job. Get a callback on this signal (not in the context of the signal). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance<br />
 <i>p</i> the priority<br />
 <i>sig</i> (SIGHUP or SIGINT) etc &#8230;.<br />
 <i>data</i> user data passed into the dispatch function<br />
 <i>dispatch_fn</i> callback function<br />
 <i>handle</i> (out) a reference to the signal job</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>status (0 == ok, -errno == failure)</dl>
<h3>int32_t qb_loop_signal_del (<code>qb_loop_t</code> *l, <code>qb_loop_signal_handle</code>handle)</h3>
<p>Delete the signal job. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance<br />
 <i>handle</i> (in) a reference to the signal job</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>status (0 == ok, -errno == failure)</dl>
<h3>int32_t qb_loop_signal_mod (<code>qb_loop_t</code> *l, enum <code>qb_loop_priority</code>p, int32_tsig, void *data, <code>qb_loop_signal_dispatch_fn</code>dispatch_fn, <code>qb_loop_signal_handle</code>handle)</h3>
<p>Modify the signal job. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance<br />
 <i>p</i> the priority<br />
 <i>sig</i> (SIGHUP or SIGINT) etc &#8230;.<br />
 <i>data</i> user data passed into the dispatch function<br />
 <i>dispatch_fn</i> callback function<br />
 <i>handle</i> (in) a reference to the signal job</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>status (0 == ok, -errno == failure)</dl>
<h3>void qb_loop_stop (<code>qb_loop_t</code> *l)</h3>
<p>Stop the main loop. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance</dl>
<h3>int32_t qb_loop_timer_add (<code>qb_loop_t</code> *l, enum <code>qb_loop_priority</code>p, uint64_tnsec_duration, void *data, <code>qb_loop_timer_dispatch_fn</code>dispatch_fn, <code>qb_loop_timer_handle</code> *timer_handle_out)</h3>
<p>Add a timer to the mainloop. </p>
<p> <code>Note:</code></p>
<dl>
<dd>it is a one-shot job.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance<br />
 <i>p</i> the priority<br />
 <i>nsec_duration</i> nano-secs in the future to run the dispatch.<br />
 <i>data</i> user data passed into the dispatch function<br />
 <i>dispatch_fn</i> callback function<br />
 <i>timer_handle_out</i> handle to delete the timer if needed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>status (0 == ok, -errno == failure)</dl>
<h3>int32_t qb_loop_timer_del (<code>qb_loop_t</code> *l, <code>qb_loop_timer_handle</code>th)</h3>
<p>Delete a timer that is still outstanding. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance<br />
 <i>th</i> handle to delete the timer if needed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>status (0 == ok, -errno == failure)</dl>
<h3>uint64_t qb_loop_timer_expire_time_get (struct qb_loop *l, <code>qb_loop_timer_handle</code>th)</h3>
<p>Get the time remaining before it expires. </p>
<p> <code>Note:</code></p>
<dl>
<dd>if the timer has already expired it will return 0</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance<br />
 <i>th</i> timer handle.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>nano seconds left</dl>
<h3>int32_t qb_loop_timer_is_running (<code>qb_loop_t</code> *l, <code>qb_loop_timer_handle</code>th)</h3>
<p>Check to see if a timer that is still outstanding. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>l</i> pointer to the loop instance<br />
 <i>th</i> handle to delete the timer if needed.</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>QB_TRUE</i> yes this timer is outstanding<br />
 <i>QB_FALSE</i> this timer does not exist or has expired</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libqb from the source code.</p>
