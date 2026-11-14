---
title: "gnash(1)"
name: "gnash"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnash/"
---

<h2>NAME</h2>

 gnash, gtk-gnash, qt4-gnash, dump-gnash, fb-gnash, sdl-gnash, gnash-gtk-launcher, gnash-qt-launcher - GNU Flash (SWF) Player

<h2>Synopsis</h2>

 <pre><code>
gnash[option]...[URL]
</code></pre>

<h2>DESCRIPTION</h2>

 Run the SWF movie player.
<dl>
<dt>-h, --help
<dd> Print usage info.
<dt>-V, --version
<dd> Print the version number, and the configuration, of the Gnash player. Please provide this information when submitting bug reports.
<dt>-s factor, --scale factor
<dd> Scale the movie up/down by the specified factor.
<dt>-c
<dd> Produce a core file instead of letting SDL trap it
<dt>-d num, --delay num
<dd> Number of milliseconds to delay in main loop.
<dt>-v, --verbose
<dd> Be verbose; i.e. print log messages to stdout.
<dt>-a
<dd> Be very verbose about movie action execution. Must be used in conjunction with -v.
<dt>-p
<dd> Be very verbose about parsing. Must be used in conjunction with -v.
<dt>-A file
<dd> Audio dump file (wave format).
<dt>--hwaccel none|vaapi|xv
<dd> Hardware Video Accelerator to use none|vaapi|xv|omap (default: none)
<dt>-x xid, --xid xid
<dd> The XID of the parent window Gnash should use instead of creating a new one. This is only used when embedding the player into another window.
<dt>-w, --writelog
<dd> Write the gnash-dbg.log debug log to disk. By default the plugin writes its log in your home directory when using a launcher from GNOME or KDE.
<dt>-j width, --width width
<dd> Set the width of the window. This is only used when embedding the player into another window.
<dt>-k height, --height height
<dd> Set the height of the window. This is only used when embedding the player into another window.
<dt>-X x-pos, --x-pos x-pos
<dd> Set window x position.
<dt>-Y y-pos, --y-pos y-pos
<dd> Set window y position.
<dt>-1, --once
<dd> Play once; exit when/if movie reaches the last frame.
<dt>-g
<dd> Start Gnash with a Flash debugger console so one can set breakpoints or watchpoints.
<dt>-r [0|1|2|3]
<dd> 0 disables rendering and sound (good for batch tests). 

 1 enables rendering, disable sound. 

 2 disables rendering, enable sound. 

 3 enables rendering and sound (default setting).
<dt>-M ffmpeg|gst, --media ffmpeg|gst
<dd> The media handler to use (default: ffmpeg).
<dt>-R agg|cairo|opengl, --renderer agg|cairo|opengl
<dd> The renderer to use (default: agg).
<dt>-t sec, --timeout sec
<dd> Timeout and exit after the specified number of seconds.
<dt>-u url, --real-url url
<dd> Set &quot;real&quot; url of the movie (useful for downloaded movies).
<dt>-U url, --base-url url
<dd> Set &quot;base&quot; url for this run (used to resolve relative urls, defaults to movie url)
<dt>-P param, --param param
<dd> Set parameter (ie. &quot;FlashVars=A=1&amp;b=2&quot;)
<dt>-F x:y, --fd x:y
<dd> Set file descriptors to use for external communications. x is use by the player to send commands to the plugin, y is used by the plugin to send commands to the standalone player.
<dt>--max-advances num
<dd> Exit after specified number of frame advances.
<dt>--fullscreen
<dd> Start in fullscreen mode.
<dt>--hide-menubar
<dd> Start without displaying the menu bar.
<dt>--screenshot list
<dd> Set a list of frame advances to be saved as screenshots. The list must be comma-separated. Valid values are integers and the phrase &quot;last&quot;. If &quot;last&quot; is specified, the final frame before exit is saved. Invalid values are ignored. Frame numbers apply to the sequence of frames as the SWF is executed, not the frame sequence defined in the SWF. Use in combination with --screenshot-file to specify output filename.
<dt>--screenshot-file file
<dd> Specify the output pattern for screenshot filenames. The token %f in a pattern will be replaced with a frame identifier. If you specify multiple frames and do not use %f, the file will be overwritten for each screenshot. If this option is not specified but screenshots are requested, a default filename will be used.</dl>

<h3>KEYS</h3>

<dl>
<dt>CTRL-Q
<dd> Quit/Exit.
<dt>CTRL-W
<dd> Quit/Exit.
<dt>CTRL-P
<dd> Toggle pause.
<dt>CTRL-R
<dd> Restart the movie.
<dt>CTRL-L
<dd> Force immediate redraw.
<dt>CTRL-F
<dd> Toggle fullscreen. ESC also exits fullscreen.
<dt>CTRL-O
<dd> Save a spontaneous screenshot. If no screenshots were requested from the command line, a default filename is used. Otherwise, the same filename pattern is used for requested and spontaneous screenshots.</dl>
 

 Flash is a registered trademark of Adobe Corporation. 

<h2>Index</h2>


