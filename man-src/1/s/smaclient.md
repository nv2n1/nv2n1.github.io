---
title: "smaclient(1)"
name: "smaclient"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smaclient/"
description: "smaclient – tool for accessing z/VM System Management functions"
---

<h2>NAME</h2>
<p> smaclient &#8211; tool for accessing z/VM System Management functions</p>
<h2>SYNOPSIS</h2>
<p> <code>smaclient</code> [FUNCTION] [OPTION] [PARAMETER]<br />
 <code>smaclient</code> [-?|&#8211;help]<br />
 <code>smaclient</code> [-T <i>target</i>] [-H <i>host</i>] [-U <i>user</i>] [-P <i>pass</i>] &lt;function&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>smaclient</code> is a tool which provides a line-mode interface to the z/VM System Management API (SMAPI) for most Unix-compatible systems such as Linux. Smaclient can exercise all the VM management interfaces to create, modify and destroy virtual machines without ever logging into z/VM.</p>
<dl>
<dt>Executing smaclient without any arguments will print a list of available arguments and options.</p>
<dd></dl>
<h2>REQUIRED OPTIONS</h2>
<dl>
<dt><code>-T</code>, <code>&#8211;target</code>=<i>TARGET</i></p>
<dd> set the target image or authorization entry name</dl>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-H</code>, <code>&#8211;smhost</code>=<i>HOST</i></p>
<dd> hostname/port of SMAPI server. Specify IUCV if SMAPI IUCV is desired</p>
<dt><code>-U</code>, <code>&#8211;smuser</code>=<i>USER</i></p>
<dd> authorized SMAPI userid</p>
<dt><code>-P</code>, <code>&#8211;smpass</code>=<i>PASS</i></p>
<dd> authorized SMAPI password</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> output usage information</dl>
<h2>FUNCTIONS</h2>
<dl>
<dt>supported long function names MUST match SMAPI function name. For a list of supported functions, execute smaclient without arguments.</p>
<dd></dl>
<h2>FILES</h2>
<p> /etc/smaclient.conf<br />
 ~/.smaclient</p>
<dl>
<dt>For /etc/smaclient.conf and ~/.smaclient, you can specify any or all of the following variables:</p>
<dd></dl>
<p> <code>smhost</code> </p>
<dl>
<dt>
<dd> For TCP/IP, specify the SMAPI host and port number. The format is:</p>
<dl>
<dt>
<dd> hostname/portnumber</dl>
<p> For IUCV, specify the literal &quot;IUCV&quot;.</dl>
<dl>
<dt><code>smuser</code></p>
<dd>
 For TCP/IP, specify the userid authorized to use SMAPPI.<br />
 For IUCV, there&#8217;s no need to specify this, but it doesn&#8217;t hurt.</p>
<dt><code>smpass</code></p>
<dd>
 For TCP/IP, specify the corresponding password.<br />
 For IUCV, there&#8217;s no need to specify this, but it doesn&#8217;t hurt.</p>
<dt>An example ~/.smaclient:</p>
<dd></dl>
<p> smhost=&quot;myzvm/44444&quot;<br />
 smuser=&quot;vsmuser&quot;<br />
 smpass=&quot;secret&quot;</p>
<h2>AUTHOR</h2>
<p> smaclient written by Leland Lucius one fun week in the snowy winter of 2011. Manpage written by Rafael Fonseca.</p>
<h2>LICENSE</h2>
<p> Released under the Artistic License 2.0. Full license text can be found at <a rel="nofollow" href="http://opensource.org/licenses/artistic-license-2.0">http://opensource.org/licenses/artistic-license-2.0</a> </p>
<h2>Index</h2>
