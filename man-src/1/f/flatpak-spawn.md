---

title: "flatpak-spawn(1)"
name: "flatpak-spawn"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-spawn/"
description: "flatpak-spawn – Run commands in a sandbox"
---

<dl>
<dt> <code>flatpak-spawn</code> [OPTION&#8230;] COMMAND [ARGUMENT&#8230;]</dt></dl>
<dd>Unlike other flatpak commands, <code>flatpak-spawn</code> is available to applications inside the sandbox. It runs COMMAND outside the sandbox, either in another sandbox, or on the host. </dd>
<p> <code>flatpak-spawn</code> uses the Flatpak portal to create a copy the sandbox it was called from, optionally using tighter permissions and the latest version of the app and runtime.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show help options and exit.</dd></dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
</dt><dd> Print debug information</dd></dl>
<p> <code>&#8211;forward-fd=FD</code></p>
<dl>
<dt>
</dt><dd> Forward a file descriptor</dd></dl>
<p> <code>&#8211;clear-env</code></p>
<dl>
<dt>
</dt><dd> Run with a clean environment</dd></dl>
<p> <code>&#8211;watch-bus</code></p>
<dl>
<dt>
</dt><dd> Make the spawned command exit if we do</dd></dl>
<p> <code>&#8211;env=VAR=VALUE</code></p>
<dl>
<dt>
</dt><dd> Set an environment variable</dd></dl>
<p> <code>&#8211;latest-version</code></p>
<dl>
<dt>
</dt><dd> Use the latest version of the refs that are used to set up the sandbox</dd></dl>
<p> <code>&#8211;no-network</code></p>
<dl>
<dt>
</dt><dd> Run without network access</dd></dl>
<p> <code>&#8211;sandbox</code></p>
<dl>
<dt>
</dt><dd> Run fully sandboxed. </dd>
<p> See the <code>&#8211;sandbox-expose</code> and <code>&#8211;sandbox-expose-ro</code> options for selective file access.</dl>
<p> <code>&#8211;sandbox-expose=NAME</code></p>
<dl>
<dt>
</dt><dd> Expose read-write access to a file in the sandbox. </dd>
<p> Note that absolute paths or subdirectories are not allowed. The files must be in the sandbox subdirectory of the instance directory (i.e. ~/.var/app/$APP_ID/sandbox). </p>
<p> This option is useful in combination with <code>&#8211;sandbox</code> (otherwise the instance directory is accessible anyway).</dl>
<p> <code>&#8211;sandbox-expose-ro=NAME</code></p>
<dl>
<dt>
</dt><dd> Expose readonly access to a file in the sandbox. </dd>
<p> Note that absolute paths or subdirectories are not allowed. The files must be in the sandbox subdirectory of the instance directory (i.e. ~/.var/app/$APP_ID/sandbox). </p>
<p> This option is useful in combination with <code>&#8211;sandbox</code> (otherwise the instance directory is accessible anyway).</dl>
<p> <code>&#8211;host</code></p>
<dl>
<dt>
</dt><dd> Run the command unsandboxed on the host. This requires access to the org.freedesktop.Flatpak D-Bus interface</dd></dl>
<p> <code>&#8211;directory=DIR</code></p>
<dl>
<dt>
</dt><dd> The working directory in which to run the command. </dd>
<p> Note that the given directory must exist in the sandbox or, when used in conjunction with <code>&#8211;host</code>, on the host.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak-spawn ls /var/run</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1) </p>
