---

title: "cdk_histogram(3)"
name: "cdk_histogram"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_histogram/"
description: "cdk_histogram – curses histogram widget"
---

<h2>NAME</h2>
<p> cdk_histogram &#8211; curses histogram widget</p>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>
void activateCDKHistogram(
    CDKHISTOGRAM *histogram,
    chtype unused);
void destroyCDKHistogram(
    CDKHISTOGRAM *histogram);
void drawCDKHistogram(
    CDKHISTOGRAM *histogram,
    boolean box);
void eraseCDKHistogram(
    CDKHISTOGRAM *histogram);
boolean getCDKHistogramBox(
    CDKHISTOGRAM *histogram);
chtype getCDKHistogramFillerChar(
    CDKHISTOGRAM *histogram);
int getCDKHistogramHighValue(
    CDKHISTOGRAM *histogram);
int getCDKHistogramLowValue(
    CDKHISTOGRAM *histogram);
chtype getCDKHistogramStatsAttr(
    CDKHISTOGRAM *histogram);
int getCDKHistogramStatsPos(
    CDKHISTOGRAM *histogram);
int getCDKHistogramValue(
    CDKHISTOGRAM *histogram);
EHistogramDisplayType getCDKHistogramViewType(
    CDKHISTOGRAM *histogram);
void moveCDKHistogram(
    CDKHISTOGRAM *histogram,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKHISTOGRAM *newCDKHistogram(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    int height,
    int width,
    int orient,
    const char *title,
    boolean box,
    boolean shadow);
void positionCDKHistogram(
    CDKHISTOGRAM *histogram);
void setCDKHistogram(
    CDKHISTOGRAM *histogram,
    EHistogramDisplayType viewType,
    int statsPos,
    chtype statsAttribute,
    int lowValue,
    int highValue,
    int currentValue,
    chtype fillerCharacter,
    boolean box);
void setCDKHistogramBackgroundAttrib(
    CDKHISTOGRAM *histogram,
    chtype attribute);
void setCDKHistogramBackgroundColor(
    CDKHISTOGRAM *histogram,
    const char *color);
void setCDKHistogramBox(
    CDKHISTOGRAM *histogram,
    boolean box);
void setCDKHistogramBoxAttribute(
    CDKHISTOGRAM *histogram,
    chtype character);
void setCDKHistogramDisplayType(
    CDKHISTOGRAM *histogram,
    EHistogramDisplayType viewtype);
void setCDKHistogramFillerChar(
    CDKHISTOGRAM *histogram,
    chtype fillerCharacter);
void setCDKHistogramHorizontalChar(
    CDKHISTOGRAM *histogram,
    chtype character);
void setCDKHistogramLLChar(
    CDKHISTOGRAM *histogram,
    chtype character);
void setCDKHistogramLRChar(
    CDKHISTOGRAM *histogram,
    chtype character);
void setCDKHistogramStatsAttr(
    CDKHISTOGRAM *histogram,
    chtype statsAttribute);
void setCDKHistogramStatsPos(
    CDKHISTOGRAM *histogram,
    int statsPosition);
void setCDKHistogramULChar(
    CDKHISTOGRAM *histogram,
    chtype character);
void setCDKHistogramURChar(
    CDKHISTOGRAM *histogram,
    chtype character);
void setCDKHistogramValue(
    CDKHISTOGRAM *histogram,
    int lowValue,
    int highValue,
    int currentValue);
void setCDKHistogramVerticalChar(
    CDKHISTOGRAM *histogram,
    chtype character);
void setCDKHistogramViewType(
    CDKHISTOGRAM *histogram,
    EHistogramDisplayType viewType);
</code></pre>
</dl>
<p> The Cdk histogram widget creates a histogram widget. This widget can draw a vertical or horizontal histogram. The functions create or manipulate the Cdk histogram box widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKHistogram</code></dt>
<dd> obsolete entrypoint which calls <code>drawCDKHistogram</code>.</dd>
<dt><code>destroyCDKHistogram</code></dt>
<dd> removes the widget from the screen and frees memory the object used.</dd>
<dt><code>drawCDKHistogram</code></dt>
<dd> draws the histogram widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</dd>
<dt><code>eraseCDKHistogram</code></dt>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</dd>
<dt><code>getCDKHistogramBox</code></dt>
<dd> returns true if the widget will be drawn with a box around it.</dd>
<dt><code>getCDKHistogramFillerChar</code></dt>
<dd> returns the character being used to draw the histogram bar.</dd>
<dt><code>getCDKHistogramHighValue</code></dt>
<dd> returns the high value of the histogram.</dd>
<dt><code>getCDKHistogramLowValue</code></dt>
<dd> returns the low value of the histogram.</dd>
<dt><code>getCDKHistogramStatsAttr</code></dt>
<dd> returns the attribute of the statistics of the histogram.</dd>
<dt><code>getCDKHistogramStatsPos</code></dt>
<dd> returns where the histogram will draw the statistics.</dd>
<dt><code>getCDKHistogramValue</code></dt>
<dd> returns the current value of the histogram.</dd>
<dt><code>getCDKHistogramViewType</code></dt>
<dd> returns the view type of the histogram widget.</dd>
<dt><code>moveCDKHistogram</code></dt>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> can be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</dd>
<dt><code>newCDKHistogram</code></dt>
<dd> creates a histogram widget and returns a pointer to it. Parameters:</dd>
<dl>
<dl>
<dt><code>screen</code></dt>
<dd> is the screen you wish this widget to be placed in.</dd>
<dt><code>xpos</code></dt>
<dd> controls the placement of the object along the horizontal axis. It may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>.</dd>
<dt><code>ypos</code></dt>
<dd> controls the placement of the object along the vertical axis. It may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</dd>
<dt><code>title</code></dt>
<dd> is the string which will be displayed at the top of the widget. The title can be more than one line; just provide a carriage return character at the line break.</dd>
<dt><code>height</code> and</dt>
<dd>
</dd><dt><code>width</code></dt>
<dd> control the height and width of the widget. If you provide a value of zero for either of the height or the width, the widget will be created with the full width and height of the screen. If you provide a negative value, the widget will be created the full height or width minus the value provided.</dd>
<dt><code>orient</code></dt>
<dd> specifies the orientation of the histogram. It is one of these pre-defined values: <i>VERTICAL</i> and <i>HORIZONTAL</i>.</dd>
<dt><code>label</code></dt>
<dd> is the string to use as the label of the histogram.</dd>
<dt><code>box</code></dt>
<dd> is true if the widget should be drawn with a box around it.</dd>
<dt><code>shadow</code></dt>
<dd> turns the shadow on or off around this widget.</dd></dl>
</dl>
<dt>
</dt><dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</dd>
<dt><code>positionCDKHistogram</code></dt>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</dd>
<dt><code>setCDKHistogram</code></dt>
<dd> lets the programmer set the specific values of the histogram widget. The parameter <code>viewType</code> specifies the type of histogram to draw. The following table lists the valid values and the results.</dd></dl>
<p> <center></p>
<table BORDER>
<tr VALIGN=top>
<td><code>Display_Type</code></td>
<td>Result
</td>
</tr>
<tr VALIGN=top>
<td>vNONE</td>
<td> Displays no information about the current values.
</td>
</tr>
<tr VALIGN=top>
<td>vPERCENT</td>
<td> Displays the current value as a percentage.
</td>
</tr>
<tr VALIGN=top>
<td>vFRACTION</td>
<td> Displays the current value as a fraction.
</td>
</tr>
<tr VALIGN=top>
<td>vREAL</td>
<td>Displays the current value.
</td>
</tr>
</table>
<p></center> </p>
<dl>
<dt>
</dt><dd> The <code>statsPosition</code> parameter states where the statistics will be displayed. It accepts <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</dd>
<dt>
</dt><dd> The parameter <code>statsAttribute</code> sets the attributes of the statistics.</dd>
<dt>
</dt><dd> The parameters <code>lowValue</code>, <code>highValue</code>, and <code>currentValue</code> are the low, high, and current values respectively.</dd>
<dt>
</dt><dd> The <code>filler</code> character is the character to use in the unused space in the histogram.</dd>
<dt>
</dt><dd> If the <code>box</code> parameter is true, the widget is drawn with a box.</dd>
<dt><code>setCDKHistogramBackgroundAttrib</code></dt>
<dd> the background color attribute the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</dd>
<dt><code>setCDKHistogramBackgroundColor</code></dt>
<dd> the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</dd>
<dt><code>setCDKHistogramBox</code></dt>
<dd> sets whether the widget will be drawn with a box around it.</dd>
<dt><code>setCDKHistogramBoxAttribute</code></dt>
<dd> sets the attribute of the box.</dd>
<dt><code>setCDKHistogramDisplayType</code></dt>
<dd> sets the display type (see <code>getCDKHistogramViewType</code>).</dd>
<dt><code>setCDKHistogramFillerChar</code></dt>
<dd> sets the character to use when drawing the histogram bar.</dd>
<dt><code>setCDKHistogramHorizontalChar</code></dt>
<dd> sets the horizontal drawing character for the box to the given character.</dd>
<dt><code>setCDKHistogramLLChar</code></dt>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKHistogramLRChar</code></dt>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKHistogramStatsAttr</code></dt>
<dd> sets the attribute to use when drawing the histogram statistics.</dd>
<dt><code>setCDKHistogramStatsPos</code></dt>
<dd> sets where the statistics will be drawn on the widget. See the <code>setCDKHistogram</code> description for more details.</dd>
<dt><code>setCDKHistogramULChar</code></dt>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKHistogramURChar</code></dt>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKHistogramValue</code></dt>
<dd> sets the low, high, and current value of the histogram.</dd>
<dt><code>setCDKHistogramVerticalChar</code></dt>
<dd> sets the vertical drawing character for the box to the given character.</dd>
<dt><code>setCDKHistogramViewType</code></dt>
<dd> sets the view type of the histogram. Look at the <code>setCDKHistogram</code> description for more details.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
