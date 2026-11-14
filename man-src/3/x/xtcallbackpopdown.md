---
title: "xtcallbackpopdown(3)"
name: "xtcallbackpopdown"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtcallbackpopdown/"
description: "XtPopdown, XtCallbackPopdown – unmap a pop-up"
---

<p>XtPopdown, XtCallbackPopdown &#8211; unmap a pop-up </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtPopdown(Widget <i>popup_shell</i>);</p>
<dd>void XtCallbackPopdown(Widget <i>w</i>, XtPointer <i>client_data</i>, XtPointer <i>call_data</i>);</dl>
<h2>Actions</h2>
<dl COMPACT>
<dd>void XtMenuPopdown(String <i>shell_name</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>call_data</i></p>
<dd>Specifies the callback data, which is not used by this procedure.</p>
<dt><i>client_data</i></p>
<dd>Specifies a pointer to the <code>XtPopdownID</code> structure.</p>
<dt><i>popup_shell</i></p>
<dd>Specifies the widget shell to pop down.</p>
<dt><i>shell_name</i></p>
<dd>Specifies the name of the widget shell to pop down.</p>
<dt><i>w</i></p>
<dd>Specifies the widget.</dl>
<h2>Description</h2>
<p>The <code>XtPopdown</code> function performs the following:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Calls <code>XtCheckSubclass</code> to ensure popup_shell is a subclass of <code>Shell</code>.</p>
<dt>&bull;</p>
<dd>Checks that popup_shell is currently popped_up; otherwise, it generates an error.</p>
<dt>&bull;</p>
<dd>Unmaps popup_shell&#8217;s window.</p>
<dt>&bull;</p>
<dd>If popup_shell&#8217;s grab_kind is either <code>XtGrabNonexclusive</code> or <code>XtGrabExclusive</code>, it calls <code>XtRemoveGrab</code>.</p>
<dt>&bull;</p>
<dd>Sets pop-up shell&#8217;s popped_up field to <code>False</code>.</p>
<dt>&bull;</p>
<dd>Calls the callback procedures on the shell&#8217;s popdown_callback list.</dl>
<p> The <code>XtCallbackPopdown</code> function casts the client data parameter to an <code>XtPopdownID</code> pointer: </p>
<dl COMPACT>
<dd>
<pre>typedef struct {
 Widget shell_widget;
 Widget enable_widget;
} XtPopdownIDRec, *XtPopdownID;</pre>
</dl>
<p> The shell_widget is the pop-up shell to pop down, and the enable_widget is the widget that was used to pop it up. </p>
<p> <code>XtCallbackPopdown</code> calls <code>XtPopdown</code> with the specified shell_widget and then calls <code>XtSetSensitive</code> to resensitize the enable_widget. </p>
<p> If a shell name is not given, <code>XtMenuPopdown</code> calls <code>XtPopdown</code> with the widget for which the translation is specified. If a shell_name is specified in the translation table, <code>XtMenuPopdown</code> tries to find the shell by looking up the widget tree starting at the parent of the widget in which it is invoked. If it finds a shell with the specified name in the pop-up children of that parent, it pops down the shell; otherwise, it moves up the parent chain as needed. If <code>XtMenuPopdown</code> gets to the application top-level shell widget and cannot find a matching shell, it generates an error.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtcreatepopupshell/">XtCreatePopupShell</a>(3), <a href="/docs/linux/man/3-xtpopup/">XtPopup</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
