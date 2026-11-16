---
title: "kdeinit4(8)"
name: "kdeinit4"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kdeinit4/"
description: "kdeinit4 – KDE process launcher."
---

<p>kdeinit4 &#8211; KDE process launcher.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kdeinit4</code> [&#8211;help] [[&#8211;no-fork] | [&#8211;no-kded] | [&#8211;suicide]] [[+programs] | [programs]]</dt></dl>
<h2>Description</h2>
<dd>kdeinit4 is a process launcher somewhat similar to the famous <code>init</code> used for booting UNIX. It executes KDE programs and kdeinit loadable modules (KLMs) starting them more efficiently. </dd>
<p> Using kdeinit4 to launch KDE applications makes starting a typical KDE application a couple times faster and reduces memory consumption by a substantial amount. </p>
<p> kdeinit4 is linked against all libraries a standard KDE application needs. With this technique, starting an application becomes much faster because now only the application itself needs to be linked whereas otherwise both the application as well as all the libaries it uses need to be linked.</p>
<h2>Disadvantages</h2>
<p>The process name of applications started via kdeinit4 is &quot;kdeinit4&quot;. This problem can be corrected to a degree by changing the application name as shown by <code>ps</code>. However, applications like <code>killall</code> will only see kdeinit4 as the process name. To workaround this, use <code>kdekillall</code> (from kdesdk/scripts) for applications started via kdeinit4.</p>
<h2>Options</h2>
<p><code>&#8211;help</code></p>
<dl>
<dd>Show help about options</dd></dl>
<p> <code>&#8211;no-fork</code></p>
<dl>
<dd>Do not fork, i.e. do not exit until all the executed programs ends</dd></dl>
<p> <code>&#8211;no-kded</code></p>
<dl>
<dd>Do not start kded</dd></dl>
<p> <code>&#8211;suicide</code></p>
<dl>
<dd>Terminate when no KDE applications are left running</dd></dl>
<p> <code>+programs</code></p>
<dl>
<dd>runs the programs handling requests</dd></dl>
<p> <code>programs</code></p>
<dl>
<dd>runs the programs without handling requests</dd></dl>
<h2>Usage</h2>
<p>A standard way to run this program is by simply specifying the following command at the prompt <code>kdeinit4</code><code> program</code> or <code>kdeinit4</code><code> +program </code></p>
<h2>Files</h2>
<p>/tmp/kde-$USER/kdeinit4_$INSTANCE</p>
<dl>
<dd>&#8230;</dd></dl>
<h2>Environment Variables</h2>
<p>$<code>HOME</code></p>
<dl>
<dd>Specifies the home directory of the current user</dd></dl>
<p> $<code>KDE_HOME_READONLY</code></p>
<dl>
<dd>Specifies if the home directory of the current user is read only</dd></dl>
<p> $<code>KDE_IS_PRELINKED</code></p>
<dl>
<dd>If set, tells kdeinit4 that the KDE programs are pre-linked. </dd>
<p> (Prelinking is a process that allows you to speed up the process of dynamic linking.)</dl>
<p> $<code>KDE_DISPLAY</code></p>
<dl>
<dd>If set, tells kdeinit4 that it is running on a KDE desktop.</dd></dl>
<h2>See Also</h2>
<p>kded, kdekillall</p>
<h2>Bugs</h2>
<p>There are probably tons of bugs. Use m[blue]<code>bugs.kde.org</code>m[]<font SIZE="-2">[1]</font> to report them.</p>
<h2>Authors</h2>
<p><code>Waldo Bastian</code> &lt;bastian [at] kde.org&gt;</p>
<dl>
<dd>Author.</dd></dl>
<p> <code>Mario Weilguni</code> &lt;mweilguni [at] sime.com&gt;</p>
<dl>
<dd>Author.</dd></dl>
<p> <code>Lubos Lunak</code> &lt;l.lunak [at] kde.org&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Notes</h2>
<dl>
<dt> 1.</dt>
<dd>bugs.kde.org</dd>
<dl>
<dd><a rel="nofollow" href="http://bugs.kde.org">http://bugs.kde.org</a></dd></dl>
</dl>