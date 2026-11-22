---

title: "virt-win-reg(1)"
name: "virt-win-reg"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-win-reg/"
description: "virt-win-reg – Export and merge Windows Registry entries from a Windows guest"
---

<p> virt-win-reg - Export and merge Windows Registry entries from a Windows guest </p>
<h2>SYNOPSIS</h2>
<pre><code> virt-win-reg domname 'HKLM\Path\To\Subkey'
 virt-win-reg domname 'HKLM\Path\To\Subkey' name
 virt-win-reg domname 'HKLM\Path\To\Subkey' @
 virt-win-reg --merge domname [input.reg ...]
 virt-win-reg [--options] disk.img ... # instead of domname
</code></pre>
<h2>WARNING</h2>
<p> You must <i>not</i> use <code>&quot;virt-win-reg&quot;</code> with the <i>--merge</i> option on live virtual machines. If you do this, you <i>will</i> get irreversible disk corruption in the VM. <code>&quot;virt-win-reg&quot;</code> tries to stop you from doing this, but doesn&#8217;t catch all cases. </p>
<p> Modifying the Windows Registry is an inherently risky operation. The format is deliberately obscure and undocumented, and Registry changes can leave the system unbootable. Therefore when using the <i>--merge</i> option, make sure you have a reliable backup first.  </p>
<h2>DESCRIPTION</h2>
<p> This program can export and merge Windows Registry entries from a Windows guest. </p>
<p> The first parameter is the libvirt guest name or the raw disk image of a Windows guest. </p>
<p> If <i>--merge</i> is <i>not</i> specified, then the chosen registry key is displayed/exported (recursively). For example: </p>
<pre><code> $ virt-win-reg Windows7 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft'
</code></pre>
<p> You can also display single values from within registry keys, for example: </p>
<pre><code> $ cvkey='HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
 $ virt-win-reg Windows7 $cvkey ProductName
 Windows 7 Enterprise
</code></pre>
<p> With <i>--merge</i>, you can merge a textual regedit file into the Windows Registry: </p>
<pre><code> $ virt-win-reg --merge Windows7 changes.reg
</code></pre>
<h3>NOTE</h3>
<p> This program is only meant for simple access to the registry. If you want to do complicated things with the registry, we suggest you download the Registry hive files from the guest using <i>libguestfs</i>(3) or <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) and access them locally, eg. using <i><a href="/docs/linux/man/3-hivex/">hivex</a></i>(3), <i><a href="/docs/linux/man/1-hivexsh/">hivexsh</a></i>(1) or <i><a href="/docs/linux/man/1-hivexregedit/">hivexregedit</a></i>(1).  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>--help</code></dt>
<dd> <p> Display brief help. </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> Display version number and exit. </p>
 </dd>
<dt><code>--debug</code></dt>
<dd> <p> Enable debugging messages. </p>
 </dd>
<dt><code>-c </code><code>URI</code></dt>
<dd>  </dd>
<dt><code>--connect </code><code>URI</code></dt>
<dd> <p> If using libvirt, connect to the given <i></i><i>URI</i><i></i>. If omitted, then we connect to the default libvirt hypervisor. </p>
<p> If you specify guest block devices directly, then libvirt is not used at all. </p>
 </dd>
<dt><code>--format</code> raw</dt>
<dd> <p> Specify the format of disk images given on the command line. If this is omitted then the format is autodetected from the content of the disk image. </p>
<p> If disk images are requested from libvirt, then this program asks libvirt for this information. In this case, the value of the format parameter is ignored. </p>
<p> If working with untrusted raw-format guest disk images, you should ensure the format is always specified. </p>
 </dd>
<dt><code>--merge</code></dt>
<dd> <p> In merge mode, this merges a textual regedit file into the Windows Registry of the virtual machine. If this flag is <i>not</i> given then virt-win-reg displays or exports Registry entries instead. </p>
<p> Note that <i>--merge</i> is <i>unsafe</i> to use on live virtual machines, and will result in disk corruption. However exporting (without this flag) is always safe. </p>
 </dd>
<dt><code>--encoding</code> UTF-16LE|ASCII</dt>
<dd> <p> When merging (only), you may need to specify the encoding for strings to be used in the hive file. This is explained in detail in ``ENCODING STRINGS&#8217;&#8216; in <i>Win::Hivex::Regedit</i>(3). </p>
<p> The default is to use UTF-16LE, which should work with recent versions of Windows. </p>
 </dd>
<dt><code>--unsafe-printable-strings</code></dt>
<dd> <p> When exporting (only), assume strings are UTF-16LE and print them as strings instead of hex sequences. Remove the final zero codepoint from strings if present. </p>
<p> This is unsafe and does not preserve the fidelity of strings in the original Registry for various reasons: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Assumes the original encoding is UTF-16LE. ASCII strings and strings in other encodings will be corrupted by this transformation. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assumes that everything which has type 1 or 2 is really a string and that everything else is not a string, but the type field in real Registries is not reliable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Loses information about whether a zero codepoint followed the string in the Registry or not. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> This all happens because the Registry itself contains no information about how strings are encoded (see ``ENCODING STRINGS&#8217;&#8216; in <i>Win::Hivex::Regedit</i>(3)). </p>
<p> You should only use this option for quick hacking and debugging of the Registry contents, and <i>never</i> use it if the output is going to be passed into another program or stored in another Registry. </p>
 </dd></dl>
</dl>
<h2>SUPPORTED SYSTEMS</h2>
<p> The program currently supports Windows NT-derived guests starting with Windows XP through to at least Windows 8. </p>
<p> The following Registry keys are supported: </p>
<dl>
<dt>&quot;HKEY_LOCAL_MACHINE\SAM&quot;</dt>
<dd>  </dd>
<dt>&quot;HKEY_LOCAL_MACHINE\SECURITY&quot;</dt>
<dd>  </dd>
<dt>&quot;HKEY_LOCAL_MACHINE\SOFTWARE&quot;</dt>
<dd>  </dd>
<dt>&quot;HKEY_LOCAL_MACHINE\SYSTEM&quot;</dt>
<dd>  </dd>
<dt>&quot;HKEY_USERS\.DEFAULT&quot;</dt>
<dd>  </dd>
<dt>&quot;HKEY_USERS\SID <code>&quot;</dt>
<dd> <p> where </code><i></i><i>SID</i><i></i> is a Windows User SID (eg. <code>&quot;S-1-5-18&quot;</code>). </p>
 </dd>
<dt>&quot;HKEY_USERS\username <code>&quot;</dt>
<dd> <p> where </code><i>username</i> is a local user name (this is a libguestfs extension). </p>
 </dd></dl>
<p> You can use <code>&quot;HKLM&quot;</code> as a shorthand for <code>&quot;HKEY_LOCAL_MACHINE&quot;</code>, and <code>&quot;HKU&quot;</code> for <code>&quot;HKEY_USERS&quot;</code>. </p>
<p> The literal keys <code>&quot;HKEY_USERS\$SID&quot;</code> and <code>&quot;HKEY_CURRENT_USER&quot;</code> are not supported (there is no ``current user&#8217;&#8216;).  </p>
<h3>WINDOWS 8</h3>
<p> Windows 8 ``fast startup&#8217;&#8216; can prevent virt-win-reg from being able to edit the Registry. See ``WINDOWS HIBERNATION AND WINDOWS 8 FAST STARTUP&#8217;&#8216; in <i>guestfs</i>(3).  </p>
<h2>ENCODING</h2>
<p> <code>&quot;virt-win-reg&quot;</code> expects that regedit files have already been reencoded in the local encoding. Usually on Linux hosts, this means UTF-8 with Unix-style line endings. Since Windows regedit files are often in UTF-16LE with Windows-style line endings, you may need to reencode the whole file before or after processing. </p>
<p> To reencode a file from Windows format to Linux (before processing it with the <i>--merge</i> option), you would do something like this: </p>
<pre><code> iconv -f utf-16le -t utf-8 &lt; win.reg | dos2unix &gt; linux.reg
</code></pre>
<p> To go in the opposite direction, after exporting and before sending the file to a Windows user, do something like this: </p>
<pre><code> unix2dos linux.reg | iconv -f utf-8 -t utf-16le &gt; win.reg
</code></pre>
<p> For more information about encoding, see <i>Win::Hivex::Regedit</i>(3). </p>
<p> If you are unsure about the current encoding, use the <i><a href="/docs/linux/man/1-file/">file</a></i>(1) command. Recent versions of Windows regedit.exe produce a UTF-16LE file with Windows-style (CRLF) line endings, like this: </p>
<pre><code> $ file software.reg
 software.reg: Little-endian UTF-16 Unicode text, with very long lines,
 with CRLF line terminators
</code></pre>
<p> This file would need conversion before you could <i>--merge</i> it.  </p>
<h2>CurrentControlSet etc.</h2>
<p> Registry keys like <code>&quot;CurrentControlSet&quot;</code> don&#8217;t really exist in the Windows Registry at the level of the hive file, and therefore you cannot modify these. </p>
<p> <code>&quot;CurrentControlSet&quot;</code> is usually an alias for <code>&quot;ControlSet001&quot;</code>. In some circumstances it might refer to another control set. The way to find out is to look at the <code>&quot;HKLM\SYSTEM\Select&quot;</code> key: </p>
<pre><code> # virt-win-reg WindowsGuest 'HKLM\SYSTEM\Select'
 [HKEY_LOCAL_MACHINE\SYSTEM\Select]
 &quot;Current&quot;=dword:00000001
 &quot;Default&quot;=dword:00000001
 &quot;Failed&quot;=dword:00000000
 &quot;LastKnownGood&quot;=dword:00000002
</code></pre>
<p> ``Current&#8217;&#8216; is the one which Windows will choose when it boots. </p>
<p> Similarly, other <code>&quot;Current...&quot;</code> keys in the path may need to be replaced.  </p>
<h2>DELETING REGISTRY KEYS AND VALUES</h2>
<p> To delete a whole registry key, use the syntax: </p>
<pre><code> [-HKEY_LOCAL_MACHINE\Foo]
</code></pre>
<p> To delete a single value within a key, use the syntax: </p>
<pre><code> [HKEY_LOCAL_MACHINE\Foo]
 &quot;Value&quot;=-
</code></pre>
<h2>WINDOWS TIPS</h2>
<p> Note that some of these tips modify the guest disk image. The guest <i>must</i> be shut off, else you will get disk corruption.  </p>
<h3>RUNNING A BATCH SCRIPT WHEN A USER LOGS IN</h3>
<p> Prepare a DOS batch script, VBScript or executable. Upload this using <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1). For this example the script is called <code>&quot;test.bat&quot;</code> and it is uploaded into <code>&quot;C:\&quot;</code>: </p>
<pre><code> guestfish -i -d WindowsGuest upload test.bat /test.bat
</code></pre>
<p> Prepare a regedit file containing the registry change: </p>
<pre><code> cat &gt; test.reg &lt;&lt;'EOF'
 [HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce]
 &quot;Test&quot;=&quot;c:\\test.bat&quot;
 EOF
</code></pre>
<p> In this example we use the key <code>&quot;RunOnce&quot;</code> which means that the script will run precisely once when the first user logs in. If you want it to run every time a user logs in, replace <code>&quot;RunOnce&quot;</code> with <code>&quot;Run&quot;</code>. </p>
<p> Now update the registry: </p>
<pre><code> virt-win-reg --merge WindowsGuest test.reg
</code></pre>
<h3>INSTALLING A SERVICE</h3>
<p> This section assumes you are familiar with Windows services, and you either have a program which handles the Windows Service Control Protocol directly or you want to run any program using a service wrapper like SrvAny or the free RHSrvAny. </p>
<p> First upload the program and optionally the service wrapper. In this case the test program is called <code>&quot;test.exe&quot;</code> and we are using the RHSrvAny wrapper: </p>
<pre><code> guestfish -i -d WindowsGuest &lt;&lt;EOF
   upload rhsrvany.exe /rhsrvany.exe
   upload test.exe /test.exe
 EOF
</code></pre>
<p> Prepare a regedit file containing the registry changes. In this example, the first registry change is needed for the service itself or the service wrapper (if used). The second registry change is only needed because I am using the RHSrvAny service wrapper. </p>
<pre><code> cat &gt; service.reg &lt;&lt;'EOF'
 [HKLM\SYSTEM\ControlSet001\services\RHSrvAny]
 &quot;Type&quot;=dword:00000010
 &quot;Start&quot;=dword:00000002
 &quot;ErrorControl&quot;=dword:00000001
 &quot;ImagePath&quot;=&quot;c:\\rhsrvany.exe&quot;
 &quot;DisplayName&quot;=&quot;RHSrvAny&quot;
 &quot;ObjectName&quot;=&quot;NetworkService&quot;
 [HKLM\SYSTEM\ControlSet001\services\RHSrvAny\Parameters]
 &quot;CommandLine&quot;=&quot;c:\\test.exe&quot;
 &quot;PWD&quot;=&quot;c:\\Temp&quot;
 EOF
</code></pre>
<p> Notes: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> For use of <code>&quot;ControlSet001&quot;</code> see the section above in this manual page. You may need to adjust this according to the control set that is in use by the guest. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;ObjectName&quot;</code> controls the privileges that the service will have. An alternative is <code>&quot;ObjectName&quot;=&quot;LocalSystem&quot;</code> which would be the most privileged account. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> For the meaning of the magic numbers, see this Microsoft KB article: <a rel="nofollow" href="http://support.microsoft.com/kb/103000.">http://support.microsoft.com/kb/103000.</a> </p>
 </dd></dl>
<p> Update the registry: </p>
<pre><code> virt-win-reg --merge WindowsGuest service.reg
</code></pre>
<h2>SHELL QUOTING</h2>
<p> Be careful when passing parameters containing <code>&quot;\&quot;</code> (backslash) in the shell. Usually you will have to use &#8216;single quotes&#8217; or double backslashes (but not both) to protect them from the shell. </p>
<p> Paths and value names are case-insensitive.  </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-hivex/">hivex</a></i>(3), <i><a href="/docs/linux/man/1-hivexsh/">hivexsh</a></i>(1), <i><a href="/docs/linux/man/1-hivexregedit/">hivexregedit</a></i>(1), <i>guestfs</i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i>Sys::Guestfs</i>(3), <i>Win::Hivex</i>(3), <i>Win::Hivex::Regedit</i>(3), <i>Sys::Virt</i>(3), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a>  </p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a>  </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010 Red Hat Inc.  </p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.  </p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The version of libguestfs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Where you got libguestfs (eg. which Linux distro, compiled from source, etc) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Describe the bug accurately and give a way to reproduce it. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
 </dd></dl>
