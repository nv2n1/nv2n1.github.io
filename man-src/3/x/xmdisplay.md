---
title: "xmdisplay(3)"
name: "xmdisplay"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdisplay/"
description: "XmDisplay — The Display widget class"
---

<p><code>XmDisplay</code> &#8212; The Display widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Display.h&gt;</pre>
<h2>Description</h2>
<p>The XmDisplay object is used by the Motif widgets to store information that is specific to a display. It also allows the toolkit to access certain information on widget hierarchies that would otherwise be unavailable. Each client has one XmDisplay object for each display it accesses. </p>
<p> An XmDisplay object is automatically created when the application creates the first shell on a display (usually accomplished by a call to <code>XtAppInitialize</code> or <code>XtAppCreateShell</code>). It is not necessary to create an XmDisplay object by any other means. An application can use the function <code>XmGetXmDisplay</code> to obtain the widget ID of the XmDisplay object for a given display. </p>
<p> An application cannot supply initial values for XmDisplay resources as arguments to a call to any function that creates widgets. The application or user can supply initial values in a resource file. After creating the first shell on the display, the application can use <code>XmGetXmDisplay</code> to obtain the widget ID of the XmDisplay object and then call <code>XtSetValues</code> to set the XmDisplay resources. </p>
<p> XmDisplay resources specify the drag protocol style for a client participating in drag and drop transactions. The two basic protocol types are preregister and dynamic. When a preregister protocol is used, the toolkit handles any communication between the initiator and receiver clients and displays the appropriate drag-over and drag-under visual effects. A client registers its drop sites in advance and this information is stored in a property for each top-level window. When the drag pointer enters a top-level window, the drop site information is read by the initiator. A dynamic protocol allows the source and destination clients to dynamically communicate drag and drop state information between each other, and to update their respective visuals accordingly. The toolkit provides drop site information as the pointer passes over any given drop site. In this mode, a receiver can supply a procedure to generate its own drag-under effects.</p>
<h3>Classes</h3>
<p>Display inherits behavior and resources from <code>Core</code>, <code>Composite</code>, <code>Shell</code>, <code>WMShell</code>, <code>VendorShell</code>, <code>TopLevelShell</code>, and <code>ApplicationShell</code> classes. </p>
<p> The class pointer is <code>xmDisplayClass</code>. </p>
<p> The class name is <code>XmDisplay</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using XtSetValues (S), retrieved by using XtGetValues (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmDisplay Resource Set</code>
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
<td>XmNdefaultButtonEmphasis</td>
<td>XmCDefaultButtonEmphasis</td>
<td>XtEnum</td>
<td>XmEXTERNAL_HIGHLIGHT</td>
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
<td>XmNdefaultVirtualBindings</td>
<td>XmCDefaultVirtualBindings</td>
<td>String</td>
<td>dynamic</td>
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
<td>XmNdragInitiatorProtocolStyle</td>
<td>XmCDragInitiatorProtocolStyle</td>
<td>unsigned char</td>
<td>XmDRAG_PREFER_RECEIVER</td>
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
<td>XmNdragReceiverProtocolStyle</td>
<td>XmCDragReceiverProtocolStyle</td>
<td>unsigned char</td>
<td>XmDRAG_PREFER_DYNAMIC</td>
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
<td>XmNdragStartCallback</td>
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
<td>XmNenableBtn1Transfer</td>
<td>XmCEnableBtn1Transfer</td>
<td>XtEnum</td>
<td>XmOFF</td>
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
<td>XmNenableButtonTab</td>
<td>XmCEnableButtonTab</td>
<td>Boolean</td>
<td>False</td>
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
<td>XmNenableDragIcon</td>
<td>XmCEnableDragIcon</td>
<td>Boolean</td>
<td>False</td>
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
<td>XmNenableEtchedInMenu</td>
<td>XmCEnableEtchedInMenu</td>
<td>Boolean</td>
<td>False</td>
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
<td>XmNenableToggleColor</td>
<td>XmCEnableToggleColor</td>
<td>Boolean</td>
<td>False</td>
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
<td>XmNenableToggleVisual</td>
<td>XmCEnableToggleVisual</td>
<td>Boolean</td>
<td>False</td>
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
<td>XmNenableUnselectableDrag</td>
<td>XmCEnableUnselectableDrag</td>
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
<td>XmNenableWarp</td>
<td>XmCEnableWarp</td>
<td>XtEnum</td>
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
<td>XmNmotifVersion</td>
<td>XmCMotifVersion</td>
<td>int</td>
<td>XmVERSION</td>
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
<td>XmNnoFontCallback</td>
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
<td>XmNnoRenditionCallback</td>
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
<dl COMPACT>
<dt><code>XmNdefaultButtonEmphasis</code></p>
<dd>Specifies whether to change the look of the PushButton widget and gadget that have the <code>XmNshowAsDefault</code> resource set. When the PushButton is the default, it has an etched out button which is enclosed with another etched in border. The <code>XmNdefaultButtonEmphasis</code> has the follow possible values, which affect the location cursor:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmINTERNAL_HIGHLIGHT</code></p>
<dd>Causes the location cursor to appear in between the two etched borders to minimize the space required.</p>
<dt><code>XmEXTERNAL_HIGHLIGHT</code></p>
<dd>Causes the PushButton to draw the location cursor outside the second border.</dl>
</dl>
<dt><code>XmNdefaultVirtualBindings</code></p>
<dd>Specifies the default virtual bindings for the display. Following is an example of a specification for the <code>defaultVirtualBindings</code> resource in a resource file:</dl>
<pre><tt>*defaultVirtualBindings: \
 osfBackSpace: &lt;Key&gt;BackSpace 
\
 osfInsert: &lt;Key&gt;InsertChar 
\
 osfDelete: &lt;Key&gt;DeleteChar 
\
 ...
 osfLeft: &lt;Key&gt;left, Ctrl&lt;Key&gt;H</tt></pre>
<dl COMPACT>
<dt><code>XmNdragInitiatorProtocolStyle</code></p>
<dd>Specifies the drag and drop protocol requirements or preference when the client is an initiator. The possible values are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmDRAG_PREREGISTER</code></p>
<dd>As an initiator, this client does not use the dynamic protocol and can only arrange visual effects with receivers who provide preregistered information.</p>
<dt><code>XmDRAG_DYNAMIC</code></p>
<dd>As an initiator, this client does not make use of any preregistered drop site information made available by other clients, and can only arrange visual effects with receivers who use the dynamic protocol.</p>
<dt><code>XmDRAG_NONE</code></p>
<dd>Specifies that drag and drop is disabled for this client.</p>
<dt><code>XmDRAG_DROP_ONLY</code></p>
<dd>As an initiator, this client does not use either the preregistered drop site information or the dynamic protocol. It supports dragging, and any time the cursor is over a client that supports drag and drop, valid feedback is provided. There are no other visual effects.</p>
<dt><code>XmDRAG_PREFER_DYNAMIC</code></p>
<dd>As an initiator, this client can support both the preregister and dynamic protocols, but prefers to use dynamic protocols whenever possible in order to provide high-quality drag-under feedback.</p>
<dt><code>XmDRAG_PREFER_PREREGISTER</code></p>
<dd>As an initiator, this client can support both the preregister and dynamic protocols, but prefers to use the preregister protocol whenever possible in order to accommodate performance needs or to provide consistent drag-over feedback.</p>
<dt><code>XmDRAG_PREFER_RECEIVER</code></p>
<dd>Indicates that this client can support both preregister and dynamic protocols, but will defer to the preference of the receiver client. This value is valid only for the <code>XmNdragInitiatorProtocolStyle</code> resource, and is its default value.</dl>
</dl>
<dt><code>XmNdragReceiverProtocolStyle</code></p>
<dd>Specifies the drag and drop protocol requirements or preference when this client is a receiver. The values are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmDRAG_PREREGISTER</code></p>
<dd>As a receiver, this client preregisters drop site information and does not use the dynamic protocol. It can only arrange visual effects with initiators who make use of the preregistered information.</p>
<dt><code>XmDRAG_DYNAMIC</code></p>
<dd>As a receiver, this client uses the dynamic protocol and does not preregister drop site information. It can only arrange visual effects with initiators who use the dynamic protocol.</p>
<dt><code>XmDRAG_NONE</code></p>
<dd>Specifies that drag and drop is disabled for this client.</p>
<dt><code>XmDRAG_DROP_ONLY</code></p>
<dd>As a receiver, this client neither uses the dynamic protocol nor preregisters drop site information. It supports dropping, and when dragging over this client, valid feedback is always provided, but there are no other visual effects.</p>
<dt><code>XmDRAG_PREFER_DYNAMIC</code></p>
<dd>As a receiver, this client can support both the preregister and dynamic protocols, but prefers to use the dynamic protocol whenever possible in order to provide high-quality drag-under feedback.</p>
<dt><code>XmDRAG_PREFER_PREREGISTER</code></p>
<dd>As a receiver, this client can support both the preregister and dynamic protocols, but prefers to use the preregister protocol whenever possible in order to accommodate performance needs.</dl>
</dl>
<dd>The default value of this resource is dependent on the capabilities of the display. If the display supports the shape extension, allowing the dynamic protocol to use arbitrarily sized drag cursors, the default of this resource is <code>XmDRAG_PREFER_DYNAMIC</code>, otherwise the default is <code>XmDRAG_PREFER_PREREGISTER</code>.</p>
<dd>The actual protocol used between an initiator and a receiver is based on the protocol style of the receiver and initiator. The decision matrix is described in the following table. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center VALIGN=center ROWSPAN=2><code>Drag Initiator</code></td>
<td ALIGN=center COLSPAN=4></td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td><code>Drag Receiver Protocol Style</code></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Preregister</code></td>
<td><code>Prefer Preregister</code></td>
<td><code>Prefer Dynamic</code></td>
<td><code>Dynamic</code></td>
<td></td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Preregister</td>
<td>Preregister</td>
<td>Preregister</td>
<td>Drop Only</td>
<td></td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Preregister</td>
<td>Preregister</td>
<td>Preregister</td>
<td>Dynamic</td>
<td></td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Preregister</td>
<td>Preregister</td>
<td>Dynamic</td>
<td>Dynamic</td>
<td></td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Preregister</td>
<td>Dynamic</td>
<td>Dynamic</td>
<td>Dynamic</td>
<td></td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Drop Only</td>
<td>Dynamic</td>
<td>Dynamic</td>
<td>Dynamic</td>
<td></td>
</tr>
</table>
</table>
<dd>The value <code>XmDRAG_NONE</code> does not appear in the matrix. When specified for either the initiator or receiver side, <code>XmDRAG_NONE</code> implies that drag and drop transactions are not supported. A value of <code>XmDRAG_DROP_ONLY</code> (Drop Only) results when an initiator and receiver cannot compromise protocol styles, that is, one client requires dynamic mode while the other can only support preregister mode, or if either explicitly has specified <code>XmDRAG_DROP_ONLY</code>.</p>
<dt><code>XmNdragStartCallback</code></p>
<dd>Specifies the list of callbacks that are invoked when the <code>XmDragStart</code> function is called. The type of structure whose address is passed to this callback is <code>XmDragStartCallbackStruct</code>. The callback reason is <code>XmCR_DRAG_START</code>.</p>
<dt><code>XmNenableBtn1Transfer</code></p>
<dd>Specifies if selection and transfer actions are integrated on Btn1 and extend actions are activated on Btn2. This resource can take the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmOFF</code></p>
<dd>Disables integration and selection activation on Btn1.</p>
<dt><code>XmBUTTON2_TRANSFER</code></p>
<dd>Enables integration and selection activation on Btn1 and transfer on Btn2.</p>
<dt><code>XmBUTTON2_ADJUST</code></p>
<dd>Enables integration and selection activation on Btn1 and adjust on Btn2.</dl>
</dl>
<dd>This resource affects the actions of Text, TextField, List, and Container.</p>
<dt><code>XmNenableButtonTab</code></p>
<dd>Specifies if the action for the <code>&lt;Tab&gt;</code> key (<code>KNextField</code> and <code>KPrevField</code> actions) is to be modified. A value of True modifies the key to move as an arrow key until the boundary of a tab group is reached. Then, at the boundary of the tab group, <code>KNextField</code> and <code>KPrevField</code> will move to the next or previous tab group, respectively. A value of False does not cause modification.</p>
<dt><code>XmNenableDragIcon</code></p>
<dd>Specifies which set of icons are to be used for system default cursors during drag and drop operations. A value of False specifies that earlier versions of Motif release icons are used, a value of True specifies that alternate icons are used. This resource affects both the 16&#215;16 and the 32&#215;32 icons that the system defaults for each of the Screen objects associated with this display.</p>
<dt><code>XmNenableEtchedInMenu</code></p>
<dd>Specifies the shadowing of the button widgets and gadgets in menus when the control is activated. A value of True causes the selected menu to be drawn with the shadow etched in; this shadow style is consistent with the selected appearance of other button widgets outside of menus. A value of False causes the selected menu to be draw with the shadow etched out. This resource affects the actions of PushButton, ToggleButton, and CascadeButton widgets and gadgets when they are children of Menu.</p>
<dd>When this resource is set, the background of a button in a menu uses the <code>XmNselectColor</code> (derived from the <code>XmNselectPixel</code>) when armed as a default. A <code>PushButton</code> uses the <code>XmNarmColor</code> if it is defined. A <code>ToggleButton</code> uses the <code>XmNselectColor</code> if <code>XmNindicatorOn</code> is <code>False</code> and <code>XmNfillOnSelect</code> is <code>True</code>.</p>
<dt><code>XmNenableToggleColor</code></p>
<dd>Specifies how to determine the default value of the <code>XmNselectColor</code> resource of ToggleButton and ToggleButtonGadget. A value of True causes the default value of <code>XmNselectColor</code> to be set to the value of <code>XmNhighlightColor</code>. A value of False causes the default value of <code>XmNselectColor</code> to be set to the value of <code>XmNbackground</code>. This resource only affects the appearance of ToggleButton widgets and gadgets that are in <code>XmONE_OF_MANY</code> or <code>XmONE_OF_MANY_ROUND</code> mode. In addition, <code>XmNenableToggleColor</code> only influences the default value of <code>XmNselectColor</code>. That is, if the user or application sets a value for <code>XmNselectColor</code>, then <code>XmNenableToggleColor</code> is ignored.</p>
<dt><code>XmNenableToggleVisual</code></p>
<dd>Specifies the visual appearance of the ToggleButton widget and/or gadget. This resource affects the default value of the ToggleButton[Gadget] <code>XmNindicatorType</code> and <code>XmNindicatorOn</code> resources. When the ToggleButton is in a RadioBox, a value of True causes the <code>XmONE_OF_MANY_ROUND</code> (a shadowed circle) to be the default. Otherwise, when this resource is True, the ToggleButton <code>XmNindicatorOn</code> resource causes a default of <code>XmN_OF_MANY</code>, which will be a shadowed square with a check mark (check box).</p>
<dd>A value of False causes the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmONE_OF_MANY</code></p>
<dd>Is a shadowed diamond.</p>
<dt><code>XmN_OF_MANY</code></p>
<dd>Is a shadowed square.</dl>
</dl>
<dt><code>XmNenableUnselectableDrag</code></p>
<dd>Specifies whether or not it is possible to drag from Label and Scale. A value of True enables the drag; a value of False disables it.</p>
<dt><code>XmNenableWarp</code></p>
<dd>Specifies if an application is allowed to warp the pointer from the user. A value of True enables warping, a value of False does not.</p>
<dt><code>XmNmotifVersion</code></p>
<dd>Specifies the current version of Motif that the current implementation is supposed to behave like. By default, this resource gets its value from release values in <code>Xm.h</code>.</p>
<dt><code>XmNnoFontCallback</code></p>
<dd>This callback is called whenever a rendition attempts to load a font or fontset and fails. This can happen on creation if the font is specified as <code>XmLOAD_IMMEDIATE</code> or when an attempt is made to render an <code>XmString</code> using a font specified as <code>XmLOAD_DEFERRED</code>. An application can have this callback attempt to remedy this problem by calling <code>XmRenditionUpdate</code> on the input rendition to provide a font for the widget to use. This may be done by either providing an an alternative font name to be loaded using the <code>XmNfontName</code> and <code>XmNfontType</code> resources or with an already loaded font using the <code>XmNfont</code> resource. The callback reason is <code>XmCR_NO_FONT</code>. This callback uses the <code>XmDisplayCallbackStruct</code> structure.</p>
<dt><code>XmNnoRenditionCallback</code></p>
<dd>This callback is called whenever an attempt is made to render a segment with a <code>RENDITION</code> tag which does not match any renditions in a given render table. The callback reason is <code>XmCR_NO_RENDITION</code>. This callback uses the <code>XmDisplayCallbackStruct</code> structure.</p>
<dd>An application can have this callback attempt to remedy this problem by creating a new rendition with the given tag and adding it to <code>render_table</code>.</p>
<dd>The <code>XmNnoRenditionCallback</code> should deallocate the render table passed in in the <code>render_table</code> field of the callback structure. Note that the table will automatically be deallocated if the <code>XmRenderTableAddRenditions</code> function is called on it. The callback should NOT deallocate the modified render table that is passed back to Motif in the <code>render_table</code> field. If the application wishes to manipulate this render table further, it should make a copy with the <code>XmRenderTableCopy</code> function before returning from the callback.</p>
<dt><code>XmNuserData</code></p>
<dd>Specifies a client data pointer for applications. An internally unused resource.</dl>
<h3>Inherited Resources</h3>
<p>All of the superclass resources inherited by XmDisplay are designated N/A (not applicable).</p>
<h3>Callback Information</h3>
<p>A pointer to the following structure is passed to the <code>XmNdragStartCallback</code> callback: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Widget <i>timeStamp</i>;
 Boolean <i>doit</i>;
}XmDragStartCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback</p>
<dt><i>widget</i></p>
<dd>Indicates the ID of the widget from which the drag was initiated.</p>
<dt><i>doit</i></p>
<dd>Is an IN/OUT member that allows the callback to determine whether to continue with the drag or cancel. Setting <i>doit</i> to False will cancel the drag. The default value is NULL.</dl>
<p> A pointer to the following structure is passed to the <code>XmNnoFontCallback</code> and <code>XmNnoRenditionCallback</code> callbacks: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 XmRendition <i>rendition</i>;
 char *<i>font_name</i>;
 XmRenderTable <i>render_table</i>;
 XmStringTag <i>tag</i>;
}XmDisplayCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback. It can be NULL.</p>
<dt><i>rendition</i></p>
<dd>Specifies the rendition with the missing font.</p>
<dt><i>font_name</i></p>
<dd>Specifies the name of the font or font set which could not be loaded.</p>
<dt><code>render_table</code></p>
<dd>Specifies the render table with the missing rendition.</p>
<dt><i>tag</i></p>
<dd>Specifies the tag of the missing rendition.</dl>
<p> The following table describes the reasons for which the individual callback structure fields are valid. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Reason</code></td>
<td><code>Valid Fields</code>
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
<td>XmCR_NO_FONT</td>
<td><i>rendition, font_name</i>
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
<td>XmCR_NO_RENDITION</td>
<td><i>render_table, tag</i>
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
</table>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-applicationshell/">ApplicationShell</a></code>(3), <code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-toplevelshell/">TopLevelShell</a></code>(3), <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3), <code><a href="/docs/linux/man/3-wmshell/">WMShell</a></code>(3), <code><a href="/docs/linux/man/3-xmgetxmdisplay/">XmGetXmDisplay</a></code>(3), and <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
