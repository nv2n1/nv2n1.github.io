---
title: "xmimsetvalues(3)"
name: "xmimsetvalues"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmimsetvalues/"
description: "XmImSetValues — An input manager function that updates attributes of an input context"
---

<p><code>XmImSetValues</code> &#8212; An input manager function that updates attributes of an input context</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/XmIm.h&gt;
<code>void XmImSetValues</code>(
<code>Widget widget</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>,
);</pre>
<h2>Description</h2>
<p><code>XmImSetValues</code> updates attributes of the input context associated with the specified widget. The <i>arglist</i> argument is a list of attribute/value pairs for the input context. This function passes the attributes and values to <code>XICSetValues</code>. The initial call to this routine should pass in all of the input context attributes. Thereafter, the application programmer calls <code>XmImSetValues</code>, for an XIC, only if a value has changed. </p>
<p> If the previous parameters for the widget&#8217;s XIC do not allow the previously registered XIC to be reused, that XIC will be unregistered, and a new one will be created and registered with the widget. Note that sharing of data is preserved. </p>
<p> Note that the Text and TextField widgets call the <code>XmImSetValues</code> function when they receive focus. Therefore, further calls to the <code>XmImSetValues</code> function for these widgets are unnecessary.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget registered with the input manager</p>
<dt><i>arglist</i></p>
<dd>Specifies the list of attribute/value pairs to be passed to <code>XICSetValues</code>; the following attributes are accepted: <code>XmNpreeditStartCallback</code> <code>XmNpreeditDoneCallback</code> <code>XmNpreeditDrawCallback</code> and <code>XmNpreeditCaretCallback</code>. These attributes accept an accompanying value of type pointer to structure of type <code>XIMCallback</code>.</p>
<dd>These callbacks are used only when the <code>XmNpreeditType</code> resource of the relevant <code>VendorShell</code> has the &quot;onthespot&quot; value, and that the XIM supports <code>XIMPreeditCallbacks</code> input style. These values are ignored if the condition is not met.</p>
<dd>For each of these callbacks, if the callback value is not set by this function, no action will be taken when the Input Method tries to call this callback. Refer to the &quot;Xlib &#8211; C Language X Interface, X Version 11, Release 6,&quot; Chapter 13 for the detail of these callbacks.</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/values pairs in the argument list (<i>arglist)</i></dl>
<p> Resources that can be set for the input context include:</p>
<dl COMPACT>
<dt><code>XmNbackground</code></p>
<dd>Specifies the pixel value for the background color.</p>
<dt><code>XmNbackgroundPixmap</code></p>
<dd>Specifies a pixmap for tiling the background.</p>
<dt><code>XmNfontList</code></p>
<dd>Specifies the font list used by the widget. The input method uses the first occurrence of a font set tagged with <code>XmFONTLIST_DEFAULT_TAG</code>. If no such instance is found, the first font set in the font list is used. If the font list does not contain a font set, a value is not passed to <code>XICSetValues</code>.</p>
<dt><code>XmNforeground</code></p>
<dd>Specifies the pixel value for the foreground color.</p>
<dt><code>XmNlineSpace</code></p>
<dd>Specifies the line spacing used in the pre-edit window.</p>
<dt><code>XmNrenderTable</code></p>
<dd>Specifies the render table used by the widget.</p>
<dt><code>XmNspotLocation</code></p>
<dd>Specifies the <i>x</i> and <i>y</i> coordinates of the position where text will be inserted in the widget handling input, whose input method style is <code>&quot;OverTheSpot&quot;</code>. The <i>y</i> coordinate is the position of the baseline used by the current text line.</dl>
<p> The caller may also pass any other vendor-defined resources to this function. For additional information on the internationalization interface, see the Xlib documentation.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmimsetfocusvalues/">XmImSetFocusValues</a></code>(3), <code><a href="/docs/linux/man/3-xmimvasetfocusvalues/">XmImVaSetFocusValues</a></code>(3), and <code><a href="/docs/linux/man/3-xmimvasetvalues/">XmImVaSetValues</a></code>(3).</p>
