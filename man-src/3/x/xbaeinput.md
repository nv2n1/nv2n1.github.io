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
<p><code>XbaeInput</code> inherits behavior and resources from the <code>Core</code>, <code>XmPrimitive</code>, and <code>XmText</code> widget classes.<br />
 The class pointer is <code>xbaeInputWidgetClass</code>.<br />
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
<td><font SIZE="-9">XmNalignment</font></td>
<td><font SIZE="-9">XmCAlignment</font></td>
<td><font SIZE="-9">unsigned char</font></td>
<td><font SIZE="-9">XmALIGNMENT_BEGINNING</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNautoFill</font></td>
<td><font SIZE="-9">XmCBoolean</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNconvertCase</font></td>
<td><font SIZE="-9">XmCBoolean</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNoverwriteMode</font></td>
<td><font SIZE="-9">XmCBoolean</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNpattern</font></td>
<td><font SIZE="-9">XmCString</font></td>
<td><font SIZE="-9">String</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNvalidateCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
</table>
</table>
<p> This resource has not been implemented. </p>
<dl COMPACT>
<dt><code>XmNalignment</code></p>
<dd>This resource has not been implemented! </p>
<p> Specifies the alignment of the text when being edited and displayed. Possible values are <code>XmALIGNMENT_BEGINNING</code>and <code>XmALIGNMENT_END</code>. If <code>XmNalignment</code> is set to <code>XmALIGNMENT_END</code>, the text will be right justified. If left as the default of <code>XmALIGNMENT_BEGINNING</code>, the text will be left justified.</p>
<dt><code>XmNautoFill</code></p>
<dd>The <code>XmNautoFill</code> resource, when set to True, attempts to automatically insert a literal if a non literal is hit in an allowed literal position. For example, if the <code>XmNpattern</code> resource was set up to accept a date in dd/mm/yyyy format and the user typed &quot;18041999&quot; The resulting string would appear as &quot;18/04/1999&quot;. The default value is False, where the user would have to type the literal.</p>
<dt><code>XmNconvertCase</code></p>
<dd>Tells the <code>XbaeInput</code> widget what should be done to alphabetic characters if the requires a lowercase or uppercase letter. If the <code>XmNconvertCase</code> is set to True (default), then the character is automatically converted to the correct case. If set to False, then the user must type the character in the correct case in order for it to be accepted. See the <code>EXAMPLE PATTERNS</code> section towards the end of this document for some examples.</p>
<dt><code>overwriteMode</code></p>
<dd>Whether the widget accepts characters in insert mode or overwrite mode is controlled by the resource. Setting this resource calls the <code>XmText</code> <code>toggle-overwrite()</code> action routine, so the Motif toolkit being used must also support this routine.</p>
<dt><code>XmNpattern</code></p>
<dd>The <code>XmNpattern</code> resource specifies what can be typed into the <code>XbaeInput</code> widget. If set to the default value of <font SIZE="-1">NULL</font> any character may be entered. The <code>XmNpattern</code> can be set to a string containing the following characters. </p>
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
<td><font SIZE="-9">XmNautoShowCursorPosition</font></td>
<td><font SIZE="-9">XmCAutoShowCursorPosition</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcursorPosition</font></td>
<td><font SIZE="-9">XmCCursorPosition</font></td>
<td><font SIZE="-9">XmTextPosition</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNeditable</font></td>
<td><font SIZE="-9">XmCEditable</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNeditMode</font></td>
<td><font SIZE="-9">XmCEditMode</font></td>
<td><font SIZE="-9">int</font></td>
<td><font SIZE="-9">XmSINGLE_LINE_EDIT</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNfocusCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">XtCallbackList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNgainPrimaryCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">XtCallbackList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNlosePrimaryCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">XtCallbackList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNlosingFocusCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">XtCallbackList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNmarginHeight</font></td>
<td><font SIZE="-9">XmCMarginHeight</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">5</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNmarginWidth</font></td>
<td><font SIZE="-9">XmCMarginWidth</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">5</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNmaxLength</font></td>
<td><font SIZE="-9">XmCMaxLength</font></td>
<td><font SIZE="-9">int</font></td>
<td><font SIZE="-9">largest integer</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNmodifyVerifyCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">XtCallbackList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNmodifyVerifyCallbackWcs</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">XtCallbackList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNmotionVerifyCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">XtCallbackList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNsource</font></td>
<td><font SIZE="-9">XmCSource</font></td>
<td><font SIZE="-9">XmTextSource</font></td>
<td><font SIZE="-9">Default source</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtopCharacter</font></td>
<td><font SIZE="-9">XmCTextPosition</font></td>
<td><font SIZE="-9">XmTextPosition</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNvalue</font></td>
<td><font SIZE="-9">XmCValue</font></td>
<td><font SIZE="-9">String</font></td>
<td><font SIZE="-9">&quot;&quot;</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNvalueChangedCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">XtCallbackList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNvalueWcs</font></td>
<td><font SIZE="-9">XmCvalueWcs</font></td>
<td><font SIZE="-9">wchar_t *</font></td>
<td><font SIZE="-9">(wchar_t *)&quot;&quot;</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNverifyBell</font></td>
<td><font SIZE="-9">XmCVerifyBell</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
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
<td><font SIZE="-9">XmNbottomShadowColor</font></td>
<td><font SIZE="-9">XmCBottomShadowColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNbottomShadowPixmap</font></td>
<td><font SIZE="-9">XmCBottomShadowPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">XmUNSPECIFIED_PIXMAP</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNforeground</font></td>
<td><font SIZE="-9">XmCForeground</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNhighlightColor</font></td>
<td><font SIZE="-9">XmCHighlightColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNhighlightOnEnter</font></td>
<td><font SIZE="-9">XmCHighlightOnEnter</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">False</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNhighlightPixmap</font></td>
<td><font SIZE="-9">XmCHighlightPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNhighlightThickness</font></td>
<td><font SIZE="-9">XmCHighlightThickness</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">2</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNnavigationType</font></td>
<td><font SIZE="-9">XmCNavigationType</font></td>
<td><font SIZE="-9">XmNavigationType</font></td>
<td><font SIZE="-9">XmNONE</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNshadowThickness</font></td>
<td><font SIZE="-9">XmCShadowThickness</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">2</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtopShadowColor</font></td>
<td><font SIZE="-9">XmCTopShadowColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtopShadowPixmap</font></td>
<td><font SIZE="-9">XmCTopShadowPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtraversalOn</font></td>
<td><font SIZE="-9">XmCTraversalOn</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNunitType</font></td>
<td><font SIZE="-9">XmCUnitType</font></td>
<td><font SIZE="-9">unsignedChar</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNuserData</font></td>
<td><font SIZE="-9">XmCUserData</font></td>
<td><font SIZE="-9">Pointer</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
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
<td><font SIZE="-9">XmNaccelerators</font></td>
<td><font SIZE="-9">XmCAccelerators</font></td>
<td><font SIZE="-9">XtAccelerators</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNancestorSensitive</font></td>
<td><font SIZE="-9">XmCSensitive</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">G</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNbackground</font></td>
<td><font SIZE="-9">XmCBackground</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNbackgroundPixmap</font></td>
<td><font SIZE="-9">XmCPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">XmUNSPECIFIED_PIXMAP</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNborderColor</font></td>
<td><font SIZE="-9">XmCBorderColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">XtDefaultForeground</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNborderPixmap</font></td>
<td><font SIZE="-9">XmCPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">XmUNSPECIFIED_PIXMAP</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNborderWidth</font></td>
<td><font SIZE="-9">XmCBorderWidth</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">1</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolormap</font></td>
<td><font SIZE="-9">XmCColormap</font></td>
<td><font SIZE="-9">Colormap</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNdepth</font></td>
<td><font SIZE="-9">XmCDepth</font></td>
<td><font SIZE="-9">int</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNdestroyCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">XtCallbackList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">C</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNheight</font></td>
<td><font SIZE="-9">XmCHeight</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNinitialResourcesPersistent</font></td>
<td><font SIZE="-9">XmCInitialResourcesPersistent</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">C</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNmappedWhenManaged</font></td>
<td><font SIZE="-9">XmCMappedWhenManaged</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNscreen</font></td>
<td><font SIZE="-9">XmCScreen</font></td>
<td><font SIZE="-9">Screen</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNsensitive</font></td>
<td><font SIZE="-9">XmCSensitive</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtranslations</font></td>
<td><font SIZE="-9">XmCTranslations</font></td>
<td><font SIZE="-9">XtTranslations</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNwidth</font></td>
<td><font SIZE="-9">XmCWidth</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNx</font></td>
<td><font SIZE="-9">XmCPosition</font></td>
<td><font SIZE="-9">Position</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNy</font></td>
<td><font SIZE="-9">XmCPosition</font></td>
<td><font SIZE="-9">Position</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
</table>
</table>
<h3>Callback Information</h3>
<dl COMPACT>
<dt><code>XmNvalidateCallback</code></p>
<dd>Callbacks on the <code>XmNvalidateCallback</code> list are called when the edits to the <code>XbaeInput</code> widget are activated or a losing focus event occurs. Each callback function is passed the following structure: </p>
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
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Set to <code>XmCR_ACTIVATE</code> if the user caused the callback to be invoked by activating the changes in the cell or <code>XmCR_LOSING_FOCUS</code> if the callback was called due to a losing focus event.</p>
<dt><i>event</i></p>
<dd>The event pointer that triggered the callback.</p>
<dt><i>pattern</i></p>
<dd>A pointer to the pattern for the <code>XbaeInput</code> widget or <font SIZE="-1">NULL</font> if one does not exist. This value is provided as a convenience to the callback.</p>
<dt><i>value</i></p>
<dd>The value as it appears in the cell at the time of the callback being invoked.</p>
<dt><i>doit</i></p>
<dd>Indicates whether or not the value is valid. By setting <i>doit</i> to False the value will not be accepted.</dl>
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
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (arglist)</dl>
<p> <code>XbaeCreateInput()</code> creates an instance of an XbaeInput widget and returns the associated widget ID.</dl>
<h3>Example Patterns</h3>
<dl COMPACT>
<dt><code>d[d]/d[d]/dd[dd]</code></p>
<dd>A date that would accept 1/1/99, 12/1/99, 1/12/1999, 01/01/2000, etc.</p>
<dt><code>U[L][L][L][L][L], U[L][L][L][L][L]</code></p>
<dd>&quot;Surname, Firstname&quot; combination, automatically forcing correct case and allowing between 1 and 6 characters per name.</p>
<dt><code>UU-dd[d][d]</code></p>
<dd>A flight number consisting of two uppercase letters and 2 to 4 numbers</p>
<dt><code>(ddd)&nbsp;<wbr>ddd-dddd</code></p>
<dd>An American style phone number</p>
<dt><code>UdU[-]dUd</code></p>
<dd>A Canadian postcode with optional dash.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="//www.systutorials.com/docs/linux/man/3X-VirtualBindings/">VirtualBindings</a>(3X)</code>.</p>
<h2>Author</h2>
<p><code>Andrew Lister</code> (lister [at] db.com) </p>
<h2>Release</h2>
<p>This document describes XbaeInput from Xbae Version 4.9.</p>
<h2>See Also</h2>
<p><code><a href="//www.systutorials.com/docs/linux/man/3X-Core/">Core</a>(3X), <a href="//www.systutorials.com/docs/linux/man/3X-XmPrimitive/">XmPrimitive</a>(3X), <a href="//www.systutorials.com/docs/linux/man/3X-XmText/">XmText</a>(3X)</code></p>
<h2>Notice of Limitation</h2>
<p>The Author, previous and current maintainers of the Xbae widgets (collectively &#8216;authors&#8217;) provide this information solely to professionals who have the appropriate degree of experience to understand and interpret its contents in accordance with generally accepted engineering or other professional standards and applicable regulations. No recommendations as to products or vendors is made or should be implied. </p>
<p> While the information contained herein has been prepared from sources deemed to be reliable, the authors reserve the right to revise the information without notice, but have no obligation to do so. Unless the recipient has been expressly granted a license by Bellcore under separate applicable written agreement with Bellcore, no license, expressed or implied, is granted under any patents, copyrights or other intellectual property rights. Use of the information is at your discretion and shall not be deemed an inducement by Bellcore to infringe any existing or later-issued patent, copyrights or other intellectual property right. </p>
<p> THE AUTHORS MAKE NO REPRESENTATIONS AND EXTENDS NO WARRANTIES, EXPRESS OR IMPLIED, WITH RESPECT TO THE INFORMATION, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR ANY PARTICULAR PURPOSE, AND THE WARRANTY AGAINST INFRINGEMENT OF PATENTS OR OTHER INTELLECTUAL PROPERTY RIGHTS. THE INFORMATION IS PROVIDED &#8220;AS IS&#8221;, AND IN NO EVENT SHALL THE AUTHORS OR ANY OF ITS AFFILIATES BE LIABLE FOR ANY DAMAGES, INCLUDING ANY LOST PROFITS OR OTHER INCIDENTAL OR CONSEQUENTIAL DAMAGES RELATING TO THE INFORMATION. </p>
<p> Copyright 1999 Andrew Lister. All Rights Reserved.<br />
 Copyright 1999-2002 LessTif Developers </p>
<p> The above no warranty extends to all additions and contributions. No contributor shall be held liable; this work is provided &#8220;as is&#8221;. If this is a problem for you, then don&#8217;t use this software.</p>
