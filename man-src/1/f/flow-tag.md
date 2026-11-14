---
title: "flow-tag(1)"
name: "flow-tag"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-tag/"
description: "flow-tag – Apply tags to flow files."
---

<h2>NAME</h2>
<p> flow-tag &#8211; Apply tags to flow files.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-tag</code> [ <code>-hk</code> ] [ <code>-b</code><i> big</i><code>|</code><i>little</i> ] [ <code>-C</code><i> comment</i> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-t</code><i> tag_fname</i> ] [ <code>-T</code><i> tag_definition</i> ] [ <code>-v</code><i> variable binding</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-tag</code> utility is used to add or modify source and destination tags in flow records. Tags are 32 bit identifiers derived from rules and fields in a flow record. Tags can be used to group flows with common prefixes, autonomous systems, next hops, exporter id and/or input/output interface. <code>flow-stat</code> can be used with tagged flows to produce group based reports. For example, all outbound traffic for a customer where the customer is defined by a list of IP prefixes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code><i> big</i><code>|</code><i>little</i></p>
<dd> Byte order of output.</p>
<dt><code>-C</code><i> Comment</i></p>
<dd> Add a comment.</p>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-k</code></p>
<dd> Keep time from input.</p>
<dt><code>-t</code><i> tag_fname</i></p>
<dd> Load tags from <i>tag_name</i>. Defaults to <i>/etc/flow-tools/cfg/tag</i></p>
<dt><code>-T</code><i> active_def</i><code>|</code></p>
<dd> Use <i>active_def</i> as the active tag definition(s).</p>
<dt><code>-v</code><i> variable binding</i></p>
<dd> Set a variable FOO=bar.</dl>
<p> The configuration file is a collection of actions and definitions. An action is triggered by a definition and a definition is invoked only if listed with the <i>-T</i> flag. Lines begining with # are treated as comments and ignored. </p>
<p> Words in the configuration file of the form @VAR or @{VAR:default} will be expanded at run-time by setting variable names with the -v option. </p>
<pre><code>
tag - action command Description / Example-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --tag - action Begin tag - action section tag - action foo type Configure the type of action, one of source - prefix, destination - prefix, prefix,
    source - as, destination - as, as, next - hop,
    tcp - source - port, tcp - destination - port,
    tcp - port, udp - source - port,
    udp - destination - port, udp - port,
    tos, exporter, source - ip - address,
    destination - ip - address, ip - address,
    input - interface, output - interface,
    interface, any.type src - prefix match Match criteria.The match condition depends on the type.Following the match condition is one of set - destination, set - source,
    or -destination, or -source to set or logically or a value to the source or destination tag.match 128.146 / 16 set - destination 0x010001 Multiple actions may match and set tags on the same flow.Note that listing many actions will cause tags to be applied in O(actions) time.The actions try to run in O(1) time.For example if 10 prefixes are listed in a single action it will take about the same CPU as if 100 prefixes are used.Listing 100 actions will require 100 times the CPU as 1 action.tag - action types Description-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --source - prefix Source Prefix destination - prefix Destination Prefix prefix Source or Destination Prefix source - as Source AS destination - as Destination AS as Source or Destination AS next - hop IP Next Hop tcp - source - port TCP Source Port tcp - destination - port TCP Destination Port tcp - port TCP Source or Destination Port udp - source - port UDP Source Port udp - destination - port UDP Destination Port udp - port UDP Source or Destination Port tos Type of Service exporter Exporter IP Address source - ip - address Source IP Address destination - ip - address Destination IP Address ip - address Source or Destination IP Address input - interface Input Interface output - interface Output Interface interface Input or Output Interface any Match any flows tag - action matches Description-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --set - destination Set the destination tag, replacing any previous tag.set - source Set the source tag, replacing any previous tag.or -destination Logically or this value to the existing destination tag or -source Logically or this value to the existing source tag
</code></pre>
<p> A definition lists a set of actions which are evaluated if the filter criteria is met. Each definition is built with terms. A term has its action(s) evaluated if the filter is passed. </p>
<p>definition command Description / Example&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -tag &#8211; definition Begin tag &#8211; defintion secrion tag &#8211; definition bar term Begin a list of actions to be evaluated that match the filter rule.term input &#8211; filter List of input ifIndexes the flow must match.input &#8211; filter 1, 2, 3, 4 output &#8211; filter List of output ifIndexes the flow must match.output &#8211; filter 1, 2, 3, 4 exporter IP address of exporter the flow must match.exporter 1.2.3.4 action Name of action to evaluate.Actions are evaluated in the order they appear in a definition.action foo</p>
<h2>EXAMPLES</h2>
<p> The meaning of a tag is user defined. The following example uses 16 bits of a tag as a customer ID and 4 bits as a customer type. <code>flow-xlate</code> can be used to apply a mask to these fields. </p>
<p>#file : gigapop &#8211; tags<br />
#tag format<br />
#<br />
# 0 7 15 23 31<br />
# 0000 0000 0000 0000 0000 0000 0000 0000(32 bits)<br />
#RRRRRRRRRRRRRR TTTT NNNNNNNNNNNNNNNNNNN<br />
#| | | Site name<br />
#| | Site type<br />
#| Reserved<br />
#<br />
#<br />
#SITE_NAME_MASK = 0x0000FFFF<br />
#SITE_TYPE_MASK = 0x00FF0000<br />
#<br />
#ID Name<br />
#&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;<br />
# 0x0001 OSU<br />
# 0x0002 CWRU<br />
# 0x0003 BGSU<br />
#&#8230; etc<br />
# 0x0019 MULTICAST<br />
#<br />
#ID Type<br />
#&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;<br />
# 0x01 Participant<br />
# 0x02 SEGP<br />
# 0x03 Sponsored &#8211; Participant<br />
# 0x04 Gigapop<br />
# 0x05 MULTICAST<br />
tag &#8211; action OHIO &#8211; GIGAPOP_DST type destination &#8211; prefix<br />
#OSU<br />
                                                           match 128.146 /<br />
                                                       16 set &#8211;<br />
    destination 0x010001 match 164.107 / 16 set &#8211; destination 0x010001 match 140.254 / 16 set &#8211; destination 0x010001 match 192.153.26 / 24 set &#8211; destination 0x010001<br />
#CWRU<br />
                                                                                                                                                     match 129.22 /<br />
                                                                                                                                                     16 set &#8211;<br />
    destination 0x010002 match 192.5.110 / 24 set &#8211; destination 0x010002<br />
#BGSU<br />
                                                        match 129.1 /<br />
                                                        16 set &#8211;<br />
    destination 0x010003<br />
#&#8230; etc<br />
#MULTICAST<br />
        match 224 /<br />
        4 set &#8211;<br />
    destination 0x050019 tag &#8211; action OHIO &#8211; GIGAPOP_SRC type source &#8211; prefix<br />
#OSU<br />
                                                                               match 128.146 /<br />
                                                                           16 set &#8211;<br />
    source 0x010001 match 164.107 / 16 set &#8211; source 0x010001 match 140.254 / 16 set &#8211; source 0x010001 match 192.153.26 / 24 set &#8211; source 0x010001<br />
#CWRU<br />
                                                                                                                                      match 129.22 /<br />
                                                                                                                                      16 set &#8211;<br />
    source 0x010002 match 192.5.110 / 24 set &#8211; source 0x010002<br />
#BGSU<br />
                                                   match 129.1 /<br />
                                                   16 set &#8211;<br />
    source 0x010003<br />
#&#8230; etc<br />
    tag &#8211;<br />
    action OTHER_DST<br />
        type destination &#8211;<br />
    prefix<br />
            match 0 /<br />
        0 set &#8211;<br />
    destination 0x0</p>
<p>    tag &#8211;<br />
    action OTHER_SRC<br />
        type source &#8211;<br />
    prefix<br />
            match 0 /<br />
        0 set &#8211;<br />
    source 0x0 tag &#8211; definition OHIO &#8211; GIGAPOP term<br />
#Abilene interface<br />
                                           input &#8211;<br />
    filter 25<br />
#clear tag first&#8211; it defaults to 0, so this may not be necessary.<br />
    action OTHER_DST<br />
        action OHIO &#8211;<br />
    GIGAPOP_DST<br />
        term<br />
#Abilene interface<br />
            output &#8211;<br />
    filter 25<br />
#clear tag first&#8211; it defaults to 0, so this may not be necessary.<br />
    action OTHER_SRC<br />
        action OHIO &#8211;<br />
    GIGAPOP_SRC</p>
<p> First populate <i>/etc/flow-tools/sym/tag</i> for <code>flow-stat</code> to use as symbols. </p>
<pre>
0x0001 OSU
0x0002 CWRU
0x0003 BGSU
0x0019 MULTICAST
0x010000 PART
0x020000 SEGP
0x030000 SPART
0x040000 GIGAPOP
0x050000 MULTICAST
</pre>
<p> To generate a report for outgoing traffic to Abilene based on customer ID: </p>
<pre>
flow-cat <i>flows</i> | flow-filter -I25 | flow-tag -t gigapop-tags -TOHIO-GIGAPOP | flow-xlate -t0x0000FFFF | flow-stat -n -f30 -S2
</pre>
<p>#&#8211; &#8211; &#8212; &#8212; &#8212; &#8212; Report Information &#8212; &#8211; &#8212; &#8211; &#8212; &#8211;<br />
#<br />
#Fields : Total<br />
#Symbols : Enabled<br />
#Sorting : Descending Field 2<br />
#Name : Source Tag<br />
#<br />
#Args :../ flow &#8211; stat &#8211; n &#8211; f30 &#8211; S2<br />
#<br />
#<br />
#Src Tag flows octets packets<br />
#<br />
OSU 4942230 181326237007 302476793 CWRU 874883 54358312807 70589318 BGSU 1008797 7600209852 22060870</p>
<p> To generate a report for inbound traffic from Abilene based on customer type: </p>
<pre>
flow-cat <i>flows</i> | flow-filter -i25 | flow-tag -t gigapop-tags -TOHIO-GIGAPOP | flow-xlate -T0xFF0000 | flow-stat -n -f31 -S2
</pre>
<pre><code>
#-- - -- -- -- -- Report Information -- - -- - -- -
#
#Fields : Total
#Symbols : Enabled
#Sorting : Descending Field 2
#Name : Destination Tag
#
#Args :../ flow - stat - n - f31 - S2
#
#
#Dst Tag flows octets packets
#
PART 15923156 663289954569 981163979 SEGP 4995795 135525076170 196534917 MULTICAST 45171 49866825003 137798118 GIGAPOP 942209 26422533266 23199961 SPART 73998 5170323905 7597985
</code></pre>
<h2>FILES</h2>
<p> Configuration files: Symbols &#8211; <i>/etc/flow-tools/sym/*</i>. Tag &#8211; <i>/etc/flow-tools/cfg/tag.cfg</i>.</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
