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
<dt>&bull;</dt>
<dd> <code>unaccepted</code>: key is waiting to be accepted.</dd>
<dt>&bull;</dt>
<dd> <code>accepted</code>: key was accepted and the minion can communicate with the Salt master.</dd>
<dt>&bull;</dt>
<dd> <code>rejected</code>: key was rejected using the <code>salt-key</code> command. In this state the minion does not receive any communication from the Salt master.</dd>
<dt>&bull;</dt>
<dd> <code>denied</code>: key was rejected automatically by the Salt master. This occurs when a minion has a duplicate ID, or when a minion was rebuilt or had new keys generated and the previous key was not deleted from the Salt master. In this state the minion does not receive any communication from the Salt master. </dd>
<p> To change the state of a minion key, use <code>-d</code> to delete the key and then accept or reject the key.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Print the version of Salt that is running.</dd>
<dt><code>&#8211;versions-report</code></dt>
<dd> Show program&#8217;s dependencies and version number, and then exit</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show the help message and exit</dd>
<dt><code>-c CONFIG_DIR, &#8211;config-dir=CONFIG_dir</code></dt>
<dd> The location of the Salt configuration directory. This directory contains the configuration files for Salt master and minions. The default location on most systems is <code>/etc/salt</code>.</dd>
<dt><code>-u USER, &#8211;user=USER</code></dt>
<dd> Specify user to run salt-key</dd>
<dt><code>&#8211;hard-crash</code></dt>
<dd> Raise any original exception rather than exiting gracefully. Default is False.</dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> Suppress output</dd>
<dt><code>-y, &#8211;yes</code></dt>
<dd> Answer &#8216;Yes&#8217; to all questions presented, defaults to False</dd>
<dt><code>&#8211;rotate-aes-key=ROTATE_AES_KEY</code></dt>
<dd> Setting this to False prevents the master from refreshing the key session when keys are deleted or rejected, this lowers the security of the key deletion/rejection operation. Default is True.</dd></dl>
<h3>Logging Options</h3>
<p> Logging options which override any settings defined on the configuration files.</p>
<dl>
<dt><code>&#8211;log-file=LOG_FILE</code></dt>
<dd> Log file path. Default: /var/log/salt/minion.</dd>
<dt><code>&#8211;log-file-level=LOG_LEVEL_LOGFILE</code></dt>
<dd> Logfile logging log level. One of <code>all</code>, <code>garbage</code>, <code>trace</code>, <code>debug</code>, <code>info</code>, <code>warning</code>, <code>error</code>, <code>quiet</code>. Default: <code>warning</code>.</dd></dl>
<h3>Output Options</h3>
<dl>
<dt><code>&#8211;out</code></dt>
<dd> Pass in an alternative outputter to display the return of data. This outputter can be any of the available outputters: <code>grains</code>, <code>highstate</code>, <code>json</code>, <code>key</code>, <code>overstatestage</code>, <code>pprint</code>, <code>raw</code>, <code>txt</code>, <code>yaml</code> </dd>
<p> Some outputters are formatted only for data returned from specific functions; for instance, the <code>grains</code> outputter will not work for non-grains data. </p>
<p> If an outputter is used that does not support the data passed into it, then Salt will fall back on the <code>pprint</code> outputter and display the return data using the Python <code>pprint</code> standard library module. </p>
<p> <code>NOTE:</code> If using <code>&#8211;out=json</code>, you will probably want <code>&#8211;static</code> as well. Without the static option, you will get a separate JSON string per minion which makes JSON output invalid as a whole. This is due to using an iterative outputter. So if you want to feed it to a JSON parser, use <code>&#8211;static</code> as well.</p>
<dt><code>&#8211;out-indent OUTPUT_INDENT, &#8211;output-indent OUTPUT_INDENT</code></dt>
<dd> Print the output indented by the provided value in spaces. Negative values disable indentation. Only applicable in outputters that support indentation.</dd>
<dt><code>&#8211;out-file=OUTPUT_FILE, &#8211;output-file=OUTPUT_FILE</code></dt>
<dd> Write the output to the specified file.</dd>
<dt><code>&#8211;no-color</code></dt>
<dd> Disable all colored output</dd>
<dt><code>&#8211;force-color</code></dt>
<dd> Force colored output </dd>
<p> <code>NOTE:</code> When using colored output the color codes are as follows: </p>
<p> <code>green</code> denotes success, <code>red</code> denotes failure, <code>blue</code> denotes changes and success and <code>yellow</code> denotes a expected future change in configuration.</dl>
<h3>Actions</h3>
<dl>
<dt><code>-l ARG, &#8211;list=ARG</code></dt>
<dd> List the public keys. The args <code>pre</code>, <code>un</code>, and <code>unaccepted</code> will list unaccepted/unsigned keys. <code>acc</code> or <code>accepted</code> will list accepted/signed keys. <code>rej</code> or <code>rejected</code> will list rejected keys. Finally, <code>all</code> will list all keys.</dd>
<dt><code>-L, &#8211;list-all</code></dt>
<dd> List all public keys. (Deprecated: use <code>&#8211;list all</code>)</dd>
<dt><code>-a ACCEPT, &#8211;accept=ACCEPT</code></dt>
<dd> Accept the specified public key (use &#8211;include-all to match rejected keys in addition to pending keys). Globs are supported.</dd>
<dt><code>-A, &#8211;accept-all</code></dt>
<dd> Accepts all pending keys.</dd>
<dt><code>-r REJECT, &#8211;reject=REJECT</code></dt>
<dd> Reject the specified public key (use &#8211;include-all to match accepted keys in addition to pending keys). Globs are supported.</dd>
<dt><code>-R, &#8211;reject-all</code></dt>
<dd> Rejects all pending keys.</dd>
<dt><code>&#8211;include-all</code></dt>
<dd> Include non-pending keys when accepting/rejecting.</dd>
<dt><code>-p PRINT, &#8211;print=PRINT</code></dt>
<dd> Print the specified public key.</dd>
<dt><code>-P, &#8211;print-all</code></dt>
<dd> Print all public keys</dd>
<dt><code>-d DELETE, &#8211;delete=DELETE</code></dt>
<dd> Delete the specified key. Globs are supported.</dd>
<dt><code>-D, &#8211;delete-all</code></dt>
<dd> Delete all keys.</dd>
<dt><code>-f FINGER, &#8211;finger=FINGER</code></dt>
<dd> Print the specified key&#8217;s fingerprint.</dd>
<dt><code>-F, &#8211;finger-all</code></dt>
<dd> Print all keys&#8217; fingerprints.</dd></dl>
<h3>Key Generation Options</h3>
<dl>
<dt><code>&#8211;gen-keys=GEN_KEYS</code></dt>
<dd> Set a name to generate a keypair for use with salt</dd>
<dt><code>&#8211;gen-keys-dir=GEN_KEYS_DIR</code></dt>
<dd> Set the directory to save the generated keypair. Only works with &#8216;gen_keys_dir&#8217; option; default is the current directory.</dd>
<dt><code>&#8211;keysize=KEYSIZE</code></dt>
<dd> Set the keysize for the generated key, only works with the &#8216;&#8211;gen-keys&#8217; option, the key size must be 2048 or higher, otherwise it will be rounded up to 2048. The default is 2048.</dd>
<dt><code>&#8211;gen-signature</code></dt>
<dd> Create a signature file of the masters public-key named master_pubkey_signature. The signature can be send to a minion in the masters auth-reply and enables the minion to verify the masters public-key cryptographically. This requires a new signing-key- pair which can be auto-created with the &#8211;auto-create parameter.</dd>
<dt><code>&#8211;priv=PRIV</code></dt>
<dd> The private-key file to create a signature with</dd>
<dt><code>&#8211;signature-path=SIGNATURE_PATH</code></dt>
<dd> The path where the signature file should be written</dd>
<dt><code>&#8211;pub=PUB</code></dt>
<dd> The public-key file to create a signature for</dd>
<dt><code>&#8211;auto-create</code></dt>
<dd> Auto-create a signing key-pair if it does not yet exist</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-salt/">salt</a>(7)</i> <i><a href="/docs/linux/man/1-salt-master/">salt-master</a>(1)</i> <i><a href="/docs/linux/man/1-salt-minion/">salt-minion</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> Thomas S. Hatch &lt;thatch45 [at] gmail.com&gt; and many others, please see the Authors file</p>
<h2>COPYRIGHT</h2>
<p> 2016 SaltStack, Inc. </p>
