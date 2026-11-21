---
title: "cdk_dscale(3)"
name: "cdk_dscale"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_dscale/"
description: "cdk_dscale – curses scale widget (type double)."
---

<h2>NAME</h2>
<p> cdk_dscale &#8211; curses scale widget (type double).</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>
double activateCDKDScale(
    CDKDSCALE *scale,
    chtype *actions);
void destroyCDKDScale(
    CDKDSCALE *scale);
void drawCDKDScale(
    CDKDSCALE *scale,
    boolean box);
void eraseCDKDScale(
    CDKDSCALE *scale);
boolean getCDKDScaleBox(
    CDKDSCALE *scale);
int getCDKDScaleDigits(
    CDKDSCALE *scale);
double getCDKDScaleHighValue(
    CDKDSCALE *scale);
double getCDKDScaleLowValue(
    CDKDSCALE *scale);
double getCDKDScaleValue(
    CDKDSCALE *scale);
int injectCDKDScale(
    CDKDSCALE *scale,
    chtype input);
void moveCDKDScale(
    CDKDSCALE *scale,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKDSCALE *newCDKDScale(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    const char *title,
    const char *label,
    chtype fieldAttribute,
    int fieldWidth,
    double currentValue,
    double lowValue,
    double highValue,
    double increment,
    double fastIncrement,
    int digits,
    boolean box,
    boolean shadow);
void positionCDKDScale(
    CDKDSCALE *scale);
void setCDKDScale(
    CDKDSCALE *scale,
    double lowValue,
    double highValue,
    double currentValue,
    boolean box);
void setCDKDScaleBackgroundAttrib(
    CDKDSCALE *scale,
    chtype attribute);
void setCDKDScaleBackgroundColor(
    CDKDSCALE *scale,
    const char *color);
void setCDKDScaleBox(
    CDKDSCALE *scale,
    boolean box);
void setCDKDScaleBoxAttribute(
    CDKDSCALE *scale,
    chtype character);
void setCDKDScaleDigits(
    CDKDSCALE *scale,
    int digits);
void setCDKDScaleHorizontalChar(
    CDKDSCALE *scale,
    chtype character);
void setCDKDScaleLLChar(
    CDKDSCALE *scale,
    chtype character);
void setCDKDScaleLRChar(
    CDKDSCALE *scale,
    chtype character);
void setCDKDScaleLowHigh(
    CDKDSCALE *scale,
    double low,
    double high);
void setCDKDScalePostProcess(
    CDKDSCALE *scale,
    PROCESSFN callback,
    void *data);
void setCDKDScalePreProcess(
    CDKDSCALE *scale,
    PROCESSFN callback,
    void *data);
void setCDKDScaleULChar(
    CDKDSCALE *scale,
    chtype character);
void setCDKDScaleURChar(
    CDKDSCALE *scale,
    chtype character);
void setCDKDScaleValue(
    CDKDSCALE *scale,
    double value);
void setCDKDScaleVerticalChar(
    CDKDSCALE *scale,
    chtype character);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk scale widget creates a scale box with a label and a scale field. The following functions create or manipulate the Cdk scale box widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKDScale</code></dt>
<dd> activates the scale widget and lets the user interact with the widget. The parameter <code>scale</code> is a pointer to a non-NULL scale widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> or <i>TAB</i> then this function will return a value from the low value to the high value. It will also set the widget data <i>exitType</i> to <i>vNORMAL</i>. If the character entered into this widget was <i>ESCAPE</i> then the widget will return the unknownDouble value (see the cdk_objs.h header file). The widget data <i>exitType</i> will be set to <i>vESCAPE_HIT</i>.</dd>
<dt><code>destroyCDKDScale</code></dt>
<dd> removes the widget from the screen and frees memory the object used.</dd>
<dt><code>drawCDKDScale</code></dt>
<dd> draws the scale widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</dd>
<dt><code>eraseCDKDScale</code></dt>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</dd>
<dt><code>getCDKDScaleBox</code></dt>
<dd> returns whether the widget will be drawn with a box around it.</dd>
<dt><code>getCDKDScaleDigits</code></dt>
<dd> returns the number of digits shown after the decimal point for the box value.</dd>
<dt><code>getCDKDScaleHighValue</code></dt>
<dd> returns the high value of the scale widget.</dd>
<dt><code>getCDKDScaleLowValue</code></dt>
<dd> returns the low value of the scale widget.</dd>
<dt><code>getCDKDScaleValue</code></dt>
<dd> returns the current value of the widget.</dd>
<dt><code>injectCDKDScale</code></dt>
<dd> injects a single character into the widget. The parameter <code>scale</code> is a pointer to a non-NULL scale widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</dd>
<dl>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></dt>
<dd> the function returns a value ranging from the scale&#8217;s low value to the scale&#8217;s high value. The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</dd>
<dt><i>ESCAPE</i></dt>
<dd> the function returns the unknownDouble value (see the cdk_objs.h header file). The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</dd>
<dt>Otherwise</dt>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns the unknownDouble value (see the cdk_objs.h header file). The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dd></dl>
</dl>
<dt><code>moveCDKDScale</code></dt>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</dd>
<dt><code>newCDKDScale</code></dt>
<dd> creates a pointer to a scale widget. Parameters:</dd>
<dl>
<dl>
<dt><code>screen</code></dt>
<dd> is the screen you wish this widget to be placed in.</dd>
<dt><code>xpos</code></dt>
<dd> controls the placement of the object along the horizontal axis. It may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>.</dd>
<dt><code>ypos</code></dt>
<dd> controls the placement of the object along the vertical axis. It may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</dd>
<dt><code>title</code></dt>
<dd> is the string to display at the top of the widget. The title can be more than one line; just provide a carriage return character at the line break.</dd>
<dt><code>label</code></dt>
<dd> is the string to display in the label of the scale field.</dd>
<dt><code>fieldAttribute</code></dt>
<dd> is the attribute of the characters displayed in the field.</dd>
<dt><code>fieldWidth</code></dt>
<dd> controls the width of the widget. If you provide a value of zero the widget will be created with the full width of the screen. If you provide a negative value, the widget will be created the full width minus the value provided.</dd>
<dt><code>currentValue</code></dt>
<dd> is the value of the scale field when the widget is activated.</dd>
<dt><code>lowValue</code> and</dt>
<dd>
</dd><dt><code>highValue</code></dt>
<dd> are the low and high values of the widget respectively.</dd>
<dt><code>increment</code></dt>
<dd> is the regular increment value</dd>
<dt><code>fastIncrement</code></dt>
<dd> is the accelerated increment value.</dd>
<dt><code>box</code></dt>
<dd> is true if the widget should be drawn with a box around it.</dd>
<dt><code>shadow</code></dt>
<dd> turns the shadow on or off around this widget.</dd></dl>
</dl>
<dt>
</dt><dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</dd>
<dt><code>positionCDKDScale</code></dt>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</dd>
<dt><code>setCDKDScale</code></dt>
<dd> lets the programmer modify certain elements of an existing scale widget. The parameter names correspond to the same parameter names listed in the <i>newCDKDScale</i> function.</dd>
<dt><code>setCDKDScaleBackgroundAttrib</code></dt>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</dd>
<dt><code>setCDKDScaleBackgroundColor</code></dt>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</dd>
<dt><code>setCDKDScaleBox</code></dt>
<dd> sets whether the widget will be drawn with a box around it.</dd>
<dt><code>setCDKDScaleBoxAttribute</code></dt>
<dd> sets the attribute of the box.</dd>
<dt><code>setCDKDScaleDigits</code></dt>
<dd> sets the number of digits shown after the decimal point for the box value.</dd>
<dt><code>setCDKDScaleHorizontalChar</code></dt>
<dd> sets the horizontal drawing character for the box to the given character.</dd>
<dt><code>setCDKDScaleLLChar</code></dt>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKDScaleLRChar</code></dt>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKDScaleLowHigh</code></dt>
<dd> sets the low and high values of the widget.</dd>
<dt><code>setCDKDScalePostProcess</code></dt>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about post-processing see <i>cdk_process (3)</i>.</dd>
<dt><code>setCDKDScalePreProcess</code></dt>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about pre-processing see <i>cdk_process (3)</i>.</dd>
<dt><code>setCDKDScaleULChar</code></dt>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKDScaleURChar</code></dt>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKDScaleValue</code></dt>
<dd> sets the current value of the widget.</dd>
<dt><code>setCDKDScaleVerticalChar</code></dt>
<dd> sets the vertical drawing character for the box to the given character.</dd></dl>
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
<td>Down Arrow</td>
<td> Decrements the scale by the normal value.
</td>
</tr>
<tr VALIGN=top>
<td>Up Arrow</td>
<td>Increments the scale by the normal value.
</td>
</tr>
<tr VALIGN=top>
<td>u</td>
<td>Increments the scale by the normal value.
</td>
</tr>
<tr VALIGN=top>
<td>Prev Page</td>
<td>Decrements the scale by the accelerated value.
</td>
</tr>
<tr VALIGN=top>
<td>U</td>
<td>Decrements the scale by the accelerated value.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-B</td>
<td>Decrements the scale by the accelerated value.
</td>
</tr>
<tr VALIGN=top>
<td>Next Page</td>
<td>Increments the scale by the accelerated value.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-F</td>
<td>Increments the scale by the accelerated value.
</td>
</tr>
<tr VALIGN=top>
<td>Home</td>
<td>Sets the scale to the low value.
</td>
</tr>
<tr VALIGN=top>
<td>g</td>
<td>Sets the scale to the low value.
</td>
</tr>
<tr VALIGN=top>
<td>^</td>
<td>Sets the scale to the low value.
</td>
</tr>
<tr VALIGN=top>
<td>End</td>
<td>Sets the scale to the high value.
</td>
</tr>
<tr VALIGN=top>
<td>G</td>
<td>Sets the scale to the high value.
</td>
</tr>
<tr VALIGN=top>
<td>$</td>
<td>Sets the scale to the high value.
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Exits the widget and returns the index of the selected value. This also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td> Exits the widget and returns the index of the selected value. This also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Escape</td>
<td> Exits the widget and returns the unknownDouble value (see the cdk_objs.h header file). This also sets the widget data <i>exitType</i> to <i>vESCAPE_HIT</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-R</td>
<td>Refreshes the screen.
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> If the cursor is not pointing to the field&#8217;s value, the following key bindings apply. You may use the left/right arrows to move the cursor onto the field&#8217;s value and modify it by typing characters to replace the digits and sign. <center></p>
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
<td> Decrements the scale by the normal value.
</td>
</tr>
<tr VALIGN=top>
<td>Right Arrow</td>
<td>Increments the scale by the normal value.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>d</td>
<td>Decrements the scale by the normal value.
</td>
</tr>
<tr VALIGN=top>
<td>D</td>
<td>Increments the scale by the accelerated value.
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;</td>
<td>Decrements the scale by the normal value.
</td>
</tr>
<tr VALIGN=top>
<td>+</td>
<td>Increments the scale by the normal value.
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>Sets the scale to the low value.
</td>
</tr>
</table>
</table>
<p></center></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
