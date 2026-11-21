---

title: "cdk_graph(3)"
name: "cdk_graph"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_graph/"
description: "cdk_graph – curses graph widget"
---

<h2>NAME</h2>
<p> cdk_graph &#8211; curses graph widget</p>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>
void activateCDKGraph(
    CDKGRAPH *graph,
    chtype *unused);
void destroyCDKGraph(
    CDKGRAPH *graph);
void drawCDKGraph(
    CDKGRAPH *graph,
    boolean box);
void eraseCDKGraph(
    CDKGRAPH *graph);
boolean getCDKGraphBox(
    CDKGRAPH *graph);
chtype getCDKGraphCharacter(
    CDKGRAPH *graph,
    int index);
chtype *getCDKGraphCharacters(
    CDKGRAPH *graph);
EGraphDisplayType getCDKGraphDisplayType(
    CDKGRAPH *graph);
int getCDKGraphValue(
    CDKGRAPH *graph,
    int index);
int *getCDKGraphValues(
    CDKGRAPH *graph,
    int *size);
void moveCDKGraph(
    CDKGRAPH *graph,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKGRAPH *newCDKGraph(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    int height,
    int width,
    const char *title,
    const char *xtitle,
    const char *ytitle);
void positionCDKGraph(
    CDKGRAPH *graph);
int setCDKGraph(
    CDKGRAPH *graph,
    int *values,
    int valueCount,
    const char *graphCharacters,
    boolean startAtZero,
    EGraphDisplayType displayType);
void setCDKGraphBackgroundAttrib(
    CDKGRAPH *graph,
    chtype attribute);
void setCDKGraphBackgroundColor(
    CDKGRAPH *graph,
    const char *color);
void setCDKGraphBox(
    CDKGRAPH *graph,
    boolean box);
void setCDKGraphBoxAttribute(
    CDKGRAPH *graph,
    chtype character);
int setCDKGraphCharacter(
    CDKGRAPH *graph,
    int index,
    const char *graphCharacter);
int setCDKGraphCharacters(
    CDKGRAPH *graph,
    const char *graphCharacters);
void setCDKGraphDisplayType(
    CDKGRAPH *graph,
    EGraphDisplayType type);
void setCDKGraphHorizontalChar(
    CDKGRAPH *graph,
    chtype character);
void setCDKGraphLLChar(
    CDKGRAPH *graph,
    chtype character);
void setCDKGraphLRChar(
    CDKGRAPH *graph,
    chtype character);
void setCDKGraphULChar(
    CDKGRAPH *graph,
    chtype character);
void setCDKGraphURChar(
    CDKGRAPH *graph,
    chtype character);
int setCDKGraphValue(
    CDKGRAPH *graph,
    int index,
    int value,
    boolean startAtZero);
int setCDKGraphValues(
    CDKGRAPH *graph,
    int *values,
    int valueCount,
    boolean startAtZero);
void setCDKGraphVerticalChar(
    CDKGRAPH *graph,
    chtype character);
</code></pre>
</dl>
<p> The Cdk graph widget creates a graph in either X/Y plot or line mode. The following functions create or manipulate the Cdk graph box widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKGraph</code></dt>
<dd> this is an obsolete function that calls <code>drawCDKGraph</code>.</dd>
<dt><code>destroyCDKGraph</code></dt>
<dd> removes the widget from the screen and frees memory the object used.</dd>
<dt><code>drawCDKGraph</code></dt>
<dd> draws the graph widget on the screen. The <code>box</code> option tells whether to draw the widget with a box.</dd>
<dt><code>eraseCDKGraph</code></dt>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</dd>
<dt><code>getCDKGraphBox</code></dt>
<dd> returns true if the widget will be drawn with a box around it.</dd>
<dt><code>getCDKGraphCharacter</code></dt>
<dd> returns the character in the graph at the given index.</dd>
<dt><code>getCDKGraphCharacters</code></dt>
<dd> returns all the characters currently in the graph widget.</dd>
<dt><code>getCDKGraphDisplayType</code></dt>
<dd> returns the current display type of the widget.</dd>
<dt><code>getCDKGraphValue</code></dt>
<dd> returns the value in the graph at the given index.</dd>
<dt><code>getCDKGraphValues</code></dt>
<dd> returns all the values currently in the graph widget.</dd>
<dt><code>moveCDKGraph</code></dt>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</dd>
<dt><code>newCDKGraph</code></dt>
<dd> creates a pointer to a graph widget. Parameters:</dd>
<dl>
<dl>
<dt><code>screen</code></dt>
<dd> is the screen you wish this widget to be placed in.</dd>
<dt><code>xpos</code></dt>
<dd> controls the placement of the object along the horizontal axis. It may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>.</dd>
<dt><code>ypos</code></dt>
<dd> controls the placement of the object along the vertical axis. It may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</dd>
<dt><code>height</code> and</dt>
<dd>
</dd><dt><code>width</code></dt>
<dd> control the height and width of the widget. If you provide a zero for either of the height or the width, the widget will be created with the full width and height of the screen. If you provide a negative value, the widget will be created the full height or width minus the value provided.</dd>
<dt><code>title</code>,</dt>
<dd>
</dd><dt><code>xtitle</code> and</dt>
<dd>
</dd><dt><code>ytitle</code></dt>
<dd> are the graph title, the X axis title, and the Y axis title respectively. The graph title may be more than one line by providing a carriage return character at the line break.</dd></dl>
</dl>
<dt>
</dt><dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</dd>
<dt><code>positionCDKGraph</code></dt>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</dd>
<dt><code>setCDKGraph</code></dt>
<dd> lets the programmer set the specific values of the graph widget. The parameter <code>values</code> is an integer array of the values to display in the widget; <code>valueCount</code> is the number of values in the array. The parameter <code>graphCharacters</code> is an array of the characters to use for each graph point. The parameter <code>startAtZero</code> states whether you want the graph to start at zero or the lowest values of the X and Y axis&#8217;. The parameter <code>displayType</code> may be <i>vPLOT</i>, to make the graph draw the values as a plot graph, or <i>vLINE</i> to draw the values as a line graph.</dd>
<dt><code>setCDKGraphBackgroundAttrib</code></dt>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</dd>
<dt><code>setCDKGraphBackgroundColor</code></dt>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</dd>
<dt><code>setCDKGraphBox</code></dt>
<dd> sets whether the widget will be drawn with a box around it.</dd>
<dt><code>setCDKGraphBoxAttribute</code></dt>
<dd> function sets the attribute of the box.</dd>
<dt><code>setCDKGraphCharacter</code></dt>
<dd> lets the programmer set a specific character of the graph widget. The parameter <code>character</code> is the new character, while <code>index</code> is the index where the new character will be stored.</dd>
<dt><code>setCDKGraphCharacters</code></dt>
<dd> lets the programmer set the specific characters of the graph widget. The parameter <code>characters</code> is a char pointer array of the characters to display in the widget.</dd>
<dt><code>setCDKGraphDisplayType</code></dt>
<dd> allows the programmer tochange the way the graph draws itself. The parameter <code>displayType</code> may be <i>vPLOT</i>, to make the graph draw the values as a plot graph, or <i>vLINE</i> to draw the values as a line graph.</dd>
<dt><code>setCDKGraphHorizontalChar</code></dt>
<dd> sets the horizontal drawing character for the box to the given character.</dd>
<dt><code>setCDKGraphLLChar</code></dt>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKGraphLRChar</code></dt>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKGraphULChar</code></dt>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKGraphURChar</code></dt>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKGraphValue</code></dt>
<dd> lets the programmer set a specific value of the graph widget. The parameter <code>value</code> is the new value, while <code>index</code> is the index where the new value will be stored. The parameter <code>startAtZero</code> states whether you want the graph to start at zero or the lowest values of the X and Y axis.</dd>
<dt><code>setCDKGraphValues</code></dt>
<dd> lets the programmer set the specific values of the graph widget. The parameter <code>values</code> is an integer array of the values to display in the widget; where <code>valueCount</code> is the number of values in the array. The parameter <code>startAtZero</code> states whether you want the graph to start at zero or the lowest values of the X and Y axis&#8217;.</dd>
<dt><code>setCDKGraphVerticalChar</code></dt>
<dd> sets the vertical drawing character for the box to the given character.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
