---
title: "tuned-main-conf(5)"
name: "tuned-main-conf"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tuned-main-conf/"
description: "tuned-main.conf – Tuned global configuration file"
---

<p>tuned-main.conf &#8211; Tuned global configuration file</p>
<h2>Synopsis</h2>
<p><code>/etc/tuned/tuned-main.conf</code></p>
<h2>Description</h2>
<p>This man page documents format of the Tuned global configuration file. The <i>tuned-main.conf</i> file uses the ini-file format.</p>
<dl>
<dt><code>daemon=</code><i>BOOL</i></p>
<dd>This defines whether Tuned will use daemon or not. It is boolean value. It can be <code>True</code> or <code>1</code> if the daemon is enabled and <code>False</code> or <code>0</code> if disabled. It is not recommended to disable daemon, because many functions will not work without daemon, e.g. there will be no D-Bus, no settings rollback, no hotplug support, no dynamic tuning, &#8230;</p>
<dt><code>dynamic_tuning=</code><i>BOOL</i></p>
<dd>This defines whether the dynamic tuning is enabled. It is boolean value. It can be <code>True</code> or <code>1</code> if the dynamic tuning is enabled and <code>False</code> or <code>0</code> if disabled. In such case only the static tuning will be used. Please note if it is enabled here, it is still possible to individually disable it in plugins. It is only applicable if <code>daemon</code> is enabled.</p>
<dt><code>sleep_interval=</code><i>INT</i></p>
<dd>Tuned daemon is periodically waken after <i>INT</i> seconds and checks for events. By default this is set to 1 second. If you have Python 2 interpreter with applied patch from Red Hat Bugzilla #917709 this controls responsiveness time of Tuned to commands (i.e. if you request profile switch, it may take up to 1 second until Tuned reacts). Increase this number for higher responsiveness times and more power savings (due to lower number of wakeups). In case you have unpatched Python 2 interpreter, this settings will have no visible effect, because the intepreter will poll 20 times per second. It is only applicable if <code>daemon</code> is enabled.</p>
<dt><code>update_interval=</code><i>INT</i></p>
<dd>Update interval for dynamic tuning (in seconds). Tuned daemon is periodically waken after <i>INT</i> seconds, updates its monitors, calculates new tuning parameters for enabled plugins and applies the changes. Plugins that have disabled dynamic tuning are not processed. By default the <i>INT</i> is set to 10 seconds. Tuned daemon doesn&#8217;t periodically wake if dynamic tuning is globally disabled (see <code>dynamic_tuning</code>) or this setting set to 0. This must be multiple of <code>sleep_interval</code>. It is only applicable if <code>daemon</code> is enabled. </p>
<pre><code>recommend_command=BOOL


This controls whether recommend functionality will be enabled or not. It is
boolean value. It can be True or 1 if the recommend command is
enabled and False or 0 if disabled. If disabled recommend
command will be not available in CLI, tuned will not parse recommend.conf
and will return one hardcoded profile (by default balanced). It is only
applicable if daemon is enabled. By default it's set to True.</code></pre>
<dt><code>reapply_sysctl=</code><i>BOOL</i></p>
<dd>This controls whether to reapply sysctl settings from the <i>/etc/sysctl.conf</i>, <i>/etc/sysctl.d/*.conf</i>, <i>/usr/lib/sysctl.d/*.conf</i>, <i>/usr/local/lib/sysctl.d/*.conf</i>, <i>/lib/sysctl.d/*.conf</i>, <i>/run/sysctl.d/*.conf</i>, i.e. all locations supported by <code>sysctl &#8211;system</code> after Tuned sysctl settings are applied, i.e. if set to <code>True</code> or <code>1</code> Tuned sysctl settings will not override system sysctl settings. If set to <code>False</code> or <code>0</code> Tuned sysctl settings will override system sysctl settings. By defualt it&#8217;s set to <code>True</code>.</p>
<dt><code>default_instance_priority=</code><i>INT</i></p>
<dd>Default instance (unit) priority. By default it&#8217;s <code>0</code>. Each unit has a priority which is by default preset to the <i>INT</i>. It can be overridden in the Tuned profile by the <code>priority</code> option. Tuned units are processed in order defined by their priorities, i.e. unit with the lowest number is processed as the first. </p>
<h2>Example</h2>
<pre><code>no_daemon = 0
dynamic_tuning = 1
sleep_interval = 1
update_interval = 10
recommend_command = 0
reapply_sysctl = 1
default_instance_priority = 0
</code></pre>
<h2>Files</h2>
<p><i>/etc/tuned/tuned-main.conf</i></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-tuned/">tuned</a>(8)</p>
<h2>Author</h2>
<p>Written by Jaroslav Škarvada &lt;jskarvad [at] redhat.com&gt;.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://bugzilla.redhat.com/.">https://bugzilla.redhat.com/.</a></p>
