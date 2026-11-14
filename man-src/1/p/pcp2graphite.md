---
title: "pcp2graphite(1)"
name: "pcp2graphite"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcp2graphite/"
description: "pcp2graphite – pcp-to-graphite metrics exporter"
---

<h2>NAME</h2>
<p> <code>pcp2graphite </code> &#8211; pcp-to-graphite metrics exporter</p>
<h2>SYNOPSIS</h2>
<p> <code>pcp2graphite</code> [<code>-h</code> <i>hostspec</i>] [<code>-a</code> <i>archive</i>] [<code>-L</code>] [<code>-O</code> <i>origin</i>] [<code>-T</code> <i>finish</i>] [<code>-s</code> <i>samples</i>] [<code>-t</code> <i>delta</i>] [<code>-g</code> <i>graphitehost</i>] [<code>-p</code> <i>pickleport</i>] [<code>-P</code> <i>textport</i>] [<code>-r</code> <i>pickleprotocol</i>] [<code>-u</code> <i>units</i>] [<code>-m</code> <i>prefix</i>] <i>metricname</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>pcp2graphite</code> is a PCP metric exporter. It relays hierarchies of the <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5) to a designated Graphite (Carbon/Whisper) database by periodically polling, then copying/converting relevant numerical metrics across the Graphite &quot;text&quot; or &quot;pickled&quot; TCP protocols. Metric values are optionally scaled to a given unit/scale, but are not rate-converted. Metric names may be prefixed and are somewhat canonicalized to fit the Graphite namespace rules. </p>
<p> The data transfer will continue on a best-effort basis until the program is interrupted. Temporary errors are ignored. Multiple copies of this program may be run in parallel, to populate different Graphite databases or subtrees, with different scaling or sampling intervals. </p>
<p> The <code><a href="/docs/linux/man/1-pmmgr/">pmmgr</a></code>(1) daemon can be used to ensure one or more <code>pcp2grapite</code> instances start at system boot time.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h </code><i>hostspec</i></p>
<dd> Extract metrics from the specified <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) daemon, using a host specification as described on <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). The default is <code>local:</code>.</p>
<dt><code>-a </code><i>archive</i></p>
<dd> Extract metrics from the given set of archives, which is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives.</p>
<dt><code>-L</code></p>
<dd> Extract metrics from the local context PCP PMDAs.</p>
<dt><code>-t </code><i>delta</i></p>
<dd> Specify the polling interval in seconds. If live, polling is aligned to natural multiples of this interval. The default is <code>60</code> seconds.</p>
<dt><code>-O </code><i>origin</i></p>
<dd> Set the time origin for archive scanning. The default is the start of the set of archives.</p>
<dt><code>-T </code><i>finish</i></p>
<dd> Set the time finish for archive scanning. The default is the end of the set of archives.</p>
<dt><code>-s </code><i>samples</i></p>
<dd> Set the maximum number of samples to relay. The default is unlimited.</p>
<dt><code>-g </code><i>graphitehost</i></p>
<dd> Specify the graphite carbon-cache server where the relayed data is to be relayed. The default is <code>localhost</code>.</p>
<dt><code>-p </code><i>pickleport</i></p>
<dd> Select the more efficient &quot;pickled&quot; encoding for carbon-cache communication, and use the given TCP port. This is the default, using port <code>2004</code>.</p>
<dt><code>-P </code><i>textport</i></p>
<dd> Alternately, select the less efficient &quot;text&quot; encoding for carbon-cache communication, and use the given TCP port. This protocol is not default, because it requires a separate TCP connection for each metric. The typical port is <code>2003</code>.</p>
<dt><code>-r </code><i>pickleprotocol</i></p>
<dd> Select the protocol for the &quot;pickled&quot; encoding. The possible values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> 0 &#8211; ASCII protocol (the slowest),</p>
<dt>&bull;</p>
<dd> 1 &#8211; old binary protocol &#8211; pre Python 2.3,</p>
<dt>&bull;</p>
<dd> 2 &#8211; new binary protocol introduced in Python 2.3.</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>The default is <code>0</code>.</p>
<dd></dl>
</dl>
<dt><code>-u </code><i>units</i></p>
<dd> Rescale the metrics to the given UNITS string, as parsed by the <i><a href="/docs/linux/man/3-pmparseunitsstr/">pmParseUnitsStr</a></i>(3) function. This must be dimensionally consistent with the underlying PCP metric. The default is to perform no scaling.</p>
<dt><code>-m </code><i>prefix</i></p>
<dd> Use the given string as a prefix for all PMNS metrics relayed to Graphite. The default is <code>pcp.</code> (note the period at the end).</p>
<dt><i>metricname</i></p>
<dd> Relay all numeric metrics nested at or below the given name in the PMNS. This option may be repeated. This is a compulsory option, having no default.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/3-pmparseunitsstr/">pmParseUnitsStr</a></code>(3), <code><a rel="nofollow" href="http://graphite.wikidot.com/">http://graphite.wikidot.com/</a></code>, <code><a href="/docs/linux/man/1-pmmgr/">pmmgr</a></code>(1), <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). </p>
<h2>Index</h2>
