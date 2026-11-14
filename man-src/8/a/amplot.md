---
title: "amplot(8)"
name: "amplot"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amplot/"
description: "amplot – visualize the behavior of Amanda"
---

<p>amplot &#8211; visualize the behavior of Amanda</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amplot</code> [-b] [-c] [-e] [-g] [-l] [-p] [-t&nbsp;<wbr><i>T</i>] <i>amdump_files</i></p>
<dd>
<h2>Description</h2>
<p><code>Amplot</code></p>
<dd>reads an <code>amdump</code> output file that Amanda generates each run (e.g. <i>amdump.1</i>) and translates the information into a picture format that may be used to determine how your installation is doing and if any parameters need to be changed. <code>Amplot</code> also prints out <code>amdump</code> lines that it either does not understand or knows to be warning or error lines and a summary of the start, end and total time for each backup image. </p>
<p> <code>Amplot</code> is a shell script that executes an <code>awk</code> program (<i>amplot.awk</i>) to scan the <code>amdump</code> output file. It then executes a <code>gnuplot</code> program (<i>amplot.g</i>) to generate the graph. The <code>awk</code> program is written in an enhanced version of awk, such as GNU awk (<code><a href="/docs/linux/man/1-gawk/">gawk</a></code>(1) version 2.15 or later) or <code><a href="/docs/linux/man/1-nawk/">nawk</a></code>(1). </p>
<p> During execution, <code>amplot</code> generates a few temporary files that <code>gnuplot</code> uses. These files are deleted at the end of execution. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Options</h2>
<p><code>-b</code></p>
<dl>
<dd>Generate b/w postscript file (need <code>-p</code>).</dl>
<p> <code>-c</code></p>
<dl>
<dd>Compress <i>amdump_files</i> after plotting.</dl>
<p> <code>-e</code></p>
<dl>
<dd>Extend the X (time) axis if needed.</dl>
<p> <code>-g</code></p>
<dl>
<dd>Direct <i>gnuplot</i> output directly to the X11 display (default).</dl>
<p> <code>-p</code></p>
<dl>
<dd>Direct postscript output to file <i>YYYYMMDD</i><i>.ps</i> (opposite of <code>-g</code>).</dl>
<p> <code>-l</code></p>
<dl>
<dd>Generate landscape oriented output (needs <code>-p</code>).</dl>
<p> <code>-t </code><i>T</i></p>
<dl>
<dd>Set the right edge of the plot to be <i>T</i> hours.</dl>
<p> The <i>amdump_files</i> may be in various compressed formats (<i>compress</i>, <code>gzip</code>, <code>pact</code>, <code>compact</code>).</p>
<h2>Interpretation</h2>
<p>The figure is divided into a number of regions. There are titles on the top that show important statistical information about the configuration and from this execution of <code>amdump</code>. In the figure, the X axis is time, with 0 being the moment <code>amdump</code> was started. The Y axis is divided into 5 regions: </p>
<p> <i>QUEUES:</i> How many backups have not been started, how many are waiting on space in the holding disk and how many have been transferred successfully to tape. </p>
<p> <i>%BANDWIDTH:</i> Percentage of allowed network bandwidth in use. </p>
<p> <i>HOLDING DISK:</i> The higher line depicts space allocated on the holding disk to backups in progress and completed backups waiting to be written to tape. The lower line depicts the fraction of the holding disk containing completed backups waiting to be written to tape including the file currently being written to tape. The scale is percentage of the holding disk. </p>
<p> <i>TAPE:</i> Tape drive usage. </p>
<p> <i>%DUMPERS:</i> Percentage of active dumpers. </p>
<p> The idle period at the left of the graph is time <code>amdump</code> is asking the machines how much data they are going to dump. This process can take a while if hosts are down or it takes them a long time to generate estimates.</p>
<h2>Bugs</h2>
<p>Reports lines it does not recognize, mainly error cases but some are legitimate lines the program needs to be taught about.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8), <code><a href="/docs/linux/man/1-gnuplot/">gnuplot</a></code>(1), <code><a href="/docs/linux/man/1-compress/">compress</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Olafur Gudmundsson</code> &lt;ogud [at] tis.com&gt;</p>
<dl>
<dd>Trusted Information Systems</dl>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
