---
title: "cdk_fselect(3)"
name: "cdk_fselect"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_fselect/"
description: "cdk_fselect – curses file selector widget."
---

<h2>NAME</h2>
<p> cdk_fselect &#8211; curses file selector widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

char *activateCDKFselect(
    CDKFSELECT *fselect,
    chtype *actions);
void deleteFileCB(
    EObjectType objectType,
    void *object,
    void *clientData);
void destroyCDKFselect(
    CDKFSELECT *fselect);
void drawCDKFselect(
    CDKFSELECT *fselect,
    boolean box);
void eraseCDKFselect(
    CDKFSELECT *fselect);
boolean getCDKFselectBox(
    CDKFSELECT *fselect);
char **getCDKFselectContents(
    CDKFSELECT *widget,
    int *size);
int getCDKFselectCurrentItem(
    CDKFSELECT *widget);
char *getCDKFselectDirAttribute(
    CDKFSELECT *fselect);
char **getCDKFselectDirContents(
    CDKFSELECT *fselect,
    int *count);
char *getCDKFselectDirectory(
    CDKFSELECT *fselect);
char *getCDKFselectFileAttribute(
    CDKFSELECT *fselect);
chtype getCDKFselectFillerChar(
    CDKFSELECT *fselect);
chtype getCDKFselectHighlight(
    CDKFSELECT *fselect);
char *getCDKFselectLinkAttribute(
    CDKFSELECT *fselect);
char *getCDKFselectSocketAttribute(
    CDKFSELECT *fselect);
char *injectCDKFselect(
    CDKFSELECT *fselect,
    chtype input);
void moveCDKFselect(
    CDKFSELECT *fselect,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKFSELECT *newCDKFselect(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    int height,
    int width,
    const char *title,
    const char *label,
    chtype fieldAttribute,
    chtype fillerCharacter,
    chtype highlight,
    const char *dirAttribute,
    const char *fileAttribute,
    const char *linkAttribute,
    const char *sockAttribute,
    boolean box,
    boolean shadow);
void positionCDKFselect(
    CDKFSELECT *fselect);
void setCDKFselect(
    CDKFSELECT *fselect,
    const char *directory,
    chtype fieldAttribute,
    chtype fillerCharacter,
    chtype highlight,
    const char *dirAttribute,
    const char *fileAttribute,
    const char *linkAttribute,
    const char *sockAttribute,
    boolean box);
void setCDKFselectBackgroundAttrib(
    CDKFSELECT *fselect,
    chtype attribute);
void setCDKFselectBackgroundColor(
    CDKFSELECT *fselect,
    const char *color);
void setCDKFselectBox(
    CDKFSELECT *fselect,
    boolean box);
void setCDKFselectBoxAttribute(
    CDKFSELECT *fselect,
    chtype character);
void setCDKFselectContents(
    CDKFSELECT *widget,
    CDK_CONST char **list,
    int listSize);
void setCDKFselectCurrentItem(
    CDKFSELECT *widget,
    int item);
void setCDKFselectDirAttribute(
    CDKFSELECT *fselect,
    const char *attribute);
int setCDKFselectDirContents(
    CDKFSELECT *fselect);
int setCDKFselectDirectory(
    CDKFSELECT *fselect,
    const char *directory);
void setCDKFselectFileAttribute(
    CDKFSELECT *fselect,
    const char *attribute);
void setCDKFselectFillerChar(
    CDKFSELECT *fselect,
    chtype filler);
void setCDKFselectHighlight(
    CDKFSELECT *fselect,
    chtype highlight);
void setCDKFselectHorizontalChar(
    CDKFSELECT *fselect,
    chtype character);
void setCDKFselectLLChar(
    CDKFSELECT *fselect,
    chtype character);
void setCDKFselectLRChar(
    CDKFSELECT *fselect,
    chtype character);
void setCDKFselectLinkAttribute(
    CDKFSELECT *fselect,
    const char *attribute);
void setCDKFselectSocketAttribute(
    CDKFSELECT *fselect,
    const char *attribute);
void setCDKFselectULChar(
    CDKFSELECT *fselect,
    chtype character);
void setCDKFselectURChar(
    CDKFSELECT *fselect,
    chtype character);
void setCDKFselectVerticalChar(
    CDKFSELECT *fselect,
    chtype character);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk file selector widget creates a widget which allows a user to interact with the Unix file system. This widget allows the user to traverse the file system and even delete files. (See <i>NOTES</i> below for more information)</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKFselect</code></p>
<dd> activates the file selector widget and lets the user interact with the widget. The parameter <code>fselect</code> is a pointer to a non-NULL file selector widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> or <i>TAB</i> then this function will return a <i>char *</i> representing the information typed into the widget and the widget data <i>exitType</i> will be set to <i>vNORMAL</i>. If the character entered was <i>ESCAPE</i> then the function will return <i>NULL</i> pointer and the widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>. void deleteFileCB (EObjectType objectType GCC_UNUSED, void *object, void *clientData)</p>
<dt><code>deleteFileCB</code></p>
<dd> Prompts the user to confirm, and deletes the current item in the file-list.</p>
<dt><code>destroyCDKFselect</code></p>
<dd> removes the widget from the screen and frees memory the object used.</p>
<dt><code>drawCDKFselect</code></p>
<dd> draws the fselect widget on the screen. If the <code>box</code> option is true, the widget is drawn with a box.</p>
<dt><code>eraseCDKFselect</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKFselectBox</code></p>
<dd> returns true if the widget will be drawn with a box around it.</p>
<dt><code>getCDKFselectContents</code></p>
<dd> returns the directory-contents (which are formatted), and sets the number of entries via the <i>size</i> parameter.</p>
<dt><code>getCDKFselectCurrentItem</code></p>
<dd> returns the current position in the scroll-widget.</p>
<dt><code>getCDKFselectDirAttribute</code></p>
<dd> returns the attribute that directories are drawn with in the scrolling region of the widget.</p>
<dt><code>getCDKFselectDirContents</code></p>
<dd> returns the list of files and the corresponding count as a side-effect. If no files are found, this function returns zero, otherwise one.</p>
<dt><code>getCDKFselectDirectory</code></p>
<dd> returns the current directory of the widget.</p>
<dt><code>getCDKFselectFileAttribute</code></p>
<dd> returns the attribute that plain files are drawn with in the scrolling region of the widget.</p>
<dt><code>getCDKFselectFillerChar</code></p>
<dd> returns the character being used as the filler character in the entry field portion of the widget.</p>
<dt><code>getCDKFselectHighlight</code></p>
<dd> returns the attribute of the highlight bar of the scrolling list portion of the widget.</p>
<dt><code>getCDKFselectLinkAttribute</code></p>
<dd> returns the attribute that symbolic links are drawn with in the scrolling region of the widget.</p>
<dt><code>getCDKFselectSocketAttribute</code></p>
<dd> returns the attribute that sockets are drawn with in the scrolling region of the widget.</p>
<dt><code>injectCDKFselect</code></p>
<dd> injects a single character into the widget. The parameter <code>fselect</code> is a pointer to a non-NULL file selector widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</p>
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
<dt><code>moveCDKFselect</code></p>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>newCDKFselect</code></p>
<dd> creates an fselect widget and returns a pointer to it. Parameters:</p>
<dl>
<dt>
<dd>
<dl>
<dt>The <code>screen</code> parameter</p>
<dd> is the screen you wish this widget to be placed in.</p>
<dt>The parameter <code>xpos</code></p>
<dd> controls the placement of the object along the horizontal axis. This parameter may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>.</p>
<dt><code>ypos</code></p>
<dd> controls the placement of the object along the vertical axis. It may be an integer value or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</p>
<dt><code>height</code> and</p>
<dd>
<dt><code>width</code></p>
<dd> control the height and width of the widget. If you provide a value of zero for either of the height or the width, the widget will be created with the full width and height of the screen. If you provide a negative value, the widget will be created the full height or width minus the value provided.</p>
<dt><code>title</code></p>
<dd> is the string which will be displayed at the top of the widget. The title can be more than one line; just provide a carriage return character at the line break.</p>
<dt><code>label</code></p>
<dd> is the text to use as the label of the file selector.</p>
<dt><code>fieldAttribute</code></p>
<dd> is the attribute of the entry field at the top of the widget;</p>
<dt><code>fillerCharacter</code></p>
<dd> is the filler character for the entry field.</p>
<dt><code>highlight</code></p>
<dd> is the highlight attribute on the scrolling list.</p>
<dt><code>dirAttribute</code>,</p>
<dd>
<dt><code>fileAttribute</code>,</p>
<dd>
<dt><code>linkAttribute</code> and</p>
<dd>
<dt><code>sockAttribute</code></p>
<dd> are the attributes of directories, files, links, and sockets found in the directory list.</p>
<dt><code>box</code></p>
<dd> is true if the widget should be drawn with a box around it.</p>
<dt><code>shadow</code></p>
<dd> turns the shadow on or off around this widget.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKFselect</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>setCDKFselect</code></p>
<dd> lets the programmer modify certain elements of an existing fselect widget. The parameter names correspond to the same parameter names listed in the <code>newCDKFselect</code> function.</p>
<dt><code>setCDKFselectBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKFselectBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</p>
<dt><code>setCDKFselectBox</code></p>
<dd> sets whether the widget will be drawn with a box around it.</p>
<dt><code>setCDKFselectBoxAttribute</code></p>
<dd> sets the attribute of the box.</p>
<dt><code>setCDKFselectContents</code></p>
<dd> sets the contents of the widget.</p>
<dt><code>setCDKFselectCurrentItem</code></p>
<dd> set the current position in the scroll-widget.</p>
<dt><code>setCDKFselectDirAttribute</code></p>
<dd> sets the attribute that directories will be drawn with in the scrolling region of the widget. <code>setCDKFselectDirContents</code> This creates a list of the files in the current directory. See <code>getCDKFselectDirContentsFP.</p>
<dt>setCDKFselectDirectory</code></p>
<dd> sets the current directory of the widget.</p>
<dt><code>setCDKFselectFileAttribute</code></p>
<dd> sets the attribute that plain files will be drawn with in the scrolling region of the widget.</p>
<dt><code>setCDKFselectFillerChar</code></p>
<dd> sets the character to use when drawing the entry field portion of the widget.</p>
<dt><code>setCDKFselectHighlight</code></p>
<dd> sets the attribute of the highlight bar of the scrolling list portion of the widget.</p>
<dt><code>setCDKFselectHorizontalChar</code></p>
<dd> sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKFselectLLChar</code></p>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKFselectLRChar</code></p>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKFselectLinkAttribute</code></p>
<dd> sets the attribute that symbolic links will be drawn with in the scrolling region of the widget.</p>
<dt><code>setCDKFselectSocketAttribute</code></p>
<dd> sets the attribute that sockets will be drawn with in the scrolling region of the widget.</p>
<dt><code>setCDKFselectULChar</code></p>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKFselectURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKFselectVerticalChar</code></p>
<dd> sets the vertical drawing character for the box to the given character.</dl>
<h2>KEY BINDINGS</h2>
<p> When the widget is activated there are several default key bindings which will help the user enter or manipulate the information quickly. Since this widget is built from both the scrolling list widget and the entry field widget, the key bindings are the same for the respective fields. The extra key bindings are listed below. </p>
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
<td>CTRL-^</td>
<td>Displays statistics about the current filename.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td>Tries to complete the current filename.
</td>
</tr>
<tr VALIGN=top>
<td>Up Arrow</td>
<td>Scrolls the scrolling list up one line.
</td>
</tr>
<tr VALIGN=top>
<td>Down Arrow</td>
<td>Scrolls the scrolling list down one line.
</td>
</tr>
<tr VALIGN=top>
<td>Page Up</td>
<td>Scrolls the scrolling list up one page.
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-B</td>
<td>Scrolls the scrolling list up one page.
</td>
</tr>
<tr VALIGN=top>
<td>Page Down</td>
<td> Scrolls the scrolling list down one page.
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-F</td>
<td> Scrolls the scrolling list down one page.
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Returns the filename in the entry field of the file selector. It also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Escape</td>
<td> Exits the widget and returns a <i>NULL</i> pointer. It also sets the widget data <i>exitType</i> to <i>vESCAPE_HIT</i>.
</td>
</tr>
</table>
<p></center></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3)</p>
<h2>NOTES</h2>
<p> This widget is created from the scrolling list widget and the entry field widget. This is a good example on how to build your own widgets using the base widgets provided in this distribution. In order for you to delete files using the file selector, you must add the following call into your program. (the character X is the character you wish to use to tell the file selector you want to delete a file.)</p>
<dl>
<dt>
<dd> <code>bindCDKObject (vSCROLL, fselect-&gt;filelist, X, deleteFile, fselect);</code></dl>
<p> where <code>fselect</code> is a pointer to the object. This was originally turned on, but I thought it better to put the control of file deletion on an &#8216;as-need&#8217; basis. </p>
<h2>Index</h2>
