---
title: "muscan(1)"
name: "muscan"
section: "1"
letter: "m"
url: "/docs/linux/man/1-muscan/"
description: "Muscan – File scanner for Museek"
---

<h2>NAME</h2>
<p> <code>Muscan</code> &#8211; File scanner for Museek</p>
<h2>SYNOPSIS</h2>
<p> <code>muscan</code> [-c &lt;<i>filename</i>&gt;] [&#8211;config &lt;<i>filename</i>&gt;] [-b] [&#8211;buddy] [-v] [&#8211;verbose] [-r] [&#8211;rescan] [-n] [&#8211;noscan] [-s &lt;<i>directory</i>&gt;] [&#8211;share &lt;<i>directory</i>&gt;] [-u &lt;<i>directory</i>&gt;] [&#8211;unshare &lt;<i>directory</i>&gt;] [-l] [&#8211;list] [-h] [&#8211;help]</p>
<h2>DESCRIPTION</h2>
<p> Muscan scans paths &amp; files to be shared by <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1). It creates a database of files, with meta-data for MP3 and OGG Vorbis files, if Vorbis support was compiled in. There are two available shares databases, Normal and Buddies-Only. Buddies-Only is an optional shares database that, if enabled, is only accessable by the users you&#8217;ve chosen as &quot;Buddies&quot;. </p>
<p> Before running muscan, you will need a configured museekd, which can be done with <i><a href="/docs/linux/man/1-musetup/">musetup</a></i>(1) or fI&gt;<a href="/docs/linux/man/1-musetup-gtk/">musetup-gtk</a>(1), and add some shared paths with either of the setup tools or with <i><a href="/docs/linux/man/1-muscan/">muscan</a></i>(1).</p>
<h2>OPTIONS</h2>
<p> Muscan accepts the following options:</p>
<dl>
<dt><code>-c &lt;</code><i>filename</i>&gt;, &#8211;config &lt;<i>filename</i>&gt;</p>
<dd> Use a different config file.</p>
<dt><code>-b, &#8211;buddy</code></p>
<dd> Select Buddy-Only Shares.</p>
<dt><code>-s &lt;</code><i>directory</i>&gt;, &#8211;share &lt;<i>directory</i>&gt;</p>
<dd> Add directory to shares.</p>
<dt><code>-u &lt;</code><i>directory</i>&gt;, &#8211;unshare &lt;<i>directory</i>&gt;</p>
<dd> Remove directory from shares.</p>
<dt><code>-r, &#8211;rescan</code></p>
<dd> Rescan shares.</p>
<dt><code>-n, &#8211;noscan</code></p>
<dd> Do not rescan shares.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Be verbose while scanning shares.</p>
<dt><code>-l, &#8211;list</code></p>
<dd> Display list of shared directories.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display Help, version and exit.</dl>
<h2>EXAMPLE</h2>
<p> To run a quick shares update, run: </p>
<p> <code>muscan</code> or <code>muscan -b</code> </p>
<p> To rescan everything, run: </p>
<p> <code>muscan -r</code> or <code>muscan -b -r</code> </p>
<p> Alternatively you use a different config file with: </p>
<p> <code>muscan &#8211;config config.xml</code> </p>
<h2>FILES</h2>
<dl>
<dt>
&nbsp;<wbr><i>~/.museekd/config.xml</i></p>
<dd> The default location for the <code>museekd</code> config file.</p>
<dt>
&nbsp;<wbr><i>~/.museekd/config.shares</i></p>
<dd> The default location for the Normal shares database.</p>
<dt>
&nbsp;<wbr><i>~/.museekd/config.shares.state</i></p>
<dd> The default location for the active Normal shares database.</p>
<dt>
&nbsp;<wbr><i>~/.museekd/config.buddyshares</i></p>
<dd> The default location for the Buddy shares database.</p>
<dt>
&nbsp;<wbr><i>~/.museekd/config.buddyshares.state</i></p>
<dd> The default location for the active Buddy shares database&#8217;s.</dl>
<h2>AUTHORS</h2>
<p> Hyriand &lt;hyriand [at] thegraveyard.org&gt; </p>
<p> daelstorm &lt;daelstorm [at] gmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mucous/">mucous</a></i>(1) <i><a href="/docs/linux/man/1-mulog/">mulog</a></i>(1) <i><a href="/docs/linux/man/1-murmur/">murmur</a></i>(1) <i><a href="/docs/linux/man/1-muscand/">muscand</a></i>(1) <i><a href="/docs/linux/man/1-museekcontrol/">museekcontrol</a></i>(1) <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1) <i><a href="/docs/linux/man/1-museeq/">museeq</a></i>(1) <i><a href="/docs/linux/man/1-musetup/">musetup</a></i>(1) <i><a href="/docs/linux/man/1-musetup-gtk/">musetup-gtk</a></i>(1) </p>
<h2>Index</h2>
