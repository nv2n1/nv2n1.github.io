---
title: "watch(1)"
name: "watch"
section: "1"
letter: "w"
url: "/docs/linux/man/1-watch/"
description: "watch – execute a program periodically, showing output fullscreen"
---

<h2 class="name">NAME</h2>
<p> watch &#8211; execute a program periodically, showing output fullscreen </p>
<h2>SYNOPSIS</h2>
<p> <code>watch</code> [<i>options</i>] <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> <code>watch</code> runs <i>command</i> repeatedly, displaying its output and errors (the first screenfull). This allows you to watch the program output change over time. By default, <i>command</i> is run every 2 seconds and <code>watch</code> will run until interrupted.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;differences</code>[=<i>permanent</i>]</p>
<dd> Highlight the differences between successive updates. If the optional <i>permanent</i> argument is specified then <code>watch</code> will show all changes since the first iteration.</p>
<dt><code>-n</code>, <code>&#8211;interval</code> <i>seconds</i></p>
<dd> Specify update interval. The command will not allow quicker than 0.1 second interval, in which the smaller values are converted. Both &#8216;.&#8217; and &#8216;,&#8217; work for any locales. The WATCH_INTERVAL environment can be used to persistently set a non-default interval (following the same rules and formatting).</p>
<dt><code>-p</code>, <code>&#8211;precise</code></p>
<dd> Make <code>watch</code> attempt to run <i>command</i> every <code>&#8211;interval</code> <i>seconds</i>. Try it with <code>ntptime</code> (if present) and notice how the fractional seconds stays (nearly) the same, as opposed to normal mode where they continuously increase.</p>
<dt><code>-t</code>, <code>&#8211;no-title</code></p>
<dd> Turn off the header showing the interval, command, and current time at the top of the display, as well as the following blank line.</p>
<dt><code>-b</code>, <code>&#8211;beep</code></p>
<dd> Beep if command has a non-zero exit.</p>
<dt><code>-e</code>, <code>&#8211;errexit</code></p>
<dd> Freeze updates on command error, and exit after a key press.</p>
<dt><code>-g</code>, <code>&#8211;chgexit</code></p>
<dd> Exit when the output of <i>command</i> changes.</p>
<dt><code>-c</code>, <code>&#8211;color</code></p>
<dd> Interpret ANSI color and style sequences.</p>
<dt><code>-x</code>, <code>&#8211;exec</code></p>
<dd> Pass <i>command</i> to <code><a href="/docs/linux/man/2-exec/">exec</a></code>(2) instead of <code>sh -c</code> which reduces the need to use extra quoting to get the desired effect.</p>
<dt><code>-w</code>, <code>&#8211;no-linewrap</code></p>
<dd> Turn off line wrapping. Long lines will be truncated instead of wrapped to the next line.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help text and exit.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Display version information and exit.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> Success.</p>
<dt><code>1</code></p>
<dd> Various failures.</p>
<dt><code>2</code></p>
<dd> Forking the process to watch failed.</p>
<dt><code>3</code></p>
<dd> Replacing child process stdout with write side pipe failed.</p>
<dt><code>4</code></p>
<dd> Command execution failed.</p>
<dt><code>5</code></p>
<dd> Closing child process write pipe failed.</p>
<dt><code>7</code></p>
<dd> IPC pipe creation failed.</p>
<dt><code>8</code></p>
<dd> Getting child process return value with <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) failed, or command exited up on error.</p>
<dt><code>other</code></p>
<dd> The watch will propagate command exit status as child exit status.</dl>
</dl>
<h2>ENVIRONMENT</h2>
<p> The behaviour of <code>watch</code> is affected by the following environment variables. </p>
<dl>
<dt><code>WATCH_INTERVAL</code></p>
<dd> Update interval, follows the same rules as the <code>&#8211;interval</code> command line option.</dl>
<h2>NOTES</h2>
<p> POSIX option processing is used (i.e., option processing stops at the first non-option argument). This means that flags after <i>command</i> don&#8217;t get interpreted by <code>watch</code> itself.</p>
<h2>BUGS</h2>
<p> Upon terminal resize, the screen will not be correctly repainted until the next scheduled update. All <code>&#8211;differences</code> highlighting is lost on that update as well. </p>
<p> Non-printing characters are stripped from program output. Use <code>cat -v</code> as part of the command pipeline if you want to see them. </p>
<p> Combining Characters that are supposed to display on the character at the last column on the screen may display one column early, or they may not display at all. </p>
<p> Combining Characters never count as different in <code>&#8211;differences</code> mode. Only the base character counts. </p>
<p> Blank lines directly after a line which ends in the last column do not display. </p>
<p> <code>&#8211;precise</code> mode doesn&#8217;t yet have advanced temporal distortion technology to compensate for a <i>command</i> that takes more than <code>&#8211;interval</code> <i>seconds</i> to execute. <code>watch</code> also can get into a state where it rapid-fires as many executions of <i>command</i> as it can to catch up from a previous executions running longer than <code>&#8211;interval</code> (for example, <code>netstat</code> taking ages on a DNS lookup).</p>
<h2>EXAMPLES</h2>
<p> To watch for mail, you might do</p>
<dl>
<dt>
<dd> watch -n 60 from</dl>
<p> To watch the contents of a directory change, you could use</p>
<dl>
<dt>
<dd> watch -d ls -l</dl>
<p> If you&#8217;re only interested in files owned by user joe, you might use</p>
<dl>
<dt>
<dd> watch -d &#8216;ls -l | fgrep joe&#8217;</dl>
<p> To see the effects of quoting, try these out</p>
<dl>
<dt>
<dd> watch echo $$<br />
 watch echo &#8216;$$&#8217;<br />
 watch echo &quot;&#8217;&quot;&#8217;$$&#8217;&quot;&#8217;&quot;</dl>
<p> To see the effect of precision time keeping, try adding <code>-p</code> to</p>
<dl>
<dt>
<dd> watch -n 10 sleep 1</dl>
<p> You can watch for your administrator to install the latest kernel with</p>
<dl>
<dt>
<dd> watch uname -r</dl>
<p> (Note that <code>-p</code> isn&#8217;t guaranteed to work across reboots, especially in the face of <code>ntpdate</code> (if present) or other bootup time-changing mechanisms) </p>
<h2>Index</h2>
