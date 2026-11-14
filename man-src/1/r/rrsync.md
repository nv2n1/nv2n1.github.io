---
title: "rrsync(1)"
name: "rrsync"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrsync/"
description: "rrsync – a script to setup restricted rsync users via ssh logins"
---

<h2 class="name">NAME</h2>
<p> rrsync &#8211; a script to setup restricted rsync users via ssh logins</p>
<h2>SYNOPSIS</h2>
<pre><code>
rrsync[-ro | -rw][-munge][-no - del][-no - lock] DIR
</code></pre>
<p> The single non-option argument specifies the restricted <i>DIR</i> to use. It can be relative to the user&#8217;s home directory or an absolute path. </p>
<p> The online version of this manpage (that includes cross-linking of topics) is available at <a rel="nofollow" href="https://download.samba.org/pub/rsync/rrsync.1.">https://download.samba.org/pub/rsync/rrsync.1.</a> </p>
<h2>DESCRIPTION</h2>
<p> A user&#8217;s ssh login can be restricted to only allow the running of an rsync transfer in one of two easy ways: </p>
<dl>
<dt>o</p>
<dd> forcing the running of the rrsync script</p>
<dt>o</p>
<dd> forcing the running of an rsync daemon-over-ssh command.</dl>
<p> Both of these setups use a feature of ssh that allows a command to be forced to run instead of an interactive shell. However, if the user&#8217;s home shell is bash, please see BASH SECURITY ISSUE for a potential issue. </p>
<p> To use the rrsync script, edit the user&#8217;s <code>~/.ssh/authorized_keys</code> file and add a prefix like one of the following (followed by a space) in front of each ssh-key line that should be restricted:</p>
<dl>
<dt>
<dd>
<pre>
command=&quot;rrsync DIR&quot;
command=&quot;rrsync -ro DIR&quot;
command=&quot;rrsync -munge -no-del DIR&quot;
</pre>
</dl>
<p> Then, ensure that the rrsync script has your desired option restrictions. You may want to copy the script to a local bin dir with a unique name if you want to have multiple configurations. One or more rrsync options can be specified prior to the <i>DIR</i> if you want to further restrict the transfer. </p>
<p> To use an rsync daemon setup, edit the user&#8217;s <code>~/.ssh/authorized_keys</code> file and add a prefix like one of the following (followed by a space) in front of each ssh-key line that should be restricted:</p>
<dl>
<dt>
<dd>
<pre><code>
command = "rsync --server --daemon ." command = "rsync --server --daemon --config=/PATH/TO/rsyncd.conf ."
</code></pre>
</dl>
<p> Then, ensure that the rsyncd.conf file is created with one or more module names with the appropriate path and option restrictions. If rsync&#8217;s <code>&#8211;config</code> option is omitted, it defaults to <code>~/rsyncd.conf</code>. See the <code><a href="/docs/linux/man/5-rsyncd-conf/">rsyncd.conf</a></code>(5) manpage for details of how to configure an rsync daemon. </p>
<p> When using rrsync, there can be just one restricted dir per authorized key. A daemon setup, on the other hand, allows multiple module names inside the config file, each one with its own path setting. </p>
<p> The remainder of this manpage is dedicated to using the rrsync script. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-ro</code></p>
<dd> Allow only reading from the DIR. Implies <code>-no-del</code> and <code>-no-lock</code>.</p>
<dt><code>-wo</code></p>
<dd> Allow only writing to the DIR.</p>
<dt><code>-munge</code></p>
<dd> Enable rsync&#8217;s <code>&#8211;munge-links</code> on the server side.</p>
<dt><code>-no-del</code></p>
<dd> Disable rsync&#8217;s <code>&#8211;delete*</code> and <code>&#8211;remove*</code> options.</p>
<dt><code>-no-lock</code></p>
<dd> Avoid the single-run (per-user) lock check. Useful with <code>-munge</code>.</p>
<dt><code>-help</code>, <code>-h</code></p>
<dd> Output this help message and exit.</dl>
<h2>SECURITY RESTRICTIONS</h2>
<p> The rrsync script validates the path arguments it is sent to try to restrict them to staying within the specified DIR. </p>
<p> The rrsync script rejects rsync&#8217;s <code>&#8211;copy-links</code> option (by default) so that a copy cannot dereference a symlink within the DIR to get to a file outside the DIR. </p>
<p> The rrsync script rejects rsync&#8217;s <code>&#8211;protect-args</code> (<code>-s</code>) option because it would allow options to be sent to the server-side that the script cannot check. If you want to support <code>&#8211;protect-args</code>, use a daemon-over-ssh setup. </p>
<p> The rrsync script accepts just a subset of rsync&#8217;s options that the real rsync uses when running the server command. A few extra convenience options are also included to help it to interact with BackupPC and accept some convenient user overrides. </p>
<p> The script (or a copy of it) can be manually edited if you want it to customize the option handling. </p>
<h2>BASH SECURITY ISSUE</h2>
<p> If your users have bash set as their home shell, bash may try to be overly helpful and ensure that the user&#8217;s login bashrc files are run prior to executing the forced command. This can be a problem if the user can somehow update their home bashrc files, perhaps via the restricted copy, a shared home directory, or something similar. </p>
<p> One simple way to avoid the issue is to switch the user to a simpler shell, such as dash. When choosing the new home shell, make sure that you&#8217;re not choosing bash in disguise, as it is unclear if it avoids the security issue. </p>
<p> Another potential fix is to ensure that the user&#8217;s home directory is not a shared mount and that they have no means of copying files outside of their restricted directories. This may require you to force the enabling of symlink munging on the server side. </p>
<p> A future version of openssh may have a change to the handling of forced commands that allows it to avoid using the user&#8217;s home shell. </p>
<h2>EXAMPLES</h2>
<p> The <code>~/.ssh/authorized_keys</code> file might have lines in it like this:</p>
<dl>
<dt>
<dd>
<pre>
command=&quot;rrsync client/logs&quot; ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAIEAzG...
command=&quot;rrsync -ro results&quot; ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAIEAmk...
</pre>
</dl>
<h2>FILES</h2>
<p> ~/.ssh/authorized_keys </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1), <code><a href="/docs/linux/man/5-rsyncd-conf/">rsyncd.conf</a></code>(5) </p>
<h2>VERSION</h2>
<p> This manpage is current for version 3.2.7 of rsync. </p>
<h2>CREDITS</h2>
<p> rsync is distributed under the GNU General Public License. See the file COPYING for details. </p>
<p> An rsync web site is available at <a rel="nofollow" href="https://rsync.samba.org/">https://rsync.samba.org/</a> and its github project is <a rel="nofollow" href="https://github.com/WayneD/rsync.">https://github.com/WayneD/rsync.</a> </p>
<h2>AUTHOR</h2>
<p> The original rrsync perl script was written by Joe Smith. Many people have later contributed to it. The python version was created by Wayne Davison. </p>
<h2>Index</h2>
