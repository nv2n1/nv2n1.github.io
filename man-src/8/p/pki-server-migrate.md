---
title: "pki-server-migrate(8)"
name: "pki-server-migrate"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pki-server-migrate/"
description: "pki-server-migrate – Command-Line Interface to run migration scripts on CS instances."
---

<p>pki-server-migrate &#8211; Command-Line Interface to run migration scripts on CS instances.</p>
<h2>Synopsis</h2>
<pre><code>pki-server [CLI options] migrate --tomcat </code>[7|8]</pre>
<h2>Description</h2>
<p>Apache Tomcat instances are configured differently in Tomcat 7 and 8. <code>pki-server migrate</code> makes the necessary changes in the instance configuration files and symbolic links so that the instance will work with the target Tomcat version. This command will migrate all instances to the target Apache Tomcat version. To migrate a specific instance only, use <code>pki-server instance-migrateFR. </p>
<h2>Options</h2>
<p>The CLI options are described in <code><a href="/docs/linux/man/8-pki-server/">pki-server</a></code>(8).</p>
<h2>Operations</h2>
<p>All <code>pki-server</code> commands must be executed as the system administrator.</p>
<h2>Authors</h2>
<p>Ade Lee &lt;alee [at] redhat.com&gt;</p>
<h2>Copyright</h2>
<p>Copyright (c) 2015 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
