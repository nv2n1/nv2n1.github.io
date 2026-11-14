---
title: "cdk_entry(3)"
name: "cdk_entry"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_entry/"
description: "cdk_entry – curses text-entry widget."
---

<h2>NAME</h2>
<p> cdk_entry &#8211; curses text-entry widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

char *activateCDKEntry(
    CDKENTRY *entry,
    chtype *actions);
void cleanCDKEntry(
    CDKENTRY *entry);
void destroyCDKEntry(
    CDKENTRY *entry);
void drawCDKEntry(
    CDKENTRY *entry,
    boolean box);
void eraseCDKEntry(
    CDKENTRY *entry);
boolean getCDKEntryBox(
    CDKENTRY *entry);
chtype getCDKEntryFillerChar(
    CDKENTRY *entry);
chtype getCDKEntryHiddenChar(
    CDKENTRY *entry);
int getCDKEntryMax(
    CDKENTRY *entry);
int getCDKEntryMin(
    CDKENTRY *entry);
char *getCDKEntryValue(
    CDKENTRY *entry);
int injectCDKEntry(
    CDKENTRY *entry,
    chtype input);
void moveCDKEntry(
    CDKENTRY *entry,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKENTRY *newCDKEntry(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    const char *title,
    const char *label,
    chtype fieldAttribute,
    chtype fillerCharacter,
    EDisplayType displayType,
    int fieldWidth,
    int minimumLength,
    int maximumLength,
    boolean box,
    boolean shadow);
void positionCDKEntry(
    CDKENTRY *entry);
void setCDKEntry(
    CDKENTRY *entry,
    const char *value,
    int minimumLength,
    int maximumLength,
    boolean box);
void setCDKEntryBackgroundAttrib(
    CDKENTRY *entry,
    chtype attribute);
void setCDKEntryBackgroundColor(
    CDKENTRY *entry,
    const char *color);
void setCDKEntryBox(
    CDKENTRY *entry,
    boolean box);
void setCDKEntryBoxAttribute(
    CDKENTRY *entry,
    chtype character);
void setCDKEntryCB(
    CDKENTRY *entry,
    ENTRYCB callBackFunction);
void setCDKEntryFillerChar(
    CDKENTRY *entry,
    chtype character);
void setCDKEntryHiddenChar(
    CDKENTRY *entry,
    chtype character);
void setCDKEntryHighlight(
    CDKENTRY *entry,
    chtype highlight,
    boolean cursor);
void setCDKEntryHorizontalChar(
    CDKENTRY *entry,
    chtype character);
void setCDKEntryLLChar(
    CDKENTRY *entry,
    chtype character);
void setCDKEntryLRChar(
    CDKENTRY *entry,
    chtype character);
void setCDKEntryMax(
    CDKENTRY *entry,
    int maximum);
void setCDKEntryMin(
    CDKENTRY *entry,
    int minimum);
void setCDKEntryPostProcess(
    CDKENTRY *entry,
    PROCESSFN callback,
    void *data);
void setCDKEntryPreProcess(
    CDKENTRY *entry,
    PROCESSFN callback,
    void *data);
void setCDKEntryULChar(
    CDKENTRY *entry,
    chtype character);
void setCDKEntryURChar(
    CDKENTRY *entry,
    chtype character);
void setCDKEntryValue(
    CDKENTRY *entry,
    const char *value);
void setCDKEntryVerticalChar(
    CDKENTRY *entry,
    chtype character);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk entry widget creates a text-entry box with a label and an entry field. The following functions create or manipulate the Cdk entry box widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKEntry</code></p>
<dd> activates the entry widget and lets the user interact with the widget. The parameter <code>entry</code> is a pointer to a non-NULL entry widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> or <i>TAB</i> then this function will return a <i>char *</i> representing the information typed into the widget and the widget data <i>exitType</i> will be set to <i>vNORMAL</i>. If the character entered was <i>ESCAPE</i> then the function will return <i>NULL</i> pointer and the widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</p>
<dt><code>cleanCDKEntry</code></p>
<dd> clears the information from the field.</p>
<dt><code>destroyCDKEntry</code></p>
<dd> removes the widget from the screen and frees memory the object used.</p>
<dt><code>drawCDKEntry</code></p>
<dd> draws the entry widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</p>
<dt><code>eraseCDKEntry</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKEntryBox</code></p>
<dd> returns true if the widget will be drawn with a box around it.</p>
<dt><code>getCDKEntryFillerChar</code></p>
<dd> returns the character being used to draw unused space in the widget.</p>
<dt><code>getCDKEntryHiddenChar</code></p>
<dd> returns the character being used to draw the hidden character type.</p>
<dt><code>getCDKEntryMax</code></p>
<dd> returns the maximum length of a string the widget will allow.</p>
<dt><code>getCDKEntryMin</code></p>
<dd> returns the minimum length of a string the widget will allow.</p>
<dt><code>getCDKEntryValue</code></p>
<dd> returns the current value of the widget.</p>
<dt><code>injectCDKEntry</code></p>
<dd> injects a single character into the widget. The parameter <code>entry</code> is a pointer to a non-NULL entry widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</p>
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
<dt><code>moveCDKEntry</code></p>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>newCDKEntry</code></p>
<dd> creates a pointer to an entry widget. Parameters:</p>
<dl>
<dt>
<dd>
<dl>
<dt>The <code>screen</code> parameter</p>
<dd> is the screen you wish this widget to be placed in.</p>
<dt><code>xpos</code></p>
<dd> controls the placement of the object along the horizontal axis. It may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>.</p>
<dt><code>ypos</code></p>
<dd> controls the placement of the object along the vertical axis. It may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</p>
<dt><code>title</code></p>
<dd> is the string which will be displayed at the top of the widget. The title can be more than one line; just provide a carriage return character at the line break.</p>
<dt><code>label</code></p>
<dd> is the string which will be displayed in the label of the entry field.</p>
<dt><code>fieldAttribute</code></p>
<dd> is the attribute of the characters which are typed in.</p>
<dt><code>filler</code></p>
<dd> is the character which is to be displayed in an empty space in the entry field.</p>
<dt><code>displayType</code></p>
<dd> tells how the entry field will behave when a character is entered into the field. See <code>cdk_display (3)</code> for valid values for this field.</p>
<dt><code>fieldWidth</code></p>
<dd> denotes the width of the field. If a value of zero is provided, the field will be made as wide as possible on the screen. If a negative value is given, then the field width will be the maximum width minus the value provided.</p>
<dt><code>minimumLength</code></p>
<dd> controls the number of characters which must be entered before the user can exit the entry field.</p>
<dt><code>maximumLength</code></p>
<dd> sets the maximum number of characters that can be entered.</p>
<dt><code>box</code></p>
<dd> is true if the widget should be drawn with a box around it.</p>
<dt><code>shadow</code></p>
<dd> turns the shadow on around this widget.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKEntry</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. The following key bindings can be used to move the widget around the screen. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>setCDKEntry</code></p>
<dd> lets the programmer modify certain elements of an existing entry widget. The <code>value</code> parameter sets the value of the contents of the entry field. The other parameter names correspond to the same parameter names listed in the <code>newCDKEntry</code> function.</p>
<dt><code>setCDKEntryBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKEntryBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</p>
<dt><code>setCDKEntryBox</code></p>
<dd> sets whether the widget will be drawn with a box around it.</p>
<dt><code>setCDKEntryBoxAttribute</code></p>
<dd> function sets the attribute of the box.</p>
<dt><code>setCDKEntryCB</code></p>
<dd> allows the programmer to set a different widget input handler. The parameter <code>callbackFunction</code> is of type <i>ENTRYCB</i>. The default function is <i>CDKEntryCallBack</i>.</p>
<dt><code>setCDKEntryFillerChar</code></p>
<dd> sets the character to use when drawing unused space in the field.</p>
<dt><code>setCDKEntryHiddenChar</code></p>
<dd> sets the character to use when using a hidden character type.</p>
<dt><code>setCDKEntryHighlight</code></p>
<dd> sets the attribute of the entry field.</p>
<dt><code>setCDKEntryHorizontalChar</code></p>
<dd> sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKEntryLLChar</code></p>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKEntryLRChar</code></p>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKEntryMax</code></p>
<dd> sets the maximum length of the string that the widget will allow.</p>
<dt><code>setCDKEntryMin</code></p>
<dd> sets the minimum length of the string that the widget will allow.</p>
<dt><code>setCDKEntryPostProcess</code></p>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about post-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKEntryPreProcess</code></p>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about pre-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKEntryULChar</code></p>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKEntryURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKEntryValue</code></p>
<dd> sets the current value of the widget.</p>
<dt><code>setCDKEntryVerticalChar</code></p>
<dd> sets the vertical drawing character for the box to the given character.</dl>
<h2>KEY BINDINGS</h2>
<p> When the widget is activated there are several default key bindings which will help the user enter or manipulate the information quickly. The following table outlines the keys and their actions for this widget. </p>
<p> <center></p>
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
<td>Erases the contents of the widget.
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
<td> Exits the widget and returns a <i>char *</i> representing the information which was typed into the field. It also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td> Exits the widget and returns a <i>char *</i> representing the information which was typed into the field. It also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
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
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_process/">cdk_process</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
