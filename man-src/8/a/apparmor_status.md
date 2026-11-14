---
title: "apparmor_status(8)"
name: "apparmor_status"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apparmor_status/"
description: "aa-status – display various information about the current AppArmor policy."
---

<p>aa-status &#8211; display various information about the current AppArmor policy.</p>
<h2>Synopsis</h2>
<p><code>aa-status</code> [option]</p>
<h2>Description</h2>
<p><code>aa-status</code> will report various aspects of the current state of AppArmor confinement. By default, it displays the same information as if the <i>&#8211;verbose</i> argument were given. A sample of what this looks like is: </p>
<pre> apparmor module is loaded.
 110 profiles are loaded.
 102 profiles are in enforce mode.
 8 profiles are in complain mode.
 Out of 129 processes running:
 13 processes have profiles defined.
 8 processes have profiles in enforce mode.
 5 processes have profiles in complain mode.</pre>
<p>Other argument options are provided to report individual aspects, to support being used in scripts.</p>
<h2>Options</h2>
<p><code>aa-status</code> accepts only one argument at a time out of:</p>
<dl>
<dt>&#8211;enabled</p>
<dd>returns error code if AppArmor is not enabled.</p>
<dt>&#8211;profiled</p>
<dd>displays the number of loaded AppArmor policies.</p>
<dt>&#8211;enforced</p>
<dd>displays the number of loaded enforcing AppArmor policies.</p>
<dt>&#8211;complaining</p>
<dd>displays the number of loaded non-enforcing AppArmor policies.</p>
<dt>&#8211;kill</p>
<dd>displays the number of loaded enforcing AppArmor policies that will kill tasks on policy violations.</p>
<dt>&#8211;special-unconfined</p>
<dd>displays the number of loaded non-enforcing AppArmor policies that are in the special unconfined mode.</p>
<dt>&#8211;process-mixed displays the number of processes confined by profile stacks with profiles in different modes.</p>
<dd>
<dt>&#8211;verbose</p>
<dd>displays multiple data points about loaded AppArmor policy set (the default action if no arguments are given).</p>
<dt>&#8211;json</p>
<dd>displays multiple data points about loaded AppArmor policy set in a <font SIZE="-1">JSON</font> format, fit for machine consumption.</p>
<dt>&#8211;pretty-json</p>
<dd>same as &#8211;json, formatted to be readable by humans as well as by machines.</p>
<dt>&#8211;help</p>
<dd>displays a short usage statement.</dl>
<h2>Exit Status</h2>
<p>Upon exiting, <code>aa-status</code> will set its exit status to the following values:</p>
<dl>
<dt><code>0</code></p>
<dd>if apparmor is enabled and policy is loaded.</p>
<dt><code>1</code></p>
<dd>if apparmor is not enabled/loaded.</p>
<dt><code>2</code></p>
<dd>if apparmor is enabled but no policy is loaded.</p>
<dt><code>3</code></p>
<dd>if the apparmor control files aren&#8217;t available under /sys/kernel/security/.</p>
<dt><code>4</code></p>
<dd>if the user running the script doesn&#8217;t have enough privileges to read the apparmor control files.</p>
<dt><code>42</code></p>
<dd>if an internal error occurred.</dl>
<h2>Bugs</h2>
<p><code>aa-status</code> must be run as root to read the state of the loaded policy from the apparmor module. It uses the /proc filesystem to determine which processes are confined and so is susceptible to race conditions. </p>
<p> If you find any additional bugs, please report them at &lt;<a rel="nofollow" href="https://gitlab.com/apparmor/apparmor/-/issues">https://gitlab.com/apparmor/apparmor/-/issues</a>&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-apparmor/">apparmor</a></code>(7), <code><a href="/docs/linux/man/5-apparmor-d/">apparmor.d</a></code>(5), and &lt;<a rel="nofollow" href="https://wiki.apparmor.net">https://wiki.apparmor.net</a>&gt;. </p>
