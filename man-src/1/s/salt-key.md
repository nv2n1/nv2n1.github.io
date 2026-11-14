---
title: "salt-key(1)"
name: "salt-key"
section: "1"
letter: "s"
url: "/docs/linux/man/1-salt-key/"
description: "salt-key – salt-key Documentation"
---

<h2>NAME</h2>
<p> salt-key &#8211; salt-key Documentation</p>
<h2>SYNOPSIS</h2>
<pre>
salt-key [ options ]
</pre>
<h2>DESCRIPTION</h2>
<p> Salt-key executes simple management of Salt server public keys used for authentication. </p>
<p> On initial connection, a Salt minion sends its public key to the Salt master. This key must be accepted using the <code>salt-key</code> command on the Salt master. </p>
<p> Salt minion keys can be in one of the following states:</p>
<dl>
<dt>&bull;</p>
<dd> <code>unaccepted</code>: key is waiting to be accepted.</p>
<dt>&bull;</p>
<dd> <code>accepted</code>: key was accepted and the minion can communicate with the Salt master.</p>
<dt>&bull;</p>
<dd> <code>rejected</code>: key was rejected using the <code>salt-key</code> command. In this state the minion does not receive any communication from the Salt master.</p>
<dt>&bull;</p>
<dd> <code>denied</code>: key was rejected automatically by the Salt master. This occurs when a minion has a duplicate ID, or when a minion was rebuilt or had new keys generated and the previous key was not deleted from the Salt master. In this state the minion does not receive any communication from the Salt master. </p>
<p> To change the state of a minion key, use <code>-d</code> to delete the key and then accept or reject the key.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the version of Salt that is running.</p>
<dt><code>&#8211;versions-report</code></p>
<dd> Show program&#8217;s dependencies and version number, and then exit</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show the help message and exit</p>
<dt><code>-c CONFIG_DIR, &#8211;config-dir=CONFIG_dir</code></p>
<dd> The location of the Salt configuration directory. This directory contains the configuration files for Salt master and minions. The default location on most systems is <code>/etc/salt</code>.</p>
<dt><code>-u USER, &#8211;user=USER</code></p>
<dd> Specify user to run salt-key</p>
<dt><code>&#8211;hard-crash</code></p>
<dd> Raise any original exception rather than exiting gracefully. Default is False.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Suppress output</p>
<dt><code>-y, &#8211;yes</code></p>
<dd> Answer &#8216;Yes&#8217; to all questions presented, defaults to False</p>
<dt><code>&#8211;rotate-aes-key=ROTATE_AES_KEY</code></p>
<dd> Setting this to False prevents the master from refreshing the key session when keys are deleted or rejected, this lowers the security of the key deletion/rejection operation. Default is True.</dl>
<h3>Logging Options</h3>
<p> Logging options which override any settings defined on the configuration files.</p>
<dl>
<dt><code>&#8211;log-file=LOG_FILE</code></p>
<dd> Log file path. Default: /var/log/salt/minion.</p>
<dt><code>&#8211;log-file-level=LOG_LEVEL_LOGFILE</code></p>
<dd> Logfile logging log level. One of <code>all</code>, <code>garbage</code>, <code>trace</code>, <code>debug</code>, <code>info</code>, <code>warning</code>, <code>error</code>, <code>quiet</code>. Default: <code>warning</code>.</dl>
<h3>Output Options</h3>
<dl>
<dt><code>&#8211;out</code></p>
<dd> Pass in an alternative outputter to display the return of data. This outputter can be any of the available outputters: <code>grains</code>, <code>highstate</code>, <code>json</code>, <code>key</code>, <code>overstatestage</code>, <code>pprint</code>, <code>raw</code>, <code>txt</code>, <code>yaml</code> </p>
<p> Some outputters are formatted only for data returned from specific functions; for instance, the <code>grains</code> outputter will not work for non-grains data. </p>
<p> If an outputter is used that does not support the data passed into it, then Salt will fall back on the <code>pprint</code> outputter and display the return data using the Python <code>pprint</code> standard library module. </p>
<p> <code>NOTE:</code> If using <code>&#8211;out=json</code>, you will probably want <code>&#8211;static</code> as well. Without the static option, you will get a separate JSON string per minion which makes JSON output invalid as a whole. This is due to using an iterative outputter. So if you want to feed it to a JSON parser, use <code>&#8211;static</code> as well.</p>
<dt><code>&#8211;out-indent OUTPUT_INDENT, &#8211;output-indent OUTPUT_INDENT</code></p>
<dd> Print the output indented by the provided value in spaces. Negative values disable indentation. Only applicable in outputters that support indentation.</p>
<dt><code>&#8211;out-file=OUTPUT_FILE, &#8211;output-file=OUTPUT_FILE</code></p>
<dd> Write the output to the specified file.</p>
<dt><code>&#8211;no-color</code></p>
<dd> Disable all colored output</p>
<dt><code>&#8211;force-color</code></p>
<dd> Force colored output </p>
<p> <code>NOTE:</code> When using colored output the color codes are as follows: </p>
<p> <code>green</code> denotes success, <code>red</code> denotes failure, <code>blue</code> denotes changes and success and <code>yellow</code> denotes a expected future change in configuration.</dl>
<h3>Actions</h3>
<dl>
<dt><code>-l ARG, &#8211;list=ARG</code></p>
<dd> List the public keys. The args <code>pre</code>, <code>un</code>, and <code>unaccepted</code> will list unaccepted/unsigned keys. <code>acc</code> or <code>accepted</code> will list accepted/signed keys. <code>rej</code> or <code>rejected</code> will list rejected keys. Finally, <code>all</code> will list all keys.</p>
<dt><code>-L, &#8211;list-all</code></p>
<dd> List all public keys. (Deprecated: use <code>&#8211;list all</code>)</p>
<dt><code>-a ACCEPT, &#8211;accept=ACCEPT</code></p>
<dd> Accept the specified public key (use &#8211;include-all to match rejected keys in addition to pending keys). Globs are supported.</p>
<dt><code>-A, &#8211;accept-all</code></p>
<dd> Accepts all pending keys.</p>
<dt><code>-r REJECT, &#8211;reject=REJECT</code></p>
<dd> Reject the specified public key (use &#8211;include-all to match accepted keys in addition to pending keys). Globs are supported.</p>
<dt><code>-R, &#8211;reject-all</code></p>
<dd> Rejects all pending keys.</p>
<dt><code>&#8211;include-all</code></p>
<dd> Include non-pending keys when accepting/rejecting.</p>
<dt><code>-p PRINT, &#8211;print=PRINT</code></p>
<dd> Print the specified public key.</p>
<dt><code>-P, &#8211;print-all</code></p>
<dd> Print all public keys</p>
<dt><code>-d DELETE, &#8211;delete=DELETE</code></p>
<dd> Delete the specified key. Globs are supported.</p>
<dt><code>-D, &#8211;delete-all</code></p>
<dd> Delete all keys.</p>
<dt><code>-f FINGER, &#8211;finger=FINGER</code></p>
<dd> Print the specified key&#8217;s fingerprint.</p>
<dt><code>-F, &#8211;finger-all</code></p>
<dd> Print all keys&#8217; fingerprints.</dl>
<h3>Key Generation Options</h3>
<dl>
<dt><code>&#8211;gen-keys=GEN_KEYS</code></p>
<dd> Set a name to generate a keypair for use with salt</p>
<dt><code>&#8211;gen-keys-dir=GEN_KEYS_DIR</code></p>
<dd> Set the directory to save the generated keypair. Only works with &#8216;gen_keys_dir&#8217; option; default is the current directory.</p>
<dt><code>&#8211;keysize=KEYSIZE</code></p>
<dd> Set the keysize for the generated key, only works with the &#8216;&#8211;gen-keys&#8217; option, the key size must be 2048 or higher, otherwise it will be rounded up to 2048. The default is 2048.</p>
<dt><code>&#8211;gen-signature</code></p>
<dd> Create a signature file of the masters public-key named master_pubkey_signature. The signature can be send to a minion in the masters auth-reply and enables the minion to verify the masters public-key cryptographically. This requires a new signing-key- pair which can be auto-created with the &#8211;auto-create parameter.</p>
<dt><code>&#8211;priv=PRIV</code></p>
<dd> The private-key file to create a signature with</p>
<dt><code>&#8211;signature-path=SIGNATURE_PATH</code></p>
<dd> The path where the signature file should be written</p>
<dt><code>&#8211;pub=PUB</code></p>
<dd> The public-key file to create a signature for</p>
<dt><code>&#8211;auto-create</code></p>
<dd> Auto-create a signing key-pair if it does not yet exist</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-salt/">salt</a>(7)</i> <i><a href="/docs/linux/man/1-salt-master/">salt-master</a>(1)</i> <i><a href="/docs/linux/man/1-salt-minion/">salt-minion</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> Thomas S. Hatch &lt;thatch45 [at] gmail.com&gt; and many others, please see the Authors file</p>
<h2>COPYRIGHT</h2>
<p> 2016 SaltStack, Inc. </p>
<h2>Index</h2>
