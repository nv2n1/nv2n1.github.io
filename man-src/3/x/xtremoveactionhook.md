---
title: "xtremoveactionhook(3)"
name: "xtremoveactionhook"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtremoveactionhook/"
description: "XtAppAddActionHook, XtRemoveActionHook – register an action hook procedure"
---

<p>XtAppAddActionHook, XtRemoveActionHook &#8211; register an action hook procedure </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtActionHookId XtAppAddActionHook(XtAppContext <i>app_context</i>, XtActionHookProc <i>proc</i>, XtPointer <i>client_data</i>);</p>
<dd>void XtRemoveActionHook(XtActionHookId <i>id</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</p>
<dt><i>proc</i></p>
<dd>Specifies the action hook procedure.</p>
<dt><i>num_args</i></p>
<dd>Specifies the application-specific data to be passed to the action hook.</dl>
<h2>Description</h2>
<p><code>XtAppAddActionHook</code> adds the specified procedure to the front of a list maintained in the application context. In the future, when an action routine is about to be invoked for any widget in this application context, either through the translation manager or via <code>XtCallActionProc</code>, the action hohok procedures will be called in reverse order of registration jut prior to invoking the action routine. </p>
<p> Action hook procedures are removed automatically and the <code>XtActionHookId</code> s destroyed when the application context in which they were added is destroyed. </p>
<p> <code>XtRemoveActionHook</code> removes the specified action hook procedure from the list in which it was registered.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
