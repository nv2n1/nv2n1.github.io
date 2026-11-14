---
title: "pam_ssh_agent_auth(8)"
name: "pam_ssh_agent_auth"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_ssh_agent_auth/"
---

pam_ssh_agent_auth - PAM module for granting permissions based on SSH agent requests

<h2>Description</h2>

This module provides authentication via ssh-agent. If an ssh-agent listening at <font SIZE="-1">SSH_AUTH_SOCK</font> can successfully authenticate that it has the secret key for a public key in the specified file, authentication is granted, otherwise authentication fails.

<h2>Configuration</h2>

<dl><dt>/etc/pam.d/sudo: auth<tt>&nbsp;<wbr></tt>sufficient<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>pam_ssh_agent_auth.so file=/etc/security/authorized_keys
<dd><dt>/etc/sudoers:
<dd>In older versions of sudo (&lt; 1.8.5) it was necessary to set: 
&nbsp;<wbr>Defaults&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>env_keep&nbsp;<wbr>+=&nbsp;<wbr>``<font SIZE="-1">SSH_AUTH_SOCK''</font></dl>
 

 This configuration would permit anyone who has an <font SIZE="-1">SSH_AUTH_SOCK</font> that manages the private key matching a public key in /etc/security/authorized_keys to execute sudo without having to enter a password. Note that the ssh-agent listening to <font SIZE="-1">SSH_AUTH_SOCK</font> can either be local, or forwarded. 

 Unlike <font SIZE="-1">NOPASSWD,</font> this still requires an authentication, it's just that the authentication is provided by ssh-agent, and not password entry.

<h2>Arguments</h2>

<dl><dt>file=&lt;path to authorized_keys&gt;
<dd>Specify the path to the authorized_keys file(s) you would like to use for authentication. Subject to tilde and % <font SIZE="-1">EXPANSIONS </font>(below)
<dt>allow_user_owned_authorized_keys_file
<dd>A flag which enables authorized_keys files to be owned by the invoking user, instead of root. This flag is enabled automatically whenever the expansions <tt>%h</tt> or ~ are used.
<dt>authorized_keys_command=&lt;path to executable&gt;
<dd>Specify an external command to run, which should take a single argument, the username of the person being authenticated, and emit to its stdout a file in authorized_keys format. This is ideally suited for use with sssd's sss_ssh_authorizedkeys, for authenticating users via authorized_keys stored in ldap or other sssd supported security service.
<dt>authorized_keys_command_user=&lt;username&gt;
<dd>Specify a user to run the authorized_keys_command as. If this option is not specified, the authorized_keys_command will be run as the user being authenticated.
<dt>debug
<dd>A flag which enables verbose logging
<dt>sudo_service_name=&lt;service name you compiled sudo to use&gt;
<dd>(when compiled with --enable-sudo-hack) 

 Specify the service name to use to identify the service ``sudo''. When the <font SIZE="-1">PAM_SERVICE</font> identifier matches this string, and if <font SIZE="-1">PAM_RUSER</font> is not set, pam_ssh_agent_auth will attempt to identify the calling user from the environment variable <font SIZE="-1">SUDO_USER. </font> 

 This defaults to ``sudo''.</dl>

<h2>Expansions</h2>

<dl><dt>~ --- same as in shells, a user's Home directory
<dd>Automatically enables allow_user_owned_authorized_keys_file if used in the context of ~/. If used as ~user/, it would expect the file to be owned by 'user', unless you explicitely set allow_user_owned_authorized_keys_file
<dt>%h --- User's Home directory
<dd>Automatically enables allow_user_owned_authorized_keys_file
<dt>%H --- The short-hostname
<dd><dt>%u --- Username
<dd><dt>%f --- <font SIZE="-1">FQDN</font>
<dd></dl>

<h2>Examples</h2>

in /etc/pam.d/sudo
<dl><dt>&quot;auth sufficient pam_ssh_agent_auth.so file=~/.ssh/authorized_keys&quot;
<dd>The default .ssh/authorized_keys file in a user's home-directory
<dt>&quot;auth sufficient pam_ssh_agent_auth.so file=%h/.ssh/authorized_keys&quot;
<dd>Same as above.
<dt>&quot;auth sufficient pam_ssh_agent_auth.so file=~fred/.ssh/authorized_keys&quot;
<dd>If the home-directory of user 'fred' was /home/fred, this would expand to /home/fred/.ssh/authorized_keys. In this case, we have not specified allow_user_owned_authorized_keys_file, so this file must be owned by 'fred'.
<dt>&quot;auth sufficient pam_ssh_agent_auth.so file=/secure/%H/%u/authorized_keys allow_user_owned_authorized_keys_file&quot;
<dd>On a host named foobar.baz.com, and a user named fred, would expand to /secure/foobar/fred/authorized_keys. In this case, we specified allow_user_owned_authorized_keys_file, so fred would be able to manage that authorized_keys file himself.
<dt>&quot;auth sufficient pam_ssh_agent_auth.so file=/secure/%f/%u/authorized_keys&quot;
<dd>On a host named foobar.baz.com, and a user named fred, would expand to /secure/foobar.baz.com/fred/authorized_keys. In this case, we have not specified allow_user_owned_authorized_keys_file, so this file must be owned by root.</dl>

<h2>Copyright</h2>

<pre> Copyright (c) 2008-2014, Jamie Beverly.
 And is based on openssh, and the included works by Markus Friedl, Darren Tucker,
 Todd C. Miller, Ben Lindstrom, Tim Rice, Damien Miller, and many others.
 All rights reserved.
 See sources for complete attributions.
 
 Redistribution and use in source and binary forms, with or without modification, are
 permitted provided that the following conditions are met:
 1. Redistributions of source code must retain the above copyright notice, this list of
 conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright notice, this list
 of conditions and the following disclaimer in the documentation and/or other materials
 provided with the distribution.
 THIS SOFTWARE IS PROVIDED BY Jamie Beverly ``AS IS'' AND ANY EXPRESS OR IMPLIED
 WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
 FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Jamie Beverly OR
 CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
 ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
 ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</pre>
