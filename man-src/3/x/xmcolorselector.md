---
title: "xmcolorselector(3)"
name: "xmcolorselector"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcolorselector/"
---

The Color Selector widget
<h2>Synopsis</h2>#include &lt;Xm/ColorS.h&gt;
<h2>Description</h2><table> <tr VALIGN=top></tr><tr VALIGN=top><td><font SIZE="+9">&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></font></td></tr> </table> 

 The Color Selector widget allows users to choose a color by using either a set of RGB sliders or choosing from a list of all colors available in the rgb database. The name or rgb value, as well as the color selected, are dynamically displayed to the user as they pick and choose different colors. 

<h2>Normal Resources</h2><table> <tr VALIGN=top><td>Name</td><td>Class</td><td>Type</td><td>Initial Value
</td></tr><tr VALIGN=top><td>blueSliderLabel</td><td>SliderLabel</td><td>XmString</td><td>&quot;Blue&quot;
</td></tr><tr VALIGN=top><td>colorListTogLabel</td><td>TogLabel</td><td>XmString</td><td>&quot;Color List&quot;
</td></tr><tr VALIGN=top><td>colorMode</td><td>ColorMode</td><td>XiColorMode</td><td>XmScaleMode
</td></tr><tr VALIGN=top><td>colorName</td><td>String</td><td>String</td><td>White
</td></tr><tr VALIGN=top><td>fileReadError</td><td>FileReadError</td><td>XmString</td><td>&quot;Could not read
</td></tr><tr VALIGN=top><td></td><td></td><td></td><td> RGB.txt file&quot;
</td></tr><tr VALIGN=top><td>greenSliderLabel</td><td>SliderLabel</td><td>XmString</td><td>&quot;Green&quot;
</td></tr><tr VALIGN=top><td>marginHeight</td><td>MarginHeight</td><td>VerticalDimension</td><td>2
</td></tr><tr VALIGN=top><td>marginWidth</td><td>MarginWidth</td><td>HorizontalDimension</td><td>2
</td></tr><tr VALIGN=top><td>noCellError</td><td>NoCellError</td><td>XmString</td><td>&quot;No Color Cell
</td></tr><tr VALIGN=top><td></td><td></td><td></td><td> Available&quot;
</td></tr><tr VALIGN=top><td>redSliderLabel</td><td>SliderLabel</td><td>XmString</td><td>&quot;Red&quot;
</td></tr><tr VALIGN=top><td>rgbFile</td><td>String</td><td>String</td><td>/usr/share/X11/rgb.txt
</td></tr><tr VALIGN=top><td>sliderTogLabel</td><td>TogLabel</td><td>XmString</td><td>&quot;Color Sliders&quot;
</td></tr> </table> 

 All resource names begin with XmN and all resource class names begin with XmC.
<h2>blueSliderLabel</h2>The string appearing for the label of the blue slider 

<h2>colorListTogLabel</h2>The string appearing for the label of the color list toggle 

<h2>colorMode</h2>The color list can be used in either slider or list mode. Acceptable values are XmListMode and XmScaleMode. This resource allows the application to determine the mode that the color selector should use when it is created. After this point, the user may freely change modes by utilizing a pair of radio buttons in the color selector. A type converter is registered to convert the strings &quot;ScaleMode&quot; and &quot;ListMode&quot; to color modes for use with the resource database. 

<h2>colorName</h2>This resource controls the color name that is currently displayed to the user. This value can be modified to change the color displayed in the color selector or queried to find the color the user has selected. The string returned here is either a color name or a pound sign (#) followed by a set of rgb values as specified in the Xlib specification. 

<h2>fileReadError</h2>The message which is displayed when the Color Selector cannot read the rgb.txt file. The message is displayed at the top of the window in which the color list would normally appear. 

<h2>greenSliderLabel</h2>The string appearing for the label of the green slider 

<h2>marginHeight</h2><h2>marginWidth</h2>This is the amount of space left between each of the children in the color selector and between the outside children and the edge of the color selector widget. 

<h2>noCellError</h2>This resource controls the message which is displayed in the sample color field when the Color Selector cannot allocate a read/write color cell 

<h2>redSliderLabel</h2>The string appearing for the label of the red slider 

<h2>rgbFile</h2>This is the name of the file to be loaded, which contains the valid color names. Each of these names is sorted and the duplicates removed before being shown to the user. 

<h2>sliderTogLabel</h2>The string appearing for the label of the color slider toggle 

<h2>Convenience Routine</h2><h2>
<dt></h2></dl><h2>XmCreateColorSelector - Widget creation convenience routine</h2><pre><dd>Widget XmCreateColorSelector( 
 Widget parent, /* Widget id of parent for ColorSelector */
 String name, /* Name of the created widget */
 ArgList args, /* argument list */
 Cardinal num_args /* number of items in argument list */
 ) </pre><h2>Children</h2>The color selector is composed of many sub-widgets. As with all widgets, most values are passed to this widget through the argument list at creation time or via set values and are passed to each of this widget's children, although get values requests must be made on a child-by-child basis. The children of the color selector are listed below. The documentation for each of the children should be consulted for a list of resources for each child. 

 

 XmColorSelector&lt;named by application&gt;
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmScrolledWindowscrolled
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmScrollBarListvScrollBar
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmScrollBarListhScrollBar
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmListlist
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmButtonBoxbuttonBox
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmScalescale
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmLabelGadgetscale_title
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmScrollBarscale_scrollbar
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmRowColumnradioBox
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtoncolorListToggle
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmToggleButtoncolorSlidersToggle
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmFramecolorFrame
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XmLabelcolorWindow 
 

<h2>Copyright</h2>Copyright (c) 1992 by Integrated Computer Solutions, Inc.
