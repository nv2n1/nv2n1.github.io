---
title: "aa-enabled(1)"
name: "aa-enabled"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aa-enabled/"
description: "aa-enabled – test whether AppArmor is enabled"
---

<h2 class="name">NAME</h2>
<p> aa-enabled &#8211; test whether AppArmor is enabled </p>
<h2>SYNOPSIS</h2>
<p> <code>aa-enabled</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>aa-enabled</code> is used to determine if AppArmor is enabled.</p>
<h2>OPTIONS</h2>
<p> <code>aa-enabled</code> accepts the following arguments:</p>
<dl>
<dt>-h, &#8211;help</p>
<dd> Display a brief usage guide.</p>
<dt>-q, &#8211;quiet</p>
<dd> Do not output anything to stdout. This option is intended to be used by scripts that simply want to use the exit code to determine if AppArmor is enabled.</p>
<dt>-x, &#8211;exclusive</p>
<dd> Require AppArmor to have exclusive access to shared <font SIZE="-1">LSM</font> interfaces to be considered enabled.</dl>
<h2>EXIT STATUS</h2>
<p> Upon exiting, <code>aa-enabled</code> will set its exit status to the following values:</p>
<dl>
<dt><code>0</code></p>
<dd> if AppArmor is enabled.</p>
<dt><code>1</code></p>
<dd> if AppArmor is not enabled/loaded.</p>
<dt><code>2</code></p>
<dd> intentionally not used as an <code>aa-enabled</code> exit status.</p>
<dt><code>3</code></p>
<dd> if the AppArmor control files aren&#8217;t available under /sys/kernel/security/.</p>
<dt><code>4</code></p>
<dd> if <code>aa-enabled</code> doesn&#8217;t have enough privileges to read the apparmor control files.</p>
<dt><code>10</code></p>
<dd> AppArmor is enabled but does not have access to shared <font SIZE="-1">LSM</font> interfaces.</p>
<dt><code>64</code></p>
<dd> if any unexpected error or condition is encountered.</dl>
<h2>BUGS</h2>
<p> If you find any bugs, please report them at &lt;<a rel="nofollow" href="https://gitlab.com/apparmor/apparmor/-/issues">https://gitlab.com/apparmor/apparmor/-/issues</a>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-apparmor/">apparmor</a></code>(7), <code><a href="/docs/linux/man/5-apparmor-d/">apparmor.d</a></code>(5), <code><a href="/docs/linux/man/2-aa_is_enabled/">aa_is_enabled</a></code>(2), and &lt;<a rel="nofollow" href="https://wiki.apparmor.net">https://wiki.apparmor.net</a>&gt;. </p>
<h2>Index</h2>
