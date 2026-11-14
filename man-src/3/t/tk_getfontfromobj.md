---
title: "tk_getfontfromobj(3)"
name: "tk_getfontfromobj"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getfontfromobj/"
description: "Tk_AllocFontFromObj, Tk_GetFont, Tk_GetFontFromObj, Tk_NameOfFont, Tk_FreeFontFromObj, Tk_FreeFont – maintain database of fonts"
---

<p>Tk_AllocFontFromObj, Tk_GetFont, Tk_GetFontFromObj, Tk_NameOfFont, Tk_FreeFontFromObj, Tk_FreeFont &#8211; maintain database of fonts </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_Font 
<code>Tk_AllocFontFromObj(</code><i>interp, tkwin, objPtr</i><code>)</code>
Tk_Font 
<code>Tk_GetFont(</code><i>interp, tkwin, string</i><code>)</code> 
Tk_Font 
<code>Tk_GetFontFromObj(</code><i>tkwin, objPtr</i><code>)</code>
const char *
<code>Tk_NameOfFont(</code><i>tkfont</i><code>)</code>
Tk_Font 
<code>Tk_FreeFontFromObj(</code><i>tkwin, objPtr</i><code>)</code>
void
<code>Tk_FreeFont(</code><i>tkfont</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting. If <code>NULL</code>, then no error messages are left after errors.</p>
<dd>Tk_Window <i>tkwin</i> (in) Token for window in which font will be used.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in/out) Gives name or description of font. See documentation for the <code>font</code> command for details on acceptable formats. Internal rep will be modified to cache corresponding Tk_Font.</p>
<dd>const char <i>*string</i> (in) Same as <i>objPtr</i> except description of font is passed as a string and resulting Tk_Font is not cached.</p>
<dd>Tk_Font <i>tkfont</i> (in) Opaque font token.
</dl>
<h2>Description</h2>
<p><code>Tk_AllocFontFromObj</code> finds the font indicated by <i>objPtr</i> and returns a token that represents the font. The return value can be used in subsequent calls to procedures such as <code>Tk_GetFontMetrics</code>, <code>Tk_MeasureChars</code>, and <code>Tk_FreeFont</code>. The Tk_Font token will remain valid until <code>Tk_FreeFontFromObj</code> or <code>Tk_FreeFont</code> is called to release it. <i>ObjPtr</i> can contain either a symbolic name or a font description; see the documentation for the <code>font</code> command for a description of the valid formats. If <code>Tk_AllocFontFromObj</code> is unsuccessful (because, for example, <i>objPtr</i> did not contain a valid font specification) then it returns <code>NULL</code> and leaves an error message in <i>interp</i>&#8216;s result if <i>interp</i> is not <code>NULL</code>. <code>Tk_AllocFontFromObj</code> caches information about the return value in <i>objPtr</i>, which speeds up future calls to procedures such as <code>Tk_AllocFontFromObj</code> and <code>Tk_GetFontFromObj</code>. </p>
<p> <code>Tk_GetFont</code> is identical to <code>Tk_AllocFontFromObj</code> except that the description of the font is specified with a string instead of an object. This prevents <code>Tk_GetFont</code> from caching the matching Tk_Font, so <code>Tk_GetFont</code> is less efficient than <code>Tk_AllocFontFromObj</code>. </p>
<p> <code>Tk_GetFontFromObj</code> returns the token for an existing font, given the window and description used to create the font. <code>Tk_GetFontFromObj</code> does not actually create the font; the font must already have been created with a previous call to <code>Tk_AllocFontFromObj</code> or <code>Tk_GetFont</code>. The return value is cached in <i>objPtr</i>, which speeds up future calls to <code>Tk_GetFontFromObj</code> with the same <i>objPtr</i> and <i>tkwin</i>. </p>
<p> <code>Tk_AllocFontFromObj</code> and <code>Tk_GetFont</code> maintain a database of all fonts they have allocated. If the same font is requested multiple times (e.g. by different windows or for different purposes), then a single Tk_Font will be shared for all uses. The underlying resources will be freed automatically when no-one is using the font anymore. </p>
<p> The procedure <code>Tk_NameOfFont</code> is roughly the inverse of <code>Tk_GetFont</code>. Given a <i>tkfont</i> that was created by <code>Tk_GetFont</code> (or <code>Tk_AllocFontFromObj</code>), the return value is the <i>string</i> argument that was passed to <code>Tk_GetFont</code> to create the font. The string returned by <code>Tk_NameOfFont</code> is only guaranteed to persist until the <i>tkfont</i> is deleted. The caller must not modify this string. </p>
<p> When a font is no longer needed, <code>Tk_FreeFontFromObj</code> or <code>Tk_FreeFont</code> should be called to release it. For <code>Tk_FreeFontFromObj</code> the font to release is specified with the same information used to create it; for <code>Tk_FreeFont</code> the font to release is specified with its Tk_Font token. There should be exactly one call to <code>Tk_FreeFontFromObj</code> or <code>Tk_FreeFont</code> for each call to <code>Tk_AllocFontFromObj</code> or <code>Tk_GetFont</code>. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tk_fontid/">Tk_FontId</a>(3)</p>
<h2>Keywords</h2>
<p>font</p>
