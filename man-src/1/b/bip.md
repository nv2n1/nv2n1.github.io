---
title: "bip(1)"
name: "bip"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bip/"
description: "bip – BIP IRC Proxy"
---

<h2>SYNOPSIS</h2>
<p> <code>bip</code> [ <code>-f</code> <i>config_file</i> ] [ <code>-n</code> ] [ <code>-h</code> ] </p>
<h2>DESCRIPTION</h2>
<p> BIP is an IRC Proxy </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code></dt>
<dd> Don&#8217;t daemonize. Log into stderr. </dd>
<dt><code>-f</code> config_file</dt>
<dd> Use config_file as the configuration file. If no config file is given, bip will try to open ~/.bip/bip.conf. </dd>
<dt><code>-s</code> homedir</dt>
<dd> Set bip home directory to homedir instead of $HOME/.bip. </dd>
<dt><code>-h</code></dt>
<dd> Help. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> bip.conf </p>
<h2>AUTHOR</h2>
<p> Arnaud &#8216;nohar&#8217; Cornet Loïc &#8216;Kyoshiro&#8217; Gomez </p>
<p> Thanks to jj, YS and lafouine, for hanging around while we were coding. </p>
<p> Crypto shamelessly taken from Christophe &#8216;sexy&#8217; Devine. </p>
