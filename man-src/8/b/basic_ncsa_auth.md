---
title: "basic_ncsa_auth(8)"
name: "basic_ncsa_auth"
section: "8"
letter: "b"
url: "/docs/linux/man/8-basic_ncsa_auth/"
description: "basic_ncsa_auth – NCSA httpd-style password file authentication helper for Squid"
---

<p>basic_ncsa_auth &#8211; NCSA httpd-style password file authentication helper for Squid</p>
<h2>Synopsis</h2>
<p><code>basic_ncsa_auth</code> passwd file</p>
<h2>Description</h2>
<p><code>basic_ncsa_auth</code> allows Squid to read and authenticate user and password information from an NCSA/Apache httpd-style password file when using basic HTTP authentication. </p>
<p> This password file can be manipulated using <code>htpasswd.</code> </p>
<p> This authenticator accepts: * Blowfish &#8211; for passwords 72 characters or less in length * SHA256 &#8211; with salting and magic strings * SHA512 &#8211; with salting and magic strings * MD5 &#8211; with optional salt and magic strings * DES &#8211; for passwords 8 characters or less in length NOTE: Blowfish and SHA algorithms require system-specific support.</p>
<h2>Options</h2>
<p>The only parameter is the password file. It must have permissions to be read by the user that Squid is running as.</p>
<h2>Configuration</h2>
<dl>
<dd><code>basic_ncsa_auth /etc/squid/squid.pass</code></dl>
<p> <code>basic_ncsa_auth</code> must have access to the password file to be executed.</p>
<h2>Known Issues</h2>
<p>DES functionality (used by htpasswd by default) silently truncates passwords to 8 characters. Allowing login with password values shorter than the one desired. This authenticator will reject login with long passwords when using DES.</p>
<h2>Author</h2>
<p>This manual was written by <i>Amos Jeffries &lt;amosjeffries [at] squid-cache.org&gt;</i> </p>
<p> Based on original documentation by <i>Rodrigo Rubira Branco &lt;rrbranco [at] br.ibm.com&gt;</i></p>
<h2>Copyright</h2>
<p>&nbsp;<wbr>*&nbsp;<wbr>Copyright&nbsp;<wbr>(C)&nbsp;<wbr>1996-2016 The Squid Software Foundation and contributors<br />
&nbsp;<wbr>*<br />
&nbsp;<wbr>*&nbsp;<wbr>Squid software is distributed under GPLv2+&nbsp;<wbr>license and includes<br />
&nbsp;<wbr>*&nbsp;<wbr>contributions from numerous individuals and organizations.<br />
&nbsp;<wbr>*&nbsp;<wbr>Please see the COPYING and CONTRIBUTORS files for details. </p>
<p> This file is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this file; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA</p>
<h2>Questions</h2>
<p>Questions on the usage of this program can be sent to the <i>Squid Users mailing list</i> &lt;squid-users [at] squid-cache.org&gt;</p>
<h2>Reporting Bugs</h2>
<p>Bug reports need to be made in English. See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org&gt;</i> </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list</i> &lt;squid-dev [at] squid-cache.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-squid/">squid</a></code>(8), <code><a href="/docs/linux/man/1-htpasswd/">htpasswd</a></code>(1), <code><a href="/docs/linux/man/7-gpl/">GPL</a></code>(7),<br />
 The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a><br />
 The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
