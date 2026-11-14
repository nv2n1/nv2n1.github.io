---
title: "xtpopupspringloaded(3)"
name: "xtpopupspringloaded"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtpopupspringloaded/"
description: "XtPopup, XtPopupSpringLoaded, XtCallbackNone, XtCallbackNonexclusive, XtCallbackExclusive – map a pop-up"
---

<p>XtPopup, XtPopupSpringLoaded, XtCallbackNone, XtCallbackNonexclusive, XtCallbackExclusive &#8211; map a pop-up </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtPopup(Widget <i>popup_shell</i>, XtGrabKind <i>grab_kind</i>);</p>
<dd>void XtPopupSpringLoaded(Widget <i>popup_shell</i>);</p>
<dd>void XtCallbackNone(Widget <i>w</i>, XtPointer <i>client_data</i>, XtPointer <i>call_data</i>);</p>
<dd>void XtCallbackNonexclusive(Widget <i>w</i>, XtPointer <i>client_data</i>, XtPointer <i>call_data</i>);</p>
<dd>void XtCallbackExclusive(Widget <i>w</i>, XtPointer <i>client_data</i>, XtPointer <i>call_data</i>);</dl>
<h2>Actions</h2>
<dl COMPACT>
<dd>void XtMenuPopup(String <i>shell_name</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>call_data</i></p>
<dd>Specifies the callback data, which is not used by this procedure.</p>
<dt><i>client_data</i></p>
<dd>Specifies the pop-up shell.</p>
<dt><i>grab_kind</i></p>
<dd>Specifies the way in which user events should be constrained.</p>
<dt><i>popup_shell</i></p>
<dd>Specifies the widget shell.</p>
<dt><i>w</i></p>
<dd>Specifies the widget.</dl>
<h2>Description</h2>
<p>The <code>XtPopup</code> function performs the following:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Calls <code>XtCheckSubclass</code> to ensure popup_shell is a subclass of <code>Shell</code>.</p>
<dt>&bull;</p>
<dd>Generates an error if the shell&#8217;s popped_up field is already <code>True</code>.</p>
<dt>&bull;</p>
<dd>Calls the callback procedures on the shell&#8217;s popup_callback list.</p>
<dt>&bull;</p>
<dd>Sets the shell popped_up field to <code>True</code>, the shell spring_loaded field to <code>False</code>, and the shell grab_kind field from grab_kind.</p>
<dt>&bull;</p>
<dd>If the shell&#8217;s create_popup_child field is non-NULL, <code>XtPopup</code> calls it with popup_shell as the parameter.</p>
<dt>&bull;</p>
<dd>If grab_kind is either <code>XtGrabNonexclusive</code> or <code>XtGrabExclusive</code>, it calls:</dl>
<dl COMPACT>
<dd>
<pre>XtAddGrab(popup_shell, (grab_kind == XtGrabExclusive), False)</pre>
</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>Calls <code>XtRealizeWidget</code> with popup_shell specified.</p>
<dt>&bull;</p>
<dd>Calls <code>XMapWindow</code> with popup_shell specified.</dl>
<p> The <code>XtPopupSpringLoaded</code> function performs exactly as <code>XtPopup</code> except that it sets the shell <i>spring_loaded</i> field to <code>True</code> and always calls <code>XtAddGrab</code> with <i>exclusive</i> <code>True</code> and <i>spring_loaded</i> <code>True</code>. </p>
<p> The <code>XtCallbackNone</code>, <code>XtCallbackNonexclusive</code>, and <code>XtCallbackExclusive</code> functions call <code>XtPopup</code> with the shell specified by the client data argument and grab_kind set as the name specifies. <code>XtCallbackNone</code>, <code>XtCallbackNonexclusive</code>, and <code>XtCallbackExclusive</code> specify <code>XtGrabNone</code>, <code>XtGrabNonexclusive</code>, and <code>XtGrabExclusive</code>, respectively. Each function then sets the widget that executed the callback list to be insensitive by using <code>XtSetSensitive</code>. Using these functions in callbacks is not required. In particular, an application must provide customized code for callbacks that create pop-up shells dynamically or that must do more than desensitizing the button. </p>
<p> <code>XtMenuPopup</code> is known to the translation manager, which must perform special actions for spring-loaded pop-ups. Calls to <code>XtMenuPopup</code> in a translation specification are mapped into calls to a nonexported action procedure, and the translation manager fills in parameters based on the event specified on the left-hand side of a translation. </p>
<p> If <code>XtMenuPopup</code> is invoked on <code>ButtonPress</code> (possibly with modifiers), the translation manager pops up the shell with grab_kind set to <code>XtGrabExclusive</code> and spring_loaded set to <code>True</code>. If <code>XtMenuPopup</code> is invoked on <code>EnterWindow</code> (possibly with modifiers), the translation manager pops up the shell with grab_kind set to <code>XtGrabNonexclusive</code> and spring_loaded set to <code>False</code>. Otherwise, the translation manager generates an error. When the widget is popped up, the following actions occur:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Calls <code>XtCheckSubclass</code> to ensure popup_shell is a subclass of <code>Shell</code>.</p>
<dt>&bull;</p>
<dd>Generates an error if the shell&#8217;s popped_up field is already <code>True</code>.</p>
<dt>&bull;</p>
<dd>Calls the callback procedures on the shell&#8217;s popup_callback list.</p>
<dt>&bull;</p>
<dd>Sets the shell popped_up field to <code>True</code> and the shell grab_kind and spring_loaded fields appropriately.</p>
<dt>&bull;</p>
<dd>If the shell&#8217;s create_popup_child field is non-NULL, it is called with popup_shell as the parameter.</p>
<dt>&bull;</p>
<dd>Calls:</dl>
<dl COMPACT>
<dd>
<pre>XtAddGrab(popup_shell, (grab_kind == XtGrabExclusive), spring_loaded)</pre>
</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>Calls <code>XtRealizeWidget</code> with popup_shell specified.</p>
<dt>&bull;</p>
<dd>Calls <code>XMapWindow</code> with popup_shell specified.</dl>
<p> (Note that these actions are the same as those for <code>XtPopup</code>.) <code>XtMenuPopup</code> tries to find the shell by searching the widget tree starting at the parent of the widget in which it is invoked. If it finds a shell with the specified name in the pop-up children of that parent, it pops up the shell with the appropriate parameters. Otherwise, it moves up the parent chain as needed. If <code>XtMenuPopup</code> gets to the application widget and cannot find a matching shell, it generates an error.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtcreatepopupshell/">XtCreatePopupShell</a>(3), <a href="/docs/linux/man/3-xtpopdown/">XtPopdown</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
