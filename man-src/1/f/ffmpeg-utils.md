---
title: "ffmpeg-utils(1)"
name: "ffmpeg-utils"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffmpeg-utils/"
description: "ffmpeg-utils – FFmpeg utilities"
---

<h2 class="name">NAME</h2>
<p> ffmpeg-utils &#8211; FFmpeg utilities </p>
<h2>DESCRIPTION</h2>
<p> This document describes some generic features and utilities provided by the libavutil library.</p>
<h2>SYNTAX</h2>
<p> This section documents the syntax and formats employed by the FFmpeg libraries and tools.</p>
<h3>Quoting and escaping</h3>
<p> FFmpeg adopts the following quoting and escaping mechanism, unless explicitly specified. The following rules are applied:</p>
<dl>
<dt>&bull;</dt>
<dd> <code>&#8216;</code> and <code>\</code> are special characters (respectively used for quoting and escaping). In addition to them, there might be other special characters depending on the specific syntax where the escaping and quoting are employed.</dd>
<dt>&bull;</dt>
<dd> A special character is escaped by prefixing it with a <code>\</code>.</dd>
<dt>&bull;</dt>
<dd> All characters enclosed between <code>&#8221;</code> are included literally in the parsed string. The quote character <code>&#8216;</code> itself cannot be quoted, so you may need to close the quote and escape it.</dd>
<dt>&bull;</dt>
<dd> Leading and trailing whitespaces, unless escaped or quoted, are removed from the parsed string.</dd></dl>
<p> Note that you may need to add a second level of escaping when using the command line or a script, which depends on the syntax of the adopted shell language. </p>
<p> The function <tt>&quot;av_get_token&quot;</tt> defined in <i>libavutil/avstring.h</i> can be used to parse a token quoted or escaped according to the rules defined above. </p>
<p> The tool <i>tools/ffescape</i> in the FFmpeg source tree can be used to automatically quote or escape a string in a script. </p>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</dt>
<dd> Escape the string <tt>&quot;Crime d'Amour&quot;</tt> containing the <tt>&quot;'&quot;</tt> special character: </dd>
<pre>
        Crime d\'Amour
</pre>
<dt>&bull;</dt>
<dd> The string above contains a quote, so the <tt>&quot;'&quot;</tt> needs to be escaped when quoting it: </dd>
<pre>
        'Crime d'\''Amour'
</pre>
<dt>&bull;</dt>
<dd> Include leading or trailing whitespaces using quoting: </dd>
<pre>
        '  this string starts and ends with whitespaces  '
</pre>
<dt>&bull;</dt>
<dd> Escaping and quoting can be mixed together: </dd>
<pre>
        ' The string '\'string\'' is a string '
</pre>
<dt>&bull;</dt>
<dd> To include a literal <code>\</code> you can use either escaping or quoting: </dd>
<pre>
        'c:oo' can be written as c:\foo
</pre>
</dl>
<h3>Date</h3>
<p> The accepted syntax is: </p>
<pre><code>
        [(YYYY-MM-DD|YYYYMMDD)[T|t| ]]((HH:MM:SS[.m...]]])|(HHMMSS[.m...]]]))[Z]
        now
</code></pre>
<p> If the value is &#8220;now&#8221; it takes the current time. </p>
<p> Time is local time unless Z is appended, in which case it is interpreted as <font SIZE="-1">UTC.</font> If the year-month-day part is not specified it takes the current year-month-day.</p>
<h3>Time duration</h3>
<p> There are two accepted syntaxes for expressing time duration. </p>
<p>[-] [&lt;HH&gt;:]&lt;MM&gt; : &lt;SS&gt;[.&lt;m&gt;&#8230;]</p>
<p> <i></i><font SIZE="-1"><i>HH</i></font><i></i> expresses the number of hours, <i></i><font SIZE="-1"><i>MM</i></font><i></i> the number of minutes for a maximum of 2 digits, and <i></i><font SIZE="-1"><i>SS</i></font><i></i> the number of seconds for a maximum of 2 digits. The <i>m</i> at the end expresses decimal value for <i></i><font SIZE="-1"><i>SS</i></font><i></i>. </p>
<p> <i>or</i> </p>
<pre><code>
[-]&lt;S&gt; + [.&lt;m&gt;...][s | ms | us]
</code></pre>
<p> <i>S</i> expresses the number of seconds, with the optional decimal part <i>m</i>. The optional literal suffixes <code>s</code>, <code>ms</code> or <code>us</code> indicate to interpret the value as seconds, milliseconds or microseconds, respectively. </p>
<p> In both expressions, the optional <code>&#8211;</code> indicates negative duration. </p>
<p> <i>Examples</i> </p>
<p> The following examples are all valid time duration:</p>
<dl>
<dt><code>55</code></dt>
<dd> 55 seconds</dd>
<dt><code>0.2</code></dt>
<dd> 0.2 seconds</dd>
<dt><code>200ms</code></dt>
<dd> 200 milliseconds, that&#8217;s 0.2s</dd>
<dt><code>200000us</code></dt>
<dd> 200000 microseconds, that&#8217;s 0.2s</dd>
<dt><code>12:03:45</code></dt>
<dd> 12 hours, 03 minutes and 45 seconds</dd>
<dt><code>23.189</code></dt>
<dd> 23.189 seconds</dd></dl>
<h3>Video size</h3>
<p> Specify the size of the sourced video, it may be a string of the form <i>width</i>x<i>height</i>, or the name of a size abbreviation. </p>
<p> The following abbreviations are recognized:</p>
<dl>
<dt><code>ntsc</code></dt>
<dd> 720&#215;480</dd>
<dt><code>pal</code></dt>
<dd> 720&#215;576</dd>
<dt><code>qntsc</code></dt>
<dd> 352&#215;240</dd>
<dt><code>qpal</code></dt>
<dd> 352&#215;288</dd>
<dt><code>sntsc</code></dt>
<dd> 640&#215;480</dd>
<dt><code>spal</code></dt>
<dd> 768&#215;576</dd>
<dt><code>film</code></dt>
<dd> 352&#215;240</dd>
<dt><code>ntsc-film</code></dt>
<dd> 352&#215;240</dd>
<dt><code>sqcif</code></dt>
<dd> 128&#215;96</dd>
<dt><code>qcif</code></dt>
<dd> 176&#215;144</dd>
<dt><code>cif</code></dt>
<dd> 352&#215;288</dd>
<dt><code>4cif</code></dt>
<dd> 704&#215;576</dd>
<dt><code>16cif</code></dt>
<dd> 1408&#215;1152</dd>
<dt><code>qqvga</code></dt>
<dd> 160&#215;120</dd>
<dt><code>qvga</code></dt>
<dd> 320&#215;240</dd>
<dt><code>vga</code></dt>
<dd> 640&#215;480</dd>
<dt><code>svga</code></dt>
<dd> 800&#215;600</dd>
<dt><code>xga</code></dt>
<dd> 1024&#215;768</dd>
<dt><code>uxga</code></dt>
<dd> 1600&#215;1200</dd>
<dt><code>qxga</code></dt>
<dd> 2048&#215;1536</dd>
<dt><code>sxga</code></dt>
<dd> 1280&#215;1024</dd>
<dt><code>qsxga</code></dt>
<dd> 2560&#215;2048</dd>
<dt><code>hsxga</code></dt>
<dd> 5120&#215;4096</dd>
<dt><code>wvga</code></dt>
<dd> 852&#215;480</dd>
<dt><code>wxga</code></dt>
<dd> 1366&#215;768</dd>
<dt><code>wsxga</code></dt>
<dd> 1600&#215;1024</dd>
<dt><code>wuxga</code></dt>
<dd> 1920&#215;1200</dd>
<dt><code>woxga</code></dt>
<dd> 2560&#215;1600</dd>
<dt><code>wqsxga</code></dt>
<dd> 3200&#215;2048</dd>
<dt><code>wquxga</code></dt>
<dd> 3840&#215;2400</dd>
<dt><code>whsxga</code></dt>
<dd> 6400&#215;4096</dd>
<dt><code>whuxga</code></dt>
<dd> 7680&#215;4800</dd>
<dt><code>cga</code></dt>
<dd> 320&#215;200</dd>
<dt><code>ega</code></dt>
<dd> 640&#215;350</dd>
<dt><code>hd480</code></dt>
<dd> 852&#215;480</dd>
<dt><code>hd720</code></dt>
<dd> 1280&#215;720</dd>
<dt><code>hd1080</code></dt>
<dd> 1920&#215;1080</dd>
<dt><code>2k</code></dt>
<dd> 2048&#215;1080</dd>
<dt><code>2kflat</code></dt>
<dd> 1998&#215;1080</dd>
<dt><code>2kscope</code></dt>
<dd> 2048&#215;858</dd>
<dt><code>4k</code></dt>
<dd> 4096&#215;2160</dd>
<dt><code>4kflat</code></dt>
<dd> 3996&#215;2160</dd>
<dt><code>4kscope</code></dt>
<dd> 4096&#215;1716</dd>
<dt><code>nhd</code></dt>
<dd> 640&#215;360</dd>
<dt><code>hqvga</code></dt>
<dd> 240&#215;160</dd>
<dt><code>wqvga</code></dt>
<dd> 400&#215;240</dd>
<dt><code>fwqvga</code></dt>
<dd> 432&#215;240</dd>
<dt><code>hvga</code></dt>
<dd> 480&#215;320</dd>
<dt><code>qhd</code></dt>
<dd> 960&#215;540</dd>
<dt><code>2kdci</code></dt>
<dd> 2048&#215;1080</dd>
<dt><code>4kdci</code></dt>
<dd> 4096&#215;2160</dd>
<dt><code>uhd2160</code></dt>
<dd> 3840&#215;2160</dd>
<dt><code>uhd4320</code></dt>
<dd> 7680&#215;4320</dd></dl>
<h3>Video rate</h3>
<p> Specify the frame rate of a video, expressed as the number of frames generated per second. It has to be a string in the format <i>frame_rate_num</i>/<i>frame_rate_den</i>, an integer number, a float number or a valid video frame rate abbreviation. </p>
<p> The following abbreviations are recognized:</p>
<dl>
<dt><code>ntsc</code></dt>
<dd> 30000/1001</dd>
<dt><code>pal</code></dt>
<dd> 25/1</dd>
<dt><code>qntsc</code></dt>
<dd> 30000/1001</dd>
<dt><code>qpal</code></dt>
<dd> 25/1</dd>
<dt><code>sntsc</code></dt>
<dd> 30000/1001</dd>
<dt><code>spal</code></dt>
<dd> 25/1</dd>
<dt><code>film</code></dt>
<dd> 24/1</dd>
<dt><code>ntsc-film</code></dt>
<dd> 24000/1001</dd></dl>
<h3>Ratio</h3>
<p> A ratio can be expressed as an expression, or in the form <i>numerator</i>:<i>denominator</i>. </p>
<p> Note that a ratio with infinite (1/0) or negative value is considered valid, so you should check on the returned value if you want to exclude those values. </p>
<p> The undefined value can be expressed using the &#8220;0:0&#8221; string.</p>
<h3>Color</h3>
<p> It can be the name of a color as defined below (case insensitive match) or a <tt>&quot;[0x|#]RRGGBB[AA]&quot;</tt> sequence, possibly followed by @ and a string representing the alpha component. </p>
<p> The alpha component may be a string composed by &#8220;0x&#8221; followed by an hexadecimal number or a decimal number between 0.0 and 1.0, which represents the opacity value (<code>0x00</code> or <code>0.0</code> means completely transparent, <code>0xff</code> or <code>1.0</code> completely opaque). If the alpha component is not specified then <code>0xff</code> is assumed. </p>
<p> The string <code>random</code> will result in a random color. </p>
<p> The following names of colors are recognized:</p>
<dl>
<dt><code>AliceBlue</code></dt>
<dd> 0xF0F8FF</dd>
<dt><code>AntiqueWhite</code></dt>
<dd> 0xFAEBD7</dd>
<dt><code>Aqua</code></dt>
<dd> 0x00FFFF</dd>
<dt><code>Aquamarine</code></dt>
<dd> 0x7FFFD4</dd>
<dt><code>Azure</code></dt>
<dd> 0xF0FFFF</dd>
<dt><code>Beige</code></dt>
<dd> 0xF5F5DC</dd>
<dt><code>Bisque</code></dt>
<dd> 0xFFE4C4</dd>
<dt><code>Black</code></dt>
<dd> 0x000000</dd>
<dt><code>BlanchedAlmond</code></dt>
<dd> 0xFFEBCD</dd>
<dt><code>Blue</code></dt>
<dd> 0x0000FF</dd>
<dt><code>BlueViolet</code></dt>
<dd> 0x8A2BE2</dd>
<dt><code>Brown</code></dt>
<dd> 0xA52A2A</dd>
<dt><code>BurlyWood</code></dt>
<dd> 0xDEB887</dd>
<dt><code>CadetBlue</code></dt>
<dd> 0x5F9EA0</dd>
<dt><code>Chartreuse</code></dt>
<dd> 0x7FFF00</dd>
<dt><code>Chocolate</code></dt>
<dd> 0xD2691E</dd>
<dt><code>Coral</code></dt>
<dd> 0xFF7F50</dd>
<dt><code>CornflowerBlue</code></dt>
<dd> 0x6495ED</dd>
<dt><code>Cornsilk</code></dt>
<dd> 0xFFF8DC</dd>
<dt><code>Crimson</code></dt>
<dd> 0xDC143C</dd>
<dt><code>Cyan</code></dt>
<dd> 0x00FFFF</dd>
<dt><code>DarkBlue</code></dt>
<dd> 0x00008B</dd>
<dt><code>DarkCyan</code></dt>
<dd> 0x008B8B</dd>
<dt><code>DarkGoldenRod</code></dt>
<dd> 0xB8860B</dd>
<dt><code>DarkGray</code></dt>
<dd> 0xA9A9A9</dd>
<dt><code>DarkGreen</code></dt>
<dd> 0x006400</dd>
<dt><code>DarkKhaki</code></dt>
<dd> 0xBDB76B</dd>
<dt><code>DarkMagenta</code></dt>
<dd> 0x8B008B</dd>
<dt><code>DarkOliveGreen</code></dt>
<dd> 0x556B2F</dd>
<dt><code>Darkorange</code></dt>
<dd> 0xFF8C00</dd>
<dt><code>DarkOrchid</code></dt>
<dd> 0x9932CC</dd>
<dt><code>DarkRed</code></dt>
<dd> 0x8B0000</dd>
<dt><code>DarkSalmon</code></dt>
<dd> 0xE9967A</dd>
<dt><code>DarkSeaGreen</code></dt>
<dd> 0x8FBC8F</dd>
<dt><code>DarkSlateBlue</code></dt>
<dd> 0x483D8B</dd>
<dt><code>DarkSlateGray</code></dt>
<dd> 0x2F4F4F</dd>
<dt><code>DarkTurquoise</code></dt>
<dd> 0x00CED1</dd>
<dt><code>DarkViolet</code></dt>
<dd> 0x9400D3</dd>
<dt><code>DeepPink</code></dt>
<dd> 0xFF1493</dd>
<dt><code>DeepSkyBlue</code></dt>
<dd> 0x00BFFF</dd>
<dt><code>DimGray</code></dt>
<dd> 0x696969</dd>
<dt><code>DodgerBlue</code></dt>
<dd> 0x1E90FF</dd>
<dt><code>FireBrick</code></dt>
<dd> 0xB22222</dd>
<dt><code>FloralWhite</code></dt>
<dd> 0xFFFAF0</dd>
<dt><code>ForestGreen</code></dt>
<dd> 0x228B22</dd>
<dt><code>Fuchsia</code></dt>
<dd> 0xFF00FF</dd>
<dt><code>Gainsboro</code></dt>
<dd> 0xDCDCDC</dd>
<dt><code>GhostWhite</code></dt>
<dd> 0xF8F8FF</dd>
<dt><code>Gold</code></dt>
<dd> 0xFFD700</dd>
<dt><code>GoldenRod</code></dt>
<dd> 0xDAA520</dd>
<dt><code>Gray</code></dt>
<dd> 0x808080</dd>
<dt><code>Green</code></dt>
<dd> 0x008000</dd>
<dt><code>GreenYellow</code></dt>
<dd> 0xADFF2F</dd>
<dt><code>HoneyDew</code></dt>
<dd> 0xF0FFF0</dd>
<dt><code>HotPink</code></dt>
<dd> 0xFF69B4</dd>
<dt><code>IndianRed</code></dt>
<dd> 0xCD5C5C</dd>
<dt><code>Indigo</code></dt>
<dd> 0x4B0082</dd>
<dt><code>Ivory</code></dt>
<dd> 0xFFFFF0</dd>
<dt><code>Khaki</code></dt>
<dd> 0xF0E68C</dd>
<dt><code>Lavender</code></dt>
<dd> 0xE6E6FA</dd>
<dt><code>LavenderBlush</code></dt>
<dd> 0xFFF0F5</dd>
<dt><code>LawnGreen</code></dt>
<dd> 0x7CFC00</dd>
<dt><code>LemonChiffon</code></dt>
<dd> 0xFFFACD</dd>
<dt><code>LightBlue</code></dt>
<dd> 0xADD8E6</dd>
<dt><code>LightCoral</code></dt>
<dd> 0xF08080</dd>
<dt><code>LightCyan</code></dt>
<dd> 0xE0FFFF</dd>
<dt><code>LightGoldenRodYellow</code></dt>
<dd> 0xFAFAD2</dd>
<dt><code>LightGreen</code></dt>
<dd> 0x90EE90</dd>
<dt><code>LightGrey</code></dt>
<dd> 0xD3D3D3</dd>
<dt><code>LightPink</code></dt>
<dd> 0xFFB6C1</dd>
<dt><code>LightSalmon</code></dt>
<dd> 0xFFA07A</dd>
<dt><code>LightSeaGreen</code></dt>
<dd> 0x20B2AA</dd>
<dt><code>LightSkyBlue</code></dt>
<dd> 0x87CEFA</dd>
<dt><code>LightSlateGray</code></dt>
<dd> 0x778899</dd>
<dt><code>LightSteelBlue</code></dt>
<dd> 0xB0C4DE</dd>
<dt><code>LightYellow</code></dt>
<dd> 0xFFFFE0</dd>
<dt><code>Lime</code></dt>
<dd> 0x00FF00</dd>
<dt><code>LimeGreen</code></dt>
<dd> 0x32CD32</dd>
<dt><code>Linen</code></dt>
<dd> 0xFAF0E6</dd>
<dt><code>Magenta</code></dt>
<dd> 0xFF00FF</dd>
<dt><code>Maroon</code></dt>
<dd> 0x800000</dd>
<dt><code>MediumAquaMarine</code></dt>
<dd> 0x66CDAA</dd>
<dt><code>MediumBlue</code></dt>
<dd> 0x0000CD</dd>
<dt><code>MediumOrchid</code></dt>
<dd> 0xBA55D3</dd>
<dt><code>MediumPurple</code></dt>
<dd> 0x9370D8</dd>
<dt><code>MediumSeaGreen</code></dt>
<dd> 0x3CB371</dd>
<dt><code>MediumSlateBlue</code></dt>
<dd> 0x7B68EE</dd>
<dt><code>MediumSpringGreen</code></dt>
<dd> 0x00FA9A</dd>
<dt><code>MediumTurquoise</code></dt>
<dd> 0x48D1CC</dd>
<dt><code>MediumVioletRed</code></dt>
<dd> 0xC71585</dd>
<dt><code>MidnightBlue</code></dt>
<dd> 0x191970</dd>
<dt><code>MintCream</code></dt>
<dd> 0xF5FFFA</dd>
<dt><code>MistyRose</code></dt>
<dd> 0xFFE4E1</dd>
<dt><code>Moccasin</code></dt>
<dd> 0xFFE4B5</dd>
<dt><code>NavajoWhite</code></dt>
<dd> 0xFFDEAD</dd>
<dt><code>Navy</code></dt>
<dd> 0x000080</dd>
<dt><code>OldLace</code></dt>
<dd> 0xFDF5E6</dd>
<dt><code>Olive</code></dt>
<dd> 0x808000</dd>
<dt><code>OliveDrab</code></dt>
<dd> 0x6B8E23</dd>
<dt><code>Orange</code></dt>
<dd> 0xFFA500</dd>
<dt><code>OrangeRed</code></dt>
<dd> 0xFF4500</dd>
<dt><code>Orchid</code></dt>
<dd> 0xDA70D6</dd>
<dt><code>PaleGoldenRod</code></dt>
<dd> 0xEEE8AA</dd>
<dt><code>PaleGreen</code></dt>
<dd> 0x98FB98</dd>
<dt><code>PaleTurquoise</code></dt>
<dd> 0xAFEEEE</dd>
<dt><code>PaleVioletRed</code></dt>
<dd> 0xD87093</dd>
<dt><code>PapayaWhip</code></dt>
<dd> 0xFFEFD5</dd>
<dt><code>PeachPuff</code></dt>
<dd> 0xFFDAB9</dd>
<dt><code>Peru</code></dt>
<dd> 0xCD853F</dd>
<dt><code>Pink</code></dt>
<dd> 0xFFC0CB</dd>
<dt><code>Plum</code></dt>
<dd> 0xDDA0DD</dd>
<dt><code>PowderBlue</code></dt>
<dd> 0xB0E0E6</dd>
<dt><code>Purple</code></dt>
<dd> 0x800080</dd>
<dt><code>Red</code></dt>
<dd> 0xFF0000</dd>
<dt><code>RosyBrown</code></dt>
<dd> 0xBC8F8F</dd>
<dt><code>RoyalBlue</code></dt>
<dd> 0x4169E1</dd>
<dt><code>SaddleBrown</code></dt>
<dd> 0x8B4513</dd>
<dt><code>Salmon</code></dt>
<dd> 0xFA8072</dd>
<dt><code>SandyBrown</code></dt>
<dd> 0xF4A460</dd>
<dt><code>SeaGreen</code></dt>
<dd> 0x2E8B57</dd>
<dt><code>SeaShell</code></dt>
<dd> 0xFFF5EE</dd>
<dt><code>Sienna</code></dt>
<dd> 0xA0522D</dd>
<dt><code>Silver</code></dt>
<dd> 0xC0C0C0</dd>
<dt><code>SkyBlue</code></dt>
<dd> 0x87CEEB</dd>
<dt><code>SlateBlue</code></dt>
<dd> 0x6A5ACD</dd>
<dt><code>SlateGray</code></dt>
<dd> 0x708090</dd>
<dt><code>Snow</code></dt>
<dd> 0xFFFAFA</dd>
<dt><code>SpringGreen</code></dt>
<dd> 0x00FF7F</dd>
<dt><code>SteelBlue</code></dt>
<dd> 0x4682B4</dd>
<dt><code>Tan</code></dt>
<dd> 0xD2B48C</dd>
<dt><code>Teal</code></dt>
<dd> 0x008080</dd>
<dt><code>Thistle</code></dt>
<dd> 0xD8BFD8</dd>
<dt><code>Tomato</code></dt>
<dd> 0xFF6347</dd>
<dt><code>Turquoise</code></dt>
<dd> 0x40E0D0</dd>
<dt><code>Violet</code></dt>
<dd> 0xEE82EE</dd>
<dt><code>Wheat</code></dt>
<dd> 0xF5DEB3</dd>
<dt><code>White</code></dt>
<dd> 0xFFFFFF</dd>
<dt><code>WhiteSmoke</code></dt>
<dd> 0xF5F5F5</dd>
<dt><code>Yellow</code></dt>
<dd> 0xFFFF00</dd>
<dt><code>YellowGreen</code></dt>
<dd> 0x9ACD32</dd></dl>
<h3>Channel Layout</h3>
<p> A channel layout specifies the spatial disposition of the channels in a multi-channel audio stream. To specify a channel layout, FFmpeg makes use of a special syntax. </p>
<p> Individual channels are identified by an id, as given by the table below:</p>
<dl>
<dt><font SIZE="-1"><code>FL</code></font></dt>
<dd> front left</dd>
<dt><font SIZE="-1"><code>FR</code></font></dt>
<dd> front right</dd>
<dt><font SIZE="-1"><code>FC</code></font></dt>
<dd> front center</dd>
<dt><font SIZE="-1"><code>LFE</code></font></dt>
<dd> low frequency</dd>
<dt><font SIZE="-1"><code>BL</code></font></dt>
<dd> back left</dd>
<dt><font SIZE="-1"><code>BR</code></font></dt>
<dd> back right</dd>
<dt><font SIZE="-1"><code>FLC</code></font></dt>
<dd> front left-of-center</dd>
<dt><font SIZE="-1"><code>FRC</code></font></dt>
<dd> front right-of-center</dd>
<dt><font SIZE="-1"><code>BC</code></font></dt>
<dd> back center</dd>
<dt><font SIZE="-1"><code>SL</code></font></dt>
<dd> side left</dd>
<dt><font SIZE="-1"><code>SR</code></font></dt>
<dd> side right</dd>
<dt><font SIZE="-1"><code>TC</code></font></dt>
<dd> top center</dd>
<dt><font SIZE="-1"><code>TFL</code></font></dt>
<dd> top front left</dd>
<dt><font SIZE="-1"><code>TFC</code></font></dt>
<dd> top front center</dd>
<dt><font SIZE="-1"><code>TFR</code></font></dt>
<dd> top front right</dd>
<dt><font SIZE="-1"><code>TBL</code></font></dt>
<dd> top back left</dd>
<dt><font SIZE="-1"><code>TBC</code></font></dt>
<dd> top back center</dd>
<dt><font SIZE="-1"><code>TBR</code></font></dt>
<dd> top back right</dd>
<dt><font SIZE="-1"><code>DL</code></font></dt>
<dd> downmix left</dd>
<dt><font SIZE="-1"><code>DR</code></font></dt>
<dd> downmix right</dd>
<dt><font SIZE="-1"><code>WL</code></font></dt>
<dd> wide left</dd>
<dt><font SIZE="-1"><code>WR</code></font></dt>
<dd> wide right</dd>
<dt><font SIZE="-1"><code>SDL</code></font></dt>
<dd> surround direct left</dd>
<dt><font SIZE="-1"><code>SDR</code></font></dt>
<dd> surround direct right</dd>
<dt><font SIZE="-1"><code>LFE2</code></font></dt>
<dd> low frequency 2</dd></dl>
<p> Standard channel layout compositions can be specified by using the following identifiers:</p>
<dl>
<dt><code>mono</code></dt>
<dd> <font SIZE="-1">FC</font></dd>
<dt><code>stereo</code></dt>
<dd> <font SIZE="-1">FL+FR</font></dd>
<dt><code>2.1</code></dt>
<dd> <font SIZE="-1">FL+FR+LFE</font></dd>
<dt><code>3.0</code></dt>
<dd> <font SIZE="-1">FL+FR+FC</font></dd>
<dt><code>3.0(back)</code></dt>
<dd> <font SIZE="-1">FL+FR+BC</font></dd>
<dt><code>4.0</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+BC</font></dd>
<dt><code>quad</code></dt>
<dd> <font SIZE="-1">FL+FR+BL+BR</font></dd>
<dt><code>quad(side)</code></dt>
<dd> <font SIZE="-1">FL+FR+SL+SR</font></dd>
<dt><code>3.1</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+LFE</font></dd>
<dt><code>5.0</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+BL+BR</font></dd>
<dt><code>5.0(side)</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+SL+SR</font></dd>
<dt><code>4.1</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+LFE+BC</font></dd>
<dt><code>5.1</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+LFE+BL+BR</font></dd>
<dt><code>5.1(side)</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+LFE+SL+SR</font></dd>
<dt><code>6.0</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+BC+SL+SR</font></dd>
<dt><code>6.0(front)</code></dt>
<dd> <font SIZE="-1">FL+FR+FLC+FRC+SL+SR</font></dd>
<dt><code>hexagonal</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+BL+BR+BC</font></dd>
<dt><code>6.1</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+LFE+BC+SL+SR</font></dd>
<dt><code>6.1</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+LFE+BL+BR+BC</font></dd>
<dt><code>6.1(front)</code></dt>
<dd> <font SIZE="-1">FL+FR+LFE+FLC+FRC+SL+SR</font></dd>
<dt><code>7.0</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+BL+BR+SL+SR</font></dd>
<dt><code>7.0(front)</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+FLC+FRC+SL+SR</font></dd>
<dt><code>7.1</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+LFE+BL+BR+SL+SR</font></dd>
<dt><code>7.1(wide)</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+LFE+BL+BR+FLC+FRC</font></dd>
<dt><code>7.1(wide-side)</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+LFE+FLC+FRC+SL+SR</font></dd>
<dt><code>octagonal</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+BL+BR+BC+SL+SR</font></dd>
<dt><code>hexadecagonal</code></dt>
<dd> <font SIZE="-1">FL+FR+FC+BL+BR+BC+SL+SR+WL+WR+TBL+TBR+TBC+TFC+TFL+TFR</font></dd>
<dt><code>downmix</code></dt>
<dd> <font SIZE="-1">DL+DR</font></dd></dl>
<p> A custom channel layout can be specified as a sequence of terms, separated by &#8216;+&#8217; or &#8216;|&#8217;. Each term can be:</p>
<dl>
<dt>&bull;</dt>
<dd> the name of a standard channel layout (e.g. <code>mono</code>, <code>stereo</code>, <code>4.0</code>, <code>quad</code>, <code>5.0</code>, etc.)</dd>
<dt>&bull;</dt>
<dd> the name of a single channel (e.g. <font SIZE="-1"><code>FL</code></font>, <font SIZE="-1"><code>FR</code></font>, <font SIZE="-1"><code>FC</code></font>, <font SIZE="-1"><code>LFE</code></font>, etc.)</dd>
<dt>&bull;</dt>
<dd> a number of channels, in decimal, followed by &#8216;c&#8217;, yielding the default channel layout for that number of channels (see the function <tt>&quot;av_get_default_channel_layout&quot;</tt>). Note that not all channel counts have a default layout.</dd>
<dt>&bull;</dt>
<dd> a number of channels, in decimal, followed by &#8216;C&#8217;, yielding an unknown channel layout with the specified number of channels. Note that not all channel layout specification strings support unknown channel layouts.</dd>
<dt>&bull;</dt>
<dd> a channel layout mask, in hexadecimal starting with &#8220;0x&#8221; (see the <tt>&quot;AV_CH_*&quot;</tt> macros in <i>libavutil/channel_layout.h</i>.</dd></dl>
<p> Before libavutil version 53 the trailing character &#8220;c&#8221; to specify a number of channels was optional, but now it is required, while a channel layout mask can also be specified as a decimal number (if and only if not followed by &#8220;c&#8221; or &#8220;C&#8221;). </p>
<p> See also the function <tt>&quot;av_get_channel_layout&quot;</tt> defined in <i>libavutil/channel_layout.h</i>.</p>
<h2>EXPRESSION EVALUATION</h2>
<p> When evaluating an arithmetic expression, FFmpeg uses an internal formula evaluator, implemented through the <i>libavutil/eval.h</i> interface. </p>
<p> An expression may contain unary, binary operators, constants, and functions. </p>
<p> Two expressions <i>expr1</i> and <i>expr2</i> can be combined to form another expression &quot;<i>expr1</i>;<i>expr2</i>&quot;. <i>expr1</i> and <i>expr2</i> are evaluated in turn, and the new expression evaluates to the value of <i>expr2</i>. </p>
<p> The following binary operators are available: <tt>&quot;+&quot;</tt>, <tt>&quot;-&quot;</tt>, <tt>&quot;*&quot;</tt>, <tt>&quot;/&quot;</tt>, <tt>&quot;^&quot;</tt>. </p>
<p> The following unary operators are available: <tt>&quot;+&quot;</tt>, <tt>&quot;-&quot;</tt>. </p>
<p> The following functions are available:</p>
<dl>
<dt><code>abs(x)</code></dt>
<dd> Compute absolute value of <i>x</i>.</dd>
<dt><code>acos(x)</code></dt>
<dd> Compute arccosine of <i>x</i>.</dd>
<dt><code>asin(x)</code></dt>
<dd> Compute arcsine of <i>x</i>.</dd>
<dt><code>atan(x)</code></dt>
<dd> Compute arctangent of <i>x</i>.</dd>
<dt><code>atan2(x, y)</code></dt>
<dd> Compute principal value of the arc tangent of <i>y</i>/<i>x</i>.</dd>
<dt><code>between(x, min, max)</code></dt>
<dd> Return 1 if <i>x</i> is greater than or equal to <i>min</i> and lesser than or equal to <i>max</i>, 0 otherwise.</dd>
<dt><code>bitand(x, y)</code></dt>
<dd>
</dd><dt><code>bitor(x, y)</code></dt>
<dd> Compute bitwise and/or operation on <i>x</i> and <i>y</i>. </dd>
<p> The results of the evaluation of <i>x</i> and <i>y</i> are converted to integers before executing the bitwise operation. </p>
<p> Note that both the conversion to integer and the conversion back to floating point can lose precision. Beware of unexpected results for large numbers (usually 2^53 and larger).</p>
<dt><code>ceil(expr)</code></dt>
<dd> Round the value of expression <i>expr</i> upwards to the nearest integer. For example, &#8220;ceil(1.5)&#8221; is &#8220;2.0&#8221;.</dd>
<dt><code>clip(x, min, max)</code></dt>
<dd> Return the value of <i>x</i> clipped between <i>min</i> and <i>max</i>.</dd>
<dt><code>cos(x)</code></dt>
<dd> Compute cosine of <i>x</i>.</dd>
<dt><code>cosh(x)</code></dt>
<dd> Compute hyperbolic cosine of <i>x</i>.</dd>
<dt><code>eq(x, y)</code></dt>
<dd> Return 1 if <i>x</i> and <i>y</i> are equivalent, 0 otherwise.</dd>
<dt><code>exp(x)</code></dt>
<dd> Compute exponential of <i>x</i> (with base <tt>&quot;e&quot;</tt>, the Euler&#8217;s number).</dd>
<dt><code>floor(expr)</code></dt>
<dd> Round the value of expression <i>expr</i> downwards to the nearest integer. For example, &#8220;floor(-1.5)&#8221; is &#8220;-2.0&#8221;.</dd>
<dt><code>gauss(x)</code></dt>
<dd> Compute Gauss function of <i>x</i>, corresponding to <tt>&quot;exp(-x*x/2) / sqrt(2*PI)&quot;</tt>.</dd>
<dt><code>gcd(x, y)</code></dt>
<dd> Return the greatest common divisor of <i>x</i> and <i>y</i>. If both <i>x</i> and <i>y</i> are 0 or either or both are less than zero then behavior is undefined.</dd>
<dt><code>gt(x, y)</code></dt>
<dd> Return 1 if <i>x</i> is greater than <i>y</i>, 0 otherwise.</dd>
<dt><code>gte(x, y)</code></dt>
<dd> Return 1 if <i>x</i> is greater than or equal to <i>y</i>, 0 otherwise.</dd>
<dt><code>hypot(x, y)</code></dt>
<dd> This function is similar to the C function with the same name; it returns &quot;sqrt(<i>x</i>*<i>x</i> + <i>y</i>*<i>y</i>)&quot;, the length of the hypotenuse of a right triangle with sides of length <i>x</i> and <i>y</i>, or the distance of the point (<i>x</i>, <i>y</i>) from the origin.</dd>
<dt><code>if(x, y)</code></dt>
<dd> Evaluate <i>x</i>, and if the result is non-zero return the result of the evaluation of <i>y</i>, return 0 otherwise.</dd>
<dt><code>if(x, y, z)</code></dt>
<dd> Evaluate <i>x</i>, and if the result is non-zero return the evaluation result of <i>y</i>, otherwise the evaluation result of <i>z</i>.</dd>
<dt><code>ifnot(x, y)</code></dt>
<dd> Evaluate <i>x</i>, and if the result is zero return the result of the evaluation of <i>y</i>, return 0 otherwise.</dd>
<dt><code>ifnot(x, y, z)</code></dt>
<dd> Evaluate <i>x</i>, and if the result is zero return the evaluation result of <i>y</i>, otherwise the evaluation result of <i>z</i>.</dd>
<dt><code>isinf(x)</code></dt>
<dd> Return 1.0 if <i>x</i> is +/-INFINITY, 0.0 otherwise.</dd>
<dt><code>isnan(x)</code></dt>
<dd> Return 1.0 if <i>x</i> is <font SIZE="-1">NAN, 0.0</font> otherwise.</dd>
<dt><code>ld(var)</code></dt>
<dd> Load the value of the internal variable with number <i>var</i>, which was previously stored with st(<i>var</i>, <i>expr</i>). The function returns the loaded value.</dd>
<dt><code>lerp(x, y, z)</code></dt>
<dd> Return linear interpolation between <i>x</i> and <i>y</i> by amount of <i>z</i>.</dd>
<dt><code>log(x)</code></dt>
<dd> Compute natural logarithm of <i>x</i>.</dd>
<dt><code>lt(x, y)</code></dt>
<dd> Return 1 if <i>x</i> is lesser than <i>y</i>, 0 otherwise.</dd>
<dt><code>lte(x, y)</code></dt>
<dd> Return 1 if <i>x</i> is lesser than or equal to <i>y</i>, 0 otherwise.</dd>
<dt><code>max(x, y)</code></dt>
<dd> Return the maximum between <i>x</i> and <i>y</i>.</dd>
<dt><code>min(x, y)</code></dt>
<dd> Return the minimum between <i>x</i> and <i>y</i>.</dd>
<dt><code>mod(x, y)</code></dt>
<dd> Compute the remainder of division of <i>x</i> by <i>y</i>.</dd>
<dt><code>not(expr)</code></dt>
<dd> Return 1.0 if <i>expr</i> is zero, 0.0 otherwise.</dd>
<dt><code>pow(x, y)</code></dt>
<dd> Compute the power of <i>x</i> elevated <i>y</i>, it is equivalent to &quot;(<i>x</i>)^(<i>y</i>)&quot;.</dd>
<dt><code>print(t)</code></dt>
<dd>
</dd><dt><code>print(t, l)</code></dt>
<dd> Print the value of expression <i>t</i> with loglevel <i>l</i>. If <i>l</i> is not specified then a default log level is used. Returns the value of the expression printed. </dd>
<p> Prints t with loglevel l</p>
<dt><code>random(x)</code></dt>
<dd> Return a pseudo random value between 0.0 and 1.0. <i>x</i> is the index of the internal variable which will be used to save the seed/state.</dd>
<dt><code>root(expr, max)</code></dt>
<dd> Find an input value for which the function represented by <i>expr</i> with argument <i></i>ld<i>(0)</i> is 0 in the interval 0..<i>max</i>. </dd>
<p> The expression in <i>expr</i> must denote a continuous function or the result is undefined. </p>
<p> <i></i>ld<i>(0)</i> is used to represent the function input value, which means that the given expression will be evaluated multiple times with various input values that the expression can access through <tt>ld(0)</tt>. When the expression evaluates to 0 then the corresponding input value will be returned.</p>
<dt><code>round(expr)</code></dt>
<dd> Round the value of expression <i>expr</i> to the nearest integer. For example, &#8220;round(1.5)&#8221; is &#8220;2.0&#8221;.</dd>
<dt><code>sgn(x)</code></dt>
<dd> Compute sign of <i>x</i>.</dd>
<dt><code>sin(x)</code></dt>
<dd> Compute sine of <i>x</i>.</dd>
<dt><code>sinh(x)</code></dt>
<dd> Compute hyperbolic sine of <i>x</i>.</dd>
<dt><code>sqrt(expr)</code></dt>
<dd> Compute the square root of <i>expr</i>. This is equivalent to &quot;(<i>expr</i>)^.5&quot;.</dd>
<dt><code>squish(x)</code></dt>
<dd> Compute expression <tt>&quot;1/(1 + exp(4*x))&quot;</tt>.</dd>
<dt><code>st(var, expr)</code></dt>
<dd> Store the value of the expression <i>expr</i> in an internal variable. <i>var</i> specifies the number of the variable where to store the value, and it is a value ranging from 0 to 9. The function returns the value stored in the internal variable. Note, Variables are currently not shared between expressions.</dd>
<dt><code>tan(x)</code></dt>
<dd> Compute tangent of <i>x</i>.</dd>
<dt><code>tanh(x)</code></dt>
<dd> Compute hyperbolic tangent of <i>x</i>.</dd>
<dt><code>taylor(expr, x)</code></dt>
<dd>
</dd><dt><code>taylor(expr, x, id)</code></dt>
<dd> Evaluate a Taylor series at <i>x</i>, given an expression representing the <tt>&quot;ld(id)&quot;</tt>-th derivative of a function at 0. </dd>
<p> When the series does not converge the result is undefined. </p>
<p> <i>ld(id)</i> is used to represent the derivative order in <i>expr</i>, which means that the given expression will be evaluated multiple times with various input values that the expression can access through <tt>&quot;ld(id)&quot;</tt>. If <i>id</i> is not specified then 0 is assumed. </p>
<p> Note, when you have the derivatives at y instead of 0, <tt>&quot;taylor(expr, x-y)&quot;</tt> can be used.</p>
<dt><code>time(0)</code></dt>
<dd> Return the current (wallclock) time in seconds.</dd>
<dt><code>trunc(expr)</code></dt>
<dd> Round the value of expression <i>expr</i> towards zero to the nearest integer. For example, &#8220;trunc(-1.5)&#8221; is &#8220;-1.0&#8221;.</dd>
<dt><code>while(cond, expr)</code></dt>
<dd> Evaluate expression <i>expr</i> while the expression <i>cond</i> is non-zero, and returns the value of the last <i>expr</i> evaluation, or <font SIZE="-1">NAN</font> if <i>cond</i> was always false.</dd></dl>
<p> The following constants are available:</p>
<dl>
<dt><font SIZE="-1"><code>PI</code></font></dt>
<dd> area of the unit disc, approximately 3.14</dd>
<dt><code>E</code></dt>
<dd> <code>exp</code>(1) (Euler&#8217;s number), approximately 2.718</dd>
<dt><font SIZE="-1"><code>PHI</code></font></dt>
<dd> golden ratio (1+<code>sqrt</code>(5))/2, approximately 1.618</dd></dl>
<p> Assuming that an expression is considered &#8220;true&#8221; if it has a non-zero value, note that: </p>
<p> <tt>&quot;*&quot;</tt> works like <font SIZE="-1">AND</font> </p>
<p> <tt>&quot;+&quot;</tt> works like <font SIZE="-1">OR</font> </p>
<p> For example the construct: </p>
<pre>
        if (A AND B) then C
</pre>
<p> is equivalent to: </p>
<pre>
        if(A*B, C)
</pre>
<p> In your C code, you can extend the list of unary and binary functions, and define recognized constants, so that they are available for your expressions. </p>
<p> The evaluator also recognizes the International System unit prefixes. If &#8216;i&#8217; is appended after the prefix, binary prefixes are used, which are based on powers of 1024 instead of powers of 1000. The &#8216;B&#8217; postfix multiplies the value by 8, and can be appended after a unit prefix or used alone. This allows using for example &#8216;<font SIZE="-1">KB</font>&#8216;, &#8216;MiB&#8217;, &#8216;G&#8217; and &#8216;B&#8217; as number postfix. </p>
<p> The list of available International System prefixes follows, with indication of the corresponding powers of 10 and of 2.</p>
<dl>
<dt><code>y</code></dt>
<dd> 10^-24 / 2^-80</dd>
<dt><code>z</code></dt>
<dd> 10^-21 / 2^-70</dd>
<dt><code>a</code></dt>
<dd> 10^-18 / 2^-60</dd>
<dt><code>f</code></dt>
<dd> 10^-15 / 2^-50</dd>
<dt><code>p</code></dt>
<dd> 10^-12 / 2^-40</dd>
<dt><code>n</code></dt>
<dd> 10^-9 / 2^-30</dd>
<dt><code>u</code></dt>
<dd> 10^-6 / 2^-20</dd>
<dt><code>m</code></dt>
<dd> 10^-3 / 2^-10</dd>
<dt><code>c</code></dt>
<dd> 10^-2</dd>
<dt><code>d</code></dt>
<dd> 10^-1</dd>
<dt><code>h</code></dt>
<dd> 10^2</dd>
<dt><code>k</code></dt>
<dd> 10^3 / 2^10</dd>
<dt><code>K</code></dt>
<dd> 10^3 / 2^10</dd>
<dt><code>M</code></dt>
<dd> 10^6 / 2^20</dd>
<dt><code>G</code></dt>
<dd> 10^9 / 2^30</dd>
<dt><code>T</code></dt>
<dd> 10^12 / 2^40</dd>
<dt><code>P</code></dt>
<dd> 10^15 / 2^40</dd>
<dt><code>E</code></dt>
<dd> 10^18 / 2^50</dd>
<dt><code>Z</code></dt>
<dd> 10^21 / 2^60</dd>
<dt><code>Y</code></dt>
<dd> 10^24 / 2^70</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></code>(1), <code><a href="/docs/linux/man/1-ffplay/">ffplay</a></code>(1), <code><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></code>(1), <code><a href="/docs/linux/man/3-libavutil/">libavutil</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
<h2>Index</h2>
