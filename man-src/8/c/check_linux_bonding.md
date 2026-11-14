---
title: "check_linux_bonding(8)"
name: "check_linux_bonding"
section: "8"
letter: "c"
url: "/docs/linux/man/8-check_linux_bonding/"
description: "check_linux_bonding – Nagios plugin for checking the status of bonded network interfaces (masters and slaves) on Linux servers."
---

<p>check_linux_bonding &#8211; Nagios plugin for checking the status of bonded network interfaces (masters and slaves) on Linux servers.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>check_linux_bonding</code> [<i>option</i>&#8230;]</dl>
<h2>Description</h2>
<p><code>check_linux_bonding</code></p>
<dd>is a plugin for the Nagios monitoring software that checks bonding interfaces on Linux. The plugin is fairly simple and will report any interfaces that are down (both masters and slaves). It will also alert you of bonding interfaces with only one slave, since that usually points to a misconfiguration. If no bonding interfaces are detected, the plugin will exit with an OK value (modifiable with the <code>&#8211;no-bonding</code> option). It is therefore safe to run this plugin on all your Linux machines:</p>
<dl>
<dd>
<pre>$ ./check_linux_bonding
OK: No bonding interfaces found</pre>
</dl>
<p> The plugin will first try to use the sysfs (/sys) filesystem to detect bonding interfaces. If that does not work, i.e. the kernel or bonding module is too old for the necessary files to exist, the plugin will use procfs (/proc) as a fallback. The plugin supports an unlimited number of bonding interfaces. In the OK output, the plugin will indicate which of the slaves is active with an exclamation mark &#8220;!&#8221;, if applicable. If one of the slaves is configured as primary, this is indicated with an asterisk &#8220;*&#8221;:</p>
<dl>
<dd>
<pre>$ ./check_linux_bonding
Interface bond0 is UP: mode=1 (active-backup), 2 slaves: eth0*, eth1!</pre>
</dl>
<h2>Options</h2>
<p><code>-b</code>, <code>&#8211;blacklist </code><i>string</i><code> | </code><i>file</i></p>
<dl>
<dd>Blacklist one or more interfaces. The option can be specified multiple times. If the argument is a file, the file is expected to contain a single line with the same syntax, i.e.: </p>
<dl>
<dd>
<pre><i>interface1</i>,<i>interface2</i>,...</pre>
</dl>
<p> Examples: </p>
<dl>
<dd>
<pre>check_linux_bonding -b bond1 -b eth1
check_linux_bonding -b bond1,eth1
check_linux_bonding -b /etc/check_linux_bonding.black</pre>
</dl>
</dl>
<p> <code>-n</code>, <code>&#8211;no-bonding </code><i>string</i></p>
<dl>
<dd>This option lets you specify the return value of the plugin if no bonding interfaces are found. The option expects &#8220;ok&#8221;, &#8220;warning&#8221;, &#8220;critical&#8221; or &#8220;unknown&#8221; as the argument. Default is &#8220;ok&#8221; if the option is not present.</dl>
<p> <code>&#8211;slave-down</code> <i>string</i></p>
<dl>
<dd>This option lets you specify the return value of the plugin if a slave interface is down. The option expects &#8220;ok&#8221;, &#8220;warning&#8221;, &#8220;critical&#8221; or &#8220;unknown&#8221; as the argument. Default is &#8220;warning&#8221; if the option is not present.</dl>
<p> <code>-t</code>, <code>&#8211;timeout </code><i>seconds</i></p>
<dl>
<dd>The number of seconds after which the plugin will abort. Default timeout is 5 seconds if the option is not present.</dl>
<p> <code>-s</code>, <code>&#8211;state</code></p>
<dl>
<dd>Prefix each alert with its corresponding service state (i.e. warning, critical etc.). This is useful in case of several alerts from the same monitored system.</dl>
<p> <code>-S</code>, <code>&#8211;short-state</code></p>
<dl>
<dd>Same as the <code>&#8211;state</code> option above, except that the state is abbreviated to a single letter (<i>W</i>=warning, <i>C</i>=critical etc.).</dl>
<p> <code>&#8211;ignore-num-ad</code></p>
<dl>
<dd>Only relevant for IEEE 802.3ad type bonding. Turning on this option instructs the plugin to not issue a warning if the number of AD ports are not equal to the number of slaves. Usually you&#8217;ll want the default behaviour, but if your 802.3ad bonding device is bound on more than one switch, you&#8217;ll want to use this option to avoid false positives.</dl>
<p> <code>&#8211;linebreak</code> <i>string</i></p>
<dl>
<dd>check_linux_bonding will sometimes report more than one line, e.g. if there are several alerts. If the script has a TTY, it will use regular linebreaks. If not (which is the case with NRPE) it will use HTML linebreaks. Sometimes it can be useful to control what the plugin uses as a line separator, and this option provides that control. </p>
<p> The argument is the exact string to be used as the line separator. There are two exceptions, i.e. two keywords that translates to the following: </p>
<p> <i>REG</i>: Regular linebreaks, i.e. &#8220;
&#8221;. </p>
<p> <i>HTML</i>: HTML linebreaks, i.e. &#8220;&lt;br/&gt;&#8221;. </p>
<p> This is a rather special option that is normally not needed. The default behaviour should be sufficient for most users.</dl>
<p> <code>&#8211;disable-sysfs</code></p>
<dl>
<dd>Sometimes the information in /sys is partly absent or deficient, and the plugin is unable to detect this discrepancy and reports errors. This usually happens with old Linux kernels and Xen domain-0 systems. This option exists as a workaround. If specified, this option will make the plugin ignore the /sys filesystem alltogether and use the /proc filesystem instead.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Verbose output. Will report status on all bonding interfaces, regardless of their alert state.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Print version info and exit.</dl>
<h2>Diagnostics</h2>
<p>The option <code>-v</code> or <code>&#8211;verbose</code> can be specified to display all bonding interfaces.</p>
<h2>Dependencies</h2>
<p>This plugin depends on sysfs and fallbacks to procfs. Without these filesystems the plugin will not find any bonding interfaces.</p>
<h2>Exit Status</h2>
<p>If no errors are discovered, a value of 0 (OK) is returned. An exit value of 1 (WARNING) signifies one or more non-critical errors, while 2 (CRITICAL) signifies one or more critical errors. </p>
<p> The exit value 3 (UNKNOWN) is reserved for errors within the script, or errors getting values sysfs or procfs.</p>
<h2>Bugs And Limitations</h2>
<p>None known at present.</p>
<h2>Incompatibilities</h2>
<p>The plugin is only compatible with the Linux operating system.</p>
<h2>License And Copyright</h2>
<p>This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program. If not, see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a></p>
<h2>See Also</h2>
<p><a rel="nofollow" href="http://folk.uio.no/trondham/software/check_linux_bonding.html">http://folk.uio.no/trondham/software/check_linux_bonding.html</a></p>
<h2>Authors</h2>
<p><code>Trond Hasle Amundsen &lt;t.h.amundsen [at] usit.uio.no&gt;</code></p>
