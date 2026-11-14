---
title: "rlwrap(1)"
name: "rlwrap"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rlwrap/"
description: "rlwrap – readline wrapper"
---

<h2>NAME</h2>
<p> rlwrap &#8211; readline wrapper</p>
<h2>SYNOPSIS</h2>
<p> <code>rlwrap</code> <i>[rlwrap-options]</i> <i>command &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>rlwrap</code> runs the specified <i>command</i>, intercepting user input in order to provide <code>readline</code>&#8216;s line editing, persistent history and completion. </p>
<p> <code>rlwrap</code> tries to be completely transparent &#8211; you (or your shell) shouldn&#8217;t notice any difference between <code>command</code> and <code>rlwrap command</code> &#8211; except the added readline functionality, of course. This should even hold true when you are re-directing, piping and sending signals from and to <i>command</i>, or when <i>command</i> manipulates its terminal settings. </p>
<p> There are many options to add (programmable) completion, handle multi-line input, colour and re-write prompts. If you don&#8217;t need them (and you probably don&#8217;t), you can skip the rest of this manpage.</p>
<h2>OPTIONS</h2>
<dl>
<dt> <code>-a, &#8211;always-readline [<i>password_prompt</i>]</code></p>
<dd> Always remain in &quot;readline mode&quot;, regardless of <i>command</i>&#8216;s terminal settings. Use this option if you want to use <code>rlwrap</code> with <i>command</i>s that already use readline. <code>NB</code>: With this option, rlwrap will echo (and save) passwords, unless you give <i>command</i>&#8216;s password prompt as an argument. The argument is optional; if given, it has to directly follow the option without an intervening space. </p>
<p> On a linux machine you can use the <code>-N</code> (<code>&#8211;no-children</code>) option to prevent the wrapping of pagers and editors called from <i>command</i>; this should make them much more usable </p>
<p> Many commands that need <code>&#8211;always-readline</code> may also need <code>-t dumb</code> to prevent terminal control sequences from confusing <code>rlwrap</code> (although this will annoy the above-mentioned pagers and editors)<br />
&nbsp;<wbr></p>
<dt> <code>-A, &#8211;ansi-colour-aware </code></p>
<dd> Prompts that use colour will confuse rlwrap, especially at the end of long input lines. This option will make rlwrap better behaved in such cases. If the prompt contains anything fancier than ANSI colour codes, this option may actually make things worse.</p>
<dt> <code>-b, &#8211;break-chars <i>list_of_characters</i></code></p>
<dd> Consider the specified characters word-breaking (whitespace is always word-breaking). This determines what is considered a &quot;word&quot;, both when completing and when building a completion word list from files specified by <code>-f</code> options following (not preceding!) it. Default list (){}[],&#8217;+-=&amp;^%$#@&quot;&quot;;|\ Unless -c is specified, / and . (period) are included in the default list.</p>
<dt> <code>-c, &#8211;complete-filenames </code></p>
<dd> Complete filenames (filename completion is always case-sensitive, even with the -i option)<br />
&nbsp;<wbr>When doing this, rlwrap keeps track of&nbsp;<wbr><i>command</i>s working directory.</p>
<dt> <code>-C, &#8211;command-name <i>command_name|N</i></code></p>
<dd> Use <i>command_name</i> instead of <i>command</i> to determine the names of history and completion files, and to initialise readline (as specified in ~/.inputrc). A numeric argument N &gt; 0 means: use the Nth argument counting backwards from the end of the argument list</p>
<dt> <code>-D, &#8211;history-no-dupes <i>n</i></code></p>
<dd> How agressively to weed out duplicate entries from the input history. If <i>n</i> = <code>0</code>, all inputs are kept in the history list, if <i>n</i> = <code>1</code> (this is the default) consecutive duplicates are dropped from the list, while <i>n</i> = <code>2</code> will make <code>rlwrap</code> drop all previous occurrences of the current input from the list.</p>
<dt> <code>-e, &#8211;extra-char-after-completion <i>char</i></code></p>
<dd> By default, rlwrap appends a space after any inserted completion text. Use this option to change this to &#8221; (don&#8217;t insert anything) or some other character.</p>
<dt> <code>-f, &#8211;file <i>file</i></code></p>
<dd> Split <i>file</i> into words and add them to the completion word list. This option can be given more than once, and <i>adds</i> to the default completion list in $RLWRAP_HOME or /usr/share/rlwrap/completions. </p>
<p> Specifying <code>-f .</code> will make <code>rlwrap</code> use the current history file as a completion word list.</p>
<dt> <code>-g, &#8211;forget-matching <i>regexp</i></code></p>
<dd> Forget (i.e. drop from history list) all input lines that match the POSIX 1003.2 regular expression <i>regexp</i>. The match is always case-insensitive. <i>regexp</i> may be an ordinary string. For more about regular expressions, see <code>regex (7)</code></p>
<dt> <code>-h, &#8211;help </code></p>
<dd> Print a short help message.</p>
<dt> <code>-H, &#8211;history-filename <i>file</i></code></p>
<dd> Read command history from <i>file</i> (and write it back there if &#8211;histsize &gt;= 0)</p>
<dt> <code>-i, &#8211;case-insensitive </code></p>
<dd> Ignore case when completing (filename completion remains case-sensitive). This option has to come before any -f options.</p>
<dt> <code>-I, &#8211;pass-sigint-as-sigterm </code></p>
<dd> Send a TERM signal to <i>command</i> when an INT is received (e.g. when you press CTRL-C).</p>
<dt> <code>-l, &#8211;logfile <i>file</i></code></p>
<dd> When in readline mode, append <i>command</i>&#8216;s output (including echo&#8217;ed user input) to <i>file</i> (creating <i>file</i> when it doesn&#8217;t exist).</p>
<dt> <code>-n, &#8211;no-warnings </code></p>
<dd> Don&#8217;t print warnings.</p>
<dt> <code>-N, &#8211;no-children </code></p>
<dd> Don&#8217;t rlwrap <i>command</i>&#8216;s children: whenever <code>rlwrap</code> notices that <i>command</i> is waiting for one of its children, it switches to direct mode, handing down all keypresses immediately. With this option commands that need &#8211;always-readline can call editors and pagers and still be usable. </p>
<p> This option needs /proc/<i>command</i>_pid/wchan, so it only works with linux kernels configured with CONFIG_KALLSYMS.</p>
<dt> <code>-m, &#8211;multi-line [<i>newline_substitute</i>]</code></p>
<dd> Enable multi-line input using a &quot;newline substitute&quot; character sequence (&quot; \ &quot;, [space-backslash-space] by default). Newline substitutes are translated to newlines before sending the input to <i>command</i>. With this option, you can call an external editor $RLWRAP_EDITOR on the (expanded) current input with the <i>rlwrap_call_editor</i> key (CTRL-^ by default) The argument is optional; if given, it has to directly follow the option without an intervening space.</p>
<dt> <code>-M, &#8211;multi-line-ext <i>.ext</i></code></p>
<dd> Call multi-line-editor on temporary files with filename extension <i>.ext</i> (useful for e.g. automatic syntax colouring)</p>
<dt> <code>-o, &#8211;one-shot </code></p>
<dd> Send an EOF to <i>command</i> after accepting the first line of input</p>
<dt> <code>-O, &#8211;only-cook <i>regexp</i></code></p>
<dd> Only ever &quot;cook&quot; prompts that match <i>regexp</i></p>
<dt> <code>-p, &#8211;prompt-colour [<i>colour_name|Colour_name|colour_spec</i>]</code></p>
<dd> Use one of the colour names <i>black, red, green, yellow, blue, cyan, purple (=magenta)</i> or <i>white</i>, or an ANSI-conformant &lt;colour_spec&gt; to colour any prompt displayed by <i>command</i>. An uppercase colour name (<i>Yellow</i> or <i>YELLOW</i> ) gives a bold prompt. Prompts that already contain (colour) escape sequences or one of the readline &quot;ignore markers&quot; (ASCII 0x01 and 0x02) are not coloured. This option implies &#8211;ansi-colour-aware. <i>colour spec</i> has the form &lt;attr&gt;;&lt;fg&gt;[;&lt;bg&gt;] Example: -p&#8217;1;31&#8242; will give a bold red prompt on the current background (this is the default when no argument is given). Google for &#8216;ANSI color&#8217; to learn more about colour codes. The argument is optional; if given, it has to directly follow the option without an intervening space.</p>
<dt> <code>-P, &#8211;pre-given <i>text</i></code></p>
<dd> Start <code>rlwrap</code> with <i>text</i> in its edit buffer (this will automatically set the &#8211;always-readline option).</p>
<dt> <code>-q, &#8211;quote-characters <i>list_of_characters</i></code></p>
<dd> Assume that the given characters act as quotes, e.g. when matching parentheses. Take care to escape the list properly for your shell (example: -q &quot;\&quot;&#8217;&quot;, which happens to be the default, or -q &quot;\&quot;&quot; which will be better for Lisp users)</p>
<dt> <code>-r, &#8211;remember </code></p>
<dd> Put all words seen on in- and output on the completion list.</p>
<dt> <code>-R, &#8211;renice </code></p>
<dd> Make <code>rlwrap</code> nicer than <i>command</i> (cf <code>nice (1)</code>). This may prevent <code>rlwrap</code> from interrupting <i>command</i> to display a prompt when <i>command</i> is still &quot;thinking&quot; about what to output next.</p>
<dt> <code>-s, &#8211;histsize <i>N</i></code></p>
<dd> Limit the history list to N entries, truncating the history file (default: 300). A negative size -N means the same as N, but treats the history file as read-only.</p>
<dt> <code>-S, &#8211;substitute-prompt <i>prompt</i></code></p>
<dd> Substitute the specified prompt for <i>command</i>&#8216;s own prompt. Mainly useful when <i>command</i> doesn&#8217;t have a prompt.</p>
<dt> <code>-t, &#8211;set-term-name <i>name</i></code></p>
<dd> Set <i>command</i>&#8216;s TERM to <i>name</i>. Programs that confuse <code>rlwrap</code> with fancy screen control codes can sometimes be tamed by specifying <code>-t dumb</code></p>
<dt> <code>-U, &#8211;mirror-arguments </code></p>
<dd> (linux only) Keep track of <i>command</i>&#8216;s arguments as seen by the <code>ps (1)</code> command, and mirror them in <code>rlwrap</code>&#8216;s own arguments This is mainly useful for commands that overwrite command-line password arguments that would be exposed by rlwrap without this option.</p>
<dt> <code>-v, &#8211;version </code></p>
<dd> Print rlwrap version.</p>
<dt> <code>-w, &#8211;wait-before-prompt <i>timeout</i></code></p>
<dd> In order to determine if <i>command</i>&#8216;s last output is a prompt, <code>rlwrap</code> waits <i>timeout</i> millisecs after receiving it. Only when no more output has arrived, it is cooked (coloured, filtered and/or replaced by a substitute prompt) and displayed as a prompt. Before this the prompt is displayed &quot;uncooked&quot;. Most users won&#8217;t notice, but heavy cookers can prepend the timeout with a minus sign, making rlwrap hold back the prompt until it has been cooked (&quot;patient mode&quot;). This will prevent flashing of the prompt, but it will also interfere with long output lines and make switches from direct to readline mode less reliable. Default timeout: 40 ms</p>
<dt> <code>-W, &#8211;polling </code></p>
<dd> EXPERIMENTAL: Wake up every <i>timeout</i> millisecs, where <i>timeout</i> is the same as for the -w (&#8211;wait-before-prompt) option, 40 ms by default. This is used to sense the slave&#8217;s interrupt character and ISIG flag and to adjust stdin&#8217;s terminal settings accordingly, even before you press a key. Try this option e.g. when CTRL-C acts differently on <i>command</i> with, and without, rlwrap.</p>
<dt> <code>-z, &#8211;filter <i>filter</i></code></p>
<dd> Use a filter to change <code>rlwrap</code>&#8216;s behaviour. A filter can be used to keep certain input out of the history, to change the prompt, to implement simple macros or programmable completion.. <code>rlwrap</code> comes with a special <code>perl</code> module (cf. <code><a href="//www.systutorials.com/docs/linux/man/3pm-RlwrapFilter/">RlwrapFilter</a>(3pm)</code>) for easy filter writing. A number of example filters are installed in the directory /usr/share/rlwrap/filters. &quot;rlwrap -z <i>filter</i>&quot; displays information about a filter, &quot;rlwrap -z listing&quot; lists all currently installed filters. If <i>filter</i> needs arguments, you should quote the whole filter command line: </p>
<pre>
    rlwrap -z 'filter args' command
</pre>
<p> If this command line contains shell metacharacters, <code>rlwrap</code> passes it to the system shell for parsing.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Run <code>nc</code> (netcat) with command-line editing and history</p>
<dd> <code>rlwrap nc</code></p>
<dt>Wrap <code>smbclient</code> (which uses readline itself), keep passwords out of the history and don&#8217;t wrap commands launched from smbclient (like <code>more</code>)</p>
<dd> <code>rlwrap -aPassword: -N smbclient //PEANUT/C</code></p>
<dt>Wrap <code>gauche</code> (a Scheme interpreter) with a bold blue prompt, enable multi-line editing (using .scm as filename extension) and don&#8217;t consider single quotes as quotes (so that the parentheses in e.g. (print &#8216;q) match)</p>
<dd> <code>rlwrap -pBlue -m -M .scm -q&#8221; gosh</code></p>
<dt>Get a list of all currently installed filters</p>
<dd> <code>rlwrap -z listing</code></p>
<dt>Get help for the filter <code>pipeto</code></p>
<dd> <code>rlwrap -z pipeto</code></p>
<dt>Wrap <code>sqlite3</code>, use the <code>pipeto</code> filter to be able to pipe the output of SQL commands through <code>grep</code> and/or <code>less</code>, complete (case-insensitively) on the SQL keywords in &#8216;sql_words&#8217;</p>
<dd> <code>rlwrap -a -z pipeto -i -f sql_words sqlite3 contacts.db</code></p>
<dt>In a shell script, use <code>rlwrap</code> in &#8216;one-shot&#8217; mode as a replacement for <code>read</code></p>
<dd> <code>order=$(rlwrap -pYellow -S&nbsp;<wbr>&#8216;Your pizza?&nbsp;<wbr>&#8216;&nbsp;<wbr>-H past_orders -P Margherita -o cat)</code> </p>
</dl>
<h2>DIRECT MODE AND READLINE MODE</h2>
<p> Most simple console commands put your terminal either in &quot;cooked&quot; or in &quot;raw&quot; mode. In cooked mode the terminal will wait until you press the ENTER key before handing the entire line to the program, in raw mode every key you press is handed down immediately. In cooked mode you generally can use the backspace key, but not the arrow keys, to edit your input. Most simple console commands use cooked mode whenever they want whole input lines, and raw mode when they want single keypresses. More sophisticated commands tend to use raw mode all the time; they may sometimes be rlwrappable with the <code>-a</code> (and <code>-N</code>) options. </p>
<p> When you <code>rlwrap</code> <i>command</i>, <code>rlwrap</code> will run it a in a separate session, with its own &quot;pseudo-terminal&quot; (pty), and monitor this pty to see whether the pty is in raw mode or in cooked mode. In the first case, <code>rlwrap</code> will copy all input and output directly between <i>command</i> and your terminal (&quot;direct mode&quot;). In the second case, <code>rlwrap</code> will use readline to edit your input (&quot;readline mode&quot;), and monitor <code>command</code>&#8216;s output &#8211; every last line that doesn&#8217;t end with a newline is a potential prompt. How it handles such a candidate prompt depends on its being in &quot;patient&quot; or &quot;impatient&quot; mode:</p>
<h2>PATIENT AND IMPATIENT MODE</h2>
<p> If <i>command</i> writes a lot of output, it tends to be written (and read) in &quot;chunks&quot;. Not all chunks will end with a newline, and we need to distinguish their last lines from real prompts, especially if we want to re-write (&quot;cook&quot;) prompts. <code>rlwrap</code> solves this (almost) by waiting a little, to see if there is more to come. &quot;A little&quot; is 40 msec by default, but this can be changed with the <code>-w</code> option. Normally <code>rlwrap</code> writes the suspected prompt as soon as it is received, replacing it with a &quot;cooked&quot; version afer the wait time. This is called &quot;impatient&quot; mode. If you don&#8217;t like the flashing effect (which can become annoying when you &quot;cook&quot; the prompt heavily) you can put <code>rlwrap</code> in &quot;patient mode&quot; by specifying a negative value with <code>-w</code> (e.g. -w -40). Rlwrap will then hold back the prompt and only print if after cooking.</p>
<h2>COOKING PROMPTS</h2>
<p> If and when <code>rlwrap</code> decides that it has a prompt, it will perform a number of actions on it, depending on the given options: filtering (<code>-z</code>), substituting (<code>-S</code>) and colouring (<code>-p</code>), in this order. The resulting &quot;cooked&quot; prompt is then printed (after erasing the &quot;raw&quot; prompt, if necessary)</p>
<h2>SPECIAL KEYS</h2>
<dl>
<dt><code>Control + O</code></p>
<dd> Accept the current line, but don&#8217;t put it in the history list. This action has a <code>readline</code> command name <i>rlwrap-accept-line-and-forget</i></p>
<dt><code>Control + ^</code></p>
<dd> Use an external editor to edit the current input (this will only work if the -m option is set). This action has a <code>readline</code> command name <i>rlwrap-call-editor</i></dl>
<p> These special keys were chosen for no other reason than that they are not currently bound to any readline action. If you don&#8217;t like them, (or your window manager swallows them) they can be re-bound more sensibly by including lines like the following in your <code>~/.inputrc</code>: </p>
<pre>
   &quot;\M-\C-m&quot;: rlwrap-accept-line-and-forget # ESC-ENTER 
   &quot;\C-xe&quot;:   rlwrap-call-editor            # CTRL-x e 
</pre>
<p> cf. the <code><a href="/docs/linux/man/3-readline/">readline</a>(3)</code> manpage</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>RLWRAP_HOME</code>:</p>
<dd> directory in which the history and completion files are kept.</p>
<dt><code>RLWRAP_EDITOR</code> (or else <code>EDITOR</code>, or else <code>VISUAL</code>):</p>
<dd> editor to use for multi-line input. Example:</dl>
<pre>
    export RLWRAP_EDITOR=&quot;vi&nbsp;<wbr>+%L&quot;
    export RLWRAP_EDITOR=&quot;vim&nbsp;<wbr>'+call cursor(%L,%C)'&quot;
</pre>
<p> The first example above is the default; %L and %C are replaced by line and column numbers corresponding to the cursor position in <code>rlwrap</code>&#8216;s edit buffer</p>
<dl>
<dt><code>RLWRAP_FILTERDIR</code>:</p>
<dd> Any executable along your PATH can in theory be used as a filter, but because filters have to follow a rather outlandish protocol (cf. <code>RlwrapFilter (3)</code>) it is a good idea to keep them separate. This is why <code>rlwrap</code> adds a special filter directory to $PATH just before launching a filter. By default, this is /usr/share/rlwrap/filters, but $RLWRAP_FILTERDIR is used if set.</dl>
<h2>SIGNALS</h2>
<p> A number of signals are forwarded to <i>command</i>: HUP INT QUIT USR1 USR2 TERM and (by way of resizing <i>command</i>&#8216;s terminal) WINCH. Some care is taken to handle TSTP (usually a result of a CTRL-Z from the terminal) sensibly &#8211; for example, after suspending <code>rlwrap</code> in the middle of a line edit, continuing (by typing &#8216;fg&#8217;) will land you at the exact spot where you suspended it. </p>
<p> Filters that take more than 1 second to respond can be interrupted by a CTRL-C from the terminal (although <code>rlwrap</code> will not survive this) </p>
<p> If <i>command</i> changes the keystrokes that send a particular signal from the keyboard (like emacs, which uses CTRL-G instead of CTRL-C) <code>rlwrap</code> will do the same (but only after the next keystroke &#8211; use the <code>&#8211;polling</code> option to make rlwrap more transparent in this respect) </p>
<p> When <i>command</i> is killed by a signal, <code>rlwrap</code> will clean up, reset its signal handlers an then commit suicide by sending the same signal to itself. This means that your shell sees the same exit status as it would have seen without <code>rlwrap</code>. </p>
<h2>REDIRECTION</h2>
<p> When the standard input is not a terminal, editing input doesn&#8217;t make sense, so <code>rlwrap</code> will ignore all options and simply execute <i>command</i>. When stdout (or stderr) is not a terminal, rlwrap will re-open it to /dev/tty (the users terminal) after it has started <i>command</i>, so that <i>command</i>&#8216;s output is redirected as expected, but keyboard input and <code>rlwrap</code> error messages are still visible. </p>
<p> The upshot of this is that <code>rlwrap</code> <i>command</i> behaves more or less like <i>command</i> when redirecting. </p>
<h2>EXIT STATUS</h2>
<p> non-zero after a <code>rlwrap</code> error, or else <i>command</i>&#8216;s exit status. <code>rlwrap</code> will always leave the terminal in a tidy state, even after a crash.</p>
<h2>FILES</h2>
<p> <code>rlwrap</code> expects its history and completion files in $RLWRAP_HOME, but uses .dotfiles in the user&#8217;s home directory if this variable is not set. This will quickly become messy if you use <code>rlwrap</code> for many different commands.</p>
<dl>
<dt>$RLWRAP_HOME/<i>command</i>_history, ~/.<i>command</i>_history</p>
<dd> History for <i>command</i></p>
<dt>$RLWRAP_HOME/<i>command</i>_completions, ~/.<i>command</i>_completions</p>
<dd> Per-user completion word list for <i>command</i>. <code>rlwrap</code> never writes into this list, but one can combine <code>-l</code> and <code>-f</code> options to to simulate the effect of a <code>-r</code> option that works across invocations.</p>
<dt>/usr/share/rlwrap/completions/<i>command</i></p>
<dd> System-wide completion word list for <i>command</i>. This file is only consulted if the per-user completion word list is not found.</p>
<dt>$INPUTRC, ~/.inputrc</p>
<dd> Individual <code>readline</code> initialisation file (See <code>readline</code> (3) for its format). <code>rlwrap</code> sets its <i>application name</i> to <i>command</i> (this can be overridden by the <code>-C</code> option), enabling different behaviours for different commands. One could e.g. put the following lines in <code>~/.inputrc</code>:</p>
<dl>
<dt>
<dd>
<pre>
   $if coqtop
       set show-all-if-ambiguous On
   $endif
</pre>
<p> making <code>rlwrap</code> show all completions whenever it runs <code>coqtop</code></dl>
</dl>
<h2>BUGS and LIMITATIONS</h2>
<p> Though it is flexible, delivers the goods (readline functionality), and adheres to the Unix &quot;many small tools&quot; paradigm, <code>rlwrap</code> is a kludge. It cannot know anything about <i>command</i>&#8216;s internal state, which makes context-sensitive completion impossible. Using the readline library from within <i>command</i> is still the best option. </p>
<p> Also, because &quot;it takes two to tango&quot; there is no way for <code>rlwrap</code> to synchronise its internal state with <i>command</i>, resulting in a number of subtle race conditions, where e.g. <i>command</i> may have changed the state of its terminal before <code>rlwrap</code> has read <i>command</i> output that was written before the state change. You will notice these races especially on a busy machine and with heavy &quot;cooking&quot; and filtering, when suddenly (and unpredictably) promtps or command output are garbled or incorrectly coloured.<br />
&nbsp;<wbr>&nbsp;<wbr> <code>rlwrap</code> can try, but often fails to, handle prompts that contain control characters. A flter may be used to clean up the prompt. </p>
<h2>VERSION</h2>
<p> This manpage documents rlwrap version 0.42</p>
<h2>AUTHORS</h2>
<p> The readline library (written by Brian Fox and Chet Ramey) does all the hard work behind the scenes, the pty-handling code has been taken practically unchanged from rxvt-2.7.10 (currently maintained by Geoff C. Wing), and completion word lists are managed by Damian Ivereigh&#8217;s libredblack library. The few remaining lines of code were written by Hans Lub (hanslub42 [at] gmail.com).</p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/3-readline/">readline</a>(3), <a href="//www.systutorials.com/docs/linux/man/3pm-RlwrapFilter/">RlwrapFilter</a>(3pm)</code></p>
<dd>
</dl>
<h2>Index</h2>
