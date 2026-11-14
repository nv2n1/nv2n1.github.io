---
title: "pure-uploadscript(8)"
name: "pure-uploadscript"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pure-uploadscript/"
description: "pure-uploadscript – Automatically run an external program after a successful upload"
---

<p>pure-uploadscript &#8211; Automatically run an external program after a successful upload</p>
<h2>Syntax</h2>
<p>pure-uploadscript [<i>-p</i> &lt;<i>/path/to/pidfile</i>&gt;] [<i>-B</i>] [<i>-g</i> &lt;<i>gid</i>&gt;] [<i>-h</i>] <i>-r</i> &lt;<i>program to run</i>&gt; [<i>-u</i> &lt;<i>uid</i>&gt;]</p>
<h2>Description</h2>
<p>If Pure-FTPd is compiled with <code>&#8211;with-uploadscript</code> (default in binary distributions), and if the <code>-o</code> (or <code>&#8211;uploadscript</code>) is passed to the server, a named pipe called <code>/var/run/pure-ftpd.upload.pipe</code> is created. You will also notice an important file called <code>/var/run/pure-ftpd.upload.lock</code>, used for locking.<br />
 After a successful upload, the file name is written to the pipe.<br />
 <code>pure-uploadscript</code> reads this pipe to automatically run any program or script to process the newly uploaded file.</p>
<h2>Options</h2>
<dl>
<dt><code>-B</code></p>
<dd>Daemonize the process and fork it in background.</p>
<dt><code>-g</code> &lt;<i>gid</i>&gt;</p>
<dd>Switch the group ID to &lt;<i>gid</i>&gt;.</p>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd>Display available options.</p>
<dt><code>-r</code> &lt;<i>program to run</i>&gt;</p>
<dd>Tell what program/script to run. It has to be <i>an absolute filename</i>, the <code>PATH</code> environment variable is ignored. The first argument of that program will be the <i>unquoted</i> name of the newly uploaded file. Environment variables aren&#8217;t cleared. So don&#8217;t put sensitive data in them before calling pure-uploadscript if you switch uid.</p>
<dt><code>-u</code> &lt;<i>uid</i>&gt;</p>
<dd>Switch the user ID to &lt;<i>uid</i>&gt;.</dl>
<h2>Environment</h2>
<p>When the upload script is run, the name of the newly uploaded file is the first argument passed to the script (referenced as $1 by most shells) . Some environment variables are also filled by useful info about the file. <code>UPLOAD_SIZE</code> The size of the file, in bytes. <code>UPLOAD_PERMS</code> The permissions, as an octal integer. <code>UPLOAD_UID</code> The numerical UID of the owner. <code>UPLOAD_GID</code> The numerical GID of the owner. <code>UPLOAD_USER</code> The login of the owner. <code>UPLOAD_GROUP</code> The group name the files belongs to. <code>UPLOAD_VUSER</code> The full user name, or the virtual user name (127 chars max) .</p>
<h2>Files</h2>
<p><i>/var/run/pure-ftpd.upload.pipe</i> <i>/var/run/pure-ftpd.upload.lock</i> <i>/var/run/pure-uploadscript.pid</i></p>
<h2>Security</h2>
<p><code>pure-ftpd</code> and <code>pure-uploadscript</code> are trying to limit security implications of such a feature.</p>
<dl>
<dt>&#8211; The pipe can only be created and opened by root. It must have perms 600, with uid 0, or it will be ignored.</p>
<dd>
<dt>&#8211; The argument passed to an external program/script is always an exact absolute path name. It doesn&#8217;t get fooled by <code>chroot()</code>ed environments, and by absolute or relative paths added to the STOR command.</p>
<dd>
<dt>&#8211; UID and GID are set just after parsing command-line options, and <code>pure-uploadscript</code> never gets back supervisor privileges.</p>
<dd>
<dt>&#8211; Descriptors to the pipe are never passed to external programs/scripts. So when UID switched, the target user can&#8217;t mess the pipe.</p>
<dd>
<dt>&#8211; Only regular files are processed, control characters are rejected, and a header+footer avoid partial file names.</p>
<dd>
<dt>&#8211; Two external programs/scripts can&#8217;t run at the same time. Uploads are always processed sequentially, in chronological order. This is to avoid denial-of-services by issuing a lot of simultaneous STOR commands in order to launch a fork bomb on the server. For this reason, your programs shouldn&#8217;t take a long time to complete (but they can run themselves in background) .</p>
<dd></dl>
<h2>Examples</h2>
<p>A sample script could be : #! /bin/sh<br />
 echo &quot;$1 uploaded&quot; | /usr/bin/mutt -s &quot;New upload : $1&quot; \ ftpadmin [at] dom.ai.n Never forget to quote (<code>&quot;variable&quot;</code>) all variables in all your shell scripts to avoid security flaws. </p>
<h2>Authors</h2>
<p>Frank DENIS &lt;j at pureftpd dot org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ftp/">ftp</a>(1)</code>, <code><a href="/docs/linux/man/8-pure-ftpd/">pure-ftpd</a>(8)</code> <code><a href="/docs/linux/man/8-pure-ftpwho/">pure-ftpwho</a>(8)</code> <code><a href="/docs/linux/man/8-pure-mrtginfo/">pure-mrtginfo</a>(8)</code> <code><a href="/docs/linux/man/8-pure-uploadscript/">pure-uploadscript</a>(8)</code> <code><a href="/docs/linux/man/8-pure-statsdecode/">pure-statsdecode</a>(8)</code> <code><a href="/docs/linux/man/8-pure-pw/">pure-pw</a>(8)</code> <code><a href="/docs/linux/man/8-pure-quotacheck/">pure-quotacheck</a>(8)</code> <code><a href="/docs/linux/man/8-pure-authd/">pure-authd</a>(8)</code> <code>RFC 959</code>, <code>RFC 2228,</code> <code>RFC 2389</code> and <code>RFC 2428</code>. </p>
