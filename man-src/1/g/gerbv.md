---
title: "gerbv(1)"
name: "gerbv"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gerbv/"
description: "gerbv – Gerber Viewer"
---

<h2>NAME</h2>
<p> gerbv &#8211; Gerber Viewer</p>
<h2>SYNOPSIS</h2>
<p> <code>gerbv [OPTIONS] [gerberfile[s]]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>gerbv</i> is a viewer for RS274-X, commonly known as Gerber, files. RS274-X files are generated from different PCB CAD programs and are used in the printed circuit board manufacturing process. <i>gerbv</i> also supports Excellon/NC drill files as well as XY (centroid) files produced by the program PCB (<a rel="nofollow" href="http://pcb.sf.net">http://pcb.sf.net</a>). </p>
<h2>OPTIONS</h2>
<p> <code>Warning! </code> On some platforms, which hasn&#8217;t long option available, only short options are available. </p>
<h3>gerbv General options:</h3>
<p> <code>-V|&#8211;version</code> Print the version number of gerbv and exit.</p>
<dl>
<dt><code>-h|&#8211;help</code></p>
<dd> Print a brief usage guide and exit.</p>
<dt><code>-b&lt;hex&gt;|&#8211;background=&lt;hex&gt;</code></p>
<dd> Use background color &lt;hex&gt;. &lt;hex&gt; is specified as an html-color code, e.g. #FF0000 for Red.</p>
<dt><code>-f&lt;hex&gt;|&#8211;foreground=&lt;hex&gt;</code></p>
<dd> Use foreground color &lt;hex&gt;. &lt;hex&gt; is specified as an html-color code, e.g. #00FF00 for Green. If a user also wants to set the alpha (rendering with Cairo) it can be specified as an #RRGGBBAA code. Use multiple -f flags to set the color for multiple layers.</p>
<dt><code>-l&nbsp;<wbr>&lt;filename&gt;|&#8211;log=&lt;filename&gt;</code></p>
<dd> All error messages etc are stored in a file with filename <i>&lt;filename&gt;</i>.</p>
<dt><code>-t&nbsp;<wbr>&lt;filename&gt;|&#8211;tools=&lt;filename&gt;</code></p>
<dd> Read Excellon tools from the file <i>&lt;filename&gt;</i>.</p>
<dt><code>-p&nbsp;<wbr>&lt;project filename&gt;|&#8211;project=&lt;project filename&gt;</code></p>
<dd> Load a stored project. Please note that the project file must be stored in the same directory as the gerber files. </p>
</dl>
<h3>gerbv Export-specific options:</h3>
<p> The following commands can be used in combination with the -x flag: <code>-B&lt;b&gt;|&#8211;Border=&lt;b&gt;</code> Set the border around the image &lt;b&gt; percent of the width and height. Default &lt;b&gt; is 5%%.</p>
<dl>
<dt><code>-D&lt;XxY&gt;or&lt;R&gt;|&#8211;dpi=&lt;XxY&gt;or&lt;R&gt;</code></p>
<dd> Resolution (Dots per inch) for the output bitmap. Use &lt;XxY&gt; for different resolutions for the width and height (only when compiled with Cairo as render engine). Use &lt;R&gt; to have the same resolution in both directions. Defaults to 72 DPI in both directions.</p>
<dt><code>-T&lt;X,Y&gt;|&#8211;translate=&lt;X,Y&gt;</code></p>
<dd> Translate the image by the distance &lt;X,Y&gt;. Use multiple -T flags to translate multiple files.</p>
<dt><code>-O&lt;XxY&gt;|&#8211;origin=&lt;XxY&gt;</code></p>
<dd> Set the lower left corner of the exported image to coordinate &lt;XxY&gt;. Coordinates are in inches.</p>
<dt><code>-a|&#8211;antialias</code></p>
<dd> Use antialiasing for the generated output-bitmap.</p>
<dt><code>-o&nbsp;<wbr>&lt;filename&gt;|&#8211;output=&lt;filename&gt;</code></p>
<dd> Export to &lt;filename&gt;.</p>
<dt><code>-W&lt;WxH&gt;|&#8211;window_inch=&lt;WxH&gt;</code></p>
<dd> Window size in inches &lt;WxH&gt; for the exported image.</p>
<dt><code>-w&lt;WxH&gt;|&#8211;window=WxH&gt;</code></p>
<dd> Window size in pixels &lt;WxH&gt; for the exported image. Autoscales to fit if no resolution is specified (note that the default 72 DPI also changes in that case). If a resolution is specified, it will clip the image to this size.</p>
<dt><code>-x&lt;png/pdf/ps/svg/rs274x/drill&gt;|&#8211;export=&lt;png/pdf/ps/svg/rs274x/drill&gt;</code></p>
<dd> Export to a file and set the format for the output file. </p>
</dl>
<h3>GTK Options</h3>
<p> <code>&#8211;gtk-module=</code><i>MODULE</i> Load an additional GTK module</p>
<dl>
<dt><code>&#8211;g-fatal-warnings</code></p>
<dd> Make all warnings fatal</p>
<dt><code>&#8211;gtk-debug=</code><i>FLAGS</i></p>
<dd> GTK debugging flags to set</p>
<dt><code>&#8211;gtk-no-debug=</code><i>FLAGS</i></p>
<dd> GTK debugging flags to unset</p>
<dt><code>&#8211;gdk-debug=</code><i>FLAGS</i></p>
<dd> GDK debugging flags to set</p>
<dt><code>&#8211;gdk-no-debug=</code><i>FLAGS</i></p>
<dd> GDK debugging flags to unset</p>
<dt><code>&#8211;display=</code><i>DISPLAY</i></p>
<dd> X display to use</p>
<dt><code>&#8211;sync</code></p>
<dd> Make X call synchronous</p>
<dt><code>&#8211;no-xshm</code></p>
<dd> Don&#8217;t use X shared memory extension</p>
<dt><code>&#8211;name=</code><i>NAME</i></p>
<dd> Program name as used by the window manager</p>
<dt><code>&#8211;class=</code><i>CLASS</i></p>
<dd> Program class as used by the window manager </p>
</dl>
<h2>GENERAL</h2>
<p> When you start gerbv you can give the files to be loaded on the command line, either as each file separated with a space or by using wildcards. </p>
<p> The user interface is graphical. Simply press left mouse button and the image will pan as you move the mouse. To manipulate a layer, right-click on one of the rightmost buttons. That will bring up a pop-up menu where you can select what you want to do with that layer (load file, change color, etc). </p>
<p> If you hold the mouse button over one the rightmost button a tooltips will show you the name of the file loaded on that layer. </p>
<h2>ACTIVATION AND DEACTIVATION OF LAYERS</h2>
<p> You can load several files at one time. You can then turn displaying of the layers on and off by clicking on one of the rightmost buttons. </p>
<p> You can also control this from the keyboard. Press Alt, enter the number on the layer you want activate/deactivate on the numerical keypad and then release the Alt key. </p>
<h2>ZOOMING</h2>
<p> Zooming can be handled by either menu choices, keypressing, middle mouse button or scroll wheel. If you press Alt+I you will zoom in and if you press Alt+O you will zoom out. If you press middle mouse button you will zoom out, and if you press Shift and middle mouse button you will zoom in. Scroll wheel works if you enabled that in your X server and mapped it to button 4 and 5. You can also zoom in by pressing z and zoom out by pressing shift+z (ie Z). You can make the image fit by pressing f (there is also a menu alternative for this). </p>
<p> You can also do zooming by outline. Press right mouse button, draw, release. The dashed line shows how the zooming will be dependent on the resolution of the window. The non-dashed outline will show what you actually selected. If you change your mind when started to mark outline, you can always abort by pressing escape. By holding down the shift key when you press the right mouse button, you will select an area where the point you started at will be the center of your selection. </p>
<h2>MEASUREMENTS</h2>
<p> You can do measurement on the image displayed. By pressing shift, the cursor changes to a plus. By using left mouse button you can draw the lines that you want to measure. The result of the last measurement is also displayed on the statusbar. All measurements are in the drawing until you either zoom, pan or press the escape key. </p>
<p> The statusbar shows the current mouse position on the layer in the same coordinates as in the file. Ie if you have (0,0) in the middle of the image in the gerber files, the statusbar will show (0,0) at the same place. </p>
<h2>SUPERIMPOSING</h2>
<p> When you load several Gerber files, you can display them &quot;on top of each other&quot;, ie superimposing. The general way to display them are that upper layers cover the layers beneath, which is called copy (GTK+ terms). </p>
<p> The other ways selectable are and, or, xor and invert. They map directly to corresponding functions in GTK. In GTK they are described as: &quot;For colored images, only GDK_COPY, GDK_XOR and GDK_INVERT are generally useful. For bitmaps, GDK_AND and GDK_OR are also useful.&quot; </p>
<h2>PROJECTS</h2>
<p> gerbv can also handle projects. A project consist of bunch of loaded layers with their resp. color and the background color. The easiest way to create a project is to load all files you want into the layer you want, set all the colors etc and do a &quot;Save Project As&#8230;&quot;. </p>
<p> You load a project either from the menu bar or by using the commandline switches -p or &#8211;project. </p>
<p> Currently there is a limit in that the project file must be in the same directory as the gerber files to be loaded. </p>
<h2>SCHEME</h2>
<p> The project files are simple Scheme programs that is interpreted by a built in Scheme interpreter. The Scheme interpreter is TinyScheme and needs a Scheme program called init.scm to initialize itself. The search path for init.scm is (in the following order) /usr/share/gerbv/scheme, the directory with the executable gerbv, the directory gerbv was invoked from and finally according to the environment variable GERBV_SCHEMEINIT. </p>
<h2>TOOLS FILE</h2>
<p> Not every Excellon drill file is self-sufficient. Some CADs produce .drd files where tools are only referenced, but never defined (such as what diameter of the tool is.) Eagle CAD is one of such CADs, and there are more since many board houses require Tools files. </p>
<p> A Tools file is a plain text file which you create in an editor. Each line of the file describes one tool (the name and the diameter, in inches): </p>
<pre>
        T01 0.024
        T02 0.040
        ...
</pre>
<p> These are the same tools (T01 etc.) that are used in the Drill file. A standard practice with Eagle is to create an empty Tools file, run the CAM processor, and the error report tells you which tools you &quot;forgot&quot;. Then you put these tools into the file and rerun the CAM processor. </p>
<p> You load a tool file by using the commandline switches -t or &#8211;tools. The file can have any name you wish, but Eagle expects the file type to be &quot;.drl&quot;, so it makes sense to keep it this way. Some board houses are still using CAM software from DOS era, so you may want to excercise caution before going beyond the 8.3 naming convention. </p>
<p> When <i>gerbv</i> reads the Tools file it also checks that there are no duplicate definitions of tools. This does happen from time to time as you edit the file by hand, especially if you, during design, add or remove parts from the board and then have to add new tools into the Tools file. The duplicate tools are a very serious error which will stop (HOLD) your board until you fix the Tools file and maybe the Excellon file. <i>gerbv</i> will detect duplicate tools if they are present, and will exit immediately to indicate such a fatal error in a very obvious way. A message will also be printed to standard error. </p>
<p> If your Excellon file does not contain tool definitions then <i>gerbv</i> will preconfigure the tools by deriving the diameter of the drill bit from the tool number. This is probably not what you want, and you will see warnings printed on the console. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>GERBV_SCHEMEINIT</p>
<dd> Defines where the init.scm file is stored. Used by scheme interpreter, which is used by the project reader. </p>
</dl>
<h2>AUTHOR</h2>
<pre>
Stefan Petersen (spetm at users.sourceforge.net): Overall hacker and project leader
Andreas Andersson (e92_aan at e.kth.se): Drill file support and general hacking
Anders Eriksson (aenfaldor at users.sourceforge.net) : X and GTK+ ideas and hacking
</pre>
<h2>COPYRIGHT</h2>
<pre>
Copyright &#169;  2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008 Stefan Petersen
This document can be freely redistributed according to the terms of the 
GNU General Public License version 2.0
</pre>
<h2>Index</h2>
