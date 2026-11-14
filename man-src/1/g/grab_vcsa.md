---
title: "grab_vcsa(1)"
name: "grab_vcsa"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grab_vcsa/"
description: "grab_vcsa – Linux console vcsa grabber"
---

<h2>NAME</h2>
<p> grab_vcsa &#8211; Linux console vcsa grabber </p>
<h2>SYNOPSIS</h2>
<p> <code>grab_vcsa</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>Linux</i> console allows text mode <i>video buffer access</i> (/dev/tty0..31) there exist two devices (/dev/vcs0..31) and (/dev/vcsa0..31). These devices are two different representations of the content of the console. </p>
<p> When you login on the Linux console, your tty device is changed owner to you, so you can read/write it. When you logout it is takes from you. This does not happen with the vcs and vcsa devices, i.e. you cannot access the video buffer of your own tty. </p>
<p> Unfortunately there is a lot of reason to use the text mode video buffer. For instance, it is not possible to get access to the full 256 characters the VGA adapter can display without using the text mode video buffer (Linux emulates the vt100 character set which does not have all VGA characters). This annoyance severely limits the porting possibilities to Linux of software that was written with a VGA character set in mind. </p>
<p> <code>grab_vcsa</code> is a setuid root program that, when called will change the owner of the vcs and vcsa devices to you, after a series of security checks have been performed. </p>
<p> It is not necessary to change the permissions back again (this would be pointless since a user could kill a imaginary release_vcsa program before it can do its work). The permissions are automatically reverted on logout. </p>
<p> <code>grab_vcsa</code> is used by the Free Pascal video unit. The video unit allows programmers to develop portable programs accross Dos, Linux, FreeBSD, Windows, OS/2 and other operating systems while they can still assume being able to use the full VGA character set. </p>
<h2>RETURN CODES</h2>
<p> <code>grab_vcsa</code> has the following return codes:</p>
<dl>
<dt><code>0</code></p>
<dd> Success</p>
<dt><code>1</code></p>
<dd> You are not running on the Linux console</p>
<dt><code>2</code></p>
<dd> Error while statting tty.</p>
<dt><code>3</code></p>
<dd> Error while executing chown.</p>
<dt><code>4</code></p>
<dd> Error while executing chmod.</p>
<dt><code>4</code></p>
<dd> You do not own your own tty. </p>
</dl>
<h2>AUTHOR</h2>
<p> Daniel Mantione &lt;daniel.mantione [at] freepascal.org&gt; </p>
<h2>Index</h2>
