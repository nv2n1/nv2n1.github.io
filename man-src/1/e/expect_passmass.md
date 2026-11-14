---
title: "expect_passmass(1)"
name: "expect_passmass"
section: "1"
letter: "e"
url: "/docs/linux/man/1-expect_passmass/"
description: "passmass – change password on multiple machines"
---

<h2 class="name">NAME</h2>
<p> passmass &#8211; change password on multiple machines </p>
<h2>SYNOPSIS</h2>
<p> <code>passmass</code> [ <i>host1 host2 host3 &#8230;</i> ]</p>
<h2>INTRODUCTION</h2>
<p> <code>Passmass</code> changes a password on multiple machines. If you have accounts on several machines that do not share password databases, Passmass can help you keep them all in sync. This, in turn, will make it easier to change them more frequently. </p>
<p> When Passmass runs, it asks you for the old and new passwords. (If you are changing root passwords and have equivalencing, the old password is not used and may be omitted.) </p>
<p> Passmass understands the &quot;usual&quot; conventions. Additional arguments may be used for tuning. They affect all hosts which follow until another argument overrides it. For example, if you are known as &quot;libes&quot; on host1 and host2, but &quot;don&quot; on host3, you would say: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>passmass host1 host2 -user don host3</p>
<p> Arguments are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>-user</p>
<dd> User whose password will be changed. By default, the current user is used. </p>
<dt>-rlogin</p>
<dd> Use rlogin to access host. (default) </p>
<dt>-slogin</p>
<dd> Use slogin to access host. </p>
<dt>-ssh</p>
<dd> Use ssh to access host. </p>
<dt>-telnet</p>
<dd> Use telnet to access host. </p>
<dt>-program</p>
<dd>
<p> Next argument is a program to run to set the password. Default is &quot;passwd&quot;. Other common choices are &quot;yppasswd&quot; and &quot;set passwd&quot; (e.g., VMS hosts). A program name such as &quot;password fred&quot; can be used to create entries for new accounts (when run as root). </p>
<dt>-prompt</p>
<dd> Next argument is a prompt suffix pattern. This allows the script to know when the shell is prompting. The default is &quot;# &quot; for root and &quot;% &quot; for non-root accounts. </p>
<dt>-timeout</p>
<dd> Next argument is the number of seconds to wait for responses. Default is 30 but some systems can be much slower logging in. </p>
<dt>-su</p>
<dd>
<p> Next argument is 1 or 0. If 1, you are additionally prompted for a root password which is used to su after logging in. root&#8217;s password is changed rather than the user&#8217;s. This is useful for hosts which do not allow root to log in. </p>
</dl>
</dl>
<h2>HOW TO USE</h2>
<p> The best way to run Passmass is to put the command in a one-line shell script or alias. Whenever you get a new account on a new machine, add the appropriate arguments to the command. Then run it whenever you want to change your passwords on all the hosts. </p>
<h2>CAVEATS</h2>
<p> Using the same password on multiple hosts carries risks. In particular, if the password can be stolen, then all of your accounts are at risk. Thus, you should not use Passmass in situations where your password is visible, such as across a network which hackers are known to eavesdrop. </p>
<p> On the other hand, if you have enough accounts with different passwords, you may end up writing them down somewhere &#8211; and <i>that</i> can be a security problem. Funny story: my college roommate had an 11&quot;x13&quot; piece of paper on which he had listed accounts and passwords all across the Internet. This was several years worth of careful work and he carried it with him everywhere he went. Well one day, he forgot to remove it from his jeans, and we found a perfectly blank sheet of paper when we took out the wash the following day!</p>
<h2>SEE ALSO</h2>
<p> <i>&quot;Exploring Expect: A Tcl-Based Toolkit for Automating Interactive Programs&quot;</i> by Don Libes, O&#8217;Reilly and Associates, January 1995.</p>
<h2>AUTHOR</h2>
<p> Don Libes, National Institute of Standards and Technology </p>
<h2>Index</h2>
