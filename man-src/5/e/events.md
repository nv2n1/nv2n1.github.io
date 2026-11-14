---
title: "events(5)"
name: "events"
section: "5"
letter: "e"
url: "/docs/linux/man/5-events/"
description: "events – format of event files used by the upstart init system"
---

<p>events &#8211; format of event files used by the upstart init system</p>
<h2>Description</h2>
<p>upstart works on the basis of <code>event</code> files that describe jobs that should be managed. This includes the particulars about what binary or shell script code should executed while the job is running, and which events can cause the job to be started or stopped. </p>
<p> Event files are stored in the <i>/etc/event.d</i> directory.</p>
<h2>Syntax</h2>
<p>Event files can contain the following stanzaz. </p>
<dl>
<dt><code>exec &lt;command&gt; &lt;arguments&gt;</code></p>
<dd>When the event is started by <code>init</code>, execute the following arguments. </p>
<p> Example: exec /bin/dbus-daemon &#8211;system </p>
<dt><code>script &#8230;</code></p>
<dd>Like <code>exec</code> but instead of executing a single program, execute the following shell code. <code>script</code> sections are closed with a <code>end script</code> marker. </p>
<p> Example: </p>
<pre> script
 rm -f /var/run/sshd.pid
 sshd
 end script
Only one of <code>exec</code> and <code>script</code> can be used at a time. If both
are bspecifed, <code>exec</code> takes priority.
<dt><code>pre-start</code>
<dd>Execute the command/script before actually starting the process.
<code>pre-start</code> can be invoked as <code>pre-start exec</code> or <code>pre-start script</code>
in the same way that a start action can be handled by either
<code>exec</code> or <code>script</code>.
<dt><code>post-start</code>
<dd>Execute the command/script after starting the process.
The format is similar to <code>pre-start</code>.
<dt><code>pre-stop</code>
<dd>Execute the command/script before stopping the process.
The format is similar to <code>pre-start</code>.
<dt><code>post-stop</code>
<dd>Execute the command/script after stopping the process.
The format is similar to <code>pre-start</code>.
<dt><code>start on &lt;event&gt;</code>
<dd>Describes on what condition to start this job. Without this
section, the job can only be manually started with the
<code><a href="//www.systutorials.com/docs/linux/man/8-initctl/">initctl</a>(8)</code> command.
Examples:
 start on startup
 This starts immediately after boot.
 start on stopped rc3
 This starts when the 'rc3' event has stopped.
Events are matched via globbing. So a stanza of the form
 start on runlevel [2345]
would match any of runlevels 2, 3, 4, or 5.
<dt><code>stop on &lt;event&gt;</code>
<dd>Describes on what condition to stop this job. Without this
section, the job can only be manually stopped with the
<code>initctl</code> command.
Examples:
 stop on runlevel 0
 This stops the job when runlevel 0 is entered.
 stop on stopping dbus ok
 This stops the job when the 'dbus' job is stopped.
Events are matched via globbing. So a stanza of the form
 stop on runlevel [!5]
would match any runlevel other than 5.
<dt><code>daemon</code>
<dd>Sets the daemon flag for the job. This means that the job will
fork in the background and that its PID needs to be obtained.
<dt><code>respawn</code>
<dd>This sets the daemon, service, and respawn flags for the job.
The respawn flag means that the process will be restarted when
it ends.
<dt><code>respawn limit [count [timeout]]</code>
<dd>This configures respawn limits. Respawn limits only apply
if the <code>respawn</code> flag is set for the job; setting a limit
does not automatically set respawning capability. If the
process is respawned more than <i>count</i> times within an
interval of <i>timeout</i> seconds, the job will be stopped
automatically, andn ot restarted. The limit defaults to 10
times within 5 seconds.
Example: respawn limit 10 120
This sets the limit for respawn to ten times within two
minutes, the historical behavior for System V init.
<dt><code>service</code>
<dd><code>service</code> means that the job has reached its goal when running.
<code>service</code> is implied by the <code>respawn</code> flag.
<dt><code>instance</code>
<dd><code>instance</code> means that the job starts new instances every time
it is started, even if there is another instance running. It
is the converse of <code>daemon</code>.
<dt><code>kill timeout &lt;time&gt;</code>
<dd>Sets the time to wait between sending TERM and KILL signals to
<i>time</i> seconds.
<dt><code>normal exit &lt;status&gt;</code>
<dd>When used with <code>respawn</code> any exit codes denoted in <i>status</i> will
prevent a respawn of the process.
<dt><code>console {logged|output|owner|none}</code>
<dd>Describes what to do with the job's output. Valid values are:
<i>logged</i>
Redirect to logger. (the default setting)
<i>output</i>
Direct to the current stdout
<i>owner</i>
The process becomes the owner of the console, allowing it to
receive signals from the keyboard
<i>none</i>
Output is redirected to /dev/null
<dt><code>env &lt;name&gt;=&lt;value&gt;</code>
<dd>Sets an environment variable for the job.
Example: env LD_LIBRARY_PATH=/opt/app/lib
<dt><code>umask &lt;umask&gt;</code>
<dd>Sets the umask of the job to <i>umask</i>.
Example: umask 0755
<dt><code>nice &lt;value&gt;</code>
<dd>Sets the nice level of the job to <i>value</i>.
Example: nice 5
<dt><code>chroot &lt;path&gt;</code>
<dd>Changes the job's root directory to <i>path</i>.
Example: chroot /var/empty
<dt><code>chdir &lt;path&gt;</code>
<dd>Changes the working directory of the job to <i>path</i>.
Example: chdir /var/tmp
<dt><code>limit {as|core|cpu|data|fsize|memlock|msgqueue|nice|nofile|nproc|rss|rtprio|sigpending|stack} {unlimited|&lt;value&gt;}</code>
<dd>Changes the limit of the process to whatever is specfied.
Examples:
 limit nproc 10
 limit core unlimited
<dt><code>description &lt;text&gt;</code>
<dd>Describes the job. Not currently used by any <code><a href="//www.systutorials.com/docs/linux/man/8-init/">init</a>(8)</code> tools.
Example: descripton &quot;This is a test job.&quot;
<dt><code>author &lt;text&gt;</code>
<dd>Author of the job. Not currently used by any <code><a href="//www.systutorials.com/docs/linux/man/8-init/">init</a>(8)</code> tools.
Example: author &quot;Obi-wan Kennedy &lt;bidy [at] whitehouse.gov&gt;&quot;
<dt><code>version &lt;version&gt;</code>
<dd>Version of the job. Not currently used by any <code><a href="//www.systutorials.com/docs/linux/man/8-init/">init</a>(8)</code> tools.
Example: version &quot;0.0.0.0.1 test&quot;
<dt><code>emits &lt;signals&gt;</code>
<dd>Describes signals emitted by the job. Not currently used by
any <code><a href="//www.systutorials.com/docs/linux/man/8-init/">init</a>(8)</code> tools. For more information on signals, see the
<code><a href="//www.systutorials.com/docs/linux/man/8-initctl/">initctl</a>(8)</code> man page and the <code>emit</code> option.
Example: emits spam egg ham
</dl></pre>
<h2>Events</h2>
<p>A wide array of events can be emitted by the system (see <code><a href="/docs/linux/man/8-initctl/">initctl</a>(8)</code>) but the following events are generated by upstart itself, or are usually seen on a typical install. </p>
<dl>
<dt><code>stalled</code></p>
<dd>No jobs are running and no events are pending. </p>
<dt><code>control-alt-delete</code></p>
<dd>Control-Alt-Delete has been pressed. </p>
<dt><code>kbdrequest</code></p>
<dd>A kbdrequest event has occurred. </p>
<dt><code>power-status-changed</code></p>
<dd>Init received SIGPWR. </p>
<dt><code>starting &lt;job&gt;</code></p>
<dd>The given job is being started. </p>
<dt><code>started &lt;job&gt;</code></p>
<dd>The given job has successfully been started. </p>
<dt><code>stopping &lt;job&gt;</code></p>
<dd>The given job is being stopped. </p>
<dt><code>stopped &lt;job&gt;</code></p>
<dd>The given job has been stopped successfully. </p>
<dt><code>startup</code></p>
<dd>Emitted when the system boots. </p>
<dt><code>runlevel &lt;runlevel&gt;</code></p>
<dd>Init has been asked to move to the given runlevel.</dl>
<h2>Files</h2>
<p><i>/etc/event.d</i> The directory where event files are stored.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) <code><a href="/docs/linux/man/8-init/">init</a></code>(8) <code><a rel="nofollow" href="http://upstart.ubuntu.com/getting-started.html">http://upstart.ubuntu.com/getting-started.html</a></code> </p>
