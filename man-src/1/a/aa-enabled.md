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
<dt>-h, &#8211;help</dt>
<dd> Display a brief usage guide.</dd>
<dt>-q, &#8211;quiet</dt>
<dd> Do not output anything to stdout. This option is intended to be used by scripts that simply want to use the exit code to determine if AppArmor is enabled.</dd>
<dt>-x, &#8211;exclusive</dt>
<dd> Require AppArmor to have exclusive access to shared <font SIZE="-1">LSM</font> interfaces to be considered enabled.</dd></dl>
<h2>EXIT STATUS</h2>
<p> Upon exiting, <code>aa-enabled</code> will set its exit status to the following values:</p>
<dl>
<dt><code>0</code></dt>
<dd> if AppArmor is enabled.</dd>
<dt><code>1</code></dt>
<dd> if AppArmor is not enabled/loaded.</dd>
<dt><code>2</code></dt>
<dd> intentionally not used as an <code>aa-enabled</code> exit status.</dd>
<dt><code>3</code></dt>
<dd> if the AppArmor control files aren&#8217;t available under /sys/kernel/security/.</dd>
<dt><code>4</code></dt>
<dd> if <code>aa-enabled</code> doesn&#8217;t have enough privileges to read the apparmor control files.</dd>
<dt><code>10</code></dt>
<dd> AppArmor is enabled but does not have access to shared <font SIZE="-1">LSM</font> interfaces.</dd>
<dt><code>64</code></dt>
<dd> if any unexpected error or condition is encountered.</dd></dl>
<h2>BUGS</h2>
<p> If you find any bugs, please report them at &lt;<a rel="nofollow" href="https://gitlab.com/apparmor/apparmor/-/issues">https://gitlab.com/apparmor/apparmor/-/issues</a>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-apparmor/">apparmor</a></code>(7), <code><a href="/docs/linux/man/5-apparmor-d/">apparmor.d</a></code>(5), <code>aa_is_enabled</code>(2), and &lt;<a rel="nofollow" href="https://wiki.apparmor.net">https://wiki.apparmor.net</a>&gt;. </p>
