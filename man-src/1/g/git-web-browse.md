---
title: "git-web-browse(1)"
name: "git-web-browse"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-web-browse/"
description: "git-web–browse – Git helper script to launch a web browser"
---

<p>git-web&#8211;browse &#8211; Git helper script to launch a web browser </p>
<h2>Synopsis</h2>
<pre><i>git web--browse</i> [&lt;options&gt;] &lt;url|file&gt;...</pre>
<h2>Description</h2>
<p>This script tries, as much as possible, to display the URLs and FILEs that are passed as arguments, as HTML pages in new tabs on an already opened web browser. </p>
<p> The following browsers (or commands) are currently supported: </p>
<dl>
<dd>&bull; firefox (this is the default under X Window when not using KDE)</dl>
<dl>
<dd>&bull; iceweasel</dl>
<dl>
<dd>&bull; seamonkey</dl>
<dl>
<dd>&bull; iceape</dl>
<dl>
<dd>&bull; chromium (also supported as chromium-browser)</dl>
<dl>
<dd>&bull; google-chrome (also supported as chrome)</dl>
<dl>
<dd>&bull; konqueror (this is the default under KDE, see <i>Note about konqueror</i> below)</dl>
<dl>
<dd>&bull; opera</dl>
<dl>
<dd>&bull; w3m (this is the default outside graphical environments)</dl>
<dl>
<dd>&bull; elinks</dl>
<dl>
<dd>&bull; links</dl>
<dl>
<dd>&bull; lynx</dl>
<dl>
<dd>&bull; dillo</dl>
<dl>
<dd>&bull; open (this is the default under Mac OS X GUI)</dl>
<dl>
<dd>&bull; start (this is the default under MinGW)</dl>
<dl>
<dd>&bull; cygstart (this is the default under Cygwin)</dl>
<dl>
<dd>&bull; xdg-open</dl>
<p> Custom commands may also be specified.</p>
<h2>Options</h2>
<p>-b &lt;browser&gt;, &#8211;browser=&lt;browser&gt;</p>
<dl>
<dd>Use the specified browser. It must be in the list of supported browsers.</dl>
<p> -t &lt;browser&gt;, &#8211;tool=&lt;browser&gt;</p>
<dl>
<dd>Same as above.</dl>
<p> -c &lt;conf.var&gt;, &#8211;config=&lt;conf.var&gt;</p>
<dl>
<dd>CONF.VAR is looked up in the Git config files. If it&#8217;s set, then its value specifies the browser that should be used.</dl>
<h2>Configuration Variables</h2>
<h3>CONF.VAR (from -c option) and web.browser</h3>
<p>The web browser can be specified using a configuration variable passed with the -c (or &#8211;config) command-line option, or the <code>web.browser</code> configuration variable if the former is not used.</p>
<h3>browser.&lt;tool&gt;.path</h3>
<p>You can explicitly provide a full path to your preferred browser by setting the configuration variable <code>browser.&lt;tool&gt;.path</code>. For example, you can configure the absolute path to firefox by setting <i>browser.firefox.path</i>. Otherwise, <i>git web&#8211;browse</i> assumes the tool is available in PATH.</p>
<h3>browser.&lt;tool&gt;.cmd</h3>
<p>When the browser, specified by options or configuration variables, is not among the supported ones, then the corresponding <code>browser.&lt;tool&gt;.cmd</code> configuration variable will be looked up. If this variable exists then <i>git web&#8211;browse</i> will treat the specified tool as a custom command and will use a shell eval to run the command with the URLs passed as arguments.</p>
<h2>Note About Konqueror</h2>
<p>When <i>konqueror</i> is specified by a command-line option or a configuration variable, we launch <i>kfmclient</i> to try to open the HTML man page on an already opened konqueror in a new tab if possible. </p>
<p> For consistency, we also try such a trick if <i>browser.konqueror.path</i> is set to something like <code>A_PATH_TO/konqueror</code>. That means we will try to launch <code>A_PATH_TO/kfmclient</code> instead. </p>
<p> If you really want to use <i>konqueror</i>, then you can use something like the following: </p>
<dl>
<dd>
<pre> [web]
 browser = konq
 [browser &quot;konq&quot;]
 cmd = A_PATH_TO/konqueror</pre>
</dl>
<h3>Note about git-config &#8211;global</h3>
<p>Note that these configuration variables should probably be set using the <code>&#8211;global</code> flag, for example like this: </p>
<dl>
<dd>
<pre>$ git config --global web.browser firefox</pre>
</dl>
<p> as they are probably more user specific than repository specific. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for more information about this.</p>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
