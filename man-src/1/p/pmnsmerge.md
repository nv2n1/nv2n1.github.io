---
title: "pmnsmerge(1)"
name: "pmnsmerge"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmnsmerge/"
description: "pmnsmerge – merge multiple versions of a Performance Co-Pilot PMNS"
---

<h2>NAME</h2>
<p> <code>pmnsmerge</code> &#8211; merge multiple versions of a Performance Co-Pilot PMNS</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmnsmerge</code> [<code>-adfxv</code>] <i>infile</i> [&#8230;] <i>outfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmnsmerge</code> merges multiple instances of a Performance Metrics Name Space (PMNS), as used by the components of the Performance Co-Pilot (PCP). </p>
<p> Each <i>infile</i> argument names a file that includes the root of a PMNS, of the form </p>
<pre>
root {
    /* arbitrary stuff */
}
</pre>
<p> The order in which the <i>infile</i> files are processed is determined by the presence or absence of embedded control lines of the form #define _DATESTAMP YYYYMMDD </p>
<p> Files without a control line are processed first and in the order they appear on the command line. The other files are then processed in order of ascending <tt>_DATESTAMP</tt>. </p>
<p> The <code>-a</code> option suppresses the argument re-ordering and processes all files in the order they appear on the command line. </p>
<p> The merging proceeds by matching names in PMNS, only those <code>new</code> names in each PMNS are considered, and these are added after any existing metrics with the longest possible matching prefix in their names. For example, merging these two input PMNS </p>
<pre><code>
root
{
    root
    {
        surprise 1 : 1 : 3 mine 1 : 1 : 1 mine 1 : 1 : 1 foo foo
            yawn
                yours 1 : 1 : 2
    }
}
foo
{
    foo
    {
        fumble 1 : 2 : 1 mumble 1 : 2 : 3 stumble 1 : 2 : 2 stumble 1 : 2 : 2
    }
}
yawn
{
    sleepy 1 : 3 : 1
}
</code></pre>
<p> Produces the resulting PMNS in <i>out</i>. </p>
<pre><code>
root{
    mine 1 : 1 : 1 foo
        yours 1 : 1 : 2 surprise 1 : 1 : 3 yawn
}
foo{
    fumble 1 : 2 : 1 stumble 1 : 2 : 2 mumble 1 : 2 : 3
} yawn
{
    sleepy 1 : 3 : 1
}
</code></pre>
<p> To avoid accidental over-writing of PMNS files, <i>outfile</i> is expected to not exist when <code>pmnsmerge</code> starts. The <code>-f</code> option allows an existing <i>outfile</i> to be unlinked (if possible) and truncated before writing starts. </p>
<p> Normally duplicate names for the same Performance Metric Identifier (PMID) in a PMNS are allowed. The <code>-d</code> option is the default option and is included for backwards compatibility. The <code>-x</code> option reverses the default and <code>pmnsmerge</code> will report an error and exit with a non-zero status if a duplicate name is found for a PMID in any of the <i>input</i> PMNS files or in the merged <i>output</i> PMNS. </p>
<p> The <code>-v</code> option produces one line of diagnostic output as each <i>infile</i> is processed. </p>
<p> Once all of the merging has been completed, <code>pmnsmerge</code> will attempt to load the resultant namespace using <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3) &#8211; if this fails for any reason, <i>outfile</i> will still be created, but <code>pmnsmerge</code> will report the problem and exit with non-zero status. </p>
<p> Using <code>pmnsmerge</code> with a single <i>input</i> argument allows that PMNS file to be checked. In addition to syntactic checking, specifying <code>-x</code> will also enable a check for duplicate names for all PMIDs.</p>
<h2>CAVEAT</h2>
<p> Once the writing of the new <i>outfile</i> file has begun, the signals SIGINT, SIGHUP and SIGTERM will be ignored to protect the integrity of the new file.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmnsadd/">pmnsadd</a></code>(1), <code><a href="/docs/linux/man/1-pmnsdel/">pmnsdel</a></code>(1), <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). </p>
<h2>Index</h2>
