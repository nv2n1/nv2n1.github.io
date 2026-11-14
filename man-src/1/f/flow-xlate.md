---
title: "flow-xlate(1)"
name: "flow-xlate"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-xlate/"
description: "flow-xlate – Apply translations to selected fields of a flow."
---

<h2>NAME</h2>
<p> flow-xlate &#8211; Apply translations to selected fields of a flow.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-xlate</code> [ <code>-hkn</code> ] [ <code>-b</code><i> big</i><code>|</code><i>little</i> ] [ <code>-C</code><i> comment</i> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-v</code><i> variable binding</i> ] [ <code>-V</code><i> flow_version</i> ] [ <code>-x</code><i> xlate_fname</i> ] [ <code>-X</code><i> xlate_definition</i> ] [ <code>-z</code><i> z_level</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-xlate</code> utility is used to apply translations to flows. Translations are defined in a configuration file and are composed of actions and a definition to invoke action(s). The definitions are in the form of terms, each term can have a filter and multiple actions. </p>
<p> Words in the configuration file of the form @VAR or @{VAR:default} will be expanded at run-time by setting variable names with the -v option. </p>
<p> Translation actions begin with the xlate-action keyword followed by a symbolic name. Each action has a type defined below. </p>
<p> Translation definitions begin with the xlate-definition keyword followed by a symbolic name. Each definition is composed of terms which are evaluated in the order of the configuration file. A term may invoke a filter to conditionally invoke an action. </p>
<pre><code>
Action type / sub - commands Description / Example-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --ip - source - address - to - network Zero host bits based on mask.ip - destination - address - to - network Zero host bits based on mask.(no sub - commands) ip - source - address - to - class - network Zero source host bits to match class.ip - destination - address - to - class - network Zero dst host bits to match class.

                                                                                                                                                                                                                                                                                                                                                                                                                                                      (no sub - commands) ip
    - source - address - anonymize Anonymize source address.ip - destination - address - anonymize Anonymize destination address.ip - address - anonymize Anonymize src / dst address.algorithm Algorithm.cryptopan - aes128 is currently supported.algorithm cryptopan - aes128 key Key.Key is 128 bits in hex.key 0123456789ABCDEFG key - file File to load key from.Key is 128 bits in hex.key - file / mfstmp / secret - key key - file - refresh How often to check the key file.Interval is in minutes,
    the
        optional second argument is
        hour : min : sec to specify the
                     first refresh.This example
                     will load a new key every day
                     at 12 : 00 : 00. 14400 12 : 00 : 00 ip
        - address - privacy - mask Apply a mask to the source and destination address to remove bits.ip - port - privacy - mask Apply a mask to the source and destination port to remove bits.tag - mask Apply mask to the source and destination tag.mask Source and Destination mask to apply.mask 0xFFFF 0xFFFF scale Scale packets and bytes.scale Scale to apply.scale 100 replace - source - as0 Replace source AS 0 replace - destination - as0 Replace destination AS 0 as AS replacement value.as 3112
</code></pre>
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
<dt><code>-n</code></p>
<dd> Don&#8217;t load configuration file. Useful only with -V</p>
<dt><code>-v</code><i> variable binding</i></p>
<dd> Set a variable FOO=bar.</p>
<dt><code>-V</code><i> pdu_version</i></p>
<dd> Use <i>pdu_version</i> format output. </p>
<pre>
    1    NetFlow version 1 (No sequence numbers, AS, or mask)
    5    NetFlow version 5
    6    NetFlow version 6 (5+ Encapsulation size)
    7    NetFlow version 7 (Catalyst switches)
    8.1  NetFlow AS Aggregation
    8.2  NetFlow Proto Port Aggregation
    8.3  NetFlow Source Prefix Aggregation
    8.4  NetFlow Destination Prefix Aggregation
    8.5  NetFlow Prefix Aggregation
    8.6  NetFlow Destination (Catalyst switches)
    8.7  NetFlow Source Destination (Catalyst switches)
    8.8  NetFlow Full Flow (Catalyst switches)
    8.9  NetFlow ToS AS Aggregation
    8.10 NetFlow ToS Proto Port Aggregation
    8.11 NetFlow ToS Source Prefix Aggregation
    8.12 NetFlow ToS Destination Prefix Aggregation
    8.13 NetFlow ToS Prefix Aggregation
    8.14 NetFlow ToS Prefix Port Aggregation
    1005 Flow-Tools tagged version 5
</pre>
<dt><code>-x</code><i> xlate_fname</i></p>
<dd> Translation config file name. Defaults to <i>/etc/flow-tools/cfg/xlate.cfg</i></p>
<dt><code>-X</code><i> xlate_definition</i></p>
<dd> Translation definition. Defaults to default.</p>
<dt><code>-z</code><i> z_level</i></p>
<dd> Configure compression level to <i> z_level</i>. 0 is disabled (no compression), 9 is highest compression.</dl>
<h2>EXAMPLES</h2>
<p> Convert the version 7 flows in <i>flows.v7</i> to version 5, storing the result in <i>flows.v5</i>. </p>
<p> <code>flow-xlate -V5 &lt; flows.v7 &gt; flows.v5</code> </p>
<p> Set the low 11 bits in the IP addresses to zero unless the address is multicast or it belongs to the 192.88.99/24 network. </p>
<pre>
# xlate.cfg
include-filter filter.cfg
xlate-action MULTICAST-PRIVACY
  type ip-address-privacy-mask
  mask 0xFFFFFFFF 0xFFFFFFFF  
  
xlate-action UNICAST-PRIVACY
  type ip-address-privacy-mask
  mask 0xFFFFFF00 0xFFFFF800
xlate-definition abilene_privacy
  term
    filter mcast
    action MULTICAST-PRIVACY
    stop
  term
    filter ucast
    action UNICAST-PRIVACY
</pre>
<pre>
# filter.cfg
filter-primitive MCAST
  type ip-address-mask
  permit 224.0.0.0 240.0.0.0
filter-primitive UCAST
  type ip-address-mask
  deny 224.0.0.0 240.0.0.0
  default permit
filter-primitive SKIP
  type ip-address-mask
  deny 192.88.99.0 255.255.255.0
  default permit
filter-definition mcast
  match ip-destination-address MCAST
filter-definition ucast
  match ip-destination-address UCAST
  match ip-destination-address SKIP
  match ip-source-address SKIP
</pre>
<p> <code>flow-cat </code><i>flows</i><code> | flow-xlate -xxlate.cfg -Xabilene_privacy | flow-print</code></p>
<h2>FILES</h2>
<p> Configuration files: Symbols &#8211; <i>/etc/flow-tools/sym/*</i>. Filter &#8211; <i>/etc/flow-tools/cfg/filter.cfg</i>. Xlate &#8211; <i>/etc/flow-tools/cfg/xlate.cfg</i>.</p>
<h2>BUGS</h2>
<p> The scale option can overflow the 32 bit flow counters. This could be solved by detecting this condition and splitting the flow in two. </p>
<p> Translation between aggregated and non aggregated formats is not supported.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
