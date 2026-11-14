---
title: "modemmanager(8)"
name: "modemmanager"
section: "8"
letter: "m"
url: "/docs/linux/man/8-modemmanager/"
description: "ModemManager – mobile broadband modem management daemon"
---

<p>ModemManager &#8211; mobile broadband modem management daemon</p>
<h2>Synopsis</h2>
<p><code>ModemManager</code> [<i>OPTION</i>&#8230;] </p>
<h2>Description</h2>
<p>ModemManager provides a unified high level API for communicating with mobile broadband modems, regardless of the protocol used to communicate with the actual device (Generic AT, vendor-specific AT, QCDM, QMI, MBIM&#8230;). ModemManager is a DBus-based system daemon and is not meant to be used directly from the command line. </p>
<h2>Application Options</h2>
<dl>
<dt><code>&#8211;filter-policy=&lt;policy&gt;</code></p>
<dd>Specify which ports are probed and how:</p>
<dl>
<dd>
<dl>
<dt><code>&#8216;ALLOWLIST-ONLY&#8217;</code></p>
<dd>Only devices or ports explicitly allowlisted with the &#8216;ID_MM_DEVICE_PROCESS&#8217; udev tag are probed.</p>
<dt><code>&#8216;STRICT&#8217;</code></p>
<dd>Only the TTY ports that are heuristically determined to be very likely to be modem ports are probed. Nay end up ignoring some devices.</dl>
</dl>
<dt><code>&#8211;no-auto-scan</code></p>
<dd>Fully disable udev-based auto-scan looking for devices.</p>
<dt><code>&#8211;initial-kernel-events=&lt;filename&gt;</code></p>
<dd>Specify location of the file where the list of initial kernel events is available. The ModemManager daemon will process this file on startup.</p>
<dt><code>&#8211;debug</code></p>
<dd>Runs ModemManager with &quot;DEBUG&quot; log level and without daemonizing. This is useful for debugging, as it directs log output to the controlling terminal in addition to syslog.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print the ModemManager software version and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Show application options. </p>
</dl>
<h2>Logging Options</h2>
<dl>
<dt><code>&#8211;log-level=&lt;level&gt;</code></p>
<dd>Sets how much information ModemManager sends to the log destination (usually syslog&#8217;s &quot;daemon&quot; facility). By default, only informational, warning, and error messages are logged. Given level must be one of &quot;ERR&quot;, &quot;WARN&quot;, &quot;INFO&quot; or &quot;DEBUG&quot;.</p>
<dt><code>&#8211;log-file=&lt;filename&gt;</code></p>
<dd>Specify location of the file where ModemManager will dump its log messages, instead of syslog.</p>
<dt><code>&#8211;log-journal</code></p>
<dd>Output log message to the systemd journal.</p>
<dt><code>&#8211;log-timestamps</code></p>
<dd>Include absolute timestamps in the log output.</p>
<dt><code>&#8211;log-relative-timestamps</code></p>
<dd>Include timestamps, relative to the start time of the daemon, in the log output. </p>
</dl>
<h2>Test Options</h2>
<dl>
<dt><code>&#8211;test-session</code></p>
<dd>Run the ModemManager daemon in the Session bus instead of the System bus.</p>
<dt><code>&#8211;test-enable</code></p>
<dd>Enable the Test DBus interface in the daemon.</p>
<dt><code>&#8211;test-plugin-dir=[PATH]</code></p>
<dd>Specify an alternate directory where the daemon should look for vendor plugins. </p>
</dl>
<h2>Author</h2>
<p>Aleksander Morgado &lt;aleksander [at] aleksander.es&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mmcli/">mmcli</a></code>(1), <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8) </p>
