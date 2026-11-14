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
<dt>&bull;</p>
<dd> <code>&#8216;</code> and <code>\</code> are special characters (respectively used for quoting and escaping). In addition to them, there might be other special characters depending on the specific syntax where the escaping and quoting are employed.</p>
<dt>&bull;</p>
<dd> A special character is escaped by prefixing it with a <code>\</code>.</p>
<dt>&bull;</p>
<dd> All characters enclosed between <code>&#8221;</code> are included literally in the parsed string. The quote character <code>&#8216;</code> itself cannot be quoted, so you may need to close the quote and escape it.</p>
<dt>&bull;</p>
<dd> Leading and trailing whitespaces, unless escaped or quoted, are removed from the parsed string.</dl>
<p> Note that you may need to add a second level of escaping when using the command line or a script, which depends on the syntax of the adopted shell language. </p>
<p> The function <tt>&quot;av_get_token&quot;</tt> defined in <i>libavutil/avstring.h</i> can be used to parse a token quoted or escaped according to the rules defined above. </p>
<p> The tool <i>tools/ffescape</i> in the FFmpeg source tree can be used to automatically quote or escape a string in a script. </p>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Escape the string <tt>&quot;Crime d'Amour&quot;</tt> containing the <tt>&quot;'&quot;</tt> special character: </p>
<pre>
        Crime d\'Amour
</pre>
<dt>&bull;</p>
<dd> The string above contains a quote, so the <tt>&quot;'&quot;</tt> needs to be escaped when quoting it: </p>
<pre>
        'Crime d'\''Amour'
</pre>
<dt>&bull;</p>
<dd> Include leading or trailing whitespaces using quoting: </p>
<pre>
        '  this string starts and ends with whitespaces  '
</pre>
<dt>&bull;</p>
<dd> Escaping and quoting can be mixed together: </p>
<pre>
        ' The string '\'string\'' is a string '
</pre>
<dt>&bull;</p>
<dd> To include a literal <code>\</code> you can use either escaping or quoting: </p>
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
<dt><code>55</code></p>
<dd> 55 seconds</p>
<dt><code>0.2</code></p>
<dd> 0.2 seconds</p>
<dt><code>200ms</code></p>
<dd> 200 milliseconds, that&#8217;s 0.2s</p>
<dt><code>200000us</code></p>
<dd> 200000 microseconds, that&#8217;s 0.2s</p>
<dt><code>12:03:45</code></p>
<dd> 12 hours, 03 minutes and 45 seconds</p>
<dt><code>23.189</code></p>
<dd> 23.189 seconds</dl>
<h3>Video size</h3>
<p> Specify the size of the sourced video, it may be a string of the form <i>width</i>x<i>height</i>, or the name of a size abbreviation. </p>
<p> The following abbreviations are recognized:</p>
<dl>
<dt><code>ntsc</code></p>
<dd> 720&#215;480</p>
<dt><code>pal</code></p>
<dd> 720&#215;576</p>
<dt><code>qntsc</code></p>
<dd> 352&#215;240</p>
<dt><code>qpal</code></p>
<dd> 352&#215;288</p>
<dt><code>sntsc</code></p>
<dd> 640&#215;480</p>
<dt><code>spal</code></p>
<dd> 768&#215;576</p>
<dt><code>film</code></p>
<dd> 352&#215;240</p>
<dt><code>ntsc-film</code></p>
<dd> 352&#215;240</p>
<dt><code>sqcif</code></p>
<dd> 128&#215;96</p>
<dt><code>qcif</code></p>
<dd> 176&#215;144</p>
<dt><code>cif</code></p>
<dd> 352&#215;288</p>
<dt><code>4cif</code></p>
<dd> 704&#215;576</p>
<dt><code>16cif</code></p>
<dd> 1408&#215;1152</p>
<dt><code>qqvga</code></p>
<dd> 160&#215;120</p>
<dt><code>qvga</code></p>
<dd> 320&#215;240</p>
<dt><code>vga</code></p>
<dd> 640&#215;480</p>
<dt><code>svga</code></p>
<dd> 800&#215;600</p>
<dt><code>xga</code></p>
<dd> 1024&#215;768</p>
<dt><code>uxga</code></p>
<dd> 1600&#215;1200</p>
<dt><code>qxga</code></p>
<dd> 2048&#215;1536</p>
<dt><code>sxga</code></p>
<dd> 1280&#215;1024</p>
<dt><code>qsxga</code></p>
<dd> 2560&#215;2048</p>
<dt><code>hsxga</code></p>
<dd> 5120&#215;4096</p>
<dt><code>wvga</code></p>
<dd> 852&#215;480</p>
<dt><code>wxga</code></p>
<dd> 1366&#215;768</p>
<dt><code>wsxga</code></p>
<dd> 1600&#215;1024</p>
<dt><code>wuxga</code></p>
<dd> 1920&#215;1200</p>
<dt><code>woxga</code></p>
<dd> 2560&#215;1600</p>
<dt><code>wqsxga</code></p>
<dd> 3200&#215;2048</p>
<dt><code>wquxga</code></p>
<dd> 3840&#215;2400</p>
<dt><code>whsxga</code></p>
<dd> 6400&#215;4096</p>
<dt><code>whuxga</code></p>
<dd> 7680&#215;4800</p>
<dt><code>cga</code></p>
<dd> 320&#215;200</p>
<dt><code>ega</code></p>
<dd> 640&#215;350</p>
<dt><code>hd480</code></p>
<dd> 852&#215;480</p>
<dt><code>hd720</code></p>
<dd> 1280&#215;720</p>
<dt><code>hd1080</code></p>
<dd> 1920&#215;1080</p>
<dt><code>2k</code></p>
<dd> 2048&#215;1080</p>
<dt><code>2kflat</code></p>
<dd> 1998&#215;1080</p>
<dt><code>2kscope</code></p>
<dd> 2048&#215;858</p>
<dt><code>4k</code></p>
<dd> 4096&#215;2160</p>
<dt><code>4kflat</code></p>
<dd> 3996&#215;2160</p>
<dt><code>4kscope</code></p>
<dd> 4096&#215;1716</p>
<dt><code>nhd</code></p>
<dd> 640&#215;360</p>
<dt><code>hqvga</code></p>
<dd> 240&#215;160</p>
<dt><code>wqvga</code></p>
<dd> 400&#215;240</p>
<dt><code>fwqvga</code></p>
<dd> 432&#215;240</p>
<dt><code>hvga</code></p>
<dd> 480&#215;320</p>
<dt><code>qhd</code></p>
<dd> 960&#215;540</p>
<dt><code>2kdci</code></p>
<dd> 2048&#215;1080</p>
<dt><code>4kdci</code></p>
<dd> 4096&#215;2160</p>
<dt><code>uhd2160</code></p>
<dd> 3840&#215;2160</p>
<dt><code>uhd4320</code></p>
<dd> 7680&#215;4320</dl>
<h3>Video rate</h3>
<p> Specify the frame rate of a video, expressed as the number of frames generated per second. It has to be a string in the format <i>frame_rate_num</i>/<i>frame_rate_den</i>, an integer number, a float number or a valid video frame rate abbreviation. </p>
<p> The following abbreviations are recognized:</p>
<dl>
<dt><code>ntsc</code></p>
<dd> 30000/1001</p>
<dt><code>pal</code></p>
<dd> 25/1</p>
<dt><code>qntsc</code></p>
<dd> 30000/1001</p>
<dt><code>qpal</code></p>
<dd> 25/1</p>
<dt><code>sntsc</code></p>
<dd> 30000/1001</p>
<dt><code>spal</code></p>
<dd> 25/1</p>
<dt><code>film</code></p>
<dd> 24/1</p>
<dt><code>ntsc-film</code></p>
<dd> 24000/1001</dl>
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
<dt><code>AliceBlue</code></p>
<dd> 0xF0F8FF</p>
<dt><code>AntiqueWhite</code></p>
<dd> 0xFAEBD7</p>
<dt><code>Aqua</code></p>
<dd> 0x00FFFF</p>
<dt><code>Aquamarine</code></p>
<dd> 0x7FFFD4</p>
<dt><code>Azure</code></p>
<dd> 0xF0FFFF</p>
<dt><code>Beige</code></p>
<dd> 0xF5F5DC</p>
<dt><code>Bisque</code></p>
<dd> 0xFFE4C4</p>
<dt><code>Black</code></p>
<dd> 0x000000</p>
<dt><code>BlanchedAlmond</code></p>
<dd> 0xFFEBCD</p>
<dt><code>Blue</code></p>
<dd> 0x0000FF</p>
<dt><code>BlueViolet</code></p>
<dd> 0x8A2BE2</p>
<dt><code>Brown</code></p>
<dd> 0xA52A2A</p>
<dt><code>BurlyWood</code></p>
<dd> 0xDEB887</p>
<dt><code>CadetBlue</code></p>
<dd> 0x5F9EA0</p>
<dt><code>Chartreuse</code></p>
<dd> 0x7FFF00</p>
<dt><code>Chocolate</code></p>
<dd> 0xD2691E</p>
<dt><code>Coral</code></p>
<dd> 0xFF7F50</p>
<dt><code>CornflowerBlue</code></p>
<dd> 0x6495ED</p>
<dt><code>Cornsilk</code></p>
<dd> 0xFFF8DC</p>
<dt><code>Crimson</code></p>
<dd> 0xDC143C</p>
<dt><code>Cyan</code></p>
<dd> 0x00FFFF</p>
<dt><code>DarkBlue</code></p>
<dd> 0x00008B</p>
<dt><code>DarkCyan</code></p>
<dd> 0x008B8B</p>
<dt><code>DarkGoldenRod</code></p>
<dd> 0xB8860B</p>
<dt><code>DarkGray</code></p>
<dd> 0xA9A9A9</p>
<dt><code>DarkGreen</code></p>
<dd> 0x006400</p>
<dt><code>DarkKhaki</code></p>
<dd> 0xBDB76B</p>
<dt><code>DarkMagenta</code></p>
<dd> 0x8B008B</p>
<dt><code>DarkOliveGreen</code></p>
<dd> 0x556B2F</p>
<dt><code>Darkorange</code></p>
<dd> 0xFF8C00</p>
<dt><code>DarkOrchid</code></p>
<dd> 0x9932CC</p>
<dt><code>DarkRed</code></p>
<dd> 0x8B0000</p>
<dt><code>DarkSalmon</code></p>
<dd> 0xE9967A</p>
<dt><code>DarkSeaGreen</code></p>
<dd> 0x8FBC8F</p>
<dt><code>DarkSlateBlue</code></p>
<dd> 0x483D8B</p>
<dt><code>DarkSlateGray</code></p>
<dd> 0x2F4F4F</p>
<dt><code>DarkTurquoise</code></p>
<dd> 0x00CED1</p>
<dt><code>DarkViolet</code></p>
<dd> 0x9400D3</p>
<dt><code>DeepPink</code></p>
<dd> 0xFF1493</p>
<dt><code>DeepSkyBlue</code></p>
<dd> 0x00BFFF</p>
<dt><code>DimGray</code></p>
<dd> 0x696969</p>
<dt><code>DodgerBlue</code></p>
<dd> 0x1E90FF</p>
<dt><code>FireBrick</code></p>
<dd> 0xB22222</p>
<dt><code>FloralWhite</code></p>
<dd> 0xFFFAF0</p>
<dt><code>ForestGreen</code></p>
<dd> 0x228B22</p>
<dt><code>Fuchsia</code></p>
<dd> 0xFF00FF</p>
<dt><code>Gainsboro</code></p>
<dd> 0xDCDCDC</p>
<dt><code>GhostWhite</code></p>
<dd> 0xF8F8FF</p>
<dt><code>Gold</code></p>
<dd> 0xFFD700</p>
<dt><code>GoldenRod</code></p>
<dd> 0xDAA520</p>
<dt><code>Gray</code></p>
<dd> 0x808080</p>
<dt><code>Green</code></p>
<dd> 0x008000</p>
<dt><code>GreenYellow</code></p>
<dd> 0xADFF2F</p>
<dt><code>HoneyDew</code></p>
<dd> 0xF0FFF0</p>
<dt><code>HotPink</code></p>
<dd> 0xFF69B4</p>
<dt><code>IndianRed</code></p>
<dd> 0xCD5C5C</p>
<dt><code>Indigo</code></p>
<dd> 0x4B0082</p>
<dt><code>Ivory</code></p>
<dd> 0xFFFFF0</p>
<dt><code>Khaki</code></p>
<dd> 0xF0E68C</p>
<dt><code>Lavender</code></p>
<dd> 0xE6E6FA</p>
<dt><code>LavenderBlush</code></p>
<dd> 0xFFF0F5</p>
<dt><code>LawnGreen</code></p>
<dd> 0x7CFC00</p>
<dt><code>LemonChiffon</code></p>
<dd> 0xFFFACD</p>
<dt><code>LightBlue</code></p>
<dd> 0xADD8E6</p>
<dt><code>LightCoral</code></p>
<dd> 0xF08080</p>
<dt><code>LightCyan</code></p>
<dd> 0xE0FFFF</p>
<dt><code>LightGoldenRodYellow</code></p>
<dd> 0xFAFAD2</p>
<dt><code>LightGreen</code></p>
<dd> 0x90EE90</p>
<dt><code>LightGrey</code></p>
<dd> 0xD3D3D3</p>
<dt><code>LightPink</code></p>
<dd> 0xFFB6C1</p>
<dt><code>LightSalmon</code></p>
<dd> 0xFFA07A</p>
<dt><code>LightSeaGreen</code></p>
<dd> 0x20B2AA</p>
<dt><code>LightSkyBlue</code></p>
<dd> 0x87CEFA</p>
<dt><code>LightSlateGray</code></p>
<dd> 0x778899</p>
<dt><code>LightSteelBlue</code></p>
<dd> 0xB0C4DE</p>
<dt><code>LightYellow</code></p>
<dd> 0xFFFFE0</p>
<dt><code>Lime</code></p>
<dd> 0x00FF00</p>
<dt><code>LimeGreen</code></p>
<dd> 0x32CD32</p>
<dt><code>Linen</code></p>
<dd> 0xFAF0E6</p>
<dt><code>Magenta</code></p>
<dd> 0xFF00FF</p>
<dt><code>Maroon</code></p>
<dd> 0x800000</p>
<dt><code>MediumAquaMarine</code></p>
<dd> 0x66CDAA</p>
<dt><code>MediumBlue</code></p>
<dd> 0x0000CD</p>
<dt><code>MediumOrchid</code></p>
<dd> 0xBA55D3</p>
<dt><code>MediumPurple</code></p>
<dd> 0x9370D8</p>
<dt><code>MediumSeaGreen</code></p>
<dd> 0x3CB371</p>
<dt><code>MediumSlateBlue</code></p>
<dd> 0x7B68EE</p>
<dt><code>MediumSpringGreen</code></p>
<dd> 0x00FA9A</p>
<dt><code>MediumTurquoise</code></p>
<dd> 0x48D1CC</p>
<dt><code>MediumVioletRed</code></p>
<dd> 0xC71585</p>
<dt><code>MidnightBlue</code></p>
<dd> 0x191970</p>
<dt><code>MintCream</code></p>
<dd> 0xF5FFFA</p>
<dt><code>MistyRose</code></p>
<dd> 0xFFE4E1</p>
<dt><code>Moccasin</code></p>
<dd> 0xFFE4B5</p>
<dt><code>NavajoWhite</code></p>
<dd> 0xFFDEAD</p>
<dt><code>Navy</code></p>
<dd> 0x000080</p>
<dt><code>OldLace</code></p>
<dd> 0xFDF5E6</p>
<dt><code>Olive</code></p>
<dd> 0x808000</p>
<dt><code>OliveDrab</code></p>
<dd> 0x6B8E23</p>
<dt><code>Orange</code></p>
<dd> 0xFFA500</p>
<dt><code>OrangeRed</code></p>
<dd> 0xFF4500</p>
<dt><code>Orchid</code></p>
<dd> 0xDA70D6</p>
<dt><code>PaleGoldenRod</code></p>
<dd> 0xEEE8AA</p>
<dt><code>PaleGreen</code></p>
<dd> 0x98FB98</p>
<dt><code>PaleTurquoise</code></p>
<dd> 0xAFEEEE</p>
<dt><code>PaleVioletRed</code></p>
<dd> 0xD87093</p>
<dt><code>PapayaWhip</code></p>
<dd> 0xFFEFD5</p>
<dt><code>PeachPuff</code></p>
<dd> 0xFFDAB9</p>
<dt><code>Peru</code></p>
<dd> 0xCD853F</p>
<dt><code>Pink</code></p>
<dd> 0xFFC0CB</p>
<dt><code>Plum</code></p>
<dd> 0xDDA0DD</p>
<dt><code>PowderBlue</code></p>
<dd> 0xB0E0E6</p>
<dt><code>Purple</code></p>
<dd> 0x800080</p>
<dt><code>Red</code></p>
<dd> 0xFF0000</p>
<dt><code>RosyBrown</code></p>
<dd> 0xBC8F8F</p>
<dt><code>RoyalBlue</code></p>
<dd> 0x4169E1</p>
<dt><code>SaddleBrown</code></p>
<dd> 0x8B4513</p>
<dt><code>Salmon</code></p>
<dd> 0xFA8072</p>
<dt><code>SandyBrown</code></p>
<dd> 0xF4A460</p>
<dt><code>SeaGreen</code></p>
<dd> 0x2E8B57</p>
<dt><code>SeaShell</code></p>
<dd> 0xFFF5EE</p>
<dt><code>Sienna</code></p>
<dd> 0xA0522D</p>
<dt><code>Silver</code></p>
<dd> 0xC0C0C0</p>
<dt><code>SkyBlue</code></p>
<dd> 0x87CEEB</p>
<dt><code>SlateBlue</code></p>
<dd> 0x6A5ACD</p>
<dt><code>SlateGray</code></p>
<dd> 0x708090</p>
<dt><code>Snow</code></p>
<dd> 0xFFFAFA</p>
<dt><code>SpringGreen</code></p>
<dd> 0x00FF7F</p>
<dt><code>SteelBlue</code></p>
<dd> 0x4682B4</p>
<dt><code>Tan</code></p>
<dd> 0xD2B48C</p>
<dt><code>Teal</code></p>
<dd> 0x008080</p>
<dt><code>Thistle</code></p>
<dd> 0xD8BFD8</p>
<dt><code>Tomato</code></p>
<dd> 0xFF6347</p>
<dt><code>Turquoise</code></p>
<dd> 0x40E0D0</p>
<dt><code>Violet</code></p>
<dd> 0xEE82EE</p>
<dt><code>Wheat</code></p>
<dd> 0xF5DEB3</p>
<dt><code>White</code></p>
<dd> 0xFFFFFF</p>
<dt><code>WhiteSmoke</code></p>
<dd> 0xF5F5F5</p>
<dt><code>Yellow</code></p>
<dd> 0xFFFF00</p>
<dt><code>YellowGreen</code></p>
<dd> 0x9ACD32</dl>
<h3>Channel Layout</h3>
<p> A channel layout specifies the spatial disposition of the channels in a multi-channel audio stream. To specify a channel layout, FFmpeg makes use of a special syntax. </p>
<p> Individual channels are identified by an id, as given by the table below:</p>
<dl>
<dt><font SIZE="-1"><code>FL</code></font></p>
<dd> front left</p>
<dt><font SIZE="-1"><code>FR</code></font></p>
<dd> front right</p>
<dt><font SIZE="-1"><code>FC</code></font></p>
<dd> front center</p>
<dt><font SIZE="-1"><code>LFE</code></font></p>
<dd> low frequency</p>
<dt><font SIZE="-1"><code>BL</code></font></p>
<dd> back left</p>
<dt><font SIZE="-1"><code>BR</code></font></p>
<dd> back right</p>
<dt><font SIZE="-1"><code>FLC</code></font></p>
<dd> front left-of-center</p>
<dt><font SIZE="-1"><code>FRC</code></font></p>
<dd> front right-of-center</p>
<dt><font SIZE="-1"><code>BC</code></font></p>
<dd> back center</p>
<dt><font SIZE="-1"><code>SL</code></font></p>
<dd> side left</p>
<dt><font SIZE="-1"><code>SR</code></font></p>
<dd> side right</p>
<dt><font SIZE="-1"><code>TC</code></font></p>
<dd> top center</p>
<dt><font SIZE="-1"><code>TFL</code></font></p>
<dd> top front left</p>
<dt><font SIZE="-1"><code>TFC</code></font></p>
<dd> top front center</p>
<dt><font SIZE="-1"><code>TFR</code></font></p>
<dd> top front right</p>
<dt><font SIZE="-1"><code>TBL</code></font></p>
<dd> top back left</p>
<dt><font SIZE="-1"><code>TBC</code></font></p>
<dd> top back center</p>
<dt><font SIZE="-1"><code>TBR</code></font></p>
<dd> top back right</p>
<dt><font SIZE="-1"><code>DL</code></font></p>
<dd> downmix left</p>
<dt><font SIZE="-1"><code>DR</code></font></p>
<dd> downmix right</p>
<dt><font SIZE="-1"><code>WL</code></font></p>
<dd> wide left</p>
<dt><font SIZE="-1"><code>WR</code></font></p>
<dd> wide right</p>
<dt><font SIZE="-1"><code>SDL</code></font></p>
<dd> surround direct left</p>
<dt><font SIZE="-1"><code>SDR</code></font></p>
<dd> surround direct right</p>
<dt><font SIZE="-1"><code>LFE2</code></font></p>
<dd> low frequency 2</dl>
<p> Standard channel layout compositions can be specified by using the following identifiers:</p>
<dl>
<dt><code>mono</code></p>
<dd> <font SIZE="-1">FC</font></p>
<dt><code>stereo</code></p>
<dd> <font SIZE="-1">FL+FR</font></p>
<dt><code>2.1</code></p>
<dd> <font SIZE="-1">FL+FR+LFE</font></p>
<dt><code>3.0</code></p>
<dd> <font SIZE="-1">FL+FR+FC</font></p>
<dt><code>3.0(back)</code></p>
<dd> <font SIZE="-1">FL+FR+BC</font></p>
<dt><code>4.0</code></p>
<dd> <font SIZE="-1">FL+FR+FC+BC</font></p>
<dt><code>quad</code></p>
<dd> <font SIZE="-1">FL+FR+BL+BR</font></p>
<dt><code>quad(side)</code></p>
<dd> <font SIZE="-1">FL+FR+SL+SR</font></p>
<dt><code>3.1</code></p>
<dd> <font SIZE="-1">FL+FR+FC+LFE</font></p>
<dt><code>5.0</code></p>
<dd> <font SIZE="-1">FL+FR+FC+BL+BR</font></p>
<dt><code>5.0(side)</code></p>
<dd> <font SIZE="-1">FL+FR+FC+SL+SR</font></p>
<dt><code>4.1</code></p>
<dd> <font SIZE="-1">FL+FR+FC+LFE+BC</font></p>
<dt><code>5.1</code></p>
<dd> <font SIZE="-1">FL+FR+FC+LFE+BL+BR</font></p>
<dt><code>5.1(side)</code></p>
<dd> <font SIZE="-1">FL+FR+FC+LFE+SL+SR</font></p>
<dt><code>6.0</code></p>
<dd> <font SIZE="-1">FL+FR+FC+BC+SL+SR</font></p>
<dt><code>6.0(front)</code></p>
<dd> <font SIZE="-1">FL+FR+FLC+FRC+SL+SR</font></p>
<dt><code>hexagonal</code></p>
<dd> <font SIZE="-1">FL+FR+FC+BL+BR+BC</font></p>
<dt><code>6.1</code></p>
<dd> <font SIZE="-1">FL+FR+FC+LFE+BC+SL+SR</font></p>
<dt><code>6.1</code></p>
<dd> <font SIZE="-1">FL+FR+FC+LFE+BL+BR+BC</font></p>
<dt><code>6.1(front)</code></p>
<dd> <font SIZE="-1">FL+FR+LFE+FLC+FRC+SL+SR</font></p>
<dt><code>7.0</code></p>
<dd> <font SIZE="-1">FL+FR+FC+BL+BR+SL+SR</font></p>
<dt><code>7.0(front)</code></p>
<dd> <font SIZE="-1">FL+FR+FC+FLC+FRC+SL+SR</font></p>
<dt><code>7.1</code></p>
<dd> <font SIZE="-1">FL+FR+FC+LFE+BL+BR+SL+SR</font></p>
<dt><code>7.1(wide)</code></p>
<dd> <font SIZE="-1">FL+FR+FC+LFE+BL+BR+FLC+FRC</font></p>
<dt><code>7.1(wide-side)</code></p>
<dd> <font SIZE="-1">FL+FR+FC+LFE+FLC+FRC+SL+SR</font></p>
<dt><code>octagonal</code></p>
<dd> <font SIZE="-1">FL+FR+FC+BL+BR+BC+SL+SR</font></p>
<dt><code>hexadecagonal</code></p>
<dd> <font SIZE="-1">FL+FR+FC+BL+BR+BC+SL+SR+WL+WR+TBL+TBR+TBC+TFC+TFL+TFR</font></p>
<dt><code>downmix</code></p>
<dd> <font SIZE="-1">DL+DR</font></dl>
<p> A custom channel layout can be specified as a sequence of terms, separated by &#8216;+&#8217; or &#8216;|&#8217;. Each term can be:</p>
<dl>
<dt>&bull;</p>
<dd> the name of a standard channel layout (e.g. <code>mono</code>, <code>stereo</code>, <code>4.0</code>, <code>quad</code>, <code>5.0</code>, etc.)</p>
<dt>&bull;</p>
<dd> the name of a single channel (e.g. <font SIZE="-1"><code>FL</code></font>, <font SIZE="-1"><code>FR</code></font>, <font SIZE="-1"><code>FC</code></font>, <font SIZE="-1"><code>LFE</code></font>, etc.)</p>
<dt>&bull;</p>
<dd> a number of channels, in decimal, followed by &#8216;c&#8217;, yielding the default channel layout for that number of channels (see the function <tt>&quot;av_get_default_channel_layout&quot;</tt>). Note that not all channel counts have a default layout.</p>
<dt>&bull;</p>
<dd> a number of channels, in decimal, followed by &#8216;C&#8217;, yielding an unknown channel layout with the specified number of channels. Note that not all channel layout specification strings support unknown channel layouts.</p>
<dt>&bull;</p>
<dd> a channel layout mask, in hexadecimal starting with &#8220;0x&#8221; (see the <tt>&quot;AV_CH_*&quot;</tt> macros in <i>libavutil/channel_layout.h</i>.</dl>
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
<dt><code>abs(x)</code></p>
<dd> Compute absolute value of <i>x</i>.</p>
<dt><code>acos(x)</code></p>
<dd> Compute arccosine of <i>x</i>.</p>
<dt><code>asin(x)</code></p>
<dd> Compute arcsine of <i>x</i>.</p>
<dt><code>atan(x)</code></p>
<dd> Compute arctangent of <i>x</i>.</p>
<dt><code>atan2(x, y)</code></p>
<dd> Compute principal value of the arc tangent of <i>y</i>/<i>x</i>.</p>
<dt><code>between(x, min, max)</code></p>
<dd> Return 1 if <i>x</i> is greater than or equal to <i>min</i> and lesser than or equal to <i>max</i>, 0 otherwise.</p>
<dt><code>bitand(x, y)</code></p>
<dd>
<dt><code>bitor(x, y)</code></p>
<dd> Compute bitwise and/or operation on <i>x</i> and <i>y</i>. </p>
<p> The results of the evaluation of <i>x</i> and <i>y</i> are converted to integers before executing the bitwise operation. </p>
<p> Note that both the conversion to integer and the conversion back to floating point can lose precision. Beware of unexpected results for large numbers (usually 2^53 and larger).</p>
<dt><code>ceil(expr)</code></p>
<dd> Round the value of expression <i>expr</i> upwards to the nearest integer. For example, &#8220;ceil(1.5)&#8221; is &#8220;2.0&#8221;.</p>
<dt><code>clip(x, min, max)</code></p>
<dd> Return the value of <i>x</i> clipped between <i>min</i> and <i>max</i>.</p>
<dt><code>cos(x)</code></p>
<dd> Compute cosine of <i>x</i>.</p>
<dt><code>cosh(x)</code></p>
<dd> Compute hyperbolic cosine of <i>x</i>.</p>
<dt><code>eq(x, y)</code></p>
<dd> Return 1 if <i>x</i> and <i>y</i> are equivalent, 0 otherwise.</p>
<dt><code>exp(x)</code></p>
<dd> Compute exponential of <i>x</i> (with base <tt>&quot;e&quot;</tt>, the Euler&#8217;s number).</p>
<dt><code>floor(expr)</code></p>
<dd> Round the value of expression <i>expr</i> downwards to the nearest integer. For example, &#8220;floor(-1.5)&#8221; is &#8220;-2.0&#8221;.</p>
<dt><code>gauss(x)</code></p>
<dd> Compute Gauss function of <i>x</i>, corresponding to <tt>&quot;exp(-x*x/2) / sqrt(2*PI)&quot;</tt>.</p>
<dt><code>gcd(x, y)</code></p>
<dd> Return the greatest common divisor of <i>x</i> and <i>y</i>. If both <i>x</i> and <i>y</i> are 0 or either or both are less than zero then behavior is undefined.</p>
<dt><code>gt(x, y)</code></p>
<dd> Return 1 if <i>x</i> is greater than <i>y</i>, 0 otherwise.</p>
<dt><code>gte(x, y)</code></p>
<dd> Return 1 if <i>x</i> is greater than or equal to <i>y</i>, 0 otherwise.</p>
<dt><code>hypot(x, y)</code></p>
<dd> This function is similar to the C function with the same name; it returns &quot;sqrt(<i>x</i>*<i>x</i> + <i>y</i>*<i>y</i>)&quot;, the length of the hypotenuse of a right triangle with sides of length <i>x</i> and <i>y</i>, or the distance of the point (<i>x</i>, <i>y</i>) from the origin.</p>
<dt><code>if(x, y)</code></p>
<dd> Evaluate <i>x</i>, and if the result is non-zero return the result of the evaluation of <i>y</i>, return 0 otherwise.</p>
<dt><code>if(x, y, z)</code></p>
<dd> Evaluate <i>x</i>, and if the result is non-zero return the evaluation result of <i>y</i>, otherwise the evaluation result of <i>z</i>.</p>
<dt><code>ifnot(x, y)</code></p>
<dd> Evaluate <i>x</i>, and if the result is zero return the result of the evaluation of <i>y</i>, return 0 otherwise.</p>
<dt><code>ifnot(x, y, z)</code></p>
<dd> Evaluate <i>x</i>, and if the result is zero return the evaluation result of <i>y</i>, otherwise the evaluation result of <i>z</i>.</p>
<dt><code>isinf(x)</code></p>
<dd> Return 1.0 if <i>x</i> is +/-INFINITY, 0.0 otherwise.</p>
<dt><code>isnan(x)</code></p>
<dd> Return 1.0 if <i>x</i> is <font SIZE="-1">NAN, 0.0</font> otherwise.</p>
<dt><code>ld(var)</code></p>
<dd> Load the value of the internal variable with number <i>var</i>, which was previously stored with st(<i>var</i>, <i>expr</i>). The function returns the loaded value.</p>
<dt><code>lerp(x, y, z)</code></p>
<dd> Return linear interpolation between <i>x</i> and <i>y</i> by amount of <i>z</i>.</p>
<dt><code>log(x)</code></p>
<dd> Compute natural logarithm of <i>x</i>.</p>
<dt><code>lt(x, y)</code></p>
<dd> Return 1 if <i>x</i> is lesser than <i>y</i>, 0 otherwise.</p>
<dt><code>lte(x, y)</code></p>
<dd> Return 1 if <i>x</i> is lesser than or equal to <i>y</i>, 0 otherwise.</p>
<dt><code>max(x, y)</code></p>
<dd> Return the maximum between <i>x</i> and <i>y</i>.</p>
<dt><code>min(x, y)</code></p>
<dd> Return the minimum between <i>x</i> and <i>y</i>.</p>
<dt><code>mod(x, y)</code></p>
<dd> Compute the remainder of division of <i>x</i> by <i>y</i>.</p>
<dt><code>not(expr)</code></p>
<dd> Return 1.0 if <i>expr</i> is zero, 0.0 otherwise.</p>
<dt><code>pow(x, y)</code></p>
<dd> Compute the power of <i>x</i> elevated <i>y</i>, it is equivalent to &quot;(<i>x</i>)^(<i>y</i>)&quot;.</p>
<dt><code>print(t)</code></p>
<dd>
<dt><code>print(t, l)</code></p>
<dd> Print the value of expression <i>t</i> with loglevel <i>l</i>. If <i>l</i> is not specified then a default log level is used. Returns the value of the expression printed. </p>
<p> Prints t with loglevel l</p>
<dt><code>random(x)</code></p>
<dd> Return a pseudo random value between 0.0 and 1.0. <i>x</i> is the index of the internal variable which will be used to save the seed/state.</p>
<dt><code>root(expr, max)</code></p>
<dd> Find an input value for which the function represented by <i>expr</i> with argument <i></i>ld<i>(0)</i> is 0 in the interval 0..<i>max</i>. </p>
<p> The expression in <i>expr</i> must denote a continuous function or the result is undefined. </p>
<p> <i></i>ld<i>(0)</i> is used to represent the function input value, which means that the given expression will be evaluated multiple times with various input values that the expression can access through <tt>ld(0)</tt>. When the expression evaluates to 0 then the corresponding input value will be returned.</p>
<dt><code>round(expr)</code></p>
<dd> Round the value of expression <i>expr</i> to the nearest integer. For example, &#8220;round(1.5)&#8221; is &#8220;2.0&#8221;.</p>
<dt><code>sgn(x)</code></p>
<dd> Compute sign of <i>x</i>.</p>
<dt><code>sin(x)</code></p>
<dd> Compute sine of <i>x</i>.</p>
<dt><code>sinh(x)</code></p>
<dd> Compute hyperbolic sine of <i>x</i>.</p>
<dt><code>sqrt(expr)</code></p>
<dd> Compute the square root of <i>expr</i>. This is equivalent to &quot;(<i>expr</i>)^.5&quot;.</p>
<dt><code>squish(x)</code></p>
<dd> Compute expression <tt>&quot;1/(1 + exp(4*x))&quot;</tt>.</p>
<dt><code>st(var, expr)</code></p>
<dd> Store the value of the expression <i>expr</i> in an internal variable. <i>var</i> specifies the number of the variable where to store the value, and it is a value ranging from 0 to 9. The function returns the value stored in the internal variable. Note, Variables are currently not shared between expressions.</p>
<dt><code>tan(x)</code></p>
<dd> Compute tangent of <i>x</i>.</p>
<dt><code>tanh(x)</code></p>
<dd> Compute hyperbolic tangent of <i>x</i>.</p>
<dt><code>taylor(expr, x)</code></p>
<dd>
<dt><code>taylor(expr, x, id)</code></p>
<dd> Evaluate a Taylor series at <i>x</i>, given an expression representing the <tt>&quot;ld(id)&quot;</tt>-th derivative of a function at 0. </p>
<p> When the series does not converge the result is undefined. </p>
<p> <i>ld(id)</i> is used to represent the derivative order in <i>expr</i>, which means that the given expression will be evaluated multiple times with various input values that the expression can access through <tt>&quot;ld(id)&quot;</tt>. If <i>id</i> is not specified then 0 is assumed. </p>
<p> Note, when you have the derivatives at y instead of 0, <tt>&quot;taylor(expr, x-y)&quot;</tt> can be used.</p>
<dt><code>time(0)</code></p>
<dd> Return the current (wallclock) time in seconds.</p>
<dt><code>trunc(expr)</code></p>
<dd> Round the value of expression <i>expr</i> towards zero to the nearest integer. For example, &#8220;trunc(-1.5)&#8221; is &#8220;-1.0&#8221;.</p>
<dt><code>while(cond, expr)</code></p>
<dd> Evaluate expression <i>expr</i> while the expression <i>cond</i> is non-zero, and returns the value of the last <i>expr</i> evaluation, or <font SIZE="-1">NAN</font> if <i>cond</i> was always false.</dl>
<p> The following constants are available:</p>
<dl>
<dt><font SIZE="-1"><code>PI</code></font></p>
<dd> area of the unit disc, approximately 3.14</p>
<dt><code>E</code></p>
<dd> <code><a href="/docs/linux/man/1-exp/">exp</a></code>(1) (Euler&#8217;s number), approximately 2.718</p>
<dt><font SIZE="-1"><code>PHI</code></font></p>
<dd> golden ratio (1+<code><a href="/docs/linux/man/5-sqrt/">sqrt</a></code>(5))/2, approximately 1.618</dl>
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
<dt><code>y</code></p>
<dd> 10^-24 / 2^-80</p>
<dt><code>z</code></p>
<dd> 10^-21 / 2^-70</p>
<dt><code>a</code></p>
<dd> 10^-18 / 2^-60</p>
<dt><code>f</code></p>
<dd> 10^-15 / 2^-50</p>
<dt><code>p</code></p>
<dd> 10^-12 / 2^-40</p>
<dt><code>n</code></p>
<dd> 10^-9 / 2^-30</p>
<dt><code>u</code></p>
<dd> 10^-6 / 2^-20</p>
<dt><code>m</code></p>
<dd> 10^-3 / 2^-10</p>
<dt><code>c</code></p>
<dd> 10^-2</p>
<dt><code>d</code></p>
<dd> 10^-1</p>
<dt><code>h</code></p>
<dd> 10^2</p>
<dt><code>k</code></p>
<dd> 10^3 / 2^10</p>
<dt><code>K</code></p>
<dd> 10^3 / 2^10</p>
<dt><code>M</code></p>
<dd> 10^6 / 2^20</p>
<dt><code>G</code></p>
<dd> 10^9 / 2^30</p>
<dt><code>T</code></p>
<dd> 10^12 / 2^40</p>
<dt><code>P</code></p>
<dd> 10^15 / 2^40</p>
<dt><code>E</code></p>
<dd> 10^18 / 2^50</p>
<dt><code>Z</code></p>
<dd> 10^21 / 2^60</p>
<dt><code>Y</code></p>
<dd> 10^24 / 2^70</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></code>(1), <code><a href="/docs/linux/man/1-ffplay/">ffplay</a></code>(1), <code><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></code>(1), <code><a href="/docs/linux/man/3-libavutil/">libavutil</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
<h2>Index</h2>
