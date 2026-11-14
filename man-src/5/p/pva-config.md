---
title: "pva-config(5)"
name: "pva-config"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pva-config/"
description: "pva-config – general PHP VOMS-Admin interface configuration"
---

<p>pva-config &#8211; general PHP VOMS-Admin interface configuration</p>
<h2>Description</h2>
<p>Configauration file for general PHP VOMS-Admin interface settings </p>
<h2>Synopsis</h2>
<p><code>/etc/pva/pva-config</code> </p>
<h2>Extended Description</h2>
<dl>
<dt>Configuration file is the PHP script containing configuration variables:</p>
<dd><code>&lt;?php</code><br />
 <code>$variable1=keyword;</code><br />
 <code>$variable2=keyword;</code> </p>
<p> <code>$variableN=keyword;</code><br />
 <code>?&gt;</code> </p>
<p> PHP supports &#8216;C&#8217;, &#8216;C++&#8217; and Unix shell-style comments that can be used in file. </p>
<p> Configuration file contains several configuration variables:</p>
<dt><code>pva_install_path</code></p>
<dd>path to directory containing PHP VOMS-Admin web-interface files root </p>
<p> <i>Example:</i> $pva_install_path=&quot;/usr/share/pva&quot;;</p>
<dt><code>ca_certificates_path</code></p>
<dd>path to trusted CA certificates installation </p>
<p> <i>Example: </i> $ca_certificates_path=&quot;/etc/grid-security/certificates&quot;;</p>
<dt><code>mail_filecopies_path</code></p>
<dd>path to directory for storing e-mail copies; when variable is set e-mail sent to VOMS administrator also stored in the file </p>
<p> <i>Example: </i> $mail_filecopies_path=&quot;/var/www/pva/mail-copies&quot;; </p>
<dt><code>items_per_page</code></p>
<dd>determine how many entries (users, groups, roles, etc) will be shown simultaneously on the same page during PHP VOMS-Admin output </p>
<p> <i>Example:</i> $items_per_page=10;</p>
<dt><code>lastresort_permissions</code></p>
<dd>set the default numeric permissions applied, when more specific match is not found in ACL table (see <code>PERMISSIONS</code> ). HTTP insecure access is the most common example of lastresort_permissions appliance </p>
<p> <i>Example:</i> $lastresort_permissions = 517;</p>
<dt><code>mail_from</code></p>
<dd>e-mail address used for sending e-mails from PHP VOMS-Admin </p>
<p> <i>Example:</i> $mail_from = &quot;pva [at] example.org&quot;;</p>
<dt><code>mail_from_name</code></p>
<dd>name used for sending e-mails from PHP VOMS-Admin </p>
<p> <i>Example:</i> $mail_from_name = &quot;PHP VOMS Admin&quot;;</p>
<dt><code>voms_admin_mail</code></p>
<dd>contact e-mail address of PHP VOMS Admin server administrator </p>
<p> <i>Example:</i> $voms_admin_mail = &quot;admin [at] example.org&quot;; </p>
</dl>
<h2>Permissions</h2>
<p>The following permissions are supported by PHP VOMS-Admin:</p>
<dl>
<dt><code>Container:Read (1)</code></p>
<dd>view information about groups and roles</p>
<dt><code>Container:Write (2)</code></p>
<dd>view groups membership and roles assignment</p>
<dt><code>Membership:Read (4) </code></p>
<dd>list VO users</p>
<dt><code>Membership:Write (8)</code></p>
<dd>create/modify/delete VO users</p>
<dt><code>ACL:List (16)</code></p>
<dd>view ACLs permissions</p>
<dt><code>ACL:Set (32)</code></p>
<dd>define general ACLs permissions</p>
<dt><code>ACL:Defaults (64)</code></p>
<dd>define default ACLs permissions</p>
<dt><code>Subscription:List (128)</code></p>
<dd>view membership VO requests</p>
<dt><code>Subscription:Define (256)</code></p>
<dd>approve/decline membership requests</p>
<dt><code>Attributes:List (512)</code></p>
<dd>view assigned attributes</p>
<dt><code>Attributes:Manage (1024)</code></p>
<dd>create/assign attributes</p>
<dt><code>Preferences:Read (2048)</code></p>
<dd>view VO preferences options</p>
<dt><code>Preferences:Write (4096)</code></p>
<dd>modify VO preferences options </p>
</dl>
<p> Permissions numerical decimal values shown in parentheses. Adding numerical values for each allowed action results total ACL numeric permissions.</p>
<dl>
<dt><i>Example:</i></p>
<dd>517 = <a href="/docs/linux/man/1-container-read/">Container:Read</a>(1) + <a href="/docs/linux/man/4-membership-read/">Membership:Read</a>(4) + Attributes:List(512)</dl>
<p> For more information read PHP VOMS-Admin operation manual: <i><a rel="nofollow" href="http://grid.org.ua/development/pva/?act=manual">http://grid.org.ua/development/pva/?act=manual</a></i></p>
<h2>Author</h2>
<p>Andrii Salnikov &lt;manf [at] grid.org.ua&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pva-addvo/">pva-addvo</a></code>(1), <code><a href="/docs/linux/man/5-addvo-conf/">addvo.conf</a></code>(5), <code><a href="/docs/linux/man/8-voms/">voms</a></code>(8) </p>
