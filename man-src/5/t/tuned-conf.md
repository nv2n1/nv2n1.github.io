---
title: "tuned-conf(5)"
name: "tuned-conf"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tuned-conf/"
description: "tuned.conf – Tuned profile definition"
---

<p>tuned.conf &#8211; Tuned profile definition</p>
<h2>Description</h2>
<p>This man page documents format of Tuned 2.0 profile definition files. Profile is stored in /etc/tuned/&lt;profile_name&gt;/tuned.conf or in /usr/lib/tuned/&lt;profile_name&gt;/tuned.conf file where the /etc/tuned/ directory has higher priority. The <code>tuned.conf</code> configures the profile and it is in ini-file format. </p>
<h2>Main Section</h2>
<p>The main section is called &quot;[main]&quot; and can contain following options: </p>
<dl>
<dt>include=</p>
<dd>Includes config file defined as value. Config file can be defined as full path or by the profile name to which it belongs. If this parameter is present, the histogram will be shown at the end of the measurement. </p>
</dl>
<h2>Plugins</h2>
<p>Every other section defines one plugin. The name of the section is used as name for the plugin and is used in logs to identify the plugin. There can be only one plugin of particular type tuning particular device. Conflicts are by default fixed by merging the options of both plugins together. This can be changed by &quot;replace&quot; option. </p>
<p> Every plugin section can contain following sections: </p>
<dl>
<dt>type=</p>
<dd>Plugin type. Currently there are following upstream plugins: audio, bootloader, cpu, disk, eeepc_she, mounts, net script, selinux, scheduler, sysctl, sysfs, usb, video, vm. This list may be incomplete. If you installed tuned through RPM you can list upstream plugins by the following command: <code>rpm -ql tuned | grep &#8216;plugins/plugin_.*.py$&#8217;</code> Check the plugins directory returned by this command to see all plugins (e.g. plugins provided by 3rd party packages). </p>
<dt>devices=</p>
<dd>Comma separated list of devices which should be tuned by this plugin instance. If you omit this option, all found devices will be tuned.</p>
<dt>replace=1</p>
<dd>If there is conflict between two plugins (meaning two plugins of the same type are trying to configure the same devices), then the plugin defined as last replaces all options defined by the previosly defined plugin.</dl>
<p> Plugins can also have plugin related options.</p>
<h2>Example</h2>
<p>[main] # Includes plugins defined in &quot;included&quot; profile. include=included # Define my_sysctl plugin [my_sysctl] type=sysctl # This plugin will replace any sysctl plugin defined in &quot;included&quot; profile replace=1 # 256 KB default performs well experimentally. net.core.rmem_default = 262144 net.core.wmem_default = 262144 # Define my_script plugin # Both scripts (profile.sh from this profile and script from &quot;included&quot; # profile) will be run, because if there is no &quot;replace=1&quot; option the # default action is merge. [my_script] type=script script=profile.sh </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-tuned/">tuned</a>(8)</p>
<h2>Author</h2>
<p>Written by Jan Kaluža &lt;jkaluza [at] redhat.com&gt;.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://bugzilla.redhat.com/.">https://bugzilla.redhat.com/.</a></p>
