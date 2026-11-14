---
title: "flow-rpt2rrd(1)"
name: "flow-rpt2rrd"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-rpt2rrd/"
description: "flow-rpt2rrd – Convert flow-report CSV output to RRDtool format."
---

<h2>NAME</h2>
<p> flow-rpt2rrd &#8211; Convert flow-report CSV output to RRDtool format.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-rpt2rrd</code> [ <code>-nv</code> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-k</code><i> keys</i> ] [ <code>-K</code><i> keys_file</i> ] [ <code>-f</code><i> fields</i> ] [ <code>-p</code><i> rrd_path</i> ] [ <code>-P</code><i> rrd_postfix</i> ] [ <code>-r</code><i> rrd_storage</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-rpt2rrd</code> utility processes the CSV output of flow-report into RRDtool format. The aggregates for a key are each stored as a DS in RRD filename {rrd_path,&quot;/&quot;,key,rrd_postfix,&quot;.rrd&quot;}. By default a DS is created for flows, octets, and packets. The key must be specified, for example an ip-port report could use smtp,nntp,ssh,telnet as the keys which would create a separate RRD for each key.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Set debug level to debug_level (debugging code)</p>
<dt><code>-h</code></p>
<dd> Help.</p>
<dt><code>-k</code><i> keys</i><code>|</code><i>html</i></p>
<dd> Comma separated list of key values. If the report has symbols then the key must be the symbol, ie smtp not 25. The totals_* lines may be used if they are enabled in the report. There is no default, keys must be specified with -k or -K.</p>
<dt><code>-K</code><i> keys_file</i></p>
<dd> Load keys from <i>keys_file</i>. See -k.</p>
<dt><code>-f</code></p>
<dd> Comma separated list of columns to store. Each column maps to a DS in the RRD. Defaults to flows,octets,packets</p>
<dt><code>-n</code></p>
<dd> Enable symbol table lookups. For example TCP port 25 = smtp. This will result in RRD file names with the symbolic names if symbol lookups were not enabled in the report.</p>
<dt><code>-p</code><i> rrd_path</i></p>
<dd> Set path to RRD files. Defaults to &quot;.&quot;.</p>
<dt><code>-P</code><i> rrd_postfix</i></p>
<dd> Set RRD file name postfix. Defaults to &quot;&quot;.</p>
<dt><code>-r</code><i> rrd_storage</i></p>
<dd> Set RRD storage for 5 minute, 30 minute, 2 hour, and 1 day databases. List items are : seperated. Defaults to 600:600:600:732.</p>
<dt><code>-v</code></p>
<dd> Enable verbose output.</dl>
<h2>EXAMPLES</h2>
<pre><code>
The following example shows the combined use of flow-nfilter (inline), 
flow-report, and flow-rpt2rrd to create an RRD depicting traffic 
from clmbo-r4 to AS 10796 and 6478 for 2004-11-08.  rrdtool graph is
then used to create a .png.
#!/ bin / sh
cat &lt;&lt; EOF&gt;report.cfg
include-filter nfilter.cfg
stat-report CLMBO-R4-TO-INTERNET-BY-DESTINATION-AS
  type destination-as
  filter CLMBO-R4-INTERNET-OUT
  scale 100
  output   
    options +header,+xheader
    fields -duration
stat-definition 5min-summaries
  report CLMBO-R4-TO-INTERNET-BY-DESTINATION-AS
EOF
cat &lt;&lt; EOF&gt;nfilter.cfg
#ifMIB.ifMIBObjects.ifXTable.ifXEntry.ifName .46 = so - 0 / 0 / 0.0
filter-primitive CLMBO-R4-INTERNET
  type ifindex
  permit 46
#Match on traffic to the Internet
filter-definition CLMBO-R4-INTERNET-OUT
  match output-interface CLMBO-R4-INTERNET
EOF
mkdir rrds
# 5 minute flow files from flow - capture are here
FLOW_DATA=/flows/clmbo-r4/2004-11-08/
#for each 5 minute flow, aggregate with flow - report then store to RRD
for name in $FLOW_DATA/*; do
  echo working...$name
  flow-report -s report.cfg -S5min-summaries &lt; $name | flow-rpt2rrd -k10796,6478  -p rrds
done
# first flow - 0:1:23 11/8/2004
START=1099890083
# last flow - 0:1:25 11/9/2004
END=1099976485
rrdtool graph CLMBO-R4-TO-INTERNET.png --start $START --end $END \
        --vertical-label "Bits/Second" --title="CLMBO-R4 TO INTERNET BY AS" \
        DEF:AS10796in=rrds/10796.rrd:octets:AVERAGE \
        DEF:AS6478in=rrds/6478.rrd:octets:AVERAGE \
        CDEF:b_AS10796in=AS10796in,8,* \
        CDEF:b_AS6478in=AS6478in,8,* \
        LINE1:b_AS10796in#FF0000:AS10796-in \
        LINE1:b_AS6478in#555555:AS6478-in \
</code></pre>
<h2>BUGS</h2>
<p> Hard coded to expect 5 minute flow file intervals. Does not properly parse flow-report time-series output.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
