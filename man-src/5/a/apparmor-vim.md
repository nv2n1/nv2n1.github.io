---
title: "apparmor-vim(5)"
name: "apparmor-vim"
section: "5"
letter: "a"
url: "/docs/linux/man/5-apparmor-vim/"
description: "apparmor.vim – vim syntax highlighting file for AppArmor profiles"
---

<p>apparmor.vim &#8211; vim syntax highlighting file for AppArmor profiles</p>
<h2>Synopsis</h2>
<p>Your system may be configured to automatically use syntax highlighting for installed AppArmor policies. If not, you can enable syntax highlighting in a specific vim session by performing: </p>
<pre> :set syntax=apparmor</pre>
<h2>Description</h2>
<p><code>apparmor.vim</code> provides syntax highlighting rules for the <code><a href="/docs/linux/man/1-vim/">vim</a></code>(1) text editor; the rules provide an easy visual method to inspect AppArmor profiles for syntax correctness and semantics. </p>
<p> The colors indicate the relative severity of granting a specific set of privileges. Ranking access with colors is necessarily generic and vague, but it may help you understand your profiles better.</p>
<h2>Bugs</h2>
<p><code>apparmor.vim</code> does not properly detect dark versus light backgrounds. Patches accepted. If you find any bugs, please report them at &lt;<a rel="nofollow" href="https://gitlab.com/apparmor/apparmor/-/issues">https://gitlab.com/apparmor/apparmor/-/issues</a>&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-vim/">vim</a></code>(1), <code><a href="/docs/linux/man/7-apparmor/">apparmor</a></code>(7), <code><a href="/docs/linux/man/5-apparmor-d/">apparmor.d</a></code>(5), <code><a href="/docs/linux/man/2-aa_change_hat/">aa_change_hat</a></code>(2), and &lt;<a rel="nofollow" href="https://wiki.apparmor.net">https://wiki.apparmor.net</a>&gt;. </p>
