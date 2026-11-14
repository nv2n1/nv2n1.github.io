---
title: "semanage-fcontext(8)"
name: "semanage-fcontext"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semanage-fcontext/"
description: "semanage-fcontext – SELinux Policy Management file context tool"
---

<p>semanage-fcontext &#8211; SELinux Policy Management file context tool </p>
<h2>Synopsis</h2>
<p><code>semanage fcontext [-h] [-n] [-N] [-S STORE] [ &#8211;add ( -t TYPE -f FTYPE -r RANGE -s SEUSER | -e EQUAL ) FILE_SPEC ) | &#8211;delete ( -t TYPE -f FTYPE | -e EQUAL ) FILE_SPEC ) | &#8211;deleteall | &#8211;extract | &#8211;list [-C] | &#8211;modify ( -t TYPE -f FTYPE -r RANGE -s SEUSER | -e EQUAL ) FILE_SPEC ) ]</code> </p>
<h2>Description</h2>
<p>semanage is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources. semanage fcontext is used to manage the default file system labeling on an SELinux system. This command maps file paths using regular expressions to SELinux labels. </p>
<h2>Options</h2>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd>show this help message and exit</p>
<dt><i>-n, &#8211;noheading</i></p>
<dd>Do not print heading when listing the specified object type</p>
<dt><i>-N, &#8211;noreload</i></p>
<dd>Do not reload policy after commit</p>
<dt><i>-C, &#8211;locallist</i></p>
<dd>List local customizations</p>
<dt><i>-S STORE, &#8211;store STORE</i></p>
<dd>Select an alternate SELinux Policy Store to manage</p>
<dt><i>-a, &#8211;add</i></p>
<dd>Add a record of the specified object type</p>
<dt><i>-d, &#8211;delete</i></p>
<dd>Delete a record of the specified object type</p>
<dt><i>-m, &#8211;modify</i></p>
<dd>Modify a record of the specified object type</p>
<dt><i>-l, &#8211;list</i></p>
<dd>List records of the specified object type</p>
<dt><i>-E, &#8211;extract</i></p>
<dd>Extract customizable commands, for use within a transaction</p>
<dt><i>-D, &#8211;deleteall</i></p>
<dd>Remove all local customizations</p>
<dt><i>-e EQUAL, &#8211;equal EQUAL</i></p>
<dd>Substitute target path with sourcepath when generating default label. This is used with fcontext. Requires source and target path arguments. The context labeling for the target subtree is made equivalent to that defined for the source.</p>
<dt><i>-f [{a,f,d,c,b,s,l,p}], &#8211;ftype [{a,f,d,c,b,s,l,p}]</i></p>
<dd>File Type. This is used with fcontext. Requires a file type as shown in the mode field by ls, e.g. use &#8216;d&#8217; to match only directories or &#8216;f&#8217; to match only regular files. The following file type options can be passed: f (regular file),d (directory),c (character device), b (block device),s (socket),l (symbolic link),p (named pipe). If you do not specify a file type, the file type will default to &quot;all files&quot;. </p>
<dt><i>-s SEUSER, &#8211;seuser SEUSER</i></p>
<dd>SELinux user name</p>
<dt><i>-t TYPE, &#8211;type TYPE</i></p>
<dd>SELinux Type for the object</p>
<dt><i>-r RANGE, &#8211;range RANGE</i></p>
<dd>MLS/MCS Security Range (MLS/MCS Systems only) SELinux Range for SELinux login mapping defaults to the SELinux user record range. SELinux Range for SELinux user defaults to s0. </p>
</dl>
<h2>Example</h2>
<pre><i>remember to run restorecon after you set the file context</i>
Add file-context for everything under /web
# semanage fcontext -a -t httpd_sys_content_t &quot;/web(/.*)?&quot;
# restorecon -R -v /web
Substitute /home1 with /home when setting file context
# semanage fcontext -a -e /home /home1
# restorecon -R -v /home1
For home directories under top level directory, for example /disk6/home,
execute the following commands.
# semanage fcontext -a -t home_root_t &quot;/disk6&quot;
# semanage fcontext -a -e /home /disk6/home
# restorecon -R -v /disk6</pre>
<h2>See Also</h2>
<p><code>selinux (8),</code> <code>semanage (8)</code> </p>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
