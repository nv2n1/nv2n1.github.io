---
title: "tk_alloccursorfromobj(3)"
name: "tk_alloccursorfromobj"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_alloccursorfromobj/"
description: "Tk_AllocCursorFromObj, Tk_GetCursor, Tk_GetCursorFromObj, Tk_GetCursorFromData, Tk_NameOfCursor, Tk_FreeCursorFromObj, Tk_FreeCursor – maintain database of cursors"
---

<p>Tk_AllocCursorFromObj, Tk_GetCursor, Tk_GetCursorFromObj, Tk_GetCursorFromData, Tk_NameOfCursor, Tk_FreeCursorFromObj, Tk_FreeCursor &#8211; maintain database of cursors </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_Cursor
<code>Tk_AllocCursorFromObj(</code><i>interp, tkwin, objPtr</i><code>)</code>
Tk_Cursor
<code>Tk_GetCursor(</code><i>interp, tkwin, name</i><code>)</code>
Tk_Cursor
<code>Tk_GetCursorFromObj(</code><i>tkwin, objPtr</i><code>)</code>
Tk_Cursor
<code>Tk_GetCursorFromData(</code><i>interp, tkwin, source, mask, width, height, xHot, yHot, fg, bg</i><code>)</code>
const char *
<code>Tk_NameOfCursor(</code><i>display, cursor</i><code>)</code>
<code>Tk_FreeCursorFromObj(</code><i>tkwin, objPtr</i><code>)</code>
<code>Tk_FreeCursor(</code><i>display, cursor</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting.</p>
<dd>Tk_Window <i>tkwin</i> (in) Token for window in which the cursor will be used.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in/out) Description of cursor; see below for possible values. Internal rep will be modified to cache pointer to corresponding Tk_Cursor.</p>
<dd>char <i>*name</i> (in) Same as <i>objPtr</i> except description of cursor is passed as a string and resulting Tk_Cursor is not cached.</p>
<dd>const char <i>*source</i> (in) Data for cursor cursor, in standard cursor format.</p>
<dd>const char <i>*mask</i> (in) Data for mask cursor, in standard cursor format.</p>
<dd>int <i>width</i> (in) Width of <i>source</i> and <i>mask</i>.</p>
<dd>int <i>height</i> (in) Height of <i>source</i> and <i>mask</i>.</p>
<dd>int <i>xHot</i> (in) X-location of cursor hot-spot.</p>
<dd>int <i>yHot</i> (in) Y-location of cursor hot-spot.</p>
<dd>Tk_Uid <i>fg</i> (in) Textual description of foreground color for cursor.</p>
<dd>Tk_Uid <i>bg</i> (in) Textual description of background color for cursor.</p>
<dd>Display <i>*display</i> (in) Display for which <i>cursor</i> was allocated.</p>
<dd>Tk_Cursor <i>cursor</i> (in) Opaque Tk identifier for cursor. If passed to <code>Tk_FreeCursor</code>, must have been returned by some previous call to <code>Tk_GetCursor</code> or <code>Tk_GetCursorFromData</code>. </p>
</dl>
<h2>Description</h2>
<p>These procedures manage a collection of cursors being used by an application. The procedures allow cursors to be re-used efficiently, thereby avoiding server overhead, and also allow cursors to be named with character strings. </p>
<p> <code>Tk_AllocCursorFromObj</code> takes as argument an object describing a cursor, and returns an opaque Tk identifier for a cursor corresponding to the description. It re-uses an existing cursor if possible and creates a new one otherwise. <code>Tk_AllocCursorFromObj</code> caches information about the return value in <i>objPtr</i>, which speeds up future calls to procedures such as <code>Tk_AllocCursorFromObj</code> and <code>Tk_GetCursorFromObj</code>. If an error occurs in creating the cursor, such as when <i>objPtr</i> refers to a non-existent file, then <code>None</code> is returned and an error message will be stored in <i>interp</i>&#8216;s result if <i>interp</i> is not NULL. <i>ObjPtr</i> must contain a standard Tcl list with one of the following forms:</p>
<dl COMPACT>
<dt><i>name</i>&nbsp;<wbr>[<i>fgColor</i>&nbsp;<wbr>[<i>bgColor</i>]]</p>
<dd><i>Name</i> is the name of a cursor in the standard X cursor cursor, i.e., any of the names defined in <code>cursorcursor.h</code>, without the <code>XC_</code>. Some example values are <code>X_cursor</code>, <code>hand2</code>, or <code>left_ptr</code>. Appendix B of &#8220;The X Window System&#8221; by Scheifler &amp; Gettys has illustrations showing what each of these cursors looks like. If <i>fgColor</i> and <i>bgColor</i> are both specified, they give the foreground and background colors to use for the cursor (any of the forms acceptable to <code>Tk_GetColor</code> may be used). If only <i>fgColor</i> is specified, then there will be no background color: the background will be transparent. If no colors are specified, then the cursor will use black for its foreground color and white for its background color.</p>
<dl COMPACT>
<dd>The Macintosh version of Tk supports all of the X cursors and will also accept any of the standard Mac cursors including <code>ibeam</code>, <code>crosshair</code>, <code>watch</code>, <code>plus</code>, and <code>arrow</code>. In addition, Tk will load Macintosh cursor resources of the types <code>crsr</code> (color) and <code>CURS</code> (black and white) by the name of the resource. The application and all its open dynamic library&#8217;s resource files will be searched for the named cursor. If there are conflicts color cursors will always be loaded in preference to black and white cursors.</dl>
<dt><code>@</code><i>sourceName maskName fgColor bgColor</i></p>
<dd>In this form, <i>sourceName</i> and <i>maskName</i> are the names of files describing cursors for the cursor&#8217;s source bits and mask. Each file must be in standard X11 or X10 cursor format. <i>FgColor</i> and <i>bgColor</i> indicate the colors to use for the cursor, in any of the forms acceptable to <code>Tk_GetColor</code>. This form of the command will not work on Macintosh or Windows computers.</p>
<dt><code>@</code><i>sourceName fgColor</i></p>
<dd>This form is similar to the one above, except that the source is used as mask also. This means that the cursor&#8217;s background is transparent. This form of the command will not work on Macintosh or Windows computers.</p>
<dt><code>@</code><i>sourceName</i></p>
<dd>This form only works on Windows, and will load a Windows system cursor (<code>.ani</code> or <code>.cur</code>) from the file specified in <i>sourceName</i>.</dl>
<p> <code>Tk_GetCursor</code> is identical to <code>Tk_AllocCursorFromObj</code> except that the description of the cursor is specified with a string instead of an object. This prevents <code>Tk_GetCursor</code> from caching the return value, so <code>Tk_GetCursor</code> is less efficient than <code>Tk_AllocCursorFromObj</code>. </p>
<p> <code>Tk_GetCursorFromObj</code> returns the token for an existing cursor, given the window and description used to create the cursor. <code>Tk_GetCursorFromObj</code> does not actually create the cursor; the cursor must already have been created with a previous call to <code>Tk_AllocCursorFromObj</code> or <code>Tk_GetCursor</code>. The return value is cached in <i>objPtr</i>, which speeds up future calls to <code>Tk_GetCursorFromObj</code> with the same <i>objPtr</i> and <i>tkwin</i>. </p>
<p> <code>Tk_GetCursorFromData</code> allows cursors to be created from in-memory descriptions of their source and mask cursors. <i>Source</i> points to standard cursor data for the cursor&#8217;s source bits, and <i>mask</i> points to standard cursor data describing which pixels of <i>source</i> are to be drawn and which are to be considered transparent. <i>Width</i> and <i>height</i> give the dimensions of the cursor, <i>xHot</i> and <i>yHot</i> indicate the location of the cursor&#8217;s hot-spot (the point that is reported when an event occurs), and <i>fg</i> and <i>bg</i> describe the cursor&#8217;s foreground and background colors textually (any of the forms suitable for <code>Tk_GetColor</code> may be used). Typically, the arguments to <code>Tk_GetCursorFromData</code> are created by including a cursor file directly into the source code for a program, as in the following example:</p>
<dl COMPACT>
<dd>
<pre>Tk_Cursor cursor;
#include &quot;source.cursor&quot;
#include &quot;mask.cursor&quot;
cursor = Tk_GetCursorFromData(interp, tkwin, source_bits,
 mask_bits, source_width, source_height, source_x_hot,
 source_y_hot, Tk_GetUid(&quot;red&quot;), Tk_GetUid(&quot;blue&quot;));</pre>
</dl>
<p> Under normal conditions <code>Tk_GetCursorFromData</code> will return an identifier for the requested cursor. If an error occurs in creating the cursor then <code>None</code> is returned and an error message will be stored in <i>interp</i>&#8216;s result. </p>
<p> <code>Tk_AllocCursorFromObj</code>, <code>Tk_GetCursor</code>, and <code>Tk_GetCursorFromData</code> maintain a database of all the cursors they have created. Whenever possible, a call to <code>Tk_AllocCursorFromObj</code>, <code>Tk_GetCursor</code>, or <code>Tk_GetCursorFromData</code> will return an existing cursor rather than creating a new one. This approach can substantially reduce server overhead, so the Tk procedures should generally be used in preference to Xlib procedures like <code>XCreateFontCursor</code> or <code>XCreatePixmapCursor</code>, which create a new cursor on each call. The Tk procedures are also more portable than the lower-level X procedures. </p>
<p> The procedure <code>Tk_NameOfCursor</code> is roughly the inverse of <code>Tk_GetCursor</code>. If its <i>cursor</i> argument was created by <code>Tk_GetCursor</code>, then the return value is the <i>name</i> argument that was passed to <code>Tk_GetCursor</code> to create the cursor. If <i>cursor</i> was created by a call to <code>Tk_GetCursorFromData</code>, or by any other mechanism, then the return value is a hexadecimal string giving the X identifier for the cursor. Note: the string returned by <code>Tk_NameOfCursor</code> is only guaranteed to persist until the next call to <code>Tk_NameOfCursor</code>. Also, this call is not portable except for cursors returned by <code>Tk_GetCursor</code>. </p>
<p> When a cursor returned by <code>Tk_AllocCursorFromObj</code>, <code>Tk_GetCursor</code>, or <code>Tk_GetCursorFromData</code> is no longer needed, <code>Tk_FreeCursorFromObj</code> or <code>Tk_FreeCursor</code> should be called to release it. For <code>Tk_FreeCursorFromObj</code> the cursor to release is specified with the same information used to create it; for <code>Tk_FreeCursor</code> the cursor to release is specified with its Tk_Cursor token. There should be exactly one call to <code>Tk_FreeCursor</code> for each call to <code>Tk_AllocCursorFromObj</code>, <code>Tk_GetCursor</code>, or <code>Tk_GetCursorFromData</code>. </p>
<h2>Bugs</h2>
<p>In determining whether an existing cursor can be used to satisfy a new request, <code>Tk_AllocCursorFromObj</code>, <code>Tk_GetCursor</code>, and <code>Tk_GetCursorFromData</code> consider only the immediate values of their arguments. For example, when a file name is passed to <code>Tk_GetCursor</code>, <code>Tk_GetCursor</code> will assume it is safe to re-use an existing cursor created from the same file name: it will not check to see whether the file itself has changed, or whether the current directory has changed, thereby causing the name to refer to a different file. Similarly, <code>Tk_GetCursorFromData</code> assumes that if the same <i>source</i> pointer is used in two different calls, then the pointers refer to the same data; it does not check to see if the actual data values have changed. </p>
<h2>Keywords</h2>
<p>cursor</p>
