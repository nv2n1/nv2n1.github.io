---
title: "removing-npm(1)"
name: "removing-npm"
section: "1"
letter: "r"
url: "/docs/linux/man/1-removing-npm/"
description: "npm-removal – Cleaning the Slate"
---

<h2 class="name">NAME</h2>
<p> <code>npm-removal</code> &#8211; Cleaning the Slate </p>
<h2>SYNOPSIS</h2>
<p> So sad to see you go.</p>
<dl>
<dt>
<dd>
<pre>
sudo npm uninstall npm -g
</pre>
<dt>
<dd></dl>
<p> Or, if that fails, get the npm source code, and do:</p>
<dl>
<dt>
<dd>
<pre>
sudo make uninstall
</pre>
<dt>
<dd></dl>
<h2>More Severe Uninstalling</h2>
<p> Usually, the above instructions are sufficient. That will remove npm, but leave behind anything you&#8217;ve installed. </p>
<p> If that doesn&#8217;t work, or if you require more drastic measures, continue reading. </p>
<p> Note that this is only necessary for globally-installed packages. Local installs are completely contained within a project&#8217;s <code>node_modules</code> folder. Delete that folder, and everything is gone (unless a package&#8217;s install script is particularly ill-behaved). </p>
<p> This assumes that you installed node and npm in the default place. If you configured node with a different <code>&#8211;prefix</code>, or installed npm with a different prefix setting, then adjust the paths accordingly, replacing <code>/usr/local</code> with your install prefix. </p>
<p> To remove everything npm-related manually:</p>
<dl>
<dt>
<dd>
<pre><code>
rm - rf / usr / local / {lib / node{, /.npm, _modules}, bin, share / man} / npm *
</code></pre>
<dt>
<dd></dl>
<p> If you installed things <i>with</i> npm, then your best bet is to uninstall them with npm first, and then install them again once you have a proper install. This can help find any symlinks that are lying around:</p>
<dl>
<dt>
<dd>
ls &#8211; laF / usr / local / {lib / node{, /.npm}, bin, share / man} | grep npm</p>
<dt>
<dd></dl>
<p> Prior to version 0.3, npm used shim files for executables and node modules. To track those down, you can do the following:</p>
<dl>
<dt>
<dd>
<pre><code>
find / usr / local / {lib / node, bin} - exec grep - l npm \
{
    \
}
\;
;
</code></pre>
<dt>
<dd></dl>
<p> (This is also in the README file.)</p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> README</p>
<dt>&bull;</p>
<dd> npm help uninstall</p>
<dt>&bull;</p>
<dd> npm help prune</p>
<dt>
<dd>
</dl>
<h2>Index</h2>
