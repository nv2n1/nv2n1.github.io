---
title: "tk_getbitmapfromobj(3)"
name: "tk_getbitmapfromobj"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getbitmapfromobj/"
description: "Tk_AllocBitmapFromObj, Tk_GetBitmap, Tk_GetBitmapFromObj, Tk_DefineBitmap, Tk_NameOfBitmap, Tk_SizeOfBitmap, Tk_FreeBitmapFromObj, Tk_FreeBitmap – maintain database of single-plane pixmaps"
---

<p>Tk_AllocBitmapFromObj, Tk_GetBitmap, Tk_GetBitmapFromObj, Tk_DefineBitmap, Tk_NameOfBitmap, Tk_SizeOfBitmap, Tk_FreeBitmapFromObj, Tk_FreeBitmap &#8211; maintain database of single-plane pixmaps </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Pixmap
<code>Tk_AllocBitmapFromObj(</code><i>interp, tkwin, objPtr</i><code>)</code>
Pixmap
<code>Tk_GetBitmap(</code><i>interp, tkwin, info</i><code>)</code>
Pixmap
<code>Tk_GetBitmapFromObj(</code><i>tkwin, objPtr</i><code>)</code>
int
<code>Tk_DefineBitmap(</code><i>interp, name, source, width, height</i><code>)</code>
const char *
<code>Tk_NameOfBitmap(</code><i>display, bitmap</i><code>)</code>
<code>Tk_SizeOfBitmap(</code><i>display, bitmap, widthPtr, heightPtr</i><code>)</code>
<code>Tk_FreeBitmapFromObj(</code><i>tkwin, objPtr</i><code>)</code>
<code>Tk_FreeBitmap(</code><i>display, bitmap</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting; if NULL then no error message is left after errors.</p>
<dd>Tk_Window <i>tkwin</i> (in) Token for window in which the bitmap will be used.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in/out) String value describes desired bitmap; internal rep will be modified to cache pointer to corresponding Pixmap.</p>
<dd>const char <i>*info</i> (in) Same as <i>objPtr</i> except description of bitmap is passed as a string and resulting Pixmap is not cached.</p>
<dd>const char <i>*name</i> (in) Name for new bitmap to be defined.</p>
<dd>const char <i>*source</i> (in) Data for bitmap, in standard bitmap format. Must be stored in static memory whose value will never change.</p>
<dd>int <i>width</i> (in) Width of bitmap.</p>
<dd>int <i>height</i> (in) Height of bitmap.</p>
<dd>int <i>*widthPtr</i> (out) Pointer to word to fill in with <i>bitmap</i>&#8216;s width.</p>
<dd>int <i>*heightPtr</i> (out) Pointer to word to fill in with <i>bitmap</i>&#8216;s height.</p>
<dd>Display <i>*display</i> (in) Display for which <i>bitmap</i> was allocated.</p>
<dd>Pixmap <i>bitmap</i> (in) Identifier for a bitmap allocated by <code>Tk_AllocBitmapFromObj</code> or <code>Tk_GetBitmap</code>. </p>
</dl>
<h2>Description</h2>
<p>These procedures manage a collection of bitmaps (one-plane pixmaps) being used by an application. The procedures allow bitmaps to be re-used efficiently, thereby avoiding server overhead, and also allow bitmaps to be named with character strings. </p>
<p> <code>Tk_AllocBitmapFromObj</code> returns a Pixmap identifier for a bitmap that matches the description in <i>objPtr</i> and is suitable for use in <i>tkwin</i>. It re-uses an existing bitmap, if possible, and creates a new one otherwise. <i>ObjPtr</i>&#8216;s value must have one of the following forms:</p>
<dl COMPACT>
<dt><code>@</code><i>fileName</i></p>
<dd><i>FileName</i> must be the name of a file containing a bitmap description in the standard X11 or X10 format.</p>
<dt><i>name</i></p>
<dd><i>Name</i> must be the name of a bitmap defined previously with a call to <code>Tk_DefineBitmap</code>. The following names are pre-defined by Tk:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>error</code></p>
<dd>The international &#8220;don&#8217;t&#8221; symbol: a circle with a diagonal line across it.</p>
<dt><code>gray75</code></p>
<dd>75% gray: a checkerboard pattern where three out of four bits are on.</p>
<dt><code>gray50</code></p>
<dd>50% gray: a checkerboard pattern where every other bit is on.</p>
<dt><code>gray25</code></p>
<dd>25% gray: a checkerboard pattern where one out of every four bits is on.</p>
<dt><code>gray12</code></p>
<dd>12.5% gray: a pattern where one-eighth of the bits are on, consisting of every fourth pixel in every other row.</p>
<dt><code>hourglass</code></p>
<dd>An hourglass symbol.</p>
<dt><code>info</code></p>
<dd>A large letter &#8220;i&#8221;.</p>
<dt><code>questhead</code></p>
<dd>The silhouette of a human head, with a question mark in it.</p>
<dt><code>question</code></p>
<dd>A large question-mark.</p>
<dt><code>warning</code></p>
<dd>A large exclamation point.</dl>
<p> In addition, the following pre-defined names are available only on the <code>Macintosh</code> platform:</p>
<dl COMPACT>
<dt><code>document</code></p>
<dd>A generic document.</p>
<dt><code>stationery</code></p>
<dd>Document stationery.</p>
<dt><code>edition</code></p>
<dd>The <i>edition</i> symbol.</p>
<dt><code>application</code></p>
<dd>Generic application icon.</p>
<dt><code>accessory</code></p>
<dd>A desk accessory.</p>
<dt><code>folder</code></p>
<dd>Generic folder icon.</p>
<dt><code>pfolder</code></p>
<dd>A locked folder.</p>
<dt><code>trash</code></p>
<dd>A trash can.</p>
<dt><code>floppy</code></p>
<dd>A floppy disk.</p>
<dt><code>ramdisk</code></p>
<dd>A floppy disk with chip.</p>
<dt><code>cdrom</code></p>
<dd>A cd disk icon.</p>
<dt><code>preferences</code></p>
<dd>A folder with prefs symbol.</p>
<dt><code>querydoc</code></p>
<dd>A database document icon.</p>
<dt><code>stop</code></p>
<dd>A stop sign.</p>
<dt><code>note</code></p>
<dd>A face with balloon words.</p>
<dt><code>caution</code></p>
<dd>A triangle with an exclamation point.</dl>
</dl>
</dl>
<p> Under normal conditions, <code>Tk_AllocBitmapFromObj</code> returns an identifier for the requested bitmap. If an error occurs in creating the bitmap, such as when <i>objPtr</i> refers to a non-existent file, then <code>None</code> is returned and an error message is left in <i>interp</i>&#8216;s result if <i>interp</i> is not NULL. <code>Tk_AllocBitmapFromObj</code> caches information about the return value in <i>objPtr</i>, which speeds up future calls to procedures such as <code>Tk_AllocBitmapFromObj</code> and <code>Tk_GetBitmapFromObj</code>. </p>
<p> <code>Tk_GetBitmap</code> is identical to <code>Tk_AllocBitmapFromObj</code> except that the description of the bitmap is specified with a string instead of an object. This prevents <code>Tk_GetBitmap</code> from caching the return value, so <code>Tk_GetBitmap</code> is less efficient than <code>Tk_AllocBitmapFromObj</code>. </p>
<p> <code>Tk_GetBitmapFromObj</code> returns the token for an existing bitmap, given the window and description used to create the bitmap. <code>Tk_GetBitmapFromObj</code> does not actually create the bitmap; the bitmap must already have been created with a previous call to <code>Tk_AllocBitmapFromObj</code> or <code>Tk_GetBitmap</code>. The return value is cached in <i>objPtr</i>, which speeds up future calls to <code>Tk_GetBitmapFromObj</code> with the same <i>objPtr</i> and <i>tkwin</i>. </p>
<p> <code>Tk_DefineBitmap</code> associates a name with in-memory bitmap data so that the name can be used in later calls to <code>Tk_AllocBitmapFromObj</code> or <code>Tk_GetBitmap</code>. The <i>nameId</i> argument gives a name for the bitmap; it must not previously have been used in a call to <code>Tk_DefineBitmap</code>. The arguments <i>source</i>, <i>width</i>, and <i>height</i> describe the bitmap. <code>Tk_DefineBitmap</code> normally returns <code>TCL_OK</code>; if an error occurs (e.g. a bitmap named <i>nameId</i> has already been defined) then <code>TCL_ERROR</code> is returned and an error message is left in <i>interp-&gt;result</i>. Note: <code>Tk_DefineBitmap</code> expects the memory pointed to by <i>source</i> to be static: <code>Tk_DefineBitmap</code> does not make a private copy of this memory, but uses the bytes pointed to by <i>source</i> later in calls to <code>Tk_AllocBitmapFromObj</code> or <code>Tk_GetBitmap</code>. </p>
<p> Typically <code>Tk_DefineBitmap</code> is used by <code>#include</code>-ing a bitmap file directly into a C program and then referencing the variables defined by the file. For example, suppose there exists a file <code>stip.bitmap</code>, which was created by the <code>bitmap</code> program and contains a stipple pattern. The following code uses <code>Tk_DefineBitmap</code> to define a new bitmap named <code>foo</code>:</p>
<dl COMPACT>
<dd>
<pre>Pixmap bitmap;
#include &quot;stip.bitmap&quot;
Tk_DefineBitmap(interp, &quot;foo&quot;, stip_bits,
 stip_width, stip_height);
...
bitmap = Tk_GetBitmap(interp, tkwin, &quot;foo&quot;);</pre>
</dl>
<p> This code causes the bitmap file to be read at compile-time and incorporates the bitmap information into the program&#8217;s executable image. The same bitmap file could be read at run-time using <code>Tk_GetBitmap</code>:</p>
<dl COMPACT>
<dd>
<pre>Pixmap bitmap;
bitmap = Tk_GetBitmap(interp, tkwin, &quot;@stip.bitmap&quot;);</pre>
</dl>
<p> The second form is a bit more flexible (the file could be modified after the program has been compiled, or a different string could be provided to read a different file), but it is a little slower and requires the bitmap file to exist separately from the program. </p>
<p> Tk maintains a database of all the bitmaps that are currently in use. Whenever possible, it will return an existing bitmap rather than creating a new one. When a bitmap is no longer used, Tk will release it automatically. This approach can substantially reduce server overhead, so <code>Tk_AllocBitmapFromObj</code> and <code>Tk_GetBitmap</code> should generally be used in preference to Xlib procedures like <code>XReadBitmapFile</code>. </p>
<p> The bitmaps returned by <code>Tk_AllocBitmapFromObj</code> and <code>Tk_GetBitmap</code> are shared, so callers should never modify them. If a bitmap must be modified dynamically, then it should be created by calling Xlib procedures such as <code>XReadBitmapFile</code> or <code>XCreatePixmap</code> directly. </p>
<p> The procedure <code>Tk_NameOfBitmap</code> is roughly the inverse of <code>Tk_GetBitmap</code>. Given an X Pixmap argument, it returns the textual description that was passed to <code>Tk_GetBitmap</code> when the bitmap was created. <i>Bitmap</i> must have been the return value from a previous call to <code>Tk_AllocBitmapFromObj</code> or <code>Tk_GetBitmap</code>. </p>
<p> <code>Tk_SizeOfBitmap</code> returns the dimensions of its <i>bitmap</i> argument in the words pointed to by the <i>widthPtr</i> and <i>heightPtr</i> arguments. As with <code>Tk_NameOfBitmap</code>, <i>bitmap</i> must have been created by <code>Tk_AllocBitmapFromObj</code> or <code>Tk_GetBitmap</code>. </p>
<p> When a bitmap is no longer needed, <code>Tk_FreeBitmapFromObj</code> or <code>Tk_FreeBitmap</code> should be called to release it. For <code>Tk_FreeBitmapFromObj</code> the bitmap to release is specified with the same information used to create it; for <code>Tk_FreeBitmap</code> the bitmap to release is specified with its Pixmap token. There should be exactly one call to <code>Tk_FreeBitmapFromObj</code> or <code>Tk_FreeBitmap</code> for each call to <code>Tk_AllocBitmapFromObj</code> or <code>Tk_GetBitmap</code>. </p>
<h2>Bugs</h2>
<p>In determining whether an existing bitmap can be used to satisfy a new request, <code>Tk_AllocBitmapFromObj</code> and <code>Tk_GetBitmap</code> consider only the immediate value of the string description. For example, when a file name is passed to <code>Tk_GetBitmap</code>, <code>Tk_GetBitmap</code> will assume it is safe to re-use an existing bitmap created from the same file name: it will not check to see whether the file itself has changed, or whether the current directory has changed, thereby causing the name to refer to a different file. </p>
<h2>Keywords</h2>
<p>bitmap, pixmap</p>
