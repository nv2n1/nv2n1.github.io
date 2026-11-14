---
title: "tk_resizewindow-2(3)"
name: "tk_resizewindow-2"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_resizewindow-2/"
description: "Tk_ConfigureWindow, Tk_MoveWindow, Tk_ResizeWindow, Tk_MoveResizeWindow, Tk_SetWindowBorderWidth, Tk_ChangeWindowAttributes, Tk_SetWindowBackground, Tk_SetWindowBackgroundPixmap, Tk_SetWindowBorder..."
---

<p>Tk_ConfigureWindow, Tk_MoveWindow, Tk_ResizeWindow, Tk_MoveResizeWindow, Tk_SetWindowBorderWidth, Tk_ChangeWindowAttributes, Tk_SetWindowBackground, Tk_SetWindowBackgroundPixmap, Tk_SetWindowBorder, Tk_SetWindowBorderPixmap, Tk_SetWindowColormap, Tk_DefineCursor, Tk_UndefineCursor &#8211; change window configuration or attributes </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_ConfigureWindow</code>(<i>tkwin, valueMask, valuePtr</i>)
<code>Tk_MoveWindow</code>(<i>tkwin, x, y</i>)
<code>Tk_ResizeWindow</code>(<i>tkwin, width, height</i>)
<code>Tk_MoveResizeWindow</code>(<i>tkwin, x, y, width, height</i>)
<code>Tk_SetWindowBorderWidth</code>(<i>tkwin, borderWidth</i>)
<code>Tk_ChangeWindowAttributes</code>(<i>tkwin, valueMask, attsPtr</i>)
<code>Tk_SetWindowBackground</code>(<i>tkwin, pixel</i>)
<code>Tk_SetWindowBackgroundPixmap</code>(<i>tkwin, pixmap</i>)
<code>Tk_SetWindowBorder</code>(<i>tkwin, pixel</i>)
<code>Tk_SetWindowBorderPixmap</code>(<i>tkwin, pixmap</i>)
<code>Tk_SetWindowColormap</code>(<i>tkwin, colormap</i>)
<code>Tk_DefineCursor</code>(<i>tkwin, cursor</i>)
<code>Tk_UndefineCursor</code>(<i>tkwin</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window.</p>
<dd>unsigned int <i>valueMask</i> (in) OR-ed mask of values like <code>CWX</code> or <code>CWBorderPixel</code>, indicating which fields of <i>*valuePtr</i> or <i>*attsPtr</i> to use.</p>
<dd>XWindowChanges <i>*valuePtr</i> (in) Points to a structure containing new values for the configuration parameters selected by <i>valueMask</i>. Fields not selected by <i>valueMask</i> are ignored.</p>
<dd>int <i>x</i> (in) New x-coordinate for <i>tkwin</i>&#8216;s top left pixel (including border, if any) within tkwin&#8217;s parent.</p>
<dd>int <i>y</i> (in) New y-coordinate for <i>tkwin</i>&#8216;s top left pixel (including border, if any) within tkwin&#8217;s parent.</p>
<dd>int <i>width</i> (in) New width for <i>tkwin</i> (interior, not including border).</p>
<dd>int <i>height</i> (in) New height for <i>tkwin</i> (interior, not including border).</p>
<dd>int <i>borderWidth</i> (in) New width for <i>tkwin</i>&#8216;s border.</p>
<dd>XSetWindowAttributes <i>*attsPtr</i> (in) Points to a structure containing new values for the attributes given by the <i>valueMask</i> argument. Attributes not selected by <i>valueMask</i> are ignored.</p>
<dd>unsigned long <i>pixel</i> (in) New background or border color for window.</p>
<dd>Pixmap <i>pixmap</i> (in) New pixmap to use for background or border of <i>tkwin</i>. WARNING: cannot necessarily be deleted immediately, as for Xlib calls. See note below.</p>
<dd>Colormap <i>colormap</i> (in) New colormap to use for <i>tkwin</i>.</p>
<dd>Tk_Cursor <i>cursor</i> (in) New cursor to use for <i>tkwin</i>. If <code>None</code> is specified, then <i>tkwin</i> will not have its own cursor; it will use the cursor of its parent.
</dl>
<h2>Description</h2>
<p>These procedures are analogous to the X library procedures with similar names, such as <code>XConfigureWindow</code>. Each one of the above procedures calls the corresponding X procedure and also saves the configuration information in Tk&#8217;s local structure for the window. This allows the information to be retrieved quickly by the application (using macros such as <code>Tk_X</code> and <code>Tk_Height</code>) without having to contact the X server. In addition, if no X window has actually been created for <i>tkwin</i> yet, these procedures do not issue X operations or cause event handlers to be invoked; they save the information in Tk&#8217;s local structure for the window; when the window is created later, the saved information will be used to configure the window. </p>
<p> See the X library documentation for details on what these procedures do and how they use their arguments. </p>
<p> In the procedures <code>Tk_ConfigureWindow</code>, <code>Tk_MoveWindow</code>, <code>Tk_ResizeWindow</code>, <code>Tk_MoveResizeWindow</code>, and <code>Tk_SetWindowBorderWidth</code>, if <i>tkwin</i> is an internal window then event handlers interested in configure events are invoked immediately, before the procedure returns. If <i>tkwin</i> is a top-level window then the event handlers will be invoked later, after X has seen the request and returned an event for it. </p>
<p> Applications using Tk should never call procedures like <code>XConfigureWindow</code> directly; they should always use the corresponding Tk procedures. </p>
<p> The size and location of a window should only be modified by the appropriate geometry manager for that window and never by a window itself (but see <code>Tk_MoveToplevelWindow</code> for moving a top-level window). </p>
<p> You may not use <code>Tk_ConfigureWindow</code> to change the stacking order of a window (<i>valueMask</i> may not contain the <code>CWSibling</code> or <code>CWStackMode</code> bits). To change the stacking order, use the procedure <code>Tk_RestackWindow</code>. </p>
<p> The procedure <code>Tk_SetWindowColormap</code> will automatically add <i>tkwin</i> to the <code>TK_COLORMAP_WINDOWS</code> property of its nearest top-level ancestor if the new colormap is different from that of <i>tkwin</i>&#8216;s parent and <i>tkwin</i> is not already in the <code>TK_COLORMAP_WINDOWS</code> property.</p>
<h2>Bugs</h2>
<p><code>Tk_SetWindowBackgroundPixmap</code> and <code>Tk_SetWindowBorderPixmap</code> differ slightly from their Xlib counterparts in that the <i>pixmap</i> argument may not necessarily be deleted immediately after calling one of these procedures. This is because <i>tkwin</i>&#8216;s window may not exist yet at the time of the call, in which case <i>pixmap</i> is merely saved and used later when <i>tkwin</i>&#8216;s window is actually created. If you wish to delete <i>pixmap</i>, then call <code>Tk_MakeWindowExist</code> first to be sure that <i>tkwin</i>&#8216;s window exists and <i>pixmap</i> has been passed to the X server. </p>
<p> A similar problem occurs for the <i>cursor</i> argument passed to <code>Tk_DefineCursor</code>. The solution is the same as for pixmaps above: call <code>Tk_MakeWindowExist</code> before freeing the cursor.</p>
<h2>See Also</h2>
<p>Tk_MoveToplevelWindow, Tk_RestackWindow</p>
<h2>Keywords</h2>
<p>attributes, border, color, configure, height, pixel, pixmap, width, window, x, y</p>
