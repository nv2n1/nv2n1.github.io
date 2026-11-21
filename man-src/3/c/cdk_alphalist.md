---
title: "cdk_alphalist(3)"
name: "cdk_alphalist"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_alphalist/"
description: "cdk_alphalist – curses sorted list widget."
---

<h2>NAME</h2>
<p> cdk_alphalist &#8211; curses sorted list widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>
char *activateCDKAlphalist(
    CDKALPHALIST *alphalist,
    chtype *actions);
void destroyCDKAlphalist(
    CDKALPHALIST *alphalist);
void drawCDKAlphalist(
    CDKALPHALIST *alphalist,
    boolean box);
void eraseCDKAlphalist(
    CDKALPHALIST *alphalist);
boolean getCDKAlphalistBox(
    CDKALPHALIST *alphalist);
char **getCDKAlphalistContents(
    CDKALPHALIST *alphalist,
    int *size);
int getCDKAlphalistCurrentItem(
    CDKALPHALIST *widget);
chtype getCDKAlphalistFillerChar(
    CDKALPHALIST *alphalist);
chtype getCDKAlphalistHighlight(
    CDKALPHALIST *alphalist);
char *injectCDKAlphalist(
    CDKALPHALIST *alphalist,
    chtype input);
void moveCDKAlphalist(
    CDKALPHALIST *alphalist,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKALPHALIST *newCDKAlphalist(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    int height,
    int width,
    const char *title,
    const char *label,
    CDK_CONST char **list,
    int listSize,
    chtype fillerCharacter,
    chtype highlight,
    boolean box,
    boolean shadow);
void positionCDKAlphalist(
    CDKALPHALIST *alphalist);
void setCDKAlphalist(
    CDKALPHALIST *alphalist,
    CDK_CONST char **list,
    int listSize,
    chtype fillerCharacter,
    chtype highlight,
    boolean box);
void setCDKAlphalistBackgroundAttrib(
    CDKALPHALIST *alphalist,
    chtype attribute);
void setCDKAlphalistBackgroundColor(
    CDKALPHALIST *alphalist,
    const char *color);
void setCDKAlphalistBox(
    CDKALPHALIST *alphalist,
    boolean box);
void setCDKAlphalistBoxAttribute(
    CDKALPHALIST *alphalist,
    chtype character);
void setCDKAlphalistContents(
    CDKALPHALIST *alphalist,
    CDK_CONST char **list,
    int listSize);
void setCDKAlphalistCurrentItem(
    CDKALPHALIST *widget,
    int item);
void setCDKAlphalistFillerChar(
    CDKALPHALIST *alphalist,
    chtype fillerCharacter);
void setCDKAlphalistHighlight(
    CDKALPHALIST *alphalist,
    chtype highlight);
void setCDKAlphalistHorizontalChar(
    CDKALPHALIST *alphalist,
    chtype character);
void setCDKAlphalistLLChar(
    CDKALPHALIST *alphalist,
    chtype character);
void setCDKAlphalistLRChar(
    CDKALPHALIST *alphalist,
    chtype character);
void setCDKAlphalistPostProcess(
    CDKALPHALIST *alphalist,
    PROCESSFN callback,
    void *data);
void setCDKAlphalistPreProcess(
    CDKALPHALIST *alphalist,
    PROCESSFN callback,
    void *data);
void setCDKAlphalistULChar(
    CDKALPHALIST *alphalist,
    chtype character);
void setCDKAlphalistURChar(
    CDKALPHALIST *alphalist,
    chtype character);
void setCDKAlphalistVerticalChar(
    CDKALPHALIST *alphalist,
    chtype character);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The Cdk alphalist allows a user to select from a list of alphabetically sorted words. The user can use the arrow keys to traverse through the list or type in the beginning of the word and the list will automatically adjust itself in the correct place in the scrolling list. This widget, like the file selector widget, is a compound widget of both the entry field widget and the scrolling list widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKAlphalist</code></dt>
<dd> activates the alphalist widget and lets the user interact with the widget. The parameter <code>alphalist</code> is a pointer to a non-NULL alphalist widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> then this function will return a <i>char *</i> of the information which was typed in the field. If the <i>TAB</i> character is hit then the widget will try to complete the word in the entry field. If the widget is exited with the <i>RETURN</i> character then the widget data <i>exitType</i> will be set to <i>vNORMAL</i>. If the widget was exited with the <i>ESCAPE</i> key then the widget data <i>exitType</i> will be set to <i>vESCAPE_HIT</i> and the widget returns <i>NULL</i>.</dd>
<dt><code>destroyCDKAlphalist</code></dt>
<dd> removes the widget from the screen and frees memory the object used.</dd>
<dt><code>drawCDKAlphalist</code></dt>
<dd> draws the alphalist widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</dd>
<dt><code>eraseCDKAlphalist</code></dt>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</dd>
<dt><code>getCDKAlphalistBox</code></dt>
<dd> returns true if the widget will be drawn with a box around it.</dd>
<dt><code>getCDKAlphalistContents</code></dt>
<dd> returns the contents of the alphalist.</dd>
<dt><code>getCDKAlphalistCurrentItem</code></dt>
<dd> returns the current position in the scroll-widget.</dd>
<dt><code>getCDKAlphalistFillerChar</code></dt>
<dd> returns the character being used as the filler character in the entry field portion of the widget.</dd>
<dt><code>getCDKAlphalistHighlight</code></dt>
<dd> returns the attribute of the highlight bar of the scrolling list portion of the widget.</dd>
<dt><code>injectCDKAlphalist</code></dt>
<dd> injects a single character into the widget (actually the entry widget). The parameter <code>alphalist</code> is a pointer to a non-NULL alphalist widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</dd>
<dl>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></dt>
<dd> the function returns the information in the entry field. The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</dd>
<dt><i>ESCAPE</i></dt>
<dd> the function returns a <i>NULL</i> pointer. The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</dd>
<dt>Otherwise</dt>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns a <i>NULL</i> pointer. The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dd></dl>
</dl>
<dt><code>moveCDKAlphalist</code></dt>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</dd>
<dt><code>newCDKAlphalist</code></dt>
<dd> creates a pointer to an alphalist widget. Parameters:</dd>
<dl>
<dl>
<dt><code>screen</code></dt>
<dd> is the screen you wish this widget to be placed in.</dd>
<dt><code>xpos</code></dt>
<dd> controls the placement of the object along the horizontal axis. This parameter can take an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>.</dd>
<dt><code>ypos</code></dt>
<dd> controls the placement of the object along the vertical axis. This parameter may be an integer value or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</dd>
<dt><code>height</code> and</dt>
<dd>
</dd><dt><code>width</code></dt>
<dd> control the height and width of the widget. If you provide a value of zero for either of the height or the width, the widget will be created with the full width and height of the screen. If you provide a negative value, the widget will be created the full height or width minus the value provided.</dd>
<dt><code>title</code></dt>
<dd> is the string which will be displayed at the top of the scrolling list. The title can be more than one line; just provide a carriage return character at the line break.</dd>
<dt><code>label</code></dt>
<dd> is the string which will be displayed in the label of the entry field.</dd>
<dt><code>list</code></dt>
<dd> is the list of words which will be displayed in the scrolling list. This list does not have to be sorted, this widget automatically sorts the list (note that it modifies the caller&#8217;s copy of the list to do this).</dd>
<dt><code>listSize</code></dt>
<dd> tells the widget how large the word list is.</dd>
<dt><code>fillerCharacter</code></dt>
<dd> is the character which is to be displayed in an empty space in the entry field.</dd>
<dt><code>highlight</code></dt>
<dd> is the attribute of the highlight bar in the scrolling list.</dd>
<dt><code>box</code></dt>
<dd> is true if the widget should be drawn with a box around it.</dd>
<dt><code>shadow</code></dt>
<dd> is true to turn the shadow on around this widget.</dd></dl>
</dl>
<dt>
</dt><dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</dd>
<dt><code>positionCDKAlphalist</code></dt>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</dd>
<dt><code>setCDKAlphalist</code></dt>
<dd> lets the programmer modify certain elements of an existing alphalist widget. The parameter names correspond to the same parameter names listed in the <code>newCDKAlphalist</code> function.</dd>
<dt><code>setCDKAlphalistBackgroundAttrib</code></dt>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</dd>
<dt><code>setCDKAlphalistBackgroundColor</code></dt>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</dd>
<dt><code>setCDKAlphalistBox</code></dt>
<dd> sets whether the widget will be drawn with a box around it.</dd>
<dt><code>setCDKAlphalistBoxAttribute</code></dt>
<dd> sets the attribute of the box.</dd>
<dt><code>setCDKAlphalistContents</code></dt>
<dd> sets the contents of the alphalist widget (note that it sorts the caller&#8217;s copy of the list).</dd>
<dt><code>setCDKAlphalistCurrentItem</code></dt>
<dd> set the current position in the scroll-widget.</dd>
<dt><code>setCDKAlphalistFillerChar</code></dt>
<dd> sets the character to use when drawing the entry field portion of the widget.</dd>
<dt><code>setCDKAlphalistHighlight</code></dt>
<dd> sets the attribute of the highlight bar of the scrolling list portion of the widget.</dd>
<dt><code>setCDKAlphalistHorizontalChar</code></dt>
<dd> sets the horizontal drawing character for the box to the given character.</dd>
<dt><code>setCDKAlphalistLLChar</code></dt>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKAlphalistLRChar</code></dt>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKAlphalistPostProcess</code></dt>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about post-processing see <i>cdk_process (3)</i>.</dd>
<dt><code>setCDKAlphalistPreProcess</code></dt>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about pre-processing see <i>cdk_process (3)</i>.</dd>
<dt><code>setCDKAlphalistULChar</code></dt>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKAlphalistURChar</code></dt>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKAlphalistVerticalChar</code></dt>
<dd> sets the vertical drawing character for the box to the given character.</dd></dl>
<h2>KEY BINDINGS</h2>
<p> When the widget is activated there are several default key bindings which will help the user enter or manipulate the information quickly. Since this widget is built from both the scrolling list widget and the entry field widget, the key bindings are the same for the respective fields. The extra key bindings are listed below. </p>
<p> <center></p>
<table BORDER>
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
<td>Up Arrow</td>
<td> Scrolls the scrolling list up one line.
</td>
</tr>
<tr VALIGN=top>
<td>Down Arrow</td>
<td> Scrolls the scrolling list down one line.
</td>
</tr>
<tr VALIGN=top>
<td>Page Up</td>
<td> Scrolls the scrolling list up one page.
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-B</td>
<td> Scrolls the scrolling list up one page. Page Down/Scrolls the scrolling list down one page.
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-F</td>
<td> Scrolls the scrolling list down one page.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td> Tries to complete the word in the entry field. If the word segment is not unique then the widget will beep and present a list of close matches.
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Returns the word in the entry field. It also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Escape</td>
<td> Exits the widget and returns a <i>NULL</i> pointer. It also sets the widget data <i>exitType</i> to <i>vESCAPE_HIT</i>.
</td>
</tr>
</table>
<p></center></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3)</p>
<h2>NOTES</h2>
<p> This widget is created from the scrolling list widget and the entry field widget. This is a good example on how to build your own widgets using the base widgets provided in this distribution. </p>
