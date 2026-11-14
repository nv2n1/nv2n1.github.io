---
title: "cdk_util(3)"
name: "cdk_util"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_util/"
description: "cdk_util – Cdk utility functions"
---

<h2>NAME</h2>
<p> cdk_util &#8211; Cdk utility functions</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

int CDKgetDirectoryContents(
    const char *directory,
    char ***list);
int CDKreadFile(
    const char *filename,
    char ***info);
void alignxy(
    WINDOW *window,
    int *xpos,
    int *ypos,
    int boxWidth,
    int boxHeight);
chtype *char2Chtype(
    const char *string,
    int *length,
    int *align);
EDisplayType char2DisplayType(
    const char *string);
int checkForLink(
    const char *line,
    char *filename);
char *chtype2String(
    const chtype *string);
void deleteCursesWindow(
    WINDOW *window);
void eraseCursesWindow(
    WINDOW *window);
int getListIndex(
    CDKSCREEN *screen,
    const char *title,
    CDK_CONST char **list,
    int listSize,
    boolean numbers);
char *getString(
    CDKSCREEN *screen,
    const char *title,
    const char *label,
    const char *init);
int justifyString(
    int fieldWidth,
    int mesglen,
    int justify);
int mode2Filetype(
    mode_t fileMode);
void moveCursesWindow(
    WINDOW *window,
    int xdiff,
    int ydiff);
int popupDialog(
    CDKSCREEN *screen,
    CDK_CONST char **mesg,
    int mesgCount,
    CDK_CONST char **buttons,
    int buttonCount);
void popupLabel(
    CDKSCREEN *win,
    CDK_CONST char **mesg,
    int count);
void popupLabelAttrib(
    CDKSCREEN *win,
    CDK_CONST char **mesg,
    int count,
    chtype attribute);
char *selectFile(
    CDKSCREEN *screen,
    const char *title);
int setWidgetDimension(
    int parentDim,
    int proposedDim,
    int adjustment);
void stripWhiteSpace(
    EStripType stripType,
    char *string);
int viewFile(
    CDKSCREEN *screen,
    const char *title,
    const char *filename,
    CDK_CONST char **buttons,
    int buttonCount);
int viewInfo(
    CDKSCREEN *screen,
    const char *title,
    CDK_CONST char **info,
    int size,
    CDK_CONST char **buttons,
    int buttonCount,
    boolean interpret);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> These are utility functions that one may use to initialize, build or customize widgets.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>CDKgetDirectoryContents</code></p>
<dd> opens and reads the contents of the given directory, filling the array <code>list</code> with the sorted contents of the directory. If the directory cannot be opened then it returns a value of -1.</p>
<dt><code>CDKreadFile</code></p>
<dd> Read the file <i>filename</i>, load the contents into a dynamically allocated array, storing its address via <i>info</i>. It returns the number of lines read if the file could be opened, -1 otherwise.</p>
<dt><code>alignxy</code></p>
<dd> Aligns a box on the given <i>window</i> with the height and width given. See cdk_position (3) for the interpretation of the <i>xpos</i>, <i>ypos</i>, <i>boxWidth</i> and <i>boxHeight</i>, parameters.</p>
<dt><code>char2Chtype</code></p>
<dd> Translate a character <i>string</i> with embedded format markers (e.g., &quot;&lt;/X/Y&gt;Blah Blah&quot;) to a null-terminated array of chtype&#8217;s. The length of the array is stored via the <i>length</i> parameter. The <code>align</code> parameter contains justification information (LEFT, CENTER, RIGHT). The caller is responsible for freeing the result.</p>
<dt><code>char2DisplayType</code></p>
<dd> Lookup the given name in <i>string</i> and return the equivalent display type. See also cdk_display (3).</p>
<dt><code>checkForLink</code></p>
<dd> Check if the given <i>line</i> is of the form</p>
<dl>
<dt>
<dd> &lt;F=<i>filename</i>&gt;</dl>
<dt>
<dd> If so, extract the filename from the line, storing it in the <i>filename</i> buffer (which must hold at least CDK_PATHMAX characters). Return nonzero if a filename is extracted.</p>
<dt><code>chtype2String</code></p>
<dd> Extract the characters and formatting information from a null-terminated array of chtype&#8217;s <i>string</i>. A dynamically allocated string is returned.</p>
<dt><code>deleteCursesWindow</code></p>
<dd> Safely delete a given window, i.e., first check if the <i>window</i> parameter is nonnull.</p>
<dt><code>eraseCursesWindow</code></p>
<dd> Safely erase a given window, i.e., first check if the <i>window</i> parameter is nonnull.</p>
<dt><code>getListIndex</code></p>
<dd> Display a scrollable list of strings in a dialog, allow the user to select one. Return the index in the list of the value selected. The <i>list</i> parameter contains the strings to display; there are <i>listSize</i> strings in the list. If <i>numbers</i> is true, the displayed list items will be numbered.</p>
<dt><code>getString</code></p>
<dd> pops up an entry widget with a title supplied by the value of the <code>title</code> parameter, a label supplied by the <code>label</code> parameter, and an initial value supplied by the <code>initialValue</code> parameter. It returns a pointer to the value typed in or NULL if the widget was exited early.</p>
<dt><code>justifyString</code></p>
<dd> Given a string length <i>mesglen</i>, the available field width <i>fieldWidth</i> and a justification type <i>justify</i>, return the number of characters by which to shift the string.</p>
<dt><code>mode2Filetype</code></p>
<dd> Given a file protection mode <i>fileMode</i>, return ignoring the file-type bits, i.e., ignoring the corresponding permissions data.</p>
<dt><code>moveCursesWindow</code></p>
<dd> Move a given <i>window</i> by the amounts in <i>xdiff</i> and <i>ydiff</i>.</p>
<dt><code>popupDialog</code></p>
<dd> creates a quick pop-up dialog box. Pass in the message in the <code>mesg</code> parameter, the size of the message in the <code>mesgCount</code> parameter, the button labels in the <code>buttons</code> parameter and the number of buttons in the <code>buttonCount</code> parameter. The dialog box will be centered on the screen.</p>
<dt><code>popupLabel</code></p>
<dd> creates a quick pop-up label widget. The message and the size of the message are passed in via the <code>mesg</code> and <code>count</code> parameters respectively. The label widget waits until the user hits a character and is centered on the screen.</p>
<dt><code>popupLabelAttrib</code></p>
<dd> Display a simple dialog with a list of <i>count</i> message strings <i>mesg</i>. Use the given <i>attribute</i> for the background of the dialog.</p>
<dt><code>selectFile</code></p>
<dd> Display a file-selection dialog. Return the selected filename, or null if none is selected. The caller should free the return-value.</p>
<dt><code>setWidgetDimension</code></p>
<dd> This is a helper function used to set the height/width of a widget:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> If the proposed dimension <i>proposedDim</i> is FULL or zero, the return value will be <i>parentDim</i>.</p>
<dt>&#8211;</p>
<dd> If the proposed dimension <i>proposedDim</i> is positive,</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> and it is larger than <i>parentDim</i>, return <i>proposedDim</i>,</p>
<dt>&#8211;</p>
<dd> otherwise return <i>proposedDim</i> plus <i>adjustment</i>.</dl>
</dl>
<dt>&#8211;</p>
<dd> If the proposed dimension <i>proposedDim</i> is negative, the return value will be <i>parentDim</i> plus <i>proposedDim</i>.</p>
<dt>&#8211;</p>
<dd> Otherwise, the return value will be <i>proposedDim</i>.</dl>
</dl>
<dt><code>stripWhiteSpace</code></p>
<dd> Strip whitespace from the front and/or back of the given <i>string</i>. The <i>stripType</i> parameter controls the type of stripping done: vFRONT, vBACK or vBOTH.</p>
<dt><code>viewFile</code></p>
<dd> Read the file specified by <i>filename</i> and display it in a CDKVIEWER window. The <i>title</i>, <i>buttons</i> and <i>buttonCount</i> are applied to the CDKVIEWER window. The viewer shows the contents of the file supplied by the <code>filename</code> value. The buttons on the file viewer are supplied by the <code>buttons</code> parameter. It returns the index of the button selected, or -1 if the file does not exist or if the widget was exited early.</dl>
<p> <center></p>
<table BORDER>
<tr VALIGN=top>
<td><code>Strip_Type</code></td>
<td>Result
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>vFRONT</td>
<td> This tells the function to remove all of the white space from the front of the given string.
</td>
</tr>
<tr VALIGN=top>
<td>vBACK</td>
<td> This tells the function to remove all of the white space from the back of the given string.
</td>
</tr>
<tr VALIGN=top>
<td>vBOTH</td>
<td> This tells the function to remove all of the white space from both the front and the back of the given string.
</td>
</tr>
</table>
<p></center></p>
<dl>
<dt><code>viewInfo</code></p>
<dd> Display the list of strings in <i>info</i> in a CDKVIEWER window. The number of strings is given by <i>size</i>. The <i>title</i>, <i>buttons</i> and <i>buttonCount</i> are applied to the CDKVIEWER window.</dl>
<h2>SEE ALSO</h2>
<p> cdk_dialog (3), cdk_display (3), cdk_position (3), cdk_misc (3). </p>
<h2>Index</h2>
