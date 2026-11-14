---
title: "qjackctl(1)"
name: "qjackctl"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qjackctl/"
description: "qjackctl – User interface for controlling JACK (Jack Audio Connection Kit)"
---

<h2 class="name">NAME</h2>
<p> qjackctl &#8211; User interface for controlling JACK (Jack Audio Connection Kit) </p>
<h2>SYNOPSIS</h2>
<p> <code>qjackctl </code> [options]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>qjackctl</code> command. This manual page was written for the Debian distribution because the original program does not have a manual page. </p>
<p> <code>qjackctl </code> is used for controlling the Jack Audio Connection Kit (JACK) and as a patchbay for ALSA MIDI devices. Qjackctl also has support for the JACK transport control protocol, so you can use it to start and stop the JACK transport. Once you start qjackctl, you get presented with a single GUI window, the buttons are self-explanatory and have tooltips. </p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. For a complete description, see the Info files.</p>
<dl>
<dt><code>-s, &#8211;start</code></p>
<dd> Start JACK audio server immediately</p>
<dt><code>-p, &#8211;preset=[label]</code></p>
<dd> Set default settings preset name</p>
<dt><code>-a, &#8211;active-patchbay=[path]</code></p>
<dd> Set active patchbay definition file</p>
<dt><code>-n, &#8211;server-name=[label]</code></p>
<dd> Set default JACK audio server name</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show help about command line options</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show version information.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jackd/">jackd</a>(1).</code> </p>
<h2>FILES</h2>
<p> Settings for the JACK system are stored in ~/.config/rncbc.org/QjackCtl.conf and optionally in ~/.jackdrc. </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Guenter Geiger &lt;geiger [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
