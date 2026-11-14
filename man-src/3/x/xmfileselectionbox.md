---
title: "xmfileselectionbox(3)"
name: "xmfileselectionbox"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfileselectionbox/"
description: "XmFileSelectionBox — The FileSelectionBox widget class"
---

<p><code>XmFileSelectionBox</code> &#8212; The FileSelectionBox widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/FileSB.h&gt;</pre>
<h2>Description</h2>
<p>FileSelectionBox traverses through directories, views the files and subdirectories in them, and then selects files. </p>
<p> A FileSelectionBox has five main areas:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>A text input field for displaying and editing a directory mask used to select the files to be displayed</p>
<dt> &bull;</p>
<dd>An optional text input field for displaying and editing a filter mask used to select the files to be displayed.</p>
<dt> &bull;</p>
<dd>A scrollable list of filenames</p>
<dt> &bull;</p>
<dd>A scrollable list of subdirectories</p>
<dt> &bull;</p>
<dd>A text input field for displaying and editing a filename</p>
<dt> &bull;</p>
<dd>A group of PushButtons, labeled <code>OK</code>, <code>Filter</code>, <code>Cancel</code>, and <code>Help</code>. The layout direction of the buttons depends on the <code>XmNlayoutDirection</code> resource.</dl>
<p> ####Additional children may be added to the FileSelectionBox after creation. FileSelectionBox inherits the layout functionality provided by SelectionBox for any additional children. To remove the list of filenames, the list of subdirectories, or both from the FileSelectionBox after creation, unmanage the appropriate widgets and their labels. The list and label widgets are obtained through a call to the <code>XmFileSelectionBoxGetChild</code> function. To remove either the directory list or the file list, unmanage the parent of the appropriate list widget and unmanage the corresponding label. </p>
<p> The user can specify resources in a resource file for the automatically created widgets and gadgets of FileSelectionBox. The following list identifies the names of these widgets (or gadgets) and the associated FileSelectionBox areas:</p>
<dl COMPACT>
<dt>FilterLabel</p>
<dd><code>FilterText</code></p>
<dt>Filter Text</p>
<dd><code>TextField</code></p>
<dt>Directory List</p>
<dd><code>DirList</code></p>
<dt>Directory List Label</p>
<dd><code>Dir</code></p>
<dt>DirL</p>
<dd><code>Label</code></p>
<dt>DirText</p>
<dd><code>TextField</code></dl>
<p> The directory mask is a string specifying the base directory to be examined and a search pattern. Ordinarily, the directory list displays the subdirectories of the base directory, as well as the base directory itself and its parent directory. The file list ordinarily displays all files and/or subdirectories in the base directory that match the search pattern. </p>
<p> Optionally, the search pattern mask and the base directory can be displayed in two separate text fields. This option is controlled by the <code>XmNpathMode</code> resource. Using this alternate display does not change the meaning of resources that control the content of these fields: <code>XmNdirectory</code>, <code>XmNdirMask</code>, <code>XmNpattern</code>. </p>
<p> A procedure specified by the <code>XmNqualifySearchDataProc</code> resource extracts the base directory and search pattern from the directory mask. If the directory specification is empty, the current working directory is used. If the search pattern is empty, a pattern that matches all files is used. </p>
<p> An application can supply its own <code>XmNqualifySearchDataProc</code> as well as its own procedures to search for subdirectories and files. The default <code>XmNqualifySearchDataProc</code> works as follows: The directory mask is a pathname that can contain zero or more <i>wildcard</i> characters in its directory portion, its file portion, or both. The directory components of the directory mask &#8212; up to, but not including, the first component with a wildcard character &#8212; specify the directory to be searched, relative to the current working directory. The remaining components specify the search pattern. If the directory mask is empty or if its first component contains a wildcard character, the current working directory is searched. If no component of the directory mask contains a wildcard character, the entire directory mask is the directory specification, and all files in that directory are matched. </p>
<p> The user can select a new directory to examine by scrolling through the list of directories and selecting the desired directory or by editing the directory mask. Selecting a new directory from the directory list does not change the search pattern. A user can select a new search pattern by editing the directory mask or, when the FileSelectionBox has the optional <code>XmNpathMode XmPATH_MODE_RELATIVE</code> display, the filter text field. Double clicking or pressing <code>KActivate</code> on a directory in the directory list initiates a search for files and subdirectories in the new directory, using the current search pattern. </p>
<p> The user can select a file by scrolling through the list of filenames and selecting the desired file or by entering the filename directly into the text edit area. Selecting a file from the list causes that filename to appear in the file selection text edit area. </p>
<p> The user may select a new file as many times as desired. The application is not notified until the user takes one of the following actions:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>Selects the <code>OK</code> PushButton</p>
<dt> &bull;</p>
<dd>Presses <code>KActivate</code> while the selection text edit area has the keyboard focus</p>
<dt> &bull;</p>
<dd>Double clicks or presses <code>KActivate</code> on an item in the file list</dl>
<p> FileSelectionBox initiates a directory and file search when any of the following occurs:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>The FileSelectionBox is initialized</p>
<dt> &bull;</p>
<dd>The function <code>XtSetValues</code> is used to change <code>XmNdirMask</code>, <code>XmNdirectory</code>, <code>XmNpattern</code>, or <code>XmNfileTypeMask</code></p>
<dt> &bull;</p>
<dd>The user activates the <code>Filter</code> PushButton</p>
<dt> &bull;</p>
<dd>The user double clicks or presses <code>KActivate</code> on an item in the directory list</p>
<dt> &bull;</p>
<dd>The application calls <code>XmFileSelectionDoSearch</code></p>
<dt> &bull;</p>
<dd>The user presses <code>KActivate</code> while the directory mask text edit area has the keyboard focus</dl>
<p> When a file search is initiated, the FileSelectionBox takes the following actions:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>Constructs an <code>XmFileSelectionBoxCallbackStruct</code> structure with values appropriate for the action that initiated the search</p>
<dt> &bull;</p>
<dd>Calls the <code>XmNqualifySearchDataProc</code> with the callback structure as the data input argument</p>
<dt> &bull;</p>
<dd>Sets <code>XmNdirectoryValid</code> and <code>XmNlistUpdated</code> to False</p>
<dt> &bull;</p>
<dd>Calls the <code>XmNdirSearchProc</code> with the qualified data returned by the <code>XmNqualifySearchDataProc</code></dl>
<p> If <code>XmNdirectoryValid</code> is True, the FileSelectionBox takes the following additional actions:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>Sets <code>XmNlistUpdated</code> to False</p>
<dt> &bull;</p>
<dd>Calls the <code>XmNfileSearchProc</code> with the qualified data returned by the <code>XmNqualifySearchDataProc</code> (and possibly modified by the <code>XmNdirSearchProc</code>)</p>
<dt> &bull;</p>
<dd>If <code>XmNlistUpdated</code> is True and the file list is empty, displays the <code>XmNnoMatchString</code> in the file list and clears the selection text and <code>XmNdirSpec</code></p>
<dt> &bull;</p>
<dd>If <code>XmNlistUpdated</code> is True and the file list is not empty, sets the selection text and <code>XmNdirSpec</code> to the qualified <i>dir</i> returned by the <code>XmNqualifySearchDataProc</code> (and possibly modified by the <code>XmNdirSearchProc</code>)</p>
<dt> &bull;</p>
<dd>Sets the directory mask text and <code>XmNdirMask</code> to the qualified <i>mask</i> returned by the <code>XmNqualifySearchDataProc</code> (and possibly modified by the <code>XmNdirSearchProc</code>)</p>
<dt> &bull;</p>
<dd>Sets <code>XmNdirectory</code> to the qualified <i>dir</i> returned by the <code>XmNqualifySearchDataProc</code> (and possibly modified by the <code>XmNdirSearchProc</code>)</p>
<dt> &bull;</p>
<dd>Sets <code>XmNpattern</code> to the qualified <i>pattern</i> returned by the <code>XmNqualifySearchDataProc</code> (and possibly modified by the <code>XmNdirSearchProc</code>)</dl>
<p> FileSelectionBox uses the <code>XmQTactivatable</code> trait.</p>
<h3>Data Transfer Behavior</h3>
<p>Child widgets of a FileSelectionBox support the data transfer operations and targets associated with their widget classes. </p>
<p> In addition, if the source of a data transfer is the directory list and if <code>XmNdirSearchProc</code> has its default value, the directory list supports the <code>FILE</code> and <code>FILE_NAME</code> targets. </p>
<p> If the source of a data transfer is the file list and if <code>XmNfileSearchProc</code> has its default value, the file list supports the <code>FILE</code> and <code>FILE_NAME</code> targets. </p>
<p> In either case, FileSelectionBox adds an <code>XmNconvertCallback</code> procedure to the appropriate list. This procedure adds <code>FILE</code> and <code>FILE_NAME</code> to the <code>TARGETS</code> returned by the list. It treats requests for conversion of a selection to <code>FILE</code> and <code>FILE_NAME</code> exactly like requests for conversion to <code>TEXT</code>. </p>
<p> If an application changes <code>XmNdirSearchProc</code> or <code>XmNfileSearchProc</code> and wants to support the <code>FILE</code> and <code>FILE_NAME</code> targets on the corresponding list, it must provide support itself by adding a procedure to the list&#8217;s <code>XmNconvertCallback</code> list.</p>
<h3>Descendants</h3>
<p>FileSelectionBox automatically creates the descendants shown in the following table. An application can use <code>XtNameToWidget</code> to gain access to the named descendant. In addition, a user or an application can use the named descendant when specifying resource values. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Named Descendant</code></td>
<td><code>Class</code></td>
<td><code>Identity</code>
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
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
<hr>
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
</tr>
<tr VALIGN=top>
<td><code>Apply</code></td>
<td><code>XmPushButtonGadget</code></td>
<td>Apply button
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
</tr>
<tr VALIGN=top>
<td><code>Cancel</code></td>
<td><code>XmPushButtonGadget</code></td>
<td>Cancel button
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
</tr>
<tr VALIGN=top>
<td><code>Dir</code></td>
<td><code>XmLabelGadget</code></td>
<td>title above list of directories
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
</tr>
<tr VALIGN=top>
<td><code>DirList</code></td>
<td><code>XmList</code></td>
<td>list of directories
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
</tr>
<tr VALIGN=top>
<td><code>DirListSW</code></td>
<td><code>XmScrolledWindow</code></td>
<td>ScrolledWindow parent of <code>DirList</code>
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
</tr>
<tr VALIGN=top>
<td><code>FilterLabel</code></td>
<td><code>XmLabelGadget</code></td>
<td>title above filter box
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
</tr>
<tr VALIGN=top>
<td><code>FilterText</code></td>
<td><code>XmText</code> or <code>XmTextField</code></td>
<td>text within filter box
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
</tr>
<tr VALIGN=top>
<td><code>Help</code></td>
<td><code>XmPushButtonGadget</code></td>
<td>Help button
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
</tr>
<tr VALIGN=top>
<td><code>Items</code></td>
<td><code>XmLabelGadget</code></td>
<td>title above list of filenames
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
</tr>
<tr VALIGN=top>
<td><code>ItemsList</code></td>
<td><code>XmList</code></td>
<td>list of filenames
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
</tr>
<tr VALIGN=top>
<td><code>ItemsListSW</code></td>
<td><code>XmScrolledWindow</code></td>
<td>ScrolledWindow parent of <code>ItemsList</code>
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
</tr>
<tr VALIGN=top>
<td><code>OK</code></td>
<td><code>XmPushButtonGadget</code></td>
<td>OK button
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
</tr>
<tr VALIGN=top>
<td><code>Selection</code></td>
<td><code>XmLabelGadget</code></td>
<td>title above selection box
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
</tr>
<tr VALIGN=top>
<td><code>Separator</code></td>
<td><code>XmSeparatorGadget</code></td>
<td>optional dividing line
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
</tr>
<tr VALIGN=top>
<td><code>Text</code></td>
<td><code>XmText</code> or <code>XmTextField</code></td>
<td>text within selection box
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
</tr>
</table>
</table>
<h3>Classes</h3>
<p>FileSelectionBox inherits behavior, resources, and traits from <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, <code>XmManager</code>, <code>XmBulletinBoard</code>, and <code>XmSelectionBox</code>. </p>
<p> The class pointer is <code>xmFileSelectionBoxWidgetClass</code>. </p>
<p> The class name is <code>XmFileSelectionBox</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmFileSelectionBox Resource Set</code>
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
<td>XmNdirectory</td>
<td>XmCDirectory</td>
<td>XmString</td>
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
<td>XmNdirectoryValid</td>
<td>XmCDirectoryValid</td>
<td>Boolean</td>
<td>dynamic</td>
<td>SG
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
<td>XmNdirListItems</td>
<td>XmCDirListItems</td>
<td>XmStringTable</td>
<td>dynamic</td>
<td>SG
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
<td>XmNdirListItemCount</td>
<td>XmCDirListItemCount</td>
<td>int</td>
<td>dynamic</td>
<td>SG
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
<td>XmNdirListLabelString</td>
<td>XmCDirListLabelString</td>
<td>XmString</td>
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
<td>XmNdirMask</td>
<td>XmCDirMask</td>
<td>XmString</td>
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
<td>XmNdirSearchProc</td>
<td>XmCDirSearchProc</td>
<td>XmSearchProc</td>
<td>default procedure</td>
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
<td>XmNdirSpec</td>
<td>XmCDirSpec</td>
<td>XmString</td>
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
<td>XmNdirTextLabelString</td>
<td>XmCDirTextLabelString</td>
<td>XmString</td>
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
<td>XmNfileFilterStyle</td>
<td>XmCFileFilterStyle</td>
<td>XtEnum</td>
<td>XmFILTER_NONE</td>
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
<td>XmNfileListItems</td>
<td>XmCItems</td>
<td>XmStringTable</td>
<td>dynamic</td>
<td>SG
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
<td>XmNfileListItemCount</td>
<td>XmCItemCount</td>
<td>int</td>
<td>dynamic</td>
<td>SG
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
<td>XmNfileListLabelString</td>
<td>XmCFileListLabelString</td>
<td>XmString</td>
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
<td>XmNfileSearchProc</td>
<td>XmCFileSearchProc</td>
<td>XmSearchProc</td>
<td>default procedure</td>
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
<td>XmNfileTypeMask</td>
<td>XmCFileTypeMask</td>
<td>unsigned char</td>
<td>XmFILE_REGULAR</td>
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
<td>XmNfilterLabelString</td>
<td>XmCFilterLabelString</td>
<td>XmString</td>
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
<td>XmNlistUpdated</td>
<td>XmCListUpdated</td>
<td>Boolean</td>
<td>dynamic</td>
<td>SG
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
<td>XmNnoMatchString</td>
<td>XmCNoMatchString</td>
<td>XmString</td>
<td> &quot;&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>]&nbsp;<wbr>&quot; </td>
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
<td>XmNpathMode</td>
<td>XmCPathMode</td>
<td>XtEnum</td>
<td>XmPATH_MODE_FULL</td>
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
<td>XmNpattern</td>
<td>XmCPattern</td>
<td>XmString</td>
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
<td>XmNqualifySearchDataProc</td>
<td>XmCQualifySearchDataProc</td>
<td>XmQualifyProc</td>
<td>default procedure</td>
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
<dt><code>XmNdirectory</code></p>
<dd>Specifies the base directory used in combination with <code>XmNpattern</code> in determining the files and directories to be displayed. The default value is determined by the <code>XmNqualifySearchDataProc</code> and depends on the initial values of <code>XmNdirMask</code>, <code>XmNdirectory</code>, and <code>XmNpattern</code>. If the default is NULL or empty, the current working directory is used.</p>
<dt><code>XmNdirectoryValid</code></p>
<dd>Specifies an attribute that is set only by the directory search procedure. The value is set to True if the directory passed to the directory search procedure can actually be searched. If this value is False the file search procedure is not called, and <code>XmNdirMask</code>, <code>XmNdirectory</code>, and <code>XmNpattern</code> are not changed.</p>
<dt><code>XmNdirListItems</code></p>
<dd>Specifies the items in the directory list. <code>XtGetValues</code> for this resource returns the list items themselves, not a copy of the list items. The application must not free the returned items.</p>
<dt><code>XmNdirListItemCount</code></p>
<dd>Specifies the number of items in the directory list. The value must not be negative.</p>
<dt><code>XmNdirListLabelString</code></p>
<dd>Specifies the label string of the directory list. The default for this resource depends on the locale. In the C locale the default is <code>Directories</code>.</p>
<dd>Now that some default localized label strings are provided through message catalogs for the children of composite widgets, the <code>labelString</code> resources cannot be set on the child through default resource files. Instead, the resource provided at the parent level must be used.</p>
<dt><code>XmNdirMask</code></p>
<dd>Specifies the directory mask used in determining the files and directories to be displayed. The default value is determined by the <code>XmNqualifySearchDataProc</code> and depends on the initial values of <code>XmNdirMask</code>, <code>XmNdirectory</code>, and <code>XmNpattern</code>.</p>
<dt><code>XmNdirSearchProc</code></p>
<dd>Specifies a directory search procedure to replace the default directory search procedure. FileSelectionBox&#8217;s default directory search procedure fulfills the needs of most applications. Because it is impossible to cover the requirements of all applications, you can replace the default search procedure.</p>
<dd>The directory search procedure is called with two arguments: the FileSelectionBox widget and a pointer to an <code>XmFileSelectionBoxCallbackStruct</code> structure. The callback structure is generated by the <code>XmNqualifySearchDataProc</code> and contains all information required to conduct a directory search, including the directory mask and a qualified base directory and search pattern. Once called, it is up to the search routine to generate a new list of directories and update the FileSelectionBox widget by using <code>XtSetValues</code>.</p>
<dd>The search procedure must set <code>XmNdirectoryValid</code> and <code>XmNlistUpdated</code>. If it generates a new list of directories, it must also set <code>XmNdirListItems</code> and <code>XmNdirListItemCount</code>.</p>
<dd>If the search procedure cannot search the specified directory, it must warn the user and set <code>XmNdirectoryValid</code> and <code>XmNlistUpdated</code> to False, unless it prompts and subsequently obtains a valid directory. If the directory is valid but is the same as the current <code>XmNdirectory</code>, the search procedure must set <code>XmNdirectoryValid</code> to True, but it may elect not to generate a new list of directories. In this case, it must set <code>XmNlistUpdated</code> to False.</p>
<dd>If the search procedure generates a new list of directories, it must set <code>XmNdirListItems</code> to the new list of directories and <code>XmNdirListItemCount</code> to the number of items in the list. If there are no directories, it sets <code>XmNdirListItems</code> to NULL and <code>XmNdirListItemCount</code> to 0 (zero). In either case, it must set <code>XmNdirectoryValid</code> and <code>XmNlistUpdated</code> to True.</p>
<dd>The search procedure ordinarily should not change the callback structure. But if the original directory is not valid, the search procedure may obtain a new directory from the user. In this case, it should set the <i>dir</i> member of the callback structure to the new directory, call the <code>XmNqualifySearchDataProc</code> with the callback struct as the input argument, and copy the qualified data returned by the <code>XmNqualifySearchDataProc</code> into the callback struct.</p>
<dt><code>XmNdirSpec</code></p>
<dd>Specifies the full file path specification. This is the <code>XmNtextString</code> resource in SelectionBox, renamed for FileSelectionBox. The default value is determined by the FileSelectionBox after conducting the initial directory and file search.</p>
<dt><code>XmNdirTextLabelString</code></p>
<dd>Uses the specified <code>XmString</code> as the label above the TextField directory. The resource takes effect when the <code>XmNpathMode</code> resource has a value of <code>XmPATH_MODE_RELATIVE</code>. It is ignored when the <code>XmNpathMode</code> resource has a value of <code>XmPATH_MODE_FULL</code>.</p>
<dd>Now that some default localized label strings are provided through message catalogs for the children of composite widgets, the <code>labelString</code> resources cannot be set on the child through default resource files. Instead, the resource provided at the parent level must be used.</p>
<dt><code>XmNfileFilterStyle</code></p>
<dd>Specifies whether or not the &quot;hidden&quot; files (those whose names begin with . (period) in POSIX systems) will be listed in the file and directory scrolling lists (where the default directory search procedure is used). The possible values are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmFILTER_NONE</code></p>
<dd>Does not filter hidden files.</p>
<dt><code>XmFILTER_HIDDEN_FILES</code></p>
<dd>Restricts the list of possible file names, such as those beginning with . (period).</dl>
</dl>
<dt><code>XmNfileListItems</code></p>
<dd>Specifies the items in the file list. This is the <code>XmNlistItems</code> resource in SelectionBox, renamed for FileSelectionBox. <code>XtGetValues</code> for this resource returns the list items themselves, not a copy of the list items. The application must not free the returned items.</p>
<dt><code>XmNfileListItemCount</code></p>
<dd>Specifies the number of items in the file list. This is the <code>XmNlistItemCount</code> resource in SelectionBox, renamed for FileSelectionBox. The value must not be negative.</p>
<dt><code>XmNfileListLabelString</code></p>
<dd>Specifies the label string of the file list. This is the <code>XmNlistLabelString</code> resource in SelectionBox, renamed for FileSelectionBox. The default for this resource depends on the locale. In the C locale the default is <code>Files</code>.</p>
<dd>Now that some default localized label strings are provided through message catalogs for the children of composite widgets, the <code>labelString</code> resources cannot be set on the child through default resource files. Instead, the resource provided at the parent level must be used.</p>
<dt><code>XmNfileSearchProc</code></p>
<dd>Specifies a file search procedure to replace the default file search procedure. FileSelectionBox&#8217;s default file search procedure fulfills the needs of most applications. Because it is impossible to cover the requirements of all applications, you can replace the default search procedure.</p>
<dd>The file search procedure is called with two arguments: the FileSelectionBox widget and a pointer to an <code>XmFileSelectionBoxCallbackStruct</code> structure. The callback structure is generated by the <code>XmNqualifySearchDataProc</code> (and possibly modified by the <code>XmNdirSearchProc</code>). It contains all information required to conduct a file search, including the directory mask and a qualified base directory and search pattern. Once this procedure is called, it is up to the search routine to generate a new list of files and update the FileSelectionBox widget by using <code>XtSetValues</code>.</p>
<dd>The search procedure must set <code>XmNlistUpdated</code>. If it generates a new list of files, it must also set <code>XmNfileListItems</code> and <code>XmNfileListItemCount</code>.</p>
<dd>It is recommended that the search procedure always generate a new list of files. If the <i>mask</i> member of the callback structure is the same as the <i>mask</i> member of the callback struct in the preceding call to the search procedure, the procedure may elect not to generate a new list of files. In this case it must set <code>XmNlistUpdated</code> to False.</p>
<dd>If the search procedure generates a new list of files, it must set <code>XmNfileListItems</code> to the new list of files and <code>XmNfileListItemCount</code> to the number of items in the list. If there are no files, it sets <code>XmNfileListItems</code> to NULL and <code>XmNfileListItemCount</code> to 0 (zero). In either case it must set <code>XmNlistUpdated</code> to True.</p>
<dd>In constructing the list of files, the search procedure should include only files of the types specified by the widget&#8217;s <code>XmNfileTypeMask</code>.</p>
<dd>Setting <code>XmNdirSpec</code> is optional, but recommended. Set this attribute to the full file specification of the directory searched. The directory specification is displayed below the directory and file lists.</p>
<dt><code>XmNfileTypeMask</code></p>
<dd>Specifies the type of files listed in the file list. The possible values are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmFILE_REGULAR</code></p>
<dd>Restricts the file list to contain only regular files.</p>
<dt><code>XmFILE_DIRECTORY</code></p>
<dd>Restricts the file list to contain only directories.</p>
<dt><code>XmFILE_ANY_TYPE</code></p>
<dd>Allows the list to contain all file types including directories.</dl>
</dl>
<dt><code>XmNfilterLabelString</code></p>
<dd>Specifies the label string for the text entry field for the directory mask. The default for this resource depends on the locale. In the C locale the default is <code>Filter</code>.</p>
<dd>Now that some default localized label strings are provided through message catalogs for the children of composite widgets, the <code>labelString</code> resources cannot be set on the child through default resource files. Instead, the resource provided at the parent level must be used.</p>
<dt><code>XmNlistUpdated</code></p>
<dd>Specifies an attribute that is set only by the directory and file search procedures. This resource is set to True if the search procedure updated the directory or file list.</p>
<dt><code>XmNnoMatchString</code></p>
<dd>Specifies a string to be displayed in the file list if the list of files is empty.</p>
<dt><code>XmNpattern</code></p>
<dd>Specifies the search pattern used in combination with <code>XmNdirectory</code> in determining the files and directories to be displayed. The default value is determined by <code>XmNqualifySearchDataProc</code> and depends on the initial values of <code>XmNdirMask</code>, <code>XmNdirectory</code>, and <code>XmNpattern</code>. If the default is NULL or empty, a pattern that matches all files is used.</p>
<dt><code>XmNpathMode</code></p>
<dd>Specifies whether or not an additional text field will be used to display and edit the filter. The possible values are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmPATH_MODE_FULL</code></p>
<dd>Specifies that no additional text field will be used to display the filter. There will just be a single text field to display <code>XmNdirMask</code>.</p>
<dt><code>XmPATH_MODE_RELATIVE</code></p>
<dd>Specifies that there will be two text field displays, one to display the <code>XmNdirectory</code> and one to display the <code>XmNpattern</code>. In this instance, the <code>XmNfilterLabelString</code> resource applies to the text field for <code>XmNpattern</code> and <code>XmNdirTextLabelString</code> applies to the text field for <code>XmNdirectory</code>.</dl>
</dl>
<dt><code>XmNqualifySearchDataProc</code></p>
<dd>Specifies a search data qualification procedure to replace the default data qualification procedure. FileSelectionBox&#8217;s default data qualification procedure fulfills the needs of most applications. Because it is impossible to cover the requirements of all applications, you can replace the default procedure.</p>
<dd>The data qualification procedure is called to generate a qualified directory mask, base directory, and search pattern for use by the directory and file search procedures. It is called with three arguments: the FileSelectionBox widget and pointers to two <code>XmFileSelectionBoxCallbackStruct</code> structures. The first callback structure contains the input data. The second callback structure contains the output data, to be filled in by the data qualification procedure.</p>
<dd>If the input <i>dir</i> and <i>pattern</i> members are not NULL, the procedure must copy them to the corresponding members of the output callback structure.</p>
<dd>If the input <i>dir</i> is NULL, the procedure constructs the output <i>dir</i> as follows: If the input <i>mask</i> member is NULL, the procedure uses the widget&#8217;s <code>XmNdirectory</code> as the output <i>dir</i>; otherwise, it extracts the output <i>dir</i> from the input <i>mask</i>. If the resulting output <i>dir</i> is empty, the procedure uses the current working directory instead.</p>
<dd>If the input <i>pattern</i> is NULL, the procedure constructs the output <i>pattern</i> as follows: If the input <i>mask</i> member is NULL, the procedure uses the widget&#8217;s <code>XmNpattern</code> as the output <i>pattern</i>; otherwise, it extracts the output <i>pattern</i> from the input <i>mask</i>. If the resulting output <i>pattern</i> is empty, the procedure uses a pattern that matches all files instead.</p>
<dd>The data qualification procedure constructs the output <i>mask</i> from the output <i>dir</i> and <i>pattern</i>. The procedure must ensure that the output <i>dir</i>, <i>pattern</i>, and <i>mask</i> are fully qualified.</p>
<dd>If the input <i>value</i> member is not NULL, the procedure must copy it to the output <i>value</i> member; otherwise, the procedure must copy the widget&#8217;s <code>XmNdirSpec</code> to the output <i>value</i>.</p>
<dd>The data qualification procedure must calculate the lengths of the output <i>value</i>, <i>mask</i>, <i>dir</i>, and <i>pattern</i> members and must fill in the corresponding length members of the output callback struct.</p>
<dd>The data qualification procedure must copy the input <i>reason</i> and <i>event</i> members to the corresponding output members.</dl>
<p> The values of the <code>XmNdirSearchProc</code> and <code>XmNfileSearchProc</code> are procedure pointers of type <code>XmSearchProc</code>, defined as follows: </p>
<pre>void (* XmSearchProc) (<i>w, search_data</i>)
 Widget <i>w</i>;
 XtPointer <i>search_data</i>;</pre>
<dl COMPACT>
<dt><i>w</i></p>
<dd>The FileSelectionBox widget</p>
<dt><i>search_data</i></p>
<dd>Pointer to an <code>XmFileSelectionBoxCallbackStruct</code> containing information for conducting a search</dl>
<p> The value of the <code>XmNqualifySearchDataProc</code> resource is a procedure pointer of type <code>XmQualifyProc</code>, defined as follows: </p>
<pre>void (* XmQualifyProc) (<i>w, input_data, output_data</i>)
 Widget <i>w</i>;
 XtPointer <i>input_data</i>;
 XtPointer <i>output_data</i>;</pre>
<dl COMPACT>
<dt><i>w</i></p>
<dd>The FileSelectionBox widget</p>
<dt><i>input_data</i></p>
<dd>Pointer to an <code>XmFileSelectionBoxCallbackStruct</code> containing input data to be qualified</p>
<dt><i>output_data</i></p>
<dd>Pointer to an <code>XmFileSelectionBoxCallbackStruct</code> containing output data to be filled in by the qualification procedure</dl>
<h3>Inherited Resources</h3>
<p>FileSelectionBox inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmSelectionBox Resource Set</code>
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
<td>XmNapplyCallback</td>
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
<td>XmNapplyLabelString</td>
<td>XmCApplyLabelString</td>
<td>XmString</td>
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
<td>XmNcancelCallback</td>
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
<td>XmNcancelLabelString</td>
<td>XmCCancelLabelString</td>
<td>XmString</td>
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
<td>XmNchildPlacement</td>
<td>XmCChildPlacement</td>
<td>unsigned char</td>
<td>XmPLACE_ABOVE_SELECTION</td>
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
<td>XmNdialogType</td>
<td>XmCDialogType</td>
<td>unsigned char</td>
<td>XmDIALOG_FILE_SELECTION</td>
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
<td>XmNhelpLabelString</td>
<td>XmCHelpLabelString</td>
<td>XmString</td>
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
<td>XmNlistItemCount</td>
<td>XmCItemCount</td>
<td>int</td>
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
<td>XmNlistItems</td>
<td>XmCItems</td>
<td>XmStringTable</td>
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
<td>XmNlistLabelString</td>
<td>XmCListLabelString</td>
<td>XmString</td>
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
<td>XmNlistVisibleItemCount</td>
<td>XmCVisibleItemCount</td>
<td>int</td>
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
<td>XmNminimizeButtons</td>
<td>XmCMinimizeButtons</td>
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
<td>XmNmustMatch</td>
<td>XmCMustMatch</td>
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
<td>XmNnoMatchCallback</td>
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
<td>XmNokCallback</td>
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
<td>XmNokLabelString</td>
<td>XmCOkLabelString</td>
<td>XmString</td>
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
<td>XmNselectionLabelString</td>
<td>XmCSelectionLabelString</td>
<td>XmString</td>
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
<td>XmNtextAccelerators</td>
<td>XmCTextAccelerators</td>
<td>XtAccelerators</td>
<td>default</td>
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
<td>XmNtextColumns</td>
<td>XmCColumns</td>
<td>short</td>
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
<td>XmNtextString</td>
<td>XmCTextString</td>
<td>XmString</td>
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
</table>
</table>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmBulletinBoard Resource Set</code>
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
<td>XmNallowOverlap</td>
<td>XmCAllowOverlap</td>
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
<td>XmNautoUnmanage</td>
<td>XmCAutoUnmanage</td>
<td>Boolean</td>
<td>False</td>
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
<td>XmNbuttonFontList</td>
<td>XmCButtonFontList</td>
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
<td>XmNbuttonRenderTable</td>
<td>XmCButtonRenderTable</td>
<td>XmRenderTable</td>
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
<td>XmNcancelButton</td>
<td>XmCWidget</td>
<td>Widget</td>
<td>Cancel button</td>
<td>SG
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
<td>XmNdefaultButton</td>
<td>XmCWidget</td>
<td>Widget</td>
<td>OK button</td>
<td>SG
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
<td>XmNdefaultPosition</td>
<td>XmCDefaultPosition</td>
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
<td>XmNdialogStyle</td>
<td>XmCDialogStyle</td>
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
<td>XmNdialogTitle</td>
<td>XmCDialogTitle</td>
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
<td>XmNfocusCallback</td>
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
<td>XmNlabelFontList</td>
<td>XmCLabelFontList</td>
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
<td>XmNlabelRenderTable</td>
<td>XmCLabelRenderTable</td>
<td>XmRenderTable</td>
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
<td>XmNmapCallback</td>
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
<td>XmNmarginHeight</td>
<td>XmCMarginHeight</td>
<td>Dimension</td>
<td>10</td>
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
<td>XmNmarginWidth</td>
<td>XmCMarginWidth</td>
<td>Dimension</td>
<td>10</td>
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
<td>XmNnoResize</td>
<td>XmCNoResize</td>
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
<td>XmNresizePolicy</td>
<td>XmCResizePolicy</td>
<td>unsigned char</td>
<td>XmRESIZE_ANY</td>
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
<td>XmNshadowType</td>
<td>XmCShadowType</td>
<td>unsigned char</td>
<td>XmSHADOW_OUT</td>
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
<td>XmNtextFontList</td>
<td>XmCTextFontList</td>
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
<td>XmNtextRenderTable</td>
<td>XmCTextRenderTable</td>
<td>XmRenderTable</td>
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
<td>XmNtextTranslations</td>
<td>XmCTranslations</td>
<td>XtTranslations</td>
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
<td>XmNunmapCallback</td>
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
</table>
</table>
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
<h3>Callback Information</h3>
<p>A pointer to the following structure is passed to each callback: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent <i>* event</i>;
 XmString <i>value</i>;
 int <i>length</i>;
 XmString <i>mask</i>;
 int <i>mask_length</i>;
 XmString <i>dir</i>;
 int <i>dir_length</i>;
 XmString <i>pattern</i>;
 int <i>pattern_length</i>;
} XmFileSelectionBoxCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback</p>
<dt><i>value</i></p>
<dd>Specifies the current value of <code>XmNdirSpec</code></p>
<dt><i>length</i></p>
<dd>Specifies the number of bytes in <i>value</i> This member is obsolete and exists for compatibility with earlier releases.</p>
<dt><i>mask</i></p>
<dd>Specifies the current value of <code>XmNdirMask</code></p>
<dt><i>mask_length</i></p>
<dd>Specifies the number of bytes in <i>mask</i> This member is obsolete and exists for compatibility with earlier releases.</p>
<dt><i>dir</i></p>
<dd>Specifies the current base directory</p>
<dt><i>dir_length</i></p>
<dd>Specifies the number of bytes in <i>dir</i> This member is obsolete and exists for compatibility with earlier releases.</p>
<dt><i>pattern</i></p>
<dd>Specifies the current search pattern</p>
<dt><i>pattern_length</i></p>
<dd>Specifies the number of bytes in <i>pattern</i> This member is obsolete and exists for compatibility with earlier releases.</dl>
<h3>Translations</h3>
<p>XmFileSelectionBox inherits translations from XmSelectionBox.</p>
<h3>Accelerators</h3>
<p>The <code>XmNtextAccelerators</code> from XmSelectionBox are added to the selection and directory mask (filter) Text descendants of XmFileSelectionBox.</p>
<h3>Action Routines</h3>
<p>The XmFileSelectionBox action routines are</p>
<dl COMPACT>
<dt>SelectionBoxUpOrDown(<code>Previous|Next|First|Last</code>):</p>
<dd>If neither the selection text nor the directory mask (filter) text has the focus, this action does nothing.</p>
<dd>If the selection text has the focus, the term <i>list</i> in the following description refers to the file list, and the term <i>text</i> refers to the selection text. If the directory mask text has the focus, <i>list</i> refers to the directory list, and <i>text</i> refers to the directory mask text.</p>
<dd>When called with an argument of <code>Previous</code>, or 0 (zero) for compatibility, this action selects the previous item in the list and replaces the text with that item.</p>
<dd>When called with an argument of <code>Next</code>, or 1 for compatibility, this action selects the next item in the list and replaces the text with that item.</p>
<dd>When called with an argument of <code>First</code>, or 2 for compatibility, this action selects the first item in the list and replaces the text with that item.</p>
<dd>When called with an argument of <code>Last</code>, or 3 for compatibility, this action selects the last item in the list and replaces the text with that item.</p>
<dt>SelectionBoxRestore():</p>
<dd>If neither the selection text nor the directory mask (filter) text has the focus, this action does nothing.</p>
<dd>If the selection text has the focus, this action replaces the selection text with the selected item in the file list. If no item in the file list is selected, it clears the selection text.</p>
<dd>If the directory mask text has the focus, this action replaces the directory mask text with a new directory mask constructed from the <code>XmNdirectory</code> and <code>XmNpattern</code> resources.</dl>
<h3>Additional Behavior</h3>
<p>The FileSelectionBox widget has the following additional behavior:</p>
<dl COMPACT>
<dt><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>Calls the activate callbacks for the cancel button if it is sensitive. If no cancel button exists and the parent of the FileSelectionBox is a manager, it passes the event to the parent.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>&nbsp;<wbr>in Selection Text:</p>
<dd>Calls the selection text widget&#8217;s <code>XmNactivateCallback</code> callbacks. If <code>XmNmustMatch</code> is True and the selection text does not match an item in the file list, it calls the <code>XmNnoMatchCallback</code> callbacks with reason <code>XmCR_NO_MATCH</code>. Otherwise, it calls the <code>XmNokCallback</code> callbacks with reason <code>XmCR_OK</code>.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>&nbsp;<wbr>in Directory Mask Text:</p>
<dd>Calls the directory mask text widget&#8217;s <code>XmNactivateCallback</code> callbacks, initiates a directory and file search, and calls the <code>XmNapplyCallback</code> callbacks with reason <code>XmCR_APPLY</code>.</p>
<dt><code>&lt;Btn1Down&gt;</code><code>(2+)</code>&nbsp;<wbr>or&nbsp;<wbr><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>&nbsp;<wbr>in Directory List:</p>
<dd>Calls the directory list widget&#8217;s <code>XmNdefaultActionCallback</code> callbacks, initiates a directory and file search, and calls the <code>XmNapplyCallback</code> callbacks with reason <code>XmCR_APPLY</code>.</p>
<dt><code>&lt;Btn1Down&gt;</code><code>(2+)</code>&nbsp;<wbr>or&nbsp;<wbr><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>&nbsp;<wbr>in File List:</p>
<dd>Calls the file list widget&#8217;s <code>XmNdefaultActionCallback</code> callbacks and calls the <code>XmNokCallback</code> callbacks with reason <code>XmCR_OK</code>.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfSelect&gt;</code>&nbsp;<wbr>in Directory List:</p>
<dd>Generates a new directory mask, using the selected list item as the directory and the pattern extracted from the current directory mask text as the search pattern. If the search pattern is empty, it uses a pattern that matches all files in the directory. Replaces the directory mask text with the new directory mask.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfSelect&gt;</code>&nbsp;<wbr>in File List:</p>
<dd>Replaces the selection text with the selected list item.</p>
<dt><code>&lt;Btn2Down&gt;</code> in File List:</p>
<dd>Drags the content of one or more selected list items using the drag and drop facility. If <code>&lt;Btn2Down</code> is pressed on an unselected item, drags only that item, excluding any other selected items.</p>
<dd>This action sets the <code>XmNconvertProc</code> of the DragContext to a function that calls the <code>XmNconvertCallback</code> procedures of the file list, possibly multiple times, for the <code>_MOTIF_DROP</code> selection.</p>
<dt><code>&lt;Btn2Down&gt;</code> in Directory List:</p>
<dd>Drags the content of one or more selected list items using the drag and drop facility. If <code>&lt;Btn2Down</code> is pressed on an unselected item, it drags only that item, excluding any other selected items.</p>
<dd>This action sets the <code>XmNconvertProc</code> of the DragContext to a function that calls the <code>XmNconvertCallback</code> procedures of the directory list, possibly multiple times, for the <code>_MOTIF_DROP</code> selection.</p>
<dt><code>&lt;Apply Button Activated&gt;</code>:</p>
<dd>Initiates a directory and file search. Calls the <code>XmNapplyCallback</code> callbacks with reason <code>XmCR_APPLY</code>.</p>
<dt><code>&lt;OK Button Activated&gt;</code>:</p>
<dd>If <code>XmNmustMatch</code> is True and the selection text does not match an item in the file list, calls the <code>XmNnoMatchCallback</code> callbacks with reason <code>XmCR_NO_MATCH</code>. Otherwise, calls the <code>XmNokCallback</code> callbacks with reason <code>XmCR_OK</code>.</p>
<dt><code>&lt;Cancel Button Activated&gt;</code>:</p>
<dd>Calls the <code>XmNcancelCallback</code> callbacks with reason <code>XmCR_CANCEL</code>.</p>
<dt><code>&lt;Help Button Activated&gt;</code>:</p>
<dd>Calls the <code>XmNhelpCallback</code> callbacks with reason <code>XmCR_HELP</code>.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>If no button, list widget, or text widget has the keyboard focus, if <code>XmNmustMatch</code> is True and the selection text does not match an item in the file list, it calls the <code>XmNnoMatchCallback</code> callbacks with reason <code>XmCR_NO_MATCH</code>. Otherwise, it calls the <code>XmNokCallback</code> callbacks with reason <code>XmCR_OK</code>.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmbulletinboard/">XmBulletinBoard</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatefileselectionbox/">XmCreateFileSelectionBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatefileselectiondialog/">XmCreateFileSelectionDialog</a></code>(3), <code><a href="/docs/linux/man/3-xmfileselectionboxgetchild/">XmFileSelectionBoxGetChild</a></code>(3), <code><a href="/docs/linux/man/3-xmfileselectiondosearch/">XmFileSelectionDoSearch</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmselectionbox/">XmSelectionBox</a></code>(3) <code><a href="/docs/linux/man/3-xmvacreatefileselectionbox/">XmVaCreateFileSelectionBox</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedfileselectionbox/">XmVaCreateManagedFileSelectionBox</a></code>(3),.</p>
