---
title: "tk_canvaseventuallyredraw(3)"
name: "tk_canvaseventuallyredraw"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_canvaseventuallyredraw/"
description: "Tk_CanvasTkwin, Tk_CanvasGetCoord, Tk_CanvasDrawableCoords, Tk_CanvasSetStippleOrigin, Tk_CanvasWindowCoords, Tk_CanvasEventuallyRedraw, Tk_CanvasTagsOption – utility procedures for canvas type man..."
---

<p>Tk_CanvasTkwin, Tk_CanvasGetCoord, Tk_CanvasDrawableCoords, Tk_CanvasSetStippleOrigin, Tk_CanvasWindowCoords, Tk_CanvasEventuallyRedraw, Tk_CanvasTagsOption &#8211; utility procedures for canvas type managers </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_Window
<code>Tk_CanvasTkwin</code>(<i>canvas</i>)
int
<code>Tk_CanvasGetCoord</code>(<i>interp, canvas, string, doublePtr</i>)
<code>Tk_CanvasDrawableCoords</code>(<i>canvas, x, y, drawableXPtr, drawableYPtr</i>)
<code>Tk_CanvasSetStippleOrigin</code>(<i>canvas, gc</i>)
<code>Tk_CanvasWindowCoords</code>(<i>canvas, x, y, screenXPtr, screenYPtr</i>)
<code>Tk_CanvasEventuallyRedraw</code>(<i>canvas, x1, y1, x2, y2</i>)
Tk_OptionParseProc *<code>Tk_CanvasTagsParseProc</code>;
Tk_OptionPrintProc *<code>Tk_CanvasTagsPrintProc</code>;</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Canvas <i>canvas</i> (in) A token that identifies a canvas widget.</p>
<dd>Tcl_Interp <i>*interp</i> (in/out) Interpreter to use for error reporting.</p>
<dd>const char <i>*string</i> (in) Textual description of a canvas coordinate.</p>
<dd>double <i>*doublePtr</i> (out) Points to place to store a converted coordinate.</p>
<dd>double <i>x</i> (in) An x coordinate in the space of the canvas.</p>
<dd>double <i>y</i> (in) A y coordinate in the space of the canvas.</p>
<dd>short <i>*drawableXPtr</i> (out) Pointer to a location in which to store an x coordinate in the space of the drawable currently being used to redisplay the canvas.</p>
<dd>short <i>*drawableYPtr</i> (out) Pointer to a location in which to store a y coordinate in the space of the drawable currently being used to redisplay the canvas.</p>
<dd>GC <i>gc</i> (out) Graphics context to modify.</p>
<dd>short <i>*screenXPtr</i> (out) Points to a location in which to store the screen coordinate in the canvas window that corresponds to <i>x</i>.</p>
<dd>short <i>*screenYPtr</i> (out) Points to a location in which to store the screen coordinate in the canvas window that corresponds to <i>y</i>.</p>
<dd>int <i>x1</i> (in) Left edge of the region that needs redisplay. Only pixels at or to the right of this coordinate need to be redisplayed.</p>
<dd>int <i>y1</i> (in) Top edge of the region that needs redisplay. Only pixels at or below this coordinate need to be redisplayed.</p>
<dd>int <i>x2</i> (in) Right edge of the region that needs redisplay. Only pixels to the left of this coordinate need to be redisplayed.</p>
<dd>int <i>y2</i> (in) Bottom edge of the region that needs redisplay. Only pixels above this coordinate need to be redisplayed. </p>
</dl>
<h2>Description</h2>
<p>These procedures are called by canvas type managers to perform various utility functions. </p>
<p> <code>Tk_CanvasTkwin</code> returns the Tk_Window associated with a particular canvas. </p>
<p> <code>Tk_CanvasGetCoord</code> translates a string specification of a coordinate (such as <code>2p</code> or <code>1.6c</code>) into a double-precision canvas coordinate. If <i>string</i> is a valid coordinate description then <code>Tk_CanvasGetCoord</code> stores the corresponding canvas coordinate at *<i>doublePtr</i> and returns <code>TCL_OK</code>. Otherwise it stores an error message in <i>interp-&gt;result</i> and returns <code>TCL_ERROR</code>. </p>
<p> <code>Tk_CanvasDrawableCoords</code> is called by type managers during redisplay to compute where to draw things. Given <i>x</i> and <i>y</i> coordinates in the space of the canvas, <code>Tk_CanvasDrawableCoords</code> computes the corresponding pixel in the drawable that is currently being used for redisplay; it returns those coordinates in *<i>drawableXPtr</i> and *<i>drawableYPtr</i>. This procedure should not be invoked except during redisplay. </p>
<p> <code>Tk_CanvasSetStippleOrigin</code> is also used during redisplay. It sets the stipple origin in <i>gc</i> so that stipples drawn with <i>gc</i> in the current offscreen pixmap will line up with stipples drawn with origin (0,0) in the canvas&#8217;s actual window. <code>Tk_CanvasSetStippleOrigin</code> is needed in order to guarantee that stipple patterns line up properly when the canvas is redisplayed in small pieces. Redisplays are carried out in double-buffered fashion where a piece of the canvas is redrawn in an offscreen pixmap and then copied back onto the screen. In this approach the stipple origins in graphics contexts need to be adjusted during each redisplay to compensate for the position of the off-screen pixmap relative to the window. If an item is being drawn with stipples, its type manager typically calls <code>Tk_CanvasSetStippleOrigin</code> just before using <i>gc</i> to draw something; after it is finished drawing, the type manager calls <code>XSetTSOrigin</code> to restore the origin in <i>gc</i> back to (0,0) (the restore is needed because graphics contexts are shared, so they cannot be modified permanently). </p>
<p> <code>Tk_CanvasWindowCoords</code> is similar to <code>Tk_CanvasDrawableCoords</code> except that it returns coordinates in the canvas&#8217;s window on the screen, instead of coordinates in an off-screen pixmap. </p>
<p> <code>Tk_CanvasEventuallyRedraw</code> may be invoked by a type manager to inform Tk that a portion of a canvas needs to be redrawn. The <i>x1</i>, <i>y1</i>, <i>x2</i>, and <i>y2</i> arguments specify the region that needs to be redrawn, in canvas coordinates. Type managers rarely need to invoke <code>Tk_CanvasEventuallyRedraw</code>, since Tk can normally figure out when an item has changed and make the redisplay request on its behalf (this happens, for example whenever Tk calls a <i>configureProc</i> or <i>scaleProc</i>). The only time that a type manager needs to call <code>Tk_CanvasEventuallyRedraw</code> is if an item has changed on its own without being invoked through one of the procedures in its Tk_ItemType; this could happen, for example, in an image item if the image is modified using image commands. </p>
<p> <code>Tk_CanvasTagsParseProc</code> and <code>Tk_CanvasTagsPrintProc</code> are procedures that handle the <code>-tags</code> option for canvas items. The code of a canvas type manager will not call these procedures directly, but will use their addresses to create a <code>Tk_CustomOption</code> structure for the <code>-tags</code> option. The code typically looks like this:</p>
<dl COMPACT>
<dd>
<pre>static Tk_CustomOption tagsOption = {Tk_CanvasTagsParseProc,
 Tk_CanvasTagsPrintProc, (ClientData) NULL
};
static Tk_ConfigSpec configSpecs[] = {
 ...
 {TK_CONFIG_CUSTOM, &quot;-tags&quot;, (char *) NULL, (char *) NULL,
 (char *) NULL, 0, TK_CONFIG_NULL_OK, &amp;tagsOption},
 ...
};</pre>
</dl>
<h2>Keywords</h2>
<p>canvas, focus, item type, redisplay, selection, type manager</p>
