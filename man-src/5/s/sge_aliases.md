---
title: "sge_aliases(5)"
name: "sge_aliases"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_aliases/"
description: "xxqs_name_sxx_aliases – xxQS_NAMExx path aliases file format"
---

<p>xxqs_name_sxx_aliases &#8211; xxQS_NAMExx path aliases file format</p>
<h2>Description</h2>
<p>The xxQS_NAMExx path aliasing facility provides administrators and users with the means to reflect complicated and inhomogeneous file system structures in distributed environments (such as user home directories mounted under different paths on different hosts) and to ensure that xxQS_NAMExx is able to locate the appropriate working directories for executing batch jobs. </p>
<p> There is a system global path aliasing file and a user-local file. <i>xxqs_name_sxx_aliases</i> defines the format of both:</p>
<dl>
<dt>&bull;</p>
<dd>Blank lines, and lines with a &#8216;#&#8217; sign in the first column, are skipped.</p>
<dt>&bull;</p>
<dd>Each line other than a blank line or a line with a leading &#8216;#&#8217; has to contain four strings separated by any number of blanks or tabs.</p>
<dt>&bull;</p>
<dd>The first string specifies a source path, the second a submit host, the third an execution host, and the fourth the source path replacement.</p>
<dt>&bull;</p>
<dd>Both the submit and the execution host entries may consist of only a &#8216;*&#8217; sign which matches any host.</dl>
<p> If the<br />
&nbsp;<i>-cwd</i>&nbsp;flag is specified&nbsp;(and only if &#8211; otherwise the user&#8217;s home directory on the execution host is selected to execute the job), the path aliasing mechanism is activated, and the files are processed as follows:</p>
<dl>
<dt>&bull;</p>
<dd>After has retrieved the physical current working directory path, the cluster global path aliasing file is read, if present. The user path aliases file is read afterwards as if it were appended to the global file.</p>
<dt>&bull;</p>
<dd>Lines not to be skipped are read from the top of the file one by one while the translations specified by those lines are stored if necessary.</p>
<dt>&bull;</p>
<dd>A translation is stored only if the submit host entry matches the host is executed on and if the source path forms the initial part of either the current working directory or of the source path replacements already stored.</p>
<dt>&bull;</p>
<dd>As soon as both files are read the stored, path aliasing information is passed along with the submitted job.</p>
<dt>&bull;</p>
<dd>On the execution host, the aliasing information will be evaluated. The leading part of the current working directory will be replaced by the source-path replacement if the execution-host entry of the path alias matches the executing host. <code>Note:</code> The current working directory string will be changed in this case, and subsequent path aliases must match the replaced working directory path to be applied.</dl>
<h2>Examples</h2>
<p>The following is a simple example of a path aliasing file resolving problems with inhomogeneous paths if <i><a href="/docs/linux/man/8-automount/">automount</a></i>(8) is used: </p>
<pre>=====================================================
# Path Aliasing File
# src-path sub-host exec-host replacement
/tmp_mnt/ * * /
# replaces any occurrence of /tmp_mnt/ by /
# if submitting or executing on any host.
# Thus paths on nfs server and clients are the same
=====================================================</pre>
<h2>Files</h2>
<pre><i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/xxqs_name_sxx_aliases</i>
 global aliases file
<i>$HOME/.xxqs_name_sxx_aliases</i> user local aliases file</pre>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
