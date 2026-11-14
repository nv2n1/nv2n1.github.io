---
title: "subdomain-conf(5)"
name: "subdomain-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-subdomain-conf/"
description: "/etc/apparmor/subdomain.conf – configuration file for fine-tuning the behavior of the AppArmor security tool."
---

<p>/etc/apparmor/subdomain.conf &#8211; configuration file for fine-tuning the behavior of the AppArmor security tool.</p>
<h2>Description</h2>
<p>The AppArmor security tool can be configured to have certain default behaviors based on configuration options set in subdomain.conf. There are two variables that can be set in subdomain.conf: <font SIZE="-1"><code>SUBDOMAIN_PATH</code></font>, and <font SIZE="-1"><code>SUBDOMAIN_MODULE_PANIC</code></font>.</p>
<h3><font SIZE="-1">SUBDOMAIN_PATH</font></h3>
<p>This variable accepts a string (path), and is by default set to &#8216;/etc/apparmor.d/&#8217; This variable defines where the AppArmor security tool looks for its policy definitions (a.k.a. AppArmor profiles).</p>
<h3><font SIZE="-1">SUBDOMAIN_MODULE_PANIC</font></h3>
<p>This variable accepts a string that is one of four values: <i>warn</i>, <i>build</i>, <i>panic</i>, or <i>build-panic</i>, and is set by default to <i>warn</i>. </p>
<p> This setting controls the behavior of the AppArmor initscript if it cannot successfully load the AppArmor kernel module on startup. The four possible settings are:</p>
<dl>
<dt><i>warn</i></p>
<dd>Log a failure message (the default behavior).</p>
<dt><i>build</i></p>
<dd>Attempt to build the AppArmor module against the currently running kernel. If the compilation is successful, the module will be loaded and AppArmor started; if the compilation fails, a failure message is logged.</p>
<dt><i>panic</i></p>
<dd>Log a failure message and drop to runlevel 1 (single user).</p>
<dt><i>build-panic</i></p>
<dd>Attempt to build the module against the running kernel (like <i>build</i>) and if the compilation fails, drop to runlevel 1 (single user).</dl>
<h2>Bugs</h2>
<p>Setting the initscript to recompile the module will fail on <font SIZE="-1">SUSE,</font> as the module source is no longer installed by default. However, the module has been included with the <font SIZE="-1">SUSE</font> kernel, so no rebuilding should be necessary. </p>
<p> If you find any additional bugs, please report them at &lt;<a rel="nofollow" href="https://bugs.launchpad.net/apparmor/+filebug">https://bugs.launchpad.net/apparmor/+filebug</a>&gt;.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/7-apparmor/">apparmor</a></i>(7), <i><a href="/docs/linux/man/8-apparmor_parser/">apparmor_parser</a></i>(8), and &lt;<a rel="nofollow" href="http://wiki.apparmor.net">http://wiki.apparmor.net</a>&gt;. </p>
