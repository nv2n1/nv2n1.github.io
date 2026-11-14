---
title: "gnome-extensions(1)"
name: "gnome-extensions"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-extensions/"
description: "gnome-extensions – Command line tool for managing GNOME extensions"
---

<h2 class="name">NAME</h2>
<p> gnome-extensions &#8211; Command line tool for managing GNOME extensions </p>
<h2>SYNOPSIS</h2>
<p> <code>gnome-extensions</code> help [<i>COMMAND</i>] </p>
<p> <code>gnome-extensions</code> version </p>
<p> <code>gnome-extensions</code> enable <i>UUID</i> </p>
<p> <code>gnome-extensions</code> disable <i>UUID</i> </p>
<p> <code>gnome-extensions</code> reset <i>UUID</i> </p>
<p> <code>gnome-extensions</code> info <i>UUID</i> </p>
<p> <code>gnome-extensions</code> show <i>UUID</i> </p>
<p> <code>gnome-extensions</code> list [<i>OPTION</i>&#8230;] </p>
<p> <code>gnome-extensions</code> prefs <i>UUID</i> </p>
<p> <code>gnome-extensions</code> create [<i>OPTION</i>&#8230;] </p>
<p> <code>gnome-extensions</code> pack [<i>OPTION</i>&#8230;] </p>
<p> <code>gnome-extensions</code> install [<i>OPTION</i>&#8230;] <i>PACK</i> </p>
<p> <code>gnome-extensions</code> uninstall <i>UUID</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gnome-extensions</code> is a utility that makes some common GNOME extensions operations available on the command line.</p>
<h2>COMMON OPTIONS</h2>
<p> All commands except for <code>help</code> and <code>version</code> handle the following options: </p>
<p> <code>&#8211;quiet</code>, <code>-q</code></p>
<dl>
<dt>
<dd> Do not print error messages</dl>
<h2>COMMANDS</h2>
<p> <code>help</code> [<i>COMMAND</i>]</p>
<dl>
<dt>
<dd> Displays a short synopsis of the available commands or provides detailed help on a specific command.</dl>
<p> <code>version</code></p>
<dl>
<dt>
<dd> Prints the program version.</dl>
<p> <code>enable</code> <i>UUID</i></p>
<dl>
<dt>
<dd> Enables the extension identified by <i>UUID</i>. </p>
<p> The command will not detect any errors from the extension itself, use the <code>info</code> command to confirm that the extension state is <code>ENABLED</code>. </p>
<p> If the extension is already enabled, the command will do nothing.</dl>
<p> <code>disable</code> <i>UUID</i></p>
<dl>
<dt>
<dd> Disables the extension identified by <i>UUID</i>. </p>
<p> If the extension is not enabled, the command will do nothing.</dl>
<p> <code>reset</code> <i>UUID</i></p>
<dl>
<dt>
<dd> Reset the extension identified by <i>UUID</i>. </p>
<p> The extension will be disabled in GNOME, but may be enabled by other sessions like GNOME Classic.</dl>
<p> <code>info</code> <i>UUID</i></p>
<dl>
<dt>
<dd> Show details of the extension identified by <i>UUID</i>, including name, description and state.</dl>
<p> <code>show</code> <i>UUID</i></p>
<dl>
<dt>
<dd> Synonym of info.</dl>
<p> <code>list</code> [<i>OPTION</i>&#8230;]</p>
<dl>
<dt>
<dd> Displays a list of installed extensions. </p>
<p> <code>Options</code></p>
<dl>
<dt>
<dd> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Include extensions installed in the user&#8217;s <code>$HOME</code></dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Include extensions installed in the system</dl>
<p> <code>&#8211;enabled</code></p>
<dl>
<dt>
<dd> Include enabled extensions</dl>
<p> <code>&#8211;disabled</code></p>
<dl>
<dt>
<dd> Include disabled extensions</dl>
<p> <code>&#8211;prefs</code></p>
<dl>
<dt>
<dd> Only include extensions with preferences</dl>
<p> <code>&#8211;updates</code></p>
<dl>
<dt>
<dd> Only include extensions with pending updates</dl>
<p> <code>-d</code>, <code>&#8211;details</code></p>
<dl>
<dt>
<dd> Show some extra information for each extension</dl>
</dl>
</dl>
<p> <code>prefs</code> <i>UUID</i></p>
<dl>
<dt>
<dd> Open the preference dialog of the extension identified by <i>UUID</i>.</dl>
<p> <code>create</code> [<i>OPTION</i>&#8230;]</p>
<dl>
<dt>
<dd> Creates a new extension from a template. </p>
<p> <code>Options</code></p>
<dl>
<dt>
<dd> <code>&#8211;name</code>=<i>NAME</i></p>
<dl>
<dt>
<dd> Set the user-visible name in the extension&#8217;s metadata to <i>NAME</i></dl>
<p> <code>&#8211;description</code>=<i>DESC</i></p>
<dl>
<dt>
<dd> Set the description in the extension&#8217;s metadata to <i>DESC</i></dl>
<p> <code>&#8211;uuid</code>=<i>UUID</i></p>
<dl>
<dt>
<dd> Set the unique extension ID in the metadata to <i>UUID</i></dl>
<p> <code>&#8211;template</code>=<i>TEMPLATE</i></p>
<dl>
<dt>
<dd> Use <i>TEMPLATE</i> as base for the new extension</dl>
<p> <code>-i</code>, <code>&#8211;interactive</code></p>
<dl>
<dt>
<dd> Prompt for any extension metadata that hasn&#8217;t been provided on the command line</dl>
</dl>
</dl>
<p> <code>pack</code> [<i>OPTION</i>&#8230;] [<i>SOURCE-DIRECTORY</i>]</p>
<dl>
<dt>
<dd> Creates an extension bundle that is suitable for publishing. </p>
<p> The bundle will always include the required files extension.js and metadata.json, as well as the optional stylesheet.css and prefs.js if found. Each additional source that should be included must be specified with <code>&#8211;extra-source</code>. </p>
<p> If the extension includes one or more GSettings schemas, they can either be placed in a schemas/ folder to be picked up automatically, or be specified with <code>&#8211;schema</code>. </p>
<p> Similarily, translations are included automatically when they are located in a po/ folder, otherwise the <code>&#8211;podir</code> option can be used to point to the correct directory. If no gettext domain is provided on the command line, the value of the <code>gettext-domain</code> metadata field is used if it exists, and the extension UUID if not. </p>
<p> All files are searched in <i>SOURCE-DIRECTORY</i> if specified, or the current directory otherwise. </p>
<p> <code>Options</code></p>
<dl>
<dt>
<dd> <code>&#8211;extra-source</code>=<i>FILE</i></p>
<dl>
<dt>
<dd> Additional source to include in the bundle</dl>
<p> <code>&#8211;schema</code>=<i>SCHEMA</i></p>
<dl>
<dt>
<dd> A GSettings schema that should be compiled and included</dl>
<p> <code>&#8211;podir</code>=<i>PODIR</i></p>
<dl>
<dt>
<dd> A directory with translations that should be compiled and included</dl>
<p> <code>&#8211;gettext-domain</code>=<i>DOMAIN</i></p>
<dl>
<dt>
<dd> The gettext domain to use for translations</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Overwrite an existing pack</dl>
<p> <code>-o</code>, <code>&#8211;out-dir</code>=<i>DIRECTORY</i></p>
<dl>
<dt>
<dd> The directory where the pack should be created</dl>
</dl>
</dl>
<p> <code>install</code> [<i>OPTION</i>&#8230;] <i>PACK</i></p>
<dl>
<dt>
<dd> Installs an extension from the bundle <i>PACK</i>. </p>
<p> The command unpacks the extension files and moves them to the expected location in the user&#8217;s <code>$HOME</code>, so that it will be loaded in the next session. </p>
<p> It is mainly intended for testing, not as a replacement for the extension website. As extensions have privileged access to the user&#8217;s session, it is advised to never load extensions from untrusted sources without carefully reviewing their content. </p>
<p> <code>Options</code></p>
<dl>
<dt>
<dd> <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Override an existing extension</dl>
</dl>
</dl>
<p> <code>uninstall</code> <i>UUID</i></p>
<dl>
<dt>
<dd> Uninstalls the extension identified by <i>UUID</i>.</dl>
<h2>EXIT STATUS</h2>
<p> On success 0 is returned, a non-zero failure code otherwise.</p>
<h2>BUGS</h2>
<p> The tool is part of the gnome-shell project, and bugs should be reported in its issue tracker at m[blue]<code><a rel="nofollow" href="https://gitlab.gnome.org/GNOME/gnome-shell/issues">https://gitlab.gnome.org/GNOME/gnome-shell/issues</a></code>m[]. </p>
<h2>Index</h2>
