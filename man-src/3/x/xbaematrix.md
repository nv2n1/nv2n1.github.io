---
title: "xbaematrix(3)"
name: "xbaematrix"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xbaematrix/"
description: "XbaeMatrix – The Bellcore Application Environment (BAE) XbaeMatrix widget class."
---

<p>XbaeMatrix &#8211; The Bellcore Application Environment (BAE) XbaeMatrix widget class.</p>
<h2>Synopsis</h2>
<p>#include &lt;Xbae/Matrix.h&gt;</p>
<h2>Description</h2>
<p><code>XbaeMatrix</code> presents an editable array of string data to the user in a scrollable grid-like format similar to a spreadsheet. Non editable pixmaps can also be displayed on the matrix. The rows and columns of the Matrix may optionally be labeled. Also, a number of fixed leading or trailing rows or columns may be specified &#8211; these behave similarly to the labels. While <code>XbaeMatrix</code> looks and acts like a grid of <code>XmText</code> widgets, it actually contains only one <code>XmText</code>. This means that <code>XbaeMatrix</code> widgets with hundreds or thousands of rows have much less overhead than they would if they used an <code>XmText</code> for each cell. </p>
<p> Clicking on a cell with <code>Button1</code> will edit the cell. While a cell is being edited, <code>Tab</code> and <code>Shift-Tab</code> will edit the cell to the right or left respectively. The <code>osfUp</code> and <code>osfDown</code> keys will edit the cell above or below. <code>Ctrl-Tab</code> and <code>Shift-Ctrl-Tab will traverse out of the Matrix and</code> into the next or previous tab groups. </p>
<p> The <code>osfCancel</code> key will cancel any edits made to a cell. The <code>osfActivate</code> key will commit any edits made to a cell and store them in the Matrix. When traversing from another tab group into the Matrix, the focus will go to whichever cell is currently being edited. If no cells are being edited, then the upper left most visible non-fixed cell will be edited. </p>
<p> The column sizes may be dynamically resized by pressing the Shift-Button2 combination when over a column boundary, similar to the behaviour of some popular spreadsheets. After a column has been resized in this manner, the <code>XbaeMatrix</code> calls the callbacks on the <code>XmNresizeColumnCallback</code> callback list for post processing. </p>
<p> If the Matrix is resized until it is too small to display all of the cells in a given dimension, then it will display a ScrollBar for that dimension. The horizontal ScrollBar will scroll the cells and column labels, but not the row labels, fixed columns or trailing fixed columns. The vertical ScrollBar will scroll the cells and row labels, but not the column labels, fixed rows or trailing fixed rows. </p>
<p> For the application programmer, <code>XbaeMatrix</code> provides callbacks to assist in data validation. The callbacks on the <code>XmNmodifyVerifyCallback</code> callback list are called before text is inserted into, or deleted from, a cell. This callback list can be used to force user input to match a certain pattern (e.g. a date format). Similarly, the <code>XmNvalueChangedCallback</code> is called after text is inserted or deleted. </p>
<p> When a cell is edited (by clicking on it or tabbing into it), the <code>XmNleaveCellCallback</code> callbacks are called for the previous cell being edited, if any. The application can verify the data entered in that cell and disallow editing of the new cell if the data is invalid. If the data was valid, then the <code>XmNenterCellCallback</code> callbacks for the new cell are called. These callbacks can be used to specify the editability of the new cell. </p>
<p> The <code>XmNtraverseCellCallback</code> callbacks are also called when the user attempts to edit a new cell and when the matrix gains or looses focus. This allows the application to override the default traversal behavior of <code>XbaeMatrix</code>. </p>
<p> The <code>XmNdefaultActionCallback</code> is provided to allow a double click action in a cell to perform some function. </p>
<p> Motif&#8217;s Drag and Drop functionality can be achieved via the <code>XmNprocessDragCallback</code>. </p>
<p> For large amounts of data, the overhead of assigning data to the widget can be avoided using the <code>XmNdrawCellCallback</code>. This callback also allows user defined pixmaps to be placed in a certain cell. When using this callback, data for string fields can be written back to the application by using the <code>XmNwriteCellCallback</code>.</p>
<h2>Classes</h2>
<p><code>XbaeMatrix</code> inherits behavior and resources from the <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, and <code>XmManager</code> widget classes.<br />
 The class pointer is <code>xbaeMatrixWidgetClass</code>.<br />
 The class name is <code>XbaeMatrix</code>.</p>
<h2>New Resources</h2>
<p>The following table lists the new resources defined by <code>XbaeMatrix</code>. The codes in the &#8220;Access&#8221; column indicate whether the given resource can be set at creation time (C), or set by using XtSetValues (S), or retrieved by using XtGetValues (G). </p>
<table BORDER>
<tr>
<td>
<table WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>XbaeMatrix Resource Set
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
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
<td COLSPAN=5>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNallowColumnResize</font></td>
<td><font SIZE="-9">XmCAllowResize</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNallowRowResize</font></td>
<td><font SIZE="-9">XmCAllowResize</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNaltRowCount</font></td>
<td><font SIZE="-9">XmCAltRowCount</font></td>
<td><font SIZE="-9">int</font></td>
<td><font SIZE="-9">1</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNboldLabels</font></td>
<td><font SIZE="-9">XmCBoldLabels</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNbuttonLabels</font></td>
<td><font SIZE="-9">XmCButtonLabels</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNbuttonLabelBackground</font></td>
<td><font SIZE="-9">XmCColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcalcCursorPosition</font></td>
<td><font SIZE="-9">XmCCalcCursorPosition</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcellBackgrounds</font></td>
<td><font SIZE="-9">XmCColors</font></td>
<td><font SIZE="-9">PixelTable</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcellHighlightThickness</font></td>
<td><font SIZE="-9">XmCHighlightThickness</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcellMarginHeight</font></td>
<td><font SIZE="-9">XmCMarginHeight</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcellMarginWidth</font></td>
<td><font SIZE="-9">XmCMarginWidth</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcellShadowThickness</font></td>
<td><font SIZE="-9">XmCShadowThickness</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">2</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcellShadowType</font></td>
<td><font SIZE="-9">XmCShadowType</font></td>
<td><font SIZE="-9">unsigned char</font></td>
<td><font SIZE="-9">XmSHADOW_OUT</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcellShadowTypes</font></td>
<td><font SIZE="-9">XmCCellShadowTypes</font></td>
<td><font SIZE="-9">unsigned char **</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcellUserData</font></td>
<td><font SIZE="-9">XmCCellUserData</font></td>
<td><font SIZE="-9">XtPointer **</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNclipWindow</font></td>
<td><font SIZE="-9">XmCClipWindow</font></td>
<td><font SIZE="-9">Widget</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">G</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcells</font></td>
<td><font SIZE="-9">XmCCells</font></td>
<td><font SIZE="-9">CellTable</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolors</font></td>
<td><font SIZE="-9">XmCColors</font></td>
<td><font SIZE="-9">PixelTable</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolumnAlignments</font></td>
<td><font SIZE="-9">XmCAlignments</font></td>
<td><font SIZE="-9">AlignmentArray</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolumnButtonLabels</font></td>
<td><font SIZE="-9">XmCButtonLabels</font></td>
<td><font SIZE="-9">BooleanArray</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolumnLabelAlignments</font></td>
<td><font SIZE="-9">XmCAlignments</font></td>
<td><font SIZE="-9">AlignmentArray</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolumnLabelColor</font></td>
<td><font SIZE="-9">XmCColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolumnLabels</font></td>
<td><font SIZE="-9">XmCLabels</font></td>
<td><font SIZE="-9">StringArray</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolumnMaxLengths</font></td>
<td><font SIZE="-9">XmCColumnMaxLengths</font></td>
<td><font SIZE="-9">MaxLengthArray</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolumnShadowTypes</font></td>
<td><font SIZE="-9">XmCShadowTypes</font></td>
<td><font SIZE="-9">unsigned char *</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolumnUserData</font></td>
<td><font SIZE="-9">XmCUserDatas</font></td>
<td><font SIZE="-9">XtPointer *</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolumnWidthInPixels</font></td>
<td><font SIZE="-9">XmCColumnWidthInPixels</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolumnWidths</font></td>
<td><font SIZE="-9">XmCColumnWidths</font></td>
<td><font SIZE="-9">WidthArray</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolumns</font></td>
<td><font SIZE="-9">XmCColumns</font></td>
<td><font SIZE="-9">int</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNdefaultActionCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">XtCallbackList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNdoubleClickInterval</font></td>
<td><font SIZE="-9">XmCDoubleClickInterval</font></td>
<td><font SIZE="-9">int</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNdrawCellCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNenterCellCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNevenRowBackground</font></td>
<td><font SIZE="-9">XmCBackground</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNfill</font></td>
<td><font SIZE="-9">XmCFill</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNhorzFill</font></td>
<td><font SIZE="-9">XmCHorzFill</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNvertFill</font></td>
<td><font SIZE="-9">XmCVertFill</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNfixedColumns</font></td>
<td><font SIZE="-9">XmCFixedColumns</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNfixedRows</font></td>
<td><font SIZE="-9">XmCFixedRows</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNfontList</font></td>
<td><font SIZE="-9">XmCFontList</font></td>
<td><font SIZE="-9">FontList</font></td>
<td><font SIZE="-9">fixed</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNgridLineColor</font></td>
<td><font SIZE="-9">XmCColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNgridType</font></td>
<td><font SIZE="-9">XmCGridType</font></td>
<td><font SIZE="-9">GridType</font></td>
<td><font SIZE="-9">XmGRID_CELL_LINE</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td>
<table WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>XbaeMatrix Resource Set (continued)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
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
<td COLSPAN=5>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNhighlightedCells</font></td>
<td><font SIZE="-9">XmCHighlightedCells</font></td>
<td><font SIZE="-9">HighlightTable *</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNhorizontalScrollBar</font></td>
<td><font SIZE="-9">XmCHorizontalScrollBar</font></td>
<td><font SIZE="-9">Widget</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">G</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNhorizontalScrollBarDisplayPolicy</font></td>
<td><font SIZE="-9">XmCMatrixScrollBarDisplayPolicy</font></td>
<td><font SIZE="-9">unsigned char</font></td>
<td><font SIZE="-9">XmDISPLAY_AS_NEEDED</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNlabelActivateCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNlabelFont</font></td>
<td><font SIZE="-9">XmCFontList</font></td>
<td><font SIZE="-9">FontList</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNleaveCellCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNleftColumn</font></td>
<td><font SIZE="-9">XmCLeftColumn</font></td>
<td><font SIZE="-9">int</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNmodifyVerifyCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNmultiLineCell</font></td>
<td><font SIZE="-9">XmCMultiLineCell</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNnonFixedDetachedLeft</font></td>
<td><font SIZE="-9">XmCNonFixedDetachedLeft</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNnonFixedDetachedTop</font></td>
<td><font SIZE="-9">XmCNonFixedDetachedTop</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNoddRowBackground</font></td>
<td><font SIZE="-9">XmCBackground</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNprocessDragCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNrenderTable</font></td>
<td><font SIZE="-9">XmCRenderTable</font></td>
<td><font SIZE="-9">RenderTable</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNresizeCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNresizeColumnCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNreverseSelect</font></td>
<td><font SIZE="-9">XmCReverseSelect</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNrowButtonLabels</font></td>
<td><font SIZE="-9">XmCButtonLabels</font></td>
<td><font SIZE="-9">BooleanArray</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNrowHeightInPixels</font></td>
<td><font SIZE="-9">XmCRowHeightInPixels</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNrowHeights</font></td>
<td><font SIZE="-9">XmCColumnWidths</font></td>
<td><font SIZE="-9">WidthArray</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNrowLabelAlignment</font></td>
<td><font SIZE="-9">XmCAlignment</font></td>
<td><font SIZE="-9">Alignment</font></td>
<td><font SIZE="-9">XmALIGNMENT_END</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNrowLabelColor</font></td>
<td><font SIZE="-9">XmCColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNrowLabelWidth</font></td>
<td><font SIZE="-9">XmCRowLabelWidth</font></td>
<td><font SIZE="-9">Short</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNrowLabels</font></td>
<td><font SIZE="-9">XmCLabels</font></td>
<td><font SIZE="-9">StringArray</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNrowShadowTypes</font></td>
<td><font SIZE="-9">XmCShadowTypes</font></td>
<td><font SIZE="-9">unsigned char *</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNrowUserData</font></td>
<td><font SIZE="-9">XmCUserDatas</font></td>
<td><font SIZE="-9">XtPointer *</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNrows</font></td>
<td><font SIZE="-9">XmCRows</font></td>
<td><font SIZE="-9">int</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNscrollBarPlacement</font></td>
<td><font SIZE="-9">XmCScrollBarPlacement</font></td>
<td><font SIZE="-9">unsigned char</font></td>
<td><font SIZE="-9">XmBOTTOM_RIGHT</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNselectCellCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNselectScrollVisible</font></td>
<td><font SIZE="-9">XmCSelectScrollVisible</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNselectedBackground</font></td>
<td><font SIZE="-9">XmCColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNselectedCells</font></td>
<td><font SIZE="-9">XmCSelectedCells</font></td>
<td><font SIZE="-9">BooleanTable</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNselectedForeground</font></td>
<td><font SIZE="-9">XmCColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNshadowType</font></td>
<td><font SIZE="-9">XmCShadowType</font></td>
<td><font SIZE="-9">unsigned char</font></td>
<td><font SIZE="-9">XmSHADOW_IN</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNshowArrows</font></td>
<td><font SIZE="-9">XmCShowArrows</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNspace</font></td>
<td><font SIZE="-9">XmCSpace</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">dynamic </font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtextBackground</font></td>
<td><font SIZE="-9">XmCBackground</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">XmUNSPECIFIED_PIXEL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtextBackgroundIsCell</font></td>
<td><font SIZE="-9">XmCTextBackgroundIsCell</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtextField</font></td>
<td><font SIZE="-9">XmCTextField</font></td>
<td><font SIZE="-9">Widget</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">G</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtextShadowThickness</font></td>
<td><font SIZE="-9">XmCTextShadowThickness</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtextTranslations</font></td>
<td><font SIZE="-9">XmCTranslations</font></td>
<td><font SIZE="-9">TranslationTable</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtopRow</font></td>
<td><font SIZE="-9">XmCTopRow</font></td>
<td><font SIZE="-9">int</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtrackcellCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtrailingAttachedBottom</font></td>
<td><font SIZE="-9">XmCTrailingAttachedBottom</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtrailingAttachedRight</font></td>
<td><font SIZE="-9">XmCTrailingAttachedRight</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtrailingFixedColumns</font></td>
<td><font SIZE="-9">XmCTrailingFixedColumns</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtrailingFixedRows</font></td>
<td><font SIZE="-9">XmCTrailingFixedRows</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtraverseCellCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtraverseFixedCells</font></td>
<td><font SIZE="-9">XmCTraverseFixedCells</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td>
<table WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>XbaeMatrix Resource Set (continued)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
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
<td COLSPAN=5>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNuseXbaeInput</font></td>
<td><font SIZE="-9">XmCUseXbaeInput</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNvalueChangedCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNverticalScrollBar</font></td>
<td><font SIZE="-9">XmCVerticalScrollBar</font></td>
<td><font SIZE="-9">Widget</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">G</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNverticalScrollBarDisplayPolicy</font></td>
<td><font SIZE="-9">XmCMatrixScrollBarDisplayPolicy</font></td>
<td><font SIZE="-9">unsigned char</font></td>
<td><font SIZE="-9">XmDISPLAY_AS_NEEDED</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNvisibleColumns</font></td>
<td><font SIZE="-9">XmCVisibleColumns</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNvisibleRows</font></td>
<td><font SIZE="-9">XmCVisibleRows</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNwrapType</font></td>
<td><font SIZE="-9">XmCWrapType</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">XbaeWrapNone</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNwriteCellCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNxmColumnLabels</font></td>
<td><font SIZE="-9">XmCXmLabels</font></td>
<td><font SIZE="-9">XmString *</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNxmRowLabels</font></td>
<td><font SIZE="-9">XmCXmLabels</font></td>
<td><font SIZE="-9">XmString *</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
</table>
</table>
<p> This resource cannot be specified in a resource file </p>
<dl COMPACT>
<dt><code>XmNallowColumnResize</code></p>
<dd>If True, allows the columns to be dynamically resized via the ResizeColumns() action. The default value is to allow column resizing.</p>
<dt><code>XmNallowRowResize</code></p>
<dd>If True, allows the rows to be dynamically resized via the ResizeRows() action. The default value is to allow row resizing.</p>
<dt><code>XmNaltRowCount</code></p>
<dd>Specifies the number of rows to use for each of the <code>XmNevenRowBackground</code> and <code>XmNoddRowBackround</code> colors. This resource is ignored if <code>XmNevenRowBackground</code> and <code>XmNoddRowBackround</code> are not used.</p>
<dt><code>XmNboldLabels</code></p>
<dd>Overstrikes the row and column labels to create a bold font appearance when True.</p>
<dt><code>XmNbuttonLabels</code></p>
<dd>When set to True, the labels will be drawn with a shadow around them similar to an <code>XmPushButton</code> widget. A ButtonPress event generated on the labels, when <code>XmNbuttonLabels</code> is True will cause the label to reverse the shadow and take on a pushed in appearance. A ButtonRelease event on the same label will invoke callbacks on the <code>XmNlabelActivateCallback</code>, list. The default value is False.</p>
<dt><code>XmNbuttonLabelBackground</code></p>
<dd>Specifies a Pixel value in which to draw the <code>XmNbuttonLabels</code>.</p>
<dt><code>XmNcalcCursorPosition</code></p>
<dd>If set to True, the insertion position on the text field is calculated with respect to where the pointer was clicked in the cell. The default value is False. The insertion position will be overridden if the <i>position</i> member of the <code>XbaeEnterCellCallbackStruct</code> is set to a valid position.</p>
<dt><code>XmNcellBackgrounds</code></p>
<dd>Points to an array of pointers to rows. Each row is an array of Pixel values, one for each column in that row. This data structure is the same as that for <code>XmNcells</code>, except each entry is a Pixel instead of a String. The background of a cell will be drawn in the color specified for that cell. If <code>XmNcellBackgrounds</code> is <font SIZE="-1">NULL,</font> backgrounds will be drawn using the color specified by <code>XmNbackground</code>. This resource is copied. <code>XmNcellBackgrounds may be specified in a resource file but due to the</code> two dimensional nature of the <code>XbaeMatrix</code> widget, it must be done by terminating each line with a 
 character. If the <code>XbaeMatrix widget had</code> <code>XmNrows</code> set to 5 and <code>XmNcolumns</code> set to 5, <code>XmNcellBackgrounds</code> would be specified as: </p>
<table>
<tr VALIGN=top>
<td>*mw.cellBackgrounds:</td>
<td>blue, white, blue, white, blue
\
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>white, blue, white, blue, white
\
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>blue, white, blue, white, blue
\
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>white, blue, white, blue, white
\
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>blue, white, blue, white, blue

</td>
</tr>
</table>
<p> Care must be taken when specifying these values in a resource file as an incorrect format can produce undesirable results.</p>
<dt><code>XmNcellHighlightThickness</code></p>
<dd>Specifies the <code>XmNhighlightThickness</code> resource of the <code>XmText</code> cell edit widget. This resource is also used to compute the size of each cell. See the description of <code>XmNhighlightThickness</code> in <code><a href="//www.systutorials.com/docs/linux/man/3X-XmText/">XmText</a>(3X)</code>.</p>
<dt><code>XmNcellMarginHeight</code></p>
<dd>Specifies the <code>XmNmarginHeight </code> resource of the <code>XmText</code> widget. This resource is also used to compute the size of each cell. See the description of <code>XmNmarginHeight</code> in <code><a href="//www.systutorials.com/docs/linux/man/3X-XmText/">XmText</a>(3X)</code>.</p>
<dt><code>XmNcellMarginWidth</code></p>
<dd>Specifies the <code>XmNmarginWidth</code> resource of the <code>XmText</code> cell edit widget. This resource is also used to compute the size of each cell. See the description of <code>XmNmarginWidth</code> in <code><a href="//www.systutorials.com/docs/linux/man/3X-XmText/">XmText</a>(3X)</code>.</p>
<dt><code>XmNcellShadowThickness</code></p>
<dd>Specifies the <code>XmNshadowThickness</code> resource of the <code>XmText</code> cell edit widget. This resource is also used to compute the size of each cell. See the description of <code>XmNshadowThickness</code> in <code><a href="//www.systutorials.com/docs/linux/man/3X-XmText/">XmText</a>(3X)</code>.</p>
<dt><code>XmNcellShadowType</code></p>
<dd>Specifies the type of shadow drawn around each cell. Possible values for this resource are <code>XmSHADOW_OUT</code>, <code>XmSHADOW_IN</code>, <code>XmSHADOW_ETCHED_OUT</code>, and <code>XmSHADOW_ETCHED_IN</code>. The default shadow type is <code>XmSHADOW_OUT</code>.</p>
<dt><code>XmNcellShadowTypes</code></p>
<dd>Specifies on a per cell basis, the <code>XmNcellShadowType</code>. Values for the resource are the same as for <code>XmNcellShadowType</code>. This resource is copied.</p>
<dt><code>XmNcellUserData</code></p>
<dd>Points to an array of pointers to individual user defined data areas associated with each cell. The data should be set using <code>XbaeMatrixSetCellUserData()</code> and retrieved using <code>XbaeMatrixGetCellUserData()</code>. This resource cannot be specified in a resource file and is copied.</p>
<dt><code>XmNcells</code></p>
<dd>Points to an array of pointers to rows. Each row is an array of String, one for each column in that row. For example, the cells for a 2&#215;3 Matrix could be set up as follows: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=4>String rows[2][3] =
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>&quot;00&quot;,</td>
<td>&quot;01&quot;,</td>
<td>&quot;02&quot;,
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>&quot;10&quot;,</td>
<td>&quot;11&quot;,</td>
<td>&quot;12&quot;
</td>
</tr>
<tr VALIGN=top>
<td>};</td>
<td></td>
<td></td>
<td>
</td>
</tr>
</table>
<table>
<tr VALIGN=top>
<td></td>
<td>String *cells[2];</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>cells[0] = &amp;rows[0][0];</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>cells[1] = &amp;rows[1][0];</td>
<td>
</td>
</tr>
</table>
<p> Now cells could be used as the <code>XmNcells</code> resource. If <code>XmNcells</code> is <font SIZE="-1">NULL,</font> <code>XbaeMatrix</code> will <code>not</code> generate an internal table of empty Strings. This implies that if <code>XmNcells </code> is <code>NULL</code>, no cells have been set. This resource is copied. See the discussion in <code>XmNcellBackgrounds</code> for how to specify <code>XmNcells</code> in a resource file.</p>
<dt><code>XmNclipWindow</code></p>
<dd>The widget ID of the clip window. The clip window is the widget that contains the non-fixed region of cells. This resource can not be set to a new value.</p>
<dt><code>XmNcolors</code></p>
<dd>Points to an array of pointers to rows. Each row is an array of Pixel values, one for each column in that row. This data structure is the same as that for <code>XmNcells</code>, except each entry is a Pixel instead of a String. The text in a cell will be drawn in the color specified for that cell. If <code>XmNcolors</code> is <font SIZE="-1">NULL,</font> text will be drawn using the color specified by <code>XmNforeground</code>. This resource is copied. See the discussion in <code>XmNcellBackgrounds</code> for how to specify <code>XmNcolors</code> in a resource file.</p>
<dt><code>XmNcolumnAlignments</code></p>
<dd>Points to an array of alignments (unsigned char), one for each column. Each element can be one of <code>XmALIGNMENT_BEGINNING</code>, <code>XmALIGNMENT_CENTER</code> or <code>XmALIGNMENT_END</code>. This specifies the alignment of the text or pixmap in each cell of that column. See the description of <code>XmNalignment</code> for <code><a href="//www.systutorials.com/docs/linux/man/3X-XmLabel/">XmLabel</a>(3X)</code>. If <code>XmNcolumnAlignments</code> is <font SIZE="-1">NULL, </font> each column will default to <code>XmALIGNMENT_BEGINNING</code>. This resource is copied.</p>
<dt><code>XmNcolumnButtonLabels</code></p>
<dd>An array of Booleans that tells the <code>XbaeMatrix</code> which column labels should be drawn as a button. Each Boolean can be specified as a Boolean string or integer. In order to use this resource, <code>XmNbuttonLabels</code> should be set to False.</p>
<dt><code>XmNcolumnLabelAlignments</code></p>
<dd>Points to an array of alignments (unsigned char), one for each column label. Each element can be one of <code>XmALIGNMENT_BEGINNING,</code> <code>XmALIGNMENT_CENTER</code> or <code>XmALIGNMENT_END</code>. This specifies the alignment of the text of each column label. See the description of <code>XmNalignment</code> for <code><a href="//www.systutorials.com/docs/linux/man/3X-XmLabel/">XmLabel</a>(3X)</code>. If <code>XmNcolumnLabelAlignments</code> is <font SIZE="-1">NULL,</font> each column label will default to <code>XmALIGNMENT_BEGINNING</code>. This resource is copied.</p>
<dt><code>XmNcolumnLabelColor</code></p>
<dd>Specifies a Pixel value in which to draw the <code>XmNcolumnLabels</code>.</p>
<dt><code>XmNcolumnLabels</code></p>
<dd>Points to an array of Strings to be drawn above each column. Each String may have embedded newline characters, in which case the label will be drawn on multiple lines. If there is a <code>XmNxmColumnLabels </code> defined for this coluumn it will be displayed in place of the <code>XmNcolumnLabels. </code> If <code>XmNcolumnLabels </code> and <code>XmNxmColumnLabels </code> are <font SIZE="-1">NULL, </font> no labels will be drawn. This resource is copied.</p>
<dt><code>XmNcolumnMaxLengths</code></p>
<dd>Points to an array of int, one for each column. These specify the maximum length of a String which can be entered in the cells in that column. See the description of the <code><a href="//www.systutorials.com/docs/linux/man/3X-XmText/">XmText</a>(3X) XmNmaxLength</code> resource. If <code>XmNcolumnMaxLengths</code> is <font SIZE="-1">NULL</font> or an element of the array is equal to 0, then the corresponding width from <code>XmNcolumnWidths</code> is used. This resource is copied.</p>
<dt><code>XmNcolumnShadowTypes</code></p>
<dd>Specifies on a per column basis, the <code>XmNcellShadowType</code>. Values for the resource are the same as for <code>XmNcellShadowType</code>. This resource is copied.</p>
<dt><code>XmNcolumnUserData</code></p>
<dd>Points to a user defined data area associated with a particular column. The data should be set using <code>XbaeMatrixSetColumnUserData()</code> and retrieved using <code>XbaeMatrixGetColumnUserData()</code>. This resource cannot be specified in a resource file.</p>
<dt><code>XmNcolumnWidthInPixels</code></p>
<dd>Specifies wether the elements of <code>XmNcolumnWidths </code> are measured in pixels or characters.</p>
<dt><code>XmNcolumnWidths</code></p>
<dd>Points to an array of short, one for each column. These specify the visible width of the cells in each column. See the description of the <code><a href="//www.systutorials.com/docs/linux/man/3X-XmText/">XmText</a>(3X) XmNcolumns</code> resource. This resource is copied.</p>
<dt><code>XmNcolumns</code></p>
<dd>Specifies the total number of columns of cells. <code>XmNcolumns</code> must be at least one. If the number of columns is changed via XtSetValues, then <code>XmNcolumnMaxLengths</code> must change or be <font SIZE="-1">NULL,</font> <code>XmNcolumnLabels</code> must change or be <font SIZE="-1">NULL,</font> <code>XmNcolumnAlignments</code> must change or be <font SIZE="-1">NULL </font> and <code>XmNcolumnLabelAlignments</code> must change or be <font SIZE="-1">NULL.</font> The preferred way to dynamically change the number of columns is to use <code>XbaeMatrixAddColumns()</code> or <code>XbaeMatrixDeleteColumns()</code>.</p>
<dt><code>XmNdefaultActionCallback</code></p>
<dd>Specifies a list of callbacks to be called when a double click occurs in a cell. A pointer to an <code>XbaeMatrixDefaultActionCallbackStruct</code> is passed to the callbacks. Events are reported to the cell in which the double click occurs regardless of whether or not a callback exists. This callback is called by the DefaultAction() action and is NULL by default. The <code>XmNdefaultActionCallback</code> is ideal for popping up a dialog or other window when a double click occurs.</p>
<dt><code>XmNdoubleClickInterval</code></p>
<dd>Specifies the amount of time between mouse clicks before it is considered a double click. A double click is defined to be the time between the realease of the mouse button and subsequent press in the same cell. The default value is inherited from the display.</p>
<dt><code>XmNdrawCellCallback</code></p>
<dd>Specifies a list of callbacks to be called when a cell needs to be drawn. A pointer to an <code>XbaeMatrixDrawCellCallbackStruct</code> is passed to the callbacks. The application can specify what to put in a cell by modifying the callback struct&#8217;s data fields. When the application callback returns to the widget code, the type field will determine what the widget draws on the screen. If the value is <code>XbaeString</code>, then the regular string drawing function for the widget will be called with the value the applicaton assigned to the string field in the struct. If the value is <code>XbaeStringFree</code> the widget also calls <code>XtFree</code> on the string when it is not needed anymore. Else, if the value is <code>XbaePixmap</code>, the widget will do an <code>XCopyPlane()</code>, in the case of a single plane bitmap, or <code>XCopyArea()</code>, in the case of a color pixmap. The width and height of cell is passed in the struct so the application can know how big to make the pixmap. In no case will a copy of the string or the pixmap value be made. The widget also uses the <code>XmNcolumnAlignments</code> resource to determine the horizontal alignment of the Pixmap. To have an editable array of data when the <code>XmNdrawCellCallback</code> is used and the cell is of type XbaeString or XbaeStringFree, use the <code>XmNwriteCellCallback</code>.</p>
<dt><code>XmNenterCellCallback</code></p>
<dd>Specifies a list of callbacks to be called immediately before a cell is to be edited. This callback list is called by the EditCell() action. A pointer to an <code>XbaeMatrixEnterCellCallbackStruct</code> is passed to the callbacks. The application can specify the editability of specific cells using this callback list as well as specifying configuration options for the <code>XmText</code>.</p>
<dt><code>XmNevenRowBackground</code></p>
<dd>Specifies a background cell Pixel value to use on even rows. This allows the matrix to look like computer paper. For wider bands of color, increase the size of <code>XmNaltRowCount</code>.</p>
<dt><code>XmNfill</code></p>
<dd>If True, controls whether the matrix should fill all of its available space when additional space if available, or if it should simply size itself as large as necessary, regardless of any additonal available space.</p>
<dt><code>XmNhorzFill</code></p>
<dd>If True, controls whether the matrix should highlight available space on the right of the selected cell(s) when the selected cell(s) are in the last column of the matrix.</p>
<dt><code>XmNvertFill</code></p>
<dd>If True, controls whether the matrix should highlight available space below the selected cell(s) when the selected cell(s) are in the last row of the Matrix.</p>
<dt><code>XmNfixedColumns</code></p>
<dd>Specifies the number of leading columns (starting from the left column) which should not be horizontally scrollable. <code>XmNfixedColumns</code> must be less than <code>XmNcolumns</code>&#8211;<code>XmNtrailingFixedColumns</code>. Cells in fixed columns are not editable unless <code>XmNtraverseFixedCells</code> is set to True.</p>
<dt><code>XmNfixedRows</code></p>
<dd>Specifies the number of leading rows (starting from the top row) which should not be vertically scrollable. <code>XmNfixedRows</code> must be less than <code>XmNrows</code>&#8211;<code>XmNtrailingFixedRows</code>. Cells in fixed rows are not editable unless <code>XmNtraverseFixedCells</code> is set to True.</p>
<dt><code>XmNfontList</code></p>
<dd>If the value of <code>XmNrenderTable </code> is NULL this resource specifies the font list to be used for the text displayed in the cells and the <code>XmText</code> cell edit widget. See <code><a href="//www.systutorials.com/docs/linux/man/3X-XmFontListCreate/">XmFontListCreate</a>(3X)</code> to create a font list. This resource is copied. The preferred way of specifying a font for the table is in a resource file. </p>
<p> When drawing a cell, the matrix uses the first entry with the tag <code>XmFONTLIST_DEFAULT_TAG </code> if no tag has been set on the cell using <code>XbaeMatrixSetCellTag.</code> If a tag has been set on the cell the first entry with a matching tag is used.</p>
<dt><code>XmNgridLineColor</code></p>
<dd>Specifies the color in which the grid line should be drawn if <code>XmNgridType</code> is set to <code>XmGRID_CELL_LINE</code>, <code>XmGRID_ROW_LINE</code> or <code>XmGRID_COLUMN_LINE</code>. The default is that of <code>XmNforeground</code>.</p>
<dt><code>XmNgridType</code></p>
<dd>Sets the way the matrix grid is drawn. The grid types available include <code>XmGRID_NONE</code>, <code>XmGRID_CELL_LINE</code>, <code>XmGRID_CELL_SHADOW</code>, <code>XmGRID_ROW_LINE</code>, <code>XmGRID_ROW_SHADOW</code>, <code>XmGRID_COLUMN_LINE</code> and <code>XmGRID_COLUMN_SHADOW</code>. All of the grid types vary the way the shadow or line is drawn around the cell. <code>XmGRID_ROW_LINE</code>, <code>XmGRID_ROW_SHADOW</code>, <code>XmGRID_COLUMN_LINE</code>, and <code>XmGRID_COLUMN_SHADOW</code> only draw a border around the rows and columns, giving a more tabular rather than spreadsheet appearance. The default is <code>XmGRID_CELL_LINE</code> which draws a solid line around the cells.</p>
<dt><code>XmNhighlightedCells</code></p>
<dd>Points to an array of pointers to rows. Each row is an array of unsigned char values, one for each column in that row. This data structure is the same as that for <code>XmNcells</code>, except each entry is an unsigned char instead of a String. Each entry in the array will have a value that is either <code>HighlightNone</code>, <code>HighlightCell</code>, <code>HighlightRow</code>, <code>HighlightColumn</code>, <code>HighlightOther</code> or the bitwise OR of those values, depending on the value of <code>XmNgridType</code> and which call was used to highlight the cell. A cell will be drawn as highlighted if the corresponding unsigned char does not have the value <code>HighlightNone</code>. If <code>XmNhighlightedCells</code> is <font SIZE="-1">NULL,</font> <code>XbaeMatrix</code> then no cells have been highlighted. This resource is copied, and cannot be specified in a resource file.</p>
<dt><code>XmNhorizontalScrollBar</code></p>
<dd>The widget ID of the horizontal <code>XmScrollBar</code>. This resource exists only for those applications that need to tie another scrollbar to the matrix&#8217;s for synchronized scrolling. This resource can not be set to a new value.</p>
<dt><code>XmNhorizontalScrollBarDisplayPolicy</code></p>
<dd>Determines when to display a horizontal scrollbar in the matrix. Possible values are <code>XmDISPLAY_NONE</code>, which makes the matrix never display the scrollbar, <code>XmDISPLAY_AS_NEEDED</code>, which makes the matrix display the scrollbar when the list is too large, and <code>XmDISPLAY_STATIC</code>, which makes the matrix always display the scrollbar.</p>
<dt><code>XmNlabelFont</code></p>
<dd>If the value of <code>XmNrenderTable </code> is NULL this resource specifies the font list to be used for the text displayed in row and column labels. If <code>XmNlabelFont</code> is not specified, the value of <code>XmNfontList </code> is used for the label fonts. See <code><a href="//www.systutorials.com/docs/linux/man/3X-XmFontListCreate/">XmFontListCreate</a>(3X)</code> to create a font list. This resource is copied. The preferred way of specifying a font for the labels is in a resource file. </p>
<p> When drawing a label, the matrix uses the first entry with the tag <code>XmFONTLIST_DEFAULT_TAG.</code> </p>
<dt><code>XmNlabelActivateCallback</code></p>
<dd>Specifies a list of callbacks to be called after a button label has been pressed. A pointer to an <code>XbaeMatrixLabelActivateCallbackStruct</code> is passed to the callbacks on this list.</p>
<dt><code>XmNleaveCellCallback</code></p>
<dd>Specifies a list of callbacks to be called immediately after a cell has been edited. This callback list is called by the EditCell() and CommitEdit() actions. A pointer to an <code>XbaeMatrixLeaveCellCallbackStruct</code> is passed to the callbacks. The application can perform cell specific data checks using this callback list.</p>
<dt><code>XmNleftColumn</code></p>
<dd>Allows the programmer to specify the first non fixed column to appear on the leftmost side of the matrix. This resource compliments the <code>XmNtopRow</code> resource. See the discussion of <code>XmNtopRow</code> for more details.</p>
<dt><code>XmNmodifyVerifyCallback</code></p>
<dd>Specifies a list of callbacks to be called before text is deleted from or inserted into the <code>XmText</code> cell edit widget. A pointer to an <code>XbaeMatrixModifyVerifyCallbackStruct</code> is passed to the callbacks. See the description of the <code><a href="//www.systutorials.com/docs/linux/man/3X-XmText/">XmText</a>(3X) XmNmodifyVerifyCallback</code> resource.</p>
<dt><code>XmNmultiLineCell</code></p>
<dd>is a boolean (default False) which specifies whether the matrix displays more than one line of text in a cell, when appropriate.</p>
<dt><code>XmNnonFixedDetachedLeft</code></p>
<dd>Indicated that empty space should be displayed after the fixed rows. This resource only has effect when <code>XmNfill</code> is true and <code>XmNfixedRows</code> is greater than zero.</p>
<dt><code>XmNnonFixedDetachedTop</code></p>
<dd>Indicated that empty space should be displayed after the fixed columns. This resource only has effect when <code>XmNfill</code> is true and <code>XmNfixedColumns</code> is greater than zero.</p>
<dt><code>XmNoddRowBackground</code></p>
<dd>Specifies a background cell color to use on odd rows. This allows the matrix to look like computer paper. For wider bands of color, increase the size of <code>XmNaltRowCount</code>.</p>
<dt><code>XmNprocessDragCallback</code></p>
<dd>Specifies a list of callbacks to be called from the ProcessDrag() action A pointer to an <code>XbaeMatrixProcessDragCallbackStruct</code> will be passed to the callbacks. The application can use this callback list to perform particular processing during a drag.</p>
<dt><code>XmNrenderTable</code></p>
<dd>Specifies the render table used to derive a font set or a font to draw the text displayed in the cells, the <code>XmText</code> cell edit widget and the labels. </p>
<p> When drawing a cell, the matrix uses the first entry with the tag <code>_MOTIF_DEFAULT_LOCALE</code> if no tag has been set on the cell using <code>XbaeMatrixSetCellTag.</code> If a tag has been set on the cell the first entry with a matching tag is used. </p>
<p> When drawing a label, the matrix uses the first entry with the tag &quot;labels&quot;. If there is no such entry the first entry with the tag <code>_MOTIF_DEFAULT_LOCALE</code> is used. </p>
<dt><code>XmNresizeCallback</code></p>
<dd>Specifies a list of callbacks to be called when the matrix is resized.</p>
<dt><code>XmNresizeColumnCallback</code></p>
<dd>Specifies a list of callbacks to be called when a column is dynamically resized by the user.</p>
<dt><code>XmNreverseSelect</code></p>
<dd>Overrides the default <code>XmNselectedForeground</code> and <code>XmNselectedBackground</code> and draws a selected cell in the colours specified by <code>XmNcellBackgrounds</code> and <code>XmNcolors</code> for the particular cell. If these values are not set then the default colours will be used.</p>
<dt><code>XmNrowButtonLabels</code></p>
<dd>An array of Booleans that tells the <code>XbaeMatrix</code> which row labels should be drawn as a button. Each Boolean can be specified as a Boolean string or integer. In order to use this resource, <code>XmNbuttonLabels</code> should be set to False.</p>
<dt><code>XmNrowLabelAlignment</code></p>
<dd>Specifies the alignment of the row labels. It can be one of <code>XmALIGNMENT_BEGINNING</code>, <code>XmALIGNMENT_CENTER</code> or <code>XmALIGNMENT_END</code>. See the description of <code>XmNalignment</code> for <code><a href="//www.systutorials.com/docs/linux/man/3X-XmLabel/">XmLabel</a>(3X)</code>. <code>XmNrowLabelAlignment</code> defaults to <code>XmALIGNMENT_END</code>.</p>
<dt><code>XmNrowLabelColor</code></p>
<dd>Specifies a Pixel value in which to draw the <code>XmNrowLabels</code>.</p>
<dt><code>XmNrowLabelWidth</code></p>
<dd>Specifies the width of the row labels. <code>XmNrowLabelWidth</code> defaults to the width of the longest row label.</p>
<dt><code>XmNrowLabels</code></p>
<dd>Points to an array of Strings to be drawn to the left of each row. Each String may have embedded newline characters, in which case the label will be drawn on multiple lines. If there is a <code>XmNxmRowLabels </code> defined for this row it will be displayed in place of the <code>XmNrowLabels. </code> If <code>XmNrowLabels</code> and <code>XmNxmRowLabels</code> are <font SIZE="-1">NULL, </font> no labels will be drawn. This resource is copied.</p>
<dt><code>XmNrowHeightInPixels</code></p>
<dd>Specifies wether the elements of <code>XmNrowHeights </code> are measured in pixels or lines.</p>
<dt><code>XmNrowHeights</code></p>
<dd>Points to an array of short, one for each row. These specify the visible height of the cells in each row. This resource is copied.</p>
<dt><code>XmNrowShadowTypes</code></p>
<dd>Specifies on a per row basis, the <code>XmNcellShadowType</code>. Values for the resource are the same as for <code>XmNcellShadowType</code>. This resource is copied.</p>
<dt><code>XmNrowUserData</code></p>
<dd>Points to a user defined data area associated with a particular row. The data should be set using <code>XbaeMatrixSetRowUserData()</code> and retrieved using <code>XbaeMatrixGetRowUserData()</code>. This resource cannot be specified in a resource file.</p>
<dt><code>XmNrows</code></p>
<dd>Specifies the total number of rows of cells. <code>XmNrows</code> must be at least one. If the number of rows is changed via XtSetValues, then <code>XmNrowLabels</code> must change or be <font SIZE="-1">NULL.</font> The preferred way to dynamically change the number of rows is to use <code>XbaeMatrixAddRows()</code> or <code>XbaeMatrixDeleteRows()</code>.</p>
<dt><code>XmNscrollBarPlacement</code></p>
<dd>Determines where the scrollbars will be drawn. See the discussion of <code>XmNscrollBarPlacement</code> in <code><a href="/docs/linux/man/3-xmscrolledwindow/">XmScrolledWindow</a>(3)</code> for a complete discussion on this resource.</p>
<dt><code>XmNselectCellCallback</code></p>
<dd>Specifies a list of callbacks to be called from the SelectCell() action. A pointer to an <code>XbaeMatrixSelectCellCallbackStruct</code> will be passed to the callbacks. The application can use this callback list to perform selection/deselection of cells using the provided widget methods.</p>
<dt><code>XmNselectScrollVisible</code></p>
<dd>Specifies whether the matrix will scroll to make the selected cell visible. This flag is only checked when cells are selected programmatically, as when the user selects a cell with the mouse, it will already be visible.</p>
<dt><code>XmNselectedBackground</code></p>
<dd>Allows the background of selected cells in <code>XmNselectedCells</code> to be specified.</p>
<dt><code>XmNselectedCells</code></p>
<dd>Points to an array of pointers to rows. Each row is an array of Boolean values, one for each column in that row. This data structure is the same as that for <code>XmNcells</code>, except each entry is a Boolean instead of a String. A cell will be drawn as selected if the corresponding Boolean is True. If <code>XmNselectedCells</code> is <font SIZE="-1">NULL,</font> then no cells have been selected. This resource is copied. It cannot be specified in a resource file.</p>
<dt><code>XmNselectedForeground</code></p>
<dd>Allows the foreground of selected cells in <code>XmNselectedCells</code> to be specified.</p>
<dt><code>XmNshadowType</code></p>
<dd>Specifies the type of shadow drawn around the border of the matrix. Possible values for this resource are <code>XmSHADOW_OUT</code>, <code>XmSHADOW_IN</code>, <code>XmSHADOW_ETCHED_OUT</code>, and <code>XmSHADOW_ETCHED_IN</code>. The default shadow type is XmSHADOW_OUT.</p>
<dt><code>XmNshowArrows</code></p>
<dd>Specifies whether arrows should be drawn when data in a cell has been obscured due to the value of <code>XmNcolumnWidths</code>.</p>
<dt><code>XmNspace</code></p>
<dd>Specifies the distance that separates the ScrollBars from the cell grid. The default value is 4 pixels.</p>
<dt><code>XmNtextBackground</code></p>
<dd>Specifies the background of the <code>XmText</code> cell edit widget. This can be used to make the <code>XmText</code> stand out against a uniformly colored matrix.</p>
<dt><code>XmNtextBackgroundIsCell</code></p>
<dd>Specifies if the background of the <code>XmText</code> cell edit widget defaults to the core background of the matrix or the background of the cell being edited when <code>XmNtextBackground</code> has the value <code>XmUNSPECIFIED_PIXEL.</code></p>
<dt><code>XmNtextField</code></p>
<dd>The widget ID of the <code>XmText</code>. This resource cannot be set to a new value.</p>
<dt><code>XmNtextShadowThickness</code></p>
<dd>Specifies the <code>XmNshadowThickness</code> of the <code>XmText</code>. Interesting effects can be achieved by setting the <code>XmNcellHighlightThickness</code> to 0 and replacing the highlight with an indented shadow.</p>
<dt><code>XmNtextTranslations</code></p>
<dd>Specifies the <code>XmNtranslations</code> resource of the <code>XmText</code> cell edit widget. See the description of <code>XmNtranslations</code> in <code><a href="//www.systutorials.com/docs/linux/man/3X-XmText/">XmText</a>(3X)</code>.</p>
<dt><code>XmNtopRow</code></p>
<dd>Specifies the row which should be displayed at the top of the non-fixed rows. <code>XmNtopRow</code> is specified relative to the first non-fixed row, so (XmNfixedRows + XmNtopRow) is the actual row number which will be moved to the top. If (XmNtopRow &gt; (XmNrows &#8211; (&lt;number of rows visible&gt; + XmNfixedRows), then the actual row which will be moved to the top is (XmNrows &#8211; (&lt;number of rows visible&gt; + XmNfixedRows).</p>
<dt><code>XmNtrackCellCallback</code></p>
<dd>specifies a list of callbacks to be called when the mouse pointer is being moved.</p>
<dt><code>XmNtrailingAttachedBottom</code></p>
<dd>Indicated that any trailing fixed rows should be attached to the bottom of the matrix. This resource only has effect when <code>XmNfill</code> is true and <code>XmNtrailingFixedRows</code> is greater than zero.</p>
<dt><code>XmNtrailingAttachedRight</code></p>
<dd>Indicated that any trailing fixed columns should be attached to the right of the matrix. This resource only has effect when <code>XmNfill</code> is true and <code>XmNtrailingFixedColumns</code> is greater than zero.</p>
<dt><code>XmNtrailingFixedColumns</code></p>
<dd>Specifies the number of trailing columns (starting from the right column) which should not be horizontally scrollable. <code>XmNtrailingFixedColumns</code> must be less than <code>XmNcolumns</code>&#8211;<code>XmNfixedColumns</code>. Cells in trailing fixed columns are not editable unless <code>XmNtraverseFixedCells</code> is set to True.</p>
<dt><code>XmNtrailingFixedRows</code></p>
<dd>Specifies the number of trailing rows (starting from the bottom row) which should not be vertically scrollable. <code>XmNtrailingFixedRows</code> must be less than <code>XmNrows</code>&#8211;<code>XmNfixedRows</code>. Cells in trailing fixed rows are not editable unless <code>XmNtraverseFixedCells</code> is set to True.</p>
<dt><code>XmNtraverseCellCallback</code></p>
<dd>Specifies a list of callbacks to be called before a new cell is edited. These callbacks are called by the EditCell() action and when <code>XbaeMatrix</code> receives or looses focus. A pointer to an <code>XbaeMatrixTraverseCellCallbackStruct</code> is passed to the callbacks. The application can specify the next cell which should be edited via this callback list, thereby performing custom traversal.</p>
<dt><code>XmNtraverseFixedCells</code></p>
<dd>If True, this resource allows fixed cells and columns to be edited. The default is to not allow fixed rows or columns to be edited.</p>
<dt><code>XmNuseXbaeInput</code></p>
<dd>This boolean value determines whether to use XbaeInput or XmTextField as the widget used for editing cells. Default is not to use XbaeInput.</p>
<dt><code>XmNvalueChangedCallback</code></p>
<dd>Specifies a list of callbacks to be called after text is deleted from or inserted into the <code>XmText</code> cell edit widget. A pointer to an <code>XbaeMatrixValueChangedCallbackStruct</code> is passed to the callbacks. See the description of the <code><a href="//www.systutorials.com/docs/linux/man/3X-XmText/">XmText</a>(3X) XmNvalueChangedCallback</code> resource.</p>
<dt><code>XmNverticalScrollBar</code></p>
<dd>The widget ID of the vertical <code>XmScrollBar</code>. This resource exists only for those applications that need to tie another scrollbar to the matrix&#8217;s for synchronized scrolling. This resource can not be set to a new value.</p>
<dt><code>XmNverticalScrollBarDisplayPolicy</code></p>
<dd>Determines when to display a horizontal scrollbar in the matrix. Possible values and their effects are listed under <code>XmNhorizontalScrollBarDisplayPolicy</code>.</p>
<dt><code>XmNvisibleColumns</code></p>
<dd>Specifies the number of non-fixed columns which should be visible. The widget will request a size which will allow <code>XmNvisibleColumns</code> columns to be displayed. The programmer should take into allowance any <code>XmNfixedColumns</code> that are specified. This feature becomes even more apparent if the number of <code>XmNfixedColumns</code> changes at runtime as the value may need to be adjusted to avoid a warning.</p>
<dt><code>XmNvisibleRows</code></p>
<dd>Specifies the number of rows which should be visible at any one time. The widget will request a size which will allow <code>XmNvisibleRows</code> rows to be displayed.</p>
<dt><code>XmNwrapType</code></p>
<dd>When <code>XmNmultiLineCell </code> is true this resource specifies how to break the lines. When set to XbaeWrapNone, lines are broken on newlines only. When set to XbaeWrapContinuous, long lines are further broken up so they fit in their cell. When set to XbaeWrapWord the breaking of long lines occures preferably on spaces.</p>
<dt><code>XmNwriteCellCallback</code></p>
<dd>Specifies a list of callbacks to be called when a cell value changes and an <code>XmNdrawCellCallback</code> is defined. A pointer to an <code>XbaeMatrixWriteCellCallbackStruct</code> is passed to the callbacks. The <code>XmNwriteCellCallback</code> allows data to be written back into the application&#8217;s data structure and must be defined for an editable <code>XbaeMatrix</code> with an <code>XmNdrawCellCallback</code>.</p>
<dt><code>XmNxmRowLabels</code></p>
<dd>Points to an array of XmStrings to be drawn to the left of each row. If <code>XmNxmRowLabels</code> is <font SIZE="-1">NULL, </font> <code>XmNrowLabels </code> will be used. This resource is copied.</p>
<dt><code>XmNxmColumnLabels</code></p>
<dd>Points to an array of XmStrings to be drawn above each column. If <code>XmNxmColumnLabels</code> is <font SIZE="-1">NULL, </font> <code>XmNcolumnLabels </code> will be used. This resource is copied.</dl>
<h2>Inherited Resources</h2>
<p>The following table lists the resources which <code>XbaeMatrix</code> inherits from it&#8217;s superclasses <code>XmManager</code>, <code>Compositeand</code> <code>Core</code>. For a complete description of each resource, refer to the man page for that superclass. The codes in the &#8220;Access&#8221; column indicate whether the given resource can be set at creation time (C), or set by using XtSetValues (S), or retrieved by using XtGetValues (G). </p>
<table BORDER>
<tr>
<td>
<table WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>XmManager Resource Set
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
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
<td COLSPAN=5>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNbottomShadowColor</font></td>
<td><font SIZE="-9">XmCBottomShadowColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNbottomShadowPixmap</font></td>
<td><font SIZE="-9">XmCBottomShadowPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">XmUNSPECIFIED_PIXMAP</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNforeground</font></td>
<td><font SIZE="-9">XmCForeground</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNhighlightColor</font></td>
<td><font SIZE="-9">XmCHighlightColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNhighlightPixmap</font></td>
<td><font SIZE="-9">XmCHighlightPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNinitialFocus</font></td>
<td><font SIZE="-9">XmCInitialFocus</font></td>
<td><font SIZE="-9">Widget</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNnavigationType</font></td>
<td><font SIZE="-9">XmCNavigationType</font></td>
<td><font SIZE="-9">XmNavigationType</font></td>
<td><font SIZE="-9">XmTAB_GROUP</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNshadowThickness</font></td>
<td><font SIZE="-9">XmCShadowThickness</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNstringDirection</font></td>
<td><font SIZE="-9">XmCStringDirection</font></td>
<td><font SIZE="-9">XmStringDirection</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtopShadowColor</font></td>
<td><font SIZE="-9">XmCTopShadowColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtopShadowPixmap</font></td>
<td><font SIZE="-9">XmCTopShadowPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtraversalOn</font></td>
<td><font SIZE="-9">XmCTraversalOn</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNunitType</font></td>
<td><font SIZE="-9">XmCUnitType</font></td>
<td><font SIZE="-9">unsigned char</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNuserData</font></td>
<td><font SIZE="-9">XmCUserData</font></td>
<td><font SIZE="-9">XtPointer</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td>
<table WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>Composite Resource Set
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
<hr>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNchildren</font></td>
<td><font SIZE="-9">XmCReadOnly</font></td>
<td><font SIZE="-9">WidgetList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">G</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNinsertPosition</font></td>
<td><font SIZE="-9">XmCInsertPosition</font></td>
<td><font SIZE="-9">XtOrderProc</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNnumChildren</font></td>
<td><font SIZE="-9">XmCReadOnly</font></td>
<td><font SIZE="-9">Cardinal</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">G</font>
</td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td>
<table WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>Core Resource Set
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
<hr>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNaccelerators</font></td>
<td><font SIZE="-9">XmCAccelerators</font></td>
<td><font SIZE="-9">XtAccelerators</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNancestorSensitive</font></td>
<td><font SIZE="-9">XmCSensitive</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">G</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNbackground</font></td>
<td><font SIZE="-9">XmCBackground</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNbackgroundPixmap</font></td>
<td><font SIZE="-9">XmCPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">XmUNSPECIFIED_PIXMAP</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNborderColor</font></td>
<td><font SIZE="-9">XmCBorderColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">XtDefaultForeground</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNborderPixmap</font></td>
<td><font SIZE="-9">XmCPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">XmUNSPECIFIED_PIXMAP</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNborderWidth</font></td>
<td><font SIZE="-9">XmCBorderWidth</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">1</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolormap</font></td>
<td><font SIZE="-9">XmCColormap</font></td>
<td><font SIZE="-9">Colormap</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNdepth</font></td>
<td><font SIZE="-9">XmCDepth</font></td>
<td><font SIZE="-9">int</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNdestroyCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">XtCallbackList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">C</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNheight</font></td>
<td><font SIZE="-9">XmCHeight</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNinitialResourcesPersistent</font></td>
<td><font SIZE="-9">XmCInitialResourcesPersistent</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">C</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNmappedWhenManaged</font></td>
<td><font SIZE="-9">XmCMappedWhenManaged</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNscreen</font></td>
<td><font SIZE="-9">XmCScreen</font></td>
<td><font SIZE="-9">Screen</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNsensitive</font></td>
<td><font SIZE="-9">XmCSensitive</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtranslations</font></td>
<td><font SIZE="-9">XmCTranslations</font></td>
<td><font SIZE="-9">XtTranslations</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNwidth</font></td>
<td><font SIZE="-9">XmCWidth</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNx</font></td>
<td><font SIZE="-9">XmCPosition</font></td>
<td><font SIZE="-9">Position</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNy</font></td>
<td><font SIZE="-9">XmCPosition</font></td>
<td><font SIZE="-9">Position</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
</table>
</table>
<h2>Callback Information</h2>
<dl COMPACT>
<dt><code>XbaeMatrixAnyCallbackStruct</code></p>
<dd>A callback struct that is suitable for all callbacks that require the <i>reason</i>, <i>event</i>, <i>row</i> and <i>column</i> to be available. Any callback called may therefore cast the third parameter to the following struct in <code>XbaeMatrix</code> and can rest assured that evrything in it will be available. </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeReasonType</code></td>
<td><i>reason;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XEvent</code></td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixAnyCallbackStruct;</code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>Each of the members are set to the appropriate struct for the callback. </p>
<p> If this idea is a little foreign to you, recommended reading is K&amp;R II page 213.</dl>
</dl>
<dl COMPACT>
<dt><code>XmNdefaultActionCallback</code></p>
<dd>Callbacks on the <code>XmNdefaultActionCallback</code> list are called when the DefaultAction() action occurs. The application can bind the DefaultAction() action to any pointer based event. When a double click occurs on this pointer event, DefaultAction() will call the callbacks on the <code>XmNdefaultActionCallback</code> list. A pointer to the following structure is passed to each callback on the <code>XmNdefaultActionCallback</code> list: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeReasonType</code></td>
<td><i>reason;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XEvent</code></td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixDefaultActionCallbackStruct;</code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XbaeDefaultActionReason .</code></p>
<dt><i>event</i></p>
<dd>The event that invoked this callback.</p>
<dt><i>row</i></p>
<dd>The row number of the cell in which the double click occurred.</p>
<dt><i>column</i></p>
<dd>The column number of the cell in which the double click occurred.</p>
<dt><i>event</i></p>
<dd></dl>
<p> If an application has an <code>XmNdefaultActionCallback</code>, then the callbacks on the list will be called when the user clicks twice in a cell within <code>XmNdoubleClickInterval</code>, enabling some action to occur for the particular cell.</dl>
</dl>
<dl COMPACT>
<dt><code>XmNdrawCellCallback</code></p>
<dd>Callbacks on the <code>XmNdrawCellCallback</code> list are called when the widget needs to draw a cell. A pointer to the following structure is passed to each callback on the <code>XmNdrawCellCallback</code> list: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeReasonType</code></td>
<td><i>reason;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XEvent</code></td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>width;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>height;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeCellType</code></td>
<td><i>type;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>String</code></td>
<td><i>string;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Pixmap</code></td>
<td><i>pixmap;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Pixmap</code></td>
<td><i>mask;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Pixel</code></td>
<td><i>foreground;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Pixel</code></td>
<td><i>background;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>depth;</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixDrawCellCallbackStruct;</code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XbaeDrawCellReason</code>.</p>
<dt><i>event</i></p>
<dd>Always set to <font SIZE="-1">NULL</font></p>
<dt><i>row</i></p>
<dd>The row number of the cell that needs to be drawn.</p>
<dt><i>column</i></p>
<dd>The column number of the cell that needs to be drawn.</p>
<dt><i>width</i></p>
<dd>The width of the cell that needs to be drawn.</p>
<dt><i>height</i></p>
<dd>The height of the cell that needs to be drawn.</p>
<dt><i>type</i></p>
<dd>The type of &#8220;data&#8221; the programmer wants drawn in the cell, or which field should be looked at for data to draw: string or pixmap.</p>
<dt><i>string</i></p>
<dd>The string to draw if <i>type</i> is set to <code>XbaeString</code> or <code>XbaeStringFree</code>.</p>
<dt><i>pixmap</i></p>
<dd>The pixmap to copy if <i>type</i> is set to <code>XbaePixmap</code>. It will be clipped to width by height if necessary.</p>
<dt><i>mask</i></p>
<dd>A mask for the pixmap as obtained from the XPM library. <i>mask</i> is only necessary when <i>pixmap</i> has a depth greater than one.</p>
<dt><i>foreground</i></p>
<dd>The foreground color of the cell.</p>
<dt><i>background</i></p>
<dd>The background color of the cell.</p>
<dt><i>depth</i></p>
<dd>The depth of the pixmap image (in bits per pixel).</dl>
<p> If the application adds this callback, when the <code>XbaeMatrix</code> determines that a cell at (row, column) needs to be redrawn, the normal cell drawing mechanism will be skipped and this callback called so the application can tell the widget what to put in the cell. </p>
<p> The <i>type</i> field is defaulted to <code>XbaeString</code> and no cacheing or saving of the string or pixmap is done. </p>
<p> If the application sets <i>type</i> to XbaePixmap, the width, height and depth of the returned pixmap will be calculated with a call to <code>XGetGeometry()</code>. If the programmer wishes to supply the width, height and depth there is a marked improvement as a round trip to the X server is avoided. Note that all geometry parameters must be supplied to ensure successful display of the pixmap. </p>
<p> If a <i>mask</i> is also provided, it will be used to display the pixmap transparently. Pixmaps drawn in cells also respect the value of <code>XmNcolumnAlignments</code>. </p>
<p> By defining an <code>XmNdrawCellCallback</code> the need for the storage of the <code>XbaeMatrix</code> data within the matrix is eliminated and can prove to be advantageous for memory usage. </p>
<p> To write the data back to the application, use the <code>XmNwriteCellCallback</code> described below.</dl>
<dt><code>XmNenterCellCallback</code></p>
<dd>Callbacks on the <code>XmNenterCellCallback</code> list are called from the EditCell() action just before a cell is edited to determine it&#8217;s editability. A pointer to the following structure is passed to each callback on the <code>XmNenterCellCallback</code> list: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeReasonType</code></td>
<td><i>reason;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XEvent</code></td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>position;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>String</code></td>
<td><i>pattern;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Boolean</code></td>
<td><i>auto_fill;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Boolean</code></td>
<td><i>convert_case;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Boolean</code></td>
<td><i>overwrite_mode;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Boolean</code></td>
<td><i>select_text;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Boolean</code></td>
<td><i>map;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Cardinal</code></td>
<td><i>num_params;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>String</code></td>
<td><i>*params;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Boolean</code></td>
<td><i>doit;</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixEnterCellCallbackStruct;</code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XbaeEnterCellReason</code>.</p>
<dt><i>event</i></p>
<dd>The event that invoked the callback.</p>
<dt><i>row</i></p>
<dd>The row number of the cell about to be edited.</p>
<dt><i>column</i></p>
<dd>The column number of the cell about to be edited.</p>
<dt><i>position</i></p>
<dd>The location of the cursor in the text field. The default is to place the cursor at the end of the string in the cell.</p>
<dt><i>pattern</i></p>
<dd>A pattern for the <code>XbaeInput</code> widget (see <a href="/docs/linux/man/3-xbaeinput/">XbaeInput</a>(3)). The default is to not specify a <i>pattern</i>.</p>
<dt><i>auto_fill</i></p>
<dd>Used in conjunction with the setting of the <i>pattern</i> to allow literals in the <i>pattern</i> to be automatically inserted.</p>
<dt><i>convert_case</i></p>
<dd>If the <i>pattern</i> specifies an upper or lower case letter, the character typed in the position can automatically be converted to the appropriate case when set to True. The default is to not convert the case of the typed letter.</p>
<dt><i>overwrite_mode</i></p>
<dd>Normally, the cursor appears as the familiar I caret. By setting <i>overwrite_mode</i> to True, the text field will go into overwrite mode where keystrokes replace the character underneath the block cursor.</p>
<dt><i>select_text</i></p>
<dd>Indicates whether the text in the cell should be highlighted (only valid if <i>doit</i> is set to True also.</p>
<dt><i>map</i></p>
<dd>Tells the matrix if the <code>XmText</code> should be mapped onto the cell. Only makes sense if <i>doit</i> is set to False.</p>
<dt><i>num_params</i></p>
<dd>The number of String parameters passed to the EditCell() action.</p>
<dt><i>params</i></p>
<dd>An array containing the num_params String parameters passed to the EditCell() action.</p>
<dt><i>doit</i></p>
<dd>Indicates whether or not this cell is editable. Setting doit to False will make this cell not editable. The default value is True.</dl>
<p> If the application determines that the cell at (<i>row</i>, <i>column</i>) is not editable, it should set the doit flag to False. If the <i>map</i> flag is also set to False, <code>XbaeMatrix</code> will not place the <code>XmText</code> cell editor on the cell. If <i>map</i> is left as True, the <code>XmText</code> will be placed on the cell but the user will not be able to add or delete characters from it. If the application leaves <i>doit</i> as True, then the TextField will be editable. In addition, if <i>select_text</i> is set to True, the text in the cell will be selected via <code>XmTextSetSelection</code>. Assuming <code>XmNpendingDelete</code> for the <code>XmText</code> is also True, the selected text will be deleted as soon as the next text insertion occurs.</dl>
</dl>
<dl COMPACT>
<dt><code>XmNlabelActivateCallback</code></p>
<dd>Callbacks on the <code>XmNlabelActivateCallback</code> list are called after a button label has been activated via a mouse click. A pointer to the following structure is passed to each callback on the <code>XmNlabelActivateCallback</code> list: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeReasonType</code></td>
<td><i>reason;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XEvent</code></td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Boolean</code></td>
<td><i>row_label;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>String</code></td>
<td><i>label;</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixLabelActivateCallbackStruct;</code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XbaeLabelActivateReason</code>.</p>
<dt><i>event</i></p>
<dd>The event that invoked this callback.</p>
<dt><i>row</i></p>
<dd>The row number of the button label or -1 if the button was a column label.</p>
<dt><i>column</i></p>
<dd>The column number of the button label or -1 if the button was a row label.</p>
<dt><i>row_label</i></p>
<dd>If the button label that invoked the callback is a row label, then this value is set to True. If it was a column label then it is set to False.</p>
<dt><i>label</i></p>
<dd>The label on the button that was pressed.</dl>
<p> When the <code>XbaeMatrix</code> receives a ButtonRelease event on the same button label that it received a ButtonPress event, the <code>XmNlabelActivateCallback</code> is called to allow the programmer to respond to the event. The callback has been provided to emulate some popular spreadsheets on the market.</dl>
</dl>
<dl COMPACT>
<dt><code>XmNleaveCellCallback</code></p>
<dd>Callbacks on the <code>XmNleaveCellCallback</code> list are called from the EditCell() and CommitEdit() actions just before the edit to the current cell is committed. The application can validate the changes made to the cell, and allow or disallow them. A pointer to the following structure is passed to each callback on the <code>XmNleaveCellCallback</code> list: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeReasonType</code></td>
<td><i>reason;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XEvent</code></td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>row, column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>String</code></td>
<td><i>value;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Boolean</code></td>
<td><i>doit;</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixLeaveCellCallbackStruct;</code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XbaeLeaveCellReason</code>.</p>
<dt><i>event</i></p>
<dd>The event that invoked this callback.</p>
<dt><i>row</i></p>
<dd>The row number of the cell being edited.</p>
<dt><i>column</i></p>
<dd>The column number of the cell being edited.</p>
<dt><i>value</i></p>
<dd>Contains the new data which will be stored in this cell if doit is True. The memory pointed to by value may be modified, or if the new contents are larger than the current contents, then value should be set to point to a larger piece of allocated memory.</p>
<dt><i>doit</i></p>
<dd>Indicates whether the edits applied to this cell should actually be stored into <code>XbaeMatrix</code>. Setting doit to False will cause the changes to be discarded and the cell will retain its original value. The default value is True.</dl>
<p> If the application determines that the value entered in the cell at (row, column) is not valid, it should set the doit flag to False. This will prevent the changes from being stored in the cell. The TextField edit widget will remain on the current cell. If the application leaves doit as True, then the changes made to the cell will be committed and the TextField will move to the next cell or be unmapped. The application can also modify the String in value, e.g. to force a String to be all upper case.</dl>
</dl>
<dl COMPACT>
<dt><code>XmNmodifyVerifyCallback</code></p>
<dd>Callbacks on the <code>XmNmodifyVerifyCallback</code> list are called while a cell is being edited. The callbacks are called before text is inserted into or deleted from the TextField edit widget. A pointer to the following structure is passed to each callback on the <code>XmNmodifyVerifyCallback</code> list: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeReasonType</code></td>
<td><i>reason;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XEvent</code></td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XmTextVerifyCallbackStruct</code></td>
<td><i>*verify;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>const char</code></td>
<td><i>*prev_text;</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixModifyVerifyCallbackStruct;</code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XbaeModifyVerifyReason</code>.</p>
<dt><i>event</i></p>
<dd>Always set to NULL.</p>
<dt><i>row</i></p>
<dd>The row number of the cell being edited.</p>
<dt><i>column</i></p>
<dd>The column number of the cell being edited.</p>
<dt><i>verify</i></p>
<dd>The contents of this structure and its use are documented in the <code><a href="//www.systutorials.com/docs/linux/man/3X-XmText/">XmText</a>(3X)</code> man page.</p>
<dt><i>prev_text</i></p>
<dd>The contents of the cell as seen by this user before the new text. If other text has already been entered, this value will not match the official <code>XbaeMatrix</code> value of the cell. This pointer and the string should not be modified.</dl>
</dl>
</dl>
<dl COMPACT>
<dt><code>XmNprocessDragCallback</code></p>
<dd>Callbacks on the <code>XmNprocessDragCallback</code> list are called from the ProcessDrag() action. The application can bind the ProcessDrag() action to any pointer based event, though by default it is bound to the Button2Down event. When this event occurs, ProcessDrag() will call the callbacks on the <code>XmNprocessDragCallback</code> list. A pointer to the following structure is passed to each callback on the <code>XmNprocessDragCallback</code> list: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeReasonType</code></td>
<td><i>reason;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XEvent</code></td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>String</code></td>
<td><i>string;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeCellType</code></td>
<td><i>type;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Pixmap</code></td>
<td><i>pixmap;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Pixmap</code></td>
<td><i>mask;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Cardinal</code></td>
<td><i>num_params;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>String</code></td>
<td><i>*params;</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixProcessDragCallbackStruct; </code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XbaeProcessDragReason</code>.</p>
<dt><i>event</i></p>
<dd>The XEvent which invoked the ProcessDrag() action.</p>
<dt><i>row</i></p>
<dd>The row number of the cell where the drag was initiated..</p>
<dt><i>column</i></p>
<dd>The column number of the cell where the drag was initiated..</p>
<dt><i>string</i></p>
<dd>The string in the cell where the drag was initiated if <i>type</i> is <code>XbaeString</code> or <code>XbaeStringFree</code>. This is provided as a convenience to the application.</p>
<dt><i>type</i></p>
<dd>The type of the cell in which the drag was initiated.</p>
<dt><i>pixmap</i></p>
<dd>The pixmap in the cell where the drag was initiated if <i>type</i> is <code>XbaePixmap</code>. This is provided as a convenience to the application.</p>
<dt><i>mask</i></p>
<dd>A mask for the pixmap as obtained from the XPM library. <i>mask</i> is only necessary when <i>pixmap</i> has a depth greater than one. Also provided as a convenience to the application.</p>
<dt><i>num_params</i></p>
<dd>The number of String parameters passed to the ProcessDrag() action.</p>
<dt><i>params</i></p>
<dd>An array containing the num_params String parameters passed to the ProcessDrag() action.</dl>
<p> The application can use the <code>XmNprocessDragCallback</code> list to implement particular processing for Motif&#8217;s drag-and-drop.</dl>
</dl>
<dl COMPACT>
<dt><code>XmNresizeCallback</code></p>
<dd>Callbacks on the <code>XmNresizeCallback</code> list are called when the <code>XbaeMatrix</code> widget is resized. A pointer to the following structure is passed to<br />
&nbsp;<wbr>each callback on the <code>XmNresizeCallback</code> list: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeReasonType</code></td>
<td><i>reason;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XEvent</code></td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Dimension</code></td>
<td><i>width;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Dimension</code></td>
<td><i>height;</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixResizeCallbackStruct; </code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XbaeResizeReason</code>.</p>
<dt><i>event</i></p>
<dd>Always set to <font SIZE="-1">NULL</font></p>
<dt><i>row</i></p>
<dd>Set to the number of rows in the matrix (provided for convenience).</p>
<dt><i>column</i></p>
<dd>Set to the number of colums in the matrix (provided for convenience).</p>
<dt><i>width</i></p>
<dd>The new width of the <code>XbaeMatrix</code> widget.</p>
<dt><i>height</i></p>
<dd>The new height of the <code>XbaeMatrix</code> widget.</dl>
<p> The application can use the <code>XmNresizeCallback</code> to adjust such resources as <code>XmNcolumnWidths</code>, <code>XmNvisibleColumns</code> and <code>XmNvisibleRows</code> when the widget containing an <code>XbaeMatrix</code> widget is resized.</dl>
</dl>
<dl COMPACT>
<dt><code>XmNresizeColumnCallback</code></p>
<dd>Callbacks on the <code>XmNresizeColumnCallback</code> list are called when a column of the <code>XbaeMatrix</code> widget is dynamically resized by the user. A pointer to the following structure is passed to each callback on the <code>XmNresizeColumnCallback</code> list: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeReasonType</code></td>
<td><i>reason;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XEvent </code></td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>which;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>columns;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>short</code></td>
<td><i>*column_widths;</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixResizeColumnCallbackStruct; </code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XbaeResizeColumnReason</code>.</p>
<dt><i>event</i></p>
<dd>The XEvent that ended the resize. The event will be of type <code>XButtonReleasedEvent</code>.</p>
<dt><i>row</i></p>
<dd>The row in which the <code>ResizeColumn()</code> action began.</p>
<dt><i>column</i></p>
<dd>The column in which the <code>ResizeColumn()</code> action began (and ended).</p>
<dt><i>which</i></p>
<dd>The column that was resized in the <code>ResizeColumn()</code> action.</p>
<dt><i>columns</i></p>
<dd>The number of columns in the <code>XbaeMatrix</code> widget.</p>
<dt><i>column_widths</i></p>
<dd>The widths of each column as they stand <i>after</i> the <code>ResizeColumn()</code> action.</dl>
<p> The application can use the <code>XmNresizeColumnCallback</code> to perform post processing after a column has been resized. By adjusting the values contained in <i>column_widths</i> the <code>XbaeMatrix</code> widget will use the values upon return from the callback. Changing the number of columns in the matrix in the <code>XmNresizeColumnCallback</code> should be used carefully as it may cause unexpected results.</dl>
</dl>
<dl COMPACT>
<dt><code>XmNselectCellCallback</code></p>
<dd>Callbacks on the <code>XmNselectCellCallback</code> list are called from the SelectCell() action. The application can bind the SelectCell() action to any pointer based event. When this event occurs, SelectCell() will call the callbacks on the <code>XmNselectCellCallback</code> list. A pointer to the following structure is passed to each callback on the <code>XmNselectCellCallback</code> list: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeReasonType</code></td>
<td><i>reason;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XEvent</code></td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Boolean</code></td>
<td><i>**selected_cells;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>String</code></td>
<td><i>**cells;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Cardinal</code></td>
<td><i>num_params;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>String</code></td>
<td><i>*params;</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixSelectCellCallbackStruct; </code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XbaeSelectCellReason</code>.</p>
<dt><i>event</i></p>
<dd>The XEvent which invoked the SelectCell() action.</p>
<dt><i>row</i></p>
<dd>The row number of the cell which was selected.</p>
<dt><i>column</i></p>
<dd>The column number of the cell which was selected.</p>
<dt><i>selected_cells</i></p>
<dd>The value of the <code>XmNselectedCells</code> resource. This is provided as a convenience to the application and will be <font SIZE="-1">NULL</font> if no cells have yet been selected.</p>
<dt><i>cells</i></p>
<dd>The value of the <code>XmNcells</code> resource. This is provided as a convenience to the application and will be <font SIZE="-1">NULL</font> if no cells have been specified or the <code>XmNdrawCellCallback</code> is being used.</p>
<dt><i>num_params</i></p>
<dd>The number of String parameters passed to the SelectCell() action.</p>
<dt><i>params</i></p>
<dd>An array containing the num_params String parameters passed to the SelectCell() action.</dl>
<p> The application can use the <code>XmNselectCellCallback</code> list to implement it&#8217;s own selection model. The <code>XbaeMatrixSelectCellCallbackStruct</code> contains the array of String parameters passed to the SelectCell() action which invoked this callback. By binding the SelectCell() action to various events via the translation manager, and using String action parameters to distinguish them, the application can implement various selection models. For example, the following translations could be used to implement a model in which a modifier key indicates whether a single cell or an entire row should be selected. The callbacks on the <code>XmNselectCellCallback</code> list would examine the parameter and take the appropriate action. </p>
<table>
<tr VALIGN=top>
<td>#override
\ </td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Shift&lt;Btn1Down&gt;:</td>
<td>SelectCell(cell)
\
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Ctrl&lt;Btn1Down&gt;:</td>
<td>SelectCell(row)
</td>
</tr>
</table>
<p> The callbacks on the <code>XmNselectCellCallback</code> list can also be used in other ways, e.g. to pop up a cell specific menu. </p>
<p> <code>NOTE:</code> If no cells have been selected, the value of <i>selected_cells</i> will be <font SIZE="-1">NULL.</font> The same applies for <i>cells</i>. Care must be taken so as not to dereference these members of the callback struct.</dl>
</dl>
<dl COMPACT>
<dt><code>XmNtrackCellCallback</code></p>
<dd>Callbacks on the <code>XmNtrackCellCallback</code> list are being called by the HandleTracking() action, which is triggered by pointer motion. One of the purposes of this callback list is to figure out from which cell to which cell the pointer is being moved. A pointer to the <code>XbaeMatrixTrackCellCallbackStruct</code> structure is being passed. Its fields are defined as : </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct _XbaeMatrixTrackCellCallbackStruct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeReasonType</code></td>
<td><i>reason;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XEvent</code></td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>row, column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>prev_row, prev_column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Position</code></td>
<td><i>pointer_x, pointer_y;</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixTrackCellCallbackStruct;</code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XbaeSelectCellReason</code>.</p>
<dt><i>event</i></p>
<dd>The XEvent which invoked the HandleTracking() action.</p>
<dt><i>row</i></p>
<dd>This is the row number that the pointer is currently in.</p>
<dt><i>column</i></p>
<dd>This is the column number that the pointer is currently in.</p>
<dt><i>prev_row</i></p>
<dd>The row that the pointer was previously in.</p>
<dt><i>prev_column</i></p>
<dd>The column that the pointer was previously in.</p>
<dt><i>pointer_x</i></p>
<dd>The x position of the pointer.</p>
<dt><i>pointer_y</i></p>
<dd>The y position of the pointer.</dl>
</dl>
</dl>
<dl COMPACT>
<dt><code>XmNtraverseCellCallback</code></p>
<dd>Callbacks on the <code>XmNtraverseCellCallback</code> list are called from the EditCell() action and when <code>XbaeMatrix</code> receives or looses focus. The application can customize cell traversal using these callbacks. <code>XbaeMatrix</code> has a default traversal order, outlined below, which the application can override. A pointer to the following structure is passed to each callback on the <code>XmNtraverseCellCallback</code> list: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeReasonType</code></td>
<td><i>reason;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XEvent</code></td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>next_row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>next_column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>fixed_rows;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>fixed_columns;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>trailing_fixed_rows;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>trailing_fixed_columns;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>num_rows;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>num_columns;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>String</code></td>
<td><i>param;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XrmQuark</code></td>
<td><i>qparam;</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixTraverseCellCallbackStruct;</code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XbaeTraverseCellReason</code>.</p>
<dt><i>event</i></p>
<dd>The event that invoked this callback.</p>
<dt><i>row</i></p>
<dd>The row number of the cell currently being edited.</p>
<dt><i>column</i></p>
<dd>The column number of the cell currently being edited.</p>
<dt><i>next_row</i></p>
<dd>The row number of the next cell to be edited, this can be changed by the application.</p>
<dt><i>next_column</i></p>
<dd>The column number of the next cell to be edited, this can be changed by the application.</p>
<dt><i>fixed_rows</i></p>
<dd>The value of the <code>XmNfixedRows</code> resource. This is provided as a convenience for the application in calculating the next_row and next_column fields.</p>
<dt><i>fixed_columns</i></p>
<dd>The value of the <code>XmNfixedColumns</code> resource. This is provided as a convenience for the application in calculating the next_row and next_column fields.</p>
<dt><i>trailing_fixed_rows</i></p>
<dd>The value of the <code>XmNtrailingFixedRows</code> resource. This is provided as a convenience for the application in calculating the next_row and next_column fields.</p>
<dt><i>trailing_fixed_columns</i></p>
<dd>The value of the <code>XmNtrailingFixedColumns</code> resource. This is provided as a convenience for the application in calculating the next_row and next_column fields.</p>
<dt><i>num_rows</i></p>
<dd>The value of the <code>XmNrows</code> resource. This is provided as a convenience for the application in calculating the next_row and next_column fields.</p>
<dt><i>num_columns</i></p>
<dd>The value of the <code>XmNcolumns</code> resource. This is provided as a convenience for the application in calculating the next_row and next_column fields.</p>
<dt><i>param</i></p>
<dd>The String value of the parameter passed to the EditCell() action.</p>
<dt><i>qparam</i></p>
<dd>The XrmQuark value of the parameter passed to the EditCell() action.</dl>
<p> The EditCell() action takes an arbitrary parameter which it passes through to the callbacks on the <code>XmNtraverseCellCallback</code> list in both String and XrmQuark forms. The EditCell() action recognizes five special parameters which it uses to implement it&#8217;s default cell traversal. These parameters and their corresponding traversal results are: </p>
<dl COMPACT>
<dt><i>Pointer</i></p>
<dd>Set next_row and next_column to the cell underneath the mouse pointer.</p>
<dt><i>Left</i></p>
<dd>If we are currently editing cell (XmNfixedRows, XmNfixedColumns), then do not move. Otherwise move one column to the left, if that column is less than <code>XmNfixedColumns</code> , then move up to the last column of the row above.</p>
<dt><i>Right</i></p>
<dd>If we are currently editing cell (XmNrows &#8211; 1, XmNcolumns &#8211; 1), then do not move. Otherwise move one column to the right, if that column is greater than or equal to <code>XmNcolumns</code> , then move down to column <code>XmNfixedColumns</code> of the row below.</p>
<dt><i>Up</i></p>
<dd>Move up one row. If that row is less than <code>XmNfixedRows</code> , then move to the last row.</p>
<dt><i>Down</i></p>
<dd>Move down one row. If that row is greater than or equal to <code>XmNrows</code> , then move to row <code>XmNfixedRows</code>.</dl>
<p> If the EditCell() action recognizes one of these special parameters, it calculates the new cell to be edited accordingly and stores the results in the next_row and next_column fields of the <code>XbaeMatrixTraverseCellCallbackStruct</code>. If EditCell() does not recognize it&#8217;s parameter, it sets next_row and next_column to the current row and column. It also stores a String and XrmQuark version of it&#8217;s parameter in the param and qparam fields. EditCell() then calls the callbacks on the <code>XmNtraverseCellCallback</code> list. These callbacks can examine the parameter and recalculate the next_row and next_column fields appropriately. The application can override the default calculation for the special parameters, or it can define an entirely new parameter with a corresponding new calculation. It would do this by binding EditCell() with a new application specific parameter to an event in a translation table. It is expected that application callbacks will use the XrmQuark version of the parameter for efficiency reasons (by statically creating the new XrmQuarks and comparing them against the incoming qparam). </p>
<p> When <code>XbaeMatrix</code> receives the focus it will also call the <code>XmNtraverseCellCallback</code> callbacks before returning to the current cell or the upper left most visible cell if no cell is currently edited. The <code>XbaeMatrixTraverseCellCallbackStruct</code> will have param and qparm set to <i>Focus. </i> If there is no current cell row and column will be set to -1. </p>
<p> When XbaeMatrix looses the focus it will also call the <code>XmNtraverseCellCallback</code> with param and qparm set to <i>LoosingFocus.</i></dl>
</dl>
<dl COMPACT>
<dt><code>XmNvalueChangedCallback</code></p>
<dd>Callbacks on the <code>XmNvalueChangedCallback</code> list are called while a cell is being edited. The callbacks are called after text is inserted into or deleted from the TextField edit widget. A pointer to the following structure is passed to each callback on the <code>XmNvalueChangedCallback</code> list: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XbaeReasonType&nbsp;<wbr>&nbsp;<wbr>reason;</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XEvent&nbsp;<wbr>&nbsp;<wbr>*event;</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>row;</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>column;</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixValueChangedCallbackStruct;</code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XbaeValueChangedReason</code>.</p>
<dt><i>event</i></p>
<dd>The event that triggered this callback.</p>
<dt><i>row</i></p>
<dd>The row number of the cell being edited.</p>
<dt><i>column</i></p>
<dd>The column number of the cell being edited.</dl>
</dl>
</dl>
<dl COMPACT>
<dt><code>XmNwriteCellCallback</code></p>
<dd>Callbacks (although it probably only makes sense to have one) on the <code>XmNwriteCellCallback</code> list are called when the widget needs to write data to a cell, but only when <code>XmNdrawCellCallback</code> is defined. A pointer to the following structure is passed to each callback on the <code>XmNwriteCellCallback</code> list: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3><code>typedef struct</code>
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeReasonType</code></td>
<td><i>reason;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XEvent</code></td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>int</code></td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>XbaeCellType</code></td>
<td><i>type;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>String</code></td>
<td><i>string;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Pixmap</code></td>
<td><i>pixmap;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>Pixmap</code></td>
<td><i>mask;</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3><code>} XbaeMatrixWriteCellCallbackStruct;</code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XbaeWriteCellReason</code>.</p>
<dt><i>event</i></p>
<dd>Always set to <font SIZE="-1">NULL</font></p>
<dt><i>row</i></p>
<dd>The row number of the cell that needs to be written.</p>
<dt><i>column</i></p>
<dd>The column number of the cell that needs to be written.</p>
<dt><i>type</i></p>
<dd>The type of &#8220;data&#8221; contained in the cell, either <code>XbaeString</code> or <code>XbaePixmap</code>.</p>
<dt><i>string</i></p>
<dd>The string to store if <i>type</i> is set to <code>XbaeString</code>.</p>
<dt><i>pixmap</i></p>
<dd>The pixmap to store if <i>type</i> is set to <code>XbaePixmap</code>. (maybe a little meaningless unless you can edit a pixmap in a cell)</p>
<dt><i>mask</i></p>
<dd>A mask for the pixmap as obtained from the XPM library. <i>mask</i> is only necessary when <i>pixmap</i> has a depth greater than one.</dl>
<p> If the application adds this callback, when the <code>XbaeMatrix</code> is editable and has been assigned an <code>XmNdrawCellCallback</code>, data on the widget can be edited and stored back in the application&#8217;s data structure. Only if an <code>XmNdrawCellCallback</code> has been assigned to the <code>XbaeMatrix</code> widget, will the <code>XmNwriteCellCallback</code> be called. </p>
<p> At the moment, <i>pixmap</i> and <i>mask</i> will be sent to the <code>XmNwriteCellCallback</code> as <font SIZE="-1">NULL.</font> </p>
</dl>
</dl>
<h2>Translations</h2>
<p><code>XbaeMatrix</code> inherits translations from <code>XmManager</code>. In addition, <code>XbaeMatrix</code> uses the following translation: </p>
<table>
<tr VALIGN=top>
<td>:&lt;Btn1Up&gt;:</td>
<td>DefaultAction()
\
</td>
</tr>
<tr VALIGN=top>
<td>:&lt;Btn1Down&gt;:</td>
<td>DefaultAction() EditCell(Pointer)
\
</td>
</tr>
<tr VALIGN=top>
<td>:Shift&lt;Btn2Down&gt;:</td>
<td>ResizeColumns()
\
</td>
</tr>
<tr VALIGN=top>
<td>:&lt;Btn2Down&gt;:</td>
<td>ProcessDrag()
\
</td>
</tr>
<tr VALIGN=top>
<td>:&lt;Btn1Motion&gt;:</td>
<td>HandleMotion() HandleTracking()()
\
</td>
</tr>
<tr VALIGN=top>
<td>:&lt;Motion&gt;:</td>
<td>HandleTracking()()
\
</td>
</tr>
<tr VALIGN=top>
<td>:&lt;Btn4Down&gt;:</td>
<td>ScrollRows(-50)()
\
</td>
</tr>
<tr VALIGN=top>
<td>:&lt;Btn5Down&gt;:</td>
<td>ScrollRows( 50)()
</td>
</tr>
</table>
<p> <code>XbaeMatrix</code> installs the following default <code>XmNtextTranslations</code> on the <code>TextField</code> edit widget: </p>
<table>
<tr VALIGN=top>
<td>#override
\ </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Shift ~Ctrl ~Meta ~Alt &lt;Key&gt;Tab:</td>
<td>EditCell(Left)
\
</td>
</tr>
<tr VALIGN=top>
<td>~Ctrl ~Meta ~Alt &lt;Key&gt;Tab:</td>
<td>EditCell(Right)
\
</td>
</tr>
<tr VALIGN=top>
<td>&lt;Key&gt;osfUp:</td>
<td>EditCell(Up)
\
</td>
</tr>
<tr VALIGN=top>
<td>&lt;Key&gt;osfDown:</td>
<td>EditCell(Down)
\
</td>
</tr>
<tr VALIGN=top>
<td>&lt;Key&gt;osfActivate:</td>
<td>CommitEdit(False)
\
</td>
</tr>
<tr VALIGN=top>
<td>~Shift ~Meta ~Alt &lt;Key&gt;Return:</td>
<td>CommitEdit(False)
\
</td>
</tr>
<tr VALIGN=top>
<td>&lt;Key&gt;osfCancel:</td>
<td>CommitEdit(False)
\
</td>
</tr>
<tr VALIGN=top>
<td>Shift Ctrl ~Meta ~Alt &lt;Key&gt;Tab:</td>
<td>TraversePrev()
\
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl ~Meta ~Alt &lt;Key&gt;Tab:</td>
<td>TraverseNext()
\
</td>
</tr>
<tr VALIGN=top>
<td>&lt;Key&gt;osfPageDown:</td>
<td>PageDown()
\
</td>
</tr>
<tr VALIGN=top>
<td>&lt;Key&gt;osfPageUp:</td>
<td>PageUp()

</td>
</tr>
</table>
<h2>Action Routines</h2>
<dl COMPACT>
<dt>CancelEdit()</p>
<dd>If the single parameter to CancelEdit() is the String True, then it unmaps the edit TextField, discarding any changes which were made to the cell being edited. If the parameter is False, then CancelEdit() restores the edit TextField to the original contents of the cell, discarding any changes made to the cell being edited. The TextField is not unmapped.</p>
<dt>CommitEdit()</p>
<dd>
<dl COMPACT>
<dd>CommitEdit() first calls any callbacks on the <code>XmNleaveCellCallback</code> list to determine if the changes made to the current cell are valid. If they are, it then saves any changes made to the cell into the cell. If the callbacks on the <code>XmNleaveCellCallback</code> list return that the changes are not valid, CommitEdit() does nothing. </p>
<p> If the changes are valid, CommitEdit() examines it&#8217;s one parameter, which must be the string True or False. If the parameter is True, then the edit TextField is unmapped. If it is False, then the TextField is not unmapped.</dl>
<dt>DefaultAction()</p>
<dd>
<dl COMPACT>
<dd>DefaultAction() sets up a mechanism for determining whether two successive mouse clicks form a double click. The DefaultAction() should normally be used in conjunction with other pointer based events and provides a mechanism for acting on double clicks in a cell.</dl>
<dt>EditCell()</p>
<dd>
<dl COMPACT>
<dd>EditCell() edits a new cell. EditCell() first calculates the new cell to edit based on it&#8217;s single parameter. It then calls the callbacks on the <code>XmNtraverseCellCallback</code> list to allow them to specify a different cell to edit (see the discussion of <code>XmNtraverseCellCallback</code> above). EditCell() then calls the callbacks on the <code>XmNleaveCellCallback</code> list to determine if the changes made to the current cell are valid. If they are, it then saves any changes made to the cell into the cell. If the changes are not valid, EditCell() does nothing further. </p>
<p> If the changes are valid, EditCell() attempts to scroll the new cell to be edited so that it is fully visible. If the new cell is in a fixed row or column, EditCell() returns and does nothing further (these cells are not editable). Otherwise, EditCell() calls the callbacks on the <code>XmNenterCellCallback</code> list to determine if the new cell is editable. It then moves the <code>XmText</code> edit widget to the new cell, setting it&#8217;s editability based on the return from the <code>XmNenterCellCallback</code> callbacks.</dl>
<dt>ProcessDrag()</p>
<dd>
<dl COMPACT>
<dd>ProcessDrag() calls the callbacks on the <code>XmNprocessDragCallback</code> list, passing them a pointer to a <code>XbaeMatrixProcessDragCallbackStruct</code>.</dl>
<dt>ResizeColumns()</p>
<dd>
<dl COMPACT>
<dd>Allows the user to dynamically resize the column widths, provided that <code>XmNallowColumnResize</code> is True.</dl>
<dt>ScrollRows()</p>
<dd>ScrollRows() makes the rows of the matrix scroll by the pixel amount specified by it&#8217;s argument.</p>
<dt>ScrollColumns()</p>
<dd>ScrollColumns() makes the columns of the matrix scroll by the pixel amount specified by it&#8217;s argument.</p>
<dt>SelectCell()</p>
<dd>SelectCell() calls the callbacks on the <code>XmNselectCellCallback</code> list, passing them a pointer to a <code>XbaeMatrixSelectCellCallbackStruct</code>. This structure will contain the String parameters passed to the SelectCell() action, among other things (see the discussion of <code>XmNselectCellCallback</code> above).</p>
<dt>TraverseNext()</p>
<dd>TraverseNext() will traverse out of the Matrix and into the next tab group.</p>
<dt>TraversePrev()</p>
<dd>TraversePrev() will traverse out of the Matrix and into the previous tab group.</p>
<dt>PageDown()</p>
<dd>PageDown() causes the Matrix to scroll down a full page. The text widget is placed on the first non fixed row of the new page.</p>
<dt>PageUp()</p>
<dd>PageUp() causes the Matrix to scroll up a full page. The text widget is placed on the first non fixed row of the new page.</dl>
<h2>Type Converters</h2>
<p>In addition to the standard type converters registered by Xt and Motif, <code>XbaeMatrix</code> registers the following additional type converters:</p>
<dl COMPACT>
<dt>CvtStringToStringArray()</p>
<dd>Converts a comma separated list of Strings to an array of String pointers, one for each substring. Commas in the list may be escaped with the character `\&#8217;. This converter allows the <code>XmNrowLabels</code> and <code>XmNcolumnLabels</code> resources to be specified in resource files.</p>
<dt>CvtStringToWidthArray()</p>
<dd>Converts a comma separated list of numeric Strings to an array of short integers. This converter allows the <code>XmNcolumnWidths</code> resource to be specified in resource files.</p>
<dt>CvtStringToMaxLengthArray()</p>
<dd>Converts a comma separated list of numeric Strings to an array of integers. This converter allows the <code>XmNcolumnMaxLengths</code> resource to be specified in resource files.</p>
<dt>CvtStringToAlignmentArray()</p>
<dd>Converts a comma separated list of alignments to an array of unsigned chars. This converter allows the <code>XmNcolumnLabelAlignments</code> and <code>XmNcolumnAlignments</code> resources to be specified in resource files.</p>
<dt>CvtStringToGridType()</p>
<dd>Converts a single string as discussed in <code>XmNgridType</code> to a grid type value. This converter allows <code>XmNgridType</code> to be specified in resource files.</p>
<dt>CvtStringToMatrixScrollBarDisplayPolicy()</p>
<dd>Converts a single string as discussed in <code>XmNhorizontalScrollBarDisplayPolicy</code> and <code>XmNverticalScrollBarDisplayPolicy</code> to a display policy value. This converter allows <code>XmNhorizontalScrollBarDisplayPolicy</code> and <code>XmNverticalScrollBarDisplayPolicy</code> to be specified in resource files.</p>
<dt>CvtStringToCellTable()</p>
<dd>Converts a comma separated list of Strings with 
 delimited rows to a two dimensional array of String pointers. This converter allows the <code>XmNcells</code> resource to be specified in resource files.</p>
<dt>CvtStringToPixelTable()</p>
<dd>Converts a comma separated list of color names with 
 delimited rows to a two dimensional array of Pixel values. This converter allows the <code>XmNcellBackgrounds</code>and<code>XmNcolors</code> resources to be specified in resource files.</p>
<dt>CvtStringToBooleanArray()</p>
<dd>Converts a comma separated list of string or numeric values to an array of Booleans. The converter recongnises a comma separated list of values. Each value is parsed such that if the first character is This converter allows the <code>XmNcolumnButtonLabels</code> and <code>XmNrowButtonLabels</code> resources to be specified in resource files.</dl>
<h2>Public Functions</h2>
<p>The following external entry points to <code>XbaeMatrix</code> class methods are defined: </p>
<p> <code>XbaeCreateMatrix()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>Widget XbaeCreateMatrix()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>parent;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>String</td>
<td><i>name;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>ArgList</td>
<td><i>arglist;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Cardinal</td>
<td><i>argcount;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (arglist)</dl>
<p> <code>XbaeCreateMatrix()</code> creates an unmanaged instance of an XbaeMatrix widget and returns the associated widget ID.</dl>
<p> <code>XbaeMatrixAddColumns()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixAddColumns()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>position;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>String</td>
<td><i>*columns;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>String</td>
<td><i>*labels;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>short</td>
<td><i>*widths;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*max_lengths;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>unsigned</td>
<td><i>char *alignments;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>unsigned</td>
<td><i>char *label_alignments;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Pixel</td>
<td><i>*colors;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>num_columns;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>position</i></p>
<dd>The column position before which to add the new columns. Must be greater than or equal to zero, and less than or equal to <code>XmNcolumns</code>.</p>
<dt><i>columns</i></p>
<dd>Points to an ordinary two dimensional array of String, or <font SIZE="-1">NULL.</font> These Strings will be used to modify the <code>XmNcells</code> resource to populate the new columns. Each row in the array must have <code>XmNrows</code> elements and represents one of the new columns. columns must have <code>num_columns</code> rows. If columns is <font SIZE="-1">NULL,</font> empty columns will be added.</p>
<dt><i>labels</i></p>
<dd>Points to an array of String, or <font SIZE="-1">NULL.</font> These Strings will be used as the <code>XmNcolumnLabels</code> for the new columns. The labels array must have num_columns elements. If labels is <font SIZE="-1">NULL,</font> and <code>XmNcolumnLabels</code> is set, then blank column labels will be used.</p>
<dt><i>widths</i></p>
<dd>Points to an array of short or <font SIZE="-1">NULL.</font> These values will be used as the <code>XmNcolumnWidths</code> for the new columns. The widths array must have num_columns elements. if widths is NULL then a default width will be used for the new columns.</p>
<dt><i>max_lengths</i></p>
<dd>Points to an array of int, or <font SIZE="-1">NULL.</font> These values will be used as the <code>XmNcolumnMaxLengths</code> for the new columns. The max_lengths array must have num_columns elements. If max_lengths is <font SIZE="-1">NULL,</font> then the corresponding value from widths will be used.</p>
<dt><i>alignments</i></p>
<dd>Points to an array of unsigned char, or <font SIZE="-1">NULL.</font> These values will be used as the <code>XmNcolumnAlignments</code> for the new columns. The alignments array must have num_columns elements. If alignments is <font SIZE="-1">NULL,</font> then <code>XmALIGNMENT_BEGINNING</code> will be used.</p>
<dt><i>label_alignments</i></p>
<dd>Points to an array of unsigned char, or <font SIZE="-1">NULL.</font> These values will be used as the <code>XmNcolumnLabelAlignments</code> for the new column labels. The label_alignments array must have num_columns elements. If label_alignments is <font SIZE="-1">NULL,</font> then <code>XmALIGNMENT_BEGINNING</code> will be used.</p>
<dt><i>colors</i></p>
<dd>Points to an array of Pixel, or <font SIZE="-1">NULL.</font> These values will be used to set the corresponding columns in the <code>XmNcolors</code> table for the new columns. The colors array must have num_columns elements. If colors is <font SIZE="-1">NULL,</font> then <code>XmNforeground</code> will be used.</p>
<dt><i>num_columns</i></p>
<dd>The number of columns which are being added to the widget.</dl>
<p> <code>XbaeMatrixAddColumns()</code> allows the application developer to dynamically add new columns anywhere in the Matrix. The columns will be added before the column specified in position. Columns are numbered starting at zero. To append new columns onto the end of the Matrix, specify position as the total number of columns. Most of the arguments to <code>XbaeMatrixAddColumns()</code> may be specified as <font SIZE="-1">NULL.</font> Default values will be used by the widget. </p>
<p> If the programmer attempts to add columns using <code>XbaeMatrixAddColumns()</code> when there are no rows, it will result in a warning message. There must be at least one row in the <code>XbaeMatrix</code> widget to add columns. </p>
<p> To maintain backward compatability, the cell backgrounds cannot be set in a call to <code>XbaeMatrixAddColumns()</code> and must be set (if so desired) in a separate call to <code>XtVaSetValues()</code>. </p>
</dl>
<p> <code>XbaeMatrixAddRows()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixAddRows()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>position;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>String</td>
<td><i>*rows;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>String</td>
<td><i>*labels;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Pixel</td>
<td><i>*colors;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>num_rows;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>position</i></p>
<dd>The row position before which to add the new rows. Must be greater than or equal to zero, and less than or equal to <code>XmNrows</code>.</p>
<dt><i>rows</i></p>
<dd>Points to an ordinary two dimensional array of String, or <font SIZE="-1">NULL.</font> These Strings will be used to modify the <code>XmNcells</code> resource to populate the new rows. Each row in the array must have <code>XmNcolumns</code> elements and represents one of the new rows. rows must have num_rows rows. If rows is <font SIZE="-1">NULL,</font> empty rows will be added.</p>
<dt><i>labels</i></p>
<dd>Points to an array of String, or <font SIZE="-1">NULL.</font> These Strings will be used as the <code>XmNrowLabels</code> for the new rows. The labels array must have num_rows elements. If labels is <font SIZE="-1">NULL,</font> and <code>XmNrowLabels</code> is set, then blank row labels will be used</p>
<dt><i>colors</i></p>
<dd>Points to an array of Pixel, or <font SIZE="-1">NULL.</font> These values will be used to set the corresponding rows in the <code>XmNcolors</code> table for the new rows. The colors array must have num_rows elements. If colors is <font SIZE="-1">NULL,</font> then <code>XmNforeground</code> will be used.</p>
<dt><i>num_rows</i></p>
<dd>The number of rows which are being added to the widget.</dl>
<p> <code>XbaeMatrixAddRows()</code> allows the application developer to dynamically add new rows anywhere in the Matrix. The rows will be added before the row specified in position. Rows are numbered starting at zero. To append new rows onto the end of the Matrix, specify position as the total number of rows. </p>
<p> To maintain backward compatability, the cell backgrounds cannot be set in a call to <code>XbaeMatrixAddRows()</code> and must be set (if so desired) in a separate call to <code>XtVaSetValues()</code>.</dl>
<p> <code>XbaeMatrixCancelEdit()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixCancelEdit()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Boolean</td>
<td><i>unmap;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>unmap</i></p>
<dd>Specifies whether the TextField cell edit widget should be unmapped after the edit is canceled.</dl>
<p> <code>XbaeMatrixCancelEdit()</code> allows the application developer to programmatically cancel a cell edit in progress, discarding any changes made by the user. This function unmaps the TextField edit widget if the unmap flag is True. If unmap is False, the contents of the TextField are restored to their original value, and the TextField is not unmapped. </p>
</dl>
<p> <code>XbaeMatrixCommitEdit()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>Boolean XbaeMatrixCommitEdit()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Boolean</td>
<td><i>unmap;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An XbaeMatrix widget.</p>
<dt><i>unmap</i></p>
<dd>Specifies whether the TextField cell edit widget should be unmapped after an edit is successfully committed.</dl>
<p> <code>XbaeMatrixCommitEdit()</code> can be used by the application developer to programmatically commit an edit, saving any changes made by the user. This will cause the callbacks on the <code>XmNleaveCellCallback</code> list to be called to verify that the changes the user made are valid. If the changes are valid, then they are saved into the cell and if the unmap flag is True, the TextField widget will be unmapped. </p>
</dl>
<p> <code>XbaeMatrixDeleteColumns()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixDeleteColumns()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>position;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>num_columns;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>position</i></p>
<dd>The column position at which to begin deleting columns. Must be greater than or equal to zero, and (position + num_columns) must be less than or equal to <code>XmNcolumns</code>.</p>
<dt><i>num_columns</i></p>
<dd>The number of columns to delete from the widget.</dl>
<p> <code>XbaeMatrixDeleteColumns()</code> allows the application developer to dynamically delete columns from anywhere in the Matrix. Columns will be deleted starting at the column specified by position. </p>
</dl>
<p> <code>XbaeMatrixDeleteRows()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixDeleteRows()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>position;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>num_rows;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An XbaeMatrix widget.</p>
<dt><i>position</i></p>
<dd>The row position at which to begin deleting rows. Must be greater than or equal to zero, and (position + num_rows) must be less than or equal to <code>XmNrows</code>.</p>
<dt><i>num_rows</i></p>
<dd>The number of rows to delete from the widget.</dl>
<p> <code>XbaeMatrixDeleteRows()</code> allows the application developer to dynamically delete rows from anywhere in the Matrix. Rows will be deleted starting at the row specified by position. </p>
</dl>
<p> <code>XbaeMatrixDeselectAll()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixDeselectAll()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</dl>
<p> <code>XbaeMatrixDeselectAll()</code> allows the application developer to programmatically deselect all cells. <code>XbaeMatrixDeselectAll()</code> redraws the cells in normal video. All Booleans in the <code>XmNselectedCells</code> array will be set to False. </p>
</dl>
<p> <code>XbaeMatrixDeselectCell()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixDeselectCell()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell to deselect.</p>
<dt><i>column</i></p>
<dd>The column of the cell to deselect.</dl>
<p> <code>XbaeMatrixDeselectCell()</code> allows the application developer to programmatically deselect a cell. <code>XbaeMatrixDeselectCell()</code> redraws the cell in normal video. The corresponding Boolean in the <code>XmNselectedCells</code> array will be set to False. </p>
</dl>
<p> <code>XbaeMatrixDeselectColumn()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixDeselectColumn()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column to deselect.</dl>
<p> <code>XbaeMatrixDeselectColumn()</code> allows the application developer to programmatically deselect a column. <code>XbaeMatrixDeselectColumn()</code> draws the column in normal video. The corresponding Booleans in the <code>XmNselectedCells</code> array will be set to False. </p>
</dl>
<p> <code>XbaeMatrixDeselectRow()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixDeselectRow()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row to deselect.</dl>
<p> <code>XbaeMatrixDeselectRow()</code> allows the application developer to programmatically deselect a row. <code>XbaeMatrixDeselectRow()</code> draws the row in reverse video (or selectedForeground / selectedBackground if set). The corresponding Booleans in the <code>XmNselectedCells</code> array will be set to False. </p>
</dl>
<p> <code>XbaeMatrixDisableRedisplay()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixDisableRedisplay()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</dl>
<p> <code>XbaeMatrixDisableRedisplay()</code> and <code>XbaeMatrixEnableRedisplay()</code> allow an application to make multiple changes to a matrix without immediate visual updates. When multiple changes are made with redisplay enabled, visual flashing often occurs. These routines help eliminate this problem. </p>
</dl>
<p> <code>XbaeMatrixEditCell()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixEditCell()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell to be edited.</p>
<dt><i>column</i></p>
<dd>The column of the cell to be edited.</dl>
<p> <code>XbaeMatrixEditCell()</code> </p>
<p> allows the application developer to programmatically force a specific cell to be edited. This function will first attempt to commit the edit in the current cell. If the <code>XmNleaveCellCallback</code> callbacks disallow this commit, then <code>XbaeMatrixEditCell()</code> will return. Otherwise the specified cell is scrolled until it is visible. If the specified cell is in a fixed row or column, it cannot be edited and <code>XbaeMatrixEditCell()</code> will return. Next, the callbacks on the <code>XmNenterCellCallback</code> callback list are called for the specified cell to determine it&#8217;s editability. Then the TextField edit widget is mapped on top of the specified cell. </p>
</dl>
<p> <code>XbaeMatrixEnableRedisplay()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixEnableRedisplay()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Boolean</td>
<td><i>redisplay;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>redisplay</i></p>
<dd>Force the matrix to redisplay if True and no other calls to <code>XbaeMatrixDisableRedisplay()</code> have been made.</dl>
<p> <code>XbaeMatrixDisableRedisplay()</code> and <code>XbaeMatrixEnableRedisplay()</code> allow an application to make multiple changes to a matrix without immediate visual updates. When multiple changes are made with redisplay enabled, visual flashing often occurs. These routines help eliminate this problem. </p>
</dl>
<p> <code>XbaeMatrixEventToXY()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>Boolean XbaeMatrixEventToXY()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>XEvent</td>
<td><i>*event; </i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*x;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*y;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>event</i></p>
<dd>An X event structure pointer, usually from an XEventHandler function.</p>
<dt><i>x</i></p>
<dd>The translated x coordinate.</p>
<dt><i>y</i></p>
<dd>The translated y coordinate.</dl>
<p> <code>XbaeMatrixEventToXY</code> enables the programmer to determine the x and y values of a given event with respect to the <code>XbaeMatrix</code> widget. The returned values are also adjusted to allow for the <code>XbaeClip</code> widget. </p>
</dl>
<p> <code>XbaeMatrixFirstSelectedCell()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixFirstSelectedCell()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The first selected row.</p>
<dt><i>column</i></p>
<dd>The first selected column.</dl>
<p> <code>XbaeMatrixFirstSelectedCell()</code> allows the application developer to find out which cell is the first selected. The function traverses the <code>XbaeMatrix</code> widget in a left to right, top to bottom manner to determine this value. If no cell is selected, row and column are set to -1. </p>
</dl>
<p> <code>XbaeMatrixFirstSelectedColumn()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixFirstSelectedColumn()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</dl>
<p> <code>XbaeMatrixFirstSelectedColumn()</code> returns the column number of the first selected column in the <code>XbaeMatrix</code> widget. The function traverses the matrix from column 0. A column must be entirely selected for the column to be considered selected. If no column is selected then -1 is returned. </p>
</dl>
<p> <code>XbaeMatrixFirstSelectedRow()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixFirstSelectedRow()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</dl>
<p> <code>XbaeMatrixFirstSelectedRow()</code> returns the row number of the first selected row in the <code>XbaeMatrix</code> widget. The function traverses the matrix from row 0. A row must be entirely selected for the row to be considered selected. If no row is selected then -1 is returned. </p>
</dl>
<p> <code>XbaeMatrixGetCell()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>String XbaeMatrixGetCell()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell whose value should be retrieved.</p>
<dt><i>column</i></p>
<dd>The column of the cell whose value should be retrieved.</dl>
<p> <code>XbaeMatrixGetCell()</code> returns the String value stored in the specified cell. This String should not be freed. To examine many cells, it is more efficient to do an XtGetValues() on <code>XmNcells</code> and examine the values in that array. </p>
</dl>
<p> <code>XbaeMatrixGetCellBackground()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>Pixel XbaeMatrixGetCellBackground()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>A <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell whose background color should be retrieved.</p>
<dt><i>column</i></p>
<dd>The column of the cell whose background color should be retrieved. </p>
</dl>
</dl>
<p> <code>XbaeMatrixGetCellColor()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>Pixel XbaeMatrixGetCellColor()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>A <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell whose foreground color should be retrieved.</p>
<dt><i>column</i></p>
<dd>The column of the cell whose foreground color should be retrieved. </p>
</dl>
</dl>
<p> <code>XbaeMatrixGetCellPixmap()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixGetCellPixmap()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Pixmap</td>
<td><i>*pixmap;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Pixmap</td>
<td><i>*mask;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>A <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell whose pixmap and mask should be retrieved.</p>
<dt><i>column</i></p>
<dd>The column of the cell whose pixmap and mask should be retrieved.</p>
<dt><i>pixmap</i></p>
<dd>A pointer to a Pixmap variable, in which the function will store the cell&#8217;s pixmap.</p>
<dt><i>mask</i></p>
<dd>A pointer to a Pixmap variable, in which the function will store the cell&#8217;s pixmap mask. </p>
</dl>
</dl>
<p> <code>XbaeMatrixGetCellTag()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>XmStringTag XbaeMatrixGetCellTag()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>A <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell whose tag should be retrieved.</p>
<dt><i>column</i></p>
<dd>The column of the cell tag should be retrieved.</dl>
<p> <code>XbaeMatrixGetCellTag</code> returns the font tag of the indicated cell. The application should not modify or free the returned value.</dl>
<p> <code>XbaeMatrixGetCellUserData()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>XtPointer XbaeMatrixGetCellUserData()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell whose data should be retrieved.</p>
<dt><i>column</i></p>
<dd>The column of the cell whose data should be retrieved.</dl>
<p> <code>XbaeMatrixGetCellUserData()</code> returns a pointer to the data assigned to the cell in the given coordinates. The data should be set using <code>XbaeMatrixSetCellUserData()</code>. If no data is found to be associated with the particular cell, <font SIZE="-1">NULL</font> is returned. </p>
</dl>
<p> <code>XbaeMatrixGetColumnWidth()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixGetColumnWidth()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column whose width we&#8217;re querying.</dl>
<p> <code>XbaeMatrixGetColumnWidth()</code> is a convenient way to query a column width. </p>
</dl>
<p> <code>XbaeMatrixGetColumnLabel()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>String XbaeMatrixGetColumnLabel()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column of the label that should be retrieved.</dl>
<p> <code>XbaeMatrixGetColumnLabel()</code> returns a pointer to the label of the given column. If no column labels exist or the given column is not a valid column <font SIZE="-1">NULL</font> is returned. If no data is found to be associated with the particular column, <font SIZE="-1">NULL</font> is returned. </p>
</dl>
<p> <code>XbaeMatrixGetColumnUserData()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>XtPointer XbaeMatrixGetColumnUserData()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column of the cell whose data should be retrieved.</dl>
<p> <code>XbaeMatrixGetColumnUserData()</code> returns a pointer to the data assigned to the given column. The data should be set using <code>XbaeMatrixSetColumnUserData()</code>. If no data is found to be associated with the particular column, <font SIZE="-1">NULL</font> is returned. </p>
</dl>
<p> <code>XbaeMatrixGetCurrentCell()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixGetCurrentCell()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell the &#8220;cursor&#8221; or TextField is in.</p>
<dt><i>column</i></p>
<dd>The column of the cell the &#8220;cursor&#8221; or TextField is in.</dl>
<p> <code>XbaeMatrixGetCurrentCell()</code> allows the application developer to determine what cell is being edited or has focus. </p>
</dl>
<p> <code>XbaeMatrixGetEventRowColumn()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixGetEventRowColumn()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>XEvent</td>
<td><i>*event;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>event</i></p>
<dd>An X event structure pointer. This is usually from an XEventHandler function. It can be either a button or a key event.</p>
<dt><i>row</i></p>
<dd>The row of the cell the &#8220;cursor&#8221; or TextField is in.</p>
<dt><i>column</i></p>
<dd>The column of the cell the &#8220;cursor&#8221; or TextField is in.</dl>
<p> <code>XbaeMatrixGetEventRowColumn()</code> allows the application developer to determine what cell corresponds to an (x, y) in an event. If the (x, y) of the event is a legal cell, row and column are set and True is returned. However, if the (x, y) is not over a cell, False is returned, and row and column will have undefined values. </p>
</dl>
<p> <code>XbaeMatrixGetNumSelected()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixGetNumSelected()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</dl>
<p> <code>XbaeMatrixGetNumSelected()</code> returns the number of cells that are currently selected in the given matrix. The widget maintains an internal variable as cells are selected and deselected so a complete traversal of the widget is avoided. </p>
</dl>
<p> <code>XbaeMatrixGetRowHeight()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixGetRowHeight()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row whose height we query.</dl>
<p> <code>XbaeMatrixGetRowHeight()</code> is a convenient way to query a row height. </p>
</dl>
<p> <code>XbaeMatrixGetRowLabel()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>String XbaeMatrixGetRowLabel()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the label that should be retrieved.</dl>
<p> <code>XbaeMatrixGetRowLabel()</code> returns a pointer to the label of the given row. If no row labels exist or the given row is not a valid row <font SIZE="-1">NULL</font> is returned. </p>
</dl>
<p> <code>XbaeMatrixGetRowUserData()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>XtPointer XbaeMatrixGetRowUserData()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell whose data should be retrieved.</dl>
<p> <code>XbaeMatrixGetRowUserData()</code> returns a pointer to the data assigned to the given row. The data should be set using <code>XbaeMatrixSetRowUserData()</code>. If no data is found to be associated with the particular row, <font SIZE="-1">NULL</font> is returned. </p>
</dl>
<p> <code>XbaeMatrixGetXmColumnLabel()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>XmString XbaeMatrixGetXmColumnLabel()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column of the xmLabel that should be retrieved.</dl>
<p> <code>XbaeMatrixGetXmColumnLabel()</code> returns a pointer to the xmLabel of the given column. If no xmColumnLabels exist or the given column is not a valid column <font SIZE="-1">NULL</font> is returned. If no data is found to be associated with the particular column, <font SIZE="-1">NULL</font> is returned. </p>
</dl>
<p> <code>XbaeMatrixGetXmRowLabel()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>XmString XbaeMatrixGetXmRowLabel()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the xmLabel that should be retrieved.</dl>
<p> <code>XbaeMatrixGetXmRowLabel()</code> returns a pointer to the xmLabel of the given row. If no xmRowLabels exist or the given row is not a valid row <font SIZE="-1">NULL</font> is returned. If no data is found to be associated with the particular row, <font SIZE="-1">NULL</font> is returned. </p>
</dl>
<p> <code>XbaeMatrixHighlightCell()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixHighlightCell()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell to highlight.</p>
<dt><i>column</i></p>
<dd>The column of the cell to highlight.</dl>
<p> <code>XbaeMatrixHighlightCell()</code> allows the application developer to programmatically highlight a cell. <code>XbaeMatrixHighlightCell()</code> draws the highlight around the cell. The corresponding unsigned char in the <code>XmNhighlightedCells</code> array will be have its <code>HighlightCell</code> bit set. </p>
</dl>
<p> <code>XbaeMatrixHighlightColumn()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixHighlightColumn()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column to highlight.</dl>
<p> <code>XbaeMatrixHighlightColumn()</code> allows the application developer to programmatically highlight a column. <code>XbaeMatrixHighlightColumn()</code> draws the highlight around the column if <code>XmNgridType</code> is <code>XmGRID_COLUMN_SHADOW</code> or from around each cell in the column otherwise. The corresponding unsigned chars in the <code>XmNhighlightedCells</code> array will be have its <code>HighlightColumn</code> or <code>HighlightOther</code> bit set, depending on whether <code>XmNgridType</code> is set to <code>XmGRID_COLUMN_SHADOW</code> or not. </p>
</dl>
<p> <code>XbaeMatrixHighlightRow()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixHighlightRow()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row to highlight.</dl>
<p> <code>XbaeMatrixHighlightRow()</code> allows the application developer to programmatically highlight a row. <code>XbaeMatrixHighlightRow()</code> draws the highlight around the row if <code>XmNgridType</code> is <code>XmGRID_ROW_SHADOW</code> or from around each cell in the row otherwise. The corresponding unsigned chars in the <code>XmNhighlightedCells</code> array will be have its <code>HighlightRow</code> or <code>HighlightOther</code> bit set, depending on whether <code>XmNgridType</code> is set to <code>XmGRID_ROW_SHADOW</code> or not. </p>
</dl>
<p> <code>XbaeMatrixIsCellSelected()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>Boolean XbaeMatrixIsCellSelected()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell to check.</p>
<dt><i>column</i></p>
<dd>The column of the cell to check.</dl>
<p> <code>XbaeMatrixIsCellSelected()</code> allows the application developer to determine whether or not a particular cell is selected. The function returns True if the cell is selected and False otherwise. </p>
</dl>
<p> <code>XbaeMatrixIsCellVisible()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>Boolean XbaeMatrixIsCellVisible()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell to check.</p>
<dt><i>column</i></p>
<dd>The column of the cell to check.</dl>
<p> <code>XbaeMatrixIsCellVisible()</code> allows the application developer to determine whether or not a particular cell is in the visible area of the <code>XbaeMatrix</code> widget. The function returns True if the cell is visible and False otherwise. </p>
</dl>
<p> <code>XbaeMatrixIsColumnSelected()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>Boolean XbaeMatrixIsColumnSelected()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column of the matrix to check.</dl>
<p> <code>XbaeMatrixIsColumnSelected()</code> allows the application developer to determine whether or not a particular column is selected. The function returns True if the column is selected and False otherwise. A column must be selected in its entirety for <code>XbaeMatrixIsColumnSelected()</code> to return True. </p>
</dl>
<p> <code>XbaeMatrixIsColumnVisible()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>Boolean XbaeMatrixIsColumnVisible()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column of the matrix to check.</dl>
<p> <code>XbaeMatrixIsColumnVisible()</code> allows the application developer to determine whether or not a particular column is in the visible area of the <code>XbaeMatrix</code> widget. The function returns True if the column is visible and False otherwise. </p>
</dl>
<p> <code>XbaeMatrixIsRowSelected()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>Boolean XbaeMatrixIsRowSelected()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the matrix to check.</dl>
<p> <code>XbaeMatrixIsRowSelected()</code> allows the application developer to determine whether or not a particular row is selected. The function returns True if the row is selected and False otherwise. A row must be selected in its entirety for <code>XbaeMatrixIsRowSelected()</code> to return True. </p>
</dl>
<p> <code>XbaeMatrixIsRowVisible()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>Boolean XbaeMatrixIsRowVisible()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the matrix to check.</dl>
<p> <code>XbaeMatrixIsRowVisible()</code> allows the application developer to determine whether or not a particular row is in the visible area of the <code>XbaeMatrix</code> widget. The function returns True if the row is visible and False otherwise. </p>
</dl>
<p> <code>XbaeMatrixMakeCellVisible()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixMakeCellVisible()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row to scroll into the visible area of the matrix.</p>
<dt><i>column</i></p>
<dd>The column to scroll into the visible area of the matrix.</dl>
<p> <code>XbaeMatrixMakeCellVisible()</code> allows a cell to be programatically scrolled into the visible area of the <code>XbaeMatrix</code> widget. By calling this function, the <code>XmNselectScrollVisible</code> resource is ignored. For a more accurate cell location after scrolling, the programmer should use the <code>XmNleftColumn</code>and<code>XmNtopRow</code> resources. </p>
</dl>
<p> <code>XbaeMatrixNumRows()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixNumRows()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</dl>
<p> <code>XbaeMatrixNumRows()</code> returns the number of rows in the given matrix. </p>
</dl>
<p> <code>XbaeMatrixNumColumns()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixNumColumns()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</dl>
<p> <code>XbaeMatrixNumColumns()</code> returns the number of columns in the given matrix. </p>
</dl>
<p> <code>XbaeMatrixNumRows()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixNumRows()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</dl>
<p> <code>XbaeMatrixNumRows()</code> returns the number of rows in the given matrix. </p>
</dl>
<p> <code>XbaeMatrixRefresh()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixRefresh()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</dl>
<p> <code>XbaeMatrixRefresh()</code> allows the application developer to force the widget to redraw itself. This might be used when the programmer knows the widget&#8217;s values have changed, but the widget has not detected the change. For example, the quickest way to swap the values of 2 rows would be to do an XtGetValues on <code>XmNcells</code>, swap the values of the 2 rows, and then do an XtSetValues on <code>XmNcells</code> with the same StringTable variable. Because of the way the Intrinsics work, the widget will not see this change and will display the old values until a redraw is preformed because of a resize or scroll event (assuming no other change in the XtSetValues caused a redraw). Calling <code>XbaeMatrixRefresh()</code> will cause the correct values to be drawn and overcome this limitation in the Intrinsics. While this function should rarely be needed, it is provided &#8220;just in case&#8221;. </p>
</dl>
<p> <code>XbaeMatrixRefreshCell()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixRefreshCell()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell to redraw.</p>
<dt><i>column</i></p>
<dd>The column of the cell to redraw.</dl>
<p> <code>XbaeMatrixRefreshCell()</code> allows the application developer to redraw a specific cell of the matrix. This function is particularly useful when used with the <code>XbaeMatrixDrawCellCallback</code> as it allows updates of the data without an explicit expose event. </p>
</dl>
<p> <code>XbaeMatrixRefreshColumn()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixRefreshColumn()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column of the matrix to redraw.</dl>
<p> <code>XbaeMatrixRefreshColumn()</code> allows the application developer to efficiently redraw a specific column<br />
&nbsp;<wbr>of the matrix. </p>
</dl>
<p> <code>XbaeMatrixRefreshRow()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixRefreshRow()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the matrix to redraw.</dl>
<p> <code>XbaeMatrixRefreshRow()</code> allows the application developer to efficiently redraw a specific row<br />
&nbsp;<wbr>of the matrix. </p>
</dl>
<p> <code>XbaeMatrixRowColToXY()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixRowColToXY()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*x;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*y;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row the of the cell in question.</p>
<dt><i>column</i></p>
<dd>The column the of the cell in question.</p>
<dt><i>x</i></p>
<dd>The x coordinate returned that represents the left coordinates of the given cell.</p>
<dt><i>y</i></p>
<dd>The y coordinate returned that represents the upper coordinates of the given cell.</dl>
<p> <code>XbaeMatrixRowColToXY()</code> allows the application developer to determine the coordinates of the upper left corner of a given cell. If the given widget is not an <code>XbaeMatrix</code> widget, False will be returned and the values of x and y will be undefined. This function is useful for drag and drop calculations. </p>
</dl>
<p> <code>XbaeMatrixSelectAll()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSelectAll()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</dl>
<p> <code>XbaeMatrixSelectAll()</code> allows the application developer to programmatically select all cells. <code>XbaeMatrixSelectAll()</code> redraws the cells in reverse video. All Booleans in the <code>XmNselectedCells</code> array will be set to True. </p>
</dl>
<p> <code>XbaeMatrixSelectCell()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSelectCell()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell to select.</p>
<dt><i>column</i></p>
<dd>The column of the cell to select.</dl>
<p> <code>XbaeMatrixSelectCell()</code> allows the application developer to programmatically select a cell. <code>XbaeMatrixSelectCell()</code> first scrolls the specified cell until it is visible, and then draws the cell in reverse video (or selectedForeground / selectedBackground if set).<br />
&nbsp;<wbr>The corresponding Boolean in the <code>XmNselectedCells</code> array will be set to True. </p>
</dl>
<p> <code>XbaeMatrixSelectColumn()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSelectColumn()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column to select.</dl>
<p> <code>XbaeMatrixSelectColumn()</code> allows the application developer to programmatically select a column. <code>XbaeMatrixSelectColumn()</code> first scrolls the specified column until it is visible, and then draws the column in reverse video (or selectedForeground / selectedBackground if set). The corresponding Booleans in the <code>XmNselectedCells</code> array will be set to True. </p>
</dl>
<p> <code>XbaeMatrixSelectRow()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSelectRow()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row to select.</dl>
<p> <code>XbaeMatrixSelectRow()</code> allows the application developer to programmatically select a row. <code>XbaeMatrixSelectRow()</code> first scrolls the specified row until it is visible, and then draws the row in reverse video (or selectedForeground / selectedBackground if set). The corresponding Booleans in the <code>XmNselectedCells</code> array will be set to True. </p>
</dl>
<p> <code>XbaeMatrixSetCell()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetCell()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>const</td>
<td><i>String value;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell whose value should be set.</p>
<dt><i>column</i></p>
<dd>The column of the cell whose value should be set.</p>
<dt><i>value</i></p>
<dd>The new value to set this cell to.</dl>
<p> <code>XbaeMatrixSetCell()</code> allows the application developer to programmatically set the value of the specified cell. To set the values of many cells, it may be more efficient to do an XtSetValues() on the <code>XmNcells</code> resource. </p>
</dl>
<p> <code>XbaeMatrixSetCellBackground()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetCellBackground()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Pixel</td>
<td><i>color;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell whose backgroundshould be set.</p>
<dt><i>column</i></p>
<dd>The column of the cell whose background should be set.</p>
<dt><i>color</i></p>
<dd>The new color to which to set this cell&#8217;s background.</dl>
<p> <code>XbaeMatrixSetCellBackground()</code> is a convenient way to specify and modify the <code>XmNcellBackgrounds</code> resource when changing the background of a single cell. If <code>XmNcellBackgrounds</code> is <font SIZE="-1">NULL,</font> then <code>XbaeMatrixSetCellBackground()</code> will create a Pixel table initialized to <code>XmNforeground</code> except for the cell specified in it&#8217;s arguments. If <code>XmNcellBackgrounds</code> is not <font SIZE="-1">NULL,</font> then <code>XbaeMatrixSetCellBackground()</code> will changed the specified cell in that resource to the specified color. </p>
</dl>
<p> <code>XbaeMatrixSetCellColor()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetCellColor()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Pixel</td>
<td><i>color;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell whose color should be set.</p>
<dt><i>column</i></p>
<dd>The column of the cell whose color should be set.</p>
<dt><i>color</i></p>
<dd>The new color to which to set this cell.</dl>
<p> <code>XbaeMatrixSetCellColor()</code> is a convenient way to specify and modify the <code>XmNcolors</code> resource when changing the color of a single cell. If <code>XmNcolors</code> is <font SIZE="-1">NULL,</font> then <code>XbaeMatrixSetCellColor()</code> will create a Pixel table initialized to <code>XmNforeground</code> except for the cell specified in it&#8217;s arguments. If <code>XmNcolors</code> is not <font SIZE="-1">NULL,</font> then <code>XbaeMatrixSetCellColor()</code> will changed the specified cell in that resource to the specified color. </p>
</dl>
<p> <code>XbaeMatrixSetCellPixmap()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetCellPixmap()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Pixmap</td>
<td><i>pixmap;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Pixmap</td>
<td><i>mask;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>A <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell whose pixmap and mask should be set.</p>
<dt><i>column</i></p>
<dd>The column of the cell whose pixmap and mask should be set.</p>
<dt><i>pixmap</i></p>
<dd>the function will store the contents of this Pixmap variable</p>
<dt><i>mask</i></p>
<dd>the function will store the contents of this variable as the pixmap mask</dl>
<p> <code>XbaeMatrixSetCellPixmap</code> will set the pixmap and the associated mask of the indicated cell. If the row or column are out of bounds, or the widget is not an <code>XbaeMatrix</code> widget, then nothing is changed; this erroneous condition is silently ignored. </p>
</dl>
<p> <code>XbaeMatrixSetCellShadow()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetCellShadow()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>unsigned char</td>
<td><i>shadow_type;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell whose shadow should be set.</p>
<dt><i>column</i></p>
<dd>The column of the cell whose shadow should be set.</p>
<dt><i>shadow_type</i></p>
<dd>The value to which to set the cells shadow</dl>
<p> <code>XbaeMatrixSetShadow()</code> allows the application developer to programmatically set the shadow of a specified cell. </p>
</dl>
<p> <code>XbaeMatrixSetCellTag()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetCellTag()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>XmStringTag</td>
<td><i>tag;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell whose tag should be set.</p>
<dt><i>column</i></p>
<dd>The column of the cell whose tag should be set.</p>
<dt><i>tag</i></p>
<dd>The value to which to set the cells tag</dl>
<p> <code>XbaeMatrixSetTag()</code> allows the application developer to programmatically set the font tag of a specified cell. This value is copied (quarkified). </p>
</dl>
<p> <code>XbaeMatrixSetCellUserData()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetCellUserData()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>XtPointer</td>
<td><i>data;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell whose value should be set.</p>
<dt><i>column</i></p>
<dd>The column of the cell whose value should be set.</p>
<dt><i>data</i></p>
<dd>A pointer to a user defined data area.</dl>
<p> <code>XbaeMatrixSetCellUserData()</code> allows the application developer to programmatically set the user data of a specified cell. To set the data value of many cells, it may be more efficient to do an XtSetValues() on the <code>XmNcellUserData</code> resource. This resource is copied. </p>
</dl>
<p> <code>XbaeMatrixSetCellWidget()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetCellWidget(w, row, column, widget)
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>widget;</i>
</td>
</tr>
</table>
<p> <code>XbaeMatrixSetCellWidget()</code> is a function to attach a widget to a matrix cell. The cell is selected by specifying its <code>row</code> and <code>column ,</code> <code>widget</code> is the cell widget to be associated with that cell. XbaeMatrix will manage the cell widget&#8217;s position and size so it is displayed inside the cell at all times, including when scrolling. </p>
<p> Using a NULL <code>widget</code> removes the link between a widget and its cell. Only one widget can be in a cell, a widget should also be in only one cell at a time. </p>
</dl>
<p> <code>XbaeMatrixSetCellWidget()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetCellWidget(w, row, column, widget)
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>widget;</i>
</td>
</tr>
</table>
<p> <code>XbaeMatrixSetCellWidget()</code> is a function to attach a widget to a matrix cell. The cell is selected by specifying its <code>row</code> and <code>column ,</code> <code>widget</code> is the cell widget to be associated with that cell. XbaeMatrix will manage the cell widget&#8217;s position and size so it is displayed inside the cell at all times, including when scrolling. </p>
<p> Using a NULL <code>widget</code> removes the link between a widget and its cell. Only one widget can be in a cell, a widget should also be in only one cell at a time. </p>
</dl>
<p> <code>XbaeMatrixSetColumnBackgrounds()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetColumnBackgrounds()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>position;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Pixel</td>
<td><i>*colors;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>num_colors;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>position</i></p>
<dd>The column position at which to begin applying the new backgrounds. Must be greater than or equal to zero, and (position + num_colors) must be less than or equal to <code>XmNcolumns</code>.</p>
<dt><i>colors</i></p>
<dd>Points to an array of Pixel. These specify the backgrounds for the cells in the specified columns. The colors array must have num_colors elements.</p>
<dt><i>num_colors</i></p>
<dd>The number of colors in the colors array.</dl>
<p> <code>XbaeMatrixSetColumnBackgrounds()</code> is a convenient way to specify and modify the <code>XmNcellBackgrounds</code> resource when setting the background of an entire column or columns. If <code>XmNcellBackgrounds</code> is <font SIZE="-1">NULL,</font> then <code>XbaeMatrixSetColumnBackgrounds()</code> will create a Pixel table initialized to <code>XmNforeground</code> except for the columns specified in it&#8217;s arguments. If <code>XmNcellBackgrounds</code> is not <font SIZE="-1">NULL,</font> then <code>XbaeMatrixSetColumnBackgrounds()</code> will changed the specified columns in that resource to the specified colors. </p>
</dl>
<p> <code>XbaeMatrixSetColumnColors()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetColumnColors()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>position;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Pixel</td>
<td><i>*colors;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>num_colors;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>position</i></p>
<dd>The column position at which to begin applying the new colors. Must be greater than or equal to zero, and (position + num_colors) must be less than or equal to <code>XmNcolumns</code>.</p>
<dt><i>colors</i></p>
<dd>Points to an array of Pixel. These specify the colors for the cells in the specified columns. The colors array must have num_colors elements.</p>
<dt><i>num_colors</i></p>
<dd>The number of colors in the colors array.</dl>
<p> <code>XbaeMatrixSetColumnColors()</code> is a convenient way to specify and modify the <code>XmNcolors</code> resource when setting the color of an entire column or columns. If <code>XmNcolors</code> is <font SIZE="-1">NULL,</font> then <code>XbaeMatrixSetColumnColors()</code> will create a Pixel table initialized to <code>XmNforeground</code> except for the columns specified in it&#8217;s arguments. If <code>XmNcolors</code> is not <font SIZE="-1">NULL,</font> then <code>XbaeMatrixSetColumnColors()</code> will changed the specified columns in that resource to the specified colors. </p>
</dl>
<p> <code>XbaeMatrixSetColumnWidth()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetColumnWidth()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>width;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column whose width we&#8217;ll be changing.</p>
<dt><i>width</i></p>
<dd>The new width of this column. A column width can be 0 to hide a column.</dl>
<p> <code>XbaeMatrixSetColumnWidth()</code> is a convenient way to change the width of a column without the need to allocate an array with column width numbers. Passing -1 as the new width will reset the column width to the default value. </p>
</dl>
<p> <code>XbaeMatrixSetColumnLabel()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetColumnLabel()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>String</td>
<td><i>value;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column of the label is to be set.</p>
<dt><i>value</i></p>
<dd>The new value of the label.</dl>
<p> <code>XbaeMatrixSetColumnLabel()</code> allows the application developer to programmatically change the label of a specified column. </p>
</dl>
<p> <code>XbaeMatrixSetColumnShadow()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetColumnShadow()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>unsidned char</td>
<td><i>shadow_type;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column for which the shadow to be set.</p>
<dt><i>shadow_type</i></p>
<dd>The new value of the shadow.</dl>
<p> <code>XbaeMatrixSetColumnShadow()</code> allows the application developer to programmatically change the shadow of a specified column. </p>
</dl>
<p> <code>XbaeMatrixSetColumnUserData()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetColumnUserData()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>XtPointer</td>
<td><i>data;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column whose value should be set.</p>
<dt><i>data</i></p>
<dd>A pointer to a user defined data area.</dl>
<p> <code>XbaeMatrixSetColumnUserData()</code> allows the application developer to programmatically associate user data for the specified column. </p>
</dl>
<p> <code>XbaeMatrixSetRowBackgrounds()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetRowBackgrounds()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>position;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Pixel</td>
<td><i>*colors;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>num_colors;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>position</i></p>
<dd>The row position at which to begin applying the new colors. Must be greater than or equal to zero, and (position + num_colors) must be less than or equal to <code>XmNrows</code>.</p>
<dt><i>colors</i></p>
<dd>Points to an array of Pixel. These specify the backgrounds for the cells in the specified rows. The colors array must have num_colors elements.</p>
<dt><i>num_colors</i></p>
<dd>The number of colors in the colors array.</dl>
<p> <code>XbaeMatrixSetRowBackgrounds()</code> is a convenient way to specify and modify the <code>XmNcellBackgrounds</code> resource when setting the background of an entire row or rows. If <code>XmNcellBackgrounds</code> is <font SIZE="-1">NULL,</font> then <code>XbaeMatrixSetRowBackgrounds()</code> will create a Pixel table initialized to <code>XmNforeground</code> except for the rows specified in it&#8217;s arguments. If <code>XmNcellBackgrounds</code> is not <font SIZE="-1">NULL,</font> then <code>XbaeMatrixSetRowBackgrounds()</code> will changed the specified rows in that resource to the specified colors. </p>
</dl>
<p> <code>XbaeMatrixSetRowColors()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetRowColors()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>position;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Pixel</td>
<td><i>*colors;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>num_colors;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>position</i></p>
<dd>The row position at which to begin applying the new colors. Must be greater than or equal to zero, and (position + num_colors) must be less than or equal to <code>XmNrows</code>.</p>
<dt><i>colors</i></p>
<dd>Points to an array of Pixel. These specify the colors for the cells in the specified rows. The colors array must have num_colors elements.</p>
<dt><i>num_colors</i></p>
<dd>The number of colors in the colors array.</dl>
<p> <code>XbaeMatrixSetRowColors()</code> is a convenient way to specify and modify the <code>XmNcolors</code> resource when setting the color of an entire row or rows. If <code>XmNcolors</code> is <font SIZE="-1">NULL,</font> then <code>XbaeMatrixSetRowColors()</code> will create a Pixel table initialized to <code>XmNforeground</code> except for the rows specified in it&#8217;s arguments. If <code>XmNcolors</code> is not <font SIZE="-1">NULL,</font> then <code>XbaeMatrixSetRowColors()</code> will changed the specified rows in that resource to the specified colors. </p>
</dl>
<p> <code>XbaeMatrixSetRowHeight()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetRowHeight()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>height;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row whose height we&#8217;ll be changing.</p>
<dt><i>height</i></p>
<dd>The new height of this row. A row height can be 0 to hide a row.</dl>
<p> <code>XbaeMatrixSetRowHeight()</code> is a convenient way to change the height of a row without the need to allocate an array with row height numbers. Passing -1 as the new height will reset the row&#8217;s height to the default value. </p>
</dl>
<p> <code>XbaeMatrixSetRowLabel()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetRowLabel()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>String</td>
<td><i>value;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the label is to be set.</p>
<dt><i>value</i></p>
<dd>The new value of the label.</dl>
<p> <code>XbaeMatrixSetRowLabel()</code> allows the application developer to programmatically change the label of the specified row. </p>
</dl>
<p> <code>XbaeMatrixSetRowShadow()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetRowShadow()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>unsigned char</td>
<td><i>shadow_type;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row whose shadow should be set.</p>
<dt><i>shadow_type</i></p>
<dd>The value of the new shadow.</dl>
<p> <code>XbaeMatrixSetRowShadow()</code> allows the application developer to programmatically change the shadow for the specified row. </p>
</dl>
<p> <code>XbaeMatrixSetRowUserData()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetRowUserData()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>XtPointer</td>
<td><i>data;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row whose value should be set.</p>
<dt><i>data</i></p>
<dd>A pointer to a user defined data area.</dl>
<p> <code>XbaeMatrixSetRowUserData()</code> allows the application developer to programmatically associate user data for the specified row. </p>
</dl>
<p> <code>XbaeMatrixSetXmColumnLabel()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetXmColumnLabel()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>XmString</td>
<td><i>value;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column of the xmLabel is to be set.</p>
<dt><i>value</i></p>
<dd>The new value of the xmLabel.</dl>
<p> <code>XbaeMatrixSetXmColumnLabel()</code> allows the application developer to programmatically change the xmLabel of a specified column. </p>
</dl>
<p> <code>XbaeMatrixSetXmRowLabel()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSetXmRowLabel()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>XmString</td>
<td><i>value;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the xmLabel is to be set.</p>
<dt><i>value</i></p>
<dd>The new value of the xmLabel.</dl>
<p> <code>XbaeMatrixSetXmRowLabel()</code> allows the application developer to programmatically change the xmLabel of a specified row. </p>
</dl>
<p> <code>XbaeMatrixSortColumns()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSortColumns()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>(*proc)(Widget, int, int, void *);</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>void</td>
<td><i>*user_data;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>proc</i></p>
<dd>a pointer to a function that can compare columns.</p>
<dt><i>user_data</i></p>
<dd>a pointer the application can use for its own needs.</dl>
<p> <code>XbaeMatrixSortColumns</code> allows you to sort the columns in the <code>XbaeMatrix</code> widget according to criteria determined by the <code>proc</code> function. The <code>proc</code> function should have the above signature and functionality as demanded by the <code><a href="/docs/linux/man/3-qsort/">qsort</a>(3)</code> function. It will be called with a the matrix being sorted, the indices of two columns to compare and the user_data pointer <code>XbaeMatrixSortColumns</code> was called with. It should return -1, 0, or 1 as appropriate. It is guaranteed that the matrix does not change while sorting and the necessary reordering will only take place after the last call to proc has been made. </p>
</dl>
<p> <code>XbaeMatrixSortRows()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixSortRows()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>(*proc)(Widget, int, int, void *);</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>void</td>
<td><i>*user_data;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>proc</i></p>
<dd>a pointer to a function that can compare rows.</p>
<dt><i>user_data</i></p>
<dd>a pointer the application can use for its own needs.</dl>
<p> <code>XbaeMatrixSortRows</code> allows you to sort the rows in the <code>XbaeMatrix</code> widget according to criteria determined by the <code>proc</code> function. The <code>proc</code> function should have the above signature and functionality as demanded by the <code><a href="/docs/linux/man/3-qsort/">qsort</a>(3)</code> function. It will be called with the matrix being sorted, the indices of two rows to compare and the user_data pointer <code>XbaeMatrixSortRows </code> was called with. It should return -1, 0, or 1 as appropriate. It is guaranteed that the matrix does not change while sorting and the necessary reordering will only take place after the last call to proc has been made. </p>
</dl>
<p> <code>XbaeMatrixUnhighlightAll()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixUnhighlightAll()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</dl>
<p> <code>XbaeMatrixUnhighlightAll()</code> allows the application developer to programmatically unhighlight all cells. <code>XbaeMatrixUnhighlightAll()</code> erases the highlight from all cells. All unsigned chars in the <code>XmNhighlightedCells</code> array will be set to <code>HighlightNone</code>. </p>
</dl>
<p> <code>XbaeMatrixUnhighlightCell()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixUnhighlightCell()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row of the cell to unhighlight.</p>
<dt><i>column</i></p>
<dd>The column of the cell to unhighlight.</dl>
<p> <code>XbaeMatrixUnhighlightCell()</code> allows the application developer to programmatically unhighlight a cell. <code>XbaeMatrixUnhighlightCell()</code> erases the highlight from the cell. The corresponding unsigned char in the <code>XmNhighlightedCells</code> array will be have its <code>HighlightCell</code> bit cleared. </p>
</dl>
<p> <code>XbaeMatrixUnhighlightColumn()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixUnhighlightColumn()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>column</i></p>
<dd>The column to unhighlight.</dl>
<p> <code>XbaeMatrixUnhighlightColumn()</code> allows the application developer to programmatically unhighlight a column. <code>XbaeMatrixUnhighlightColumn()</code> erases the highlight from around the column if <code>XmNgridType</code> is <code>XmGRID_COLUMN_SHADOW</code> or from around each cell in the column otherwise. The corresponding unsigned chars in the <code>XmNhighlightedCells</code> array will be have its <code>HighlightColumn</code> or <code>HighlightOther</code> bit cleared, depending on whether <code>XmNgridType</code> is set to <code>XmGRID_COLUMN_SHADOW</code> or not. </p>
</dl>
<p> <code>XbaeMatrixUnhighlightRow()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>void XbaeMatrixUnhighlightRow()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>row;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>row</i></p>
<dd>The row to unhighlight.</dl>
<p> <code>XbaeMatrixUnhighlightRow()</code> allows the application developer to programmatically unhighlight a row. <code>XbaeMatrixUnhighlightRow()</code> erases the highlight from around the row if <code>XmNgridType</code> is <code>XmGRID_ROW_SHADOW</code> or from around each cell in the row otherwise. The corresponding unsigned chars in the <code>XmNhighlightedCells</code> array will be have its <code>HighlightRow</code> or <code>HighlightOther</code> bit cleared, depending on whether <code>XmNgridType</code> is set to <code>XmGRID_ROW_SHADOW</code> or not. </p>
</dl>
<p> <code>XbaeMatrixVisibleCells()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixVisibleCells()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*top_row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*bottom_row;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*left_column;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>int</td>
<td><i>*right_column;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</p>
<dt><i>top_row</i></p>
<dd>The first row that is currently visible in the matrix.</p>
<dt><i>bottom_row</i></p>
<dd>The last row that is currently visible in the matrix.</p>
<dt><i>left_column</i></p>
<dd>The leftmost column that is currently visible in the matrix.</p>
<dt><i>right_column</i></p>
<dd>The rightmost column that is currently visible in the matrix.</dl>
<p> <code>XbaeMatrixVisibleCells()</code> allows the the application developer to obtain the currently visible portion of the <code>XbaeMatrix</code> <i>w</i>. </p>
</dl>
<p> <code>XbaeMatrixVisibleColumns()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixVisibleColumns()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</dl>
<p> <code>XbaeMatrixVisibleColumns()</code> allows the the application developer to programmatically check how many columns are currently displayed in the <code>XbaeMatrix</code> <i>w</i>. A partially visible column will be declared an entire column. </p>
</dl>
<p> <code>XbaeMatrixVisibleRows()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeMatrixVisibleRows()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>w;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>w</i></p>
<dd>An <code>XbaeMatrix</code> widget.</dl>
<p> <code>XbaeMatrixVisibleRows()</code> allows the the application developer to programmatically check how many rows are currently displayed in the <code>XbaeMatrix</code> <i>w</i>. A partially visible row will be declared an entire row. </p>
</dl>
<p> <code>XbaeGetVersionNum()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>int XbaeGetVersionNum()
</td>
</tr>
</table>
<p> <code>XbaeGetVersionNum()</code> is a function that returns the numeric representation of the version of the Xbae library that your program is working with. This is the run-time version of the Xbae widgets, where <code>XbaeVersion</code> is a macro that represents the compile-time version. </p>
<p> The numeric representation is a simple calculation based on the major, minor, and pico numbers representing an Xbae widget release. E.g. version 4.8.1 would be represented as 40801. </p>
<p> Releases prior to 4.8.0 didn&#8217;t have this functionality. </p>
</dl>
<p> <code>XbaeGetVersionText()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>char * XbaeGetVersionText()
</td>
</tr>
</table>
<p> <code>XbaeGetVersionText()</code> is a function that returns the textual representation of the version of the Xbae library that your program is working with. This is the run-time version of the Xbae widgets, where <code>XbaeVersionTxt</code> is a macro that represents the compile-time version. </p>
</dl>
<h2>Additional Behavior</h2>
<p>Using XtSetValues to set the Matrix&#8217;s <code>XmNwidth</code> resource to 0 will cause it to recompute it&#8217;s horizontal size. It will request a new size which results in <code>XmNvisibleColumns</code> columns being displayed. If <code>XmNvisibleColumns</code> is 0, then it will request a new size such that it does not need a horizontal ScrollBar (full horizontal size). </p>
<p> Using XtSetValues to set the Matrix&#8217;s <code>XmNheight</code> resource to 0 will cause it to recompute it&#8217;s vertical size. It will request a new size which results in <code>XmNvisibleRows</code> rows being displayed. If <code>XmNvisibleRows</code> is 0, then it will request a new size such that it does not need a vertical ScrollBar (full vertical size). </p>
<p> An XtSetValues on <code>XmNvisibleRows</code> will cause the Matrix to request a new size which results in <code>XmNvisibleRows</code> non-fixed rows being displayed, only if the new value is different than the old one. </p>
<p> An XtSetValues on <code>XmNvisibleColumns</code> will cause the Matrix to request a new size which results in the first <code>XmNvisibleColumns</code> non-fixed columns being displayed, only if the new value is different than the old one. </p>
<p> An XtSetValues on any other resource will not result in a request for a new size. Setting other resources in conjunction with setting <code>XmNwidth</code> and/or <code>XmNheight</code> to 0 allows for more control of the Matrix&#8217;s geometry. </p>
<p> An XtSetValues setting <code>XmNrowLabelWidth</code> to 0 will cause <code>XmNrowLabelWidth</code> to be set to the width of the longest row label. </p>
<h2>Virtual Bindings</h2>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="//www.systutorials.com/docs/linux/man/3X-VirtualBindings/">VirtualBindings</a>(3X)</code>.</p>
<h2>Author</h2>
<p><code>Andrew Wason</code> (aw [at] bae.bellcore.com) of Bellcore, Piscataway NJ, wrote the original version of the Xbae widgets. His final release of the widgets was version 3.8. </p>
<p> <code>Kevin Brannen</code> (kbrannen [at] metronet.com) took over maintainership following Andrew Wason&#8217;s departure and released version 4.0. </p>
<p> <code>Andrew Lister</code> (lister [at] db.com) maintained from 1995 to 1999.</p>
<h2>Special Thanks</h2>
<p>Andrew Wason for the original idea and source code.<br />
 Jay Schmidgall for his contributions.<br />
 Nick Banyard for providing the multibyte extensions.<br />
 Callum Gibson for the pattern parsing in the XbaeInput widget.<br />
 Sascha Goebel for debugging the scroll-per-pixel code.<br />
 Tobias Oed for lots of code cleanup and debugging.<br />
 The people from Arcad Systemhaus for code submission for XbaeMatrixSort and a couple of related functionalities, and easier pixmap support.</p>
<h2>Release</h2>
<p>This document describes XbaeMatrix, version 4.60.4.</p>
<h2>See Also</h2>
<p><code><a href="//www.systutorials.com/docs/linux/man/3X-Core/">Core</a>(3X), <a href="//www.systutorials.com/docs/linux/man/3X-Composite/">Composite</a>(3X), <a href="//www.systutorials.com/docs/linux/man/3X-XmManager/">XmManager</a>(3X), <a href="//www.systutorials.com/docs/linux/man/3X-XmScrollBar/">XmScrollBar</a>(3X), <a href="//www.systutorials.com/docs/linux/man/3X-XbaeInput/">XbaeInput</a>(3X),</code> <a href="//www.systutorials.com/docs/linux/man/3X-XmText/">XmText</a>(3X)</p>
<h2>Notice of Limitation</h2>
<p>Bellcore, previous and current maintainers of the Xbae widgets (collectively &#8216;authors&#8217;) provide this information solely to professionals who have the appropriate degree of experience to understand and interpret its contents in accordance with generally accepted engineering or other professional standards and applicable regulations. No recommendations as to products or vendors is made or should be implied. </p>
<p> While the information contained herein has been prepared from sources deemed to be reliable, the authors reserve the right to revise the information without notice, but has no obligation to do so. Unless the recipient has been expressly granted a license by Bellcore under separate applicable written agreement with Bellcore, no license, expressed or implied, is granted under any patents, copyrights or other intellectual property rights. Use of the information is at your discretion and shall not be deemed an inducement by Bellcore to infringe any existing or later-issued patent, copyrights or other intellectual property right. </p>
<p> THE AUTHORS MAKE NO REPRESENTATIONS AND EXTENDS NO WARRANTIES, EXPRESS OR IMPLIED, WITH RESPECT TO THE INFORMATION, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR ANY PARTICULAR PURPOSE, AND THE WARRANTY AGAINST INFRINGEMENT OF PATENTS OR OTHER INTELLECTUAL PROPERTY RIGHTS. THE INFORMATION IS PROVIDED &#8220;AS IS&#8221;, AND IN NO EVENT SHALL THE AUTHORS OR ANY OF ITS AFFILIATES BE LIABLE FOR ANY DAMAGES, INCLUDING ANY LOST PROFITS OR OTHER INCIDENTAL OR CONSEQUENTIAL DAMAGES RELATING TO THE INFORMATION. </p>
<p> Copyright 1991, 1992 Bellcore.<br />
 Copyright 1995-99 Andrew Lister All Rights Reserved.<br />
 Copyright 1999-2002 LessTif Developers </p>
<p> The above no warranty extends to all additions and contributions. No contributor shall be held liable; this work is provided &#8220;as is&#8221;. If this is a problem for you, then don&#8217;t use this software.</p>
