---
title: "sudo_root(8)"
name: "sudo_root"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sudo_root/"
description: "sudo_root – How to run administrative commands"
---

<p>sudo_root &#8211; How to run administrative commands</p>
<h2>Synopsis</h2>
<p><code>sudo</code> <i>command</i> <code>sudo -i</code> </p>
<h2>Introduction</h2>
<p>By default, the password for the user &quot;root&quot; (the system administrator) is locked. This means you cannot login as root or use su. Instead, the installer will set up sudo to allow the user that is created during install to run all administrative commands. </p>
<p> This means that in the terminal you can use sudo for commands that require root privileges. All programs in the menu will use a graphical sudo to prompt for a password. When sudo asks for a password, it needs <code>your password, </code> this means that a root password is not needed. </p>
<p> To run a command which requires root privileges in a terminal, simply prepend <code>sudo</code> in front of it. To get an interactive root shell, use <code>sudo -i</code>.</p>
<h2>Allowing Other Users To Run Sudo</h2>
<p>By default, only the user who installed the system is permitted to run sudo. To add more administrators, i. e. users who can run sudo, you have to add these users to the group &#8216;sudo&#8217; by doing one of the following steps: </p>
<dl>
<dt>*</p>
<dd>In a shell, do </p>
<dl>
<dd><code>sudo adduser</code> <i>username</i> <code>sudo</code></dl>
<dt>*</p>
<dd>Use the graphical &quot;Users &amp; Groups&quot; program in the &quot;System settings&quot; menu to add the new user to the <code>sudo</code> group. </p>
</dl>
<h2>Benefits Of Using Sudo</h2>
<p>The benefits of leaving root disabled by default include the following: </p>
<dl>
<dt>*</p>
<dd>Users do not have to remember an extra password, which they are likely to forget.</p>
<dt>*</p>
<dd>The installer is able to ask fewer questions.</p>
<dt>*</p>
<dd>It avoids the &quot;I can do anything&quot; interactive login by default &#8211; you will be prompted for a password before major changes can happen, which should make you think about the consequences of what you are doing.</p>
<dt>*</p>
<dd>Sudo adds a log entry of the command(s) run (in <code>/var/log/auth.log</code>).</p>
<dt>*</p>
<dd>Every attacker trying to brute-force their way into your box will know it has an account named root and will try that first. What they do not know is what the usernames of your other users are.</p>
<dt>*</p>
<dd>Allows easy transfer for admin rights, in a short term or long term period, by adding and removing users from the sudo group, while not compromising the root account.</p>
<dt>*</p>
<dd>sudo can be set up with a much more fine-grained security policy.</p>
<dt>*</p>
<dd>On systems with more than one administrator using sudo avoids sharing a password amongst them. </p>
</dl>
<h2>Downsides Of Using Sudo</h2>
<p>Although for desktops the benefits of using sudo are great, there are possible issues which need to be noted: </p>
<dl>
<dt>*</p>
<dd>Redirecting the output of commands run with sudo can be confusing at first. For instance consider </p>
<dl>
<dd><code>sudo ls &gt; /root/somefile</code></dl>
<dl>
<dd>will not work since it is the shell that tries to write to that file. You can use</dl>
<dl>
<dd><code>ls | sudo tee /root/somefile</code></dl>
<dl>
<dd>to get the behaviour you want.</dl>
<dt>*</p>
<dd>In a lot of office environments the ONLY local user on a system is root. All other users are imported using NSS techniques such as nss-ldap. To setup a workstation, or fix it, in the case of a network failure where nss-ldap is broken, root is required. This tends to leave the system unusable. An extra local user, or an enabled root password is needed here. </p>
</dl>
<h2>Going Back To A Traditional Root Account</h2>
<p><code>This is not recommended!</code> </p>
<p> To enable the root account (i.e. set a password) use: </p>
<dl>
<dd><code>sudo passwd root</code></dl>
<p> Afterwards, edit the sudo configuration with <code>sudo visudo</code> and comment out the line </p>
<dl>
<dd>%sudo ALL=(ALL) ALL</dl>
<p> to disable sudo access to members of the sudo group.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8), <code><a rel="nofollow" href="https://wiki.ubuntu.com/RootSudo">https://wiki.ubuntu.com/RootSudo</a></code> </p>
