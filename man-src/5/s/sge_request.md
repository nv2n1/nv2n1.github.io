---
title: "sge_request(5)"
name: "sge_request"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_request/"
description: "xxqs_name_sxx_request – xxQS_NAMExx default request definition file format"
---

<p>xxqs_name_sxx_request &#8211; xxQS_NAMExx default request definition file format</p>
<h2>Description</h2>
<p><i>xxqs_name_sxx_request</i> reflects the format of the files defining default request profiles. These apply to and but for convenience, only qsub is mentioned below. If available, default request files are read and processed during job submission, before any submit options embedded in the job script, and before any options in the command-line are considered. Thus, the command-line and embedded script options may overwrite the settings in the default request files (see for details). However, where options may be repeated and accumulated, typically they are collected into a list from the various sources, which may not be what you want. </p>
<p> There is a cluster global, a user private, and a working directory local default request definition file. The working directory local default request file has the highest precedence and is followed by the user private and then the cluster global default request file. </p>
<p> <code>Note</code>, that the <i>-clear</i> option to can be used to discard any previous settings at any time in a default request file, in the embedded script flags or in a command-line option. </p>
<p> The format of the default request definition files is:</p>
<dl>
<dt>&bull;</p>
<dd>The default request files may contain an arbitrary number of lines. Blank lines, and lines with a &#8216;#&#8217; sign in the first column, are skipped.</p>
<dt>&bull;</p>
<dd>Each line not to be skipped may contain any option. More than one option per line is allowed. The batch script file and argument options to the batch script are not considered as options and thus are not allowed in a default request file.</dl>
<h2>Examples</h2>
<p>The following is a simple example of a default request definition file: </p>
<pre>=====================================================
# Default Requests File
# request group to be sun4 and a CPU-time of 5hr
-l arch=sun4,s_cpu=5:0:0
# don't restart the job in case of system crashes
-r n
=====================================================</pre>
<p>Having defined a default request definition file like this, submitting a job as follows: </p>
<pre>qsub test.sh</pre>
<p>would have precisely the same effect as if the job was submitted with: </p>
<pre>qsub -l arch=sun4,s_cpu=5:0:0 -r n test.sh</pre>
<h2>Files</h2>
<pre><i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/xxqs_name_sxx_request</i>
 global defaults file
<i>$HOME/.xxqs_name_sxx_request</i> user private defaults file
<i>$cwd/.xxqs_name_sxx_request</i> cwd directory defaults file</pre>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
