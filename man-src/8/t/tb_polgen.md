---
title: "tb_polgen(8)"
name: "tb_polgen"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tb_polgen/"
description: "tb_polgen – manage tboot verified launch policy"
---

<p>tb_polgen &#8211; manage tboot verified launch policy</p>
<h2>Synopsis</h2>
<p><code>tb_polgen</code> <i>COMMAND</i> [<i>OPTION</i>]</p>
<h2>Description</h2>
<p><code>tb_polgen</code> is used to manage tboot verified launch policy.</p>
<h2>Commands</h2>
<dl>
<dt><code>&#8211;create</code></dt>
<dd>Create an empty tboot verified launch policy file.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>&#8211;type </code><i>nonfatal </i>|<i> continue </i>|<i> halt</i></dt>
<dd>Nonfatal means ignoring all non-fatal errors and continuing. Continue means ignoring verification errors and halting otherwise. Halt means halting on any errors.</dd>
<dt>[<code>&#8211;ctrl </code><i>policy-control-value</i>]</dt>
<dd>The default value 1 is to extend policy into PCR 17.</dd>
<dt><i>policy-file</i></dt>
<dd></dd></dl>
</dl>
<dt><code>&#8211;add</code></dt>
<dd>Add a module hash entry into a policy file.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>&#8211;num </code><i>module-number </i>|<i> any</i></dt>
<dd>The module-number is the 0-based module number corresponding to modules loaded by the bootloader.</dd>
<dt><code>&#8211;pcr </code><i>TPM-PCR-number </i>|<i> none</i></dt>
<dd>The TPM-PCR-number is the PCR to extend the module&#8217;s measurement into.</dd>
<dt><code>&#8211;hash </code><i>any </i>|<i> image</i></dt>
<dd>
</dd><dt>[<code>&#8211;cmdline </code><i>command-line</i>]</dt>
<dd>The command line is from grub.conf, and it should not include the module name (e.g. &quot;/xen.gz&quot;).</dd>
<dt>[<code>&#8211;image </code><i>image-file-name</i>]</dt>
<dd>
</dd><dt><i>policy-file</i></dt>
<dd></dd></dl>
</dl>
<dt><code>&#8211;del</code></dt>
<dd>Delete a module hash entry from a policy file.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>&#8211;num </code><i>module-number </i>|<i> any</i></dt>
<dd>The module-number is the 0-based module number corresponding to modules loaded by the bootloader.</dd>
<dt>[<code>&#8211;pos </code><i>hash-number</i>]</dt>
<dd>The hash-number is the 0-based index of the hash, within the list of hashes for the specified module.</dd>
<dt><i>policy-file</i></dt>
<dd></dd></dl>
</dl>
<dt><code>&#8211;unwrap</code></dt>
<dd>Extract the tboot verified launch policy from a TXT LCP element file.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>&#8211;elt </code><i>elt-file</i></dt>
<dd>
</dd><dt><i>policy-file</i></dt>
<dd></dd></dl>
</dl>
<dt><code>&#8211;show </code><i>policy-file</i></dt>
<dd>Show the policy information in a policy file.</dd>
<dt><code>&#8211;help</code></dt>
<dd>Print out the help message.</dd>
<dt><code>&#8211;verbose</code></dt>
<dd>Enable verbose output; can be specified with any command.</dd></dl>
<h2>Examples</h2>
<p><code>tb_polgen &#8211;create &#8211;type </code><i>nonfatal vl.pol</i> </p>
<p> <code>tb_polgen &#8211;add &#8211;num </code><i>0 </i><code>&#8211;pcr </code><i>none </i><code>&#8211;hash </code><i>image </i><code>&#8211;cmdline </code><i>&quot;cmdline&quot; </i><code>&#8211;image </code><i>/boot/xen.gz vl.pol</i> </p>
<p> <code>tb_polgen &#8211;add &#8211;num </code><i>1 </i><code>&#8211;pcr </code><i>19 </i><code>&#8211;hash </code><i>image </i><code>&#8211;cmdline </code><i>&quot;cmdline&quot; </i><code>&#8211;image </code><i>/boot/vmlinuz-2.6.18.8-xen vl.pol</i> </p>
<p> <code>tb_polgen &#8211;add &#8211;num </code><i>2 </i><code>&#8211;pcr </code><i>19 </i><code>&#8211;hash </code><i>image </i><code>&#8211;cmdline </code><i>&quot;&quot; </i><code>&#8211;image </code><i>/boot/initrd-2.6.18.8-xen.img vl.pol</i> </p>
<p> <code>tb_polgen &#8211;del &#8211;num </code><i>1 vl.pol</i> </p>
<p> <code>tb_polgen &#8211;show &#8211;verbose </code><i>vl.pol</i></p>
<h3>Note1:</h3>
<p>It is not necessary to specify a PCR for module 0, since this module&#8217;s measurement will always be extended to PCR 18. If a PCR is specified, then the measurement will be extended to that PCR in addition to PCR 18.</p>
<h3>Note2:</h3>
<p>&#8211;unwrap is not implemented correctly. There should be a defined UUID for this and that should be checked before copying the data. There should be a wrap or similar command to generates an element file for a policy.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lcp_crtpol/">lcp_crtpol</a></code>(8), <code><a href="/docs/linux/man/8-lcp_crtpol2/">lcp_crtpol2</a></code>(8), <code><a href="/docs/linux/man/8-lcp_crtpolelt/">lcp_crtpolelt</a></code>(8). </p>
