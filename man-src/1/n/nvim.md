---
title: "nvim(1)"
name: "nvim"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvim/"
description: "nvim – edit text"
---

<h2 class="name">NAME</h2>
<p> <code>nvim</code> &#8211; edit text </p>
<h2>SYNOPSIS</h2>
<p> <code>nvim</code> [<i>options</i> ] [<i>file &#8230;</i> ]<br />
<code>nvim</code> [<i>options</i> ] &#8211;<br />
<code>nvim</code> [<i>options</i> ] &#8211;<code>t </code><i>tag</i><br />
<code>nvim</code> [<i>options</i> ] &#8211;<code>q </code>[<i>errorfile</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>nvim</code> is a text editor based on Vim. Start <code>nvim</code> followed by any number of options and/or files: </p>
<blockquote><p><tt>nvim [options] [file ...]</tt></p></blockquote>
<p> Commands in <code>nvim</code> begin with colon (`:&#8217; ) Type &quot;:help subject&quot; to get help on a specific subject. Use &lt;Tab&gt; and CTRL-D to complete subjects (&quot;:help cmdline-completion&quot;). </p>
<p> The &quot;quickref&quot; help section is a condensed reference of editor features: </p>
<blockquote><p><tt>:help quickref</tt></p></blockquote>
<p> If you are new to Vim/Nvim, start with the 30-minute tutorial: </p>
<blockquote><p><tt>:Tutor</tt></p></blockquote>
<p> After installing/updating Nvim, it&#8217;s a good idea to run the self-check: </p>
<blockquote><p><tt>:checkhealth</tt></p></blockquote>
<dl>
<dt><i>file &#8230;</i></p>
<dd> File(s) to edit. Opens one buffer per file. To switch between buffers, use the <code>:next</code> and <code>:previous</code> commands.</p>
<dt><code>&#8211; </code></p>
<dd> Reads text from standard input until <code>EOF</code> then opens a buffer with that text. User input is read from standard error, which should be a terminal.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t </code><i>tag</i></p>
<dd> Finds <i>tag</i> in the tags file, the associated file becomes the current file and the associated command is executed. Cursor is positioned at the tag location in the file. <code>:help tag-commands</code></p>
<dt><code>-q </code>[<i>errorfile</i> ]</p>
<dd> QuickFix mode. Display the first error in <i>errorfile</i> If <i>errorfile</i> is omitted, the value of the &#8216;errorfile&#8217; option is used (defaults to <code>errors.err )</code> Further errors can be jumped to with the <code>:cnext</code> command. <code>:help quickfix</code></p>
<dt><code>&#8211; </code></p>
<dd> End of options. Remaining arguments are treated as literal file names, including filenames starting with hyphen (`-&#8216; )</p>
<dt><code>-e</code></p>
<dd> Ex mode, reading stdin as Ex commands. <code>:help Ex-mode</code></p>
<dt><code>-E</code></p>
<dd> Ex mode, reading stdin as text. <code>:help Ex-mode</code></p>
<dt><code>-es</code></p>
<dd> Silent (non-interactive) Ex mode, reading stdin as Ex commands. Useful for scripting because it does NOT start a UI, unlike &#8211;<code>e</code> <code>:help silent-mode</code></p>
<dt><code>-Es </code>Silent (non-interactive) Ex mode, reading stdin as text.</p>
<dd> Useful for scripting because it does NOT start a UI, unlike &#8211;<code>E</code> <code>:help silent-mode</code></p>
<dt><code>-d</code></p>
<dd> Diff mode. Show the difference between two to eight files, similar to <a href="/docs/linux/man/1-sdiff/">sdiff</a>(1). <code>:help diff</code></p>
<dt><code>-R</code></p>
<dd> Read-only mode. Sets the &#8216;readonly&#8217; option. Implies &#8211;<code>n</code> Buffers can still be edited, but cannot be written to disk if already associated with a file. To overwrite a file, add an exclamation mark to the relevant Ex command, such as <code>:w!</code> <code>:help &#8216;readonly&#8217;</code></p>
<dt><code>-m</code></p>
<dd> Resets the &#8216;write&#8217; option, to disable file modifications. Writing to a file is disabled, but buffers can still be modified.</p>
<dt><code>-M</code></p>
<dd> Resets the &#8216;write&#8217; and &#8216;modifiable&#8217; options, to disable file and buffer modifications.</p>
<dt><code>-b</code></p>
<dd> Binary mode. <code>:help edit-binary</code></p>
<dt><code>-l</code></p>
<dd> Lisp mode. Sets the &#8216;lisp&#8217; and &#8216;showmatch&#8217; options.</p>
<dt><code>-A</code></p>
<dd> Arabic mode. Sets the &#8216;arabic&#8217; option.</p>
<dt><code>-H</code></p>
<dd> Hebrew mode. Sets the &#8216;hkmap&#8217; and &#8216;rightleft&#8217; options.</p>
<dt><code>-V </code>[<i>N </i>[<i>file</i> ] ]</p>
<dd> Verbose mode. Prints debug messages. <i>N</i> is the &#8216;verbose&#8217; level, defaults to <code>10</code> If <i>file</i> is specified, append messages to <i>file</i> instead of printing them. <code>:help &#8216;verbose&#8217;</code></p>
<dt><code>-D</code></p>
<dd> Debug mode for VimL (Vim script). Started when executing the first command from a script. :help debug-mode</p>
<dt><code>-n</code></p>
<dd> Disable the use of swap files. Sets the &#8216;updatecount&#8217; option to <code>0</code> Can be useful for editing files on a slow medium.</p>
<dt><code>-r </code>[<i>file</i> ]</p>
<dd> Recovery mode. If <i>file</i> is omitted then list swap files with recovery information. Otherwise the swap file <i>file</i> is used to recover a crashed session. The swap file has the same name as the file it&#8217;s associated with, but with `.swp&#8217; appended. <code>:help recovery</code></p>
<dt><code>-L </code>[<i>file</i> ]</p>
<dd> Alias for &#8211;<code>r</code></p>
<dt><code>-u </code><i>vimrc</i></p>
<dd> Use <i>vimrc</i> instead of the default ~/.config/nvim/init.vim If <i>vimrc</i> is <code>NORC</code> do not load any initialization files (except plugins). If <i>vimrc</i> is <code>NONE</code> loading plugins is also skipped. <code>:help initialization</code></p>
<dt><code>-i </code><i>shada</i></p>
<dd> Use <i>shada</i> instead of the default ~/.local/share/nvim/shada/main.shada If <i>shada</i> is <code>NONE</code> do not read or write a ShaDa file. <code>:help shada</code></p>
<dt><code>&#8211;noplugin</code></p>
<dd> Skip loading plugins. Implied by <code>-u NONE</code></p>
<dt><code>&#8211;clean</code></p>
<dd> Mimic a fresh install of Nvim. Skip loading non-builtin plugins and shada (viminfo) file.</p>
<dt><code>-o </code>[<i>N</i> ]</p>
<dd> Open <i>N</i> windows stacked horizontally. If <i>N</i> is omitted, open one window for each file. If <i>N</i> is less than the number of file arguments, allocate windows for the first <i>N</i> files and hide the rest.</p>
<dt><code>-O </code>[<i>N</i> ]</p>
<dd> Like &#8211;<code>o</code> but tile windows vertically.</p>
<dt><code>-p </code>[<i>N</i> ]</p>
<dd> Like &#8211;<code>o</code> but for tab pages.</p>
<dt><code>+ </code>[<i>linenum</i> ]</p>
<dd> For the first file, position the cursor on line <i>linenum</i> If <i>linenum</i> is omitted, position the cursor on the last line of the file. <code>+5</code> and <code>-c 5</code> on the command-line are equivalent to <code>:5</code> inside <code>nvim.</code></p>
<dt><code>+/ </code>[<i>pattern</i> ]</p>
<dd> For the first file, position the cursor on the first occurrence of <i>pattern</i> If <i>pattern</i> is omitted, the most recent search pattern is used (if any). <code>+/foo</code> and <code>-c /foo</code> on the command-line are equivalent to <code>/foo</code> and <code>:/foo</code> inside <code>nvim.</code> <code>:help search-pattern</code></p>
<dt><code>+</code><i>,command/</i> , &#8211;<code>c </code><i>command</i></p>
<dd> Execute <i>command</i> after reading the first file. Up to 10 instances allowed. Qq Cm +foo and <code>-c &quot;foo&quot;</code> are equivalent.</p>
<dt><code>&#8211;cmd </code><i>command</i></p>
<dd> Like &#8211;<code>c</code> but execute <i>command</i> before processing any vimrc. Up to 10 instances of these can be used independently from instances of &#8211;<code>c</code></p>
<dt><code>-S </code>[<i>session</i> ]</p>
<dd> Source <i>session</i> after the first file argument has been read. Equivalent to <code>-c &quot;source session&quot;</code> <i>session</i> cannot start with a hyphen (`-&#8216; ) If <i>session</i> is omitted then Session.vim is used, if found. <code>:help session-file</code></p>
<dt><code>-s </code><i>scriptin</i></p>
<dd> Read normal mode commands from <i>scriptin</i> The same can be done with the command <code>:source! scriptin</code> If the end of the file is reached before <code>nvim</code> exits, further characters are read from the keyboard.</p>
<dt><code>-w </code><i>scriptout</i></p>
<dd> Append all typed characters to <i>scriptout</i> Can be used for creating a script to be used with &#8211;<code>s</code> or <code>:source!</code></p>
<dt><code>-W </code><i>scriptout</i></p>
<dd> Like &#8211;<code>w</code> but truncate <i>scriptout</i></p>
<dt><code>&#8211;startuptime </code><i>file</i></p>
<dd> During startup, append timing messages to <i>file</i> Can be used to diagnose slow startup times.</p>
<dt><code>&#8211;api-info</code></p>
<dd> Dump API metadata serialized to msgpack and exit.</p>
<dt><code>&#8211;embed</code></p>
<dd> Use standard input and standard output as a msgpack-rpc channel. :help &#8211;embed</p>
<dt><code>&#8211;headless</code></p>
<dd> Do not start a UI. When supplied with &#8211;embed this implies that the embedding application does not intend to (immediately) start a UI. Also useful for &quot;scraping&quot; messages in a pipe. :help &#8211;headless</p>
<dt><code>&#8211;listen </code><i>address</i></p>
<dd> Start RPC server on this pipe or TCP socket.</p>
<dt><code>-h , -help</code></p>
<dd> Print usage information and exit.</p>
<dt><code>-v , -version</code></p>
<dd> Print version information and exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>NVIM_LOG_FILE</code></p>
<dd> Low-level log file, usually found at ~/.cache/nvim/log. :help $NVIM_LOG_FILE</p>
<dt><code>VIM</code></p>
<dd> Used to locate user files, such as init.vim. System-dependent. :help $VIM</p>
<dt><code>VIMRUNTIME</code></p>
<dd> Used to locate runtime files (documentation, syntax highlighting, etc.).</p>
<dt><code>XDG_CONFIG_HOME</code></p>
<dd> Path to the user-local configuration directory, see Sx FILES . Defaults to ~/.config :help xdg</p>
<dt><code>XDG_DATA_HOME</code></p>
<dd> Like <code>XDG_CONFIG_HOME</code> but used to store data not generally edited by the user, namely swap, backup, and ShaDa files. Defaults to ~/.local/share :help xdg</p>
<dt><code>VIMINIT</code></p>
<dd> Ex commands to be executed at startup. <code>:help VIMINIT</code></p>
<dt><code>SHELL</code></p>
<dd> Used to initialize the &#8216;shell&#8217; option, which decides the default shell used by features like <code>:terminal</code> <code>:! , and</code> <code>system()</code></dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.config/nvim/init.vim </code></p>
<dd> User-local <code>nvim</code> configuration file.</p>
<dt><code>~/.config/nvim </code></p>
<dd> User-local <code>nvim</code> configuration directory. See also <code>XDG_CONFIG_HOME</code></p>
<dt><code>$VIM/sysinit.vim </code></p>
<dd> System-global <code>nvim</code> configuration file.</p>
<dt><code>$VIM </code></p>
<dd> System-global <code>nvim</code> runtime directory.</dl>
<h2>AUTHORS</h2>
<p> Nvim was started by An Thiago de Arruda . Most of Vim was written by An -nosplit An Bram Moolenaar . Vim is based on Stevie, worked on by An Tim Thompson , An Tony Andrews , and An G.R. (Fred) Walter . <code>:help credits</code> </p>
<h2>Index</h2>
