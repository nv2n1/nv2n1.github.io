---
title: "cdk_scroll(3)"
name: "cdk_scroll"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_scroll/"
description: "cdk_scroll – curses scrolling list widget."
---

<h2>NAME</h2>
<p> cdk_scroll &#8211; curses scrolling list widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

int activateCDKScroll(
    CDKSCROLL *scroll,
    chtype *actions);
void addCDKScrollItem(
    CDKSCROLL *scroll,
    const char *item);
void deleteCDKScrollItem(
    CDKSCROLL *scroll,
    int position);
void destroyCDKScroll(
    CDKSCROLL *scroll);
void drawCDKScroll(
    CDKSCROLL *scroll,
    boolean box);
void eraseCDKScroll(
    CDKSCROLL *scroll);
boolean getCDKScrollBox(
    CDKSCROLL *scroll);
int getCDKScrollCurrent(
    CDKSCROLL *scroll);
int getCDKScrollCurrentItem(
    CDKSCROLL *widget);
chtype getCDKScrollHighlight(
    CDKSCROLL *scroll,
    chtype highlight);
int getCDKScrollCurrentTop(
    CDKSCROLL *widget);
int getCDKScrollItems(
    CDKSCROLL *scroll,
    char **itemList);
int injectCDKScroll(
    CDKSCROLL *scroll,
    chtype input);
void insertCDKScrollItem(
    CDKSCROLL *scroll,
    const char *item);
void moveCDKScroll(
    CDKSCROLL *scroll,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKSCROLL *newCDKScroll(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    int spos,
    int height,
    int width,
    const char *title,
    CDK_CONST char **itemList,
    int items,
    boolean numbers,
    chtype highlight,
    boolean box,
    boolean shadow);
void positionCDKScroll(
    CDKSCROLL *scroll);
void setCDKScroll(
    CDKSCROLL *scroll,
    CDK_CONST char **itemList,
    int items,
    boolean numbers,
    chtype highlight,
    boolean box);
void setCDKScrollBackgroundAttrib(
    CDKSCROLL *scroll,
    chtype attribute);
void setCDKScrollBackgroundColor(
    CDKSCROLL *scroll,
    const char *color);
void setCDKScrollBox(
    CDKSCROLL *scroll,
    boolean box);
void setCDKScrollBoxAttribute(
    CDKSCROLL *scroll,
    chtype character);
void setCDKScrollCurrent(
    CDKSCROLL *scroll,
    intitem);
void setCDKScrollCurrentItem(
    CDKSCROLL *widget,
    intitem);
int getCDKScrollCurrentTop(
    CDKSCROLL *widget);
void setCDKScrollHighlight(
    CDKSCROLL *scroll,
    chtype highlight);
void setCDKScrollHorizontalChar(
    CDKSCROLL *scroll,
    chtype character);
void setCDKScrollItems(
    CDKSCROLL *scroll,
    CDK_CONST char **itemList,
    int listSize,
    boolean numbers);
void setCDKScrollLLChar(
    CDKSCROLL *scroll,
    chtype character);
void setCDKScrollLRChar(
    CDKSCROLL *scroll,
    chtype character);
void setCDKScrollPosition(
    CDKSCROLL *scroll,
    intitem);
void setCDKScrollPostProcess(
    CDKSCROLL *scroll,
    PROCESSFN callback,
    void *data);
void setCDKScrollPreProcess(
    CDKSCROLL *scroll,
    PROCESSFN callback,
    void *data);
void setCDKScrollULChar(
    CDKSCROLL *scroll,
    chtype character);
void setCDKScrollURChar(
    CDKSCROLL *scroll,
    chtype character);
void setCDKScrollVerticalChar(
    CDKSCROLL *scroll,
    chtype character);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk scroll widget creates a scrolling list. The following are functions which create or manipulate the Cdk scrolling list widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKScroll</code></p>
<dd> activates the scroll widget and lets the user interact with the widget. The parameter <code>scroll</code> points to a non-NULL scroll widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> or <i>TAB</i> then this function will return a value from 0 to the number of items-1, representing the item selected. It will also set the widget data <i>exitType</i> to <i>vNORMAL</i>. If the character entered into this widget was <i>ESCAPE</i> then the widget will return a value of -1 and the widget data <i>exitType</i> will be set to <i>vESCAPE_HIT</i>.</p>
<dt><code>addCDKScrollItem</code></p>
<dd> allows the user to add an item into an existing scrolling list. The <code>scroll</code> parameter points to the scrolling list to add the item to. The parameter <code>item</code> is a <i>char *</i> representing the new item to add. The item is always added to the end of the list.</p>
<dt><code>deleteCDKScrollItem</code></p>
<dd> allows the user to add an item into an existing scrolling list. The <code>scroll</code> parameter points to the scrolling list to add the item to. The parameter <code>f2position</code> is an <i>int</i> which specifies which element to remove.</p>
<dt><code>destroyCDKScroll</code></p>
<dd> removes the widget from the screen and frees memory the object used.</p>
<dt><code>drawCDKScroll</code></p>
<dd> draws the scroll widget on the screen. If the <code>box</code> option is true, the widget is drawn with a box.</p>
<dt><code>eraseCDKScroll</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKScrollBox</code></p>
<dd> returns true if the widget will be drawn with a box around it.</p>
<dt><code>getCDKScrollCurrent</code></p>
<dd> returns the current item&#8217;s index.</p>
<dt><code>getCDKScrollCurrentItem</code></p>
<dd> returns the current item number in the scroller.</p>
<dt><code>getCDKScrollHighlight</code></p>
<dd> returns the attribute of the highlight bar.</p>
<dt><code>getCDKScrollCurrentTop</code></p>
<dd> returns the top line of the scroller, counting from zero.</p>
<dt><code>getCDKScrollItems</code></p>
<dd> fills the parameter <code>itemList</code> with the contents of the scrolling list. It returns the number of elements in the scrolling list.</p>
<dt><code>injectCDKScroll</code></p>
<dd> injects a single character into the widget. The parameter <code>scroll</code> points to a non-NULL scroll widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></p>
<dd> the function returns a value ranging from zero to one less than the number of items, representing the item selected. The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</p>
<dt><i>ESCAPE</i></p>
<dd> the function returns -1. The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</p>
<dt>Otherwise</p>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns -1. The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dl>
</dl>
<dt><code>insertCDKScrollItem</code></p>
<dd> allows the user to add an item into an existing scrolling list. The <code>scroll</code> parameter points to the scrolling list to add the item to. The parameter <code>item</code> is a <i>char *</i> representing the new item to add. The item is always added before the current item in the list.</p>
<dt><code>moveCDKScroll</code></p>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>newCDKScroll</code></p>
<dd> creates a scroll widget and returns a pointer to it. Parameters:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>screen</code></p>
<dd> parameter is the screen you wish this widget to be placed in. The parameter <code>xpos</code> controls the placement of the object along the horizontal axis. This parameter may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>.</p>
<dt><code>ypos</code></p>
<dd> controls the placement of the object along the vertical axis. This parameter may be an integer value or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</p>
<dt><code>spos</code></p>
<dd> is where the scroll bar is to be placed. This may be one of three values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>LEFT</i>,</p>
<dd> which puts the scroll bar on the left of the scrolling list.</p>
<dt><i>RIGHT</i></p>
<dd> which puts the scroll bar on the right side of the list, and</p>
<dt><i>NONE</i> which does not add a scroll bar.</p>
<dd></dl>
</dl>
<dt><code>height</code> and</p>
<dd>
<dt><code>width</code></p>
<dd> control the height and width of the widget. If you provide a value of zero for either of the height or the width, the widget will be created with the full width and height of the screen. If you provide a negative value, the widget will be created the full height or width minus the value provided.</p>
<dt><code>title</code></p>
<dd> is the string which will be displayed at the top of the widget. The title can be more than one line; just provide a carriage return character at the line break.</p>
<dt><code>itemList</code></p>
<dd> is the list of items to be displayed in the scrolling list.</p>
<dt><code>items</code></p>
<dd> is the number of elements in the given list.</p>
<dt><code>numbers</code></p>
<dd> is true if you want the items in the list to have a number attached to the front of the list items.</p>
<dt><code>highlight</code></p>
<dd> specifies the display attribute of the currently selected item.</p>
<dt><code>box</code></p>
<dd> is true if the widget should be drawn with a box around it.</p>
<dt><code>shadow</code></p>
<dd> is true to turn the shadow on around this widget.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKScroll</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>setCDKScroll</code></p>
<dd> lets the programmer modify certain elements of an existing scroll widget. The parameter names correspond to the same parameter names listed in the <code>newCDKScroll</code> function.</p>
<dt><code>setCDKScrollBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKScrollBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</p>
<dt><code>setCDKScrollBox</code></p>
<dd> sets whether the widget will be drawn with a box around it.</p>
<dt><code>setCDKScrollBoxAttribute</code></p>
<dd> sets the attribute of the box.</p>
<dt><code>setCDKScrollCurrent</code></p>
<dd> sets the index for the current item.</p>
<dt><code>setCDKScrollCurrentItem</code></p>
<dd> set the current item number in the scroller.</p>
<dt><code>setCDKScrollCurrentTop</code></p>
<dd> set the top line number of the scroller.</p>
<dt><code>setCDKScrollHighlight</code></p>
<dd> sets the attribute of the highlight bar.</p>
<dt><code>setCDKScrollHorizontalChar</code></p>
<dd> sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKScrollItems</code></p>
<dd> sets the contents of the scrolling list.</p>
<dt><code>setCDKScrollLLChar</code></p>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKScrollLRChar</code></p>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKScrollPosition</code></p>
<dd> sets the current item in the widget to the given position.</p>
<dt><code>setCDKScrollPostProcess</code></p>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about post-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKScrollPreProcess</code></p>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about pre-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKScrollULChar</code></p>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKScrollURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKScrollVerticalChar</code></p>
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
<td>Shift the list left one column.
</td>
</tr>
<tr VALIGN=top>
<td>Right Arrow</td>
<td>Shift the list right one column.
</td>
</tr>
<tr VALIGN=top>
<td>Up Arrow</td>
<td>Select the previous item in the list.
</td>
</tr>
<tr VALIGN=top>
<td>Down Arrow</td>
<td>Select the next item in the list.
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
<td>Shift the list to the far right.
</td>
</tr>
<tr VALIGN=top>
<td>|</td>
<td>Shift the list to the far left.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Exit the widget and return the index of the selected item. Also set the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td> Exit the widget and return the index of the selected item. Also set the widget data <i>exitType</i> to <i>vNORMAL</i>.
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
