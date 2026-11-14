---
title: "cdk_marquee(3)"
name: "cdk_marquee"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_marquee/"
description: "cdk_marquee – curses marquee widget"
---

<h2>NAME</h2>
<p> cdk_marquee &#8211; curses marquee widget</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

int activateCDKMarquee(
    CDKMARQUEE *marquee,
    const char *message,
    int delay,
    int repeat,
    boolean box);
void deactivateCDKMarquee(
    CDKMARQUEE *marquee);
void destroyCDKMarquee(
    CDKMARQUEE *marquee);
void drawCDKMarquee(
    CDKMARQUEE *marquee,
    boolean box);
void eraseCDKMarquee(
    CDKMARQUEE *marquee);
boolean getCDKMarqueeBox(
    CDKMENTRY *mentry);
void moveCDKMarquee(
    CDKMARQUEE *marquee,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKMARQUEE *newCDKMarquee(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    int fieldWidth,
    boolean box,
    boolean shadow);
void positionCDKMarquee(
    CDKMARQUEE *marquee);
void setCDKMarqueeBackgroundAttrib(
    CDKMARQUEE *marquee,
    chtype attribute);
void setCDKMarqueeBackgroundColor(
    CDKMARQUEE *marquee,
    const char *color);
void setCDKMarqueeBox(
    CDKMENTRY *mentry,
    boolean boxWidget);
void setCDKMarqueeBoxAttribute(
    CDKMARQUEE *marquee,
    chtype character);
void setCDKMarqueeHorizontalChar(
    CDKMARQUEE *marquee,
    chtype character);
void setCDKMarqueeLLChar(
    CDKMARQUEE *marquee,
    chtype character);
void setCDKMarqueeLRChar(
    CDKMARQUEE *marquee,
    chtype character);
void setCDKMarqueeULChar(
    CDKMARQUEE *marquee,
    chtype character);
void setCDKMarqueeURChar(
    CDKMARQUEE *marquee,
    chtype character);
void setCDKMarqueeVerticalChar(
    CDKMARQUEE *marquee,
    chtype character);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk marquee widget creates a pop-up marquee window. The following functions create or manipulate the Cdk marquee widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKMarquee</code></p>
<dd> activates the marquee widget. The <code>marquee</code> parameter is a pointer to a defined marquee widget. The <code>delay</code> parameter states how long to wait between movements. This value is highly dependent on each machine the program runs on. The <code>repeat</code> value tells the marquee widget how many times to display the given message. The <code>box</code> option draws the widget with or without a box. This function returns -1 if the message passed is <i>NULL</i>, 0 otherwise.</p>
<dt><code>deactivateCDKMarquee</code></p>
<dd> deactivates the marquee widget.</p>
<dt><code>destroyCDKMarquee</code></p>
<dd> removes the widget from the screen and frees memory the object used.</p>
<dt><code>drawCDKMarquee</code></p>
<dd> draws the marquee widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</p>
<dt><code>eraseCDKMarquee</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKMarqueeBox</code></p>
<dd> returns true if the widget will be drawn with a box around it.</p>
<dt><code>moveCDKMarquee</code></p>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>newCDKMarquee</code></p>
<dd> creates a marquee widget and returns a pointer to it. Parameters:</p>
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
<dt><code>width</code></p>
<dd> controls the width of the field. If you provide a value of zero for the width, the widget uses the width of the screen. If a negative value is provided, then the widget uses the width of the screen less the value provided.</p>
<dt><code>shadow</code></p>
<dd> turns the shadow on or off around this widget.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKMarquee</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>setCDKMarqueeBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKMarqueeBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. For more information see <i>cdk_display (3)</i>.</p>
<dt><code>setCDKMarqueeBox</code></p>
<dd> sets whether the widget will be drawn with a box around it.</p>
<dt><code>setCDKMarqueeBoxAttribute</code></p>
<dd> sets the attribute of the box.</p>
<dt><code>setCDKMarqueeHorizontalChar</code></p>
<dd> sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKMarqueeLLChar</code></p>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKMarqueeLRChar</code></p>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKMarqueeULChar</code></p>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKMarqueeURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKMarqueeVerticalChar</code></p>
<dd> sets the vertical drawing character for the box to the given character.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
