---
title: "qtask(5)"
name: "qtask"
section: "5"
letter: "q"
url: "/docs/linux/man/5-qtask/"
---

qtask - file format of the qtask file.

<h2>Description</h2>

A <i>qtask</i> file defines which commands are submitted to xxQS_NAMExx for remote execution by The <i>qtask </i> file optionally may contain command-line parameters. These parameters are passed to the command being used by <i>qtcsh</i> to submit the commands. 

 Both a cluster global <i>qtask</i> file defining cluster wide defaults, and a user specific <i>qtask</i> file eventually overriding and enhancing those definitions, are supported. The cluster global file resides at &lt;xxqs_name_sxx_root&gt;/&lt;cell/common/qtask, while the user specific file can be found at ~/.qtask. An exclamation mark preceding command definitions in the cluster global file can be used by the administrator to deny overriding of such commands by users.

<h2>Format</h2>

The overall format of the <i>qtask</i> file is that of a tabulated list. Each line starting with a '#' character is a comment line. Each non-comment line defines a command to be started remotely. 

 Definition starts with the command name that must match exactly the name as typed in a command-line. Pathnames are not allowed in <i>qtask</i> files. Hence absolute or relative pathnames in command-lines always lead to local execution, even if the command itself is the same as defined in the <i>qtask</i> file. 

 The command name can be followed by an arbitrary number of option arguments which are passed on to by 

 An exclamation mark prefixing the command in the cluster global <i>qtask</i> file prevents overriding by the user supplied <i>qtask</i> file.

<h2>Examples</h2>

The following <i>qtask</i> file 

 <pre><dl><dt><dd>firefox -l a=sol-sparc64 -v DISPLAY=myhost:0
grep -l h=filesurfer
verilog -l veri_lic=1
</dl></pre>designates the applications firefox, grep and verilog for interactive remote execution through xxQS_NAMExx. Firefox is requested to run only on Solaris64 architectures with the DISPLAY environment variable set to 'myhost:0', grep only runs on the host named 'filesurfer', and verilog requests availability of a verilog license in order to get executed remotely.

<h2>See Also</h2>



<h2>Copyright</h2>

See for a full statement of rights and permissions.
