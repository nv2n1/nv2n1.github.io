---
title: "squeak(1)"
name: "squeak"
section: "1"
letter: "s"
url: "/docs/linux/man/1-squeak/"
description: "squeak, inisqueak – Unix Squeak virtual machine and installer"
---

<h2>NAME</h2>
<p> squeak, inisqueak &#8211; Unix Squeak virtual machine and installer</p>
<h2>SYNOPSIS</h2>
<p> <code>inisqueak</code><br />
 <code>squeak</code> [ <i>option</i>&#8230; ] [ <i>image</i> ] [ <i>script</i> [ <i>argument</i>&#8230; ] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>squeak</code> is the virtual machine for the Squeak Smalltalk system. It requires three files to operate correctly: an <code>image</code> file containing a `snapshot&#8217; of a live Squeak session, a <code>changes</code> file containing the source code for modified methods in the image, and a copy of (or a link to) a shared system <code>sources</code> file containing the source code for methods that have not been modified since the last major version increment. </p>
<p> The image and changes files contain the state of a user&#8217;s Squeak session, which is persistent between consecutive sessions. Private copies of these files are therefore normally required. The <code>inisqueak</code> script checks that the local Squeak installation appears sane, and then copies the required files to the current working directory. If <code>inisqueak</code> encounters no problems, it will finish by running <code>squeak</code> to start a Squeak session using the newly copied image and changes files. </p>
<p> <code>inisqueak</code> should be run <i>once</i>, when using Squeak for the first time, to create a new &#8216;personal&#8217; Squeak session. Afterwards, <code>squeak</code> should be run each time that session is to be resumed. </p>
<h2>INVOCATION</h2>
<p> <code>inisqueak</code> has no options or arguments. Simply &#8216;cd&#8217; to the directory that is to contain the working copies of the image and changes files, then run it. </p>
<p> <code>squeak</code> accepts various <i>options</i> (described below), and then an optional <i>image</i> name (which must not begin with a minus sign &#8216;-&#8216;). If an <i>image</i> name is given on the command line then <code>squeak</code> tries to run that image. Otherwise <code>squeak</code> checks the environment variable <code>SQUEAK_IMAGE</code> and, if it is set, uses its value as the name of the image to run. Otherwise <code>squeak</code> looks for an image called &#8216;squeak.image&#8217; in the current directory. If the image file does not exist then <code>squeak</code> prints a message indicating which image file it failed to find and then exits. If the extension &#8216;.image&#8217; is missing in the <i>image</i> argument or in the value of the <code>SQUEAK_IMAGE</code> variable, it will be appended automatically. </p>
<p> The <i>image</i> argument can be followed by a <i>script</i> name. This is the name of a &#8216;document&#8217; that should contain Smalltalk code to be executed on startup. The document can be either the name of a file or a URL starting with &#8216;http:&#8217;. Any <i>argument</i>s that appear after the <i>script</i> name are ignored, but are made available to the <i>script</i> from within Squeak via the method <code>getSystemAttribute:</code>. (See the section <code>SCRIPTS</code> below.) </p>
<p> If <i>image</i> is given as &#8216;&#8211;&#8216; then <code>squeak</code> immediately stops argument processing (and behaves as if <i>image</i> was not specified). This is useful to specify a <i>script</i> (possibly with script arguments) without specifying an explicit <i>image</i>.</p>
<h2>OPTIONS</h2>
<p> Command line options fall into two categories: &#8216;common&#8217; options that are recognised by the base VM and &#8216;specific&#8217; options that are tied to a particular display or sound driver. Common options will always be recognised by <code>squeak</code>, whereas a given specific option will be recognised only after <code>squeak</code> has loaded the driver to which it relates. Refer to the &#8216;-vm&#8217; option below for more details. </p>
<p> The common options recognised by <code>squeak</code> are as follows:</p>
<dl>
<dt><code>-encoding </code><i>enc</i></p>
<dd> specifies the internal character encoding to be used by Squeak. This affects the translation that the VM performs when importing text (from the keyboard or via &#8216;paste&#8217; from an external selection) or exporting text (pasting text from Squeak to another application, or when generating filenames containing special characters). In other words, it affects the correspondence between what Squeak displays on the screen and what it sends to (or receives from) external applications. The correct value depends on the way Squeak&#8217;s internal fonts are encoded. Current images are delivered with traditional Macintosh &#8216;New York&#8217; fonts that use <code>Mac Roman</code> encoding, and so this is the default internal encoding. If other fonts (from X11 or elsewhere) are imported into the image and used as system fonts then the this default translation will give incorrect results for diacritical marks and special characters. In such cases the <code>-encoding</code> option can be used to change the internal encoding, for example </p>
<pre><code>
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
- encoding ISO - 8859 - 15
</code></pre>
<p> (aka <code>Latin9</code>) which would be appropriate for many of the fonts designed for European languages.</p>
<dt><code>-help</code></p>
<dd> prints a short summary of the command-line syntax, options and available drivers, then exits.</p>
<dt><code>-memory </code><i>size[mk]</i></p>
<dd> requests that a fixed heap of <i>size</i> bytes be allocated for the Squeak image. If the suffix `<code>k</code>&#8216; is given then the argument is expressed in kilobytes. If the suffux `<code>m</code>&#8216; is given then the argument is expressed in megabytes. This option SHOULD NOT be used, unless there is a good reason to do so, since it places an arbitrary limit on Squeak&#8217;s object memory size.</p>
<dt><code>-mmap </code><i>size[mk]</i></p>
<dd> requests that a variable heap of at most <i>size</i> bytes be allocated. (The suffixes are as described for the &#8216;-memory&#8217; option.) <code>squeak</code> will initially allocate a heap that is large enough to hold the image, with a small amount of headroom. If at any time Squeak requires more memory for its image then additional space will be allocated dynamically. Likewise, when memory is no longer needed it will deallocated and returned to the system. The <i>size</i> argument places an upper limit on how big the heap can grow in this fashion. <code>squeak</code> uses a dynamic heap by default with the maximum size set to 75% of the available virtual memory or 1 gigabyte, whichever is smaller.</p>
<dt><code>-noevents</code></p>
<dd> disables the new (image 2.8 and later) event-driven input mechanism. This option is only useful for testing backwards compatibility with older images and should not be used.</p>
<dt><code>-notimer</code></p>
<dd> disables the use of the interval timer for keeping track of low-resolution time. (If you are having problems with file, sound or socket i/o reporting `interrupted system call&#8217; then setting this flag might help.)</p>
<dt><code>-pathenc </code><i>enc</i></p>
<dd> specifies the external character encoding to be used by Squeak when accessing the filesystem (file and directory pathnames). The correct value depends on the local platform&#8217;s characteristics. If no encoding conversion should be performed then this should be set to the same encoding as Squeak uses internally (see the <i>-encoding</i> option). Otherwise <code>ISO-8859-15</code> (aka <code>Latin9</code>) might make sense on a filesystem supporting 8-bit characters, and <code>UTF-8</code> for filesystems that use Unicode-based pathnames. The default is <code>UTF-8</code> which is correct for Mac OS X and very recent GNU/Linux distributions, and which (in an ideal world) will eventually be adopted by all Unix variants.</p>
<dt><code>-plugins </code><i>path</i></p>
<dd> specifies an alternative location for external plugins (collections of named primitives) and drivers (for display and sound). The <i>path</i> argument contains a pattern in which any occurrences of `<code>%n</code>&#8216; will be replaced by the name of the plugin or driver being loaded. The <i>path</i> can name either a directory or the plugin itself and can be absolute or relative (to the directory in which <code>squeak</code> was run). If a plugin or driver cannot be found in the location specified by <i>path</i> then the search continues in the default locations.</p>
<dt><code>-textenc </code><i>enc</i></p>
<dd> specifies the external character encoding to be used by Squeak when exchanging clipboard text with other applications. The default is <code>UTF-8</code> on Mac OS X and <code>ISO-8859-15</code> (aka <code>Latin9</code>) on other Unix systems. Note that X11 applications requesting the selection converted to <code>UTF8_STRING</code> data will (correctly) receive the clipboard text encoded as <code>UTF-8</code>, regardless of this setting. </p>
<p> Squeak recognises a subset of the encoding names defined by the IANA. (If you prefer to use the international currency symbol rather than the Euro symbol in external text then you might want to set this to <code>ISO-8859-1</code>, aka <code>Latin1</code>.)</p>
<dt><code>-version</code></p>
<dd> prints three or more lines of version information, as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*</p>
<dd> the architecture configured for the virtual machine at compile time, the compilation `sequence number&#8217;, the time and date of compilation, and the name (and version, if known) of the compiler that was used to compile <code>squeak</code>;</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*</p>
<dd> the complete <code><a href="/docs/linux/man/1-uname/">uname</a></code>(1) information for the host on which the virtual machine was compiled;</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*</p>
<dd> the default installed location for plugins and drivers;</dl>
<p> After printing the above, the virtual machine exits.</dl>
<dt><code>-vm </code><i>driver</i></p>
<dd> asks <code>squeak</code> to load a sound/display driver. For each supported device there is a corresponding driver that <code>squeak</code> loads during initialisation. Unless told otherwise, <code>squeak</code> will figure out sensible default drivers to load. This choice can be overridden using this option. The <i>driver</i> argument is a list of one or more &#8216;assignments&#8217; of the form </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>class</i>=<i>device</i> </p>
<p> separated by spaces or commas. The supported combinations are currently:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>display=X11</code></p>
<dd> to display the Squeak window on a local or remote X Window System server.</p>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>display=Quartz</code></p>
<dd> to display on the local Mac OS X desktop.</p>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>display=none</code></p>
<dd> to disable the display (and keyboard/mouse) entirely. (This driver is useful primarily for running &#8216;server&#8217; applications in Squeak.)</p>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sound=OSS</code></p>
<dd> provides sound input and output via the Open Sound System. (If you have a device called &#8216;/dev/dsp&#8217; then this is likely the one you want.)</p>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sound=MacOSX</code></p>
<dd> provides sound input/output via Core Audio on Mac OS X.</p>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sound=NAS</code></p>
<dd> provides sound i/o via the Network Audio System.</p>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sound=Sun</code></p>
<dd> provides sound on Sun Microsystems hardware.</p>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sound=none</code></p>
<dd> disables sound entirely. <code>squeak</code> will not attempt to play or record sounds when this driver is loaded.</dl>
</dl>
</dl>
<dl>
<dt>
<dd> Note that only those drivers relevant to the local platform will be available. Attempting to load an unsupported driver will cause <code>squeak</code> to exit with an error message. A list of available drivers is printed by the &#8216;-help&#8217; option. If a particular driver cannot load system libraries on which it depends then it will neither be listed nor be available to load at runtime.</dl>
<dl>
<dt>
<dd> Note also that on Mac OS X both the X11 and Quartz display drivers are supported, although the former will refuse to load if the X11 client libraries are not installed on the local machine. The Quartz driver will happily load (and Squeak will run as a fully-fledged application) even when <code>squeak</code> is invoked from the command line. Exercise caution when logged into Mac OS X from another machine: forgetting to set DISPLAY before trying to run <code>squeak</code> on the remote display could cause embarrassement.</dl>
<p> Options specific to the X11 display driver are as follows:</p>
<dl>
<dt><code>-browserWindow </code><i>id</i></p>
<dd> specifies the <i>id</i> of the window that <code>squeak</code> should use for its display. This option is intended for use when Squeak is running as a web browser plugin.</p>
<dt><code>-display </code><i>server</i></p>
<dd> specifies that Squeak should connect to the given display <i>server </i> instead of looking in the environment variable <code>DISPLAY</code> (the default behaviour) to find the name of the server to use.</p>
<dt><code>-cmdmod </code><i>N</i></p>
<dd> tells the VM to map modifier key <i>N</i> on the keyboard to the modifier code that the image expects for the Command key.</p>
<dt><code>-optmod </code><i>N</i></p>
<dd> tells the VM to map modifier key <i>N</i> on the keyboard to the modifier code that the image expects for the Option key.</p>
<dt><code>-compositioninput</code></p>
<dd> enables support for an overlay window in which individual characters (e.g., Japanese hiragana) are composed before being interpreted as a single character (e.g., Japanese kanji) by the image.</p>
<dt><code>-xicfont </code><i>font</i></p>
<dd> tells the VM to use the named <i>font</i> within the composition overlay window.</p>
<dt><code>-fullscreen</code></p>
<dd> causes the Squeak window to occupy as much of the screen area as possible. Implies &#8216;<code>-notitle</code>&#8216;.</p>
<dt><code>-headless</code></p>
<dd> disables the graphical display and mouse/keyboard input. This mode of operation is useful primarily for servers.</p>
<dt><code>-iconic</code></p>
<dd> asks the window manager to iconify the Squeak window at startup.</p>
<dt><code>-lazy</code></p>
<dd> causes Squeak to `snooze&#8217; whenever the main winodw is unmapped. This can be used if Squeak appears to be using consuming CPU time while idling (which should not normally be the case). Note that if this option is in effect, when the Squeak window is unmapped <code>squeak</code> will not respond to any external stimuli (other than to provide the X selection to requestors, when Squeak is the owner).</p>
<dt><code>-mapdelbs</code></p>
<dd> maps the Delete key onto Backspace. Backspace deletes the character to the left of the cursor and Delete normally deletes the character to the right of the cursor. With this option, Deletes will behave like Backspace. The behaviour of Backspace is not changed.</p>
<dt><code>-noxdnd</code></p>
<dd> disables support for the X drag-and-drop protocol.</p>
<dt><code>-nointl</code></p>
<dd> disables the handling of dead keys on international keyboards. Without this option, dead key handling is enabled if either <code>LC_ALL</code> or <code>LC_CTYPE</code> is set in the environment.</p>
<dt><code>-notitle</code></p>
<dd> disables the title bar on the Squeak window (if the window manager supports it). This option is implied by &#8216;<code>-fullscreen</code>&#8216;.</p>
<dt><code>-swapbtn</code></p>
<dd> swaps the yellow and blue buttons. (Traditionally, the red button is on the left, yellow in the middle and blue on the right. The colourful names come from the Xerox Alto on which Smalltalk was first implemented.) Squeak normally maps X buttons 1, 2 and 3 to the <code>red</code>, <code>yellow</code> and <code>blue</code> buttons, in that order. With this option, it maps X buttons 1, 2 and 3 to the <code>red</code>, <code>blue</code> and <code>yellow</code> buttons.)</p>
<dt><code>-xasync</code></p>
<dd> causes Squeak to use asynchronous display updates. The virtual machine normally flushes and synchronises the display connection at regular intervals. Using this option disables synchronisation, which will be performed only when the image explicitly requests it.</p>
<dt><code>-xshm</code></p>
<dd> enables the use of the X Shared Memory extension on servers that support it. This can dramatically improve display performance, but works only when Squeak is running on the server.</dl>
<p> Options specific to the FBDev display driver are as follows:</p>
<dl>
<dt><code>-fbdev </code><i>device</i></p>
<dd> Use the given framebuffer <i>device</i> instead of the default &#8216;/dev/fb0&#8217;.</p>
<dt><code>-kbmap </code><i>mapfile</i></p>
<dd> Load the keyboard map from the given <i>mapfile</i> instead of reading it from the running kernel. Note that <code>squeak</code> cannot (currently) read compressed or &#8216;shorthand&#8217; map files (as found in /usr/share/keymaps or /lib/kbd/keymaps). To generate a keymap file usable by <code>squeak</code>, execute the following program from the console: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>dumpkeys -f -n &#8211;keys-only &gt; key.map </p>
<p> If <code>squeak</code> encounters a problem while trying to load <i>mapfile</i>, it will print an error message and exit. See <code><a href="/docs/linux/man/5-keymaps/">keymaps</a></code>(5) for more information about the keymap file format. The programs <code><a href="/docs/linux/man/1-dumpkeys/">dumpkeys</a></code>(1), <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1), and <code><a href="/docs/linux/man/1-showkey/">showkey</a></code>(1) can be used to modify the keyboard map before creating a keymap file for <code>squeak</code>.</p>
<dt><code>-msdev </code><i>device</i></p>
<dd> Use the given mouse <i>device</i> instead of the default. The default is to try &#8216;/dev/psaux&#8217;, &#8216;/dev/input/mice&#8217; and &#8216;/dev/adbmouse&#8217;, in that order, and to use the first one that has a physical device attached.</p>
<dt><code>-msproto </code><i>protocol</i></p>
<dd> Use the given mouse <i>protocol</i> instead of the default. The supported protocols are &#8216;ps2&#8217; and &#8216;adb&#8217;. The default is &#8216;ps2&#8217; for mice attached to &#8216;/dev/psaux&#8217; or &#8216;/dev/input/mice&#8217;, and &#8216;adb&#8217; for mice attached to &#8216;/dev/adbmouse&#8217;.</p>
<dt><code>-vtlock</code></p>
<dd> Disallows VT switching, regardless of whether the request comes from the keyboard or from another program such as <code><a href="/docs/linux/man/1-chvt/">chvt</a></code>(1).</p>
<dt><code>-vtswitch</code></p>
<dd> Enables keyboard VT switching. Note that this option is effectively disabled if the &#8216;<code>-vtlock</code>&#8216; option is also enabled.</dl>
<p> Options specific to the OSS and MacOSX sound drivers are as follows:</p>
<dl>
<dt><code>-nomixer</code></p>
<dd> disables the primitives that change mixer (sound) settings. If you prefer that Squeak leave these alone (they are, after all, really the reponsibility of whichever mixer program or sound control panel you use) then this option is for you.</dl>
<p> Options specific to the ALSA sound driver are as follows:</p>
<dl>
<dt><code>-capture </code><i>device</i></p>
<dd> Uses the named input <i>device</i> for sound capture.</p>
<dt><code>-playback </code><i>device</i></p>
<dd> Uses the named output <i>device</i> for sound playback.</dl>
<p> Several common options are deprecated and are provided only for backward compatibility. These options should not be used and will be removed in a future release:</p>
<dl>
<dt><code>-display </code><i>dpy</i></p>
<dd> is equivalent to &#8216;-vm display=X11 -display <i>dpy</i>&#8216;.</p>
<dt><code>-headless</code></p>
<dd> is equivalent to &#8216;-vm display=X11 -headless&#8217;.</p>
<dt><code>-nodisplay</code></p>
<dd> is equivalent to &#8216;-vm display=none&#8217;.</p>
<dt><code>-nosound</code></p>
<dd> is equivalent to &#8216;-vm sound=none&#8217;.</p>
<dt><code>-quartz</code></p>
<dd> is equivalent to &#8216;-vm display=Quartz&#8217;.</dl>
<h2>ENVIRONMENT</h2>
<p> Many of the options that can be set on the command line can also be set from environment variables.</p>
<dl>
<dt><code>SQUEAK_ASYNC</code></p>
<dd> if set in the environment then equivalent to the &#8216;<code>-xasync</code>&#8216; flag. (The value is ignored.)</p>
<dt><code>SQUEAK_CAPTURE</code></p>
<dd> see &#8216;<code>-capture</code>&#8216;.</p>
<dt><code>SQUEAK_COMPOSITIONINPUT</code></p>
<dd> if set in the environment then equivalent to the &#8216;<code>-compositioninput</code>&#8216; flag. (The value is ignored.)</p>
<dt><code>SQUEAK_ENCODING</code></p>
<dd> the name of the internal character encoding used by Squeak. Equivalent to giving the &#8216;<code>-encoding</code>&#8216; command-line option if set.</p>
<dt><code>SQUEAK_FBDEV</code></p>
<dd> the name of the framebuffer device to use when running on the console. See the &#8216;<code>-fbdev</code>&#8216; option.</p>
<dt><code>SQUEAK_FULLSCREEN</code></p>
<dd> equivalent to &#8216;<code>-fullscreen</code>&#8216; if set.</p>
<dt><code>SQUEAK_ICONIC</code></p>
<dd> equivalent to the &#8216;<code>-iconic</code>&#8216; flag.</p>
<dt><code>SQUEAK_IMAGE</code></p>
<dd> the name of the image file to execute if no <i>image</i> argument is given on the command line.</p>
<dt><code>SQUEAK_KBMAP</code></p>
<dd> the name of the keymap file to use when running on the console. See the &#8216;<code>-kbmap</code>&#8216; option.</p>
<dt><code>SQUEAK_LAZY</code></p>
<dd> equivalent to the &#8216;<code>-lazy</code>&#8216; flag.</p>
<dt><code>SQUEAK_MAPDELBS</code></p>
<dd> equivalent to the &#8216;<code>-mapdelbs</code>&#8216; flag.</p>
<dt><code>SQUEAK_MEMORY</code></p>
<dd> the initial size of the heap, with optional &#8216;k&#8217; or &#8216;m&#8217; suffix. Equivalent to the &#8216;<code>-memory </code><i>size</i><code>[km]</code>&#8216; flag.</p>
<dt><code>SQUEAK_MSDEV</code></p>
<dd> the name of the mouse device to use when running on the console. See the &#8216;<code>-msdev</code>&#8216; option.</p>
<dt><code>SQUEAK_MSPROTO</code></p>
<dd> the name of the mouse protocl to use when running on the console. See the &#8216;<code>-msproto</code>&#8216; option.</p>
<dt><code>SQUEAK_VTLOCK</code></p>
<dd> if set then equivalent to specifying the &#8216;<code>-vtlock</code>&#8216; option on the command line.</p>
<dt><code>SQUEAK_VTSWITCH</code></p>
<dd> if set then equivalent to specifying the &#8216;<code>-vtswitch</code>&#8216; option on the command line.</p>
<dt><code>SQUEAK_NOEVENTS</code></p>
<dd> if set, equivalent to &#8216;<code>-noevents</code>&#8216;.</p>
<dt><code>SQUEAK_NOINTL</code></p>
<dd> equivalent to &#8216;<code>-nointl</code>&#8216; if set.</p>
<dt><code>SQUEAK_NOMIXER</code></p>
<dd> equivalent to &#8216;<code>-nomixer</code>&#8216; if set.</p>
<dt><code>SQUEAK_NOTIMER</code></p>
<dd> equivalent to &#8216;<code>-notimer</code>&#8216; if set.</p>
<dt><code>SQUEAK_NOTITLE</code></p>
<dd> if set, equivalent to &#8216;<code>-notitle</code>&#8216;.</p>
<dt><code>SQUEAK_PATHENC</code></p>
<dd> the name of the character encoding used to construct file and directory names. Equivalent to giving the &#8216;<code>-pathenc</code>&#8216; command-line option if set.</p>
<dt><code>SQUEAK_PLAYBACK</code></p>
<dd> see &#8216;<code>-playback</code>&#8216;.</p>
<dt><code>SQUEAK_PLUGINS</code></p>
<dd> see &#8216;<code>-plugins</code>&#8216;.</p>
<dt><code>SQUEAK_SWAPBTN</code></p>
<dd> equivalent to &#8216;<code>-swapbtn</code>&#8216; if set.</p>
<dt><code>SQUEAK_TEXTENC</code></p>
<dd> the name of the character encoding used to copy/paste text from/to external applications. Equivalent to giving the &#8216;<code>-textenc</code>&#8216; command-line option if set.</p>
<dt><code>SQUEAK_VM</code></p>
<dd> contains the names of one or more drivers to be loaded during initialisation. See the &#8216;<code>-vm</code>&#8216; option for details.</p>
<dt><code>SQUEAK_XICFONT</code></p>
<dd> if set in the environment then it provides a default name for the composition overlay font; see the &#8216;<code>-xicfont</code>&#8216; flag.</p>
<dt><code>SQUEAK_XSHM</code></p>
<dd> equivalent to &#8216;<code>-xshm</code>&#8216;.</dl>
<p> If an environment variable and a command-line option conflict over a particular value then normally the value in the command line takes precedence. The exception to this rule is the &#8216;-vm&#8217; option. Environment variables are processed before command-line arguments and &#8216;-vm&#8217; cannnot be used to unload a driver that was loaded while processing the contents of &#8216;SQUEAK_VM&#8217;. </p>
<p> <code>squeak</code> also checks the environment for <code>LC_ALL</code> and <code>LC_CTYPE</code>. If either of these variables is set then support for international keyboards (including dead keys for diacritical marks) is enabled. To prevent this support being enabled even when one or both of these variables is set, use the &#8216;-nointl&#8217; option (or set <code>SQUEAK_NOINTL</code> in the environment). For example, to start <code>squeak</code> with support for dead keys on Spanish keyboards, with Latin-1 encoding of external characters and the default MacRoman internal font encoding, run <code>squeak</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
export LC_CTYPE=es_ES
export SQUEAK_TEXTENC=latin1
squeak
</pre>
</dl>
<h2>SCRIPTS</h2>
<p> Squeak can load and execute a &#8216;script&#8217; file containing Smalltalk code at startup. The name of the file should be given as the <i>script</i> argument to <code>squeak</code>. For example, assuming that the image &#8216;foo.image&#8217; contains an open Transcript window, then the following represents the &#8216;hello world&#8217; program for Squeak: </p>
<dl>
<dt>
<dd>
<pre>
Transcript cr; show: 'Hello, world'.
</pre>
</dl>
<p> If this script is in a file called &#8216;hello.sq&#8217;, then it could be run like this: </p>
<dl>
<dt>
<dd>
<pre>
squeak foo.image hello.sq
</pre>
</dl>
<p> It is also possible to make &#8216;self interpreting&#8217; scripts by adding an &#8216;interpreter line&#8217; to the start of the script. The &#8216;hello.sq&#8217; file could be changed to </p>
<dl>
<dt>
<dd>
<pre>
#!/usr/bin/squeak --
Transcript cr; show: 'Hello, world'.
</pre>
</dl>
<p> and then made executable with </p>
<dl>
<dt>
<dd>
<pre>
chmod +x hello.sq
</pre>
</dl>
<p> and then invoked by running the script file directly: </p>
<dl>
<dt>
<dd>
<pre>
SQUEAK_IMAGE=&quot;foo.image&quot;
export SQUEAK_IMAGE
./hello.sq
</pre>
</dl>
<p> If any <i>argument</i>s are present after the <i>script</i> name then they can be retrieved from within the script using the method </p>
<dl>
<dt>
<dd>
<pre>
Smalltalk getSystemAttribute: <i>n</i>
</pre>
</dl>
<p> where <i>n</i> is the index of the argument, starting at 3 for the first argument. (See the method comment for </p>
<dl>
<dt>
<dd>
<pre>
SystemDictionary&gt;&gt;getSystemAttribute:
</pre>
</dl>
<p> in the image for an explanation of the meanings of the indices.) </p>
<p> As an example of this, here is the &#8216;echo&#8217; program written as a Squeak script: </p>
<dl>
<dt>
<dd>
<pre><code>
#!/ usr / bin / squeak --
"Echo arguments to the Transcript." | i a |
    i : = 2.
              [(a
                : = Smalltalk getSystemAttribute
                : (i
                   : = i + 1))
                   notNil] whileTrue : [Transcript space; show:a]
                                           .
</code></pre>
</dl>
<p> When run as </p>
<dl>
<dt>
<dd>
<pre>
./echo.sq one two three
</pre>
</dl>
<p> this would print &#8216;one two three&#8217; in the Transcript window.</p>
<h2>DIAGNOSTICS</h2>
<dl>
<dt><code>inisqueak</code></p>
<dd> prints several informational messages while doing its stuff. If it encounters a problem it prints an appropriate message before bailing out. The messages should be self-explanatory.</p>
<dt><code>squeak</code></p>
<dd> normally does not print anything at all. If it prints something then there is a problem. The messages should be self-explanatory.</dl>
<h2>FILES</h2>
<p> <i>/usr/share/squeak/SqueakV3.sources</i></p>
<dl>
<dt>
<dd> Shared system sources file for the Squeak image. There must be a copy of (or link to) this file in the working directory when running <code>squeak</code>.</dl>
<p> <i>/usr/share/squeak/Squeak*.image</i> <i>/usr/share/squeak/Squeak*.changes</i></p>
<dl>
<dt>
<dd> Distributed image and changes files holding a `shapshot&#8217; of a live Squeak session. (The contents of these files change during a session, and so private copies should always be made before running <code>squeak</code> for the first time. See <code><a href="/docs/linux/man/1-inisqueak/">inisqueak</a></code>(1)).</dl>
<p> <i>./SqueakV3.sources</i></p>
<dl>
<dt>
<dd> A link to the system sources file.</dl>
<p> <i>./</i>name<i>.image</i><br />
 <i>./</i>name<i>.changes</i></p>
<dl>
<dt>
<dd> Private copies of image and changes files.</dl>
<p> <i>/usr/lib64/squeak/3.10-5/*.so</i><br />
 <i>/usr/lib64/squeak/3.10-5/*.la</i></p>
<dl>
<dt>
<dd> Virtual machine &#8216;plugins&#8217; (containing primitives that are loaded on demand) and drivers (for different types of display and sound hardware).</dl>
<p> <i>/usr/bin/squeak</i><br />
 <i>/usr/bin/inisqueak</i></p>
<dl>
<dt>
<dd> The Squeak virtual machine and personal image installer script.</dl>
<p> <i>/usr/share/man/squeak.1</i></p>
<dl>
<dt>
<dd> This manual page.</dl>
<p> <i>/usr/doc/squeak/*</i></p>
<dl>
<dt>
<dd> Miscellaneous documentation.</dl>
<h2>NOTES</h2>
<p> This manual page documents version 3.10-5 of Unix Squeak. It may not be appropriate for any other version. </p>
<p> The image and changes files containing a saved Squeak session are intimately related. They should always be used together, never be separated, and under no circumstances should an image be run with a changes file that has been used with a different image. Failure to adhere to the above could cause the source code for the methods in the image to become garbled and impossible to retrieve. </p>
<p> The Unix Squeak virtual machine fully supports OpenGL in both the X11 and Quartz display drivers. Open Croquet will run just fine with either of these drivers (and many Mac OS X users will even have the choice of which driver to use :).</p>
<h2>BUGS</h2>
<p> If a &#8216;binary&#8217; option is enabled by an environment variable, there is no way to disable it on the command line. </p>
<p> Similarly, drivers specified in the <i>SQUEAK_VM</i> environment variable cannot be overridden by passing options on the command line. </p>
<p> <code>squeak</code> should never crash. In the unlikely event that it does crash, or prints any kind of message that <i>does not</i> appear to be caused by incorrect arguments or illegal operations from within a Squeak program, please send a bug report to: &lt;ian.piumarta [at] squeakland.org&gt;. (Do not send bug reports to the general-purpose &#8216;squeak-dev&#8217; mailing list. They will not be read. If you feel you must post a bug report to a mailing list, send it to the Squeak &#8216;vm-dev&#8217; mailing list in addition to the above email address.)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Ian Piumarta.</p>
<h2>SEE ALSO</h2>
<p> Dan Ingalls, Ted Kaehler, John Maloney, Scott Wallace and Alan Kay, <i>Back to the Future: The Story of Squeak, A Practical Smalltalk Written in Itself</i>. Proc. OOPSLA&#8217;97. </p>
<p> The official Squeak home page:</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://squeak.org">http://squeak.org</a></code></dl>
<p> The general-purpose &#8216;squeak-dev&#8217; mailing list (not for VM-related bug reports):</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://lists.squeakfoundation.org/listinfo/squeak-dev">http://lists.squeakfoundation.org/listinfo/squeak-dev</a></code></dl>
<p> The Squeak &#8216;vm-dev&#8217; mailing list (amongst others):</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://discuss.squeakfoundation.org/">http://discuss.squeakfoundation.org/</a></code></dl>
<p> The latest source and binary distributions of Unix Squeak:</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://squeak.hpl.hp.com/~piumarta/squeak">http://squeak.hpl.hp.com/~piumarta/squeak</a></code></dl>
<h2>Index</h2>
