---
title: "pulse-cli-syntax(5)"
name: "pulse-cli-syntax"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pulse-cli-syntax/"
description: "pulse-cli-syntax – PulseAudio Command Line Interface Syntax"
---

<p>pulse-cli-syntax &#8211; PulseAudio Command Line Interface Syntax</p>
<h2>Synopsis</h2>
<p><i>~/.config/pulse/default.pa</i><code> </p>
<p> </code><i>/etc/pulse/default.pa</i><code> </p>
<p> </code><i>/etc/pulse/system.pa</i></p>
<h2>Description</h2>
<p>PulseAudio provides a simple command line language used by configuration scripts, the pacmd interactive shell, and the modules module-cli and module-cli-protocol-{unix,tcp}. Empty lines and lines beginning with a hashmark (#) are silently ignored. Several commands are supported. </p>
<p> Note that any boolean arguments can be given positively as &#8216;1&#8217;, &#8216;t&#8217;, &#8216;y&#8217;, &#8216;true&#8217;, &#8216;yes&#8217; or &#8216;on&#8217;. Likewise, negative values can be given as &#8216;0&#8217;, &#8216;f&#8217;, &#8216;n&#8217;, &#8216;false&#8217;, &#8216;no&#8217; or &#8216;off&#8217;. Case is ignored.</p>
<h2>General Commands</h2>
<dl>
<dt><code>help</code></p>
<dd>Show a quick help on the commands available.</dl>
<h2>Status Commands</h2>
<dl>
<dt><code>list-modules</code></p>
<dd>Show all currently loaded modules with their arguments.</p>
<dt><code>list-cards</code></p>
<dd>Show all currently registered cards</p>
<dt><code>list-sinks</code> or <code>list-sources</code></p>
<dd>Show all currently registered sinks (resp. sources).</p>
<dt><code>list-clients</code></p>
<dd>Show all currently active clients.</p>
<dt><code>list-sink-inputs</code> or <code>list-source-outputs</code></p>
<dd>Show all currently active inputs to sinks a.k.a. playback streams (resp. outputs of sources a.k.a. recording streams).</p>
<dt><code>stat</code></p>
<dd>Show some simple statistics about the allocated memory blocks and the space used by them.</p>
<dt><code>info</code> or <code>ls</code> or <code>list</code></p>
<dd>A combination of all status commands described above (all three commands are synonyms).</dl>
<h2>Module Management</h2>
<dl>
<dt><code>load-module</code> <i>name</i> [<i>arguments&#8230;</i>]</p>
<dd>Load a module specified by its name and arguments. For most modules it is OK to be loaded more than once.</p>
<dt><code>unload-module</code> <i>index|name</i></p>
<dd>Unload a module, specified either by its index in the module list or its name.</p>
<dt><code>describe-module</code> <i>name</i></p>
<dd>Give information about a module specified by its name.</dl>
<h2>Volume Commands</h2>
<dl>
<dt><code>set-sink-volume|set-source-volume</code> <i>index|name</i> <i>volume</i></p>
<dd>Set the volume of the specified sink (resp. source). You may specify the sink (resp. source) either by its index in the sink/source list or by its name. The volume should be an integer value greater or equal than 0 (muted). Volume 65536 (0x10000) is &#8216;normal&#8217; volume a.k.a. 100%. Values greater than this amplify the audio signal (with clipping).</p>
<dt><code>set-sink-mute|set-source-mute</code> <i>index|name</i> <i>boolean</i></p>
<dd>Mute or unmute the specified sink (resp. source). You may specify the sink (resp. source) either by its index or by its name. The mute value is either 0 (not muted) or 1 (muted).</p>
<dt><code>set-sink-input-volume|set-source-output-volume</code> <i>index</i> <i>volume</i></p>
<dd>Set the volume of a sink input (resp. source output) specified by its index. The same volume rules apply as with set-sink-volume.</p>
<dt><code>set-sink-input-mute|set-source-output-mute</code> <i>index</i> <i>boolean</i></p>
<dd>Mute or unmute a sink input (resp. source output) specified by its index. The same mute rules apply as with set-sink-mute.</dl>
<h2>Configuration Commands</h2>
<dl>
<dt><code>set-default-sink|set-default-source</code> <i>index|name</i></p>
<dd>Make a sink (resp. source) the default. You may specify the sink (resp. source) by its index in the sink (resp. source) list or by its name. </p>
<p> Note that defaults may be overridden by various policy modules or by specific stream configurations.</p>
<dt><code>set-card-profile</code> <i>index|name</i> <i>profile-name</i></p>
<dd>Change the profile of a card.</p>
<dt><code>set-sink-port|set-source-port</code> <i>index|name</i> <i>port-name</i></p>
<dd>Change the profile of a sink (resp. source).</p>
<dt><code>set-port-latency-offset</code> <i>card-index|card-name</i> <i>port-name</i> <i>offset</i></p>
<dd>Change the latency offset of a port belonging to the specified card</p>
<dt><code>suspend-sink|suspend-source</code> <i>name|index</i> <i>true|false</i></p>
<dd>Suspend or resume the specified sink or source (which may be specified either by its name or index), depending whether true (suspend) or false (resume) is passed as last argument. Suspending a sink will pause all playback and suspending a source will pause all capturing. Depending on the module implementing the sink or source this might have the effect that the underlying device is closed, making it available for other applications to use. The exact behaviour depends on the module.</p>
<dt><code>suspend</code> <i>boolean</i></p>
<dd>Suspend all sinks and sources.</dl>
<h2>Moving Streams</h2>
<dl>
<dt><code>move-sink-input|move-source-output</code> <i>index</i> <i>sink-index|sink-name</i></p>
<dd>Move sink input (resp. source output) to another sink (resp. source).</dl>
<h2>Property Lists</h2>
<dl>
<dt><code>update-sink-proplist|update-source-proplist</code> <i>index|name</i> <i>properties</i></p>
<dd>Update the properties of a sink (resp. source) specified by name or index. The property is specified as e.g. device.description=&quot;My Preferred Name&quot;</p>
<dt><code>update-sink-input-proplist|update-source-output-proplist</code> <i>index</i> <i>properties</i></p>
<dd>Update the properties of a sink input (resp. source output) specified by index. The properties are specified as above.</dl>
<h2>Sample Cache</h2>
<dl>
<dt><code>list-samples</code></p>
<dd>Lists the contents of the sample cache.</p>
<dt><code>play-sample</code> <i>name</i> <i>sink-index|sink-name</i></p>
<dd>Play a sample cache entry to a sink.</p>
<dt><code>remove-sample</code> <i>name</i></p>
<dd>Remove an entry from the sample cache.</p>
<dt><code>load-sample</code> <i>name</i> <i>filename</i></p>
<dd>Load an audio file to the sample cache.</p>
<dt><code>load-sample-lazy</code> <i>name</i> <i>filename</i></p>
<dd>Create a new entry in the sample cache, but don&#8217;t load the sample immediately. The sample is loaded only when it is first used. After a certain idle time it is freed again.</p>
<dt><code>load-sample-dir-lazy</code> <i>path</i></p>
<dd>Load all entries in the specified directory into the sample cache as lazy entries. A shell globbing expression (e.g. *.wav) may be appended to the path of the directory to add.</dl>
<h2>Killing Clients/Streams</h2>
<dl>
<dt><code>kill-client</code> <i>index</i></p>
<dd>Remove a client forcibly from the server. There is no protection against the client reconnecting immediately.</p>
<dt><code>kill-sink-input|kill-source-output</code> <i>index</i></p>
<dd>Remove a sink input (resp. source output) forcibly from the server. This will not remove the owning client or any other streams opened by the same client from the server.</dl>
<h2>Log Commands</h2>
<dl>
<dt><code>set-log-level</code> <i>numeric-level</i></p>
<dd>Change the log level.</p>
<dt><code>set-log-meta</code> <i>boolean</i></p>
<dd>Show source code location in log messages.</p>
<dt><code>set-log-target</code> <i>target</i></p>
<dd>Change the log target (null, auto, journal, syslog, stderr, file:PATH, newfile:PATH).</p>
<dt><code>set-log-time</code> <i>boolean</i></p>
<dd>Show timestamps in log messages.</p>
<dt><code>set-log-backtrace</code> <i>num-frames</i></p>
<dd>Show backtrace in log messages.</dl>
<h2>Miscellaneous Commands</h2>
<dl>
<dt><code>play-file</code> <i>filename</i> <i>sink-index|sink-name</i></p>
<dd>Play an audio file to a sink.</p>
<dt><code>dump</code></p>
<dd>Dump the daemon&#8217;s current configuration in CLI commands.</p>
<dt><code>dump-volumes</code></p>
<dd>Debug: Shows the current state of all volumes.</p>
<dt><code>shared</code></p>
<dd>Debug: Show shared properties.</p>
<dt><code>send-message</code> <i>recipient</i> <i>message</i> <i>message_parameters</i></p>
<dd>Send a message to the specified recipient object. If applicable an additional string containing message parameters can be specified. A string is returned as a response to the message. For available messages see <a rel="nofollow" href="https://cgit.freedesktop.org/pulseaudio/pulseaudio/tree/doc/messaging_api.txt.">https://cgit.freedesktop.org/pulseaudio/pulseaudio/tree/doc/messaging_api.txt.</a></p>
<dt><code>exit</code></p>
<dd>Terminate the daemon. If you want to terminate a CLI connection (&quot;log out&quot;) you might want to use ctrl+d</dl>
<h2>Meta Commands</h2>
<p>In addition to the commands described above there are a few meta directives supported by the command line interpreter.</p>
<dl>
<dt><code>.include</code> <i>filename|folder</i></p>
<dd>Executes the commands from the specified script file or in all of the *.pa files within the folder.</p>
<dt><code>.fail</code> and <code>.nofail</code></p>
<dd>Enable (resp. disable) that following failing commands will cancel the execution of the current script file. This is ignored when used on the interactive command line.</p>
<dt><code>.ifexists</code> <i>filename</i></p>
<dd>Execute the subsequent block of commands only if the specified file exists. Typically <i>filename</i> indicates a module. Relative paths are resolved using the module directory as the base. By using an absolute path, the existence of other files can be checked as well.</p>
<dt><code>.else</code> and <code>.endif</code></p>
<dd>A block of commands is delimited by an <code>.else</code> or <code>.endif</code> meta command. Nesting conditional commands is not supported.</dl>
<h2>Authors</h2>
<p>The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-default-pa/">default.pa</a>(5)</code>, <code><a href="/docs/linux/man/1-pacmd/">pacmd</a>(1)</code>, <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code> </p>
