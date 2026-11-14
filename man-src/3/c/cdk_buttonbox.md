---
title: "cdk_buttonbox(3)"
name: "cdk_buttonbox"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_buttonbox/"
description: "cdk_buttonbox – Creates a managed curses buttonbox widget."
---

<h2>NAME</h2>
<p> cdk_buttonbox &#8211; Creates a managed curses buttonbox widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

int activateCDKButtonbox(
    CDKBUTTONBOX *buttonbox,
    chtype *actions);
void destroyCDKButtonbox(
    CDKBUTTONBOX *buttonbox);
void drawCDKButtonbox(
    CDKBUTTONBOX *buttonbox,
    boolean box);
void drawCDKButtonboxButtons(
    CDKBUTTONBOX *buttonbox);
void eraseCDKButtonbox(
    CDKBUTTONBOX *buttonbox);
boolean getCDKButtonboxBox(
    CDKBUTTONBOX *buttonbox);
int getCDKButtonboxButtonCount(
    CDKBUTTONBOX *buttonbox);
int getCDKButtonboxCurrentButton(
    CDKBUTTONBOX *buttonbox);
chtype getCDKButtonboxHighlight(
    CDKBUTTONBOX *buttonbox);
int injectCDKButtonbox(
    CDKBUTTONBOX *buttonbox,
    chtype input);
void moveCDKButtonbox(
    CDKBUTTONBOX *buttonbox,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKBUTTONBOX *newCDKButtonbox(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    int height,
    int width,
    const char *title,
    int rows,
    int cols,
    CDK_CONST char **buttons,
    int buttonCount,
    chtype highlight,
    boolean box,
    boolean shadow);
void positionCDKButtonbox(
    CDKBUTTONBOX *buttonbox);
void setCDKButtonbox(
    CDKBUTTONBOX *buttonbox,
    chtype highlight,
    boolean box);
void setCDKButtonboxBackgroundAttrib(
    CDKBUTTONBOX *buttonbox,
    chtype attribute);
void setCDKButtonboxBackgroundColor(
    CDKBUTTONBOX *buttonbox,
    const char *color);
void setCDKButtonboxBox(
    CDKBUTTONBOX *buttonbox,
    boolean box);
void setCDKButtonboxBoxAttribute(
    CDKBUTTONBOX *buttonbox,
    chtype character);
void setCDKButtonboxCurrentButton(
    CDKBUTTONBOX *buttonbox,
    int button);
void setCDKButtonboxHighlight(
    CDKBUTTONBOX *buttonbox,
    chtype highlight);
void setCDKButtonboxHorizontalChar(
    CDKBUTTONBOX *buttonbox,
    chtype character);
void setCDKButtonboxLLChar(
    CDKBUTTONBOX *buttonbox,
    chtype character);
void setCDKButtonboxLRChar(
    CDKBUTTONBOX *buttonbox,
    chtype character);
void setCDKButtonboxPostProcess(
    CDKBUTTONBOX *buttonbox,
    PROCESSFN callback,
    void *data);
void setCDKButtonboxPreProcess(
    CDKBUTTONBOX *buttonbox,
    PROCESSFN callback,
    void *data);
void setCDKButtonboxULChar(
    CDKBUTTONBOX *buttonbox,
    chtype character);
void setCDKButtonboxURChar(
    CDKBUTTONBOX *buttonbox,
    chtype character);
void setCDKButtonboxVerticalChar(
    CDKBUTTONBOX *buttonbox,
    chtype character);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk buttonbox widget creates a buttonbox box with a message and a varied number of buttons to choose from. The following functions create or manipulate the Cdk buttonbox box widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKButtonbox</code></p>
<dd> activates the buttonbox widget and lets the user interact with the widget. The parameter <code>buttonbox</code> is a pointer to a non-NULL buttonbox widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> or <i>TAB</i> then this function will return a value from 0 to the number of buttons -1, representing the button selected. It will also set the widget data <i>exitType</i> to <i>vNORMAL</i>. If the character entered into this widget was <i>ESCAPE</i> then the widget will return a value of -1 and the widget data <i>exitType</i> will be set to <i>vESCAPE_HIT</i>.</p>
<dt><code>destroyCDKButtonbox</code></p>
<dd> removes the widget from the screen and releases any memory the object used.</p>
<dt><code>drawCDKButtonbox</code></p>
<dd> draws the buttonbox widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</p>
<dt><code>drawCDKButtonboxButtons</code></p>
<dd> draws the buttons.</p>
<dt><code>eraseCDKButtonbox</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKButtonboxBox</code></p>
<dd> returns true if the widget will be drawn with a box around it.</p>
<dt><code>getCDKButtonboxButtonCount</code></p>
<dd> returns the number of buttons in the button box.</p>
<dt><code>getCDKButtonboxCurrentButton</code></p>
<dd> returns the current button-number.</p>
<dt><code>getCDKButtonboxHighlight</code></p>
<dd> returns the highlight attribute of the widget.</p>
<dt><code>injectCDKButtonbox</code></p>
<dd> injects a single character into the widget. The parameter <code>buttonbox</code> is a pointer to a non-NULL buttonbox widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></p>
<dd> the function returns a value ranging from zero to one less than the number of buttons, representing the button selected. The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</p>
<dt><i>ESCAPE</i></p>
<dd> the function returns -1. <i>vESCAPE_HIT</i>. The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</p>
<dt>Otherwise</p>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns -1. The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dl>
</dl>
<dt><code>moveCDKButtonbox</code></p>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>newCDKButtonbox</code></p>
<dd> creates a pointer to a buttonbox widget. Parameters:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>screen</code></p>
<dd> is the screen you wish this widget to be placed in.</p>
<dt><code>xpos</code></p>
<dd> controls the placement of the object along the horizontal axis. It may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>.</p>
<dt><code>ypos</code></p>
<dd> controls the placement of the object along the vertical axis. It be an integer value or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</p>
<dt><code>height</code> and</p>
<dd>
<dt><code>width</code></p>
<dd> control the height and width of the widget.</p>
<dt><code>title</code></p>
<dd> is the title of the widget.</p>
<dt><code>rows</code></p>
<dd> is the number of rows of buttons.</p>
<dt><code>cols</code></p>
<dd> sets the number of columns.</p>
<dt><code>buttons</code></p>
<dd> is an array containing the button labels.</p>
<dt><code>buttonCount</code></p>
<dd> is the number of elements in the <code>buttons</code> array.</p>
<dt><code>highlight</code></p>
<dd> is the attribute of the currently highlighted button.</p>
<dt><code>box</code></p>
<dd> is true if the widget should be drawn with a box around it.</p>
<dt><code>shadow</code></p>
<dd> turns the shadow on or off around this widget.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKButtonbox</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>setCDKButtonbox</code></p>
<dd> lets the programmer modify certain elements of an existing buttonbox widget. The parameter names correspond to the same parameter names listed in the <code>newCDKButtonbox</code> function.</p>
<dt><code>setCDKButtonboxBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKButtonboxBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. (See <i>cdk_display</i>).</p>
<dt><code>setCDKButtonboxBox</code></p>
<dd> sets true if the widget will be drawn with a box around it.</p>
<dt><code>setCDKButtonboxBoxAttribute</code></p>
<dd> sets the attribute of the box.</p>
<dt><code>setCDKButtonboxCurrentButton</code></p>
<dd> sets the current button-number for the box.</p>
<dt><code>setCDKButtonboxHighlight</code></p>
<dd> sets the highlight attribute of the selected button.</p>
<dt><code>setCDKButtonboxHorizontalChar</code></p>
<dd> sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKButtonboxLLChar</code></p>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKButtonboxLRChar</code></p>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKButtonboxPostProcess</code></p>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. The parameter <code>function</code> is the callback function. (See <i>cdk_process</i>).</p>
<dt><code>setCDKButtonboxPreProcess</code></p>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. The parameter <code>function</code> is the callback function. (See <i>cdk_process</i>).</p>
<dt><code>setCDKButtonboxULChar</code></p>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKButtonboxURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKButtonboxVerticalChar</code></p>
<dd> sets the vertical drawing character for the box to the given character.</dl>
<h2>KEY BINDINGS</h2>
<p> When the widget is activated there are several default key bindings which will help the user enter or manipulate the information quickly. The following table outlines the keys and their actions for this widget. </p>
<p> <center></p>
<table BORDER>
<tr VALIGN=top>
<td><code>Key Action</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Left Arrow</td>
<td> Selects the button to the left of the current button.
</td>
</tr>
<tr VALIGN=top>
<td>Right Arrow</td>
<td> Selects the button to the right of the current button.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td> Selects the button to the right of the current button.
</td>
</tr>
<tr VALIGN=top>
<td>Space</td>
<td> Selects the button to the right of the current button.
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Exits the widget and returns the index of the selected button. This also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td> Exits the widget and returns the index of the selected button. This also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Escape</td>
<td> Exits the widget and returns -1. This also sets the widget data <i>exitType</i> to <i>vESCAPE_HIT</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-L</td>
<td> Refreshes the screen.
</td>
</tr>
</table>
<p></center></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_process/">cdk_process</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
