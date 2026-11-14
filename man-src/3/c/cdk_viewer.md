---
title: "cdk_viewer(3)"
name: "cdk_viewer"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_viewer/"
description: "cdk_viewer – curses viewer list widget."
---

<h2>NAME</h2>
<p> cdk_viewer &#8211; curses viewer list widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

int activateCDKViewer(
    CDKVIEWER *viewer);
void cleanCDKViewer(
    CDKVIEWER *viewer);
void destroyCDKViewer(
    CDKVIEWER *viewer);
void drawCDKViewer(
    CDKVIEWER *viewer,
    boolean box);
void eraseCDKViewer(
    CDKVIEWER *viewer);
boolean getCDKViewerBox(
    CDKVIEWER *viewer);
chtype getCDKViewerHighlight(
    CDKVIEWER *viewer);
chtype **getCDKViewerInfo(
    CDKVIEWER *viewer,
    char **itemList);
boolean getCDKViewerInfoLine(
    CDKVIEWER *viewer);
chtype **getCDKViewerTitle(
    CDKVIEWER *viewer);
void moveCDKViewer(
    CDKVIEWEE *viewer,
    int box,
    int box,
    boolean relative,
    boolean refresh);
CDKVIEWER *newCDKViewer(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    int height,
    int width,
    CDK_CONST char **buttonList,
    int buttonCount,
    chtype buttonHighlight,
    boolean box,
    boolean shadow);
void positionCDKViewer(
    CDKVIEWER *viewer);
void setCDKViewer(
    CDKVIEWER *viewer,
    const char *title,
    CDK_CONST char **list,
    int listSize,
    chtype buttonAttribute,
    boolean interpret,
    boolean showLineInfo,
    boolean box);
void setCDKViewerBackgroundAttrib(
    CDKVIEWER *viewer,
    chtype attribute);
void setCDKViewerBackgroundColor(
    CDKVIEWER *viewer,
    const char *color);
void setCDKViewerBox(
    CDKVIEWER *viewer,
    boolean Box);
void setCDKViewerBoxAttribute(
    CDKVIEWER *viewer,
    chtype character);
void setCDKViewerHighlight(
    CDKVIEWER *viewer,
    chtype highlight);
void setCDKViewerHorizontalChar(
    CDKVIEWER *viewer,
    chtype character);
void setCDKViewerInfo(
    CDKVIEWER *viewer,
    CDK_CONST char **list,
    int listSize,
    boolean interpret);
void setCDKViewerInfoLine(
    CDKVIEWER *viewer,
    boolean showInfoLine);
void setCDKViewerLLChar(
    CDKVIEWER *viewer,
    chtype character);
void setCDKViewerLRChar(
    CDKVIEWER *viewer,
    chtype character);
void setCDKViewerTitle(
    CDKVIEWER *viewer,
    const char *title);
void setCDKViewerULChar(
    CDKVIEWER *viewer,
    chtype character);
void setCDKViewerURChar(
    CDKVIEWER *viewer,
    chtype character);
void setCDKViewerVerticalChar(
    CDKVIEWER *viewer,
    chtype character);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk viewer widget creates a file viewer widget. This widget allows a user to interact with a file. It does <i>NOT</i> allow editing, this is view only. The following are functions which create or manipulate the Cdk viewer list widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKViewer</code></p>
<dd> activates the viewer widget and lets the user interact with the widget. The parameter <code>viewer</code> is a pointer to a non-NULL viewer widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> then this function will return a value from 0 to the number of buttons -1, representing the button selected. It will also set the widget data <i>exitType</i> to <i>vNORMAL</i>. If the character entered into this widget was <i>ESCAPE</i> then the widget will return a value of -1 and the widget data <i>exitType</i> will be set to <i>vESCAPE_HIT</i>.</p>
<dt><code>cleanCDKViewer</code></p>
<dd> clears the information from the window.</p>
<dt><code>destroyCDKViewer</code></p>
<dd> removes the widget from the screen and frees memory the object used.</p>
<dt><code>drawCDKViewer</code></p>
<dd> draws the viewer widget on the screen. If the <code>box</code> option is true, the widget is drawn with a box.</p>
<dt><code>eraseCDKViewer</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKViewerBox</code></p>
<dd> returns true if the widget will be drawn with a box around it.</p>
<dt><code>getCDKViewerHighlight</code></p>
<dd> returns the attribute of the buttons.</p>
<dt><code>getCDKViewerInfo</code></p>
<dd> returns the contents of the viewer widget.</p>
<dt><code>getCDKViewerInfoLine</code></p>
<dd> returns true if the information line is on.</p>
<dt><code>getCDKViewerTitle</code></p>
<dd> returns the title of the widget.</p>
<dt><code>moveCDKViewer</code></p>
<dd> function moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>*newCDKViewer</code></p>
<dd> function creates a viewer widget and returns a pointer to it. Parameters:</p>
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
<dd> are the height and width of the viewer window.</p>
<dt><code>buttons</code></p>
<dd> is an array of the button labels which are to be attached to the viewer on the bottom.</p>
<dt><code>buttonCount</code></p>
<dd> is the number of buttons in <code>buttons</code>.</p>
<dt><code>buttonHighlight</code></p>
<dd> is the highlight attribute of the currently selected button.</p>
<dt><code>box</code></p>
<dd> is true if the widget should be drawn with a box around it.</p>
<dt><code>shadow</code></p>
<dd> turns the shadow on or off around this widget.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKViewer</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>setCDKViewer</code></p>
<dd> lets the programmer modify several elements of an existing viewer widget. The parameter <code>title</code> is the title to be displayed on the top of the viewer.</p>
<dt>
<dd> The parameter <code>list</code> is the information to display, while <code>listSize</code> states how many rows there are in the <code>list</code> array. If <code>listSize</code> is negative, <code>list</code> is scanned to find its length, including files which will be included via embedded links.</p>
<dt>
<dd> The parameter <code>buttonAttribute</code> states the attribute of the current highlighted button. The boolean parameter <code>interpret</code> tells the viewer to interpret the contents of <code>list</code> for Cdk display command. The <code>showLineInfo</code> boolean flag tells the viewer to show to show the line number and percentage in the top left corner of the viewer window. The parameters <code>box</code> and <code>shadow</code> are the same as in the function description of <code>newCDKViewer</code>.</p>
<dt><code>setCDKViewerBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKViewerBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</p>
<dt><code>setCDKViewerBox</code></p>
<dd> sets whether the widget will be drawn with a box around it.</p>
<dt><code>setCDKViewerBoxAttribute</code></p>
<dd> sets the attribute of the box.</p>
<dt><code>setCDKViewerHighlight</code></p>
<dd> sets the highlight attribute of the buttons on the widget.</p>
<dt><code>setCDKViewerHorizontalChar</code></p>
<dd> sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKViewerInfo</code></p>
<dd> sets the contents of the viewer widget. See <code>setCDKViewer</code> for parameter descriptions.</p>
<dt><code>setCDKViewerInfoLine</code></p>
<dd> turns on/off the information line in the top left hand corner of the widget. If the value of <code>showInfoLine</code> is <i>TRUE</i>, the information line will be displayed. If it is <i>FALSE</i> it won&#8217;t.</p>
<dt><code>setCDKViewerLLChar</code></p>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKViewerLRChar</code></p>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKViewerTitle</code></p>
<dd> sets the title of the widget.</p>
<dt><code>setCDKViewerULChar</code></p>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKViewerURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKViewerVerticalChar</code></p>
<dd> sets the vertical drawing character for the box to the given character.</dl>
<h2>KEY BINDINGS</h2>
<p> When the widget is activated there are several default key bindings which will help the user enter or manipulate the information quickly. The following table outlines the keys and their actions for this widget. </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Key</code></td>
<td>Action
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
<td>Shifts the viewport one column left.
</td>
</tr>
<tr VALIGN=top>
<td>Right Arrow</td>
<td>Shifts the viewport one column left
</td>
</tr>
<tr VALIGN=top>
<td>Up Arrow</td>
<td>Scrolls the viewport one line up.
</td>
</tr>
<tr VALIGN=top>
<td>Down Arrow</td>
<td>Scrolls the viewport one line down.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Prev Page</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-B</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>B</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>b</td>
<td>Scroll one page backward.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Next Page</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-F</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Space</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>F</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>f</td>
<td>Scroll one page forward.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Home</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>|</td>
<td>Shift the whole list to the far left.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>End</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>$</td>
<td>Shift the whole list to the far right.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&lt;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>g</td>
<td>Moves to the first line in the viewer.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&gt;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>G</td>
<td>Moves to the last line in the viewer.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>L</td>
<td> Moves half the distance to the end of the viewer.
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td> Moves half the distance to the top of the viewer.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>?</td>
<td>Searches up for a pattern.
</td>
</tr>
<tr VALIGN=top>
<td>/</td>
<td>Searches down for a pattern.
</td>
</tr>
<tr VALIGN=top>
<td>n</td>
<td>Repeats last search.
</td>
</tr>
<tr VALIGN=top>
<td>N</td>
<td>Repeats last search, reversed direction.
</td>
</tr>
<tr VALIGN=top>
<td>:</td>
<td>Jumps to a given line.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>i</td>
<td>Displays file statistics.
</td>
</tr>
<tr VALIGN=top>
<td>s</td>
<td>Displays file statistics.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td>Switches buttons.
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Exit the widget and return the index of the selected button. Set the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Escape</td>
<td> Exit the widget and return -1. Set the widget data <i>exitType</i> to <i>vESCAPE_HIT</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-L</td>
<td>Refreshes the screen.
</td>
</tr>
</table>
</table>
<p></center></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
