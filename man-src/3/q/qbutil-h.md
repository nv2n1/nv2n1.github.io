---
title: "qbutil-h(3)"
name: "qbutil-h"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qbutil-h/"
description: "qbutil.h –"
---

<p>qbutil.h &#8211; </p>
<p> These are some convience functions used throughout libqb.</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;pthread.h&gt;

#include &lt;stdint.h&gt;

#include &lt;unistd.h&gt;

#include &lt;qb/qbdefs.h&gt;</code></pre>
<h3>Macros</h3>
<pre><code>#define QB_UTIL_SW_OVERWRITE   0x01



Typedefs</code></pre>
<p> typedef struct qb_thread_lock_s <code>qb_thread_lock_t</code> </p>
<p> typedef void(* <code>qb_util_log_fn_t</code> )(const char *file_name, int32_t file_line, int32_t severity, const char *msg) </p>
<p> typedef struct qb_util_stopwatch <code>qb_util_stopwatch_t</code></p>
<h3>Enumerations</h3>
<p>enum <code>qb_thread_lock_type_t</code> { <code>QB_THREAD_LOCK_SHORT</code>, <code>QB_THREAD_LOCK_LONG</code> }<br />
 <i>QB_THREAD_LOCK_SHORT is a short term lock (spinlock if available on your system) QB_THREAD_LOCK_LONG is a mutex. </i></p>
<h3>Functions</h3>
<p><code>qb_thread_lock_t</code> * <code>qb_thread_lock_create</code> (<code>qb_thread_lock_type_t</code> type)<br />
 <i>Create a new lock of the given type. </i><br />
 int32_t <code>qb_thread_lock</code> (<code>qb_thread_lock_t</code> *tl)<br />
 <i>Calls either pthread_mutex_lock() or pthread_spin_lock(). </i><br />
 int32_t <code>qb_thread_trylock</code> (<code>qb_thread_lock_t</code> *tl)<br />
 <i>Calls either pthread_mutex_trylock() or pthread_spin_trylock(). </i><br />
 int32_t <code>qb_thread_unlock</code> (<code>qb_thread_lock_t</code> *tl)<br />
 <i>Calls either pthread_mutex_unlock() or pthread_spin_unlock. </i><br />
 int32_t <code>qb_thread_lock_destroy</code> (<code>qb_thread_lock_t</code> *tl)<br />
 <i>Calls either pthread_mutex_destro() or pthread_spin_destroy(). </i><br />
 void <code>qb_util_set_log_function</code> (<code>qb_util_log_fn_t</code> fn) <code>QB_GNUC_DEPRECATED</code><br />
 <i>Use this function to output libqb internal log message as you wish. </i><br />
 void <code>qb_timespec_add_ms</code> (struct timespec *ts, int32_t ms)<br />
 <i>Add milliseconds onto the timespec. </i><br />
 uint64_t <code>qb_util_nano_current_get</code> (void)<br />
 <i>Get the current number of nano secounds produced by the systems incrementing clock (CLOCK_MONOTOMIC if available). </i><br />
 uint64_t <code>qb_util_nano_monotonic_hz</code> (void)<br />
 <i>Get the frequence of the clock used in </i><code>qb_util_nano_current_get()</code>.<br />
 uint64_t <code>qb_util_nano_from_epoch_get</code> (void)<br />
 <i>Get the time in nano seconds since epoch. </i><br />
 void <code>qb_util_timespec_from_epoch_get</code> (struct timespec *ts)<br />
 <i>Get the time in timespec since epoch. </i><br />
 char * <code>qb_strerror_r</code> (int errnum, char *buf, size_t buflen)<br />
 <i>strerror_r replacement. </i><br />
 <code>qb_util_stopwatch_t</code> * <code>qb_util_stopwatch_create</code> (void)<br />
 <i>Create a Stopwatch (to time operations) </i><br />
 void <code>qb_util_stopwatch_free</code> (<code>qb_util_stopwatch_t</code> *sw)<br />
 <i>Free the stopwatch. </i><br />
 void <code>qb_util_stopwatch_start</code> (<code>qb_util_stopwatch_t</code> *sw)<br />
 <i>Start the stopwatch. </i><br />
 void <code>qb_util_stopwatch_stop</code> (<code>qb_util_stopwatch_t</code> *sw)<br />
 <i>Stop the stopwatch. </i><br />
 uint64_t <code>qb_util_stopwatch_us_elapsed_get</code> (<code>qb_util_stopwatch_t</code> *sw)<br />
 <i>Get the elapsed time in micro seconds. </i><br />
 float <code>qb_util_stopwatch_sec_elapsed_get</code> (<code>qb_util_stopwatch_t</code> *sw)<br />
 <i>Get the elapsed time in seconds. </i><br />
 int32_t <code>qb_util_stopwatch_split_ctl</code> (<code>qb_util_stopwatch_t</code> *sw, uint32_t max_splits, uint32_t options) </p>
<p> uint64_t <code>qb_util_stopwatch_split</code> (<code>qb_util_stopwatch_t</code> *sw)<br />
 <i>Create a new time split (or lap time) </i><br />
 uint32_t <code>qb_util_stopwatch_split_last</code> (<code>qb_util_stopwatch_t</code> *sw)<br />
 <i>Get the last split index to be used by </i><code>qb_util_stopwatch_time_split_get()</code><br />
 uint64_t <code>qb_util_stopwatch_time_split_get</code> (<code>qb_util_stopwatch_t</code> *sw, uint32_t receint, uint32_t older)<br />
 <i>Read the time split (in us) from &#8216;receint&#8217; to &#8216;older&#8217;. </i></p>
<h2>Detailed Description</h2>
<p>These are some convience functions used throughout libqb. </p>
<p> <code>Author:</code></p>
<dl>
<dd>Angus Salkeld asalkeld [at] redhat.com</dl>
<p> <code>Locking</code></p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>qb_thread_lock_create()</code></p>
<dt>&bull;</p>
<dd><code>qb_thread_lock()</code></p>
<dt>&bull;</p>
<dd><code>qb_thread_trylock()</code></p>
<dt>&bull;</p>
<dd><code>qb_thread_unlock()</code></p>
<dt>&bull;</p>
<dd><code>qb_thread_lock_destroy()</code></dl>
</dl>
<p> <code>Time functions</code></p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>qb_timespec_add_ms()</code></p>
<dt>&bull;</p>
<dd><code>qb_util_nano_current_get()</code></p>
<dt>&bull;</p>
<dd><code>qb_util_nano_monotonic_hz()</code></p>
<dt>&bull;</p>
<dd><code>qb_util_nano_from_epoch_get()</code></p>
<dt>&bull;</p>
<dd><code>qb_util_timespec_from_epoch_get()</code></dl>
</dl>
<p> <code>Basic Stopwatch</code></p>
<dl>
<dd>
<pre>* uint64_t elapsed1;
* uint64_t elapsed2;
* qb_util_stopwatch_t *sw = qb_util_stopwatch_create();
*
* qb_util_stopwatch_start(sw);
*
* usleep(sometime);
* qb_util_stopwatch_stop(sw);
* elapsed1 = qb_util_stopwatch_us_elapsed_get(sw);
*
* usleep(somemoretime);
* qb_util_stopwatch_stop(sw);
* elapsed2 = qb_util_stopwatch_us_elapsed_get(sw);
*
* qb_util_stopwatch_free(sw);
* </pre>
</dl>
<p> <code>Stopwatch with splits</code></p>
<dl>
<dd>Setup a stopwatch with space for 3 splits.</dl>
<pre>* uint64_t split;
* qb_util_stopwatch_t *sw = qb_util_stopwatch_create();
*
* qb_util_stopwatch_split_ctl(sw, 3, 0);
* qb_util_stopwatch_start(sw);
*
* usleep(sometime);
* qb_util_stopwatch_split(sw);
*
* usleep(somemoretime);
* qb_util_stopwatch_split(sw);
*
* usleep(somemoretime);
* qb_util_stopwatch_split(sw);
*
* idx = qb_util_stopwatch_split_last(sw);
* do {
* split = qb_util_stopwatch_time_split_get(sw, idx, idx);
* qb_log(LOG_INFO, &quot;split %d is %&quot;PRIu64&quot;&quot;, last, split);
* idx--;
* } while (split &gt; 0);
*
* split = qb_util_stopwatch_time_split_get(sw, 2, 1);
* qb_log(LOG_INFO, &quot;time between second and third split is %&quot;PRIu64&quot;&quot;, split);
*
* qb_util_stopwatch_free(sw);
* </pre>
<p>&nbsp;<wbr></p>
<h2>Macro Definition Documentation</h2>
<h3>#define QB_UTIL_SW_OVERWRITE 0x01</h3>
<h2>Typedef Documentation</h2>
<h3>typedef struct qb_thread_lock_s <code>qb_thread_lock_t</code></h3>
<h3>typedef void(* qb_util_log_fn_t)(const char *file_name, int32_t file_line, int32_t severity, const char *msg)</h3>
<h3>typedef struct qb_util_stopwatch <code>qb_util_stopwatch_t</code></h3>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>qb_thread_lock_type_t</code></h3>
<p>QB_THREAD_LOCK_SHORT is a short term lock (spinlock if available on your system) QB_THREAD_LOCK_LONG is a mutex. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>QB_THREAD_LOCK_SHORT </i></p>
<dd>
<dt><i>QB_THREAD_LOCK_LONG </i></p>
<dd></dl>
<h2>Function Documentation</h2>
<h3>char* qb_strerror_r (interrnum, char *buf, size_tbuflen)</h3>
<p>strerror_r replacement.</p>
<h3>int32_t qb_thread_lock (<code>qb_thread_lock_t</code> *tl)</h3>
<p>Calls either pthread_mutex_lock() or pthread_spin_lock().</p>
<h3><code>qb_thread_lock_t</code>* qb_thread_lock_create (<code>qb_thread_lock_type_t</code>type)</h3>
<p>Create a new lock of the given type. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>type</i> QB_THREAD_LOCK_SHORT == spinlock (where available, else mutex) QB_THREAD_LOCK_LONG == mutex</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>pointer to qb_thread_lock_type_t or NULL on error.</dl>
<h3>int32_t qb_thread_lock_destroy (<code>qb_thread_lock_t</code> *tl)</h3>
<p>Calls either pthread_mutex_destro() or pthread_spin_destroy().</p>
<h3>int32_t qb_thread_trylock (<code>qb_thread_lock_t</code> *tl)</h3>
<p>Calls either pthread_mutex_trylock() or pthread_spin_trylock().</p>
<h3>int32_t qb_thread_unlock (<code>qb_thread_lock_t</code> *tl)</h3>
<p>Calls either pthread_mutex_unlock() or pthread_spin_unlock.</p>
<h3>void qb_timespec_add_ms (struct timespec *ts, int32_tms)</h3>
<p>Add milliseconds onto the timespec. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ts</i> the ts to add to<br />
 <i>ms</i> the amount of milliseconds to increment ts</dl>
<h3>uint64_t qb_util_nano_current_get (void)</h3>
<p>Get the current number of nano secounds produced by the systems incrementing clock (CLOCK_MONOTOMIC if available).</p>
<h3>uint64_t qb_util_nano_from_epoch_get (void)</h3>
<p>Get the time in nano seconds since epoch.</p>
<h3>uint64_t qb_util_nano_monotonic_hz (void)</h3>
<p>Get the frequence of the clock used in <code>qb_util_nano_current_get()</code>.</p>
<h3>void qb_util_set_log_function (<code>qb_util_log_fn_t</code>fn)</h3>
<p>Use this function to output libqb internal log message as you wish.</p>
<h3><code>qb_util_stopwatch_t</code>* qb_util_stopwatch_create (void)</h3>
<p>Create a Stopwatch (to time operations)</p>
<h3>void qb_util_stopwatch_free (<code>qb_util_stopwatch_t</code> *sw)</h3>
<p>Free the stopwatch.</p>
<h3>float qb_util_stopwatch_sec_elapsed_get (<code>qb_util_stopwatch_t</code> *sw)</h3>
<p>Get the elapsed time in seconds. (it must have been started and stopped).</p>
<h3>uint64_t qb_util_stopwatch_split (<code>qb_util_stopwatch_t</code> *sw)</h3>
<p>Create a new time split (or lap time) </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>sw</i> the stopwatch</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>the</i> relative split time in micro seconds<br />
 <i>0</i> if no more splits available</dl>
<h3>int32_t qb_util_stopwatch_split_ctl (<code>qb_util_stopwatch_t</code> *sw, uint32_tmax_splits, uint32_toptions)</h3>
<p><code>Parameters:</code></p>
<dl>
<dd><i>sw</i> the stopwatch<br />
 <i>max_splits</i> maximum number of time splits<br />
 <i>options</i> (0 or QB_UTIL_SW_OVERWRITE )</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>0</i> on success<br />
 <i>-errno</i> on failure</dl>
<h3>uint32_t qb_util_stopwatch_split_last (<code>qb_util_stopwatch_t</code> *sw)</h3>
<p>Get the last split index to be used by <code>qb_util_stopwatch_time_split_get()</code> </p>
<p> <code>Note:</code></p>
<dl>
<dd>this is zero based</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>sw</i> the stopwatch</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the last entry index</dl>
<h3>void qb_util_stopwatch_start (<code>qb_util_stopwatch_t</code> *sw)</h3>
<p>Start the stopwatch. This also acts as a reset. Essentially it sets the starting time and clears the splits.</p>
<h3>void qb_util_stopwatch_stop (<code>qb_util_stopwatch_t</code> *sw)</h3>
<p>Stop the stopwatch. This just allows you to get the elapsed time. So you can call this multiple times. Do not call <code>qb_util_stopwatch_start()</code> unless you want to reset the stopwatch.</p>
<h3>uint64_t qb_util_stopwatch_time_split_get (<code>qb_util_stopwatch_t</code> *sw, uint32_treceint, uint32_tolder)</h3>
<p>Read the time split (in us) from &#8216;receint&#8217; to &#8216;older&#8217;. If older == receint then the cumulated split will be returned (from the stopwatch start). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>sw</i> the stopwatch<br />
 <i>receint</i> split<br />
 <i>older</i> split</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>the</i> split time in micro seconds<br />
 <i>0</i> if not a valid split</dl>
<h3>uint64_t qb_util_stopwatch_us_elapsed_get (<code>qb_util_stopwatch_t</code> *sw)</h3>
<p>Get the elapsed time in micro seconds. (it must have been started and stopped).</p>
<h3>void qb_util_timespec_from_epoch_get (struct timespec *ts)</h3>
<p>Get the time in timespec since epoch. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ts</i> (out) the timespec</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>status (0 == ok, -errno on error)</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libqb from the source code.</p>
