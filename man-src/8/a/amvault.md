---
title: "amvault(8)"
name: "amvault"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amvault/"
description: "amvault – Copy Amanda dumps from one volume to another"
---

<p>amvault &#8211; Copy Amanda dumps from one volume to another</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amvault</code> [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] [&#8211;dry-run | -n] [&#8211;quiet | -q] [&#8211;fulls-only] [&#8211;exact-match] [&#8211;export] [<code>&#8211;src-timestamp</code>&nbsp;<wbr><i>src-timestamp</i>]</p>
<dd><code>&#8211;label-template</code>&nbsp;<wbr><i>label-template</i> <code>&#8211;dst-changer</code>&nbsp;<wbr><i>dst-changer</i> [<code>&#8211;autolabel</code>&nbsp;<wbr><i>autolabel-arg</i>&#8230;]</p>
<dd><i>config</i> [<i>hostname</i>&nbsp;<wbr>[&nbsp;<wbr><i>disk</i>&nbsp;<wbr>[&nbsp;<wbr><i>date</i>&nbsp;<wbr>[&nbsp;<wbr><i>level</i>&nbsp;<wbr>[&nbsp;<wbr><i>hostname</i>&nbsp;<wbr>[&#8230;]&nbsp;<wbr>]&nbsp;<wbr>]&nbsp;<wbr>]&nbsp;<wbr>]]</dl>
<h2>Warning</h2>
<dd>This application is not yet in its final form, and is subject to major revision in subsequent versions of Amanda. Backward compatibility is not guaranteed. </p>
<p> Note that Amanda restore/recover operations will request tertiary media by label when dumpfiles are not found on secondary media, but there is no provision to automatically fetch such media from a different changer </p>
<p> Feedback on and patches to this application are invited and encouraged!</p>
<h2>Description</h2>
<p>Amvault is conceptually equivalent to &quot;amfetchdump | taper&quot;. That is, it reads specified dumps from secondary media and re-writes them on tertiary media. </p>
<p> <code>Amvault</code> Copies data from the run with timestamp <code>src-timestamp</code> onto volumes using the changer <code>dst-changer</code>, and labeling new volumes with <code>label-template</code>.</p>
<h3>Secondary Media</h3>
<p>The dumps to be read from secondary media can be specified by any combination of dump specifications, <code>&#8211;fulls-only</code>, and <code>&#8211;src-timestamp</code>. At least one must be specified, lest amvault attempt to vault all dumps in the catalog. See <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7) for more information on dump specifications. </p>
<p> Note that the datestamp given in the dumpspec is the <i>dump</i> datestamp &#8211; the run in which the backup was taken on the Amanda client. The <code>&#8211;src-timestamp</code>, on the other hand, is the <i>write</i> timestamp &#8211; the run in which the dump was written to secondary media. The latter option facilitates duplicating the results of an entire backup run, including any dumps that might have been flushed from holding disk.</p>
<h3>Tertiary Media</h3>
<p>The <code>&#8211;dst-changer</code> must be specified, and names the changer in which tertiary media are stored. </p>
<p> If <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) contains the new <code>part-size</code> splitting parameters, then amvault will use them without any additional configuration. However, if the configuration still uses the old splitting parameters (<code>tape_splitsize</code>, <code>split_diskbuffer</code>, and <code>fallback_splitsize</code>), then amvault will need some additional configuration in order to properly split dumps to tertiary media. To do so, specify a new tapetype in <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), say &quot;TERTIARY&quot;, and set the <code>part-size</code> and other appropriate parameters there. Then reference that tapetype in the amvault invocation: </p>
<pre> amvault -otapetype=TERTIARY ...</pre>
<h2>Options</h2>
<p><code>&#8211;autolabel</code> [any] [other-config] [non-amanda] [volume-error] [empty]</p>
<dl>
<dd>Works just like the <code>autolabel</code> parameter in <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), and can be specified multiple times if necessary. The default is &#8217;empty&#8217;.</dl>
<p> <code>&#8211;dst-changer</code> <i>dst-changer</i></p>
<dl>
<dd>Specifies the changer in which tertiary media are stored. In general, this should be different from the secondary changer, to eliminate the possibility of overwriting secondary media with tertiary data. </p>
<p> The <code>dst-changer</code> parameter should specify the name of a changer defined in <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5). For example: </p>
<pre>define changer vaulting_tape {
 tapedev &quot;/dev/rmt/1n&quot;
 tpchanger &quot;chg-zd-mtx&quot;
 changerdev &quot;/dev/sg0&quot;
 changerfile &quot;vaulting-changer.conf&quot;
}</pre>
</dl>
<p> <code>&#8211;dry-run</code>, <code>-n</code></p>
<dl>
<dd>Cause amvault to print the dumps it would vault, but not actually perform any vaulting operations.</dl>
<p> <code>&#8211;exact-match</code></p>
<dl>
<dd>The host and disk are parsed as exact values</dl>
<p> <code>&#8211;export</code></p>
<dl>
<dd>Cause amvault to attempt to move completed tertiary volumes to import/export slots, where they can be more easily removed by an operator.</dl>
<p> <code>&#8212;fulls-only</code></p>
<dl>
<dd>Only full (level-0) dumps are copied.</dl>
<p> <code>&#8211;label-template</code> <i>label-template</i></p>
<dl>
<dd>Specifies a label template which is used to generate new labels for tertiary volumes.</dl>
<p> <code>&#8211;quiet</code>, <code>-q</code></p>
<dl>
<dd>Eliminate non-error messages, and is useful when running amvault from cron.</dl>
<p> <code>&#8211;src-timestamps</code> <i>src-timestamps</i></p>
<dl>
<dd>Specifies the timestamps in the format &#8216;YYYYMMDDHHMMSS&#8217; of the run to vault, can be &quot;latest&quot;, then the most recent amdump or amflush run will be used.</dl>
<p> <code>-o</code> <i>configoption</i></p>
<dl>
<dd>See the &quot;<code>CONFIGURATION OVERRIDE</code>&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8).</dl>
<h2>Examples</h2>
<p>Vault all dump written to tape in the latest amdump or amflush run: </p>
<pre>$ amvault --src-timestamps latest --label-template &quot;CONF-%%%&quot; --dst-changer vault-changer CONF</pre>
<p>Vault all dump written on the run of December 7 2011 12:13:14 : </p>
<pre>$ amvault --src-timestamps 20111207121314 --label-template &quot;CONF-%%%&quot; --dst-changer vault-changer CONF</pre>
<p>Vault all dump dumped on any run of December 7 2011: </p>
<pre>$ amvault --label-template &quot;CONF-%%%&quot; --dst-changer vault-changer CONF \* \* 20111207</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/7-amanda-changers/">amanda-changers</a></code>(7), <code><a href="/docs/linux/man/8-amfetchdump/">amfetchdump</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
