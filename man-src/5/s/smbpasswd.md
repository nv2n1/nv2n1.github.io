---
title: "smbpasswd(5)"
name: "smbpasswd"
section: "5"
letter: "s"
url: "/docs/linux/man/5-smbpasswd/"
description: "smbpasswd – The Samba encrypted password file"
---

<p>smbpasswd &#8211; The Samba encrypted password file</p>
<h2>Synopsis</h2>
<p>smbpasswd</p>
<h2>Description</h2>
<p>This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> smbpasswd is the Samba encrypted password file. It contains the username, Unix user id and the SMB hashed passwords of the user, as well as account flag information and the time the password was last changed. This file format has been evolving with Samba and has had several different formats in the past.</p>
<h2>File Format</h2>
<p>The format of the smbpasswd file used by Samba 2.2 is very similar to the familiar Unix <a href="/docs/linux/man/5-passwd/">passwd</a>(5) file. It is an ASCII file containing one line for each user. Each field within each line is separated from the next by a colon. Any entry beginning with &#8216;#&#8217; is ignored. The smbpasswd file contains the following information for each user: </p>
<p> name</p>
<dl>
<dd>This is the user name. It must be a name that already exists in the standard UNIX passwd file.</dl>
<p> uid</p>
<dl>
<dd>This is the UNIX uid. It must match the uid field for the same user entry in the standard UNIX passwd file. If this does not match then Samba will refuse to recognize this smbpasswd file entry as being valid for a user.</dl>
<p> Lanman Password Hash</p>
<dl>
<dd>This is the LANMAN hash of the user&#8217;s password, encoded as 32 hex digits. The LANMAN hash is created by DES encrypting a well known string with the user&#8217;s password as the DES key. This is the same password used by Windows 95/98 machines. Note that this password hash is regarded as weak as it is vulnerable to dictionary attacks and if two users choose the same password this entry will be identical (i.e. the password is not &quot;salted&quot; as the UNIX password is). If the user has a null password this field will contain the characters &quot;NO PASSWORD&quot; as the start of the hex string. If the hex string is equal to 32 &#8216;X&#8217; characters then the user&#8217;s account is marked as <code>disabled</code> and the user will not be able to log onto the Samba server. </p>
<p> <i>WARNING !!</i> Note that, due to the challenge-response nature of the SMB/CIFS authentication protocol, anyone with a knowledge of this password hash will be able to impersonate the user on the network. For this reason these hashes are known as <i>plain text equivalents</i> and must <i>NOT</i> be made available to anyone but the root user. To protect these passwords the smbpasswd file is placed in a directory with read and traverse access only to the root user and the smbpasswd file itself must be set to be read/write only by root, with no other access.</dl>
<p> NT Password Hash</p>
<dl>
<dd>This is the Windows NT hash of the user&#8217;s password, encoded as 32 hex digits. The Windows NT hash is created by taking the user&#8217;s password as represented in 16-bit, little-endian UNICODE and then applying the MD4 (internet rfc1321) hashing algorithm to it. </p>
<p> This password hash is considered more secure than the LANMAN Password Hash as it preserves the case of the password and uses a much higher quality hashing algorithm. However, it is still the case that if two users choose the same password this entry will be identical (i.e. the password is not &quot;salted&quot; as the UNIX password is). </p>
<p> <i>WARNING !!</i>. Note that, due to the challenge-response nature of the SMB/CIFS authentication protocol, anyone with a knowledge of this password hash will be able to impersonate the user on the network. For this reason these hashes are known as <i>plain text equivalents</i> and must <i>NOT</i> be made available to anyone but the root user. To protect these passwords the smbpasswd file is placed in a directory with read and traverse access only to the root user and the smbpasswd file itself must be set to be read/write only by root, with no other access.</dl>
<p> Account Flags</p>
<dl>
<dd>This section contains flags that describe the attributes of the users account. This field is bracketed by &#8216;[&#8216; and &#8216;]&#8217; characters and is always 13 characters in length (including the &#8216;[&#8216; and &#8216;]&#8217; characters). The contents of this field may be any of the following characters:</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>U</i> &#8211; This means this is a &quot;User&quot; account, i.e. an ordinary user.</dl>
<dl>
<dd>&bull; <i>N</i> &#8211; This means the account has no password (the passwords in the fields LANMAN Password Hash and NT Password Hash are ignored). Note that this will only allow users to log on with no password if the <i> null passwords</i> parameter is set in the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) config file.</dl>
<dl>
<dd>&bull; <i>D</i> &#8211; This means the account is disabled and no SMB/CIFS logins will be allowed for this user.</dl>
<dl>
<dd>&bull; <i>X</i> &#8211; This means the password does not expire.</dl>
<dl>
<dd>&bull; <i>W</i> &#8211; This means this account is a &quot;Workstation Trust&quot; account. This kind of account is used in the Samba PDC code stream to allow Windows NT Workstations and Servers to join a Domain hosted by a Samba PDC.</dl>
</dl>
<p> Other flags may be added as the code is extended in future. The rest of this field space is filled in with spaces. For further information regarding the flags that are supported please refer to the man page for the pdbedit command.</dl>
<p> Last Change Time</p>
<dl>
<dd>This field consists of the time the account was last modified. It consists of the characters &#8216;LCT-&#8216; (standing for &quot;Last Change Time&quot;) followed by a numeric encoding of the UNIX time in seconds since the epoch (1970) that the last change was made.</dl>
<p> All other colon separated fields are ignored at this time.</p>
<h2>Version</h2>
<p>This man page is part of version 4.11.6-Ubuntu of the Samba suite.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-smbpasswd/">smbpasswd</a></code>(8), <code><a href="/docs/linux/man/7-samba/">Samba</a></code>(7), and the Internet RFC1321 for details on the MD4 algorithm.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
