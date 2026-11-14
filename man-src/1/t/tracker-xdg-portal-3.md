---
title: "tracker-xdg-portal-3(1)"
name: "tracker-xdg-portal-3"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-xdg-portal-3/"
description: "tracker-xdg-portal-3 – Portal to Tracker endpoints"
---

<h2 class="name">NAME</h2>
<p> tracker-xdg-portal-3 &#8211; Portal to Tracker endpoints </p>
<h2>SYNOPSIS</h2>
<pre>
tracker-xdg-portal-3 [--version | -v]
</pre>
<h2>DESCRIPTION</h2>
<p> This daemon allows access to Tracker endpoints in a controlled manner. By default access to every service is disallowed, services may be whitelisted through additional policy in the <i>.flatpak-info</i> file. </p>
<p> When whitelisting services, the policy may define specific graph names to allow access to, the <i>default</i> keyword to allow access to the default unnamed graph, or <i>*</i> keyword to allow access to all graphs.</p>
<h2>CONFIGURATION</h2>
<p> When interacting with sandboxed clients, the service expects the following format in the <i>.flatpak-info</i> file: </p>
<dl>
<dt>
<dd>
<pre><code>
[Policy Tracker3] dbus : org.example.SparqlEndpoint1 = graphA;
graphB;
default dbus: org.example.SparqlEndpoint2 = *
</code></pre>
</dl>
<p> This will allow access to the endpoints behind the <code>org.example.SparqlEndpoint1</code> and <code>org.example.SparqlEndpoint2</code> bus names. Only to the <code>graphA</code> and <code>graphB</code> graph IRIs and the default unnamed graph on the first endpoint, and to all graphs in the second. </p>
<p> This policy can be set when building or running the sandboxed application through the &#8211;add-policy option. This can be set via <code>finish-args</code> in the flatpak manifest, specified along the build chain in <code><a href="/docs/linux/man/1-flatpak-build-finish/">flatpak-build-finish</a></code>(1), or modified at start time with <code><a href="/docs/linux/man/1-flatpak-run/">flatpak-run</a></code>(1). For example: </p>
<dl>
<dt>
<dd>
<pre><code>
$ flatpak run-- add - policy = Tracker3.dbus : org.example.SparqlEndpoint1 = graphA;
graphB;
default --add - policy = Tracker3.dbus: org.example.SparqlEndpoint2 = *org.freedesktop.TrackerSandbox
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak-build-finish/">flatpak-build-finish</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-override/">flatpak-override</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-run/">flatpak-run</a></code>(1) </p>
<h2>Index</h2>
