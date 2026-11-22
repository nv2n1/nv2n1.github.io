---

title: "multitail(1)"
name: "multitail"
section: "1"
letter: "m"
url: "/docs/linux/man/1-multitail/"
description: "MultiTail – browse through several files at once"
---

<p> MultiTail &#8211; browse through several files at once</p>
<h2>SYNOPSIS</h2>
<p> <code>MultiTail [</code><i>options</i><code>]</code> </p>
<p> options: <code>[-cs|-Cs|-c-] [-s] [-i] inputfile [-i anotherinputfile] [&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> The program <code>MultiTail</code> lets you view one or multiple files like the original tail program. The difference is that it creates multiple windows on your console (with ncurses). It can also monitor wildcards: if another file matching the wildcard has a more recent modification date, it will automatically switch to that file. That way you can, for example, monitor a complete directory of files. Merging of 2 or even more logfiles is possible. It can also use colors while displaying the logfiles (through regular expressions), for faster recognition of what is important and what not. It can also filter lines (again with regular expressions). It has interactive menus for editing given regular expressions and deleting and adding windows. One can also have windows with the output of shell scripts and other software. When viewing the output of external software, MultiTail can mimic the functionality of tools like &#8216;watch&#8217; and such. When new mail arrives for the current user, the statuslines will become green. To reset this &quot;mail has arrived&quot;-state, press &#8216; &#8216; (a space). For help at any time, press F1. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i file</code></dt>
<dd> Select a file to monitor. You can have multiple <code>-i </code><i>file</i> parameters. You only need to add <code>-i </code><i>file</i> in front of a filename if the filename starts with a dash (&#8216;-&#8216;).</dd>
<dt><code>-I file</code></dt>
<dd> Same as <code>-i </code><i>file</i> but add the output to the previous window (so the output is merged).</dd>
<dt><code>-iw file interval</code></dt>
<dd> <code>-Iw file interval</code> Like &#8216;-i&#8217;/&#8217;-I&#8217; but expects the parameter to be a wildcard and the second(!) an interval. Initially MultiTail will start monitoring the first file with the most recent modification time. Every interval it will check if any new files were created (or modified) and start tailing that one. *Don&#8217;t forget* to put quotation marks around the filename as otherwhise the shell will try to substitute them!</dd>
<dt><code>-l command</code></dt>
<dd> Command to execute in a window. Parameter is the command. Do not forget to use &quot;&#8217;s if the external command needs parameter! (e.g. -l &quot;ping host&quot;).</dd>
<dt><code>-L command</code></dt>
<dd> Same as <code>-l</code> but add the output to the previous window (so the output is merged).</dd>
<dt><code>-j</code></dt>
<dd> Read from stdin (can be used only once as there is only 1 stdin).</dd>
<dt><code>-J</code></dt>
<dd> Same as <code>-j</code> but add the output to the previous window (so the output is merged).</dd>
<dt><code>&#8211;mergeall</code></dt>
<dd> Merge all of the following files into the same window (see &#8216;&#8211;no-mergeall&#8217;).</dd>
<dt><code>&#8211;no-mergeall</code></dt>
<dd> Stop merging all files into one window (see &#8216;&#8211;mergeall&#8217;);</dd>
<dt><code>&#8211;no-repeat</code></dt>
<dd> When the same line is repeated, it will be suppressed while printing a &quot;Last message repeated x times&quot; message.</dd>
<dt><code>&#8211;mark-interval x</code></dt>
<dd> Print every &#8216;x&#8217; seconds a mark-line when nothing else was printed.</dd>
<dt><code>-q i path</code></dt>
<dd> Check path for new files with interval &#8216;i&#8217;, all in new windows. One can enter paths here understood by the shell. E.g. &quot;/tmp/*&quot;. Note: do not forget to add quotes around the pathname to prevent the shell from parsing it!</dd>
<dt><code>-Q i path</code></dt>
<dd> Like -q: but merge them all in one window.</dd>
<dt><code>&#8211;new-only</code></dt>
<dd> For -q/-Q: only create windows for files created after MultiTail was started.</dd>
<dt><code>&#8211;closeidle x</code></dt>
<dd> Close windows when more then &#8216;x&#8217; seconds no new data was processed.</dd>
<dt><code>-a x</code></dt>
<dd> Write the output also to file &#8216;x&#8217; (like &#8216;tee&#8217;) AFTER it was filtered by MultiTail.</dd>
<dt><code>-A x</code></dt>
<dd> Write the output also to file &#8216;x&#8217; (like &#8216;tee&#8217;) BEFORE it was filtered by MultiTail.</dd>
<dt><code>-g x</code></dt>
<dd> Send the output also to command &#8216;x&#8217; AFTER it was filtered by MultiTail.</dd>
<dt><code>-G x</code></dt>
<dd> Send the output also to command &#8216;x&#8217; BEFORE it was filtered by MultiTail.</dd>
<dt><code>-S</code></dt>
<dd> Prepend merged output with subwindow-number.</dd>
<dt><code>-t title</code></dt>
<dd> With this switch, &quot;title&quot; is displayed in the statusline instead of the filename or commandline.</dd>
<dt><code>-n number_of_lines</code></dt>
<dd> Number of lines to tail initially. The default depends on the size of the terminal-window.</dd>
<dt><code>-N number_of_lines</code></dt>
<dd> Like -n but this parameter will be used for all files/commands you tail after this parameter.</dd>
<dt><code>-r interval</code></dt>
<dd> Restart the command (started with -l/-L) after it has exited. With interval you can set how long to sleep before restarting.</dd>
<dt><code>-R interval</code></dt>
<dd> Restarts a command like -r only this one shows the difference in output compared to the previous run.</dd>
<dt><code>-rc / -Rc interval</code></dt>
<dd> Like -r / -R but clears the window before each iteration.</dd>
<dt><code>-h</code></dt>
<dd> The help.</dd>
<dt><code>-f</code></dt>
<dd> Follow the following filename, not the descriptor.</dd>
<dt><code>&#8211;follow-all</code></dt>
<dd> For all files after this switch: follow the following filename, not the descriptor.</dd>
<dt><code>-fr filter</code></dt>
<dd> Use the predefined filter(s) from the configfile.</dd>
<dt><code>-e</code></dt>
<dd> Use the next regular expression on the following file.</dd>
<dt><code>-ex</code></dt>
<dd> Use regular expression on the following file and execute the command when it matches. The command gets as commandline parameter the whole matching line.</dd>
<dt><code>-eX</code></dt>
<dd> Like &#8216;-ex&#8217; but only give the matching substring as parameter. This requires a regular expression with &#8216;(&#8216; and &#8216;)&#8217;.</dd>
<dt><code>-ec</code></dt>
<dd> Use regular expression on the following file and display the matches.</dd>
<dt><code>-eC</code></dt>
<dd> Use regular expression on the following file but display everything and display the matches inverted.</dd>
<dt><code>-E</code></dt>
<dd> Use the next regular expression on the following files.</dd>
<dt><code>-v</code></dt>
<dd> Negate the next regular expression.</dd>
<dt><code>-s x</code></dt>
<dd> Splits the screen vertically in &#8216;x&#8217; columns.</dd>
<dt><code>-sw x</code></dt>
<dd> At what position to split the screen. e.g. &#8216;-sw 20,40,,10&#8217; (=4 columns)</dd>
<dt><code>-sn x</code></dt>
<dd> How many windows per column for vertical split (use with -s or -sw). e.g. &#8216;-sn 3,,2&#8217;.</dd>
<dt><code>-wh x</code></dt>
<dd> Sets the height of a window (advisory: if it won&#8217;t fit, the height is adjusted).</dd>
<dt><code>-cS scheme</code></dt>
<dd> Show the next given file using the colorscheme selected with &#8216;scheme&#8217; (as defined in multitail.conf).</dd>
<dt><code>-CS scheme</code></dt>
<dd> Show all following files using the colorscheme selected with &#8216;scheme&#8217; (as defined in multitail.conf).</dd>
<dt><code>-csn</code></dt>
<dd> Extra switch for the following switches; do not use reverse (inverted) colors.</dd>
<dt><code>-cs</code></dt>
<dd> Show the next given file in colors (syslog).</dd>
<dt><code>-c</code></dt>
<dd> Show the next given file in colors.</dd>
<dt><code>-Cs</code></dt>
<dd> Show all following files in color (through syslog-scheme).</dd>
<dt><code>-C</code></dt>
<dd> Show all following files in color.</dd>
<dt><code>-Cf field_index delimiter</code></dt>
<dd> Show all following files in color depending on field selected with field_index. Fields are delimited by the defined delimiter.</dd>
<dt><code>-cf field_index delimiter</code></dt>
<dd> Show the next file in color depending on field selected with field_index. Fields are delimited by the defined delimiter.</dd>
<dt><code>-ci color</code></dt>
<dd> Use a specific color. Usefull when merging multiple outputs.</dd>
<dt><code>-cT terminalmode</code></dt>
<dd> Interpret terminal codes. Only ANSI supported at this time.</dd>
<dt><code>-c-</code></dt>
<dd> Do NOT colorize the following file.</dd>
<dt><code>-C-</code></dt>
<dd> Do NOT colorize the following files.</dd>
<dt><code>-ts</code></dt>
<dd> Add a timestamp to each line (format is configurable in multitail.conf).</dd>
<dt><code>-Z color</code></dt>
<dd> Specify the color-attributes for the markerline.</dd>
<dt><code>-T</code></dt>
<dd> A timestamp will be placed in the markerline.</dd>
<dt><code>-d</code></dt>
<dd> Do NOT update statusline.</dd>
<dt><code>-D</code></dt>
<dd> Do not display a statusline at all.</dd>
<dt><code>-du</code></dt>
<dd> Put the statusline above the data window.</dd>
<dt><code>-z</code></dt>
<dd> Do not display &quot;window closed&quot; windows.</dd>
<dt><code>-u</code></dt>
<dd> Set screen updateinterval (for slow links).</dd>
<dt><code>-m nlines</code></dt>
<dd> Set buffersize Set <code>nlines</code> to 0 (zero) if you want no limits on the buffering.</dd>
<dt><code>-mb x</code></dt>
<dd> Set scrollback buffer size (in bytes, use xKB/MB/GB).</dd>
<dt><code>-M nlines</code></dt>
<dd> Set the buffersize on ALL following files.</dd>
<dt><code>-p x [y]</code></dt>
<dd> Set linewrap: a = print everything including linewrap. l = just show everything starting at the left until the rightside of the window is reached. r = show everything starting from the right of the line. s = show everything starting with the processname. S = show everything starting after the processname. o = show everything starting at offset &#8216;y&#8217;.</dd>
<dt><code>-P x [y]</code></dt>
<dd> Like -p but for all following windows.</dd>
<dt><code>-ke x</code></dt>
<dd> Strip parts of the input using regular expression &#8216;x&#8217;.</dd>
<dt><code>-kr x y</code></dt>
<dd> Strip parts of the input starting at offset x and ending (not including!) offset y.</dd>
<dt><code>-kc x y</code></dt>
<dd> Strip parts of the input: strip column &#8216;y&#8217; with delimiter &#8216;x&#8217;.</dd>
<dt><code>-ks x</code></dt>
<dd> Use editscheme &#8216;x&#8217; from configfile.</dd>
<dt><code>-w</code></dt>
<dd> Do not use colors.</dd>
<dt><code>-b n</code></dt>
<dd> Sets the TAB-width.</dd>
<dt><code>&#8211;config filename</code></dt>
<dd> Load the configuration from given filename.</dd>
<dt><code>-x</code></dt>
<dd> Set xterm-title: %f will be replaced with the last changed file, %h with the hostname, %l with the load of the system, %m with &quot;New mail!&quot; when the current user has new mail, %u with the current effective user, %t timestamp of last changed file, %% with a %</dd>
<dt><code>-o configfile-item</code></dt>
<dd> Proces a configurationfile item via the commandline in case you cannot edit the default configfile.</dd>
<dt><code>&#8211;cont</code></dt>
<dd> Reconnect lines with a &#8221; at the end.</dd>
<dt><code>&#8211;mark-interval interval</code></dt>
<dd> When nothing comes in, print a &#8216;&#8212;mark&#8212;&#8216; line every &#8216;interval&#8217; seconds.</dd>
<dt><code>&#8211;mark-change</code></dt>
<dd> When multiple files are merged an multitail switches between two windows, print a markerline with the filename.</dd>
<dt><code>&#8211;no-mark-change</code></dt>
<dd> Do NOT print the markerline when the file changes (overrides the configfile).</dd>
<dt><code>&#8211;label text</code></dt>
<dd> Put &quot;text&quot; in front of each line. Usefull when merging multiple files and/or commands.</dd>
<dt><code>&#8211;retry</code></dt>
<dd> Keep trying to open the following file if it is inaccessible.</dd>
<dt><code>&#8211;retry-all</code></dt>
<dd> Like &#8211;retry but for all following files.</dd>
<dt><code>-cv x</code></dt>
<dd> Use conversion scheme &#8216;x&#8217; (see multitail.conf).</dd>
<dt><code>&#8211;basename</code></dt>
<dd> Only display the filename (and not the path) in the statusline.</dd>
<dt><code>-F file</code></dt>
<dd> Use &#8216;file&#8217; as configfile (instead of default configfile).</dd>
<dt><code>&#8211;no-load-global-config</code></dt>
<dd> Do NOT load the global configfile.</dd>
<dt><code>&#8211;beep-interval x</code></dt>
<dd> Let the terminal beep for every x-th line processed. Press &#8216;i&#8217; in the main menu to see how many times it beeped.</dd>
<dt><code>&#8211;bi x</code></dt>
<dd> Like &#8216;&#8211;beep-interval&#8217; but only for current (sub-)window. Statistics on the number of beeps can be found in the statistics for this (sub-)window. Press &#8216;t&#8217; in the main menu.</dd>
<dt><code>-H</code></dt>
<dd> Show heartbeat (to keep your sessions alive).</dd>
<dt><code>-V</code></dt>
<dd> Show the version and exit. </dd>
</dl>
<h2>KEYS</h2>
<p> You can press a couple of keys while the program runs. To see a list of them, press F1 (or ^h). You can press F1 (or ^h) at any time: it gives you context related information. Press &#8216;q&#8217; to exit the program. </p>
<h2>EXAMPLES</h2>
<p> See <a rel="nofollow" href="http://www.vanheusden.com/multitail/examples.html">http://www.vanheusden.com/multitail/examples.html</a> for more and other examples.</p>
<dl>
<dt><code>multitail /var/log/apache/access_log logfile -i -filestartingwithdatsh</code></dt>
<dd> This creates three windows. One with the contents of /var/log/apache/access_log, one with the contents of logfile and so on.</dd>
<dt><code>multitail -R 2 -l &quot;netstat -t&quot;</code></dt>
<dd> This runs netstat every 2 seconds and then shows what has changed since the previous run. That way one can see new connections being made and closed connections fading away.</dd>
<dt><code>multitail logfile -l &quot;ping 192.168.1.3&quot;</code></dt>
<dd> This creates two windows. One with the contents of logfile, one with with the output of &#8216;ping 192.168.1.3&#8217;.</dd>
<dt><code>multitail /var/log/apache/access_log -I /var/log/apache/error_log</code></dt>
<dd> This creates <code>one</code> window with the contents of /var/log/apache/access_log <code>merged</code> with the contents of /var/log/apache/error_log.</dd>
<dt><code>multitail -M 0 /var/log/apache/access_log -I /var/log/apache/error_log</code></dt>
<dd> Same as previous example. This example will store all logged entries in a buffer so that you can later on browse through them (by pressing &#8216; <code>b</code><br/>
&nbsp;<wbr>&#8216;). </dd>
</dl>
<h2>BUGS</h2>
<p> As this program grew larger and larger over the time with new functionality sometimes added ad-hoc, some bugs may have been introduced. Please notify folkert [at] vanheusden.com if you find any. </p>
<p> Well, except for the resizing of your terminal window. The program might crash when doing such things. Upgrading the ncurses library to at least version 5.3 might help in that case. </p>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="http://www.vanheusden.com/multitail/">http://www.vanheusden.com/multitail/</a></code> </p>
<h2>NOTES</h2>
<p> This page describes <code>MultiTail</code> as found in the multitail-4.3.1 package; other versions may differ slightly. Mail corrections and additions to folkert [at] vanheusden.com. Report bugs in the program to folkert [at] vanheusden.com. </p>
