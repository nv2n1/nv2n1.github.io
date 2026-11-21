---
title: "pstoimg(1)"
name: "pstoimg"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pstoimg/"
description: "pstoimg – Convert a PostScript file to a bitmap image using Ghostscript and the Netpbm utilities"
---

<h2 class="name">NAME</h2>
<p> pstoimg &#8211; Convert a PostScript file to a bitmap image using Ghostscript and the Netpbm utilities </p>
<h2>SYNOPSIS</h2>
<p> <code>pstoimg</code> <code>-help</code> | <code>-version</code> </p>
<p> <code>pstoimg</code> [&nbsp;<code>-antialias</code>&nbsp;] [&nbsp;<code>-aaliastext</code>&nbsp;] [&nbsp;<code>-center</code>&nbsp;<i>num</i>&nbsp;] [&nbsp;<code>-color</code>&nbsp;<i>num</i>&nbsp;] [&nbsp;<code>-crop</code>&nbsp;<i>code</i>&nbsp;] [&nbsp;<code>-debug</code>&nbsp;] [&nbsp;<code>-density</code>&nbsp;<i>num</i>] [&nbsp;<code>-depth</code>&nbsp;<i>num</i>&nbsp;] [&nbsp;<code>-discard</code>&nbsp;] [&nbsp;<code>-flip</code>&nbsp;<i>code</i>&nbsp;] [&nbsp;<code>-geometry</code>&nbsp;<i>X</i>x<i>Y</i>&nbsp;] [&nbsp;<code>-interlaced</code>&nbsp;] [&nbsp;<code>-margins</code>&nbsp;<i>X</i>,<i>Y</i>&nbsp;] [&nbsp;<code>-multipage</code>&nbsp;] [&nbsp;<code>-out</code>&nbsp;<i>file</i>&nbsp;] [&nbsp;<code>-quiet</code>&nbsp;] [&nbsp;<code>-rightjustify</code>&nbsp;<i>num</i>&nbsp;] [&nbsp;<code>-scale</code>&nbsp;<i>num</i>&nbsp;] [&nbsp;<code>-tmp</code>&nbsp;<i>path</i>&nbsp;] [&nbsp;<code>-topjustify</code>&nbsp;[<code>x</code>]<i>num</i>&nbsp;] [&nbsp;<code>-transparent</code>&nbsp;] [&nbsp;<code>-type</code>&nbsp;<i>type</i>&nbsp;] [&nbsp;<code>-shoreup</code>&nbsp;<i>num</i>[<code>d</code>]&nbsp;] [&nbsp;<code>-white</code>&nbsp;] <i>file</i> [&nbsp;<i>file2</i>&nbsp;&#8230;&nbsp;]</p>
<h2>OPTIONS</h2>
<p> The command line options may be abbreviated to the shortest unique prefix.</p>
<dl>
<dt><code>-help</code></dt>
<dd> Show this help page and exit.</dd>
<dt><code>-version</code></dt>
<dd> Show the release and version of pstoimg and exit.</dd>
<dt><code>-antialias</code></dt>
<dd> Use Ghostscript&#8217;s anti-aliasing feature for rendering &#8220;softer&#8221; images. This applies to lines and edges of polygonal and oval or circular shapes. Only valid if Ghostscript 4.03 or higher is installed.</dd>
<dt><code>-aaliastext</code></dt>
<dd> Use Ghostscript&#8217;s anti-aliasing feature for &#8220;smoother&#8221; font characters, without the jagged edges. Similar to <code>-antialias</code> for graphic components. Only valid if Ghostscript 4.03 or higher is installed.</dd>
<dt><code>-center</code> <i>num</i></dt>
<dd> Add the appropriate amount of whitespace to the left of the image so that the image appears to be centered in a total width of <i>num</i> pixels.</dd>
<dt><code>-crop</code> <i>code</i></dt>
<dd> Crop the bitmap from the given directions. <i>code</i> may be a string of several cropping instructions, which are executed strictly in the given order. Possible values are: <code>h</code> (horizontal, i.e. crop top and bottom), <code>v</code> (vertical), <code>tblr</code> (top, bottom, left, right) and <code>a</code> (all directions). A special case is <code>s</code>: &#8220;shave&#8221; the image at the bottom, but only if a single line of whitespace exists.</dd>
<dt><code>-debug</code></dt>
<dd> Turn on debugging output. This can get rather verbose. Any intermediate files generated are not removed to help debugging.</dd>
<dt><code>-density</code> <i>num</i></dt>
<dd> The density (resolution) in <font SIZE="-1">DPI</font> in which to render the bitmap. The default is 72.</dd>
<dt><code>-depth</code> <i>num</i> or <code>-color</code> <i>num</i></dt>
<dd> Specify the color depth of the bitmap. Legal values are 1 (black &amp; white), 8 (256 colors) and 24 (true color).</dd>
<dt><code>-discard</code></dt>
<dd> Delete the input postscript file if the conversion was successful. Setting the environment <font SIZE="-1">DISCARD</font> to a true value (as perl sees it) has the same effect.</dd>
<dt><code>-flip</code> <i>code</i></dt>
<dd> Flip all generated output bitmaps. The following codes are recognized: lr (flip left-right), tb (flip top-bottom), xy (flip bottom/left-top/right), r90 and ccw (rotate by 90 degrees counterclockwise), r270 and cw (rotate 90 degrees clockwise) and r180 (rotate 180 degrees).</dd>
<dt><code>-geometry</code> <i>X</i>x<i>Y</i></dt>
<dd> Render only this &#8220;window&#8221; of the PostScript file. If given, this option can dramatically reduce memory requirements and speed up conversion. The geometry is automatically detected in case of <font SIZE="-1">EPS</font> files (Encapsulated PostScript).</dd>
<dt><code>-interlaced</code></dt>
<dd> Generate an interlaced bitmap. Interlaced images build up from coarse to fine as they are loaded. This option may not work on every installation and/or bitmap type, depending of the capabilities of external programs.</dd>
<dt><code>-margins</code> <i>X</i>,<i>Y</i></dt>
<dd> The offset of the rectangle in the postscript file that is going to be rendered from top/left. Can be used together with <code>-geometry</code> to further reduce the size of the intermediate bitmap file generated by Ghostscript.</dd>
<dt><code>-multipage</code></dt>
<dd> Process a multi-page PostScript file, i.e. create an individual bitmap for every page. The resulting files are numbered: The decimal number (starting with 1) is appended to the basename of the PostScript input file (or the basename of the filename specified with <code>-out</code>), while keeping the extension.</dd>
<dt><code>-out</code> <i>file</i></dt>
<dd> The file where to write the bitmap. If multiple PostScript files are supplied on the command line, this option is ignored. The bitmap type extension is appended automatically if <i>file</i> does not contain a dot. In connection with <code>-multipage</code> <i>file</i> is extended by the page number as shown in this example: </dd>
<p> -outfile foo.gif &#8212;&#8212;&#8211;&gt; foo1.gif, foo2.gif, &#8230;</p>
<dt><code>-quiet</code></dt>
<dd> Do not print anything except error messages.</dd>
<dt><code>-rightjustify</code> <i>num</i></dt>
<dd> Add the appropriate amount of whitespace to the left of the image so that it appears to be aligned to the right in a total width of <i>num</i> pixels.</dd>
<dt><code>-scale</code> <i>factor</i></dt>
<dd> Scale the image by <i>factor</i>. Valid choices are any numbers greater than zero. Useful choices are numbers between 0.1 &#8211; 5. Large numbers may generate very large intermediate files and will take longer to process. If this option is omitted, the environment <font SIZE="-1">SCALE</font> is considered.</dd>
<dt><code>-shoreup</code> <i>num</i>[<code>d</code>]</dt>
<dd> Make height and width of the bitmap(s) an exact multiple of <i>num</i>. If <i>num</i> is followed by a &#8220;d&#8221;, then half the extra vertical space is placed underneath. This option is useful, if you want to have &#8220;blown-up&#8221; images of high quality for print, but downscale them in <font SIZE="-1">HTML</font> using <tt>&quot;&lt;IMG WIDTH=x HEIGHT=y&gt;&quot;</tt>. If the actual image is is not an integer multiple of x,y then browsers tend to display distorted images.</dd>
<dt><code>-tmp</code> <i>path</i></dt>
<dd> Use <i>path</i> to store temporary files. Defaults to /tmp on this installation. This parameter can be set by the environment <font SIZE="-1"><code>TMP</code></font> or <font SIZE="-1"><code>TEMP</code></font>, too.</dd>
<dt><code>-topjustify</code> [<code>x</code>]<i>num</i></dt>
<dd> Add padding whitespace to the image so that it gets a defined height. If an integer value is given, it defines the total height. The whitespace is added at the bottom. If the number is preceded by &#8220;x&#8221;, then this multiple of the image height is added as whitespace at the bottom.</dd>
<dt><code>-transparent</code></dt>
<dd> Generate transparent bitmaps, i.e. the background color (white) is transparent if viewed with certain viewers (e.g. browsers). This option may not be available due to missing capabilities of external programs.</dd>
<dt><code>-type</code> <i>type</i></dt>
<dd> Instruct pstoimg to render the bitmap in <i>type</i> format. Depending on the local installation, pstoimg is capable of generating either <font SIZE="-1">GIF</font> or <font SIZE="-1">PNG</font> bitmaps. This site features the following types: svg png gif </dd>
<p> If omitted, the first type in this list is taken.</p>
<dt><code>-white</code></dt>
<dd> Remove TeX&#8217;s page color information from the PostScript file before converting so that a white background is used.</dd></dl>
<h2>DESCRIPTION</h2>
<p> <code>pstoimg</code> iterates over the given input files and runs them through Ghostscript. The resulting pnm (portable anymap files) are processed with different Netpbm tools (cropping, color mapping, aligning, &#8230;) and finally converted into (currently) either <font SIZE="-1">GIF</font> or <font SIZE="-1">PNG</font> format. The bitmaps can now be included e.g. in <font SIZE="-1">WWW</font> pages. </p>
<p> The PostScript file is converted as is. If a valid bounding box is found (<font SIZE="-1">EPS</font> format), then only this area is converted. The image is <i>not</i> cropped by default.</p>
<h2>RETURN VALUE</h2>
<dl>
<dt>0</dt>
<dd> if everything went all right</dd>
<dt>x</dt>
<dd> (x != 0) something went wrong. See the message output.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>&quot;pstoimg foo.ps&quot;</dt>
<dd> Convert the first page of foo.ps to the default bitmap type.</dd>
<dt>&quot;pstoimg -type png -crop a -trans -interlace foo.ps&quot;</dt>
<dd> Same as above, but force png output and crop all the whitespace around the image and make the color white transparent and generate an interlaced bitmap.</dd>
<dt>&quot;pstoimg -multi -out bar -type gif -crop a foo.ps&quot;</dt>
<dd> Consider foo.ps a multiple page PostScript file and create output files bar1.gif, bar2.gif, etc.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1">DENSITY, DEPTH, DEBUG, DISCARD</font></dt>
<dd> See <code>-density</code>, <code>-depth</code>, <code>-debug</code>, <code>-discard</code>, respectively.</dd>
<dt><font SIZE="-1">GS_LIB</font></dt>
<dd> This variable is set to the path(s) where Ghostscript libraries have been found on this system during configuration, but only if the built-in paths are not correct. This fixes the problem of relocation that is quite common on Win32 installations. This behavior can be overridden by setting <font SIZE="-1">GS_LIB</font> manually before starting pstoimg.</dd>
<dt><font SIZE="-1">LATEX2HTMLDIR</font></dt>
<dd> The directory where the LaTeX2HTML library and perl modules are found. Defaults to &#8220;/usr/share/latex2html&#8221; on this installation.</dd>
<dt><font SIZE="-1">OUTFILE</font></dt>
<dd> Setting this has the same effect as specifying <code>-out</code>. Please do not rely on this feature any more, it will disappear from the next releases!</dd>
<dt><font SIZE="-1">PAPERSIZE</font></dt>
<dd> The papersize to use by Ghostscript to render the image. pstoimg tries hard to optimize for rendering on the smallest possible bitmap size. Still this option is there to enable tuning by hand, although it is deprecated. If pstoimg finds a better setting, this parameter is ignored.</dd>
<dt><font SIZE="-1">SCALE</font></dt>
<dd> See the discussion of <code>-scale</code>.</dd>
<dt><font SIZE="-1">TMP</font> and <font SIZE="-1">TEMP</font></dt>
<dd> Unless overridden by <code>-tmp</code>, these variables denote a directory where to store temporary files. <font SIZE="-1">TMP</font> is considered first, then <font SIZE="-1">TEMP.</font></dd></dl>
<h2>SEE ALSO</h2>
<p> gs, pnmcrop, pnmquant, pbmmake, pnmcat, pnmfile, pnmflip, ppmtogif, pnmtopng, giftool, giftrans.</p>
<h2>NOTES</h2>
<p> Several people have suggested to use ImageMagick&#8217;s convert instead of pstoimg. A few comments on this: convert uses (of course) Ghostscript for conversion of PostScript to bitmap, so one still needs gs. And for the special requirements of LaTeX2HTML convert&#8217;s features are not sufficient. The ImageMagick toolset has everything in place, but it has some overhead that can prove killing when processing some 100 images. pstoimg only does what it really has to, so it should be quite efficient. Don&#8217;t get me wrong &#8211; I like ImageMagick, but not in the context of LaTeX2HTML.</p>
<h2>CAVEATS</h2>
<p> This utility is automatically configured and built to work on the local setup. If this setup changes (e.g. some of the external commands are moved), the script has be be reconfigured. </p>
<p> Despite the portability of perl, a pstoimg configured on <font SIZE="-1">UNIX</font> will probably not work on Win32 and vice versa.</p>
<h2>BUGS</h2>
<p> Please report bugs to latex2html [at] tug.org, stating the (debug) output of pstoimg, your perl version and the versions of the external tools. Best is to include the cfgcache.pm file from the configuration procedure.</p>
<h2>AUTHOR</h2>
<p> Marek Rouchal &lt;marek [at] saftsack.fs.uni-bayreuth.de&gt;</p>
<h2>HISTORY</h2>
<p> This script went through a long evolution, beginning with a modification of Doug Crabill&#8217;s &lt;dgc [at] cs.purdue.edu&gt; ps2epsi script. The first perl version was done by Nikos Drakos &lt;nikos [at] cbl.leeds.ac.uk&gt;. It was gradually improved by numerous LaTeX2HTML developers: Ross Moore &lt;ross [at] maths.mq.edu.au&gt;, Jens Lippmann &lt;lippmann [at] rbg.informatik.tu-darmstadt.de&gt; and others (sorry for not mentioning everyone and thanks for your contributions). </p>
