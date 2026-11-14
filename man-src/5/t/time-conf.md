---
title: "time-conf(5)"
name: "time-conf"
section: "5"
letter: "t"
url: "/docs/linux/man/5-time-conf/"
description: "time.conf – configuration file for the pam_time module"
---

<p>time.conf &#8211; configuration file for the pam_time module</p>
<h2>Description</h2>
<p>The pam_time PAM module does not authenticate the user, but instead it restricts access to a system and or specific applications at various times of the day and on specific days or over various terminal lines. This module can be configured to deny access to (individual) users based on their name, the time of day, the day of week, the service they are applying for and their terminal from which they are making their request. </p>
<p> For this module to function correctly there must be a correctly formatted /etc/security/time.conf file present. White spaces are ignored and lines maybe extended with &#8216;\&#8217; (escaped newlines). Text following a &#8216;#&#8217; is ignored to the end of the line. </p>
<p> The syntax of the lines is as follows: </p>
<p> <i>services</i>;<i>ttys</i>;<i>users</i>;<i>times</i> </p>
<p> In words, each rule occupies a line, terminated with a newline or the beginning of a comment; a &#8216;<code>#</code>&#8216;. It contains four fields separated with semicolons, &#8216;<code>;</code>&#8216;. </p>
<p> The first field, the <i>services</i> field, is a logic list of PAM service names that the rule applies to. </p>
<p> The second field, the <i>tty</i> field, is a logic list of terminal names that this rule applies to. </p>
<p> The third field, the <i>users</i> field, is a logic list of users or a netgroup of users to whom this rule applies. </p>
<p> A logic list namely means individual tokens that are optionally prefixed with &#8216;!&#8217; (logical not) and separated with &#8216;&amp;&#8217; (logical and) and &#8216;|&#8217; (logical or). </p>
<p> For these items the simple wildcard &#8216;*&#8217; may be used only once. With netgroups no wildcards or logic operators are allowed. </p>
<p> The <i>times</i> field is used to indicate the times at which this rule applies. The format here is a logic list of day/time-range entries. The days are specified by a sequence of two character entries, MoTuSa for example is Monday Tuesday and Saturday. Note that repeated days are unset MoMo = no day, and MoWk = all weekdays bar Monday. The two character combinations accepted are Mo Tu We Th Fr Sa Su Wk Wd Al, the last two being week-end days and all 7 days of the week respectively. As a final example, AlFr means all days except Friday. </p>
<p> Each day/time-range can be prefixed with a &#8216;!&#8217; to indicate &quot;anything but&quot;. The time-range part is two 24-hour times HHMM, separated by a hyphen, indicating the start and finish time (if the finish time is smaller than the start time it is deemed to apply on the following day). </p>
<p> For a rule to be active, ALL of service+ttys+users must be satisfied by the applying process. </p>
<p> Note, currently there is no daemon enforcing the end of a session. This needs to be remedied. </p>
<p> Poorly formatted rules are logged as errors using <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</p>
<h2>Examples</h2>
<p>These are some example lines which might be specified in /etc/security/time.conf. All users except for <i>root</i> are denied access to console-login at all times:</p>
<dl>
<dd>
<pre>login ; tty* &amp; !ttyp* ; !root ; !Al0000-2400</pre>
</dl>
<p> Games (configured to use PAM) are only to be accessed out of working hours. This rule does not apply to the user <i>waster</i>:</p>
<dl>
<dd>
<pre>games ; * ; !waster ; Wd0000-2400 | Wk1800-0800</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_time/">pam_time</a></code>(8), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_time was written by Andrew G. Morgan &lt;morgan [at] kernel.org&gt;.</p>
