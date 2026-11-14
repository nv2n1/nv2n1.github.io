---
title: "cdk_itemlist(3)"
name: "cdk_itemlist"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_itemlist/"
description: "cdk_itemlist – curses itemlist widget."
---

<h2>NAME</h2>
<p> cdk_itemlist &#8211; curses itemlist widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

int activateCDKItemlist(
    CDKITEMLIST *itemlist,
    chtype *actions);
void destroyCDKItemlist(
    CDKITEMLIST *itemlist);
void drawCDKItemlist(
    CDKITEMLIST *itemlist,
    boolean box);
void drawCDKItemlistField(
    CDKITEMLIST *itemlist,
    boolean highlight);
void eraseCDKItemlist(
    CDKITEMLIST *itemlist);
boolean getCDKItemlistBox(
    CDKITEMLIST *itemlist);
int getCDKItemlistCurrentItem(
    CDKITEMLIST *itemlist);
int getCDKItemlistDefaultItem(
    CDKITEMLIST *itemlist);
chtype **getCDKItemlistValues(
    CDKITEMLIST *itemlist,
    int *listSize);
int injectCDKItemlist(
    CDKITEMLIST *itemlist,
    chtype input);
void moveCDKItemlist(
    CDKITEMLIST *itemlist,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKITEMLIST *newCDKItemlist(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    const char *title,
    const char *label,
    CDK_CONST char **itemList,
    int itemCount,
    int defaultItem,
    boolean box,
    boolean shadow);
void positionCDKItemlist(
    CDKITEMLIST *itemlist);
void setCDKItemlist(
    CDKITEMLIST *itemlist,
    CDK_CONST char **itemList,
    int itemCount,
    int currentSelection,
    boolean box);
void setCDKItemlistBackgroundAttrib(
    CDKITEMLIST *itemlist,
    chtypeattribute);
void setCDKItemlistBackgroundColor(
    CDKITEMLIST *itemlist,
    const char *color);
void setCDKItemlistBox(
    CDKITEMLIST *itemlist,
    boolean box);
void setCDKItemlistBoxAttribute(
    CDKITEMLIST *itemlist,
    chtype character);
void setCDKItemlistCurrentItem(
    CDKITEMLIST *itemlist,
    int currentItem);
void setCDKItemlistDefaultItem(
    CDKITEMLIST *itemlist,
    int defaultItem);
void setCDKItemlistHorizontalChar(
    CDKITEMLIST *itemlist,
    chtype character);
void setCDKItemlistLLChar(
    CDKITEMLIST *itemlist,
    chtype character);
void setCDKItemlistLRChar(
    CDKITEMLIST *itemlist,
    chtype character);
void setCDKItemlistPostProcess(
    CDKITEMLIST *itemlist,
    PROCESSFN callback,
    void *data);
void setCDKItemlistPreProcess(
    CDKITEMLIST *itemlist,
    PROCESSFN callback,
    void *data);
void setCDKItemlistULChar(
    CDKITEMLIST *itemlist,
    chtype character);
void setCDKItemlistURChar(
    CDKITEMLIST *itemlist,
    chtype character);
void setCDKItemlistValues(
    CDKITEMLIST *itemlist,
    CDK_CONST char **itemList,
    int itemCount);
void setCDKItemlistVerticalChar(
    CDKITEMLIST *itemlist,
    chtype character);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk itemlist widget creates a widget which allows a user to select from a list of preset character strings such as the days of the week or the months of the year. The following functions create or manipulate the Cdk itemlist widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKItemlist</code></p>
<dd> activates the itemlist widget and lets the user interact with the widget. The parameter <code>itemlist</code> is a pointer to a non-NULL itemlist widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> or <i>TAB</i> then this function will return a value from 0 to the number of buttons -1, representing the button selected. It will also set the widget data <i>exitType</i> to <i>vNORMAL</i>. If the character entered into this widget was <i>ESCAPE</i> then the widget will return a -1 and the widget data <i>exitType</i> will be set to <i>vESCAPE_HIT</i>.</p>
<dt><code>destroyCDKItemlist</code></p>
<dd> removes the widget from the screen and frees memory the object used.</p>
<dt><code>drawCDKItemlist</code></p>
<dd> draws the itemlist widget on the screen. The <code>box</code> option is true if the widget is drawn with a box.</p>
<dt><code>drawCDKItemlistField</code></p>
<dd> draws the contents of the field.</p>
<dt><code>eraseCDKItemlist</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKItemlistBox</code></p>
<dd> returns true if the widget will be drawn with a box around it.</p>
<dt><code>getCDKItemlistCurrentItem</code></p>
<dd> returns the index of the currently displayed item in the widget.</p>
<dt><code>getCDKItemlistDefaultItem</code></p>
<dd> returns the index of the default item in the widget.</p>
<dt><code>getCDKItemlistValues</code></p>
<dd> returns the list of pointers to the items. The parameter <code>size</code> points to a location which receives the item count.</p>
<dt><code>injectCDKItemlist</code></p>
<dd> injects a single character into the widget. The parameter <code>itemlist</code> is a pointer to a non-NULL itemlist widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></p>
<dd> the function returns a value ranging from zero to one less than the number of buttons, representing the button selected. The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</p>
<dt><i>ESCAPE</i></p>
<dd> the function returns -1. The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</p>
<dt>Otherwise</p>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns -1. The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dl>
</dl>
<dt><code>moveCDKItemlist</code></p>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>newCDKItemlist</code></p>
<dd> creates a pointer to an itemlist widget. Parameters:</p>
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
<dt><code>title</code></p>
<dd> is the string which will be displayed at the top of the widget. The title can be more than one line; just provide a carriage return character at the line break.</p>
<dt><code>label</code></p>
<dd> is the string to use as the label of the itemlist field.</p>
<dt><code>itemList</code></p>
<dd> is the list of the strings which will be displayed in the widget.</p>
<dt><code>itemCount</code></p>
<dd> is the number of elements in the list.</p>
<dt><code>defaultItem</code></p>
<dd> is the index of the default item for the list.</p>
<dt><code>box</code></p>
<dd> is true if widget should be drawn with a box around it.</p>
<dt><code>shadow</code></p>
<dd> turns the shadow on or off around this widget.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKItemlist</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>setCDKItemlist</code></p>
<dd> lets the programmer modify certain elements of an existing itemlist widget. The parameter names correspond to the same parameter names listed in the <code>newCDKItemlist</code> function.</p>
<dt><code>setCDKItemlistBackgroundAttrib</code></p>
<dd> the background color attribute the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKItemlistBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</p>
<dt><code>setCDKItemlistBox</code></p>
<dd> sets whether the widget will be drawn with a box around it.</p>
<dt><code>setCDKItemlistBoxAttribute</code></p>
<dd> sets the attribute of the box.</p>
<dt><code>setCDKItemlistCurrentItem</code></p>
<dd> sets the currently displayed item in the widget.</p>
<dt><code>setCDKItemlistDefaultItem</code></p>
<dd> sets the default item in the widget.</p>
<dt><code>setCDKItemlistHorizontalChar</code></p>
<dd> sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKItemlistLLChar</code></p>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKItemlistLRChar</code></p>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKItemlistPostProcess</code></p>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about post-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKItemlistPreProcess</code></p>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about pre-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKItemlistULChar</code></p>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKItemlistURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKItemlistValues</code></p>
<dd> sets the contents of the list from an array of string pointers <code>item</code> whose final index is given by <code>count</code>. If <code>defaultItem</code> is in the range 0..<code>count</code>, that sets the default item value for the list.</p>
<dt><code>setCDKItemlistVerticalChar</code></p>
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
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Down Arrow</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>p</td>
<td>Shift the list one column to the left.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Right Arrow</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Up Arrow</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Space</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>+</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>n</td>
<td>Shift the list one column to the right.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>d</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>D</td>
<td>Display the default item.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>Display the first item in the list.
</td>
</tr>
<tr VALIGN=top>
<td>$</td>
<td>Display the last item in the list.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Exit the widget and return an integer representing the current selection. Also set the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td> Exit the widget and return an integer representing the current selection. Also set the widget data <i>exitType</i> to <i>vNORMAL</i>.
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
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_process/">cdk_process</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
