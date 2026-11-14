---
title: "flow-nfilter(1)"
name: "flow-nfilter"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-nfilter/"
description: "flow-nfilter – Filter flows."
---

<h2>NAME</h2>
<p> flow-nfilter &#8211; Filter flows.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-nfilter</code> [ <code>-hk</code> ] [ <code>-b</code><i> big</i><code>|</code><i>little</i> ] [ <code>-C</code><i> comment</i> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-f</code><i> filter_fname</i> ] [ <code>-F</code><i> filter_definition</i> ] [ <code>-v</code><i> variable binding</i> ] [ <code>-z</code><i> z_level</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-nfilter</code> utility will filter flows based on user selectable criteria. Filters are defined in a configuration file and are composed of primitives and a definition. Definitions contain match lines grouped to form logical AND and OR operations on the flow using the selected primitives. A definition may contain the invert command which will invert the result of the evaluation. </p>
<p> Words in the configuration file of the form @VAR or @{VAR:default} will be expanded at run-time by setting variable names with the -v option. </p>
<p> Filter primitives begin with the filter-primitive keyword followed by a symbolic name. Each primitive has a type defined below. A list of permit and or deny keywords followed by an argument are later evaulated to determine if the flow is permitted or denied. The default action for a primitive is to deny which may be changed with the default keyword. Symbolic substitutions are done where appropriate. </p>
<p> The match keyword in a definition selects the criteria to match a primitive. A match type may allow more than one type of primitive, for example the src-ip-addr match type will accept any of {ip-address, ip-address-mask, ip-address-prefix} primitive types. </p>
<pre><code>
Primitive type Type Description / Example-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -as Bucket Autonomous System Number.600, 159, 3112 ip - address - prefix - len Numeric Integer from 0 to 32. 16 - 31 ip - protocol Bucket Integer from 0 to 255. 6, 17, 1 ip - tos Bucket Integer from 0 to 255 with mask.0xA0 / 0xE0 ip - tcp - flags Bucket Integer from 0 to 255 with mask.0x2 / 0x2 ifindex Bucket Integer from 0 to 65535 0, 5, 10 engine Bucket Integer from 0 to 255. 0 ip - port Bucket Integer from 0 to 65535. 80, 8080, 23, 22 ip - address Hash List of IP Addresses.10.0.0.1 ip - address - mask List List of IP address / mask pairs.10.1.0.0 255.255.0.0 ip - address - prefix Trie List of IP address / mask pairs.10.1 / 16 tag Hash List of tags.0xFF00 tag - mask List List of tags.0xF000 / 0xFF00 counter List List of Integers with qualifier.lt 32 time List List of relative time specifiers.gt 5 : 00 time - date List List of absolute time specifiers.gt December 12, 2002 5 : 13 : 21 double List List of doubles with qualifier.lt 32.0 rate Element Rate is calculated as 1 / rate.permit 100 Match type Description Primitives accepted-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -source - as Source AS as destination - as Destination AS as ip - source - address Source IP Address ip - address,
    ip - address - mask,
    ip - address - prefix ip - destination - address Destination IP Address ip - address,
    ip - address - mask,
    ip - address - prefix ip - exporter - address Exporter IP Address ip - address,
    ip - address - mask,
    ip - address - prefix ip - nexthop - address NextHop IP Address ip - address,
    ip - address - mask,
    ip - address - prefix ip - shortcut - address Shortcut IP Address ip - address,
    ip - address - mask,
    ip - address - prefix ip - protocol IP Protocol ip - protocol ip - source - address - prefix - len Source IP address ip - address - prefix - len prefix length ip - destination - address - prefix - len Destination IP address ip - address - prefix - len prefix length

                                                                                                                                                                                                                                                                ip -
        tos IP Type Of Service ip - tos ip - marked - tos IP Type Of Service ip - tos ip - tcp - flags IP / TCP Flags ip - tcp - flags ip - source - port Source IP Port ip - port eg TCP / UDP ip - destination - port Destination IP Port ip - port eg TCP / UDP input - interface Source ifIndex ifindex eg Input Interface output - interface Destination ifIndex ifindex eg Output Interface start - time Start Time of flow time,
    time - date end - time End Time of Flow time, time - date flows Number of flows counter octets Number of octets counter packets Number of packets counter duration Duration of flow in ms counter engine - id Engine ID engine engine - type Engine Type engine source - tag Source Tag tag, tag - mask destination - tag Destination Tag tag, tag - mask pps Packets Per Second double bps Bits Per Second double random - sample Random Sample rate
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code><i> big</i><code>|</code><i>little</i></p>
<dd> Byte order of output.</p>
<dt><code>-C</code><i> Comment</i></p>
<dd> Add a comment.</p>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-f</code><i> filter_fname</i></p>
<dd> Filter list filename. Defaults to <i>/etc/flow-tools/cfg/filter</i>.</p>
<dt><code>-F</code><i> filter_definition</i></p>
<dd> Select the active definition. Defaults to default.</p>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-k</code></p>
<dd> Keep time from input.</p>
<dt><code>-v</code><i> variable binding</i></p>
<dd> Set a variable FOO=bar.</p>
<dt><code>-z</code><i> z_level</i></p>
<dd> Configure compression level to <i> z_level</i>. 0 is disabled (no compression), 9 is highest compression.</dl>
<h2>TIME/DATE PARSING</h2>
<p> time-date parsing is implemented with <i>getdate.y</i>, a commonly used function to process free-form time date specifications. Example usage borrowed from <code>cvs</code>: 1 month ago 2 hours ago 400000 seconds ago last year last Monday yesterday a fortnight ago 3/31/92 10:00:07 PST January 23, 1987 10:05pm 22:00 GMT</p>
<h2>EXAMPLES</h2>
<p> An example of filter configuration file. </p>
<pre>
filter-primitive srate
  type rate
  permit 100
filter-primitive test-as
  type as
  permit 600,159
filter-primitive test-prefix-len
  type ip-address-prefix-len
  permit 32
filter-primitive test-protocol
  type ip-protocol
  permit tcp
filter-primitive test-tos
  type ip-tos
  mask 0xA0
  permit 0xE0
filter-primitive test-tcp-flags
  type ip-tcp-flags
  mask 0x2
  permit 0x2
filter-primitive test-ifindex
  type ifindex
  permit 0,5,10
filter-primitive test-engine
  type engine
  permit 0
filter-primitive test-port
  type ip-port
  permit https
  permit 80
  default deny
filter-primitive test-address
  type ip-address
  permit 0.0.0.1
  permit 0.0.0.2
  default deny
filter-primitive test-address-mask
  type ip-address-mask
  permit 128.146.197.1 255.255.255.255
  permit 128.146.197.2 255.255.255.255
filter-primitive test-prefix
  type ip-address-prefix
  permit 128.146.0.0/16
  default deny
filter-primitive test-tag
  type tag
  permit 0x00
  permit 0x01
  permit 0xFF
filter-primitive test-tag-mask
  type tag-mask  
  permit OSU 0xFF
  permit 0xFF 0xFF
  default deny
filter-primitive test-counter
  type counter
  permit lt 5 
  permit gt 10
  default deny
filter-primitive test-time-date
  type time-date
  permit gt December 12, 2002 5:13:21
filter-primitive test-time
  type time-date
  permit gt 12:15:00
filter-definition sample-1-in-100
  match random-sample srate
filter-definition t1
  match engine-type test-engine
  or
  match destination-tag test-tag-mask
</pre>
<p> Display all flows with a destination port of 80 or source port of 25 (smtp) starting after Dec 12, 2001. The file <i>test</i> is populated with the following: </p>
<pre>
filter-primitive port80
  type ip-port
  permit 80
filter-primitive port25
  type ip-port
  permit smtp
filter-primitive dec12
  type time-date
  permit gt Dec 12, 2001
filter-definition foo
  match ip-source-port port80
  match start-time dec12
  or
  match ip-destination-port port25
  match start-time dec12
</pre>
<p> <code>flow-cat </code><i>flows</i><code> | flow-nfilter -ftest -Ffoo | flow-print</code></p>
<h2>FILES</h2>
<p> Configuration files: Symbols &#8211; <i>/etc/flow-tools/sym/*</i>. Tag &#8211; <i>/etc/flow-tools/cfg/tag.cfg</i>. Filter &#8211; <i>/etc/flow-tools/cfg/filter.cfg</i>.</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
