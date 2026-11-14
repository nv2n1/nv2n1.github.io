---
title: "shorewall-actions(5)"
name: "shorewall-actions"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-actions/"
description: "actions – Shorewall action declaration file"
---

<p>actions &#8211; Shorewall action declaration file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/actions</code></dl>
<h2>Description</h2>
<dd>This file allows you to define new ACTIONS for use in rules (see m[blue]<code><a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5)</code>m[]<font SIZE="-2">[1]</font>). You define the iptables rules to be performed in an ACTION in /etc/shorewall/action.<i>action-name</i>. Columns are: NAME</p>
<dl>
<dd>The name of the action. ACTION names should begin with an upper-case letter to distinguish them from Shorewall-generated chain names and be composed of letters, digits or numbers. If you intend to log from the action then the name must be no longer than 11 characters in length if you use the standard LOGFORMAT.</dl>
<p> OPTIONS</p>
<dl>
<dd>Added in Shorewall 4.5.10. Available options are: <code>audit</code></p>
<dl>
<dd>Added in Shorewall 5.0.7. When this option is specified, the action is expected to have at least two parameters; the first is a target and the second is either &#8216;audit&#8217; or omitted. If the second is &#8216;audit&#8217;, then the first must be an auditable target (ACCEPT, DROP or REJECT).</dl>
<p> <code>builtin</code></p>
<dl>
<dd>Added in Shorewall 4.5.16. Defines the action as a rule target that is supported by your iptables but is not directly supported by Shorewall. The action may be used as the rule target in an INLINE rule in m[blue]<code>shorewall-rules</code>m[]<font SIZE="-2">[1]</font>(5). Beginning with Shorewall 4.6.0, the Netfilter table(s) in which the <code>builtin</code> can be used may be specified: <code>filter</code>, <code>nat</code>, <code>mangle</code> and <code>raw</code>. If no table name(s) are given, then <code>filter</code> is assumed. The table names follow <code>builtin</code> and are separated by commas; for example, &quot;FOOBAR builtin,filter,mangle&quot; would specify FOOBAR as a builtin target that can be used in the filter and mangle tables. Beginning with Shorewall 4.6.4, you may specify the <code>terminating</code> option with <code>builtin</code> to indicate to the Shorewall optimizer that the action is terminating (the current packet will not be passed to the next rule in the chain).</dl>
<p> <code>inline</code></p>
<dl>
<dd>Causes the action body (defined in action.<i>action-name</i>) to be expanded in-line like a macro rather than in its own chain. You can list Shorewall Standard Actions in this file to specify the <code>inline</code> option.</p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 Some of the Shorewall standard actions cannot be used in-line and will generate a warning and the compiler will ignore <code>inline</code> if you try to use them that way:</p>
<dl>
<dd>DropSmurfs</dl>
<dl>
<dd>IfEvent</dl>
<dl>
<dd>Invalid (Prior to Shorewall 4.5.13)</dl>
<dl>
<dd>NotSyn (Prior to Shorewall 4.5.13)</dl>
<dl>
<dd>RST (Prior to Shorewall 4.5.13)</dl>
<dl>
<dd>TCPFlags</dl>
<p>  <code>logjump</code></p>
<dl>
<dd>Added in Shorewall 5.0.8. Performs the same function as <code>nolog</code> (below), with the addition that the jump to the actions chain is logged if a log level is specified on the action invocation. For inline actions, this option is identical to <code>nolog</code>.</dl>
<p> <code>mangle</code></p>
<dl>
<dd>Added in Shorewall 5.0.7. Specifies that this action is to be used in m[blue]<code><a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5)</code>m[]<font SIZE="-2">[2]</font> rather than m[blue]<code><a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5)</code>m[]<font SIZE="-2">[3]</font>.</dl>
<p> <code>nat</code></p>
<dl>
<dd>Added in Shorewall 5.0.13. Specifies that this action is to be used in m[blue]<code><a href="/docs/linux/man/5-shorewall-snat/">shorewall-snat</a>(5)</code>m[]<font SIZE="-2">[4]</font> rather than m[blue]<code><a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5)</code>m[]<font SIZE="-2">[3]</font>. The <code>mangle</code> and <code>nat</code> options are mutually exclusive.</dl>
<p> <code>noinline</code></p>
<dl>
<dd>Causes any later <code>inline</code> option for the same action to be ignored with a warning.</dl>
<p> <code>nolog</code></p>
<dl>
<dd>Added in Shorewall 4.5.11. When this option is specified, the compiler does not automatically apply the log level and/or tag from the invocation of the action to all rules inside of the action. Rather, it simply sets the $_loglevel and $_logtag shell variables which can be used within the action body to apply those logging options only to a subset of the rules.</dl>
<p> <code>state</code>={<code>UNTRACKED</code>|<code>NEW</code>|<code>ESTABLISHED</code>|<code>RELATED</code>|<code>INVALID</code>}</p>
<dl>
<dd>Added in Shorewall 5.0.7. Reserved for use by Shorewall in actions.std.</dl>
<p> <code>terminating</code></p>
<dl>
<dd>Added in Shorewall 4.6.4. When used with <i>builtin</i>, indicates that the built-in action is termiating (i.e., if the action is jumped to, the next rule in the chain is not evaluated).</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/actions</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/Actions.html">http://www.shorewall.net/Actions.html</a></code>m[]<font SIZE="-2">[5]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-rules.html">http://www.shorewall.net/manpages/shorewall-rules.html</a></dl>
<dt> 2.</p>
<dd><a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall-mangle.html">http://www.shorewall.netshorewall-mangle.html</a></dl>
<dt> 3.</p>
<dd><a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall-rules.html">http://www.shorewall.netshorewall-rules.html</a></dl>
<dt> 4.</p>
<dd><a href="/docs/linux/man/5-shorewall-snat/">shorewall-snat</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall-snat.html">http://www.shorewall.netshorewall-snat.html</a></dl>
<dt> 5.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/Actions.html">http://www.shorewall.net/Actions.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/Actions.html">http://www.shorewall.net/Actions.html</a></dl>
