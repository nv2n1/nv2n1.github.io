---
title: "jove(1)"
name: "jove"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jove/"
description: "jove – an interactive display-oriented text editor"
---

<h2>NAME</h2>
<p> jove &#8211; an interactive display-oriented text editor</p>
<h2>SYNOPSIS</h2>
<p> <code>jove</code> [ <code>-d</code><i>&nbsp;<wbr>directory</i> ] [ <code>-l</code><i>&nbsp;<wbr>libdir</i> ] [ <code>-s</code><i>&nbsp;<wbr>sharedir</i> ] [ <code>-ls</code><i>&nbsp;<wbr>bothdir</i> ] [ <code>-J</code> ] [ <code>-j</code> ] [ <code>-w</code><i>n</i> ] [ <code>-t</code><i>&nbsp;<wbr>tag</i> ] [ <code>+</code><i>n file</i> ] [ <code>+/</code><i>pattern file</i> ] [ <code>-p</code><i>&nbsp;<wbr>file</i> ] [ <i>file</i>&#8230; ]<br />
 <code>jove -r</code></p>
<h2>DESCRIPTION</h2>
<p> JOVE is Jonathan&#8217;s Own Version of Emacs. It is based on the original EMACS editor written at MIT by Richard Stallman. Although JOVE is meant to be compatible with EMACS, there are some major differences between the two editors and you shouldn&#8217;t rely on their behaving identically. </p>
<p> JOVE works on any reasonable display terminal that is described in the <i>termcap</i> file (see <a href="/docs/linux/man/5-termcap/">TERMCAP</a>(5) for more details). When you start up JOVE, it checks to see whether you have your <i>TERM</i> environment variable set. On most systems that will automatically be set up for you, but if it&#8217;s not JOVE will ask you what kind of terminal you are using. To avoid having to type this every time you run JOVE you can set your <i>TERM</i> environment variable yourself. How you do this depends on which shell you are running. If you are running the C Shell, as most of you are, you type </p>
<p>&nbsp;<wbr>&nbsp;<wbr>%&nbsp;<wbr>setenv TERM <i>type</i> </p>
<p> and with the Bourne Shell, you type </p>
<p>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>TERM= <i>type</i> ; export TERM </p>
<p> where <i>type</i> is the name of the kind of terminal you are using (e.g., vt100). If neither of these works get somebody to help you.</p>
<h2>INVOKING JOVE</h2>
<p> If you run JOVE with no arguments you will be placed in an empty buffer, called <i>Main.</i> Otherwise, any arguments you supply are considered file names and each is &#8220;given&#8221; its own buffer. Only the first file is actually read in &#8212; reading other files is deferred until you actually try to use the buffers they are attached to. This is for efficiency&#8217;s sake: most of the time, when you run JOVE on a big list of files, you end up editing only a few of them. </p>
<p> The names of all of the files specified on the command line are saved in a buffer, called <i>*minibuf*.</i> The mini-buffer is a special JOVE buffer that is used when JOVE is prompting for some input to many commands (for example, when JOVE is prompting for a file name). When you are being prompted for a file name, you can type ^N (that&#8217;s Control-N) and ^P to cycle through the list of files that were specified on the command line. The file name will be inserted where you are typing and then you can edit it as if you typed it in yourself. </p>
<p> JOVE recognizes the following switches:</p>
<dl>
<dt><code>-d</code><i>&nbsp;<wbr>dirname</i></p>
<dd> <i>dirname</i> is taken to be the name of the current directory. This is for systems that don&#8217;t have a version of C shell that automatically maintains the <i>CWD</i> environment variable. If <code>-d</code> is not specified on a system without a modified C shell, JOVE will have to figure out the current directory itself, and that can be slow. You can simulate the modified C shell by putting the following lines in your C shell initialization file (.cshrc): </p>
<pre>
        alias cd        'cd \!*; setenv CWD $cwd'
        alias popd      'popd \!*; setenv CWD $cwd'
        alias pushd     'pushd \!*; setenv CWD $cwd'
</pre>
<dt><code>-l</code><i>&nbsp;<wbr>libdir</i></p>
<dd> Allows the user to specify the directory in which binary files required by JOVE can be found (default /usr/lib64/jove).</p>
<dt><code>-s</code><i>&nbsp;<wbr>sharedir</i></p>
<dd> Allows the user to specify the directory in which initialization files required by JOVE can be found (default /usr/share/jove).</p>
<dt><code>-ls</code><i>&nbsp;<wbr>bothdir</i></p>
<dd> Allows the user to specify the directory in which binary files and initialization files required by JOVE can be found.</p>
<dt><code>-J</code></p>
<dd> Inhibits reading of the system-wide initialization file (/usr/share/jove/jove.rc).</p>
<dt><code>-j</code></p>
<dd> Inhibits reading of the user&#8217;s initialization file (~/.joverc).</p>
<dt><code>+</code><i>n</i></p>
<dd> Reads the file designated by the following argument, and positions point at the <i>n&#8217;th</i> line instead of the (default) first line. This can be specified more than once but it doesn&#8217;t make sense to use it twice on the same file; in that case the second one wins. If no numeric argument is given after the +, the point is positioned at the end of the file.</p>
<dt><code>+/</code><i>pattern</i></p>
<dd> Reads the file designated by the following argument, and positions point at the first match of the pattern.</p>
<dt><code>-p</code><i>&nbsp;<wbr>file</i></p>
<dd> Parses the error messages in <i>file</i>. The error messages are assumed to be in a format similar to the C compiler, LINT, or GREP output.</p>
<dt><code>-t</code><i>&nbsp;<wbr>tag</i></p>
<dd> Runs the <i>find-tag</i> command on <i>tag</i> (see <a href="/docs/linux/man/1-ctags/">ctags</a>(1)).</p>
<dt><code>-w</code><i>n</i></p>
<dd> Divides the window into <i>n</i> windows (if <i>n</i> is omitted, it is taken to be 2). Subsequent files in the list are read in and displayed in succeeding windows.</dl>
<h2>RECOVERING BUFFERS AFTER A CRASH</h2>
<p> The <code>-r</code> option of jove runs the JOVE recover program. Use this when the system crashes, or JOVE crashes, or you accidently get logged out while in JOVE. If there are any buffers to be recovered, this will find them. </p>
<p> Recover looks for JOVE buffers that are left around and are owned by you. (You cannot recover other peoples&#8217; buffers, obviously.) If there were no buffers that were modified at the time of the crash or there were but recover can&#8217;t get its hands on them, you will be informed with the message, &#8220;There is nothing to recover.&#8221; Otherwise, recover prints the date and time of the version of the buffers it has, and then waits for you type a command. </p>
<p> To get a list of the buffers recover knows about, use the <i>list</i> command. This will list all the buffers and the files and the number of lines associated with them. Next to each buffer is a number. When you want to recover a buffer, use the <i>get</i> command. The syntax is <i>get buffer filename</i> where <i>buffer</i> is either the buffer&#8217;s name or the number at the beginning of the line. If you don&#8217;t type the buffer name or the filename, recover will prompt you for them. </p>
<p> If there are a lot of buffers and you want to recover all of them, use the <i>recover</i> command. This will recover each buffer to the name of the buffer with &#8220;.#&#8221; prepended to the name (so that the original isn&#8217;t over-written). It asks for each file and if you want to restore that buffer to that name you type &#8220;yes&#8221;. If you want to recover the file but to a different name, just type the new name in. If you type &#8220;no&#8221; recover will skip that file and go on to the next one. </p>
<p> If you want to look at a buffer before deciding to recover it, use the <i>print</i> command. The syntax for this is <i>print buffer</i> where <i>buffer</i> again is either its name or the number. You can type ^C if you want to abort printing the file to the terminal, and recover will respond with an appropriate message. </p>
<p> When you&#8217;re done and have all the buffers you want, type the <i>quit</i> command to leave. You will then be asked whether it&#8217;s okay to delete the tmp files. Most of the time that&#8217;s okay and you should type &#8220;yes&#8221;. When you say that, JOVE removes all traces of those buffers and you won&#8217;t be able to look at them again. (If you recovered some buffers they will still be around, so don&#8217;t worry.) So, if you&#8217;re not sure whether you&#8217;ve gotten all the buffers, you should answer &#8220;no&#8221; so that you&#8217;ll be able to run recover again at a later time (presumably after you&#8217;ve figured out which ones you want to save). If there were more than one crashed JOVE session, <i>quit</i> will move you on to dealing with the next one instead of exiting. </p>
<p> If you type ^C at any time other than when you&#8217;re printing a file to the terminal, recover will exit without a word. If you do this but wish you hadn&#8217;t, just type &#8220;jove -r&#8221; to the shell again, and you will be put back with no loss.</p>
<h2>GETTING HELP</h2>
<p> Once in JOVE, there are several commands available to get help. To execute any JOVE command, you type &#8220;&lt;ESC&gt; X command-name&#8221; followed by &lt;Return&gt;. To get a list of all the JOVE commands you type &#8220;&lt;ESC&gt; X&#8221; followed by &#8220;?&#8221;. The <i>describe-bindings</i> command can be used to get a list containing each key, and its associated command (that is, the command that gets executed when you type that key). If you want to save the list of bindings, you can set the jove variable <i>send-typeout-to-buffer</i> to ON (using the <i>set</i> command), and then execute the <i>describe-bindings</i> command. This will create a buffer and put in it the bindings list it normally would have printed on the screen. Then you can save that buffer to a file and print it to use as a quick reference card. (See VARIABLES below.) </p>
<p> Once you know the name of a command, you can find out what it does with the <i>describe-command</i> command, which you can invoke quickly by typing &#8220;ESC ?&#8221;. The <i>apropos</i> command will give you a list of all the command with a specific string in their names. For example, if you want to know the names of all the commands that are concerned with windows, you can run &#8220;apropos&#8221; with the keyword <i>window.</i> </p>
<p> If the initialization file has provided specific keybindings for your terminal, it should also be possible to view the keyboard layout with the keychart macro. </p>
<p> If you&#8217;re not familiar with the EMACS command set, it would be worth your while to use run TEACHJOVE. Do do that, just type &#8220;teachjove&#8221; to your shell and you will be placed in JOVE in a file which contains directions. I highly recommend this for beginners; you may save yourself a lot of time and headaches.</p>
<h2>KEY BINDINGS and VARIABLES</h2>
<p> You can alter the key bindings in JOVE to fit your personal tastes. That is, you can change what a key does every time you strike it. For example, by default the ^N key is bound to the command <i>next-line</i> and so when you type it you move down a line. If you want to change a binding or add a new one, you use the <i>bind-to-key</i> command. The syntax is &#8220;bind-to-key &lt;command&gt; key&#8221;. </p>
<p> You can also change the way JOVE behaves in little ways by changing the value of some variables with the <i>set</i> command. The syntax is &#8220;set &lt;variable&gt; value&#8221;, where value is a number or a string, or &#8220;on&#8221; or &#8220;off&#8221;, depending on the context. For example, if you want JOVE to make backup files, you set the &#8220;make-backup-files&#8221; variable to &#8220;on&#8221;. To see the value of a variable, use the &#8220;print &lt;variable&gt;&#8221; command.</p>
<h2>INITIALIZATION</h2>
<p> JOVE first reads the system-wide initialization file (/usr/share/jove/jove.rc) which provides reasonable defaults for your installation and loads standard macros. It will normally observe your TERM environment variable in order to provide terminal-specific key bindings and a map of your keyboard (see the standard &#8220;keychart&#8221; macro). </p>
<p> JOVE then automatically reads further commands from the initialization file called &#8220;.joverc&#8221; (&#8220;jove.rc&#8221; under MSDOS) in your HOME directory. In this file you can place commands that you would normally type in JOVE. If you like to rearrange the key bindings and set some variables every time you get into JOVE, you should put them in your initialization file. Here are a few lines from mine: </p>
<pre>
        set match-regular-expressions on
        1 auto-execute-command auto-fill /tmp/Re\|.*drft
        bind-to-key i-search-forward ^\
        bind-to-key i-search-reverse ^R
        bind-to-key find-tag-at-point ^[^T
        bind-to-key scroll-down ^C
        bind-to-key grow-window ^Xg
        bind-to-key shrink-window ^Xs
</pre>
<p> (Note that the Control Characters can be either two character sequences (e.g. ^ and C together as ^C) or the actual control character. If you want to use an ^ by itself you must BackSlash it (e.g., bind-to-key grow-window ^X\^ binds grow-window to &#8220;^X^&#8221;).</p>
<h2>ENVIRONMENT</h2>
<p> If the variable <font SIZE="-1"><code>&quot;LC_CTYPE&quot;</code></font> (see <code><a href="/docs/linux/man/5-environ/">environ</a></code>(5)) is not set in the environment, the operational behavior of JOVE for the <font SIZE="-1"><code>&quot;LC_CTYPE&quot;</code></font> locale category is determined by the value of the <font SIZE="-1"><code>LANG</code></font> environment variable. If <font SIZE="-1"><code>LC_ALL</code></font> is set, its contents are used to override both the <font SIZE="-1"><code>LANG</code></font> and the <font SIZE="-1"><code>&quot;LC_CTYPE&quot;</code></font> variable. If none of the above variables is set in the environment, the &quot;C&quot; (U.S. style) locale determines how JOVE behaves.</p>
<dl>
<dt><font SIZE="-1"><code>LC_CTYPE</code></font></p>
<dd> Determines how JOVE handles characters. When <font SIZE="-1"><code>LC_CTYPE</code></font> is set to a valid value, JOVE can display and handle text and filenames containing valid characters for that locale. In particular, characters will be correctly recognised as upper or lower case and displayed if printable. However JOVE cannot display or handle Extended Unix Code (EUC) characters which are more than 1 byte wide. In the &quot;C&quot; locale, only characters from 7-bit ASCII are valid (all characters with the eighth bit set being displayed in octal). In the &quot;iso_8859_1&quot; locale (if supported by the OS), the full Latin-1 alphabet is available. The JOVE variable &#8220;lc-ctype&#8221; can be used to change the locale while JOVE is running.</dl>
<h2>SOME MINOR DETAILS</h2>
<p> You should type ^\ instead of ^S in many instances. For example, the way to search for a string is documented as being &#8220;^S&#8221; but in reality you should type &#8220;^\&#8221;. This is because ^S is the XOFF character (what gets sent when you type the NO SCROLL key), and clearly that won&#8217;t work. The XON character is &#8220;^Q&#8221; (what gets sent when you type NO SCROLL again) which is documented as the way to do a quoted-insert. The alternate key for this is &#8220;^^&#8221; (typed as &#8220;^`&#8221; on vt100&#8217;s and its look-alikes). If you want to enable ^S and ^Q and you know what you are doing, you can put the line: </p>
<pre>
        set allow-^S-and-^Q on
</pre>
<p> in your initialization file. </p>
<p> If your terminal has a metakey and you turn on the &#8220;meta-key&#8221; variable, JOVE will use it to generate commands which would otherwise start with an ESC. JOVE will automatically turn on &#8220;meta-key&#8221; if the METAKEY environment variable exists. This is useful for if you have different terminals (e.g., one at home and one at work) and one has a metakey and the other doesn&#8217;t. However, if a locale which recognises 8-bit characters is in force, a metakey may be better used to generate the extra characters (so leave the &#8220;meta-key&#8221; variable off).</p>
<h2>FILES</h2>
<pre><code>
/usr/share/jove/jove.rc --- system-wide initialization file
/usr/share/jove/jove.rc.$TERM --- terminal-specific initialization file
/usr/share/jove/keychart.$TERM --- terminal-specific help file
/usr/share/jove/macros --- standard macros file
~/.joverc --- personal initialization file
/tmp --- where temporary files are stored
/usr/share/jove/teach-jove --- the interactive tutorial
/usr/lib64/jove/recover --- the recovery program
/usr/lib64/jove/portsrv --- for running shells in windows (pdp11 only)
</code></pre>
<h2>ENVIRONMENT VARIABLES</h2>
<p>TERM &#8212; your terminal type<br />
METAKEY &#8212; if defined, sets the &#8220;meta-key&#8221; variable<br />
SHELL &#8212; the shell to be used by the &#8220;shell&#8221; and other commands<br />
COMSPEC &#8212; (on MSDOS) used if SHELL is not defined<br />
MAIL &#8212; to initialize the &#8220;mailbox&#8221; variable<br />
JOVELIB &#8212; overrides /usr/lib64/jove unless overridden by -l<br />
JOVESHARE &#8212; overrides /usr/share/jove unless overridden by -s<br />
TMPDIR &#8212; overrides /tmp as directory for temporary files<br />
LC_ALL, LC_CTYPE, LANG &#8212; to set the locale</p>
<h2>SEE ALSO</h2>
<pre><code>
ctags(1) --- to generate tags for the find-tag command and the -t command-line
option
ed(1) --- for a description of regular expressions
teachjove(1) --- for an interactive JOVE tutorial.
</code></pre>
<h2>DIAGNOSTICS</h2>
<p> JOVE diagnostics are meant to be self-explanatory, but you are advised to seek help whenever you are confused. You can easily lose a lot of work if you don&#8217;t know EXACTLY what you are doing.</p>
<h2>BUGS</h2>
<p> Lines can&#8217;t be more than 1024 characters long. </p>
<p> Searches can&#8217;t cross line boundaries.</p>
<h2>AUTHOR</h2>
<p> Jonathan Payne </p>
<h2>Index</h2>
