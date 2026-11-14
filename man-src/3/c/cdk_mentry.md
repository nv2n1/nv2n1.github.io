---
title: "cdk_mentry(3)"
name: "cdk_mentry"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_mentry/"
description: "cdk_mentry – curses multiple line entry widget."
---

<h2>NAME</h2>
<p> cdk_mentry &#8211; curses multiple line entry widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

char *activateCDKMentry(
    CDKMENTRY *mentry,
    chtype *actions);
void cleanCDKMentry(
    CDKMENTRY *mentry);
void destroyCDKMentry(
    CDKMENTRY *mentry);
void drawCDKMentry(
    CDKMENTRY *mentry,
    boolean box);
void drawCDKMentryField(
    CDKMENTRY *mentry);
void eraseCDKMentry(
    CDKMENTRY *mentry);
boolean getCDKMentryBox(
    CDKMENTRY *mentry);
chtype getCDKMentryFillerChar(
    CDKMENTRY *mentry);
chtype getCDKMentryHiddenChar(
    CDKMENTRY *mentry);
int getCDKMentryMin(
    CDKMENTRY *mentry);
char *getCDKMentryValue(
    CDKMENTRY *mentry);
char *injectCDKMentry(
    CDKMENTRY *mentry,
    chtype input);
void moveCDKMentry(
    CDKMENTRY *mentry,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKMENTRY *newCDKMentry(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    const char *title,
    const char *label,
    chtype fieldAttribute,
    chtype fillerCharacter,
    EDisplayType displayType,
    int fieldWidth,
    int fieldRows,
    int logicalRows,
    int minimumLength,
    boolean box,
    boolean shadow);
void positionCDKMentry(
    CDKMENTRY *mentry);
void setCDKMentry(
    CDKMENTRY *mentry,
    const char *value,
    int minimumLength,
    boolean box);
void setCDKMentryBackgroundAttrib(
    CDKMENTRY *mentry,
    chtype attribute);
void setCDKMentryBackgroundColor(
    CDKMENTRY *mentry,
    const char *color);
void setCDKMentryBox(
    CDKMENTRY *mentry,
    boolean boxWidget);
void setCDKMentryBoxAttribute(
    CDKMENTRY *mentry,
    chtype character);
void setCDKMentryCB(
    CDKMENTRY *mentry,
    MENTRYCB callBackFunction);
void setCDKMentryFillerChar(
    CDKMENTRY *mentry,
    chtype filler);
void setCDKMentryHiddenChar(
    CDKMENTRY *mentry,
    chtype character);
void setCDKMentryHorizontalChar(
    CDKMENTRY *mentry,
    chtype character);
void setCDKMentryLLChar(
    CDKMENTRY *mentry,
    chtype character);
void setCDKMentryLRChar(
    CDKMENTRY *mentry,
    chtype character);
void setCDKMentryMin(
    CDKMENTRY *mentry,
    int maximum);
void setCDKMentryPostProcess(
    CDKMENTRY *mentry,
    PROCESSFN callback,
    void *data);
void setCDKMentryPreProcess(
    CDKMENTRY *mentry,
    PROCESSFN callback,
    void *data);
void setCDKMentryULChar(
    CDKMENTRY *mentry,
    chtype character);
void setCDKMentryURChar(
    CDKMENTRY *mentry,
    chtype character);
void setCDKMentryValue(
    CDKMENTRY *mentry,
    const char *value);
void setCDKMentryVerticalChar(
    CDKMENTRY *mentry,
    chtype character);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk mentry widget creates a multiple line entry box with a label and an entry field. The following are functions which create or manipulate the Cdk mentry box widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKMentry</code></p>
<dd> activates the mentry widget and lets the user interact with the widget. The parameter <code>mentry</code> is a pointer to a non-NULL mentry widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> or <i>TAB</i> then this function will return a <i>char *</i> representing the information typed into the widget and the widget data <i>exitType</i> will be set to <i>vNORMAL</i>. If the character entered was <i>ESCAPE</i> then the function will return <i>NULL</i> pointer and the widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</p>
<dt><code>cleanCDKMentry</code></p>
<dd> clears the information from the field.</p>
<dt><code>destroyCDKMentry</code></p>
<dd> removes the widget from the screen and frees memory the object used.</p>
<dt><code>drawCDKMentry</code></p>
<dd> draws the widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</p>
<dt><code>drawCDKMentryField</code></p>
<dd> redraws the multiple line entry field.</p>
<dt><code>eraseCDKMentry</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKMentryBox</code></p>
<dd> returns true if the widget will be drawn with a box around it.</p>
<dt><code>getCDKMentryFillerChar</code></p>
<dd> returns the character being used to draw unused space in the widget.</p>
<dt><code>getCDKMentryHiddenChar</code></p>
<dd> returns the character being used to draw hidden characters in the widget (obsolete).</p>
<dt><code>getCDKMentryMin</code></p>
<dd> returns the minimum length of a string the widget will allow.</p>
<dt><code>getCDKMentryValue</code></p>
<dd> returns the current value of the widget.</p>
<dt><code>injectCDKMentry</code></p>
<dd> injects a single character into the widget. The parameter <code>mentry</code> is a pointer to a non-NULL mentry. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></p>
<dd> the function returns a <i>char *</i> representing the information typed into the widget. The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</p>
<dt><i>ESCAPE</i></p>
<dd> the function returns a <i>NULL</i> pointer. The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</p>
<dt>Otherwise</p>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns a <i>NULL</i> pointer. The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dl>
</dl>
<dt><code>moveCDKMentry</code></p>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>newCDKMentry</code></p>
<dd> creates a mentry widget and returns a pointer to it. Parameters:</p>
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
<dd> is the string which will be displayed in the label of the mentry field.</p>
<dt><code>fieldAttribute</code></p>
<dd> is the attribute of the characters to be displayed when they are typed in.</p>
<dt><code>filler</code></p>
<dd> is the character which is to display in an empty space in the mentry field.</p>
<dt><code>displayType</code></p>
<dd> tells how the mentry field will behave when a character is entered into the field. The following table outlines valid values for this field and what they mean:</dl>
<p> <center></p>
<table>
<tr VALIGN=top>
<td><code>Display_Type</code></td>
<td>Meaning
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>vCHAR</td>
<td>Only accepts alphabetic characters.
</td>
</tr>
<tr VALIGN=top>
<td>vLCHAR</td>
<td> Only accepts alphabetic characters. Maps the character to lower case when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vUCHAR</td>
<td> Only accepts alphabetic characters. Maps the character to upper case when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vHCHAR</td>
<td> Only accepts alphabetic characters. Displays a <i>.</i> when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vUHCHAR</td>
<td> Only accepts alphabetic characters. Displays a <i>.</i> and maps the character to upper case when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vLHCHAR</td>
<td> Only accepts alphabetic characters. Displays a <i>.</i> and maps the character to lower case when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vINT</td>
<td>Only accepts numeric characters.
</td>
</tr>
<tr VALIGN=top>
<td>vHINT</td>
<td> Only accepts numeric characters. Displays a <i>.</i> when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vMIXED</td>
<td>Accepts any character types.
</td>
</tr>
<tr VALIGN=top>
<td>vLMIXED</td>
<td> Accepts any character types. Maps the character to lower case when an alphabetic character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vUMIXED</td>
<td> Accepts any character types. Maps the character to upper case when an alphabetic character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vHMIXED</td>
<td> Accepts any character types. Displays a <i>.</i> when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vLHMIXED</td>
<td> Accepts any character types. Displays a <i>.</i> and maps the character to lower case when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vUHMIXED</td>
<td> Accepts any character types. Displays a <i>.</i> and maps the character to upper case when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vVIEWONLY</td>
<td>Uneditable field.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dl>
<dt><code>fieldRows</code> and</p>
<dd>
<dt><code>fieldWidth</code></p>
<dd> control the height and width of the field of the widget. If you provide a value of zero for either of the values, the field in the widget will be made as large as it can both in width and in height. If you provide a negative value, the field will be created the full height or width minus the value provided.</p>
<dt><code>logicalRows</code></p>
<dd> is the number of rows for the mentry field.</p>
<dt><code>minimumLength</code></p>
<dd> is the number of characters which must be entered before the use can exit the mentry field.</p>
<dt><code>callBackFunction</code></p>
<dd> allows the user to override the key processing element of the widget.</p>
<dt><code>box</code></p>
<dd> is true if widget should be drawn with a box around it.</p>
<dt><code>shadow</code></p>
<dd> turns the shadow on or off around this widget.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKMentry</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>setCDKMentry</code></p>
<dd> lets the programmer modify certain elements of an existing entry widget. The parameter names correspond to the same parameter names listed in the <code>newCDKMentry</code> function.</p>
<dt><code>setCDKMentryBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKMentryBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</p>
<dt><code>setCDKMentryBox</code></p>
<dd> sets whether the widget will be drawn with a box around it.</p>
<dt><code>setCDKMentryBoxAttribute</code></p>
<dd> function sets the attribute of the box.</p>
<dt><code>setCDKMentryCB</code></p>
<dd> function allows the programmer to set a different widget input handler. The parameter <code>callbackFunction</code> is of type <i>MENTRYCB</i>. The default function is <i>CDKMentryCallBack</i>.</p>
<dt><code>setCDKMentryFillerChar</code></p>
<dd> sets the character to use when drawing unused space in the field.</p>
<dt><code>setCDKMentryHiddenChar</code></p>
<dd> sets the character to use when a hidden character type is used (obsolete).</p>
<dt><code>setCDKMentryHorizontalChar</code></p>
<dd> function sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKMentryLLChar</code></p>
<dd> function sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKMentryLRChar</code></p>
<dd> function sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKMentryMin</code></p>
<dd> sets the minimum length of the string that the widget will allow.</p>
<dt><code>setCDKMentryPostProcess</code></p>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about post-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKMentryPreProcess</code></p>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about pre-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKMentryULChar</code></p>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKMentryURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKMentryValue</code></p>
<dd> sets the current value of the widget.</p>
<dt><code>setCDKMentryVerticalChar</code></p>
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
<td>Moves the cursor to the left.
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-B</td>
<td>Moves the cursor to the left.
</td>
</tr>
<tr VALIGN=top>
<td>Right Arrow</td>
<td>Moves the cursor to the right.
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-F</td>
<td>Moves the cursor to the right.
</td>
</tr>
<tr VALIGN=top>
<td>Up Arrow</td>
<td>Moves the cursor one row down.
</td>
</tr>
<tr VALIGN=top>
<td>Down Arrow</td>
<td>Moves the cursor one row up.
</td>
</tr>
<tr VALIGN=top>
<td>Delete</td>
<td>Deletes the character at the cursor.
</td>
</tr>
<tr VALIGN=top>
<td>Backspace</td>
<td>Deletes the character before cursor, moves cursor left.
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-V</td>
<td> Pastes whatever is in the paste buffer, into the widget.
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-X</td>
<td> Cuts the contents from the widget and saves a copy in the paste buffer.
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-Y</td>
<td> Copies the contents of the widget into the paste buffer.
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-U</td>
<td> Erases the contents of the widget.
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-A</td>
<td> Moves the cursor to the beginning of the entry field.
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-E</td>
<td> Moves the cursor to the end of the entry field.
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-T</td>
<td> Transposes the character under the cursor with the character to the right.
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Exits the widget and returns a <i>char *</i> representing the information which was typed into the field. It also sets the widget data <i>exitType</i> in the widget pointer to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td> Exits the widget and returns a <i>char *</i> representing the information which was typed into the field. It also sets the widget data <i>exitType</i> in the widget pointer to <i>vNORMAL</i>.
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
</table>
<p></center></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
