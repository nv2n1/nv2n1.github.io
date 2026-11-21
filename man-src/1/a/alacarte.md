---

title: "alacarte(1)"
name: "alacarte"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alacarte/"
description: "alacarte – Edit freedesktop.org menus"
---

<p> alacarte &#8211; Edit freedesktop.org menus </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>alacarte</code></dt></dl>
<h2>DESCRIPTION</h2>
<dd>alacarte is a graphical editor for the freedesktop.org menus that are used by many desktop environments. It can also edit and create application desktop files.</dd>
<h2>OPTIONS</h2>
<p> <code>alacarte</code> does not accept any commandline options.</p>
<h2>ENVIRONMENT</h2>
<p> <code>XDG_CONFIG_DIRS</code></p>
<dl>
<dt>
</dt><dd> <code>alacarte</code> looks in the menus subdirectory of these directories for menu files. The default location for menu files is /etc/xdg/menus.</dd></dl>
<p> <code>XDG_DATA_DIRS</code></p>
<dl>
<dt>
</dt><dd> <code>alacarte</code> looks in the applications subdirectory of these directories for desktop files. The default location for desktop files is /usr/share/applications.</dd></dl>
<p> <code>XDG_CONFIG_HOME</code></p>
<dl>
<dt>
</dt><dd> The menus subdirectory of this directory is where <code>alacarte</code> stores modified menu files. The default location for modified menu files is <code>$HOME</code>/.config/menus.</dd></dl>
<p> <code>XDG_DATA_HOME</code></p>
<dl>
<dt>
</dt><dd> The applications subdirectory of this directory is where <code>alacarte</code> stores modified and newly created desktop files. The default location for these is <code>$HOME</code>/.local/share/applications.</dd></dl>
<p> <code>XDG_MENU_PREFIX</code></p>
<dl>
<dt>
</dt><dd> <code>alacarte</code> is editing the menus defined by the file <code>$XDG_MENU_PREFIX</code>applications.menu. GNOME uses the menu file gnome-applications.menu.</dd></dl>
