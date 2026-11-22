---
title: "ip-neighbour(8)"
name: "ip-neighbour"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-neighbour/"
description: "ip-neighbour – neighbour/arp tables management."
---

<p>ip-neighbour &#8211; neighbour/arp tables management.</p>
<h2>Synopsis</h2>
<pre><code>ip
[ OPTIONS ]
neigh
{ COMMAND |
    help }
</code></pre>
<p> <code>ip neigh</code> { <code>add</code> | <code>del</code> | <code>change</code> | <code>replace</code> } { <i>ADDR</i> [ <code>lladdr</code> <i>LLADDR</i> ] [ <code>nud</code> <i>STATE</i> ] | <code>proxy</code> <i>ADDR</i> } [ <code>dev</code> <i>DEV</i> ] [ <code>router</code> ] [ <code>extern_learn</code> ]<br/>
 <code>ip neigh</code> { <code>show</code> | <code>flush</code> } [ <code>proxy</code> ] [ <code>to</code> <i>PREFIX</i> ] [ <code>dev</code> <i>DEV</i> ] [ <code>nud</code> <i>STATE</i> ] [ <code>vrf</code> <i>NAME</i> ]<br/>
 <code>ip neigh get</code> <i>ADDR</i> <code>dev</code> <i>DEV</i> </p>
<pre><code>STATE := {
    permanent | noarp | stale | reachable | none |
    incomplete | delay | probe | failed }
</code></pre>
<h2>Description</h2>
<p>The <code>ip neigh</code> command manipulates <i>neighbour</i> objects that establish bindings between protocol addresses and link layer addresses for hosts sharing the same link. Neighbour entries are organized into tables. The IPv4 neighbour table is also known by another name &#8211; the ARP table. The corresponding commands display neighbour bindings and their properties, add new neighbour entries and delete old ones.</p>
<dl>
<dt>ip neighbour add</dt>
<dd>add a new neighbour entry</dd>
<dt>ip neighbour change</dt>
<dd>change an existing entry</dd>
<dt>ip neighbour replace</dt>
<dd>add a new entry or change an existing one</dd>
<dl>
<dd>These commands create new neighbour records or update existing ones.</dd>
<dl>
<dt><code>to</code><i> ADDRESS </i><code>(default)</code></dt>
<dd>the protocol address of the neighbour. It is either an IPv4 or IPv6 address.</dd>
<dt><code>dev</code><i> NAME</i></dt>
<dd>the interface to which this neighbour is attached.</dd>
<dt><code>proxy</code></dt>
<dd>indicates whether we are proxying for this neighbour entry</dd>
<dt><code>router</code></dt>
<dd>indicates whether neighbour is a router</dd>
<dt><code>extern_learn</code></dt>
<dd>this neigh entry was learned externally. This option can be used to indicate to the kernel that this is a controller learnt dynamic entry. Kernel will not gc such an entry.</dd>
<dt><code>lladdr</code><i> LLADDRESS</i></dt>
<dd>the link layer address of the neighbour. <i>LLADDRESS</i> can also be <code>null</code>.</dd>
<dt><code>nud</code><i> STATE</i></dt>
<dd>the state of the neighbour entry. <code>nud</code> is an abbreviation for &#8216;Neighbour Unreachability Detection&#8217;. The state can take one of the following values:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>permanent</code></dt>
<dd>the neighbour entry is valid forever and can be only be removed administratively.</dd>
<dt><code>noarp</code></dt>
<dd>the neighbour entry is valid. No attempts to validate this entry will be made but it can be removed when its lifetime expires.</dd>
<dt><code>reachable</code></dt>
<dd>the neighbour entry is valid until the reachability timeout expires.</dd>
<dt><code>stale</code></dt>
<dd>the neighbour entry is valid but suspicious. This option to <code>ip neigh</code> does not change the neighbour state if it was valid and the address is not changed by this command.</dd>
<dt><code>none</code></dt>
<dd>this is a pseudo state used when initially creating a neighbour entry or after trying to remove it before it becomes free to do so.</dd>
<dt><code>incomplete</code></dt>
<dd>the neighbour entry has not (yet) been validated/resolved.</dd>
<dt><code>delay</code></dt>
<dd>neighbor entry validation is currently delayed.</dd>
<dt><code>probe</code></dt>
<dd>neighbor is being probed.</dd>
<dt><code>failed</code></dt>
<dd>max number of probes exceeded without success, neighbor validation has ultimately failed.</dd></dl>
</dl>
</dl>
</dl>
<dt>ip neighbour delete</dt>
<dd>delete a neighbour entry</dd>
<dl>
<dd>The arguments are the same as with <code>ip neigh add</code>, except that <code>lladdr</code> and <code>nud</code> are ignored. <code>Warning:</code> Attempts to delete or manually change a <code>noarp</code> entry created by the kernel may result in unpredictable behaviour. Particularly, the kernel may try to resolve this address even on a <code>NOARP</code> interface or if the address is multicast or broadcast.</dd></dl>
<dt>ip neighbour show</dt>
<dd>list neighbour entries</dd>
<dl>
<dd>
</dd><dl>
<dt><code>to</code><i> ADDRESS </i><code>(default)</code></dt>
<dd>the prefix selecting the neighbours to list.</dd>
<dt><code>dev</code><i> NAME</i></dt>
<dd>only list the neighbours attached to this device.</dd>
<dt><code>vrf</code><i> NAME</i></dt>
<dd>only list the neighbours for given VRF.</dd>
<dt><code>proxy</code></dt>
<dd>list neighbour proxies.</dd>
<dt><code>unused</code></dt>
<dd>only list neighbours which are not currently in use.</dd>
<dt><code>nud</code><i> STATE</i></dt>
<dd>only list neighbour entries in this state. <i>NUD_STATE</i> takes values listed below or the special value <code>all</code> which means all states. This option may occur more than once. If this option is absent, <code>ip</code> lists all entries except for <code>none</code> and <code>noarp</code>.</dd></dl>
</dl>
<dt>ip neighbour flush</dt>
<dd>flush neighbour entries</dd>
<dl>
<dd>This command has the same arguments as <code>show.</code> The differences are that it does not run when no arguments are given, and that the default neighbour states to be flushed do not include <code>permanent</code> and <code>noarp</code>. With the <code>-statistics</code> option, the command becomes verbose. It prints out the number of deleted neighbours and the number of rounds made to flush the neighbour table. If the option is given twice, <code>ip neigh flush</code> also dumps all the deleted neighbours.</dd></dl>
<dt>ip neigh get</dt>
<dd>lookup a neighbour entry to a destination given a device</dd>
<dl>
<dd>
</dd><dl>
<dt><code>proxy</code></dt>
<dd>indicates whether we should lookup a proxy neighbour entry</dd>
<dt><code>to</code><i> ADDRESS </i><code>(default)</code></dt>
<dd>the prefix selecting the neighbour to query.</dd>
<dt><code>dev</code><i> NAME</i></dt>
<dd>get neighbour entry attached to this device.</dd></dl>
</dl>
<h2>Examples</h2>
<p>ip neighbour</p>
<dl>
<dd>Shows the current neighbour table in kernel.</dd></dl>
<p> ip neigh flush dev eth0</p>
<dl>
<dd>Removes entries in the neighbour table on device eth0.</dd></dl>
<p> ip neigh get 10.0.1.10 dev eth0</p>
<dl>
<dd>Performs a neighbour lookup in the kernel and returns a neighbour entry.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by Michail Litvak &lt;mci [at] owl.openwall.com&gt;</p>
</dl>