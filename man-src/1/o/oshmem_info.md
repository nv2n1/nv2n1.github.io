---
title: "oshmem_info(1)"
name: "oshmem_info"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oshmem_info/"
description: "oshmem_info – Display information about the Open MPI installation"
---

<h2 class="name">NAME</h2>
<p> oshmem_info &#8211; Display information about the Open MPI installation </p>
<h2>SYNOPSIS</h2>
<p> <code>oshmem_info [options]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>oshmem_info</code> provides detailed information about the Open MPI/SHMEM installation. It can be useful for at least three common scenarios: </p>
<p> 1. Checking local configuration and seeing how Open MPI/SHMEM was installed. </p>
<p> 2. Submitting bug reports / help requests to the Open MPI/SHMEM community (see <i><a rel="nofollow" href="http://www.open-mpi.org/community/help/">http://www.open-mpi.org/community/help/</a></i>) </p>
<p> 3. Seeing a list of installed Open MPI/SHMEM plugins and querying what MCA parameters they support.</p>
<h2>OPTIONS</h2>
<p> <code>oshmem_info</code> accepts the following options:</p>
<dl>
<dt><i>-a|&#8211;all</i></p>
<dd> Show all configuration options and MCA parameters</p>
<dt><i>&#8211;arch</i></p>
<dd> Show architecture Open MPI/SHMEM was compiled on</p>
<dt><i>-c|&#8211;config</i></p>
<dd> Show configuration options</p>
<dt><i>-gmca|&#8211;gmca &lt;param&gt; &lt;value&gt;</i></p>
<dd> Pass global MCA parameters that are applicable to all contexts.</p>
<dt><i>-h|&#8211;help</i></p>
<dd> Shows help / usage message</p>
<dt><i>&#8211;hostname</i></p>
<dd> Show the hostname that Open MPI/SHMEM was configured and built on</p>
<dt><i>&#8211;internal</i></p>
<dd> Show internal MCA parameters (not meant to be modified by users)</p>
<dt><i>&#8211;level</i></p>
<dd> Show only variables with at most this level (1-9). The default is 1 unless &#8211;all is specified without &#8211;level in which case the default is 9. See the LEVEL section for more information.</p>
<dt><i>-mca|&#8211;mca &lt;param&gt; &lt;value&gt;</i></p>
<dd> Pass context-specific MCA parameters; they are considered global if &#8211;gmca is not used and only one context is specified.</p>
<dt><i>&#8211;param &lt;type&gt; &lt;component&gt;</i></p>
<dd> Show MCA parameters. The first parameter is the type of the component to display; the second parameter is the specific component to display (or the keyword &quot;all&quot;, meaning &quot;display all components of this type&quot;).</p>
<dt><i>&#8211;parsable</i></p>
<dd> When used in conjunction with other parameters, the output is displayed in a machine-parsable format <i>&#8211;parseable</i> Synonym for &#8211;parsable</p>
<dt><i>&#8211;path &lt;type&gt;</i></p>
<dd> Show paths that Open MPI/SHMEM was configured with. Accepts the following parameters: prefix, bindir, libdir, incdir, pkglibdir, sysconfdir.</p>
<dt><i>&#8211;pretty</i></p>
<dd> When used in conjunction with other parameters, the output is displayed in &#8216;prettyprint&#8217; format (default)</p>
<dt><i>&#8211;selected-only</i></p>
<dd> Show only variables from selected components.</p>
<dt><i>-V|&#8211;version</i></p>
<dd> Show version of Open MPI/SHMEM.</dl>
<h2>LEVELS</h2>
<dl>
<dt>1</p>
<dd> Basic information of interest to users</p>
<dt>2</p>
<dd> Detailed information of interest to users</p>
<dt>3</p>
<dd> All remaining information of interest to users</p>
<dt>4</p>
<dd> Basic information required for tuning</p>
<dt>5</p>
<dd> Detailed information required for tuning</p>
<dt>6</p>
<dd> All remaining information required for tuning</p>
<dt>7</p>
<dd> Basic information for MPI implementors</p>
<dt>8</p>
<dd> Detailed information for MPI implementors</p>
<dt>9</p>
<dd> All remaining information for MPI implementors</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>oshmem_info</p>
<dd> Show the default output of options and listing of installed components in a human-readable / prettyprint format.</p>
<dt>oshmem_info &#8211;parsable</p>
<dd> Show the default output of options and listing of installed components in a machine-parsable format.</p>
<dt>oshmem_info &#8211;param btl openib</p>
<dd> Show the MCA parameters of the &quot;openib&quot; BTL component in a human-readable / prettyprint format.</p>
<dt>oshmem_info &#8211;param btl openib &#8211;parsable</p>
<dd> Show the MCA parameters of the &quot;openib&quot; BTL component in a machine-parsable format.</p>
<dt>oshmem_info &#8211;path bindir</p>
<dd> Show the &quot;bindir&quot; that Open MPI was configured with.</p>
<dt>oshmem_info &#8211;version ompi full &#8211;parsable</p>
<dd> Show the full version numbers of Open MPI/SHMEM (including the ORTE and OPAL version numbers) in a machine-readable format.</p>
<dt>oshmem_info &#8211;version btl major</p>
<dd> Show the major version number of all BTL components in a prettyprint format.</p>
<dt>oshmem_info &#8211;version btl:tcp minor</p>
<dd> Show the minor version number of the TCP BTL component in a prettyprint format.</p>
<dt>oshmem_info &#8211;all</p>
<dd> Show <i>all</i> information about the Open MPI/SHMEM installation, including all components that can be found, the MCA parameters that they support, versions of Open MPI/SHMEM and the components, etc.</dl>
<h2>AUTHORS</h2>
<p> The Open MPI/SHMEM maintainers &#8212; see <i><a rel="nofollow" href="http://www.openmpi.org/">http://www.openmpi.org/</a></i> or the file <i>AUTHORS</i>. </p>
<p> This manual page was originally contributed by Dirk Eddelbuettel &lt;edd [at] debian.org&gt;, one of the Debian GNU/Linux maintainers for Open MPI, and may be used by others. </p>
<h2>Index</h2>
