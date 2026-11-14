---
title: "sa-update(1)"
name: "sa-update"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sa-update/"
description: "sa-update – automate SpamAssassin rule updates"
---

<h2 class="name">NAME</h2>
<p> sa-update &#8211; automate SpamAssassin rule updates </p>
<h2>SYNOPSIS</h2>
<p> <code>sa-update</code> [options] </p>
<p> Options: </p>
<pre><code>
  --channel channel       Retrieve updates from this channel
                          Use multiple times for multiple channels
  --channelfile file      Retrieve updates from the channels in the file
  --checkonly             Check for update availability, do not install
  --install filename      Install updates directly from this file. Signature
                          verification will use "file.asc" and "file.sha1"
  --allowplugins          Allow updates to load plugin code
  --gpgkey key            Trust the key id to sign releases
                          Use multiple times for multiple keys
  --gpgkeyfile file       Trust the key ids in the file to sign releases
  --gpghomedir path       Store the GPG keyring in this directory
  --gpg and --nogpg       Use (or do not use) GPG to verify updates
                          (--gpg is assumed by use of the above
                          --gpgkey and --gpgkeyfile options)
  --import file           Import GPG key(s) from file into sa-update's
                          keyring. Use multiple times for multiple files
  --updatedir path        Directory to place updates, defaults to the
                          SpamAssassin site rules directory
                          (default: /var/lib/spamassassin/3.004000)
  --refreshmirrors        Force the MIRRORED.BY file to be updated
  -D, --debug [area=n,...]  Print debugging messages
  -v, --verbose           Be verbose, like print updated channel names;
  For more verbosity specify multiple times - V, --version Print version - h, --help Print usage message - 4 Force using the inet protocol(IPv4), not inet6 - 6 Force using the inet6 protocol(IPv6), not inet
</code></pre>
<h2>DESCRIPTION</h2>
<p> sa-update automates the process of downloading and installing new rules and configuration, based on channels. The default channel is <i>updates.spamassassin.org</i>, which has updated rules since the previous release. </p>
<p> Update archives are verified using <font SIZE="-1">SHA1</font> hashes and <font SIZE="-1">GPG</font> signatures, by default. </p>
<p> Note that <tt>&quot;sa-update&quot;</tt> will not restart <tt>&quot;spamd&quot;</tt> or otherwise cause a scanner to reload the now-updated ruleset automatically. Instead, <tt>&quot;sa-update&quot;</tt> is typically used in something like the following manner: </p>
<pre>
        sa-update &amp;&amp; /etc/init.d/spamassassin reload
</pre>
<p> This works because <tt>&quot;sa-update&quot;</tt> only returns an exit status of <tt>0</tt> if it has successfully downloaded and installed an updated ruleset. </p>
<p> The program sa-update uses the underlying operating system umask for the updated rule files it installs. You may wish to run sa-update from a script that sets the umask prior to calling sa-update. For example: </p>
<pre>
        #!/bin/sh
        umask 022
        sa-update
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;channel</code></p>
<dd> sa-update can update multiple channels at the same time. By default, it will only access &#8220;updates.spamassassin.org&#8221;, but more channels can be specified via this option. If there are multiple additional channels, use the option multiple times, once per channel. i.e.: </p>
<pre>
        sa-update --channel foo.example.com --channel bar.example.com
</pre>
<dt><code>&#8211;channelfile</code></p>
<dd> Similar to the <code>&#8211;channel</code> option, except specify the additional channels in a file instead of on the commandline. This is useful when there are a lot of additional channels.</p>
<dt><code>&#8211;checkonly</code></p>
<dd> Only check if an update is available, don&#8217;t actually download and install it. The exit code will be <tt>0</tt> or <tt>1</tt> as described below.</p>
<dt><code>&#8211;install</code></p>
<dd> Install updates &#8220;offline&#8221;, from the named tar.gz file, instead of performing <font SIZE="-1">DNS</font> lookups and <font SIZE="-1">HTTP</font> invocations. </p>
<p> Files named <code>file</code>.sha1 and <code>file</code>.asc will be used for the <font SIZE="-1">SHA-1</font> and <font SIZE="-1">GPG</font> signature, respectively. The filename provided must contain a version number of at least 3 digits, which will be used as the channel&#8217;s update version number. </p>
<p> Multiple <code>&#8211;channel</code> switches cannot be used with <code>&#8211;install</code>. To install multiple channels from tarballs, run <tt>&quot;sa-update&quot;</tt> multiple times with different <code>&#8211;channel</code> and <code>&#8211;install</code> switches, e.g.: </p>
<pre><code>
sa - update-- channel foo.example.com-- install foo - 34958.tgz sa - update-- channel bar.example.com-- install bar - 938455.tgz
</code></pre>
<dt><code>&#8211;allowplugins</code></p>
<dd> Allow downloaded updates to activate plugins. The default is not to activate plugins; any <tt>&quot;loadplugin&quot;</tt> or <tt>&quot;tryplugin&quot;</tt> lines will be commented in the downloaded update rules files.</p>
<dt><code>&#8211;gpg</code>, <code>&#8211;nogpg</code></p>
<dd> sa-update by default will verify update archives by use of a <font SIZE="-1">SHA1</font> checksum and <font SIZE="-1">GPG</font> signature. <font SIZE="-1">SHA1</font> hashes can verify whether or not the downloaded archive has been corrupted, but it does not offer any form of security regarding whether or not the downloaded archive is legitimate (aka: non-modifed by evildoers). <font SIZE="-1">GPG</font> verification of the archive is used to solve that problem. </p>
<p> If you wish to skip <font SIZE="-1">GPG</font> verification, you can use the <code>&#8211;nogpg</code> option to disable its use. Use of the following gpgkey-related options will override <code>&#8211;nogpg</code> and keep <font SIZE="-1">GPG</font> verification enabled. </p>
<p> Note: Currently, only <font SIZE="-1">GPG</font> itself is supported (ie: not <font SIZE="-1">PGP</font>). v1.2 has been tested, although later versions ought to work as well.</p>
<dt><code>&#8211;gpgkey</code></p>
<dd> sa-update has the concept of &#8220;release trusted&#8221; <font SIZE="-1">GPG</font> keys. When an archive is downloaded and the signature verified, sa-update requires that the signature be from one of these &#8220;release trusted&#8221; keys or else verification fails. This prevents third parties from manipulating the files on a mirror, for instance, and signing with their own key. </p>
<p> By default, sa-update trusts key ids <tt>&quot;24F434CE&quot;</tt> and <tt>&quot;5244EC45&quot;</tt>, which are the standard SpamAssassin release key and its sub-key. Use this option to trust additional keys. See the <code>&#8211;import</code> option for how to add keys to sa-update&#8217;s keyring. For sa-update to use a key it must be in sa-update&#8217;s keyring and trusted. </p>
<p> For multiple keys, use the option multiple times. i.e.: </p>
<pre>
        sa-update --gpgkey E580B363 --gpgkey 298BC7D0
</pre>
<p> Note: use of this option automatically enables <font SIZE="-1">GPG</font> verification.</p>
<dt><code>&#8211;gpgkeyfile</code></p>
<dd> Similar to the <code>&#8211;gpgkey</code> option, except specify the additional keys in a file instead of on the commandline. This is extremely useful when there are a lot of additional keys that you wish to trust.</p>
<dt><code>&#8211;gpghomedir</code></p>
<dd> Specify a directory path to use as a storage area for the <tt>&quot;sa-update&quot;</tt> <font SIZE="-1">GPG</font> keyring. By default, this is </p>
<pre>
        /etc/mail/spamassassin/sa-update-keys
</pre>
<dt><code>&#8211;import</code></p>
<dd> Use to import <font SIZE="-1">GPG</font> key(s) from a file into the sa-update keyring which is located in the directory specified by <code>&#8211;gpghomedir</code>. Before using channels from third party sources, you should use this option to import the <font SIZE="-1">GPG</font> key(s) used by those channels. You must still use the <code>&#8211;gpgkey</code> or <code>&#8211;gpgkeyfile</code> options above to get sa-update to trust imported keys. </p>
<p> To import multiple keys, use the option multiple times. i.e.: </p>
<pre>
        sa-update --import channel1-GPG.KEY --import channel2-GPG.KEY
</pre>
<p> Note: use of this option automatically enables <font SIZE="-1">GPG</font> verification.</p>
<dt><code>&#8211;refreshmirrors</code></p>
<dd> Force the list of sa-update mirrors for each channel, stored in the <font SIZE="-1">MIRRORED.BY</font> file, to be updated. By default, the <font SIZE="-1">MIRRORED.BY</font> file will be cached for up to 7 days after each time it is downloaded.</p>
<dt><code>&#8211;updatedir</code></p>
<dd> By default, <tt>&quot;sa-update&quot;</tt> will use the system-wide rules update directory: </p>
<pre>
        /var/lib/spamassassin/3.004000
</pre>
<p> If the updates should be stored in another location, specify it here. </p>
<p> Note that use of this option is not recommended; if you&#8217;re just using sa-update to download updated rulesets for a scanner, and sa-update is placing updates in the wrong directory, you probably need to rebuild SpamAssassin with different <tt>&quot;Makefile.PL&quot;</tt> arguments, instead of overriding sa-update&#8217;s runtime behaviour.</p>
<dt><code>-D</code> [<i>area,&#8230;</i>], <code>&#8211;debug</code> [<i>area,&#8230;</i>]</p>
<dd> Produce debugging output. If no areas are listed, all debugging information is printed. Diagnostic output can also be enabled for each area individually; <i>area</i> is the area of the code to instrument. For example, to produce diagnostic output on channel, gpg, and http, use: </p>
<pre>
        sa-update -D channel,gpg,http
</pre>
<p> For more information about which areas (also known as channels) are available, please see the documentation at &lt;<a rel="nofollow" href="http://wiki.apache.org/spamassassin/DebugChannels">http://wiki.apache.org/spamassassin/DebugChannels</a>&gt;.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print sa-update version and exit.</dl>
<h2>EXIT CODES</h2>
<p> An exit code of <tt>0</tt> means an update was available, and was downloaded and installed successfully if &#8211;checkonly was not specified. </p>
<p> An exit code of <tt>1</tt> means no fresh updates were available. </p>
<p> An exit code of <tt>2</tt> means that at least one update is available but that a lint check of the site pre files failed. The site pre files must pass a lint check before any updates are attempted. </p>
<p> An exit code of <tt>3</tt> means that at least one update succeeded while other channels failed. If using sa-compile, you should proceed with it. </p>
<p> An exit code of <tt>4</tt> or higher, indicates that errors occurred while attempting to download and extract updates, and no channels were updated.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-mail--spamassassin/">Mail::SpamAssassin</a></i>(3) <i><a href="/docs/linux/man/3-mail--spamassassin--conf/">Mail::SpamAssassin::Conf</a></i>(3) <i><a href="/docs/linux/man/1-spamassassin/">spamassassin</a></i>(1) <i><a href="/docs/linux/man/1-spamd/">spamd</a></i>(1) &lt;<a rel="nofollow" href="http://wiki.apache.org/spamassassin/RuleUpdates">http://wiki.apache.org/spamassassin/RuleUpdates</a>&gt;</p>
<h2>PREREQUESITES</h2>
<p> <tt>&quot;Mail::SpamAssassin&quot;</tt></p>
<h2>BUGS</h2>
<p> See &lt;<a rel="nofollow" href="http://issues.apache.org/SpamAssassin/">http://issues.apache.org/SpamAssassin/</a>&gt;</p>
<h2>AUTHORS</h2>
<p> The Apache SpamAssassin(tm) Project &lt;<a rel="nofollow" href="http://spamassassin.apache.org/">http://spamassassin.apache.org/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> SpamAssassin is distributed under the Apache License, Version 2.0, as described in the file <tt>&quot;LICENSE&quot;</tt> included with the distribution. </p>
<h2>Index</h2>
