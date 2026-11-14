---
title: "systemd-ask-password(1)"
name: "systemd-ask-password"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-ask-password/"
description: "systemd-ask-password – Query the user for a system password"
---

<h2 class="name">NAME</h2>
<p> systemd-ask-password &#8211; Query the user for a system password </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-ask-password </code><code>[OPTIONS&#8230;]</code><code>[MESSAGE]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-ask-password</code></p>
<dd>may be used to query a system password or passphrase from the user, using a question message specified on the command line. When run from a TTY it will query a password on the TTY and print it to standard output. When run with no TTY or with <code>&#8211;no-tty</code> it will use the system-wide query mechanism, which allows active users to respond via several agents, listed below. </p>
<p> The purpose of this tool is to query system-wide passwords &#8212; that is passwords not attached to a specific user account. Examples include: unlocking encrypted hard disks when they are plugged in or at boot, entering an SSL certificate passphrase for web and VPN servers. </p>
<p> Existing agents are: </p>
<dl>
<dt>
<dd> &bull; A boot-time password agent asking the user for passwords using <code><a href="/docs/linux/man/8-plymouth/">plymouth</a></code>(8),</dl>
<dl>
<dt>
<dd> &bull; A boot-time password agent querying the user directly on the console &#8212; <code><a href="/docs/linux/man/8-systemd-ask-password-console-service/">systemd-ask-password-console.service</a></code>(8),</dl>
<dl>
<dt>
<dd> &bull; An agent requesting password input via a <code><a href="/docs/linux/man/1-wall/">wall</a></code>(1) message &#8212; <code><a href="/docs/linux/man/8-systemd-ask-password-wall-service/">systemd-ask-password-wall.service</a></code>(8),</dl>
<dl>
<dt>
<dd> &bull; A TTY agent that is temporarily spawned during <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) invocations,</dl>
<dl>
<dt>
<dd> &bull; A command line agent which can be started temporarily to process queued password requests &#8212; <code>systemd-tty-ask-password-agent &#8211;query</code>.</dl>
<p> Answering system-wide password queries is a privileged operation, hence all the agents listed above (except for the last one), run as privileged system services. The last one also needs elevated privileges, so should be run through <code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8) or similar. </p>
<p> Additional password agents may be implemented according to the m[blue]<code>systemd Password Agent Specification</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> If a password is queried on a TTY, the user may press TAB to hide the asterisks normally shown for each character typed. Pressing Backspace as first key achieves the same effect.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;icon=</code></p>
<dl>
<dt>
<dd> Specify an icon name alongside the password query, which may be used in all agents supporting graphical display. The icon name should follow the m[blue]<code>XDG Icon Naming Specification</code>m[]<font SIZE="-2">[2]</font>.</dl>
<p> <code>&#8211;id=</code></p>
<dl>
<dt>
<dd> Specify an identifier for this password query. This identifier is freely choosable and allows recognition of queries by involved agents. It should include the subsystem doing the query and the specific object the query is done for. Example: &quot;&#8211;id=cryptsetup:/dev/sda5&quot;.</dl>
<p> <code>&#8211;keyname=</code></p>
<dl>
<dt>
<dd> Configure a kernel keyring key name to use as cache for the password. If set, then the tool will try to push any collected passwords into the kernel keyring of the root user, as a key of the specified name. If combined with <code>&#8211;accept-cached</code>, it will also try to retrieve such cached passwords from the key in the kernel keyring instead of querying the user right away. By using this option, the kernel keyring may be used as effective cache to avoid repeatedly asking users for passwords, if there are multiple objects that may be unlocked with the same password. The cached key will have a timeout of 2.5min set, after which it will be purged from the kernel keyring. Note that it is possible to cache multiple passwords under the same keyname, in which case they will be stored as <code>NUL</code>-separated list of passwords. Use <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1) to access the cached key via the kernel keyring directly. Example: &quot;&#8211;keyname=cryptsetup&quot;</dl>
<p> <code>&#8211;credential=</code></p>
<dl>
<dt>
<dd> Configure a credential to read the password from &#8211; if it exists. This may be used in conjunction with the <i>LoadCredential=</i> and <i>SetCredential=</i> settings in unit files. See <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details. If not specified, defaults to &quot;password&quot;. This option has no effect if no credentials directory is passed to the program (i.e. <i>$CREDENTIALS_DIRECTORY</i> is not set) or if the no credential of the specified name exists.</dl>
<p> <code>&#8211;timeout=</code></p>
<dl>
<dt>
<dd> Specify the query timeout in seconds. Defaults to 90s. A timeout of 0 waits indefinitely.</dl>
<p> <code>&#8211;echo=yes|no|masked</code></p>
<dl>
<dt>
<dd> Controls whether to echo user input. Takes a boolean or the special string &quot;masked&quot;, the default being the latter. If enabled the typed characters are echoed literally, which is useful for prompting for usernames and other non-protected data. If disabled the typed characters are not echoed in any form, the user will not get feedback on their input. If set to &quot;masked&quot;, an asterisk (&quot;*&quot;) is echoed for each character typed. In this mode, if the user hits the tabulator key (&quot;↹&quot;), echo is turned off. (Alternatively, if the user hits the backspace key (&quot;⌫&quot;) while no data has been entered otherwise, echo is turned off, too).</dl>
<p> <code>&#8211;echo</code>, <code>-e</code></p>
<dl>
<dt>
<dd> Equivalent to <code>&#8211;echo=yes</code>, see above.</dl>
<p> <code>&#8211;emoji=yes|no|auto</code></p>
<dl>
<dt>
<dd> Controls whether or not to prefix the query with a lock and key emoji (), if the TTY settings permit this. The default is &quot;auto&quot;, which defaults to &quot;yes&quot;, unless <code>&#8211;echo=yes</code> is given.</dl>
<p> <code>&#8211;no-tty</code></p>
<dl>
<dt>
<dd> Never ask for password on current TTY even if one is available. Always use agent system.</dl>
<p> <code>&#8211;accept-cached</code></p>
<dl>
<dt>
<dd> If passed, accept cached passwords, i.e. passwords previously entered.</dl>
<p> <code>&#8211;multiple</code></p>
<dl>
<dt>
<dd> When used in conjunction with <code>&#8211;accept-cached</code> accept multiple passwords. This will output one password per line.</dl>
<p> <code>&#8211;no-output</code></p>
<dl>
<dt>
<dd> Do not print passwords to standard output. This is useful if you want to store a password in kernel keyring with <code>&#8211;keyname=</code> but do not want it to show up on screen or in logs.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> By default, when writing the acquired password to standard output it is suffixed by a newline character. This may be turned off with the <code>-n</code> switch, similar to the switch of the same name of the <code><a href="/docs/linux/man/1-echo/">echo</a></code>(1) command.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-ask-password-console-service/">systemd-ask-password-console.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd-tty-ask-password-agent/">systemd-tty-ask-password-agent</a></code>(1), <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/8-plymouth/">plymouth</a></code>(8), <code><a href="/docs/linux/man/1-wall/">wall</a></code>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> systemd Password Agent Specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://systemd.io/PASSWORD_AGENTS/">https://systemd.io/PASSWORD_AGENTS/</a></dl>
<dt> 2.</p>
<dd> XDG Icon Naming Specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html">http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html</a></dl>
</dl>
<h2>Index</h2>
