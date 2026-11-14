---
title: "org(7)"
name: "org"
section: "7"
letter: "o"
url: "/docs/linux/man/7-org/"
description: "org.debian.apt.transaction – the main interface of an aptdaemon transaction"
---

<p>org.debian.apt.transaction &#8211; the main interface of an aptdaemon transaction</p>
<h2>Synopsis</h2>
<p>Each transaction is represented as an unique D-Bus object, e.g. at the D-Bus path <i>/or/debian/apt/transaction/12123-123-123213</i>. Which provides the following interface.</p>
<h2>Description</h2>
<h3>Methods</h3>
<dl>
<dt><code>ProvideMedium</code></p>
<dd><code>ProvideMedium (in &#8216;s&#8217; </code><i>medium</i><code>)</code></p>
<dl>
<dd>Continue a paused transaction which is waiting for the given <i>medium</i>. </p>
<p> If a media change is required to e.g. install packages from a CD/DVD the transaction will be paused and the RequiredMedium property changed to an array of the <i>medium label</i> and its <i>mount point</i>. Furthermore the MediumRequired signal will be emitted.</dl>
<dt><code>ResolveConfigFileConflict</code></p>
<dd><code>ResolveConfigFilePrompt (in &#8216;s&#8217; </code><i>config</i><code>,</code><br />
 <code> in &#8216;s&#8217; </code><i>answer</i><code>)</code></p>
<dl>
<dd>Continue a paused transaction which is waiting for an answer to handle a configuration file conflict. <i>Config</i> is the path to the current configuration file and <i>answer</i> can be either &quot;replace&quot; or &quot;keep&quot;. </p>
<p> If a later config file is shipped in a package which overrides some user modifications the transaction will be paused and the ConfigFileConflict property of the transaction will be set to an array of the old and new configuration file path. The later one is supposed to replace the former one. Furthermore the ConfigFileConflict signal will be emitted.</dl>
<dt><code>Simulate</code></p>
<dd><code>Simulate ()</code></p>
<dl>
<dd>Simulate the transaction and calculate dependencies, required disk space and download size. If a transaction would fail the corresponding error will be raised.</dl>
<dt><code>Run</code></p>
<dd><code>Run ()</code></p>
<dl>
<dd>Queue the transaction for processing. Afterwards there cannot be made any further changes to the transaction, e.g. modifing the http proxy.</dl>
<dt><code>Cancel</code></p>
<dd><code>Cancel ()</code></p>
<dl>
<dd>Cancel the transaction if possible.</dl>
</dl>
<h3>Signals</h3>
<dl>
<dt><code>Finished</code></p>
<dd><code>Finished (&#8216;s&#8217; </code><i>exit_state</i><code>)</code></p>
<dl>
<dd>The signal will be emitted when the transaction has been processed. The <i>exit_state</i> indicates if the transaction was completed, cancelled or failed.</dl>
<dt><code>MediumRequired</code></p>
<dd><code>MediumRequired (&#8216;s&#8217; </code><i>label</i><code>,</code><br />
 <code> &#8216;s&#8217; </code><i>mount_point</i><code>)</code></p>
<dl>
<dd>The signal will be emitted if the transaction has been paused and waits for a media change to install packages.</dl>
<dt><code>ConfigFileConflict</code></p>
<dd><code>ConfigFileConflict (&#8216;s&#8217; </code><i>old</i><code>,</code><br />
 <code> &#8216;s&#8217; </code><i>new</i><code>)</code></p>
<dl>
<dd>The signal will be emitted if the transaction has been paused because a <i>new</i> configuration file is shipped in a package which would override changes by the user in the <i>old</i> configuration file.</dl>
<dt><code>PropertyChanged</code></p>
<dd><code>PropertyChanged (&#8216;s&#8217;</code><i> property_name ,</i><br />
 <code> &#8216;v&#8217; </code><i>value</i><code>)</code></p>
<dl>
<dd>The signal will be emitted if one of the following properties has changed.</dl>
</dl>
<h3>Properties</h3>
<p>The properties of the transaction are available through the Get And GetAll methods of the D-Bus properties interface and can be changed using the Set method.</p>
<dl>
<dt><code>Role</code> read &#8216;s&#8217;</p>
<dd>The role enum of the transaction, e.g. update-cache.</p>
<dt><code>Status</code> read &#8216;s&#8217;</p>
<dd>The current status enum of the transaction, e.g. downloading</p>
<dt><code>StatusDetails</code> read &#8216;s&#8217;</p>
<dd>A clear text message describing the current status.</p>
<dt><code>Progress</code> read &#8216;i&#8217;</p>
<dd>The progress of the transaction in percent.</p>
<dt><code>ProgressDownload</code> read &#8216;sssiis&#8217;</p>
<dd>The last download progress information recieved from APT. It is an array of the URI, status enum, short description, full size, already downloaded size and an error or status message.</p>
<dt><code>Space</code> read &#8216;i&#8217;</p>
<dd>The additional disk space in Bytes which will be required by the transaction. The <code>Simulate</code> method has to be called to calculate the download size.</p>
<dt><code>Download</code> read &#8216;i&#8217;</p>
<dd>The required download size in Bytes of the transaction. The <code>Simulate</code> method has to be called to calculate the download size.</p>
<dt><code>Packages</code> read &#8216;a(a(s)a(s)a(s)a(s)a(s)a(s)a(s))&#8217;</p>
<dd>The lists of packages which are initially queued to be installed, reinstalled, removed, purged, upgraded, downgraded or skipped from upgrading.</p>
<dt><code>Dependenciens</code> read &#8216;a(a(s)a(s)a(s)a(s)a(s)a(s)a(s))&#8217;</p>
<dd>The lists of packages which are additionally required to be installed, reinstalled, removed, purged, upgraded, downgraded or skipped from upgrading. The <code>Simulate</code> method has to be called to calculate the dependencies.</p>
<dt><code>Cancellable</code> read &#8216;b&#8217;</p>
<dd>If the transaction can be cancelled.</p>
<dt><code>TerminalAttached</code> read &#8216;b&#8217;</p>
<dd>If the master pty which has to be set using the Terminal property is attached as controlling terminal to the underlying dpkg call.</p>
<dt><code>RequiredMedium</code> read &#8216;a(ss)&#8217;</p>
<dd>The transaction will be stopped if a media change is required to install packages. This property provides the <i>label</i> and the <i>mount point</i> of the requested medium.</p>
<dt><code>ConfigFileConflict</code> read &#8216;a(ss)&#8217;</p>
<dd>The transaction will be stopped if a configuration file shipped in the package overrides changes of the user. This property provides the path to <i>current</i> and the path to the <i>new</i> configuration file.</p>
<dt><code>ExitState</code> read &#8216;s&#8217;</p>
<dd>The exit state enum of the transaction.</p>
<dt><code>Error</code> read &#8216;a(ss)&#8217;</p>
<dd>If an error occured this property provides the <i>error enum</i> and the <i>error message.</i></p>
<dt><code>Locale</code> read-write &#8216;s&#8217;</p>
<dd>This is the locale which will be used for translating status and error messages of apt, e.g. de_DE [at] utf-8.</p>
<dt><code>Terminal</code> read-write &#8216;s&#8217;</p>
<dd>The path to the master pty which will be the controlling terminal of the underlying dpkg call. This allows to have an interactive terminal session.</p>
<dt><code>DebconfSocket</code> read-write &#8216;s&#8217;</p>
<dd>The path to the socket which will be used by the debconf passthrough backend to forward the debconf communication to the user session.</p>
<dt><code>Paused</code> read &#8216;b&#8217;</p>
<dd>If the transaction is paused, e.g. waiting for a conflict file resolution or media change.</p>
<dt><code>Unauthenticated</code> read &#8216;as&#8217;</p>
<dd>List of unauthenticated packages which are going to be installed.</p>
<dt><code>RemoveObsoletedDepends</code> read-write &#8216;b&#8217;</p>
<dd>If obsoleted dependencies of to be removed packages which have been installed automatically should be removed too.</p>
<dt><code>AllowUnauthenticated</code> read-write &#8216;b&#8217;</p>
<dd>If it is allowed to install not authenticated software packages.</p>
<dt><code>HttpProxy</code> read-write &#8216;s&#8217;</p>
<dd>The URL of an http proxy which should be used to download repository meta data and package files, e.g. <a rel="nofollow" href="http://myproxy.athome:8080.">http://myproxy.athome:8080.</a> You should set the system wide proxy if you use this feature regularly. <code>MetaData</code> read-write &#8216;a{ss}&#8217; A dictonary which allows client application to store additional data in the transaction. The key name has to include an identifier of the client application separated by an unterscore from the key name, e.g. sc_icon for the application icon name stored by software-center. The property cannot be changed anymore after the transaction has been queued.</dl>
<h2>Homepage</h2>
<p><a rel="nofollow" href="https://launchpad.net/aptdaemon">https://launchpad.net/aptdaemon</a></p>
<h2>Bugs</h2>
<p>You can report bugs at the Launchpad site of aptdaemon: <a rel="nofollow" href="https://bugs.launchpad.net/aptdaemon/+filebug">https://bugs.launchpad.net/aptdaemon/+filebug</a></p>
<h2>Author</h2>
<p>Sebastian Heinlein &lt;devel at glatzor dot de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-org-debian-apt-transaction/">org.debian.apt.transaction</a></code>(7), <code><a href="/docs/linux/man/2-aptd/">aptd</a></code>(2), <code><a href="/docs/linux/man/2-aptdcon/">aptdcon</a></code>(2) </p>
