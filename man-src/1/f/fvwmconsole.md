---
title: "fvwmconsole(1)"
name: "fvwmconsole"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmconsole/"
description: "FvwmConsole – an fvwm command input interface"
---

<p>FvwmConsole &#8211; an fvwm command input interface</p>
<h2>Synopsis</h2>
<p>Module FvwmConsole [options] </p>
<p> <i>FvwmConsole</i> can only be invoked by fvwm. Command line invocation of the <i>FvwmConsole</i> module will not work. </p>
<h2>Description</h2>
<p>FvwmConsole allows the user to type fvwm configuration commands interactively, and have them executed immediately. This tool is particularly useful for testing new configuration ideas, or for implementing temporary changes to your environment. </p>
<h2>Invocation</h2>
<p>FvwmConsole must be spawned as a module by fvwm. FvwmConsole takes all <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1) options. </p>
<p> FvwmConsole can be invoked by inserting the line &#8216;Module FvwmConsole&#8217; in the .fvwm2rc file. This can be placed on a line by itself, if FvwmConsole is to be spawned during fvwm&#8217;s initialization, or can be bound to a menu or mouse button or keystroke to invoke it later. </p>
<h2>Configuration Options</h2>
<p>FvwmConsole uses <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1). All resources set for xterm are inherited unless overridden by command line options. </p>
<dl>
<dd>Module FvwmConsole -g 40&#215;10 -fg black -bg green3</dl>
<p> A different terminal emulator can be specified with the -terminal option. However, only terminal programs that understand the options -name, -title and -e can be used. </p>
<dl>
<dd>Module FvwmConsole -terminal rxvt</dl>
<p> Previous versions of FvwmConsole supported a -e option to choose a different front-end. Although this option is still provided for backwards compatibility its use is discouraged unless you know exactly what you are doing. </p>
<dl>
<dd>Module FvwmConsole -e FvwmConsoleC.pl</dl>
<p> (see <i><a href="/docs/linux/man/1-fvwmconsolec-pl/">FvwmConsoleC.pl</a></i>(1)). </p>
<p> Also X resources can be set in your ~/.Xdefaults file: </p>
<dl>
<dd>FvwmConsole*VT100*geometry: 40&#215;4<br />
 FvwmConsole*font: 7&#215;14</dl>
<h2>Command Editing</h2>
<p>There are a few options. If the GNU readline library is available, it can be used. </p>
<p> If Perl5 is installed, FvwmConsoleC.pl can be used as a command editor. This can be accomplished by either copying FvwmConsoleC.pl to fvwmlib directory as FvwmConsoleC or invoking FvwmConsole with -e option. For example: </p>
<dl>
<dd>Module FvwmConsole -e FvwmConsoleC.pl</dl>
<p> If neither one is installed, a simple input reading function which doesn&#8217;t have editing capabilities is used. </p>
<p> GNU readline and FvwmConsoleC.pl have some frequent used commands in common as default. These commands are similar to emacs. For more details, refer GNU readline man and info pages, and FvwmConsoleC.pl man page. </p>
<dl>
<dd>
<dl>
<dt>Ctrl-A</p>
<dd>&#8211; beginning of line</p>
<dt>Ctrl-B</p>
<dd>&#8211; previous char</p>
<dt>Ctrl-D</p>
<dd>&#8211; delete char</p>
<dt>Ctrl-E</p>
<dd>&#8211; end of line</p>
<dt>Ctrl-F</p>
<dd>&#8211; next char</p>
<dt>Ctrl-H</p>
<dd>&#8211; backspace</p>
<dt>Ctrl-K</p>
<dd>&#8211; erase to the end of line</p>
<dt>Ctrl-N</p>
<dd>&#8211; next line</p>
<dt>Ctrl-P</p>
<dd>&#8211; previous line</p>
<dt>Ctrl-R</p>
<dd>&#8211; search reverse</p>
<dt>Ctrl-U</p>
<dd>&#8211; delete line</p>
<dt>Meta-B</p>
<dd>&#8211; previous word</p>
<dt>Meta-F</p>
<dd>&#8211; next word</p>
<dt>Esc &lt;</p>
<dd>&#8211; beginning of history</p>
<dt>Esc &gt;</p>
<dd>&#8211; end of history</dl>
</dl>
<h2>Exiting</h2>
<p>FvwmConsole can be stopped by entering the EOF character (usually CTRL-D). </p>
<p> <code>Note!</code> Do not use the &quot;quit&quot; command, as this is an fvwm builtin: typing &quot;quit&quot; at the FvwmConsole command line will cause fvwm to exit. </p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1), <i><a href="/docs/linux/man/1-fvwmconsolec-pl/">FvwmConsoleC.pl</a></i>(1), GNU Readline library </p>
<h2>Author</h2>
<p>FvwmConsole is the original work of Toshi Isogai.</p>
