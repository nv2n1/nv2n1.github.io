---
title: "selinux_config(5)"
name: "selinux_config"
section: "5"
letter: "s"
url: "/docs/linux/man/5-selinux_config/"
description: "config – The SELinux sub-system configuration file."
---

<p>config &#8211; The SELinux sub-system configuration file.</p>
<h2>Description</h2>
<p>The SELinux <i>config</i> file controls the state of SELinux regarding:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>The policy enforcement status &#8211; <i>enforcing</i>, <i>permissive</i> or <i>disabled</i>.</p>
<dt>2.</p>
<dd>The policy name or type that forms a path to the policy to be loaded and its supporting configuration files.</p>
<dt>3.</p>
<dd>How local users and booleans will be managed when the policy is loaded (note that this function was used by older releases of SELinux and is now deprecated).</p>
<dt>4.</p>
<dd>How SELinux-aware login applications should behave if no valid SELinux users are configured.</p>
<dt>5.</p>
<dd>Whether the system is to be relabeled or not.</dl>
</dl>
<p> The entries controlling these functions are described in the <code>FILE FORMAT</code> section. The fully qualified path name of the SELinux configuration file is <i>/etc/selinux/config</i>. If the <i>config</i> file is missing or corrupt, then no SELinux policy is loaded (i.e. SELinux is disabled). The <code>sestatus</code> (8) command and the libselinux function <code>selinux_path</code> (3) will return the location of the <i>config</i> file. </p>
<h2>File Format</h2>
<p>The <i>config</i> file supports the following parameters: </p>
<dl>
<dd><code>SELINUX = </code><i>enforcing</i> | <i>permissive</i> | <i>disabled</i><br />
 <code>SELINUXTYPE = </code><i>policy_name</i><br />
 <code>SETLOCALDEFS = </code><i>0</i> | <i>1</i><br />
 <code>REQUIREUSERS = </code><i>0</i> | <i>1</i><br />
 <code>AUTORELABEL = </code><i>0</i> | <i>1</i></dl>
<p> Where:<br />
 <code>SELINUX</code></p>
<dl>
<dd>This entry can contain one of three values:</p>
<dl>
<dd>
<dl>
<dt><i>enforcing</i></p>
<dd>SELinux security policy is enforced.</p>
<dt><i>permissive</i></p>
<dd>SELinux security policy is not enforced but logs the warnings (i.e. the action is allowed to proceed).</p>
<dt><i>disabled</i></p>
<dd>SELinux is disabled and no policy is loaded.</dl>
</dl>
<p> The entry can be determined using the <code><a href="/docs/linux/man/8-sestatus/">sestatus</a></code>(8) command or <code><a href="/docs/linux/man/3-selinux_getenforcemode/">selinux_getenforcemode</a></code>(3).</dl>
<p> <code>SELINUXTYPE</code></p>
<dl>
<dd>The <i>policy_name</i> entry is used to identify the policy type, and becomes the directory name of where the policy and its configuration files are located. </p>
<p> The entry can be determined using the <code><a href="/docs/linux/man/8-sestatus/">sestatus</a></code>(8) command or <code><a href="/docs/linux/man/3-selinux_getpolicytype/">selinux_getpolicytype</a></code>(3). </p>
<p> The <i>policy_name</i> is relative to a path that is defined within the SELinux subsystem that can be retrieved by using <code><a href="/docs/linux/man/3-selinux_path/">selinux_path</a></code>(3). An example entry retrieved by <code><a href="/docs/linux/man/3-selinux_path/">selinux_path</a></code>(3) is: </p>
<dl>
<dd><i>/etc/selinux/</i></dl>
<p> The <i>policy_name</i> is then appended to this and becomes the &#8216;policy root&#8217; location that can be retrieved by <code><a href="/docs/linux/man/3-selinux_policy_root_path/">selinux_policy_root_path</a></code>(3). An example entry retrieved is:</p>
<dl>
<dd><i>/etc/selinux/targeted</i></dl>
<p> The actual binary policy is located relative to this directory and also has a policy name pre-allocated. This information can be retrieved using <code><a href="/docs/linux/man/3-selinux_binary_policy_path/">selinux_binary_policy_path</a></code>(3). An example entry retrieved by <code><a href="/docs/linux/man/3-selinux_binary_policy_path/">selinux_binary_policy_path</a></code>(3) is: </p>
<dl>
<dd><i>/etc/selinux/targeted/policy/policy</i></dl>
<p> The binary policy name has by convention the SELinux policy version that it supports appended to it. The maximum policy version supported by the kernel can be determined using the <code><a href="/docs/linux/man/8-sestatus/">sestatus</a></code>(8) command or <code><a href="/docs/linux/man/3-security_policyvers/">security_policyvers</a></code>(3). An example binary policy file with the version is: </p>
<dl>
<dd><i>/etc/selinux/targeted/policy/policy.24</i></dl>
</dl>
<p> <code>SETLOCALDEFS</code></p>
<dl>
<dd>This entry is deprecated and should be removed or set to <i>0</i>. </p>
<p> If set to <i>1</i>, then <code><a href="/docs/linux/man/3-selinux_mkload_policy/">selinux_mkload_policy</a></code>(3) will read the local customization for booleans (see <code><a href="/docs/linux/man/5-booleans/">booleans</a></code>(5)) and users (see <code><a href="/docs/linux/man/5-local-users/">local.users</a></code>(5)).</dl>
<p> <code>REQUIRESEUSERS</code></p>
<dl>
<dd>This optional entry can be used to fail a login if there is no matching or default entry in the <code><a href="/docs/linux/man/5-seusers/">seusers</a></code>(5) file or if the <code>seusers</code> file is missing. </p>
<p> It is checked by <code><a href="/docs/linux/man/3-getseuserbyname/">getseuserbyname</a></code>(3) that is called by SELinux-aware login applications such as <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8). </p>
<p> If set to <i>0</i> or the entry missing:</p>
<dl>
<dd><code><a href="/docs/linux/man/3-getseuserbyname/">getseuserbyname</a></code>(3) will return the GNU / Linux user name as the SELinux user.</dl>
<p> If set to <i>1</i>:</p>
<dl>
<dd><code><a href="/docs/linux/man/3-getseuserbyname/">getseuserbyname</a></code>(3) will fail.</dl>
<p> The <code><a href="/docs/linux/man/3-getseuserbyname/">getseuserbyname</a></code>(3) man page should be consulted for its use. The format of the <i>seusers</i> file is shown in <code><a href="/docs/linux/man/5-seusers/">seusers</a></code>(5). </p>
</dl>
<p> <code>AUTORELABEL</code></p>
<dl>
<dd>This is an optional entry that allows the file system to be relabeled. </p>
<p> If set to <i>0</i> and there is a file called <i>.autorelabel</i> in the root directory, then on a reboot, the loader will drop to a shell where a root login is required. An administrator can then manually relabel the file system. </p>
<p> If set to <i>1</i> or no entry present (the default) and there is a <i>.autorelabel</i> file in the root directory, then the file system will be automatically relabeled using <code>fixfiles -F restore</code> </p>
<p> In both cases the <i>/.autorelabel</i> file will be removed so that relabeling is not done again.</dl>
<h2>Example</h2>
<p>This example <i>config</i> file shows the minimum contents for a system to run SELinux in enforcing mode, with a <i>policy_name</i> of &#8216;targeted&#8217;:</p>
<dl>
<dd>SELINUX = enforcing<br />
 SELINUXTYPE = targeted</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/8-sestatus/">sestatus</a></code>(8), <code><a href="/docs/linux/man/3-selinux_path/">selinux_path</a></code>(3), <code><a href="/docs/linux/man/3-selinux_policy_root_path/">selinux_policy_root_path</a></code>(3), <code><a href="/docs/linux/man/3-selinux_binary_policy_path/">selinux_binary_policy_path</a></code>(3), <code><a href="/docs/linux/man/3-getseuserbyname/">getseuserbyname</a></code>(3), <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8), <code><a href="/docs/linux/man/8-fixfiles/">fixfiles</a></code>(8), <code><a href="/docs/linux/man/3-selinux_mkload_policy/">selinux_mkload_policy</a></code>(3), <code><a href="/docs/linux/man/3-selinux_getpolicytype/">selinux_getpolicytype</a></code>(3), <code><a href="/docs/linux/man/3-security_policyvers/">security_policyvers</a></code>(3), <code><a href="/docs/linux/man/3-selinux_getenforcemode/">selinux_getenforcemode</a></code>(3), <code><a href="/docs/linux/man/5-seusers/">seusers</a></code>(5), <code><a href="/docs/linux/man/5-booleans/">booleans</a></code>(5), <code><a href="/docs/linux/man/5-local-users/">local.users</a></code>(5) </p>
