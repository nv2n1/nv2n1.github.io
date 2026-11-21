---
title: "mate-cpufreq-selector(1)"
name: "mate-cpufreq-selector"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mate-cpufreq-selector/"
description: "mate-cpufreq-selector – A generic command line tool to change the cpu frequency."
---

<h2>SYNOPSIS</h2>
<p> <code>mate-cpufreq-selector [OPTIONS]</code></p>
<h2>DESCRIPTION</h2>
<p> This tool is a part of the CPU Frequency Scaling Monitor Applet for the MATE Panel. It can be called from the command line when installed. <code>mate-cpufreq-selector</code> is used to adjust the CPU Frequency settings if the system supports scaling. </p>
<p> This manual page briefly documents the <code>mate-cpufreq-selector</code> command. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c NUMBER, &#8211;cpu=NUMBER</code></dt>
<dd> Specify the CPU Number to adjust settings for. If no CPU is specified, CPU0 is assumed.</dd>
<dt><code>-g GOVERNOR, &#8211;governor=GOVERNOR</code></dt>
<dd> Specify a valid CPU Governor to use. (ie. conservative, ondemand, performance, powersave)</dd>
<dt><code>-f FREQ, &#8211;frequency=FREQ</code></dt>
<dd> Specify a CPU Frequency to set in KHz.</dd>
<dt><code>-?, -h, &#8211;help</code></dt>
<dd> Print standard command line options.</dd></dl>
<h2>EXAMPLES</h2>
<p> <code>mate-cpufreq-selector &#8211;cpu=1 -g powersave</code></p>
<dl>
<dt>
</dt><dd> Set scaling Governor &quot;Powersave&quot; on CPU1</dd></dl>
<p> <code>mate-cpufreq-selector -f 1200</code></p>
<dl>
<dt>
</dt><dd> Set max CPU Frequency to 1200KHz (1.2GHz) on CPU0</dd></dl>
<h2>BUGS</h2>
<h3>Should you encounter any bugs, they may be reported at:</h3>
<p> <a rel="nofollow" href="http://github.com/mate-desktop/mate-applets/issues">http://github.com/mate-desktop/mate-applets/issues</a></p>
<h2>AUTHORS</h2>
<h3>This Man Page has been written for the MATE Desktop Environment by:</h3>
<p> Adam Erdman &lt;hekel [at] archlinux.info&gt; (2014)</p>
<h2>HISTORY</h2>
<h3>cpufreq-selector was originally written for gnome-applets by:</h3>
<p> Carlos García Campos &lt;carlosgc [at] gnome.org&gt; (2004)</p>
<h2>SEE ALSO</h2>
<h3>Further information may also be available at: <a rel="nofollow" href="http://wiki.mate-desktop.org/docs">http://wiki.mate-desktop.org/docs</a></h3>
