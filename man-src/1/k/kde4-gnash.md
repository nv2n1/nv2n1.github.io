---
title: "kde4-gnash(1)"
name: "kde4-gnash"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kde4-gnash/"
---

<h2>NAME</h2>

 gnash, gtk-gnash, kde4-gnash - GNU Flash (SWF) Player

<h2>Synopsis</h2>

 <pre><code>
gnash[option]...[URL]
</code></pre>

<h2>DESCRIPTION</h2>

 Run the SWF movie player.
<dl>
<dt>-h
<dd> Print usage info.
<dt>-s factor
<dd> Scale the movie up/down by the specified factor.
<dt>-d num
<dd> Number of milliseconds to delay in main loop.
<dt>-a
<dd> Be very verbose about movie action execution. Must be used in conjunction with -v.
<dt>-p
<dd> Be very verbose about parsing. Must be used in conjunction with -v.
<dt>-x xid, --xid xid
<dd> The XID of the parent window Gnash should use instead of creating a new one. This is only used when embedding the player into another window.
<dt>-j width, --width width
<dd> Set the width of the window. This is only used when embedding the player into another window.
<dt>-k height, --height height
<dd> Set the height of the window. This is only used when embedding the player into another window.
<dt>-v
<dd> Be verbose; i.e. print log messages to stdout.
<dt>-g
<dd> Start Gnash with a Flash debugger console so one can set breakpoints or watchpoints.
<dt>-w
<dd> Write the gnash-dbg.log debug log to disk. By default the plugin writes its log in your home directory when using a launcher from GNOME or KDE.
<dt>-1, --once
<dd> Play once; exit when/if movie reaches the last frame.
<dt>-r [0|1|2]
<dd> 0 disables rendering and sound (good for batch tests). 

 1 enables rendering and sound (default setting). 

 2 enables rendering and disables sound.
<dt>-t sec, --timeout sec
<dd> Timeout and exit after the specified number of seconds.
<dt>-u, --real-url
<dd> Set &quot;real&quot; url of the movie (useful for downloaded movies).
<dt>-U, --base-url
<dd> Set &quot;base&quot; url for this run (used to resolve relative urls, defaults to movie url)
<dt>-P param, --param param
<dd> Set parameter (ie. &quot;FlashVars=A=1&amp;b=2&quot;)
<dt>-F, --fd x:y
<dd> Set file descriptors to use for external communications. x is use by the player to send commands to the plugin, y is used by the plugin to send commands to the standalone player.
<dt>--version
<dd> Print the version number, and the configuration, of the Gnash player. Please provide this information when submitting bug reports.
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
<dt>CTRL-F
<dd> Toggle fullscreen. ESC also exits fullscreen.
<dt>CTRL-O
<dd> Save a spontaneous screenshot. If no screenshots were requested from the command line, a default filename is used. Otherwise, the same filename pattern is used for requested and spontaneous screenshots.</dl>
 

 Flash is a registered trademark of Adobe Corporation. 

<h2>Index</h2>


