---
title: "cdk_button(3)"
name: "cdk_button"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_button/"
description: "cdk_button – create and manage a curses button widget."
---

<h2>NAME</h2>
<p> cdk_button &#8211; create and manage a curses button widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<p> typedef void (*tButtonCallback)(struct SButton *button); </p>
<pre><code>

int activateCDKButton(
    CDKBUTTON *button,
    chtype *actions);
void destroyCDKButton(
    CDKBUTTON *button);
void drawCDKButton(
    CDKBUTTON *b,
    boolean box);
void eraseCDKButton(
    CDKBUTTON *button);
boolean getCDKButtonBox(
    CDKBUTTON *b);
chtype *getCDKButtonMessage(
    CDKBUTTON *b);
int injectCDKButtonbox(
    CDKBUTTON *buttonbox,
    chtype input);
CDKBUTTON *newCDKButton(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    const char *message,
    tButtonCallback callback,
    boolean box,
    boolean shadow);
void setCDKButton(
    CDKBUTTON *b,
    const char *message,
    boolean box);
void setCDKButtonBackgroundAttrib(
    CDKBUTTON *b,
    chtype attribute);
void setCDKButtonBackgroundColor(
    CDKBUTTON *b,
    const char *color);
void setCDKButtonBox(
    CDKBUTTON *button,
    boolean box);
void setCDKButtonBoxAttribute(
    CDKBUTTON *b,
    chtype c);
void setCDKButtonHorizontalChar(
    CDKBUTTON *b,
    chtype c);
void setCDKButtonLLChar(
    CDKBUTTON *b,
    chtype c);
void setCDKButtonLRChar(
    CDKBUTTON *b,
    chtype c);
void setCDKButtonMessage(
    CDKBUTTON *b,
    const char *message);
void setCDKButtonULChar(
    CDKBUTTON *b,
    chtype c);
void setCDKButtonURChar(
    CDKBUTTON *b,
    chtype c);
void setCDKButtonVerticalChar(
    CDKBUTTON *b,
    chtype c);
void moveCDKButton(
    CDKBUTTON *b,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
void positionCDKButton(
    CDKBUTTON *b);
void waitCDKButton(
    CDKBUTTON *button,
    char key);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk button widget displays a message string and executes a callback when the user presses enter or space. As such, it is only useful on a screen that is being managed by some external screen traversal engine such as <code>traverseCDKScreen()</code>. The button will be highlighted when the widget has the focus. The following functions create or manipulate the Cdk button widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKButton</code></p>
<dd> activates the button widget and lets the user interact with the widget. The parameter <code>button</code> is a pointer to a non-NULL button widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> or <i>TAB</i> then this function will return a value from 0 to the number of buttons -1, representing the button selected. It will also set the widget data <i>exitType</i> to <i>vNORMAL</i>. If the character entered into this widget was <i>ESCAPE</i> then the widget will return a value of -1 and the widget data <i>exitType</i> will be set to <i>vESCAPE_HIT</i>.</p>
<dt><code>destroyCDKButton</code></p>
<dd> removes the widget from the screen and frees up any memory the object used.</p>
<dt><code>drawCDKButton</code></p>
<dd> draws the button widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</p>
<dt><code>eraseCDKButton</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKButtonBox</code></p>
<dd> returns true if the widget will be drawn with a box around it.</p>
<dt><code>getCDKButtonMessage</code></p>
<dd> returns the contents of the button widget.</p>
<dt><code>injectCDKButton</code></p>
<dd> injects a single character into the widget. The parameter <code>button</code> is a pointer to a non-NULL button widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></p>
<dd> this function returns 0, representing the button selected. The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</p>
<dt><i>ESCAPE</i></p>
<dd> the function returns -1. The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</p>
<dt>Otherwise</p>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns -1. The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dl>
</dl>
<dt><code>moveCDKButton</code></p>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>newCDKButton</code></p>
<dd> creates a pointer to a buttonbox widget. Parameters:</p>
<dl>
<dt>
<dd>
<dl>
<dt>The <code>screen</code> parameter</p>
<dd> is the screen you wish this widget to be placed in.</p>
<dt><code>xpos</code></p>
<dd> controls the placement of the object along the horizontal axis. It may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>.</p>
<dt><code>ypos</code></p>
<dd> controls the placement of the object along the vertical axis. It be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</p>
<dt><code>message</code></p>
<dd> is the message to display in the button window, formatted as described in <i>cdk_display</i>.</p>
<dt><code>callback</code></p>
<dd> is an optional pointer to a callback function that will be executed when the user activates the button by pressing space or enter.</p>
<dt><code>box</code></p>
<dd> is true if the widget should be drawn with a box around it.</p>
<dt><code>shadow</code></p>
<dd> turns the shadow on or off around this widget.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKButton</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>setCDKButton</code></p>
<dd> lets the programmer modify certain elements of an existing buttonbox widget. The parameter names correspond to the same parameter names listed in the <code>newCDKButton</code> function.</p>
<dt><code>setCDKButtonBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKButtonBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. (See <i>cdk_display</i>).</p>
<dt><code>setCDKButtonBox </code></p>
<dd> sets true if the widget will be drawn with a box around it.</p>
<dt><code>setCDKButtonBoxAttribute</code></p>
<dd> sets the attribute of the box.</p>
<dt><code>setCDKButtonHorizontalChar</code></p>
<dd> sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKButtonLLChar</code></p>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKButtonLRChar</code></p>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKButtonMessage</code></p>
<dd> This sets the contents of the label widget.</p>
<dt><code>setCDKButtonULChar</code></p>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKButtonURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKButtonVerticalChar</code></p>
<dd> sets the vertical drawing character for the box to the given character.</dl>
<h2>BUGS</h2>
<p> Changing the Box attribute after the widget has been created probably does not work right. None of the positioning/movement code has been tested.</p>
<h2>AUTHOR</h2>
<p> Grant Edwards, Aspen Research Corporation</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_process/">cdk_process</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3), <code><a href="/docs/linux/man/3-cdk_traverse/">cdk_traverse</a></code>(3) </p>
<h2>Index</h2>
