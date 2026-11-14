---
title: "os-release(5)"
name: "os-release"
section: "5"
letter: "o"
url: "/docs/linux/man/5-os-release/"
description: "os-release, initrd-release – Operating system identification"
---

<p>os-release, initrd-release &#8211; Operating system identification</p>
<h2>Synopsis</h2>
<p>/etc/os-release </p>
<p> /usr/lib/os-release </p>
<p> /etc/initrd-release</p>
<h2>Description</h2>
<p>The /etc/os-release and /usr/lib/os-release files contain operating system identification data. </p>
<p> The basic file format of os-release is a newline-separated list of environment-like shell-compatible variable assignments. It is possible to source the configuration from shell scripts, however, beyond mere variable assignments, no shell features are supported (this means variable expansion is explicitly not supported), allowing applications to read the file without implementing a shell compatible execution engine. Variable assignment values must be enclosed in double or single quotes if they include spaces, semicolons or other special characters outside of A-Z, a-z, 0-9. Shell special characters (&quot;$&quot;, quotes, backslash, backtick) must be escaped with backslashes, following shell style. All strings should be in UTF-8 format, and non-printable characters should not be used. It is not supported to concatenate multiple individually quoted strings. Lines beginning with &quot;#&quot; shall be ignored as comments. Blank lines are permitted and ignored. </p>
<p> The file /etc/os-release takes precedence over /usr/lib/os-release. Applications should check for the former, and exclusively use its data if it exists, and only fall back to /usr/lib/os-release if it is missing. Applications should not read data from both files at the same time. /usr/lib/os-release is the recommended place to store OS release information as part of vendor trees. /etc/os-release should be a relative symlink to /usr/lib/os-release, to provide compatibility with applications only looking at /etc/. A relative symlink instead of an absolute symlink is necessary to avoid breaking the link in a chroot or initrd environment such as dracut. </p>
<p> os-release contains data that is defined by the operating system vendor and should generally not be changed by the administrator. </p>
<p> As this file only encodes names and identifiers it should not be localized. </p>
<p> The /etc/os-release and /usr/lib/os-release files might be symlinks to other files, but it is important that the file is available from earliest boot on, and hence must be located on the root file system. </p>
<p> For a longer rationale for os-release please refer to the m[blue]<code>Announcement of /etc/os-release</code>m[]<font SIZE="-2">[1]</font>.</p>
<h3>/etc/initrd-release</h3>
<p>In the m[blue]<code>initrd</code>m[]<font SIZE="-2">[2]</font>, /etc/initrd-release plays the same role as os-release in the main system. Additionally, the presence of that file means that the system is in the initrd phase. /etc/os-release should be symlinked to /etc/initrd-release (or vice versa), so programs that only look for /etc/os-release (as described above) work correctly. The rest of this document that talks about os-release should be understood to apply to initrd-release too.</p>
<h2>Options</h2>
<p>The following OS identifications parameters may be set using os-release:</p>
<h3>General information identifying the operating system</h3>
<p><i>NAME=</i></p>
<dl>
<dd>A string identifying the operating system, without a version component, and suitable for presentation to the user. If not set, a default of &quot;NAME=Linux&quot; may be used. </p>
<p> Examples: &quot;NAME=Fedora&quot;, &quot;NAME=&quot;Debian GNU/Linux&quot;&quot;.</dl>
<p> <i>ID=</i></p>
<dl>
<dd>A lower-case string (no spaces or other characters outside of 0-9, a-z, &quot;.&quot;, &quot;_&quot; and &quot;-&quot;) identifying the operating system, excluding any version information and suitable for processing by scripts or usage in generated filenames. If not set, a default of &quot;ID=linux&quot; may be used. </p>
<p> Examples: &quot;ID=fedora&quot;, &quot;ID=debian&quot;.</dl>
<p> <i>ID_LIKE=</i></p>
<dl>
<dd>A space-separated list of operating system identifiers in the same syntax as the <i>ID=</i> setting. It should list identifiers of operating systems that are closely related to the local operating system in regards to packaging and programming interfaces, for example listing one or more OS identifiers the local OS is a derivative from. An OS should generally only list other OS identifiers it itself is a derivative of, and not any OSes that are derived from it, though symmetric relationships are possible. Build scripts and similar should check this variable if they need to identify the local operating system and the value of <i>ID=</i> is not recognized. Operating systems should be listed in order of how closely the local operating system relates to the listed ones, starting with the closest. This field is optional. </p>
<p> Examples: for an operating system with &quot;ID=centos&quot;, an assignment of &quot;ID_LIKE=&quot;rhel fedora&quot;&quot; would be appropriate. For an operating system with &quot;ID=ubuntu&quot;, an assignment of &quot;ID_LIKE=debian&quot; is appropriate.</dl>
<p> <i>PRETTY_NAME=</i></p>
<dl>
<dd>A pretty operating system name in a format suitable for presentation to the user. May or may not contain a release code name or OS version of some kind, as suitable. If not set, a default of &quot;PRETTY_NAME=&quot;Linux&quot;&quot; may be used </p>
<p> Example: &quot;PRETTY_NAME=&quot;Fedora 17 (Beefy Miracle)&quot;&quot;.</dl>
<p> <i>CPE_NAME=</i></p>
<dl>
<dd>A CPE name for the operating system, in URI binding syntax, following the m[blue]<code>Common Platform Enumeration Specification</code>m[]<font SIZE="-2">[3]</font> as proposed by the NIST. This field is optional. </p>
<p> Example: &quot;CPE_NAME=&quot;cpe:/o:fedoraproject:fedora:17&quot;&quot;</dl>
<p> <i>VARIANT=</i></p>
<dl>
<dd>A string identifying a specific variant or edition of the operating system suitable for presentation to the user. This field may be used to inform the user that the configuration of this system is subject to a specific divergent set of rules or default configuration settings. This field is optional and may not be implemented on all systems. </p>
<p> Examples: &quot;VARIANT=&quot;Server Edition&quot;&quot;, &quot;VARIANT=&quot;Smart Refrigerator Edition&quot;&quot;. </p>
<p> Note: this field is for display purposes only. The <i>VARIANT_ID</i> field should be used for making programmatic decisions.</dl>
<p> <i>VARIANT_ID=</i></p>
<dl>
<dd>A lower-case string (no spaces or other characters outside of 0-9, a-z, &quot;.&quot;, &quot;_&quot; and &quot;-&quot;), identifying a specific variant or edition of the operating system. This may be interpreted by other packages in order to determine a divergent default configuration. This field is optional and may not be implemented on all systems. </p>
<p> Examples: &quot;VARIANT_ID=server&quot;, &quot;VARIANT_ID=embedded&quot;.</dl>
<h3>Information about the version of the operating system</h3>
<p><i>VERSION=</i></p>
<dl>
<dd>A string identifying the operating system version, excluding any OS name information, possibly including a release code name, and suitable for presentation to the user. This field is optional. </p>
<p> Examples: &quot;VERSION=17&quot;, &quot;VERSION=&quot;17 (Beefy Miracle)&quot;&quot;.</dl>
<p> <i>VERSION_ID=</i></p>
<dl>
<dd>A lower-case string (mostly numeric, no spaces or other characters outside of 0-9, a-z, &quot;.&quot;, &quot;_&quot; and &quot;-&quot;) identifying the operating system version, excluding any OS name information or release code name, and suitable for processing by scripts or usage in generated filenames. This field is optional. </p>
<p> Examples: &quot;VERSION_ID=17&quot;, &quot;VERSION_ID=11.04&quot;.</dl>
<p> <i>VERSION_CODENAME=</i></p>
<dl>
<dd>A lower-case string (no spaces or other characters outside of 0-9, a-z, &quot;.&quot;, &quot;_&quot; and &quot;-&quot;) identifying the operating system release code name, excluding any OS name information or release version, and suitable for processing by scripts or usage in generated filenames. This field is optional and may not be implemented on all systems. </p>
<p> Examples: &quot;VERSION_CODENAME=buster&quot;, &quot;VERSION_CODENAME=xenial&quot;.</dl>
<p> <i>BUILD_ID=</i></p>
<dl>
<dd>A string uniquely identifying the system image originally used as the installation base. In most cases, <i>VERSION_ID</i> or <i>IMAGE_ID</i>+<i>IMAGE_VERSION</i> are updated when the entire system image is replaced during an update. <i>BUILD_ID</i> may be used in distributions where the original installation image version is important: <i>VERSION_ID</i> would change during incremental system updates, but <i>BUILD_ID</i> would not. This field is optional. </p>
<p> Examples: &quot;BUILD_ID=&quot;2013-03-20.3&quot;&quot;, &quot;BUILD_ID=201303203&quot;.</dl>
<p> <i>IMAGE_ID=</i></p>
<dl>
<dd>A lower-case string (no spaces or other characters outside of 0-9, a-z, &quot;.&quot;, &quot;_&quot; and &quot;-&quot;), identifying a specific image of the operating system. This is supposed to be used for environments where OS images are prepared, built, shipped and updated as comprehensive, consistent OS images. This field is optional and may not be implemented on all systems, in particularly not on those that are not managed via images but put together and updated from individual packages and on the local system. </p>
<p> Examples: &quot;IMAGE_ID=vendorx-cashier-system&quot;, &quot;IMAGE_ID=netbook-image&quot;.</dl>
<p> <i>IMAGE_VERSION=</i></p>
<dl>
<dd>A lower-case string (mostly numeric, no spaces or other characters outside of 0-9, a-z, &quot;.&quot;, &quot;_&quot; and &quot;-&quot;) identifying the OS image version. This is supposed to be used together with <i>IMAGE_ID</i> described above, to discern different versions of the same image. </p>
<p> Examples: &quot;IMAGE_VERSION=33&quot;, &quot;IMAGE_VERSION=47.1rc1&quot;.</dl>
<p> To summarize: if the image updates are built and shipped as comprehensive units, <i>IMAGE_ID</i>+<i>IMAGE_VERSION</i> is the best fit. Otherwise, if updates eventually completely replace previously installed contents, as in a typical binary distribution, <i>VERSION_ID</i> should be used to identify major releases of the operating system. <i>BUILD_ID</i> may be used instead or in addition to <i>VERSION_ID</i> when the original system image version is important.</p>
<h3>Presentation information and links</h3>
<p><i>HOME_URL=</i>, <i>DOCUMENTATION_URL=</i>, <i>SUPPORT_URL=</i>, <i>BUG_REPORT_URL=</i>, <i>PRIVACY_POLICY_URL=</i></p>
<dl>
<dd>Links to resources on the Internet related to the operating system. <i>HOME_URL=</i> should refer to the homepage of the operating system, or alternatively some homepage of the specific version of the operating system. <i>DOCUMENTATION_URL=</i> should refer to the main documentation page for this operating system. <i>SUPPORT_URL=</i> should refer to the main support page for the operating system, if there is any. This is primarily intended for operating systems which vendors provide support for. <i>BUG_REPORT_URL=</i> should refer to the main bug reporting page for the operating system, if there is any. This is primarily intended for operating systems that rely on community QA. <i>PRIVACY_POLICY_URL=</i> should refer to the main privacy policy page for the operating system, if there is any. These settings are optional, and providing only some of these settings is common. These URLs are intended to be exposed in &quot;About this system&quot; UIs behind links with captions such as &quot;About this Operating System&quot;, &quot;Obtain Support&quot;, &quot;Report a Bug&quot;, or &quot;Privacy Policy&quot;. The values should be in m[blue]<code>RFC3986 format</code>m[]<font SIZE="-2">[4]</font>, and should be &quot;http:&quot; or &quot;https:&quot; URLs, and possibly &quot;mailto:&quot; or &quot;tel:&quot;. Only one URL shall be listed in each setting. If multiple resources need to be referenced, it is recommended to provide an online landing page linking all available resources. </p>
<p> Examples: &quot;HOME_URL=&quot;<a rel="nofollow" href="https://fedoraproject.org/">https://fedoraproject.org/</a>&quot;&quot;, &quot;BUG_REPORT_URL=&quot;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&quot;&quot;.</dl>
<p> <i>LOGO=</i></p>
<dl>
<dd>A string, specifying the name of an icon as defined by m[blue]<code>freedesktop.org Icon Theme Specification</code>m[]<font SIZE="-2">[5]</font>. This can be used by graphical applications to display an operating system&#8217;s or distributor&#8217;s logo. This field is optional and may not necessarily be implemented on all systems. </p>
<p> Examples: &quot;LOGO=fedora-logo&quot;, &quot;LOGO=distributor-logo-opensuse&quot;</dl>
<p> <i>ANSI_COLOR=</i></p>
<dl>
<dd>A suggested presentation color when showing the OS name on the console. This should be specified as string suitable for inclusion in the ESC [ m ANSI/ECMA-48 escape code for setting graphical rendition. This field is optional. </p>
<p> Examples: &quot;ANSI_COLOR=&quot;0;31&quot;&quot; for red, &quot;ANSI_COLOR=&quot;1;34&quot;&quot; for light blue, or &quot;ANSI_COLOR=&quot;0;38;2;60;110;180&quot;&quot; for Fedora blue.</dl>
<h3>Distribution-level defaults and metadata</h3>
<p><i>DEFAULT_HOSTNAME=</i></p>
<dl>
<dd>A string specifying the hostname if <code><a href="/docs/linux/man/5-hostname/">hostname</a></code>(5) is not present and no other configuration source specifies the hostname. Must be either a single DNS label (a string composed of 7-bit ASCII lower-case characters and no spaces or dots, limited to the format allowed for DNS domain name labels), or a sequence of such labels separated by single dots that forms a valid DNS FQDN. The hostname must be at most 64 characters, which is a Linux limitation (DNS allows longer names). </p>
<p> See <code><a href="/docs/linux/man/5-org-freedesktop-hostname1/">org.freedesktop.hostname1</a></code>(5) for a description of how <code><a href="/docs/linux/man/8-systemd-hostnamed-service/">systemd-hostnamed.service</a></code>(8) determines the fallback hostname.</dl>
<p> <i>SYSEXT_LEVEL=</i></p>
<dl>
<dd>A lower-case string (mostly numeric, no spaces or other characters outside of 0-9, a-z, &quot;.&quot;, &quot;_&quot; and &quot;-&quot;) identifying the operating system extensions support level, to indicate which extension images are supported. See <code><a href="/docs/linux/man/8-systemd-sysext/">systemd-sysext</a></code>(8)) for more information. </p>
<p> Examples: &quot;SYSEXT_LEVEL=2&quot;, &quot;SYSEXT_LEVEL=15.14&quot;.</dl>
<h3>Notes</h3>
<p>If you are using this file to determine the OS or a specific version of it, use the <i>ID</i> and <i>VERSION_ID</i> fields, possibly with <i>ID_LIKE</i> as fallback for <i>ID</i>. When looking for an OS identification string for presentation to the user use the <i>PRETTY_NAME</i> field. </p>
<p> Note that operating system vendors may choose not to provide version information, for example to accommodate for rolling releases. In this case, <i>VERSION</i> and <i>VERSION_ID</i> may be unset. Applications should not rely on these fields to be set. </p>
<p> Operating system vendors may extend the file format and introduce new fields. It is highly recommended to prefix new fields with an OS specific name in order to avoid name clashes. Applications reading this file must ignore unknown fields. </p>
<p> Example: &quot;DEBIAN_BTS=&quot;debbugs://bugs.debian.org/&quot;&quot;. </p>
<p> Container and sandbox runtime managers may make the host&#8217;s identification data available to applications by providing the host&#8217;s /etc/os-release (if available, otherwise /usr/lib/os-release as a fallback) as /run/host/os-release.</p>
<h2>Examples</h2>
<p><code>Example 1. os-release file for Fedora Workstation</code> </p>
<dl>
<dd>
<pre>NAME=Fedora
VERSION=&quot;32 (Workstation Edition)&quot;
ID=fedora
VERSION_ID=32
PRETTY_NAME=&quot;Fedora 32 (Workstation Edition)&quot;
ANSI_COLOR=&quot;0;38;2;60;110;180&quot;
LOGO=fedora-logo-icon
CPE_NAME=&quot;cpe:/o:fedoraproject:fedora:32&quot;
HOME_URL=&quot;<a rel="nofollow" href="https://fedoraproject.org/">https://fedoraproject.org/</a>&quot;
DOCUMENTATION_URL=&quot;<a rel="nofollow" href="https://docs.fedoraproject.org/en-US/fedora/f32/system-administrators-guide/">https://docs.fedoraproject.org/en-US/fedora/f32/system-administrators-guide/</a>&quot;
SUPPORT_URL=&quot;<a rel="nofollow" href="https://fedoraproject.org/wiki/Communicating_and_getting_help">https://fedoraproject.org/wiki/Communicating_and_getting_help</a>&quot;
BUG_REPORT_URL=&quot;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&quot;
REDHAT_BUGZILLA_PRODUCT=&quot;Fedora&quot;
REDHAT_BUGZILLA_PRODUCT_VERSION=32
REDHAT_SUPPORT_PRODUCT=&quot;Fedora&quot;
REDHAT_SUPPORT_PRODUCT_VERSION=32
PRIVACY_POLICY_URL=&quot;<a rel="nofollow" href="https://fedoraproject.org/wiki/Legal:PrivacyPolicy">https://fedoraproject.org/wiki/Legal:PrivacyPolicy</a>&quot;
VARIANT=&quot;Workstation Edition&quot;
VARIANT_ID=workstation</pre>
</dl>
<p> <code>Example 2. Reading os-release in <a href="/docs/linux/man/1-sh/">sh</a>(1)</code> </p>
<dl>
<dd>
<pre>#!/bin/sh -eu
test -e /etc/os-release &amp;&amp; os_release='/etc/os-release' || os_release='/usr/lib/os-release'
. &quot;${os_release}&quot;
echo &quot;Running on ${PRETTY_NAME:-Linux}&quot;
if [ &quot;${ID:-linux}&quot; = &quot;debian&quot; ] || [ &quot;${ID_LIKE#*debian*}&quot; != &quot;${ID_LIKE}&quot; ]; then
 echo &quot;Looks like Debian!&quot;
fi</pre>
</dl>
<p> <code>Example 3. Reading os-release in <a href="/docs/linux/man/1-python/">python</a>(1) (versions &gt;= 3.10)</code> </p>
<dl>
<dd>
<pre>#!/usr/bin/python
# SPDX-License-Identifier: CC0-1.0
import platform
os_release = platform.freedesktop_os_release()
pretty_name = os_release.get('PRETTY_NAME', 'Linux')
print(f'Running on {pretty_name!r}')
if 'fedora' in [os_release.get('ID', 'linux'),
 *os_release.get('ID_LIKE', '').split()]:
 print('Looks like Fedora!')</pre>
</dl>
<p> See docs for m[blue]<code>platform.freedesktop_os_release</code>m[]<font SIZE="-2">[6]</font> for more details. </p>
<p> <code>Example 4. Reading os-release in <a href="/docs/linux/man/1-python/">python</a>(1) (any version)</code> </p>
<dl>
<dd>
<pre>#!/usr/bin/python
import ast
import re
import sys
def read_os_release():
 try:
 filename = '/etc/os-release'
 f = open(filename)
 except FileNotFoundError:
 filename = '/usr/lib/os-release'
 f = open(filename)
 for line_number, line in enumerate(f):
 line = line.rstrip()
 if not line or line.startswith('#'):
 continue
 if m := re.match(r'([A-Z][A-Z_0-9]+)=(.*)', line):
 name, val = m.groups()
 if val and val[0] in '&quot;\'':
 val = ast.literal_eval(val)
 yield name, val
 else:
 print(f'{filename}:{line_number + 1}: bad line {line!r}',
 file=sys.stderr)
os_release = dict(read_os_release())
pretty_name = os_release.get('PRETTY_NAME', 'Linux')
print(f'Running on {pretty_name!r}')
if 'debian' in [os_release.get('ID', 'linux'),
 *os_release.get('ID_LIKE', '').split()]:
 print('Looks like Debian!')</pre>
</dl>
<p> Note that the above version that uses the built-in implementation is preferred in most cases, and the open-coded version here is provided for reference.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-lsb_release/">lsb_release</a></code>(1), <code><a href="/docs/linux/man/5-hostname/">hostname</a></code>(5), <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5), <code><a href="/docs/linux/man/5-machine-info/">machine-info</a></code>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Announcement of /etc/os-release</p>
<dl>
<dd><a rel="nofollow" href="http://0pointer.de/blog/projects/os-release">http://0pointer.de/blog/projects/os-release</a></dl>
<dt> 2.</p>
<dd>initrd</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/admin-guide/initrd.html">https://www.kernel.org/doc/html/latest/admin-guide/initrd.html</a></dl>
<dt> 3.</p>
<dd>Common Platform Enumeration Specification</p>
<dl>
<dd><a rel="nofollow" href="http://scap.nist.gov/specifications/cpe/">http://scap.nist.gov/specifications/cpe/</a></dl>
<dt> 4.</p>
<dd>RFC3986 format</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc3986">https://tools.ietf.org/html/rfc3986</a></dl>
<dt> 5.</p>
<dd>freedesktop.org Icon Theme Specification</p>
<dl>
<dd><a rel="nofollow" href="http://standards.freedesktop.org/icon-theme-spec/latest">http://standards.freedesktop.org/icon-theme-spec/latest</a></dl>
<dt> 6.</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>platform.freedesktop_os_release</code></p>
<dl>
<dd><a rel="nofollow" href="https://docs.python.org/3/library/platform.html#platform.freedesktop_os_release">https://docs.python.org/3/library/platform.html#platform.freedesktop_os_release</a></dl>
