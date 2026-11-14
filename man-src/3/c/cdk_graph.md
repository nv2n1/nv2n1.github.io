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
<h2>SYNOPSIS</h2>
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
<h2>DESCRIPTION</h2>
<p> The Cdk graph widget creates a graph in either X/Y plot or line mode. The following functions create or manipulate the Cdk graph box widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKGraph</code></p>
<dd> this is an obsolete function that calls <code>drawCDKGraph</code>.</p>
<dt><code>destroyCDKGraph</code></p>
<dd> removes the widget from the screen and frees memory the object used.</p>
<dt><code>drawCDKGraph</code></p>
<dd> draws the graph widget on the screen. The <code>box</code> option tells whether to draw the widget with a box.</p>
<dt><code>eraseCDKGraph</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKGraphBox</code></p>
<dd> returns true if the widget will be drawn with a box around it.</p>
<dt><code>getCDKGraphCharacter</code></p>
<dd> returns the character in the graph at the given index.</p>
<dt><code>getCDKGraphCharacters</code></p>
<dd> returns all the characters currently in the graph widget.</p>
<dt><code>getCDKGraphDisplayType</code></p>
<dd> returns the current display type of the widget.</p>
<dt><code>getCDKGraphValue</code></p>
<dd> returns the value in the graph at the given index.</p>
<dt><code>getCDKGraphValues</code></p>
<dd> returns all the values currently in the graph widget.</p>
<dt><code>moveCDKGraph</code></p>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>newCDKGraph</code></p>
<dd> creates a pointer to a graph widget. Parameters:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>screen</code></p>
<dd> is the screen you wish this widget to be placed in.</p>
<dt><code>xpos</code></p>
<dd> controls the placement of the object along the horizontal axis. It may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>.</p>
<dt><code>ypos</code></p>
<dd> controls the placement of the object along the vertical axis. It may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</p>
<dt><code>height</code> and</p>
<dd>
<dt><code>width</code></p>
<dd> control the height and width of the widget. If you provide a zero for either of the height or the width, the widget will be created with the full width and height of the screen. If you provide a negative value, the widget will be created the full height or width minus the value provided.</p>
<dt><code>title</code>,</p>
<dd>
<dt><code>xtitle</code> and</p>
<dd>
<dt><code>ytitle</code></p>
<dd> are the graph title, the X axis title, and the Y axis title respectively. The graph title may be more than one line by providing a carriage return character at the line break.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKGraph</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>setCDKGraph</code></p>
<dd> lets the programmer set the specific values of the graph widget. The parameter <code>values</code> is an integer array of the values to display in the widget; <code>valueCount</code> is the number of values in the array. The parameter <code>graphCharacters</code> is an array of the characters to use for each graph point. The parameter <code>startAtZero</code> states whether you want the graph to start at zero or the lowest values of the X and Y axis&#8217;. The parameter <code>displayType</code> may be <i>vPLOT</i>, to make the graph draw the values as a plot graph, or <i>vLINE</i> to draw the values as a line graph.</p>
<dt><code>setCDKGraphBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKGraphBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</p>
<dt><code>setCDKGraphBox</code></p>
<dd> sets whether the widget will be drawn with a box around it.</p>
<dt><code>setCDKGraphBoxAttribute</code></p>
<dd> function sets the attribute of the box.</p>
<dt><code>setCDKGraphCharacter</code></p>
<dd> lets the programmer set a specific character of the graph widget. The parameter <code>character</code> is the new character, while <code>index</code> is the index where the new character will be stored.</p>
<dt><code>setCDKGraphCharacters</code></p>
<dd> lets the programmer set the specific characters of the graph widget. The parameter <code>characters</code> is a char pointer array of the characters to display in the widget.</p>
<dt><code>setCDKGraphDisplayType</code></p>
<dd> allows the programmer tochange the way the graph draws itself. The parameter <code>displayType</code> may be <i>vPLOT</i>, to make the graph draw the values as a plot graph, or <i>vLINE</i> to draw the values as a line graph.</p>
<dt><code>setCDKGraphHorizontalChar</code></p>
<dd> sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKGraphLLChar</code></p>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKGraphLRChar</code></p>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKGraphULChar</code></p>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKGraphURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKGraphValue</code></p>
<dd> lets the programmer set a specific value of the graph widget. The parameter <code>value</code> is the new value, while <code>index</code> is the index where the new value will be stored. The parameter <code>startAtZero</code> states whether you want the graph to start at zero or the lowest values of the X and Y axis.</p>
<dt><code>setCDKGraphValues</code></p>
<dd> lets the programmer set the specific values of the graph widget. The parameter <code>values</code> is an integer array of the values to display in the widget; where <code>valueCount</code> is the number of values in the array. The parameter <code>startAtZero</code> states whether you want the graph to start at zero or the lowest values of the X and Y axis&#8217;.</p>
<dt><code>setCDKGraphVerticalChar</code></p>
<dd> sets the vertical drawing character for the box to the given character.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
