---
title: "shorewall-ipsets(5)"
name: "shorewall-ipsets"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-ipsets/"
description: "ipsets – Specifying the name if an ipset in Shorewall configuration files"
---

<p>ipsets &#8211; Specifying the name if an ipset in Shorewall configuration files</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>+</code><i>ipsetname</i></p>
<dt> <code>+</code><i>ipsetname</i><code>[</code><i>flag</i><code>,&#8230;]</code></p>
<dt> <code>+[ipsetname,&#8230;]</code></dl>
<h2>Description</h2>
<dd>Note: In the above syntax descriptions, the square brackets (&quot;[]&quot;) are to be taken literally rather than as meta-characters. In most places where a network address may be entered, an ipset may be substituted. Set names must be prefixed by the character &quot;+&quot;, must start with a letter and may be composed of alphanumeric characters, &quot;-&quot; and &quot;_&quot;. Whether the set is matched against the packet source or destination is determined by which column the set name appears (SOURCE or DEST). For those set types that specify a tuple, two alternative syntaxes are available:</p>
<dl>
<dd>[<i>number</i>] &#8211; Indicates that &#8216;src&#8217; or<br />
&#8216;dst&#8217;&nbsp;<wbr>should be repeated&nbsp;<wbr><i>number</i>&nbsp;<wbr>times.<br />
Example: myset[2].</dl>
<dl>
<dd>[<i>flag</i>,&#8230;] where<br />
<i>flag</i>&nbsp;<wbr>is&nbsp;<wbr><code>src</code>&nbsp;<wbr>or<br />
<code>dst</code>. Example: myset[src,dst].</dl>
<p> In a SOURCE or SPORT column, the following pairs are equivalent:</p>
<dl>
<dd>&bull; +myset[2] and +myset[src,src]</dl>
<p> In a DEST or DPORT column, the following pairs are equivalent:</p>
<dl>
<dd>&bull; +myset[2] and +myset[dst,dst]</dl>
<p> Beginning with Shorewall 4.4.14, multiple source or destination matches may be specified by enclosing the set names within +[&#8230;]. The set names need not be prefixed with &#8216;+&#8217;. When such a list of sets is specified, matching packets must match all of the listed sets. For information about set lists and exclusion, see m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[1]</font> (5). Beginning with Shorewall 4.5.16, you can increment one or more nfacct objects each time a packet matches an ipset. You do that by listing the objects separated by commas within parentheses. Example:</p>
<dl>
<dd>+myset[src](myobject)</dl>
<p> In that example, when the source address of a packet matches the <code>myset</code> ipset, the <code>myobject</code> nfacct counter will be incremented. Beginning with Shorewall 4.6.0, an ipset name (and src/dst list, if any) can be immediately be followed by a list of match options.</p>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font><br />
 These additional match options are not available in m[blue]<code><a href="/docs/linux/man/5-shorewall-tcfilters/">shorewall-tcfilters</a>(5)</code>m[]<font SIZE="-2">[2]</font>.  Available options are: nomatch</p>
<dl>
<dd>If the set type supports the nomatch flag, then the matching is reversed: a match with an element flagged with nomatch returns true, while a match with a plain element returns false. This option requires the &#8216;Ipset Match nomatch&#8217; capability in your kernel and ip[6]tables.</dl>
<p> no-update-counters</p>
<dl>
<dd>The packet and byte counters of the matching element in the set won&#8217;t be updated. By default, the packet and byte counters are updated. This option and those that follow require the &#8216;Ipset Match counters&#8217; capability in your kernel and ip[6]tables.</dl>
<p> no-update-subcounters</p>
<dl>
<dd>The packet and byte counters of the matching element in the member set of a list type of set won&#8217;t be updated. Default the packet and byte counters are updated.</dl>
<p> packets=<i>value</i></p>
<dl>
<dd>If the packet is matched an element in the set, match only if the packet counter of the element matches the given <i>value</i> also.</dl>
<p> packets&lt;<i>value</i></p>
<dl>
<dd>If the packet is matched an element in the set, match only if the packet counter of the element is less than the given <i>value</i> as well.</dl>
<p> packets&gt;<i>value</i></p>
<dl>
<dd>If the packet is matched an element in the set, match only if the packet counter of the element is greater than the given <i>value</i> as well.</dl>
<p> packets!=<i>value</i></p>
<dl>
<dd>If the packet is matched an element in the set, match only if the packet counter of the element does not match the given <i>value</i> also.</dl>
<p> bytes=<i>value</i></p>
<dl>
<dd>If the packet is matched an element in the set, match only if the byte counter of the element matches the given <i>value</i> also.</dl>
<p> bytes&lt;<i>value</i></p>
<dl>
<dd>If the packet is matched an element in the set, match only if the byte counter of the element is less than the given <i>value</i> as well.</dl>
<p> bytes&gt;<i>value</i></p>
<dl>
<dd>If the packet is matched an element in the set, match only if the byte counter of the element is greater than the given <i>value</i> as well.</dl>
<p> bytes&lt;&gt;<i>value</i></p>
<dl>
<dd>If the packet is matched an element in the set, match only if the byte counter of the element does not match the given <i>value</i> also.</dl>
<h2>Examples</h2>
<p>In the examples that follow, myset, myset1 and myset2 are ipsets and myObject is an NFacct object name. </p>
<p> +myset </p>
<p> +myset[src] </p>
<p> +myset[2] </p>
<p> +[myset1,myset2[dst]] </p>
<p> +myset[src](myObject) </p>
<p> +myset[src,nomatch,packets&gt;100] </p>
<p> +myset[nomatch,no-update-counters](myObject)</p>
<h2>Files</h2>
<p>/etc/shorewall/accounting </p>
<p> /etc/shorewall/blrules </p>
<p> /etc/shorewall/hosts &#8212; <code>Note:</code> Multiple matches enclosed in +[&#8230;] may not be used in this file. </p>
<p> /etc/shorewall/maclist &#8212; <code>Note:</code> Multiple matches enclosed in +[&#8230;] may not be used in this file. </p>
<p> /etc/shorewall/masq </p>
<p> /etc/shorewall/rules </p>
<p> /etc/shorewall/secmarks </p>
<p> /etc/shorewall/mangle</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall-exclusion</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-exclusion.html">http://www.shorewall.net/manpages/shorewall-exclusion.html</a></dl>
<dt> 2.</p>
<dd><a href="/docs/linux/man/5-shorewall-tcfilters/">shorewall-tcfilters</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall-tcfilters.html">http://www.shorewall.netshorewall-tcfilters.html</a></dl>
