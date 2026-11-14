---
title: "wicd-curses(8)"
name: "wicd-curses"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wicd-curses/"
description: "wicd-curses – curses-based wicd(8) controller"
---

<p><code>wicd-curses</code> &#8211; curses-based <a href="/docs/linux/man/8-wicd/">wicd</a>(8) controller</p>
<h2>Description</h2>
<p>wicd-curses is a curses-based network controller that uses the Wired/Wireless Internet Connection Daemon (wicd) to control your network connections. It is suitable to run in terminal multiplexers like <a href="/docs/linux/man/1-screen/">screen</a>(1). </p>
<p> It is designed to imitate the GTK-based <a href="/docs/linux/man/1-wicd-client/">wicd-client</a>(1) as much as possible, and uses the Urwid (<a rel="nofollow" href="http://excess.org/urwid)">http://excess.org/urwid)</a> console widget library to vastly simplify development. </p>
<p> This man page only documents the current status of wicd-curses. This may/may not be the most up-to-date document.</p>
<h2>Controls</h2>
<p>All of these are case sensitive.</p>
<dl>
<dt><code>C </code>or<code> enter</code></p>
<dd>Connect to selected network</p>
<dt><code>F8 </code>or<code> Q </code>or<code> q</code></p>
<dd>Quit the client.</p>
<dt><code>D</code></p>
<dd>Disconnect all devices from network connections</p>
<dt><code>ESC</code></p>
<dd>If connecting to a network, stop doing so</p>
<dt><code>F5 </code>or<code> R</code></p>
<dd>Refresh the network list</p>
<dt><code>P</code></p>
<dd>Bring up the preferences controller</p>
<dt><code>I</code></p>
<dd>Bring up hidden network scanning dialog</p>
<dt><code>H </code>or<code> h </code>or<code> ?</code></p>
<dd>Bring up a rather simplistic help dialog. Of course, it mentions this man page first. :-)</p>
<dt><code>A</code></p>
<dd>Raise the &quot;About wicd-curses&quot; dialog</p>
<dt><code>right-arrow</code></p>
<dd>Bring up network configuration controller for the selected network</p>
<dt><code>delete</code></p>
<dd>Delete the selected wired network profile (from the wired network combo box at the top)</p>
<dt><code>F2</code></p>
<dd>Rename the selected wired network profile (from the wired network combo box at the top)</p>
<dt><code>S</code></p>
<dd>Bring up instructions on how to edit the scripts. I have implemented a way to do this in the interface itself, but making it function with all Linux distros would be difficult. Since you are reading this, you should know how to do what I suggest. ;-)</p>
<dt><code>O</code></p>
<dd>Raise the Ad-Hoc network creation dialog </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-wicd-client/">wicd-client</a></code>(1), <code><a href="/docs/linux/man/8-wicd/">wicd</a></code>(8) </p>
<h2>Bugs</h2>
<p>Probably lots. ;-) If you happen to find one, ask about it on #wicd on freenode, or submit a bug report to <a rel="nofollow" href="http://launchpad.net/wicd.">http://launchpad.net/wicd.</a> </p>
<h2>Wicd-Curses Author</h2>
<p>Andrew Psaltis &lt;ampsaltis [at] gmail.com&gt;</p>
<h2>Wicd Authors</h2>
<p>Adam Blackburn &lt;compwiz18 [at] gmail.com&gt;<br />
 Dan O&#8217;Reilly &lt;oreilldf [at] gmail.com&gt;<br />
 David Paleino &lt;d.paleino [at] gmail.com&gt;</p>
