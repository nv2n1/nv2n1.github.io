---
title: "ecore_x_dpms_group(3)"
name: "ecore_x_dpms_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_dpms_group/"
description: "X DPMS Extension Functions – Functions related to the X DPMS extension."
---

<p>X DPMS Extension Functions &#8211; Functions related to the X DPMS extension. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_x_dpms_query</code> (void)<br />
 <i>Checks if the DPMS extension is available or not. </i><br />
 EAPI void <code>ecore_x_dpms_capable_get_prefetch</code> (void)<br />
 <i>Sends the DPMSCapable request. </i><br />
 EAPI void <code>ecore_x_dpms_capable_get_fetch</code> (void)<br />
 <i>Gets the reply of the DPMSCapable request sent by </i><code>ecore_x_dpms_capable_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_dpms_capable_get</code> (void)<br />
 <i>Checks if the X server is capable of DPMS. </i><br />
 EAPI void <code>ecore_x_dpms_enable_get_prefetch</code> (void)<br />
 <i>Sends the DPMSInfo request. </i><br />
 EAPI void <code>ecore_x_dpms_enable_get_fetch</code> (void)<br />
 <i>Gets the reply of the DPMSInfo request sent by </i><code>ecore_x_dpms_enable_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_dpms_enable_get</code> (void)<br />
 <i>Checks the DPMS state of the display. </i><br />
 EAPI void <code>ecore_x_dpms_enabled_set</code> (int enabled)<br />
 <i>Sets the DPMS state of the display. </i><br />
 EAPI int <code>ecore_x_dpms_timeouts_set</code> (unsigned int standby, unsigned int suspend, unsigned int off)<br />
 <i>Sets the timeouts. </i><br />
 EAPI void <code>ecore_x_dpms_timeouts_get_prefetch</code> (void)<br />
 <i>Sends the DPMSGetTimeouts request. </i><br />
 EAPI void <code>ecore_x_dpms_timeouts_get_fetch</code> (void)<br />
 <i>Gets the reply of the DPMSGetTimeouts request sent by </i><code>ecore_x_dpms_timeouts_get_prefetch()</code>.<br />
 EAPI void <code>ecore_x_dpms_timeouts_get</code> (unsigned int *standby, unsigned int *suspend, unsigned int *off)<br />
 <i>Gets the timeouts. </i><br />
 EAPI unsigned int <code>ecore_x_dpms_timeout_standby_get</code> (void)<br />
 <i>Returns the amount of time of inactivity before standby mode is invoked. </i><br />
 EAPI unsigned int <code>ecore_x_dpms_timeout_suspend_get</code> (void)<br />
 <i>Returns the amount of time of inactivity before the second level of power saving is invoked. </i><br />
 EAPI unsigned int <code>ecore_x_dpms_timeout_off_get</code> (void)<br />
 <i>Returns the amount of time of inactivity before the third and final level of power saving is invoked. </i><br />
 EAPI void <code>ecore_x_dpms_timeout_standby_set</code> (unsigned int new_standby)<br />
 <i>Sets the standby timeout (in unit of seconds). </i><br />
 EAPI void <code>ecore_x_dpms_timeout_suspend_set</code> (unsigned int new_suspend)<br />
 <i>Sets the suspend timeout (in unit of seconds). </i><br />
 EAPI void <code>ecore_x_dpms_timeout_off_set</code> (unsigned int new_off)<br />
 <i>Sets the off timeout (in unit of seconds). </i><br />
 EAPI int <code>ecore_x_dpms_enabled_get</code> (void)<br />
 <i>Checks the DPMS state of the display. </i></p>
<h2>Detailed Description</h2>
<p>Functions related to the X DPMS extension.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_x_dpms_capable_get (void)</h3>
<p>Checks if the X server is capable of DPMS. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the X server is capable of DPMS, 0 otherwise.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_dpms_capable_get_prefetch()</code>, which sends the DPMSCapable request, then <code>ecore_x_dpms_capable_get_fetch()</code>, which gets the reply. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the X server is capable of DPMS, 0 otherwise.</dl>
<h3>EAPI int ecore_x_dpms_enable_get (void)</h3>
<p>Checks the DPMS state of the display. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if DPMS is enabled, 0 otherwise.</dl>
<p> To use this function, you must call before, and in order, ecore_x_dpms_enapable_get_prefetch(), which sends the DPMSInfo request, then ecore_x_dpms_enapable_get_fetch(), which gets the reply.</p>
<h3>EAPI int ecore_x_dpms_enabled_get (void)</h3>
<p>Checks the DPMS state of the display. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if DPMS is enabled, 0 otherwise.</dl>
<h3>EAPI void ecore_x_dpms_enabled_set (int enabled)</h3>
<p>Sets the DPMS state of the display. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>enabled</i> 0 to disable DPMS characteristics of the server, enable it otherwise.</dl>
<h3>EAPI int ecore_x_dpms_query (void)</h3>
<p>Checks if the DPMS extension is available or not. </p>
<p> Checks if the X DPMS extension is available on the server. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the DPMS extension is available, 0 otherwise.</dl>
<p> Return 1 if the X server supports the DPMS Extension version 1.0, 0 otherwise. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the X DPMS extension is available, 0 otherwise.</dl>
<h3>EAPI unsigned int ecore_x_dpms_timeout_off_get (void)</h3>
<p>Returns the amount of time of inactivity before the third and final level of power saving is invoked. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The off timeout value.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_dpms_timeouts_get_prefetch()</code>, which sends the DPMSGetTimeouts request, then <code>ecore_x_dpms_timeouts_get_fetch()</code>, which gets the reply. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The off timeout value.</dl>
<h3>EAPI void ecore_x_dpms_timeout_off_set (unsigned int new_timeout)</h3>
<p>Sets the off timeout (in unit of seconds). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>off</i> Amount of time of inactivity before the monitor is shut off.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_dpms_timeouts_get_prefetch()</code>, which sends the DPMSGetTimeouts request, then <code>ecore_x_dpms_timeouts_get_fetch()</code>, which gets the reply. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>off</i> Amount of time of inactivity before the monitor is shut off.</dl>
<h3>EAPI unsigned int ecore_x_dpms_timeout_standby_get (void)</h3>
<p>Returns the amount of time of inactivity before standby mode is invoked. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The standby timeout value.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_dpms_timeouts_get_prefetch()</code>, which sends the DPMSGetTimeouts request, then <code>ecore_x_dpms_timeouts_get_fetch()</code>, which gets the reply. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The standby timeout value.</dl>
<h3>EAPI void ecore_x_dpms_timeout_standby_set (unsigned int new_timeout)</h3>
<p>Sets the standby timeout (in unit of seconds). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>new_standby</i> Amount of time of inactivity before standby mode will be invoked.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_dpms_timeouts_get_prefetch()</code>, which sends the DPMSGetTimeouts request, then <code>ecore_x_dpms_timeouts_get_fetch()</code>, which gets the reply. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>new_standby</i> Amount of time of inactivity before standby mode will be invoked.</dl>
<h3>EAPI unsigned int ecore_x_dpms_timeout_suspend_get (void)</h3>
<p>Returns the amount of time of inactivity before the second level of power saving is invoked. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The suspend timeout value.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_dpms_timeouts_get_prefetch()</code>, which sends the DPMSGetTimeouts request, then <code>ecore_x_dpms_timeouts_get_fetch()</code>, which gets the reply. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The suspend timeout value.</dl>
<h3>EAPI void ecore_x_dpms_timeout_suspend_set (unsigned int new_timeout)</h3>
<p>Sets the suspend timeout (in unit of seconds). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>suspend</i> Amount of time of inactivity before the screen is placed into suspend mode.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_dpms_timeouts_get_prefetch()</code>, which sends the DPMSGetTimeouts request, then <code>ecore_x_dpms_timeouts_get_fetch()</code>, which gets the reply. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>suspend</i> Amount of time of inactivity before the screen is placed into suspend mode.</dl>
<h3>EAPI void ecore_x_dpms_timeouts_get (unsigned int * standby, unsigned int * suspend, unsigned int * off)</h3>
<p>Gets the timeouts. </p>
<p> The values are in unit of seconds. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>standby</i> Amount of time of inactivity before standby mode will be invoked.<br />
 <i>suspend</i> Amount of time of inactivity before the screen is placed into suspend mode.<br />
 <i>off</i> Amount of time of inactivity before the monitor is shut off.</dl>
<h3>EAPI int ecore_x_dpms_timeouts_set (unsigned int standby, unsigned int suspend, unsigned int off)</h3>
<p>Sets the timeouts. </p>
<p> The values are in unit of seconds. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>standby</i> Amount of time of inactivity before standby mode will be invoked.<br />
 <i>suspend</i> Amount of time of inactivity before the screen is placed into suspend mode.<br />
 <i>off</i> Amount of time of inactivity before the monitor is shut off.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns always 1.</dl>
<p> The values are in unit of seconds. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>standby</i> Amount of time of inactivity before standby mode will be invoked.<br />
 <i>suspend</i> Amount of time of inactivity before the screen is placed into suspend mode.<br />
 <i>off</i> Amount of time of inactivity before the monitor is shut off.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
