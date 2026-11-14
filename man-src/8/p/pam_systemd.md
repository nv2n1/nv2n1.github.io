---
title: "pam_systemd(8)"
name: "pam_systemd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_systemd/"
description: "pam_systemd – Register user sessions in the systemd login manager"
---

<p>pam_systemd &#8211; Register user sessions in the systemd login manager</p>
<h2>Synopsis</h2>
<p>pam_systemd.so</p>
<h2>Description</h2>
<p><code>pam_systemd</code> registers user sessions with the systemd login manager <code><a href="/docs/linux/man/8-systemd-logind-service/">systemd-logind.service</a></code>(8), and hence the systemd control group hierarchy. </p>
<p> The module also applies various resource management and runtime parameters to the new session, as configured in the m[blue]<code>JSON User Records</code>m[]<font SIZE="-2">[1]</font> of the user, when one is defined. </p>
<p> On login, this module &#8212; in conjunction with systemd-logind.service &#8212; ensures the following: </p>
<dl>
<dd>1. If it does not exist yet, the user runtime directory /run/user/$UID is either created or mounted as new &quot;tmpfs&quot; file system with quota applied, and its ownership changed to the user that is logging in.</dl>
<dl>
<dd>2. The <i>$XDG_SESSION_ID</i> environment variable is initialized. If auditing is available and <code>pam_loginuid.so</code> was run before this module (which is highly recommended), the variable is initialized from the auditing session id (/proc/self/sessionid). Otherwise, an independent session counter is used.</dl>
<dl>
<dd>3. A new systemd scope unit is created for the session. If this is the first concurrent session of the user, an implicit per-user slice unit below user.slice is automatically created and the scope placed into it. An instance of the system service user [at] .service, which runs the systemd user manager instance, is started.</dl>
<dl>
<dd>4. The &quot;$TZ&quot;, &quot;$EMAIL&quot; and &quot;$LANG&quot; environment variables are configured for the user, based on the respective data from the user&#8217;s JSON record (if it is defined). Moreover, any environment variables explicitly configured in the user record are imported, and the umask, nice level, and resource limits initialized.</dl>
<p> On logout, this module ensures the following: </p>
<dl>
<dd>1. If enabled in <code><a href="/docs/linux/man/5-logind-conf/">logind.conf</a></code>(5) (<i>KillUserProcesses=</i>), all processes of the session are terminated. If the last concurrent session of a user ends, the user&#8217;s systemd instance will be terminated too, and so will the user&#8217;s slice unit.</dl>
<dl>
<dd>2. If the last concurrent session of a user ends, the user runtime directory /run/user/$UID and all its contents are removed, too.</dl>
<p> If the system was not booted up with systemd as init system, this module does nothing and immediately returns <code>PAM_SUCCESS</code>.</p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <i>class=</i></p>
<dl>
<dd>Takes a string argument which sets the session class. The <i>XDG_SESSION_CLASS</i> environment variable (see below) takes precedence. One of &quot;user&quot;, &quot;greeter&quot;, &quot;lock-screen&quot; or &quot;background&quot;. See <code><a href="/docs/linux/man/3-sd_session_get_class/">sd_session_get_class</a></code>(3) for details about the session class.</dl>
<p> <i>type=</i></p>
<dl>
<dd>Takes a string argument which sets the session type. The <i>XDG_SESSION_TYPE</i> environment variable (see below) takes precedence. One of &quot;unspecified&quot;, &quot;tty&quot;, &quot;x11&quot;, &quot;wayland&quot; or &quot;mir&quot;. See <code><a href="/docs/linux/man/3-sd_session_get_type/">sd_session_get_type</a></code>(3) for details about the session type.</dl>
<p> <i>desktop=</i></p>
<dl>
<dd>Takes a single, short identifier string for the desktop environment. The <i>XDG_SESSION_DESKTOP</i> environment variable (see below) takes precedence. This may be used to indicate the session desktop used, where this applies and if this information is available. For example: &quot;GNOME&quot;, or &quot;KDE&quot;. It is recommended to use the same identifiers and capitalization as for <i>$XDG_CURRENT_DESKTOP</i>, as defined by the m[blue]<code>Desktop Entry Specification</code>m[]<font SIZE="-2">[2]</font>. (However, note that the option only takes a single item, and not a colon-separated list like <i>$XDG_CURRENT_DESKTOP</i>.) See <code><a href="/docs/linux/man/3-sd_session_get_desktop/">sd_session_get_desktop</a></code>(3) for further details.</dl>
<p> <i>debug</i>[=]</p>
<dl>
<dd>Takes an optional boolean argument. If yes or without the argument, the module will log debugging information as it operates.</dl>
<h2>Module Types Provided</h2>
<p>Only <code>session</code> is provided.</p>
<h2>Environment</h2>
<p>The following environment variables are initialized by the module and available to the processes of the user&#8217;s session: </p>
<p> <i>$XDG_SESSION_ID</i></p>
<dl>
<dd>A short session identifier, suitable to be used in filenames. The string itself should be considered opaque, although often it is just the audit session ID as reported by /proc/self/sessionid. Each ID will be assigned only once during machine uptime. It may hence be used to uniquely label files or other resources of this session. Combine this ID with the boot identifier, as returned by <code><a href="/docs/linux/man/3-sd_id128_get_boot/">sd_id128_get_boot</a></code>(3), for a globally unique identifier.</dl>
<p> <i>$XDG_RUNTIME_DIR</i></p>
<dl>
<dd>Path to a user-private user-writable directory that is bound to the user login time on the machine. It is automatically created the first time a user logs in and removed on the user&#8217;s final logout. If a user logs in twice at the same time, both sessions will see the same <i>$XDG_RUNTIME_DIR</i> and the same contents. If a user logs in once, then logs out again, and logs in again, the directory contents will have been lost in between, but applications should not rely on this behavior and must be able to deal with stale files. To store session-private data in this directory, the user should include the value of <i>$XDG_SESSION_ID</i> in the filename. This directory shall be used for runtime file system objects such as <code>AF_UNIX</code> sockets, FIFOs, PID files and similar. It is guaranteed that this directory is local and offers the greatest possible file system feature set the operating system provides. For further details, see the m[blue]<code>XDG Base Directory Specification</code>m[]<font SIZE="-2">[3]</font>. <i>$XDG_RUNTIME_DIR</i> is not set if the current user is not the original user of the session.</dl>
<p> <i>$TZ</i>, <i>$EMAIL</i>, <i>$LANG</i></p>
<dl>
<dd>If a JSON user record is known for the user logging in these variables are initialized from the respective data in the record.</dl>
<p> The following environment variables are read by the module and may be used by the PAM service to pass metadata to the module. If these variables are not set when the PAM module is invoked but can be determined otherwise they are set by the module, so that these variables are initialized for the session and applications if known at all. </p>
<p> <i>$XDG_SESSION_TYPE</i></p>
<dl>
<dd>The session type. This may be used instead of <i>type=</i> on the module parameter line, and is usually preferred.</dl>
<p> <i>$XDG_SESSION_CLASS</i></p>
<dl>
<dd>The session class. This may be used instead of <i>class=</i> on the module parameter line, and is usually preferred.</dl>
<p> <i>$XDG_SESSION_DESKTOP</i></p>
<dl>
<dd>The desktop identifier. This may be used instead of <i>desktop=</i> on the module parameter line, and is usually preferred.</dl>
<p> <i>$XDG_SEAT</i></p>
<dl>
<dd>The seat name the session shall be registered for, if any.</dl>
<p> <i>$XDG_VTNR</i></p>
<dl>
<dd>The VT number the session shall be registered for, if any. (Only applies to seats with a VT available, such as &quot;seat0&quot;)</dl>
<p> If not set, <code>pam_systemd</code> will initialize <i>$XDG_SEAT</i> and <i>$XDG_VTNR</i> based on the <i>$DISPLAY</i> variable (if the latter is set).</p>
<h2>Session Limits</h2>
<p>PAM modules earlier in the stack, that is those that come before <code>pam_systemd.so</code>, can set session scope limits using the PAM context objects. The data for these objects is provided as <code>NUL</code>-terminated C strings and maps directly to the respective unit resource control directives. Note that these limits apply to individual sessions of the user, they do not apply to all user processes as a combined whole. In particular, the per-user <code>user [at] .service</code> unit instance, which runs the <code>systemd &#8211;user</code> manager process and its children, and is tracked outside of any session, being shared by all the user&#8217;s sessions, is not covered by these limits. </p>
<p> See <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5) for more information about the resources. Also, see <code><a href="/docs/linux/man/3-pam_set_data/">pam_set_data</a></code>(3) for additional information about how to set the context objects. </p>
<p> <i>systemd.memory_max=</i></p>
<dl>
<dd>Sets unit <i>MemoryMax=</i>.</dl>
<p> <i>systemd.tasks_max=</i></p>
<dl>
<dd>Sets unit <i>TasksMax=</i>.</dl>
<p> <i>systemd.cpu_weight=</i></p>
<dl>
<dd>Sets unit <i>CPUWeight=</i>.</dl>
<p> <i>systemd.io_weight=</i></p>
<dl>
<dd>Sets unit <i>IOWeight=</i>.</dl>
<p> <i>systemd.runtime_max_sec=</i></p>
<dl>
<dd>Sets unit <i>RuntimeMaxSec=</i>.</dl>
<p> Example data as can be provided from an another PAM module: </p>
<dl>
<dd>
<pre>pam_set_data(handle, &quot;systemd.memory_max&quot;, (void *)&quot;200M&quot;, cleanup);
pam_set_data(handle, &quot;systemd.tasks_max&quot;, (void *)&quot;50&quot;, cleanup);
pam_set_data(handle, &quot;systemd.cpu_weight&quot;, (void *)&quot;100&quot;, cleanup);
pam_set_data(handle, &quot;systemd.io_weight&quot;, (void *)&quot;340&quot;, cleanup);
pam_set_data(handle, &quot;systemd.runtime_max_sec&quot;, (void *)&quot;3600&quot;, cleanup);</pre>
</dl>
<h2>Example</h2>
<p>Here&#8217;s an example PAM configuration fragment that allows users sessions to be managed by systemd-logind.service: </p>
<dl>
<dd>
<pre>#%PAM-1.0
auth sufficient pam_unix.so
-auth sufficient pam_systemd_home.so
auth required pam_deny.so
account required pam_nologin.so
-account sufficient pam_systemd_home.so
account sufficient pam_unix.so
account required pam_permit.so
-password sufficient pam_systemd_home.so
password sufficient pam_unix.so sha512 shadow try_first_pass use_authtok
password required pam_deny.so
-session optional pam_keyinit.so revoke
-session optional pam_loginuid.so
-session optional pam_systemd_home.so
<code>-session optional pam_systemd.so</code>
session required pam_unix.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-logind-service/">systemd-logind.service</a></code>(8), <code><a href="/docs/linux/man/5-logind-conf/">logind.conf</a></code>(5), <code><a href="/docs/linux/man/1-loginctl/">loginctl</a></code>(1), <code><a href="/docs/linux/man/8-pam_systemd_home/">pam_systemd_home</a></code>(8), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8), <code><a href="/docs/linux/man/8-pam_loginuid/">pam_loginuid</a></code>(8), <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5), <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>JSON User Records</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/USER_RECORD">https://systemd.io/USER_RECORD</a></dl>
<dt> 2.</p>
<dd>Desktop Entry Specification</p>
<dl>
<dd><a rel="nofollow" href="http://standards.freedesktop.org/desktop-entry-spec/latest/">http://standards.freedesktop.org/desktop-entry-spec/latest/</a></dl>
<dt> 3.</p>
<dd>XDG Base Directory Specification</p>
<dl>
<dd><a rel="nofollow" href="http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html">http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html</a></dl>
