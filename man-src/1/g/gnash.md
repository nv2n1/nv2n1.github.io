---

title: "gnash(1)"
name: "gnash"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnash/"
---

gnash, gtk-gnash, qt4-gnash, dump-gnash, fb-gnash, sdl-gnash, gnash-gtk-launcher, gnash-qt-launcher - GNU Flash (SWF) Player

<h2>Synopsis</h2>

 <pre><code>
gnash[option]...[URL]
</code></pre>

<h2>DESCRIPTION</h2>

 Run the SWF movie player.
<dl>
<dt>-h, --help
</dt><dd> Print usage info.
</dd><dt>-V, --version
</dt><dd> Print the version number, and the configuration, of the Gnash player. Please provide this information when submitting bug reports.
</dd><dt>-s factor, --scale factor
</dt><dd> Scale the movie up/down by the specified factor.
</dd><dt>-c
</dt><dd> Produce a core file instead of letting SDL trap it
</dd><dt>-d num, --delay num
</dt><dd> Number of milliseconds to delay in main loop.
</dd><dt>-v, --verbose
</dt><dd> Be verbose; i.e. print log messages to stdout.
</dd><dt>-a
</dt><dd> Be very verbose about movie action execution. Must be used in conjunction with -v.
</dd><dt>-p
</dt><dd> Be very verbose about parsing. Must be used in conjunction with -v.
</dd><dt>-A file
</dt><dd> Audio dump file (wave format).
</dd><dt>--hwaccel none|vaapi|xv
</dt><dd> Hardware Video Accelerator to use none|vaapi|xv|omap (default: none)
</dd><dt>-x xid, --xid xid
</dt><dd> The XID of the parent window Gnash should use instead of creating a new one. This is only used when embedding the player into another window.
</dd><dt>-w, --writelog
</dt><dd> Write the gnash-dbg.log debug log to disk. By default the plugin writes its log in your home directory when using a launcher from GNOME or KDE.
</dd><dt>-j width, --width width
</dt><dd> Set the width of the window. This is only used when embedding the player into another window.
</dd><dt>-k height, --height height
</dt><dd> Set the height of the window. This is only used when embedding the player into another window.
</dd><dt>-X x-pos, --x-pos x-pos
</dt><dd> Set window x position.
</dd><dt>-Y y-pos, --y-pos y-pos
</dt><dd> Set window y position.
</dd><dt>-1, --once
</dt><dd> Play once; exit when/if movie reaches the last frame.
</dd><dt>-g
</dt><dd> Start Gnash with a Flash debugger console so one can set breakpoints or watchpoints.
</dd><dt>-r [0|1|2|3]
</dt><dd> 0 disables rendering and sound (good for batch tests). 
 1 enables rendering, disable sound. 
 2 disables rendering, enable sound. 
 3 enables rendering and sound (default setting).
</dd><dt>-M ffmpeg|gst, --media ffmpeg|gst
</dt><dd> The media handler to use (default: ffmpeg).
</dd><dt>-R agg|cairo|opengl, --renderer agg|cairo|opengl
</dt><dd> The renderer to use (default: agg).
</dd><dt>-t sec, --timeout sec
</dt><dd> Timeout and exit after the specified number of seconds.
</dd><dt>-u url, --real-url url
</dt><dd> Set &quot;real&quot; url of the movie (useful for downloaded movies).
</dd><dt>-U url, --base-url url
</dt><dd> Set &quot;base&quot; url for this run (used to resolve relative urls, defaults to movie url)
</dd><dt>-P param, --param param
</dt><dd> Set parameter (ie. &quot;FlashVars=A=1&amp;b=2&quot;)
</dd><dt>-F x:y, --fd x:y
</dt><dd> Set file descriptors to use for external communications. x is use by the player to send commands to the plugin, y is used by the plugin to send commands to the standalone player.
</dd><dt>--max-advances num
</dt><dd> Exit after specified number of frame advances.
</dd><dt>--fullscreen
</dt><dd> Start in fullscreen mode.
</dd><dt>--hide-menubar
</dt><dd> Start without displaying the menu bar.
</dd><dt>--screenshot list
</dt><dd> Set a list of frame advances to be saved as screenshots. The list must be comma-separated. Valid values are integers and the phrase &quot;last&quot;. If &quot;last&quot; is specified, the final frame before exit is saved. Invalid values are ignored. Frame numbers apply to the sequence of frames as the SWF is executed, not the frame sequence defined in the SWF. Use in combination with --screenshot-file to specify output filename.
</dd><dt>--screenshot-file file
</dt><dd> Specify the output pattern for screenshot filenames. The token %f in a pattern will be replaced with a frame identifier. If you specify multiple frames and do not use %f, the file will be overwritten for each screenshot. If this option is not specified but screenshots are requested, a default filename will be used.</dd></dl>

<h3>KEYS</h3>

<dl>
<dt>CTRL-Q
</dt><dd> Quit/Exit.
</dd><dt>CTRL-W
</dt><dd> Quit/Exit.
</dd><dt>CTRL-P
</dt><dd> Toggle pause.
</dd><dt>CTRL-R
</dt><dd> Restart the movie.
</dd><dt>CTRL-L
</dt><dd> Force immediate redraw.
</dd><dt>CTRL-F
</dt><dd> Toggle fullscreen. ESC also exits fullscreen.
</dd><dt>CTRL-O
</dt><dd> Save a spontaneous screenshot. If no screenshots were requested from the command line, a default filename is used. Otherwise, the same filename pattern is used for requested and spontaneous screenshots.</dd></dl>
 

 Flash is a registered trademark of Adobe Corporation.
