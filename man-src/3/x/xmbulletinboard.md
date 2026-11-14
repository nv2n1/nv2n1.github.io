---
title: "xmbulletinboard(3)"
name: "xmbulletinboard"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmbulletinboard/"
description: "XmBulletinBoard — The BulletinBoard widget class"
---

<p><code>XmBulletinBoard</code> &#8212; The BulletinBoard widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/BulletinB.h&gt;</pre>
<h2>Description</h2>
<p>BulletinBoard is a composite widget that provides simple geometry management for child widgets. It does not force positioning on its children, but can be set to reject geometry requests that result in overlapping children. BulletinBoard is the base widget for most dialog widgets and is also used as a general container widget. </p>
<p> Modal and modeless dialogs are implemented as collections of widgets that include a DialogShell, a BulletinBoard (or subclass) child of the shell, and various dialog components (buttons, labels, and so on) that are children of BulletinBoard. BulletinBoard defines callbacks useful for dialogs (focus, map, unmap), which are available for application use. If its parent is a DialogShell, BulletinBoard passes title and input mode (based on dialog style) information to the parent, which is responsible for appropriate communication with the window manager. </p>
<p> The default value for <code>XmNinitialFocus</code> is the value of <code>XmNdefaultButton</code>. </p>
<p> BulletinBoard uses the <code>XmQTtakesDefault</code> trait, and holds the <code>XmQTdialogShellSavvy</code> and <code>XmQTspecifyRenderTable</code> traits.</p>
<h3>Classes</h3>
<p>BulletinBoard inherits behavior, resources, and traits from the <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, and <code>XmManager</code> classes. </p>
<p> The class pointer is <code>xmBulletinBoardWidgetClass</code>. </p>
<p> The class name is <code>XmBulletinBoard</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
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
<td>True</td>
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
<td>NULL</td>
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
<td>NULL</td>
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
<dl COMPACT>
<dt><code>XmNallowOverlap</code></p>
<dd>Controls the policy for overlapping child widgets. If this resource is True, BulletinBoard allows geometry requests that result in overlapping children.</p>
<dt><code>XmNautoUnmanage</code></p>
<dd>Controls whether or not BulletinBoard is automatically unmanaged after a button is activated. If this resource is True on initialization and if the BulletinBoard&#8217;s parent is a DialogShell, BulletinBoard adds a callback to button children (PushButtons, PushButtonGadgets, and DrawnButtons) that unmanages the BulletinBoard when a button is activated. If this resource is False on initialization or if the BulletinBoard&#8217;s parent is not a DialogShell, the BulletinBoard is not automatically unmanaged. For BulletinBoard subclasses with Apply or Help buttons, activating those buttons does not automatically unmanage the BulletinBoard.</p>
<dt><code>XmNbuttonFontList</code></p>
<dd>Specifies the font list used for button descendants. See the <code>XmNbuttonRenderTable</code> resource.</p>
<dt><code>XmNbuttonRenderTable</code></p>
<dd>Specifies the render table used for BulletinBoard&#8217;s button descendants. If this value is NULL at initialization, the parent hierarchy of the widget is searched for an ancestor that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, the render table is initialized to the <code>XmBUTTON_RENDER_TABLE</code> value of the ancestor widget. If no such ancestor is found, the default is implementation dependent. Refer to <code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3) for more information on the creation and structure of a render table.</p>
<dt><code>XmNcancelButton</code></p>
<dd>Specifies the widget ID of the <code>Cancel</code> button. BulletinBoard&#8217;s subclasses, which define a <code>Cancel</code> button, set this resource. BulletinBoard does not directly provide any behavior for that button.</p>
<dt><code>XmNdefaultButton</code></p>
<dd>Specifies the widget ID of the default button. Some BulletinBoard subclasses, which define a default button, set this resource. BulletinBoard defines translations and installs accelerators that activate that button when <code>KActivate</code> is pressed and the keyboard focus is not in another button.</p>
<dt><code>XmNdefaultPosition</code></p>
<dd>Controls the positioning of a DialogShell managing a BulletinBoard. If the BulletinBoard is not being managed by a DialogShell, then this resource has no effect. If <code>XmNdefaultPosition</code> is True, the DialogShell will center itself at the center of its own parent. For example, if the parent of the DialogShell is an ApplicationShell, then the center of the DialogShell will be at the same coordinates as the center of the ApplicationShell. If the DialogShell becomes unmapped (but stays managed) and then remapped, this resource has no influence on the DialogShell&#8217;s position. If this resource is False, the DialogShell does not automatically center itself.</p>
<dt><code>XmNdialogStyle</code></p>
<dd>Indicates the dialog style associated with the BulletinBoard. If the parent of the BulletinBoard is a DialogShell, the parent&#8217;s <code>XmNmwmInputMode</code> is set according to the value of this resource. This resource can be set only if the BulletinBoard is unmanaged. Possible values for this resource include the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmDIALOG_SYSTEM_MODAL</code></p>
<dd>Used for dialogs that must be responded to before any other interaction in any application.</p>
<dt><code>XmDIALOG_PRIMARY_APPLICATION_MODAL</code></p>
<dd>Used for dialogs that must be responded to before some other interactions in ancestors of the widget.</p>
<dt><code>XmDIALOG_APPLICATION_MODAL</code></p>
<dd>Used for dialogs that must be responded to before some other interactions in ancestors of the widget. This value is the same as <code>XmDIALOG_PRIMARY_APPLICATION_MODAL</code>, and remains for compatibility.</p>
<dt><code>XmDIALOG_FULL_APPLICATION_MODAL</code></p>
<dd>Used for dialogs that must be responded to before some other interactions in the same application.</p>
<dt><code>XmDIALOG_MODELESS</code></p>
<dd>Used for dialogs that do not interrupt interaction of any application. This is the default when the parent of the BulletinBoard is a DialogShell.</p>
<dt><code>XmDIALOG_WORK_AREA</code></p>
<dd>Used for BulletinBoard widgets whose parents are not DialogShells. <code>XmNdialogStyle</code> is forced to have this value when the parent of the BulletinBoard is not a DialogShell.</dl>
</dl>
<dd>Posting a modal dialog in response to a button down or key down event (via translation actions or callbacks) can cause the corresponding button up or key up event to be lost. For example, posting a modal dialog from an <code>XmNincrementCallback</code> of <code>XmScrollBar</code> will cause the loss of the button up event, causing the <code>XmScrollBar</code> to auto-increment indefinitely.</p>
<dt><code>XmNdialogTitle</code></p>
<dd>Specifies the dialog title. If this resource is not NULL, and the parent of the BulletinBoard is a subclass of WMShell, BulletinBoard sets the <code>XmNtitle</code> and <code>XmNtitleEncoding</code> of its parent. If the only character set in <code>XmNdialogTitle</code> is ISO8859-1, <code>XmNtitle</code> is set to the string of the title, and <code>XmNtitleEncoding</code> is set to <code>STRING</code>. If <code>XmNdialogTitle</code> contains character sets other than ISO8859-1, <code>XmNtitle</code> is set to the string of the title converted to a compound text string, and <code>XmNtitleEncoding</code> is set to <code>COMPOUND_TEXT</code>. The direction of the title is based on the <code>XmNlayoutDirection</code> resource of the widget.</p>
<dt><code>XmNfocusCallback</code></p>
<dd>Specifies the list of callbacks that is called when the BulletinBoard widget or one of its descendants accepts the input focus. The callback reason is <code>XmCR_FOCUS</code>.</p>
<dt><code>XmNlabelFontList</code></p>
<dd>Specifies the font list used for label descendants. See the <code>XmNlabelRenderTable</code> resource.</p>
<dt><code>XmNlabelRenderTable</code></p>
<dd>Specifies the render table used for BulletinBoard&#8217;s label descendants. If this value is NULL at initialization, the parent hierarchy of the widget is searched for an ancestor that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, the render table is initialized to the <code>XmLABEL_RENDER_TABLE</code> value of the ancestor widget. If no such ancestor is found, the default is implementation dependent. Refer to <code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3) for more information on the creation and structure of a render table.</p>
<dt><code>XmNmapCallback</code></p>
<dd>Specifies the list of callbacks that is called only when the parent of the BulletinBoard is a DialogShell. In this case, this callback list is invoked when the BulletinBoard widget is mapped. The callback reason is <code>XmCR_MAP</code>. DialogShells are usually mapped when the DialogShell is managed.</p>
<dt><code>XmNmarginHeight</code></p>
<dd>Specifies the minimum spacing in pixels between the top or bottom edge of BulletinBoard and any child widget.</p>
<dt><code>XmNmarginWidth</code></p>
<dd>Specifies the minimum spacing in pixels between the left or right edge of BulletinBoard and any child widget.</p>
<dt><code>XmNnoResize</code></p>
<dd>Controls whether or not resize controls are included in the window manager frame around the BulletinBoard&#8217;s parent. If this resource is set to True, <code>mwm</code> does not include resize controls in the window manager frame containing the parent of the BulletinBoard if the parent is a subclass of VendorShell. If this resource is set to False, the window manager frame does include resize controls. Other controls provided by <code>mwm</code> can be included or excluded through the <code>mwm</code> resources provided by VendorShell.</p>
<dt><code>XmNresizePolicy</code></p>
<dd>Controls the policy for resizing BulletinBoard widgets. Possible values include</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmRESIZE_NONE</code></p>
<dd>Fixed size</p>
<dt><code>XmRESIZE_ANY</code></p>
<dd>Shrink or grow as needed</p>
<dt><code>XmRESIZE_GROW</code></p>
<dd>Grow only</dl>
</dl>
<dt><code>XmNshadowType</code></p>
<dd>Describes the shadow drawing style for BulletinBoard. This resource can have the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmSHADOW_IN</code></p>
<dd>Draws the BulletinBoard shadow so that it appears inset. This means that the bottom shadow visuals and top shadow visuals are reversed.</p>
<dt><code>XmSHADOW_OUT</code></p>
<dd>Draws the BulletinBoard shadow so that it appears outset.</p>
<dt><code>XmSHADOW_ETCHED_IN</code></p>
<dd>Draws the BulletinBoard shadow using a double line giving the effect of a line etched into the window, similar to the Separator widget.</p>
<dt><code>XmSHADOW_ETCHED_OUT</code></p>
<dd>Draws the BulletinBoard shadow using a double line giving the effect of a line coming out of the window, similar to the Separator widget.</dl>
</dl>
<dt><code>XmNtextFontList</code></p>
<dd>Specifies the font list used for text descendants. See the <code>XmNtextRenderTable</code> resource.</p>
<dt><code>XmNtextRenderTable</code></p>
<dd>Specifies the render table used for BulletinBoard&#8217;s text descendants. If this value is NULL at initialization, the parent hierarchy of the widget is searched for an ancestor that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, the render table is initialized to the <code>XmTEXT_RENDER_TABLE</code> value of the ancestor widget. If no such ancestor is found, the default is implementation dependent. Refer to <code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3) for more information on the creation and structure of a render table.</p>
<dt><code>XmNtextTranslations</code></p>
<dd>It adds translations to any Text widget or Text widget subclass that is added as a child of BulletinBoard.</p>
<dt><code>XmNunmapCallback</code></p>
<dd>Specifies the list of callbacks that is called only when the parent of the BulletinBoard is a DialogShell. In this case, this callback list is invoked when the BulletinBoard widget is unmapped. The callback reason is <code>XmCR_UNMAP</code>. DialogShells are usually unmapped when the DialogShell is unmanaged.</dl>
<h3>Inherited Resources</h3>
<p>BulletinBoard inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
} XmAnyCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback</dl>
<h3>Translations</h3>
<p><code>XmBulletinBoard</code> includes the translations from <code>XmManager</code>.</p>
<h3>Additional Behavior</h3>
<p>The <code>XmBulletinBoard</code> widget has the following additional behavior:</p>
<dl COMPACT>
<dt><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>Calls the activate callbacks for the cancel button if it is sensitive. If no cancel button exists and if the parent of the BulletinBoard is a manager, passes the event to the parent.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>Calls the activate callbacks for the button with the keyboard focus. If no button has the keyboard focus, calls the activate callbacks for the default button if it is sensitive. In a List widget or single-line Text widget, the List or Text action associated with <code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code> is called before the BulletinBoard actions associated with <code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>.</p>
<dd>In a multiline Text widget, any <code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code> event except <code>&lt;Key&gt;</code><code>&lt;Enter&gt;</code> calls the Text action associated with <code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>, then the BulletinBoard actions associated with <code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>. If no button has the focus, no default button exists, and the parent of the BulletinBoard is a manager, passes the event to the parent.</p>
<dt><code>&lt;FocusIn&gt;</code>:</p>
<dd>Calls the callbacks for <code>XmNfocusCallback</code>. When the focus policy is <code>XmPOINTER</code>, the callbacks are called when the pointer enters the window. When the focus policy is <code>XmEXPLICIT</code>, the callbacks are called when the user traverses to the widget.</p>
<dt><code>&lt;Map&gt;</code>:</p>
<dd>Calls the callbacks for <code>XmNmapCallback</code>.</p>
<dt><code>&lt;Unmap&gt;</code>:</p>
<dd>Calls the callbacks for <code>XmNunmapCallback</code>.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatebulletinboard/">XmCreateBulletinBoard</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatebulletinboarddialog/">XmCreateBulletinBoardDialog</a></code>(3), <code><a href="/docs/linux/man/3-xmdialogshell/">XmDialogShell</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatebulletinboard/">XmVaCreateBulletinBoard</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedbulletinboard/">XmVaCreateManagedBulletinBoard</a></code>(3).</p>
