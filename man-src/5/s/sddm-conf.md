---
title: "sddm-conf(5)"
name: "sddm-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sddm-conf/"
description: "sddm.conf – sddm display manager configuration"
---

<p>sddm.conf &#8211; sddm display manager configuration</p>
<h2>Synopsis</h2>
<p>/etc/sddm.conf</p>
<h2>Description</h2>
<p>This file configures various parameters of the sddm display manager <code><a href="/docs/linux/man/1-sddm/">sddm</a></code>(1). If this file is not available, default values are used.</p>
<h2>Options</h2>
<p>[General] section:</p>
<dl>
<dt><i>HaltCommand=</i></p>
<dd>Halt command. Default value is &quot;/usr/bin/systemctl poweroff&quot;.</p>
<dt><i>RebootCommand=</i></p>
<dd>Reboot command. Default value is &quot;/usr/bin/systemctl reboot&quot;.</p>
<dt><i>Numlock=</i></p>
<dd>Change numlock state when <code>sddm-greeter</code> starts. Valid values are <i>on</i>, <i>off</i> or <i>none</i>. If property is set to <i>none</i>, numlock won&#8217;t be changed. Default value is &quot;none&quot;.</p>
<dt><i>InputMethod=</i></p>
<dd>Set the Qt input method for the greeter. Tablet users with Qt Virtual Keyboard installed can set this to &quot;qtvirtualkeyboard&quot; for the on-screen keyboard. Other known values are &quot;ibus&quot; for the Intelligent Input Bus, or &quot;compose&quot; for dead keys support. Leave this empty if unsure. </p>
<p> [Theme] section:</p>
<dt><i>ThemeDir=</i></p>
<dd>Path of the directory containing theme files. Default value is &quot;/usr/share/sddm/themes&quot;.</p>
<dt><i>Current=</i></p>
<dd>Name of the current theme. Default value is &quot;maui&quot;.</p>
<dt><i>FacesDir=</i></p>
<dd>Path of the directory containing face files, face files should be in username.face.icon format. Default value is &quot;/usr/share/sddm/faces&quot;.</p>
<dt><i>CursorTheme=</i></p>
<dd>Name of the cursor theme to be set before starting the display server.</p>
<dt><i>EnableAvatars=</i></p>
<dd>When enabled, home directories are searched for &quot;.face.icon&quot; images to display as their avatars. This can be slow on some file systems. When disabled, all avatars will be default. Themes may choose to hide them altogether. Default value is true. </p>
<p> [X11] section:</p>
<dt><i>ServerPath=</i></p>
<dd>Path of the X server. Default value is &quot;/usr/bin/X&quot;.</p>
<dt><i>ServerArguments=</i></p>
<dd>Arguments to the X server. Default value is &quot;-nolisten tcp&quot;.</p>
<dt><i>XephyrPath=</i></p>
<dd>Path of the Xephyr. Default value is &quot;/usr/bin/Xephyr&quot;.</p>
<dt><i>XauthPath=</i></p>
<dd>Path of the Xauth. Default value is &quot;/usr/bin/xauth&quot;.</p>
<dt><i>SessionDir=</i></p>
<dd>Path of the directory containing session files. Default value is &quot;/usr/share/xsessions&quot;.</p>
<dt><i>SessionCommand=</i></p>
<dd>Path of script to execute when starting the user session. This script receives the value of the &quot;Exec&quot; setting in the &quot;.desktop&quot; file of the selected session and runs it. Default value is &quot;/etc/X11/xinit/Xsession&quot;.</p>
<dt><i>SessionLogFile=</i></p>
<dd>Path to the user session log file, relative to the home directory. Default value is &quot;.local/share/sddm/xorg-session.log&quot;.</p>
<dt><i>UserAuthFile=</i></p>
<dd>Path to the Xauthority file, relative to the home directory. Default value is &quot;.Xauthority&quot;.</p>
<dt><i>DisplayCommand=</i></p>
<dd>Path of script to execute when starting the display server. Default value is &quot;/usr/share/sddm/scripts/Xsetup&quot;.</p>
<dt><i>DisplayStopCommand=</i></p>
<dd>Path of script to execute when stopping the display server. Default value is &quot;/usr/share/sddm/scripts/Xstop&quot;.</p>
<dt><i>MinimumVT=</i></p>
<dd>Minimum virtual terminal number that will be used by the first display. Virtual terminal number will increase as new displays added. Default value is 1. </p>
<p> [Wayland] section:</p>
<dt><i>SessionDir=</i></p>
<dd>Path of the directory containing session files. Default value is &quot;/usr/share/wayland-sessions&quot;.</p>
<dt><i>SessionCommand=</i></p>
<dd>Path of script to execute when starting the user session. This script receives the value of the &quot;Exec&quot; setting in the &quot;.desktop&quot; file of the selected session and run it. Default value is &quot;/etc/sddm/wayland-session&quot;.</p>
<dt><i>SessionLogFile=</i></p>
<dd>Path to the user session log file, relative to the home directory. Default value is &quot;.local/share/sddm/wayland-session.log&quot;. </p>
<p> [Users] section:</p>
<dt><i>DefaultPath=</i></p>
<dd>Default path to set after successfully logging in. Default value is &quot;/bin:/usr/bin:/usr/local/bin&quot;.</p>
<dt><i>MinimumUid=</i></p>
<dd>Minimum user id of the users to be listed in the user interface. Default value is 1000.</p>
<dt><i>MaximumUid=</i></p>
<dd>Maximum user id of the users to be listed in the user interface. Default value is 60000</p>
<dt><i>HideUsers=</i></p>
<dd>Comma-separated list of Users that shouldn&#8217;t show up in the user list. Default value is empty.</p>
<dt><i>HideShells=</i></p>
<dd>Comma-separated list of Shells of users that shouldn&#8217;t show up in the user list. Default value is empty.</p>
<dt><i>RememberLastUser=</i></p>
<dd>If this flag is true, LastUser value will updated on every successful login, if false last user value won&#8217;t be updated. Default value is true.</p>
<dt><i>RememberLastSession=</i></p>
<dd>If this flag is true, LastSession value will updated on every successful login, if false last session value won&#8217;t be updated. Default value is true. </p>
<p> [Autologin] section:</p>
<dt><i>User=</i></p>
<dd>Name of the user to automatically log in when the system starts first time. Default value is empty.</p>
<dt><i>Session=</i></p>
<dd>Name of the session to automatically log in when the system starts first time. Default value is empty.</p>
<dt><i>Relogin=</i></p>
<dd>If true and User and Session are set automatic login will kick in again on session exit, otherwise it will work only the first time. Default value is false.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sddm/">sddm</a></code>(1) The full documentation for sddm is available at <i><a rel="nofollow" href="https://github.com/sddm/sddm">https://github.com/sddm/sddm</a></i> </p>
