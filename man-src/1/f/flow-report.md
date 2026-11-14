---
title: "flow-report(1)"
name: "flow-report"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-report/"
description: "flow-report – Generate reports from flow data."
---

<h2>NAME</h2>
<p> flow-report &#8211; Generate reports from flow data.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-report</code> [ <code>-h</code> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-s</code><i> stat_fname</i> ] [ <code>-S</code><i> stat_definition</i> ] [ <code>-v</code><i> variable binding</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-report</code> utility will generate reports from flow data. The reports are easy to parse ASCII text that can be used by a front end to produce readable reports, graphs, and charts. </p>
<p> Reports are definied in a configuration file by the &#8216;stat-report&#8217; keyword followed by a report name. Each report has a type defined below and other commands. Reports are grouped into a definition with the &#8216;stat-definition&#8217; keyword followed by a definition name. Each definition can invoke a filter and optionally apply tags. </p>
<p> Words in the configuration file of the form @VAR or @{VAR:default} will be expanded at run-time by setting variable names with the -v option. </p>
<p> Generated reports consist of comment lines and report lines. Comment lines begin with a # and include details such as the options used, report name, records in the report, and the report line format. Some of the more verbose comments can be controlled with the +header and +xheader options. By default this information is not displayed. A column title beginning with the string rec precedes the report lines. Report lines consist of key fields, such as an IP address and calculated totals for that key such as the number of flows. The summary-detail report is a little bit different from other reports in that it has multiple title lines and no key fields. The column titles are described below. </p>
<pre>
 +time_real   Difference between the real time of the first and last
              flow.
 +aflowtime   Total time of the flows / Total number of flows.
 +aps         Total Octets / Total Packets (Average Packet Size)
 +afs         Total Octets / Total Flows / (Average Flow Size)
 +apf         Total Packets / Total Flows (Average Packets / Flow)
 +fps         Total Flows / (Last End Time of Flow -
                First Start Time of Flow) (Average Flows / Second)
 +fps_real    (Average Flows / Second in realtime)
 +psizeN      Average Packet Size buckets.
 +fpsizeN     Packets / Flow buckets.
 +fosizeN     Octets / Flow buckets.
 +ftimeN      Time / Flow buckets.
  ignores     Flows with a packet count of 0.
  SSS-count   Count of of an item, example source-ip-address-count
  SSS*        key fields, example source-ip-address
  index       Report line index.
  first       Time of first flow in unix_secs format.
  last        Time of last flow in unix_secs format.
  flows       Summation of flows/key.
  octets      Summation of octets/key.
  packets     Summation of packets/key.
  duration    End time of Flow - Start time of Flow.
  avg-bps     Average Bits/Second.
  min-bps     Minimum Bits/Second.
  max-bps     Maximum Bits/Second.
  avg-pps     Average Packets/Second.
  min-pps     Minimum Packets/Second.
  max-pps     Maximum Packets/Second.
  frecs       Records used in average calculations.
Note fields with a + are only available in the summary-detail report.
</pre>
<p> The PPS and BPS calculations will not always be correct due to flows which only have one packet, or some other condition where the start time is equal to the end time. In this case these flows are not used in the PPS and BPS calculations. To facilitate aggregating multiple reports and retaining the PPS and BPS fields, the number of flows counted is available in the frecs field. </p>
<pre><code>
stat - report command Description / Example-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --type Define the report type.type destination - tag filter Apply this filter definition.filter permit - only - tcp scale Scale report by n.scale 100 tag - mask Apply source and destination mask to tag.tag - mask 0xFF00 0xFF00 ip - source - address - format Format of source IP address.address - address, ie 128.146.1.7 prefix - len - address / len ie 128.146.1.7 / 24 prefix - mask - prefix / len 128.146.1 / 24 ip - destination - address - format Format of destination IP address.address - address, ie 128.146.1.7 prefix - len - address / len ie 128.146.1.7 / 24 prefix - mask - prefix / len 128.146.1 / 24 output Start an output configuration.Multiple output configurations can be configured per report.
</code></pre>
<p>output option Description / Example&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -path Pathname of output.If the path begins<br />
                                with a |<br />
        the output is a pipe.The<br />
                    pathname is formatted through<br />
                    strftime()<br />
                        .Directories not in the path are<br />
                automatically created.path<br />
                / tmp / % Y / % m / % d / foo.out time What time to use when formatting the pathname with strftime.now<br />
            &#8211; current time start &#8211; first flow end &#8211; last flow mid &#8211; average of first<br />
    and last.tally Emit a % total line every n records.tally 10 format Output format.Currently only ascii.format ascii<br />
                            sort Sort on a field.+<br />
            ascending,<br />
    -descending.sort + flows &#8211; sort on the flows field Sortable fields are flows, octets, packets,<br />
    duration, avg &#8211; pps, min &#8211; pps, max &#8211; pps, avg &#8211; bps,<br />
    min &#8211; bps, max &#8211; bps records Truncate report at n records.records 10 fields Enable / Disable fields with + / -.Fields : index, first, last, flows, octets, packets,<br />
    duration, pps, bps, other, key, key1, key2,<br />
    key3, key4, count.fields + key, +flows, +octets, +packets,<br />
    For reports with one key, the key field is referenced with key, else key1, key2, key3, etc Note that the count field is only available in select reports, those which end in &#8211; count.</p>
<p>                                                                                                                                                                                       options Enable<br />
                                                                                                                                                                                       / Disable options with<br />
                                                                                                                                                                  + / -+header &#8211; include header.+ xheader &#8211; include extra header.+ totals &#8211; include a totals line.+ percent &#8211; total &#8211; report in % total form.+ names &#8211; use symbolic names.options + header,<br />
    +xheader</p>
<p>stat &#8211; definition option Description / Example&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -filter Apply this filter definition.filter default tag Apply this tag definition.tag default mask Apply this mask definition.mask default report Invoke this report.Multiple reports can be set.report foo time &#8211; series How often to produce a report in seconds.time &#8211; series 60</p>
<p>global options Description / Example&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -include &#8211; tag Specify path to include tag definitions.include &#8211; tag / flows / tags / test1 include &#8211; filter Specify path to include filter definitions.include &#8211; filter / flows / filters / test1 include &#8211; mask Specify path to include mask definitions.include &#8211; filter / flows / masks / test1</p>
<pre><code>
Report type Summarization Key Elements.-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --summary - detail Totals plus quick breakdown.summary - counters Totals only.packet - size Average packet size distribution.octets Octets per flow distribution.packets Packets per flow distribution.ip - source - port IP Source Port.ip - destination - port IP Destination Port.ip - source / destination - port IP Source / Destination Port pair.bps Bits / Second distribution.pps Packets / Second distribution.ip - destination - address - type IP class with ASM / SSM Multicast breakout.ip - protocol IP Protocol.ip - tos IP Type of Service.ip - next - hop - address IP Next Hop Address.ip - source - address IP Source Address.ip - destination - address IP Destination Address.ip - source / destination - address IP Source / Destination Address pair.ip - exporter - address IP Exporter Address.input - interface Input Interface.output - interface Output Interface.input / output - interface Input / Output Interface pair.source - as Source AS.destination - as Destination AS.source / destination - as Source / Destination AS.ip - source - address / source - as IP Source Addrss and Source AS.ip - destination - address / source - as IP Destination Address and Source AS.ip - source - address / destination - as IP Source Address and Destination AS.ip - destination - address / destination - as IP Destination Address and Destination AS.ip - source / destination - address / source - as IP Source / Destination Address and Source AS.ip - source / destination - address / destination - as IP Source / Destination Address and Destination AS.ip - source / destination - address / source / destination - as IP Source / Destination Address and Source / Destination AS.ip - source - address / input - interface IP Source Address and Input Interface.ip - destination - address / input - interface IP Destination Address and Input Interface.ip - source - address / output - interface IP Source Address and Output Interface.ip - destination - address / output - interface IP Destination Address and Output Interface.ip - source / destination - address / input - interface IP Source / Destination Address and Input Interface.ip - source / destination - address / output - interface IP Source / Destination Address and Output Interface.ip - source / destination - address / input / output - interface IP Source / Destination Address and Input / Output Interface.input - interface / source - as Input Interface and Source AS.input - interface / destination - as Input Interface and Destination AS.output - interface / source - as Output Interface and Source AS.output - interface / destination - as Output Interface and Destination AS.input - interface / source / destination - as Input Interface and Source / Destination AS.output - interface / source / destination - as Output Interface and Source / Destination AS.input / output - interface / source / destination - as Input / Output Interface and Source / Destination AS.engine - id Engine ID.engine - type Engine Type.source - tag Source Tag.destination - tag Destination Tag.source / destination - tag Source / Destination Tag.ip - source - address / ip - source - port IP Source Address and IP Source Port.ip - source - address / ip - destination - port IP Source Address and IP Destination Port.ip - destination - address / ip - source - port IP Destination Address and IP Source Port.ip - destination - address / ip - destination - port IP Destination Address and IP Destination Port.ip - source - address / ip - source / destination - port IP Source Address and IP Source / Destination Port.ip - destination - address / ip - source / destination - port IP Destination Address and IP Source / Destination Port.ip - source / destination - address / ip - source - port IP Source / Destination Address and IP Source Port.ip - source / destination - address / ip - destination - port IP Source / Destination Address and IP Destination Port.ip - source / destination - address / ip - source / destination - port IP Source / Destination Address and IP Source / Destination Port.ip - source - address / input / output - interface IP Source Address and Input / Output Interface.ip - destination - address / input / output - interface IP Destination Address and Input / Output Interface.ip - source - address / source / destination - as IP Source Address and Source / Destination AS.ip - destination - address / source / destination - as IP Destination Address and Source / Destination AS.ip - address IP Address(both source and destination).ip - port IP Port(both source and destination).ip - source - address - destination - count Count of destination IP addresses associated with a source IP address.ip - destination - address - source - count Count of source IP addresses associated with a destination IP address.linear - interpolated - flows - octets - packets Linear interpolated distribution of flows,
    octets and packets.The distribution is
        done across the start and end time of the
        flow.first First packet of flow distribution.last Last packet of flow distribution.duration Duration of flow distribution.ip
        - source - address / source - tag IP Source Address and Source tag.ip - source - address / destination - tag IP Source Address and Destination tag.ip - destination - address / source - tag IP Destination Address and Source tag.ip - destination - address / destination - tag IP Destination Address and Destination tag.ip - source / destination - address / source / destination - tag IP Source / Destination Address and Source / Destination tag.ip - source / destination - address / ip - protocol / ip - tos IP Source / Destination Address,
    IP Protocol,
    and ToS.ip - source / destination - address / ip - protocol / ip - tos / ip - source / destination - port IP Source / Destination Addess, IP Protocol,
    IP Tos, IP Source / Destination Port.
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-s</code><i> stat_fname</i></p>
<dd> Report configuration filename. Defaults to <i>/etc/flow-tools/cfg/stat</i>.</p>
<dt><code>-S</code><i> stat_definition</i></p>
<dd> Select the active definition.</p>
<dt><code>-v</code><i> variable binding</i></p>
<dd> Set a variable FOO=bar.</p>
<dt><code>-h</code></p>
<dd> Display help. -hh will list the available reports.</dl>
<h2>EXAMPLES</h2>
<p> An example of report configuration file </p>
<pre>
# stat config file
include-filter /tmp/filter
stat-report t1
  type summary-detail
  filter default
  scale 100 
  output
    format ascii
    options +header,+xheader,+totals
    fields +other
    path /tmp/output1
stat-report t6
  type ip-source-port  
  output
    format ascii
    options +header,+xheader,+totals,+names,+percent-total
    sort +pps
    tally 5
    path /tmp/output6
stat-definition test
  filter tcp
  report t1
  report t6
</pre>
<pre>
# filter config file
filter-primitive TCP
  type ip-protocol
  permit TCP
filter-definition tcp
  match ip-protocol TCP
</pre>
<p> <code>flow-cat </code><i>flows</i><code> | flow-report -stest -Stest</code></p>
<h2>IMPLEMENTATION NOTES</h2>
<p> Packet size calculations are dOctets / dPkts, ie an average packet size. It is not possible to get a true packet size from flow exports. pps and bps calculations are an average of the averages. Flows that do not have a duration (start == end) are not counted in the pps and bps calculations. Flows without a packet or octet count are ignored.</p>
<h2>FILES</h2>
<p> Configuration files: Symbols &#8211; <i>/etc/flow-tools/sym/*</i>. Tag &#8211; <i>/etc/flow-tools/cfg/tag.cfg</i>. Filter &#8211; <i>/etc/flow-tools/cfg/filter.cfg</i>. Mask &#8211; <i>/etc/flow-tools/cfg/mask.cfg</i>. Report &#8211; <i>/etc/flow-tools/cfg/stat.cfg</i>. Xlate &#8211; <i>/etc/flow-tools/cfg/xlate.cfg</i>.</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
