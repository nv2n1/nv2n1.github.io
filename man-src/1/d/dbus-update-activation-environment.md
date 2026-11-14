---
title: "dbus-update-activation-environment(1)"
name: "dbus-update-activation-environment"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbus-update-activation-environment/"
description: "dbus-update-activation-environment – update environment used for D-Bus session services"
---

<h2 class="name">NAME</h2>
<p> dbus-update-activation-environment &#8211; update environment used for D-Bus session services </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dbus-update-activation-environment</code> [&#8211;systemd] [&#8211;verbose] &#8211;all | <i>VAR</i>&#8230; | <i>VAR</i>=<i>VAL</i>&#8230;</dl>
<h2>DESCRIPTION</h2>
<p> <code>dbus-update-activation-environment</code></p>
<dd>updates the list of environment variables used by <code>dbus-daemon &#8211;session</code> when it activates session services without using <code>systemd</code>. </p>
<p> With the <code>&#8211;systemd</code> option, if an instance of <code>systemd &#8211;user</code> is available on D-Bus, it also updates the list of environment variables used by <code>systemd &#8211;user</code> when it activates user services, including D-Bus session services for which <code>dbus-daemon</code> has been configured to delegate activation to <code>systemd</code>. This is very similar to the <code>import-environment</code> command provided by <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1)). </p>
<p> Variables that are special to <code>dbus-daemon</code> or <code>systemd</code> may be set, but their values will be overridden when a service is started. For instance, it is not useful to add <code>DBUS_SESSION_BUS_ADDRESS</code> to <code>dbus-daemon</code>&#8216;s activation environment, although it might still be useful to add it to <code>systemd</code>&#8216;s activation environment.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Set all environment variables present in the environment used by <code>dbus-update-activation-environment</code>.</dl>
<p> <code>&#8211;systemd</code></p>
<dl>
<dt>
<dd> Set environment variables for systemd user services as well as for traditional D-Bus session services.</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Output messages to standard error explaining what dbus-update-activation-environment is doing.</dl>
<p> <i>VAR</i></p>
<dl>
<dt>
<dd> If <i>VAR</i> is present in the environment of <code>dbus-update-activation-environment</code>, set it to the same value for D-Bus services. Its value must be UTF-8 (if not, it is skipped with a warning). If <i>VAR</i> is not present in the environment, this argument is silently ignored.</dl>
<p> <i>VAR</i>=<i>VAL</i></p>
<dl>
<dt>
<dd> Set <i>VAR</i> to <i>VAL</i>, which must be UTF-8.</dl>
<h2>EXAMPLES</h2>
<p> <code>dbus-update-activation-environment</code> is primarily designed to be used in Linux distributions&#8217; X11 session startup scripts, in conjunction with the &quot;user bus&quot; design. </p>
<p> To propagate <code>DISPLAY</code> and <code>XAUTHORITY</code> to <code>dbus-daemon</code> and, if present, <code>systemd</code>, and propagate <code>DBUS_SESSION_BUS_ADDRESS</code> to <code>systemd</code>: </p>
<dl>
<dt>
<dd>
<pre>
        dbus-update-activation-environment --systemd \
            DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY
      
</pre>
</dl>
<p> To propagate all environment variables except <code>XDG_SEAT</code>, <code>XDG_SESSION_ID</code> and <code>XDG_VTNR</code> to <code>dbus-daemon</code> (and, if present, <code>systemd</code>) for compatibility with legacy X11 session startup scripts: </p>
<dl>
<dt>
<dd>
<pre>
        # in a subshell so the variables remain set in the
        # parent script
        (
          unset XDG_SEAT
          unset XDG_SESSION_ID
          unset XDG_VTNR
          dbus-update-activation-environment --systemd --all
        )
      
</pre>
</dl>
<h2>EXIT STATUS</h2>
<p> <code>dbus-update-activation-environment</code> exits with status 0 on success, EX_USAGE (64) on invalid command-line options, EX_OSERR (71) if unable to connect to the session bus, or EX_UNAVAILABLE (69) if unable to set the environment variables. Other nonzero exit codes might be added in future versions.</p>
<h2>ENVIRONMENT</h2>
<p> <code>DBUS_SESSION_BUS_ADDRESS</code>, <code>XDG_RUNTIME_DIR</code> and/or <code>DISPLAY</code> are used to find the address of the session bus.</p>
<h2>LIMITATIONS</h2>
<p> <code>dbus-daemon</code> does not provide a way to unset environment variables after they have been set (although <code>systemd</code> does), so <code>dbus-update-activation-environment</code> does not offer this functionality either. </p>
<p> POSIX does not specify the encoding of non-ASCII environment variable names or values and allows them to contain any non-zero byte, but neither <code>dbus-daemon</code> nor <code>systemd</code> supports environment variables with non-UTF-8 names or values. Accordingly, <code>dbus-update-activation-environment</code> assumes that any name or value that appears to be valid UTF-8 is intended to be UTF-8, and ignores other names or values with a warning.</p>
<h2>BUGS</h2>
<p> Please send bug reports to the D-Bus bug tracker or mailing list. See m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/dbus/">http://www.freedesktop.org/software/dbus/</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), the <code>import-environment</code> command of <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2015 Collabora Ltd. </p>
<p> This man page is distributed under the same terms as dbus-update-activation-environment (MIT/X11). There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
