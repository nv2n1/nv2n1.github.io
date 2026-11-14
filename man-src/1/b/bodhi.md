---
title: "bodhi(1)"
name: "bodhi"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bodhi/"
description: "bodhi – manage Fedora updates"
---

<h2>NAME</h2>
<p> bodhi &#8211; manage Fedora updates</p>
<h2>SYNOPSIS</h2>
<p> <code>bodhi</code> COMMAND SUBCOMMAND [OPTIONS] [ARGS]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>bodhi</code> is the command line interface to bodhi, Fedora&#8217;s update release management system. It can be used to create or modify updates and overrides.</p>
<h2>OPTIONS</h2>
<p> Most of the commands will accept these three options: </p>
<p> <code>&#8211;help</code> Show help text and exit. </p>
<p> <code>&#8211;password &lt;text&gt;</code> A password to authenticate as the user given by <code>&#8211;user</code>. </p>
<p> <code>&#8211;staging</code> Use the staging bodhi instance instead of the production instance. </p>
<p> <code>&#8211;user &lt;username&gt;</code> Many commands accept this flag to specify which user&#8217;s updates should be operated upon. </p>
<p> <code>&#8211;version</code> Show version and exit. Not accepted by subcommands.</p>
<h2>COMMANDS</h2>
<p> There are two commands, <code>overrides</code> and <code>updates</code>. They are described in more detail in their own sections below. </p>
<p> <code>bodhi overrides &lt;subcommand&gt; [options] [args]</code> Provides commands to aid in management of build overrides. Supports subcommands <code>query</code> and <code>save</code>, described below. </p>
<p> <code>bodhi updates &lt;subcommand&gt; [options] [args]</code> Provides an interface to manage updates. Supports subcommands <code>comment</code>, <code>download</code>, <code>new</code>, <code>query</code>, and <code>request</code>, described below.</p>
<h2>OVERRIDES</h2>
<p> The <code>overrides</code> command allows users to manage build overrides. </p>
<p> <code>bodhi overrides query [options]</code> The <code>query</code> subcommand provides an interface for users to query the bodhi server for existing overrides. </p>
<p> <code>bodhi overrides save [options] &lt;nvr&gt;</code> Save the build root given by <code>&lt;nvr&gt;</code> as a buildroot override. The <code>save</code> subcommand supports the following options: </p>
<p> <code>&#8211;duration &lt;days&gt;</code> The number of days the override should exist, given as an integer. </p>
<p> <code>&#8211;notes &lt;text&gt;</code> Notes on why this override is in place.</p>
<h2>UPDATES</h2>
<p> The <code>updates</code> command allows users to interact with bodhi updates. </p>
<p> <code>bodhi updates comment [options] &lt;update&gt; &lt;text&gt;</code> Leave the given text as a comment on a bodhi update. The <code>comment</code> subcommand supports the following options: </p>
<p> <code>&#8211;karma [+1 | 0 | -1]</code> The karma value you wish to contribute to the update. </p>
<p> <code>bodhi updates download [options]</code> Download update(s) given by CVE(s), ID(s), or NVR(s). One of <code>&#8211;cves</code>, <code>&#8211;updateid</code>, or <code>builds</code> is required. The download subcommand supports the following options: </p>
<p> <code>&#8211;cves &lt;cves&gt;</code> A comma-separated list of CVEs that identify updates you would like to download. </p>
<p> <code>&#8211;updateid &lt;ids&gt;</code> A comman-separated list of update IDs you would like to download. </p>
<p> <code>&#8211;builds &lt;nvrs</code> A comma-separated list of NVRs that identify updates you would like to download. </p>
<p> <code>bodhi updates new [options] &lt;builds&gt;</code> Create a new bodhi update containing the builds, given as a comma separated list of NVRs. The <code>new</code> subcommand supports the following options: </p>
<p> <code>&#8211;type [security | bugfix | enhancement | newpackage]</code> The type of the new update. </p>
<p> <code>&#8211;notes &lt;text&gt;</code> The description of the update. </p>
<p> <code>&#8211;notes-file &lt;path&gt;</code> A path to a file containing a description of the update. </p>
<p> <code>&#8211;bugs &lt;bugs&gt;</code> A comma separated list of bugs to associate with this update. </p>
<p> <code>&#8211;close-bugs</code> If given, this flag will cause bodhi to close the referenced bugs automatically when the update reaches stable. </p>
<p> <code>&#8211;request [testing | stable | upush]</code> The repository requested for this update. </p>
<p> <code>&#8211;autokarma</code> Enable autokarma for this update. </p>
<p> <code>&#8211;stable-karma &lt;integer&gt;</code> Configure the stable karma threshold for the given value. </p>
<p> <code>&#8211;unstable-karma &lt;integer&gt;</code> Configure the unstable karma threshold for the given value. </p>
<p> <code>&#8211;suggest [logout | reboot]</code> Suggest that the user logout or reboot upon applying the update. </p>
<p> <code>&#8211;file &lt;path&gt;</code> A path to a file containing all the update details. </p>
<p> <code>bodhi updates query [options]</code> Query the bodhi server for updates. The <code>query</code> subcommand supports the following options: </p>
<p> <code>&#8211;updateid &lt;id&gt;</code> Query for the update given by id. </p>
<p> <code>&#8211;approved-since &lt;timestamp&gt;</code> Query for updates approved after the given timestamp. </p>
<p> <code>&#8211;modified-since &lt;timestamp&gt;</code> Query for updates modified after the given timestamp. </p>
<p> <code>&#8211;builds &lt;builds&gt;</code> Query for updates containing the given builds, given as a comma-separated list. </p>
<p> <code>&#8211;bugs &lt;bugs&gt;</code> Query for updates related to the given bugs, given as a comma-separated list. </p>
<p> <code>&#8211;critpath</code> Query for updates submitted for the critical path. </p>
<p> <code>&#8211;cves &lt;cves&gt;</code> Query for updates related to the given CVEs, given as a comma-separated list. </p>
<p> <code>&#8211;packages &lt;packages&gt;</code> Query for updates related to the given packages, given as a comma-separated list. </p>
<p> <code>&#8211;pushed</code> Query for updates that have been pushed. </p>
<p> <code>&#8211;pushed-since &lt;timestamp&gt;</code> Query for updates that have been pushed after the given timestamp. </p>
<p> <code>&#8211;releases &lt;releases&gt;</code> Query for updates related to a list of releases, given as a comma-separated list. </p>
<p> <code>&#8211;locked</code> Query for updates that are currently locked. </p>
<p> <code>&#8211;request [testing | stable | unpush]</code> Query for updates marked with the given request type. </p>
<p> <code>&#8211;submitted-since &lt;timestamp&gt;</code> Query for updates that were submitted since the given timestamp. </p>
<p> <code>&#8211;status [pending | testing | stable | obsolete | unpushed | processing]</code> Filter by status. </p>
<p> <code>&#8211;suggest [logout | reboot]</code> Filter for updates that suggest logout or reboot to the user. </p>
<p> <code>&#8211;type [newpackage | security | bugfix | enhancement]</code> Filter by update type. </p>
<p> <code>&#8211;user &lt;username&gt;</code> Filter for updates by the given username. </p>
<p> <code>bodhi updates request [options] &lt;update&gt; &lt;state&gt;</code> Request that the given update be changed to the given state. <code>update</code> should be given by update id, and <code>state</code> should be one of testing, stable, unpush, obsolete, or revoke.</p>
<h2>BUGS</h2>
<p> If you find bugs in bodhi (or in the mage page), please feel free to file a bug report or a pull request: </p>
<pre>
<a rel="nofollow" href="https://github.com/fedora-infra/bodhi">https://github.com/fedora-infra/bodhi</a>
</pre>
<h2>AUTHOR</h2>
<p> Randy Barlow, Luke Macken</p>
<h2>COPYRIGHT</h2>
<p> 2007-2017, Red Hat, Inc. </p>
<h2>Index</h2>
