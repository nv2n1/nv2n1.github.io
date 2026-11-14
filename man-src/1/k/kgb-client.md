---
title: "kgb-client(1)"
name: "kgb-client"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kgb-client/"
description: "kgb-client – relay commits to KGB servers"
---

<h2 class="name">NAME</h2>
<p> kgb-client &#8211; relay commits to KGB servers </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>kgb-client</code> &#8211;conf <i>/path/to/config</i> [<i>other-option</i> &#8230;]</p>
<dd>
<dt><code>kgb-client</code> &#8211;uri <i><a rel="nofollow" href="http://some.server:port/service">http://some.server:port/service</a></i> &#8211;password <i>password</i> &#8211;repo-id <i>repository</i> &#8211;repository <i>svn|git|cvs</i> &#8211;timeout <i>timeout-in-seconds</i> &#8211;single-line-commits <i>off|forced|auto</i> &#8211;use-irc-notices &#8211;web-link <i>template</i> &#8211;short-url-service <i>service</i> &#8211;status-dir <i>directory</i> &#8211;[no]-use-color &#8211;message-template <i>template</i> &#8211;batch-messages</p>
<dd>
<dt><code>kgb-client</code> <i>option</i>&#8230; <i>/svn/repo</i> <i>revision</i></p>
<dd>
<dt><code>kgb-client</code> <i>option</i>&#8230; <i>old-rev</i> <i>new-rev</i> <i>ref-name</i></p>
<dd>
<dt><code>kgb-client</code> <i>option</i>&#8230; $CVSROOT &quot;%p&quot;</p>
<dd>
<dt><code>kgb-client</code> <i>option</i>&#8230; &#8211;fake</p>
<dd>
<dt><code>kgb-client</code> <i>option</i>&#8230; &#8211;relay-msg <i>message</i>&#8230;</p>
<dd>
<dt><code>kgb-client</code> &#8211;help</p>
<dd>
<dt><code>kgb-client</code> &#8211;man</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> <code>kgb-client</code> is the client counterpart of <i><a href="/docs/linux/man/1-kgb-bot/">kgb-bot</a></i>(1). It is intended to be used as a hook in your version control system, executed after the repository gets updated. It analyzes the commit(s) and then relays the information to the <font SIZE="-1">KGB</font> server, which will show it on <font SIZE="-1">IRC.</font></p>
<h2>CONFIGURATION</h2>
<dl>
<dt><code>&#8211;conf</code> <i>configuration file</i></p>
<dd> Specifies the path to kgb-client configuration file.</dl>
<p> Configuration options (except <code>&#8211;conf</code>, <code>&#8211;fake</code> and <code>&#8211;relay-msg</code>) may be specified both in the configuration file and on the command line. Usually you want to have all the options in a configuration file, because having passwords on the command line is insecure. The configuration file also gives more control, for example it supports multiple servers and multiple ways of detection of branch and module names. </p>
<p> See <i><a href="/docs/linux/man/5-kgb-client-conf/">kgb-client.conf</a></i>(5) for available configuration options. Unless noted otherwise, all the options in the configuration file can also be used on command line, prefixing them with two dashes. E.g. <tt>&quot;repo-id&quot;</tt> becomes <tt>&quot;--repo-id&quot;</tt>. </p>
<p> Options given on the command line take precedence over configuration file.</p>
<h2>FAKE COMMIT MODE</h2>
<p> If invoked with the <code>&#8211;fake</code> option, <code>kgb-client</code> will send a fake commit to the servers. This is useful for testing client-server communication independently from <font SIZE="-1">VCS</font> setup.</p>
<h2>MESSAGE RELAY MODE</h2>
<p> When the <code>&#8211;relay-msg</code> option is given, there is no repository to be inspected. Instead, the non-option command line arguments are passed verbatim to the bot to display on <font SIZE="-1">IRC.</font> This can be used for real-time notification about other events like bug submissions etc.</p>
<h2>SUPPORTED VERSION CONTROL SYSTEMS</h2>
<h3>Subversion</h3>
<p> Installation requires calling <code>kgb-client</code> with two command line arguments, like this: </p>
<pre>
    /path/to/kgb-client &quot;$REPOS&quot; &quot;$REV&quot;
</pre>
<dl>
<dt><i>path to the subversion repository</i></p>
<dd> This is the physical path to the Subversion repository. Something like <i>/srv/svn/my-repo</i></p>
<dt><i>revision</i></p>
<dd> This is the revision number of the commit, that has triggered the hook.</dl>
<p> Both these arguments are supplied to the standard Subversion post-commit hooks.</p>
<h3>Git</h3>
<p> <code>kgb-client</code> shall be installed as a <code>post-receive</code> hook. Something along the following shall do: </p>
<pre>
    #!/bin/sh
    exec /path/to/kgb-client --conf /path/to.conf ...
</pre>
<p> By default, <code>kgb-client</code> will read the reflog information from standard input as any standard Git post-receive hook. See <code>&#8211;git-reflog</code> option if something else is wanted. </p>
<p> There are other ways to give kgb-client information about Git reflog, mostly useful when debugging on in unusual situations. See App::KGB::Client::Git. </p>
<p> The following settings can be configured via <i><a href="/docs/linux/man/1-git-config/">git-config</a></i>(1):</p>
<dl>
<dt>conf =item web-link</p>
<dd></dl>
<h3><font SIZE="-1">CVS</font></h3>
<p> <code>kgb-client</code> shall be installed in the <i>loginfo</i> file in the <tt>&quot;CVSROOT&quot;</tt> module of the <font SIZE="-1">CVS</font> repository. It shall be given two arguments &#8212; the repository root, and the directory in which the changes are being made. </p>
<p> For example: </p>
<pre>
    ALL /path/to/kgb-client --conf /path/to.conf ... &quot;$CVSROOT&quot; &quot;%p&quot;
</pre>
<h2>SEE ALSO</h2>
<dl>
<dt><i><a href="/docs/linux/man/5-kgb-client-conf/">kgb-client.conf</a></i>(5)</p>
<dd>
<dt>App::KGB::Client</p>
<dd>
<dt>App::KGB::Client::Subversion</p>
<dd>
<dt>App::KGB::Client::Git</p>
<dd>
<dt>App::KGB::Client::CVS</p>
<dd>
</dl>
<h2>Index</h2>
<dt><a href="#lbAL">SEE ALSO</a></p>
<dd></dl>
