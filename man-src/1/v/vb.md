---
title: "vb(1)"
name: "vb"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vb/"
---

VB - Visual Builder for the Prima toolkit 

<h2>Description</h2>Visual Builder is a RAD-style suite for designing forms under the Prima toolkit. It provides rich set of perl-composed widgets, whose can be inserted into a form by simple actions. The form can be stored in a file and loaded by either user program or a simple wrapper, <tt>&quot;utils/fmview.pl&quot;</tt>; the form can be also stored as a valid perl program. 

 A form file typically has <i>.fm</i> extension, an can be loaded by using Prima::VB::VBLoader module. The following example is the only content of <tt>&quot;fmview.pl&quot;</tt>: 

 <pre> use Prima qw(Application VB::VBLoader);
 my $ret = Prima::VBLoad( $ARGV[0] );
 die &quot;$@\n&quot; unless $ret;
 $ret-&gt; execute;</pre>and is usually sufficient for executing a form file.
<h2>Help</h2>The builder provides three main windows, that are used for designing. These are called <i>main panel</i>, <i>object inspector</i> and <i>form window</i>. When the builder is started, the form window is empty. 

 The main panel consists of the menu bar, speed buttons and the widget buttons. If the user presses a widget button, and then clicks the mouse on the form window, the designated widget is inserted into the form and becomes a child of the form window. If the click was made on a visible widget in the form window, the newly inserted widget becomes a children of that widget. After the widget is inserted, its properties are accessible via the object inspector window. 

 The menu bar contains the following commands:
<dl><dt>File
<dd><dl><dd><dl><dt>New
<dd>Closes the current form and opens a new, empty form. If the old form was not saved, the user is asked if the changes made have to be saved. 

 This command is an alias to a 'new file' icon on the panel.
<dt>Open
<dd>Invokes a file open dialog, so a <i>.fm</i> form file can be opened. After the successful file load, all form widgets are visible and available for editing. 

 This command is an alias to an 'open folder' icon on the panel.
<dt>Save
<dd>Stores the form into a file. The user here can select a type of the file to be saved. If the form is saved as <i>.fm</i> form file, then it can be re-loaded either in the builder or in the user program ( see Prima::VB::VBLoader for details ). If the form is saved as <i>.pl</i> program, then it can not be loaded; instead, the program can be run immediately without the builder or any supplementary code. 

 Once the user assigned a name and a type for the form, it is never asked when selecting this command. 

 This command is an alias to a 'save on disk' icon on the panel.
<dt>Save as
<dd>Same as Save, except that a new name or type of file are asked every time the command is invoked.
<dt>Close
<dd>Closes the form and removes the form window. If the form window was changed, the user is asked if the changes made have to be saved.</dl></dl><dl><dd></dl><dt>Edit
<dd><dl><dd><dl><dt>Copy
<dd>Copies the selected widgets into the clipboard, so they can be inserted later by using Paste command. The form window can not be copied.
<dt>Paste
<dd>Reads the information, put by the builder Copy command into the clipboard, and inserts the widgets into the form window. The child-parent relation is kept by names of the widgets; if the widget with the name of the parent of the clipboard-read widgets is not found, the widgets are inserted into the form window. The form window is not affected by this command.
<dt>Delete
<dd>Deletes the selected widgets. The form window can not be deleted.
<dt>Select all
<dd>Selects all of the widgets, inserted in the form window, except the form window itself.
<dt>Duplicate
<dd>Duplicates the selected widgets. The form window is not affected by this command.
<dt>Align
<dd>This menu item contains z-ordering actions, that are performed on selected widgets. These are: 

 Bring to front Send to back Step forward Step backward Restore order</dl></dl><dl><dd></dl><dt>Change class
<dd>Changes the class of an inserted widget. This is an advanced option, and can lead to confusions or errors, if the default widget class and the supplied class differ too much. It is used when the widget that has to be inserted is not present in the builder installation. Also, it is called implicitly when a loaded form does not contain a valid widget class; in such case <i>Prima::Widget</i> class is assigned.
<dt>Creation order
<dd>Opens the dialog, that manages the creation order of the widgets. It is not that important for the widget child-parent relation, since the builder tracks these, and does not allow a child to be created before its parent. However, the explicit order might be helpful in a case, when, for example, <tt>&quot;tabOrder&quot;</tt> property is left to its default value, so it is assigned according to the order of widget creation.
<dt>Toggle lock
<dd>Changes the lock status for selected widgets. The lock, if set, prevents a widget from being selected by mouse, to avoid occasional positional changes. This is useful when a widget is used as owner for many sub-widgets. 

 Ctrl+mouse click locks and unlocks a widget.
<dt>View
<dd><dl><dd><dl><dt>Object inspector
<dd>Brings the object inspector window, if it was hidden or closed.
<dt>Add widgets
<dd>Opens a file dialog, where the additional <font SIZE="-1">VB</font> modules can be located. The modules are used for providing custom widgets and properties for the builder. As an example, the <i>Prima/VB/examples/Widgety.pm</i> module is provided with the builder and the toolkit. Look inside this file for the implementation details.
<dt>Reset guidelines
<dd>Reset the guidelines on the form window into a center position.
<dt>Snap to guidelines
<dd>Specifies if the moving and resizing widget actions must treat the form window guidelines as snapping areas.
<dt>Snap to grid
<dd>Specifies if the moving and resizing widget actions must use the form window grid granularity instead of the pixel granularity.
<dt>Run
<dd>This command hides the form and object inspector windows and 'executes' the form, as if it would be run by <tt>&quot;fmview.pl&quot;</tt>. The execution session ends either by closing the form window or by calling Break command. 

 This command is an alias to a 'run' icon on the panel.
<dt>Break
<dd>Explicitly terminates the execution session, initiated by Run command.</dl></dl><dl><dd></dl><dt>Help
<dd><dl><dd><dl><dt>About
<dd>Displays the information about the visual builder.
<dt>Help
<dd>Displays the information about the usage of the visual builder.
<dt>Widget property
<dd>Invokes a help viewer on Prima::Widget manpage and tries to open a topic, corresponding to the current selection of the object inspector property or event list. While this manpage covers far not all ( but still many ) properties and events, it is still a little bit more convenient than nothing.</dl></dl><dl><dd></dl></dl><h3>Form window</h3>The form widget is a common parent for all widgets, created by the builder. The form window provides the following basic navigation functionality.
<dl><dt>Guidelines
<dd>The form window contains two guidelines, the horizontal and the vertical, drawn as blue dashed lines. Dragging with the mouse can move these lines. If menu option ``Snap to guidelines'' is on, the widgets moving and sizing operations treat the guidelines as the snapping areas.
<dt>Selection
<dd>A widget can be selected by clicking with the mouse on it. There can be more than one selected widget at a time, or none at all. To explicitly select a widget in addition to the already selected ones, hold the <tt>&quot;shift&quot;</tt> key while clicking on a widget. This combination also deselects the widget. To select all widgets on the form window, call ``Select all'' command from the menu. To prevent widgets from being occasionally selected, lock them with ``Edit/Toggle lock'' command or Ctrl+mouse click.
<dt>Moving
<dd>Dragging the mouse can move the selected widgets. The widgets can be snapped to the grid or the guidelines during the move. If one of the moving widgets is selected in the object inspector window, the coordinate changes are reflected in the <tt>&quot;origin&quot;</tt> property. 

 If the <tt>&quot;Tab&quot;</tt> key is pressed during the move, the mouse pointer is changed between three states, each reflecting the currently accessible coordinates for dragging. The default accessible coordinates are both the horizontal and the vertical; other two are the horizontal only and the vertical only.
<dt>Sizing
<dd>The sizeable widgets can be dynamically resized. Regardless to the amount of the selected widgets, only one widget at a time can be resized. If the resized widget is selected in the object inspector window, the size changes are reflected in the <tt>&quot;size&quot;</tt> property.
<dt>Context menus
<dd>The right-click ( or the other system-defined pop-up menu invocation command) provides the menu, identical to the main panel's Edit submenu. 

 The alternative context menus can be provided with some widgets ( for example, <tt>&quot;TabbedNotebook&quot;</tt> ), and are accessible with <tt>&quot;control + right click&quot;</tt> combination.</dl><h3>Object inspector window</h3>The inspector window reflects the events and properties of a widget. To explicitly select a widget, it must be either clicked by the mouse on the form window, or selected in the widget combo-box. Depending on whether the properties or the events are selected, the left panel of the inspector provides the properties or events list, and the right panel - a value of the currently selected property or event. To toggle between the properties and the events, use the button below the list. 

 The adjustable properties of a widget include an incomplete set of the properties, returned by the class method <tt>&quot;profile_default&quot;</tt> ( the detailed explanation see in Prima::Object). Among these are such basic properties as <tt>&quot;origin&quot;</tt>, <tt>&quot;size&quot;</tt>, <tt>&quot;name&quot;</tt>, <tt>&quot;color&quot;</tt>, <tt>&quot;font&quot;</tt>, <tt>&quot;visible&quot;</tt>, <tt>&quot;enabled&quot;</tt>, <tt>&quot;owner&quot;</tt> and many others. All the widgets share some common denominator, but almost all provide their own intrinsic properties. Each property can be selected by the right-pane hosted property selector; in such case, the name of a property is highlighted in the list - that means, that the property is initialized. To remove a property from the initialization list, double-click on it, so it is grayed again. Some very basic properties as <tt>&quot;name&quot;</tt> can not be deselected. This is because the builder keeps a name-keyed list; another consequence of this fact is that no widgets of same name can exist simultaneously within the builder. 

 The events, much like the properties, are accessible for direct change. All the events provide a small editor, so the custom code can be supplied. This code is executed when the form is run or loaded via <tt>&quot;Prima::VB::VBLoader&quot;</tt> interface. 

 The full explanation of properties and events is not provided here. It is not even the goal of this document, because the builder can work with the widgets irrespective of their property or event capabilities; this information is extracted by native toolkit functionality. To read on what each property or event means, use the documentation on the class of interest; Prima::Widget is a good start because it encompasses the ground <tt>&quot;Prima::Widget&quot;</tt> functionality. The other widgets are ( hopefully ) documented in their modules, for example, <tt>&quot;Prima::ScrollBar&quot;</tt> documentation can be found in Prima::ScrollBar.
<h2>See Also</h2>Prima, Prima::VB::VBLoader
<h2>Author</h2>Dmitry Karasik, &lt;dmitry [at] karasik.eu.org&gt;.
<h2>Copyright</h2>This program is distributed under the <font SIZE="-1">BSD</font> License.
