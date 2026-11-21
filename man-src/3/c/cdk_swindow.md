---

title: "cdk_swindow(3)"
name: "cdk_swindow"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_swindow/"
description: "cdk_swindow – a curses scrolling window widget."
---

<h2>NAME</h2>
<p> cdk_swindow &#8211; a curses scrolling window widget.</p>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>
void activateCDKSwindow(
    CDKSWINDOW *swindow,
    chtype *actions);
void addCDKSwindow(
    CDKSWINDOW *swindow,
    const char *info,
    int insertPosition);
void cleanCDKSwindow(
    CDKSWINDOW *swindow);
int execCDKSwindow(
    CDKSWINDOW *swindow,
    const char *command,
    int insertPosition);
void destroyCDKSwindow(
    CDKSWINDOW *swindow);
void drawCDKSwindow(
    CDKSWINDOW *swindow,
    boolean box);
void dumpCDKSwindow(
    CDKSWINDOW *swindow,
    const char *filename);
void eraseCDKSwindow(
    CDKSWINDOW *swindow);
void execCDKSwindow(
    CDKSWINDOW *swindow,
    char *command,
    int insertPosition);
boolean getCDKSwindowBox(
    CDKSWINDOW *swindow);
chtype **getCDKSwindowContents(
    CDKSWINDOW *swindow);
int injectCDKSwindow(
    CDKSWINDOW *swindow,
    chtype input);
void jumpToLineCDKSwindow(
    CDKSWINDOW *swindow,
    int line);
void loadCDKSwindowInformation(
    CDKSWINDOW *swindow);
void moveCDKSwindow(
    CDKSWINDOW *swindow,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKSWINDOW *newCDKSwindow(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    int height,
    int width,
    const char *title,
    int saveLines,
    boolean box,
    boolean shadow);
void positionCDKSwindow(
    CDKSWINDOW *swindow);
void saveCDKSwindowInformation(
    CDKSWINDOW *swindow);
void setCDKSwindow(
    CDKSWINDOW *swindow,
    CDK_CONST char **info,
    int lines,
    boolean box);
void setCDKSwindowBackgroundAttrib(
    CDKSWINDOW *swindow,
    chtype attribute);
void setCDKSwindowBackgroundColor(
    CDKSWINDOW *swindow,
    const char *color);
void setCDKSwindowBox(
    CDKSWINDOW *swindow,
    boolean boxWidget);
void setCDKSwindowBoxAttribute(
    CDKSWINDOW *swindow,
    chtype character);
void setCDKSwindowContents(
    CDKSWINDOW *swindow,
    char **info,
    int lines);
void setCDKSwindowHorizontalChar(
    CDKSWINDOW *swindow,
    chtype character);
void setCDKSwindowLLChar(
    CDKSWINDOW *swindow,
    chtype character);
void setCDKSwindowLRChar(
    CDKSWINDOW *swindow,
    chtype character);
void setCDKSwindowPostProcess(
    CDKSWINDOW *swindow,
    PROCESSFN callback,
    void *data);
void setCDKSwindowPreProcess(
    CDKSWINDOW *swindow,
    PROCESSFN callback,
    void *data);
void setCDKSwindowULChar(
    CDKSWINDOW *swindow,
    chtype character);
void setCDKSwindowURChar(
    CDKSWINDOW *swindow,
    chtype character);
void setCDKSwindowVerticalChar(
    CDKSWINDOW *swindow,
    chtype character);
void trimCDKSwindow(
    CDKSWINDOW *swindow,
    int start,
    int finish);
</code></pre>
</dl>
<p> The Cdk scrolling window (swindow) widget can be used to display messages. The following functions create or manipulate the Cdk swindow box widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKSwindow</code></dt>
<dd> function activates the swindow widget and lets the user interact with the widget. The parameter <code>swindow</code> is a pointer to a non-NULL swindow widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> or <i>TAB</i> then this function will return 1. It will also set the widget data <i>exitType</i> to <i>vNORMAL</i>. If the character entered into this widget was <i>ESCAPE</i> then the widget will return a value of -1 and the widget data <i>exitType</i> will be set to <i>vESCAPE_HIT</i>.</dd>
<dt><code>addCDKSwindow</code></dt>
<dd> adds information to a scrolling window. The information is supplied by the <code>info</code> parameter. The information is immediately added to the scrolling window. The position of the new information is governed by the value of the parameter <code>insertPosition</code>. This parameter may be two values: <i>TOP</i> or <i>BOTTOM</i>.</dd>
<dt><code>cleanCDKSwindow</code></dt>
<dd> clears the information from the window.</dd>
<dt><code>destroyCDKSwindow</code></dt>
<dd> removes the widget from the screen and frees memory the object used.</dd>
<dt><code>drawCDKSwindow</code></dt>
<dd> draws the swindow widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</dd>
<dt><code>dumpCDKSwindow</code></dt>
<dd> saves the contents of the scrolling window into the file specified by the <code>filename</code> parameter. It returns -1 on failure, and the number of lines saved if the dump was successful.</dd>
<dt><code>eraseCDKSwindow</code></dt>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</dd>
<dt><code>execCDKSwindow</code></dt>
<dd> allows the user to execute a shell command and have the output of the shell command direct itself to the scrolling window. The <code>command</code> parameter is the command to execute. The <code>insertPosition</code> parameter tells where the output will be inserted within the scrolling window.</dd>
<dt><code>getCDKSwindowBox</code></dt>
<dd> returns true if the widget will be drawn with a box around it.</dd>
<dt><code>getCDKSwindowContents</code></dt>
<dd> returns the contents of the scrolling window. The parameter <code>lines</code> will be set to the number of lines returned.</dd>
<dt><code>injectCDKSwindow</code></dt>
<dd> injects a single character into the widget. The parameter <code>swindow</code> is a pointer to a non-NULL swindow widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</dd>
<dl>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></dt>
<dd> the function returns 1. The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</dd>
<dt><i>ESCAPE</i></dt>
<dd> the function returns -1. The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</dd>
<dt>Otherwise</dt>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns -1. The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dd></dl>
</dl>
<dt><code>jumpToLineCDKSwindow</code></dt>
<dd> moves the scrolling window to the given line. The parameter <code>line</code> may be an integer or one of the two predefined values <i>TOP</i> and <i>BOTTOM</i>.</dd>
<dt><code>loadCDKSwindowInformation</code></dt>
<dd> allows the user to load the contents of a file into the scrolling window. This function is interactive, and will ask for a filename.</dd>
<dt><code>moveCDKSwindow</code></dt>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i> (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</dd>
<dt><code>newCDKSwindow</code></dt>
<dd> creates a swindow widget and returns a pointer to it. Parameters:</dd>
<dl>
<dl>
<dt><code>screen</code></dt>
<dd> is the screen you wish this widget to be placed in.</dd>
<dt><code>xpos</code></dt>
<dd> controls the placement of the object along the horizontal axis. It may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>.</dd>
<dt><code>ypos</code></dt>
<dd> controls the placement of the object along the vertical axis. It may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</dd>
<dt><code>height</code> and</dt>
<dd>
</dd><dt><code>width</code></dt>
<dd> control the height and width of the widget. If you provide a value of zero for either of the height or the width, the widget will be created with the full width and height of the screen. If you provide a negative value, the widget will be created the full height or width minus the value provided.</dd>
<dt><code>title</code></dt>
<dd> is the string to display at the top of the widget. The title can be more than one line; just provide a carriage return character at the line break.</dd>
<dt><code>saveLines</code></dt>
<dd> is the number of lines to save before throwing information away.</dd>
<dt><code>box</code></dt>
<dd> is true if the widget should be drawn with a box around it.</dd>
<dt>The <code>shadow</code></dt>
<dd> turns the shadow on or off around this widget.</dd></dl>
</dl>
<dt>
</dt><dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</dd>
<dt><code>positionCDKSwindow</code></dt>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</dd>
<dt><code>saveCDKSwindowInformation</code></dt>
<dd> allows the user to save the contents of the scrolling window into a file. This function is interactive, and will ask for a filename.</dd>
<dt><code>setCDKSwindow</code></dt>
<dd> lets the programmer modify certain elements of an existing swindow widget. The parameter <code>info</code> is a <i>char **</i> of the information to set in the scrolling window; <code>lines</code> is the number of lines being added. The other parameter names correspond to the same parameter names listed in the <code>newCDKSwindow</code> function.</dd>
<dt><code>setCDKSwindowBackgroundAttrib</code></dt>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</dd>
<dt><code>setCDKSwindowBackgroundColor</code></dt>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</dd>
<dt><code>setCDKSwindowBox</code></dt>
<dd> sets whether the widget will be drawn with a box around it.</dd>
<dt><code>setCDKSwindowBoxAttribute</code></dt>
<dd> sets the attribute of the box.</dd>
<dt><code>setCDKSwindowContents</code></dt>
<dd> lets the programmer modify certain elements of an existing swindow widget. The parameter <code>info</code> is a <i>char **</i> of the information to set in the scrolling window; <code>lines</code> is the number of lines being added.</dd>
<dt><code>setCDKSwindowHorizontalChar</code></dt>
<dd> sets the horizontal drawing character for the box to the given character.</dd>
<dt><code>setCDKSwindowLLChar</code></dt>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKSwindowLRChar</code></dt>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKSwindowPostProcess</code></dt>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about post-processing see <i>cdk_process (3)</i>.</dd>
<dt><code>setCDKSwindowPreProcess</code></dt>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about pre-processing see <i>cdk_process (3)</i>.</dd>
<dt><code>setCDKSwindowULChar</code></dt>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKSwindowURChar</code></dt>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</dd>
<dt><code>setCDKSwindowVerticalChar</code></dt>
<dd> sets the vertical drawing character for the box to the given character.</dd>
<dt><code>trimCDKSwindow</code></dt>
<dd> removes information from a scrolling window. The parameters <code>start</code> and <code>end</code> state where to start cutting from and where to stop. The first element in the scrolling window starts at index 0.</dd></dl>
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
<td>Scrolls the window left one column.
</td>
</tr>
<tr VALIGN=top>
<td>Right Arrow</td>
<td>Scrolls the window right one column.
</td>
</tr>
<tr VALIGN=top>
<td>Up Arrow</td>
<td>Scrolls the window up one row.
</td>
</tr>
<tr VALIGN=top>
<td>Down Arrow</td>
<td>Scrolls the window down one row.
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
<td>
</td>
</tr>
<tr VALIGN=top>
<td>b</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>B</td>
<td>Scroll the window backward one page.
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
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Space</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>f</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>F</td>
<td>Scroll the window forward one page.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Home</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>|</td>
<td>Scroll the list to the left margin.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>End</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>$</td>
<td>Scroll the list to the right margin.
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
<td>Move to the top of the scrolling window.
</td>
</tr>
<tr VALIGN=top>
<td>&gt;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>G</td>
<td>Move to the bottom of the scrolling window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>L</td>
<td>Load a file into the scrolling window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>s</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>S</td>
<td> Save the contents of the scrolling window into a file.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Set the widget&#8217;s <i>exitType</i> to <i>vNORMAL</i>, exit the widget and return 1.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td> Set the widget&#8217;s <i>exitType</i> to <i>vNORMAL</i>, exit the widget and return 1.
</td>
</tr>
<tr VALIGN=top>
<td>Escape</td>
<td> Set the widget&#8217;s <i>exitType</i> to <i>vESCAPE_HIT</i>, exit the widget and return -1.
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
</table>
<p></center></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
