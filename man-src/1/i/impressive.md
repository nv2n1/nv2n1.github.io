---
title: "impressive(1)"
name: "impressive"
section: "1"
letter: "i"
url: "/docs/linux/man/1-impressive/"
description: "Impressive – presentation tool with eye candy"
---

<h2>NAME</h2>
<p> Impressive &#8211; presentation tool with eye candy</p>
<h2>SYNOPSIS</h2>
<p> <code>impressive</code> [OPTIONS&#8230;] FILES&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Impressive is a simple presentation program that displays slideshows of image files (JPEG, PNG, TIFF and BMP) or PDF documents. Rendering is done via OpenGL, which allows for some &quot;eye candy&quot; effects. </p>
<h2>OPTIONS</h2>
<p> <code>-a </code><i>&lt;seconds&gt;</i> or <code>&#8211;auto </code><i>&lt;seconds&gt;</i></p>
<dl>
<dt>
<dd> Automatically advance to the next page after the given number of seconds. Together with the <code>-w</code> option (described below), this can be used to create automatic slideshows.</dl>
<p> <code>-A </code><i>&lt;X&gt;</i>:<i>&lt;Y&gt;</i> or <code>&#8211;aspect </code><i>&lt;X&gt;</i>:<i>&lt;Y&gt;</i></p>
<dl>
<dt>
<dd> Specifies the display aspect ratio. Normally, Impressive assumes that the pixel aspect ratio is 1:1 (square pixels), regardless of the display resolution that has been set up. If a resolution has been selected that doesn&#8217;t match the display&#8217;s aspect ratio, the screen will be distorted. To overcome this, this option may be used to manually specify the display aspect ratio, e.g. &quot;-A 16:9&quot;. Note that this option has no effect if Xpdf is used for rendering.</dl>
<p> <code>-b</code> or <code>&#8211;noback</code></p>
<dl>
<dt>
<dd> Disabled background rendering. By default, Impressive will pre-render all pages in a separate background thread while the presentation runs. If this option is specified, it will instead render all pages immediately on startup. This option has no effect if caching is disabled (<code>&#8211;cache none</code>, see below).</dl>
<p> <code>-B </code><i>&lt;ms&gt;</i> or <code>&#8211;boxfade </code><i>&lt;ms&gt;</i></p>
<dl>
<dt>
<dd> Sets the duration (in milliseconds) of the highlight box fade-in/:fade-out animation. Default value: 100 ms.</dl>
<p> <code>-c </code><i>&lt;mode&gt;</i> or <code>&#8211;cache </code><i>&lt;mode&gt;</i></p>
<dl>
<dt>
<dd> Specifies the page cache mode to use. Valid options are:<br />
 <code>none</code></p>
<dl>
<dt>
<dd> Disables page caching altogether, only the current and the following page will be kept in RAM. Jumping between pages will be very slow, because Impressive will need to render the requested pages on the fly. In addition, the overview page won&#8217;t be complete until every page has been shown at least once.</dl>
<p> <code>memory</code></p>
<dl>
<dt>
<dd> Caches all page images in memory. This is the fastest method, but it requires very large amounts of memory (about 3 MiB per page at 1024&#215;768 resolution).</dl>
<p> <code>disk</code></p>
<dl>
<dt>
<dd> Like above, but uses a temporary file rather than memory for storage. This is the default.</dl>
<p> <code>persistent</code></p>
<dl>
<dt>
<dd> Uses a permanent cache file for caching. This file will not be deleted when Impressive quits and will be reused on subsequent invocations. The default name for the cache file is derived like the names for Info Scripts (see below for an explanation), but with a <code>.cache</code> file name extension instead of <code>.info</code>. This method is a little bit slower than <code>disk</code> mode, but the time span until the overview page is fully populated will be significantly decreased if Impressive is ran again with the same input files and options.</dl>
<p> The mode name may be abbreviated at will, down to one character. Thus, <code>&#8211;cache persistent</code>, <code>-c persist</code> and even <code>-cp</code> are all synonyms.</dl>
<p> <code>-C </code><i>&lt;filename&gt;</i>[:<i>&lt;X&gt;</i>,<i>&lt;Y&gt;</i>] or <code>&#8211;cursor </code><i>&lt;filename&gt;</i>[:<i>&lt;X&gt;</i>,<i>&lt;Y&gt;</i>]</p>
<dl>
<dt>
<dd> This option can be used to specify the path to an image file (typically a transparent .png) that shall be used as the mouse cursor instead of the default one. Optionally, the hotspot may be specified (this is the position inside the cursor image where the real mouse position is located). Example: <code>&#8211;cursor mycursor.png:2,4</code></dl>
<p> <code>-d </code><i>&lt;time&gt;</i> or <code>&#8211;duration </code><i>&lt;time&gt;</i></p>
<dl>
<dt>
<dd> Specifies the expected run time of the presentation. The <i>time</i> parameter can be either a number of seconds or a human-readable time like <code>1:23</code> (1 minute and 23 seconds), <code>4:56h</code> (4 hours and 56 minutes), <code>3m45s</code> (3 minutes and 45 seconds), <code>5m</code> (5 minutes) or <code>1:23:45</code> (1 hour, 23 minutes and 45 seconds).<br />
 If an expected duration is specified, Impressive will show a semi-transparent green progress bar at the lower edge of the screen, indicating how much time has already passed. If the time is up, the bar will occupy the whole edge and fade to yellow (at 125% of the expected time) to red (at 150% or more).</dl>
<p> <code>-D </code><i>&lt;ms&gt;</i> or <code>&#8211;mousedelay </code><i>&lt;ms&gt;</i></p>
<dl>
<dt>
<dd> Sets the time (in milliseconds) the mouse cursor is shown in fullscreen mode if it is not moved. Default value: 3000 ms.</dl>
<p> <code>-e</code> or <code>&#8211;noext</code></p>
<dl>
<dt>
<dd> OpenGL normally only supports textures with power-of-two dimensions. This means that for a 1024&#215;768 screen, the actual texture size will be 1024&#215;1024, for 1600&#215;1200 it will even be 2048&#215;2048. To overcome this limit and save texture memory, Impressive will automatically use the OpenGL extensions <code>GL_ARB_texture_rectangle</code> (available on most graphics cards) or <code>GL_ARB_texture_non_power_of_two</code> (available on modern graphics cards with current drivers). If these cause any trouble, the <code>-e</code> option may be used to prevent Impressive from using the problematic extensions.</dl>
<p> <code>-f</code> or <code>&#8211;fullscreen</code></p>
<dl>
<dt>
<dd> Toggles fullscreen mode. By default, fullscreen mode is activated, and can be deactivated using this switch.
</dl>
<p> <code>-F </code><i>&lt;file&gt;</i> or <code>&#8211;font </code><i>&lt;file&gt;</i></p>
<dl>
<dt>
<dd> Impressive uses some kind of text OSD to overlay the current page number and title (if available) on the overview page. This option can be used to specify a TrueType font file (.ttf) to use for the OSD. If the path specified doesn&#8217;t directly point to a useable font file, Impressive will try to search the system font directories. It assumes that all fonts are stored below <code>/:usr/:share/:fonts</code>, <code>/:usr/:local/:share/:fonts</code> or <code>/:usr/:X11R6/:lib/:X11/:fonts/:TTF</code> for this purpose (the latter one is useful for Mac OS X systems specifically). If this option is not specified, any of <code>DejaVuSans.ttf</code> or <code>Vera.ttf</code> (the typical file name of Bitstream Vera Sans) will be used as a default.</dl>
<p> <code>-g </code><i>&lt;width&gt;</i>x<i>&lt;height&gt;</i> or <code>&#8211;geometry </code><i>&lt;width&gt;</i>x<i>&lt;height&gt;</i></p>
<dl>
<dt>
<dd> Sets the screen size or resolution Impressive shall use (in pixels). If <code>xrandr</code> is installed, the default screen size for fullscreen mode is the current screen resolution; on other platforms, Impressive uses the highest resolution available to the graphics system. If a standard resolution cannot be determined, the default is 1024&#215;768 pixels. Note that this option is <i>not</i> the standard X &quot;geometry&quot; option and does therefore not support window positioning (e.g. <code>-g 800&#215;600+0-0</code> will <i>not</i> work!).</dl>
<p> <code>-G </code><i>&lt;gamma&gt;</i>[:<i>&lt;blacklevel&gt;</i>] or <code>&#8211;gamma </code><i>&lt;gamma&gt;</i>[:<i>&lt;blacklevel&gt;</i>]</p>
<dl>
<dt>
<dd> Sets up the startup gamma and (optional) black level value. The black level is the original image&#8217;s intensity level (0&#8230;254) that is to be mapped to black in Impressive&#8217;s output. Note that gamma and black level adjustments may be unavailable or constrained on some systems.</dl>
<p> <code>-h</code> or <code>&#8211;help</code></p>
<dl>
<dt>
<dd> If this option is specified, Impressive writes a short command line help screen to standard output and does not start a presentation.</dl>
<p> <code>-i </code><i>&lt;page&gt;</i> or <code>&#8211;initialpage </code><i>&lt;page&gt;</i></p>
<dl>
<dt>
<dd> Specifies the page number to start with. The default value is 1 (start with the first page). If another value is specified, the page shown by Impressive right after initialization is not the first one of the PDF or image list. Additionally, pre-rendering (if enabled) will also start at the specified page.</dl>
<p> <code>-I </code><i>&lt;filename&gt;</i> or <code>&#8211;script </code><i>&lt;filename&gt;</i></p>
<dl>
<dt>
<dd> Overrides automatic derivation of the info script filename and specifies a script file directly.</dl>
<p> <code>-l</code> or <code>&#8211;listtrans</code></p>
<dl>
<dt>
<dd> If this option is specified, Impressive writes a list of all available transition classes to standard output and does not start a presentation. Transitions that are enabled by default are marked with a star (<code>*</code>) left of the class name.</dl>
<p> <code>-L </code><i>&lt;spec&gt;</i> or <code>&#8211;layout </code><i>&lt;spec&gt;</i></p>
<dl>
<dt>
<dd> Specified the OSD layout. Read below for an explanation of this option</dl>
<p> <code>-M</code> or <code>&#8211;minutes</code></p>
<dl>
<dt>
<dd> If this option is set, Impressive will show the on-screen timer (activated with the [T] key) only with 1 minute resolution. By default, it will show a timer with 1 second resolution.</dl>
<p> <code>-o </code><i>&lt;directory&gt;</i> or <code>&#8211;output </code><i>&lt;directory&gt;</i></p>
<dl>
<dt>
<dd> Do not display the presentation, but render it into a series of PNG image files inside the specified directory. The images will be generated in the current resolution as specified by the <code>-g</code> option. This option is useful if you&#8217;re going to give a presentation on a foreigh PC with an old, broken or otherwise problematic Xpdf or GhostScript installation: By generating images of the PDF pages you can ensure that no rendering bugs will happen on the target system.</dl>
<p> <code>-O </code><i>&lt;mode&gt;</i> or <code>&#8211;autooverview </code><i>&lt;mode&gt;</i></p>
<dl>
<dt>
<dd> Enables or disables automatic derivation of whether a page shall or shall not be shown on the overview page. This feature is based on the fact that some LaTeX presentation packages tag all pages with a title (that can be read by Impressive with the help of <code>pdftk</code>), except those that contain multiple reveal steps.<br />
 The following modes are available:<br />
 <code>off</code></p>
<dl>
<dt>
<dd> Disables automatic overview mode. All pages will be shown on the overview page by default. This is also the default setting.</dl>
<p> <code>first</code></p>
<dl>
<dt>
<dd> All pages with a PDF title will be shown on the overview page. The purpose is to show the <code>initial</code> state of multi-step slides on the overview page.</dl>
<p> <code>last</code></p>
<dl>
<dt>
<dd> All pages <code>before</code> a page with a PDF title will be shown on the overview page. The purpose is to show the <code>final</code> state of multi-step slides on the overview page.</dl>
<p> Again, the mode may be abbreviated arbitrarily, down to one character, just like with the <code>-c</code> option above..</dl>
<p> <code>-p </code><i>&lt;start&gt;</i>&#8211;<i>&lt;end&gt;</i> or <code>&#8211;pages </code><i>&lt;start&gt;</i>&#8211;<i>&lt;end&gt;</i></p>
<dl>
<dt>
<dd> Using this option, the range of the page displayed can be narrowed down. The presentation will start at the first page in the range. All pages outside of the range will not be shown on the overview page and will not be cached. However, they can be entered manually when cycling through the presentation. Due to the fact that these pages are uncached, preparation of the display will take considerably longer.</dl>
<p> <code>-P </code><i>&lt;path&gt;</i> or <code>&#8211;gspath </code><i>&lt;path&gt;</i></p>
<dl>
<dt>
<dd> This option can be used to override the Xpdf /: GhostScript path autodetection. The full path to the executable of either GhostScript (<code>gs</code> or <code>gs.exe</code>) or Xpdf&#8217;s <code>pdftoppm</code> utility must be specified.</dl>
<p> <code>-r </code><i>&lt;n&gt;</i> or <code>&#8211;rotate </code><i>&lt;n&gt;</i></p>
<dl>
<dt>
<dd> Display all pages rotated by <i>n</i>x90 degrees clockwise. Try <code>-r 1</code> or <code>-r 3</code> if you run into problems with PDFs generated by LaTeX on some Xpdf or GhostScript versions.</dl>
<p> <code>-R </code><i>&lt;X&gt;</i>x<i>&lt;Y&gt;</i> or <code>&#8211;meshres </code><i>&lt;X&gt;</i>x<i>&lt;Y&gt;</i></p>
<dl>
<dt>
<dd> Most effects subdivide the visible screen into a mesh of rectangular or quadratic pieces, each with its own coordinates and alpha blend values. Using this parameter, the resolution of the subdivision mesh can be defined. The default value is 48&#215;36. On slow machines, lower values like 24&#215;18 or 12&#215;9 can heavily speed up transition rendering at the cost of visual quality. On the other hand, higher values like 64&#215;48 or 96&#215;72 improve quality, but use much more CPU cycles.</dl>
<p> <code>-s</code> or <code>&#8211;scale</code> <i>(image input only)</i></p>
<dl>
<dt>
<dd> If a directory with image files is used as input, Impressive will scale down images that are too big for the screen. But by default, it will not scale up smaller images to fit the screen; it will leave a black border instead. This option overrides this setting and enables upscaling of smaller images.</dl>
<p> <code>-s</code> or <code>&#8211;supersample</code> <i>(PDF input only)</i></p>
<dl>
<dt>
<dd> This switch enables antialiasing by 4x supersampling instead of the normal multisampling method used by Xpdf or GhostScript. While this usually degrades both visual quality and performance, it may be necessary for circumventing white strips or moire-like patterns in gradients.</dl>
<p> <code>-S </code><i>&lt;pixels&gt;</i> or <code>&#8211;fontsize </code><i>&lt;pixels&gt;</i></p>
<dl>
<dt>
<dd> This option sets the size, in pixels, of the OSD font. The default value is 14.</dl>
<p> <code>-t </code><i>&lt;ms&gt;</i> or <code>&#8211;transition </code><i>&lt;trans1[,trans2&#8230;]&gt;</i></p>
<dl>
<dt>
<dd> Using this switch, the set of transitions Impressive will randomly draw at page changes can be specified. If only one transition class is specified, this class will be used for all pages that do not have another transition explicitly assigned in their page properties. Multiple transitions have to be separated by commas; they will be used in random order. The <code>-l</code> option can be used to get a list of available transitions.</dl>
<p> <code>-T </code><i>&lt;ms&gt;</i> or <code>&#8211;transtime </code><i>&lt;ms&gt;</i></p>
<dl>
<dt>
<dd> Sets the duration (in milliseconds) of page transitions. 0 (zero) disables transitions altogether. Default value: 1000 ms.</dl>
<p> <code>-u </code><i>&lt;seconds&gt;</i> or <code>&#8211;poll </code><i>&lt;seconds&gt;</i></p>
<dl>
<dt>
<dd> If this option is specified, the source file or directory will be checked for changed regularly. If a change in the input PDF file or any of the image files in the input image directory is detected, the page cache will be flushed and the current page as well as the info script will be reloaded. The current page&#8217;s transition will be shown between the old and the new version of the page.<br />
 The new PDF file must have at least as much pages as the old one; also, it should have the same aspect ratio. If the input is a directory, image files must not have disappeared.</dl>
<p> <code>-w</code> or <code>&#8211;wrap</code></p>
<dl>
<dt>
<dd> If this option is set, Impressive will &quot;wrap&quot; over to the first page after the last page. In other words, advancing to the next page at the end of the presentation will restart the whole presentation.</dl>
<p> <code>-Z </code><i>&lt;ms&gt;</i> or <code>&#8211;zoom </code><i>&lt;ms&gt;</i></p>
<dl>
<dt>
<dd> Sets the duration (in milliseconds) of the overview page zoom-in/:zoom-out effects. Default value: 250 ms.</dl>
<p> <code>&#8211;cachefile </code><i>&lt;filename&gt;</i></p>
<dl>
<dt>
<dd> Activates persistent cache mode and specifies the name of the cache file to use.</dl>
<h2>ARGUMENTS</h2>
<p> Following the options, the input file name(s) must be specified. Recognized file types are PDF, JPEG, PNG, TIFF, BMP and PGM/:PPM. If the name of a directory is put on the command line, all recognized image files (no PDF files!) in this directory will be played in alphanumeric order (case-insensitive). </p>
<p> In addition, Impressive can use a text file containing a list of files or directories to show: This text file must contain at most one file name per line; every character after a hash sign (<code>#</code>) is treated as a comment and will be ignored. If such a comment is put on the same line as an image file name, it will be used as the page&#8217;s title. List file names must be prefixed with an at sign (<code>@</code>) on the command line, e.g. <code>impressive @my_list_file</code>. </p>
<p> Impressive will also expand wild-card characters (<code>*</code> and <code>?</code>) if this isn&#8217;t already done by the shell, but apart from that, it will not reorder the arguments. Thus, it will show the documents in the order specified at the command line. </p>
<h2>LAYOUT OPTIONS</h2>
<p> The OSD layout option (<code>-L</code>/:<code>&#8211;layout</code>) accepts a string with comma-separated <i>key</i>=<i>value</i> pairs. The following keywords are recognized: </p>
<p> <code>alpha</code></p>
<dl>
<dt>
<dd> The opacity of the OSD text, either as a floating-point value between 0 and 1 or a percentage between 2 and 100.</dl>
<p> <code>margin</code></p>
<dl>
<dt>
<dd> The distance (in pixels) of the OSD text to the screen borders.</dl>
<p> <code>time</code></p>
<dl>
<dt>
<dd> The position of the timer.</dl>
<p> <code>title</code></p>
<dl>
<dt>
<dd> The position of the page title in overview mode.</dl>
<p> <code>page</code></p>
<dl>
<dt>
<dd> The position of the page number in overview mode.</dl>
<p> <code>status</code></p>
<dl>
<dt>
<dd> The position of the status line.</dl>
<p> The position specifications are composed by one character that indicates whether the text shall be displayed at the top (<code>T</code>) or bottom (<code>B</code>) edge of the screen and one character that indicates whether it shall appear on the left (<code>L</code>), on the right (<code>R</code>) or centered (<code>C</code>). </p>
<p> For example, the default OSD layout equals the following option string:<br />
 <code> -L margin=16,alpha=1,time=TR,title=BL,page=BR,status=TL</code> </p>
<h2>USAGE</h2>
<p> On startup, Impressive will display a black screen with the program logo at the center. If caching is enabled, but background rendering is disabled, all pages of the presentation will then be rendered once. A bar in the lower half of the screen displays the progress of this operation. Any key (except for Q and Esc) or mouse click skips this process, with the effect that Impressive will render the remaining pages on demand. Please note that the overview page will not be complete until every page has been rendered at least once. In other words, if the precaching process was skipped, placeholders will be displayed for all pages that have not been rendered yet. By default, Impressive will build up the cache in the background while the presentation runs. Thus, the progress bar will not appear and the preparation will only take the amount of time required to render the first two pages of the presentation. </p>
<p> After this initialization process, Impressive will switch to the first page directly and without any transition.</p>
<h2>CONTROLS</h2>
<p> <code>Q</code> key or <code>Esc</code> key</p>
<dl>
<dt>
<dd> Quit Impressive immediately.</dl>
<p> <code>LMB</code> (left mouse button), <code>Page Down</code> key, <code>Cursor Down</code> key, <code>Cursor Right</code> key or <code>Spacebar</code></p>
<dl>
<dt>
<dd> Go to the next page (using a transition).</dl>
<p> <code>RMB</code> (right mouse button), <code>Page Up</code> key, <code>Cursor Up</code> key, <code>Cursor Left</code> key or <code>Backspace</code> key</p>
<dl>
<dt>
<dd> Go to the previous page (using a transition).</dl>
<p> <code>Home</code> key /: <code>End</code> key</p>
<dl>
<dt>
<dd> Go directly to the first or last page of the presentation.</dl>
<p> <code>L</code> key</p>
<dl>
<dt>
<dd> Return to the last (most recently displayed) page. This can be used to toggle back and forth between two pages.</dl>
<p> <code>F</code> key</p>
<dl>
<dt>
<dd> Toggle fullscreen mode.</dl>
<p> <code>Tab</code> key or <code>MMB</code> (middle mouse button)</p>
<dl>
<dt>
<dd> Zoom back to the overview page. While in overview mode, a page can be selected with the mouse and activated with the left mouse button. The right or middle mouse button or the Tab key leave overview mode <i>without</i> changing the current page.</dl>
<p> <code>LMB</code> over a PDF hyperlink</p>
<dl>
<dt>
<dd> Jump to the page referenced by the hyperlink. Two types of hyperlinks are supported: Links that point to some other page of the same document, and URL hyperlinks like Web links and e-mail addresses. This feature is only available if <code>pdftk</code> is installed. Furthermore, <code>xdg-open</code> from the freedesktop.org Portland project is required for URL links to work. Please note that the hyperlink feature will not work properly when pages are rotated.</dl>
<p> click&amp;drag with <code>LMB</code> (left mouse button)</p>
<dl>
<dt>
<dd> Create a new highlight box. While at least one highlight box is defined on the current page, the page itself will be shown in a darker and blurry rendition. Only the highlight boxes will be displayed in their original lightness and sharpness.<br />
 If a page with highlight boxes is left, the boxes will be saved and restored the next time this page is shown again.</dl>
<p> <code>RMB</code> (right mouse button) over a highlight box</p>
<dl>
<dt>
<dd> If the right mouse button is clicked while the mouse cursor is above a highlight box, the box will be removed. If the last box on a page is removed, the page will turn bright and sharp again.</dl>
<p> <code>S</code> key</p>
<dl>
<dt>
<dd> Save the info script associated with the current presentation. The main purpose for this is to permanently save highlight boxes or keyboard shortcuts, so they will be restored the next time this presentation is started.</dl>
<p> <code>T</code> key</p>
<dl>
<dt>
<dd> Activate or deactivate the time display at the upper-right corner of the screen. If the timer is activated while the very first page of the presentation is shown, it activates &quot;time tracking&quot; mode. In this mode, a report of all pages visited with their display duration, enter and leave times will be written to standard output. This can be very useful when preparing presentations.</dl>
<p> <code>R</code> key</p>
<dl>
<dt>
<dd> Reset the presentation timer.</dl>
<p> <code>Return</code> key or <code>Enter</code> key</p>
<dl>
<dt>
<dd> Toggle spotlight mode. In this mode, the page is darkened in the same way as if highlight boxes are present, but instead of (or in addition to) the boxes, a circular &quot;spotlight&quot; will be shown around the mouse cursor position, following every motion of the mouse cursor.</dl>
<p> <code>+</code> key /: <code>&#8211;</code> key or mouse wheel</p>
<dl>
<dt>
<dd> Adjust the spotlight radius.</dl>
<p> <code>Z</code> key</p>
<dl>
<dt>
<dd> Toggle zoom mode. When this key is first pressed, the current page will zoom in. The page will be displayed at double size, but in its original resolution (i.e. it will be blurry). Impressive will re-render the page at the new resolution if the graphics hardware supports it. During this time, Impressive will <code>not</code> accept any input, so don&#8217;t even think about clicking the mouse or pressing keys before the image gets crisp again.<br />
 In zoom mode, all other functions will work as normal. Any operations that leave the current page, such as flipping the page or entering the overview screen, will leave zoom mode, too.</dl>
<p> <code>[</code> /: <code>]</code> key</p>
<dl>
<dt>
<dd> Adjust the gamma value of the display (might not be supported on every hardware).</dl>
<p> <code>{</code> /: <code>}</code> key</p>
<dl>
<dt>
<dd> Adjust the black level of the display (might not be supported on every hardware).</dl>
<p> <code>\</code> key</p>
<dl>
<dt>
<dd> Revert gamma and black level back to normal.</dl>
<p> <code>O</code> key</p>
<dl>
<dt>
<dd> This will toggle the &quot;visible on overview page&quot; flag of the current page. The result will not be visible immediately, but it can be saved to the info script (using the <code>S</code> key) and will be in effect the next time the presentation is started.</dl>
<p> <code>I</code> key</p>
<dl>
<dt>
<dd> This will toggle the skip flag of the current page. A page marked as skipped will not be reachable with the normal forward/:backward navigation keys.</dl>
<p> <code>B</code> key /: <code>W</code> key</p>
<dl>
<dt>
<dd> Fade to black or white, respectively. This feature can be used if a whiteboard or blackboard in front of the projection area is to be used during the presentation. Using these two keys, the screen will fade into a solid color. On any keypress or mouse click, it will fade back to normal. These keys are not available in overview mode.</dl>
<p> click&amp;drag with <code>RMB</code> (right mouse button) in zoom mode</p>
<dl>
<dt>
<dd> Move the visible part of the page in zoom mode.</dl>
<p> <code>Cursor</code> keys in overview mode</p>
<dl>
<dt>
<dd> Navigate through pages.</dl>
<p> <code>Alt</code>+<code>Tab</code> keys</p>
<dl>
<dt>
<dd> Leaves fullscreen mode to facilitate task switching while running full-screen presentations.</dl>
<p> Any other alphanumeric (A-z, 0-9) or function key (F1-F12) can be used to assign shortcuts to pages that require quick access. If one of the keys is pressed together with <code>Shift</code>, the currently displayed page is associated with this key. To recall the page later, it is sufficient to press the shortcut key again. Shortcuts can be permanently stored with the <code>S</code> key. </p>
<h2>INFO SCRIPTS</h2>
<p> Impressive offers a powerful way to customize individual presentations using so-called info scripts. An info script is a text file having the same name and located in the same directory as the presentation file itself, except for the additional suffix <code>.info</code>. Thus, a presentation file called <code>BrandNewProduct.pdf</code> would have a info script with the name <code>BrandNewProduct.pdf.info</code>. If multiple arguments were specified on the command line, the info script will be called just <code>.info</code> (a dot file, so to speak). If a directory name was specified as the only argument, either a file called <i>DirectoryName</i>.info or a file called <code>.info</code> <i>inside</i> the directory will be used, depending on whether a path separator was specified at the end of the directory name or not &#8211; Impressive simply appends <code>.info</code> to whatever the input path name was.<br />
 In any case, the default file name can be overridden by the <code>-I</code> command line option. </p>
<p> Info scripts are actually Python scripts with full access to Impressive&#8217;s global data structures and functions. (It is possible to write real interactive applications using info scripts.) Thus, they can modify a broad range of settings concerning Impressive. This manual will only cover the most basic ones. </p>
<h2> PAGE PROPERTIES</h2>
<p> The main part of an info script defines the properties of each page. At the moment, the following properties are defined: </p>
<p> <code>title</code></p>
<dl>
<dt>
<dd> Each page can have a title that is displayed in the Impressive window&#8217;s title bar. If there is no title explicitly specified in the info script, the title of the page will be extracted from PDF metadata if pdftk is installed, or the image file name will be used if the presentation is an image slideshow.</dl>
<p> <code>transition</code></p>
<dl>
<dt>
<dd> With this property, the transition class to be used for rendering the transition between this page and the following page can be specified. For pages lacking this property, random transitions will be chosen. A list of available transition classes can be obtained with <code>impressive -l</code>.</dl>
<p> <code>transtime</code></p>
<dl>
<dt>
<dd> This property overrides the global transition time parameter (<code>-T</code> at the command line). It contains the integer time (in milliseconds) the transition between this page and the following page shall be shown.</dl>
<p> <code>overview</code></p>
<dl>
<dt>
<dd> This property holds a boolean value (0/:<code>False</code> or 1/:<code>True</code>) that specifies whether the page shall be included in the overview page. If this property isn&#8217;t specified, it is assumed to be <code>True</code>.</dl>
<p> <code>skip</code></p>
<dl>
<dt>
<dd> This boolean property can be set to 1/:<code>True</code> if the page shall be skipped during the presentation.<br />
 Pages with <code>overview:True, skip:False</code> will be accessible both by cycling through the pages and using the overview page,<br />
 pages with <code>overview:True, skip:True</code> will be silently skipped in the normal page cycle, but remain accessible from the overview page,<br />
 pages with <code>overview:False, skip:False</code> will appear in the normal cycle, but not on the overview page<br />
 and pages with <code>overview:False, skip:True</code> will not be accessible at all.</dl>
<p> <code>boxes</code></p>
<dl>
<dt>
<dd> This property stores a list of highlight box coordinates. Normally, there is no need to edit this by hand, as Impressive handles this automatically if the <code>S</code> key is pressed.</dl>
<p> <code>timeout</code></p>
<dl>
<dt>
<dd> If a <code>timeout</code> property is present and the page is shown for the first time, Impressive will automatically switch to the next page after the specified number of milliseconds.</dl>
<p> <code>comment</code></p>
<dl>
<dt>
<dd> This property can hold a string with a single line of text that will be displayed on screen while the page is shown. Display of this text can not be disabled.</dl>
<p> <code>sound</code></p>
<dl>
<dt>
<dd> Specifies the file name of a sound file to be played (via MPlayer) when the page is first entered. Once started, the sound will be played until its end is reached, another sound or video is played, or Impressive is exited.</dl>
<p> <code>video</code></p>
<dl>
<dt>
<dd> Specifies the file name of a video file to be played when the page is entered. The video will be displayed full-screen. Any key or mouse click stops playback. Note that this function is highly experimental and might not work reliably on every system!</dl>
<p> <code>progress</code></p>
<dl>
<dt>
<dd> If this property is set to zero, the presentation progress bar (which is usually set up with the <code>-d</code>/:<code>&#8211;duration</code> command line switch) will not be shown on this page. In practice, it might be useful to hide the bar from the first page so that it is not visible during the introduction.</dl>
<p> <code>reset</code></p>
<dl>
<dt>
<dd> If this property is set to 1 or <code>True</code>, the timer will be reset each time this page is left, just as if the <code>R</code> has been pressed. If the special value 2 or <code>FirstTimeOnly</code> is used, the reset will only take place if the page was shown for the first time. Again, this is particularly useful on the first page: A combination of <code>progress:False, reset:FirstTimeOnly</code> makes it possible to set up the presentation long before it actually begins &#8211; the first page can be showed as long as desired, actual timing starts at the second page.</dl>
<p> <code>rotate</code></p>
<dl>
<dt>
<dd> This property is a per-page override of the global <code>-r</code> command line option: It specifies how the page shall be rotated, in 90-degree steps clockwise.</dl>
<p> <code>OnEnter</code>, <code>OnLeave</code>, <code>OnEnterOnce</code>, <code>OnLeaveOnce</code></p>
<dl>
<dt>
<dd> These properties can contain a Python callable (i.e. a function reference or lambda expression) that is executed when the page is entered or left. The <code>~Once</code> variants will only be executed when the page is entered or left for the first time. The callable must not take any arguments. This feature can be used to associate arbitrary Python code with specific pages, for example to execute external programs.<br />
 <code>Warning:</code> Lambda expressions cannot be properly processed by the Info Script save function (<code>S</code> key). If Impressive encounters lambda expressions when saving, it will remove them. In addition, it will not overwrite the original info script, but generate an extra file that needs to be merged withe the original script by hand.</dl>
<p> <code>keys</code></p>
<dl>
<dt>
<dd> This property can be assigned a dictionary that maps alphanumerical keys to Python functions. For example, <code>&#8216;keys&#8217;: { &#8216;x&#8217;: SomeFunction }</code> will invoke <code>SomeFunction()</code> if the lowercase character &#8216;x&#8217; is typed while the page is displayed. Regarding the functions, the same restrictions as for the <code>OnEnter</code>/:<code>OnLeave</code> family apply: the function must not take any parameters and lambda functions can not be saved. Also note that it is not possible to overwrite Impressive&#8217;s pre-defined key bindings with this method.</dl>
<p> The properties are stored together in a Python dictionary called <code>PageProps</code>. The syntax looks like in this example: </p>
<pre><code>
PageProps = {
    1 : {
        'title' : "Title Page",
        'transition' : PagePeel,
        'sound' : "background_music.mp3"
    },
    2 : {
        'title' : "Another Page",
        'timeout' : 5000
    }
}
</code></pre>
<p> The PageProps definition (and <code>only</code> the PageProps definition) will be rewritten by Impressive if the <code>S</code> key is pressed. User-defined PageProps entries will also be left untouched, except for some pretty-printing. </p>
<h2> GLOBAL PRESENTATION PROPERTIES</h2>
<p> The name of the presentation is shown in the title bar of the Impressive window (if not in fullscreen mode). By default, the file name or (if available) PDF metadata title will be used for this purpose, but the presentation title can also be explicitly set by overwriting the <code>DocumentTitle</code> variable:<br />
 <code> DocumentTitle = &quot;My Presentation&quot;</code> </p>
<p> Another useful variable, <code>AvailableTransitions</code>, contains a list of all transition classes that may be used for randomly assigning transitions to pages lacking the <code>transition</code> property. Thus, if you want to exclude a certain transition (either because you don&#8217;t like it or because you want to have it exclusively on pages where you manually assigned it using <code>PageProps</code>), you can write something like<br />
 <code> AvailableTransitions.remove(WipeBlobs)</code><br />
 On the other side, it&#8217;s possible to activate transitions that are not enabled by default:<br />
 <code> AvailableTransitions += [SlideUp, SlideDown]</code><br />
 Alternatively, you can completely overwrite <code>AvailableTransitions</code> to have the same transition (or set of transitions) assigned to all pages:<br />
 <code> AvailableTransitions = [Crossfade]</code> </p>
<h2> OPTION OVERRIDES</h2>
<p> Another use of info scripts is overriding the default or command-line settings on a per-file basis. This can be done by simply overwriting one of the variables that are defined at the beginning of <code>impressive.py</code>. Each of these variables corresponds either to a command-line setting, or to some constant related to visual appearance or performance. So, for example, to force fullscreen mode for a presentation, write<br />
 <code> Fullscreen = True</code> </p>
<h2>AUTHOR</h2>
<p> Impressive and its documentation has been written mainly by Martin J. Fiedler &lt;martin.fiedler [at] gmx.net&gt;, with small portions of the code written by external contributors. See the source code file for details.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to to &lt;martin.fiedler [at] gmx.net&gt;. </p>
<h2>Index</h2>
