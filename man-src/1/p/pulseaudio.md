---
title: "pulseaudio(1)"
name: "pulseaudio"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pulseaudio/"
description: "pulseaudio – The PulseAudio Sound System"
---

<h2 class="name">NAME</h2>
<p> pulseaudio &#8211; The PulseAudio Sound System </p>
<h2>SYNOPSIS</h2>
<p> <code>pulseaudio [</code><i>options</i><code>] </p>
<p> pulseaudio &#8211;help </p>
<p> pulseaudio &#8211;version </p>
<p> pulseaudio &#8211;dump-conf </p>
<p> pulseaudio &#8211;dump-modules </p>
<p> pulseaudio &#8211;dump-resample-methods </p>
<p> pulseaudio &#8211;cleanup-shm </p>
<p> pulseaudio &#8211;start </p>
<p> pulseaudio &#8211;kill </p>
<p> pulseaudio &#8211;check </code></p>
<h2>DESCRIPTION</h2>
<p> PulseAudio is a networked low-latency sound server for Linux, POSIX and Windows systems.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information.</p>
<dt><code>&#8211;dump-conf</code></p>
<dd> Load the daemon configuration file <i>daemon.conf</i> (see below), parse remaining configuration options on the command line and dump the resulting daemon configuration, in a format that is compatible with <i>daemon.conf</i>.</p>
<dt><code>&#8211;dump-modules</code></p>
<dd> List available loadable modules. Combine with <code>-v</code> for a more elaborate listing.</p>
<dt><code>&#8211;dump-resample-methods</code></p>
<dd> List available audio resamplers.</p>
<dt><code>&#8211;cleanup-shm</code></p>
<dd> Identify stale PulseAudio POSIX shared memory segments in <i>/dev/shm</i> and remove them if possible. This is done implicitly whenever a new daemon starts up or a client tries to connect to a daemon. It should normally not be necessary to issue this command by hand. Only available on systems with POSIX shared memory segments implemented via a virtual file system mounted to <i>/dev/shm</i> (e.g. Linux).</p>
<dt><code>&#8211;start</code></p>
<dd> Start PulseAudio if it is not running yet. This is different from starting PulseAudio without <code>&#8211;start</code> which would fail if PA is already running. PulseAudio is guaranteed to be fully initialized when this call returns. Implies <code>&#8211;daemonize</code>.</p>
<dt><code>-k | &#8211;kill</code></p>
<dd> Kill an already running PulseAudio daemon of the calling user (Equivalent to sending a SIGTERM).</p>
<dt><code>&#8211;check</code></p>
<dd> Return 0 as return code when the PulseAudio daemon is already running for the calling user, or non-zero otherwise. Produces no output on the console except for errors to stderr. </p>
<p> Note that a non-zero return value doesn&#8217;t necessarily mean that PulseAudio is not usable. Even if the server is not running, it may get automatically started via PulseAudio&#8217;s autospawning mechanism or systemd&#8217;s socket activation, or the environment might be such that checking for processes doesn&#8217;t work (for example, the running server might not show up in a container, even if the server is accessible via a socket). Also disabling PID files with <code>&#8211;use-pid-file=no</code> prevents <code>&#8211;check</code> from detecting running servers. </p>
<p> A more robust check in most situations would be to try establishing a client connection to the server. Unfortunately there&#8217;s currently no <code>&#8211;check-connection</code> option to replace <code>&#8211;check</code>, but running &quot;pactl info&quot; could be a pretty good substitute.</p>
<dt><code>&#8211;system</code><i>[=BOOL]</i></p>
<dd> Run as system-wide instance instead of per-user. Please note that this disables certain features of PulseAudio and is generally not recommended unless the system knows no local users (e.g. is a thin client). This feature needs special configuration and a dedicated UNIX user set up. It is highly recommended to combine this with <code>&#8211;disallow-module-loading</code> (see below).</p>
<dt><code>-D | &#8211;daemonize</code><i>[=BOOL]</i></p>
<dd> Daemonize after startup, i.e. detach from the terminal. Note that when running as a systemd service you should use <code>&#8211;daemonize=no</code> for systemd notification to work.</p>
<dt><code>&#8211;fail</code><i>[=BOOL]</i></p>
<dd> Fail startup when any of the commands specified in the startup script <i>default.pa</i> (see below) fails.</p>
<dt><code>&#8211;high-priority</code><i>[=BOOL]</i></p>
<dd> Try to acquire a high Unix nice level. This will only succeed if the calling user has a non-zero RLIMIT_NICE resource limit set (on systems that support this), or we&#8217;re configured to be run as system daemon (see <i>&#8211;system</i> above). It is recommended to enable this, since it is only a negligible security risk (see below).</p>
<dt><code>&#8211;realtime</code><i>[=BOOL]</i></p>
<dd> Try to acquire a real-time scheduling for PulseAudio&#8217;s I/O threads. This will only succeed if the calling user has a non-zero RLIMIT_RTPRIO resource limit set (on systems that support this), or rtkit is available and allows PulseAudio to enable real-time scheduling, or we are configured to be run as system daemon (see <i>&#8211;system</i> above).</p>
<dt><code>&#8211;disallow-module-loading</code><i>[=BOOL]</i></p>
<dd> Disallow module loading after startup. This is a security feature since it disallows additional module loading during runtime and on user request. It is highly recommended when <i>&#8211;system</i> is used (see above). Note however, that this breaks certain features like automatic module loading on hot plug.</p>
<dt><code>&#8211;disallow-exit</code><i>[=BOOL]</i></p>
<dd> Disallow user requested exit</p>
<dt><code>&#8211;exit-idle-time</code><i>=SECS</i></p>
<dd> Terminate the daemon after the last client quit and this time in seconds passed. Use a negative value to disable this feature. Defaults to 20. </p>
<p> When PulseAudio runs in the per-user mode and detects a login session, then any positive value will be reset to 0 so that PulseAudio will terminate immediately on logout. A positive value therefore has effect only in environments where there&#8217;s no support for login session tracking (or if the user is logged in without a session spawned, a.k.a. lingering). A negative value can still be used to disable any automatic exit. </p>
<p> When PulseAudio runs in the system mode, automatic exit is always disabled, so this option does nothing.</p>
<dt><code>&#8211;scache-idle-time</code><i>=SECS</i></p>
<dd> Unload autoloaded samples from the cache when they haven&#8217;t been used for the specified number of seconds.</p>
<dt><code>&#8211;log-level</code><i>[=LEVEL]</i></p>
<dd> If an argument is passed, set the log level to the specified value, otherwise increase the configured verbosity level by one. The log levels are numerical from 0 to 4, corresponding to <i>error</i>, <i>warn</i>, <i>notice</i>, <i>info</i>, <i>debug</i>. Default log level is <i>notice</i>, i.e. all log messages with lower log levels are printed: <i>error</i>, <i>warn</i>, <i>notice</i>.</p>
<dt><code>-v | &#8211;verbose</code></p>
<dd> Increase the configured verbosity level by one (see <code>&#8211;log-level</code> above). Specify multiple times to increase log level multiple times.</p>
<dt><code>&#8211;log-target</code><i>={auto,syslog,journal,stderr,file:PATH,newfile:PATH}</i></p>
<dd> Specify the log target. If set to <i>auto</i> (which is the default), then logging is directed to syslog when <code>&#8211;daemonize</code> is passed, otherwise to STDERR. If set to <i>journal</i> logging is directed to the systemd journal. If set to <i>file:PATH</i>, logging is directed to the file indicated by PATH. <i>newfile:PATH</i> is otherwise the same as file:PATH, but existing files are never overwritten. If the specified file already exists, a suffix is added to the file name to avoid overwriting.</p>
<dt><code>&#8211;log-meta</code><i>[=BOOL]</i></p>
<dd> Show source code location in log messages.</p>
<dt><code>&#8211;log-time</code><i>[=BOOL]</i></p>
<dd> Show timestamps in log messages.</p>
<dt><code>&#8211;log-backtrace</code><i>=FRAMES</i></p>
<dd> When FRAMES is greater than 0, log for each message a stack trace up to the number of specified stack frames.</p>
<dt><code>-p | &#8211;dl-search-path</code><i>=PATH</i></p>
<dd> Set the search path for dynamic shared objects (plugins).</p>
<dt><code>&#8211;resample-method</code><i>=METHOD</i></p>
<dd> Use the specified resampler by default (See <code>&#8211;dump-resample-methods</code> above for possible values).</p>
<dt><code>&#8211;use-pid-file</code><i>[=BOOL]</i></p>
<dd> Create a PID file. If this options is disabled it is possible to run multiple sound servers per user.</p>
<dt><code>&#8211;no-cpu-limit</code><i>[=BOOL]</i></p>
<dd> Do not install CPU load limiter on platforms that support it. By default, PulseAudio will terminate itself when it notices that it takes up too much CPU time. This is useful as a protection against system lockups when real-time scheduling is used (see below). Disabling this mechanism is useful when debugging PulseAudio with tools like <code><a href="/docs/linux/man/1-valgrind/">valgrind</a>(1)</code> which slow down execution.</p>
<dt><code>&#8211;disable-shm</code><i>[=BOOL]</i></p>
<dd> PulseAudio clients and the server can exchange audio data via POSIX or memfd shared memory segments (on systems that support this). If disabled PulseAudio will communicate exclusively over sockets. Please note that data transfer via shared memory segments is always disabled when PulseAudio is running with <code>&#8211;system</code> enabled (see above).</p>
<dt><code>&#8211;enable-memfd</code><i>[=BOOL]</i></p>
<dd> PulseAudio clients and the server can exchange audio data via memfds &#8211; the anonymous Linux Kernel shared memory mechanism (on kernels that support this). If disabled PulseAudio will communicate via POSIX shared memory.</p>
<dt><code>-L | &#8211;load</code><i>=&quot;MODULE ARGUMENTS&quot;</i></p>
<dd> Load the specified plugin module with the specified arguments.</p>
<dt><code>-F | &#8211;file</code><i>=FILENAME</i></p>
<dd> Run the specified script on startup. May be specified multiple times to specify multiple scripts to be run in order. Combine with <code>-n</code> to disable loading of the default script <i>default.pa</i> (see below).</p>
<dt><code>-C</code></p>
<dd> Open a command interpreter on STDIN/STDOUT after startup. This may be used to configure PulseAudio dynamically during runtime. Equivalent to <code>&#8211;load</code><i>=module-cli</i>.</p>
<dt><code>-n</code></p>
<dd> Don&#8217;t load default script file <i>default.pa</i> (see below) on startup. Useful in conjunction with <code>-C</code> or <code>&#8211;file</code>.</dl>
<h2>FILES</h2>
<p> <i>~/.config/pulse/daemon.conf</i>, <i>/etc/pulse/daemon.conf</i>: configuration settings for the PulseAudio daemon. If the version in the user&#8217;s home directory does not exist the global configuration file is loaded. See <code><a href="/docs/linux/man/5-pulse-daemon-conf/">pulse-daemon.conf</a>(5)</code> for more information. </p>
<p> <i>~/.config/pulse/default.pa</i>, <i>/etc/pulse/default.pa</i>: the default configuration script to execute when the PulseAudio daemon is started. If the version in the user&#8217;s home directory does not exist the global configuration script is loaded. See <code><a href="/docs/linux/man/5-default-pa/">default.pa</a>(5)</code> for more information. </p>
<p> <i>~/.config/pulse/client.conf</i>, <i>/etc/pulse/client.conf</i>: configuration settings for PulseAudio client applications. If the version in the user&#8217;s home directory does not exist the global configuration file is loaded. See <code><a href="/docs/linux/man/5-pulse-client-conf/">pulse-client.conf</a>(5)</code> for more information.</p>
<h2>SIGNALS</h2>
<p> <i>SIGINT, SIGTERM</i>: the PulseAudio daemon will shut down (Same as <code>&#8211;kill</code>). </p>
<p> <i>SIGHUP</i>: dump a long status report to STDOUT or syslog, depending on the configuration. </p>
<p> <i>SIGUSR1</i>: load module-cli, allowing runtime reconfiguration via STDIN/STDOUT. </p>
<p> <i>SIGUSR2</i>: load module-cli-protocol-unix, allowing runtime reconfiguration via a AF_UNIX socket. See <code><a href="/docs/linux/man/1-pacmd/">pacmd</a>(1)</code> for more information.</p>
<h2>UNIX GROUPS AND USERS</h2>
<p> Group <i>pulse-access</i>: if PulseAudio is running as a system daemon (see <code>&#8211;system</code> above) access is granted to members of this group when they connect via AF_UNIX sockets. If PulseAudio is running as a user daemon this group has no meaning. </p>
<p> User <i>pulse</i>, group <i>pulse</i>: if PulseAudio is running as a system daemon (see <code>&#8211;system</code> above) and is started as root the daemon will drop privileges and become a normal user process using this user and group. If PulseAudio is running as a user daemon this user and group has no meaning.</p>
<h2>REAL-TIME AND HIGH-PRIORITY SCHEDULING</h2>
<p> To minimize the risk of drop-outs during playback it is recommended to run PulseAudio with real-time scheduling if the underlying platform supports it. This decouples the scheduling latency of the PulseAudio daemon from the system load and is thus the best way to make sure that PulseAudio always gets CPU time when it needs it to refill the hardware playback buffers. Unfortunately this can be a security risk on some systems, since PulseAudio runs as user process, and giving realtime scheduling privileges to a user always comes with the risk that the user misuses it to lock up the system &#8212; which is possible since making a process real-time effectively disables preemption. To solve this problem, PulseAudio uses rtkit to safely acquire real-time scheduling when available. </p>
<p> If the risk of locking up the machine is considered too big to enable real-time scheduling, high-priority scheduling can be enabled instead (i.e. negative nice level). This can be enabled by passing <code>&#8211;high-priority</code> (see above) when starting PulseAudio and may also be enabled with the appropriate option in <i>daemon.conf</i>. Negative nice levels can only be enabled when the appropriate resource limit RLIMIT_NICE is set (see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a>(2)</code> for more information), possibly configured in <i>/etc/security/limits.conf</i>. A resource limit of 31 (corresponding with nice level -11) is recommended.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The PulseAudio client libraries check for the existence of the following environment variables and change their local configuration accordingly: </p>
<p> <i>$PULSE_SERVER</i>: the server string specifying the server to connect to when a client asks for a sound server connection and doesn&#8217;t explicitly ask for a specific server. The server string is a list of server addresses separated by whitespace which are tried in turn. A server address consists of an optional address type specifier (unix:, tcp:, tcp4:, tcp6:), followed by a path or host address. A host address may include an optional port number. A server address may be prefixed by a string enclosed in {}. In this case the following server address is ignored unless the prefix string equals the local hostname or the machine id (/etc/machine-id). </p>
<p> <i>$PULSE_SINK</i>: the symbolic name of the sink to connect to when a client creates a playback stream and doesn&#8217;t explicitly ask for a specific sink. </p>
<p> <i>$PULSE_SOURCE</i>: the symbolic name of the source to connect to when a client creates a record stream and doesn&#8217;t explicitly ask for a specific source. </p>
<p> <i>$PULSE_BINARY</i>: path of PulseAudio executable to run when server auto-spawning is used. </p>
<p> <i>$PULSE_CLIENTCONFIG</i>: path of file that shall be read instead of <i>client.conf</i> (see above) for client configuration. </p>
<p> <i>$PULSE_COOKIE</i>: path of file that contains the PulseAudio authentication cookie. Defaults to <i>~/.config/pulse/cookie</i>. </p>
<p> These environment settings take precedence &#8212; if set &#8212; over the configuration settings from <i>client.conf</i> (see above).</p>
<h2>AUTHORS</h2>
<p> The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pulse-daemon-conf/">pulse-daemon.conf</a>(5)</code>, <code><a href="/docs/linux/man/5-default-pa/">default.pa</a>(5)</code>, <code><a href="/docs/linux/man/5-pulse-client-conf/">pulse-client.conf</a>(5)</code>, <code><a href="/docs/linux/man/1-pacmd/">pacmd</a>(1)</code> </p>
<h2>Index</h2>
