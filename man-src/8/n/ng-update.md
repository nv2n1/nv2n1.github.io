---
title: "ng-update(8)"
name: "ng-update"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ng-update/"
description: "ng-update – Initng runlevel configuration tool."
---

<p>ng-update &#8211; Initng runlevel configuration tool.</p>
<h2>Synopsis</h2>
<p><code>ng-update</code> <i>a</i>|<i>add</i> <i>script1</i> [<i>script2</i> <i>&#8230;</i>] [<i>runlevel1</i>] [<i>runlevel2 &#8230;</i>]<br />
 <code>ng-update</code> <i>d</i>|<i>del</i>|<i>delete</i> <i>script1</i> [<i>script2 &#8230;</i>] [<i>runlevel1</i>] [<i>runlevel2 &#8230;</i>]<br />
 <code>ng-update</code> <i>s</i>|<i>show</i>|<i>view</i> [<i>script</i>] [<i>runlevel</i>]</p>
<h2>Description</h2>
<p>ng-update allows you to control/show which services are started by initng. Yo can add and delete services to/from different runlevels. To find out which services are available take a look at /etc/initng/[daemon|net|system].</p>
<h2>Options</h2>
<dl>
<dt><code>a, add</code></p>
<dd>Add one or more scripts to one or more runlevels. If runlevel is left blank the script will be added to every runlevel.</p>
<dt><code>d, del</code></p>
<dd>Delete one or more scripts from one or more runlevels. If runlevel is left blank the script will be deleted from every runlevel.</p>
<dt><code>s, show, view</code></p>
<dd>Shows the scripts started in the passed runlevel(s).</p>
<dt><code>script</code></p>
<dd>A script found in /etc/initng/[daemon|net|system] which should be added/removed.<br />
 The form is [daemon|net|system]/script_without_i. Take a look in the examples section.</p>
<dt><code>runlevel</code></p>
<dd>The runlevel the script(s) should be added to/deleted from. Normally this should be <i>&quot;default&quot;</i>, some times <i>&quot;system&quot;</i>.<br />
 Take a look at <i>/etc/initng/*.runlevel</i></dl>
<h2>Examples</h2>
<p>Use <code>ng-update add system/alsasound default</code> to add <i>alsasound</i> to the runlevel default.<br />
 Use <code>ng-update del system/alsasound</code> to remove <i>alsasound</i> from every runlevel.<br />
 Use <code>ng-update del system/alsasound default</code> to remove alsasound from the runlevel default.<br />
 Use <code>ng-update show</code> to show <i>all</i> available services and their runlevel (if existing).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-initng/">initng</a>(8)</code> <code><a href="/docs/linux/man/8-ngc/">ngc</a>(8),</code> <code><a href="/docs/linux/man/8-ngdc/">ngdc</a>(8),</code> <code><a href="/docs/linux/man/8-gen_system_runlevel/">gen_system_runlevel</a>(8),</code> <code><a href="/docs/linux/man/8-install_service/">install_service</a>(8),</code> <code><a href="/docs/linux/man/8-system_off/">system_off</a>(8).</code></p>
<h2>Author</h2>
<p>initng was written by Jimmy Wennlund &lt;jimmy.wennlund [at] gmail.com&gt; and can be found at <a rel="nofollow" href="http://www.initng.org/.">http://www.initng.org/.</a> </p>
<p> This manual page was written by Armin Berres &lt;a.berres [at] onlinehome.de&gt;.</p>
