---
title: "rrdgraph(1)"
name: "rrdgraph"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdgraph/"
description: "rrdgraph – Round Robin Database tool graphing functions"
---

<h2 class="name">NAME</h2>
<p> rrdgraph &#8211; Round Robin Database tool graphing functions </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool graph|graphv</code> <i>filename</i> [<i>option</i> &#8230;] [<i>data definition</i> &#8230;] [<i>data calculation</i> &#8230;] [<i>variable definition</i> &#8230;] [<i>graph element</i> &#8230;] [<i>print element</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <code>graph</code> function of <code>RRDtool</code> is used to present the data from an <font SIZE="-1"><code>RRD</code></font> to a human viewer. Its main purpose is to create a nice graphical representation, but it can also generate a numerical report.</p>
<h2>OVERVIEW</h2>
<p> <code>rrdtool graph</code> needs data to work with, so you must use one or more <code>data definition</code> statements to collect this data. You are not limited to one database, it&#8217;s perfectly legal to collect data from two or more databases (one per statement, though). </p>
<p> If you want to display averages, maxima, percentiles, etcetera it is best to collect them now using the <code>variable definition</code> statement. Currently this makes no difference, but in a future version of RRDtool you may want to collect these values before consolidation. </p>
<p> The data fetched from the <font SIZE="-1"><code>RRA</code></font> is then <code>consolidated</code> so that there is exactly one data point per pixel in the graph. If you do not take care yourself, <code>RRDtool</code> will expand the range slightly if necessary. Note, in that case the first and/or last pixel may very well become unknown! </p>
<p> Sometimes data is not exactly in the format you would like to display it. For instance, you might be collecting <code>bytes</code> per second, but want to display <code>bits</code> per second. This is what the <code>data calculation</code> command is designed for. After <code>consolidating</code> the data, a copy is made and this copy is modified using a rather powerful <font SIZE="-1"><code>RPN</code></font> command set. </p>
<p> When you are done fetching and processing the data, it is time to graph it (or print it). This ends the <code>rrdtool graph</code> sequence. </p>
<p> Use <code>graphv</code> instead of <code>graph</code> to get detailed information about the graph geometry and data once it is drawn. See the bottom of the document for more information.</p>
<h2>OPTIONS</h2>
<h3><i>filename</i></h3>
<p> The name and path of the graph to generate. It is recommended to end this in <tt>&quot;.png&quot;</tt>, <tt>&quot;.svg&quot;</tt> or <tt>&quot;.eps&quot;</tt>, but <code>RRDtool</code> does not enforce this. </p>
<p> <i>filename</i> can be &#8216;<tt>&quot;-&quot;</tt>&#8216; to send the image to <tt>&quot;stdout&quot;</tt>. In this case, no other output is generated.</p>
<h3>Time range</h3>
<p> [<code>-s</code>|<code>&#8211;start</code> <i>time</i>] [<code>-e</code>|<code>&#8211;end</code> <i>time</i>] [<code>-S</code>|<code>&#8211;step</code> <i>seconds</i>] </p>
<p> The start and end of the time series you would like to display, and which <font SIZE="-1"><code>RRA</code></font> the data should come from. Defaults are: 1 day ago until now, with the best possible resolution. <code>Start</code> and <code>end</code> can be specified in several formats, see AT-STYLE <font SIZE="-1">TIME</font> <font SIZE="-1">SPECIFICATION</font> and rrdgraph_examples. By default, <code>rrdtool graph</code> calculates the width of one pixel in the time domain and tries to get data from an <font SIZE="-1"><code>RRA</code></font> with that resolution. With the <code>step</code> option you can alter this behavior. If you want <code>rrdtool graph</code> to get data at a one-hour resolution from the <font SIZE="-1"><code>RRD</code></font>, set <code>step</code> to 3&#8217;600. Note: a step smaller than one pixel will silently be ignored.</p>
<h3>Labels</h3>
<p> [<code>-t</code>|<code>&#8211;title</code> <i>string</i>] [<code>-v</code>|<code>&#8211;vertical-label</code> <i>string</i>] </p>
<p> A horizontal string at the top of the graph and/or a vertically placed string at the left hand side of the graph.</p>
<h3>Size</h3>
<p> [<code>-w</code>|<code>&#8211;width</code> <i>pixels</i>] [<code>-h</code>|<code>&#8211;height</code> <i>pixels</i>] [<code>-j</code>|<code>&#8211;only-graph</code>] [<code>-D</code>|<code>&#8211;full-size-mode</code>] </p>
<p> By default, the width and height of the <code>canvas</code> (the part with the actual data and such). This defaults to 400 pixels by 100 pixels. </p>
<p> If you specify the <code>&#8211;full-size-mode</code> option, the width and height specify the final dimensions of the output image and the canvas is automatically resized to fit. </p>
<p> If you specify the <code>&#8211;only-graph</code> option and set the height &lt; 32 pixels you will get a tiny graph image (thumbnail) to use as an icon for use in an overview, for example. All labeling will be stripped off the graph.</p>
<h3>Limits</h3>
<p> [<code>-u</code>|<code>&#8211;upper-limit</code> <i>value</i>] [<code>-l</code>|<code>&#8211;lower-limit</code> <i>value</i>] [<code>-r</code>|<code>&#8211;rigid</code>] </p>
<p> By default the graph will be autoscaling so that it will adjust the y-axis to the range of the data. You can change this behavior by explicitly setting the limits. The displayed y-axis will then range at least from <code>lower-limit</code> to <code>upper-limit</code>. Autoscaling will still permit those boundaries to be stretched unless the <code>rigid</code> option is set. </p>
<p> [<code>-A</code>|<code>&#8211;alt-autoscale</code>] </p>
<p> Sometimes the default algorithm for selecting the y-axis scale is not satisfactory. Normally the scale is selected from a predefined set of ranges and this fails miserably when you need to graph something like <tt>&quot;260 + 0.001 * sin(x)&quot;</tt>. This option calculates the minimum and maximum y-axis from the actual minimum and maximum data values. Our example would display slightly less than <tt>&quot;260-0.001&quot;</tt> to slightly more than <tt>&quot;260+0.001&quot;</tt> (this feature was contributed by Sasha Mikheev). </p>
<p> [<code>-J</code>|<code>&#8211;alt-autoscale-min</code>] </p>
<p> Where <tt>&quot;--alt-autoscale&quot;</tt> will modify both the absolute maximum <font SIZE="-1">AND</font> minimum values, this option will only affect the minimum value. The maximum value, if not defined on the command line, will be 0. This option can be useful when graphing router traffic when the <font SIZE="-1">WAN</font> line uses compression, and thus the throughput may be higher than the <font SIZE="-1">WAN</font> line speed. </p>
<p> [<code>-M</code>|<code>&#8211;alt-autoscale-max</code>] </p>
<p> Where <tt>&quot;--alt-autoscale&quot;</tt> will modify both the absolute maximum <font SIZE="-1">AND</font> minimum values, this option will only affect the maximum value. The minimum value, if not defined on the command line, will be 0. This option can be useful when graphing router traffic when the <font SIZE="-1">WAN</font> line uses compression, and thus the throughput may be higher than the <font SIZE="-1">WAN</font> line speed. </p>
<p> [<code>-N</code>|<code>&#8211;no-gridfit</code>] </p>
<p> In order to avoid anti-aliasing blurring effects RRDtool snaps points to device resolution pixels, this results in a crisper appearance. If this is not to your liking, you can use this switch to turn this behavior off. </p>
<p> Grid-fitting is turned off for <font SIZE="-1">PDF</font>, <font SIZE="-1">EPS</font>, <font SIZE="-1">SVG</font> output by default.</p>
<h3>X-Axis</h3>
<p> [<code>-x</code>|<code>&#8211;x-grid</code> <i></i><font SIZE="-1"><i>GTM</i></font><i></i><code>:</code><i></i><font SIZE="-1"><i>GST</i></font><i></i><code>:</code><i></i><font SIZE="-1"><i>MTM</i></font><i></i><code>:</code><i></i><font SIZE="-1"><i>MST</i></font><i></i><code>:</code><i></i><font SIZE="-1"><i>LTM</i></font><i></i><code>:</code><i></i><font SIZE="-1"><i>LST</i></font><i></i><code>:</code><i></i><font SIZE="-1"><i>LPR</i></font><i></i><code>:</code><i></i><font SIZE="-1"><i>LFM</i></font><i></i>] </p>
<p> [<code>-x</code>|<code>&#8211;x-grid</code> <code>none</code>] </p>
<p> The x-axis label is quite complex to configure. If you don&#8217;t have very special needs it is probably best to rely on the auto configuration to get this right. You can specify the string <tt>&quot;none&quot;</tt> to suppress the grid and labels altogether. </p>
<p> The grid is defined by specifying a certain amount of time in the <i>?TM</i> positions. You can choose from <tt>&quot;SECOND&quot;</tt>, <tt>&quot;MINUTE&quot;</tt>, <tt>&quot;HOUR&quot;</tt>, <tt>&quot;DAY&quot;</tt>, <tt>&quot;WEEK&quot;</tt>, <tt>&quot;MONTH&quot;</tt> or <tt>&quot;YEAR&quot;</tt>. Then you define how many of these should pass between each line or label. This pair (<i>?TM:?ST</i>) needs to be specified for the base grid (<i>G??</i>), the major grid (<i>M??</i>) and the labels (<i>L??</i>). For the labels you also must define a precision in <i></i><font SIZE="-1"><i>LPR</i></font><i></i> and a <i>strftime</i> format string in <i></i><font SIZE="-1"><i>LFM</i></font><i></i>. <i></i><font SIZE="-1"><i>LPR</i></font><i></i> defines where each label will be placed. If it is zero, the label will be placed right under the corresponding line (useful for hours, dates etcetera). If you specify a number of seconds here the label is centered on this interval (useful for Monday, January etcetera). </p>
<pre>
 --x-grid MINUTE:10:HOUR:1:HOUR:4:0:%X
</pre>
<p> This places grid lines every 10 minutes, major grid lines every hour, and labels every 4 hours. The labels are placed under the major grid lines as they specify exactly that time. </p>
<pre>
 --x-grid HOUR:8:DAY:1:DAY:1:86400:%A
</pre>
<p> This places grid lines every 8 hours, major grid lines and labels each day. The labels are placed exactly between two major grid lines as they specify the complete day and not just midnight.</p>
<h3>Y-Axis</h3>
<p> [<code>-y</code>|<code>&#8211;y-grid</code> <i>grid step</i><code>:</code><i>label factor</i>] </p>
<p> [<code>-y</code>|<code>&#8211;y-grid</code> <code>none</code>] </p>
<p> Y-axis grid lines appear at each <i>grid step</i> interval. Labels are placed every <i>label factor</i> lines. You can specify <tt>&quot;-y none&quot;</tt> to suppress the grid and labels altogether. The default for this option is to automatically select sensible values. </p>
<p> If you have set &#8211;y-grid to &#8216;none&#8217; not only the labels get suppressed, also the space reserved for the labels is removed. You can still add space manually if you use the &#8211;units-length command to explicitly reserve space. </p>
<p> [<code>-Y</code>|<code>&#8211;alt-y-grid</code>] </p>
<p> Place the Y grid dynamically based on the graph&#8217;s Y range. The algorithm ensures that you always have a grid, that there are enough but not too many grid lines, and that the grid is metric. That is the grid lines are placed every 1, 2, 5 or 10 units. This parameter will also ensure that you get enough decimals displayed even if your graph goes from 69.998 to 70.001. (contributed by Sasha Mikheev). </p>
<p> [<code>-o</code>|<code>&#8211;logarithmic</code>] </p>
<p> Logarithmic y-axis scaling. </p>
<p> [<code>-X</code>|<code>&#8211;units-exponent</code> <i>value</i>] </p>
<p> This sets the 10**exponent scaling of the y-axis values. Normally, values will be scaled to the appropriate units (k, M, etc.). However, you may wish to display units always in k (Kilo, 10e3) even if the data is in the M (Mega, 10e6) range, for instance. Value should be an integer which is a multiple of 3 between -18 and 18 inclusively. It is the exponent on the units you wish to use. For example, use 3 to display the y-axis values in k (Kilo, 10e3, thousands), use -6 to display the y-axis values in u (Micro, 10e-6, millionths). Use a value of 0 to prevent any scaling of the y-axis values. </p>
<p> This option is very effective at confusing the heck out of the default RRDtool autoscaling function and grid painter. If RRDtool detects that it is not successful in labeling the graph under the given circumstances, it will switch to the more robust <code>&#8211;alt-y-grid</code> mode. </p>
<p> [<code>-L</code>|<code>&#8211;units-length</code> <i>value</i>] </p>
<p> How many digits should RRDtool assume the y-axis labels to be? You may have to use this option to make enough space once you start fiddling with the y-axis labeling. </p>
<p> [<code>&#8211;units=si</code>] </p>
<p> With this option y-axis values on logarithmic graphs will be scaled to the appropriate units (k, M, etc.) instead of using exponential notation. Note that for linear graphs, <font SIZE="-1">SI</font> notation is used by default.</p>
<h3>Right Y Axis</h3>
<p> [<code>&#8211;right-axis</code> <i>scale</i><code>:</code><i>shift</i>] [<code>&#8211;right-axis-label</code> <i>label</i>] </p>
<p> A second axis will be drawn to the right of the graph. It is tied to the left axis via the scale and shift parameters. You can also define a label for the right axis. </p>
<p> [<code>&#8211;right-axis-format</code> <i>format-string</i>] </p>
<p> By default the format of the axis labels gets determined automatically. If you want to do this your self, use this option with the same <tt>%lf</tt> arguments you know from the <font SIZE="-1">PRINT</font> and <font SIZE="-1">GPRINT</font> commands.</p>
<h3>Legend</h3>
<p> [<code>-g</code>|<code>&#8211;no-legend</code>] </p>
<p> Suppress generation of the legend; only render the graph. </p>
<p> [<code>-F</code>|<code>&#8211;force-rules-legend</code>] </p>
<p> Force the generation of <font SIZE="-1">HRULE</font> and <font SIZE="-1">VRULE</font> legends even if those <font SIZE="-1">HRULE</font> or <font SIZE="-1">VRULE</font> will not be drawn because out of graph boundaries (mimics behavior of pre 1.0.42 versions). </p>
<p> [<code>&#8211;legend-position</code>=(north|south|west|east)] </p>
<p> Place the legend at the given side of the graph. The default is south. In west or east position it is necessary to add line breaks manually. </p>
<p> [<code>&#8211;legend-direction</code>=(topdown|bottomup)] </p>
<p> Place the legend items in the given vertical order. The default is topdown. Using bottomup the legend items appear in the same vertical order as a stack of lines or areas.</p>
<h3>Miscellaneous</h3>
<p> [<code>-z</code>|<code>&#8211;lazy</code>] </p>
<p> Only generate the graph if the current graph is out of date or not existent. Note, that all the calculations will happen regardless so that the output of <font SIZE="-1">PRINT</font> and graphv will be complete regardless. Note that the behavior of lazy in this regard has seen several changes over time. The only thing you can really rely on before RRDtool 1.3.7 is that lazy will not generate the graph when it is already there and up to date, and also that it will output the size of the graph. </p>
<p> [<code>&#8211;daemon</code> <i>address</i>] </p>
<p> Address of the rrdcached daemon. If specified, a <tt>&quot;flush&quot;</tt> command is sent to the server before reading the <font SIZE="-1">RRD</font> files. This allows the graph to contain fresh data even if the daemon is configured to cache values for a long time. For a list of accepted formats, see the <code>-l</code> option in the rrdcached manual. </p>
<pre><code>
rrdtool graph[...]-- daemon unix : / var / run / rrdcached.sock[...]
</code></pre>
<p> [<code>-f</code>|<code>&#8211;imginfo</code> <i>printfstr</i>] </p>
<p> After the image has been created, the graph function uses printf together with this format string to create output similar to the <font SIZE="-1">PRINT</font> function, only that the printf function is supplied with the parameters <i>filename</i>, <i>xsize</i> and <i>ysize</i>. In order to generate an <font SIZE="-1"><code>IMG</code></font> tag suitable for including the graph into a web page, the command line would look like this: </p>
<pre>
 --imginfo '&lt;IMG SRC=&quot;/img/%s&quot; WIDTH=&quot;%lu&quot; HEIGHT=&quot;%lu&quot; ALT=&quot;Demo&quot;&gt;'
</pre>
<p> [<code>-c</code>|<code>&#8211;color</code> <i></i><font SIZE="-1"><i>COLORTAG</i></font><i></i>#<i>rrggbb</i>[<i>aa</i>]] </p>
<p> Override the default colors for the standard elements of the graph. The <i></i><font SIZE="-1"><i>COLORTAG</i></font><i></i> is one of <tt>&quot;BACK&quot;</tt> background, <tt>&quot;CANVAS&quot;</tt> for the background of the actual graph, <tt>&quot;SHADEA&quot;</tt> for the left and top border, <tt>&quot;SHADEB&quot;</tt> for the right and bottom border, <tt>&quot;GRID&quot;</tt>, <tt>&quot;MGRID&quot;</tt> for the major grid, <tt>&quot;FONT&quot;</tt> for the color of the font, <tt>&quot;AXIS&quot;</tt> for the axis of the graph, <tt>&quot;FRAME&quot;</tt> for the line around the color spots, and finally <tt>&quot;ARROW&quot;</tt> for the arrow head pointing up and forward. Each color is composed out of three hexadecimal numbers specifying its rgb color component (00 is off, <font SIZE="-1">FF</font> is maximum) of red, green and blue. Optionally you may add another hexadecimal number specifying the transparency (<font SIZE="-1">FF</font> is solid). You may set this option several times to alter multiple defaults. </p>
<p> A green arrow is made by: <tt>&quot;--color ARROW#00FF00&quot;</tt> </p>
<p> [<code>&#8211;grid-dash</code> <i>on</i><code>:</code><i>off</i>] </p>
<p> by default the grid is drawn in a 1 on, 1 off pattern. With this option you can set this yourself </p>
<p> &#8211;grid-dash 1:3    for a dot grid</p>
<p> &#8211;grid-dash 1:0    for uninterrupted grid lines</p>
<p> [<code>&#8211;border</code> <i>width</i>]] </p>
<p> Width in pixels for the 3d border drawn around the image. Default 2, 0 disables the border. See <tt>&quot;SHADEA&quot;</tt> and <tt>&quot;SHADEB&quot;</tt> above for setting the border color. </p>
<p> [<code>&#8211;dynamic-labels</code>] </p>
<p> Pick the shape of the color marker next to the label according to the element drawn on the graph. </p>
<p> [<code>-m</code>|<code>&#8211;zoom</code> <i>factor</i>] </p>
<p> Zoom the graphics by the given amount. The factor must be &gt; 0 </p>
<p> [<code>-n</code>|<code>&#8211;font</code> <i></i><font SIZE="-1"><i>FONTTAG</i></font><i></i><code>:</code><i>size</i><code>:</code>[<i>font</i>]] </p>
<p> This lets you customize which font to use for the various text elements on the <font SIZE="-1">RRD</font> graphs. <tt>&quot;DEFAULT&quot;</tt> sets the default value for all elements, <tt>&quot;TITLE&quot;</tt> for the title, <tt>&quot;AXIS&quot;</tt> for the axis labels, <tt>&quot;UNIT&quot;</tt> for the vertical unit label, <tt>&quot;LEGEND&quot;</tt> for the graph legend, <tt>&quot;WATERMARK&quot;</tt> for the watermark on the edge of the graph. </p>
<p> Use Times for the title: <tt>&quot;--font TITLE:13:Times&quot;</tt> </p>
<p> Note that you need to quote the argument to <code>&#8211;font</code> if the font-name contains whitespace: &#8211;font &#8220;TITLE:13:Some Font&#8221; </p>
<p> If you do not give a font string you can modify just the size of the default font: <tt>&quot;--font TITLE:13:&quot;</tt>. </p>
<p> If you specify the size 0 then you can modify just the font without touching the size. This is especially useful for altering the default font without resetting the default fontsizes: <tt>&quot;--font DEFAULT:0:Courier&quot;</tt>. </p>
<p> RRDtool comes with a preset default font. You can set the environment variable <tt>&quot;RRD_DEFAULT_FONT&quot;</tt> if you want to change this. </p>
<p> RRDtool uses Pango for its font handling. This means you can to use the full Pango syntax when selecting your font: </p>
<p> The font name has the form &quot;[<i>FAMILY-LIST</i>] [<i>STYLE-OPTIONS</i>] [<i></i><font SIZE="-1"><i>SIZE</i></font><i></i>]&quot;, where <i>FAMILY-LIST</i> is a comma separated list of families optionally terminated by a comma, <i></i><font SIZE="-1"><i>STYLE_OPTIONS</i></font><i></i> is a whitespace separated list of words where each <font SIZE="-1">WORD</font> describes one of style, variant, weight, stretch, or gravity, and <i></i><font SIZE="-1"><i>SIZE</i></font><i></i> is a decimal number (size in points) or optionally followed by the unit modifier &#8220;px&#8221; for absolute size. Any one of the options may be absent. </p>
<p> [<code>-R</code>|<code>&#8211;font-render-mode</code> {<code>normal</code>,<code>light</code>,<code>mono</code>}] </p>
<p> There are 3 font render modes: </p>
<p> <code>normal</code>: Full Hinting and Anti-aliasing (default) </p>
<p> <code>light</code>: Slight Hinting and Anti-aliasing </p>
<p> <code>mono</code>: Full Hinting and <font SIZE="-1">NO</font> Anti-aliasing </p>
<p> [<code>-B</code>|<code>&#8211;font-smoothing-threshold</code> <i>size</i>] </p>
<p> (this gets ignored in 1.3 for now!) </p>
<p> This specifies the largest font size which will be rendered bitmapped, that is, without any font smoothing. By default, no text is rendered bitmapped. </p>
<p> [<code>-P</code>|<code>&#8211;pango-markup</code>] </p>
<p> All text in RRDtool is rendered using Pango. With the <code>&#8211;pango-markup</code> option, all text will be processed by pango markup. This allows to embed some simple html like markup tags using </p>
<pre>
 &lt;span key=&quot;value&quot;&gt;text&lt;/span&gt;
</pre>
<p> Apart from the verbose syntax, there are also the following short tags available. </p>
<pre>
 b     Bold
 big   Makes font relatively larger, equivalent to &lt;span size=&quot;larger&quot;&gt;
 i     Italic
 s     Strikethrough
 sub   Subscript
 sup   Superscript
 small Makes font relatively smaller, equivalent to &lt;span size=&quot;smaller&quot;&gt;
 tt    Monospace font
 u     Underline
</pre>
<p> More details on &lt;<a rel="nofollow" href="http://developer.gnome.org/pango/stable/PangoMarkupFormat.html">http://developer.gnome.org/pango/stable/PangoMarkupFormat.html</a>&gt;. </p>
<p> [<code>-G</code>|<code>&#8211;graph-render-mode</code> {<code>normal</code>,<code>mono</code>}] </p>
<p> There are 2 render modes: </p>
<p> <code>normal</code>: Graphs are fully Anti-aliased (default) </p>
<p> <code>mono</code>: No Anti-aliasing </p>
<p> [<code>-E</code>|<code>&#8211;slope-mode</code>] </p>
<p> RRDtool graphs are composed of stair case curves by default. This is in line with the way RRDtool calculates its data. Some people favor a more &#8216;organic&#8217; look for their graphs even though it is not all that true. </p>
<p> [<code>-a</code>|<code>&#8211;imgformat</code> <font SIZE="-1"><code>PNG</code></font>|<font SIZE="-1"><code>SVG</code></font>|<font SIZE="-1"><code>EPS</code></font>|<font SIZE="-1"><code>PDF</code></font>] </p>
<p> Image format for the generated graph. For the vector formats you can choose among the standard Postscript fonts Courier-Bold, Courier-BoldOblique, Courier-Oblique, Courier, Helvetica-Bold, Helvetica-BoldOblique, Helvetica-Oblique, Helvetica, Symbol, Times-Bold, Times-BoldItalic, Times-Italic, Times-Roman, and ZapfDingbats. </p>
<p> [<code>-i</code>|<code>&#8211;interlaced</code>] </p>
<p> (this gets ignored in 1.3 for now!) </p>
<p> If images are interlaced they become visible on browsers more quickly. </p>
<p> [<code>-T</code>|<code>&#8211;tabwidth</code> <i>value</i>] </p>
<p> By default the tab-width is 40 pixels, use this option to change it. </p>
<p> [<code>-b</code>|<code>&#8211;base</code> <i>value</i>] </p>
<p> If you are graphing memory (and <font SIZE="-1">NOT</font> network traffic) this switch should be set to 1024 so that one Kb is 1024 byte. For traffic measurement, 1 kb/s is 1000 b/s. </p>
<p> [<code>-W</code>|<code>&#8211;watermark</code> <i>string</i>] </p>
<p> Adds the given string as a watermark, horizontally centered, at the bottom of the graph.</p>
<h3>Data and variables</h3>
<p> <font SIZE="-1"><code>DEF:</code></font><i>vname</i><code>=</code><i>rrdfile</i><code>:</code><i>ds-name</i><code>:</code><i></i><font SIZE="-1"><i>CF</i></font><i></i>[<code>:step=</code><i>step</i>][<code>:start=</code><i>time</i>][<code>:end=</code><i>time</i>] </p>
<p> <font SIZE="-1"><code>CDEF:</code></font><i>vname</i><code>=</code><i></i><font SIZE="-1"><i>RPN</i></font><i> expression</i> </p>
<p> <font SIZE="-1"><code>VDEF:</code></font><i>vname</i><code>=</code><i></i><font SIZE="-1"><i>RPN</i></font><i> expression</i> </p>
<p> You need at least one <font SIZE="-1"><code>DEF</code></font> and one <font SIZE="-1"><code>LINE</code></font>, <font SIZE="-1"><code>AREA</code></font>, <font SIZE="-1"><code>GPRINT</code></font>, <font SIZE="-1"><code>PRINT</code></font> statement to generate anything useful. </p>
<p> See rrdgraph_data and rrdgraph_rpn for the exact format. </p>
<p> <font SIZE="-1">NOTE:</font> <code>Graph and print elements</code> </p>
<p> You need at least one graph element to generate an image and/or at least one print statement to generate a report. See rrdgraph_graph for the exact format.</p>
<h3>graphv</h3>
<p> Calling RRDtool with the graphv option will return information in the RRDtool info format. On the command line this means that all output will be in key=value format. When used from the Perl and Ruby bindings a hash pointer will be returned from the call. </p>
<p> When the filename &#8216;-&#8216; is given, the contents of the graph itself will also be returned through this interface (hash key &#8216;image&#8217;). On the command line the output will look like this: </p>
<pre><code>
print[0] = "0.020833" print[1] = "0.0440833" graph_left = 51 graph_top = 22 graph_width = 400 graph_height = 100 graph_start = 1232908800 graph_end = 1232914200 image_width = 481 image_height = 154 value_min = 0.0000000000e+00 value_max = 4.0000000000e-02 image = BLOB_SIZE : 8196
    [... 8196 bytes of image data...]
</code></pre>
<p> There is more information returned than in the standard interface. Especially the &#8216;graph_*&#8217; keys are new. They help applications that want to know what is where on the graph.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables may be used to change the behavior of <tt>&quot;rrdtool graph&quot;</tt>:</p>
<dl>
<dt><font SIZE="-1"><code>RRDCACHED_ADDRESS</code></font></p>
<dd> If this environment variable is set it will have the same effect as specifying the <tt>&quot;--daemon&quot;</tt> option on the command line. If both are present, the command line argument takes precedence.</dl>
<h2>SEE ALSO</h2>
<p> rrdgraph gives an overview of how <code>rrdtool graph</code> works. rrdgraph_data describes <font SIZE="-1"><code>DEF</code></font>,<font SIZE="-1"><code>CDEF</code></font> and <font SIZE="-1"><code>VDEF</code></font> in detail. rrdgraph_rpn describes the <font SIZE="-1"><code>RPN</code></font> language used in the <code>?DEF</code> statements. rrdgraph_graph page describes all of the graph and print functions. </p>
<p> Make sure to read rrdgraph_examples for tips&amp;tricks.</p>
<h2>AUTHOR</h2>
<p> Program by Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<p> This manual page by Alex van den Bogaerdt &lt;alex [at] vandenbogaerdt.nl&gt; with corrections and/or additions by several people </p>
<h2>Index</h2>
<dt><a href="#lbAS">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAT">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAU">AUTHOR</a></p>
<dd></dl>
