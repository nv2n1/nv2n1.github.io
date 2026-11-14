---
title: "xgetfontproperty(3)"
name: "xgetfontproperty"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgetfontproperty/"
description: "XLoadFont, XQueryFont, XLoadQueryFont, XFreeFont, XGetFontProperty, XUnloadFont, XCharStruct, XFontProp, XChar2b, XFontStruct – load or unload fonts and font metric structures"
---

<p>XLoadFont, XQueryFont, XLoadQueryFont, XFreeFont, XGetFontProperty, XUnloadFont, XCharStruct, XFontProp, XChar2b, XFontStruct &#8211; load or unload fonts and font metric structures </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Font XLoadFont(Display *<i>display</i>, char *<i>name</i>);</p>
<dd>XFontStruct *XQueryFont(Display *<i>display</i>, XID <i>font_ID</i>);</p>
<dd>XFontStruct *XLoadQueryFont(Display *<i>display</i>, char *<i>name</i>);</p>
<dd>int XFreeFont(Display *<i>display</i>, XFontStruct *<i>font_struct</i>);</p>
<dd>Bool XGetFontProperty(XFontStruct *<i>font_struct</i>, Atom <i>atom</i>, unsigned long *<i>value_return</i>);</p>
<dd>int XUnloadFont(Display *<i>display</i>, Font <i>font</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>atom</i></p>
<dd>Specifies the atom for the property name you want returned.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>font</i></p>
<dd>Specifies the font.</p>
<dt><i>font_ID</i></p>
<dd>Specifies the font ID or the <code>GContext</code> ID.</p>
<dt><i>font_struct</i></p>
<dd>Specifies the storage associated with the font.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the font, which is a null-terminated string.</p>
<dt><i>value_return</i></p>
<dd>Returns the value of the font property.</dl>
<h2>Description</h2>
<p>The <code>XLoadFont</code> function loads the specified font and returns its associated font ID. If the font name is not in the Host Portable Character Encoding, the result is implementation-dependent. Use of uppercase or lowercase does not matter. When the characters &#8220;?&#8221; and &#8220;&#8221; are used in a font name, a pattern match is performed and any matching font is used. In the pattern, the &#8220;?&#8221; character will match any single character, and the &#8220;*&#8221; character will match any number of characters. A structured format for font names is specified in the X Consortium standard <i>X Logical Font Description Conventions</i>. If <code>XLoadFont</code> was unsuccessful at loading the specified font, a <code>BadName</code> error results. Fonts are not associated with a particular screen and can be stored as a component of any GC. When the font is no longer needed, call <code>XUnloadFont</code>. </p>
<p> <code>XLoadFont</code> can generate <code>BadAlloc</code> and <code>BadName</code> errors. </p>
<p> The <code>XQueryFont</code> function returns a pointer to the <code>XFontStruct</code> structure, which contains information associated with the font. You can query a font or the font stored in a GC. The font ID stored in the <code>XFontStruct</code> structure will be the <code>GContext</code> ID, and you need to be careful when using this ID in other functions (see <code>XGContextFromGC</code>). If the font does not exist, <code>XQueryFont</code> returns NULL. To free this data, use <code>XFreeFontInfo</code>. </p>
<p> <code>XLoadQueryFont</code> can generate a <code>BadAlloc</code> error. </p>
<p> The <code>XLoadQueryFont</code> function provides the most common way for accessing a font. <code>XLoadQueryFont</code> both opens (loads) the specified font and returns a pointer to the appropriate <code>XFontStruct</code> structure. If the font name is not in the Host Portable Character Encoding, the result is implementation-dependent. If the font does not exist, <code>XLoadQueryFont</code> returns NULL. </p>
<p> The <code>XFreeFont</code> function deletes the association between the font resource ID and the specified font and frees the <code>XFontStruct</code> structure. The font itself will be freed when no other resource references it. The data and the font should not be referenced again. </p>
<p> <code>XFreeFont</code> can generate a <code>BadFont</code> error. </p>
<p> Given the atom for that property, the <code>XGetFontProperty</code> function returns the value of the specified font property. <code>XGetFontProperty</code> also returns <code>False</code> if the property was not defined or <code>True</code> if it was defined. A set of predefined atoms exists for font properties, which can be found in This set contains the standard properties associated with a font. Although it is not guaranteed, it is likely that the predefined font properties will be present. </p>
<p> The <code>XUnloadFont</code> function deletes the association between the font resource ID and the specified font. The font itself will be freed when no other resource references it. The font should not be referenced again. </p>
<p> <code>XUnloadFont</code> can generate a <code>BadFont</code> error.</p>
<h2>Structures</h2>
<p>The <code>XFontStruct</code> structure contains all of the information for the font and consists of the font-specific information as well as a pointer to an array of <code>XCharStruct</code> structures for the characters contained in the font. The <code>XFontStruct</code>, <code>XFontProp</code>, and <code>XCharStruct</code> structures contain: </p>
<pre>typedef struct {
 short lbearing; /* origin to left edge of raster */
 short rbearing; /* origin to right edge of raster */
 short width; /* advance to next char's origin */
 short ascent; /* baseline to top edge of raster */
 short descent; /* baseline to bottom edge of raster */
 unsigned short attributes; /* per char flags (not predefined) */
} XCharStruct;</pre>
<pre>typedef struct {
 Atom name;
 unsigned long card32;
} XFontProp;</pre>
<pre>typedef struct { /* normal 16 bit characters are two bytes */
 unsigned char byte1;
 unsigned char byte2;
} XChar2b;</pre>
<pre>typedef struct {
 XExtData *ext_data; /* hook for extension to hang data */
 Font fid; /* Font id for this font */
 unsigned direction; /* hint about the direction font is painted */
 unsigned min_char_or_byte2; /* first character */
 unsigned max_char_or_byte2; /* last character */
 unsigned min_byte1; /* first row that exists */
 unsigned max_byte1; /* last row that exists */
 Bool all_chars_exist; /* flag if all characters have nonzero size */
 unsigned default_char; /* char to print for undefined character */
 int n_properties; /* how many properties there are */
 XFontProp *properties; /* pointer to array of additional properties */
 XCharStruct min_bounds; /* minimum bounds over all existing char */
 XCharStruct max_bounds; /* maximum bounds over all existing char */
 XCharStruct *per_char; /* first_char to last_char information */
 int ascent; /* logical extent above baseline for spacing */
 int descent; /* logical decent below baseline for spacing */
} XFontStruct;</pre>
<p>X supports single byte/character, two bytes/character matrix, and 16-bit character text operations. Note that any of these forms can be used with a font, but a single byte/character text request can only specify a single byte (that is, the first row of a 2-byte font). You should view 2-byte fonts as a two-dimensional matrix of defined characters: byte1 specifies the range of defined rows and byte2 defines the range of defined columns of the font. Single byte/character fonts have one row defined, and the byte2 range specified in the structure defines a range of characters. </p>
<p> The bounding box of a character is defined by the <code>XCharStruct</code> of that character. When characters are absent from a font, the default_char is used. When fonts have all characters of the same size, only the information in the <code>XFontStruct</code> min and max bounds are used. </p>
<p> The members of the <code>XFontStruct</code> have the following semantics:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>The direction member can be either <code>FontLeftToRight</code> or <code>FontRightToLeft</code>. It is just a hint as to whether most <code>XCharStruct</code> elements have a positive or a negative character width metric. The core protocol defines no support for vertical text.</p>
<dt>&bull;</p>
<dd>If the min_byte1 and max_byte1 members are both zero, min_char_or_byte2 specifies the linear character index corresponding to the first element of the per_char array, and max_char_or_byte2 specifies the linear character index of the last element.</p>
<dd>If either min_byte1 or max_byte1 are nonzero, both min_char_or_byte2 and max_char_or_byte2 are less than 256, and the 2-byte character index values corresponding to the per_char array element N (counting from 0) are:</p>
<dd>
<pre> byte1 = N/D + min_byte1
 byte2 = N\D + min_char_or_byte2</pre>
<p>where: </p>
<pre> D = max_char_or_byte2 - min_char_or_byte2 + 1
 / = integer division
 \ = integer modulus</pre>
<dt>&bull;</p>
<dd>If the per_char pointer is NULL, all glyphs between the first and last character indexes inclusive have the same information, as given by both min_bounds and max_bounds.</p>
<dt>&bull;</p>
<dd>If all_chars_exist is <code>True</code>, all characters in the per_char array have nonzero bounding boxes.</p>
<dt>&bull;</p>
<dd>The default_char member specifies the character that will be used when an undefined or nonexistent character is printed. The default_char is a 16-bit character (not a 2-byte character). For a font using 2-byte matrix format, the default_char has byte1 in the most-significant byte and byte2 in the least significant byte. If the default_char itself specifies an undefined or nonexistent character, no printing is performed for an undefined or nonexistent character.</p>
<dt>&bull;</p>
<dd>The min_bounds and max_bounds members contain the most extreme values of each individual <code>XCharStruct</code> component over all elements of this array (and ignore nonexistent characters). The bounding box of the font (the smallest rectangle enclosing the shape obtained by superimposing all of the characters at the same origin [x,y]) has its upper-left coordinate at: </p>
<pre> [x + min_bounds.lbearing, y - max_bounds.ascent]</pre>
<dd>Its width is: </p>
<pre> max_bounds.rbearing - min_bounds.lbearing</pre>
<dd>Its height is: </p>
<pre> max_bounds.ascent + max_bounds.descent</pre>
<dt>&bull;</p>
<dd>The ascent member is the logical extent of the font above the baseline that is used for determining line spacing. Specific characters may extend beyond this.</p>
<dt>&bull;</p>
<dd>The descent member is the logical extent of the font at or below the baseline that is used for determining line spacing. Specific characters may extend beyond this.</p>
<dt>&bull;</p>
<dd>If the baseline is at Y-coordinate y, the logical extent of the font is inclusive between the Y-coordinate values (y &#8211; font.ascent) and (y + font.descent &#8211; 1). Typically, the minimum interline spacing between rows of text is given by ascent + descent.</dl>
<p> For a character origin at [x,y], the bounding box of a character (that is, the smallest rectangle that encloses the character&#8217;s shape) described in terms of <code>XCharStruct</code> components is a rectangle with its upper-left corner at: </p>
<pre>[x + lbearing, y - ascent]</pre>
<p>Its width is: </p>
<pre>rbearing - lbearing</pre>
<p>Its height is: </p>
<pre>ascent + descent</pre>
<p>The origin for the next character is defined to be: </p>
<pre>[x + width, y]</pre>
<p>The lbearing member defines the extent of the left edge of the character ink from the origin. The rbearing member defines the extent of the right edge of the character ink from the origin. The ascent member defines the extent of the top edge of the character ink from the origin. The descent member defines the extent of the bottom edge of the character ink from the origin. The width member defines the logical width of the character.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadFont</code></p>
<dd>A value for a Font or GContext argument does not name a defined Font.</p>
<dt><code>BadName</code></p>
<dd>A font or color of the specified name does not exist.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreategc/">XCreateGC</a>(3), <a href="/docs/linux/man/3-xlistfonts/">XListFonts</a>(3), <a href="/docs/linux/man/3-xsetfontpath/">XSetFontPath</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
