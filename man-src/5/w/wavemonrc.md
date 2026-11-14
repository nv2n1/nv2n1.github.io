---
title: "wavemonrc(5)"
name: "wavemonrc"
section: "5"
letter: "w"
url: "/docs/linux/man/5-wavemonrc/"
description: "$HOME/.wavemonrc – wavemon configuration file"
---

<p>$HOME/.wavemonrc &#8211; wavemon configuration file</p>
<h2>Description</h2>
<p><i>wavemonrc</i> is the per-user configuration file for <code><a href="/docs/linux/man/1-wavemon/">wavemon</a></code>(1). This page describes its individual configuration options. Each corresponds to a configuration item of the <i>Preferences</i> screen (F7 key), whose on-screen name is shown in parentheses. </p>
<p> <code>interface = &lt;ifname&gt;</code></p>
<dl>
<dd></dl>
<p> (Interface)</p>
<dl>
<dd>Selects the wireless interface to use. </p>
</dl>
<p> <code>cisco_mac = (on|off)</code></p>
<dl>
<dd></dl>
<p> (Cisco-style MAC addresses)</p>
<dl>
<dd>If enabled, display MAC addresses using lower-case hex digits separated by dots rather than colons. </p>
</dl>
<p> <code>sort_order = (channel|essid|signal|open|chan/sig|open/sig)</code></p>
<dl>
<dd></dl>
<p> (Scan sort type)</p>
<dl>
<dd>Determines the ordering used in the scan window: <i>channel</i> sorts by channel number, <i>essid</i> by access point name, <i>signal</i> by signal strength, and <i>open</i> by openness. The combined variants <i>chan/sig</i> and <i>open/sig</i> sort first by channel/openness and then by signal strength. It also affects the status line at the bottom: normally the most crowded channels are listed, sorting by <i>channel</i> in descending order switches to least crowded ones instead. </p>
</dl>
<p> <code>sort_ascending = (on|off)</code></p>
<dl>
<dd></dl>
<p> (Scan sort direction)</p>
<dl>
<dd>Sets the direction of the <i>sort_order</i>: ascending (on) or descending (off). </p>
</dl>
<p> <code>stat_updates = &lt;n&gt;</code></p>
<dl>
<dd></dl>
<p> (Statistics updates)</p>
<dl>
<dd>Time interval for polling new statistics (including scan refresh). Range: 10..4000ms. </p>
</dl>
<p> <code>lhist_slot_size = &lt;n&gt;</code></p>
<dl>
<dd></dl>
<p> (Histogram update cycles)</p>
<dl>
<dd>Number of samples used per each histogram slot. For example, if the stat_updates interval is 500ms and the histogram slot size is 4, the histogram is moved one slot further every 2 seconds. Range: 1..64. </p>
</dl>
<p> <code>meter_smoothness = &lt;n&gt;</code></p>
<dl>
<dd></dl>
<p> (Level meter smoothness)</p>
<dl>
<dd>Determines the responsiveness of level meters, tracking the moving average rather than following each new sample. The given value specifies the percentage of the history (the &#8216;inertia&#8217;) of preceding samples. A value of 0 disables this option. Range: 0..99%. </p>
</dl>
<p> <code>info_updates = &lt;n&gt;</code></p>
<dl>
<dd></dl>
<p> (Dynamic info updates)</p>
<dl>
<dd>Sets refresh rate for dynamic device parameters (e.g. bitrate) and the refresh interval for the Scan window (F3). Range: 1..60s. </p>
</dl>
<p> <code>override_auto_scale = (on|off)</code></p>
<dl>
<dd></dl>
<p> (Override scale autodetect)</p>
<dl>
<dd>Override the auto-scaling of the bar graphs and histogram, allowing you to set your own scales. </p>
</dl>
<p> <code>min_signal_level, max_signal_level = &lt;n&gt;</code></p>
<dl>
<dd></dl>
<p> (Minimum signal level, Maximum signal level)</p>
<dl>
<dd>Set the left and right boundaries of the signal level scales. Ranges: -128..-60dBm (minimum) and -59..120dBm (maximum). </p>
</dl>
<p> <code>min_noise_level, max_noise_level = &lt;n&gt;</code></p>
<dl>
<dd></dl>
<p> (Minimum noise level, Maximum noise level)</p>
<dl>
<dd>These work similar to the signal boundary settings. Ranges: -128..-60dBm (minimum) and -60..120dBm (maximum). </p>
</dl>
<p> <code>random = (on|off)</code></p>
<dl>
<dd></dl>
<p> (Random signals)</p>
<dl>
<dd>Switches on a fancy random generator for testing. </p>
</dl>
<p> <code>lo_threshold_action = (disabled|beep|flash|beep+flash)</code></p>
<dl>
<dd></dl>
<p> (Low threshold action)</p>
<dl>
<dd>Issue a warning at a given threshold at the lower end of the signal scale. It is meant for alarming you when a signal appears at the receiver. </p>
</dl>
<p> <code>lo_threshold = &lt;n&gt;</code></p>
<dl>
<dd></dl>
<p> (Low threshold)</p>
<dl>
<dd>Sets the threshold value for the &#8216;Low threshold action&#8217;. Range: -120..-60dBm. </p>
</dl>
<p> <code>hi_threshold_action = (disabled|beep|flash|beep+flash)</code></p>
<dl>
<dd></dl>
<p> (High threshold action)</p>
<dl>
<dd>Analogous to lo_threshold_action, only this time the threshold is at the upper end of the scale and the action is performed when the signal level drops below it. The acoustic signal is also different in order to be easily distinguishable from the lower one. Correctly adjusted, this little fellow will tell you when you should move closer to the base station. </p>
</dl>
<p> <code>hi_threshold = &lt;n&gt;</code></p>
<dl>
<dd></dl>
<p> (High threshold)</p>
<dl>
<dd>Sets the threshold for the &#8216;High threshold action&#8217;. Range: -59..120dBm. </p>
</dl>
<p> <code>startup_screen = (info|histogram|scan window)</code></p>
<dl>
<dd></dl>
<p> (Startup screen)</p>
<dl>
<dd>Which of the screens appears at program startup.</dl>
<h2>Author</h2>
<p>Written by Jan Morgenstern &lt;jan [at] jm-music.de&gt;.</p>
<h2>Reporting Bugs</h2>
<p>Send bug reports and/or suggestions to Gerrit Renker &lt;gerrit [at] erg.abdn.ac.uk&gt;.</p>
<h2>Copyright</h2>
<p>This is free software with ABSOLUTELY NO WARRANTY. See file COPYING for details.</p>
