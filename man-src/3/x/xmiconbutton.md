---
title: "xmiconbutton(3)"
name: "xmiconbutton"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmiconbutton/"
---

The Icon Button widget
<h2>Synopsis</h2>Documents the XmIconButton widget
<h2>Description</h2><table> <tr VALIGN=top></tr><tr VALIGN=top><td><font SIZE="+9">&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></font></td></tr> </table> 

 The Icon Button widget is a selectable area of the screen that contains both a label and a string. When the user selects this button with the OSF/Motif select button its activateCallback is called. This widget can also be used as a Toggle button, although it will have no indicator. The placement of the icon relative to the text can be modified by using the iconPlacement resource. 

 Note: This widget takes a String as its label, not an XmString, so there is no need to use XmStringCreate to get a properly formatted string. Internationalized text is not currently supported. 

<h2>Normal Resources</h2><table> <tr VALIGN=top><td>Name</td><td>Class</td><td>Type</td><td>Initial Value
</td></tr><tr VALIGN=top><td>activateCallback</td><td>Callback</td><td>Callback</td><td>NULL
</td></tr><tr VALIGN=top><td>alignment</td><td>Alignment</td><td>Alignment</td><td>XmALIGNMENT_
</td></tr><tr VALIGN=top><td></td><td></td><td></td><td> BEGINNING
</td></tr><tr VALIGN=top><td>armColor</td><td>ArmColor</td><td>Pixel</td><td>&lt;dynamic&gt;
</td></tr><tr VALIGN=top><td>doubleClickCallback</td><td>Callback</td><td>Callback</td><td>NULL
</td></tr><tr VALIGN=top><td>fontList</td><td>FontList</td><td>FontList</td><td>fixed
</td></tr><tr VALIGN=top><td>horizontalMargin</td><td>Space</td><td>HorizontalDimension</td><td>2
</td></tr><tr VALIGN=top><td>iconTextPadding</td><td>Space</td><td>VerticalDimension</td><td>2
</td></tr><tr VALIGN=top><td>iconPlacement</td><td>IconPlacement</td><td>IconPlacement</td><td>XmIconTop
</td></tr><tr VALIGN=top><td>label</td><td>Label</td><td>String</td><td>Widget name
</td></tr><tr VALIGN=top><td>labelString</td><td>LabelString</td><td>XmString</td><td>Widget name
</td></tr><tr VALIGN=top><td>pixmap</td><td>Pixmap</td><td>Pixmap</td><td>None
</td></tr><tr VALIGN=top><td>recomputeSize</td><td>Boolean</td><td>Boolean</td><td>True
</td></tr><tr VALIGN=top><td>set</td><td>Boolean</td><td>Boolean</td><td>False
</td></tr><tr VALIGN=top><td>stringDirection</td><td>StringDirection</td><td>StringDirection</td><td>XmSTRING_
</td></tr><tr VALIGN=top><td></td><td></td><td></td><td>DIRECTION_L_TO_R
</td></tr><tr VALIGN=top><td>verticalMargin</td><td>Space</td><td>VerticalDimension</td><td>2
</td></tr> </table> 

 All resource names begin with XmN and all resource class names begin with XmC. 

<h2>activateCallback</h2>This list of callback routines is called whenever the icon button is clicked on by the user. The format of the callback routines is specified below. 

<h2>armColor</h2>This is the pixel index that describes the color to fill the widget with when it is set. 

<h2>doubleClickCallback</h2>This list of callback routines is called whenever the user double clicks on this widget. The format of the callback routines is specified below. 

<h2>fontList</h2>The default font in this list is used to render the label string of the icon button. 

<h2>horizontalMargin</h2><h2>verticalMargin</h2>The amount of space to be left between the edge of the shadow and the text or pixmap displayed. The vertical and horizontal spacing can be controlled independently. 

<h2>iconTextPadding</h2>The amount of space to be left between the pixmap and the label string. 

<h2>iconPlacement</h2>The location of the pixmap (icon) with respect to the displayed text. This resource can take one of the following values: XmIconTop, XmIconBottom, XmIconLeft, XmIconRight, XmIconNone, and XmIconOnly. A type converter has been registered that converts the following strings: &quot;top&quot;, &quot;bottom&quot;, &quot;left&quot;, &quot;right&quot;, &quot;none&quot;, and &quot;iconOnly&quot;. 

 If only a string is displayed in the Icon Button, this resource can be used to change the justification of the label. XmIconTop=bottom, XmIconBottom=top, XmIconRight=Left, XmIconLeft=Right, XmIconNone=Center. In order to use these options, pixmap must be set to None. 

<h2>label</h2>The string to display in this button. This string can only have one font, but can be any number of lines long. Use the NEW_LINE character ( ' ) to separate lines. This resource has been superceded by labelString, but is included for backwards compatibility. If XmNlabelString is set , XmNlabel is ignored 

<h2>labelString</h2>Specifies the compound string to be displayed in the button. If this value is NULL, the value of XmNlabel is used. If both are NULL, labelString is initialized by converting the name of the widget to a compound string. Refer to <a HREF="//www.systutorials.com/docs/linux/man/3X-XmString/">XmString</a>(3X) in the OSD/Motif Programmers' Reference for more information on the creation and structure of compound strings.
<h2>pixmap</h2>The pixmap to display. This pixmap may either be of depth one (1), or the same depth as the screen this widget is being displayed on. If the pixmap is of depth one then XCopyPlane is used to render the pixmap in the foreground and background colors. If the pixmap is not of depth one then XCopyArea is used and all the original colors of the pixmap are preserved. Unlike the Motif PushButton widget the pixmap is automatically stippled when the Icon Button becomes insensitive. 

<h2>recomputeSize</h2>If this Boolean value is True then the icon button will ask its parent to resize it to be just large enough to contain the pixmap, label and shadows. If it is False then the icon button will not attempt a resize. 

<h2>set</h2>This Boolean value represents the current state of the icon button. If this value is True then the icon button is set and is rendered as depressed. Otherwise it is unset and is rendered normally. 

<h2>stringDirection</h2>Specifies the direction in which the string is to be drawn. XmNSTRING_DIRECTION_L_TO_R is drawn left to right, while XmNSTRING_DIRECTION_R_TO_L is drawn right to left. The default for this resource is determined at creation time. If no value is specified for this resource and the widget's parent is a manager, the value is inherited from the parent; otherwise, it defaults to XmNSTRING_DIRECTION_L_TO_R. 

<h2>Callback Routines</h2>Whenever the user selects the icon button the activate callbacks will be called. When- ever the user double clicks on this widget the first click will call the activateCallback, and if the second occurs within MultiClickTime it will call the doubleClickCallback.. These callbacks have the following parameters: 

<dl COMPACT><dd>void (activate_callback)(Widget w, XtPointer client_data, XtPointer call_data) 

<dd>w<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the Icon Button widget

<dd>client_data<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the client data specified by the application

<dd>call_data<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>a pointer to an XmIconButtonCallbackInfo structure
 

<dd>void (double_click_callback)(Widget w, XtPointer client_data, XtPointer call_data) 

<dd>w<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the Icon Button widget

<dd>client_data<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the client data specified by the application

<dd>call_data<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>a pointer to an XmIconButtonCallbackInfo structure
</dl>
 

 All procedures on the Icon Button's activateCallback and doubleClickCallback lists will have a pointer to an IconButtonCallbackInfo structure passed to them in the call_data field. This structure is defined in the Icon Button widget's public header file as follows: 

 typedef struct _XmIconButtonCallbackInfo { 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Boolean state; /* The current state of the icon button.*/
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XEvent * event; /* The event that caused this action.*/
 

 } XmIconButtonCallbackInfo; 

<dl COMPACT><dd>state<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the current state of the icon button. When this is used as a push 
 button (the default) the state variable will always be True.
<dd>event<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the X Event that caused this action, see Translations and Actions 
 below for details on the events that can cause these callbacks to be called.</dl><h2>Convenience Routine</h2><h2>
<dt></h2></dl><h2>XmCreateIconButton - Widget creation convenience routine</h2><pre><dd>Widget XmCreateIconButton( 
 Widget parent,/* Widget id of parent for IconButton */
 String name, /* Name of the created widget */
 ArgList args,/* argument list */
 Cardinal num_args/* number of items in argument list */
 ) 
Translations and Actions:
The following are the default translation bindings used by the icon button:</pre><table> <tr VALIGN=top><td>&lt;Btn1Down&gt;,&lt;Btn1Up&gt;:</td><td>XmToggle() XmNotify()
</td></tr><tr VALIGN=top><td>&lt;Btn1Down&gt;(2):</td><td>XmDoubleNotify()
</td></tr><tr VALIGN=top><td>&lt;Btn1Down&gt;:</td><td>XmGetFocus() XmToggle()
</td></tr><tr VALIGN=top><td>&lt;Key&gt;osfSelect:</td><td>XmArmAndActivate()
</td></tr><tr VALIGN=top><td>&lt;Key&gt;osfActivate:</td><td>XmArmAndActivate()
</td></tr><tr VALIGN=top><td>None&lt;Key&gt;space:</td><td>XmArmAndActivate()
</td></tr><tr VALIGN=top><td>None&lt;Key&gt;Return:</td><td>XmArmAndActivate()
</td></tr><tr VALIGN=top><td>&lt;Btn1Down&gt;,&lt;Leave&gt;</td><td>XmToggle()
</td></tr> </table> <pre>The following actions are supported by the icon button:
<dl COMPACT><dt><dd>XmToggle() Toggles the state of the icon button.
<dt><dd>XmNotify() Calls all routines on activateCallback list.
<dt><dd>XmDoubleNotify()Calls all routines on the doubleClickCallback list. 
<dt><dd>XmArmAndActivated()This action will arm the button, call the actions on the activateCallback 
list, wait a fraction of a second and then disarm the button.
</dl>
To use this button as a toggle button rather than a push button, replace the default 
translation table with the following table.</pre><table> <tr VALIGN=top><td>&lt;Btn1Down&gt;:</td><td>XmToggle() XmNotify()
</td></tr><tr VALIGN=top><td>&lt;Btn1Up&gt;(2):</td><td>XmDoubleNotify()
</td></tr><tr VALIGN=top><td>&lt;Key&gt;osfSelect:</td><td>XmToggle() XmNotify()
</td></tr><tr VALIGN=top><td>&lt;Key&gt;osfActivate:</td><td>XmToggle() XmNotify()
</td></tr><tr VALIGN=top><td>None&lt;Key&gt;space:</td><td>XmToggle() XmNotify()
</td></tr><tr VALIGN=top><td>None&lt;Key&gt;Return:</td><td>XmToggle() XmNotify()
</td></tr> </table><h2>Copyright</h2>Copyright (c) 1992 by Integrated Computer Solutions, Inc.
