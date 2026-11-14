---
title: "vendorshell(3)"
name: "vendorshell"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vendorshell/"
description: "VendorShell — The VendorShell widget class"
---

<p><code>VendorShell</code> &#8212; The VendorShell widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
#include &lt;X11/Shell.h&gt;</pre>
<h2>Description</h2>
<p>VendorShell is a Motif widget class used as a supporting superclass for all shell classes that are visible to the window manager and that are not override redirect. It contains resources that describe the MWM-specific look and feel. It also manages the MWM-specific communication needed by all VendorShell subclasses. See the <code>mwm</code> reference page for more information. </p>
<p> It is also responsible for managing toolTips. All <code>XmPrimitive</code> and <code>XmGadget</code> subclasses have an <code>XmNtoolTipString</code> resource. If <code>XmNtoolTipEnable</code> is True, and the pointer enters a Primitive or Gadget that has traversal enabled, and the XmNtoolTipString is not NULL, the <code>XmNtoolTipString</code> will be displayed according to the VendorShell resources for controlling toolTips. VendorShell displays the XmNtooTipString in an XmLabel that is a child of a transientShell. The name of the transientShell is TipShell, and the name of the XmLabel is TipLabel. The appearance of the tip can be controlled by specifing resources on these widgets. </p>
<p> If an application uses the <code>XmNmwmDecorations</code>, <code>XmNmwmFunctions</code>, or <code>XmNmwmInputMode</code> resource, it should include the file <code>Xm/MwmUtil.h</code>. </p>
<p> Setting <code>XmNheight</code>, <code>XmNwidth</code>, or <code>XmNborderWidth</code> for either a VendorShell or its managed child usually sets that resource to the same value in both the parent and the child. When an off-the-spot input method exists, the height and width of the shell may be greater than those of the managed child in order to accommodate the input method. In this case, setting <code>XmNheight</code> or <code>XmNwidth</code> for the shell does not necessarily set that resource to the same value in the managed child, and setting <code>XmNheight</code> or <code>XmNwidth</code> for the child does not necessarily set that resource to the same value in the shell. </p>
<p> For the managed child of a VendorShell, regardless of the value of the shell&#8217;s <code>XmNallowShellResize</code>, setting <code>XmNx</code> or <code>XmNy</code> sets the corresponding resource of the parent but does not change the child&#8217;s position relative to the parent. <code>XtGetValues</code> for the child&#8217;s <code>XmNx</code> or <code>XmNy</code> yields the value of the corresponding resource in the parent. The x and y-coordinates of the child&#8217;s upper left outside corner relative to the parent&#8217;s upper left inside corner are both 0 (zero) minus the value of <code>XmNborderWidth</code>. </p>
<p> Note that the <i>Inter-Client Communication Conventions Manual</i> (ICCCM) allows a window manager to change or control the border width of a reparented top-level window. </p>
<p> VendorShell holds the <code>XmQTspecifyRenderTable</code> trait.</p>
<h3>Classes</h3>
<p>VendorShell inherits behavior, resources, and traits from the <code>Core</code>, <code>Composite</code>, <code>Shell</code>, and <code>WMShell</code> classes. </p>
<p> The class pointer is <code>vendorShellWidgetClass</code>. </p>
<p> The class name is <code>VendorShell</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a subresource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a subresource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given subresource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>VendorShell Resource Set</code>
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
<td>XmNaudibleWarning</td>
<td>XmCAudibleWarning</td>
<td>unsigned char</td>
<td>XmBELL</td>
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
<td>XmNdefaultFontList</td>
<td>XmCDefaultFontList</td>
<td>XmFontList</td>
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
<td>XmNdeleteResponse</td>
<td>XmCDeleteResponse</td>
<td>unsigned char</td>
<td>XmDESTROY</td>
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
<td>XmNinputMethod</td>
<td>XmCInputMethod</td>
<td>string</td>
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
<td>XmNinputPolicy</td>
<td>XmCInputPolicy</td>
<td>XmInputPolicy</td>
<td>XmPER_SHELL</td>
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
<td>XmNkeyboardFocusPolicy</td>
<td>XmCKeyboardFocusPolicy</td>
<td>unsigned char</td>
<td>XmEXPLICIT</td>
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
<td>XmCLabelRenderTabel</td>
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
<td>XmNlayoutDirection</td>
<td>XmCLayoutDirection</td>
<td>XmDirection</td>
<td>XmLEFT_TO_RIGHT</td>
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
<td>XmNmwmDecorations</td>
<td>XmCMwmDecorations</td>
<td>int</td>
<td>-1</td>
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
<td>XmNmwmFunctions</td>
<td>XmCMwmFunctions</td>
<td>int</td>
<td>-1</td>
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
<td>XmNmwmInputMode</td>
<td>XmCMwmInputMode</td>
<td>int</td>
<td>-1</td>
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
<td>XmNmwmMenu</td>
<td>XmCMwmMenu</td>
<td>String</td>
<td>NULL</td>
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
<td>XmNpreeditType</td>
<td>XmCPreeditType</td>
<td>String</td>
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
<td>XmNverifyPreedit</td>
<td>XmCVerifyPreedit</td>
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
<td>XmNshellUnitType</td>
<td>XmCShellUnitType</td>
<td>unsigned char</td>
<td>XmPIXELS</td>
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
<td>XmNtoolTipPostDelay</td>
<td>XmCToolTipPostDelay</td>
<td>int</td>
<td>5000</td>
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
<td>XmNtoolTipPostDuration</td>
<td>XmCToolTipPostDuration</td>
<td>int</td>
<td>5000</td>
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
<td>XmNtoolTipEnable</td>
<td>XmCToolTipEnable</td>
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
<td>XmNunitType</td>
<td>XmCUnitType</td>
<td>unsigned char</td>
<td>XmPIXELS</td>
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
<td>XmNuseAsyncGeometry</td>
<td>XmCUseAsyncGeometry</td>
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
</table>
</table>
<dl COMPACT>
<dt><code>XmNaudibleWarning</code></p>
<dd>Determines whether an action activates its associated audible cue. The possible values are <code>XmBELL</code> and <code>XmNONE</code>.</p>
<dt><code>XmNbuttonFontList</code></p>
<dd>Specifies the font list used for button descendants. See the <code>XmNbuttonRenderTable</code> resource.</p>
<dt><code>XmNbuttonRenderTable</code></p>
<dd>Specifies the render table used for VendorShell&#8217;s button descendants. If this value is NULL at initialization and if the value of <code>XmNdefaultFontList</code> is not NULL, <code>XmNbuttonRenderTable</code> is initialized to the value of <code>XmNdefaultFontList</code>. If the value of <code>XmNdefaultFontList</code> is NULL, the parent hierarchy of the widget is searched for an ancestor that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, <code>XmNbuttonRenderTable</code> is initialized to the <code>XmBUTTON_RENDER_TABLE</code> value of the ancestor widget. If no such ancestor is found, the default is implementation dependent. Refer to <code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3) for more information on the creation and structure of a render table.</p>
<dt><code>XmNdefaultFontList</code></p>
<dd>Specifies a default font list for VendorShell&#8217;s descendants. This resource is obsolete and exists for compatibility with earlier releases. It has been replaced by <code>XmNbuttonFontList</code>, <code>XmNlabelFontList</code>, and <code>XmNtextFontList</code>.</p>
<dt><code>XmNdeleteResponse</code></p>
<dd>Determines what action the shell takes in response to a <code>WM_DELETE_WINDOW</code> message. The setting can be one of three values: <code>XmDESTROY</code>, <code>XmUNMAP</code>, and <code>XmDO_NOTHING</code>. The resource is scanned, and the appropriate action is taken after the <code>WM_DELETE_WINDOW</code> callback list (if any) that is registered with the Protocol manager has been called.</p>
<dt><code>XmNinputMethod</code></p>
<dd>Specifies the string that sets the locale modifier for the input method. When <code>XtGetValues</code> is called on this resource, the returned value is a pointer to the actual resource value and should not be freed.</p>
<dt><code>XmNinputPolicy</code></p>
<dd>Specifies the policy to follow for creating an Input Context (IC) for this shell. This resource can have the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmPER_SHELL</code></p>
<dd>Specifies that only one XIC is created per shell.</p>
<dt><code>XmPER_WIDGET</code></p>
<dd>Specifies that one XIC is created for each widget.</dl>
</dl>
<dt><code>XmNkeyboardFocusPolicy</code></p>
<dd>Determines allocation of keyboard focus within the widget hierarchy rooted at this shell. The X keyboard focus must be directed to somewhere in the hierarchy for this client-side focus management to take effect. Possible values are <code>XmEXPLICIT</code>, specifying a click-to-type policy, and <code>XmPOINTER</code>, specifying a pointer-driven policy.</p>
<dt><code>XmNlabelFontList</code></p>
<dd>Specifies the font list used for label descendants. See the <code>XmNlabelRenderTable</code> resource.</p>
<dt><code>XmNlabelRenderTable</code></p>
<dd>Specifies the font list used for VendorShell&#8217;s label descendants (Labels and LabelGadgets). If this value is NULL at initialization and if the value of <code>XmNdefaultFontList</code> is not NULL, <code>XmNlabelFontList</code> is initialized to the value of <code>XmNdefaultFontList</code>. If the value of <code>XmNdefaultFontList</code> is NULL, the parent hierarchy of the widget is searched for an ancestor that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, <code>XmNlabelRenderTable</code> is initialized to the <code>XmLABEL_RENDER_TABLE</code> of the ancestor widget. If no such ancestor is found, the default is implementation dependent. Refer to <code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3) for more information on the creation and structure of a render table.</p>
<dt><code>XmNlayoutDirection</code></p>
<dd>Specifies the direction in which the subwidgets, children of a widget, or other visual components are to be laid out. This policy will apply as the default layout policy for all descendants of this VendorShell.</p>
<dt><code>XmNmwmDecorations</code></p>
<dd>Specifies the decoration flags (specific decorations to add or remove from the window manager frame) for the <code>_MOTIF_WM_HINTS</code> property. If any decoration flags are specified by the <code>_MOTIF_WM_HINTS</code> property, only decorations indicated by both that property and the MWM <code>clientDecoration</code> and <code>transientDecoration</code> resources are displayed. If no decoration flags are specified by the <code>_MOTIF_WM_HINTS</code> property, decorations indicated by the MWM <code>clientDecoration</code> and <code>transientDecoration</code> resources are displayed. The default for the <code>XmNmwmDecorations</code> resource is not to specify any decoration flags for the <code>_MOTIF_WM_HINTS</code> property.</p>
<dd>The value of this resource is the bitwise inclusive OR of one or more flag bits. The possible flag bit constants, defined in the include file <code>Xm/MwmUtil.h</code>, are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>MWM_DECOR_ALL</code></p>
<dd>All decorations <i>except</i> those specified by other flag bits that are set</p>
<dt><code>MWM_DECOR_BORDER</code></p>
<dd>Client window border</p>
<dt><code>MWM_DECOR_RESIZEH</code></p>
<dd>Resize frame handles</p>
<dt><code>MWM_DECOR_TITLE</code></p>
<dd>Title bar</p>
<dt><code>MWM_DECOR_MENU</code></p>
<dd>Window menu button</p>
<dt><code>MWM_DECOR_MINIMIZE</code></p>
<dd>Minimize window button</p>
<dt><code>MWM_DECOR_MAXIMIZE</code></p>
<dd>Maximize window button</dl>
</dl>
<dt><code>XmNmwmFunctions</code></p>
<dd>Specifies the function flags (specific window manager functions to apply or not apply to the client window) for the <code>_MOTIF_WM_HINTS</code> property. If any function flags are specified by the <code>_MOTIF_WM_HINTS</code> property, only functions indicated by both that property and the MWM <code>clientFunctions</code> and <code>transientFunctions</code> resources are applied. If no function flags are specified by the <code>_MOTIF_WM_HINTS</code> property, functions indicated by the MWM <code>clientFunctions</code> and <code>transientFunctions</code> resources are applied. The default for the <code>XmNmwmFunctions</code> resource is not to specify any function flags for the <code>_MOTIF_WM_HINTS</code> property.</p>
<dd>The value of this resource is the bitwise inclusive OR of one or more flag bits. The possible flag bit constants, defined in the include file <code>Xm/MwmUtil.h</code>, are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>MWM_FUNC_ALL</code></p>
<dd>All functions <i>except</i> those specified by other flag bits that are set</p>
<dt><code>MWM_FUNC_RESIZE</code></p>
<dd><code>f.resize</code></p>
<dt><code>MWM_FUNC_MOVE</code></p>
<dd><code>f.move</code></p>
<dt><code>MWM_FUNC_MINIMIZE</code></p>
<dd><code>f.minimize</code></p>
<dt><code>MWM_FUNC_MAXIMIZE</code></p>
<dd><code>f.maximize</code></p>
<dt><code>MWM_FUNC_CLOSE</code></p>
<dd><code>f.kill</code></dl>
</dl>
<dt><code>XmNmwmInputMode</code></p>
<dd>Specifies the input mode flag (application modal or system modal input constraints) for the <code>_MOTIF_WM_HINTS</code> property. If no input mode flag is specified by the <code>_MOTIF_WM_HINTS</code> property, no input constraints are applied, and input goes to any window. The default for the <code>XmNmwmInputMode</code> resource is not to specify any input mode flag for the <code>_MOTIF_WM_HINTS</code> property.</p>
<dd>An application that sets input constraints on a dialog usually uses the BulletinBoard&#8217;s <code>XmNdialogStyle</code> resource rather than the parent DialogShell&#8217;s <code>XmNmwmInputMode</code> resource.</p>
<dd>The possible values for this resource, defined in the include file <code>Xm/MwmUtil.h</code>, are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>MWM_INPUT_MODELESS</code></p>
<dd>Input goes to any window.</p>
<dt><code>MWM_INPUT_PRIMARY_APPLICATION_MODAL</code></p>
<dd>Input does not go to ancestors of this window.</p>
<dt><code>MWM_INPUT_SYSTEM_MODAL</code></p>
<dd>Input goes only to this window.</p>
<dt><code>MWM_INPUT_FULL_APPLICATION_MODAL</code></p>
<dd>Input does not go to other windows in this application.</dl>
</dl>
<dt><code>XmNmwmMenu</code></p>
<dd>Specifies the menu items that the Motif window manager should add to the end of the window menu. The string contains a list of items separated by <code>fP with the following format:</dl>
<p> </code></p>
<pre><i>label [mnemonic] [accelerator] function</i></pre>
<dl COMPACT>
<dd>If more than one item is specified, the items should be separated by a newline character.</p>
<dd>When <code>XtGetValues</code> is called on this resource, the returned value is a pointer to the actual resource value and should not be freed.</p>
<dt><code>XmNpreeditType</code></p>
<dd>Specifies the input method style or styles available to the input manager. The resource can be a comma-separated list of the following values: </p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2><code>Preedit Values</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Preedit Value</code></td>
<td><code>XIM Style</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>OffTheSpot</td>
<td>XIMPreeditArea
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Root</td>
<td>XIMPreeditNothing
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>None</td>
<td>XIMPreeditNone
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>OverTheSpot</td>
<td>XIMPreeditPosition
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>OnTheSpot</td>
<td>XIMPreeditCallbacks
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
<dd>When <code>XtGetValues</code> is called on this resource, the returned value is a pointer to the actual resource value and should not be freed.</p>
<dt><code>XmNshellUnitType</code></p>
<dd>This resource is obsolete, and is included only for compatibility with earlier releases of Motif. Use the <code>XmNunitType</code> resource instead.</p>
<dt><code>XmNtextFontList</code></p>
<dd>Specifies the font list used for text descendants. See the <code>XmNtextRenderTable</code> resource.</p>
<dt><code>XmNtextRenderTable</code></p>
<dd>Specifies the render table used for VendorShell&#8217;s Text and List descendants. If this value is NULL at initialization and if the value of <code>XmNdefaultFontList</code> is not NULL, <code>XmNtextRenderTable</code> is initialized to the value of <code>XmNdefaultFontList</code>. If the value of <code>XmNdefaultFontList</code> is NULL, the parent hierarchy of the widget is searched for an ancestor that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, <code>XmNtextRenderTable</code> is initialized to the <code>XmTEXT_RENDER_TABLE</code> value of the ancestor widget. If no such ancestor is found, the default is implementation dependent. Refer to <code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3) for more information on the creation and structure of a render table.</p>
<dt><code>XmNtoolTipEnable</code></p>
<dd>Specifies whether toolTips are enabled for this shell or not. </p>
<dt><code>XmNtoolTipPostDelay</code></p>
<dd>Specifies the time, in milliseconds, to wait after the pointer enters a widget before posting the toolTip associated with this widget. </p>
<dt><code>XmNtoolTipPostDuration</code></p>
<dd>Specifies the time, in milliseconds, that the toolTip is displayed. A value of 0 will display the tip indefinitely. </p>
<dt><code>XmNunitType</code></p>
<dd>Provides the basic support for resolution independence. It defines the type of units a widget uses with sizing and positioning resources. The resource has a default unit type of <code>XmPIXELS</code>.</p>
<dd>The unit type can also be specified in resource files, with the following format:</dl>
<pre><tt></tt><i>&lt;floating value&gt;&lt;unit&gt;</i></pre>
<dl COMPACT>
<dd>where:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>unit</i></p>
<dd>is &lt;&quot; &quot;, pixels, inches, centimeters, millimeters, points, font units&gt;</p>
<dt><i>pixels</i></p>
<dd>is &lt;<i>pix</i>, <i>pixel</i>, <i>pixels</i>&gt;</p>
<dt><i>inches</i></p>
<dd>is &lt;<i>in</i>, <i>inch</i>, <i>inches</i>&gt;</p>
<dt><i>centimeter</i></p>
<dd>is &lt;<i>cm</i>, <i>centimeter</i>, <i>centimeters</i>&gt;</p>
<dt><i>millimeters</i></p>
<dd>is &lt;<i>mm</i>, <i>millimeter</i>, <i>millimeters</i>&gt;</p>
<dt><code>points</code></p>
<dd>is &lt;<i>pt</i>, <i>point</i>, <i>points</i>&gt;</p>
<dt><code>font units</code></p>
<dd>is &lt;<i>fu</i>, <code>font_unit</code>, <code>font_units</code>&gt;</p>
<dt><i>float</i></p>
<dd>is {&quot;+&quot;|&quot;-&quot;}&#123;&#123;&lt;&quot;0&quot;-&quot;9&quot;&gt;*}.}&lt;&quot;0&quot;-&quot;9&quot;&gt;*</p>
<dd>Note that the type Dimension must always be positive.</dl>
</dl>
<dd>For example,</dl>
<pre><tt>xmfonts*XmMainWindow.height: 10.4cm
*PostIn.width: 3inches</tt></pre>
<dl COMPACT>
<dd><code>XmNunitType</code> can have the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmPIXELS</code></p>
<dd>All values provided to the widget are treated as normal pixel values.</p>
<dt><code>XmMILLIMETERS</code></p>
<dd>All values provided to the widget are treated as normal millimeter values.</p>
<dt><code>Xm100TH_MILLIMETERS</code></p>
<dd>All values provided to the widget are treated as 1/100 of a millimeter.</p>
<dt><code>XmCENTIMETERS</code></p>
<dd>All values provided to the widget are treated as normal centimeter values.</p>
<dt><code>XmINCHES</code></p>
<dd>All values provided to the widget are treated as normal inch values.</p>
<dt><code>Xm1000TH_INCHES</code></p>
<dd>All values provided to the widget are treated as 1/1000 of an inch.</p>
<dt><code>XmPOINTS</code></p>
<dd>All values provided to the widget are treated as normal point values. A point is a unit used in text processing applications and is defined as 1/72 of an inch.</p>
<dt><code>Xm100TH_POINTS</code></p>
<dd>All values provided to the widget are treated as 1/100 of a point. A point is a unit used in text processing applications and is defined as 1/72 of an inch.</p>
<dt><code>XmFONT_UNITS</code></p>
<dd>All values provided to the widget are treated as normal font units. A font unit has horizontal and vertical components. These are the values of the XmScreen resources <code>XmNhorizontalFontUnit</code> and <code>XmNverticalFontUnit</code>.</p>
<dt><code>Xm100TH_FONT_UNITS</code></p>
<dd>All values provided to the widget are treated as 1/100 of a font unit. A font unit has horizontal and vertical components. These are the values of the <code>XmScreen</code> resources <code>XmNhorizontalFontUnit</code> and <code>XmNverticalFontUnit</code>.</dl>
</dl>
<dd>For more information about units, refer to the <code>XmConvertUnits</code> reference page.</p>
<dt><code>XmNuseAsyncGeometry</code></p>
<dd>Specifies whether the geometry manager should wait for confirmation of a geometry request to the window manager. When the value of this resource is True, the geometry manager forces <code>XmNwaitForWm</code> to False and <code>XmNwmTimeout</code> to 0, and it relies on asynchronous notification. When the value of this resource is False, <code>XmNwaitForWm</code> and <code>XmNwmTimeout</code> are unaffected. The default is False. </p>
</dl>
<h3>Inherited Resources</h3>
<p>VendorShell inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>WMShell Resource Set</code>
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
<td>XmNbaseHeight</td>
<td>XmCBaseHeight</td>
<td>int</td>
<td>XtUnspecifiedShellInt</td>
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
<td>XmNbaseWidth</td>
<td>XmCBaseWidth</td>
<td>int</td>
<td>XtUnspecifiedShellInt</td>
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
<td>XmNheightInc</td>
<td>XmCHeightInc</td>
<td>int</td>
<td>XtUnspecifiedShellInt</td>
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
<td>XmNiconMask</td>
<td>XmCIconMask</td>
<td>Pixmap</td>
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
<td>XmNiconPixmap</td>
<td>XmCIconPixmap</td>
<td>Pixmap</td>
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
<td>XmNiconWindow</td>
<td>XmCIconWindow</td>
<td>Window</td>
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
<td>XmNiconX</td>
<td>XmCIconX</td>
<td>int</td>
<td>XtUnspecifiedShellInt</td>
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
<td>XmNiconY</td>
<td>XmCIconY</td>
<td>int</td>
<td>XtUnspecifiedShellInt</td>
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
<td>XmNinitialState</td>
<td>XmCInitialState</td>
<td>int</td>
<td>NormalState</td>
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
<td>XmNinput</td>
<td>XmCInput</td>
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
<td>XmNmaxAspectX</td>
<td>XmCMaxAspectX</td>
<td>int</td>
<td>XtUnspecifiedShellInt</td>
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
<td>XmNmaxAspectY</td>
<td>XmCMaxAspectY</td>
<td>int</td>
<td>XtUnspecifiedShellInt</td>
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
<td>XmNmaxHeight</td>
<td>XmCMaxHeight</td>
<td>int</td>
<td>XtUnspecifiedShellInt</td>
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
<td>XmNmaxWidth</td>
<td>XmCMaxWidth</td>
<td>int</td>
<td>XtUnspecifiedShellInt</td>
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
<td>XmNminAspectX</td>
<td>XmCMinAspectX</td>
<td>int</td>
<td>XtUnspecifiedShellInt</td>
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
<td>XmNminAspectY</td>
<td>XmCMinAspectY</td>
<td>int</td>
<td>XtUnspecifiedShellInt</td>
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
<td>XmNminHeight</td>
<td>XmCMinHeight</td>
<td>int</td>
<td>XtUnspecifiedShellInt</td>
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
<td>XmNminWidth</td>
<td>XmCMinWidth</td>
<td>int</td>
<td>XtUnspecifiedShellInt</td>
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
<td>String</td>
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
<td>XmNtitleEncoding</td>
<td>XmCTitleEncoding</td>
<td>Atom</td>
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
<td>XmNtransient</td>
<td>XmCTransient</td>
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
<td>XmNwaitForWm</td>
<td>XmCWaitForWm</td>
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
<td>XmNwidthInc</td>
<td>XmCWidthInc</td>
<td>int</td>
<td>XtUnspecifiedShellInt</td>
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
<td>XmNwindowGroup</td>
<td>XmCWindowGroup</td>
<td>Window</td>
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
<td>mNwinGravity</td>
<td>XmCWinGravity</td>
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
<td>XmNwmTimeout</td>
<td>XmCWmTimeout</td>
<td>int</td>
<td>5000 ms</td>
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
<td ALIGN=center COLSPAN=5><code>Shell Resource Set</code>
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
<td>XmNallowShellResize</td>
<td>XmCAllowShellResize</td>
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
<td>XmNcreatePopupChildProc</td>
<td>XmCCreatePopupChildProc</td>
<td>XtCreatePopupChildProc</td>
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
<td>XmNgeometry</td>
<td>XmCGeometry</td>
<td>String</td>
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
<td>XmNoverrideRedirect</td>
<td>XmCOverrideRedirect</td>
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
<td>XmNpopdownCallback</td>
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
<td>XmNpopupCallback</td>
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
<td>XmNsaveUnder</td>
<td>XmCSaveUnder</td>
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
<td>XmNvisual</td>
<td>XmCVisual</td>
<td>Visual *</td>
<td>CopyFromParent</td>
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
<p>There are no translations for VendorShell.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/1-mwm/">mwm</a></code>(1), <code><a href="/docs/linux/man/3-shell/">Shell</a></code>(3), <code><a href="/docs/linux/man/3-wmshell/">WMShell</a></code>(3), <code><a href="/docs/linux/man/3-xmactivateprotocol/">XmActivateProtocol</a></code>(3), <code><a href="/docs/linux/man/3-xmactivatewmprotocol/">XmActivateWMProtocol</a></code>(3), <code><a href="/docs/linux/man/3-xmaddprotocolcallback/">XmAddProtocolCallback</a></code>(3), <code><a href="/docs/linux/man/3-xmaddwmprotocolcallback/">XmAddWMProtocolCallback</a></code>(3), <code><a href="/docs/linux/man/3-xmaddprotocols/">XmAddProtocols</a></code>(3), <code><a href="/docs/linux/man/3-xmaddwmprotocols/">XmAddWMProtocols</a></code>(3), <code><a href="/docs/linux/man/3-xmdeactivateprotocol/">XmDeactivateProtocol</a></code>(3), <code><a href="/docs/linux/man/3-xmdeactivatewmprotocol/">XmDeactivateWMProtocol</a></code>(3), <code><a href="/docs/linux/man/3-xmgetatomname/">XmGetAtomName</a></code>(3), <code><a href="/docs/linux/man/3-xminternatom/">XmInternAtom</a></code>(3), <code><a href="/docs/linux/man/3-xmismotifwmrunning/">XmIsMotifWMRunning</a></code>(3), <code><a href="/docs/linux/man/3-xmremoveprotocolcallback/">XmRemoveProtocolCallback</a></code>(3), <code><a href="/docs/linux/man/3-xmremovewmprotocolcallback/">XmRemoveWMProtocolCallback</a></code>(3), <code><a href="/docs/linux/man/3-xmremoveprotocols/">XmRemoveProtocols</a></code>(3), <code><a href="/docs/linux/man/3-xmremovewmprotocols/">XmRemoveWMProtocols</a></code>(3), <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3), <code><a href="/docs/linux/man/3-xmsetprotocolhooks/">XmSetProtocolHooks</a></code>(3), and <code><a href="/docs/linux/man/3-xmsetwmprotocolhooks/">XmSetWMProtocolHooks</a></code>(3).</p>
