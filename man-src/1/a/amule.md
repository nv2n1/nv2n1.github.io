---
title: "amule(1)"
name: "amule"
section: "1"
letter: "a"
url: "/docs/linux/man/1-amule/"
description: "amule – the all-platform eMule p2p client"
---

<h2 class="name">NAME</h2>
<p> amule &#8211; the all-platform eMule p2p client </p>
<h2>SYNOPSIS</h2>
<p> [<code>-c</code> <i>&lt;path&gt;</i>] [<code>-geometry</code> <i>&lt;geom&gt;</i>] _untranslated<code>[</code>-o<code>]</code> _untranslated<code>[</code>-r<code>]</code> [<code>-w</code> <i>&lt;path&gt;</i>] _untranslated<code>[</code>-d<code>]</code> _untranslated<code>[</code>-i<code>]</code> [<code>-t</code> <i>&lt;num&gt;</i>] [<i>eD2k-link</i>] </p>
<p> _untranslated<code>[</code>-v<code>]</code> </p>
<p> _untranslated<code>[</code>-h<code>]</code> </p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>[ -c</code> <i>&lt;path&gt;</i>, <code>&#8211;config-dir</code>=<i>&lt;path&gt;</i> <code>]</code></p>
<dd> Read config from <i>&lt;path&gt;</i> instead of home</p>
<dt><code>[ -geometry </code><i>&lt;geom&gt;</i> <code>]</code></p>
<dd> Sets the geometry of the app. <i>&lt;geom&gt;</i> uses the same format as standard X11 apps:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[<code>=</code>][<i>&lt;width&gt;</i>{<code>xX</code>}<i>&lt;height&gt;</i>][{<code>+-</code>}<i>&lt;xoffset&gt;</i>{<code>+-</code>}<i>&lt;yoffset&gt;</i>]</p>
<dt>
<dd> Prints log messages to stdout.</p>
<dt>
<dd> Resets config to default values.</p>
<dt><code>[ -w</code> <i>&lt;path&gt;</i>, <code>&#8211;use-amuleweb</code>=<i>&lt;path&gt;</i> <code>]</code></p>
<dd> Specify location of amuleweb binary to <i>&lt;path&gt;</i>.</p>
<dt>
<dd> Does not handle fatal exception.</p>
<dt>
<dd> Does not disable stdin.</p>
<dt><code>[ -t</code>, <code>&#8211;category</code>=<i>&lt;num&gt;</i> <code>]</code></p>
<dd> Set category for passed eD2k links to <i>&lt;num&gt;</i></p>
<dt>
<dd> Displays the current version number.</p>
<dt>
<dd> Prints a short usage description.</p>
<dt><code>[ eD2k-link ]</code></p>
<dd> Adds an eD2k-link to the core.</dl>
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
<dd> a serverlist link, in which case all servers in the list will be added to the server list;</p>
<dt>&bull;</p>
<dd> a magnet link.</dl>
</dl>
<h2>NOTES</h2>
<h3>Paths</h3>
<p> For all options which take a <i>&lt;path&gt;</i> value, if the <i>path</i> contains no directory part (i.e. just a plain filename), then it is considered to be under the aMule configuration directory, <i>~/.aMule</i>.</p>
<h2>FILES</h2>
<p> ~/.aMule/*</p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs either on our forum (<i><a rel="nofollow" href="http://forum.amule.org/">http://forum.amule.org/</a></i>), or in our bugtracker (<i><a href="http://bugs.amule.org/">http://bugs.amule.org/</a></i>). Please do not report bugs in e-mail, neither to our mailing list nor directly to any team member.</p>
<h2>COPYRIGHT</h2>
<p> aMule and all of its related utilities are distributed under the GNU General Public License.</p>
<h2>SEE ALSO</h2>
<h2>AUTHOR</h2>
<p> This manpage was written by Vollstrecker &lt;amule [at] vollstreckernet.de&gt; </p>
<h2>Index</h2>
