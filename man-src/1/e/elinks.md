---
title: "elinks(1)"
name: "elinks"
section: "1"
letter: "e"
url: "/docs/linux/man/1-elinks/"
description: "elinks – lynx-like alternative character mode WWW browser"
---

<h2 class="name">NAME</h2>
<p> elinks &#8211; lynx-like alternative character mode WWW browser </p>
<h2>SYNOPSIS</h2>
<p> <i>elinks</i> [OPTION]&#8230; [URL]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <i>ELinks</i> is a text mode WWW browser, supporting colors, table rendering, background downloading, menu driven configuration interface, tabbed browsing and slim code. </p>
<p> Frames are supported. You can have different file formats associated with external viewers. mailto: and telnet: are supported via external clients. </p>
<p> ELinks can handle both local files and remote URLs. The main supported remote URL protocols are <i>HTTP</i>, <i>HTTPS</i> (with SSL support compiled in) and <i>FTP</i>. Additional protocol support exists for <i>BitTorrent</i> <i>finger</i>, <i>Gopher</i>, <i>SMB</i> and <i>NNTP</i>. </p>
<p> The homepage of <i>ELinks</i> can be found at &lt;<a rel="nofollow" href="http://elinks.cz/">http://elinks.cz/</a>&gt;, where the ELinks manual is also hosted. </p>
<h2>OPTIONS</h2>
<p> Most options can be set in the user interface or config file, so usually you do not need to care about them. Note that this list is roughly equivalent to the output of running ELinks with the option &#8211;long-help. </p>
<p> <code>-anonymous</code> <i>[0|1]</i> (default: 0)</p>
<dl>
<dt>
</dt><dd> Restricts ELinks so it can run on an anonymous account. Local file browsing, downloads, and modification of options will be disabled. Execution of viewers is allowed, but entries in the association table can&#8217;t be added or modified.</dd></dl>
<p> <code>-auto-submit</code> <i>[0|1]</i> (default: 0)</p>
<dl>
<dt>
</dt><dd> Automatically submit the first form in the given URLs.</dd></dl>
<p> <code>-base-session</code> <i>&lt;num&gt;</i> (default: 0)</p>
<dl>
<dt>
</dt><dd> Used internally when opening ELinks instances in new windows. The ID maps to information that will be used when creating the new instance. You don&#8217;t want to use it.</dd></dl>
<p> <code>-config-dir</code> <i>&lt;str&gt;</i> (default: &quot;&quot;)</p>
<dl>
<dt>
</dt><dd> Path of the directory ELinks will read and write its config and runtime state files to instead of <i>~/.elinks</i>. If the path does not begin with a &#8216;/&#8217; it is assumed to be relative to your <code>HOME</code> directory.</dd></dl>
<p> <code>-config-dump</code></p>
<dl>
<dt>
</dt><dd> Print a configuration file with options set to the built-in defaults to stdout.</dd></dl>
<p> <code>-config-file</code> <i>&lt;str&gt;</i> (default: &quot;elinks.conf&quot;)</p>
<dl>
<dt>
</dt><dd> Name of the configuration file that all configuration options will be read from and written to. It should be relative to config-dir.</dd></dl>
<p> <code>-config-help</code></p>
<dl>
<dt>
</dt><dd> Print help for configuration options and exit.</dd></dl>
<p> <code>-default-mime-type</code> (alias for mime.default_type)</p>
<dl>
<dt>
</dt><dd> The default MIME type used for documents of unknown type.</dd></dl>
<p> <code>-default-keys</code> <i>[0|1]</i> (default: 0)</p>
<dl>
<dt>
</dt><dd> When set, all keybindings from configuration files will be ignored. It forces use of default keybindings and will reset user-defined ones on save.</dd></dl>
<p> <code>-dump</code> <i>[0|1]</i> (default: 0)</p>
<dl>
<dt>
</dt><dd> Print formatted plain-text versions of given URLs to stdout.</dd></dl>
<p> <code>-dump-charset</code> (alias for document.dump.codepage)</p>
<dl>
<dt>
</dt><dd> Codepage used when formatting dump output.</dd></dl>
<p> <code>-dump-color-mode</code> (alias for document.dump.color_mode)</p>
<dl>
<dt>
</dt><dd> Color mode used with -dump.</dd></dl>
<p> <code>-dump-width</code> (alias for document.dump.width)</p>
<dl>
<dt>
</dt><dd> Width of the dump output.</dd></dl>
<p> <code>-eval</code></p>
<dl>
<dt>
</dt><dd> Specify configuration file directives on the command-line which will be evaluated after all configuration files has been read. Example usage: <code>-eval &#8216;set protocol.file.allow_special_files = 1&#8217;</code></dd></dl>
<p> <code>-force-html</code></p>
<dl>
<dt>
</dt><dd> Makes ELinks assume documents of unknown types are HTML. Useful when using ELinks as an external viewer from MUAs. This is equivalent to <code>-default-mime-type</code><code> text/html</code>.</dd></dl>
<p> <code>-?</code>, <code>-h</code>, <code>-help</code></p>
<dl>
<dt>
</dt><dd> Print usage help and exit.</dd></dl>
<p> <code>-localhost</code> <i>[0|1]</i> (default: 0)</p>
<dl>
<dt>
</dt><dd> Restricts ELinks to work offline and only connect to servers with local addresses (ie. 127.0.0.1). No connections to remote servers will be permitted.</dd></dl>
<p> <code>-long-help</code></p>
<dl>
<dt>
</dt><dd> Print detailed usage help and exit.</dd></dl>
<p> <code>-lookup</code></p>
<dl>
<dt>
</dt><dd> Look up specified host and print all DNS resolved IP addresses.</dd></dl>
<p> <code>-no-connect</code> <i>[0|1]</i> (default: 0)</p>
<dl>
<dt>
</dt><dd> Run ELinks as a separate instance instead of connecting to an existing instance. Note that normally no runtime state files (bookmarks, history, etc.) are written to the disk when this option is used. See also -touch-files.</dd></dl>
<p> <code>-no-home</code> <i>[0|1]</i> (default: 0)</p>
<dl>
<dt>
</dt><dd> Disables creation and use of files in the user specific home configuration directory (<i>~/.elinks</i>). It forces default configuration values to be used and disables saving of runtime state files.</dd></dl>
<p> <code>-no-numbering</code> (alias for document.dump.numbering)</p>
<dl>
<dt>
</dt><dd> Prevents printing of link number in dump output. </dd>
<p> Note that this really affects only -dump, nothing else.</dl>
<p> <code>-no-references</code> (alias for document.dump.references)</p>
<dl>
<dt>
</dt><dd> Prevents printing of references (URIs) of document links in dump output. </dd>
<p> Note that this really affects only -dump, nothing else.</dl>
<p> <code>-remote</code></p>
<dl>
<dt>
</dt><dd> Control a remote ELinks instance by passing commands to it. The option takes an additional argument containing the method which should be invoked and any parameters that should be passed to it. For ease of use, the additional method argument can be omitted in which case any URL arguments will be opened in new tabs in the remote instance. </dd>
<p> Following is a list of the supported methods: </p>
<dl>
<dt>
</dt><dd> &bull;<code>ping()</code>: look for a remote instance</dd></dl>
<dl>
<dt>
</dt><dd> &bull;<code>openURL()</code>: prompt URL in current tab</dd></dl>
<dl>
<dt>
</dt><dd> &bull;<code>openURL(</code><i>URL</i><code>)</code>: open URL in current tab</dd></dl>
<dl>
<dt>
</dt><dd> &bull;<code>openURL(</code><i>URL</i><code>, </code><code>new-tab</code><code>)</code>: open URL in new tab</dd></dl>
<dl>
<dt>
</dt><dd> &bull;<code>openURL(</code><i>URL</i><code>, </code><code>new-window</code><code>)</code>: open URL in new window</dd></dl>
<dl>
<dt>
</dt><dd> &bull;<code>addBookmark(</code><i>URL</i><code>)</code>: bookmark URL</dd></dl>
<dl>
<dt>
</dt><dd> &bull;<code>infoBox(</code><i>text</i><code>)</code>: show text in a message box</dd></dl>
<dl>
<dt>
</dt><dd> &bull;<code>reload()</code>: reload the document in the current tab</dd></dl>
<dl>
<dt>
</dt><dd> &bull;<code>xfeDoCommand(</code><code>openBrowser</code><code>)</code>: open new window</dd></dl>
</dl>
<p> <code>-session-ring</code> <i>&lt;num&gt;</i> (default: 0)</p>
<dl>
<dt>
</dt><dd> ID of session ring this ELinks session should connect to. ELinks works in so-called session rings, whereby all instances of ELinks are interconnected and share state (cache, bookmarks, cookies, and so on). By default, all ELinks instances connect to session ring 0. You can change that behaviour with this switch and form as many session rings as you want. Obviously, if the session-ring with this number doesn&#8217;t exist yet, it&#8217;s created and this ELinks instance will become the master instance (that usually doesn&#8217;t matter for you as a user much). </dd>
<p> Note that you usually don&#8217;t want to use this unless you&#8217;re a developer and you want to do some testing &#8211; if you want the ELinks instances each running standalone, rather use the -no-connect command-line option. Also note that normally no runtime state files are written to the disk when this option is used. See also -touch-files.</dl>
<p> <code>-source</code> <i>[0|1]</i> (default: 0)</p>
<dl>
<dt>
</dt><dd> Print given URLs in source form to stdout.</dd></dl>
<p> <code>-touch-files</code> <i>[0|1]</i> (default: 0)</p>
<dl>
<dt>
</dt><dd> When enabled, runtime state files (bookmarks, history, etc.) are written to disk, even when -no-connect or -session-ring is used. The option has no effect if not used in conjunction with any of these options.</dd></dl>
<p> <code>-verbose</code> <i>&lt;num&gt;</i> (default: 1)</p>
<dl>
<dt>
</dt><dd> The verbose level controls what messages are shown at start up and while running: </dd>
<dl>
<dt>
</dt><dd> &bull;0 means only show serious errors</dd></dl>
<dl>
<dt>
</dt><dd> &bull;1 means show serious errors and warnings</dd></dl>
<dl>
<dt>
</dt><dd> &bull;2 means show all messages</dd></dl>
</dl>
<p> <code>-version</code></p>
<dl>
<dt>
</dt><dd> Print ELinks version information and exit.</dd></dl>
<p> Generated using output from ELinks version 0.13.GIT. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> COMSPEC, SHELL</p>
<dl>
<dt>
</dt><dd> The shell used for File -&gt; OS Shell on DOS/Windows and UNIX, respectively.</dd></dl>
<p> EDITOR</p>
<dl>
<dt>
</dt><dd> The program to use for external editor (when editing textareas).</dd></dl>
<p> ELINKS_CONFDIR</p>
<dl>
<dt>
</dt><dd> The location of the directory containing configuration files. If not set the default is ~/.elinks/.</dd></dl>
<p> ELINKS_TWTERM, LINKS_TWTERM</p>
<dl>
<dt>
</dt><dd> The command to run when selecting File -&gt; New window and if TWDISPLAY is defined (default twterm -e).</dd></dl>
<p> ELINKS_XTERM, LINKS_XTERM</p>
<dl>
<dt>
</dt><dd> The command to run when selecting File -&gt; New window and if DISPLAY is defined (default xterm -e).</dd></dl>
<p> FTP_PROXY, HTTP_PROXY, HTTPS_PROXY</p>
<dl>
<dt>
</dt><dd> The host to proxy the various protocol traffic through.</dd></dl>
<p> NO_PROXY</p>
<dl>
<dt>
</dt><dd> A comma separated list of URLs which should not be proxied.</dd></dl>
<p> HOME</p>
<dl>
<dt>
</dt><dd> The path to the users home directory. Used when expanding ~/.</dd></dl>
<p> WWW_HOME</p>
<dl>
<dt>
</dt><dd> Homepage location (as in <code><a href="/docs/linux/man/1-lynx/">lynx</a></code>(1)).</dd></dl>
<h2>FILES</h2>
<p> Configuration files controlled by ELinks are located in the user configuration directory, defaulting to <i>~/.elinks/</i>. In addition to the files listed below, a user defined CSS stylesheet can be defined using the <i>document.css.stylesheet</i> option. </p>
<p> /etc/elinks/elinks.conf</p>
<dl>
<dt>
</dt><dd> Site-wide configuration file.</dd></dl>
<p> ~/.elinks/elinks.conf</p>
<dl>
<dt>
</dt><dd> Per-user config file, loaded after site-wide configuration.</dd></dl>
<p> ~/.elinks/bookmarks</p>
<dl>
<dt>
</dt><dd> Bookmarks file.</dd></dl>
<p> ~/.elinks/cookies</p>
<dl>
<dt>
</dt><dd> Cookies file.</dd></dl>
<p> ~/.elinks/exmodehist</p>
<dl>
<dt>
</dt><dd> Exmode history file.</dd></dl>
<p> ~/.elinks/formhist</p>
<dl>
<dt>
</dt><dd> Form history file.</dd></dl>
<p> ~/.elinks/globhist</p>
<dl>
<dt>
</dt><dd> History file containing most recently visited URLs.</dd></dl>
<p> ~/.elinks/gotohist</p>
<dl>
<dt>
</dt><dd> GoTo URL dialog history file.</dd></dl>
<p> ~/.elinks/hooks.{js,lua,pl,py,rb,scm}</p>
<dl>
<dt>
</dt><dd> Browser scripting hooks.</dd></dl>
<p> ~/.elinks/searchhist</p>
<dl>
<dt>
</dt><dd> Search history file.</dd></dl>
<p> ~/.elinks/socket</p>
<dl>
<dt>
</dt><dd> Internal <i>ELinks</i> socket for communication between its instances.</dd></dl>
<p> ~/.mailcap, /etc/mailcap</p>
<dl>
<dt>
</dt><dd> Mappings of MIME types to external handlers.</dd></dl>
<p> ~/.mime.types, /etc/mime.types</p>
<dl>
<dt>
</dt><dd> Mappings of file extensions to MIME types.</dd></dl>
<h2>BUGS</h2>
<p> Please report any other bugs you find to the either the ELinks mailing list at &lt;elinks-users [at] linuxfromscratch.org&gt; or if you prefer enter them into the bug tracking system &lt;<a rel="nofollow" href="http://bugzilla.elinks.cz/">http://bugzilla.elinks.cz/</a>&gt;. More information about how to get in contact with developers and getting help can be found on the community page &lt;<a rel="nofollow" href="http://elinks.cz/community.html">http://elinks.cz/community.html</a>&gt;. </p>
<h2>LICENSE</h2>
<p> <i>ELinks</i> is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/copyleft/gpl.html">http://www.gnu.org/copyleft/gpl.html</a>&gt; as published by the Free Software Foundation; version 2 of the License. </p>
<h2>AUTHORS</h2>
<p> The <i>Links</i> browser &#8211; on which <i>ELinks</i> is based &#8211; was written by Mikulas Patocka &lt;mikulas [at] artax.karlin.mff.cuni.cz&gt;. <i>ELinks</i> was written by Petr Baudis &lt;pasky [at] ucw.cz&gt;. See file AUTHORS in the source tree for a list of people contributing to this project. </p>
<p> This manual page was written by Peter Gervai &lt;grin [at] tolna.net&gt;, using excerpts from a (yet?) unknown <i>Links</i> fan for the <i>Debian GNU/Linux system</i> (but may be used by others). Contributions from Francis A. Holop. Extended, clarified and made more up-to-date by Petr Baudis &lt;pasky [at] ucw.cz&gt;. Updated by Zas &lt;zas [at] norz.org&gt;. The conversion to Asciidoc and trimming was done by Jonas Fonseca &lt;fonseca [at] diku.dk&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-elinkskeys/">elinkskeys</a></code>(5), <code><a href="/docs/linux/man/5-elinks-conf/">elinks.conf</a></code>(5), <code>links</code>(1), <code><a href="/docs/linux/man/1-lynx/">lynx</a></code>(1), <code><a href="/docs/linux/man/1-w3m/">w3m</a></code>(1), <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1) </p>
