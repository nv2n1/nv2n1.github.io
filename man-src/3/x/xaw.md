---
title: "xaw(3)"
name: "xaw"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xaw/"
description: "Xaw – X Athena Widgets"
---

<p>&nbsp;<wbr>Xaw &#8211; X Athena Widgets</p>
<h2>Description</h2>
<p><code>Xaw</code> is a widget set based on the X Toolkit Intrinsics (Xt) Library. This release by the X.org Foundation includes additions and modifications originally made for The XFree86 Project, Inc. This manual page describes these changes as well as some of the common interfaces between its version and the previous X Consortium release (Xaw6).</p>
<h2>Actions</h2>
<p>All of the <i>Xaw</i> widgets now have the additional translations <code>call-proc, declare, get-values</code> and <code>set-values</code>. The syntax for these actions is: </p>
<p> <i>action-name </i>(<i>boolean-expression</i>, <i>arguments</i>) </p>
<p> <code>Action-name</code> is one of <i>call-proc</i>, <i>declare</i>, <i>get-values</i> or <i>set-values</i>. </p>
<p> <code>Boolean-expression</code> is composed with the operators <i>|</i> (or), <i>&amp;</i> (and), <i>^</i> (xor), and <i>~</i> (not). The operands can be a variable name, which starts with a <i>$</i>; a resource name without the bindings <i>.</i> or <i>*</i>; or a constant name, including <i>mine</i> (event-&gt;xany.window == XtWindow(widget)), <i>faked</i> (event-&gt;xany.send_event != 0), <i>true</i> (1) and <i>false</i> (0). </p>
<p> <code>Arguments</code> are self-explanatory; when starting with a <i>$</i> they name a variable, otherwise, they indicate a resource name.</p>
<dl COMPACT>
<dt><code>call-proc </code>(<i>boolean-expression</i>, <i>procedure-name</i>)</p>
<dd>This action allows the evaluation of a boolean expression in the first parameter before calling a action procedure. The procedure is only called if the expression evaluates as true. Example: </p>
<pre>call-proc(&quot;$inside &amp; $pressed&quot;, notify)</pre>
<dt><code>declare </code>(<i>boolean-expression</i>, <i>variable</i>, <i>value</i>, &#8230;)</p>
<dd>This action is used to create new variables or change their values. Any number of variable-value tuples may be specified. Example: </p>
<pre>declare(1, $pressed, 1)</pre>
<dt><code>get-values </code>(<i>boolean-expression</i>, <i>variable</i>, <i>value</i>, &#8230;)</p>
<dd>This action reads a widget resource value into a variable. Any number of variable-value tuples may be specified. Example: </p>
<pre>get-values(1, $fg, foreground, $bg, background)</pre>
<dt><code>set-values </code>(<i>boolean-expression</i>, <i>variable</i>, <i>value</i>, &#8230;)</p>
<dd>This action sets a widget resource to the given value, which may be a variable. Any number of variable-value tuples may be specified. Example: </p>
<pre>set-values(1, foreground, $bg, background, $fg)</pre>
</dl>
<p> Here is a sample translation to make a label widget behave like a button: </p>
<pre>&lt;Map&gt;: get-values(1, $fg, foreground, $bg, background)
\
&lt;Btn1Down&gt;: set-values(1, foreground, yellow, background, gray30)
\
&lt;Btn1Up&gt;: set-values(1, foreground, $fg, background, $bg)</pre>
<h2>Display Lists</h2>
<p>All of the <code>Xaw</code> widgets have now the additional resource <i>displayList</i>. This resource allows drawing the widget decorations using commands embedded in a resource string. The displayList resource has the syntax: </p>
<p> <i>[class-name:]function-name arguments[[{;
}]&#8230;]</i> </p>
<p> <code>Class-name</code> is any registered set of functions to draw in the widget. Currently the only existing class is <i>xlib</i>, which provides access to the Xlib drawing primitives. </p>
<p> <code>Function-name</code> is the drawing or configuration function to be called, described bellow. </p>
<p> <code>Arguments</code> may be anything suitable to the displayList function being called. When the function requires a coordinate, the syntax is <i>{+-}&lt;integer&gt;</i> or <i>&lt;integer&gt;/&lt;integer&gt;</i>. Examples: </p>
<pre> +0,+0 top, left
 -0,-0 bottom, right
 -+10,-+10 bottom+10, right+10
 +0,1/2 left, vertical-center</pre>
<dl COMPACT>
<dt><code>arc-mode </code>mode</p>
<dd>Sets the arc mode. Accepted <i>mode</i>s are &quot;pieslice&quot; and &quot;chord&quot;, which set the arc to ArcPieSlice or ArcChord, respectively. Example: </p>
<pre>arc-mode chord</pre>
<dt><code>bg </code>color-spec</p>
<dd>
<dt> <code>background </code>color-spec</p>
<dd>Sets the background color. <i>color-spec</i> must a valid color specification. Example: </p>
<pre>background red</pre>
<dt><code>cap-style </code>style</p>
<dd>Sets the cap style. Accepted <i>style</i>s are &quot;notlast&quot;, &quot;butt&quot;, &quot;round&quot;, and &quot;projecting&quot;, which set the cap style to CapNotLast, CapBut, CapRound or CapProjecting, respectively. Example: </p>
<pre>cap-style round</pre>
<dt><code>clip-mask </code>pixmap-spec</p>
<dd>Sets the pixmap for the clip mask. Requires a pixmap parameter, as described in the <code>PIXMAPS</code> section below. Example: </p>
<pre>clip-mask xlogo11</pre>
<dt><code>clip-origin </code>x,y</p>
<dd>Sets the clip x and y origin. Requires two arguments, the x and y coordinates. Example: </p>
<pre>clip-origin 10,10</pre>
<dt><code>clip-rects </code>x1,y1,x2,y2 [&#8230;,xn,yn]</p>
<dd>
<dt> <code>clip-rectangles </code>x1,y1,x2,y2 [&#8230;,xn,yn]</p>
<dd>Sets a list of rectangles to the clip mask. The number of arguments must be a multiple of four. The arguments are coordinates. The parser calculates the width and height of the rectangles. Example: </p>
<pre>clip-rects 0,0,10,20, 20,10,30,30</pre>
<dt><code>coord-mode </code>mode</p>
<dd>Changes the coord mode for <i>fill-polygon</i>, <i>draw-lines</i>, and <i>draw-points</i>. Accepted parameters are &quot;modeorigin&quot; and &quot;previous&quot;, that sets the coord mode to CoordModeOrigin or CoordModePrevious, respectively. Example: </p>
<pre>coord-mode previous</pre>
<dt><code>copy-area </code>{pixmap-spec|.},dstx,dsty[,x2,y2,srcx,srcy]</p>
<dd>Calls XCopyArea. The character <i>.</i> means copy the window contents; pixmap-spec is as defined in the <code>PIXMAPS</code> section below. <i>X2</i> and <i>y2</i> are the coordinates of the end copy, not the width and height; if not defined, the parser calculates them. <i>src_x</i> and <i>src_y</i> default to zero. Example: </p>
<pre>copy-area Term,10,10</pre>
<dt><code>copy-plane </code>{pixmap-spec|.},dstx,dsty[,x2,y2,srcx,srcy,plane]</p>
<dd>Calls XCopyPlane. The character <i>.</i> means copy the window contents; pixmap-spec is as defined in the <code>PIXMAPS</code> section below. <i>X2</i> and <i>y2</i> are the coordinates of the end copy, not the width and height; if not defined, the parser calculates them. <i>src_x</i> and <i>src_y</i> default to zero. <i>Plane</i> defaults to one. Example: </p>
<pre>copy-plane star,10,10</pre>
<dt><code>dashes </code>i1[&#8230;,in]</p>
<dd>Sets the dashes for line drawing. Accepts up to 127 arguments. Example: </p>
<pre>dashes 3,7 9,10</pre>
<dt><code>draw-arc </code>x1,y1,x2,y2[,start-angle,end-angle]</p>
<dd>Draws an arc. The four first arguments are the rectangle enclosing the arc. The two remaining arguments, if specified, are the start and end angle, in degrees. Example: </p>
<pre>draw-arc +0,+0,-1,-1,0,90</pre>
<dt><code>draw-rect </code>x1,y1,x2,y2</p>
<dd>
<dt> <code>draw-rectangle </code>x1,y1,x2,y2</p>
<dd>Draws a rectangle. Requires four arguments, which are the start and end coordinate pairs. Example: </p>
<pre>draw-rect +1,+1,-5,-5</pre>
<dt><code>draw-string </code>x,y,string</p>
<dd>Draws a text string. Requires three arguments, a x coordinate, a y coordinate, and a string. Strings that have white space can be quoted with the <i>&quot;</i> character; the backslash character <i>\</i> can also be used, but it will be necessary escape it twice. Example: </p>
<pre> draw-string 10,10, &quot;Hello world!&quot;</pre>
<dt><code>exposures </code>boolean</p>
<dd>Sets graphics exposures in the GC. Allowed parameters are a integer or the strings &quot;true&quot;, &quot;false&quot;, &quot;on&quot; and &quot;off&quot;. Example: </p>
<pre>exposures true</pre>
<dt><code>fill-arc </code>x1,y1,x2,y2[,start-angle,end-angle]</p>
<dd>Like <i>draw-arc</i>, but fills the contents of the arc with the currently selected foreground. Example: </p>
<pre>fill-arc +0,+0,-1,-1,0,180</pre>
<dt><code>fill-poly </code>x1,y1 [&#8230;,xn,yn]</p>
<dd>
<dt> <code>fill-polygon </code>x1,y1 [&#8230;,xn,yn]</p>
<dd>Like <i>draw-lines</i>, but fills the enclosed polygon and joins the first and last point, if they are not at the same position. Example: </p>
<pre>fill-poly +0,+10, +10,+20, +30,+0</pre>
<dt><code>fill-rect </code>x1,y1,x2,y2</p>
<dd>
<dt> <code>fill-rectangle </code>x1,y1,x2,y2</p>
<dd>Like <i>draw-rect</i>, but fills the contents of the rectangle with the selected foreground color. Example: </p>
<pre>fill-rect +10,+10,-20,-20</pre>
<dt><code>fill-rule </code>rule</p>
<dd>Sets the fill rule. Accepted parameters are &quot;evenodd&quot; and &quot;winding&quot;, which set the fill rule to EvenOddRule or WindingRule, respectively. Example: </p>
<pre>fill-rule winding</pre>
<dt><code>fill-style </code>style</p>
<dd>Sets the fill style. Allowed parameters are &quot;solid&quot;, &quot;tiled&quot;, &quot;stippled&quot; and &quot;opaquestippled&quot;, which set the fill style to FillSolid, FillTiled, FillStippled or FillOpaqueStippled, respectively. Example: </p>
<pre>fill-style tiled</pre>
<dt><code>font </code>font-spec</p>
<dd>Sets the font for text functions. Example: </p>
<pre>font -*-*-*-R-*-*-*-120-*-*-*-*-ISO8859-1</pre>
<dt><code>fg </code>color-spec</p>
<dd>
<dt> <code>foreground </code>color-spec</p>
<dd>Like <i>background</i>, but sets the current foreground color. Example: </p>
<pre>foreground blue</pre>
<dt><code>mask</code></p>
<dd>This command is useful when you want to draw only in the region that really needs to be repainted. Requires no arguments.</p>
<dt><code>function </code>function-spec</p>
<dd>Sets the specific GC function. Allowed parameters are &quot;set&quot;, &quot;clear&quot;, &quot;and&quot;, &quot;andreverse&quot;, &quot;copy&quot;, &quot;andinverted&quot;, &quot;noop&quot;, &quot;xor&quot;, &quot;or&quot;, &quot;nor&quot;, &quot;equiv&quot;, &quot;invert&quot;, &quot;orreverse&quot;, &quot;copyinverted&quot; and &quot;nand&quot;, which set the function to GXset, GXclear, GXand, GXandReverse, GXcopy, GXandInverted, GXnoop, GXxor, GXor, GXnor, GXequiv, GXinvert, GXorReverse, GXcopyInverted or GXnand, respectively. Example: </p>
<pre>function xor</pre>
<dt><code>join-style </code>style</p>
<dd>Sets the join style. Allowed parameters are &quot;miter&quot;, &quot;round&quot; and &quot;bevel&quot;, which set the join style to JoinMiter, JoinRound and JoinBevel, respectively. Example: </p>
<pre>join-style round</pre>
<dt><code>image </code>{pixmap-spec},xs,ys,[xe,ye]</p>
<dd>This function is implemented as a way to quickly compose complex decorations in widgets. <i>Pixmap-spec</i> is as defined in the <code>PIXMAPS</code> section below. <i>xs</i> and <i>ys</i> are the coordinates from where to start copying the pixmap; <i>xe</i> and <i>ye</i> are optional (they default to xs + pixmap.width and ys + pixmap.height, respectively). If the pixmap has a mask, the copy is masked accordingly. Example: </p>
<pre>image pixmap.xpm,0,0,20,20</pre>
<dt><code>line </code>x1,y1,x2,y2</p>
<dd>
<dt> <code>draw-line </code>x1,y1,x2,y2</p>
<dd>Draws a line with the current foreground color. Requires four arguments, the starting and ending coordinate pairs. Example: </p>
<pre>line +0,+0, -1,-1</pre>
<dt><code>line-width </code>integer</p>
<dd>Selects a line width for drawing. Example: </p>
<pre>line-width 2</pre>
<dt><code>line-style </code>style</p>
<dd>Sets the line style. Accepted parameters are &quot;solid&quot;, &quot;onoffdash&quot; and &quot;doubledash&quot;, which set the line style to LineSolid, LineOnOffDash or LineDoubleDash, respectively. Example: </p>
<pre>line-style onoffdash</pre>
<dt><code>lines </code>x1,y1,x2,y2 [&#8230;,xn,yn]</p>
<dd>
<dt> <code>draw-lines </code>x1,y1,x2,y2 [&#8230;,xn,yn]</p>
<dd>Draws a list of lines. Any number of argument pairs may be supplied. Example: </p>
<pre>lines +0,-1, -1,-1, -1,+0</pre>
<dt><code>paint-string </code>x,y,string</p>
<dd>Identical to draw-string, but also uses the background color. Example: </p>
<pre> paint-string 10,20, &quot;Sample text&quot;</pre>
<dt><code>point </code>x,y</p>
<dd>
<dt> <code>draw-point </code>x,y</p>
<dd>Draws a point. Requires two arguments, a coordinate pair. Example: </p>
<pre>point +10,+10</pre>
<dt><code>plane-mask </code>integer</p>
<dd>Sets the plane mask. Requires an integer parameter. Example: </p>
<pre>plane-mask -1</pre>
<dt><code>points </code>x1,y1 [&#8230;,xn,yn]</p>
<dd>
<dt> <code>draw-points </code>x1,y1 [&#8230;,xn,yn]</p>
<dd>Draws a list of points at the specified coordinates. Example: </p>
<pre>points +1,+2, +1,+4, +1,+6</pre>
<dt><code>segments </code>x1,y1,x2,y2 [&#8230;,xn,yn]</p>
<dd>
<dt> <code>draw-segments </code>x1,y1,x2,y2 [&#8230;,xn,yn]</p>
<dd>Draws a list of segment lines. The number of parameters must be multiple of 4. Example: </p>
<pre>segments +1,+2,+1,-3, +2,-2,-3,-2</pre>
<dt><code>shape-mode </code>mode</p>
<dd>Sets the shape mode used in <i>fill-polygon</i>. Accepted parameters are &quot;complex&quot;, &quot;convex&quot; or &quot;nonconvex&quot;, which set the shape mode to Complex, Convex or Nonconvex, accordingly. Example: </p>
<pre>shape-mode convex</pre>
<dt><code>stipple </code>pixmap-spec</p>
<dd>Sets the pixmap for a stipple. Requires a pixmap parameter, as described in the <code>PIXMAPS</code> section below. Example: </p>
<pre>stipple plaid</pre>
<dt><code>subwindow-mode </code>mode</p>
<dd>Sets the subwindow mode in the GC. Accepted parameters are &quot;includeinferiors&quot; and &quot;clipbychildren&quot;, which set the subwindow mode to IncludeInferiors or ClipByChildren, respectively. Example: </p>
<pre>subwindow-mode includeinferiors</pre>
<dt><code>tile </code>pixmap-spec</p>
<dd>Sets the pixmap for a tile. Requires a pixmap parameter, as described in the <code>PIXMAPS</code> section below. Example: </p>
<pre>tile xlogo11?foreground=red&amp;background=gray80</pre>
<dt><code>ts-origin </code>x,y</p>
<dd>Sets the tile stipple x and y origin. Requires two arguments, a x and y coordinate. Example: </p>
<pre>ts-origin 10,10</pre>
<dt><code>umask</code></p>
<dd>Disables the GC mask, if it has been set with the command <i>mask</i>. Requires no arguments.</dl>
<p> Example for drawing a shadow effect in a widget: </p>
<pre>foreground gray30;\
draw-lines +1,-1,-1,-1,-1,+1;\
foreground gray85;\
draw-lines -1,+0,+0,+0,+0,-1</pre>
<h2>Pixmaps</h2>
<p>A String to Pixmap converter has been added to <code>Xaw</code>. This converter is meant to be extended, and has enough abstraction to allow loading several image formats. It uses a format that resembles a <i>URL</i>, with the syntax: </p>
<p> <i>[type:]name[?arg=val[{&amp;}&#8230;]]</i> </p>
<p> <code>Type</code> can be one of <i>bitmap</i>, <i>gradient</i> or <i>xpm</i>. </p>
<p> <code>Name</code> may be a file name, or, in the case of type <i>gradient</i>, may be either <i>vertical</i> or <i>horizontal</i>. </p>
<p> <code>Arg=val</code> is a list of arguments to the converter. An argument list is preceded by a question mark, and multiple arguments are separated by ampersands. The most common arguments are <i>foreground</i> and <i>background</i>. Gradients also support the arguments <i>start</i> and <i>end</i> (colors with which to start and end the gradient); the steps argument, to allow using less colors; and the <i>dimension</i> argument to specify the size of the gradient.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>The <i>xpm</i> converter<br />
 understands the <i>closeness</i> argument, which aids in using fewer colors (useful if you have a limited colormap).</p>
<h2>Text Widget</h2>
<p>Most of the changes to this version of the Xaw library were done in the TextWidget, TextSrcObject, TextSinkObject and related files. </p>
<p> A couple of highly visible changes in the Text widget are due to many bugs in the Xaw6 implementation involving scrollbars and auto-resizing. Scrollbars being added or removed caused several problems in keeping the text cursor visible, and in Xaw6 it was very easy to have a widget thinking the cursor was visible, when it was not. Also, permitting automatic resizing of the widget to a larger geometry created other problems, making it difficult to have a consistent layout in the application, and, if the window manager did not interfere, windows larger than the screen could result. Therefore, some functionality involving scrollbars and auto-resizing has been disabled; see the section on new and modified Text widget resources below. </p>
<p> The Text widget&#8217;s default key bindings were originally based on the Emacs text editor. In this release, even more operations familiar to Emacs users have been added. New text actions include:</p>
<dl COMPACT>
<dt><code>indent</code></p>
<dd>Indents text blocks. Not bound by default. The Text widget also does not attempt to perform auto-indentation of its source object by default.</p>
<dt><code>keyboard-reset</code></p>
<dd>Resets the keyboard state. Reverts the action multiplier to 1, and if undo is enabled, toggles between undo and redo. Bound by default to <i>Control&lt;Key&gt;G</i>.</p>
<dt><code>kill-ring-yank</code></p>
<dd>In this version of Xaw, text killed in any text field is kept in memory, allowing cut and paste operations internally to the program between text fields. Bound by default to <i>Meta&lt;Key&gt;Y</i>.</p>
<dt><code>numeric</code></p>
<dd>Listed here only for purposes of documentation. Called by default when one of the characters <i>1, 2, 3, 4, 5, 6, 7, 8, 9, 0,</i> or <i>&#8211;</i> is typed, allowing composition of the multiplication number of text actions.</p>
<dt><code>set-keyboard-focus</code></p>
<dd>Sets the input focus of the top level widget to the text field. Not enabled by default, but bound to the <i>&lt;Btn1Down&gt;</i> event.</p>
<dt><code>toggle-overwrite</code></p>
<dd>Toggles overwrite mode. In overwrite mode, any text inserted in a text field will replace existing text. Bound by default to <i>&lt;Key&gt;Insert</i>.</p>
<dt><code>undo</code></p>
<dd>Sets the <i>enableUndo</i> resource of the textSrcObject. Not enabled by default, but bound to <i>Control&lt;Key&gt;_</i>.</dl>
<p> New and modified Text widget resources include:</p>
<dl COMPACT>
<dt><code>justify (</code>Class<code> Justify)</code></p>
<dd>Sets the text justification. Can be one of <i>left, right, center</i>, or <i>full</i>. Only enabled when the <i>autoFill</i> resource is set, and the resources <i>leftColumn</i> and <i>rightColumn</i> are correctly set.</p>
<dt><code>leftColumn (</code>Class<code> Column)</code></p>
<dd>Specifies the left column at which to break text. Text lines started with an alphanumeric character will automatically start at this column.</p>
<dt><code>positionCallback (</code>Class<code> Callback)</code></p>
<dd>Allows installation of a callback to be called every time the cursor is moved, and/or the file changes its size. The callback is called with a pointer to a structure containing the following data: </p>
<pre>typedef struct {
 int line_number;
 int column_number;
 XawTextPosition insert_position;
 XawTextPosition last_position;
 Boolean overwrite_mode;
} XawTextPositionInfo;</pre>
<p>This callback is intended to help programmers write text editors based on the Xaw widget set.</p>
<dt><code>resize (</code>Class<code> Resize)</code></p>
<dd>No longer supported, but recognized for backward compatibility with resource specifications written for the Xaw6 Text widget.</p>
<dt><code>rightColumn (</code>Class<code> Column)</code></p>
<dd>Specifies the right column at which to break text. Text lines started with an alphanumeric character will automatically end at this column.</p>
<dt><code>scrollHorizontal (</code>Class<code> Scroll)</code></p>
<dd>
<dt> <code>scrollVertical (</code>Class<code> Scroll)</code></p>
<dd>These resources control the placement of scrollbars on the left and bottom edges of the Text widget. They accept the values <i>XawtextScrollAlways</i> and <i>XawtextScrollNever</i>. A converter is registered for this resource that will convert the following strings: <i>always</i> and <i>never</i>. The value <i>XawtextScrollWhenNeeded</i> (and <i>whenNeeded</i>, recognized by the converter), is accepted for backwards compatibility with resource specifications written for the Xaw6 Text widget, but ignored (effectively treated as <i>XawtextScrollNever</i>).</dl>
<h2>Text Source Object</h2>
<p>The textSrcObject allows display of its contents to more than one window, and also stores undo information. The new resources for the textSrcObject are:</p>
<dl COMPACT>
<dt><code>callback (</code>Class<code> Callback)</code></p>
<dd>Previous versions of Xaw had this resource in subclasses of the TextSource object. This was changed to make it possible to tell the callback the state of the text when undo is enabled.</p>
<dt><code>enableUndo (</code>Class<code> Undo)</code></p>
<dd>A boolean resource that enables or disables the undo function. The default value is False.</p>
<dt><code>sourceChanged (</code>Class<code> Changed)</code></p>
<dd>Like the callback resource, this resource was previously in subclasses of the TextSource object. It is now in the textSrcObject to control the changed/unchanged state when undo is enabled.</dl>
<h2>Text Sink Object</h2>
<p>The textSinkObject subclasses asciiSinkObject and multiSinkObject have been changed slightly to use a new cursor shape (no longer a caret at the baseline) that indicates the input focus of the text widget, and allow specification of the cursor color. The new resource is:</p>
<dl COMPACT>
<dt><code>cursorColor (</code>Class<code> Color)</code></p>
<dd>Sets the cursor color of the text. This color is also used to draw selected text.</dl>
<h2>Simple Menu Widget</h2>
<p>The simpleMenuWidget algorithm to lay out menu entries has been changed to enable multiple columns when a single column does not fit on the screen. It was also modified to enable submenus.</p>
<h2>Sme Bsb Object</h2>
<p>A new resource has been added to the smeBSBObject to allow binding submenus to it. The new resource is:</p>
<dl COMPACT>
<dt><code>menuName (</code>Class<code> MenuName)</code></p>
<dd>Specifies the name of the popup widget to be popped up when the pointer is over the menu entry, or NULL. Note that the named menu must be a child of the popup parent of the smeBSBObject.</dl>
<h2>Authors</h2>
<p>The original X Consortium version of the Athena Widget Set and its documentation were the work of many people, including Chris D. Peterson, Ralph Swick, Mark Ackerman, Donna Converse, Jim Fulton, Loretta Guarino-Reid, Charles Haynes, Rich Hyde, Mary Larson, Joel McCormack, Ron Newman, Jeanne Rich, Terry Weissman, Mike Gancarz, Phil Karlton, Kathleen Langone, Ram Rao, Smokey Wallace, Al Mento, and Jean Diaz. </p>
<p> The additions and modifications to <i>Xaw</i> which were originally made for XFree86 were written by Paulo C&#8217;esar Pereira de Andrade.</p>
<h2>See Also</h2>
<p><i>Athena Widget Set &#8211; C Language Interface</i></p>
