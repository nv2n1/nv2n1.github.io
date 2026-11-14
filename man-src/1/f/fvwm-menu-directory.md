---
title: "fvwm-menu-directory(1)"
name: "fvwm-menu-directory"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwm-menu-directory/"
description: "fvwm-menu-directory – builds a directory browsing menu for fvwm"
---

<h2 class="name">NAME</h2>
<p> fvwm-menu-directory &#8211; builds a directory browsing menu for fvwm </p>
<h2>SYNOPSIS</h2>
<p> <code>fvwm-menu-directory</code> [ <code>&#8211;help</code>|<code>-h</code>|<code>-?</code> ] [ <code>&#8211;version</code>|<code>-V</code> ] [ <code>&#8211;name</code>|<code>-na</code> <font SIZE="-1">NAME</font> ] [ <code>&#8211;title</code>|<code>-t</code> <font SIZE="-1">NAME</font> ] [ <code>&#8211;item</code>|<code>-it</code> <font SIZE="-1">NAME</font> ] [ <code>&#8211;icon-title</code>|<code>-icon-t</code> <font SIZE="-1">XPM</font> ] [ <code>&#8211;icon-dir</code>|<code>-icon-d</code> <font SIZE="-1">XPM</font> ] [ <code>&#8211;icon-file</code>|<code>-icon-f</code> <font SIZE="-1">XPM</font> ] [ <code>&#8211;icon-app</code>|<code>-icon-a</code> <font SIZE="-1">XPM</font> ] [ <code>&#8211;wm-icons</code> ] [ <code>&#8211;dir</code>|<code>-d</code> <font SIZE="-1">NAME</font> ] [ <code>&#8211;order</code>|<code>-o</code> <font SIZE="-1">NUM</font> ] [ <code>&#8211;[no]all</code>|<code>-a</code> ] [ <code>&#8211;[no]links</code>|<code>-l</code> ] [ <code>&#8211;xterm</code>|<code>-x</code> <font SIZE="-1">CMD</font> ] [ <code>&#8211;exec-title</code>|<code>-exec-t</code> <font SIZE="-1">CMD</font> ] [ <code>&#8211;exec-file</code>|<code>-exec-f</code> <font SIZE="-1">CMD</font> ] [ <code>&#8211;exec-app</code>|<code>-exec-a</code> [<font SIZE="-1">CMD</font>] ] [ <code>&#8211;command-title</code>|<code>-command-t</code> <font SIZE="-1">CMD</font> ] [ <code>&#8211;command-file</code>|<code>-command-f</code> <font SIZE="-1">CMD</font> ] [ <code>&#8211;command-app</code>|<code>-command-a</code> <font SIZE="-1">CMD</font> ] [ <code>&#8211;[no]reuse</code>|<code>-r</code> ] [ <code>&#8211;[no]check-subdirs</code>|<code>-ch</code> ] [ <code>&#8211;special-dirs</code>|<code>-s</code> [<font SIZE="-1">VALUE</font>] ] [ <code>&#8211;[no]memory-for-speed</code>|<code>-mem</code> ] [ <code>&#8211;menu-style</code>|<code>-men</code> <font SIZE="-1">NAME</font> ] [ <code>&#8211;func-name</code>|<code>-f</code> <font SIZE="-1">NAME</font> ]</p>
<h2>DESCRIPTION</h2>
<p> A perl script which provides an output to read in with PipeRead to build an fvwm menu containing a directory listing. Almost everything can be configured.</p>
<h2>HINTS</h2>
<p> The title item with its own attached action is usually added to the menu. This may be used to define an action for the directory for which the menu is built, such as starting a terminal in this directory (the default). However, this may annoy some users. To disable the title action use <code>&#8211;command-title</code> &quot;&quot;, to remove the title completely use <code>&#8211;title</code> &quot;&quot;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> show the usage and exit</p>
<dt><code>&#8211;version</code></p>
<dd> show version and exit</p>
<dt><code>&#8211;name</code> name</p>
<dd> menu name, used only with &#8211;reuse, default is MenuBrowser</p>
<dt><code>&#8211;title</code> title</p>
<dd> menu title format, default is &#8216;%*-40p&#8217; &#8211; last 40 characters of the current full path. <font SIZE="-1">TAB</font> can be specified as &#8216;	&#8217;, but in .fvwm2rc you should specify a double backslash or a real <font SIZE="-1">TAB</font>. </p>
<p> Format specifiers: <tt>%d</tt> &#8211; the current directory name <tt>%p</tt> &#8211; the current directory full path </p>
<p> These specifiers can receive an optional integer size, positive for right adjusted string or negative for left adjusted, example: <tt>%8x</tt>; and optional *num or *-num, which means to leave only the first or last (if minus) num of chars, the num must be greater than 3, since the striped part is replaced with &#8220;&#8230;&#8221;, example: %*30x. Both can be combined: %-10*-20x, this instructs to get only the 20 last characters, but if the length is less then 10 &#8211; to fill with up to 10 spaces on the right.</p>
<dt><code>&#8211;item</code> format</p>
<dd> menu item format, default is &#8216;%n&#8217;. <font SIZE="-1">TAB</font> and width modifiers for <tt>%n</tt>, <tt>%N</tt> and <tt>%s</tt> can be specified as described in <code>&#8211;title</code> above. Note, specifying a non default format slows the script. </p>
<p> Format specifiers: </p>
<pre>
  %n - file/dir name (without the path)
  %N - file/dir name (full with the path)
  %d - file/dir date (yyyy-mm-dd HH:MM:SS)
  %D - file/dir date (yyyy-mm-dd)
  %s - file/dir size (in bytes)
  %t - file/dir type (File|Dir |Link|Sock|Blck|Char|Pipe)
  %T - file/dir type (F|D|L|S|B|C|P)
</pre>
<p> Example: &#8211;title &#8216;%*-40p	Date, Type	Size&#8217; &#8211;item &#8216;%*40n	%d <tt>%t</tt>	%s&#8217;</p>
<dt><code>&#8211;icon-title</code> icon</p>
<dd> menu title icon, default is none</p>
<dt><code>&#8211;icon-dir</code> icon</p>
<dd> menu dir icon, default is none</p>
<dt><code>&#8211;icon-file</code> icon</p>
<dd> menu file icon, default is none</p>
<dt><code>&#8211;icon-app</code> icon</p>
<dd> menu application icon, default is none</p>
<dt><code>&#8211;wm-icons</code></p>
<dd> define icon names suitable for use with wm-icons package. Currently this is equivalent to: &#8211;icon-title menu/folder-open.xpm &#8211;icon-item menu/file.xpm &#8211;icon-dir menu/folder.xpm &#8211;icon-app menu/utility.xpm.</p>
<dt><code>&#8211;dir</code> dir</p>
<dd> starting dir, default is ${<font SIZE="-1">HOME-</font>.}</p>
<dt><code>&#8211;order</code> number</p>
<dd> in the range (-6 .. 6), default is 5: </p>
<pre>
  1 - do not sort,  2 - dirs first, 3 - files first
  4 - sort by name, 5 - dirs first, 6 - files first
  Negative number represents reverse order.
</pre>
<dt><code>&#8211;[no]all</code></p>
<dd> show hidden files, like in &#8216;ls -A&#8217;, default is &#8211;noall</p>
<dt><code>&#8211;[no]links</code></p>
<dd> follow linked directories, default is &#8211;nolinks</p>
<dt><code>&#8211;xterm</code> command</p>
<dd> X terminal call, default is &#8216;xterm -e&#8217;</p>
<dt><code>&#8211;exec-title</code> command</p>
<dd> an fvwm Exec command on directory title (usually the shell), default is ${SHELL-/bin/sh}. &#8216;-&#8216; means no Exec command, i.e. Nop. If the command is not started with &#8216;^&#8217; X terminal call is prepended. The command is started in the currently browsed directory.</p>
<dt><code>&#8211;exec-file</code> command</p>
<dd> an fvwm Exec command on regular files, default is ${EDITOR-vi}. &#8216;-&#8216; means no Exec command, i.e. Nop. If the command is not started with &#8216;^&#8217; X terminal call is prepended. The actual file name is appended to the command.</p>
<dt><code>&#8211;exec-app</code> [command]</p>
<dd> an fvwm Exec command on +x files, default is &#8216;-&#8216;, which means the same command as on regular files. If no command is given, it is assumed to be empty &#8211; simply run the +x file. If the command is not started with &#8216;^&#8217; X terminal call is prepended. The actual file name is appended to the command.</p>
<dt><code>&#8211;command-title</code> command</p>
<dd> an fvwm command to execute on title. If this option is not given (or command is &#8216;-&#8216;), the <tt>&quot;--exec-title&quot;</tt> is used instead. In the command, <tt>%d</tt> is substituted with the full directory path. </p>
<p> In fact, <i>&#8211;exec-title=tcsh</i> is equivalent to <i>&#8211;command-title=&#8217;Exec cd &#8220;%d&#8221;; xterm -e tcsh&#8217;</i> </p>
<p> The empty value disables the title action.</p>
<dt><code>&#8211;command-file</code> command</p>
<dd> an fvwm command to execute on regular files. If this option is not given (or command is &#8216;-&#8216;), the <tt>&quot;--exec-file&quot;</tt> is used instead. In the command, <tt>%f</tt> is substituted with the full file path. </p>
<p> In fact, &#8211;exec-file=vi is equivalent to &#8211;command-file=&#8217;Exec xterm -e vi &#8220;%f&#8221;&#8217;</p>
<dt><code>&#8211;command-app</code> command</p>
<dd> an fvwm command to execute on +x files. If this option is not given (or command is &#8216;-&#8216;), the <tt>&quot;--command-app&quot;</tt> is used instead. In the command, <tt>%f</tt> is substituted with the full file path. </p>
<p> In fact, &#8211;exec-app=^exec is equivalent to &#8211;command-app=&#8217;Exec exec &#8220;%f&#8221;&#8217;</p>
<dt><code>&#8211;[no]reuse</code></p>
<dd> no pop-up menus, reuse the same menu, default is &#8211;noreuse. When you specify this option the Menu action is used, not Popup. Also, the &#8211;name parameter is not ignored, and &#8211;dir parameter is ignored if there is ~/.fvwm/.fvwm-menu-directory.dir file. This file is only created or used with this option specified, it is the only solution for the current fvwm menu state.</p>
<dt><code>&#8211;[no]check-subdirs</code></p>
<dd> check all subdirs for having execute (+x) permission and replace &#8220;Popup&#8221;/&#8220;Menu&#8221; command with &#8220;Nop&#8221; for these without permissions. This has a visual effect of disabling popup triangle in the subdirectory item. The default is &#8211;nocheck-subdirs, because: 1) enabling this slows a bit the script, 2) with this option enabled, if no icons used and no dir/file separate sorting used there is no way to know that the item is directory and not file.</p>
<dt><code>&#8211;special-dirs</code> value</p>
<dd> add .. or ~ or / special directories according to given optional value. Without with option these directories are not added. Default value if not specified is &#8220;1,2&#8221;. The value is comma separated ordered special directory indexes, where 1 is parent directory, 2 is home directory, 3 is root directory. If minus is prepended to the value, special directories are added at the bottom of menu instead of top. Value &#8220;0&#8221; or any bad value is equivalent to non-specifying this option at all.</p>
<dt><code>&#8211;[no]memory-for-speed</code></p>
<dd> use speed optimization, i.e. use previously created directory menus without destroying it when closed, default is &#8211;nomemory-for-speed </p>
<pre>
    Warning: speed optimization takes up a lot of memory
    that is never free'd again while fvwm is running.
</pre>
<dt><code>&#8211;menu-style</code> name</p>
<dd> assign MenuStyle name to the menus</p>
<dt><code>&#8211;func-name</code> name</p>
<dd> overwrite the default MissingSubmenuFunction name that is &#8220;FuncFvwmMenuDirectory&#8221;</dl>
<p> Option parameters can be specified either using &#8216;=&#8217; or in the next argument. Short options are ok if not ambiguous: <tt>&quot;-a&quot;</tt>, <tt>&quot;-x&quot;</tt>, <tt>&quot;-icon-f&quot;</tt>; but be careful with short options, what is now unambiguous, can become ambiguous in the next versions.</p>
<h2>USAGE</h2>
<p> Put this into your fvwm configuration file to invoke the script: </p>
<pre>
  AddToFunc FuncFvwmMenuDirectory
  + I PipeRead &quot;fvwm-menu-directory -d '$0'&quot;
</pre>
<p> More complex example: </p>
<pre><code>
#AddToFunc FuncFvwmMenuDirectory
#+ I PipeRead "fvwm-menu-directory -d '$0' -x 'Eterm -g 80x40 -e' \
    -a -l -o 6 --exec-app --exec-title 'tcsh -l' --exec-file 'vim -R' \
    -t 'Go to: %d' --wm-icons"
</code></pre>
<p> And put this in the menu from which you want to pop-up the directory menus: </p>
<pre>
  AddToMenu SomeMenu MissingSubmenuFunction FuncFvwmMenuDirectory
  + &quot;Home Directory&quot;  Popup $[HOME]
  + &quot;Httpd Directory&quot; Popup /home/httpd
</pre>
<p> Note: please use absolute path names. </p>
<p> It is a good idea to set the menu pop-up delay to something positive and enable busy cursor </p>
<pre>
  MenuStyle * PopupDelayed, PopupDelay 200
  BusyCursor DynamicMenu True
</pre>
<p> in your configuration file when using this script for better results. </p>
<p> Another interesting usage (<tt>&quot;--reuse&quot;</tt> or <tt>&quot;-r&quot;</tt> is mandatary for this): </p>
<pre>
  AddToMenu Browser
  + DynamicPopupAction PipeRead \
    &quot;fvwm-menu-directory -r -na Browser -d / -s&quot;
  AddToMenu SomeMenu &quot;My Browser&quot; Menu Browser
</pre>
<p> Here the <tt>&quot;--dir&quot;</tt> parameter (starting directory) is ignored if there is ~/.fvwm/.fvwm-menu-directory.dir file, which you can delete.</p>
<h2>AUTHORS</h2>
<p> Inspired on 1999-06-07 by Dominik Vogt &lt;domivogt [at] fvwm.org&gt;. </p>
<p> Rewritten on 1999-08-05 by Mikhael Goikhman &lt;migo [at] homemail.com&gt;.</p>
<h2>COPYING</h2>
<p> The script is distributed by the same terms as fvwm itself. See <font SIZE="-1">GNU</font> General Public License for details.</p>
<h2>BUGS</h2>
<p> Report bugs to fvwm-bug [at] fvwm.org. </p>
<h2>Index</h2>
