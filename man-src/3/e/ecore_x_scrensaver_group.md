---
title: "ecore_x_scrensaver_group(3)"
name: "ecore_x_scrensaver_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_scrensaver_group/"
description: "X Shape extension – These functions use the shape extension of the X server to change shape of given windows."
---

<p>X Shape extension &#8211; These functions use the shape extension of the X server to change shape of given windows. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_x_screensaver_event_available_get</code> (void)<br />
 <i>Return whether the X server supports the ScrenSaver Extension. </i><br />
 EAPI void <code>ecore_x_screensaver_idle_time_prefetch</code> (void)<br />
 <i>Sends the QueryInfo request. </i><br />
 EAPI void <code>ecore_x_screensaver_idle_time_fetch</code> (void)<br />
 <i>Gets the reply of the QueryInfo request sent by </i><code>ecore_x_get_screensaver_prefetch()</code>.<br />
 EAPI int <code>ecore_x_screensaver_idle_time_get</code> (void)<br />
 <i>Get the number of seconds since the last input was received. </i><br />
 EAPI void <code>ecore_x_screensaver_set</code> (int timeout, int interval, int blank, int expose)<br />
 <i>Set the parameters of the screen saver. </i><br />
 EAPI void <code>ecore_x_get_screensaver_prefetch</code> (void)<br />
 <i>Sends the GetScreenSaver request. </i><br />
 EAPI void <code>ecore_x_get_screensaver_fetch</code> (void)<br />
 <i>Gets the reply of the GetScreenSaver request sent by </i><code>ecore_x_get_screensaver_prefetch()</code>.<br />
 EAPI void <code>ecore_x_screensaver_timeout_set</code> (int timeout)<br />
 <i>Set the timeout of the screen saver. </i><br />
 EAPI int <code>ecore_x_screensaver_timeout_get</code> (void)<br />
 <i>Get the timeout of the screen saver. </i><br />
 EAPI void <code>ecore_x_screensaver_interval_set</code> (int interval)<br />
 <i>Set the interval of the screen saver. </i><br />
 EAPI int <code>ecore_x_screensaver_interval_get</code> (void)<br />
 <i>Get the interval of the screen saver. </i><br />
 EAPI void <code>ecore_x_screensaver_blank_set</code> (int blank)<br />
 <i>Set the screen blanking. </i><br />
 EAPI int <code>ecore_x_screensaver_blank_get</code> (void)<br />
 <i>Get the screen blanking. </i><br />
 EAPI void <code>ecore_x_screensaver_expose_set</code> (int expose)<br />
 <i>Set the screen save control values. </i><br />
 EAPI int <code>ecore_x_screensaver_expose_get</code> (void)<br />
 <i>Get the screen save control values. </i><br />
 EAPI void <code>ecore_x_screensaver_event_listen_set</code> (int on)<br />
 <i>Specifies if the Screen Saver NotifyMask event should be generated. </i></p>
<h2>Detailed Description</h2>
<p>These functions use the shape extension of the X server to change shape of given windows.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_x_screensaver_blank_get (void)</h3>
<p>Get the screen blanking. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The blanking.</dl>
<p> Get the screen blanking. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_get_screensaver_prefetch()</code>, which sends the GetScreenSaver request, then <code>ecore_x_get_screensaver_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_screensaver_blank_set (int blank)</h3>
<p>Set the screen blanking. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>blank</i> The blank to set.</dl>
<p> blank specifies how to enable screen blanking. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_get_screensaver_prefetch()</code>, which sends the GetScreenSaver request, then <code>ecore_x_get_screensaver_fetch()</code>, which gets the reply.</p>
<h3>EAPI int ecore_x_screensaver_event_available_get (void)</h3>
<p>Return whether the X server supports the ScrenSaver Extension. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the X ScrenSaver Extension is available, 0 otherwise.</dl>
<p> Return 1 if the X server supports the ScrenSaver Extension version 1.0, 0 otherwise.</p>
<h3>EAPI void ecore_x_screensaver_event_listen_set (int on)</h3>
<p>Specifies if the Screen Saver NotifyMask event should be generated. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> 0 to disable the generation of the event, otherwise enable it.</dl>
<p> Specifies if the Screen Saver NotifyMask event on the screen associated with drawable should be generated for this client. If on is set to 0, the generation is disabled, otherwise, it is enabled.</p>
<h3>EAPI int ecore_x_screensaver_expose_get (void)</h3>
<p>Get the screen save control values. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The expose.</dl>
<p> Get the screen save control values. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_get_screensaver_prefetch()</code>, which sends the GetScreenSaver request, then <code>ecore_x_get_screensaver_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_screensaver_expose_set (int expose)</h3>
<p>Set the screen save control values. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>expose</i> The expose to set.</dl>
<p> Set the screen save control values. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_get_screensaver_prefetch()</code>, which sends the GetScreenSaver request, then <code>ecore_x_get_screensaver_fetch()</code>, which gets the reply.</p>
<h3>EAPI int ecore_x_screensaver_idle_time_get (void)</h3>
<p>Get the number of seconds since the last input was received. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of seconds.</dl>
<p> Get the number of milliseconds since the last input was received from the user on any of the input devices. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_get_screensaver_prefetch()</code>, which sends the GetScreenSaver request, then <code>ecore_x_get_screensaver_fetch()</code>, which gets the reply.</p>
<h3>EAPI int ecore_x_screensaver_interval_get (void)</h3>
<p>Get the interval of the screen saver. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The interval.</dl>
<p> Get the interval, in seconds, between screen saver alterations. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_get_screensaver_prefetch()</code>, which sends the GetScreenSaver request, then <code>ecore_x_get_screensaver_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_screensaver_interval_set (int interval)</h3>
<p>Set the interval of the screen saver. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> The interval to set.</dl>
<p> Set the interval, in seconds, between screen saver alterations. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_get_screensaver_prefetch()</code>, which sends the GetScreenSaver request, then <code>ecore_x_get_screensaver_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_screensaver_set (int timeout, int interval, int blank, int expose)</h3>
<p>Set the parameters of the screen saver. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>timeout</i> The timeout, in second.<br />
 <i>interval</i> The interval, in seconds.<br />
 <i>blank</i> 0 to disable screen blanking, otherwise enable it.<br />
 <i>expose</i> Allow Expose generation event or not.</dl>
<p> Set the parameters of the screen saver. timeout is the timeout, in seconds, until the screen saver turns on. interval is the interval, in seconds, between screen saver alterations. blank specifies how to enable screen blanking. expose specifies the screen save control values.</p>
<h3>EAPI int ecore_x_screensaver_timeout_get (void)</h3>
<p>Get the timeout of the screen saver. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The timeout.</dl>
<p> Get the timeout, in seconds, until the screen saver turns on. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_get_screensaver_prefetch()</code>, which sends the GetScreenSaver request, then <code>ecore_x_get_screensaver_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_screensaver_timeout_set (int timeout)</h3>
<p>Set the timeout of the screen saver. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>timeout</i> The timeout to set.</dl>
<p> Set the timeout, in seconds, until the screen saver turns on. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_get_screensaver_prefetch()</code>, which sends the GetScreenSaver request, then <code>ecore_x_get_screensaver_fetch()</code>, which gets the reply.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
