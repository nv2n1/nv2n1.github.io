---

title: "feh(1)"
name: "feh"
section: "1"
letter: "f"
url: "/docs/linux/man/1-feh/"
---

<p> feh - image viewer and cataloguer  </p>
<p> feh [options] file(s)  </p>
<p> <code>feh</code> is an image viewer using the <code>imlib2</code> library to open and manipulate images. <code>feh</code> has a large number of operational modes. The default mode is an image slideshow, showing one image at a time from those specified on the commandline. Keys and mouse control may be used to move through them. Other modes can be specified on the commandline, and are described below. </p>
<p> <code>feh</code> can also recurse through a directory structure to form a filelist for processing, and will convert directory names on the commandline into a list of their contents automatically. </p>
<p> <code>Filelists</code> can be sorted in a number of ways. The default is the order the files were specified on the commandline, or the order they were read from the disk. You can specify sorting modes such as <code>randomize</code> or you can sort by filename, image name, width, height, pixels, etc. Filelists can also be saved to or loaded from files.  </p>
<h2>MODES</h2>
<p> <code>Montage mode</code> forms a montage from the filelist. The resultant image can be viewed or saved, and it&#8217;s size can be limited by height, width or both. </p>
<p> <code>Collage mode</code> is very similar to montage mode, except the images are distributed randomly and may overlap eachother </p>
<p> <code>Index mode</code> forms an index print from the filelist. Image thumbnails are shown along with the filename, filesize and pixel size, printed using a truetype font of your choice. The resultant image can be viewed or saved, and it&#8217;s size can be limited by height, width or both. </p>
<p> <code>Thumbnail mode</code> is like index mode, but the mini-images are clickable, and launch the clicked image in a browser window. </p>
<p> <code>Multiwindow mode</code> shows images in multiple windows, instead of as a slideshow in one window. Don&#8217;t use with a large filelist ;) </p>
<p> <code>Fullscreen mode</code> shows image in fullscreen view, can be combined with a slide-change delay to show an automated presentation. </p>
<p> <code>List mode</code> doesn&#8217;t display images. Outputs an &#8216;ls&#8217;-style listing of the files in the filelist, including image info such as size, pixels, type, etc. Customlist mode will display whatever image info you want, in the format you choose. </p>
<p> <code>feh</code> can also list either all the loadable files in a filelist or all the unloadable files. Useful for preening a directory. </p>
<p> <code>feh</code> also has the ability to load files over http or ftp, simply specify the url on the commandline. </p>
<p> <code>feh</code> can read options from the commandline, or from a config file. The syntax is the same in each case. See <code>CONFIG FILE SYNTAX</code> for details about using themes defined in a config file. These methods may be used in conjunction.  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, --help</code></dt>
<dd> <p> display help output and exit </p>
 </dd>
<dt><code>-v, --version</code></dt>
<dd> <p> output version information and exit </p>
 </dd>
<dt><code>-V, --verbose</code></dt>
<dd> <p> output useful information, progress bars, etc </p>
 </dd>
<dt><code>-q, --quiet</code></dt>
<dd> <p> Don&#8217;t report non-fatal errors for failed loads. Verbose and quiet modes are not mutually exclusive, the first controls informational messages, the second only errors. </p>
 </dd>
<dt><code>-T, --theme THEME</code></dt>
<dd> <p> Load options from config file with name THEME - see CONFIG FILE SYNTAX for more info. </p>
 </dd>
<dt><code>--rcfile FILE</code></dt>
<dd> <p> Use FILE to parse themes and options from, instead of the default ~/.fehrc, /etc/fehrc files. </p>
 </dd>
<dt><code>-r, --recursive</code></dt>
<dd> <p> Recursively expand any directories in FILE to the content of those directories, all the way down to the bottom level. (Take it easy) </p>
 </dd>
<dt><code>-z, --randomize</code></dt>
<dd> <p> When viewing multiple files in a slideshow, randomise the file list before displaying. </p>
 </dd>
<dt><code>-f, --filelist FILE</code></dt>
<dd> <p> This option is similar to the playlists used by music software. If FILE exists, it will be read for a list of files to load, in the order they appear. The format is a list of image filenames, absolute or relative to the current directory, one filename per line. <br />
 If FILE doesn&#8217;t exist, it will be created from the internal filelist at the end of a viewing session. This is best used to store the results of complex sorts (-Spixels for example) for later viewing. Any changes to the internal filelist (such as deleting a file or it being pruned for being unloadable) will be saved to FILE when feh exits. You can add files to filelists by specifying them on the commandline when also specifying the list. </p>
 </dd>
<dt><code>-p, --preload</code></dt>
<dd> <p> Preload images. This doesn&#8217;t mean hold them in RAM, it means run through them and eliminate unloadable images first. Otherwise they will be removed as you flick through. This also analyses the images to get data for use in sorting, such as pixel size, type etc. A preload run will be automatically performed if you specify one of these sort modes. </p>
 </dd>
<dt><code>-F, --full-screen</code></dt>
<dd> <p> Make the window fullscreen </p>
 </dd>
<dt><code>-g, --geometry STRING</code></dt>
<dd> <p> Limit (and don&#8217;t change) the window size. Takes an X-style geometry string like 640x480. Note that larger images will be zoomed out to fit but you can see them at 1:1 by clicking the zoom button. </p>
 </dd>
<dt><code>-Z, --auto-zoom</code></dt>
<dd> <p> Zoom picture to screen size in fullscreen (affected by --stretch and --ignore-aspect). </p>
 </dd>
<dt><code>--zoom PERCENT</code></dt>
<dd> <p> Zooms images by a PERCENT, when in full screen mode or when window geometry is fixed. If combined with --auto-zoom, zooming will be limited to the the size. </p>
 </dd>
<dt><code>-w, --multiwindow</code></dt>
<dd> <p> Disable slideshow mode. With this setting, instead of opening multiple files in slideshow mode, multiple windows will be opened, one per file. </p>
 </dd>
<dt><code>-x, --borderless</code></dt>
<dd> <p> Create borderless windows </p>
 </dd>
<dt><code>-d, --draw-filename</code></dt>
<dd> <p> Draw the filename at the top-left of the image </p>
 </dd>
<dt><code>-D, --slideshow-delay NUM</code></dt>
<dd> <p> For slideshow mode, specifies time delay (seconds, can be a decimal) between automatically changing slides. Great for presentations. </p>
 </dd>
<dt><code>-R, --reload NUM</code></dt>
<dd> <p> Use this option to tell <code>feh</code> to reload an image after NUM seconds. Useful for viewing webcams via http, or even on your local machine. </p>
 </dd>
<dt><code>-k, --keep-http</code></dt>
<dd> <p> When viewing files using HTTP, feh normally deletes the local copies after viewing, or, if caching, on exit. This option prevents this so that you get to keep the local copies. They will be in /tmp with &quot;feh&quot; in the name. </p>
 </dd>
<dt><code>-Q, --builtin</code></dt>
<dd> <p> Use builtin http client to grab remote files instead of wget, useful if you don&#8217;t have wget installed. </p>
 </dd>
<dt><code>--caption-path PATH</code></dt>
<dd> <p> Path to directory containing image captions. This turns on caption viewing, and if captions are found in PATH, which is relative to the directory of each image, they are overlayed on the displayed image. e.g with caption path &quot;captions&quot;, and viewing image images/foo.jpg, caption will be looked for as &quot;images/captions/foo.jpg.txt&quot; </p>
 </dd>
<dt><code>-l, --list</code></dt>
<dd> <p> Don&#8217;t display images. Analyse them and display an &#8216;ls&#8217;-style listing. Useful in scripts hunt out images of a certain size/resolution/type etc. </p>
 </dd>
<dt><code>-L, --customlist FORMAT</code></dt>
<dd> <p> Use FORMAT as the format specifier for list output. FORMAT is a printf-like string containing image info specifiers. See FORMAT SPECIFIERS. </p>
 </dd>
<dt><code>-U, --loadable</code></dt>
<dd> <p> Don&#8217;t display images. Just print out their names if imlib2 can successfully load them. </p>
 </dd>
<dt><code>-u, --unloadable</code></dt>
<dd> <p> Don&#8217;t display images. Just print out their name if imlib2 can NOT successfully load them. </p>
 </dd>
<dt><code>-S, --sort SORT_TYPE</code></dt>
<dd> <p> The file list may be sorted according to image parameters. Allowed sort types are: name, filename, width, height, pixels, size, format. For sort modes other than name or filename, a preload run will be necessary, causing a delay proportional to the number of images in the list </p>
 </dd>
<dt><code>-n, --reverse</code></dt>
<dd> <p> Reverse the sort order. Use this to invert the order of the filelist. Eg to sort in reverse width order, use <code>-nSwidth</code> </p>
 </dd>
<dt><code>-A, --action ACTION</code></dt>
<dd> <p> Specify a string as an action to perform on the image. In slideshow or multiwindow modes, the action will be run when the enter key is pressed, in list mode, the action will be run for each file listed. The action will be executed by /bin/sh. Use format specifiers to refer to image info. See FORMAT SPECIFIERS for examples <br />
 Eg. feh -A &quot;mv %f ~/images/%n&quot; * <br />
 In slideshow mode, the next image will be shown after running the action, in multiwindow mode, the window will be closed. </p>
 </dd>
<dt><code>--action1...9</code></dt>
<dd> <p> Extra actions which can be set and triggered using the appropriate number key. </p>
 </dd>
<dt><code>-m, --montage</code></dt>
<dd> <p> Enable montage mode. Montage mode creates a new image consisting of a grid of thumbnails of the images in the filelist. When montage mode is selected, certain other options become available. See MONTAGE MODE OPTIONS </p>
 </dd>
<dt><code>-c, --collage</code></dt>
<dd> <p> Enable collage mode. Collage mode is very similar to montage mode, except the images are distributed randomly. </p>
 </dd>
<dt><code>-i, --index</code></dt>
<dd> <p> Enable Index mode. Index mode is similar to montage mode, and accepts the same options. It creates an index print of thumbails, printing the image name beneath each thumbnail. Index mode enables certain other options, see INDEX MODE OPTIONS </p>
 </dd>
<dt><code>-I, --fullindex</code></dt>
<dd> <p> Same as Index mode, but you also get image size and dimensions printed below each thumbnail. </p>
 </dd>
<dt><code>-t, --thumbnails</code></dt>
<dd> <p> Same as Index mode, but the thumbnails are clickable image launchers. </p>
 </dd>
<dt><code>--bg-tile FILE</code></dt>
<dd>  </dd>
<dt><code>--bg-center FILE</code></dt>
<dd>  </dd>
<dt><code>--bg-scale FILE</code></dt>
<dd>  </dd>
<dt><code>--bg-seamless FILE</code></dt>
<dd> <p> Set your desktop background to FILE. Feh can use enlightenment IPC if you are running it, or will fall back to X methods. Feh stores the commandline necessary to restore the background you chose in ~/.fehbg. So to have feh-set backgrounds restored when you restart X, add the line &quot;`cat $HOME/.fehbg`&quot; to your X startup script (e.g. ~/.xsession). Note that you only need to do this for non E window managers. </p>
 </dd>
<dt><code>-M, --menu-font FONT</code></dt>
<dd> <p> Use FONT for the font in menus. </p>
 </dd>
<dt><code>--menu-style FILE</code></dt>
<dd> <p> Use FILE as the style descriptor for menu text. </p>
 </dd>
<dt><code>--menu-bg BG</code></dt>
<dd> <p> Use BG for the background image in menus. </p>
 </dd>
<dt><code>--menu-border INT</code></dt>
<dd> <p> Specify number of pixels that define the menu background&#8217;s border. Borders are not stretched when images are scaled. </p>
 </dd>
<dt><code>-N, --no-menus</code></dt>
<dd> <p> Don&#8217;t load or show any menus. </p>
 </dd>
<dt><code>-1, --next-button B</code></dt>
<dd> <p> Use button B to advance to the next image in slideshow mode (defaults to 1, usually the left button). </p>
 </dd>
<dt><code>-2, --zoom-button B</code></dt>
<dd> <p> Use button B to zoom the current image in any mode (defaults to 2, usually the middle button). </p>
 </dd>
<dt><code>-3, --pan-button B</code></dt>
<dd> <p> Use button B to pan the current image in any mode (defaults to 3, usually the right button). </p>
 </dd>
<dt><code>--no-pan-ctrl-mask</code></dt>
<dd> <p> Don&#8217;t require CTRL+Button for panning in any mode -- just use the button (default=off). </p>
 </dd>
<dt><code>-4, --menu-button B</code></dt>
<dd> <p> Use CTRL+Button B to activate the menu in any mode. Set to 0 to use any button. This option is disabled if the -N or --no-menus option is set (defaults to 3, usually the right button). </p>
 </dd>
<dt><code>-5, --no-menu-ctrl-mask</code></dt>
<dd> <p> Don&#8217;t require CTRL+Button for menu activation in any mode -- just use the button (default=off). </p>
 </dd>
<dt><code>-6, --rotate-button B</code></dt>
<dd> <p> Use CTRL+Button B to rotate the current image in any mode (default=2). </p>
 </dd>
<dt><code>-7, --no-rotate-ctrl-mask</code></dt>
<dd> <p> Don&#8217;t require CTRL+Button for rotation in any mode -- just use the button (default=off). </p>
 </dd>
<dt><code>-8, --blur-button B</code></dt>
<dd> <p> Use CTRL+Button B to blur the current image in any mode (default=1). </p>
 </dd>
<dt><code>-9, --no-blur-ctrl-mask</code></dt>
<dd> <p> Don&#8217;t require CTRL+Button for blurring in any mode -- just use the button (default=off). </p>
 </dd>
<dt><code>--xinerama</code></dt>
<dd> <p> Enable/disable Xinerama support. Has no effect unless you have an Xinerama compiled in. </p>
 </dd>
<dt><code>--screen-clip</code></dt>
<dd> <p> Enable/disable window clipping based on screen size. WARNING: With this disabled, windows could become very large, making them unmanageable in certain window managers. </p>
 </dd>
<dt><code>--hide-pointer</code></dt>
<dd> <p> Hide the mouse pointer in full screen mode (useful for slideshows etc). </p>
 </dd></dl>
<h2>FORMAT SPECIFIERS</h2>
<p> <code>%f</code> image path/filename <br />
 <code>%n</code> image name <br />
 <code>%s</code> image size (bytes) <br />
 <code>%p</code> image pixel size <br />
 <code>%w</code> image width <br />
 <code>%h</code> image height <br />
 <code>%t</code> image format <br />
 <code>%P</code> prints feh <br />
 <code>%v</code> prints the version <br />
 <code>%m</code> prints the mode (slideshow, multiwindow...) <br />
 <code>%l</code> prints the total number of files in the filelist <br />
 <code>%u</code> prints the current file number <br />
 </p>
<pre><code>\n newline
</code></pre>
<p> <br />
 Eg. feh -A &quot;mv %f ~/images/%n&quot; *  </p>
<h2>MONTAGE MODE OPTIONS</h2>
<dl>
<dt><code>-X, --ignore-aspect</code></dt>
<dd> <p> By default, the montage thumbnails will retain their aspect ratios, while fitting in --thumb-width and --thumb-height. This option will force them to be the size set by --thumb-width and --thumb-height This will prevent any whitespace in the final montage </p>
 </dd>
<dt><code>-s, --stretch</code></dt>
<dd> <p> Normally, if an image is smaller than the specified thumbnail size, it will not be enlarged. If this option is set, the image will be scaled up to fit the thumnail size. (Aspect ratio will be maintained unless --ignore-aspect is specified) </p>
 </dd>
<dt><code>-y, --thumb-width NUM</code></dt>
<dd> <p> Set thumbnail width in pixels </p>
 </dd>
<dt><code>-E, --thumb-height NUM</code></dt>
<dd> <p> Set thumbnail height in pixels Thumbnails default to 20x20 pixels </p>
 </dd>
<dt><code>-W, --limit-width NUM</code></dt>
<dd> <p> Limit the width of the montage in pixels </p>
 </dd>
<dt><code>-H, --limit-height NUM</code></dt>
<dd> <p> Limit the height of the montage in pixels These options can be used together (to define the image size exactly), or separately. If only one is specified, theother is calculated from the number of files specified and the size of the thumbnails. The default is to limit width to 800 pixels and calculate the height as necessary </p>
 </dd>
<dt><code>-b, --bg FILE|trans</code></dt>
<dd> <p> Use FILE as a background for your montage. With this option specified, the size of the montage will default to the size of FILE if no size restrictions are specified. Alternatively, if FILE is &#8216;trans&#8217;, the background will be made transparent. </p>
 </dd>
<dt><code>-a, --alpha NUM</code></dt>
<dd> <p> When drawing thumbnails onto the background, apply them with a transparency level of NUM (0-255). </p>
 </dd>
<dt><code>-o FILE</code></dt>
<dd> <p> Save the created montage to FILE </p>
 </dd>
<dt><code>-O FILE</code></dt>
<dd> <p> Just save the created montage to FILE without displaying it (use in scripts) </p>
 </dd></dl>
<h2>INDEX MODE OPTIONS</h2>
<dl>
<dt><code>-e, --font FONT</code></dt>
<dd> <p> Use FONT to print the information under each thumbnail. FONT should be a truetype font, resident in the current directory, or in feh&#8217;s font directory, and should be defined in the form fontname/size(points). (No extension). eg. --font myfont/12 </p>
 </dd>
<dt><code>--fontpath PATH</code></dt>
<dd> <p> Specify PATH as an extra directory in which to search for fonts, can use multiple times to add multiple paths, e.g --fontpath /path/a --fontpath /path/b. </p>
 </dd>
<dt><code>--title-font FONT</code></dt>
<dd> <p> Use FONT to print a title on the index, if no font is specified, a title will not be printed </p>
 </dd></dl>
<h2>CONFIG FILE SYNTAX</h2>
<p> The feh config file allows the naming of option groups, or themes. If <code>$HOME/.fehrc</code> exists, or if not, but <code>/etc/fehrc</code> exists, feh will look in it for theme name/options pairs. If neither $HOME/.fehrc or /etc/fehrc exist, feh will create a default one in ~/.fehrc. An example entry would be: <br />
 <code>imagemap -rVq --thumb-width 40 --thumb-height 30</code> <br />
 You can then use this theme in two ways. Either <br />
 <code>feh --theme imagemap *.jpg</code> <br />
 or you can create a symbolic link to feh with the name of the options you want it to use. So from the example above: <br />
 <code>ln -s `which feh` ~/bin/imagemap</code> <br />
 Now I just run <code>imagemap *.jpg</code> to use those options. A cooler example is <br />
 <code>mkindex -iVO index.jpg --title-font 20thcent/24 .</code> <br />
 Notice the &#8216;.&#8216; at the end. Now with a symlink I can create a mkindex command which will create an index.jpg in the current directory. I just run <code>mkindex</code> to do it. <br />
 You can combine these themes with commandline options, they will be combined. So in the example above, typing <code>mkindex -q</code> will create and index, suppressing error messages. An example.fehrc is provided with a couple of cool examples.  </p>
<h2>SLIDESHOW KEYS</h2>
<p> The default mode for viewing mulitple images is Slideshow mode When viewing a slideshow, the following keys may be used: </p>
<dl>
<dt><code>p, P, &lt;BACKSPACE&gt;, &lt;LEFT&gt;</code></dt>
<dd> <p> Goto previous slide </p>
 </dd>
<dt><code>n, N, &lt;SPACE&gt;, &lt;RIGHT&gt;</code></dt>
<dd> <p> Goto next slide </p>
 </dd>
<dt><code>r, R</code></dt>
<dd> <p> Reload current image. Useful for webcams. </p>
 </dd>
<dt><code>v, V</code></dt>
<dd> <p> Toggle fullscreen. </p>
 </dd>
<dt><code>m, M</code></dt>
<dd> <p> Show popup menu. </p>
 </dd>
<dt><code>c, C</code></dt>
<dd> <p> Caption entry mode. If --caption-path has been specified, then this enables caption editing. The caption will turn yellow and be editable, hit enter to confirm and save the caption, or hit escape to cancel and revert the caption. </p>
 </dd>
<dt><code>w, W</code></dt>
<dd> <p> Size window to current image size. </p>
 </dd>
<dt><code>h, H</code></dt>
<dd> <p> Pause the slideshow (only useful when using timed reloading or image changes) </p>
 </dd>
<dt><code>s, S</code></dt>
<dd> <p> Save the current image to a unique filename. </p>
 </dd>
<dt><code>f, F</code></dt>
<dd> <p> Save the current filelist to a unique filename. </p>
 </dd>
<dt><code>&lt;, &gt;</code></dt>
<dd> <p> In place editing, rotate the image 90 degrees left/right. </p>
 </dd>
<dt><code>&lt;HOME&gt;</code></dt>
<dd> <p> Goto first slide </p>
 </dd>
<dt><code>&lt;END&gt;</code></dt>
<dd> <p> Goto last slide </p>
 </dd>
<dt><code>&lt;PAGE UP&gt;</code></dt>
<dd> <p> Go forward around 5% of the way through the slideshow </p>
 </dd>
<dt><code>&lt;PAGE DOWN&gt;</code></dt>
<dd> <p> Go backward around 5% of the way through the slideshow </p>
 </dd>
<dt><code>&lt;ESCAPE&gt;</code></dt>
<dd> <p> Quit the slideshow </p>
 </dd>
<dt><code>+, =</code></dt>
<dd> <p> Increase reload delay </p>
 </dd>
<dt><code>-, _</code></dt>
<dd> <p> Decrease reload delay </p>
 </dd>
<dt><code>&lt;DELETE&gt;</code></dt>
<dd> <p> Remove the currently viewed file from the filelist </p>
 </dd>
<dt><code>&lt;CTRL+DELETE&gt;</code></dt>
<dd> <p> Delete the currently viewed file and remove it from the filelist </p>
 </dd>
<dt><code>x, X</code></dt>
<dd> <p> Close current window. </p>
 </dd>
<dt><code>q, Q</code></dt>
<dd> <p> Quit the slideshow <code>&lt;KEYPAD LEFT&gt;</code> Move the image to the left <code>&lt;KEYPAD RIGHT&gt;</code> Move the image to the right <code>&lt;KEYPAD +&gt;</code> Zoom in <code>&lt;KEYPAD -&gt;</code> Zoom out <code>&lt;KEYPAD *&gt;</code> Zoom to 100% <code>&lt;KEYPAD /&gt;</code> Zoom to fit the window </p>
 </dd></dl>
<h2>MOUSE ACTIONS</h2>
<p> When viewing an image, mouse button 1 moves to the next image (slideshow mode only), button 2 zooms (click and drag left-&gt;right to zoom in, right-&gt; left to zoom out, click once to restore 1x zoom), and mouse button 3 pans. Ctrl+button 1 blurs or sharpens the image (drag left to blur and right to sharpen). Ctrl+button 2 rotates the image around the center point. Ctrl+ button 3 activates the context-sensitive menu. Buttons can be redefined with the -1 through -9 (or --*-button) cmdline flags. All you people with million button mice can remove the ctrl mask with the --no-*-ctrl-mask options.  </p>
<h2>SUGGESTED USAGE EXAMPLES</h2>
<p> Here are some examples of nice option combinations to achieve cool results: </p>
<dl>
<dt><code>feh -r /opt/images</code></dt>
<dd> <p> Recursively scan /opt/images and show all the images in a slideshow. </p>
 </dd>
<dt><code>feh -rSname /opt/image</code></dt>
<dd> <p> Same again, but sort by name before showing. </p>
 </dd>
<dt><code>feh -m /opt/images/landscapes</code></dt>
<dd> <p> Create a montage from the images in /opt/images/landscapes </p>
 </dd>
<dt><code>feh -Xrm -W 400 --thumb-width 30 --thumb-height 20 ./landscapes</code></dt>
<dd> <p> Create a montage from the images in /opt/images/landscapes and all directories below it. Limit the width of the image to 400 and make the thumbnails 30x20, ignoring aspect ratio. </p>
 </dd>
<dt><code>feh -irFarial/14 -O index.jpg /opt/images</code></dt>
<dd> <p> Make an index print of /opt/images and all directories below it, using 14 point arial to write the image info under each thumbnail. Save the image as index.jpg and don&#8217;t display it, just exit. </p>
 </dd>
<dt><code>feh -LrSpixels /opt/images</code></dt>
<dd> <p> List the images in /opt/images and all directories within, sorted by pixel size, giving as much info as possible. </p>
 </dd>
<dt><code>feh -kR30 <a rel="nofollow" href="http://url.of.a.webcam.jpg">http://url.of.a.webcam.jpg</a></code></dt>
<dd> <p> Use feh to view a webcam, reloading every 30 seconds, and saving the images in /tmp. </p>
 </dd>
<dt><code>feh --unloadables -r /opt/images</code></dt>
<dd> <p> Weed out (list) all the unloadable images in /opt/images and below. </p>
 </dd>
<dt><code>feh -w /opt/images/holidays</code></dt>
<dd> <p> Open each image in /opt/images/holidays in it&#8217;s own window </p>
 </dd>
<dt><code>feh -FD5 -Sname /opt/images/presentation</code></dt>
<dd> <p> Show the images in /opt/images/presentation, sorted by name, in fullscreen view, automatically changing slides every 5 seconds. </p>
 </dd>
<dt><code>feh -rSwidth -A &#8216;mv %f ~/images/%n&#8217; /opt/images</code></dt>
<dd> <p> View all the images in /opt/images and below, sorted by width (smallest first) and move the image to ~/images/image_name when enter is pressed. </p>
 </dd></dl>
<h2>BUGS</h2>
<p> None known. However there are many, many options. It is possible that some do not work well in conjuncion with each other. Let me know :)  </p>
<h2>LICENSE</h2>
<p> Copyright Tom Gilbert (and various contributors), 1999, 2000 </p>
<p>Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &quot;Software&quot;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: </p>
<p>The above copyright notice and this permission notice shall be included in all copies of the Software and its documentation and acknowledgment shall be given in the documentation and software packages that this Software was used. </p>
<p>THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. </p>
<p>Email bugs and feature requests to <br />
 <code>&lt;feh_sucks [at] linuxbrit.co.uk&gt;</code> </p>
