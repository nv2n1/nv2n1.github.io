---
title: "update-java-alternatives(8)"
name: "update-java-alternatives"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-java-alternatives/"
description: "update-java-alternatives – update alternatives for jre/sdk installations"
---

<p>update-java-alternatives &#8211; update alternatives for jre/sdk installations</p>
<h2>Synopsis</h2>
<p><code>update-java-alternatives [&#8211;jre] [&#8211;plugin] [-v|&#8211;verbose]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-l|&#8211;list&nbsp;[&lt;jname&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-s|&#8211;set&nbsp;&lt;jname&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-a|&#8211;auto<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-h|-?|&#8211;help</p>
<h2>Description</h2>
<p>update-java-alternatives updates all alternatives belonging to one runtime or development kit for the Java language. A package does provide these information of it&#8217;s alternatives in /usr/lib/jvm/.&lt;jname&gt;.jinfo.</p>
<h2>Options</h2>
<dl>
<dt><code>-l|&#8211;list [&lt;jname&gt;]</code></p>
<dd>List all installed packages (or just &lt;jname&gt;) providing information to set a bunch of java alternatives. Verbose output shows each alternative provided by the packages.</p>
<dt><code>-a|&#8211;auto</code></p>
<dd>Switch all alternatives of registered jre/sdk installations to automatic mode.</p>
<dt><code>-s|&#8211;set &lt;jname&gt;</code></p>
<dd>Set all alternatives of the registered jre/sdk installation to the program path provided by the &lt;jname&gt; installation.</p>
<dt><code>&#8211;jre</code></p>
<dd>Limit the actions to alternatives belong to a runtime environment, not a development kit.</p>
<dt><code>&#8211;jre-headless</code></p>
<dd>Limit the actions to alternatives belong to the headless part of a runtime environment.</p>
<dt><code>&#8211;plugin</code></p>
<dd>Limit the actions to alternatives providing browser plugins.</p>
<dt><code>-h|&#8211;help</code></p>
<dd>Display a help message.</p>
<dt><code>-v|&#8211;verbose</code></p>
<dd>Verbose output. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/jvm/.*.jinfo</i></p>
<dd>A text file describing a jre/sdk installation. Consists of some variables of the form &lt;var&gt;=&lt;value&gt; and a list of alternatives of the form jre|jdk &lt;name&gt; &lt;path&gt;. </p>
</dl>
<h2>Author</h2>
<p>update-java-alternatives and this manual page was written by Matthias Klose &lt;doko [at] ubuntu.com&gt;.</p>
