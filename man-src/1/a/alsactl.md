---
title: "alsactl(1)"
name: "alsactl"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alsactl/"
description: "alsactl – advanced controls for ALSA soundcard driver"
---

<h2 class="name">NAME</h2>
<p> alsactl &#8211; advanced controls for ALSA soundcard driver</p>
<h2>SYNOPSIS</h2>
<p> <code>alsactl</code> [<i>options</i>] [<i>store</i>|<i>restore</i>|<i>init</i>] &lt;card # or id or device&gt; </p>
<p> <code>alsactl</code> <i>monitor</i> &lt;card # or id&gt; </p>
<p> <code>alsactl</code> [<i>clean</i>] &lt;card # or id or device&gt; [[control identifiers]] </p>
<h2>DESCRIPTION</h2>
<p> <code>alsactl</code> is used to control advanced settings for the ALSA soundcard drivers. It supports multiple soundcards. If your card has features that you can&#8217;t seem to control from a mixer application, you have come to the right place. </p>
<h2>COMMANDS</h2>
<h3>Introduction</h3>
<p> The <i>&lt;card&gt;</i> argument is optional. If no soundcards are specified, setup for all cards will be saved, loaded or monitored. </p>
<h3>store &lt;card&gt;</h3>
<p> This command saves the current driver state for the selected soundcard to the configuration file. </p>
<h3>restore &lt;card&gt;</h3>
<p> This command loads driver state for the selected soundcard from the configuration file. If restoring fails (eventually partly), the init action is called. </p>
<h3>nrestore &lt;card&gt;</h3>
<p> This command is like <i>restore</i>, but it notifies also the daemon to do new rescan for available soundcards. </p>
<h3>init &lt;card&gt;</h3>
<p> This command tries to initialize all devices to a default state. If device is not known, error code 99 is returned. </p>
<h3>daemon</h3>
<p> This command manages to save periodically the sound state. </p>
<h3>rdaemon</h3>
<p> This command is like <i>daemon</i> but restore the sound state at first. </p>
<h3>kill &lt;cmd&gt;</h3>
<p> This command notifies the daemon to do the specified operation (quit, rescan, save_and_quit). </p>
<h3>monitor &lt;card&gt;</h3>
<p> This command is for monitoring the events received from the given control device. </p>
<h3>clean &lt;card&gt; [filter]</h3>
<p> This command cleans the controls created by applications. </p>
<p> The optional element identifiers are accepted as a filter. One extra argument is parsed as an element identifiers. </p>
<p> <i>Example:</i> alsactl clean 0 &quot;name=&#8217;PCM&#8217;&quot; &quot;name=&#8217;Mic Phantom&#8217;&quot; </p>
<h3>dump-state</h3>
<p> This command dumps the current state (all cards) to stdout. </p>
<h3>dump-cfg</h3>
<p> This command dumps the current configuration (all cards) to stdout. Note that the configuration hooks are evaluated. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd> Help: show available flags and commands. </p>
<dt><i>-d, &#8211;debug</i></p>
<dd> Use debug mode: a bit more verbose. </p>
<dt><i>-v, &#8211;version</i></p>
<dd> Print alsactl version number. </p>
<dt><i>-f, &#8211;file</i></p>
<dd> Select the configuration file to use. The default is /var/lib/alsa/asound.state. </p>
<dt><i>-a, &#8211;config-dir</i></p>
<dd> Select the boot / hotplug ALSA configuration directory to use. The default is /var/lib/alsa. </p>
<dt><i>-l, &#8211;lock</i></p>
<dd> Use the file locking to serialize the concurrent access to the state file (this option is default for the global state file). </p>
<dt><i>-L, &#8211;no-lock</i></p>
<dd> Do not use the file locking to serialize the concurrent access to the state file (including the global state file). </p>
<dt><i>-O, &#8211;lock-state-file</i></p>
<dd> Select the state lock file path. </p>
<dt><i>-F, &#8211;force</i></p>
<dd> Used with restore command. Try to restore the matching control elements as much as possible. This option is set as default now. </p>
<dt><i>-g, &#8211;ignore</i></p>
<dd> Used with store, restore and init commands. Do not show &#8216;No soundcards found&#8217; and do not set an error exit code when soundcards are not installed. </p>
<dt><i>-P, &#8211;pedantic</i></p>
<dd> Used with restore command. Don&#8217;t restore mismatching control elements. This option was the old default behavior. </p>
<dt><i>-I, &#8211;no-init-fallback</i></p>
<dd> Don&#8217;t initialize cards if restore fails. Since version 1.0.18, <code>alsactl</code> tries to initialize the card with the restore operation as default. But this can cause incompatibility with the older version. The caller may expect that the state won&#8217;t be touched if no state file exists. This option takes the restore behavior back to the older version by suppressing the initialization. </p>
<dt><i>-r, &#8211;runstate</i></p>
<dd> Save restore and init state to this file. The file will contain only errors. Errors are appended with the soundcard id to the end of file. </p>
<dt><i>-R, &#8211;remove</i></p>
<dd> Remove runstate file at first. </p>
<dt><i>-E, &#8211;env</i> #=#</p>
<dd> Set environment variable (useful for init action or you may override ALSA_CONFIG_PATH to read different or optimized configuration &#8211; may be useful for &quot;boot&quot; scripts). </p>
<dt><i>-i, &#8211;initfile</i></p>
<dd> The configuration file for init. By default, PREFIX/share/alsa/init/00main is used. </p>
<dt><i>-p, &#8211;period</i></p>
<dd> The store period in seconds for the daemon command. </p>
<dt><i>-e, &#8211;pid-file</i></p>
<dd> The pathname to store the process-id file in the HDB UUCP format (ASCII). </p>
<dt><i>-b, &#8211;background</i></p>
<dd> Run the task in background. </p>
<dt><i>-s, &#8211;syslog</i></p>
<dd> Use syslog for messages. </p>
<dt><i>-n, &#8211;nice</i></p>
<dd> Set the process priority (see &#8216;man nice&#8217;) </p>
<dt><i>-c, &#8211;sched-idle</i></p>
<dd> Set the process scheduling policy to idle (SCHED_IDLE). </p>
<dt><i>-D, &#8211;ucm-defaults</i></p>
<dd> Execute also the &#8216;defaults&#8217; section from the UCM configuration. The standard behaviour is to execute only &#8216;once&#8217; section. </p>
<dt><i>-U, &#8211;no-ucm</i></p>
<dd> Skip the UCM init even if available. It may be useful for the test the legacy init configuration. </p>
</dl>
<h2>FILES</h2>
<p> <i>/var/lib/alsa/asound.state</i> (or whatever file you specify with the <code>-f</code> flag) is used to store current settings for your soundcards. The settings include all the usual soundcard mixer settings. More importantly, alsactl is capable of controlling other card-specific features that mixer apps usually don&#8217;t know about. </p>
<p> The configuration file is generated automatically by running <code>alsactl store</code>. Editing the configuration file by hand may be necessary for some soundcard features (e.g. enabling/disabling automatic mic gain, digital output, joystick/game ports, some future MIDI routing options, etc). </p>
<h2>SEE ALSO</h2>
<p> <code> <a href="/docs/linux/man/1-amixer/">amixer</a>(1), <a href="/docs/linux/man/1-alsamixer/">alsamixer</a>(1), <a href="/docs/linux/man/1-aplay/">aplay</a>(1), <a href="/docs/linux/man/7-alsactl_init/">alsactl_init</a>(7) </code> </p>
<h2>BUGS</h2>
<p> None known. </p>
<h2>AUTHOR</h2>
<p> <code>alsactl</code> is by Jaroslav Kysela &lt;perex [at] perex.cz&gt; and Abramo Bagnara &lt;abramo [at] alsa-project.org&gt;. This document is by Paul Winkler &lt;zarmzarm [at] erols.com&gt;. </p>
<h2>Index</h2>
