---
title: "opadownloadall(8)"
name: "opadownloadall"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opadownloadall/"
description: "opadownloadall (Linux) Copies one or more files to a group of hosts from a system. Since the file contents to copy may be different for each host, a separate directory on this system is used for th..."
---

<p>opadownloadall <code>(Linux)</code> Copies one or more files to a group of hosts from a system. Since the file contents to copy may be different for each host, a separate directory on this system is used for the source files for each host. This can also be used in conjunction with opauploadall to upload a host-specific configuration file, edit it for each host, and download the new version to all the hosts. <code>NOTE:</code> The tool opadownloadall can only copy from this system to a group of hosts in the cluster. To copy files from hosts in the cluster to this host, use opauploadall. </p>
<h2>Syntax</h2>
<p>opadownloadall [-rp] [-f <i>hostfile</i>] [-d <i>download_dir</i>] [-h &#8216;<i>HOSTS</i>&#8216;] [-u <i>user</i>] source_file &#8230; <i>dest_file</i></p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-p</p>
<dd>Performs copy in parallel on all hosts. </p>
<dt>-r</p>
<dd>Performs recursive download of directories. </p>
<dt>-f <i>hostfile</i></p>
<dd>File with hosts in cluster. The default is /etc/sysconfig/opa/hosts. </p>
<dt>-d <i>download_dir</i></p>
<dd>Directory to download files from. The default is downloads. If not specified, the environment variable <code>DOWNLOADS_DIR</code> is used. If that is not exported, the default is used. </p>
<dt>-h <i>HOSTS</i></p>
<dd>List of hosts to download files to. </p>
<dt>-u <i>user</i></p>
<dd>User to perform the copy. The default is the current user code. </p>
<dd></dl>
<p> <code>NOTE:</code> The user@ style syntax cannot be used in the arguments to opadownloadall. </p>
<dl>
<dt>
&nbsp;<wbr><i>source_file</i>&nbsp;<wbr></p>
<dd>The name of files to copy from the system. Multiple files may be listed. The option <i>source_file</i> is relative to <i>download_dir</i>/<i>hostname</i>. A local directory within <i>download_dir</i>/ must exist for each host being downloaded to. Each downloaded file is copied from <i>download_dir</i>/<i>hostname</i>/<i>source_file</i>. </p>
<dt>
&nbsp;<wbr><i>dest_file</i>&nbsp;<wbr></p>
<dd>The name of the file or directory on the destination hosts to copy to. </p>
<dd>If more than one source file is specified, <i>dest_file</i> is treated as a directory name. The given directory must already exist on the destination host. The copy fails for hosts where the directory does not exist.</dl>
<h2>Example</h2>
<p>opadownloadall -h &#8216;arwen elrond&#8217; irqbalance vncservers /etc/sysconfig<br />
 # Copies two files to 2 hosts </p>
<p> opadownloadall -p irqbalance vncservers /etc/sysconfig<br />
 # Copies two files to all hosts</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>HOSTS</code></p>
<dd>List of hosts; used if -h option not supplied. </p>
<dt><code>HOSTS_FILE</code></p>
<dd>File containing list of hosts; used in absence of -f and -h. </p>
<dt><code>FF_MAX_PARALLEL</code></p>
<dd>When the -p option is used, maximum concurrent operations are performed. </p>
<dt><code>DOWNLOADS_DIR</code></p>
<dd>Directory to download from, used in absence of -d. </p>
</dl>
