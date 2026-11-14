---
title: "xtvacreatepopupshell(3)"
name: "xtvacreatepopupshell"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtvacreatepopupshell/"
description: "XtCreatePopupShell, XtVaCreatePopupShell – create a popup shell"
---

<p>XtCreatePopupShell, XtVaCreatePopupShell &#8211; create a popup shell </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Widget XtCreatePopupShell(const char *<i>name</i>, WidgetClass <i>widget_class</i>, Widget <i>parent</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);</p>
<dd>Widget XtVaCreatePopupShell(const char *<i>name</i>, WidgetClass <i>widget_class</i>, Widget <i>parent</i>, &#8230;);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>args</i></p>
<dd>Specifies the argument list to override the resource defaults.</p>
<dt><i>name</i></p>
<dd>Specifies the text name for the created shell widget.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of arguments in the argument list.</p>
<dt><i>parent</i></p>
<dd>Specifies the parent widget.</p>
<dt><i>widget_class</i></p>
<dd>Specifies the widget class pointer for the created shell widget.</p>
<dt><i>&#8230;</i></p>
<dd>Specifies the variable argument list to override the resource defaults.</dl>
<h2>Description</h2>
<p>The <code>XtCreatePopupShell</code> function ensures that the specified class is a subclass of <code>Shell</code> and, rather than using insert_child to attach the widget to the parent&#8217;s children list, attaches the shell to the parent&#8217;s pop-ups list directly. </p>
<p> A spring-loaded pop-up invoked from a translation table already must exist at the time that the translation is invoked, so the translation manager can find the shell by name. Pop-ups invoked in other ways can be created &#8220;on-the-fly&#8221; when the pop-up actually is needed. This delayed creation of the shell is particularly useful when you pop up an unspecified number of pop-ups. You can look to see if an appropriate unused shell (that is, not currently popped up) exists and create a new shell if needed.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtcreatewidget/">XtCreateWidget</a>(3), <a href="/docs/linux/man/3-xtpopdown/">XtPopdown</a>(3), <a href="/docs/linux/man/3-xtpopup/">XtPopup</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
