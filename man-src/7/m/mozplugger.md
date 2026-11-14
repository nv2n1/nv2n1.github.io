---
title: "mozplugger(7)"
name: "mozplugger"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mozplugger/"
description: "mozplugger – a streaming multimedia plugin for UNIX mozilla"
---

<p>mozplugger &#8211; a streaming multimedia plugin for UNIX mozilla </p>
<h2>Description</h2>
<p><i>MozPlugger</i> is a Mozilla plugin which can show many types of multimedia inside your Mozilla. To accomplish this, MozPlugger uses external programs such as mplayer, xanim, mtv, timidity and tracker. </p>
<h2>Configure File</h2>
<p>You can configure mozplugger by changing the file <i>mozpluggerrc</i> which can be located in any of the following directories: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$HOME/.netscape/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$HOME/.mozilla/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$HOME/.opera/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$MOZILLA_HOME/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$OPERA_HOME/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/local/netscape/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/local/mozilla/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/local/netscape/</p>
<p> MozPlugger will use the first mozpluggerrc it finds and ignore any others. The search order is from top of the list above. </p>
<p> The format of <i>mozpluggerrc</i> is very simple. The general layout is to have one or more lines describing mime types followed by one or more lines describing commands used to handle those mime types. Lines beginning with # are considered comments and are ignored. Here is a simple example: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>video/mpeg: mpeg: Mpeg video</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>video/quicktime: qt,mov: Mpeg video</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>: xanim +W$window -Zr +q +Ze +f $file</p>
<p> Each line describing a mime type has three fields: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><br />
 <code>mime type</code> : <code>extensions</code> : <code>description</code> </p>
<dl>
<dt><code>mime type</code></p>
<dd>The mime type is the standardized name for the content type you want MozPlugger to handle. This must be the same type as the web server claims the file to be, or MozPlugger will not be used for that file, regardless of the extension. Note: Some web servers incorrectly report the wrong mime type, blame the web server adminstrator not mozplugger.</p>
<dt><code>extensions</code></p>
<dd>This is a comma separated list of extensions that should be associated with this particular mime type. The extensions are only used when a web server does not report what type of file it is, or when loading files directly from disk.</p>
<dt><code>description</code></p>
<dd>This is the description that shows up in about:plugins and in the application preferences section in Mozilla. </p>
<dt>Lines that describe what command to use for a mime type must begin</p>
<dd>with a whitespace and have two fields: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><br />
 <code>flags</code> : <code>command</code> </p>
<dt><code>flags</code></p>
<dd>This is a space separated list of flags associated with the command and tells mozplugger how to handle this command. See below for further details.</p>
<dt><code>command</code></p>
<dd>This is a command which is sent to /bin/sh when handling this mime type. Mozplugger assumes the command line starts with the name of an application followed by various arguments passed to that application. </p>
</dl>
<h2>Using M4</h2>
<p>When loading, MozPlugger will pass the mozpluggerrc file through m4, a general purpose macro processor (assuming m4 is installed). This provides the ablity to use macros within mozpluggerrc especially for those commonly used command lines. m4 brings text replacement, parameter substitution, file inclusion, string manipulation, conditional evaluation, arthemtic expressions, etc to mozpluggerrc. Please see m4 documentation for more details.</p>
<h2>Finding The Right Command</h2>
<p>When MozPlugger is called from your browser, it looks through the configuration file and finds a matching mime type. </p>
<p> When a matching mimetype is found, it tries to figure out which command to use. Commands that have the flags <code>loop, embed, noembed, link </code> and <code>fmatch </code> will be rejected if they do not match what is expected from the associated HTML code (see later for details). </p>
<p> In addition for a command to be choosen the application has to be available. That is, MozPlugger will assume the first word of the command is the name of an application and search $PATH for that application. If that application is not found MozPlugger will skip that command line. </p>
<p> Of the commands that remain, Mozplugger looks for the first command that has the <code>stream</code> flag set. If there is not such a command line, Mozplugger then downloads the file and picks the first (of the remaining) commands.</p>
<h2>When It Doesnt Work</h2>
<p>If for some reason the embedded object fails to be rendered in the browser, this could be a fault with the application as opposed to MozPlugger. To diagnosis the fault it is suggested that first you make sure that any output from the application will be visible to you by removing the <code>noisy</code> flag (if set in mozpluggerrc). </p>
<p> Next run the browser from the shell (xterm or equivalent) passing the appropriate browser command line flag to enable output from stdout and stderr to be displayed. </p>
<p> For example, for firefox the command line string is: </p>
<p>&nbsp;<wbr>&nbsp;<wbr> <code>firefox -debug </code> </p>
<p> This should allow any output from the application to be visible at the shell and hopefully lead to a diagnosis of the fault.</p>
<h2>Flags</h2>
<dl>
<dt><code>autostart</code></p>
<dd>This flag indicates that the command uses the $autostart environment variable. That is mozplugger will run the command on the assumption that the command/application will check the value of the $autostart environment variable. If this flag is not present and the HTML code for the embedded object indicates autostart is false, mozplugger will not run the command but instead draw a single start button.</p>
<dt><code>repeat</code></p>
<dd>This flag indicates that the command uses the $repeats environment variable. That is mozplugger will run the command on the assumption that the command/application will check the value of the $repeats environment variable and perform the repeats. If this flag is not set, mozplugger will perform the required number of repeats as indicated in the HTML code by calling the command $repeats times.</p>
<dt><code>loop</code></p>
<dd>This indicates that the command loops forever. If the HTML code for the embedded object indicates don&#8217;t loop/repeat forever (e.g. the loop attribute is not present or not set to true), the command on this line will not be used.</p>
<dt><code>stream</code></p>
<dd>This indicates that this command can take an url. In this case, the environment variable $file contains the URL of the file to play and the browser does not download it. It is assumed that the command can handle the URL. Note: if a username and password is required for this URL, the command/application will have to obtain this as it is not passed to it from the browser.</p>
<dt><code>ignore_errors</code></p>
<dd>This flag tells MozPlugger to ignore the exit status of the command. For example is mozplugger is repeating the command &#8216;n&#8217; times and the command exits with an error, normally mozplugger would terminate at this time. With this flag set, mozplugger continues the repeats.</p>
<dt><code>noisy</code></p>
<dd>This flag tells MozPlugger to redirect the stdout and stderr of the command to /dev/null.</p>
<dt><code>swallow (name)</code></p>
<dd>This flag tells mozplugger that the command will open a window with the specified name and that Mozplugger will then move this window inside your browser. If name is prefixed with &#8216;=&#8217; then mozplugger looks for an exact match with the window name, if the prefix is &#8216;~&#8217; then mozplugger looks for a case insensitive match, if prefixed with &#8216;*&#8217; then mozplugger looks for a window name that starts with &#8216;name&#8217; and is case insensitive. If none of these prefixes then, mozplugger checks if name occurs anywhere in the window name, but is case sensitive. Note any spaces between the brackets are counted as part of the window name. The window name to use in mozpluggerrc can be obtained by using the utility xprop(). Run the command in question, type &quot;xprop WM_CLASS&quot; at a shell prompt and then click on the application window.</p>
<dt><code>fmatch (string)</code></p>
<dd>This flag defines a command that will be used only if the filename or url (i.e. $file) contains &#8216;string&#8217;. If &#8216;string&#8217; is prefixed with &#8216;*&#8217; then mozplugger defines a match when the file starts with &#8216;string&#8217; (the check is case insensitive). If &#8216;string&#8217; is prefixed with &#8216;%&#8217; then mozplugger defines a match when the file ends with &#8216;string&#8217; (the check is case insenstive and ignores any parameters at the end of a url {i.e. &#8216;?xxx=yyy&#8217;}). If none of these prefixes then mozplugger defines a match when the &#8216;string&#8217; is found somewhere in the file (but this time match is case sensitive). Note any spaces between the brackets are counted as part of the &#8216;string&#8217;.</p>
<dt><code>nokill</code></p>
<dd>This flag tells MozPlugger to not try to kill the command when leaving the page, and to not start the command in a loop. This is normally used for applications that are not swallowed and can play multiple files, such as xmms.</p>
<dt><code>exits</code></p>
<dd>This flag tells MozPlugger that the command will exits straight away and hence does not need to be killed when leaving the page, and to not start the command in a loop. This is normally used for applications that just display an image in the $window and then exit.</p>
<dt><code>fill</code></p>
<dd>This flag tells MozPlugger to maximize a swallowed window.</p>
<dt><code>maxaspect</code></p>
<dd>This flag tells Mozplugger to maximize a swallowed window while keeping the width/height ratio constant.</p>
<dt><code>controls</code></p>
<dd>This flag tells MozPlugger to draw controls and is typically used with audio files to display a controller with the buttons play, pause and stop. Be aware if the embedded object has no sub-window defined within the browser&#8217;s window (e.g. if the HTML uses the tag hidden = true) then the controls will not appear.</p>
<dt><code>embed</code></p>
<dd>This flags tells Mozplugger to only use this command if the associated HTML refers to an embedded object that is a small part of a HTML page.</p>
<dt><code>noembed</code></p>
<dd>This flags tells Mozplugger to only use this command if the associated HTML refers to a separate window that only contains the object.</p>
<dt><code>links</code></p>
<dd>This flag tells Mozplugger to only use this command for embedded objects that are really links to external applications (such objects typically use the target and href variables to indicate a clickable link). Embedded Quicktime objects sometimes use this mechanism.</p>
<dt><code>hidden</code></p>
<dd>In conjunction with the swallow keyword, this tells the plugin to swallow windows which are not visible yet. </p>
</dl>
<h2>Variables</h2>
<p>MozPlugger gives some variables to /bin/sh when running the command, these variables are: </p>
<dl>
<dt><code>$autostart</code></p>
<dd>This variable contains 1 or 0. When set to 1 it indicates that the command should start playing/showing the associated media. By default it is 0 if controls flag is present and 1 otherwise, but it is overridden if the associated HTML contains the attribute autostart or autoplay. Command/applications that use this environment variable should also have the <code>autostart </code> flag set.</p>
<dt><code>$repeats</code></p>
<dd>This variable contains how many times the file should be played. By default it is once, but it is overridden if the associated HTML contains the attribute loop, numloop or playcount. Command/applications which use this environment variable should also have the <code>repeat</code> flag set.</p>
<dt><code>$window</code></p>
<dd>This is the X window Mozilla has given the plugin. This can be used with applications such as MPlayer to display graphics inside the mozilla window. Be aware if the embedded object has no sub-window defined within the browser&#8217;s window (e.g. if the HTML uses the tag hidden = true) then the variable will have the value zero (null).</p>
<dt><code>$hexwindow</code></p>
<dd>Same as $window except the value is expressed as an hexidecimal string in the form 0xNNNNNN where NNNNNN is the hexadecimal digits.</p>
<dt><code>$width</code></p>
<dd>This is the horizontal resolution in pixels and is taken from the width attribute in the HTML code.</p>
<dt><code>$height</code></p>
<dd>This is the vertical resolution in pixels and is taken from the height attribute in the HTML code.</p>
<dt><code>$file</code></p>
<dd>This is the file to play. If the command has the <code>stream</code> flag set, this variable contains the URL of the file to play. This is taken from the associated HTML code. The value is that of the attribute src, data, href, qtsrc, filename, url or location depending on which is present and whether the &lt;EMBED&gt; or &lt;OBJECT&gt; tag is used. If the <code>stream</code> is not set, this variable contains a local temporary file that the browser has created.</p>
<dt><code>$fragment</code></p>
<dd>This is the part of the original URL that appears after the # if it exists. Sometimes this contains additional information that could be useful for the application e.g. starting page number in a pdf document</p>
<dt><code>$mimetype</code></p>
<dd>This variable contains the mime type of $file.</p>
<dt><code>$VAR_&lt;parameter_name&gt;</code></p>
<dd>All the parameters of the &lt;EMBED&gt; or &lt;OBJECT&gt; tags are made available in mozpluggerrc through environment variables. For example the parameter loop=&quot;1&quot; in an &lt;EMBED&gt; tag defines the variable VAR_loop=1. </p>
</dl>
<h2>Bugs</h2>
<p>You have to remove ~/.netscape/plugin-list or ~/.mozilla/firefox/pluginreg.dat after changing the configuration, or nothing will happen. This is a Netscape/Mozilla/Firefox bug, not a MozPlugger bug. </p>
<p> Netscape 3.x will not play anything for &lt;EMBED&gt; tags for which height or width are zero. This too is a Netscape bug. </p>
<p> Occassionally you may notice some zombie mozplugger-helper processes (defunct), this is not a bug, this is by design. The zombie processes occur when either the application exits or when using <code>nokill</code> flag (without exiting the page with the embedded object). The zombie(s) are reaped when closing the web page containing the associated embedded objects. </p>
<p> If using behind a non-transparent HTTP proxy, it may be found that the commands using the <code>stream</code> flag do not work. This is because the proxy settings are not passed to the application in the command line. To work around this situation, dont use the stream flag OR edit the mozpluggerrc file and passed in necessary proxy setiings via the command line.</p>
<h2>Authors</h2>
<p>Fredrik Hubinette, hubbe [at] hubbe.net<br />
 Louis Bavoil, louis [at] bavoil.net<br />
 Peter Leese, peter [at] leese.net</p>
