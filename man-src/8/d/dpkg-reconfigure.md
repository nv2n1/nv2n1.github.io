---
title: "dpkg-reconfigure(8)"
name: "dpkg-reconfigure"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dpkg-reconfigure/"
description: "dpkg-reconfigure – reconfigure an already installed package"
---

<p>dpkg-reconfigure &#8211; reconfigure an already installed package</p>
<h2>Synopsis</h2>
<pre> dpkg-reconfigure [options] packages</pre>
<h2>Description</h2>
<p><code>dpkg-reconfigure</code> reconfigures packages after they have already been installed. Pass it the names of a package or packages to reconfigure. It will ask configuration questions, much like when the package was first installed. </p>
<p> If you just want to see the current configuration of a package, see <code><a href="/docs/linux/man/1-debconf-show/">debconf-show</a></code>(1) instead.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code><i>type</i>, <code>&#8211;frontend=</code><i>type</i></p>
<dd>Select the frontend to use. The default frontend can be permanently changed by: </p>
<pre> dpkg-reconfigure debconf</pre>
<p>Note that if you normally have debconf set to use the noninteractive frontend, dpkg-reconfigure will use the dialog frontend instead, so you actually get to reconfigure the package.</p>
<dt><code>-p</code><i>value</i>, <code>&#8211;priority=</code><i>value</i></p>
<dd>Specify the minimum priority of question that will be displayed. dpkg-reconfigure normally shows low priority questions no matter what your default priority is. See <code><a href="/docs/linux/man/7-debconf/">debconf</a></code>(7) for a list.</p>
<dt><code>&#8211;default-priority</code></p>
<dd>Use whatever the default priority of question is, instead of forcing the priority to low.</p>
<dt><code>-u</code>, <code>&#8211;unseen-only</code></p>
<dd>By default, all questions are shown, even if they have already been answered. If this parameter is set though, only questions that have not yet been seen will be asked.</p>
<dt><code>&#8211;force</code></p>
<dd>Force dpkg-reconfigure to reconfigure a package even if the package is in an inconsistent or broken state. Use with caution.</p>
<dt><code>&#8211;no-reload</code></p>
<dd>Prevent dpkg-reconfigure from reloading templates. Use with caution; this will prevent dpkg-reconfigure from repairing broken templates databases. However, it may be useful in constrained environments where rewriting the templates database is expensive.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display usage help.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-debconf/">debconf</a></code>(7)</p>
<h2>Author</h2>
<p>Joey Hess &lt;joeyh [at] debian.org&gt;</p>
