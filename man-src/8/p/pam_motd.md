---
title: "pam_motd(8)"
name: "pam_motd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_motd/"
description: "pam_motd – Display the motd file"
---

<p>pam_motd &#8211; Display the motd file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_motd.so</code> [motd=<i>/path/filename</i>] [motd_dir=<i>/path/dirname.d</i>]</dl>
<h2>Description</h2>
<dd>pam_motd is a PAM module that can be used to display arbitrary motd (message of the day) files after a successful login. By default, pam_motd shows files in the following locations: </p>
<dl>
<dd>/etc/motd</dl>
<dl>
<dd>/run/motd</dl>
<dl>
<dd>/usr/lib/motd</dl>
<dl>
<dd>/etc/motd.d/</dl>
<dl>
<dd>/run/motd.d/</dl>
<dl>
<dd>/usr/lib/motd.d/</dl>
<p> Each message size is limited to 64KB. </p>
<p> If /etc/motd does not exist, then /run/motd is shown. If /run/motd does not exist, then /usr/lib/motd is shown. </p>
<p> Similar overriding behavior applies to the directories. Files in /etc/motd.d/ override files with the same name in /run/motd.d/ and /usr/lib/motd.d/. Files in /run/motd.d/ override files with the same name in /usr/lib/motd.d/. </p>
<p> Files the in the directories listed above are displayed in lexicographic order by name. </p>
<p> To silence a message, a symbolic link with target /dev/null may be placed in /etc/motd.d with the same filename as the message to be silenced. Example: Creating a symbolic link as follows silences /usr/lib/motd.d/my_motd. </p>
<p> <code>ln -s /dev/null /etc/motd.d/my_motd</code> </p>
<p> The <code>MOTD_SHOWN=pam</code> environment variable is set after showing the motd files, even when all of them were silenced using symbolic links.</p>
<h2>Options</h2>
<p><code>motd=</code><i>/path/filename</i></p>
<dl>
<dd>The /path/filename file is displayed as message of the day. Multiple paths to try can be specified as a colon-separated list. By default this option is set to /etc/motd:/run/motd:/usr/lib/motd.</dl>
<p> <code>motd_dir=</code><i>/path/dirname.d</i></p>
<dl>
<dd>The /path/dirname.d directory is scanned and each file contained inside of it is displayed. Multiple directories to scan can be specified as a colon-separated list. By default this option is set to /etc/motd.d:/run/motd.d:/usr/lib/motd.d.</dl>
<p> <code>noupdate</code></p>
<dl>
<dd>Don&#8217;t run the scripts in /etc/update-motd.d to refresh the motd file.</dl>
<p> When no options are given, the default behavior applies for both options. Specifying either option (or both) will disable the default behavior for both options.</p>
<h2>Module Types Provided</h2>
<p>Only the <code>session</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_ABORT</p>
<dl>
<dd>Not all relevant data or options could be obtained.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>This is the default return value of this module.</dl>
<h2>Examples</h2>
<p>The suggested usage for /etc/pam.d/login is:</p>
<dl>
<dd>
<pre>session optional pam_motd.so</pre>
</dl>
<p> To use a motd file from a different location:</p>
<dl>
<dd>
<pre>session optional pam_motd.so motd=/elsewhere/motd</pre>
</dl>
<p> To use a motd file from elsewhere, along with a corresponding .d directory:</p>
<dl>
<dd>
<pre>session optional pam_motd.so motd=/elsewhere/motd motd_dir=/elsewhere/motd.d</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-motd/">motd</a></code>(5), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7), <code><a href="/docs/linux/man/5-update-motd/">update-motd</a></code>(5)</p>
<h2>Author</h2>
<p>pam_motd was written by Ben Collins &lt;bcollins [at] debian.org&gt;. </p>
<p> The <code>motd_dir=</code> option was added by Allison Karlitskaya &lt;allison.karlitskaya [at] redhat.com&gt;.</p>
