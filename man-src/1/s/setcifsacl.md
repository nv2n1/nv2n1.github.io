---

title: "setcifsacl(1)"
name: "setcifsacl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setcifsacl/"
description: "setcifsacl – Userspace helper to alter an ACL in a security descriptor for Common Internet File System (CIFS)"
---

<dl>
<dt>
</dt><dd>setcifsacl [-v|-a|-D|-M|-S] &quot;{one or more ACEs}&quot; {file system object}</dd></dl>
<p> This tool is part of the cifs-utils suite. </p>
<p> setcifsacl is a userspace helper program for the Linux CIFS client file system. It is intended to alter an ACL of a security descriptor for a file system object. Whether a security descriptor to be set is applied or not is determined by the CIFS/SMB server. </p>
<p> This program uses a plugin to handle the mapping of user and group names to SIDs. <code>/etc/cifs-utils/idmap-plugin</code> should be a symlink that points to the correct plugin to use.</p>
<h2>OPTIONS</h2>
<p> -h</p>
<dl>
<dt>
</dt><dd> Print usage message and exit.</dd></dl>
<p> -v</p>
<dl>
<dt>
</dt><dd> Print version number and exit.</dd></dl>
<p> -a</p>
<dl>
<dt>
</dt><dd> Add one or more ACEs to an ACL of a security descriptor. An ACE is added even if the same ACE exists in the ACL.</dd></dl>
<p> -D</p>
<dl>
<dt>
</dt><dd> Delete one or more ACEs from an ACL of a security descriptor. Entire ACE has to match in an existing ACL for the listed ACEs to be deleted.</dd></dl>
<p> -M</p>
<dl>
<dt>
</dt><dd> Modify one or more ACEs from an ACL of a security descriptor. SID and type are used to match for existing ACEs to be modified with the list of ACEs specified.</dd></dl>
<p> -S</p>
<dl>
<dt>
</dt><dd> Set an ACL of security descriptor with the list of ACEs Existing ACL is replaced entirely with the specified ACEs.</dd></dl>
<p> Every ACE entry starts with &quot;ACL:&quot; One or more ACEs are specified within double quotes. Multiple ACEs are separated by a comma. </p>
<p> Following fields of an ACE can be modified with possible values: </p>
<p> SID: Either a name or a raw SID value. </p>
<p> type: ALLOWED (0x0), DENIED (0x1), OBJECT_ALLOWED (0x5), OBJECT_DENIED (0x6) </p>
<p> flags: OBJECT_INHERIT_FLAG (OI or 0x1), CONTAINER_INHERIT_FLAG (CI or 0x2), NO_PROPAGATE_INHERIT_FLAG (NI or 0x4), INHERIT_ONLY_FLAG (IO or 0x8), INHERITED_ACE_FLAG (IA or 0x10) or a combination/OR of these values. </p>
<p> mask: Either one of FULL, CHANGE, READ, a combination of R W X D P O, or a hex value</p>
<h2>EXAMPLES</h2>
<p> Add an ACE<br />
 setcifsacl -a &quot;ACL:CIFSTESTDOM\user2:DENIED/0x1/D&quot; &lt;file_name&gt; setcifsacl -a &quot;ACL:CIFSTESTDOM\user1:ALLOWED/OI|CI|NI/D&quot; &lt;file_name&gt; </p>
<p> Delete an ACE <br />
 setcifsacl -D &quot;ACL:S-1-1-0:0x1/OI/0x1201ff&quot; &lt;file_name&gt; </p>
<p> Modify an ACE <br />
 setcifsacl -M &quot;ACL:CIFSTESTDOM\user1:ALLOWED/0x1f/CHANGE&quot; &lt;file_name&gt; </p>
<p> Set an ACL <br />
 setcifsacl -S &quot;ACL:CIFSTESTDOM\Administrator:0x0/0x0/FULL, <br />
 ACL:CIFSTESTDOM\user2:0x0/0x0/FULL&quot; &lt;file_name&gt; </p>
<h2>NOTES</h2>
<p> Kernel support for getcifsacl/setcifsacl utilities was initially introduced in the 2.6.37 kernel.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-mount.cifs/">mount.cifs</a></code>(8), <code><a href="/docs/linux/man/1-getcifsacl/">getcifsacl</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Shirish Pargaonkar wrote the setcifsacl program. </p>
<p> The Linux CIFS Mailing list is the preferred place to ask questions regarding these programs. </p>
