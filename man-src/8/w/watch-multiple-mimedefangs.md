---
title: "watch-multiple-mimedefangs(8)"
name: "watch-multiple-mimedefangs"
section: "8"
letter: "w"
url: "/docs/linux/man/8-watch-multiple-mimedefangs/"
description: "watch-multiple-mimdefangs.tcl – Keep an eye on a cluster of MIMEDefang machines"
---

<p>watch-multiple-mimdefangs.tcl &#8211; Keep an eye on a cluster of MIMEDefang machines</p>
<h2>Synopsis</h2>
<p><code>watch-multiple-mimdefangs.tcl [-n] [-r] [-s] [-t] [-archive] </code><i>machine-1 machine-2 &#8230; machine-N</i> </p>
<h2>Description</h2>
<p><code>watch-multiple-mimdefangs.tcl</code> is a Tk script that graphically displays the status of <code><a href="/docs/linux/man/8-mimedefang-multiplexor/">mimedefang-multiplexor</a></code>(8) on a cluster of machines. Note that Tcl/Tk 8.4 or higher is required to run <code>watch-multiple-mimdefangs.tcl</code>. If you supply the <code>-archive</code> command-line option, then <code>watch-multiple-mimdefangs.tcl</code> logs the output of <code>md-mx-ctrl rawload</code> for each machine. The output for <i>machine_name</i> is logged in: $HOME/.watch-multiple-mimedefangs/<i>machine_name</i>/data. If you supply any of <code>-n</code>, <code>-r</code>, <code>-s</code> or <code>-t</code> options, then <code>watch-multiple-mimdefangs.tcl</code> uses the <code>rawload1</code> command rather than <code>rawload</code> command to read performance data. <i>Do not use these options unless all monitored machines are running MIMEDefang 2.74 or newer!</i>. The <code>-n</code>, <code>-r</code>, <code>-s</code>, and <code>-t</code> options enable monitoring of scan times, filter_relay times, filter_sender times and filter_recipient times, respectively. </p>
<h2>Prerequisites</h2>
<p>To use <code>watch-multiple-mimdefangs.tcl</code> to monitor a cluster of machines, you need the following prerequisites: </p>
<dl>
<dt><code>o</code></p>
<dd>A UNIX-like machine with Tcl/Tk 8.4, the X window system and an SSH client. You also need &quot;xterm&quot; to use some of the features. </p>
<dt><code>o</code></p>
<dd>The ability to SSH <i>as root</i> to all of the machines you want to monitor. Ideally, you should be using the SSH agent so that you can SSH to the monitored machines as root without being prompted for a password or pass phrase. </p>
<dt><code>o</code></p>
<dd>The program <code>md-mx-ctrl</code> on root&#8217;s path on all the machines you want to monitor. </p>
</dl>
<h2>Display</h2>
<p>For each machine specified on the command line, <code>watch-multiple-mimdefangs.tcl</code> creates a chart with five columns. The columns are: </p>
<dl>
<dt><code>o</code></p>
<dd>A button with the name of the machine. Clicking the button pops up a menu that lets you take various actions, as described later. If all slaves on the machine are busy, the button turns yellow. </p>
<dt><code>o</code></p>
<dd>A label showing the number of busy slaves in the form &quot;busy/total&quot;, where total is the total number of slaves. </p>
<dt><code>o</code></p>
<dd>A label showing the average number of messages per second over the last 10 seconds. </p>
<dt><code>o</code></p>
<dd>A label showing the average number of milliseconds per scan over the last 10 seconds. </p>
<dt><code>o</code></p>
<dd>A chart that graphs the average number of busy slaves, the average number of messages per second and the average scan time in milliseconds, all averaged over the last 10 seconds. </p>
</dl>
<h2>Machine Menu</h2>
<p>If you click on a machine name, a menu with three options pops up: </p>
<dl>
<dt><code>SSH</code></p>
<dd>Open an xterm session and ssh as root to the machine. </p>
<dt><code>Busy Slaves</code></p>
<dd>Monitor the busy slaves on the machine. If you click on the process-ID of a slave, an xterm will open up and the command &quot;strace -s 100 -t -p <i>pid</i>&quot; will be executed on the remote machine. This is Linux-specific, but you can edit <code>watch-multiple-mimdefangs.tcl</code> to replace the command with your particular system&#8217;s command for tracing system calls. </p>
<dt><code>Delete</code></p>
<dd>Remove the machine from the list of machines being monitored. </p>
</dl>
<h2>Adding A Machine</h2>
<p>If you need to add a machine to the display, simply type the name of the machine in the &quot;Add Machine:&quot; box and press Enter.</p>
<h2>Author</h2>
<p><code>watch-multiple-mimdefangs.tcl</code> was written by Dianne Skoll.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mimedefang-pl/">mimedefang.pl</a>(8), <a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a>(5), <a href="/docs/linux/man/8-mimedefang/">mimedefang</a>(8), <a href="/docs/linux/man/7-mimedefang-protocol/">mimedefang-protocol</a>(7), <a href="/docs/linux/man/8-md-mx-ctrl/">md-mx-ctrl</a>(8), <a href="/docs/linux/man/8-watch-mimedefang/">watch-mimedefang</a>(8) </p>
