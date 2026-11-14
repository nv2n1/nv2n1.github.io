---
title: "tk_getuserinactivetime(3)"
name: "tk_getuserinactivetime"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getuserinactivetime/"
description: "Tk_GetUserInactiveTime, Tk_ResetUserInactiveTime – discover user inactivity time"
---

<p>Tk_GetUserInactiveTime, Tk_ResetUserInactiveTime &#8211; discover user inactivity time </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
long
<code>Tk_GetUserInactiveTime(</code><i>display</i><code>)</code>
<code>Tk_GetUserInactiveTime(</code><i>display</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Display <i>*display</i> (in) The display on which the user inactivity timer is to be queried or reset. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_GetUserInactiveTime</code> returns the number of milliseconds that have passed since the last user interaction (usually via keyboard or mouse) with the respective display. On systems and displays that do not support querying the user inactiviy time, <code>-1</code> is returned. <code>Tk_GetUserInactiveTime</code> resets the user inactivity timer of the given display to zero. On windowing systems that do not support multiple displays <i>display</i> can be passed as <code>NULL</code>. </p>
<h2>Keywords</h2>
<p>idle, inactive</p>
