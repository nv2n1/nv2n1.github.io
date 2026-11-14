---
title: "xmismotifwmrunning(3)"
name: "xmismotifwmrunning"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmismotifwmrunning/"
description: "XmIsMotifWMRunning — A function that determines whether the window manager is running"
---

<p><code>XmIsMotifWMRunning</code> &#8212; A function that determines whether the window manager is running</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmIsMotifWMRunning</code>(
<code>Widget shell</code>);</pre>
<h2>Description</h2>
<p><code>XmIsMotifWMRunning</code> lets a user know whether the Motif Window Manager is running on a screen that contains a specific widget hierarchy. This function first sees whether the <code>_MOTIF_WM_INFO</code> property is present on the root window of the shell&#8217;s screen. If it is, its window field is used to query for the presence of the specified window as a child of root.</p>
<dl COMPACT>
<dt><i>shell</i></p>
<dd>Specifies the shell whose screen will be tested for <code>mwm</code>&#8216;s presence.</dl>
<h2>Return</h2>
<p>Returns True if MWM is running.</p>
