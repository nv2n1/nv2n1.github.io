---
title: "cinnamon-session(1)"
name: "cinnamon-session"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cinnamon-session/"
description: "cinnamon-session – Start the GNOME desktop environment"
---

<h2>NAME</h2>
<p> cinnamon-session &#8211; Start the GNOME desktop environment</p>
<h2>SYNOPSIS</h2>
<p> <code>cinnamon-session [-a|&#8211;autostart=DIR] [&#8211;session=SESSION] [&#8211;failsafe|-f] [&#8211;debug] [&#8211;whale]</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>cinnamon-session</i> program starts up the GNOME desktop environment. This command is typically executed by your login manager (either mdm, xdm, or from your X startup scripts). It will load either your saved session, or it will provide a default session for the user as defined by the system administrator (or the default GNOME installation on your system). </p>
<p> The default session is defined in <code>gnome.session</code>, a .desktop-like file that is looked for in <code>$XDG_CONFIG_HOME/cinnamon-session/sessions</code>, <code>$XDG_CONFIG_DIRS/cinnamon-session/sessions</code> and <code>$XDG_DATA_DIRS/cinnamon-session/sessions</code>. </p>
<p> When saving a session, <i>cinnamon-session</i> saves the currently running applications in the <code>$XDG_CONFIG_HOME/cinnamon-session/saved-session</code> directory. </p>
<p> <i>cinnamon-session</i> is an X11R6 session manager. It can manage GNOME applications as well as any X11R6 SM compliant application.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>&#8211;autostart=DIR</i></p>
<dd> Start all applications defined in <i>DIR</i>, instead of starting the applications defined in <code>gnome.session</code>, or via the <i>&#8211;session</i> option. Multiple <i>&#8211;autostart</i> options can be passed.</p>
<dt><i>&#8211;session=SESSION</i></p>
<dd> Use the applications defined in <code>SESSION.session</code>. If not specified, <code>gnome.session</code> will be used.</p>
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
<dd> List of component identifiers (desktop files) that are required by the session. The required components will always run in the session.</p>
<dt><i>RequiredProviders</i></p>
<dd> List of task providers that are required by the session. A default provider for each task has to be defined with a <i>DefaultProvider-TASK</i> key; the provider can be overridden by required components, the saved session or autostart applications. The task providers will always run in the session.</p>
<dt><i>DefaultProvider-TASK</i></p>
<dd> Identifier (desktop file) of the default provider for <code>TASK</code>. If no provider for <code>TASK</code> is found in the required components, the saved session and in the autostart applications, the default provider will be started.</dl>
<p> Here is an example of a session definition: </p>
<pre><code>
[GNOME Session] Name = GNOME fallback
    RequiredComponents = gnome - panel;
metacity;
gnome - settings - daemon;
RequiredProviders = notifications;
DefaultProvider - notifications = notification - daemon
</code></pre>
<p> The <code>.session</code> files are looked for in <code>$XDG_CONFIG_HOME/cinnamon-session/sessions</code>, <code>$XDG_CONFIG_DIRS/cinnamon-session/sessions</code> and <code>$XDG_DATA_DIRS/cinnamon-session/sessions</code>.</p>
<h2>ENVIRONMENT</h2>
<p> <i>cinnamon-session</i> sets several environment variables for the use of its child processes: </p>
<p> <code>SESSION_MANAGER</code></p>
<dl>
<dt>
<dd> This variable is used by session-manager aware clients to contact cinnamon-session.</dl>
<p> <code>DISPLAY</code></p>
<dl>
<dt>
<dd> This variable is set to the X display being used by <i>cinnamon-session</i>. Note that if the <i>&#8211;display</i> option is used this might be different from the setting of the environment variable when cinnamon-session is invoked.</dl>
<h2>FILES</h2>
<p> <code>$XDG_CONFIG_HOME/config/autostart</code> <code>$XDG_CONFIG_DIRS/config/autostart</code> <code>/usr/share/gnome/autostart</code></p>
<dl>
<dt>
<dd> The applications defined in those directories will be started on login. <i><a href="/docs/linux/man/1-cinnamon-settings/">cinnamon-settings</a>(1)</i> can be used to easily configure them.</dl>
<p> <code>$XDG_CONFIG_HOME/cinnamon-session/sessions</code> <code>$XDG_CONFIG_DIRS/cinnamon-session/sessions</code> <code>$XDG_DATA_DIRS/cinnamon-session/sessions</code></p>
<dl>
<dt>
<dd> These directories contain the <code>.session</code> files that can be used with the <i>&#8211;session</i> option.</dl>
<p> <code>$XDG_CONFIG_HOME/cinnamon-session/saved-session</code></p>
<dl>
<dt>
<dd> This directory contains the list of applications of the saved session.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cinnamon-settings/">cinnamon-settings</a>(1)</code> <code><a href="/docs/linux/man/1-cinnamon-session-quit/">cinnamon-session-quit</a>(1)</code> </p>
<h2>Index</h2>
