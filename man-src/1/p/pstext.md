---
title: "pstext(1)"
name: "pstext"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pstext/"
description: "pstext – Plot or typeset text on maps"
---

<h2>NAME</h2>
<p> pstext &#8211; Plot or typeset text on maps</p>
<h2>SYNOPSIS</h2>
<p> <code>pstext</code> [ <i>textfiles</i> ] <i>parameters</i> <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>] [ ] [<code>p</code>|<code>s</code>]<i>parameters</i> [ [<code>j</code>|<code>J</code>]<i>dx</i>[/<i>dy</i>][<code>v</code>[<i>pen</i>]] ] [ [<code>+a</code>[<i>angle</i>]][<code>+c</code>[<i>justify</i>]][<code>+f</code>[<i>font</i>]][<code>+h</code>][<code>+j</code>[<i>justify</i>]][<code>+l</code>] ] [ <i>color</i> ] [ ((<code>z</code>|<code>Z</code><i>parameters</i> ] [ ] [ ] [ ] [ ] [ ] [ ] [ <code>l</code>|<code>u</code> ] [ <code>o</code>|<code>O</code>|<code>c</code>|<code>C</code> ] [ [ <i>pen</i> ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ ] [ <code>-a</code><i>col</i>=<i>name</i>[&#8230;] ] [ <code>-c</code><i>copies</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>pstext</code> plots text strings of variable size, font type, and orientation. Various map projections are provided, with the option to draw and annotate the map boundaries. PostScript code is written to standard output. Greek characters, subscript, superscript, and small caps are supported as follows: The sequence @~ toggles between the selected font and Greek (Symbol). @%<i>no</i>% sets the font to <i>no</i>; @%% resets the font to the starting font, @- toggles subscripts on/off, @+ toggles superscript on/off, @# toggles small caps on/off, @;<i>color</i>; changes the font color (@;; resets it), @:<i>size</i>: changes the font size (@:: resets it), and @_ toggles underline on/off. @@ prints the @ sign. @e, @o, @a, @E, @O, @A give the accented Scandinavian characters. Composite characters (overstrike) may be indicated with the @!&lt;char1&gt;&lt;char2&gt; sequence, which will print the two characters on top of each other. To learn the octal codes for symbols not available on the keyboard and some accented European characters, see Section <i>Char-esc-seq</i> and Appendix <i>Chart-Octal-Codes-for-Chars</i> in the GMT Technical Reference and Cookbook. Note that <i>PS_CHAR_ENCODING</i> must be set to an extended character set in your <code>gmt.conf</code> file in order to use the accented characters. Using the <code>-G</code> or <code>-W</code> options, a rectangle underlying the text may be plotted (does not work for strings with sub/super scripts, symbols, or composite characters, except in paragraph mode (<code>-M</code>)).</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i></dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>textfiles</i></p>
<dd> This is one or more files containing 1 or more records with (<i>x</i>, <i>y</i>[, <i>font</i>, <i>angle</i>, <i>justify</i>], <i>text</i>). The attributes in brackets can alternatively be set directly via <code>-F</code>. If no files are given, <code>pstext</code> will read standard input. <i>font</i> is a font specification with format [<i>size</i>,][<i>font</i>,][<i>color</i>] where <i>size</i> is text size in points, <i>font</i> is the font to use, and <i>color</i> sets the font color. To draw outline fonts you append =<i>pen</i> to the font specification. The <i>angle</i> is measured in degrees counter-clockwise from horizontal, and <i>justify</i> sets the alignment. If <i>font</i> is not an integer, then it is taken to be a text string with the desired font name (see <code>-L</code> for available fonts). The alignment refers to the part of the text string that will be mapped onto the (<i>x</i>,<i>y</i>) point. Choose a 2 character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left.</p>
<dt><code>-A</code></p>
<dd> Angles are given as azimuths; convert them to directions using the current projection.</p>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-C</code><i>dx/dy</i></p>
<dd> Sets the clearance between the text and the surrounding box [15%]. Only used if <code>-W</code> or <code>-G</code> are specified. Append the unit you want (<code>c</code>m, <code>i</code>nch, or <code>p</code>oint; if not given we consult <i>PROJ_LENGTH_UNIT</i>) or % for a percentage of the font size.</p>
<dt><code>-D</code>[<code>j</code>|<code>J</code>]<i>dx</i>[/<i>dy</i>][<code>v</code>[<i>pen</i>]]</p>
<dd> Offsets the text from the projected (<i>x</i>,<i>y</i>) point by <i>dx</i>,<i>dy</i> [0/0]. If <i>dy</i> is not specified then it is set equal to <i>dx</i>. Use <code>-Dj</code> to offset the text away from the point instead (i.e., the text justification will determine the direction of the shift). Using <code>-DJ</code> will shorten diagonal offsets at corners by <a href="/docs/linux/man/2-sqrt/">sqrt</a>(2). Optionally, append <code>v</code> which will draw a line from the original point to the shifted point; append a <i>pen</i> to change the attributes for this line.</p>
<dt><code>-F</code>[<code>+a</code>[<i>angle</i>]][<code>+c</code>[<i>justify</i>]][<code>+f</code>[<i>font</i>]][<code>+h</code>][<code>+j</code>[<i>justify</i>]][<code>+l</code>]</p>
<dd> By default, text will be placed horizontally, using the primary annotation font attributes (<i>FONT_ANNOT_PRIMARY</i>), and centered on the data point. Use this option to override these defaults by specifying up to three text attributes (font, angle, and justification) directly on the command line. Use <code>+f</code> to set the font (size,fontname,color); if no font info is given then the input file must have this information in one of its columns. Use <code>+a</code> to set the angle; if no angle is given then the input file must have this as a column. Use <code>+j</code> to set the justification; if no justification is given then the input file must have this as a column. Items read from the data file should be in the same order as specified with the <code>-F</code> option. Example: <code>-F</code><code>+f</code>12p,Helvetica-Bold,red<code>+j+a</code> selects a 12p red Helvetica-Bold font and expects to read the justification and angle from the file, in that order, after <i>x</i>, <i>y</i> and before <i>text</i>. In addition, the <code>+c</code> justification lets us use x,y coordinates extracted from the <code>-R</code> string instead of providing them in the input file. For example <code>-F+c</code>TL gets the <i>x_min</i>, <i>y_max</i> from the <code>-R</code> string and plots the text at the Upper Left corner of the map. Normally, the text to be plotted comes from the data record. Instead, use <code>+h</code> or <code>+l</code> to select the text as the most recent segment header or segment label, respectively in a multisegment input file.</p>
<dt><code>-G</code><i>color</i></p>
<dd> Sets the shade or color used for filling the text box [Default is no fill]. Alternatively, use <code>-Gc</code> to plot the text and then use the text dimensions (and <code>-C</code>) to build clip paths and turn clipping on. This clipping can then be turned off later with psclip <code>-C</code>. To <code>not</code> plot the text but activate clipping, use <code>-GC</code> instead.</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code></p>
<dd> Lists the font-numbers and font-names available, then exits.</p>
<dt><code>-M</code></p>
<dd> Paragraph mode. Files must be multiple segment files. Segments are separated by a special record whose first character must be <i>flag</i> [Default is <code>&gt;</code>]. Starting in the 3rd column, we expect to find information pertaining to the typesetting of a text paragraph (the remaining lines until next segment header). The information expected is (<i>x y</i> [<i>font angle justify</i>] <i>linespace parwidth parjust</i>), where <i>x y font angle justify</i> are defined above (<i>font</i>, <i>angle</i>, and <i>justify</i> can be set via <code>-F</code>), while <i>linespace</i> and <i>parwidth</i> are the linespacing and paragraph width, respectively. The justification of the text paragraph is governed by <i>parjust</i> which may be <code>l</code>(eft), <code>c</code>(enter), <code>r</code>(ight), or <code>j</code>(ustified). The segment header is followed by one or more lines with paragraph text. Text may contain the escape sequences discussed above. Separate paragraphs with a blank line. Note that here, the justification set via <code>-F+j</code> applies to the box alignment since the text justification is set by <i>parjust</i>.</p>
<dt><code>-N</code></p>
<dd> Do NOT clip text at map boundaries [Default will clip].</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Q</code></p>
<dd> Change all text to either <code>l</code>ower or <code>u</code>pper case [Default leaves all text as is].</p>
<dt><code>-T</code></p>
<dd> Specify the shape of the textbox when using <code>-G</code> and/or <code>-W</code>. Choose lower case <code>o</code> to get a straight rectangle [Default]. Choose upper case <code>O</code> to get a rounded rectangle. In paragraph mode (<code>-M</code>) you can also choose lower case <code>c</code> to get a concave rectangle or upper case <code>C</code> to get a convex rectangle.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code><i>pen</i></p>
<dd> Sets the pen used to draw a rectangle around the text string (see <code>-T</code>) [Default is width = default, color = black, style = solid]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-Z</code></p>
<dd> For 3-D projections: expect each item to have its own level given in the 3rd column, and <code>-N</code> is implicitly set. (Not implemented for paragraph mode).</p>
<dt><code>-a</code><i>col</i>=<i>name</i>[<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Set aspatial column associations <i>col</i>=<i>name</i>.</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-:</code>[<code>i</code>|<code>o</code>] <i>(more &#8230;)</i></p>
<dd> Swap 1st and 2nd column on input and/or output.</p>
<dt><code>-p</code>[<code>x</code>|<code>y</code>|<code>z</code>]<i>azim</i>/<i>elev</i>[/<i>zlevel</i>][<code>+w</code><i>lon0</i>/<i>lat0</i>[/<i>z0</i>]][<code>+v</code><i>x0</i>/<i>y0</i>] <i>(more &#8230;)</i></p>
<dd> Select perspective view. (Not implemented for paragraph mode).</p>
<dt><code>-t</code>[<i>transp</i>] <i>(more &#8230;)</i></p>
<dd> Set PDF transparency level in percent.</p>
<dt><code>-^</code> or just <code>&#8211;</code></p>
<dd> Print a short message about the syntax of the command, then exits (NOTE: on Windows use just <code>&#8211;</code>).</p>
<dt><code>-+</code> or just <code>+</code></p>
<dd> Print an extensive usage (help) message, including the explanation of any module-specific option (but not the GMT common options), then exits.</p>
<dt><code>-?</code> or no arguments</p>
<dd> Print a complete usage (help) message, including the explanation of options, then exits.</p>
<dt><code>&#8211;</code><code>-version</code></p>
<dd> Print GMT version and exit.</p>
<dt><code>&#8211;</code><code>-show-datadir</code></p>
<dd> Print full path to GMT share directory and exit.</dl>
<h2>EXAMPLES</h2>
<p> To plot just the red outlines of the (lon lat text strings) stored in the file text.d on a Mercator plot with the given specifications, use </p>
<pre>
gmt pstext text.d -R-30/30/-10/20 -Jm0.1i -P -F+f18p,Helvetica,-=0.5p,red -B5 &gt; plot.ps
</pre>
<p> To plot a text at the upper left corner of a 10 cm map </p>
<pre>
echo TopLeft | gmt pstext -R1/10/1/10 -JX10 -F+cTL -P &gt; plot.ps
</pre>
<p> To add a typeset figure caption for a 3-inch wide illustration, use </p>
<pre>
gmt pstext -R0/3/0/5 -JX3i -O -h1 -M -N -F+f12,Times-Roman+jLT &lt;&lt; EOF &gt;&gt; figure.ps
</pre>
<pre><code>
This is an unmarked header record not starting with # &gt; 0 - 0.5 13p 3i j
                                                                @ %
                                                                5 % Figure 1. @ % % This illustration shows nothing useful,
    but it still needs
        a figure caption.Highlighted in @;
255 / 0 / 0;
red @;
;
you can see the locations
    of cities where it is @\_impossible @\_ to get any good Thai food;
these are to be avoided.EOF
</code></pre>
<h2>WINDOWS REMARKS</h2>
<p> Note that under Windows, the percent sign (%) is a variable indicator (like $ under Unix). To indicate a plain percentage sign in a batch script you need to repeat it (%%); hence the font switching mechanism (@%*font*% and @%%) may require twice the number of percent signs. This only applies to text inside a script or that otherwise is processed by DOS. Data files that are opened and read by <code>pstext</code> do not need such duplication.</p>
<h2>LIMITATIONS</h2>
<p> In paragraph mode, the presence of composite characters and other escape sequences may lead to unfortunate word splitting. Also, if a font is requested with an outline pen it will not be used in paragraph mode. Note if any single word is wider than your chosen paragraph width then the paragraph width is automatically enlarged to fit the widest word.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtcolors</code>, <code>psconvert</code>, <code>psbasemap</code>, <code>pslegend</code>, <code>psxy</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
