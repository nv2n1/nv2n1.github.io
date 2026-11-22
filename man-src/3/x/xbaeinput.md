---
title: "xbaeinput(3)"
name: "xbaeinput"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xbaeinput/"
description: "XbaeInput – The Input widget class."
---

<p>XbaeInput &#8211; The Input widget class.</p>
<h2>Synopsis</h2>
<p>#include &lt;Xbae/Input.h&gt;</p>
<h2>Description</h2>
<p><code>XbaeInput</code> is a text input field that provides generic customised data entry and formatting for strings. It does this by using a clever <code>XmNmodifyVerifyCallback</code> that is installed when the <code>XmNpattern</code> resource is set. The <code>XmNpattern</code> value may include optional characters and literals which will be discussed later in this document. </p>
<p> The <code>XbaeInput</code> widget is ideal for restricting data input to a digit, alphanumeric character or an alphabetic character. If <code>XmNconvertCase</code> is set, the widget automatically changes an inserted character to uppercase or lowercase. Literal characters can also be included in the <code>XmNpattern</code> that can be automatically inserted as the user types by setting the <code>XmNautofill</code> resource to True. Optional literals cannot be auto inserted, however. </p>
<p> Unlike the <code>XmText</code> field from which this widget is subclassed, the <code>toggle-overwrite</code> action is bound to the <code>osfInsert</code> key. The <code>XmNoverwriteMode</code> is also provided to allow the resource to be changed programatically. </p>
<p> When the <code>XbaeInput</code> widget loses focus or is activated in the same way as the <code>XmText</code> field would be, callbacks on the XmNvalidateCallback list are invoked, allowing the programmer to validate the data as well as reformatting the existing string.</p>
<h3>Classes</h3>
<p><code>XbaeInput</code> inherits behavior and resources from the <code>Core</code>, <code>XmPrimitive</code>, and <code>XmText</code> widget classes.<br/>
 The class pointer is <code>xbaeInputWidgetClass</code>.<br/>
 The class name is <code>XbaeInput</code>.</p>
<h3>New Resources</h3>
<p>The following table lists the new resources defined by <code>XbaeInput</code>. The codes in the Access column indicate whether the given resource can be set at creation time (C), or set by using XtSetValues (S), or retrieved by using XtGetValues (G). </p>
<table BORDER>
<tr>
<td>
<table WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>XbaeInput Resource Set
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
<td>XmNalignment</td>
<td>XmCAlignment</td>
<td>unsigned char</td>
<td>XmALIGNMENT_BEGINNING</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNautoFill</td>
<td>XmCBoolean</td>
<td>Boolean</td>
<td>False</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNconvertCase</td>
<td>XmCBoolean</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNoverwriteMode</td>
<td>XmCBoolean</td>
<td>Boolean</td>
<td>False</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNpattern</td>
<td>XmCString</td>
<td>String</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNvalidateCallback</td>
<td>XmCCallback</td>
<td>Callback</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
</table>
</table>
<p> This resource has not been implemented. </p>
<dl COMPACT>
<dt><code>XmNalignment</code></dt>
<dd>This resource has not been implemented! </dd>
<p> Specifies the alignment of the text when being edited and displayed. Possible values are <code>XmALIGNMENT_BEGINNING</code>and <code>XmALIGNMENT_END</code>. If <code>XmNalignment</code> is set to <code>XmALIGNMENT_END</code>, the text will be right justified. If left as the default of <code>XmALIGNMENT_BEGINNING</code>, the text will be left justified.</p>
<dt><code>XmNautoFill</code></dt>
<dd>The <code>XmNautoFill</code> resource, when set to True, attempts to automatically insert a literal if a non literal is hit in an allowed literal position. For example, if the <code>XmNpattern</code> resource was set up to accept a date in dd/mm/yyyy format and the user typed &quot;18041999&quot; The resulting string would appear as &quot;18/04/1999&quot;. The default value is False, where the user would have to type the literal.</dd>
<dt><code>XmNconvertCase</code></dt>
<dd>Tells the <code>XbaeInput</code> widget what should be done to alphabetic characters if the requires a lowercase or uppercase letter. If the <code>XmNconvertCase</code> is set to True (default), then the character is automatically converted to the correct case. If set to False, then the user must type the character in the correct case in order for it to be accepted. See the <code>EXAMPLE PATTERNS</code> section towards the end of this document for some examples.</dd>
<dt><code>overwriteMode</code></dt>
<dd>Whether the widget accepts characters in insert mode or overwrite mode is controlled by the resource. Setting this resource calls the <code>XmText</code> <code>toggle-overwrite()</code> action routine, so the Motif toolkit being used must also support this routine.</dd>
<dt><code>XmNpattern</code></dt>
<dd>The <code>XmNpattern</code> resource specifies what can be typed into the <code>XbaeInput</code> widget. If set to the default value of NULL any character may be entered. The <code>XmNpattern</code> can be set to a string containing the following characters. </dd>
<table>
<tr VALIGN=top>
<td><code>a</code></td>
<td>alphabetic characters only
</td>
</tr>
<tr VALIGN=top>
<td><code>b</code></td>
<td>both &#8211; either digit or character
</td>
</tr>
<tr VALIGN=top>
<td><code>c</code></td>
<td>any character at all
</td>
</tr>
<tr VALIGN=top>
<td><code>d</code></td>
<td>digits only
</td>
</tr>
<tr VALIGN=top>
<td><code>U</code></td>
<td>upperchase character only
</td>
</tr>
<tr VALIGN=top>
<td><code>L</code></td>
<td>lowercase character only
</td>
</tr>
<tr VALIGN=top>
<td><code>[</code></td>
<td>start of optional sequence
</td>
</tr>
<tr VALIGN=top>
<td><code>]</code></td>
<td>end of optional sequence
</td>
</tr>
<tr VALIGN=top>
<td><code>\escapes the next character</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>|</code></td>
<td>next char is an alternative to previous. May be chained.
</td>
</tr>
</table>
</dl>
<h3>Inherited Resources</h3>
<p>The following table lists the resources which <code>XbaeInput</code> inherits from it&#8217;s superclasses <code>XmText</code>, <code>XmPrimitive and</code> <code>Core</code>. For a complete description of each resource, refer to the man page for that superclass. The codes in the &quot;Access&quot; column indicate whether the given resource can be set at creation time (C), or set by using XtSetValues (S), or retrieved by using XtGetValues (G). </p>
<table BORDER>
<tr>
<td>
<table WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>XmText Resource Set
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
<td>XmNautoShowCursorPosition</td>
<td>XmCAutoShowCursorPosition</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNcursorPosition</td>
<td>XmCCursorPosition</td>
<td>XmTextPosition</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNeditable</td>
<td>XmCEditable</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNeditMode</td>
<td>XmCEditMode</td>
<td>int</td>
<td>XmSINGLE_LINE_EDIT</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfocusCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNgainPrimaryCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlosePrimaryCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlosingFocusCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmarginHeight</td>
<td>XmCMarginHeight</td>
<td>Dimension</td>
<td>5</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmarginWidth</td>
<td>XmCMarginWidth</td>
<td>Dimension</td>
<td>5</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmaxLength</td>
<td>XmCMaxLength</td>
<td>int</td>
<td>largest integer</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmodifyVerifyCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmodifyVerifyCallbackWcs</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmotionVerifyCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsource</td>
<td>XmCSource</td>
<td>XmTextSource</td>
<td>Default source</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtopCharacter</td>
<td>XmCTextPosition</td>
<td>XmTextPosition</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNvalue</td>
<td>XmCValue</td>
<td>String</td>
<td>&quot;&quot;</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNvalueChangedCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNvalueWcs</td>
<td>XmCvalueWcs</td>
<td>wchar_t *</td>
<td>(wchar_t *)&quot;&quot;</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNverifyBell</td>
<td>XmCVerifyBell</td>
<td>Boolean</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td>
<table WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>XmPrimitive Resource Set
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
<td>XmNbottomShadowColor</td>
<td>XmCBottomShadowColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightOnEnter</td>
<td>XmCHighlightOnEnter</td>
<td>Boolean</td>
<td>False</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightThickness</td>
<td>XmCHighlightThickness</td>
<td>Dimension</td>
<td>2</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnavigationType</td>
<td>XmCNavigationType</td>
<td>XmNavigationType</td>
<td>XmNONE</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNshadowThickness</td>
<td>XmCShadowThickness</td>
<td>Dimension</td>
<td>2</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNunitType</td>
<td>XmCUnitType</td>
<td>unsignedChar</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNuserData</td>
<td>XmCUserData</td>
<td>Pointer</td>
<td>NULL</td>
<td>CSG
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
<td>XmNaccelerators</td>
<td>XmCAccelerators</td>
<td>XtAccelerators</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
<td>1</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNscreen</td>
<td>XmCScreen</td>
<td>Screen</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
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
</table>
</table>
<h3>Callback Information</h3>
<dl COMPACT>
<dt><code>XmNvalidateCallback</code></dt>
<dd>Callbacks on the <code>XmNvalidateCallback</code> list are called when the edits to the <code>XbaeInput</code> widget are activated or a losing focus event occurs. Each callback function is passed the following structure: </dd>
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
<td><code>int</code></td>
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
<td><code>String</code></td>
<td><i>pattern;</i>
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
<td COLSPAN=3><code>} XbaeInputValidateCallbackStruct;</code>
</td>
</tr>
</table>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt><i>reason</i></dt>
<dd>Set to <code>XmCR_ACTIVATE</code> if the user caused the callback to be invoked by activating the changes in the cell or <code>XmCR_LOSING_FOCUS</code> if the callback was called due to a losing focus event.</dd>
<dt><i>event</i></dt>
<dd>The event pointer that triggered the callback.</dd>
<dt><i>pattern</i></dt>
<dd>A pointer to the pattern for the <code>XbaeInput</code> widget or NULL if one does not exist. This value is provided as a convenience to the callback.</dd>
<dt><i>value</i></dt>
<dd>The value as it appears in the cell at the time of the callback being invoked.</dd>
<dt><i>doit</i></dt>
<dd>Indicates whether or not the value is valid. By setting <i>doit</i> to False the value will not be accepted.</dd></dl>
<p> This callback provides the application of checking the validity of the value entered into the <code>XbaeInput</code> widget. Checking the validity of a date may be one such instance. If the value is verified as valid, all values of the callback may be left unchanged. If the pointer to the value is changed, the new value will be displayed in the cell and storage for the old value deallocated by the <code>XbaeInput</code> widget. The new value&#8217;s memory is owned by the application and it is up to the application to use XtFree to deallocate it. </p>
<p> If the <i>value</i> is not considered valid, the <i>doit</i> flag should be set to False, forcing the user to make changes before the value can be accepted.</dl>
</dl>
<h3>Translations</h3>
<p><code>XbaeInput</code> inherits translations from <code>XmText</code>. Some versions of Motif do not have the </p>
<table>
<tr VALIGN=top>
<td>:&lt;Key&gt;osfInsert:</td>
<td>toggle-overstrike()
</td>
</tr>
</table>
<p> translation installed by default. If this is the case, <code>XbaeInput</code> automatically registers this translation. </p>
<h3>Type Converters</h3>
<p><code>XbaeInput</code> does not define any new type converters other than the standard type converters registered by Xt and Motif. </p>
<h3>Public Functions</h3>
<p>The following external entry points to <code>XbaeInput</code> class methods are defined: </p>
<p> <code>XbaeCreateInput()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>Widget XbaeCreateInput()
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
</dd><dl COMPACT>
<dt><i>parent</i></dt>
<dd>Specifies the parent widget ID.</dd>
<dt><i>name</i></dt>
<dd>Specifies the name of the created widget</dd>
<dt><i>arglist</i></dt>
<dd>Specifies the argument list</dd>
<dt><i>argcount</i></dt>
<dd>Specifies the number of attribute/value pairs in the argument list (arglist)</dd></dl>
<p> <code>XbaeCreateInput()</code> creates an instance of an XbaeInput widget and returns the associated widget ID.</dl>
<h3>Example Patterns</h3>
<dl COMPACT>
<dt><code>d[d]/d[d]/dd[dd]</code></dt>
<dd>A date that would accept 1/1/99, 12/1/99, 1/12/1999, 01/01/2000, etc.</dd>
<dt><code>U[L][L][L][L][L], U[L][L][L][L][L]</code></dt>
<dd>&quot;Surname, Firstname&quot; combination, automatically forcing correct case and allowing between 1 and 6 characters per name.</dd>
<dt><code>UU-dd[d][d]</code></dt>
<dd>A flight number consisting of two uppercase letters and 2 to 4 numbers</dd>
<dt><code>(ddd)&nbsp;<wbr>ddd-dddd</code></dt>
<dd>An American style phone number</dd>
<dt><code>UdU[-]dUd</code></dt>
<dd>A Canadian postcode with optional dash.</dd></dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code>VirtualBindings(3X)</code>.</p>
<h2>Author</h2>
<p><code>Andrew Lister</code> (lister [at] db.com) </p>
<h2>Release</h2>
<p>This document describes XbaeInput from Xbae Version 4.9.</p>
<h2>See Also</h2>
<p><code>Core(3X), XmPrimitive(3X), XmText(3X)</code></p>
<h2>Notice of Limitation</h2>
<p>The Author, previous and current maintainers of the Xbae widgets (collectively &#8216;authors&#8217;) provide this information solely to professionals who have the appropriate degree of experience to understand and interpret its contents in accordance with generally accepted engineering or other professional standards and applicable regulations. No recommendations as to products or vendors is made or should be implied. </p>
<p> While the information contained herein has been prepared from sources deemed to be reliable, the authors reserve the right to revise the information without notice, but have no obligation to do so. Unless the recipient has been expressly granted a license by Bellcore under separate applicable written agreement with Bellcore, no license, expressed or implied, is granted under any patents, copyrights or other intellectual property rights. Use of the information is at your discretion and shall not be deemed an inducement by Bellcore to infringe any existing or later-issued patent, copyrights or other intellectual property right. </p>
<p> THE AUTHORS MAKE NO REPRESENTATIONS AND EXTENDS NO WARRANTIES, EXPRESS OR IMPLIED, WITH RESPECT TO THE INFORMATION, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR ANY PARTICULAR PURPOSE, AND THE WARRANTY AGAINST INFRINGEMENT OF PATENTS OR OTHER INTELLECTUAL PROPERTY RIGHTS. THE INFORMATION IS PROVIDED &#8220;AS IS&#8221;, AND IN NO EVENT SHALL THE AUTHORS OR ANY OF ITS AFFILIATES BE LIABLE FOR ANY DAMAGES, INCLUDING ANY LOST PROFITS OR OTHER INCIDENTAL OR CONSEQUENTIAL DAMAGES RELATING TO THE INFORMATION. </p>
<p> Copyright 1999 Andrew Lister. All Rights Reserved.<br/>
 Copyright 1999-2002 LessTif Developers </p>
<p> The above no warranty extends to all additions and contributions. No contributor shall be held liable; this work is provided &#8220;as is&#8221;. If this is a problem for you, then don&#8217;t use this software.</p>
