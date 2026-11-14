---
title: "cdk_label(3)"
name: "cdk_label"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_label/"
description: "cdk_label – Creates a managed curses label widget."
---

<h2>NAME</h2>
<p> cdk_label &#8211; Creates a managed curses label widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

void activateCDKLabel(
    CDKLABEL *label,
    chtype unused);
void destroyCDKLabel(
    CDKLABEL *label);
void drawCDKLabel(
    CDKLABEL *label,
    boolean box);
void eraseCDKLabel(
    CDKLABEL *label);
boolean getCDKLabelBox(
    CDKLABEL *label);
chtype **getCDKLabelMessage(
    CDKLABEL *label int *messageLines);
void moveCDKLabel(
    CDKLABEL *label,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKLABEL *newCDKLabel(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    CDK_CONST char **message,
    int messageLines,
    boolean box,
    boolean shadow);
void positionCDKLabel(
    CDKLABEL *label);
void setCDKLabel(
    CDKLABEL *label,
    CDK_CONST char **message,
    int messageLines,
    boolean box);
void setCDKLabelBackgroundAttrib(
    CDKLABEL *label,
    chtype attribute);
void setCDKLabelBackgroundColor(
    CDKLABEL *label,
    const char *color);
void setCDKLabelBox(
    CDKLABEL *label,
    boolean box);
void setCDKLabelBoxAttribute(
    CDKLABEL *label,
    chtype character);
void setCDKLabelHorizontalChar(
    CDKLABEL *label,
    chtype character);
void setCDKLabelLLChar(
    CDKLABEL *label,
    chtype character);
void setCDKLabelLRChar(
    CDKLABEL *label,
    chtype character);
void setCDKLabelMessage(
    CDKLABEL *label,
    CDK_CONST char **message,
    int messageLines);
void setCDKLabelULChar(
    CDKLABEL *label,
    chtype character);
void setCDKLabelURChar(
    CDKLABEL *label,
    chtype character);
void setCDKLabelVerticalChar(
    CDKLABEL *label,
    chtype character);
char waitCDKLabel(
    CDKLABEL *label,
    char key);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk label widget creates a pop-up label window. The following functions create or manipulate the Cdk label widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKLabel</code></p>
<dd> obsolete entrypoint which calls <code>drawCDKLabel</code>.</p>
<dt><code>destroyCDKLabel</code></p>
<dd> removes the widget from the screen and frees memory the object used.</p>
<dt><code>drawCDKLabel</code></p>
<dd> draws the label widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</p>
<dt><code>eraseCDKLabel</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKLabelBox</code></p>
<dd> returns true if the widget will be drawn with a box around it.</p>
<dt><code>getCDKLabelMessage</code></p>
<dd> returns the contents of the label widget. The parameter <code>messageLines</code> points to the location which will be given the number of message-lines.</p>
<dt><code>moveCDKLabel</code></p>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>newCDKLabel</code></p>
<dd> creates a label widget and returns a pointer to it. Parameters:</p>
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
<dt><code>message</code></p>
<dd> is the message to be displayed in the window. It may contain any of the standard Cdk display format commands. To learn more about this see <i>cdk_display (3)</i>.</p>
<dt><code>rows</code></p>
<dd> is the number of message rows that were passed in the <code>message</code> parameter.</p>
<dt><code>box</code></p>
<dd> is true if widget should be drawn with a box around it.</p>
<dt><code>shadow</code></p>
<dd> turns the shadow on or off around this widget.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKLabel</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>setCDKLabel</code></p>
<dd> allows the user to change the contents of the label widget. The parameters are the same as the <code>newCDKLabel</code>.</p>
<dt><code>setCDKLabelBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKLabelBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. For more information see <i>cdk_display (3)</i>.</p>
<dt><code>setCDKLabelBox</code></p>
<dd> sets whether the widget will be drawn with a box around it.</p>
<dt><code>setCDKLabelBoxAttribute</code></p>
<dd> sets the attribute of the box.</p>
<dt><code>setCDKLabelHorizontalChar</code></p>
<dd> sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKLabelLLChar</code></p>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKLabelLRChar</code></p>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKLabelMessage</code></p>
<dd> This sets the contents of the label widget.</p>
<dt><code>setCDKLabelULChar</code></p>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKLabelURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKLabelVerticalChar</code></p>
<dd> sets the vertical drawing character for the box to the given character.</p>
<dt><code>waitCDKLabel</code></p>
<dd> waits for a user to press a key. The <code>label</code> parameter is the pointer to a label widget, and <code>key</code> is the key to wait for. If no specific key is desired, use <i>(char)0</i>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
