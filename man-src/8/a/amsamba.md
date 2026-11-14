---
title: "amsamba(8)"
name: "amsamba"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amsamba/"
description: "amsamba – Amanda Application to interface with smbclient"
---

<p>amsamba &#8211; Amanda Application to interface with smbclient</p>
<h2>Description</h2>
<p>Amsamba is an Amanda Application API script. It should not be run by users directly. It uses smbclient to backup and restore data. </p>
<p> The <code>diskdevice</code> in the disklist (DLE) must have the form &#8216;//CIFSHOST/SHARE/SUBDIR&#8217; where CIFSHOST is the CIFS host containing the data to be backed up, SHARE is the share to connect, and subdir is the subdirectory to backup. &#8216;/subdir&#8217; can be ommited, in which case the complete share is archived. </p>
<p> Unlike most applications, amsamba backs up and restores data located on a different system from that where amsamba itself runs. The host containing the data is the CIFS host. In practice, amsamba is usually run on the same system as the Amanda server, with a DLE like </p>
<pre>localhost &quot;//CIFSHOST/SHARENAME&quot; amsamba-dumptype</pre>
<p>Include or exclude can be used, but not both. The path for &#8216;exclude list&#8217; or &#8216;include list&#8217; must be absolute path on the CIFS host. The estimate calculates the complete size of the share, without regard for include or exclude directives. It will be larger than the actual dump if you use include or exclude. Using &#8216;estimate server&#8217; in the dumptype could give better estimate.</p>
<h2>Properties</h2>
<p>This section lists the properties that control amsamba&#8217;s functionality. See <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7) for information on application properties and how they are configured. </p>
<p> SMBCLIENT-PATH</p>
<dl>
<dd>The path to the smbclient binary. The default is set when Amanda is built by the &#8211;with-smbclient configure option.</dl>
<p> GNUTAR-PATH</p>
<dl>
<dd>The path to the gnutar binary. The default is set when Amanda is built by the &#8211;with-gnutar configure option. gnutar is used to create the index.</dl>
<p> AMANDAPASS</p>
<dl>
<dd>Location of the amandapass file, defaulting to &quot;$CONFIG_DIR/amandapass&quot;. Relative pathnames are relative to the configuration directory, &quot;$CONFIG_DIR/&lt;config&gt;&quot;. Note that this file is located on the client, not on the server. The format of the file is as follow: </p>
<pre> Sharename User%Password Domain</pre>
<p>Sharename is &#8216;//HOST/SHARE&#8217; without the SUBDIR. Sharename can be quoted, it can be &#8216;*&#8217; to match all share, it can be &#8216;//pc-host/*&#8217; to match all share on pc-host. User is the username use to connect to the share. Password is the password use to connect to the share. &#8216;%Password&#8217; is optional if the user can connect to the share without password. &#8216;User%Password&#8217; is optional, the user &#8216;guest&#8217; without password is use to connect to the share. Domain is optional. Example: </p>
<pre> //another-pc/share otheruser%otherpw domain
 //another-pc/share otheruser%otherpw
 //another-pc/share myuser mydomain
 //another-pc/share myuser
 //another-pc/share</pre>
</dl>
<p> ALLOW-ANONYMOUS</p>
<dl>
<dd>This username without password is used to connect to the share if no matching entry is found in the amandapass file.</dl>
<p> DIRECTORY</p>
<dl>
<dd>For restore command only, the data is recoved in that directory. Must be a unix path for &quot;tar&quot; RECOVER-MODE or a smb path for &quot;smb&quot; recover-MODE.</dl>
<p> RECOVER-MODE</p>
<dl>
<dd>&quot;tar&quot; or &quot;smb&quot;, default to &quot;tar&quot;. If &quot;tar&quot;, the data is recovered on the local machine, If &quot;smb&quot;, the data is recovered on the smb client machine.</dl>
<h2>Include And Exclude Lists</h2>
<p>This application supplies exclude lists via the <code>smbclient</code> <code>-TX</code> option. Normal shell-style wildcard expressions, using * and ?, are not supported. All expressions are matched only from the base directory of the DLE. Expressions that match a directory may have a leading or trailing &quot;/&quot;. Example expressions: </p>
<pre> ./temp-files # exclude top-level dir &quot;temp-files&quot; entirely
 ./temp-files/ # same
 /temp-files # same
 temp-files # same
 ./temp-files/* # BAD: does nothing
 *.iso # BAD: does nothing
 proxy/local/cache # exclude &quot;cache&quot; in dir &quot;proxy/local&quot;</pre>
<p>Include lists are supported only if excludes are not given. They are handled via the <code>smbclient</code> <code>-TI</code> option. Include matching is identical to the exclude matching described above.</p>
<h2>Example</h2>
<pre> define application app_amsamba {
 property &quot;SMBCLIENT-PATH&quot; &quot;/usr/bin/smbclient&quot;
 property &quot;GNUTAR-PATH&quot; &quot;/bin/tar&quot;
 property &quot;AMANDAPASS&quot; /etc/amandapass&quot;
 property &quot;ALLOW-ANONYMOUS&quot; &quot;guest&quot;
 }</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
