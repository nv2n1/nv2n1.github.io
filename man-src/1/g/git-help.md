---
title: "git-help(1)"
name: "git-help"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-help/"
description: "git-help – Display help information about Git"
---

<h2 class="name">NAME</h2>
<p> git-help &#8211; Display help information about Git </p>
<h2>SYNOPSIS</h2>
<pre><code>
git help[-a | --all[--[no - ] verbose]]
        [[-i | --info][-m | --man][-w | --web]][COMMAND | GUIDE] git help[-g | --guides] git help[-c | --config]
</code></pre>
<h2>DESCRIPTION</h2>
<p> With no options and no COMMAND or GUIDE given, the synopsis of the <i>git</i> command and a list of the most commonly used Git commands are printed on the standard output. </p>
<p> If the option <code>&#8211;all</code> or <code>-a</code> is given, all available commands are printed on the standard output. </p>
<p> If the option <code>&#8211;guides</code> or <code>-g</code> is given, a list of the Git concept guides is also printed on the standard output. </p>
<p> If a command, or a guide, is given, a manual page for that command or guide is brought up. The <i>man</i> program is used by default for this purpose, but this can be overridden by other options or configuration variables. </p>
<p> If an alias is given, git shows the definition of the alias on standard output. To get the manual page for the aliased command, use <code>git COMMAND &#8211;help</code>. </p>
<p> Note that <code>git &#8211;help &#8230;</code> is identical to <code>git help &#8230;</code> because the former is internally converted into the latter. </p>
<p> To display the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) man page, use <code>git help git</code>. </p>
<p> This page can be displayed with <i>git help help</i> or <code>git help &#8211;help</code></p>
<h2>OPTIONS</h2>
<p> -a, &#8211;all</p>
<dl>
<dt>
<dd> Prints all the available commands on the standard output. This option overrides any given command or guide name.</dl>
<p> &#8211;verbose</p>
<dl>
<dt>
<dd> When used with <code>&#8211;all</code> print description for all recognized commands. This is the default.</dl>
<p> -c, &#8211;config</p>
<dl>
<dt>
<dd> List all available configuration variables. This is a short summary of the list in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> -g, &#8211;guides</p>
<dl>
<dt>
<dd> Prints a list of the Git concept guides on the standard output.</dl>
<p> -i, &#8211;info</p>
<dl>
<dt>
<dd> Display manual page for the command in the <i>info</i> format. The <i>info</i> program will be used for that purpose.</dl>
<p> -m, &#8211;man</p>
<dl>
<dt>
<dd> Display manual page for the command in the <i>man</i> format. This option may be used to override a value set in the <code>help.format</code> configuration variable. </p>
<p> By default the <i>man</i> program will be used to display the manual page, but the <code>man.viewer</code> configuration variable may be used to choose other display programs (see below).</dl>
<p> -w, &#8211;web</p>
<dl>
<dt>
<dd> Display manual page for the command in the <i>web</i> (HTML) format. A web browser will be used for that purpose. </p>
<p> The web browser can be specified using the configuration variable <code>help.browser</code>, or <code>web.browser</code> if the former is not set. If none of these config variables is set, the <i>git web&#8211;browse</i> helper script (called by <i>git help</i>) will pick a suitable default. See <code><a href="/docs/linux/man/1-git-web--browse/">git-web&#8211;browse</a></code>(1) for more information about this.</dl>
<h2>CONFIGURATION VARIABLES</h2>
<h3>help.format</h3>
<p> If no command-line option is passed, the <code>help.format</code> configuration variable will be checked. The following values are supported for this variable; they make <i>git help</i> behave as their corresponding command- line option: </p>
<dl>
<dt>
<dd> &bull; &quot;man&quot; corresponds to <i>-m|&#8211;man</i>,</dl>
<dl>
<dt>
<dd> &bull; &quot;info&quot; corresponds to <i>-i|&#8211;info</i>,</dl>
<dl>
<dt>
<dd> &bull; &quot;web&quot; or &quot;html&quot; correspond to <i>-w|&#8211;web</i>.</dl>
<h3>help.browser, web.browser and browser.&lt;tool&gt;.path</h3>
<p> The <code>help.browser</code>, <code>web.browser</code> and <code>browser.&lt;tool&gt;.path</code> will also be checked if the <i>web</i> format is chosen (either by command-line option or configuration variable). See <i>-w|&#8211;web</i> in the OPTIONS section above and <code><a href="/docs/linux/man/1-git-web--browse/">git-web&#8211;browse</a></code>(1).</p>
<h3>man.viewer</h3>
<p> The <code>man.viewer</code> configuration variable will be checked if the <i>man</i> format is chosen. The following values are currently supported: </p>
<dl>
<dt>
<dd> &bull; &quot;man&quot;: use the <i>man</i> program as usual,</dl>
<dl>
<dt>
<dd> &bull; &quot;woman&quot;: use <i>emacsclient</i> to launch the &quot;woman&quot; mode in emacs (this only works starting with emacsclient versions 22),</dl>
<dl>
<dt>
<dd> &bull; &quot;konqueror&quot;: use <i>kfmclient</i> to open the man page in a new konqueror tab (see <i>Note about konqueror</i> below).</dl>
<p> Values for other tools can be used if there is a corresponding <code>man.&lt;tool&gt;.cmd</code> configuration entry (see below). </p>
<p> Multiple values may be given to the <code>man.viewer</code> configuration variable. Their corresponding programs will be tried in the order listed in the configuration file. </p>
<p> For example, this configuration: </p>
<dl>
<dt>
<dd>
<pre>
        [man]
                viewer = konqueror
                viewer = woman
</pre>
</dl>
<p> will try to use konqueror first. But this may fail (for example, if DISPLAY is not set) and in that case emacs&#8217; woman mode will be tried. </p>
<p> If everything fails, or if no viewer is configured, the viewer specified in the <code>GIT_MAN_VIEWER</code> environment variable will be tried. If that fails too, the <i>man</i> program will be tried anyway.</p>
<h3>man.&lt;tool&gt;.path</h3>
<p> You can explicitly provide a full path to your preferred man viewer by setting the configuration variable <code>man.&lt;tool&gt;.path</code>. For example, you can configure the absolute path to konqueror by setting <i>man.konqueror.path</i>. Otherwise, <i>git help</i> assumes the tool is available in PATH.</p>
<h3>man.&lt;tool&gt;.cmd</h3>
<p> When the man viewer, specified by the <code>man.viewer</code> configuration variables, is not among the supported ones, then the corresponding <code>man.&lt;tool&gt;.cmd</code> configuration variable will be looked up. If this variable exists then the specified tool will be treated as a custom command and a shell eval will be used to run the command with the man page passed as arguments.</p>
<h3>Note about konqueror</h3>
<p> When <i>konqueror</i> is specified in the <code>man.viewer</code> configuration variable, we launch <i>kfmclient</i> to try to open the man page on an already opened konqueror in a new tab if possible. </p>
<p> For consistency, we also try such a trick if <i>man.konqueror.path</i> is set to something like <code>A_PATH_TO/konqueror</code>. That means we will try to launch <code>A_PATH_TO/kfmclient</code> instead. </p>
<p> If you really want to use <i>konqueror</i>, then you can use something like the following: </p>
<dl>
<dt>
<dd>
<pre><code>
[man] viewer = konq
    [man "konq"] cmd = A_PATH_TO / konqueror
</code></pre>
</dl>
<h3>Note about git config &#8211;global</h3>
<p> Note that all these configuration variables should probably be set using the <code>&#8211;global</code> flag, for example like this: </p>
<dl>
<dt>
<dd>
<pre>
$ git config --global help.format web
$ git config --global web.browser firefox
</pre>
</dl>
<p> as they are probably more user specific than repository specific. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for more information about this.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
