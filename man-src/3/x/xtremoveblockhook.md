---
title: "xtremoveblockhook(3)"
name: "xtremoveblockhook"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtremoveblockhook/"
description: "XtAppAddBlockHook, XtRemoveBlockHook – register a block hook procedure"
---

<p>XtAppAddBlockHook, XtRemoveBlockHook &#8211; register a block hook procedure </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtBlockHookId XtAppAddBlockHook(XtAppContext <i>app_context</i>, XtBlockHookProc <i>proc</i>, XtPointer <i>client_data</i>);</p>
<dd>void XtRemoveBlockHook(XtBlockHookId <i>id</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</p>
<dt><i>proc</i></p>
<dd>Specifies the block hook procedure.</p>
<dt><i>num_args</i></p>
<dd>Specifies the application-specific data to be passed to the block hook.</dl>
<h2>Description</h2>
<p><code>XtAppAddBlockHook</code> registers the specified procedure and returns an identifier for it. The hook is called at any time in the future when the Intrinsics are about to block pending some input. </p>
<p> Block hook procedures are removed automatically and the <code>XtBlockHookId</code> is destroyed when the application context in which they were added is destroyed. </p>
<p> <code>XtRemoveBlockHook</code> removes the specified block hook procedure from the list in which it was registered.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
