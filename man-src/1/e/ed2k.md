---
title: "ed2k(1)"
name: "ed2k"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ed2k/"
description: "ed2k – aMule eD2k link parser"
---

<h2 class="name">NAME</h2>
<p> ed2k &#8211; aMule eD2k link parser </p>
<h2>SYNOPSIS</h2>
<p> [<code>-c</code> <i>&lt;path&gt;</i>] [<code>-t</code> <i>&lt;num&gt;</i>] _untranslated<code>[</code>-e<code>]</code> _untranslated<code>[</code>-l<code>]</code> <i>&lt;eD2k-link&gt;</i> </p>
<p> _untranslated<code>[</code>-h<code>]</code> </p>
<p> _untranslated<code>[</code>-v<code>]</code></p>
<h2>DESCRIPTION</h2>
<p> Sends the given <i>&lt;eD2k-link&gt;</i> to aMule, i.e. writes it to the file ~/.aMule/ED2KLinks, which will be checked by aMule every second for links.</p>
<dl>
<dt><code>[ -c</code> <i>&lt;path&gt;</i>, <code>&#8211;config-dir</code>=<i>&lt;path&gt;</i> <code>]</code></p>
<dd> Read config from <i>&lt;path&gt;</i> instead of home</p>
<dt><code>[ -t</code>, <code>&#8211;category</code>=<i>&lt;num&gt;</i> <code>]</code></p>
<dd> Set category for passed eD2k links to <i>&lt;num&gt;</i></p>
<dt>
<dd> Loads all link found in the emulecollection given as <i>&lt;ed2k-link&gt;</i></p>
<dt>
<dd> Lists all link found in the emulecollection given as <i>&lt;ed2k-link&gt;</i></p>
<dt>
<dd> Prints a short usage description.</p>
<dt>
<dd> Displays the current version number.</p>
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
<dd> a magnet link;</p>
<dt>&bull;</p>
<dd> an emulecollection file.</dl>
</dl>
<p> <code>The order in which you give the parameters is important.</code> You can give more than one link, and every link can have it&#8217;s own params. For example <code>ed2k &lt;link1&gt; -t2 &lt;link2&gt;</code> will download <i>&lt;link1&gt;</i> in standard category and <i>&lt;link2&gt;</i> in category 2.</p>
<h2>FILES</h2>
<p> ~/.aMule/ED2KLinks</p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs either on our forum (<i><a rel="nofollow" href="http://forum.amule.org/">http://forum.amule.org/</a></i>), or in our bugtracker (<i><a href="http://bugs.amule.org/">http://bugs.amule.org/</a></i>). Please do not report bugs in e-mail, neither to our mailing list nor directly to any team member.</p>
<h2>COPYRIGHT</h2>
<p> aMule and all of its related utilities are distributed under the GNU General Public License.</p>
<h2>SEE ALSO</h2>
<h2>AUTHOR</h2>
<p> This manpage was written by Vollstrecker &lt;amule [at] vollstreckernet.de&gt; </p>
<h2>Index</h2>
