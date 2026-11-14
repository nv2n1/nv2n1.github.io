---
title: "gamemoded(8)"
name: "gamemoded"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gamemoded/"
description: "gamemoded – daemon that optimises system performance on demand"
---

<p>gamemoded &#8211; daemon that optimises system performance on demand</p>
<h2>Synopsis</h2>
<p><code>gamemoded</code> [OPTIONS&#8230;]</p>
<h2>Description</h2>
<p><code>GameMode</code> is a daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS. </p>
<p> The design has a clear cut abstraction between the host daemon and library (<code>gamemoded</code> and <code>libgamemode</code>), and the client loaders (<code>libgamemodeauto</code> and <code>gamemode_client.h</code>) that allows for safe usage without worrying about whether the daemon is installed or running. This design also means that while the host library currently relies on systemd for exchanging messages with the daemon, it&#8217;s entirely possible to implement other internals that still work with the same clients. </p>
<p> <code>GameMode</code> was designed primarily as a stop-gap solution to problems with the Intel and AMD CPU powersave or ondemand governors, but is intended to be expanded beyond just CPU governor states, as there are a wealth of automation tasks one might want to apply.</p>
<h2>Options</h2>
<dl>
<dt><code>-r[PID], &#8211;request=[PID]</code></p>
<dd>Toggle gamemode for process. When no PID given, requests gamemode and pauses</p>
<dt><code>-s[PID], &#8211;status=[PID]</code></p>
<dd>Query the status of gamemode for process When no PID given, queries the status globally</p>
<dt><code>-d, &#8211;daemonize</code></p>
<dd>Run the daemon as a separate process (daemonize it)</p>
<dt><code>-l, &#8211;log-to-syslog</code></p>
<dd>Log to syslog</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Print help text</p>
<dt><code>-t, &#8211;test</code></p>
<dd>Run diagnostic tests on the current installation</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Print the version </p>
</dl>
<h2>Usage</h2>
<p><code>libgamemodeauto.so.0</code> can be pre-loaded into any program to request <code>gamemoded</code> begin or end the mode. See <a href="/docs/linux/man/1-gamemoderun/">gamemoderun</a>(1) for details. </p>
<p> The <code>gamemode_client.h</code> header can be used by developers to build the requests into a program: </p>
<dl>
<dd>
<pre>#include &quot;gamemode_client.h&quot;
 if( gamemode_request_start() &lt; 0 ) {
 fprintf( stderr, &quot;gamemode request failed: %s
&quot;, gamemode_error_string() )
 }
 /* run the process */
 /* Not required, gamemoded can clean up after game exits */
 gamemode_request_end();</pre>
</dl>
<p> Atlernatively developers can define <code>GAMEMODE_AUTO</code> to mimic the behaviour of <code>libgamemodeauto.so.0</code>: </p>
<dl>
<dd>
<pre>#define GAMEMODE_AUTO
#include &quot;gamemode_client.h&quot;</pre>
</dl>
<p> Or, distribute <code>libgamemodeauto.so.0</code> and either link with <code>-lgamemodeauto</code> or inject it as above with <code>LD_PRELOAD</code>.</p>
<h2>Config</h2>
<p><code>gamemoded</code> will load and merge <code>gamemode.ini</code> config files from these directories in the following order: </p>
<dl>
<dd>/usr/share/gamemode/</dl>
<dl>
<dd>/etc/</dl>
<dl>
<dd>$XDG_CONFIG_HOME or $HOME/.config/</dl>
<dl>
<dd>$PWD</dl>
<p> Behaviour of the config file can be explained by presenting a commented example: </p>
<dl>
<dd>
<pre>[general]
; The reaper thread will check every 5 seconds for exited clients, for config file changes, and for the CPU/iGPU power balance
reaper_freq=5
; The desired governor is used when entering GameMode instead of &quot;performance&quot;
desiredgov=performance
; The default governor is used when leaving GameMode instead of restoring the original value
;defaultgov=powersave
; The iGPU desired governor is used when the integrated GPU is under heavy load
igpu_desiredgov=powersave
; Threshold to use to decide when the integrated GPU is under heavy load.
; This is a ratio of iGPU Watts / CPU Watts which is used to determine when the
; integraged GPU is under heavy enough load to justify switching to
; igpu_desiredgov. Set this to -1 to disable all iGPU checking and always
; use desiredgov for games.
igpu_power_threshold=0.3
; GameMode can change the scheduler policy to SCHED_ISO on kernels which support it (currently
; not supported by upstream kernels). Can be set to &quot;auto&quot;, &quot;on&quot; or &quot;off&quot;. &quot;auto&quot; will enable
; with 4 or more CPU cores. &quot;on&quot; will always enable. Defaults to &quot;off&quot;.
softrealtime=off
; GameMode can renice game processes. You can put any value between 0 and 20 here, the value
; will be negated and applied as a nice value (0 means no change). Defaults to 0.
renice=0
; By default, GameMode adjusts the iopriority of clients to BE/0, you can put any value
; between 0 and 7 here (with 0 being highest priority), or one of the special values
; &quot;off&quot; (to disable) or &quot;reset&quot; (to restore Linux default behavior based on CPU priority),
; currently, only the best-effort class is supported thus you cannot set it here
ioprio=0
; Sets whether gamemode will inhibit the screensaver when active
; Defaults to 1
inhibit_screensaver=1
[filter]
; If &quot;whitelist&quot; entry has a value(s)
; gamemode will reject anything not in the whitelist
;whitelist=RiseOfTheTombRaider
; Gamemode will always reject anything in the blacklist
;blacklist=HalfLife3
; glxgears
[gpu]
; Here Be Dragons!
; Warning: Use these settings at your own risk
; Any damage to hardware incurred due to this feature is your responsibility and yours alone
; It is also highly recommended you try these settings out first manually to find the sweet spots
; Setting this to the keyphrase &quot;accept-responsibility&quot; will allow gamemode to apply GPU optimisations such as overclocks
;apply_gpu_optimisations=0
; The DRM device number on the system (usually 0), ie. the number in /sys/class/drm/card0/
;gpu_device=0
; Nvidia specific settings
; Requires the coolbits extension activated in nvidia-xconfig
; This corresponds to the desired GPUPowerMizerMode
; &quot;Adaptive&quot;=0 &quot;Prefer Maximum Performance&quot;=1 and &quot;Auto&quot;=2
; See NV_CTRL_GPU_POWER_MIZER_MODE and friends in <a rel="nofollow" href="https://github.com/NVIDIA/nvidia-settings/blob/master/src/libXNVCtrl/NVCtrl.h">https://github.com/NVIDIA/nvidia-settings/blob/master/src/libXNVCtrl/NVCtrl.h</a>
;nv_powermizer_mode=1
; These will modify the core and mem clocks of the highest perf state in the Nvidia PowerMizer
; They are measured as Mhz offsets from the baseline, 0 will reset values to default, -1 or unset will not modify values
;nv_core_clock_mhz_offset=0
;nv_mem_clock_mhz_offset=0
; AMD specific settings
; Requires a relatively up to date AMDGPU kernel module
; See: <a rel="nofollow" href="https://dri.freedesktop.org/docs/drm/gpu/amdgpu.html#gpu-power-thermal-controls-and-monitoring">https://dri.freedesktop.org/docs/drm/gpu/amdgpu.html#gpu-power-thermal-controls-and-monitoring</a>
; It is also highly recommended you use lm-sensors (or other available tools) to verify card temperatures
; This corresponds to power_dpm_force_performance_level, &quot;manual&quot; is not supported for now
;amd_performance_level=high
[supervisor]
; This section controls the new gamemode functions gamemode_request_start_for and gamemode_request_end_for
; The whilelist and blacklist control which supervisor programs are allowed to make the above requests
;supervisor_whitelist=
;supervisor_blacklist=
; In case you want to allow a supervisor to take full control of gamemode, this option can be set
; This will only allow gamemode clients to be registered by using the above functions by a supervisor client
;require_supervisor=0
[custom]
; Custom scripts (executed using the shell) when gamemode starts and ends
;start=notify-send &quot;GameMode started&quot;
; /home/me/bin/stop_ethmining.sh
;end=notify-send &quot;GameMode ended&quot;
; /home/me/bin/start_ethmining.sh
; Timeout for scripts (seconds). Scripts will be killed if they do not complete within this time.
;script_timeout=10</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-gamemoderun/">gamemoderun</a>(1), <a href="/docs/linux/man/1-systemd/">systemd</a>(1) </p>
<h2>About</h2>
<p>GameMode source can be found at <i><a rel="nofollow" href="https://github.com/FeralInteractive/gamemode.git">https://github.com/FeralInteractive/gamemode.git</a></i></p>
<h2>Author</h2>
<p>Feral Interactive (linux-contact [at] feralinteractive.com)</p>
