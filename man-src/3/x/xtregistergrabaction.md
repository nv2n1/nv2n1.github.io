---
title: "xtregistergrabaction(3)"
name: "xtregistergrabaction"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtregistergrabaction/"
description: "XtRegisterGrabAction – register button and key grabs"
---

<p>XtRegisterGrabAction &#8211; register button and key grabs </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtRegisterGrabAction(XtActionProc <i>action_proc</i>, Boolean <i>owner_events</i>, unsigned int <i>event_mask</i>, int <i>pointer_mode</i>, int <i>keyboard_mode</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>action_proc</i></p>
<dd>Specifies the action procedure to search for in translation tables.</p>
<dt><i>action</i></p>
<dd>
<dt><i>event</i></p>
<dd>
<dt><i>params</i></p>
<dd>
<dt><i>num_params</i></p>
<dd>Specify arguments to <code>XtGrabButton</code> or <code>XtGrabKey</code></dl>
<h2>Description</h2>
<p><code>XtRegisterGrabAction</code> adds the specified <i>action_proc</i> to a list known to the translation manager.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
