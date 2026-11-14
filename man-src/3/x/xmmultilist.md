---
title: "xmmultilist(3)"
name: "xmmultilist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmultilist/"
description: "XmMultiList — The Multi-column List widget"
---

<p><code>XmMultiList</code> &#8212; The Multi-column List widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MultiList.h&gt;</pre>
<h2>Description</h2>
<p>This widget contains a multi-column list with headers along the top and a search area along the bottom. The list has scrollbars along the right and bottom edges that allow vertical and horizontal scrolling both by column and by pixel. The portion of the list data that is currently visible can be altered by scrollbar actions, widget resource setting and the redisplay of the list data after a string search has been successful. The sorting of elements within a particular column is also supported. To sort the list by the elements in a given column, select the column&#8217;s title. </p>
<p> To search for a particular string in the list, type the string value to be searched for in the list&#8217;s associated text field and then press the &quot;Find&quot; pushbutton. The search for the string begins in the currently selected row, after the location of the previously searched for string, or at the first column and first row if there is no column selected. If the string is not found in that row, then the search continues through all rows after and then before, the currently selected row. If the string is found, the display of the list is adjusted to make the string visible. If the string was not found, or if the string is visible, the application will issue a warning beep. </p>
<p> Pointer button one allows the user to select a row or a column for sorting. The callbacks on the doubleClickCallback list are called when the user double clicks pointer button one. If the list data can contain a row pixmap to display at the extreme left of the row.</p>
<h3>Classes</h3>
<p>MultiList inherits behavior, resources, and traits from <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, and <code>XmManager</code>. </p>
<p> The class pointer is <code>xmMultiListWidgetClass</code>. </p>
<p> The class name is <code>XmMultiList</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmMultiList Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNcolumnTitles</td>
<td>XmCColumnTitles</td>
<td>XmString *</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdoubleClickCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNentryData</td>
<td>XmCEntryData</td>
<td>XtPointer</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfindLabel</td>
<td>XmCFindLabel</td>
<td>XmString</td>
<td>Find</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfirstColumn</td>
<td>XmCFirstLocation</td>
<td>short</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfirstColumnPixmaps</td>
<td>XmCFirstColumnPixmaps</td>
<td>Boolean</td>
<td>False</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfirstRow</td>
<td>XmCFirstLocation</td>
<td>short</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfontList</td>
<td>XmCFontList</td>
<td>XmFontList</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNheight</td>
<td>XmCHeight</td>
<td>Dimension</td>
<td>300</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnumColumns</td>
<td>XmCNumColumns</td>
<td>short</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnumRows</td>
<td>XmCNumRows</td>
<td>short</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNselectedColumn</td>
<td>XmCSelectedColumn</td>
<td>short</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNselectionPolicy</td>
<td>XmCSelectionPolicy</td>
<td>unsigned char</td>
<td>XmEXTENDED_SELECT</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNshowFind</td>
<td>XmCShowFind</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsingleSelectionCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsortFunctions</td>
<td>XmCFunction</td>
<td>XmMultiListSortFunction **</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtitle</td>
<td>XmCTitle</td>
<td>XmString</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNwidth</td>
<td>XmCWidth</td>
<td>Dimension</td>
<td>300</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<dl COMPACT>
<dt><code>XmNcolumnTitles</code></p>
<dd>This is an array of length numColumns of strings displayed at the top of each column. The data is allocated and maintained by the client.</p>
<dt><code>XmNdoubleClickCallback</code></p>
<dd>All routines in this list will be called whenever the user double clicks on a row in the list.</p>
<dt><code>XmNentryData</code></p>
<dd>This resource is the data associated with each row in the list. The data is an array of XmMultiListRowInfo structures of length numRows allocated by the client. The data is allocated and maintained by the client. The XmMultiListRowInfo structure is defined below.</p>
<dt><code>XmNfindLabel</code></p>
<dd>The label to be shown on the find button.</p>
<dt><code>XmNfirstColumn</code></p>
<dd>This resource allows the client to adjust the current view of the list data to have a new top left column location. When setting this resource, firstRow should also be updated.</p>
<dt><code>XmNfirstColumnPixmaps</code></p>
<dd>This resource specifies that the pixmap stored in the row info structure should be used instead of XmMultiListRowInfo values[0]. If pixmaps are present, the rows may be dragged by pressing on the pixmap with pointer button three. If this resource is True, then values[0] is never referenced. If False, then the XmMultiListRowInfo data pixmap is never referenced.</p>
<dt><code>XmNfirstRow</code></p>
<dd>This resource allows the client to adjust the current view of the list data to have a new top left row location. When setting this resource, firstColumn should also be updated.</p>
<dt><code>XmNfontList</code></p>
<dd>This is an OSF/Motif style font list. The first font in this list will be used to display all text in the MultiList widget. The MultiList widget currently supports only one font.</p>
<dt><code>XmNheight</code></p>
<dd>This is the overall height value assigned to the MultiList widget. Modifying this resource will affect scrollbar size and location.</p>
<dt><code>XmNnumColumns</code></p>
<dd>
<dt><code>XmNnumRows</code></p>
<dd>These resources specify the number of columns and rows the widget expects to display. These resources are used as the maximum indices for many of the other resources in this widget. Care should be taken when modifying these resources to ensure that the other values have also been modified.</p>
<dt><code>XmNselectedColumn</code></p>
<dd>This is the index of the currently selected column. This also the column by which the list is being sorted.</p>
<dt><code>XmNselectionPolicy</code></p>
<dd>Defines the interpretation of the select action. This resource can have the values XmSINGLE_SELECT or XmEXTENDED_SELECT. Other values result in undefined behavior.</p>
<dt><code>XmNshowFind</code></p>
<dd>This boolean manages and unmanages the find button</p>
<dt><code>XmNsingleSelectionCallback</code></p>
<dd>All routines in this list will be called whenever the user clicks on a line in the list. A pointer to the XmMultiListRowInfo structure corresponding to the line selected is passed as call_data. If in extended select mode the value of call_data is undefined.</p>
<dt><code>XmNsortFunctions</code></p>
<dd>This is an array of functions, one for each column, called to determine the ordering of the rows in the column, similar to qsort.</p>
<dt><code>XmNtitle</code></p>
<dd>This is the title that is displayed at the top of the MultiList widget. If this value is NULL, the title area will not be shown.</p>
<dt><code>XmNwidth</code></p>
<dd>This is the overall width value assigned to the MultiList widget. Modifying this resource will affect scrollbar size and location.</dl>
<h3>Specifying Children Resources</h3>
<p>The MultiList widget is composed of many simple widgets. In order to achieve full functionality of the Toolkit, it is sometimes desirable to set attribute values directly on those widgets. The widget ids of the sub-widgets can be obtained by using the XtNameToWidget() function provided by the Xt Intrinsics. </p>
<p> XmMultiList &lt;named by application&gt; </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmLabel title</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmScrollbar vertBar</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmScrollBar horizBar</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmFrame frame</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmPushButton find</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmText findText</p>
<h3>Using the Resource Database</h3>
<p>The MultiList widget is actually a collection of pieces. It provides the geometry layout for the collection as well as tying together the pieces to form a consistent package. Many of the resources that are documented as being part of the MultiList widget are really part of the internal list sub-component. The MultiList widget will pass these values through to the proper child when they are set at time of creation or with XtSetValues or XtGetValues. However, when setting a resource via the resource database you must use either the name of the child or the general specification (*) rather than the specific one (.). </p>
<h3>The XmMultiListRowInfo Structure</h3>
<p>The XmMultiListRowInfo structure is used to contain the entryData associated with each Row in the List. </p>
<pre>typedef struct {
 String * values; /* The array of column strings */
 Pixmap pixmap; /* mini-icon pixmaps. */
 Boolean selected; /* row selected. */
 /*
 * Provided for the convenience of the application programmer
 */
 short * sort_id;
 XtPointer data;
 /*
 * Private to the MultiList widget (do not modify these)
 */
 short pix_width; /* of the pixmap. */
 short pix_height; /* of the pixmap. */
 short pix_depth; /* of the pixmap. */
 Boolean old_sel_state;
} XmMultiListRowInfo;</pre>
<p><i>values</i><tt>&nbsp;<wbr></tt>This is an array of strings of length numColumns which<br />
 represents the strings displayed in each column of this row. The data is allocated and maintained by the client. If firstColumnPixmaps is True, then value[0] is never referenced. <i>pixmap</i><tt>&nbsp;<wbr>&nbsp;<wbr></tt>This is the pixmap displayed to the left of this row. If<br />
 firstColumnPixmaps is True then this value is never referenced and mayn remain unset. If no pixmap is desired for this row, even though firstColumnPixmaps is True, set the value of pixmap to None. Color pixmaps may be used. <i>sort_id</i><tt>&nbsp;<wbr></tt>This is provided for the convenience of the client and is expected<br />
 to be used as a sort index for this row. One value should be specified for each column of the row. See &quot;sortFunctions&quot; below for details. <i>data</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>This is provided for the convenience of the client and may be<br />
 used for any purpose. It is intended to be used as an identifier for the object pointed to by this row </p>
<p> <i>selected</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>This value is True if this row is selected; may be set by the<br />
 application. </p>
<p> Neither <i>sort_id</i> nor <i>data</i> are used by the MultiList widget; they exist solely for the convenience of the programmer. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmManager Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbottomShadowColor</td>
<td>XmCBottomShadowColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbottomShadowPixmap</td>
<td>XmCBottomShadowPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNforeground</td>
<td>XmCForeground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhelpCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightColor</td>
<td>XmCHighlightColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightPixmap</td>
<td>XmCHighlightPixmap</td>
<td>Pixmap</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinitialFocus</td>
<td>XmCInitialFocus</td>
<td>Widget</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlayoutDirection</td>
<td>XmCLayoutDirection</td>
<td>XmDirection</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnavigationType</td>
<td>XmCNavigationType</td>
<td>XmNavigationType</td>
<td>XmTAB_GROUP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNpopupHandlerCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNshadowThickness</td>
<td>XmCShadowThickness</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNstringDirection</td>
<td>XmCStringDirection</td>
<td>XmStringDirection</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtopShadowColor</td>
<td>XmCTopShadowColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtopShadowPixmap</td>
<td>XmCTopShadowPixmap</td>
<td>Pixmap</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtraversalOn</td>
<td>XmCTraversalOn</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNunitType</td>
<td>XmCUnitType</td>
<td>unsigned char</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNuserData</td>
<td>XmCUserData</td>
<td>XtPointer</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>Composite Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNchildren</td>
<td>XmCReadOnly</td>
<td>WidgetList</td>
<td>NULL</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinsertPosition</td>
<td>XmCInsertPosition</td>
<td>XtOrderProc</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnumChildren</td>
<td>XmCReadOnly</td>
<td>Cardinal</td>
<td>0</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>Core Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNaccelerators</td>
<td>XmCAccelerators</td>
<td>XtAccelerators</td>
<td>dynamic</td>
<td>N/A
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNancestorSensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>dynamic</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackground</td>
<td>XmCBackground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackgroundPixmap</td>
<td>XmCPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderColor</td>
<td>XmCBorderColor</td>
<td>Pixel</td>
<td>XtDefaultForeground</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderPixmap</td>
<td>XmCPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNcolormap</td>
<td>XmCColormap</td>
<td>Colormap</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdepth</td>
<td>XmCDepth</td>
<td>int</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdestroyCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNheight</td>
<td>XmCHeight</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinitialResourcesPersistent</td>
<td>XmCInitialResourcesPersistent</td>
<td>Boolean</td>
<td>True</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmappedWhenManaged</td>
<td>XmCMappedWhenManaged</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNscreen</td>
<td>XmCScreen</td>
<td>Screen *</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtranslations</td>
<td>XmCTranslations</td>
<td>XtTranslations</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNwidth</td>
<td>XmCWidth</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNx</td>
<td>XmCPosition</td>
<td>Position</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNy</td>
<td>XmCPosition</td>
<td>Position</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<h3>Translations</h3>
<p>The following are the default translation bindings used by the icon button: </p>
<table>
<tr VALIGN=top>
<td>~Ctrl ~Shift &lt;Btn1Down&gt;:</td>
<td>ButtonDown()
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl ~Shift &lt;Btn1Down&gt;:</td>
<td>ButtonDown(Toggle)
</td>
</tr>
<tr VALIGN=top>
<td>~Ctrl Shift &lt;Btn1Down&gt;:</td>
<td>ButtonDown(Extend)
</td>
</tr>
<tr VALIGN=top>
<td>Button1 &lt;Motion&gt;:</td>
<td>Motion()
</td>
</tr>
<tr VALIGN=top>
<td>&lt;Btn1Up&gt;:</td>
<td>ButtonUpOrLeave()
</td>
</tr>
</table>
<p> The following actions are supported by the MultiList:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>ButtonDown(type)</code></p>
<dd>Processes a button press action that may begin with either a select or a double click. The type argument can be either Toggle or Extend. These values determine which mode of an extended select will be initiated on this button event. Consult the OSF/Motif Style Guide for details.</p>
<dt><code>Motion()</code></p>
<dd>Processes motion events to allow the selection region to be modified when in extended selection mode. It is assumed that this action is called between a ButtonDown() and ButtonUpOrLeave() action.</p>
<dt><code>ButtonUpOrLeave()</code></p>
<dd>Cleans up after ButtonDown() and Motion().</dl>
</dl>
<h2>Callback Routines</h2>
<p>All procedures on the MultiList&#8217;s singleSelectionCallback and doubleClickCallback lists will have a pointer to a XmMultiListRowInfo structure passed to them in the call_data field. This structure is defined above. </p>
<p> Note: if a single SelectionCallback is registered on an MultiList in extended_select_mode, the value of call_data is undefined.</p>
<dl COMPACT>
<dd><code>void</code> (callback)(<code>Widget</code> <i>w</i>, <code>XtPointer</code> <i>client_data</i>, <code>XtPointer</code> <i>call_data</i>)</p>
<dt><i>w</i></p>
<dd>the MultiList widget</p>
<dt><i>client_data</i></p>
<dd>the client data specified by the application</p>
<dt><i>call_data</i></p>
<dd>a pointer to an XmMultiListRowInfo structure corrsponding the the row selected</dl>
<h2>Sort Function</h2>
<p>typedef <code>int</code> (XmMultiListSortFunction) (<code>short</code> <i>column</i>, <code>XmMultiRowInfo *</code> <i>row1</i>, <code>XmMultiRowInfo *</code> <i>row2</i>);</p>
<dl COMPACT>
<dt><i>column</i></p>
<dd>the column currently being sorted</p>
<dt><i>row1</i>, <i>row2</i></p>
<dd>the two rows being compared. The return value must be an integer less than, equal to, or greater than 0, depending on whether the first argument is less than, equal to, or greater than the second.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatemultilist/">XmCreateMultiList</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmmultilistdeselectallitems/">XmMultiListDeselectAllItems</a></code>(3), <code><a href="/docs/linux/man/3-xmmultilistdeselectitem/">XmMultiListDeselectItem</a></code>(3), <code><a href="/docs/linux/man/3-xmmultilistdeselectitems/">XmMultiListDeselectItems</a></code>(3), <code><a href="/docs/linux/man/3-xmmultilistdeselectrow/">XmMultiListDeselectRow</a></code>(3), <code><a href="/docs/linux/man/3-xmmultilistgetselectedrowarray/">XmMultiListGetSelectedRowArray</a></code>(3), <code><a href="/docs/linux/man/3-xmmultilistgetselectedrows/">XmMultiListGetSelectedRows</a></code>(3), <code><a href="/docs/linux/man/3-xmmultilistmakerowvisible/">XmMultiListMakeRowVisible</a></code>(3), <code><a href="/docs/linux/man/3-xmmultilistselectallitems/">XmMultiListSelectAllItems</a></code>(3), <code><a href="/docs/linux/man/3-xmmultilistselectitems/">XmMultiListSelectItems</a></code>(3), <code><a href="/docs/linux/man/3-xmmultilistselectrow/">XmMultiListSelectRow</a></code>(3), and <code><a href="/docs/linux/man/3-xmmultilisttogglerow/">XmMultiListToggleRow</a></code>(3). </p>
<h2>Copyright</h2>
<p>Copyright (c) 1992 by Integrated Computer Solutions, Inc.</p>
