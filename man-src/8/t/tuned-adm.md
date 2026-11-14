---
title: "tuned-adm(8)"
name: "tuned-adm"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tuned-adm/"
description: "tuned-adm – commandline tool for switching between different tuning profiles"
---

<p>tuned-adm &#8211; commandline tool for switching between different tuning profiles</p>
<h2>Synopsis</h2>
<p><code>tuned-adm </code> [<code>list</code> | <code>active</code> | <code>profile </code><i>&lt;profile&gt;</i> | <code>off</code> | <code>verify</code> | <code>recommend</code>] </p>
<h2>Description</h2>
<p>This command line utility allows you to switch between user definable tuning profiles. Several predefined profiles are already included. You can even create your own profile, either based on one of the existing ones by copying it or make a completely new one. The distribution provided profiles are stored in subdirectories below <i>/usr/lib/tuned</i> and the user defined profiles in subdirectories below <i>/etc/tuned</i>. If there are same profiles on both places, user defined profiles have precedence. </p>
<h2>Options</h2>
<h3>
<dt><code>list</code></p>
<dd></h3>
<p>List all available profiles. </p>
<dt><code>active</code></p>
<dd>Show current active profile. </p>
<dt><code>profile </code><i>PROFILE</i></p>
<dd>Switches to the given profilename. If none is given or no valid one is given the command gracefully exits without performing any operation. </p>
<dt><code>verify</code></p>
<dd>Verifies current profile against system settings. Outputs information whether system settings matches current profile or not (e.g. somebody modified sysfs/sysctl value by hand). Detailed information what is checked, what value is set and what value is expected can be found in the log. </p>
<dt><code>recommend</code></p>
<dd>Recommend profile suitable for your system. Currently only static detection is implemented &#8211; it decides according to data in /etc/system-release-cpe and virt-what output. The rules for autodetection are defined in recommend.conf in profile directory. They can be overriden by user by putting the recommend.conf into /etc/tuned. The default rules recommend profiles targeted to the best performance or balanced profile if unsure. </p>
<dt><code>off</code></p>
<dd>Unload tunings. </p>
</dl>
<h2>Files</h2>
<p>/etc/tuned/* /usr/lib/tuned/*</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tuned/">tuned</a></code>(8) <code><a href="/docs/linux/man/5-tuned-conf/">tuned-conf</a></code>(5) <code><a href="/docs/linux/man/7-tuned-profiles/">tuned-profiles</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-atomic/">tuned-profiles-atomic</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-sap/">tuned-profiles-sap</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-sap-hana/">tuned-profiles-sap-hana</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-oracle/">tuned-profiles-oracle</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-realtime/">tuned-profiles-realtime</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-nfv-host/">tuned-profiles-nfv-host</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-nfv-guest/">tuned-profiles-nfv-guest</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-compat/">tuned-profiles-compat</a></code>(7)</p>
<h2>Author</h2>
<p>Jaroslav Škarvada &lt;jskarvad [at] redhat.com&gt; Jan Kaluža &lt;jkaluza [at] redhat.com&gt; Jan Včelák &lt;jvcelak [at] redhat.com&gt; Marcela Mašláňová &lt;mmaslano [at] redhat.com&gt; Phil Knirsch &lt;pknirsch [at] redhat.com&gt;</p>
