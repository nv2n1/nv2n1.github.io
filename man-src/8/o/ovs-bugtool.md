---
title: "ovs-bugtool(8)"
name: "ovs-bugtool"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovs-bugtool/"
description: "ovs-bugtool – Open vSwitch bug reporting utility"
---

<p>ovs-bugtool &#8211; Open vSwitch bug reporting utility</p>
<h2>Synopsis</h2>
<p><code>ovs-bugtool</code></p>
<h2>Description</h2>
<p>Generates a debug bundle with useful information about Open vSwitch on this system and places it in <code>/var/log/ovs-bugtool</code>.</p>
<h2>Collection Options</h2>
<p>These options influence what categories of data <code>ovs-bugtool</code> collects.</p>
<dl>
<dt><code>&#8211;entries=</code><i>list</i></p>
<dd>Collect the capabilities specified in the comma-separated <i>list</i>.</p>
<dt><code>&#8211;all</code></p>
<dd>Collect all available capabilities.</p>
<dt><code>&#8211;ovs</code></p>
<dd>In addition to Open vSwitch configuration and status, <code>ovs-bugtool</code> can collect a variety of relevant system information. This option limits collection to Open vSwitch-specific categories.</p>
<dt><code>&#8211;log-days=</code><i>days</i></p>
<dd>Include the logs with last modification time in the previous <i>days</i> days in the debug bundle. The number of log files included has a big impact on the eventual bundle size. The default value is 20 days.</p>
<dt><code>-y</code></p>
<dd>
<dt><code>&#8211;yestoall</code></p>
<dd>Answer yes to all prompts.</p>
<dt><code>&#8211;capabilities</code></p>
<dd>Writes the categories that <code>ovs-bugtool</code> can collect on stdout in XML, then exits.</dl>
<h2>Output Options</h2>
<p>These options influence the format and destination of <code>ovs-bugtool</code> output.</p>
<dl>
<dt><code>&#8211;output=</code><i>filetype</i></p>
<dd>Generates a debug bundle with the specified file type. Options include <code>tar</code>, <code>tar.gz</code>, <code>tar.bz2</code>, and <code>zip</code>.</p>
<dt><code>&#8211;outfile=</code><i>file</i></p>
<dd>Write output to <i>file</i>. Mutually exclusive with <code>&#8211;outfd</code>.</p>
<dt><code>&#8211;outfd=</code><i>fd</i></p>
<dd>Write output to file descriptor <i>fd</i>. This option must be used with <code>&#8211;output=tar</code>.</p>
<dt><code>&#8211;unlimited</code></p>
<dd>Do not exclude files which are too large. Also skip checking free disk space. By default up to 90 percent of the free disk space can be used.</p>
<dt><code>&#8211;debug</code></p>
<dd>Print verbose debugging output.</dl>
<h2>Other Options</h2>
<dl>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;silent</code></p>
<dd>Suppress most output to stdout.</p>
<dt><code>&#8211;help</code></p>
<dd>Print a summary of <code>ovs-bugtool</code> usage to stdout, then exit.</dl>
<h2>Examples</h2>
<p>Here&#8217;s a collection of some commonly useful options: </p>
<p> <code>ovs-bugtool -y -s &#8211;output=tar.gz &#8211;outfile=/var/log/bugtool-report.tgz</code></p>
<h2>Bugs</h2>
<p><code>ovs-bugtool</code> makes many assumptions about file locations and the availability of system utilities. It has been tested on Debian and Red Hat and derived distributions. On other distributions it is likely to be less useful. </p>
