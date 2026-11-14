---
title: "virt-win-reg(1)"
name: "virt-win-reg"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-win-reg/"
description: "virt-win-reg – Export and merge Windows Registry entries from a Windows guest"
---

<h2 class="name">NAME</h2>
<p> virt-win-reg &#8211; Export and merge Windows Registry entries from a Windows guest </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - win - reg domname 'HKLM\Path\To\Subkey' virt - win - reg domname 'HKLM\Path\To\Subkey' name virt - win - reg domname 'HKLM\Path\To\Subkey' @virt - win - reg-- merge domname[input.reg...] virt - win - reg[--options] disk.img... #instead of domname
</code></pre>
<h2>WARNING</h2>
<p> You must <i>not</i> use <tt>&quot;virt-win-reg&quot;</tt> with the <i>&#8211;merge</i> option on live virtual machines. If you do this, you <i>will</i> get irreversible disk corruption in the <font SIZE="-1">VM. </font><tt>&quot;virt-win-reg&quot;</tt> tries to stop you from doing this, but doesn&#8217;t catch all cases. </p>
<p> Modifying the Windows Registry is an inherently risky operation. The format is deliberately obscure and undocumented, and Registry changes can leave the system unbootable. Therefore when using the <i>&#8211;merge</i> option, make sure you have a reliable backup first.</p>
<h2>DESCRIPTION</h2>
<p> This program can export and merge Windows Registry entries from a Windows guest. </p>
<p> The first parameter is the libvirt guest name or the raw disk image of a Windows guest. </p>
<p> If <i>&#8211;merge</i> is <i>not</i> specified, then the chosen registry key is displayed/exported (recursively). For example: </p>
<pre>
 $ virt-win-reg Windows7 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft'
</pre>
<p> You can also display single values from within registry keys, for example: </p>
<pre>
 $ cvkey='HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
 $ virt-win-reg Windows7 $cvkey ProductName
 Windows 7 Enterprise
</pre>
<p> With <i>&#8211;merge</i>, you can merge a textual regedit file into the Windows Registry: </p>
<pre>
 $ virt-win-reg --merge Windows7 changes.reg
</pre>
<h3><font SIZE="-1">NOTE</font></h3>
<p> This program is only meant for simple access to the registry. If you want to do complicated things with the registry, we suggest you download the Registry hive files from the guest using <i><a href="/docs/linux/man/3-libguestfs/">libguestfs</a></i>(3) or <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) and access them locally, eg. using <i><a href="/docs/linux/man/3-hivex/">hivex</a></i>(3), <i><a href="/docs/linux/man/1-hivexsh/">hivexsh</a></i>(1) or <i><a href="/docs/linux/man/1-hivexregedit/">hivexregedit</a></i>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display brief help.</p>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>&#8211;debug</code></p>
<dd> Enable debugging messages.</p>
<dt><code>-c </code><font SIZE="-1"><code>URI</code></font></p>
<dd>
<dt><code>&#8211;connect </code><font SIZE="-1"><code>URI</code></font></p>
<dd> If using libvirt, connect to the given <i></i><font SIZE="-1"><i>URI</i></font><i></i>. If omitted, then we connect to the default libvirt hypervisor. </p>
<p> If you specify guest block devices directly, then libvirt is not used at all.</p>
<dt><code>&#8211;format</code> raw</p>
<dd> Specify the format of disk images given on the command line. If this is omitted then the format is autodetected from the content of the disk image. </p>
<p> If disk images are requested from libvirt, then this program asks libvirt for this information. In this case, the value of the format parameter is ignored. </p>
<p> If working with untrusted raw-format guest disk images, you should ensure the format is always specified.</p>
<dt><code>&#8211;merge</code></p>
<dd> In merge mode, this merges a textual regedit file into the Windows Registry of the virtual machine. If this flag is <i>not</i> given then virt-win-reg displays or exports Registry entries instead. </p>
<p> Note that <i>&#8211;merge</i> is <i>unsafe</i> to use on live virtual machines, and will result in disk corruption. However exporting (without this flag) is always safe.</p>
<dt><code>&#8211;encoding</code> UTF-16LE|ASCII</p>
<dd> When merging (only), you may need to specify the encoding for strings to be used in the hive file. This is explained in detail in &#8220;<font SIZE="-1">ENCODING STRINGS&#8221;</font> in <i><a href="/docs/linux/man/3-win--hivex--regedit/">Win::Hivex::Regedit</a></i>(3). </p>
<p> The default is to use <font SIZE="-1">UTF-16LE,</font> which should work with recent versions of Windows.</p>
<dt><code>&#8211;unsafe-printable-strings</code></p>
<dd> When exporting (only), assume strings are <font SIZE="-1">UTF-16LE</font> and print them as strings instead of hex sequences. Remove the final zero codepoint from strings if present. </p>
<p> This is unsafe and does not preserve the fidelity of strings in the original Registry for various reasons:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Assumes the original encoding is <font SIZE="-1">UTF-16LE. ASCII</font> strings and strings in other encodings will be corrupted by this transformation.</p>
<dt>&bull;</p>
<dd> Assumes that everything which has type 1 or 2 is really a string and that everything else is not a string, but the type field in real Registries is not reliable.</p>
<dt>&bull;</p>
<dd> Loses information about whether a zero codepoint followed the string in the Registry or not.</dl>
</dl>
<dl>
<dt>
<dd>
<p> This all happens because the Registry itself contains no information about how strings are encoded (see &#8220;<font SIZE="-1">ENCODING STRINGS&#8221;</font> in <i><a href="/docs/linux/man/3-win--hivex--regedit/">Win::Hivex::Regedit</a></i>(3)). </p>
<p> You should only use this option for quick hacking and debugging of the Registry contents, and <i>never</i> use it if the output is going to be passed into another program or stored in another Registry.</dl>
</dl>
<h2>SUPPORTED SYSTEMS</h2>
<p> The program currently supports Windows NT-derived guests starting with Windows <font SIZE="-1">XP</font> through to at least Windows 8. </p>
<p> The following Registry keys are supported:</p>
<dl>
<dt>&quot;HKEY_LOCAL_MACHINE\SAM&quot;</p>
<dd>
<dt>&quot;HKEY_LOCAL_MACHINE\SECURITY&quot;</p>
<dd>
<dt>&quot;HKEY_LOCAL_MACHINE\SOFTWARE&quot;</p>
<dd>
<dt>&quot;HKEY_LOCAL_MACHINE\SYSTEM&quot;</p>
<dd>
<dt>&quot;HKEY_USERS\.DEFAULT&quot;</p>
<dd>
<dt>&quot;HKEY_USERS\SID<tt>&quot;</p>
<dd> where </tt><i></i><font SIZE="-1"><i>SID</i></font><i></i> is a Windows User <font SIZE="-1">SID </font>(eg. <tt>&quot;S-1-5-18&quot;</tt>).</p>
<dt>&quot;HKEY_USERS
