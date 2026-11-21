---

title: "ardour(1)"
name: "ardour"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ardour/"
description: "ardour – a digital audio workstation"
---

<p> ardour &#8211; a digital audio workstation</p>
<h2>SYNOPSIS</h2>
<p> ardour <code>-b</code> [<code>-U</code> <i>file</i>] [<i>session</i>]<br />
 ardour <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> Ardour is a multichannel hard disk recorder (HDR) and digital audio workstation (DAW). It is capable of simultaneous recording 24 or more channels of 32 bit audio at 48kHz. Ardour is intended to function as a &quot;professional&quot; HDR system, replacing dedicated hardware solutions such as the Mackie HDR, the Tascam 2424 and more traditional tape systems like the Alesis ADAT series. It is also intended to provide the same or better functionality as software systems such as ProTools, Samplitude, Logic Audio, Nuendo and Cubase VST (we acknowledge these and all other names as trademarks of their respective owners). It supports MIDI Machine Control, and so can be controlled from any MMC controller, such as the Mackie Digital 8 Bus mixer and many other modern digital mixers.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></dt>
<dd> Print all possible keyboard binding names.</dd>
<dt><code>-U</code></dt>
<dd> Specify the path to the GTK RC file to use. The provided one is called <code>ardour_ui.rc</code> and lives in the top level Ardour source directory. This file controls all color and font use within Ardour. Ardour will run without it, but its appearance is, uhm, ugly.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Displays the help message.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>ardour.rc</code></dt>
<dd> Defaults and startup settings for Ardour.</dd>
<dt><code>ardour_ui.rc</code></dt>
<dd> Definitions for the Ardour interface.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>ARDOUR_RC</code></dt>
<dd> Path to ardour.rc.</dd>
<dt><code>ARDOUR_SYSTEM_RC</code></dt>
<dd> Path to the ardour_system.rc</dd>
<dt><code>LADSPA_PATH</code></dt>
<dd> Path to LADSPA plugins.</dd></dl>
<h2>BUGS</h2>
<p> Yes. <a rel="nofollow" href="http://ardour.org/mantis">http://ardour.org/mantis</a> is the preferred bugtracker.</p>
<h2>AUTHOR</h2>
<p> Paul Davis. Do <i>not</i> contact him directly. Instead, contact him at &lt;ardour-dev [at] lists.ardour.org&gt;. You can subscribe here:<br />
 <a rel="nofollow" href="http://lists.ardour.org/listinfo.cgi/ardour-dev-ardour.org">http://lists.ardour.org/listinfo.cgi/ardour-dev-ardour.org</a> </p>
