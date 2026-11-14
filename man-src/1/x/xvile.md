---
title: "xvile(1)"
name: "xvile"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xvile/"
description: "vile, xvile, uxvile, lxvile – VI Like Emacs"
---

<h2>NAME</h2>
<p> vile, xvile, uxvile, lxvile &#8211; <code>VI L</code>ike <code>E</code>macs</p>
<h2>SYNOPSIS</h2>
<p> <code>vile [@</code><i>cmdfile</i><code>] [+</code><i>command</i><code>] [-FhIiRVv] [-g</code><i>NNN</i><code>] [-k</code><i>cryptkey</i><code>] [-s</code><i>pattern</i><code>] [-t</code><i>tag</i><code>] [</code><i>filename</i><code>]&#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> <i>vile</i> is a text editor. This man page is fairly terse. More information can be obtained from the internal help, available with the <code>-h</code> option or by using the &quot;:help&quot; command from within <i>vile</i>. </p>
<p> <i>xvile</i> is the same text editor, built as an X-windows application, with fully integrated mouse support, scrollbars, etc. </p>
<p> <i>uxvile</i> is a wrapper around <i>xvile</i> which invokes the latter program with the correct locale environment required to use a unicode character set and the &quot;UXVile&quot; X resource class set. </p>
<p> <i>lxvile</i> is a wrapper around <i>xvile</i> which invokes the latter program with a font chosen to match the current locale environment.</p>
<h2>SPIRIT</h2>
<p> <i>vile</i> retains the &quot;finger-feel&quot;, if you will, of <i>vi</i>, while adding the multiple buffer and multiple window features of emacs and other editors. It is definitely not a vi clone, in that some substantial stuff is missing, and the screen doesn&#8217;t look quite the same. The things that you tend to type over and over probably work. Things done less frequently, like configuring a startup file, are somewhat (or very, depending on how ambitious you are) different. But what matters most is that one&#8217;s &quot;muscle memory&quot; does the right thing to the text in front of you, and that is what <i>vile</i> tries to do for vi users.</p>
<h2>OPTIONS</h2>
<p> Vile accumulates most options into two temporary buffers <i>[vileinit]</i> and <i>[vileopts]</i>. The former is executed before reading the first file into a buffer. The latter is executed after reading the first file into a buffer. Each is removed after executing (unless an error is detected).</p>
<h3>COMMON OPTIONS</h3>
<dl>
<dt>-c<i>command</i></p>
<dd> <i>vile</i> will begin the session on the first file invoking the given command. Legal commands include many ex-style commands, vile-commands, etc., subject to shell quoting. This option is used most often with a line number or search pattern. For example </p>
<dl>
<dt>
<dd>
<pre>
vile -c123 filename
vile -c/pattern filename
</pre>
</dl>
<dt>
<dd> They correspond to ex-style commands on the given file: </p>
<dl>
<dt>
<dd>
<pre>
:123
:/pattern
</pre>
</dl>
<dt>
<dd> These are more verbose equivalents: </p>
<dl>
<dt>
<dd>
<pre>
vile -c'123 goto-line' filename
vile -c'search-forward /pattern/' filename
</pre>
</dl>
<dt>
<dd> You can use more than one command, e.g., </p>
<dl>
<dt>
<dd> vile -c&#8217;123&#8242; -c&#8217;10*goto-col&#8217; filename</dl>
<dt>
<dd> to put the cursor on column 10 of line 123. The &quot;*&quot; (or &quot;:&quot;) separates the repeat count (used by <i>goto-col</i>) from the line- or range-specification used by line-oriented commands.</p>
<dt>@<i>cmdfile</i></p>
<dd> <i>vile</i> will run the specified file as its startup file, and will bypass any normal startup file (i.e. <i>.vilerc</i>) or environment variable (i.e. <i>$VILEINIT</i>). This is added to <i>[vileinit]</i>.</p>
<dt>-D</p>
<dd> tells <i>vile</i> to trace the results of macro execution into the hidden buffer &quot;[Trace]&quot;.</p>
<dt>-e | -E</p>
<dd> Invokes <i>vile</i> in &quot;noview&quot; mode &#8211; changes are permitted to any buffer while in this mode (see &quot;-v&quot;).</p>
<dt>-F</p>
<dd> will run the syntax filter that applies to each filename on the command-line, and write the attributed text to the standard output.</p>
<dt>-h</p>
<dd> Invokes <i>vile</i> on the helpfile.</p>
<dt>-i | -I</p>
<dd> Tells <i>vile</i> to use <i>vileinit.rc</i> (which is installed) as the initialization file. If you do not have a .vilerc, <i>vile</i> will make a short one that sources <i>vileinit.rc</i> This is added to <i>[vileinit]</i>.</p>
<dt>-k <i>cryptkey</i> | -K <i>cryptkey</i></p>
<dd> Specifies an encryption/decryption key. See below for further discussion. This option applies only locally to the buffers named on the command-line, and is not added to <i>[vileopts]</i>, since that is executed too late.</p>
<dt>-R</p>
<dd> Invokes <i>vile</i> in &quot;readonly&quot; mode &#8211; no writes are permitted while in this mode. (This will also be true if <i>vile</i> is invoked as <i>view</i>, or if &quot;readonly&quot; mode is set in the startup file.)</p>
<dt>-s <i>pattern</i> | -S <i>pattern</i></p>
<dd> In the first file, <i>vile</i> will execute an initial search for the given pattern. This is not the same as &quot;-c/<i>pattern</i>&quot;, since that positions the cursor to the line matching the pattern. This option positions the cursor within the line.</p>
<dt>-t <i>tag</i></p>
<dd>
 <i>vile</i> will edit the correct file and move the cursor to the location of the tag. This requires a tagsfile created with the <i><a href="/docs/linux/man/1-ctags/">ctags</a></i>(1) command. The option -T is equivalent, and can be used when X11 option parsing eats the -t.</p>
<dt>-U</p>
<dd> overrides the $system-crlf variable, making new buffers start in dos mode.</p>
<dt>-u</p>
<dd> overrides the $system-crlf variable, making new buffers start in nodos mode.</p>
<dt>-v</p>
<dd> Invokes <i>vile</i> in &quot;view&quot; mode &#8211; no changes are permitted to any buffer while in this mode (see &quot;-e&quot;).</p>
<dt>-V</p>
<dd> <i>vile</i> will report its version number.</p>
<dt>-25 -43 -50 -60</p>
<dd> On PC systems you may be able to set the initial screen resolution from the command line.</p>
<dt>-80 -132</p>
<dd> On VMS systems you may be able to set the initial screen resolution from the command line. See <i>vile.hlp</i> for details.</dl>
<h3>X11 OPTIONS</h3>
<p> <i>xvile</i>-specific command-line options are detailed in the help file (see &quot;Standard X command line arguments&quot;). The standard ones (e.g. -display, -fn, -geometry, -name, etc.) are all supported.</p>
<h3>OBSOLETE OPTIONS</h3>
<p> vile recognizes some options which duplicate the functionality of the POSIX &quot;-c&quot; option:</p>
<dl>
<dt>+<i>command</i></p>
<dd> This has the same effect as &quot;-c<i>command</i>&quot;.</p>
<dt>-g <i>NNN</i> | -G <i>NNN</i></p>
<dd> This has the same effect as &quot;-c<i>NNN</i>&quot;. <i>vile</i> will begin the session on the first file jumping to the given line number <i>NNN</i>.</dl>
<h2>INVOCATION</h2>
<p> vile will edit the files specified on the command line. If no files are specified, and standard input is not connected to a terminal, then vile will bring up a buffer containing the output of the pipe it is connected to, and will re-open /dev/tty for commands. Files (except for the first) are not actually read into buffers until &quot;visited&quot;. All buffers are kept in memory: machines with not much memory or swap space may have trouble with this.</p>
<h2>STARTUP</h2>
<p> If the <i>@</i>cmdfile option is given, then the file given as &quot;cmdfile&quot; will be run before any files are loaded. If no <i>@</i> option appears, startup commands will be taken from the user&#8217;s <i>VILEINIT</i> variable, if it is set, from the file <i>.vilerc</i> in the current directory, if it exists, or from <i>$HOME/.vilerc</i>, as a last resort. See the help file for examples of what sorts of things might go into these command files.</p>
<h2>COMMANDS</h2>
<p> Please refer to the help available within <i>vile</i> for <i>vile</i>-specific commands. (That document, however, assumes familiarity with vi.) Short descriptions of each <i>vile</i> command may be obtained with the &quot;:describe-function&quot; and &quot;:describe-key&quot; commands. All commands may be listed with &quot;:show-commands&quot;. </p>
<p> Additional documentation on writing macros using the internal scripting language can be found in the file <i>macros.doc</i>, distributed with the vile source.</p>
<h2>RELATED PROGRAMS</h2>
<p> <i>vile</i> may also be built and installed as <i>xvile</i>, in which case it behaves as a native X Windows application, with scrollbars, better mouse support, etc. The help file has more information on this. </p>
<p> There is a program distributed with the vile source which is usually installed as <i>vile-manfilt</i>. (Two versions of the source for <i>vile-manfilt</i> are available, in C (manfilt.c) and in Perl (manfilt.pl).) It may be used in conjunction with <i>vile</i> or <i>xvile</i> (with the help of the macro in the file manpage.rc) to filter and view system manual pages. <i>xvile</i> will even (with your font set properly) display certain portions of the manual page text in bold or italics as appropriate. See the help file for details. </p>
<p> Likewise, there are several language filters, e.g., <i>vile-c-filt</i> for C, which can embolden, underline, or perform coloring on program source code. Again, see the help file for more information.</p>
<h2>ENCRYPTION</h2>
<p> The program <i>vile-crypt</i> can be used to encrypt/decrypt files using the same algorithm as <i>microEmac</i>&#8216;s internal crypt algorithm. This program, which uses public domain code written by by Dana Hoggatt, is no longer used in vile, though it is provided for compatibility. </p>
<p> <i>vile</i> currently uses the <i><a href="/docs/linux/man/3-crypt/">crypt</a>(3)</i> function for encryption/decryption, which is available on most Unix systems. This ensures that <i>vile</i> is able to read and write files compatibly with vi (but not vim, which uses an different algorithm derived from info-zip). The editor&#8217;s encryption/decryption key can be specified on the command line with &quot;-k key&quot;. Text to be encrypted can be specified as filenames on the command line, or provided as the standard input. On systems with a getpass() library routine, the user will be prompted for the encryption key if it is not given on the command line. To accommodate systems (such as linux) where the getpass() library routine is not interruptible from the keyboard, entering a crypt-key password which ends in ^C will cause the program to quit. See the help file for more information on <i>vile</i>&#8216;s encryption support, including a discussion of a collection of macros that interface with GNU&#8217;s gpg package.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>VILEINIT</code></p>
<dd> Editor initialization commands in lieu of a startup file. These are copied into <i>[vileinit]</i>, and executed.</p>
<dt><code>VILE_HELP_FILE</code></p>
<dd> Override the name of the help file, normally &#8220;vile.hlp&#8221;.</p>
<dt><code>VILE_LIBDIR_PATH</code></p>
<dd> Augment $PATH when searching for a filter program.</p>
<dt><code>VILE_STARTUP_FILE</code></p>
<dd> Override the name of the startup file, normally &#8220;.vilerc&#8221; (or &#8220;vile.rc&#8221; for non-UNIX systems).</p>
<dt><code>VILE_STARTUP_PATH</code></p>
<dd> Override the search path for the startup and help files.</dl>
<h2>SEE ALSO</h2>
<p> Your favorite vi document, the file <i>macros.doc</i>, and the <i>vile</i> help page, available with the <i>-h</i> option or as the text file <i>vile.hlp</i>.</p>
<h2>DEBTS and CREDITS</h2>
<p> <i>vile</i> was originally built from a copy of microEmacs, so a large debt of gratitude is due to the developers of that program. A lot of people have helped with code and bug reports on <i>vile</i>. Names are named at the bottom of the help file.</p>
<h2>AUTHORS</h2>
<p> <i>vile</i> was created by Paul Fox, Tom Dickey, and Kevin Buettner.</p>
<h2>BUGS</h2>
<p> The &quot;<code>VI L</code>ike <code>E</code>macs&quot; joke isn&#8217;t really funny. It only sounds that way. :-) Other suspicious behavior should be reported via the project mailing list, or via the web-based bug reporting system. Both of these are available here: </p>
<p> <a rel="nofollow" href="https://savannah.nongnu.org/projects/vile">https://savannah.nongnu.org/projects/vile</a> </p>
<h2>Index</h2>
