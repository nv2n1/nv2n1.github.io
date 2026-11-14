---
title: "josm(1)"
name: "josm"
section: "1"
letter: "j"
url: "/docs/linux/man/1-josm/"
description: "josm – Java OpenStreetMap Editor"
---

<h2 class="name">NAME</h2>
<p> josm &#8211; Java OpenStreetMap Editor </p>
<h2>SYNOPSIS</h2>
<p> <code>josm</code></p>
<h2>DESCRIPTION</h2>
<p> <code>JOSM </code> is an editor for OpenStreetMap written in Java 7. </p>
<p> <code>OpenStreetMap </code> is a project aimed squarely at creating and providing free geographic data such as street maps to anyone who wants them. It allows you to view, edit and use geographical data in a collaborative way from anywhere on earth. The project was started because most maps you think of as free actually have legal or technical restrictions on their use, holding back people from using them in creative, productive or unexpected ways.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, -?, &#8211;help</code></p>
<dd> Show help</p>
<dt><code>&#8211;geometry=&lt;width&gt;x&lt;height&gt;(+|-)x(+|-)y</code></p>
<dd> Standard X geometry argument</p>
<dt><code>[&#8211;download=]minlat,minlon,maxlat,maxlon</code></p>
<dd> Download the bounding box</p>
<dt><code>[&#8211;download=]&lt;url&gt;</code></p>
<dd> Download the location at the url (with lat=x&amp;lon=y&amp;zoom=z)</p>
<dt><code>[&#8211;download=]&lt;filename&gt;</code></p>
<dd> Open file (any file type that can be opened with File/Open)</p>
<dt><code>&#8211;downloadgps=minlat,minlon,maxlat,maxlon</code></p>
<dd> Download the bounding box as raw gps</p>
<dt><code>&#8211;selection=&lt;searchstring&gt;</code></p>
<dd> Select with the given search</p>
<dt><code>&#8211;[no-]maximize</code></p>
<dd> Do [not] launch in maximized mode</p>
<dt><code>&#8211;reset-preferences</code></p>
<dd> Reset the preferences to the default</p>
<dt><code>&#8211;load-preferences=&lt;url-to-xml&gt;</code></p>
<dd> Change preferences according to the XML file</p>
<dt><code>&#8211;set=&lt;key&gt;=&lt;value&gt;</code></p>
<dd> Set preference key to value</p>
<dt><code>&#8211;language=&lt;language&gt;</code></p>
<dd> Set the language</p>
<dt><code>&#8211;version</code></p>
<dd> Display the JOSM version</p>
<dt><code>&#8211;debug</code></p>
<dd> Print debugging messages to console</p>
<dt><code>&#8211;offline=&lt;osm_api|josm_website|all&gt;</code></p>
<dd> Disable access to the given resource(s), separated by comma</dl>
<h2>JAVA PROPERTIES</h2>
<p> The following options can be set by using Java system properties (i.e. -Dkey=value passed to java, or specified inside JAVA_OPTS).</p>
<dl>
<dt><code>josm.pref=&lt;path&gt;</code></p>
<dd> Set the JOSM preferences directory.</p>
<dt><code>josm.userdata=&lt;path&gt;</code></p>
<dd> Set the JOSM user data directory.</p>
<dt><code>josm.cache=&lt;path&gt;</code></p>
<dd> Set the JOSM cache directory.</p>
<dt><code>josm.home=&lt;homedir&gt;</code></p>
<dd> Relocate all 3 directories to homedir. Cache directory will be in homedir/cache. Default is ~/.josm/.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>JAVA_HOME</p>
<dd> Specify an alternate Java environment.</p>
<dt>JAVA_OPTS</p>
<dd> Specify Java options. For example, to use a HTTP proxy server with this program, set this environment variable to something like <i>JAVA_OPTS=-Dhttp.proxyHost=yourProxyURL</i> before starting josm.</dl>
<h2>AUTHOR</h2>
<p> JOSM was originally designed and coded by Immanuel Scholz, and is now maintained by the OpenStreetMap community. </p>
<p> The current JOSM maintainer is Dirk Stöcker. A lot of administration work is done by Paul Hartmann and Vincent Privat. </p>
<p> Major code contributions from (in alphabetical order): </p>
<p> Stefan Breunig David Earl Gabriel Ebner Dave Hansen Paul Hartmann Karl Guggisberg Matthias Julius Alexei Kasatkin Jiri Klement Ulf Lamping Simon Legner Raphael Mack Upliner Mikhalych Vincent Privat Frederik Ramm Dirk Stöcker </p>
<p> Many minor contributions and patches by others; see SVN history at <a rel="nofollow" href="http://josm.openstreetmap.de/svn/">http://josm.openstreetmap.de/svn/</a> for details. Use &quot;josm-dev AT openstreetmap.org&quot; to contact still active authors. The logo has been designed by Ilya Palikov. </p>
<p> This manual page was initially written by Andreas Putzo &lt;andreas [at] putzo.net&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
