---
title: "otr_toolkit(1)"
name: "otr_toolkit"
section: "1"
letter: "o"
url: "/docs/linux/man/1-otr_toolkit/"
description: "otr_parse, otr_sesskeys, otr_mackey, otr_readforge, otr_modify, otr_remac – Process Off-the-Record Messaging transcripts"
---

<h2 class="name">NAME</h2>
<p> otr_parse, otr_sesskeys, otr_mackey, otr_readforge, otr_modify, otr_remac &#8211; Process Off-the-Record Messaging transcripts </p>
<h2>SYNOPSIS</h2>
<p> <code>otr_parse</code><br />
 <code>otr_sesskeys</code> <i>our_privkey their_pubkey</i><br />
 <code>otr_mackey</code> <i>aes_enc_key</i><br />
 <code>otr_readforge</code> <i>aes_enc_key [newmsg]</i><br />
 <code>otr_modify</code> <i>mackey old_text new_text offset</i><br />
 <code>otr_remac</code> <i>mackey sender_instance receiver_instance flags snd_keyid rcv_keyid pubkey counter encdata revealed_mackeys</i></p>
<h2>DESCRIPTION</h2>
<p> Off-the-Record (OTR) Messaging allows you to have private conversations over IM by providing:<br />
&nbsp;<wbr>&#8211; Encryption<br />
&#8211; No one else can read your instant messages.<br />
&nbsp;<wbr>&#8211; Authentication<br />
&#8211; You are assured the correspondent is who you think it is.<br />
&nbsp;<wbr>&#8211; Deniability<br />
&#8211; The messages you send do&nbsp;<wbr><i>not</i>&nbsp;<wbr>have digital signatures that are<br />
&nbsp;<wbr>&nbsp;<wbr>checkable by a third party.&nbsp;<wbr>&nbsp;<wbr>Anyone can forge messages after a<br />
&nbsp;<wbr>&nbsp;<wbr>conversation to make them look like they came from you.&nbsp;<wbr>&nbsp;<wbr>However,<br />
&nbsp;<wbr>&nbsp;<wbr><i>during</i>&nbsp;<wbr>a conversation, your correspondent is assured the messages<br />
&nbsp;<wbr>&nbsp;<wbr>he sees are authentic and unmodified.<br />
&nbsp;<wbr>&#8211; Perfect forward secrecy<br />
&#8211; If you lose control of your private keys, no previous conversation<br />
&nbsp;<wbr>&nbsp;<wbr>is compromised. </p>
<p> The OTR Toolkit is useful for analyzing and/or forging OTR messages. Why do we offer this? Primarily, to make absolutely sure that transcripts of OTR conversations are really easy to forge after the fact. [Note that <i>during</i> an OTR conversation, messages can&#8217;t be forged without real-time access to the secret keys on the participants&#8217; computers, and in that case, all security has already been lost.] Easily-forgeable transcripts help us provide the &quot;Deniability&quot; property: if someone claims you said something over OTR, they&#8217;ll have no proof, as anyone at all can modify a transcript to make it say whatever they like, and still have all the verification come out correctly. </p>
<p> Here are the six programs in the toolkit: </p>
<p>&nbsp;<wbr>&#8211; otr_parse<br />
&#8211; Parse OTR messages given on stdin, showing the values of all the<br />
&nbsp;<wbr>&nbsp;<wbr>fields in OTR protocol messages. </p>
<p>&nbsp;<wbr>&#8211; otr_sesskeys our_privkey their_pubkey<br />
&#8211; Shows our public key, the session id, two AES and two MAC keys<br />
&nbsp;<wbr>&nbsp;<wbr>derived from the given Diffie-Hellman keys&nbsp;<wbr>(one private, one public). </p>
<p>&nbsp;<wbr>&#8211; otr_mackey aes_enc_key<br />
&#8211; Shows the MAC key derived from the given AES key. </p>
<p>&nbsp;<wbr>&#8211; otr_readforge aes_enc_key&nbsp;<wbr>[newmsg]<br />
&#8211; Decrypts an OTR Data message using the given AES key, and displays<br />
&nbsp;<wbr>&nbsp;<wbr>the message.<br />
&#8211; If newmsg is given, replace the message with that one, encrypt<br />
&nbsp;<wbr>&nbsp;<wbr>and MAC it properly, and output the resulting OTR Data Message.<br />
&nbsp;<wbr>&nbsp;<wbr>This works even if the given key was not correct for the original<br />
&nbsp;<wbr>&nbsp;<wbr>message, so as to enable complete forgeries. </p>
<p>&nbsp;<wbr>&#8211; otr_modify mackey old_text new_text offset<br />
&#8211; Even if you can&#8217;t read the data because you don&#8217;t know either<br />
&nbsp;<wbr>&nbsp;<wbr>the AES key or the Diffie-Hellman private key, but you can make a<br />
&nbsp;<wbr>&nbsp;<wbr>good guess that the substring&nbsp;<wbr>&quot;old_text&quot;&nbsp;<wbr>appears at the given<br />
&nbsp;<wbr>&nbsp;<wbr>offset in the message, replace the old_text with the new_text<br />
&nbsp;<wbr>&nbsp;<wbr>(which must be of the same length), recalculate the MAC with the<br />
&nbsp;<wbr>&nbsp;<wbr>given mackey, and output the resulting Data message.<br />
&#8211; Note that, even if you don&#8217;t know any text in an existing message,<br />
&nbsp;<wbr>&nbsp;<wbr>you can still forge messages of your choice using the<br />
&nbsp;<wbr>&nbsp;<wbr>otr_readforge command, above. </p>
<p>&nbsp;<wbr>&#8211; otr_remac mackey sender_instance receiver_instance flags snd_keyid rcv_keyid pubkey counter encdata revealed_mackeys<br />
&#8211; Make a new OTR protocol version 3 Data Message, with the given<br />
&nbsp;<wbr>&nbsp;<wbr>pieces&nbsp;<wbr>(note that the data part is already encrypted).&nbsp;<wbr>&nbsp;<wbr>MAC it&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>with the given mackey. </p>
<h2>SEE ALSO</h2>
<p> <code>Off-the-Record Messaging</code>, at <a rel="nofollow" href="https://www.cypherpunks.ca/otr/">https://www.cypherpunks.ca/otr/</a></p>
<h2>AUTHOR</h2>
<p> otr_toolkit was written by the OTR Dev Team &lt;otr [at] cypherpunks.ca&gt;. </p>
<h2>Index</h2>
