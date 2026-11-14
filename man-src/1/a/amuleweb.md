---
title: "amuleweb(1)"
name: "amuleweb"
section: "1"
letter: "a"
url: "/docs/linux/man/1-amuleweb/"
description: "amuleweb – aMule web server"
---

<h2 class="name">NAME</h2>
<p> amuleweb &#8211; aMule web server </p>
<h2>SYNOPSIS</h2>
<p> [<code>-h</code> <i>&lt;host&gt;</i>] [<code>-p</code> <i>&lt;port&gt;</i>] [<code>-P</code> <i>&lt;password&gt;</i>] [<code>-f</code> <i>&lt;path&gt;</i>] _untranslated<code>[</code>-q<code>]</code> _untranslated<code>[</code>-v<code>]</code> [<code>-l</code> <i>&lt;lang&gt;</i>] _untranslated<code>[</code>-w<code>]</code> [<code>-t</code> <i>&lt;name&gt;</i>] [<code>-s</code> <i>&lt;port&gt;</i>] _untranslated<code>[</code>-u<code>]</code> [<code>-U</code> <i>&lt;port&gt;</i>] _untranslated<code>[</code>-z<code>]</code> _untranslated<code>[</code>-Z<code>]</code> [<code>-A</code> <i>&lt;password&gt;</i>] [<code>-G</code> <i>&lt;password&gt;</i>] _untranslated<code>[</code>-a|-d<code>]</code> _untranslated<code>[</code>-L<code>]</code> _untranslated<code>[</code>&#8211;no-php<code>]</code> _untranslated<code>[</code>-N<code>]</code> </p>
<p> [<code>&#8211;create-config-from</code>=<i>&lt;path&gt;</i>] </p>
<p> _untranslated<code>[</code>&#8211;help<code>]</code> </p>
<p> _untranslated<code>[</code>&#8211;version<code>]</code> </p>
<p> [<code>&#8211;amule-config-file</code>=<i>&lt;path&gt;</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>amuleweb</code> manages your access to amule through a web browser. You can start amuleweb together with <code><a href="/docs/linux/man/1-amule/">amule</a></code>(1), or separately, any time later. Options can be specified via command-line or via config-file. Command-line options take precedence over config-file options.</p>
<dl>
<dt><code>[ -h</code> <i>&lt;host&gt;</i>, <code>&#8211;host</code>=<i>&lt;host&gt;</i> <code>]</code></p>
<dd> Host where aMule is running (default: <i>localhost</i>). <i>&lt;host&gt;</i> might be an IP address or a DNS name</p>
<dt><code>[ -p</code> <i>&lt;port&gt;</i>, <code>&#8211;port</code>=<i>&lt;port&gt;</i> <code>]</code></p>
<dd> aMule&#8217;s port for External Connections, as set in Preferences-&gt;Remote Controls (default: <i>4712</i>)</p>
<dt><code>[ -P</code> <i>&lt;password&gt;</i>, <code>&#8211;password</code>=<i>&lt;password&gt;</i> <code>]</code></p>
<dd> External Connections password.</p>
<dt><code>[ -f</code> <i>&lt;path&gt;</i>, <code>&#8211;config-file</code>=<i>&lt;path&gt;</i> <code>]</code></p>
<dd> Use the given configuration file. Default configuration file is <i>~/.aMule/remote.conf</i></p>
<dt>
<dd> Do not print any output to stdout.</p>
<dt>
<dd> Be verbose &#8211; show also debug messages.</p>
<dt><code>[ -l</code> <i>&lt;lang&gt;</i>, <code>&#8211;locale</code>=<i>&lt;lang&gt;</i> <code>]</code></p>
<dd> Sets program locale (language). See the <code>NOTES</code> section for the description of the <i>&lt;lang&gt;</i> parameter.</p>
<dt>
<dd> Write command line options to config file and exit</p>
<dt><code>[ -t</code> <i>&lt;name&gt;</i>, <code>&#8211;template</code>=<i>&lt;name&gt;</i> <code>]</code></p>
<dd> Loads the template named <i>&lt;name&gt;</i>. See the <code>SKIN SUPPORT</code> section for details.</p>
<dt><code>[ -s</code> <i>&lt;port&gt;</i>, <code>&#8211;server-port</code>=<i>&lt;port&gt;</i> <code>]</code></p>
<dd> Webserver&#8217;s HTTP port. This is the port you must point your browser to (default: <i>4711</i>).</p>
<dt>
<dd>
 Enable UPnP.</p>
<dt><code>[ -U</code> <i>&lt;port&gt;</i>, <code>&#8211;upnp-port</code> <i>&lt;port&gt;</i> <code>]</code></p>
<dd> UPnP port.</p>
<dt>
<dd> Enables using gzip compression in HTTP traffic to save bandwidth.</p>
<dt>
<dd> Disables using gzip compression (this is the default).</p>
<dt><code>[ -A</code> <i>&lt;passwd&gt;</i>, <code>&#8211;admin-pass</code>=<i>&lt;passwd&gt;</i> <code>]</code></p>
<dd> Full access password for webserver.</p>
<dt><code>[ -G</code> <i>&lt;passwd&gt;</i>, <code>&#8211;guest-pass</code>=<i>&lt;passwd&gt;</i> <code>]</code></p>
<dd> Guest password for webserver.</p>
<dt>
<dd> Allows guest access.</p>
<dt>
<dd> Denies guest access (default).</p>
<dt>
<dd> Load/save webserver settings from/to remote aMule. This causes amuleweb to ignore command-line and config-file settings, and load them from aMule. When saving preferences none will be written to the config file, but to aMule. (Of course, this works only for those settings that can be set in aMule&#8217;s Preferences-&gt;Remote Controls.)</p>
<dt>
<dd> Disable PHP interpreter (deprecated)</p>
<dt>
<dd> Recompiles PHP pages on each request.</p>
<dt><code>[ &#8211;create-config-from</code>=<i>&lt;path&gt;</i> <code>]</code></p>
<dd> Create config file based upon <i>&lt;path&gt;</i>, which must point to a valid aMule config file, and then exit.</p>
<dt>
<dd> Prints a short usage description.</p>
<dt>
<dd> Displays the current version number.</p>
<dt><code>[ &#8211;amule-config-file</code>=<i>&lt;path&gt;</i> <code>]</code></p>
<dd> aMule config file path. <code>DO NOT USE DIRECTLY!</code> aMule uses this option when starting amuleweb at aMule startup. This option causes all other command-line and config-file settings to be ignored, preferences to be read from the given config file, and also implies the <code>-q -L</code> options.</dl>
<h2>NOTES</h2>
<h3>Paths</h3>
<p> For all options which take a <i>&lt;path&gt;</i> value, if the <i>path</i> contains no directory part (i.e. just a plain filename), then it is considered to be under the aMule configuration directory, <i>~/.aMule</i>.</p>
<h3>Languages</h3>
<p> The <i>&lt;lang&gt;</i> parameter for the <code>-l</code> option has the following form: <i>lang</i>[<code>_</code><i>LANG</i>][<code>.</code><i>encoding</i>][<code>@</code><i>modifier</i>] where <i>lang</i> is the primary language, <i>LANG</i> is a sublanguage/territory, <i>encoding</i> is the character set to use and <i>modifier</i> allows the user to select a specific instance of localization data within a single category. </p>
<p> For example, the following strings are valid:</p>
<dl>
<dt>
<dd> _untranslated<code>de</code><br />
 _untranslated<code>de_DE</code><br />
 _untranslated<code>de_DE.iso88591</code><br />
 _untranslated<code>de_DE [at] euro</code><br />
 _untranslated<code>de_DE.iso88591 [at] euro</code></dl>
<p> Though all the above strings are accepted as valid language definitions, <i>encoding</i> and <i>modifier</i> are yet unused. </p>
<p> In addition to the format above, you can also specify full language names in English &#8211; so <code>-l german</code> is also valid and is equal to <code>-l de_DE</code>. </p>
<p> When no locale is defined, either on command-line or in config file, system default language will be used.</p>
<h2>SKIN SUPPORT</h2>
<p> <code>amuleweb</code> is capable of displaying information in different skins. These skins are called templates, and you can make amuleweb load a specific template via the <code>-t</code> command line option. Templates are searched in two places: first in <i>~/.aMule/webserver/</i> and then in <i>/usr/share/amule/webserver/</i> if you installed with &#8211;prefix=/usr. </p>
<p> Each template must be in a subdirectory of the template name, and this directory must contain all files the template needs.</p>
<h2>FILES</h2>
<p> ~/.aMule/remote.conf<br />
 ~/.aMule/webserver/<br />
 <i>$(pkgdatadir)</i>/webserver/</p>
<h2>EXAMPLE</h2>
<p> Typically amuleweb will be first run as: </p>
<p> <code>amuleweb</code> <code>-h</code> <i>hostname</i> <code>-p</code> <i>ECport</i> <code>-P</code> <i>ECpassword</i> <code>-s</code> <i>HTTPport</i> <code>-A</code> <i>AdminPassword</i> <code>-w</code> </p>
<p> or </p>
<p> <code>amuleweb</code> <code>&#8211;create-config-from</code>=<i>/home/username/.aMule/amule.conf</i> </p>
<p> These will save settings to <i>$HOME/.aMule/remote.conf</i>, and later you only need to type: </p>
<p> Of course, you may specify any more or less options on the first example line, and you may also totally omit it.</p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs either on our forum (<i><a rel="nofollow" href="http://forum.amule.org/">http://forum.amule.org/</a></i>), or in our bugtracker (<i><a href="http://bugs.amule.org/">http://bugs.amule.org/</a></i>). Please do not report bugs in e-mail, neither to our mailing list nor directly to any team member.</p>
<h2>COPYRIGHT</h2>
<p> aMule and all of its related utilities are distributed under the GNU General Public License.</p>
<h2>SEE ALSO</h2>
<h2>AUTHOR</h2>
<p> This manpage was written by Vollstrecker &lt;amule [at] vollstreckernet.de&gt; </p>
<h2>Index</h2>
