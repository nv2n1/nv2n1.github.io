---
title: "disper(1)"
name: "disper"
section: "1"
letter: "d"
url: "/docs/linux/man/1-disper/"
description: "disper – on-the-fly display switcher"
---

<h2>NAME</h2>
<p> disper &#8211; on-the-fly display switcher</p>
<h2>SYNOPSIS</h2>
<p> <code>disper</code> [<i>options</i>] <i>(-l|-s|-c|-e|-p|-i)</i></p>
<h2>DESCRIPTION</h2>
<p> Disper re-routes your screen output to one or more connected displays. For example when giving a presentation, all one wants is that the beamer, which has just been connected, is able to show whatever you prepared. </p>
<p> There is the option to either clone all detected displays, or extend the desktop to them. Resolutions are automatically detected by default. For cloning, the highest resolution supported by all displays devices is chosen; for extending every display device gets its preferred or highest supported resolution. For special setups requiring more detailed control, one can still use the vendor-supplied display configuration utilities.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> show what&#8217;s happening</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> be quiet and only show errors</p>
<dt><code>-r</code> RESOLUTION, <code>&#8211;resolution</code>=<i>RESOLUTION</i></p>
<dd> set resolution, e.g. &quot;800&#215;600&quot;, or &quot;auto&quot; to detect the display&#8217;s preferred resolution, &quot;max&quot; to use the maximum resolution advertised, or &quot;off&quot; to disable the display entirely. For extend it is possible to enter a single resolution for all displays or a commaseparated list of resolutions (one for each display). Beware that many displays advertise resolutions they can not fully show, so &quot;max&quot; is not advised.</p>
<dt><code>-d</code> DISPLAYS, <code>&#8211;displays</code>=<i>DISPLAYS</i></p>
<dd> comma-separated list of displays to operate on, or &quot;auto&quot; to detect; the first is the primary display.</p>
<dt><code>-t</code> DIRECTION, <code>&#8211;direction</code>=<i>DIRECTION</i></p>
<dd> where to extend displays: &quot;left&quot;, &quot;right&quot;, &quot;top&quot;, or &quot;bottom&quot;</p>
<dt><code>&#8211;scaling</code>=<i>SCALING</i></p>
<dd> flat-panel scaling mode: &quot;default&quot;, &quot;native&quot;, &quot;scaled&quot;, &quot;centered&quot;, or &quot;aspect-scaled&quot;</p>
<dt><code>&#8211;plugins</code>=<i>PLUGINS</i></p>
<dd> comma-separated list of plugins to enable. Special names: &quot;user&quot; for all user plugins in ~/.config/disper/hooks; &quot;all&quot; for all plugins found; &quot;none&quot; for no plugins.</p>
<dt><code>&#8211;cycle-stages</code>=<i>CYCLE_STAGES</i></p>
<dd> colon-separated list command-line arguments to cycle through; &quot;-S:-c:-s&quot; by default</dl>
<h2>ACTIONS</h2>
<dl>
<dt>Select exactly one of the following actions</p>
<dd>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> list the attached displays</p>
<dt><code>-s</code>, <code>&#8211;single</code></p>
<dd> only enable the primary display</p>
<dt><code>-S</code>, <code>&#8211;secondary</code></p>
<dd> only enable the secondary display</p>
<dt><code>-c</code>, <code>&#8211;clone</code></p>
<dd> clone displays</p>
<dt><code>-e</code>, <code>&#8211;extend</code></p>
<dd> extend displays</p>
<dt><code>-p</code>, <code>&#8211;export</code></p>
<dd> export current settings to standard output</p>
<dt><code>-i</code>, <code>&#8211;import</code></p>
<dd> import current settings from standard input</p>
<dt><code>-C</code>, <code>&#8211;cycle</code></p>
<dd> cycle through the list of cycle stages</dl>
<h2>FILES</h2>
<p> <i>$XDG_CONFIG_HOME/disper/config</i> or <i>~/.config/disper/config</i> or <i>~/.disper/config</i></p>
<dl>
<dt>
<dd> Default command-line options to include at each disper invocation. Multiple lines are concatenated, and lines starting with <code>#</code> are ignored. A typical example might include:</p>
<dl>
<dt>
<dd>
<pre>
# enable all plugins in ~/.config/disper/hooks
--plugins=user
# cycle over clone and extend
--cycle-stages='-c : -e'
</pre>
</dl>
</dl>
<p> <i>$XDG_CONFIG_HOME/disper/hooks/</i> or <i>~/.config/disper/hooks/</i> or <i>~/.disper/hooks/</i></p>
<dl>
<dt>
<dd> Directory containing user hooks. These can be enabled with the <code>&#8211;plugins</code> option.</dl>
<p> <i>/usr/share/disper/hooks/</i></p>
<dl>
<dt>
<dd> Directory containing system hooks. User hooks take preference of system hooks or plugins.</dl>
<h2>CYCLE</h2>
<p> There is a possibility to cycle between different setups with a single disper invocation using the option <code>&#8211;cycle</code>. The options to cycle through are specified by the option <code>&#8211;cycle-stages</code>, which consists of a colon-separated list of disper options. To alternate, for example, between clone and extend, one could use</p>
<dl>
<dt>
<dd>
<pre>
<code>disper --cycle-stages='-e : -c' --cycle</code>
</pre>
</dl>
<p> Currently the last selected stage is stored in the file <i>$XDG_CONFIG_HOME/disper/last_cycle_stage</i> (actually the file <i>last_cycle_stage</i> in the directory of the last configuration file read). This means that when display configuration is modified by something else than disper (for example by restarting the computer), cycling will continue from where it was last time, not necessarily from the current display configuration. This is something that may change in the future.</p>
<h2>PLUGINS</h2>
<p> It is possible to execute user-supplied hooks on display switch, for example to display a notification or change the wallpaper. Which ones are enabled is specified by the <code>&#8211;plugins</code> option. System hooks are located in <code>/usr/share/disper/hooks/</code> while user hooks should be placed in <code>$XDG_CONFIG_HOME/disper/hooks</code> (or <code>~/.config/disper/hooks/</code> or <code>~/.disper/hooks/</code>). </p>
<p> Each hook is an executable file (which includes scripts). The following environment variables are available when invoked:</p>
<dl>
<dt><i>DISPER_VERSION</i></p>
<dd> Version of disper (0.3.1).</p>
<dt><i>DISPER_LOG_LEVEL</i></p>
<dd> Log level: 0 (quiet), 1 (normal) or 2 (verbose).</p>
<dt><i>DISPER_STAGE</i></p>
<dd> Execution stage: <code>prepare</code> or <code>switch</code>. Most plugins will only need to act on the <code>switch</code> stage, which is just after the display switch has happened. Please make sure to execute an action only on <code>switch</code> for future compatibility. (There are ideas for <code>import</code> and <code>export</code> as well.)</p>
<dt><i>DISPER_DISPLAYS</i></p>
<dd> Space-separated list of displays that have output. These names may be slightly different from what disper uses internally because they have to be valid environment variable names. (e.g. DFP_0 CRT_0)</p>
<dt><i>DISPER_LAYOUT</i></p>
<dd> One of: <code>clone</code>, <code>top</code>, <code>right</code>, <code>bottom</code> or <code>left</code>.</p>
<dt><i>DISPER_BB_RESOLUTION</i></p>
<dd> Size of full bounding box (e.g. 1024&#215;768).</dl>
<p> For each of <i>DISPER_DISPLAYS</i> the resolution of the corresponding display is supplied as well. If only DFP-0 would be attached, <i>DISPER_DISPLAYS</i> would contain just DFP_0 and the following variables would be set as well:</p>
<dl>
<dt><i>DISPER_RESOLUTION_DFP_0</i></p>
<dd> Resolution of display DFP-0 (e.g. 1024&#215;768).</dl>
<p> If you want to write your own hook you can also look at the ones supplied with disper in /usr/share/disper/hooks/.</p>
<h2>AUTHOR</h2>
<p> Written by Willem van Engen.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xrandr/">xrandr</a></code>(1), <code><a href="/docs/linux/man/1-nvidia-settings/">nvidia-settings</a></code>(1) </p>
<h2>Index</h2>
