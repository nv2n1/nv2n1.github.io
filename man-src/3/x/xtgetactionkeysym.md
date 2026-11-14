---
title: "xtgetactionkeysym(3)"
name: "xtgetactionkeysym"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgetactionkeysym/"
description: "XtGetActionKeysym – obtain corresponding keysym"
---

<p>XtGetActionKeysym &#8211; obtain corresponding keysym </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>KeySym XtGetActionKeysym(XEvent* <i>event</i>, Modifiers* <i>modifiers_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>event</i></p>
<dd>Specifies the event pointer passed to the action procedure by the Intrinsics.</p>
<dt><i>modifiers_return</i></p>
<dd>Returns the modifiers that caused the match, if non-NULL.</dl>
<h2>Description</h2>
<p>If <code>XtGetActionKeysym</code> is called after an action procedure has been invoked by the Intrinsics and before that action procedure returns, and if the event pointer has the same value as the event pointer passed to that action routine, and if the event is a <code>KeyPress</code> or <code>KeyRelease</code> event, then <code>XtGetActionKeysym</code> returns the KeySym that matched the final event specification in the translation table and, if <i>modifiers_return</i> is non-NULL, the modifier state actually used to generate this KeySym; otherwise, if the event is a <code>KeyPress</code> or <code>KeyRelease</code> event, then <code>XtGetActionKeysym</code> calls <code>XtTranslateKeycode</code> and returns the results; else it returns <code>NoSymbol</code> and does not examine <i>modifiers_return</i>.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
