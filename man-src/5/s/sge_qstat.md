---
title: "sge_qstat(5)"
name: "sge_qstat"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_qstat/"
---

sge_qstat - xxQS_NAMExx default qstat file format

<h2>Description</h2>

<i>sge_qstat</i> defines the command line switches that will be used by qstat by default. If available, the default sge_qstat file is read and processed by 

 There is a cluster global and a user private sge_qstat file. The user private file has the highest precedence and is followed by the cluster global sge_qstat file. Command line switches used with override all switches contained in the user private or cluster global sge_qstat file. 

 The format of the default files is:
<dl><dt>&bull;
<dd>The default sge_qstat file may contain an arbitrary number of lines. Blank lines and lines with a '#' sign in the first column are skipped. Each line not to be skipped may contain any option. More than one option per line is allowed.</dl>

<h2>Examples</h2>

The following is a simple example of a default sge_qstat file: 

 <pre>=====================================================
# Just show me my own running and suspended jobs
-s rs -u $user
=====================================================</pre>Having defined a default sge_qstat file like this and using qstat as follows: 

 <pre>qstat </pre>has the same effect as if qstat was executed with: 

 <pre>qstat -s rs -u <i>current_user</i></pre>(Note that -u $USER is now the default behaviour.)

<h2>Files</h2>

<pre><i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/sge_qstat</i> global defaults file
<i>$HOME/.sge_qstat</i> user private defaults file</pre>

<h2>See Also</h2>



<h2>Copyright</h2>

See for a full statement of rights and permissions.
