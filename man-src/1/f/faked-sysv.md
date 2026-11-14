---
title: "faked-sysv(1)"
name: "faked-sysv"
section: "1"
letter: "f"
url: "/docs/linux/man/1-faked-sysv/"
description: "faked – daemon that remembers fake ownership/permissions of files manipulated by fakeroot processes."
---

<h2 class="name">NAME</h2>
<p> faked &#8211; daemon that remembers fake ownership/permissions of files manipulated by fakeroot processes. </p>
<h2>SYNOPSIS</h2>
<p> <code>faked</code> <code>[&#8211;debug] [&#8211;foreground] [&#8211;cleanup] [&#8211;key</code> <i>msg-key</i><code>]</code> <code>[&#8211;load] [&#8211;save-file</code> <i>save-file</i><code>]</code> <code>[&#8211;port</code> <i>TCP-port</i><code>]</code></p>
<h2>DESCRIPTION</h2>
<p> If a fakeroot process wants to change the ownership of a file, then <code>faked</code> is the process that remembers that new owner. If later the same fakeroot process does a stat() for that filename, then the libfakeroot wrapped stat() call will first ask faked for the fake ownership etc of that file, and then report it. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;debug</code></p>
<dd> Print debugging information on stderr.</p>
<dt><code>&#8211;foreground</code></p>
<dd> Don&#8217;t fork into the background.</p>
<dt><code>&#8211;cleanup &nbsp;number</code></p>
<dd> Cleanup the semaphores.</p>
<dt><code>&#8211;key &nbsp;key-number</code></p>
<dd> Don&#8217;t allocate a new communication channel, but use channel specified by key. (If the specified channel doesn&#8217;t exist, it&#8217;s created).</p>
<dt><code>&#8211;save-file &nbsp;save-file</code></p>
<dd> Save the environment to save-file on exit.</p>
<dt><code>&#8211;load</code></p>
<dd> Load a previously saved environment from the standard input.</p>
<dt><code>&#8211;unknown-is-real</code></p>
<dd> Use real ownership of previously-unknown files instead of setting them to root:root.</p>
<dt><code>&#8211;port &nbsp;tcp-port</code></p>
<dd> Use TCP port tcp-port. </p>
</dl>
<h2>BUGS</h2>
<p> None so far. Be warned, though: although I&#8217;ve written quite a few much larger (and smaller) programs, I&#8217;ve never written anything that was as tiny as <code>fakeroot</code>, had as many bugs as <code>fakeroot</code>, and still was as usable as, say, <code>fakeroot</code> version 0.0_3, the first version that could be used to build itself.</p>
<h2>COPYING</h2>
<p> <code>fakeroot</code> is distributed under the GNU General Public License. (GPL 2.0 or greater).</p>
<h2>AUTHORS</h2>
<dl>
<dt>joost witteveen</p>
<dd> &lt;<i>joostje [at] debian.org</i>&gt;</p>
<dt>Clint Adams</p>
<dd> &lt;<i>clint [at] debian.org</i>&gt;</p>
<dt>Timo Savola</p>
<dd></dl>
<h2>MANUAL PAGE</h2>
<p> mostly by J.H.M. Dassen &lt;jdassen [at] debian.org&gt; mods/additions by joost and Clint.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fakeroot/">fakeroot</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-buildpackage/">dpkg-buildpackage</a></code>(1), <code><a href="/docs/linux/man/1-debuild/">debuild</a></code>(1) <code>/usr/share/doc/fakeroot/DEBUG</code> </p>
<h2>Index</h2>
