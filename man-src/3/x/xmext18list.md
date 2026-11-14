---
title: "xmext18list(3)"
name: "xmext18list"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmext18list/"
---

The Internationalized Extended List widget
<h2>Synopsis</h2>#include &lt;Xm/Ext18List.h&gt;
<h2>Description</h2><table> <tr VALIGN=top></tr><tr VALIGN=top><td><font SIZE="+9">&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></font></td></tr> </table> 

 This widget contains a multi-column list with headers along the top and a search area along the bottom. The list has scrollbars along the right and bottom edges that allow vertical and horizontal scrolling both by column and by pixel. The portion of the list data that is currently visible can be altered by scrollbar actions, widget resource setting and the redisplay of the list data after a string search has been successful. The sorting of elements within a particular column is also supported. To sort the list by the elements in a given column, select the column's title. 

 To search for a particular string in the list, type the string value to be searched for in the list's associated text field and then press the &quot;Find&quot; pushbutton. The search for the string begins in the currently selected row, after the location of the previously searched for string, or at the first column and first row if there is no column selected. If the string is not found in that row, then the search continues through all rows after and then before, the currently selected row. If the string is found, the display of the list is adjusted to make the string visible. If the string was not found, or if the string is visible, the application will issue a warning beep. 

 Pointer button one allows the user to select a row or a column for sorting. The callbacks on the doubleClickCallback list are called when the user double clicks pointer button one. If the list data can contain a row pixmap to display at the extreme left of the row. 

<h2>Normal Resources</h2><table> <tr VALIGN=top><td>Name</td><td>Class</td><td>Type</td><td>Default
</td></tr><tr VALIGN=top><td>columnTitles</td><td>ColumnTitles</td><td>String *</td><td>NULL
</td></tr><tr VALIGN=top><td>doubleClickCallback</td><td>Callback</td><td>Callback</td><td>NULL
</td></tr><tr VALIGN=top><td>entryData</td><td>EntryData</td><td>Xm18RowInfo*</td><td>NULL
</td></tr><tr VALIGN=top><td>findLabel</td><td>XmString</td><td>XmString</td><td>Find
</td></tr><tr VALIGN=top><td>firstColumn</td><td>FirstLocation</td><td>short</td><td>0
</td></tr><tr VALIGN=top><td>firstColumnPixmaps</td><td>FirstColumnPixmaps</td><td>Boolean</td><td>False
</td></tr><tr VALIGN=top><td>firstRow</td><td>FirstLocation</td><td>short</td><td>0
</td></tr><tr VALIGN=top><td>fontList</td><td>FontList</td><td>FontList</td><td>&quot;fixed&quot;
</td></tr><tr VALIGN=top><td>height</td><td>Dimension</td><td>VerticalDimension</td><td>300
</td></tr><tr VALIGN=top><td>numColumns</td><td>NumColumns</td><td>short</td><td>0
</td></tr><tr VALIGN=top><td>numRows</td><td>NumRows</td><td>short</td><td>0
</td></tr><tr VALIGN=top><td>selectedColumn</td><td>SelectedColumn</td><td>short</td><td>0
</td></tr><tr VALIGN=top><td>selectionPolicy</td><td>SelectionPolicy</td><td>SelectionPolicy</td><td>XmEXTENDED_
</td></tr><tr VALIGN=top><td></td><td></td><td></td><td>SELECT
</td></tr><tr VALIGN=top><td>showFind</td><td>boolean</td><td>boolean</td><td>True
</td></tr><tr VALIGN=top><td>singleSelection</td><td>Callback</td><td>Callback</td><td>NULL
</td></tr><tr VALIGN=top><td>sortFunctions</td><td>Function</td><td>Function</td><td>NULL
</td></tr><tr VALIGN=top><td>title</td><td>Title</td><td>String</td><td>name of 
</td></tr><tr VALIGN=top><td></td><td></td><td></td><td>widget
</td></tr><tr VALIGN=top><td>width</td><td>Dimension</td><td>Horizontal</td><td>Dimension
</td></tr> </table> 

 All resource names begin with XmN and all resource class names begin with XmC. 

<h2>columnTitles</h2>This is an array of length numColumns of strings displayed at the top of each column. The data is allocated and maintained by the client. 

<h2>doubleClickCallback</h2>All routines in this list will be called whenever the user double clicks on a row in the list. 

<h2>entryData</h2>This resource is the data associated with each row in the list. The data is an array of Xm18RowInfo structures of length numRows allocated by the client. The data is allocated and maintained by the client. The Xm18RowInfo structure is defined below. 

<h2>findLabel</h2>The label to be shown on the find button. 

<h2>firstColumn</h2>This resource allows the client to adjust the current view of the list data to have a new top left column location. When setting this resource, firstRow should also be updated. 

<h2>firstColumnPixmaps</h2>This resource specifies that the pixmap stored in the row info structure should be used instead of Xm18RowInfo values[0]. If pixmaps are present, the rows may be dragged by pressing on the pixmap with pointer button three. If this resource is True, then values[0] is never referenced. If False, then the Xm18RowInfo data pixmap is never referenced. 

<h2>firstRow</h2>This resource allows the client to adjust the current view of the list data to have a new top left row location. When setting this resource, firstColumn should also be updated. 

<h2>fontList</h2>This is an OSF/Motif style font list. The first font in this list will be used to display all text in the Extended List widget. The Extended List widget currently supports only one font. 

<h2>height</h2>This is the overall height value assigned to the Extended List widget. Modifying this resource will affect scrollbar size and location. 

<h2>numColumns</h2><h2>numRows</h2>These resources specify the number of columns and rows the widget expects to display. These resources are used as the maximum indices for many of the other resources in this widget. Care should be taken when modifying these resources to ensure that the other values have also been modified. 

<h2>selectedColumn</h2>This is the index of the currently selected column. This also the column by which the list is being sorted. 

<h2>selectionPolicy</h2>Defines the interpretation of the select action. This resource can have the values XmSINGLE_SELECT or XmEXTENDED_SELECT. Other values result in undefined behavior. 

<h2>showFind</h2>This boolean manages and unmanages the find button 

<h2>singleSelectionCallback</h2>All routines in this list will be called whenever the user clicks on a line in the list. A pointer to the Xm18RowInfo structure corresponding to the line selected is passed as call_data. If in extended select mode the value of call_data is undefined. 

<h2>sortFunctions</h2>This is an array of functions, one for each column, called to determine the ordering of the rows in the column, similar to qsort. 

<h2>title</h2>This is the title that is displayed at the top of the Extended List widget. If this value is NULL, the title area will not be shown. 

<h2>width</h2>This is the overall width value assigned to the Extended List widget. Modifying this resource will affect scrollbar size and location. 

<h2>Specifying Children Resources</h2>The Extended List widget is composed of many simple widgets. In order to achieve full functionality of the Toolkit, it is sometimes desirable to set attribute values directly on those widgets. The widget ids of the sub-widgets can be obtained by using the XtNameToWidget() function provided by the Xt Intrinsics. 

 

 

 XmExt18List &lt;named by application&gt; 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmLabel title
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmScrollbar vertBar
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmScrollBar horizBar
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmFrame frame
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmPushButton find
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmText findText
 

 

<h2>Using the Resource Database</h2>The Extended List widget is actually a collection of pieces. It provides the geometry layout for the collection as well as tying together the pieces to form a consistent package. Many of the resources that are documented as being part of the Extended List widget are really part of the internal list sub-component. The Extended List widget will pass these values through to the proper child when they are set at time of creation or with XtSetValues or XtGetValues. However, when setting a resource via the resource database you must use either the name of the child or the general specification (*) rather than the specific one (.). 

<h2>The Xm18RowInfo Structure</h2>The Xm18RowInfo structure is used to contain the entryData associated with each Row in the Extended List. 

 

 

 typedef struct _Xm18RowInfo{ 

 /* 

 
&nbsp;<wbr>*&nbsp;<wbr>Used by the IList widget 

 
&nbsp;<wbr>*/ 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>String * values;/* The array of column strings */
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Pixmap pixmap;/* mini-icon pixmaps. */
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Boolean selected;/* row selected. */
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/*
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * Provided for the convenience of the application programmer
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> */
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>short * sort_id;
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XtPointer data;
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/*
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * Private to the Extended List widget (do not modify these)
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> */
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>short pix_width;/* of the pixmap. */
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>short pix_height;/* of the pixmap. */
 
&nbsp;<wbr> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>short pix_depth;/* of the pixmap. */
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Boolean old_sel_state;
 

 } Xm18RowInfo; 

<dl COMPACT><dd>values<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>This is an array of strings of length numColumns which 
 represents the strings displayed in each column of this row. The data is allocated and maintained by the client. If firstColumnPixmaps is True, then value[0] is never referenced.
<dd>pixmap<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>This is the pixmap displayed to the left of this row. If 
 firstColumnPixmaps is True then this value is never referenced and mayn remain unset. If no pixmap is desired for this row, even though firstColumnPixmaps is True, set the value of pixmap to None. Color pixmaps may be used.
<dd>sort_id<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>This is provided for the convenience of the client and is expected 
 to be used as a sort index for this row. One value should be specified for each column of the row. See &quot;sortFunctions&quot; below for details.
<dd>data<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>This is provided for the convenience of the client and may be 
 used for any purpose. It is intended to be used as an identifier for the object pointed to by this row
<dd>selected<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>This value is True if this row is selected; may be set by the 
 application.</dl>
 

 Neither sort_id nor data are used by the Extended List widget; they exist solely for the convenience of the programmer. 

<h2>Translations and Actions</h2>The following are the default translation bindings used by the icon button: 

 <table> <tr VALIGN=top><td>~Ctrl ~Shift &lt;Btn1Down&gt;:</td><td>ButtonDown()
</td></tr><tr VALIGN=top><td>Ctrl ~Shift &lt;Btn1Down&gt;:</td><td>ButtonDown(Toggle)
</td></tr><tr VALIGN=top><td>~Ctrl Shift &lt;Btn1Down&gt;:</td><td>ButtonDown(Extend)
</td></tr><tr VALIGN=top><td>Button1 &lt;Motion&gt;:</td><td>Motion()
</td></tr><tr VALIGN=top><td>&lt;Btn1Up&gt;:</td><td>ButtonUpOrLeave()
</td></tr> </table> 

 The following actions are supported by the icon button: 

<h2>ButtonDown(type)</h2>Processes a button press action that may begin with 
 either a select or a double click. The type argument can be either Toggle or Extend. These values determine which mode of an extended select will be initiated on this button event. Consult the OSF/Motif Style Guide for details. 

<h2>Motion()</h2>Processes motion events to allow the selection region to 
 be modified when in extended selection mode. It is assumed that this action is called between a ButtonDown() and ButtonUpOrLeave() action. 

<h2>ButtonUpOrLeave()</h2>Cleans up after ButtonDown() and Motion().
 

<h2>Callback Routines</h2>All procedures on the Extended List's singleSelectionCallback and doubleClickCallback lists will have a pointer to a Xm18RowInfo structure passed to them in the call_data field. This structure is defined above. 

 Note: if a single SelectionCallback is registered on an extended list in extended_se- lect_mode, the value of call_data is undefined. 

<dl COMPACT><dd>void (callback)(Widget w, XtPointer client_data, XtPointer call_data)
<dd>w<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the Extended List widget

<dd>client_data<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the client data specified by the application

<dd>call_data<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>a pointer to an Xm18RowInfo structure corrsponding the the row 
 selected 

</dl><h2>Sort Function</h2><dl COMPACT><dd>typedef int (Xm18SortFunction) (short column, Xm18RowInfo * row1, Xm18RowInfo * row2);
<dd>column<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the column currently being sorted

<dd>row1, row2<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the two rows being compared. The return value must be an 
 integer less than, equal to, or greater than 0, depending on whether the first argument is less than, equal to, or greater than the second. 

</dl><h2>Convenience Routines</h2><h2>
<dt></h2></dl><h2>XmExt18ListGetSelectedRows</h2><dd>Xm18RowInfo ** XmExt18ListGetSelectedRows (Widget w) 

 w<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>extended list widget
 

 Use the XmExt18ListGetSelectedRows function to find the rows that currently are selected in an extended list. The Xm18RowInfo ** returned by this function contains a NULL terminated array of Xm18RowInfo pointers. The calling routine is responsible for freeing the returned pointer with XtFree(). The function will return NULL if no elements are selected. 

<h2>XmCreateExtended18List</h2>Widget XmCreateExtended18List(Widget parent, String name, <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> ArgList args, Cardinal num_args)
 

 parent<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>parent of the extended list widget to be 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>created
 
 name<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>name of the extended list widget to be
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>created
 
 args<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>arguments to pass to XtCreateWidget for the 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>extended list
 
 num_args<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>number of arguments passed
 

 This convenience routine simply takes the passed parameters and calls XtCreateWidget, returning the widget created. 

<h2>XmExt18ListUnselectAllItems</h2>void XmExt18ListUnselectAllItems( Widget w ) 

 w<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the extended list widget to be modified
 

 Unselects all rows of the passed extended list widget and returns nothing. 

<h2>XmExt18ListUnselectItem</h2>void XmExt18ListUnselectItem(Widget w, Xm18RowInfo *row_info) 

 w<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>extended list widget
 
 row_info<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>pointer to the row which is to be
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>unselected.
 

 Unselects the row designated by row_info of the passed extended list widget w 

<h2>Copyright</h2>Copyright (c) 1992 by Integrated Computer Solutions, Inc.
