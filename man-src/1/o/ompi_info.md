---
title: "ompi_info(1)"
name: "ompi_info"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ompi_info/"
description: "ompi_info – Display information about the Open MPI installation"
---

<h2 class="name">NAME</h2>
<p> ompi_info &#8211; Display information about the Open MPI installation </p>
<h2>SYNOPSIS</h2>
<p> <code>ompi_info [options]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>ompi_info</code> provides detailed information about the Open MPI installation. It can be useful for at least three common scenarios: </p>
<p> 1. Checking local configuration and seeing how Open MPI was installed. </p>
<p> 2. Submitting bug reports / help requests to the Open MPI community (see <i><a rel="nofollow" href="http://www.open-mpi.org/community/help/">http://www.open-mpi.org/community/help/</a></i>) </p>
<p> 3. Seeing a list of installed Open MPI plugins and querying what MCA parameters they support. </p>
<p> <code>NOTE:</code> <code>ompi_info</code> defaults to only showing a few MCA parameters by default (i.e., level 1 parameters). Use the <code>&#8211;level</code> option to enable showing more options (see the LEVELS section for more information).</p>
<h2>OPTIONS</h2>
<p> <code>ompi_info</code> accepts the following options:</p>
<dl>
<dt><i>-a|&#8211;all</i></p>
<dd> Show all configuration options and MCA parameters. Also changes the default MCA parameter level to 9, unless <i>&#8211;level</i> is also specified.</p>
<dt><i>&#8211;arch</i></p>
<dd> Show architecture on which Open MPI was compiled.</p>
<dt><i>-c|&#8211;config</i></p>
<dd> Show configuration options</p>
<dt><i>-gmca|&#8211;gmca &lt;param&gt; &lt;value&gt;</i></p>
<dd> Pass global MCA parameters that are applicable to all contexts.</p>
<dt><i>-h|&#8211;help</i></p>
<dd> Shows help / usage message.</p>
<dt><i>&#8211;hostname</i></p>
<dd> Show the hostname on which Open MPI was configured and built.</p>
<dt><i>&#8211;internal</i></p>
<dd> Show internal MCA parameters (not meant to be modified by users).</p>
<dt><i>&#8211;level &lt;level&gt;</i></p>
<dd> Show only variables with at most this level (1-9). The default is 1 unless &#8211;all is specified without &#8211;level, in which case the default is 9. See the LEVELS section for more information.</p>
<dt><i>-mca|&#8211;mca &lt;param&gt; &lt;value&gt;</i></p>
<dd> Pass context-specific MCA parameters; they are considered global if &#8211;gmca is not used and only one context is specified.</p>
<dt><i>&#8211;param &lt;type&gt; &lt;component&gt;</i></p>
<dd> Show MCA parameters. The first parameter is the type of the component to display; the second parameter is the specific component to display (or the keyword &quot;all&quot;, meaning &quot;display all components of this type&quot;).</p>
<dt><i>-t|&#8211;type</i></p>
<dd> Show MCA parameters of the type specified in the parameter. Accepts the following parameters: unsigned_int, unsigned_long, unsigned_long_long, size_t, string, version_string, bool, double. By default level is 1 unless it is specified with &#8211;level.</p>
<dt><i>&#8211;parsable</i></p>
<dd> When used in conjunction with other parameters, the output is displayed in a machine-parsable format <i>&#8211;parseable</i> Synonym for &#8211;parsable</p>
<dt><i>&#8211;path &lt;type&gt;</i></p>
<dd> Show paths that Open MPI was configured with. Accepts the following parameters: prefix, bindir, libdir, incdir, pkglibdir, sysconfdir.</p>
<dt><i>&#8211;pretty</i></p>
<dd> When used in conjunction with other parameters, the output is displayed in &#8216;prettyprint&#8217; format (default)</p>
<dt><i>&#8211;selected-only</i></p>
<dd> Show only variables from selected components.</p>
<dt><i>-V|&#8211;version</i></p>
<dd> Show version of Open MPI.</dl>
<h2>LEVELS</h2>
<p> Open MPI has many, many run-time tunable parameters (called &quot;MCA parameters&quot;), and usually only a handfull of them are useful to a given user. </p>
<p> As such, Open MPI has divided these parameters up into nine distinct levels, broken down into three categories, each with three sub-categories. </p>
<p> Note that since each MCA parameter is accessible through the MPI_T control variable API (introduced in MPI-3.0), these levels exactly correspond to the nine MPI_T cvar levels. </p>
<p> The three categories are:</p>
<dl>
<dt><code>End user</code></p>
<dd> Generally, these are parameters that are required for correctness, meaning that a user may need to set these just to get their MPI application to run correctly. For example, BTL &quot;if_include&quot; and &quot;if_exclude&quot; parameters fit into this category.</p>
<dt><code>Application tuner</code></p>
<dd> Generally, these are parameters that can be used to tweak MPI application performance. This even includes parameters that control resource exhaustion levels (e.g., number of free list entries, size of buffers, etc.), and could be considered &quot;correctness&quot; parameters if they&#8217;re set too low. But, really &#8212; they&#8217;re tuning parameters.</p>
<dt><code>Open MPI developer</code></p>
<dd> Parameters in this category either don&#8217;t fit in the other two, or are specifically intended for debugging / development of Open MPI itself.</dl>
<p> And within each category, there are three sub-categories:</p>
<dl>
<dt><code>Basic</code></p>
<dd> This sub-category is for parameters that everyone in this category will want to see &#8212; even less-advanced end users, application tuners, and new OMPI developers.</p>
<dt><code>Detailed</code></p>
<dd> This sub-category is for parameters that are generally useful, but users probably won&#8217;t need to change them often.</p>
<dt><code>All</code></p>
<dd> This sub-category is for all other parameters. Such parameters are likely fairly esoteric.</dl>
<p> Combining the categories and sub-categories, here&#8217;s how Open MPI defines all nine levels:</p>
<dl>
<dt>1</p>
<dd> Basic information of interest to end users.</p>
<dt>2</p>
<dd> Detailed information of interest to end users.</p>
<dt>3</p>
<dd> All remaining information of interest to end users.</p>
<dt>4</p>
<dd> Basic information required for application tuners.</p>
<dt>5</p>
<dd> Detailed information required for application tuners.</p>
<dt>6</p>
<dd> All remaining information required for application tuners.</p>
<dt>7</p>
<dd> Basic information for Open MPI implementors.</p>
<dt>8</p>
<dd> Detailed information for Open MPI implementors.</p>
<dt>9</p>
<dd> All remaining information for Open MPI implementors.</dl>
<p> By default, <code>ompi_info</code> only shows level 1 MCA parameters. To see more MCA parameters, use the <code>&#8211;level</code> command line option. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>ompi_info</p>
<dd> Show the default output of options and listing of installed components in a human-readable / prettyprint format.</p>
<dt>ompi_info &#8211;parsable</p>
<dd> Show the default output of options and listing of installed components in a machine-parsable format.</p>
<dt>ompi_info &#8211;param btl tcp</p>
<dd> Show the level 1 MCA parameters of the &quot;tcp&quot; BTL component in a human-readable / prettyprint format.</p>
<dt>ompi_info &#8211;param btl tcp &#8211;level 6</p>
<dd> Show the level 1 through level 6 MCA parameters of the &quot;tcp&quot; BTL component in a human-readable / prettyprint format.</p>
<dt>ompi_info &#8211;param btl tcp &#8211;parsable</p>
<dd> Show the level 1 MCA parameters of the &quot;tcp&quot; BTL component in a machine-parsable format.</p>
<dt>ompi_info &#8211;type string &#8211;pretty-print &#8211;level 3</p>
<dd> Show the level 3 MCA parameters of string type in a human-readable / prettyprint format.</p>
<dt>ompi_info &#8211;path bindir</p>
<dd> Show the &quot;bindir&quot; that Open MPI was configured with.</p>
<dt>ompi_info &#8211;version</p>
<dd> Show the version of Open MPI version numbers in a prettyprint format.</p>
<dt>ompi_info &#8211;all</p>
<dd> Show <i>all</i> information about the Open MPI installation, including all components that can be found, all the MCA parameters that they support (i.e., levels 1 through 9), versions of Open MPI and the components, etc.</dl>
<h2>AUTHORS</h2>
<p> The Open MPI maintainers &#8212; see <i><a rel="nofollow" href="http://www.openmpi.org/">http://www.openmpi.org/</a></i> or the file <i>AUTHORS</i>. </p>
<p> This manual page was originally contributed by Dirk Eddelbuettel &lt;edd [at] debian.org&gt;, one of the Debian GNU/Linux maintainers for Open MPI, and may be used by others. </p>
<h2>Index</h2>
