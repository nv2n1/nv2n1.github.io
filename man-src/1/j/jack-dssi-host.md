---
title: "jack-dssi-host(1)"
name: "jack-dssi-host"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jack-dssi-host/"
description: "jack-dssi-host – a simple JACK host for DSSI plugins"
---

<h2 class="name">NAME</h2>
<p> jack-dssi-host &#8211; a simple JACK host for DSSI plugins </p>
<h2>SYNOPSIS</h2>
<p> <code>jack-dssi-host</code> <i>[-v] [-a] [-n] [-p &lt;projdir&gt;] [-c &lt;cname&gt;] [-&lt;i&gt;] &lt;libname&gt;[:&lt;label&gt;] [&#8230;]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>jack-dssi-host</code> is a simple DSSI host that listens for MIDI events on an ALSA sequencer port, delivers them to DSSI synth plugins, and outputs the resulting audio via JACK.<br />
 <code>jack-dssi-host</code> can host up to 16 instances of DSSI synth plugins, each of which is sequentially assigned a MIDI channel from 1 to 16. Plugin outputs (if `-a&#8217; is not specified) are connected sequentially to the available JACK physical output ports, wrapping back to the first JACK port whenever the available ports are exhausted. Plugin user interfaces (UIs) are started for each instance (if &#8216;-n&#8217; is not specified.) <code>jack-dssi-host</code> will exit when the last plugin UI has exited.<br />
 As a special case, if <code>jack-dssi-host</code> is started with a name other than `jack-dssi-host&#8217;, and if that name (plus an `.so&#8217; suffix) can be found in the DSSI_PATH search path (see <code>ENVIRONMENT</code> below) as a valid plugin shared library, and if no further command line arguments are given, then the first plugin in that library will be loaded automatically. This provides a convenient way to run a plugin by simply symlinking the plugin&#8217;s basename to jack-dssi-host. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Verbose mode.</p>
<dt><code>-a</code></p>
<dd> Disable automatic connection of outputs to JACK physical outputs.</p>
<dt><code>-n</code></p>
<dd> Disable automatic starting of plugin user interfaces (UIs).</p>
<dt><code>-p &lt;projdir&gt;</code></p>
<dd> The project directory to pass to both plugin and UI.</p>
<dt><code>-c &lt;cname&gt;</code></p>
<dd> The client name to use for ALSA and JACK.</p>
<dt><code>-&lt;i&gt;</code></p>
<dd> Number of instances of the following plugin to run (max 16 total, default 1).</p>
<dt><code>&lt;libname&gt;</code></p>
<dd> Name of the DSSI plugin shared library (.so) to load. This may be an absolute path to the library file, or just the filename itself, in which case the DSSI search path is searched (see ENVIRONMENT below).</p>
<dt><code>&lt;label&gt;</code></p>
<dd> the label of the plugin to load from the library. If this is omitted, the first plugin in the library is used.</p>
<dt><code>[&#8230;]</code></p>
<dd> Optionally more instance counts, plugins and labels.
</dl>
<h2>EXAMPLE</h2>
<p> <code>jack-dssi-host -2 lib1.so -1 lib2.so:fuzzy</code><br />
 Runs two instances of the first plugin found in lib1.so, assigned to MIDI channels 1 and 2 and connected to the first available JACK outputs, and one instance of the &quot;fuzzy&quot; plugin in lib2.so on MIDI channel 3 and connected to the next available JACK output.</p>
<h2>ENVIRONMENT</h2>
<p> <code>jack-dssi-host</code> will search for plugin shared libraries in the directories specified by the environment variable <code>DSSI_PATH,</code> which is a colon-separated list of directories. If <code>DSSI_PATH</code> is not set, a default search path of /usr/lib64/dssi, /usr/local/lib64/dssi, /usr/lib/dssi, /usr/local/lib/dssi, and (assuming the environment variable HOME is set,) $HOME/.dssi is used. </p>
<h2>AUTHOR</h2>
<p> This manual page was originally created by Mark Hymers from the help text of the application, for the Debian project (but may be freely used by others). </p>
<h2>Index</h2>
