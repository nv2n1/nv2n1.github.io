---
title: "cdk_radio(3)"
name: "cdk_radio"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_radio/"
description: "cdk_radio – curses radio list widget."
---

<h2>NAME</h2>
<p> cdk_radio &#8211; curses radio list widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>
int activateCDKRadio(
    CDKRADIO *radio,
    chtype *actions);
void destroyCDKRadio(
    CDKRADIO *radio);
void drawCDKRadio(
    CDKRADIO *radio,
    boolean box);
void eraseCDKRadio(
    CDKRADIO *radio);
boolean getCDKRadioBox(
    CDKRADIO *radio);
chtype getCDKRadioChoiceCharacter(
    CDKRADIO *radio);
int getCDKRadioCurrentItem(
    CDKRADIO *radio);
chtype getCDKRadioHighlight(
    CDKRADIO *radio);
int getCDKRadioItems(
    CDKRADIO *radio,
    char **list);
chtype getCDKRadioLeftBrace(
    CDKRADIO *radio);
chtype getCDKRadioRightBrace(
    CDKRADIO *radio);
int getCDKRadioSelectedItem(
    CDKRADIO *radio);
int injectCDKRadio(
    CDKRADIO *radio,
    chtype input);
void moveCDKRadio(
    CDKRADIO *radio,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKRADIO *newCDKRadio(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    int spos,
    int height,
    int width,
    const char *title,
    CDK_CONST char **radioList,
    int radioListLength,
    chtype choiceCharacter,
    int defaultItem,
    chtype highlight,
    boolean box,
    boolean shadow);
void positionCDKRadio(
    CDKRADIO *radio);
void setCDKRadio(
    CDKRADIO *radio,
    chtype highlight,
    chtype choiceCharacter,
    boolean box);
void setCDKRadioBackgroundAttrib(
    CDKRADIO *radio,
    chtype attribute);
void setCDKRadioBackgroundColor(
    CDKRADIO *radio,
    const char *color);
void setCDKRadioBox(
    CDKRADIO *radio,
    boolean box);
void setCDKRadioBoxAttribute(
    CDKRADIO *radio,
    chtype character);
void setCDKRadioChoiceCharacter(
    CDKRADIO *radio,
    chtype character);
void setCDKRadioCurrentItem(
    CDKRADIO *radio,
    intindex);
void setCDKRadioHighlight(
    CDKRADIO *radio,
    chtype highlight);
void setCDKRadioHorizontalChar(
    CDKRADIO *radio,
    chtype character);
void setCDKRadioItems(
    CDKRADIO *radio,
    CDK_CONST char **list,
    int listSize);
void setCDKRadioLLChar(
    CDKRADIO *radio,
    chtype character);
void setCDKRadioLRChar(
    CDKRADIO *radio,
    chtype character);
void setCDKRadioLeftBrace(
    CDKRADIO *radio,
    chtype character);
void setCDKRadioPostProcess(
    CDKRADIO *radio,
    PROCESSFN callback,
    void *data);
void setCDKRadioPreProcess(
    CDKRADIO *radio,
    PROCESSFN callback,
    void *data);
void setCDKRadioRightBrace(
    CDKRADIO *radio,
    chtype character);
void setCDKRadioSelectedItem(
    CDKRADIO *radio,
    int item);
void setCDKRadioULChar(
    CDKRADIO *radio,
    chtype character);
void setCDKRadioURChar(
    CDKRADIO *radio,
    chtype character);
void setCDKRadioVerticalChar(
    CDKRADIO *radio,
    chtype character);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk radio widget creates a radio list. The following are functions which create or manipulate the Cdk radio box widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKRadio</code></dt>
<dd> activates the radio widget and lets the user interact with the widget. The parameter <code>radio</code> is a pointer to a non-NULL radio widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> or <i>TAB</i> then this function will return a value from 0 to the number of items -1, representing the item selected. It will also set the widget data <i>exitType</i> to <i>vNORMAL</i>. If the character entered into this widget was <i>ESCAPE</i> then the widget will return a value of -1 and the widget data <i>exitType</i> will be set to <i>vESCAPE_HIT</i>.</dd>
<dt><code>destroyCDKRadio</code></dt>
<dd> removes the widget from the screen and frees memory the object used.</dd>
<dt><code>drawCDKRadio</code></dt>
<dd> draws the radio widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</dd>
<dt><code>eraseCDKRadio</code></dt>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</dd>
<dt><code>getCDKRadioBox</code></dt>
<dd> returns true if the widget will be drawn with a box around it.</dd>
<dt><code>getCDKRadioChoiceCharacter</code></dt>
<dd> returns the character being used to draw the selected element in the list.</dd>
<dt><code>getCDKRadioCurrentItem </code></dt>
<dd> returns the index of the current item.</dd>
<dt><code>getCDKRadioHighlight</code></dt>
<dd> returns the attribute of the highlight bar.</dd>
<dt><code>getCDKRadioItems</code></dt>
<dd> copies the radio box items into the caller&#8217;s list, which must be large enough since this function does not allocate it. It returns the list size.</dd>
<dt><code>getCDKRadioLeftBrace</code></dt>
<dd> returns the character being used to draw the left brace of the selection box.</dd>
<dt><code>getCDKRadioRightBrace</code></dt>
<dd> returns the character being used to draw the right brace of the selection box.</dd>
<dt><code>getCDKRadioSelectedItem,</code></dt>
<dd> returns the selected item of the widget.</dd>
<dt><code>injectCDKRadio</code></dt>
<dd> function injects a single character into the widget. The parameter <code>radio</code> is a pointer to a non-NULL radio widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</dd>
<dl>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></dt>
<dd> the function returns a value ranging from zero to one less than the number of items, representing the items selected. The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</dd>
<dt><i>ESCAPE</i></dt>
<dd> the function returns -1. The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</dd>
<dt>Otherwise</dt>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns -1. The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dd></dl>
</dl>
<dt><code>moveCDKRadio</code></dt>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</dd>
<dt><code>newCDKRadio</code></dt>
<dd> creates a radio widget and returns a pointer to it. Parameters:</dd>
<dl>
<dl>
<dt><code>screen</code></dt>
<dd> is the screen you wish this widget to be placed in.</dd>
<dt><code>xpos</code></dt>
<dd> controls the placement of the object along the horizontal axis. It may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>.</dd>
<dt><code>ypos</code></dt>
<dd> controls the placement of the object along the vertical axis. It may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</dd>
<dt><code>spos</code></dt>
<dd> tells where the scroll bar is to be placed. This may be one of three values:</dd>
<dl>
<dl>
<dt><i>LEFT</i></dt>
<dd> puts the scroll bar on the left of the scrolling list.</dd>
<dt><i>RIGHT</i></dt>
<dd> puts the scroll bar on the right side of the list, and</dd>
<dt><i>NONE</i></dt>
<dd> does not add a scroll bar.</dd></dl>
</dl>
<dt><code>height</code> and</dt>
<dd> <code>width</code> control the height and width of the widget. If you provide a value of zero for either of the height or the width, the widget will be created with the full width and height of the screen. If you provide a negative value, the widget will be created the full height or width minus the value provided.</dd>
<dt><code>title</code></dt>
<dd> is the string which will be displayed at the top of the widget. The title can be more than one line; just provide a carriage return character at the line break.</dd>
<dt><code>radioList</code></dt>
<dd> is the list of items to display in the radio list.</dd>
<dt><code>radioListLength</code></dt>
<dd> is the number of elements in the given list.</dd>
<dt><code>choiceCharacter</code></dt>
<dd> is the character to use to highlight the current selection.</dd>
<dt><code>highlight</code></dt>
<dd> specifies the display attribute of the currently selected item.</dd>
<dt><code>defaultItem</code></dt>
<dd> is the index in the list of the default selection.</dd>
<dt><code>box</code></dt>
<dd> is true if widget should be drawn with a box around it.</dd>
<dt><code>shadow</code></dt>
<dd> turns the shadow on or off around this widget.</dd></dl>
</dl>
<dt>
</dt><dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</dd>
<dt><code>positionCDKRadio</code></dt>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See cdk_position (3) for key bindings.</dd>
<dt><code>setCDKRadio</code></dt>
<dd> lets the programmer modify certain elements of an existing radio widget. The parameter names correspond to the same parameter names listed in the <code>newCDKRadio</code> function.</dd>
<dt><code>setCDKRadioBackgroundAttrib</code></dt>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</dd>
<dt><code>setCDKRadioBackgroundColor</code></dt>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</dd>
<dt><code>setCDKRadioBox</code></dt>
<dd> sets whether the widget will be drawn with a box around it.</dd>
<dt><code>setCDKRadioBoxAttribute</code></dt>
<dd> function sets the attribute of the box.</dd>
<dt><code>setCDKRadioChoiceCharacter</code></dt>
<dd> sets the character to use to draw the selected element in the list.</dd>
<dt><code>setCDKRadioCurrentItem </code></dt>
<dd> sets the current item by its index in the list.</dd>
<dt><code>setCDKRadioHighlight</code></dt>
<dd> sets the attribute of the highlight bar.</dd>
<dt><code>setCDKRadioHorizontalChar</code></dt>
<dd> sets the horizontal drawing character for the box to the given character.</dd>
<dt><code>setCDKRadioItems</code></dt>
<dd> set the radio list items and display the result. The current item is set to the beginning of the list.</dd>
<dt><code>setCDKRadioLLChar</code></dt>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKRadioLRChar</code></dt>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKRadioLeftBrace</code></dt>
<dd> sets the character to use to draw the left brace of the selection box.</dd>
<dt><code>setCDKRadioPostProcess</code></dt>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about post-processing see <i>cdk_process (3)</i>.</dd>
<dt><code>setCDKRadioPreProcess</code></dt>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about pre-processing see <i>cdk_process (3)</i>.</dd>
<dt><code>setCDKRadioRightBrace</code></dt>
<dd> sets the character to use to draw the right brace of the selection box.</dd>
<dt><code>setCDKRadioSelectedItem</code></dt>
<dd> sets the selected item.</dd>
<dt><code>setCDKRadioULChar</code></dt>
<dd> function sets the upper left hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKRadioURChar</code></dt>
<dd> function sets the upper right hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKRadioVerticalChar</code></dt>
<dd> function sets the vertical drawing character for the box to the given character.</dd></dl>
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
<td>Shifts the whole list left one character.
</td>
</tr>
<tr VALIGN=top>
<td>Right Arrow</td>
<td>Shifts the whole list right one character.
</td>
</tr>
<tr VALIGN=top>
<td>Up Arrow</td>
<td>Selects the next item up in the list.
</td>
</tr>
<tr VALIGN=top>
<td>Down Arrow</td>
<td>Selects the next item down in the list.
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
<td>Shifts the whole list to the far right.
</td>
</tr>
<tr VALIGN=top>
<td>|</td>
<td>Shifts the whole list to the far left.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Space</td>
<td>Selects or deselects the current choice.
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Exits the widget and returns the index of the selected item. This also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td> Exit the widget and return the index of the selected item. Set the widget data <i>exitType</i> to <i>vNORMAL</i>.
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
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
</table>
<p></center></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
