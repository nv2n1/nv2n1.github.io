---
title: "muscand(1)"
name: "muscand"
section: "1"
letter: "m"
url: "/docs/linux/man/1-muscand/"
description: "Muscand – File scanner daemon for Museek"
---

<h2>NAME</h2>
<p> <code>Muscand</code> &#8211; File scanner daemon for Museek</p>
<h2>SYNOPSIS</h2>
<p> <code>muscand</code> [-c &lt;<i>filename</i>&gt;] [&#8211;config &lt;<i>filename</i>&gt;] [-b] [&#8211;buddy] [-l] [&#8211;list] [-h] [&#8211;help] [-v] [&#8211;verbose] [&#8211;no-reload]</p>
<h2>DESCRIPTION</h2>
<p> Muscand is a FAM service that scans paths already configured by <i><a href="/docs/linux/man/1-muscan/">muscan</a></i>(1) or <i><a href="/docs/linux/man/1-musetup/">musetup</a></i>(1). If it detects changes to the paths, it will update the Shares Database it is watching after a few seconds. There are two available shares databases, Normal and Buddies-Only. Buddies-Only is an optional shares database that, if enabled, is only accessable by the users you&#8217;ve chosen as &quot;Buddies&quot;. </p>
<p> Before running muscand, you will need a configured museekd, which can be done with <i><a href="/docs/linux/man/1-musetup/">musetup</a></i>(1) or fI&gt;<a href="/docs/linux/man/1-musetup-gtk/">musetup-gtk</a>(1), and add some shared paths with either of the setup tools or with <i><a href="/docs/linux/man/1-muscan/">muscan</a></i>(1).</p>
<h2>OPTIONS</h2>
<p> Muscand accepts the following options:</p>
<dl>
<dt><code>-c &lt;</code><i>filename</i>&gt;, &#8211;config &lt;<i>filename</i>&gt;</p>
<dd> Use a different config file.</p>
<dt><code>-b, &#8211;buddy</code></p>
<dd> Select Buddy-Only Shares.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display Help, version and exit.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Be verbose while scanning shares.</p>
<dt><code>&#8211;no-reload</code></p>
<dd> Don&#8217;t ask museekd to reload the database</dl>
<h2>EXAMPLE</h2>
<p> To run this program the standard way type: </p>
<p> muscand </p>
<p> Alternativly you use a different config file with: </p>
<p> muscand &#8211;config config.xml </p>
<p> Or, you can watch Buddy-Only shares: </p>
<p> muscand &#8211;buddy </p>
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
<p> <i><a href="/docs/linux/man/1-mucous/">mucous</a></i>(1) <i><a href="/docs/linux/man/1-mulog/">mulog</a></i>(1) <i><a href="/docs/linux/man/1-murmur/">murmur</a></i>(1) <i><a href="/docs/linux/man/1-muscan/">muscan</a></i>(1) <i><a href="/docs/linux/man/1-museekcontrol/">museekcontrol</a></i>(1) <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1) <i><a href="/docs/linux/man/1-museeq/">museeq</a></i>(1) <i><a href="/docs/linux/man/1-musetup/">musetup</a></i>(1) <i><a href="/docs/linux/man/1-musetup-gtk/">musetup-gtk</a></i>(1) </p>
<h2>Index</h2>
