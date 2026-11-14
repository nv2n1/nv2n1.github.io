---
title: "amulecmd(1)"
name: "amulecmd"
section: "1"
letter: "a"
url: "/docs/linux/man/1-amulecmd/"
description: "amulecmd – Console-based program to control aMule"
---

<h2 class="name">NAME</h2>
<p> amulecmd &#8211; Console-based program to control aMule </p>
<h2>SYNOPSIS</h2>
<p> [<code>-h</code> <i>&lt;host&gt;</i>] [<code>-p</code> <i>&lt;port&gt;</i>] [<code>-P</code> <i>&lt;password&gt;</i>] [<code>-f</code> <i>&lt;path&gt;</i>] _untranslated<code>[</code>-q<code>]</code> _untranslated<code>[</code>-v<code>]</code> [<code>-l</code> <i>&lt;lang&gt;</i>] {[<code>-w</code>]|[<code>-c</code> <i>&lt;command&gt;</i>]} </p>
<p> [<code>&#8211;create-config-from</code>=<i>&lt;path&gt;</i>] </p>
<p> _untranslated<code>[</code>&#8211;version<code>]</code> </p>
<p> _untranslated<code>[</code>&#8211;help<code>]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>amulecmd</code> is a console-based client to control aMule.</p>
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
<dt><code>[ -c</code> <i>&lt;command&gt;</i>, <code>&#8211;command</code>=<i>&lt;command&gt;</i> <code>]</code></p>
<dd> Execute <i>&lt;command&gt;</i> as if it was entered at amulecmd&#8217;s prompt and exit.</p>
<dt><code>[ &#8211;create-config-from</code>=<i>&lt;path&gt;</i> <code>]</code></p>
<dd> Create config file based upon <i>&lt;path&gt;</i>, which must point to a valid aMule config file, and then exit.</p>
<dt>
<dd> Displays the current version number.</p>
<dt>
<dd> Prints a short usage description.</dl>
<h2>COMMANDS</h2>
<p> All commands are case insensitive.</p>
<h3>Add <i>&lt;eD2k-link&gt;</i> | <i>&lt;magnet-link&gt;</i></h3>
<p> Adds an eD2k-link or a magnet-link to the core. </p>
<p> The eD2k link to be added can be:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> a file link (ed2k://|file|&#8230;), it will be added to the download queue;</p>
<dt>&bull;</p>
<dd> a server link (ed2k://|server|&#8230;), it will be added to the server list;</p>
<dt>&bull;</p>
<dd> a serverlist link, in which case all servers in the list will be added to the server list.</dl>
</dl>
<p> The magnet link must contain the eD2k hash and file length.</p>
<h3>Cancel <i>&lt;hash&gt;</i> | <i>&lt;number&gt;</i></h3>
<p> Cancels the download specified by <i>&lt;hash&gt;</i> or <i>&lt;number&gt;</i>. To get the value use <code>show</code>.</p>
<h3>Connect [ <i>kad</i> | <i>ed2k</i> | <i>&lt;ip|name&gt;</i> ]</h3>
<p> Connect to the network. </p>
<p> This will connect to all networks that are enabled in Preferences. </p>
<p> With the optional parameter you can specify which network to connect to. Giving a server address in the form of IP:Port (where IP is either a dotted decimal IPv4 address or a resolvable DNS name) aMule will connect to that server only.</p>
<h3>_untranslated Disconnect [ <i>ed2k</i> | <i>kad</i> ]</h3>
<p> Disconnect from all networks you are connected to, or just disconnect from the specified network.</p>
<h3>Download <i>&lt;number&gt;</i></h3>
<p> Start downloading a file. </p>
<p> The <i>&lt;number&gt;</i> of a file from the last search has to be given. Example: `download 12&#8242; will start to download the file with the number 12 of the previous search.</p>
<h3>_untranslated Exit</h3>
<p> Disconnect from amule/amuled and quit amulecmd.</p>
<h3>Get <i>&lt;what&gt;</i></h3>
<p> Get and display a preference value. </p>
<p> Available values for <i>&lt;what&gt;</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>BwLimits</p>
<dd> Get bandwidth limits.</p>
<dt>IPFilter</p>
<dd> Get IPFilter preferences.</dl>
</dl>
<h3>Help [ <i>&lt;command&gt;</i> ]</h3>
<p> Prints a short usage description. If called without parameter, it shows a list of available commands. If called with <i>&lt;command&gt;</i>, it shows a short description of the given command.</p>
<h3>Pause <i>&lt;hash&gt;</i> | <i>&lt;number&gt;</i></h3>
<p> Pauses the download specified by <i>&lt;hash&gt;</i> or <i>&lt;number&gt;</i>. To get the value use <code>show</code>.</p>
<h3>Priority <i>&lt;priority&gt;</i> <i>&lt;hash&gt;</i> | <i>&lt;number&gt;</i></h3>
<p> Set priority of a download specified by <i>&lt;hash&gt;</i> or <i>&lt;number&gt;</i>. </p>
<p> Available values for <i>&lt;priority&gt;</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Auto</p>
<dd> Automatic priority.</p>
<dt>High</p>
<dd> High priority.</p>
<dt>Low</p>
<dd> Low priority.</p>
<dt>Normal</p>
<dd> Normal priority.</dl>
</dl>
<h3>_untranslated Progress</h3>
<p> Shows the progress of an on-going search.</p>
<h3>_untranslated Quit</h3>
<p> A synonim of the <code>exit</code> command.</p>
<h3>Reload <i>&lt;what&gt;</i></h3>
<p> Reloads a given object. </p>
<p> Available values for <i>&lt;what&gt;</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Shared</p>
<dd> Reload shared files list.</p>
<dt>IPFilter</p>
<dd> Reload IP filter tables.</dl>
</dl>
<h3>_untranslated Reset</h3>
<p> Reset the log.</p>
<h3>_untranslated Results</h3>
<p> Shows you the results of the last search.</p>
<h3>Resume <i>&lt;hash&gt;</i> | <i>&lt;number&gt;</i></h3>
<p> Resumes the download specified by <i>&lt;hash&gt;</i> or <i>&lt;number&gt;</i>. To get the value use <code>show</code>.</p>
<h3>Search <i>&lt;type&gt;</i> <i>&lt;keyword&gt;</i></h3>
<p> Makes a search for the given <i>&lt;keyword&gt;</i>. A search type and a keyword to search is mandatory to do this. Example: `search kad amule&#8217; performs a kad search for `amule&#8217;. </p>
<p> Available search types:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Global</p>
<dd> Performs a global search.</p>
<dt>Kad</p>
<dd> Performs a search on the Kademlia network.</p>
<dt>Local</p>
<dd> Performs a local search.</dl>
</dl>
<h3>Set <i>&lt;what&gt;</i></h3>
<p> Sets a given preferences value. </p>
<p> Available values for <i>&lt;what&gt;</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>BwLimits</p>
<dd> Set bandwidth limits.</p>
<dt>IPFilter</p>
<dd> Set IPFilter preferences.</dl>
</dl>
<h3>Show <i>&lt;what&gt;</i></h3>
<p> Shows upload/download queue, servers list or shared files list. </p>
<p> Available values for <i>&lt;what&gt;</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>DL</p>
<dd> Show download queue.</p>
<dt>Log</p>
<dd> Show log.</p>
<dt>Servers</p>
<dd> Show servers list.</p>
<dt>UL</p>
<dd> Show upload queue.</dl>
</dl>
<h3>_untranslated Shutdown</h3>
<p> Shutdown the remote running core (amule/amuled). This will also shut down the text client, since it is unusable without a running core.</p>
<h3>Statistics [ <i>&lt;number&gt;</i> ]</h3>
<p> Show statistics tree. </p>
<p> The optional <i>&lt;number&gt;</i> in the range of 0-255 can be passed as argument to this command, which tells how many entries of the client version subtree should be shown. Passing 0, or omitting it means `unlimited&#8217;. </p>
<p> Example: `statistics 5&#8242; will show only the top 5 versions for each client type.</p>
<h3>_untranslated Status</h3>
<p> Show connection status, current up/download speeds, etc.</p>
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
<h2>FILES</h2>
<p> ~/.aMule/remote.conf</p>
<h2>EXAMPLE</h2>
<p> Typically amulecmd will be first run as: </p>
<p> <code>amulecmd</code> <code>-h</code> <i>hostname</i> <code>-p</code> <i>ECport</i> <code>-P</code> <i>ECpassword</i> <code>-w</code> </p>
<p> or </p>
<p> <code>amulecmd</code> <code>&#8211;create-config-from</code>=<i>/home/username/.aMule/amule.conf</i> </p>
<p> These will save settings to <i>$HOME/.aMule/remote.conf</i>, and later you only need to type: </p>
<p> Of course, you don&#8217;t have to follow this example.</p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs either on our forum (<i><a rel="nofollow" href="http://forum.amule.org/">http://forum.amule.org/</a></i>), or in our bugtracker (<i><a href="http://bugs.amule.org/">http://bugs.amule.org/</a></i>). Please do not report bugs in e-mail, neither to our mailing list nor directly to any team member.</p>
<h2>COPYRIGHT</h2>
<p> aMule and all of its related utilities are distributed under the GNU General Public License.</p>
<h2>SEE ALSO</h2>
<h2>AUTHOR</h2>
<p> This manpage was written by Vollstrecker &lt;amule [at] vollstreckernet.de&gt; </p>
<h2>Index</h2>
<dt><a href="#lbBB">NOTES</a></p>
<dd>
<dt><a href="#lbBE">FILES</a></p>
<dd>
<dt><a href="#lbBF">EXAMPLE</a></p>
<dd>
<dt><a href="#lbBG">REPORTING BUGS</a></p>
<dd>
<dt><a href="#lbBH">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbBI">SEE ALSO</a></p>
<dd>
<dt><a href="#lbBJ">AUTHOR</a></p>
<dd></dl>
