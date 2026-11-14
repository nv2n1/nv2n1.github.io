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
<p> <code>ip neigh</code> { <code>add</code> | <code>del</code> | <code>change</code> | <code>replace</code> } { <i>ADDR</i> [ <code>lladdr</code> <i>LLADDR</i> ] [ <code>nud</code> <i>STATE</i> ] | <code>proxy</code> <i>ADDR</i> } [ <code>dev</code> <i>DEV</i> ] [ <code>router</code> ] [ <code>extern_learn</code> ]<br />
 <code>ip neigh</code> { <code>show</code> | <code>flush</code> } [ <code>proxy</code> ] [ <code>to</code> <i>PREFIX</i> ] [ <code>dev</code> <i>DEV</i> ] [ <code>nud</code> <i>STATE</i> ] [ <code>vrf</code> <i>NAME</i> ]<br />
 <code>ip neigh get</code> <i>ADDR</i> <code>dev</code> <i>DEV</i> </p>
<pre><code>STATE := {

    permanent | noarp | stale | reachable | none |

    incomplete | delay | probe | failed }
</code></pre>
<h2>Description</h2>
<p>The <code>ip neigh</code> command manipulates <i>neighbour</i> objects that establish bindings between protocol addresses and link layer addresses for hosts sharing the same link. Neighbour entries are organized into tables. The IPv4 neighbour table is also known by another name &#8211; the ARP table. The corresponding commands display neighbour bindings and their properties, add new neighbour entries and delete old ones.</p>
<dl>
<dt>ip neighbour add</p>
<dd>add a new neighbour entry</p>
<dt>ip neighbour change</p>
<dd>change an existing entry</p>
<dt>ip neighbour replace</p>
<dd>add a new entry or change an existing one</p>
<dl>
<dd>These commands create new neighbour records or update existing ones.</p>
<dl>
<dt><code>to</code><i> ADDRESS </i><code>(default)</code></p>
<dd>the protocol address of the neighbour. It is either an IPv4 or IPv6 address.</p>
<dt><code>dev</code><i> NAME</i></p>
<dd>the interface to which this neighbour is attached.</p>
<dt><code>proxy</code></p>
<dd>indicates whether we are proxying for this neighbour entry</p>
<dt><code>router</code></p>
<dd>indicates whether neighbour is a router</p>
<dt><code>extern_learn</code></p>
<dd>this neigh entry was learned externally. This option can be used to indicate to the kernel that this is a controller learnt dynamic entry. Kernel will not gc such an entry.</p>
<dt><code>lladdr</code><i> LLADDRESS</i></p>
<dd>the link layer address of the neighbour. <i>LLADDRESS</i> can also be <code>null</code>.</p>
<dt><code>nud</code><i> STATE</i></p>
<dd>the state of the neighbour entry. <code>nud</code> is an abbreviation for &#8216;Neighbour Unreachability Detection&#8217;. The state can take one of the following values:</p>
<dl>
<dd>
<dl>
<dt><code>permanent</code></p>
<dd>the neighbour entry is valid forever and can be only be removed administratively.</p>
<dt><code>noarp</code></p>
<dd>the neighbour entry is valid. No attempts to validate this entry will be made but it can be removed when its lifetime expires.</p>
<dt><code>reachable</code></p>
<dd>the neighbour entry is valid until the reachability timeout expires.</p>
<dt><code>stale</code></p>
<dd>the neighbour entry is valid but suspicious. This option to <code>ip neigh</code> does not change the neighbour state if it was valid and the address is not changed by this command.</p>
<dt><code>none</code></p>
<dd>this is a pseudo state used when initially creating a neighbour entry or after trying to remove it before it becomes free to do so.</p>
<dt><code>incomplete</code></p>
<dd>the neighbour entry has not (yet) been validated/resolved.</p>
<dt><code>delay</code></p>
<dd>neighbor entry validation is currently delayed.</p>
<dt><code>probe</code></p>
<dd>neighbor is being probed.</p>
<dt><code>failed</code></p>
<dd>max number of probes exceeded without success, neighbor validation has ultimately failed.</dl>
</dl>
</dl>
</dl>
<dt>ip neighbour delete</p>
<dd>delete a neighbour entry</p>
<dl>
<dd>The arguments are the same as with <code>ip neigh add</code>, except that <code>lladdr</code> and <code>nud</code> are ignored. <code>Warning:</code> Attempts to delete or manually change a <code>noarp</code> entry created by the kernel may result in unpredictable behaviour. Particularly, the kernel may try to resolve this address even on a <code>NOARP</code> interface or if the address is multicast or broadcast.</dl>
<dt>ip neighbour show</p>
<dd>list neighbour entries</p>
<dl>
<dd>
<dl>
<dt><code>to</code><i> ADDRESS </i><code>(default)</code></p>
<dd>the prefix selecting the neighbours to list.</p>
<dt><code>dev</code><i> NAME</i></p>
<dd>only list the neighbours attached to this device.</p>
<dt><code>vrf</code><i> NAME</i></p>
<dd>only list the neighbours for given VRF.</p>
<dt><code>proxy</code></p>
<dd>list neighbour proxies.</p>
<dt><code>unused</code></p>
<dd>only list neighbours which are not currently in use.</p>
<dt><code>nud</code><i> STATE</i></p>
<dd>only list neighbour entries in this state. <i>NUD_STATE</i> takes values listed below or the special value <code>all</code> which means all states. This option may occur more than once. If this option is absent, <code>ip</code> lists all entries except for <code>none</code> and <code>noarp</code>.</dl>
</dl>
<dt>ip neighbour flush</p>
<dd>flush neighbour entries</p>
<dl>
<dd>This command has the same arguments as <code>show.</code> The differences are that it does not run when no arguments are given, and that the default neighbour states to be flushed do not include <code>permanent</code> and <code>noarp</code>. With the <code>-statistics</code> option, the command becomes verbose. It prints out the number of deleted neighbours and the number of rounds made to flush the neighbour table. If the option is given twice, <code>ip neigh flush</code> also dumps all the deleted neighbours.</dl>
<dt>ip neigh get</p>
<dd>lookup a neighbour entry to a destination given a device</p>
<dl>
<dd>
<dl>
<dt><code>proxy</code></p>
<dd>indicates whether we should lookup a proxy neighbour entry</p>
<dt><code>to</code><i> ADDRESS </i><code>(default)</code></p>
<dd>the prefix selecting the neighbour to query.</p>
<dt><code>dev</code><i> NAME</i></p>
<dd>get neighbour entry attached to this device.</dl>
</dl>
<h2>Examples</h2>
<p>ip neighbour</p>
<dl>
<dd>Shows the current neighbour table in kernel.</dl>
<p> ip neigh flush dev eth0</p>
<dl>
<dd>Removes entries in the neighbour table on device eth0.</dl>
<p> ip neigh get 10.0.1.10 dev eth0</p>
<dl>
<dd>Performs a neighbour lookup in the kernel and returns a neighbour entry.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by Michail Litvak &lt;mci [at] owl.openwall.com&gt;</p>
