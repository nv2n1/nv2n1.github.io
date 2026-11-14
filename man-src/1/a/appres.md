---
title: "appres(1)"
name: "appres"
section: "1"
letter: "a"
url: "/docs/linux/man/1-appres/"
description: "appres – list X application resource database"
---

<h2 class="name">NAME</h2>
<p> appres &#8211; list X application resource database </p>
<h2>SYNOPSIS</h2>
<p> <code>appres</code> [class [instance]] [-1] [-V] [toolkitoptions]</p>
<h2>DESCRIPTION</h2>
<p> The <i>appres</i> program prints the resources seen by an application (or subhierarchy of an application) with the specified <i>class</i> and <i>instance</i> names. It can be used to determine which resources a particular program will load. For example, </p>
<pre>
% appres  XTerm
</pre>
<p> will list the resources that any <i>xterm</i> program will load. If no application class is specified, the class <i>-AppResTest-</i> is used. </p>
<p> To match a particular instance name, specify an instance name explicitly after the class name, or use the normal Xt toolkit option. For example, </p>
<pre>
% appres  XTerm  myxterm
</pre>
<p> or </p>
<pre>
% appres  XTerm  -name  myxterm
</pre>
<p> To list resources that match a subhierarchy of an application, specify hierarchical class and instance names. The number of class and instance components must be equal, and the instance name should not be specified with a toolkit option. For example, </p>
<pre>
% appres  Xman.TopLevelShell.Form  xman.topBox.form
</pre>
<p> will list the resources of widgets of <i>xman</i> topBox hierarchy. To list just the resources matching a specific level in the hierarchy, use the -1 option. For example, </p>
<pre>
% appres  XTerm.VT100  xterm.vt100  -1
</pre>
<p> will list the resources matching the <i>xterm</i> vt100 widget. </p>
<p> The -V option prints the appres command version and exits.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1), <a href="/docs/linux/man/1-listres/">listres</a>(1)</p>
<h2>AUTHOR</h2>
<p> Jim Fulton, MIT X Consortium </p>
<h2>Index</h2>
