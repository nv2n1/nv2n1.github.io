---
title: "fvwmperl(1)"
name: "fvwmperl"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmperl/"
description: "FvwmPerl – the fvwm perl manipulator and preprocessor"
---

<p>FvwmPerl &#8211; the fvwm perl manipulator and preprocessor </p>
<h2>Synopsis</h2>
<p>FvwmPerl should be spawned by <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1) for normal functionality. </p>
<p> To run this module, place this command somewhere in the configuration: </p>
<pre> Module FvwmPerl [params]</pre>
<p>or: </p>
<pre> ModuleSynchronize FvwmPerl [params]</pre>
<p>if you want to immediately start to send commands to FvwmPerl.</p>
<h2>Description</h2>
<p>This module is intended to extend fvwm commands with the perl scripting power.&nbsp;<wbr> It enables to embed perl expressions in the fvwm config files and construct fvwm commands.</p>
<h2>Invocation</h2>
<p>If you want to invoke the unique and persistent instanse of FvwmPerl, it is suggested to do this from the <i>StartFunction</i>.&nbsp;<wbr> Calling it from the top is also possible, but involves some issues not discussed here. </p>
<pre> AddToFunc StartFunction I Module FvwmPerl</pre>
<p>There are several command line switches: </p>
<p> <code>FvwmPerl</code> [ <code>&#8211;eval</code> line ] [ <code>&#8211;load</code> file ] [ <code>&#8211;preprocess</code> [ <code>&#8211;quote</code> char ] [ <code>&#8211;winid</code> wid ] [ <code>&#8211;cmd</code> ] [ <code>&#8211;nosend</code> ] [ <code>&#8211;noremove</code> ] [ line | file ] ] [ <code>&#8211;export</code> [names] ] [ <code>&#8211;stay</code> ] [ <code>&#8211;nolock</code> ] [ alias ] </p>
<p> Long switches may be abbreviated to short one-letter switches. </p>
<p> <code>-e</code>|<code>&#8211;eval</code> line &#8211; evaluate the given perl code </p>
<p> <code>-l</code>|<code>&#8211;load</code> file &#8211; evaluate perl code in the given file </p>
<p> <code>-p</code>|<code>&#8211;preprocess</code> [ file ] &#8211; preprocess the given fvwm config file </p>
<p> The following 5 options are only valid together with <code>&#8211;preprocess</code> option. </p>
<p> <code>-c</code>|<code>&#8211;cmd</code> line &#8211; an fvwm command to be preprocessed instead of file </p>
<p> <code>-q</code>|<code>&#8211;quote</code> char &#8211; change the default &#8216;%&#8217; quote </p>
<p> <code>-w</code>|<code>&#8211;winid</code> wid &#8211; set explicit window context (should begin with digit, may be in oct or hex form; this window id overwrites implicit window context if any) </p>
<p> <code>&#8211;nosend</code> &#8211; do not send the preprocessed file to <i>fvwm</i> for <code>Read</code>ing, the default is send. Useful for preprocessing non fvwm config files. </p>
<p> <code>&#8211;noremove</code> &#8211; do not remove the preprocessed file after sending it to <i>fvwm</i> for <code>Read</code>ing, the default is remove. Useful for debugging. </p>
<p> <code>-x</code>|<code>&#8211;export</code> [names] &#8211; define fvwm shortcut functions (by default, two functions named &#8220;Eval&#8221; and &#8220;.&#8221;).&nbsp;<wbr> This option implies <code>&#8211;stay</code>. </p>
<p> <code>-s</code>|<code>&#8211;stay</code> &#8211; continues an execution after <code>&#8211;eval</code>, <code>&#8211;load</code> or <code>&#8211;preprocess</code> are processed.&nbsp;<wbr> By default, the module is not persistent in this case, i.e. <code>&#8211;nostay</code> is assumed. </p>
<p> <code>&#8211;nolock</code> &#8211; when one of the 3 action options is given, this option causes unlocking <i>fvwm</i> immediately. By default the requested action is executed synchronously; this only makes difference when invoked like: </p>
<pre> ModuleSynchronous FvwmPerl --preprocess someconfig.ppp</pre>
<p>If <code>&#8211;nolock</code> is added here, <code>ModuleSynchronous</code> returns immediately. Note that <code>Module</code> returns immediately regardless of this option.</p>
<h2>Using Alias</h2>
<p>Aliases allow to have several module invocations and work separately with all invocations, here is an example: </p>
<pre> ModuleSynchronous FvwmPerl FvwmPerl-JustTest
 SendToModule FvwmPerl-JustTest eval $a = 2 + 2; $b = $a
 SendToModule FvwmPerl-JustTest eval cmd(&quot;Echo 2 + 2 = $b&quot;)
 KillModule FvwmPerl FvwmPerl-JustTest</pre>
<h2>Preprocessing Example</h2>
<p>One of the effective proprocessing solutions is to pass the whole fvwm configuration with embeded perl code to &#8220;FvwmPerl &#8211;preprocess&#8221;. An alternative approach is to write a perl script that produces fvwm commands and sends them for execution, this script may be loaded using &#8220;FvwmPerl &#8211;load&#8221;. There are hovewer intermediate solutions that preprocess only separate configuration lines (or alternatively, execute separate perl commands that produce fvwm commands). </p>
<p> The following code snippet adds ability of arithmetics and string scripting to certain lines that need this. To use this, you want to start FvwmPerl as your first command so that other commands may be asked to be preprosessed. </p>
<pre> ModuleSynchronize FvwmPerl
 AddToFunc .
 + I SendToModule FvwmPerl preprocess -c -- $*
 . Exec exec xterm -name xterm-%{++$i}% # use unique name
 . GotoDesk 0 %{ $[desk.n] + 1 }% # go to next desk
 . Exec exec %{ -x &quot;/usr/bin/X11/aterm&quot; ? &quot;aterm&quot; : &quot;xterm&quot; }% -sb
 # center a window
 Next (MyWindow) . Move \
 %{($WIDTH - $[w.width]) / 2}%p %{($HEIGHT - $[w.height]) / 2}%p
 . Exec exec xmessage %{2 + 2}% # simple calculator
 . %{main::show_message(2 + 2, &quot;Yet another Calculator&quot;); &quot;&quot;}%</pre>
<h2>Actions</h2>
<p>There are several actions that FvwmPerl may perform:</p>
<dl>
<dt><code>eval</code> perl-code</p>
<dd>Evaluate a line of perl code. </p>
<p> A special function <code>cmd(</code>&#8220;command&#8221;<code>)</code> may be used in perl code to send commands back to fvwm. </p>
<p> If perl code contains an error, it is printed to the standard error stream with the <i>[FvwmPerl][eval]:</i> header prepended.</p>
<dt><code>load</code> file-name</p>
<dd>Load a file of perl code. If the file is not fully qualified, it is searched in the user directory <tt>$FVWM_USERDIR</tt> (usually ~/.fvwm) and the system wide data directory <tt>$FVWM_DATADIR</tt>. </p>
<p> A special function <code>cmd(</code>&#8220;command&#8221;<code>)</code> may be used in perl code to send commands back to fvwm. </p>
<p> If perl code contains an error, it is printed to the standard error stream with the <i>[FvwmPerl][load]:</i> header prepended.</p>
<dt><code>preprocess</code> [-q|&#8211;quote char] [-c|&#8211;cmd] [<i>line</i> | <i>file</i>]</p>
<dd>Preprocess fvwm config <i>file</i> or (if &#8211;cmd is given) <i>line</i>. This file contains lines that are not touched (usually fvwm commands) and specially preformatted perl code that is processed and replaced. Text enclosed in <code>%{</code> &#8230; <code>}%</code> delimiters, that may start anywhere on the line and end anywhere on the same or another line, is perl code. </p>
<p> The <i>quote</i> parameter changes perl code delimiters.&nbsp;<wbr> If a single char is given, like &#8216;@&#8217;, the delimiters are <code>@{</code> &#8230; <code>}@</code>. If the given quote is 2 chars, like <code>&lt;&gt;</code>, the quotes are <code>&lt;{</code> &#8230; <code>}&gt;</code> </p>
<p> The perl code is substituted for the result of its evaluation. I.e. %{$a = &#8220;c&#8221;; ++$a}% is replaced with &#8220;d&#8221;. </p>
<p> The evaluation is unlike <code>eval</code> and <code>load</code> is done under the package PreprocessNamespace and without <i>use strict</i>, so you are free to use any variable names without fear of conflicts. Just don&#8217;t use uninitialized variables to mean undef or empty list (they may be in fact initialized by the previous preprocess action), and do a clean-up if needed. The variables and function in the <i>main</i> package are still available, like ::<i>cmd()</i> or ::<i>skip()</i>, but it is just not a good idea to access them while preprocessing. </p>
<p> There is a special function <code>include</code>(<i>file</i>) that loads a file, preprocesses it and returns the preprocessed result. Avoid recursion. </p>
<p> If any embedded perl code contains an error, it is printed to the standard error stream and prepended with the <i>[FvwmPerl][preprocess]:</i> header. The result of substitution is empty in this case. </p>
<p> The following variables may be used in the perl code: </p>
<p> <tt>$USER</tt>, <tt>$DISPLAY</tt>, <tt>$WIDTH</tt>, <tt>$HEIGHT</tt>, <tt>$FVWM_VERSION</tt>, <tt>$FVWM_MODULEDIR</tt>, <tt>$FVWM_DATADIR</tt>, <tt>$FVWM_USERDIR</tt> </p>
<p> The following line based directives are recognized when preprocessing. They are processed after the perl code (if any) is substituted.</p>
<dl>
<dd>
<dl>
<dt>%<code>Repeat</code> <i>count</i></p>
<dd>Causes the following lines to be repeated <i>count</i> times.</p>
<dt>%<code>ModuleConfig</code> <i>module-name</i> [ destroy ]</p>
<dd>Causes the following lines to be interpreted as the given module configuration. If &#8220;destroy&#8221; is specified the previous module configuration is destroyed first.</p>
<dt>%<code>Prefix</code> <i>prefix</i></p>
<dd>Prefixes the following lines with the quoted <i>prefix</i>.</p>
<dt>%<code>End</code> any-optional-comment</p>
<dd>Ends any of the directives described above, may be nested.</dl>
</dl>
<dl>
<dd>Examples: </p>
<pre> %Prefix &quot;AddToFunc SwitchToWindow I&quot;
 Iconify off
 WindowShade off
 Raise
 WarpToWindow 50 50
 %End
 %ModuleConfig FvwmPager destroy
 Colorset 0
 Font lucidasans-10
 DeskTopScale 28
 MiniIcons
 %End ModuleConfig FvwmPager
 %Prefix &quot;All (MyWindowToAnimate) ResizeMove &quot;
 100 100 %{($WIDTH - 100) / 2}% %{($HEIGHT - 100) / 2}%
 %Repeat %{$count}%
 br w+2c w+2c w-1c w-1c
 %End
 %Repeat %{$count}%
 br w-2c w-2c w+1c w+1c
 %End
 %End Prefix</pre>
<p>Additional preprocess parameters &#8211;nosend and &#8211;noremove may be given too. See their description at the top.</dl>
<dt><code>export</code> [<i>func-names</i>]</p>
<dd>Send to <i>fvwm</i> the definition of shortcut functions that help to activate different actions of the module (i.e. <code>eval</code>, <code>load</code> and <code>preprocess</code>). </p>
<p> Function names (<i>func-names</i>) may be separated by commas or/and whitespace. By default, two functions &#8220;Eval&#8221; and &#8220;.&#8221; are assumed. </p>
<p> The actual action defined in a function is guessed from the function name if possible, where function name &#8220;.&#8221; is reserved for <code>preprocess</code> action. </p>
<p> For example, any of these two fvwm commands </p>
<pre> SendToModule MyPerl export PerlEval,PP
 FvwmPerl --export PerlEval,PP MyPerl</pre>
<p>define the following two shortcut functions: </p>
<pre> DestroyFunc PerlEval
 AddToFunc I SendToModule MyPerl eval $*
 DestroyFunc PP
 AddToFunc I SendToModule MyPerl preprocess -c -- $*</pre>
</dl>
<p> These 4 actions may be requested in one of 3 ways: 1) in the command line when FvwmPerl is invoked (in this case FvwmPerl is short-lived unless <code>&#8211;stay</code> or <code>&#8211;export</code> is also given), 2) by sending the corresponding message in fvwm config using SendToModule, 3) by calling the corresponding perl function in perl code.</p>
<h2>Functions</h2>
<p>There are several functions that perl code may call:</p>
<dl>
<dt><code>cmd(</code><i>$fvwm_command</i><code>)</code></p>
<dd>In case of <code>eval</code> or <code>load</code> &#8211; send back to fvwm a string <i></i>$fvwm_command<i></i>. In case of <code>preprocess</code> &#8211; append a string <i></i>$fvwm_command<i></i> to the output of the embedded perl code.</p>
<dt><code>do_eval(</code><i>$perl_code</i><code>)</code></p>
<dd>This function is equivalent to the <code>eval</code> functionality on the string <i></i>$perl_code<i></i>, described above.</p>
<dt><code>load(</code><i>$filename</i><code>)</code></p>
<dd>This function is equivalent to the <code>load</code> functionality on the file <tt>$filename</tt>, described above.</p>
<dt><code>preprocess(</code><i>@params, [&quot;-c </i>$command<i>&quot;] [$filename]</i><code>)</code></p>
<dd>This function is equivalent to the <code>preprocess</code> functionality with the given parameters and the file <tt>$filename</tt> described above.</p>
<dt><code>export(</code><i>$func_names, [$do_unexport]</i><code>)</code></p>
<dd>This function is equivalent to the <code>export</code> functionality with the given <tt>$func_names</tt>, described above. May also <code>unexport</code> the function names if the second parameter is true. </p>
<p> Function names should be separated by commas or/and whitespace. If <i></i>$func_names<i></i> is empty then functions &#8220;Eval&#8221; and &#8220;.&#8221; are assumed.</p>
<dt>stop()</p>
<dd>Terminates the module.</p>
<dt>skip()</p>
<dd>Skips the rest of the event callback code, i.e. the module returns to listen to new module events.</p>
<dt>unlock()</p>
<dd>Unsynchronizes the event callback from fvwm. This may be useful to prevent deadlocks, i.e. usually fvwm kills the non-responding module if the event callback is not finished in <i>ModuleTimeout</i> seconds. This prevents it. </p>
<p> This example causes FvwmPerl to suspend its execution for one minute: </p>
<pre> SendModule FvwmPerl eval unlock(); sleep(60);</pre>
<p>However, verify that there is no way a new message is sent by fvwm while the module is busy, and fvwm stays locked on this new message for too long. See also the <code>detach</code> solution if you need long lasting operations.</p>
<dt>detach()</p>
<dd>Forks and detaches the rest of the event callback code from the main process. This may be useful to prevent killing the module if its event callback should take a long time to complete and it may be done in the detached child. The detached child may still send commands to fvwm (don&#8217;t rely on this), but not receive the events of course, it exits immediately after the callback execution is finished. </p>
<p> If you use <i>detach()</i>, better only send commands to fvwm in one process (the main one or the detached one), doing otherwise may often cause conflicts.</p>
<dt><code>show_message(</code>$msg, <tt>$title</tt>[, <tt>$use_stderr_too</tt>=1]<code>)</p>
<dd>Shows a dialog window with the given message, using whichever X tool is found in the system. </p>
<p> See FVWM::Module::Toolkit</code>::<code>show_message</code> for more information.</dl>
<h2>Variables</h2>
<p>There are several global variables in the <i>main</i> namespace that may be used in the perl code: </p>
<pre> $a, $b, ... $h
 @a, @b, ... @h
 %a, %b, ... %h</pre>
<p>They all are initialized to the empty value and may be used to store a state between different calls to FvwmPerl actions (<code>eval</code> and <code>load</code>). </p>
<p> If you need more readable variable names, either write &#8220;no strict &#8216;vars&#8217;;&#8221; at the start of every perl code or use a hash for this, like: </p>
<pre> $h{id} = $h{first_name} . &quot; &quot; . $h{second_name}</pre>
<p>or use a package name, like: </p>
<pre> @MyMenu::terminals = qw( xterm rxvt );
 $MyMenu::item_num = @MyMenu::terminals;</pre>
<p>There may be a configuration option to turn strictness on and off.</p>
<h2>Messages</h2>
<p>FvwmPerl may receive messages using the fvwm command SendToModule. The names, meanings and parameters of the messages are the same as the corresponding actions, described above. </p>
<p> Additionally, a message <code>stop</code> causes a module to quit. </p>
<p> A message <code>unexport</code> [<i>func-names</i>] undoes the effect of <code>export</code>, described in the <font SIZE="-1">ACTIONS</font> section. </p>
<p> A message <code>dump</code> dumps the contents of the changed variables (not yet).</p>
<h2>Examples</h2>
<p>A simple test: </p>
<pre> SendToModule FvwmPerl eval $h{dir} = $ENV{HOME}
 SendToModule FvwmPerl eval load($h{dir} . &quot;/test.fpl&quot;)
 SendToModule FvwmPerl load $[HOME]/test.fpl
 SendToModule FvwmPerl preprocess config.ppp
 SendToModule FvwmPerl export Eval,PerlEval,PerlLoad,PerlPP
 SendToModule FvwmPerl unexport PerlEval,PerlLoad,PerlPP
 SendToModule FvwmPerl stop</pre>
<p>The following example handles root backgrounds in fvwmrc. All these commands may be added to StartFunction. </p>
<pre> Module FvwmPerl --export PerlEval
 # find all background pixmaps for a later use
 PerlEval $a = $ENV{HOME} . &quot;/bg&quot;; \
 opendir DIR, $a; @b = grep { /xpm$/ } readdir(DIR); closedir DIR
 # build a menu of background pixmaps
 AddToMenu MyBackgrounds &quot;My Backgrounds&quot; Title
 PerlEval foreach $b (@b) \
 { cmd(&quot;AddToMenu MyBackgrounds '$b' Exec fvwm-root $a/$b&quot;) }
 # choose a random background to load on start-up
 PerlEval cmd(&quot;AddToFunc \
 InitFunction + I Exec exec fvwm-root $a/&quot; . $b[int(random(@b))])</pre>
<h2>Escaping</h2>
<p><code>SendToModule</code> just like any other fvwm commands expands several dollar prefixed variables.&nbsp;<wbr> This may clash with the dollars perl uses. You may avoid this by prefixing SendToModule with a leading dash. The following 2 lines in each pair are equivalent: </p>
<pre> SendToModule FvwmPerl eval $$d = &quot;$[DISPLAY]&quot;
 -SendToModule FvwmPerl eval $d = &quot;$ENV{DISPLAY}&quot;
 SendToModule FvwmPerl eval \
 cmd(&quot;Echo desk=$d, display=$$d&quot;)
 SendToModule FvwmPerl preprocess -c \
 Echo desk=%(&quot;$d&quot;)%, display=%{$$d}%</pre>
<p>Another solution to avoid escaping of special symbols like dollars and backslashes is to create a perl file in ~/.fvwm and then load it: </p>
<pre> SendToModule FvwmPerl load build-menus.fpl</pre>
<p>If you need to preprocess one command starting with a dash, you should precede it using &#8220;&#8211;&#8221;. </p>
<pre> # this prints the current desk, i.e. &quot;0&quot;
 SendToModule FvwmPerl preprocess -c Echo &quot;$%{$a = &quot;c&quot;; ++$a}%&quot;
 # this prints &quot;$d&quot;
 SendToModule FvwmPerl preprocess -c -- -Echo &quot;$%{&quot;d&quot;}%&quot;
 # this prints &quot;$d&quot; (SendToModule expands $$ to $)
 SendToModule FvwmPerl preprocess -c -- -Echo &quot;$$%{&quot;d&quot;}%&quot;
 # this prints &quot;$$d&quot;
 -SendToModule FvwmPerl preprocess -c -- -Echo &quot;$$%{&quot;d&quot;}%&quot;</pre>
<p>Again, it is suggested to put your command(s) into file and preprocess the file instead.</p>
<h2>Caveats</h2>
<p>FvwmPerl being written in perl and dealing with perl, follows the famous perl motto: &#8220;There&#8217;s more than one way to do it&#8221;, so the choice is yours. </p>
<p> Here are more pairs of equivalent lines: </p>
<pre> Module FvwmPerl --load &quot;my.fpl&quot; --stay
 Module FvwmPerl -e 'load(&quot;my.fpl&quot;)' -s
 SendToModule FvwmPerl preprocess --quote '@' my.ppp
 SendToModule FvwmPerl eval preprocess({quote =&gt; '@'}, &quot;my.ppp&quot;);</pre>
<p>Warning, you may affect the way FvwmPerl works by evaluating appropriate perl code, this is considered a feature not a bug.&nbsp;<wbr> But please don&#8217;t do this, write your own fvwm module in perl instead.</p>
<h2>See Also</h2>
<p>The <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1) man page describes all available commands. </p>
<p> Basically, in your perl code you may use any function or class method from the perl library installed with fvwm, see the man pages of perl packages <code>General::FileSystem</code>, <code>General::Parse</code> and <code>FVWM::Module</code>.</p>
<h2>Author</h2>
<p>Mikhael Goikhman &lt;migo [at] homemail.com&gt;.</p>
