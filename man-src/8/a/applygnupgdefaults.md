---
title: "applygnupgdefaults(8)"
name: "applygnupgdefaults"
section: "8"
letter: "a"
url: "/docs/linux/man/8-applygnupgdefaults/"
description: "applygnupgdefaults – Run gpgconf –apply-defaults for all users."
---

<p><code>applygnupgdefaults</code> &#8211; Run gpgconf &#8211;apply-defaults for all users.</p>
<h2>Synopsis</h2>
<p><code>applygnupgdefaults</code> </p>
<h2>Description</h2>
<p>This script is a wrapper around <code>gpgconf</code> to run it with the command <code>&#8211;apply-defaults</code> for all real users with an existing GnuPG home directory. Admins might want to use this script to update he GnuPG configuration files for all users after &#8216;<i>/etc/gnupg/gpgconf.conf</i>&#8216; has been changed. This allows enforcing certain policies for all users. Note, that this is not a bulletproof way to force a user to use certain options. A user may always directly edit the configuration files and bypass gpgconf. <code>applygnupgdefaults</code> is invoked by root as:</p>
<dl>
<dd>
<pre>applygnupgdefaults</pre>
</dl>
