---
title: "gsexec(8)"
name: "gsexec"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gsexec/"
description: "gsexec – Switch user before executing external programs"
---

<p><code>gsexec </code> &#8211; Switch user before executing external programs </p>
<h2>Synopsis</h2>
<p>&nbsp;<wbr> <code>gsexec</code> [-V]<br />
&nbsp;<wbr></p>
<h2>Summary</h2>
<p>gsexec is used by the Apache HTTP Server to switch to another user before executing CGI programs. In order to achieve this, it must run as root. Since the HTTP daemon normally doesn&#8217;t run as root, the gsexec executable needs the setuid bit set and must be owned by root. It should never be writable for any other person than root.<br />
&nbsp;<wbr> gsexec is based on Apache&#8217;s suexec, and its behaviour is controlled with the Apache configuration file directives <code>GridSiteExecMethod</code> and <code>GridSiteUserGroup</code> added to Apache by <code><a href="/docs/linux/man/8-mod_gridsite/">mod_gridsite</a>(8)</code> Four execution methods are supported: nosetuid, suexec, X509DN and directory, and these may be set on a per-directory basis within the Apache configuration file.</p>
<h2>Nosetuid Method</h2>
<p>This is the default behaviour, but can also be produced by giving <code>GridSiteExecMethod nosetuid</code> </p>
<p> CGI programs will then be executed without using gsexec, and will run as the Unix user given by the User and Group Apache directives (normally apache.apache on Red Hat derived systems.)</p>
<h2>Suexec Method</h2>
<p>If <code>GridSiteExecMethod suexec</code> is given for this virtual host or directory, then CGI programs will be executed using the user and group given by the <code>GridSiteUserGroup user group</code> directive, which may also be set on a per-directory basis (unlike suexec&#8217;s <code>SuexecUserGroup</code> which is per-server only.) The CGI program must either be owned by root, the Apache user and group specified at gsexec build-time (normally apache.apache) or by the user and group given with the <code>GridSiteUserGroup</code> directive.</p>
<h2>X509Dn Method</h2>
<p>If <code>GridSiteExecMethod X509DN</code> is given, then the CGI program runs as a pool user, detemined using lock files in the exec mapping directory chosen as build time of gsexec. The pool user is chosen according to the client&#8217;s full certificate X.509 DN (ie with any trailing GSI proxy name components stripped off.) Subsequent requests by the same X.509 identity will be mapped to the same pool user. The CGI program must either be owned by root, the Apache user and group specified at gsexec build-time (normally apache.apache) or by the pool user selected.</p>
<h2>Directory Method</h2>
<p>If <code>GridSiteExecMethod directory</code> is given, then the CGI program runs as a pool user chosen according to the directory in which the CGI is located: all CGIs in that directory run as the same pool user. The CGI program must either be owned by root, the Apache user and group specified at gsexec build-time (normally apache.apache) or by the pool user selected.</p>
<h2>Execmapdir</h2>
<p>The default exec mapping directory is /var/www/execmapdir and this is fixed when the gsexec executable is built. The exec mapping directory and all of its lock files must be owned and only writable by root. To initialise the lock files, create an empty lock file for each pool user, with the pool username as the filename (eg user0001, user0002, &#8230;) As the pool users are leased to X.509 identities or directories, they will become hard linked to lock files with the URL-encoded X.509 DN or full directory path. </p>
<p> You can recycle pool users by removing the corresponding URL-encoded hard link. <code><a href="/docs/linux/man/1-stat/">stat</a>(1)</code> and <code><a href="/docs/linux/man/1-ls/">ls</a>(1)</code> with option <code>-i</code> can be used to print the inodes of lock files to match up the hard links. </p>
<p> <code>However, you must ensure that all files and processes owned by the pool</code> <code>user are deleted before recycling!</code></p>
<h2>Options</h2>
<p>&nbsp;<wbr></p>
<dl>
<dt>-V</p>
<dd>If you are root, this option displays the compile options of gsexec. For security reasons all configuration options are changeable only at compile time.<br />
&nbsp;<wbr></dl>
<h2>More Information</h2>
<p>For further information about the concepts and the security model of the original Apache suexec please refer to the suexec documentation: </p>
<p> <a rel="nofollow" href="http://httpd.apache.org/docs-2.0/suexec.html">http://httpd.apache.org/docs-2.0/suexec.html</a> </p>
<p> For examples using the gsexec extensions, please see the GridSite gsexec page: </p>
<p> <a rel="nofollow" href="http://www.gridsite.org/wiki/Gsexec">http://www.gridsite.org/wiki/Gsexec</a></p>
<h2>Authors</h2>
<p>Apache project, for original suexec </p>
<p> Andrew McNab &lt;Andrew.McNab [at] manchester.ac.uk&gt; for gsexec modifications. </p>
<p> gsexec is part of GridSite: <a rel="nofollow" href="http://www.gridsite.org/">http://www.gridsite.org/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-httpd/">httpd</a>(8),</code> <code><a href="/docs/linux/man/8-suexec/">suexec</a>(8),</code> <code><a href="/docs/linux/man/8-mod_gridsite/">mod_gridsite</a>(8)</code> </p>
