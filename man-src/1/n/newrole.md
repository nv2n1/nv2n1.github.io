---
title: "newrole(1)"
name: "newrole"
section: "1"
letter: "n"
url: "/docs/linux/man/1-newrole/"
description: "newrole – run a shell with a new SELinux role"
---

<h2>NAME</h2>
<p> newrole &#8211; run a shell with a new SELinux role</p>
<h2>SYNOPSIS</h2>
<p> <code>newrole</code> [<code>-r</code>|<code>&#8211;role</code>] <i>ROLE</i> [<code>-t</code>|<code>&#8211;type</code>] <i>TYPE</i> [<code>-l</code>|<code>&#8211;level</code>] [<code>-p</code>|<code>&#8211;preserve-environment</code>] <i>LEVEL</i> [&#8211; [<i>ARGS</i>]&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Run a new shell in a new context. The new context is derived from the old context in which <code>newrole</code> is originally executed. If the <code>-r</code> or <code>&#8211;role</code> option is specified, then the new context will have the role specified by <i>ROLE</i>. If the <code>-t</code> or <code>&#8211;type</code> option is specified, then the new context will have the type (domain) specified by <i>TYPE</i>. If a role is specified, but no type is specified, the default type is derived from the specified role. If the <code>-l</code> or <code>&#8211;level</code> option is specified, then the new context will have the sensitivity level specified by <i>LEVEL</i>. If <i>LEVEL</i> is a range, the new context will have the sensitivity level and clearance specified by that range. If the <code>-p</code> or <code>&#8211;preserve-environment</code> option is specified, the shell with the new SELinux context will preserve environment variables, otherwise a new minimal enviroment is created. </p>
<p> Additional arguments <i>ARGS</i> may be provided after a &#8212; option, in which case they are supplied to the new shell. In particular, an argument of &#8212; -c will cause the next argument to be treated as a command by most command interpreters. </p>
<p> If a command argument is specified to newrole and the command name is found in /etc/selinux/newrole_pam.conf, then the pam service name listed in that file for the command will be used rather than the normal newrole pam configuration. This allows for per-command pam configuration when invoked via newrole, e.g. to skip the interactive re-authentication phase. </p>
<p> The new shell will be the shell specified in the user&#8217;s entry in the <i>/etc/passwd</i> file. </p>
<p> The <code>-V</code> or <code>&#8211;version</code> shows the current version of newrole </p>
<h2>EXAMPLE</h2>
<p> Changing role:<br />
#&nbsp;<wbr>id -Z<br />
staff_u:staff_r:staff_t:SystemLow-SystemHigh<br />
#&nbsp;<wbr>newrole -r sysadm_r<br />
#&nbsp;<wbr>id -Z<br />
staff_u:sysadm_r:sysadm_t:SystemLow-SystemHigh </p>
<p> Changing sensitivity only:<br />
#&nbsp;<wbr>id -Z<br />
staff_u:sysadm_r:sysadm_t:Unclassified-SystemHigh<br />
#&nbsp;<wbr>newrole -l Secret<br />
#&nbsp;<wbr>id -Z<br />
staff_u:sysadm_r:sysadm_t:Secret-SystemHigh </p>
<p> Changing sensitivity and clearance:<br />
#&nbsp;<wbr>id -Z<br />
staff_u:sysadm_r:sysadm_t:Unclassified-SystemHigh<br />
#&nbsp;<wbr>newrole -l Secret-Secret<br />
#&nbsp;<wbr>id -Z<br />
staff_u:sysadm_r:sysadm_t:Secret </p>
<p> Running a program in a given role or level:<br />
#&nbsp;<wbr>newrole -r sysadm_r &#8212; -c&nbsp;<wbr>&quot;/path/to/app arg1 arg2&#8230;&quot;<br />
#&nbsp;<wbr>newrole -l Secret &#8212; -c&nbsp;<wbr>&quot;/path/to/app arg1 arg2&#8230;&quot; </p>
<h2>FILES</h2>
<p> /etc/passwd &#8211; user account information<br />
 /etc/shadow &#8211; encrypted passwords and age information<br />
 /etc/selinux/&lt;policy&gt;/contexts/default_type &#8211; default types for roles<br />
 /etc/selinux/&lt;policy&gt;/contexts/securetty_types &#8211; securetty types for level changes<br />
 /etc/selinux/newrole_pam.conf &#8211; optional mapping of commands to separate pam service names </p>
<h2>SEE ALSO</h2>
<p> <code>runcon</code> (1)</p>
<h2>AUTHORS</h2>
<pre><code>
Anthony Colatrella
    Tim Fraser
        Steve Grubb&lt;sgrubb[at] redhat.com&gt;
            Darrel Goeddel&lt;DGoeddel[at] trustedcs.com&gt;
                Michael Thompson&lt;mcthomps[at] us.ibm.com&gt;
                    Dan Walsh&lt;dwalsh[at] redhat.com&gt;
</code></pre>
<h2>Index</h2>
