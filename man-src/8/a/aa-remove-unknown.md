---
title: "aa-remove-unknown(8)"
name: "aa-remove-unknown"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aa-remove-unknown/"
description: "aa-remove-unknown – remove unknown AppArmor profiles"
---

<p>aa-remove-unknown &#8211; remove unknown AppArmor profiles</p>
<h2>Synopsis</h2>
<p><code>aa-remove-unknown</code> [option]</p>
<h2>Description</h2>
<p><code>aa-remove-unknown</code> will inventory all profiles in /etc/apparmor.d/, compare that list to the profiles currently loaded into the kernel, and then remove all of the loaded profiles that were not found in /etc/apparmor.d/. It will also report the name of each profile that it removes on standard out.</p>
<h2>Options</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd>displays a short usage statement.</p>
<dt>-n</p>
<dd>dry run; only prints the names of profiles that would be removed</dl>
<h2>Examples</h2>
<pre> $ sudo ./aa-remove-unknown -n
 Would remove 'test//null-/usr/bin/whoami'
 Would remove 'test'
 $ sudo ./aa-remove-unknown
 Removing 'test//null-/usr/bin/whoami'
 Removing 'test'</pre>
<h2>Bugs</h2>
<p>None. Please report any you find to Gitlab at &lt;<a rel="nofollow" href="https://gitlab.com/apparmor/apparmor/-/issues">https://gitlab.com/apparmor/apparmor/-/issues</a>&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-apparmor/">apparmor</a></code>(7) </p>
