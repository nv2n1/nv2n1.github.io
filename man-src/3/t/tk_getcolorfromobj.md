---
title: "tk_getcolorfromobj(3)"
name: "tk_getcolorfromobj"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getcolorfromobj/"
description: "Tk_AllocColorFromObj, Tk_GetColor, Tk_GetColorFromObj, Tk_GetColorByValue, Tk_NameOfColor, Tk_FreeColorFromObj, Tk_FreeColor – maintain database of colors"
---

<p>Tk_AllocColorFromObj, Tk_GetColor, Tk_GetColorFromObj, Tk_GetColorByValue, Tk_NameOfColor, Tk_FreeColorFromObj, Tk_FreeColor &#8211; maintain database of colors </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
XColor *
<code>Tk_AllocColorFromObj(</code><i>interp, tkwin, objPtr</i><code>)</code>
XColor *
<code>Tk_GetColor(</code><i>interp, tkwin, name</i><code>)</code>
XColor *
<code>Tk_GetColorFromObj(</code><i>tkwin, objPtr</i><code>)</code>
XColor *
<code>Tk_GetColorByValue(</code><i>tkwin, prefPtr</i><code>)</code>
const char *
<code>Tk_NameOfColor(</code><i>colorPtr</i><code>)</code>
GC
<code>Tk_GCForColor(</code><i>colorPtr, drawable</i><code>)</code>
<code>Tk_FreeColorFromObj(</code><i>tkwin, objPtr</i><code>)</code>
<code>Tk_FreeColor(</code><i>colorPtr</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting.</p>
<dd>Tk_Window <i>tkwin</i> (in) Token for window in which color will be used.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in/out) String value describes desired color; internal rep will be modified to cache pointer to corresponding (XColor *).</p>
<dd>char <i>*name</i> (in) Same as <i>objPtr</i> except description of color is passed as a string and resulting (XColor *) is not cached.</p>
<dd>XColor <i>*prefPtr</i> (in) Indicates red, green, and blue intensities of desired color.</p>
<dd>XColor <i>*colorPtr</i> (in) Pointer to X color information. Must have been allocated by previous call to <code>Tk_AllocColorFromObj</code>, <code>Tk_GetColor</code> or <code>Tk_GetColorByValue</code>, except when passed to <code>Tk_NameOfColor</code>.</p>
<dd>Drawable <i>drawable</i> (in) Drawable in which the result graphics context will be used. Must have same screen and depth as the window for which the color was allocated. </p>
</dl>
<h2>Description</h2>
<p>These procedures manage the colors being used by a Tk application. They allow colors to be shared whenever possible, so that colormap space is preserved, and they pick closest available colors when colormap space is exhausted. </p>
<p> Given a textual description of a color, <code>Tk_AllocColorFromObj</code> locates a pixel value that may be used to render the color in a particular window. The desired color is specified with an object whose string value must have one of the following forms:</p>
<dl COMPACT>
<dt><i>colorname</i></p>
<dd>Any of the valid textual names for a color defined in the server&#8217;s color database file, such as <code>red</code> or <code>PeachPuff</code>.</p>
<dt><code>#</code><i>RGB</i></p>
<dd>
<dt><code>#</code><i>RRGGBB</i></p>
<dd>
<dt><code>#</code><i>RRRGGGBBB</i></p>
<dd>
<dt><code>#</code><i>RRRRGGGGBBBB</i></p>
<dd>A numeric specification of the red, green, and blue intensities to use to display the color. Each <i>R</i>, <i>G</i>, or <i>B</i> represents a single hexadecimal digit. The four forms permit colors to be specified with 4-bit, 8-bit, 12-bit or 16-bit values. When fewer than 16 bits are provided for each color, they represent the most significant bits of the color, while the lower unfilled bits will be repeatedly replicated from the available higher bits. For example, #3a7 is the same as #3333aaaa7777.</dl>
<p> <code>Tk_AllocColorFromObj</code> returns a pointer to an XColor structure; the structure indicates the exact intensities of the allocated color (which may differ slightly from those requested, depending on the limitations of the screen) and a pixel value that may be used to draw with the color in <i>tkwin</i>. If an error occurs in <code>Tk_AllocColorFromObj</code> (such as an unknown color name) then NULL is returned and an error message is stored in <i>interp</i>&#8216;s result if <i>interp</i> is not NULL. If the colormap for <i>tkwin</i> is full, <code>Tk_AllocColorFromObj</code> will use the closest existing color in the colormap. <code>Tk_AllocColorFromObj</code> caches information about the return value in <i>objPtr</i>, which speeds up future calls to procedures such as <code>Tk_AllocColorFromObj</code> and <code>Tk_GetColorFromObj</code>. </p>
<p> <code>Tk_GetColor</code> is identical to <code>Tk_AllocColorFromObj</code> except that the description of the color is specified with a string instead of an object. This prevents <code>Tk_GetColor</code> from caching the return value, so <code>Tk_GetColor</code> is less efficient than <code>Tk_AllocColorFromObj</code>. </p>
<p> <code>Tk_GetColorFromObj</code> returns the token for an existing color, given the window and description used to create the color. <code>Tk_GetColorFromObj</code> does not actually create the color; the color must already have been created with a previous call to <code>Tk_AllocColorFromObj</code> or <code>Tk_GetColor</code>. The return value is cached in <i>objPtr</i>, which speeds up future calls to <code>Tk_GetColorFromObj</code> with the same <i>objPtr</i> and <i>tkwin</i>. </p>
<p> <code>Tk_GetColorByValue</code> is similar to <code>Tk_GetColor</code> except that the desired color is indicated with the <i>red</i>, <i>green</i>, and <i>blue</i> fields of the structure pointed to by <i>colorPtr</i>. </p>
<p> This package maintains a database of all the colors currently in use. If the same color is requested multiple times from <code>Tk_GetColor</code> or <code>Tk_AllocColorFromObj</code> (e.g. by different windows), or if the same intensities are requested multiple times from <code>Tk_GetColorByValue</code>, then existing pixel values will be re-used. Re-using an existing pixel avoids any interaction with the window server, which makes the allocation much more efficient. These procedures also provide a portable interface that works across all platforms. For this reason, you should generally use <code>Tk_AllocColorFromObj</code>, <code>Tk_GetColor</code>, or <code>Tk_GetColorByValue</code> instead of lower level procedures like <code>XAllocColor</code>. </p>
<p> Since different calls to this package may return the same shared pixel value, callers should never change the color of a pixel returned by the procedures. If you need to change a color value dynamically, you should use <code>XAllocColorCells</code> to allocate the pixel value for the color. </p>
<p> The procedure <code>Tk_NameOfColor</code> is roughly the inverse of <code>Tk_GetColor</code>. If its <i>colorPtr</i> argument was created by <code>Tk_AllocColorFromObj</code> or <code>Tk_GetColor</code> then the return value is the string that was used to create the color. If <i>colorPtr</i> was created by a call to <code>Tk_GetColorByValue</code>, or by any other mechanism, then the return value is a string that could be passed to <code>Tk_GetColor</code> to return the same color. Note: the string returned by <code>Tk_NameOfColor</code> is only guaranteed to persist until the next call to <code>Tk_NameOfColor</code>. </p>
<p> <code>Tk_GCForColor</code> returns a graphics context whose <code>foreground</code> field is the pixel allocated for <i>colorPtr</i> and whose other fields all have default values. This provides an easy way to do basic drawing with a color. The graphics context is cached with the color and will exist only as long as <i>colorPtr</i> exists; it is freed when the last reference to <i>colorPtr</i> is freed by calling <code>Tk_FreeColor</code>. </p>
<p> When a color is no longer needed <code>Tk_FreeColorFromObj</code> or <code>Tk_FreeColor</code> should be called to release it. For <code>Tk_FreeColorFromObj</code> the color to release is specified with the same information used to create it; for <code>Tk_FreeColor</code> the color to release is specified with a pointer to its XColor structure. There should be exactly one call to <code>Tk_FreeColorFromObj</code> or <code>Tk_FreeColor</code> for each call to <code>Tk_AllocColorFromObj</code>, <code>Tk_GetColor</code>, or <code>Tk_GetColorByValue</code>.</p>
<h2>Keywords</h2>
<p>color, intensity, object, pixel value</p>
