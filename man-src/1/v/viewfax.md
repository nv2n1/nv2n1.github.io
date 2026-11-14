---
title: "viewfax(1)"
name: "viewfax"
section: "1"
letter: "v"
url: "/docs/linux/man/1-viewfax/"
description: "viewfax – display fax files in an X11 window"
---

<h2>NAME</h2>
<p> viewfax &#8211; display fax files in an X11 window</p>
<h2>SYNOPSIS</h2>
<p> <code>viewfax</code> [<code>-fnluirvW24</code>] [<code>-h</code><i>height</i>] [<code>-w</code><i>width</i>] [<code>-z</code><i>zoom</i>] [<code>-d</code><i>display</i>] [<code>-g</code><i>wxh+x+y</i>] [<code>-b</code><i>bell</i>] [<code>-m</code><i>memory</i>] <i>filename&#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>viewfax</code> displays one or more fax files in an X11 window. The input files may be either raw, single-page faxes received by a fax modem with a program such as <code><a href="/docs/linux/man/1-mgetty/">mgetty</a>(1),</code> or tiff files such as those used by <code>hylafax.</code> The first (or only) page of &quot;PC-Research&quot;-style (DigiFAX) files produced by the <code>ghostscript</code> dfaxhigh or dfaxlow drivers can also be displayed. </p>
<p> Input files using any common fax encoding such as group 3 (1 and 2 dimensional) and group 4 can be displayed. </p>
<p> The fax images are rendered at full resolution and then successively scaled down by a linear factor of 2 prior to display, until they fit on the screen. The display can be controlled interactively using mouse and keyboard commands. The left mouse button expands the image by a factor of two and the right button reduces it by the same factor. If the image is bigger than the available window size, the middle mouse button can be used to reposition it within the window. Hold down the middle button while dragging the image to its new position. </p>
<p> If the mouse has a scroll-wheel it can be used to move an oversized image vertically. With the shift key depressed, the wheel scrolls through the pages. The shift sense is inverted if <code>viewfax</code> is started with <code>-W</code> on the command-line. </p>
<p> Further interaction is controlled by single-key commands:</p>
<dl>
<dt><code>h or Help</code></p>
<dd> displays a page of help information. Type &#8216;q&#8217; to return to the original document.</p>
<dt><code>p or Prior or PgUP or &#8211; or BackSpace</code></p>
<dd> displays the previous page from the command-line list.</p>
<dt><code>n or Next or PgDn or + or space</code></p>
<dd> displays the next page from the command-line list.</p>
<dt><code>Shift HOME</code></p>
<dd> displays the first page from the command-line list.</p>
<dt><code>Shift END</code></p>
<dd> displays the last page from the command-line list.</p>
<dt><code>z</code></p>
<dd> zoom in (same as right mouse button).</p>
<dt><code>Shift Z</code></p>
<dd> zoom out (same as left mouse button).</p>
<dt><code>u</code></p>
<dd> turns the image upside down, which is useful if the fax was originally fed the wrong way into the machine.</p>
<dt><code>Shift U</code></p>
<dd> turns this and all following pages upside down.</p>
<dt><code>l</code></p>
<dd> turns the image through 90 degrees, to view landscape text.</p>
<dt><code>Shift L</code></p>
<dd> turns this and all following pages sideways.</p>
<dt><code>m</code></p>
<dd> produce a left/right mirror image of the page.</p>
<dt><code>Shift M</code></p>
<dd> mirror this and all following pages.</p>
<dt><code>cursor arrows</code></p>
<dd> reposition the displayed image if it exceeds the window size.</p>
<dt><code>HOME</code></p>
<dd> repositions so that the top left corner is visible.</p>
<dt><code>END</code></p>
<dd> makes the bottom right corner visible.</p>
<dt><code>Print</code></p>
<dd> if the environment variable VIEWFAX_PRINT is defined, the current page is printed. All pages are printed with Shift Print.</p>
<dt><code>e</code></p>
<dd> if the environment variable VIEWFAX_EDIT is defined, the current page is passed to the editor. All input files can be edited with Shift e.</p>
<dt><code>q</code></p>
<dd> terminates the program.</p>
<dt><code>Shift Q</code></p>
<dd> terminates the program with non-zero exit status. Can be used to abort a shell script, e.g. when the user is previewing an outbound fax and decides not to send it.</dl>
<h2>OPTIONS</h2>
<p> <code>viewfax</code> is designed to &quot;do the right thing&quot; when given just a filename. Special cases can be handled with the following options. (Note that tiff-files contain a header which overrides the <code>-f, -n, -h, -w, -l, -m, </code>and <code>-u </code>flags.)</p>
<dl>
<dt><code>-f</code></p>
<dd> indicates that raw input files are fine resolution (7.7 lines/mm) faxes. This is the default unless the filename begins with &quot;fn&quot;. Tiff and &quot;PC-Research&quot; (DigiFAX) files are self-specifying.</p>
<dt><code>-n</code></p>
<dd> indicates that raw input files are normal resolution (3.85 lines/mm) faxes. Each fax line is duplicated in the displayed image to give approximately equal vertical and horizontal scales.</p>
<dt><code>-h</code><i>height</i></p>
<dd> specifies the number of fax lines. If this option is missing, <code>viewfax</code> counts the number of lines in the input file.</p>
<dt><code>-w</code><i>width</i></p>
<dd> specifies the number of pixels in each scan-line. The default value is 1728.</p>
<dt><code>-l</code></p>
<dd> display in landscape mode.</p>
<dt><code>-u</code></p>
<dd> turn the image upside down.</p>
<dt><code>-i</code></p>
<dd> invert pixels (black/white).</p>
<dt><code>-b</code></p>
<dd> preferred warning style: &#8216;a&#8217; for audible bell (console beep), &#8216;v&#8217; for visible bell (flash the window), &#8216;n&#8217; for neither. &#8216;v&#8217; is the default.</p>
<dt><code>-d or -display</code></p>
<dd> use specified X server</p>
<dt><code>-g or -geometry</code></p>
<dd> the preferred size and position of the window, specified as <i>width</i>x<i>height</i>+<i>x</i>+<i>y</i>. If a position is given (x and y values), <code>viewfax</code> asks the window manager to place the window there. The initial size of the window is constrained to be at most <i>width</i>x<i>height</i>. </p>
<p> If the window is subsequently resized due to the user zooming in or out, the geometry is taken as a constraint on the screen area which may be used by <code>viewfax.</code> </p>
<p> If you do not supply a geometry value, everything works fine with ICCCM-compliant window managers like <code>olwm, mwm, twm, </code>and <code>tvtwm</code>. When fully zoomed out the <code>viewfax</code> window will occupy the entire screen. </p>
<p> Users of <code>fvwm</code> will notice that the title bar and left border are moved off screen when <code>viewfax</code> repositions the window to (0,0). A workaround is to use -geometry +5+23 when using <code>fvwm.</code> The proper fix would be for someone to update the routine HandleConfigureRequest() in fvwm/events.c to correspond to the code in twm/events.c.</p>
<dt><code>-m</code><i>memory limit</i></p>
<dd> each page is kept in memory after being fetched and expanded, which saves time if the user returns to it in the same session. To prevent viewfax from using all the available swap space, a limit is placed on the total size of cached images. This defaults to 4 MBytes, enough for about 6 typical pages. If the memory limit is exceeded, old images are discarded and must be reloaded from disk if the user returns to them. The operation of this mechanism is transparent apart from the occasional delays due to reloading. The value specified on the command line can be suffixed <code>k</code> or <code>m</code> for kilo- or megabytes.</p>
<dt><code>-r</code></p>
<dd> the bit order of the bytes in the input file is reversed. The fax specification deals only with serial data transmission. Modem manufacturers have to decide whether the first bit received should be placed in the most significant or the least significant position in a byte. The consensus is to pack most significant first, but the -r flag is available to deal with the opposite order.</p>
<dt><code>-v</code></p>
<dd> produce some informative messages (verbose mode).</p>
<dt><code>-z</code><i>zoom</i></p>
<dd> specifies an initial zoom factor. A full-scale fax will usually not fit on the screen. If the <code>-z</code> option is not specified, <code>viewfax</code> scales the image by a power of 2 such that it is fully visible at a reduced size. The user can then use the mouse buttons (see above) to view expanded portions of the image.</p>
<dt><code>-2</code></p>
<dd> Assume that raw input files use group 3 two dimensional coding.</p>
<dt><code>-4</code></p>
<dd> Assume that raw input files use group 4 coding. The number of fax lines (-h option) is required in this case.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>VIEWFAX_PRINT</code></p>
<dd> Defines a command that will print one or more fax pages. </p>
<dt><code>VIEWFAX_EDIT</code></p>
<dd> Defines a command that will calls an editor on one or more fax pages. </p>
</dl>
<p> These two variables are optional. If a variable is undefined, the corresponding keyboard command is ignored. If the variable is defined, it should contain the name of a command or executable script that performs the desired function. The command should process a single page if called with a -p&nbsp;<wbr><i>page-number</i> argument. Alternatively, if can be called with just a list of filenames, meaning that all pages should be processed. </p>
<p> Here is an oversimplified example of a print command. Note that it assumes that the format is tiff and will fail when handed a raw fax file. </p>
<pre><code>
  VIEWFAX_PRINT=printfax
 
  /usr/local/bin/printfax:
#!/ bin / sh
  case "$1" in
  -p) shift
      dopt=`expr $1 - 1`
      shift
      tiff2ps -d ${dopt} -2 -h 11.69 -w 8.27 "$1" | lp
      ;
  ;
  *)  tiff2ps -2 -h 11.69 -w 8.27 "$*" | lp
      ;
  ;
  esac
</code></pre>
<h2>SEE ALSO</h2>
<p> <code>mgetty</code> (<a rel="nofollow" href="http://alpha.greenie.net/mgetty/)">http://alpha.greenie.net/mgetty/)</a> controls data/fax/voice modems. </p>
<p> <code>hylafax</code> (<a rel="nofollow" href="http://www.hylafax.org/)">http://www.hylafax.org/)</a> is a full-function fax client/server system. </p>
<p> <code><a href="/docs/linux/man/1-g3topbm/">g3topbm</a>(1)</code> and <code><a href="/docs/linux/man/1-xv/">xv</a>(1)</code> can be used in a pipeline to view faxes. This will usually be slower than using <code>viewfax,</code> but <code>xv</code> has many capabilities for manipulating the image and saving it in other formats. </p>
<p> <code>faxview.tcl,</code> (<a href="ftp://ftp.leo.org/pub/comp/os/unix/networking/mgetty/faxview.tcl.gz)">ftp://ftp.leo.org/pub/comp/os/unix/networking/mgetty/faxview.tcl.gz)</a> a simple dialog for viewing FAX messages by Ralph Schleicher (rs [at] purple.in-ulm.de). This is a useful tool which provides a file menu from which incoming faxes can be selected for display with <code>viewfax.</code> </p>
<p> CCITT (now ITU) Recommendation T.4, <i>Standardization of Group 3 Facsimile Apparatus for Document</i> <i>Transmission. </i> </p>
<p> CCITT (now ITU) Recommendation T.6, <i>Facsimile Coding Schemes and Coding Control Functions for Group 4</i> <i>Facsimile Apparatus.</i></p>
<h2>BUGS</h2>
<p> The user interface does not comply with any known style guide.<br />
 The help text looks moth-eaten because it is encoded as a fax. This avoids dealing with X11 fonts.<br />
 The program does not refer to the X resources database.</p>
<h2>AUTHOR</h2>
<p> Frank D. Cringle (fdc [at] cliwe.ping.de). </p>
<h2>Index</h2>
