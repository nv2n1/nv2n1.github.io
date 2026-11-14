---
title: "xmspinbox(3)"
name: "xmspinbox"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmspinbox/"
description: "XmSpinBox — The SpinBox widget class"
---

<p><code>XmSpinBox</code> &#8212; The SpinBox widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/SpinB.h&gt;</pre>
<h2>Description</h2>
<p>SpinBox allows the user to select a value from a ring of related but mutually exclusive choices which are displayed in sequence. The SpinBox always has an increment arrow, a decrement arrow, and one or more other children. The choices are displayed, one at a time, in a traversable text child ( <code>XmText</code> or <code>XmTextField</code>. The user clicks <code>&lt;Btn1&gt;</code> on an arrow to display the next (or previous) item in the ring of choices. By pressing and holding <code>&lt;Btn1&gt;</code> on an arrow, the user continuously cycles through the choices. </p>
<p> The traversable children in a SpinBox can be of type <code>XmNUMERIC</code> or <code>XmSTRING</code>, as defined by the <code>XmNspinBoxChildType</code> constraint resource. The ring of choices for numeric children is defined by minimum, maximum, incremental, and decimal point values. The ring of choices for string children is defined in an array of compound strings. </p>
<p> The application programmer can include multiple traversable children in the SpinBox. For example, a SpinBox might consist of a pair of arrows and month, day, and year text fields. The arrows only spin the child that currently has focus. </p>
<p> Arrow size is specified by the SpinBox resource <code>XmNarrowSize</code>. This value sets both width and height of each arrow in pixels. </p>
<p> The programmer can display SpinBox arrows in one of several layouts, as specified by the <code>XmNarrowLayout</code> resource:</p>
<dl COMPACT>
<dt><code>XmARROWS_BEGINNING</code></p>
<dd>Places a pair of left and right arrows before the children.</p>
<dt><code>XmARROWS_END</code></p>
<dd>Places a pair of left and right arrows after the children.</p>
<dt><code>XmARROWS_SPLIT</code></p>
<dd>Places one arrow on each side of the children.</p>
<dt><code>XmARROWS_FLAT_BEGINNING</code></p>
<dd>Places a pair of arrows side by side before the <code>XmSpinBox</code> children.</p>
<dt><code>XmARROWS_FLAT_BEGINNING</code></p>
<dd>Places a pair of arrows side by side after the <code>XmSpinBox</code> children.</dl>
<p> Positions for <code>XmARROWS_BEGINNING</code> and <code>XmARROWS_END</code> are dependent on the <code>VendorShell</code> resource <code>XmNlayoutDirection</code>. When layout direction is left-to-right, beginning arrows are positioned to the left of the children. When layout direction is right-to-left, beginning arrows are positioned to the right. </p>
<p> The actions of the arrows are determined by the <code>VendorShell</code> resource <code>XmNlayoutDirection</code>. For left-to-right layouts, the right arrow is the increment arrow and the left arrow is the decrement arrow. For right-to-left layouts, the right arrow is the decrement arrow and the left arrow is the increment arrow. </p>
<p> For a numeric type child, the increment arrow increases the displayed value by the incremental value up to the maximum. The decrement arrow decreases the displayed value by the given incremental value down to the minimum. </p>
<p> The increment arrow for a string type child moves toward the last entry of the array of compound strings (by increasing the SpinBox constraint resource <code>XmNposition</code>). The decrement arrow moves toward the first entry of the compound string array. </p>
<p> The programmer can also control the sensitivity of each arrow in the SpinBox. Sensitive arrows spin choices; insensitive arrows do not spin choices. Arrow sensitivity is set for the SpinBox widget by using the <code>XmNdefaultArrowSensitivity</code> resource, but it can be modified on a per child basis by using the <code>XmNarrowSensitivity</code> constraint resource. </p>
<p> SpinBox provides two callbacks to application programmers. (In addition, the callbacks of the SpinBox&#8217;s children may be invoked.) Each of these callbacks receives a pointer to <code>XmSpinBoxCallbackStruct</code>. The <code>XmNmodifyVerifyCallback</code> procedures are called <i>before</i> a new choice is displayed. The <code>XmNvalueChangedCallback</code> procedures are called <i>after</i> a new choice is displayed. </p>
<p> <code>XmNmodifyVerifyCallback</code> tells the application what the new position will be in the ring of choices. This callback can be used to make the SpinBox stop at the upper and lower limits or go to a different, nonconsecutive choice. The application allows the change in position by leaving the <i>doit</i> member set to True. The application can spin to a position other than the next consecutive position by leaving <i>doit</i> set to True and by changing the <i>position</i> member to the desired position. When <i>doit</i> is set to False by an application, there is no change in the choice displayed. </p>
<p> After a new choice is displayed, the <code>XmNvalueChangedCallback</code> procedure is called. The application can use this procedure to perform tasks when specific values are reached or when boundaries are crossed. For example, if the user spins from January back to December, the application could change to the previous year. If the user spins from December to January, the application could change to the next year. </p>
<p> SpinBox dimensions can be set using the Core resources <code>XmNheight</code> and <code>XmNwidth</code>. If dimensions are not specified, the SpinBox size is determined by the sizes of its arrows and children. The SpinBox will attempt to grow so that the arrows and all children are visible. </p>
<p> SpinBox uses the <code>XmQTaccessTextual</code> trait and holds the <code>XmQTnavigator</code> trait.</p>
<h3>Classes</h3>
<p>SpinBox inherits behavior, resources, and traits from the <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, and <code>XmManager</code> classes. </p>
<p> The class pointer is <code>xmSpinBoxWidgetClass</code>. </p>
<p> The class name is <code>XmSpinBox</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate whether the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table>
<tr VALIGN=top>
<td><code>XmSpinBox Resource</code></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Set</td>
<td></td>
<td></td>
<td></td>
<td>
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
<td>XmNarrowLayout</td>
<td>XmCArrowLayout</td>
<td>unsigned char</td>
<td>XmARROWS_BEGINNING</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNarrowOrientation</td>
<td>XmCArrowOrientation</td>
<td>unsigned char</td>
<td>XmARROWS_VERTICAL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNarrowSize</td>
<td>XmCArrowSize</td>
<td>Dimension</td>
<td>16</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNdefaultArrowSensitivity</td>
<td>XmCDefaultArrowSensitivity</td>
<td>unsigned char</td>
<td>XmARROWS_SENSITIVE</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNdetailShadowThickness</td>
<td>XmCDetailShadowThickness</td>
<td>Dimension</td>
<td>2</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNinitialDelay</td>
<td>XmCInitialDelay</td>
<td>unsigned int</td>
<td>250 ms</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNmarginHeight</td>
<td>XmCMarginHeight</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNmarginWidth</td>
<td>XmCMarginWidth</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNmodifyVerifyCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>XmNrepeatDelay</td>
<td>XmCRepeatDelay</td>
<td>unsigned int</td>
<td>200 ms</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNspacing</td>
<td>XmCSpacing</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNvalueChangedCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
</table>
<dl COMPACT>
<dt><code>XmNarrowLayout</code></p>
<dd>Specifies placement of the two arrows in the widget. Possible layouts are as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmARROWS_BEGINNING</code></p>
<dd>Places left and right arrows beside each other, before the child(ren). Positioning for this layout is dependent on the VendorShell resource <code>XmNlayoutDirection.</code></p>
<dt><code>XmARROWS_END</code></p>
<dd>Places left and right arrows beside each other, after the child(ren). Positioning for this layout is dependent on the VendorShell resource <code>XmNlayoutDirection</code>.</p>
<dt><code>XmARROWS_FLAT_BEGINNING</code></p>
<dd>Places a pair of arrows side by side before the <code>XmSpinBox</code> children. Positioning for this layout is dependent on the VendorShell resource <code>XmNlayoutDirection.</code></p>
<dt><code>XmARROWS_FLAT_END</code></p>
<dd>Places a pair of arrows side by side after the <code>XmSpinBox</code> children. Positioning for this layout is dependent on the VendorShell resource <code>XmNlayoutDirection.</code></p>
<dt><code>XmARROWS_SPLIT</code></p>
<dd>Places a left arrow on the left side and a right arrow on the right side of the child(ren).</dl>
</dl>
<dt><code>XmNarrowSize</code></p>
<dd>Specifies both the width and height of the arrow in pixels.</p>
<dt><code>XmNdefaultArrowSensitivity</code></p>
<dd>Specifies the default sensitivity of the arrows in the widget. Insensitive arrows change color, cannot be depressed, and perform no action. (This resource may be overridden by the constraint resource <code>XmNarrowSensitivity</code> for individual traversable text children of the SpinBox.) Possible default sensitivity values are as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmARROWS_SENSITIVE</code></p>
<dd>Both arrows are sensitive.</p>
<dt><code>XmARROWS_DECREMENT_SENSITIVE</code></p>
<dd>Only the decrement arrow (as determined by <code>XmNlayoutDirection</code>) is sensitive. The increment arrow is insensitive.</p>
<dt><code>XmARROWS_INCREMENT_SENSITIVE</code></p>
<dd>Only the increment arrow (as determined by <code>XmNlayoutDirection</code>) is sensitive. The decrement arrow is insensitive.</p>
<dt><code>XmARROWS_INSENSITIVE</code></p>
<dd>Both arrows are insensitive.</dl>
</dl>
<dt><code>XmNdetailShadowThickness</code></p>
<dd>Specifies the thickness of the inside arrow shadows. The default thickness is 2 pixels.</p>
<dt><code>XmNinitialDelay</code></p>
<dd>Specifies how long, in milliseconds, the mouse button must be held down before automatic spinning begins. In other words, when the user selects the increment or decrement arrow and keeps it depressed, this delay occurs before the choices start spinning. If <code>XmNinitialDelay</code> is 0, then <code>XmNrepeatDelay</code> is used as the initial delay.</p>
<dt><code>XmNmarginHeight</code></p>
<dd>Specifies the amount of blank space between the top edge of the SpinBox widget and the first item in each column, and the bottom edge of the SpinBox widget and the last item in each column.</p>
<dt><code>XmNmarginWidth</code></p>
<dd>Specifies the amount of blank space between the left edge of the SpinBox widget and the first item in each row, and the right edge of the SpinBox widget and the last item in each row.</p>
<dt><code>XmNmodifyVerifyCallback</code></p>
<dd>This callback is called before the SpinBox position changes (see the Constraint resource <code>XmNposition</code>). The application can use this callback to set the next position, change SpinBox resources, or cancel the impending action. For example, this callback can be used to stop the spinning just before wrapping at the upper and lower position boundaries. If the <i>doit</i> member is set to False, nothing happens. Otherwise the position changes. Reasons sent by the callback are <code>XmCR_SPIN_NEXT</code>, <code>XmCR_SPIN_PRIOR</code>, <code>XmCR_SPIN_FIRST</code>, or <code>XmCR_SPIN_LAST</code>.</p>
<dt><code>XmNrepeatDelay</code></p>
<dd>When the user selects and keeps an arrow button depressed by pressing and holding <code>&lt;Btn1&gt;</code>, spinning begins. After the time specified in <code>XmNinitialDelay</code> elapses, the SpinBox position changes automatically until the arrow button is released. The <code>XmNrepeatDelay</code> resource specifies the delay in milliseconds between each automatic change. If <code>XmNrepeatDelay</code> is set to 0 (zero), automatic spinning is turned off and <code>XmNinitialDelay</code> is ignored.</p>
<dt><code>XmNspacing</code></p>
<dd>Specifies the horizontal and vertical spacing between items contained within the SpinBox widget.</p>
<dt><code>XmNvalueChangedCallback</code></p>
<dd>This is called <i>n</i>+1 times for <i>n</i> SpinBox position changes (see the Constraint resource <code>XmNposition</code>). Reasons sent by the callback are <code>XmCR_OK</code>, <code>XmCR_SPIN_NEXT</code>, <code>XmCR_SPIN_PRIOR</code>, <code>XmCR_SPIN_FIRST</code>, or <code>XmCR_SPIN_LAST</code>. Other members are detailed in the callback structure description. </p>
<table>
<tr VALIGN=top>
<td><code>XmSpinBox Constraint</code></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Resource Set</td>
<td></td>
<td></td>
<td></td>
<td>
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
<td>XmNarrowSensitivity</td>
<td>XmCArrowSensitivity</td>
<td>unsigned char</td>
<td>XmARROWS_DEFAULT_SENSITIVITY</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNdecimalPoints</td>
<td>XmCDecimalPoints</td>
<td>short</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNincrementValue</td>
<td>XmCIncrementValue</td>
<td>int</td>
<td>1</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNmaximumValue</td>
<td>XmCMaximumValue</td>
<td>int</td>
<td>10</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNminimumValue</td>
<td>XmCMinimumValue</td>
<td>int</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNnumValues</td>
<td>XmCNumValues</td>
<td>int</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNposition</td>
<td>XmCPosition</td>
<td>int</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNpositionType</td>
<td>XmCPositionType</td>
<td>char</td>
<td>XmPOSITION_VALUE</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>XmNspinBoxChildType</td>
<td>XmSpinBoxChildType</td>
<td>unsigned char</td>
<td>XmSTRING</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>XmNvalues</td>
<td>XmCValues</td>
<td>XmStringTable</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
</table>
<dt><code>XmNarrowSensitivity</code></p>
<dd>Specifies the sensitivity of the arrows for a SpinBox child. By using this resource in the definition of a SpinBox child, the application programmer can override the default SpinBox sensitivity (set by <code>XmNdefaultArrowSensitivity</code>) for a particular child. This allows each traversable child to have a different arrow sensitivity. The arrow sensitivity values are as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmARROWS_SENSITIVE</code></p>
<dd>Both arrows are sensitive.</p>
<dt><code>XmARROWS_DECREMENT_SENSITIVE</code></p>
<dd>Only the decrement arrow (as determined by <code>XmNlayoutDirection</code>) is sensitive.</p>
<dt><code>XmARROWS_INCREMENT_SENSITIVE</code></p>
<dd>Only the increment arrow (as determined by <code>XmNlayoutDirection</code>) is sensitive.</p>
<dt><code>XmARROWS_INSENSITIVE</code></p>
<dd>Both arrows are insensitive.</p>
<dt><code>XmARROWS_DEFAULT_SENSITIVITY</code></p>
<dd>Use the sensitivity specified in the <code>XmNdefaultArrowSensitivity</code> resource.</dl>
</dl>
<dt><code>XmNdecimalPoints</code></p>
<dd>Specifies the number of decimal places used when displaying the value of a SpinBox numeric type child. If the number of decimal places specified is greater than the number of digits in a displayed value, the value is padded with 0 (zeros). For example, when <code>XmNinitialValue</code> is 1 and <code>XmNmaximumValue</code> is 1000 and <code>XmNdecimalPoints</code> is 3, the range of values displayed in the SpinBox is 0.001 to 1.000. This is used only when <code>XmNspinBoxChildType</code> is <code>XmNUMERIC</code>.</p>
<dt><code>XmNincrementValue</code></p>
<dd>Specifies the amount by which to increment or decrement a SpinBox numeric type child. This is used only when <code>XmNspinBoxChildType</code> is <code>XmNUMERIC</code>.</p>
<dt><code>XmNmaximumValue</code></p>
<dd>Specifies the highest possible value for a numeric SpinBox. This is used only when <code>XmNspinBoxChildType</code> is <code>XmNUMERIC</code>.</p>
<dt><code>XmNminimumValue</code></p>
<dd>Specifies the lowest possible value for a numeric SpinBox. This is used only when <code>XmNspinBoxChildType</code> is <code>XmNUMERIC</code>.</p>
<dt><code>XmNnumValues</code></p>
<dd>Specifies the number of strings in <code>XmNvalues</code>. The application must change this value when strings are added or removed from <code>XmNvalues</code>. This is used only when <code>XmNspinBoxChildType</code> is <code>XmSTRING</code>.</p>
<dt><code>XmNposition</code></p>
<dd>Specifies the position of the currently displayed item. The interpritation of <code>XmNposition</code> is dependent upon the value of the <code>XmNpositionType</code> resource.</p>
<dd>When <code>XmNpositionType</code> is <code>XmPOSITION_INDEX</code> the <code>XmNposition</code> value is interpreted as follows: For <code>XmSpinBox</code> children of type <code>XmNUMERIC</code>, the <code>XmNposition</code> resource is interpreted as an index into an array of items. The minimum allowable value for <code>XmNposition</code> is 0. The maximum allowable value for <code>XmNposition</code> is <code>(XmNmaximumValue-XmNminimumValue)/XmNincrementValue</code>. The value display by the <code>XmSpinBox</code> child is <code>XmNminimumValue+(XmNposition*XmNincrementValue)</code>. For <code>XmSpinBox</code> children of type <code>XmSTRING</code>, the <code>XmNposition</code> resource is interpreted as an index into an array of <code>XmNnumValues</code> items. The minimum allowable value for <code>XmNposition</code> is 0. The maximum allowable value for <code>XmNposition</code> is <code>XmNnumValues &#8211; 1</code>. The value displayed by the <code>XmSpinBox</code> is the <code>XmNposition</code>&#8216;th value in the <code>XmNvalues</code> array.</p>
<dd>When <code>XmNpositionType</code> is <code>XmPOSITION_VALUE</code> the <code>XmNposition</code> value is interpreted as follows:</p>
<dd>For <code>XmSpinBox</code> children of type <code>XmNUMERIC</code>, the <code>XmNposition</code> resource is interpreted as the actual value to be displayed. The minimum allowable value for <code>XmNposition</code> is <code>XmNminimumValue</code>. The maximum allowable value for <code>XmNposition</code> is <code>XmNmaximumValue</code>. The value displayed by the <code>XmSpinBox</code> child is <code>XmNposition</code>. For <code>XmSpinBox</code> children of type <code>XmSTRING</code>, the interpretation is the same for <code>XmPOSITION_VALUE</code> as for <code>XmPOSITION_INDEX</code>.</p>
<dd>Position values falling outside the specified range are invalid. When an application assigns a value to <code>XmNposition</code> which is less than the minimum, <code>XmNposition</code> is set to the minimum and an error message is displayed. When an application assigns a value to <code>XmNposition</code> which is greater than the maximum, <code>XmNposition</code> is set to the maximum and an error message is displayed.</p>
<dt><code>XmNpositionType</code></p>
<dd>Specifies how values the <code>XmNposition</code> resource are to be interpreted. Valid values include <code>XmPOSITION_INDEX</code> and <code>XmPOSITION_VALUE</code>.</p>
<dt><code>XmNspinBoxChildType</code></p>
<dd>Specifies the type of data displayed in the child:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmNUMERIC</code></p>
<dd>The SpinBox choice range is defined by numeric minimum, maximum, and incremental values.</p>
<dt><code>XmSTRING</code></p>
<dd>The SpinBox choices are alphanumeric.</dl>
</dl>
<dt><code>XmNvalues</code></p>
<dd>Specifies the array of <code>XmString</code>s to be displayed in a SpinBox string type child. The application must change <code>XmNnumValues</code> when strings are added to or removed from <code>XmNvalues</code>. This is used only when <code>XmNspinBoxChildType</code> is <code>XmSTRING</code>.</dl>
<h3>Inherited Resources</h3>
<p>SpinBox inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
<table>
<tr VALIGN=top>
<td><code>XmManager Resource</code></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Set</td>
<td></td>
<td></td>
<td></td>
<td>
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
<td>XmNbottomShadowColor</td>
<td>XmCBottomShadowColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNforeground</td>
<td>XmCForeground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNhighlightColor</td>
<td>XmCHighlightColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNinitialFocus</td>
<td>XmCInitialFocus</td>
<td>Widget</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNnavigationType</td>
<td>XmCNavigationType</td>
<td>XmNavigationType</td>
<td>XmTAB_GROUP</td>
<td>CSG
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
<td>XmNshadowThickness</td>
<td>XmCShadowThickness</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
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
<td>XmNtopShadowColor</td>
<td>XmCTopShadowColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNtraversalOn</td>
<td>XmCTraversalOn</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
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
<td>XmNuserData</td>
<td>XmCUserData</td>
<td>XtPointer</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
</table>
<table>
<tr VALIGN=top>
<td><code>Composite Resource</code></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Set</td>
<td></td>
<td></td>
<td></td>
<td>
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
<td>XmNchildren</td>
<td>XmCReadOnly</td>
<td>WidgetList</td>
<td>NULL</td>
<td>G
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
<td>XmNnumChildren</td>
<td>XmCReadOnly</td>
<td>Cardinal</td>
<td>0</td>
<td>G
</td>
</tr>
</table>
<table>
<tr VALIGN=top>
<td><code>Core Resource Set</code></td>
<td></td>
<td></td>
<td></td>
<td>
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
<td>XmNaccelerators</td>
<td>XmCAccelerators</td>
<td>XtAccelerators</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNbackground</td>
<td>XmCBackground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNborderColor</td>
<td>XmCBorderColor</td>
<td>Pixel</td>
<td>XtDefaultForeground</td>
<td>CSG
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
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
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
<td>XmNdepth</td>
<td>XmCDepth</td>
<td>int</td>
<td>dynamic</td>
<td>CG
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
<td>XmNheight</td>
<td>XmCHeight</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNmappedWhenManaged</td>
<td>XmCMappedWhenManaged</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
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
<td>XmNsensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
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
<td>XmNwidth</td>
<td>XmCWidth</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNy</td>
<td>XmCPosition</td>
<td>Position</td>
<td>0</td>
<td>CSG
</td>
</tr>
</table>
<h3>Callback</h3>
<p>A pointer to the following structure is passed to each callback: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent <i>* event</i>;
 Widget <i>widget</i>;
 Boolean <i>doit</i>;
 int <i>position</i>;
 XmString <i>value</i>;
 Boolean <i>crossed_boundary</i>;
} XmSpinBoxCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked. Reasons may be the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmCR_OK</code></p>
<dd>Spinning has stopped because the SpinBox arrow has been disarmed. <code>XmCR_OK</code> is either the last or only call.</p>
<dt><code>XmCR_SPIN_NEXT</code></p>
<dd>The increment arrow has been armed and position is increasing. Further callbacks will come. For a numeric type child, the values displayed are approaching the maximum. For a string SpinBox, the values displayed are approaching the last entry in the array of <code>XmString</code> s.</p>
<dt><code>XmCR_SPIN_PRIOR</code></p>
<dd>The decrement arrow has been armed and position is decreasing. Further callbacks will come. For a numeric type child, the values displayed are approaching the minimum. For a string type child, the values displayed are approaching the first entry in the array of <code>XmString</code>s.</p>
<dt><code>XmCR_SPIN_FIRST</code></p>
<dd>The begin data (<code>&lt;osfBeginData&gt;</code>) key sequence has been pressed. The SpinBox is at its first position, displaying the lowest value or the first entry in the array of <code>XmString</code>s.</p>
<dt><code>XmCR_SPIN_LAST</code></p>
<dd>The end data (<code>&lt;osfEndData&gt;</code>) key sequence has been pressed. The SpinBox is at its last position, displaying the highest value or the last entry in the array of <code>XmString</code>s.</dl>
</dl>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered this callback.</p>
<dt><i>widget</i></p>
<dd>Specifies the child widget affected by this callback.</p>
<dt><i>doit</i></p>
<dd>When the callback is <code>XmNmodifyVerifyCallback</code>, <i>doit</i> indicates whether or not an action will be performed before the SpinBox position changes. If the callback leaves <i>doit</i> set to True (the default), the spinning action is performed. If the callback sets <i>doit</i> to False, the spinning action is not performed. When the callback is <code>XmNvalueChangedCallback</code>, <i>doit</i> is ignored.</p>
<dt><i>position</i></p>
<dd>Specifies the next value of the SpinBox position (same as <code>XmNposition</code>). This is an output field for the <code>XmNmodifyVerifyCallback</code>, which may change the next position as dictated by the needs of an application.</p>
<dt><i>value</i></p>
<dd>Specifies the new <code>XmString</code> value in the text child widget. The user program must copy this string if it is to be used outside the callback routine.</p>
<dt><i>crossed_boundary</i></p>
<dd>Specifies whether or not the SpinBox has crossed the upper or lower boundary (the last or first compound string, or the maximum or minimum value). The <i>crossed_boundary</i> value is True if the SpinBox has just crossed a boundary, and False if it has not.</dl>
<h3>Translations</h3>
<p>The <code>XmSpinBox</code> translations are as follows: </p>
<p> The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>&lt;Btn1Down&gt;</code>:</p>
<dd>SpinBArm()</p>
<dt><code>&lt;Btn1Up&gt;</code>:</p>
<dd>SpinBDisarm()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code> :</p>
<dd>SpinBPrior()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code> :</p>
<dd>SpinBNext()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code> :</p>
<dd>SpinBLeft()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code> :</p>
<dd>SpinBRight()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfBeginData&gt;</code> :</p>
<dd>SpinBFirst()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfEndData&gt;</code> :</p>
<dd>SpinBLast()</dl>
<h3>Accelerators</h3>
<p>The <code>XmNaccelerators</code> resource of a SpinBox are added to each traversable text child. The default <code>XmNaccelerators</code> are defined in the following list. The bindings for <code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code> and <code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code> cannot be changed.</p>
<dl COMPACT>
<dt><code>&lt;Key&gt;</code> <code>&lt;osfUp&gt;</code>:</p>
<dd>SpinBPrior()</p>
<dt><code>&lt;Key&gt;</code> <code>&lt;osfDown&gt;</code>:</p>
<dd>SpinBNext()</p>
<dt><code>&lt;KeyUp&gt;</code> <code>&lt;osfUp&gt;</code>:</p>
<dd>SpinBDisarm()</p>
<dt><code>&lt;KeyUp&gt;</code> <code>&lt;osfDown&gt;</code>:</p>
<dd>SpinBDisarm()</p>
<dt><code>&lt;Key&gt;</code> <code>&lt;osfLeft&gt;</code>:</p>
<dd>SpinBLeft()</p>
<dt><code>&lt;Key&gt;</code> <code>&lt;osfRight&gt;</code>:</p>
<dd>SpinBRight()</p>
<dt><code>&lt;KeyUp&gt;</code> <code>&lt;osfLeft&gt;</code>:</p>
<dd>SpinBDisarm()</p>
<dt><code>&lt;KeyUp&gt;</code> <code>&lt;osfRight&gt;</code>:</p>
<dd>SpinBDisarm()</p>
<dt><code>&lt;Key&gt;</code> <code>&lt;osfBeginData&gt;</code>:</p>
<dd>SpinBFirst()</p>
<dt><code>&lt;Key&gt;</code> <code>&lt;osfEndData&gt;</code>:</p>
<dd>SpinBLast()</dl>
<h3>Action Routines</h3>
<p>The <code>XmSpinBox</code> action routines are as follows:</p>
<dl COMPACT>
<dt>SpinBArm():</p>
<dd>Visually arms the SpinBox by drawing the armed arrow so that it appears to be depressed. This action is initiated when the user presses <code>&lt;Btn1&gt;</code> while the pointer is within the boundaries of either the increment or decrement arrow. The arrow remains visually armed as long as <code>&lt;Btn1&gt;</code> remains depressed.</p>
<dd>If the time period specified by <code>XmNrepeatDelay</code> is not greater than zero milliseconds, nothing else happens while <code>&lt;Btn1&gt;</code> remains depressed.</p>
<dd>If the time period specified by <code>XmNrepeatDelay</code> is greater than zero milliseconds, and the arrow is disarmed before the time period specified by <code>XmNinitialDelay</code> has elapsed, nothing else happens in this action.</p>
<dd>If the time period specified by <code>XmNrepeatDelay</code> is greater than zero milliseconds, and the arrow is still armed after the time period specified by <code>XmNinitialDelay</code> has elapsed, the following occurs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure, <code>XmSpinBoxCallbackStruct</code>, is set to <code>XmCR_SPIN_NEXT</code> if the increment arrow is armed, or to <code>XmCR_SPIN_PRIOR</code> if the decrement arrow is armed.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the next position.</p>
<dt> &bull;</p>
<dd>The <i>doit</i> member is set to True.</p>
<dt> &bull;</p>
<dd><code>XmNmodifyVerifyCallback</code>, if it exists, is invoked. The application may change the value of <i>position</i> and <i>doit</i>. If the application sets <i>doit</i> to False, nothing else happens until the <code>XmNrepeatDelay</code> period has elapsed, or until <code>&lt;Btn1&gt;</code> is released.</dl>
</dl>
<dd>If <i>doit</i> remains set to True, the following occurs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The value of <code>XmNposition</code> is changed to the value of <i>position</i> in the SpinBox callback structure.</p>
<dt> &bull;</p>
<dd>The text corresponding to the new position is displayed in the traversable text child that currently has focus.</p>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure is set to <code>XmCR_SPIN_NEXT</code> if the increment arrow is armed, or <code>XmCR_SPIN_PRIOR</code> if the decrement arrow is armed.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the current (new) value of <code>XmNposition</code>.</p>
<dt> &bull;</p>
<dd><code>XmNvalueChangedCallback</code>, if it exists, is called. SpinBox ignores any changes to <i>position</i> or <i>doit</i> members made by <code>XmNvalueChangedCallback</code>.</dl>
</dl>
<dd>These events are repeated each time the <code>XmNrepeatDelay</code> period elapses and the arrow remains armed.</p>
<dt>SpinBDisarm():</p>
<dd>Visually disarms the SpinBox by drawing the previously armed arrow so that it no longer appears to be depressed.</p>
<dd>If the time period specified by <code>XmNrepeatDelay</code> is not greater than zero milliseconds, or the time period specified by <code>XmNinitialDelay</code> has not elapsed, the following then occurs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure, <code>XmSpinBoxCallbackStruct</code>, is set to <code>XmCR_SPIN_NEXT</code> if the increment arrow is armed, or to <code>XmCR_SPIN_PRIOR</code> if the decrement arrow is armed.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the next position.</p>
<dt> &bull;</p>
<dd>The <i>doit</i> member is set to True.</p>
<dt> &bull;</p>
<dd>The <code>XmNmodifyVerifyCallback</code>, if there is one, is invoked. The application may change the value of <i>position</i> and <i>doit</i>. If the application sets <i>doit</i> to False, nothing else happens until the <code>XmNrepeatDelay</code> period has elapsed, or until <code>&lt;Btn1&gt;</code> is released.</dl>
</dl>
<dd>If <i>doit</i> remains set to True, the following occurs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The value of <code>XmNposition</code> is changed to the value of <i>position</i> in the SpinBox callback structure.</p>
<dt> &bull;</p>
<dd>The text corresponding to the new position is displayed in the traversable text child that currently has focus.</p>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure is set to <code>XmCR_SPIN_NEXT</code> if the increment arrow is armed, or <code>XmCR_SPIN_PRIOR</code> if the decrement arrow is armed.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the current (new) value of <code>XmNposition</code>.</p>
<dt> &bull;</p>
<dd><code>XmNvalueChangedCallback</code>, if it exists, is called. SpinBox ignores any changes to <i>position</i> or <i>doit</i> members made by an <code>XmNvalueChangedCallback</code>.</dl>
</dl>
<dd>If an <code>XmNvalueChangedCallback</code> procedure is issued after the button has been armed, regardless of the value of <code>XmNrepeatDelay</code> or whether the <code>XmNinitialDelay</code> has expired:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure is set to <code>XmCR_OK</code>.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the current value of <code>XmNposition</code>.</p>
<dt> &bull;</p>
<dd><code>XmNvalueChangedCallback</code>, if it exists, is called.</dl>
</dl>
<dt>SpinBFirst():</p>
<dd>The following occurs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure, <code>XmSpinBoxCallbackStruct</code>, is set to <code>XmCR_SPIN_FIRST</code>.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the first (0) position.</p>
<dt> &bull;</p>
<dd>The <i>doit</i> member is set to True.</p>
<dt> &bull;</p>
<dd><code>XmNmodifyVerifyCallback</code>, if it exists, is invoked. The application may change the value of <i>position</i> and <i>doit</i>. If the application sets <i>doit</i> to False, nothing else happens until the <code>XmNrepeatDelay</code> period has elapsed, or until <code>&lt;Btn1&gt;</code> is released.</dl>
</dl>
<dd>If <i>doit</i> remains set to True, the following occurs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The value of <code>XmNposition</code> is changed to the value of <i>position</i> in the SpinBox callback structure.</p>
<dt> &bull;</p>
<dd>The text corresponding to the new position is displayed in the traversable text child that currently has focus.</p>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure is set to <code>XmCR_SPIN_FIRST</code>.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the current (new) value of <code>XmNposition</code>.</p>
<dt> &bull;</p>
<dd><code>XmNvalueChangedCallback</code>, if it exists, is called.</p>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure is set to <code>XmCR_OK</code>.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the current (new) <code>XmNposition</code> value.</p>
<dt> &bull;</p>
<dd>The <code>XmNvalueChangedCallback</code> is called again. SpinBox ignores any changes to <i>position</i> or <i>doit</i> members made by <code>XmNvalueChangedCallback</code>.</dl>
</dl>
<dt>SpinBLast():</p>
<dd>The following occurs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure, <code>XmSpinBoxCallbackStruct</code>, is set to <code>XmCR_SPIN_LAST</code>.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the last position.</p>
<dt> &bull;</p>
<dd>The <i>doit</i> member is set to True.</p>
<dt> &bull;</p>
<dd><code>XmNmodifyVerifyCallback</code>, if it exists, is invoked. The application may change the value of <i>position</i> and <i>doit</i>. If the application sets <i>doit</i> to False, nothing else happens until the <code>XmNrepeatDelay</code> period has elapsed, or until <code>&lt;Btn1&gt;</code> is released.</dl>
</dl>
<dd>If <i>doit</i> remains set to True, the following occurs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The value of <code>XmNposition</code> is changed to the value of <i>position</i> in the SpinBox callback structure.</p>
<dt> &bull;</p>
<dd>The text corresponding to the new position is displayed in the traversable text child that currently has focus.</p>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure is set to <code>XmCR_SPIN_LAST</code>.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the current (new) value <code>XmNposition</code>.</p>
<dt> &bull;</p>
<dd><code>XmNvalueChangedCallback</code>, if it exists, is called.</p>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure is set to <code>XmCR_OK</code>.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the current (new) of <code>XmNposition</code>.</p>
<dt> &bull;</p>
<dd><code>XmNvalueChangedCallback</code> is called again. SpinBox ignores any changes to the <i>position</i> or <i>doit</i> members made by <code>XmNvalueChangedCallback</code>.</dl>
</dl>
<dt>SpinBLeft():</p>
<dd>If the VendorShell resource <code>XmNlayoutDirection</code> is left-to-right, the <code>SpinBPrior</code> action is invoked. Otherwise, the <code>SpinBNext</code> action is invoked.</p>
<dt>SpinBNext():</p>
<dd>Visually arms the SpinBox by drawing the increment arrow so that it appears to be depressed. The following occurs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure, <code>XmSpinBoxCallbackStruct</code>, is set to <code>XmCR_SPIN_NEXT</code>.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the next position.</p>
<dt> &bull;</p>
<dd>The <i>doit</i> member is set to True.</p>
<dt> &bull;</p>
<dd><code>XmNmodifyVerifyCallback</code>, if it exists, is invoked. The application may change the value of <i>position</i> and <i>doit</i>. If the application sets <i>doit</i> to False, nothing else happens until the <code>XmNrepeatDelay</code> period has elapsed, or until <code>&lt;Btn1&gt;</code> is released.</dl>
</dl>
<dd>If <i>doit</i> remains set to True, the following occurs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The value of <code>XmNposition</code> is changed to the value of <i>position</i> in the SpinBox callback structure.</p>
<dt> &bull;</p>
<dd>The text corresponding to the new position is displayed in the traversable text child that currently has focus.</p>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure is set to <code>XmCR_SPIN_NEXT</code>.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the current (new) value of <code>XmNposition</code>.</p>
<dt> &bull;</p>
<dd><code>XmNvalueChangedCallback</code>, if it exists, is called.</p>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure is set to <code>XmCR_OK</code>.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the current (new) <code>XmNposition</code>.</p>
<dt> &bull;</p>
<dd>The <code>XmNvalueChangedCallback</code> is called again. SpinBox ignores any changes to <i>position</i> or <i>doit</i> members made by <code>XmNvalueChangedCallback</code>.</dl>
</dl>
<dt>SpinBPrior():</p>
<dd>Visually arms the SpinBox by drawing the decrement arrow so that it appears to be depressed. The following occurs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure, <code>XmSpinBoxCallbackStruct</code>, is set to <code>XmCR_SPIN_PRIOR</code>.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the next position.</p>
<dt> &bull;</p>
<dd>The <i>doit</i> member is set to True.</p>
<dt> &bull;</p>
<dd><code>XmNmodifyVerifyCallback</code>, if it exists, is invoked. The application may change the value of <i>position</i> and <i>doit</i>. If the application sets <i>doit</i> to False, nothing else happens until the <code>XmNrepeatDelay</code> period has elapsed, or until <code>&lt;Btn1&gt;</code> is released.</dl>
</dl>
<dd>If <i>doit</i> remains set to True, the following occurs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The value of <code>XmNposition</code> is changed to the value of <i>position</i> in the SpinBox callback structure.</p>
<dt> &bull;</p>
<dd>The text corresponding to the new position is displayed in the traversable text child that currently has focus.</p>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure is set to <code>XmCR_SPIN_PRIOR</code>.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the current (new) value of <code>XmNposition</code>.</p>
<dt> &bull;</p>
<dd><code>XmNvalueChangedCallback</code>, if it exists, is called.</p>
<dt> &bull;</p>
<dd>The <i>reason</i> member of the SpinBox callback structure is set to <code>XmCR_OK</code>.</p>
<dt> &bull;</p>
<dd>The <i>position</i> member is set to the current (new) value of <code>XmNposition</code>.</p>
<dt> &bull;</p>
<dd><code>XmNvalueChangedCallback</code> is called again. SpinBox ignores any changes to <i>position</i> or <i>doit</i> members made by <code>XmNvalueChangedCallback</code>.</dl>
</dl>
<dt>SpinBRight():</p>
<dd>If the VendorShell resource <code>XmNlayoutDirection</code> is left-to-right, the <code>SpinBNext</code> action is invoked. Otherwise, the <code>SpinBPrior</code> action is invoked.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatespinbox/">XmCreateSpinBox</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatespinbox/">XmVaCreateSpinBox</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedspinbox/">XmVaCreateManagedSpinBox</a></code>(3).</p>
