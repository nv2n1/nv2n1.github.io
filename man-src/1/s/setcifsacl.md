---
title: "setcifsacl(1)"
name: "setcifsacl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setcifsacl/"
description: "setcifsacl – Userspace helper to alter an ACL in a security descriptor for Common Internet File System (CIFS)"
---

<h2 class="name">NAME</h2>
<p> setcifsacl &#8211; Userspace helper to alter an ACL in a security descriptor for Common Internet File System (CIFS) </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>setcifsacl [-v|-a|-D|-M|-S] &quot;{one or more ACEs}&quot; {file system object}</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the cifs-utils suite. </p>
<p> setcifsacl is a userspace helper program for the Linux CIFS client file system. It is intended to alter an ACL of a security descriptor for a file system object. Whether a security descriptor to be set is applied or not is determined by the CIFS/SMB server. </p>
<p> This program uses a plugin to handle the mapping of user and group names to SIDs. <code>/etc/cifs-utils/idmap-plugin</code> should be a symlink that points to the correct plugin to use.</p>
<h2>OPTIONS</h2>
<p> -h</p>
<dl>
<dt>
<dd> Print usage message and exit.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Print version number and exit.</dl>
<p> -a</p>
<dl>
<dt>
<dd> Add one or more ACEs to an ACL of a security descriptor. An ACE is added even if the same ACE exists in the ACL.</dl>
<p> -D</p>
<dl>
<dt>
<dd> Delete one or more ACEs from an ACL of a security descriptor. Entire ACE has to match in an existing ACL for the listed ACEs to be deleted.</dl>
<p> -M</p>
<dl>
<dt>
<dd> Modify one or more ACEs from an ACL of a security descriptor. SID and type are used to match for existing ACEs to be modified with the list of ACEs specified.</dl>
<p> -S</p>
<dl>
<dt>
<dd> Set an ACL of security descriptor with the list of ACEs Existing ACL is replaced entirely with the specified ACEs.</dl>
<p> Every ACE entry starts with &quot;ACL:&quot; One or more ACEs are specified within double quotes. Multiple ACEs are separated by a comma. </p>
<p> Following fields of an ACE can be modified with possible values: </p>
<p> SID: Either a name or a raw SID value. </p>
<p> type: ALLOWED (0x0), DENIED (0x1), OBJECT_ALLOWED (0x5), OBJECT_DENIED (0x6) </p>
<p> flags: OBJECT_INHERIT_FLAG (OI or 0x1), CONTAINER_INHERIT_FLAG (CI or 0x2), NO_PROPAGATE_INHERIT_FLAG (NI or 0x4), INHERIT_ONLY_FLAG (IO or 0x8), INHERITED_ACE_FLAG (IA or 0x10) or a combination/OR of these values. </p>
<p> mask: Either one of FULL, CHANGE, READ, a combination of R W X D P O, or a hex value</p>
<h2>EXAMPLES</h2>
<p> Add an ACE<br />
 setcifsacl -a &quot;ACL:CIFSTESTDOM
