---
title: "snapper-configs(5)"
name: "snapper-configs"
section: "5"
letter: "s"
url: "/docs/linux/man/5-snapper-configs/"
description: "snapper-configs – Configuration files for snapper configs"
---

<p>snapper-configs &#8211; Configuration files for snapper configs</p>
<h2>Description</h2>
<p>Each file /etc/snapper/configs/* describes a snapper config.</p>
<h2>Variables</h2>
<p>The following is a list of variables that can be present in the configuration file. Boolean values must be &quot;yes&quot; or &quot;no&quot;. </p>
<p> <code>SUBVOLUME=</code><i>path</i></p>
<dl>
<dd>Path of the subvolume or mount point. </p>
<p> There is no default value. The value must always be specified.</dl>
<p> <code>FSTYPE=</code><i>value</i></p>
<dl>
<dd>Filesystem type for the subvolume. </p>
<p> Default value is &quot;btrfs&quot; but it&#8217;s recommended to always specify the filesystem type.</dl>
<p> <code>ALLOW_USERS=</code><i>users</i></p>
<dl>
<dd>List of users allowed to operate with the config. The user-names must be separated by spaces. Spaces in usernames can be escaped with a &quot;\&quot;. </p>
<p> Also see the PERMISSONS section in <code><a href="/docs/linux/man/8-snapper/">snapper</a></code>(8). </p>
<p> Default value is &quot;&quot; but &quot;root&quot; is always implicitly included.</dl>
<p> <code>ALLOW_GROUPS=</code><i>groups</i></p>
<dl>
<dd>List of groups allowed to operate with the config. The group-names must be separated by spaces. Spaces in group-names can be escaped with a &quot;\&quot;. </p>
<p> Also see the PERMISSONS section in <code><a href="/docs/linux/man/8-snapper/">snapper</a></code>(8). </p>
<p> Default value is &quot;&quot;.</dl>
<p> <code>SYNC_ACL=</code><i>boolean</i></p>
<dl>
<dd>Defines whether snapper will sync the users and groups from ALLOW_USERS and ALLOW_GROUPS to the ACL of the .snapshots directory. </p>
<p> Also see the PERMISSONS section in <code><a href="/docs/linux/man/8-snapper/">snapper</a></code>(8). </p>
<p> Default value is &quot;no&quot;. </p>
<p> New in version 0.2.0.</dl>
<p> <code>BACKGROUND_COMPARISON=</code><i>boolean</i></p>
<dl>
<dd>Defines whether pre and post snapshots should be compared in the background after creation. </p>
<p> Default value is &quot;yes&quot;.</dl>
<p> <code>NUMBER_CLEANUP=</code><i>boolean</i></p>
<dl>
<dd>Defines whether the number cleanup algorithm should be run for the config. </p>
<p> Default value is &quot;no&quot;.</dl>
<p> <code>NUMBER_MIN_AGE=</code><i>seconds</i></p>
<dl>
<dd>Minimal age for snapshots to be deleted by the number cleanup algorithm. </p>
<p> Default value is &quot;1800&quot;.</dl>
<p> <code>NUMBER_LIMIT=</code><i>number</i></p>
<dl>
<dd>Defines how many snapshots the number cleanup algorithm should keep. The youngest snapshots will be kept. </p>
<p> Default value is &quot;50&quot;.</dl>
<p> <code>NUMBER_LIMIT_IMPORTANT=</code><i>number</i></p>
<dl>
<dd>Defines how many important snapshots the number cleanup algorithm should keep. Important snapshots have important=yes in the userdata. The youngest important snapshots will be kept. </p>
<p> The number of normal and important snapshots are counted independently. </p>
<p> Default value is &quot;10&quot;. </p>
<p> New in version 0.1.8.</dl>
<p> <code>TIMELINE_CREATE=</code><i>boolean</i></p>
<dl>
<dd>Defines whether hourly snapshots should be created. </p>
<p> Together with the timeline cleanup algorithm this will create a collection of snapshots with more snapshots is the near past and less snapshots in the far past. </p>
<p> Default value is &quot;no&quot;.</dl>
<p> <code>TIMELINE_CLEANUP=</code><i>boolean</i></p>
<dl>
<dd>Defines whether the timeline cleanup algorithm should be run for the config. </p>
<p> Default value is &quot;no&quot;.</dl>
<p> <code>TIMELINE_MIN_AGE=</code><i>seconds</i></p>
<dl>
<dd>Minimal age for snapshots to be deleted by the timeline cleanup algorithm. </p>
<p> Default value is &quot;1800&quot;.</dl>
<p> <code>TIMELINE_LIMIT_HOURLY=</code><i>number</i></p>
<dl>
<dd>Defines how many hourly snapshots the timeline cleanup algorithm should keep. An hourly snapshot is the first snapshot in an hour. The youngest hourly snapshots will be kept. </p>
<p> Default value is &quot;10&quot;.</dl>
<p> <code>TIMELINE_LIMIT_DAILY=</code><i>number</i></p>
<dl>
<dd>Defines how many daily snapshots the timeline cleanup algorithm should keep. A daily snapshot is the first snapshot in a day. The youngest daily snapshots will be kept. </p>
<p> Default value is &quot;10&quot;.</dl>
<p> <code>TIMELINE_LIMIT_WEEKLY=</code><i>number</i></p>
<dl>
<dd>Defines how many weekly snapshots the timeline cleanup algorithm should keep. A weekly snapshot is the first snapshot in a week. The youngest weekly snapshots will be kept. In compliance with ISO 8601 weeks start on Monday. </p>
<p> Default value is &quot;0&quot;.</dl>
<p> <code>TIMELINE_LIMIT_MONTHLY=</code><i>number</i></p>
<dl>
<dd>Defines how many monthly snapshots the timeline cleanup algorithm should keep. A monthly snapshot is the first snapshot in a month. The youngest monthly snapshots will be kept. </p>
<p> Default value is &quot;10&quot;.</dl>
<p> <code>TIMELINE_LIMIT_YEARLY=</code><i>number</i></p>
<dl>
<dd>Defines how many yearly snapshots the timeline cleanup algorithm should keep. A yearly snapshot is the first snapshot in a year. The youngest yearly snapshots will be kept. </p>
<p> Default value is &quot;10&quot;.</dl>
<p> <code>EMPTY_PRE_POST_CLEANUP=</code><i>boolean</i></p>
<dl>
<dd>Defines whether the empty-pre-post cleanup algorithm should be run for the config. </p>
<p> Default value is &quot;no&quot;.</dl>
<p> <code>EMPTY_PRE_POST_MIN_AGE=</code><i>seconds</i></p>
<dl>
<dd>Minimal age for snapshots to be deleted by the empty-pre-post cleanup algorithm. </p>
<p> Default value is &quot;1800&quot;.</dl>
<h2>Notes</h2>
<p>The default values stated here are the values snapper uses when the entry is missing in the configuration file. Some are not identical to the values from the configuration file template.</p>
<h2>Homepage</h2>
<p>m[blue]<code><a rel="nofollow" href="http://snapper.io/">http://snapper.io/</a></code>m[]</p>
<h2>Authors</h2>
<p>Arvin Schnell &lt;aschnell [at] suse.de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-snapper/">snapper</a></code>(8), <code><a href="/docs/linux/man/8-snapperd/">snapperd</a></code>(8) </p>
