---
title: "initctl2dot(8)"
name: "initctl2dot"
section: "8"
letter: "i"
url: "/docs/linux/man/8-initctl2dot/"
description: "initctl2dot – manual page for initctl2dot"
---

<p>initctl2dot &#8211; manual page for initctl2dot</p>
<h2>Synopsis</h2>
<p><code>initctl2dot</code> [<i>OPTIONS</i>]</p>
<h2>Description</h2>
<p>Convert <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) output to GraphViz <code><a href="/docs/linux/man/1-dot/">dot</a></code>(1) format. </p>
<p> With no options, <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) will be invoked automatically and the output written to file <i>upstart.dot</i>. If run from within an Upstart user session, unless <code>&#8211;system</code> is specified, the data generated will be for the user session.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code> <i>INFILE</i> , &#8211;infile=<i>INFILE</i></p>
<dd>File to read <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) output from (&quot;initctl show-config -e&quot;). If not specified, <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) will be run automatically.</p>
<dt><code>-h</code></p>
<dd>Display usage statement.</p>
<dt><code>-r</code> <i>RESTRICTIONS</i> , &#8211;restrict-to-jobs=<i>RESTRICTIONS</i></p>
<dd>Limit display of <code>start on</code> and <code>stop on</code> conditions to comma-separated list of jobs.</p>
<dt><code>-w</code> <i>OUTFILE</i> , &#8211;outfile=<i>OUTFILE</i></p>
<dd>File to write output to.</p>
<dt><code>&#8211;color-emits</code>=<i>COLOR_EMITS</i></p>
<dd>Specify color for &#8217;emits&#8217; lines.</p>
<dt><code>&#8211;color-start-on</code>=<i>COLOR_START_ON</i></p>
<dd>Specify color for &#8216;start on&#8217; lines.</p>
<dt><code>&#8211;color-stop-on</code>=<i>COLOR_STOP_ON</i></p>
<dd>Specify color for &#8216;stop on&#8217; lines.</p>
<dt><code>&#8211;color-event</code>=<i>COLOR_EVENT</i></p>
<dd>Specify color for event boxes.</p>
<dt><code>&#8211;color-text</code>=<i>COLOR_TEXT</i></p>
<dd>Specify color for summary text.</p>
<dt><code>&#8211;color-bg</code>=<i>COLOR_BG</i></p>
<dd>Specify background color for diagram.</p>
<dt><code>&#8211;color-event-text</code>=<i>COLOR_EVENT_TEXT</i></p>
<dd>Specify color for text in event boxes.</p>
<dt><code>&#8211;color-job-text</code>=<i>COLOR_JOB_TEXT</i></p>
<dd>Specify color for text in job boxes.</p>
<dt><code>&#8211;color-job</code>=<i>COLOR_JOB</i></p>
<dd>Specify color for job boxes.</p>
<dt><code>&#8211;system</code></p>
<dd>Connect to the Upstart system session.</p>
<dt><code>&#8211;user</code></p>
<dd>Connect to the Upstart user session.</dl>
<h2>Author</h2>
<p>Written by James Hunt &lt;<code>james.hunt [at] ubuntu.com</code>&gt;</p>
<h2>Reporting Bugs</h2>
<p>Report bugs at &lt;<code><a rel="nofollow" href="https://launchpad.net/upstart/+bugs">https://launchpad.net/upstart/+bugs</a></code>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011 Canonical Ltd.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-init/">init</a></code>(8) <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) </p>
