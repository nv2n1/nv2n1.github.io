---
title: "vlock-main(8)"
name: "vlock-main"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vlock-main/"
description: "vlock-main – lock current virtual console"
---

<p>vlock-main &#8211; lock current virtual console</p>
<h2>Synopsis</h2>
<p><code>vlock-main [plugins&#8230;]</code></p>
<h2>Description</h2>
<p><code>vlock-main</code> is part of <a href="/docs/linux/man/1-vlock/">vlock</a>(1), the Virtual Console locking program for Linux. It locks the current session and will only exit if the current user can authenticate themselves. The root user will also be able to unlock the session, unless disabled at compile time. The command line arguments specify plugins that should be loaded by vlock-main. See <a href="/docs/linux/man/5-vlock-plugins/">vlock-plugins</a>(5) for more information. </p>
<p> If plugin support is disabled at compile time, the only supported argument is &quot;all&quot;.</p>
<h2>Environment Variables</h2>
<p>The following environment variables can be used to change the behavior of vlock-main: </p>
<p> <code>USER</code></p>
<dl>
<dd>If this variable is when vlock-main is run as root (uid 0) vlock locks the screen as this user instead of root. The root password will still be able to unlock the session, unless disabled at compile time.</dl>
<p> <code>VLOCK_ALL_MESSAGE</code></p>
<dl>
<dd>If this variable is set and all consoles are locked its contents will be used as the locking message instead of the default message.</dl>
<p> <code>VLOCK_CURRENT_MESSAGE</code></p>
<dl>
<dd>If this variable is set and only the current consoles is locked its contents will be used as the locking message instead of the default message.</dl>
<p> <code>VLOCK_MESSAGE</code></p>
<dl>
<dd>If this variable is set its contents will be used as the locking message instead of the default. This overrides the former two variables.</dl>
<p> <code>VLOCK_TIMEOUT</code></p>
<dl>
<dd>Set this variable to specify the timeout (in seconds) after which the screen saver plugins (if any) will be invoked. If this variable is unset or set to an invalid value or 0 no timeout is used. See <a href="/docs/linux/man/5-vlock-plugins/">vlock-plugins</a>(5) for more information about plugins.</dl>
<p> <code>VLOCK_PROMPT_TIMEOUT</code></p>
<dl>
<dd>Set this variable to specify the amount of time (in seconds) you will have to enter your password at the password prompt. If this variable is unset or set to an invalid value or 0 no timeout is used. <code>Warning</code>: If this value is too low, you may not be able to unlock your session.</dl>
<h2>Signals</h2>
<p>Several signals are ignored. <code>vlock-main</code> will try to exit cleanly if SIGTERM is received.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-vlock/">vlock</a></code>(1), <code><a href="/docs/linux/man/5-vlock-plugins/">vlock-plugins</a></code>(5)</p>
<h2>Authors</h2>
<p>Frank Benkstein &lt;frank-vlock [at] benkstein.net&gt;</p>
