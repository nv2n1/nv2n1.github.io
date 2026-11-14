---
title: "x-session-manager(1)"
name: "x-session-manager"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x-session-manager/"
description: "gnome-session – Start the GNOME desktop environment"
---

<h2 class="name">NAME</h2>
<p> gnome-session &#8211; Start the GNOME desktop environment </p>
<h2>SYNOPSIS</h2>
<p> <code>gnome-session [-a|&#8211;autostart=DIR] [&#8211;session=SESSION] [&#8211;failsafe|-f] [&#8211;debug] [&#8211;whale]</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>gnome-session</i> program starts up the GNOME desktop environment. This command is typically executed by your login manager (either gdm, xdm, or from your X startup scripts). It will load either your saved session, or it will provide a default session for the user as defined by the system administrator (or the default GNOME installation on your system). Note that <i>gnome-session</i> is a wrapper script for <i>gnome-session-binary</i>. </p>
<p> The default session is defined in <code>gnome.session</code>, a .desktop-like file that is looked for in <code>$XDG_CONFIG_HOME/gnome-session/sessions</code>, <code>$XDG_CONFIG_DIRS/gnome-session/sessions</code> and <code>$XDG_DATA_DIRS/gnome-session/sessions</code>. </p>
<p> When saving a session, <i>gnome-session</i> saves the currently running applications in the <code>$XDG_CONFIG_HOME/gnome-session/saved-session</code> directory. Saving sessions is only supported with the legacy non-systemd startup method. </p>
<p> <i>gnome-session</i> is an X11R6 session manager. It can manage GNOME applications as well as any X11R6 SM compliant application.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>&#8211;autostart=DIR</i></p>
<dd> The directory <code>DIR</code> to be searched for autostart .desktop files. This option can be used multiple times. When this option is present, then default autostart directories will not be searched.</p>
<dt><i>&#8211;session=SESSION</i></p>
<dd> Use the applications defined in <code>SESSION.session</code>. If not specified, <code>gnome.session</code> will be used.</p>
<dt><i>&#8211;builtin</i></p>
<dd> Use the legacy non-systemd method of managing the user session. This is the opposite of the <i>&#8211;systemd</i> option.</p>
<dt><i>&#8211;systemd</i></p>
<dd> Use the systemd method of managing the user session. This is the opposite of the <i>&#8211;builtin</i> option.</p>
<dt><i>&#8211;failsafe</i></p>
<dd> Run in fail-safe mode. User-specified applications will not be started.</p>
<dt><i>&#8211;debug</i></p>
<dd> Enable debugging code.</p>
<dt><i>&#8211;whale</i></p>
<dd> Show the fail whale in a dialog for debugging it.</dl>
<h2>SESSION DEFINITION</h2>
<p> Sessions are defined in <code>.session</code> files, that are using a .desktop-like format, with the following keys in the <code>GNOME Session</code> group:</p>
<dl>
<dt><i>Name</i></p>
<dd> Name of the session. This can be localized.</p>
<dt><i>RequiredComponents</i></p>
<dd> List of component identifiers (desktop files) that are required by the session. The required components will always run in the session.</dl>
<p> Here is an example of a session definition: </p>
<pre><code>
[GNOME Session] Name = GNOME
    RequiredComponents = gnome - shell;
gnome - settings - daemon;
</code></pre>
<p> In <code>systemd</code> managed sessions the RequiredComponents may be provided by systemd units instead. In this case the corresponding <code>.desktop</code> file needs to contain <code>X-GNOME-HiddenUnderSystemd=true</code>. <i>gnome-session</i> will ignore these components and rely on <i>systemd</i> to manage them appropriately, see the <i>systemd</i> for more information on how this works. </p>
<p> The <code>.session</code> files are looked for in <code>$XDG_CONFIG_HOME/gnome-session/sessions</code>, <code>$XDG_CONFIG_DIRS/gnome-session/sessions</code> and <code>$XDG_DATA_DIRS/gnome-session/sessions</code>.</p>
<h2>systemd</h2>
<p> <i>gnome-session</i> can pass much of the session management over to systemd (see the <i>&#8211;systemd</i> option which may be the default since 3.34). In this case, startup components that have <code>X-GNOME-HiddenUnderSystemd=true</code> set in their <code>.desktop</code> file will be ignored by <i>gnome-session</i>. It instead relies on the fact that these components are managed by systemd. </p>
<p> As of GNOME 3.34 the systemd support is new and the customizing the configuration is not yet easily possible. With GNOME 3.34 it may be best to use <i>&#8211;builtin</i> if session customizations are required. This is due to the way that GNOME currently defines the components that will be started on each session type. </p>
<p> <code>systemd</code> provides the two special targets <code>graphical-session.target</code> and <code>graphical-session-pre.target</code> which are fully functional and should be used. <i>gnome-session</i> provides the following main targets:</p>
<dl>
<dt><i>gnome-session.target</i></p>
<dd> Generic unit that will be active throughout the session. Similar to <code>graphical-session.target</code>.</p>
<dt><i>gnome-session-pre.target</i></p>
<dd> Used for tasks that need to be done before session startup. Similar to <code>graphical-session-pre.target</code>.</p>
<dt><i>gnome-session-x11 [at] SESSION.target gnome-session-wayland [at] SESSION.target</i></p>
<dd> Main unit started for X11/wayland based session. <code>SESSION</code> is set according to the session that is passed in <i>&#8211;session</i>.</p>
<dt><i>gnome-session-x11.target gnome-session-wayland.target</i></p>
<dd> Convenience units without the session embedded into the target.</p>
<dt><i>gnome-session [at] SESSION.target</i></p>
<dd> Convenience unit with just the <code>SESSION</code> information embedded.</p>
<dt><i>gnome-session-x11-services.target</i></p>
<dd> Special unit started when X11 services are needed. This will be used from GNOME 3.36 onwards. Programs will need to use the special <code>GNOME_SETUP_DISPLAY</code> environment variable instead of <i>DISPLAY</i>.</dl>
<p> Note that care must be taken to set appropriate <code>After=</code> rules. It is also strongly recommended to always do this in combination with <code>BindsTo=</code> or <code>PartOf=</code> on one of the core targets (e.g. <code>graphical-session.target</code>). </p>
<p> Units are required to set <code>CollectMode=inactive-or-failed</code>. In addition, it is strongly recommended to set <code>TimeoutStopSec=5</code> so that logout will not be delayed indefinitely in case the process does not stop properly.</p>
<h2>ENVIRONMENT</h2>
<p> <i>gnome-session</i> sets several environment variables for the use of its child processes: </p>
<p> <code>SESSION_MANAGER</code></p>
<dl>
<dt>
<dd> This variable is used by session-manager aware clients to contact gnome-session.</dl>
<p> <code>DISPLAY</code></p>
<dl>
<dt>
<dd> This variable is set to the X display being used by <i>gnome-session</i>. Note that if the <i>&#8211;display</i> option is used this might be different from the setting of the environment variable when gnome-session is invoked.</dl>
<p> Behavior of <i>gnome-session</i> ifself can be modified via the following environment variable: </p>
<p> <code>GNOME_SESSION_AUTOSTART_DIR</code></p>
<dl>
<dt>
<dd> This variable specifies a list of directories to the searched for autostart files. This variable overrides all directories specified via the <i>&#8211;autostart</i> option, as well as all default autostart directories.</dl>
<h2>FILES</h2>
<p> <code>$XDG_CONFIG_HOME/autostart</code> <code>$XDG_CONFIG_DIRS/autostart</code> <code>/usr/share/gnome/autostart</code></p>
<dl>
<dt>
<dd> Applications defined via .desktop files in those directories will be started on login. <i><a href="/docs/linux/man/1-gnome-session-properties/">gnome-session-properties</a>(1)</i> can be used to easily configure them.</dl>
<p> <code>$XDG_CONFIG_HOME/gnome-session/sessions</code> <code>$XDG_CONFIG_DIRS/gnome-session/sessions</code> <code>$XDG_DATA_DIRS/gnome-session/sessions</code></p>
<dl>
<dt>
<dd> These directories contain the <code>.session</code> files that can be used with the <i>&#8211;session</i> option.</dl>
<p> <code>$XDG_CONFIG_HOME/gnome-session/saved-session</code></p>
<dl>
<dt>
<dd> This directory contains the list of applications of the saved session.</dl>
<h2>BUGS</h2>
<p> If you find bugs in the <i>gnome-session</i> program, please report these on <a rel="nofollow" href="https://gitlab.gnome.org/GNOME/gnome-session/issues.">https://gitlab.gnome.org/GNOME/gnome-session/issues.</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gnome-session-properties/">gnome-session-properties</a>(1)</code> <code><a href="/docs/linux/man/1-gnome-session-quit/">gnome-session-quit</a>(1)</code> </p>
<h2>Index</h2>
