---
title: "pam_snapper(8)"
name: "pam_snapper"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_snapper/"
description: "pam_snapper – PAM module which creates filesystem snapshots via \"snapper\""
---

<p>pam_snapper &#8211; PAM module which creates filesystem snapshots via &quot;snapper&quot;</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_snapper.so</code> [debug] [homeprefix=<i>prefix</i>] [ignoreservices=<i>services</i>] [ignoreusers=<i>users</i>] [rootasroot] [ignoreroot] [openonly] [closeonly] [cleanup=<i>algorithm</i>]</dl>
<h2>Description</h2>
<dd>Create a snapshot at every login of a user, thus he or she always has a save starting point. </p>
<p> As many users do not logout for some time, it is a good idea to enable snapper&#8217;s time based snapshots in addition.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Switch on debugging in the module.</dl>
<p> <code>homeprefix=</code><i>prefix</i></p>
<dl>
<dd>Prefix for the name of the snapper configuration. The username will be appended to this prefix. </p>
<p> Default: &quot;home_&quot;</dl>
<p> <code>ignoreservices=</code><i>comma separated list of services</i></p>
<dl>
<dd>Default: &quot;crond&quot;</dl>
<p> <code>ignoreusers=</code><i>comma separated list of users</i></p>
<dl>
<dd>Default: (none)</dl>
<p> <code>rootasroot</code></p>
<dl>
<dd>Perform a snapshot using the snapper configuration &quot;root&quot; if the user &quot;root&quot; logs in. In other words: the homeprefix is not used in this case. As the snapper configuration &quot;root&quot; is used for the system (the root filesystem), this means that with every login of the user &quot;root&quot; the complete &quot;/&quot; filesystem will be snapshotted. This can be useful to help administrators rolling back in case their activity / configuration changes have been accidentally wrong. </p>
<p> &quot;rootasroot&quot; and &quot;ignoreroot&quot; are mutually exclusive.</dl>
<p> <code>ignoreroot</code></p>
<dl>
<dd>No snapshot is taken, if the user &quot;root&quot; opens/closes a session. </p>
<p> &quot;rootasroot&quot; and &quot;ignoreroot&quot; are mutually exclusive.</dl>
<p> <code>openonly</code></p>
<dl>
<dd>Only create a single snapshot when opening the PAM session. </p>
<p> Default: create pre- and post-snapshots</dl>
<p> <code>closeonly</code></p>
<dl>
<dd>Only create a single snapshot when closing the PAM session. </p>
<p> Default: create pre- and post-snapshots</dl>
<p> <code>cleanup=</code><i>cleanup-algorithm</i></p>
<dl>
<dd>Set snapper cleanup algorithm. </p>
<p> Default: (none)</dl>
<h2>Module Types Provided</h2>
<p>Only the module type &quot;session&quot; is provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>pam_snapper will always return PAM_SUCCESS, to not prevent users from login, in case a snapshot fails. This may change in the future.</dl>
<h2>Examples</h2>
<h3>Basic usage</h3>
<dl>
<dd>1. Create a btrfs subvolume for the new user and a snapper configuration, e.g. using the tool /usr/lib/pam_snapper/pam_snapper_useradd.sh.</dl>
<dl>
<dd>2. Add the following line to /etc/pam.d/common-session:</p>
<dl>
<dd>
<pre>session optional pam_snapper.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-snapper/">snapper</a></code>(8), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8), pam_snapper_homeconvert, pam_snapper_pamconfig, pam_snapper_useradd, pam_snapper_userdel</p>
<h2>Homepage</h2>
<p>m[blue]<code><a rel="nofollow" href="http://snapper.io/">http://snapper.io/</a></code>m[]</p>
<h2>Authors</h2>
<p>pam-snapper was written by Matthias G. Eckermann &lt;mge [at] suse.com&gt; as part of SUSE Hackweek#9 in April 2013. </p>
<p> This module would not have been possible without the work of Arvin Schnell on the snapper project. pam-snapper inherits DBUS handling from &quot;snapper_dbus_cli.c&quot; by David Disseldorp. </p>
<p> The module builds on the Linux PAM stack and its documentation, written by Thorsten Kukuk.</p>
<h2>License</h2>
<p>Copyright (c) 2013 SUSE </p>
<p> All Rights Reserved. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of version 2 of the GNU General Public License as published by the Free Software Foundation. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, contact SUSE. </p>
<p> To contact SUSE about this file by physical or electronic mail, you may find current contact information at <a rel="nofollow" href="http://www.suse.com">www.suse.com</a>.</p>
