---

title: "cdk_template(3)"
name: "cdk_template"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_template/"
description: "cdk_template – a curses template widget."
---

<p> cdk_template &#8211; a curses template widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>
char *activateCDKTemplate(
    CDKTEMPLATE *template,
    chtype *actions);
void cleanCDKTemplate(
    CDKTEMPLATE *template);
void destroyCDKTemplate(
    CDKTEMPLATE *template);
void drawCDKTemplate(
    CDKTEMPLATE *template,
    boolean box);
void eraseCDKTemplate(
    CDKTEMPLATE *template);
boolean getCDKTemplateBox(
    CDKTEMPLATE *template);
int getCDKTemplateMin(
    CDKTEMPLATE *template);
char *getCDKTemplateValue(
    CDKTEMPLATE *template);
char *injectCDKTemplate(
    CDKTEMPLATE *template,
    chtype input);
char *mixCDKTemplate(
    CDKTEMPLATE *template);
void moveCDKTemplate(
    CDKTEMPLATE *template,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKTEMPLATE *newCDKTemplate(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    const char *title,
    const char *label,
    const char *plate,
    const char *overlay,
    boolean box,
    boolean shadow);
void positionCDKTemplate(
    CDKTEMPLATE *template);
void setCDKTemplate(
    CDKTEMPLATE *template,
    const char *value,
    boolean box);
void setCDKTemplateBackgroundAttrib(
    CDKTEMPLATE *template,
    chtype attribute);
void setCDKTemplateBackgroundColor(
    CDKTEMPLATE *template,
    const char *color);
void setCDKTemplateBox(
    CDKTEMPLATE *template,
    boolean box);
void setCDKTemplateBoxAttribute(
    CDKTEMPLATE *template,
    chtype character);
void setCDKTemplateCB(
    CDKTEMPLATE *template,
    TEMPLATECB callbackFunction);
void setCDKTemplateHorizontalChar(
    CDKTEMPLATE *template,
    chtype character);
void setCDKTemplateLLChar(
    CDKTEMPLATE *template,
    chtype character);
void setCDKTemplateLRChar(
    CDKTEMPLATE *template,
    chtype character);
void setCDKTemplateMin(
    CDKTEMPLATE *template,
    int minimum);
void setCDKTemplatePostProcess(
    CDKTEMPLATE *template,
    PROCESSFN callback,
    void *data);
void setCDKTemplatePreProcess(
    CDKTEMPLATE *template,
    PROCESSFN callback,
    void *data);
void setCDKTemplateULChar(
    CDKTEMPLATE *template,
    chtype character);
void setCDKTemplateURChar(
    CDKTEMPLATE *template,
    chtype character);
void setCDKTemplateValue(
    CDKTEMPLATE *template,
    const char *value);
void setCDKTemplateVerticalChar(
    CDKTEMPLATE *template,
    chtype character);
char *unmixCDKTemplate(
    CDKTEMPLATE *template,
    const char *string);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk template widget creates a template widget which allows a user to type information into an entry field with a pre-set field format. Typical uses for this widget would be a date field or a time field. The following are functions which create or manipulate the Cdk template box widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKTemplate</code></dt>
<dd> activates the template widget and lets the user interact with the widget. The parameter <code>template</code> is a pointer to a non-NULL template widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> or <i>TAB</i> then this function will return a <i>char&nbsp;<wbr>*</i> representing the information typed into the widget and the widget data <i>exitType</i> will be set to <i>vNORMAL</i>. If the character entered was <i>ESCAPE</i> then the function will return <i>NULL</i> pointer and the widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</dd>
<dt><code>cleanCDKTemplate</code></dt>
<dd> clears the information from the field.</dd>
<dt><code>destroyCDKTemplate</code></dt>
<dd> removes the widget from the screen and frees any memory the object used.</dd>
<dt><code>drawCDKTemplate</code></dt>
<dd> draws the template widget on the screen. If <code>box</code> is true, the widget is drawn with a box.</dd>
<dt><code>eraseCDKTemplate</code></dt>
<dd> removes the widget from the screen. This does <code>NOT</code> destroy the widget.</dd>
<dt><code>getCDKTemplateBox</code></dt>
<dd> returns true if the widget will be drawn with a box around it.</dd>
<dt><code>getCDKTemplateMin</code></dt>
<dd> returns the minimum characters that must be entered before the widget will exit.</dd>
<dt><code>getCDKTemplateValue</code></dt>
<dd> returns the current value of the widget.</dd>
<dt><code>injectCDKTemplate</code></dt>
<dd> injects a single character into the widget. The parameter <code>template</code> is a pointer to a non-NULL template widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</dd>
<dl>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></dt>
<dd> the function returns a <i>char&nbsp;<wbr>*</i> representing the information typed into the widget. The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</dd>
<dt><i>ESCAPE</i></dt>
<dd> the function returns a <i>NULL</i> pointer. The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</dd>
<dt>Otherwise</dt>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns a <i>NULL</i> pointer. The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dd></dl>
</dl>
<dt><code>mixCDKTemplate</code></dt>
<dd> returns a <i>char*</i> pointer to the field value and the plate.</dd>
<dt><code>moveCDKTemplate</code></dt>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> is an integer or one of the predefined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i> (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will be repainted after the move.</dd>
<dt><code>newCDKTemplate</code></dt>
<dd> creates a template widget, returning a pointer to it. Parameters:</dd>
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
<dd> is the string to display in the label of the template field.</dd>
<dt><code>plate</code></dt>
<dd> defines the character to allow at each position in the template field. This is done by creating a character plate by using special format character to tell the template widget what type of character is allowed where in the template widget. The following table lists the format types.</dd></dl>
<p> <center></p>
<table>
<tr VALIGN=top>
<td><code>Plate_Character</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>#
</td>
<td>Accepts an integer.
</td>
</tr>
<tr VALIGN=top>
<td>A
</td>
<td>Accepts an alphabetic value.
</td>
</tr>
<tr VALIGN=top>
<td>C
</td>
<td> Accepts an alphabetic value. Automatically converts the character to upper case.
</td>
</tr>
<tr VALIGN=top>
<td>c
</td>
<td> Accepts an alphabetic value. Automatically converts the character to lower case.
</td>
</tr>
<tr VALIGN=top>
<td>M
</td>
<td> Accepts alphanumeric characters.
</td>
</tr>
<tr VALIGN=top>
<td>X
</td>
<td> Accepts alphanumeric characters. Automatically converts the character to upper case.
</td>
</tr>
<tr VALIGN=top>
<td>x
</td>
<td> Accepts alphanumeric characters. Automatically converts the character to upper case.
</td>
</tr>
<tr VALIGN=top>
<td>Anything else
</td>
<td> Ignored and assumed a non-editable position.
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dl>
<dt><code>overlay</code></dt>
<dd> is the overlay of the template field. If the field needs some sort of overlay, this parameter supplies this. A date field could have YY/MM/DD, the overlay parameter would display YY/MM/DD on an empty template field.</dd>
<dt><code>box</code></dt>
<dd> is true if the widget should be drawn with a box around it.</dd>
<dt><code>shadow</code></dt>
<dd> turns the shadow on or off around this widget.</dd></dl>
</dl>
<dt>
</dt><dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</dd>
<dt><code>positionCDKTemplate</code></dt>
<dd> allows the user to move the widget around the screen via the single keystroke commands. See <code>cdk_position (3)</code> for key bindings.</dd>
<dt><code>setCDKTemplate</code></dt>
<dd> lets the programmer modify certain elements of an existing template widget. The parameter names correspond to the same parameter names listed in the <code>newCDKTemplate</code> function.</dd>
<dt><code>setCDKTemplateBackgroundAttrib</code></dt>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</dd>
<dt><code>setCDKTemplateBackgroundColor</code></dt>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. For more information, see the <i>cdk_display (3)</i>.</dd>
<dt><code>setCDKTemplateBox</code></dt>
<dd> sets a flag, true if the widget will be drawn with a box around it.</dd>
<dt><code>setCDKTemplateBoxAttribute</code></dt>
<dd> sets the attribute of the box.</dd>
<dt><code>setCDKTemplateCB</code></dt>
<dd> allows the programmer to set a different widget input handler. The parameter <code>callbackFunction</code> is of type <i>TEMPLATECB</i>. The default input handler is <i>CDKTemplateCallBack</i>.</dd>
<dt><code>setCDKTemplateHorizontalChar</code></dt>
<dd> sets the horizontal drawing character for the box to the given character.</dd>
<dt><code>setCDKTemplateLLChar</code></dt>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKTemplateLRChar</code></dt>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKTemplateMin</code></dt>
<dd> sets the minimum number of characters that must be entered before the widget will exit.</dd>
<dt><code>setCDKTemplatePostProcess</code></dt>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. To learn more about post-processing see <i>cdk_process</i> (3).</dd>
<dt><code>setCDKTemplatePreProcess</code></dt>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. To learn more about preprocessing see <i>cdk_process</i> (3).</dd>
<dt><code>setCDKTemplateULChar</code></dt>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKTemplateURChar</code></dt>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKTemplateValue</code></dt>
<dd> sets a value in the widget.</dd>
<dt><code>setCDKTemplateVerticalChar</code></dt>
<dd> sets the vertical drawing character for the box to the given character.</dd>
<dt><code>unmixCDKTemplate</code></dt>
<dd> returns a <i>char*</i> pointer to the field value without any plate characters.</dd></dl>
<h2>KEY BINDINGS</h2>
<p> When the widget is activated there are several default key bindings which will help the user enter or manipulate the information quickly. The following table outlines the keys and their actions for this widget. <center></p>
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
<td>Delete</td>
<td> Deletes the character at the cursor.
</td>
</tr>
<tr VALIGN=top>
<td>Backspace</td>
<td> Deletes the character before cursor, moves cursor left.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-P</td>
<td> Pastes whatever is in the paste buffer, into the widget.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-K</td>
<td> Cuts the contents from the widget and saves a copy in the paste buffer.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-T</td>
<td> Copies the contents of the widget into the paste buffer.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-E</td>
<td> Erases the contents of the widget.
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Exits the widget and returns a <i>char*</i> representing the information which was typed into the field. It also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td> Exits the widget and returns a <i>char*</i> representing the information which was typed into the field. It also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Escape</td>
<td> Exits the widget and returns a <i>NULL</i> pointer. It also sets the widget data <i>exitType</i> to <i>vESCAPE_HIT</i>.
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
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
