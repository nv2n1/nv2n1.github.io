---
title: "multitail(1)"
name: "multitail"
section: "1"
letter: "m"
url: "/docs/linux/man/1-multitail/"
description: "MultiTail – browse through several files at once"
---

<h2>NAME</h2>
<p> MultiTail &#8211; browse through several files at once</p>
<h2>SYNOPSIS</h2>
<p> <code>MultiTail [</code><i>options</i><code>]</code> </p>
<p> options: <code>[-cs|-Cs|-c-] [-s] [-i] inputfile [-i anotherinputfile] [&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> The program <code>MultiTail</code> lets you view one or multiple files like the original tail program. The difference is that it creates multiple windows on your console (with ncurses). It can also monitor wildcards: if another file matching the wildcard has a more recent modification date, it will automatically switch to that file. That way you can, for example, monitor a complete directory of files. Merging of 2 or even more logfiles is possible. It can also use colors while displaying the logfiles (through regular expressions), for faster recognition of what is important and what not. It can also filter lines (again with regular expressions). It has interactive menus for editing given regular expressions and deleting and adding windows. One can also have windows with the output of shell scripts and other software. When viewing the output of external software, MultiTail can mimic the functionality of tools like &#8216;watch&#8217; and such. When new mail arrives for the current user, the statuslines will become green. To reset this &quot;mail has arrived&quot;-state, press &#8216; &#8216; (a space). For help at any time, press F1. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i file</code></p>
<dd> Select a file to monitor. You can have multiple <code>-i </code><i>file</i> parameters. You only need to add <code>-i </code><i>file</i> in front of a filename if the filename starts with a dash (&#8216;-&#8216;).</p>
<dt><code>-I file</code></p>
<dd> Same as <code>-i </code><i>file</i> but add the output to the previous window (so the output is merged).</p>
<dt><code>-iw file interval</code></p>
<dd> <code>-Iw file interval</code> Like &#8216;-i&#8217;/&#8217;-I&#8217; but expects the parameter to be a wildcard and the second(!) an interval. Initially MultiTail will start monitoring the first file with the most recent modification time. Every interval it will check if any new files were created (or modified) and start tailing that one. *Don&#8217;t forget* to put quotation marks around the filename as otherwhise the shell will try to substitute them!</p>
<dt><code>-l command</code></p>
<dd> Command to execute in a window. Parameter is the command. Do not forget to use &quot;&#8217;s if the external command needs parameter! (e.g. -l &quot;ping host&quot;).</p>
<dt><code>-L command</code></p>
<dd> Same as <code>-l</code> but add the output to the previous window (so the output is merged).</p>
<dt><code>-j</code></p>
<dd> Read from stdin (can be used only once as there is only 1 stdin).</p>
<dt><code>-J</code></p>
<dd> Same as <code>-j</code> but add the output to the previous window (so the output is merged).</p>
<dt><code>&#8211;mergeall</code></p>
<dd> Merge all of the following files into the same window (see &#8216;&#8211;no-mergeall&#8217;).</p>
<dt><code>&#8211;no-mergeall</code></p>
<dd> Stop merging all files into one window (see &#8216;&#8211;mergeall&#8217;);</p>
<dt><code>&#8211;no-repeat</code></p>
<dd> When the same line is repeated, it will be suppressed while printing a &quot;Last message repeated x times&quot; message.</p>
<dt><code>&#8211;mark-interval x</code></p>
<dd> Print every &#8216;x&#8217; seconds a mark-line when nothing else was printed.</p>
<dt><code>-q i path</code></p>
<dd> Check path for new files with interval &#8216;i&#8217;, all in new windows. One can enter paths here understood by the shell. E.g. &quot;/tmp/*&quot;. Note: do not forget to add quotes around the pathname to prevent the shell from parsing it!</p>
<dt><code>-Q i path</code></p>
<dd> Like -q: but merge them all in one window.</p>
<dt><code>&#8211;new-only</code></p>
<dd> For -q/-Q: only create windows for files created after MultiTail was started.</p>
<dt><code>&#8211;closeidle x</code></p>
<dd> Close windows when more then &#8216;x&#8217; seconds no new data was processed.</p>
<dt><code>-a x</code></p>
<dd> Write the output also to file &#8216;x&#8217; (like &#8216;tee&#8217;) AFTER it was filtered by MultiTail.</p>
<dt><code>-A x</code></p>
<dd> Write the output also to file &#8216;x&#8217; (like &#8216;tee&#8217;) BEFORE it was filtered by MultiTail.</p>
<dt><code>-g x</code></p>
<dd> Send the output also to command &#8216;x&#8217; AFTER it was filtered by MultiTail.</p>
<dt><code>-G x</code></p>
<dd> Send the output also to command &#8216;x&#8217; BEFORE it was filtered by MultiTail.</p>
<dt><code>-S</code></p>
<dd> Prepend merged output with subwindow-number.</p>
<dt><code>-t title</code></p>
<dd> With this switch, &quot;title&quot; is displayed in the statusline instead of the filename or commandline.</p>
<dt><code>-n number_of_lines</code></p>
<dd> Number of lines to tail initially. The default depends on the size of the terminal-window.</p>
<dt><code>-N number_of_lines</code></p>
<dd> Like -n but this parameter will be used for all files/commands you tail after this parameter.</p>
<dt><code>-r interval</code></p>
<dd> Restart the command (started with -l/-L) after it has exited. With interval you can set how long to sleep before restarting.</p>
<dt><code>-R interval</code></p>
<dd> Restarts a command like -r only this one shows the difference in output compared to the previous run.</p>
<dt><code>-rc / -Rc interval</code></p>
<dd> Like -r / -R but clears the window before each iteration.</p>
<dt><code>-h</code></p>
<dd> The help.</p>
<dt><code>-f</code></p>
<dd> Follow the following filename, not the descriptor.</p>
<dt><code>&#8211;follow-all</code></p>
<dd> For all files after this switch: follow the following filename, not the descriptor.</p>
<dt><code>-fr filter</code></p>
<dd> Use the predefined filter(s) from the configfile.</p>
<dt><code>-e</code></p>
<dd> Use the next regular expression on the following file.</p>
<dt><code>-ex</code></p>
<dd> Use regular expression on the following file and execute the command when it matches. The command gets as commandline parameter the whole matching line.</p>
<dt><code>-eX</code></p>
<dd> Like &#8216;-ex&#8217; but only give the matching substring as parameter. This requires a regular expression with &#8216;(&#8216; and &#8216;)&#8217;.</p>
<dt><code>-ec</code></p>
<dd> Use regular expression on the following file and display the matches.</p>
<dt><code>-eC</code></p>
<dd> Use regular expression on the following file but display everything and display the matches inverted.</p>
<dt><code>-E</code></p>
<dd> Use the next regular expression on the following files.</p>
<dt><code>-v</code></p>
<dd> Negate the next regular expression.</p>
<dt><code>-s x</code></p>
<dd> Splits the screen vertically in &#8216;x&#8217; columns.</p>
<dt><code>-sw x</code></p>
<dd> At what position to split the screen. e.g. &#8216;-sw 20,40,,10&#8217; (=4 columns)</p>
<dt><code>-sn x</code></p>
<dd> How many windows per column for vertical split (use with -s or -sw). e.g. &#8216;-sn 3,,2&#8217;.</p>
<dt><code>-wh x</code></p>
<dd> Sets the height of a window (advisory: if it won&#8217;t fit, the height is adjusted).</p>
<dt><code>-cS scheme</code></p>
<dd> Show the next given file using the colorscheme selected with &#8216;scheme&#8217; (as defined in multitail.conf).</p>
<dt><code>-CS scheme</code></p>
<dd> Show all following files using the colorscheme selected with &#8216;scheme&#8217; (as defined in multitail.conf).</p>
<dt><code>-csn</code></p>
<dd> Extra switch for the following switches; do not use reverse (inverted) colors.</p>
<dt><code>-cs</code></p>
<dd> Show the next given file in colors (syslog).</p>
<dt><code>-c</code></p>
<dd> Show the next given file in colors.</p>
<dt><code>-Cs</code></p>
<dd> Show all following files in color (through syslog-scheme).</p>
<dt><code>-C</code></p>
<dd> Show all following files in color.</p>
<dt><code>-Cf field_index delimiter</code></p>
<dd> Show all following files in color depending on field selected with field_index. Fields are delimited by the defined delimiter.</p>
<dt><code>-cf field_index delimiter</code></p>
<dd> Show the next file in color depending on field selected with field_index. Fields are delimited by the defined delimiter.</p>
<dt><code>-ci color</code></p>
<dd> Use a specific color. Usefull when merging multiple outputs.</p>
<dt><code>-cT terminalmode</code></p>
<dd> Interpret terminal codes. Only ANSI supported at this time.</p>
<dt><code>-c-</code></p>
<dd> Do NOT colorize the following file.</p>
<dt><code>-C-</code></p>
<dd> Do NOT colorize the following files.</p>
<dt><code>-ts</code></p>
<dd> Add a timestamp to each line (format is configurable in multitail.conf).</p>
<dt><code>-Z color</code></p>
<dd> Specify the color-attributes for the markerline.</p>
<dt><code>-T</code></p>
<dd> A timestamp will be placed in the markerline.</p>
<dt><code>-d</code></p>
<dd> Do NOT update statusline.</p>
<dt><code>-D</code></p>
<dd> Do not display a statusline at all.</p>
<dt><code>-du</code></p>
<dd> Put the statusline above the data window.</p>
<dt><code>-z</code></p>
<dd> Do not display &quot;window closed&quot; windows.</p>
<dt><code>-u</code></p>
<dd> Set screen updateinterval (for slow links).</p>
<dt><code>-m nlines</code></p>
<dd> Set buffersize Set <code>nlines</code> to 0 (zero) if you want no limits on the buffering.</p>
<dt><code>-mb x</code></p>
<dd> Set scrollback buffer size (in bytes, use xKB/MB/GB).</p>
<dt><code>-M nlines</code></p>
<dd> Set the buffersize on ALL following files.</p>
<dt><code>-p x [y]</code></p>
<dd> Set linewrap: a = print everything including linewrap. l = just show everything starting at the left until the rightside of the window is reached. r = show everything starting from the right of the line. s = show everything starting with the processname. S = show everything starting after the processname. o = show everything starting at offset &#8216;y&#8217;.</p>
<dt><code>-P x [y]</code></p>
<dd> Like -p but for all following windows.</p>
<dt><code>-ke x</code></p>
<dd> Strip parts of the input using regular expression &#8216;x&#8217;.</p>
<dt><code>-kr x y</code></p>
<dd> Strip parts of the input starting at offset x and ending (not including!) offset y.</p>
<dt><code>-kc x y</code></p>
<dd> Strip parts of the input: strip column &#8216;y&#8217; with delimiter &#8216;x&#8217;.</p>
<dt><code>-ks x</code></p>
<dd> Use editscheme &#8216;x&#8217; from configfile.</p>
<dt><code>-w</code></p>
<dd> Do not use colors.</p>
<dt><code>-b n</code></p>
<dd> Sets the TAB-width.</p>
<dt><code>&#8211;config filename</code></p>
<dd> Load the configuration from given filename.</p>
<dt><code>-x</code></p>
<dd> Set xterm-title: %f will be replaced with the last changed file, %h with the hostname, %l with the load of the system, %m with &quot;New mail!&quot; when the current user has new mail, %u with the current effective user, %t timestamp of last changed file, %% with a %</p>
<dt><code>-o configfile-item</code></p>
<dd> Proces a configurationfile item via the commandline in case you cannot edit the default configfile.</p>
<dt><code>&#8211;cont</code></p>
<dd> Reconnect lines with a &#8221; at the end.</p>
<dt><code>&#8211;mark-interval interval</code></p>
<dd> When nothing comes in, print a &#8216;&#8212;mark&#8212;&#8216; line every &#8216;interval&#8217; seconds.</p>
<dt><code>&#8211;mark-change</code></p>
<dd> When multiple files are merged an multitail switches between two windows, print a markerline with the filename.</p>
<dt><code>&#8211;no-mark-change</code></p>
<dd> Do NOT print the markerline when the file changes (overrides the configfile).</p>
<dt><code>&#8211;label text</code></p>
<dd> Put &quot;text&quot; in front of each line. Usefull when merging multiple files and/or commands.</p>
<dt><code>&#8211;retry</code></p>
<dd> Keep trying to open the following file if it is inaccessible.</p>
<dt><code>&#8211;retry-all</code></p>
<dd> Like &#8211;retry but for all following files.</p>
<dt><code>-cv x</code></p>
<dd> Use conversion scheme &#8216;x&#8217; (see multitail.conf).</p>
<dt><code>&#8211;basename</code></p>
<dd> Only display the filename (and not the path) in the statusline.</p>
<dt><code>-F file</code></p>
<dd> Use &#8216;file&#8217; as configfile (instead of default configfile).</p>
<dt><code>&#8211;no-load-global-config</code></p>
<dd> Do NOT load the global configfile.</p>
<dt><code>&#8211;beep-interval x</code></p>
<dd> Let the terminal beep for every x-th line processed. Press &#8216;i&#8217; in the main menu to see how many times it beeped.</p>
<dt><code>&#8211;bi x</code></p>
<dd> Like &#8216;&#8211;beep-interval&#8217; but only for current (sub-)window. Statistics on the number of beeps can be found in the statistics for this (sub-)window. Press &#8216;t&#8217; in the main menu.</p>
<dt><code>-H</code></p>
<dd> Show heartbeat (to keep your sessions alive).</p>
<dt><code>-V</code></p>
<dd> Show the version and exit. </p>
</dl>
<h2>KEYS</h2>
<p> You can press a couple of keys while the program runs. To see a list of them, press F1 (or ^h). You can press F1 (or ^h) at any time: it gives you context related information. Press &#8216;q&#8217; to exit the program. </p>
<h2>EXAMPLES</h2>
<p> See <a rel="nofollow" href="http://www.vanheusden.com/multitail/examples.html">http://www.vanheusden.com/multitail/examples.html</a> for more and other examples.</p>
<dl>
<dt><code>multitail /var/log/apache/access_log logfile -i -filestartingwithdatsh</code></p>
<dd> This creates three windows. One with the contents of /var/log/apache/access_log, one with the contents of logfile and so on.</p>
<dt><code>multitail -R 2 -l &quot;netstat -t&quot;</code></p>
<dd> This runs netstat every 2 seconds and then shows what has changed since the previous run. That way one can see new connections being made and closed connections fading away.</p>
<dt><code>multitail logfile -l &quot;ping 192.168.1.3&quot;</code></p>
<dd> This creates two windows. One with the contents of logfile, one with with the output of &#8216;ping 192.168.1.3&#8217;.</p>
<dt><code>multitail /var/log/apache/access_log -I /var/log/apache/error_log</code></p>
<dd> This creates <code>one</code> window with the contents of /var/log/apache/access_log <code>merged</code> with the contents of /var/log/apache/error_log.</p>
<dt><code>multitail -M 0 /var/log/apache/access_log -I /var/log/apache/error_log</code></p>
<dd> Same as previous example. This example will store all logged entries in a buffer so that you can later on browse through them (by pressing &#8216; <code>b</code><br />
&nbsp;<wbr>&#8216;). </p>
</dl>
<h2>BUGS</h2>
<p> As this program grew larger and larger over the time with new functionality sometimes added ad-hoc, some bugs may have been introduced. Please notify folkert [at] vanheusden.com if you find any. </p>
<p> Well, except for the resizing of your terminal window. The program might crash when doing such things. Upgrading the ncurses library to at least version 5.3 might help in that case. </p>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="http://www.vanheusden.com/multitail/">http://www.vanheusden.com/multitail/</a></code> </p>
<h2>NOTES</h2>
<p> This page describes <code>MultiTail</code> as found in the multitail-4.3.1 package; other versions may differ slightly. Mail corrections and additions to folkert [at] vanheusden.com. Report bugs in the program to folkert [at] vanheusden.com. </p>
<h2>Index</h2>
