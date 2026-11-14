---
title: "vi(1)"
name: "vi"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vi/"
description: "vim – Vi IMproved, a programmer’s text editor"
---

<h2 class="name">NAME</h2>
<p> vim &#8211; Vi IMproved, a programmer&#8217;s text editor </p>
<h2>SYNOPSIS</h2>
<p> <code>vim</code> [options] [file ..]<br />
 <code>vim</code> [options] &#8211;<br />
 <code>vim</code> [options] -t tag<br />
 <code>vim</code> [options] -q [errorfile] </p>
<p> <code>ex</code><br />
 <code>view</code><br />
 <code>gvim</code> <code>gview</code> <code>evim</code> <code>eview</code><br />
 <code>rvim</code> <code>rview</code> <code>rgvim</code> <code>rgview</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Vim</code> is a text editor that is upwards compatible to Vi. It can be used to edit all kinds of plain text. It is especially useful for editing programs. </p>
<p> There are a lot of enhancements above Vi: multi level undo, multi windows and buffers, syntax highlighting, command line editing, filename completion, on-line help, visual selection, etc.. See &quot;:help vi_diff.txt&quot; for a summary of the differences between <code>Vim</code> and Vi. </p>
<p> While running <code>Vim</code> a lot of help can be obtained from the on-line help system, with the &quot;:help&quot; command. See the ON-LINE HELP section below. </p>
<p> Most often <code>Vim</code> is started to edit a single file with the command </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>vim file</p>
<p> More generally <code>Vim</code> is started with: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>vim [options] [filelist]</p>
<p> If the filelist is missing, the editor will start with an empty buffer. Otherwise exactly one out of the following four may be used to choose one or more files to be edited.</p>
<dl>
<dt>file ..</p>
<dd> A list of filenames. The first one will be the current file and read into the buffer. The cursor will be positioned on the first line of the buffer. You can get to the other files with the &quot;:next&quot; command. To edit a file that starts with a dash, precede the filelist with &quot;&#8211;&quot;.</p>
<dt>&#8211;</p>
<dd> The file to edit is read from stdin. Commands are read from stderr, which should be a tty.</p>
<dt>-t {tag}</p>
<dd> The file to edit and the initial cursor position depends on a &quot;tag&quot;, a sort of goto label. {tag} is looked up in the tags file, the associated file becomes the current file and the associated command is executed. Mostly this is used for C programs, in which case {tag} could be a function name. The effect is that the file containing that function becomes the current file and the cursor is positioned on the start of the function. See &quot;:help tag-commands&quot;.</p>
<dt>-q [errorfile]</p>
<dd> Start in quickFix mode. The file [errorfile] is read and the first error is displayed. If [errorfile] is omitted, the filename is obtained from the &#8216;errorfile&#8217; option (defaults to &quot;AztecC.Err&quot; for the Amiga, &quot;errors.err&quot; on other systems). Further errors can be jumped to with the &quot;:cn&quot; command. See &quot;:help quickfix&quot;.</dl>
<p> <code>Vim</code> behaves differently, depending on the name of the command (the executable may still be the same file).</p>
<dl>
<dt>vim</p>
<dd> The &quot;normal&quot; way, everything is default.</p>
<dt>ex</p>
<dd> Start in Ex mode. Go to Normal mode with the &quot;:vi&quot; command. Can also be done with the &quot;-e&quot; argument.</p>
<dt>view</p>
<dd> Start in read-only mode. You will be protected from writing the files. Can also be done with the &quot;-R&quot; argument.</p>
<dt>gvim gview</p>
<dd> The GUI version. Starts a new window. Can also be done with the &quot;-g&quot; argument.</p>
<dt>evim eview</p>
<dd> The GUI version in easy mode. Starts a new window. Can also be done with the &quot;-y&quot; argument.</p>
<dt>rvim rview rgvim rgview</p>
<dd> Like the above, but with restrictions. It will not be possible to start shell commands, or suspend <code>Vim.</code> Can also be done with the &quot;-Z&quot; argument.</dl>
<h2>OPTIONS</h2>
<p> The options may be given in any order, before or after filenames. Options without an argument can be combined after a single dash.</p>
<dl>
<dt>+[num]</p>
<dd> For the first file the cursor will be positioned on line &quot;num&quot;. If &quot;num&quot; is missing, the cursor will be positioned on the last line.</p>
<dt>+/{pat}</p>
<dd> For the first file the cursor will be positioned in the line with the first occurrence of {pat}. See &quot;:help search-pattern&quot; for the available search patterns.</p>
<dt>+{command}</p>
<dd>
<dt>-c {command}</p>
<dd> {command} will be executed after the first file has been read. {command} is interpreted as an Ex command. If the {command} contains spaces it must be enclosed in double quotes (this depends on the shell that is used). Example: Vim &quot;+set si&quot; main.c<br />
 Note: You can use up to 10 &quot;+&quot; or &quot;-c&quot; commands.</p>
<dt>-S {file}</p>
<dd> {file} will be sourced after the first file has been read. This is equivalent to -c &quot;source {file}&quot;. {file} cannot start with &#8216;-&#8216;. If {file} is omitted &quot;Session.vim&quot; is used (only works when -S is the last argument).</p>
<dt>&#8211;cmd {command}</p>
<dd> Like using &quot;-c&quot;, but the command is executed just before processing any vimrc file. You can use up to 10 of these commands, independently from &quot;-c&quot; commands.</p>
<dt>-A</p>
<dd> If <code>Vim</code> has been compiled with ARABIC support for editing right-to-left oriented files and Arabic keyboard mapping, this option starts <code>Vim</code> in Arabic mode, i.e. &#8216;arabic&#8217; is set. Otherwise an error message is given and <code>Vim</code> aborts.</p>
<dt>-b</p>
<dd> Binary mode. A few options will be set that makes it possible to edit a binary or executable file.</p>
<dt>-C</p>
<dd> Compatible. Set the &#8216;compatible&#8217; option. This will make <code>Vim</code> behave mostly like Vi, even though a .vimrc file exists.</p>
<dt>-d</p>
<dd> Start in diff mode. There should be two, three or four file name arguments. <code>Vim</code> will open all the files and show differences between them. Works like <a href="/docs/linux/man/1-vimdiff/">vimdiff</a>(1).</p>
<dt>-d {device}</p>
<dd> Open {device} for use as a terminal. Only on the Amiga. Example: &quot;-d con:20/30/600/150&quot;.</p>
<dt>-D</p>
<dd> Debugging. Go to debugging mode when executing the first command from a script.</p>
<dt>-e</p>
<dd> Start <code>Vim</code> in Ex mode, just like the executable was called &quot;ex&quot;.</p>
<dt>-E</p>
<dd> Start <code>Vim</code> in improved Ex mode, just like the executable was called &quot;exim&quot;.</p>
<dt>-f</p>
<dd> Foreground. For the GUI version, <code>Vim</code> will not fork and detach from the shell it was started in. On the Amiga, <code>Vim</code> is not restarted to open a new window. This option should be used when <code>Vim</code> is executed by a program that will wait for the edit session to finish (e.g. mail). On the Amiga the &quot;:sh&quot; and &quot;:!&quot; commands will not work.</p>
<dt>&#8211;nofork</p>
<dd> Foreground. For the GUI version, <code>Vim</code> will not fork and detach from the shell it was started in.</p>
<dt>-F</p>
<dd> If <code>Vim</code> has been compiled with FKMAP support for editing right-to-left oriented files and Farsi keyboard mapping, this option starts <code>Vim</code> in Farsi mode, i.e. &#8216;fkmap&#8217; and &#8216;rightleft&#8217; are set. Otherwise an error message is given and <code>Vim</code> aborts.</p>
<dt>-g</p>
<dd> If <code>Vim</code> has been compiled with GUI support, this option enables the GUI. If no GUI support was compiled in, an error message is given and <code>Vim</code> aborts.</p>
<dt>-h</p>
<dd> Give a bit of help about the command line arguments and options. After this <code>Vim</code> exits.</p>
<dt>-H</p>
<dd> If <code>Vim</code> has been compiled with RIGHTLEFT support for editing right-to-left oriented files and Hebrew keyboard mapping, this option starts <code>Vim</code> in Hebrew mode, i.e. &#8216;hkmap&#8217; and &#8216;rightleft&#8217; are set. Otherwise an error message is given and <code>Vim</code> aborts.</p>
<dt>-i {viminfo}</p>
<dd> Specifies the filename to use when reading or writing the viminfo file, instead of the default &quot;~/.viminfo&quot;. This can also be used to skip the use of the .viminfo file, by giving the name &quot;NONE&quot;.</p>
<dt>-L</p>
<dd> Same as -r.</p>
<dt>-l</p>
<dd> Lisp mode. Sets the &#8216;lisp&#8217; and &#8216;showmatch&#8217; options on.</p>
<dt>-m</p>
<dd> Modifying files is disabled. Resets the &#8216;write&#8217; option. You can still modify the buffer, but writing a file is not possible.</p>
<dt>-M</p>
<dd> Modifications not allowed. The &#8216;modifiable&#8217; and &#8216;write&#8217; options will be unset, so that changes are not allowed and files can not be written. Note that these options can be set to enable making modifications.</p>
<dt>-N</p>
<dd> No-compatible mode. Resets the &#8216;compatible&#8217; option. This will make <code>Vim</code> behave a bit better, but less Vi compatible, even though a .vimrc file does not exist.</p>
<dt>-n</p>
<dd> No swap file will be used. Recovery after a crash will be impossible. Handy if you want to edit a file on a very slow medium (e.g. floppy). Can also be done with &quot;:set uc=0&quot;. Can be undone with &quot;:set uc=200&quot;.</p>
<dt>-nb</p>
<dd> Become an editor server for NetBeans. See the docs for details.</p>
<dt>-o[N]</p>
<dd> Open N windows stacked. When N is omitted, open one window for each file.</p>
<dt>-O[N]</p>
<dd> Open N windows side by side. When N is omitted, open one window for each file.</p>
<dt>-p[N]</p>
<dd> Open N tab pages. When N is omitted, open one tab page for each file.</p>
<dt>-R</p>
<dd> Read-only mode. The &#8216;readonly&#8217; option will be set. You can still edit the buffer, but will be prevented from accidentally overwriting a file. If you do want to overwrite a file, add an exclamation mark to the Ex command, as in &quot;:w!&quot;. The -R option also implies the -n option (see above). The &#8216;readonly&#8217; option can be reset with &quot;:set noro&quot;. See &quot;:help &#8216;readonly&#8217;&quot;.</p>
<dt>-r</p>
<dd> List swap files, with information about using them for recovery.</p>
<dt>-r {file}</p>
<dd> Recovery mode. The swap file is used to recover a crashed editing session. The swap file is a file with the same filename as the text file with &quot;.swp&quot; appended. See &quot;:help recovery&quot;.</p>
<dt>-s</p>
<dd> Silent mode. Only when started as &quot;Ex&quot; or when the &quot;-e&quot; option was given before the &quot;-s&quot; option.</p>
<dt>-s {scriptin}</p>
<dd> The script file {scriptin} is read. The characters in the file are interpreted as if you had typed them. The same can be done with the command &quot;:source! {scriptin}&quot;. If the end of the file is reached before the editor exits, further characters are read from the keyboard.</p>
<dt>-T {terminal}</p>
<dd> Tells <code>Vim</code> the name of the terminal you are using. Only required when the automatic way doesn&#8217;t work. Should be a terminal known to <code>Vim</code> (builtin) or defined in the termcap or terminfo file.</p>
<dt>-u {vimrc}</p>
<dd> Use the commands in the file {vimrc} for initializations. All the other initializations are skipped. Use this to edit a special kind of files. It can also be used to skip all initializations by giving the name &quot;NONE&quot;. See &quot;:help initialization&quot; within vim for more details.</p>
<dt>-U {gvimrc}</p>
<dd> Use the commands in the file {gvimrc} for GUI initializations. All the other GUI initializations are skipped. It can also be used to skip all GUI initializations by giving the name &quot;NONE&quot;. See &quot;:help gui-init&quot; within vim for more details.</p>
<dt>-V[N]</p>
<dd> Verbose. Give messages about which files are sourced and for reading and writing a viminfo file. The optional number N is the value for &#8216;verbose&#8217;. Default is 10.</p>
<dt>-v</p>
<dd> Start <code>Vim</code> in Vi mode, just like the executable was called &quot;vi&quot;. This only has effect when the executable is called &quot;ex&quot;.</p>
<dt>-w {scriptout}</p>
<dd> All the characters that you type are recorded in the file {scriptout}, until you exit <code>Vim.</code> This is useful if you want to create a script file to be used with &quot;vim -s&quot; or &quot;:source!&quot;. If the {scriptout} file exists, characters are appended.</p>
<dt>-W {scriptout}</p>
<dd> Like -w, but an existing file is overwritten.</p>
<dt>-x</p>
<dd> Use encryption when writing files. Will prompt for a crypt key.</p>
<dt>-X</p>
<dd> Don&#8217;t connect to the X server. Shortens startup time in a terminal, but the window title and clipboard will not be used.</p>
<dt>-y</p>
<dd> Start <code>Vim</code> in easy mode, just like the executable was called &quot;evim&quot; or &quot;eview&quot;. Makes <code>Vim</code> behave like a click-and-type editor.</p>
<dt>-Z</p>
<dd> Restricted mode. Works like the executable starts with &quot;r&quot;.</p>
<dt>&#8212;</p>
<dd> Denotes the end of the options. Arguments after this will be handled as a file name. This can be used to edit a filename that starts with a &#8216;-&#8216;.</p>
<dt>&#8211;echo-wid</p>
<dd> GTK GUI only: Echo the Window ID on stdout.</p>
<dt>&#8211;help</p>
<dd> Give a help message and exit, just like &quot;-h&quot;.</p>
<dt>&#8211;literal</p>
<dd> Take file name arguments literally, do not expand wildcards. This has no effect on Unix where the shell expands wildcards.</p>
<dt>&#8211;noplugin</p>
<dd> Skip loading plugins. Implied by -u NONE.</p>
<dt>&#8211;remote</p>
<dd> Connect to a Vim server and make it edit the files given in the rest of the arguments. If no server is found a warning is given and the files are edited in the current Vim.</p>
<dt>&#8211;remote-expr {expr}</p>
<dd> Connect to a Vim server, evaluate {expr} in it and print the result on stdout.</p>
<dt>&#8211;remote-send {keys}</p>
<dd> Connect to a Vim server and send {keys} to it.</p>
<dt>&#8211;remote-silent</p>
<dd> As &#8211;remote, but without the warning when no server is found.</p>
<dt>&#8211;remote-wait</p>
<dd> As &#8211;remote, but Vim does not exit until the files have been edited.</p>
<dt>&#8211;remote-wait-silent</p>
<dd> As &#8211;remote-wait, but without the warning when no server is found.</p>
<dt>&#8211;serverlist</p>
<dd> List the names of all Vim servers that can be found.</p>
<dt>&#8211;servername {name}</p>
<dd> Use {name} as the server name. Used for the current Vim, unless used with a &#8211;remote argument, then it&#8217;s the name of the server to connect to.</p>
<dt>&#8211;socketid {id}</p>
<dd> GTK GUI only: Use the GtkPlug mechanism to run gvim in another window.</p>
<dt>&#8211;version</p>
<dd> Print version information and exit.</dl>
<h2>ON-LINE HELP</h2>
<p> Type &quot;:help&quot; in <code>Vim</code> to get started. Type &quot;:help subject&quot; to get help on a specific subject. For example: &quot;:help ZZ&quot; to get help for the &quot;ZZ&quot; command. Use &lt;Tab&gt; and CTRL-D to complete subjects (&quot;:help cmdline-completion&quot;). Tags are present to jump from one place to another (sort of hypertext links, see &quot;:help&quot;). All documentation files can be viewed in this way, for example &quot;:help syntax.txt&quot;.</p>
<h2>FILES</h2>
<dl>
<dt>/usr/share/vim/vim81/doc/*.txt</p>
<dd> The <code>Vim</code> documentation files. Use &quot;:help doc-file-list&quot; to get the complete list.</p>
<dt>/usr/share/vim/vim81/doc/tags</p>
<dd> The tags file used for finding information in the documentation files.</p>
<dt>/usr/share/vim/vim81/syntax/syntax.vim</p>
<dd> System wide syntax initializations.</p>
<dt>/usr/share/vim/vim81/syntax/*.vim</p>
<dd> Syntax files for various languages.</p>
<dt>/usr/share/vim/vimrc</p>
<dd> System wide <code>Vim</code> initializations.</p>
<dt>~/.vimrc</p>
<dd> Your personal <code>Vim</code> initializations.</p>
<dt>/usr/share/vim/gvimrc</p>
<dd> System wide gvim initializations.</p>
<dt>~/.gvimrc</p>
<dd> Your personal gvim initializations.</p>
<dt>/usr/share/vim/vim81/optwin.vim</p>
<dd> Script used for the &quot;:options&quot; command, a nice way to view and set options.</p>
<dt>/usr/share/vim/vim81/menu.vim</p>
<dd> System wide menu initializations for gvim.</p>
<dt>/usr/share/vim/vim81/bugreport.vim</p>
<dd> Script to generate a bug report. See &quot;:help bugs&quot;.</p>
<dt>/usr/share/vim/vim81/filetype.vim</p>
<dd> Script to detect the type of a file by its name. See &quot;:help &#8216;filetype&#8217;&quot;.</p>
<dt>/usr/share/vim/vim81/scripts.vim</p>
<dd> Script to detect the type of a file by its contents. See &quot;:help &#8216;filetype&#8217;&quot;.</p>
<dt>/usr/share/vim/vim81/print/*.ps</p>
<dd> Files used for PostScript printing.</dl>
<p> For recent info read the VIM home page:<br />
 &lt;URL:<a rel="nofollow" href="http://www.vim.org/">http://www.vim.org/</a>&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-vimtutor/">vimtutor</a>(1)</p>
<h2>AUTHOR</h2>
<p> Most of <code>Vim</code> was made by Bram Moolenaar, with a lot of help from others. See &quot;:help credits&quot; in <code>Vim.</code><br />
 <code>Vim</code> is based on Stevie, worked on by: Tim Thompson, Tony Andrews and G.R. (Fred) Walter. Although hardly any of the original code remains.</p>
<h2>BUGS</h2>
<p> Probably. See &quot;:help todo&quot; for a list of known problems. </p>
<p> Note that a number of things that may be regarded as bugs by some, are in fact caused by a too-faithful reproduction of Vi&#8217;s behaviour. And if you think other things are bugs &quot;because Vi does it differently&quot;, you should take a closer look at the vi_diff.txt file (or type :help vi_diff.txt when in Vim). Also have a look at the &#8216;compatible&#8217; and &#8216;cpoptions&#8217; options. </p>
<h2>Index</h2>
