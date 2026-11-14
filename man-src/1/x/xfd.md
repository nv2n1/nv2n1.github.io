---
title: "xfd(1)"
name: "xfd"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xfd/"
description: "xfd – display all the characters in an X font"
---

<h2 class="name">NAME</h2>
<p> xfd &#8211; display all the characters in an X font </p>
<h2>SYNOPSIS</h2>
<p> <code>xfd</code> [-options &#8230;] <code>-fn</code> <i>fontname</i> </p>
<p> <code>xfd</code> [-options &#8230;] <code>-fa</code> <i>fontname</i></p>
<h2>DESCRIPTION</h2>
<p> The <i>xfd</i> utility creates a window containing the name of the font being displayed, a row of command buttons, several lines of text for displaying character metrics, and a grid containing one glyph per cell. The characters are shown in increasing order from left to right, top to bottom. The first character displayed at the top left will be character number 0 unless the <code>-start</code> option has been supplied in which case the character with the number given in the <code>-start</code> option will be used. </p>
<p> The characters are displayed in a grid of boxes, each large enough to hold any single character in the font. Each character glyph is drawn using the PolyText16 request (used by the <i>Xlib</i> routine <code>XDrawString16</code>) or the XftDrawString32 routine, depending on whether the <code>-fn</code> or <code>-fa</code> option was given. If the <code>-box</code> option is given, a rectangle will be drawn around each character, showing where an ImageText16 request (used by the <i>Xlib</i> routine <code>XDrawImageString16</code>) would cause background color to be displayed. </p>
<p> The origin of each glyph is normally set so that the character is drawn in the upper left hand corner of the grid cell. However, if a glyph has a negative left bearing or an unusually large ascent, descent, or right bearing (as is the case with <i>cursor</i> font), some character may not appear in their own grid cells. The <code>-center</code> option may be used to force all glyphs to be centered in their respective cells. </p>
<p> All the characters in the font may not fit in the window at once. To see the next page of glyphs, press the <i>Next</i> button at the top of the window. To see the previous page, press <i>Prev</i>. To exit <i>xfd</i>, press <i>Quit</i>. </p>
<p> Individual character metrics (index, width, bearings, ascent and descent) can be displayed at the top of the window by clicking on the desired character. </p>
<p> The font name displayed at the top of the window is the full name of the font, as determined by the server. See <i>xlsfonts</i> and <i>fc-list</i> for ways to generate lists of fonts, as well as more detailed summaries of their metrics and properties.</p>
<h2>OPTIONS</h2>
<p> <i>xfd</i> accepts all of the standard toolkit command line options along with the additional options listed below:</p>
<dl>
<dt><code>-fn </code><i>font</i></p>
<dd> This option specifies the core X server side font to be displayed. This can also be set with the FontGrid <code>font</code> resource. A font must be specified.</p>
<dt><code>-fa </code><i>font</i></p>
<dd> This option specifies a Xft font to be displayed. This can also be set with the FontGrid <code>face</code> resource. A font pattern must be specified.</p>
<dt><code>-box</code></p>
<dd> This option indicates that a box should be displayed outlining the area that would be filled with background color by an ImageText request. This can also be set with the FontGrid <code>boxChars</code> resource. The default is False.</p>
<dt><code>-center</code></p>
<dd> This option indicates that each glyph should be centered in its grid. This can also be set with the FontGrid <code>centerChars</code> resource. The default is False.</p>
<dt><code>-start </code><i>number</i></p>
<dd> This option specifies the glyph index of the upper left hand corner of the grid. This is used to view characters at arbitrary locations in the font. This can also be set with the FontGrid <code>startChar</code> resource. The default is 0.</p>
<dt><code>-bc </code><i>color</i></p>
<dd> This option specifies the color to be used if ImageText boxes are drawn. This can also be set with the FontGrid <code>boxColor</code> resource.</p>
<dt><code>-rows </code><i>numrows</i></p>
<dd> This option specifies the number of rows in the grid. This can also be set with the FontGrid <code>cellRows</code> resource.</p>
<dt><code>-columns </code><i>numcols</i></p>
<dd> This option specifies the number of columns in the grid. This can also be set with the FontGrid <code>cellColumns</code> resource.</dl>
<h2>WIDGETS</h2>
<p> In order to specify resources, it is useful to know the widgets which compose <i>xfd</i>. In the notation below, indentation indicates hierarchical structure. The widget class name is given first, followed by the widget instance name. The application class name is Xfd. </p>
<pre>
Xfd  xfd
        Paned  pane
                Label  fontname
                Box  box
                        Command  quit
                        Command  prev
                        Command  next
                Label  select
                Label  metrics
                Label  range
                Label  start
                Form  form
                        FontGrid  grid
</pre>
<h2>FONTGRID RESOURCES</h2>
<p> The FontGrid widget is an application-specific widget, and a subclass of the Simple widget in the Athena widget set. The effects and instance names of this widget&#8217;s resources are given in the <code>OPTIONS</code> section. Capitalize the first letter of the resource instance name to get the corresponding class name.</p>
<h2>APPLICATION SPECIFIC RESOURCES</h2>
<p> The instance names of the application specific resources are given below. Capitalize the first letter of the resource instance name to get the corresponding class name. These resources are unlikely to be interesting unless you are localizing xfd for a different language.</p>
<dl>
<dt><code>selectFormat</code></p>
<dd> Specifies a printf-style format string used to display information about the selected character. The default is &quot;character 0x%02x%02x (%u,%u) (%#o,%#o)&quot;. The arguments that will come after the format string are char.byte1, char.byte2, char.byte1, char.byte2, char.byte1, char.byte2. char.byte1 is byte 1 of the selected character. char.byte2 is byte 2 of the selected character.</p>
<dt><code>metricsFormat</code></p>
<dd> Specifies a printf-style format string used to display character metrics. The default is &quot;width %d; left %d, right %d; ascent %d, descent %d (font %d, %d)&quot;. The arguments that will come after the format string are the character metrics width, lbearing, rbearing, character ascent, character descent, font ascent, and font descent.</p>
<dt><code>rangeFormat</code></p>
<dd> Specifies a printf-style format string used to display the range of characters currently being displayed. The default is &quot;range: 0x%02x%02x (%u,%u) thru 0x%02x%02x (%u,%u)&quot;. The arguments that will come after the format string are the following fields from the XFontStruct that is returned from opening the font: min_byte1, min_char_or_byte2, min_byte1, min_char_or_byte2, max_byte1, max_char_or_byte2, max_byte1, max_char_or_byte2.</p>
<dt><code>startFormat</code></p>
<dd> Specifies a printf-style format string used to display information about the character at the upper left corner of the font grid. The default is &quot;upper left: 0x%04x (%d,%d)&quot;. The arguments that will come after the format string are the new character, the high byte of the new character, and the low byte of the new character.</p>
<dt><code>nocharFormat</code></p>
<dd> Specifies a printf-style format string to display when the selected character does not exist. The default is &quot;no such character 0x%02x%02x (%u,%u) (%#o,%#o)&quot;. The arguments that will come after the format string are the same as for the <code>selectFormat</code> resource.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xlsfonts/">xlsfonts</a>(1), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1), <a href="/docs/linux/man/1-xfontsel/">xfontsel</a>(1), <a href="/docs/linux/man/1-fc-list/">fc-list</a>(1), <a href="/docs/linux/man/5-fonts-conf/">fonts.conf</a>(5), <i>X Logical Font Description Conventions</i></p>
<h2>BUGS</h2>
<p> The program should skip over pages full of non-existent characters.</p>
<h2>AUTHOR</h2>
<p> Jim Fulton, MIT X Consortium; previous program of the same name by Mark Lillibridge, MIT Project Athena. </p>
<h2>Index</h2>
