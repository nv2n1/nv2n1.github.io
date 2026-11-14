---
title: "keychain(1)"
name: "keychain"
section: "1"
letter: "k"
url: "/docs/linux/man/1-keychain/"
description: "keychain – re-use ssh-agent and/or gpg-agent between logins"
---

<h2>NAME</h2>
<p> keychain &#8211; re-use ssh-agent and/or gpg-agent between logins</p>
<h2>SYNOPSIS</h2>
<p> keychain&nbsp;<wbr>[&nbsp;<wbr>-hkQqV&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>&#8211;clear &#8211;help &#8211;ignore-missing &#8211;noask &#8211;nocolor &#8211;nogui &#8211;nolock &#8211;quick &#8211;quiet &#8211;version&nbsp;<wbr>] [&nbsp;<wbr>&#8211;agents&nbsp;<wbr><i>list</i>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>&#8211;attempts&nbsp;<wbr><i>num</i>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>&#8211;dir&nbsp;<wbr><i>dirname</i>&nbsp;<wbr>] [&nbsp;<wbr>&#8211;host&nbsp;<wbr><i>name</i>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>&#8211;lockwait&nbsp;<wbr><i>seconds</i>&nbsp;<wbr>] [&nbsp;<wbr>&#8211;stop&nbsp;<wbr><i>which</i>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>&#8211;timeout&nbsp;<wbr><i>minutes</i>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>keys&#8230;&nbsp;<wbr>]</p>
<h2>DESCRIPTION</h2>
<p> keychain is a manager for ssh-agent, typically run from ~/.bash_profile. It allows your shells and cron jobs to share a single ssh-agent process. By default, the ssh-agent started by keychain is long-running and will continue to run, even after you have logged out from the system. If you want to change this behavior, take a look at the &#8211;clear and &#8211;timeout options, described below. </p>
<p> When keychain is run, it checks for a running ssh-agent, otherwise it starts one. It saves the ssh-agent environment variables to ~/.keychain/${<font SIZE="-1">HOSTNAME</font>}-sh, so that subsequent logins and non-interactive shells such as cron jobs can source the file and make passwordless ssh connections. In addition, when keychain runs, it verifies that the key files specified on the command-line are known to ssh-agent, otherwise it loads them, prompting you for a password if necessary. </p>
<p> Keychain also supports gpg-agent in the same ways that ssh-agent is supported. By default keychain attempts to start all available agents but will fall back to only gpg-agent or only ssh-agent if either is unavailable. You can specifically limit keychain using the &#8211;agents option. </p>
<p> keychain supports most UNIX-like operating systems, including Cygwin. It works with Bourne-compatible, csh-compatible and fish shells.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;agents</code> <i>list</i></p>
<dd> Start the agents listed. By default keychain will build the list automatically based on the existence of ssh-agent and/or gpg-agent on the system. The list should be comma-separated, for example &#8220;gpg,ssh&#8221;</p>
<dt><code>&#8211;attempts</code> <i>num</i></p>
<dd> Try num times to add keys before giving up. The default is 1.</p>
<dt><code>&#8211;clear</code></p>
<dd> Delete all of ssh-agent&#8217;s keys. Typically this is used in .bash_profile. The theory behind this is that keychain should assume that you are an intruder until proven otherwise. However, while this option increases security, it still allows your cron jobs to use your ssh keys when you&#8217;re logged out.</p>
<dt><code>&#8211;confirm</code></p>
<dd> Keys are subject to interactive confirmation by the <font SIZE="-1">SSH_ASKPASS</font> program before being used for authentication. See the -c option for <i><a href="/docs/linux/man/1-ssh-add/">ssh-add</a></i>(1).</p>
<dt><code>&#8211;dir</code> <i>dirname</i></p>
<dd> Keychain will use dirname rather than <tt>$HOME</tt>/.keychain</p>
<dt><code>&#8211;eval</code></p>
<dd> Keychain will print lines to be evaluated in the shell on stdout. It respects the <font SIZE="-1">SHELL</font> environment variable to determine if Bourne shell or C shell output is expected.</p>
<dt><code>&#8211;env</code> <i>filename</i></p>
<dd> After parsing options, keychain will load additional environment settings from &#8220;filename&#8221;. By default, if &#8220;&#8211;env&#8221; is not given, then keychain will attempt to load from ~/.keychain/[hostname]-env or alternatively ~/.keychain/env. The purpose of this file is to override settings such as <font SIZE="-1">PATH</font>, in case ssh is stored in a non-standard place.</p>
<dt><code>-h &#8211;help</code></p>
<dd> Show help that looks remarkably like this man-page.</p>
<dt><code>&#8211;host</code> <i>name</i></p>
<dd> Set alternate hostname for creation of pidfiles</p>
<dt><code>&#8211;ignore-missing</code></p>
<dd> Don&#8217;t warn if some keys on the command-line can&#8217;t be found. This is useful for situations where you have a shared .bash_profile, but your keys might not be available on every machine where keychain is run.</p>
<dt><code>&#8211;inherit</code> <i>which</i></p>
<dd> Attempt to inherit agent variables from the environment. This can be useful in a variety of circumstances, for example when ssh-agent is started by gdm. The following values are valid for &#8220;which&#8221;:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>local</code></p>
<dd> Inherit when a pid (e.g. <font SIZE="-1">SSH_AGENT_PID</font>) is set in the environment. This disallows inheriting a forwarded agent.</p>
<dt><code>any</code></p>
<dd> Inherit when a sock (e.g. <font SIZE="-1">SSH_AUTH_SOCK</font>) is set in the environment. This allows inheriting a forwarded agent.</p>
<dt><code>local-once</code></p>
<dd> Same as &#8220;local&#8221;, but only inherit if keychain isn&#8217;t already providing an agent.</p>
<dt><code>any-once</code></p>
<dd> Same as &#8220;any&#8221;, but only inherit if keychain isn&#8217;t already providing an agent.</dl>
</dl>
<dl>
<dt>
<dd>
<p> By default, keychain-2.5.0 and later will behave as if &#8220;&#8211;inherit local-once&#8221; is specified. You should specify &#8220;&#8211;noinherit&#8221; if you want the older behavior.</dl>
<dt><code>&#8211;lockwait</code> <i>seconds</i></p>
<dd> How long to wait for the lock to become available. Defaults to 30 seconds. -1 indicates to wait forever.</p>
<dt><code>&#8211;noask</code></p>
<dd> This option tells keychain do everything it normally does (ensure ssh-agent is running, set up the ~/.keychain/[hostname]-{c}sh files) except that it will not prompt you to add any of the keys you specified if they haven&#8217;t yet been added to ssh-agent.</p>
<dt><code>&#8211;nocolor</code></p>
<dd> Disable color hilighting for non ANSI-compatible terms.</p>
<dt><code>&#8211;nogui</code></p>
<dd> Don&#8217;t honor <font SIZE="-1">SSH_ASKPASS</font>, if it is set. This will cause ssh-add to prompt on the terminal instead of using a graphical program.</p>
<dt><code>&#8211;noinherit</code></p>
<dd> Don&#8217;t inherit any agent processes, overriding the default &#8220;&#8211;inherit local-once&#8221;</p>
<dt><code>&#8211;nolock</code></p>
<dd> Don&#8217;t attempt to use a lockfile while manipulating files, pids and keys.</p>
<dt><code>-k &#8211;stop</code> <i>which</i></p>
<dd> Kill currently running agent processes. The following values are valid for &#8220;which&#8221;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>all</p>
<dd> Kill all agent processes and quit keychain immediately. Prior to keychain-2.5.0, this was the behavior of the bare &#8220;&#8211;stop&#8221; option.</p>
<dt>others</p>
<dd> Kill agent processes other than the one keychain is providing. Prior to keychain-2.5.0, keychain would do this automatically. The new behavior requires that you specify it explicitly if you want it.</p>
<dt>mine</p>
<dd> Kill keychain&#8217;s agent processes, leaving other agents alone.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-Q &#8211;quick</code></p>
<dd> If an ssh-agent process is running then use it. Don&#8217;t verify the list of keys, other than making sure it&#8217;s non-empty. This option avoids locking when possible so that multiple terminals can be opened simultaneously without waiting on each other.</p>
<dt><code>-q &#8211;quiet</code></p>
<dd> Only print messages in case of warning, error or required interactivity.</p>
<dt><code>&#8211;timeout</code> <i>minutes</i></p>
<dd> Set a timeout in minutes on your keys. This is conveyed to ssh-agent which does the actual timing out of keys since keychain doesn&#8217;t run continuously.</p>
<dt><code>-V &#8211;version</code></p>
<dd> Show version information.</dl>
<h2>EXAMPLES</h2>
<p> Note that the examples below assume that keychain is available on the machine they&#8217;re run. If you&#8217;re using them in your login profile snippets that are shared between systems, it may be a good idea to protect their invocation by first checking if keychain is indeed available. </p>
<p> This snippet should work in any shell to load two ssh keys (id_rsa and id_dsa) and one gpg key (key id 0123ABCD): </p>
<pre>
    eval `keychain --eval id_rsa id_dsa 0123ABCD`
</pre>
<p> If you have trouble with that in csh: </p>
<pre>
    setenv SHELL /bin/csh
    eval `keychain --eval id_rsa id_dsa 0123ABCD`
</pre>
<p> This is equivalent for Bourne shells (including bash and zsh) but doesn&#8217;t use keychain&#8217;s &#8211;eval feature: </p>
<pre><code>
keychain id_rsa id_dsa 0123ABCD
    [-z "$HOSTNAME"] &amp;&amp;HOSTNAME =`uname - n`
                                              [-f $HOME /.keychain / $HOSTNAME - sh] &amp;&amp;
                                     .$HOME /.keychain / $HOSTNAME - sh
                                                                         [-f $HOME /.keychain / $HOSTNAME - sh - gpg] &amp;&amp;
                                     .$HOME /.keychain / $HOSTNAME - sh - gpg
</code></pre>
<p> This is equivalent for C shell (including tcsh): </p>
<p>keychain id_rsa id_dsa 0123ABCD host =`uname &#8211; n` if (-f $HOME /.keychain / $host &#8211; csh) then source $HOME /.keychain / $host &#8211; csh endif if (-f $HOME /.keychain / $host &#8211; csh &#8211; gpg) then source $HOME /.keychain / $host &#8211; csh &#8211; gpg endif</p>
<p> To load keychain variables from a script (for example from cron) and abort unless id_dsa is available: </p>
<pre><code>
#Load keychain variables and check for id_dsa
[-z "$HOSTNAME"] &amp;&amp;HOSTNAME =`uname - n` .$HOME /.keychain / $HOSTNAME - sh 2 &gt; / dev / null ssh - add - l 2 &gt; / dev / null | grep - q id_dsa || exit 1
</code></pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ssh-agent/">ssh-agent</a></i>(1)</p>
<h2>NOTES</h2>
<p> Keychain is maintained by Aron Griffis &lt;agriffis [at] gentoo.org&gt;. If you need to report a bug or request an enhancement, please do so at &lt;<a rel="nofollow" href="http://bugs.gentoo.org/">http://bugs.gentoo.org/</a>&gt; and assign to agriffis [at] gentoo.org </p>
<p> Keychain was originally written by Daniel Robbins &lt;drobbins [at] gentoo.org&gt;, who has also written a series of three articles about it. The articles can be found starting at &lt;<a rel="nofollow" href="http://www-106.ibm.com/developerworks/library/l-keyc.html">http://www-106.ibm.com/developerworks/library/l-keyc.html</a>&gt; </p>
<h2>Index</h2>
