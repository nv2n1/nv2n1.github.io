---
title: "xquerycolor(3)"
name: "xquerycolor"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xquerycolor/"
description: "XQueryColor, XQueryColors, XLookupColor, XParseColor – obtain color values"
---

<p>XQueryColor, XQueryColors, XLookupColor, XParseColor &#8211; obtain color values </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XQueryColor(Display *<i>display</i>, Colormap <i>colormap</i>, XColor *<i>def_in_out</i>);</p>
<dd>int XQueryColors(Display *<i>display</i>, Colormap <i>colormap</i>, XColor <i>defs_in_out</i>[], int <i>ncolors</i>);</p>
<dd>Status XLookupColor(Display *<i>display</i>, Colormap <i>colormap</i>, char *<i>color_name</i>, XColor *<i>exact_def_return</i>, XColor *<i>screen_def_return</i>);</p>
<dd>Status XParseColor(Display *<i>display</i>, Colormap <i>colormap</i>, char *<i>spec</i>, XColor *<i>exact_def_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>colormap</i></p>
<dd>Specifies the colormap.</p>
<dt><i>color_name</i></p>
<dd>Specifies the color name string (for example, red) whose color definition structure you want returned.</p>
<dt><i>def_in_out</i></p>
<dd>Specifies and returns the RGB values for the pixel specified in the structure.</p>
<dt><i>defs_in_out</i></p>
<dd>Specifies and returns an array of color definition structures for the pixel specified in the structure.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>exact_def_return</i></p>
<dd>Returns the exact RGB values.</p>
<dt><i>ncolors</i></p>
<dd>Specifies the number of <code>XColor</code> structures in the color definition array.</p>
<dt><i>screen_def_return</i></p>
<dd>Returns the closest RGB values provided by the hardware.</p>
<dt><i>spec</i></p>
<dd>Specifies the color name string; case is ignored.</p>
<dt><i>exact_def_return</i></p>
<dd>Returns the exact color value for later use and sets the <code>DoRed</code>, <code>DoGreen</code>, and <code>DoBlue</code> flags.</dl>
<h2>Description</h2>
<p>The <code>XQueryColor</code> function returns the current RGB value for the pixel in the <code>XColor</code> structure and sets the <code>DoRed</code>, <code>DoGreen</code>, and <code>DoBlue</code> flags. The <code>XQueryColors</code> function returns the RGB value for each pixel in each <code>XColor</code> structure and sets the <code>DoRed</code>, <code>DoGreen</code>, and <code>DoBlue</code> flags in each structure. </p>
<p> <code>XQueryColor</code> and <code>XQueryColors</code> can generate <code>BadColor</code> and <code>BadValue</code> errors. </p>
<p> The <code>XLookupColor</code> function looks up the string name of a color with respect to the screen associated with the specified colormap. It returns both the exact color values and the closest values provided by the screen with respect to the visual type of the specified colormap. If the color name is not in the Host Portable Character Encoding, the result is implementation-dependent. Use of uppercase or lowercase does not matter. <code>XLookupColor</code> returns nonzero if the name is resolved; otherwise, it returns zero. </p>
<p> The <code>XParseColor</code> function looks up the string name of a color with respect to the screen associated with the specified colormap. It returns the exact color value. If the color name is not in the Host Portable Character Encoding, the result is implementation-dependent. Use of uppercase or lowercase does not matter. <code>XParseColor</code> returns nonzero if the name is resolved; otherwise, it returns zero. </p>
<p> <code>XLookupColor</code> and <code>XParseColor</code> can generate <code>BadColor</code> error.</p>
<h2>Color Names</h2>
<p>An RGB Device specification is identified by the prefix &#8220;rgb:&#8221; and conforms to the following syntax: </p>
<p> rgb:<i>&lt;red&gt;/&lt;green&gt;/&lt;blue&gt;</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>&lt;red&gt;</i>,&nbsp;<i>&lt;green&gt;</i>,&nbsp;<i>&lt;blue&gt;</i>&nbsp;:=&nbsp;<i>h</i>&nbsp;|&nbsp;<i>hh</i>&nbsp;|&nbsp;<i>hhh</i>&nbsp;|&nbsp;<i>hhhh</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>h</i>&nbsp;:=&nbsp;single hexadecimal digits&nbsp;(case insignificant) </p>
<p> Note that <i>h</i> indicates the value scaled in 4 bits, <i>hh</i> the value scaled in 8 bits, <i>hhh</i> the value scaled in 12 bits, and <i>hhhh</i> the value scaled in 16 bits, respectively. </p>
<p> For backward compatibility, an older syntax for RGB Device is supported, but its continued use is not encouraged. The syntax is an initial sharp sign character followed by a numeric specification, in one of the following formats: </p>
<table>
<tr VALIGN=top>
<td>#RGB</td>
<td>(4 bits each)
</td>
</tr>
<tr VALIGN=top>
<td>#RRGGBB</td>
<td>(8 bits each)
</td>
</tr>
<tr VALIGN=top>
<td>#RRRGGGBBB</td>
<td>(12 bits each)
</td>
</tr>
<tr VALIGN=top>
<td>#RRRRGGGGBBBB</td>
<td>(16 bits each)
</td>
</tr>
</table>
<p> The R, G, and B represent single hexadecimal digits. When fewer than 16 bits each are specified, they represent the most significant bits of the value (unlike the &#8220;rgb:&#8221; syntax, in which values are scaled). For example, the string &#8220;#3a7&#8221; is the same as &#8220;#3000a0007000&#8221;. </p>
<p> An RGB intensity specification is identified by the prefix &#8220;rgbi:&#8221; and conforms to the following syntax: </p>
<p> rgbi:<i>&lt;red&gt;/&lt;green&gt;/&lt;blue&gt;</i> </p>
<p> Note that red, green, and blue are floating-point values between 0.0 and 1.0, inclusive. The input format for these values is an optional sign, a string of numbers possibly containing a decimal point, and an optional exponent field containing an E or e followed by a possibly signed integer string. </p>
<p> The standard device-independent string specifications have the following syntax: </p>
<p> CIEXYZ:<i>&lt;X&gt;/&lt;Y&gt;/&lt;Z&gt;</i> CIEuvY:<i>&lt;u&gt;/&lt;v&gt;/&lt;Y&gt;</i> CIExyY:<i>&lt;x&gt;/&lt;y&gt;/&lt;Y&gt;</i> CIELab:<i>&lt;L&gt;/&lt;a&gt;/&lt;b&gt;</i> CIELuv:<i>&lt;L&gt;/&lt;u&gt;/&lt;v&gt;</i> TekHVC:<i>&lt;H&gt;/&lt;V&gt;/&lt;C&gt;</i> </p>
<p> All of the values (C, H, V, X, Y, Z, a, b, u, v, y, x) are floating-point values. The syntax for these values is an optional plus or minus sign, a string of digits possibly containing a decimal point, and an optional exponent field consisting of an &#8220;E&#8221; or &#8220;e&#8221; followed by an optional plus or minus followed by a string of digits.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadColor</code></p>
<dd>A value for a Colormap argument does not name a defined Colormap.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xalloccolor/">XAllocColor</a>(3), <a href="/docs/linux/man/3-xcreatecolormap/">XCreateColormap</a>(3), <a href="/docs/linux/man/3-xstorecolors/">XStoreColors</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
