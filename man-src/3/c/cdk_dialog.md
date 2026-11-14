---
title: "cdk_dialog(3)"
name: "cdk_dialog"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_dialog/"
description: "cdk_dialog – curses dialog widget"
---

<h2>NAME</h2>
<p> cdk_dialog &#8211; curses dialog widget</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

int activateCDKDialog(
    CDKDIALOG *dialog,
    chtype *actions);
void destroyCDKDialog(
    CDKDIALOG *dialog);
void drawCDKDialog(
    CDKDIALOG *dialog,
    boolean box);
void drawCDKDialogButtons(
    CDKDIALOG *dialog);
void eraseCDKDialog(
    CDKDIALOG *dialog);
boolean getCDKDialog(
    CDKDIALOG *dialog);
boolean getCDKDialogBox(
    CDKDIALOG *dialog);
chtype getCDKDialogHighlight(
    CDKDIALOG *dialog);
boolean getCDKDialogSeparator(
    CDKDIALOG *dialog);
int injectCDKDialog(
    CDKDIALOG *dialog,
    chtype input);
void moveCDKDialog(
    CDKDIALOG *dialog,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKDIALOG *newCDKDialog(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    CDK_CONST char **message,
    int rows,
    CDK_CONST char **buttons,
    int buttonCount,
    chtype highlight,
    boolean separator,
    boolean box,
    boolean shadow);
void positionCDKDialog(
    CDKDIALOG *dialog);
void setCDKDialogBox(
    CDKDIALOG *dialog,
    boolean boxWidget);
void setCDKDialog(
    CDKDIALOG *dialog,
    chtype highlight,
    boolean separator,
    boolean box);
void setCDKDialogBackgroundAttrib(
    CDKDIALOG *dialog,
    chtype attribute);
void setCDKDialogBackgroundColor(
    CDKDIALOG *dialog,
    const char *color);
void setCDKDialogBox(
    CDKDIALOG *dialog,
    boolean box);
void setCDKDialogBoxAttribute(
    CDKDIALOG *dialog,
    chtype character);
void setCDKDialogHighlight(
    CDKDIALOG *dialog,
    chtype highlight);
void setCDKDialogHorizontalChar(
    CDKDIALOG *dialog,
    chtype character);
void setCDKDialogLLChar(
    CDKDIALOG *dialog,
    chtype character);
void setCDKDialogLRChar(
    CDKDIALOG *dialog,
    chtype character);
void setCDKDialogPostProcess(
    CDKDIALOG *dialog,
    PROCESSFN callback,
    void *data);
void setCDKDialogPreProcess(
    CDKDIALOG *dialog,
    PROCESSFN callback,
    void *data);
void setCDKDialogSeparator(
    CDKDIALOG *dialog,
    boolean separator);
void setCDKDialogULChar(
    CDKDIALOG *dialog,
    chtype character);
void setCDKDialogURChar(
    CDKDIALOG *dialog,
    chtype character);
void setCDKDialogVerticalChar(
    CDKDIALOG *dialog,
    chtype character);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk dialog widget creates a dialog box with a message and a varied number of buttons to choose from. The following functions create or manipulate the Cdk dialog box widget. </p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKDialog</code></p>
<dd> activates the dialog widget and lets the user interact with the widget. The parameter <code>dialog</code> is a pointer to a non-NULL dialog widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> or <i>TAB</i> then this function will return a value from 0 to the number of buttons -1, representing the button selected. It also sets the widget data <i>exitType</i> to <i>vNORMAL</i>. If the character entered into this widget was <i>ESCAPE</i> then the widget returns a value of -1 and the widget data <i>exitType</i> will be set to <i>vESCAPE_HIT</i>.</p>
<dt><code>destroyCDKDialog</code></p>
<dd> removes the widget from the screen and frees memory the object used.</p>
<dt><code>drawCDKDialog</code></p>
<dd> draws the dialog widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</p>
<dt><code>drawCDKDialogButtons</code></p>
<dd> draws the dialog buttons and the separation line.</p>
<dt><code>eraseCDKDialog</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKDialog</code></p>
<dd> returns true if the list will be drawn with a box around it.</p>
<dt><code>getCDKDialogBox</code></p>
<dd> returns true if the dialog will be drawn with a box around it.</p>
<dt><code>getCDKDialogHighlight</code></p>
<dd> returns the highlight attribute of the widget.</p>
<dt><code>getCDKDialogSeparator</code></p>
<dd> returns the state of the separator flag.</p>
<dt><code>injectCDKDialog</code></p>
<dd> injects a single character into the widget. The parameter <code>dialog</code> is a pointer to a non-NULL dialog widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></p>
<dd> the function returns a value from zero to one less than the number of buttons, representing the button selected. The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</p>
<dt><i>ESCAPE</i></p>
<dd> the function returns -1. The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</p>
<dt>Otherwise</p>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns -1. The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dl>
</dl>
<dt><code>moveCDKDialog</code></p>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>newCDKDialog</code></p>
<dd> creates a dialog widget and returns a pointer to it. Parameters:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>screen</code></p>
<dd> is the screen you wish this widget to be placed in.</p>
<dt><code>xpos</code></p>
<dd> controls the placement of the object along the horizontal axis. It may be integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>.</p>
<dt><code>ypos</code></p>
<dd> controls the placement of the object along the vertical axis. It may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</p>
<dt><code>message</code></p>
<dd> is the text to be displayed in the message region of the dialog box.</p>
<dt><code>rows</code></p>
<dd> is the number of elements in the <code>message</code> list.</p>
<dt><code>buttons</code></p>
<dd> is an array containing the button labels to be displayed on the bottom of the dialog box.</p>
<dt><code>buttonCount</code></p>
<dd> is the number of elements in the <code>buttons</code> array.</p>
<dt><code>highlight</code></p>
<dd> is the attribute of the currently highlighted button.</p>
<dt><code>box</code></p>
<dd> is true if the widget should be drawn with a box around it.</p>
<dt><code>separator</code></p>
<dd> is true if a separator line should be drawn between the message region and the buttons.</p>
<dt><code>shadow</code></p>
<dd> turns the shadow on or off around this widget.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKDialog</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>setCDKDialogBox</code></p>
<dd> sets whether the widget will be drawn with a box around it.</p>
<dt><code>setCDKDialog</code></p>
<dd> lets the programmer modify certain elements of an existing dialog widget. The parameter names correspond to the same parameter names listed in the <code>newCDKDialog</code> function.</p>
<dt><code>setCDKDialogBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKDialogBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>. <code>setCDKDialogBox</code> sets the box attribute of the dialog widget.</p>
<dt><code>setCDKDialogBoxAttribute</code></p>
<dd> function sets the attribute of the box.</p>
<dt><code>setCDKDialogHighlight</code></p>
<dd> sets the highlight attribute of the selected button.</p>
<dt><code>setCDKDialogHorizontalChar</code></p>
<dd> sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKDialogLLChar</code></p>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKDialogLRChar</code></p>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKDialogPreProcess</code></p>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> is a pointer to <i>void</i>. To learn more about pre-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKDialogPostProcess</code></p>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about post-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKDialogSeparator</code></p>
<dd> sets the boolean flag whether the widget will be drawn with the separator bar between the buttons and the message area.</p>
<dt><code>setCDKDialogULChar</code></p>
<dd> function sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKDialogURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKDialogVerticalChar</code></p>
<dd> sets the vertical drawing character for the box to the given character.</dl>
<h2>KEY BINDINGS</h2>
<p> When the widget is activated there are several default key bindings which will help the user enter or manipulate the information quickly. The following table outlines the keys and their actions for this widget. </p>
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
<td>Refreshes the screen.
</td>
</tr>
</table>
<p></center></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_process/">cdk_process</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
