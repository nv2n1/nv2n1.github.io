---
title: "editres(1)"
name: "editres"
section: "1"
letter: "e"
url: "/docs/linux/man/1-editres/"
description: "editres – a dynamic resource editor for X Toolkit applications"
---

<h2 class="name">NAME</h2>
<p> editres &#8211; a dynamic resource editor for X Toolkit applications </p>
<h2>SYNTAX</h2>
<p> <code>editres</code> [ <i>-toolkitoption</i> &#8230; ]</p>
<h2>OPTIONS</h2>
<p> <i>Editres</i> accepts all of the standard X Toolkit command line options (see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>). The order of the command line options is not important.</p>
<h2>DESCRIPTION</h2>
<p> Editres is a tool that allows users and application developers to view the full widget hierarchy of any X Toolkit application that speaks the Editres protocol. In addition, editres will help the user construct resource specifications, allow the user to apply the resource to the application and view the results dynamically. Once the user is happy with a resource specification editres will append the resource string to the user&#8217;s X Resources file.</p>
<h2>USING EDITRES</h2>
<p> <i>Editres</i> provides a window consisting of the following four areas:</p>
<dl>
<dt>Menu Bar</p>
<dd> A set of popup menus that allow you full access to editres&#8217;s features.</p>
<dt>Panner</p>
<dd> The panner allows a more intuitive way to scroll the application tree display.</p>
<dt>Message Area</p>
<dd> Displays information to the user about the action that editres expects of her.</p>
<dt>Application Widget Tree</p>
<dd> This area will be used to display the selected application&#8217;s widget tree.</dl>
<p> To begin an editres session select the <code>Get Widget Tree</code> menu item from the command menu. This will change the pointer cursor to cross hair. You should now select the application you wish look at by clicking on any of its windows. If this application understands the editres protocol then editres will display the application&#8217;s widget tree in its tree window. If the application does not understand the editres protocol editres will inform you of this fact in the message area after a few seconds delay. </p>
<p> Once you have a widget tree you may now select any of the other menu options. The effect of each of these is described below.</p>
<h2>COMMANDS</h2>
<dl>
<dt>Get Widget Tree</p>
<dd> Allows the user to click on any application that speaks the editres protocol and receive its widget tree.</p>
<dt>Refresh Current Widget Tree</p>
<dd> Editres only knows about the widgets that exist at the present time. Many applications create and destroy widgets on the fly. Selecting this menu item will cause editres to ask the application to resend its widget tree, thus updating its information to the new state of the application.</p>
<dt>
<dd> For example, xman only creates the widgets for its <i>topbox</i> when it starts up. None of the widgets for the manual page window are created until the user actually clicks on the <i>Manual Page</i> button. If you retrieved xman&#8217;s widget tree before the the manual page is active, you may wish to refresh the widget tree after the manual page has been displayed. This will allow you to also edit the manual page&#8217;s resources.</p>
<dt>Dump Widget Tree to a File</p>
<dd> For documenting applications it is often useful to be able to dump the entire application widget tree to an ASCII file. This file can then be included in the manual page. When this menu item is selected a popup dialog is activated. Type the name of the file in this dialog, and either select <i>okay</i>, or type a carriage-return. Editres will now dump the widget tree to this file. To cancel the file dialog, select the <i>cancel</i> button.</p>
<dt>Show Resource Box</p>
<dd> This command will popup a resource box for the current application. This resource box (described in detail below) will allow the user to see exactly which resources can be set for the widget that is currently selected in the widget tree display. Only one widget may be currently selected; if greater or fewer are selected editres will refuse to pop up the resource box and put an error message in the <code>Message Area</code>.</p>
<dt>Set Resource</p>
<dd> This command will popup a simple dialog box for setting an arbitrary resource on all selected widgets. You must type in the resource name, as well as the value. You can use the Tab key to switch between the resource name field the resource value field.</p>
<dt>Quit</p>
<dd> Exits editres.</dl>
<h2>TREE COMMANDS</h2>
<p> The <code>Tree</code> menu contains several commands that allow operations to be performed on the widget tree.</p>
<dl>
<dt>Select Widget in Client</p>
<dd> This menu item allows you to select any widget in the application; editres will then highlight the corresponding element the widget tree display. Once this menu item is selected the pointer cursor will again turn to a crosshair, and you must click any pointer button in the widget you wish to have displayed. Since some widgets are fully obscured by their children, it is not possible to get to every widget this way, but this mechanism does give very useful feedback between the elements in the widget tree and those in the actual application.</p>
<dt>Select All</p>
<dd>
<dt>Unselect All</p>
<dd>
<dt>Invert All</p>
<dd> These functions allow the user to select, unselect, or invert all widgets in the widget tree.</p>
<dt>Select Children</p>
<dd>
<dt>Select Parents</p>
<dd> These functions select the immediate parent or children of each of the currently selected widgets.</p>
<dt>Select Descendants</p>
<dd>
<dt>Select Ancestors</p>
<dd> These functions select all parents or children of each of the currently selected widgets. This is a recursive search.</p>
<dt>Show Widget Names</p>
<dd>
<dt>Show Class Names</p>
<dd>
<dt>Show Widget IDs</p>
<dd>
<dt>Show Widget Windows</p>
<dd> When the tree widget is initially displayed the labels of each widget in the tree correspond to the widget names. These functions will cause the label of <code>all</code> widgets in the tree to be changed to show the class name, IDs, or window associated with each widget in the application. The widget IDs, and windows are shown as hex numbers.</dl>
<p> In addition there are keyboard accelerators for each of the Tree operations. If the input focus is over an individual widget in the tree, then that operation will only effect that widget. If the input focus is in the Tree background it will have exactly the same effect as the corresponding menu item. </p>
<p> The translation entries shown may be applied to any widget in the application. If that widget is a child of the Tree widget, then it will only affect that widget, otherwise it will have the same effect as the commands in the tree menu.</p>
<dl>
<dt>Flash Active Widgets</p>
<dd> This command is the inverse of the <code>Select Widget in Client</code> command, it will show the user each widget that is currently selected in the widget tree, by flashing the corresponding widget in the application <i>numFlashes</i> (three by default) times in the <i>flashColor</i>. </p>
<table>
<tr VALIGN=top>
<td><code>Key</code></td>
<td><code>Option</code></td>
<td><code>Translation Entry</code>
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>space</td>
<td>Unselect</td>
<td>Select(nothing)
</td>
</tr>
<tr VALIGN=top>
<td>w</td>
<td>Select</td>
<td>Select(widget)
</td>
</tr>
<tr VALIGN=top>
<td>s</td>
<td>Select</td>
<td>Select(all)
</td>
</tr>
<tr VALIGN=top>
<td>i</td>
<td>Invert</td>
<td>Select(invert)
</td>
</tr>
<tr VALIGN=top>
<td>c</td>
<td>Select Children</td>
<td>Select(children)
</td>
</tr>
<tr VALIGN=top>
<td>d</td>
<td>Select Descendants</td>
<td>Select(descendants)
</td>
</tr>
<tr VALIGN=top>
<td>p</td>
<td>Select Parent</td>
<td>Select(parent)
</td>
</tr>
<tr VALIGN=top>
<td>a</td>
<td>Select Ancestors</td>
<td>Select(ancestors)
</td>
</tr>
<tr VALIGN=top>
<td>N</td>
<td>Show Widget Names</td>
<td>Relabel(name)
</td>
</tr>
<tr VALIGN=top>
<td>C</td>
<td>Show Class Names</td>
<td>Relabel(class)
</td>
</tr>
<tr VALIGN=top>
<td>I</td>
<td>Show Widget IDs</td>
<td>Relabel(id)
</td>
</tr>
<tr VALIGN=top>
<td>W</td>
<td>Show Widget Windows</td>
<td>Relabel(window)
</td>
</tr>
<tr VALIGN=top>
<td>T</td>
<td>Toggle Widget/Class Name</td>
<td>Relabel(toggle)
</td>
</tr>
</table>
<p> Clicking button 1 on a widget adds it to the set of selected widgets. Clicking button 2 on a widget deselects all other widgets and then selects just that widget. Clicking button 3 on a widget toggles its label between the widget&#8217;s instance name the widget&#8217;s class name. </p>
</dl>
<h2>USING THE RESOURCE BOX</h2>
<p> The resource box contains five different areas. Each of the areas, as they appear on the screen, from top to bottom will be discussed.</p>
<dl>
<dt>The Resource Line</p>
<dd> This area at the top of the resource box shows the current resource name exactly as it would appear if you were to save it to a file or apply it.</p>
<dt>The Widget Names and Classes</p>
<dd> This area allows you to select exactly which widgets this resource will apply to. The area contains four lines, the first contains the name of the selected widget and all its ancestors, and the more restrictive dot (<code>.</code>) separator. The second line contains less specific the Class names of each widget, and well as the less restrictive star (<code>*</code>) separator. The third line contains a set of special buttons called <code>Any Widget</code> which will generalize this level to match any widget. The last line contains a set of special buttons called <code>Any Widget Chain</code> which will turn the single level into something that matches zero or more levels. </p>
<p> The initial state of this area is the most restrictive, using the resource names and the dot separator. By selecting the other buttons in this area you can ease the restrictions to allow more and more widgets to match the specification. The extreme case is to select all the <code>Any Widget Chain</code> buttons, which will match every widget in the application. As you select different buttons the tree display will update to show you exactly which widgets will be effected by the current resource specification.</p>
<dt>Normal and Constraint Resources</p>
<dd> The next area allows you to select the name of the normal or constraint resources you wish to set. Some widgets may not have constraint resources, so that area will not appear.</p>
<dt>Resource Value</p>
<dd> This next area allows you to enter the resource value. This value should be entered exactly as you would type a line into your resource file. Thus it should contain no unescaped new-lines. There are a few special character sequences for this file: </p>
<p> 
 &#8211; This will be replaced with a newline. </p>
<p> \### &#8211; Where # is any octal digit. This will be replaced with a single byte that contains this sequence interpreted as an octal number. For example, a value containing a NULL byte can be stored by specifying 
