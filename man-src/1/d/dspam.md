---
title: "dspam(1)"
name: "dspam"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dspam/"
description: "dspam – DSPAM Anti-Spam Agent"
---

<h2 class="name">NAME</h2>
<p> dspam &#8211; DSPAM Anti-Spam Agent</p>
<h2>SYNOPSIS</h2>
<p> <code>dspam</code> [<code>&#8211;mode=</code><i>teft|toe|tum|notrain|unlearn</i>] [<code>&#8211;user</code><i>&nbsp;<wbr>user1</i> user2 &#8230; userN] [<code>&#8211;feature=</code><i>noise|no,tb=N,whitelist|wh</i>] [<code>&#8211;class=</code><i>spam|innocent</i>] [<code>&#8211;source=</code><i>error|corpus|inoculation</i>] [<code>&#8211;profile=</code><i>PROFILE</i>] [<code>&#8211;deliver=</code><i>spam,innocent|nonspam,summary,stdout</i>] [<code>&#8211;help</code>] [<code>&#8211;version</code>] [<code>&#8211;process</code>] [<code>&#8211;classify</code>] [<code>&#8211;signature=</code><i>signature</i>] [<code>&#8211;stdout</code>] [<code>&#8211;debug</code>] [<code>&#8211;daemon</code>] [<code>&#8211;nofork</code>]] [<code>&#8211;client</code>] [<code>&#8211;rcpt-to</code><i>&nbsp;<wbr>recipient-address(es)</i>] [<code>&#8211;mail-from=</code><i>sender-address</i>] [<code>passthru-delivery-arguments</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>The DSPAM agent </code> provides a direct interface to mail servers for command-line spam filtering. The agent can masquerade as the mail server&#8217;s local delivery agent and will process any email passed to it. The agent will then call whatever delivery agent was specified at compile time or quarantine/tag/drop messages identified as spam. The DSPAM agent can function locally or as a proxy. It is also responsible for processing classification errors so that DSPAM can learn from its mistakes. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;user</code><i>&nbsp;<wbr>user1</i>&nbsp;<wbr>user2 &#8230; userN</p>
<dd> Specifies the destination users of the incoming message. In most cases this is the local user on the system, however some implementations may call for virtual usernames, specific to DSPAM, to be assigned. The agent processes an incoming message once for each user specified. If the message is to be delivered, the $u (or %u) parameters of the argument string will be interpolated for the current user being processed.<br />
&nbsp;<wbr></p>
<dt><code>&#8211;mode=</code><i>toe|tum|teft|notrain</i></p>
<dd> Configures the training mode to be used for this process, overriding any defaults in dspam.conf or the preference extension: </p>
<p> <code>teft</code> : Train-Everything. Trains on all messages processed. This is a very thorough training approach and should be considered the standard training approach for most users. TEFT may, however, prove too volatile on installations with extremely high per-user traffic, or prove not very scalable on systems with extremely large user-bases. In the event that TEFT is proving ineffective, one of the other modes is recommended. </p>
<p> <code>toe</code> : Train-on-Error. Trains only on a classification error, once the user&#8217;s metadata has matured to 2500 innocent messages. This training mode is much less resource intensive, as only occasional metadata writes are necessary. It is also far less volatile than the TEFT mode of training. One drawback, however, is that TOE only learns when DSPAM has made a mistake &#8211; which means the data is sometimes too static, and unable to &quot;ease into&quot; a different type of behavior. </p>
<p> <code>tum</code> : Train-until-Mature. This training mode is a hybrid between the other two training modes and provides a great balance between volatility and static metadata. TuM will train on a per-token basis only tokens which have had fewer than 25 &quot;hits&quot; on them, unless an error is being retrained in which case all tokens are trained. This training mode provides a solid core of stable tokens to keep accuracy consistent, but also allows for dynamic adaptation to any new types of email behavior a user might be experiencing. </p>
<p> <code>notrain</code> : No training. Do not train the user&#8217;s data, and do not keep totals. This should only be used in cases where you want to process mail for a particular user (based on a group, for example), but don&#8217;t want the user to accumulate any learning data. </p>
<p> <code>unlearn</code> : Unlearn original training. Use this if you wish to unlearn a previously learned message. Be sure to specify <code>&#8211;source=error</code> and <code>&#8211;class</code> to whatever the original classification the message was learned under. If not using TrainPristine, this will require the original signature from training. </p>
<dt><code>&#8211;feature=</code><i>noise|no,whitelist|wh,tb=N</i></p>
<dd> Specifies the features that should be activated for this filter instance. The following features may be used individually or combined using a comma as a delimiter: </p>
<p> <code>(no)ise</code> : Bayesian Noise Reduction (BNR). Bayesian Noise Reduction kicks in at 2500 innocent messages and provides an advanced progressive noise logic to reduce Bayesian Noise (wordlist attacks) in spams. See <a rel="nofollow" href="http://www.zdziarski.com/papers/bnr.html">http://www.zdziarski.com/papers/bnr.html</a> for more information. </p>
<p> <code>(tb)=N</code> : Sets the training loop buffering level. Training loop buffering is the amount of statistical sedation performed to water down statistics and avoid false positives during the user&#8217;s training loop. The training buffer sets the buffer sensitivity, and should be a number between 0 (no buffering whatsoever) to 10 (heavy buffering). The default is 5, half of what previous versions of DSPAM used. To avoid dulling down statistics at all during the training loop, set this to 0. </p>
<p> <code>(wh)itelist</code> : Automatic whitelisting. DSPAM will keep track of the entire &quot;From:&quot; line for each message received per user, and automatically whitelist messages from senders with more than 20 innocent messages and zero spams. Once the user reports a spam from the sender, automatic whitelisting will automatically be deactivated for that sender. Since DSPAM uses the entire &quot;From:&quot; line, and not just the sender&#8217;s email address, automatic whitelisting is a very safe approach to improving accuracy especially during initial training. </p>
<p> <code>NOTE:</code> : None of the present features are necessary when the source is &quot;error&quot;, because the original training data is used from the signature to retrain, instantiating whatever features (such as whitelisting) were active at the time of the initial classification. Since BNR is only necessary when a message is being classified, the <code>&#8211;feature</code> flag can be safely omitted from error source calls. </p>
<dt><code>&#8211;class=</code><i>spam|innocent</i></p>
<dd> Identifies the disposition (if any) of the message being presented. This flag should be used when a misclassification has occured, when the user is corpus-feeding a message, or when an inoculation is being presented. This flag should not be used for standard processing. This flag must be used in conjunction with the <code>&#8211;source</code> flag. Omitting this flag causes DSPAM to determine the disposition of the message on its own (the standard operating mode).<br />
&nbsp;<wbr></p>
<dt><code>&#8211;source=</code><i>error|corpus|inoculation</i></p>
<dd> Where <code>&#8211;class</code> is used, the source of the classification must also be provided. The source tells dspam how to learn the message being presented:<br />
&nbsp;<wbr> <code>error</code> : The message being presented was a message previously misclassified by DSPAM. When &#8216;error&#8217; is provided as a source, DSPAM requires that the DSPAM signature be present in the message, and will use the signature to recall the original training metadata. If the signature is not present, the message will be rejected. In this source mode, DSPAM will also decrement each token&#8217;s previous classification&#8217;s count as well as the user totals. </p>
<p> You should use error only when DSPAM has made an error in classifying the message, and should present the modified version of the message with the DSPAM signature when doing so. </p>
<p> <code>corpus</code> : The message being presented is from a mail corpus, and should be trained as a new message, rather than re-trained based on a signature. The message&#8217;s full headers and body will be analyzed and the correct classification will be incremented, without its opposite being decremented. </p>
<p> You should use corpus only when feeding messages in from corpus.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <code>inoculation</code> : The message being presented is in pristine form, and should be trained as an inoculation. Inoculations are a more intense mode of training designed to cause DSPAM to train the user&#8217;s metadata repeatedly on previoulsy unknown tokens, in an attempt to vaccinate the user from future messages similar to the one being presented. You should use inoculation only on honeypots and the like. </p>
<dt><code>&#8211;profile=</code><i>PROFILE</i></p>
<dd> Specify a storage profile from dspam.conf. The storage profile selected will be used for all database connectivity. See dspam.conf for more information. </p>
<dt><code>&#8211;deliver=</code><i>spam,innocent|nonspam,summary,stdout</i></p>
<dd> Tells <code>DSPAM</code> to deliver the message if its result falls within the criteria specified. For example, <code>&#8211;deliver=innocent</code> or <code>&#8211;deliver=nonspam</code> will cause DSPAM to only deliver the message if its classification has been determined as innocent. Providing <code>&#8211;deliver=innocent,spam</code> or <code>&#8211;deliver=nonspam,spam</code> will cause DSPAM to deliver the message regardless of its classification. This flag provides a significant amount of flexibility for nonstandard implementations, where false positives may not be delivered but spam is, and etcetera. </p>
<p> <code>summary</code> : Deliver (to stdout) a summary indentical to the output of message classification: </p>
<p> X-DSPAM-Result: User; result=&quot;Innocent&quot;; class=&quot;Innocent&quot;; probability=0.0000; confidence=1.00; signature=4b11c532158749980119923 </p>
<p> <code>stdout</code> : Is a shortcut for for <code>&#8211;deliver=innocent,spam &#8211;stdout</code> </p>
<dt><code>&#8211;stdout </code></p>
<dd> If the message is indeed deemed &quot;deliverable&quot; by the <code>&#8211;deliver</code> flag, this flag will cause DSPAM to deliver the message to stdout, rather than the configured delivery agent. </p>
<dt><code>&#8211;process</code></p>
<dd> Tells <code>DSPAM</code> to process the message. This is the default behavior, and the flag is implied unless <code>&#8211;classify</code> is used. </p>
<dt><code>&#8211;classify</code></p>
<dd> Tells <code>DSPAM</code> to only classify the message, and not perform any writes to the user&#8217;s data or attempt to deliver/quarantine the message. The results of a classification are printed to stdout in the following format: </p>
<p> X-DSPAM-Result: User; result=&quot;Spam&quot;; probability=1.0000; confidence=0.80 </p>
<p> <code>NOTE</code> : The output of the classification is specific to a user&#8217;s own data, and does not include the output of any groups they might be affiliated with, so it is entirely possible that the message would be caught as spam by a group the user belongs to, and appear as innocent in the output of a classification. To get the classification for the <code>group</code> , use the group name as the user instead of an individual. </p>
<dt><code>&#8211;signature=</code><i>signature</i></p>
<dd> If only the signature is available for training, and not the entire message, the <code>&#8211;signature</code> flag may be used to feed the signature into DSPAM and forego the reading of stdin. DSPAM will process the signature with whatever commandline classification was specified. </p>
<p> <code>NOTE</code> : This should only be used with <code>&#8211;source=error</code> </p>
<dt><code>&#8211;debug</code></p>
<dd> If <code>DSPAM</code> was compiled with <code>&#8211;enable-debug</code> then using <code>&#8211;debug</code> will turn on debugging messages. </p>
<dt><code>&#8211;daemon</code></p>
<dd> If <code>DSPAM</code> was compiled with <code>&#8211;enable-daemon</code> then using <code>&#8211;daemon</code> will cause DSPAM to enter daemon mode, where it will listen for DSPAM clients to connect and actively service requests. </p>
<dt><code>&#8211;nofork</code></p>
<dd> If <code>DSPAM</code> was compiled with <code>&#8211;enable-daemon</code> then using <code>&#8211;nofork</code> will cause DSPAM to not fork the daemon into backgound when using <code>&#8211;daemon</code> switch. </p>
<dt><code>&#8211;client</code></p>
<dd> If <code>DSPAM</code> was compiled with <code>&#8211;enable-daemon</code> then using <code>&#8211;client</code> will cause DSPAM to act as a client and attempt to connect to the DSPAM server specified in the client&#8217;s configuration within dspam.conf. If client behavior is desired, this option <code>must</code> be specified, otherwise the agent simply operate as self-contained and processes the message on its own, eliminating any benefit of using the daemon. </p>
<dt><code>&#8211;rcpt-to</code><i>&nbsp;<wbr>recipient-address(es)</i></p>
<dd> If <code>DSPAM</code> will be configured to deliver via LMTP or SMTP, this flag may be used to define the RCPT TOs which will be used for the delivery of each user specified with <code>&#8211;user</code> If no recipients are provided, the RCPT TOs will match the username. </p>
<p> <code>NOTE</code> : The recipient list should always be balanced with the user list, or empty. Specifying an unbalanced number of recipients to users will result in undefined behavior. </p>
<dt><code>&#8211;mail-from=</code><i>sender-address</i></p>
<dd> If <code>DSPAM</code> will be cofigured to deliver via LMTP or SMTP, this flag will set the MAIL FROM sent on delivery of the message. The default MAIL FROM depends on how the message was originally relayed to DSPAM. If it was relayed via the commandline, an empty MAIL FROM will be used. If it was relayed via LMTP, the original MAIL FROM will be used. </p>
</dl>
<h2>EXIT VALUE</h2>
<dl>
<dt><code>0</code></p>
<dd> Operation was successful.</p>
<dt><code>other</code></p>
<dd> Operation resulted in an error. If the error involved an error in calling the delivery agent, the exit value of the delivery agent will be returned. </p>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2012 DSPAM Project<br />
 All rights reserved. </p>
<p> For more information, see <a rel="nofollow" href="http://dspam.sourceforge.net.">http://dspam.sourceforge.net.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dspam_admin/">dspam_admin</a></code>(1), <code><a href="/docs/linux/man/1-dspam_clean/">dspam_clean</a></code>(1), <code><a href="/docs/linux/man/1-dspam_crc/">dspam_crc</a></code>(1), <code><a href="/docs/linux/man/1-dspam_dump/">dspam_dump</a></code>(1), <code><a href="/docs/linux/man/1-dspam_logrotate/">dspam_logrotate</a></code>(1), <code><a href="/docs/linux/man/1-dspam_merge/">dspam_merge</a></code>(1), <code><a href="/docs/linux/man/1-dspam_stats/">dspam_stats</a></code>(1), <code><a href="/docs/linux/man/1-dspam_train/">dspam_train</a></code>(1) </p>
<h2>Index</h2>
