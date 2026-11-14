---
title: "slsh(1)"
name: "slsh"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slsh/"
description: "slsh – Interpreter for S-Lang scripts"
---

<h2 class="name">NAME</h2>
<p> slsh &#8211; Interpreter for S-Lang scripts </p>
<h2>SYNOPSIS</h2>
<p> <code>slsh</code> [ <code>&#8211;help</code> ] [ <code>&#8211;version</code> ] [ <code>-g</code> ] [ <code>-n</code> ] [ <code>&#8211;init </code><i>file</i> ] [ <code>&#8211;no-readline</code> ] [ <code>-e </code><i>string</i> ] [ <code>-i</code> ] [ <code>-q, &#8211;quiet</code> ] [ <code>-t</code> ] [ <code>-v</code> ] [ <code>-|</code><i>script-file args&#8230;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>slsh</code> is a simple program for interpreting S-Lang scripts. It supports dynamic loading of S-Lang modules and includes a readline interface for interactive use.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show a summary of options</p>
<dt><code>&#8211;version</code></p>
<dd> Show <code>slsh</code> version information</p>
<dt><code>-g</code></p>
<dd> Compile with debugging code, tracebacks, etc</p>
<dt><code>-n</code></p>
<dd> Don&#8217;t load the personal initialization file</p>
<dt><code>&#8211;init </code><i>file</i></p>
<dd> Use this file instead of ~/.slshrc</p>
<dt><code>&#8211;no-readline</code></p>
<dd> Do not use a readline interface for the interactive mode</p>
<dt><code>-e </code><i>string</i></p>
<dd> Execute &#8220;string&#8221; as S-Lang code.</p>
<dt><code>-i</code></p>
<dd> Force interactive mode. Normally <code>slsh</code> will go into interactive mode if both stdin and stdout are attached to a terminal.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Startup quietly by not printing the version and copyright information.</p>
<dt><code>-t</code></p>
<dd> Normally, <code>slsh</code> will call slsh_main if it is defined. This option prevents that from happening making it useful for checking for syntax error.</p>
<dt><code>-v</code></p>
<dd> Show verbose loading messages. This is useful for seeing what files are being loaded.</dl>
<h2>INITIALIZATION</h2>
<p> Upon startup, the program will try to load <i>slsh.rc</i> as follows. If either SLSH_CONF_DIR or SLSH_LIB_DIR environment variables exist, then <code>slsh</code> will look look in the corresponding directories for <i>slsh.rc</i>. Otherwise it will look in: </p>
<p> <i>$(prefix)/etc/</i> (as specified in the Makefile) </p>
<p> <i>/usr/local/etc/</i> </p>
<p> <i>/usr/local/etc/slsh/</i> </p>
<p> <i>/etc/</i> </p>
<p> <i>/etc/slsh/</i> </p>
<p> The <i>slsh.rc</i> file may load other files from slsh&#8217;s library directory in the manner described below. </p>
<p> Once <i>slsh.rc</i> has been loaded, <code>slsh</code> will load $HOME/.slshrc if present. Finally, it will load the script specified on the command line. If the name of the script is -, then it will be read from stdin. If the script name is not present, or a string to execute was not specified using the -e option, then <code>slsh</code> will go into interactive mode and read input from the terminal. If the script is present and defines a function called slsh_main, that function will be called.</p>
<h2>LOADING FILES</h2>
<p> When a script loads a file via the built-in evalfile function or the require function (autoloaded by slsh.rc), the file is searched for along the SLSH_PATH as specified in the Makefile. An alternate path may be specified by the SLSH_PATH environment variable. </p>
<p> The search path may be queried and set during run time via the get_slang_load_path and set_slang_load_path functions, e.g., </p>
<pre>
   set_slang_load_path (&quot;/home/bill/lib/slsh:/usr/share/slsh&quot;);
</pre>
<h2>INTERACTIVE MODE</h2>
<p> When <code>slsh</code> is invoked without a script or is given the <code>-i</code> command line argument, it will go into into interactive mode. In this mode, the user will be prompted for input. The program will leave this mode and exit if it sees an EOF (Ctrl-D) or the user exits by issuing the quit command. </p>
<p> If an uncaught exception occurs during execution of a command, the error message will be shown and the user will be prompted for more input. </p>
<p> Any objects left on the stack after a command will be printed and the stack cleared. This makes interactive mode useful as a calculator, e.g., </p>
<pre><code>
slsh &gt; 3 * 10;
30 slsh &gt; x = [1:20];
slsh &gt; sum(sin(x) - cos(x));
0.458613 slsh &gt; quit;
</code></pre>
<p> Note that in this mode, variables are automatically declared. </p>
<p> The interactive mode also supports command logging. Logging is enabled by the start_log function. The stop_log function will turn off logging. The default file where logging information will be written is <i>slsh.log</i>. An alternative may be specified as an optional argument to the start_log function: </p>
<p>slsh &gt; start_log;<br />
Logging input to slsh.log<br />
        .<br />
        .slsh &gt; stop_log;<br />
slsh &gt; start_log(&#8220;foo.log&#8221;);<br />
Logging input to foo.log<br />
        .<br />
        .slsh &gt; stop_log;<br />
slsh &gt; start_log;<br />
Logging input to foo.log</p>
<p> Similarly, the save_input function may be used to save the previous input to a specified file: </p>
<p>slsh &gt; save_input;<br />
Input saved to slsh.log<br />
        slsh &gt; save_input(&#8220;foo.log&#8221;);<br />
Input saved to foo.log</p>
<p> As the above examples indicate, lines must end in a semicolon. This is a basic feature of the language and permits commands to span multiple lines, e.g., </p>
<p>slsh &gt; x = [<br />
    1, 2, 3,<br />
    4, 5, 6<br />
];<br />
slsh &gt; sum(x);<br />
 For convenience some users prefer that commands be automatically terminated with a semicolon. To have a semicolon silently appended to the end of an input line, put the following in <i>$HOME/.slshrc</i> file: </p>
<p>#ifdef __INTERACTIVE__<br />
slsh_append_semicolon(1);<br />
#endif</p>
<p> The interactive mode also supports shell escapes. To pass a command to the shell, prefix it with !, e.g., </p>
<pre>
    slsh&gt; !pwd
    /grandpa/d1/src/slang2/slsh
    slsh&gt; !cd doc/tm
    slsh&gt; !pwd
    /grandpa/d1/src/slang2/slsh/doc/tm
</pre>
<p> Finally, the interactive mode supports a help and apropos function: </p>
<pre>
    slsh&gt; apropos list
    apropos list ==&gt;
    List_Type
    list_append
    list_delete
.
.
    slsh&gt; help list_append
    list_append
     SYNOPSIS
       Append an object to a list
     USAGE
       list_append (List_Type, object, Int_Type nth)
.
.
</pre>
<p> For convenience, the help and apropos functions do not require the syntactic constraints of the other functions.</p>
<h2>READLINE HISTORY MECHANISM</h2>
<p> By default, <code>slsh</code> is built to use the S-Lang readline interface, which includes a customizable command completion and a history mechanism. When <code>slsh</code> (or any S-Lang application that makes use of this feature) starts in interactive mode, it will look for a file in the user&#8217;s home directory called <i>.slrlinerc</i> and load it if present. This file allows the user to customize the readline interface and enable the history to be saved between sessions. As an example, here is a version of the author&#8217;s <i>.slrlinerc</i> file: </p>
<pre><code>
% Load some basic functions that implement the history mechanism() = evalfile("rline/slrline.rc");
     % The name of the history file -- expands to .slsh_hist for slsh
     RLine_History_File = "$HOME/.${name}_hist";
     % Some addition keybindings.Some of these functions are defined % in rline / editfuns.sl, loaded by rline / slrline.rc
                                                                                                                     rline_unsetkey("^K");
     rline_setkey("bol", "^B");
     rline_setkey("eol", "^E");
     rline_setkey(&amp;rline_kill_eol, "^L");
     rline_setkey(&amp;rline_set_mark, "^K^B");
     rline_setkey(&amp;rline_copy_region, "^Kk");
     rline_setkey(&amp;rline_kill_region, "^K^V");
     rline_setkey(&amp;rline_yank, "^K^P");
     rline_setkey("redraw", "^R");
#ifexists rline_up_hist_search
     % Map the up / down arrow to the history search mechanism rline_setkey(&amp;rline_up_hist_search, "[A");
     rline_setkey(&amp;rline_down_hist_search, "[B");
#endif
#ifexists rline_edit_history
     rline_setkey(&amp;rline_edit_history, "^Kj");
#endif
     % Add a new function private define double_line()
     {
         variable p = rline_get_point();
         variable line = rline_get_line();
         rline_eol();
         variable pend = rline_get_point();
         rline_ins(line);
         rline_set_point(pend + p);
     }
     rline_setkey(&amp;double_line, "^K^L");
</code></pre>
<h2>MISCELLANEOUS SCRIPTS</h2>
<p> Several useful example scripts are located in <i>$prefix/share/slsh/scripts/</i>, where $prefix represents the <code>slsh</code> installation prefix (<i>/usr</i>, <i>/usr/local</i>,&#8230;). These scripts include:</p>
<dl>
<dt><code>sldb</code></p>
<dd> A script that runs the S-Lang debugger.</p>
<dt><code>jpegsize</code></p>
<dd> Reports the size of a jpeg file.</p>
<dt><code>svnsh</code></p>
<dd> A shell for browsing an SVN repository.</dl>
<h2>AUTHOR</h2>
<p> The principal author of <code>slsh</code> is John E. Davis &lt;<a rel="nofollow" href="http://www.jedsoft.org">www.jedsoft.org</a>&gt;. The interactive mode was provided by Mike Noble. The S-Lang library upon which <code>slsh</code> is based is primarily the work of John E. Davis with help from many others. </p>
<p> This manual page was originally written by Rafael Laboissiere for the Debian system (but may be used by others). </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in <i>/usr/share/common-licenses/GPL</i> </p>
<h2>Index</h2>
