---
title: "watch-mimedefang(8)"
name: "watch-mimedefang"
section: "8"
letter: "w"
url: "/docs/linux/man/8-watch-mimedefang/"
description: "watch-mimedefang – Keep an eye on mimedefang-multiplexor"
---

<p>watch-mimedefang &#8211; Keep an eye on mimedefang-multiplexor</p>
<h2>Synopsis</h2>
<p><code>watch-mimedefang </code>[<i>options</i>] </p>
<h2>Description</h2>
<p><code>watch-mimedefang</code> is a Tk script which graphically displays the status of <code><a href="/docs/linux/man/8-mimedefang-multiplexor/">mimedefang-multiplexor</a></code>(8). Note that Tcl/Tk 8.0 or higher is required to run <code>watch-mimedefang</code>. </p>
<h2>Display</h2>
<p><code>watch-mimedefang</code>&#8216;s display is divided into three main areas, from top to bottom: </p>
<dl>
<dt><code>o</code></p>
<dd>The graph display shows six graphs representing various statistics about the multiplexor. </p>
<dt><code>o</code></p>
<dd>The control area shows the maximum number of slaves, number of busy slaves, and number of idle slaves. The &quot;Control Command&quot; text entry lets you monitor remote MIMEDefang servers; see &quot;REMOTE MONITORING&quot; for details. </p>
<p> The &quot;10s&quot;, &quot;1m&quot;, &quot;5m&quot; and &quot;10m&quot; checkboxes allow you to enable or disable the graphing of statistics averaged over the last 10 seconds, 1 minute, 5 minutes and 10 minutes. </p>
<p> The &quot;Reread Filters&quot; button forces the multiplexor to reread filter rules. The &quot;Quit&quot; button terminates <code>watch-mimedefang</code>. </p>
<dt><code>o</code></p>
<dd>The scale at the bottom lets you change the update interval (default 500ms). Be aware that frequent updating may make <code>watch-mimedefang</code> consume a significant fraction of CPU time. </p>
</dl>
<h2>The Graph Area</h2>
<p>The graph area contains six graphs: </p>
<dl>
<dt><code>o Busy Slaves</code></p>
<dd>This graph shows the number of busy slaves each time the statistics are sampled. </p>
<dt><code>o Slaves/scan</code></p>
<dd>This graph shows the average number of busy slaves each time a message was scanned. The red plot shows the average over the last ten seconds, the blue plot shows the average over the last minute, and the green and yellow plots show the average over the last five and ten minutes, respectively. </p>
<dt><code>o Latency (ms)</code></p>
<dd>This graph shows the average time taken by each SCAN command over the last ten seconds, one minute, five minutes and ten minutes. </p>
<dt><code>o Messages/s</code></p>
<dd>This graph shows the average number of messages per second that were scanned. </p>
<dt><code>o Activations/s</code></p>
<dd>This graph shows the average number of new slaves activated per second. </p>
<dt><code>o Reaps/s</code></p>
<dd>This graph shows the average number of slaves that have terminated per second. </p>
<p> If the Activations and Reaps increase significantly, it could indicate heavy load, or an error causing filters to terminate abnormally. </p>
<p> If only Activations increase, then it probably indicates a sudden increase in e-mail volume. </p>
<p> If only Reaps increase, then it probably indicates a quiet time just after a period of heavy mail volume. </p>
</dl>
<p> You can enable or disable the ten second, one minute, five minute or ten minute plots by clicking on the &quot;10s&quot;, &quot;1m&quot;, &quot;5m&quot; or &quot;10m&quot; checkbox.</p>
<h2>Remote Monitoring</h2>
<p>Running <code>watch-mimedefang</code> on your actual mail server poses two problems: You need Tcl/Tk and the X client libraries installed, and the CPU consumption of <code>watch-mimedefang</code> can be considerable. </p>
<p> A better method is to run <code>watch-mimedefang</code> on a desktop machine, but have it monitor the mail server with a remote session. </p>
<p> The best way to establish a remote session is via SSH. For example, if you are running MIMEDefang on &quot;mail.mydomain.net&quot;, you can type the following into the <code>Control Command</code> entry box and press enter: </p>
<pre> ssh root [at] mail.mydomain.net md-mx-ctrl</pre>
<p>You <i>must</i> have a public/private key for the target machine and you must be running ssh-agent or equivalent; you cannot use an ssh command that requires entry of a password or passphrase. </p>
<p> Assuming your SSH setup is correct, <code>watch-mimedefang</code> will open an SSH connection to mail.mydomain.net and exchange low-bandwith information over that session for monitoring purposes.</p>
<h2>Command-Line Options</h2>
<p><code>watch-mimedefang</code> accepts the following command-line options: </p>
<dl>
<dt><code>-command </code><i>cmd</i></p>
<dd>Use <i>cmd</i> as the control command. You may need to quote <i>cmd</i> </p>
<dt><code>-interval </code><i>msec</i></p>
<dd>Set the update interval to <i>msec</i> milliseconds. </p>
<dt><code>-10s </code><i>flag</i></p>
<dd>Enable the &quot;10s&quot; graph plot if <i>flag</i> is 1, or disable it if <i>flag</i> is 0. </p>
<dt><code>-1m </code><i>flag</i></p>
<dd>Enable the &quot;1m&quot; graph plot if <i>flag</i> is 1, or disable it if <i>flag</i> is 0. </p>
<dt><code>-5m </code><i>flag</i></p>
<dd>Enable the &quot;5m&quot; graph plot if <i>flag</i> is 1, or disable it if <i>flag</i> is 0. </p>
<dt><code>-10m </code><i>flag</i></p>
<dd>Enable the &quot;10m&quot; graph plot if <i>flag</i> is 1, or disable it if <i>flag</i> is 0. </p>
<dt><code>-title </code><i>string</i></p>
<dd>Add <i>string</i> to the title of the main window. </p>
<dt><code>-help</code></p>
<dd>Print usage information. </p>
</dl>
<h2>Example</h2>
<p>As an example, to monitor MIMEDefang on the machine &quot;mail.mydomain.net&quot; updating once a second, with the 5m and 10m plots turned off, use: </p>
<pre> watch-mimedefang -command 'ssh root [at] mail.mydomain.net md-mx-ctrl' \
 -interval 1000 -5m 0 -10m 0 -title &quot;mail&quot;</pre>
<h2>Author</h2>
<p><code>watch-mimedefang</code> was written by Dianne Skoll &lt;dfs [at] roaringpenguin.com&gt;. The <code>mimedefang</code> home page is <i><a rel="nofollow" href="http://www.mimedefang.org/">http://www.mimedefang.org/</a></i>.</p>
<h2>Permissions</h2>
<p><code>watch-mimedefang</code> uses <code>md-mx-ctrl</code>; therefore, it probably needs to be run as <i>root</i> or the same user as <code>mimedefang-multiplexor</code>, or (if you are monitoring a remote machine), the SSH connection must be done as root or the MIMEDefang user.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mimedefang-pl/">mimedefang.pl</a>(8), <a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a>(5), <a href="/docs/linux/man/8-mimedefang/">mimedefang</a>(8), <a href="/docs/linux/man/7-mimedefang-protocol/">mimedefang-protocol</a>(7), <a href="/docs/linux/man/8-md-mx-ctrl/">md-mx-ctrl</a>(8), <a href="/docs/linux/man/8-watch-multiple-mimedefangs/">watch-multiple-mimedefangs</a>(8) </p>
