---
title: "shorewall6-ipsets(5)"
name: "shorewall6-ipsets"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-ipsets/"
description: "ipsets – Specifying the name if an ipset in Shorewall6 configuration files"
---

<p>ipsets &#8211; Specifying the name if an ipset in Shorewall6 configuration files</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>+</code><i>ipsetname</i></p>
<dt> <code>+</code><i>ipsetname</i><code>[</code><i>flag</i><code>,&#8230;]</code></p>
<dt> <code>+[ipsetname,&#8230;]</code></dl>
<h2>Description</h2>
<dd>Note: In the above syntax descriptions, the square brackets (&quot;[]&quot;) are to be taken literally rather than as meta-characters. In most places where a network address may be entered, an ipset may be substituted. Set names must be prefixed by the character &quot;+&quot;, must start with a letter and may be composed of alphanumeric characters, &quot;-&quot; and &quot;_&quot;. Whether the set is matched against the packet source or destination is determined by which column the set name appears (SOURCE or DEST). For those set types that specify a tuple, two alternative syntaxes are available:</p>
<dl>
<dd>[<i>number</i>] &#8211; Indicates that &#8216;src&#8217; or<br />
&#8216;dst&#8217;&nbsp;<wbr>should repeated number times. Example: myset[2].</dl>
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
<p> Beginning with Shorewall 4.4.14, multiple source or destination matches may be specified by enclosing the set names within +[&#8230;]. The set names need not be prefixed with &#8216;+&#8217;. When such a list of sets is specified, matching packets must match all of the listed sets. For information about set lists and exclusion, see m[blue]<code>shorewall6-exclusion</code>m[]<font SIZE="-2">[1]</font> (5). Beginning with Shorewall 4.5.16, you can increment one or more nfacct objects each time a packet matches an ipset. You do that by listing the objects separated by commas within parentheses. Example:</p>
<dl>
<dd>+myset[src](myobject)</dl>
<p> In that example, when the source address of a packet matches the <code>myset</code> ipset, the <code>myobject</code> nfacct counter will be incremented. Beginning with Shorewall 4.6.0, an ipset name (and src/dst list, if any) can be immediately be followed by a list of match options.</p>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font><br />
 These additional match options are not available in m[blue]<code><a href="/docs/linux/man/5-shorewall6-tcfilters/">shorewall6-tcfilters</a>(5)</code>m[]<font SIZE="-2">[2]</font>.  Available options are: nomatch</p>
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
<p>+myset </p>
<p> +myset[src] </p>
<p> +myset[2] </p>
<p> +[myset1,myset2[dst]] </p>
<p> +myset[src,nomatch,packets&gt;100] </p>
<p> +myset[nomatch,no-update-counters](myObject)</p>
<h2>Files</h2>
<p>/etc/shorewall6/accounting </p>
<p> /etc/shorewall6/blrules </p>
<p> /etc/shorewall6/hosts &#8212; <code>Note:</code> Multiple matches enclosed in +[&#8230;] may not be used in this file. </p>
<p> /etc/shorewall6/maclist &#8212; <code>Note:</code> Multiple matches enclosed in +[&#8230;] may not be used in this file. </p>
<p> /etc/shorewall6/rules </p>
<p> /etc/shorewall6/secmarks </p>
<p> /etc/shorewall6/mangle</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall6-exclusion</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-exclusion.html">http://www.shorewall.net/manpages6/shorewall6-exclusion.html</a></dl>
<dt> 2.</p>
<dd><a href="/docs/linux/man/5-shorewall6-tcfilters/">shorewall6-tcfilters</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall6-tcfilters.html">http://www.shorewall.netshorewall6-tcfilters.html</a></dl>
