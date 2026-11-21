---
title: "flatpak-ps(1)"
name: "flatpak-ps"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-ps/"
description: "flatpak-ps – Enumerate running instances"
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak ps</code> [OPTION&#8230;]</dt></dl>
<h2>DESCRIPTION</h2>
<dd>Lists useful information about running Flatpak instances. </dd>
<p> To see full details of a running instance, you can open the file /run/user/$UID/.flatpak/$INSTANCE/info, where <i>$INSTANCE</i> is the instance ID reported by flatpak ps.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show help options and exit.</dd></dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
</dt><dd> Print debug information during command processing.</dd></dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
</dt><dd> Print OSTree debug information during command processing.</dd></dl>
<p> <code>&#8211;columns=FIELD,&#8230;</code></p>
<dl>
<dt>
</dt><dd> Specify what information to show about each instance. You can list multiple fields, or use this option multiple times. </dd>
<p> Append :s[tart], :m[iddle], :e[nd] or :f[ull] to column names to change ellipsization.</dl>
<h2>FIELDS</h2>
<p> The following fields are understood by the <code>&#8211;columns</code> option: </p>
<p> instance</p>
<dl>
<dt>
</dt><dd> Show the instance ID</dd></dl>
<p> application</p>
<dl>
<dt>
</dt><dd> Show the application ID</dd></dl>
<p> arch</p>
<dl>
<dt>
</dt><dd> Show the architecture</dd></dl>
<p> branch</p>
<dl>
<dt>
</dt><dd> Show the application branch</dd></dl>
<p> commit</p>
<dl>
<dt>
</dt><dd> Show the application commit</dd></dl>
<p> runtime</p>
<dl>
<dt>
</dt><dd> Show the runtime ID</dd></dl>
<p> runtime-branch</p>
<dl>
<dt>
</dt><dd> Show the runtime branch</dd></dl>
<p> runtime-commit</p>
<dl>
<dt>
</dt><dd> Show the runtime commit</dd></dl>
<p> pid</p>
<dl>
<dt>
</dt><dd> Show the PID of the wrapper process</dd></dl>
<p> child-pid</p>
<dl>
<dt>
</dt><dd> Show the PID of the sandbox process</dd></dl>
<p> active</p>
<dl>
<dt>
</dt><dd> Show whether the app is active (i.e. has an active window)</dd></dl>
<p> background</p>
<dl>
<dt>
</dt><dd> Show whether the app is in the background (with no open windows)</dd></dl>
<p> all</p>
<dl>
<dt>
</dt><dd> Show all columns</dd></dl>
<p> help</p>
<dl>
<dt>
</dt><dd> Show the list of available columns</dd></dl>
<p> Note that field names can be abbreviated to a unique prefix.</p>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak ps &#8211;columns=application,pid,runtime,runtime-branch</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-run/">flatpak-run</a></code>(1) </p>
