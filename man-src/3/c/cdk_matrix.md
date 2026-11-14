---
title: "cdk_matrix(3)"
name: "cdk_matrix"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_matrix/"
description: "cdk_matrix – curses matrix widget."
---

<h2>NAME</h2>
<p> cdk_matrix &#8211; curses matrix widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

int activateCDKMatrix(
    CDKMATRIX *matrix,
    chtype *actions);
void cleanCDKMatrix(
    CDKMATRIX *matrix);
void cleanCDKMatrixCell(
    CDKMATRIX *matrix,
    int row,
    int col);
void destroyCDKMatrix(
    CDKMATRIX *matrix);
void drawCDKMatrix(
    CDKMATRIX *matrix,
    boolean box);
void eraseCDKMatrix(
    CDKMATRIX *matrix);
boolean getCDKMatrixBox(
    CDKMENTRY *matrix);
char *getCDKMatrixCell(
    CDKMATRIX *matrix,
    int row,
    int col);
int getCDKMatrixCol(
    CDKMENTRY *matrix);
int getCDKMatrixRow(
    CDKMENTRY *matrix);
int injectCDKMatrix(
    CDKMATRIX *matrix,
    chtype input);
int jumpToCell(
    CDKMATRIX *matrix,
    int row,
    int col);
void moveCDKMatrix(
    CDKMATRIX *matrix,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
int moveToCDKMatrixCell(
    CDKMATRIX *matrix,
    int row,
    int col);
CDKMATRIX *newCDKMatrix(
    CDKSCREEN *cdkscreen,
    int xpos,
    int ypos,
    int screenRows,
    int screenCols,
    int actualRows,
    int actualCols,
    const char *title,
    CDK_CONST char **rowTitles,
    CDK_CONST char **colTitles,
    int *columnWidths,
    int *columnTypes,
    int rowSpace,
    int colSpace,
    chtype filler,
    int dominantAttribute,
    boolean boxMatrix,
    boolean boxCell,
    boolean shadow);
void positionCDKMatrix(
    CDKMATRIX *matrix);
void setCDKMatrix(
    CDKMATRIX *matrix,
    char *info[MAX_MATRIX_ROWS][MAX_MATRIX_COLS],
    int rows,
    int *columnLengths);
void setCDKMatrixBackgroundAttrib(
    CDKMATRIX *matrix,
    chtype attribute);
void setCDKMatrixBackgroundColor(
    CDKMATRIX *matrix,
    const char *color);
void setCDKMatrixBox(
    CDKMENTRY *matrix,
    boolean boxWidget);
void setCDKMatrixBoxAttribute(
    CDKMATRIX *matrix,
    chtype character);
void setCDKMatrixCB(
    CDKMATRIX *matrix,
    MATRIXCB callbackFunction);
int setCDKMatrixCell(
    CDKMATRIX *matrix,
    int row,
    int col,
    const char *value);
void setCDKMatrixCells(
    CDKMATRIX *matrix,
    CDK_CONST char **info,
    int rows,
    int cols,
    int *columnLengths);
void setCDKMatrixHorizontalChar(
    CDKMATRIX *matrix,
    chtype character);
void setCDKMatrixLLChar(
    CDKMATRIX *matrix,
    chtype character);
void setCDKMatrixLRChar(
    CDKMATRIX *matrix,
    chtype character);
void setCDKMatrixPostProcess(
    CDKMATRIX *matrix,
    PROCESSFN callback,
    void *data);
void setCDKMatrixPreProcess(
    CDKMATRIX *matrix,
    PROCESSFN callback,
    void *data);
void setCDKMatrixULChar(
    CDKMATRIX *matrix,
    chtype character);
void setCDKMatrixURChar(
    CDKMATRIX *matrix,
    chtype character);
void setCDKMatrixVerticalChar(
    CDKMATRIX *matrix,
    chtype character);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk matrix widget creates a matrix widget. The following are functions which create or manipulate the Cdk matrix box widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKMatrix</code></p>
<dd> activates the matrix widget and lets the user interact with the widget. The parameter <code>matrix</code> is a pointer to a non-NULL matrix widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> then this function will return 1. It will also set the widget data <i>exitType</i> to <i>vNORMAL</i>. If the character entered into this widget was <i>ESCAPE</i> then the widget will return a value of -1 and the widget data <i>exitType</i> will be set to <i>vESCAPE_HIT</i>. The matrix cell contents can be retrieved by using the <code>info</code> array of the matrix widget.</p>
<dt><code>cleanCDKMatrix</code></p>
<dd> clears the information from all cells of the matrix.</p>
<dt><code>cleanCDKMatrixCell</code></p>
<dd> clears the information from the specified cell of the matrix.</p>
<dt><code>destroyCDKMatrix</code></p>
<dd> removes the widget from the screen and frees memory the object used.</p>
<dt><code>drawCDKMatrix</code></p>
<dd> draws the matrix widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</p>
<dt><code>eraseCDKMatrix</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKMatrixBox</code></p>
<dd> returns true if the widget will be drawn with a box around it.</p>
<dt><code>getCDKMatrixCell</code></p>
<dd> returns the contents of the cell located by the <code>row</code> and <code>col</code> pair.</p>
<dt><code>getCDKMatrixCol</code></p>
<dd> returns the current column index.</p>
<dt><code>getCDKMatrixRow</code></p>
<dd> returns the current row index.</p>
<dt><code>injectCDKMatrix</code></p>
<dd> injects a single character into the widget. The parameter <code>matrix</code> is a pointer to a non-NULL matrix widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></p>
<dd> the function returns 1. The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</p>
<dt><i>ESCAPE</i></p>
<dd> the function returns -1. The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</p>
<dt>Otherwise</p>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns -1. The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dl>
</dl>
<dt>
<dd> The matrix cell contents can be retrieved by using the <code>info</code> array of the matrix widget.</p>
<dt><code>jumpToCell</code></p>
<dd> provides an interactive method of moving to a cell. It pops up a scale widget and asks which cell the user wants to go to. Then it performs the jump.</p>
<dt><code>moveCDKMatrix</code></p>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>moveToCDKMatrixCell</code></p>
<dd> jumps to the given cells dictated by the parameters <code>row</code> and <code>col</code>. It returns a value of <i>TRUE</i> or <i>FALSE</i> depending if the move was successful.</p>
<dt><code>newCDKMatrix</code></p>
<dd> creates a matrix widget and returns a pointer to it. Parameters:</p>
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
<dt><code>screenRows</code> and</p>
<dd>
<dt><code>screenCols</code></p>
<dd> are the number of rows and columns to be displayed on the screen respectively.</p>
<dt><code>actualRows</code> and</p>
<dd>
<dt><code>actualCols</code></p>
<dd> are the number of actual rows and columns the matrix has.</p>
<dt><code>title</code></p>
<dd> is the string which will be displayed at the top of the widget. The title can be more than one line; just provide a carriage return character at the line break.</p>
<dt><code>rowTitles</code> and</p>
<dd>
<dt><code>colTitles</code></p>
<dd> are the titles along the row and columns respectively.</p>
<dt><code>columnWidths</code></p>
<dd> is an array of integers stating how wide the individual columns are to be.</p>
<dt><code>columnTypes</code></p>
<dd> is an array of integers which correspond to the individual column display types. The values of the array should be assigned a value of type <i>EDisplayType</i>. See <code>cdk_display (3)</code> for legal values of <i>EDisplayType</i>.</p>
<dt><code>rowSpace</code> and</p>
<dd>
<dt><code>colSpace</code></p>
<dd> dictate how much white space is to be between rows and columns respectively.</p>
<dt><code>filler</code></p>
<dd> is the character to use in empty space within a cell.</p>
<dt><code>dominantAttribute</code></p>
<dd> states which (the rows or the columns) will have the dominant character attributes. This is stated when a cell has both a row attribute and a column attribute. If the value of the parameter <code>dominantAttribute</code> is set to <code>ROW</code> then the attribute of the row will be displayed. If it is set to <code>COL</code> then the column&#8217;s attributes will be displayed instead.</p>
<dt><code>boxMatrix</code></p>
<dd> is true if the widget should be drawn with a box around it.</p>
<dt><code>boxCell</code></p>
<dd> is true if the individual cells should have boxes drawn around them.</p>
<dt><code>shadow</code></p>
<dd> turns the shadow on or off around this widget.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKMatrix</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>setCDKMatrix</code></p>
<dd> lets the programmer modify certain elements of an existing matrix widget. The parameter <code>info</code> is an array of <i>char *</i> which contains the cell information. The parameter <code>rows</code> has the number of rows the parameter <code>info</code> contains, while <code>columnLengths</code> has the lengths of the individual columns in <code>info</code>.</p>
<dt>
<dd> Do not use this function. It is obsolete, provided only for compatibility with older versions of CDK. Use <code>setCDKMatrixCells</code>.</p>
<dt><code>setCDKMatrixBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKMatrixBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</p>
<dt><code>setCDKMatrixBox</code></p>
<dd> sets whether the widget will be drawn with a box around it.</p>
<dt><code>setCDKMatrixBoxAttribute</code></p>
<dd> sets the attribute of the box.</p>
<dt><code>setCDKMatrixCB</code></p>
<dd> allows the programmer to set a different widget input handler. The parameter <code>callbackFunction</code> is of type <i>MATRIXCB</i>. The default function is <i>CDKMatrixCallBack</i>.</p>
<dt><code>setCDKMatrixCell</code></p>
<dd> sets the contents of the cell located by the <code>row</code> and <code>col</code> pair. The value of the cell will be set to <code>value</code>.</p>
<dt><code>setCDKMatrixCells,</code></p>
<dd> lets the programmer initialize elements of an existing matrix widget. The parameter <code>info</code> is an array of <i>char *</i> which contains the cell information. The parameter <code>rows</code> has the number of rows The parameter <code>cols</code> has the number of columns the parameter <code>info</code> contains, while <code>columnLengths</code> has the lengths of the individual columns in <code>info</code>.</p>
<dt><code>setCDKMatrixHorizontalChar</code></p>
<dd> sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKMatrixLLChar</code></p>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKMatrixLRChar</code></p>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKMatrixPostProcess</code></p>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about post-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKMatrixPreProcess</code></p>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about pre-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKMatrixULChar</code></p>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKMatrixURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKMatrixVerticalChar</code></p>
<dd> sets the vertical drawing character for the box to the given character.</dl>
<h2>KEY BINDINGS</h2>
<p> When the widget is activated there are several default key bindings which will help the user enter or manipulate the information quickly. The following table outlines the keys and their actions for this widget. <center></p>
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
<td>Moves one cell to the left.
</td>
</tr>
<tr VALIGN=top>
<td>Right Arrow</td>
<td>Moves the cell to the right.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td>Moves the cell to the right.
</td>
</tr>
<tr VALIGN=top>
<td>Up Arrow</td>
<td>Moves one cell up.
</td>
</tr>
<tr VALIGN=top>
<td>Down Arrow</td>
<td>Moves one cell down.
</td>
</tr>
<tr VALIGN=top>
<td>Next Page</td>
<td>Moves one page forward.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-F</td>
<td>Moves one page forward.
</td>
</tr>
<tr VALIGN=top>
<td>Prev Page</td>
<td>Moves one page backward.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-B</td>
<td>Moves one page backward.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-G</td>
<td> Calls the function <code>jumpToCell</code> and requests which cell the user wishes to jump to.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-P</td>
<td> Pastes whatever is in the paste buffer, into the current cell.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-K</td>
<td> Cuts the contents from the current cell and saves a copy in the paste buffer.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-T</td>
<td> Copies the contents of the current cell into the paste buffer.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-E</td>
<td>Erases the contents of the current cell.
</td>
</tr>
<tr VALIGN=top>
<td>Delete</td>
<td> Deletes the character before the cursor, moves cursor left. There is no function to delete the character at the cursor since there are no functions for moving the cursor within the edited text.
</td>
</tr>
<tr VALIGN=top>
<td>Backspace</td>
<td> Deletes the character before cursor, moves cursor left.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-H</td>
<td>Deletes the character before the cursor.
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Exits the widget and returns 1. This also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Escape</td>
<td> Exits the widget and returns -1. This also sets the widget data <i>exitType</i> to <i>vESCAPE_HIT</i>.
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
