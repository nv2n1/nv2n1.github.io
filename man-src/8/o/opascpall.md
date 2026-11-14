---
title: "opascpall(8)"
name: "opascpall"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opascpall/"
description: "opascpall (Linux) Copies files or directories from the current system to multiple hosts in the fabric. When copying large directory trees, use the -t option to improve performance. This option tars..."
---

<p>opascpall <code>(Linux)</code> Copies files or directories from the current system to multiple hosts in the fabric. When copying large directory trees, use the -t option to improve performance. This option tars and compresses the tree, transfers the resulting compressed tarball to each node, and untars it on each node. Use this tool for copying data files, operating system files, or applications to all the hosts (or a subset of hosts) within the fabric. <code>NOTE:</code> This tool can only copy from this system to a group of systems in the cluster. To copy from hosts in the cluster to this host, use opauploadall. user@ style syntax cannot be used when specifying filenames. </p>
<h2>Syntax</h2>
<p>opascpall [-p] [-r] [-f <i>hostfile</i>] [-h &#8216;<i>hosts</i>&#8216;] [-u <i>user</i>] source_file &#8230; dest_file opascpall -t [-p] [-f <i>hostfile</i>] [-h &#8216;<i>hosts</i>&#8216;] [-u <i>user</i>] [ <i>source_dir</i>[ <i>dest_dir</i>]]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text.</p>
<dt>-p</p>
<dd>Performs copy in parallel on all hosts.</p>
<dt>-r</p>
<dd>Performs recursive copy of directories.</p>
<dt>-t</p>
<dd>Performs optimized recursive copy of directories using tar. <i>dest_dir</i> is optional. If <i>dest_dir</i> is not specified, it defaults to the current directory name. If both <i>source_dir</i> and <i>dest_dir</i> are omitted, they both default to the current directory name. </p>
<dt>-h <i>hosts</i></p>
<dd>List of hosts to copy to.</p>
<dt>-f <i>hostfile</i></p>
<dd>File with hosts in cluster. Default is /etc/sysconfig/opa/hosts file.</p>
<dt>-u <i>user</i></p>
<dd>User to perform copy to. Default is current user code.</p>
<dt>
&nbsp;<wbr><i>source_file</i>&nbsp;<wbr></p>
<dd>Name of files to copy from this system, relative to the current directory. Multiple files may be listed.</p>
<dt>
&nbsp;<wbr><i>source_dir</i>&nbsp;<wbr></p>
<dd>Name of directory to copy from this system, relative to the current directory.</p>
<dt>
&nbsp;<wbr><i>dest_file</i>&nbsp;<wbr>or&nbsp;<wbr>&nbsp;<wbr><i>dest_dir</i>&nbsp;<wbr></p>
<dd>Name of the file or directory on the destination system to copy to, relative to the home directory of the specified user. An absolute path name may be specified.</dl>
<h2>Example</h2>
<p># copy a single file<br />
 opascpall MPI-PMB /root/MPI-PMB<br />
 # efficiently copy an entire directory tree<br />
 opascpall -t -p /usr/lib/opa-ff/src/mpi_apps /usr/lib/opa-ff/src/mpi_apps<br />
 # copy a group of files<br />
 opascpall a b c /root/tools/<br />
 # copy to an explitly specified set of hosts<br />
 opascpall -h &#8216;arwen elrond&#8217; a b c /root/tools<br />
 HOSTS=&#8217;arwen elrond&#8217; opascpall a b c /root/tools</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>HOSTS</code></p>
<dd>List of hosts; used if -h option not supplied. </p>
<dt><code>HOSTS_FILE</code></p>
<dd>File containing list of hosts; used in absence of -f and -h. </p>
<dt><code>FF_MAX_PARALLEL</code></p>
<dd>When the -p option is used, maximum concurrent operations are performed. </p>
</dl>
