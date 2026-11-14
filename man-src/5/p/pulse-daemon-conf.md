---
title: "pulse-daemon-conf(5)"
name: "pulse-daemon-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pulse-daemon-conf/"
description: "pulse-daemon.conf – PulseAudio daemon configuration file"
---

<p>pulse-daemon.conf &#8211; PulseAudio daemon configuration file</p>
<h2>Synopsis</h2>
<p><i>~/.config/pulse/daemon.conf</i><code> </p>
<p> </code><i>~/.config/pulse/daemon.conf.d/*.conf</i><code> </p>
<p> </code><i>/etc/pulse/daemon.conf</i><code> </p>
<p> </code><i>/etc/pulse/daemon.conf.d/*.conf</i></p>
<h2>Description</h2>
<p>The PulseAudio sound server reads configuration directives from a configuration file on startup. If the per-user file <i>~/.config/pulse/daemon.conf</i> exists, it is used, otherwise the system configuration file <i>/etc/pulse/daemon.conf</i> is used. In addition to those main files, configuration directives can also be put in files under directories <i>~/.config/pulse/daemon.conf.d/</i> and <i>/etc/pulse/daemon.conf.d/</i>. Those files have to have the .conf file name extension, but otherwise the file names can be chosen freely. The files under daemon.conf.d are processed in alphabetical order. In case the same option is set in multiple files, the last file to set an option overrides earlier files. The main daemon.conf file is processed first, so options set in files under daemon.conf.d override the main file. </p>
<p> Please note that the server also reads a configuration script on startup. See <code><a href="/docs/linux/man/5-default-pa/">default.pa</a>(5)</code>. </p>
<p> The configuration file is a simple collection of variable declarations. If the configuration file parser encounters either ; or # it ignores the rest of the line until its end. </p>
<p> For the settings that take a boolean argument the values <code>true</code>, <code>yes</code>, <code>on</code> and <code>1</code> are equivalent, resp. <code>false</code>, <code>no</code>, <code>off</code>, <code>0</code>.</p>
<h2>General Directives</h2>
<dl>
<dt><code>daemonize=</code> Daemonize after startup. Takes a boolean value, defaults to <code>no</code>. The <code>&#8211;daemonize</code> command line option takes precedence.</p>
<dd>
<dt><code>fail=</code> Fail to start up if any of the directives in the configuration script <i>default.pa</i> fail. Takes a boolean argument, defaults to <code>yes</code>. The <code>&#8211;fail</code> command line option takes precedence.</p>
<dd>
<dt><code>allow-module-loading=</code> Allow/disallow module loading after startup. This is a security feature that if disabled makes sure that no further modules may be loaded into the PulseAudio server after startup completed. It is recommended to disable this when <code>system-instance</code> is enabled. Please note that certain features like automatic hot-plug support will not work if this option is enabled. Takes a boolean argument, defaults to <code>yes</code>. The <code>&#8211;disallow-module-loading</code> command line option takes precedence.</p>
<dd>
<dt><code>allow-exit=</code> Allow/disallow exit on user request. Defaults to <code>yes</code>.</p>
<dd>
<dt><code>resample-method=</code> The resampling algorithm to use. Use one of <code>src-sinc-best-quality</code>, <code>src-sinc-medium-quality</code>, <code>src-sinc-fastest</code>, <code>src-zero-order-hold</code>, <code>src-linear</code>, <code>trivial</code>, <code>speex-float-N</code>, <code>speex-fixed-N</code>, <code>ffmpeg</code>, <code>soxr-mq</code>, <code>soxr-hq</code>, <code>soxr-vhq</code>. See the documentation of libsamplerate and speex for explanations of the different src- and speex- methods, respectively. The method <code>trivial</code> is the most basic algorithm implemented. If you&#8217;re tight on CPU consider using this. On the other hand it has the worst quality of them all. The Speex resamplers take an integer quality setting in the range 0..10 (bad&#8230;good). They exist in two flavours: <code>fixed</code> and <code>float</code>. The former uses fixed point numbers, the latter relies on floating point numbers. On most desktop CPUs the float point resampler is a lot faster, and it also offers slightly better quality. The soxr-family methods are based on libsoxr, a resampler library from the SoX sound processing utility. The mq variant has the best performance of the three. The hq is more expensive and, according to SoX developers, is considered the best choice for audio of up to 16 bits per sample. The vhq variant has more precision than hq and is more suitable for larger samples. The Soxr resamplers generally offer better quality at less CPU compared to other resamplers, such as speex. The downside is that they can add a significant delay to the output (usually up to around 20 ms, in rare cases more). See the output of <code>dump-resample-methods</code> for a complete list of all available resamplers. Defaults to <code>speex-float-1</code>. The <code>&#8211;resample-method</code> command line option takes precedence. Note that some modules overwrite or allow overwriting of the resampler to use.</p>
<dd>
<dt><code>avoid-resampling=</code> If set, try to configure the device to avoid resampling. This only works on devices which support reconfiguring their rate, and when no other streams are already playing or capturing audio. The device will also not be configured to a rate less than the default and alternate sample rates.</p>
<dd>
<dt><code>enable-remixing=</code> If disabled never upmix or downmix channels to different channel maps. Instead, do a simple name-based matching only. Defaults to <code>yes</code>. There is no known valid use case for setting this option to <code>no</code>, therefore, this option is deprecated and may be removed in a future version of PulseAudio.</p>
<dd>
<dt><code>remixing-use-all-sink-channels=</code> If enabled, use all sink channels when remixing. Otherwise, remix to the minimal set of sink channels needed to reproduce all of the source channels. (This has no effect on LFE remixing.) Defaults to <code>yes</code>.</p>
<dd>
<dt><code>enable-lfe-remixing=</code> This is a way to set <code>remixing-produce-lfe</code> and <code>remixing-consume-lfe</code> to the same value at once. This option only exists for backward compatibility and may be removed in a future version of PulseAudio.</p>
<dd>
<dt><code>remixing-produce-lfe=</code> If enabled, and the sink input does not have the LFE channel, synthesize the output LFE channel as a (lowpass-filtered, if <code>lfe-crossover-freq</code> is not 0) average of all input channels. Also, when <code>lfe-crossover-freq</code> is not 0, filter out low frequencies from other channels while producing a synthetic LFE output. If disabled, the output LFE channel will only get a signal when an input LFE channel is available as well. Defaults to <code>no</code>.</p>
<dd>
<dt><code>remixing-consume-lfe=</code> If enabled, and the sink does not have an LFE channel, redirect the input LFE channel (if any) to other channels. If disabled, the input LFE channel will remain unused unless the sink has the LFE channel as well. Defaults to <code>no</code>.</p>
<dd>
<dt><code>lfe-crossover-freq=</code> The crossover frequency (in Hz) for the LFE filter. Set it to 0 to disable the LFE filter. Defaults to 0.</p>
<dd>
<dt><code>use-pid-file=</code> Create a PID file in the runtime directory (<i>$XDG_RUNTIME_DIR/pulse/pid</i>). If this is enabled you may use commands like <code>&#8211;kill</code> or <code>&#8211;check</code>. If you are planning to start more than one PulseAudio process per user, you better disable this option since it effectively disables multiple instances. Takes a boolean argument, defaults to <code>yes</code>. The <code>&#8211;use-pid-file</code> command line option takes precedence.</p>
<dd>
<dt><code>cpu-limit=</code> If disabled do not install the CPU load limiter, even on platforms where it is supported. This option is useful when debugging/profiling PulseAudio to disable disturbing SIGXCPU signals. Takes a boolean argument, defaults to <code>no</code>. The <code>&#8211;no-cpu-limit</code> command line argument takes precedence.</p>
<dd>
<dt><code>system-instance=</code> Run the daemon as system-wide instance, requires root privileges. Takes a boolean argument, defaults to <code>no</code>. The <code>&#8211;system</code> command line argument takes precedence.</p>
<dd>
<dt><code>local-server-type=</code> Please don&#8217;t use this option if you don&#8217;t have to! This option is currently only useful when you want D-Bus clients to use a remote server. This option may be removed in future versions. If you only want to run PulseAudio in the system mode, use the <code>system-instance</code> option. This option takes one of <code>user</code>, <code>system</code> or <code>none</code> as the argument. This is essentially a duplicate for the <code>system-instance</code> option. The difference is the <code>none</code> option, which is useful when you want to use a remote server with D-Bus clients. If both this and <code>system-instance</code> are defined, this option takes precedence. Defaults to whatever the <code>system-instance</code> is set.</p>
<dd>
<dt><code>enable-shm=</code> Enable data transfer via POSIX or memfd shared memory. Takes a boolean argument, defaults to <code>yes</code>. The <code>&#8211;disable-shm</code> command line argument takes precedence.</p>
<dd>
<dt><code>enable-memfd=</code>. Enable memfd shared memory. Takes a boolean argument, defaults to <code>yes</code>.</p>
<dd>
<dt><code>shm-size-bytes=</code> Sets the shared memory segment size for the daemon, in bytes. If left unspecified or is set to 0 it will default to some system-specific default, usually 64 MiB. Please note that usually there is no need to change this value, unless you are running an OS kernel that does not do memory overcommit.</p>
<dd>
<dt><code>lock-memory=</code> Locks the entire PulseAudio process into memory. While this might increase drop-out safety when used in conjunction with real-time scheduling this takes away a lot of memory from other processes and might hence considerably slow down your system. Defaults to <code>no</code>.</p>
<dd>
<dt><code>flat-volumes=</code> Enable &#8216;flat&#8217; volumes, i.e. where possible let the sink volume equal the maximum of the volumes of the inputs connected to it. Takes a boolean argument, defaults to <code>no</code>.</p>
<dd>
<dt><code>rescue-streams=</code> Enable rescuing of streams if the used sink or source becomes unavailable. Takes a boolean argument. If set to <code>yes</code>, pulseaudio will try to move the streams from a sink or source that becomes unavailable to the default sink or source. If set to <code>no</code>, streams will be killed if the corresponding sink or source disappears. Defaults to <code>yes</code>.</p>
<dd></dl>
<h2>Scheduling</h2>
<dl>
<dt><code>high-priority=</code> Renice the daemon after startup to become a high-priority process. This a good idea if you experience drop-outs during playback. However, this is a certain security issue, since it works when called SUID root only, or RLIMIT_NICE is used. root is dropped immediately after gaining the nice level on startup, thus it is presumably safe. See <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code> for more information. Takes a boolean argument, defaults to <code>yes</code>. The <code>&#8211;high-priority</code> command line option takes precedence.</p>
<dd>
<dt><code>realtime-scheduling=</code> Try to acquire SCHED_FIFO scheduling for the IO threads. The same security concerns as mentioned above apply. However, if PA enters an endless loop, realtime scheduling causes a system lockup. Thus, realtime scheduling should only be enabled on trusted machines for now. Please note that only the IO threads of PulseAudio are made real-time. The controlling thread is left a normally scheduled thread. Thus enabling the high-priority option is orthogonal. See <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code> for more information. Takes a boolean argument, defaults to <code>yes</code>. The <code>&#8211;realtime</code> command line option takes precedence.</p>
<dd>
<dt><code>realtime-priority=</code> The realtime priority to acquire, if <code>realtime-scheduling</code> is enabled. Note: JACK uses 10 by default, 9 for clients. Thus it is recommended to choose the PulseAudio real-time priorities lower. Some PulseAudio threads might choose a priority a little lower or higher than the specified value. Defaults to <code>5</code>.</p>
<dd>
<dt><code>nice-level=</code> The nice level to acquire for the daemon, if <code>high-priority</code> is enabled. Note: on some distributions X11 uses -10 by default. Defaults to -11.</p>
<dd></dl>
<h2>Idle Times</h2>
<dl>
<dt><code>exit-idle-time=</code> Terminate the daemon after the last client quit and this time in seconds passed. Use a negative value to disable this feature. Defaults to 20. The <code>&#8211;exit-idle-time</code> command line option takes precedence.</p>
<dd>When PulseAudio runs in the per-user mode and detects a login session, then any positive value will be reset to 0 so that PulseAudio will terminate immediately on logout. A positive value therefore has effect only in environments where there&#8217;s no support for login session tracking (or if the user is logged in without a session spawned, a.k.a. lingering). A negative value can still be used to disable any automatic exit. </p>
<p> When PulseAudio runs in the system mode, automatic exit is always disabled, so this option does nothing.</p>
<dt><code>scache-idle-time=</code> Unload autoloaded sample cache entries after being idle for this time in seconds. Defaults to 20. The <code>&#8211;scache-idle-time</code> command line option takes precedence.</p>
<dd></dl>
<h2>Paths</h2>
<dl>
<dt><code>dl-search-path=</code> The path where to look for dynamic shared objects (DSOs/plugins). You may specify more than one path separated by colons. The default path depends on compile time settings. The <code>&#8211;dl-search-path</code> command line option takes precedence.</p>
<dd>
<dt><code>default-script-file=</code> The default configuration script file to load. Specify an empty string for not loading a default script file. The default behaviour is to load <i>~/.config/pulse/default.pa</i>, and if that file does not exist fall back to the system wide installed version <i>/etc/pulse/default.pa</i>. If run in system-wide mode the file <i>/etc/pulse/system.pa</i> is used instead. If <code>-n</code> is passed on the command line or <code>default-script-file=</code> is disabled the default configuration script is ignored.</p>
<dd>
<dt><code>load-default-script-file=</code> Load the default configuration script file as specified in <code>default-script-file=</code>. Defaults to <code>yes</code>.</p>
<dd></dl>
<h2>Logging</h2>
<dl>
<dt><code>log-target=</code> The default log target. Use either <code>stderr</code>, <code>syslog</code>, <code>journal</code> (optional), <code>auto</code>, <code>file:PATH</code> or <code>newfile:PATH</code>. On traditional systems <code>auto</code> is equivalent to <code>syslog</code>. On systemd-enabled systems, auto is equivalent to <code>journal</code>, in case <code>daemonize</code> is enabled, and to <code>stderr</code> otherwise. If set to <code>file:PATH</code>, logging is directed to the file indicated by PATH. <code>newfile:PATH</code> is otherwise the same as <code>file:PATH</code>, but existing files are never overwritten. If the specified file already exists, a suffix is added to the file name to avoid overwriting. Defaults to <code>auto</code>. The <code>&#8211;log-target</code> command line option takes precedence.</p>
<dd>
<dt><code>log-level=</code> Log level, one of <code>debug</code>, <code>info</code>, <code>notice</code>, <code>warning</code>, <code>error</code>. Log messages with a lower log level than specified here are not logged. Defaults to <code>notice</code>. The <code>&#8211;log-level</code> command line option takes precedence. The <code>-v</code> command line option might alter this setting.</p>
<dd>
<dt><code>log-meta=</code> With each logged message log the code location the message was generated from. Defaults to <code>no</code>.</p>
<dd>
<dt><code>log-time=</code> With each logged message log the relative time since startup. Defaults to <code>no</code>.</p>
<dd>
<dt><code>log-backtrace=</code> When greater than 0, with each logged message log a code stack trace up the specified number of stack frames. Defaults to <code>0</code>.</p>
<dd></dl>
<h2>Resource Limits</h2>
<p>See <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a>(2)</code> for more information. Set to -1 if PulseAudio shall not touch the resource limit. Not all resource limits are available on all operating systems.</p>
<dl>
<dt><code>rlimit-as</code> Defaults to -1.</p>
<dd>
<dt><code>rlimit-rss</code> Defaults to -1.</p>
<dd>
<dt><code>rlimit-core</code> Defaults to -1.</p>
<dd>
<dt><code>rlimit-data</code> Defaults to -1.</p>
<dd>
<dt><code>rlimit-fsize</code> Defaults to -1.</p>
<dd>
<dt><code>rlimit-nofile</code> Defaults to 256.</p>
<dd>
<dt><code>rlimit-stack</code> Defaults to -1.</p>
<dd>
<dt><code>rlimit-nproc</code> Defaults to -1.</p>
<dd>
<dt><code>rlimit-locks</code> Defaults to -1.</p>
<dd>
<dt><code>rlimit-sigpending</code> Defaults to -1.</p>
<dd>
<dt><code>rlimit-msgqueue</code> Defaults to -1.</p>
<dd>
<dt><code>rlimit-memlock</code> Defaults to 16 KiB. Please note that the JACK client libraries may require more locked memory.</p>
<dd>
<dt><code>rlimit-nice</code> Defaults to 31. Please make sure that the default nice level as configured with <code>nice-level</code> fits in this resource limit, if <code>high-priority</code> is enabled.</p>
<dd>
<dt><code>rlimit-rtprio</code> Defaults to 9. Please make sure that the default real-time priority level as configured with <code>realtime-priority=</code> fits in this resource limit, if <code>realtime-scheduling</code> is enabled. The JACK client libraries require a real-time priority of 9 by default.</p>
<dd>
<dt><code>rlimit-rttime</code> Defaults to 1000000.</p>
<dd></dl>
<h2>Default Device Settings</h2>
<p>Most drivers try to open the audio device with these settings and then fall back to lower settings. The default settings are CD quality: 16bit native endian, 2 channels, 44100 Hz sampling.</p>
<dl>
<dt><code>default-sample-format=</code> The default sampling format. See <a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/SupportedAudioFormats/">https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/SupportedAudioFormats/</a> for possible values.</p>
<dd>
<dt><code>default-sample-rate=</code> The default sample frequency.</p>
<dd>
<dt><code>default-sample-channels</code> The default number of channels.</p>
<dd>
<dt><code>default-channel-map</code> The default channel map.</p>
<dd>
<dt><code>alternate-sample-rate</code> The alternate sample frequency. Sinks and sources will use either the default-sample-rate value or this alternate value, typically 44.1 or 48kHz. Switching between default and alternate values is enabled only when the sinks/sources are suspended. This option is ignored in passthrough mode where the stream rate will be used. If set to the same value as the default sample rate, this feature is disabled.</p>
<dd></dl>
<h2>Default Fragment Settings</h2>
<p>Some hardware drivers require the hardware playback buffer to be subdivided into several fragments. It is possible to change these buffer metrics for machines with high scheduling latencies. Not all possible values that may be configured here are available in all hardware. The driver will find the nearest setting supported. Modern drivers that support timer-based scheduling ignore these options.</p>
<dl>
<dt><code>default-fragments=</code> The default number of fragments. Defaults to 4.</p>
<dd>
<dt><code>default-fragment-size-msec=</code>The duration of a single fragment. Defaults to 25ms (i.e. the total buffer is thus 100ms long).</p>
<dd></dl>
<h2>Default Deferred Volume Settings</h2>
<p>With the flat volume feature enabled, the sink HW volume is set to the same level as the highest volume input stream. Any other streams (with lower volumes) have the appropriate adjustment applied in SW to bring them to the correct overall level. Sadly hardware mixer changes cannot be timed accurately and thus this change of volumes can sometimes cause the resulting output sound to be momentarily too loud or too soft. So to ensure SW and HW volumes are applied concurrently without any glitches, their application needs to be synchronized. The sink implementation needs to support deferred volumes. The following parameters can be used to refine the process.</p>
<dl>
<dt><code>enable-deferred-volume=</code> Enable deferred volume for the sinks that support it. This feature is enabled by default.</p>
<dd>
<dt><code>deferred-volume-safety-margin-usec=</code> The amount of time (in usec) by which the HW volume increases are delayed and HW volume decreases are advanced. Defaults to 8000 usec.</p>
<dd>
<dt><code>deferred-volume-extra-delay-usec=</code> The amount of time (in usec) by which HW volume changes are delayed. Negative values are also allowed. Defaults to 0.</p>
<dd></dl>
<h2>Authors</h2>
<p>The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pulse-client-conf/">pulse-client.conf</a>(5)</code>, <code><a href="/docs/linux/man/5-default-pa/">default.pa</a>(5)</code>, <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code>, <code><a href="/docs/linux/man/1-pacmd/">pacmd</a>(1)</code> </p>
