---
title: "audtty(1)"
name: "audtty"
section: "1"
letter: "a"
url: "/docs/linux/man/1-audtty/"
description: "audtty – Control Audacious from the command line with a friendly ncurses interface"
---

<h2>NAME</h2>
<p> audtty &#8211; Control Audacious from the command line with a friendly ncurses interface</p>
<h2>SYNOPSIS</h2>
<p> <code>audtty</code> [&lt;<code>&#8211;</code>|<code>+</code>&gt;ahlntV<code>]</code> [ <i>options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> audtty is a simple application for controlling Audacious from the command line. It is designed to make common, simple tasks fast and easy to do. It is operated using arrow keys and standard Audacious keys, to make it easy and intuitive to learn.</p>
<h2>OPTIONS</h2>
<p> To negate a short option, use &#8216;<code>+</code>&#8216; instead of &#8216;<code>&#8211;</code>&#8216; (e.g. <code>+a</code>).<br />
 Long-options are negated with <code>no-</code>, (e.g. <code>&#8211;no-read-all</code>).</p>
<dl>
<dt><code>The keys for basic control are as follows:</code></p>
<dd> +&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;+<br />
 | &lt;&lt; &gt; || o &gt;&gt; |<br />
 +&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;+ </p>
<p>&nbsp;<wbr>z&nbsp;<wbr>&nbsp;<wbr>x&nbsp;<wbr>&nbsp;<wbr>c&nbsp;<wbr>&nbsp;<wbr>v&nbsp;<wbr>&nbsp;<wbr>b</p>
<dt><code>-a, &#8211;read-all</code></p>
<dd> Read all titles and lengths on startup (EXTREMELY SLOW) (default off).</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print help message.</p>
<dt><code>-l, &#8211;length</code></p>
<dd> Show length of track in playlist (SLOW) (default on).</p>
<dt><code>-n, &#8211;numbers</code></p>
<dd> Show numbers in playlist (default on).</p>
<dt><code>-t, &#8211;title</code></p>
<dd> Read the title from ID3/ogg-tags (SLOW) (default on).</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Display version information.</dl>
<p> Tip: Things going slow? Try <code>audtty -ntl</code></p>
<h2>KEYS</h2>
<dl>
<dt><code>Arrow right/left</code></p>
<dd> Skip forward/backward 5 seconds.</p>
<dt><code>Arrow up/down</code></p>
<dd> Move up/down in the playlist or search results.</p>
<dt><code>Page up/down</code></p>
<dd> Scroll up/down one page in the playlist or search results.</p>
<dt><code>Enter</code></p>
<dd> Select and play file.</p>
<dt><code>Esc</code></p>
<dd> Exit from application, or, if in other dialog, go to main view.</p>
<dt><code>0 or +</code></p>
<dd> Increase volume.</p>
<dt><code>9 or &#8211;</code></p>
<dd> Decrease volume.</p>
<dt><code>a</code></p>
<dd> Open a file browser window.</p>
<dt><code>b</code></p>
<dd> Jump to next song.</p>
<dt><code>c</code></p>
<dd> Pause.</p>
<dt><code>d</code></p>
<dd> Remove currently selected item from playlist.</p>
<dt><code>j</code></p>
<dd> Search for file to jump to.</p>
<dt><code>L</code></p>
<dd> Add URI to playlist.</p>
<dt><code>q</code></p>
<dd> Exit from application.</p>
<dt><code>R</code></p>
<dd> Reload playlist.</p>
<dt><code>u</code></p>
<dd> Save playlist.</p>
<dt><code>v</code></p>
<dd> Stop</p>
<dt><code>x</code></p>
<dd> Play</p>
<dt><code>z</code></p>
<dd> Jump to previuos song</dl>
<h2>FILE BROWSER</h2>
<dl>
<dt><code>Enter</code></p>
<dd> Will either add the current selection if it is a file, or change directories if it is a directory.</p>
<dt><code>a or A</code></p>
<dd> Will add selected file or directory to the playlist.</p>
<dt><code>q or Esc</code></p>
<dd> Exit back to the main playlist window.</dl>
<h2>CONFIGURATION FILES</h2>
<dl>
<dt><code>/etc/audtty.conf</code></p>
<dd> Global configuration file.</p>
<dt><code>$HOME/.audtty.conf</code></p>
<dd> Local configuration file, specific for each user. Can be used to override the global options.</dl>
<p> The syntax of the configuration files are long options without the &#8216;&#8211;&#8216;, one on each line.</p>
<dl>
<dt><code>Example:</code></p>
<dd> numbers<br />
 title<br />
 length no-read-all</dl>
<h2>BUGS</h2>
<p> The xmms remote controlling library provides no good way of detecting changes in the playlist, and therefore <code>audtty</code> might need to be told to reload the playlist if songs are moved. Do so by pressing <code>L</code>. If the length of the playlist changes, <code>audtty</code> will assume the playlist has changed and reload the entire playlist to make sure it is correct. </p>
<p> Probably lots more. </p>
<p> Report bugs at <a rel="nofollow" href="http://bugs.code-monkeys.org">http://bugs.code-monkeys.org</a></p>
<h2>AUTHORS</h2>
<pre>
See /usr/share/doc/audtty/copyright for the list of authors.
</pre>
<h2>RESOURCES</h2>
<p> The audtty website can be found at &lt;<a rel="nofollow" href="http://audacious-media-player.org/Audtty">http://audacious-media-player.org/Audtty</a>&gt; </p>
<p> This man page was originally written by Knut Auvor Grythe &lt;audtty [at] auvor.no&gt;. Updated by Chris Taylor &lt;chris [at] code-monkeys.org&gt;. </p>
<h2>Index</h2>
