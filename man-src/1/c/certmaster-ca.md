---
title: "certmaster-ca(1)"
name: "certmaster-ca"
section: "1"
letter: "c"
url: "/docs/linux/man/1-certmaster-ca/"
---

<h2 class="name">NAME</h2>
 

 certmaster-ca -- signs certificate requests gathered by certmaster. 

<h2>SYNOPSIS</h2>

 certmaster-ca --list 

 certmaster-ca --sign machine.example.org

<h2>DESCRIPTION</h2>

 ``certmaster-ca --list'' 

 The list command prints all certificates that have been requested from certmaster by a remote application (such as funcd or certmaster-request) but are not yet signed. 

 ``certmaster-ca --sign [hostname]'' 

 This command is used to sign a certificate and send it back to the requester.

<h2>AUTO-SIGNING</h2>

 The certmaster can be configured to make this command unneccessary; all incoming requests can be signed automatically by certmaster. 

 To configure this, edit /etc/certmaster/certmaster.conf.

<h2>ADDITONAL RESOURCES</h2>

 See <a rel="nofollow" HREF="https://fedorahosted.org/certmaster.">https://fedorahosted.org/certmaster.</a> It's a Wiki. See also <a rel="nofollow" HREF="https://fedorahosted.org/func">https://fedorahosted.org/func</a> See also the manpages for ``certmaster'' and ``certmaster-request''.

<h2>AUTHOR</h2>

 Various. See <a rel="nofollow" HREF="https://fedorahosted.org/certmaster">https://fedorahosted.org/certmaster</a> and <a rel="nofollow" HREF="https://fedorahosted.org/func">https://fedorahosted.org/func</a> 

<h2>Index</h2>


