---
title: "cdk_selection(3)"
name: "cdk_selection"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_selection/"
description: "cdk_selection – curses selection list widget."
---

<h2>NAME</h2>
<p> cdk_selection &#8211; curses selection list widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

int activateCDKSelection(
    CDKSELECTION *selection,
    chtype *actions);
void destroyCDKSelection(
    CDKSELECTION *selection);
void drawCDKSelection(
    CDKSELECTION *selection,
    boolean box);
void eraseCDKSelection(
    CDKSELECTION *selection);
boolean getCDKSelectionBox(
    CDKSELECTION *selection);
int getCDKSelectionChoice(
    CDKSELECTION *selection,
    int index);
int *getCDKSelectionChoices(
    CDKSELECTION *selection);
int getCDKSelectionCurrent(
    CDKSELECTION *selection);
chtype getCDKSelectionHighlight(
    CDKSELECTION *selection);
int getCDKSelectionItems(
    CDKSELECTION *selection,
    char **list);
int getCDKSelectionMode(
    CDKSELECTION *selection,
    int index);
int *getCDKSelectionModes(
    CDKSELECTION *selection);
char *getCDKSelectionTitle(
    CDKSELECTION *selection);
int injectCDKSelection(
    CDKSELECTION *selection,
    chtype input);
void moveCDKSelection(
    CDKSELECTION *selection,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKSELECTION *newCDKSelection(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    int spos,
    int height,
    int width,
    const char *title,
    CDK_CONST char **selectionList,
    int selectionListLength,
    CDK_CONST char **choiceList,
    int choiceListLength,
    chtype highlight,
    boolean box,
    boolean shadow);
void positionCDKSelection(
    CDKSELECTION *selection);
void setCDKSelection(
    CDKSELECTION *selection,
    chtype highlight,
    int *defChoices,
    boolean box);
void setCDKSelectionBackgroundAttrib(
    CDKSELECTION *selection,
    chtype attribute);
void setCDKSelectionBackgroundColor(
    CDKSELECTION *selection,
    const char *color);
void setCDKSelectionBox(
    CDKSELECTION *selection,
    boolean boxWidget);
void setCDKSelectionBoxAttribute(
    CDKSELECTION *selection,
    chtype character);
void setCDKSelectionChoice(
    CDKSELECTION *selection,
    int index,
    int choice);
void setCDKSelectionChoices(
    CDKSELECTION *selection,
    int *choices);
void setCDKSelectionCurrent(
    CDKSELECTION *selection,
    intindex);
void setCDKSelectionHighlight(
    CDKSELECTION *selection,
    chtype highlight);
void setCDKSelectionHorizontalChar(
    CDKSELECTION *selection,
    chtype character);
void setCDKSelectionItems(
    CDKSELECTION *selection,
    CDK_CONST char **list,
    int listSize);
void setCDKSelectionLLChar(
    CDKSELECTION *selection,
    chtype character);
void setCDKSelectionLRChar(
    CDKSELECTION *selection,
    chtype character);
void setCDKSelectionMode(
    CDKSELECTION *selection,
    int index,
    int mode);
void setCDKSelectionModes(
    CDKSELECTION *selection,
    int *modes);
void setCDKSelectionPostProcess(
    CDKSELECTION *selection,
    PROCESSFN callback,
    void *data);
void setCDKSelectionPreProcess(
    CDKSELECTION *selection,
    PROCESSFN callback,
    void *data);
void setCDKSelectionTitle(
    CDKSELECTION *selection,
    const char *title);
void setCDKSelectionULChar(
    CDKSELECTION *selection,
    chtype character);
void setCDKSelectionURChar(
    CDKSELECTION *selection,
    chtype character);
void setCDKSelectionVerticalChar(
    CDKSELECTION *selection,
    chtype character);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk selection widget creates a selection list. The following functions create or manipulate the Cdk selection list widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKSelection</code></p>
<dd> activates the selection widget and lets the user interact with the widget. The parameter <code>selection</code> is a pointer to a non-NULL selection widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> or <i>TAB</i> then this function will return 1. Itm will also set the widget data <i>exitType</i> to <i>vNORMAL</i>. If the character entered into this widget was <i>ESCAPE</i> then the widget will return a value of -1 and the widget data <i>exitType</i> will be set to <i>vESCAPE_HIT</i>.</p>
<dt><code>destroyCDKSelection</code></p>
<dd> removes the widget from the screen and frees memory the object used.</p>
<dt><code>drawCDKSelection</code></p>
<dd> draws the selection widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</p>
<dt><code>eraseCDKSelection</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKSelectionBox</code></p>
<dd> returns true if the widget will be drawn with a box around it.</p>
<dt><code>getCDKSelectionChoice</code></p>
<dd> returns the selection choice at the given index.</p>
<dt><code>getCDKSelectionChoices</code></p>
<dd> returns an array of the current selection choices for the widget.</p>
<dt><code>getCDKSelectionCurrent </code></p>
<dd> returns the current selection index.</p>
<dt><code>getCDKSelectionHighlight</code></p>
<dd> returns the attribute of the highlight bar.</p>
<dt><code>getCDKSelectionItems</code></p>
<dd> copies the selection-list items into the caller&#8217;s array and returns the number of items in the list.</p>
<dt><code>getCDKSelectionMode</code></p>
<dd> returns the selection mode at the given index.</p>
<dt><code>getCDKSelectionModes</code></p>
<dd> returns an array of the current modes for the widget.</p>
<dt><code>getCDKSelectionTitle</code></p>
<dd> returns the first line of the title of the selection widget. The caller must free the returned value.</p>
<dt><code>injectCDKSelection</code></p>
<dd> injects a single character into the widget. The parameter <code>selection</code> is a pointer to a non-NULL selection widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></p>
<dd> the function returns 1. The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</p>
<dt><i>ESCAPE</i></p>
<dd> the function returns -1. <i>vESCAPE_HIT</i>. The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</p>
<dt>Otherwise</p>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns -1. The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dl>
</dl>
<dt><code>moveCDKSelection</code></p>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>newCDKSelection</code></p>
<dd> creates a selection widget and returns a pointer to it. Parameters:</p>
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
<dt><code>spos</code></p>
<dd> is where the scroll bar is to be placed. It may be one of three values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>LEFT</i></p>
<dd> puts the scroll bar on the left of the scrolling list. <i>RIGHT</i> puts the scroll bar on the right side of the list, and</p>
<dt><i>NONE</i></p>
<dd> does not add a scroll bar.</dl>
</dl>
<dt><code>height</code> and</p>
<dd>
<dt><code>width</code></p>
<dd> control the height and width of the widget. If you provide a value of zero for either of the height or the width, the widget will be created with the full width and height of the screen. If you provide a negative value, the widget will be created the full height or width minus the value provided.</p>
<dt><code>title</code></p>
<dd> is the string which to display at the top of the widget. The title can be more than one line; just provide a carriage return character at the line break.</p>
<dt><code>selectionList</code></p>
<dd> is the list of items to display in the selection list</p>
<dt><code>selectionListLength</code></p>
<dd> is the number of elements in the given list.</p>
<dt><code>choiceList</code></p>
<dd> is the list of choices that will be selected when the user presses the space bar.</p>
<dt><code>choiceListLength</code></p>
<dd> is the length of this list.</p>
<dt><code>highlight</code></p>
<dd> specifies the display attribute of the currently selected item.</p>
<dt><code>box</code></p>
<dd> is true if the widget should be drawn with a box around it.</p>
<dt><code>shadow</code></p>
<dd> turns the shadow on or off around this widget.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKSelection</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>setCDKSelection</code></p>
<dd> lets the programmer modify certain elements of an existing selection widget. The parameter names correspond to the same parameter names listed in the <code>newCDKSelection</code> function.</p>
<dt><code>setCDKSelectionBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKSelectionBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</p>
<dt><code>setCDKSelectionBox</code></p>
<dd> sets whether the widget will be drawn with a box around it.</p>
<dt><code>setCDKSelectionBoxAttribute</code></p>
<dd> sets the attribute of the box.</p>
<dt><code>setCDKSelectionChoice</code></p>
<dd> sets the selection choice value at the given index.</p>
<dt><code>setCDKSelectionChoices</code></p>
<dd> sets the selection choice values of the widget.</p>
<dt><code>setCDKSelectionCurrent </code></p>
<dd> sets the current selection index.</p>
<dt><code>setCDKSelectionHighlight</code></p>
<dd> sets the attribute of the highlight bar.</p>
<dt><code>setCDKSelectionHorizontalChar</code></p>
<dd> sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKSelectionItems</code></p>
<dd> sets the selection list items.</p>
<dt><code>setCDKSelectionLLChar</code></p>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKSelectionLRChar</code></p>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKSelectionMode</code></p>
<dd> sets the selection mode at the given index.</p>
<dt><code>setCDKSelectionModes</code></p>
<dd> sets the selection mode of the elements of the widget. There are two acceptable values for the modes: 0 which allows the user to change the selection value at the given index; and 1 which sets the element to a read-only state.</p>
<dt><code>setCDKSelectionPostProcess</code></p>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about post-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKSelectionPreProcess</code></p>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> is a pointer to <i>void</i>. To learn more about pre-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKSelectionTitle</code></p>
<dd> set the selection list&#8217;s title.</p>
<dt><code>setCDKSelectionULChar</code></p>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKSelectionURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKSelectionVerticalChar</code></p>
<dd> sets the vertical drawing character for the box to the given character.</dl>
<h2>KEY BINDINGS</h2>
<p> When the widget is activated there are several default key bindings which help the user enter or manipulate the information quickly: </p>
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
<td> Shift the whole list left one column.
</td>
</tr>
<tr VALIGN=top>
<td>Right Arrow</td>
<td> Shift the whole list right one column.
</td>
</tr>
<tr VALIGN=top>
<td>Up Arrow</td>
<td> Select the previous item in the list.
</td>
</tr>
<tr VALIGN=top>
<td>Down Arrow</td>
<td> Select the next item in the list.
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
<td>Scroll one page forward.
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
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Home</td>
<td>Move to the first element in the list.
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
<td>
</td>
</tr>
<tr VALIGN=top>
<td>End</td>
<td>Move to the last element in the list.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>$</td>
<td>Shift the whole list to the far right.
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
<td>Space</td>
<td> Cycles to the next choice on the current item.
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Exit the widget and return 1. Also set the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td> Exit the widget and return 1. Also set the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Escape</td>
<td> Exit the widget and return -1. Also set the widget data <i>exitType</i> to <i>vESCAPE_HIT</i>.
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
