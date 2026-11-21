---
title: "gliv(1)"
name: "gliv"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gliv/"
description: "gliv – An OpenGL Image Viewer"
---
<h2>NAME</h2>
<p> gliv - An OpenGL Image Viewer  </p>
<h2>SYNOPSIS</h2>
<p> <code>gliv</code> [OPTIONS]... [FILES]...  </p>
<h2>DESCRIPTION</h2>
<p> <i>gliv</i> uses gdk-pixbuf to load images and OpenGL to render them. It allows to do some moving, rotating, zooming and slide show.  </p>
<h2>OPTIONS</h2>
<p> The options are first set to their default values, &quot;off&quot; for flags, then read either from ~/.glivrc or /etc/glivrc or a configuration file specified on the command line, and finally read from the command line. <br />
 Omitting the argument for an option that takes an &quot;on|off&quot; argument (flags) is like giving it &quot;on&quot;, so --foo is the same as --foo=on if foo is an on|off flag. </p>
<dl>
<dt><code>-h, --help</code></dt>
<dd> <p> Print help and exit. </p>
 </dd>
<dt><code>-V, --version</code></dt>
<dd> <p> Print version and exit. </p>
 </dd>
<dt><code>-a, --add-all[=on|off]</code></dt>
<dd> <p> Add all files in the directory. With this option, when you open a file on the command line or with the open dialog, all others files in the directory are added as well. </p>
 </dd>
<dt><code>-R, --recursive[=on|off]</code></dt>
<dd> <p> Recursive directory traversal. If <i>gliv</i> tries to load a direcory, it will also load every image all its subdirectories. </p>
 </dd>
<dt><code>-S, --sort[=on|off]</code></dt>
<dd> <p> Show images in sorted order. The images list will be sorted before the slide show. </p>
 </dd>
<dt><code>-s, --shuffle[=on|off]</code></dt>
<dd> <p> Show images in random order. The images list will be shuffled before the slide show. </p>
 </dd>
<dt><code>-F, --force-load[=on|off]</code></dt>
<dd> <p> Try to load every file. When loading a file, the loader is chosen according to the filename extension in order to optimize the loading time. If the extension is unknown, the file is ignored, with this option <i>gliv</i> will always try to load the file. </p>
 </dd>
<dt><code>-C, --client[=on|off]</code></dt>
<dd> <p> Connect to an already running <i>gliv</i>. With this option, <i>gliv</i> will open the files passed in the arguments in the <i>gliv</i> server window. It can also be used with the -0 option. The <i>gliv</i> server is the latest launched <i>gliv</i> or the one which has been chosen using the Options menu. </p>
 </dd>
<dt><code>-e, --build-menus[=on|off]</code></dt>
<dd> <p> No images menu at startup. Disabling the images menus creation at startup makes it faster, especially with many files on the command line. </p>
 </dd>
<dt><code>-g, --glivrc[=FILE]</code></dt>
<dd> <p> Use this configuration file or none. Specify it to disable loading of the rc file. With a filename as argument it will use it as a configuration file. </p>
 </dd>
<dt><code>-w, --slide-show[=on|off]</code></dt>
<dd> <p> Start the slide show immediately. This way you will not have to start it manually from the menu. </p>
 </dd>
<dt><code>-0, --null[=on|off]</code></dt>
<dd> <p> Read null-terminated filenames. This can be used with &quot;find -print0&quot; or with &quot;tr &#8216;\n&#8217; &#8216;\0&#8217;&quot; when you have a very long list of filenames to pass to <i>gliv</i>. Unlike <a href="/docs/linux/man/1-xargs/">xargs</a>(1) it allows an unlimited number of filenames. </p>
 </dd>
<dt><code>-o, --collection[=FILE]</code></dt>
<dd> <p> Output a collection. With this option, <i>gliv</i> creates a collection from the loaded files and outputs it to stdout or in the specified file. </p>
 </dd>
<dt><code>-G, --geometry=GEOMETRY</code></dt>
<dd> <p> Initial window geometry. This option can be used to specify the position and dimension of the <i>gliv</i> window. It expects a geometry argument in the XParseGeometry(3X11) format like: 640x480+20-30 for example. </p>
 </dd></dl>
<h2>COLLECTIONS</h2>
<p> Starting with version 1.8, <i>gliv</i> supports a file format called &quot;GLiv collection&quot;. It contains an images list and the associated thumbnails, this way, when you load a collection the images menus rebuilding is faster since it does not have to make thumbnails. <br />
 <i>gliv</i> supports also transparent decompression, so the collections can be compressed in bzip2, gzip or <a href="/docs/linux/man/1-compress/">compress</a>(1) provided that you have the corresponding decompressor.  </p>
<h2>CONTROLS</h2>
<p> ESC, q : Quit <br />
 f : Full-screen/window <br />
 +/=/- : Zoom in/in/out <br />
 n/p : Next/previous image <br />
 Pause : Start/stop the slide show <br />
 l : Reduce the image to the window <br />
 M : Maximize the image to the window <br />
 m : Make the image fit the window <br />
 r : Reset position and size <br />
 b : Toggle display of the menu bar <br />
 i : Toggle display of the info bar <br />
 s : Toggle display of the scrollbars <br />
 a : Toggle display of the alpha checks <br />
 h : Toggle display of the help box <br />
 w : Toggle display of floating windows <br />
 o : Display the open dialog <br />
 g : Display the image selector <br />
 t : Display the options dialog <br />
 d : Hide the cursor <br />
 u : Undo <br />
 y : Redo <br />
 c : Clear the history <br />
 Delete : Delete the current file <br />
 C-up : Rotate by +90 degrees <br />
 C-down : Rotate by -90 degrees <br />
 C-left : Rotate by +0.1 degree <br />
 C-right: Rotate by -0.1 degree <br />
 z : Horizontal flip <br />
 e : Vertical flip <br />
 </p>
<p> The first mouse button and the arrow keys will move the image unless the Control key is pressed. In which case the image will be rotated around the window center. <br />
 </p>
<p> Your mouse wheel (if supported) will zoom the image and switch it when you press the button. <br />
 </p>
<p> You can also zoom by dragging the mouse vertically while holding Shift and the first button. <br />
 </p>
<p> Space and Backspace act like n and p. <br />
 </p>
<p> Draw a rectangle with the third button and <i>gliv</i> will zoom in it. <br />
 </p>
<h2>FILE</h2>
<p> <code>~/.glivrc</code> - This file is absolutely not mandatory.  </p>
<h2>AUTHOR</h2>
<p> Guillaume Chazarain &lt;guichaz [at] yahoo.fr&gt; <br />
 See <a rel="nofollow" href="http://guichaz.free.fr/gliv">http://guichaz.free.fr/gliv</a> </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">COLLECTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">CONTROLS</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">FILE</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">AUTHOR</a></dt>
<dd>  </dd></dl>
