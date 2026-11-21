---

title: "flow-filter(1)"
name: "flow-filter"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-filter/"
description: "flow-filter – Filter flows."
---

<h2>NAME</h2>
<p> flow-filter &#8211; Filter flows.</p>
<p> <code>flow-filter</code> [ <code>-hko</code> ] [ <code>-a</code><i> src_as_filter</i> ] [ <code>-A</code><i> dst_as_filter</i> ] [ <code>-b</code><i> big</i><code>|</code><i>little</i> ] [ <code>-C</code><i> comment</i> ] [ <code>-D</code><i> dstaddr_filter_name</i> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-e</code><i> exaddr_filter</i> ] [ <code>-f</code><i> acl_fname</i> ] [ <code>-i</code><i> input_filter</i> ] [ <code>-I</code><i> output_filter</i> ] [ <code>-p</code><i> srcport_filter</i> ] [ <code>-P</code><i> dstport_filter</i> ] [ <code>-r</code><i> ipprot_filter</i> ] [ <code>-S</code><i> srcaddr_filter_name</i> ] [ <code>-t</code><i> tos_filter</i> ] [ <code>-T</code><i> tcp_flags_filter</i> ] [ <code>-x</code><i> nexthop_filter_name</i> ] [ <code>-z</code><i> z_level</i> ]</p>
<p> The <code>flow-filter</code> utility will filter flows based on user selectable criteria. The IP address filters are defined in <i>flow.acl</i> or by the filename specified by -f. </p>
<p> Other filters such as input interface and ports are defined on the command line. These filters accept range and negation operators, ie -i1-15 for input interfaces 1 through 15 or -i1,15 for input interfaces 1 and 15, or !1,15 for not input interfaces 1 and 15. </p>
<p> The syntax is kludgy and needs reworked but works for most applications.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code><i> src_as_filter</i></dt>
<dd> Source AS filter, ie -a159 to permit Autonomous System 159.</dd>
<dt><code>-A</code><i> dst_as_filter</i></dt>
<dd> Destination AS filter, ie -A159,3112 to permit Autonomous Systems 159 and 3112.</dd>
<dt><code>-b</code><i> big</i><code>|</code><i>little</i></dt>
<dd> Byte order of output.</dd>
<dt><code>-C</code><i> Comment</i></dt>
<dd> Add a comment.</dd>
<dt><code>-d</code><i> debug_level</i></dt>
<dd> Enable debugging.</dd>
<dt><code>-D</code><i> dstaddr_filter_name</i></dt>
<dd> Destination IP address filter. This is the name or number of a standard access list defined in <i>flow.acl</i> or the file specified by -f.</dd>
<dt><code>-e</code><i> exaddr_filter</i></dt>
<dd> Exporter IP address filter. One exporter address can be filtered.</dd>
<dt><code>-f</code><i> acl_fname</i></dt>
<dd> Access list filename. Defaults to <i>flow.acl</i>.</dd>
<dt><code>-h</code></dt>
<dd> Display help.</dd>
<dt><code>-i</code><i> input_filter</i></dt>
<dd> Input interface filter, ie -i0 to permit traffic from interface 0.</dd>
<dt><code>-k</code></dt>
<dd> Keep time from input.</dd>
<dt><code>-I</code><i> output_filter</i></dt>
<dd> Output interface filter, ie -I0 to permit traffic to interface 0.</dd>
<dt><code>-o</code></dt>
<dd> Logical OR instead of AND filters.</dd>
<dt><code>-p</code><i> srcport_filter</i></dt>
<dd> Source port filter, ie -p80 to only permit source port 80.</dd>
<dt><code>-P</code><i> dstport_filter</i></dt>
<dd> Destination port filter, ie -P80,8080 to permit destination ports 80 and 8080.</dd>
<dt><code>-r</code><i> ipprot_filter</i></dt>
<dd> IP Protocol filter, ie -r6 to only permit TCP traffic.</dd>
<dt><code>-S</code><i> srcaddr_filter_name</i></dt>
<dd> Source IP address filter. This is the name or number of a standard access list defined in <i>flow.acl</i> or the file specified by -f.</dd>
<dt><code>-t</code><i> tos_filter</i></dt>
<dd> ToS bits filter. An optional mask is available which is applied to the tos field before comparing to the filter list. For example to match a tos bit pattern of 101xxxxx use 0xA0/0xE0.</dd>
<dt><code>-T</code><i> tcp_flags_filter</i></dt>
<dd> TCP bits filter. An optional mask is available which is applied to the TCP flags field before comparing to the filter list. For example to match a flows with the SYN bit set use 0x2/0x2.</dd>
<dt><code>-x</code><i> nexthop_filter_name</i></dt>
<dd> NextHop IP address filter. This is the name or number of a standard access list defined in <i>flow.acl</i> or the file specified by -f.</dd>
<dt><code>-z</code><i> z_level</i></dt>
<dd> Configure compression level to <i> z_level</i>. 0 is disabled (no compression), 9 is highest compression.</dd></dl>
<h2>EXAMPLES</h2>
<p> Print all traffic with a destination port of 80. </p>
<p> <code>flow-cat /flows/krc4 | flow-filter -P80 | flow-print</code> </p>
<p> Print all traffic with with source IP 10.0.0.1. Populate <i>flow.acl</i> with ip access-list standard badguy permit host 10.0.0.1 </p>
<p> <code>flow-cat /flows/krc4 | flow-filter -Sbadguy | flow-print</code> </p>
<p> Report all destinations that IP 10.0.0.1 has sent traffic to. Sort by octets. Populate <i>flow.acl</i> with ip access-list standard badguy permit host 10.0.0.1 </p>
<p> <code>flow-cat /flows/krc4 | flow-filter -Sbadguy | flow-stat -f8 -S2</code></p>
<h2>BUGS</h2>
<p> Extended access lists are not fully implemented. The command line filter syntax is a kludge.</p>
<h2>NOTES</h2>
<p> Use flow-nfilter.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
