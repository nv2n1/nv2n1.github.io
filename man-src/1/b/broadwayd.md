---
title: "broadwayd(1)"
name: "broadwayd"
section: "1"
letter: "b"
url: "/docs/linux/man/1-broadwayd/"
description: "broadwayd – Broadway display server"
---

<h2 class="name">NAME</h2>
<p> broadwayd &#8211; Broadway display server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>broadwayd</code> [&#8211;port&nbsp;<i>PORT</i>] [&#8211;address&nbsp;<i>ADDRESS</i>] [&#8211;unixsocket&nbsp;<i>ADDRESS</i>] [<i>:DISPLAY</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>broadwayd</code></p>
<dd>is a display server for the Broadway GDK backend. It allows multiple GTK+ applications to display their windows in the same web browser, by connecting to broadwayd. </p>
<p> When using broadwayd, specify the display number to use, prefixed with a colon, similar to X. The default display number is 0. </p>
<dl>
<dt>
<dd>
<pre>
broadwayd :5
</pre>
</dl>
<p> Then point your web browser at <a rel="nofollow" href="http://127.0.0.1:8085.">http://127.0.0.1:8085.</a> Start your applications like this: </p>
<dl>
<dt>
<dd>
<pre>
GDK_BACKEND=broadway BROADWAY_DISPLAY=:5 gtk3-demo
</pre>
</dl>
<p> You can add password protection for your session by creating a file in $XDG_CONFIG_HOME/broadway.passwd or $HOME/.config/broadway.passwd with a <a href="/docs/linux/man/3-crypt/">crypt</a>(3) style password hash. A simple way to generate it is with openssl: </p>
<dl>
<dt>
<dd>
<pre>
openssl passwd -1  &gt; ~/.config/broadway.passwd
</pre>
</dl>
<h2>OPTIONS</h2>
<p> &#8211;port</p>
<dl>
<dt>
<dd> Use <i>PORT</i> as the HTTP port, instead of the default 8080 + (<i>DISPLAY</i> &#8211; 1).</dl>
<p> &#8211;address</p>
<dl>
<dt>
<dd> Use <i>ADDRESS</i> as the HTTP address, instead of the default <a rel="nofollow" href="http://127.0.0.1:">http://127.0.0.1:</a><i>PORT</i>.</dl>
<p> &#8211;unixsocket</p>
<dl>
<dt>
<dd> Use <i>ADDRESS</i> as the unix domain socket address. This option overrides &#8211;address and &#8211;port. It is available only on Unix-like systems.</dl>
<h2>Index</h2>
