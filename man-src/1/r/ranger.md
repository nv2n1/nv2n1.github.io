---
title: "ranger(1)"
name: "ranger"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ranger/"
description: "ranger – visual file manager"
---

<p>ranger &#8211; visual file manager</p>
<h2>SYNOPSIS</h2>
<p> <code>ranger</code> [<code>&#8211;version</code>] [<code>&#8211;help</code>] [<code>&#8211;debug</code>] [<code>&#8211;clean</code>] [<code>&#8211;cachedir</code>=<i>directory</i>] [<code>&#8211;confdir</code>=<i>directory</i>] [<code>&#8211;datadir</code>=<i>directory</i>] [<code>&#8211;copy-config</code>=<i>which</i>] [<code>&#8211;choosefile</code>=<i>target</i>] [<code>&#8211;choosefiles</code>=<i>target</i>] [<code>&#8211;choosedir</code>=<i>target</i>] [<code>&#8211;selectfile</code>=<i>filepath</i>] [<code>&#8211;show-only-dirs</code>] [<code>&#8211;list-unused-keys</code>] [<code>&#8211;list-tagged-files</code>=<i>tag</i>] [<code>&#8211;profile</code>] [<code>&#8211;cmd</code>=<i>command</i>] [<i>path &#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> ranger is a console file manager with <font SIZE="-1">VI</font> key bindings.</p>
<h2>RESOURCES</h2>
<p> This <i>manual</i> contains instructions on how to use and configure ranger. </p>
<p> Inside <i>ranger</i>, you can press <i>?</i> for a list of key bindings, commands or settings. </p>
<p> The file <i></i><font SIZE="-1"><i>README</i></font><i>.md</i> contains install instructions. </p>
<p> The file <i></i><font SIZE="-1"><i>HACKING</i></font><i>.md</i> contains guidelines for code modification. </p>
<p> The directory <i>doc/configs</i> contains configuration files. They are usually installed to <i>/etc/ranger/config</i> and can be obtained with ranger&#8217;s &#8211;copy-config option. </p>
<p> The directory <i>examples</i> contains reference implementations for ranger plugins, sample configuration files and some programs for integrating ranger with other software. They are usually installed to <i>/usr/share/doc/ranger/examples</i>. </p>
<p> The man page of <code><a href="/docs/linux/man/1-rifle/">rifle</a></code>(1) describes the functions of the file opener </p>
<p> The section <i></i><font SIZE="-1"><i>LINKS</i></font><i></i> of this man page contains further resources.</p>
<h2>POSITIONAL ARGUMENTS</h2>
<dl>
<dt><i>path &#8230;</i></p>
<dd> Each path will be opened in a tab and if the path is a file it will be selected. Omitting this is equivalent to providing the current directory.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Activate the debug mode: Whenever an error occurs, ranger will exit and print a full traceback. The default behavior is to merely print the name of the exception in the statusbar/log and try to keep running.</p>
<dt><code>-c</code>, <code>&#8211;clean</code></p>
<dd> Activate the clean mode: ranger will not access or create any configuration files nor will it leave any traces on your system. This is useful when your configuration is broken, when you want to avoid clutter, etc.</p>
<dt><code>&#8211;cachedir</code>=<i>dir</i></p>
<dd> Change the cache directory of ranger from <tt>$XDG_CACHE_HOME</tt> or ~/.cache/ranger to &#8220;dir&#8221;.</p>
<dt><code>-r</code> <i>dir</i>, <code>&#8211;confdir</code>=<i>dir</i></p>
<dd> Change the configuration directory of ranger from <tt>$XDG_CONFIG_HOME</tt> or ~/.config/ranger to &#8220;dir&#8221;.</p>
<dt><code>&#8211;datadir</code>=<i>dir</i></p>
<dd> Change the data directory of ranger from <tt>$XDG_DATA_HOME</tt> or ~/.local/share/ranger to &#8220;dir&#8221;.</p>
<dt><code>&#8211;copy-config</code>=<i>file</i></p>
<dd> Create copies of the default configuration files in your local configuration directory. Existing ones will not be overwritten. Possible values: <i>all</i>, <i>commands</i>, <i>commands_full</i>, <i>rc</i>, <i>rifle</i>, <i>scope</i>. </p>
<p> Note: You may want to disable loading of the global configuration files by exporting <i>RANGER_LOAD_DEFAULT_RC=FALSE</i> in your environment. See also: <font SIZE="-1"><code>FILES</code></font>, <font SIZE="-1"><code>ENVIRONMENT</code></font> </p>
<p> &#8211;copy-config=<code>commands</code> will copy only a small sample configuration file with a thoroughly commented example. It is recommended to keep this file tidy to avoid getting defunct commands on ranger upgrades. The full default commands.py can be copied with &#8211;copy-config=<code>commands_full</code>, but that file will be ignored by ranger and serves only as a reference for making your own commands.</p>
<dt><code>&#8211;choosefile</code>=<i>targetfile</i></p>
<dd> Allows you to pick a file with ranger. This changes the behavior so that when you open a file, ranger will exit and write the absolute path of that file into <i>targetfile</i>.</p>
<dt><code>&#8211;choosefiles</code>=<i>targetfile</i></p>
<dd> Allows you to pick multiple files with ranger. This changes the behavior so that when you open a file, ranger will exit and write the absolute paths of all selected files into <i>targetfile</i>, adding one newline after each filename.</p>
<dt><code>&#8211;choosedir</code>=<i>targetfile</i></p>
<dd> Allows you to pick a directory with ranger. When you exit ranger, it will write the last visited directory into <i>targetfile</i>.</p>
<dt><code>&#8211;selectfile</code>=<i>targetfile</i></p>
<dd> Open ranger with <i>targetfile</i> selected. This is a legacy option, superseded by the behavior for the <font SIZE="-1">POSITIONAL ARGUMENTS.</font></p>
<dt><code>&#8211;show-only-dirs</code></p>
<dd> Display only the directories. May be used in conjunction with <code>&#8211;choosedir</code>=<i>targetfile</i>.</p>
<dt><code>&#8211;list-unused-keys</code></p>
<dd> List common keys which are not bound to any action in the &#8220;browser&#8221; context. This list is not complete, you can bind any key that is supported by curses: use the key code returned by <tt>&quot;getch()&quot;</tt>.</p>
<dt><code>&#8211;list-tagged-files</code>=<i>tag</i></p>
<dd> List all files which are tagged with the given tag. Note: Tags are single characters. The default tag is &#8220;*&#8221;</p>
<dt><code>&#8211;profile</code></p>
<dd> Print statistics of <font SIZE="-1">CPU</font> usage on exit.</p>
<dt><code>&#8211;cmd</code>=<i>command</i></p>
<dd> Execute the command after the configuration has been read. Use this option multiple times to run multiple commands.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a list of options and exit.</dl>
<h2>CONCEPTS</h2>
<p> This part explains how certain parts of ranger work and how they can be used efficiently.</p>
<h3><font SIZE="-1">TAGS</font></h3>
<p> Tags are single characters which are displayed left of a filename. You can use tags however you want. Press &#8220;t&#8221; to toggle tags and &#8220;ut&#8221; to remove any tags of the selection. The default tag is an Asterisk (&#8220;*&#8221;), but you can use any tag by typing <i>&quot;&lt;tagname&gt;</i>.</p>
<h3><font SIZE="-1">PREVIEWS</font></h3>
<p> By default, only text files are previewed, but you can enable external preview scripts by setting the option <tt>&quot;use_preview_script&quot;</tt> and <tt>&quot;preview_files&quot;</tt> to true. </p>
<p> This default script is <i></i>%rangerdir<i>/data/scope.sh</i>. It contains more documentation and calls to many external programs to generate previews. They are automatically used when available but completely optional.</p>
<dl>
<dt>For general usage:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> <tt>&quot;file&quot;</tt> for determining file types</p>
<dt>&#8211;</p>
<dd> <tt>&quot;chardet&quot;</tt> (Python package) for improved encoding detection of text files</p>
<dt>&#8211;</p>
<dd> <tt>&quot;sudo&quot;</tt> to use the &#8220;run as root&#8221; feature</p>
<dt>&#8211;</p>
<dd> <tt>&quot;python-bidi&quot;</tt> (Python package) to display right-to-left file names correctly (Hebrew, Arabic)</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>For enhanced file previews (with scope.sh):</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> <tt>&quot;img2txt&quot;</tt> (from <tt>&quot;caca-utils&quot;</tt>) for ASCII-art image previews</p>
<dt>&#8211;</p>
<dd> <tt>&quot;w3mimgdisplay&quot;</tt>, <tt>&quot;ueberzug&quot;</tt>, <tt>&quot;mpv&quot;</tt>, <tt>&quot;iTerm2&quot;</tt>, <tt>&quot;kitty&quot;</tt>, <tt>&quot;terminology&quot;</tt> or <tt>&quot;urxvt&quot;</tt> for image previews</p>
<dt>&#8211;</p>
<dd> <tt>&quot;convert&quot;</tt> (from <tt>&quot;imagemagick&quot;</tt>) to auto-rotate images and for <font SIZE="-1">SVG</font> previews</p>
<dt>&#8211;</p>
<dd> <tt>&quot;ffmpegthumbnailer&quot;</tt> for video thumbnails</p>
<dt>&#8211;</p>
<dd> <tt>&quot;highlight&quot;</tt>, <tt>&quot;bat&quot;</tt> or <tt>&quot;pygmentize&quot;</tt> for syntax highlighting of code</p>
<dt>&#8211;</p>
<dd> <tt>&quot;atool&quot;</tt>, <tt>&quot;bsdtar&quot;</tt>, <tt>&quot;unrar&quot;</tt> and/or <tt>&quot;7z&quot;</tt> to preview archives</p>
<dt>&#8211;</p>
<dd> <tt>&quot;bsdtar&quot;</tt>, <tt>&quot;tar&quot;</tt>, <tt>&quot;unrar&quot;</tt>, <tt>&quot;unzip&quot;</tt> and/or <tt>&quot;zipinfo&quot;</tt> (and <tt>&quot;sed&quot;</tt>) to preview archives as their first image</p>
<dt>&#8211;</p>
<dd> <tt>&quot;lynx&quot;</tt>, <tt>&quot;w3m&quot;</tt> or <tt>&quot;elinks&quot;</tt> to preview html pages</p>
<dt>&#8211;</p>
<dd> <tt>&quot;pdftotext&quot;</tt> or <tt>&quot;mutool&quot;</tt> (and <tt>&quot;fmt&quot;</tt>) for textual pdf previews, <tt>&quot;pdftoppm&quot;</tt> to preview as image</p>
<dt>&#8211;</p>
<dd> <tt>&quot;djvutxt&quot;</tt> for textual DjVu previews, <tt>&quot;ddjvu&quot;</tt> to preview as image</p>
<dt>&#8211;</p>
<dd> <tt>&quot;calibre&quot;</tt> or <tt>&quot;epub-thumbnailer&quot;</tt> for image previews of ebooks</p>
<dt>&#8211;</p>
<dd> <tt>&quot;transmission-show&quot;</tt> for viewing BitTorrent information</p>
<dt>&#8211;</p>
<dd> <tt>&quot;mediainfo&quot;</tt> or <tt>&quot;exiftool&quot;</tt> for viewing information about media files</p>
<dt>&#8211;</p>
<dd> <tt>&quot;odt2txt&quot;</tt> for OpenDocument text files (odt, ods, odp and sxw)</p>
<dt>&#8211;</p>
<dd> <tt>&quot;python&quot;</tt> or <tt>&quot;jq&quot;</tt> for <font SIZE="-1">JSON</font> files</p>
<dt>&#8211;</p>
<dd> <tt>&quot;fontimage&quot;</tt> for font previews</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> Install these programs (just the ones you need) and scope.sh will automatically use them. </p>
<p> Independently of the preview script, there is a feature to preview images by drawing them directly into the terminal. To enable this feature, set the option <tt>&quot;preview_images&quot;</tt> to true and enable one of the image preview modes: </p>
<p> <i>iTerm2</i> </p>
<p> This only works in iTerm2 compiled with image preview support, but works over ssh. </p>
<p> To enable this feature, set the option <tt>&quot;preview_images_method&quot;</tt> to iterm2. </p>
<p> This feature relies on the dimensions of the terminal&#8217;s font. By default, a width of 8 and height of 11 are used. To use other values, set the options <tt>&quot;iterm2_font_width&quot;</tt> and <tt>&quot;iterm2_font_height&quot;</tt> to the desired values. </p>
<p> <i>kitty</i> </p>
<p> This only works in Kitty. It requires <font SIZE="-1">PIL</font> (or pillow) to work. Allows remote image previews, for example in an ssh session. </p>
<p> To enable this feature, set the option <tt>&quot;preview_images_method&quot;</tt> to kitty. </p>
<p> <i>terminology</i> </p>
<p> This only works in terminology. It can render vector graphics, but works only locally. </p>
<p> To enable this feature, set the option <tt>&quot;preview_images_method&quot;</tt> to terminology. </p>
<p> <i>ueberzug</i> </p>
<p> U.berzug is a command line utility which draws images on terminals using child windows. It requires <font SIZE="-1">PIL</font> (or pillow) and relies on X11. This makes it compatible (in a limited way, i.e., tmux splits are not supported) with many terminals and tmux but not the Linux console or Wayland. </p>
<p> To enable this feature, set the option <tt>&quot;preview_images_method&quot;</tt> to ueberzug. </p>
<p> <i>urxvt</i> </p>
<p> This only works in urxvt compiled with pixbuf support. Does not work over ssh. </p>
<p> Essentially this mode sets an image as a terminal background temporarily, so it will break any previously set image background. </p>
<p> To enable this feature, set the option <tt>&quot;preview_images_method&quot;</tt> to urxvt. </p>
<p> <i>urxvt-full</i> </p>
<p> The same as urxvt but utilizing not only the preview pane but the whole terminal window. </p>
<p> To enable this feature, set the option <tt>&quot;preview_images_method&quot;</tt> to urxvt-full. </p>
<p> <i>w3m</i> </p>
<p> This does not work over ssh, requires certain terminals (tested on &#8220;xterm&#8221; and &#8220;urxvt&#8221;) and is incompatible with tmux, although it works with screen. </p>
<p> To enable this feature, install the program &#8220;w3m&#8221; and set the option <tt>&quot;preview_images_method&quot;</tt> to w3m. </p>
<p> When using a terminal with a nonzero border which is not automatically detected, the w3m preview will be misaligned. Use the <tt>&quot;w3m_offset&quot;</tt> option to manually adjust the image offset. This should be the same value as the terminal&#8217;s border value.</p>
<h3><font SIZE="-1">SELECTION</font></h3>
<p> The <i>selection</i> is defined as &#8220;All marked files <font SIZE="-1">IF THERE ARE ANY,</font> otherwise the current file.&#8221; Be aware of this when using the :delete command, which deletes all files in the selection. </p>
<p> You can mark files by pressing &lt;Space&gt;, v, etc. A yellow <code>Mrk</code> symbol at the bottom right indicates that there are marked files in this directory.</p>
<h3><font SIZE="-1">MACROS</font></h3>
<p> Macros can be used in commands to abbreviate things. </p>
<pre>
 %f   the highlighted file
 %d   the path of the current directory
 %s   the selected files in the current directory
 %t   all tagged files in the current directory
 %c   the full paths of the currently copied/cut files
 %p   the full paths of selected files
</pre>
<p> The macros <tt>%f</tt>, <tt>%d</tt>, <tt>%p</tt>, and <tt>%s</tt> also have upper case variants, <tt>%F</tt>, <tt>%D</tt>, <tt>%P</tt>, and <tt>%S</tt>, which refer to the next tab. To refer to specific tabs, add a number in between. (%7s = selection of the seventh tab.) </p>
<p> <tt>%c</tt> is the only macro which ranges out of the current directory. So you may &#8220;abuse&#8221; the copying function for other purposes, like diffing two files which are in different directories: </p>
<pre>
 Yank the file A (type yy), move to the file B, then type
 @diff %c %f
</pre>
<p> Macros for file paths are generally shell-escaped so they can be used in the <tt>&quot;shell&quot;</tt> command. </p>
<p> When mapping keys you can use the placeholder &lt;any&gt;, the key entered in that position can be used through the <tt>%any</tt> and <tt>%any_path</tt> macros. (When using multiple &lt;any&gt; placeholders you can index the macros: <tt>%any0</tt>, <tt>%any_path0</tt>, <tt>%any1</tt>, <tt>%any_path1</tt>&#8230;) The macro <tt>%any</tt> will be replaced with the key pressed in the position of the &lt;any&gt; placeholder. The macro <tt>%any_path</tt> will be replaced with the path of the bookmark mapped to the key pressed in the position of the &lt;any&gt; placeholder. For example this macro can be used to echo the key that was pressed after &#8220;c&#8221;: </p>
<pre>
 map c&lt;any&gt; echo %any
</pre>
<p> <tt>%any</tt> is used in the ranger configuration to create a keybinding for adding a bookmark. c&lt;set_bookmark&gt; creates a bookmark for the current directory and the key for the bookmark is the first supplied argument. In this case the key pressed after &#8220;m&#8221;: </p>
<pre>
 map m&lt;any&gt; set_bookmark %any
</pre>
<p> The <tt>%any_path</tt> macro can be used to echo the path of the bookmark that is set to the key pressed after &#8220;c&#8221;: </p>
<pre>
 map c&lt;any&gt; echo %any_path
</pre>
<p> A practical example of the use of <tt>%any_path</tt> is the pasting of cut/copied files to a bookmarked directory: </p>
<pre>
 map p'&lt;any&gt; paste dest=%any_path
</pre>
<p> The macro <tt>%rangerdir</tt> expands to the directory of ranger&#8217;s python library, you can use it for something like this command:<br />
&nbsp;alias show_commands shell less&nbsp;<tt>%rangerdir</tt>/config/commands.py </p>
<p> <tt>%confdir</tt> expands to the directory given by <code>&#8211;confdir</code>. </p>
<p> <tt>%datadir</tt> expands to the directory given by <code>&#8211;datadir</code>. </p>
<p> The macro <tt>%space</tt> expands to a space character. You can use it to add spaces to the end of a command when needed, while preventing editors to strip spaces off the end of the line automatically. </p>
<p> To write a literal %, you need to escape it by writing %%. </p>
<p> Note that macros are expanded twice when using chain. For example, to insert a space character in a chained command, you would write %%space:<br />
&nbsp;chain command1;&nbsp;command2%%space</p>
<h3><font SIZE="-1">BOOKMARKS</font></h3>
<p> Type <code>m&lt;key&gt;</code> to bookmark the current directory. You can re-enter this directory by typing <code>`&lt;key&gt;</code>. &lt;key&gt; can be any letter or digit. Unlike vim, both lowercase and uppercase bookmarks are persistent. </p>
<p> Each time you jump to a bookmark, the special bookmark at key ` will be set to the last directory. So typing &#8220;&#8220;&#8221; gets you back to where you were before. </p>
<p> Bookmarks are selectable when tabbing in the :cd command. </p>
<p> Note: The bookmarks &#8216; (Apostrophe) and ` (Backtick) are the same.</p>
<h3><font SIZE="-1">RIFLE</font></h3>
<p> Rifle is the file opener of ranger. It can be used as a standalone program or a python module. It is located at <i></i>$repo<i>/ranger/ext/rifle.py</i>. In contrast to other, more simple file openers, rifle can automatically find installed programs so it can be used effectively out of the box on a variety of systems. </p>
<p> It&#8217;s configured in <i>rifle.conf</i> through a list of conditions and commands. For each line the conditions are checked and if they are met, the respective command is taken into consideration. By default, simply the first matching rule is used. In ranger, you can list and choose rules by typing &#8220;r&#8221; or simply by typing &#8220;&lt;rulenumber&gt;&lt;enter&gt;&#8221;. If you use rifle standalone, you can list all rules with the &#8220;-l&#8221; option and pick a rule with &#8220;-p &lt;number&gt;&#8221;. </p>
<p> The rules, along with further documentation, are contained in <i></i>$repo<i>/ranger/config/rifle.conf</i>.</p>
<h3><font SIZE="-1">FLAGS</font></h3>
<p> Flags give you a way to modify the behavior of the spawned process. They are used in the commands <tt>&quot;:open_with&quot;</tt> (key &#8220;r&#8221;) and <tt>&quot;:shell&quot;</tt> (key &#8220;!&#8221;). </p>
<pre>
 f   Fork the process, i.e. run in background. Please use this flag
     instead of calling &quot;disown&quot; or &quot;nohup&quot;, to avoid killing the
     background command when pressing Ctrl+C in ranger.
 c   Run the current file only, instead of the selection
 r   Run application with root privilege (requires sudo)
 t   Run application in a new terminal window
</pre>
<p> There are some additional flags that can currently be used only in the <tt>&quot;shell&quot;</tt> command: (for example <tt>&quot;:shell -w df&quot;</tt>) </p>
<pre>
 p   Redirect output to the pager
 s   Silent mode.  Output will be discarded.
 w   Wait for an Enter-press when the process is done
</pre>
<p> By default, all the flags are off unless otherwise specified in <i>rc.conf</i> key bindings or <i>rifle.conf</i> rules. You can specify as many flags as you want. An uppercase flag negates the effect: &#8220;ffcccFsf&#8221; is equivalent to &#8220;cs&#8221;. </p>
<p> The terminal program name for the &#8220;t&#8221; flag is taken from the environment variable <tt>$TERMCMD</tt>. If it doesn&#8217;t exist, it tries to extract it from <tt>$TERM</tt>, uses &#8220;x-terminal-emulator&#8221; as a fallback, and then &#8220;xterm&#8221; if that fails. </p>
<p> Examples: <tt>&quot;:open_with c&quot;</tt> will open the file that you currently point at, even if you have selected other files. <tt>&quot;:shell -w df&quot;</tt> will run &#8220;df&#8221; and wait for you to press Enter before switching back to ranger.</p>
<h3><font SIZE="-1">PLUGINS</font></h3>
<p> ranger&#8217;s plugin system consists of python files which are located in <i>~/.config/ranger/plugins/</i> and are imported in alphabetical order when starting ranger. A plugin changes rangers behavior by overwriting or extending a function that ranger uses. This allows you to change pretty much every part of ranger, but there is no guarantee that things will continue to work in future versions as the source code evolves. </p>
<p> Adding new commands via a plugin as simple as specifying them like you would do in the <i>commands.py</i>. </p>
<p> There are some hooks that are specifically made for the use in plugins. They are functions that start with hook_ and can be found throughout the code. </p>
<pre>
 grep 'def hook_' -r /path/to/rangers/source
</pre>
<p> Also try: </p>
<pre>
 pydoc ranger.api
</pre>
<p> Note that you should <font SIZE="-1">NOT</font> simply overwrite a function unless you know what you&#8217;re doing. Instead, save the existing function and call it from your new one. This way, multiple plugins can use the same hook. There are several sample plugins in the <i>/usr/share/doc/ranger/examples/</i> directory, including a hello-world plugin that describes this procedure.</p>
<h2>KEY BINDINGS</h2>
<p> Key bindings are defined in the file <i></i>%rangerdir<i>/config/rc.conf</i>. Check this file for a list of all key bindings. You can copy it to your local configuration directory with the &#8211;copy-config=rc option. </p>
<p> Many key bindings take an additional numeric argument. Type <i>5j</i> to move down 5 lines, <i>2l</i> to open a file in mode 2, <i>10&lt;Space&gt;</i> to mark 10 files. </p>
<p> This list contains the most useful bindings:</p>
<h3><font SIZE="-1">MAIN BINDINGS</font></h3>
<dl>
<dt>h, j, k, l</p>
<dd> Move left, down, up or right</p>
<dt>^D or J, ^U or K</p>
<dd> Move a half page down, up</p>
<dt>H, L</p>
<dd> Move back and forward in the history</p>
<dt>gg</p>
<dd> Move to the top</p>
<dt>G</p>
<dd> Move to the bottom</p>
<dt>[, ]</p>
<dd> Move up and down in the parent directory.</p>
<dt>^R</p>
<dd> Reload everything</p>
<dt>F</p>
<dd> Toggle <i>freeze_files</i> setting. When active (indicated by a cyan <i></i><font SIZE="-1"><i>FROZEN</i></font><i></i> message in the status bar), directories and files will not be loaded, improving performance when all the files you need are already loaded. This does not affect file previews, which can be toggled with <i>zI</i>. Also try disabling the preview of directories with <i>zP</i>.</p>
<dt>^L</p>
<dd> Redraw the screen</p>
<dt>i</p>
<dd> Inspect the current file in a bigger window.</p>
<dt>E</p>
<dd> Edit the current file in <tt>$VISUAL</tt> otherwise <tt>$EDITOR</tt> otherwise &#8220;vim&#8221;</p>
<dt>S</p>
<dd> Open a shell in the current directory</p>
<dt>?</p>
<dd> Opens this man page</p>
<dt>W</p>
<dd> Opens the log window where you can review messages that pop up at the bottom.</p>
<dt>w</p>
<dd> Opens the task window where you can view and modify background processes that currently run in ranger. In there, you can type &#8220;dd&#8221; to abort a process and &#8220;J&#8221; or &#8220;K&#8221; to change the priority of a process. Only one process is run at a time.</p>
<dt>^C</p>
<dd> Stop the currently running background process that ranger has started, like copying files, loading directories or file previews.</p>
<dt>&lt;octal&gt;=, +&lt;who&gt;&lt;what&gt;, -&lt;who&gt;&lt;what&gt;</p>
<dd> Change the permissions of the selection. For example, <tt>&quot;777=&quot;</tt> is equivalent to <tt>&quot;chmod 777 %s&quot;</tt>, <tt>&quot;+ar&quot;</tt> does <tt>&quot;chmod a+r %s&quot;</tt>, <tt>&quot;-ow&quot;</tt> does <tt>&quot;chmod o-w %s&quot;</tt> etc.</p>
<dt>yy</p>
<dd> Copy (yank) the selection, like pressing Ctrl+C in modern <font SIZE="-1">GUI</font> programs. (You can also type &#8220;ya&#8221; to add files to the copy buffer, &#8220;yr&#8221; to remove files again, or &#8220;yt&#8221; for toggling.)</p>
<dt>dd</p>
<dd> Cut the selection, like pressing Ctrl+X in modern <font SIZE="-1">GUI</font> programs. (There are also &#8220;da&#8221;, &#8220;dr&#8221; and &#8220;dt&#8221; shortcuts equivalent to &#8220;ya&#8221;, &#8220;yr&#8221; and &#8220;yt&#8221;.)</p>
<dt>pp</p>
<dd> Paste the files which were previously copied or cut, like pressing Ctrl+V in modern <font SIZE="-1">GUI</font> programs. </p>
<p> Conflicts will be renamed by appending an &#8216;_&#8217; (and a counter if necessary), resulting in <tt>&quot;file.ext_&quot;</tt>, <tt>&quot;file.ext_0&quot;</tt>, etc. If you prefer <tt>&quot;file_.ext&quot;</tt> you can use the <tt>&quot;paste_ext&quot;</tt> command.</p>
<dt>po</p>
<dd> Paste the copied/cut files, overwriting existing files.</p>
<dt>pP, pO</p>
<dd> Like pp and po, but queues the operation so that it will be executed <i>after</i> any other operations. Reminder: type <tt>&quot;w&quot;</tt> to open the task window.</p>
<dt>pl, pL</p>
<dd> Create symlinks (absolute or relative) to the copied files</p>
<dt>phl</p>
<dd> Create hardlinks to the copied files</p>
<dt>pht</p>
<dd> Duplicate the subdirectory tree of the copied directory, then create hardlinks for each contained file into the new directory tree.</p>
<dt>m<i>X</i></p>
<dd> Create a bookmark with the name <i>X</i></p>
<dt>`<i>X</i></p>
<dd> Move to the bookmark with the name <i>X</i></p>
<dt>n</p>
<dd> Find the next file. By default, this gets you to the newest file in the directory, but if you search something using the keys /, cm, ct, &#8230;, it will get you to the next found entry.</p>
<dt>N</p>
<dd> Find the previous file.</p>
<dt>o<i>X</i></p>
<dd> Change the sort method (like in mutt)</p>
<dt>z<i>X</i></p>
<dd> Change settings. See the settings section for a list of settings and their hotkey.</p>
<dt>u<i>?</i></p>
<dd> Universal undo-key. Depending on the key that you press after &#8220;u&#8221;, it either restores closed tabs (uq), removes tags (ut), clears the copy/cut buffer (ud), starts the reversed visual mode (uV) or clears the selection (uv).</p>
<dt>f</p>
<dd> Quickly navigate by entering a part of the filename.</p>
<dt>Space</p>
<dd> Mark a file.</p>
<dt>v</p>
<dd> Toggle the mark-status of all files</p>
<dt>V</p>
<dd> Starts the visual mode, which selects all files between the starting point and the cursor until you press <font SIZE="-1">ESC.</font> To unselect files in the same way, use &#8220;uV&#8221;.</p>
<dt>/</p>
<dd> Search for files in the current directory.</p>
<dt>:</p>
<dd> Open the console.</p>
<dt>!</p>
<dd> Open the console with the content &#8220;shell &#8221; so you can quickly run commands</p>
<dt>@</p>
<dd> Open the console with the content &#8220;shell <tt>%s</tt>&#8221;, placing the cursor before the &#8220; <tt>%s</tt>&#8221; so you can quickly run commands with the current selection as the argument.</p>
<dt>r</p>
<dd> Open the console with the content &#8220;open with &#8221; so you can decide which program to use to open the current file selection.</p>
<dt>cd</p>
<dd> Open the console with the content &#8220;cd &#8221;</p>
<dt>^P</p>
<dd> Open the console with the most recent command.</p>
<dt>Alt-<i>N</i></p>
<dd> Open a tab. N has to be a number from 0 to 9. If the tab doesn&#8217;t exist yet, it will be created.</p>
<dt>Alt-l, Alt-r</p>
<dd> Shift a tab left, respectively right.</p>
<dt>gn, ^N</p>
<dd> Create a new tab.</p>
<dt>gt, gT</p>
<dd> Go to the next or previous tab. You can also use <font SIZE="-1">TAB</font> and <font SIZE="-1">SHIFT+TAB</font> instead.</p>
<dt>gc, ^W</p>
<dd> Close the current tab. The last tab cannot be closed this way.</p>
<dt>M</p>
<dd> A key chain that allows you to quickly change the line mode of all the files of the current directory. For a more permanent solution, use the command &#8220;default_linemode&#8221; in your rc.conf.</p>
<dt>.d</p>
<dd> Apply the typefilter &#8220;directory&#8221;.</p>
<dt>.f</p>
<dd> Apply the typefilter &#8220;file&#8221;.</p>
<dt>.l</p>
<dd> Apply the typefilter &#8220;symlink&#8221;.</p>
<dt>.m</p>
<dd> Apply a new mimetype filter.</p>
<dt>.n</p>
<dd> Apply a new filename filter.</p>
<dt>.#</p>
<dd> Apply a new hash filter.</p>
<dt>.&quot;</p>
<dd> Apply a new duplicate filter.</p>
<dt>.&#8217;</p>
<dd> Apply a new unique filter.</p>
<dt>.|</p>
<dd> Combine the two topmost filters from the filter stack in the <tt>&quot;OR&quot;</tt> relationship, instead of the <tt>&quot;AND&quot;</tt> used implicitly.</p>
<dt>.&amp;</p>
<dd> Explicitly combine the two topmost filters in the <tt>&quot;AND&quot;</tt> relationship. Usually not needed because filters are implicitly in this relationship though might be useful in more complicated scenarios.</p>
<dt>.!</p>
<dd> Negate the topmost filter.</p>
<dt>.r</p>
<dd> Rotate the filter stack by N elements. Where N is provided as a numeric prefix like vim&#8217;s <i>count</i> and defaults to 1, i.e. move the topmost element to the bottom of the stack.</p>
<dt>.c</p>
<dd> Clear the filter stack.</p>
<dt>.*</p>
<dd> Decompose the topmost filter combinator (e.g. <tt>&quot;.!&quot;</tt>, <tt>&quot;.|&quot;</tt>).</p>
<dt>.p</p>
<dd> Pop the topmost filter from the filter stack.</p>
<dt>..</p>
<dd> Show the current filter stack state.</dl>
<h3>READLINE-LIKE <font SIZE="-1">BINDINGS IN THE CONSOLE</font></h3>
<dl>
<dt>^B, ^F</p>
<dd> Move left and right (B for back, F for forward)</p>
<dt>^P, ^N</p>
<dd> Move up and down (P for previous, N for Next)</p>
<dt>^A, ^E</p>
<dd> Move to the start or to the end</p>
<dt>Alt-B, Alt-LEFT</p>
<dd> Move backwards by words.</p>
<dt>Alt-F, Alt-RIGHT</p>
<dd> Move forwards by words.</p>
<dt>^D</p>
<dd> Delete the current character.</p>
<dt>^H</p>
<dd> Backspace.</dl>
<h2>MOUSE BUTTONS</h2>
<dl>
<dt>Left Mouse Button</p>
<dd> Click on something and you&#8217;ll move there. To run a file, &#8220;enter&#8221; it, like a directory, by clicking on the preview.</p>
<dt>Right Mouse Button</p>
<dd> Enter a directory or run a file.</p>
<dt>Scroll Wheel</p>
<dd> Scrolls up or down. You can point at the column of the parent directory while scrolling to switch directories.</dl>
<h2>SETTINGS</h2>
<p> This section lists all built-in settings of ranger. The valid types for the value are in [brackets]. The hotkey to toggle the setting is in &lt;brakets&gt;, if a hotkey exists. </p>
<p> Settings can be changed in the file <i>~/.config/ranger/rc.conf</i> or on the fly with the command <code>:set option value</code>. Examples: </p>
<pre>
 set column_ratios 1,2,3
 set show_hidden true
</pre>
<p> Toggling options can be done with: </p>
<pre>
 set show_hidden!
</pre>
<p> The different types of settings and an example for each type: </p>
<pre><code>
setting type | example values-- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -- --bool | true, false integer | 1, 23, 1337 string | foo, hello world list | 1, 2, 3, 4 none | none
</code></pre>
<p> You can view a list of all settings and their current values by pressing &#8220;3?&#8221; in ranger.</p>
<dl>
<dt>automatically_count_files [bool]</p>
<dd> Should ranger count and display the number of files in each directory as soon as it&#8217;s visible? This gets slow with remote file systems. Turning it off will still allow you to see the number of files after entering the directory.</p>
<dt>autosave_bookmarks [bool]</p>
<dd> Save bookmarks (used with mX and `X) instantly? This helps to synchronize bookmarks between multiple ranger instances but leads to *slight* performance loss. When false, bookmarks are saved when ranger is exited.</p>
<dt>autoupdate_cumulative_size [bool]</p>
<dd> You can display the &#8220;real&#8221; cumulative size of directories by using the command :get_cumulative_size or typing &#8220;dc&#8221;. The size is expensive to calculate and will not be updated automatically. You can choose to update it automatically though by turning on this option.</p>
<dt>cd_bookmarks [bool]</p>
<dd> Specify whether bookmarks should be included in the tab completion of the &#8220;cd&#8221; command.</p>
<dt>cd_tab_case [string]</p>
<dd> Changes case sensitivity for the &#8220;cd&#8221; command tab completion. Possible values are: </p>
<pre>
 sensitive
 insensitive
 smart
</pre>
<dt>cd_tab_fuzzy [bool]</p>
<dd> Use fuzzy tab completion with the &#8220;cd&#8221; command. For example, <code>:cd /u/lo/b&lt;</code><font SIZE="-1"><code>TAB</code></font><code>&gt;</code> expands to <code>:cd /usr/local/bin</code>.</p>
<dt>clear_filters_on_dir_change [bool]</p>
<dd> If set to &#8216;true&#8217;, persistent filters would be cleared upon leaving the directory</p>
<dt>collapse_preview [bool] &lt;zc&gt;</p>
<dd> When no preview is visible, should the last column be squeezed to make use of the whitespace?</p>
<dt>colorscheme [string]</p>
<dd> Which colorscheme to use? These colorschemes are available by default: <code>default</code>, <code>jungle</code>, <code>snow</code>. Snow is a monochrome scheme, jungle replaces blue directories with green ones for better visibility on certain terminals.</p>
<dt>column_ratios [list]</p>
<dd> How many columns are there, and what are their relative widths? For example, a value of 1,1,1 would mean 3 evenly sized columns. 1,1,1,1,4 means 5 columns with the preview column being as large as the other columns combined.</p>
<dt>confirm_on_delete [string]</p>
<dd> Ask for a confirmation when running the &#8220;delete&#8221; command? Valid values are &#8220;always&#8221; (default), &#8220;never&#8221;, &#8220;multiple&#8221;. With &#8220;multiple&#8221;, ranger will ask only if you delete multiple files at once.</p>
<dt>dirname_in_tabs [bool]</p>
<dd> Display the directory name in tabs?</p>
<dt>display_size_in_main_column [bool]</p>
<dd> Display the file size in the main column?</p>
<dt>display_size_in_status_bar [bool]</p>
<dd> Display the file size in the status bar?</p>
<dt>display_free_space_in_status_bar [bool]</p>
<dd> Display the free disk space in the status bar?</p>
<dt>display_tags_in_all_columns [bool]</p>
<dd> Display tags in all columns?</p>
<dt>draw_borders [string]</p>
<dd> Draw borders around or between the columns? Possible values are: </p>
<pre>
 none           no borders of any sort
 outline        draw an outline around all the columns
 separators     draw only vertical lines between columns
 both           both of the above
</pre>
<dt>draw_progress_bar_in_status_bar [bool]</p>
<dd> Draw a progress bar in the status bar which displays the average state of all currently running tasks which support progress bars?</p>
<dt>flushinput [bool] &lt;zi&gt;</p>
<dd> Flush the input after each key hit? One advantage is that when scrolling down with &#8220;j&#8221;, ranger stops scrolling instantly when you release the key. One disadvantage is that when you type commands blindly, some keys might get lost.</p>
<dt>freeze_files [bool] &lt;F&gt;</p>
<dd> When active, directories and files will not be loaded, improving performance when all the files you need are already loaded. This does not affect file previews.</p>
<dt>global_inode_type_filter [string]</p>
<dd> Like filter_inode_type, but globally for all directories. Useful in combination with <code>&#8211;choosedir</code>: </p>
<pre>
 ranger --choosedir=/tmp/x --cmd='set global_inode_type_filter d'
</pre>
<dt>hidden_filter [string]</p>
<dd> A regular expression pattern for files which should be hidden. For example, this pattern will hide all files that start with a dot or end with a tilde. </p>
<pre>
 set hidden_filter ^\.|~$
</pre>
<dt>hint_collapse_threshold [int]</p>
<dd> The key hint lists up to this size have their sublists expanded. Otherwise the submaps are replaced with &#8220;&#8230;&#8221;.</p>
<dt>hostname_in_titlebar [bool]</p>
<dd> Show hostname in titlebar?</p>
<dt>size_in_bytes [bool]</p>
<dd> Print file sizes in bytes instead of the default human-readable format.</p>
<dt>idle_delay [integer]</p>
<dd> The delay that ranger idly waits for user input, in milliseconds, with a resolution of 100ms. Lower delay reduces lag between directory updates but increases <font SIZE="-1">CPU</font> load.</p>
<dt>iterm2_font_height [integer]</p>
<dd> Change the assumed font height in iTerm2, which may help with iTerm image previews</p>
<dt>iterm2_font_width [integer]</p>
<dd> Change the assumed font width in iTerm2, which may help with iTerm image previews</p>
<dt>line_numbers [string]</p>
<dd> Show line numbers in main column. Possible values are: </p>
<pre>
 false      turn the feature off
 absolute   absolute line numbers for use with &quot;&lt;N&gt;gg&quot;
 relative   relative line numbers for &quot;&lt;N&gt;k&quot; or &quot;&lt;N&gt;j&quot;
</pre>
<dt>max_console_history_size [integer, none]</p>
<dd> How many console commands should be kept in history? &#8220;none&#8221; will disable the limit.</p>
<dt>max_history_size [integer, none]</p>
<dd> How many directory changes should be kept in history?</p>
<dt>metadata_deep_search [bool]</p>
<dd> When the metadata manager module looks for metadata, should it only look for a &#8220;.metadata.json&#8221; file in the current directory, or do a deep search and check all directories above the current one as well?</p>
<dt>mouse_enabled [bool] &lt;zm&gt;</p>
<dd> Enable mouse input?</p>
<dt>nested_ranger_warning [string]</p>
<dd> Warn at startup if <tt>&quot;RANGER_LEVEL&quot;</tt> is greater than 0, in other words give a warning when you nest ranger in a subshell started by ranger. Allowed values are <tt>&quot;true&quot;</tt>, <tt>&quot;false&quot;</tt> and <tt>&quot;error&quot;</tt>. The special value <tt>&quot;error&quot;</tt> promotes the warning to an error, this is usually shown as red text but will crash ranger when run with the <tt>&quot;--debug&quot;</tt> flag.</p>
<dt>one_indexed [bool]</p>
<dd> Start line numbers from 1. Possible values are: </p>
<pre>
 false      start line numbers from 0
 true       start line numbers from 1
</pre>
<dt>open_all_images [bool]</p>
<dd> Open all images in this directory when running certain image viewers like feh or sxiv? You can still open selected files by marking them. </p>
<p> If there would be too many files for the system to handle, this option will be temporarily disabled automatically.</p>
<dt>padding_right [bool]</p>
<dd> When collapse_preview is on and there is no preview, should there remain a little padding on the right? This allows you to click into that space to run the file.</p>
<dt>preview_directories [bool] &lt;zP&gt;</p>
<dd> Preview directories in the preview column?</p>
<dt>preview_files [bool] &lt;zp&gt;</p>
<dd> Preview files in the preview column?</p>
<dt>preview_images [bool]</p>
<dd> Draw images inside the console with the external program w3mimgpreview?</p>
<dt>preview_images_method [string]</p>
<dd> Set the preview image method. Supported methods: w3m, iterm2, urxvt, urxvt-full, terminology. See <i></i><font SIZE="-1"><i>PREVIEWS</i></font><i></i> section.</p>
<dt>preview_max_size [int]</p>
<dd> Avoid previewing files that exceed a certain size, in bytes. Use a value of 0 to disable this feature.</p>
<dt>preview_script [string, none]</p>
<dd> Which script should handle generating previews? If the file doesn&#8217;t exist, or use_preview_script is off, ranger will handle previews itself by just printing the content.</p>
<dt>relative_current_zero [bool]</p>
<dd> When line_numbers is set to relative, show 0 on the current line if true or show the absolute number of the current line when false.</p>
<dt>save_backtick_bookmark [bool]</p>
<dd> Save the <tt>&quot;`&quot;</tt> bookmark to disk. This bookmark is used to switch to the last directory by typing <tt>&quot;``&quot;</tt>.</p>
<dt>save_console_history [bool]</p>
<dd> Should the console history be saved on exit? If disabled, the console history is reset when you restart ranger.</p>
<dt>save_tabs_on_exit [bool]</p>
<dd> Save all tabs, except the active, on exit? The last saved tabs are restored once when starting the next session. Multiple sessions are stored in a stack and the oldest saved tabs are restored first.</p>
<dt>scroll_offset [integer]</p>
<dd> Try to keep this much space between the top/bottom border when scrolling.</p>
<dt>shorten_title [integer]</p>
<dd> Trim the title of the window if it gets long? The number defines how many directories are displayed at once. A value of 0 turns off this feature.</p>
<dt>show_cursor [bool]</p>
<dd> Always show the terminal cursor?</p>
<dt>show_hidden_bookmarks [bool]</p>
<dd> Show dotfiles in the bookmark preview window? (Type &#8216;)</p>
<dt>show_hidden [bool] &lt;zh&gt;, &lt;^H&gt;</p>
<dd> Show hidden files?</p>
<dt>show_selection_in_titlebar [bool]</p>
<dd> Add the highlighted file to the path in the titlebar</p>
<dt>sort_case_insensitive [bool] &lt;zc&gt;</p>
<dd> Sort case-insensitively? If true, &#8220;a&#8221; will be listed before &#8220;B&#8221; even though its <font SIZE="-1">ASCII</font> value is higher.</p>
<dt>sort_directories_first [bool] &lt;zd&gt;</p>
<dd> Sort directories first?</p>
<dt>sort_reverse [bool] &lt;or&gt;</p>
<dd> Reverse the order of files?</p>
<dt>sort_unicode [bool]</p>
<dd> When sorting according to some string, should the unicode characters be compared, instead of looking at the raw character values to save time?</p>
<dt>sort [string] &lt;oa&gt;, &lt;ob&gt;, &lt;oc&gt;, &lt;oe&gt;, &lt;om&gt;, &lt;on&gt;, &lt;ot&gt;, &lt;os&gt;, &lt;oz&gt;</p>
<dd> Which sorting mechanism should be used? Choose one of <code>atime</code>, <code>basename</code>, <code>ctime</code>, <code>extension</code>, <code>mtime</code>, <code>natural</code>, <code>type</code>, <code>size</code>, <code>random</code> </p>
<p> Note: You can reverse the order by typing an uppercase second letter in the key combination, e.g. &#8220;oN&#8221; to sort from Z to A.</p>
<dt>status_bar_on_top [bool]</p>
<dd> Put the status bar at the top of the window?</p>
<dt>tilde_in_titlebar [bool]</p>
<dd> Abbreviate <tt>$HOME</tt> with ~ in the titlebar (first line) of ranger?</p>
<dt>unicode_ellipsis [bool]</p>
<dd> Use a unicode &#8220;&#8230;&#8221; character instead of &#8220;~&#8221; to mark cut-off filenames?</p>
<dt>bidi_support [bool]</p>
<dd> Try to properly display file names in <font SIZE="-1">RTL</font> languages (Hebrew, Arabic) by using a <font SIZE="-1">BIDI</font> algorithm to reverse the relevant parts of the text. Requires the python-bidi pip package.</p>
<dt>update_title [bool]</p>
<dd> Set a window title? Updates both the <i></i><font SIZE="-1"><i>WM_NAME</i></font><i></i> and <i></i><font SIZE="-1"><i>WM_ICON_NAME</i></font><i></i> properties.</p>
<dt>update_tmux_title [bool]</p>
<dd> Set the tmux/screen <i>window-name</i> to &#8220;ranger&#8221;?</p>
<dt>use_preview_script [bool] &lt;zv&gt;</p>
<dd> Use the preview script defined in the setting <i>preview_script</i>?</p>
<dt>vcs_aware [bool]</p>
<dd> Gather and display data about version control systems. Supported vcs: git, hg.</p>
<dt>vcs_backend_git, vcs_backend_hg, vcs_backend_bzr, vcs_backend_svn [string]</p>
<dd> Sets the state for the version control backend. The possible values are: </p>
<pre>
 disabled   Don't display any information.
 local      Display only local state.
 enabled    Display both, local and remote state.
            May be slow for hg and bzr.
</pre>
<dt>vcs_msg_length [int]</p>
<dd> Length to truncate first line of the commit messages to when shown in the statusbar. Defaults to 50.</p>
<dt>viewmode [string]</p>
<dd> Sets the view mode, which can be <code>miller</code> to display the files in the traditional miller column view that shows multiple levels of the hierarchy, or <code>multipane</code> to use multiple panes (one per tab) similar to midnight-commander.</p>
<dt>w3m_delay [float]</p>
<dd> Delay in seconds before displaying an image with the w3m method. Increase it in case of experiencing display corruption.</p>
<dt>w3m_offset [int]</p>
<dd> Offset in pixels for the inner border of the terminal. Some terminals require the offset to be specified explicitly, among others st and UXterm, some don&#8217;t like urxvt.</p>
<dt>wrap_plaintext_previews [bool]</p>
<dd> Whether or not to wrap long lines in the pager, this includes previews of plain text files.</p>
<dt>wrap_scroll [bool]</p>
<dd> Enable scroll wrapping &#8211; moving down while on the last item will wrap around to the top and vice versa.</p>
<dt>xterm_alt_key [bool]</p>
<dd> Enable this if key combinations with the Alt Key don&#8217;t work for you. (Especially on xterm)</dl>
<h2>COMMANDS</h2>
<p> You can enter the commands in the console which is opened by pressing &#8220;:&#8221;. </p>
<p> You can always get a list of the currently existing commands by typing &#8220;?c&#8221; in ranger. For your convenience, this is a list of the &#8220;public&#8221; commands including their parameters, excluding descriptions: </p>
<p>alias[newcommand][oldcommand] bulkrename<br />
    cd[path] chain command1[; command2[; command3&#8230;]] chmod octal_number<br />
        cmap key command<br />
            console[-pSTARTPOSITION] command<br />
                copycmap key newkey[newkey2&#8230;] copymap key newkey[newkey2&#8230;] copypmap key newkey[newkey2&#8230;] copytmap key newkey[newkey2&#8230;] cunmap keys&#8230; default_linemode[path = regexp | tag = tags] linemodename delete echo[text] edit[filename] eval[-q] python_code<br />
                    filter[string] filter_inode_type[dfl] find pattern<br />
                        flat level<br />
                            grep pattern<br />
                                help<br />
                                    jump_non[-FLAGS&#8230;] linemode linemodename<br />
                                        load_copy_buffer<br />
                                            map key command<br />
                                                mark pattern<br />
                                                    mark_tag[tags] meta key value<br />
                                                        mkdir dirname<br />
                                                            open_with[application][flags][mode] pmap key command<br />
                                                                prompt_metadata[key1[key2[&#8230;]]] punmap keys&#8230; quit<br />
                                                                    quit !quitall<br />
                                                                        quitall !relink newpath<br />
                                                                            rename_append[-FLAGS&#8230;] rename newname<br />
                                                                                save_copy_buffer<br />
                                                                                    scout[-FLAGS&#8230;] pattern<br />
                                                                                        search pattern<br />
                                                                                            search_inc pattern<br />
                                                                                                set option value<br />
                                                                                                    setintag tags option value<br />
                                                                                                        setlocal[path = &lt;path&gt;] option value<br />
                                                                                                            shell[-FLAGS&#8230;] command<br />
                                                                                                                source filename<br />
                                                                                                                    terminal<br />
                                                                                                                        tmap key command<br />
                                                                                                                            touch filename<br />
                                                                                                                                trash<br />
                                                                                                                                    travel pattern<br />
                                                                                                                                        tunmap keys&#8230; unmap keys&#8230; unmark pattern<br />
                                                                                                                                            unmark_tag[tags]</p>
<p> There are additional commands which are directly translated to python functions, one for every method in the ranger.core.actions.Actions class. They are not documented here, since they are mostly for key bindings, not to be typed in by a user. Read the source if you are interested in them. </p>
<p> These are the public commands including their descriptions:</p>
<dl>
<dt>alias [<i>newcommand</i>] [<i>oldcommand</i>]</p>
<dd> Copies the oldcommand as newcommand.</p>
<dt>bulkrename</p>
<dd> This command opens a list of selected files in an external editor. After you edit and save the file, it will generate a shell script which does bulk renaming according to the changes you did in the file. </p>
<p> This shell script is opened in an editor for you to review. After you close it, it will be executed.</p>
<dt>cd [<i>path</i>]</p>
<dd> The cd command changes the directory. If path is a file, selects that file. The command <tt>&quot;:cd -&quot;</tt> is equivalent to typing &#8220;.</p>
<dt>chain <i>command1</i>[; <i>command2</i>[; <i>command3</i>&#8230;]]</p>
<dd> Combines multiple commands into one, separated by semicolons.</p>
<dt>chmod <i>octal_number</i></p>
<dd> Sets the permissions of the selection to the octal number. </p>
<p> The octal number is between 000 and 777. The digits specify the permissions for the user, the group and others. A 1 permits execution, a 2 permits writing, a 4 permits reading. Add those numbers to combine them. So a 7 permits everything. </p>
<p> Key bindings in the form of [-+]&lt;who&gt;&lt;what&gt; and &lt;octal&gt;= also exist. For example, <code>+ar</code> allows reading for everyone, -ow forbids others to write and 777= allows everything. </p>
<p> See also: man 1 chmod</p>
<dt>console [-p<i>N</i>] <i>command</i></p>
<dd> Opens the console with the command already typed in. The cursor is placed at <i>N</i>.</p>
<dt>copymap <i>key</i> <i>newkey</i> [<i>newkey2</i> &#8230;]</p>
<dd>
<dt>copycmap <i>key</i> <i>newkey</i> [<i>newkey2</i> &#8230;]</p>
<dd>
<dt>copypmap <i>key</i> <i>newkey</i> [<i>newkey2</i> &#8230;]</p>
<dd>
<dt>copytmap <i>key</i> <i>newkey</i> [<i>newkey2</i> &#8230;]</p>
<dd> Copies the keybinding <i>key</i> to <i>newkey</i> in the &#8220;browser&#8221; context. This is a deep copy, so if you change the new binding (or parts of it) later, the old one is not modified. For example, <i>copymap j down</i> will make the key sequence &#8220;down&#8221; move the cursor down one item. </p>
<p> To copy key bindings of the console, pager or taskview use &#8220;copycmap&#8221;, &#8220;copypmap&#8221; or &#8220;copytmap&#8221; respectively.</p>
<dt>default_linemode [<i>path=regexp</i> | <i>tag=tags</i>] <i>linemodename</i></p>
<dd> Sets the default linemode. See <i>linemode</i> command. </p>
<p> Examples: </p>
<p> Set the global default linemode to &#8220;permissions&#8221;:<br />
&nbsp;:default_linemode permissions </p>
<p> Set the default linemode to &#8220;permissions&#8221; for all files tagged with &#8220;p&#8221; or &#8220;P&#8221;:<br />
&nbsp;:default_linemode tag=pP permissions </p>
<p> Set the default linemode for all files in ~/books/ to &#8220;metatitle&#8221;:<br />
&nbsp;:default_linemode path=/home/.*?/books/.*&nbsp;metatitle</p>
<dt>delete</p>
<dd> Destroy all files in the selection with a roundhouse kick. ranger will ask for a confirmation if you attempt to delete multiple (marked) files or non-empty directories. This can be changed by modifying the setting &#8220;confirm_on_delete&#8221;.</p>
<dt>echo <i>text</i></p>
<dd> Display the text in the statusbar.</p>
<dt>edit [<i>filename</i>]</p>
<dd> Edit the current file or the file in the argument.</p>
<dt>eval [<i>-q</i>] <i>python_code</i></p>
<dd> Evaluates the python code. `fm&#8217; is a reference to the <font SIZE="-1">FM</font> instance. To display text, use the function `p&#8217;. The result is displayed on the screen unless you use the &#8220;-q&#8221; option. </p>
<p> Examples:<br />
&nbsp;:eval fm<br />
&nbsp;:eval len(fm.tabs)<br />
&nbsp;:eval p(&#8220;Hello World!&#8221;)</p>
<dt>filter [<i>string</i>]</p>
<dd> Displays only the files which contain the <i>string</i> in their basename. Running this command without any parameter will reset the filter. </p>
<p> This command is based on the <i>scout</i> command and supports all of its options.</p>
<dt>filter_inode_type [dfl]</p>
<dd> Displays only the files of specified inode type. To display only directories, use the &#8216;d&#8217; parameter. To display only files, use the &#8216;f&#8217; parameter. To display only links, use the &#8216;l&#8217; parameter. Parameters can be combined. To remove this filter, use no parameter.</p>
<dt>filter_stack [<i>command</i> [<i>args</i>]]</p>
<dd> Manage the filter stack, adding, removing and manipulating filters. For example, to show only duplicate files and symlinks: </p>
<pre>
  :filter_stack add type f
  :filter_stack add duplicate
  :filter_stack add and
  :filter_stack add type l
  :filter_stack add or
</pre>
<p> Or using the mapped keys: </p>
<pre>
  .f .&quot; .&amp; .l .|
</pre>
<p> Available subcommands:</p>
<dl>
<dt>
<dd>
<dl>
<dt>add <font SIZE="-1">FILTER_TYPE</font> [<font SIZE="-1">ARGS&#8230;</font>]</p>
<dd> Add a new filter to the top of the filter stack. Each filter on the stack is applied in turn, resulting in an implicit logical <tt>&quot;AND&quot;</tt> relation. The following <tt>&quot;FILTER_TYPE&quot;</tt>s are available:</p>
<dl>
<dt>
<dd>
<dl>
<dt>duplicate</p>
<dd> Filter files so only files that have duplicates in the same directory are shown. Useful when cleaning up identical songs and memes that were saved using distinct file names.</p>
<dt>filename <font SIZE="-1">NAME</font></p>
<dd> Filter files that contain <font SIZE="-1">NAME</font> in the filename, regular expression syntax is allowed.</p>
<dt>hash <font SIZE="-1">PATH</font></p>
<dd> Filter files so only files with the same hash as <font SIZE="-1">PATH</font> are shown.</p>
<dt>mimetype <font SIZE="-1">TYPE</font></p>
<dd> Filter files of a certain <font SIZE="-1">MIME</font> type, regular expression syntax is allowed.</p>
<dt>typefilter [d|f|l]</p>
<dd> Filter files of a certain type, <tt>&quot;d&quot;</tt> for directories, <tt>&quot;f&quot;</tt> for files and <tt>&quot;l&quot;</tt> for symlinks.</p>
<dt>unique</p>
<dd> Filter files so only unique files and the oldest file of every set of duplicates is shown.</p>
<dt>and</p>
<dd> Explicitly combine the two topmost filters in the &#8220;<font SIZE="-1">AND&#8221;</font> relationship. Usually not needed because filters are implicitly in this relationship though might be useful in more complicated scenarios.</p>
<dt>not</p>
<dd> Negate the topmost filter.</p>
<dt>or</p>
<dd> Combine the two topmost filters from the filter stack in the &#8220;<font SIZE="-1">OR&#8221;</font> relationship, instead of the &#8220;<font SIZE="-1">AND&#8221;</font> used implicitly.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>pop</p>
<dd> Pop the topmost filter from the filter stack.</p>
<dt>decompose</p>
<dd> Decompose the topmost filter combinator (e.g. <tt>&quot;.!&quot;</tt>, <tt>&quot;.|&quot;</tt>).</p>
<dt>rotate [N=1]</p>
<dd> Rotate the filter stack by N elements. Where N is passed as argument or as a numeric prefix like vim&#8217;s <i>count</i>, default to 1, i.e. move the topmost element to the bottom of the stack.</p>
<dt>clear</p>
<dd> Clear the filter stack.</p>
<dt>show</p>
<dd> Show the current filter stack state.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>find <i>pattern</i></p>
<dd> Search files in the current directory that contain the given (case-insensitive) string in their name as you type. Once there is an unambiguous result, it will be run immediately. (Or entered, if it&#8217;s a directory.) </p>
<p> This command is based on the <i>scout</i> command and supports all of its options.</p>
<dt>flat level</p>
<dd> Flattens the directory view up to the specified level. Level -1 means infinite level. Level 0 means standard view without flattened directory view. Level values -2 and less are invalid.</p>
<dt>grep <i>pattern</i></p>
<dd> Looks for a string in all marked files or directories.</p>
<dt>help</p>
<dd> Provides a quick way to view ranger documentations.</p>
<dt>jump_non [-<i>flags</i>&#8230;]</p>
<dd> Jumps to first non-directory if highlighted file is a directory and vice versa. </p>
<p> Flags:<br />
&nbsp;-r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Jump in reverse order<br />
&nbsp;-w&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Wrap around if reaching end of filelist</p>
<dt>linemode <i>linemodename</i></p>
<dd> Sets the linemode of all files in the current directory. The linemode may be: </p>
<pre>
 &quot;filename&quot;:
   display each line as &quot;&lt;basename&gt;...&lt;size&gt;&quot;
 &quot;fileinfo&quot;:
   display each line as &quot;&lt;basename&gt;...&lt;<a href="//www.systutorials.com/docs/linux/man/1-file/">file</a>(1) output&gt;&quot;
 &quot;mtime&quot;:
   display each line as &quot;&lt;basename&gt;...&lt;mtime&gt;&quot; in ISO format
 &quot;humanreadablemtime&quot;:
   display each line as &quot;&lt;basename&gt;...&lt;mtime&gt;&quot; in a human readable
   format, more precise the more recent.
 &quot;sizemtime&quot;:
   display each line as &quot;&lt;basename&gt;...&lt;size&gt; &lt;mtime&gt;&quot; in ISO format
 &quot;humanreadablesizemtime&quot;:
   display each line as &quot;&lt;basename&gt;...&lt;size&gt; &lt;mtime&gt;&quot; in a human
   readable format, more precise the more recent.
 &quot;permissions&quot;:
   display each line as &quot;&lt;permissions&gt; &lt;owner&gt; &lt;group&gt; &lt;basename&gt;&quot;
 &quot;metatitle&quot;:
   display metadata from .metadata.json files if available, fall back
   to the &quot;filename&quot; linemode if no metadata was found.
   See :meta command.
</pre>
<p> The custom linemodes may be added by subclassing the <i>LinemodeBase</i> class. See the <i>ranger.core.linemode</i> module for some examples.</p>
<dt>load_copy_buffer</p>
<dd> Load the copy buffer from <i>~/.config/ranger/copy_buffer</i>. This can be used to pass the list of copied files to another ranger instance.</p>
<dt>map <i>key</i> <i>command</i></p>
<dd>
<dt>cmap <i>key</i> <i>command</i></p>
<dd>
<dt>pmap <i>key</i> <i>command</i></p>
<dd>
<dt>tmap <i>key</i> <i>command</i></p>
<dd> Assign the key combination to the given command. Whenever you type the key/keys, the command will be executed. Additionally, if you use a quantifier when typing the key, like 5j, it will be passed to the command as the attribute &#8220;self.quantifier&#8221;. </p>
<p> The keys you bind with this command are accessible in the file browser only, not in the console, pager or taskview. To bind keys there, use the commands &#8220;cmap&#8221;, &#8220;pmap&#8221; or &#8220;tmap&#8221;.</p>
<dt>mark <i>pattern</i></p>
<dd> Mark all files matching the regular expression pattern. </p>
<p> This command is based on the <i>scout</i> command and supports all of its options.</p>
<dt>mark_tag [<i>tags</i>]</p>
<dd> Mark all tags that are tagged with either of the given tags. When leaving out the tag argument, all tagged files are marked.</p>
<dt>meta <i>key</i> <i>value</i></p>
<dd> Set the metadata of the currently highlighted file. Example: </p>
<pre>
 :meta title The Hitchhiker's Guide to the Galaxy
 :meta year 1979
</pre>
<p> This metadata can be displayed by, for example, using the &#8220;metatitle&#8221; line mode by typing Mt.</p>
<dt>mkdir <i>dirname</i></p>
<dd> Creates a directory with the name <i>dirname</i>.</p>
<dt>open_with [<i>application</i>] [<i>flags</i>] [<i>mode</i>]</p>
<dd> Open the selected files with the given application, unless it is omitted, in which case the default application is used. <i>flags</i> change the way the application is executed and are described in their own section in this man page. The <i>mode</i> is a number that specifies which application to use. The list of applications is generated by the external file opener &#8220;rifle&#8221; and can be displayed when pressing &#8220;r&#8221; in ranger. </p>
<p> Note that if you specify an application, the mode is ignored.</p>
<dt>prompt_metadata [<i>keys &#8230;</i>]</p>
<dd> Prompt the user to input metadata with the <tt>&quot;meta&quot;</tt> command for multiple keys in a row.</p>
<dt>quit</p>
<dd> Closes the current tab, if there&#8217;s only one tab. Otherwise quits if there are no tasks in progress. The current directory will be bookmarked as &#8216; so you can re-enter it by typing &#8220; or &#8221; the next time you start ranger.</p>
<dt>quit!</p>
<dd> Like <tt>&quot;quit&quot;</tt>, except will force quit even if tasks are in progress.</p>
<dt>quitall</p>
<dd> Like <tt>&quot;quit&quot;</tt>, except will quit even if multiple tabs are open.</p>
<dt>quitall!</p>
<dd> Like <tt>&quot;quitall&quot;</tt>, except will force quit even if tasks are in progress.</p>
<dt>relink <i>newpath</i></p>
<dd> Change the link destination of the current symlink file to &lt;newpath&gt;. First &lt;tab&gt; will load the original link.</p>
<dt>rename <i>newname</i></p>
<dd> Rename the current file. If a file with that name already exists, the renaming will fail. Also try the key binding A for appending something to a file name.</p>
<dt>rename_append [-<i>flags</i>&#8230;]</p>
<dd> Opens the console with &#8220;:rename &lt;current file&gt;&#8221; with the cursor positioned before the file extension. </p>
<p> Flags:<br />
&nbsp;-a&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Position before all extensions<br />
&nbsp;-r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Remove everything before extensions</p>
<dt>save_copy_buffer</p>
<dd> Save the copy buffer to <i>~/.config/ranger/copy_buffer</i>. This can be used to pass the list of copied files to another ranger instance.</p>
<dt>scout [-<i>flags</i>&#8230;] [&#8211;] <i>pattern</i></p>
<dd> Swiss army knife command for searching, traveling and filtering files. </p>
<p> Flags:<br />
&nbsp;-a&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Automatically open a file on unambiguous match<br />
&nbsp;-e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Open the selected file when pressing enter<br />
&nbsp;-f&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Filter files that match the current search pattern<br />
&nbsp;-g&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Interpret pattern as a glob pattern<br />
&nbsp;-i&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Ignore the letter case of the files<br />
&nbsp;-k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Keep the console open when changing a directory with the command<br />
&nbsp;-l&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Letter skipping;&nbsp;e.g. allow&nbsp;&#8220;rdme&#8221;&nbsp;to match the file&nbsp;&#8220;readme&#8221;<br />
&nbsp;-m&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Mark the matching files after pressing enter<br />
&nbsp;-M&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Unmark the matching files after pressing enter<br />
&nbsp;-p&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Permanent filter: hide non-matching files after pressing enter<br />
&nbsp;-r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Interpret pattern as a regular expression pattern<br />
&nbsp;-s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Smart case;&nbsp;like -i unless pattern contains upper case letters<br />
&nbsp;-t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Apply filter and search pattern as you type<br />
&nbsp;-v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Inverts the match </p>
<p> Multiple flags can be combined. For example, &#8220;:scout -gpt&#8221; would create a :filter-like command using globbing.</p>
<dt>search <i>pattern</i></p>
<dd> Search files in the current directory that match the given (case insensitive) regular expression pattern. </p>
<p> This command is based on the <i>scout</i> command and supports all of its options.</p>
<dt>search_inc <i>pattern</i></p>
<dd> Search files in the current directory that match the given (case insensitive) regular expression pattern. This command gets you to matching files as you type. </p>
<p> This command is based on the <i>scout</i> command and supports all of its options.</p>
<dt>set <i>option</i> <i>value</i></p>
<dd> Assigns a new value to an option. Valid options are listed in the settings section. Use tab completion to get the current value of an option, though this doesn&#8217;t work for functions and regular expressions. Valid values are: </p>
<pre><code>
setting type | example values-- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -- --bool | true, false integer | 1, 23, 1337 string | foo, hello world list | 1, 2, 3, 4 none | none
</code></pre>
<dt>setintag <i>tags</i> <i>option</i> <i>value</i></p>
<dd> Assigns a new value to an option, but locally for the directories that are marked with <i>tag</i>. This means, that this option only takes effect when visiting that directory. </p>
<p> For example, to change the sorting order in your downloads directory, tag it with the <i>v</i> tag by typing <i>&quot;v</i>, then use this command: </p>
<pre>
 setintag v sort ctime
</pre>
<dt>setlocal [path=<i>path</i>] <i>option</i> <i>value</i></p>
<dd> Assigns a new value to an option, but locally for the directory given by <i>path</i>. This means, that this option only takes effect when visiting that directory. If no path is given, uses the current directory. </p>
<p> <i>path</i> is a regular expression. This means that <tt>&quot;path=~/dl&quot;</tt> applies to all paths that start with <i>~/dl</i>, e.g. <i>~/dl2</i> and <i>~/dl/foo</i>. To avoid this, use <tt>&quot;path=~/dl$&quot;</tt>. </p>
<p> <i>path</i> can be quoted with either single or double quotes to prevent unwanted splitting. <i>path=&#8217;~/dl dl$&#8217;</i> or <i>path=&#8220;~/dl dl$&#8221;</i></p>
<dt>shell [-<i>flags</i>] <i>command</i></p>
<dd> Run a shell command. <i>flags</i> are discussed in their own section.</p>
<dt>source <i>filename</i></p>
<dd> Reads commands from a file and executes them in the ranger console. </p>
<p> This can be used to re-evaluate the rc.conf file after changing it: </p>
<pre>
 map X chain shell vim -p %confdir/rc.conf %rangerdir/config/rc.conf; \
                   source %confdir/rc.conf
</pre>
<dt>scroll_preview <i>value</i></p>
<dd> Scroll the file preview by <i>value</i> lines.</p>
<dt>terminal</p>
<dd> Spawns the <i>x-terminal-emulator</i> starting in the current directory.</p>
<dt>touch <i>filename</i></p>
<dd> Creates an empty file with the name <i>filename</i>, unless it already exists.</p>
<dt>trash</p>
<dd> Move all files in the selection to the trash using rifle. Rifle tries to use a trash manager like <i>trash-cli</i> if available but will fall back to moving files to either <i></i>$XDG_DATA_HOME<i>/ranger-trash</i> or <i>~/.ranger/ranger-trash</i>. This is a less permanent version of <i>delete</i>, relying on the user to clear out the trash whenever it&#8217;s convenient. While having the possibility of restoring trashed files until this happens. ranger will ask for a confirmation if you attempt to trash multiple (marked) files or non-empty directories. This can be changed by modifying the setting &#8220;confirm_on_delete&#8221;.</p>
<dt>travel <i>pattern</i></p>
<dd> Filters the current directory for files containing the letters in the string, possibly with other letters in between. The filter is applied as you type. When only one directory is left, it is entered and the console is automatically reopened, allowing for fast travel. To close the console, press <font SIZE="-1">ESC</font> or execute a file. </p>
<p> This command is based on the <i>scout</i> command and supports all of its options.</p>
<dt>unmap [<i>keys</i> &#8230;]</p>
<dd>
<dt>cunmap [<i>keys</i> &#8230;]</p>
<dd>
<dt>punmap [<i>keys</i> &#8230;]</p>
<dd>
<dt>tunmap [<i>keys</i> &#8230;]</p>
<dd> Removes the given key mappings in the &#8220;browser&#8221; context. To unmap key bindings in the console, pager, or taskview use &#8220;cunmap&#8221;, &#8220;punmap&#8221; or &#8220;tunmap&#8221;.</p>
<dt>unmark <i>pattern</i></p>
<dd> Unmark all files matching a regular expression pattern. </p>
<p> This command is based on the <i>scout</i> command and supports all of its options.</p>
<dt>unmark_tag [<i>tags</i>]</p>
<dd> Unmark all tags that are tagged with either of the given tags. When leaving out the tag argument, all tagged files are unmarked.</dl>
<h2>FILES</h2>
<p> ranger reads several configuration files which are located in <i></i>$HOME<i>/.config/ranger</i> or <i></i>$XDG_CONFIG_HOME<i>/ranger</i> if <tt>$XDG_CONFIG_HOME</tt> is defined. You can use the &#8211;copy-config option to obtain the default configuration files. The files contain further documentation. </p>
<p> <i>rc.conf</i>, <i>commands.py</i> and <i>colorschemes</i> do not need to be copied fully as they will only be adding to the default configuration files except if explicitly overridden. This may lead to some confusing situations, for example when a key is being bound despite the corresponding line being removed from the user&#8217;s copy of the configuration file. This behavior may be disabled with an environment variable (see also: <font SIZE="-1"><code>ENVIRONMENT</code></font>). Note: All other configuration files only read from one source; i.e. default <font SIZE="-1">OR</font> user, not both. <i>rc.conf</i> and <i>commands.py</i> are additionally read from <i>/etc/ranger</i> if they exist for system-wide configuration, user configuration overrides system configuration which overrides the default configuration. </p>
<p> When starting ranger with the <code>&#8211;clean</code> option, it will not access or create any of these files.</p>
<h3><font SIZE="-1">CONFIGURATION</font></h3>
<dl>
<dt>rc.conf</p>
<dd> Contains a list of commands which are executed on startup. Mostly key bindings and settings are defined here.</p>
<dt>commands.py</p>
<dd> A python module that defines commands which can be used in ranger&#8217;s console by typing &#8220;:&#8221; or in the rc.conf file. Note that you can define commands in the same manner within plugins.</p>
<dt>commands_full.py</p>
<dd> This file is copied by &#8211;copy-config=commands_full and serves as a reference for custom commands. It is entirely ignored by ranger.</p>
<dt>rifle.conf</p>
<dd> This is the configuration file for the built-in file launcher called &#8220;rifle&#8221;.</p>
<dt>scope.sh</p>
<dd> This is a script that handles file previews. When the options <i>use_preview_script</i> and <i>preview_files</i> are set, the program specified in the option <i>preview_script</i> is run and its output and/or exit code determines rangers reaction.</p>
<dt>colorschemes/</p>
<dd> Colorschemes can be placed here.</p>
<dt>plugins/</p>
<dd> Plugins can be placed here.</dl>
<h3><font SIZE="-1">STORAGE</font></h3>
<dl>
<dt>bookmarks</p>
<dd> This file contains a list of bookmarks. The syntax is /^(.):(.*)$/. The first character is the bookmark key and the rest after the colon is the path to the file. In ranger, bookmarks can be set by typing m&lt;key&gt;, accessed by typing &#8216;&lt;key&gt; and deleted by typing um&lt;key&gt;.</p>
<dt>copy_buffer</p>
<dd> When running the command :save_copy_buffer, the paths of all currently copied files are saved in this file. You can later run :load_copy_buffer to copy the same files again, pass them to another ranger instance or process them in a script.</p>
<dt>history</p>
<dd> Contains a list of commands that have been previously typed in.</p>
<dt>tagged</p>
<dd> Contains a list of tagged files. The syntax is /^(.:)?(.*)$/ where the first letter is the optional name of the tag and the rest after the optional colon is the path to the file. In ranger, tags can be set by pressing t and removed with T. To assign a named tag, type &quot;&lt;tagname&gt;.</dl>
<h2>ENVIRONMENT</h2>
<p> These environment variables have an effect on ranger:</p>
<dl>
<dt><font SIZE="-1">RANGER_LEVEL</font></p>
<dd> ranger sets this environment variable to &#8220;1&#8221; or increments it if it already exists. External programs can determine whether they were spawned from ranger by checking for this variable.</p>
<dt><font SIZE="-1">RANGER_LOAD_DEFAULT_RC</font></p>
<dd> If this variable is set to <font SIZE="-1">FALSE,</font> ranger will not load the default rc.conf. This can save time if you copied the whole rc.conf to <i>~/.config/ranger/</i> and don&#8217;t need the default one at all.</p>
<dt><font SIZE="-1">VISUAL</font></p>
<dd> Defines the editor to be used for the &#8220;E&#8221; key. Falls back to <font SIZE="-1">EDITOR</font> if undefined or empty.</p>
<dt><font SIZE="-1">EDITOR</font></p>
<dd> Defines the editor to be used for the &#8220;E&#8221; key if <font SIZE="-1">VISUAL</font> is undefined or empty. Defaults to &#8220;vim&#8221;.</p>
<dt><font SIZE="-1">SHELL</font></p>
<dd> Defines the shell that ranger is going to use with the :shell command and the &#8220;S&#8221; key. Defaults to &#8220;/bin/sh&#8221;.</p>
<dt><font SIZE="-1">TERMCMD</font></p>
<dd> Defines the terminal emulator command that ranger is going to use with the :terminal command and the &#8220;t&#8221; run flag. Defaults to &#8220;xterm&#8221;.</p>
<dt><font SIZE="-1">BAT_STYLE</font></p>
<dd> Specifies the theme to be used for syntax highlighting when <i>bat</i> is installed, unless <i>highlight</i> is also installed. Find out possible values by running <tt>&quot;bat --list-themes&quot;</tt>.</p>
<dt><font SIZE="-1">PYGMENTIZE_STYLE</font></p>
<dd> Specifies the theme to be used for syntax highlighting when <i>pygmentize</i> is installed, unless <i>highlight</i> is also installed. Find out possible values by running:<br />
&nbsp;python -c&nbsp;&#8216;import pygments.styles;&nbsp;[print(stl)&nbsp;for stl in<br />
&nbsp;pygments.styles.<code>get_all_styles()</code>]&#8217;</p>
<dt><font SIZE="-1">HIGHLIGHT_STYLE</font></p>
<dd> Specifies the theme to be used for syntax highlighting when <i>highlight</i> is installed. Find out possible values by running <tt>&quot;highlight --list-themes&quot;</tt>.</p>
<dt><font SIZE="-1">HIGHLIGHT_TABWIDTH</font></p>
<dd> Specifies the number of spaces to use to replace tabs in <i>highlight</i>ed files.</p>
<dt><font SIZE="-1">HIGHLIGHT_OPTIONS</font></p>
<dd> <i>highlight</i> will pick up command line options specified in this variable. A <tt>&quot;--style=&quot;</tt> option specified here will override <tt>&quot;HIGHLIGHT_STYLE&quot;</tt>. Similarly, <tt>&quot;--replace-tabs=&quot;</tt> will override <tt>&quot;HIGHLIGHT_TABWIDTH&quot;</tt>.</p>
<dt><font SIZE="-1">OPENSCAD_COLORSCHEME</font></p>
<dd> Specifies the colorscheme used by <i>openscad</i> while previewing 3D models. Read <i>openscad</i> man page for colorschemes. Ranger will default to Tomorrow Night.</p>
<dt><font SIZE="-1">OPENSCAD_IMGSIZE</font></p>
<dd> Specifies the internal resolution <i>openscad</i> will use for rendering 3D models. The image will be downscaled to fit the preview pane. This resolution will default to &#8220;1000,1000&#8221; if no value is set.</p>
<dt><font SIZE="-1">XDG_CONFIG_HOME</font></p>
<dd> Specifies the directory for configuration files. Defaults to <i></i>$HOME<i>/.config</i>.</p>
<dt><font SIZE="-1">PYTHONOPTIMIZE</font></p>
<dd> This variable determines the optimize level of python. </p>
<p> Using PYTHONOPTIMIZE=1 (like python -O) will make python discard assertion statements. You will gain efficiency at the cost of losing some debug info. </p>
<p> Using PYTHONOPTIMIZE=2 (like python -OO) will additionally discard any docstrings. Using this will disable the &lt;F1&gt; key on commands.</p>
<dt>W3MIMGDISPLAY_PATH</p>
<dd> By changing this variable, you can change the path of the executable file for image previews. By default, it is set to <i>/usr/lib/w3m/w3mimgdisplay</i>.</dl>
<h2>EXAMPLES</h2>
<p> There are various examples on how to extend ranger with plugins or combine ranger with other programs. These can be found in the <i>/usr/share/doc/ranger/examples/</i> directory, or the <i>doc/ranger/</i> that is provided along with the source code.</p>
<h2>LICENSE</h2>
<p> <font SIZE="-1">GNU</font> General Public License 3 or (at your option) any later version.</p>
<h2>LINKS</h2>
<dl>
<dt>Download: &lt;<a rel="nofollow" href="https://ranger.github.io/ranger-stable.tar.gz">https://ranger.github.io/ranger-stable.tar.gz</a>&gt;</p>
<dd>
<dt>The project page: &lt;<a rel="nofollow" href="https://ranger.github.io/">https://ranger.github.io/</a>&gt;</p>
<dd>
<dt>The mailing list: &lt;<a rel="nofollow" href="https://savannah.nongnu.org/mail/?group=ranger">https://savannah.nongnu.org/mail/?group=ranger</a>&gt;</p>
<dd>
<dt><font SIZE="-1">IRC</font> channel: #ranger on freenode.net</p>
<dd></dl>
<p> ranger is maintained with the git version control system. To fetch a fresh copy, run: </p>
<pre>
 git clone git [at] github.com:ranger/ranger.git
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rifle/">rifle</a></code>(1)</p>
<h2>BUGS</h2>
<p> Report bugs here: &lt;<a rel="nofollow" href="https://github.com/ranger/ranger/issues">https://github.com/ranger/ranger/issues</a>&gt; </p>
<p> Please include as much relevant information as possible. For the most diagnostic output, run ranger like this: <tt>&quot;PYTHONOPTIMIZE= ranger --debug&quot;</tt> </p>
<h2>Index</h2>
<dt><a href="#lbAP">KEY BINDINGS</a></p>
<dd>
<dt><a href="#lbAS">MOUSE BUTTONS</a></p>
<dd>
<dt><a href="#lbAT">SETTINGS</a></p>
<dd>
<dt><a href="#lbAU">COMMANDS</a></p>
<dd>
<dt><a href="#lbAV">FILES</a></p>
<dd>
<dt><a href="#lbAY">ENVIRONMENT</a></p>
<dd>
<dt><a href="#lbAZ">EXAMPLES</a></p>
<dd>
<dt><a href="#lbBA">LICENSE</a></p>
<dd>
<dt><a href="#lbBB">LINKS</a></p>
<dd>
<dt><a href="#lbBC">SEE ALSO</a></p>
<dd>
<dt><a href="#lbBD">BUGS</a></p>
<dd></dl>
