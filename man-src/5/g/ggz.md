---
title: "ggz(5)"
name: "ggz"
section: "5"
letter: "g"
url: "/docs/linux/man/5-ggz/"
description: "ggz.modules – GGZ Gaming Zone module configuration file"
---

<p>ggz.modules &#8211; GGZ Gaming Zone module configuration file</p>
<h2>Description</h2>
<p>The GGZ Gaming Zone uses the file <i>ggz.modules</i> in order to configure which game modules are properly installed. The only approved method of altering this file is using the <i>ggz-config</i> utility, however the file structure is documented here in order to facilitate manual repairs if necessary.</p>
<h2>Parameters</h2>
<p>The <i>ggz.modules</i> file is formattted in sections, each of which begins with a <i>[SectionID]</i> line. The first (required) section is <i>[Games]</i>. This section is followed by any number of game-specific sections named <i>[g#]</i>. </p>
<p> The <i>[Games]</i> section is formatted as follows: </p>
<p> [Games]<br />
 <code>*GameList*</code> = GameName1 GameName2 &#8230;<br />
 <code>GameName1</code> = g1 g2 &#8230;<br />
 <code>GameName2</code> = g3 &#8230;</p>
<dl>
<dt><code>*GameList*</code></p>
<dd>Should be set to a list of all the game names which are currently installed. Each name should appear once and only once, and should be the internal game name (eg: <i>NetSpades</i>) and not the full descriptive name of the game.</p>
<dt><code>GameNameX</code></p>
<dd>Should equal a game name from the <i>*GameList*</i>, a real world example would be <i>NetSpades</i>. It should be set to a list of unique game section ID&#8217;s of the form <i>g#</i>. Each game section ID must be the name of a section ID which follows in the file. The ID&#8217;s need not be in any specific order, and ID numbers may be skipped but NOT repeated. </p>
</dl>
<p> A game section is formatted as follows: </p>
<p> <code>[g#]</code><br />
 Author = Game&#8217;s Author<br />
 CommandLine = /path/to/command [optionlist]<br />
 Frontend = <code>FECODE</code><br />
 Homepage = URL to Game&#8217;s homepage<br />
 Name = <code>GameName</code><br />
 Protocol = <code>ProtocolVersion</code><br />
 Version = <code>GameVersion</code> </p>
<p> Most of these parameters are self explanatory, however the following may need clarification:</p>
<dl>
<dt><code>[g#]</code></p>
<dd>This section code ID must be present in one of the game lists in the <i>[Games]</i> section above.</p>
<dt><code>FECODE</code></p>
<dd>The frontend code should be set to either <i>gtk</i> or <i>kde</i> depending on which user interface the game was designed for. Note that the game is expected to work with either the GTK+ or KDE clients, assuming that the user has the proper windowing system installed.</p>
<dt><code>GameName</code></p>
<dd>This must equal the game name (in the <i>[Games]</i> section) which properly points to this <i>[g#]</i> section.</p>
<dt><code>ProtocolVersion</code></p>
<dd>This will be used to match an installed game client with the protocol version currently used by the game server. This allows a new game client to be installed, while retaining the old client for backwards compatibility with older servers.</p>
<dt><code>GameVersion</code></p>
<dd>This is simply the version of the game client itself. It need not be the same version as the game server as long as the <i>ProtocolVersion</i> ID matches.</dl>
<h2>Files</h2>
<p><i>@ggzconfdir@/ggz.modules</i></p>
<h2>Authors</h2>
<p>The GGZ Development Team &lt;ggz-dev [at] mail.ggzgamingzone.org&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/6-ggz-config/">ggz-config</a>(6), <a href="/docs/linux/man/7-ggz/">ggz</a>(7) </p>
