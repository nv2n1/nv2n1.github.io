---
title: "asy(1)"
name: "asy"
section: "1"
letter: "a"
url: "/docs/linux/man/1-asy/"
description: "asy – Asymptote: a script-based vector graphics language"
---

<h2 class="name">NAME</h2>
<p> asy &#8211; Asymptote: a script-based vector graphics language </p>
<h2>SYNOPSIS</h2>
<p> <code>asy</code> [<i>options</i>] [<i>file</i>&nbsp;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>Asymptote</code> is a powerful descriptive vector graphics language for technical drawings, inspired by MetaPost but with an improved C++-like syntax. Asymptote provides for figures the same high-quality level of typesetting that LaTeX does for scientific text.</p>
<h2>OPTIONS</h2>
<p> If no arguments are given, Asymptote runs in interactive mode. </p>
<p> If &quot;-&quot; is given as the file argument, Asymptote reads from standard input. </p>
<p> A summary of options is included below. The effect of most options can be negated by prepending <code>no</code> to the option name. Default values for most options may also be entered in the file <code>.asy/config.asy</code> in the user&#8217;s home directory using the long form: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;import settings;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;batchView=true; </p>
<p> For a complete description, see the Info files.</p>
<dl>
<dt><code>-GPUindexing </code></p>
<dd> Compute indexing partial sums on GPU [true].</p>
<dt><code>-GPUinterlock </code></p>
<dd> Use fragment shader interlock [true].</p>
<dt><code>-V,-View </code></p>
<dd> View output; command-line only.</p>
<dt><code>-absolute </code></p>
<dd> Use absolute WebGL dimensions [false].</p>
<dt><code>-a,-align C|B|T|Z </code></p>
<dd> Center, Bottom, Top, or Zero page alignment [C].</p>
<dt><code>-aligndir pair </code></p>
<dd> Directional page alignment (overrides align) [(0,0)].</p>
<dt><code>-antialias n </code></p>
<dd> Antialiasing width for rasterized output [2].</p>
<dt><code>-auto3D </code></p>
<dd> Automatically activate 3D scene [true].</p>
<dt><code>-autobillboard </code></p>
<dd> 3D labels always face viewer by default [true].</p>
<dt><code>-autoimport string </code></p>
<dd> Module to automatically import.</p>
<dt><code>-autoplain </code></p>
<dd> Enable automatic importing of plain [true].</p>
<dt><code>-autoplay </code></p>
<dd> Autoplay 3D animations [false].</p>
<dt><code>-autorotate </code></p>
<dd> Enable automatic PDF page rotation [false].</p>
<dt><code>-axes3 </code></p>
<dd> Show 3D axes in PDF output [true].</p>
<dt><code>-batchMask </code></p>
<dd> Mask fpu exceptions in batch mode [false].</p>
<dt><code>-batchView </code></p>
<dd> View output in batch mode [false].</p>
<dt><code>-bw </code></p>
<dd> Convert all colors to black and white [false].</p>
<dt><code>-cd directory </code></p>
<dd> Set current directory; command-line only.</p>
<dt><code>-cmyk </code></p>
<dd> Convert rgb colors to cmyk [false].</p>
<dt><code>-c,-command string </code></p>
<dd> Command to autoexecute.</p>
<dt><code>-compact </code></p>
<dd> Conserve memory at the expense of speed [false].</p>
<dt><code>-compress </code></p>
<dd> Compress images in PDF output [true].</p>
<dt><code>-d,-debug </code></p>
<dd> Enable debugging messages [false].</p>
<dt><code>-devicepixelratio n </code></p>
<dd> Ratio of physical to logical pixels [1].</p>
<dt><code>-digits n </code></p>
<dd> Default output file precision [7].</p>
<dt><code>-divisor n </code></p>
<dd> Garbage collect using purge(divisor=n) [2].</p>
<dt><code>-dvisvgmMultipleFiles</code></p>
<dd> dvisvgm supports multiple files [false].</p>
<dt><code>-embed </code></p>
<dd> Embed rendered preview image [true].</p>
<dt><code>-exitonEOF </code></p>
<dd> Exit interactive mode on EOF [true].</p>
<dt><code>-fitscreen </code></p>
<dd> Fit rendered image to screen [true].</p>
<dt><code>-framedelay ms </code></p>
<dd> Additional frame delay [0].</p>
<dt><code>-framerate frames/s </code></p>
<dd> Animation speed [30].</p>
<dt><code>-globalread </code></p>
<dd> Allow read from other directory [true].</p>
<dt><code>-globalwrite </code></p>
<dd> Allow write to other directory [false].</p>
<dt><code>-gray </code></p>
<dd> Convert all colors to grayscale [false].</p>
<dt><code>-h,-help </code></p>
<dd> Show summary of options; command-line only.</p>
<dt><code>-historylines n </code></p>
<dd> Retain n lines of history [1000].</p>
<dt><code>-ibl </code></p>
<dd> Enable environment map image-based lighting [false].</p>
<dt><code>-iconify </code></p>
<dd> Iconify rendering window [false].</p>
<dt><code>-image string </code></p>
<dd> Environment image name [snowyField].</p>
<dt><code>-imageDir string </code></p>
<dd> Environment image library directory [ibl].</p>
<dt><code>-inlineimage </code></p>
<dd> Generate inline embedded image [false].</p>
<dt><code>-inlinetex </code></p>
<dd> Generate inline TeX code [false].</p>
<dt><code>-interactiveMask </code></p>
<dd> Mask fpu exceptions in interactive mode [true].</p>
<dt><code>-interactiveView </code></p>
<dd> View output in interactive mode [true].</p>
<dt><code>-interactiveWrite </code></p>
<dd> Write expressions entered at the prompt to stdout [true].</p>
<dt><code>-k,-keep </code></p>
<dd> Keep intermediate files [false].</p>
<dt><code>-keepaux </code></p>
<dd> Keep intermediate LaTeX .aux files [false].</p>
<dt><code>-level n </code></p>
<dd> Postscript level [3].</p>
<dt><code>-l,-listvariables </code></p>
<dd> List available global functions and variables [false].</p>
<dt><code>-localhistory </code></p>
<dd> Use a local interactive history file [false].</p>
<dt><code>-loop </code></p>
<dd> Loop 3D animations [false].</p>
<dt><code>-lossy </code></p>
<dd> Use single precision for V3D reals [false].</p>
<dt><code>-lsp </code></p>
<dd> Interactive mode for the Language Server Protocol [false].</p>
<dt><code>-m,-mask </code></p>
<dd> Mask fpu exceptions; command-line only.</p>
<dt><code>-maxtile pair </code></p>
<dd> Maximum rendering tile size [(1024,768)].</p>
<dt><code>-maxviewport pair </code></p>
<dd> Maximum viewport size [(0,0)].</p>
<dt><code>-multiline </code></p>
<dd> Input code over multiple lines at the prompt [false].</p>
<dt><code>-multipleView </code></p>
<dd> View output from multiple batch-mode files [false].</p>
<dt><code>-multisample n </code></p>
<dd> Multisampling width for screen images [4].</p>
<dt><code>-offline </code></p>
<dd> Produce offline html files [false].</p>
<dt><code>-O,-offset pair </code></p>
<dd> PostScript offset [(0,0)].</p>
<dt><code>-f,-outformat format </code></p>
<dd> Convert each output file to specified format.</p>
<dt><code>-o,-outname name </code></p>
<dd> Alternative output directory/filename.</p>
<dt><code>-p,-parseonly </code></p>
<dd> Parse file [false].</p>
<dt><code>-pdfreload </code></p>
<dd> Automatically reload document in pdfviewer [false].</p>
<dt><code>-pdfreloaddelay usec </code></p>
<dd> Delay before attempting initial pdf reload [750000].</p>
<dt><code>-position pair </code></p>
<dd> Initial 3D rendering screen position [(0,0)].</p>
<dt><code>-prc </code></p>
<dd> Embed 3D PRC graphics in PDF output [false].</p>
<dt><code>-prerender resolution</code></p>
<dd> Prerender V3D objects (0 implies vector output) [0].</p>
<dt><code>-prompt string </code></p>
<dd> Prompt [&gt; ].</p>
<dt><code>-prompt2 string </code></p>
<dd> Continuation prompt for multiline input [..].</p>
<dt><code>-q,-quiet </code></p>
<dd> Suppress welcome text and noninteractive stdout [false].</p>
<dt><code>-render n </code></p>
<dd> Render 3D graphics using n pixels per bp (-1=auto) [-1].</p>
<dt><code>-resizestep step </code></p>
<dd> Resize step [1.2].</p>
<dt><code>-reverse </code></p>
<dd> reverse 3D animations [false].</p>
<dt><code>-rgb </code></p>
<dd> Convert cmyk colors to rgb [false].</p>
<dt><code>-safe </code></p>
<dd> Disable system call [true].</p>
<dt><code>-scroll n </code></p>
<dd> Scroll standard output n lines at a time [0].</p>
<dt><code>-shiftHoldDistance n </code></p>
<dd> WebGL touch screen distance limit for shift mode [20].</p>
<dt><code>-shiftWaitTime ms </code></p>
<dd> WebGL touch screen shift mode delay [200].</p>
<dt><code>-spinstep deg/s </code></p>
<dd> Spin speed [60].</p>
<dt><code>-svgemulation </code></p>
<dd> Emulate unimplemented SVG shading [true].</p>
<dt><code>-tabcompletion </code></p>
<dd> Interactive prompt auto-completion [true].</p>
<dt><code>-tex engine </code></p>
<dd> latex|pdflatex|xelatex|lualatex|tex|pdftex|luatex|context|none [latex].</p>
<dt><code>-thick </code></p>
<dd> Render thick 3D lines [true].</p>
<dt><code>-thin </code></p>
<dd> Render thin 3D lines [true].</p>
<dt><code>-threads </code></p>
<dd> Use POSIX threads for 3D rendering [true].</p>
<dt><code>-toolbar </code></p>
<dd> Show 3D toolbar in PDF output [true].</p>
<dt><code>-s,-translate </code></p>
<dd> Show translated virtual machine code [false].</p>
<dt><code>-twice </code></p>
<dd> Run LaTeX twice (to resolve references) [false].</p>
<dt><code>-twosided </code></p>
<dd> Use two-sided 3D lighting model for rendering [true].</p>
<dt><code>-u,-user string </code></p>
<dd> General purpose user string.</p>
<dt><code>-v,-verbose </code></p>
<dd> Increase verbosity level (can specify multiple times) [0].</p>
<dt><code>-version </code></p>
<dd> Show version; command-line only.</p>
<dt><code>-vibrateTime ms </code></p>
<dd> WebGL shift mode vibrate duration [25].</p>
<dt><code>-viewportmargin pair </code></p>
<dd> Horizontal and vertical 3D viewport margin [(0.5,0.5)].</p>
<dt><code>-wait </code></p>
<dd> Wait for child processes to finish before exiting [false].</p>
<dt><code>-warn string </code></p>
<dd> Enable warning; command-line only.</p>
<dt><code>-webgl2 </code></p>
<dd> Use webgl2 if available [false].</p>
<dt><code>-where </code></p>
<dd> Show where listed variables are declared [false].</p>
<dt><code>-wsl </code></p>
<dd> Run asy under the Windows Subsystem for Linux. [false].</p>
<dt><code>-xasy </code></p>
<dd> Interactive mode for xasy [false].</p>
<dt><code>-zoomPinchCap limit </code></p>
<dd> WebGL maximum zoom pinch [100].</p>
<dt><code>-zoomPinchFactor n </code></p>
<dd> WebGL zoom pinch sensitivity [10].</p>
<dt><code>-zoomfactor factor </code></p>
<dd> Zoom step factor [1.05].</p>
<dt><code>-zoomstep step </code></p>
<dd> Mouse motion zoom step [0.1]. </p>
</dl>
<h2>SEE ALSO</h2>
<p> Asymptote is documented fully in the asymptote Info page. The manual can also be accessed in interactive mode with the &quot;help&quot; command. </p>
<h2>AUTHOR</h2>
<p> Asymptote was written by Andy Hammerlindl, John Bowman, and Tom Prince. </p>
<p> This manual page was written by Hubert Chan for the Debian project (but may be used by others). </p>
<h2>Index</h2>
