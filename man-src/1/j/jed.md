---
title: "jed(1)"
name: "jed"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jed/"
description: "Jed – programmers editor"
---

<h2>NAME</h2>
<p> Jed &#8211; programmers editor</p>
<h2>SYNOPSIS</h2>
<p> <code>jed [options] </code> <i>file</i> <code>&#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Jed &#8211; programmers editor</code> </p>
<p> Features: </p>
<p> Color syntax <i>highlighting. </i> Emulation of <code>Emacs,</code> <code>EDT,</code> <code>Wordstar, </code> and Brief editors. Extensible in a language resembling C. Completely customizable. Editing TeX files with AUC-TeX style editing (BiBTeX support too). Folding support, and much more&#8230; </p>
<p> For complete documentation, see GNU info files, this manual only provides brief tutorial.</p>
<h2>OPTIONS</h2>
<p> <i>-batch</i></p>
<dl>
<dt>
<dd> run Jed in batch mode. This is a non-interactive mode.</dl>
<p> <i>-n </i></p>
<dl>
<dt>
<dd> do not load <i>.jedrc </i> file.</dl>
<p> <i>-a &#8216;file&#8217;</i></p>
<dl>
<dt>
<dd> load <i>file</i> as user configuration file instead of .jedrc.</dl>
<p> <i>-g &#8216;n&#8217;</i></p>
<dl>
<dt>
<dd> goto line <i>n </i> in buffer (notice that in order to this option to take effect, if must appear after the file name in the command line, like &#8216;jed file -g 3&#8217;)</dl>
<p> <i>-l &#8216;file&#8217; </i></p>
<dl>
<dt>
<dd> load <i>file </i> as S-Lang code.</dl>
<p> <i>-f &#8216;function&#8217; </i></p>
<dl>
<dt>
<dd> execute S-Lang function named <i>function</i></dl>
<p> <i>-s &#8216;string&#8217;</i></p>
<dl>
<dt>
<dd> search forward for <i>string</i></dl>
<p> <i>-2 </i></p>
<dl>
<dt>
<dd> split window</dl>
<p> <i>-i &#8216;file&#8217;</i></p>
<dl>
<dt>
<dd> insert <i>file </i> into current buffer.</dl>
<h2>CONFIGURATION</h2>
<dl>
<dt>
<dd> <i>Emulating Other Editors</i></dl>
<p> JED&#8217;s ability to create new functions using the <i>S&#8211;Lang </i> programming language as well as allowing the user to choose key bindings, makes the emulation of other editors possible. Currently, JED provides reasonable emulation of the <i>Emacs, EDT, and Wordstar</i> editors. </p>
<dl>
<dt>
<dd> <i>Emacs Emulation</i></dl>
<p> <i>Emacs Emulation</i> is provided by the S-Lang code in <i>emacs.sl.</i> The basic functionality of Emacs is emulated; most Emacs users should have no problem with JED. To enable Emacs emulation in JED, make sure that the line: </p>
<dl>
<dt>
<dd> <i>() = evalfile (emacs); </i></dl>
<p> is in your <i>jed.rc</i> (.jedrc) startup file. JED is distributed with this line already present in the default jed.rc file. </p>
<dl>
<dt>
<dd> <i>EDT Emulation</i></dl>
<p> For <i>EDT</i> emulation, <i>edt.sl</i> must be loaded. This is accomplished by ensuring that the line: </p>
<dl>
<dt>
<dd> <i>() = evalfile (edt);</i></dl>
<p> is in present in the jed.rc (.jedrc) Startup File. </p>
<dl>
<dt>
<dd> <i>Wordstar Emulation</i></dl>
<p> wordstar.sl contains the S-Lang code for JED&#8217;s Wordstar emulation. Adding the line </p>
<dl>
<dt>
<dd> <i>() = evalfile (wordstar);</i></dl>
<p> to your jed.rc (.jedrc) startup file will enable JED&#8217;s Wordstar emulation.</p>
<h2>RUN TIME</h2>
<dl>
<dt>
<dd> <i>Status line and Windows</i></dl>
<p> <i>JED </i> supports multiple windows. Each window may contain the same buffer or different buffers. A status line is displayed immediately below each window. The status line contains information such as the JED version number, the buffer name, <i>mode,</i> etc. Please beware of the following indicators: </p>
<p> <i>**</i></p>
<dl>
<dt>
<dd> buffer has been modified since last save.</dl>
<p> <i>%%</i></p>
<dl>
<dt>
<dd> buffer is read only.</dl>
<p> <i>m</i></p>
<dl>
<dt>
<dd> Mark set indicator. This means a region is being defined.</dl>
<p> <i>d</i></p>
<dl>
<dt>
<dd> File changed on disk indicator. This indicates that the file associated with the buffer is newer than the buffer itself.</dl>
<p> <i>s</i></p>
<dl>
<dt>
<dd> spot pushed indicator.</dl>
<p> <i>+</i></p>
<dl>
<dt>
<dd> Undo is enabled for the buffer.</dl>
<p> <i>[Narrow]</i></p>
<dl>
<dt>
<dd> Buffer is narrowed to a region of LINES.</dl>
<p> <i>[Macro]</i></p>
<dl>
<dt>
<dd> A macro is being defined.</dl>
<dl>
<dt>
<dd> <i>Mini-Buffer.</i></dl>
<p> The <i>Mini-Buffer</i> consists of a single line located at the bottom of the screen. Much of the dialog between the user and JED takes place in this buffer. For example, when you search for a string, JED will prompt you for the string in the Mini-Buffer. </p>
<p> The <i>Mini-Buffer </i> also provides a direct link to the S-Langinterpreter. To access the interpreter, press <i>Ctrl-X Esc</i> and the <i>S-Lang&gt;</i> prompt will appear in the Mini-Buffer. Enter any valid S-Lang expression for evaluation by the interpreter. </p>
<p> It is possible to recall data previously entered into the <i>Mini-Buffer</i> by using the up and down arrow keys. This makes it possible to use and edit previous expressions in a convenient and efficient manner. </p>
<dl>
<dt>
<dd> <i>Basic Editing</i></dl>
<p> <i>Editing with JED</i> is pretty easy &#8211; most keys simply insert themselves. Movement around the buffer is usually done using the <i>arrow keys or page up and page down keys.</i> If <i>edt.sl</i> is loaded, the keypads on VTxxx terminals function as well. Here, only the highlights are touched upon (cut/paste operations are not considered `highlights&#8217;). In the following, any character prefixed by the <i>^</i> character denotes a Control character. On keyboards without an explicit Escape key, <i>Ctrl-[</i> will most likely generate and Escape character. </p>
<p> A <i>prefix argument</i> to a command may be generated by first hitting the <i>Esc</i> key, then entering the number followed by pressing the desired key. Normally, the prefix argument is used simply for repetition. For example, to move to the right 40 characters, one would press <i>Esc 4 0</i> followed immediately by the right arrow key. This illustrates the use of the repeat argument for repetition. However, the prefix argument may be used in other ways as well. For example, to begin defining a region, one would press the <i>Ctrl-@</i> key. This sets the mark and begins highlighting. Pressing the <i>Ctrl-@</i> key with a prefix argument will abort the act of defining the region and to pop the mark. </p>
<p> The following list of useful keybindings assumes that <i>emacs.sl</i> has been loaded. </p>
<p> <i>Ctrl-L</i></p>
<dl>
<dt>
<dd> Redraw screen.</dl>
<p> <i>Ctrl-_</i></p>
<dl>
<dt>
<dd> Undo (Control-underscore, also Ctrl-X u&#8217;).</dl>
<p> <i>Esc q</i></p>
<dl>
<dt>
<dd> Reformat paragraph (wrap mode). Used with a prefix argument. will justify the paragraph as well.</dl>
<p> <i>Esc n</i></p>
<dl>
<dt>
<dd> narrow paragraph (wrap mode). Used with a prefix argument will justify the paragraph as well.</dl>
<p> <i>Esc ;</i></p>
<dl>
<dt>
<dd> Make Language comment (Fortran and C)</dl>
<p> <i>Esc \</i></p>
<dl>
<dt>
<dd> Trim whitespace around point</dl>
<p> <i>Esc !</i></p>
<dl>
<dt>
<dd> Execute shell command</dl>
<p> <i>Esc $</i></p>
<dl>
<dt>
<dd> Ispell word</dl>
<p> <i>Ctrl-X ?</i></p>
<dl>
<dt>
<dd> Show line/column information.</dl>
<p> <i>`</i></p>
<dl>
<dt>
<dd> quoted_insert &#8212; insert next char as is (backquote key)</dl>
<p> <i>Esc s</i></p>
<dl>
<dt>
<dd> Center line.</dl>
<p> <i>Esc u</i></p>
<dl>
<dt>
<dd> Upcase word.</dl>
<p> <i>Esc d</i></p>
<dl>
<dt>
<dd> Downcase word.</dl>
<p> <i>Esc c</i></p>
<dl>
<dt>
<dd> Capitalize word.</dl>
<p> <i>Esc x</i></p>
<dl>
<dt>
<dd> Get M-x minibuffer prompt with command completion</dl>
<p> <i>Ctrl-X Ctrl-B</i></p>
<dl>
<dt>
<dd> pop up a list of buffers</dl>
<p> <i>Ctrl-X Ctrl-C</i></p>
<dl>
<dt>
<dd> exit JED</dl>
<p> <i>Ctrl-X 0</i></p>
<dl>
<dt>
<dd> Delete Current Window</dl>
<p> <i>Ctrl-X 1</i></p>
<dl>
<dt>
<dd> One Window.</dl>
<p> <i>Ctrl-X 2</i></p>
<dl>
<dt>
<dd> Split Window.</dl>
<dl>
<dt>
<dd> <i>Ctrl-X o</i></dl>
<dl>
<dt>
<dd> Other window.</dl>
<p> <i>Ctrl-X b</i></p>
<dl>
<dt>
<dd> switch to buffer</dl>
<p> <i>Ctrl-X k</i></p>
<dl>
<dt>
<dd> kill buffer</dl>
<p> <i>Ctrl-X s</i></p>
<dl>
<dt>
<dd> save some buffers</dl>
<p> <i>Ctrl-X Esc</i></p>
<dl>
<dt>
<dd> Get &quot;S-Lang&gt;&quot; prompt for interface to the S-Lang interpreter.</dl>
<p> <i>Esc .</i></p>
<dl>
<dt>
<dd> Find tag</dl>
<p> <i>Ctrl-@</i></p>
<dl>
<dt>
<dd> Set Mark (Begin defining a region). Used with a prefix argument aborts the act of defining the region and pops the Mark.</dl>
<h2>FILES</h2>
<p> <i>/usr/share/jed/lib/*.sl</i></p>
<dl>
<dt>
<dd> these are the default runtime jed slang files</dl>
<p> <i>/usr/share/jed/lib/site.sl</i></p>
<dl>
<dt>
<dd> This is the default startup file.</dl>
<p> <i>/etc/jed.rc</i></p>
<dl>
<dt>
<dd> The system wide configuration file.</dl>
<p> <i>~/.jedrc</i></p>
<dl>
<dt>
<dd> Per user configuration file.</dl>
<h2>AUTHOR</h2>
<p> <i>John E. Davis &lt;davis [at] space.mit.edu&gt;</i></p>
<dl>
<dt>
<dd> Jed&#8217;s Author</dl>
<p> &#8212; This document was <i>translated</i> to nroff by &quot;Boris D. Beletsky&quot; &lt;borik [at] isracom.co.il&gt; </p>
<h2>Index</h2>
