---
title: "brlapi__writewtext(3)"
name: "brlapi__writewtext"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi__writewtext/"
description: "Writing on the braille display –"
---

<p>Writing on the braille display &#8211; </p>
<p> Write text to the braille display.</p>
<h3>Data Structures</h3>
<p>struct <code>brlapi_writeArguments_t</code> </p>
<h3>Macros</h3>
<p>#define <code>BRLAPI_DISPLAY_DEFAULT</code> -1 </p>
<p> #define <code>BRLAPI_CURSOR_LEAVE</code> -1 </p>
<p> #define <code>BRLAPI_CURSOR_OFF</code> 0 </p>
<p> #define <code>BRLAPI_WRITEARGUMENTS_INITIALIZER</code> { <code>BRLAPI_DISPLAY_DEFAULT</code>, 0, 0, NULL, -1, NULL, NULL, <code>BRLAPI_CURSOR_LEAVE</code>, NULL } </p>
<h3>Functions</h3>
<p>int <code>BRLAPI_STDCALL</code> <code>brlapi_writeText</code> (int cursor, const char *text) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__writeText</code> (<code>brlapi_handle_t</code> *handle, int cursor, const char *text) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_writeWText</code> (int cursor, const wchar_t *text) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__writeWText</code> (<code>brlapi_handle_t</code> *handle, int cursor, const wchar_t *text) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_writeDots</code> (const unsigned char *dots) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__writeDots</code> (<code>brlapi_handle_t</code> *handle, const unsigned char *dots) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_write</code> (const <code>brlapi_writeArguments_t</code> *arguments) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__write</code> (<code>brlapi_handle_t</code> *handle, const <code>brlapi_writeArguments_t</code> *arguments) </p>
<h2>Detailed Description</h2>
<p>After <code>brlapi_enterTtyMode()</code> has been called, the application can call one of these functions to write things on the braille display. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Be sure to call <code>brlapi_enterTtyMode()</code> <i>before</i> calling <code>brlapi_write()</code>, or else you&#8217;ll get an error. This is particularly not always trivial when writing multithreaded applications. </p>
<p> Dots are coded as described in ISO/TR 11548-1: a dot pattern is coded by a byte in which bit 0 is set iff dot 1 is up, bit 1 is set iff dot 2 is up, &#8230; bit 7 is set iff dot 8 is up. This also corresponds to the low-order byte of the coding of unicode&#8217;s braille row U+2800. </p>
<p> Text is translated by the server one to one, by just using a simple wchar_t to pattern table, i.e. no contraction/expansion is performed, because the client would then have no way to know how wide the output would be and thus the quantity of text to feed. If contraction/expansion is desired, the client should perform it itself (e.g. thanks to liblouis or gnome-braille) and send the resulting dot patterns. This is actually exactly the same problem as font rendering on a graphical display: for better control, nowadays all font rasterization is performed on the client side, and mere pixmaps are sent to the X server.</dl>
<h2>Macro Definition Documentation</h2>
<h3>#define BRLAPI_CURSOR_LEAVE -1</h3>
<p>Do not change the cursor&#8217;s state or position. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brlapi_writeText()</code> <code>brlapi_write()</code> <code>brlapi_writeArguments_t</code></dl>
<h3>#define BRLAPI_CURSOR_OFF 0</h3>
<p>Do not display the cursor. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brlapi_writeText()</code> <code>brlapi_write()</code> <code>brlapi_writeArguments_t</code></dl>
<h3>#define BRLAPI_DISPLAY_DEFAULT -1</h3>
<p>Write to the default display on the braille device. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brlapi_write()</code> <code>brlapi_writeArguments_t</code></dl>
<h3>#define BRLAPI_WRITEARGUMENTS_INITIALIZER { <code>BRLAPI_DISPLAY_DEFAULT</code>, 0, 0, NULL, -1, NULL, NULL, <code>BRLAPI_CURSOR_LEAVE</code>, NULL }</h3>
<p>Allows to initialize a structure of type <i></i><code>brlapi_writeArguments_t</code> * with default values: displayNumber = <code>BRLAPI_DISPLAY_DEFAULT</code>; (unspecified) regionBegin = regionSize = 0; (update the whole display, DEPRECATED and will be forbidden in next release. You must always express the region you wish to update) text = andMask = orMask = NULL; (no text, no attribute) cursor = <code>BRLAPI_CURSOR_LEAVE</code>; (don&#8217;t touch cursor)</p>
<h2>Function Documentation</h2>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__write (<code>brlapi_handle_t</code> *handle, const <code>brlapi_writeArguments_t</code> *arguments)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__writeDots (<code>brlapi_handle_t</code> *handle, const unsigned char *dots)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__writeText (<code>brlapi_handle_t</code> *handle, intcursor, const char *text)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__writeWText (<code>brlapi_handle_t</code> *handle, intcursor, const wchar_t *text)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_write (const <code>brlapi_writeArguments_t</code> *arguments)</h3>
<p>Update a specific region of the braille display and apply and/or masks </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>arguments</i> gives information necessary for the update</dl>
<p> regionBegin and regionSize must be filled for specifying which part of the display will be updated, as well as the size (in characters, not bytes) of the text, andMask and orMask members. </p>
<p> If given, the &#8216;text&#8217; field holds the text that will be displayed in the region. The char string must hold exactly as many characters as the region fields express. For multibyte text, this is the number of <i>multibyte</i> caracters. Notably, combining and double-width caracters count for 1. </p>
<p> The actual length of the text in <i>bytes</i> may be specified thanks to textSize. If -1 is given, it will be computed thanks to strlen(), so &#8216;text&#8217; must then be a NUL-terminated string. </p>
<p> The &#8216;andMask&#8217; and &#8216;orMask&#8217; masks, if present, are then applied on top of the text, one byte per character. This hence permits the superimposing of attributes over the text. For instance, setting an andMask mask full of <code>BRLAPI_DOTS(1,1,1,1,1,1,0,0)</code> will only keep (logical AND) dots 1-6, hence dropping dots 7 and 8. On the contrary, setting an orMask full of BRLAPI_DOT7|BRLAPI_DOT8 will add (logical OR) dots 7 and 8. </p>
<p> The &#8216;charset&#8217; field, if present, specifies the charset of the &#8216;text&#8217; field. If it is &#8221;, the current locale&#8217;s charset (if any) is assumed. Else, the 8-bit charset of the server is assumed. </p>
<p> A special invocation is with an unmodified initialized structure: this clears the client&#8217;s whole display, letting the display of other applications on the same tty or of applications &#8216;under&#8217; the tty appear. See Concurrency management section of the BrlAPI documentation for more details. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, -1 on error.</dl>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_writeDots (const unsigned char *dots)</h3>
<p>Write the given dots array to the display </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dots</i> points on an array of dot information, one per character. Its size must hence be the same as what <code>brlapi_getDisplaySize()</code> returns.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, -1 on error.</dl>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_writeText (intcursor, const char *text)</h3>
<p>Write the given 
