---
title: "rancid-cvs(1)"
name: "rancid-cvs"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rancid-cvs/"
description: "rancid-cvs – initialize CVS, Subversion or git and rancid group files and directories"
---

<h2 class="name">NAME</h2>
<p> rancid-cvs &#8211; initialize CVS, Subversion or git and rancid group files and directories </p>
<h2>SYNOPSIS</h2>
<p> <code>rancid-cvs</code> [<code>-V</code>] [<code>-f&nbsp;<wbr></code>config_file]&nbsp;<wbr>[group [group &#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> <code>rancid-cvs</code> creates the directories and <code><a href="/docs/linux/man/5-router-db/">router.db</a></code>(5) for each rancid group and handles the revision control system (CVS, Subversion or git) set-up in the location defined by the <i>CVSROOT</i> in <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5). It must be run after the initial installation and whenever a rancid group is added. If <i>CVSROOT</i> is a URL, <code>rancid-cvs</code> will not initialize the repository, the user must do this themselves. </p>
<p> <code>rancid-cvs</code> reads <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5) to configure itself, then proceeds with the initialization. First of the CVS, Subversion or git repository, if necessary, and then for each of the rancid groups listed on the command-line or those in the variable <i>LIST_OF_GROUPS</i> from <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5), if the argument is omitted. </p>
<p> Running <code>rancid-cvs</code> for groups which already exist will not cause problems. If the group&#8217;s directory already exists, the import into the revision control system will be skipped, and if it&#8217;s <code><a href="/docs/linux/man/5-router-db/">router.db</a></code>(5) already exists, it will not be altered. </p>
<p> The command-line options are as follows:</p>
<dl>
<dt><code>-V</code></p>
<dd> Prints package name and version strings.</p>
<dt><code>-f group_config_file</code></p>
<dd> Specify an alternative rancid.conf. The global rancid.conf file is read by <code>rancid-run.</code></dl>
<p> The best method for adding groups is by adding the group name to <i>LIST_OF_GROUPS</i> in <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5), then run <code>rancid-cvs.</code> <code>Do not create the directories manually, allow rancid-cvs to do it.</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cvs/">cvs</a></code>(1), <code><a href="/docs/linux/man/1-git/">git</a></code>(1), <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5), <code><a href="/docs/linux/man/5-router-db/">router.db</a></code>(5), <code><a href="/docs/linux/man/1-svn/">svn</a></code>(1)</p>
<h2>CAVEATS</h2>
<p> In the case of git, the groups are not exactly imported into the repository, rather a new repository is created for it, due to the way that git handles, what it calls, sparse checkouts. Instead, each group is a separate repository under the <code>CVSROOT</code> directory. </p>
<h2>Index</h2>
