---
title: "xmsimplespinbox(3)"
name: "xmsimplespinbox"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmsimplespinbox/"
description: "XmSimpleSpinBox — a simple SpinBox widget class"
---

<p><code>XmSimpleSpinBox</code> &#8212; a simple SpinBox widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/SSpinB.h&gt;</pre>
<h2>Description</h2>
<p>The XmSimpleSpinBox widget is a user interface control to increment and decrement an arbitrary TextField. For example, it can be used to cycle through the months of the year or days of the month. </p>
<p> Widget subclassing is not supported for the XmSimpleSpinBox widget class.</p>
<h3>Classes</h3>
<p>The XmSimpleSpinBox widget inherits behavior and resources from the <code>Core</code>, <code>Composite</code> and <code>XmManager</code> classes. </p>
<p> The class pointer is <code>XmSimpleSpinBoxWidgetClass</code>. </p>
<p> The class name is <code>XmSimpleSpinBoxWidget</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the application to specify data. The application can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, the application must remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, the application must remove the <code>Xm</code> prefix and use the remaining letters (in either lower case or upper case, but including any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table>
<tr VALIGN=top>
<td><code>XmSimpleSpinBox Resource</code></td>
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
<td><code>XmNarrowLayout</code></td>
<td><code>XmCArrowLayout</code></td>
<td><code>unsigned char</code></td>
<td>XmARROWS_END</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNarrowSensitivity</code></td>
<td><code>XmCArrowSensitivity</code></td>
<td><code>unsigned char</code></td>
<td>XmARROWS-_SENSITIVE</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNcolumns</code></td>
<td><code>XmCColumn</code></td>
<td><code>short</code></td>
<td>20</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNdecimalPoints</code></td>
<td><code>XmCDecimalPoints</code></td>
<td><code>short</code></td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNeditable</code></td>
<td><code>XmCEditable</code></td>
<td><code>Boolean</code></td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNincrementValue</code></td>
<td><code>XmCIncrementValue</code></td>
<td><code>int</code></td>
<td>1</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNinitialDelay</code></td>
<td><code>XmCInitialDelay</code></td>
<td><code>unsigned int</code></td>
<td>250</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNmaximumValue</code></td>
<td><code>XmCMaximumValue</code></td>
<td><code>int</code></td>
<td>10</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNminimumValue</code></td>
<td><code>XmCMinimumValue</code></td>
<td><code>int</code></td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNmodifyVerifyCallback</code></td>
<td><code>XmCCallback</code></td>
<td><code>XtCallbackList</code></td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNnumValues</code></td>
<td><code>XmCNumValues</code></td>
<td><code>int</code></td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNposition</code></td>
<td><code>XmCPosition</code></td>
<td><code>int</code></td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNrepeatDelay</code></td>
<td><code>XmCRepeatDelay</code></td>
<td><code>unsigned int</code></td>
<td>200</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNspinBoxChildType</code></td>
<td><code>XmCSpinBoxChildType</code></td>
<td><code>unsigned char</code></td>
<td>XmSTRING</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNtextField</code></td>
<td><code>XmCTextField</code></td>
<td><code>Widget</code></td>
<td>dynamic</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNvalueChangedCallback</code></td>
<td><code>XmCCallback</code></td>
<td><code>XtCallbackList</code></td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNvalues</code></td>
<td><code>XmCValues</code></td>
<td><code>XmStringTable</code></td>
<td>NULL</td>
<td>CSG
</td>
</tr>
</table>
<dl COMPACT>
<dt><code>XmNarrowLayout</code></p>
<dd>Specifies the style and position of the SpinBox arrows. The following values are supported:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>XmARROWS_FLAT_BEGINNING</p>
<dd>The arrows are placed side by side to the right of the TextField.</p>
<dt>XmARROWS_FLAT_END</p>
<dd>The arrows are placed side by side to the left of the TextField.</p>
<dt>XmARROWS_SPLIT</p>
<dd>The down arrow is on the left and the up arrow is on the right of the TextField.</p>
<dt>XmARROWS_BEGINNING</p>
<dd>The arrows are stacked and placed on the left of the TextField.</p>
<dt>XmARROWS_END</p>
<dd>The arrows are stacked and placed on the right of the TextField.</dl>
</dl>
<dt><code>XmNarrowSensitivity</code></p>
<dd>Specifies the sensitivity of the arrows in the XmSimpleSpinBox. The following values are supported:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>XmARROWS_SENSITIVE</p>
<dd>Both arrows are active to user selection.</p>
<dt>XmARROWS_DECREMENT_SENSITIVE</p>
<dd>The down arrow is active and the up arrow is inactive to user selection.</p>
<dt>XmARROWS_INCREMENT_SENSITIVE</p>
<dd>The up arrow is active and the down arrow is inactive to user selection.</p>
<dt>XmARROWS_INSENSITIVE</p>
<dd>Both arrows are inactive to user selection.</dl>
</dl>
<dt><code>XmNcolumns</code></p>
<dd>Specifies the number of columns of the text field.</p>
<dt><code>XmNdecimalPoints</code></p>
<dd>Specifies the position of the radix character within the numeric value when <code>XmNspinBoxChildType</code> is <code>XmNUMERIC</code>. This resource is used to allow for floating point values in the XmSimpleSpinBox widget.</p>
<dt><code>XmNeditable</code></p>
<dd>Specifies whether the text field can take input.</p>
<dd>When <code>XmNeditable</code> is used on a widget it sets the dropsite to <code>XmDROP_SITE_ACTIVE</code>.</p>
<dt><code>XmNincrementValue</code></p>
<dd>Specifies the amount to increment or decrement the <code>XmNposition</code> when the <code>XmNspinBoxChildType</code> is <code>XmNUMERIC</code>. When the Up action is activated, the <code>XmNincrementValue</code> is added to the <code>XmNposition</code> value; when the Down action is activated, the <code>XmNincrementValue</code> is subtracted from the <code>XmNposition</code> value. When <code>XmNspinBoxChildType</code> is <code>XmSTRING</code>, this resource is ignored.</p>
<dt><code>XmNinitialDelay</code></p>
<dd>Specifies the amount of time in milliseconds before the Arrow buttons will begin to spin continuously.</p>
<dt><code>XmNnumValues</code></p>
<dd>Specifies the number of items in the <code>XmNvalues</code> list when the <code>XmNspinBoxChildType</code> resource is <code>XmSTRING</code>. The value of this resource must be a positive integer. The <code>XmNnumValues</code> is maintained by the XmSimpleSpinBox widget when items are added or deleted from the <code>XmNvalues</code> list. When <code>XmNspinBoxChildType</code> is not <code>XmSTRING</code>, this resource is ignored.</p>
<dt><code>XmNvalues</code></p>
<dd>Supplies the list of strings to cycle through when the <code>XmNspinButtonChildType</code> resource is <code>XmSTRING</code>. When <code>XmNspinBoxChildType</code> is not <code>XmSTRING</code>, this resource is ignored.</p>
<dt><code>XmNmaximumValue</code></p>
<dd>Specifies the upper bound on the XmSimpleSpinBox&#8217;s range when <code>XmNspinBoxChildType</code> is <code>XmNUMERIC</code>.</p>
<dt><code>XmNminimumValue</code></p>
<dd>Specifies the lower bound on the XmSimpleSpinBox&#8217;s range when <code>XmNspinBoxChildType</code> is <code>XmNUMERIC</code>.</p>
<dt><code>XmNmodifyVerifyCallback</code></p>
<dd>Specifies the callback to be invoked just before the XmSimpleSpinBox position changes. The application can use this callback to implement new application-related logic (including setting new position spinning to, or canceling the impending action). For example, this callback can be used to stop the spinning just before wrapping at the upper and lower position boundaries. If the application sets the <i>doit</i> member of the <code>XmSimpleSpinBoxCallbackStruct</code> to False, nothing happens. Otherwise, the position changes. Reasons sent by the callback are <code>XmCR_SPIN_NEXT</code>, or <code>XmCR_SPIN_PRIOR</code>.</p>
<dt><code>XmNposition</code></p>
<dd>The <code>XmNposition</code> resource has a different value based on the <code>XmNspinBoxChildType</code> resource. When <code>XmNspinBoxChildType</code> is <code>XmSTRING</code>, the <code>XmNposition</code> is the index into the <code>XmNvalues</code> list for the current item. When the <code>XmNspinBoxChildType</code> resource is <code>XmNUMERIC</code>, the <code>XmNposition</code> is the integer value of the XmSimpleSpinBox that falls within the range of <code>XmNmaximumValue</code> and <code>XmNminimumValue</code>.</p>
<dt><code>XmNrepeatDelay</code></p>
<dd>Specifies the number of milliseconds between repeated calls to the <code>XmNvalueChangedCallback</code> while the user is spinning the XmSimpleSpinBox.</p>
<dt><code>XmNspinBoxChildType</code></p>
<dd>Specifies the style of the XmSimpleSpinBox. The following values are supported:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>XmSTRING</p>
<dd>The child is a string value that is specified through the <code>XmNvalues</code> resource and incremented and decremented by changing the <code>XmNposition</code> resource.</p>
<dt>XmNUMERIC</p>
<dd>The child is a numeric value that is specified through the <code>XmNposition</code> resource and incremented according to the <code>XmNincrementValue</code> resource.</dl>
</dl>
<dt><code>XmtextField</code></p>
<dd>Specifies the textfield widget.</p>
<dt><code>XmNvalueChangedCallback</code></p>
<dd>Specifies the callback to be invoked whenever the value of the <code>XmNposition</code> resource is changed through the use of the spinner arrows. The <code>XmNvalueChangedCallback</code> passes the <code>XmSimpleSpinBoxCallbackStruct</code> <i>call_data</i> structure.</dl>
<h3>Inherited Resources</h3>
<p>The XmSimpleSpinBox widget inherits behavior and resources from the following named superclasses. For a complete description of each resource, see the man page for that superclass. </p>
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
<td><code>XmNbottomShadowColor</code></td>
<td><code>XmCBottomShadowColor</code></td>
<td><code>Pixel</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNbottomShadowPixmap</code></td>
<td><code>XmCBottomShadowPixmap</code></td>
<td><code>Pixmap</code></td>
<td><code>XmUNSPECIFIED_PIXMAP</code></td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNforeground</code></td>
<td><code>XmCForeground</code></td>
<td><code>Pixel</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNhelpCallback</code></td>
<td><code>XmCCallback</code></td>
<td><code>XtCallbackList</code></td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNhighlightColor</code></td>
<td><code>XmCHighlightColor</code></td>
<td><code>Pixel</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNhighlightPixmap</code></td>
<td><code>XmCHighlightPixmap</code></td>
<td><code>Pixmap</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNinitialFocus</code></td>
<td><code>XmCInitialFocus</code></td>
<td><code>Widget</code></td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNnavigationType</code></td>
<td><code>XmCNavigationType</code></td>
<td><code>XmNavigationType</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNshadowThickness</code></td>
<td><code>XmCShadowThickness</code></td>
<td><code>Dimension</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNstringDirection</code></td>
<td><code>XmCStringDirection</code></td>
<td><code>XmStringDirection</code></td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNtopShadowColor</code></td>
<td><code>XmCTopShadowColor</code></td>
<td><code>Pixel</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNtopShadowPixmap</code></td>
<td><code>XmCTopShadowPixmap</code></td>
<td><code>Pixmap</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNtraversalOn</code></td>
<td><code>XmCTraversalOn</code></td>
<td><code>Boolean</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNunitType</code></td>
<td><code>XmCUnitType</code></td>
<td><code>unsigned char</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNuserData</code></td>
<td><code>XmCUserData</code></td>
<td><code>XtPointer</code></td>
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
<td><code>XmNchildren</code></td>
<td><code>XmCReadOnly</code></td>
<td><code>WidgetList</code></td>
<td>NULL</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNinsertPosition</code></td>
<td><code>XmCInsertPosition</code></td>
<td><code>XtOrderProc</code></td>
<td>default procedure</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNnumChildren</code></td>
<td><code>XmCReadOnly</code></td>
<td><code>Cardinal</code></td>
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
<td><code>XmNaccelerators</code></td>
<td><code>XmCAccelerators</code></td>
<td><code>XtAccelerators</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNancestorSensitive</code></td>
<td><code>XmCSensitive</code></td>
<td><code>Boolean</code></td>
<td>dynamic</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNbackground</code></td>
<td><code>XmCBackground</code></td>
<td><code>Pixel</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNbackgroundPixmap</code></td>
<td><code>XmCPixmap</code></td>
<td><code>Pixmap</code></td>
<td><code>XmUNSPECIFIED_PIXMAP</code></td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNborderColor</code></td>
<td><code>XmCBorderColor</code></td>
<td><code>Pixel</code></td>
<td>XtDefaultForeground</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNborderPixmap</code></td>
<td><code>XmCPixmap</code></td>
<td><code>Pixmap</code></td>
<td><code>XmUNSPECIFIED_PIXMAP</code></td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNborderWidth</code></td>
<td><code>XmCBorderWidth</code></td>
<td><code>Dimension</code></td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNcolormap</code></td>
<td><code>XmCColormap</code></td>
<td><code>Colormap</code></td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNdepth</code></td>
<td><code>XmCDepth</code></td>
<td><code>int</code></td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNdestroyCallback</code></td>
<td><code>XmCCallback</code></td>
<td><code>XtCallbackList</code></td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNheight</code></td>
<td><code>XmCHeight</code></td>
<td><code>Dimension</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNinitialResourcesPersistent</code></td>
<td><code>XmCInitialResourcesPersistent</code></td>
<td><code>Boolean</code></td>
<td>True</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNmappedWhenManaged</code></td>
<td><code>XmCMappedWhenManaged</code></td>
<td><code>Boolean</code></td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNscreen</code></td>
<td><code>XmCScreen</code></td>
<td><code>Screen *</code></td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNsensitive</code></td>
<td><code>XmCSensitive</code></td>
<td><code>Boolean</code></td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNtranslations</code></td>
<td><code>XmCTranslations</code></td>
<td><code>XtTranslations</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNwidth</code></td>
<td><code>XmCWidth</code></td>
<td><code>Dimension</code></td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNx</code></td>
<td><code>XmCPosition</code></td>
<td><code>Position</code></td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNy</code></td>
<td><code>XmCPosition</code></td>
<td><code>Position</code></td>
<td>0</td>
<td>CSG
</td>
</tr>
</table>
<h3>Callback Information</h3>
<p>A pointer to the following structure is passed to each XmSimpleSpinBox callback: </p>
<pre><tt>typedef struct {
 int </tt><i>reason</i>;
 XEvent *<i>event</i>;
 Widget <i>widget</i>;
 Boolean <i>doit</i>;
 int <i>position</i>;
 XmString <i>value</i>;
 Boolean <i>crossed_boundary</i>;
} XmSimpleSpinBoxCallbackStruct;</pre>
<p>The <i>reason</i> argument indicates why the callback was invoked. There are three possible reasons for this callback to be issued. The reason is <code>XmCR_OK</code> when this is the first call to the callback at the beginning of a spin or if it is a single activation of the spin arrows. If the XmSimpleSpinBox is in the process of being continuously spun, then the reason will be <code>XmCR_SPIN_NEXT</code> or <code>XmCR_SPIN_PRIOR</code>, depending on the arrow that is spinning. </p>
<p> The <i>event</i> argument points to the <code>XEvent</code> that triggered the callback. It can be <code>NULL</code> when the XmSimpleSpinBox is continuously spinning. </p>
<p> The <i>widget</i> argument is the widget identifier for the simple spin box widget that has been affected by this callback. </p>
<p> The <i>doit</i> argument is set only when the <i>call_data</i> comes from the <code>XmNmodifyVerifyCallback</code>. It indicates that the action that caused the callback to be called should be performed. The action is not performed if <i>doit</i> is set to False. </p>
<p> The <i>position</i> argument is the new value of the <code>XmNposition</code> resource as a result of the spin. </p>
<p> The <i>value</i> argument is the new <code>XmString</code> value displayed in the Text widget as a result of the spin. The application must copy this string if it is used beyond the scope of the <i>call_data</i> structure. </p>
<p> The <i>crossed_boundary</i> argument is True when the spinbox cycles. This is the case when a <code>XmNspinBoxChildType</code> of <code>XmSTRING</code> wraps from the first item to the last or the last item to the first. In the case of the <code>XmNspinBoxChildType</code> of <code>XmNUMERIC</code>, the boundary is crossed when the XmSimpleSpinBox cycles from the maximum value to the minimum or vice versa.</p>
<h2>Errors/Warnings</h2>
<p>The toolkit will display a warning if the application tries to set the value of the <code>XmNtextField</code> resource, which is read-only (marked G in the resource table).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmspinbox/">XmSpinBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimplespinbox/">XmCreateSimpleSpinBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatespinbox/">XmCreateSpinBox</a></code>(3), <code><a href="/docs/linux/man/3-xmsimplespinboxadditem/">XmSimpleSpinBoxAddItem</a></code>(3), <code><a href="/docs/linux/man/3-xmsimplespinboxdeletepos/">XmSimpleSpinBoxDeletePos</a></code>(3), <code><a href="/docs/linux/man/3-xmsimplespinboxsetitem/">XmSimpleSpinBoxSetItem</a></code>(3), <code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3), <code><a href="/docs/linux/man/3-xtgetvalues/">XtGetValues</a></code>(3), <code><a href="/docs/linux/man/3-xtsetvalues/">XtSetValues</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatesimplespinbox/">XmVaCreateSimpleSpinBox</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedsimplespinbox/">XmVaCreateManagedSimpleSpinBox</a></code>(3).</p>
