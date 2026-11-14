---
title: "xmfontselector(3)"
name: "xmfontselector"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontselector/"
---

The Font Selector widget
<h2>Synopsis</h2>#include &lt;Xm/FontS.h&gt;
<h2>Description</h2><table> <tr VALIGN=top></tr><tr VALIGN=top><td><font SIZE="+9">&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></font></td></tr> </table> 

 The Font Selector widget allows users to easily choose a font by selecting the font family and size of the font. The bold and italic attributes may also be set for any font for which they are available. Any font may be passed to the font selector by the application as the initial value shown to the user. Advanced features greatly extend the widget's functionality. 

<h2>Basic Features</h2>The font selector widget presents the user with two combination box widgets, one with a list of choices for the font family, and the other with the choices for the font size. In addition there are two independent toggle buttons that allow the user to make the font bold or italic or bold/italic. Below the font choice area is a text widget that displays sample text of the chosen font to the user. This text area is editable, allowing the user to add or remove text to see how various characters appear in the chosen font. For the novice user this set of features allows access to all standard fonts on the system. The font selector dynamically removes choices that are inappropriate so the user is free to play around with different combinations and can always be assured that once they have selected a font that it will exist on the machine that the font selector is running on. For example if there is no Times Roman 14 point font available, and the user selects a point size of 14, then Times Roman will not be available in the family combination box. Likewise, if the user had chosen Times Roman from the family dialog box then a size of 14 would not be shown. To have all choices available simply choose a size and family of Any. 

<h2>Advanced Features</h2>For the advanced user the font selector provides tremendous flexibility in font choices. By activating the options button an additional panel of controls is presented to the user. This allows the user to gain access to non-XLFD fonts, control the resolutions of the fonts chosen, choose from fixed or proportional fonts only, remove the use of font scaling, allow non iso8859-1 fonts to be viewed, and see the XLFD name the font selector is constructing. 

<h2>Non XLFD Fonts</h2>By choosing the &quot;Other Fonts&quot; toggle from the option panel, the family and size lists, as well as the bold and italic toggles, are replaced with a combo box containing all non-XLFD fonts available on your system. This feature allows users to select non-XLFD fonts with the FontSelector. The text field of the combination box may be edited by the user and any string entered will be interpreted as a font name. It should be noted that XLFD names can be typed in by hand here. This feature allows the font selector to be used to get any font on the entire system. 

<h2>Resolution Control</h2>The font selector finds which of the two standard resolutions the current display is closest to and uses that as its default. To allow a wider range of choices a user may choose to access fonts of a different resolution, or both 75 and 100 dpi resolutions. 

<h2>Fixed or Proportional</h2>In most cases the fact that a font is fixed width or proportional is of no great interest to the user. But some applications require a fixed width font, such as terminal emulators, and most people find that proportional fonts look better. The Font selector allows users to limit the font choices to fixed width or proportional or to allow both. 

<h2>Font Scaling</h2>The font scaling technology that is available in X11R5 uses bitmap scaling which, although useful in some cases, generally results in very ugly fonts. We noticed that users often wanted to know which fonts are scaled and which ones exist as hand crafted bitmaps. To remove the scaled fonts from the list of choices, toggle the &quot;Use Font Scaling&quot; button off. This value is resource controllable and defaults to on, which uses font scaling. 

<h2>Encoding</h2>The programmer can specify which encidings are valid selctions. These encoding choices appear in an option menu. The list of font choices is restricted to those which use the current selected coding. 

<h2>XLFD Name Display</h2>Clicking the Show toggle displays the current font's XLFD name is shown at the bottom of the font selector. 

<h2>Normal Resources</h2><table> <tr VALIGN=top><td>Name</td><td>Class</td><td>Type</td><td>InitialValue
</td></tr><tr VALIGN=top><td>100DPIstring</td><td>100DPIString</td><td>XmString</td><td>&quot;100 dpi&quot;
</td></tr><tr VALIGN=top><td>75DPIstring</td><td>75DPIString</td><td>XmString</td><td>&quot;75 dpi&quot;
</td></tr><tr VALIGN=top><td>anyLowerString</td><td>AnyLowerString</td><td>XmString</td><td>&quot;any&quot;
</td></tr><tr VALIGN=top><td>anyString</td><td>AnyString</td><td>XmString</td><td>&quot;Any&quot;
</td></tr><tr VALIGN=top><td>boldString</td><td>BoldString</td><td>XmString</td><td>&quot;Bold&quot;
</td></tr><tr VALIGN=top><td>bothString</td><td>BothString</td><td>XmString</td><td>&quot;Both&quot;
</td></tr><tr VALIGN=top><td>currentFont</td><td>String</td><td>String</td><td>NULL
</td></tr><tr VALIGN=top><td>defaultEncodingString</td><td>DefaultEncodingString</td><td>String</td><td>&quot;iso8859-1&quot;
</td></tr><tr VALIGN=top><td>encodingList</td><td>EncodingList</td><td>StringTable</td><td>&quot;iso8859-1&quot;
</td></tr><tr VALIGN=top><td>encodingString</td><td>EncodingString</td><td>XmString</td><td>&quot;Encoding&quot;
</td></tr><tr VALIGN=top><td>familyString</td><td>BothString</td><td>XmString</td><td>&quot;Family&quot;
</td></tr><tr VALIGN=top><td>italicString</td><td>ItalicString</td><td>XmString</td><td>&quot;Italic&quot;
</td></tr><tr VALIGN=top><td>marginHeight</td><td>Margin</td><td>Dimension</td><td>0
</td></tr><tr VALIGN=top><td>monoSpaceString</td><td>MonoSpaceString</td><td>XmString</td><td>&quot;Fixed Width
</td></tr><tr VALIGN=top><td></td><td></td><td></td><td> Fonts&quot;
</td></tr><tr VALIGN=top><td>optionString</td><td>OptionString</td><td>XmString</td><td>&quot;Options ...&quot;
</td></tr><tr VALIGN=top><td>otherString</td><td>OtherString</td><td>XmString</td><td>&quot;Other Fonts&quot;
</td></tr><tr VALIGN=top><td>propSpaceString</td><td>PropSpaceString</td><td>XmString</td><td>&quot;Proportional
</td></tr><tr VALIGN=top><td></td><td></td><td></td><td> Fonts&quot;
</td></tr><tr VALIGN=top><td>sampleText</td><td>SampleText</td><td>XmString</td><td>&quot;abcdef...&quot;
</td></tr><tr VALIGN=top><td>scalingString</td><td>ScalingString</td><td>XmString</td><td>&quot;Use Font
</td></tr><tr VALIGN=top><td></td><td></td><td></td><td> Scaling&quot;
</td></tr><tr VALIGN=top><td>showFontName</td><td>ShowFontName</td><td>Boolean</td><td>False
</td></tr><tr VALIGN=top><td>showNameString</td><td>ShowNameString</td><td>XmString</td><td>&quot;Show Font
</td></tr><tr VALIGN=top><td></td><td></td><td></td><td> Name&quot;
</td></tr><tr VALIGN=top><td>sizeString</td><td>SizeString</td><td>XmSring</td><td>&quot;Size&quot;
</td></tr><tr VALIGN=top><td>spacing</td><td>Spacing</td><td>Dimension</td><td>2
</td></tr><tr VALIGN=top><td>textRows</td><td>TextRows</td><td>Dimension</td><td>8
</td></tr><tr VALIGN=top><td>useScaling</td><td>Boolean</td><td>Boolean</td><td>True
</td></tr><tr VALIGN=top><td>valueChangedCallback</td><td>Callback</td><td>XtCallbackList</td><td>NULL
</td></tr><tr VALIGN=top><td>xlfdString</td><td>XlfdString</td><td>XmString</td><td>&quot;Xlfd Fonts&quot;
</td></tr> </table> 

 All resource names begin with XmN and all resource class names begin with XmC. 

<h2>100DPSString</h2>The label for the 100 DPI radio button. 

<h2>75DPSString</h2>The label for the 75 DPI radio button. 

<h2>anyLowerString</h2>The label for the any button. 

<h2>anyString</h2>The label for the Any button. 

<h2>boldString</h2>The label for the Bold toggle button. 

<h2>bothString</h2>The labels for the Both radio buttons controlling both the dpi and width of the fonts displayed. The same resource is used to ensure consistent labels. 

<h2>currentFont</h2>This resource provides the main application input and output to the font selector. If the programmer sets the value at creation time or with XtSetValues then the currently displayed family, size, bold and italic will be changed to correspond to the values shown in the current font. Otherwise, the name of the font will be shown. The Font Selector's mode will be set to correspond to the type of font passed. 

 Note: currentFont must contain 14 hyphens (-) to be considered an XLFD font. This resource is also used to retrieve the font the user has selected from the font selector. The value returned is only valid until the next time XtGetValues is called on this instance of the font selector widget. 

<h2>defaultEncodingString</h2>This resource is the default selection from the Encoding options menu. 

<h2>encodingList</h2>This resource is the list of encodings available from the FontSelector Encoding options menu. 

<h2>encodingString</h2>This resource is the default selection from the Encoding options menu. 

<h2>familyString</h2>This resource is the default selection from the Family options menu. 

<h2>isoFontsOnly</h2>This resource controls and maintains the state of the iso8859-1 fonts only toggle button. 

<h2>italicString</h2>This resource is the default selection from the Italic toggle button. 

<h2>marginHeight</h2>The margin height for all subwidgets of the Font Selector. 

<h2>monoSpaceString</h2>The label of the Fixed Width Fonts radio button. 

<h2>optionString</h2>The label for the Options... push button. 

<h2>otherString</h2>The label for the Other Fonts radio button. 

<h2>propSpaceString</h2>The label for the Proportional Fonts radio button. 

<h2>sampleText</h2>The string which appears in the sample text area. 

<h2>scalingString</h2>The label for the Use Font Scaling toggle button. 

<h2>showFontName</h2>This boolean resource controls and maintains the state of Show Font Name toggle button. 

<h2>showNameString</h2>The label of the Show Font Name toggle button. 

<h2>sizeString</h2>The label for the Size option menu. 

<h2>spacing</h2>The space between the toggle indicator and the toggle label. 

<h2>textRows</h2>This resource controls the number of rows that are shown in the text widget that displays sample text in the currently selected font. Since this is a scrolled text widget it will never dynamically change size, regardless of the font displayed. Unless the initial font is large this value should be at least 4 or the user interaction may be poor. 

<h2>useScaling</h2>This resource controls and maintains the state of the Use Font Scaling toggle button. 

<h2>valueChangedCallback</h2>The list of callbacks called when the XmNcurrentFont value is changed. 

<h2>xlfdString</h2>The label for the Xlfd Fonts radio button. 

<h2>Convenience Routine</h2><h2>
<dt></h2></dl><h2>XmCreateFontSelector - Widget creation convenience routine</h2><pre><dd>Widget XmCreateFontSelector( 
 Widget parent, /* Widget id of parent for FontSelector */
 String name, /* Name of the created widget */
 ArgList args, /* argument list */
 Cardinal num_args /* number of items in argument list */
 ) </pre><h2>Children</h2>The font selector is composed of many sub-widgets. As with all widgets, most values passed to this widget through the argument list at creation time or via set values are passed to each of this widget's children. Get values requests must be made on a child by child basis. The children of the font selector are listed below. The documentation for each of the children should be consulted for a list of resources for each child. 

 XiFontSelector&lt;named by application&gt;
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XiPanedtopPane
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmComboBoxfamilies
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt; See XmComboBox for list of children &gt;
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmSeparatorseparator
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XiComboBoxsizes
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt; See XmComboBox for list of children &gt;
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmSeparatorseparator
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmButtonBoxboldItalicBox
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtonboldButton
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtonitalicButton
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmSeparatorseparator
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtonoptionButton
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmSeparatorseparator
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmPanedmiddlePane
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmPanedleftPane
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmButtonBoxchoiceBox
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtonxlfdButton
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtonotherButton
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmSeparatorseparator
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmButtonBoxresolutionBox
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtondpi75Button
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtondpi100Button
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtonanyButton
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmSeparatorseparator
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmSeparatorseparator
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmButtonBoxspacingBox
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtonproportionalButton
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtonmonoButton
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtonbothButton
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmSeparatorseparator
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmButtonBoxotherChoiceBox
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtonscalingButton
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtonisoButton
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtonshowNameButton
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmRowColum encodingOptionMenu
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmLabelGadget OptionLabel 
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmCascadeButtonGadget OptionButton
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmMenuShell menuShell
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmRowColum pulldownMenu
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;dependent on XmNencoding&gt;
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmSeparatorseparator
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmSeparatorseparator
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmButtonBoxbox
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmScrolledWindowtextSW
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmScrollBarvbar
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmTexttext
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmSeparatorseparator
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmLabelnameLabel
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmSeparatorseparator
 

<h2>Copyright</h2>Copyright (c) 1992 by Integrated Computer Solutions, Inc.
