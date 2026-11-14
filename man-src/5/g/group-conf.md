---
title: "group-conf(5)"
name: "group-conf"
section: "5"
letter: "g"
url: "/docs/linux/man/5-group-conf/"
description: "group.conf – configuration file for the pam_group module"
---

<p>group.conf &#8211; configuration file for the pam_group module</p>
<h2>Description</h2>
<p>The pam_group PAM module does not authenticate the user, but instead it grants group memberships (in the credential setting phase of the authentication module) to the user. Such memberships are based on the service they are applying for. </p>
<p> For this module to function correctly there must be a correctly formatted /etc/security/group.conf file present. White spaces are ignored and lines maybe extended with &#8216;\&#8217; (escaped newlines). Text following a &#8216;#&#8217; is ignored to the end of the line. </p>
<p> The syntax of the lines is as follows: </p>
<p> <i>services</i>;<i>ttys</i>;<i>users</i>;<i>times</i>;<i>groups</i> </p>
<p> The first field, the <i>services</i> field, is a logic list of PAM service names that the rule applies to. </p>
<p> The second field, the <i>tty</i> field, is a logic list of terminal names that this rule applies to. </p>
<p> The third field, the <i>users</i> field, is a logic list of users, or a UNIX group, or a netgroup of users to whom this rule applies. Group names are preceded by a &#8216;%&#8217; symbol, while netgroup names are preceded by a &#8216;@&#8217; symbol. </p>
<p> A logic list namely means individual tokens that are optionally prefixed with &#8216;!&#8217; (logical not) and separated with &#8216;&amp;&#8217; (logical and) and &#8216;|&#8217; (logical or). </p>
<p> For these items the simple wildcard &#8216;*&#8217; may be used only once. With UNIX groups or netgroups no wildcards or logic operators are allowed. </p>
<p> The <i>times</i> field is used to indicate &quot;when&quot; these groups are to be given to the user. The format here is a logic list of day/time-range entries. The days are specified by a sequence of two character entries, MoTuSa for example is Monday Tuesday and Saturday. Note that repeated days are unset MoMo = no day, and MoWk = all weekdays bar Monday. The two character combinations accepted are Mo Tu We Th Fr Sa Su Wk Wd Al, the last two being week-end days and all 7 days of the week respectively. As a final example, AlFr means all days except Friday. </p>
<p> Each day/time-range can be prefixed with a &#8216;!&#8217; to indicate &quot;anything but&quot;. The time-range part is two 24-hour times HHMM, separated by a hyphen, indicating the start and finish time (if the finish time is smaller than the start time it is deemed to apply on the following day). </p>
<p> The <i>groups</i> field is a comma or space separated list of groups that the user inherits membership of. These groups are added if the previous fields are satisfied by the user&#8217;s request. </p>
<p> For a rule to be active, ALL of service+ttys+users must be satisfied by the applying process.</p>
<h2>Examples</h2>
<p>These are some example lines which might be specified in /etc/security/group.conf. </p>
<p> Running &#8216;xsh&#8217; on tty* (any ttyXXX device), the user &#8216;us&#8217; is given access to the floppy (through membership of the floppy group) </p>
<dl>
<dd>
<pre>xsh;tty*&amp;!ttyp*;us;Al0000-2400;floppy</pre>
</dl>
<p> Running &#8216;xsh&#8217; on tty* (any ttyXXX device), the users &#8216;sword&#8217;, &#8216;pike&#8217; and &#8216;shield&#8217; are given access to games (through membership of the floppy group) after work hours. </p>
<dl>
<dd>
<pre>xsh; tty* ;sword|pike|shield;!Wk0900-1800;games, sound
xsh; tty* ;*;Al0900-1800;floppy</pre>
</dl>
<p> Any member of the group &#8216;admin&#8217; running &#8216;xsh&#8217; on tty*, is granted access (at any time) to the group &#8216;plugdev&#8217; </p>
<dl>
<dd>
<pre>xsh; tty* ;%admin;Al0000-2400;plugdev</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_group/">pam_group</a></code>(8), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_group was written by Andrew G. Morgan &lt;morgan [at] kernel.org&gt;.</p>
