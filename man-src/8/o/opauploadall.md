---
title: "opauploadall(8)"
name: "opauploadall"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opauploadall/"
description: "opauploadall (Linux) Copies one or more files from a group of hosts to this system. Since the file name is the same on each host, a separate directory on this system is created for each host and th..."
---

<p>opauploadall <code>(Linux)</code> Copies one or more files from a group of hosts to this system. Since the file name is the same on each host, a separate directory on this system is created for each host and the file is copied to it. This is a convenient way to upload log files or configuration files for review. This tool can also be used in conjunction with opadownloadall to upload a host specific configuration file, edit it for each host, and download the new version to all the hosts. <code>NOTE:</code> To copy files from this host to hosts in the cluster, use opascpall or opadownloadall. user@ style syntax cannot be used when specifying filenames. </p>
<h2>Syntax</h2>
<p>opauploadall [-rp] [-f <i>hostfile</i>] [-d <i>upload_dir</i>] [-h &#8216;<i>hosts</i>&#8216;] [-u <i>user</i>] <i>source_file</i>&#8230; <i>dest_file</i></p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text.</p>
<dt>-p</p>
<dd>Performs copy in parallel on all hosts.</p>
<dt>-r</p>
<dd>Performs recursive upload of directories.</p>
<dt>-f <i>hostfile</i></p>
<dd>File with hosts in cluster. Default is /etc/sysconfig/opa/hosts file.</p>
<dt>-h <i>hosts</i></p>
<dd>List of hosts to upload from.</p>
<dt>-u <i>user</i></p>
<dd>User to perform copy to. Default is current user code.</p>
<dt>-d <i>upload_dir</i></p>
<dd>Directory to upload to. Default is uploads. If not specified, the environment variable <code>UPLOADS_DIR</code> is used. If that is not exported, the default, /uploads, is used.</p>
<dt>
&nbsp;<wbr><i>source_file</i>&nbsp;<wbr></p>
<dd>Name of files to copy to this system, relative to the current directory. Multiple files may be listed.</p>
<dt>
&nbsp;<wbr><i>dest_file</i>&nbsp;<wbr></p>
<dd>Name of the file or directory on this system to copy to. It is relative to <i>upload_dir</i>/<i>HOSTNAME</i> .A local directory within <i>upload_dir</i>/ is created for each host. Each uploaded file is copied to upload_dir/<i>HOSTNAME</i>/<i>dest_file</i> within the local system. If more than one source file is specified, dest_file is treated as a directory name.</dl>
<h2>Example</h2>
<p># upload two files from 2 hosts<br />
 opauploadall -h &#8216;arwen elrond&#8217; capture.tgz /etc/init.d/ipoib.cfg.<br />
 # upload two files from all hosts<br />
 opauploadall -p capture.tgz /etc/init.d/ipoib.cfg.<br />
 # upload network config files from all hosts<br />
 opauploadall capture.tgz /etc/init.d/ipoib.cfg pre-install</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>HOSTS</code></p>
<dd>List of hosts; used if -h option not supplied. </p>
<dt><code>HOSTS_FILE</code></p>
<dd>File containing list of hosts; used in absence of -f and -h. </p>
<dt><code>UPLOADS_DIR</code></p>
<dd>Directory to upload to, used in absence of -d. </p>
<dt><code>FF_MAX_PARALLEL</code></p>
<dd>When the -p option is used, maximum concurrent operations are performed. </p>
</dl>
