---
title: "ecore_time_group(3)"
name: "ecore_time_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_time_group/"
description: "Ecore Time Functions – Functions that deal with time."
---

<p>Ecore Time Functions &#8211; Functions that deal with time. </p>
<h3>Functions</h3>
<p>EAPI double <code>ecore_time_get</code> (void)<br />
 <i>Retrieves the current system time as a floating point value in seconds. </i><br />
 EAPI <code>Ecore_Timer</code> * <code>ecore_timer_add</code> (double in, int(*func)(void *data), const void *data)<br />
 <i>Creates a timer to call the given function in the given period of time. </i><br />
 EAPI void * <code>ecore_timer_del</code> (<code>Ecore_Timer</code> *timer)<br />
 <i>Delete the specified timer from the timer list. </i><br />
 EAPI void <code>ecore_timer_interval_set</code> (<code>Ecore_Timer</code> *timer, double in)<br />
 <i>Change the interval the timer ticks of. </i><br />
 EAPI void <code>ecore_timer_delay</code> (<code>Ecore_Timer</code> *timer, double add)<br />
 <i>Add some delay for the next occurence of a timer. </i><br />
 EAPI double <code>ecore_timer_pending_get</code> (<code>Ecore_Timer</code> *timer)<br />
 <i>Get the pending time regarding a timer. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with time. </p>
<p> These functions include those that simply retrieve it in a given format, and those that create events based on it.</p>
<h2>Function Documentation</h2>
<h3>EAPI double ecore_time_get (void)</h3>
<p>Retrieves the current system time as a floating point value in seconds. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of seconds since 12.00AM 1st January 1970.</dl>
<p> Referenced by ecore_evas_fb_new(), ecore_timer_add(), and ecore_timer_pending_get().</p>
<h3>EAPI <code>Ecore_Timer</code>* ecore_timer_add (double in, int(*)(void *data) func, const void * data)</h3>
<p>Creates a timer to call the given function in the given period of time. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>in</i> The interval in seconds.<br />
 <i>func</i> The given function. If func returns 1, the timer is rescheduled for the next interval in.<br />
 <i>data</i> Data to pass to func when it is called.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A timer object on success. NULL on failure.</dl>
<p> This function adds a timer and returns its handle on success and NULL on failure. The function func will be called every @ seconds. The function will be passed the data pointer as its parameter. </p>
<p> When the timer func is called, it must return a value of either 1 (or ECORE_CALLBACK_RENEW) or 0 (or ECORE_CALLBACK_CANCEL). If it returns 1, it will be called again at the next tick, or if it returns 0 it will be deleted automatically making any references/handles for it invalid. </p>
<p> References ecore_time_get(). </p>
<p> Referenced by ecore_animator_add(), ecore_animator_frametime_set(), and ecore_exe_kill().</p>
<h3>EAPI void* ecore_timer_del (<code>Ecore_Timer</code> * timer)</h3>
<p>Delete the specified timer from the timer list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>timer</i> The timer to delete.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer set for the timer when <code>ecore_timer_add</code> was called. NULL is returned if the function is unsuccessful.</dl>
<p> Note: timer must be a valid handle. If the timer function has already returned 0, the handle is no longer valid (and does not need to be delete). </p>
<p> Referenced by ecore_animator_frametime_set(), ecore_exe_free(), and ecore_exe_kill().</p>
<h3>EAPI void ecore_timer_delay (<code>Ecore_Timer</code> * timer, double add)</h3>
<p>Add some delay for the next occurence of a timer. </p>
<p> This doesn&#8217;t affect the interval of a timer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>timer</i> The timer to change.<br />
 <i>add</i> The dalay to add to the next iteration.</dl>
<h3>EAPI void ecore_timer_interval_set (<code>Ecore_Timer</code> * timer, double in)</h3>
<p>Change the interval the timer ticks of. </p>
<p> If set during a timer call, this will affect the next interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>timer</i> The timer to change.<br />
 <i>in</i> The interval in seconds.</dl>
<h3>EAPI double ecore_timer_pending_get (<code>Ecore_Timer</code> * timer)</h3>
<p>Get the pending time regarding a timer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>timer</i> The timer to learn from.</dl>
<p> References ecore_time_get().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
