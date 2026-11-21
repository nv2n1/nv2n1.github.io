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
<dt><code>The keys for basic control are as follows:</code></dt>
<dd> +&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;+<br />
 | &lt;&lt; &gt; || o &gt;&gt; |<br />
 +&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;+ </dd>
<p>&nbsp;<wbr>z&nbsp;<wbr>&nbsp;<wbr>x&nbsp;<wbr>&nbsp;<wbr>c&nbsp;<wbr>&nbsp;<wbr>v&nbsp;<wbr>&nbsp;<wbr>b</p>
<dt><code>-a, &#8211;read-all</code></dt>
<dd> Read all titles and lengths on startup (EXTREMELY SLOW) (default off).</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print help message.</dd>
<dt><code>-l, &#8211;length</code></dt>
<dd> Show length of track in playlist (SLOW) (default on).</dd>
<dt><code>-n, &#8211;numbers</code></dt>
<dd> Show numbers in playlist (default on).</dd>
<dt><code>-t, &#8211;title</code></dt>
<dd> Read the title from ID3/ogg-tags (SLOW) (default on).</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Display version information.</dd></dl>
<p> Tip: Things going slow? Try <code>audtty -ntl</code></p>
<h2>KEYS</h2>
<dl>
<dt><code>Arrow right/left</code></dt>
<dd> Skip forward/backward 5 seconds.</dd>
<dt><code>Arrow up/down</code></dt>
<dd> Move up/down in the playlist or search results.</dd>
<dt><code>Page up/down</code></dt>
<dd> Scroll up/down one page in the playlist or search results.</dd>
<dt><code>Enter</code></dt>
<dd> Select and play file.</dd>
<dt><code>Esc</code></dt>
<dd> Exit from application, or, if in other dialog, go to main view.</dd>
<dt><code>0 or +</code></dt>
<dd> Increase volume.</dd>
<dt><code>9 or &#8211;</code></dt>
<dd> Decrease volume.</dd>
<dt><code>a</code></dt>
<dd> Open a file browser window.</dd>
<dt><code>b</code></dt>
<dd> Jump to next song.</dd>
<dt><code>c</code></dt>
<dd> Pause.</dd>
<dt><code>d</code></dt>
<dd> Remove currently selected item from playlist.</dd>
<dt><code>j</code></dt>
<dd> Search for file to jump to.</dd>
<dt><code>L</code></dt>
<dd> Add URI to playlist.</dd>
<dt><code>q</code></dt>
<dd> Exit from application.</dd>
<dt><code>R</code></dt>
<dd> Reload playlist.</dd>
<dt><code>u</code></dt>
<dd> Save playlist.</dd>
<dt><code>v</code></dt>
<dd> Stop</dd>
<dt><code>x</code></dt>
<dd> Play</dd>
<dt><code>z</code></dt>
<dd> Jump to previuos song</dd></dl>
<h2>FILE BROWSER</h2>
<dl>
<dt><code>Enter</code></dt>
<dd> Will either add the current selection if it is a file, or change directories if it is a directory.</dd>
<dt><code>a or A</code></dt>
<dd> Will add selected file or directory to the playlist.</dd>
<dt><code>q or Esc</code></dt>
<dd> Exit back to the main playlist window.</dd></dl>
<h2>CONFIGURATION FILES</h2>
<dl>
<dt><code>/etc/audtty.conf</code></dt>
<dd> Global configuration file.</dd>
<dt><code>$HOME/.audtty.conf</code></dt>
<dd> Local configuration file, specific for each user. Can be used to override the global options.</dd></dl>
<p> The syntax of the configuration files are long options without the &#8216;&#8211;&#8216;, one on each line.</p>
<dl>
<dt><code>Example:</code></dt>
<dd> numbers<br />
 title<br />
 length no-read-all</dd></dl>
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
